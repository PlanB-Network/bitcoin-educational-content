---
term: Taproot
---

Veliko ažuriranje Bitcoin protokola, usvojeno kroz Soft Fork u novembru 2021. Ovo ažuriranje donosi značajna poboljšanja u pogledu privatnosti, efikasnosti i fleksibilnosti implementacijom BIP340, BIP341 i BIP342. Ovo ažuriranje je zaključano na bloku 687,284 12. juna 2021, kada je 90% blokova generisanih tokom perioda signaliziralo u korist, čime je naznačena spremnost rudara da aktiviraju ažuriranje (*Speedy Trial*). Aktivacija se konačno dogodila na bloku 709,632 14. novembra 2021, skoro četiri godine nakon početnih diskusija o toj temi između Pietera Wuillea, Andrewa Poelstre i Gregoryja Maxwella. Bio je to prvi pokušaj velikog ažuriranja od sporne aktivacije SegWit 2017. godine.


Taproot je takođe naziv za BIP341, implementiran unutar Soft Fork istog imena, koji uvodi novi model skripte nazvan P2TR. Skripta P2TR zaključava bitkoine na jedinstveni Schnorr javni ključ, označen kao $K$. Međutim, ovaj ključ $K$ je zapravo agregat javnog ključa $P$ i javnog ključa $M$, pri čemu se potonji izračunava iz Merkle Root liste `scriptPubKey`. Bitkoini zaključani sa skriptom P2TR mogu se potrošiti na dva različita načina: ili objavljivanjem potpisa za javni ključ $P$, ili ispunjavanjem jedne od skripti sadržanih u Merkle Tree. Prva opcija se naziva "*key path*" a druga "*script path*".