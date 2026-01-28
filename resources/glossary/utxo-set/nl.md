---
term: UTXO set
definition: Verzameling van alle bestaande UTXO's op een bepaald moment, bijgehouden door elke node om transacties te verifiëren.
---

Verwijst naar de verzameling van alle bestaande UTXO's op een bepaald moment. Met andere woorden, het is een grote lijst van alle verschillende stukjes bitcoins die wachten om uitgegeven te worden. Als je de bedragen van alle UTXO's in de UTXO set optelt, geeft dat ons de totale monetaire massa van bitcoins in omloop. Elk knooppunt in het Bitcoin netwerk onderhoudt zijn eigen UTXO set in real-time. Het werkt het bij als nieuwe geldige blokken worden bevestigd, met de transacties die ze bevatten, die wat UTXO's uit de UTXO set verbruiken en er nieuwe voor terug creëren.


Deze UTXO set wordt door elk knooppunt bewaard om snel te verifiëren of de UTXO's die in transacties zijn uitgegeven inderdaad legitiem zijn. Hierdoor kunnen ze Double-spending pogingen detecteren en afwijzen. De UTXO set is vaak de kern van de bezorgdheid over de decentralisatie van Bitcoin, omdat de grootte ervan natuurlijk zeer snel toeneemt. Omdat een deel ervan in RAM moet worden bewaard om transacties binnen een redelijke tijd te kunnen verifiëren, zou de UTXO set het gebruik van een Full node geleidelijk aan te duur kunnen maken. De UTXO set heeft ook een significante invloed op de IBD (*Initial Block Download*). Hoe meer van de UTXO set in het RAM kan worden geplaatst, hoe sneller de IBD is. Op Bitcoin core wordt de UTXO set opgeslagen in de map genaamd `/chainstate`.


