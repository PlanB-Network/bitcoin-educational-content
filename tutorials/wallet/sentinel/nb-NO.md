---
name: Sentinel Watch-Only
description: Hva er en Watch-Only lommebok og hvordan bruke den?
---
![cover](assets/cover.webp)

---

***ADVARSEL:** Etter arrestasjonen av grunnleggerne av Samourai Wallet og beslagleggelsen av deres servere den 24. april, fortsetter Sentinel-appen å fungere, men **det er obligatorisk å bruke din egen Dojo** for å få tilgang til blockchain-informasjon og kringkaste transaksjoner.*

_Vi følger nøye med på utviklingen av denne saken samt utviklingen angående de tilknyttede verktøyene. Vær trygg på at vi vil oppdatere denne opplæringen når ny informasjon blir tilgjengelig._

_Denne opplæringen er gitt kun for utdannings- og informasjonsformål. Vi støtter eller oppmuntrer ikke bruk av disse verktøyene til kriminelle formål. Det er hver brukers ansvar å overholde lovene i sin jurisdiksjon_

---

*"Hold dine private nøkler, private."*

I denne artikkelen utforsker vi alt du trenger å vite om Watch-Only lommebøker. Vi diskuterer hvordan de fungerer og ser på de forskjellige applikasjonene som er tilgjengelige på markedet. Til slutt tilbyr vi en detaljert opplæring om en av de mest populære Watch-Only lommebokapplikasjonene: Sentinel.

## Hva er en Watch-Only Lommebok?
En Watch-Only lommebok, eller en skrivebeskyttet lommebok, er en type programvare designet for å tillate brukeren å observere transaksjoner knyttet til en eller flere spesifikke Bitcoin offentlige nøkler, uten å ha tilgang til de tilsvarende private nøklene.

Denne typen applikasjon beholder kun dataene som er nødvendige for å overvåke en Bitcoin lommebok, inkludert å se saldoen og transaksjonshistorikken, men den har ikke tilgang til de private nøklene. Derfor er det umulig å bruke bitcoins som holdes i lommeboken på Watch-Only applikasjonen.
![watch-only](assets/en/1.webp)
Watch-Only brukes generelt i forbindelse med en maskinvarelommebok. Dette tillater lagring av lommebokens private nøkler "kaldt," på en enhet som ikke er koblet til internett, som har en minimal angrepsflate, isolerer de private nøklene fra potensielt sårbare miljøer. Watch-Only applikasjonen, på den andre siden, lagrer utelukkende den utvidede offentlige nøkkelen (`xpub`, `zpub`, osv.) til Bitcoin lommeboken. Denne foreldrenøkkelen tillater ikke oppdagelsen av de tilknyttede private nøklene og, følgelig, tillater ikke bruk av bitcoins. Men, den tillater derivasjon av barn offentlige nøkler og mottaksadresser. Med kunnskap om adressene til lommeboken sikret av maskinvarelommeboken, kan Watch-Only applikasjonen spore disse transaksjonene på Bitcoin-nettverket, og tilby brukeren muligheten til å overvåke sin saldo og generere nye mottaksadresser, uten å måtte koble til sin maskinvarelommebok hver gang.

## Hvilken Watch-Only Lommebok skal man bruke?
For øyeblikket er den mest omfattende Watch-Only applikasjonen [Sentinel](https://sentinel.watch/), utviklet av teamene hos Samourai Wallet. Den omfatter alle de essensielle funksjonene for en god Watch-Only lommebok:
- Støtte for utvidede nøkler, offentlige nøkler, og adresser;
- Evnen til å organisere flere kontoer eller lommebøker i samlinger;
- Generering av adresser for å motta bitcoins på ens maskinvarelommebok uten å kreve dens direkte bruk;
- Evnen til å konstruere og kringkaste transaksjoner offline;
- Alternativ for å koble til ens egen Bitcoin-node;
- Integrering av Tor for forbedret personvern.
De unike ulempene med Sentinel ligger i det faktum at applikasjonen er eksklusivt tilgjengelig for Android og den støtter ikke multi-signatur lommebøker. Derfor, hvis du eier en Android-enhet og lommeboken din er en klassisk enkel signatur, anbefaler jeg Sentinel.
For de som ser etter å spore en multi-signatur lommebok, er Blue Wallet den eneste applikasjonen jeg kjenner til som tilbyr en Watch-Only modus for disse typer lommebøker, og den er tilgjengelig på både Android og iOS.
For iOS-brukere som ser etter et alternativ til Sentinel, kan [Green Wallet](https://blockstream.com/green/) eller [Blue Wallet](https://bluewallet.io/watch-only/) være alternativer, selv om deres funksjonalitet for kun-visning ikke er like omfattende som Sentinels. ![watch-only](assets/notext/2.webp)
## Hvordan bruke Sentinel Watch-Only Wallet?
### Installasjon og oppsett
Start med å installere Sentinel-applikasjonen. Dette kan du gjøre enten fra Google Play Store eller ved å bruke [APK-en som er tilgjengelig for nedlasting på det offisielle nettstedet](https://sentinel.watch/download/).

![watch-only](assets/notext/3.webp)

Når du først åpner applikasjonen, får du valget mellom:
- `Connect to Dojo`;
- `Connect to Samourai's server`.

Dojo, utviklet av Samourai-teamet, er en fullstendig Bitcoin node-versjon som kan installeres alene eller legges til med ett klikk i node-i-boks-løsninger som [Umbrel](https://umbrel.com/) og [RoninDojo](https://ronindojo.io/).

[**-> Oppdag hvordan du installerer RoninDojo v2 på en Raspberry Pi.**](https://planb.network/en/tutorials/node/ronin-dojo-v2)

Hvis du har din egen Dojo, kan du koble den til på dette stadiet. Ved å gjøre dette, vil du dra nytte av det høyeste nivået av personvern når du sjekker din Bitcoin nettverkstransaksjonsinformasjon.

![watch-only](assets/notext/4.webp)

Ellers er det mulig å velge Samourais standardserver. Du kan også velge om du vil koble til via Tor eller ikke.

![watch-only](assets/notext/5.webp)

Du vil deretter ankomme hovedsiden til Sentinel.

![watch-only](assets/notext/6.webp)

For å komme i gang, kan du sette opp applikasjonen. Klikk på de tre små prikkene i øvre høyre hjørne, deretter på `Settings`.

![watch-only](assets/notext/7.webp)
Ved å velge `User PIN code`, har du muligheten til å sette et passord for å sikre tilgangen til din kun-visning-lommebok. Du har også muligheten til å endre referansevalutaen for å konvertere saldoene dine til fiatvaluta, eller til og med skjule fiatverdier ved å aktivere `Hide fiat values`-alternativet. For økt sikkerhet kan du aktivere `Disable Screenshots`, som forhindrer alle skjermbilder av din Sentinel-applikasjon og dermed unngår enhver avsløring av informasjon på en ekstern skjerm.
![watch-only](assets/notext/8.webp)

I denne innstillingsmenyen har du også muligheten til å ta sikkerhetskopi av din Sentinel.

### Bruke Watch-Only Wallet
Fra hjemmesiden, trykk på den blå `NEW`-knappen for å legge til en ny utvidet offentlig nøkkel for å spore. Du har da muligheten til å skanne QR-koden til nøkkelen din, eller til å direkte lime inn nøkkelen (`xpub`, `zpub`...) ved å velge `Paste Pubkey`.

![watch-only](assets/notext/9.webp)

Generelt er `xpub` til lommeboken din direkte tilgjengelig via lommebokforvaltningsprogramvaren du bruker. For eksempel, hvis du forvalter din hardware-lommebok med Sparrow, finnes denne informasjonen i `Settings`-fanen, under `Keystore`-seksjonen.

![watch-only](assets/notext/10.webp)
Etter å ha lagt inn den utvidede offentlige nøkkelen i Sentinel, tilbyr applikasjonen deg å opprette en ny samling. En samling representerer et sett med utvidede offentlige nøkler organisert sammen. Denne muligheten gir deg ikke bare muligheten til å liste opp alle dine `xpubs`, men også til å klassifisere dem på en ordnet måte. For eksempel, hvis du har en Samourai Wallet med flere kontoer (innskudd, premix, postmix...), kan du samle alle disse kontoene under `Samourai`-samlingen. For lommebøker som administreres for din familie, kan du opprette en samling kalt `Familie`.

Velg `Opprett ny samling`. Deretter skriver du inn et navn for den utvidede nøkkelen du nettopp integrerte. For eksempel, hvis jeg skanner innskuddskontoen til min Samourai-lommebok, ville jeg navngi denne nøkkelen `Innskudd`. Klikk på `LAGRE` for å fullføre.

![watch-only](assets/notext/11.webp)

Deretter tildeler du et navn til denne samlingen og trykker på valideringsikonet som er plassert øverst til høyre på skjermen for å lagre samlingen. Din samling er nå synlig på Sentinel-hjemmeskjermen.

![watch-only](assets/notext/12.webp)

Hvis du ønsker å legge til en annen utvidet offentlig nøkkel, klikker du på `NY` igjen og skriver inn nøkkelen din.

![watch-only](assets/notext/13.webp)
Du vil da bli bedt om å velge samlingen du ønsker å integrere denne nøkkelen i, eller å opprette en ny. For eksempel, i mitt tilfelle, har jeg satt opp en samling spesielt for min Ledger-lommebok.
![watch-only](assets/notext/14.webp)

For å se de utvidede nøklene til en samling i detalj, klikker du bare på den. Du kan deretter navigere gjennom de forskjellige fanene for å se transaksjonshistorikken.

![watch-only](assets/notext/15.webp)

Fra en samling, ved å trykke på de tre små prikkene øverst til høyre, deretter på `Vis Ubrukte Utganger`, kan du få tilgang til en liste over UTXOer som holdes av den sporede lommeboken.

![watch-only](assets/notext/16.webp)

### Å sende og motta bitcoins fra Sentinel
Som med enhver god watch-only lommebok, lar Sentinel deg generere mottaksadresser for å motta bitcoins på den sporede lommeboken. Men Sentinel tilbyr også en annen avansert funksjon: opprettelsen og kringkastingen av en delvis signert Bitcoin-transaksjon (PSBT). Dermed kan lommeboken som holder de private nøklene signere denne transaksjonen, som, når den er signert, kan kringkastes på Bitcoin-nettverket av Sentinel. La oss se hvordan vi gjør alt dette.

**Forsiktighet, det anbefales ikke å motta bitcoins på en mottaksadresse som ikke er verifisert av lommeboken selv.** Hvis lommeboken som holder de private nøklene, som en maskinvarelommebok, ikke har bekreftet eksplisitt at en viss adresse er tilknyttet den, er det å sende bitcoins til denne adressen en risikabel praksis. Faktisk, uten denne bekreftelsen, er det ingen garanti for at adressen virkelig tilhører lommeboken din. Derfor bør mottaksfunksjonaliteten til en watch-only lommebok brukes med forsiktighet, med tanke på at de sendte midlene potensielt kan gå tapt.

For å motta bitcoins via Sentinel, velg samlingen av interesse, deretter klikker du på fanen som tilsvarer den utvidede offentlige nøkkelen mot hvilken du ønsker å overføre midler.

![watch-only](assets/notext/17.webp)

Til slutt, klikk på pilikonet nederst til venstre på skjermen. Sentinel genererer da en blank mottaksadresse for deg. Du kan kopiere den, eller skanne den ved hjelp av QR-koden.

![watch-only](assets/notext/18.webp)
For å generere en PSBT fra Sentinel, og dermed initiere en betalingstransaksjon, gå til den utvidede nøkkelen til lommeboken du ønsker å gjøre betalingen fra. La oss ta, for eksempel, min innskuddskonto på min Samourai-lommebok. Klikk deretter på pilikonet som er plassert nederst til høyre på skjermen.
![watch-only](assets/notext/19.webp)

Skriv inn alle parameterne relatert til transaksjonen din:
- Skriv inn mottakerens adresse (ved å klikke på QR-kodeikonet, har du muligheten til å skanne denne adressen);
- Spesifiser beløpet du vil sende til denne adressen;
- Bestem transaksjonsgebyrene.

Når du har fylt ut alle nødvendige felt for transaksjonen din, trykk på `COMPOSE UNSIGNED TRANSACTION`-knappen.

![watch-only](assets/notext/20.webp)

Du vil da få tilgang til PSBT-en, som representerer en konstruert, men usignert Bitcoin-transaksjon, siden Sentinel ikke har tilgang til dine private nøkler. Du har muligheten til å kopiere denne transaksjonen, eksportere den som en `.psbt`-fil, eller skanne den via den animerte QR-koden.

![watch-only](assets/notext/21.webp)

Gå deretter til lommeboken din som har de private nøklene for å signere transaksjonen (Samourai, maskinvarelommebok...).

![watch-only](assets/notext/22.webp)

Når transaksjonen er signert, kan du returnere til Sentinel for å kringkaste den. For å gjøre dette, fra hjemmemenyen, klikk på de tre små prikkene øverst til høyre, deretter på `Broadcast transaction`.

![watch-only](assets/notext/23.webp)

Du har muligheten til å angi din signerte PSBT på tre forskjellige måter:
- Ved å lime den direkte inn fra utklippstavlen din;
- Ved å importere den fra en `.psbt`-fil;
- Ved å skanne den via en QR-kode.

![watch-only](assets/notext/24.webp)

Når den signerte transaksjonen er angitt i det grå rammen, kan du klikke på den grønne `BROADCAST TRANSACTION`-knappen for å kringkaste den på Bitcoin-nettverket. Sentinel vil gi deg dens TXID.

![watch-only](assets/notext/25.webp)