---
name: Bacca
description: Konfigurera en Ledger utan Ledger Live-programvara
---
![cover](assets/cover.webp)


Om du använder en Ledger har du förmodligen upptäckt att du måste gå igenom Ledger Live-programvaran, åtminstone för den första enhetskonfigurationen, för att kontrollera dess äkthet och installera Bitcoin-applikationen på den. Efter denna konfiguration föredrar dock många bitcoiners att använda specialiserad Bitcoin Wallet-hanteringsprogramvara som Sparrow eller Liana snarare än Ledger Live. Även om Ledger producerar utmärkta hårdvaruplånböcker som snabbt inkluderar de senaste Bitcoin-funktionerna, är deras programvara inte nödvändigtvis anpassad till bitcoiners specifika behov. Ledger Live innehåller faktiskt många funktioner som är utformade för altcoins, medan alternativen för Bitcoin Wallet-hantering är begränsade. Men problemet med Sparrow och Liana (för tillfället) är att de inte tillåter dig att installera Bitcoin-applikationen på Ledger.


För att kringgå behovet av att använda Ledger Live under den inledande konfigurationen av din Ledger kan du använda Bacca-verktyget (eller "Ledger Installer"). Med den här programvaran kan du installera och uppdatera Bitcoin-applikationen, verifiera äktheten hos din Ledger och även senare uppdatera enhetens firmware. Bacca skapades av Antoine Poinsot (Darosior), Bitcoin Core-utvecklare på Chaincode Labs, medgrundare [av Revault och Liana] (https://wizardsardine.com/) och Pythcoiner.


I den här handledningen visar jag dig hur du använder det här verktyget, så att du kan klara dig utan Ledger Live-programvara för gott och fortfarande njuta av Ledger-enheter. Det fungerar på alla enheter: Nano S Classic, Nano S Plus, Nano X, Flex och Stax.


---
*Observera att det här verktyget är ganska nytt och att dess utvecklare anger att det fortfarande är **i testfasen**. De rekommenderar att det endast används för teständamål och inte för en enhet som är avsedd att vara värd för en riktig Bitcoin Wallet, även om det är möjligt att göra det. I detta avseende rekommenderar jag att du följer rekommendationerna från utvecklarna av detta verktyg, som anges [på README i deras GitHub-arkiv](https://github.com/darosior/ledger_installer).*


---
## Förkunskapskrav


På din dator behöver du två verktyg för att använda Bacca:




- Git ;
- Rust.


Om du redan har installerat dem kan du hoppa över det här steget.


**Linux:**


På en Linux-distribution är Git i allmänhet förinstallerat. Om du vill kontrollera om Git är installerat på ditt system kan du skriva följande kommando i terminalen :


```bash
git --version
```


Om du inte har Git installerat på ditt system, här är kommandot för att installera det på en Debian :


```bash
sudo apt install git
```


Slutligen installerar du din Rust-utvecklingsmiljö genom att använda kommandot :


```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```


**Windows:**


För att installera Git, gå till [projektets officiella webbplats] (https://git-scm.com/). Ladda ner programvaran och följ installationsanvisningarna.


![BACCA](assets/fr/01.webp)


Fortsätt på samma sätt för att installera Rust från [den officiella webbplatsen] (https://www.Rust-lang.org/tools/install).


![BACCA](assets/fr/02.webp)


**MacOS:**


Om Git inte redan är installerat på ditt system öppnar du en terminal och kör följande kommando för att installera det:


```bash
git --version
```


Om Git inte är installerat på ditt system öppnas ett fönster som erbjuder dig att installera Xcode, som innehåller Git. Följ bara instruktionerna på skärmen för att fortsätta med installationen.


För att installera Rust kör du följande kommando:


```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```


## Bacca-installation


Öppna en terminal och gå till den mapp där du vill spara programvaran och kör sedan följande kommando:


```bash
git clone https://github.com/darosior/ledger_installer.git
```


Navigera till programvarukatalogen:


```bash
cd ledger_installer
```


Använd sedan Cargo för att kompilera projektet och köra Bacca GUI:


```bash
cargo run -p ledger_manager_gui
```


Du har nu tillgång till programvaran Interface.


![BACCA](assets/fr/03.webp)


## Konfigurera Ledger


Innan du börjar, om din Ledger är ny, se till att du har ställt in PIN-koden och sparat återställningsfrasen. Du behöver inte Ledger Live för dessa inledande steg. Anslut helt enkelt din Ledger via USB-kabeln för att driva den. Om du inte är säker på hur du ska gå vidare med dessa två steg kan du hänvisa till början av den handledning som är specifik för din modell:


https://planb.network/tutorials/wallet/hardware/ledger-c6fc7d82-91e7-4c74-bad7-cbff7fea7a88

https://planb.network/tutorials/wallet/hardware/ledger-nano-s-plus-75043cb3-2e8e-43e8-862d-ca243b8215a4

https://planb.network/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a

## Använda Bacca


Anslut din Ledger till din dator och lås upp den med den PIN-kod du har angett. Bacca bör automatiskt upptäcka din Ledger.


![BACCA](assets/fr/04.webp)


För att bekräfta att din Ledger är äkta klickar du på knappen "*Check*". Du måste auktorisera anslutningen på din Ledger-enhet för att fortsätta.


![BACCA](assets/fr/05.webp)


Bacca kommer sedan att informera dig om din Ledger är äkta. Om den inte är det indikerar detta antingen att enheten har äventyrats eller att den är en förfalskning. I så fall ska du omedelbart sluta använda den.


![BACCA](assets/fr/06.webp)


I menyn "*Apps*" kan du se en lista över de program som redan är installerade på din Ledger.


![BACCA](assets/fr/07.webp)


För att installera Bitcoin-applikationen klickar du på "*Install*" och godkänner sedan installationen på din Ledger.


![BACCA](assets/fr/08.webp)


Applikationen är väl installerad.


![BACCA](assets/fr/09.webp)


Om du inte har den senaste versionen av Bitcoin-programmet installerat kommer Bacca att visa en "*Uppdatera*"-knapp istället för "*Senaste*"-indikationen. Klicka bara på denna knapp för att uppdatera applikationen.


![BACCA](assets/fr/10.webp)


Nu när din Ledger är korrekt konfigurerad med den senaste versionen av Bitcoin-programmet är du redo att importera och använda din Wallet på hanteringsprogram som Sparrow eller Liana, utan att behöva gå igenom Ledger Live!


Om du tyckte att den här handledningen var användbar skulle jag vara tacksam om du lämnar en Green-tumme nedan. Dela gärna den här artikeln på dina sociala nätverk. Tack så mycket!


Jag rekommenderar också att du tar en titt på den här handledningen om GnuPG, som förklarar hur du kontrollerar integriteten och äktheten hos din programvara innan du installerar den. Detta är en viktig praxis, särskilt när du installerar Wallet-hanteringsprogramvara som Liana eller Sparrow :


https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc