---
term: XOR
---

Kifupi cha operesheni "Exclusive au," kwa Kifaransa "Ou exclusif." Ni kazi ya msingi ya mantiki ya Boolean. Operesheni hii huchukua oparesheni mbili za Boolean, kila moja ikiwa $true$ au $false$, na hutoa pato la $true$ wakati operesheni hizo mbili zinatofautiana. Kwa maneno mengine, matokeo ya operesheni ya XOR ni $true$ ikiwa moja (lakini sio zote mbili) za operesheni ni $true$. Kwa mfano, operesheni ya XOR kati ya $1$ na $0$ itasababisha $1$. Tunakumbuka:


$$
1 \oplus 0 = 1
$$


Vile vile, operesheni ya XOR inaweza kufanywa kwa mlolongo mrefu wa bits. Kwa mfano:


$$
10110 \oplus 01110 = 11000
$$


Kila kidogo katika mlolongo inalinganishwa na mwenzake, na operesheni ya XOR inatumika. Hapa kuna jedwali la ukweli kwa operesheni ya XOR:


<div align="center">


| $A$ | $B$ | $A \oplus B$ |
|:---:|:---:|:------------:|
| $0$ | $0$ |      $0$     |
| $0$ | $1$ |      $1$     |
| $1$ | $0$ |      $1$     |
| $1$ | $1$ |      $0$     |

</ div>


Operesheni ya XOR inatumika katika maeneo mengi ya sayansi ya kompyuta, haswa katika cryptography, kwa sifa zake za kupendeza kama vile:


- Commutativity yake: utaratibu wa uendeshaji hauathiri matokeo. Kwa vigezo viwili vilivyopewa $D$ na $E$: $D \plus E = E \plus D$;
- Ushirikiano wake: kambi ya watendaji haiathiri matokeo. Kwa vigezo vitatu vilivyotolewa $A$, $B$, na $C$: $(A \plus B) \plus C = A \plus (B \plus C) $;
- Ina kipengele cha upande wowote $0$: opereta iliyounganishwa na $0$ daima itakuwa sawa na uendeshaji. Kwa tofauti fulani $A$: $A \plus 0 = A$;
- Kila kipengele ni kinyume chake. Kwa tofauti fulani $A$: $A \plus A = 0$.


Katika muktadha wa Bitcoin, operesheni ya XOR ni dhahiri inatumika katika maeneo mengi. Kwa mfano, XOR hutumiwa kwa kiasi kikubwa katika kazi ya SHA256, ambayo hutumiwa sana katika itifaki ya Bitcoin. Baadhi ya itifaki kama vile *SeedXOR* ya Coldcard pia hutumia primitive kwa programu zingine. Inapatikana pia katika BIP47 ili kusimba msimbo wa malipo unaoweza kutumika tena wakati wa uwasilishaji wake.

Katika uwanja mpana wa usimbaji fiche, XOR inaweza kutumika kama ilivyo kama algoriti ya usimbaji linganifu. Kanuni hii inaitwa "Padi ya Wakati Mmoja" au "Vernam Cipher," iliyopewa jina la mvumbuzi wake. Ingawa haiwezekani kwa sababu ya urefu wa ufunguo, algoriti hii ni mojawapo ya kanuni za usimbaji fiche zinazotambuliwa kuwa salama bila masharti.