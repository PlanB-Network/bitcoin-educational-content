---
name: Bisq 2
description: Komplett guide till att använda Bisq 2 och växla bitcoins P2P
---
![cover](assets/cover.webp)


## Inledning


KYC-fria peer-to-peer (P2P)-börser är viktiga för att bevara användarnas integritet och finansiella självständighet. De möjliggör direkta transaktioner mellan individer utan behov av identitetsverifiering, vilket är avgörande för dem som värdesätter integritet. För en mer djupgående förståelse av de teoretiska begreppen, ta en titt på BTC204-kursen:


https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

### Vad är Bisq 2?


Bisq 2 är den nya versionen av den populära decentraliserade Bisq Exchange, som lanserades 2024. Till skillnad från sin föregångare har Bisq 2 utvecklats för att stödja flera Exchange-protokoll, vilket ger användarna större flexibilitet.


**Viktiga nya funktioner:**




- Stöd för flera sekretessnätverk (Tor, I2P)
- Flera identiteter för ökad integritet
- REST API för handelsrobotar
- Stöd för flera Wallet-typer
- Rollsystem med obligatorisk deposition i BSQ


Denna guide fokuserar uteslutande på "Bisq Easy", det enda protokoll som för närvarande är tillgängligt. Bisq Easy har utformats speciellt för nya Bitcoin-användare. Detta protokoll gör det möjligt för användare att köpa och sälja Bitcoins mot fiatvalutor på en decentraliserad peer-to-peer-plattform. Transaktioner är begränsade till motsvarande 600 USD (med ett minimum på 6 USD), och Exchange-säkerheten förlitar sig på BTC-säljarnas rykte. Bisq Easy har inga handelsavgifter eller krav på säkerhetsdeposition. Bisq Easy förväntas ersätta Bisq 1 för kontantutbyten under 600 USD (eller motsvarande).


**Huvudfunktioner:**




- Skrivbordsapplikation för flera plattformar
- Flera Exchange-protokoll tillgängliga
- Decentraliserat P2P-nätverk
- Fokus på integritet (ingen KYC, användning av Tor)
- Icke-förvaltare (du behåller kontrollen över dina medel)
- Öppen källkod (AGPL)


### Skillnader med Bisq 1


**För köpare:**




- Ingen deposition krävs
- Inga handelsavgifter
- Inga Mining avgifter
- Säkerhet baserad på leverantörens rykte
- Lägre handelslimiter (motsvarande 600 USD)


**För säljare:**




- Ingen deposition krävs
- Bygga upp ett gott rykte
- Möjlighet att bränna BSQ eller skapa BSQ-obligationer
- Potentiellt högre försäljningspremie (10-15% över marknadspriset)


**Viktigt att notera:** När Bisq Multisig-protokollet har implementerats i Bisq 2 kan den gamla versionen av Bisq fasas ut. Bisq 1 kommer dock att fortsätta att användas som ett hanteringsverktyg för Bisq CAD och för BSQ-BTC-utbyten.


### Exchange-processen




- Den som skapar erbjudandet definierar villkoren för Exchange
- När handlarna har kommit överens om villkoren (betalningsmetod och pris) börjar Exchange
- Säljaren skickar sina bankuppgifter till köparen, och köparen skickar sina Bitcoin Address till säljaren
- Köparen erlägger kontant betalning och meddelar säljaren
- När betalningen har mottagits skickar säljaren bitcoins till köparens Address
- Exchange är slutfört när köparen tar emot bitcoins


### Viktiga regler




- Innan betalningsuppgifterna utväxlas kan Exchange annulleras utan motivering
- Efter att uppgifter har utväxlats kan underlåtenhet att uppfylla skyldigheter leda till bannlysning
- För banköverföringar, **använd aldrig termerna "Bisq" eller "Bitcoin"** i skälet till betalningen (detta kan leda till att pengarna fryses eller till och med att mottagarens eller betalarens bankkonto blockeras)
- Handlare måste logga in minst en gång om dagen för att följa processen
- Om det uppstår problem kan handlarna anlita en medlare


## Installation och konfiguration


### 1. Ladda ner och verifiera Bisq 2


![Téléchargement de Bisq 2](assets/fr/01.webp)




- Gå till [bisq.network](https://bisq.network/downloads/)
- Ladda ner den Bisq 2-version som motsvarar ditt operativsystem (skrolla ner på sidan)
- Verifiera äktheten för den nedladdade filen (rekommenderas starkt). För en detaljerad guide till signaturverifiering, se följande handledning:


https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

### 2. Installation enligt ditt system


Följ de installationssteg som gäller för ditt operativsystem. Om du stöter på några problem under installationen kan du läsa den detaljerade guiden på [officiella Bisq-wiki] (https://bisq.wiki/Downloading_and_installing).


### 3. Första uppstarten




- Starta Bisq 2 och godkänn användarvillkoren


![Conditions d'utilisation](assets/fr/01.webp)




- Skapa en ny profil genom att välja ett namn och en avatar


![Création du profil](assets/fr/02.webp)




- Du tas sedan till applikationens huvudinstrumentpanel, där du kan starta Bisq Easy för att köpa eller sälja dina första bitcoins


![Page d'accueil de Bisq 2](assets/fr/03.webp)


### 4. Konfigurera betalningsmetoder




- Gå till avsnittet om betalkonton från huvudmenyn


![Liste des comptes de paiement](assets/fr/04.webp)




- Lägg till en ny betalningsmetod genom att fylla i den information som krävs


![Création d'un nouveau compte de paiement](assets/fr/05.webp)


Att förkonfigurera betalningsmetoder är valfritt, men rekommenderas för att spara tid när du handlar. Du kan också konfigurera dina betalningsmetoder direkt under en handel genom att kontakta din Exchange-partner.


### 5. Kontosäkerhet


**Säkerhetskopiering av data:**


Till skillnad från Bisq 1 integrerar Bisq 2 för närvarande inte en Bitcoin Wallet: transaktioner utförs därför via dina egna externa plånböcker. Vi rekommenderar ändå att du regelbundet säkerhetskopierar din Bisq 2-datamapp. För att hitta din datamapp, se [officiella Bisq-wiki] (https://bisq.wiki/Backing_up_application_data#Back_up_the_entire_Bisq_data_directory).


**Identitetshantering:**


Med Bisq 2 kan du skapa flera identiteter. Varje identitet kan användas för olika typer av transaktioner. Dina identiteter lagras i datamappen.


## Köpa och sälja bitcoins


### Hur man köper Bitcoins


**Alternativ 1: Utnyttja ett befintligt erbjudande**




- På huvudskärmen väljer du "Bisq Easy", fliken "Komma igång" och klickar sedan på "Starta handelsguiden"


![Lancer trade wizard](assets/fr/06.webp)




- Välj "Köp Bitcoin" och välj din valuta


![Sélection achat Bitcoin](assets/fr/07.webp)


![Choix de la devise](assets/fr/08.webp)




- Konfigurera dina önskade betalningsmetoder (SEPA, Revolut etc.)


![Configuration méthodes de paiement](assets/fr/09.webp)




- Vid denna tidpunkt har du antingen en lista med erbjudanden som motsvarar dina tidigare kriterier, eller så måste du gå till "Offerbook"


![Liste des offres](assets/fr/10.webp)




- I det andra fallet kan du visa och filtrera erbjudanden med hjälp av knapparna längst upp till höger på Interface


![Filtres des offres](assets/fr/11.webp)




- När du har valt ditt erbjudande är allt du behöver göra att välja din betalningsmetod och sedan validera handelssammanfattningen


![Choix modalités de paiement](assets/fr/12.webp)


![Configuration du trade](assets/fr/13.webp)


![Récapitulatif du trade](assets/fr/14.webp)


**Alternativ 2: Skapa ditt eget erbjudande**




- Välj "Bisq Easy" och sedan "Offerbook"
- Välj ditt handelspar (t.ex. BTC/EUR)
- Klicka på "Skapa erbjudande
- Följ guiden för att skapa ett erbjudande: Definiera beloppet (fast eller intervall)


![Configuration du montant](assets/fr/20.webp)




- Välj accepterade betalningsmetoder


![Sélection méthodes de paiement](assets/fr/21.webp)




  - Kontrollera sammanfattningen och publicera erbjudandet


![Récapitulatif et publication](assets/fr/22.webp)


När Exchange har startats :




- Skicka din Bitcoin Address eller Lightning Invoice till säljaren


![Envoi adresse Bitcoin](assets/fr/15.webp)




- Ta emot säljarens bankuppgifter


![Réception coordonnées bancaires](assets/fr/16.webp)


![Détails coordonnées bancaires](assets/fr/17.webp)




- Genomför betalningen (utan att nämna "Bisq" eller "Bitcoin")
- Meddela säljaren om din betalning


![Notification paiement](assets/fr/18.webp)




- Vänta på att bitcoins ska komma fram


![Attente réception](assets/fr/19.webp)


### Hur säljer man Bitcoins?


Försäljningsprocessen på Bisq 2 följer en liknande logik som köpprocessen, med samma huvudsteg men i omvänd ordning. Du kan antingen skapa ett eget erbjudande om att sälja eller svara på ett befintligt erbjudande om att köpa. Här följer en genomgång av de olika alternativen och stegen i processen:


**Alternativ 1: Skapa ett erbjudande om försäljning**




- Välj "Bisq Easy" och sedan "Offerbook"
- Klicka på "Skapa erbjudande" och välj "Sälj Bitcoin"
- Konfigurera ditt erbjudande :
 - Välj valuta (EUR, USD, etc.)
 - Välj de accepterade betalningsmetoderna
 - Ställ in beloppet (mellan 6 och 600 motsvarande USD)
 - Fastställ ditt pris (fast eller % av marknaden)
- Kontrollera detaljer och publicera erbjudandet


**Alternativ 2: Ta ett befintligt erbjudande**




- Bläddra bland erbjudanden på fliken "Offerbook"
- Filtrera efter valuta och betalningsmetod
- Välj ett erbjudande som passar dig
- Kontrollera detaljer och acceptera erbjudandet


**Försäljningsprocess:**


När Exchange har startats :




   - Skicka dina bankuppgifter till köparen
   - Invänta köparens Bitcoin Address
   - Kontrollera att Address är giltig


Efter betalningsavisering :




   - Kontrollera att betalning har mottagits på ditt konto
   - Bekräfta att belopp och uppgifter stämmer
   - Skicka bitcoins till Address som tillhandahålls
   - Markera transaktionen som slutförd


Slutförande :




   - Invänta bekräftelse från köparen
   - Lämna feedback om transaktionen
   - Bygg upp ditt rykte för framtida försäljning


**Viktigt att notera:** Som säljare måste du vara särskilt vaksam på risken för chargebacks. Använd i första hand säkra betalningsmetoder och kontrollera alltid att betalningen har mottagits innan du skickar bitcoins.


## God praxis och säkerhet


### Tips om säkerhet


**För köpare:**




- Börja med små mängder
- Kontrollera säljarnas rykte (lägsta poäng 30 000)
- Använd endast de föreslagna betalningsmetoderna
- Kontrollera att säljaren är aktiv innan du skickar betalningen
- Använd endast de bankuppgifter som anges i Exchange-chatten
- Kommunicera aldrig utanför Bisq 2:s plattform
- Spara bevis på betalning
- Skicka aldrig känslig information


**För säljare:**




- Var försiktig med nya konton
- Undvik betalningsmetoder som är känsliga för återbetalningar (PayPal, Venmo)
- Kontrollera att kontouppgifterna stämmer överens med köparen
- Begränsa kommunikationen till chatt Bisq 2
- Öppna en medling i tveksamma fall


### Skapa ett gott rykte (för säljare)


För att förbättra ditt rykte som säljare på Bisq bör du genomföra regelbundna transaktioner och upprätthålla en professionell kommunikation med köparna. Svara snabbt på köparens förfrågningar för att säkerställa en positiv upplevelse. Du kan också skapa en BSQ-obligation för att visa din Commitment till plattformen. Dessa åtgärder kommer att bygga förtroende och locka fler köpare.


### Tvistlösning




- Kontakta din motpart via chatt
- Om nödvändigt, öppna en tvist
- Lämna in alla begärda bevis
- Följ medlarens instruktioner


### Integritetspolicy :




- Ingen registrering eller centraliserad identitetsverifiering krävs
- Alla anslutningar går via Tor-nätverket (och snart I2P)
- Ingen central server för lagring av data
- Transaktionsuppgifter kan endast läsas av de inblandade parterna


### Skydd mot censur :




- Fullt distribuerat P2P-nätverk
- Använda Tor-nätverket (och snart I2P) för att motstå censur
- Projekt med öppen källkod som hanteras av en DAO, utan någon centraliserad juridisk enhet


## Fördelar och nackdelar


### Fördelar med Bisq 2




- Maximal integritet**: Ingen KYC, användning av Tor
- Decentralisering**: Ingen central server
- Säkerhet**: Öppen källkod, kod utan förmyndarskap
- Intuitiv Interface**: enklare än Bisq 1
- Flexibilitet**: Flera Exchange-protokoll


### Bisq 2 nackdelar




- Begränsad likviditet** (för närvarande) :
 - Nytt protokoll i uppstartsfasen
 - Ett fåtal försäljningserbjudanden tillgängliga
 - Potentiellt långa väntetider för att hitta en köpare
- Gränser för handel**: Högst 600 USD per transaktion (med Bisq easy)
- Endast skrivbord**: Ingen mobilapplikation


## Framtida protokoll


Även om Bisq Easy för närvarande är det enda tillgängliga protokollet, är flera andra protokoll under utveckling för Bisq 2 :




- Bisq Lightning**: Exchange-protokoll baserat på ett spärrsystem som använder kryptografi för flerpartsberäkning på Lightning Network.
- Bisq MuSig**: Migrering av huvudprotokollet från Bisq 1 till Bisq 2, med hjälp av en 2-mot-2 Multisig med säkerhetsdepositioner.
- BSQ Swappar**: Omedelbara atomära swappar mellan BSQ och BTC.
- Liquid Swappar**: Exchange av tillgångar på Liquid Network (USDT, BTC-L) via atomära swappar.
- Monero Byten**: Atomutbyten mellan Bitcoin och Monero.
- Liquid MuSig**: Version av Multisig-protokollet som använder L-BTC för lägre kostnader och större integritet.
- Submarine Swaps**: Utbyten mellan Bitcoin på Lightning Network och Bitcoin On-Chain.
- Byte av stablecoin**: Atomiska utbyten mellan Bitcoin och USD stablecoins.
- Multisig Optioner**: Skapande av sälj- och köpoptioner för P2P med BTC-blockering i en On-Chain Multisig-transaktion.
- Multisig Öppna kontrakt**: Gör det möjligt att skapa anpassade villkorade kontrakt med hjälp av ett 2-på-3 Multisig-system med arbitrage.


Dessa protokoll är för närvarande under utveckling och kommer successivt att integreras i Bisq 2, vilket ger användarna större flexibilitet i enlighet med deras specifika behov.


## Användbara resurser




- Officiell webbplats: [bisq.network](https://bisq.network)
- Dokumentation: [Bisq Wiki](https://bisq.wiki)
- Stöd: [Forum Bisq](https://bisq.community)
- Källkod : [GitHub] (https://github.com/bisq-network)