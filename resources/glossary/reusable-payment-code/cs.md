---
term: OPĚTOVNĚ POUŽITELNÝ PLATEBNÍ KÓD
---

V BIP47 je opětovně použitelný platební kód statický identifikátor generovaný z Bitcoinové peněženky, který umožňuje notifikační transakci a odvození unikátních adres. To umožňuje vyhnout se opětovnému použití adres, což vede ke ztrátě soukromí, aniž by bylo nutné ručně odvozovat a přenášet nové, nepoužité adresy pro každou platbu. V BIP47 jsou opětovně použitelné platební kódy konstruovány následovně:
* Byte 0 odpovídá verzi;
* Byte 1 je bitové pole pro přidání informací v případě specifického použití;
* Byte 2 udává paritu `y` veřejného klíče;
* Od bytu 3 do bytu 34 najdete hodnotu `x` veřejného klíče;
* Od bytu 35 do bytu 66 je zde řetězový kód spojený s veřejným klíčem;
* Od bytu 67 do bytu 79 je nulové vyplnění.

Na začátku platebního kódu je obvykle přidána Část Lidsky Čitelná (HRP) a na konci kontrolní součet, a poté je zakódován v base58. Konstrukce platebního kódu je tedy velmi podobná té u rozšířeného klíče. Zde je můj vlastní BIP47 platební kód v base58 jako příklad:

```text
PM8TJSBiQmNQDwTogMAbyqJe2PE2kQXjtgh88MRTxsrnHC8zpEtJ8j7Aj628oUFk8X6P5rJ7P5qD
udE4Hwq9JXSRzGcZJbdJAjM9oVQ1UKU5j2nr7VR5
```

V implementaci PayNym BIP47 mohou být platební kódy také vyjádřeny ve formě identifikátorů spojených s obrázkem robota. Zde je například můj:

```text
+throbbingpond8B1
```

Použití platebních kódů s implementací PayNym je v současné době dostupné na Sparrow Wallet na PC a na Samourai Wallet na mobilu.