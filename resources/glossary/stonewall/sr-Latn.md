---
term: STONEWALL
---

Specifičan oblik Bitcoin transakcije usmeren na povećanje privatnosti korisnika tokom trošenja, imitirajući CoinJoin između dve osobe, bez da to zapravo bude. Zaista, ova transakcija nije kolaborativna. Korisnik je može konstruisati samostalno, uključujući samo svoje UTXO-e kao ulaze. Stoga, možete kreirati Stonewall transakciju za bilo koju priliku, bez potrebe za sinhronizacijom sa drugim korisnikom.


Operacija Stonewall transakcije funkcioniše na sledeći način: na ulazu transakcije, pošiljalac koristi 2 UTXO-a koja pripadaju njemu. Transakcija zatim proizvodi 4 izlaza, od kojih će 2 biti tačno isti iznos. Druga 2 će predstavljati kusur. Među 2 izlaza istog iznosa, samo jedan će zapravo otići primaocu uplate.


Dakle, postoje samo 2 uloge u Stonewall transakciji:


- Pošiljalac, koji vrši stvarno plaćanje;
- Primalac, koji možda nije svestan specifične prirode transakcije i jednostavno čeka uplatu od pošiljaoca.


![](../../dictionnaire/assets/33.webp)

Transakcije Stonewall su dostupne na obe aplikacije, Samourai Wallet i Sparrow Wallet softveru.


Stonewall struktura dodaje mnogo entropije transakciji i zamagljuje trag za analizu lanca. Sa spoljašnje strane, takva transakcija može biti interpretirana kao mali CoinJoin između dve osobe. Ali u stvarnosti, baš kao i Stonewall x2 transakcija, to je plaćanje. Ova metoda stoga generiše nesigurnosti u analizi lanca, ili čak vodi ka lažnim tragovima. Čak i ako spoljni posmatrač uspe da identifikuje obrazac Stonewall transakcije, neće imati sve informacije. Neće moći da odredi koji od dva UTXO-a istih iznosa odgovara plaćanju. Štaviše, neće moći da odredi da li dva UTXO-a na ulazu dolaze od dve različite osobe ili pripadaju jednoj osobi koja ih je spojila. Ova poslednja tačka je zbog činjenice da Stonewall x2 transakcije prate potpuno isti obrazac kao Stonewall transakcije. Sa spoljašnje strane i bez dodatnih informacija o kontekstu, nemoguće je razlikovati Stonewall transakciju od Stonewall x2 transakcije. Međutim, prve nisu kolaborativne transakcije, dok druge jesu. Ovo dodaje još više sumnje u vezi sa ovim troškom.