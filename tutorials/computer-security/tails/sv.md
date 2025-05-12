---
name: Svansar

description: Installera Tails på ett USB-minne
---

![image](assets/cover.webp)


Ett portabelt operativsystem med minnesförlust som skyddar dig mot övervakning och censur.


## Varför ha ett USB-minne med Tails installerat?


Tails (https://tails.boum.org/) är det enklaste sättet att alltid ha en säker dator till hands, som inte lämnar några spår på den dator du använder den med.


För att använda Tails stänger du av den dator du har tillgång till (hos dina föräldrar, hos dina vänner, på ett internetcafé ...) och startar den med din Tails USB-nyckel istället för Windows, macOS eller Linux.


Efter det kommer du att ha en arbetsyta och kommunikationsmiljö som är oberoende av det vanliga operativsystemet och aldrig använder Hard-enheten.


Tails skriver aldrig till Hard-enheten utan använder endast datorns RAM-minne för att fungera. Detta minne raderas helt när Tails stängs av och därmed försvinner alla möjliga spår.


## Några konkreta användningsfall


För att ge dig konkreta idéer om fördelarna med att alltid ha en USB-nyckel med Tails, här är en liten icke uttömmande lista sammanställd av Agora256-teamet:



- Anslut till Internet och Tor på ett ocensurerat och anonymt sätt för att surfa på webbplatser utan att lämna spår;
- Öppna en PDF från en misstänkt webbplats;
- Testa din säkerhetskopia av den privata nyckeln Bitcoin med Electrum Wallet;
- Använd en kontorssvit (LibreOffice) och arbeta på en dator som inte tillhör dig;
- Ta dina första steg i en Linux-miljö för att lära dig hur du lämnar Microsofts och Apples värld.


## Hur litar man på svansar?


Det finns alltid ett element av förtroende när man använder programvara, men det behöver inte vara blint. Ett verktyg som Tails måste sträva efter att förse sina användare med medel för att vara pålitliga. För Tails innebär detta:



- Offentlig källkod: https://gitlab.tails.boum.org/;
- Ett projekt baserat på välrenommerade projekt: Tor och Debian;
- Verifierbara och reproducerbara nedladdningar;
- Rekommendationer från olika personer och organisationer.


## Installations- och användarhandbok


Syftet med den här installationsguiden är att guida dig genom varje steg i installationen. Vi kommer inte att beskriva åtgärder som ska vidtas mer än den officiella guiden, men vi kommer att peka dig i rätt riktning samtidigt som vi ger dig tips och tricks.


Av praktiska skäl kommer dessa tips att fokusera på macOS- och Linux-plattformar.

🛠️

Innan du påbörjar denna procedur bör du se till att du har ett USB-minne med en läshastighet på minst 150 MB/s och en kapacitet på minst 8 GB, helst USB 3.0.


Förkunskapskrav:



- 1 USB-minne, endast för Tails, med en kapacitet på minst 8 GB
- En dator som är ansluten till Internet med Linux, macOS (eller Windows)
- Ungefär en timmes ledig tid, beroende på hastigheten på din Internetanslutning, inklusive ½ timme för installation (1,3 GB fil att ladda ner)


## Steg 1: Ladda ner Tails från din dator


![image](assets/1.webp)


🔗 **Officiell svanssektion:** https://tails.boum.org/install/linux/index.fr.html#download


Nedladdning av installationsfilen med tillägget .img kan ta lite tid beroende på din nedladdningshastighet på Internet, så planera i förväg. Med en modern och effektiv anslutning tar det mindre än 5 minuter.


Spara filen i en känd mapp, t.ex. Downloads, eftersom den kommer att behövas i nästa steg.


## Steg 2: Verifiera din nedladdning


![image](assets/2.webp)


🔗 **Officiell svanssektion:** https://tails.boum.org/install/linux/index.fr.html#verify


Genom att verifiera nedladdningen säkerställs att den är utfärdad av Tails-utvecklarna och inte har skadats eller fångats upp under nedladdningen.


Det är möjligt att manuellt verifiera att den fil du just har laddat ner är den förväntade med hjälp av PGP, men utan avancerad kunskap erbjuder denna verifiering samma säkerhetsnivå som JavaScript-verifieringen på nedladdningssidan, samtidigt som den är mycket mer komplicerad och benägen att göra fel.


För att verifiera filen, använd knappen "Välj din nedladdning ..." som finns i det officiella avsnittet!


## Steg 3: Installera Tails på din USB-nyckel


![image](assets/3.webp)


🔗 **Officiell svanssektion:**



- Linux:** https://tails.boum.org/install/linux/index.fr.html#install
- macOS:** https://tails.boum.org/install/mac/index.fr.html#etcher och https://tails.boum.org/install/mac/index.fr.html#install


Detta steg för att installera Tails på din USB-nyckel är det svåraste i hela guiden, särskilt om du aldrig har gjort det förut. Den viktigaste punkten är att välja rätt procedur i det officiella avsnittet för ditt operativsystem: Linux eller macOS.


När verktygen har installerats och förberetts enligt rekommendationerna kan filen med tillägget .img kopieras till din nyckel (all befintlig data raderas) för att göra den "startbar" på egen hand.


Lycka till! och vi ses på steg 4.


## Steg 4: Starta om på din Tails USB-nyckel


![image](assets/4.webp)


🔗 **Officiell svanssektion:** https://tails.boum.org/install/linux/index.en.html#restart


Nu är det dags att starta en av dina datorer med hjälp av ditt nya USB-minne. Sätt in det i en av dess USB-portar och starta om!


**Notera💡: De flesta datorer startar inte automatiskt från Tails USB-minne, men du kan trycka på startmenyknappen för att visa en lista över möjliga enheter att starta från.**


För att avgöra vilken tangent du ska trycka på för att se till att du har en startmeny som låter dig välja USB-minnet istället för din vanliga Hard-enhet, följer här en icke uttömmande lista per tillverkare:


| Manufacturer | Key              |
| ------------ | ---------------- |
| Acer         | F12, F9, F2, Esc |
| Apple        | Option           |
| Asus         | Esc              |
| Clevo        | F7               |
| Dell         | F12              |
| Fujitsu      | F12, Esc         |
| HP           | F9               |
| Huawei       | F12              |
| Intel        | F10              |
| Lenovo       | F12              |
| MSI          | F11              |
| Samsung      | Esc, F12, F2     |
| Sony         | F11, Esc, F10    |
| Toshiba      | F12              |
| others...    | F12, Esc         |

När USB-minnet har valts bör du se den här nya startskärmen, vilket är ett mycket gott tecken, så låt datorn fortsätta att starta ...


![image](assets/5.webp)


## Steg 5: Välkommen till Tails!


![image](assets/6.webp)


🔗 **Officiell svanssektion:** https://tails.boum.org/install/linux/index.en.html#tails


En eller två minuter efter startladdaren och laddningsskärmen visas välkomstskärmen.


![image](assets/7.webp)


På välkomstskärmen väljer du språk och tangentbordslayout i avsnittet Language & Region. Klicka på Start Tails.


![image](assets/8.webp)


Om din dator inte är ansluten till ditt nätverk kan du läsa de officiella Tails-instruktionerna för att ansluta till ditt nätverk utan Wi-Fi (avsnittet "Testa ditt Wi-Fi").


När du är ansluten till det lokala nätverket visas guiden Tor Connection som hjälper dig att ansluta till Tor-nätverket.


![image](assets/9.webp)


Du kan börja surfa anonymt och utforska de alternativ och program som ingår i Tails. Ha kul, du har gott om utrymme för fel, eftersom ingenting ändras på USB-minnet... Vid nästa omstart kommer du att ha glömt alla dina erfarenheter!


## I en framtida guide...


När du har experimenterat lite mer med ditt eget Tails USB-minne kommer vi att utforska andra mer avancerade ämnen i en annan artikel, till exempel:



- Uppdatera en nyckel med den **senaste versionen av Tails**;
- Konfigurera och använda **persistent lagring**;
- Installera **ytterligare programvara**.


Fram till dess, som alltid, om du har några frågor är du välkommen att dela dem med Agora256-gemenskapen. Vi lär oss tillsammans för att bli bättre imorgon än vad vi är idag!