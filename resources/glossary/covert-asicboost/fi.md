---
term: Covert ASICBoost

definition: Salainen versio AsicBoostista, joka muokkaa Merkle-puuta ja jonka SegWit teki tehottomaksi.
---
AsicBoostin salainen versio. AsicBoost on algoritminen optimointimenetelmä Bitcoin-louhintaa varten. Covert-versiossaan louhijat manipuloivat Merkle-puuta nonce-tiedon sijaan ja vähentävät siten kunkin SHA256-hajautuslaskennan vaatimia laskutoimituksia pitämällä osan tiedoista muuttumattomina hajautusyritysten välillä. Toisin kuin AsicBoostin Overt-versiossa, Covert-versiossa AsicBoostin käyttö salataan louhintaprosessin aikana. SegWitin ja sen toisen Merkle-puun käyttöönoton jälkeen tämä menetelmä on kuitenkin menettänyt tehoaan, koska sen käyttöön tarvittavien laskutoimitusten määrä on kasvanut liian suureksi verrattuna perinteiseen louhintaprosessiin.