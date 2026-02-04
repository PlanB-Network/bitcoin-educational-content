---
term: BIP0145
definition: Ažuriranje JSON-RPC poziva getblocktemplate radi integracije SegWit podrške i izračunavanja težine transakcija.
---

Ažurira JSON-RPC poziv `getblocktemplate` kako bi uključio podršku za SegWit, u skladu sa BIP141. Ovo ažuriranje omogućava rudarima da konstruiraju blokove uzimajući u obzir novu "težinu" merenja transakcija i blokova uvedenu od strane SegWit, kao i druge parametre kao što je izračunavanje limita sigops.