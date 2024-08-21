---
term: WALLET IMPORT FORMAT (WIF)
---

Metoda pro kódování soukromého klíče Bitcoinu tak, aby bylo možné jej snadněji importovat nebo exportovat mezi různými peněženkami. WIF využívá kódování `Base58Check`, které zahrnuje informace o verzi, kompresi odpovídajícího veřejného klíče a kontrolní součet pro detekci chyb při psaní. Soukromý klíč ve formátu WIF začíná znaky `5` pro nekomprimované klíče, nebo `K` a `L` pro komprimované klíče, a obsahuje všechny znaky potřebné pro rekonstrukci původního soukromého klíče. Formát WIF poskytuje standardizovaný způsob přenosu soukromého klíče mezi různými softwary peněženek.