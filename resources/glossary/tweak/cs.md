---
term: TWEAK
---

V kryptografii znamená "vylepšení" veřejného klíče jeho úpravu pomocí aditivní hodnoty zvané "tweak" tak, aby zůstal použitelný při znalosti původního soukromého klíče i tohoto vylepšení. Technicky vzato je tweak skalární hodnota, která se přidává k původnímu veřejnému klíči. Pokud je $P$ veřejný klíč a $t$ je tweak, pak se z tweakovaného veřejného klíče stane :


$$
P' = P + tG
$$


Kde $G$ je generátor použité eliptické křivky. Tato operace vytváří nový veřejný klíč odvozený od původního, přičemž zachovává určité kryptografické vlastnosti, které umožňují jeho použití. Tato metoda se používá například pro adresy Taproot (P2TR), aby bylo možné vydávat buď předložením Schnorrova podpisu tradičním způsobem, nebo splněním jedné z podmínek stanovených v Merkle Tree, známém také jako "MAST".