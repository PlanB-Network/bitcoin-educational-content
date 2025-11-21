---
term: BIP0032
---

BIP32 je uveo koncept hijerarhijski determinističkog Wallet (HD Wallet). Ovaj predlog omogućava generisanje hijerarhije parova ključeva iz zajedničkog `master seed`, koristeći funkcije jednosmerne derivacije. Svaki generisani par ključeva može sam biti roditelj drugih ključeva, formirajući tako strukturu nalik stablu (hijerarhijsku). Prednost BIP32 je u tome što omogućava upravljanje sa više različitih parova ključeva uz potrebu da se čuva samo jedan seed za njihovu regeneraciju. Ova inovacija je značajno pomogla u borbi protiv problema ponovne upotrebe Address, što je ozbiljno za privatnost korisnika. BIP32 takođe omogućava kreiranje podgrana unutar istog Wallet radi olakšavanja njegovog upravljanja.