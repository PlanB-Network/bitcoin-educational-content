---
name: BTCPAY SERVER - Deštník
description: Instalace a používání BTCPAY SERVER v systému Umbrel pro přijetí Bitcoin a Lightning
---

![cover](assets/cover.webp)



V ekosystému Bitcoin představuje přijímání plateb pro obchodníky i podniky velkou výzvu. Tradiční řešení, ať už bankovní (kreditní karty, Stripe, PayPal), nebo dokonce Bitcoin (BitPay, Coinbase Commerce), vnucují zprostředkovatele, kteří vybírají značné poplatky, shromažďují vaše citlivé obchodní údaje a mohou BLOCK vaše transakce podle svého rozmaru cenzurovat. Tato závislost je v rozporu se základními principy Bitcoin, kterými jsou decentralizace, důvěrnost a finanční suverenita.



BTCPAY SERVER se stává open-source odpovědí na tento problém. Tento samostatně hostovaný platební procesor promění váš vlastní uzel Bitcoin v profesionální infrastrukturu bez prostředníka, bez dalších poplatků za zpracování a bez kompromisů v oblasti ochrany osobních údajů. BTCPAY SERVER, vyvíjený globální komunitou přispěvatelů od roku 2017, vám umožňuje přijímat platby Bitcoin a Lightning přímo do vašich peněženek, přičemž si vždy zachováváte plnou kontrolu nad svými prostředky.



Instalace systému BTCPAY SERVER tradičně vyžaduje pokročilé technické dovednosti: Konfigurace serveru Linux, ovládání nástroje Docker, správa certifikátů SSL a zabezpečení sítě. Společnost Umbrel přináší revoluci v tomto přístupu díky instalaci na jedno kliknutí, která je přímo integrovaná s vašimi systémy Bitcoin a LIGHTNING NODE. Toto zjednodušení zpřístupňuje každému to, co bylo dříve vyhrazeno zkušeným technikům.



**Důležité porozumět**: BTCPAY SERVER na Umbrel funguje ve výchozím nastavení pouze v místní síti. Můžete vytvářet faktury, přijímat platby Lightning a Bitcoin a spravovat účetnictví z libovolného zařízení připojeného k domácí síti (počítač, chytrý telefon, tablet). Tato konfigurace je ideální pro účtování osobních služeb, správu osobních plateb nebo používání BTCPAY SERVER z místní sítě. Na druhou stranu, chcete-li integrovat BTCPAY SERVER do internetového obchodu, který je veřejně přístupný na internetu, bude zapotřebí další konfigurace s veřejným vystavením (této problematice se budeme věnovat na konci výukového kurzu).



Tento výukový program vás provede kompletní instalací systému BTCPAY SERVER v systému Umbrel, konfigurací systémů Bitcoin Wallet a LIGHTNING NODE, vytvářením a placením faktur a správou účetních výkazů. Dozvíte se, jak efektivně používat BTCPAY SERVER v místní síti, a poté si povíme o řešeních pro veřejné zobrazení, pokud jej chcete integrovat s webem elektronického obchodu.



## Předpoklady



Abyste mohli postupovat podle tohoto návodu, musíte mít správně nainstalovanou a nakonfigurovanou aplikaci Umbrel. Pokud jste tak ještě neučinili, přečtěte si náš návod na instalaci Umbrelu.



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

Uzel Bitcoin core musí být plně synchronizován s uzlem Blockchain (100 % v aplikaci Bitcoin společnosti Umbrel). Tato počáteční synchronizace obvykle trvá 3 dny až 2 týdny v závislosti na vašem hardwaru a internetovém připojení.



Abyste mohli přijímat okamžité platby Lightning, musíte si také nainstalovat aplikaci LND (Lightning Network Daemon) v systému Umbrel. Pokud chcete tuto funkci povolit, podívejte se na náš návod na instalaci a konfiguraci LND v systému Umbrel.



https://planb.academy/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

Pro BTCPAY SERVER, jeho databáze a data Lightning vyčleňte alespoň 50 GB volného místa na disku. Důrazně se doporučuje stabilní připojení k internetu prostřednictvím ethernetového kabelu, aby nedocházelo k odpojování.



## Instalace BTCPAY SERVER na deštník



V aplikaci Umbrel Interface (`umbrel.local`) přejděte do obchodu s aplikacemi a v kategorii Bitcoin vyhledejte položku "BTCPAY SERVER".



![Interface Umbrel App Store avec BTCPay Server](assets/fr/01.webp)



Klikněte na tlačítko Instalovat. Umbrel automaticky zkontroluje, zda jsou Bitcoin core a LND nainstalovány, a poté zahájí nasazování (2-5 minut).



![Dépendances requises pour BTCPay Server](assets/fr/02.webp)



Po instalaci aplikaci otevřete. Budete muset vytvořit účet správce se silnými přihlašovacími údaji.



![Création du compte administrateur BTCPay Server](assets/fr/03.webp)



Po vytvoření účtu vás společnost BTCPAY SERVER okamžitě vyzve k nastavení prvního obchodu. Zvolte si profesionální název a vyberte referenční měnu (EUR, USD nebo BTC).



![Création du premier magasin BTCPay Server](assets/fr/04.webp)



## Přístup ke BTCPAY SERVER v místní síti



BTCPAY SERVER je přístupný z jakéhokoli zařízení v místní síti (WiFi nebo Ethernet). Přístup z prohlížeče na :



```url
http://umbrel.local
```



Nebo přímo na :



```url
http://umbrel.local:3003
```



**Dálkový přístup pomocí Tailscale**: Pro přístup ke BTCPAY SERVER odkudkoli na světě použijte Tailscale. Tato zabezpečená síť VPN vám umožní připojit se k zařízení Umbrel, jako byste byli v místní síti. Podívejte se na náš návod věnovaný nástroji Tailscale v zařízení Umbrel.



https://planb.academy/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

## Konfigurace portfolia Bitcoin



Chcete-li přijímat platby, musíte nakonfigurovat Bitcoin Wallet. BTCPAY SERVER zobrazuje možnosti konfigurace na ovládacím panelu.



![Tableau de bord avec options de configuration de portefeuille](assets/fr/05.webp)



Chcete-li nakonfigurovat Wallet Bitcoin, přejděte do části "Peněženky" > "Bitcoin".



Máte dvě možnosti: vytvořit nové portfolio přímo v BTCPay nebo importovat stávající portfolio. Pro import je k dispozici několik metod:




- Připojte Hardware Wallet** (doporučeno): Importujte své veřejné klíče prostřednictvím aplikace Trezor
- Importovat soubor Wallet** (doporučeno): Nahrajte exportovaný soubor ze svého portfolia
- Zadejte rozšířený veřejný klíč**: Zadejte svůj XPub/YPub/ZPub ručně
- Naskenujte QR kód Wallet** : Naskenujte QR kód z BlueWallet, Cobo Vault, Passport nebo Specter DIY
- Zadejte Wallet seed** (nedoporučuje se) : Zadejte 12- nebo 24slovnou frázi pro obnovení



![Options de création de portefeuille](assets/fr/06.webp)



V tomto tutoriálu vytvoříme nový klíč Hot Wallet: soukromý klíč bude proto uložen na našem serveru Umbrel. V tomto případě důrazně doporučujeme pravidelně přesouvat prostředky na Cold Wallet, abyste se vyhnuli ukládání velkých částek na serveru.



![Choix entre Hot wallet et Watch-only wallet](assets/fr/07.webp)



Po konfiguraci BTCPAY SERVER potvrdí, že váš Wallet je připraven přijímat platby On-Chain.



![Portefeuille Bitcoin configuré avec succès](assets/fr/08.webp)



## Aktivace Lightning Network



Chcete-li přijímat okamžité platby Lightning, přejděte do nabídky Peněženky > Lightning. Poté, protože váš uzel LND je již na místě v Umbrel, jednoduše klikněte na tlačítko "Uložit", abyste potvrdili spojení mezi vaším BTCPAY SERVER a LIGHTNING NODE.



![Configuration du nœud Lightning](assets/fr/09.webp)



## Vytvářet a platit faktury



V okně Interface BTCPAY SERVER přejděte do nabídky Faktury > Vytvořit Invoice. Zadejte částku, přidejte volitelný popis a klikněte na tlačítko Vytvořit.



![Création d'une nouvelle facture](assets/fr/10.webp)



Poté můžete kliknout na tlačítko "Checkout" a zobrazit si Invoice. BTCPay poté vygeneruje Invoice s jednotným QR kódem (BIP21) obsahujícím Bitcoin Address a blesk Invoice.



![Détails de la facture générée](assets/fr/11.webp)



Zákazník může QR kód naskenovat jakýmkoli kompatibilním zařízením Wallet.



![Page de paiement avec QR code](assets/fr/12.webp)



Po zaplacení se účet Invoice během několika vteřin stane "vypořádaným" účtem pro službu Lightning.



![Confirmation de paiement réussi](assets/fr/13.webp)



## Správa a sledování plateb



V části "Reporting", na kartě "Invoices" najdete kompletní historii faktur s datem, částkou, stavem a způsobem platby. V případě potřeby ji můžete exportovat.



![Section reporting avec l'historique des factures](assets/fr/14.webp)



## Konfigurace obchodu



BTCPAY SERVER umožňuje spravovat více skladů s odlišnými parametry. Každý obchod představuje samostatný obchodní subjekt: e-shop, fyzické prodejní místo nebo fakturaci služeb.



V nastavení obchodu najdete několik důležitých sekcí:



![Paramètres du magasin](assets/fr/15.webp)





- Obecná nastavení**: Název obchodu, referenční měna (BTC, EUR, USD), doba platnosti Invoice (výchozí 15 minut), počet požadovaných potvrzení Blockchain
- Sazby**: Konfigurace zdrojů sazeb Exchange a převodů fiat/Bitcoin
- Vzhled pokladny**: Přizpůsobte si vzhled svých pokladních stránek (logo, barvy, personalizované zprávy)
- Nastavení e-mailu**: Konfigurace e-mailových oznámení o přijatých platbách
- Přístupové tokeny**: API Správa token pro integrace s elektronickými obchody (WooCommerce, Shopify atd.)
- Uživatelé**: Spravujte přístup uživatelů do obchodu s různými úrovněmi oprávnění (vlastník, host)
- Webové háčky**: Konfigurace webových háčků pro synchronizaci s účetním nebo ERP systémem v reálném čase



BTCPAY SERVER nabízí také sekci Plugins, která rozšiřuje funkčnost o integrace s elektronickým obchodem, systémy pro prodejní místa a další nástroje.



![Gestion des plugins](assets/fr/16.webp)



## Výhody a omezení místního použití



**Výhody BTCPAY SERVER na deštníku** :




- Naprostá suverenita: výhradní kontrola nad soukromými klíči a finančními prostředky, žádná třetí strana nemůže zmrazit nebo cenzurovat vaše platby
- Výrazné úspory: pouze Bitcoin síťových nákladů (několik centů u Lightningu) oproti 2-3 % u tradičních procesorů
- Maximální důvěrnost: žádná registrace, ověřování totožnosti ani sdílení údajů se společnostmi třetích stran
- Architektura s otevřeným zdrojovým kódem zaručuje transparentnost, auditovatelnost a udržitelnost díky velké komunitě vývojářů
- Snadná instalace pomocí nástroje Umbrel bez nutnosti pokročilých technických dovedností



**Důležitá omezení** :




- Pouze místní síť**: BTCPAY SERVER na Umbrelu je přístupný pouze z domácí sítě. Ideální pro osobní fakturaci, služby na volné noze nebo malé fyzické podniky, ale nevhodné pro online obchody, které jsou veřejně přístupné na internetu.
- Plná technická odpovědnost: údržba uzlů, pravidelné zálohování, monitorování připojení
- Řízení bleskové likvidity: otevření a správa kanálů s dostatečnou příchozí kapacitou
- Podpora omezená na komunitní dokumentaci a fóra, což vyžaduje větší samostatnost než komerční oddělení služeb zákazníkům



Toto omezení sítě LAN je hlavní překážkou integrace systému BTCPAY SERVER do elektronického obchodu, kde zákazníci potřebují mít přístup k platebním stránkám odkudkoli na internetu.



## Osvědčené postupy a bezpečnost



Aktivujte automatické zálohování Umbrel a uložte kopii na externí médium (USB disk, disk Hard, šifrovaný cloud). Semínka Bitcoin (fráze pro obnovení) uchovávejte na bezpečném, fyzicky odděleném místě. Uložte soubor LND channel.backup pro bleskové obnovení.



Pravidelně sledujte synchronizaci Bitcoin core, kanály Lightning a odezvu BTCPAY SERVER. Jednoduchý týdenní test: generate a zaplaťte účet za několik satošů. Udržujte Umbrel v aktuálním stavu (bezpečnostní záplaty, vylepšení). Před většími aktualizacemi proveďte zálohu. Pro profesionální použití zvažte externí monitorování (UptimeRobot) s upozorněními e-mailem/SMS.



## Zobrazit BTCPAY SERVER veřejně pro online obchod



Chcete-li integrovat BTCPAY SERVER do webového e-shopu (WooCommerce, Shopify atd.), musí mít vaši zákazníci přístup k platebním stránkám odkudkoli, nejen z vaší místní sítě.



**Řešení: Nginx Proxy Manager**



Službu BTCPAY SERVER můžete veřejně vystavit pomocí nástroje Nginx Proxy Manager (dostupný v obchodě s aplikacemi Umbrel). Toto řešení vyžaduje :




- Název domény (klasický nebo zdarma přes DuckDNS, No-IP, Afraid.org)
- Konfigurace přesměrování portů (porty 80 a 443) na směrovači
- Instalace Správce proxy serveru Nginx, který automaticky spravuje certifikáty SSL



Tato konfigurace vystavuje server internetu a vyžaduje zvýšenou ostražitost (silná hesla, 2FA, pravidelné aktualizace). Připravujeme speciální výukový program s podrobným popisem tohoto kompletního postupu.



## Závěr



BTCPAY SERVER na platformě Umbrel kombinuje výkon uzlu Bitcoin s jednoduchostí platformy Umbrel a vytváří tak profesionální platební infrastrukturu dostupnou všem. Tato finanční suverenita s sebou nese odpovědnost za údržbu, ale Umbrel značně zjednodušuje provozní zátěž ve srovnání s výhodami: eliminace poplatků za zpracování, ochrana soukromí, odolnost vůči cenzuře a úplná kontrola nad finančními prostředky.



Využití místní sítě již zahrnuje širokou škálu aplikací: účtování služeb na volné noze, platby tváří v tvář, malé fyzické obchody nebo prosté učení a experimentování s Bitcoin a Lightning v kontrolovaném prostředí. Pro potřeby elektronického obchodování vyžadující veřejné vystavení existuje řešení Nginx Proxy Manager, které však vyžaduje další technickou konfiguraci, kterou podrobně popíšeme ve speciálním tutoriálu.



Ať už provozujete firmu, začínající projekt, nebo jen experimentujete, BTCPAY SERVER on Umbrel nabízí naprostou finanční nezávislost. Cesta začíná prvním obchodem, prvním Invoice, první platbou přijatou přímo do vaší suverénní infrastruktury.



## Zdroje



### Oficiální dokumentace




- [oficiální stránky BTCPAY SERVER](https://btcpayserver.org)
- [Kompletní dokumentace BTCPAY SERVER](https://docs.btcpayserver.org)
- [GitHub BTCPAY SERVER](https://github.com/btcpayserver/btcpayserver)
- [dokumentace Tailscale](https://tailscale.com/kb)


### Společenství a podpora




- [Fórum BTCPAY SERVER](https://chat.btcpayserver.org)
- [Fórum Deštník](https://community.getumbrel.com)
- [Reddit r/BTCPayServer](https://reddit.com/r/BTCPayServer)