---
name: GnuPG
description: Hur verifierar man programvarans integritet och äkthet?
---
![cover](assets/cover.webp)


När du laddar ner programvara är det mycket viktigt att se till att den inte har ändrats och att den verkligen kommer från den officiella källan. Detta gäller särskilt för programvara relaterad till Bitcoin, till exempel Wallet-programvara, som låter dig säkra nycklarna som ger tillgång till dina medel. I den här handledningen kommer vi att se hur man verifierar programvarans integritet och äkthet innan man installerar den. Vi kommer att använda Sparrow Wallet som ett exempel, en favorit Wallet-programvara bland bitcoiners, men proceduren kommer att vara densamma för alla andra programvaror.


Verifiering av integritet innebär att man säkerställer att den nedladdade filen inte har modifierats genom att jämföra dess digitala fingeravtryck (dvs. dess Hash) med det som tillhandahålls av den officiella utvecklaren. Om de två stämmer överens betyder det att filen är identisk med originalet och inte har korrumperats eller modifierats av en angripare.


Verifiering av äkthet å andra sidan säkerställer att filen verkligen kommer från den officiella utvecklaren och inte från en bedragare. Detta görs genom att verifiera en digital signatur. Signaturen bevisar att programvaran har signerats med den legitima utvecklarens privata nyckel.


Om dessa kontroller inte utförs finns det risk för att du installerar skadlig kod som kan innehålla modifierad kod. Den här koden kan antingen stjäla information som dina privata nycklar eller blockera åtkomsten till dina filer. Den här typen av attacker är ganska vanliga, särskilt i samband med programvara med öppen källkod där förfalskade versioner kan distribueras.


För att utföra denna verifiering kommer vi att använda två verktyg: hashfunktioner för att verifiera integritet och GnuPG, ett verktyg med öppen källkod som implementerar PGP-protokollet, för att verifiera äkthet.


## Förkunskapskrav


Om du använder **Linux** är GPG förinstallerat i de flesta distributioner. Om inte, kan du installera det med följande kommando:


```bash
sudo apt install gnupg
```


För **macOS**, om du inte redan har installerat Homebrew-pakethanteraren, gör du det med följande kommandon:


```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```


```bash
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
```


```bash
eval "$(/opt/homebrew/bin/brew shellenv)"
```


Installera sedan GPG med det här kommandot:


```bash
brew install gnupg
```

För **Windows**, om du inte har GPG, kan du installera programvaran [Gpg4win](https://www.gpg4win.org/).

![GnuPG](assets/notext/01.webp)


## Ladda ner dokument


Till att börja med behöver vi olika dokument. Besök den officiella webbplatsen för [Sparrow Wallet i avsnittet "*Download*"](https://sparrowwallet.com/download/). Om du vill verifiera en annan programvara, gå till den programvarans webbplats.


![GnuPG](assets/notext/02.webp)


Du kan också gå [till GitHub-arkivet för projektet] (https://github.com/sparrowwallet/sparrow/releases).


![GnuPG](assets/notext/03.webp)


Ladda ner installationsprogrammet för den programvara som motsvarar ditt operativsystem.


![GnuPG](assets/notext/04.webp)


Du behöver också filens Hash, som ofta kallas "*SHA256SUMS*" eller "*MANIFEST*".


![GnuPG](assets/notext/05.webp)


Ladda ner PGP-signaturen för filen också. Detta är dokumentet i `.asc`-format.


![GnuPG](assets/notext/06.webp)


Se till att placera alla dessa filer i samma mapp för de följande stegen.


Slutligen behöver du utvecklarens offentliga nyckel, som vi kommer att använda för att verifiera PGP-signaturen. Den här nyckeln finns ofta tillgänglig antingen på programvarans webbplats, på GitHub-arkivet för projektet, ibland på utvecklarens sociala medier eller på specialiserade webbplatser som Keybase. När det gäller Sparrow Wallet kan du hitta utvecklaren Craig Raw's offentliga nyckel [på Keybase] (https://keybase.io/craigraw). För att ladda ner den direkt från terminalen, kör kommandot:


```bash
curl https://keybase.io/craigraw/pgp_keys.asc | gpg --import
```


![GnuPG](assets/notext/07.webp)


## Verifiering av signatur


Processen för att verifiera signaturen är densamma på **Windows**, **macOS** och **Linux**. Normalt sett har du redan importerat den publika nyckeln under föregående steg, men om inte, gör det med kommandot:


```bash
gpg --import [key path]
```


Ersätt `[nyckelsökväg]` med platsen för utvecklarens offentliga nyckelfil.


![GnuPG](assets/notext/08.webp)


Verifiera signaturen med följande kommando:


```bash
gpg --verify [file.asc]
```


Ersätt `[file.asc]` med sökvägen till signaturfilen. I fallet Sparrow heter den här filen "*sparrow-2.0.0-manifest.txt.asc*" för version 2.0.0.


![GnuPG](assets/notext/09.webp)


Om signaturen är giltig kommer GPG att ange detta för dig. Du kan då gå vidare till nästa steg, eftersom detta bekräftar filens äkthet.


![GnuPG](assets/notext/10.webp)


## Verifiering av Hash

Nu när programvarans äkthet har bekräftats är det också nödvändigt att verifiera dess integritet. Vi kommer att jämföra programvarans Hash med den Hash som tillhandahålls av utvecklaren. Om de två stämmer överens garanterar det att programvarans kod inte har ändrats.


På **Windows** öppnar du en terminal och kör följande kommando:


```bash
CertUtil -hashfile [file path] SHA256 | findstr /v "hash"
```


Ersätt `[filsökväg]` med platsen för installationsprogrammet.


![GnuPG](assets/notext/11.webp)


Terminalen returnerar Hash för den nedladdade programvaran.


![GnuPG](assets/notext/12.webp)


Tänk på att det för viss programvara kan vara nödvändigt att använda en annan Hash-funktion än SHA256. I så fall ersätter du helt enkelt Hash-funktionens namn i kommandot.


Jämför sedan resultatet med motsvarande värde i filen "*sparrow-2.0.0-manifest.txt*".


![GnuPG](assets/notext/13.webp)


I mitt fall ser vi att de två hasharna matchar varandra perfekt.


På **macOS** och **Linux** är verifieringsprocessen för Hash automatiserad. Det är inte nödvändigt att manuellt kontrollera matchningen mellan de två hasharna som på Windows.


Kör helt enkelt detta kommando på **macOS**:


```bash
shasum --check [file name] --ignore-missing
```


Ersätt `[filnamn]` med namnet på installationsprogrammet. Till exempel för Sparrow Wallet:


```bash
shasum --check sparrow-2.0.0-manifest.txt --ignore-missing
```


Om hasharna matchar bör du se följande utdata:


```bash
Sparrow-2.0.0.dmg: OK
```


På **Linux** är kommandot liknande:


```bash
sha256sum --check [file name] --ignore-missing
```


Och om hasharna matchar bör du se följande utdata:


```bash
sparrow_2.0.0-1_amd64.deb: OK
```


Du är nu säker på att den programvara du har laddat ner är både äkta och intakt. Du kan fortsätta med installationen på din maskin.


Om du tyckte att den här handledningen var till hjälp skulle jag uppskatta tummen upp nedan. Dela gärna den här artikeln på dina sociala nätverk. Tack så mycket!


Jag rekommenderar också att du kollar in den här andra handledningen om VeraCrypt, en programvara som låter dig kryptera och dekryptera lagringsenheter.


https://planb.network/tutorials/computer-security/data/veracrypt-d5ed4c83-7c1c-4181-95ea-963fdf2d83c5