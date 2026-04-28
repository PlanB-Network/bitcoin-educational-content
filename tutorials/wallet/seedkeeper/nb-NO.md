---
name: Seedkeeper
description: Hvordan sikkerhetskopierer jeg wallet Bitcoin med Seedkeeper-smartkortet?
---

![cover](assets/cover.webp)



Seedkeeper er et smartkort utviklet av Satochip, et belgisk selskap som spesialiserer seg på maskinvareløsninger for håndtering og beskyttelse av digitale hemmeligheter. Satochip er kjent for sitt utvalg av smartkort for Bitcoin-økosystemet, og har utviklet Seedkeeper som et alternativ til tradisjonelle metoder for lagring av mnemotekniske fraser.



Seedkeeper er et multifunksjonelt, EAL6-sertifisert smartkort med en sikker prosessor og et sabotasjesikkert minne (et såkalt "Secure Element"). Som navnet antyder, er kortets rolle å lagre Bitcoin wallet mnemonics og passord på en kryptert og beskyttet måte. Med Seedkeeper kan du generate, importere, organisere og lagre hemmelighetene dine direkte i kortets sikre komponent.



Etter min mening har Seedkeeper to hovedbruksområder, som vi vil utforske i to separate veiledninger:




- Bitcoin** lagring av minnefraser: I stedet for å skrive ned de 12 eller 24 ordene på papir, kan du importere dem til smartkortet og beskytte dem med en PIN-kode.
- Passordadministrasjon**: Du kan generate sterke passord via Seedkeeper-applikasjonen og lagre dem direkte på smartkortet, noe som gir deg en praktisk og brukervennlig passordadministrator uten nett.



Teknisk sett har Seedkeeper en kapasitet på 8192 byte, noe som gjør det mulig å lagre minst 50 separate hemmeligheter (det nøyaktige antallet avhenger av størrelsen på hemmelighetene og metadataene som er knyttet til hver av dem). Seedkeeper er tilgjengelig enten [via en smartkortleser som er koblet til](https://satochip.io/accessories/) til en datamaskin, eller via mobilapplikasjonen med NFC-tilkobling. Hele systemet fungerer i frakoblet modus, uten Internett-tilkobling, noe som garanterer en begrenset angrepsflate.



![Image](assets/fr/001.webp)



En spesielt interessant funksjon er muligheten til å duplisere innholdet i en Seedkeeper til en annen for å lage en sikkerhetskopi. I denne veiledningen viser vi deg hvordan du gjør nettopp det.



Seedkeeper er også svært interessant når den kombineres med wallet statsløs maskinvare som SeedSigner eller Spectre DIY. I dette tilfellet er det ikke nødvendig å bruke Satochips klient på datamaskinen eller mobiltelefonen. Seedkeeper beholder seed i sin secure element og kan brukes direkte med signeringsenheten, noe som eliminerer behovet for en QR-kode på papir. Jeg vil ikke gå nærmere inn på dette bruksområdet i denne veiledningen, da det er gjenstand for en annen dedikert veiledning:



https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

## 1. Hvilket bruksområde for Seedkeeper?



I denne veiledningen vil jeg bare ta for meg brukstilfeller knyttet til Bitcoin, siden det er det denne veiledningen handler om. Vi kommer ikke til å gå inn på passordadministrasjonsfunksjonaliteten, som vil bli gjenstand for en annen veiledning.



Sammenlignet med en enkel papirbackup av minnefrasen har en Seedkeeper flere fordeler:





- Tyverisikret:** seed i wallet er ikke tilgjengelig i klartekst. For å hente den ut, må du kjenne Seedkeeper PIN-koden. En tyv som får tak i enheten, vil ikke kunne gjøre noe med den uten denne koden.





- Spredning av risikoen over to faktorer:** Du kan dele sikkerheten mellom en digital og en fysisk faktor. Hvis du for eksempel lagrer Seedkeeper-PIN-koden i passordadministratoren din, trenger du både tilgang til denne administratoren og fysisk besittelse av smartkortet for å få tak i seed (en betydelig redusert angrepssannsynlighet).





- Sentralisert administrasjon:** Seedkeeper gjør det enklere å administrere flere frø fra ulike porteføljer.





- Enkel sikkerhetskopiering:** Dupliser enkelt krypterte sikkerhetskopier til andre SeedKeepers.



Det er imidlertid en rekke ulemper sammenlignet med en enkel papirbackup av seed:





- Selv om prisen er beskjeden (ca. 25 euro), er den likevel høyere enn for et papirark.





- Avhengighet av en generell databehandlingsenhet:** For å legge inn og administrere seed kreves det en datamaskin eller smarttelefon, noe som betyr at mnemonikken din passerer gjennom en maskin med en mye større angrepsflate enn wallet-maskinvaren. Dette kan utgjøre en risiko hvis maskinen blir kompromittert. Derfor anbefaler jeg ikke å bruke Seedkeeper til å lagre seed for en wallet-maskinvare (bortsett fra i tilstandsløs bruk uten datamaskin, som med SeedSigner). wallet-maskinvarens rolle er nettopp å lagre seed i et minimalistisk, svært sikkert miljø. Ved å legge inn seed manuelt på din vanlige datamaskin, er den ikke lenger begrenset til wallet-maskinvaren: Den havner også på en generell maskin, som er eksponert for flere angrepsvektorer. Så det er bedre å bruke Seedkeeper for en varm wallet enn en kald wallet (unntatt SeedSigner / statsløs wallet-maskinvare).





- Tapsrisikoen knyttet til PIN-koden:** Den direkte utilgjengeligheten til seed, i motsetning til en papirbackup, gir faktisk beskyttelse mot fysisk tyveri. Men som alltid er sikkerhet en balansegang mellom risikoen for tyveri og risikoen for tap. Hvis sikkerhetskopien din krever en PIN-kode, vil tap av denne koden gjøre det umulig å gjenopprette minnefrasen din, og dermed få tilgang til bitcoinsene dine.



Med tanke på disse fordelene og ulempene mener jeg at de beste bruksområdene for Seedkeeper (bortsett fra passordadministratorfunksjonen) er, på den ene siden, å lagre frø fra **programvareporteføljene**, siden de allerede ligger på telefonen eller datamaskinen din, eller fra skjermløs wallet-maskinvare som Satochip, og på den andre siden, å bruke den i kombinasjon med statsløs wallet-maskinvare som SeedSigner, der den virkelig kommer til sin rett.



Et annet spesielt interessant bruksområde for Seedkeeper er muligheten til å sikkerhetskopiere porteføljenes *Descriptors* på en sikker og pålitelig måte.



## 2. Hvordan får jeg en Seedkeeper?



Det er to hovedmåter å få tak i Seedkeeper på. Du kan [kjøpe den direkte fra Satochips offisielle butikk](https://satochip.io/product/seedkeeper/) eller fra en autorisert forhandler. Men siden [Seedkeeper-appleten er åpen kildekode](https://github.com/Toporin/Seedkeeper-Applet), har du også muligheten til å installere den selv på [et tomt smartkort](https://satochip.io/product/blank-javacard-for-diy-project/).



Hvis du ønsker å bruke Seedkeepers backup-funksjonalitet, må du selvsagt kjøpe to smartkort.



## 3. Installere Seedkeeper-klienten



I denne veiledningen tar vi sikkerhetskopi av seed-porteføljen vår på Seedkeeper. Det første trinnet er å installere programvaren på datamaskinen eller smarttelefonen din. På en PC må du [laste ned den nyeste versjonen av Satochip-Utils](https://github.com/Toporin/Satochip-Utils/releases). På mobil er Seedkeeper-applikasjonen tilgjengelig på [Google Play Store](https://play.google.com/store/apps/details?id=org.satochip.seedkeeper) og på [Apple App Store](https://apps.apple.com/be/app/seedkeeper/id6502836060).



![Image](assets/fr/002.webp)



## 4. Initialisering av seedkeeper



Start programmet og klikk på "*Click & Scan*"-knappen.



![Image](assets/fr/003.webp)



Du vil bli bedt om å oppgi en PIN-kode for din Seedkeeper. Siden dette er et nytt kort, er det ikke definert noen PIN-kode ennå. Skriv inn en hvilken som helst kode for å hoppe over dette trinnet, og klikk deretter på "*Neste*".



![Image](assets/fr/004.webp)



Plasser deretter kortet på baksiden av smarttelefonen. Programmet registrerer at Seedkeeper ennå ikke er initialisert, og ber deg om å angi PIN-koden til smartkortet, som kan være mellom 4 og 16 tegn lang. For optimal sikkerhet bør du velge et sterkt passord som er så langt som mulig, tilfeldig og sammensatt av mange forskjellige tegn. PIN-koden er den eneste barrieren mot fysisk tilgang til gjenopprettingsfrasen din.



**Husk også å lagre denne PIN-koden nå**, for eksempel i en passordbehandler eller på et separat fysisk medium. I sistnevnte tilfelle må du aldri oppbevare mediet som inneholder PIN-koden på samme sted som Seedkeeper, ellers vil denne sikkerheten bli ubrukelig. Det er viktig å ha en pålitelig sikkerhetskopi: Uten PIN-koden vil du ikke kunne gjenopprette hemmelighetene som er lagret på din Seedkeeper.



![Image](assets/fr/005.webp)



Bekreft PIN-koden en gang til.



![Image](assets/fr/006.webp)



Seedkeeperen din er nå initialisert. Du kan låse den opp ved å taste inn PIN-koden du nettopp har angitt.



![Image](assets/fr/007.webp)



Du kommer nå til siden for administrasjon av smartkort.



![Image](assets/fr/008.webp)



## 5. Registrer en seed på Seedkeeper



Når Seedkeeper er låst opp, klikker du på "*+*"-knappen.



![Image](assets/fr/009.webp)



Velg "Importer hemmelighet*". Med alternativet "*Generere hemmelighet*" kan du opprette en ny mnemoteknisk frase direkte i programmet.



![Image](assets/fr/010.webp)



I vårt tilfelle ønsker vi å lagre seed i porteføljen vår. Klikk på "*Mnemonic*".



![Image](assets/fr/011.webp)



Tildel denne hemmeligheten en "*Label*", slik at den lett kan identifiseres hvis du lagrer flere opplysninger i Seedkeeper.



![Image](assets/fr/012.webp)



Skriv deretter inn gjenopprettingsfrasen din i feltet. Hvis du ønsker det, kan du også legge til en passphrase BIP39 eller dine *Descriptors*. Klikk deretter på "Importer*".



![Image](assets/fr/013.webp)



*Mnemonikken som vises i dette bildet er fiktiv og tilhører ikke noen. Det er kun et eksempel. Avslør aldri din egen huskeregel for noen, ellers vil bitcoinsene dine bli stjålet



Plasser Seedkeeper på baksiden av smarttelefonen.



![Image](assets/fr/014.webp)



Din seed har blitt registrert.



![Image](assets/fr/015.webp)



## 6. Få tilgang til din seed på Seedkeeper



Hvis du vil sjekke minnefrasen din, tar du opp Seedkeeper og klikker på "*Click & Scan*"-knappen.



![Image](assets/fr/016.webp)



Skriv inn PIN-koden din, og trykk deretter på "*Neste*".



![Image](assets/fr/017.webp)



Plasser Seedkeeper på baksiden av smarttelefonen.



![Image](assets/fr/018.webp)



Dette tar deg til en liste over alle dine registrerte hemmeligheter. I dette eksempelet ønsker jeg å vise seed for porteføljen "*Blockstream App*", så jeg klikker på den.



![Image](assets/fr/019.webp)



Trykk på knappen "*Reveal*".



![Image](assets/fr/020.webp)



Skann Seedkeeperen din igjen.



![Image](assets/fr/021.webp)



Den tidligere innspilte minnefrasen vises nå på skjermen.



![Image](assets/fr/022.webp)



## 7. Sikkerhetskopiering av Seedkeeper



Vi skal nå ta en sikkerhetskopi av Seedkeeperen min på en annen Seedkeeper, slik at vi har to kopier. Denne redundansen kan være en del av en strategi for å sikre bitcoinsene dine: for eksempel ved å lagre frasen på to separate steder for å begrense fysiske risikoer, eller ved å overlate en kopi til en betrodd slektning som en del av en arveplan.



Dette gjør du ved å ta med deg den andre Seedkeeperen (husk å merke den ene av de to med et merke for å unngå forveksling). Start med å initialisere den, som beskrevet i trinn 4 i denne veiledningen. Velg et sterkt passord nok en gang. Avhengig av hvilken strategi du har, kan du velge et annet passord eller beholde det samme.



![Image](assets/fr/023.webp)



Åpne programmet, klikk på "*Click & Scan*", skriv inn passordet til din Seedkeeper n°1 (kilde), og skann den deretter.



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



Det er alt som skal til! Nå vet du hvordan du bruker Seedkeeper til å lagre den mnemoniske frasen til en Bitcoin wallet. I en fremtidig veiledning vil vi se på hvordan du kan bruke Seedkeeper til å lagre passordene dine. Jeg inviterer deg også til å oppdage den kombinerte bruken med SeedSigner :



https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

https://planb.academy/tutorials/computer-security/authentication/seedkeeper-password-64ffaf68-53aa-43c3-bc7a-c1dc2a17fee3

I denne veiledningen har vi nevnt ***Descriptors*** i Bitcoin-porteføljen din flere ganger. Vet du ikke hva de er? I så fall anbefaler jeg at du tar vårt gratis CYP 201-kurs, som går i dybden på alle mekanismene som er involvert i driften av HD-porteføljer!



https://planb.academy/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f