---
term: SERA (MINISCRIPT)
---

Lugha ya kiwango cha juu, inayolenga mtumiaji ambayo inaruhusu ubainishaji rahisi wa masharti ambayo UTXO inaweza kufunguliwa ndani ya mfumo wa Hati Ndogo. Sera ni maelezo dhahania ya sheria za matumizi. Kisha inaweza kukusanywa kuwa hati ndogo, ambayo ni sawa na moja hadi moja na utendakazi kutoka kwa lugha asilia ya hati ya Bitcoin.


![](../../dictionnaire/assets/30.webp)


Lugha ya sera ni tofauti kidogo na lugha ya hati ndogo. Kwa mfano, fikiria mfumo wa usalama ulio na njia ya msingi kuwa ufunguo A, na njia ya uokoaji ikiwa ufunguo B, lakini chini ya muda wa mwaka mmoja (takriban vitalu 52,560). Katika sera, hii itakuwa:


```plaintext
or(pk(A),and(pk(B),older(52560)))
```


Mara tu ikiwa imejumuishwa katika maandishi madogo, itakuwa:


```plaintext
andor(pk(B),older(52560),pk(A))
```


Na mara tu ikibadilishwa kuwa hati asili, itakuwa:


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