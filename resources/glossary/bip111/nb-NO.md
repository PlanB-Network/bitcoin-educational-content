---
term: BIP111

---
Foreslår å legge til en tjenestebit kalt `NODE_BLOOM` for å tillate noder å eksplisitt signalisere sin støtte for Bloom-filtre som beskrevet i BIP37. Innføringen av `NODE_BLOOM` gjør det mulig for nodeoperatører å deaktivere denne tjenesten for å redusere risikoen for DoS. BIP37-alternativet er deaktivert som standard i Bitcoin Core. For å aktivere den må parameteren `peerbloomfilters=1` legges inn i konfigurasjonsfilen.