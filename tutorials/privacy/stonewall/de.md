---
name: Stonewall
description: Verständnis und Verwendung von Stonewall-Transaktionen
---
![cover stonewall](assets/cover.jpeg)

> *"Brechen Sie die Annahmen der Blockchain-Analyse mit mathematisch beweisbarem Zweifel zwischen Absender und Empfänger Ihrer Transaktionen."*

## Was ist eine Stonewall-Transaktion?
Stonewall ist eine spezielle Form einer Bitcoin-Transaktion, die darauf abzielt, die Benutzerprivatsphäre während einer Ausgabe zu erhöhen, indem sie eine Coinjoin zwischen zwei Personen imitiert, ohne tatsächlich eine zu sein. Tatsächlich handelt es sich bei dieser Transaktion nicht um eine Zusammenarbeit. Ein Benutzer kann sie alleine erstellen und nur seine eigenen UTXOs als Eingabe verwenden. Daher können Sie eine Stonewall-Transaktion für jede Gelegenheit erstellen, ohne sich mit einem anderen Benutzer synchronisieren zu müssen.

Der Ablauf einer Stonewall-Transaktion ist wie folgt: Als Eingabe für die Transaktion verwendet der Absender 2 UTXOs, die ihm gehören. Als Ausgabe erzeugt die Transaktion 4 Ausgaben, von denen 2 genau den gleichen Betrag haben werden. Die anderen 2 werden Wechselgeld sein. Von den 2 Ausgaben mit dem gleichen Betrag geht nur eine tatsächlich an den Zahlungsempfänger.

Daher gibt es in einer Stonewall-Transaktion nur 2 Rollen:
- Der Absender, der die eigentliche Zahlung vornimmt;
- Der Empfänger, der die spezifische Natur der Transaktion ignorieren kann und einfach eine Zahlung vom Absender erwartet.

Lassen Sie uns anhand eines Beispiels diese Transaktionsstruktur verstehen. Alice ist in der Bäckerei, um ihr Baguette zu kaufen, das 4.000 Sats kostet. Sie möchte in Bitcoins bezahlen und dabei ein gewisses Maß an Privatsphäre für ihre Zahlung wahren. Daher beschließt sie, eine Stonewall-Transaktion für die Zahlung zu erstellen.
![transaction stonewall bakery](assets/fr/1.png)
Bei der Analyse dieser Transaktion können wir sehen, dass der Bäcker tatsächlich 4.000 Sats als Zahlung für das Baguette erhalten hat. Alice hat 2 UTXOs als Eingabe verwendet: einen im Wert von 10.000 Sats und einen im Wert von 15.000 Sats. Als Ausgabe erhielt sie 3 UTXOs: einen im Wert von 4.000 Sats, einen im Wert von 6.000 Sats und einen im Wert von 11.000 Sats. Alice hat daher in dieser Transaktion einen Netto-Saldo von -4.000 Sats, was dem Preis des Baguettes entspricht.

In diesem Beispiel habe ich absichtlich die Mining-Gebühren vernachlässigt, um das Verständnis zu erleichtern. In Wirklichkeit werden die Transaktionsgebühren vollständig vom Absender übernommen.

Was ist der Unterschied zwischen Stonewall und Stonewall x2?
Die Stonewall-Transaktion funktioniert genauso wie die StonewallX2-Transaktion, mit der Ausnahme, dass letztere eine Zusammenarbeit erfordert, im Gegensatz zur klassischen Stonewall-Transaktion, daher die Bezeichnung "x2". Die Stonewall-Transaktion kann tatsächlich ohne externe Zusammenarbeit ausgeführt werden: Der Absender kann sie ohne die Hilfe einer anderen Person abschließen. Für eine Stonewall x2-Transaktion tritt jedoch ein zusätzlicher Teilnehmer, der "Kollaborateur", in den Prozess ein. Der Kollaborateur steuert seine eigenen Bitcoins als Eingabe bei, zusammen mit denen des Absenders, und erhält die gesamte Summe als Ausgabe (abzüglich der Mining-Gebühren).

Lassen Sie uns unser Beispiel mit Alice in der Bäckerei noch einmal betrachten. Wenn sie eine Stonewall x2-Transaktion hätte durchführen wollen, hätte Alice während der Transaktionserstellung mit Bob (einer dritten Person) zusammenarbeiten müssen. Jeder von ihnen hätte eine UTXO als Eingabe bereitgestellt. Bob hätte dann die Gesamtheit seines Beitrags als Ausgabe erhalten. Der Bäcker hätte die Zahlung für das Baguette auf die gleiche Weise wie bei der Stonewall-Transaktion erhalten, während Alice ihren anfänglichen Saldo abzüglich der Kosten des Baguettes erhalten hätte.
![Stonewall Tutorial - Sparrow Wallet](https://youtu.be/mlRtZvWGuk0?si=e_lSKJLvybWUna1j)
Als erfahrener professioneller Übersetzer liegt meine Hauptaufgabe darin, technische Inhalte aus dem Englischen präzise in meine Muttersprache, Deutsch, zu übersetzen. Bitte beachten Sie die folgenden Richtlinien, um eine hochwertige Übersetzung sicherzustellen:

Ursprungssprache: Der Inhalt liegt ursprünglich auf Englisch vor.
Art des Inhalts: Sie werden auf technisches Material stoßen, möglicherweise einschließlich branchenspezifischer Terminologie.
Links und technische Begriffe: Übersetzen Sie keine URLs oder hochspezifischen technischen Begriffe. Wenn Sie unsicher sind, behalten Sie den Originalbegriff bei.
Formatierungskonsistenz: Beibehaltung des gleichen Markdown-Layouts und der Formatierung wie im Originaltext. Die Konsistenz der Struktur ist entscheidend.
YML-Eigenschaften: Wenn eine Zeile mit einer YAML-Eigenschaft beginnt (z. B. 'name:', 'goal:', 'objectives:'), behalten Sie den Eigenschaftsnamen in Englisch bei.
Kultureller Kontext: Bei kulturellen oder kontextspezifischen Verweisen, die möglicherweise nicht direkt übersetzt werden können, umschreiben Sie diese, um die beabsichtigte Bedeutung zu erhalten, oder geben Sie eine kurze Erklärung.
Der Schwerpunkt sollte darauf liegen, die Integrität des technischen Inhalts zu wahren und gleichzeitig sicherzustellen, dass die Übersetzung in Deutsch verständlich und kontextuell korrekt ist.

Dies ist der zu übersetzende Text:
![Stonewall Tutorial - Sparrow Wallet](https://youtu.be/su89ljkV_OI?si=1jNaSJGvECUYe6Or)

**Externe Ressourcen:**
- https://docs.samourai.io/en/spend-tools#stonewall ;
- https://samouraiwallet.com/stonewall.