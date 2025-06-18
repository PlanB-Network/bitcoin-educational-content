---
name: BitBox02

description: Konfigurera och använda en BitBox02
---

![cover](assets/cover.webp)


BitBox02 (https://bitbox.swiss/) är en schweizisktillverkad fysisk Wallet som är särskilt utformad för att säkra dina Bitcoins. Några av dess viktigaste funktioner inkluderar enkel säkerhetskopiering och återställning med hjälp av ett microSD-kort, en minimalistisk och diskret design och omfattande stöd för Bitcoin.


![device](assets/1.webp)


Den erbjuder banbrytande säkerhet som tagits fram av experter, med en dubbelchipdesign som inkluderar ett säkert chip. Dess källkod har granskats fullständigt av säkerhetsforskare och är helt öppen källkod. BitBox02 levereras med en enkel men kraftfull BitBoxApp, som ger säker hantering av dina Bitcoins. Den stöder Full node för Bitcoin och säkerställer end-to-end-krypterad kommunikation mellan appen och enheten. BitBox02 är tillverkad i Schweiz och har fått ett positivt rykte bland sina användare.


![video](https://youtu.be/sB4b2PbYaj0)


Här är specifikationerna för Wallet:



- Anslutningsmöjligheter: USB-C
- Kompatibilitet med: Windows 7 och senare, macOS 10.13 och senare, Linux, Android
- Ingång: Kapacitiva touchsensorer
- Mikrokontroller: ATSAMD51J20A; 120 Mhz 32-bitars Cortex-M4F; sann slumptalsgenerator
- Säkert chip: ATECC608B; Sann slumptalsgenerator (NIST SP 800-90A/B/C)
- Display: 128 x 64 px vit OLED
- Material:: Polykarbonat
- Storlek: 54,5 x 25,4 x 9,6 mm inklusive USB-C-kontakt
- Vikt: Apparat Enhet 12g; med förpackning och tillbehör 160g


Ladda ner datablad på deras hemsida https://bitbox.swiss/bitbox02/


## Så här använder du BitBox02 Hardware Wallet


### Konfigurera BitBox02


BitBox02 har en USB-C-anslutning som är fäst vid skalet. Om din dator använder den vanliga USB-porten måste du använda adaptern som medföljer enheten.


Anslut den till din dator och enheten slås på (gör det inte än).


Den har sensorer ovanför och nedanför, och den kommer att uppmana dig att röra vid toppen eller botten för att orientera skärmen på det sätt du vill.


![image](assets/2.webp)


### Ladda ner BitBox02-appen


Besök https://shiftcrypto.ch/ och klicka på länken "App" högst upp för att komma till nedladdningssidan:


![image](assets/3.webp)


Klicka på den blå Download-knappen:


![image](assets/4.webp)


För att verifiera nedladdningen (det gör det mer komplicerat, men rekommenderas, särskilt om du lagrar många Bitcoin), se Bilaga A.


Efter nedladdningen kan du packa upp filen. På en Mac dubbelklickar du bara på den nedladdade filen, så visas en BitBox App-ikon i din nedladdningskatalog. Du kan dra den till skrivbordet (eller var som helst) för enkel åtkomst.


Dubbelklicka på appen för att köra den (den blir inte "installerad").


På Mac kommer din datananny att ge dig en varning. Ignorera den bara och klicka på "öppna":


![image](assets/5.webp)


Du kommer då att se detta:


![image](assets/6.webp)


Gå vidare och anslut enheten till datorn.


Den visar en parningskod. Kontrollera att de matchar och tryck sedan på sensorn för att markera kryssmarkeringen. När du sedan återvänder till skärmen blir fortsättningsknappen tillgänglig för dig.


![image](assets/7.webp)


Du får då möjlighet att skapa en ny seed eller återställa en seed. Jag ska demonstrera hur du skapar en ny seed (det är viktigt att du också återställer den seed du skapade för att testa kvaliteten på din säkerhetskopia innan du laddar någon Bitcoin på Wallet).


![image](assets/8.webp)


Enheten levererades med ett microSD-kort. Sätt i det om du inte har det.


![image](assets/9.webp)


Namnge din enhet och klicka på Fortsätt, bekräfta sedan på enheten.


![image](assets/10.webp)


Du kommer sedan att bli ombedd att ange ett lösenord för enheten. Detta är inte en del av din seed. Det är inte heller en passphrase (det är en del av din seed). Det är helt enkelt ett lösenord för att låsa enheten. När du slår på enheten kommer du att bli ombedd att ange detta lösenord varje gång. Du har 10 misslyckanden i följd innan enheten kommer att radera sig själv från allt minne, så var försiktig. Animationen på skärmen visar dig hur du använder enhetens kontroller för att ställa in lösenordet.


![image](assets/11.webp)


Läs nästa sida, kryssa i alla rutor och fortsätt sedan.


![image](assets/12.webp)

![image](assets/13.webp)

![image](assets/14.webp)


Och så här ser Wallet ut när den är klar att användas.


![image](assets/15.webp)


### INTE SÅ SNABBT!!!


Det är ganska konstigt, men BitBox02 säger till oss att vi är redo att använda enheten, men den har inte uppmanat oss att skriva ner seed-orden! Den ENDA säkerhetskopian vi har är filen som sparats på microSD-kortet. Detta är otillräckligt. Dessa lagringsenheter håller inte för evigt (på grund av "bitrot"). Vi behöver en pappersbackup och duplikat som förvaras i ett kassaskåp (som förklaras i den allmänna guiden om hur man använder hårdvaruplånböcker)


För att få vår seed-fras och skriva ner den, gå till fliken "hantera enhet" till vänster och klicka sedan på "visa återställningsord"


![image](assets/16.webp)


Du kan sedan gå igenom bekräftelsen, och enheten kommer att presentera orden för dig. Skriv ner dem prydligt och låt aldrig någon se orden.


![image](assets/17.webp)


Därefter kan du klicka på fliken Bitcoin till vänster för att få dina mottagningsadresser.


![image](assets/18.webp)


Den visar en i taget, men låter dig åtminstone välja vilken Address du vill använda bland de första 20:


![image](assets/19.webp)


Om du klickar på den blå knappen visas hela Address, och du uppmanas att kontrollera att Address matchar det som visas på skärmen. Det här är bra praxis för att bekräfta att ingen skadlig kod på din dator lurar dig att skicka Bitcoin till en angripares Address.


![image](assets/20.webp)


För att skicka Bitcoin till detta Wallet kan du kopiera Address och klistra in den på uttagssidan för Exchange där dina mynt finns. Jag rekommenderar att du skickar ett litet testbelopp först och sedan övar på att spendera det antingen tillbaka till Exchange eller till den andra Address i din Wallet.


För större mängder föreslår jag att du skapar en passphrase (se nedan). Den ursprungliga Wallet (ingen passphrase) kan användas som ditt lockbete Wallet (det måste finnas en rimlig mängd i den för att det ska vara ett trovärdigt lockbete).


### Anslut till en nod


BitBox02 kommer automatiskt att ansluta till en nod. Låt oss se var den ansluter till. Klicka på fliken Inställningar till vänster och sedan på "Anslut din egen Full node".


![image](assets/21.webp)


Och här kan vi se att den ansluter till shiftcryptos nod. Inte så bra. Vi har förrått alla våra Bitcoin-adresser till dem, och vår IP Address (inte seed naturligtvis; de kan se våra adresser/balanser, men kan inte spendera dem). Vi kan ange våra egna noddetaljer på den här sidan (utanför ramen för den här guiden), eller så kan vi använda bättre programvara som Sparrow Bitcoin Wallet, Electrum Desktop Wallet eller Specter Desktop. Jag kommer att demonstrera Sparrow Bitcoin Wallet senare i guiden.


![image](assets/22.webp)


Lägg till en passphrase


Nu när vi har konfigurerat enheten med BitBox02-appen (och avslöjat våra adresser, vilket är oundvikligt med just denna Hardware Wallet) kan vi lägga till en passphrase till vår seed-fras. Detta gör att vi kan skapa en ny Wallet med samma seed, och ShiftCrypto kommer aldrig att se våra nya adresser. Vi kommer endast att ansluta denna Wallet till vår egen programvara.


### Aktivera passphrase


Gå vidare nu och "aktivera" passphrase-funktionen (men vi ställer inte in en passphrase ännu). Gå till fliken "Hantera enhet" och klicka på "Aktivera passphrase" (röd cirkel nedan).


![image](assets/23.webp)


Läs igenom stegen..


![image](assets/24.webp)

![image](assets/25.webp)

![image](assets/26.webp)


Koppla nu bort enheten och stäng av BitBox02-appen


Avslutning av avsnittet bitbox02 av Parman.


Din divice är nu fullt fungerande och kan användas på alla skrivbordslösningar som specter, sparrow och med bitboxen Interface.