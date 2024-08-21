---
termi: BIP43
---

Ehdotus parannukseksi, joka esittelee johdannaispolun tason käytön kuvaamaan tarkoituskenttää HD-lompakoiden rakenteessa, joka esiteltiin aiemmin BIP32:ssa. BIP43:n mukaan HD-lompakon ensimmäinen johdannaispolun taso, heti pääavaimen `m/` jälkeen, on varattu tarkoitusnumeron käyttöön, joka osoittaa loppupolun käyttämän johdannaisstandardin. Tämä numero kirjataan kovetetuna indeksinä. Esimerkiksi, jos lompakko noudattaa SegWit-standardia (BIP84), sen johdannaispolun alku olisi: `m/84'/`. BIP43 mahdollistaa siis kunkin lompakko-ohjelmiston noudattamien standardien selventämisen, jotta niiden välillä olisi parempi yhteentoimivuus. Loppupolun standardisoinnin kuvaus löytyy BIP44:stä.