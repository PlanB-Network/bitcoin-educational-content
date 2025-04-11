---
term: TRANSAKSJONSGEBYRER

---
Transaksjonsavgifter er en sum som skal kompensere utvinnerne for deres deltakelse i proof of work-mekanismen. Disse avgiftene oppmuntrer utvinnere til å inkludere transaksjoner i blokkene de lager. De oppstår som følge av differansen mellom den totale mengden input og den totale mengden output i en transaksjon:

```text
fees = inputs - outputs
```

De uttrykkes i `sats/vBytes`, noe som betyr at avgiftene ikke avhenger av mengden bitcoins som sendes, men av transaksjonens vekt. De velges fritt av avsenderen av en transaksjon og bestemmer hvor raskt den inkluderes i en blokk gjennom en auksjonsmekanisme. La oss for eksempel si at jeg foretar en transaksjon med en input på 100 000 sats, en output på 40 000 sats og en annen output på 58 500 sats. Summen av utdataene er 98 500 sats. Avgiftene som er allokert til denne transaksjonen er 1 500 sats. Gruvearbeideren som inkluderer min transaksjon kan opprette 1 500 sats i sin coinbase-transaksjon i bytte mot de 1 500 satsene som jeg ikke fikk tilbake i mine utganger.

Transaksjoner med høyere gebyrer, i forhold til størrelsen, blir prioritert av utvinnerne, noe som kan fremskynde bekreftelsesprosessen. Omvendt kan transaksjoner med lavere gebyrer bli forsinket i perioder med høy overbelastning. Det er verdt å merke seg at Bitcoins transaksjonsgebyrer er forskjellige fra blokkbelønningen, som er et ekstra insentiv for utvinnere. Blokkbelønningen består av nye bitcoins som skapes for hver blokk som utvinnes (blokksubsidie), samt de innkrevde transaksjonsgebyrene. Mens blokksubsidien reduseres over tid på grunn av den totale forsyningsgrensen for bitcoins, vil transaksjonsgebyrene fortsette å spille en avgjørende rolle for å oppmuntre utvinnere til å delta.

På protokollnivå er det ingenting som hindrer brukere i å inkludere transaksjoner uten gebyrer i en blokk. I virkeligheten er denne typen gebyrfrie transaksjoner eksepsjonelle. Som standard videresender ikke Bitcoin-noder transaksjoner med gebyrer som er lavere enn `1 sat/vBytes`. Hvis noen gebyrfrie transaksjoner har passert, er det fordi de ble integrert direkte av den vinnende utvinneren, uten å gå gjennom nettverket av noder. Følgende transaksjon inkluderer for eksempel ingen gebyrer:

```text
fd456524104a6674693c29946543f8a0befccce5a352bda55ec8559fc630f5f3
```

I dette konkrete eksempelet var det en transaksjon initiert av direktøren for F2Pool-gruvebassenget. Som vanlig bruker er den nåværende nedre grensen derfor `1 sat/vBytes`.

Det er også nødvendig å ta hensyn til grensene for rensing. I perioder med høy overbelastning renser nodenes mempools sine ventende transaksjoner under en viss terskel, for å respektere deres tildelte RAM-grense. Denne grensen velges fritt av brukeren, men mange lar standardverdien til Bitcoin Core være 300 MB. Den kan endres i filen `bitcoin.conf` med parameteren `maxmempool`.

> på engelsk kaller vi det "transaction fees"