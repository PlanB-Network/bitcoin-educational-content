---
term: BIP0093
---

Informační BIP, který navrhuje standard pro ukládání a obnovu seed hierarchického deterministického portfolia (podle BIP32) pomocí Shamirova tajného sdílení klíčů. Tento protokol definuje formát "codex32", který je inspirován formátem bech32, zavedením strukturovaného řetězce sestávajícího z prefixu, prahového parametru, identifikátoru, indexu sdílení, užitečného zatížení a kontrolního součtu (BCH). Metoda umožňuje rozdělit seed až na 31 sdílení, z nichž pro úplné obnovení seed je vyžadován definovaný práh (mezi 1 a 9).