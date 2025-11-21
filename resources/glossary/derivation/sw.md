---
term: DERIVATION
---

Inarejelea mchakato wa kuzalisha jozi za vitufe vya mtoto kutoka kwa jozi ya ufunguo wa mzazi (ufunguo wa faragha na ufunguo wa umma) na msimbo wa mnyororo ndani ya uaguzi na daraja (HD) Wallet. Utaratibu huu unaruhusu mgawanyiko wa matawi na upangaji wa Wallet katika viwango tofauti na jozi nyingi muhimu za watoto, ambazo zinaweza kurejeshwa kwa kujua tu habari ya msingi ya uokoaji (maneno ya Mnemonic na passphrase yoyote inayowezekana). Ili kupata ufunguo wa mtoto, chaguo za kukokotoa za `HMAC-SHA512` hutumiwa pamoja na msimbo wa mnyororo wa mzazi na muunganisho wa ufunguo wa mzazi na faharasa ya biti 32. Kuna aina mbili za derivations:


- Utoaji wa kawaida, unaotumia ufunguo kuu wa umma kama msingi wa chaguo za kukokotoa `HMAC-SHA512`;
- Utoaji mgumu, unaotumia ufunguo wa faragha kuu kama msingi wa chaguo za kukokotoa `HMAC-SHA512`;


Matokeo ya HMAC-SHA512 imegawanywa katika mbili: bits 256 za kwanza huwa ufunguo wa mtoto (faragha au umma baada ya usindikaji kupitia ECDSA), na bits 256 zilizobaki huwa msimbo wa mnyororo wa watoto.