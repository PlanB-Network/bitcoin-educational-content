---
term: PBKDF2
definition: Ikora ry'imfunguzo z'ibanga rikura ijambo ry'ibanga mu bisubiriza.
---

`PBKDF2` bihagarariye *Ijambobanga-Rufunguzo Rushingiye ku Murimo 2*. Ni uburyo bwo kurema imfunguruzo z’ibanga zivuye mu ijambobanga hakoreshejwe igikorwa co gukuraho. Bifata nk'inyungu ijambobanga, umunyu w'ibanga, kandi bisubiramwo igikorwa categekanijwe (kenshi igikorwa ca Hash nka `SHA256` canke `HMAC`) kuri ayo makuru. Ivyo bisubirwamwo kenshi kugira ngo generate urufunguzo rw’ibanga.


Mu bijanye na Bitcoin, `PBKDF2` ikoreshwa hamwe n’igikorwa ca `HMAC-SHA512` kugira ngo ireme seed ya Wallet (seed) ishingiye ku nsiguro y’amajambo 12 canke 24. Umunyu w'ibanga ukoreshwa muri iki kibazo ni BIP39 passphrase, kandi umubare w'ibisubirwamwo ni `2048`.