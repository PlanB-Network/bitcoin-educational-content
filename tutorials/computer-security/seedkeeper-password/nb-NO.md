---
name: Seedkeeper - Passordbehandler
description: Hvordan lagrer du passordene dine med Seedkeeper-smartkortet?
---

![cover](assets/cover.webp)



Seedkeeper er et smartkort utviklet av Satochip, et belgisk selskap som spesialiserer seg på maskinvareløsninger for håndtering og beskyttelse av digitale hemmeligheter. Satochip er kjent for sitt utvalg av smartkort for Bitcoin-økosystemet, og Seedkeeper er et alternativ til tradisjonelle metoder for lagring av mnemotekniske fraser og andre digitale hemmeligheter.



Seedkeeper har form av et multifunksjonelt, EAL6-sertifisert smartkort med en sikker prosessor og et sabotasjesikkert minne (et såkalt "Secure Element"). Som navnet antyder, er dets rolle å lagre Bitcoin-porteføljens mnemoteknikk og passord på en kryptert og beskyttet måte. Med Seedkeeper kan du generate, importere, organisere og lagre hemmelighetene dine direkte i kortets sikre komponent.



Etter min mening har Seedkeeper to hovedbruksområder, som vi vil utforske i to separate veiledninger:




- Bitcoin** lagring av minnefraser: I stedet for å skrive ned de 12 eller 24 ordene på papir, kan du importere dem til smartkortet og beskytte dem med en PIN-kode.
- Passordadministrasjon**: Du kan generate sterke passord via Seedkeeper-applikasjonen og lagre dem direkte på smartkortet, noe som gir deg en praktisk og brukervennlig passordadministrator uten nett.



Teknisk sett har Seedkeeper en kapasitet på 8192 byte, noe som gjør det mulig å lagre minst 50 separate hemmeligheter (det nøyaktige antallet avhenger av størrelsen på hemmelighetene og metadataene som er knyttet til hver av dem). Seedkeeper er tilgjengelig enten [via en smartkortleser som er koblet til] (https://satochip.io/accessories/) til en datamaskin, eller via mobilapplikasjonen med NFC-tilkobling. Hele systemet fungerer i frakoblet modus, uten Internett-tilkobling, noe som garanterer en begrenset angrepsflate.



![Image](assets/fr/001.webp)



En spesielt interessant funksjon er muligheten til å duplisere innholdet i en Seedkeeper til en annen for å lage en sikkerhetskopi. I denne veiledningen viser vi deg hvordan du gjør nettopp det.



I denne veiledningen tar vi kun for oss bruken av SeedKeeper for tradisjonelle passord, på samme måte som en passordbehandler. Hvis du ønsker å bruke SeedKeeper til å lagre Bitcoin wallet mnemoniske fraser, kan du se denne andre veiledningen:



https://planb.academy/tutorials/wallet/backup/seedkeeper-906dfff8-1826-4837-92d1-8669e216d356

## 1. Hvordan får jeg en Seedkeeper?



Det er to hovedmåter å få tak i Seedkeeper på. Du kan [kjøpe den direkte fra Satochips offisielle butikk](https://satochip.io/product/seedkeeper/) eller fra en autorisert forhandler. Men siden [Seedkeeper-appleten er åpen kildekode](https://github.com/Toporin/Seedkeeper-Applet), har du også muligheten til å installere den selv på [et tomt smartkort](https://satochip.io/product/blank-javacard-for-diy-project/).



Hvis du ønsker å bruke Seedkeepers backup-funksjonalitet, må du selvsagt kjøpe to smartkort.



## 2. Installere Seedkeeper-klienten



Det første trinnet er å installere programvaren på datamaskinen eller smarttelefonen. På PC må du [laste ned den nyeste versjonen av Satochip-Utils](https://github.com/Toporin/Satochip-Utils/releases). På mobiler er Seedkeeper-applikasjonen tilgjengelig på [Google Play Store](https://play.google.com/store/apps/details?id=org.satochip.seedkeeper) og på [Apple App Store](https://apps.apple.com/be/app/seedkeeper/id6502836060).



![Image](assets/fr/002.webp)



## 3. Initialisering av seedkeeper



Start programmet og klikk på "*Click & Scan*"-knappen.



![Image](assets/fr/003.webp)



Du vil bli bedt om å oppgi en PIN-kode for din Seedkeeper. Siden dette er et nytt kort, er det ikke definert noen PIN-kode ennå. Skriv inn en hvilken som helst kode for å hoppe over dette trinnet, og klikk deretter på "*Neste*".



![Image](assets/fr/004.webp)



Plasser deretter kortet på baksiden av smarttelefonen. Programmet registrerer at Seedkeeper ennå ikke er initialisert, og ber deg om å angi smartkortets PIN-kode på mellom 4 og 16 tegn. For optimal sikkerhet bør du velge en robust PIN-kode som er så lang som mulig, tilfeldig og som består av mange forskjellige tegn. PIN-koden er den eneste barrieren mot fysisk tilgang til passordene dine.



**Husk også å lagre denne PIN-koden nå**, for eksempel i en passordbehandler eller på et separat fysisk medium. I sistnevnte tilfelle må du aldri oppbevare mediet som inneholder PIN-koden på samme sted som Seedkeeper, ellers vil denne sikkerheten bli ubrukelig. Det er viktig å ha en pålitelig sikkerhetskopi: Uten PIN-koden vil du ikke kunne gjenopprette hemmelighetene som er lagret på din Seedkeeper.



![Image](assets/fr/005.webp)



Bekreft PIN-koden en gang til.



![Image](assets/fr/006.webp)



Seedkeeperen din er nå initialisert. Du kan låse den opp ved å taste inn PIN-koden du nettopp har angitt.



![Image](assets/fr/007.webp)



Du kommer nå til siden for administrasjon av smartkort.



![Image](assets/fr/008.webp)



## 4. Lagre passord på Seedkeeper



Når Seedkeeper er låst opp, klikker du på "*+*"-knappen.



![Image](assets/fr/009.webp)



Velg "Generer hemmelighet*". Med alternativet "*Importer en hemmelighet*" kan du lagre en eksisterende hemmelighet (for eksempel et passord du har opprettet tidligere).



![Image](assets/fr/010.webp)



I vårt tilfelle ønsker vi å lagre et passord. Klikk på "*Passord*".



![Image](assets/fr/011.webp)



Tildel en "*Label*" til denne hemmeligheten, slik at den lett kan identifiseres hvis du lagrer flere opplysninger i Seedkeeper. Du kan også legge til en identifikator knyttet til passordet og nettadressen til nettstedet.



![Image](assets/fr/012.webp)



Velg lengde og parametere for passordet ditt, og klikk deretter på "*Generate*" og "*Import*".



![Image](assets/fr/013.webp)



Plasser Seedkeeper på baksiden av smarttelefonen.



![Image](assets/fr/014.webp)



Passordet ditt er registrert.



![Image](assets/fr/015.webp)



## 5. Få tilgang til passordet ditt for Seedkeeper



Hvis du vil sjekke passordet ditt, tar du Seedkeeper og klikker på "*Click & Scan*"-knappen.



![Image](assets/fr/016.webp)



Skriv inn PIN-koden din, og trykk deretter på "*Neste*".



![Image](assets/fr/017.webp)



Plasser Seedkeeper på baksiden av smarttelefonen.



![Image](assets/fr/018.webp)



Da kommer du til en liste over alle dine registrerte hemmeligheter. I dette eksempelet ønsker jeg å vise passordet for Plan ₿ Academy-kontoen min, så jeg klikker på det.



![Image](assets/fr/019.webp)



Trykk på knappen "*Reveal*".



![Image](assets/fr/020.webp)



Skann Seedkeeperen din igjen.



![Image](assets/fr/021.webp)



Det tidligere lagrede passordet ditt vises nå på skjermen. Du kan kopiere det og bruke det på det aktuelle nettstedet.



![Image](assets/fr/022.webp)



## 6. Sikkerhetskopiering av Seedkeeper



Vi skal nå ta en sikkerhetskopi av min Seedkeeper på en annen Seedkeeper, slik at vi har to kopier. Denne redundansen kan være en del av en strategi for å sikre de viktigste passordene dine, for eksempel ved å lagre Seedkeeperne dine på to forskjellige steder for å begrense den fysiske risikoen, eller ved å overlate en kopi til en betrodd slektning.



Dette gjør du ved å ta med deg den andre Seedkeeperen (husk å merke den ene av de to med et merke for å unngå forveksling). Start med å initialisere den, som beskrevet i trinn 3 i denne veiledningen. Igjen, velg en sterk PIN-kode. Avhengig av hvilken strategi du har, kan du velge en annen PIN-kode eller beholde den samme.



![Image](assets/fr/023.webp)



Åpne applikasjonen, klikk på "*Click & Scan*", skriv inn PIN-koden til din Seedkeeper n°1 (kilde), og skann den deretter.



![Image](assets/fr/024.webp)



Dette fører deg til startsiden, med en liste over hemmelighetene dine. Klikk på de tre små prikkene øverst til høyre i grensesnittet.



![Image](assets/fr/025.webp)



Velg "*Lag en sikkerhetskopi*", og trykk deretter på "*Start*".



![Image](assets/fr/026.webp)



Tast inn PIN-koden til backupkortet (Seedkeeper nr. 2).



![Image](assets/fr/027.webp)



Skann deretter kortet.



![Image](assets/fr/028.webp)



Gjør det samme med hovedkortet (Seedkeeper nr. 1), og klikk deretter på "*Make a backup*".



![Image](assets/fr/029.webp)



Din Seedkeeper nr. 2 inneholder nå alle hemmelighetene som er lagret på Seedkeeper nr. 1.



![Image](assets/fr/030.webp)



Du kan skanne Seedkeeper n°2 for å kontrollere at hemmelighetene er kopiert.



![Image](assets/fr/031.webp)



Det er alt som trengs! Nå vet du hvordan du bruker Seedkeeper til å lagre passordene dine. I en fremtidig veiledning vil vi se på hvordan du bruker Seedkeeper til å sikkerhetskopiere en Bitcoin wallet. Jeg inviterer deg også til å oppdage den kombinerte bruken med SeedSigner :



https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

https://planb.academy/tutorials/wallet/backup/seedkeeper-906dfff8-1826-4837-92d1-8669e216d356