---
name: COLDCARD Mk4
description: Een handleiding voor het instellen en gebruiken van een COLDCARD Mk4 met Sparrow Wallet
---

![cover-mk4](assets/cover.webp)


**Hardware wallet's** zijn fysieke apparaten die speciaal gemaakt zijn om de private sleutel van Bitcoin veilig op te slaan. Ze slaan de private sleutels offline op, wat betekent dat hackers er niet bij kunnen via het internet. Terwijl **software wallet's** vooral gebruikt worden voor alledaagse transacties, worden **hardware wallet's** vaak gebruikt om grotere hoeveelheden bitcoins voor lange tijd veilig op te slaan. Wanneer een Bitcoin transactie wordt gedaan met **hardware wallet's**, kan de wallet de transacties binnen het apparaat ondertekenen, zodat de privésleutel nooit wordt blootgesteld aan omgevingen met internetverbinding.


In deze tutorial verkennen we een van de populairste hardware wallet's geproduceerd door Coinkite, de Coldcard Mk4. We bekijken hoe je deze hardware wallet kunt instellen en gebruiken om Bitcoin transacties uit te voeren.


## Coldcard Mk4 Overzicht


Coldcard Mk4 is een Bitcoin hardware wallet vervaardigd door Coinkite. Dit apparaat is uitgerust met een scherm, een numeriek toetsenbord en een beschermende schuifklep. Daarnaast biedt het apparaat verschillende manieren om verbinding te maken en te communiceren, waaronder USB-C, air-gapped werking met behulp van een MicroSD-kaart, NFC en een virtuele schijfmodus. De Mk4 bevat ook geavanceerde beveiligingsfuncties zoals de BIP39 passphrase en trick PINs, waardoor gebruikers meer controle en bescherming hebben over hun Bitcoin.


## Eerste installatie: PIN en anti-hishingwoorden


Om te beginnen kan de Coldcard Mk4 direct worden aangeschaft bij [Coinkite's website] (https://store.coinkite.com/store). Kopers kunnen ook kiezen om met fiatvaluta of Bitcoin te betalen. Daarnaast heb je ook een MicroSD-kaart nodig (4 GB is voldoende) en een voedingsbron die kan worden aangesloten via een USB-C kabel (de Coldcard Mk4 heeft alleen een USB-C voedingsingang). Aangezien de Mk4 geen ingebouwde batterij heeft, moet hij tijdens het gebruik altijd aangesloten zijn op de voedingsbron.


Je ontvangt je Mk4 in een tamper-evident zakje. Controleer of het zakje niet beschadigd is. Als je iets ziet dat een probleem kan zijn, zoals beschadigingen of scheuren op de zak, kun je Coinkite informeren door een e-mail te sturen naar support@coinkite.com. Daarnaast vind je ook een 12-cijferig nummer op de tamper-evident zak, waarnaar we zullen verwijzen als het zaknummer van de Mk4. Dit zaknummer wordt later gebruikt om te controleren of er tijdens de verzending niet met het apparaat is geknoeid en of het rechtstreeks van Coinkite komt. Het zaknummer wordt veilig opgeslagen in de secure element van de Coldkaart met behulp van OTP (One-Time-Programmable) flashgeheugen, wat betekent dat het niet kan worden veranderd als het eenmaal is geprogrammeerd. Als je het apparaat voor het eerst inschakelt, moet het nummer op het scherm overeenkomen met het nummer op de zak. Dit garandeert dat de Mk4 die je hebt ontvangen het originele apparaat uit de fabriek is en niet is vervangen of gewijzigd. Hoewel deze verificatie alleen de integriteit van het apparaat bevestigt op het moment dat het voor de eerste keer wordt ingeschakeld, blijft de secure element je privésleutels, PIN-code en passphrase beschermen, waardoor het extreem moeilijk wordt om met je Bitcoin te knoeien. Daarnaast zullen goede praktijken, zoals het goed beveiligen van uw wallet-gerelateerde gegevens, gunstig zijn voor de algehele beveiliging van de Cold-kaart zelf. Voor meer informatie kun je dit [artikel] (https://blog.coinkite.com/understanding-mk4-security-model/) raadplegen, waarin het beveiligingsmodel van de Coldkaart wordt uitgewerkt.


Het toetsenbord bestaat uit 10 numerieke knoppen, een OK-knop (`✓`) en een annuleertoets (`✕`). Sommige numerieke knoppen kunnen ook worden gebruikt voor navigatie: `5` om omhoog te navigeren (`^`), `7` om naar links te navigeren (`<`), `8` om naar beneden te navigeren `˅`, en `9` om naar rechts te navigeren (`>`).


![01](assets/en/01.webp)


Als er geen problemen zijn met de verpakking, mag je het zakje openen. De Mk4 wordt geleverd met een wallet back-up kaart die gebruikt kan worden om informatie op te slaan over de PIN-code van het apparaat, anti-phishing woorden en seedphrase. Volg de volgende stappen voor de initialisatie:


1. Leg een stuk papier en een pen klaar.

2. Sluit de Mk4 aan op een voedingsbron (USB-C kabel) en plaats de MicroSD-kaart.

3. Zodra het apparaat voor de eerste keer wordt ingeschakeld, verschijnt op het scherm een bericht over de verkoop- en gebruiksvoorwaarden van Coldcard. Navigeer naar beneden en druk op `✓` om verder te gaan.

4. Vervolgens verschijnt er een 12-cijferig nummer op het scherm. Controleer dit nummer met het nummer op de verzegelde zak en de extra kopie van het zaknummer dat in de verzegelde zak zat, om er zeker van te zijn dat er niet met het apparaat is geknoeid. Als de nummers niet overeenkomen, neem dan onmiddellijk contact op met Coinkite support voordat u verder gaat. Druk anders op `✓` om door te gaan.


![02](assets/en/02.webp)


5. Selecteer `Kies PIN-code`.

6. Navigeer naar beneden terwijl je de instructies leest om door te gaan naar de volgende stap.


![03](assets/en/03.webp)


7. Maak en voer op de Mk4 de PIN-prefix in (moet 2 tot 6 tekens lang zijn) en schrijf deze op, druk vervolgens op `✓` om verder te gaan.

8. Schrijf de twee woorden op die op het scherm worden weergegeven. Dit zijn de anti-phishing woorden. Druk op `✓` om verder te gaan.


![04](assets/en/04.webp)


9. Maak en voer het achtervoegsel van de pincode in (of de rest van de pincode, moet 2 tot 6 tekens lang zijn) en schrijf deze op. Druk op `✓` om verder te gaan.

10. Voer uw pincode opnieuw in. Druk op `✓` om verder te gaan.


![05](assets/en/05.webp)


11. Controleer of de anti-phishing woorden hetzelfde zijn als de woorden die je bij stap 8 hebt geschreven. Druk op `✓` om door te gaan.

12. Voer uw PIN-suffix (of de rest van de PIN) opnieuw in. Druk op `✓` om door te gaan.


![06](assets/en/06.webp)


13. De PIN-code en anti-phishingwoorden van je Mk4 zijn nu succesvol aangemaakt en opgeslagen door het apparaat.


![07](assets/en/07.webp)


Merk op dat de Mk4 je altijd zal vragen om je PIN in te voeren, elke keer dat je het apparaat aanzet. Zonder deze PIN heb je geen toegang tot je Coldcard Mk4. Zorg er dus voor dat je voldoende back-up maakt voor de PIN en anti-phishing woorden.


## Uw Wallet instellen


De volgende stap is het instellen van je wallet. Er zijn drie manieren om dit te doen:


- Een nieuwe wallet aanmaken (standaard)
- Een nieuwe wallet met dobbelstenen maken
- Een wallet importeren


### Een nieuwe wallet aanmaken (standaard)


Om een nieuwe wallet aan te maken, voer je gewoon de volgende stappen uit.


1. Selecteer `New Wallet` (of `New Seed Words`) > Selecteer `12 Word` of `24 Word (standaard)` afhankelijk van je voorkeur.


![08](assets/en/08.webp)


2. Het apparaat genereert 12 of 24 woorden als seedphrase, afhankelijk van je keuze. Navigeer naar beneden terwijl je zorgvuldig elk woord in de juiste volgorde opschrijft. Druk vervolgens op `✓` om verder te gaan.


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

3. Het apparaat zal je vragen je seedphrase te verifiëren door de vragen in een willekeurige volgorde te stellen (bijvoorbeeld `Woord 1 is?`, dan `Woord 5 is?`, dan `Woord 12 is?`, enzovoort) en er zullen drie woordkeuzes zijn voor elke vraag. Raadpleeg de notitie van Stap 2 en kies de juiste woorden (door op `1`, `2` of `3` te drukken, wat overeenkomt met het juiste woord) om de wallet creatie te voltooien.


![09](assets/en/09.webp)


4. De Mk4 vraagt vervolgens of je NFC/Tap wilt inschakelen of niet. Selecteer voorlopig `✕` voor deze optie. Dit kan in de toekomst worden gewijzigd in de instellingen.

5. Tot slot zal Mk4 ook aangeven of je de USB-poort wilt uitschakelen (die kan worden gebruikt voor niet-airgapped gegevensoverdracht). Selecteer voorlopig `✓` voor deze optie. Dit kan in de toekomst worden gewijzigd in de instellingen.

6. Het scherm toont nu het hoofdmenu met bovenaan `Ready to Sign`. Hiermee is het aanmaken van wallet voltooid.


![10](assets/en/10.webp)


### Een nieuwe wallet maken met dobbelsteenworp


Je kunt er ook voor kiezen om de nieuwe seedphrase met entropie te genereren. Doe dit als je de vers gegenereerde seedphrase van Mk4 niet vertrouwt.


De procedure op de Coldcard Mk4 is als volgt:


1. Selecteer `Nieuw Wallet` (of `Nieuwe zaadwoorden`) > Selecteer `12 woorden dobbelen` of `24 woorden dobbelen`, afhankelijk van je voorkeur.

2. Je wordt gevraagd om de resultaten van je dobbelsteenworp in te voeren. Elke worp met de dobbelstenen voegt willekeur toe aan het wallet creatieproces, en zorgt ervoor dat jouw seedphrase op een volledig veilige en onvoorspelbare manier gegenereerd wordt. Het minimum aantal worpen is 50 voor seedphrase met 12 woorden en 99 voor seedphrase met 24 woorden. Druk op `✓` nadat je minstens 99 dobbelsteen worpen hebt ingevoerd.


![11](assets/en/11.webp)


3. Het apparaat genereert 12 of 24 woorden als seedphrase, afhankelijk van je keuze. Navigeer naar beneden terwijl je zorgvuldig elk woord in de juiste volgorde opschrijft. Druk vervolgens op `✓` om verder te gaan.

4. Het apparaat zal je vragen je seedphrase te verifiëren door de vragen in een willekeurige volgorde te stellen (bijvoorbeeld `Woord 1 is?`, dan `Woord 5 is?`, dan `Woord 12 is?`, enzovoort) en er zullen drie woordkeuzes zijn voor elke vraag. Raadpleeg de notitie van Stap 3 en kies de juiste woorden (door op `1`, `2` of `3` te drukken, wat overeenkomt met het juiste woord) om de wallet creatie te voltooien.


![12](assets/en/12.webp)


5. De Mk4 vraagt vervolgens of je NFC/Tap wilt inschakelen of niet. Selecteer voorlopig `✕` voor deze optie. Dit kan in de toekomst worden gewijzigd in de instellingen.

6. Tot slot zal Mk4 ook aangeven of je de USB-poort wilt uitschakelen (die kan worden gebruikt voor niet-airgapped gegevensoverdracht). Selecteer voorlopig `✓` voor deze optie. Dit kan in de toekomst worden gewijzigd in de instellingen.

7. Het scherm toont nu het hoofdmenu met bovenaan `Ready to Sign`. Hiermee is het aanmaken van wallet voltooid.


![13](assets/en/13.webp)


### Een wallet importeren


De laatste optie is het importeren van een wallet. Dit kun je doen als je een wallet wilt herstellen van een seedphrase die je al hebt. Volg deze stappen:


1. Selecteer `Import bestaande`.

2. Selecteer `24 woorden`, `18 woorden` of `12 woorden`, afhankelijk van het aantal woorden van je seedphrase.


![14](assets/en/14.webp)


3. Coldcard Mk4 zal je vervolgens vragen wat elk woord in opeenvolgende volgorde is. Navigeer voor elk woord naar beneden of naar boven tot je het schrijfvoorvoegsel voor elk woord vindt. Het apparaat zal de mogelijkheden verkleinen totdat je het juiste woord vindt. Doe dit ook voor de rest van de andere woorden.

4. Voor het laatste woord zal Coldcard Mk4 slechts een beperkt aantal mogelijke woorden weergeven. Als er geen overeenkomsten zijn, heb je de woorden misschien verkeerd ingevoerd. Kies anders het woord dat overeenkomt met het woord op je seedphrase.


![15](assets/en/15.webp)


5. De Mk4 vraagt vervolgens of je NFC/Tap wilt inschakelen of niet. Selecteer voorlopig `✕` voor deze optie. Dit kan in de toekomst worden gewijzigd in de instellingen.

6. Tot slot zal Mk4 ook aangeven of je de USB-poort wilt uitschakelen (die kan worden gebruikt voor niet-airgapped gegevensoverdracht). Selecteer voorlopig `✓` voor deze optie. Dit kan in de toekomst worden gewijzigd in de instellingen.

7. Het scherm toont nu het hoofdmenu met bovenaan `Ready to Sign`. Hiermee is het aanmaken van de wallet voltooid.


![16](assets/en/16.webp)


Houd er rekening mee dat de seedphrase de enige toegang is om je wallet te herstellen. Maak een back-up van je seedphrase en bewaar die op een veilige plek. **Niet je sleutels, niet je munten**, wie je seedphrase heeft, heeft toegang tot je bitcoins!


## Uw passphrase instellen


Een van de best practices in Bitcoin is het gebruik van een passphrase. De passphrase fungeert als 13e of 25e woord naast de seedphrase. Wat het anders maakt, is dat je elke zin kunt kiezen die je wilt, terwijl de seedphrase gekozen wordt uit een vooraf bepaalde lijst van 2048 woorden. Standaard, na het instellen van je wallet, begin je met een wallet met een lege passphrase. Om een niet-blanco passphrase in te stellen, voer je gewoon de volgende stappen uit:


1. Ga naar `Passphrase`.

2. Navigeer naar beneden om de beschrijving over passphrase te lezen en druk dan op `✓` om verder te gaan.

3. Selecteer `Zin bewerken`.


![17](assets/en/17.webp)


4. Voer je passphrase in:


   - Druk op `1` (letters), `2` (cijfers) of `3` (symbolen) om het soort teken te selecteren.
   - Druk op `4` om te wisselen tussen kleine letters en hoofdletters (alleen te gebruiken bij het invoeren van letters).
   - Navigeer met `^` of `˅` om het karakter voor je passphrase te selecteren.
   - Navigeer met `<` of `>` om tussen tekens te bewegen. Je kunt ook `>` gebruiken om spaties toe te voegen.
   - Druk op `✕` om de tekens te verwijderen.
   - Druk op `✓` wanneer u klaar bent met het bewerken van de passphrase.

5. Daarnaast hebben de andere opties de volgende functionaliteiten:


   - De functies `Woord toevoegen` of `Cijfers toevoegen` kunnen worden gebruikt om letters/cijfers toe te voegen aan de passphrase die u op dat moment bewerkt.
   - Druk op `Clear ALL` om de passphrase die je op dat moment bewerkt te resetten.
   - Druk op `CANCEL` om terug te gaan naar het hoofdmenu.

6. Schrijf je passphrase op als back-up.

7. Druk op `APPLY` om de wallet te openen met de passphrase die u zojuist hebt ingesteld.

8. Mk4 zal dan een 8 karakters lange master key fingerprint weergeven. Dit kan worden beschouwd als de "ID" van de wallet. Schrijf deze vingerafdruk op en druk op `✓` om verder te gaan. Noteer deze vingerafdruk en druk op `✓` om verder te gaan.


![18](assets/en/18.webp)


9. Nu zal de wallet het hoofdmenu van de wallet weergeven met de passphrase die je hebt ingevoerd.

10. Het is belangrijk om te weten dat een wallet je niet zal vertellen dat je de verkeerde passphrase hebt ingevoerd, omdat elke passphrase correspondeert met elke eigen wallet met een unieke identiteit (master key fingerprint). Daarom is het een goede gewoonte om dezelfde passphrase opnieuw in te voeren en te controleren of het dezelfde wallet vingerafdruk oplevert, om er zeker van te zijn dat je het correct hebt ingevoerd. Voer daarvoor de stappen 11 tot en met 14 uit.

11. Selecteer `Restore Master` in het hoofdmenu en druk vervolgens op `✓`. Je bent nu terug in het hoofdmenu van de wallet met de lege passphrase.


![19](assets/en/19.webp)


12. Ga nogmaals naar `Passphrase` en druk vervolgens op `✓` om verder te gaan.

13. Voer de passphrase die u in Stap 6 hebt opgeschreven opnieuw in en druk vervolgens op `APPLY`.

14. Controleer de 8 karakters lange mastertoetsvingerafdruk met de vingerafdruk die u in stap 8 hebt opgeschreven. Als beide vingerafdrukken niet overeenkomen, hebt u mogelijk verkeerd getypte tekens ingevoerd. U kunt in plaats daarvan een nieuwe passphrase selecteren en het proces vanaf stap 1 herhalen. Maar als beide vingerafdrukken overeenkomen, betekent dit dat u de passphrase correct hebt ingevoerd.

15. De wallet met de door jou gekozen passphrase is klaar voor gebruik.


## Wallet exporteren naar Sparrow


Net als andere hardware wallet's kan de Coldkaart Mk4 niet alleen worden gebruikt. Hij moet verbonden worden met een wallet software-interface. Met de wallet software kun je je saldo bekijken, transacties aanmaken en adressen beheren, terwijl de Coldcard deze transacties veilig ondertekent zonder ooit je privésleutels bloot te geven.


In deze tutorial gebruiken we Sparrow Wallet als interface. De procedure om de wallet te exporteren is als volgt:


1. Zorg ervoor dat je een MicroSD-kaart in de Mk4 hebt geplaatst.

2. Voer de stappen "Uw passphrase instellen" uit op de wallet met de passphrase die u wilt exporteren. Als u de wallet met de lege passphrase wilt exporteren, kunt u deze stap overslaan.

3. Ga naar `Geavanceerd/Tools` > Kies `Export Wallet` > Kies `Generic JSON` > Scroll naar beneden terwijl je de instructies leest en druk dan op `✓`.


![20](assets/en/20.webp)


4. Mk4 heeft nu een bestand met het formaat `.json` op de MicroSD-kaart aangemaakt.


![21](assets/en/21.webp)


5. Verwijder de MicroSD-kaart uit de Cold-kaart en plaats deze in het apparaat waar Sparrow Wallet is geïnstalleerd.

6. Open Sparrow Wallet.

7. Klik op `Bestand`


![22](assets/en/22.webp)


Klik vervolgens op `New Wallet`


![23](assets/en/23.webp)


Voer dan de naam in voor de wallet


![24](assets/en/24.webp)


Klik daarna op `Creëer Wallet`


![25](assets/en/25.webp)


8. Selecteer het `Script Type`.


![26](assets/en/26.webp)


9. Selecteer `Airgapped Hardware Wallet` in de Keystore sectie.


![27](assets/en/27.webp)


10. Zoek Coldcard en klik op `Import File...`.


![28](assets/en/28.webp)


11. Selecteer het bestand dat in stap 4 is gemaakt (het bestand met de indeling `.json`).


![29](assets/en/29.webp)


12. Ga op de Mk4 terug naar het hoofdmenu en navigeer naar `Advanced/Tools` > `View Identity`. Zorg ervoor dat de vingerafdruk op het scherm van de Mk4 overeenkomt met die op Sparrow Wallet (de hoofdvingerafdruk in het gedeelte Keystore)

13. Klik op de knop `Toepassen` in de rechterbenedenhoek.


![30](assets/en/30.webp)


14. Optioneel kunt u ook een wachtwoord toevoegen voor de geëxporteerde wallet. Dit wachtwoord is vereist telkens wanneer u de Sparrow Wallet-toepassing opent om toegang te krijgen tot de wallet. Als u het wachtwoord in de toekomst vergeet, kunt u gewoon stap 1-13 herhalen en een nieuw wachtwoord kiezen.


![31](assets/en/31.webp)


15. De wallet is nu succesvol geëxporteerd en klaar voor gebruik.


![32](assets/en/32.webp)


## Bitcoin ontvangen


Vervolgens leren we hoe we Bitcoin kunnen ontvangen met de Mk4. Dit proces is vrij eenvoudig, omdat je het Mk4-apparaat zelf niet hoeft te gebruiken. Zolang je je wallet al naar Sparrow hebt geëxporteerd, kun je Bitcoin direct via Sparrow Wallet ontvangen. Volg deze stappen om bitcoins te ontvangen met Mk4:


1. Open Sparrow Wallet.

2. Selecteer `Open Wallet` > Kies het wallet bestand waarnaar je bitcoin wilt ontvangen > Voer het wachtwoord in dat bij die wallet hoort.


![33](assets/en/33.webp)


3. Klik in de interface van Sparrow op de tab `Receive` aan de linkerkant van de interface.


![34](assets/en/34.webp)


4. Bovenaan verschijnt een adres met een QR-code. Je kunt het adres kopiëren en plakken of de QR-code scannen met de wallet waarmee je bitcoin naar Sparrow Wallet stuurt. Optioneel kun je een label typen voor de bitcoin die je ontvangt.


![35](assets/en/35.webp)


5. Nadat u de bitcoins hebt verzonden, klikt u in de interface van Sparrow op de tab `Transacties` aan de linkerkant van de interface. U ziet een nieuw item bovenaan de transactiegeschiedenis, dat overeenkomt met de transactie die u zojuist hebt gedaan.


![36](assets/en/36.webp)


6. Je kunt ook navigeren op de `UTXOs` tab aan de linkerkant van de interface om de bitcoin te zien die je zojuist hebt ontvangen.


![37](assets/en/37.webp)


## Bitcoin versturen


In tegenstelling tot het ontvangen van bitcoins, vereist het uitgeven van bitcoins die gekoppeld zijn aan uw Coldcard dat u de Coldcard gebruikt voor het ondertekenen van de transacties. De procedure voor het verzenden van bitcoins met Mk4 is als volgt:


1. Plaats de MicroSD-kaart in het apparaat waar uw Sparrow Wallet is geïnstalleerd.

2. Open Sparrow Wallet.

3. Selecteer `Open Wallet` > Kies het wallet bestand dat je wilt gebruiken om bitcoins mee te versturen > Voer het wachtwoord in dat bij die wallet hoort.


![38](assets/en/38.webp)


4. Klik in de interface van Sparrow op de tab `Versturen` aan de linkerkant van de interface.


![39](assets/en/39.webp)


5. Voer op het tabblad `Betalen aan` het adres in waarnaar je de bitcoins wilt sturen.

6. Voeg een label toe voor de transactie.

7. Voer het aantal bitcoins in dat je wilt versturen.

8. Voer de vergoeding in door de `Range` aan te vinken of voer direct een getal in bij `Fee`.


![40](assets/en/40.webp)


9. Klik rechtsonder op `Transactie maken`.


![41](assets/en/41.webp)


10. U komt in een nieuw transactietabblad met de naam van het label dat u in stap 6 hebt ingevoerd. Klik op `Transactie voltooien voor ondertekening`.


![42](assets/en/42.webp)


11. Klik op `Transactie opslaan` en sla de transactie op de MicroSD-kaart op. Hernoem het bestand indien nodig. Deze stap slaat de transactie op als een PSBT bestand.


![43](assets/en/43.webp)


12. Verwijder de MicroSD-kaart en plaats deze in uw Coldcard Mk4.

13. Zet je Mk4 aan door hem op een voedingsbron aan te sluiten.

14. Voer uw pincode in.

15. Ga naar `Passphrase` en voer de passphrase in van de wallet die je wilt gebruiken om de bitcoins mee te versturen. Als je de wallet met de lege passphrase wilt gebruiken, sla deze stap dan over.

16. Zorg ervoor dat de master key fingerprint dezelfde is als die op uw Sparrow Wallet. Je kunt dit controleren op het tabblad `Instellingen` van de Sparrow Wallet aan de linkerkant van de interface. Druk vervolgens op `✓` op je Mk4 om verder te gaan. Dit brengt je naar het hoofdmenu.

17. Selecteer in het hoofdmenu van de Mk4 `Klaar om te tekenen`. Op het scherm verschijnt het bericht `OKAY TO SEND?`. Controleer of het bedrag van de bitcoins die u wilt verzenden en het ontvangende adres correct zijn. Druk op `✓` om te bevestigen of op `✕` om te annuleren.

18. Als er meerdere PSBT-bestanden zijn om uit te kiezen, geeft Mk4 het bericht `Kies PSBT-bestand om te ondertekenen` weer. Druk op `✓` om verder te gaan. Selecteer vervolgens het PSBT-bestand dat u wilt ondertekenen door naar beneden of boven te navigeren. Voer stap 17 uit op die transactie.


![44](assets/en/44.webp)


19. Mk4 toont nu het bericht `PSBT ondertekend` samen met de naam van het bestand van de ondertekende PSBT. Druk op `✓` om verder te gaan.

20. Verwijder de MicroSD-kaart uit de Cold en plaats deze in het apparaat waar Sparrow Wallet is geïnstalleerd.

21. Klik op Sparrow Wallet op `Laad transactie`.


![45](assets/en/45.webp)


22. Selecteer het bestand met dezelfde naam als het bestand dat in stap 19 is gemaakt.


![46](assets/en/46.webp)


23. Klik op `Transactie uitzenden`.


![47](assets/en/47.webp)


24. Uw transactie is uitgezonden en wordt verwerkt. Je kunt naar het tabblad `Transacties` gaan om de bevestigingsstatus van je transactie te bekijken.


![48](assets/en/48.webp)


## Firmware-upgrade


### De firmwareversie controleren


De firmware van de Coldcard Mk4 kan altijd worden geüpgraded naar een nieuwere versie. Voer de volgende stappen uit om te controleren of je Mk4 is geüpgraded naar de nieuwste versie of niet:

1. Zet je Mk4 aan door hem op een voedingsbron aan te sluiten.

2. Voer uw pincode in.

3. Ga naar `Geavanceerd/Tools` > Selecteer `Upgrade Firmware` > Selecteer `Toon versie`.


![49](assets/en/49.webp)


Controleer de versie die wordt weergegeven op het scherm van de Mk4 met de versie op [Coinkite's website] (https://coldcard.com/downloads). Als de versie verschilt, kun je de firmware upgraden naar de nieuwere versie.


![50](assets/en/50.webp)


### Uw firmware upgraden


Voer de volgende stappen uit als u de firmware wilt upgraden naar de nieuwste versie:


1. Plaats de MicroSD-kaart in je laptop/PC.

2. Ga naar [Coinkite's website](https://coldcard.com/downloads) en download de nieuwste firmware naar je MicroSD-kaart (De rode knop rechts van de Mk4-afbeelding met het versienummer erop).


![51](assets/en/51.webp)


Je kunt ook andere versies downloaden door te klikken op `Alle bestanden op Mk4` en de versie die je wilt downloaden te verkennen. Het gedownloade bestand zal in `.dfu` formaat zijn.


![52](assets/en/52.webp)


3. Verwijder de MicroSD-kaart en plaats deze in je Mk4.

4. Zet je Mk4 aan door hem op een voedingsbron aan te sluiten.

5. Voer uw pincode in.

6. Ga naar `Geavanceerd/Tools` > Selecteer `Upgrade Firmware` > Selecteer `Van MicroSD` > Scroll naar beneden terwijl je de instructies leest en druk dan op `✓`.


![53](assets/en/53.webp)


7. Selecteer het `.dfu` bestand dat je in stap 2 hebt gedownload.

8. Coldcard Mk4 zal een `Installeer deze nieuwe firmware?` bericht weergeven. Scroll naar beneden terwijl je de instructies leest en druk vervolgens op `✓`.


![54](assets/en/54.webp)


9. Wacht tot de Mk4 klaar is met het installeren van de nieuwe firmware. Koppel de stroombron niet los tijdens de installatie.

10. Na voltooiing start de Mk4 zichzelf opnieuw op. U kunt uw PIN-code invoeren en de stappen "Uw firmwareversie controleren" uitvoeren om te controleren of de firmware is geüpgraded of niet.


## Geavanceerde functies


### Uw pincode wijzigen


Als u uw inlogcode wilt wijzigen, voert u gewoon de volgende stappen uit:


1. Leg een pen en een stuk papier klaar.

2. Zet je Mk4 aan door hem op een voedingsbron aan te sluiten.

3. Voer uw pincode in.

4. Ga naar `Instellingen` > Selecteer `Inloginstellingen` > Selecteer `Wijzig hoofdpincode`

5. Navigeer naar beneden terwijl je het bericht leest en druk vervolgens op `✓` om verder te gaan.


![55](assets/en/55.webp)


6. Voer uw oude PIN-code in.

7. Voer uw nieuwe PIN-code in (moet 2 tot 6 tekens lang zijn) en schrijf deze op.

8. Mk4 toont nu twee nieuwe anti-phishing woorden, schrijf ze op en druk op `✓` om verder te gaan.

9. Voer uw nieuwe PIN achtervoegsel in (of de rest van de PIN, moet 2 tot 6 tekens lang zijn) en schrijf het op.


![56](assets/en/56.webp)


10. Voer uw nieuwe PIN-code opnieuw in.

11. Controleer of de anti-phishing woorden overeenkomen met de woorden die u in stap 8 hebt geschreven.

12. Voer uw nieuwe PIN-code (of de rest van de PIN-code) opnieuw in.


![57](assets/en/57.webp)


13. Uw pincode is gewijzigd.


### Truc PIN - Nieuwe truc toevoegen


Een trick PIN is een alternatieve PIN-code die verschilt van de PIN-code die u gebruikt om uw Coldcard Mk4 voor de allereerste keer in te stellen. Wanneer u uw Mk4 inschakelt, kunt u de trick PIN(s) invoeren in plaats van uw Hoofd PIN om bepaalde acties te activeren. Om de trick PIN in Mk4 te configureren, kunt u de volgende stappen uitvoeren:


1. Leg een pen en een stuk papier klaar.

2. Zet je Mk4 aan door hem op een voedingsbron aan te sluiten.

3. Voer uw pincode in.

4. Ga naar `Instellingen` > Selecteer `Inloginstellingen` > Selecteer `Trick Pincodes` > Selecteer `Nieuwe truc toevoegen`.


![58](assets/en/58.webp)


5. Voer uw trick PIN prefix in (moet 2 tot 6 tekens lang zijn) en schrijf het op.

6. Mk4 toont nu twee nieuwe anti-phishing woorden, schrijf ze op en druk op `✓` om verder te gaan.

7. Voer uw trick PIN suffix in (of de rest van de PIN, moet 2 tot 6 karakters lang zijn) en schrijf het op.


![59](assets/en/59.webp)


8. Navigeer omlaag of omhoog om de actie te selecteren die je wilt koppelen aan de trick PIN die je zojuist hebt aangemaakt. De lijst met acties is als volgt:


    - als je `Brick Self` selecteert, worden de chips van je Mk4 vernietigd nadat de PIN-code is ingevoerd, waardoor je Mk4 permanent onbruikbaar wordt.
    - `Wipe Seed` kunt u kiezen uit de volgende acties:
      - veeg & Herstart`: De seed wordt gewist en de Cold-kaart wordt opnieuw opgestart nadat de PIN-code is ingevoerd.
      - stil wissen`: De seed wordt stil gewist, maar de Cold-kaart zal reageren alsof de PIN-code verkeerd is ingevoerd.
      - veeg -> Wallet`: De seed wordt geruisloos gewist, en de Cold-kaart brengt je in een wallet in noodtoestand.
    - `Duress Wallet`, wanneer geselecteerd, zal je Mk4 naar een duress wallet leiden nadat de PIN is ingevoerd.
    - bij `Login Countdown` kun je kiezen uit de volgende acties:
      - wissen & Aftellen`: De seed wordt onmiddellijk gewist, waarna Mk4 een aftelling begint weer te geven.
      - aftellen en bouwen: Het aftellen begint en Mk4 metselt zichzelf nadat de tijd is verstreken.
      - aftellen`: Mk4 begint met aftellen en start zichzelf opnieuw op nadat de tijd is verstreken.
    - als u `Look Blank` selecteert, nadat de pincode van de truc is ingevoerd, doet de Coldkaart alsof de seedphrase is gewist, maar in feite staat deze nog in het geheugen.
    - `Just Reboot`, indien geselecteerd zal Coldcard zichzelf herstarten nadat de trick PIN is ingevoerd.
    - `Delta Mode`, Deze geavanceerde functie is bedoeld voor ervaren gebruikers en is ontworpen om te beschermen tegen ernstige bedreigingen, zoals dwang door iemand met voorkennis. Wanneer de Delta Mode is geactiveerd, lijkt het alsof de COLDCARD de echte wallet opent, waardoor de aanvaller kan browsen en bevestigen dat het er echt uitziet. In het geheim wordt echter alle ondertekening van transacties geblokkeerd, zodat er geen bitcoin kan worden verzonden. Het schakelt ook de toegang tot de seed zinsnede uit, en elke poging om deze te bekijken zal deze volledig wissen. Om de valse wallet er overtuigender uit te laten zien, moet de Trick PIN die gebruikt wordt voor Delta Mode beginnen met dezelfde nummers als de echte PIN (dus het toont dezelfde anti-phishing woorden), maar anders eindigen.
    - `Policy Unlock`, indien geselecteerd zal Single Signer Spending Policy (SSSP) worden uitgeschakeld nadat de trick PIN is ingevoerd.
    - `Policy Unlock & Wipe`, wanneer geselecteerd, doet het alsof het SSSP uitschakelt, maar het wist de seedphrase tijdens dit proces.

9. Nadat u de actie hebt geselecteerd die u aan de trick PIN wilt koppelen, bevestigt u uw keuze door op `✓` te drukken. Uw trick PIN is succesvol geconfigureerd.

10. In `Instellingen` > `Inloginstellingen` > `Trick Pincodes`, kunt u de lijst met trick Pincodes zien die u hebt aangemaakt en de acties die eraan gekoppeld zijn. U kunt ervoor kiezen om de trick PINs en de bijbehorende acties opnieuw te configureren. U kunt ze ook verbergen of verwijderen door de PIN te selecteren en vervolgens `Trick verbergen` of `Trick verwijderen` te selecteren.


![60](assets/en/60.webp)


### Trick PIN's - Toevoegen indien fout


Als alternatief kunt u een actie `Aanvullen indien fout` toevoegen die wordt geactiveerd nadat de onjuiste PIN-code een bepaald aantal keren is ingevoerd. U kunt dit configureren door de volgende stappen uit te voeren:


1. Zet je Mk4 aan door hem op een voedingsbron aan te sluiten.

2. Voer uw pincode in.

3. Ga naar `Instellingen` > Selecteer `Inloginstellingen` > Selecteer `Trick Pincodes` > Selecteer `Toevoegen indien fout`.


![61](assets/en/61.webp)


4. De Mk4 geeft een bericht weer over deze instelling. Navigeer naar beneden terwijl je de uitleg leest en druk vervolgens op `✓` om verder te gaan.

5. Voer het aantal verkeerde pogingen in dat nodig is om de actie te activeren. Opmerking: Het maximale aantal pogingen is `12`. Dit is omdat de Mk4 zo is ontworpen dat wanneer de verkeerde PIN-code `13` keer wordt ingevoerd, het apparaat zichzelf vastzet, waardoor het permanent onbruikbaar wordt. Nadat u het nummer hebt ingevoerd, drukt u op `✓` om verder te gaan.

6. Navigeer omhoog of omlaag om de actie te selecteren. De beschikbare acties zijn als volgt:


   - `Wipe, Stop`: De seedphrase wordt gewist en het apparaat toont "Seed is wipeed, Stop"
   - wissen en herstarten`: De seedphrase wordt gewist en het apparaat start opnieuw op zonder melding.
   - stil wissen`: De seedphrase wordt stil gewist en het apparaat gedraagt zich als een verkeerde PIN-poging (geen duidelijk wisbericht).
   - `Brick Self`: Het apparaat is permanent uitgeschakeld en toont alleen "Bricked"
   - laatste Kans`: De seedphrase wordt gewist, maar je krijgt een laatste PIN poging; voer de verkeerde PIN nogmaals in en het apparaat wordt gebricked.
   - gewoon herstarten`: Het apparaat start gewoon opnieuw op en verder verandert er niets.

Kies de actie die je wilt toepassen en druk op `✓` om verder te gaan


![62](assets/en/62.webp)


7. U wordt teruggebracht naar de map `Instellingen > Aanmeldingsinstellingen > Trick PINs`. Onder de `Trick PINs:`, vindt u de lijst met trick pins samen met de `WRONG PIN` actie. U kunt deze ook verbergen of verwijderen door de PIN te selecteren en vervolgens `Trick verbergen` of `Trick verwijderen` te selecteren.


![63](assets/en/63.webp)



## Conclusie


In deze handleiding wordt uitgelegd hoe je Mk4 instelt, hoe je Bitcoin-transacties uitvoert met Mk4 en hoe je enkele geavanceerde functies van Mk4 gebruikt. Het biedt veilige en flexibele manieren om je bitcoins op te slaan en te beheren. Het ontwerp zorgt ervoor dat privésleutels het apparaat nooit verlaten, terwijl functies zoals passphrases, trick PINs en air-gapped transacties gebruikers volledige controle geven over hun beveiligingsinstellingen. Het kan gekoppeld worden met Sparrow Wallet voor een gebruiksvriendelijke ervaring bij het creëren, ondertekenen en beheren van Bitcoin transacties zonder in te leveren op privacy of veiligheid.


Als je andere functionaliteiten wilt ontdekken, kun je de documentatie op de Coinkite website [hier](https://coldcard.com/docs/) bekijken. Ik hoop dat je wat aan deze handleiding hebt bij het gebruik van je Coldkaart Mk4. Bedankt en tot de volgende keer!