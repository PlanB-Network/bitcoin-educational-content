---
name: BTCPay Server - Umbrel
description: Installera och använda BTCPay Server på Umbrel för att acceptera Bitcoin och Lightning
---

![cover](assets/cover.webp)



I Bitcoin:s ekosystem är det en stor utmaning för både handlare och företag att ta emot betalningar. Traditionella lösningar, oavsett om det gäller bank (kreditkort, Stripe, PayPal) eller till och med Bitcoin (BitPay, Coinbase Commerce), innebär att mellanhänder tar ut betydande avgifter, samlar in dina känsliga affärsuppgifter och kan blockera eller censurera dina transaktioner efter eget gottfinnande. Detta beroende strider mot Bitcoin:s grundläggande principer om decentralisering, sekretess och finansiell suveränitet.



BTCPay Server framträder som open source-svaret på detta problem. Denna självhostade betalningsprocessor förvandlar din egen Bitcoin-nod till en professionell infrastruktur, utan mellanhänder, inga extra behandlingsavgifter och ingen kompromiss om integritet. BTCPay Server har utvecklats av en global grupp av bidragsgivare sedan 2017 och låter dig ta emot Bitcoin- och Lightning-betalningar direkt i dina plånböcker och behålla full kontroll över dina medel hela tiden.



Traditionellt sett kräver installation av BTCPay Server avancerade tekniska färdigheter: Linux-serverkonfiguration, behärskning av Docker, SSL-certifikathantering och nätverkssäkerhet. Umbrel revolutionerar detta tillvägagångssätt med en installation med ett klick som är direkt integrerad med din Bitcoin- och Lightning-nod. Denna förenkling gör det som tidigare var reserverat för erfarna tekniker tillgängligt för alla.



**Viktigt att förstå**: BTCPay Server på Umbrel fungerar som standard endast på ditt lokala nätverk. Du kan skapa fakturor, acceptera Lightning- och Bitcoin-betalningar och hantera din bokföring från vilken enhet som helst som är ansluten till ditt hemnätverk (dator, smartphone, surfplatta). Den här konfigurationen är idealisk för fakturering av personliga tjänster, hantering av betalningar ansikte mot ansikte eller användning av BTCPay Server från ditt lokala nätverk. Å andra sidan, för att integrera BTCPay Server i en webbutik som är allmänt tillgänglig på Internet, krävs en ytterligare konfiguration med offentlig exponering (vi kommer att täcka denna fråga i slutet av handledningen).



Denna handledning tar dig igenom den fullständiga installationen av BTCPay Server på Umbrel, konfigurerar din Bitcoin wallet och Lightning-nod, skapar och betalar fakturor och hanterar redovisningsrapportering. Du kommer att upptäcka hur du använder BTCPay Server effektivt i ditt lokala nätverk, och sedan tittar vi på lösningar för offentlig visning om du vill integrera den med en e-handelswebbplats.



## Förkunskapskrav



För att följa denna handledning måste du ha Umbrel korrekt installerat och konfigurerat. Om du inte redan har gjort det, vänligen se vår handledning om Umbrel-installation.



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

Din Bitcoin Core-nod måste vara helt synkroniserad med blockkedjan (100% i Umbrels Bitcoin-applikation). Denna initiala synkronisering tar vanligtvis mellan 3 dagar och 2 veckor, beroende på din hårdvara och internetanslutning.



För att acceptera omedelbara Lightning-betalningar måste du också installera LND (Lightning Network Daemon) på Umbrel. Se vår handledning om installation och konfiguration av LND på Umbrel om du vill aktivera den här funktionen.



https://planb.academy/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

Tillåt minst 50 GB ledigt diskutrymme för BTCPay Server, dess databaser och Lightning-data. En stabil internetanslutning via Ethernet-kabel rekommenderas starkt för att undvika avbrott.



## Installera BTCPay Server på Umbrel



Från Umbrel-gränssnittet (`umbrel.local`), gå till App Store och sök efter "BTCPay Server" i kategorin Bitcoin.



![Interface Umbrel App Store avec BTCPay Server](assets/fr/01.webp)



Klicka på Installera. Umbrel kontrollerar automatiskt att Bitcoin Core och LND är installerade och påbörjar sedan driftsättningen (2-5 minuter).



![Dépendances requises pour BTCPay Server](assets/fr/02.webp)



När du har installerat programmet öppnar du det. Du måste skapa ett administratörskonto med starka autentiseringsuppgifter.



![Création du compte administrateur BTCPay Server](assets/fr/03.webp)



När ditt konto har skapats kommer BTCPay Server omedelbart att uppmana dig att skapa din första butik. Välj ett företagsnamn och välj en referensvaluta (EUR, USD eller BTC).



![Création du premier magasin BTCPay Server](assets/fr/04.webp)



## Få åtkomst till BTCPay Server i ditt lokala nätverk



BTCPay Server är tillgänglig från alla enheter i ditt lokala nätverk (WiFi eller Ethernet). Åtkomst från din webbläsare till :



```url
http://umbrel.local
```



Eller direkt till :



```url
http://umbrel.local:3003
```



** Fjärråtkomst med Tailscale**: För att komma åt BTCPay Server från var som helst i världen, använd Tailscale. Detta säkra VPN låter dig ansluta till din Umbrel som om du vore på ditt lokala nätverk. Se vår handledning tillägnad Tailscale på Umbrel.



https://planb.academy/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

## Konfigurera din Bitcoin-portfölj



För att acceptera betalningar måste du konfigurera en Bitcoin wallet. BTCPay Server visar konfigurationsalternativ i instrumentpanelen.



![Tableau de bord avec options de configuration de portefeuille](assets/fr/05.webp)



För att konfigurera wallet Bitcoin, gå till "Plånböcker" > "Bitcoin".



Du har två alternativ: skapa en ny portfölj direkt i BTCPay eller importera en befintlig portfölj. För import finns flera metoder tillgängliga:




- Anslut hårdvaran wallet** (rekommenderas): Importera dina publika nycklar via Vault-applikationen
- Importera wallet-fil** (rekommenderas): Ladda upp en exporterad fil från din portfolio
- Ange utökad publik nyckel**: Ange din XPub/YPub/ZPub manuellt
- Skanna wallet QR-kod** : Skanna en QR-kod från BlueWallet, Cobo Vault, Passport eller Spectre DIY
- Ange wallet seed** (rekommenderas inte) : Ange din återställningsfras på 12 eller 24 ord



![Options de création de portefeuille](assets/fr/06.webp)



För denna handledning kommer vi att skapa en ny Hot wallet: den privata nyckeln kommer därför att lagras på vår Umbrel-server. I det här fallet rekommenderar vi starkt att du flyttar pengarna regelbundet till en kall wallet för att undvika att lagra stora mängder på servern.



![Choix entre Hot wallet et Watch-only wallet](assets/fr/07.webp)



När den har konfigurerats bekräftar BTCPay Server att din wallet är redo att ta emot on-chain-betalningar.



![Portefeuille Bitcoin configuré avec succès](assets/fr/08.webp)



## Aktivera Lightning Network



För att acceptera omedelbara Lightning-betalningar, gå till Wallets > Lightning. Eftersom din LND-nod redan finns på plats på Umbrel klickar du bara på knappen "Spara" för att validera anslutningen mellan din BTCPay-server och din Lightning-nod.



![Configuration du nœud Lightning](assets/fr/09.webp)



## Skapa och betala fakturor



Gå till Fakturor > Skapa Invoice i gränssnittet för BTCPay Server. Ange beloppet, lägg till en valfri beskrivning och klicka på Skapa.



![Création d'une nouvelle facture](assets/fr/10.webp)



Du kan sedan klicka på knappen "Checkout" för att visa fakturan. BTCPay genererar sedan en faktura med en enhetlig QR-kod (BIP21) som innehåller Bitcoin-adressen och Lightning-fakturan.



![Détails de la facture générée](assets/fr/11.webp)



Din kund kan skanna QR-koden med vilken kompatibel wallet som helst.



![Page de paiement avec QR code](assets/fr/12.webp)



När fakturan har betalats blir den "reglerad" på några sekunder för Lightning.



![Confirmation de paiement réussi](assets/fr/13.webp)



## Hantering och spårning av betalningar



I avsnittet "Rapportering", fliken "Fakturor", hittar du en fullständig historik över dina fakturor med datum, belopp, status och betalningsmetod. Du kan exportera den om du vill.



![Section reporting avec l'historique des factures](assets/fr/14.webp)



## Förvara konfiguration



Med BTCPay Server kan du hantera flera butiker med olika parametrar. Varje butik representerar en separat affärsenhet: e-handelsbutik, fysisk försäljningsplats eller tjänstefakturering.



I butiksinställningarna hittar du flera viktiga avsnitt:



![Paramètres du magasin](assets/fr/15.webp)





- Allmänna inställningar**: Butiksnamn, referensvaluta (BTC, EUR, USD), fakturans utgångstid (standard 15 minuter), antal blockchain-bekräftelser som krävs
- Priser**: Konfiguration av växelkurskällor och konvertering av fiat/Bitcoin
- Utseende på kassan**: Anpassa utseendet på dina kassasidor (logotyp, färger, personliga meddelanden)
- Inställningar för e-post**: Konfiguration av e-postmeddelanden för mottagna betalningar
- Åtkomsttokens**: Hantering av API-tokens för e-handelsintegrationer (WooCommerce, Shopify, etc.)
- Användare**: Hantera användarnas åtkomst till butiken med olika behörighetsnivåer (ägare, gäst)
- Webhooks**: Webhook-konfiguration för realtidssynkronisering med ditt bokförings- eller ERP-system



BTCPay Server erbjuder också en Plugins-sektion för att utöka funktionaliteten med e-handelsintegrationer, kassasystem och ytterligare verktyg.



![Gestion des plugins](assets/fr/16.webp)



## Fördelar och begränsningar med lokal användning



**Fördelarna med BTCPay Server jämfört med Umbrel** :




- Total suveränitet: exklusiv kontroll över privata nycklar och medel, ingen tredje part kan frysa eller censurera dina betalningar
- Betydande besparingar: endast Bitcoin nätverkskostnader (några cent för Lightning) jämfört med 2-3% för traditionella processorer
- Maximal sekretess: ingen registrering, identitetsverifiering eller datadelning med tredjepartsföretag
- Arkitektur med öppen källkod garanterar transparens, granskningsbarhet och hållbarhet genom en stor grupp utvecklare
- Enkel installation via Umbrel, utan behov av avancerad teknisk kompetens



**Viktiga begränsningar** :




- Endast lokalt nätverk**: BTCPay Server på Umbrel är endast tillgänglig från ditt hemnätverk. Perfekt för fakturering ansikte mot ansikte, frilanstjänster eller små fysiska företag, men olämpligt för offentligt tillgängliga onlinebutiker.
- Fullt tekniskt ansvar: underhåll av noder, regelbundna säkerhetskopior, övervakning av anslutningar
- Hantering av blixtlikviditet: öppna och hantera kanaler med tillräcklig inkommande kapacitet
- Support begränsad till community-dokumentation och forum, vilket kräver mer självständighet än en kommersiell kundtjänstavdelning



Denna lokala nätverksbegränsning är det största hindret för att integrera BTCPay Server i en e-handelsbutik, där kunderna måste kunna komma åt betalningssidor från var som helst på Internet.



## Bästa praxis och säkerhet



Aktivera automatisk säkerhetskopiering av Umbrel och lagra en kopia på externt media (USB-minne, hårddisk, krypterat moln). Förvara dina Bitcoin-frön (återställningsfraser) på en säker, fysiskt separat plats. Säkerhetskopiera LND:s channel.backup-fil för Lightning-återställning.



Övervaka regelbundet Bitcoin Core-synkronisering, Lightning-kanaler och BTCPay Server-svar. Ett enkelt veckotest: generate och betala en räkning på några satoshis. Håll Umbrel uppdaterad (säkerhetsfixar, förbättringar). Gör en säkerhetskopia före större uppdateringar. För professionell användning, överväg extern övervakning (UptimeRobot) med e-post/SMS-varningar.



## Exponera BTCPay Server offentligt för en onlinebutik



För att integrera BTCPay Server i en webbaserad e-handelsbutik (WooCommerce, Shopify etc.) måste dina kunder kunna komma åt betalningssidor från var som helst, inte bara ditt lokala nätverk.



**Lösning: Nginx Proxy Manager**



Du kan exponera BTCPay Server offentligt med hjälp av Nginx Proxy Manager (finns i Umbrel App Store). Denna lösning kräver :




- Ett domännamn (klassiskt eller gratis via DuckDNS, No-IP, Afraid.org)
- Konfigurera portvidarebefordran (portarna 80 och 443) på din router
- Installation av Nginx Proxy Manager, som automatiskt hanterar SSL-certifikat



Den här konfigurationen exponerar din server mot Internet och kräver extra vaksamhet (starka lösenord, 2FA, regelbundna uppdateringar). Vi kommer att förbereda en dedikerad handledning som beskriver hela proceduren.



## Slutsats



BTCPay Server on Umbrel kombinerar kraften i Bitcoin-noden med enkelheten i Umbrel för att skapa en professionell betalningsinfrastruktur med egen värd som är tillgänglig för alla. Denna ekonomiska suveränitet kommer med ett underhållsansvar, men Umbrel förenklar kraftigt den operativa bördan jämfört med fördelarna: eliminering av behandlingsavgifter, skydd av din integritet, motstånd mot censur och total kontroll över dina medel.



Användningen av lokala nätverk täcker redan ett brett spektrum av applikationer: fakturering för frilanstjänster, personliga betalningar, små fysiska butiker eller helt enkelt att lära sig och experimentera med Bitcoin och Lightning i en kontrollerad miljö. För e-handelsbehov som kräver offentlig exponering finns lösningen Nginx Proxy Manager, men den kräver ytterligare teknisk konfiguration, som vi beskriver i en särskild handledning.



Oavsett om du driver ett företag, ett nystartat projekt eller bara experimenterar, erbjuder BTCPay Server on Umbrel fullständig ekonomisk autonomi. Vägen börjar med din första butik, din första faktura, din första betalning som tas emot direkt i din suveräna infrastruktur.



## Resurser



### Officiell dokumentation




- [Officiell webbplats för BTCPay Server](https://btcpayserver.org)
- [Komplett dokumentation för BTCPay Server](https://docs.btcpayserver.org)
- [GitHub BTCPay Server](https://github.com/btcpayserver/btcpayserver)
- [Tailscale-dokumentation](https://tailscale.com/kb)


### Gemenskap och stöd




- [Forum BTCPay Server](https://chat.btcpayserver.org)
- [Forum Umbrel](https://community.getumbrel.com)
- [Reddit r/BTCPayServer](https://reddit.com/r/BTCPayServer)