---
name: Ashigaru Terminal
description: Gebruik Ashigaru op het bureaublad om coinjoins te maken
---

![cover](assets/cover.webp)



Ashigaru Terminal is de aanpassing van het Ashigaru team van Sparrow Server, die het Whirlpool coinjoin protocol implementeert. Deze software is een voortzetting van het werk begonnen door Samourai Wallet, in het bijzonder de Whirlpool GUI, waarvan het de fundamentele principes overneemt: zelfbehoud en vertrouwelijkheid.



Deze software is een fork van Sparrow Server, aangepast en geoptimaliseerd voor volledige integratie met het Whirlpool ecosysteem, het ZeroLink coinjoin protocol dat oorspronkelijk ontwikkeld is door de Samourai teams.



Ashigaru Terminal werkt met een minimalistische TUI-interface en kan op een pc of een dedicated server worden geïnstalleerd. Het laat je direct communiceren met Whirlpool om "*Tx0*" te initiëren, "*Deposit*", "*Premix*", "*Postmix*" en "*Badbank*" accounts te beheren en automatische remixes uit te voeren om de vertrouwelijkheid van je onderdelen te versterken.



Kortom, Ashigaru Terminal is vooral handig als je coinjoins wilt maken met Whirlpool.



In deze eerste tutorial neem ik je mee door de installatie en werking van Ashigaru Terminal. Een tweede, meer geavanceerde tutorial zal dan gewijd zijn aan het daadwerkelijk creëren van coinjoins.



https://planb.academy/tutorials/privacy/on-chain/ashigaru-whirlpool-e566803d-ab3f-4d98-9136-5462009262ef

## 1. Ashigaru-terminal installeren



Om Ashigaru Terminal te installeren heb je Tor Browser nodig, omdat de binaries alleen via het Tor netwerk worden gedistribueerd. Als je dit nog niet hebt gedaan, [installeer het op je machine](https://www.torproject.org/download/).



### 1.1. download Ashigaru Terminal



Ga vanuit Tor Browser naar [de releases pagina van hun Git repository](http://ashicodepbnpvslzsl2bz7l2pwrjvajgumgac423pp3y2deprbnzz7id.onion/Ashigaru/Ashigaru-Terminal/releases/) om de laatste versie van Ashigaru Terminal voor je besturingssysteem te downloaden.



```txt
ashicodepbnpvslzsl2bz7l2pwrjvajgumgac423pp3y2deprbnzz7id.onion/Ashigaru/Ashigaru-Terminal/releases/
```



![Image](assets/fr/01.webp)



Download de volgende 2 bestanden voor je besturingssysteem:




- De binary (`ashigaru_terminal_v1.0.0_amd64.deb` voor Debian/Ubuntu, `.dmg` voor macOS of `.zip` voor Windows) ;
- Het ondertekende hashes-bestand: `ashigaru_terminal_v1.0.0_signed_hashes.txt`.



### 1.2. Controleer de Ashigaru-terminal



Voordat je de software op je apparaat draait, moet je de authenticiteit en integriteit ervan controleren. Dit is een belangrijke stap, omdat het voorkomt dat je een frauduleuze versie installeert die je bitcoins in gevaar kan brengen of je machine kan infecteren.



Open een nieuw browserscherm en ga naar [Keybase verificatietool](https://keybase.io/verify). Plak de inhoud van het `.txt` bestand dat je net hebt gedownload in het daarvoor bestemde veld en klik dan op de `Verifieer` knop.



![Image](assets/fr/02.webp)



Om je verificatiebronnen te diversifiëren, kun je het bericht ook vergelijken met het bericht dat beschikbaar is op de clearnet [ashigaru.rs](https://ashigaru.rs/download/) site, in de `/download` sectie.



![Image](assets/fr/03.webp)



Als de handtekening geldig is, zal Keybase een bericht weergeven dat bevestigt dat het bestand is ondertekend door de ontwikkelaars van Ashigaru.



![Image](assets/fr/04.webp)



Je kunt ook klikken op het `ashigarudev` profiel dat wordt weergegeven door Keybase en controleren of hun sleutelvingerafdruk precies overeenkomt met : `A138 06B1 FA2A 676B`.



![Image](assets/fr/05.webp)



Als er in dit stadium een foutmelding verschijnt, is de handtekening ongeldig. In dit geval **installeer de gedownloade software** niet. Begin opnieuw bij het begin of vraag de community om hulp voordat u verder gaat.



Keybase heeft je voorzien van de geverifieerde hash van de applicatie. We gaan nu controleren of de hash van het `.deb`, `.zip` of `.dmg` bestand dat je hebt gedownload overeenkomt met de hash die is gevalideerd op Keybase. Ga hiervoor naar [HASH FILE ONLINE](https://hash-file.online/).



Klik op de knop `BROWSE...` en selecteer het bestand `.deb`, `.zip` of `.dmg` dat je in stap 1.1 hebt gedownload. Kies dan de hashfunctie `SHA-256` en klik op `CALCULATE HASH` om generate de hash voor je bestand te berekenen.



![Image](assets/fr/06.webp)



De site zal dan de hash van de software weergeven. Vergelijk deze met de hash die je hebt geverifieerd op Keybase.io. Als de twee perfect overeenkomen, is de echtheids- en integriteitscontrole geslaagd. U kunt de software dan gebruiken.



![Image](assets/fr/07.webp)



### 1.3 Start Ashigaru Terminal





- Debian / Ubuntu



Voer het commando :



```bash
cd ~/Downloads
sudo apt install ./ashigaru_terminal_v1.0.0_amd64.deb
```



Pas de volgorde aan volgens de gedownloade versie.



Controleer vervolgens de installatie:



```bash
/opt/ashigaru-terminal/bin/Ashigaru-terminal --version
```



Start vervolgens de software:



```bash
/opt/ashigaru-terminal/bin/Ashigaru-terminal
```





- Vensters**



Klik met de rechtermuisknop op het bestand `.zip` dat je hebt gedownload en gecontroleerd en selecteer vervolgens `Extract All...` om de inhoud uit te pakken.



Zodra het uitpakken is voltooid, dubbelklik je op het bestand `Ashigaru-terminal.exe` om de software te starten.



![Image](assets/fr/08.webp)



## 2. Aan de slag met Ashigaru Terminal



Ashigaru Terminal is een TUI (*Text-based User Interface*) programma, d.w.z. een minimalistische interface die direct in de terminal draait. Je communiceert ermee door middel van menu's en sneltoetsen, maar zonder een echte klassieke grafische omgeving.



![Image](assets/fr/09.webp)



Het is eenvoudig te gebruiken: gebruik de pijltjestoetsen van je toetsenbord om door de menu's te navigeren en druk op de `Enter` toets om een actie te valideren of een keuze te bevestigen.



## 3. Je knooppunt verbinden met Ashigaru Terminal



Standaard maakt Ashigaru Terminal verbinding met een publieke Electrum server. Dit brengt natuurlijk risico's met zich mee in termen van vertrouwelijkheid en soevereiniteit. Dus gaan we het configureren om direct verbinding te maken met uw eigen Electrum Server.



Open hiervoor het menu `Voorkeuren > Server`.



![Image](assets/fr/10.webp)



Klik op de knop `< Bewerken >`.



![Image](assets/fr/11.webp)



Selecteer `Private Electrum Server` en klik dan op `<Continue>`.



![Image](assets/fr/12.webp)



Voer de URL en poort van je server in. Je kunt een Tor-adres opgeven in `.onion`. Klik vervolgens op `< Test >` om de verbinding te verifiëren.



![Image](assets/fr/13.webp)



Als de verbinding succesvol is, verschijnt het bericht `Success`, samen met de gegevens van je server.



![Image](assets/fr/14.webp)



Als je nog geen Bitcoin node hebt, raad ik je aan deze cursus te volgen:



https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426

*In mijn geval ga ik voor deze tutorial de verbinding met mijn Electrs server verbreken, omdat ik op testnet werk. De werking blijft echter strikt identiek op mainnet.*



## 4. Creëer een portfolio op Ashigaru Terminal



Nu de software correct is geconfigureerd, kunnen we een Bitcoin portfolio toevoegen.



Je hebt twee opties:




- Je kunt een nieuwe wallet vanaf nul maken en deze uitsluitend op Ashigaru Terminal gebruiken. In dat geval moet je deze software elke keer openen als je met je wallet wilt communiceren;
- Als alternatief kunt u uw bestaande Ashigaru wallet rechtstreeks vanaf uw telefoon in Ashigaru Terminal importeren. Het nadeel van deze methode is dat het de veiligheid van je installatie iets vermindert, omdat je wallet dan wordt blootgesteld aan twee risicovolle omgevingen in plaats van één. Aan de andere kant biedt het het voordeel dat je Ashigaru Terminal continu kunt laten draaien om je munten te mixen, terwijl je ze op afstand kunt uitgeven via de Ashigaru mobiele app.



In deze tutorial kiezen we voor de tweede methode. Als je echter liever een volledig nieuwe portfolio aanmaakt, blijft de procedure hetzelfde: het enige verschil is tijdens het aanmaken, wanneer je je nieuwe mnemonische zin en je nieuwe passphrase moet opslaan.



Let er ook op dat Ashigaru Terminal niet toestaat dat je je bitcoins direct uitgeeft. Je kunt dezelfde wallet synchroniseren op Ashigaru Terminal en de Ashigaru-app (wat ik in deze handleiding zal doen), of op Sparrow Wallet.



Als je nog geen wallet hebt op de Ashigaru-toepassing, kun je de speciale tutorial volgen:



https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f

Ga naar het menu `Wallets`.



![Image](assets/fr/15.webp)



Selecteer vervolgens `Maak/herstel wallet...`. Met de optie `Open Wallet...` kun je op een later tijdstip een portefeuille openen die al in Ashigaru Terminal is opgeslagen.



![Image](assets/fr/16.webp)



Geef je portfolio een naam.



![Image](assets/fr/17.webp)



Kies dan portfoliotype `Hot Wallet`.






![Image](assets/fr/18.webp)



In dit stadium verschilt de procedure afhankelijk van je eerste keuze:




- Als je een nieuwe portefeuille vanaf nul wilt aanmaken, klik dan op `<Nieuw Wallet>`, definieer een passphrase BIP39, sla dan zorgvuldig je mnemonische zin en je passphrase op een fysieke drager op;



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270



- Als u dezelfde wallet wilt gebruiken als uw Ashigaru-toepassing, voer dan de 12 woorden van uw mnemonische zin en uw passphrase BIP39 rechtstreeks in de overeenkomstige velden in. Schrijf de woorden in kleine letters, heel, in volgorde, gescheiden door een spatie, zonder cijfers of extra tekens.



Zodra deze stap is voltooid, klikt u op `< Volgende >`.



*Opmerking*: Als je niet op deze knop kunt klikken, is je mnemonische zin ongeldig. Controleer zorgvuldig of geen van de woorden onjuist of verkeerd gespeld is.



![Image](assets/fr/19.webp)



Vervolgens moet je een wachtwoord instellen. Dit wordt gebruikt om je Ashigaru Terminal wallet te ontgrendelen en te beschermen tegen ongeautoriseerde fysieke toegang. Het is niet betrokken bij de cryptografische afleiding van uw sleutels: met andere woorden, zelfs zonder dit wachtwoord kan iedereen met uw geheugensteuntje en passphrase uw wallet herstellen en toegang krijgen tot uw bitcoins.



Kies een lang, complex, willekeurig wachtwoord. Bewaar een kopie op een veilige plaats: idealiter op een fysieke drager of in een veilige wachtwoordmanager.



Klik op `< OK >` als je klaar bent.



![Image](assets/fr/20.webp)



## 5. De portfolio gebruiken



Je kunt dan kiezen welke account je wilt gebruiken. Op dit moment hebben we nog geen mixen geïnitieerd, dus openen we de `Deposit` account.



![Image](assets/fr/21.webp)



De bediening is dan identiek aan die van Sparrow, aangezien Ashigaru Terminal een fork van Sparrow Server is. Je vindt dezelfde menu's:



![Image](assets/fr/22.webp)





- transacties": hiermee kun je de geschiedenis van de transacties bekijken die aan deze rekening zijn gekoppeld. In mijn geval verschijnen er al enkele, omdat ik er al enkele had gemaakt met de Ashigaru-toepassing op dezelfde wallet.



![Image](assets/fr/23.webp)





- ontvangen`: genereert een nieuw, leeg ontvangstadres voor het plaatsen van satss op de depositorekening.



![Image](assets/fr/24.webp)





- adressen`: toont een lijst met al je adressen, ongeacht of ze tot de interne of externe keten van je account behoren.



![Image](assets/fr/25.webp)





- `UTXOs`: geeft een lijst van alle beschikbare UTXOs.



![Image](assets/fr/26.webp)





- instellingen: geeft toegang tot de *descriptor* van je portefeuille. Je kunt er ook je seed raadplegen, de *Gap Limit* aanpassen of de aanmaakdatum van je portefeuille wijzigen.



![Image](assets/fr/27.webp)



Je weet nu hoe je Ashigaru Terminal installeert en gebruikt. In de volgende handleiding zullen we zien hoe je coinjoins uitvoert met deze software en hoe je fondsen beheert in "*Postmix*".
https://planb.academy/tutorials/privacy/on-chain/ashigaru-whirlpool-e566803d-ab3f-4d98-9136-5462009262ef
