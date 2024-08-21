---
term: SETTINGS.JSON
---

Soubor používaný v Bitcoin Core pro ukládání nastavení grafického uživatelského rozhraní (GUI). Uchovává informace o uživatelských konfiguracích, jako jsou například otevřené peněženky. Když je Bitcoin Core restartován, tento soubor umožňuje automatické znovuotevření peněženek, které byly aktivní před zavřením aplikace. Pokud je peněženka zavřena prostřednictvím GUI, je také odstraněna z tohoto souboru a tudíž nebude při dalším spuštění automaticky znovu otevřena.