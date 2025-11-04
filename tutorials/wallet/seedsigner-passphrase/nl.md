---
name: BIP-39 wachtwoordzin SeedOndertekenaar
description: Hoe voeg ik een passphrase toe aan mijn SeedSigner-portfolio?
---

![cover](assets/cover.webp)



Een passphrase BIP39 is een optioneel wachtwoord dat, gecombineerd met de mnemonische zin, een extra beveiligingslaag biedt voor deterministische en hiërarchische Bitcoin wallets. In deze tutorial zullen we samen ontdekken hoe je een passphrase instelt op je Bitcoin wallet die gebruikt wordt met een SeedSigner.



![Image](assets/fr/01.webp)



## Vereisten voordat u een wachtwoordzin toevoegt



Voordat je aan deze tutorial begint, als je niet bekend bent met het passphrase concept, hoe het werkt en de implicaties voor je Bitcoin wallet, raad ik je ten zeerste aan dit andere theoretische artikel te raadplegen waar ik alles uitleg (dit is erg belangrijk, omdat het gebruik van een passphrase zonder volledig te begrijpen hoe het werkt, je bitcoins in gevaar kan brengen):



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Zorg er ook voor dat u uw SeedSigner al hebt geïnitialiseerd en uw mnemonische zin hebt gegenereerd voordat u aan deze tutorial begint. Als dat niet het geval is en je SeedSigner gloednieuw is, volg dan de tutorial op Plan ₿ Academy. Zodra je deze stap hebt voltooid, kun je terugkeren naar deze handleiding:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## Hoe voeg ik een passphrase toe aan de SeedSigner?



Een passphrase toevoegen aan je portfolio beheerd via SeedSigner creëert een volledig nieuwe portfolio, die een volledig aparte set sleutels genereert. Bijgevolg, als je al een portfolio hebt met satss, zal je er geen toegang meer toe hebben met de passphrase, aangezien het een volledig ander portfolio genereert.



Om een passphrase toe te passen op je SeedSigner, zet je het apparaat aan en scan je zoals gewoonlijk je SeedQR. De SeedSigner toont dan de vingerafdruk van uw huidige wallet, die overeenkomt met de wallet zonder passphrase**. De wallet met passphrase zal een andere vingerafdruk hebben.



Klik op de knop `BIP-39 Passphrase`.



![Image](assets/fr/02.webp)



Voer dan de passphrase van je keuze in het daarvoor bestemde veld in, met behulp van het toetsenbord op het scherm. Zorg ervoor dat je één of meer fysieke back-ups maakt (papier of metaal): verlies van deze passphrase zal resulteren in permanent verlies van toegang tot je bitcoins. **Om een wallet te herstellen, zijn zowel de mnemonic als de passphrase essentieel ** Als een van beide verloren gaat, worden je bitcoins onherroepelijk geblokkeerd.



Zodra je je invoer hebt voltooid, valideer je door op de `KEY3` knop rechtsonder op de SeedSigner te drukken.



![Image](assets/fr/03.webp)



*In dit voorbeeld heb ik de passphrase `pba` gebruikt. Zorg er in jouw geval echter voor dat je een robuuste passphrase kiest. Om uit te vinden hoe je een optimale passphrase kunt definiëren, kun je dit andere artikel raadplegen:*



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

De SeedSigner toont dan de nieuwe vingerafdruk van jouw passphrase wallet. Maak meerdere kopieën van deze vingerafdruk: het is belangrijk als je een wallet met passphrase gebruikt, want zo kun je elke keer dat je de passphrase invoert controleren of je geen typefouten hebt gemaakt en of je de juiste wallet gebruikt.



Als ik bijvoorbeeld in mijn geval bij het opstarten van SeedSigner per ongeluk de passphrase `Pba` opschrijf in plaats van `pba`, dan zal deze eenvoudige verandering van kleine letters naar hoofdletters resulteren in het aanmaken van een heel andere portefeuille dan degene die ik wil openen.



Deze vingerafdruk vormt geen risico voor de veiligheid of vertrouwelijkheid van uw wallet. Het geeft geen informatie vrij, publiek of privé, over uw sleutels. Dus, in tegenstelling tot de mnemonic en passphrase, kun je de vingerafdruk opslaan op een digitaal medium. Ik raad je aan om een kopie op verschillende plaatsen te bewaren: op papier, in een wachtwoordmanager, enz.



Zodra je je vingerafdruk hebt opgeslagen, klik je op `Done`.



![Image](assets/fr/04.webp)



Je hebt dan toegang tot alle functies van je portfolio, net zoals op een klassieke SeedSigner.



![Image](assets/fr/05.webp)



Je kunt nu de sleutelbewaarplaats in Sparrow Wallet importeren en je wallet normaal gebruiken. Elke keer dat je opnieuw opstart, moet je zowel je SeedQR scannen als je passphrase opnieuw invoeren met het toetsenbord, zoals we hier deden.



Voordat je je wallet met passphrase gaat gebruiken, raad ik je sterk aan om een volledige lege hersteltest uit te voeren. Hiermee kun je bevestigen dat je back-ups van de mnemonic phrase en passphrase geldig zijn. Om te leren hoe je deze controle uitvoert, zie de volgende tutorial:



https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895