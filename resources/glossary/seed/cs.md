---
term: GRAIN
---

Ve specifickém kontextu hierarchického deterministického portfolia Bitcoin je seed 512bitová informace odvozená z náhodné události. Používá se k deterministickému a hierarchickému generate souboru soukromých klíčů a jim odpovídajících veřejných klíčů pro portfolio Bitcoin. seed je často zaměňován se samotnou frází pro obnovu. Není to však totéž. Frázi seed získáme aplikací funkce `PBKDF2` na frázi Mnemonic a libovolnou frázi passphrase.


seed byl vynalezen společně s BIP32, který definoval základy hierarchického deterministického portfolia. V tomto standardu měřil seed 128 bitů. To umožnilo odvodit všechny klíče v portfoliu z jediné informace, na rozdíl od portfolií JBOK (*Just a Bunch Of Keys*), která vyžadují nové zálohy pro každý generovaný klíč. BIP39 pak navrhl kódování tohoto kódu seed, aby se zjednodušilo jeho čtení lidmi. Toto kódování má podobu fráze, obecně označované jako fráze Mnemonic nebo fráze pro obnovu. Tento standard zabraňuje chybám při ukládání seed, zejména díky použití kontrolního součtu.


Mimo kontext Bitcoin je v kryptografii obecně seed počáteční hodnota používaná pro kryptografické klíče generate nebo obecněji pro jakýkoli typ dat vytvořených generátorem pseudonáhodných čísel. Tato počáteční hodnota musí být náhodná a nepředvídatelná, aby byla zaručena bezpečnost kryptografického systému. seed skutečně vnáší do systému entropii, ale následný proces generování je deterministický.


> ► *V běžném jazyce většina bitcoinářů mluví o frázi Mnemonic, když hovoří o "seed", a nikoli o mezistavu derivace, který leží mezi frází Mnemonic a hlavním klíčem.*