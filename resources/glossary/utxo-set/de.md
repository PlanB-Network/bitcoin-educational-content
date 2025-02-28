---
term: UTXO SET

---
Bezieht sich auf die Sammlung aller vorhandenen UTXOs zu einem bestimmten Zeitpunkt. Mit anderen Worten, es handelt sich um eine große Liste aller verschiedenen Bitcoin-Stücke, die darauf warten, ausgegeben zu werden. Wenn man die Beträge aller UTXOs im UTXO-Set zusammenzählt, erhält man die gesamte monetäre Masse der im Umlauf befindlichen Bitcoins. Jeder Knoten im Bitcoin-Netzwerk verwaltet sein eigenes UTXO-Set in Echtzeit. Er aktualisiert es, wenn neue gültige Blöcke bestätigt werden, mit den darin enthaltenen Transaktionen, die einige UTXOs aus dem UTXO-Set verbrauchen und im Gegenzug neue erzeugen.

Dieser UTXO-Satz wird von jedem Knoten aufbewahrt, um schnell überprüfen zu können, ob die in Transaktionen ausgegebenen UTXOs tatsächlich rechtmäßig sind. Dies ermöglicht es ihnen, Versuche von Doppelausgaben zu erkennen und zurückzuweisen. Der UTXO-Satz steht oft im Mittelpunkt der Bedenken über die Dezentralisierung von Bitcoin, da seine Größe natürlich sehr schnell ansteigt. Da ein Teil davon im RAM gehalten werden muss, um Transaktionen in einer angemessenen Zeit zu verifizieren, könnte der UTXO-Satz den Betrieb eines kompletten Knotens allmählich zu kostspielig machen. Der UTXO-Satz hat auch einen erheblichen Einfluss auf den IBD (*Initial Block Download*). Je mehr des UTXO-Sets im RAM platziert werden kann, desto schneller ist der IBD. Auf Bitcoin Core wird das UTXO-Set im Ordner `/chainstate` gespeichert.

> ► *Im Englischen könnte "UTXO set" mit "UTXO set" übersetzt werden