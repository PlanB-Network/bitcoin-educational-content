---
name: Umbrel
description: Upptäck och installera Umbrel - din Bitcoin-nod och hemserver
---

![cover](assets/cover.webp)


![video](https://youtu.be/qFfhr4sApso)


## Inledning



### Vad är en Bitcoin-nod?



En Bitcoin-nod är en dator som deltar i Bitcoin-nätverket genom att köra Bitcoin Core-programvaran eller en alternativ klient. Dess roll är avgörande för nätverkets drift och säkerhet:





- **Blockchain-lagring**: Upprätthåller en fullständig, uppdaterad kopia av Blockchain Bitcoin
- **Transaktionsverifiering**: validerar varje transaktion och block i enlighet med protokollreglerna
- **Informationsspridning**: Delar nya transaktioner och block med andra noder
- **Skapande av samförstånd**: Bidrar till tillämpningen av nätverksreglerna



Att driva en egen Bitcoin-nod är ett viktigt steg mot finansiell suveränitet och erbjuder flera viktiga fördelar:





- **Konfidentialitet**: Dela dina transaktioner utan att avslöja din information för tredje part
- **Motstånd mot censur**: Ingen kan hindra dig från att använda Bitcoin
- **Oberoende verifiering**: Du behöver inte lita på andras noder för att verifiera dina transaktioner
- **Skapa samförstånd**: Bidra till tillämpningen av Bitcoin:s nätverksregler
- **Stöd till nätverk**: Bli en aktiv deltagare i nätverksdistribution och decentralisering



### Umbrel: En enkel lösning för att driva en Bitcoin-nod



Umbrel är ett operativsystem med öppen källkod som förenklar installation och hantering av en Bitcoin-nod. Det förvandlar också din dator till en personlig och privat hemserver, vilket gör det enkelt att vara värd för :





- En komplett Bitcoin-nod
- Bitcoin viktiga applikationer (Electrs, Mempool.space)
- Andra personliga tjänster (molnlagring, streaming, VPN, etc.)



Med sin eleganta och intuitiva Interface-användare Interface gör Umbrel self-hosting-tjänster tillgängliga för alla, samtidigt som du behåller total kontroll över dina data.



## Alternativ för installation av paraply



Umbrel erbjuder två huvudsakliga sätt att använda sin lösning: ett nyckelfärdigt alternativ (Umbrel Home) och en gratis open source-version (UmbrelOS).



![Comparaison Umbrel Home et UmbrelOS](assets/fr/22.webp)



### Umbrel Home: Den nyckelfärdiga lösningen



Umbrel Home är en förkonfigurerad hemserver, speciellt utformad för en optimal upplevelse. Denna allt-i-ett-hårdvarulösning inkluderar:



**Hårdvarufunktioner**




- Högpresterande processor optimerad för self-hosting
- Förinstallerad SSD-lagring med hög hastighet
- Tyst kylsystem
- Kompakt, elegant design
- Integrerade USB- och Ethernet-portar



**Exklusiva förmåner**




- Plug-and-play-installation: koppla in och sätt igång
- Premiumsupport med dedikerad assistans
- Garanterade automatiska uppdateringar
- Integrerad migreringsguide
- Fullständig hårdvarugaranti
- Fullt stöd för alla funktioner



**Pris**: €399 (priset kan variera beroende på säsong)



### UmbrelOS: Versionen med öppen källkod



UmbrelOS är den kostnadsfria versionen av operativsystemet Umbrel med öppen källkod. Med denna flexibla lösning kan du använda din egen hårdvara och samtidigt dra nytta av Umbrels grundläggande funktioner.



**Förmåner**




- Helt kostnadsfritt
- Öppen, verifierbar källkod
- Frihet att välja
- Avancerade anpassningsmöjligheter



**Plattformar som stöds**




- Raspberry Pi 5: En populär och prisvärd lösning
- X86-system: För standarddatorer eller servrar
- Virtuell maskin: För testning eller användning på befintlig infrastruktur



**Begränsningar**




- Endast gemenskapsstöd
- Vissa avancerade funktioner reserverade för Umbrel Home
- Mer teknisk initial konfiguration
- Prestanda beror på vald hårdvara



Denna version är idealisk för :




- Tekniska användare
- De som redan äger kompatibel utrustning
- Människor som vill lära sig och experimentera
- Utvecklare som vill bidra till projektet



Officiella installationslänkar :




- [Installation på Raspberry Pi 5] (https://github.com/getumbrel/umbrel/wiki/Install-umbrelOS-on-a-Raspberry-Pi-5)
- [Installation på x86-system (https://github.com/getumbrel/umbrel/wiki/Install-umbrelOS-on-x86-Systems)
- [Installation av virtuell maskin] (https://github.com/getumbrel/umbrel/wiki/Install-umbrelOS-on-a-Linux-VM)



I den här handledningen koncentrerar vi oss på att installera UmbrelOS på en Raspberry Pi 5, men de grundläggande principerna är liknande för andra plattformar.



## Installera Umbrel OS på Raspberry Pi 5



### Nödvändiga komponenter



För denna installation behöver du :





- Raspberry Pi 5 (4 GB eller 8 GB RAM)
- En officiell Raspberry Pi-ström Supply (avgörande för stabilitet!)
- MicroSD-kort (minst 32 GB)
- En microSD-kortläsare
- En extern SSD för datalagring
- Ethernet-kabel
- En USB-kabel för att ansluta SSD-enheten



### Steg för installation



**Ladda ner UmbrelOS**



![Téléchargement UmbrelOS](assets/fr/01.webp)




- Besök den [officiella webbplatsen] (https://github.com/getumbrel/umbrel/wiki/Install-umbrelOS-on-a-Raspberry-Pi-5)
- Ladda ner den senaste versionen av UmbrelOS för Raspberry Pi 5



**Balena Etcher** installation



![Téléchargement Balena Etcher](assets/fr/02.webp)




- Ladda ner och installera [Balena Etcher](https://www.balena.io/etcher/) på din dator



**Förberedelse av microSD**-kortet



![Insertion carte microSD](assets/fr/03.webp)




- Sätt i ditt microSD-kort i datorns kortläsare



**Bilden blinkar**



![Flashage UmbrelOS](assets/fr/04.webp)




- Lansering Balena Etcher
- Välj den nedladdade UmbrelOS-imagen
- Välj ditt microSD-kort som destination
- Klicka på "Flash!" och vänta tills processen är klar
- Skjut ut kortet på ett säkert sätt



**Installation av microSD-kort**



![Installation microSD](assets/fr/05.webp)




- Sätt i microSD-kortet i din Raspberry Pi 5



**Perifer anslutning**



![Connexion périphériques](assets/fr/06.webp)




- Anslut den externa SSD-enheten till en tillgänglig USB-port
- Anslut Ethernet-kabeln mellan Pi och din router



**Slå på strömmen**



![Démarrage du Pi](assets/fr/07.webp)




- Anslut den officiella Raspberry Pi-strömförsörjningen Supply
- Vänta några minuter tills systemet har startat



**Första tillträde**



![Accès interface web](assets/fr/08.webp)




- Öppna din webbläsare på en enhet som är ansluten till samma nätverk
- Umbrels Interface-webbplats finns på följande adress `http://umbrel.local`



![Page d'accueil Umbrel](assets/fr/09.webp)



Om `umbrel.local` inte fungerar måste du ta reda på IP Address för din Raspberry Pi i ditt lokala nätverk. Du kan :




- Rådfråga din routers Interface
- Använda en nätverksskanner som nmap
- Använd kommandot `arp -a` i din dators terminal



## Första steget på Umbrel



När din Umbrel är startad och tillgänglig via din webbläsare följer du dessa steg för att komma igång:



### Inledande konfiguration



**Skapa ditt konto**



![Création compte](assets/fr/10.webp)




- Välj ett användarnamn
- Ange ett säkert lösenord
- Du behöver dessa inloggningsuppgifter för att komma åt din Umbrel



**Bekräftelse av konto**



![Confirmation compte](assets/fr/11.webp)




- Klicka på "Nästa" för att komma till din instrumentpanel



**Upptäckten av Interface**



![Interface Umbrel](assets/fr/12.webp)




- Få tillgång till Umbrel App Store
- Upptäck de många tillgängliga applikationerna
- Låt oss börja med att installera de viktigaste applikationerna för Bitcoin



### Installera Bitcoin-applikationer



**Bitcoin Node**



![Bitcoin Node](assets/fr/13.webp)




- Första programmet att installera
- Ladda ner och kontrollera hela Blockchain Bitcoin



**Electrs**



![Installation Electrs](assets/fr/14.webp)




- Electrum-server för anslutning av Bitcoin-plånböcker
- Synkroniseras med din Bitcoin-nod



**Mempool**



![Installation Mempool](assets/fr/15.webp)




- Interface display för Blockchain
- Spårar transaktioner och blockeringar i realtid



## Spåra en transaktion med Mempool.space



Mempool.space är en Blockchain-utforskare med öppen källkod som ger visualisering i realtid av Bitcoin-nätverket. Det låter dig spåra dina transaktioner och förstå hur transaktioner sprids i nätverket.



### Förstå Mempool och bekräftelser



"Mempool" (minnespoolen) är som ett virtuellt väntrum där alla obekräftade Bitcoin-transaktioner lagras innan de inkluderas i ett block. Så här behandlas en transaktion:



1. **Sändning**: När du skickar en transaktion sänds den först ut i Bitcoin-nätverket


2. **Väntar i Mempool**: Väntar på att bli utvald av en Miner på grundval av kostnader


3. **Första bekräftelsen**: En minderårig inkluderar det i ett block (1:a bekräftelsen)


4. **Ytterligare bekräftelser**: Varje nytt block som bryts efter det som innehåller din transaktion lägger till en bekräftelse



Det rekommenderade antalet bekräftelser beror på hur mycket :




- För små belopp: 1-2 bekräftelser kan räcka
- För stora belopp: 6 bekräftelser anses i allmänhet vara mycket säkert



### Utforska Interface från Mempool.space



1. **Hemsidan** ger dig en översikt över Bitcoin-nätverket:




   - Nyligen utvunna block
   - Kostnadsberäkningar för olika prioriteringar
   - Det aktuella läget för Mempool



![Page d'accueil de Mempool.space avec visualisation des blocs et estimations de frais](assets/fr/23.webp)



2. **Sök efter en transaktion**: För att spåra en specifik transaktion, klistra in dess identifierare (txid) i sökfältet högst upp på sidan.



![Recherche d'une transaction dans Mempool.space](assets/fr/24.webp)



### Analysera transaktionsdetaljer



När din transaktion har hittats presenterar Mempool.space dig med en fullständig analys:



1. **Väsentlig information** :




   - Status (bekräftad eller ej)
   - Betalda kostnader (i Sats/vB)
   - Beräknad bekräftelsetid



![Détails des frais et statut de la transaction](assets/fr/25.webp)



2. **Transaktionsstruktur** :




   - Visuell representation av inmatningar och utmatningar
   - Detaljerad lista över berörda adresser
   - Överförda belopp



3. **Tekniska data** :




   - Transaktionens vikt
   - Virtuell storlek
   - Format och version som används
   - Andra specifika metadata



![Informations techniques et structure des entrées/sorties](assets/fr/26.webp)



### Fördelar med att använda Mempool.space på Umbrel



1. **Konfidentialitet**: Dina förfrågningar går via din egen nod


2. **oberoende**: Inget behov av att förlita sig på en tredjepartstjänst


3. **Säkerhet**: Tillgång till data även när offentliga webbläsare ligger nere



Med den här applikationen kan du effektivt övervaka dina transaktioner, förstå hur avgifter påverkar bekräftelsehastigheten och få en bättre förståelse för hur Bitcoin-nätverket fungerar.



## Ansluta en Wallet Bitcoin till din nod



### Electrs konfiguration



**Lokal anslutning**



![Connexion locale](assets/fr/18.webp)




- För användning i ditt lokala nätverk
- Snabbare och enklare att installera



**Fjärranslutning via Tor**



![Connexion Tor](assets/fr/19.webp)




- För att komma åt din nod från var som helst
- Säkrare och mer privat



### Anslutning med Sparrow wallet



**Tillgång till parametrar**



![Paramètres Sparrow](assets/fr/20.webp)




- Öppna Sparrow wallet
- Gå till Inställningar > Server
- Klicka på "Ändra befintlig anslutning"



**Val av anslutningstyp**



Sparrow erbjuder tre anslutningslägen:



***Publik server***




- Anslutning till offentliga servrar (t.ex. blockstream.info, Mempool.space)
- Enkelt men mindre privat



***Bitcoin Core***




- Direkt anslutning till en Bitcoin-nod
- Privat men långsammare



***Privat elektrum***




- Anslut till din ElectrS-server
- Kombinerar integritet och prestanda



**Electrs** konfiguration



Välj anslutningstyp med hjälp av den information som visas i Electrs-programmet som vi såg tidigare:



I båda fallen ska du inte markera alternativen "Använd SSL" och "Använd proxy".



**Lokal anslutning**


Värd: umbrel.local


Portnummer: 50001



**Fjärranslutning (Tor)**


Värd : [din-Address-onion]


Portnummer: 50001



Tor-anslutningen är nödvändig om du vill komma åt din nod utanför ditt lokala nätverk.



![Configuration connexion](assets/fr/21.webp)


För mer information om Sparrow wallet-programvaran har vi en omfattande handledning :


https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d
## Slutsats



Din Umbrel är nu redo att användas. Du deltar aktivt i Bitcoin-nätverket samtidigt som du behåller full kontroll över dina data. Utforska gärna de många andra applikationer som finns tillgängliga i Umbrel App Store för att utöka kapaciteten hos din hemserver.



## Användbara resurser



### Officiell dokumentation




- [Umbrels officiella webbplats](https://umbrel.com)
- [Umbrel-dokumentation](https://github.com/getumbrel/umbrel/wiki)
- [App Store Umbrel] (https://apps.umbrel.com)



### Bitcoin tillämpningar




- [Bitcoin Core] (https://Bitcoin.org/fr/)
- [Electrs] (https://github.com/romanz/electrs)
- [Mempool] (https://Mempool.space)
- [Sparrow wallet] (https://sparrowwallet.com)



### Gemenskap




- [Forum Umbrel](https://community.getumbrel.com)
- [GitHub Umbrel](https://github.com/getumbrel)
- [Twitter Umbrel](https://twitter.com/umbrel)