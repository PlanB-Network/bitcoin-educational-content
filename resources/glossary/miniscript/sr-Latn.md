---
term: MINISCRIPT
---

Okvir dizajniran da obezbedi okvir za sigurno programiranje skripti na Bitcoin. Izvorni jezik Bitcoin se zove script. Prilično je složen za korišćenje u praksi, posebno za sofisticirane i prilagođene aplikacije. Pre svega, veoma je teško verifikovati ograničenja skripte. Miniscript koristi podskup Bitcoin skripti kako bi pojednostavio njihovo kreiranje, analizu i verifikaciju. Svaki miniscript je ekvivalentan 1 za 1 sa izvornom skriptom. Koristi se jezik politika prilagođen korisniku, koji se zatim kompajlira u miniscript, da bi konačno odgovarao izvornoj skripti.


![](../../dictionnaire/assets/30.webp)


Miniscript omogućava programerima da kreiraju sofisticirane skripte na sigurniji i pouzdaniji način. Osnovne osobine Miniscripta su sledeće:


- Omogućava statičku analizu skripte, uključujući uslove trošenja koje dopušta i njen trošak u smislu resursa;
- Omogućava kreiranje skripti koje se pridržavaju konsenzusa;
- Omogućava analizu da li različiti putevi trošenja ispunjavaju standardna pravila čvorova;
- Uspostavlja opšti standard, razumljiv i sastavljiv, za sav Wallet softver i hardver.


Miniscript projekat je pokrenut 2018. godine od strane Petera Wuillea, Andrewa Poelstre i Sanketa Kanjalkara, kroz kompaniju Blockstream. Miniscript je dodat u Bitcoin Core Wallet u režimu samo za gledanje u decembru 2022. sa verzijom 24.0, a zatim u potpunosti u maju 2023. sa verzijom 25.0.