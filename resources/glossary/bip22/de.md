---
term: BIP22
---

BIP, vorgeschlagen im Jahr 2012 von Luke Dashjr, das eine standardisierte JSON-RPC Methode für externe Mining-Schnittstellen einführt, genannt "getblocktemplate". Mit der Zunahme der Mining-Schwierigkeit hat sich die Verwendung von spezialisierter externer Software zur Erzeugung von Proof of Work entwickelt. Dieses BIP schlägt einen gemeinsamen Kommunikationsstandard für die Blockvorlage zwischen Vollknoten und auf Mining spezialisierter Software vor. Diese Methode beinhaltet das Senden der gesamten Struktur des Blocks, anstatt nur des Headers, um dem Miner zu ermöglichen, ihn anzupassen.