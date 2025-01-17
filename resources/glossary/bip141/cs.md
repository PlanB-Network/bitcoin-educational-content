---
term: BIP141

---
Zavedl koncept Segregated Witness (SegWit), který dal jméno soft forku SegWit. BIP141 zavádí zásadní úpravu protokolu Bitcoin, jejímž cílem je vyřešit problém s podvržením transakcí. SegWit odděluje svědka (podpisové údaje) od ostatních transakčních údajů. Tohoto oddělení je dosaženo vložením svědků do samostatné datové struktury, odevzdané v novém Merklově stromu, který je sám odkazován v bloku prostřednictvím transakce coinbase, díky čemuž je SegWit kompatibilní se staršími verzemi protokolu.