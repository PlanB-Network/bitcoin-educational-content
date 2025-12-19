---
name: Blockstream Explorer
description: Istražite glavni sloj Bitcoin i Liquid Network
---

![cover](assets/cover.webp)



Blockstream Explorer je projekat koji olakšava istraživanje transakcija i globalnog stanja Bitcoin protokola, kao i [*sidechain*](https://planb.academy/en/resources/glossary/sidechain) Liquid koji je razvila kompanija Blockstream.



Pokrenut 2014. godine od strane Blockstream-a, kompanije koju je osnovao Adam Back, [blockstream.info](https://blockstream.info) explorer ima za cilj da obezbedi robusnu infrastrukturu za Bitcoin, garantujući interoperabilnost i praćenje transakcija između slojeva (on-chain i Liquid), uz poboljšanje sigurnosti i privatnosti korisnika.



U ovom vodiču ćemo pogledati šta ga izdvaja, njegove usluge i kako nudi besprekorno praćenje operacija i statusa Bitcoin-ovih on-chain i Liquid slojeva.



## Početak sa Blockstream explorerom



### Navigirajte glavnim kanalom



Kada odete na Blockstream.info explorer, na "**Dashboard**", Bitcoin protokol glavnog lanca je podrazumevano izabran. Sa ovog interfejsa, imate pregled:





- Veličina glavnog lanca: Nedavno iskopani blokovi.



![blocks](assets/fr/01.webp)



Ovaj odeljak pruža informacije o nedavno iskopanim blokovima, vremenskoj oznaci, broju transakcija uključenih u svaki blok, veličini u kilobajtima (kB) i merenju svakog bloka u jedinicama težine (**WU** = *Weight Units*). Ovo poslednje merenje je od interesa, jer nam omogućava da procenimo optimizaciju bloka, s obzirom na to da je svaki blok glavnog lanca ograničen na `4,000,000 WU`, ili `4,000 kWU`.





- Nedavne transakcije.



![transactions](assets/fr/02.webp)



Odeljak o transakcijama pruža informacije o jedinstvenom identifikatoru transakcije, vrednosti bitcoina koja je uključena, veličini u virtualnim bajtovima (vB) - što predstavlja zbir svih podataka (ulaznih i izlaznih) - i povezanoj stopi naknade. Na primer, transakcija sa veličinom od `153 vB` po stopi od `2 sat/vB` će imati naknadu od `306 satoshija`.



### Istraživanje fluida



Iz menija "**Blocks**" možete pratiti istoriju cele glavne lanca unazad do poslednjeg iskopanog bloka.



![blocs](assets/fr/03.webp)



Klikom na određeni blok možete dobiti više detalja o informacijama i transakcijama uključenim u njega. Na primer, za blok 919330: videćete heš bloka. Takođe možete preći na prethodni blok, jer je svaki iskopani blok (osim Genesis) povezan sa prethodnim, zadržavajući heš svog prethodnika.



![metadata](assets/fr/04.webp)



Klikom na dugme **"Details "** možete dobiti više informacija o ovom bloku, kao što je njegov status, koji potvrđuje da je dodat u zadržani i propagirani glavni lanac. Takođe imate težinu na kojoj je ovaj blok iskopan: ova težina predstavlja računarsku snagu potrebnu za rešavanje kriptografskog problema mining i podešava se svakih 2016 blokova (otprilike 2 nedelje).



![details](assets/fr/05.webp)



Ispod ovog odeljka sa detaljima nalazimo sve transakcije uključene u ovaj blok.



Prva transakcija u bloku naziva se **transaction coinbase**. Koristi se za dodelu mining nagrade rudara (sve naknade povezane sa transakcijama uključenim u blok i blok grant). Bitcoini stvoreni ovom transakcijom mogu se potrošiti tek kada se iskopa još 100 uzastopnih blokova. Drugim rečima, da bi ih mogao koristiti, rudar će morati da sačeka proizvodnju bloka **919430**. Ovo je poznato kao [*"maturity period "*](https://planb.academy/fr/resources/glossary/maturity-period).



Coinbase je posebna transakcija: to je jedina transakcija bez pravog ulaza, jer ne troši bitkoine iz prethodne transakcije.




![coinbase](assets/fr/06.webp)



Sve ostale transakcije su podeljene u dva dela: ulazi i izlazi.



Da bi se bitkoini koristili kao ulazi u novoj transakciji, inicijator transakcije mora dokazati svoje vlasništvo pružanjem potpisa koji odgovara određenom skriptu. Svaki deo bitkoina (UTXO) sadrži skript koji generalno zahteva specifičan potpis koji samo privatni ključ vlasnika može da obezbedi. Ovi skripti su ***scriptSig*** (u ASM), napisani u Bitcoin Script, i mogu biti različitih tipova. U ovom primeru, možemo videti da su korišćeni UTXO-i bili tipa P2SH za izlaz tipa P2WPKH (*Pay-to-Witness-Public-Key-Hash*).



Možete pratiti istoriju određenog UTXO koristeći heuristiku. Pozivamo vas da otkrijete različite Bitcoin heuristike i načine za jačanje poverljivosti vaših transakcija na Bitcoin :



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

![trxs](assets/fr/07.webp)



Hajde da uzmemo primer odlaznog troška ove transakcije. Klikom na identifikator transakcije, preusmereni smo na sekciju **Transakcije** na stranici sa detaljima transakcije.



![transaction](assets/fr/08.webp)



Sa ove stranice možete saznati u kojem bloku je transakcija uključena. U zavisnosti od tipa korišćene adrese, transakcija može optimizovati svoje podatke (*virtuelni bajtovi*) i stoga platiti manje naknade za transakciju. Ova transakcija, na primer, uštedela je 53% na naknadama korišćenjem nativnog SegWit Bech32 formata adrese koji počinje sa `bc1q`.



![trx_details](assets/fr/09.webp)



## Liquid sloj



Liquid Network je [*sidechain*](https://planb.academy/en/resources/glossary/sidechain) i rešenje otvorenog koda nivoa 2 za Bitcoin protokol. Konkretno, omogućava brže i poverljivije bitcoin transakcije.



Na Blockstream.info exploreru, kliknite na dugme **"Liquid"** da biste prešli na Liquid mrežu.



![liquid](assets/fr/10.webp)



Klikom na jednu od transakcija koje želimo pratiti, vidimo da su iznosi bitcoin delova zamenjeni rečima "**Poverljivo**". Na ovoj mreži, transakcije mogu biti poverljive, tako da ne možemo videti iznose svakog UTXO, bilo ulaznog ili izlaznog iz transakcije.



![liquid_trx](assets/fr/11.webp)



Međutim, primećujemo da su principi i mehanizmi prisutni na glavnom sloju Bitcoin protokola isti: skripte za zaključavanje bitcoina i UTXO sledljivost.



![liquid_details](assets/fr/12.webp)



Liquid Network takođe pruža nedepozitne digitalne aktive koje mogu koristiti organizacije. U meniju **"Assets "**, pronaći ćete listu registrovanih aktiva, njihov ukupan broj i domen na koji se odnose.



![assets](assets/fr/13.webp)



Za svaki resurs, možete pratiti istoriju transakcija izdavanja i spaljivanja (brisanje ukupnog broja u opticaju).



![assets_trxs](assets/fr/14.webp)




## Više opcija



Blockstream.info explorer takođe uključuje vizualizacije i praćenje transakcija na Testnet, Bitcoin, on-chain i Liquid Network.



![testnet](assets/fr/15.webp)



Kada odete na Testnet mrežu, ne koristite prave bitkoine, ali imate sve gore opisane funkcije.



![liquid_testnet](assets/fr/16.webp)



Ova mreža ima različitu dužinu lanca, na koju možete povezati i testirati rad mehanizama Bitcoin i Liquid.





- Odeljak API posvećen je svima koji žele integrisati određene funkcije Explorera u svoju aplikaciju. Kroz ovaj API možete ispitivati glavni lanac različitih slojeva (on-chain i Liquid), pratiti transakcije i saznati prosečne naknade za transakcije u bloku, na primer.



![api](assets/fr/17.webp)



Sada ste spremni da iskoristite puni potencijal Blockstream Explorer-a za upite blockchain-a na on-chain i Liquid slojevima. Nadamo se da vam je ovaj vodič bio informativan, i preporučujemo naš vodič o drugom Bitcoin explorer-u:



https://planb.academy/tutorials/privacy/explorer/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f