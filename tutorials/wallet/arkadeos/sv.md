---
name: ArkadeOS
description: Komplett guide till Arkade-portföljen och Ark Protocol
---

![cover](assets/cover.webp)



Bitcoin-nätverket står inför en stor utmaning: skalbarhet. Även om huvudlagret (lager 1) erbjuder oöverträffad säkerhet och decentralisering kan det bara hantera ett begränsat antal transaktioner per sekund. Lightning Network har framstått som en lovande lösning för det andra lagret (lager 2), som möjliggör snabba betalningar till låg kostnad. Lightning har dock sina egna begränsningar: kanalhantering, behov av inkommande likviditet och en teknisk komplexitet som kan avskräcka nya användare.



Detta är bakgrunden till **Ark**, ett nytt lager 2-protokoll som är utformat för att erbjuda en förenklad användarupplevelse utan att offra suveränitet. **ArkadeOS** (eller Arkade) är den första större implementeringen av detta protokoll och erbjuder en nästa generations Bitcoin-portfölj.



Denna handledning kommer att guida dig genom Arkades värld. Vi kommer att utforska hur Ark-protokollet fungerar, hur du installerar och konfigurerar Arkade wallet och hur du använder den för att skicka och ta emot bitcoins direkt, konfidentiellt och utan de vanliga Lightning Network-friktionsmomenten.



## Förståelse av Ark-protokollet



Innan vi dyker in i användningen av Arkade är det viktigt att förstå nyckelbegreppen i Ark-protokollet som driver det. Ark är inte en separat blockkedja, utan en intelligent samordningsmekanism ovanpå Bitcoin.



### VTXO-konceptet


I hjärtat av Ark finns **VTXO** (Virtual UTXO). En VTXO är en UTXO som ännu inte har publicerats på Bitcoin-blockkedjan: den finns utanför huvudkedjan (off-chain) men backas upp av transaktioner som har signerats i blockkedjan.



Till skillnad från ett saldo på en centraliserad börs tillhör en VTXO verkligen dig. Du har ett kryptografiskt bevis som gör att du när som helst kan göra anspråk på motsvarande riktiga bitcoins på blockkedjan, även om Ark-servern försvinner. VTXO:er gör att du kan överföra värde direkt mellan användare utan att vänta på blockbekräftelser.



### ASP:s (Ark Service Provider) roll


Ark-protokollet fungerar enligt en klient-servermodell. Servern kallas **ASP** (Ark Service Provider). ASP:n spelar rollen som dirigent:




- Det ger den nödvändiga likviditeten för nätverket.
- Den samordnar transaktioner mellan användare.
- Den organiserar "rundor" för avveckling på blockkedjan.



Det är viktigt att notera att ASP är **inte frihetsberövande**. Den har aldrig dina privata nycklar och kan inte heller stjäla dina pengar. Dess roll är rent teknisk och logistisk. Om en ASP censurerar dina transaktioner eller går ner kan du alltid få tillbaka dina pengar genom ett ensidigt utträdesförfarande.



### Rundor och integritet


Transaktioner på Ark slutförs i omgångar som kallas **Rounds**. Med jämna mellanrum (t.ex. med några sekunders mellanrum) samlar ASP alla väntande transaktioner och förankrar dem i Bitcoin-blockkedjan i en enda optimerad transaktion.


Denna mekanism erbjuder två stora fördelar:




- Skalbarhet**: En enda on-chain-transaktion kan validera tusentals off-chain-betalningar, vilket drastiskt minskar kostnaderna för användarna.
- Konfidentialitet**: Varje omgång fungerar som en **CoinJoin**. Pengar från alla deltagare blandas i en gemensam pool innan de omfördelas i form av nya VTXO:er. Detta bryter länken mellan avsändare och mottagare, vilket gör det extremt svårt, om inte omöjligt, för en utomstående observatör att spåra betalningar.



## Presentation av ArkadeOS



ArkadeOS är den konkreta applikation som gör Ark-protokollet tillgängligt för allmänheten. Den är utvecklad av Ark Labs och är ett komplett ekosystem som består av en portfölj (Wallet), en server (Operator) och utvecklarverktyg.



För slutanvändaren tar Arkade formen av en elegant, intuitiv webb-wallet (PWA - Progressive Web App). Den döljer den kryptografiska komplexiteten hos VTXO:er och rundor bakom ett välbekant gränssnitt. Med Arkade har du en adress för att ta emot, en knapp för att skicka och en transaktionshistorik, precis som en klassisk wallet, men med kraften i Arks omedelbarhet och konfidentialitet.



## Installation och konfiguration



Eftersom Arkade är en Progressive Web App är den särskilt enkel att installera och behöver inte nödvändigtvis involvera traditionella applikationsbutiker.



### Tillträde och installation


Du kan komma åt Arkade direkt från alla moderna webbläsare (Chrome, Safari, Brave) på dator eller mobil.





- Besök applikationens officiella webbplats: **[arkade.money](https://arkade.money)**.



![arkade homepage](assets/fr/01.webp)



Du kommer att mötas av en serie introduktionsskärmar som presenterar Arkades nyckelbegrepp: ett nytt ekosystem för Bitcoin, vikten av självförvaring och fördelarna med batch-transaktioner.



![arkade onboarding](assets/fr/02.webp)





- På Android (Chrome/Brave)** : Tryck på webbläsarens meny (tre prickar) och välj "Installera program" eller "Lägg till på startskärmen".
- På iOS (Safari)**: Tryck på delningsknappen (fyrkant med en pil uppåt) och välj "På startskärmen".



När Arkade har installerats startar det som ett inbyggt program, i helskärm och utan adressfält.



### Skapande av portfölj


Vid första lanseringen ombeds du att konfigurera din portfölj.





- Klicka på **"Skapa ny Wallet"**.



![create wallet](assets/fr/03.webp)





- wallet skapas omedelbart. Till skillnad från traditionella Bitcoin-plånböcker använder **Arkade inte en återställningsfras på 12 eller 24 ord**. Istället genererar Arkade automatiskt en **privat nyckel** i Nostr (nsec)-format, som kommer att användas för att säkerhetskopiera och återställa din wallet. Kom ihåg att spara denna nyckel omedelbart (se nästa avsnitt).





- Du kommer att se skärmen "Din nya wallet är live!", som bekräftar att din wallet är redo att användas. Klicka på **"GO TO WALLET"** för att komma till huvudgränssnittet.



När du är inne i din wallet kommer du till Arkades huvudgränssnitt. Här hittar du ditt saldo, knappar för att skicka och ta emot pengar och en flik "Apps" som ger tillgång till integrerade applikationer som Boltz (Lightning exchange), LendaSat och LendaSwap (utlåningstjänster) och Fuji Money (syntetiska tillgångar).



![wallet interface](assets/fr/04.webp)



### Anslutning till ASP


Som standard är portföljen automatiskt konfigurerad för att ansluta till den officiella Arkade Labs ASP. Du kan kontrollera vilken server du är ansluten till genom att gå till **Inställningar** > **Om** där du ser serveradressen (för närvarande `https://arkade.computer`).



I den nuvarande versionen av Arkade (Beta) är det inte möjligt att manuellt ändra ASP-servern. Programmet ansluter automatiskt till den officiella ASP:n för Arkade Labs. I framtiden kan användarna kanske välja mellan olika ASP:er enligt deras preferenser, men den här funktionen är ännu inte tillgänglig.



### Säkerhetskopiera din privata nyckel


**Arkade använder en privat nyckel i Nostr (nsec)-format som en metod för säkerhetskopiering och återställning. För att säkerhetskopiera din privata nyckel :





- Gå till **Settings** från huvudskärmen.
- Välj **"Säkerhetskopiering och sekretess"**.
- Du kommer att se din **privata nyckel** visas i `nsec...`-format. Denna långa teckensträng är ditt enda sätt att återställa din wallet.
- Tryck på **"COPY NSEC TO CLIPBOARD"** för att kopiera din privata nyckel.
- Förvara nyckeln på en säker plats**: skriv ner den på papper, förvara den i en säker lösenordshanterare eller använd någon annan säkerhetskopieringsmetod som passar dig.
- Arkade erbjuder också alternativet ** "Aktivera Nostr-säkerhetskopior" **. Den här funktionen använder Nostr-protokollet (ett decentraliserat nätverk) för att automatiskt säkerhetskopiera vissa data från din wallet i krypterad form till Nostr-reläer. Detta underlättar synkronisering mellan flera enheter och erbjuder enklare återställning av din wallet:s status.



**Viktigt**: Nostr-backuper är endast en **komfortfunktion**. De ersätter inte säkerhetskopian av din nsec-nyckel. Nostr reläer garanterar inte permanent datalagring. Din privata nsec-nyckel förblir ditt enda garanterade sätt att återfå dina pengar.



![backup private key](assets/fr/05.webp)




## Använda Arkade



När du har konfigurerat din wallet är du redo att utforska Arkades funktioner. Gränssnittet är utformat för att förenkla de olika typerna av Bitcoin-betalningar (On-chain, Lightning, Ark) sömlöst.



### Mottagande av medel



För att finansiera din portfölj, tryck på **"Receive"**. Arkade erbjuder tre metoder för mottagande:





- Betalning med Ark**: Om avsändaren också använder Arkade kan du dela din Ark-adress för en omedelbar, konfidentiell och praktiskt taget gratis överföring.
- Insättning på kedjan (ombordstigning)**: Använd Bitcoin-adressen (`bc1p...`) för att ta emot från en klassisk wallet eller en börs. Vänta på bekräftelse (~10 min) innan pengarna omvandlas till VTXO:er.
- Lightning swap**: Skapa en Lightning-faktura och betala den från en extern wallet Lightning. Pengarna kommer in direkt via en automatisk swap.



![receive amount](assets/fr/06.webp)



Kvittoskärmen visar alla tillgängliga alternativ: QR-kod, Ark-adress, Bitcoin (BIP21)-adress och Lightning-faktura. För Lightning-betalningar ska du hålla programmet öppet under transaktionen.



![receive confirmation](assets/fr/07.webp)



### Skicka pengar



För att skicka pengar, tryck på **"Skicka"** och klistra in mottagarens adress eller skanna QR-koden. Arkade känner automatiskt av vilken typ av betalning som krävs:





- Betalning med Ark**: Till en Ark-adress är överföringen omedelbar, privat och praktiskt taget gratis (0 SATS avgift). Mottagaren behöver inte vara online.
- Blixt** betalning: Skanna en Lightning-faktura (`lnbc...`) och Arkade gör automatiskt en swap. ASP:n betalar fakturan åt dig och debiterar ditt Arkade-saldo.
- Betalning i kedjan**: Mot en klassisk Bitcoin-adress (`bc1q...` eller `bc1p...`) initierar Arkade en "Collaborative Output" som kommer att ingå i nästa on-chain-runda.



Kontrollera detaljerna på skärmen "Sign transaction" och bekräfta sedan med **"TAP TO SIGN"**.



![send payment](assets/fr/08.webp)



**Aktuell begränsning (Beta)**: VTXO:er som skapats för mindre än 24 timmar sedan kan inte användas för on-chain-utgångar. Om du stöter på ett fel, vänligen vänta tills dina VTXO:er är "mogna".



**on-chain sekretess för utdata**: Exemplet nedan visar en [Ark-utdatatransaktion på mempool.space](https://mempool.space/fr/tx/153a70384d1c8a183c0e408e29b0a11820fd71a8bd5b4b00b12bc9b7f9decacb). Vi observerar en distribuerad inmatning till 4 olika utmatningar, som en CoinJoin. För en extern observatör är det omöjligt att avgöra vilken mängd som tillhör vilken användare.



![transaction ark mempool](assets/fr/11.webp)



## Avancerade funktioner



### Hantering av VTXO-expiration


En teknisk egenskap hos Ark-protokollet är att VTXO:er har en **begränsad livstid**. Denna tidsbegränsning är inbyggd i protokollets utformning. Utgångstiden kan konfigureras av varje ASP-server; på den officiella ASP:n för Arkade Labs är denna period cirka **4 veckor (≈30 dagar)**.



**Denna begränsning gör det möjligt för Ark-servern att effektivt hantera likviditeten och rensa upp VTXO:er från inaktiva användare. Efter utgången kan Ark-servern tekniskt sett göra anspråk på de återstående medlen i VTXO-trädet.



**För att hålla dina VTXO:er aktiva måste de "uppdateras" innan de löper ut. Uppdateringen består av att delta i en ny "runda" där dina VTXO:er som är nära att löpa ut byts ut mot nya VTXO:er med en ny full giltighetstid (≈30 dagar på Arkade Labs ASP).



Arkade-portföljen hanterar denna process automatiskt: applikationen övervakar ständigt statusen för dina VTXO:er och uppdaterar dem automatiskt några dagar innan de löper ut. Så länge du öppnar din applikation regelbundet (minst en gång i veckan) kommer dina VTXO:er automatiskt att hållas aktiva.



**Om du inte öppnar din portfölj på mer än 4 veckor kommer dina VTXO:er att förfalla. Du förlorar dock inte dina medel: du behåller möjligheten att återfå dem genom en **unilateral exit** (se nästa avsnitt). Detta förfarande är dyrare och långsammare, men det säkerställer att dina medel förblir återvinningsbara.



Behovet av att öppna applikationen regelbundet gör Arkade till en **"Hot Wallet"** designad för dagliga utgifter, inte ett säkert för långsiktiga besparingar. För att lagra bitcoins utan att använda dem under långa perioder, föredra en kall wallet-hårdvara.



**Kontrollera statusen för dina VTXO:er**: Du kan övervaka statusen för dina VTXO:er i **Inställningar** > **Avancerat**. Se "Nästa förnyelse" för att se när nästa automatiska förnyelse kommer att ske och "Virtuella mynt" för att se en detaljerad lista över alla dina VTXO:er med utgångsdatum.



![vtxo management](assets/fr/09.webp)



### Sortie Unilatérale (ensidigt utträde)



Unilateral exit är en **grundläggande kryptografisk garanti** i Ark-protokollet som säkerställer att du får tillbaka dina pengar, även om ASP:n försvinner, censurerar dina transaktioner eller vägrar att samarbeta. Tekniskt sett är dina VTXO:er **förhandssignerade Bitcoin-transaktioner** som du äger. I en absolut nödsituation kan du sända dessa transaktioner på Bitcoin-blockkedjan för att återfå dina medel utan någons tillstånd.



**Hur fungerar det? Processen sker i två steg. Först **Unrolling**: du sänder sekventiellt de för-signerade transaktionerna som utgör dina VTXO:er i transaktionsträdet. Sedan **Finalization**: när tidslåset har löpt ut (vanligtvis 24 timmar) samlar du in dina bitcoins från en standardadress.



**Nuvarande status i Arkade**: I Betaversionen finns det ännu ingen knapp eller enkelt användargränssnitt för ensidig utmatning. Denna funktionalitet kräver för närvarande användning av Arkade SDK och teknisk kunskap om TypeScript-programmering.



**Även om proceduren inte är tillgänglig med en knapptryckning finns den kryptografiska garantin där. Dina VTXO:er innehåller för-signerade transaktioner som legitimt tillhör dig. Det är denna tekniska garanti som gör Ark till ett **non-custodial** protokoll: även i värsta fall förblir dina medel tekniskt återvinningsbara. Ett förenklat gränssnitt kommer förmodligen att läggas till i framtida versioner av Arkade.



## Fördelar och begränsningar



För att sätta Arkade i rätt sammanhang, låt oss sammanfatta dess nuvarande styrkor och svagheter.



### Höjdpunkter




- Användarupplevelse (UX)**: Ingen kanalhantering, inkommande kapacitet eller komplexa säkerhetskopior av kanaler som med Lightning. Bara att installera och använda.
- Sekretess** : Standardarkitekturen CoinJoin erbjuder en mycket högre nivå av anonymitet än standard on-chain eller Lightning-transaktioner.
- Interoperabilitet**: Betala med alla Bitcoin QR-koder (On-chain eller Lightning) från ett enda gränssnitt.



### Begränsningar




- Ungt protokoll**: Arken är en mycket ny teknik. Buggar kan förekomma. Det är tillrådligt att inte använda Ark för att lagra summor vars förlust skulle vara kritisk.
- Beroende av ASP**: Även om systemet inte är frihetsberövande är det beroende av ASP:s tillgänglighet för att fungera smidigt. Om ASP:n är offline kan du inte längre göra omedelbara transaktioner (endast uttag av dina on-chain-medel).
- Endast Hot Wallet** : Behovet av att öppna applikationen regelbundet för att uppdatera VTXO:er är inte lämpligt för kylförvaring (Cold Storage).



## Jämförelse: Arkade vs Lightning vs Cashu



För att bättre förstå Arkades positionering, låt oss jämföra den med de andra två stora skalbarhetslösningarna.



| Critère | Arkade (Ark) | Lightning Network | Cashu (E-cash) |
| :--- | :--- | :--- | :--- |
| **Modèle** | UTXO partagé coordonné par serveur (ASP) | Réseau P2P de canaux de paiement | Jetons aveugles émis par une banque (Mint) |
| **Custodie** | **Non-custodial** (vous avez les clés) | **Non-custodial** (vous avez les clés) | **Custodial** (le Mint a les fonds) |
| **Confidentialité** | **Élevée** (CoinJoin natif, aveugle pour le public) | **Moyenne** (Routage en oignon, mais canaux visibles) | **Très Élevée** (Aveugle même pour le Mint) |
| **Scalabilité** | Excellente (Batching massif on-chain) | Excellente (Transactions infinies off-chain) | Excellente (Simples signatures serveur) |
| **Expérience** | Simple (proche d'un wallet on-chain) | Complexe (gestion de canaux, liquidité) | Très simple (comme du cash numérique) |
| **Risque principal** | Disponibilité de l'ASP & Expiration | Gestion des canaux & Backups | Confiance dans le Mint (risque de vol) |

**Arkade** är den perfekta kompromissen: enkelheten och sekretessen hos Cashu, men med suveräniteten (icke-frihetsberövande) hos Lightning.



## Stöd och hjälp



Om du stöter på några problem eller har några frågor när du använder Arkade, erbjuder programmet flera supportalternativ:





- Gå till **Inställningar** > **Support**.
- Du kommer att hitta flera alternativ:
  - Kundtjänst**: Få hjälp med din portfölj, rapportera buggar eller ställ frågor.
  - Säker chatt**: Dina konversationer är säkra och privata, och historiken bevaras mellan sessionerna.
  - Felrapporter**: Rapportera eventuella problem som du stöter på, inklusive åtgärder för att reproducera dem.
  - Spåra framsteg**: Håll hela tiden koll på dina supportärenden och konversationer.



![support](assets/fr/10.webp)



Arkade-teamet är också aktivt på Telegram via kanalen @arkade_os för support och integrationsmöjligheter.



## Viktig anmärkning: Applikation i Beta



**⚠️ Arkade är för närvarande i Public Beta på mainnet Bitcoin**. Även om applikationen är funktionell med riktiga bitcoins är det viktigt att vidta vissa försiktighetsåtgärder.



### Rekommendationer för användning




- Använd små mängder**: Undvik att lagra stora summor på Arkade. Använd denna wallet för dina dagliga utgifter och förvara dina besparingar på en kall wallet-hårdvara.
- Möjliga buggar och begränsningar**: Som med alla applikationer under aktiv utveckling kan Arkade innehålla buggar eller oväntat beteende. Rapportera eventuella problem via integrerad support.
- Snabb utveckling** : Applikationen och protokollet förbättras ständigt. Vissa funktioner kan komma att ändras eller läggas till i framtida versioner.



### Nuvarande kända begränsningar




- 24 timmars fördröjning på VTXO** : Nyskapade VTXO:er kan inte användas omedelbart för on-chain-utgångar.
- ASP unik**: Det är ännu inte möjligt att ändra ASP-servern i applikationen.
- Teknisk unilateral utmatning**: Inget förenklat gränssnitt för unilateral output ännu (kräver SDK).



Arkade Labs-teamet arbetar aktivt för att lätta på dessa begränsningar i framtida versioner.



## Slutsats



ArkadeOS representerar ett stort genombrott i Bitcoin:s ekosystem. Genom att implementera Ark-protokollet bevisar det att det är möjligt att förena enkel användning med de grundläggande principerna för Bitcoin: lita inte på, verifiera.



Även om Arkade fortfarande är i sin linda ger den en fascinerande inblick i hur framtidens Bitcoin-betalningar kan se ut: omedelbara, privata och tillgängliga för alla utan tekniska förutsättningar. Det är det perfekta verktyget för dina dagliga utgifter och kompletterar din säkra sparlösning (Cold Wallet).



Vi uppmuntrar dig att testa Arkade med små mängder för att själv upptäcka detta nya protokoll. Ekosystemet utvecklas snabbt och Arkade ligger i framkant av denna innovation.



## Resurser



För att få reda på mer, se de officiella resurserna:





- Arkade** webbplats: [arkadeos.com](https://arkadeos.com)
- Dokumentation**: [docs.arkadeos.com](https://docs.arkadeos.com)
- Ark** protokoll: [ark-protocol.org](https://ark-protocol.org)
- Källkod** : [GitHub Arkade](https://github.com/arkade-os)