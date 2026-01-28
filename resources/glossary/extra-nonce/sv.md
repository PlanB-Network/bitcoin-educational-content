---
term: Extra-nonce
definition: Fält i coinbase som gör det möjligt att utöka sökutrymmet bortom den klassiska noncen för brytning.
---

Fält som används i `scriptSig` för ett blocks Coinbase Transaction, vilket gör att ett större antal möjligheter kan testas för att få en Hash som är lägre än svårighetsmålet, utöver den klassiska Nonce, som finns direkt i rubriken för varje block.


Genom att ändra extra-Nonce i Coinbase Transaction ändras identifieraren för denna transaktion, och därmed Merkle Root för alla transaktioner i blocket, vilket också ändrar blockhuvudet. Detta gör att Miner kan fortsätta att söka efter hashkoder när den klassiska Nonce:s räckvidd redan är uttömd, utan att ändra strukturen på sitt kandidatblock.


I Mining-pooler är extra-Nonce ofta uppdelad i två delar: en som genereras av poolen för att identifiera varje chopper, och en som modifieras av choppern i sökandet efter en giltig share. Detta gör att de olika chopparna i poolen kan arbeta samtidigt på samma kandidatblock med hela nonces-intervallet, utan att duplicera samma arbete på poolnivå.