---
name: GnuPG
description: Hoe controleer je de integriteit en authenticiteit van software?
---
![cover](assets/cover.webp)


Als je software downloadt, is het heel belangrijk dat je zeker weet dat het niet veranderd is en dat het inderdaad van de officiële bron komt. Dit geldt vooral voor software die gerelateerd is aan Bitcoin, zoals Wallet software, waarmee je de sleutels kunt beveiligen die toegang geven tot je fondsen. In deze tutorial zullen we zien hoe je de integriteit en authenticiteit van software kunt controleren voordat je het installeert. We gebruiken Sparrow wallet als voorbeeld, een favoriete Wallet software onder bitcoiners, maar de procedure is hetzelfde voor elke andere software.


Het verifiëren van de integriteit houdt in dat wordt gecontroleerd of het gedownloade bestand niet is gewijzigd door de digitale vingerafdruk (Hash) te vergelijken met die van de officiële ontwikkelaar. Als de twee overeenkomen, betekent dit dat het bestand identiek is aan het origineel en niet is beschadigd of gewijzigd door een aanvaller.


Het verifiëren van de authenticiteit, aan de andere kant, zorgt ervoor dat het bestand inderdaad afkomstig is van de officiële ontwikkelaar en niet van een bedrieger. Dit wordt gedaan door een digitale handtekening te verifiëren. Deze handtekening bewijst dat de software is ondertekend met de privésleutel van de legitieme ontwikkelaar.


Als deze controles niet worden uitgevoerd, bestaat het risico dat er malware wordt geïnstalleerd die gewijzigde code kan bevatten. Deze code kan informatie stelen zoals je privésleutels of de toegang tot je bestanden blokkeren. Dit soort aanvallen komt vaak voor, vooral in de context van open source software waar vervalste versies kunnen worden verspreid.


Om deze verificatie uit te voeren zullen we twee tools gebruiken: hashingfuncties om de integriteit te verifiëren en GnuPG, een open-source tool die het PGP-protocol implementeert, om de authenticiteit te verifiëren.


## Vereisten


Als je **Linux** gebruikt, is GPG vooraf geïnstalleerd op de meeste distributies. Zo niet, dan kun je het installeren met het volgende commando:


```bash
sudo apt install gnupg
```


Voor **macOS**, als je de Homebrew package manager nog niet hebt geïnstalleerd, doe dat dan met de volgende commando's:


```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```


```bash
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
```


```bash
eval "$(/opt/homebrew/bin/brew shellenv)"
```


Installeer dan GPG met dit commando:


```bash
brew install gnupg
```

Voor **Windows**, als u geen GPG heeft, kunt u de software [Gpg4win](https://www.gpg4win.org/) installeren.

![GnuPG](assets/notext/01.webp)


## Documenten downloaden


Om te beginnen hebben we verschillende documenten nodig. Bezoek de officiële site van [Sparrow wallet in de sectie "*Download*"] (https://sparrowwallet.com/download/). Als je een andere software wilt verifiëren, ga dan naar de website van die software.


![GnuPG](assets/notext/02.webp)


Je kunt ook naar [de GitHub repository van het project] gaan (https://github.com/sparrowwallet/Sparrow/releases).


![GnuPG](assets/notext/03.webp)


Download het installatieprogramma voor de software die overeenkomt met je besturingssysteem.


![GnuPG](assets/notext/04.webp)


Je hebt ook de Hash van het bestand nodig, vaak "*SHA256SUMS*" of "*MANIFEST*" genoemd.


![GnuPG](assets/notext/05.webp)


Download ook de PGP-handtekening van het bestand. Dit is het document in `.asc` formaat.


![GnuPG](assets/notext/06.webp)


Zorg ervoor dat je al deze bestanden in dezelfde map plaatst voor de volgende stappen.


Tot slot heb je de publieke sleutel van de ontwikkelaar nodig, die we zullen gebruiken om de PGP-handtekening te verifiëren. Deze sleutel is vaak beschikbaar op de website van de software, op de GitHub repository van het project, soms op de sociale media van de ontwikkelaar, of op gespecialiseerde sites zoals Keybase. In het geval van Sparrow wallet kun je de publieke sleutel van ontwikkelaar Craig Raw vinden [op Keybase] (https://keybase.io/craigraw). Om het direct vanaf de terminal te downloaden, voert u het commando uit:


```bash
curl https://keybase.io/craigraw/pgp_keys.asc | gpg --import
```


![GnuPG](assets/notext/07.webp)


## De handtekening verifiëren


Het proces om de handtekening te verifiëren is hetzelfde op **Windows**, **macOS** en **Linux**. Normaal gesproken heeft u de publieke sleutel al geïmporteerd tijdens de vorige stap, maar als dat niet het geval is, kunt u dat doen met het commando:


```bash
gpg --import [key path]
```


Vervang `[sleutelpad]` door de locatie van het openbare sleutelbestand van de ontwikkelaar.


![GnuPG](assets/notext/08.webp)


Controleer de handtekening met het volgende commando:


```bash
gpg --verify [file.asc]
```


Vervang `[file.asc]` door het pad van het handtekeningbestand. In het geval van Sparrow heet dit bestand "*Sparrow-2.0.0-manifest.txt.asc*" voor versie 2.0.0.


![GnuPG](assets/notext/09.webp)


Als de handtekening geldig is, zal GPG dit aangeven. U kunt dan doorgaan naar de volgende stap, omdat dit de authenticiteit van het bestand bevestigt.


![GnuPG](assets/notext/10.webp)


## De Hash controleren

Nu de authenticiteit van de software is bevestigd, is het ook nodig om de integriteit te controleren. We vergelijken de Hash van de software met de Hash van de ontwikkelaar. Als de twee overeenkomen, is gegarandeerd dat de softwarecode niet is gewijzigd.


Open op **Windows** een terminal en voer het volgende commando uit:


```bash
CertUtil -hashfile [file path] SHA256 | findstr /v "hash"
```


Vervang `[bestandspad]` door de locatie van het installatieprogramma.


![GnuPG](assets/notext/11.webp)


De terminal geeft de Hash van de gedownloade software terug.


![GnuPG](assets/notext/12.webp)


Voor sommige software kan het nodig zijn om een andere Hash functie dan SHA256 te gebruiken. Vervang in dat geval gewoon de naam van de Hash functie in het commando.


Vergelijk vervolgens het resultaat met de corresponderende waarde in het bestand "*Sparrow-2.0.0-manifest.txt*".


![GnuPG](assets/notext/13.webp)


In mijn geval zien we dat de twee hashes perfect overeenkomen.


Op **macOS** en **Linux** is het Hash verificatieproces geautomatiseerd. Het is niet nodig om handmatig te controleren of de twee hashes overeenkomen zoals op Windows.


Voer gewoon dit commando uit op **macOS**:


```bash
shasum --check [file name] --ignore-missing
```


Vervang `[bestandsnaam]` door de naam van het installatieprogramma. Bijvoorbeeld voor Sparrow wallet:


```bash
shasum --check sparrow-2.0.0-manifest.txt --ignore-missing
```


Als de hashes overeenkomen, zou je de volgende uitvoer moeten zien:


```bash
Sparrow-2.0.0.dmg: OK
```


Op **Linux** is het commando vergelijkbaar:


```bash
sha256sum --check [file name] --ignore-missing
```


En als de hashes overeenkomen, zou je de volgende uitvoer moeten zien:


```bash
sparrow_2.0.0-1_amd64.deb: OK
```


Je bent er nu zeker van dat de software die je hebt gedownload zowel authentiek als intact is. Je kunt doorgaan met de installatie ervan op je machine.


Als je deze handleiding nuttig vond, zou ik een duim omhoog hieronder op prijs stellen. Voel je vrij om dit artikel te delen op je sociale netwerken. Hartelijk dank!


Ik raad ook aan om deze andere tutorial over VeraCrypt te bekijken, een software waarmee je opslagapparaten kunt versleutelen en ontsleutelen.


https://planb.network/tutorials/computer-security/data/veracrypt-d5ed4c83-7c1c-4181-95ea-963fdf2d83c5