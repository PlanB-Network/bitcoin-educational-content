---
name: Trezor model One
description: Oppsett og bruk av Trezor model One
---

![cover](assets/cover.webp)

Kald hardware lommebok – 60€ – Nybegynner – Sikrer mellom 2 000€ og 50 000€.

Som en kald fysisk lommebok, er Trezor ideell for å starte med Bitcoin. Den er enkel å bruke, ikke for dyr og funksjonell.

Vi har allerede laget veiledninger om hvordan du bruker den:

1. Sette den opp
2. Gjenopprette bitcoins
3. Bruke, sende og motta bitcoins

Vil du også ha din egen Trezor?
Du kan bidra til prosjektet ved å klikke nedenfor!

sette opp -https://www.youtube.com/watch?v=q-BlT6R4_bE

gjenoppretting: https://www.youtube.com/watch?v=3n4d4egjiFM

bruk: https://www.youtube.com/watch?v=syouZjLC1zY

## skriveguide

guide foreslått av https://armantheparman.com/trezor/

## Sette opp Trezor

Trezor kommer med sin egen mikro USB-kabel. Sørg for at du bruker den og ikke bare en hvilken som helst gammel kabel som ligger rundt. Noen USB-kabler er kun for strøm. Denne overfører både data OG strøm. Hvis du bruker enheten med en USB-kabel for lading av telefon, kan enheten mislykkes i å koble til.

Koble den til datamaskinen din, og enheten vil slå seg på. Du vil få en melding som sier "Gå til Trezor.io/start". Gjør det, og last ned Trezor Suite til datamaskinen din.

![image](assets/0.webp)

Klikk på nedlastingsknappen ("Get Desktop App")

![image](assets/1.webp)

Legg merke til Signature og Signing key lenkene. For å verifisere nedlastingen (sjekk at nedlastingen din ikke har blitt tuklet med), er det ytterligere trinn som er valgfrie hvis du er nybegynner, men OBLIGATORISKE hvis du har betydelig formue å sikre. Instruksjoner for det er i Appendix A (slutten av veiledningen)

Koble Trezor til datamaskinen med mikro USB-kabelen, og installer og kjør programmet. Slik ser det ut på en Mac:

![image](assets/2.webp)

Du vil få en dum advarsel etter å ha kjørt programmet, bare fortsett:

![image](assets/3.webp)

Klikk på Sett opp Trezor

![image](assets/4.webp)

Hvis firmwaren er utdatert, la Trezor oppdatere firmwaren.

Deretter kan du opprette et nytt frø, eller gjenopprette en lommebok fra en annen enhet med et frø du allerede har. Jeg vil gå gjennom å opprette et nytt frø.

![image](assets/5.webp)

Klikk "Opprett ny lommebok" – og bekreft at du vil gjøre dette på enheten selv ved å klikke på bekreftelsesknappen.

Deretter klikker du på det eneste alternativet "Standard frø sikkerhetskopi"

![image](assets/6.webp)

Deretter klikker du "opprett sikkerhetskopi"

![image](assets/7.webp)

Klikk på de tre avkrysningsfeltene for å gjøre dem grønne (les selvfølgelig hver melding), og klikk deretter "begynn sikkerhetskopi".

![image](assets/8.webp)

Deretter vil du se dette:

![image](assets/9.webp)

Din Trezor viser din 12-ords minnefrase. **Denne minnefrasen gir full og ubegrenset tilgang til alle dine bitcoins**. Enhver som har tilgang til denne frasen kan stjele midlene dine, selv uten fysisk tilgang til din Trezor. 12-ords frasen lar deg gjenopprette tilgangen til dine bitcoins i tilfelle tap, tyveri eller skade på din hardware-lommebok. Derfor er det svært viktig å lagre den nøye og oppbevare den på et trygt sted.

Du kan skrive den ned på pappkortet som følger med i esken, eller for ekstra sikkerhet anbefaler jeg at du graverer den på en rustfri stålplate for å beskytte den mot brann, flom eller kollaps.

For mer informasjon om hvordan du riktig sikkerhetskopierer og administrerer din minnefrase, anbefaler jeg sterkt å følge denne andre veiledningen, spesielt hvis du er nybegynner:

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270


![image](assets/10.webp)

Neste trinn er å sette opp PIN-koden. PIN-koden brukes til å låse opp din Trezor. Den fungerer som beskyttelse mot uautorisert fysisk tilgang. Denne PIN-koden spiller ingen rolle i utledning av de kryptografiske nøklene til lommeboken din. Dermed, selv uten tilgang til denne PIN-koden, vil det å eie din 12- eller 24-ords minnefrase tillate deg å gjenvinne tilgang til dine bitcoins.

Det anbefales å velge en PIN-kode som er så tilfeldig som mulig. Sørg også for å lagre denne koden et annet sted enn der du oppbevarer din Trezor (for eksempel i en passordbehandler).

Du kan velge en PIN-kode med opptil 9 sifre. Jeg anbefaler å gjøre den så lang som mulig.


![image](assets/11.webp)
Du har muligheter til å legge til shitcoins i lommeboken din – jeg oppfordrer deg til ikke å gjøre det, og kun spare i Bitcoin, som jeg forklarer her (hvorfor bitcoin) og her (hvorfor kun bitcoin).
![bilde](assets/12.webp)

Navngi lommeboken din, og klikk på "Access Suite":

![bilde](assets/13.webp)

Før du fortsetter, kan du, hvis du ønsker det, legge til en BIP39-passfrase. En BIP39-passfrase er et valgfritt passord som du kan velge fritt, og som legges til din mnemoniske frase for å styrke sikkerheten til lommeboken. Med denne funksjonen aktivert vil tilgang til din Bitcoin-lommebok kreve både den mnemoniske frasen og passfrasen. Uten en av dem vil det være umulig å gjenopprette lommeboken.

Før du konfigurerer dette alternativet på din Trezor, anbefales det sterkt å lese denne artikkelen for å fullt ut forstå hvordan passfrasen fungerer i teorien, og unngå feil som kan føre til tap av dine bitcoins:

https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

For å aktivere det, må du velge alternativet "Hidden wallet" og notere det i det tilsvarende feltet. Hver gang du får tilgang til lommeboken din via Trezor Suite, vil du bli spurt om du ønsker å bruke passfrasen eller ikke.


![bilde](assets/14.webp)

Det er også viktig å sikkerhetskopiere denne passfrasen riktig, på samme måte som din mnemoniske frase. Å miste den tilsvarer å miste tilgangen til dine bitcoins. Jeg anbefaler sterkt å ikke stole utelukkende på hukommelsen din, da dette urimelig øker risikoen for tap. Ideelt sett bør du skrive den ned på et fysisk medium (papir eller metall) adskilt fra den mnemoniske frasen. Denne sikkerhetskopien bør selvfølgelig lagres et annet sted enn din mnemoniske frase for å unngå at begge blir kompromittert samtidig.

For at den skal være effektiv, må du velge en sterk, tilfeldig passfrase som inkluderer alle typer tegn og er tilstrekkelig lang (som et sterkt passord).

![bilde](assets/15.webp)

Jeg liker at det kalles en "skjult" lommebok, da det delvis forklarer hvordan passfraser fungerer.

Bekreft passfrasen på enheten.

Siden denne lommeboken er tom, ble jeg bedt om å bekrefte at passfrasen er korrekt:

![bilde](assets/16.webp)

Deretter vil du bli spurt om du ønsker å aktivere merking. Ikke noe jeg har utforsket, men det høres ut som en måte du kan merke transaksjonene dine på og lagre dataene på datamaskinen eller i skyen.

![bilde](assets/17.webp)

Til slutt vil lommeboken din være tilgjengelig:

![bilde](assets/18.webp)

Det du har på datamaskinen din kalles en "watching wallet", fordi den har dine offentlige nøkler (og adresser), men ikke dine private nøkler. Du trenger de private nøklene for å bruke (ved å signere transaksjoner med de private nøklene). Måten å gjøre det på er ved å koble til maskinvarelommeboken. Poenget med maskinvarelommeboken er at transaksjoner kan sendes frem og tilbake mellom datamaskinen og Trezor, en signatur kan påføres inne i Trezor, og den private nøkkelen forblir alltid inne i enheten (for sikkerhet mot datamaskinmalware).

Trezor Suite er en dårlig watching-wallet av ulike grunner. Den er OK for det helt grunnleggende, men hvis du vil gå videre, les videre og lær hvordan du kobler enheten til Sparrow Bitcoin Wallet.

## Watching Wallet

I tidligere artikler forklarte jeg hvordan du laster ned og verifiserer Sparrow Bitcoin Wallet, og hvordan du kobler den til din egen node, eller en offentlig node. Du kan følge disse veiledningene:

- Installer Bitcoin Core
- Installer Sparrow Bitcoin Wallet
- Koble Sparrow Bitcoin Wallet til Bitcoin Core

Et alternativ til å bruke Sparrow Bitcoin Wallet er Electrum Desktop Wallet, men jeg vil fortsette å forklare Sparrow Bitcoin Wallet da jeg anser den for å være den beste for de fleste. Avanserte brukere kan like å bruke Electrum som et alternativ (se min veiledning).

Vi vil nå laste opp Sparrow og koble til Trezor (med frøfrasen, men nå med en passfrase). Denne lommeboken har aldri vært eksponert for Trezor Suite fordi den vil bli opprettet ETTER at vi koblet enheten til Trezor Suite. Sørg for at du aldri kobler den til Trezor Suite igjen for å ikke eksponere din nye lommebok. (Du kan koble den til uten passfrase fordi det kan være din lokkelommebok).

Opprett en ny lommebok:

![bilde](assets/19.webp)

Navngi den noe pent

![bilde](assets/20.webp)

Klikk på "Connected Hardware Wallet".

![bilde](assets/21.webp)

![bilde](assets/22.webp)
Klikk på "Scan" og deretter "set passphrase" på neste skjerm for å opprette en helt ny lommebok (bruk en helt ny passfrase, f.eks. den gamle passfrasen med et tall etter ville fungere). Deretter "send passphrase", og bekreft den på enheten.
![image](assets/23.webp)

Deretter klikker du på "import keystore".

Det er ingenting å redigere på neste skjerm, Trezor har fylt det ut for deg. Klikk på "Apply"

![image](assets/24.webp)

Neste skjerm lar deg legge til et passord. Ikke forveksle dette med "passphrase"; mange vil gjøre det. Navngivningen er uheldig. Passordet lar deg låse denne lommeboken på datamaskinen din. Det er spesifikt for denne programvaren på denne datamaskinen. Det er ikke en del av din Bitcoin private nøkkel.

Klikk på "Apply"

![image](assets/25.webp)

Etter en pause, mens datamaskinen tenker, vil du se at knappene på venstre side endrer seg fra grå til blå. Gratulerer, lommeboken din er nå klar til bruk. Gjør og send transaksjoner etter hjertens innhold.

![image](assets/26.webp)

Mottak

For å motta litt bitcoin, gå til fanen Adresser på venstre side og velg en av adressene for å motta. Bare høyreklikk på adressen du vil ha, og velg "copy address". Gå deretter til din børs hvor pengene sendes fra og lim den inn der. Eller du kan gi adressen til en kunde som kan bruke den til å betale deg.

Når du bruker lommeboken for første gang, bør du motta et veldig lite beløp, øv på å bruke det til en annen adresse, enten innenfor lommeboken eller tilbake til børsen, for å bevise at lommeboken fungerer som forventet.

Når du har gjort det, må du sikkerhetskopiere ordene du skrev ned. En enkelt kopi er ikke nok. Ha minst to papirkopier (metall er bedre), og oppbevar dem på to forskjellige, godt sikrede steder. Dette reduserer risikoen for at en naturkatastrofe ødelegger din HWW og papirsikkerhetskopi i én hendelse. Se "Using Bitcoin Hardware Wallets" for en full diskusjon om dette.

## Sending

![image](assets/27.webp)

Når du gjør en betaling, må du lime inn adressen du betaler til i "Pay to"-feltet. Du kan faktisk ikke la etiketten være tom, den er bare for dine egne lommebøkers registreringer, men Sparrow tillater det ikke – bare skriv inn noe (bare du vil se det). Angi beløpet og du kan også manuelt justere gebyret du ønsker.

Lommeboken kan ikke signere transaksjonen med mindre HWW er tilkoblet. Det er jobben til HWW – å motta transaksjonen, signere den, og gi den tilbake, signert. Sørg for at når du signerer på enheten, visuelt inspiserer du at adressen du betaler til er den samme på enheten og på dataskjermen, og fakturaen du mottar (f.eks. du kan ha mottatt en e-post for å betale en bestemt adresse).

Vær også oppmerksom på at hvis du velger å bruke en mynt som er større enn betalingsbeløpet, vil resten bli sendt tilbake til en av dine lommebøkers vekseladresser. Noen mennesker har ikke kjent til dette, og sett opp transaksjonen sin på en offentlig blokkjede, og trodd at noen bitcoin ble sendt til en angripers adresse, men faktisk var det deres egen vekseladresse.
Firmware

For å oppdatere firmwaren, må du koble til Trezor Suite. Hvis du vil gjøre dette, sørg for at du har dine sikkerhetskopierte ord og passfrase tilgjengelig for å gjenopprette enheten, i tilfelle enheten nullstilles.
Konklusjon
Denne artikkelen viste deg hvordan du kan bruke en Trezor HWW på en tryggere og mer privat måte enn det som er annonsert – men denne artikkelen alene er ikke nok. Som jeg sa i starten, bør du kombinere den med informasjonen som er gitt i "Bruk av Bitcoin Hardware Wallets".

## Appendix A - Verifiser nedlastingen av programvaren

![bilde](assets/28 .webp)

Last ned Signaturen (en tekstfil) og Signeringsnøkkelen (en tekstfil) og noter filnavnene og hvor du lastet ned filen til.

Deretter, for Mac, må du laste ned GPG Suite (Se instruksjoner her).

For Windows, trenger du GPG4win (Se instruksjoner her).

For Linux, er GPG allerede en del av hver pakke. I tilfelle du ikke har det, få det med kommandoen: sudo apt-get install gpg

Deretter, for Mac/Windows eller Linux, åpne terminalen, og skriv inn kommandoen:

```bash
gpg –import XXXXXXXXXX
```

hvor XXXXXXXXXX er den fulle stien til signeringsnøkkelfilen (full sti betyr katalogen og filnavnet der filen er). Du bør se en bekreftelse på en vellykket nøkkelimport.

Deretter

```bash
gpg –verify ZZZZZZZZZZ WWWWWWWWWW
```

hvor ZZZZZZZZZZ er den fulle stien til signaturfilen og WWWWWWWWWW er den fulle stien til Trezor Suite-programmet som du lastet ned.

Du bør se en melding "Good signature from SatoshiLabs" et sted i utdataen. Det er en advarsel nederst som er trygg å ignorere.