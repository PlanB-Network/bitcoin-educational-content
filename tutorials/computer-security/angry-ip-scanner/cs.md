---
name: Angry IP Scanner
description: Jednoduchý způsob skenování sítě
---
![cover](assets/cover.webp)



___



*Tento návod vychází z původního obsahu Floriana BURNELA zveřejněného na stránkách [IT-Connect](https://www.it-connect.fr/). Licence [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). V původním textu mohly být provedeny změny.*



___



## I. Prezentace



Jak snadno a rychle vyhledat připojené počítače v síti Windows? Odpovědí je Angry IP Scanner. Tento projekt s otevřeným zdrojovým kódem umožňuje snadné skenování sítě pomocí snadno použitelného grafického nástroje Interface.



Tento nástroj mohou používat jednotlivci ke **skenování své místní sítě**, ale také profesionálové v oblasti IT ke stejnému účelu. Důkazem toho, že **tento nástroj je velmi praktický**, je skutečnost, že jej již **některé skupiny kyberzločinců** používají ke skenování podnikových sítí (stejně jako Nmap). Dobrým příkladem je [ransomwarová skupina RansomHub](https://www.it-connect.fr/deja-210-victimes-pour-le-groupe-de-ransomware-ransomhub-lance-en-fevrier-2024/). Stále se jedná o solidní software, ale stejně jako u jiných nástrojů zaměřených na sítě a bezpečnost může být jeho použití zneužito.



Zde ji budeme používat v systému **Windows 11**, ale je možné ji používat i v jiných verzích systému **Windows** a také v systémech **Linux** a **macOS**.



Skener **Angry IP** je méně komplexní než Nmap, přesto je zajímavý pro rychlou základní analýzu sítě, ale také proto, že je dostupný každému. Zjistí **hostitele připojené k síti** a identifikuje **názvy hostitelů** a **otevřené porty**.



Pokud chcete pokračovat, podívejte se na výukový program Nmap:



https://planb.network/tutorials/computer-security/communication/nmap-862300d7-6dfb-4660-970d-f56a9f58f60d

## II. Začínáme s programem Angry IP Scanner



### A. Stáhněte a nainstalujte Angry IP Scanner



Nejnovější verzi aplikace Angry IP Scanner si můžete stáhnout z oficiálních stránek aplikace nebo z GitHubu. My použijeme druhou možnost. Klikněte na níže uvedený odkaz a stáhněte si verzi EXE: "**ipscan-3.9.1-setup.exe**".





- [Angry IP Scanner GitHub](https://github.com/angryip/ipscan/releases/latest)



![Image](assets/fr/016.webp)



Spuštěním spustitelného souboru pokračujte v instalaci. Během instalace není třeba dělat nic zvláštního.



![Image](assets/fr/013.webp)



### B. Spusťte počáteční skenování sítě



Při prvním spuštění si přečtěte pokyny v okně "**Začínáme**", abyste se dozvěděli více o tom, jak nástroj funguje. Mimochodem, je třeba vzít v úvahu několik pojmů:





- **Podavač**: modul odpovědný za generování seznamů IP adres ke skenování z náhodného rozsahu IP adres nebo ze souboru se seznamem IP adres.
- **Fetcher**: sada modulů pro získávání informací o hostitelích v síti. Existují například fetchery pro zjišťování adres MAC, skenování portů, zjišťování názvů hostitelů nebo odesílání požadavků HTTP.



![Image](assets/fr/018.webp)



Chcete-li skenovat podsíť IP, jednoduše zadejte **počáteční IP Address** a **konečnou IP Address** do pole "**rozsah IP**" (v opačném případě změňte typ vpravo). Poté klikněte na tlačítko "**Start**".



![Image](assets/fr/019.webp)



O několik desítek sekund později bude výsledek viditelný v softwaru Interface. **Pro každou IP adresu Address v analyzovaném rozsahu uvidíte, zda program Angry IP Scanner detekoval hostitele, nebo ne.** Na obrazovce se také zobrazí souhrnný přehled s počtem aktivních hostitelů (v tomto případě 6) a počtem hostitelů s otevřenými porty.



![Image](assets/fr/020.webp)



Zde vidíme přítomnost hostitele s názvem "**OPNsense.local.domain**", přidruženého k IP adrese Address "**192.168.10.1**" a přístupného na **port 80** a **443** (HTTP a HTTPS). Kliknutím pravým tlačítkem myši na hostitele získáte přístup k dalším příkazům, jako je ping, trace route a otevření prohlížeče přes tuto IP adresu Address.



![Image](assets/fr/012.webp)



### C. Přidání skenovacích portů



Ve výchozím nastavení bude **Angry IP Scanner** skenovat 3 porty: **80** (HTTP), **443** (HTTPS) a **8080**. V předvolbách aplikace můžete přidat další skenované porty. Klikněte na nabídku "**Nástroje**" a poté na kartu "**Porty**".



Zde můžete upravit seznam portů pomocí možnosti "**Výběr portu**". Můžete **uvést konkrétní čísla portů oddělená čárkou nebo rozsahy portů**. Níže uvedený příklad přidává dva porty: **445** (SMB) a **389** (LDAP). Chcete-li skenovat porty od 1 do 1000, zadejte "**1-1000**". Není uvedeno, zda se skenování portů provádí v protokolu TCP, UDP nebo v obou.



![Image](assets/fr/021.webp)



Pokud kontrolu spustíte znovu, pravděpodobně získáte nové informace. V níže uvedeném příkladu mi program Angry IP Scanner sdělil, že na hostitelích "**SRV-ADDS-01**" a "**SRV-ADDS-02**" jsou otevřeny porty 389 a 445, a to díky nové konfiguraci skenovaných portů.



![Image](assets/fr/022.webp)



**Poznámka**: v nabídce "**Scanner**" můžete výsledky skenování exportovat do textového souboru.



Pokud chcete skenování posunout dále, klikněte na nabídku "**Tools**" a poté na "**Fetchers**". Tím se ke skenování přidají "schopnosti". Jednoduše vyberte fetcher a přesuňte jej doleva, abyste jej aktivovali. Tím se do výsledku skenování přidá další sloupec.



![Image](assets/fr/014.webp)



Níže uvedený příklad ukazuje funkce "**NetBIOS info**" a "**Web detection**". První z nich poskytuje další informace, například MAC Address a název domény počítače, zatímco druhá zobrazuje název webové stránky (který může naznačovat typ webového serveru nebo aplikace).



![Image](assets/fr/011.webp)



V předvolbách můžete také změnit metodu použitou pro "**ping**", tj. zohlednit, zda je hostitel aktivní, nebo ne. Protože někteří hostitelé na ping neodpovídají, můžete zde vyzkoušet i jiné metody (paket UDP, sondování portů TCP, ARP, kombinace UDP + TCP atd.).



## III. Závěr



Jednoduché a účinné: Angry IP Scanner detekuje hostitele připojené k síti a umožňuje konfigurovat skenování portů. Z hlediska možností není tak flexibilní jako Nmap a nejde tak daleko, ale pro rychlé skenování je to dobrý začátek.



Pokud chcete používat **Nmap** s grafickým Interface, můžete použít **aplikaci Zenmap** (viz přehled níže).



![Image](assets/fr/015.webp)



https://planb.network/tutorials/computer-security/communication/nmap-862300d7-6dfb-4660-970d-f56a9f58f60d