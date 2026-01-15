---
name: Bull Bitcoin Wallet
description: Ta reda på hur du använder Wallet Bull Bitcoin
---

![cover](assets/cover.webp)


![video](https://www.youtube.com/watch?v=6b0xTB2sE8E)


*Denna videohandledning från BTC Sessions går igenom processen för att konfigurera och använda Bull Bitcoin Wallet!


Den här guiden tar dig igenom installation, konfiguration och användning av Bull Bitcoin Wallet. Du får lära dig att skicka och ta emot pengar i Bitcoin:s On-Chain-, Liquid- och Lightning-nätverk, samt hur du flyttar Bitcoin mellan dem. wallet:s omfattande funktioner gör den till ett kraftfullt allt-i-ett-verktyg för att hantera din Bitcoin. Låt oss komma igång.


## Inledning


Bull Bitcoin Wallet, utvecklad av [Bull Bitcoin](https://www.bullbitcoin.com/), är en **self-custodial** Bitcoin wallet, vilket innebär att du har full kontroll över dina privata nycklar och därmed dina pengar, utan att vara beroende av en tredje part. Denna Wallet är öppen källkod och har sina rötter i en Cypherpunk-filosofi och kombinerar enkelhet, konfidentialitet och avancerade funktioner som swappar över nätverk och PayJoin-stöd. Det låter dig hantera dina bitcoins på tre nätverk: ** Bitcoin onchain**, ** Liquid** och ** Lightning**, var och en skräddarsydd för specifika användningsområden. På [BullBitcoin GitHub](https://github.com/orgs/SatoshiPortal/projects/49) kan du kolla in aktuella ämnen och kommande utvecklingar. Eftersom projektet är 100% öppen källkod och "byggt offentligt" kan du också skicka dina förslag och eventuella buggar du stöter på. Medan vissa plånböcker nu stöder flera nätverk, sticker Bull Bitcoin Wallet ut genom att djupt integrera integritetsfunktioner över dem alla, vilket gör det till ett kraftfullt verktyg för att hantera din Bitcoin över alla större nätverk


## 1️⃣ Förkunskapskrav


Innan du börjar använda **Bull Bitcoin Wallet** ska du se till att du har följande saker:



- Kompatibel smartphone**: En **iOS** (iPhone eller iPad) eller **Android** enhet
- Internetanslutning
- Säkra backup-media**: Skriv ner din **återställningsfras** (12 ord) på papper eller metall och förvara den på en säker plats.
- Grundläggande kunskaper**: En minimiförståelse för Bitcoin-koncept (adresser, transaktioner, avgifter) är användbar, även om denna handledning förklarar varje steg för nybörjare.


## 2️⃣ Installation


Du kan installera programmet via:



- [Apple App Store](https://apps.apple.com/app/bull-bitcoin/id6743380972)[ ](https://apps.apple.com/us/app/bitchat-mesh/id6748219622)(för iOS-enheter)
- [Google Play Store](https://play.google.com/store/apps/details?id=com.bullbitcoin.mobile&hl=en) (för Android-enheter)


Android-användare har också alternativa möjligheter:



- Ladda ner APK direkt från sidan [GitHub Releases](https://github.com/SatoshiPortal/bullbitcoin-mobile/releases) eller
- Installera via den Nostr-kompatibla [Zapstore](https://zapstore.dev/apps/naddr1qvzqqqr7pvpzq7xwd748yfjrsu5yuerm56fcn9tntmyv04w95etn0e23xrczvvraqqtxxmmd9e382mrvvf5hgcm0d9hzumt0vf5kcegnah0ap)


När du har installerat programmet ska du följa upp välkomstskärmen för att konfigurera ditt konto.


## 3️⃣ Initial konfiguration


Vid öppnandet uppmanas du att välja följande alternativ:



- "Skapa ny Wallet
- "Återta Wallet" och
- "Avancerade alternativ


Låt oss börja med att knacka på `Avancerade alternativ`.


Här kan vi konfigurera de avancerade inställningarna innan vi skapar eller återställer en wallet:


1. Aktivera `Tor proxy` för att dirigera trafik över Tor-nätverket.

1. [Orbot app](https://orbot.app/en/) måste installeras och köras innan du kan aktivera

2. Tor Proxy gäller endast för Bitcoin (inte Liquid) och kan resultera i en långsammare anslutning.

2. Installera en `Custom Electrum Server`, eller

3. Justera inställningarna för `Recover Bull`. Vi kommer att lära oss mer om [Recover Bull](https://recoverbull.com/) senare.


När du har gjort alla valfria justeringar trycker du på `Done`. Om du vill återanvända en befintlig Wallet klickar du på "Återanvänd Wallet" och fyller i de 12 orden i din återanvändningsfras.


Annars klickar du på `Create a New Wallet`.


![image](assets/en/01.webp)


## 4️⃣ Startskärm


Innan vi går djupare, låt oss ta en titt på "Hemskärmen" för att orientera oss:



- `transaktionsöversikten` och `inställningsmenyn` finns högst upp.
- I `Available Balance` finns ett sekretessalternativ som kan `aktiveras eller avaktiveras`.
- Gå in på `Bitcoin Bull Exchange` för att `köpa, sälja eller betala` (detta beror på jurisdiktion och kan kräva KYC).
- `Överföring` av pengar mellan plånböcker
- `Säkra Bitcoin` är lika med Onchain Bitcoin Wallet
- `Instant payments` via Lightning- / Liquid Network *(Obs: Bull Bitcoin Wallet gör det möjligt att göra och ta emot betalningar via Lightning. Medel som tas emot via Lightning lagras i [*Liquid-nätverket](https://liquid.net/) (i Wallet Instant Payments) tack vare en automatisk swap via [*Boltz exchange](https://boltz.exchange/). Detta ger dig möjlighet att interagera med Lightning utan att behöva hantera likviditetskanaler, samtidigt som du förblir i självförvar.)*
- "Sändande" och "mottagande" av medel


![image](assets/en/02.webp)


Låt oss först göra några viktiga konfigurationer och börja med `Backup`.


## 5️⃣ Backup


För att påbörja säkerhetskopieringen, tryck på "kugghjulsikonen (⚙)" i appens övre högra hörn och välj "Wallet Backup". Du kommer att presenteras med två metoder för att säkra din wallet: `Encrypted Vault` och `Physical Backup`. Låt oss utforska var och en av dem.


![image](assets/en/03.webp)


### Fysisk säkerhetskopiering


Tryck på `Physical Backup` för att se en lista med 12 ord som representerar din återhämtning eller seed fras. Vänligen överväg följande:



- Skriv ner din "återhämtningsfras" med största försiktighet. Skriv ner den på papper eller metall och förvara den på en säker plats (bankfack, offlineplats). Denna fras är ditt enda sätt att få tillgång till dina bitcoins om du förlorar din enhet eller raderar programmet.
- Det är också viktigt att notera att vem som helst med den här frasen kan stjäla alla dina bitcoins. Förvara dem aldrig digitalt:
- Ingen skärmdump
- Ingen säkerhetskopiering i molnet, via e-post eller meddelanden
- Ingen kopiera/klistra in (risk för att spara i urklipp)


![image](assets/en/25.webp)


På nästa skärm får du lägga in orden i rätt ordning för att se till att du har rätt seed-fras. Du kommer att få en bekräftelse när testet är klart och det är framgångsrikt.


! **Denna punkt är kritisk**. För ytterligare hjälp :


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.academy/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

### Krypterat valv


Det finns också möjlighet till en krypterad, anonym säkerhetskopiering i molnet. Men nämnde vi inte i sista stycket att säkerhetskopiering i molnet är riskabelt och bör undvikas? Bull Bitcoin-teamet har dock utvecklat ett smart sätt att göra processen säker. Så här fungerar det:


`Recoverbull` är ett säkerhetskopieringsprotokoll som förenklar säkringen av din Bitcoin wallet genom att dela upp säkerhetskopieringen i två delar. Först krypteras din wallet:s säkerhetskopieringsfil på din enhet med hjälp av en stark krypteringsnyckel. Du kan spara den här krypterade filen var du vill, till exempel på Google Drive eller på din enhet. För det andra lagras den krypteringsnyckel som behövs för att låsa upp filen av Recoverbull Key Server. För att återställa din wallet behöver du både den krypterade backup-filen och nyckeln, som du får tillgång till med din PIN-kod eller ditt lösenord. Denna design säkerställer att din molnbackup ensam är värdelös och att nyckelservern ensam är värdelös utan din specifika backupfil. Detta håller dina medel säkra även om en del äventyras.


Tänk på det som ett bankfack. Den krypterade backupfilen är *boxen*, som du kan lagra var som helst (som Google Drive). Din återställnings-PIN är *nyckeln*, som lagras separat av Recoverbull Key Server. En tjuv skulle behöva både din specifika låda och din specifika nyckel för att öppna den. Denna design säkerställer att även om någon får din säkerhetskopieringsfil, är den värdelös utan nyckeln från servern, och serverns nyckel är värdelös utan din unika säkerhetskopieringsfil.


Läs mer om `Recoverbull` wallet backup protokoll [här](https://recoverbull.com/).


Tryck på `Krypterat valv` och sedan `Fortsätt` för att bekräfta att du använder standardservern. Anslutningen kommer att dirigeras genom `Tor`-nätverket för att säkerställa integritet och anonymitet.


**Förstå dina PIN-koder**



- `App Unlock PIN`**:** Den valfria PIN-koden som anges i `Inställningar > Säkerhets-PIN` för att låsa appen på din telefon.
- `Recovery PIN`**:** Den obligatoriska PIN-koden som skapades under säkerhetskopieringen av `Encrypted Vault` och som används för att dekryptera din säkerhetskopierade fil under återställningen.


Dessa är två separata PIN-koder. Glöm inte din återställnings-PIN, eftersom den är nödvändig för att återställa din wallet."


**Återställning PIN-inställning: **



- Du måste skapa en PIN-kod eller ett lösenord för att få tillgång till din wallet.
- PIN-koden/lösenordet måste vara minst 6 siffror långt (undvik t.ex. enkla sekvenser som 123456, som inte accepteras).
- Utan denna PIN-kod är det omöjligt att återställa wallet.


Välj sedan en valvleverantör:



- `Google Drive` eller
- en "anpassad plats" (t.ex. din enhet)


![image](assets/en/04.webp)


Spara nu `backup-filen`. Tryck sedan på `Test Recovery`, välj din sparade säkerhetskopieringsfil eller valv och tryck sedan på `Decrypt Vault`. Ange ditt `PIN` eller `Lösenord`. Om allt fungerade visas skärmen `Testet slutfördes framgångsrikt`.


### Etiketter för import/export


Nu när vi har skapat vår Backup ska vi ta en titt på `Etiketter`.  Bull Bitcoin wallet förbättrar sekretess och organisation genom att låta användare skapa anpassade etiketter för sina mottagningsadresser och transaktioner. Dessa etiketter hjälper dig att kategorisera dina medel, eftersom transaktioner som skickas till en märkt adress kommer att ärva den etiketten, och du kan också märka utgående transaktioner för att spåra deras förändring. wallet har fullt stöd för standarden [BIP-329](https://bip329.org/), vilket innebär att du kan exportera alla dina etiketter till en fil och importera dem till en annan wallet. Den här funktionen säkerställer att du sömlöst kan säkerhetskopiera din transaktionshistorik och dina kategoriseringar, eller migrera dem mellan olika instanser av wallet, utan att förlora din personliga organisation.


![image](assets/en/05.webp)


## 6️⃣ Inställningar


Nu när din primära säkerhetskopia är säkrad kan vi utforska de andra funktionerna som finns i inställningarna.


### A - Säkerställa tillgång


För att säkra appen, navigera till `Inställningar` och välj `Säkerhets-PIN` för att välja PIN-kod. Skapa en stark PIN-kod för att låsa åtkomsten till din wallet. Även om detta steg är valfritt rekommenderas det starkt för att förhindra obehörig åtkomst om någon annan använder din telefon.


![image](assets/en/06.webp)


### B - Anslutning till en personlig nod (tillval)


Wallet BullBitcoin ansluter som standard till Electrum servrar: den första som hanteras av Bull Bitcoin och en sekundär server från Blockstream, som båda anses inte föra några loggar, vilket minskar risken för spårning.


För större sekretess kan du ansluta programmet till din egen Bitcoin-nod via en Electrum-server. För att göra det, tryck på `Inställningar` > `Bitcoin Inställningar` > `Electrum Server Inställningar`, tryck sedan på `+ Lägg till anpassad server` för att ange serverns adress och autentiseringsuppgifter.


![image](assets/en/07.webp)


### C - Valuta


Det tillgängliga saldot visas på huvudskärmen i både `sats` och `USD`. För att ändra detta, navigera till `Inställningar` > `Valuta`. Där kan du växla mellan `sats/BTC` och välja din `standard fiat-valuta`.


![image](assets/en/08.webp)


### D - Bitcoin Inställningar


Menyn `Bitcoin Settings` erbjuder djup åtkomst till din wallet:s kärnkonfigurationer och data. Här kan du inspektera de grundläggande detaljerna i dina `Secure Bitcoin` och `Instant payments wallets`, vilket ger dig full transparens och kontroll. Viktiga funktioner inom denna meny inkluderar:



- Wallet Detaljer:** Navigera till din säkra Bitcoin eller direktbetalning wallet för att se specifik information.
- Wallet Fingerprint:** En unik identifierare för din wallet.
- Public Key (Pubkey):** Den nyckel som används för att generate:a dina Bitcoin-mottagaradresser.
- Descriptor:** En teknisk sammanfattning av din wallet:s struktur.
- Derivation Path:** Den specifika sökväg som används för att generate alla adresser från din privata huvudnyckel.
- Address View:** Få tillgång till en lista över dina oanvända mottagningsadresser och ändra adresser (kommer snart)


Dessutom har du möjlighet att:



- `Enable Auto Transfer` inställningar för att ställa in ett maximalt omedelbart wallet-saldo, som sedan automatiskt kommer att överföras till den säkra bitcoin wallet.
- Importera generiska plånböcker via `Mnemonic` fras eller importera `watch-only`
- Anslut `Hårdvaruplånböcker`: enheter som för närvarande stöds är ColdcardQ, SeedSigner, Specter, Krux, Blockstream Jade och Foundation Passport


## 7️⃣ Bull Bitcoin Exchange


Direkt från wallet har du tillgång till [Bull Bitcoin exchange](https://www.bullbitcoin.com/), vilket gör att du kan köpa, sälja och betala Bitcoin utan att lämna appen. Denna integration ger en bekväm lösning för att hantera dina Bitcoin-behov. Observera att åtkomst till börsen och dess tjänster kan vara begränsad baserat på din jurisdiktion, och att det kan krävas att du slutför en kundkännedomskontroll (KYC) för att följa regleringsstandarder och använda plattformens alla funktioner.


För att komma igång, tryck på `Exchange` i det nedre högra hörnet, sedan `Sign up` eller `Login` till ditt konto.


Börsen erbjuder följande [funktioner](https://www.bullbitcoin.com/):



- Köp Bitcoin med självförvaring från ditt bankkonto
- Ej frihetsberövande
- Enskilda personer eller företag
- Omedelbart uttag
- Inga dolda avgifter
- Lightning Network tillgänglig
- Inga transaktionsgränser
- Återkommande köpoptioner


![image](assets/en/09.webp)


För att lära dig mer, besök denna handledning:


https://planb.academy/en/tutorials/exchange/centralized/bull-bitcoin-europe-0ccf713e-efcd-44ec-8205-211f49ac7d53

## 8️⃣ Mottagande av medel


Att ta emot pengar med **Bull Bitcoin Wallet** är enkelt och flexibelt och stöder tre olika nätverk som är skräddarsydda för olika användningsområden:



- Nätverket `Bitcoin (onchain)` för säker, långsiktig lagring.
- Nätverket `Liquid` för snabbare och mer konfidentiella transaktioner.
- Nätverket `Lightning` för omedelbara betalningar till låg kostnad.


Appen genererar automatiskt rätt adress eller faktura baserat på det nätverk du har valt. Så här går du tillväga för varje nätverk.


### Mottagning via Onchain (Bitcoin-nätverk)


För att ta emot on-chain-medel kan du antingen välja `Secure Bitcoin Wallet` från startskärmen och trycka på `Receive`, eller trycka på huvudknappen `Receive` och sedan välja `Bitcoin network`.


Du har två primära sätt att generera en mottagningsadress:


**Default Mode (URI med ytterligare inmatningsparametrar)


Som standard genererar wallet en [BIP21 URI](https://bips.dev/21/). Detta är ett standardiserat format som innehåller mer information än en enkel adress, inklusive ett belopp, en personlig anteckning och PayJoin-parametrar för att förbättra integriteten. Denna omfattande URI kodas till en QR-kod och görs tillgänglig för kopiering. Formatet ser ut så här: `bitcoin:<adress>?<parameter1>=<värde1>&<parameter2>=<värde2>`.



- Ytterligare inmatningsparametrar:**
    - Belopp:** Ange ett begärt belopp i BTC, sats eller en fiatvaluta.
    - Meddelande:** Lägg till en personlig anteckning som är synlig för avsändaren.
    - PayJoin:** Aktivera det här alternativet för att förbättra integriteten genom att kombinera uppgifter från både avsändaren och mottagaren i transaktionen.


Exempel på URI:


```
bitcoin:bc1q0vv86t2sj7daduvdc50njms6u6jzh2y54xxxxx?amount=0.0005&message=Tip+for+tutorial&pj=HTTPS%3A%2F%2FPAYJO.IN%2F78UH9WZUP8KKJ%23RK1Q2H30FASCU9WW09DQY2LK0K8P2DPRJ99V72CA78ACQAEL675QYTMQ+OH1QYP87E2AVMDKXDTU6R25WCPQ5ZUF02XHNPA65JMD8ZA2W4YRQN6UUWG+EX1L0LYV6G
```


*Viktig anmärkning: Skicka inga pengar till adresserna i denna handledning, wallet kommer att raderas.*


![image](assets/en/10.webp)


**Endast alternativet Kopiera eller skanna Address aktiverat


Med alternativet `Kopiera eller skanna endast Address` aktiverat genererar programmet en enkel Bitcoin-adress i SegWit-format (bech32).


Exempel:


```javascript
bc1q0vv86t2sj7daduvdc50njms6u6jzh2y54x3g56
```


Även om du anger ett belopp eller en anteckning kommer de inte att inkluderas i QR-koden eller den kopierade adressen.


![image](assets/en/11.webp)


### Mottagning via Liquid Network


Du kan ta emot en betalning på Liquid Network. När du är på skärmen "Ta emot" har du samma två alternativ för att skapa en betalningsbegäran:


**1. Enkel Address:** Kopiera den vanliga `Liquid-adressen`. Detta är en unik identifierare för din wallet i Liquid-nätverket och innehåller inte något specifikt belopp eller meddelande.


Exempel Address:


```javascript
lq1qq05k3vmnvbullbitcoinjujn6h04z9jtw53xuyktqf9mam2zpfz05j2fe2x8xhejgkga3nvmp4yyp35qynkcw2xqmy7xxxxxxx
```


**2. Detaljerad betalningsbegäran (URI):** För en mer strukturerad begäran kan du ange ett belopp och en personlig anteckning. Denna information kodas automatiskt till en delbar URI och dess motsvarande QR-kod.



- Belopp:** Du kan ange beloppet i Bitcoin (BTC), Satoshis (Sats) eller en fiatvaluta.
- Obs:** Lägg till ett personligt meddelande för att identifiera transaktionen.


**Exempel på URI:**


```javascript
liquidnetwork:lq1qqdhgs7w537nun55a5sdy4gxkd08pclk3d7v4qz36sy4xp0cq6gvl52fcfv7kdgkgzmfycrud0zsygqgyjclycckpasxxxxxx?amount=0.00001&message=Test&assetid=6f0279e9ed041c3d710a9f57d0c02928416460c4b722ae3457a11eec381c526d
```


För att slutföra transaktionen måste du förse avsändaren med "adress" eller "URL". Du kan göra detta genom att kopiera den till ditt urklipp eller genom att låta dem skanna QR-koden direkt från din skärm.


![image](assets/en/12.webp)


### Mottagning via blixtnedslag



Med Bull Bitcoin Wallet kan du också skicka och ta emot betalningar via Lightning Network. En viktig funktion är att medel som tas emot via Lightning automatiskt byts ut och lagras på `Liquid Network` inom dina `Instant Payments Wallet`. Denna tjänst drivs av `Boltz`. Denna design gör att du kan njuta av hastigheten och den låga kostnaden för Lightning utan komplexiteten i att hantera likviditetskanaler, samtidigt som du behåller full självförvaring av dina medel. Även om denna hybridmetod är självförvaltande och undviker komplexiteten med att hantera kanaler, introducerar den en tredjepartstjänst (Boltz), en liten swapavgift och förlitar sig på Liquid Network:s federation av funktionärer som nyckelinnehavare, vilket skiljer sig från en traditionell, icke-förvaltande Lightning wallet där du hanterar dina egna kanaler. Du kan lära dig mer om Liquid och dess styrmodell här:


https://planb.academy/en/courses/e17ee350-41d4-49fa-b270-29e4d26d22f8/overview-of-liquid-architecture-and-governance-model-17650c4b-cd1f-4bc6-b490-708f92dc9306


- Gränser:**
    - Minimibelopp:** Ett minimibelopp krävs för fakturan. Kontrollera appen för aktuell gräns
    - Avgifter:** Du, mottagaren, är ansvarig för en liten swapavgift. Denna avgift dras av från det belopp som avsändaren överför och kan komma att ändras
- Förmåner:**
    - Självförvaltande:** Dina pengar är alltid under din kontroll, säkrade i Liquid-nätverket.
    - Undvik höga On-Chain-avgifter:** Genom att använda Lightning och lagra på Liquid kringgår du on-chain-avgifterna som är förknippade med att öppna en traditionell Lightning-kanal. Du kan välja att flytta pengar till en on-chain-kanal senare, när det ackumulerade beloppet motiverar kostnaden.
    - Tips:** För den mest kostnadseffektiva transaktionen mellan två Bull Bitcoin-användare, använd **Liquid-nätverket direkt** för att helt undvika Lightning swap-avgifter.


För att få en betalning måste du generate en `Lightning faktura`:


1. "Ange ett belopp":** Ange det belopp du vill få i Bitcoin (BTC), Satoshis (Sats) eller en fiatvaluta.

2. lägg till en anteckning **(Valfritt):** Skriv ett memo eller en anteckning. Denna kommer att bäddas in i fakturan och visas i din transaktionshistorik när betalningen är klar, vilket gör det lättare att identifiera den.

3. `Invoice Giltighet`**:** Blixtfakturan är tidskänslig och förfaller efter **12 timmar**. Om den inte betalas inom denna period blir den ogiltig och du måste generate en ny.


Ge avsändaren fakturan genom att kopiera den till ditt urklipp eller genom att låta dem skanna QR-koden som visas på din skärm.


![image](assets/en/13.webp)


## 9️⃣ Sändning av medel


Du kan komma åt sändningsskärmen direkt från startsidan eller från någon av dina plånböcker. Bull Bitcoin Wallet förenklar processen genom att automatiskt upptäcka destinationsnätverket - `Bitcoin`, `Liquid` eller `Lightning` - baserat på adressen eller fakturan du anger, oavsett om den klistras in eller skannas via QR-kod.


### On-Chain Överföring via Bitcoin-nätverket


Att skicka pengar on-chain innebär att din transaktion registreras direkt på Bitcoin-blockkedjan. Den här metoden är bäst för större överföringar eller överföringar som inte är tidskänsliga. För att börja kan du trycka på `Sänd-knappen` nere till höger och skanna eller ange en `standard Bitcoin-adress`.


Om den adress du anger inte innehåller ett specifikt belopp kommer du att uppmanas att fylla i detaljerna på sändningsskärmen. Du kan ange beloppet i den enhet du föredrar, t.ex. BTC, satoshis eller en fiatekvivalent. Du har också möjlighet att lägga till en personlig anteckning, vilket är ett privat memo för din egen referens som hjälper dig att identifiera transaktionen senare. Den här anteckningen delas inte med mottagaren.


Om betalningsbegäran som du skannar eller klistrar in redan innehåller alla nödvändiga detaljer, t.ex. en BIP21 URI med ett fördefinierat belopp, kommer wallet att kringgå skärmen för datainmatning och ta dig direkt till bekräftelseskärmen för att godkänna betalningen.


![image](assets/en/14.webp)


Innan din transaktion sänds kommer du att få se en bekräftelseskärm. Det är viktigt att du tar en stund och noggrant granskar varje parameter, med särskild uppmärksamhet på mottagaradressen, det belopp som skickas och nätverksavgifterna. På den här skärmen finns också kraftfulla verktyg för att anpassa din transaktion.


Du kan styra avgifterna på två olika sätt. Den första metoden är att välja önskad transaktionshastighet, t.ex. låg, medel eller hög, och wallet beräknar automatiskt lämplig avgift åt dig. Den andra metoden ger mer exakt kontroll genom att låta dig ställa in en specifik avgift, antingen som en absolut summa i satoshis eller som en relativ avgift per byte, som sedan ger en beräknad bekräftelsetid.


För avancerade användare erbjuder wallet flera inställningar för att finjustera transaktionen. "Replace-by-Fee" (RBF) är aktiverat som standard, vilket är en värdefull funktion som gör att du kan påskynda en transaktion om den fastnar i mempoolen genom att sända den på nytt med en högre avgift. Du kan också manuellt välja vilka UTXO:er (Unspent Transaction Outputs) som ska användas. Detta är ett kraftfullt verktyg för UTXO-konsolidering, en strategi där du kombinerar flera små inmatningar till en enda större. Även om detta kan kosta mer i avgifter för den aktuella transaktionen, kan det avsevärt minska avgifterna för framtida transaktioner, särskilt om nätverksavgifterna förväntas stiga.


![image](assets/en/15.webp)


PayJoin aktiveras automatiskt när du skannar en mottagares betalningsbegäran (en BIP21 URI) som innehåller en `pj=` parameter. Om du bara klistrar in en vanlig adress utan extra parametrar aktiveras inte den här funktionen. Denna samarbetsmetod förbättrar integriteten genom att kombinera indata från både avsändaren och mottagaren, vilket bryter heuristiken med gemensamt ägande av indata och möjliggör bättre skalning och avgiftsbesparingar under vissa omständigheter.


### Sändning till Liquid Network


Liquid Network är utformad för snabba, konfidentiella transaktioner med minimala avgifter. När du skickar pengar via Liquid tas de ut från din `Instant Payments Wallet`. Processen är enkel: du anger eller skannar helt enkelt mottagarens `Liquid-adress`.


Om adressen inte anger något belopp kommer du att bli ombedd att ange ett på sändningsskärmen. Du kan ange beloppet i BTC, satoshis eller fiat. En viktig fördel med Liquid är dess låga minimitröskel. Precis som med on-chain-transaktioner kan du lägga till en valfri personlig anteckning för dina egna register. Om betalningsbegäran redan innehåller ett belopp kommer wallet att gå direkt till bekräftelseskärmen.


På bekräftelseskärmen för en Liquid-transaktion kommer du att granska detaljerna. Avgifterna är anmärkningsvärt låga och beräknas utifrån hur komplicerad transaktionen är. De är vanligtvis cirka 0,1 sat/vB, vilket för en enkel transaktion uppgår till bara 20-40 satoshis (till exempel 26 satoshis per den 21 december 2025).


![image](assets/en/16.webp)


### Sändning till Lightning Network


Du kan antingen skanna en Lightning Address (t.ex. `runningbitcoin@rizful.com`) där du kan ange beloppet och en valfri anteckning för mottagaren, eller skanna en faktura med ett fördefinierat belopp, vilket tar dig direkt till bekräftelseskärmen.


*Observera att minimibelopp och avgifter tillkommer*


Bull Bitcoin Wallet skickar Lightning-betalningar genom att ta ut pengar från din `Instant Payments Wallet` (på Liquid) och byta dem via `Boltz`. Denna hybridmetod är helt självförvaltande och undviker de höga on-chain-avgifterna för att hantera en dedikerad Lightning-kanal, men det kräver att man betalar en "swap-avgift". För den lägsta kostnaden, skicka direkt till en mottagares Liquid-adress om de också använder en Bull Bitcoin wallet.


## 🔟 Överföring av pengar mellan dina plånböcker


Bull Bitcoin låter dig flytta din Bitcoin mellan din `Secure Bitcoin` wallet och din `Instant Payments Wallet` på Liquid Network eller till en `extern Wallet`. För att utföra en överföring navigerar du helt enkelt till avsnittet "Överföring", väljer käll- och målplånböckerna, anger beloppet du vill flytta och bekräftar transaktionen.


![image](assets/en/17.webp)


## 1️⃣1️⃣ Återställning av din Bull Bitcoin Wallet


I detta avsnitt förklaras hur du återfår tillgång till dina Bull Bitcoin Wallet-medel om du förlorar din enhet, avinstallerar appen eller helt enkelt behöver byta till en ny. Som redan förklarats finns det två primära metoder för återhämtning: att använda den unika `Recoverbull`-metoden och att använda en standard `BIP39 seed-fras`.


### Metod 1: Recoverbull


Sammanställning: Wallet säkerhetskopior krypteras lokalt. Den krypterade filen kan lagras i molnlagring eller på en annan enhet. Krypteringsnyckeln lagras av Recoverbull Key Server. Båda hålls åtskilda och måste kombineras för att återställa en wallet.


För att börja kommer jag att radera Wallet med alla medel på den och installera om wallet. Vi kommer att landa på `Välkomstskärmen` igen. Den här gången väljer du alternativet `Recover Wallet`. Navigera sedan till metoden `Encrypted Vault`, bekräfta att du använder `Default Key server` och välj den plats eller `Vault provider` där du lagrade säkerhetskopian.


![image](assets/en/18.webp)


Det står att valvet har importerats framgångsrikt. Tryck på `Decrypt Vault` -knappen och ange `PIN`. Nästa skärm visar dina `balanser` och `antalet transaktioner` som återställdes.


![image](assets/en/19.webp)


### Metod 2: Seed-fras


Den här metoden använder din wallet:s huvudåterställningsfras, en standardlista med 12 ord som fungerar som den ultimata säkerhetskopian för dina medel. Det är det mest universella sättet att återställa en Bitcoin wallet, eftersom det inte är knutet till någon specifik tjänst eller server. Så länge du har den här frasen kan du återställa din wallet på vilken kompatibel enhet som helst, även utan tillgång till Bull Bitcoin Key Server.


Från välkomstskärmen väljer du `Recover Wallet`. Den här gången väljer du metoden `Fysisk backup`. Appen kommer att presentera ett rutnät med ord. Välj noggrant varje ord i din 12-ords seed-fras i rätt ordning. Var noggrann, eftersom ett enda misstag kommer att resultera i en felaktig wallet.


## 1️⃣2️⃣ Ansluta en Hardware Wallet


För högsta säkerhetsnivå väljer många Bitcoin-användare att lagra sina medel i "kall förvaring". Detta innebär att du förvarar de "privata nycklar" som styr din Bitcoin på en enhet som aldrig är ansluten till internet. En "hårdvaru-wallet" (eller signeringsenhet) är en specialiserad fysisk enhet som är utformad för just detta ändamål. Den fungerar som ett digitalt valv för dina nycklar och säkerställer att de aldrig utsätts för de potentiella hoten från en online-dator eller smartphone.


Genom att ansluta en hårdvaru-wallet till Bull Bitcoin-appen får du det bästa av två världar: den kompromisslösa säkerheten med kall lagring för dina privata nycklar, kombinerat med de kraftfulla funktionerna och det användarvänliga gränssnittet i Bull Bitcoin wallet för att visa saldon och hantera transaktioner. I det här sista kapitlet visar vi hur du ansluter en hårdvaru-wallet, t.ex. ett [Coldcard Q](https://coldcard.com/q), till din Bull Bitcoin wallet. Den här handledningen kommer inte att gå på djupet med att konfigurera ett Coldcard Q; du kan läsa mer om det här:


https://planb.academy/en/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3

https://planb.academy/en/tutorials/wallet/hardware/coldcard-q-advanced-b8cc3f29-eea9-48fe-a953-b003d5b115e0

### Importera en Wallet


![image](assets/en/26.webp)


Först, från huvudmenyn på ditt Coldcard Q, välj `Export Wallet`, välj sedan `Bull Wallet`. Ditt Coldcard kommer att generate en QR-kod.


![image](assets/en/20.webp)


Öppna Bull Bitcoin Wallet och navigera till `Inställningar` > `Bitcoin Inställningar` > `Importera wallet` och välj `Kortkort Q` på din telefon och tryck på `Öppna kameran` för att skanna denna QR-kod för att importera din hårdvara wallet:s publika nycklar.


![image](assets/en/21.webp)


### Mottagning med Coldcard Q


För att ta emot Bitcoin med ditt anslutna Coldcard Q behöver du inte ha enheten fysiskt ansluten till din telefon. Bull Bitcoin Wallet har redan importerat de nödvändiga publika nycklarna, vilket gör att den kan generate-adresser på egen hand.


1. Tryck på din importerade Coldcard Q-signeringsenhet och välj `Receive`.

2. Appen kommer automatiskt att visa en ny Bitcoin-adress från ditt Coldcards wallet.

3. Använd denna adress för att ta emot pengar. Bitcoin kommer att säkras direkt till hårdvaran wallet:s nycklar, även om enheten var offline under processen.


![image](assets/en/22.webp)


### Skicka med Coldcard Q


När du skickar Bitcoin med ditt Coldcard Q krävs din fysiska bekräftelse för att godkänna en transaktion. Medan Bull Wallet-appen används för att skapa transaktionen, kan den slutliga signaturen endast skapas på själva hårdvaran wallet.


För att börja, öppna ditt `Coldcard Q` wallet och tryck på `Send`. Öppna sedan kameran för att skanna QR-koden för mottagaradressen. Efter skanning anger du det "belopp" du vill skicka och justerar "avgiftsprioriteten" efter behov.


Om du vill ha fler alternativ kan du titta under Avancerade inställningar. Här hittar du alternativet `Replace by Fee` (RBF), som är aktiverat som standard och gör att du kan påskynda en fastnad transaktion senare. Du har också alternativet `Coin Control`, som låter dig manuellt välja de specifika UTXO som du vill spendera.


När du har granskat alla detaljer trycker du på `Visa PSBT` för att förbereda transaktionen.


![image](assets/en/23.webp)


Tryck på `Scan`-knappen på ditt Coldcard Q och använd kameran för att skanna QR-koden som visas på din telefon. På Coldcard-skärmen visas sedan alla transaktionsuppgifter. Kontrollera noggrant beloppet, mottagarens adress och din ändringsadress. Om allt är korrekt trycker du på "Enter"-knappen på Coldcard Q för att signera transaktionen. Därefter visas en QR-kod för den signerade transaktionen på skärmen.


![image](assets/en/24.webp)


På Bull wallet trycker du på "Jag är klar" och sedan på "Kamera"-knappen för att skanna QR-koden för den "signerade transaktionen" från ditt Coldcard Q. Bull Wallet visar nu en sammanfattningsskärm för den signerade transaktionen. Granska den en sista gång och tryck sedan på `Broadcast` Transaction. Detta slutför processen genom att skicka transaktionen till Bitcoin-nätverket, och dina pengar kommer att vara på väg.


## 🎯 Slutsats


Du har nu slutfört din resa genom Bull Bitcoin Wallet. Appen ger dig kraftfulla integritets- och säkerhetsverktyg direkt till hands och gör avancerade funktioner enkla att använda. Den hjälper dig att hålla dig privat med funktioner som `PayJoin`, som döljer dina transaktioner på blockkedjan, och `Tor integration`, som maskerar din nätverksaktivitet från nyfikna ögon. För dem som vill ha ultimat kontroll kan du ansluta till din "egen personliga Bitcoin-nod" för att sluta förlita dig på tredjepartsservrar och använda en "hårdvaru-wallet" för att hålla dina privata nycklar helt offline och säkra. Med smarta alternativ för säkerhetskopiering och sömlöst stöd för Bitcoin, Liquid och Lightning är Bull Bitcoin Wallet ett starkt allt-i-ett-val för alla som menar allvar med att hålla sina pengar privata, säkra och helt under egen kontroll.


## 📚 Bull Wallet Resurser


[Github](https://github.com/SatoshiPortal/bullbitcoin-mobile) | [Hemsida ](https://www.bullbitcoin.com/)| [Recoverbull](https://recoverbull.com/)