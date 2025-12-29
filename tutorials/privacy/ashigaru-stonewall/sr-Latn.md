---
name: Ashigaru - Stonewall
description: Razumevanje i korišćenje Stonewall transakcija na Ashigaru
---
![cover stonewall](assets/cover.webp)



> *Prekinite pretpostavke analize blokčejna matematički dokazivom sumnjom između pošiljaoca i primaoca vaših transakcija.*

## Šta je Stonewall transakcija?



Stonewall je specifičan oblik Bitcoin transakcije dizajniran da poveća poverljivost korisnika prilikom trošenja, imitirajući coinjoin između dve osobe, bez da to zapravo bude. U stvari, ova transakcija nije kolaborativna. Korisnik je može samostalno kreirati, koristeći samo UTXO-ove koje poseduje kao ulaz. Tako možete kreirati Stonewall transakciju za bilo koju priliku, bez potrebe za sinhronizacijom sa drugim korisnikom.



Transakcija Stonewall funkcioniše na sledeći način: kao ulaz u transakciju, izdavalac koristi 2 UTXO koja mu pripadaju. Na izlaznoj strani, transakcija proizvodi 4 izlaza, od kojih su 2 u potpuno istom iznosu. Druga 2 će biti devizna sredstva. Od 2 izlaza istog iznosa, samo jedan će zapravo otići primaocu.



Dakle, postoje samo 2 uloge u Stonewall transakciji:




- Izdavalac, koji vrši stvarnu uplatu ;
- Primalac, koji možda nije svestan specifične prirode transakcije i jednostavno očekuje uplatu od pošiljaoca.



Hajde da uzmemo primer da bismo razumeli ovu strukturu transakcije. Alice je kod pekara da kupi svoj baget, koji košta `4,000 sats`. Ona želi da plati u bitkoinima, dok zadržava neki oblik poverljivosti o svojoj uplati. Zato odlučuje da napravi Stonewall transakciju za uplatu.



![image](assets/fr/01.webp)



Analizom ovom transakcijom, možemo videti da je pekar zaista primio `4,000 sats` kao uplatu za baget. Alice je koristio 2 UTXO kao ulaze: jedan od `10,000 sats` i jedan od `15,000 sats`. Na izlaznoj strani, povratio je 3 UTXO: jedan od `4,000 sats`, jedan od `6,000 sats` i jedan od `11,000 sats`. Alice stoga ima neto saldo od `- 4,000 sats` na ovoj transakciji, što se dobro poklapa sa cenom bageta.



U ovom primeru, namerno sam zanemario mining naknade kako bih olakšao razumevanje. U stvarnosti, troškove transakcije u potpunosti snosi izdavalac.



## Koja je razlika između Stonewall i Stonewall x2?



Stonewall transakcija funkcioniše identično kao StonewallX2 transakcija, osim što druga zahteva saradnju, za razliku od klasične Stonewall transakcije, otuda naziv "x2". To je zato što se Stonewall transakcija izvršava bez potrebe za eksternom saradnjom: pošiljalac je može sprovesti bez pomoći druge osobe. Nasuprot tome, za Stonewall x2 transakciju, dodatni učesnik, poznat kao "saradnik", pridružuje se procesu. On ili ona doprinosi svojim bitcoinima transakciji, zajedno sa onima pošiljaoca, i preuzima celu sumu na kraju (modulo mining troškovi).



Hajde da se vratimo na naš primer sa Alice u pekari. Ako je želela da izvrši Stonewall x2 transakciju, Alice bi morala da sarađuje sa Bob (trećom stranom) prilikom postavljanja transakcije. Obe bi unele po jedan UTXO. Bob bi zatim dobila ceo svoj doprinos nazad. Pekar bi primio uplatu za svoj baget na isti način kao u Stonewall transakciji, dok bi Alice povratila svoj početni saldo, umanjen za cenu bageta.



![image](assets/fr/02.webp)



Iz perspektive autsajdera, transakcija bi ostala potpuno ista.



![image](assets/fr/03.webp)



Ukratko, Stonewall i Stonewall x2 transakcije dele identičnu strukturu. Razlika između njih leži u njihovoj kolaborativnoj ili nekolaborativnoj prirodi. Stonewall transakcija se razvija individualno, bez potrebe za saradnjom. Stonewall x2 transakcija, s druge strane, oslanja se na saradnju između dve osobe za njeno postavljanje.



[**-> Saznajte više o Stonewall transakcijama x2**](https://planb.academy/tutorials/privacy/on-chain/stonewall-x2-05120280-f6f9-4e14-9fb8-c9e603f73e5b)



## Koja je svrha Stonewall transakcije?



Stonewall struktura dodaje ogromnu količinu entropije transakciji, zamagljujući linije analize lanca. Gledano spolja, takva transakcija može biti interpretirana kao mali coinjoin između dve osobe. Ali u stvarnosti, kao Stonewall x2 transakcija, to je plaćanje. Ova metoda stoga generiše nesigurnosti u analizi lanca, ili čak vodi ka lažnim tragovima.



Hajde da uzmemo primer Alice kod pekara. Transakcija na blokčejnu bi izgledala ovako:



![image](assets/fr/04.webp)



Spoljašnji posmatrač koji se oslanja na uobičajene heuristike analize lanca mogao bi pogrešno zaključiti da "**dve osobe su napravile mali coinjoin, sa po jednim UTXO kao ulazom i po dva UTXO-a kao izlazom**".



![image](assets/fr/05.webp)



Ovo tumačenje je netačno, jer, kao što znate, jedan UTXO je poslat pekaru, 2 dolazna UTXO-a su došla od Alice, i ona je povratila 3 izlaza kursa razmene.



![image](assets/fr/01.webp)



Čak i ako spoljašnji posmatrač uspe da identifikuje obrazac Stonewall transakcije, neće imati sve informacije. Neće moći da odredi koji od dva UTXO-a istih iznosa odgovara uplati. Pored toga, neće moći da utvrdi da li su dva uneta UTXO-a od dve različite osobe, ili pripadaju jednoj osobi koja ih je spojila. Ova poslednja tačka je zbog činjenice da Stonewall x2 transakcije, pomenute gore, prate tačno isti obrazac kao Stonewall transakcije. Posmatrano spolja, i bez dodatnih kontekstualnih informacija, nemoguće je napraviti razliku između Stonewall transakcije i Stonewall x2 transakcije. Prve nisu kolaborativne transakcije, dok druge jesu. Ovo dodaje još više sumnje na trošak.



![image](assets/fr/03.webp)



## Kako da izvršim Stonewall transakciju na Ashigaru?



Prvobitno razvijen od strane Samourai Wallet tima, Stonewall transakcije su preuzete od strane Ashigaru aplikacije, fork originalnog wallet kreiranog nakon hapšenja Samourai developera. Trebaće vam da instalirate Ashigaru i kreirate wallet:



https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f

Za razliku od transakcija Stowaway ili Stonewall x2 (*cahoots*), Stonewall transakcije ne zahtevaju korišćenje Paynyms-a. Mogu se izvršiti direktno, bez prethodne pripreme ili saradnje sa drugim korisnikom.



Zapravo, za obavljanje Stonewall transakcija vam nije potreban vodič, jer ih Ashigaru automatski generiše svaki put kada trošite, čim vaš wallet sadrži dovoljno UTXO-a.



Kliknite na dugme `+` u donjem desnom uglu ekrana, zatim izaberite `Pošalji`.



![Image](assets/fr/06.webp)



Izaberite račun sa kojeg želite izvršiti trošak.



![Image](assets/fr/07.webp)



Zatim unesite detalje transakcije: adresu primaoca i iznos koji treba poslati, i pritisnite strelicu da potvrdite.



![Image](assets/fr/08.webp)



Ovde, naravno, možete prilagoditi podrazumevane naknade za transakcije u skladu sa tržišnim uslovima. Međutim, najzanimljiviji element na ovoj stranici je tip transakcije. Primetićete da je Ashigaru automatski odabrao `STONEWALL`. Kliknite na dugme `PREVIEW` da saznate više.



![Image](assets/fr/09.webp)



Možete videti da je transakcija zaista tipa Stonewall: sadrži 2 ulaza iste vrednosti, 2 izlaza iste vrednosti, kao i izlaze za razmenu i, u mom slučaju, dodatni ulaz da zadovolji iznos plaćanja.



![Image](assets/fr/10.webp)



Ako ne želite da izvršite Stonewall transakciju, već preferirate konvencionalno plaćanje, kliknite na ikonu olovke u gornjem desnom uglu ekrana, zatim izaberite `Simple` umesto `STONEWALL`.



![Image](assets/fr/11.webp)



Kada proverite sve detalje, prevucite zeleni strelicu na dnu ekrana da potpišete i oslobodite transakciju.



![Image](assets/fr/12.webp)



Sada znate kako da izvršite Stonewall transakciju, i što je još važnije, kako ona funkcioniše. Ako želite da saznate više, pogledajte moj vodič na Ashigaru Terminalu, koji objašnjava kako napraviti coinjoins putem Whirlpool.



https://planb.academy/tutorials/privacy/on-chain/ashigaru-terminal-9a0d46d3-33b9-4c64-84c5-bfa25b3a0add