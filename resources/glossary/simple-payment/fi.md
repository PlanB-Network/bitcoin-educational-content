---
term: Yksinkertainen maksu

definition: Tapahtumamalli, jossa on kaksi ulostuloa, yleensä maksu ja vaihtoraha.
---
Ketjuanalyysissä käytetty transaktiomalli (tai -malli), jolle on ominaista yhden tai useamman UTXO:n kulutus tuotantopanoksina ja kahden UTXO:n tuotanto tuotoksina. Tämä malli näyttää siis seuraavalta:



Tämä yksinkertainen maksumalli osoittaa, että kyseessä on todennäköisesti lähetys- tai maksutapahtuma. Käyttäjä on kuluttanut oman UTXO:nsa syötteinä tyydyttääkseen maksun UTXO:n ja muutoksen UTXO:n (samalle käyttäjälle palautettu muutos). Tiedämme siis, että havaittu käyttäjä ei todennäköisesti enää omista toista kahdesta UTXO:sta (maksun UTXO), mutta toinen UTXO (muutoksen UTXO) on edelleen hänen hallussaan.