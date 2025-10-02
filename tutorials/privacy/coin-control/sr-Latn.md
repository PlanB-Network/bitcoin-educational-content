---
name: Coin Control
description: Upoznajte se sa Coin Control, ključnim alatom za zaštitu vaše privatnosti na Bitcoinu
---
![cover](assets/cover.webp)


*Ovaj tutorijal je uvezen iz [lekcije Officine Bitcoin](https://officinebitcoin.it/lezioni/coinco/).*



## Uvod



Stabilnost Bitcoin protokola obezbeđena je jednostavnim ključnim konceptima. Među njima se izdvaja transparentnost: sve Bitcoin transakcije su javne i lako proverljive od strane bilo koga. Iako je ova karakteristika kamen temeljac protokola, jer sprečava prevare i garantuje autentičnost sredstava, ona može predstavljati i izazov za poverljivost. **Da li ste se zapitali da li tolika transparentnost može ugroziti vašu privatnost?**



Trebalo bi. Dok je akumuliranje Satoshi non-kyc prilično lako, vaša privatnost je najviše ugrožena upravo u fazi trošenja.



### Šta se dešava kada potrošite UTXO



Trošenje Bitcoin nije samo prenos vrednosti na nekog drugog.



Konzumiranjem jednog od vaših UTXO-a, morate zapravo ispuniti uslove nametnute za transparentnost protokola, jer imate obavezu da dokažete da posedujete ta sredstva. Stoga postajete odgovorni za :




- izložite svoj javni ključ;
- proizvedi digitalni potpis.



Vreme trošenja je stoga najkritičnije: **trošenje Bitcoin je čin koji treba obaviti svesno i sa što više kontrole**.



## Coin Kontrola



U Bitcoin protokolu, stavke kao što su _račun_ ili _novčane jedinice_ ne postoje. Koncept UTXO je odlično objašnjen u sledećem kursu, koji toplo preporučujem:



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Sa Bitcoin ono što akumulirate i kasnije trošite su male ili velike jedinice računa merene u Satoshi, predstavljene kao `nepotrošeni izlazi transakcija`, **UTXO**, takođe nazvani `novčići`. Kada koristite UTXO-e za kreiranje transakcije, oni su potpuno uništeni i drugi UTXO-i se stvaraju na njihovom mestu.



Softverski novčanici su razvijeni da automatski donose ovaj izbor, koristeći "nasumično" odabrane kovanice, usvajajući određene algoritme koje obezbeđuje protokol. Jedini kriterijum koji ovi algoritmi ispunjavaju jeste da pokriju potrebnu sumu za trošenje.



Oni mogu mešati UTXO-e različitih starosti, ili favorizovati trošenje najnovijih ili "najstarijih," u zavisnosti od algoritma koji su izabrali programeri. Najbolji Softverski Novčanici, takođe planiraju da ostave korisniku važan izbor.



Priručnik `Coin Control`, koji možete pronaći i pod nazivom `Coin Selection`, je funkcija nekih Softverskih Novčanika koja vam omogućava da **ručno odaberete UTXO-e za trošenje kada kreirate svoju transakciju**.



Pretpostavimo da imamo Wallet sa 3 UTXO-a od 21,000, 42,000 i 63,000 Satoshi, respektivno.



![img](assets/en/01.webp)



Ako morate potrošiti 24,000 Sats i dozvoliti algoritmu da izvrši automatski odabir, dobar Software Wallet bi mogao odabrati da kombinuje UTXO 1 + UTXO 2 kako bi platio 24k Sats i Miner naknade, stvarajući ostatak koji se vraća na interni Address početnog Wallet.



![img](assets/en/02.webp)



Nakon transakcije, nova situacija u Wallet, računajući samo UTXO-e, može se rezimirati na sledeći način.



![img](assets/en/03.webp)



Međutim, sa pravim softverom i vašom svesnošću, mogli ste doneti drugačiji, na neki način ispravniji izbor. Na primer, odabirom samo UTXO2 (od 42,000 Sats).



![img](assets/en/04.webp)



Sa krajnjom situacijom u vašem Wallet, na nivou UTXO, koja izgleda drugačije nego ranije.



![img](assets/en/05.webp)



## Zašto ručni coin control?



![img](assets/en/06.webp)



U dva gornja primera, saldo je zapravo isti `108,280 Sats`. Nakon trošenja 24,000 Sats, bez ručnog odabira imali bismo 2 UTXO u Wallet; sa ručnom kontrolom Coin imamo ukupno 3.



Pitanje koje bismo mogli postaviti sebi je sledeće: **zašto raditi sve ovo?** Postoje, ili bi mogli postojati, različiti razlozi zbog kojih nismo koristili `UTXO1` **i svi oni leže u osnovi toga zašto je — prilikom trošenja — aktiviranje ručne coin control jedna od dobrih praksi koje treba slediti**.



Odabir UTXO-a omogućava vam da favorizujete neke aspekte u odnosu na druge. Izbor zaista zavisi od ciljeva koje želite postići.



### Privatnost



Jedna od glavnih prednosti, kada je reč o ručnoj kontroli Coin, jeste **veća privatnost za potrošača**. Uzmimo uvek naš primer: trošak od 24,000 Satoshi _bez ručnog izbora Coin_. Pošto su Blockchain od Bitcoin javni zapis, spoljašnji posmatrač može izjaviti, bez trunke sumnje, da ulazi `UTXO1 od 21,000 Sats` i `UTXO2 od 42,000 Sats`, kao i ostali, `UTXO5 od 38,280 Sats` **sva tri pripadaju istom korisniku**.



Ručnim odabirom `UTXO2`, s druge strane, `UTXO1` ostaje potpuno rezervisan, čekajući u UTXO skupu da bude potrošen u prikladnije vreme.



`UTXO1` bi mogao doći iz KYC izvora, kao što je uplata primljena u Exchange za robu i usluge, dok ostali UTXO-i ne dolaze. Mešanje UTXO-kyc sa drugima koji su poverljiviji kompromituje anonimnost skupa sredstava koja nisu kyc.



**KYC sredstva bi neizbežno dovela do otkrivanja identiteta platioca. Da je to tvoj novčanik, da li bi želeo da spoljašnji posmatrač može da otkrije tvoj identitet sa tolikom apsolutnom sigurnošću?**



Pokušajte onda razmotriti da Novčanici koji implementiraju ručni odabir UTXO-a, na primer, omogućavaju **separaciju jednog ili više UTXO-a**, funkciju koja se koristi kada se takve situacije pojave.



Iako sam uveren da KYC sredstva treba čuvati u zasebnom Wallet nego Bitcoin kupljenom bez kyc, ako je ovo vaš slučaj, segregacija nekih vaših adresa je ključna pomoć, koju biste mogli iskoristiti učenjem kako ručno odabrati svoje ulaze za trošenje.



### Štednja na naknadama



Odabir pravog UTXO za izvršenje troška, **omogućava optimizaciju naknada**. Ponovo, počevši od našeg početnog primera, Software Wallet je odabrao dva UTXO-a da pokrije trošak koji treba napraviti. Dva UTXO-a podrazumevaju dva potpisa koja treba prikazati mreži. Iz toga sledi da transakcija ima veću "težinu" u smislu vBytes.



S druge strane, koristeći ručnu kontrolu Coin, možete odabrati samo jedan koji je dovoljan da pokrije iznos, štedeći naknade smanjenjem "težine" transakcije.



U vremenima kada su naknade visoke, ali ste primorani da potrošite Bitcoin On-Chain (npr., da otvorite Lightning Network kanal), tada se Coin kontrola pokazuje kao pravi ekonomski podsticaj kojem treba da se okrenete.



### Agregacija ostataka



Kada izvršite uplatu i koristite Bitcoin On-Chain, mogućnost dobijanja kusura gotovo uvek postaje izvesnost. Svaki ostatak je sam po sebi mali gubitak privatnosti, jer otkriva mreži (a posebno primaocu uplate) jedan Address vaš koji može biti povezan sa vašim izvornim ulazom.



S obzirom na to da najbolji Wallet HD-ovi generate specijalne adrese za ostatke, možete ih lako prepoznati i "razdvojiti" sve ostatke raznih transakcija; kada dostignu određeni iznos, možete ih ručno odabrati i konsolidovati, ili prebaciti na Lightning Network (moj omiljeni metod) i obraditi ih kako biste povratili privatnost izgubljenu prilikom trošenja.



### Trošak od Cold Wallet



Cold Wallet je instrument s kojim se može razumno postići dobar stepen sigurnosti, za čuvanje bilo koje količine sredstava na duži vremenski period. Međutim, nepredviđeni događaji se mogu desiti, pa se javlja potreba da se dođe do ušteđevine i pokriju neki neočekivani troškovi.



Ne znam koliko njih može deliti moj pristup, ali moj savet je da **nikada ne vršite trošak direktno sa Cold Wallet, kako biste izbegli primanje kusura između adresa istih**. Naučite da ručno birate UTXO-ove potrebne za pokrivanje troška, prebacite ih na Wallet Hot i pripremite svoju transakciju sa potonjeg. Bilo koji kusur, zatim, možete poslati nazad na Cold Wallet Address (ako je iznos adekvatan), koristiti ga za druge troškove, ili ga još uvek segregirati kao što smo upravo videli.



## Praktična prezentacija


Nakon tehničkog uvoda u `zašto`, pogledajmo kako primeniti ručno upravljanje Coin u praksi sa različitim softverom, desktop i mobilnim. Uvek ćemo koristiti isti Wallet BIP39, importovan u svaki od izabranih alata, kako bismo vam pokazali male razlike između njih.



## Wallet Desktop



### Sparrow



Ako koristite Sparrow, otvorite svoj Wallet i izaberite _UTXOs_ iz menija sa leve strane. Videćete listu svih UTXO-a povezanih sa vašim Wallet.



Jednostavno kliknite mišem na jedan od njih i zatim izaberite _Send Selected_. Sparrow vam takođe prikazuje ukupno dostupno za trošenje nakon izbora, odmah pored komande. Grafički, Sparrow vam prikazuje izabrani UTXO tako što ga ističe plavom bojom.



![img](assets/en/07.webp)



Možete odabrati i više od jednog. Pomoću tastera _CTRL_ odaberite neuzastopne UTXO-ove na listi.



![img](assets/en/08.webp)



Nakon ručnog odabira UTXO, možete početi sa izgradnjom transakcije, a Sparrow će vam grafički prikazati kako je ona konstituisana.



![img](assets/en/09.webp)



#### Segregacija UTXO



Razdvajanje sredstava znači "zaključavanje" unutar Wallet tako da se ne mogu koristiti kao ulaz u transakciju. Sparrow omogućava ovu funkcionalnost, koja se uvek pristupa iz menija _UTXOs_: postavite miš preko UTXO koji želite "zaključati" i kliknite desnim tasterom miša. Među opcijama ovog postupka pojaviće se _Freeze UTXO_. Ovako ćete moći da razdvojite novčiće sa Sparrow novčanicima.



![img](assets/en/29.webp)



### Elektrum



Ako je vaša Wallet radna površina Electrum, trebalo bi da znate da možete ručno izabrati UTXO-e bilo iz menija _Addresses_ ili iz menija _Coins_. U oba menija, izbor se vrši tako što se miš usmeri na željeni UTXO i odabere _Add to Coin control_ nakon desnog klika.



![img](assets/en/10.webp)



Čak i sa ovim softverom možete odabrati više od jednog UTXO, pomažući sa _CTRL_ tasterom na vašoj tastaturi ako nisu jedan do drugog.



![img](assets/en/11.webp)



Grafički, Electrum će vam prikazati izbor isticanjem odabranih UTXO-a u Green, dok će se na dnu pojaviti traka, istaknuta istom bojom, koja prikazuje raspoloživi saldo nakon kontrole Coin.



![img](assets/en/12.webp)



Kada odaberete izlaz, ili izlaze, možete kreirati svoju transakciju kao što to obično činite iz menija _Pošalji_.



#### Segregacija UTXO



Electrum pruža ovu funkcionalnost odlaskom u meni _Coins_, gde ćete odabrati određeni UTXO, a zatim desnim klikom izabrati _Freeze_. Možete "zamrznuti" Address čak i bez sredstava iz menija _Addresses_, ili "Coin" da ga ne potrošite.



![img](assets/en/28.webp)



### Nunchuk



Nunchuk vam omogućava da ručno izaberete UTXO-ove iz glavnog menija kada je otvoren. Pokrenite Nunchuk i kliknite _View coins_.



![img](assets/en/13.webp)



Ovo otvara prozor koji sadrži sve UTXO-ove u vašem Wallet, gde možete odabrati jedan ili više aktiviranjem oznake pored svakog iznosa. Nakon što napravite izbor, nastavite sa _Kreiraj transakciju_.



![img](assets/en/14.webp)



Nakon toga možete uneti odredište Address i postaviti iznos i naknade.



![img](assets/en/15.webp)



#### Segregacija UTXO



Radi potpunosti, Nunchuk takođe omogućava među svojim funkcijama, da segregira jedan (ili više) UTXO-a i to čini na dva različita načina. Pristupite meniju _View coins_ i ručno izaberite sa liste novčića. Zatim kliknite na meni _More_ u donjem desnom uglu: pojaviće se lista opcija, iz koje možete izabrati _Lock coins_.



![img](assets/en/39.webp)



![img](assets/en/40.webp)



Takođe možete kliknuti u prostor rezervisan za UTXO, da biste pristupili prozoru _Detalji o novčiću_. Ovde se komanda za zaključavanje/otključavanje dotičnog UTXO pojavljuje u gornjem desnom uglu.



![img](assets/en/41.webp)



### Blockstream App



Blockstream App desktop, formerly known as Green, allows you to make Coin selection when you have already started building the transaction. Therefore, open your Wallet and click on _Send_.



![img](assets/en/16.webp)



Zalepite odredište Address u odgovarajuće polje, a zatim izaberite _Ručno biranje Coin_.



![img](assets/en/17.webp)



Ovo otvara prozor gde možete izabrati jedan ili više UTXO novčića. U primeru ispod, izabrali smo dva novčića. Nakon toga, potvrdite svoj izbor klikom na _Confirm Coin Selection_.



![img](assets/en/18.webp)



Postavite iznos i naknade, a zatim nastavite normalno sa svojom transakcijom.



![img](assets/en/19.webp)



⚠️ N.B. U meniju _Coins_ na Green nalaze se stavke _Lock_/_Unlock_ koje nagoveštavaju mogućnost segregacije UTXO. Ova funkcija se aktivira samo na takozvanim Multisig nalozima; takođe se aktivira samo odabirom UTXO vrlo male vrednosti, blizu praga `Dust`.



## Wallet mobilni



Novčanici se takođe mogu birati sa mobilnog, što omogućava ručno biranje UTXO-a. Pogledajmo Blue Wallet kao prvi primer.



### Plava Wallet



Ako ste korisnik ovog Wallet, otvorite ga i kliknite da uđete u kontrolne ekrane povezane s jednim od vaših Novčanika. Da biste pristupili kontrolnom priručniku za Coin, morate ući u fazu trošenja, a zatim kliknite _Pošalji_.



![img](assets/en/21.webp)



Na sledećem ekranu izaberite menije označene sa tri tačke u gornjem desnom uglu. Otvara se padajući prozor sa nizom komandi. Izaberite poslednju: _Coin Control_.



![img](assets/en/22.webp)



U ovom trenutku Blue Wallet prikazuje sve vaše UTXO-e. Pored iznosa, oni su grafički diferencirani različitim bojama.



![img](assets/en/27.webp)



Izaberite UTXO, zatim izaberite _Use Coin_.



![img](assets/en/23.webp)



Plavi Wallet vas vraća na prozor _Send_ kako biste nastavili sa kreiranjem transakcije. Podesite iznos i naknade, nakon čega birate _Next_.



![img](assets/en/24.webp)



U ovom trenutku možete završiti transakciju, kao što to obično radite.



#### Razdvajanje UTXO



Plavi Wallet takođe vam omogućava da segregirate UTXO-e, čineći ih nedostupnim za trošenje, što nije loša funkcija za Wallet sa mobilnog uređaja. Pristupate kontroli Coin sa upravo objašnjenom procedurom i, nakon odabira UTXO, birate _Freeze_ umesto _Use Coin_.



![img](assets/en/26.webp)



### Nunchuk



Mobilna verzija Nunchuk takođe pruža mogućnost korisniku da vrši kontrolu Coin. Ako koristite ovu aplikaciju sa mobilnog uređaja, otvorite je i idite na meni _Wallet_. Odatle izaberite _View coins_.



![img](assets/en/30.webp)



U prozoru gde se pojavljuje lista UTXO-a, kliknite na _Select_.



![img](assets/en/38.webp)



Pored svakog UTXO pojavljuje se funkcija za izbor. Kao u desktop verziji, ručni izbor na Nunchuk mobilnom se vrši označavanjem malog kvadratića pored iznosa. Ekran prikazuje broj odabranih UTXO-a i ukupan raspoloživi iznos. Kada završite, kliknite na simbol ₿ u donjem levom uglu, što je komanda za početak izrade transakcije.



![img](assets/en/31.webp)



Sada možete dovršiti transakciju, odabrati iznos i kliknuti _Nastavi_.



![img](assets/en/32.webp)



Nastavite kao i uvek, lepljenjem odredišta Address, opisom i podešavanjem naknada za prilagođavanje.



#### Segregacija UTXO



Takođe možete segregirati UTXO-e pomoću mobilnog Nunchuk-a. Pristupite prozoru sa listom posvećenih novčića i izaberite strelicu pored UTXO koji želite da segregirate.



![img](assets/en/42.webp)



Videćete prostor rezervisan za _Detalje o novčiću_, gde možete izabrati _Zaključaj ovaj novčić_.



![img](assets/en/43.webp)



### Bitcoin Keeper



Bitcoin Keeper je poslednji Wallet koji ćemo videti u ovom vodiču. Vidimo njegovu funkcionalnost primenjenu na Coin kontrolu sa Wallet single-sig, iako takva upotreba nije svrha ove veoma specifične aplikacije. Nakon što instalirate Keeper na svom telefonu, pokrenite ga i otvorite Wallet koji sadrži neka sredstva. U centru glavnog ekrana kliknite _View All Coins_.



![img](assets/en/34.webp)



Keeper prikazuje pregled UTXO-a. Da biste pristupili ekranu za odabir, kliknite _Select To Send_.



![img](assets/en/35.webp)



Možete odabrati novčiće tako što ćete ih označiti klikom na odgovarajuću komandu. Kada završite, kliknite _Pošalji_.



![img](assets/en/36.webp)



Bitcoin Keeper vas vodi direktno u meni _Send_, gde možete kreirati transakciju sa odabranim UTXO-ima.



![img](assets/en/37.webp)



## Hardware Wallet



Svaki od Softverskih Novčanika prikazanih u ovom vodiču može biti samo za gledanje Interface za jedan od vaših Hardverskih Novčanika. To znači da se Coin kontrola za uređaj za offline potpisivanje izvodi koracima viđenim do sada.



### Opšte preporuke



Coin kontrola je veoma efikasna praksa za odabir ulaza vaših transakcija. Ručni odabir je još efikasniji ako ste, prilikom kupovine/primanja vaših sredstava, dobro označili izvor vaših Satošija. Ako želite dobro naučiti ovu tehniku, preporučujem sledeći vodič:



https://planb.network/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

Ranije smo razgovarali o `segregation of remains`. Ako želite zaključati ostatke za kasniju obradu i povratiti privatnost (swap na Layer 2), morate se pobrinuti da ih `label` svaki put kada primite jedan. Od Softverskih Novčanika viđenih do sada, samo Electrum grafički boji UTXO ostatke kako bi bili vidljivi na prvi pogled. Drugi, kao što je Sparrow, prikazuju vam lanac u putanji derivacije pojedinačnog UTXO (`m/84'/0'/0'/1/11`).



Da biste ovu tehniku primenili efikasno, zapamtite da uvek dodate opis na kusur koji primite: osoba kojoj ste poslali svoja sredstva (uplata, tutorijal ili drugo), zna Address povezan sa kusurom i zna da pripada vama, jer dolazi iz transakcije koju ste zajedno obavili!