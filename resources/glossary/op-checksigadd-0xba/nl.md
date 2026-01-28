---
term: OP_CHECKSIGADD (0XBA)
definition: Tapscript-opcode die een handtekening controleert en een teller verhoogt als deze geldig is.
---

Haalt de bovenste drie waarden uit de stack: een `public key`, een `CScriptNum` `n`, en een `signature`. Als de handtekening niet de lege vector is en niet geldig is, eindigt het script met een foutmelding. Als de handtekening geldig is of de lege vector is (`OP_0`), worden twee scenario's gepresenteerd:


- Als de handtekening de lege vector is: een `CScriptNum` met de waarde `n` wordt op de stack geduwd en de uitvoering gaat verder;
- Als de handtekening niet de lege vector is en geldig blijft: een `CScriptNum` met de waarde `n + 1` wordt op de stack geduwd en de uitvoering gaat verder.

Ter vereenvoudiging voert `OP_CHECKSIGADD` een operatie uit die lijkt op `OP_CHECKSIG`, maar in plaats van true of false op de stack te duwen, voegt het `1` toe aan de tweede waarde bovenaan de stack als de handtekening geldig is, of laat het deze waarde onveranderd als de handtekening de lege vector representeert. `OP_CHECKSIGADD` maakt het mogelijk om hetzelfde multisignature beleid in Tapscript te maken als met `OP_CHECKMULTISIG` en `OP_CHECKMULTISIGVERIFY` maar dan op een batch verifieerbare manier, wat betekent dat het opzoekproces in de verificatie van een traditionele Multisig wordt verwijderd en dus de verificatie versnelt terwijl de operationele belasting op de CPU's van de nodes wordt verminderd. Deze opcode is toegevoegd in Tapscript alleen voor de behoeften van Taproot.