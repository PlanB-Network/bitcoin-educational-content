---
term: Mempool
---

Een samentrekking van de termen "geheugen" en "pool". Dit verwijst naar een virtuele ruimte waarin Bitcoin transacties die wachten op opname in een blok, gegroepeerd zijn. Wanneer een transactie wordt aangemaakt en uitgezonden op het Bitcoin netwerk, wordt deze eerst geverifieerd door de knooppunten van het netwerk. Als het geldig wordt geacht, wordt het in de Mempool van elk knooppunt geplaatst, waar het blijft totdat het door een Miner wordt geselecteerd om in een blok te worden opgenomen.


Het is belangrijk op te merken dat elk knooppunt in het Bitcoin netwerk zijn eigen Mempool onderhoudt, en daarom kunnen er op elk moment variaties zijn in de inhoud van de Mempool tussen verschillende knooppunten. Met name de `maxmempool` parameter in het `Bitcoin.conf` bestand van elk knooppunt stelt operators in staat om de hoeveelheid RAM (random access memory) te controleren die hun knooppunt zal gebruiken om lopende transacties in de Mempool op te slaan. Door de grootte van de Mempool te beperken, kunnen nodebeheerders voorkomen dat de node te veel bronnen op hun systeem gebruikt. Deze parameter wordt gespecificeerd in megabytes (MB). De standaardwaarde voor Bitcoin core tot nu toe is 300 MB.


Transacties in de Mempool zijn voorlopig. Ze moeten niet als onveranderlijk worden beschouwd totdat ze in een blok zijn opgenomen en na een bepaald aantal bevestigingen. Ze kunnen vaak worden vervangen of gezuiverd.