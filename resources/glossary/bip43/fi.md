---
term: BIP43

---
Parannusehdotus, jossa otetaan käyttöön derivaatiopolun taso kuvaamaan käyttötarkoituskenttää HD-lompakoiden rakenteessa, joka otettiin käyttöön aiemmin BIP32:ssa. BIP43:n mukaan HD-lompakon ensimmäinen derivaatiotaso, heti pääavaimen jälkeen, jota merkitään "m/"-merkinnällä, on varattu tarkoituksen numerolle, joka ilmaisee loppupolulla käytettävän derivaatiostandardin. Tämä numero kirjataan karkaistuksi indeksiksi. Jos lompakko esimerkiksi noudattaa SegWit-standardia (BIP84), sen derivointipolun alku on seuraava: `m/84'/`. BIP43 mahdollistaa siis kunkin lompakko-ohjelmiston noudattamien standardien selventämisen, jotta niiden välinen yhteentoimivuus paranisi. Johdannaispolun loppuosan standardointi kuvataan BIP44:ssä.