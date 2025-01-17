---
term: SWEEP TRANSACTION

---
Ketjuanalyysissä käytetty malli tai liiketoimintamalli, jolla määritetään liiketoimen luonne. Tälle mallille on ominaista yhden UTXO:n kulutus panoksena ja yhden UTXO:n tuotanto tuotoksena. Tämän mallin tulkinta on, että kyseessä on itsesiirto. Käyttäjä on siirtänyt bitcoininsa itselleen, toiseen omistamaansa osoitteeseen. Koska transaktiossa ei tapahdu mitään muutosta, on hyvin epätodennäköistä, että kyseessä on maksu. Maksua suoritettaessa on nimittäin lähes mahdotonta, että maksajalla on UTXO, joka vastaa täsmälleen myyjän vaatimaa summaa transaktiomaksujen lisäksi. Yleensä maksaja joutuu siksi tuottamaan muutostuloksen. Tällöin tiedämme, että kyseinen UTXO on todennäköisesti edelleen havaitun käyttäjän hallussa. Ketjuanalyysin yhteydessä, jos tiedämme, että transaktiossa syötteenä käytetty UTXO kuuluu Alicelle, voimme olettaa, että myös tuotoksena oleva UTXO kuuluu hänelle.

![](../../dictionnaire/assets/6.webp)

> ► *Ranskan kielessä "sweep transaction" voitaisiin kääntää "transaction de balayage".*