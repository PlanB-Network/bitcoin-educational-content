---
term: CHAIN CODE
---

V kontextu hierarchické deterministické (HD) derivace Bitcoinových peněženek je chain code 256-bitová kryptografická sůl používaná k generování dětských klíčů z rodičovského klíče podle standardu BIP32. Chain code se používá ve spojení s rodičovským klíčem a indexem dítěte k deterministickému generování nového páru klíčů (soukromý klíč a veřejný klíč) bez odhalení rodičovského klíče nebo jiných odvozených dětských klíčů.

Takže pro každý pár klíčů existuje unikátní chain code. Chain code je získán buď hašováním seedu peněženky a vzítím pravé poloviny bitů. V tomto případě se mu říká master chain code, spojený s hlavním soukromým klíčem. Alternativně může být získán hašováním rodičovského klíče s jeho rodičovským chain code a indexem, poté se uchovávají pravé bity. To se pak označuje jako dětský chain code.

Bez znalosti chain code spojeného s každým rodičovským párem není možné odvodit klíče. Do procesu derivace zavádí pseudo-náhodná data, aby se zajistilo, že generování kryptografických klíčů zůstane nepředvídatelné pro útočníky, zatímco pro držitele peněženky bude deterministické.

> ► *V angličtině se "code de chaîne" nazývá "chain code" a "code de chaîne maître" se nazývá "master chain code".*