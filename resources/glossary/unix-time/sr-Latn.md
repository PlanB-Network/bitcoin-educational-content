---
term: UNIX VREME
---

Unix Time ili Unix Timestamp predstavlja broj sekundi koje su protekle od 1. januara 1970. godine, u ponoć po UTC vremenu (Unix Epoch). Ovaj sistem se koristi u Unix operativnim sistemima i njihovim izvedenicama za označavanje vremena na univerzalan i standardizovan način. Omogućava sinhronizaciju satova i upravljanje događajima zasnovanim na vremenu, bez obzira na vremenske zone.


U kontekstu Bitcoin, koristi se za lokalni sat čvorova, i stoga za izračunavanje NAT (Network-Adjusted Time). Mrežno prilagođeno vreme je medijana vremena čvorova izračunata lokalno od strane svakog čvora, i ova referenca se zatim koristi za verifikaciju validnosti vremenskih oznaka blokova. Zaista, da bi blok bio prihvaćen od strane čvora, njegov Timestamp mora biti između MTP (Median Time Past poslednjih 11 iskopanih blokova) i NAT plus 2 sata:


```text
MTP < Valid Timestamp < (NAT + 2h)
```


Unix Time se takođe koristi za uspostavljanje vremenskih zaključavanja kada su zasnovana na stvarnom vremenu, a ne na broju blokova.