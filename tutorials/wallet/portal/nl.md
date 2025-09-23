---
name: Portal
description: De TwentyTwo-Devices Hardware Wallet-portal configureren en gebruiken
---
![cover](assets/cover.webp)


Portal is een Bitcoin Hardware Wallet ontworpen door TwentyTwo Devices, een bedrijf gespecialiseerd in het maken van open-source hardware wallets voor bitcoiners. TwentyTwo Devices is opgericht door Alekos Filini, maker van het Magical Bitcoin project ([voortaan BDK genoemd](https://github.com/bitcoindevkit)) en heeft gewerkt voor Blockstream en BHB Network. Het bedrijf richt zich op autonomie, eenvoud en veiligheid voor de gebruiker.


Wat Portal onderscheidt van andere hardware wallets op de markt is de integratie met smartphones. Het werkt zonder kabels of batterijen. Het maakt gebruik van NFC-technologie om zichzelf van stroom te voorzien en te communiceren met elke compatibele mobiele Wallet. Het intrigerende ontwerp is ontworpen voor ergonomisch gebruik. Het ronde deel wordt op de achterkant van de smartphone geplaatst om een scherm te onthullen waarop je de details van je transacties kunt controleren voordat je ze ondertekent met de speciale knop.


![Image](assets/fr/01.webp)


De Portal is volledig open-source, gebaseerd op firmware geschreven in Rust en gebruikt BDK (Bitcoin Dev Kit) voor sleutel- en transactiebeheer. Hij wordt verkocht voor €89 [op de officiële website] (https://store.twenty-two.xyz/products/portal-hardware-Wallet).


Op het moment van schrijven is de Portal compatibel met de Nunchuk en Bitcoin Keeper applicaties. In deze tutorial configureren we het met Nunchuk.


## Unboxing


Controleer bij ontvangst of de doos en het etiket dat de Portal verzegelt, in goede staat zijn. Binnenin vind je je portaal in een verzegeld zakje.


Controleer of de Seal intact is om te bevestigen dat het zakje niet geopend is. Het unieke nummer dat in grote letters op het zakje staat, moet overeenkomen met het nummer dat in het zwart onder de blauwe Seal geschreven staat, met het nummer op het dooslabel en met het nummer dat op uw scherm verschijnt wanneer u voor het eerst opstart.


![Image](assets/fr/02.webp)


## Nunchuk installatie


Om de Wallet gehost op de Portal te beheren, gaan we de Nunchuk applicatie gebruiken. Download de applicatie van de [Google Play Store](https://play.google.com/store/apps/details?id=io.nunchuk.android), de [App Store](https://apps.apple.com/us/app/nunchuk-Bitcoin-Wallet/id1563190073) of direct via het [bestand `.apk`](https://github.com/nunchuk-io/nunchuk-android/releases).


![Image](assets/fr/03.webp)


Als je de Nunchuk voor de eerste keer gebruikt, zal de applicatie je vragen om een account aan te maken. Voor deze tutorial is het niet nodig om een account aan te maken. Selecteer "*Doorgaan als gast*" om door te gaan zonder account.


![Image](assets/fr/04.webp)


## Portaalconfiguratie


Klik op het startscherm van de Nunchuk op het "*NFC*"-logo bovenaan het scherm.


![Image](assets/fr/05.webp)


Plaats je Portal op de achterkant van je smartphone om hem te activeren.


![Image](assets/fr/06.webp)


Nunchuk zal je portaal herkennen. Klik dan op "*Doorgaan*".


![Image](assets/fr/07.webp)


Om een nieuwe Wallet aan te maken, selecteer je "*generate seed op Portal*" en klik je vervolgens op "*Doorgaan*".


![Image](assets/fr/08.webp)


Je kunt kiezen tussen een 12- of 24-woords Mnemonic zin. De beveiliging die beide opties bieden is vergelijkbaar, dus je kunt kiezen voor de optie die het makkelijkst op te slaan is, d.w.z. 12 woorden.


![Image](assets/fr/09.webp)


Je wordt dan gevraagd om een wachtwoord te kiezen. Het wachtwoord ontgrendelt uw portaal. Het biedt daarom bescherming tegen onbevoegde fysieke toegang. Dit wachtwoord is niet betrokken bij de afleiding van de cryptografische sleutels van uw Wallet. Dus zelfs zonder toegang tot dit wachtwoord, kunt u met uw 12- of 24-woorden Mnemonic zin weer toegang krijgen tot uw bitcoins. Het is raadzaam om een wachtwoord te kiezen dat zo willekeurig mogelijk is en lang genoeg. Zorg ervoor dat je dit wachtwoord opslaat op een andere plaats dan waar je Portal is opgeslagen (bijvoorbeeld in een wachtwoordmanager).


![Image](assets/fr/10.webp)


Je portaal zal je Mnemonic zin van 12 woorden weergeven. Deze Mnemonic geeft je volledige, onbeperkte toegang tot al je bitcoins. Iedereen die in het bezit is van deze zin kan uw fondsen stelen, zelfs zonder fysieke toegang tot uw portaal.


De 12-woorden zin herstelt de toegang tot je bitcoins in geval van verlies, diefstal of breuk van je Portal. Het is daarom heel belangrijk om het zorgvuldig te bewaren en op een veilige plaats op te bergen.


Je kunt het op een stuk papier schrijven of voor extra veiligheid raad ik aan om het op een roestvrijstalen basis te graveren om het te beschermen tegen brand, overstroming of instorting.


Voor meer informatie over de juiste manier om je Mnemonic zin op te slaan en te beheren, raad ik je aan deze andere tutorial te volgen, vooral als je een beginner bent:


https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

natuurlijk mag je deze woorden nooit delen op het Internet, zoals ik in deze tutorial doe. Dit voorbeeld Wallet wordt alleen op Testnet gebruikt en wordt aan het einde van de tutorial verwijderd.


Druk stevig op de knop op je portaal om naar de volgende woorden te gaan. Zorg ervoor dat je je hele vinger op de knop legt en de druk een paar seconden vasthoudt, zodat de interactie goed wordt gedetecteerd.


![Image](assets/fr/11.webp)


Uw portaal bevestigt dan het wachtwoord dat u in Nunchuk hebt ingevoerd.


![Image](assets/fr/12.webp)


Je bent nu klaar met het configureren van je portaal en het aanmaken van je Mnemonic zin!


![Image](assets/fr/13.webp)


## Bitcoin Wallet configuratie


Klik op de Nunchuk op "*Continue*", terwijl je nog steeds je Portal tegen de achterkant van je telefoon houdt.


![Image](assets/fr/14.webp)


In deze tutorial ga ik een single-sig Wallet opzetten, dus ik selecteer deze optie.


![Image](assets/fr/15.webp)


Gebruik het standaardaccount, d.w.z. het eerste account in de Wallet (nummer 0). De Nunchuk zal je dan vragen om het wachtwoord van je portaal te bevestigen om het te ontgrendelen.


![Image](assets/fr/16.webp)


Bevestig op de Portal de export van je xpub naar Nunchuk. Hierdoor kun je de Wallet vanaf je smartphone beheren zonder dat je bitcoins kunt uitgeven zonder de Portal. Druk op de knop om te bevestigen.


Merk op dat het afleidingspad dat in jouw geval wordt aangegeven anders zal zijn dan het mijne, aangezien deze tutorial is uitgevoerd op Testnet.


![Image](assets/fr/17.webp)


Geef je Wallet een naam, bijvoorbeeld "*Portal*" en klik dan op "*Doorgaan*".


![Image](assets/fr/18.webp)


Nunchuk geeft je dan je Descriptor. Het is een goed idee om een back-up te maken. Hoewel je met de Descriptor geen bitcoins kunt uitgeven, kun je er wel de afleidingspaden van je sleutels mee traceren vanaf je Mnemonic zin in het geval van Wallet herstel. Bewaar het op een veilige plaats, want hoewel het uitlekken ervan geen veiligheidsprobleem vormt, is het wel een vertrouwelijkheidsprobleem.


Klik op "*Done*".


![Image](assets/fr/19.webp)


Je moet nu de publieke sleutels generate maken voor je Bitcoin Wallet. Klik hiervoor op de knop "*Nieuw Wallet* aanmaken".


![Image](assets/fr/20.webp)


Klik opnieuw op "*Nieuw Wallet maken*". Kies dan de optie "*Maak een nieuwe Wallet met gebruik van bestaande sleutels*".


![Image](assets/fr/21.webp)


Kies een naam voor je Wallet en klik op "*Doorgaan*".


![Image](assets/fr/22.webp)


Selecteer je Portal als ondertekeningsapparaat voor deze nieuwe set sleutels en klik dan op "*Doorgaan*".


![Image](assets/fr/23.webp)


Als alles naar wens is, valideer je de creatie.


![Image](assets/fr/24.webp)


Je kunt dan je Wallet configuratiebestand opslaan. Dit bestand bevat alleen je publieke sleutels, wat betekent dat zelfs als iemand er toegang toe krijgt, hij niet in staat zal zijn om je bitcoins te stelen. Ze kunnen echter wel al uw transacties volgen. Dit bestand vormt daarom alleen een risico voor uw privacy. In sommige gevallen kan het onmisbaar zijn om je Wallet terug te krijgen.


![Image](assets/fr/25.webp)


En dat is alles!


![Image](assets/fr/26.webp)


## Hoe kan ik bitcoins ontvangen met Portal?


Om bitcoins te ontvangen, selecteer je Wallet.


![Image](assets/fr/27.webp)


Voordat je de gegenereerde Address gebruikt, moet je deze controleren op het Portal scherm. Klik hiervoor op "*Ontvangen*".


![Image](assets/fr/28.webp)


Klik op de drie puntjes en selecteer "*Verifieer Address via PORTAL*". Voer vervolgens uw wachtwoord in.


![Image](assets/fr/29.webp)


Plaats je Portal op de achterkant van je telefoon en bevestig door op de knop te drukken.


![Image](assets/fr/30.webp)


Controleer of de Address op het portaal overeenkomt met de Address op je Nunchuk en bevestig dit door nogmaals op de knop te drukken. Als de adressen identiek zijn, kunt u deze Address aan de betaler geven.


![Image](assets/fr/31.webp)


Zodra de transactie van de betaler is uitgezonden, zie je deze op je Wallet verschijnen.


![Image](assets/fr/32.webp)


Klik op "*Bekijk hoeken*".


![Image](assets/fr/33.webp)


Selecteer uw nieuwe UTXO.


![Image](assets/fr/34.webp)


Klik op de "*+*" naast "*Tags*" om een tag aan je UTXO toe te voegen. Dit is een goede gewoonte, omdat het je helpt herinneren waar je munten vandaan komen en je privacy optimaliseert bij toekomstige uitgaven.


![Image](assets/fr/35.webp)


Selecteer een bestaande tag of maak een nieuwe aan en klik dan op "*Opslaan*". Je kunt ook "*verzamelingen*" maken om je onderdelen op een meer gestructureerde manier te organiseren.


![Image](assets/fr/36.webp)


## Hoe verstuur ik bitcoins via Portal?


Nu je bitcoins in je Wallet hebt, kun je ze ook versturen. Klik daarvoor op de Wallet van je keuze.


![Image](assets/fr/37.webp)


Klik op de knop "*Versturen*".


![Image](assets/fr/38.webp)


Selecteer het bedrag dat u wilt verzenden en klik vervolgens op "*Doorgaan*".


![Image](assets/fr/39.webp)


Voeg een "*noot*" toe aan je toekomstige transactie om je te herinneren aan het doel ervan.


![Image](assets/fr/40.webp)


Voer dan de Address van de ontvanger in het daarvoor bestemde veld in. Je kunt ook een als QR-code gecodeerde Address scannen door op het pictogram rechtsboven in het scherm te klikken. Klik vervolgens op de knop "*Reëer transactie*".


![Image](assets/fr/41.webp)


Controleer je transactiegegevens, klik dan op de knop "*Aftekenen*" naast je portaal en voer je wachtwoord in.


![Image](assets/fr/42.webp)


Plaats je Portaal op de achterkant van je telefoon. Controleer of de Address van de ontvanger en het bedrag correct zijn. Zo ja, druk dan op de knop om verder te gaan.


![Image](assets/fr/43.webp)


Controleer of de transactiekosten correct zijn en druk dan nogmaals op de knop om je transactie te ondertekenen.


![Image](assets/fr/44.webp)


Je transactie is ondertekend. U kunt de details nog een laatste keer controleren op de Nunchuk en dan op de knop "*Transactie uitzenden*" klikken om de transactie uit te zenden op het Bitcoin netwerk.


![Image](assets/fr/45.webp)


Je transactie wacht nu op bevestiging.


![Image](assets/fr/46.webp)


Gefeliciteerd, je hebt nu Portal onder de knie! Als je deze tutorial nuttig vond, zou ik je dankbaar zijn als je hieronder een Green duim achterlaat. Voel je vrij om dit artikel te delen op je sociale netwerken. Hartelijk dank!


Bekijk voor meer informatie onze complete training over hoe HD wallets werken:


https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f