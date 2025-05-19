---
term: CISA
---

Akronym für "Cross-Input Signature Aggregation". Hierbei handelt es sich um einen technischen Vorschlag zur Optimierung des Umfangs von Bitcoin-Transaktionen durch Verringerung der Anzahl der für ihre Validierung erforderlichen Unterschriften.


Gegenwärtig muss auf Bitcoin jede Eingabe in einer Transaktion mit einer individuellen Unterschrift versehen werden, bevor sie verbraucht werden kann. Damit wird nachgewiesen, dass der Eigentümer des betreffenden UTXO die Transaktion autorisiert hat. Mit CISA wird angestrebt, die Signaturen aller Inputs einer Transaktion zu einer einzigen Signatur für alle Inputs zusammenzufassen. Dies würde es ermöglichen, den Umfang von Transaktionen mit vielen Eingaben zu verringern und damit auch deren Kosten zu senken. Dies wäre besonders nützlich für diejenigen, die Coinjoins oder Konsolidierungen durchführen, während gleichzeitig mehr Transaktionen auf Bitcoin bestätigt werden können, ohne dass sich die Blockgrößen oder Intervalle ändern. CISA basiert auf dem Schnorr-Protokoll, das eine lineare Aggregation von Signaturen ermöglicht. Das bedeutet, dass eine einzige Signatur den Besitz mehrerer unabhängiger Schlüssel nachweisen kann.


Die Implementierung von CISA auf Bitcoin ist jedoch sehr komplex, da sie tiefgreifende Änderungen in der Arbeitsweise von Skripten erfordert. Derzeit erfolgt die Skriptüberprüfung bei Bitcoin Eingabe für Eingabe. Die Umstellung auf ein Modell, bei dem eine gesamte Transaktion auf einmal geprüft wird, wie es CISA vorschlägt, ist alles andere als eine triviale Änderung.