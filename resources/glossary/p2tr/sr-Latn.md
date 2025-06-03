---
term: P2TR
---

P2TR označava *Pay to Taproot*, što je standardni model skripte koji se koristi za uspostavljanje uslova trošenja na UTXO (nepotrošeni izlaz transakcije). Uveden je implementacijom Taproot u novembru 2021. P2TR koristi Schnorr protokol za agregaciju kriptografskih ključeva, kao i Merkle stabla za alternativne skripte, poznate kao MAST (*Merkelized Alternative Script Tree*). Za razliku od tradicionalnih transakcija gde su uslovi trošenja javno izloženi (ponekad u trenutku primanja, ponekad u trenutku trošenja), P2TR omogućava skrivanje složenih skripti iza jednog očiglednog javnog ključa.


Tehnički, P2TR skripta zaključava bitkoine na jedinstvenom Schnorr javnom ključu, označenom kao $K$. Međutim, ovaj ključ $K$ je zapravo agregat javnog ključa $P$ i javnog ključa $M$, pri čemu se potonji izračunava iz Merkle Root liste `scriptPubKey`. Bitkoini zaključani sa P2TR skriptom mogu se potrošiti na dva različita načina: ili objavljivanjem potpisa za javni ključ $P$, ili ispunjavanjem jedne od skripti sadržanih u Merkle Tree. Prva opcija se naziva "*key path*" a druga "*script path*".


Dakle, P2TR omogućava korisnicima da šalju bitkoine ili na javni ključ ili na više skripti po njihovom izboru. Još jedna prednost ove skripte je ta što, iako postoji više načina za trošenje P2TR izlaza, samo onaj koji se koristi treba da bude otkriven u trenutku trošenja, omogućavajući da neiskorišćene alternative ostanu privatne. P2TR je verzija 1 SegWit izlaza, što znači da su potpisi za P2TR ulaze smešteni u svedoku transakcije, a ne u `scriptSig`. P2TR adrese koriste `Bech32m` kodiranje i počinju sa `bc1p`.