---
term: Wallet FOOTPRINT
---

Skup karakteristika koje se mogu primetiti u transakcijama napravljenim od strane istog Bitcoin Wallet. Ove karakteristike mogu uključivati sličnosti u korišćenju tipova skripti, ponovnu upotrebu adresa, redosled UTXO-a, postavljanje izlaza za kusur, signalizaciju RBF (*Replace-by-fee*), broj verzije, polje `nSequence` i polje `nLockTime`.


Otisci Wallet koriste se od strane analitičara za praćenje aktivnosti određenog entiteta na Blockchain identifikovanjem ponavljajućih obrazaca u njegovim transakcijama. Na primer, korisnik koji sistematski šalje svoj kusur na P2TR adrese (`bc1p…`) stvara prepoznatljiv otisak koji se može koristiti za praćenje njihovih budućih transakcija.


Kao što LaurentMT objašnjava u Space Kek #19 (podcast na francuskom jeziku), korisnost Wallet otisaka u analizi lanca značajno se povećava tokom vremena. Naime, rastući broj tipova skripti i sve postepenije uvođenje ovih novih funkcija od strane Wallet softvera naglašavaju razlike. Čak je moguće tačno identifikovati softver koji koristi praćeni entitet. Stoga je važno razumeti da je proučavanje otiska Wallet posebno relevantno za nedavne transakcije, više nego za one započete početkom 2010-ih.