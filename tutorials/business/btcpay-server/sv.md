---
name: BTCPay-server
description: Acceptera BTC-betalningar utan mellanhänder
---

![cover](assets/cover.webp)



![video](https://youtu.be/KqsM-n-e4aY)



BTCPay Server är ett gratis mjukvarupaket med öppen källkod skapat av Nicolas Dorier som gör det möjligt att acceptera bitcoinbetalningar utan mellanhänder. Det är utformat för att erbjuda autonomi och ekonomisk suveränitet, installeras på sin egen server och tillhandahåller fullständig transaktionshantering, från fakturering till validering av on-chain- eller Lightning Network-betalningar och redovisning. Den integreras enkelt med e-handelssajter (WooComerce, Shopify, etc.) eller kan användas som en betalterminal för fysiska butiker (*POS*).



BTCPay Server är utan tvekan den mest avancerade lösningen för handlare som vill ta emot bitcoin. Det är den mest omfattande och robusta programvaran när det gäller säkerhet, suveränitet och sekretess. Å andra sidan är det också den mest komplexa att installera och underhålla. Det finns också enklare alternativ: vissa är helt och hållet custodial, som OpenNode, medan andra erbjuder en intressant kompromiss mellan användarvänlighet och suveränitet, som schweiziska Bitcoin Pay :



https://planb.academy/tutorials/business/point-of-sale/swiss-bitcoin-pay-2-a78b057e-ed11-47ac-860c-71019fcb451a

Syftet med denna handledning är att vägleda dig steg för steg genom installation, konfiguration och användning av BTCPay Server, så att du kan distribuera en säker, oberoende betalningsinfrastruktur i linje med Bitcoin:s etos.



## BTCPay Server-funktioner



Centraliserade Bitcoin-försäljningslösningar, som till exempel * OpenNode *, erbjuder användarvänlighet, men förlitar sig på ett tredjepartsföretag eftersom de inte kan vara självhostade och i de flesta fall är proprietära. Även om de gör det lättare att sätta upp betalningar innebär de provisionskostnader och utsätter sina användare för fler risker än en lösning som BTCPay Server, både när det gäller förvaring av medel och sekretess.



BTCPay Server riktar sig till online- eller fysiska handlare, föreningar och ideella organisationer som vill ta emot donationer i bitcoins. Det är också en idealisk lösning för projektägare och utvecklare som söker direkt stöd från sitt samhälle.



De speciella funktionerna i BTCPay Server inkluderar :




- dess **fullständiga självständighet**,
- avsaknad av ett **KYC**-förfarande,
- full kontroll över fonderna**,
- **eliminering av plattformsavgifter**.



Genom att bli din egen betalningsprocessor eliminerar du allt beroende av en centraliserad tredje part mellan dig och dina kunder. Du kan acceptera betalningar direkt i bitcoins och generate-betalningsfakturor. Detta säkerställer att varken du eller ditt företag kan förbjudas av någon annan. Du spelar rollen som både bank och betalningsbehandlare, utan att behöva betala provisioner till en mellanhand för varje transaktion.



Transaktionsavgifter för **on-chain** kvarstår, men kan reduceras genom att använda **Liquid** eller **Lightning**-nätverket.



Dessutom :




- Helt anpassningsbart gränssnitt och fakturor;
- Inbyggt **Tor**-stöd för förbättrad sekretess;
- Stöd för **crowdfunding**, **POS** och **betalningsknappar**;
- Kompatibel med många valutor ;
- Bitcoin Direktbetalningar och peer-to-peer-betalningar ;
- Fullständig kontroll över dina privata nycklar;
- Förbättrad integritet ;
- Förbättrad säkerhet ;
- Självhanterad programvara ;
- Stöd för **SegWit** och **Lightning network** ;
- Intern, nodbaserad portfölj, med integrering av hårdvaruportföljer.



## Installera och konfigurera BTCPay Server



### Välja ditt hostingläge



BTCPay Server kan installeras på ett antal olika sätt. Beroende på dina behov och resurser finns det tre huvudalternativ:




- BTCPay Server hostas av en tredje part**: du använder en plattform som hostar tjänsten åt dig. Det är enkelt, men vanligtvis inte gratis.
- BTCPay Server självhostad på en molnserver** (t.ex. via [btcpayprovider](https://btcpayprovider.com/), [Bitcoin People](http://bitcoinpeople.it/) eller någon annan leverantör). Detta är den rekommenderade lösningen för de flesta nya handlare.
- BTCPay Server installerad på din egen hårdvara (lokalt)** : på en dator, mini-PC eller Umbrel. Denna metod är mer teknisk, men erbjuder total självständighet.



https://planb.academy/tutorials/business/point-of-sale/btcpay-server-umbrel-68e1c535-4322-4507-a69c-9dfcbc36dfd1

För en nystartad handlare är **distribution på en molnserver** den bästa kompromissen mellan självständighet, enkelhet och säkerhet, utan att behöva hantera hela den tekniska infrastrukturen.



BTCPay Server kan distribueras snabbt från ett antal värdleverantörer. Bland dem utmärker sig **Voltage** som en referenslösning för användare som kräver en **tillförlitlig**, **professionell** och **suverän** infrastruktur.



### Skapa en BTCPay Server-instans på Voltage



**Voltage** är en nyckelfärdig Bitcoin- och Lightning-värdplattform som låter dig omedelbart distribuera din egen BTCPay-server utan komplex konfiguration eller serverunderhåll.



Besök [den officiella Voltage-webbplatsen] (https://voltage.cloud).



![capture](assets/fr/03.webp)



Skapa ett **användarkonto** med en giltig e-postadress och ett starkt lösenord.



![capture](assets/fr/04.webp)



Voltage erbjuder en **gratis 7-dagars provperiod**. Observera att efter vår 7-dagars kostnadsfria provperiod kommer du att bli inbjuden att registrera dig för en fast prenumeration på **$25 per månad** för att fortsätta **hålla dina noder aktiva**.



När du har skapat ditt Voltage-konto och loggat in för första gången kommer du att omdirigeras till startsidan, som har två huvudavsnitt:




- Ett **Infrastruktur**-avsnitt för hantering av Lightning-noder, Bitcoin Core, BTCPay Server och andra Bitcoin-tjänster i molnet;
- och ett **Payments**-avsnitt som ger dig tillgång till Voltage's API Lightning för att integrera Bitcoin-betalningar i anpassade applikationer.



För att distribuera din **BTCPay Server**-instans klickar du på **Access-infrastruktur**. Det är här du kan skapa, hantera och övervaka alla dina tjänster, inklusive din Bitcoin-nod och BTCPay Server.



#### Skapa en grupp



Innan du kan distribuera en tjänst kommer plattformen att uppmana dig att **skapa en grupp**. En **grupp** (arbetsyta) är en arbetsyta som grupperar alla dina Bitcoin- och Lightning-tjänster (t.ex. en nod, en BTCPay-server, en utforskare etc.) Det är lite som en mapp som innehåller dina olika projekt.



![capture](assets/fr/05.webp)



I den här handledningen kommer den grupp vi har skapat att kallas **Genesis**. Du kan lägga till en profilbild om du vill. När detta är gjort klickar du på knappen **Create**. Du kan bjuda in andra användare att gå med i gruppen och till och med ändra gruppnamnet om du vill.



På gruppens startsida visas flera alternativ:




- Lightning Nodes** : för att driftsätta en komplett Lightning-nod (LND) ;
- Bitcoin Core Nodes** : för att starta en komplett Bitcoin-nod ;
- BTCPay Server** : för att vara värd för en BTCPay-instans som är klar att använda;
- Nostr Accounts**: för att hantera Nostr-identiteter.



Aktivera **dubbel autentisering (2FA)** för att skydda ditt konto och dina tjänster (knappen visas i rött om den är avaktiverad).



![capture](assets/fr/06.webp)



Klicka på **BTCPay Server** bland alternativen och sedan på **Launch a BTCPay Store**.



![capture](assets/fr/07.webp)



Voltage kommer sedan att be dig att **skapa och konfigurera din BTCPay Server-instans** genom att välja ett **tjänstnamn** (1) och aktivera Lightning-betalningar (2).



Du behöver en Lightning-nod om du bestämmer dig för att acceptera Lightning-betalningar.



Om du inte redan har en Bitcoin- eller Lightning-nod kommer Voltage att föreslå att du skapar en automatiskt.



Klicka på **Create a Lightning node** (3) .



![capture](assets/fr/08.webp)



När du kommer till gränssnittet för skapande av noder får du välja mellan layouterna **standard** och **professionell**.



Du kan skapa en riktig nod (**Mainnet**) eller en testnod (**Testnet**). Klicka sedan på knappen **Fortsätt**.



![capture](assets/fr/09.webp)



För denna handledning använder vi standardplanen. Ange **nodnamnet**, ett **lösenord** och tryck på knappen **Create**.



![capture](assets/fr/10.webp)



Efter några ögonblick kommer din nod att vara i drift och du kan öppna en fri kanal med en mottagningskapacitet på 500 000 sats.



![capture](assets/fr/11.webp)



Lite längre ner till höger hittar du all information du behöver om din knut!



![capture](assets/fr/12.webp)



Nu när vi har fått igång vår Lightning-nod, låt oss gå tillbaka till att installera vår BTCPay-server. Du kan nu klicka på knappen **Create BTCPay**.



![capture](assets/fr/13.webp)



En sida öppnas med dina standardinloggningsuppgifter och ett meddelande som uppmanar dig att ändra ditt ursprungliga lösenord. När du har gjort detta klickar du på knappen **Login Now** för att komma åt ditt gränssnitt.



![capture](assets/fr/14.webp)



Nu är det klart! Din BTCPay-server är redo att användas. Du kommer att omdirigeras direkt till inloggningssidan för din BTCPay-server.



![capture](assets/fr/15.webp)



När du har loggat in kan du konfigurera din första **butik**:





- Ge det ett **namn**.





- Välj **standardvaluta** (EUR, USD, CFA, etc.).





- Välj en **valutakursleverantör** (t.ex. CoinGecko).



![capture](assets/fr/16.webp)



Du kommer då att omdirigeras till din butiks instrumentpanel. På instrumentpanelen kommer du att märka att knappen **Create your shop** är grönmarkerad, eftersom det här steget redan har slutförts.



![capture](assets/fr/17.webp)



Lite längre ner har vi knapparna **Konfigurera wallet** och **Konfigurera Lightning-nod**. I vårt fall har vi redan anslutit till en Lightning-nod som körs på spänning. Så vi behöver inte göra det här.



Låt oss gå vidare till att konfigurera en portfölj. Klicka på knappen **Konfigurera en portfölj**.



Eftersom vi precis har kommit igång med BTCPay Server, låt oss ansluta en befintlig wallet. Så tryck på **Anslut en befintlig portfölj**.



![capture](assets/fr/18.webp)



Du måste sedan välja din **importmetod**. Bland de tillgängliga alternativen väljer du **Enter extended public key**.



![capture](assets/fr/19.webp)



Genom att länka en befintlig wallet kan du ta emot dina betalningar **direkt på denna externa wallet**, utan att BTCPay-servern har tillgång till din privata nyckel. Så även om servern skulle hackas eller den offentliga nyckeln (`xpub`) äventyras, kan en angripare se din transaktionshistorik, men det skulle vara **omöjligt att komma åt dina pengar**.



När du klickar på knappen **Enter extended public key** kommer du att **omdirigeras** till den sida där du måste ange den här nyckeln.



Låt oss nu hämta den **utökade offentliga nyckeln**.



### Ansluta en Bitcoin wallet



För att ta emot dina betalningar måste du ansluta en Bitcoin wallet till din butik. För att göra detta har du flera alternativ:





- Hårdvaruportfölj** (Ledger, Trezor, Coldcard ...) ;





- Programvaruportfölj** (Blockstream App, Ashigaru, Electrum, Sparrow...)





- BTCPay Server** intern wallet (rekommenderas inte, eftersom det är mindre säkert och exponerar dina medel mer i händelse av serverhackning).



I den här handledningen använder vi en **programvaruportfölj**, som är mer lättillgänglig för den första konfigurationen. Du kan välja mellan ett antal kompatibla applikationer: **Electrum**, **Phoenix**, **Zeus**, **Muun**, etc.



För demonstrationen kommer vi att använda **Electrum**. Öppna **Electrum**, klicka på **Portfolio** och sedan på **Information**:



![capture](assets/fr/20.webp)



Kopiera sedan den offentliga nyckeln för **master (xpub)**.



![capture](assets/fr/21.webp)



När du har kopierat den offentliga huvudnyckeln klistrar du in den i fältet på BTCPay Server-sidan.



![capture](assets/fr/22.webp)



Efter verifiering kommer du att omdirigeras till din butiks instrumentpanel.



![capture](assets/fr/23.webp)



### Skapa ett försäljningsställe (PoS)



När du har konfigurerat din butik och portfölj kan du nu konfigurera en **Point of Sale (PoS)** för att börja ta emot Bitcoin-betalningar direkt från dina kunder.



Denna integrerade funktion i **BTCPay Server** är idealisk för **handlare, hantverkare, restauratörer eller tjänsteleverantörer** som vill acceptera Bitcoin **utan en webbplats** eller speciella tekniska färdigheter.



### Vad är försäljningspunkten?



**PoS** är ett **förenklat POS-gränssnitt** som fungerar som en **Bitcoin betalterminal**.


Det gör att du kan :




- Skapa en **meny med produkter eller tjänster** med fasta priser.
- Generera en **instantfaktura med QR-kod** att skanna.
- Dela en **Payment URL** som är tillgänglig via smartphone, surfplatta eller dator.



Med andra ord förvandlar PoS din BTCPay-server till ett **direkt försäljningsgränssnitt**, där varje betalning tas emot **i din egen Bitcoin wallet**, utan mellanhänder.



### Konfigurera PoS



I BTCPays kontrollpanel klickar du på **PLUGINS** och sedan på **Point of sale**.



Klicka sedan på **Skapa en ny PoS-applikation**. Denna åtgärd lägger till en ** ny applikation** i din BTCPay-butik, som om du installerade en mini intern försäljningswebbplats.



En sida öppnas för att skapa din applikation. Definiera ett **applikationsnamn**: detta är ett internt namn som endast är synligt från din instrumentpanel (t.ex. _Shoe Shop_).



Klicka på **Create** för att validera.



![capture](assets/fr/24.webp)



När den har skapats kommer du att omdirigeras till **Den detaljerade konfigurationssidan** för försäljningsstället.



### Anpassa ditt försäljningsgränssnitt



På den här sidan kan du definiera de viktigaste delarna av din PoS:





- Applikationsnamn** (internt förvaltningsnamn, kan ändras när som helst).





- Display title** (det som dina kunder kommer att se högst upp på sidan).





- Point of sale style** (**Description**-läget är lämpligt för tjänster som hårklippning eller måltider, medan **Product catalog**-läget är idealiskt för butiker som erbjuder flera artiklar).





- Visa valuta** (välj **XOF**, **EUR** eller **USD** enligt dina vanliga priser).





- Produktlista** (lägg till dina produkter, beskrivningar och priser här).



![capture](assets/fr/25.webp)



![capture](assets/fr/26.webp)



### Spara och testa din PoS



När du är klar med konfigurationen klickar du på **Save** för att spara dina inställningar och sedan på **View** för att förhandsgranska din PoS.



Du kommer att se en sida som presenterar dina produkter, där varje knapp motsvarar en vara eller tjänst.



Så snart en kund väljer en produkt :



1. BTCPay genererar automatiskt en Bitcoin- eller Lightning**-faktura.



2. En **QR-kod** visas på skärmen.



3. Kunderna kan **skanna och betala direkt** med sina Bitcoin wallet.




![capture](assets/fr/27.webp)



### Slutligt resultat



Du har nu en komplett **Bitcoin Point of Sale** som du kan :





- Öppna från en smartphone eller surfplatta i din butik ;





- Visas på en skärm för kunden att skanna;





- Eller dela via en publik **URL**, som en förenklad ordersida.



Vid varje betalning krediteras beloppet automatiskt till **din egen BTCPay wallet**, utan mellanhänder eller tredjepartsavgifter.


Detta förvandlar din PoS till en **stand-alone Bitcoin betalterminal**.




## Vardaglig användning



Innan du tar ut några riktiga betalningar rekommenderar vi att du utför **ett test** för att kontrollera att allt fungerar som det ska.



### Testa en betalning





- Skapa en faktura** från ditt PoS-gränssnitt (t.ex. en produkt på 1 satoshi eller ett litet belopp).





- Skanna QR-koden på skärmen** med en Bitcoin eller Lightning wallet (t.ex. **Phoenix**, **Muun** eller **Wallet av Satoshi**).




![capture](assets/fr/28.webp)





- Validera betalningen** i din wallet: transaktionen skickas direkt.





- Återgå till BTCPay Server**: fakturan kommer att visas som **Paid** i listan.



![capture](assets/fr/29.webp)



Vi gratulerar dig! Ditt försäljningsställe är nu **funktionellt**. Du kan börja ta emot Bitcoin-betalningar från dina kunder, enkelt, snabbt och utan mellanhänder.



### Skapa en faktura för en kund



I menyn **Fakturor** klickar du på **Ny faktura**.



![capture](assets/fr/30.webp)



Ange **beloppet** och den **lokala valutan** (BTCPay beräknar automatiskt motvärdet i BTC) samt annan produktinformation.



![capture](assets/fr/31.webp)



Dela **QR-koden** eller **URL** med kunden.



![capture](assets/fr/32.webp)



### Spåra mottagna betalningar



Fortfarande i menyn **Fakturor** ser du en lista över alla dina transaktioner.


De möjliga statusarna är :





- Pending**: Betalningen har ännu inte bekräftats.





- Betald**: Betalning bekräftad.





- Förfallen**: faktura som inte betalats på förfallodagen.



### Återbetalning av en kund



I menyn **Fakturor** väljer du den faktura som ska återbetalas.



![capture](assets/fr/33.webp)



Klicka på **Refund** och ange den Bitcoin-adress som kunden har angett.



![capture](assets/fr/34.webp)



![capture](assets/fr/35.webp)



### Rapporter och dataexport



BTCPay Server låter dig **exportera dina transaktioner** (i CSV- eller Excel-format). Detta är mycket praktiskt för din redovisning och kassaregisteruppföljning.



![capture](assets/fr/36.webp)



I menyn **Rapport** klickar du på **Export**: alla dina transaktioner sparas i en CSV-fil som du sedan kan läsa lokalt.



## Säkerhet och bästa praxis



Den autonomi som BTCPay Server ger (full suveränitet över dina medel) är en verklig styrka. Men med denna frihet kommer ett större ansvar när det gäller säkerhet. Genom att hantera dina egna betalningar tar du på dig rollen som din egen bank. Därför är det absolut nödvändigt att använda bästa praxis för att skydda dina medel, dina data och din infrastruktur. Här är de viktigaste punkterna att tänka på.



### Säker åtkomst till din server





- Använd ett starkt lösenord: kombinera stora och små bokstäver, siffror och specialtecken. Undvik att återanvända ett befintligt lösenord.
- Aktivera tvåfaktorsautentisering (2FA) för att komma åt ditt BTCPay-gränssnitt.
- Uppdatera regelbundet ditt operativsystem, din BTCPay Server-instans och dina beroenden (Docker, Bitcoin-nod, Lightning-nod ...). Uppdateringar korrigerar ofta säkerhetsproblem.



### Hantering och säkerhetskopiering av privata nycklar





- Spara dina privata nycklar och seedphrases offline, på fysiska medier (papper eller metall).
- Använd företrädesvis en wallet hårdvara wallet.
- Spara flera kopior av dina säkerhetskopior på separata, skyddade fysiska platser.



### Säkra betalningar och sekretess





- Använd Tor-nätverket eller ett VPN för att dölja serverns IP-adress och skydda din integritet.
- Inaktivera onödiga portar på din server och begränsa SSH-anslutningar till endast betrodda adresser.
- Aktivera HTTPS (SSL-certifikat) för alla anslutningar till ditt BTCPay-webbgränssnitt.
- Dela aldrig ditt administrationsgränssnitt med personal som inte är utbildad i Bitcoin-portföljhantering.



### Implementering av bästa praxis för Lightning-nätverket



Din butik är ansluten till en **Lightning-nod som finns på Voltage**, vilket avsevärt förenklar den tekniska hanteringen av nätverket. Det är dock fortfarande viktigt att använda **goda övervaknings- och säkerhetsrutiner**:





- Spara din Voltage-nods API**-inloggning och åtkomstnycklar (som gör det möjligt för BTCPay att ansluta).
- Skydda ditt Voltage-konto** med tvåfaktorsautentisering och ett starkt lösenord.
- Övervaka nod- och kanalstatus** från din Voltage-instrumentpanel: detta hjälper dig att upptäcka eventuella avvikelser eller desynkronisering.
- Undvik att dela dina API**-autentiseringsuppgifter eller exponera dem offentligt (t.ex. i webbplatskod).
- Vid en migrering är det bara att **konfigurera om länken mellan BTCPay och Voltage**: ingen kanal behöver stängas manuellt.



Med Voltage drar du nytta av en **säker, mycket tillgänglig** och **automatiskt säkerhetskopierad** infrastruktur, samtidigt som du behåller **full suveränitet över dina Lightning-betalningar**.



### Organisera och strukturera interna rutiner





- Definiera en tydlig policy för åtkomsthantering: vem kan skapa en faktura, se betalningar, komma åt noden osv.
- Dokumentera dina rutiner för säkerhetskopiering och återställning så att du kan reagera snabbt om något skulle hända.
- Testa regelbundet återställningen av dina säkerhetskopior för att se till att de fungerar som de ska.
- Utbilda din personal eller dina medarbetare i grundläggande operativ säkerhet: vaksamhet mot nätfiske, användning av säkra lösenord, respekt för sekretess.



### Övervaka och etablera löpande underhåll





- Övervaka kontinuerligt serverns aktivitet med hjälp av loggning eller övervakningsverktyg.
- Planera en regelbunden säkerhetsgenomgång: kontrollera uppdateringar, åtkomst, säkerhetskopior och transaktionernas konsistens.



Vi gratulerar dig! Du har kommit till slutet av denna handledning. Du kan nu lära dig BTCPay Server på egen hand, vilket gör det lättare för dig att hantera din butik.



För att ta reda på mer rekommenderar jag att du går vår kompletta utbildning om att integrera Bitcoin i ditt företag:



https://planb.academy/courses/a804c4b6-9ff5-4a29-a530-7d2f5d04bb7a