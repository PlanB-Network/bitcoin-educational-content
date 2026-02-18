---
term: Eltoo
definition: Protocol dat het beheer van Lightning-kanaalstatussen vereenvoudigt met een lineaire update-aanpak.
---

Een algemeen protocol voor de tweede lagen van Bitcoin dat definieert hoe de Ownership van een UTXO gezamenlijk beheerd moet worden. Eltoo is ontworpen door Christian Decker, Rusty Russell en Olaoluwa Osuntokun, in het bijzonder om de problemen op te lossen die samenhangen met de onderhandelingsmechanismen van Lightning kanaaltoestanden, dat wil zeggen, tussen openen en sluiten. De Eltoo architectuur vereenvoudigt het onderhandelingsproces door een lineair toestandsbeheersysteem te introduceren, waarbij de gevestigde op straffen gebaseerde aanpak wordt vervangen door een flexibelere en minder bestraffende updatemethode. Dit protocol vereist het gebruik van een nieuw type SigHash dat het mogelijk maakt om alle inputs in de handtekening van een transactie te negeren. Deze SigHash heette aanvankelijk `SIGHASH_NOINPUT`, daarna `SIGHASH_ANYPREVOUT` (*Any Previous Output*). De implementatie is gepland in BIP118.


> ► *Eltoo wordt soms ook "LN-Symmetrie" genoemd.*