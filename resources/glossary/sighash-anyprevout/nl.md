---
term: SIGHASH_ANYPREVOUT
definition: SigHash-voorstel waardoor de handtekening niet aan een specifieke UTXO hoeft te worden gekoppeld.
---

Voorstel voor de implementatie van een nieuwe SigHash Flag modifier in Bitcoin, geïntroduceerd met BIP118. `SIGHASH_ANYPREVOUT` maakt meer flexibiliteit in transactiebeheer mogelijk, vooral voor geavanceerde toepassingen zoals betaalkanalen op de Lightning Network en de Eltoo update. De `SIGHASH_ANYPREVOUT` maakt het mogelijk om de handtekening niet te binden aan een specifieke voorgaande UTXO (*Any Previous Output*). Gebruikt in combinatie met `SIGHASH_ALL`, zou het toestaan om alle uitvoer van een transactie te ondertekenen, maar geen van de invoer. Dit zou het hergebruik van de handtekening voor verschillende transacties mogelijk maken, zolang aan bepaalde voorwaarden wordt voldaan.


> ► *De SigHash modifier SIGHASH_ANYPREVOUT is afgeleid van het idee van SIGHASH_NOINPUT, oorspronkelijk voorgesteld door Joseph Poon in 2016 om zijn concept van de Lightning Network.* te verbeteren