---
term: Anchors.dat
definition: Bitcoin Core datoteka koja čuva IP adrese čvorova na koje je klijent bio povezan pre nego što je isključen, kako bi se olakšala ponovljena veza pri restartovanju.
---

Datoteka korišćena u Bitcoin Core klijentu za čuvanje IP adresa odlaznih čvorova na koje je klijent bio povezan pre nego što je isključen. Anchors.dat se stoga kreira svaki put kada se čvor zaustavi i briše kada se ponovo pokrene. Čvorovi čije su IP adrese sadržane u ovoj datoteci koriste se za brzo uspostavljanje veza kada se čvor ponovo pokrene.