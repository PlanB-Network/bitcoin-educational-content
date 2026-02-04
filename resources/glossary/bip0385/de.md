---
term: BIP0385

definition: Funktionen addr() und raw() zur Beschreibung von Output-Skripten nach Adresse oder in Hexadezimalform in Descriptoren.
---
Führt die Deskriptorfunktionen `addr(ADDR)` und `raw(HEX)` ein. Die Funktion `addr(ADDR)` ermöglicht die Beschreibung eines Ausgabeskripts durch eine Empfangsadresse, während die Funktion `raw(HEX)` die Angabe eines Ausgabeskripts durch eine rohe hexadezimale Darstellung dieses Skripts ermöglicht. BIP385 wurde zusammen mit allen anderen deskriptorbezogenen BIPs (außer BIP386) in Version 0.17 von Bitcoin Core implementiert.