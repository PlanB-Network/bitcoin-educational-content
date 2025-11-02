---
name: Misty Breez
description: De boogloze Lightning Wallet.
---

![misty-breez-cover](assets/cover.webp)



![video](https://youtu.be/mibKrTvtlyQ)


Misty Breez is een Lightning zelfdragende Wallet ontwikkeld door Breez op basis van hun Software Development Kit en het **Liquid** netwerk ontwikkeld door BlockStream.


Het komt met een compleet nieuwe aanpak voor het werken zonder een Lightning-knooppunt: een potentiële **GAME CHANGER** in Bitcoin overdrachten tussen netwerken.


In deze tutorial beschrijven we hoe deze Wallet werkt en geven we je een compleet overzicht.



## Hoe werkt Misty Breez?



Misty Breez is een implementatie zonder Lightning node als backend. Het is ontwikkeld op basis van Breez SDK en Liquid.



Liquid is een parallelle Layer aan het Bitcoin netwerk en biedt aanzienlijke verbeteringen in snelheid en transactiekosten. Met deze Layer kan Misty Breez afzien van een Lightning-knooppunt en in plaats daarvan Exchange diensten van derden gebruiken, zoals **Boltz**, om de interoperabiliteit tussen de Liquid Network en de Lightning Network te garanderen. Haast je niet, we komen hier nog op terug.



Laten we ons avontuur nu beginnen met de Misty Breez Wallet.



## Aan de slag met Misty Breez



De Misty Breez mobiele app is beschikbaar op officiële downloadplatforms zoals Google Play Store (op Android) en Apple Store (op iOS). Je kunt ook worden doorverwezen naar de juiste app vanaf de officiële [Misty Breez] website (https://breez.technology/misty/).



⚠️ Zorg ervoor dat je Misty Breez niet verwart met de Breez Wallet.



⚠️ **BELANGRIJK**: Voor de veiligheid van je bitcoins is het essentieel om de applicatie te downloaden van officiële platforms om de authenticiteit te garanderen.



![download-misty-breez](assets/fr/01.webp)



In deze tutorial gaan we uit van een Android-apparaat. Desalniettemin zijn alle stappen en specifieke functies die in dit gedeelte worden beschreven ook van toepassing op iOS.



Bij de installatie geeft Misty Breez je de optie om een nieuwe Wallet aan te maken of een oude Lightning Wallet te herstellen waarvoor je de herstelwoorden hebt.


In deze tutorial kiezen we ervoor om een nieuwe Wallet te maken.



⚠️Misty Breez bevindt zich momenteel in de ontwikkelingsfase, dus we raden je aan om met redelijke hoeveelheden te beginnen.



![create-wallet](assets/fr/02.webp)


### Sla je herstelwoorden op :


Een van de eerste dingen die je moet doen als je een nieuwe Wallet aanmaakt, is een back-up maken van je 12 herstelwoorden.


Hier volgen enkele tips voor het maken van een back-up van je back-upzin.



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Om een back-up te maken van uw zinnen, selecteert u het menu **Voorkeuren > Beveiliging** en vervolgens de optie **Controleer uw back-upzinnen**.



![backup](assets/fr/03.webp)


Voor extra veiligheid kun je ook **een pincode** aanmaken om de toegang tot je Wallet te verifiëren.




Zoek uw lokale munteenheid in de vele munteenheden die door Misty Breez worden geaccepteerd. Configureer je valuta in het **Voorkeuren > Fiatvaluta** menu en selecteer vervolgens de gewenste valuta of valuta's.



![devises](assets/fr/04.webp)



### Je eerste transacties doen


Als je al bekend bent met de Breez Wallet, zal de intuïtieve Interface van Misty Breez je absoluut niet afschrikken.



Klik in het Interface **Saldo** menu op de **Ontvangen** optie om facturen te maken om je bitcoins op je Wallet te ontvangen.



⚠️ Misty Breez vraagt je om meldingen voor de applicatie te activeren in de instellingen van je telefoon, zodat je recht hebt op een Lightning Address.



Met Misty Breez kun je :




- Ontvang bitcoins op de Lightning Network van **100 satoshis** tot **25.000.000 satoshis**.
- Bitcoins ontvangen op het Bitcoin hoofdnetwerk vanaf **25.000 satoshis**.



![transactions](assets/fr/05.webp)



Hier begint de magie van Misty Breez.


In tegenstelling tot de Breez Wallet, die je voorziet van een Lightning node en je vraagt om zelf de kosten te dekken voor het openen en sluiten van betaalkanalen, vraagt Misty Breez je helemaal niets. Zoals eerder vermeld, werkt Misty Breez niet eens op basis van een Lightning-knooppunt.



Laten we eens een kijkje achter de schermen nemen.



In werkelijkheid bezit je een Liquid Wallet die verbonden is met je Misty Breez Wallet. Logischerwijs verwerk je L-BTC (Liquid Bitcoin) tegen vaste koersen, geassocieerd met conversiediensten voor onderzeese satoshis van derden, waardoor je kunt samenwerken met de Lightning Network.



Wanneer je een betaling ontvangt op je Misty Breez Wallet, stuurt de verzender je satoshi's die via een omzettingsservice zoals Boltz (momenteel gebruikt door Misty Breez), om de verzonden satoshi's om te zetten in L-BTC die je ontvangt op je Misty Breez Wallet (geassocieerd Liquid Wallet).


Hier volgt een vereenvoudigd schema van het proces achter de schermen.



![lnswap-in](assets/fr/06.webp)



Klik op de Interface in het **Saldo** menu, klik op de **Verstuur** optie om een Lightning Invoice te betalen.


Plaats de Lightning Invoice, de Lightning Address van uw ontvanger of scan de QR-code op de Invoice om te betalen.



![send-bitcoins](assets/fr/07.webp)



Achter de schermen zet je de Liquid Wallet die verbonden is met je Misty Breez Wallet aan om het equivalent van L-BTC om te zetten in satoshis via Boltz, vervolgens maak je deze satoshis over naar de Lightning Wallet van je ontvanger (aanwezig op de Lightning Network).



![send-bitcoin-bts](assets/fr/08.webp)



Deze functie van Misty Breez's infrastructuur stelt gebruikers in staat om transacties uit te voeren, zelfs wanneer Misty Breez offline is.



Voor de meer ervaren gebruikers is er ook een menu **Voorkeuren > Ontwikkelaars** dat je wat meer details geeft over :




- De versie van de Breez Software Development Kit.
- De publieke sleutel van uw Misty Breez Wallet.
- De lener, de unieke identificator afgeleid van de primaire openbare sleutel.
- Je Wallet balans.
- Tip Liquid, voor het versturen van kleine hoeveelheden L-BTC.
- De Bitcoin Tip, voor het verzenden van kleine hoeveelheden Bitcoin.



U kunt ook bepaalde acties uitvoeren, zoals synchroniseren met de Liquid Network, een back-up maken van uw toetsen, uw activiteitenlogboek delen en ervoor kiezen om de Liquid Network opnieuw te scannen.



![dev-mode](assets/fr/09.webp)


Gefeliciteerd! Je hebt nu een goed begrip van de Misty Breez Wallet en zijn bijdrage aan Bitcoin inter-netwerk transacties. Als je deze tutorial nuttig vond, geef ons dan een Green duimpje. We horen graag van je.



Om verder te gaan, raad ik je ook aan onze tutorial over de Aqua Wallet te ontdekken, die op een vergelijkbare manier werkt als Misty Breez :



https://planb.academy/tutorials/wallet/mobile/aqua-8e6d7dd3-8c03-45cc-90dd-fe3899a7d125