---
term: MEMPOOL

---
Eine Zusammenziehung der Begriffe "Speicher" und "Pool". Dies bezieht sich auf einen virtuellen Raum, in dem Bitcoin-Transaktionen, die auf die Aufnahme in einen Block warten, gruppiert werden. Wenn eine Transaktion erstellt und im Bitcoin-Netzwerk verbreitet wird, wird sie zunächst von den Knoten des Netzwerks überprüft. Wenn sie für gültig befunden wird, wird sie im Mempool jedes Knotens abgelegt, wo sie verbleibt, bis sie von einem Miner zur Aufnahme in einen Block ausgewählt wird.

Es ist wichtig anzumerken, dass jeder Knoten im Bitcoin-Netzwerk seinen eigenen Mempool unterhält, und daher kann der Inhalt des Mempools zwischen verschiedenen Knoten zu jeder Zeit variieren. Der Parameter "maxmempool" in der Datei "bitcoin.conf" eines jeden Knotens ermöglicht es den Betreibern, die Menge an RAM (Random Access Memory) zu kontrollieren, die ihr Knoten verwendet, um anstehende Transaktionen im Mempool zu speichern. Durch die Begrenzung der Größe des Mempools können Knotenbetreiber verhindern, dass er zu viele Ressourcen auf ihrem System verbraucht. Dieser Parameter wird in Megabytes (MB) angegeben. Der Standardwert für Bitcoin Core ist bis heute 300 MB.

Die im Mempool vorhandenen Transaktionen sind vorläufig. Sie sind erst dann als unveränderlich zu betrachten, wenn sie in einen Block aufgenommen wurden und eine bestimmte Anzahl von Bestätigungen erfolgt ist. Sie können oft ersetzt oder gelöscht werden.