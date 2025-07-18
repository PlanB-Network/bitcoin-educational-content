---
name: OPNsense
description: Jak nainstaluji a nakonfiguji bránu firewall OPNsense?
---
![cover](assets/cover.webp)



___



*Tento návod vychází z původního obsahu Floriana BURNELA zveřejněného na stránkách [IT-Connect](https://www.it-connect.fr/). Licence [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). V původním textu mohly být provedeny změny.*



___



## I. Prezentace



V tomto tutoriálu se podíváme na open source firewall OPNsense. Podíváme se na jeho hlavní funkce, předpoklady a způsob instalace tohoto řešení založeného na systému FreeBSD.



Než začnete, měli byste vědět, že **OPNsense i pfSense jsou open source firewally** založené na FreeBSD. Dá se říci, že pfSense je jakýmsi starším bratrem OPNsense, protože druhý jmenovaný je Fork vytvořený v roce 2015. Nakonec je důležité zdůraznit, že od roku 2017 přešel **OPNsense na HardenedBSD namísto FreeBSD**. HardenedBSD je vylepšená verze FreeBSD s pokročilými bezpečnostními funkcemi



OPNsense vyniká modernějším uživatelským rozhraním Interface a **častější frekvencí aktualizací**. Harmonogram aktualizací systému OPNsense totiž zahrnuje dvě hlavní verze ročně, které jsou aktualizovány přibližně každé dva týdny (výsledkem jsou menší verze). Tato návaznost je ve srovnání s řešením pfSense velmi zajímavá, pokud se podíváme na komunitní verze těchto řešení.



![Image](assets/fr/050.webp)



## II. Funkce systému OPNsense



OPNsense je operační systém navržený tak, aby fungoval jako brána firewall a směrovač, ačkoli jeho funkcí je mnoho a lze je rozšířit instalací dalších balíčků. Je vhodný pro produkční použití a slouží především k zabezpečení sítě a správě toků.



### A. Hlavní rysy



Zde jsou některé z klíčových funkcí systému OPNsense:





- Brána firewall a NAT**: OPNsense poskytuje pokročilé funkce stavové brány firewall se stavovým filtrováním a také funkce překladu sítě Address (NAT).





- DNS/DHCP**: OPNsense lze nakonfigurovat tak, aby spravoval služby DNS a DHCP v síti. Může fungovat jako server DHCP, ale lze jej použít také jako překladač DNS pro počítače v místní síti. Ve výchozím nastavení je integrován také Dnsmasq.





- VPN**: OPNsense podporuje několik protokolů VPN, včetně IPsec, OpenVPN a WireGuard, které umožňují bezpečné připojení pro vzdálený přístup k mobilním pracovním stanicím nebo propojení pracovišť.





- Webový proxy server**: OPNsense obsahuje webový proxy server pro kontrolu a filtrování přístupu k internetu. Lze ji také použít k filtrování obsahu a správě přístupu k síti.





- Správa šířky pásma (QoS)**: OPNsense nabízí funkce správy kvality služeb (QoS), které umožňují upřednostňovat síťový provoz a lépe spravovat šířku pásma sítě.





- Captive portal**: tato funkce umožňuje spravovat přístup uživatelů do sítě prostřednictvím ověřovací stránky (místní základna, bony atd.). Jedná se o funkci běžně nasazovanou pro veřejné sítě Wi-Fi.





- IDS/IPS**: OPNsense integruje Suricatu a nabízí funkce detekce a prevence narušení (IDS/IPS), které chrání síť před útoky.





- Vysoká dostupnost (CARP)**: OPNsense podporuje CARP (*Common Address Redundancy Protocol*) pro vysokou dostupnost mezi více firewally OPNsense, což zajišťuje, že služba zůstane aktivní i v případě selhání hardwaru.





- Podávání zpráv a monitorování**: OPNsense poskytuje nástroje pro reportování a monitorování v reálném čase, které umožňují sledovat výkon sítě (pomocí NetFlow) a odhalovat potenciální problémy díky vytváření protokolů. To zahrnuje i grafické zobrazení. Nástroj Monit je integrován do systému OPNsense a umožňuje dohled nad samotnou bránou firewall.



### B. Další balíčky



Toto je pouze přehled funkcí, které nabízí OPNsense. Kromě toho **katalog balíčků** přístupný z administrace OPNsense Interface umožňuje **obohatit firewall o další funkce**. Patří mezi ně klient ACME, agent Wazuh, služba NTP Chrony a Caddy jako reverzní proxy server.



![Image](assets/fr/051.webp)



## III. Předpoklady OPNsense



Nejprve se musíte rozhodnout, kam budete OPNsense instalovat. Existuje několik možných řešení, včetně instalace na :





- Hypervisor jako virtuální počítač, ať už Hyper-V, Proxmox, VMware ESXi atd.
- Stroj jako *bare-metal* systém. Může to být miniaturní počítač, který funguje jako firewall.



Prostřednictvím našeho internetového obchodu si můžete zakoupit také **zařízení OPNsense pro montáž do stojanu**.



Je třeba vzít v úvahu hardwarové prostředky potřebné k provozu systému OPNsense. To je podrobně popsáno na [této stránce dokumentace](https://docs.opnsense.org/manual/hardware.html).



**Minimální a doporučené zdroje pro výrobu:**



| Caractéristiques | Minimum | Recommandation |
| --- | --- | --- |
| Processeur | 1 GHz - 2 cœurs | 1.5 GHz - Multi-coeurs |
| Mémoire vive (RAM) | 2 Go | 8 Go |
| Espace de stockage pour le système | Disque dur, disque SSD ou carte SD (4 Go) | 120 Go en SSD |

A konečně, **vaše požadavky na prostředky závisí především na počtu spravovaných připojení**, a tedy na **vašich požadavcích na šířku pásma**. Kromě toho je třeba **zohlednit služby, které budou aktivovány a používány** (proxy server, detekce narušení atd.), protože mohou být náročné na procesor a/nebo paměť RAM.



Budete také potřebovat instalační obraz ISO aplikace OPNsense, který si můžete stáhnout z [oficiální webové stránky](https://opnsense.org/download/). Pro instalaci do virtuálního počítače vyberte jako typ obrazu "**dvd**" a získáte obraz ISO (a dělejte si s ním, co chcete...). Pro instalaci prostřednictvím bootovacího klíče USB vyberte možnost "**vga**", čímž získáte soubor "**.img**".



![Image](assets/fr/048.webp)



Počítač budete potřebovat také pro správu a testování systému OPNsense.



## IV. Konfigurace cíle



Naším cílem je





- Vytvořte interní virtuální síť (192.168.10.0/24 - LAN)**, která může přistupovat k Internetu prostřednictvím brány firewall OPNsense. Pro produkční použití to může být vaše místní síť, kabelová síť a/nebo Wi-Fi.
- Aktivace a konfigurace NAT**, aby virtuální počítače ve vnitřní virtuální síti měly přístup k internetu
- Aktivace a konfigurace serveru DHCP v systému OPNsense** za účelem distribuce konfigurace IP budoucím počítačům připojeným k interní virtuální síti
- Nakonfigurujte bránu firewall** tak, aby povolovala pouze odchozí toky z LAN do WAN v protokolech HTTP (80) a HTTPS (443).
- Nakonfigurujte bránu firewall** tak, aby virtuální síť LAN mohla používat službu OPNsense jako překladač DNS (53).



Pokud používáte platformu Hyper-V, získáte následující zobrazení:



![Image](assets/fr/033.webp)



## V. Instalace brány firewall OPNsense



### A. Příprava zaváděcího klíče USB



Prvním krokem je příprava instalačního média: **spouštěcí klíč USB s OPNsense**. To je samozřejmě volitelné, pokud pracujete ve virtuálním prostředí, ale v každém případě je třeba stáhnout instalační obraz ISO OPNsense.



Po stažení získáte **archiv obsahující obraz ve formátu ".img "**. Můžete **vytvořit bootovací USB flash disk** pomocí různých aplikací, včetně **balenaEtcher**: velmi jednoduché použití. Aplikace navíc rozpozná obraz v archivu, takže jej nemusíte předem dekomprimovat.





- [Stáhnout balenaEtcher](https://etcher.balena.io/)



Po instalaci aplikace vyberte svůj obrázek, klíč USB a klikněte na tlačítko "Flash! Chvíli počkejte.



![Image](assets/fr/049.webp)



Nyní jste připraveni k instalaci.



### B. Instalace systému OPNsense



Spusťte počítač, který je hostitelem nástroje OPNsense. Měla by se zobrazit uvítací stránka podobná té níže. Po několik sekund bude v okně vidět zobrazená obrazovka. Nechte proces proběhnout...



![Image](assets/fr/019.webp)



Obraz systému OPNsense je nahrán do počítače, takže k němu lze přistupovat v režimu "**živý**", tj. dočasně uložený v paměti.



![Image](assets/fr/025.webp)



Poté se dostanete na obrazovku Interface podobnou té níže. Přihlaste se pomocí přihlašovacího jména "**installer**" a hesla "**opnsense**". Upozorňujeme, že klávesnice je v tuto chvíli **QWERTY**. V tomto okamžiku **zahájíme proces instalace OPNsense**.



![Image](assets/fr/026.webp)



Na obrazovce se zobrazí nový průvodce. Prvním krokem je výběr rozložení klávesnice odpovídající vaší konfiguraci. V případě klávesnice AZERTY vyberte ze seznamu možnost "**Francouzština (klávesy s diakritikou)**" a poté dvakrát klikněte na**.



![Image](assets/fr/027.webp)



Druhým krokem je výběr úlohy, která se má provést. Zde provedeme instalaci pomocí souborového systému **ZFS**. Umístěte se na řádek "**Install (ZFS)**" a potvrďte tlačítkem **Enter**.



![Image](assets/fr/028.webp)



Ve třetím kroku vyberte možnost "**stripe**", protože náš počítač je vybaven **pouze jedním diskem**: není možné zajistit redundanci úložiště firewallu a jeho dat. To je důležité zejména při instalaci na fyzický počítač, kdy je třeba chránit disk proti selhání hardwaru prostřednictvím principu RAID.



![Image](assets/fr/029.webp)



Ve čtvrtém kroku jednoduše potvrďte stisknutím tlačítka **Enter**.



![Image](assets/fr/030.webp)



Nakonec potvrďte volbu "**YES**" a stiskněte klávesu **Enter**.



![Image](assets/fr/031.webp)



Nyní budete muset počkat, než se OPNsense nainstaluje... Tento proces trvá asi 5 minut.



![Image](assets/fr/032.webp)



Po dokončení instalace můžeme před restartem změnit heslo "**root**". Vyberte položku "**Root Password**", stiskněte **Enter** a dvakrát zadejte heslo "**root**".



![Image](assets/fr/020.webp)



Nakonec vyberte možnost "**Dokončit instalaci**" a stiskněte **Enter**. Při této příležitosti **vyjměte disk z jednotky DVD virtuálního počítače**. V nastavení virtuálního počítače můžete také nastavit první spuštění na disk.



![Image](assets/fr/021.webp)



Virtuální počítač se restartuje a načte systém OPNsense z disku, protože jsme jej právě nainstalovali. V konzoli se přihlaste pomocí účtu "root" a nového hesla (jinak je výchozí heslo "**opnsense**").



### D. Propojení síťových rozhraní



Zobrazí se níže uvedená obrazovka. Zvolte "**1**" a stiskněte **Enter** pro přiřazení síťových karet stroje k rozhraním OPNsense.



![Image](assets/fr/022.webp)



Průvodce vás nejprve vyzve ke konfiguraci agregace linek a VLAN. Zadejte "**n**" pro odmítnutí a pokaždé potvrďte odpověď tlačítkem **Enter**. Dále je třeba přiřadit dvě rozhraní "**hn0**" a "**hn1**" k sítím **WAN** a **LAN**. V zásadě platí, že "**hn0**" odpovídá síti WAN a druhé rozhraní Interface síti LAN.



Funguje to takto:



![Image](assets/fr/023.webp)



Nyní máme :





- Síť Interface **LAN** spojená se síťovou kartou "**hn1**" a s výchozí IP OPNsense Address, tj. **192.168.1.1/24**.
- Interface **WAN** spojený se síťovou kartou "**hn0**" a s IP Address získanou prostřednictvím **DHCP** v místní síti (díky našemu externímu virtuálnímu přepínači).



Ve výchozím nastavení je z pochopitelných bezpečnostních důvodů správa OPNsense Interface přístupná pouze z LAN Interface. Pro provádění správy se proto musíte připojit k síti LAN Interface firewallu. Pokud to není možné, můžete OPNsense dočasně spravovat z WAN. To zahrnuje vypnutí funkce brány firewall.



Za tímto účelem se přepněte do režimu shellu pomocí volby "**8**" a spusťte následující příkaz:



```
pfctl -d
```



![Image](assets/fr/024.webp)



### E. Přístup do systému správy OPNsense Interface



K OPNsense Administration Interface lze přistupovat přes HTTPS pomocí IP Address sítě LAN** Interface (nebo WAN). Prohlížeč vás přenese na přihlašovací stránku. Přihlaste se pomocí účtu "root" a hesla, které jste vybrali dříve.



![Image](assets/fr/034.webp)



Počkejte několik sekund... Budete vyzváni k provedení základní konfigurace pomocí průvodce. Klepnutím na tlačítko "**Další**" pokračujte.



![Image](assets/fr/036.webp)



V prvním kroku je třeba definovat název hostitele, název domény, zvolit jazyk a definovat server(y) DNS, který(é) bude(ou) použit(y) pro překlad názvu. Ponecháním možnosti "**Povolit resolver**" umožníme bráně firewall, aby byla použita jako resolver DNS, což bude užitečné pro počítače v naší virtuální síti LAN.



![Image](assets/fr/037.webp)



Přejděte k dalšímu kroku. Průvodce vám nabízí možnost **definovat server NTP pro synchronizaci data a času**, ačkoli ve výchozím nastavení jsou již servery nakonfigurovány. Kromě toho je nezbytné zvolit časové pásmo odpovídající vaší zeměpisné poloze (pokud nemáte zvláštní požadavky).



![Image](assets/fr/038.webp)



Poté následuje důležitý krok: **Konfigurace sítě Interface WAN**. V současné době je nakonfigurován v režimu DHCP a v tomto režimu konfigurace zůstane, pokud si nepřejete nastavit statickou IP adresu Address.



![Image](assets/fr/039.webp)



Na stránce konfigurace Interface WAN je třeba zrušit zaškrtnutí možnosti "**Block access to private networks via WAN**", pokud síť na straně WAN používá privátní adresování. To bude pravděpodobně váš případ, pokud provozujete laboratoř, a může vám tak znemožnit přístup k internetu.



![Image](assets/fr/040.webp)



Dále můžete **definovat heslo "root "**, ale to je nepovinné, protože jsme to již udělali.



![Image](assets/fr/041.webp)



Pokračujte až na konec, abyste zahájili opětovné načtení konfigurace. Pokud potřebujete pokračovat v přebírání řízení prostřednictvím sítě WAN, spusťte znovu výše uvedený příkaz, jakmile bude tento proces dokončen.



![Image](assets/fr/042.webp)



To je vše!



![Image](assets/fr/035.webp)



### E. Konfigurace DHCP



Naším cílem je použít server OPNsense DHCP k distribuci IP adres ve virtuální síti LAN. K tomu potřebujeme získat přístup k tomuto umístění nabídky:



```
Services > ISC DHCPv4 > [LAN]
```



**Jak vidíte, služba DHCP je v síti LAN již ve výchozím nastavení povolena ** Pokud o tuto službu nemáte zájem, měli byste ji zakázat. Přestože je již povolena a chceme ji používat, je důležité zkontrolovat její konfiguraci.



V případě potřeby můžete změnit rozsah distribuovaných IP adres: *v závislosti na aktuálním nastavení můžete změnit rozdělení adres *192.168.10.10** až **192.168.10.245**.



![Image](assets/fr/046.webp)



Vidíme také, že pole "**Servery DNS**", "**Brána**", "**Název domény**" atd. jsou ve výchozím nastavení prázdná. Ve skutečnosti dochází k automatickému dědění určitých možností a výchozích hodnot těchto různých polí. Například pro server DNS bude rozdělena IP adresa Address sítě Interface LAN, což umožní použít bránu firewall OPNsense jako resolver DNS.



Po provedení změn konfiguraci v případě potřeby uložte.



![Image](assets/fr/047.webp)



Chcete-li otestovat server DHCP, musíte připojit počítač k síti LAN brány firewall.



Tento počítač musí získat IP adresu Address ze serveru OPNsense DHCP a náš počítač musí mít přístup do sítě. Přístup k internetu musí fungovat. Upozorňujeme, že pokud jste zakázali funkci brány firewall pro přístup k systému OPNsense ze sítě WAN, dojde k deaktivaci NAT, což znemožní přístup k webu.



**Poznámka**: aktuálně vydané pronájmy DHCP jsou viditelné v administraci OPNsense Interface. Za tímto účelem přejděte na následující místo: **Služby > ISC DHCPv4 > Pronájmy**.



![Image](assets/fr/045.webp)



### F. Konfigurace NAT a pravidel brány firewall



Dobrou zprávou je, že nyní můžeme přistupovat ke správě OPNsense Interface ze sítě LAN.



```
https://192.168.1.10
```



Po přihlášení do služby OPNsense zjistíme konfiguraci NAT. Přejděte do tohoto umístění: **Firewall > NAT > Outbound**. Zde si můžete vybrat mezi automatickým (výchozím) a ručním vytvářením odchozích pravidel NAT.



Zvolte automatický režim pomocí možnosti "**Automatické generování odchozích pravidel NAT**" a klikněte na "**Uložit**" (v zásadě je tato konfigurace již aktivní). V automatickém režimu si OPNsense sám vytvoří pravidlo NAT pro každou z vašich sítí.



![Image](assets/fr/043.webp)



Všechny počítače připojené k virtuální síti LAN "**192.168.10.0/24**" mohou prozatím přistupovat k internetu bez omezení. Naším cílem je však omezit přístup do sítě WAN na protokoly HTTP a HTTPS a také na DNS v síti LAN Interface brány firewall.



Musíme tedy vytvořit pravidla brány firewall... Projděte nabídku následujícím způsobem: **Firewall > Pravidla > LAN**.



**Ve výchozím nastavení jsou k dispozici dvě pravidla pro autorizaci veškerého odchozího provozu sítě LAN, a to v protokolech IPv4 a IPv6**. Tato dvě pravidla deaktivujte kliknutím na šipku Green zcela vlevo na začátku každého řádku.



Poté vytvořte tři nová pravidla pro autorizaci sítě **LAN** (tj. "**LAN net**") na :





- přístup ke všem cílům pomocí **HTTP**.
- přístup ke všem cílům pomocí **HTTPS**.
- požádat o **OPNsense** na své **Interface LAN** (tj. "**LAN Address**") prostřednictvím protokolu **DNS** (to znamená použít firewall jako DNS), jinak autorizovat svůj DNS resolver prostřednictvím jeho IP Address.



Z toho vyplývá následující výsledek:



![Image](assets/fr/044.webp)



Zbývá už jen kliknout na tlačítko "**Použít změny**" a přepnout nová pravidla brány firewall do produkčního režimu. **Upozorňujeme, že všechny toky, které nejsou výslovně autorizovány, budou ve výchozím nastavení blokovány



Počítač v síti LAN může přistupovat k internetu pomocí protokolů HTTP a HTTPS. Všechny ostatní protokoly budou blokovány.



![Image](assets/fr/018.webp)



## IV. Závěr



Podle tohoto návodu budete moci nainstalovat OPNsense a začít ihned pracovat. OPNsense nabízí širokou škálu funkcí pro efektivní zabezpečení a správu síťového provozu a je vhodný pro použití v profesionálním prostředí.



Tato instalace je pouze začátek: neváhejte prozkoumat nabídky a nakonfigurovat další funkce a přizpůsobit tak OPNsense svým potřebám.