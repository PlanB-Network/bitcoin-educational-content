---
name: Peach
description: Komplett guide till att använda Peach och handla bitcoins i P2P
---

![cover](assets/cover.webp)





## Inledning



KYC-fria peer-to-peer (P2P)-börser är avgörande för att bevara användarnas konfidentialitet och finansiella självständighet. De möjliggör direkta transaktioner mellan individer utan behov av identitetsverifiering, vilket är avgörande för dem som värdesätter integritet. För en mer djupgående förståelse av teoretiska begrepp, se kursen BTC204:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

### 1. Vad är Peach?



Peach är en P2P-växlingsplattform som gör det möjligt för användare att köpa och sälja bitcoins utan KYC. Den erbjuder ett intuitivt gränssnitt och avancerade säkerhetsfunktioner. Jämfört med andra lösningar som Bisq, HodlHodl och Robosat sticker Peach ut för sin användarvänlighet.


Ett multisig-naturligt spärrsystem (2-2) garanterar säkerheten för medel under transaktioner. Peach stöder olika betalningsmetoder och har ett ryktessystem för att vägleda handlare i deras handlingar. Som vanligt med P2P-plattformar är det därför viktigt att upprätthålla ett gott rykte för att upprätthålla trovärdigheten hos andra handlare.



### 2. Integritet och insamlade data



**Vilken information samlar Peach in?



Peach strävar efter att lagra det absoluta minimum av data om sina användare. Här är en översikt över de uppgifter som lagras på våra servrar:





- En hash av din unika ansökningsidentifierare (AdID)
- En hash av dina betalningsuppgifter
- Dina krypterade konversationer
- Transaktionsdata för att säkerställa att anonyma användare inte överskrider handelsgränsen (typer av betalningsmetoder som används, köp- och försäljningsbelopp)
- Address som används för att skicka och ta emot från depositionskontot
- Användningsdata (Firebase & Google Analytics), endast med ditt samtycke



Som en påminnelse är en hash data som görs oigenkännliga, på samma sätt som kryptering. Samma data kommer alltid att ge samma hash, vilket gör det möjligt att upptäcka dubbletter utan att känna till originaldata.



*För en mer detaljerad förklaring av hashing, gå den här kursen:*



https://planb.academy/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

**Vem kan se mina betalningsuppgifter?





- Endast din motpart kan se dina betalningsuppgifter
- Data överförs via Peach:s servrar, men är helt krypterade från början till slut
- I händelse av en tvist kommer dina betalningsuppgifter och din samtalshistorik att vara synliga för den tilldelade Peach-medlaren



## Installation och konfiguration



### 1. Installera Peach-applikationen



![Installation de Peach](assets/fr/01.webp)





- Ladda ner applikationen från [Peach Bitcoin] (https://peachbitcoin.com/fr/quick-start/). På iOS måste du först installera appen [testflight] (https://apps.apple.com/us/app/testflight/id899247664).
- Följ installationsanvisningarna på din enhet.
- Under installationen kommer du att bli ombedd att välja om du vill dela vissa data för att förbättra Peach-applikationen. (Bild 1)
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





- Startsida (4)** : Huvudskärmen där du kan välja att köpa eller sälja, skapa nya transaktioner och få tillgång till tillgängliga erbjudanden:
 - skapa erbjudanden med de två knapparna nedan (skapa köp / skapa sälj)
 - dra nytta av befintliga erbjudanden som skapats av andra användare, med hjälp av de två knapparna nedan ("Köp"/"Sälj").





- Wallet (5)** : Din integrerade bitcoin wallet som gör att du kan :
 - Kontrollera ditt saldo
 - Ta emot bitcoins
 - Envoyer bitcoins (med myntkontroll)
 - Se din transaktionshistorik
 - Finansiering av din försäljning





- Trades (6)**: dina nuvarande och tidigare kontrakt, under tre flikar:
 - Pågående inköp
 - Pågående försäljning
 - Historiken för dina börser





- Inställningar (7)** : Konfigurationshubben för
 - Se din profil (rykte, utmärkelser, gränser etc.)
 - Hantering av säkerhet (backup, pin)
 - Hantera dina betalningsmetoder
 - Kontakta support
 - Ändra språk
 - etc.



### 3. Konfigurera dina betalningsmetoder



![Accès aux paramètres de paiement](assets/fr/03.webp)



Du kan hantera dina betalningsmetoder i inställningarna (bild 8)



Peach erbjuder onlinebetalningar och betalningar ansikte mot ansikte (endast vid registrerade möten).



**Online-betalningar



**Viktigt:**


för att skydda användare kräver Peach att källan till medel matchar den som annonseras. Det är upp till handlare att se till att detta är fallet, för deras eget skydd.



![Configuration des paiements en ligne](assets/fr/04.webp)



För att lägga till en metod :




- På fliken "online" klickar du på "lägg till en valuta/metod"
- Välj din valuta
- Välj önskad betalningsmetod



*Typer av betalningsmetoder tillgängliga:*



***För banköverföringar: ***




- SEPA (standard eller omedelbar)
- Fyll i dina SEPA-bankuppgifter.



***Online wallet accepteras :***




- Flera alternativ tillgängliga beroende på ditt land (Revolut, Paypal, Wise, Strike, etc.)
- Följ instruktionerna för att lägga till dina inloggningsuppgifter



*presentkort användbart:*** Presentkort användbart:*** Presentkort användbart:*** Presentkort användbart:*** Presentkort användbart:*** Presentkort användbart:*** Presentkort användbart:***




- Amazon, Steam, etc.
- Ange kortets utfärdandeland och annan nödvändig information



***Nationella betalningsalternativ:***


Landspecifika betalningssystem :




- Satispay (Italien)
- MB Way (Portugal)
- Bizum (Spanien)
- Snabbare betalningar (Förenade kungariket)
- etc.



***För betalningar som sker ansikte mot ansikte: ***



![Configuration des paiements en personne](assets/fr/05.webp)





- Välj "Meetup" (bild 12)
- Välj sedan din mötesplats från listan (bild 13)



### Anvisningar för användning





- Du kan lägga till flera betalningsmetoder
- Ju fler metoder du lägger till, desto bredare utbud av erbjudanden får du tillgång till
- Kontrollera att dina uppgifter är korrekta innan du registrerar dig
- Du kan när som helst ändra eller ta bort dina betalningsmetoder



**Säkerhetsanteckning**: Din betalningsinformation är krypterad och delas endast med din bytespartner under en transaktion, förutom i händelse av en tvist där en Peach-medlare också kommer att ha tillgång.



### 4. Så säkrar du din portfölj



** Förstå ditt Peach-konto



Ett Peach-konto har inget användarnamn och lösenord. Det är en fil som lagras lokalt på din telefon, vilket innebär att Peach inte behöver lagra dina uppgifter eller känna till din identitet: du har kontrollen. Den här filen innehåller all din data: inklusive de 12 bitcoinåterställningsorden, PGP-nycklar, betalningsinformation och så vidare. Det är därför viktigt att spara den här filen och skydda den med ett __robust__ lösenord.



Detta tillvägagångssätt garanterar en viss grad av sekretess och lämnar ansvaret för data- och säkerhetskopieringshantering i händerna på användaren. Om du förlorar din telefon utan en säkerhetskopia innebär det att du förlorar åtkomsten till ditt Peach-konto och dina pengar.



**Skapa dina säkerhetskopior**






- Gå till inställningarna via fliken längst ned till höger på startskärmen
- Välj alternativet "säkerhetskopior" i inställningsmenyn



![Processus de sauvegarde](assets/fr/06.webp)



Två typer av säkerhetskopiering är tillgängliga:



**Spara kontofilen (bild 14)**




- Klicka på "Skapa ny säkerhetskopia"
- Skapa ett **strong** lösenord för att kryptera din backup-fil
- Skicka den här filen till en plats där den finns kvar om telefonen skulle försvinna.



Säkerhetskopian av filen återställer hela ditt Peach-konto, inklusive :




- Din portfölj
- Dina betalningsmetoder
- Betalningsuppgifter
- Transaktionshistorik med uppgifter om motparter och konversationer med dem



**Spara återställningsfrasen (bild 15)**




- Följ anvisningarna för att visa din återställningsfras
- Skriv försiktigt ner orden i rätt ordning
- Förvara denna säkerhetskopia på en säker plats, helst på annan plats än kontofilen



Återställningsfrasen gör att du kan återställa :




- Ditt rykte, dina affärer
- Dina bitcoin-fonder



Men ** INTE** följande:




- Dina nuvarande och tidigare konversationer
- Betalningsuppgifter
- Motpartsinformation i transaktionshistoriken




## Köpa och sälja bitcoins



### 1.a Hur man köper bitcoins: Ta ett erbjudande att sälja



En köpares första reflex bör vara att kolla in de erbjudanden till försäljning som redan är finansierade med bitcoin.



![Vue des offres de vente et filtres](assets/fr/07.webp)





- Klicka på knappen "Köp" på startskärmen (bild 16)
- Du kan sedan bläddra i en lista över bitcoins som har placerats i escrow-systemet och är redo för försäljning (bild 17). Du kan se beloppet, priset (i % i förhållande till KYCmarknaden), betalningsmetoderna och de valutor som accepteras.
- Använd filter för att sortera och ordna erbjudanden (bild 18).
- Knappen längst ned på filtersidan gör att du kan få ett meddelande när ett erbjudande som matchar dina filter har publicerats; och knappen "Återställ", som helt enkelt rensar alla filter (bild 18).



![Sélection et confirmation d'achat](assets/fr/08.webp)





- Visa det erbjudande som passar dig och skicka en bytesbegäran (bild 19)
- Du kan göra flera bytesansökningar, och det första positiva erbjudandet kommer att annullera dina andra ansökningar.
- Gör betalningen på överenskommet sätt.


**Påminnelse:** källan till pengarna måste överensstämma med den du angav när du lade till betalningsmetoden.




- Bekräfta din betalning i applikationen så snart den är genomförd**.
- Vänta på att säljaren tar emot betalningen och deklarera den som sådan (bild 20)
- Och slutligen, utvärdera din upplevelse med säljaren (bild 21)



![Réception des bitcoins](assets/fr/09.webp)





- Följ statusen för din transaktion
- Kontrollera bekräftelse på mottagande av bitcoins
- Pengarna kommer att finnas tillgängliga i din Peach-portfölj (bild 22 och 23)



### 1.b Hur man köper bitcoins: Skapa ett bud



Om du inte kan hitta ett lämpligt erbjudande att sälja kan du skapa ett erbjudande att köpa. Eftersom detta inte binder några bitcoin i det här skedet har du mindre chans att hitta en bytespartner, särskilt om ditt track record och rykte är dåligt eller obefintligt. För att åtgärda detta är det viktigt att du, när du skapar erbjudandet, *gör ett högt premiumerbjudande* för att motivera säljare att välja ditt erbjudande. Låt oss gå vidare:



![Creation d'ordre d'achat](assets/fr/10.webp)





- Klicka på knappen "Skapa ett köpeerbjudande" på startskärmen (bild 24)
- Lägg till en betalningsmetod, om du inte redan har gjort det, och ange dina preferenser (antal, premium etc.) (bild 25).


Med alternativet "direkt" kan du acceptera en handelsförfrågan automatiskt.




 - Klicka igen på "skapa ett bud" för att fortsätta
- När appen har skapats är det säljarens tur att komma till dig med en bytesbegäran. Du kan stänga och lämna appen utan bekymmer.
- Du kan ändra premien om du inte får några förfrågningar. Kom ihåg: en högre premie kommer att motivera säljarna att komma och titta på ditt erbjudande (bild 26).
- Du hittar ditt erbjudande i fliken "Köp", som i sin tur finns i fönstret "Exchange" (fig. 27)



![Reception d'une demande de vente, messagerie](assets/fr/11.webp)





- När du får en köpbegäran (bild 28) (och om du inte har avaktiverat omedelbar handel i bild 25), accepterar du affären efter att ha kontrollerat säljarens rykte. Om omedelbar handel är aktiverad hoppar du direkt till bild 29.
- Säljaren måste sedan placera bitcoin i escrow-systemet, ("fund the safe"). (bild 29)
- Betala sedan säljaren på den plats som visas i fig. 30 via ditt personliga banksystem. Dra inte markören "Jag har gjort betalningen" förrän du har gjort det!
- Du kan kommunicera med säljaren via meddelandesystemet (P2P krypterat). Om det uppstår problem kan du öppna en tvist genom att klicka på ikonen i det övre högra hörnet (bild 31). En Peach-medlare kommer då att delta i diskussionen.



![Offre de vente completée](assets/fr/12.webp)





- När säljaren har fått pengarna kommer han att rapportera det och escrow-systemet kommer att frigöra bitcoin, som kommer att vara på väg till din wallet (som standard via GroupHug, Peach:s transaktionsgrupperingssystem, som körs en gång om dagen),
- Betygsätt din erfarenhet av säljaren



Så där ja!



**Notering för nya köpare:** Säljarna baserar sina affärer på köparnas rykte och tenderar att undvika bud från köpare som inte har några avslutade affärer. Det är lättare att i första hand bygga upp ett rykte genom att acceptera befintliga erbjudanden om att sälja.




### 2.a Hur man säljer bitcoins: Skapa en försäljning



Det snabbaste och enklaste sättet att sälja på Peach är att **skapa ett erbjudande om att sälja**.



![Création d'un ordre de vente](assets/fr/13.webp)





- På startsidan klickar du på "Skapa ett försäljningserbjudande" (bild 32)
- Ställ in ditt erbjudande, se till att du anger en betalningsmetod och rätt parametrar


du kan också :




  - skapa flera identiska erbjudanden
  - aktivera "omedelbar bytesrätt" så att den första köparen som dyker upp kan ta över kontraktet (utan din bekräftelse) och fortsätta med betalningen.
  - välj en återbetalningsadress
  - finansiera trunken från din wallet Peach
- Finansiera transaktionen genom att skicka bitcoins till den angivna adressen (bild 34)
- Vänta på bekräftelse av transaktionen. När det är gjort kommer ditt erbjudande att synas på marknaden.



![Attente du paiement](assets/fr/14.webp)





- Vänta på att en köpare ska anta ditt erbjudande. Överväg att höja premien (%) om du vill skynda på processen (bild 36)
- När du har fått en bytesbegäran kan du kontrollera köparens rykte. Bedöm själv om profilen passar dig och klicka på "acceptera" om den gör det. (37)
- Nu är det köparens tur att göra betalningen från sin bank till din. Han kommer sedan att vidarebefordra betalningen till dig. Tveka inte att kontakta köparen i chatten.
- efter att ha kontrollerat att pengarna har mottagits av din bank*, frigör du pengarna genom att klicka på knappen "jag har mottagit betalning" (bild 38). Bekräfta aldrig mottagandet av en betalning innan du har kontrollerat att den har kommit in på ditt konto.
- Utvärdera transaktionen
- Bitcoin släpps automatiskt till köparen,



Så där ja!



**Säkerhetsinformation och tips för en lyckad transaktion:**




 - Observera köparens uppgifter och kontrollera att pengarnas ursprung stämmer överens med det som beskrivs på Peach Om pengarnas ursprung inte stämmer överens med det som meddelats, gå till Chatt och öppna en diskussion (bild 39) och skicka tillbaka pengarna till deras ursprung.
 - Följ instruktionerna i den gula katten.
 - Svara snabbt på meddelanden från din motpart
 - var försiktig med köparens attityd, särskilt när det handlar om en profil med liten erfarenhet
 - Tveka inte att anlita medlingstjänsten om du har ett problem



### 2.b Hur man säljer bitcoins: ta ett bud



Det är också möjligt att visa och välja köperbjudanden. Du måste vara särskilt försiktig, eftersom det är här de flesta bedragare finns.



![Prendre une offre d'achat](assets/fr/15.webp)





- På startsidan klickar du på "Försäljning" (bild 40)
- Använd filtren för att se och välja de mest attraktiva erbjudandena (bild 41)



![vérification de la réputation](assets/fr/16.webp)





- innan du begär ett byte rekommenderar vi att du bedömer lämpligheten i köparens profil. Du kan klicka på ett erbjudande och sedan på användarens ID för att se hans profil. Erbjudandet i bild 42 kan till exempel anses vara "riskabelt" (ny användare, relativt högt belopp). Den "risk" du löper genom att anta detta erbjudande är helt enkelt att du slösar bort tid, så länge du inte gör misstaget att släppa bitcoins utan att ha fått pengarna. Du kan fortfarande sätta in bitcoins i kassaskåpet.


Den på bild 43 kommer å andra sidan från en erfaren handlare (bild 44), utan några tvister i sin historia. Det är därför ett mindre riskabelt erbjudande.



![Match avec vendeur](assets/fr/17.webp)





- När erbjudandet har begärts, och om köparen accepterar din begäran, kommer programmet att ta dig till bild 34, där du kan fortsätta handeln enligt beskrivningen nedan.




## Fördelar och nackdelar



### Peach fördelar





- Ingen KYC krävs**: Bevarar användarnas sekretess.
- Ingen tillgång till bankuppgifter**: Peach har ingen tillgång till dina bankuppgifter eller din identitet.
- Interface intuitiv**: Enkel att använda för användare med lite erfarenhet.
- Öppen källkod** : Källkoden är offentlig och kan verifieras av samhället.



### Peach nackdelar





- Begränsad Liquidity**: Mindre handelsvolym än mer etablerade plattformar.
- Regulatorisk risk** : Applikationen hanteras av ett schweiziskt företag. Den är därför föremål för schweiziska bestämmelser, som kan utvecklas och eventuellt censurera applikationen.



## Användbara resurser





- Förklarande video på franska: [YouTube] (https://youtu.be/ziwhv9KqVkM)
- Snabbstartsguide: [Peach Bitcoin](https://peachbitcoin.com/fr/quick-start/)
- [Support telegram](t.me/peachtopeach) (se upp för bedragare, administratörer kommer aldrig att skriva till dig först via privat meddelande)