---
term: Initiële block download (IBD)
definition: Proces van het downloaden en verifiëren van de blockchain bij het opstarten van een nieuwe node.
---

Verwijst naar het proces waarbij een knooppunt de Blockchain downloadt en verifieert uit het Genesis blok, en synchroniseert met andere knooppunten in het Bitcoin netwerk. IBD moet worden uitgevoerd bij het lanceren van een nieuwe Full node. Aan het begin van deze initiële synchronisatie heeft het knooppunt geen informatie over eerdere transacties. Daarom downloadt het elk blok van andere knooppunten in het netwerk, controleert de geldigheid en voegt het dan toe aan zijn lokale versie van de Blockchain. Het is de moeite waard om op te merken dat IBD lang kan duren en veel middelen kan vergen vanwege de toenemende grootte van de Blockchain en UTXO verzameling. De snelheid van de uitvoering hangt af van de rekencapaciteit van de computer die het knooppunt host, de RAM capaciteit, de snelheid van het opslagapparaat en de bandbreedte. Om je een idee te geven: als je een krachtige internetverbinding hebt en het knooppunt wordt gehost op de nieuwste MacBook met veel RAM, dan duurt de IBD maar een paar uur. Als je daarentegen een microcomputer zoals een Raspberry Pi gebruikt, kan de IBD een week of meer duren.


