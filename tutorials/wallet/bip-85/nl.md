---
name: BIP-85
description: Hoe kan ik de BIP-85 gebruiken om meerdere generate zaadzinnen van een hoofd seed te maken?
---
![cover](assets/cover.webp)



## 1. De BIP-85 begrijpen



### 1.1 Wat is BIP-85?



BIP-85 is een geavanceerde functie waarmee u meerdere **seed secundaire zinnen** kunt maken van één **seed hoofdzin**.



Elke secundaire seed zin kan gebruikt worden om een volledig onafhankelijke Bitcoin portefeuille te maken. Deze portfolio's kunnen voor verschillende doeleinden gebruikt worden: een Hot Wallet mobiel, een portfolio voor een familielid, een aparte spaarportefeuille, enz.



Alle seed subzinnen zijn **wiskundig afgeleid**, maar het is **onmogelijk om vanuit een subzin terug te leiden naar de seed hoofdzin**. Dit zorgt voor een volledige scheiding tussen elke portfolio.



Zolang je toegang hebt tot je seed hoofdzin (en de bijbehorende passphrase als je die gebruikt), kun je elke seed secundaire zin **identiek** regenereren, zonder dat je die apart hoeft op te slaan.



### 1.2 Waarom BIP-85 gebruiken?



BIP-85 is handig als je :





- Meerdere onafhankelijke Bitcoin portfolio's maken zonder meerdere back-ups
- Beheer uw fondsen volgens verschillende toepassingen (sparen, uitgaven, familie, projecten)
- Waarborgen voor familieleden ("Uncle Jim"-functie)
- Een portefeuille verwijderen zonder toegang tot je fondsen te verliezen
- Vereenvoudig uw beveiliging: slechts één seed sleutelzin om te beschermen



### 1.3 Voordelen ten opzichte van BIP-32



Met BIP-32 kan een enkele seed zin gebruikt worden om generate een complete hiërarchie van Bitcoin accounts en adressen te geven, met behulp van afleidingspaden (bijvoorbeeld: `m/44'/0'/0'/0/0`). Elk pad kan een apart account vertegenwoordigen, maar **alle paden blijven verbonden met dezelfde seed zin**. Dus, als deze seed zin gecompromitteerd wordt, worden **alle afgeleide accounts toegankelijk**.



Met BIP-85 kan een seed hoofdzin gebruikt worden om generate verschillende totaal onafhankelijke seed secundaire zinnen te maken: **als één van deze secundaire zinnen gecompromitteerd wordt, zal de aanvaller nooit terug kunnen gaan naar de hoofd seed of toegang krijgen tot de andere portefeuilles**.


Dit maakt het mogelijk om risico's te compartimenteren:





- Je kunt een secundaire seed gebruiken voor Hot Wallet of tijdelijk gebruik, waarbij je een hogere blootstelling accepteert.
- Zelfs als deze Hot Wallet in gevaar komt, blijven je andere fondsen, beschermd door andere secundaire zaden of offline gehouden, **veilig**.



Aan de andere kant, voor zowel BIP-32 als BIP-85 geldt dat als de hoofd-seed gecompromitteerd is, **alle fondsen kwetsbaar** zijn. Het is daarom cruciaal om deze met het hoogste beveiligingsniveau te beschermen.



![image](assets/fr/02.webp)


## 2. Praktische gebruikssituaties voor BIP-85



Met BIP-85 kunt u meerdere Bitcoin portefeuilles creëren vanuit één seed kernzin, elk met zijn eigen seed secundaire zin. Hier zijn vijf praktische voorbeelden voor het organiseren en beveiligen van uw Bitcoin fondsen. Elke case legt uit waarom het gebruik van BIP-85 praktischer is dan het beheren van meerdere accounts met één seed zinsdeel via BIP-32.



### 2.1 Het risico van een minder veilige portefeuille beperken





- Scenario**: Je gebruikt een "Hot Wallet" Wallet (geïnstalleerd op een apparaat met internetverbinding), voor dagelijkse transacties.
- Oplossing BIP-85**: U creëert een seed secundaire zin gewijd aan deze portefeuille.
- Voordeel ten opzichte van BIP-32**: Je hoeft de seed primaire zin niet op je telefoon te importeren, waardoor het risico op hacken kleiner wordt. Alleen de seed secundaire zin wordt gecompromitteerd, waardoor uw andere portemonnees worden beschermd. Met BIP-32 moet u de seed hoofdzin en een omleidingspad gebruiken, waardoor al uw fondsen worden blootgesteld.



### 2.2 Maak een portfolio voor een familielid





- Scenario**: Je stelt een Bitcoin Wallet in voor iemand die je dierbaar is (bv. je moeder), terwijl je het kunt terugkrijgen als ze het verliezen.
- Oplossing BIP-85**: Je maakt een speciale seed secundaire zin aan en deelt alleen deze.
- Voordeel ten opzichte van BIP-32**: Met BIP-32 vereist het aanmaken van een account voor een geliefde ofwel het delen van uw hoofd seed zinsdeel, waardoor al uw fondsen in gevaar komen en het beheer voor uw geliefde ingewikkelder wordt (beheer van vertakkingspaden), of het aanmaken van een nieuwe seed zinsdeel om op te slaan naast uw hoofd seed zinsdeel.



### 2.3 Het beheer van afzonderlijke portefeuilles vergemakkelijken





- Scenario**: Je scheidt je bitcoins voor verschillende doeleinden (bijv. langetermijnsparen, niet-KYC-fondsen).
- Oplossing BIP-85**: Je maakt seed secundaire zinnen voor elke doelstelling.
- Voordeel ten opzichte van BIP-32**: Met BIP-32 delen alle accounts dezelfde seed zin, wat het beheer in portefeuilles van derden bemoeilijkt doordat afgeleide paden zoals `m/44'/0'/0'` moeten worden beheerd. Daarnaast is het niet mogelijk om een aparte account per apparaat toe te wijzen (bijv. "sparen op Coldcard", "dagelijks op mobiel", "vakanties op Trezor"). BIP-85 wijst per doelstelling een unieke seed secundaire zin toe, die eenvoudig te identificeren en afzonderlijk op elk apparaat te importeren is.



### 2.4 Een tijdelijke Wallet gebruiken voor transacties





- Scenario**: Je hebt een tijdelijke portefeuille nodig voor een eenmalige transactie of om de vertrouwelijkheid te bewaren (bv.: vermenging van fondsen, interactie met een Exchange KYC, enz.)
- Oplossing BIP-85**: Je maakt een seed secundaire zin aan, gebruikt hem voor de transactie en vernietigt hem dan indien nodig, wetende dat hij geregenereerd kan worden.
- Voordeel ten opzichte van BIP-32**: Met BIP-32 is een tijdelijke account afhankelijk van de seed hoofdzin, waardoor al uw fondsen worden blootgesteld als ze worden gecompromitteerd.





## 3. Voordat u begint





- Hardware** (optioneel)
 - Coldcard Mk4 of Q1
 - MicroSD-kaart





- Basiskennis
 - Mnemonic-zinnen begrijpen (BIP-39): een lijst van 12 tot 24 woorden om een portfolio op te slaan.
 - Weten wat een Bitcoin Wallet is: software of apparaat om je bitcoins te beheren, en hoe je het herstelt met een Mnemonic zin.
 - Meer bronnen in de bijlagen.





- Compatibele** software
 - Sparrow wallet (computer, voor alleen kijken of geavanceerd beheer)
 - Nunchuck (mobiel, voor meerdere handtekeningen)
 - BlueWallet (mobiel)
 - ...





- 3.4 Coldcard** configuratie
 - Initialiseer een seed zin van 24 woorden op de Coldcard.
 - Optioneel: Voeg een passphrase toe om de toegang tot BIP-85 takken te beveiligen.
 - Nuttige opties activeren: NFC (voor export), USB op batterij uitschakelen (beveiliging).




## 4. Stap-voor-stap uitleg



Volg deze stappen om een secundaire Mnemonic met BIP-85 op uw Coldcard aan te maken, te gebruiken en op te halen.



### 4.1 generate a seed secundaire zin



U maakt een seed secundaire zin van uw seed hoofdzin.


Zet uw Coldcard aan en voer uw pincode in.





- 1. Als u een passphrase op uw hoofd-seed hebt toegepast:**
 - Ga in het beginscherm naar `passphrase`.
    - Kies `Woord toevoegen` en voer uw wachtwoord in.
    - Druk op `Toepassen`.
    - Controleer de identiteit van de Wallet: Ga naar `Geavanceerd > Identiteit weergeven` om de vingerafdruk van de Wallet te noteren.





- 2. Ga naar menu BIP-85**
 - Ga in het Beginscherm naar `Geavanceerd > seed B85 afleiden`
 - Lees de waarschuwing en bevestig.



De ColdCard informeert je dat de gegenereerde seeds wiskundig zijn afgeleid van je hoofd seed, maar cryptografisch volledig onafhankelijk zijn.


![image](assets/fr/03.webp)





- 3. Kies een formaat


Selecteer het seed zinsformaat: 12, 18 of 24 woorden. Controleer het aantal woorden dat wordt geaccepteerd door de Wallet waarin je de seed-zin wilt importeren.


![image](assets/fr/04.webp)





- 4. Selecteer index
 - Voer een index tussen 0 en 9999 in.
 - Deze index is cruciaal voor het later regenereren van de secundaire seed. Bewaar het zorgvuldig met een label zoals: "Index 1 = Wallet mobiel", "Index 2 = familieproject", "Index 4 = testmix", ...
 - Als je het verliest, verlies je niet de toegang tot je geld, maar moet je combinaties van 0 tot 9999 testen om het terug te vinden.


![image](assets/fr/05.webp)





- 5. seed secundaire zin** noteren of exporteren


ColdCard toont nu een nieuwe seed secundaire zin. Je kunt :




 - De **handmatige notitie**.
 - Druk op :
     - 1` om het op te slaan op de SD-kaart
     - `2` om **de modus "gebruik deze seed"** in te voeren op de ColdCard (handig voor het exporteren of ondertekenen van een transactie)
     - 3` om een **QR-code** weer te geven (te scannen met een mobiele applicatie zoals BlueWallet of Nunchuck)
     - 4` om te verzenden via **NFC**



💡 Op dit punt heb je een onafhankelijke seed zin, bruikbaar in elke Wallet BIP39 (Trezor, Ledger, BlueWallet, Nunchuck...).


![image](assets/fr/06.webp)


![image](assets/fr/07.webp)


### 4.2 De secundaire seed gebruiken



Je kunt nu deze afgeleide seed gebruiken om een nieuwe portfolio aan te maken in :




- een mobiele app
- nog een Hardware Wallet
- een Multisig portefeuille



### 4.3 Een verloren seed secundaire zin herstellen



Om op elk moment een secundaire seed op te halen, herhaal je het proces:


1. Start uw ColdCard opnieuw op


2. Voer uw PIN-code in


3. Voer uw passphrase in, indien gedefinieerd


4. Ga naar `Geavanceerd > seed B85 afleiden`


5. Kies formaat (12/18/24 woorden)


6. Voer dezelfde index in (bijvoorbeeld `1`)


7. Je krijgt precies dezelfde secundaire seed




## 5. Grenzen, risico's en best practices



### 5.1 Afhankelijkheid van seed hoofdzin + passphrase



Het gebruik van BIP85 is volledig afhankelijk van de seed hoofdzin van 24 woorden, en ook van passphrase als je die hebt toegepast.




- Uit deze twee Elements kunnen alle seed secundaire zinnen geregenereerd worden.
- Zonder een van deze 2 Elements verlies je de toegang tot alle afgeleide portefeuilles.



### 5.2 Risico's bij een configuratie met meerdere handtekeningen



We raden sterk af om secundaire seed zinnen te gebruiken die gegenereerd zijn uit dezelfde primaire seed zin in een multi-sig configuratie: als het apparaat of de primaire seed zin gecompromitteerd is, kunnen alle multi-sig sleutels opnieuw gegenereerd worden door een aanvaller.



### 5.3 Softwarecompatibiliteit



Niet alle toepassingen ondersteunen BIP85-afleiding direct. De seeds die via BIP85 worden gegenereerd zijn echter standaard BIP39 seeds (12, 18 of 24 woorden) en kunnen daarom in elke BIP39-compatibele portfolio worden gebruikt.



### 5.4 BIP85 rekeningregister



Het wordt aanbevolen om een persoonlijk register bij te houden van seed secundaire zinnen.




- Hiermee kunt u snel achterhalen welke BIP85-index overeenkomt met welke portefeuille, zonder dat u seed secundaire zinnen hoeft bij te houden.
- Dit register moet minimalistisch blijven, zonder expliciete vermelding van Bitcoin, en moet apart van het hoofdregister seed worden opgeslagen. Vergeet niet om het te vermelden in je overervingsplan.



Het register kan :




- bIP85 gebruikte index (getal van 0 tot 9999)
- een gebruiks- of referentienaam (bijv. Hot Wallet, persoonlijk spaargeld, Wallet van moeder)
- indien nodig, de Wallet vingerafdruk voor verificatie in ColdCard



### 5.5 Back-up



Back-ups moeten :




- de belangrijkste seed
- gW-76 (indien gebruikt)



Nooit samen bewaren:




- de hoofd seed en passphrase
- het hoofdregister seed en het BIP85-accountregister



Meer bronnen in de bijlagen.




## BIJLAGEN



## A.1 Woordenlijst





- [BEEP](https://planb.network/resources/glossary/bip)
- [BIP-32](https://planb.network/resources/glossary/bip0032)
- [BIP-39](https://planb.network/resources/glossary/bip0039)
- [BIP-85](https://planb.network/resources/glossary/bip0085)
- [seed zin] (https://planb.network/resources/glossary/recovery-phrase)
- [passphrase] (https://planb.network/resources/glossary/passphrase-bip39)
- [Multisig] (https://planb.network/resources/glossary/multisig)




### A.2 Uw herstelzin opslaan



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270


### A.3 Het passphrase BIP39 begrijpen



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7


### A.4 Hoe Bitcoin portfolio's werken



https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f