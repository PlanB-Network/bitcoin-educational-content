---
term: MARKICE
---

Protokol koji omogućava integraciju formatiranih slikovnih podataka direktno na Bitcoin Blockchain putem sirovih transakcija sa višestrukim potpisom (P2MS). Stamps kodira binarni sadržaj slike u base 64 i dodaje ga ključevima 1/3 P2MS. Jedan ključ je pravi i koristi se za trošenje sredstava, dok su druga dva lažni ključevi (povezani privatni ključ je nepoznat) koji čuvaju podatke. Kodiranjem podataka direktno kao javnih ključeva umesto korišćenja `OP_RETURN` izlaza, slike sačuvane pomoću Stamps protokola su posebno radno intenzivne za čvorove. Ova metoda značajno stvara više UTXO-a, što povećava veličinu UTXO seta i predstavlja probleme za pune čvorove.