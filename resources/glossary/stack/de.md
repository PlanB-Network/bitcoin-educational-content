---
term: STACK

---
Im Zusammenhang mit der Skriptsprache, die verwendet wird, um Ausgabenbedingungen auf Bitcoin UTXOs anzuwenden, ist der Stapel eine "LIFO" (*Last In, First Out*) Datenstruktur, die dazu dient, temporäre Elemente während der Ausführung eines Skripts zu speichern. Jede Operation im Skript manipuliert diese Stapel, wobei Elemente hinzugefügt (*push*) oder entfernt (*pop*) werden können. Skripte verwenden Stapel, um Ausdrücke auszuwerten, temporäre Variablen zu speichern und Bedingungen zu verwalten.

Während der Ausführung eines Bitcoin-Skripts können 2 Stapel verwendet werden: der Hauptstapel und der Alt-Stapel (alternativ). Der Hauptstapel wird für den Großteil der Operationen eines Skripts verwendet. Auf diesem Stack werden bei Skriptoperationen Daten hinzugefügt, entfernt oder manipuliert. Der alternative Stack hingegen dient zur vorübergehenden Speicherung von Daten während der Skriptausführung. Bestimmte Opcodes wie `OP_TOALTSTACK` und `OP_FROMALTSTACK` ermöglichen die Übertragung von Elementen vom Hauptstapel zum alternativen Stapel und umgekehrt.

So werden beispielsweise bei der Validierung einer Transaktion Signaturen und öffentliche Schlüssel auf den Hauptstapel geschoben und durch aufeinanderfolgende Opcodes verarbeitet, um zu überprüfen, ob die Signaturen mit den Schlüsseln und den Transaktionsdaten übereinstimmen.

> ► *Im Englischen ist die Übersetzung von "pile" "Stapel". Der englische Begriff wird im Allgemeinen auch im Französischen bei technischen Diskussionen verwendet.*