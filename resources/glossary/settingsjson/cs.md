---
term: SETTINGS.JSON

---
Soubor používaný v jádře Bitcoin Core k ukládání nastavení grafického uživatelského rozhraní (GUI). Uchovává informace o uživatelských konfiguracích, jako jsou například otevřené peněženky. Při restartování jádra Bitcoin tento soubor umožňuje automatické znovuotevření peněženek, které byly aktivní před uzavřením aplikace. Pokud je peněženka uzavřena prostřednictvím grafického uživatelského rozhraní, je z tohoto souboru také odstraněna, a proto nebude při dalším spuštění automaticky znovu otevřena.