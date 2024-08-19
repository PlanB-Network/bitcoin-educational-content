---
term: RBF (REPLACE-BY-FEE)
---

Ein Transaktionsmechanismus, der es dem Sender erlaubt, eine Transaktion durch eine andere zu ersetzen, indem höhere Gebühren gezahlt werden, um deren Bestätigung zu beschleunigen. Wenn eine Transaktion aufgrund zu niedriger Gebühren stecken bleibt, kann der Sender *Replace-By-Fee* nutzen, um die Gebühren zu erhöhen und ihre Ersatztransaktion in den Mempools zu priorisieren.

RBF ist anwendbar, solange die Transaktion in den Mempools ist; einmal in einem Block, kann sie nicht mehr ersetzt werden. Beim ursprünglichen Senden muss die Transaktion ihre Verfügbarkeit zum Ersetzen durch Anpassen des `nSequence`-Wertes auf eine Zahl kleiner als `0xfffffffe` angeben. Dies wird als RBF-"Flag" bezeichnet. Diese Einstellung signalisiert die Möglichkeit, die Transaktion nach ihrer Übertragung zu aktualisieren, was anschließend ein RBF ermöglicht. Es ist jedoch manchmal möglich, eine Transaktion zu ersetzen, die RBF nicht signalisiert hat. Knoten, die den Konfigurationsparameter `mempoolfullrbf=1` verwenden, akzeptieren diesen Ersatz auch, wenn RBF ursprünglich nicht signalisiert wurde.

Im Gegensatz zu CPFP (*Child Pays For Parent*), wo der Empfänger handeln kann, um die Transaktion zu beschleunigen, ermöglicht RBF (*Replace-By-Fee*), dass der Sender die Initiative ergreift, um seine eigene Transaktion durch Erhöhung der Gebühren zu beschleunigen.