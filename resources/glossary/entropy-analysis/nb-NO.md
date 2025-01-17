---
term: ENTROPI (ANALYSE)

---
I forbindelse med kjedeanalyse er entropi også navnet på en indikator, avledet fra Shannon-entropi, oppfunnet av LaurentMT. Denne indikatoren gjør det mulig å måle mangelen på kunnskap analytikere har om den nøyaktige konfigurasjonen av en Bitcoin-transaksjon. Med andre ord, jo høyere entropien til en transaksjon er, desto vanskeligere blir det for analytikere å identifisere bevegelsene av bitcoins mellom inn- og utganger.

I praksis avslører entropi om en transaksjon, sett fra en ekstern observatørs perspektiv, gir flere mulige tolkninger, utelukkende basert på mengden av inn- og utdata, uten å ta hensyn til andre eksterne eller interne mønstre og heuristikker. Høy entropi er da synonymt med bedre konfidensialitet for transaksjonen.

Entropi defineres som den binære logaritmen av antall mulige kombinasjoner. Her er formelen som brukes, der $E$ representerer entropien til transaksjonen og $C$ antall mulige tolkninger:

$$
E = \log_2(C)
$$

Når man tar hensyn til verdiene til UTXO-ene som er involvert i transaksjonen, representerer antall tolkninger $C$ antall måter input kan assosieres med output på. Med andre ord bestemmer det hvor mange tolkninger en transaksjon kan fremkalle sett fra en ekstern observatør som analyserer den.