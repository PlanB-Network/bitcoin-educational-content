---
term: POLITIKE (INYANDITSWE NTO)
---

Ururimi rwo ku rwego rwo hejuru, rushingiye ku bakoresha rwemerera gusobanura mu buryo bworoshe ivyangombwa UTXO ishobora gufungurwa mu rwego rwa Miniscript. Iryo tegeko ni insobanuro y’ibintu bitaboneka y’amategeko agenga ivy’ugukoresha amahera. Ishobora rero gukoranirizwa hamwe mu nyandiko ntoyi, ariyo ingana n'imwe ku yindi n'ibikorwa biva mu rurimi rw'inyandiko kavukire rwa Bitcoin.


![](../../dictionnaire/assets/30.webp)


Ururimi rw’ingingo ngenderwako rutandukanye gatoyi n’ururimi rw’inyandiko ntoyi. Nk’akarorero, wiyumvire uburyo bwo gucungera umutekano bufise inzira nyamukuru ari urufunguzo A, inzira yo gusubirana ikaba urufunguzo B, ariko mu gihe c’umwaka umwe (nk’amabarabara 52.560). Mu vy’amategeko, ivyo vyoba ari:


```plaintext
or(pk(A),and(pk(B),older(52560)))
```


Iyo bimaze gukoranirizwa hamwe mu nyandiko ntoyi, vyoba ari:


```plaintext
andor(pk(B),older(52560),pk(A))
```


Kandi iyo imaze guhindurwa mu nyandiko kavukire, yoba ari:


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