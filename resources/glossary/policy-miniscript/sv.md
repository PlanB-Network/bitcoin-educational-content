---
term: Policy (miniscript)
definition: Högnivåspråk för att specificera utgiftsvillkor för en UTXO i Miniscript.
---

Ett användarorienterat språk på hög nivå som möjliggör en enkel specifikation av villkor under vilka en UTXO kan låsas upp inom ramen för Miniscript. Policyn är en abstrakt beskrivning av utgiftsreglerna. Den kan sedan kompileras till miniscript, som är en en-till-en-ekvivalent med operationer från Bitcoin:s inbyggda skriptspråk.





Policyspråket skiljer sig något från miniscriptspråket. Tänk dig till exempel ett säkerhetssystem med en primär sökväg som är nyckel A och en återställningsväg som är nyckel B, men med en tidslåsning på ett år (cirka 52 560 block). I policy skulle detta vara:


```plaintext
or(pk(A),and(pk(B),older(52560)))
```


När den väl har sammanställts till miniscript skulle den vara det:


```plaintext
andor(pk(B),older(52560),pk(A))
```


Och när den konverterats till inhemsk skrift skulle den vara det:


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