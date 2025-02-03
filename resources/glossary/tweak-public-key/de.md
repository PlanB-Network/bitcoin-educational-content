---
term: TWEAK (ÖFFENTLICHER SCHLÜSSEL)

---
In der Kryptographie bedeutet "Tweaking", dass ein öffentlicher Schlüssel durch einen additiven Wert, den so genannten "Tweak", so verändert wird, dass er mit Kenntnis des ursprünglichen privaten Schlüssels und des Tweaks verwendbar bleibt. Technisch gesehen ist ein Tweak ein skalarer Wert, der zum ursprünglichen öffentlichen Schlüssel hinzugefügt wird. Wenn $P$ der öffentliche Schlüssel und $t$ der Tweak ist, wird der getweakte öffentliche Schlüssel:

$$
P' = P + tG
$$

Dabei ist $G$ der Generator der verwendeten elliptischen Kurve. Diese Operation ermöglicht es, einen neuen öffentlichen Schlüssel zu erhalten, der vom ursprünglichen Schlüssel abgeleitet ist und bestimmte kryptografische Eigenschaften beibehält, die ihn verwendbar machen. Diese Methode wird beispielsweise für Taproot-Adressen (P2TR) verwendet, um Ausgaben entweder durch Vorlage einer Schnorr-Signatur auf herkömmliche Weise oder durch Erfüllung einer der in einem Merkle-Baum, auch "MAST" genannt, genannten Bedingungen zu ermöglichen.

![](../../dictionnaire/assets/26.webp)