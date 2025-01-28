---
term: OPAKOVANĚ POUŽITELNÝ PLATEBNÍ KÓD

---
V BIP47 je opakovaně použitelný platební kód statický identifikátor generovaný z peněženky Bitcoin, který umožňuje oznamovací transakci a odvození jedinečných adres. Tím se zamezí opakovanému používání adres, které vede ke ztrátě soukromí, aniž by bylo nutné ručně odvozovat a předávat nové, nepoužívané adresy pro každou platbu. V BIP47 jsou opakovaně použitelné platební kódy konstruovány následujícím způsobem:


- Byte 0 odpovídá verzi;
- Byte 1 je bitové pole pro přidání informací v případě specifického použití;
- Byte 2 udává paritu `y` veřejného klíče;
- Od bajtu 3 do bajtu 34 najdete hodnotu `x` veřejného klíče;
- Od bajtu 35 do bajtu 66 je řetězový kód spojený s veřejným klíčem;
- Od bajtu 67 do bajtu 79 je nulová výplň.

Na začátek platebního kódu se zpravidla přidává část čitelná pro člověka (HRP) a na konec kontrolní součet, který je pak zakódován v bázi58. Konstrukce platebního kódu je tedy dosti podobná konstrukci rozšířeného klíče. Zde je například můj vlastní platební kód BIP47 v base58:

```text
PM8TJSBiQmNQDwTogMAbyqJe2PE2kQXjtgh88MRTxsrnHC8zpEtJ8j7Aj628oUFk8X6P5rJ7P5qD
udE4Hwq9JXSRzGcZJbdJAjM9oVQ1UKU5j2nr7VR5
```

V implementaci PayNym BIP47 lze platební kódy vyjádřit také ve formě identifikátorů spojených s obrazem robota. Zde je například můj:

```text
+throbbingpond8B1
```

Používání platebních kódů s implementací PayNym je v současné době dostupné v aplikaci Sparrow Wallet na počítači a v aplikaci Samourai Wallet na mobilním telefonu.