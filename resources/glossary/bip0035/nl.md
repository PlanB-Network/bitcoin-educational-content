---
term: BIP0035
---

Voorstel waarmee een Bitcoin knooppunt informatie over zijn Mempool kan ontsluiten, d.w.z. de transacties die wachten op bevestiging. Hierdoor kunnen andere deelnemers real-time gegevens over onbevestigde transacties ontvangen door een specifiek bericht naar een knooppunt te sturen. Voor de invoering van BIP35 hadden nodes alleen toegang tot informatie over reeds bevestigde transacties. Deze verbetering biedt SPV wallets de mogelijkheid om informatie over onbevestigde transacties te ontvangen, stelt een Miner in staat om te voorkomen dat er tijdens een herstart transacties met hoge vergoedingen gemist worden en vergemakkelijkt de analyse van Mempool informatie door externe diensten.