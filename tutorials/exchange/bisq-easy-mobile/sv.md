---
name: Bisq Easy Mobile
description: Ett peer-to-peer-handelsprotokoll för nya bitcoinanvändare - inga mellanhänder, ingen KYC.
---
![cover](assets/cover.webp)


## Inledning


Handelsprotokollet [Bisq Easy] (https://bisq.network/bisq-easy/) är utformat för [Bisq 2] (https://github.com/bisq-network/bisq2), efterföljaren till [Bisq v1] (https://github.com/bisq-network/bisq). Bisq 2 kommer att stödja flera handelsprotokoll, sekretessnätverk och identiteter. Det underlättar köp av Bitcoin med noll handelsavgifter och inget krav på deposition. Den är avsedd för nya Bitcoin-köpare som söker ett icke-KYCalternativ och som vill bli effektivt ombordtagna av erfarna och kunniga säljare som är bekanta med Bisq-plattformen.


För närvarande är Bisq Easy det enda handelsprotokollet för Bisq 2. Fler handelsprotokoll planeras för framtiden. Lär dig mer om Bisq 2 i den här handledningen:


https://planb.academy/tutorials/exchange/peer-to-peer/bisq-v2-c1c6a702-6c16-4101-8b90-62c424017b80

Denna korta guide är ett komplement till handledningen ovan om att köpa Bitcoin med hjälp av applikationen [Bisq Easy Mobile] (https://github.com/bisq-network/bisq-mobile) och Lightning.


## 1️⃣ Komma igång


Till att börja med, ladda ner Bisq Easy Mobile från [nedladdningssidan] (https://bisq.network/downloads/). Vi rekommenderar att du verifierar nedladdningen. Verifieringsinstruktioner finns också på [nedladdningssidan] (https://bisq.network/downloads/). Efter installationen måste du acceptera "användaravtalet". Skapa sedan en offentlig profil som består av ett "smeknamn" och en avatar (representerad av en "bot-ikon"). Med Bisq Easy kan du också skapa flera användarprofiler inom en klient. Efter en kort initialisering kommer du till "startskärmen". Appen lyfter fram utbildningsmaterial direkt på huvudsidan. Tryck på `Öppna Trade Guide` för att bekanta dig med den senaste informationen.


![image](assets/en/01.webp)


Handelsguiden förklarar allt relevant i enkla steg:



- Hur man handlar på Bisq Easy
- Hur fungerar handelsprocessen?
- Vad behöver jag veta om handelsregler.


Ett annat viktigt avsnitt är **"Hur säkert är det att handla på Bisq Easy?"**


![image](assets/en/08.webp)


Kryssa i rutan "Jag har läst och förstått" och tryck på "Avsluta".


![image](assets/en/02.webp)


## 2️⃣ Säkerhetskopiera dina data


Innan vi börjar, låt oss ta hand om några hushållsuppgifter och skapa en "säkerhetskopia" av din datalagringsfil. Gå till `More` > `Backup & Restore` för att spara din profil och handelshistorik. Om du förlorar din enhet utan en säkerhetskopia kan ditt rykte och dina pågående affärer inte återställas. Ange ett "Lösenord" för att kryptera din säkerhetskopia.


![image](assets/en/11.webp)


## 3️⃣ Erbjudanden


Från hemskärmen finns det två sätt att navigera till erbjudandena. Tryck på "Utforska erbjudanden" i mitten av skärmen eller tryck på "Erbjudanden" i menyn längst ner. Därifrån väljer du den `valuta` du vill handla med.


![image](assets/en/03.webp)


Till skillnad från [Bisq 1] (https://planb.academy/en/tutorials/exchange/peer-to-peer/bisq-fe244bfa-dcc4-4522-8ec7-92223373ed04), som kräver säkerhet, förlitar sig Bisq Easy enbart på säljarens rykte som säkerhet. Även om detta tillvägagångssätt gör det möjligt för köpare att köpa Bitcoin för första gången utan tidigare ägande, sätter det en hög grad av förtroende för säljarens förmåga att leverera Bitcoin efter att ha mottagit fiat-betalningar. Därför är Bisq Easy-säkerhetsmodellen endast optimerad för små handelsbelopp och affärer är begränsade till motsvarande 600 USD per transaktion för att minimera risken. I avsnittet "Offertbok" väljer du filter för betalningsmetoder och avveckling i Lightning eller Bitcoin (on-chain).


![image](assets/en/04.webp)


Efter att ha tillämpat `filter`, välj ett lämpligt erbjudande från en ansedd handelspartner. Säljarens förvalda betalningsmetod och avvecklingstyp (`Lightning` eller `on-chain`) visas. Kontrollera att dessa stämmer överens med dina preferenser innan du fortsätter. Vi väljer alternativet Lightning ⚡ här.


![image](assets/en/05.webp)


Granska och bekräfta handelsinformationen genom att trycka på "Bekräfta erbjudandet". Då visas en popup-skärm som bekräftar att du har tagit erbjudandet. Tryck på Visa handel i `Öppna affärer`. I avsnittet Öppna affärer klistrar du in din `Lightning-faktura` och trycker på `Skicka till säljaren` för att dela den. Vänta nu på säljarens uppgifter om betalkonto. Säljare kan ta tid på sig att svara. Kom tillbaka med jämna mellanrum för uppdateringar i chattfönstret.


![image](assets/en/06.webp)


Skicka en kort hälsning i chatten. Säljaren kommer att dela betalningsuppgifter när de kommer online


![image](assets/en/09.webp)


När du har fått de nödvändiga betalningsuppgifterna från säljaren fortsätter du med att slutföra betalningen. Därefter trycker du på knappen `Bekräfta att du gjort betalningen` och väntar sedan tålmodigt på bekräftelse på mottagandet. ️ ⌛️


Slutligen, när säljaren bekräftar mottagandet av betalningen, måste du också bekräfta mottagandet av Bitcoin. Detta slutför köpet med Bisq i Easy Mode. Gratulerar till köpet! Du kan nu trycka på knappen "Avsluta affären".


![image](assets/en/10.webp)


## 4️⃣ Tvistlösning på Bisq Easy


Om något går fel i din handel kan både köpare och säljare begära medlingsstöd.


**Vad medlare kan göra:**

- Hjälpa till att underlätta ett framgångsrikt avslut av affären

- Verifiera fiat-, altcoin- och Bitcoin-betalningar

- Avbryt affärer vid behov

- Rapportera allvarliga regelbrott till moderatorer för eventuell avstängning av användare


**Påföljder för bedrägliga säljare: **

Beroende på vilken typ av rykte de har:



- BSQ-obligationens rykte**: DAO kan konfiskera deras bundna BSQ
- Lök Address Rykte**: Deras Bisq 1 onion-adress kan vara förbjuden


**Viktig anmärkning:** Eftersom allt rykte är knutet till din användarprofil inaktiverar en bannlysning ditt rykte helt och hållet.


## 5️⃣ Skapa ditt eget erbjudande


I stället för att ta emot befintliga erbjudanden kan du skapa ditt eget köperbjudande och låta säljarna komma till dig. Det här är rätt alternativ om du inte hittar några erbjudanden med rätt premie eller betalningsmetoder på den marknad du vill handla på, men du måste vänta på att en säljare ska acceptera.


Från "Erbjudanden"-skärmen trycker du på den gröna "+"-ikonen i det nedre högra hörnet. Välj sedan `Buy Bitcoin` och välj din fiatvaluta.


Ställ in dina handelsparametrar:



- Fast belopp eller intervallbelopp**: Välj hur mycket du vill spendera.
- Betalningsmetod**: Välj bland tillgängliga alternativ
- Avveckling**: Välj Lightning ⚡ eller ₿ on-chain


Granska dina uppgifter och tryck på "Skapa erbjudande". Ditt erbjudande visas nu i "Erbjudandeboken".


![image](assets/en/07.webp)


*Obs: Som köpare på Bisq Easy behöver du inte rykte - det här är den viktigaste fördelen. Säljare bär kravet på rykte och risken, vilket är anledningen till att de tar ut premier. Ditt erbjudande behöver helt enkelt prissättas tillräckligt attraktivt för att välrenommerade säljare ska överväga det.*


När den har publicerats väntar du i avsnittet "Offertbok". När en säljare accepterar ditt erbjudande får du ett meddelande. Öppna affären i `Open Trades`, där säljaren och du kan utbyta dina betalningsuppgifter. Skicka din Bitcoin-adress eller Lightning-faktura till säljaren. Efter att ha skickat fiat, bekräfta betalningen. När säljaren har bekräftat mottagandet släpper de Bitcoin för att slutföra affären.


## 🎯 Slutsats


Bisq Easy möjliggör Bitcoin-köp utan säkerhet, vilket löser det klassiska kyckling-och-ägg-problemet för nya köpare. Avvägningen är tydlig: du förlitar dig på säljarens rykte istället för låsta medel för säkerhet. Detta förtroendebaserade tillvägagångssätt förklarar den typiska premien på 5-15%, som kompenserar ansedda säljare för deras investering i att bygga förtroende och tillhandahålla support. Även om systemet begränsar affärer till små belopp för att begränsa potentiella förluster, håll dig alltid till säljare med solida ryktespoäng. För nykomlingar som är villiga att acceptera dessa villkor erbjuder Bisq Easy en enkel ingångspunkt till Bitcoin.


## 📚 Bisq Enkla mobila resurser


[Github](https://github.com/bisq-network/bisq-mobile) | [Webbplats ](https://bisq.network/bisq-easy/)| [Wiki](https://bisq.wiki/Bisq_Easy)