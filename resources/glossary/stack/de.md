---
term: STACK
---

Im Kontext der Skriptsprache, die verwendet wird, um Ausgabenbedingungen auf Bitcoin UTXOs anzuwenden, ist der Stack eine "LIFO" (*Last In, First Out*) Datenstruktur, die dazu dient, temporäre Elemente während der Ausführung eines Skripts zu speichern. Jede Operation im Skript manipuliert diese Stacks, wobei Elemente hinzugefügt (*push*) oder entfernt (*pop*) werden können. Skripte verwenden Stacks, um Ausdrücke zu bewerten, temporäre Variablen zu speichern und Bedingungen zu verwalten.

Während der Ausführung eines Bitcoin-Skripts können 2 Stacks verwendet werden: der Hauptstack und der Alt (alternative) Stack. Der Hauptstack wird für die Mehrheit der Operationen eines Skripts verwendet. Auf diesem Stack werden Skriptoperationen Daten hinzufügen, entfernen oder manipulieren. Der alternative Stack dient andererseits dazu, Daten während der Ausführung des Skripts temporär zu speichern. Spezifische Opcodes, wie `OP_TOALTSTACK` und `OP_FROMALTSTACK`, ermöglichen den Transfer von Elementen vom Hauptstack zum alternativen Stack und umgekehrt.

Zum Beispiel werden während der Validierung einer Transaktion Signaturen und öffentliche Schlüssel auf den Hauptstack gepusht und durch aufeinanderfolgende Opcodes verarbeitet, um zu überprüfen, ob die Signaturen mit den Schlüsseln und den Transaktionsdaten übereinstimmen.

> ► *Auf Englisch wird « pile » als « stack » übersetzt. Der englische Begriff wird sogar in technischen Diskussionen im Französischen allgemein verwendet.*