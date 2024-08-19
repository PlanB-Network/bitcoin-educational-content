---
term: UTXO SET
---

Bezieht sich auf die Sammlung aller existierenden UTXOs zu einem beliebigen Zeitpunkt. Mit anderen Worten, es ist eine große Liste aller verschiedenen Bitcoin-Beträge, die darauf warten, ausgegeben zu werden. Wenn man die Beträge aller UTXOs im UTXO-Set zusammenzählt, ergibt das die gesamte monetäre Masse der im Umlauf befindlichen Bitcoins. Jeder Knoten im Bitcoin-Netzwerk hält sein eigenes UTXO-Set in Echtzeit vor. Es wird aktualisiert, sobald neue gültige Blöcke bestätigt werden, mit den darin enthaltenen Transaktionen, die einige UTXOs aus dem UTXO-Set verbrauchen und im Gegenzug neue erstellen.

Dieses UTXO-Set wird von jedem Knoten vorgehalten, um schnell zu überprüfen, ob die in Transaktionen ausgegebenen UTXOs tatsächlich legitim sind. Dies ermöglicht es ihnen, Versuche des doppelten Ausgebens zu erkennen und abzulehnen. Das UTXO-Set steht oft im Mittelpunkt der Bedenken hinsichtlich der Dezentralisierung von Bitcoin, da seine Größe natürlich sehr schnell zunimmt. Da ein Teil davon im RAM gehalten werden muss, um Transaktionen in einer angemessenen Zeit zu verifizieren, könnte das UTXO-Set nach und nach den Betrieb eines vollständigen Knotens zu kostspielig machen. Das UTXO-Set hat auch einen erheblichen Einfluss auf den IBD (*Initial Block Download*). Je mehr vom UTXO-Set im RAM platziert werden kann, desto schneller ist der IBD. Bei Bitcoin Core wird das UTXO-Set im Ordner `/chainstate` gespeichert.

> ► *Auf Englisch könnte "UTXO set" als "UTXO-Set" übersetzt werden.*