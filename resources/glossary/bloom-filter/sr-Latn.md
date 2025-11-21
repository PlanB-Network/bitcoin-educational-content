---
term: BLOOM FILTER
---

Probabilistička struktura podataka koja se koristi za testiranje da li je element deo skupa. Bloom filteri omogućavaju brze provere članstva bez testiranja celog skupa podataka. Posebno su korisni u kontekstima gde su prostor i brzina kritični, ali je prihvatljiva niska i kontrolisana stopa greške. Naime, Bloom filteri ne proizvode lažne negativne rezultate, ali proizvode određeni broj lažno pozitivnih rezultata. Kada se element doda u filter, više funkcija raspršivanja određuje pozicije u nizu bitova. Za proveru članstva koriste se iste funkcije raspršivanja. Ako su svi odgovarajući bitovi postavljeni, element je verovatno u skupu, ali uz rizik od lažno pozitivnih rezultata. Bloom filteri su široko korišćeni u oblastima baza podataka i mreža. Poznato je da ih Google koristi za svoj komprimovani sistem upravljanja bazama podataka *BigTable*. U Bitcoin protokolu, koriste se posebno za SPV novčanike prema BIP37.


> ► *Kada se posebno govori o upotrebi Bloom filtera u kontekstu Bitcoin transakcija, termin "Transaction Bloom Filtering" se ponekad sreće.*