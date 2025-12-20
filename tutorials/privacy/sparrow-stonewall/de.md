---
name: Sparrow Wallet - Stonewall
description: Stonewall-Transaktionen auf Sparrow verstehen und nutzen
---

![cover](assets/cover.webp)




> *Brechen Sie die Annahmen der Blockchain-Analyse mit mathematisch nachweisbaren Zweifeln zwischen Absender und Empfänger Ihrer Transaktionen.*

## Was ist eine Stonewall-Transaktion?



Stonewall ist eine spezielle Form der Bitcoin-Transaktion, die darauf abzielt, die Vertraulichkeit der Nutzer beim Geldausgeben zu erhöhen, indem sie eine Münzverbindung zwischen zwei Personen imitiert, ohne tatsächlich eine zu sein. In der Tat ist diese Transaktion nicht gemeinschaftlich. Ein Benutzer kann sie selbst erstellen, indem er nur die ihm gehörenden UTXOs als Input verwendet. Sie können also eine Stonewall-Transaktion für jede Gelegenheit erstellen, ohne sich mit einem anderen Benutzer absprechen zu müssen.



Die Stonewall-Transaktion funktioniert folgendermaßen: Als Input für die Transaktion verwendet der Emittent 2 UTXO, die ihm gehören. Auf der Ausgabeseite erzeugt die Transaktion 4 Ausgaben, von denen 2 genau den gleichen Betrag haben. Bei den anderen 2 handelt es sich um Devisen. Von den 2 Outputs mit gleichem Betrag geht nur einer tatsächlich an den Zahlungsempfänger.



Es gibt also nur 2 Rollen bei einer Stonewall-Transaktion:




- Der Emittent, der die eigentliche Zahlung vornimmt;
- Der Empfänger, der möglicherweise nicht weiß, worum es sich bei der Transaktion handelt, und einfach eine Zahlung vom Absender erwartet.



Nehmen wir ein Beispiel, um diese Transaktionsstruktur zu verstehen. Alice ist beim Bäcker, um ihr Baguette zu kaufen, das 4.000 sats" kostet. Sie möchte in Bitcoins bezahlen und dabei eine gewisse Form der Vertraulichkeit über ihre Zahlung wahren. Also beschließt sie, eine Stonewall-Transaktion für die Zahlung zu erstellen.



![image](assets/fr/01.webp)



Die Analyse dieser Transaktion zeigt, dass der Bäcker tatsächlich 4.000 sats" als Bezahlung für das Baguette erhalten hat. Alice hat 2 UTXOs als Input verwendet: einen von `10.000 sats` und einen von `15.000 sats`. Als Output hat es 3 UTXO zurückerhalten: einen von `4.000 sats`, einen von `6.000 sats` und einen von `11.000 sats`. Alice hat also bei dieser Transaktion einen Nettosaldo von -4.000 sats, was dem Preis des Baguettes gut entspricht.



In diesem Beispiel habe ich die mining-Gebühren absichtlich vernachlässigt, um es leichter verständlich zu machen. In Wirklichkeit werden die Transaktionskosten vollständig vom Emittenten getragen.



## Was ist der Unterschied zwischen Stonewall und Stonewall x2?



Die Stonewall-Transaktion funktioniert genauso wie die StonewallX2-Transaktion, nur dass letztere im Gegensatz zur klassischen Stonewall-Transaktion eine Zusammenarbeit erfordert, daher der Name "x2". Der Grund dafür ist, dass die Stonewall-Transaktion ohne externe Zusammenarbeit ausgeführt wird: Der Absender kann sie ohne die Hilfe einer anderen Person durchführen. Bei einer Stonewall-x2-Transaktion hingegen tritt ein weiterer Teilnehmer, der so genannte "Kollaborateur", in den Prozess ein. Er steuert neben den Bitcoins des Absenders seine eigenen Bitcoins zur Transaktion bei und übernimmt am Ende den gesamten Betrag (abzüglich der mining-Kosten).



Kehren wir zu unserem Beispiel mit Alice in der Bäckerei zurück. Hätte sie eine Stonewall-x2-Transaktion durchführen wollen, hätte Alice bei der Einrichtung der Transaktion mit Bob (einer dritten Partei) zusammenarbeiten müssen. Sie hätten jeweils einen UTXO eingebracht. Bob hätte dann beim Austritt den vollen Betrag seiner Einlage erhalten. Der Bäcker hätte die Zahlung für sein Baguette auf die gleiche Weise wie bei der Stonewall-Transaktion erhalten, während Alice sein ursprüngliches Guthaben abzüglich der Kosten für das Baguette zurückerhalten hätte.



![image](assets/fr/02.webp)



Aus der Sicht eines Außenstehenden wäre die Transaktion genau die gleiche geblieben.



![image](assets/fr/03.webp)



Zusammenfassend lässt sich sagen, dass die Transaktionen von Stonewall und Stonewall x2 eine identische Struktur aufweisen. Der Unterschied zwischen den beiden liegt darin, ob sie kooperativ oder nicht kollaborativ sind. Die Stonewall-Transaktion wird individuell entwickelt, ohne die Notwendigkeit einer Zusammenarbeit. Die Stonewall-x2-Transaktion hingegen beruht auf der Zusammenarbeit zwischen zwei Personen, um sie aufzusetzen.



[**-> Erfahren Sie mehr über Stonewall-Transaktionen x2**](https://planb.academy/tutorials/privacy/on-chain/stonewall-x2-05120280-f6f9-4e14-9fb8-c9e603f73e5b)



## Was ist der Sinn einer Stonewall-Transaktion?



Die Stonewall-Struktur fügt der Transaktion eine enorme Menge an Entropie hinzu und verwischt die Grenzen der Kettenanalyse. Von außen betrachtet, kann eine solche Transaktion als eine kleine Münzverknüpfung zwischen zwei Personen interpretiert werden. In Wirklichkeit handelt es sich jedoch, wie bei der Stonewall x2-Transaktion, um eine Zahlung. Diese Methode führt daher zu Unsicherheiten in der Kettenanalyse oder sogar zu falschen Hinweisen.



Nehmen wir das Beispiel von Alice beim Bäcker. Die Transaktion auf der Blockchain würde wie folgt aussehen:



![image](assets/fr/04.webp)



Ein außenstehender Beobachter, der sich auf die üblichen Heuristiken der Kettenanalyse verlässt, könnte fälschlicherweise zu dem Schluss kommen, dass "*zwei Personen einen kleinen Coinjoin mit je einem UTXO als Input und zwei UTXOs als Output gemacht haben*".



![image](assets/fr/05.webp)



Diese Interpretation ist ungenau, denn, wie Sie wissen, wurde ein UTXO an den Bäcker geschickt, die 2 eingehenden UTXOs kamen von Alices, und sie erhielt 3 Austauschausgänge zurück.



![image](assets/fr/01.webp)



Selbst wenn es dem außenstehenden Beobachter gelingt, den Vater der Stonewall-Transaktion zu identifizieren, wird er nicht über alle Informationen verfügen. Er wird nicht in der Lage sein, festzustellen, welcher der beiden UTXOs mit den gleichen Beträgen der Zahlung entspricht. Außerdem wird er nicht feststellen können, ob die beiden UTXO-Einträge von zwei verschiedenen Personen stammen oder ob sie zu einer einzigen Person gehören, die sie zusammengeführt hat. Dieser letzte Punkt ergibt sich aus der Tatsache, dass die oben erwähnten Stonewall-x2-Transaktionen genau demselben Muster folgen wie die Stonewall-Transaktionen. Von außen betrachtet und ohne zusätzliche Kontextinformationen ist es unmöglich, einen Unterschied zwischen einer Stonewall-Transaktion und einer Stonewall-x2-Transaktion zu erkennen. Bei ersteren handelt es sich nicht um kollaborative Transaktionen, bei letzteren hingegen schon. Dies erhöht die Zweifel an den Kosten noch mehr.



![image](assets/fr/03.webp)



## Wie mache ich eine Stonewall-Transaktion auf Sparrow?



Ursprünglich vom Samurai-Wallet-Team entwickelt, wurden die Stonewall-Transaktionen von der Ashigaru-Anwendung übernommen, einem fork aus dem ursprünglichen Portfolio, das nach der Verhaftung der Samurai-Entwickler entstand, und auch auf Sparrow Wallet.



Sie müssen Sparrow installieren und eine :



https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Im Gegensatz zu Stowaway- oder Stonewall x2 (*cahoots*) Transaktionen erfordern Stonewall-Transaktionen nicht die Verwendung von Paynyms. Sie können direkt durchgeführt werden, ohne besondere Vorbereitung oder Zusammenarbeit mit einem anderen Nutzer.



Um eine Stonewall-Transaktion auf dem Sparrow durchzuführen, ist das Verfahren sehr einfach: Beginnen Sie mit der Erstellung einer Transaktion wie üblich, entweder über das Menü "Senden" oder über das Menü "UTXOs", wenn Sie eine *Coin-Kontrolle* durchführen möchten.



![Image](assets/fr/06.webp)



Geben Sie dann die Einzelheiten der Transaktion ein: die Adresse des Empfängers, ein Etikett, den zu versendenden Betrag und die Höhe oder den Satz der Gebühren, je nach den Marktbedingungen.



![Image](assets/fr/07.webp)



Bevor Sie bestätigen, können Sie hier die Stonewall-Struktur auswählen. Ersetzen Sie unten auf der Oberfläche "Effizienz" durch "Privatsphäre". Wenn diese Option nicht erscheint, bedeutet dies, dass Ihr Portfolio nicht über eine ausreichende Anzahl von UTXOs verfügt, um diese Art von Transaktion zu erstellen.



![Image](assets/fr/08.webp)



Nachdem Sie die Option "Privatsphäre" gewählt haben, werden Sie feststellen, dass sich die Struktur der Transaktion vollständig verändert hat: Sie wird zu einer Stonewall-Transaktion, die mehrere Ihrer UTXOs als Inputs verbraucht und zwei Outputs mit identischen Beträgen erzeugt, von denen einer der tatsächlichen Zahlung von "100.000 sats" entspricht, zusätzlich zu den Austausch-Outputs.



![Image](assets/fr/09.webp)



Wenn alles korrekt ist, klicken Sie auf "Transaktion erstellen".



Sie können dann Ihre Transaktionsdetails ein letztes Mal überprüfen und auf "Transaktion zur Unterzeichnung abschließen" klicken.



![Image](assets/fr/10.webp)



Unterschreiben Sie dann die Transaktion nach der für Ihr Portfolio spezifischen Methode und klicken Sie auf `Broadcast Transaction`, um sie im Bitcoin Netzwerk zu verbreiten und eine Bestätigung zu erwarten.



![Image](assets/fr/11.webp)



Sie wissen nun, wie eine Stonewall-Transaktion auf Sparrow Wallet funktioniert und wie man eine solche erstellt. Um Ihre Beherrschung dieser Werkzeuge zur Stärkung Ihrer Onchain-Vertraulichkeit zu vertiefen, lade ich Sie ein, mein BTC 204-Training auf der Plan ₿ Academy zu besuchen:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c