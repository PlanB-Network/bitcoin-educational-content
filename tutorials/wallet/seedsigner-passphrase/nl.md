---
name: BIP-39 passphrase SeedSigner
description: Hoe voeg ik een passphrase toe aan mijn SeedSigner portfolio?
---

![cover](assets/cover.webp)



Een passphrase BIP39 is een optioneel wachtwoord dat, gecombineerd met de Mnemonic zin, een extra Layer beveiliging biedt voor deterministische en hiërarchische Bitcoin wallets. In deze tutorial ontdekken we samen hoe je een passphrase instelt op je Bitcoin Wallet die gebruikt wordt met een SeedSigner.



![Image](assets/fr/01.webp)



## Voorwaarden voor het toevoegen van een passphrase



Voordat je aan deze tutorial begint, als je niet bekend bent met het passphrase concept, hoe het werkt en de implicaties voor je Bitcoin Wallet, raad ik je ten zeerste aan dit andere theoretische artikel te raadplegen waar ik alles uitleg (dit is erg belangrijk, omdat het gebruik van een passphrase zonder volledig te begrijpen hoe het werkt, je bitcoins in gevaar kan brengen) :



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Voordat je aan deze tutorial begint, moet je er ook voor zorgen dat je je SeedSigner al hebt geïnitialiseerd en je Mnemonic zin hebt gegenereerd. Als dat nog niet het geval is en je SeedSigner gloednieuw is, volg dan de tutorial op Plan ₿ Academy. Zodra je deze stap hebt voltooid, kun je terugkeren naar deze tutorial:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## Hoe voeg ik een passphrase toe aan de SeedSigner?



Door een passphrase toe te voegen aan je portfolio die via SeedSigner wordt beheerd, wordt een compleet nieuwe portfolio aangemaakt, die een volledig aparte set sleutels genereert. Als je dus al een portfolio met Satss hebt, kun je daar met de passphrase geen toegang meer toe krijgen, omdat het een compleet ander portfolio genereert.



Om een passphrase toe te passen op je SeedSigner, zet je het apparaat aan en scan je zoals gewoonlijk je SeedQR. De SeedSigner toont dan de vingerafdruk van uw huidige Wallet, die overeenkomt met de Wallet zonder passphrase**. De Wallet met passphrase zal een andere vingerafdruk hebben.



Klik op de knop `BIP-39 passphrase`.



![Image](assets/fr/02.webp)



Voer dan de passphrase van je keuze in het daarvoor bestemde veld in, met behulp van het toetsenbord op het scherm. Zorg ervoor dat je één of meer fysieke back-ups maakt (papier of metaal): verlies van deze passphrase resulteert in permanent verlies van toegang tot je bitcoins. **Om een Wallet te herstellen, zijn zowel de Mnemonic als de passphrase essentieel ** Als een van beide verloren gaat, worden je bitcoins onherroepelijk geblokkeerd.



Zodra je je invoer hebt voltooid, valideer je door op de `KEY3` knop rechtsonder op de SeedSigner te drukken.



![Image](assets/fr/03.webp)



*In dit voorbeeld heb ik de passphrase `pba` gebruikt. Zorg er in jouw geval echter voor dat je een robuuste passphrase kiest. Om uit te vinden hoe je een optimale passphrase kunt definiëren, kun je dit andere artikel raadplegen:*



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

SeedSigner toont dan de nieuwe vingerafdruk van je passphrase Wallet. Maak meerdere kopieën van deze vingerafdruk: het is belangrijk als je een Wallet met passphrase gebruikt, want zo kun je elke keer dat je de passphrase invoert controleren of je geen typefouten hebt gemaakt en of je bij de juiste Wallet komt.



Als ik bijvoorbeeld in mijn geval per ongeluk de passphrase `Pba` noteer bij het opstarten van SeedSigner in plaats van `pba`, dan zal deze eenvoudige verandering van kleine letters naar hoofdletters resulteren in het aanmaken van een heel andere portefeuille dan die ik wil openen.



Deze vingerafdruk vormt geen risico voor de veiligheid of vertrouwelijkheid van uw Wallet. Hij geeft geen informatie, openbaar of privé, over je sleutels vrij. In tegenstelling tot de Mnemonic en passphrase kun je de vingerafdruk op een digitaal medium opslaan. Ik raad je aan om een kopie op verschillende plaatsen te bewaren: op papier, in een wachtwoordmanager, enz.



Zodra je je vingerafdruk hebt opgeslagen, klik je op `Done`.



![Image](assets/fr/04.webp)



Je hebt dan toegang tot alle functies van je portfolio, net zoals op een klassieke SeedSigner.



![Image](assets/fr/05.webp)



Je kunt nu de sleutelbewaarplaats in Sparrow wallet importeren en je Wallet normaal gebruiken. Elke keer dat je herstart, moet je zowel je SeedQR scannen als je passphrase opnieuw invoeren met het toetsenbord, zoals we hier deden.



Voordat u uw Wallet daadwerkelijk met passphrase gebruikt, raad ik u ten zeerste aan om een volledige lege hersteltest uit te voeren. Hiermee kunt u bevestigen dat uw Mnemonic zin en passphrase back-ups geldig zijn. Om te leren hoe je deze controle uitvoert, zie de volgende tutorial:



https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895