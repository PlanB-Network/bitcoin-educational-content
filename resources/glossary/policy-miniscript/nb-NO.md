---
term: POLICY (MINISCRIPT)

---
Et brukerorientert høynivåspråk som gjør det mulig å spesifisere under hvilke betingelser en UTXO kan låses opp innenfor rammene av Miniscript. Policyen er en abstrakt beskrivelse av utgiftsreglene. Den kan deretter kompileres til miniscript, som er en én-til-én-ekvivalent med operasjoner fra Bitcoins opprinnelige skriptspråk.

![](../../dictionnaire/assets/30.webp)

Policyspråket er litt forskjellig fra miniskriptspråket. Tenk deg for eksempel et sikkerhetssystem med en primærbane som er nøkkel A, og en gjenopprettingsbane som er nøkkel B, men med en tidslås på ett år (ca. 52 560 blokker). I policyer ville dette være

```plaintext
or(pk(A),and(pk(B),older(52560)))
```

Når det er kompilert til miniscript, vil det være det:

```plaintext
andor(pk(B),older(52560),pk(A))
```

Og når det er konvertert til innfødt skript, vil det være det:

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