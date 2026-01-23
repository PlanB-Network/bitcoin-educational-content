---
term: BIP0381

definition: Funktionen pk(), pkh() und sh() zur Beschreibung von Legacy-Skripten in Descriptoren.
---
Einführung von Funktionen für Deskriptoren, insbesondere `pk(KEY)` (Pay-to-PubKey), `pkh(KEY)` (Pay-to-PubKey-Hash), und `sh(SCRIPT)` (Pay-to-Script-Hash). Diese Funktionen standardisieren die Art und Weise, wie Legacy-Skripttypen in Deskriptoren beschrieben werden. BIP381 wurde zusammen mit allen anderen deskriptorbezogenen BIPs (außer BIP386) in Version 0.17 von Bitcoin Core implementiert.