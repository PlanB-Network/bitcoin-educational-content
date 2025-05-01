---
term: BATTERIE
---

Im Zusammenhang mit der Skriptsprache, die verwendet wird, um Bitcoin UTXOs mit Ausgabenbedingungen zu versehen, ist der Stapel eine LIFO (*Last In, First Out*) Datenstruktur, die verwendet wird, um temporäre Elements während der Skriptausführung zu speichern. Jede Operation im Skript manipuliert diese Stapel, wobei Elements hinzugefügt (*push*) oder entfernt (*pop*) werden können. Skripte verwenden Stapel, um Ausdrücke auszuwerten, temporäre Variablen zu speichern und Bedingungen zu verwalten.


Bei der Ausführung eines Bitcoin-Skripts können 2 Stapel verwendet werden: der Hauptstapel und der Alt-Stapel (alternativ). Der Hauptstapel wird für die Mehrzahl der Skriptoperationen verwendet. Auf diesem Stapel werden bei Skriptoperationen Daten hinzugefügt, entfernt oder manipuliert. Der alternative Stack hingegen wird verwendet, um Daten während der Skriptausführung vorübergehend zu speichern. Mit bestimmten Opcodes wie `OP_TOALTSTACK` und `OP_FROMALTSTACK` können Sie Elements vom Hauptstapel auf den alternativen Stapel und umgekehrt übertragen.


Wenn beispielsweise eine Transaktion validiert wird, werden Signaturen und öffentliche Schlüssel auf den Hauptstapel geschoben und durch aufeinander folgende Opcodes verarbeitet, um zu überprüfen, ob die Signaturen mit den Transaktionsschlüsseln und -daten übereinstimmen.