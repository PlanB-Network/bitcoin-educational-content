---
term: BIP383

---
Führt die Funktionen `multi(NUM, KEY, ..., KEY)` und `sortedmulti(NUM, KEY, ..., KEY)` für Deskriptoren ein. Diese Funktionen ermöglichen die Beschreibung von Multisignatur-Skripten in den Deskriptoren, wobei `sortedmulti` die öffentlichen Schlüssel in lexikographischer Reihenfolge sortiert, um Kompatibilität beim Import zu gewährleisten. BIP383 wurde zusammen mit allen anderen deskriptorbezogenen BIPs (außer BIP386) in Version 0.17 von Bitcoin Core implementiert.