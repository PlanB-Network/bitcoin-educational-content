---
term: BELEID (MINISCRIPT)
---

Een gebruikersgeoriënteerde taal op hoog niveau waarmee eenvoudig de voorwaarden kunnen worden gespecificeerd waaronder een UTXO kan worden ontgrendeld binnen het kader van Miniscript. Het beleid is een abstracte beschrijving van de bestedingsregels. Het kan dan worden gecompileerd in miniscript, wat een één-op-één equivalent is met operaties uit Bitcoin's eigen scripttaal.


![](../../dictionnaire/assets/30.webp)


De beleidstaal is iets anders dan de miniscripttaal. Stel je bijvoorbeeld een beveiligingssysteem voor met een primair pad dat sleutel A is en een herstelpad dat sleutel B is, maar met een tijdslot van één jaar (ongeveer 52.560 blokken). In beleid zou dit zijn:


```plaintext
or(pk(A),and(pk(B),older(52560)))
```


Eenmaal gecompileerd in miniscript, zou het dat zijn:


```plaintext
andor(pk(B),older(52560),pk(A))
```


En zodra het is omgezet in oorspronkelijk script, zou het dat ook zijn:


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