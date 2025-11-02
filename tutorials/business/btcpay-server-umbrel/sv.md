---
name: BTCPAY SERVER - Paraply
description: Installera och använda BTCPAY SERVER på Umbrel för att acceptera Bitcoin och Lightning
---

![cover](assets/cover.webp)



I Bitcoin-ekosystemet är det en stor utmaning för både handlare och företag att ta emot betalningar. Traditionella lösningar, oavsett om det är banker (kreditkort, Stripe, PayPal) eller till och med Bitcoin (BitPay, Coinbase Commerce), innebär att mellanhänder tar ut betydande avgifter, samlar in dina känsliga affärsuppgifter och kan BLOCK eller censurera dina transaktioner efter eget gottfinnande. Detta beroende strider mot Bitcoin:s grundläggande principer om decentralisering, sekretess och finansiell suveränitet.



BTCPAY SERVER håller på att växa fram som ett open source-svar på detta problem. Denna självhostade betalningsprocessor förvandlar din egen Bitcoin-nod till en professionell infrastruktur, utan mellanhänder, utan ytterligare behandlingsavgifter och utan att kompromissa med integriteten. BTCPAY SERVER har utvecklats av en global grupp av bidragsgivare sedan 2017 och gör att du kan ta emot Bitcoin- och Lightning-betalningar direkt i dina plånböcker och alltid behålla full kontroll över dina medel.



Traditionellt sett kräver installation av BTCPAY SERVER avancerade tekniska färdigheter: Linux-serverkonfiguration, Docker-mästerskap, SSL-certifikathantering och nätverkssäkerhet. Umbrel revolutionerar detta tillvägagångssätt med en installation med ett klick som är direkt integrerad med din Bitcoin och LIGHTNING NODE. Denna förenkling gör det som tidigare var reserverat för erfarna tekniker tillgängligt för alla.



**Viktigt att förstå**: BTCPAY SERVER on Umbrel fungerar som standard endast i ditt lokala nätverk. Du kan skapa fakturor, acceptera Lightning- och Bitcoin-betalningar och hantera din bokföring från vilken enhet som helst som är ansluten till ditt hemnätverk (dator, smartphone, surfplatta). Den här konfigurationen är idealisk för att fakturera personliga tjänster, hantera personliga betalningar eller använda BTCPAY SERVER från ditt lokala nätverk. Å andra sidan, för att integrera BTCPAY SERVER i en onlinebutik som är allmänt tillgänglig på Internet, krävs en ytterligare konfiguration med offentlig exponering (vi kommer att täcka denna fråga i slutet av handledningen).



Denna handledning tar dig igenom den fullständiga installationen av BTCPAY SERVER på Umbrel, konfigurerar din Bitcoin Wallet och LIGHTNING NODE, skapar och betalar fakturor och hanterar redovisningsrapportering. Du får reda på hur du använder BTCPAY SERVER effektivt i ditt lokala nätverk, och sedan pratar vi om lösningar för offentlig visning om du vill integrera den med en e-handelswebbplats.



## Förkunskapskrav



För att följa denna handledning måste du ha Umbrel korrekt installerat och konfigurerat. Om du inte redan har gjort det, vänligen se vår handledning om Umbrel-installation.



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

Din Bitcoin core-nod måste vara helt synkroniserad med Blockchain (100% i Umbrels Bitcoin-applikation). Denna initiala synkronisering tar vanligtvis mellan 3 dagar och 2 veckor, beroende på din maskinvara och internetanslutning.



För att acceptera omedelbara Lightning-betalningar måste du också installera LND (Lightning Network Daemon) på Umbrel. Se vår handledning om installation och konfiguration av LND på Umbrel om du vill aktivera den här funktionen.



https://planb.academy/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

Tillåt minst 50 GB ledigt diskutrymme för BTCPAY SERVER, dess databaser och Lightning-data. En stabil internetanslutning via Ethernet-kabel rekommenderas starkt för att undvika avbrott.



## Installera BTCPAY SERVER på paraplyet



Från Umbrel Interface (`umbrel.local`), gå till App Store och sök efter "BTCPAY SERVER" i kategorin Bitcoin.



![Interface Umbrel App Store avec BTCPay Server](assets/fr/01.webp)



Klicka på Installera. Umbrel kontrollerar automatiskt att Bitcoin core och LND är installerade och påbörjar sedan driftsättningen (2-5 minuter).



![Dépendances requises pour BTCPay Server](assets/fr/02.webp)



När du har installerat programmet öppnar du det. Du måste skapa ett administratörskonto med starka autentiseringsuppgifter.



![Création du compte administrateur BTCPay Server](assets/fr/03.webp)



När ditt konto har skapats kommer BTCPAY SERVER omedelbart att uppmana dig att skapa din första butik. Välj ett professionellt namn och välj en referensvaluta (EUR, USD eller BTC).



![Création du premier magasin BTCPay Server](assets/fr/04.webp)



## Få tillgång till BTCPAY SERVER i ditt lokala nätverk



BTCPAY SERVER kan nås från alla enheter i ditt lokala nätverk (WiFi eller Ethernet). Åtkomst från din webbläsare till :



```url
http://umbrel.local
```



Eller direkt till :



```url
http://umbrel.local:3003
```



**Fjärråtkomst med Tailscale**: För att komma åt BTCPAY SERVER från var som helst i världen, använd Tailscale. Detta säkra VPN låter dig ansluta till din Umbrel som om du vore på ditt lokala nätverk. Se vår handledning tillägnad Tailscale på Umbrel.



https://planb.academy/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

## Konfigurera din Bitcoin-portfölj



För att acceptera betalningar måste du konfigurera en Bitcoin Wallet. BTCPAY SERVER visar konfigurationsalternativen i instrumentpanelen.



![Tableau de bord avec options de configuration de portefeuille](assets/fr/05.webp)



För att konfigurera Wallet Bitcoin, gå till "Plånböcker" > "Bitcoin".



Du har två alternativ: skapa en ny portfölj direkt i BTCPay eller importera en befintlig portfölj. För import finns flera metoder tillgängliga:




- Anslut Hardware Wallet** (rekommenderas): Importera dina publika nycklar via Vault-applikationen
- Importera Wallet-fil** (rekommenderas): Ladda upp en exporterad fil från din portfolio
- Ange utökad publik nyckel**: Ange din XPub/YPub/ZPub manuellt
- Skanna Wallet QR-kod** : Skanna en QR-kod från BlueWallet, Cobo Vault, Passport eller Spectre DIY
- Ange Wallet seed** (rekommenderas inte) : Ange din återställningsfras på 12 eller 24 ord



![Options de création de portefeuille](assets/fr/06.webp)



För denna handledning kommer vi att skapa en ny Hot Wallet: den privata nyckeln kommer därför att lagras på vår Umbrel-server. I det här fallet rekommenderar vi starkt att du flyttar pengarna regelbundet till en Cold Wallet för att undvika att lagra stora belopp på servern.



![Choix entre Hot wallet et Watch-only wallet](assets/fr/07.webp)



När den har konfigurerats bekräftar BTCPAY SERVER att din Wallet är redo att ta emot On-Chain-betalningar.



![Portefeuille Bitcoin configuré avec succès](assets/fr/08.webp)



## Aktivera Lightning Network



För att acceptera omedelbara Lightning-betalningar, gå till Wallets > Lightning. Eftersom din LND-nod redan finns på plats på Umbrel klickar du bara på knappen "Spara" för att validera anslutningen mellan din BTCPAY SERVER och din LIGHTNING NODE.



![Configuration du nœud Lightning](assets/fr/09.webp)



## Skapa och betala fakturor



I Interface BTCPAY SERVER navigerar du till Fakturor > Skapa Invoice. Ange beloppet, lägg till en valfri beskrivning och klicka på Skapa.



![Création d'une nouvelle facture](assets/fr/10.webp)



Du kan sedan klicka på knappen "Checkout" för att visa Invoice. BTCPay genererar sedan en Invoice med en enhetlig QR-kod (BIP21) som innehåller Bitcoin Address och Lightning Invoice.



![Détails de la facture générée](assets/fr/11.webp)



Din kund kan skanna QR-koden med vilken kompatibel Wallet som helst.



![Page de paiement avec QR code](assets/fr/12.webp)



När den har betalats blir Invoice "avvecklad" på några sekunder för blixtnedslag.



![Confirmation de paiement réussi](assets/fr/13.webp)



## Hantering och spårning av betalningar



I avsnittet "Rapportering", fliken "Fakturor", hittar du en fullständig historik över dina fakturor, med datum, belopp, status och betalningsmetod. Du kan exportera den om du vill.



![Section reporting avec l'historique des factures](assets/fr/14.webp)



## Förvara konfiguration



Med BTCPAY SERVER kan du hantera flera butiker med olika parametrar. Varje butik representerar en separat affärsenhet: e-handelsbutik, fysisk försäljningsplats eller fakturering av tjänster.



I butiksinställningarna hittar du flera viktiga avsnitt:



![Paramètres du magasin](assets/fr/15.webp)





- Allmänna inställningar**: Affärsnamn, referensvaluta (BTC, EUR, USD), Invoice utgångstid (standard 15 minuter), antal Blockchain bekräftelser som krävs
- Priser**: Konfiguration av Exchange-räntekällor och fiat/Bitcoin-omvandlingar
- Utseende på kassan**: Anpassa utseendet på dina kassasidor (logotyp, färger, personliga meddelanden)
- Inställningar för e-post**: Konfiguration av e-postmeddelanden för mottagna betalningar
- Åtkomsttokens**: API token hantering för e-handelsintegrationer (WooCommerce, Shopify etc.)
- Användare**: Hantera användarnas åtkomst till butiken med olika behörighetsnivåer (ägare, gäst)
- Webhooks**: Webhook-konfiguration för realtidssynkronisering med ditt bokförings- eller ERP-system



BTCPAY SERVER erbjuder också en Plugins-sektion för att utöka funktionaliteten med e-handelsintegrationer, kassasystem och ytterligare verktyg.



![Gestion des plugins](assets/fr/16.webp)



## Fördelar och begränsningar med lokal användning



**Fördelarna med BTCPAY SERVER på Umbrel** :




- Total suveränitet: exklusiv kontroll över privata nycklar och medel, ingen tredje part kan frysa eller censurera dina betalningar
- Betydande besparingar: endast Bitcoin i nätverkskostnader (några cent på Lightning) jämfört med 2-3% på traditionella processorer
- Maximal sekretess: ingen registrering, identitetsverifiering eller datadelning med tredjepartsföretag
- Arkitektur med öppen källkod garanterar transparens, granskningsbarhet och hållbarhet genom en stor grupp utvecklare
- Enkel installation via Umbrel, utan behov av avancerad teknisk kompetens



**Viktiga begränsningar** :




- Endast lokalt nätverk**: BTCPAY SERVER on Umbrel är endast tillgänglig från ditt hemnätverk. Perfekt för fakturering ansikte mot ansikte, frilanstjänster eller små fysiska företag, men olämpligt för onlinebutiker som är allmänt tillgängliga på Internet.
- Fullt tekniskt ansvar: underhåll av noder, regelbundna säkerhetskopior, övervakning av anslutningar
- Hantering av blixtlikviditet: öppna och hantera kanaler med tillräcklig inkommande kapacitet
- Support begränsad till community-dokumentation och forum, vilket kräver mer självständighet än en kommersiell kundtjänstavdelning



Denna LAN-begränsning är det största hindret för att integrera BTCPAY SERVER i en e-handelsbutik, där kunderna måste kunna komma åt betalningssidorna var som helst på Internet.



## Bästa praxis och säkerhet



Aktivera automatisk Umbrel-säkerhetskopiering och lagra en kopia på externt media (USB-minne, Hard-disk, krypterat moln). Förvara dina Bitcoin-frön (återställningsfraser) på en säker, fysiskt separat plats. Spara filen LND channel.backup för återställning av Lightning.



Övervaka regelbundet Bitcoin core-synkronisering, Lightning-kanaler och BTCPAY SERVER-svar. Ett enkelt veckotest: generate och betala en räkning på några satoshis. Håll Umbrel uppdaterat (säkerhetsfixar, förbättringar). Gör en säkerhetskopia före större uppdateringar. För professionell användning, överväg extern övervakning (UptimeRobot) med e-post/SMS-varningar.



## Visa BTCPAY SERVER offentligt för en onlinebutik



För att integrera BTCPAY SERVER i en webbaserad e-handelsbutik (WooCommerce, Shopify etc.) måste dina kunder kunna komma åt betalningssidorna var som helst, inte bara från ditt lokala nätverk.



**Lösning: Nginx Proxy Manager**



Du kan exponera BTCPAY SERVER offentligt med hjälp av Nginx Proxy Manager (finns i Umbrel App Store). Denna lösning kräver :




- Ett domännamn (klassiskt eller gratis via DuckDNS, No-IP, Afraid.org)
- Konfigurera portvidarebefordran (portarna 80 och 443) på din router
- Installation av Nginx Proxy Manager, som automatiskt hanterar SSL-certifikat



Den här konfigurationen exponerar din server mot Internet och kräver extra vaksamhet (starka lösenord, 2FA, regelbundna uppdateringar). Vi kommer att förbereda en dedikerad handledning som beskriver hela proceduren.



## Slutsats



BTCPAY SERVER on Umbrel kombinerar kraften i Bitcoin-noden med enkelheten i Umbrel för att skapa en professionell betalningsinfrastruktur med egen värd som är tillgänglig för alla. Denna ekonomiska suveränitet kommer med ett underhållsansvar, men Umbrel förenklar kraftigt den operativa bördan jämfört med fördelarna: eliminering av behandlingsavgifter, skydd av din integritet, motstånd mot censur och total kontroll över dina medel.



Användningen av lokala nätverk täcker redan ett brett spektrum av applikationer: fakturering för frilanstjänster, betalningar ansikte mot ansikte, små fysiska butiker eller helt enkelt att lära sig och experimentera med Bitcoin och Lightning i en kontrollerad miljö. För e-handelsbehov som kräver offentlig exponering finns lösningen Nginx Proxy Manager, men den kräver ytterligare teknisk konfiguration, som vi beskriver i en särskild handledning.



Oavsett om du driver ett företag, ett nystartat projekt eller bara experimenterar, erbjuder BTCPAY SERVER på Umbrel fullständig finansiell autonomi. Vägen börjar med en första butik, en första Invoice, en första betalning som tas emot direkt till din suveräna infrastruktur.



## Resurser



### Officiell dokumentation




- [BTCPAY SERVER officiella webbplats](https://btcpayserver.org)
- [Komplett BTCPAY SERVER-dokumentation] (https://docs.btcpayserver.org)
- [GitHub BTCPAY SERVER](https://github.com/btcpayserver/btcpayserver)
- [Tailscale-dokumentation] (https://tailscale.com/kb)


### Gemenskap och stöd




- [Forum BTCPAY SERVER](https://chat.btcpayserver.org)
- [Forum Umbrel](https://community.getumbrel.com)
- [Reddit r/BTCPayServer] (https://reddit.com/r/BTCPayServer)