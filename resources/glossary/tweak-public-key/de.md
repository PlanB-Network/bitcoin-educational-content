---
term: TWEAK (ÖFFENTLICHER SCHLÜSSEL)
---

Im Bereich der Kryptografie bedeutet das "Tweaken" eines öffentlichen Schlüssels, diesen Schlüssel durch die Verwendung eines additiven Werts, genannt "Tweak", zu modifizieren, sodass er unter Kenntnis des ursprünglichen privaten Schlüssels und des Tweaks weiterhin nutzbar bleibt. Technisch gesehen ist ein Tweak ein Skalarwert, der zum ursprünglichen öffentlichen Schlüssel hinzugefügt wird. Wenn $P$ der öffentliche Schlüssel und $t$ der Tweak ist, wird der getweakte öffentliche Schlüssel zu:

$$
P' = P + tG
$$

Wobei $G$ der Generator der verwendeten elliptischen Kurve ist. Diese Operation ermöglicht es, einen neuen öffentlichen Schlüssel abzuleiten, der vom ursprünglichen Schlüssel stammt, während bestimmte kryptografische Eigenschaften beibehalten werden, die ihn nutzbar machen. Zum Beispiel wird diese Methode für Taproot-Adressen (P2TR) verwendet, um Ausgaben entweder durch Vorlegen einer Schnorr-Signatur auf traditionelle Weise oder durch Erfüllen einer der Bedingungen in einem Merkle-Baum, auch "MAST" genannt, zu ermöglichen.

![](../../dictionnaire/assets/26.png)