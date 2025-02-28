---
name: Stonewall
description: Verständnis und Nutzung von Stonewall-Transaktionen
---
![cover stonewall](assets/cover.webp)

***ACHTUNG:** Nach der Verhaftung der Gründer von Samourai Wallet und der Beschlagnahme ihrer Server am 24. April erfordert die Nutzung der Samourai Wallet-App nun eine Verbindung zu Ihrem eigenen Dojo, um ordnungsgemäß zu funktionieren. Abgesehen davon sind die Stonewall-Transaktionen überhaupt nicht betroffen und können weiterhin problemlos durchgeführt werden. Tatsächlich werden diese Arten von Transaktionen autonom durchgeführt, ohne die Notwendigkeit einer externen Zusammenarbeit oder einer Verbindung über Soroban.*

_Wir verfolgen die Entwicklungen in diesem Fall sowie die Entwicklungen bezüglich der zugehörigen Tools genau. Seien Sie versichert, dass wir dieses Tutorial aktualisieren werden, sobald neue Informationen verfügbar sind._

_Dieses Tutorial wird nur zu Bildungs- und Informationszwecken bereitgestellt. Wir befürworten oder ermutigen die Verwendung dieser Tools zu kriminellen Zwecken nicht. Es liegt in der Verantwortung jedes Benutzers, die Gesetze in seiner Gerichtsbarkeit zu beachten._

---

> *"Durchbrechen Sie die Annahmen der Blockchain-Analyse mit mathematisch beweisbarem Zweifel zwischen Sender und Empfänger Ihrer Transaktionen."*

## Was ist eine Stonewall-Transaktion?
Eine Stonewall-Transaktion ist eine spezifische Form der Bitcoin-Transaktion, die darauf abzielt, die Privatsphäre der Nutzer während einer Transaktion zu erhöhen, indem sie eine Coinjoin zwischen zwei Parteien nachahmt, ohne tatsächlich eine zu sein. Tatsächlich ist diese Transaktion nicht kollaborativ. Ein Nutzer kann sie alleine durchführen, indem er nur seine eigenen UTXOs als Eingaben verwendet. Daher können Sie eine Stonewall-Transaktion für jede Gelegenheit erstellen, ohne sich mit einem anderen Nutzer abstimmen zu müssen.

Die Funktionsweise einer Stonewall-Transaktion ist wie folgt: Als Eingabe verwendet der Sender 2 UTXOs, die ihm gehören. Als Ausgabe erzeugt die Transaktion 4 Ausgaben, einschließlich 2, die genau denselben Betrag haben werden. Die anderen 2 werden Wechselgeld sein. Von den 2 Ausgaben mit demselben Betrag wird tatsächlich nur eine an den Zahlungsempfänger gehen.

Es gibt nur 2 Rollen in einer Stonewall-Transaktion:
- Der Sender, der die eigentliche Zahlung leistet;
- Der Empfänger, der sich der spezifischen Natur der Transaktion möglicherweise nicht bewusst ist und einfach eine Zahlung vom Sender erwartet.

Lassen Sie uns ein Beispiel nehmen, um diese Transaktionsstruktur zu verstehen. Alice ist in der Bäckerei, um ihre Baguette zu kaufen, die `4.000 Sats` kostet. Sie möchte in Bitcoins zahlen und dabei ein gewisses Maß an Privatsphäre bei ihrer Zahlung wahren. Daher entscheidet sie sich, eine Stonewall-Transaktion für die Zahlung zu erstellen.
![transaction stonewall bakery](assets/de/1.webp)
Bei der Analyse dieser Transaktion können wir sehen, dass der Bäcker tatsächlich `4.000 Sats` als Zahlung für die Baguette erhalten hat. Alice verwendete 2 UTXOs als Eingaben: einen von `10.000 Sats` und einen von `15.000 Sats`. Als Ausgabe erhielt sie 3 UTXOs: einen von `4.000 Sats`, einen von `6.000 Sats` und einen von `11.000 Sats`. Alice hat ein Netto-Saldo von `-4.000 Sats` in dieser Transaktion, was dem Preis der Baguette entspricht.

In diesem Beispiel habe ich die Mining-Gebühren absichtlich weggelassen, um das Verständnis zu erleichtern. In der Realität werden die Transaktionsgebühren vollständig vom Sender getragen.

## Was ist der Unterschied zwischen Stonewall und Stonewall x2?
Die Stonewall-Transaktion funktioniert auf die gleiche Weise wie die StonewallX2-Transaktion, mit dem einzigen Unterschied, dass letztere eine Zusammenarbeit erfordert, im Gegensatz zur klassischen Stonewall-Transaktion, daher die Bezeichnung "x2". Tatsächlich kann die Stonewall-Transaktion ohne externe Zusammenarbeit durchgeführt werden: Der Sender kann sie ohne die Hilfe einer anderen Person durchführen. Für eine Stonewall x2-Transaktion tritt jedoch ein zusätzlicher Teilnehmer, der "Mitarbeiter", in den Prozess ein. Der Mitarbeiter trägt seine eigenen Bitcoins als Eingabe bei, neben denen des Senders, und erhält die gesamte Summe als Ausgabe (abzüglich der Mining-Gebühren).

Lassen Sie uns unser Beispiel mit Alice in der Bäckerei erneut besuchen. Wenn sie eine Stonewall x2-Transaktion hätte durchführen wollen, hätte Alice mit Bob (einer dritten Partei) bei der Erstellung der Transaktion zusammenarbeiten müssen. Sie hätten jeweils ein Eingabe-UTXO bereitgestellt. Bob hätte dann den vollen Betrag seiner Eingabe als Ausgabe erhalten. Der Bäcker hätte seine Zahlung für seine Baguette auf die gleiche Weise wie bei der Stonewall-Transaktion erhalten, während Alice ihr anfängliches Guthaben zurückbekommen hätte, abzüglich der Kosten für die Baguette.
![transaction stonewall x2](assets/de/2.webp)
Aus externer Perspektive wäre das Muster der Transaktion genau gleich geblieben.
![Stonewall oder Stonewall x2 ?](assets/de/3.webp)

Zusammengefasst teilen Stonewall- und Stonewall x2-Transaktionen eine identische Struktur. Der Unterschied zwischen den beiden liegt in ihrer kollaborativen Natur. Die Stonewall-Transaktion wird individuell entwickelt, ohne die Notwendigkeit zur Zusammenarbeit. Im Gegensatz dazu basiert die Stonewall x2-Transaktion auf der Kooperation zwischen zwei Personen für ihre Durchführung.

[**-> Erfahren Sie mehr über Stonewall x2-Transaktionen**](https://planb.network/tutorials/privacy/on-chain/stonewall-x2-05120280-f6f9-4e14-9fb8-c9e603f73e5b)

## Was ist der Zweck einer Stonewall-Transaktion?
Die Stonewall-Struktur fügt der Transaktion eine erhebliche Menge an Entropie hinzu und verschleiert die Kettenanalyse. Aus externer Perspektive kann eine solche Transaktion als ein kleiner Coinjoin zwischen zwei Personen interpretiert werden. Aber in Wirklichkeit, genau wie die Stonewall x2-Transaktion, handelt es sich um eine Zahlung. Diese Methode erzeugt daher Unsicherheiten in der Kettenanalyse und kann sogar zu falschen Fährten führen.

Lassen Sie uns Alices Beispiel in der Bäckerei noch einmal betrachten. Die Transaktion auf der Blockchain würde wie folgt erscheinen:
![Stonewall oder Stonewall x2 ?](assets/de/4.webp)
Ein externer Beobachter, der sich auf gängige Heuristiken der Kettenanalyse verlässt, könnte fälschlicherweise schlussfolgern, dass "*zwei Personen einen kleinen Coinjoin durchgeführt haben, mit jeweils einem UTXO als Eingabe und zwei UTXOs als Ausgabe*".
![Stonewall oder Stonewall x2 ?](assets/de/5.webp)
Diese Interpretation ist falsch, denn wie Sie wissen, wurde ein UTXO an den Bäcker gesendet, die 2 UTXOs in der Eingabe stammen von Alice, und sie erhielt 3 Wechselgeld-Ausgaben.

![transaction stonewall baker](assets/de/1.webp)
Selbst wenn ein Außenstehender das Muster der Stonewall-Transaktion identifizieren kann, wird er nicht alle Informationen haben. Er wird nicht bestimmen können, welches der beiden UTXOs gleicher Beträge der Zahlung entspricht. Außerdem wird er nicht feststellen können, ob die beiden UTXOs in der Eingabe von zwei verschiedenen Personen stammen oder ob sie zu einer einzigen Person gehören, die sie zusammengeführt hat. Dieser letzte Punkt ist darauf zurückzuführen, dass Stonewall x2-Transaktionen, über die wir oben gesprochen haben, genau dem gleichen Muster wie Stonewall-Transaktionen folgen. Von außen und ohne zusätzliche Informationen über den Kontext ist es unmöglich, eine Stonewall-Transaktion von einer Stonewall x2-Transaktion zu unterscheiden. Allerdings sind erstere keine kollaborativen Transaktionen, während letztere es sind. Dies fügt noch mehr Zweifel über diese Ausgabe hinzu.
![Stonewall oder Stonewall x2 ?](assets/de/3.webp)
## Wie führt man eine Stonewall-Transaktion auf Samourai Wallet durch?
Im Gegensatz zu Stowaway- oder Stonewall x2 (Cahoots)-Transaktionen erfordert die Stonewall-Transaktion nicht die Verwendung von Paynyms. Sie kann direkt durchgeführt werden, ohne Vorbereitungsschritte. Folgen Sie dazu unserem Video-Tutorial auf Samourai Wallet: 
![Stonewall Tutorial - Samourai Wallet](https://youtu.be/mlRtZvWGuk0?si=e_lSKJLvybWUna1j)

## Wie führt man eine Stonewall-Transaktion auf Sparrow Wallet durch?
Im Gegensatz zu Stowaway- oder Stonewall x2 (Cahoots)-Transaktionen erfordert die Stonewall-Transaktion nicht die Verwendung von Paynyms. Sie kann direkt durchgeführt werden, ohne Vorbereitungsschritte. Folgen Sie dazu unserem Video-Tutorial auf Sparrow Wallet:
![Stonewall Tutorial - Sparrow Wallet](https://youtu.be/su89ljkV_OI?si=1jNaSJGvECUYe6Or)

**Externe Ressourcen:**
- https://docs.samourai.io/en/spend-tools#stonewall.
