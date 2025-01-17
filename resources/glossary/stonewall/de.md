---
term: STONEWALL

---
Eine spezielle Form der Bitcoin-Transaktion, die darauf abzielt, die Privatsphäre des Nutzers während einer Ausgabe zu erhöhen, indem ein Coinjoin zwischen zwei Personen imitiert wird, ohne tatsächlich einer zu sein. In der Tat ist diese Transaktion nicht gemeinschaftlich. Ein Nutzer kann sie alleine durchführen und nur seine eigenen UTXOs als Inputs verwenden. Daher können Sie eine Stonewall-Transaktion für jede Gelegenheit erstellen, ohne sich mit einem anderen Benutzer synchronisieren zu müssen.

Die Stonewall-Transaktion läuft folgendermaßen ab: Am Eingang der Transaktion verwendet der Absender 2 UTXOs, die ihm gehören. Die Transaktion erzeugt dann 4 Ausgaben, von denen 2 genau den gleichen Betrag ausmachen. Die anderen 2 bilden die Veränderung. Von den 2 Outputs mit gleichem Betrag geht nur einer tatsächlich an den Empfänger der Zahlung.

Es gibt also nur 2 Rollen bei einer Stonewall-Transaktion:


- Der Absender, der die eigentliche Zahlung vornimmt;
- Der Empfänger, der möglicherweise nicht weiß, um welche Art von Transaktion es sich handelt, und einfach eine Zahlung vom Absender erwartet.

![](../../dictionnaire/assets/33.webp)

Stonewall-Transaktionen sind sowohl in der Samourai Wallet-Anwendung als auch in der Sparrow Wallet-Software verfügbar.

Die Stonewall-Struktur fügt der Transaktion eine Menge Entropie hinzu und verschleiert die Spur für die Kettenanalyse. Von außen betrachtet kann eine solche Transaktion als eine kleine Münzverknüpfung zwischen zwei Personen interpretiert werden. In Wirklichkeit handelt es sich jedoch, wie bei der Stonewall x2-Transaktion, um eine Zahlung. Diese Methode führt also zu Unsicherheiten bei der Kettenanalyse oder sogar zu falschen Spuren. Selbst wenn es einem externen Beobachter gelingt, das Muster der Stonewall-Transaktion zu erkennen, wird er nicht über alle Informationen verfügen. Er wird nicht in der Lage sein zu bestimmen, welcher der beiden UTXOs mit den gleichen Beträgen der Zahlung entspricht. Außerdem können sie nicht feststellen, ob die beiden UTXOs am Eingang von zwei verschiedenen Personen stammen oder ob sie zu einer einzigen Person gehören, die sie zusammengelegt hat. Dieser letzte Punkt ist darauf zurückzuführen, dass Stonewall x2-Transaktionen genau demselben Muster folgen wie Stonewall-Transaktionen. Von außen und ohne zusätzliche Kontextinformationen ist es unmöglich, eine Stonewall-Transaktion von einer Stonewall x2-Transaktion zu unterscheiden. Allerdings handelt es sich bei ersteren nicht um kollaborative Transaktionen, bei letzteren hingegen schon. Dies lässt noch mehr Zweifel an dieser Ausgabe aufkommen.