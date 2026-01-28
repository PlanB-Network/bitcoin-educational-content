---
term: IVYANDITSWE
---

Ikintu kiri mu gucuruza Bitcoin kiri mu vyinjizwa. `scriptSig` itanga amakuru akenewe kugira ngo yuzuze ivyangombwa vyashizweho na `scriptPubKey` y'ibikorwa vya kera amafaranga ariko arakoreshwa. Gutyo irafise uruhara rwo kwuzuza `scriptPubKey`. Mu bisanzwe, `scriptSig` irimwo umukono wa digitale n'urufunguzo rwa bose. Iryo sinya rikorwa na nyen’ama bitcoins akoresheje urufunguzo rwiwe rw’ibanga kandi ryerekana ko bafise uburenganzira bwo gukoresha UTXO. Muri iki gihe, `scriptSig` yerekana ko uwufise inyungu afise urufunguzo rwihariye rujanye n'urufunguzo rwa bose rujanye n'urufunguzo rwa Address rwavuzwe muri `scriptPubKey` y'isoko ry'imbere ry'isohoka.


Iyo igikorwa kigenzuwe, amakuru ava muri `scriptSig` ashirwa mu ngiro mu `scriptPubKey` ihuye. Iyo igisubizo ari co, bisigura ko ivyangombwa vyo gukoresha ayo mahera vyarangutse. Iyo ivyinjijwe vyose vy'ibikorwa bitanga `scriptSig` yemeza `scriptPubKey` yabo, ibikorwa birafise akamaro kandi bishobora kwongerwa ku gice kugira ngo bishirwe mu ngiro.


Nk'akarorero, ng'iyi P2PKH ya kera `inyandikoSig`:


```text
<signature> <public key>
```


Ihuye n'inyandiko `Urufunguzo rwaPub` rwoba:


```text
OP_DUP OP_HASH160 OP_PUSHBYTES_20 <address> OP_EQUALVERIFY OP_CHECKSIG
```


![](../../dictionnaire/assets/35.webp)


> ► *Ico `scriptSig` na co nyene rimwe na rimwe citwa "inyandiko yo gufungura" mu congereza.*