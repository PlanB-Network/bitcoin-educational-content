---
name: BIP-39 Passphrase Trezor
description: Hoe voeg ik een passphrase toe aan mijn Trezor Wallet?
---
![cover](assets/cover.webp)



Een passphrase BIP39 is een optioneel wachtwoord dat, in combinatie met de Mnemonic zin, een extra Layer beveiliging biedt voor deterministische en hiërarchische Bitcoin wallets. In deze tutorial ontdekken we samen hoe je een passphrase instelt op je beveiligde Bitcoin Wallet op een Trezor (Safe 3, Safe 5 en Model One).



![Image](assets/fr/01.webp)



Voordat je aan deze tutorial begint, als je niet bekend bent met het passphrase concept, hoe het werkt en de implicaties voor je Bitcoin Wallet, raad ik je ten zeerste aan dit andere theoretische artikel te raadplegen waar ik alles uitleg (dit is erg belangrijk, omdat het gebruik van een passphrase zonder volledig te begrijpen hoe het werkt, je bitcoins in gevaar kan brengen) :



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

passphrase op Trezor wordt op de klassieke manier afgehandeld als je tijdens de configuratie hebt gekozen voor de BIP39 standaard (wat ik aanraad als je geen *Multi-share Backup* nodig hebt). Het bijzondere aan Trezor is dat je de passphrase direct op de Hardware Wallet kunt invoeren, of via het toetsenbord van je computer met behulp van de Trezor Suite software. Deze tweede optie is aanzienlijk minder veilig, omdat de computer een immens groter aanvalsoppervlak heeft dan de Hardware Wallet. Het intypen van een complexe passphrase kan echter sneller gaan op een conventioneel toetsenbord dan op de Hardware Wallet, wat het gebruik van sterke wachtzinnen kan stimuleren. Het is dus altijd beter om een passphrase te gebruiken, zelfs als het getypt moet worden, dan er helemaal geen te gebruiken. Het is echter belangrijk om bewust te blijven van het verhoogde risico op numerieke aanvallen dat dit met zich meebrengt.



Deze opties zijn niet beschikbaar op alle Trezor-compatibele Wallet beheersoftware. Voor het Model One kan passphrase bijvoorbeeld worden ingevoerd via het toetsenbord op Sparrow wallet. Voor de modellen Model T, Safe 3 en Safe 5 moet u ofwel Trezor Suite gebruiken of passphrase rechtstreeks op Hardware Wallet invoeren, omdat de optie om in te voeren via Sparrow een paar jaar geleden door HWI is uitgeschakeld.



![Image](assets/fr/02.webp)



In Trezor Suite heb je twee verschillende manieren om de passphrase vraag te beheren. Je kunt de optie "*passphrase*" activeren op het tabblad "*Apparaat*". Als deze optie geactiveerd is, zullen Trezor Suite en alle andere Wallet beheersoftware je systematisch vragen om je passphrase in te voeren elke keer dat je opstart. Als je de voorkeur geeft aan een meer discrete benadering van het gebruik van een passphrase, kun je de instelling op "*Standard*" houden. In dat geval moet je handmatig naar het menu van je Hardware Wallet in de linkerbovenhoek gaan en elke keer dat je hem opstart op de knop "*+ passphrase*" klikken.



Voordat je aan deze tutorial begint, moet je ervoor zorgen dat je je Trezor al hebt geïnitialiseerd en je Mnemonic zin hebt gegenereerd. Als dat niet het geval is en je Trezor nieuw is, volg dan de modelspecifieke tutorial op Plan ₿ Network. Zodra je deze stap hebt voltooid, kun je terugkeren naar deze tutorial.



https://planb.network/tutorials/wallet/hardware/trezor-safe-5-4413308a-a1b5-4ba4-bc49-72ae661cc4e0

https://planb.network/tutorials/wallet/hardware/trezor-safe-3-51d0d669-5d23-47c2-beb6-cc6fa0fb0ea0

https://planb.network/tutorials/wallet/hardware/trezor-model-one-5c250c49-ce3b-4c63-bd05-4600d7c11a02


## Een passphrase toevoegen aan een Safe 3 of Safe 5



Zodra je je Wallet hebt aangemaakt, je Mnemonic hebt opgeslagen en een PIN hebt ingesteld, ga je naar het Trezor Suite home menu. In de linkerbovenhoek moet een venster verschijnen waarin je wordt uitgenodigd om de passphrase BIP39 te activeren.



![Image](assets/fr/03.webp)



Als dit venster niet verschijnt, moet je handmatig de optie "*passphrase*" activeren in het tabblad "*Device*" instellingen.



![Image](assets/fr/04.webp)



Dit venster vraagt je om je passphrase in te voeren. Kies een sterke passphrase en maak meteen een fysieke back-up, op een medium zoals papier of metaal. In dit voorbeeld heb ik de passphrase gekozen: `fH3&kL@9mP#2sD5qR!82`. Dit is een voorbeeld; ik raad je echter aan om een iets langere passphrase te kiezen. Tussen de 30 en 40 tekens zou ideaal zijn (zoals een goed wachtwoord).



natuurlijk mag je nooit je passphrase delen op het Internet, zoals ik in deze tutorial doe. Dit voorbeeld Wallet wordt alleen gebruikt op Testnet en wordt aan het eind van de tutorial verwijderd.



Voor meer specifieke aanbevelingen voor het kiezen van je passphrase, nodig ik je nogmaals uit om dit andere artikel te raadplegen:



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Als je je passphrase via het toetsenbord van je computer wilt invoeren, voer het dan in het daarvoor bestemde veld in en klik dan op "*Toegang passphrase Wallet*".



![Image](assets/fr/05.webp)



Uw Hardware Wallet zal dan uw passphrase weergeven. Controleer of het overeenkomt met uw fysieke back-up (papier of metaal) voordat u op het scherm klikt om verder te gaan.



![Image](assets/fr/06.webp)



Dit geeft je toegang tot je passphrase-beschermde Wallet.



![Image](assets/fr/07.webp)



Als u er de voorkeur aan geeft om de veiligheid te verbeteren door uw passphrase alleen op uw Trezor in te voeren, klik dan op "*Enter passphrase on Trezor*" als daarom wordt gevraagd.



![Image](assets/fr/08.webp)



Er verschijnt een T9-toetsenbord op je Trezor, waarmee je je passphrase kunt invoeren. Zodra je klaar bent met invoeren, klik je op het Green vinkje om de passphrase toe te passen op je Wallet.



![Image](assets/fr/09.webp)



Je hebt dan toegang tot je passphrase beveiligde Wallet.



![Image](assets/fr/10.webp)



Voor het gebruik van Sparrow wallet is de procedure vergelijkbaar, maar voor de modellen T, Safe 3 en Safe 5 moet passphrase worden ingevoerd op de Hardware Wallet en niet via het toetsenbord van de computer.



Als Sparrow wallet toegang vereist tot je Trezor en passphrase nog niet is toegepast sinds de laatste keer opstarten, moet je het invoeren met het T9-toetsenbord.



![Image](assets/fr/11.webp)



## Een passphrase toevoegen aan een Model One



Op het Model One is het gebruik van een passphrase BIP39 bijna onmisbaar. Omdat dit apparaat geen secure element heeft, is het relatief eenvoudig om gevoelige informatie te onttrekken. Het is daarom niet bestand tegen fysieke aanvallen. Omdat de passphrase echter niet op het apparaat blijft nadat het is uitgeschakeld, kan het gebruik van een sterke (niet-breekbare) passphrase je beschermen tegen de meeste bekende fysieke aanvallen op dit model.



Op de Model One is het niet mogelijk om de passphrase rechtstreeks op de Hardware Wallet in te voeren. Je moet het invoeren via het toetsenbord van je computer.



Zodra je je Wallet hebt aangemaakt, je Mnemonic hebt opgeslagen en een PIN hebt ingesteld, kom je in het Trezor Suite startmenu. In de linkerbovenhoek moet een venster verschijnen waarin je wordt uitgenodigd om de passphrase BIP39 te activeren.



![Image](assets/fr/12.webp)



Als dit venster niet verschijnt, moet u de optie "*passphrase*" activeren op het tabblad "*Device*" van de instellingen.



![Image](assets/fr/13.webp)



Dit venster vraagt je om je passphrase in te voeren. Kies een sterke passphrase en maak meteen een fysieke back-up, op een medium zoals papier of metaal. In dit voorbeeld heb ik gekozen voor de passphrase: `fH3&kL@9mP#2sD5qR!82`. Dit is slechts een voorbeeld; ik raad je echter aan om een iets langere passphrase te kiezen. Tussen de 30 en 40 karakters zou ideaal zijn (zoals een goed wachtwoord).



Voor meer specifieke aanbevelingen over het kiezen van je passphrase, nodig ik je nogmaals uit om dit andere artikel te raadplegen:



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Voer je passphrase in het daarvoor bestemde veld in en klik dan op de knop "*Toegang passphrase Wallet*".



![Image](assets/fr/14.webp)



Uw Hardware Wallet zal uw passphrase weergeven. Controleer of het overeenkomt met je fysieke back-up (papier of metaal) en klik dan op de knop rechts om verder te gaan.



![Image](assets/fr/15.webp)



Dit brengt je naar je passphrase-beschermde Wallet.



![Image](assets/fr/16.webp)



Om Sparrow wallet daarna te gebruiken, blijft de procedure hetzelfde. Telkens wanneer Sparrow toegang vereist tot uw Hardware Wallet, en de passphrase niet is ingevoerd sinds het apparaat voor het laatst werd opgestart, moet u deze invoeren.



![Image](assets/fr/17.webp)



Gefeliciteerd, je bent nu op de hoogte van het gebruik van de passphrase BIP39 op Trezor hardware wallets. Als je nog een stap verder wilt gaan met de beveiliging van je Wallet, bekijk dan deze tutorial over Trezor's *Multi-share* back-up systemen (*Shamir's Secret Sharing Scheme*):



https://planb.network/tutorials/wallet/backup/trezor-shamir-backup-7f98b593-face-48fb-a643-0e811b87c94e

Als je deze tutorial nuttig vond, zou ik je dankbaar zijn als je hieronder een Green duim achterlaat. Voel je vrij om dit artikel te delen op je sociale netwerken. Hartelijk dank!