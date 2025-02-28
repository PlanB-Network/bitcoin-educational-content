---
term: (0X03)

---
SigHash-tyyppi Merkki, jota käytetään Bitcoin-tapahtuman allekirjoituksissa ilmaisemaan, että allekirjoitus koskee kaikkia tapahtuman syötteitä ja vain yhtä tulostetta, joka vastaa saman syötteen indeksiä, joka on allekirjoitettu. Näin ollen jokainen `SIGHASH_SINGLE`-merkinnällä allekirjoitettu tulo liittyy nimenomaan tiettyyn lähtöön. Allekirjoitus ei sido muita ulostuloja, joten niitä voidaan muuttaa myöhemmin. Tämäntyyppinen allekirjoitus on hyödyllinen monimutkaisissa transaktioissa, joissa osallistujat haluavat yhdistää tietyt syötteet tiettyihin tuotoksiin ja jättää samalla joustavuutta muille transaktion tuotoksille.