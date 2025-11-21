---
term: POLITIKA (MINISCRIPT)
---

Jezik visokog nivoa, usmeren ka korisniku, koji omogućava jednostavno određivanje uslova pod kojima se UTXO može otključati u okviru Miniscript-a. Politika je apstraktni opis pravila trošenja. Ona se zatim može kompajlirati u miniscript, koji je jedan-na-jedan ekvivalent sa operacijama iz izvornog skriptnog jezika Bitcoin.


![](../../dictionnaire/assets/30.webp)


Jezik politike je malo drugačiji od jezika miniscripta. Na primer, zamislite sigurnosni sistem sa primarnim putem koji je ključ A, i rezervnim putem koji je ključ B, ali pod vremenskom blokadom od jedne godine (približno 52,560 blokova). U politici, ovo bi bilo:


```plaintext
or(pk(A),and(pk(B),older(52560)))
```


Jednom kompajliran u miniscript, to bi bilo:


```plaintext
andor(pk(B),older(52560),pk(A))
```


A kada se jednom konvertuje u izvorno pismo, to bi bilo:


```plaintext
<B>
OP_CHECKSIG
OP_NOTIF
<A>
OP_CHECKSIG
OP_ELSE
<50cd00>
OP_CHECKSEQUENCEVERIFY
OP_ENDIF
```