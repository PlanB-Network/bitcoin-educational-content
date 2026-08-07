---
name: Oppdatering av BTCPay Server
description: Installer en sikkerhetsoppdatering på din BTCPay Server-instans og roter legitimasjonen som betyr noe
---

![cover](assets/cover.webp)

Å drive din egen betalingsprosessor betyr at du også er ditt eget sikkerhetsteam. Når vedlikeholderne av BTCPay Server publiserer en sikkerhetsutgivelse, er det ingen som patcher instansen din for deg: oppdateringen, verifiseringen og legitimasjonsrotasjonen som følger, er opp til deg å utføre.

Denne veiledningen går gjennom hele prosedyren, uansett hvordan du har satt opp BTCPay Server: sjekk hvilken versjon som kjører, installer oppdateringen for din type oppsett, verifiser at den faktisk ble installert, og roter hemmelighetene en angriper kan ha fanget opp mens instansen din var sårbar.

Hvis du ikke har satt opp BTCPay Server ennå, start med installasjonsveiledningen:

https://planb.academy/tutorials/business/point-of-sale/btcpay-server-928eb01e-824b-4b57-a3e8-8727633beddc

## Den kritiske sårbarheten i august 2026

⚠️ **Kritisk sikkerhetsvarsel (7. august 2026):** en kritisk sårbarhet som påvirker BTCPay Server blir aktivt utnyttet og kan føre til tap av midler. Oppdater instansen din til **versjon 2.4.2** umiddelbart via `Admin Dashboard > Server > Maintenance > Update`, og sjekk deretter at bunnteksten viser `2.4.2`. Hvis du ikke kan oppdatere med en gang, må du slå av BTCPay Server. Når du har oppdatert, må du også fullstendig fornye makaronene dine og `macaroons.db`-filen din, fullstendig fornye autentiseringsstrengene til enhver annen Lightning-backend, og, hvis du genererte en varm on-chain-lommebok inne i BTCPay Server, flytte disse midlene og lage lommeboken på nytt. Integratører bør også oppdatere NBXplorer til versjon 2.6.10. Kilde: [BTCPay Server 2.4.2 release notes](https://github.com/btcpayserver/btcpayserver/releases/tag/v2.4.2).

Versjon 2.4.2 ble publisert 7. august 2026. Utgivelsesnotatene sier at den retter en kritisk sårbarhet som allerede ble utnyttet i praksis, rapportert av `brunoerg` og `benthecarman` gjennom Bitcoin Red Team-initiativet. Samme utgivelse retter også en omgåelse av TOTP-tofaktorautentisering via Greenfield Basic-autentisering, og deaktiverer Greenfield Basic-autentisering som standard fem minutter etter at kontoen er opprettet.

To konsekvenser følger av "aktivt utnyttet":

- **Oppdatering er ikke valgfritt, og ikke noe du kan planlegge til neste uke.** En upatchet instans som er tilgjengelig fra internett, må enten oppdateres eller slås av.
- **Oppdatering er ikke nok alene.** Hvis instansen din ble kompromittert før du patchet, kan angriperen allerede ha kopier av Lightning-legitimasjonen din og av eventuelt nøkkelmateriale for varme lommebøker som BTCPay Server genererte for deg. Disse hemmelighetene forblir gyldige etter oppdateringen inntil du roterer dem. Rotasjonsdelen nedenfor er den delen folk hopper over, og det er den delen som faktisk beskytter midlene dine.

## Steg 1 — Finn ut hvilken versjon du kjører

Logg inn på BTCPay Server og se på **bunnteksten på hvilken som helst side**: versjonsstrengen vises der. Du kan også åpne `Admin Dashboard > Server > Maintenance`, som viser gjeldende versjon og oppdateringskontrollene.

Hvis instansen din eksponerer Greenfield API-et, returnerer `GET /api/v1/server/info` også versjonen.

Alt under `2.4.2` er sårbart.

## Steg 2 — Oppdater

### Selvhostet Docker-oppsett (standardinstallasjonen)

Dette dekker den offisielle Docker-installasjonen, som er det du får fra BTCPay Server-dokumentasjonen, fra LunaNodes engangs-launcher, og fra de fleste VPS-installasjoner.

Den enkleste veien er webgrensesnittet:

1. Gå til `Admin Dashboard > Server > Maintenance`.
2. Klikk **Update**.
3. Vent til containerne blir hentet og startet på nytt. Grensesnittet vil være utilgjengelig i noen minutter.

Hvis webgrensesnittet er utilgjengelig, eller du foretrekker å se loggene, gjør det over SSH:

```bash
sudo su -
cd "$BTCPAY_BASE_DIRECTORY/btcpayserver-docker"
. ./btcpay-update.sh
```

På en standardinstallasjon er `$BTCPAY_BASE_DIRECTORY` lik `/root`, så mappen er `/root/btcpayserver-docker`. Skriptet henter de nyeste bildene, gjenoppretter containerne, og skriver ut de resulterende versjonene.

Docker-oppsettet leverer NBXplorer sammen med BTCPay Server, så en standardoppdatering bringer også NBXplorer til den anbefalte versjonen `2.6.10`. Hvis du kjører NBXplorer separat — typisk for integratører og egendefinerte oppsett — oppdater den eksplisitt.

### Umbrel

Åpne Umbrel-dashbordet, gå til **App Store**, finn BTCPay Server og installer oppdateringen hvis en er tilgjengelig.

⚠️ **Viktig:** app-store-pakker blir ompakket av Umbrel-teamet og kan ligge timer eller dager bak oppstrøms. Sjekk versjonen i BTCPay Server-bunnteksten etter oppdatering. Hvis den fortsatt er under `2.4.2`, **stopp appen** fra Umbrel-dashbordet og vent på den pakkede utgivelsen i stedet for å la en sårbar instans kjøre.

Den dedikerte Umbrel-veiledningen dekker selve appen:

https://planb.academy/tutorials/business/point-of-sale/btcpay-server-umbrel-68e1c535-4322-4507-a69c-9dfcbc36dfd1

### Start9 / StartOS

Samme logikk: oppdater BTCPay Server fra StartOS-markedsplassen, og verifiser deretter versjonen i bunnteksten. Hvis den pakkede versjonen ikke enda er `2.4.2`, stopp tjenesten inntil den er det.

### Administrert og tredjeparts hosting

Hvis noen andre drifter instansen din (en hostingleverandør, en forening, en venns server), trenger du fortsatt bekreftelsen. Be operatøren om versjonsstrengen som vises i bunnteksten, og spør eksplisitt om legitimasjonsrotasjonen beskrevet nedenfor er blitt utført etter oppdateringen. "Vi oppdaterte" er ikke det samme svaret som "vi roterte makaronene dine".

## Steg 3 — Verifiser at oppdateringen faktisk ble installert

Last inn BTCPay Server-grensesnittet på nytt og les versjonen i bunnteksten. Den må vise `2.4.2` eller høyere.

Ikke stol på at oppdateringskommandoen avsluttes uten feil: på maskiner med begrensede ressurser kan et bildeuttrekk feile stille og la den forrige containeren fortsette å kjøre. Les versjonen, hver gang.

## Steg 4 — Roter legitimasjonen din

Dette er steget som gjør "patchet" til "trygt". Fordi sårbarheten ble utnyttet før rettelsen ble sendt ut, må du behandle hver hemmelighet instansen din hadde som potensielt kjent for en angriper.

### Lightning: LND

Regenerer makaronene **og** `macaroons.db`-filen. Å bare slette makaron-filene er ikke nok — LND utleder makaroner fra rotnøkkelen lagret i `macaroons.db`, så en angriper som har en kopi av en gammel makaron beholder tilgang inntil den databasen gjenopprettes.

Prosedyren er: stopp LND, fjern `macaroons.db` og `*.macaroon`-filene fra nettverksmappen (for mainnet, `data/chain/bitcoin/mainnet/` inne i LND-datamappen), og start deretter LND på nytt og lås den opp, som gjenoppretter dem. Ta sikkerhetskopi av mappen først, og par på nytt alle applikasjoner som brukte de gamle makaronene — BTCPay Server selv, Zeus, Thunderhub, RTL, Alby, og ethvert skript du har skrevet.

Hvis du også eksponerer LND over internett, gå gjennom TLS-sertifikatet og eventuell `lnd.conf`-legitimasjon samtidig.

### Lightning: andre backender

Alt som autentiserer seg mot noden din med en streng, må få en ny streng:

- **Core Lightning**: regenerer runen eller tilgangslegitimasjonen som brukes av tilkoblingen.
- **Phoenixd**: roter HTTP-passordet.
- **LNbits og lignende**: opphev og reutsted admin- og fakturanøklene.
- **Fjernnode-tilkoblingsstrenger** lagret i BTCPay Servers butikkinnstillinger: skriv dem på nytt med de nye hemmelighetene.

### Varm on-chain-lommebok generert inne i BTCPay Server

Hvis du lot BTCPay Server generere en on-chain-lommebok for deg — i motsetning til å koble til en hardware-lommebok eller importere en xpub hvis nøkler aldri berørte serveren — levde det frøet på maskinen.

Regn den som forbrent:

1. Opprett en ny lommebok, ideelt sett med en hardware-lommebok slik at nøklene aldri ligger på serveren igjen.
2. Fei midlene fra den gamle lommeboken over til den nye.
3. Erstatt utledningsskjemaet i butikkinnstillingene med den nye lommeboken.
4. Bruk aldri det gamle frøet på nytt.

Kun-observasjon-oppsett (xpub eller hardware-lommebok) trenger ikke dette: de private nøklene lå aldri på serveren. Dette er nettopp hvorfor installasjonsveiledningen anbefaler dem.

### BTCPay Server-kontoer og API-nøkler

Mens du holder på:

- Endre passordene til alle brukerkontoer på instansen.
- Opphev og reutsted alle Greenfield **API-nøkler**.
- Meld deg på tofaktorautentisering på nytt, gitt at 2.4.2 retter en 2FA-omgåelse.
- Åpne `Admin Dashboard > Server > Users` og sjekk at det ikke finnes uventede kontoer.
- Gå gjennom nylige **utbetalinger**, **pull payments** og **refusjoner** for oppføringer du ikke selv opprettet.
- Gå gjennom webhookene dine og hemmelighetene deres.

## Steg 5 — Hold deg informert til neste gang

Sikkerhetsutgivelser hjelper bare de operatørene som får høre om dem:

- Følg med på [BTCPay Server-utgivelsene på GitHub](https://github.com/btcpayserver/btcpayserver/releases) — GitHub kan sende deg e-post ved hver ny utgivelse av et repository.
- Følg prosjektets kunngjøringskanaler og [den offisielle bloggen](https://blog.btcpayserver.org/).
- Hold instansen din på en versjon du raskt kan oppdatere: jo lenger bak du henger, jo mer smertefull blir en akutt oppdatering.

Selvhosting gir deg suverenitet over betalingene dine. Prisen for den suvereniteten er nettopp dette: å lese utgivelsesnotater og være den som patcher.
