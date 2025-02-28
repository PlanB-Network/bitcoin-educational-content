---
term: BIP35

---
Forslag som gjør det mulig for en Bitcoin-node å åpne opp informasjon om sin mempool, det vil si transaksjoner som venter på bekreftelse. På denne måten kan andre deltakere motta sanntidsdata om ubekreftede transaksjoner ved å sende en spesifikk melding til en node. Før BIP35 ble tatt i bruk, hadde nodene bare tilgang til informasjon om allerede bekreftede transaksjoner. Denne forbedringen gir SPV-lommebøker muligheten til å motta informasjon om ubekreftede transaksjoner, gjør det mulig for en gruvearbeider å unngå å gå glipp av transaksjoner med høye avgifter under en omstart, og gjør det enklere for eksterne tjenester å analysere mempool-informasjon.