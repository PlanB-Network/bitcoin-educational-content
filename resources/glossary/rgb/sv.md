---
term: RGB
definition: Decentraliserat och konfidentiellt system för smarta kontrakt som körs på Bitcoin.
---

Decentraliserat, konfidentiellt Smart contract-system utformat för att fungera med Bitcoin och Lightning Network. RGB fungerar enligt en Client-side Validation-modell och separerar lagringen av Contract State från Blockchain, så att endast kryptografiska åtaganden sparas i den. På detta sätt hålls hela tillståndshistoriken utanför kedjan, vilket möjliggör större skalbarhet och konfidentialitet. RGB gör det därmed möjligt att skapa komplexa kontrakt för att lagra tokens, NFT:er, decentraliserade identiteter eller DeFi-lösningar, direkt ovanpå Bitcoin.


På RGB säkerställs motståndet mot Double-spending genom användning av Single-Use Seal, en kryptografisk mekanism som utnyttjar det faktum att UTXO:er på Bitcoin endast kan användas en gång. När det gäller token:s äkthet garanteras detta genom verifiering på klientsidan av tillståndshistoriken, från Contract:s skapande till dess senaste tillstånd.