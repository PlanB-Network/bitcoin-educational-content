---
term: BIP22

---
BIP wurde 2012 von Luke Dashjr vorgeschlagen und führt eine standardisierte JSON-RPC-Methode für externe Mining-Schnittstellen ein, die "getblocktemplate" genannt wird. Mit dem Anstieg der Mining-Schwierigkeit hat sich die Verwendung von spezialisierter externer Software für die Erstellung von Arbeitsnachweisen entwickelt. Dieses BIP schlägt einen gemeinsamen Kommunikationsstandard für die Blockvorlage zwischen den Vollknoten und der auf das Mining spezialisierten Software vor. Bei dieser Methode wird die gesamte Struktur des Blocks und nicht nur der Header übermittelt, damit der Miner ihn anpassen kann.