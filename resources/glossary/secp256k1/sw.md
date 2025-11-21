---
term: SECP256K1
---

Jina lililopewa mkunjo mahususi wa duara unaotumika katika itifaki ya Bitcoin kwa ajili ya utekelezaji wa ECDSA (*Algoriti ya Sahihi ya Elliptic Curve Digital*) na algoriti za sahihi za dijiti za Schnorr. Mviringo wa `secp256k1` ulichaguliwa na mvumbuzi wa Bitcoin, Satoshi Nakamoto. Ina baadhi ya mali ya kuvutia, hasa faida ya utendaji.


Matumizi ya `secp256k1` katika Bitcoin yanamaanisha kwamba kila ufunguo wa faragha (nambari isiyo ya kawaida ya biti 256) imechorwa kwenye ufunguo unaolingana wa umma kupitia kujumlisha na kurudia nukta ya ufunguo wa faragha na sehemu ya jenereta ya `secp256k1`. Operesheni hii ni rahisi kufanya katika mwelekeo mmoja lakini haiwezekani kugeuza, ambayo ni msingi wa usalama wa saini za dijiti kwenye Bitcoin.


Mviringo wa `secp256k1` umebainishwa na mlingano wa mkunjo wa mduara $y^2 = x^3 + 7$, kumaanisha kuwa ina viambajengo $a$ sawa na $0$ na $b$ sawa na $7$ katika umbo la jumla la mlingano wa mkunjo wa mviringo $y^2 = x^3 + shoka + b$. `secp256k1` imefafanuliwa juu ya sehemu yenye kikomo ambayo agizo lake ni nambari kuu kubwa, haswa $p = 2^{256} - 2^{32} - 977$. Mviringo pia una mpangilio wa kikundi, ambao ni idadi ya pointi tofauti kwenye mkunjo, sehemu ya jenereta iliyofafanuliwa awali (au uhakika $G$), ambayo hutumiwa katika utendakazi wa kriptografia kwa jozi muhimu za generate, na cofactor sawa na $1$.


> ► *“SEC” inawakilisha “Viwango vya Uandikaji Bora wa Siri”. "P256" inaonyesha kuwa mkunjo umefafanuliwa juu ya sehemu $\mathbb{Z}_p$ ambapo $p$ ni nambari kuu ya 256-bit. "K" inarejelea jina la mvumbuzi wake, Neal Koblitz. Hatimaye, “1” inaonyesha kuwa hili ni toleo la kwanza la mkunjo huu.*