---
term: RBF (REPLACE-BY-FEE)

---
Ein Transaktionsmechanismus, der es dem Absender ermöglicht, eine Transaktion durch eine andere zu ersetzen, indem er höhere Gebühren zahlt, um deren Bestätigung zu beschleunigen. Wenn eine Transaktion mit zu niedrigen Gebühren stecken bleibt, kann der Absender *Replace-By-Fee* verwenden, um die Gebühren zu erhöhen und seine Ersatztransaktion in den Mempools zu priorisieren.

RBF ist anwendbar, solange sich die Transaktion in den Mempools befindet; sobald sie in einem Block ist, kann sie nicht mehr ersetzt werden. Beim ersten Senden muss die Transaktion angeben, dass sie ersetzt werden kann, indem sie den Wert für `nSequence` auf eine Zahl kleiner als `0xfffffffe` einstellt. Dies wird als RBF-"Flag" bezeichnet. Diese Einstellung signalisiert die Möglichkeit, die Transaktion zu aktualisieren, nachdem sie ausgestrahlt wurde, so dass anschließend ein RBF möglich ist. Allerdings ist es manchmal möglich, eine Transaktion zu ersetzen, die kein RBF signalisiert hat. Knoten, die den Konfigurationsparameter `mempoolfullrbf=1` verwenden, akzeptieren diese Ersetzung, auch wenn RBF ursprünglich nicht signalisiert wurde.

Im Gegensatz zu CPFP (*Child Pays For Parent*), bei dem der Empfänger die Möglichkeit hat, die Transaktion zu beschleunigen, kann der Absender bei RBF (*Replace-By-Fee*) die Initiative ergreifen, um seine eigene Transaktion zu beschleunigen, indem er die Gebühren erhöht.