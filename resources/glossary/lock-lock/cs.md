---
term: LOCK (.LOCK)

---
Soubor používaný v jádře bitcoinu k uzamčení datového adresáře. Vytváří se při spuštění bitcoind nebo Bitcoin-qt, aby se zabránilo současnému přístupu více instancí softwaru do stejného datového adresáře. Cílem je zabránit konfliktům a poškození dat. Pokud se software neočekávaně zastaví, může soubor .lock zůstat a před opětovným spuštěním jádra Bitcoin jej musíte ručně odstranit.