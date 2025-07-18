---
name: KeePass
description: Hur ställer man in en lokal lösenordshanterare?
---
![cover](assets/cover.webp)


I den digitala tidsåldern måste vi hantera en mängd onlinekonton som täcker olika aspekter av vårt dagliga liv, inklusive bank, finansiella plattformar, e-post, fillagring, hälsa, administration, sociala nätverk, videospel etc.


För att autentisera oss på vart och ett av dessa konton använder vi en identifierare, ofta en e-post Address, tillsammans med ett lösenord. Eftersom det är omöjligt att memorera ett stort antal unika lösenord kan man frestas att återanvända samma lösenord eller att ändra en gemensam bas något för att göra det lättare att komma ihåg. Dessa metoder äventyrar dock allvarligt säkerheten för dina konton.


Den första principen för lösenord är att inte återanvända dem. Varje onlinekonto bör skyddas av ett unikt och helt distinkt lösenord. Det här är viktigt eftersom du inte vill att en angripare ska ha tillgång till alla dina konton om han eller hon lyckas komma över ett av dina lösenord. Genom att ha ett unikt lösenord för varje konto isoleras potentiella attacker och deras räckvidd begränsas. Om du till exempel använder samma lösenord för en videospelplattform och för din e-post, och det lösenordet avslöjas via en nätfiskewebbplats som är relaterad till spelplattformen, kan angriparen enkelt komma åt din e-post och ta kontroll över alla dina andra onlinekonton.


Den andra viktiga principen är lösenordets styrka. Ett lösenord anses vara starkt om det är svårt att brute force, det vill säga att gissa sig till genom försök och misstag. Det innebär att dina lösenord måste vara så slumpmässiga som möjligt, långa och innehålla en mängd olika tecken (små och stora bokstäver, siffror och symboler).


Att tillämpa dessa två principer för lösenordssäkerhet (unikhet och robusthet) kan visa sig vara svårt i vardagen, eftersom det är nästan omöjligt att memorera ett unikt, slumpmässigt och starkt lösenord för alla våra konton. Det är här lösenordshanteraren kommer in i bilden.


En lösenordshanterare genererar och lagrar starka lösenord på ett säkert sätt, vilket gör att du kan komma åt alla dina onlinekonton utan att behöva memorera dem individuellt. Du behöver bara komma ihåg ett lösenord, huvudlösenordet, som ger dig tillgång till alla dina sparade lösenord i hanteringen. Att använda en lösenordshanterare förbättrar din säkerhet online eftersom den förhindrar återanvändning av lösenord och systematiskt genererar slumpmässiga lösenord. Men det förenklar också din dagliga användning av dina konton genom att centralisera åtkomsten till din känsliga information.

I den här handledningen lär vi oss hur man ställer in och använder en lokal lösenordshanterare för att förbättra din online-säkerhet. Här kommer jag att introducera dig till KeePass. Men om du är nybörjare och vill ha en lösenordshanterare online som kan synkroniseras mellan flera enheter rekommenderar jag att du följer vår handledning om Bitwarden:

https://planb.network/tutorials/computer-security/authentication/bitwarden-0532f569-fb00-4fad-acba-2fcb1bf05de9

---

*Varning för detta: En lösenordshanterare är bra för att lagra lösenord, men **du ska aldrig lagra din Bitcoin Wallet:s Mnemonic-fras i den!** Kom ihåg att en Mnemonic-fras uteslutande ska sparas i ett fysiskt format, som ett papper eller metall.*


---

## Introduktion till KeePass


KeePass är en gratis lösenordshanterare med öppen källkod, perfekt för dig som vill ha en gratis och säker lösning för lokal hantering. Det är programvara som ska installeras på din dator som, utan tillägg av plugins, inte kommunicerar med Internet. Detta är ett radikalt annorlunda tillvägagångssätt än Bitwarden, som vi behandlade i en tidigare handledning. Bitwarden, till skillnad från KeePass, tillåter synkronisering mellan flera enheter och kräver därför att du lagrar dina lösenord på en onlineserver.


Som standard stöder KeePass inte användningen av webbläsartillägg som Bitwarden; därför måste du manuellt kopiera och klistra in dina lösenord från programvaran. Även om detta kan verka som en begränsning är det en bra praxis för din online-säkerhet att kopiera och klistra in lösenord snarare än att använda automatisk fyllning.


KeePass är utformat för att vara både lättviktigt och enkelt att använda, samtidigt som det följer höga säkerhetsstandarder. Programvaran krypterar din databas lokalt för optimalt skydd av dina inloggningsuppgifter. KeePass är också den enda lösenordshanteraren som validerats av ANSSI (den franska cybersäkerhetsmyndigheten).


En av de största fördelarna med KeePass är dess flexibilitet. Det kan användas på många olika sätt, t.ex. på ett USB-minne utan att behöva installeras på en dator. Tack vare sin [plugin-miljö] (https://keepass.info/plugins.html) kan KeePass dessutom anpassas för att uppfylla mer specifika behov.

![KEEPASS](assets/notext/01.webp)

## Hur laddar jag ner KeePass?


Installationsprocessen för KeePass varierar beroende på vilket operativsystem du använder. För Windows- eller Linux-användare är installationen relativt enkel. Om du använder macOS krävs dock ytterligare ett steg eftersom KeePass utvecklas på .NET-plattformen, som inte stöds direkt av macOS. Därför måste du konfigurera en kompatibel miljö för att KeePass ska kunna köras på Apple-enheter.


För Debian/Ubuntu-användare öppnar du terminalen och skriver in följande kommandon:


```bash
sudo apt-get uppdatering

sudo apt-get installera keepass2

```

For Fedora:

```

sudo dnf installera keepass

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