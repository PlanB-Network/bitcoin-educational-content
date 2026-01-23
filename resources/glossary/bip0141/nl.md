---
term: BIP0141
definition: Introductie van SegWit (Segregated Witness), waarbij handtekeningen worden gescheiden van de rest van de transactie om kneedbaarheid (malleability) op te lossen.
---

Introduceerde het concept van Segregated Witness (SegWit) dat zijn naam gaf aan SegWit Soft Fork. BIP141 introduceert een belangrijke wijziging aan het Bitcoin protocol, gericht op het oplossen van het probleem van de manipuleerbaarheid van transacties. SegWit scheidt de getuige (handtekeninggegevens) van de rest van de transactiegegevens. Deze scheiding wordt bereikt door de getuigen in een aparte datastructuur in te voegen, vastgelegd in een nieuwe Merkle Tree, waarnaar zelf in het blok verwezen wordt via de Coinbase Transaction, waardoor SegWit compatibel is met oudere versies van het protocol.