---
name: Ledger Nano S

description: Hvordan sette opp din Ledger Nano S-enhet
---

![bilde](assets/cover.webp)

Kald fysisk lommebok – €60 – Nybegynner – For å sikre €2,000 til €50,000

Ledger er den franske løsningen for å sikre bitcoins på en enkel måte.

I denne veiledningen diskuterer vi også passfrase-delen, en avansert sikkerhetsløsning for lagring av store summer: 20,000€ – 100,000€.

https://www.youtube.com/watch?v=_vsHNTLi8MQ

# Koble Ledger til Sparrow Bitcoin Wallet (skriveguide)

Sørg for at du først går gjennom den andre delen "Bruk av Bitcoin Hardware Wallets". Jeg vil skumme gjennom noen steg og fokusere mest på det som er spesifikt for Ledger her.

## Sette opp enheten

Ledger kommer med sin egen USB-kabel. Sørg for at du bruker den og ikke bare en hvilken som helst gammel kabel. Noen USB-kabler er kun for strøm. Denne overfører data OG strøm. Når jeg har brukt enheten med en telefonladings-USB-kabel som lå rundt, har enheten mislyktes i å koble til.

Koble den til datamaskinen din, og enheten vil slå seg på.

![bilde](assets/1.webp)

Sykle gjennom alternativene. Du vil se

1. Sett opp som ny enhet
2. Gjenopprett fra gjenopprettingsfrase

I bunn og grunn spør den om du vil at enheten skal opprette en seed for deg, eller om du allerede har en som du ønsker å bruke. Det er beste praksis å lage din egen seed, men å gjøre det på en sikker måte er veldig avansert og utenfor rekkevidden av denne artikkelen. Velg "Sett opp som ny enhet"

Du vil deretter bli bedt om å velge en PIN-kode. Dette er ikke en del av din Bitcoin seed og er spesifikk for denne enheten bare. Den låser enheten.

Den vil deretter presentere deg for 24 ord som du trenger å sykle gjennom og skrive ned.

Merkelig nok, når du kommer til slutten, sier den "trykk til venstre for å verifisere ordene dine". Det beskriver ikke hvordan du bekrefter for å fortsette, det betyr bare at du kan gå tilbake og se på ordene igjen. Trykk til høyre i stedet, og bekreft ved å trykke til venstre og høyre samtidig.

Neste bit er super irriterende. Den blander opp de 24 ordene, og du må bekrefte hver enkelt, 1 til 24, ved å sykle gjennom alle ordene for hvert valg. Når du er ferdig, lar den deg bekrefte med et trykk på to knapper og fortsette.

![bilde](assets/2.webp)

Du vil se på dashbordet ditt at du har en innstillingsknapp, og en pluss-tegn-knapp som lar deg installere apper. Men du må koble til Ledger Live først. Det gjør vi neste…

## Last ned Ledger Live

Du kunne laste ned Ledger Live fra deres nettside, men det er bedre å få den fra GitHub, hvor kildekoden er oppbevart.

Google "ledger live GitHub" eller klikk på denne lenken https://github.com/LedgerHQ/ledger-live-desktop

![bilde](assets/3.webp)

Rull ned til du ser overskriften, "Downloads"…

![bilde](assets/4.webp)

Nederst vil du se lenken: Instruksjoner for å verifisere hashen og signaturene til installasjonspakkene er tilgjengelige på denne siden. Klikk på den lenken.(https://live.ledger.tools/lld-signatures)

![bilde](assets/5.webp)

Øverst er det lenkevalg for programvarepakken du trenger, avhengig av operativsystemet ditt. Klikk på den som passer for å laste ned.

Neste, vi ønsker å verifisere nedlastningens hash, for ekstra sikkerhet.
Ledger publiserer hashen for hver av filene som er tilgjengelige på denne siden. Vi vil nå hashe nedlastingen og sammenligne resultatet. Det må være identisk for å forsikre oss om at filen ikke har blitt manipulert.

Åpne terminal på en Mac eller CMD på Windows. Følg disse kommandoene...

cd Downloads

<Enter>

```bash
shasum -a 512 ledger-live-desktop-2.32.2-mac.dmg # <--- For Mac
certutil -hashfile ledger-live-desktop-2.32.2-win.exe SHA512 # <--- For Windows
```

<Enter>

Forhåpentligvis er det åpenbart at kommandoene begynner etter pilene. Sørg for, hvis denne artikkelen er utdatert, at du endrer filnavnet i kommandoene til nøyaktig det filnavnet du lastet ned. Du må trykke <Enter>-tasten etter hver kommando. Kommandoene som vist her passer kanskje ikke på én linje i nettleseren din. Merk, alt er skrevet på én linje.

Se på outputen av hashen og forsikre deg om at den er identisk med den som er publisert på GitHub.

Ideelt sett vil du bli ekstra nøye og forsikre deg om at hashene som er publisert ikke er falske. Vi gjør dette med gpg-signaturer, men det er utenfor rekkevidden av denne artikkelen. Hvis du vil lære om det (og det foreslår jeg at du til slutt gjør), så se gjennom denne artikkelen.

## Koble til Ledger Live

Før du kjører Ledger Live, hjelper det litt på personvernet å slå på en VPN. Ledger vil fortsatt få alle adressene dine, men de vil ikke kjenne din IP-adresse, som avslører hjemmeadressen din. Mullvad VPN er en utmerket VPN-tjeneste og den er ikke veldig dyr (jeg reklamerer ikke, det er bare det jeg bruker).

Installer programvaren på datamaskinen din og kjør den.

![bilde](assets/6.webp)

Velg enheten din, og velg "Første gang bruk..."

![bilde](assets/7.webp)

Du vil deretter bli tatt gjennom en veiviser, men vi har allerede gjort alle disse stegene så du kan sykle gjennom.

![bilde](assets/8.webp)

Etter mange steg og en quiz, vil den sjekke at enheten er ekte. Du må sørge for at du er koblet til og har tastet inn PIN-koden, og deretter vil den spørre på enheten om du tillater Ledger Live å koble til. Du må bekrefte det, selvfølgelig.

![bilde](assets/9.webp)

Det var litt shitcoin-reklame forkledd som "release notes" i neste pop-up. Avvis den, og da bør du komme til denne skjermen.

![bilde](assets/10.webp)

Du må klikke på "Legg til konto" for å få en Bitcoin Wallet.

![bilde](assets/11.webp)

Sørg for at du velger Bitcoin, og ikke Bitcoin Cash eller noen annen shitcoin. Den vil sjekke enheten, og du må bekrefte for å fortsette PÅ ENHETEN. Den vil beregne adresser i et par minutter. Deretter klikker du FERDIG.

![bilde](assets/12.webp)
![bilde](assets/13.webp)

Flott. Nå har du en shitcoin wallet manager som inneholder en Bitcoin wallet på datamaskinen din. Du trenger faktisk ikke dette lenger og kan kvitte deg med det. Det egentlige formålet var å få Bitcoin Appen på selve enheten, og dette var den eneste måten, kort av å utføre noen ekstreme programvareingeniørteknikker.

Husk at tidligere, på enheten, hadde vi en innstillingsknapp og en pluss-tegn-knapp. Nå har vi en ekstra knapp – Bitcoin App-knappen.

Du kan slå av Ledger Live nå.

## Legg til en passfrase
Nå som vi har Bitcoin-appen, kan vi legge til en passfrase til vår seed-frase. Vi kunne ikke gjøre det før når seeden først ble opprettet fordi vi i starten ikke hadde Bitcoin-appen, og vi måtte koble til Ledger Live for å få den.

Gå til "innstillinger"-menyen på enheten, deretter undermenyen "sikkerhet". Velg deretter passfrase. Du vil se "Avansert funksjon". Klikk på høyre knapp, du vil se "les manualen..." og deretter etter et klikk på høyre knapp, vil du se "tilbake". Men det er ikke slutten. Intuitivt ville du tenke det, men klikk på høyre knapp igjen. Du vil se "sett opp passfrase".

Du kan bestemme deg for å "knytte til PIN" eller "Sett midlertidig". Jeg anbefaler "knytte til PIN". På den måten kan du få tilgang til forskjellige lommebøker avhengig av PIN-koden du taster inn når du først slår på enheten. Hvis du "setter midlertidig", må du taste inn passfrasen hver gang du ønsker å få tilgang til den lommeboken, men det er alltid fra standard PIN.

Tast inn passfrasen og bekreft den.

Den vil spørre deg om "Nåværende PIN". Dette er ikke PIN-koden du assosierer med den nye passfrasen. Det er PIN-koden du tastet inn da du slo på enheten for denne økten.

Du kan nå gå ut til hovedmenyen ved å velge tilbake-alternativet noen ganger.

## Overvåke Lommebok

I tidligere artikler forklarte jeg hvordan du laster ned og verifiserer Sparrow-lommeboken, og hvordan du kobler den til din egen node, eller en offentlig node. Du bør følge disse veiledningene:

- Installer Bitcoin Core (https://armantheparman.com/bitcoincore/)

- Installer Sparrow Bitcoin Wallet (https://armantheparman.com/download-sparrow/)

- Koble Sparrow Bitcoin Wallet til Bitcoin Core (https://armantheparman.com/sparrowcore/)

Et alternativ til å bruke Sparrow Bitcoin Wallet er Electrum Desktop Wallet, men jeg vil fortsette å forklare Sparrow Bitcoin Wallet ettersom jeg anser den for å være den beste for de fleste. Avanserte brukere kan like å bruke Electrum som et alternativ.

Vi vil nå laste den opp og koble Ledgeren, med lommeboken som inneholder passfrasen. Denne lommeboken har aldri blitt eksponert for Ledger Live fordi den ble opprettet ETTER at vi koblet enheten til Ledger Live. Sørg for at du aldri kobler den til Ledger Live igjen for å ikke eksponere din nye private lommebok.

Opprett en Ny Lommebok:

![bilde](assets/14.webp)

Gi den et pent navn

![bilde](assets/15.webp)

Legg merke til avkrysningsboksen, "Har eksisterende transaksjon". Hvis dette er en lommebok du har brukt før, så kryss av ellers vil saldoen din feilaktig vise som null. Å krysse av i denne boksen ber Sparrow om å undersøke Bitcoin Cores database (blockchain) for tidligere transaksjoner. For denne veiledningen bruker vi en helt ny lommebok, så du kan la boksen være ukrysset.

![bilde](assets/16.webp)

Klikk på "Tilkoblet Maskinvarelommebok" og sørg for at enheten faktisk er koblet til, slått på, PIN-kode er tastet inn, og du har gått inn i Bitcoin-appen.

![bilde](assets/17.webp)

Klikk "Skann" og deretter "Importer Keystore" på neste skjerm.

![bilde](assets/18.webp)

Det er ingenting å redigere på neste skjerm, Ledger har fylt det ut for deg. Klikk "Bruk"

![bilde](assets/19.webp)
Neste skjerm lar deg legge til et passord. Ikke forveksle dette med "passphrase"; mange vil gjøre det. Navngivningen er uheldig. Passordet lar deg låse denne lommeboken på datamaskinen din. Det er spesifikt for denne programvaren på denne datamaskinen. Det er ikke en del av din Bitcoin private nøkkel.
![bilde](assets/20.webp)

Etter en pause, mens datamaskinen tenker, vil du se at knappene på venstre side endrer seg fra grå til blå. Gratulerer, lommeboken din er nå klar til bruk. Gjør og send transaksjoner etter hjertets innhold.

![bilde](assets/21.webp)

## Mottak

For å motta litt bitcoin, gå til fanen Adresser på venstre side og velg en av adressene for å motta. Bare høyreklikk på adressen du vil ha, og velg "kopier adresse". Gå deretter til din børs hvor pengene sendes fra og lim den inn der. Eller du kan gi adressen til en kunde som kan bruke den til å betale deg.

Når du bruker lommeboken for første gang, bør du motta et veldig lite beløp, øv på å bruke det til en annen adresse, enten innenfor lommeboken eller tilbake til børsen, for å bevise at lommeboken fungerer som forventet.

Når du har gjort det, må du sikkerhetskopiere ordene du skrev ned. En enkelt kopi er ikke nok. Ha minst to papirkopier (metall er bedre), og oppbevar dem på to forskjellige, godt sikrede steder. Dette reduserer risikoen for at en naturkatastrofe ødelegger din HWW og papirsikkerhetskopi i én hendelse. Se "Bruk av Bitcoin Hardware Wallets" for en full diskusjon om dette.

## Sending

![bilde](assets/22.webp)

Når du gjør en betaling, må du lime inn adressen du betaler til i "Betal til"-feltet. Du kan faktisk ikke la Etikett være tom, det er bare for dine egne lommebøkers registreringer, men Sparrow tillater det ikke – bare skriv inn noe (bare du vil se det). Angi beløpet og du kan også manuelt justere gebyret du ønsker.

Lommeboken kan ikke signere transaksjonen med mindre HWW er tilkoblet. Det er jobben til HWW – å motta transaksjonen, signere den, og gi den tilbake, signert. Sørg for at når du signerer på enheten, visuelt inspiserer du at adressen du betaler til er den samme på enheten og på dataskjermen, og fakturaen du mottar (f.eks. du kan ha mottatt en e-post for å betale en bestemt adresse).

Vær også oppmerksom på at hvis du velger å bruke en mynt som er større enn betalingsbeløpet, vil resten bli sendt tilbake til en av dine lommebøkers vekseladresser. Noen mennesker har ikke kjent til dette, og sett opp transaksjonen sin på en offentlig blockchain, og trodd at noen bitcoin ble sendt til en angripers adresse, men faktisk var det deres egen vekseladresse.

## Firmware

For å oppdatere firmwaren, må du koble til Ledger Live. Hvis du vil gjøre dette, bør du tørke enheten først, og sørge for at du har sikkerhetskopieringsordene og passphrase tilgjengelig for å gjenopprette enheten. Grunnen til at jeg foretrekker å tørke enheten først er at du må koble enheten din til Ledger Live for å oppdatere firmwaren, og jeg foretrekker å ikke eksponere din nye lommebok (den med passphrase) for Ledger Live, noensinne. Jeg stoler bare ikke på at Ledger ikke trekker ut min offentlige nøkkelinformasjon fra enheten når jeg kobler til Ledger Live. De hevder de ikke gjør det, men jeg kan ikke verifisere det selv med mindre jeg leser koden, og forstår den interne maskinvaren også.

## Konklusjon
Denne artikkelen viste deg hvordan du kan bruke en Ledger HWW på en tryggere og mer privat måte enn det som er annonsert – men denne artikkelen alene er ikke nok. Som jeg sa i starten, bør du kombinere den med informasjonen som er gitt i "Bruk av Bitcoin Hardware Wallets". Tips:

Statisk Lightning-adresse: dandysack84@walletofsatoshi.com
https://armantheparman.com/ledgersparrow/

For å utforske dette emnet videre og styrke sikkerheten til lommeboken din på en Ledger Nano med en BIP39-passfrase, inviterer jeg deg til å sjekke ut denne omfattende opplæringen:

https://planb.network/tutorials/wallet/hardware/passphrase-ledger-9ae6d9a2-7293-438a-8fe0-e59147ef2f49