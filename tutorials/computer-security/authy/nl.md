---
name: Authy 2FA
description: Hoe gebruik je een 2FA-applicatie?
---
![cover](assets/cover.webp)


Tegenwoordig is twee-factor authenticatie (2FA) essentieel geworden voor het verbeteren van de beveiliging van online accounts tegen ongeautoriseerde toegang. Met de toename van cyberaanvallen is het soms niet voldoende om alleen op een wachtwoord te vertrouwen om je accounts te beveiligen. 2FA introduceert een extra Layer van beveiliging door een tweede vorm van verificatie te vereisen naast het wachtwoord. Deze verificatie kan verschillende vormen aannemen, zoals een code die via sms wordt verstuurd, een dynamische code die wordt gegenereerd door een speciale app of het gebruik van een fysieke beveiligingssleutel. Het gebruik van 2FA vermindert het risico dat je accounts worden gecompromitteerd aanzienlijk, zelfs als je wachtwoord wordt gestolen.


## 2FA via Authenticatie Apps


We zullen andere oplossingen zoals fysieke beveiligingssleutels in andere tutorials bespreken, maar in deze tutorial wil ik het specifiek over 2FA toepassingen hebben. De werking van deze applicaties is vrij eenvoudig: wanneer 2FA geactiveerd is op een account, zal je bij elke login niet alleen gevraagd worden om je gebruikelijke wachtwoord, maar ook om een 6-cijferige code. Deze code wordt gegenereerd door je 2FA-toepassing. Een belangrijk kenmerk van deze 6-cijferige code is dat deze niet statisch is; er wordt elke 30 seconden een nieuwe code gegenereerd door de applicatie.

![AUTHY 2FA](assets/notext/01.webp)

Doordat de code elke 30 seconden wordt vernieuwd, is het voor een aanvaller erg moeilijk om toegang te krijgen tot je account. Dit systeem voorkomt dat aanvallers een gestolen of onderschepte code opnieuw kunnen gebruiken, omdat de code snel verloopt. Dus zelfs als een aanvaller erin slaagt om de code te bemachtigen, zal hij deze slechts gedurende een zeer korte periode kunnen gebruiken voordat er een nieuwe code nodig is. Bovendien vermindert het feit dat de code zo vaak verandert de beschikbare tijd voor een hacker die de code probeert te raden door middel van brute kracht aanzienlijk.


2FA via authenticatie apps is dus een gebruiksvriendelijke en gratis methode om de beveiliging van je online accounts aanzienlijk te verbeteren.


Er zijn tal van toepassingen voor het instellen van 2FA, waarvan Google Authenticator en Microsoft Authenticator de bekendste zijn. In deze tutorial wil ik je echter kennis laten maken met een andere, minder bekende oplossing genaamd Authy. Al deze applicaties werken met hetzelfde TOTP (*Time based One Time Password*) protocol, waardoor hun gebruik vrij gelijkaardig is.

Authy biedt verschillende voordelen ten opzichte van andere oplossingen van de grote techbedrijven. Eerst en vooral kun je je 2FA tokens synchroniseren op meerdere apparaten, wat handig kan zijn bij verlies of verandering van telefoon. Authy maakt het ook mogelijk om generate een versleutelde back-up te maken en online op te slaan, zodat je nooit de toegang tot je tokens verliest, zelfs niet als je je primaire apparaat verliest. Vanuit het Interface perspectief van de gebruiker vind ik persoonlijk dat Authy ook een aangenamere en intuïtievere ervaring biedt dan zijn alternatieven.


## Hoe Authy installeren?


Ga op je smartphone naar de app store (Google Play Store of Apple Store) en zoek naar "*Twilio Authy Authenticator*".



- [Apple](https://apps.apple.com/us/app/twilio-authy/id494168017)
- [Android](https://play.google.com/store/apps/details?id=com.authy.authy)

![AUTHY 2FA](assets/notext/02.webp)

Als je de app voor het eerst start, moet je een account aanmaken. Selecteer de kiescode van je land en je telefoonnummer en klik vervolgens op "*Zend*".

![AUTHY 2FA](assets/notext/03.webp)

Voer je e-mail Address in voor codeherstel.

![AUTHY 2FA](assets/notext/04.webp)

U ontvangt een e-mail om uw Address te verifiëren. Voer de ontvangen 6 cijfers in om te bevestigen.

![AUTHY 2FA](assets/notext/05.webp)

Selecteer een van de twee beschikbare methoden om je telefoonnummer te verifiëren. Als u kiest voor het ontvangen van een sms, voert u de 6-cijferige code in die u per bericht hebt ontvangen om uw nummer te bevestigen.

![AUTHY 2FA](assets/notext/06.webp)

Gefeliciteerd, uw Authy account is aangemaakt!

![AUTHY 2FA](assets/notext/07.webp)

## Hoe Authy configureren?


Om te beginnen ga je naar de instellingen van de app door op de drie kleine puntjes rechtsboven in het scherm te klikken.

![AUTHY 2FA](assets/notext/08.webp)

Klik vervolgens op "*Instellingen*".

![AUTHY 2FA](assets/notext/09.webp)

In het tabblad "*Mijn account*" heb je de mogelijkheid om je account aan te passen. Ik raad aan om een pincode toe te voegen aan de app door "*App Protection*" te selecteren. Dit voegt een extra Layer beveiliging toe om toegang te krijgen tot je applicatie.

![AUTHY 2FA](assets/notext/10.webp)

In het tabblad "*Accounts*" kunt u een back-up instellen voor uw tokens. Met deze back-up kunt u uw codes herstellen in geval van een probleem. Het wordt versleuteld met een wachtwoord dat u moet definiëren. Het is belangrijk dat dit wachtwoord sterk is en op een veilige plaats wordt bewaard. Het instellen van deze back-up is niet per se verplicht als je andere herstelmethoden hebt, zoals een tweede apparaat met hetzelfde Authy-account.

![AUTHY 2FA](assets/notext/11.webp)In the "*Devices*" tab, you can see all the devices synchronized with your Authy account. You have the option to disable the use of multiple devices, which restricts access to your account to that device only. If you use only one device, this can increase the security of your account, but make sure you have another backup method in case you lose that device.


Als u liever de toevoeging van andere apparaten toestaat, raad ik u aan om de optie te activeren die bevestiging vereist van de momenteel geautoriseerde apparaten op uw Authy-account voordat u een nieuw apparaat toevoegt.

![AUTHY 2FA](assets/notext/12.webp)

Om een nieuw apparaat toe te voegen, herhaal je gewoon het installatieproces in het vorige deel met dezelfde referenties. Vervolgens wordt u gevraagd om deze nieuwe toegang vanaf uw hoofdapparaat te bevestigen.


## Hoe 2FA instellen op een account?


Om een 2FA-authenticatiecode via een app zoals Authy op een account in te stellen, moet het account deze functie ondersteunen. Tegenwoordig bieden de meeste online diensten deze 2FA-optie, maar dit is niet altijd het geval. Laten we het voorbeeld nemen van het Proton mail account dat ik in een andere tutorial heb gepresenteerd:


https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2

![AUTHY 2FA](assets/notext/13.webp)

Je vindt deze 2FA optie meestal in de instellingen van je account, vaak onder het "*Wachtwoord*" of "*Veiligheid*" gedeelte.

![AUTHY 2FA](assets/notext/14.webp)

Wanneer je deze optie activeert op je Proton mail account, krijg je een QR-code te zien. U moet deze QR-code vervolgens scannen met uw Authy-app.

![AUTHY 2FA](assets/notext/15.webp)

Klik op Authy op de knop "*+*".

![AUTHY 2FA](assets/notext/16.webp)

Klik op "*Scan QR Code*". Scan vervolgens de QR-code op de website.

![AUTHY 2FA](assets/notext/17.webp)

Je hebt ook de mogelijkheid om je gebruikersnaam aan te passen als dat nodig is. Klik na het aanbrengen van de wijzigingen op de knop "*Opslaan*".

![AUTHY 2FA](assets/notext/18.webp)

Authy zal dan je dynamische 6-cijferige code weergeven die specifiek is voor die account en die elke 30 seconden wordt vernieuwd.

![AUTHY 2FA](assets/notext/19.webp)

Voer deze code in op de website om de 2FA setup te voltooien.

![AUTHY 2FA](assets/notext/20.webp)

Sommige sites geven je ook herstelcodes na het activeren van de 2FA. Met deze codes krijg je toegang tot je account als je de toegang tot je Authy-app verliest. Ik raad aan om ze op een veilige plaats te bewaren.

![AUTHY 2FA](assets/notext/21.webp)Your account is now secured with two-factor authentication via the Authy app.

![AUTHY 2FA](assets/notext/22.webp)

Elke keer dat je inlogt op je account, moet je de dynamische code opgeven die Authy genereert. Je kunt nu al je accounts beveiligen die compatibel zijn met deze 2FA-methode. Om een nieuwe account toe te voegen op Authy, klik je op de drie kleine puntjes rechtsboven in de app.

![AUTHY 2FA](assets/notext/23.webp)

Klik vervolgens op "*Rekening toevoegen*".

![AUTHY 2FA](assets/notext/24.webp)

Volg dezelfde stappen als bij de eerste account. Uw verschillende dynamische codes zullen zichtbaar zijn op de Authy startpagina.