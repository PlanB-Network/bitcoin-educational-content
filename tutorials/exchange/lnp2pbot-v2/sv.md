---
name: LNP2PBot
description: Komplett guide till LNP2PBot och P2P Bitcoin-handel
---
![cover](assets/cover.webp)


## Inledning


KYC-fria peer-to-peer (P2P)-börser är avgörande för att bevara användarnas konfidentialitet och finansiella självständighet. De möjliggör direkta transaktioner mellan individer utan behov av identitetsverifiering, vilket är avgörande för dem som värdesätter integritet. För en mer djupgående förståelse av de teoretiska begreppen, ta en titt på BTC204-kursen:


https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Att köpa och sälja Bitcoin peer-to-peer (P2P) är en av de mest privata metoderna för att förvärva eller avyttra bitcoins. LNP2PBot är en Telegram-bot med öppen källkod som underlättar P2P-utbyten på Lightning Network, vilket möjliggör snabba, billiga och KYC-fria transaktioner.


### Varför använda Lnp2pbot?




- Ingen KYC krävs
- Snabba transaktioner på Lightning Network
- Låga kostnader
- Enkel Interface via Telegram, en populär meddelandeapplikation som är tillgänglig från var som helst i världen
- Integrerat ryktessystem
- Automatisk spärr för säker handel
- Stöd för flera valutor
- Aktiv och växande gemenskap


### Förkunskapskrav


För att använda Lnp2pbot behöver du :


1. Lightning Network Wallet (Breez, Phoenix eller Blixt rekommenderas)


2. Telegram-applikationen installerad (https://telegram.org/)


3. Ett Telegram-konto med ett definierat användarnamn


## Installation och konfiguration


### 1. Konfigurera din Lightning Wallet


Börja med att installera en kompatibel Lightning Wallet. Här är våra detaljerade rekommendationer:


**Rekommenderade plånböcker**




- [Breez] (https://breez.technology)**:
  - Utmärkt för nybörjare
  - Intuitiv, modern Interface
  - Icke-förvaltare (du behåller kontrollen över dina medel)
  - Perfekt kompatibel med Lnp2pbot
  - Tillgänglig på iOS och Android


Nedan finns en länk till handledningen för denna Wallet:


https://planb.network/tutorials/wallet/mobile/breez-46a6867b-c74b-45e7-869c-10a4e0263c06


- [Phoenix] (https://phoenix.acinq.co)** :
  - Enkel och tillförlitlig
  - Automatisk kanalkonfiguration
  - Inbyggt stöd för BOLT11-fakturor
  - Utmärkt för vardagliga transaktioner
  - Tillgänglig på iOS och Android


Nedan finns en länk till handledningen för denna Wallet:


https://planb.network/tutorials/wallet/mobile/phoenix-0f681345-abff-4bdc-819c-4ae800129cdf


- [Blixt](https://blixtwallet.github.io)** :
  - Mer teknisk men mycket komplett
  - Avancerade konfigurationsalternativ
  - Perfekt för erfarna användare
  - Öppen källkod
  - Tillgänglig på Android


Nedan finns en länk till handledningen för denna Wallet:


https://planb.network/tutorials/wallet/mobile/blixt-04b319cf-8cbe-4027-b26f-840571f2244f

**Viktigt om andra plånböcker**


⚠️ **Viktigt**: Innan du säljer Sats, se till att din Wallet stöder "hold" -fakturor, som används av botten som ett spärrsystem.




- Wallet av Satoshi**: Fungerar bra för att ta emot Sats, men det kan uppstå förseningar i uppdateringen av saldot om en försäljning avbryts.
- Muun **: Rekommenderas inte eftersom betalningar kan misslyckas på grund av gränser för bot-routingavgifter (högst 0,2%).
- Aqua**: Fungerar för att ta emot Sats, men kan ha långa fördröjningar (upp till 48 timmar) för saldouppdateringar i händelse av en annullering av försäljningen.


💡 **Tips**: För optimal upplevelse, välj rekommenderade plånböcker (Breez, Phoenix eller Blixt).


⚠️ **Viktigt**: Glöm inte att spara dina återställningsfraser på en säker plats.


### 2. Komma igång med Lnp2pbot


1. Klicka på den här länken för att komma åt botten: [@lnp2pBot](https://t.me/lnp2pbot)


2. Telegram kommer att öppnas automatiskt


3. Klicka på "Start" eller skicka kommandot "/start"


4. Boten kommer att be dig att skapa ett användarnamn om du inte redan har ett


5. Boten kommer att vägleda dig genom den inledande konfigurationen


### 3. Gå med i gemenskapen




- Gå med i huvudkanalen: [@p2plightning](https://t.me/p2plightning)
- Support: [@lnp2pbotHelp](https://t.me/lnp2pbotHelp)


## Köpa och sälja bitcoins


Det finns två huvudsakliga sätt att Exchange bitcoins på Lnp2pbot:


1. Bläddra bland och svara på befintliga erbjudanden på marknaden


2. Skapa ditt eget erbjudande om att köpa eller sälja


I den här guiden tar vi en detaljerad titt på hur :




- Köp bitcoins från ett befintligt erbjudande
- Sälj bitcoins genom att skapa ditt eget erbjudande


### Hur man köper Bitcoins


**1. Hitta och välj ett erbjudande**


![Sélection d'une offre de vente](assets/fr/01.webp)


Bläddra bland erbjudandena i [@p2plightning](https://t.me/p2plightning) och klicka på knappen "Köp satoshis" under den annons du är intresserad av.


**2. Validera erbjudande och belopp**


![Validation de l'offre](assets/fr/02.webp)


1. Återgå till botchatt


2. Bekräfta ditt val av erbjudande


3. Ange det belopp i fiatvaluta som du vill köpa


4. Boten kommer att be dig att ange en Lightning Invoice för beloppet i satoshis


**3. Kontakta säljaren**


![Mise en relation](assets/fr/03.webp)


När Invoice har skickats sätter boten dig i kontakt med säljaren.


**4. Kommunikation med säljaren**


![Chat privé](assets/fr/04.webp)


Klicka på säljarens smeknamn för att öppna en privat chattkanal där du kan Exchange fiat betalningsuppgifter.


**5. Bekräftelse av betalning


![Confirmation du paiement](assets/fr/05.webp)


Efter att ha gjort fiat-betalningen använder du kommandot `/fiatsent` i botchatten. När transaktionen är klar kommer du att kunna betygsätta säljaren och transaktionen kommer att avslutas.


### Hur man säljer Bitcoins


**1. Skapa ett försäljningserbjudande**


![Création d'une offre de vente](assets/fr/06.webp)


För att skapa ett försäljningserbjudande använder du bara kommandot :


`/sälja`


Boten kommer sedan att vägleda dig steg för steg:


1. Välj din valuta


2. Ange hur många satoshis som ska säljas


3. För priset har du två alternativ:




   - Ange ett fast pris för kvantiteten satoshis
   - Använd marknadspriset med möjlighet att tillämpa en premie (positiv eller negativ)


💡 **Tips**: Premien gör att du kan justera ditt pris i förhållande till marknadspriset. Till exempel innebär en premie på -1% att du säljer för 1% mindre än marknadspriset.


**2. Bekräftelse på skapande av order**


![Confirmation de l'ordre de vente](assets/fr/07.webp)


När ordern har skapats får du en bekräftelse med möjlighet att avbryta ordern med kommandot `/cancel`.


**3. Hantera försäljning**


![Prise de l'ordre par un acheteur](assets/fr/08.webp)




- När en köpare svarar på ditt erbjudande får du ett meddelande med en QR-kod och en Invoice för att betala.
- Kontrollera köparens profil och rykte.


![Mise en relation avec l'acheteur](assets/fr/09.webp)




- Klicka på köparens smeknamn för att öppna en privat diskussionskanal.
- Kommunicera betalningsuppgifter för fiat till köparen.
- Invänta bekräftelse på fiat-betalning från köparen.
- Kontrollera att betalning har mottagits på ditt konto.


![Confirmation de la fin de l'ordre](assets/fr/10.webp)




- Bekräfta transaktionen med `/release` och slutför ordern. Du kommer att få möjlighet att betygsätta köparen.


## God praxis och säkerhet


### Tips om säkerhet




- Börja med små mängder
- Kontrollera alltid användarnas rykte
- Använd endast de föreslagna betalningsmetoderna
- Håll all kommunikation i bot-chatten
- Dela aldrig känslig information


### System för gott rykte




- Varje användare har en ryktespoäng
- Framgångsrika transaktioner ökar din poäng
- Välj användare med gott rykte
- Rapportera alla misstänkta beteenden till moderatorerna


### Tvistlösning


1. När problem uppstår, håll dig lugn och professionell


2. Använd kommandot `/dispute` för att öppna ett ärende


3. Tillhandahålla alla nödvändiga bevis


4. Vänta på en moderator


## Jämförelse med andra lösningar


Lnp2pbot har flera fördelar och nackdelar jämfört med andra P2P Exchange-lösningar som Peach, Bisq, HodlHodl och Robosat:


### Fördelar med Lnp2pbot




- Ingen KYC krävs ** : Till skillnad från vissa plattformar kräver Lnp2pbot inte identitetsverifiering, vilket bevarar användarnas konfidentialitet.
- Snabba transaktioner**: Tack vare Lightning Network är transaktionerna nästan ögonblickliga.
- Låga avgifter** : Transaktionskostnaderna är lägre än för traditionella börser.
- Tillgänglighet för mobiler**: LNP2PBot är tillgängligt via Telegram, vilket gör det enkelt att använda på mobila enheter.
- Lätt att använda** : Lnp2pbot's intuitiva Interface gör det enkelt att använda, även för mindre erfarna användare.


### Nackdelar med Lnp2pbot




- Beroende av Telegram**: Att använda Lnp2pbot kräver ett Telegram-konto, vilket kanske inte är lämpligt för alla användare.
- Mindre likviditet**: Jämfört med mer etablerade plattformar som Bisq kan likviditeten vara mer begränsad.


I jämförelse erbjuder lösningar som Bisq större likviditet och en stationär Interface, men kan innebära högre avgifter och längre transaktionstider. HodlHodl och Robosat erbjuder också KYC-fri handel, men med olika avgiftsstrukturer och gränssnitt.


## Användbara resurser




- Officiell webbplats: https://lnp2pbot.com/
- Dokumentation: https://lnp2pbot.com/learn/
- GitHub: https://github.com/lnp2pBot/bot
- Support: [@lnp2pbotHelp](https://t.me/lnp2pbotHelp)