---
name: Linux Mint

description: Een computer instellen voor Bitcoin transacties
---

![image](assets/cover.webp)


## Wat is er mis als je een gewone computer gebruikt?


Als je Bitcoin transacties doet, is het ideaal als je computer geen malware heeft. Uiteraard.


Als je je Bitcoin seed zin (meestal 12 of 24 woorden) buiten de computer houdt met een ondertekeningsapparaat (bijvoorbeeld een Hardware Wallet - het hoofddoel), dan denk je misschien dat het niet zo belangrijk is om een "schone" computer te hebben - niet waar.


Een met malware besmette computer kan je Bitcoin adressen lezen en zo je saldo blootstellen aan een aanvaller - ze kunnen geen Bitcoin nemen door alleen de Address te kennen, maar ze kunnen wel zien hoeveel je hebt en op basis daarvan berekenen of je een waardig doelwit bent. Ze kunnen er bijvoorbeeld ook achter komen waar je woont en je vingernagels of kinderen afnemen om je losgeld te laten betalen.


## Wat is de oplossing?


Ik raad de meeste Bitcoiners aan om een speciale malwarevrije computer (met internettoegang) te gebruiken voor het doen van Bitcoin transacties. Ik raad mensen aan een open-source besturingssysteem te gebruiken zoals Linux Mint, maar gebruik Windows of Mac als het moet - dat is beter dan een gewone, goed gebruikte computer waar altijd malware in verstopt zit.


Een obstakel dat mensen tegenkomen is het installeren van een nieuw besturingssysteem op zulke computers. Deze gids helpt daarbij.


Er zijn veel Linux-varianten en ik heb er verschillende geprobeerd. Mijn aanbeveling voor Bitcoiners is Linux Mint, omdat het makkelijk te installeren is, erg snel (vooral bij het opstarten en afsluiten), niet opgeblazen (elk extra stukje software is een risico), en het is zelden gecrasht of heeft zich raar gedragen (vergeleken met andere versies zoals Ubuntu en Debian).


Sommigen zijn misschien erg tegen een nieuw besturingssysteem en geven de voorkeur aan Windows of Mac OS. Dat begrijp ik, maar de besturingssystemen van Windows en Apple zijn closed source, dus we moeten vertrouwen op wat ze doen; ik denk niet dat dat een goed beleid is, maar het is niet alles of niets. Ik heb veel liever dat mensen een vers geïnstalleerde Windows of Mac OS computer gebruiken dan een goed gebruikte computer (met wie weet wat voor malware erop). Een stap beter is om een vers geïnstalleerde Linux computer te gebruiken, wat ik zal demonstreren.


Als je zenuwachtig bent om Linux te gebruiken vanwege het onbekende, is dat normaal, maar het is ook goed om wat tijd te besteden om het te leren. Er is zoveel informatie online beschikbaar. Hier is een uitstekende korte video die de basisprincipes van de commandoregel introduceert en die ik ten zeerste aanbeveel.

Kies een computer


Ik zal beginnen met wat ik denk dat de beste optie is. Daarna geef ik mijn mening over alternatieven.


Ideale optie:


Mijn aanbeveling, als je het je kunt veroorloven en als de grootte van je Bitcoin stack het rechtvaardigt, is om een gloednieuwe instapmodel laptop te kopen. Het meest eenvoudige model dat tegenwoordig gebouwd wordt, is goed genoeg voor waar het voor gebruikt gaat worden. De processor en RAM specificaties zijn niet relevant, omdat ze allemaal goed genoeg zijn.


Vermijden:



- Elke tabletcombinatie, inclusief Surface Pro
- Chromebooks - vaak is de opslagcapaciteit te laag
- Elke computer met een eMMC-schijf; als deze een SSD-schijf heeft, is dat perfect
- Macs - ze zijn duur en de hardware werkt in mijn ervaring niet goed samen met Linux-besturingssystemen


Zoek in plaats daarvan naar een Windows 11 laptop (momenteel is Windows 11 de nieuwste versie. We raken die software wel kwijt, maak je geen zorgen). Ik heb op amazon.com gezocht naar "Windows 11 Laptop" en vond dit goede voorbeeld:


![image](assets/1.webp)


De prijs van deze hierboven is goed. De specificaties zijn goed genoeg. Het heeft een ingebouwde camera die we kunnen gebruiken voor QR-code PSBT transacties (anders zou je een USB-camera moeten kopen om dat te doen). Maak je geen zorgen over het feit dat het geen bekend merk is (het is goedkoop). Als je een beter merk wilt, kost het je bijv:


![image](assets/2.webp)


Sommige goedkopere laptops hebben slechts 64Gb aan schijfruimte; ik heb geen laptops met zulke kleine schijven getest - waarschijnlijk is 64Gb OK, maar het is misschien wat overdreven.


## Andere opties - Staarten


Tails is een besturingssysteem dat opstart vanaf een USB-stick en tijdelijk de hardware van een computer overneemt. Het maakt alleen gebruik van Tor-verbindingen, dus je moet vertrouwd zijn met het gebruik van Tor. Geen van de gegevens die je naar het geheugen schrijft tijdens je sessie wordt opgeslagen op de schijf (het begint elke keer opnieuw) tenzij je de instellingen aanpast en een permanente opslagmogelijkheid maakt (op de USB-stick) - die je vergrendelt met een wachtwoord.


Het is geen slechte optie en het is gratis, maar het is een beetje onhandig voor ons doel. Het installeren van nieuwe software is geen makkie. Een goede eigenschap is dat het wordt geleverd met Electrum, maar het nadeel hiervan is dat je het niet zelf hebt geïnstalleerd. Zorg ervoor dat de USB-schijf die je gebruikt minstens 8Gb is.


Je flexibiliteit wordt verminderd als je Tails gebruikt. Het kan zijn dat je verschillende gidsen niet kunt volgen om in te stellen wat je nodig hebt en het goed werkend te krijgen. Als je bijvoorbeeld mijn gids voor het installeren van Bitcoin core volgt, zijn er aanpassingen nodig om het te laten werken. Ik denk niet dat ik een specifieke Tails gids zal maken, dus je moet je vaardigheden opbouwen en het alleen doen.


Ik weet ook niet zeker hoe goed hardware wallets zullen samenwerken met dit OS.


Dit gezegd hebbende, een Tails computer voor Bitcoin transacties is een leuke extra optie, en zal zeker helpen bij je algehele privacy vaardigheden om Tails te leren gebruiken.


## Andere opties - Live OS Boot


Dit lijkt erg op Tails, behalve dat het besturingssysteem niet privacy-afhankelijk is. De basismanier om dit te gebruiken is om een USB-stick te flashen met het Linux-besturingssysteem van je keuze en de computer daarvan te laten opstarten in plaats van de interne schijf. Hoe je dit doet wordt later uitgelegd.


Het voordeel is dat je minder beperkingen hebt en dat dingen werken zonder geavanceerde tweaks.


Ik weet niet zeker hoe goed zo'n systeem malware op de bestaande computer isoleert van de USB boot drive die je gebruikt voor het nieuwe besturingssysteem. Het doet waarschijnlijk prima werk en is waarschijnlijk niet zo goed als Tails. Omdat ik het niet weet, gaat mijn voorkeur uit naar de dedicated laptop.

Andere opties - Je eigen gebruikte laptop of desktopcomputer


Het gebruik van een gebruikte computer is niet ideaal, vooral omdat ik niet op de hoogte ben van de innerlijke werking van geavanceerde malware en ook niet of het wissen van een schijf voldoende is om er vanaf te komen. Waarschijnlijk wel, maar ik wil niet onderschatten hoe slim snode hackers kunnen zijn. Jij mag beslissen, ik wil me niet binden.


Als je ervoor kiest om een oude desktop te gebruiken in plaats van een oude laptop, is dit prima, behalve dat het permanent ruimte inneemt voor je waarschijnlijk zeldzame Bitcoin transacties; je zou het nergens anders voor moeten gebruiken. Met een laptop kun je hem gewoon opbergen en zelfs verstoppen voor extra veiligheid.


## Linux Mint installeren op elke computer


Dit zijn instructies om elk besturingssysteem van je nieuwe laptop te wissen en Linux Mint te installeren, maar je kunt het aanpassen om zowat elke Linux-versie op zowat elke computer te installeren.


We gaan een willekeurige computer gebruiken om het besturingssysteem naar een geheugenstick te flashen. Het maakt niet uit welke geheugenstick, zolang het maar compatibel is met een USB-poort, en ik stel voor minimaal 16Gb.


Koop een van deze dingen:


![image](assets/3.webp)


Of je kunt iets als dit gebruiken:


![image](assets/4.webp)


Navigeer vervolgens naar linuxmint.com


![image](assets/5.webp)


Beweeg de muis over het Download menu bovenaan en klik dan op de link, "Linux Mint 20.3" of welke versie dan ook de laatste aanbevolen versie is op het moment dat je dit doet.


![image](assets/6.webp)


Er zijn een paar "smaken" om uit te kiezen. Kies voor "Cinnamon" om deze handleiding te volgen. Klik op de knop Downloaden.


![image](assets/7.webp)


Op de volgende pagina kun je naar beneden scrollen om de mirrors te zien (Mirrors zijn verschillende servers die een kopie hebben van het bestand dat we willen). Je kunt de download verifiëren met SHA256 en gpg (aanbevolen), maar ik sla dat hier over omdat ik hier al gidsen over heb geschreven.


![image](assets/8.webp)


Kies een mirror die het dichtst bij je in de buurt is en klik op de link (de Green tekst in de spiegelkolom). Het bestand begint te downloaden - de versie die ik download is 2,1 gigabyte.


Zodra het is gedownload, kun je het bestand flashen naar een draagbaar geheugenapparaat en het opstartbaar maken. De eenvoudigste manier om dit te doen is door Balena Etcher te gebruiken. Download en installeer het als je het nog niet hebt.


Voer het dan uit:


![image](assets/9.webp)


Klik op flash from file en selecteer het LinuxMint-bestand dat je hebt gedownload.


Klik vervolgens op Select target (Doel selecteren). Zorg ervoor dat het geheugenapparaat is aangesloten en dat je de juiste schijf selecteert, anders kun je de inhoud van de verkeerde schijf vernietigen!


Selecteer daarna Flash! Mogelijk moet u uw wachtwoord invoeren. Wanneer het klaar is, zal de schijf waarschijnlijk niet leesbaar zijn door je Windows of Mac computer omdat het getransformeerd is in een Linux apparaat. Trek het er gewoon uit.

De doelcomputer voorbereiden


Zet de nieuwe laptop aan en terwijl hij aan staat, houd je de BIOS-toets ingedrukt. Dit is meestal F2, maar het kan ook F1, F8, F10, F11, F12 of Delete zijn. Probeer ze allemaal tot je het snapt, of zoek op internet naar het model van je computer en stel de juiste vraag.


Bijv. "BIOS sleutel Dell laptops".


Elke computer heeft een ander BIOS-menu. Zoek uit in welk menu je de opstartvolgorde kunt configureren. Voor onze doeleinden willen we dat de computer probeert op te starten vanaf een USB-apparaat (als er een is aangesloten), voordat hij probeert op te starten vanaf de interne Hard-schijf (anders wordt Windows geladen). Als je dat eenmaal hebt ingesteld, moet je misschien opslaan voordat je afsluit of het kan automatisch opslaan.


Herstart de computer en hij zou moeten laden vanaf het USB-geheugenapparaat. We kunnen geen Linux installeren op de interne schijf en Windows wordt voorgoed verwijderd.


Als je bij het volgende scherm komt, selecteer dan "OEM install (voor fabrikanten)". Als je in plaats daarvan "Start Linux Mint" kiest, krijg je een Linux Mint-sessie geladen vanaf het geheugenapparaat, maar zodra je de computer afsluit, wordt er niets van je informatie opgeslagen - het is in feite een tijdelijke sessie zodat je het kunt uitproberen.


![image](assets/10.webp)


Je wordt door een grafische wizard geleid die je een aantal eenvoudige vragen stelt. Een daarvan zal gaan over de instellingen van Languange, een andere over je internetverbinding thuis en je wachtwoord. Als u wordt gevraagd om extra software te installeren, weigert u dit. Als je bij de vraag over het installatietype komt, zullen sommige mensen aarzelen - je moet "Wis schijf en installeer Linux Mint" kiezen. Versleutel de schijf ook niet en selecteer geen LVM.


Uiteindelijk kom je op het bureaublad. Op dit punt ben je nog niet helemaal klaar. Je treedt eigenlijk op als de fabrikant (d.w.z. iemand die een computer bouwt en Linux installeert voor de klant). Je moet dubbelklikken op het bureaubladpictogram "Linux Mint installeren" om het af te ronden.


![image](assets/11.webp)


Vergeet niet de geheugenstick te verwijderen en start opnieuw op. Na het herstarten gebruik je het besturingssysteem voor de eerste keer als nieuwe gebruiker. Gefeliciteerd.


Een van de eerste dingen die je moet doen (en regelmatig moet doen), is het systeem up-to-date houden.


Open de Terminal-toepassing en typ het volgende:


```bash
sudo apt-get update
```


druk op <enter>, bevestig je keuze en voer deze opdracht uit:


```bash
sudo apt-get upgrade
```


druk op <enter> en bevestig je keuze.


Laat het zijn werk doen, het kan enkele minuten duren.


Vervolgens installeer ik Tor (hoofdlettergevoelig):


```bash
sudo apt-get install tor
```


**Pro Tip:** Je kunt Linux Mint ook opstarten vanaf "OEM install" (zorg ervoor dat je verbonden bent met het internet, anders kun je fouten krijgen). Als je dit doet, moet je later op het pictogram "ship to end user" klikken dat op het bureaublad zou moeten staan. Je herstart dan en start het besturingssysteem op alsof je de computer voor de eerste keer opent.


Deze gids legt uit waarom je een speciale computer nodig hebt voor Bitcoin transacties, en hoe je er een vers Linux Mint besturingssysteem op installeert.