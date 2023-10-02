# Installera Tails på en USB-enhet

_**Guide föreslagen av Hari Seldon inom ramen för Agora256**_

![image](assets/cover.jpeg)

Ett bärbar och glömsk operativsystem som skyddar dig mot övervakning och censur.

## Varför ha en USB-enhet med Tails installerad?

Tails (https://tails.boum.org/) är det enklaste sättet att alltid ha en säker dator tillgänglig som inte lämnar några spår på den dator du använder den med.

För att använda Tails, stäng av den dator du har tillgång till (hemma hos dina föräldrar, hos dina vänner, på ett internetcafé...) och starta den från din Tails USB-enhet istället för Windows, macOS eller Linux.

Efter det kommer du ha en arbets- och kommunikationsmiljö som är oberoende av det vanliga operativsystemet och som aldrig använder hårddisken.

Tails skriver aldrig på hårddisken och använder endast datorns RAM-minne för att fungera. Detta minne raderas helt när Tails stängs av, vilket tar bort alla möjliga spår.

## Några konkreta användningsfall

För att ge dig konkreta idéer om varför det är bra att alltid ha en USB-enhet med Tails, här är en liten, icke-uttömmande lista sammanställd av Agora256-teamet:

- Ansluta till internet och Tor på ett icke-censurerat och anonymt sätt för att besöka webbplatser utan att lämna spår;
- Öppna en PDF från en misstänksam webbplats;
- Testa din backup av Bitcoin-privatnyckel med Electrum-plånboken;
- Använda en kontorspaket (LibreOffice) och arbeta på en dator som inte tillhör dig;
- Ta de första stegen i en Linux-miljö för att lära dig att lämna Microsofts och Apples värld.

## Hur kan man lita på Tails?

Det finns alltid en viss grad av förtroende när man använder programvara, men det behöver inte vara blind. Ett verktyg som Tails bör sträva efter att ge sina användare sätt att vara pålitliga. För Tails innebär detta:

- en offentlig källkod: https://gitlab.tails.boum.org/;
- ett projekt baserat på välrenommerade projekt: Tor och Debian;
- verifierbara och reproducerbara nedladdningar;
- rekommendationer från olika personer och organisationer.

## Installations- och användarguide

Syftet med denna installationsguide är att vägleda dig genom varje steg i installationen. Vi kommer inte att beskriva mer än vad den officiella guiden gör, men vi kommer att peka dig i rätt riktning och ge dig tips och tricks.

Av praktiska skäl kommer dessa råd att fokusera på macOS- och Linux-plattformarna.
🛠️
Innan du börjar med denna procedur, se till att du har en USB-enhet med en läshastighet på minst 150 MB/s och en storlek på minst 8 GB, helst av typen USB 3.0.

Förutsättningar:
- 1 USB-enhet, endast för Tails, med minst 8 GB
- En dator ansluten till internet med Linux, macOS (eller Windows)
- Ungefär en timme totalt, beroende på din internetanslutningshastighet, varav en halvtimme för installationen (1,3 GB-fil att ladda ner)

## Steg 1: Ladda ner Tails från din dator

![image](assets/1.jpeg)

> 🔗 Officiell avsnitt om Tails: https://tails.boum.org/install/linux/index.fr.html#download

Att ladda ner installationsfilen med .img-förlängning kan ta lite tid beroende på din internetnedladdningshastighet, så se till att göra det i förväg. Med en modern och snabb internetuppkoppling tar det mindre än 5 minuter.

Spara filen i en känd mapp, som "Nedladdningar", eftersom det kommer att behövas i nästa steg.

## Steg 2: Kontrollera din nedladdning

![image](assets/2.jpeg)

> 🔗 Officiell avsnitt om Tails: https://tails.boum.org/install/linux/index.fr.html#verify

Att kontrollera nedladdningen säkerställer att den kommer från Tails-utvecklarna och inte har blivit korrupt eller avlyssnad under nedladdningen.

Det är möjligt att manuellt kontrollera att filen du precis har laddat ner är den förväntade filen med hjälp av PGP, men utan avancerad kunskap ger denna kontroll samma säkerhetsnivå som JavaScript-kontrollen på nedladdningssidan, även om den är mycket mer komplicerad och felbenägen.

För att kontrollera filen, använd knappen "Välj din nedladdning..." som finns i det officiella avsnittet!

## Steg 3: Installera Tails på din USB-enhet

![image](assets/3.jpeg)

> 🔗 Officiell avsnitt om Tails:
>
> - Linux: https://tails.boum.org/install/linux/index.fr.html#install
> - macOS: https://tails.boum.org/install/mac/index.fr.html#etcher och https://tails.boum.org/install/mac/index.fr.html#install

Detta steg att installera Tails på din USB-enhet är det svåraste i hela guiden, särskilt om du aldrig har gjort det tidigare. Det viktigaste är att välja rätt procedur i det officiella avsnittet för ditt operativsystem: Linux eller macOS.

När verktygen har installerats och förberetts enligt rekommendationerna kan filen med .img-förlängning kopieras till din enhet (alla befintliga data kommer att raderas) för att göra den "startbar" oberoende.

Lycka till! och vi ses i steg 4.

## Steg 4: Starta om med din Tails USB-enhet

![image](assets/4.jpeg)
> 🔗 Officiell Tails-sektion: https://tails.boum.org/install/linux/index.sv.html#restart
Det är dags att starta en av dina datorer med hjälp av ditt nya USB-minne. Sätt in det i en av USB-portarna och starta om!

> 💡 De flesta datorer startar inte automatiskt från Tails USB-minnet, men du kan trycka på startmenyknappen för att visa en lista över möjliga enheter att starta från.

Ta reda på vilken knapp du behöver trycka på för att se till att du får upp startmenyn där du kan välja USB-minnet istället för din vanliga hårddisk. Här är en icke-uttömmande lista över tillverkare:

| Tillverkare | Knappar            |
| ----------- | ------------------ |
| Acer        | F12, F9, F2, Esc   |
| Apple       | Option             |
| Asus        | Esc                |
| Clevo       | F7                 |
| Dell        | F12                |
| Fujitsu     | F12, Esc           |
| HP          | F9                 |
| Huawei      | F12                |
| Intel       | F10                |
| Lenovo      | F12                |
| MSI         | F11                |
| Samsung     | Esc, F12, F2       |
| Sony        | F11, Esc, F10      |
| Toshiba     | F12                |
| andra...    | F12, Esc           |

När USB-minnet är valt bör du se den här nya startskärmen, det är ett mycket gott tecken, så låt datorn fortsätta starta...

![image](assets/5.jpeg)

## Steg 5: Välkommen till Tails!

![image](assets/6.jpeg)

> 🔗 Officiell Tails-sektion: https://tails.boum.org/install/linux/index.sv.html#tails

En eller två minuter efter startladdaren och laddningsskärmen visas välkomstskärmen.

![image](assets/7.jpeg)

På välkomstskärmen väljer du språk och tangentbordslayout i avsnittet Språk och region. Klicka på Starta Tails.

![image](assets/8.jpeg)

Om din dator inte är ansluten med en kabel till ditt nätverk, vänligen se Tails officiella instruktioner för hjälp med att ansluta till nätverket utan Wi-Fi (sektionen "Testa ditt Wi-Fi").

När du är ansluten till det lokala nätverket visas Tor-anslutningsguiden för att hjälpa dig att ansluta till Tor-nätverket.

![image](assets/9.jpeg)

Du kan nu börja surfa anonymt, utforska alternativ och program som ingår i Tails. Ha så kul, du kan göra misstag eftersom ingenting ändras på USB-minnet... Vid nästa omstart kommer alla dina upplevelser att vara bortglömda!

## I en kommande guide...

När du har experimenterat lite mer med ditt eget Tails USB-minne kommer vi att utforska mer avancerade ämnen i en annan artikel, som:
Uppdatera en nyckel med den senaste versionen av Tails; Konfigurera och använda persistent lagring; Installera extra programvara.
Fram tills dess, som alltid, om du har några frågor, tveka inte att dela dem med Agora256-communityn, vi lär oss tillsammans för att vara bättre imorgon än vi är idag!

_**Guide föreslagen av Hari Seldon inom ramen för Agora256; ursprungligt inlägg: https://agora256.com/installer-tails-usb/**_