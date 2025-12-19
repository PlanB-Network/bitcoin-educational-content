---
name: Cryptomator
description: Versleutel je bestanden in de cloud
---
![cover](assets/cover.webp)



___



*Deze zelfstudie is gebaseerd op originele inhoud van Florian BURNEL gepubliceerd op [IT-Connect](https://www.it-connect.fr/). Licentie [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Er kunnen wijzigingen zijn aangebracht in de oorspronkelijke tekst.*



___



## I. Presentatie



In deze tutorial gebruiken we de Cryptomator-applicatie om gegevens te versleutelen die zijn opgeslagen in de Cloud, of dat nu op Microsoft OneDrive, Google Drive, Dropbox, Box of zelfs iCloud is.



Het versleutelen van de gegevens die je opslaat op online opslagoplossingen zoals Drive is de beste manier om je bestanden en je privacy te beschermen. Dankzij versleuteling ben jij de enige die je gegevens kan ontsleutelen en lezen, zelfs als ze zijn opgeslagen op een server in de VS of een ander land in de wereld.



In deze demonstratie wordt een Windows 11 22H2-machine met OneDrive gebruikt, maar de procedure is identiek voor andere versies van Windows en andere opslagservices. Het enige wat u hoeft te doen is de synchronisatieclient installeren en uw account toevoegen. Hierdoor kan Cryptomator zijn gegevens opslaan in de kluis.



![Image](assets/fr/020.webp)



Cryptomator is een alternatief voor andere toepassingen, met name Picocrypt, dat in een ander artikel wordt beschreven en er anders uitziet, maar net zo eenvoudig te gebruiken is. Cryptomator is ook **open source**, compatibel met RGPD en zal **gegevens versleutelen met het AES-256 bit encryptie-algoritme**. Picocrypt daarentegen gebruikt het snellere XChaCha20-algoritme (ook 256-bit).



https://planb.academy/tutorials/computer-security/data/picocrypt-98c213bd-9ace-425b-b012-bea71ce6b38f

De Cryptomator-applicatie is beschikbaar op **Windows** (exe / msi), **Linux**, **macOS,** maar ook **Android** en **iOS**. Overigens zijn alle applicaties gratis, behalve de Android-applicatie, waarvoor je moet betalen (14,99 euro).



Op je machine zal **Cryptomator een map aanmaken waarbinnen het een kluis** zal creëren. Binnen de kluis, die kan worden opgeslagen op uw OneDrive, Google Drive of vergelijkbaar, worden uw gegevens versleuteld. Dus als je al je gegevens opslaat in de kluis die wordt gehost op je Drive-opslagruimte, zullen ze worden beschermd (omdat ze zijn versleuteld).



**Note**: in dit artikel worden online opslagdiensten als voorbeeld gebruikt, maar Cryptomator kan worden gebruikt om gegevens op een lokale schijf, een externe schijf of zelfs een NAS te versleutelen. Er zijn in feite geen beperkingen.



## II. Cryptomator installeren



Om te beginnen moet je **Cryptomator** downloaden en **installeren**. Zodra het downloaden is voltooid, is een paar klikken voldoende om de installatie te voltooien. Net als [Rclone](https://www.it-connect.fr/rclone-un-outil-gratuit-pour-synchroniser-vos-donnees-dans-le-cloud/), vertrouwt Cryptomator op WinFsp om **een virtuele schijf op je Windows machine te mounten**.





- [Cryptomator downloaden van de officiële website](https://cryptomator.org/downloads/)



![Image](assets/fr/025.webp)



## III. Cryptomator gebruiken onder Windows



### A. Een nieuwe kluis maken



Om een nieuwe safe aan te maken, klikt u op de knop "**Toevoegen**" en selecteert u "**Nieuwe safe...**". Uw bestaande en bekende kluizen op deze machine verschijnen dan in Interface, aan de linkerkant. **Een safe die is aangemaakt op machine A kan worden geopend en gewijzigd op machine B**, mits deze is uitgerust met Cryptomator (en de encryptiesleutel bekend is).



![Image](assets/fr/015.webp)



Geef de kluis eerst een naam, bijvoorbeeld "**IT-Connect**". Hierdoor wordt een map met de naam "**IT-Connect**" aangemaakt in mijn OneDrive.



![Image](assets/fr/011.webp)



In de volgende stap zal Cryptomator waarschijnlijk **de "Drive"** detecteren die aanwezig is op je machine: Google Drive, OneDrive, Dropbox, enz.... Zodat je de provider direct kunt selecteren. Ik heb dit geprobeerd op twee verschillende Windows 11 machines, met verschillende Drives, en het werd niet gedetecteerd. Het is geen probleem, definieer gewoon een **Aangepaste locatie** en selecteer de root van je opslagruimte. Bijvoorbeeld: **C:\Users\auteur**.



![Image](assets/fr/018.webp)



Vervolgens kun je een optie aanpassen onder expertinstellingen.



![Image](assets/fr/021.webp)



Vervolgens moet u **een wachtwoord instellen dat overeenkomt met de encryptiesleutel**. Met dit wachtwoord kunt u **uw Cryptomator-safe** ontgrendelen en toegang krijgen tot de gegevens. **Als u het verliest, verliest u de toegang tot uw gegevens**. Tenslotte heeft u nog de mogelijkheid om een **back-up sleutel** te maken door de optie **"Ja, beter veilig dan sorry"** aan te vinken, net zoals bij de [BitLocker] herstelsleutel (https://www.it-connect.fr/comment-activer-bitlocker-sur-windows-11-pour-chiffrer-son-disque/). Dit is aan te raden, maar sla deze backup sleutel niet op in de root van je OneDrive!



Klik op "**Een kluis maken**".



![Image](assets/fr/019.webp)



Kopieer de herstelsleutel en bewaar deze in je favoriete wachtwoordmanager. Klik op "**Volgende**".



![Image](assets/fr/013.webp)



Dat is het, je nieuwe stam is gemaakt en klaar voor gebruik!



![Image](assets/fr/014.webp)



### B. Toegangscijfers



Om toegang te krijgen tot een safe en zijn gegevens, om **bestaande gegevens te lezen of nieuwe gegevens toe te voegen**, moet u deze **ontgrendelen**. Cryptomator geeft een lijst met bekende safes: de IT-Connect safe verschijnt, dus selecteer deze en klik op "**Unlock**".



![Image](assets/fr/016.webp)



Je moet je wachtwoord invoeren om de kluis te ontgrendelen. Klik vervolgens op "**Release drive**".



![Image](assets/fr/022.webp)



**Uw safe wordt op de Windows-machine gemount als een virtueel station.** Dit station, dat hier de letter E krijgt, geeft je toegang tot je gegevens (in platte tekst, want de safe is ontgrendeld).



![Image](assets/fr/017.webp)



Aan de OneDrive-kant kunnen we niet rechtstreeks door de Cryptomator-kluis bladeren. We kunnen de gegevens niet zien (noch de bestandsnamen, noch de inhoud). Dit betekent dat u geen gegevens hoeft toe te voegen aan uw Cryptomator-kluis via de gebruikelijke OneDrive-snelkoppeling. **U moet uw gegevens toevoegen via de virtuele schijf van Cryptomator.**



![Image](assets/fr/012.webp)



### C. Basisopties



De instellingen van de kluis zijn toegankelijk via de knop "**Encrypted volume options**" (wanneer vergrendeld) en zullen automatisch vergrendelen inschakelen in geval van inactiviteit, net zoals je kunt doen met je wachtwoordkluis. De optie "**Vercodeerd volume ontgrendelen bij opstarten**" ontgrendelt, zoals de naam al aangeeft, de schijf zonder tussenkomst van jou en koppelt de virtuele schijf. Om veiligheidsredenen kun je deze optie beter niet activeren.



Via het tabblad "**Mounten**" kun je ook beslissen om het alleen-lezen te mounten of een specifieke letter toe te wijzen.



![Image](assets/fr/024.webp)



Daarnaast kun je in de instellingen van Cryptomator **het automatisch opstarten van de applicatie** inschakelen.



## IV. Conclusie



Met **Cryptomator** kun je in een paar minuten een versleutelde **kluis** maken om de gegevens te beschermen die je wilt opslaan op OneDrive en consorten. Het is heel eenvoudig te gebruiken als het gaat om het "koppelen" met een Drive: hiervoor heeft het mijn voorkeur boven Picocrypt.