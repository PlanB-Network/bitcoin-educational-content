---
name: Pi-Hole
description: Blokování reklam pro celou síť
---
![cover](assets/cover.webp)



___



*Tento návod vychází z původního obsahu Floriana Duchemina publikovaného na stránkách [IT-Connect](https://www.it-connect.fr/). Licence [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). V původním textu mohly být provedeny změny.*



___



## I. Prezentace



Všichni jsme to udělali, jakmile jsme spustili svůj oblíbený prohlížeč: nainstalovali jsme si **adblocker** (blokátor reklam). Když však používáme prohlížeč v televizi nebo v zařízení se systémem Android atd... Je trochu složitější najít něco, co by fungovalo. A pokud je v domácnosti více než jedno zařízení, no, musíte operaci opakovat pro každý prohlížeč!



V tomto návodu vyřešíme jednoduchý problém**: poskytneme blokátor reklam všem počítačům v naší síti a budeme ho spravovat centrálně**



K tomu použijeme nástroj vyvinutý pro tento účel: **Pi-Hole**



Pi-Hole je díra DNS. Využívá požadavky DNS odeslané vašimi zařízeními k potvrzení nebo odmítnutí provozu, čímž vás chrání před adresami a doménami, o nichž je známo, že šíří reklamu, malware apod.



DNS je zkratka pro Domain Name System (systém doménových jmen). Co je to doménové jméno? No, "it-connect.fr" je jen jeden příklad. Název domény je jedinečný identifikátor jednoho nebo více zdrojů, které obvykle spravuje jeden subjekt.



Název počítače a název domény se nazývá FQDN (Fully Qualified Domain Name*). Umožňuje dosáhnout konkrétního stroje pouhým "zavoláním". Například když napíšete "www.trucmachin.com", voláte ve skutečnosti stroj "www", který patří do domény "trucmachin.com".



Až na to, že naše počítače nerozumějí lidské řeči, rozumí pouze binárně, takže potřebují IP adresu Address, což je ekvivalent telefonního čísla, aby se dostaly na webovou stránku.



Při každém zadání názvu webové stránky do prohlížeče nebo kliknutí na odkaz se tedy počítač nejprve zeptá serveru DNS na IP adresu Address odpovídající tomuto názvu.



**Pi-Hole pak tyto požadavky (denně jich jsou stovky!) zkontroluje a automaticky zablokuje ty, o nichž je známo, že hostují reklamy nebo dokonce škodlivé soubory



## II. Instalace systému Pi-Hole



Při názvu Pi-Hole byste mohli oprávněně předpokládat, že potřebujete Raspberry-Pi... Ale to není tak docela pravda. **Pi-Hole lze nainstalovat na jakýkoli počítač s Linuxem (Debian, Fedora, Rocky, Ubuntu atd.)



Na druhou stranu je třeba mít na paměti, že **toto zařízení bude muset běžet 24 hodin denně z jednoduchého důvodu: bez DNS není internet!** Raspberry je proto dobrý nápad, protože nespotřebovává téměř žádnou energii.



Pro instalaci se jednoduše připojte k počítači se systémem Linux přes SSH a zadejte následující příkaz jako "*root*":



```
curl -sSL https://install.pi-hole.net | bash
```



> **Poznámka**: za normálních okolností není vhodné "hackovat" skript, aniž byste nejprve věděli, co dělá. Pokud si nejste jisti, přejděte na stránku pomocí prohlížeče nebo si obsah stáhněte jako soubor.
>


> **Poznámka: v minimálních verzích Debianu 11 není Curl nainstalován, takže jej musíte před zadáním výše uvedeného příkazu nainstalovat ručně pomocí příkazu **apt-get install curl**.

Po spuštění skriptu se provede řada testů a instalace se provede sama:



![Image](assets/fr/019.webp)



Instalace systému Pi-Hole



Po dokončení instalace se zobrazí tato obrazovka:



![Image](assets/fr/020.webp)



Startovací obrazovka Pi-Hole



> **Poznámka**: pokud v počítači používáte DHCP, zobrazí se varovná zpráva. Pro správné používání samozřejmě důrazně doporučujeme přiřadit počítači pevnou IP adresu.

Po této obrazovce se zobrazí několik informačních zpráv a poté budete přesměrováni na průvodce konfigurací, který se vás nejprve zeptá, na který server DNS bude Pi-Hole požadavky předávat. Já jsem si vybral Quad9, který má chartu ochrany osobních údajů uživatelů.



![Image](assets/fr/021.webp)



Výběr DNS - Pi-Hole



> **Poznámka: pokud jste ve firmě, je pravděpodobné, že váš aktuální server DNS je řadičem domény služby Active Directory. Nemějte však obavy, později můžete zadat podmíněný přesměrovač pro doménu dle vlastního výběru. Obvykle budete moci přesměrovat jakýkoli požadavek týkající se místní domény na svůj server DNS.

Všimněte si, že některé volby zahrnují možnost DNSSEC. Protokol DNS v podstatě není zabezpečený (v době svého vzniku na to nebyl myslen). DNSSEC tento problém řeší přidáním zabezpečení Layer prostřednictvím šifrování a podepisování výměn, jak je vysvětleno v příslušném článku: [Zabezpečení DNS](https://www.it-connect.fr/securite-dns-doh-quest-ce-le-dns-over-https/)



Každý blokátor reklam se při své práci spoléhá na jeden nebo více seznamů. Pi-Hole je standardně dodáván s jedním seznamem, takže si jej vyberte a další přidejte později.



![Image](assets/fr/022.webp)



Pokud jde o web Interface, jeho instalace není povinná, protože nástroj má vlastní příkazový řádek pro správu a vizualizaci. Ale tento Interface je poměrně příjemný a dobře zpracovaný, takže doporučuji jej zároveň nainstalovat:



![Image](assets/fr/023.webp)



Pokud instalujete Pi-Hole na počítač, který již má webový server, můžete na následující otázku odpovědět "ne". Mějte však na paměti, že k tomu, aby to fungovalo, je zapotřebí PHP a několik modulů. V opačném případě bude nainstalován **lighttpd se všemi potřebnými moduly**.



![Image](assets/fr/024.webp)



Poté budete dotázáni, zda si přejete zaznamenávat požadavky DNS. **Pokud chcete uchovávat historii, nastavte tuto možnost na ano; v opačném případě nastavte tuto možnost na ne, ale ztratíte část funkcí** (viz další obrazovka).



![Image](assets/fr/025.webp)



Pro web Interface používá Pi-Hole vlastní funkci FTLDNS, která poskytuje rozhraní API a generuje statistiky z požadavků DNS. Tato funkce může zahrnovat režim "soukromí", který maskuje požadované domény, zákazníky za požadavkem nebo obojí. Hodí se, pokud chcete provádět monitorování bez narušení soukromí lidí, nebo jednoduše pokud chcete dodržovat příslušné předpisy v případě použití ve veřejné síti.



![Image](assets/fr/026.webp)



Volba soukromého životního stylu



Po zodpovězení této poslední otázky skript provede to, co má: stáhne repozitáře GitHub a nakonfiguruje Pi-Hole. Na konci instalace se zobrazí souhrnná obrazovka s důležitými informacemi:



![Image](assets/fr/027.webp)



Souhrnná obrazovka instalace



Zapište si webové heslo a síťové informace Interface. Nyní je čas nakonfigurovat službu DHCP v našem aktuálním umístění.



## III. Konfigurace DHCP



Aby mohl systém Pi-Hole fungovat, musí "překládat" požadavky DNS od klientů, takže musí vědět, že je to ten, komu je má posílat. Toho lze dosáhnout několika způsoby:





- Upravte nastavení DNS na serveru DHCP (např. ve vašem Boxu)
- Zakázat tento server a používat server poskytovaný službou Pi-Hole
- Ruční úprava každého zařízení tak, aby používalo Pi-Hole jako DNS



Osobně jsem zvolil první řešení. Je pravděpodobné, že v místě, kde se nacházíte**, máte server DHCP (obvykle váš box). Takže se nemusíte obtěžovat.



Protože existuje velké množství možností mezi krabicemi různých operátorů (které všechny neznám) a těmi, kteří mají vlastní router, nebudu poskytovat snímek obrazovky pro tyto úpravy. V každém případě budete muset přejít do nastavení DHCP a upravit parametr "DNS" tak, aby obsahoval IP Address vašeho Pi-Hole.



Pokud byla některá zařízení zapnuta dříve, zachovala si stará nastavení, takže bude nutné znovu spustit požadavek na konfiguraci.



Na pracovních stanicích se systémem Windows můžete pomocí příkazového řádku:



```
ipconfig /renew
```



Na pracovní stanici se systémem Linux:



```
dhclient
```



U všech ostatních zařízení je třeba je vypnout a znovu zapnout.



Měli by tedy získat správné parametry, aby si je mohli zkontrolovat:



```
ipconfig /all
```



V poli DNS byste měli zadat číslo Address svého počítače Pi-Hole, v mém případě 192.168.1.42:



![Image](assets/fr/029.webp)



## IV. Použití webového modulu Pi-Hole Interface



Pro usnadnění správy využívá **Pi-Hole** dobře navržený web Interface. Je uživatelsky přívětivý a přístupný a umožňuje vám:





- Zobrazení počtu požadavků, blokovaných požadavků atd. v reálném čase.
- Správa bílé a černé listiny
- Přidání statických položek, aliasů atd.
- Přidat seznamy
- A mnoho dalších funkcí!



Za sebe přidám seznam blokování. Jak bylo uvedeno výše, současně s Soft byl nainstalován pouze jeden seznam. Existuje mnoho seznamů pro reklamní weby, ale nejlepší je vybrat si alespoň jeden specifický pro zemi, ve které žijete. Jedním z nejznámějších seznamů je **EasyList** a jeden z nich je specifický pro Francii: [EasyList-ListFR](https://raw.githubusercontent.com/deathbybandaid/piholeparser/master/Subscribable-Lists/ParsedBlacklists/EasyList-Liste-FR.txt)



Chcete-li jej přidat, nejprve se připojte ke správci Interface: **http://<ip_du_PiHole>/admin**



Heslo správce již bylo vygenerováno (viz obrázek na konci instalace), takže pro přístup ke službě Interface stačí zadat toto heslo:



![Image](assets/fr/030.webp)



Interface z Pi-Hole



Vidíme například, že k Pi-Hole jsou připojeni dva zákazníci, že zpracoval 442 požadavků a že 8 z nich bylo zablokováno. Tyto grafy mohou být dobrým zdrojem informací, zejména v odborném kontextu.



Chcete-li přidat náš seznam, přejděte do nabídky "**Správa skupiny**" a "**Seznamy**":



![Image](assets/fr/031.webp)



Vidíme náš první seznam "**StevenBlack**", pro přidání našeho zkopírujte odkaz, který jsem vám dal výše, a vložte jej do pole "**Address**", pro popis jsem zvolil název seznamu:



![Image](assets/fr/032.webp)



Přidání seznamu v aplikaci Pi-Hole



Zbývá jen kliknout na tlačítko "**Přidat**" a přidat ji. Pro aktivaci musíme provést další krok, abychom Pi-Hole "upozornili" na převzetí tohoto seznamu. Chcete-li to provést:





- Buď použijte vestavěný příkazový řádek
- Buď web Interface



Osobně jsem si vybral druhou možnost, protože pokud jste se pozorně podívali, odkaz na skript PHP, který provádí aktualizaci, je přímo na stránce, na které se nacházíme (slovo "online"). Stačí tedy na něj kliknout, čímž se dostanete na stránku s jedinou možností:



![Image](assets/fr/033.webp)



Po dokončení skriptu se na stránce zobrazí výsledek, což znamená, že seznam byl zohledněn (samozřejmě pokud se nezobrazí chybová zpráva).



Jak bylo oznámeno na začátku tohoto návodu, Pi-Hole umožňuje také **blokovat domény, o kterých je známo, že šíří malware. Pro posílení této funkce doporučuji přidat také pravidelně aktualizovaný seznam domén distribuovaný službou Abuse.ch**, který výrazně posílí zabezpečení vaší sítě a je k dispozici na adrese [tento Address](https://urlhaus.abuse.ch/downloads/hostfile/).



Můžete samozřejmě přidat libovolné seznamy, které považujete za relevantní, nebo spravovat černou listinu ručně prostřednictvím nabídky černé listiny.



## V. Testy Pi-Hole



Nyní, když je vše připraveno, stačí řešení otestovat a ujistit se, že funguje správně.



Pokusím se například dostat na doménu *http://admin.gentbcn.org/*, která je na seznamu Abuse.ch, protože je známo, že hostí malware:



![Image](assets/fr/034.webp)



Zřejmě jsem někde zablokovaný. Abychom se ujistili, že to udělal Pi-Hole, můžeme se podívat do protokolu dotazů na webu Interface "Query Log" a zjistit, že se jedná o blokování z položky seznamu:



![Image](assets/fr/035.webp)



## VI. Závěr



V tomto návodu jsme vám ukázali, jak nastavit server DNS, který nejenže eliminuje většinu reklam pro vaše pohodlné prohlížení, ale také přidává **a Layer zabezpečení blokováním phishingových domén a domén šířících malware**.



Vše zdarma a úsporně, pokud je nainstalováno na Raspberry-Pi (z hlediska spotřeby energie).