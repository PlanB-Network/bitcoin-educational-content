---
term: TWEAK
---

In der Kryptographie wird ein öffentlicher Schlüssel durch einen additiven Wert, den so genannten "Tweak", so verändert, dass er bei Kenntnis des ursprünglichen privaten Schlüssels und des Tweaks verwendbar bleibt. Technisch gesehen ist ein Tweak ein skalarer Wert, der zu dem ursprünglichen öffentlichen Schlüssel hinzugefügt wird. Wenn $P$ der öffentliche Schlüssel und $t$ der Tweak ist, wird der getweakte öffentliche Schlüssel zu :


$$
P' = P + tG
$$


Dabei ist $G$ der Generator der verwendeten elliptischen Kurve. Dieser Vorgang erzeugt einen neuen öffentlichen Schlüssel, der vom Original abgeleitet ist, wobei bestimmte kryptografische Eigenschaften beibehalten werden, die seine Verwendung ermöglichen. Diese Methode wird beispielsweise für Taproot (P2TR)-Adressen verwendet, um die Ausgabe entweder durch Vorlage einer Schnorr-Signatur auf herkömmliche Weise oder durch Erfüllung einer der in einem Merkle Tree, auch als "MAST" bezeichnet, festgelegten Bedingungen zu ermöglichen.