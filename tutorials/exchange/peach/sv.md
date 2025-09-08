---
name: Persika
description: Komplett guide till att använda Peach och växla bitcoins P2P
---
![cover](assets/cover.webp)


![peach](https://youtu.be/ziwhv9KqVkM)


## Inledning


KYC-fria peer-to-peer (P2P)-börser är viktiga för att bevara användarnas integritet och finansiella självständighet. De möjliggör direkta transaktioner mellan individer utan behov av identitetsverifiering, vilket är avgörande för dem som värdesätter integritet. För en mer djupgående förståelse av de teoretiska begreppen, ta en titt på BTC204-kursen:


https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

### 1. Vad är Peach?


Peach är en P2P Exchange-plattform som gör det möjligt för användare att köpa och sälja bitcoins utan KYC. Den erbjuder en intuitiv Interface och avancerade säkerhetsfunktioner. Jämfört med andra lösningar som Bisq, HodlHodl och Robosat sticker Peach ut för sin användarvänlighet och låga avgifter.


### 2. Sekretess och datainsamling


**Vilken information samlar Peach in?


Peach strävar efter att lagra ett absolut minimum av uppgifter om sina användare. Här är en översikt över de uppgifter som lagras på servrarna:




- En Hash av din unika ansökningsidentifierare (AdID)
- En Hash av dina betalningsuppgifter
- Dina krypterade konversationer
- Transaktionsdata för att säkerställa att anonyma användare inte överskrider handelsgränsen (typer av betalningsmetoder som används, köp- och försäljningsbelopp)
- Adresser som används för att skicka och ta emot från spärrkontot
- Användningsdata (Firebase & Google Analytics), endast med ditt samtycke


Som en påminnelse är en Hash data som görs oigenkännliga, på samma sätt som kryptering. Samma data ger alltid samma Hash, vilket gör det möjligt att upptäcka dubbletter utan att känna till originaldata.


*För mer information om hashing kan du följa den här kursen:*


https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

**Vem kan se mina betalningsuppgifter?




- Endast din motpart kan se dina betalningsuppgifter
- Data överförs via Peach-servrar men är helt krypterade från början till slut
- I händelse av en tvist kommer dina betalningsuppgifter och din samtalshistorik att vara synliga för den utsedda Peach-medlaren


## Installation och konfiguration


### 1. Installera Peach-applikationen


![Installation de Peach](assets/fr/01.webp)




- Ladda ner applikationen från [Peach Bitcoin] (https://peachbitcoin.com/fr/quick-start/).
- Följ installationsanvisningarna på din enhet.
- Under installationen kommer du att bli ombedd att välja om du vill dela vissa uppgifter för att förbättra Peach-applikationen (bild 1)
- På nästa skärm (bild 2) har du två alternativ:
 - Om du är en ny användare klickar du på "Ny användare" för att skapa en ny profil
 - Om du redan har ett konto kan du använda "Restore" för att återställa din befintliga profil
- Om du har en hänvisningskod kan du ange den här.
- För att återställa ett befintligt konto (bild 3) behöver du :
 - Din backup-fil
 - Lösenordet för att dekryptera den här filen


### 2. Översikt över huvudskärmarna


Peach-applikationen är uppbyggd kring fyra huvudskärmar som nås från det nedre navigeringsfältet:


![Navigation dans l'application](assets/fr/02.webp)




- Hem** : Huvudskärmen för att köpa och sälja bitcoins. Det är här du kan skapa nya transaktioner och få tillgång till tillgängliga erbjudanden.
- Wallet**: Din integrerade Bitcoin Wallet som gör det möjligt för dig att :
 - Kontrollera ditt saldo
 - Ta emot bitcoins
 - Skicka bitcoins
 - Se din transaktionshistorik
- Handel** : Ditt handelshanteringscenter där du hittar :
 - Dina aktuella transaktioner
 - En fullständig historik över dina utbyten
 - Status för varje transaktion
- Inställningar** : Ditt kontos konfigurationshubb för :
 - Hantera dina betalningsmetoder
 - Konfigurera dina säkerhetskopior
 - Anpassa dina preferenser
 - Tillgång till hjälp och stöd


### 3. Konfigurera dina betalningsmetoder


![Accès aux paramètres de paiement](assets/fr/03.webp)


Få tillgång till betalningsmetoder via fliken Inställningar (bild 8)


**Online-betalningar


![Configuration des paiements en ligne](assets/fr/04.webp)




- Klicka på knappen för att lägga till en ny betalningsmetod
- Välj din valuta
- Välj önskad betalningsmetod


*Typer av betalningsmetoder tillgängliga:*


***Banköverföringar tillgängliga: ***




- SEPA (standard eller omedelbar)
- Fyll i dina SEPA-bankuppgifter


***Online plånböcker accepteras :***




- Flera alternativ tillgängliga beroende på ditt land (Revolut, Paypal, Wise, Strike, etc.)
- Följ instruktionerna för att lägga till dina inloggningsuppgifter


***Presentkortet som kan användas :***




- Amazonas
- Ange kortets utfärdandeland och annan nödvändig information


***Nationella betalningsalternativ:***


Landspecifika betalningssystem :




- Satispay (Italien)
- MB Way (Portugal)
- Bizum (Spanien)
- Snabbare betalningar (Förenade kungariket)


***Personliga betalningar:***


![Configuration des paiements en personne](assets/fr/05.webp)




- Välj "Meetup
- Välj sedan din mötesplats från listan


### Anvisningar för användning




- Du kan ställa in flera betalningsmetoder samtidigt
- Ju fler metoder du lägger till, desto bredare utbud av erbjudanden får du tillgång till
- Vänligen kontrollera att dina uppgifter är korrekta innan du registrerar dig
- Du kan när som helst ändra eller ta bort dina betalningsmetoder


**Säkerhetsanteckning**: Din betalningsinformation är krypterad och delas endast med din Exchange-partner under en transaktion.


### 4. Så här säkrar du din Wallet


** Förstå ditt Peach-konto


Ett Peach-konto är inte ett traditionellt konto med inloggning och lösenord. Det är en fil som lagras lokalt på din telefon, vilket innebär att Peach inte behöver lagra dina uppgifter eller känna till din identitet: du har kontrollen. Den här filen innehåller alla dina uppgifter, från dina Bitcoin Wallet-nycklar till dina betalningsuppgifter.


Detta tillvägagångssätt garanterar större integritet, men innebär också ett större ansvar. Om du tappar bort din telefon utan säkerhetskopia förlorar du tillgång till ditt Peach-konto och dina pengar. Det är därför viktigt att säkerhetskopiera den här filen och skydda den med ett starkt lösenord.


**Skapa dina säkerhetskopior**


![Accéder aux sauvegardes](assets/fr/13.webp)




- Gå till inställningarna via fliken längst ned till höger på startskärmen
- Välj alternativet "säkerhetskopior" i inställningsmenyn


![Processus de sauvegarde](assets/fr/06.webp)


Två typer av säkerhetskopiering är tillgängliga:


**Spara kontofilen (bild 14)**




- Klicka på "Skapa ny säkerhetskopia"
- Skapa ett starkt lösenord för att kryptera din backup-fil
- Förvara denna fil på en säker plats


Filbackupen återställer hela ditt Peach-konto, inklusive :




- Din Wallet
- Dina betalningsmetoder
- Konversationens historia
- Betalningsuppgifter
- Transaktionshistorik med motpartsinformation


**Spara återställningsfrasen (bild 15)**




- Följ anvisningarna för att visa din återställningsfras
- Skriv försiktigt ner orden i rätt ordning
- Förvara denna säkerhetskopia på en säker plats, helst på annan plats än kontofilen


Återvinningsfrasen återvinner endast :




- Tillgång till ditt konto
- Dina Bitcoin-medel


Du kommer att förlora :




- Konversationens historia
- Betalningsuppgifter
- Motpartsinformation i transaktionshistoriken


För optimal säkerhet rekommenderar vi att du utför båda typerna av säkerhetskopiering.


## Köpa och sälja bitcoins


### 1. Hur man köper Bitcoins


![Création et vue des offres](assets/fr/07.webp)




- Klicka på knappen "Köp" på startskärmen (bild 16)
- Konfigurera ditt köp enligt dina önskemål (bild 17)
- Bläddra i listan över tillgängliga erbjudanden (bild 18)


![Sélection et confirmation d'achat](assets/fr/08.webp)




- Välj det erbjudande som passar dig bäst (bild 19)
- Betala enligt överenskommen metod
- Bekräfta betalningen i applikationen och utvärdera transaktionen (bild 20)


![Réception des bitcoins](assets/fr/09.webp)




- Följ statusen för din transaktion
- Kontrollera bekräftelse på mottagande av bitcoins
- Pengarna kommer att finnas tillgängliga i din Peach Wallet


### 2. Hur man säljer Bitcoins


![Création d'un ordre de vente](assets/fr/10.webp)




- Konfigurera ditt försäljningserbjudande (bild 24)
- Finansiera transaktionen genom att skicka bitcoins till Address som tillhandahålls (bild 25)
- Vänta på bekräftelse av transaktionen (bild 26)
- Ditt erbjudande är nu synligt för köparna (bild 27)


![Attente du paiement](assets/fr/11.webp)




- Övervaka statusen för ditt erbjudande
- Invänta betalningsbekräftelse från köparen
- Kontrollera transaktionsdetaljer


![Finalisation de la vente](assets/fr/12.webp)




- Kontrollera betalningsstatus
- Bekräfta mottagandet av betalningen
- Utvärdera transaktionen
- Bitcoins släpps automatiskt till köparen


**Tips för en lyckad transaktion**




- Svara snabbt på meddelanden från din motpart
- Kontrollera betalningsuppgifterna noggrant
- Tveka inte att anlita medlingstjänsten om du har ett problem


**Säkerhetsanmärkning**: Bekräfta aldrig mottagandet av en betalning förrän du har kontrollerat att den har mottagits på ditt konto.


## Fördelar och nackdelar


### Fördelar med persika




- Ingen KYC krävs**: Bevarar användarnas integritet.
- Ingen tillgång till bankuppgifter**: Peach har ingen tillgång till dina bankuppgifter eller din identitet.
- Intuitiv Interface**: Enkel att använda för användare på mellannivå.
- Öppen källkod** : Källkoden är offentlig och kan verifieras av samhället.


### Nackdelar med persika




- Begränsad likviditet**: Mindre handelsvolym än mer etablerade plattformar.
- Regulatorisk risk** : Applikationen hanteras av ett schweiziskt företag. Den är därför föremål för schweiziska bestämmelser, som kan utvecklas och eventuellt censurera applikationen.


## Användbara resurser




- Förklarande video på franska: [YouTube] (https://youtu.be/ziwhv9KqVkM)
- Snabbstartguide: [Peach Bitcoin] (https://peachbitcoin.com/fr/quick-start/)