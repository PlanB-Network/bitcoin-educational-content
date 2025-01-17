---
term: ELTOO

---
En generell protokoll for Bitcoins andre lag som definerer hvordan man i fellesskap håndterer eierskapet til en UTXO. Eltoo ble utviklet av Christian Decker, Rusty Russell og Olaoluwa Osuntokun, spesielt for å løse problemene knyttet til forhandlingsmekanismene for Lightning-kanaltilstander, det vil si mellom åpning og lukking. Eltoo-arkitekturen forenkler forhandlingsprosessen ved å innføre et lineært tilstandsstyringssystem som erstatter den etablerte straffebaserte tilnærmingen med en mer fleksibel og mindre straffende oppdateringsmetode. Denne protokollen krever bruk av en ny type SigHash som gjør det mulig å ignorere alle inndata i signaturen til en transaksjon. Denne SigHash-typen ble opprinnelig kalt `SIGHASH_NOINPUT`, deretter `SIGHASH_ANYPREVOUT` (*Any Previous Output*). Implementeringen er planlagt i BIP118.

> ► *Eltoo blir noen ganger også omtalt som "LN-symmetri"