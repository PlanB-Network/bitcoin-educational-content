---
term: POLICY (MINISCRIPT)
---

Eine hochrangige, benutzerorientierte Sprache, die die einfache Spezifikation von Bedingungen ermöglicht, unter denen ein UTXO im Rahmen von Miniscript entsperrt werden kann. Die Policy ist eine abstrakte Beschreibung der Ausgaberegeln. Sie kann dann in Miniscript kompiliert werden, welches ein eins-zu-eins Äquivalent mit Operationen aus der nativen Skriptsprache von Bitcoin ist.

![](../../dictionnaire/assets/30.png)

Die Policy-Sprache unterscheidet sich leicht von der Miniscript-Sprache. Stellen Sie sich zum Beispiel ein Sicherheitssystem vor, bei dem der primäre Pfad Schlüssel A und ein Wiederherstellungspfad Schlüssel B ist, jedoch unter einem Zeitraum von einem Jahr (ungefähr 52.560 Blöcke). In der Policy würde dies so aussehen:

```plaintext
or(pk(A),and(pk(B),older(52560)))
```

Einmal in Miniscript kompiliert, wäre es:

```plaintext
andor(pk(B),older(52560),pk(A))
```

Und einmal in natives Skript umgewandelt, wäre es:

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