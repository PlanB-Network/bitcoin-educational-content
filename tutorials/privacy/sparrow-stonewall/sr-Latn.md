---
name: Sparrow Wallet - Stonewall
description: Razumevanje i korišćenje Stonewall transakcija na Sparrow
---

![cover](assets/cover.webp)




> *Prekinite pretpostavke analize blockchain-a matematički dokazivom sumnjom između pošiljaoca i primaoca vaših transakcija.*

## Šta je Stonewall transakcija?



Stonewall je specifičan oblik Bitcoin transakcije dizajniran da poveća poverljivost korisnika prilikom trošenja, imitirajući coinjoin između dve osobe, bez da to zapravo bude jedan. U stvari, ova transakcija nije kolaborativna. Korisnik je može napraviti samostalno, koristeći samo UTXO-ove koji mu pripadaju kao ulaz. Tako možete kreirati Stonewall transakciju za bilo koju priliku, bez potrebe za sinhronizacijom sa drugim korisnikom.



Transakcija Stonewall funkcioniše na sledeći način: kao ulaz u transakciju, izdavalac koristi 2 UTXO koja mu pripadaju. Na izlaznoj strani, transakcija proizvodi 4 izlaza, od kojih su 2 u potpuno istom iznosu. Druga 2 će biti devizna. Od 2 izlaza istog iznosa, samo jedan će zapravo otići primaocu.



Dakle, postoje samo 2 uloge u Stonewall transakciji:




- Izdavalac, koji vrši stvarnu uplatu ;
- Primalac, koji možda nije svestan specifične prirode transakcije i jednostavno očekuje uplatu od pošiljaoca.



Hajde da uzmemo primer da bismo razumeli ovu strukturu transakcije. Alice je kod pekara da kupi svoj baget, koji košta `4,000 sats`. Ona želi da plati u bitkoinima, dok zadržava neki oblik poverljivosti o svojoj uplati. Zato odlučuje da napravi Stonewall transakciju za uplatu.



![image](assets/fr/01.webp)



Analizom ove transakcije, možemo videti da je pekar zaista primio `4,000 sats` kao uplatu za baget. Alice je koristio 2 UTXO-a kao ulaze: jedan od `10,000 sats` i jedan od `15,000 sats`. Na izlazu, povratio je 3 UTXO: jedan od `4,000 sats`, jedan od `6,000 sats` i jedan od `11,000 sats`. Alice stoga ima neto saldo od `- 4,000 sats` na ovoj transakciji, što se dobro poklapa sa cenom bageta.



U ovom primeru, namerno sam zanemario mining naknade kako bih olakšao razumevanje. U stvarnosti, troškove transakcije u potpunosti snosi izdavalac.



## Koja je razlika između Stonewall i Stonewall x2?



Stonewall transakcija funkcioniše identično kao StonewallX2 transakcija, osim što potonja zahteva saradnju, za razliku od klasične Stonewall transakcije, otuda i naziv "x2". Ovo je zato što se Stonewall transakcija izvršava bez potrebe za eksternom saradnjom: pošiljalac je može sprovesti bez pomoći druge osobe. Nasuprot tome, za Stonewall x2 transakciju, dodatni učesnik, poznat kao "saradnik", pridružuje se procesu. On ili ona doprinosi svojim bitcoinima transakciji, zajedno sa onima pošiljaoca, i preuzima čitav iznos na kraju (minus mining troškove).



Hajde da se vratimo na naš primer sa Alice u pekari. Da je želela da izvrši Stonewall x2 transakciju, Alice bi morala da sarađuje sa Bob (trećom stranom) prilikom postavljanja transakcije. Oboje bi uključili UTXO. Bob bi tada primio pun iznos svog doprinosa na izlazu. Pekar bi primio uplatu za svoj baget na isti način kao u Stonewall transakciji, dok bi Alice povratila svoj početni saldo, umanjen za cenu bageta.



![image](assets/fr/02.webp)



Iz perspektive autsajdera, transakcija bi ostala potpuno ista.



![image](assets/fr/03.webp)



Ukratko, Stonewall i Stonewall x2 transakcije dele identičnu strukturu. Razlika između njih leži u njihovoj kolaborativnoj ili nekolaborativnoj prirodi. Stonewall transakcija se razvija individualno, bez potrebe za saradnjom. Stonewall x2 transakcija, s druge strane, oslanja se na saradnju između dve osobe za njeno postavljanje.



[**-> Saznajte više o Stonewall transakcijama x2**](https://planb.academy/tutorials/privacy/on-chain/stonewall-x2-05120280-f6f9-4e14-9fb8-c9e603f73e5b)



## Koja je svrha Stonewall transakcije?



Stonewall struktura dodaje ogromnu količinu entropije transakciji, zamagljujući linije analize lanca. Gledano spolja, takva transakcija može biti interpretirana kao mali coinjoin između dve osobe. Ali u stvarnosti, kao Stonewall x2 transakcija, to je plaćanje. Ova metoda stoga generiše nesigurnosti u analizi lanca, ili čak vodi ka lažnim tragovima.



Hajde da uzmemo primer Alice kod pekara. Transakcija na blockchain-u bi izgledala ovako:



![image](assets/fr/04.webp)



Spoljašnji posmatrač koji se oslanja na uobičajene heuristike analize lanca mogao bi pogrešno zaključiti da "*dve osobe su napravile mali coinjoin, sa po jednim UTXO kao ulazom i po dva UTXO-a kao izlazom*".



![image](assets/fr/05.webp)



Ovo tumačenje je netačno, jer, kao što znate, jedan UTXO je poslat pekaru, 2 dolazna UTXO-a su došla od Alices, i ona je povratila 3 izlaza razmene.



![image](assets/fr/01.webp)



Čak i ako spoljašnji posmatrač uspe da identifikuje šablon Stonewall transakcije, neće imati sve informacije. Neće moći da odredi koji od dva UTXO-a istih iznosa odgovara uplati. Pored toga, neće moći da utvrdi da li dve UTXO stavke dolaze od dve različite osobe, ili pripadaju jednoj osobi koja ih je spojila. Ova poslednja tačka je zbog činjenice da Stonewall x2 transakcije, pomenute gore, prate potpuno isti obrazac kao Stonewall transakcije. Posmatrano spolja i bez dodatnih kontekstualnih informacija, nemoguće je napraviti razliku između Stonewall transakcije i Stonewall x2 transakcije. Prve nisu kolaborativne transakcije, dok su druge. Ovo dodaje još više sumnje na trošak.



![image](assets/fr/03.webp)



## Kako da izvršim Stonewall transakciju na Sparrow?



Prvobitno razvijene od strane tima Samurai Wallet, Stonewall transakcije su preuzete od strane Ashigaru aplikacije, fork iz originalnog portfolija kreiranog nakon hapšenja Samurai developera, a takođe i na Sparrow Wallet.



Trebaće da instalirate Sparrow i kreirate :



https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Za razliku od transakcija Stowaway ili Stonewall x2 (*cahoots*), Stonewall transakcije ne zahtevaju korišćenje Paynyms-a. Mogu se obaviti direktno, bez posebne pripreme ili saradnje sa drugim korisnikom.



Da biste izvršili Stonewall transakciju na Sparrow, procedura je veoma jednostavna: počnite kreiranjem transakcije kao i obično, bilo putem menija `Send`, ili iz menija `UTXOs` ako želite da uradite *Coin Control*.



![Image](assets/fr/06.webp)



Zatim unesite detalje transakcije: adresu primaoca, oznaku, iznos koji se šalje i iznos ili stopu naknada, u zavisnosti od uslova na tržištu.



![Image](assets/fr/07.webp)



Pre nego što potvrdite, ovde možete izabrati Stonewall strukturu. Na dnu interfejsa, zamenite `Efficiency` sa `Privacy`. Ako se ova opcija ne pojavi, to znači da vaš portfelj nema dovoljan broj UTXO-a za izgradnju ove vrste transakcije.



![Image](assets/fr/08.webp)



Nakon odabira opcije `Privacy`, primetićete da je struktura transakcije potpuno izmenjena: postaje Stonewall transakcija, koristeći nekoliko vaših UTXO-a kao ulaze i proizvodeći dva izlaza identičnih iznosa, od kojih jedan odgovara stvarnom plaćanju od `100,000 sats`, pored izlaza za razmenu.



![Image](assets/fr/09.webp)



Ako je sve ispravno, kliknite na `Create Transaction`.



Zatim možete poslednji put proveriti detalje transakcije i kliknuti na `Finalize Transaction for Signing`.



![Image](assets/fr/10.webp)



Zatim potpišite transakciju prema metodi specifičnoj za vaš portfelj i kliknite na `Broadcast Transaction` da biste je emitovali na Bitcoin mreži, čekajući potvrdu.



![Image](assets/fr/11.webp)



Sada znate kako funkcioniše Stonewall transakcija na Sparrow Wallet i kako je kreirati. Da biste produbili svoje znanje o ovim alatima dizajniranim za jačanje vaše poverljivosti na lancu, pozivam vas da pratite moju BTC 204 obuku na Plan ₿ Academy :



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c