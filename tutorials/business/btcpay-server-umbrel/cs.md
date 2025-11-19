---
name: Server BTCPay - Umbrel
description: Instalace a používání serveru BTCPay v systému Umbrel pro přijímání plateb Bitcoin a Lightning
---

![cover](assets/cover.webp)



V ekosystému Bitcoin představuje přijímání plateb pro obchodníky i podniky velkou výzvu. Tradiční řešení, ať už bankovní (kreditní karty, Stripe, PayPal), nebo dokonce Bitcoin (BitPay, Coinbase Commerce), vnucují zprostředkovatele, kteří vybírají značné poplatky, shromažďují vaše citlivé obchodní údaje a mohou vaše transakce podle svého rozmaru blokovat nebo cenzurovat. Tato závislost je v rozporu se základními principy Bitcoin, kterými jsou decentralizace, důvěrnost a finanční suverenita.



BTCPay Server se stává open-source odpovědí na tento problém. Tento samostatně hostovaný platební procesor promění váš vlastní uzel Bitcoin v profesionální infrastrukturu, bez prostředníka, bez dalších poplatků za zpracování a bez kompromisů v oblasti soukromí. BTCPay Server, vyvíjený globální komunitou přispěvatelů od roku 2017, vám umožňuje přijímat platby Bitcoin a Lightning přímo do vašich peněženek, přičemž si vždy zachováváte plnou kontrolu nad svými prostředky.



Instalace BTCPay Serveru tradičně vyžaduje pokročilé technické dovednosti: Konfigurace linuxového serveru, ovládání Dockeru, správa SSL certifikátů a zabezpečení sítě. Umbrel přináší revoluci v tomto přístupu díky instalaci jedním kliknutím přímo integrované s vaším uzlem Bitcoin a Lightning. Toto zjednodušení zpřístupňuje každému to, co bylo dříve vyhrazeno zkušeným technikům.



**Důležité porozumět**: BTCPay Server na Umbrel funguje ve výchozím nastavení pouze v místní síti. Můžete vytvářet faktury, přijímat platby Lightning a Bitcoin a spravovat účetnictví z libovolného zařízení připojeného k domácí síti (počítač, chytrý telefon, tablet). Tato konfigurace je ideální pro účtování osobních služeb, správu osobních plateb nebo používání serveru BTCPay Server z místní sítě. Na druhou stranu, chcete-li integrovat BTCPay Server do internetového obchodu, který je veřejně přístupný na internetu, bude zapotřebí další konfigurace s veřejným vystavením (této problematice se budeme věnovat na konci návodu).



Tento návod vás provede kompletní instalací serveru BTCPay na platformě Umbrel, konfigurací uzlu Bitcoin wallet a Lightning, vytvářením a placením faktur a správou účetních výkazů. Zjistíte, jak efektivně používat BTCPay Server v místní síti, a poté se podíváme na řešení pro veřejné zobrazení, pokud jej chcete integrovat s webem elektronického obchodu.



## Předpoklady



Abyste mohli postupovat podle tohoto návodu, musíte mít správně nainstalovanou a nakonfigurovanou aplikaci Umbrel. Pokud jste tak ještě neučinili, přečtěte si náš návod na instalaci Umbrelu.



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

Váš uzel Bitcoin Core musí být plně synchronizován s blockchainem (100 % v aplikaci Bitcoin společnosti Umbrel). Tato počáteční synchronizace obvykle trvá 3 dny až 2 týdny, v závislosti na vašem hardwaru a internetovém připojení.



Abyste mohli přijímat okamžité platby Lightning, je třeba do aplikace Umbrel nainstalovat také modul LND (Lightning Network Daemon). Pokud chcete tuto funkci povolit, podívejte se na náš návod na instalaci a konfiguraci LND v systému Umbrel.



https://planb.academy/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

Pro server BTCPay, jeho databáze a data Lightningu si vyhraďte alespoň 50 GB volného místa na disku. Důrazně doporučujeme stabilní připojení k internetu prostřednictvím ethernetového kabelu, aby nedocházelo k odpojování.



## Instalace serveru BTCPay na Umbrel



V rozhraní Umbrel (`umbrel.local`) přejděte do App Store a v kategorii Bitcoin vyhledejte "BTCPay Server".



![Interface Umbrel App Store avec BTCPay Server](assets/fr/01.webp)



Klikněte na tlačítko Instalovat. Umbrel automaticky zkontroluje, zda jsou nainstalovány Bitcoin Core a LND, a poté zahájí nasazování (2-5 minut).



![Dépendances requises pour BTCPay Server](assets/fr/02.webp)



Po instalaci aplikaci otevřete. Budete muset vytvořit účet správce se silnými přihlašovacími údaji.



![Création du compte administrateur BTCPay Server](assets/fr/03.webp)



Po vytvoření účtu vás server BTCPay okamžitě vyzve k nastavení prvního obchodu. Zvolte název obchodu a vyberte referenční měnu (EUR, USD nebo BTC).



![Création du premier magasin BTCPay Server](assets/fr/04.webp)



## Přístup k serveru BTCPay v místní síti



Server BTCPay je přístupný z jakéhokoli zařízení v místní síti (WiFi nebo Ethernet). Přístup z prohlížeče na :



```url
http://umbrel.local
```



Nebo přímo na :



```url
http://umbrel.local:3003
```



**Dálkový přístup pomocí Tailscale**: Pro přístup k serveru BTCPay odkudkoli na světě použijte Tailscale. Tato zabezpečená síť VPN vám umožní připojit se k Umbrelu, jako byste byli v místní síti. Podívejte se na náš návod věnovaný Tailscale na Umbrel.



https://planb.academy/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

## Konfigurace portfolia Bitcoin



Chcete-li přijímat platby, musíte nakonfigurovat Bitcoin wallet. Server BTCPay zobrazuje možnosti konfigurace na ovládacím panelu.



![Tableau de bord avec options de configuration de portefeuille](assets/fr/05.webp)



Chcete-li nakonfigurovat wallet Bitcoin, přejděte do části "Peněženky" > "Bitcoin".



Máte dvě možnosti: vytvořit nové portfolio přímo v BTCPay nebo importovat stávající portfolio. Pro import je k dispozici několik metod:




- Připojte hardware wallet** (doporučeno): Import veřejných klíčů prostřednictvím aplikace Trezor
- Importovat soubor wallet** (doporučeno): Nahrajte exportovaný soubor ze svého portfolia
- Zadejte rozšířený veřejný klíč**: Zadejte svůj XPub/YPub/ZPub ručně
- Naskenujte QR kód wallet** : Naskenujte QR kód z BlueWallet, Cobo Vault, Passport nebo Specter DIY
- Zadejte wallet seed** (nedoporučuje se) : Zadejte frázi pro obnovení o 12 nebo 24 slovech



![Options de création de portefeuille](assets/fr/06.webp)



V tomto tutoriálu vytvoříme nový klíč Hot wallet: soukromý klíč bude proto uložen na našem serveru Umbrel. V tomto případě důrazně doporučujeme pravidelně přesouvat prostředky na studený wallet, abyste se vyhnuli ukládání velkých částek na serveru.



![Choix entre Hot wallet et Watch-only wallet](assets/fr/07.webp)



Po konfiguraci server BTCPay potvrdí, že váš wallet je připraven přijímat platby on-chain.



![Portefeuille Bitcoin configuré avec succès](assets/fr/08.webp)



## Aktivace Lightning Network



Chcete-li přijímat okamžité platby Lightning, přejděte do nabídky Peněženky > Lightning. Poté, protože váš uzel LND je již na Umbrel umístěn, jednoduše klikněte na tlačítko "Uložit", abyste potvrdili spojení mezi vaším serverem BTCPay a vaším uzlem Lightning.



![Configuration du nœud Lightning](assets/fr/09.webp)



## Vytvářet a platit faktury



V rozhraní serveru BTCPay přejděte do nabídky Faktury > Vytvořit Invoice. Zadejte částku, přidejte volitelný popis a klikněte na tlačítko Vytvořit.



![Création d'une nouvelle facture](assets/fr/10.webp)



Poté můžete kliknout na tlačítko "Pokladna" a zobrazit fakturu. BTCPay poté vygeneruje fakturu s jednotným QR kódem (BIP21) obsahujícím adresu Bitcoin a fakturu Lightning.



![Détails de la facture générée](assets/fr/11.webp)



Zákazník může QR kód naskenovat jakýmkoli kompatibilním zařízením wallet.



![Page de paiement avec QR code](assets/fr/12.webp)



Jakmile je faktura zaplacena, stane se v aplikaci Lightning během několika sekund "vypořádanou".



![Confirmation de paiement réussi](assets/fr/13.webp)



## Správa a sledování plateb



V části "Reporting", na kartě "Invoices" najdete kompletní historii faktur s datem, částkou, stavem a způsobem platby. V případě potřeby ji můžete exportovat.



![Section reporting avec l'historique des factures](assets/fr/14.webp)



## Konfigurace obchodu



BTCPay Server umožňuje spravovat více obchodů s odlišnými parametry. Každý obchod představuje samostatný obchodní subjekt: e-shop, fyzické prodejní místo nebo fakturaci služeb.



V nastavení obchodu najdete několik důležitých sekcí:



![Paramètres du magasin](assets/fr/15.webp)





- Obecná nastavení**: Název obchodu, referenční měna (BTC, EUR, USD), doba platnosti faktury (výchozí 15 minut), počet požadovaných potvrzení blockchainu
- Sazby**: Konfigurace zdrojů směnných kurzů a převodů fiat/Bitcoin
- Vzhled pokladny**: Přizpůsobte si vzhled svých pokladních stránek (logo, barvy, personalizované zprávy)
- Nastavení e-mailu**: Konfigurace e-mailových oznámení o přijatých platbách
- Přístupové tokeny**: Správa tokenů API pro integrace elektronických obchodů (WooCommerce, Shopify atd.)
- Uživatelé**: Spravujte přístup uživatelů do obchodu s různými úrovněmi oprávnění (vlastník, host)
- Webové háčky**: Konfigurace webových háčků pro synchronizaci s účetním nebo ERP systémem v reálném čase



Server BTCPay nabízí také sekci Plugins, která rozšiřuje funkčnost o integrace pro elektronické obchodování, prodejní systémy a další nástroje.



![Gestion des plugins](assets/fr/16.webp)



## Výhody a omezení místního použití



**Výhody serveru BTCPay oproti Umbrel** :




- Naprostá suverenita: výhradní kontrola nad soukromými klíči a finančními prostředky, žádná třetí strana nemůže zmrazit nebo cenzurovat vaše platby
- Výrazné úspory: pouze Bitcoin síťové náklady (několik centů u Lightningu) oproti 2-3 % u tradičních procesorů
- Maximální důvěrnost: žádná registrace, ověřování totožnosti ani sdílení údajů se společnostmi třetích stran
- Architektura s otevřeným zdrojovým kódem zaručuje transparentnost, auditovatelnost a udržitelnost díky velké komunitě vývojářů
- Snadná instalace pomocí nástroje Umbrel bez nutnosti pokročilých technických dovedností



**Důležitá omezení** :




- Pouze místní síť**: Server BTCPay na serveru Umbrel je přístupný pouze z vaší domácí sítě. Ideální pro osobní vyúčtování, služby na volné noze nebo malé fyzické podniky, ale nevhodný pro veřejně přístupné internetové obchody.
- Plná technická odpovědnost: údržba uzlů, pravidelné zálohování, monitorování připojení
- Řízení bleskové likvidity: otevření a správa kanálů s dostatečnou příchozí kapacitou
- Podpora omezená na komunitní dokumentaci a fóra, což vyžaduje větší samostatnost než komerční oddělení služeb zákazníkům



Toto omezení místní sítě je hlavní překážkou integrace serveru BTCPay do elektronického obchodu, kde zákazníci potřebují mít přístup k platebním stránkám odkudkoli na internetu.



## Osvědčené postupy a bezpečnost



Aktivujte automatické zálohování Umbrel a uložte kopii na externí médium (USB disk, pevný disk, šifrovaný cloud). Semínka Bitcoin (fráze pro obnovení) uchovávejte na bezpečném, fyzicky odděleném místě. Zálohujte soubor channel.backup LND pro obnovu blesku.



Pravidelně monitorujte synchronizaci jádra Bitcoin, kanály Lightning a odezvu serveru BTCPay. Jednoduchý týdenní test: generate a zaplaťte účet za několik satošů. Udržujte Umbrel v aktuálním stavu (bezpečnostní záplaty, vylepšení). Před většími aktualizacemi proveďte zálohu. Pro profesionální použití zvažte externí monitoring (UptimeRobot) s upozorněními e-mailem/SMS.



## Veřejné vystavení serveru BTCPay pro online obchod



Chcete-li integrovat BTCPay Server do webového e-shopu (WooCommerce, Shopify atd.), musí mít vaši zákazníci přístup k platebním stránkám odkudkoli, nejen z vaší místní sítě.



**Řešení: Nginx Proxy Manager**



Server BTCPay můžete veřejně vystavit pomocí nástroje Nginx Proxy Manager (dostupný v obchodě Umbrel App Store). Toto řešení vyžaduje :




- Název domény (klasický nebo zdarma přes DuckDNS, No-IP, Afraid.org)
- Konfigurace přesměrování portů (porty 80 a 443) na směrovači
- Instalace Správce proxy serveru Nginx, který automaticky spravuje certifikáty SSL



Tato konfigurace vystavuje server internetu a vyžaduje zvýšenou ostražitost (silná hesla, 2FA, pravidelné aktualizace). Připravujeme speciální výukový program s podrobným popisem tohoto kompletního postupu.



## Závěr



BTCPay Server na platformě Umbrel kombinuje výkon uzlu Bitcoin s jednoduchostí platformy Umbrel a vytváří tak profesionální platební infrastrukturu dostupnou všem. Tato finanční suverenita s sebou nese odpovědnost za údržbu, ale Umbrel výrazně zjednodušuje provozní zátěž ve srovnání s výhodami: eliminace poplatků za zpracování, ochrana soukromí, odolnost vůči cenzuře a úplná kontrola nad finančními prostředky.



Využití místní sítě již zahrnuje širokou škálu aplikací: účtování služeb na volné noze, osobní platby, malé fyzické obchody nebo prosté učení a experimentování s Bitcoin a Lightning v kontrolovaném prostředí. Pro potřeby elektronického obchodování vyžadující veřejné vystavení existuje řešení Nginx Proxy Manager, které však vyžaduje další technickou konfiguraci, kterou podrobně popíšeme ve speciálním tutoriálu.



Ať už provozujete firmu, začínající projekt nebo jen experimentujete, server BTCPay na platformě Umbrel vám nabízí naprostou finanční autonomii. Cesta začíná vaším prvním obchodem, první fakturou, první platbou přijatou přímo do vaší suverénní infrastruktury.



## Zdroje



### Oficiální dokumentace




- [Oficiální stránky serveru BTCPay](https://btcpayserver.org)
- [Kompletní dokumentace serveru BTCPay](https://docs.btcpayserver.org)
- [Server GitHub BTCPay](https://github.com/btcpayserver/btcpayserver)
- [dokumentace Tailscale](https://tailscale.com/kb)


### Společenství a podpora




- [Fórum BTCPay Server](https://chat.btcpayserver.org)
- [Fórum Deštník](https://community.getumbrel.com)
- [Reddit r/BTCPayServer](https://reddit.com/r/BTCPayServer)