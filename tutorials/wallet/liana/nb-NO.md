---
name: Liana
description: Sette opp og bruke en lommebok på Liana
---
![cover](assets/cover.webp)

I denne veiledningen forklarer vi trinn for trinn hvordan du bruker Liana-programmet på en datamaskin. Du lærer blant annet hvordan du setter opp en automatisert arvefølgeplan, mottar og sender bitcoins i normale situasjoner og henter ut midler fra en eksisterende portefølje etter en gitt periode.

I januar 2025 var maskinvarelommebøkene som var kompatible med Liana: BitBox02, Blockstream Jade, Blockstream Jade Plus, COLDCARD MK4, COLDCARD Q, Ledger Nano S, Ledger Nano S Plus, Ledger Nano X, Ledger Flex, Spectre DIY.

Hvis du ønsker å gjenopprette midler fra en eksisterende Liana-lommebok, kan du lese presentasjonen nedenfor og gå direkte til delen "Gjenopprette bitcoins".

## Vi presenterer Liana-programvaren

Liana er en programvarepakke med åpen kildekode som er utviklet for å opprette og administrere avanserte porteføljer, særlig som en del av et automatisert arvesystem eller en robust sikkerhetskopimekanisme. Prosjektet har blitt utviklet siden 2022 av Wizardsardine, et selskap som ble grunnlagt av Kévin Loaec og Antoine Poinsot. På den offisielle nettsiden presenteres Liana som "en enkel portefølje for personlig kuratering, med gjenopprettings- og arvefunksjoner". Programvaren kjører på datamaskiner - Linux, MacOS, Windows - og den (åpne) kildekoden er tilgjengelig [på GitHub] (https://github.com/wizardsardine/liana).

Liana bygger på Bitcoins programmerbarhet for å skape en avansert lommebok. Liana utnytter spesielt tidslåser (*timelocks*), som gjør det mulig å bruke penger først når en gitt tidsperiode er utløpt, og som er involvert i utvinningen av Bitcoins. En Liana-lommebok består dermed av flere utgiftsveier:


- En hovedutgiftsvei, som alltid er tilgjengelig;
- Minst én gjenopprettingsbane, som blir tilgjengelig etter en viss tid.

Diagrammet nedenfor illustrerer hvordan en portefølje med to utgiftsbaner fungerer:

![Schéma explicatif](assets/fr/01.webp)

Denne operasjonen lar deg sette opp ulike konfigurasjoner, inkludert :


- En arveplan som gjør det mulig for arvingene å få tilbake midler i tilfelle brukerens død. For mer informasjon om dette emnet anbefaler vi at du leser [del 4] (https://planb.network/courses/btc102/233c88d3-2e8e-5eba-ac06-efe67a209038) i BTC102-kurset.
- En forsterket sikkerhetskopi med gjenopprettingstid, noe som gir brukeren mulighet til å bruke lommeboken uten å måtte oppbevare den tilhørende hemmelige frasen og risikere at den blir stjålet, for eksempel under et innbrudd.
- Et sikkerhetsnett for folk som begynner med Bitcoin: De vil administrere sin egen lommebok, og deres "verge" (for eksempel en slektning) vil forbeholde seg retten til å få tilbake pengene deres etter en gitt periode.
- En flerpartssignaturordning (*multisig*) med reduserte krav over tid, for å håndtere at en eller flere av deltakerne forsvinner, for eksempel et selskaps partnere.

Den store styrken til Liana er at den introduserer en standardisert måte å garantere gjenvinning av midler i tilfelle tap av hovednøkkelen, som brukes til løpende utgifter. Dette representerer en stor innovasjon for ren oppbevaring av midler, noe som er forbundet med risiko, spesielt hvis du ikke er godt informert om emnet. Liana kan derfor oppmuntre selv de mest risikovillige brukerne til å slutte å bruke en forvalter (for eksempel en vekslingsplattform) til å oppbevare midlene sine og gjenvinne eierskapet til pengene sine, i tråd med Bitcoins cypherpunk-etos.

Liana har selvfølgelig sine ulemper. Den første er at du må oppdatere lommeboken din regelmessig ved å gjøre en transaksjon på Bitcoin-blokkjeden. Dette kan være irriterende (avhengig av hvor ofte du bruker programvaren) og kostbart (avhengig av gebyrnivået på det aktuelle tidspunktet), men det er prisen du betaler for ekstra sikkerhet.

Et annet negativt punkt kan være konfidensialitet. Når du involverer en annen person i konfigurasjonen, får han eller hun tilgang til alle adressene dine og kan derfor overvåke aktiviteten din. Dette er imidlertid ikke noe problem hvis du velger en forsterket sikkerhetskopi eller en arveplan der arvingen din ikke har umiddelbar kjennskap til porteføljens detaljer.

## Forberedelse

I denne veiledningen skal vi sette opp en etterfølgerplan. Vi kommer til å bruke :


- En Ledger Nano S Plus, til hverdagslige utgifter;

https://planb.network/tutorials/wallet/hardware/ledger-nano-s-plus-75043cb3-2e8e-43e8-862d-ca243b8215a4

- En Blockstream Jade, som brukes til å inndrive midler;

https://planb.network/tutorials/wallet/hardware/jade-7d62bf0c-f460-4e68-9635-af9b731dabc3

- To lagringsmedier (USB-minnepinner) for å lagre porteføljebeskrivelsen;
- Et arvebrev med instruksjoner om hvordan midlene skal inndrives;
- En nummerert og forseglet pose for å sikre at gjenvinningsutstyret (Jade) ikke har blitt brukt.

## Installasjon og konfigurasjon

Besøk det offisielle Wizardsardine-nettstedet og last ned Liana på https://wizardsardine.com/liana/. Du kan også laste ned den nyeste versjonen [fra GitHub-depotet] (https://github.com/wizardsardine/liana/releases), der du kan sjekke ektheten til programvaren. Versjonen som brukes i denne veiledningen er 0.9.

![Télécharger Liana](assets/fr/02.webp)

For å finne ut hvordan du manuelt verifiserer ektheten og integriteten til programvaren før installasjon, anbefaler vi at du konsulterer denne veiledningen :

https://planb.network/tutorials/others/general/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc
Installer programvaren på maskinen din og start den. Velg alternativet "*Opprett en ny Liana-lommebok*" for å konfigurere lommeboken din.

![Accueil Liana](assets/fr/03.webp)

Velg din porteføljetype. Hvis du vil sette opp en forbedret sikkerhetskopi med gjenopprettingstid, kan du velge alternativet "*Bygg din egen*" og velge standardskjemaet. Dette vil fungere på omtrent samme måte, bortsett fra at du ikke trenger å beholde gjenopprettingsfrasen for maskinvarelommeboken.

Vi ser her bort fra *Expanding multisig*, som setter opp en mer kompleks konfigurasjon.

I denne veiledningen bruker vi enkel arv.

![Choisir type de portefeuille](assets/fr/04.webp)

Her følger en kort forklaring.

![Rapide explication](assets/fr/05.webp)

Når du har lest forklaringen, kan du sette opp nøklene til Liana-lommeboken din. Dette er et avgjørende trinn, ettersom det bestemmer kontoens bruksegenskaper.

![Configurer clés](assets/fr/06.webp)

Først og fremst kan du i menyen "Avanserte innstillinger" bestemme "beskrivelsestype", dvs. måten kontrakten skal skrives på i kjeden. Du kan velge mellom to typer: P2WSH (SegWit) eller Taproot. I begge tilfeller vil semantikken i utgiftsbetingelsene være den samme. P2WSH gjør kontrakten enklere å forstå, mens Taproot er overlegen ved at den skjuler ubrukte betingelser og sparer kostnader ved gjenfinning.

Dette valget er valgfritt: Hvis du er i tvil, bør du velge standardalternativet (P2WSH i versjon 0.9, men dette kan bli endret).

![Choisir le type de descripteur](assets/fr/07.webp)

Deretter konfigurerer du primærnøkkelen (*primary key*). Denne nøkkelen (eller rettere sagt, dette settet med nøkler) vil bli brukt til den aktuelle pengebruken, som ikke er underlagt noen tidsbetingelser. Ved å klikke på "*Set*" kan du velge den tilhørende *signeringsenheten*. I vårt tilfelle har vi valgt Ledger Nano S Plus maskinvarelommebok.

Tillat deling av den utvidede offentlige nøkkelen fra enheten. Gi denne nøkkelen et meningsfylt navn (i dette tilfellet "Nano S+"). Merk at alle applikasjoner som er installert på enheten, vil fortsette å fungere som normalt.

![Configurer clé principale](assets/fr/08.webp)

Deretter angir du tilbakebetalingsforsinkelsen, dvs. tiden etter at midlene kan brukes av *arvenøkkelen*. Denne forsinkelsen defineres i form av blokker, med gjennomsnittlig 10 minutter mellom hver blokk. Den kan variere fra 10 minutter (1 blokk) til rundt 15 måneder (65 535 blokker). Denne øvre grensen er en begrensning i Bitcoin-protokollen, ettersom låsetiden er kodet på 16 bits.

Med mindre det foreligger spesielle omstendigheter, bør du velge den lengste leveringstiden: 15 måneder eller 65 535 blokker. Dette vil spare deg for kostnader. Vi anbefaler imidlertid at du utfører oppdateringsprosedyren (beskrevet i avsnittet "Oppdatering av porteføljen") én gang i året, alltid på samme tid av året, for å "ritualisere" denne praksisen og unngå at du glemmer den.

Her har vi satt opp en gjenopprettingstid på én time (6 blokker) for å utføre testene våre.

![Configurer temps de verrouillage](assets/fr/09.webp)

Til slutt må du sette opp nøkkelen til boet ditt. Denne nøkkelen (eller rettere sagt, settet med nøkler) vil bli brukt til å gjenopprette midler i tilfelle du skulle forsvinne. Klikk på "*Set*", velg signeringsenhet og valider delingen av den utvidede offentlige nøkkelen på den.

I denne veiledningen har vi valgt Jade. Gi nøkkelen et stemningsfullt navn (her "Jade"). Som med den første enheten, vil konvensjonelle kontoer fortsette å fungere.

![Configurer clé de succession](assets/fr/10.webp)

Når alle disse handlingene er fullført, kontrollerer du at alt er i orden, og klikker på "*Fortsett*" for å bekrefte valgene dine.

![Confirmer clés](assets/fr/11.webp)

Neste trinn er å lagre porteføljebeskrivelsen din. Dette er informasjonen du trenger for å finne midlene på kontoen din. I motsetning til den mnemoniske frasen tillater ikke deskriptoren deg å bruke midler, så å avsløre det vil bare utgjøre et konfidensialitetsproblem (personen vil vite alle transaksjonene dine).

Lagre to kopier av beskrivelsen på et elektronisk medium, for eksempel en USB-pinne. Sørg for at du også skriver ut to kopier på papir, slik at du har tilgang til dem hvis det elektroniske mediet skulle bli skadet. Hver sikkerhetskopi må være knyttet til en signaturenhet.

![Sauvegarder descripteur](assets/fr/12.webp)

Vår deskriptor (som analyseres på slutten av veiledningen) er som følger:

```plaintext
wsh(or_d(pk([3689a8e7/48'/0'/0'/2']xpub6FKYNH4XbbdADV98yTVxgZZrtB4eE2tiUPreEv5iJAS3U1CvXGAtQGFXSHyFYdYNn9wNa9KU1pwfYoxQhwq4sPXGihD725VncdSy66v9WQa/<0;1>/*),and_v(v:pkh([42e629dd/48'/0'/0'/2']xpub6DpQGv9LkwAQXvghWASvsfA7t1BVj7bGDQ939v32iB6aUJsMRB6inckim26gRp74NBdS2zuyfHNXDZ9dTuNXkFFiz6QvwEeVvBuC2cnRWQd/<0;1>/*),older(6))))#8alrve5h
```

Det siste trinnet i den innledende porteføljekonfigurasjonen er å verifisere deskriptoren i hver av maskinvareporteføljene som fungerer som signaturenheter.

![Enregistrer descripteur](assets/fr/13.webp)

Gjør det samme for hver signeringsenhet. Du må kontrollere og bekrefte at deskriptoren er lagt til i hver maskinvareportefølje.

![Enregistrer descripteur Nano S Plus](assets/fr/14.webp)

Lommebokinformasjonen din er nå registrert, og det eneste som gjenstår er å konfigurere hvordan du vil koble deg til Bitcoin-nettverket. Du kan velge å bruke din egen node (lokal eller ekstern) eller bruke WizardSardines infrastruktur. I sistnevnte tilfelle må du koble en e-postadresse til lommeboken din, slik at du kan hente deskriptoren. WizardSardine vil ha tilgang til alle transaksjonene dine. Det første alternativet anbefales derfor.

![Sélectionner connexion réseau](assets/fr/15.webp)

Vi har valgt å bruke vår egen node. Du kan bruke en eksisterende node, eller installere en *beskåret node* på din maskin. Hvis du ikke har tilgang til noen annen node, må du installere din egen node på maskinen din, noe som bør ta litt tid (i størrelsesorden flere dager).

![Choisir type de nœud](assets/fr/16.webp)

I denne veiledningen har vi brukt en eksisterende (offentlig) Electrum-server. Men vær forsiktig! Den hadde tilgang til all vår aktivitet med Liana-lommeboken. Så bruk din egen node hvis du vil beskytte personvernet ditt.

![Connexion serveur Electrum public](assets/fr/17.webp)

Når nodekonfigurasjonen er fullført, åpnes hovedskjermbildet med den nyopprettede Liana-lommeboken din.

Benytt anledningen til å oppbevare gjenvinningsenheten på et trygt sted. Den bør oppbevares på et strategisk sted, slik at arvingene dine kan finne den hvis du skulle gå bort.

For ekstra sikkerhet kan du legge komponentene som brukes til gjenoppretting, i en forseglet pose (*tamper-evident bag*) og skrive ned serienummeret et sted. Dette sikrer at ingen har hatt tilgang til den, og at enheten din forblir gyldig.

I vårt eksempel har vi satt sammen følgende elementer:


- Blockstream Jade som signaturenhet for boet;
- En USB-kabel for tilkobling og lading av enheten;
- En papirbackup av setningen i tilfelle funksjonsfeil eller skade på enheten (merk at mediet også kan være av metall, og dermed beskyttet mot vær og vind, slik tilfellet er med for eksempel Cryptosteel-kapsler);
- USB-nøkkelen som inneholder porteføljebeskrivelsen ;
- En papirbackup av deskriptoren, i tilfelle feil eller skade på USB-nøkkelen (denne backupen er ikke fotografert her);
- Et arvebrev som beskriver hvilke skritt som skal tas for å få tilbake midlene.

![Éléments de récupération](assets/fr/18.webp)

Og vi setter disse varene under forsegling!

![Sachet scellé récupération](assets/fr/19.webp)

## Mottak av midler

Lianas hovedskjerm viser saldoen din og transaksjonene (tidligere og nåværende) som er knyttet til porteføljen din. I vårt tilfelle er saldoen null, noe som er normalt.

![Écran principal](assets/fr/20.webp)

For å motta penger går du til fanen "*Motta*" og klikker på "*Generere adresse*". En ny adresse vises på skjermen. Den er lengre enn i konvensjonelle porteføljer: det er en adresse knyttet til en frittstående kontrakt (P2WSH eller Taproot).

![Générer nouvelle adresse](assets/fr/21.webp)

Du må bekrefte denne adressen på maskinvareporteføljen din ved å klikke på "*Verify on hardware device*".

![Vérifier adresse portefeuille matériel](assets/fr/22.webp)

Når pengene er sendt, vises transaksjonen på hovedskjermen (først som ubekreftet, deretter som bekreftet). Her har vi sendt 50 000 satoshier (litt over 50 dollar på overføringstidspunktet) for denne testen. Det sier seg selv at beløpet som overføres i ditt tilfelle må være en størrelsesorden høyere enn denne verdien, på grunn av transaksjonsgebyrer.

![Vérifier solde](assets/fr/23.webp)

Du kan sjekke utløpsstatusen til midlene dine ved å gå til "*Coins*"-fanen. Denne fanen viser deg de forskjellige myntene (UTXO) i lommeboken din. Her kan vi se at mynten på 50 000 satoshis som ble opprettet av transaksjonen vår, utløper samme dag (om én time).

![Obtenir informations pièce](assets/fr/24.webp)

For å bedre forstå UTXO-representasjonsmodellen som brukes i Bitcoin, kan du konsultere den første delen av kurset om konfidensialitet i Bitcoin skrevet av Loïc Morel :

https://planb.network/courses/btc204
## Løpende utgifter

Løpende utgifter er den normale situasjonen for bruk av Liana. Å sende bitcoins med hovednøkkelen fungerer som i alle klassiske Bitcoin-lommebøker som Electrum eller Sparrow.

For å foreta en belastning går du til "*Send*"-fanen og legger inn de viktigste opplysningene: mottakerens BTC-adresse, beløpet som skal sendes og ønsket belastningssats. Du kan også legge til en beskrivelse (som lagres lokalt) for å gjøre det enklere for deg. I vårt eksempel sendte vi 10 000 satoshis til en viss Bob, til en avgiftssats på 4 sat/ov, eller 0,67 dollar på transaksjonstidspunktet.

Liana tilbyr også "myntkontroll": Du angir hvilken mynt (UTXO) du ønsker å bruke. Her har vi valgt den tidligere opprettede mynten på 50 000 satoshis.

![Envoyer fonds clé principale](assets/fr/25.webp)

Signer deretter transaksjonen med signaturenheten din som er koblet til hovednøkkelen, ved å klikke på "*Sign*". Du må verifisere og bekrefte transaksjonen på maskinvarelommeboken din. Her har vi brukt Nano S Plus til å signere transaksjonen.

![Signer transaction clé principale](assets/fr/26.webp)

Til slutt sender du transaksjonen over nettverket ved å klikke på "*Broadcast*". Merk at når du sender penger, tilbakestilles gjenopprettingstiden for brukte mynter.

![Diffuser transaction clé principale](assets/fr/27.webp)

Transaksjonen vises på hovedskjermen, og saldoen din oppdateres.

![Solde après dépense](assets/fr/28.webp)

## Oppdatering av porteføljen

Som forklart ovenfor krever Liana-lommeboken at du oppdaterer midlene dine regelmessig ved å utføre en transaksjon på blokkjeden. Hvis du ikke gjør det, kan pengene dine bli gjenopprettet av arvingen din (eller av den andre enheten din i tilfelle en forbedret sikkerhetskopi). Denne situasjonen er ikke ekstremt farlig, men den motvirker formålet med å sette opp denne mekanismen: å ha kontroll over bitcoinsene dine uten å måtte ty til en betrodd tredjepart, samtidig som du drar nytte av et sikkerhetsnett.

En advarsel vises før midlene dine (eller deler av dem) utløper og kan brukes av gjenopprettingsnøkkelen. Det vil indikere at "gjenopprettingsveien" (*gjenopprettingsvei*) snart vil være tilgjengelig. Gitt den korte gjenopprettingstiden vår (en time), vises denne meldingen direkte i vårt tilfelle.

![Avertissement chemin récupération](assets/fr/29.webp)

Når fristen nærmer seg, vises en knapp der du blir bedt om å oppdatere de aktuelle midlene.

![Actualiser pièces depuis l'écran principal](assets/fr/30.webp)

For å oppdatere myntene dine går du til fanen "*Mynter*" og klikker på "*Oppdater mynt*" i den aktuelle myntboksen. Hvis du har flere mynter, bør du oppdatere dem én etter én og med relativt korte intervaller, av hensyn til konfidensialiteten. For å holde kostnadene nede kan du konsolidere midlene dine ved å sende hele porteføljen til en ny mottakeradresse, men dette vil påvirke konfidensialiteten din.

![Actualiser pièce](assets/fr/31.webp)

Angi ønsket gebyrsats for transaksjonen. Siden dette er en overføring til deg selv, kan du angi en ganske lav gebyrsats, spesielt hvis du gjør det flere dager før utløpet.

![Transfert à soi-même](assets/fr/32.webp)

Transaksjonen (merket "*self-transfer*") vil kun være synlig under fanen "*Transaksjoner*".

![Transactions après auto-transfert](assets/fr/33.webp)

Når det er bekreftet, er mynten din trygg! Du kan være rolig frem til neste utløpsdato.

## Gjenoppretting av Bitcoin

Når du skal gjenopprette midler fra Liana-porteføljen, kan du stå overfor én av to situasjoner. Det kan hende du har tilgang til datamaskinen som programvaren er installert på, og i så fall trenger du bare å åpne den (noe som vil skje i tilfellet med den utvidede sikkerhetskopimodellen). Det kan imidlertid hende at du ikke har tilgang til denne datamaskinen, så vi starter fra bunnen av her. Merk at gjenopprettingsprosedyren er den samme i begge tilfeller.

For å komme i gang kan du laste ned Liana fra [det offisielle Wizardsardine-nettstedet] (https://wizardsardine.com/liana/), eller fra [GitHub-arkivet] (https://github.com/wizardsardine/liana/releases), der du kan sjekke programvarens autentisitet. Installer programvaren og kjør den. I vårt tilfelle er det versjon 0.9 som brukes, så det visuelle kan ha endret seg. På velkomstskjermen velger du alternativet "Legg til en eksisterende Liana-lommebok".

![Ajouter portefeuille existant](assets/fr/34.webp)

Konfigurer hvordan du vil koble deg til nettverket. Du kan velge å bruke din egen node (lokal eller ekstern) eller bruke WizardSardines infrastruktur. I sistnevnte tilfelle trenger du e-postadressen som brukes av porteføljeoppretteren, slik at fondene kan lokaliseres automatisk. Hvis du ikke har denne informasjonen, velger du det første alternativet.

![Sélectionner connexion réseau](assets/fr/35.webp)

Hvis du bruker din egen node, importerer du porteføljebeskrivelsen. Dette er en teknisk beskrivelse av kontoen, som gjør det mulig å hente ut midlene som står på den. I vårt tilfelle er det følgende informasjon:

```plaintext
wsh(or_d(pk([3689a8e7/48'/0'/0'/2']xpub6FKYNH4XbbdADV98yTVxgZZrtB4eE2tiUPreEv5iJAS3U1CvXGAtQGFXSHyFYdYNn9wNa9KU1pwfYoxQhwq4sPXGihD725VncdSy66v9WQa/<0;1>/*),and_v(v:pkh([42e629dd/48'/0'/0'/2']xpub6DpQGv9LkwAQXvghWASvsfA7t1BVj7bGDQ939v32iB6aUJsMRB6inckim26gRp74NBdS2zuyfHNXDZ9dTuNXkFFiz6QvwEeVvBuC2cnRWQd/<0;1>/*),older(6))))#8alrve5h
```

![Importer descripteur](assets/fr/36.webp)

Liana ber deg deretter om å skrive inn en huskefrase. Hvis du har en fungerende signaturenhet (maskinvarelommebok), kan du hoppe over denne delen. Hvis enheten din mangler eller er skadet, men du har de tilsvarende 12 eller 24 ordene, kan du fortsatt bruke dette alternativet. For å være på den sikre siden (hvis beløpet som skal gjenopprettes er høyt), foreslår vi likevel at du skaffer deg en ny maskinvarelommebok og bruker huskeregelen til å gjenopprette nøklene på den.

I vårt tilfelle bruker vi Blockstream Jade-maskinvarelommeboken som gjenopprettingsenhet og velger å hoppe over ("*Skip*") dette trinnet.

![Passer phrase mnémotechnique](assets/fr/37.webp)

Kontroller og lagre deskriptoren i signaturenheten ved å velge den på skjermen. Hvis maskinvarelommeboken ikke vises, må du kontrollere at den er tilkoblet og ulåst. Kontroller og bekreft at denne informasjonen er lagt til på enheten din.

![Enregistrer descripteur sur l'appareil de récupération](assets/fr/38.webp)

Konfigurer noden din. Du kan bruke en eksisterende node eller installere en *beskåret node* på maskinen din. I vårt tilfelle har vi brukt en eksisterende node.

![Choisir type de nœud](assets/fr/39.webp)

I denne opplæringen brukte vi en offentlig Electrum-server. Den hadde imidlertid tilgang til all vår aktivitet med Liana-lommeboken. Hvis du vil beskytte personvernet ditt, bør du bruke din egen node.

![Connexion serveur Electrum public](assets/fr/17.webp)

Når du har konfigurert noden, kommer du til hovedskjermbildet for lommeboken, der du kan se saldo og tidligere transaksjoner knyttet til kontoen. Du kan også se om det er mulig å hente ut midler. Her ser vi at en mynt kan hentes ut.

![Accueil Liana récupération](assets/fr/40.webp)

For å gjenopprette midlene i porteføljen går du til Innstillinger ("*Innstillinger*") nederst til venstre og klikker på "*Gjenoppretting*".

![Récupération dans paramètres](assets/fr/41.webp)

Bruk mynten i lommeboken ved å krysse av i den aktuelle boksen. Angi BTC-adressen du ønsker å sende pengene til, samt transaksjonsgebyret. Klikk deretter på "*Neste*".

![Récupération des pièces](assets/fr/42.webp)

Signer transaksjonen ved å klikke på "*Sign*" og validere transaksjonen på maskinvarelommeboken din.

![Signer transaction clé de récupération](assets/fr/43.webp)

Send den deretter over nettverket ved å klikke på "*Broadcast*".

![Diffuser transaction clé de récupération](assets/fr/44.webp)

Transaksjonen skal vises på hovedskjermen. Når dette er bekreftet, er gjenopprettingen fullført!

![Écran principal après récupération](assets/fr/45.webp)

## Videoer

Hvis du vil vite mer om Liana, kan du se noen videoer som gir deg en klarere idé om hvordan det fungerer. Her er en videopresentasjon av Liana med Kévin Loaec og Antoine Poinsot :

![Vidéo de présentation avec Kévin Loaec et Antoine Poinsot](https://youtu.be/siuLmQo1lM8)

Og her er en veiledning om hvordan du bruker Liana, med Antoine Poinsot :

![Vidéo-tutoriel avec Antoine Poinsot](https://youtu.be/JrG4WMVPZDQ)

Manipulasjonene som vises i sistnevnte, ligner på dem som presenteres i denne veiledningen.

## Bonus: Deskriptoranalyse

Deskriptoren er en tegnstreng som kan leses av mennesker, og som gir en uttømmende beskrivelse av et sett med adresser. Den kombinerer en rekke viktige opplysninger som er nødvendige for å finne delene (UTXO) i en avansert portefølje. Måten deskriptoren skrives på, er basert på [Miniscript syntax] (https://bitbox.swiss/blog/understanding-bitcoin-miniscript-part-2/), skriptspråket som ble utviklet av Andrew Poelstra, Pieter Wuille og Sanket Kanjalkar i 2019.

For å forstå bedre hvorfor denne tegnstrengen er viktig, la oss analysere deskriptoren i eksempelet vårt, som er :

```plaintext
wsh(or_d(pk([3689a8e7/48'/0'/0'/2']xpub6FKYNH4XbbdADV98yTVxgZZrtB4eE2tiUPreEv5iJAS3U1CvXGAtQGFXSHyFYdYNn9wNa9KU1pwfYoxQhwq4sPXGihD725VncdSy66v9WQa/<0;1>/*),and_v(v:pkh([42e629dd/48'/0'/0'/2']xpub6DpQGv9LkwAQXvghWASvsfA7t1BVj7bGDQ939v32iB6aUJsMRB6inckim26gRp74NBdS2zuyfHNXDZ9dTuNXkFFiz6QvwEeVvBuC2cnRWQd/<0;1>/*),older(6))))#8alrve5h
```

Følgende informasjon kan hentes ut fra denne deskriptoren:


- `wsh` (forkortelse for *witness script hash*): Dette er den typen transaksjonsutdata som opprettes. Hvis vi hadde valgt å bruke Taproot, ville identifikatoren ha vært `tr`.
- `eller_d`: Dette er en logisk operator som angir at *en av følgende to* betingelser må være oppfylt for at utgiften skal godtas (`_d` angir en bestemt syntaks).
- `pk` (forkortelse for *public key*): Denne operatøren sjekker en gitt signatur mot følgende offentlige nøkkel, og gir svaret som en boolsk verdi (TRUE eller FALSE).
- `[3689a8e7/48'/0'/0'/2']`: Dette elementet inneholder *fingeravtrykket* av hovednøkkelen for hovedlommeboken (i dette tilfellet Nano S Plus), og avledningsstien til den koblede utvidede privatnøkkelen (som alle andre privatnøkler er avledet fra).
- `xpub6FKY ... WQa`: Dette er den utvidede offentlige nøkkelen knyttet til hovedmaskinvareporteføljen (her Nano S Plus)
- `/<0;1>/*`: Dette er avledningsveiene for å få enkle nøkler og adresser: `0` for mottak, `1` for interne operasjoner (*endring*), med et "jokertegn" (`*`) som tillater sekvensiell avledning av flere adresser på en konfigurerbar måte, på samme måte som "gap limit"-styringen i klassisk porteføljeprogramvare.
- og_v`: Dette er en logisk operator som angir at *følgende to* betingelser må være oppfylt for at utgiften skal godtas (`_v` angir en bestemt syntaks).
- `v:pkh` (forkortelse for *verify: public key hash*): Denne operatøren verifiserer en gitt signatur og offentlig nøkkel mot den offentlige nøkkelhashingen (*hash*) som følger. Dette er i hovedsak den samme kontrollen som for P2PKH- og P2WPKH-skript.
- `[42e629dd/48'/0'/0'/2']`: Dette er det samme elementet som ovenfor (bestående av sporet og avledningsbanen), bortsett fra at sporet til hovednøkkelen til maskinvaregjenopprettingsporteføljen (i dette tilfellet Jade) er angitt.
- `xpub6DpQ ... WQd`: Dette er den utvidede offentlige nøkkelen knyttet til maskinvaregjenopprettingslommeboken (her Jade).
- `older(6)` : Denne operatøren kontrollerer at transaksjonsutdataene som opprettes, må ha en alder som er strengt tatt større enn 6 blokker for å kunne brukes.

Det siste dataelementet (`8alrve5h`) er deskriptorens sjekksum, og tilsvarer porteføljeidentifikatoren.

Skriptene som opprettes av denne porteføljen, vil ha følgende form:

```plaintext
<primary_key> CHECKSIG IFDUP NOTIF DUP HASH160 <recovery_key_hash> EQUALVERIFY CHECKSIGVERIFY <locktime> CHECKSEQUENCEVERIFY ENDIF
```

Siden sikkerheten til Bitcoin-lommeboken din også avhenger av din forståelse av hvordan den fungerer, foreslår jeg at du studerer mekanismene til deterministiske og hierarkiske lommebøker i dybden ved å ta dette gratis opplæringskurset på Plan ₿ Network :

https://planb.network/courses/cyp201