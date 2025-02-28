---
term: BLOCK

---
Struktura dat v systému Bitcoin. Blok obsahuje sadu platných transakcí a metadata obsažená v jeho záhlaví. Každý blok je spojen s dalším pomocí hashe své hlavičky, čímž vzniká blockchain. Blokový řetězec funguje jako časový server, který umožňuje každému uživateli znát všechny minulé transakce, aby bylo možné ověřit neexistenci transakce a zabránit dvojímu utrácení. Transakce jsou uspořádány do Merkleho stromu. Tento kryptografický akumulátor umožňuje vytvořit digest všech transakcí v bloku, který se nazývá "Merkleho kořen" Záhlaví bloku obsahuje 6 prvků:


- Verze bloku;
- Otisk předchozího bloku;
- Kořen Merklova stromu transakcí;
- Časové razítko bloku;
- Cíl obtížnosti;
- Nonce.

Aby byl blok platný, musí mít hlavičku, která po zaheslování pomocí `SHA256d` dává digest, který je menší nebo roven cílové hodnotě obtížnosti.