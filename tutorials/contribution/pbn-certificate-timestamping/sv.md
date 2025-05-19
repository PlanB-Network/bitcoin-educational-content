---
name: Tidsstämpling av Plan ₿ Network-certifikat och -diplom
description: Förstå hur Plan ₿ Network utfärdar verifierbara bevis för dina certifikat och examensbevis
---

![cover](assets/cover.webp)


Om du läser detta är det stor sannolikhet att du har fått antingen ett ₿-CERT-testcertifikat eller ett diplom för en av de kurser du deltog i på planb.network, så grattis till denna prestation!


I den här handledningen kommer vi att upptäcka hur Plan ₿ Network utfärdar verifierbara bevis för ditt ₿-CERT-testcertifikat eller något diplom avseende kursavslutning. I en andra del kommer vi sedan att beskriva hur man verifierar äktheten hos dessa bevis.


# Plan ₿ Network bevismekanism


På Plan ₿ Network signerar vi kryptografiskt certifikat och diplom och tidsstämplar dem med hjälp av Timechain (dvs. Bitcoin Blockchain), genom en bevismekanism som bygger på två kryptografiska operationer:


1. En GPG-signatur på en textfil som sammanfattar dina prestationer

2. Tidsstämpling av samma signerade fil via [opentimestamps] (https://opentimestamps.org/).


Den första åtgärden gör att du kan bekräfta vem som har utfärdat certifikatet (eller diplomet), medan den andra åtgärden gör att du kan verifiera datumet för utfärdandet.

Vi anser att denna enkla bevismekanism ger oss möjlighet att utfärda certifikat och diplom med obestridliga bevis som vem som helst kan verifiera oberoende av varandra.


![image](./assets/proof-mechanism.webp)


Tack vare denna bevismekanism kommer varje försök att ändra även den minsta detalj i ditt certifikat eller examensbevis att resultera i en helt annan SHA-256 Hash av den signerade filen, vilket omedelbart avslöjar eventuell manipulering, eftersom både signaturen och Timestamp inte längre är giltiga. Om någon försöker att förfalska certifikat eller diplom på Plan ₿ Network:s vägnar kommer dessutom en enkel verifiering av signaturen att avslöja bedrägeriet.


## Hur fungerar GPG-signaturen?


GPG-signaturen genereras med hjälp av en programvara med öppen källkod som heter GNU Privacy Guard. Med den här programvaran kan användare enkelt skapa privata nycklar, signera och verifiera signaturer samt kryptera och dekryptera filer. I den här handledningen är det viktigt att notera att Plan ₿ Network använder GPG för att skapa sina privata/offentliga nycklar och för att signera alla ₿-CERT-certifikat och kursbevis.


Om någon däremot vill verifiera äktheten hos en signerad fil kan de använda GPG för att importera utfärdarens publika nyckel och verifiera den.


För den som är nyfiken och vill lära sig mer om denna fantastiska programvara kan du läsa ["The GNU Privacy Handbook"](https://www.gnupg.org/gph/en/manual/x135.html)


## Hur fungerar tidsstämpling?


Vem som helst kan använda OpenTimestamps för att Timestamp en fil och få verifierbart bevis på dess existens. Med andra ord ger det inte bevis på när filen skapades, utan snarare bevis på att filen existerade senast vid en viss tidpunkt.

OpenTimestamps tillhandahåller denna tjänst kostnadsfritt genom att använda en mycket effektiv metod för att lagra bevis i Bitcoin Blockchain. Den använder SHA-256 Hash-algoritmen för att skapa en unik identifierare för din fil och konstruerar en Merkle Tree med hjälp av hashvärdena för de filer som lämnats in av andra användare. Endast Hash i Merkle Tree-strukturen är förankrad i en OP_RETURN-transaktion, vilket garanterar ett säkert och kompakt sätt att verifiera filens existens.

När den här transaktionen kommer in i ett block kan alla med den ursprungliga filen och `.ots`-filen som är associerad med den verifiera tidsstämplingens autenticitet. I den andra delen av handledningen kommer vi att se hur du verifierar ditt Bitcoin-certifikat eller något diplom för kursavslutning genom en teminal och genom en grafisk Interface på webbplatsen för OpenTimestamps.


# Hur man verifierar ett Plan ₿ Network ₿-CERT-certifikat eller -diplom


## Steg 1. Ladda ner ditt certifikat eller examensbevis


Logga in på din personliga dashboard/student dashboard på planb.network.


![image](./assets/login.webp)


Gå till "Credentials" genom att klicka på menyn på vänster sida och välj din tentamensperiod eller ditt examensbevis.


![image](./assets/credential.webp)


Ladda ner zip-filen.


![image](./assets/download.webp)


Extrahera innehållet genom att högerklicka på filen `.zip` och välja "Extract". Du kommer att hitta tre olika filer:



- En signerad textfil (t.ex. certificate.txt)
- En OTS-fil (Open Timestamp) (t.ex. certifikat.txt.ots)
- Ett certifikat i PDF-format (t.ex. certificate.pdf)


## Steg 2: Hur kan du verifiera signaturen för textfilen?


Gå först till den mapp där du extraherade filerna och öppna en terminal (högerklicka på mappfönstret och klicka på "Öppna i terminal"). Följ sedan instruktionerna nedan.


1. Importera Plan ₿ Network:s offentliga PGP-nyckel med följande kommando:


```bash
curl -s https://raw.githubusercontent.com/Asi0Flammeus/pgp-public-keys/master/planb-network-pk.asc | gpg --import
```


Du bör se ett meddelande som följande om du har lyckats importera PGP-nyckeln


```
gpg: key 8F12D0C63B1A606E: public key "PlanB Network (used for PBN platform) <admin@planb.network>" imported
gpg: Total number processed: 1
gpg:               imported: 1
```


OBS: om du ser att 1 nyckel har bearbetats och 0 nycklar har importerats, betyder det troligen att du redan har importerat samma nyckel tidigare, vilket är helt okej.


2. Verifiera signaturen på certifikatet eller diplomet med hjälp av följande kommando:


```bash
gpg --verify certificate.txt
```


Detta kommando visar dig detaljer om signaturen, inklusive:



- Vem undertecknade det (Plan ₿ Network)
- När det undertecknades
- Om signaturen är giltig eller inte


Detta är ett exempel på resultatet:


```
gpg: Signature made lun 11 nov 2024, 00:39:04 CET
gpg:                using RSA key 5720CD577E7894C98DBD580E8F12D0C63B1A606E
gpg:                issuer "admin@planb.network"
gpg: Good signature from "PlanB Network (used for PBN platform) <admin@planb.network>" [unknown]
```


Om du ser ett meddelande som "BAD signature" betyder det att filen har manipulerats.


## Steg 3: Verifiera den öppna Timestamp


### Verifiering via en grafisk Interface


1. Besök OpenTimestamps webbplats: https://opentimestamps.org/

2. Klicka på fliken "Stamp & Verify".

3. Dra och släpp OTS-filen (t.ex. `certificate.txt.ots`) i det avsedda området.

4. Dra och släpp den tidsstämplade filen (t.ex. `certificate.txt`) i det avsedda området.

5. Webbplatsen kommer automatiskt att verifiera den öppna Timestamp och visa resultatet.


Om du ser ett meddelande som det följande är Timestamp giltigt:


![cover](assets/opentimestamp_wegui_verified.webp)


### CLI-metoden


OBS: denna procedur **kräver en igångvarande lokal Bitcoin-nod**


1. Installera OpenTimestamps-klienten från det officiella [repository] (https://github.com/opentimestamps/opentimestamps-client) genom att köra följande kommando:


```
pip install opentimestamps-client
```


2. Navigera till den katalog som innehåller de extraherade certifikatfilerna.


3. Kör följande kommando för att verifiera den öppna Timestamp:


```
ots verify certificate.txt.ots
```


Detta kommando kommer:



- Kontrollera Timestamp mot Bitcoin:s Blockchain
- Visa dig exakt när filen tidsstämplades
- Bekräfta Timestamp:s äkthet


### Slutliga resultat


Verifieringen är framgångsrik om **båda** följande meddelanden visas:


1. GPG-signaturen rapporteras som **"Bra signatur från Plan ₿ Network"**

2. OpenTimestamps-verifieringen visar ett specifikt Bitcoin-block Timestamp och rapporterar **"Framgång! Bitcoin-blocket [blockhöjd] intygar att data fanns från och med [Timestamp]"**


Nu när du vet hur Plan ₿ Network utfärdar verifierbara bevis för alla ₿-CERT-certifikat och -diplom kan du enkelt verifiera integriteten hos dem.