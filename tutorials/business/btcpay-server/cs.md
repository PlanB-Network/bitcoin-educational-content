---
name: BTCPay Server
description: Přijímání plateb BTC bez zprostředkovatelů
---

![cover](assets/cover.webp)



![video](https://youtu.be/KqsM-n-e4aY)



BTCPay Server je bezplatný softwarový balíček s otevřeným zdrojovým kódem, který vytvořil Nicolas Dorier a který umožňuje přijímat bitcoinové platby bez zprostředkovatelů. Je navržen tak, aby nabízel autonomii a finanční suverenitu, instaluje se na vlastním serveru a zajišťuje kompletní správu transakcí, od fakturace po ověřování plateb on-chain nebo Lightning Network a účtování. Snadno se integruje s weby e-commerce (WooComerce, Shopify atd.) nebo jej lze použít jako platební terminál pro fyzické obchody (*POS*).



Server BTCPay je bezpochyby nejpokročilejším řešením pro obchodníky, kteří chtějí přijímat bitcoiny. Jedná se o nejkomplexnější a nejrobustnější software z hlediska bezpečnosti, suverenity a důvěrnosti. Na druhou stranu je také nejsložitější na instalaci a údržbu. Existují i jednodušší alternativy: některé jsou zcela opatrovnické, jako například OpenNode, zatímco jiné nabízejí zajímavý kompromis mezi snadností použití a suverenitou, jako například švýcarský Bitcoin Pay :



https://planb.academy/tutorials/business/point-of-sale/swiss-bitcoin-pay-2-a78b057e-ed11-47ac-860c-71019fcb451a

Cílem tohoto návodu je provést vás krok za krokem instalací, konfigurací a používáním BTCPay Serveru, abyste mohli nasadit bezpečnou a nezávislou platební infrastrukturu v souladu s étosem Bitcoin.



## Funkce serveru BTCPay



Centralizovaná řešení pro prodejní místa Bitcoin, jako je například *OpenNode*, nabízejí snadné použití, ale jsou závislá na společnosti třetí strany, protože je nelze hostovat samostatně a ve většině případů jsou proprietární. Usnadňují sice nastavení plateb, ale zahrnují poplatky za provizi a vystavují své uživatele větším rizikům než řešení, jako je BTCPay Server, a to jak z hlediska úschovy finančních prostředků, tak z hlediska důvěrnosti.



Server BTCPay je určen pro online nebo fyzické obchodníky, sdružení a neziskové organizace, které chtějí přijímat dary v bitcoinech. Je také ideálním řešením pro vlastníky projektů a vývojáře, kteří chtějí získat přímou podporu od své komunity.



Mezi speciální funkce serveru BTCPay patří :




- jeho **úplná autonomie**,
- neexistence postupu **KYC**,
- plnou kontrolu nad finančními prostředky**,
- **odstranění poplatků za platformu**.



Tím, že se stanete vlastním zpracovatelem plateb, eliminujete jakoukoli závislost na centralizované třetí straně mezi vámi a vašimi zákazníky. Můžete přijímat platby přímo v bitcoinech a generate platebních fakturách. Tím je zajištěno, že vás ani vaši společnost nemůže nikdo jiný zakázat. Hrajete roli banky i zpracovatele plateb, aniž byste museli za každou transakci platit provizi zprostředkovateli.



Transakční poplatky za **on-chain** zůstávají zachovány, ale lze je snížit použitím sítě **Liquid** nebo **Lightning**.



Kromě toho :




- Plně přizpůsobitelné rozhraní a faktury;
- Nativní podpora **Tor** pro zvýšení důvěrnosti;
- Podpora pro **crowdfunding**, **POS** a **tlačítka pro platby**;
- Kompatibilní s mnoha měnami ;
- Bitcoin přímé platby a platby peer-to-peer ;
- Úplná kontrola nad soukromými klíči;
- Zvýšená ochrana soukromí ;
- Zvýšené zabezpečení ;
- Samostatně hostovaný software ;
- Podpora pro **SegWit** a **Síť Lightning** ;
- Interní portfolio založené na uzlech s integrací portfolia hardwaru.



## Instalace a konfigurace serveru BTCPay



### Výběr režimu hostování



Server BTCPay lze nainstalovat několika různými způsoby. V závislosti na vašich potřebách a zdrojích existují tři hlavní možnosti:




- Server BTCPay hostovaný třetí stranou**: používáte platformu, která pro vás službu hostuje. Je to jednoduché, ale obvykle to není zadarmo.
- BTCPay Server hostovaný na cloudovém serveru** (např. prostřednictvím [btcpayprovider](https://btcpayprovider.com/), [Bitcoin People](http://bitcoinpeople.it/) nebo jiného poskytovatele). Toto je doporučené řešení pro většinu začínajících obchodníků.
- BTCPay Server nainstalovaný na vašem vlastním hardwaru (lokálně)** : na počítači, mini PC nebo Umbrelu. Tento způsob je technicky náročnější, ale nabízí naprostou nezávislost.



https://planb.academy/tutorials/business/point-of-sale/btcpay-server-umbrel-68e1c535-4322-4507-a69c-9dfcbc36dfd1

Pro začínajícího obchodníka je **nasazení na cloudový server** nejlepším kompromisem mezi samostatností, jednoduchostí a bezpečností, aniž by musel spravovat celou technickou infrastrukturu.



Server BTCPay lze rychle nasadit u řady poskytovatelů hostingu. Mezi nimi vyniká **Voltage** jako referenční řešení pro uživatele, kteří vyžadují **spolehlivou**, **profesionální** a **vysokou** infrastrukturu.



### Vytvoření instance serveru BTCPay na serveru Voltage



**Voltage** je hostingová platforma Bitcoin a Lightning na klíč, která vám umožní okamžitě nasadit vlastní server BTCPay bez složité konfigurace a údržby serveru.



Navštivte [oficiální webové stránky Voltage](https://voltage.cloud).



![capture](assets/fr/03.webp)



Vytvořte si **uživatelský účet** s platnou e-mailovou adresou a silným heslem.



![capture](assets/fr/04.webp)



Voltage nabízí **bezplatnou 7denní zkušební verzi**. Vezměte prosím na vědomí, že po uplynutí 7denní bezplatné zkušební doby budete vyzváni k registraci pevného předplatného ve výši **25 USD měsíčně**, abyste mohli nadále **udržovat své uzly aktivní**.



Po vytvoření účtu Voltage a prvním přihlášení budete přesměrováni na domovskou stránku, která má dvě hlavní části:




- Sekce **Infrastruktura** pro správu uzlů Lightning, jádra Bitcoin, serveru BTCPay a dalších služeb Bitcoin v cloudu;
- a sekci **Platby**, která umožňuje přístup k aplikaci API Lightning společnosti Voltage a integraci plateb Bitcoin do přizpůsobených aplikací.



Chcete-li nasadit instanci serveru **BTCPay**, klikněte na možnost **Přístupová infrastruktura**. Zde můžete vytvořit, spravovat a monitorovat všechny své služby, včetně uzlu Bitcoin a serveru BTCPay.



#### Vytvoření skupiny



Před nasazením služby vás platforma vyzve k **vytvoření skupiny**. Skupina** (pracovní prostor) je pracovní prostor, který seskupuje všechny vaše služby Bitcoin a Lightning (např. uzel, server BTCPay, průzkumník atd.). Je to něco jako složka obsahující vaše různé projekty.



![capture](assets/fr/05.webp)



Pro účely tohoto výukového programu se bude vytvořená skupina jmenovat **Genesis**. Pokud chcete, můžete přidat profilový obrázek. Jakmile tak učiníte, klikněte na tlačítko **Vytvořit**. Do skupiny můžete pozvat další uživatele, a pokud chcete, můžete změnit i její název.



Na domovské stránce skupiny se zobrazí několik možností:




- Uzly Lightning** : nasazení kompletního uzlu Lightning (LND) ;
- Základní uzly Bitcoin** : spuštění kompletního uzlu Bitcoin ;
- BTCPay Server** : hostování instance BTCPay připravené k použití;
- Účty Nostr**: správa identit Nostr.



Aktivujte **dvojité ověřování (2FA)** pro zabezpečení svého účtu a služeb (pokud je tlačítko deaktivováno, je viditelné červeně).



![capture](assets/fr/06.webp)



Mezi možnostmi klikněte na **BTCPay Server** a poté na **Spustit obchod BTCPay**.



![capture](assets/fr/07.webp)



Voltage vás poté vyzve k **vytvoření a konfiguraci instance serveru BTCPay** výběrem **názvu služby** (1) a povolením plateb Lightning (2).



Pokud se rozhodnete přijímat platby Lightning, budete potřebovat uzel Lightning.



Pokud ještě nemáte uzel Bitcoin nebo Lightning, Voltage vám nabídne jeho automatické vytvoření.



Klikněte na **Vytvořit uzel Lightning** (3) .



![capture](assets/fr/08.webp)



V rozhraní pro vytváření uzlů budete vyzváni k výběru mezi **standardním** a **profesionálním** rozložením.



Můžete vytvořit skutečný uzel (**Mainnet**) nebo testovací uzel (**Testnet**). Poté klikněte na tlačítko **Pokračovat**.



![capture](assets/fr/09.webp)



Pro tento výukový program použijeme standardní plán. Zadejte **název uzlu**, **heslo** a stiskněte tlačítko **Vytvořit**.



![capture](assets/fr/10.webp)



Po několika okamžicích bude váš uzel zprovozněn a vy budete moci otevřít volný kanál s kapacitou příjmu 500 000 sats.



![capture](assets/fr/11.webp)



O něco níže vpravo najdete všechny potřebné informace o uzlu!



![capture](assets/fr/12.webp)



Nyní, když jsme zprovoznili náš uzel Lightning, se vraťme k instalaci našeho serveru BTCPay. Nyní můžete kliknout na tlačítko **Vytvořit BTCPay**.



![capture](assets/fr/13.webp)



Otevře se stránka s výchozími přihlašovacími údaji a zprávou vyzývající ke změně původního hesla. Jakmile tak učiníte, klikněte na tlačítko **Přihlásit se nyní** a získáte přístup do svého rozhraní.



![capture](assets/fr/14.webp)



A je to! Váš server BTCPay je připraven k použití. Budete přesměrováni přímo na přihlašovací stránku vašeho serveru BTCPay.



![capture](assets/fr/15.webp)



Po přihlášení nakonfigurujte svůj první **obchod**:





- Dejte mu **jméno**.





- Zvolte **výchozí měnu** (EUR, USD, CFA atd.).





- Vyberte **poskytovatele směnných kurzů** (např. CoinGecko).



![capture](assets/fr/16.webp)



Poté budete přesměrováni na ovládací panel svého obchodu. V rozhraní ovládacího panelu si všimněte, že tlačítko **Vytvořit obchod** je označeno zeleně, protože tento krok již byl dokončen.



![capture](assets/fr/17.webp)



O něco níže jsou tlačítka **Konfigurace wallet** a **Konfigurace uzlu Lightning**. V našem případě jsme se již připojili k uzlu Lightning běžícímu na napětí. Zde to tedy nebudeme muset dělat.



Přejděme ke konfiguraci portfolia. Klikněte na tlačítko **Konfigurace portfolia**.



Protože se serverem BTCPay teprve začínáme, připojíme existující server wallet. Stiskněte tedy tlačítko **Připojit existující portfolio**.



![capture](assets/fr/18.webp)



Poté musíte zvolit metodu **importu**. Z dostupných možností vyberte možnost **Vložit rozšířený veřejný klíč**.



![capture](assets/fr/19.webp)



Propojením stávajícího účtu wallet můžete přijímat platby **přímo na tomto externím účtu wallet**, aniž by server BTCPay měl přístup k vašemu soukromému klíči. Takže i kdyby došlo k hacknutí serveru nebo kompromitaci veřejného klíče (`xpub`), útočník by si mohl prohlédnout historii vašich transakcí, ale neměl by **možnost dostat se k vašim penězům**.



Po kliknutí na tlačítko **Vložit rozšířený veřejný klíč** budete **přesměrováni** na stránku, kde musíte tento klíč zadat.



Nyní získáme **rozšířený veřejný klíč**.



### Připojení zařízení Bitcoin wallet



Abyste mohli přijímat platby, musíte ke svému obchodu připojit zařízení Bitcoin wallet. K tomu máte několik možností:





- Portfolio hardwaru** (Ledger, Trezor, Coldcard...) ;





- Portfolio softwaru** (Blockstream App, Ashigaru, Electrum, Sparrow...)





- Interní server BTCPay** wallet (nedoporučuje se, protože je méně bezpečný a v případě napadení serveru vystavuje vaše prostředky většímu riziku).



V tomto tutoriálu budeme používat **softwarové portfolio**, které je pro počáteční konfiguraci přístupnější. Můžete si vybrat z řady kompatibilních aplikací: **Electrum**, **Phoenix**, **Zeus**, **Muun** atd.



Pro demonstraci použijeme **Electrum**. Otevřete **Electrum**, klikněte na **Portfolio** a poté na **Informace** :



![capture](assets/fr/20.webp)



Poté zkopírujte **veřejný klíč master (xpub)**.



![capture](assets/fr/21.webp)



Po zkopírování hlavního veřejného klíče jej vložte do pole na stránce serveru BTCPay.



![capture](assets/fr/22.webp)



Po ověření budete přesměrováni na ovládací panel svého obchodu.



![capture](assets/fr/23.webp)



### Generování prodejního místa (PoS)



Po nastavení obchodu a portfolia si můžete nastavit **Místo prodeje (PoS)** a začít přijímat platby Bitcoin přímo od zákazníků.



Tato integrovaná funkce **BTCPay Serveru** je ideální pro **obchodníky, řemeslníky, restauratéry nebo poskytovatele služeb**, kteří chtějí přijímat Bitcoin **bez webových stránek** nebo zvláštních technických dovedností.



### Jaké je místo prodeje?



**PoS** je **zjednodušené pokladní rozhraní**, které funguje jako platební terminál **Bitcoin**.


Umožňuje vám :




- Vytvoření **nabídky produktů nebo služeb** s pevně stanovenými cenami.
- Vygenerujte **momentální fakturu s QR kódem**, který naskenujete.
- Sdílejte adresu **Payment URL** dostupnou prostřednictvím chytrého telefonu, tabletu nebo počítače.



Jinými slovy, PoS promění váš server BTCPay v **přímé prodejní rozhraní**, kde je každá platba přijata **ve vašem vlastním Bitcoin wallet**, bez prostředníků.



### Konfigurace PoS



Na hlavním panelu BTCPay klikněte na **PLUGINS** a poté na **Point of sale**.



Poté klikněte na možnost **Vytvořit novou aplikaci PoS**. Tato akce přidá **novou aplikaci** do vašeho obchodu BTCPay, jako byste instalovali miniaturní interní prodejní stránku.



Otevře se stránka pro vytvoření aplikace. Definujte **název aplikace**: jedná se o interní název viditelný pouze z ovládacího panelu (např. _Shoe Shop_).



Kliknutím na tlačítko **Vytvořit** proveďte ověření.



![capture](assets/fr/24.webp)



Po vytvoření budete přesměrováni na stránku **Podrobná konfigurace** prodejního místa.



### Přizpůsobení prodejního rozhraní



Na této stránce můžete definovat základní prvky své PoS:





- Název aplikace** (interní název pro správu, lze kdykoli změnit).





- Zobrazení nadpisu** (to, co zákazníci uvidí v horní části stránky).





- Styl prodejního místa** (režim **Popis** je vhodný pro služby, jako je kadeřnictví nebo stravování, zatímco režim **Katalog produktů** je ideální pro obchody nabízející několik položek).





- Zobrazení měny** (vyberte **XOF**, **EUR** nebo **USD** podle svých obvyklých cen).





- Seznam produktů** (zde přidejte své produkty, popisy a ceny).



![capture](assets/fr/25.webp)



![capture](assets/fr/26.webp)



### Uložení a otestování PoS



Po dokončení konfigurace klikněte na tlačítko **Uložit** pro uložení nastavení a poté na tlačítko **Zobrazit** pro zobrazení náhledu PoS.



Zobrazí se stránka s prezentací vašich produktů, přičemž každé tlačítko odpovídá jedné položce nebo službě.



Jakmile si zákazník vybere produkt :



1. BTCPay automaticky generuje fakturu Bitcoin nebo Lightning**.



2. Na obrazovce se zobrazí **QR kód**.



3. Zákazníci mohou **skenovat a platit přímo** pomocí svého zařízení Bitcoin wallet.




![capture](assets/fr/27.webp)



### Konečný výsledek



Nyní máte k dispozici kompletní prodejní místo **Bitcoin**, které můžete :





- Otevřete ze smartphonu nebo tabletu ve svém obchodě ;





- Zobrazení na obrazovce, kterou zákazník naskenuje;





- Nebo sdílejte prostřednictvím veřejné **URL**, například zjednodušené stránky objednávky.



Při každé platbě je částka automaticky připsána na **vaš vlastní účet BTCPay wallet**, bez zprostředkovatelů nebo poplatků třetích stran.


Tím se z vašeho PoS stane **samostatný platební terminál Bitcoin**.




## Každodenní použití



Před proplacením skutečných plateb doporučujeme provést **test** a zkontrolovat, zda vše funguje správně.



### Testování platby





- Vytvořte fakturu** z rozhraní PoS (například produkt 1 satoshi nebo malou částku).





- Naskenujte kód QR** na obrazovce pomocí zařízení Bitcoin nebo Lightning wallet (například **Phoenix**, **Muun** nebo **Wallet z Satoshi**).




![capture](assets/fr/28.webp)





- Ověřte platbu** v wallet: transakce se odešle okamžitě.





- Návrat na server BTCPay**: faktura se v seznamu zobrazí jako **Zaplaceno**.



![capture](assets/fr/29.webp)



Gratulujeme! Vaše prodejní místo je nyní **funkční**. Můžete začít přijímat platby Bitcoin od svých zákazníků, a to jednoduše, rychle a bez zprostředkovatelů.



### Vytvoření faktury pro zákazníka



V nabídce **Faktury** klikněte na možnost **Nová faktura**.



![capture](assets/fr/30.webp)



Zadejte **částku** a **místní měnu** (BTCPay automaticky vypočítá ekvivalent v BTC) a další informace o produktu.



![capture](assets/fr/31.webp)



Sdílejte se zákazníkem **QR kód** nebo **URL**.



![capture](assets/fr/32.webp)



### Sledování přijatých plateb



V nabídce **Faktury** se stále zobrazuje seznam všech vašich transakcí.


Možné stavy jsou :





- Čekající**: platba ještě nebyla potvrzena.





- Zaplaceno**: platba potvrzena.





- Prošlá**: faktura, která nebyla uhrazena do data splatnosti.



### Vrácení peněz zákazníkovi



V nabídce **Faktury** vyberte fakturu, která má být proplacena.



![capture](assets/fr/33.webp)



Klikněte na **Vrácení** a zadejte adresu Bitcoin, kterou vám zákazník poskytl.



![capture](assets/fr/34.webp)



![capture](assets/fr/35.webp)



### Reporty a export dat



Server BTCPay umožňuje **exportovat vaše transakce** (ve formátu CSV nebo Excel). To je velmi praktické pro vaše účetnictví a následnou pokladnu.



![capture](assets/fr/36.webp)



V nabídce **Report** klikněte na **Export**: všechny transakce se uloží do souboru CSV, který si pak můžete prohlédnout lokálně.



## Bezpečnost a osvědčené postupy



Autonomie serveru BTCPay (plná svrchovanost nad vašimi prostředky) je skutečně silnou stránkou. S touto svobodou však přichází i větší odpovědnost z hlediska bezpečnosti. Správou vlastních plateb přebíráte roli vlastní banky. Proto je nezbytné přijmout osvědčené postupy na ochranu vašich prostředků, dat a infrastruktury. Zde jsou hlavní body, které je třeba zvážit.



### Zabezpečený přístup k serveru





- Používejte silné heslo: kombinujte velká a malá písmena, číslice a speciální znaky. Vyhněte se opakovanému použití stávajícího hesla.
- Aktivujte dvoufaktorové ověřování (2FA) pro přístup k rozhraní BTCPay.
- Pravidelně aktualizujte operační systém, instanci BTCPay Serveru a závislosti (Docker, uzel Bitcoin, uzel Lightning...). Aktualizace často opravují bezpečnostní chyby.



### Správa a zálohování soukromých klíčů





- Soukromé klíče a seedfráze ukládejte offline na fyzická média (papír nebo kov).
- Použijte nejlépe hardware wallet wallet.
- Uchovávejte několik kopií záloh na oddělených, chráněných fyzických místech.



### Bezpečné platby a důvěrnost





- Pomocí sítě Tor nebo VPN můžete skrýt IP adresu serveru a chránit své soukromí.
- Zakažte na serveru nepotřebné porty a omezte připojení SSH pouze na důvěryhodné adresy.
- Aktivujte HTTPS (SSL certifikát) pro všechna připojení k webovému rozhraní BTCPay.
- Nikdy nesdílejte rozhraní pro správu s pracovníky, kteří nejsou vyškoleni ve správě portfolia Bitcoin.



### Zavedení osvědčených postupů pro síť Lightning



Váš obchod je připojen k uzlu **Lightning hostovanému na platformě Voltage**, což výrazně zjednodušuje technickou správu sítě. Přesto je i nadále důležité přijmout **dobré monitorovací a bezpečnostní postupy**:





- Uložte si přihlašovací a přístupové klíče API** uzlu Voltage (které umožňují připojení k BTCPay).
- Chraňte svůj účet Voltage** pomocí dvoufaktorového ověřování a silného hesla.
- Sledování stavu uzlů a kanálů** z ovládacího panelu Voltage: to vám pomůže odhalit případné anomálie nebo desynchronizaci.
- Vyvarujte se sdílení svých přihlašovacích údajů API** nebo jejich veřejného vystavení (např. v kódu webu).
- V případě migrace stačí **znovu nakonfigurovat spojení mezi BTCPay a Voltage**: žádný kanál není třeba ručně uzavírat.



Se službou Voltage můžete využívat **zabezpečenou, vysoce dostupnou** a **automaticky zálohovanou** infrastrukturu a zároveň si zachovat **plnou suverenitu nad svými platbami Lightning**.



### Organizovat a strukturovat interní postupy





- Definujte jasnou politiku správy přístupu: kdo může vytvářet faktury, zobrazovat platby, přistupovat k uzlu atd.
- Zdokumentujte postupy zálohování a obnovy, abyste mohli v případě incidentu rychle reagovat.
- Pravidelně testujte obnovení záloh a ujistěte se, že fungují správně.
- Proškolte své zaměstnance nebo spolupracovníky v základním zabezpečení provozu: ostražitost vůči phishingu, používání bezpečných hesel, dodržování důvěrnosti.



### Dohlížet na průběžnou údržbu a zajišťovat ji





- Průběžně sledujte činnost serveru pomocí protokolovacích nebo monitorovacích nástrojů.
- Naplánujte pravidelnou kontrolu zabezpečení: zkontrolujte aktualizace, přístup, zálohování a konzistenci transakcí.



Gratulujeme! Dostali jste se na konec tohoto návodu. Nyní se můžete se serverem BTCPay seznámit sami, což vám usnadní správu vašeho obchodu.



Chcete-li se dozvědět více, doporučuji vám absolvovat naše kompletní školení o integraci Bitcoin do vaší společnosti:



https://planb.academy/courses/a804c4b6-9ff5-4a29-a530-7d2f5d04bb7a