---
name: Ntopng
description: Monitorování sítě pomocí ntopng
---
![cover](assets/cover.webp)



___



*Tento návod vychází z původního obsahu Floriana Duchemina publikovaného na stránkách [IT-Connect](https://www.it-connect.fr/). Licence [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). V původním textu mohly být provedeny změny.*



___



## I. Prezentace



**Monitorování síťových toků je důležitou součástí podnikové sítě**, ať už jde o kontrolu plynulosti sítě, získání jasného přehledu o využití nebo statistiky výkonu. Pomáhá předvídat změny v infrastruktuře a pomáhá zajistit kvalitu používání pro uživatele (známá také jako QoE pro *Quality of Experience*, na rozdíl od QoS).



K tomu existuje mnoho technik a softwaru/protokolů. Například Netflow, vyvinutý společností Cisco, lze použít k získání statistik IP toků z Interface, ale jeho použití je omezeno na kompatibilní zařízení.



Proto vám v tomto tutoriálu představím službu **Ntop** a ukážu vám, jak ji použít ve vaší infrastruktuře, abyste měli přehled o využití sítě.



Ntop je software s otevřeným zdrojovým kódem, který lze nainstalovat na libovolný počítač se systémem Linux. Je zdarma a dokáže shromažďovat následující údaje:





- Využití šířky pásma
- Hlavní zákazníci
- Hlavní destinace
- Použité protokoly
- Použité aplikace
- Použité porty
- Atd.



Nyní je přejmenován na **Ntopng (New Generation)** a nabízí mnoho základních funkcí zdarma. K dispozici je také komerční verze, která umožňuje exportovat nakonfigurované výstrahy do softwaru typu SIEM nebo filtrovat provoz pomocí pravidel definovaných přímo ze sondy.



## II. Předpoklady



Instalace sondy Ntop se liší v závislosti na zařízení a prostředí. Nebudu vám zde proto předkládat návod krok za krokem, ale nastíním různé možnosti.



### A. Palubní režim



Pokud máte ve výrobě firewall pfSense, OPNSense nebo Endian nebo dokonce pracovní stanici Linux s NFTables, dobrá zpráva! Můžete si nainstalovat přímo Ntopng a začít monitorovat svá rozhraní.



Výhodou této techniky je, že nevyžaduje žádný další hardware. Na druhou stranu zvyšuje využití prostředků, takže se ujistěte, že máte k dispozici odpovídající hardware nebo dostatečně velký virtuální počítač (minimálně 2 jádra a 2 GB RAM).



### B. Režim TAP / SPAN



**Tap** je **síťové zařízení, které duplikuje provoz, který jím prochází, a odesílá jej do jiného zařízení.** Výhodou tohoto zařízení je, že nevyžaduje žádné úpravy stávající infrastruktury a může být umístěno kdekoli, aby monitorovalo konkrétní úseky sítě, nebo mezi hlavním přepínačem a okrajovým směrovačem, aby analyzovalo provoz do/z internetu.



Velkou nevýhodou tohoto typu zařízení je jeho cena. V dnešních gigabitových sítích nemůže pasivní odposlech správně zachytit síťový provoz, takže potřebujete aktivní zařízení, které stojí kolem 200 eur (minimálně).



Režim **SPAN**, známý také jako **zrcadlení portu**, používá přepínač k předávání přenosů z jednoho portu na druhý. Tuto metodu zdaleka preferuji, protože je jednoduchá na nastavení a stejně jako odposlech umožňuje sledovat část sítě nebo celou síť podle libosti. Má však dvě nevýhody: přepínač musí tuto funkci integrovat a její použití může zvýšit zatížení procesoru přepínače.



### C. Režim směrovače



Pod Linuxem je možné připojit směrovač a nainstalovat na něj ntopng. Jedinou nevýhodou této metody je, že se změní vaše síť, buď její vnitřní adresování, nebo adresování mezi vaším "skutečným" směrovačem a tím, který přidáváte.



Poznámka: pro čtenáře článku [Vytvořit Wifi router s Raspberry Pi a RaspAP](https://www.it-connect.fr/creer-un-routeur-wifi-avec-un-raspberry-pi-et-raspap/) je to naprosto možné nainstalovat ntopng na Rpi získat přesné statistiky!



### D. Režim mostu



Zajímavou alternativou je použití **počítače se systémem Linux v režimu mostu.** Umístěný mezi dvěma zařízeními umožňuje zachytit veškerý provoz, aniž by bylo nutné zasahovat do konfigurace infrastruktury nebo jejího vybavení. Vzhledem k tomu, že tuto práci může vykonávat starý stroj, může být tato metoda atraktivní i z hlediska nákladů. Všimněte si, že aby bylo zařízení optimální, mělo by mít tři síťové karty, dvě v režimu bridge a jednu pro přístup ke Interface a SSH. Je možné použít pouze dvě karty, ale pak bude zachycen i provoz správy zařízení...



Proto použiji **tento poslední režim**. Z praktických důvodů budu pro ukázku používat virtuální počítače, ale metoda zůstává stejná i pro použití na fyzických počítačích.



## III. Příprava sondy s můstkem Interface



Pro sondu jsem zvolil počítač **Debian 11** v minimální instalaci.



První krok je vždy stejný, aktualizujte:



```
apt-get update && apt-get upgrade
```



Poté nainstalujte balíček **bridge-utils**, který nám umožní vytvořit náš most:



```
apt-get install bridge-utils
```



Po instalaci si nejprve všimněte aktuálního názvu našich síťových karet. V Debianu může mít tento název několik podob a my ho budeme potřebovat pro konfiguraci.



Jednoduchý příkaz **ip add** vrátí výstup s těmito informacemi:



![Image](assets/fr/016.webp)



Zde vidím 3 rozhraní:





- Lo**: jedná se o zpětnou smyčku Interface; je to virtuální Interface, která "smyčkuje" přes zařízení. V podstatě se tento Interface, jehož Address je 127.0.0.1 (ačkoli stačí jakýkoli Address v rozsahu 127.0.0.0/8, protože tento rozsah je pro tento účel vyhrazen), používá ke kontaktu se samotným zařízením. Pokud jste nainstalovali webovou stránku na své pracovní stanici (například pomocí WAMPP), pravděpodobně jste použili "*localhost*" Address někdy zobrazit web hostovaný na vašem vlastním počítači. Tento název hostitele je spojen s adresou Address 127.0.0.1, a tedy se zpětnou smyčkou Interface.
- ens33**: toto je můj první Interface, který zde obdržel Address od mého DHCP
- ens36**: můj druhý Interface



Nyní, když mám všechny informace, mohu upravit soubor */etc/network/interfaces* a vytvořit můstek. Takto vypadá v současné době (může se lišit):



```
# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5).

source /etc/network/interfaces.d/*

# The loopback network interface
auto lo
iface lo inet loopback

# The primary network interface
allow-hotplug ens33
iface ens33 inet dhcp
# This is an autoconfigured IPv6 interface
iface ens33 inet6 auto
```



První část se týká mého loopbacku Interface, kterého se nebudu dotýkat, a následně Interface ens33. Úpravy zahrnují přidání mého druhého Interface (ens36) a konfiguraci mostu s těmito dvěma rozhraními:



```
# The primary network interface
auto ens33
iface ens33 inet manual

#The secondary network interface
auto ens36
iface ens36 inet manual
```



Zde je několik vysvětlení těchto prvních změn:





- auto *Interface***: automaticky "spustí" Interface při startu systému
- iface *Interface* inet manual**: pro použití Interface bez IP Address. Stejně jako klíčové slovo "static" pro definici statické IP adresy Address nebo "dhcp" pro použití dynamické adresace



Úpravy pokračují:



```
# Bridge interface
auto br0
iface br0 inet static
address 192.168.1.23
netmask 255.255.255.0
gateway 192.168.1.1
bridge_ports ens33 ens36
bridge_stp off
```



Zde opět několik vysvětlení:





- iface br0 inet static**: zde jsem definoval můstek Interface (*br0*) se statickým Address.
- Address, maska sítě, brána**: informace o adresování desky
- bridge_ports**: rozhraní, která mají být zahrnuta do mostu
- bridge_stp**: při propojování přepínačů se používá protokol Spanning Tree, který detekuje redundantní spoje a zabraňuje vzniku smyček. Vzhledem k tomu, že mezi dvě síťové cesty může být vložen most, může být zdrojem smyčky, proto je možné tento protokol povolit. Zde jej nepotřebuji, proto jej zakazuji.



Uložte změny a restartujte síť:



```
systemctl restart networking
```



Chcete-li zkontrolovat změny, zobrazte znovu výsledek příkazu **ip** add:



![Image](assets/fr/021.webp)


Zřetelně vidíte **můj nový Interface "*br0*" s IP Address, kterou jsem mu přiřadil.** Mimochodem, můžete také vidět, že moje dvě fyzická rozhraní jsou skutečně "UP", ale nemají IP Address.



## IV. Instalace NtopNG



Nyní, když je naše sonda schopna odposlouchávat provoz mezi mou sítí a směrovačem, zbývá už jen nainstalovat ntopng. K tomu nejprve upravte soubor */etc/apt/sources.list* a přidejte **contrib** na konec každého řádku začínajícího na **deb** nebo **deb-src**.



Ve výchozím nastavení obsahují zdroje balíčků pouze balíčky vyhovující zásadám DFSG (*Debian Free Sotftware Guidelines*), označené klíčovým slovem **main**. Tyto zdroje můžete také přidat:





- contrib**: balíčky obsahující software kompatibilní s DFSG, ale používající závislosti, které nejsou součástí větve **main**
- non-free**: obsahuje balíčky, které nejsou v souladu s DFSG



Příklad řádku v souboru /etc/apt/sources.list:



```
deb http://deb.debian.org/debian/ bullseye main
```



Takže k takovýmto řádkům prostě přidám slovo **contrib**.



Ostatní kroky jsou uvedeny na stránce [NtopNG] (https://packages.ntop.org/apt/), kde je pro Debian 11 nutné přidat zdrojové kódy Ntop pro budoucí instalaci. Toto přidání je automatizované pomocí souboru:



```
wget https://packages.ntop.org/apt/bullseye/all/apt-ntop.deb
apt install ./apt-ntop.deb
```



Poté následuje vlastní fáze instalace:



```
apt-get clean all
apt-get update
apt-get install ntopng
```



První příkaz odstraní mezipaměť správce balíčků apt. Druhý aktualizuje seznam balíčků a třetí nainstaluje NtopNG.



Po instalaci je software **NtopNG přímo dostupný na portu 3000 počítače Debian**. Pro mě je to tedy `http://192.168.1.23:3000`



![Image](assets/fr/022.webp)



Domovská stránka NtopNG



Zobrazí se výchozí přihlašovací jméno a heslo, takže je stačí zadat!



## V. Použití NtopNG



Při prvním přihlášení budete nejprve vyzváni ke změně výchozího hesla správce a jazyka. Francouzština mezi nimi bohužel není.



Poté se dostanete na palubní desku:



![Image](assets/fr/023.webp)



Přístrojová deska NtopNG



Na tohle si nezvykejte! Pokud si všimnete žlutého rámečku v horní části obrazovky, uvidíte větu: "*Licence expires in 04:57*". Ve výchozím nastavení instalace spustí zkušební verzi plné verze NtopNG, ovšem na (velmi) omezenou dobu. Po uplynutí tohoto "odpočtu" se aktivuje verze *komunita* a změní se ovládací panel:



![Image](assets/fr/024.webp)



Nový přístrojový panel komunity NtopNG



Nejdříve je třeba **zkontrolovat, zda poslouchá správný Interface**. V levém horním rohu se nachází rozevírací seznam dostupných rozhraní, ve kterém můžete vybrat rozhraní Interface, které nás zde zajímá: br0



![Image](assets/fr/025.webp)



Výběr Interface



V novém okně se zobrazí "Top Flaw Talkers", tj. zařízení, která komunikují nejčastěji. Zde se mi zobrazují pouze dvě stanice:



![Image](assets/fr/026.webp)



**Vlevo jsou zobrazeny zdrojové hostitelské počítače, vpravo cílové ** To umožňuje zobrazit využití celkové šířky pásma jednotlivými hostitelskými počítači a získat celkový přehled o síťovém provozu. To není špatné, ale můžeme jít dál...



Pokud například kliknu na položku "*Hosts*", zobrazí se graf zobrazující spotřebu energie při odesílání a přijímání u každého hostitele v síti. Zde například vidím, že jen na 192.168.1.37 připadá 80 % mého provozu:



![Image](assets/fr/027.webp)



Pokud kliknu na IP adresu Address daného hostitele, jsem přesměrován na souhrnnou stránku:



![Image](assets/fr/028.webp)



Vidím například, že se jedná o počítač VMWare (rozpoznáním ANO mého MAC Address), že se jmenuje DESKTOP-GHEBGV1 (takže se jistě jedná o hostitele Windows) A mám **statistiky přijatých a odeslaných paketů a množství dat**.



V horní části tohoto shrnutí si také všimnete nové nabídky. Doporučuji vám kliknout na položku "**Aplikace**" a podívat se, co je příčinou takového provozu:



![Image](assets/fr/017.webp)


Ha, vypadá to, že máme odpověď! Na grafu vlevo **vidíme, že 76,6 % návštěvnosti pochází z ... Windows Update**, takže tento hostitel stahuje aktualizace!



NtopNG používá technologii zvanou DPI (Deep Packet Inspection), která umožňuje kategorizovat každý síťový tok a definovat aplikaci (nebo rodinu aplikací), která za ním stojí.



Pro demonstraci spustím na svém hostiteli video na YouTube:



![Image](assets/fr/018.webp)



**Provoz byl okamžitě rozpoznán a zařazen do kategorií!



Poznámka: z pochopitelných důvodů může tento druh softwaru vyvolat problémy se soukromím, proto buďte opatrní a používejte jej za správných podmínek. Všimněte si také, že je možné **anonymizovat výsledky**, možnost najdete v **Nastavení > Předvolby > Různé** a jmenuje se "**Maskování hostitelské IP Address**".



## VI. Detekce a výstrahy



NtopNG je také schopen vydávat bezpečnostní upozornění na určité kanály. Ty naleznete v nabídce **Alerts** na levém banneru. Zde mám například celkem 2851 výstrah rozdělených do různých stupňů závažnosti: Upozornění, Varování a Chyba.



![Image](assets/fr/019.webp)



Podívejme se na výstrahy s vysokou kritičností, mám jich 17!



Kliknutím na tento obrázek se zobrazí podrobnosti o výstrahách. Není zde nic alarmujícího, jedná se o falešně pozitivní hlášení, stahování aktualizací je kategorizováno jako přenos binárních souborů v proudu HTTP, což by skutečně mohlo znamenat útok.



![Image](assets/fr/020.webp)



Protože však používám bezplatnou verzi, nemohu vyloučit domény nebo hostitele, kteří jsou zdrojem výstrah, takže je budete muset sledovat, abyste nepřišli o něco mnohem znepokojivějšího. NtopNG bude generate upozornění v případě:





- Stahování binárních souborů přes HTTP
- Podezřelé přenosy DNS
- Použití nestandardního portu
- Detekce SQL injection
- Cross-Site Scripting (XSS)
- Atd.



## VII. Závěr



V tomto návodu jsme se dozvěděli, **jak nastavit sondu pomocí NtopNG**, která nám umožní **analyzovat síťový provoz** a zobrazit využití protokolů a obsazenost jednotlivých hostitelů, ale také odhalit podezřelý provoz.



V tomto článku bohužel nemohu popsat všechny funkce a možnosti, ale neváhejte je prozkoumat!



Toto řešení lze trvale implementovat v rámci podnikové infrastruktury. NtopNG může také exportovat výsledky do databáze InfluxDB, což vám umožní vytvářet vlastní řídicí panely pomocí nástroje třetí strany, jako je Graphana.