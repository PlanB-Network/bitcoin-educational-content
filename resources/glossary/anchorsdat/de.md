---
term: Anchors.dat

---
Datei, die im Bitcoin Core-Client verwendet wird, um die IP-Adressen der ausgehenden Knoten zu speichern, mit denen ein Client verbunden war, bevor er abgeschaltet wurde. Anchors.dat wird also jedes Mal erstellt, wenn der Knoten angehalten wird, und gelöscht, wenn er neu gestartet wird. Die Knoten, deren IP-Adressen in dieser Datei enthalten sind, werden verwendet, um schnell Verbindungen herzustellen, wenn der Knoten neu gestartet wird.