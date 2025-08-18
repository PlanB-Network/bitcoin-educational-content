---
name: Herstel test
description: Hoe test je je back-ups om er zeker van te zijn dat je je bitcoins niet verliest?
---
![cover](assets/cover.webp)


Bij het aanmaken van een Bitcoin Wallet wordt je gevraagd een Mnemonic zin te noteren, meestal bestaande uit 12 of 24 woorden. Met deze zin kun je de toegang tot je bitcoins herstellen in geval van verlies, beschadiging of diefstal van het apparaat waarop je Wallet staat. Voordat je je nieuwe Bitcoin Wallet gaat gebruiken, is het erg belangrijk om de geldigheid van deze Mnemonic zin te controleren. De beste manier om dit te doen is door een dry-run hersteltest uit te voeren.


Bij deze test simuleren we een Wallet herstel voordat we er bitcoins in storten. Zolang de Wallet leeg is, simuleren we een situatie waarin het apparaat met onze sleutels verloren gaat en we alleen nog onze Mnemonic zin hebben om te proberen onze bitcoins terug te krijgen.


![RECOVERY TEST](assets/notext/01.webp)


## Wat is het doel?


Met dit testproces kunt u controleren of de fysieke back-up van uw Mnemonic zinsdeel, op papier of metaal, functioneel is. Een mislukking tijdens deze hersteltest duidt op een fout in de back-up van de zin, waardoor uw bitcoins in gevaar komen. Aan de andere kant, als de test slaagt, bevestigt dit dat uw Mnemonic frase volledig operationeel is en kunt u met een gerust hart bitcoins veiligstellen met deze Wallet.


Het uitvoeren van een hersteltest op het droge heeft een dubbel voordeel. Niet alleen kun je zo de nauwkeurigheid van je Mnemonic zin controleren, maar het geeft je ook de kans om vertrouwd te raken met het Wallet herstelproces. Op deze manier ontdek je potentiële moeilijkheden voordat een echte situatie zich voordoet. Op de dag dat je daadwerkelijk je Wallet moet herstellen, zul je minder gestrest zijn, omdat je het proces al kent, wat de kans op fouten verkleint. Daarom is het belangrijk om deze teststap niet te verwaarlozen en er de nodige tijd voor te nemen.


## Wat is een hersteltest?


Het proces van de test is vrij eenvoudig:


- Na het aanmaken van je nieuwe Bitcoin Wallet, en voor het storten van je eerste satoshi's, noteer je een getuige-informatie zoals een xpub, de eerste ontvangende Address, of zelfs de master key vingerafdruk;
- Wis dan opzettelijk de nog lege Wallet, bijvoorbeeld door je Hardware Wallet te resetten naar de fabrieksinstellingen;
- Simuleer vervolgens een herstel van uw Wallet met alleen de papieren back-ups van uw Mnemonic zin en uw passphrase als u die gebruikt;
- Controleer tenslotte of de getuige-informatie overeenkomt met die van de geregenereerde Wallet. Als de informatie overeenkomt, ben je verzekerd van de betrouwbaarheid van je fysieke back-up en kun je je eerste bitcoins naar deze Wallet sturen.

Let op, tijdens een hersteltest, **moet je hetzelfde apparaat gebruiken dat bedoeld is voor je uiteindelijke Wallet**, om het aanvalsoppervlak van je Wallet niet te vergroten. Als je bijvoorbeeld een Wallet maakt op een Trezor Safe 5, zorg er dan voor dat je de hersteltest uitvoert op diezelfde Trezor Safe 5. Het is belangrijk om je herstelzin niet in andere software in te voeren, omdat dit de beveiliging van je Hardware Wallet in gevaar zou brengen, zelfs als de Wallet nog leeg is.


## Hoe voer je een hersteltest uit?


In deze tutorial leg ik uit hoe je een hersteltest uitvoert op een Bitcoin Software Wallet, met behulp van Sparrow wallet (voor een Hot Wallet). Het proces blijft echter hetzelfde voor elk ander type apparaat. Nogmaals, **als je een Hardware Wallet gebruikt, voer de hersteltest dan niet uit op Sparrow wallet** (zie het vorige hoofdstuk).


Ik heb zojuist een nieuwe Hot Wallet aangemaakt op Sparrow wallet. Op dit moment heb ik er nog geen bitcoins naartoe gestuurd. Het is leeg.


![RECOVERY TEST](assets/notext/02.webp)


Ik heb mijn 12-woord Mnemonic zin zorgvuldig genoteerd op een stuk papier. En omdat ik de veiligheid van deze Wallet wil verhogen, heb ik ook een BIP39 passphrase ingesteld die ik op een ander stuk papier heb opgeslagen:


```txt
1. shield
2. brass
3. sentence
4. cube
5. marble
6. glad
7. satoshi
8. door
9. project
10. panic
11. prepare
12. general
```


```text
Passphrase: YfaicGzXH9t5C#g&47Kzbc$JL
```


***Uiteraard mag je nooit je Mnemonic zin en je passphrase delen op het internet, in tegenstelling tot wat ik doe in deze tutorial. Dit voorbeeld Wallet wordt niet gebruikt en wordt aan het einde van de tutorial verwijderd.***


Ik noteer nu op een kladje een stukje informatie van een getuige uit mijn Wallet. Je kunt verschillende stukjes informatie kiezen, zoals de eerste ontvangende Address, de xpub, of de master key fingerprint. Persoonlijk raad ik aan om de eerste ontvangende Address te kiezen. Dit stelt je in staat om te verifiëren dat je in staat bent om het volledige eerste afleidingspad te vinden dat leidt naar deze Address.


Klik op Sparrow op het tabblad "*Adressen*".


![RECOVERY TEST](assets/notext/03.webp)


Noteer dan op een stuk papier de allereerste ontvangen Address van je Wallet. In mijn voorbeeld is de Address:


```txt
tb1qxv56mma5x5r7uhdkn0ldvcx6m0gj6f3kre0gwd
```


Nadat je de informatie hebt genoteerd, ga je naar het "*Bestand*" menu en kies je "*Weg Wallet*". Ik herinner je er nogmaals aan dat je Bitcoin Wallet leeg moet zijn voordat je deze handeling uitvoert.


![RECOVERY TEST](assets/notext/04.webp)


Als uw Wallet inderdaad leeg is, bevestig dan de verwijdering van uw Wallet.


![RECOVERY TEST](assets/notext/05.webp)


Nu moet je het aanmaken van Wallet herhalen, maar dan met onze papieren back-ups. Klik op het menu "*Bestand*" en dan op "*Nieuw Wallet*".


![RECOVERY TEST](assets/notext/06.webp)


Voer de naam van je Wallet opnieuw in.


![RECOVERY TEST](assets/notext/07.webp)


In het menu "*Script Type*" moet je hetzelfde scripttype kiezen als Wallet dat je eerder hebt verwijderd.


![RECOVERY TEST](assets/notext/08.webp)


Klik dan op de knop "*Nieuw of Geïmporteerd Software Wallet*".


![RECOVERY TEST](assets/notext/09.webp)


Kies het juiste aantal woorden voor je seed.


![RECOVERY TEST](assets/notext/10.webp)


Voer uw Mnemonic zinsdeel in de software in. Als er een "*Invalid Checksum*" bericht verschijnt, geeft dit aan dat de back-up van uw Mnemonic zinsdeel onjuist is. U moet dan opnieuw beginnen met het aanmaken van uw Wallet, aangezien uw hersteltest is mislukt.


![RECOVERY TEST](assets/notext/11.webp)


Als je een passphrase hebt, zoals in mijn geval, voer die dan ook in.


![RECOVERY TEST](assets/notext/12.webp)


Klik op "*Create Keystore*" en vervolgens op "*Import Keystore*".


![RECOVERY TEST](assets/notext/13.webp)


Klik ten slotte op de knop "*Toepassen*".


![RECOVERY TEST](assets/notext/14.webp)


Je kunt nu terugkeren naar het tabblad "*Adressen*".


![RECOVERY TEST](assets/notext/15.webp)


Controleer ten slotte of de eerste Address die je ontvangt, overeenkomt met degene die je als getuige op je concept had genoteerd.


![RECOVERY TEST](assets/notext/16.webp)


Als de ontvangstadressen overeenkomen, is je hersteltest geslaagd en kun je je nieuwe Bitcoin Wallet gebruiken. Komen ze niet overeen, dan kan dit duiden op een fout in de keuze van het scripttype, waardoor het afleidingspad onjuist is, of op een probleem met de back-up van je Mnemonic frase of je passphrase. In beide gevallen raad ik sterk aan om helemaal opnieuw te beginnen en een nieuwe Bitcoin Wallet vanaf het begin aan te maken om elk risico te vermijden. Zorg er deze keer voor dat je de Mnemonic frase zonder fouten noteert.

Gefeliciteerd, je bent nu op de hoogte van het uitvoeren van een hersteltest! Ik raad je aan om dit proces te veralgemenen voor het aanmaken van al je Bitcoin wallets. Als je deze tutorial nuttig vond, zou ik het waarderen als je hieronder een duim omhoog achterlaat. Voel je vrij om dit artikel te delen op je sociale netwerken. Hartelijk dank!