---
term: BECH32 I BECH32M
---

`Bech32` i `Bech32m` su dva Address formata kodiranja za primanje bitkoina. Oni su zasnovani na blago modifikovanoj bazi 32. Uključuju kontrolni zbir zasnovan na algoritmu za ispravljanje grešaka zvanom BCH (*Bose-Chaudhuri-Hocquenghem*). U poređenju sa Legacy adresama, kodiranim u `Base58check`, `Bech32` i `Bech32m` adrese imaju efikasniji kontrolni zbir, što omogućava detekciju i potencijalno automatsko ispravljanje grešaka u kucanju. Njihov format takođe nudi bolju čitljivost, sa samo malim slovima. Ovde je matrica sabiranja za ovaj format iz baze 10:


| +   | 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0   | q   | p   | z   | r   | y   | 9   | x   | 8   |
| 8   | g   | f   | 2   | t   | v   | d   | w   | 0   |
| 16  | s   | 3   | j   | n   | 5   | 4   | k   | h   |
| 24  | c   | e   | 6   | m   | u   | a   | 7   | l   |

Bech32 i Bech32m su formati kodiranja koji se koriste za predstavljanje SegWit adresa. Bech32 je Address format kodiranja uveden BIP173 2017. godine. Koristi specifičan skup karaktera, sastavljen od brojeva i malih slova, kako bi se minimizirale greške pri kucanju i olakšalo čitanje. Bech32 adrese obično počinju sa `bc1` kako bi se naznačilo da su nativne za SegWit. Ovaj format se koristi samo na SegWit V0 adresama, sa skriptama P2WPKH (Plaćanje na Svedoka Javni Ključ Hash) i P2WSH (Plaćanje na Svedoka Skripta Hash). Međutim, postoji mali, neočekivani nedostatak specifičan za Bech32 format. Kad god je poslednji karakter Address `p`, dodavanje ili uklanjanje bilo kog broja `q` karaktera neposredno ispred njega ne poništava kontrolni zbir. Ovo ne utiče na postojeće upotrebe SegWit V0 adresa (BIP173) zbog njihove ograničenosti na dve definisane dužine. Međutim, ovo bi moglo uticati na buduće upotrebe Bech32 kodiranja. Bech32m format je jednostavno Bech32 format sa ispravljenom ovom greškom. Uveden je sa BIP350 2020. godine. Bech32m adrese takođe počinju sa `bc1`, ali su specifično dizajnirane da budu kompatibilne sa SegWit V1 (Taproot) i kasnijim verzijama, sa skriptom P2TR (Plaćanje na Taproot).