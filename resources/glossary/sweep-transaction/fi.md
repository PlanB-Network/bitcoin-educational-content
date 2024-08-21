---
termi: SWEEP TRANSACTION
---

Malli tai transaktiomalli, jota käytetään ketjuanalyysissä transaktion luonteen määrittämiseen. Tämä malli on tunnusomaista yhden UTXO:n kuluttamiselle syötteenä ja yhden UTXO:n tuottamiselle tulosteena. Tämän mallin tulkinta on, että kyseessä on itse siirto. Käyttäjä on siirtänyt bitcoinejaan itselleen, toiseen omistamaansa osoitteeseen. Koska transaktiossa ei ole vaihtorahaa, on hyvin epätodennäköistä, että kyseessä olisi maksu. Todellakin, kun maksu suoritetaan, on lähes mahdotonta, että maksajalla olisi UTXO, joka täsmälleen vastaa myyjän vaatimaa summaa, lisäksi transaktiomaksuja. Yleensä maksajan on siis pakko tuottaa vaihtorahan ulostulo. Tällöin tiedämme, että havaittu käyttäjä todennäköisesti edelleen omistaa tämän UTXO:n. Ketjuanalyysin kontekstissa, jos tiedämme, että transaktion syötteenä käytetty UTXO kuuluu Alicelle, voimme olettaa, että myös tulosteena oleva UTXO kuuluu hänelle.

![](../../dictionnaire/assets/6.png)

> ► *Ranskaksi "sweep transaction" voidaan kääntää "transaction de balayage"ksi.*