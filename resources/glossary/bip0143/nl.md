---
term: BIP0143
---

Introduceert een nieuwe manier om de transactie te hashen voor handtekeningverificatie in post-SegWit scripts. Het doel is om overbodige operaties tijdens de verificatie te minimaliseren en om de waarde van de UTXO's in de invoer op te nemen in de handtekening. Dit lost twee grote problemen op met het originele transactie hashing algoritme:


- De kwadratische groei van het hashen van gegevens met het aantal handtekeningen;
- Het ontbreken van het opnemen van de invoerwaarde in de handtekening, wat een risico vormde voor hardware wallets, vooral met betrekking tot de kennis van gemaakte transactiekosten.

Aangezien de SegWit update, uitgelegd in BIP141, een nieuwe vorm van transacties introduceert waarvan het script niet geverifieerd zal worden door oude knooppunten, maakt BIP143 van de gelegenheid gebruik om Address dit probleem op te lossen zonder dat er een Hard Fork nodig is. Daarom maakt BIP143 deel uit van SegWit Soft Fork.