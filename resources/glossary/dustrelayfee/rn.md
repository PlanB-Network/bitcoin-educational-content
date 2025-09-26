---
term: AMAFARANGA Y'IKUNGU
---

Itegeko ry'urugero rikoreshwa n'imirongo y'urubuga kugira ngo bamenye ico babona ko ari "umupaka wa Dust." Iyi parametere ishiraho igipimo c’amahera mu Sats kuri kilobyte y’ukuri (Sats/kvB) ikora nk’ishingiro ryo kubara nimba agaciro ka UTXO kari munsi y’amahera akenewe kugira ngo umuntu ayishire mu bikorwa. Nkako, UTXO ifatwa nk'"Dust" kuri Bitcoin iyo isaba amafaranga menshi kugira ngo yimurirwe kuruta agaciro yiserukira. Ibara ry’ico kigero ni iri:


```text
limit = (input size + output size) * fee rate
```


Kubera ko igipimo c’amahera gikenewe kugira ngo igikorwa gishirwe mu gice ca Bitcoin kiguma gihinduka, umurongo wa `DustRelayFee` uremerera buri nzira gusobanura igipimo c’amahera gikoreshwa muri iki giharuro. Ku mbuga, kuri Bitcoin core, ako gaciro gashirwa kuri 3.000 Sats/kvB. Nk’akarorero, kugira ngo ubaze umupaka wa Dust ku bijanye n’injiza n’isohoka rya P2PKH, bipima 148 na 34 bytes, igiharuro coba ari:


```text
limit (sats) = (148 + 34) * 3000 / 1000 = 546 sats
```


Ivyo bisigura ko iyo node iriko iravugwa itazotanga amafaranga harimwo n'iyi P2PKH UTXO ifise agaciro kari munsi ya 546 Sats.