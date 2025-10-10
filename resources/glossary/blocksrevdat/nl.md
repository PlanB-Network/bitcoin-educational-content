---
term: BLOKKEN/REV*.DAT
---

Naam van de bestanden in Bitcoin core die de informatie opslaan die nodig is om mogelijk de veranderingen terug te draaien die gemaakt zijn in de UTXO set door eerder toegevoegde blokken. Elk bestand wordt geïdentificeerd door een uniek nummer dat hetzelfde is als het blk*.dat bestand waar het mee correspondeert. De rev*.dat bestanden bevatten de omkeergegevens die corresponderen met de blokken die zijn opgeslagen in de blk*.dat bestanden. Deze gegevens zijn in wezen een lijst van alle UTXO's die in een blok als ingang zijn gebruikt. Met deze omkeerbestanden kan het knooppunt terugkeren naar een vorige toestand in het geval van een Blockchain reorganisatie waardoor eerder gevalideerde blokken worden weggegooid.