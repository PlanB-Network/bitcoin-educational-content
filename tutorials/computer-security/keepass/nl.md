---
name: KeePass
description: Hoe stel ik een lokale wachtwoordmanager in?
---
![cover](assets/cover.webp)


In het digitale tijdperk moeten we een groot aantal online accounts beheren voor verschillende aspecten van ons dagelijks leven, zoals bankieren, financiële platforms, e-mails, bestandsopslag, gezondheid, administratie, sociale netwerken, videogames, enz.


Om onszelf te authenticeren op elk van deze accounts, gebruiken we een identificatiecode, vaak een e-mail Address, vergezeld van een wachtwoord. Geconfronteerd met de onmogelijkheid om een groot aantal unieke wachtwoorden te onthouden, zou je in de verleiding kunnen komen om hetzelfde wachtwoord te hergebruiken of om een gemeenschappelijke basis lichtjes aan te passen om het gemakkelijker te onthouden. Deze praktijken brengen de veiligheid van je accounts echter ernstig in gevaar.


Het eerste principe voor wachtwoorden is om ze niet te hergebruiken. Elke online account moet worden beschermd door een uniek en volledig verschillend wachtwoord. Dit is belangrijk omdat, als een aanvaller erin slaagt om een van je wachtwoorden te kraken, je niet wilt dat hij toegang heeft tot al je accounts. Een uniek wachtwoord voor elk account isoleert potentiële aanvallen en beperkt hun bereik. Als je bijvoorbeeld hetzelfde wachtwoord gebruikt voor een videogame-platform en voor je e-mail en dat wachtwoord wordt gecompromitteerd via een phishingsite die gerelateerd is aan het gameplatform, dan kan de aanvaller gemakkelijk toegang krijgen tot je e-mail en controle krijgen over al je andere online accounts.


Het tweede essentiële principe is de sterkte van het wachtwoord. Een wachtwoord wordt als sterk beschouwd als het moeilijk te brute forceren is, dat wil zeggen, te raden met vallen en opstaan. Dit betekent dat je wachtwoorden zo willekeurig mogelijk moeten zijn, lang moeten zijn en een verscheidenheid aan tekens moeten bevatten (kleine letters, hoofdletters, cijfers en symbolen).


Het toepassen van deze twee beveiligingsprincipes voor wachtwoorden (uniekheid en robuustheid) kan moeilijk zijn in het dagelijks leven, omdat het bijna onmogelijk is om een uniek, willekeurig en sterk wachtwoord te onthouden voor al onze accounts. Dit is waar de wachtwoordmanager om de hoek komt kijken.


Een wachtwoordmanager genereert sterke wachtwoorden en slaat deze veilig op, zodat je toegang hebt tot al je online accounts zonder dat je ze afzonderlijk hoeft te onthouden. Je hoeft maar één wachtwoord te onthouden, het hoofdwachtwoord, waarmee je toegang hebt tot al je opgeslagen wachtwoorden in de manager. Het gebruik van een wachtwoordmanager verhoogt je online veiligheid omdat het hergebruik van wachtwoorden voorkomt en systematisch willekeurige wachtwoorden genereert. Maar het vereenvoudigt ook je dagelijkse gebruik van je accounts door de toegang tot je gevoelige informatie te centraliseren.

In deze tutorial leren we hoe je een lokale wachtwoordmanager instelt en gebruikt om je online beveiliging te verbeteren. Hier zal ik je kennis laten maken met KeePass. Als je echter een beginner bent en een online wachtwoordmanager wilt die op meerdere apparaten kan synchroniseren, raad ik je aan onze tutorial over Bitwarden te volgen:

https://planb.academy/tutorials/computer-security/authentication/bitwarden-0532f569-fb00-4fad-acba-2fcb1bf05de9

---

*Let op: Een wachtwoordmanager is geweldig voor het opslaan van wachtwoorden, maar **je mag er nooit de Mnemonic zin van je Bitcoin Wallet in opslaan!** Vergeet niet dat een Mnemonic zin uitsluitend moet worden opgeslagen in een fysiek formaat, zoals een stuk papier of metaal.*


---

## Inleiding tot KeePass


KeePass is een gratis en open-source wachtwoordmanager, perfect voor diegenen die een gratis en veilige oplossing willen voor lokaal beheer. Het is software die je op je pc installeert en die, zonder toevoeging van plugins, niet communiceert met het internet. Dit is een radicaal andere benadering dan die van Bitwarden, die we in een eerdere tutorial hebben behandeld. Bitwarden staat, in tegenstelling tot KeePass, synchronisatie over meerdere apparaten toe en vereist dus het opslaan van je wachtwoorden op een online server.


Standaard ondersteunt KeePass het gebruik van browserextensies zoals Bitwarden niet; daarom moet je je wachtwoorden handmatig kopiëren en plakken vanuit de software. Hoewel dit misschien een beperking lijkt, is het kopiëren en plakken van wachtwoorden in plaats van het gebruik van auto-fill een goede gewoonte voor uw online veiligheid.


KeePass is ontworpen om zowel licht als gebruiksvriendelijk te zijn, terwijl het voldoet aan hoge beveiligingsstandaarden. De software versleutelt je database lokaal voor optimale bescherming van je referenties. KeePass is ook de enige wachtwoordmanager die is gevalideerd door de ANSSI (de Franse cyberbeveiligingsautoriteit).


Een van de belangrijkste voordelen van KeePass is de flexibiliteit. Het kan op veel verschillende manieren gebruikt worden, zoals op een USB-stick zonder dat het op een computer geïnstalleerd hoeft te worden. Bovendien kan KeePass dankzij de [plugin-omgeving] (https://keepass.info/plugins.html) worden aangepast aan meer specifieke behoeften.

![KEEPASS](assets/notext/01.webp)

## Hoe KeePass downloaden?


Het installatieproces voor KeePass is afhankelijk van het besturingssysteem dat je gebruikt. Voor Windows- of Linux-gebruikers is de installatie relatief eenvoudig. Als u echter macOS gebruikt, is er een extra stap nodig vanwege de ontwikkeling van KeePass op het .NET-platform, dat niet direct wordt ondersteund door macOS. Daarom moet je een compatibele omgeving configureren om KeePass te laten draaien op Apple apparaten.


Gebruikers van Debian/Ubuntu openen de terminal en voeren de volgende commando's in:


```bash
sudo apt-get update

sudo apt-get install keepass2

```

For Fedora:

```

sudo dnf installeren keepass

```

For Arch Linux:

```

sudo pacman -S keepass

```

If you are on a Windows computer, go to the [official KeePass download page](https://keepass.info/download.html), and download the latest version of the installer:
![KEEPASS](assets/notext/02.webp)
Click on the downloaded file to run it, then follow the instructions of the setup wizard to complete the installation (see next section).

For macOS users, the installation is a bit more complex. If you wish to use the original version of KeePass as on Windows, follow the instructions below. Otherwise, you can opt for [KeePassXC](https://keepassxc.org/), an alternative version compatible with macOS, which offers a slightly different interface.

To use KeePass, you will need a runtime environment for .NET applications. I recommend installing Mono for this. Go to the [official Mono page](https://www.mono-project.com/download/stable/#download-mac) in the "*macOS*" section, and click on the link to download the installation package (`.pkg`).
![KEEPASS](assets/notext/03.webp)
Open the downloaded `.pkg` file and follow the instructions to install Mono on your Mac.
![KEEPASS](assets/notext/04.webp)
Next, go to the official KeePass website and download the latest portable version in `.zip` format.
![KEEPASS](assets/notext/05.webp)
After downloading the `.zip` file, double-click to extract it. You will get a folder containing several files, including `KeePass.exe`. Open a terminal, navigate to the KeePass folder (replace `xx` with the version number):

```

cd ~/Downloads/KeePass-2.xx

```

And finally, run KeePass with Mono:

```

mono KeePass.exe

```