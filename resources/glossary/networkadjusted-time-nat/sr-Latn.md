---
term: MREŽNO-PRILAGOĐENO VREME (NAT)
---

Procena univerzalnog vremena uspostavljena na satovima mrežnih čvorova. Svaki čvor izračunava svoj NAT uzimajući medijanu vremenskih razlika između svog lokalnog sata (UTC) i onih čvorova na koje je povezan, zatim dodaje svoj lokalni sat medijani ovih razlika, do maksimalno 70 minuta. Mrežno prilagođeno vreme je stoga medijana vremena čvorova izračunata lokalno od strane svakog čvora. Ovaj referentni okvir se zatim koristi za verifikaciju validnosti vremenskih oznaka blokova. Naime, da bi blok bio prihvaćen od strane čvora, njegov Timestamp mora biti između MTP (medijana vremena poslednjih 11 iskopanih blokova) i NAT plus 2 sata:


```text
MTP < Valid Timestamp < (NAT + 2h)
```