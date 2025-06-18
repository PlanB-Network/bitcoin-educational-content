---
term: FRAZA ZA OBNAVLJANJE
---

Fraza za oporavak, koja se ponekad naziva i Mnemonic, seed fraza ili tajna fraza, je niz koji obično sadrži 12 ili 24 reči, generisanih na pseudo-slučajan način iz izvora entropije. Pseudo-slučajni niz se uvek završava kontrolnom sumom. Mnemonic fraza, zajedno sa opcionalnim passphrase, koristi se za determinističko izvođenje svih ključeva povezanih sa HD (Hijerarhijski Deterministički) Wallet. To znači da je iz ove fraze moguće deterministički generate i ponovo kreirati sve privatne i javne ključeve Bitcoin Wallet, i samim tim pristupiti sredstvima povezanim s njim. Svrha fraze za oporavak je da obezbedi način za bekap i oporavak bitkoina koji je i siguran i lak za korišćenje.


Važno je čuvati ovu frazu na sigurnom i bezbednom mestu, jer svako ko poseduje Mnemonic imao bi pristup sredstvima odgovarajućeg Wallet. Ako se koristi u kontekstu tradicionalnog Wallet, i bez opcionalnog passphrase, često predstavlja SPOF (Single Point Of Failure). Fraza za oporavak je stoga kodiranje pseudo-slučajnog niza i kontrolne sume u svakodnevne reči kako bi se olakšala njena notacija i čitljivost za ljude. Konstruisana je prema BIP39 standardu, koji definiše i uređuje listu od 2048 reči korišćenih za ovo kodiranje.


> ► *Lista od 2048 reči iz BIP39 dostupna je na nekoliko jezika, međutim, savetuje se korišćenje samo engleske verzije, jer je to verzija koju najšire podržava Wallet softver.*