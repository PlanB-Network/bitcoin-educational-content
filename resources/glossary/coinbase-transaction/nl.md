---
term: Coinbase-transactie
definition: Eerste transactie van een blok gemaakt door de miner om de blokbeloning en subsidie te ontvangen.
---

De Coinbase Transaction is een speciale en unieke transactie die in elk blok van de Bitcoin Blockchain zit. Het vertegenwoordigt de eerste transactie van een blok en wordt aangemaakt door de Miner die met succes een header heeft gevonden die de Proof of Work (*Proof-of-Work*) valideert, dat wil zeggen, kleiner dan of gelijk aan het doel.


De Coinbase Transaction dient voornamelijk twee doelen: het toekennen van de Block reward aan de Miner en het toevoegen van nieuwe eenheden bitcoins aan het circulerende geld Supply. De Block reward is de economische stimulans voor mijnwerkers om Proof of Work te gebruiken. De Block reward, de economische stimulans voor mijnwerkers om Proof of Work te gebruiken, omvat de geaccumuleerde vergoedingen voor de transacties in het blok en een bepaald bedrag aan nieuw gecreëerde bitcoins ex-nihilo (bloksubsidie). Dit bedrag, aanvankelijk vastgesteld op 50 bitcoins per blok in 2009, wordt elke 210.000 blokken (ongeveer elke 4 jaar) gehalveerd tijdens een gebeurtenis die "Halving" wordt genoemd


De Coinbase Transaction verschilt op verschillende manieren van gewone transacties. Ten eerste heeft het geen invoer, wat betekent dat er geen bestaande transactie uitvoer (UTXO) door verbruikt wordt. Vervolgens bevat het handtekeningscript (`scriptSig`) voor de Coinbase Transaction meestal een willekeurig veld waarin aanvullende gegevens kunnen worden opgenomen, zoals aangepaste berichten of Mining softwareversie-informatie. Tenslotte zijn de bitcoins die gegenereerd worden door de Coinbase Transaction onderworpen aan een looptijd van 100 blokken (101 bevestigingen) voordat ze uitgegeven kunnen worden, om te voorkomen dat niet-bestaande bitcoins uitgegeven worden in het geval van een reorganisatie van de keten.


