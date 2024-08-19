---
term: STONEWALL
---

Eine spezifische Form der Bitcoin-Transaktion, die darauf abzielt, die Privatsphäre des Benutzers beim Ausgeben zu erhöhen, indem sie einen Coinjoin zwischen zwei Personen nachahmt, ohne tatsächlich einer zu sein. Tatsächlich ist diese Transaktion nicht kollaborativ. Ein Benutzer kann sie alleine konstruieren, wobei nur seine eigenen UTXOs als Eingaben beteiligt sind. Daher können Sie eine Stonewall-Transaktion für jeden Anlass erstellen, ohne sich mit einem anderen Benutzer synchronisieren zu müssen.

Die Funktionsweise der Stonewall-Transaktion ist wie folgt: Am Eingang der Transaktion verwendet der Sender 2 UTXOs, die ihm gehören. Die Transaktion erzeugt dann 4 Ausgänge, von denen 2 genau denselben Betrag haben werden. Die anderen 2 stellen das Wechselgeld dar. Von den 2 Ausgängen mit demselben Betrag geht tatsächlich nur einer an den Empfänger der Zahlung.

Somit gibt es nur 2 Rollen in einer Stonewall-Transaktion:
* Der Sender, der die eigentliche Zahlung leistet;
* Der Empfänger, der möglicherweise nichts von der spezifischen Natur der Transaktion weiß und einfach eine Zahlung vom Sender erwartet.

![](../../dictionnaire/assets/33.png)
Stonewall-Transaktionen sind sowohl in der Samourai Wallet-Anwendung als auch in der Sparrow Wallet-Software verfügbar.

Die Stonewall-Struktur fügt der Transaktion viel Entropie hinzu und verschleiert die Spur für die Kettenanalyse. Von außen kann eine solche Transaktion als ein kleiner Coinjoin zwischen zwei Personen interpretiert werden. Aber in Wirklichkeit, genau wie die Stonewall x2-Transaktion, ist es eine Zahlung. Diese Methode erzeugt somit Unsicherheiten in der Kettenanalyse oder führt sogar zu falschen Spuren. Selbst wenn ein externer Beobachter das Muster der Stonewall-Transaktion identifizieren kann, wird er nicht alle Informationen haben. Er wird nicht bestimmen können, welcher der beiden UTXOs mit denselben Beträgen der Zahlung entspricht. Außerdem wird er nicht feststellen können, ob die beiden UTXOs am Eingang von zwei verschiedenen Personen stammen oder ob sie zu einer einzigen Person gehören, die sie zusammengeführt hat. Dieser letzte Punkt ist darauf zurückzuführen, dass Stonewall x2-Transaktionen genau demselben Muster wie Stonewall-Transaktionen folgen. Von außen und ohne zusätzliche Kontextinformationen ist es unmöglich, eine Stonewall-Transaktion von einer Stonewall x2-Transaktion zu unterscheiden. Die ersteren sind jedoch keine kollaborativen Transaktionen, während die letzteren es sind. Dies fügt noch mehr Zweifel an dieser Ausgabe hinzu.