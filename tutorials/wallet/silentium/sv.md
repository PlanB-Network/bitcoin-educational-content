---
name: Silentium
description: Progressiv webb wallet med stöd för tysta betalningar (BIP-352)
---

![cover](assets/cover.webp)



Återanvändning av Bitcoin-adresser är ett av de mest direkta hoten mot användarnas konfidentialitet. När en mottagare delar en enda adress för att ta emot flera betalningar kan alla observatörer spåra alla associerade transaktioner och rekonstruera deras ekonomiska historia. Detta problem påverkar särskilt innehållsskapare, välgörenhetsorganisationer eller aktivister som vill visa en donationsadress offentligt utan att äventyra sin integritet.



Silentium svarar på detta problem med en elegant lösning som är tillgänglig direkt från din webbläsare. Denna progressiva webbapplikation (PWA) med öppen källkod, som lanserades i maj 2024 av Louis Singer, implementerar Silent Payments (BIP-352): en återanvändbar statisk adress där varje betalning hamnar på en separat blockkedjeadress, utan föregående interaktion eller observerbar länk mellan transaktioner.



**Viktig varning**: Silentium är ett experimentellt projekt som fungerar som ett *konceptbevis* för Silent Payments lättviktsplånböcker. Det bör inte användas som en daglig wallet eller för att lagra betydande belopp. Utvecklarna säger uttryckligen:



> Använd på egen risk.

Observera att denna wallet kan användas som ett testnät eller regtest.



## Vad är Silentium?



### Filosofi och mål



Silentium fungerar som en teknisk demonstration för implementering av tysta betalningar i en lättviktig wallet-webbläsare. Även om den också stöder konventionella Bitcoin-adresser ligger tonvikten på Silent Payments för att göra det möjligt för användare att experimentera med denna integritetsteknik på ett enkelt sätt.



### Hur fungerar tysta betalningar?



Tysta betalningar (BIP-352) använder Elliptic Curve Diffie-Hellman-nyckeln Exchange (ECDH). Mottagaren genererar en statisk adress (`sp1...` på mainnet, `tsp1...` på testnet) som består av två publika nycklar: en scan-nyckel för att upptäcka betalningar och en spend-nyckel för att använda dem.



Avsändaren kombinerar sina privata inmatningsnycklar med mottagarens skanningnyckel för att beräkna en delad hemlighet som genererar en kryptografisk "tweak". Denna tweak, som läggs till utgiftsnyckeln, skapar en unik Taproot-adress för varje transaktion. Mottagaren reproducerar denna beräkning med sin privata skanningnyckel för att upptäcka och spendera pengarna utan någon föregående interaktion.



Fördelar: ökad sekretess för avsändare och mottagare, ingen tredjepartsserver krävs, transaktioner som inte går att skilja från konventionella Taproot-betalningar. Största nackdelen: intensiv skanning av blockkedjan för att upptäcka betalningar.



För att ta reda på mer om de teoretiska funktionerna i Silent Payments, se den sista delen av BTC,204-kursen på Plan ₿ Academy :



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Plattformar som stöds



Silentium är en Progressive Web App (PWA) som är tillgänglig från alla moderna webbläsare (mobil eller stationär). Använd den direkt på `app.silentium.dev`, installera den som en inbyggd applikation via din webbläsare eller distribuera den lokalt. Installationen görs direkt från webbläsaren, utan att gå via de officiella butikerna.



## Använda webbappen



### Tillträde och installation



[Gå till `https://app.silentium.dev/` från din webbläsare](https://app.silentium.dev/). Programmet laddas direkt och visar startskärmen.



Om du vill installera den som en inbyggd applikation på iOS trycker du på delningsknappen (fyrkant med pil uppåt) och väljer sedan "På hemskärmen". På Android erbjuder webbläsaren vanligtvis en "Lägg till på startskärmen"-avisering direkt. När Silentium har installerats visas det med en särskild ikon och fungerar som en inbyggd applikation, men kräver en internetanslutning för att synkronisera transaktioner.



![Installation de Silentium comme PWA sur iOS](assets/fr/01.webp)



### Skapande av portfölj



Vid första start väljer du "Create Wallet" för att skapa en ny portfölj eller "Restore Wallet" för att återställa från en befintlig återställningsfras.



Välj "Skapa Wallet". Programmet genererar en fras på 12 ord som du måste skriva ner noggrant. Denna fras är det enda sättet att återfå dina pengar. Även på testnätet ska du ha goda rutiner för säkerhetskopiering. Tryck på "Fortsätt" när du har sparat din fras.



Programmet ber dig sedan att ange ett lösenord för att säkra åtkomsten till wallet. Välj ett starkt lösenord och bekräfta det.



![Création d'un nouveau wallet avec phrase de récupération](assets/fr/02.webp)



När frasen har bekräftats och lösenordet har angetts kommer du till huvudgränssnittet.



### Interface huvud- och parametrar



Huvudgränssnittet visar ditt saldo i satoshis (inledningsvis 0 sats), med tre knappar längst ned:




- Sync**: synkroniserar wallet med blockkedjan
- Receive**: att ta emot medel
- Skicka**: för att skicka bitcoins



Gå till Inställningar via ikonen längst upp till höger (tre horisontella streck). Menyn Inställningar erbjuder flera alternativ:





- Om**: information om ansökan
- Backup**: säkerhetskopia av återställningsfras
- Explorer**: välj blockchain explorer (Mempool som standard) och Silentiumd-server
- Nätverk**: val av nätverk (mainnet/testnet)
- Lösenord**: ändra lösenord
- Reload**: omladdning av wallet
- Återställning**: fullständig återställning
- Tema**: ändra tema



![Interface principale et paramètres avec Explorer](assets/fr/03.webp)



Avsnittet **Explorer** är särskilt viktigt: det låter dig välja den blockchain explorer som används (Mempool som standard) och visar också webbadressen till Silentiumd-servern (`https://bitcoin.silentium.dev/v1` för mainnet). Om du är värd för din egen Silentiumd-server eller vill använda testnet är det här du konfigurerar dessa parametrar.



### Mottagande av medel



Från huvudgränssnittet trycker du på knappen "Receive". Som standard visar Silentium en Silent Payment-adress med dess QR-kod. Adressen börjar med `sp1...` på mainnet eller `tsp1...` på testnet.



Du kan växla mellan Silent Payment och klassiska Bitcoin-adresser med hjälp av knappen "Växla till klassisk adress" / "Växla till tyst adress" längst ner på skärmen.



![Réception de fonds avec Silent Payment et adresse classique](assets/fr/04.webp)




När transaktionen har skickats, vänligen vänta några minuter. För tysta betalningar skannar Silentium automatiskt blockkedjan efter transaktioner som är avsedda för dig. Transaktionerna visas med statusen "Obekräftad" innan de gradvis bekräftas.



### Skicka en betalning



Från huvudgränssnittet trycker du på knappen "Send". På skärmen för sändning får du frågan :



1. **Address**: klistra in en Silent Payment-adress (`sp1...` eller `tsp1...`) eller en klassisk Bitcoin-adress. Du kan använda QR-skanningsikonen för att skanna en adress.


2. **Belopp**: Ange det belopp i satoshis som ska skickas. En numerisk knappsats visas för enkel inmatning. Ditt tillgängliga saldo visas högst upp som referens.



![Envoi de fonds depuis Silentium](assets/fr/05.webp)



När du har angett adress och belopp trycker du på "Proceed" för att fortsätta. Programmet kommer att be dig att välja önskad avgiftsnivå innan du bekräftar transaktionen.



## wallet självhanterande



### Varför självhosta?



Silentiums lokala hosting erbjuder total suveränitet, kodverifiering, en utvecklingsmiljö och motståndskraft mot fel på den officiella webbplatsen.



### Förkunskapskrav



Node.js (version 14+), npm eller yarn, Git och cirka 500 MB diskutrymme.



### Lokal installation



Klona repository och installera :



```bash
git clone https://github.com/louisinger/silentium.git
cd silentium
yarn install
```



### Lansering och användning



Starta programmet i utvecklingsläge:



```bash
yarn start
```



Gå till `http://localhost:3000` i din webbläsare. För en optimerad produktionsversion :



```bash
yarn build
```



Filer som genereras i `build/` kan användas med nginx, Apache eller någon annan webbserver. Som standard ansluter Silentium till den offentliga servern `bitcoin.silentium.dev`. Ändra denna inställning i parametrarna för att använda testnet eller din egen server.



## Silentiumd-servern



### Roll och verksamhet



Silentium använder en **Silentiumd** indexeringsserver för att optimera betalningsdetektering. Att skanna alla Taproot-transaktioner skulle vara för besvärligt för en webbläsare eller mobiltelefon.



Silentiumd förberäknar mellanliggande data (tweaks) för varje Taproot-transaktion. Din wallet laddar ner dessa tweaks (några byte per transaktion) och utför den slutliga beräkningen lokalt, vilket verifierar äganderätten till betalningen. Servern känner aldrig till dina nycklar eller kan identifiera dina transaktioner, till skillnad från konventionella Electrum-servrar.



Kompakta BIP158-filter gör det möjligt för din wallet att avgöra vilka block som ska skannas utan att dina adresser avslöjas, vilket bevarar din sekretess.



### Publik server



Den offentliga servern `bitcoin.silentium.dev` (mainnet), sponsrad av Vulpem Ventures, erbjuder en enkel och omedelbar upplevelse. Även om konfidentialiteten bevaras innebär detta tillvägagångssätt ett relativt förtroende för tredje parts infrastruktur.



### Hosta din egen Silentiumd-server



För total suveränitet, hosta din egen Silentiumd-server. Förutsättningar: Bitcoin Core non-elagged nod med `txindex=1` och `blockfilterindex=1`, Go 1.21+, 10-20 GB diskutrymme, kunskaper i systemadministration.



**Installation:**



```bash
git clone https://github.com/louisinger/silentiumd.git
cd silentiumd
make build
./build/silentium-[OS]-[ARCH]
```



Konfigureras via miljövariabler (se förvarets `config.md` för detaljer). Servern indexerar blockkedjan och exponerar en API som kan efterfrågas av din wallet.



Det finns för närvarande inga paketerade lösningar för Umbrel eller Start9, vilket begränsar tillgängligheten för icke-tekniska användare.



## Fördelar och begränsningar



### Höjdpunkter





- Maximal tillgänglighet**: kan användas från vilken webbläsare som helst, ingen tung installation krävs
- Flera plattformar**: fungerar på mobiler (Android/iOS) och datorer tack vare PWA-teknik
- Enkel självhosting**: lokal installation möjlig med några få kommandon
- Öppen källkod**: fullt granskningsbar kod på GitHub
- Fokus på integritet**: ingen spårning, ingen analys, lokala kryptografiska beräkningar
- Separat arkitektur**: tydlig åtskillnad mellan wallet (klient) och indexeringsserver
- Utan konto**: ingen registrering eller personuppgifter krävs



### Begränsningar att ta hänsyn till





- Experimentellt projekt**: endast konceptbevis, inte avsett för daglig användning eller produktion
- Inga garantier**: risk för buggar, sårbarheter, eventuell förlust av medel
- Begränsat stöd**: lite användardokumentation, liten community, inget officiellt stöd
- Serverberoende**: kräver en fungerande Silentiumd-server (offentlig eller självhostad)
- Intensiv skanning**: Tyst betalningsdetektering förbrukar bandbredd
- Reducerad funktionalitet**: ingen myntkontroll, ingen Lightning, inga multi-signaturer



## Bästa praxis



### seed säkerhet



Även på testnet ska du ta din återställningsfras på allvar. Skriv ner den och förvara den på en säker plats. Ha separata plånböcker för testnet och mainnet: använd aldrig en test-seed på en wallet som är avsedd för riktiga pengar.



### Verifiering av källkod



En av fördelarna med självhosting är möjligheten att kontrollera källkoden innan den körs. Om du planerar att använda Silentium med riktiga pengar, ta dig tid att granska koden eller få en betrodd utvecklare att göra det. Jämför också hashen för koden som distribueras på `app.silentium.dev` med den i GitHub-arkivet för att säkerställa äkthet.



### Säkerhetskopiering och återställning



Återvinning av medel från tysta betalningar kräver en wallet som är kompatibel med BIP-352-protokollet. En standard wallet kan inte skanna blockkedjan för att hämta dina UTXO tysta betalningar. Ha Silentium installerat eller se till att du har tillgång till en annan kompatibel wallet (t.ex. Cake Wallet eller andra framtida implementeringar) för att återställa dina medel vid behov.



## Slutsats



Silentium erbjuder en tillgänglig testmiljö för att förstå Silent Payments utan teknisk friktion. Som ett bevis på koncept visar det hur denna sekretessteknik kan integreras i en wallet-webbläsare samtidigt som självförvaret bevaras. Experimentera på testnet för att upptäcka detta lovande genombrott för on-chain-sekretess.



## Resurser



### Officiell dokumentation




- Silentium GitHub-arkiv (wallet): https://github.com/louisinger/silentium
- Silentiumd GitHub-arkiv (server): https://github.com/louisinger/silentiumd
- Webbapplikation: https://app.silentium.dev/
- Silent Payments webbplats för allmänheten: https://silentpayments.xyz
- Specifikation BIP-352: https://bips.dev/352



### Artiklar och resurser




- Officiellt tillkännagivande (Twitter): https://x.com/TheSingerLouis/status/1790824126472667227
- NoBS Bitcoin: https://www.nobsbitcoin.com/silentium-silent-payments/
- Bitcoin Optech - Tysta betalningar: https://bitcoinops.org/en/topics/silent-payments/



### Testnet verktyg




- Testnet blandare: https://testnet-faucet.com/
- Mempool testnätutforskare: https://mempool.space/testnet