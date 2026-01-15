---
name: Jade

description: Hoe uw JADE apparaat in te stellen
---

![image](assets/cover.webp)


## Video-handleiding


![video](https://www.youtube.com/watch?v=_U1jsTeqbTw)

Blockstream Jade - Mobiel Bitcoin Hardware Wallet VOLLEDIGE TUTORIAL door BTCsession


## Volledige schrijfgids


![image](assets/cover2.webp)


### Vereiste voorkennis


1. Download de nieuwste versie van Blockstream Green.


2. Installeer dit stuurprogramma om ervoor te zorgen dat Jade wordt herkend door je computer.


### Desktop instellen


![full guide](https://youtu.be/0fPVzsyL360)


Open Blockstream Green en klik op het Blockstream-logo onder Apparaten.


![image](assets/1.webp)


Sluit Jade aan op je bureaublad met de meegeleverde USB-kabel.


**Noot:** Als Jade niet wordt herkend door je computer, zorg er dan voor dat je de benodigde stuurprogramma's hebt geïnstalleerd en controleer of het misschien komt door een probleem met de USB-rechten.


Zodra uw Jade in Green verschijnt, werkt u Jade bij door te klikken op Check for updates (Controleren op updates) en de nieuwste firmwareversie te selecteren. Gebruik het scrollwieltje of de toggle op Jade om te bevestigen en door te gaan met de update. Zorg ervoor dat je Jade nog steeds de knop "Initialiseren" toont, anders moet je wachten tot na het instellen van Jade om hem te upgraden. Gebruik indien nodig de terugknop om naar dit scherm te gaan.


![image](assets/2.webp)


Nadat je de firmware van Jade hebt bijgewerkt, selecteer je Setup Jade op het netwerk en het beveiligingsbeleid dat je wilt gebruiken.


**Tip:** Het beveiligingsbeleid staat vermeld onder Type op het inlogscherm hieronder. Als u niet zeker weet of u Singlesig of Multisig Shield moet selecteren, bekijk dan onze gids [hier](https://help.blockstream.com/hc/en-us/articles/4403642609433)


![image](assets/3.webp)


Selecteer vervolgens om een Nieuwe Wallet te maken en kies 12 woorden om de generate herstelzin te maken. Als je op Geavanceerd klikt, kun je kiezen tussen een herstelzin van 12 of 24 woorden.


![image](assets/4.webp)


Noteer de herstelzin offline op papier (of gebruik een speciaal back-upapparaat voor de herstelzin voor extra veiligheid). Gebruik vervolgens het wiel of de tuimelschakelaar aan de bovenkant van je Jade om je herstelzin te verifiëren. Deze stap zorgt ervoor dat je het correct hebt opgeschreven.


![image](assets/5.webp)


Stel uw zescijferige PIN in en bevestig deze. Deze wordt gebruikt om Blockstream Jade te ontgrendelen elke keer dat je inlogt op je Wallet.


![image](assets/6.webp)


Selecteer nu gewoon Ga naar Wallet op de Green desktop app en je zult zien dat je Wallet open is op Blockstream Green. Blockstream Jade zal ook laten zien dat het gereed is! U kunt nu uw Jade gebruiken om Bitcoin transacties te verzenden en te ontvangen.


![image](assets/7.webp)


Nadat u klaar bent met uw Wallet, koppelt u uw Blockstream Jade los van uw apparaat. De volgende keer dat je de Wallet op Blockstream Jade wilt gebruiken, sluit je je apparaat weer aan en volg je de aanwijzingen.


bron: https://help.blockstream.com/hc/en-us/articles/17478506300825


### Bijlage A - Het Green Wallet downloadbestand controleren


De download verifiëren betekent controleren of het bestand dat je hebt gedownload niet is gewijzigd sinds het werd vrijgegeven door de ontwikkelaar.


We doen dit door te controleren of de handtekening (gemaakt door de private sleutel van de ontwikkelaar) samen met het gedownloade bestand en de publieke sleutel van de ontwikkelaar een TRUE resultaat opleveren wanneer deze door de gpg -verify functie gaat. Ik zal hierna laten zien hoe je dat doet.


Eerst krijgen we de ondertekensleutel:


Voor Linux open je de terminal en voer je dit commando uit (kopieer en plak de tekst en zet de aanhalingstekens erbij):


```bash
gpg --keyserver keyserver.ubuntu.com --recv-keys "04BE BF2E 35A2 AF2F FDF1 FA5D E7F0 54AA 2E76 E792"
```


Voor Mac doe je hetzelfde, behalve dat je eerst GPG Suite moet downloaden en installeren.


Voor Windows doe je hetzelfde, behalve dat je eerst GPG4Win moet downloaden en installeren.


U krijgt een melding dat de openbare sleutel is geïmporteerd.


![image](assets/9.webp)


Deze afbeelding heeft een leeg alt-attribuut; de bestandsnaam is image-3-1024x162.webp


Vervolgens moeten we het bestand met de Hash van de software ophalen. Het is opgeslagen op Blockstream's GitHub pagina. Ga eerst naar hun info pagina hier, en klik op de link voor "desktop". Het brengt je naar de laatste release pagina op GitHub en daar zie je een link naar het SHA256SUMS.asc bestand, wat een tekstdocument is met Blockstream's gepubliceerde Hash van het programma dat we gedownload hebben.


![image](assets/10.webp)


GitHub:


![image](assets/11.webp)


Het is niet nodig, maar na het opslaan op schijf hernoemde ik "SHA256SUMS.asc" naar "SHA256.txt" om het bestand op de Mac gemakkelijker te openen met de teksteditor. Dit was de inhoud van het bestand:


![image](assets/12.webp)


De tekst die we zoeken staat bovenaan. Afhankelijk van welk bestand we hebben gedownload, is er een overeenkomstige Hash uitvoer waarmee we later zullen vergelijken.


Het onderste deel van het document bevat de handtekening op het bericht hierboven - het is een twee in één bestand.


De volgorde maakt niet uit, maar voordat we de Hash controleren, gaan we eerst kijken of het Hash bericht echt is (dat wil zeggen dat er niet mee geknoeid is).


Terminal openen. Je moet in de juiste map zijn waar het SHA256SUMS.asc bestand is gedownload. Ervan uitgaande dat je het hebt gedownload naar de map "Downloads", ga je voor Linux en Mac als volgt naar de map (hoofdlettergevoelig):


```bash
cd Downloads
```


Natuurlijk moet je <enter> indrukken na deze commando's. Voor Windows open je CMD (command prompt) en typ je hetzelfde (hoewel het niet hoofdlettergevoelig is).


Voor Windows en Mac moet je respectievelijk GPG4Win en GPG Suite al gedownload hebben, zoals eerder aangegeven. Voor Linux wordt gpg meegeleverd met het besturingssysteem. Typ dit commando in Terminal (of CMD voor Windows):


```bash
gpg --verify SHA256SUMS.asc
```


De exacte spelling van de bestandsnaam (in rood) kan anders zijn op de dag dat je het bestand ophaalt, dus zorg ervoor dat het commando overeenkomt met de bestandsnaam zoals gedownload. U zou deze uitvoer moeten krijgen en de waarschuwing over de vertrouwde handtekening moeten negeren - dat betekent alleen dat u de computer niet handmatig hebt verteld dat u de openbare sleutel vertrouwt die we eerder hebben geïmporteerd.


![image](assets/13.webp)


Deze afbeelding heeft een leeg alt-attribuut; de bestandsnaam is image-4-1024x165.webp


Deze ouput bevestigt dat de handtekening goed is en we zijn er zeker van dat de private sleutel van "info@greenaddress.it" de gegevens (het Hash rapport) heeft ondertekend.


Nu moeten we ons gedownloade zipbestand Hash maken en de uitvoer zoals gepubliceerd vergelijken. Merk op dat er in het SHA256SUMS.asc bestand een stukje tekst staat met "Hash: SHA512", wat mij in verwarring brengt, omdat het bestand duidelijk SHA256 uitvoer bevat, dus ik ga dat negeren.


Voor Mac en Linux, open terminal, navigeer naar waar het zip-bestand is gedownload (waarschijnlijk moet je opnieuw "cd Downloads" typen, tenzij je de terminal sindsdien niet hebt gesloten). Overigens kun je altijd controleren in welke map je je bevindt door PWD ("print working directory") in te typen, en als dit allemaal vreemd is, is het handig om een snelle YouTube-video te bekijken door te zoeken op "how to navigate the Linux/Mac/Windows file system".


Typ dit om het bestand te hebben:


```bash
shasum -a 256 BlockstreamGreen_MacOS_x86_64.zip
```


Controleer hoe je bestand precies heet en pas indien nodig de tekst hierboven in het blauw aan.


Je krijgt dan een uitvoer als deze (die van jou zal verschillen als het bestand anders is dan de mijne):


![image](assets/14.webp)


Vergelijk vervolgens visueel de Hash uitvoer met wat er in het SHA256SUMS.asc bestand staat. Als ze overeenkomen, dan -> SUCCES! Gefeliciteerd.


bron: https://armantheparman.com/jade/


### Gebruiken op Sparrow


Als je al weet hoe je Sparrow moet gebruiken, dan is het zoals altijd:


**Noot:** het is hetzelfde proces met Specter bijvoorbeeld


Download Sparrow via de hier gegeven link.


![image](assets/14.5.webp)


Klik op Volgende om de installatiegids te volgen voor meer informatie over de verschillende verbindingsopties.


![image](assets/15.webp)


Kies de gewenste server en selecteer Create New Wallet.


![image](assets/16.webp)


Voer een naam in voor je Wallet en klik op Wallet aanmaken.


![image](assets/17.webp)


Kies de gewenste beleids- en scripttypes en selecteer vervolgens Verbonden Hardware Wallet.


**Noot:** Als je eerder Blockstream Jade hebt gebruikt als Singlesig Wallet met Blockstream Green en je wilt je transacties in Sparrow bekijken, zorg er dan voor dat het scripttype overeenkomt met het accounttype dat je fondsen in Green bevat. Het afleidingspad moet ook overeenkomen.


![image](assets/18.webp)


Sluit uw Blockstream Jade aan en klik op Scannen. U wordt dan gevraagd om uw PIN-code in te voeren op Jade.


**Tip:** Voordat u uw Jade aansluit, moet u ervoor zorgen dat de Blockstream Green app niet geopend is. Als Green geopend is, kan dit problemen veroorzaken met het detecteren van uw Jade in Sparrow.


![image](assets/19.webp)


Selecteer Sleutelbewaarplaats importeren om de openbare sleutel van de standaardaccount te importeren, of selecteer de pijl om handmatig het afleidingspad te selecteren dat u wilt gebruiken.


![image](assets/20.webp)


Nadat de gewenste sleutel is geïmporteerd, klik je op Toepassen.


![image](assets/21.webp)


U hebt nu met succes uw Wallet ingesteld en kunt beginnen met het ontvangen, opslaan en uitgeven van uw Bitcoin met Sparrow en Blockstream Jade.


**Noot:** Als je eerder Jade met Blockstream Green als Multisig Shield Wallet gebruikte, moet je niet verwachten dat je nieuwe Sparrow wallet hetzelfde saldo toont - dit zijn verschillende portemonnees. Om weer toegang te krijgen tot je Multisig Shield Wallet, sluit je je Jade gewoon weer aan op Blockstream Green.


![image](assets/22.webp)


bron: https://help.blockstream.com/hc/en-us/articles/7559912660761-How-do-I-use-Blockstream-Jade-with-Sparrow-


### Green app


als je meer een mobiele gids bent, kun je het gebruiken met Blockstream Green



- Hoe Blockstream Jade instellen met Green | Blockstream Jade - https://youtu.be/7aacxnc6DHg
- Hoe ontvang ik Bitcoin op een Jade Wallet | Blockstream Jade - https://youtu.be/CVtcDdiPqLA