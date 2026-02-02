---
term: Bloom filter
definition: Probabilistische datastructuur die het snel testen van lidmaatschap van een verzameling mogelijk maakt, gebruikt in SPV wallets.
---

Een probabilistische gegevensstructuur die wordt gebruikt om te testen of een element deel uitmaakt van een set. Bloom Filters maken snelle lidmaatschapscontroles mogelijk zonder de hele dataset te testen. Ze zijn vooral nuttig in contexten waar ruimte en snelheid kritisch zijn, maar een laag en gecontroleerd foutenpercentage acceptabel is. Bloom Filters produceren namelijk geen valse negatieven, maar ze generate een bepaald aantal valse positieven. Wanneer een element aan het filter wordt toegevoegd, nemen meerdere Hash functies generate posities in een bit-array in. Om te controleren op lidmaatschap worden dezelfde Hash functies gebruikt. Als alle corresponderende bits gezet zijn, zit het element waarschijnlijk in de set, maar met een risico op fout-positieven. Bloom Filters worden veel gebruikt op het gebied van databases en netwerken. Het is met name bekend dat Google ze gebruikt voor zijn gecomprimeerde databasebeheersysteem *BigTable*. In het Bitcoin protocol worden ze met name gebruikt voor SPV wallets volgens BIP37.


> ► *Wanneer specifiek wordt gesproken over het gebruik van Bloom Filters in de context van Bitcoin transacties, wordt soms de term "Transaction Bloom Filtering" gebruikt.*