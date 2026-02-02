---
name: Ashigaru - Whirlpool Coinjoin
description: Kako da napravim coinjoin-ove u aplikaciji Ashigaru?
---

![cover](assets/cover.webp)



"*a bitcoin wallet za ulice*"



U ovom vodiču ćete naučiti šta je coinjoin i kako ga napraviti pomoću Ashigaru Terminal aplikacije i Whirlpool implementacije, coinjoin protokola nasleđenog od Samourai Wallet.



## Kako Whirlpool coinjoints funkcionišu



U ovom vodiču, neću ponovo prelaziti pojam coinjoin-a, njegovu korisnost ili teoretski rad Whirlpool, jer su ove teme već detaljno objašnjene u 5. delu BTC 204 kursa obuke na Plan ₿ Akademiji. Ako još niste savladali rad Whirlpool ili princip coinjoin-a, toplo preporučujem da pogledate ovaj deo 5 pre nego što nastavite :



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Međutim, evo nekoliko brzih činjenica i brojki koje mogu biti korisne.



Portfelji kompatibilni sa Whirlpool koriste 4 odvojena računa kako bi zadovoljili potrebe coinjoin procesa:




- Račun **Depozit**, označen indeksom `0'` ;
- Nalog **Bad Bank** (ili *doxxic exchange*), identifikovan indeksom `2,147,483,644'` ;
- Nalog **Premix**, identifikovan indeksom `2 147 483 645'` ;
- Nalog **Postmix**, identifikovan indeksom `2 147 483 646'`.



Na Ashigaru, u novembru 2025, dostupne su dve denominacije bazena (ova lista će se verovatno razvijati u narednim mesecima: stoga se setite da proverite vrednosti dok čitate):




- 0.25 BTC`, sa ulaznom naknadom od `0.0125 BTC`;
- 0,025 BTC, sa ulaznom naknadom od 0,00125 BTC.



Svaki ciklus mešanja može uključivati između 5 i 10 UTXO-a na ulazu i izlazu.



![Image](assets/fr/01.webp)



## Softverski zahtevi



Da biste napravili coinjoin-e sa Whirlpool, biće vam potrebna tri odvojena programa:





- Ashigaru Terminal**, koji vam omogućava da upravljate svojim coinjoin-ovima direktno sa vašeg računara;



https://planb.academy/tutorials/privacy/on-chain/ashigaru-terminal-9a0d46d3-33b9-4c64-84c5-bfa25b3a0add



- Ashigaru Wallet**, aplikacija na vašem pametnom telefonu pomoću koje možete trošiti svoje bitkoine u *postmix* sa bilo kog mesta ;



https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f



- Dojo**, implementacija Bitcoin čvora koja garantuje suverenu vezu sa mrežom, bez oslanjanja na server treće strane.



https://planb.academy/tutorials/node/bitcoin/dojo-aa818a21-e701-48a2-8421-63c6186ed23f

Instalirajte svaki od ovih alata prateći njihove odgovarajuće tutorijale, zatim možete početi sa pravljenjem svojih prvih coinjoin-ova.



## Primite bitkoine



Nakon kreiranja vašeg portfolija, počećete sa jednim nalogom, identifikovanim indeksom `0'`. Ovo je `Depozit` nalog. Na ovaj nalog ćete slati bitkoine namenjene za coinjoin transakcije. Možete ih primiti ili putem Ashigaru aplikacije (pogledajte deo 5 posvećenog vodiča), ili putem Ashigaru Terminala (takođe detaljno objašnjeno u delu 5 posvećenog vodiča).



Kada vaš depozitni račun sadrži najmanje iznos potreban za učešće u najmanjem bazenu (plus troškovi usluge i minimalni iznos potreban za pokrivanje troškova mining), bićete spremni da započnete svoje prve coinjoin transakcije.



![Image](assets/fr/02.webp)



## Napravi Tx0



Kada sredstva stignu na vaš depozitni račun i transakcija bude potvrđena, možete započeti coinjoin proces. Da biste to uradili, na Ashigaru Terminalu, otvorite meni `Wallets`, zatim izaberite vaš wallet. Ako je vaš wallet zaključan, softver će vas tražiti vašu lozinku i passphrase.



![Image](assets/fr/03.webp)



Zatim izaberite nalog `Deposit`.



![Image](assets/fr/04.webp)



Idite na meni `UTXOs`.



![Image](assets/fr/05.webp)



Ovde ćete videti listu svih UTXO-a na vašem depozitnom računu. Izaberite one koje želite poslati u coinjoin ciklusima.



Za veću poverljivost i da bi se izbegao *Common Input Ownership Heuristic (CIOH)*, preporučuje se korišćenje samo jednog UTXO po unosu u Whirlpool (detaljno objašnjenje ovog principa može se naći u BTC 204).



Pritisnite taster `ENTER` na vašoj tastaturi da izaberete UTXO: zvezdica `(*)` će se pojaviti pored njega da označi da je izabran.



![Image](assets/fr/06.webp)



Zatim kliknite na dugme `Mix Selected`.



![Image](assets/fr/07.webp)



Ako imate UTXO dovoljno veliki da učestvuje u bilo kojem od dva dostupna bazena, možete odabrati odredišni bazen koristeći strelice. Na ovoj stranici ćete videti detalje vašeg Tx0 :




- broj UTXO-a koji će ući u bazen;
- različite naknade koje se primenjuju (naknade za usluge i mining naknade) ;
- količina *doxxic promene*.



Proverite informacije pažljivo, zatim kliknite na `Broadcast` da emitujete Tx0.



![Image](assets/fr/08.webp)



Ashigaru će zatim prikazati TXID vašeg Tx0, potvrđujući da je transakcija emitovana na mreži.



![Image](assets/fr/09.webp)



## Pravljenje coinjoin-a



Jednom kada je Tx0 emitovan, vratite se na početnu stranicu vašeg depozitnog računa, zatim kliknite na `Accounts` i odaberite `Premix` račun.



![Image](assets/fr/10.webp)



U meniju `UTXOs`, videćete različite izjednačene delove, spremne da uđu u cikluse coinjoin-a. Čim se Tx0 potvrdi, Ashigaru Terminal će automatski pokrenuti njihov prvi ciklus mešanja.



![Image](assets/fr/11.webp)



Kada je Tx0 potvrđen, prva coinjoin transakcija će biti kreirana i automatski emitovana od strane Ashigaru Terminala. Odlaskom na `Accounts > Postmix > UTXOs`, možete videti svoje izjednačene UTXO-e, koji čekaju potvrdu svog prvog ciklusa.



![Image](assets/fr/12.webp)



Sada možete ostaviti Ashigaru Terminal da radi u pozadini: nastaviće automatski da meša i remiksuje vaše numere.



## Završavanje coinjoin-a



Sada možete dozvoliti svojim kovanicama da se automatski remiksuju. Model Whirlpool znači da nema dodatnih troškova za remiksovanje: nema naknada za uslugu, nema mining naknada. Dakle, dozvoljavanje vašim kovanicama da učestvuju u više ciklusa mešanja može samo koristiti vašoj poverljivosti.



Za bolje razumevanje ovog mehanizma i koliko ciklusa vredi čekati, preporučujem čitanje ovog članka:



https://planb.academy/tutorials/privacy/on-chain/remix-whirlpool-2b887bd9-8a6a-4dca-8aa9-a1c33682b0aa

Da biste videli broj remiksa izvedenih za svako od vaših dela, otvorite meni `UTXOs` u nalogu `Postmix`.



![Image](assets/fr/13.webp)



Da biste potrošili svoje mešane novčiće, idite na Ashigaru aplikaciju, koja koristi isti wallet kao vaš Ashigaru Terminal softver. wallet prikazan pri otvaranju odgovara vašem `Deposit` nalogu. Da biste pristupili `Postmix` nalogu, koji sadrži vaše mešane UTXO-e, kliknite na Whirlpool simbol u gornjem desnom uglu.



![Image](assets/fr/14.webp)



Na ovom nalogu, videćete sve vaše novčiće koji se trenutno mešaju. Da biste ih potrošili, pritisnite simbol `+` u donjem desnom uglu ekrana, a zatim izaberite `Pošalji`.



![Image](assets/fr/15.webp)



Popunite detalje vaše transakcije: adresu primaoca, iznos koji se šalje, i, ako želite, izaberite specifičnu strukturu transakcije kako biste dodatno poboljšali vašu poverljivost (pogledajte odgovarajuće tutorijale).



![Image](assets/fr/16.webp)



Pažljivo proverite detalje transakcije, zatim prevucite strelicu na dnu ekrana da potvrdite pošiljku.



![Image](assets/fr/17.webp)



Vaša transakcija je potpisana i emitovana na Bitcoin mreži.



![Image](assets/fr/18.webp)



## Potroši Doxxic Change



Zapamti: Model Whirlpool zasnovan je na izjednačavanju vaših delova na Tx0, pre nego što uđu u bazene. Ovaj mehanizam prekida praćenje UTXO-a. Po mom mišljenju, ovo je najefikasniji coinjoin model, ali ima jedan nedostatak: generiše *kusur* koji ne prolazi kroz coinjoin proces.



Ova promena odgovara UTXO kreiranom za svaki Tx0. Izolovana je na posebnom nalogu nazvanom `Doxxic Change` ili `Bad Bank`, u zavisnosti od softvera, kako bi se izbeglo korišćenje sa vašim drugim UTXO-ima. Ovo je veoma važno, jer ovi UTXO-i nisu pomešani: njihovi tragovi ostaju netaknuti i mogu ugroziti vašu poverljivost uspostavljanjem veze između vas i vaše coinjoin aktivnosti. Zato ih pažljivo rukujte i **nikada ih ne koristite sa drugim UTXO-ima**, bilo da su pomešani ili ne. Kombinovanje toksičnog UTXO sa pomešanim UTXO će poništiti sve dobitke u privatnosti koje ste stekli coinjoin-om.



Za sada, Ashigaru ne nudi direktan pristup ovom nalogu `Doxxic Change` (barem ga ja nisam pronašao). Ova funkcija će verovatno biti dodata u nekom budućem ažuriranju. U međuvremenu, jedini način da povratite ova sredstva je da uvezete vaš seed u Sparrow Wallet. Potonji će obično automatski detektovati da je ovo wallet korišćen sa Whirlpool i omogućiti vam pristup svim četirima nalozima, uključujući nalog `Doxxic Change`. Tada možete trošiti ove UTXO-e kao obične bitkoine sa Sparrow.



Evo nekoliko mogućih strategija za upravljanje vašim deviznim UTXO-ima iz coinjoin-a bez ugrožavanja vaše privatnosti:





- Mešanje u manje grupe:** Ako je vaš toksični UTXO dovoljno veliki da se pridruži manjoj grupi, ovo je generalno najbolja opcija. Međutim, budite oprezni i nikada ne spajajte nekoliko toksičnih UTXO-a da biste to postigli, jer će to stvoriti vezu između vaših različitih unosa u Whirlpool.





- Označite ih kao nepotrošive:** Još jedan razuman pristup je jednostavno ih zadržati takvima kakvi jesu na njihovom zasebnom računu i ostaviti ih netaknutima. Ovo će vas sprečiti da ih slučajno potrošite. Ako vrednost bitcoina poraste, novi fondovi prilagođeni njihovoj veličini mogli bi biti otvoreni.





- Donirajte:** Možete odlučiti da ove toksične UTXO-ove pretvorite u donacije za Bitcoin programere, open-source projekte ili udruženja koja prihvataju BTC. Ovo vam omogućava da ih korisno zbrinete dok podržavate ekosistem.





- Kupite prepaid poklon kartice ili Visa kartice:** Platforme poput [Bitrefill](https://www.bitrefill.com/) omogućavaju vam da zamenite svoje bitkoine za poklon kartice ili punjive Visa kartice koje se mogu koristiti u prodavnicama. Ovo može biti jednostavan i diskretan način da potrošite svoje toksične UTXO-e.





- Zamenite ih za Monero:** Samourai Wallet je nekada nudio sada nepostojeću BTC/XMR atomsku zamenu uslugu. Ako slična usluga postoji (ne znam ni za jednu lično), to je odlično rešenje za izolovanje ovih UTXO-a, konvertovanje u Monero, a zatim eventualno slanje nazad na Bitcoin. Međutim, ova metoda je bila skupa i zavisila je od dostupne likvidnosti.





- Prenesite ih na Lightning Network:** Prenošenje ovih UTXO-a na Lightning Network kako biste iskoristili smanjene naknade za transakcije je potencijalno zanimljiva opcija. Međutim, ova metoda može otkriti određene informacije u zavisnosti od vaše upotrebe Lightning-a, te bi stoga trebalo da se koristi sa oprezom.



## Kako mogu saznati više o kvalitetu naših coinjoin ciklusa?



Da bi coinjoin bio zaista efikasan, mora da pokaže visok stepen uniformnosti između ulaznih i izlaznih iznosa. Ova uniformnost povećava broj mogućih interpretacija za spoljnog posmatrača, što zauzvrat povećava neizvesnost u vezi sa transakcijom. Da bismo izmerili ovu neizvesnost, koristimo koncept entropije primenjen na transakciju. Model Whirlpool je prepoznat kao jedan od najefikasnijih u tom pogledu, jer garantuje odličnu homogenost između učesnika. Za detaljniji pregled ovog principa, preporučujem da pogledate poslednje poglavlje 5. dela BTC 204 kursa obuke.



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Performanse nekoliko ciklusa coinjoin-a meri se veličinom skupova u kojima je novčić skriven. Ovi skupovi definišu ono što je poznato kao *anonsetovi*. Postoje dve vrste: prva meri poverljivost u slučaju retrospektivne analize (od sadašnjosti ka prošlosti), a druga meri otpornost na perspektivnu analizu (od prošlosti ka sadašnjosti). Za potpuno objašnjenje ova dva indikatora, molimo vas da pročitate sledeći vodič (ili, još jednom, BTC 204 kurs obuke):



https://planb.academy/tutorials/privacy/on-chain/remix-whirlpool-2b887bd9-8a6a-4dca-8aa9-a1c33682b0aa

## Kako upravljati postmixom?



Nakon što izvršite nekoliko ciklusa coinjoin-a, najbolja strategija je da zadržite svoje UTXO-e na `Postmix` računu, dopuštajući im da se neograničeno remiksuju dok ih zaista ne budete morali potrošiti.



Neki korisnici preferiraju da prebace svoje mešane bitkoine na wallet osiguran wallet hardverom. Ova opcija je moguća, ali zahteva određeni nivo rigoroznosti kako bi se osiguralo da poverljivost stečena sa coinjoin-ima nije ugrožena.



Spajanje UTXO-a je najčešća greška. Važno je nikada ne kombinovati mešane UTXO-e sa nemšanim UTXO-ima u istoj transakciji, inače rizikujete aktiviranje *Common Input Ownership Heuristic (CIOH)*. Ovo podrazumeva rigorozno upravljanje vašim UTXO-ima, naročito kroz jasno i precizno označavanje. Generalno govoreći, spajanje UTXO-a je loša praksa koja često dovodi do gubitka poverljivosti kada se loše upravlja.



https://planb.academy/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

Takođe treba biti oprezan prilikom konsolidacije mešanih UTXO-a. Ograničene konsolidacije mogu se razmotriti ako UTXO-i imaju značajne anonsete, ali one neizbežno smanjuju vaš nivo poverljivosti. Izbegavajte masovne ili ubrzane konsolidacije, sprovedene pre dovoljnog broja remiksa, jer bi mogle uspostaviti inferencijalne veze između vaših delova pre i posle mešanja. U slučaju sumnje, najbolje je ne konsolidovati vaše postmix UTXO-e i prenositi ih jedan po jedan na vaš wallet hardver, generišući svaki put novu praznu adresu za prijem. Ne zaboravite označiti svaki preneti UTXO.



Snažno savetujemo da ne premeštate svoje postmix UTXO-e u portfolije koristeći manjinske skripte. Na primer, ako ste učestvovali u Whirlpool iz multi-sig portfolija u `P2WSH`, biće vas malo koji delite ovu vrstu skripte. Slanjem svojih postmix UTXO-a na ovu istu vrstu skripte, značajno smanjujete svoju anonimnost. Pored vrste skripte, drugi specifični wallet otisci prstiju mogu ugroziti vašu poverljivost, tako da je najbolje da ih potrošite iz Ashigaru aplikacije.



Konačno, kao i kod svih Bitcoin transakcija, nikada ne koristite ponovo adresu za primanje. Svaka uplata mora biti poslata na novu, jedinstvenu, praznu adresu.



Najjednostavniji i najsigurniji metod je da pustite svoje pomešane UTXO-ove da odmaraju na njihovom `Postmix` nalogu, da se prirodno remiksuju, i da ih trošite samo kada je potrebno iz Ashigaru.



Novčanici Ashigaru i Sparrow uključuju dodatne mere zaštite protiv najčešćih grešaka povezanih sa analizom blokčejna, pomažući vam da očuvate poverljivost vaših transakcija.