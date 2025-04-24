---
name: Stonewall
description: Razumevanje i korišćenje Stonewall transakcija
---
![cover stonewall](assets/cover.webp)


***UPOZORENJE:** Nakon hapšenja osnivača Samourai Wallet i zaplene njihovih servera 24. aprila, korišćenje Samourai Wallet aplikacije sada zahteva povezivanje sa vašim sopstvenim Dojo-om da bi ispravno funkcionisala. Osim toga, Stonewall transakcije nisu uopšte pogođene i mogu se i dalje obavljati bez ikakvih problema. Zaista, ove vrste transakcija se obavljaju autonomno, bez potrebe za eksternom saradnjom ili povezivanjem putem Sorobana.*


_Pažljivo pratimo razvoj ovog slučaja kao i razvoj povezanih alata. Budite sigurni da ćemo ažurirati ovaj vodič čim nove informacije postanu dostupne._


_Ovaj vodič je pružen isključivo u obrazovne i informativne svrhe. Ne podržavamo niti ohrabrujemo korišćenje ovih alata u kriminalne svrhe. Odgovornost je svakog korisnika da se pridržava zakona u svojoj jurisdikciji._


---

> *Prekinite pretpostavke Blockchain analize sa matematički dokazivom sumnjom između pošiljaoca i primaoca vaših transakcija.*

## Šta je Stonewall transakcija?

Stonewall je specifičan oblik Bitcoin transakcije usmeren na povećanje privatnosti korisnika tokom transakcije oponašanjem CoinJoin između dve strane, bez stvarnog postojanja takve transakcije. Zapravo, ova transakcija nije kolaborativna. Korisnik je može konstruisati samostalno, koristeći samo svoje UTXO-e kao ulaze. Stoga, možete kreirati Stonewall transakciju za bilo koju priliku bez potrebe za koordinacijom sa drugim korisnikom.


Rad Stonewall transakcije funkcioniše na sledeći način: kao ulaz, pošiljalac koristi 2 UTXO-a koja pripadaju njemu. Kao izlaz, transakcija proizvodi 4 izlaza, uključujući 2 koja će biti tačno isti iznos. Druga 2 će biti kusur. Među 2 izlaza istog iznosa, samo jedan će zapravo ići primaocu uplate.


Postoje samo 2 uloge u Stonewall transakciji:


- Pošiljalac, koji vrši stvarno plaćanje;
- Primalac, koji možda nije svestan specifične prirode transakcije i jednostavno očekuje uplatu od pošiljaoca.


Hajde da uzmemo primer kako bismo razumeli ovu strukturu transakcije. Alisa je u pekari da kupi svoj baget, koji košta `4,000 Sats`. Ona želi da plati u bitkoinima, a da pritom zadrži određeni nivo privatnosti u svojoj uplati. Stoga odlučuje da kreira Stonewall transakciju za uplatu.

![transaction stonewall bakery](assets/en/1.webp)

Analizirajući ovu transakciju, možemo videti da je pekar zaista primio `4,000 Sats` kao uplatu za baget. Alisa je koristila 2 UTXO-a kao ulaze: jedan od `10,000 Sats` i jedan od `15,000 Sats`. Kao izlaz, dobila je 3 UTXO-a: jedan od `4,000 Sats`, jedan od `6,000 Sats` i jedan od `11,000 Sats`. Alisa ima neto saldo od `-4,000 Sats` u ovoj transakciji, što odgovara ceni bageta.


U ovom primeru, namerno sam izostavio Mining naknade kako bih olakšao razumevanje. U stvarnosti, troškove transakcije u potpunosti pokriva pošiljalac.


## Koja je razlika između Stonewall i Stonewall x2?

Stonewall transakcija funkcioniše na isti način kao i StonewallX2 transakcija, s jedinom razlikom što druga zahteva saradnju, za razliku od klasične Stonewall transakcije, otuda oznaka "x2". Zaista, Stonewall transakcija može biti izvršena bez potrebe za eksternom saradnjom: pošiljalac je može sprovesti bez pomoći druge osobe. Međutim, za Stonewall x2 transakciju, dodatni učesnik, nazvan "saradnik", pridružuje se procesu. Saradnik doprinosi svojim bitcoinima kao ulaz, zajedno sa onima pošiljaoca, i prima celokupan iznos kao izlaz (umanjen za Mining naknade).


Hajde da ponovo razmotrimo naš primer sa Alisom u pekari. Da je želela da napravi Stonewall x2 transakciju, Alisa bi morala da sarađuje sa Bobom (trećom stranom) prilikom kreiranja transakcije. Oboje bi dali ulaz UTXO. Bob bi zatim primio pun iznos svog ulaza kao izlaz. Pekar bi primio uplatu za svoj baget na isti način kao u Stonewall transakciji, dok bi Alisa dobila svoj početni saldo nazad, umanjen za cenu bageta.

![transaction stonewall x2](assets/en/2.webp)


Iz spoljne perspektive, obrazac transakcije bi ostao potpuno isti.

![Stonewall or Stonewall x2 ?](assets/en/3.webp)


Ukratko, Stonewall i Stonewall x2 transakcije dele identičnu strukturu. Razlika između njih leži u njihovoj kolaborativnoj prirodi. Stonewall transakcija se razvija individualno, bez potrebe za saradnjom. Nasuprot tome, Stonewall x2 transakcija se oslanja na saradnju između dve osobe za njeno sprovođenje.


[**-> Saznajte više o Stonewall x2 transakcijama**](https://planb.network/tutorials/privacy/On-Chain/stonewall-x2-05120280-f6f9-4e14-9fb8-c9e603f73e5b)


## Koja je svrha Stonewall transakcije?

Stonewall struktura dodaje značajnu količinu entropije transakciji i zamagljuje analizu lanca. Iz spoljašnje perspektive, takva transakcija može biti interpretirana kao mali CoinJoin između dve osobe. Ali u stvarnosti, baš kao i Stonewall x2 transakcija, to je plaćanje. Ova metoda stoga stvara nesigurnosti u analizi lanca, i može čak dovesti do lažnih tragova.


Hajde da ponovo pogledamo Alisin primer u pekari. Transakcija na Blockchain bi izgledala ovako:

![Stonewall or Stonewall x2 ?](assets/en/4.webp)

Spoljni posmatrač koji se oslanja na uobičajene heuristike analize lanca mogao bi pogrešno zaključiti da "*dve osobe su izvele mali CoinJoin, sa po jednim UTXO kao ulazom i po dva UTXO-a kao izlazom*".

![Stonewall or Stonewall x2 ?](assets/en/5.webp)

Ovo tumačenje je netačno jer, kao što znate, UTXO je poslat pekaru, 2 UTXO-a u ulazu dolaze od Alice, i ona je primila 3 izlaza kusura.


![transaction stonewall baker](assets/en/1.webp)

Čak i ako spoljašnji posmatrač uspe da identifikuje obrazac Stonewall transakcije, neće imati sve informacije. Neće moći da odrede koji od dva UTXO-a istih iznosa odgovara uplati. Štaviše, neće moći da utvrde da li dva UTXO-a u ulazu dolaze od dve različite osobe ili pripadaju jednoj osobi koja ih je spojila. Ova poslednja tačka je zbog činjenice da Stonewall x2 transakcije, o kojima smo gore govorili, prate potpuno isti obrazac kao Stonewall transakcije. Spolja i bez dodatnih informacija o kontekstu, nemoguće je razlikovati Stonewall transakciju od Stonewall x2 transakcije. Međutim, prve nisu kolaborativne transakcije, dok druge jesu. Ovo dodaje još više sumnji u vezi sa ovim troškom.

![Stonewall or Stonewall x2 ?](assets/en/3.webp)

## Kako izvršiti Stonewall transakciju na Samourai Wallet?

Za razliku od Stowaway ili Stonewall x2 (cahoots) transakcija, Stonewall transakcija ne zahteva korišćenje Paynyms. Može se obaviti direktno, bez ikakvih pripremnih koraka. Da biste to uradili, pratite naš video tutorijal na Samourai Wallet:

![Stonewall Tutorial - Samourai Wallet](https://youtu.be/mlRtZvWGuk0?si=e_lSKJLvybWUna1j)


## Kako izvršiti Stonewall transakciju na Sparrow Wallet?

Za razliku od Stowaway ili Stonewall x2 (cahoots) transakcija, Stonewall transakcija ne zahteva korišćenje Paynyms-a. Može se obaviti direktno, bez ikakvih pripremnih koraka. Da biste to uradili, pratite naš video tutorijal na Sparrow Wallet:

![Stonewall Tutorial - Sparrow Wallet](https://youtu.be/su89ljkV_OI?si=1jNaSJGvECUYe6Or)



**Spoljni resursi:**


- https://docs.samourai.io/en/spend-tools#stonewall.