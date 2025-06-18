---
term: GOSSIP
---

Gossip ist ein verteilter Peer-to-Peer-Algorithmus (P2P) für die epidemische Verbreitung von Informationen an alle Netzakteure. Bei Bitcoin, Lightning und anderen verteilten Systemen ermöglicht dieses Protokoll den Austausch und die Synchronisierung der Global State von Knoten in nur wenigen Zyklen. Jeder Knoten gibt Informationen an einen oder mehrere zufällige oder nicht zufällige Nachbarn weiter, die wiederum die Informationen an andere Nachbarn weitergeben, und so weiter, bis ein global synchronisierter Zustand erreicht ist.


In Lightning ist Gossip ein Kommunikationsprotokoll zwischen Knoten, um Informationen über den aktuellen Zustand und die Topologie des Netzes auszutauschen. Das Gossip-Protokoll ermöglicht es den Knoten, den dynamischen Zustand von Zahlungskanälen und anderen Knoten zu kennen, um die Weiterleitung von Transaktionen über das Netzwerk zu erleichtern, ohne dass direkte Verbindungen zwischen allen Knoten erforderlich sind.


> ► *Im Französischen könnte "gossip protocol" mit "protocole de bavardage" übersetzt werden. Quelle : https://dl.acm.org/doi/pdf/10.1145/41840.41841.*