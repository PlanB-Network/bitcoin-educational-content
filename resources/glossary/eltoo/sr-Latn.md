---
term: ELTOO
---

Opšti protokol za druge slojeve Bitcoin koji definiše kako zajednički upravljati Ownership od UTXO. Eltoo su dizajnirali Christian Decker, Rusty Russell i Olaoluwa Osuntokun, posebno da reše probleme povezane sa mehanizmima pregovaranja stanja Lightning kanala, to jest, između otvaranja i zatvaranja. Arhitektura Eltoo pojednostavljuje proces pregovaranja uvođenjem linearnog sistema upravljanja stanjima, zamenjujući uspostavljeni pristup zasnovan na kaznama fleksibilnijom i manje kaznenom metodom ažuriranja. Ovaj protokol zahteva upotrebu nove vrste SigHash-a koja omogućava ignorisanje svih ulaza u potpisu transakcije. Ovaj SigHash je prvobitno nazvan `SIGHASH_NOINPUT`, zatim `SIGHASH_ANYPREVOUT` (*Any Previous Output*). Njegova implementacija je planirana u BIP118.


> ► *Eltoo se ponekad naziva i "LN-Symmetry".*