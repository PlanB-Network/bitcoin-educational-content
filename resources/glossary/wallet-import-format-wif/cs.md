---
term: FORMÁT IMPORTU PENĚŽENKY (WIF)

---
Metoda kódování soukromého klíče Bitcoinu tak, aby jej bylo možné snadněji importovat nebo exportovat mezi různými peněženkami. WIF je založen na kódování `Base58Check`, které obsahuje informace o verzi, kompresi příslušného veřejného klíče a kontrolní součet pro detekci chyb při psaní. Soukromý klíč WIF začíná znaky `5` pro nekomprimované klíče nebo `K` a `L` pro komprimované klíče a obsahuje všechny znaky potřebné k rekonstrukci původního soukromého klíče. Formát WIF poskytuje standardizovaný prostředek pro přenos soukromého klíče mezi různými softwary peněženek.