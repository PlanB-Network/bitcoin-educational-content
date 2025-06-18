---
term: BIP0141
---

Uveo je koncept Segregated Witness (SegWit) koji je dao ime SegWit Soft Fork. BIP141 uvodi veliku modifikaciju u Bitcoin protokol s ciljem rešavanja problema promenljivosti transakcija. SegWit odvaja svedoka (podatke o potpisu) od ostatka podataka o transakciji. Ovo razdvajanje se postiže ubacivanjem svedoka u zasebnu strukturu podataka, koja se beleži u novom Merkle Tree, koji je sam po sebi referenciran u bloku putem Coinbase Transaction, čineći SegWit kompatibilnim sa starijim verzijama protokola.