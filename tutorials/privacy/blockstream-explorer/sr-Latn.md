---
name: BLOCKSTREAM Explorer
description: Istraži glavni Layer od Bitcoin i Liquid Network
---

![cover](assets/cover.webp)



BLOCKSTREAM Explorer je projekat koji olakšava istraživanje transakcija i Global State protokola Bitcoin, kao i [*Sidechain*](https://planb.network/en/resources/glossary/Sidechain) Liquid koji je razvila kompanija BLOCKSTREAM.



Pokrenut 2014. godine od strane BLOCKSTREAM, kompanije koju je osnovao Adam Back, [BLOCKSTREAM.info](https://BLOCKSTREAM.info) explorer ima za cilj da obezbedi robusnu infrastrukturu za Bitcoin, garantujući interoperabilnost i praćenje transakcija između slojeva (On-Chain i Liquid), dok poboljšava sigurnost i privatnost korisnika.



U ovom vodiču predstavljamo šta ga čini drugačijim, njegove usluge i kako nudi besprekorno praćenje operacija i statusa slojeva Bitcoin, On-Chain i Liquid.



## Početak sa BLOCKSTREAM



### Krećite se glavnim kanalom



Kada odete na BLOCKSTREAM.info explorer, na "**Dashboard**", glavni Bitcoin protokolarni kanal je podrazumevano izabran. Sa ovog Interface, imate pregled:





- Veličina glavnog lanca: Nedavno iskopani blokovi.



![blocks](assets/fr/01.webp)



Ovaj odeljak pruža informacije o nedavno iskopanim blokovima, Timestamp, broju transakcija uključenih u svaki BLOCK, veličini u kilobajtima (kB) i merenju svakog BLOCK u težinskim jedinicama (**WU** = *Weight Units*). Ovo poslednje merenje je od interesa, jer nam omogućava da procenimo optimizaciju BLOCK, s obzirom da je svaki BLOCK glavnog lanca ograničen na `4,000,000 WU`, ili `4,000 kWU`.





- Nedavne transakcije.



![transactions](assets/fr/02.webp)



Odeljak o transakcijama pruža informacije o jedinstvenom identifikatoru transakcije, uključenoj vrednosti Bitcoin, veličini u virtualnim bajtovima (vB) - što predstavlja zbir svih podataka (ulaznih i izlaznih) - i povezanoj stopi naplate. Na primer, transakcija sa veličinom od `153 vB` po stopi od `2 sat/vB` će imati trošak od `306 satoshija`.



### Istraživanje fluida



Iz menija "**Blocks**" možete pratiti istoriju cele glavne lanca unazad do poslednjeg BLOCK koji je iskopan.



![blocs](assets/fr/03.webp)



Klikom na određeni BLOCK, možete dobiti više detalja o informacijama i transakcijama koje su uključene u njega. Na primer, za BLOCK 919330: imate Hash od BLOCK. Takođe možete navigirati do prethodnog BLOCK, jer je svaki iskopani BLOCK (osim Genesis) povezan sa prethodnim, zadržavajući Hash svog prethodnika.



![metadata](assets/fr/04.webp)



Klikom na dugme **"Details "** možete dobiti više informacija o ovom BLOCK, kao što je njegov status, koji potvrđuje da je dodat u zadržani i propagirani glavni lanac. Takođe imate težinu na kojoj je ovaj BLOCK iskopan: ova težina predstavlja računarsku snagu potrebnu za rešavanje kriptografskog problema Mining i podešava se svakih 2016 blokova (otprilike 2 nedelje).



![details](assets/fr/05.webp)



Ispod ovog odeljka sa detaljima nalazimo sve transakcije uključene u ovaj BLOCK.



Prva transakcija u BLOCK naziva se **transaction coinbase**. Koristi se za dodelu Miner's Mining nagrade (sve naknade povezane sa transakcijama uključenim u BLOCK i BLOCK grant). Bitcoini stvoreni ovom transakcijom mogu se potrošiti tek nakon što se iskopa još 100 uzastopnih blokova. Drugim rečima, da bi ih mogao koristiti, Miner će morati da sačeka proizvodnju BLOCK **919430**. Ovo je poznato kao [*"maturity period "*](https://planb.network/fr/resources/glossary/maturity-period).



Coinbase je posebna transakcija: to je jedina transakcija bez pravog ulaza, jer ne troši bitkoine iz prethodne transakcije.




![coinbase](assets/fr/06.webp)



Sve ostale transakcije su podeljene u dva dela: ulazi i izlazi.



Da bi se bitkoini koristili kao ulazi u novoj transakciji, inicijator transakcije mora dokazati svoje vlasništvo pružanjem potpisa koji odgovara određenom skriptu. Svaki deo bitkoina (UTXO) sadrži skript koji obično zahteva specifičan potpis koji samo privatni ključ vlasnika može da obezbedi. Ovi skripti su ***scriptSig*** (u ASM), napisani u Bitcoin Script, i mogu biti različitih tipova. U ovom primeru, možemo videti da su korišćeni UTXO-i bili tipa P2SH za izlaz tipa P2WPKH (*Pay-to-Witness-Public-Key-Hash*).



Možete pratiti istoriju određenog UTXO koristeći heuristiku. Pozivamo vas da otkrijete različite Bitcoin heuristike i kako ojačati poverljivost vaših Bitcoin transakcija:



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

![trxs](assets/fr/07.webp)



Hajde da uzmemo primer odlaznog troška ove transakcije. Klikom na identifikator transakcije, preusmereni smo na odeljak **Transakcije** na stranici sa detaljima transakcije.



![transaction](assets/fr/08.webp)



Sa ove stranice možete saznati u koji BLOCK je transakcija uključena. U zavisnosti od tipa korišćenog Address, transakcija može optimizovati svoje podatke (*virtuelni bajtovi*) i stoga platiti manje naknade za transakciju. Ova transakcija, na primer, uštedela je 53% na naknadama korišćenjem native SegWit BECH32 Address formata počevši sa `bc1q`.



![trx_details](assets/fr/09.webp)



## Liquid premaz



Liquid Network je [*Sidechain*](https://planb.network/en/resources/glossary/Sidechain) i rešenje otvorenog koda nivoa 2 za Bitcoin protokol. Konkretno, omogućava brže i poverljivije Bitcoin transakcije.



Na BLOCKSTREAM.info exploreru, kliknite na dugme **"Liquid"** da biste prešli na Liquid Network.



![liquid](assets/fr/10.webp)



Klikom na jednu od transakcija koje želimo pratiti, vidimo da su iznosi Bitcoin delova zamenjeni rečima "**Poverljivo**". Na ovoj mreži, transakcije mogu biti poverljive, tako da ne možemo videti iznose svakog UTXO, bilo ulaznog ili izlaznog iz transakcije.



![liquid_trx](assets/fr/11.webp)



Međutim, primećujemo da su principi i mehanizmi prisutni na glavnom Layer protokolu Bitcoin isti: Bitcoin skripte za zaključavanje i UTXO sledljivost.



![liquid_details](assets/fr/12.webp)



Liquid Network takođe pruža nedepozitne digitalne asete koje organizacije mogu koristiti. U meniju **"Assets "** pronaći ćete listu registrovanih aseta, njihov ukupan broj i domen na koji se odnose.



![assets](assets/fr/13.webp)



Za svaki resurs možete pratiti istoriju transakcija izdavanja i spaljivanja (brisanje ukupnog broja u opticaju).



![assets_trxs](assets/fr/14.webp)




## Više opcija



Istraživač BLOCKSTREAM.info takođe uključuje vizualizacije i praćenje transakcija na Testnet, Bitcoin, On-Chain i Liquid Network.



![testnet](assets/fr/15.webp)



Kada odete na Testnet mrežu, ne koristite prave bitkoine, ali imate sve gore opisane funkcije.



![liquid_testnet](assets/fr/16.webp)



Ova mreža ima različitu dužinu lanca, na koji možete povezati i testirati rad mehanizama Bitcoin i Liquid.





- Odeljak API je posvećen svima koji žele integrisati određene funkcije Explorera u svoju aplikaciju. Kroz ovaj API možete ispitivati glavni lanac različitih slojeva (On-Chain i Liquid), pratiti transakcije i saznati prosečne naknade za transakcije u BLOCK, na primer.



![api](assets/fr/17.webp)



Sada ste spremni da iskoristite puni potencijal BLOCKSTREAM Explorer-a za upite na blokčejnima na On-Chain i Liquid slojevima. Nadamo se da vam je ovaj vodič bio informativan, i preporučujemo naš vodič o drugom Bitcoin Explorer-u:



https://planb.network/tutorials/privacy/analysis/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f