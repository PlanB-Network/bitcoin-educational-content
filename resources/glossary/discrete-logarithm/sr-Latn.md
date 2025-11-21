---
term: DISKRETNI LOGARITAM
---

Diskretni logaritam je matematički problem koji se koristi u nekim kriptografskim algoritmima sa javnim ključem. U cikličkoj grupi reda $q$, sa generatorom $g$, ako imamo jednačinu oblika $g^x = h$, tada je $x$ diskretni logaritam od $h$ u odnosu na bazu $g$, modulo $q$. Jednostavno rečeno, to uključuje određivanje eksponenta $x$ kada su $g$, $h$ i $q$ poznati. Diskretni logaritam je, dakle, inverzija eksponencijacije u konačnoj cikličnoj grupi. Međutim, za velike vrednosti $q$, rešavanje problema diskretnog logaritma se smatra algoritamski teškim. Ovo svojstvo se koristi za obezbeđivanje sigurnosti mnogih kriptografskih protokola, kao što je Diffie-Hellman protokol za ključ Exchange.


Diskretni logaritam se takođe koristi u kriptografiji eliptičkih krivih (ECC), uključujući u ECDSA (*Elliptic Curve Digital Signature Algorithm*). U kontekstu eliptičkih krivih, problem diskretnog logaritma se proširuje na pronalaženje skalara $k$ takvog da je $k \cdot G = K$, gde su $G$ i $K$ tačke na krivoj, a $\cdot$ predstavlja operaciju množenja tačke. U kontekstu Bitcoin, skripte mogu koristiti ili ECDSA ili Schnorr protokol za zaključavanje UTXO-a. Obe se oslanjaju na neizvodljivost izračunavanja diskretnog logaritma.