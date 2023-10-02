# BISQ: peer to peer-utbyte

Bisq är en decentraliserad handelsplattform för digitala tillgångar, främst Bitcoin. Den erbjuder direkt, säker och privat transaktioner mellan användare över hela världen utan behov av en mellanhand.

Hemsida: https://bisq.network/
Information: https://bisq.network/getting-started/

_Var försiktig så att du inte gör något ogenomtänkt, Bisq är en avancerad lösning. När den är inställd är den mycket kraftfull, men om du är helt nybörjare kanske den inte är lämplig för dig._

## handledningsvideo

Full handledning av BTC Session:

![ BISQ - Köp + Sälj Bitcoin UTAN KYC, UTAN ID! ](https://youtu.be/4LyEKA5Iq9I)

## Skrivguide:

Ursprunglig guide från Bisq-teamet: https://bisq.network/getting-started/

_Om du känner till en mer aktuell guide med bilder och mer inriktning för nybörjare, dela gärna med dig av den till oss!_

1. Ladda ner och installera Bisq

![Ladda ner, verifiera och installera Bisq: Linux och macOS](https://youtu.be/dTfM4AsxNHY)
![Ladda ner, verifiera och installera Bisq: Windows](https://youtu.be/XABzwXw6X0A)

Du kan enkelt ladda ner och installera Bisq från denna webbplats (https://bisq.network/downloads) eller från GitHub (https://github.com/bisq-network/bisq/releases/latest).

Det är också en bra idé att verifiera din installationsfil för att vara extra säker på att den inte har manipulerats. Se videorna här för instruktioner. Mer detaljer finns i denna wiki-artikel. (https://bisq.wiki/Downloading_and_installing)

Om du vill bygga Bisq från källkod, här är instruktioner (https://github.com/bisq-network/bisq/blob/master/docs/build.md). Bisq är fri/libre öppen källkod som du kan bidra till. (https://bisq.wiki/Contributor_checklist)

![bild](assets/1.png)

2. Säkerhetskopiera nycklar, skriv ner fröet

![3 saker du bör göra direkt efter att ha installerat Bisq](https://youtu.be/JSwMcQAT_CA)
![Rundtur i Bisq](https://youtu.be/HDkzUl9wibc)

Med Bisq har du full kontroll över dina medel och dina data. Det innebär att du har enastående suveränitet, men det innebär också att ingen kan hjälpa dig om du förlorar något viktigt - så det är viktigt att du gör ordentliga säkerhetskopior innan du använder Bisq för att handla.

Vi har också förberett en kort rundtur i Bisq-gränssnittet så att du kan få ut mesta möjliga av det.

Mer detaljer finns på wikin: skriv ner dina fröord och säkerhetskopiera din datakatalog. (https://bisq.wiki/Backing_up_application_data)

![bild](assets/2.png)

3. Skapa ett betalningskonto

![Skapa ett Fiat-betalningskonto på Bisq](https://youtu.be/nDgT_kFC-9Y)
![Skapa ett alternativmyntbetalningskonto på Bisq](https://youtu.be/33UTotkxw_0)
![Allt om kontogränser på Bisq (endast fiat)](https://youtu.be/TP5Zh6IJPVo)
För att handla med bitcoin på Bisq måste du ha en metod för att skicka eller ta emot andra medel. Bisq hanterar endast bitcoinsidan av en handel - den andra sidan hanteras genom fiatbetalningstjänster (banker, postanvisningar, kontanter) eller altcoin-plånböcker.
Osäker på vilken typ av betalningskonto du ska skapa? Det finns en fullständig lista över betalningsmetoder på wikin (https://bisq.wiki/Payment_methods). Om du kommer att handla med fiat, se till att du tittar på videon om kontogränser eller läser den här artikeln på wikin (https://bisq.wiki/Account_limits).

Det finns många altcoins tillgängliga för handel på Bisq. Här är några tips för toppmarknaderna:

- Monero. Om du skickar XMR, se till att din plånbok kan ge transaktionsnyckeln, transaktions-ID och mottagarens adress.
- BSQ. Du hittar din BSQ-adress under DAO > BSQ Wallet > Receive.
- Liquid BTC. Om du tar emot L-BTC måste du använda en plånbok som kan avslöja din blinding key, som t.ex. Elements-programvaran (Blockstream Green fungerar inte vid skrivandet av detta).

4. Gör en handel

![Gör ett erbjudande på Bisq](https://youtu.be/w7Uvv-xrxn8)
![Ta ett erbjudande och slutför en handel på Bisq](https://youtu.be/E6AOgXajK_E)

Att göra ett erbjudande ger vanligtvis ett bättre pris och mer kontroll (t.ex. att ställa in betalningsmetod och insättningsprocent), men att ta ett erbjudande kan vara mer bekvämt.

Se handelsavgifter här (https://bisq.wiki/Trading_fees).

Du kommer att märka att de som gör erbjudanden betalar mycket mindre. Observera att det finns en mobilapp för iOS och Android som du kan använda för att få aviseringar om nya erbjudanden och åtgärder för öppna affärer. För att se båda sidor av en Bisq-handel samtidigt, sida vid sida, se till att kolla in vår Bird's Eye View of a Bisq Trade-video.

Det är allt - de grundläggande sakerna för att komma igång med Bisq.

## Steg för steg-guide för handel

Steg för steg-guide av Bitcoiner.guide, även känd som bitcoinQ&A https://bitcoiner.guide/bisq/

3. Nu när din betalningsmetod är inställd kan du gå till fliken "Köp BTC" och se säljare som erbjuder bitcoin i utbyte mot din valda betalningsmetod. Här kan du se BTC-priset, procentuell skillnad jämfört med "spot"-priset och mängden bitcoin till salu från varje säljare. När du har hittat ett erbjudande du gillar, klicka på "Ta erbjudande för att köpa BTC".

![bild](assets/3.png)

4. Detta tar dig till en skärm där du kan kontrollera och bekräfta detaljerna innan du går in i handeln. När du är nöjd, klicka på "nästa steg".

![bild](assets/4.png)

5. Nu måste du finansiera din handelsplånbok med en liten mängd bitcoin som fungerar som en säkerhetsdeposition. Detta är vanligtvis cirka 15% av handelsstorleken. Säljaren måste också lägga upp en deposition på sin sida.

![bild](assets/5.png)

6. Du kan nu bekräfta erbjudandet och starta handeln.

![bild](assets/6.png)

7. Du kommer nu att ha en mycket kort väntetid medan Bitcoin-nätverket bekräftar handelstransaktionen, vilket placerar båda parters säkerhetsdepositioner i escrow multi-sig.

![bild](assets/7.png)

8. Efter en bekräftelse på kedjan kommer du sedan att se ett fönster med säljarens detaljer för att skicka betalningen till.

![bild](assets/8.png)
9. När du har skickat betalningen, tryck på knappen för att bekräfta att du har gjort det och vänta sedan på att säljaren bekräftar att de har mottagit dina pengar. Vid den här punkten kan du också chatta med din handelspartner via slut-till-slut-krypterade meddelanden genom att trycka på "Öppna handelschatt".
När säljaren bekräftar att de har mottagit pengarna kommer de köpta bitcoin tillsammans med din säkerhetsdeposition att släppas till din Bisq-plånbok.

![image](assets/9.png)

10. Det är allt, din första handel är nu klar! Du kan antingen ta ut dina bitcoin till en extern plånbok eller lämna dem kvar på ditt Bisq-konto.

![image](assets/10.png)

## Avvägningar med att köpa utan KYC (enligt bitcoin Q&A)

Så enkelt som det är att köpa på Bisq finns det vissa avvägningar att vara medveten om.

1. Du behöver BTC innan du handlar för att bilda en säkerhetsdeposition. Det är inget problem om du har varit med ett tag, men det kan bli ett problem om du vill använda Bisq som ditt första köp. Ditt bästa alternativ i det här fallet är att få lite bitcoin från en vän eller familjemedlem.

2. KYC-fri bitcoin lockar ofta till sig ett påslag över spotpriset, vilket kan avskräcka vissa köpare. Som jag nämnde tidigare handlar det här om avvägningar och jag skulle personligen vara beredd att betala 5-8% över spotpriset för lyxen att hålla min personliga data säker.

Om du inte har bråttom att köpa kan du också skapa ett "Köpererbjudande" där du kan låta Bisq-nätverket veta att du är villig att köpa en viss mängd bitcoin till ett visst pris i förhållande till marknadsvärdet. Om en säljare dyker upp och gillar ditt erbjudande kan de acceptera det.

3. Decentraliserade börser kan ibland ha brist på likviditet jämfört med större centraliserade enheter. Om du vill köpa större belopp oftare kan du ha svårt.

4. Även om det aldrig har hänt mig kan peer-to-peer-handel ibland inte fungera som avsett och användare måste gå igenom tvistlösningsprocessen. Som tur är, på grund av hur Bisqs incitamentsstrukturer är uppbyggda, är dessa fall få och långt mellan.

Precis som med de flesta saker som rör Bitcoin är hela KYC/Icke-KYC-debatten nyanserad och full av avvägningar. Jag förstår det, de vanligaste fiat-ingångarna som Coinbase och CashApp gör det mycket enkelt att köpa, särskilt för nybörjare, men ta dig en sekund att överväga avvägningarna och undersöka alternativen innan du så lättvindigt ger bort din personliga information.