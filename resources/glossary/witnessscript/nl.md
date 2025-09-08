---
term: WITNESSSCRIPT
---

Een script dat de voorwaarden bepaalt waaronder bitcoins kunnen worden uitgegeven van P2WSH of P2SH-P2WSH UTXO's. Typisch bepaalt `witnessScript` de voorwaarden van een Wallet met meerdere handtekeningen onder de SegWit standaard. In deze script standaarden bevat de `scriptPubKey` van de UTXO (de uitvoer) een Hash van het `witnessScript`. Om deze UTXO te gebruiken als invoer in een nieuwe transactie, moet de houder het originele `witnessScript` onthullen, om te bewijzen dat het overeenkomt met de vingerafdruk in de `scriptPubKey`. Het `witnessScript` moet dan worden opgenomen in de `scriptWitness` van de transactie, die ook de Elements bevat die nodig zijn om het script te valideren, zoals handtekeningen. Daarom is het `witnessScript` het equivalent voor SegWit van het `redeemscript` in een P2SH transactie, met het verschil dat het in de getuige van de transactie wordt geplaatst en niet in het `scriptSig`.


> let op, het `witnessScript` moet niet verward worden met het `scriptWitness`. Terwijl het `witnessScript` de bestedingsvoorwaarden van een P2WSH of P2SH-P2WSH UTXO definieert en een script op zichzelf vormt, bevat het `scriptWitness` de getuigegegevens van elke SegWit invoer.*