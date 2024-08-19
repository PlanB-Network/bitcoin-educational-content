---
term: ANCHORS.DAT
---

Datei, die im Bitcoin Core Client verwendet wird, um die IP-Adressen von ausgehenden Knoten zu speichern, mit denen ein Client verbunden war, bevor er heruntergefahren wurde. Anchors.dat wird somit jedes Mal erstellt, wenn der Knoten gestoppt wird, und gelöscht, wenn er neu gestartet wird. Die Knoten, deren IP-Adressen in dieser Datei enthalten sind, werden genutzt, um schnell Verbindungen herzustellen, wenn der Knoten neu gestartet wird.