---
term: BLOK
---

Datová struktura v systému Bitcoin. Blok obsahuje sadu platných transakcí a metadata obsažená v jeho hlavičce. Každý blok je propojen s následujícím pomocí hash hodnoty své hlavičky, čímž vzniká blockchain. Blockchain funguje jako časové razítko, které umožňuje každému uživateli znát všechny minulé transakce, aby mohl ověřit neexistenci transakce a zabránit dvojímu utrácení. Transakce jsou organizovány do Merkleova stromu. Tento kryptografický akumulátor umožňuje vytvoření souhrnu všech transakcí v bloku, nazývaného "Merkleův kořen". Hlavička bloku obsahuje 6 prvků:
* Verze bloku;
* Otisk předchozího bloku;
* Kořen Merkleova stromu transakcí;
* Časové razítko bloku;
* Cílová obtížnost;
* Nonce.

Aby byl blok platný, musí mít hlavičku, která po zahashování pomocí `SHA256d` produkuje digest, který je menší nebo roven cílové obtížnosti.