---
name: Ledger Nano S

description: Så här ställer du in din Ledger Nano S-enhet
---

![image](assets/cover.webp)


*Ledger har meddelat att mjukvarustödet för den klassiska Nano S upphör från och med den 25 juni 2025: den här enheten kommer inte längre att få säkerhetsuppdateringar eller vara kompatibel med nya funktioner, vilket utsätter dess användare för potentiella sårbarheter och framtida inkompatibilitet. Pengar förblir dock tillgängliga via återställningsfrasen, men det rekommenderas starkt att migrera till en nyare modell för att säkerställa säkerheten och den långsiktiga tillgängligheten för dina bitcoins. Observera att detta gäller den **gamla Nano S**, inte den **Nano S Plus**, som kommer att fortsätta att stödjas.*


___


Cold fysisk Wallet - €60 - Nybörjare - För att säkra €2 000 till €50 000


Ledger är den franska lösningen för att säkra bitcoins på ett enkelt sätt.


I den här handledningen diskuterar vi även avsnittet om lösenfraser, en avancerad säkerhetslösning för lagring av stora summor: 20,000€ - 100,000€.


https://www.youtube.com/watch?v=_vsHNTLi8MQ


# Anslut Ledger till Sparrow Bitcoin Wallet (skrivguide)


Se till att du går igenom den andra delen "Använda Bitcoin hårdvaruplånböcker" först. Jag kommer att skumma igenom några steg och fokusera mest på vad som är specifikt för Ledger här.


## Konfigurera enheten


Ledger levereras med en egen USB-kabel. Se till att du använder den och inte vilken kabel som helst. Vissa USB-kablar är endast strömförsörjda. Den här överför data OCH ström. När jag har använt enheten med en USB-kabel för telefonladdning som ligger och skräpar har enheten inte kunnat ansluta.


Anslut den till din dator och enheten slås på.


![image](assets/1.webp)


Bläddra igenom alternativen. Du kommer att se


1. Konfigureras som ny enhet

2. Återställ från återställningsfras


I grund och botten frågar den om du vill att enheten ska skapa en seed åt dig eller om du redan har en som du vill använda. Det är bästa praxis att skapa din egen seed, men att göra det på ett säkert sätt är mycket avancerat och ligger utanför ramen för den här artikeln. Välj "Ställ in som ny enhet"


Du kommer sedan att bli ombedd att välja en PIN-kod. Detta är inte en del av din Bitcoin seed och är endast specifikt för denna enhet. Den låser enheten.


Den kommer sedan att presentera 24 ord som du behöver gå igenom och skriva ner.


Konstigt nog står det "tryck vänster för att verifiera dina ord" när du kommer till slutet. Det beskriver inte hur du bekräftar för att gå vidare, utan betyder bara att du kan gå tillbaka och titta på orden igen. Tryck höger istället, och bekräfta genom att trycka vänster och höger samtidigt.


Nästa bit är superirriterande. Den blandar ihop de 24 orden och du måste bekräfta varje ord, 1 till 24, genom att cykla igenom alla ord för varje val. När du är klar kan du bekräfta med en tvåknappstryckning och fortsätta.


![image](assets/2.webp)


Du kommer att se på din instrumentpanel att du har en inställningsknapp och en plus-signaturknapp som låter dig installera appar. Men du måste ansluta till Ledger Live först. Vi gör det nästa gång..


## Ladda ner Ledger Live


Du kan ladda ner Ledger Live från deras webbsida, men det är bättre att hämta det från GitHub, där källkoden hålls.


Google "Ledger live GitHub" eller klicka på ![detta](länk https://github.com/LedgerHQ/Ledger-live-desktop)


![image](assets/3.webp)


Scrolla ner tills du ser rubriken "Downloads"..


![image](assets/4.webp)


Längst ner ser du länken: Instruktioner för att verifiera Hash och signaturer för installationspaketen finns på den här sidan. Klicka på den länken.(https://live.Ledger.tools/lld-signatures)


![image](assets/5.webp)


Längst upp finns länkval för det programpaket du behöver, beroende på ditt operativsystem. Klicka på lämplig länk för att ladda ner.


Därefter vill vi verifiera nedladdningens Hash, för extra säkerhet. Ledger publicerar Hash för var och en av de tillgängliga filerna. Vi kommer nu att Hash nedladdningen och jämföra utdata. Den måste vara identisk för att vi ska kunna vara säkra på att filen inte har manipulerats.


Öppna terminal på en Mac eller CMD på Windows; skriv in följande kommandon och tryck på Enter:


```bash
cd Downloads
```


```bash
shasum -a 512 ledger-live-desktop-2.32.2-mac.dmg # <--- For Mac
certutil -hashfile ledger-live-desktop-2.32.2-win.exe SHA512 # <--- For Windows
```


Förhoppningsvis är det uppenbart att kommandona börjar efter pilarna. Se till, om den här artikeln är inaktuell, att du ändrar filnamnet i kommandona till exakt det filnamn du laddade ner. Du måste trycka på <Enter>-tangenten efter varje kommando. Kommandona som du ser här kanske inte får plats på en rad i din webbläsare. Observera att allt är skrivet på en rad.


Titta på utdata från Hash och se till att den är identisk med den som publicerats på GitHub.


Helst vill du bli extra snygg och se till att hasharna som publiceras inte är falska. Vi gör detta med gpg-signaturer, men det ligger utanför ramen för den här artikeln. Om du vill lära dig om det (och jag föreslår att du så småningom gör det), titta igenom den här artikeln.


## Anslut till Ledger Live


Innan du kör Ledger Live hjälper det integriteten lite att slå på ett VPN. Ledger kommer fortfarande att få alla dina adresser, men de kommer inte att känna till din IP Address, vilket avslöjar ditt hem Address. Mullvad VPN är en utmärkt VPN-tjänst och det är inte särskilt dyrt (jag annonserar inte, det är bara vad jag använder).


Installera programvaran på din dator och kör den.


![image](assets/6.webp)


Välj din enhet och välj "Första gången du använder..."


![image](assets/7.webp)


Du kommer sedan att ledas genom en guide, men vi har gjort alla dessa steg så att du kan cykla igenom.


![image](assets/8.webp)


Efter många steg och en frågesport kommer den att kontrollera att enheten är äkta. Du måste se till att du är ansluten och har angett PIN-koden, och sedan kommer den att fråga på enheten om du tillåter Ledger Live att ansluta. Du måste naturligtvis bekräfta det.


![image](assets/9.webp)


Det fanns lite shitcoin-reklam förklädd som "release notes" i nästa popup. Avfärda det, och sedan ska du komma till den här skärmen.


![image](assets/10.webp)


Du måste klicka på "Lägg till konto" för att få en Bitcoin Wallet.


![image](assets/11.webp)


Se till att du väljer Bitcoin, och inte Bitcoin Cash eller någon annan shitcoin. Den kommer att kontrollera enheten och du måste bekräfta att du vill fortsätta PÅ ENHETEN. Den kommer att beräkna adresser i ett par minuter. Klicka sedan på DONE.


![image](assets/12.webp)

![image](assets/13.webp)


Jättebra. Nu har du en shitcoin Wallet manager som innehåller en Bitcoin Wallet på din dator. Du behöver faktiskt inte det här längre och kan bli av med det. Det verkliga syftet var att få Bitcoin-appen på själva enheten, och detta var det enda sättet, förutom att utföra några extrema mjukvaruingenjörstekniker.


Kom ihåg att vi tidigare, på enheten, hade en inställningsknapp och en plusteckenknapp. Nu har vi en extra knapp - Bitcoin App-knappen.


Du kan stänga av Ledger Live nu.


## Lägg till en passphrase


Nu när vi har Bitcoin-appen kan vi lägga till en passphrase till vår seed-fras. Vi kunde inte göra det tidigare när seed först skapades eftersom vi i början inte hade Bitcoin-appen, och vi behövde ansluta till Ledger Live för att få den.


Gå till menyn "Inställningar" i enheten och sedan till undermenyn "Säkerhet". Välj sedan passphrase. Du kommer att se "Avancerad funktion". Klicka på högerknappen, du kommer att se "läs manual..." och sedan efter ett högerklick kommer du att se "tillbaka". Men det är inte slutet. Intuitivt skulle man kunna tro det, men klicka på högerknappen igen. Du kommer att se "set up passphrase".


Du kan välja att "bifoga till PIN-koden" eller "ställa in temporärt". Jag rekommenderar att du "kopplar till PIN-koden". På så sätt kan du komma åt olika plånböcker beroende på vilken PIN-kod du anger när du först slår på enheten. Om du "ställer in temporärt" måste du ange passphrase varje gång du vill komma åt Wallet, men det är alltid från standard-PIN-koden.


Ange passphrase och bekräfta.


Du kommer att bli tillfrågad om den "aktuella PIN-koden". Detta är inte den PIN-kod som du associerar med den nya passphrase. Det är den PIN-kod som du angav när du startade enheten för den här sessionen.


Du kan nu gå tillbaka till huvudmenyn genom att välja alternativet Tillbaka några gånger.


## Tittar på Wallet


I tidigare artiklar har jag förklarat hur du laddar ner och verifierar Sparrow wallet, och hur du ansluter den till din egen nod eller en offentlig nod. Du bör följa dessa guider:



- Installera Bitcoin Core ( https://armantheparman.com/bitcoincore/)



- Installera Sparrow Bitcoin Wallet (https://armantheparman.com/download-Sparrow/)



- Anslut Sparrow Bitcoin Wallet till Bitcoin Core (https://armantheparman.com/sparrowcore/)


Ett alternativ till att använda Sparrow Bitcoin Wallet är Electrum Desktop Wallet, men jag kommer att fortsätta att förklara Sparrow Bitcoin Wallet eftersom jag bedömer att det är det bästa för de flesta människor. Avancerade användare kanske vill använda Electrum som ett alternativ.


Vi kommer nu att ladda upp den och ansluta Ledger, med Wallet som innehåller passphrase. Denna Wallet har aldrig exponerats för Ledger Live eftersom den skapades EFTER att vi anslöt enheten till Ledger Live. Se till att du aldrig ansluter den till Ledger Live någonsin igen för att inte exponera din nya privata Wallet.


Skapa en ny Wallet:


![image](assets/14.webp)


Döp det till något vackert


![image](assets/15.webp)


Lägg märke till kryssrutan "Har befintlig transaktion". Om detta är en Wallet som du har använt tidigare ska du markera denna annars kommer ditt saldo felaktigt att visas som noll. Om du markerar den här rutan ber du Sparrow att undersöka Bitcoin Core's databas (Blockchain) för tidigare transaktioner. I den här guiden använder vi en helt ny Wallet, så du kan lämna rutan omarkerad.


![image](assets/16.webp)


Klicka på "Connected Hardware Wallet" och kontrollera att enheten faktiskt är ansluten, påslagen, att PIN-koden är inmatad och att du har gått in i Bitcoin-appen.


![image](assets/17.webp)


Klicka på "Scan" och sedan på "Import Keystore" på nästa skärm.


![image](assets/18.webp)


Det finns inget att redigera på nästa skärm, Ledger har fyllt i det åt dig. Klicka på "Apply"


![image](assets/19.webp)


På nästa skärm kan du lägga till ett lösenord. Förväxla inte detta med "passphrase"; många människor kommer att göra det. Namngivningen är olycklig. Lösenordet gör att du kan låsa denna Wallet på din dator. Det är specifikt för den här programvaran på den här datorn. Det är inte en del av din Bitcoin privata nyckel.


![image](assets/20.webp)


Efter en paus, medan datorn tänker, kommer du att se att knapparna till vänster ändras från grå till blå. Gratulerar, din Wallet är nu klar att användas. Gör och skicka transaktioner till ditt hjärtas innehåll.


![image](assets/21.webp)


## Mottagning


För att ta emot några Bitcoin går du till fliken Adresser till vänster och väljer en av adresserna att ta emot. Högerklicka bara på den Address du vill ha och välj "kopiera Address". Gå sedan till din Exchange där pengarna skickas från och klistra in den där. Eller så kan du ge Address:an till en kund som kan använda den för att betala dig.


När du använder Wallet för första gången bör du få en mycket liten summa, öva på att spendera den till en annan Address, antingen inom Wallet eller tillbaka till Exchange, för att bevisa att Wallet fungerar som förväntat.


När du har gjort det måste du säkerhetskopiera de ord du har skrivit ner. En enda kopia är inte tillräckligt. Ha minst två papperskopior (metall är bättre) och förvara dem på två olika, väl skyddade, platser. Detta minskar risken för att en naturkatastrof förstör din HWW och pappersbackup i en och samma händelse. Se "Använda Bitcoin hårdvaruplånböcker" för en fullständig diskussion om detta.


## Sändning


![image](assets/22.webp)


När du gör en betalning måste du klistra in den Address som du betalar till i fältet "Pay to". Du kan faktiskt inte lämna etiketten tom, det är bara för dina egna plånboksregister, men Sparrow tillåter inte det - skriv bara in något (bara du kommer att se det). Ange beloppet och du kan också manuellt justera den avgift du vill ha.


Wallet kan inte signera transaktionen om inte HWW är ansluten. Det är HWW: s jobb - att ta emot transaktionen, underteckna den och ge den tillbaka, undertecknad. Se till att när du signerar på enheten, inspekterar du visuellt att den Address du betalar till är densamma på enheten och på datorskärmen, och den Invoice du får (t.ex. kan du ha fått ett e-postmeddelande om att betala en viss Address).


Var också uppmärksam på att om du väljer att använda ett mynt som är större än betalningsbeloppet, kommer återstoden att skickas tillbaka till en av dina plånboks ändringsadresser. Vissa människor har inte känt till detta och letat upp sin transaktion på en offentlig Blockchain och trodde att några Bitcoin skickades till en angripares Address, men i själva verket var det deras egen förändring Address.


## Firmware


För att uppdatera den fasta programvaran måste du ansluta till Ledger Live. Om du vill göra detta bör du först torka enheten och se till att du har dina säkerhetskopieringsord och passphrase tillgängliga för att återställa enheten. Anledningen till att jag föredrar att torka enheten först är att du måste ansluta din enhet till Ledger Live för att uppdatera firmware, och jag föredrar att inte utsätta din nya Wallet (den med passphrase) för Ledger Live, någonsin. Jag litar bara inte på att Ledger inte extraherar min offentliga nyckelinformation från enheten när jag ansluter till Ledger Live. De hävdar att de inte gör det, men jag kan inte verifiera det själv om jag inte läser koden och förstår den interna hårdvaran också.


## Slutsats


Den här artikeln visade dig hur du använder en Ledger HWW på ett säkrare och mer privat sätt än vad som annonserats - men den här artikeln är inte tillräcklig. Som jag sa i början bör du kombinera den med informationen i "Använda hårdvaruplånböcker av typen Bitcoin".

Tips:


Statisk blixt Address: dandysack84@walletofsatoshi.com

https://armantheparman.com/ledgersparrow/


För att utforska detta ämne ytterligare och stärka säkerheten för din Wallet på en Ledger Nano med en BIP39 passphrase, inbjuder jag dig att kolla in denna omfattande handledning:


https://planb.network/tutorials/wallet/backup/passphrase-ledger-9ae6d9a2-7293-438a-8fe0-e59147ef2f49