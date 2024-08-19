---
term: MEMPOOL
---

Eine Zusammenziehung der Begriffe "memory" (Speicher) und "pool" (Pool). Dies bezieht sich auf einen virtuellen Raum, in dem Bitcoin-Transaktionen, die auf die Aufnahme in einen Block warten, zusammengefasst werden. Wenn eine Transaktion erstellt und im Bitcoin-Netzwerk verbreitet wird, wird sie zunächst von den Knoten des Netzwerks verifiziert. Wird sie als gültig erachtet, wird sie dann in den Mempool jedes Knotens platziert, wo sie verbleibt, bis sie von einem Miner ausgewählt wird, um in einen Block aufgenommen zu werden.

Es ist wichtig zu beachten, dass jeder Knoten im Bitcoin-Netzwerk seinen eigenen Mempool unterhält und daher zu jedem Zeitpunkt Variationen im Inhalt des Mempools zwischen verschiedenen Knoten geben kann. Insbesondere ermöglicht der `maxmempool`-Parameter in der `bitcoin.conf`-Datei jedes Knotens den Betreibern, die Menge an RAM (Random Access Memory), die ihr Knoten verwenden wird, um ausstehende Transaktionen im Mempool zu speichern, zu steuern. Durch Begrenzung der Größe des Mempools können Knotenbetreiber verhindern, dass er zu viele Ressourcen auf ihrem System verbraucht. Dieser Parameter wird in Megabyte (MB) angegeben. Der Standardwert für Bitcoin Core beträgt bis heute 300 MB.

Transaktionen, die sich im Mempool befinden, sind vorläufig. Sie sollten nicht als unveränderlich betrachtet werden, bis sie in einen Block aufgenommen wurden und nach einer bestimmten Anzahl von Bestätigungen. Diese können oft ersetzt oder gelöscht werden.