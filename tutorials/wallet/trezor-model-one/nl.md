---
name: Trezor Model One
description: Instellen en gebruiken van de Hardware Wallet Model One
---
![cover](assets/cover.webp)



*Afbeelding credit: [Trezor.io](https://trezor.io/)*



De Trezor Model One is de allereerste Hardware Wallet die ooit werd uitgebracht, gelanceerd in 2014 door SatoshiLabs. Na meer dan tien jaar blijft het een interessante keuze, vooral voor gebruikers die op zoek zijn naar een Hardware Wallet die zowel technisch als budgettair toegankelijk is. Op de officiële website van Trezor kost hij €49. Het is een van de enige hardware wallets in deze prijsklasse. Hij houdt het midden tussen instapmodellen van rond de €20, zoals de Tapsigner, die vaak geen scherm hebben, en toestellen uit het middensegment van rond de €80, zoals de Ledger Nano S Plus of de Trezor Safe 3.



De Model One heeft een 0,96 inch monochroom OLED-scherm en twee fysieke knoppen. Hij werkt zonder batterij en gebruikt alleen een micro-USB-aansluiting voor stroom en data Exchange.



![Image](assets/fr/01.webp)



Het grootste nadeel van het Model One is het ontbreken van secure element, waardoor het kwetsbaar is voor verschillende fysieke aanvallen, waarvan sommige relatief eenvoudig uit te voeren zijn. Deze aanvallen kunnen bestaan uit de analyse van hulpkanalen om de PIN-code van het apparaat te bepalen, of geavanceerdere technieken om de versleutelde seed te ontfutselen om deze later te brute-forcen. Merk op dat deze aanvallen fysieke toegang tot het apparaat vereisen. Deze kwetsbaarheid kan echter aanzienlijk verminderd worden door een degelijke passphrase BIP39 te gebruiken. Als je voor deze Hardware Wallet kiest, raad ik je sterk aan om een passphrase te configureren.



Het Model One biedt twee belangrijke voordelen:




- Het is gebaseerd op een volledig open-source architectuur. In tegenstelling tot recentere modellen met secure element zijn alle hardware- en softwarecomponenten van Model One controleerbaar;
- Hij is uitgerust met een scherm. Bij mijn weten is dit de enige Hardware Wallet op de markt in deze prijsklasse met een scherm. Dit is een zeer belangrijke functie, omdat hiermee ondertekende informatie en ontvangstadressen kunnen worden geverifieerd, waardoor veel digitale aanvallen worden voorkomen.



De Trezor Model One kan daarom een verstandige keuze zijn voor beginners en gemiddelde gebruikers met een beperkt budget. Het is echter belangrijk om bewust te blijven van zijn beperkingen op het gebied van fysieke bescherming, vanwege de afwezigheid van secure element. Als je budget beperkt is, is dit een goede optie, maar als je het je kunt veroorloven om te kiezen voor een superieur model, zoals de Trezor Safe 3 voor €79, is dat te verkiezen, omdat deze een secure element bevat.



## De Trezor Model One uit de doos



Wanneer u uw Model One ontvangt, controleert u of de doos en Seal intact zijn om te bevestigen dat het pakket niet geopend is. Er wordt ook een softwareverificatie van de authenticiteit en integriteit van het apparaat uitgevoerd wanneer het later wordt ingesteld.



Inhoud van de doos :




- De Trezor Model One;
- Karton om je Mnemonic zin, stickers en instructies op te schrijven;
- USB-A naar micro-USB kabel.



![Image](assets/fr/02.webp)



Navigeren op het apparaat is heel eenvoudig:




- Klik met de rechtermuisknop om te bevestigen en door te gaan naar de volgende stappen;
- Gebruik de linkerknop om terug te gaan.



## Vereisten



In deze tutorial laat ik je zien hoe je de Trezor Model One gebruikt met [Sparrow wallet Wallet management software] (https://sparrowwallet.com/download/). Als je deze software nog niet hebt geïnstalleerd, doe dat dan nu. Als je hulp nodig hebt, hebben we ook een gedetailleerde tutorial over het configureren van Sparrow wallet :



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Je hebt ook de Trezor Suite software nodig om de Model One te configureren, de authenticiteit te controleren en de firmware te installeren. We zullen deze software alleen daarvoor gebruiken en daarna is het alleen nog nodig voor firmware-updates. Voor het dagelijkse beheer van de Wallet gebruiken we Sparrow wallet, omdat het geoptimaliseerd is voor Bitcoin en makkelijk te gebruiken, zelfs voor beginners (Sparrow ondersteunt alleen Bitcoin, geen altcoins).



[Trezor Suite downloaden van de officiële website](https://trezor.io/trezor-suite)



![Image](assets/fr/03.webp)



Voor beide programma's raad ik je sterk aan om zowel de authenticiteit (met GnuPG) als de integriteit (via Hash) te controleren voordat je ze op je machine installeert. Als je niet weet hoe je dit moet doen, kun je deze andere tutorial volgen:



https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

## De Trezor Model One starten



Sluit uw Model One aan op uw computer waarop Trezor Suite en Sparrow wallet al zijn geïnstalleerd.



![Image](assets/fr/04.webp)



Open Trezor Suite en klik op "*Mijn Trezor instellen*".



![Image](assets/fr/05.webp)



Selecteer "*Bitcoin-only firmware*" en klik vervolgens op "*Installeer Bitcoin-only*".



![Image](assets/fr/06.webp)



Trezor Suite installeert vervolgens de firmware op uw Model One. Wacht even tijdens de installatie.



![Image](assets/fr/07.webp)



Klik op "*Doorgaan*".



![Image](assets/fr/08.webp)



## Een Bitcoin Wallet maken



Klik in Trezor Suite op de knop "*Nieuw Wallet* aanmaken".



![Image](assets/fr/09.webp)



Accepteer de gebruiksvoorwaarden op de Hardware Wallet.



![Image](assets/fr/10.webp)



Klik in Trezor Suite op "*Doorgaan met back-up*".



![Image](assets/fr/11.webp)



De software geeft instructies voor het beheren van je Mnemonic zin.



Deze Mnemonic geeft je volledige, onbeperkte toegang tot al je bitcoins. Iedereen die in het bezit is van deze zin kan je geld stelen, zelfs zonder fysieke toegang tot je Trezor Model One.



De 24-woorden zin herstelt de toegang tot je bitcoins in geval van verlies, diefstal of breuk van je Hardware Wallet. Het is daarom heel belangrijk om het zorgvuldig te bewaren en op een veilige plek op te bergen.



Je kunt het op het meegeleverde karton schrijven, of voor extra veiligheid raad ik aan om het op een roestvrijstalen basis te graveren om het te beschermen tegen brand, overstroming of instorting.



Bevestig de instructies en klik dan op de knop "*Create Wallet backup*".



![Image](assets/fr/12.webp)



De Model One zal uw Mnemonic zin creëren met behulp van zijn willekeurige nummergenerator. Zorg ervoor dat u tijdens deze handeling niet in de gaten wordt gehouden. Schrijf de woorden op het scherm op een fysieke drager naar keuze. Afhankelijk van je beveiligingsstrategie, kun je overwegen om meerdere volledige fysieke kopieën van de zin te maken (maar verdeel ze vooral niet). Het is belangrijk om de woorden genummerd en in volgorde te houden.



**Het spreekt voor zich dat je deze woorden nooit mag delen op het Internet, zoals ik doe in deze tutorial. Dit voorbeeld Wallet zal alleen gebruikt worden op de Testnet en zal aan het einde van de tutorial verwijderd worden**



Voor meer informatie over de juiste manier om je Mnemonic zinnen op te slaan en te beheren, raad ik je aan deze andere tutorial te volgen, vooral als je een beginner bent:



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Om naar de volgende woorden te gaan, klik je met de rechtermuisknop. Als je alle woorden hebt opgeschreven, klik je opnieuw op de rechterknop om naar de volgende stap te gaan.



![Image](assets/fr/13.webp)



Je Hardware Wallet laat je weer al je woorden zien. Controleer of je ze allemaal hebt opgeschreven.



![Image](assets/fr/14.webp)



## De pincode instellen



Daarna volgt de stap met de PIN-code. De PIN-code ontgrendelt je Trezor. Het biedt dus bescherming tegen onbevoegde fysieke toegang. Deze PIN-code is niet betrokken bij de afleiding van de cryptografische sleutels van uw Wallet. Dus zelfs zonder toegang tot de PIN-code, kunt u met uw 12-woord Mnemonic zin weer toegang krijgen tot uw bitcoins.



Klik op Trezor Suite op "*Doorgaan naar PIN*" en vervolgens op de knop "*Set PIN*".



![Image](assets/fr/15.webp)



Bevestig op Model One.



![Image](assets/fr/16.webp)



We raden je aan een zo willekeurig mogelijke pincode te kiezen. Zorg ervoor dat je deze code opslaat op een andere locatie dan waar je Trezor is opgeslagen (bijvoorbeeld in een wachtwoordmanager). Je kunt een pincode instellen van 8 tot 50 cijfers. Ik raad je aan om een zo lang mogelijke PIN-code te kiezen om de veiligheid te vergroten.



De pincode moet worden ingevoerd in Trezor Suite op uw computer door te klikken op de puntjes die overeenkomen met de cijfers, volgens de toetsenbordconfiguratie die wordt weergegeven op de Trezor Model One.



Deze specifieke PIN-invoermethode is vereist telkens wanneer je je Trezor Model One ontgrendelt, via Trezor Suite of Sparrow wallet.



![Image](assets/fr/17.webp)



Zodra u klaar bent, klikt u op de knop "*PIN invoeren*".



![Image](assets/fr/18.webp)



Schrijf uw PIN-code nogmaals op om te bevestigen.



![Image](assets/fr/19.webp)



Klik in Trezor Suite op de knop "*Complete setup*".



![Image](assets/fr/20.webp)



De configuratie van uw Model One is nu voltooid. Als u wilt, kunt u de naam en startpagina van uw Hardware Wallet wijzigen.



![Image](assets/fr/21.webp)



We hebben de Trezor Suite software niet meer nodig, behalve om regelmatig firmware-updates uit te voeren op je Hardware Wallet, of als je een hersteltest wilt uitvoeren. We gaan nu Sparrow gebruiken om de Wallet te beheren, omdat deze software perfect geschikt is voor Bitcoin-only gebruik.



## De Wallet instellen op de Sparrow wallet



Begin met het downloaden en installeren van Sparrow wallet [van de officiële website](https://sparrowwallet.com/) op je computer, als je dat nog niet hebt gedaan.



Als je Sparrow wallet hebt geopend, zorg er dan voor dat de software is verbonden met een Bitcoin knooppunt, wat wordt aangegeven door het vinkje rechtsonder in Interface. Als je problemen hebt met het aansluiten van Sparrow, raad ik je aan het begin van deze tutorial te raadplegen:



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Klik op het tabblad "*Bestand*" en vervolgens op "*Nieuw Wallet*".



![Image](assets/fr/22.webp)



Geef je Wallet een naam en klik dan op "*Create Wallet*".



![Image](assets/fr/23.webp)



Selecteer in het vervolgkeuzemenu "*Script Type*" het type script dat zal worden gebruikt om je bitcoins te beveiligen. Ik raad "*Taproot*" aan, of anders "*Native SegWit*".



![Image](assets/fr/24.webp)



Klik op de knop "*Gereed voor Hardware Wallet*". Je Model One moet natuurlijk zijn aangesloten op de computer.



![Image](assets/fr/25.webp)



Klik op de knop "*Scan*". Uw Model One wordt nu weergegeven.



Wanneer u uw Model One aansluit op een computer met Sparrow wallet open, wordt u gevraagd een passphrase BIP39 op Sparrow in te voeren. Deze geavanceerde optie wordt in een toekomstige tutorial behandeld. Voor nu kunt u gewoon "*Gar-56 uit*" selecteren om te voorkomen dat uw Trezor u elke keer als u opstart vraagt om een passphrase in te voeren.



https://planb.network/tutorials/wallet/backup/trezor-passphrase-0474b5bf-496f-4f97-aefe-445368fdca42

![Image](assets/fr/26.webp)



Klik op "*Import Keystore*".



![Image](assets/fr/27.webp)



Je ziet nu de details van je Wallet, inclusief de uitgebreide publieke sleutel van je eerste account. Klik op de knop "*Apply*" om het aanmaken van Wallet te voltooien.



![Image](assets/fr/28.webp)



Kies een sterk wachtwoord om de toegang tot Sparrow wallet te beveiligen. Dit wachtwoord zorgt voor veilige toegang tot uw Sparrow wallet-gegevens en beschermt uw publieke sleutels, adressen, labels en transactiegeschiedenis tegen onbevoegde toegang.



Ik raad je aan om dit wachtwoord op te slaan in een wachtwoordmanager zodat je het niet vergeet.



![Image](assets/fr/29.webp)



En nu is jouw Wallet geïmporteerd in Sparrow wallet!



![Image](assets/fr/30.webp)



Voordat je je eerste bitcoins in je Wallet ontvangt, **raad ik je sterk aan om een lege hersteltest** uit te voeren. Schrijf wat referentie-informatie op, zoals je xpub, reset dan je Trezor Model One terwijl de Wallet nog leeg is. Probeer dan je Wallet op de Trezor te herstellen met je papieren back-ups. Controleer of de gegenereerde xpub na het terugzetten overeenkomt met degene die je oorspronkelijk hebt opgeschreven. Als dat zo is, kun je er zeker van zijn dat je papieren back-ups betrouwbaar zijn.



Om meer te leren over hoe je een hersteltest uitvoert, raad ik je aan deze andere tutorial te raadplegen:



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Hoe ontvang je bitcoins met de Trezor Model One?



Klik op Sparrow op het tabblad "*Ontvangen*".



![Image](assets/fr/31.webp)



Voordat je de Address gebruikt die Sparrow wallet voorstelt, controleer je deze op het scherm van je Trezor. Zo kun je bevestigen dat de Address die Sparrow weergeeft niet frauduleus is, en dat de Hardware Wallet inderdaad de privésleutel bevat die nodig is om de bitcoins uit te geven die met deze Address zijn beveiligd. Dit helpt je om verschillende soorten aanvallen te voorkomen.



Om deze controle uit te voeren, klik je op de knop "*Weergave Address*".



![Image](assets/fr/32.webp)



Controleer of de Address op je Trezor overeenkomt met die op Sparrow wallet. Het is ook raadzaam om deze controle uit te voeren vlak voordat je je Address communiceert met de verzender, om zeker te zijn van de geldigheid. Je kunt op de rechterknop drukken om te bevestigen.



![Image](assets/fr/33.webp)



Je kunt ook een "*Label*" toevoegen om de bron van bitcoins te beschrijven die beveiligd zullen worden met deze Address. Dit is een goede manier om je UTXO's beter te beheren.



![Image](assets/fr/34.webp)



Je kunt deze Address dan gebruiken om bitcoins te ontvangen.



![Image](assets/fr/35.webp)



## Hoe verstuur ik bitcoins met de Trezor Model One?



Nu je je eerste Satss hebt ontvangen in je Model One-beveiligde Wallet, kun je ze ook uitgeven! Sluit je Trezor aan op je computer, start Sparrow wallet en ga dan naar het tabblad "*Versturen*" om een nieuwe transactie aan te maken.



![Image](assets/fr/36.webp)



Als je *Coin Controle* wilt, d.w.z. specifiek wilt kiezen welke UTXO's je wilt gebruiken in de transactie, ga dan naar het tabblad "*UTXO's*". Selecteer de UTXO's die je wilt uitgeven en klik dan op "*Verstuur Geselecteerd*". Je wordt doorgestuurd naar hetzelfde scherm in het tabblad "*Versturen*", maar met je UTXO's al geselecteerd voor de transactie.



![Image](assets/fr/37.webp)



Voer de bestemming Address in. U kunt ook meerdere adressen invoeren door op de knop "*+ Add*" te klikken.



![Image](assets/fr/38.webp)



Schrijf een "*Label*" op om het doel van deze uitgave te onthouden.



![Image](assets/fr/39.webp)



Selecteer het bedrag dat naar deze Address moet worden gestuurd.



![Image](assets/fr/40.webp)



Pas het tarief van je transactie aan volgens de huidige markt. Je kunt bijvoorbeeld [Mempool.space](https://Mempool.space/) gebruiken om een geschikt tarief te kiezen.



Zorg ervoor dat al je transactieparameters juist zijn en klik dan op "*Create Transaction*".



![Image](assets/fr/41.webp)



Als alles naar wens is, klik je op "*Transactie voltooien voor ondertekening*".



![Image](assets/fr/42.webp)



Klik op "*Teken*".



![Image](assets/fr/43.webp)



Klik op "*Teken*" naast je Trezor Model One.



![Image](assets/fr/44.webp)



Controleer de transactieparameters op je Hardware Wallet scherm, inclusief de ontvangende Address van de ontvanger, het verzonden bedrag en de kosten. Zodra de transactie is geverifieerd op de Trezor, klik je met de rechtermuisknop om te ondertekenen.



![Image](assets/fr/45.webp)



Je transactie is nu ondertekend. Controleer nog een laatste keer of alles in orde is en klik dan op "*Broadcast Transaction*" om de transactie uit te zenden op het Bitcoin netwerk.



![Image](assets/fr/46.webp)



Je kunt het vinden in het tabblad "*Transacties*" van Sparrow wallet.



![Image](assets/fr/47.webp)



Gefeliciteerd, je bent nu op de hoogte van het basisgebruik van de Trezor Model One met Sparrow wallet! Om nog een stapje verder te gaan, raad ik je deze uitgebreide tutorial aan over het gebruik van een Hardware Wallet Trezor met een passphrase BIP39 om je veiligheid te vergroten:



https://planb.network/tutorials/wallet/backup/trezor-passphrase-0474b5bf-496f-4f97-aefe-445368fdca42

Als je deze tutorial nuttig vond, zou ik je dankbaar zijn als je hieronder een Green duim achterlaat. Voel je vrij om dit artikel te delen op je sociale netwerken. Hartelijk dank!