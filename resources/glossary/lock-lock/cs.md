---
term: LOCK (.LOCK)
---

Soubor používaný v Bitcoin Core pro uzamčení datového adresáře. Je vytvořen při spuštění bitcoind nebo Bitcoin-qt, aby se zabránilo současnému přístupu více instancí softwaru ke stejnému datovému adresáři. Cílem je zabránit konfliktům a poškození dat. Pokud software neočekávaně skončí, soubor .lock může zůstat a musí být před restartováním Bitcoin Core ručně smazán.