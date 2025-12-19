---
name: Seedkeeper x SeedSigner
description: Hoe gebruik ik Seedkeeper met mijn SeedSigner?
---

![cover](assets/cover.webp)



*Met dank aan het [Satochip](https://satochip.io/) team voor het hergebruiken van [hun video's](https://www.youtube.com/@satochip/videos) in deze handleiding. Dank ook aan [Crypto Guide](https://www.youtube.com/@CryptoGuide/) voor de fork van de SeedSigner firmware, waardoor ondersteuning voor smartcards mogelijk is



---

De SeedSigner is een wallet hardware die je zelf in elkaar zet met standaard hardware, meestal rond een Raspberry Pi Zero. Deze wallet wordt "*stateless*" genoemd: in tegenstelling tot de meeste andere modellen op de markt (Coldcard, Trezor, Ledger, enz.) slaat het geen gegevens op in het permanente geheugen en werkt het alleen live vanuit RAM. Hierdoor wordt de seed van jouw portfolio nooit opgeslagen op de SeedSigner. Elke keer dat je opnieuw opstart, moet je het invullen om het apparaat in staat te stellen jouw transacties te ondertekenen. De meest gebruikelijke methode is om je seed op te slaan als een QR-code, die je dan elke keer scant als je hem gebruikt (*SeedQR*).



Deze aanpak brengt echter een aanzienlijk risico met zich mee: het seed moet toegankelijk blijven in duidelijke tekst, zodat het gescand kan worden. In geval van diefstal of inbraak kan een aanvaller het gemakkelijk bemachtigen en je bitcoins stelen.



Om deze zwakte te omzeilen, kan SeedSigner gecombineerd worden met [**Seedkeeper**](https://satochip.io/product/seedkeeper/), een smartcard ontwikkeld door Satochip. Hiermee kunnen geheugenzinnen (of andere geheimen) worden opgeslagen in een secure element die beschermd is met een PIN-code. De Seedkeeper applet is open-source en de secure element is EAL6+ gecertificeerd. In combinatie met SeedSigner biedt het een zeer interessante beveiligingsfunctie: je sleutels worden volledig offline beheerd, je ondertekent je transacties op een vertrouwd scherm en de seed is fysiek beschermd in een smartcard die bestand is tegen fysieke aanvallen.



Alles wat je nodig hebt om de installatie te voltooien zijn de volgende items:




- De gebruikelijke uitrusting voor een klassieke SeedSigner: een Raspberry Pi Zero, een Waveshare 1,3" scherm, een compatibele camera en een microSD kaart (meer details vind je in de SeedSigner tutorial hieronder);
- De SeedSigner uitbreidingskit, verkrijgbaar [op de officiële Satochip winkel](https://satochip.io/product/seedsigner-extension-kit/), waarmee je direct vanaf je SeedSigner kunt lezen en schrijven naar de smartcard. Een andere optie is om een externe smartcardlezer te gebruiken, die je met een kabel kunt aansluiten op een Micro-USB poort van de Raspberry Pi. Ik heb deze oplossing echter nog niet zelf getest;
- Een Seedkeeper, of anders een lege smartcard waarop je de Seedkeeper applet kunt installeren (de uitbreidingskit die door Satochip wordt verkocht bevat al een lege smartcard).



![Image](assets/fr/01.webp)



Deze tutorial behandelt twee scenario's:




- Als je al een Bitcoin portfolio hebt die je via je SeedSigner beheert, installeer dan gewoon de nieuwe firmware. Je kunt dan je bestaande wallet blijven gebruiken, dit keer met Seedkeeper voor extra beveiliging.
- Als je nog geen Bitcoin wallet aan je SeedSigner hebt gekoppeld, moet je de stappen **5** en **6** van de onderstaande tutorial volgen. Deze secties leggen uit hoe je een mnemonische zin generate met de SeedSigner kunt maken, opslaan via een *SeedQR*, en dan deze wallet verbinden met Sparrow Wallet om het te beheren. Ik ga hier niet in op deze procedures en **ik ga ervan uit dat je al een werkende Bitcoin wallet hebt, geconfigureerd met Sparrow en je SeedSigner**.



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 1. Firmware installeren



Om je SeedSigner met een Seedkeeper te gebruiken, moet je een alternatieve firmware installeren, anders dan die van de originele SeedSigner, om het lezen van smartcards te ondersteunen. Hiervoor [raad ik aan fork van "*3rdIteration*"](https://github.com/3rdIteration/seedsigner) te gebruiken. Download [de laatste versie van de image](https://github.com/3rdIteration/seedsigner/releases) (`.zip`) die overeenkomt met het Raspberry Pi-model dat je gebruikt.



![Image](assets/fr/02.webp)



Download de [Balena Etcher] software (https://etcher.balena.io/) als je die nog niet hebt en ga dan als volgt te werk:




- Plaats de microSD-kaart in uw computer;
- Lanceer Etcher ;
- Selecteer het bestand `.zip` dat je zojuist hebt gedownload;
- Selecteer de microSD-kaart als doel;
- Klik op `Flash!`.



![Image](assets/fr/03.webp)



Wacht tot het proces is voltooid: je microSD is nu klaar voor gebruik. Je kunt nu verder gaan met het in elkaar zetten van je apparaat.



Voor meer details over het installeren van de firmware en het verifiëren van de software (een stap die ik ten zeerste aanraad), zie de volgende tutorial:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 2. De smartcardlezer monteren



![video](https://youtu.be/jqE8HDMCImA)



Installeer eerst de camera op de Raspberry Pi Zero, steek hem voorzichtig in de camera-pen en vergrendel hem met het zwarte lipje. Plaats vervolgens de Pi op de bodem van de behuizing en zorg ervoor dat de poorten uitgelijnd zijn met de corresponderende openingen.



![Image](assets/fr/04.webp)



Sluit vervolgens de smartcardlezer aan op de GPIO-pinnen van de Raspberry Pi Zero.



![Image](assets/fr/05.webp)



Schuif het plastic afdekplaatje over de smartcardlezer tot het correct geplaatst is.



![Image](assets/fr/06.webp)



Voeg vervolgens het scherm toe aan de GPIO-pinnen van de uitbreiding.



![Image](assets/fr/07.webp)



Plaats ten slotte de microSD-kaart met de firmware in de poort aan de zijkant van de Raspberry Pi Zero.



![Image](assets/fr/08.webp)



Je kunt je SeedSigner nu aansluiten via de Micro-USB poort van de Raspberry Pi Zero, of via de USB-C poort van de uitbreiding. Beide opties werken. Wacht een paar seconden voor het opstarten, dan zou je het welkomstscherm moeten zien verschijnen.



![Image](assets/fr/09.webp)



Voor meer details over de initiële setup van je SeedSigner, raad ik je de volgende tutorial aan:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 3. Flash een smartcard met de Seedkeeper-applet (optioneel)



![video](https://youtu.be/NF4HemyEcOY)



Als je al een Seedkeeper hebt, kun je deze stap overslaan en direct naar stap 4 gaan. In dit gedeelte bekijken we hoe je de Seedkeeper applet op een lege smartcard installeert (doe-het-zelf methode).



Open om te beginnen het menu `Tools > Smartcard Tools` op uw SeedSigner.



![Image](assets/fr/10.webp)



Selecteer vervolgens `DIY Tools > Install Applet`.



![Image](assets/fr/11.webp)



Steek je smartcard in de SeedSigner lezer met de chip naar beneden en kies dan de `SeedKeeper` applet.



![Image](assets/fr/12.webp)



Wees geduldig tijdens de installatie: het proces kan enkele tientallen seconden duren.



![Image](assets/fr/13.webp)



Als de applet met succes is geïnstalleerd, kun je doorgaan naar stap 4.



![Image](assets/fr/14.webp)



## 4. Een bestaande SeedQR opslaan op Seedkeeper



![video](https://youtu.be/X-vmFHU9Ec8)



Nu je Seedkeeper operationeel is, kun je je Bitcoin wallet mnemonic op de smartcard opslaan. Om te beginnen zet je zoals gewoonlijk je SeedSigner aan en scan je de *SeedQR* van je wallet om hem in het apparaat te laden. Zodra de seed is geïmporteerd, selecteer je gewoon `Done`.



![Image](assets/fr/15.webp)



Wanneer de seed geladen is, open dan het `Backup Seed` menu.



![Image](assets/fr/16.webp)



Plaats dan je Seedkeeper in de SeedSigner drive en selecteer de `To SeedKeeper` optie.



![Image](assets/fr/17.webp)



De SeedSigner zal je dan vragen om een pincode in te voeren voor jouw Seedkeeper. Aangezien dit een lege kaart is, is er nog geen code gedefinieerd. Voer een willekeurige code in om deze stap over te slaan en valideer vervolgens.



![Image](assets/fr/18.webp)



SeedSigner detecteert dat Seedkeeper nog niet is geïnitialiseerd (d.w.z. er is nog geen wachtwoord ingesteld). Klik op `Ik begrijp het` om verder te gaan.



![Image](assets/fr/19.webp)



Kies nu de nieuwe PIN-code van je Seedkeeper, tussen de 4 en 16 tekens. Kies voor extra veiligheid een lange, willekeurige code: het is de enige barrière die fysieke toegang tot je geheugensteuntje beschermt.



Vergeet niet om deze PIN-code op te slaan zodra deze is aangemaakt, in een betrouwbare wachtwoordmanager of op een aparte fysieke drager, afhankelijk van je strategie. In het laatste geval moet je ervoor zorgen dat je het medium met de PIN-code nooit op dezelfde plek bewaart als je Seedkeeper, anders is de bescherming niet meer effectief. Het is belangrijk om een reservekopie te hebben: **Zonder deze PIN heb je geen toegang tot je seed en gaan je bitcoins verloren**.



![Image](assets/fr/20.webp)



Je kunt dan een `label` koppelen aan je geheugensteuntje. Dit label is handig als je meerdere geheimen op Seedkeeper opslaat, zodat je ze gemakkelijk kunt identificeren.



![Image](assets/fr/21.webp)



Je geheugensteunzin is nu opgeslagen op de smartcard.



![Image](assets/fr/22.webp)



Qua beveiligingsstrategie zijn er verschillende benaderingen mogelijk, afhankelijk van je behoeften en het niveau van risicoblootstelling. Persoonlijk raad ik aan om minstens 2 kopieën van je seed te bewaren:




- Dit is een primeur voor smartcards, die je gemakkelijk toegankelijk kunt houden voor alledaagse handelingen, zoals het verifiëren van adressen of het ondertekenen van transacties. Deze methode is praktisch (zoals we in deel 5 zullen zien) en blijft veilig dankzij de bescherming die de pincode biedt, dus je kunt hem zonder grote risico's toegankelijk houden;
- Een tweede kopie van je niet-versleutelde mnemotechnische zin, die dient als ultieme back-up van je portfolio en die alleen wordt gebruikt in geval van verlies of diefstal van de Seedkeeper. Aangezien deze versie onversleuteld is, moet deze op een aparte, veiligere locatie worden bewaard om te voorkomen dat de 2 back-ups tegelijkertijd worden gecompromitteerd.



Afhankelijk van je beveiligingsstrategie en risicoprofiel kun je de seed ook dupliceren op verschillende Seedkeepers, of meerdere fysieke kopieën van de mnemonic maken. Bekijk de volgende tutorial voor meer informatie over deze praktijken:



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270


## 5. Een seed laden van Seedkeeper



![video](https://youtu.be/ms0Iq_IyaoE)



Je kunt nu je Seedkeeper gebruiken om je mnemonische zin bij het opstarten in de SeedSigner te laden en zo je Bitcoin transacties te ondertekenen. Om te beginnen, zet je je SeedSigner aan door hem in te pluggen, open dan het `Seeds` menu.



![Image](assets/fr/23.webp)



Selecteer dan de optie `From SeedKeeper`.



![Image](assets/fr/24.webp)



Steek uw Seedkeeper in de smartcardlezer en voer uw pincode in om de kaart te ontgrendelen. Bevestig je invoer door rechtsonder op de bevestigingstoets `KEY3` te drukken.



![Image](assets/fr/25.webp)



Seedkeeper kan meerdere geheimen bevatten, dus SeedSigner vraagt je dan om degene te kiezen die je wilt laden. Het weergegeven label komt overeen met de naam die je in stap 4 hebt gedefinieerd. Als je, zoals in mijn geval, maar één seed hebt geregistreerd, is er maar één optie beschikbaar.



![Image](assets/fr/26.webp)



Je seed is nu geladen. Controleer of dit de juiste wallet is door de vingerafdruk die op het scherm verschijnt te vergelijken met de vingerafdruk die in je Sparrow Wallet instellingen staat. Deze vingerafdruk werd ook gegeven toen de wallet voor het eerst werd aangemaakt.



Als je een passphrase gebruikt, kun je die in dit stadium toepassen (zie deel 6 van deze tutorial). Klik anders gewoon op `Gedaan`.



![Image](assets/fr/27.webp)



Je kunt je wallet dan gewoon gebruiken: controleer je afleveradressen en onderteken transacties, net als met een klassieke SeedSigner. Om meer te weten te komen over het gebruik, zie de speciale tutorial :



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 6. Seedkeeper gebruiken met een passphrase BIP39



Gebruik je een passphrase om je Bitcoin portfolio te beschermen? U kunt deze ook registreren in uw Seedkeeper, naast uw seed. Met deze oplossing kunt u uw wallet snel laden op de SeedSigner, zonder dat u de passphrase elke keer handmatig hoeft in te voeren op het kleine toetsenbord.



Ik vind deze methode bijzonder interessant, omdat je zo kunt profiteren van de beveiligingsvoordelen van de passphrase, terwijl je de beperkingen van het dagelijks gebruik wegneemt. Hier is een voorbeeld van een configuratie die ik zou aanraden:




- Bewaar je seed en passphrase in een Seedkeeper, beveiligd met een sterke PIN-code (dit is belangrijk). Met deze back-up kun je je wallet gemakkelijk dagelijks gebruiken. Als je wilt, kun je deze informatie dupliceren op een tweede Seedkeeper;
- Bewaar ook een duidelijke kopie van je mnemonic en passphrase, op papier of metaal. Dit is je laatste back-up voor het geval je je Seedkeeper of de PIN-code kwijtraakt. Zorg ervoor dat je deze kopieën op verschillende locaties bewaart, zodat ze niet tegelijkertijd gecompromitteerd kunnen worden.



In deze configuratie, als iemand alleen je mnemonische tekst in handen krijgt, kunnen ze niets stelen zonder de passphrase te kennen (vooropgesteld, natuurlijk, dat het sterk genoeg is om een brute-force aanval te weerstaan). Omgekeerd, als iemand jouw passphrase in platte tekst ontdekt, blijft het onbruikbaar zonder de bijbehorende mnemotechnische zin.



Tot slot, als iemand fysieke toegang weet te krijgen tot je Seedkeeper met seed en passphrase, kunnen ze er niets uithalen zonder de PIN-code te kennen. In tegenstelling tot een passphrase kan deze code niet geforceerd worden, omdat de smartcard zichzelf automatisch vergrendelt na 5 ongeldige pogingen.



De veiligheid van deze configuratie is daarom gebaseerd op 2 essentiële punten:




- Een **passphrase strong**: het moet lang en willekeurig zijn en een grote verscheidenheid aan tekens bevatten. De complexiteit ervan is geen probleem voor jou, omdat je het maar één keer hoeft in te voeren op het toetsenbord tijdens de initialisatie; daarna wordt het verzonden door Seedkeeper ;
- Een **sterke pincode** voor Seedkeeper: ook willekeurig en bestaande uit 16 tekens.



Om deze setup op te zetten, begin je met het laden van je passphrase in de SeedSigner op de gebruikelijke manier. Je kunt de procedure in deze tutorial volgen:



https://planb.academy/tutorials/wallet/backup/seedsigner-passphrase-7a61f64d-aa03-4bcf-8308-00c89a74cffe

Zodra uw portefeuille met passphrase correct is geladen op de SeedSigner, opent u het menu `Zaad` en selecteert u de footprint die overeenkomt met deze portefeuille. Merk op dat deze footprint verschilt van die van de portfolio zonder passphrase.



![Image](assets/fr/28.webp)



Klik dan op `Backup Seed`, plaats de Seedkeeper in het station en selecteer `To SeedKeeper`.



![Image](assets/fr/29.webp)



Voer je PIN in om Seedkeeper te ontgrendelen en wijs dan een label toe aan dit geheim. Je kunt de vingerafdruk als label laten staan om een vorm van plausibele ontkenning te behouden, of bijvoorbeeld expliciet `Passphrase Wallet` vermelden.



![Image](assets/fr/30.webp)



Je passphrase portfolio is nu geregistreerd op Seedkeeper.



![Image](assets/fr/31.webp)



De volgende keer dat je opstart, plaats je gewoon je Seedkeeper in de drive en navigeer je naar `Seeds > From SeedKeeper`.



![Image](assets/fr/32.webp)



Voer uw pincode in om de smartcard te ontgrendelen en selecteer vervolgens de wallet die overeenkomt met uw passphrase.



![Image](assets/fr/33.webp)



Controleer de passphrase en je wallet opdruk en bevestig.



![Image](assets/fr/34.webp)



Je hebt nu toegang tot je portfolio met passphrase en kunt je transacties ondertekenen zoals je normaal zou doen op een SeedSigner.



## 7. Extra opties



In het menu `Tools > Smartcard Tools` vind je verschillende opties om je Seedkeeper te beheren:





- In het menu `Common Tools` kun je :
 - Controleer de echtheid van de kaart;
 - PIN-code wijzigen ;
 - Wijzig de labels die bij je geheimen horen;
 - NFC-functie uitschakelen (aanbevolen bij gebruik van alleen chipreader) ;
 - Voer een fabrieksreset uit.





- In het `SeedKeeper Functies` menu kun je :
 - Raadpleeg de lijst van geregistreerde geheimen ;
 - Een nieuw geheim opslaan ;
 - Een bestaand geheim verwijderen ;
 - Je descriptoren opslaan of laden (handige functie voor multi-sig portfolio's).





- In het menu `DIY Tools` kun je :
 - De Seedkeeper-applet compileren ;
 - Installeer de applet op een lege kaart ;
 - Verwijder een Seedkeeper-applet om deze te resetten en weer leeg te maken.



Nu weet je hoe je Seedkeeper kunt gebruiken om veilig een back-up te maken van je portfolio in combinatie met SeedSigner.



Als deze opstelling je heeft overtuigd, aarzel dan niet om de projecten te steunen die dit mogelijk maken:




- Door uw apparatuur rechtstreeks [op de website van Satochip] te kopen (https://satochip.io/shop/);
- Door [een donatie te doen aan het SeedSigner project](https://seedsigner.com/donate/);
- Door u te abonneren op het YouTube-kanaal van [Crypto Guide] (https://www.youtube.com/@CryptoGuide/), dat wordt beheerd door de persoon die de GitHub-repository onderhoudt waarop de gewijzigde firmware staat.