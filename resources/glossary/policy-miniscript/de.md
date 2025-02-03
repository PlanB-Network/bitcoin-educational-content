---
term: POLITIK (MINISCRIPT)

---
Eine benutzerorientierte Hochsprache, die die einfache Spezifikation von Bedingungen ermöglicht, unter denen ein UTXO im Rahmen von Miniscript freigeschaltet werden kann. Die Policy ist eine abstrakte Beschreibung der Ausgaberegeln. Sie kann dann in Miniscript kompiliert werden, das ein Eins-zu-Eins-Äquivalent zu den Operationen der nativen Bitcoin-Skriptsprache ist.

![](../../dictionnaire/assets/30.webp)

Die Policy-Sprache unterscheidet sich geringfügig von der Miniscript-Sprache. Stellen Sie sich zum Beispiel ein Sicherheitssystem vor, bei dem der Schlüssel A der primäre Pfad und der Schlüssel B der Wiederherstellungspfad ist, jedoch mit einer Zeitsperre von einem Jahr (etwa 52.560 Blöcke). In der Politik würde dies so aussehen:

```plaintext
or(pk(A),and(pk(B),older(52560)))
```

Einmal in Miniskript kompiliert, wäre es:

```plaintext
andor(pk(B),older(52560),pk(A))
```

Und nach der Konvertierung in natives Skript wäre es das auch:

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