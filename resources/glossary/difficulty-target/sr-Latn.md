---
term: CILJ TEŽINE
---

Faktor težine, takođe poznat kao cilj težine, je parametar koji se koristi u mehanizmu konsenzusa od strane Proof of Work (Proof of Work, PoW) na Bitcoin. Cilj predstavlja numeričku vrednost koja određuje težinu za rudare da reše specifičan kriptografski problem, nazvan Proof of Work, prilikom kreiranja novog bloka na Blockchain.


Ciljna težina je prilagodljiv 256-bitni (64 bajta) broj koji određuje granicu prihvatljivosti za heširanje zaglavlja blokova. Drugim rečima, da bi blok bio važeći, Hash njegovog zaglavlja sa `SHA256d` (dvostruki `SHA256`) mora biti numerički manji ili jednak cilju težine. Proof of Work se sastoji od modifikacije polja `Nonce` zaglavlja bloka ili Coinbase Transaction dok rezultujući Hash ne bude manji od ciljne vrednosti.


Ova meta se prilagođava svakih 2016 blokova (otprilike svake dve nedelje), tokom događaja nazvanog "prilagođavanje." Faktor težine se ponovo izračunava na osnovu vremena potrebnog za rudarenje prethodnih 2016 blokova. Ako je ukupno vreme manje od dve nedelje, težina se povećava prilagođavanjem mete naniže. Ako je ukupno vreme više od dve nedelje, težina se smanjuje prilagođavanjem mete naviše. Cilj je održavanje prosečnog Mining vremena od 10 minuta po bloku. Ovo vreme između svakog bloka pomaže u sprečavanju podela Bitcoin mreže, što bi rezultiralo rasipanjem računarske snage. Meta težine se nalazi u svakom zaglavlju bloka, unutar polja `nBits`. Pošto je ovo polje smanjeno na 32 bita, a meta je zapravo 256 bita, meta je sabijena u manje precizan naučni format.


![](../../dictionnaire/assets/34.webp)


> ► *Ciljni nivo težine se ponekad naziva i "faktor težine." Po analogiji, može se označiti njegovim kodiranjem u zaglavljima blokova terminom "nBits."*