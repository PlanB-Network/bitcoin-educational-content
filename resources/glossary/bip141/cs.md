---
term: BIP141
---

Zavedl koncept Segregated Witness (SegWit), který dal jméno soft forku SegWit. BIP141 představuje významnou modifikaci protokolu Bitcoin, která má za cíl vyřešit problém s mutovatelností transakcí. SegWit odděluje svědectví (data podpisu) od zbytku transakčních dat. Toto oddělení je dosaženo vložením svědectví do samostatné datové struktury, která je zaznamenána v novém Merkleově stromu, jež je sám odkazován v bloku prostřednictvím coinbase transakce, čímž je SegWit kompatibilní se staršími verzemi protokolu.