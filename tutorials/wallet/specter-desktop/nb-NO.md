---
name: Specter Desktop
description: Administrer Bitcoin-porteføljene dine med flere signaturer helt suverent med din egen node
---

![cover](assets/cover.webp)



Specter Desktop er en åpen kildekode-applikasjon (MIT-lisens) utviklet av Cryptoadvance siden 2019 som forenkler administrasjonen av Bitcoin-lommebøker med maskinvarelommebøker (Ledger, Trezor, Coldcard, BitBox02, Passport osv.) og din egen Bitcoin-infrastruktur (Bitcoin core-node eller Electrum Server). Programmet utmerker seg spesielt i konfigurasjoner med flere signaturer, slik at du kan sikre store summer ved å fordele signeringskraften mellom flere uavhengige maskinvarelommebøker.



**I denne opplæringen lærer du hvordan du:**




- Installer og konfigurer Spectre Desktop på datamaskinen din (Windows, macOS eller Linux)
- Koble Specter til en Electrum Server (vi bruker Umbrel i dette eksempelet)
- Opprette en enkel Wallet med en Hardware Wallet (Coldcard)
- Motta og send bitcoins med full suverenitet
- Sette opp en 2-på-3 multisignatur Wallet med flere maskinvarelommebøker
- Installere Spectre på en Umbrel-server (avansert bonus)



Alle transaksjonene dine valideres lokalt via din egen infrastruktur, uten å overføre informasjon til eksterne servere, noe som garanterer konfidensialitet og økonomisk suverenitet. Sjekk alltid transaksjonene på Hardware Wallet-skjermen før du signerer.



## Nedlasting og installasjon



Besøk den offisielle nettsiden til Specter Desktop for å laste ned applikasjonen.



![Page d'accueil Specter](assets/fr/01.webp)



På nedlastingssiden velger du den versjonen som passer til operativsystemet ditt: macOS, Windows eller Linux.



![Téléchargement selon l'OS](assets/fr/02.webp)



Når du har lastet ned programmet, installerer du det i henhold til operativsystemets vanlige instruksjoner. For macOS drar du ikonet til Programmer. For Windows kjører du installasjonsprogrammet. For Linux følger du instruksjonene i pakken.



## Opprinnelig konfigurasjon



Ved første oppstart ber Spectre Desktop deg om å velge tilkoblingstype. Du kan koble deg til en Electrum Server eller til din egen Bitcoin core-node.



![Choix du type de connexion](assets/fr/03.webp)



I dette eksempelet bruker vi en tilkobling til en Electrum Server som kjører på Umbrel.



For mer informasjon, se vår Umbrel-veiledning:



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

Dette alternativet gir raskere synkronisering enn Bitcoin core. Hvis du foretrekker det, kan du velge "Bitcoin core" og konfigurere tilkoblingen til din lokale node. De følgende trinnene er de samme uansett hva du velger.



Velg "Electrum Connection" og velg deretter "Enter my own" for å konfigurere din egen Electrum Server.



![Configuration Electrum](assets/fr/04.webp)



Skriv inn Address for din Electrum Server. I vårt tilfelle med Umbrel vil Address være `umbrel.local` med port `50001`. Klikk på "Connect" for å opprette forbindelsen.



Når du er tilkoblet, vises velkomstskjermen med en sjekkliste for å komme i gang. Du må nå legge til maskinvarelommebøkene dine.



![Écran d'accueil](assets/fr/05.webp)



## Legge til en Hardware Wallet



I menyen til venstre klikker du på "Legg til enhet" for å legge til din Hardware Wallet.



Specter Desktop støtter en rekke maskinvarelommebøker: Trezor, Ledger, BitBox02, Coldcard, KeepKey, Keystone, Cobo Vault og mange andre.



Hvis du vil lære mer, kan du ta en titt på Hardware Wallet-veiledningene våre.



![Sélection du type de hardware wallet](assets/fr/06.webp)



Velg din Hardware Wallet. I dette eksempelet bruker vi et Coldcard MK4.



Nedenfor finner du veiledningen vår for denne Hardware Wallet :



https://planb.network/tutorials/wallet/hardware/coldcard-5d44dd94-423d-4e37-9a8c-3fc38b45ce59

For et Coldcard må du eksportere de offentlige nøklene fra Hardware Wallet enten via en USB-tilkobling eller et microSD-kort.



![Import des clés du Coldcard](assets/fr/07.webp)



Følg instruksjonene som vises for å eksportere nøklene fra Coldcard. Gi Hardware Wallet et navn (her "MK4 Tuto"). Når nøklene er importert, kan du opprette en Wallet med én enkelt nøkkel, eller legge til andre maskinvarelommebøker for en Wallet med flere signaturer.



![Dispositif ajouté](assets/fr/08.webp)



## Opprettelse av portefølje



Når du har lagt til Hardware Wallet, klikker du på "Opprett enkeltnøkkel Wallet" for å opprette en Wallet med enkeltsignatur.



Gi porteføljen et navn (f.eks. "Wallet for tuto"), og velg Address-typen. Velg "SegWit" for å bruke opprinnelige BECH32-adresser, som optimaliserer transaksjonskostnadene.



![Configuration du portefeuille](assets/fr/09.webp)



Når porteføljen din er opprettet, tilbyr Specter å lagre en sikkerhetskopi i PDF-format som inneholder all offentlig informasjon som trengs for å gjenopprette porteføljen din (deskriptorer, utvidede offentlige nøkler). Denne filen inneholder ikke de private nøklene dine.



![Sauvegarde du portefeuille](assets/fr/10.webp)



## Motta bitcoins



For å motta bitcoins velger du din Wallet i menyen til venstre, og klikker deretter på "Motta"-fanen.



Specter genererer automatisk et nytt mottak Address med en QR-kode.



![Génération d'une adresse de réception](assets/fr/11.webp)



Du kan kopiere Address eller skanne QR-koden. Sjekk alltid Address på Hardware Wallet-skjermen før du gir den videre til noen.



## Se historikk og adresser



Når du har mottatt bitcoins, kan du se transaksjonene dine i "Transaksjoner"-fanen.



![Historique des transactions](assets/fr/12.webp)



Under fanen "Adresser" kan du se alle adressene som er generert av porteføljen din, med bruksstatus og tilhørende beløp.



![Liste des adresses](assets/fr/13.webp)



## Send bitcoins



For å sende bitcoins klikker du på "Send"-fanen. Skriv inn mottakerens Address, beløpet som skal sendes, og sjekk de avanserte alternativene hvis du ønsker å velge UTXO-er manuelt (Coin-kontroll).



![Création d'une transaction](assets/fr/14.webp)



Klikk på "Create Unsigned Transaction" for å opprette transaksjonen. Specter vil deretter be deg om å signere transaksjonen med din Hardware Wallet.



![Signature de la transaction](assets/fr/15.webp)



Hvis du bruker et Coldcard, kan du velge om du vil signere via USB eller ved hjelp av microSD-kortet (air-gapped). Bekreft transaksjonen på Hardware Wallet-skjermen, og kontroller nøye destinasjonen Address og beløpet.



Når transaksjonen er signert, kan du kringkaste den i Bitcoin-nettverket.



![Options de diffusion](assets/fr/16.webp)



Klikk på "Send transaksjon" for å sende transaksjonen. Specter bekrefter at transaksjonen er sendt, og du kan følge med på statusen under fanen Transaksjoner.



![Diffusion de la transaction](assets/fr/17.webp)



## Opprette og bruke en portefølje med flere signaturer



En av de største fordelene med Specter Desktop er muligheten til å forenkle håndteringen av porteføljer med flere signaturer. En Multisig Wallet krever flere signaturer for å autorisere en transaksjon, noe som eliminerer det eneste feilpunktet. En 2-på-3-konfigurasjon krever for eksempel to signaturer fra tre separate maskinvarelommebøker for å validere en utgift.



For å opprette en Multisig Wallet, begynner du med å legge til alle signerende maskinvarelommebøker via "Legg til enhet". I dette eksempelet bruker vi tre forskjellige maskinvare-lommebøker: et Coldcard MK4 (allerede lagt til tidligere), et Passport og en Ledger. Denne diversifiseringen av produsenter styrker sikkerheten ved å unngå avhengighet av en enkelt Supply-kjede eller fastvare.



Her er lenkene til veiledningene for Ledger og Passport:



https://planb.network/tutorials/wallet/hardware/ledger-nano-s-plus-75043cb3-2e8e-43e8-862d-ca243b8215a4

https://planb.network/tutorials/wallet/hardware/passport-74e53858-3fa2-43f9-b866-573297546236

Legg til Passport ved å gi Hardware Wallet et navn (f.eks. "Passport multi") og importere nøklene via microSD-kort eller QR-kode. Klikk deretter på "Fortsett" for å fortsette.



![Ajout du Passport](assets/fr/23.webp)



Legg deretter til Ledger ved å koble den til via USB og åpne Bitcoin-programmet på Hardware Wallet. Gi den et navn (f.eks. "Ledger multi") og klikk på "Hent via USB" og deretter "Fortsett" for å importere de offentlige nøklene.



![Ajout du Ledger](assets/fr/24.webp)



Når du har registrert de tre maskinvarelommebøkene dine i Specter, klikker du på "Legg til Wallet" og velger alternativet "Flere signaturer" for å opprette en Wallet med flere signaturer.



![Choix du type de wallet](assets/fr/25.webp)



Velg de tre maskinvarelommebøkene du ønsker å inkludere i multisignaturkvorumet: MK4 Tuto, Passport multi og Ledger multi. Klikk på "Fortsett" for å gå videre til neste trinn.



![Sélection des hardware wallets pour le multisig](assets/fr/26.webp)



Velg konfigurasjon for multisignatur. Velg "SegWit" som Address-type for å dra nytte av optimaliserte gebyrer. Med parameteren "Nødvendige signaturer for å autorisere transaksjoner (m av 3)" kan du definere terskelen: for en 2-på-3-konfigurasjon kreves det 2 signaturer. Hver Hardware Wallet viser den tilsvarende Multisig-nøkkelen. Klikk på "Opprett Wallet" for å fullføre opprettelsen.



![Configuration 2-sur-3 Segwit](assets/fr/27.webp)



Din "Multi tuto"-mappe med flere signaturer er nå opprettet. Specter anbefaler at du umiddelbart lagrer sikkerhetskopien av PDF-filen som inneholder porteføljen Descriptor. Klikk på "Lagre sikkerhetskopi-PDF" for å laste ned denne viktige filen.



![Wallet multisig créé](assets/fr/28.webp)



Med Specter kan du også eksportere Wallet-informasjon til hver av maskinvarelommebøkene dine via QR-kode eller fil. Dette gjør det mulig for visse maskinvarelommebøker (for eksempel Coldcard eller Passport) å lagre Multisig-konfigurasjonen direkte i minnet.



For Passport låser du opp enheten og går til "Administrer konto" > "Koble til Wallet" > "Specter" > "Multisig" > "QR-kode", og skanner deretter QR-koden som genereres av Specter. Passport vil deretter be deg om å skanne en mottakende Address fra din Wallet for å validere Multisig-konfigurasjonen.



For MK4 kobler du den til PC-en og låser den opp. Klikk deretter på "Save MK4 Tuto file" og lagre filen på MK4. Neste gang du signerer Hardware Wallet, vil MK4 bruke denne filen til å fullføre konfigurasjonen av Multisig.



![Export vers les hardware wallets](assets/fr/29.webp)



Du kan når som helst få tilgang til sikkerhetskopier fra fanen "Innstillinger" i porteføljen din, og deretter "Eksporter":



![Accès au backup PDF](assets/fr/30.webp)



Den daglige bruken forblir lik en enkel Wallet: du generate mottar adresser som normalt. For å sende bitcoins, gå til "Send"-fanen, skriv inn mottakerens Address og beløpet, og klikk deretter på "Create Unsigned Transaction".



![Création d'une transaction multisig](assets/fr/31.webp)



Specter bygger en PSBT (Partially Signed Bitcoin Transaction) og viser "Acquired 0 of 2 signatures". Du må nå signere med minst to av de tre maskinvarelommebøkene dine. Klikk på den første Hardware Wallet (f.eks. "MK4 Tuto") for å signere med Coldcard, og deretter på den andre (f.eks. "Passport multi") for å få den andre signaturen som kreves.



![Signature de la transaction](assets/fr/32.webp)



Når du har innhentet de to nødvendige signaturene (Interface viser "Acquired 2 of 2 signatures" og "Transaction is ready to send"), klikker du på "Send Transaction" for å kringkaste transaksjonen på Bitcoin-nettverket.



![Transaction prête à être diffusée](assets/fr/33.webp)



Denne multisignaturtilnærmingen egner seg spesielt godt for bedrifter (flere ledere må godkjenne utgiftene), familier (beskyttelse av arv i flere generasjoner) eller enkeltpersoner som forvalter store summer (geografisk fordeling av maskinvarelommebøker for å motstå lokale katastrofer).



### Sikkerhetskopiering med flere signaturer er avgjørende



**Merk**: Sikkerhetskopiering av en portefølje med flere signaturer er fundamentalt forskjellig fra sikkerhetskopiering av en enkelt portefølje. Gjenopprettingsfraser (seed-fraser) alene er ikke tilstrekkelig for å gjenopprette en Multisig-portefølje. Du må også sikkerhetskopiere **output descriptor** (output descriptor), som inneholder konfigurasjonsinformasjonen for multisignaturporteføljen din.



output descriptor inneholder viktige data: de utvidede offentlige nøklene (xpubs) til hver medunderskriver, signaturterskelen (2-på-3 i vårt eksempel), typen skript som brukes (SegWit native, nested eller legacy), og avledningsbanene for hver Hardware Wallet. Uten denne Descriptor vil du ikke kunne gjenoppbygge Wallet eller få tilgang til bitcoinsene dine, selv om du har to av dine tre gjenopprettingsfraser. Descriptor lar programvaren din vite hvordan du skal kombinere de offentlige nøklene til generate Bitcoin-adressene som tilsvarer midlene dine.



Specter Desktop genererer automatisk en sikkerhetskopi av en PDF-fil når du oppretter Multisig-porteføljen. Denne PDF-filen inneholder den komplette Descriptor, fingeravtrykkene til hver Hardware Wallet og all offentlig informasjon som kreves for restaurering. **Denne filen inneholder ikke dine private nøkler** og lar deg derfor ikke i seg selv bruke bitcoinsene dine, men den lar alle som får tilgang til den, se din komplette transaksjonshistorikk og saldo.



For å sikkerhetskopiere multisignaturkonfigurasjonen din på riktig måte, følger du denne prosedyren: Når du har opprettet porteføljen, klikker du på fanen "Innstillinger", deretter "Eksporter" og velger "Lagre sikkerhetskopi-PDF". Lag flere kopier av denne PDF-filen: Skriv ut minst to eksemplarer på papir, og ta også vare på en kryptert digital kopi. Lagre én kopi av PDF-filen med hver av gjenopprettingsfrasene dine, på geografisk adskilte steder.



Brenn gjenopprettingsfraser på brannsikre og vanntette metallplater for å garantere lang levetid. Undervurder aldri viktigheten av disse sikkerhetskopiene: Hvis du mister datamaskinens `~/.specter`-mappe OG du mister en av maskinvarelommebøkene dine uten en Descriptor-sikkerhetskopi, vil alle pengene dine være ugjenkallelig tapt, selv med en 2-på-3-konfigurasjon. Multisignaturredundans beskytter mot tap av en Hardware Wallet, men bare hvis du har sikkerhetskopiert Wallets Descriptor på riktig måte.



## Fordeler og begrensninger med Spectre Desktop



**Fordeler**: Optimal konfidensialitet med fullstendig lokal validering uten tredjepartsservere. Fleksibilitet med flere signaturer for avanserte konfigurasjoner (bedrift, familie, individ). Omfattende Hardware Wallet-støtte med full interoperabilitet (USB og luftgap).



**Begrensninger**: Betydelig læringskurve for avanserte Bitcoin-konsepter (UTXO-er, deskriptorer, avledningsstier).



## Beste praksis



Kontroller alltid adresser og beløp på Hardware Wallet-skjermen før du validerer, for å beskytte deg mot skadelig programvare.



Hold PDF-sikkerhetskopier adskilt fra frøene dine. Disse offentlige deskriptorene kan lagres i et bankhvelv eller i en kryptert sky, noe som gjør det enklere å gjenopprette dem uten å eksponere de private nøklene.



Test gjenoppretting på token-beløp før du bruker porteføljene dine med store midler. Opprett, test, slett og gjenopprett for å validere prosedyrene dine.



Hold Specter og fastvaren oppdatert. Fordel medsignaturene geografisk (hjemme/på kontoret/nærområdet) for å motstå lokale katastrofer. Bruk beskrivende etiketter for å forenkle regnskap og selvangivelser.



## Bonus: Installasjon på en Bitcoin-server (Umbrel, RaspiBlitz, Start9)



Hvis du allerede eier en Bitcoin-server som Umbrel, RaspiBlitz, MyNode eller Start9, kan du installere Spectre Desktop direkte fra deres applikasjonsbutikk. Denne tilnærmingen gir flere betydelige fordeler: applikasjonen konfigurerer seg automatisk med din lokale Bitcoin core-node, den er tilgjengelig døgnet rundt via et Interface-nettverk fra hvilken som helst enhet i nettverket ditt, og du kan til og med få sikker fjerntilgang via Tor. Hele Bitcoin-infrastrukturen din er sentralisert på én dedikert server, noe som forenkler administrasjonen og styrker suvereniteten din.



### Installasjon fra Umbrel App Store



Fra Umbrel Interface går du til App Store og søker etter Specter Desktop. Klikk på "Install" for å starte installasjonen.



![App Store Umbrel - Specter Desktop](assets/fr/18.webp)



Når installasjonen er fullført, åpner du Specter Desktop på din Umbrel. Velkomstskjermen vil be deg om å velge tilkoblingstype. Hvis du bruker Specter på din Umbrel, klikker du på "Oppdater innstillinger" for å konfigurere tilkoblingen.



![Écran de bienvenue Specter sur Umbrel](assets/fr/19.webp)



Velg "Remote Specter USB-tilkobling" for å aktivere bruk av USB-maskinvare-lommebøker som er koblet til den lokale datamaskinen mens du bruker Specter på den eksterne Umbrel-serveren.



![Configuration Remote Specter USB](assets/fr/20.webp)



Følg instruksjonene som vises for å konfigurere HWI-broen. Du må få tilgang til enhetens broinnstillinger og legge til domenet `http://umbrel.local:25441` i hvitelisten. Klikk på "Oppdater" for å lagre konfigurasjonen.



![HWI Bridge Settings](assets/fr/21.webp)



Hvis du også ønsker å bruke USB-maskinvarelommebøkene fra din lokale datamaskin, laster du ned Specter Desktop-applikasjonen til maskinen din og setter den til "Yes, I run Specter remotely". Klikk på "Lagre" for å fullføre konfigurasjonen.



![Configuration connexion remote dans l'app](assets/fr/22.webp)



## Konklusjon



Specter Desktop demokratiserer avanserte Bitcoin-konfigurasjoner og gjør multisignatur tilgjengelig uten at det går på bekostning av suverenitet eller konfidensialitet. For brukere som forvalter store pengebeløp, forvandler den institusjonelle praksiser til løsninger som kan tas i bruk av privatpersoner.



Selv om applikasjonen krever en innledende investering i infrastruktur og læring, tilbyr den fullstendig suverenitet: kontroll over valideringsinfrastrukturen, fysisk Ownership av nøkler og transaksjoner uten overvåkning fra tredjeparter. Enten du er en privatperson som sikrer sparepengene dine, en familie som oppretter en bankboks for flere generasjoner, eller et selskap som håndterer kontantstrømmen, er Specter Desktop referanseverktøyet for å forene maksimal sikkerhet og absolutt suverenitet.



## Ressurser



### Offisiell dokumentasjon




- [Specter Desktop offisielle nettsted] (https://specter.solutions/desktop/)
- [GitHub-kildekode] (https://github.com/cryptoadvance/specter-desktop)
- [Fullstendig dokumentasjon] (https://docs.specter.solutions/)



### Fellesskap og støtte




- [Telegram Specter Community Group] (https://t.me/spectersupport)
- [Reddit diskusjonsforum] (https://reddit.com/r/specterdesktop/)
- [GitHub-feilrapporter] (https://github.com/cryptoadvance/specter-desktop/issues)