---
term: SECP256K1
---

Izina ry’umurongo wihariye w’umurongo w’uruzitiro ukoreshwa mu masezerano ya Bitcoin yo gushirwa mu ngiro kwa ECDSA (*Igiharuro c’umukono w’uruzitiro*) n’umurongo w’uruzitiro rwa Schnorr. Igiharuro ca `secp256k1` catowe n’uwahinguye Bitcoin, Satoshi Nakamoto. Ifise ibintu bimwe bimwe bishimishije, cane cane inyungu z’ibikorwa.


Ikoreshwa rya `secp256k1` muri Bitcoin bisigura ko urufunguzo rw'ibanga rwose (umubare w'ibice 256) rushirwa ku rufunguzo rwa bose ruhuye n'urwo biciye mu kwongerako no gukubita kabiri urufunguzo rw'urufunguzo rw'ibanga n'urufunguzo rw'umuhinguzi w'umurongo `secp256k1`. Ivyo bikorwa biroroshe gukora mu buryo bumwe ariko ntabwo bishoboka gusubira inyuma, ivyo bikaba ari vyo bishingirako umutekano w’imikono ya digitale kuri Bitcoin.


Igiharuro ca `secp256k1` kigaragazwa n’ingero y’igiharuro c’uruzitiro $y^2 = x^3 + 7$, bisobanura ko gifise ibiharuro $a$ bingana na $0$ na $b$ bingana na $7$ mu buryo rusangi bw’ingero y’igiharuro c’uruzitiro $y^2 = x^3 + ax + b$. `secp256k1` isobanurwa hejuru y'umurima ufise impera urutonde rwawo ari umubare munini cane w'intango, cane cane $p = 2^{256} - 2^{32} - 977$. Ico gicapo kandi gifise urutonde rw’imigwi, ari rwo mubare w’uturongo dutandukanye ku gicapo, akarongo k’umuyagankuba (canke akarongo $G$), gakoreshwa mu bikorwa vy’ubuhinga bwo gupfuka amakuru ku bice bibiri vy’urufunguzo rwa generate, n’igice c’umuyagankuba kingana na $1$.


> ► *“SEC” ni “Ingingo ngenderwako zo gukora neza amakuru y’ibanga”. “P256” yerekana ko umurongo usobanurwa hejuru y’umurima $\mathbb{Z}_p$ aho $p$ ari umubare w’intango w’ibice 256. “K” yerekeza ku izina ry’uwayihinguye, ari we Neal Koblitz. Ubwa nyuma, “1” yerekana ko iyo ari yo verisiyo ya mbere y’iyi nzira y’uruzitiro.*