---
term: BIP31
---

Vorschlag zur Verbesserung der Netzwerkverwaltungsmechanismen durch Bitcoin-Knoten. Vor BIP31 hatten Bitcoin-Knoten keine direkte Möglichkeit zu wissen, ob ihre Peers noch verbunden, betriebsbereit und nicht überlastet waren. BIP31 führte die Verwendung einer `pong` Nachricht ein, als Antwort auf eine `ping` Nachricht, was eine aktive Überprüfung der Konnektivität zwischen Knoten ermöglicht.