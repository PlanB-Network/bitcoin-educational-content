---
name: Uvod u Bitcoin mining
goal: Razumevanje Bitcoin mining i proof-of-work od početka
objectives: 


  - Razumeti proof-of-work i njegovu ulogu u Bitcoin.
  - Analizirajte mehanizam prilagođavanja težine.
  - Znajte šta tehnički termini povezani sa mining zapravo znače.
  - Opišite korake uključene u izgradnju Bitcoin bloka i njegove komponente.
  - Identifikujte glavne razvoje u industriji mining.


---

# Otkrijte osnove Bitcoin mining



Da biste razumeli proof of work, morate razumeti kako Bitcoin funkcioniše. Bez ovog izuma i njegove genijalne upotrebe, Bitcoin jednostavno ne bi mogao postojati. Ovaj kurs vam pruža svu teoriju mining koju trebate za vaše bitcoin putovanje.



MIN 101 je prvenstveno namenjen početnicima, jer objašnjava sve pojmove precizno od samog početka. Međutim, ako već imate srednji nivo znanja, ovaj kurs će vam omogućiti da konsolidujete svoje razumevanje, ispravite neke približne intuicije i istražite detalje koji često nedostaju u uobičajenim objašnjenjima.



Do kraja ovog kursa, moći ćete da objasnite kako proof-of-work funkcioniše na jednostavan i rigorozan način. MIN 101 je takođe idealan uvod u sve druge naprednije kurseve posvećene Bitcoin mining na Plan ₿ Academy, bilo teoretske ili praktične.



+++


# Uvod


<partId>041ff0fa-53c3-4d55-9888-d7840de283e9</partId>



## Pregled kursa


<chapterId>a82d49dc-d68a-4e3f-985e-bcef6643677e</chapterId>



Dobrodošli na kurs MIN 101, u kojem ćete otkriti osnovne teorijske koncepte mining i Proof-of-Work unutar sistema Bitcoin. Ovaj kurs je prvi korak na vašem bitcoiner putovanju ka razumevanju kako mining funkcioniše. Kada ga završite, moći ćete da pređete na naprednije teorijske kurseve, ili da se praktično uključite i postanete bitcoin rudar!



U ovom kursu MIN 101, nećemo se vraćati na osnovne pojmove Bitcoin, jer ćemo odmah preći na suštinu: mining. Ako nikada niste čuli za Bitcoin, ili ako su vam njegovi osnovni pojmovi još uvek malo nejasni, toplo preporučujem da počnete sa našim uvodnim kursom BTC 101. Kada usvojite ove osnove, moći ćete sa sigurnošću da se uhvatite u koštac sa MIN 101:



https://planb.academy/courses/2b7dc507-81e3-4b70-88e6-41ed44239966


### Deo 1 - Uvod



Počećemo ovaj kurs sa opcionim prvim poglavljem, u kojem nudim veoma pojednostavljeno objašnjenje mining, kako bih vam pružio jasnu mentalnu sliku pre nego što pređemo na tehničke mehanizme.



Cilj ovde nije da vam damo sve tehničke detalje (oni će doći kasnije u kursu), već da vam pružimo vodič. Kada ovaj okvir bude postavljen, svaki napredniji koncept koji se kasnije uvede prirodno će se uklopiti u ovu strukturu.



### Deo 2 - Kako proof of work funkcioniše



Nakon uvoda, Deo 2 je tehnička osnova programa obuke. Njegov cilj je da objasni, korak po korak, kako Bitcoin proizvodi validne blokove. Počećemo otkrivanjem strukture bloka, pre nego što pređemo na mehanizam proof-of-work: ulogu cilja, nonce-a i hash funkcije. Na kraju, videćemo kako Bitcoin uspeva da održi stabilnu stopu proizvodnje blokova uprkos varijacijama u hash snazi, zahvaljujući mehanizmu prilagođavanja težine. Na kraju ovog dela, imaćete potpuno razumevanje osnovnih principa Bitcoin-ovog proof-of-work.



### Deo 3 - Sistem podsticaja Bitcoin mining



U trećem delu, pogledaćemo zašto su rudari podstaknuti da učestvuju pošteno u mining. Detaljno ćemo objasniti princip nagrade za blok, njen sastav i metod izračunavanja, njenu evoluciju tokom vremena kroz prepolovljavanja, i specifičnu ulogu coinbase transakcije.



### Deo 4 - Industrija Bitcoin mining



Četvrti deo vraća mining u njegovu operativnu stvarnost. Prati evoluciju mining mašina, od početka Bitcoin do modernog ASIC, kako bi se razumele trenutne hardverske ograničenja. Takođe razmatramo osnove mining bazena, da bismo razumeli kako rudari uspevaju da smanje varijansu svog prihoda.



### Deo 5 - Završni deo



U završnom delu kursa, možete testirati svoje znanje o mining polaganjem diplome.



Cilj ovog kursa MIN 101 je stoga da vam omogući da odete sa jasnim, strukturiranim i trajnim razumevanjem Bitcoin mining, kako tehnički tako i ekonomski.



Spremni da otkrijete Bitcoin mining? Hajde da počnemo!




## Bitcoin mining olakšan


<chapterId>278577a6-98bb-4659-86c7-f6c4f6d5fa3e</chapterId>



Pre nego što pređemo na detaljno i tehničkije objašnjenje Bitcoin [mining](https://planb.academy/resources/glossary/mining), želeo bih da vam dam pregled principa, koji je namerno jednostavan i shematski. Ako već imate osnovno znanje, možete odmah preći na suštinu u sledećem poglavlju, nakon što odgovorite na pitanja iz kviza. Ovo poglavlje je prvenstveno namenjeno početnicima, kako bi vam pružilo lagan početak.



Zamislite Bitcoin kao veliku javnu beležnicu, koju svi dele, gde beležimo ko je kome poslao bitkoine. Ova beležnica se zove [blokčejn](https://planb.academy/resources/glossary/blockchain). Ne može je držati samo jedna osoba, inače bi joj se moralo verovati. Umesto toga, Bitcoin radi kolektivno: hiljade računara verifikuju i održavaju istu verziju ove beležnice.



![Image](assets/fr/049.webp)



U Bitcoin, kada izvršite uplatu, kreirate [transakciju](https://planb.academy/resources/glossary/transaction-tx). Ova transakcija nije odmah dodata u beležnicu. Prvo se šalje na mrežu, zatim čeka da bude integrisana u sledeći paket transakcija. Ovaj paket se zove [blok](https://planb.academy/resources/glossary/block).



![Image](assets/fr/050.webp)



Blok je jednostavno skup transakcija grupisanih zajedno. Kada je blok spreman, nije dovoljno samo ga objaviti. Morate dokazati mreži da je blok vredan dodavanja u bazen. Tu dolazi mining.



Mining je rad validacije bloka trošenjem energije. Akteri zvani [rudari](https://planb.academy/resources/glossary/miner) koriste specijalizovane računare. Ove mašine troše električnu energiju da bi izvršile veoma veliki broj testova, u petlji, sve dok ne pronađu dokaz koji mreža prihvata. Kada rudar pronađe ovaj dokaz, njegov blok se smatra validnim.



Kada je blok validiran, on se emituje na mrežu. Ostali [čvorovi](https://planb.academy/resources/glossary/node) brzo proveravaju da li je u skladu sa pravilima, a zatim ga dodaju u niz prethodnih blokova. Zato se zove "blokčejn": svaki novi blok dolazi posle drugih, u sekvencijalnom redosledu, i ovaj lanac raste malo po malo.



![Image](assets/fr/051.webp)



Da rezimiramo, transakcije se prvo kreiraju. Zatim se grupišu zajedno u blok. Potom, rudar validira ovaj blok trošeći električnu energiju. Na kraju, ovaj blok se dodaje u blokčejn, i transakcije koje sadrži postaju [potvrđene](https://planb.academy/resources/glossary/confirmation).



Ako rudari troše struju, to nije zato što su volonteri. Oni to rade zbog nagrade. Kada rudar validira blok, dobija dve vrste prihoda. S jedne strane, dobija novoizgenerisane bitkoine. S druge strane, prikuplja [naknade](https://planb.academy/resources/glossary/transaction-fees) koje plaćaju korisnici za transakcije uključene u blok. Drugim rečima, rudar je kompenzovan i kroz programirano izdavanje novca i kroz transakcione naknade koje određuje tržište.



U ovoj fazi, namerno vam je dat veoma jednostavan prikaz mining. Još uvek ne objašnjava kako je blok konstruisan u detalje, ili kako tačno funkcioniše dokaz koji rudari traže, ili kako Bitcoin održava stalan tempo, ili kako se nagrada precizno izračunava, ili kako se preuzima. To je u redu, to je sve što ćemo videti u ostatku ovog kursa MIN 101!



Cilj ovog poglavlja bio je jednostavno da vam pruži jasnu mentalnu strukturu: transakcije → blokovi → mining → blokčejn → nagrada. Držite ovaj lanac ideja na umu. U ostatku kursa, svako poglavlje će dodati sloj tehničkih detalja na jedan od ovih elemenata, sve dok ne razumete ne samo šta se dešava, već i kako i zašto to funkcioniše pouzdano, u velikom obimu, bez šefa i bez potrebe za poverenjem.



# Kako proof of work funkcioniše


<partId>e917e8e3-37f2-46fb-91b2-6a5ce6f0f5c3</partId>



## Putanja transakcije Bitcoin


<chapterId>3b7a3502-4814-4554-8de1-86ac961a2958</chapterId>



Da bismo razumeli o čemu se radi kod Bitcoin mining, prvo moramo pratiti put tipične Bitcoin transakcije. Ovo će vam tačno pokazati gde blok dolazi u igru i zašto je on u srcu sistema. To je ono što bih voleo da otkrijete u ovom prvom poglavlju.



U Bitcoin, transakcija je struktura podataka koja prenosi vlasništvo nad bitkoinima sa jednog korisnika na drugog. U konkretnim terminima, ona troši `outputs` iz prošlih transakcija (tzv. [UTXOs](https://planb.academy/resources/glossary/utxo)), referišući se na njih kao `inputs`, a zatim kreira nove `outputs` koji definišu kome ovi bitkoini sada pripadaju i pod kojim uslovima mogu biti potrošeni kasnije.



![Image](assets/fr/001.webp)



Važna tačka o Bitcoin je autorizacija za trošenje. Bitcoin nisu na računu, kao što bi vaš novac mogao biti u banci, već su zaključani uslovima trošenja. Kada [wallet](https://planb.academy/resources/glossary/wallet) želi da koristi UTXO kao [ulaz](https://planb.academy/resources/glossary/input), mora da pruži kriptografski dokaz da ima pravo da ga otključa. Ovaj dokaz često ima oblik [digitalnog potpisa](https://planb.academy/resources/glossary/digital-signature) generated iz [privatnog ključa](https://planb.academy/resources/glossary/private-key). Zato bitkoineri insistiraju na obezbeđivanju vaših privatnih ključeva: oni su ti koji otključavaju pristup vašim bitkoinima i, samim tim, omogućavaju vam da ih trošite.



![Image](assets/fr/002.webp)



Digitalni potpis u Bitcoin ima dve važne uloge:




- Autorizuj trošak: ovo dokazuje da korisnik poseduje privatni ključ koji se očekuje prema UTXO uslovu troška;
- Zaštita integriteta: povezuje autorizaciju sa preciznim detaljima transakcije (primaoci, iznosi, naknade, itd.). Ako neko izmeni transakciju nakon toga, potpis više neće biti važeći.



Kada je transakcija ispravno konstruisana i potpisana od strane korisnikovog Bitcoin wallet, mora biti emitovana na Bitcoin mreži.



### Uloga Bitcoin čvora u distribuciji



Bitcoin je [peer-to-peer](https://planb.academy/resources/glossary/peertopeer-p2p) mreža: ne postoji centralni server koji prima i obrađuje sve transakcije. Ovu ulogu kolektivno igraju čvorovi. Bitcoin čvor je deo softvera (npr. [Bitcoin Core](https://planb.academy/resources/glossary/bitcoin-core)) povezan sa drugim čvorovima u Bitcoin mreži, čija je glavna misija verifikacija, skladištenje i prenos transakcija i blokova.



Kada pošaljete transakciju sa wallet, wallet je prosleđuje čvoru (vašem ili čvoru usluge). Ovaj čvor će prvo proveriti da li transakcija ispunjava različita pravila, kao što su:




- potpisi su važeći;
- ulazi se odnose na postojeće UTXOs (tj. bitcoine koji postoje);
- ove UTXO nisu već potrošene negde drugde;
- količina [izlaza](https://planb.academy/resources/glossary/output) je manja ili jednaka količini ulaza (bitkoini se ne stvaraju ni iz čega);
- itd.



Ako transakcija prođe sve ove provere, čvor je propagira drugim čvorovima u mreži sa kojima je povezan. Oni je zauzvrat proveravaju i prosleđuju dalje, i tako dalje. U roku od nekoliko sekundi, transakcija se propagira i postaje poznata celokupnoj, ili bar velikom delu, Bitcoin mreže.



![Image](assets/fr/003.webp)



### Mempool: čekaonica za transakcije



Između trenutka kada se transakcija emituje i trenutka kada se potvrdi u bloku, mora čekati. Ova zona čekanja se zove **[mempool](https://planb.academy/resources/glossary/mempool)** (skraćenica od `memory` i `pool`). Mempool je stoga privremeni prostor za skladištenje validnih, ali još nepotvrđenih, transakcija.



Važna tačka: ne postoji nešto kao što je jedinstveni mempool, već samo mempoolovi. Svaki čvor održava svoj sopstveni mempool, sa sopstvenim lokalnim ograničenjima. To znači da u bilo kom trenutku, dva čvora mogu imati blago različit sadržaj mempoola (u zavisnosti od toga šta su primili, šta su odbacili ili šta su očistili).



![Image](assets/fr/004.webp)



U ovoj fazi, mreža zna za transakciju, verifikovala ju je i drži je u memoriji dok ne bude potvrđena. Ali potvrda ove transakcije će doći tek kada je rudar ubaci u blok, i taj blok bude prihvaćen od strane mreže.



### Blockchain: javni registar vremenskog označavanja



Kako je bitcoin nematerijalna valuta, mora rešiti jedan problem: sprečavanje [dvostrukog trošenja](https://planb.academy/resources/glossary/double-spending-attack) bez centralnog autoriteta. Ako dve transakcije pokušaju da potroše isti UTXO, svi moraju biti u stanju da se usaglase na jedno, koherentno stanje. Satoshi Nakamoto sumira ovaj problem ovom čuvenom rečenicom:



> Jedini način da potvrdite odsustvo transakcije je da budete upoznati sa svim transakcijama.

Drugim rečima, da biste znali da bitcoin već nije potrošen, potreban vam je zajednički zapis o prošlim troškovima.



Ovo je uloga blockchain-a: javni registar koji sadrži istoriju transakcija. Ali umesto da beleži svaku transakciju kako se dešava, Bitcoin ih grupiše u blokove. Svaki blok deluje kao stranica istorije, i sistem tako funkcioniše kao server za vremensko pečatiranje: on redosledi transakcije tokom vremena na proverljiv način.



Ovaj registar ne može biti prepisan, zahvaljujući jednostavnom principu: svaki blok uključuje kriptografski otisak ([hash](https://planb.academy/resources/glossary/hash-function)) prethodnog bloka. Tako su blokovi povezani: ako izmenite blok iz prošlosti, njegov hash se menja, što prekida vezu sa sledećim blokom, što prekida vezu sa blokom nakon toga, i tako dalje. Upravo ovaj lanac zavisnosti daje "*blockchain*-u" njegovo ime.



![Image](assets/fr/005.webp)



Jednom kada razumemo ove osnovne principe Bitcoin, možemo opisati cilj rudara u konkretnijim terminima: izgraditi novi blok koji proširuje postojeći lanac, upisivanjem transakcija na čekanju, a zatim pokušati da ga učini validnim (ovo je čuveni "[proof of work](https://planb.academy/resources/glossary/proof-of-work)" koji ćemo proučiti u kasnijem poglavlju). Ali prvo, hajde da zajedno otkrijemo u sledećem poglavlju kako se konstruira blok kandidat.



## Izgradnja Bitcoin bloka


<chapterId>2b5cd04b-d400-4865-b0a0-e70fa7e67c17</chapterId>



Sada ste razumeli kako funkcioniše Bitcoin transakcija i ulogu blockchain-a. Međutim, pre nego što detaljnije pogledamo kako funkcioniše proof-of-work, postoji još jedan ključni korak koji rudar mora da izvrši: izgradnja kandidatskog bloka. Hajde da zajedno otkrijemo šta je [kandidatski blok](https://planb.academy/resources/glossary/candidate-block) i kako ga rudar konstruira, pre nego što krenemo u potragu za validnim dokazom.



### Blok kandidata



Miners moraju sami da izgrade svoje blokove pre nego što pokušaju da ih rudare. Svaki rudar, zauzvrat, konstruira ono što je poznato kao kandidat blok iz transakcija koje čekaju u njegovom mempool-u. Izgradnja kandidat bloka se stoga sastoji od:




- izaberite koje transakcije da uključite;
- organizujte ove transakcije na način koji je kompatibilan sa pravilima Bitcoin;
- proizvedi metapodatke bloka, pohranjene u njegovom [zaglavlju](https://planb.academy/resources/glossary/block-header).



Izbor transakcija prati jednostavnu ekonomsku logiku: blok ima kapacitet ograničen protokolom Bitcoin, tako da rudar nastoji da maksimizira ono što zarađuje za ovaj prostor. On kao prioritet bira transakcije koje nude najviše naknade u odnosu na prostor koji zauzimaju u bloku (ovo je poznato kao "stopa naknade", izražena u sats/vB). Detalji o naknadama će biti obrađeni kasnije; samo zapamtite ideju sortiranja prema efikasnosti prostora.



Blok Bitcoin se stoga sastoji od dva glavna dela:




- lista transakcija;
- zaglavlje bloka, koje služi, na neki način, kao lična karta bloka.



![Image](assets/fr/006.webp)



Zaglavlje je ključno, jer se koristi kao osnova za proof-of-work: u Bitcoin, ne kopate ceo blok direktno; kopate samo zaglavlje bloka, koje rezimira informacije potrebne za povezivanje bloka sa lancem i potvrđivanje njegovog sadržaja. Da bi zaglavlje moglo da predstavlja sve transakcije, Bitcoin koristi kriptografski alat: [Merkle stablo](https://planb.academy/resources/glossary/merkle-tree).



### Merkle drvo: sumiranje velikog skupa transakcija



Navođenje svih transakcija u zaglavlju bilo bi nemoguće: blok može sadržati hiljade transakcija, dok zaglavlje ima fiksnu veličinu (80 bajtova). Rešenje je stoga izračunavanje jedinstvenog heša koji zavisi od svih transakcija u bloku: ovo je [Merkleov koren](https://planb.academy/resources/glossary/merkle-root).



Princip je sledeći:




- kriptografski otisak prsta (hash) svake transakcije se izračunava;
- ovi heševi su upareni, konkatenirani, a zatim ponovo heširani da bi formirali novi sloj heševa;
- ovaj proces se ponavlja sve dok se ne dobije jedan konačni heš: Merkle koren.



![Image](assets/fr/007.webp)



Dakle, ako se jedna transakcija promeni, čak i za jedan bit, rezultat je modifikacija njenog otiska prsta, što se propagira do Merkle korena. Ovaj koren je uključen u zaglavlje bloka. Dakle, modifikovanje prošle transakcije znači modifikovanje zaglavlja bloka u kojem je uključena, a samim tim i otiska bloka, i zatim veze sa narednim blokovima.



Od [SegWit](https://planb.academy/resources/glossary/segwit), odvojili smo potpise od ostatka. Dakle, u stvarnosti, postoje 2 Merkle stabla ugnježdena unutar svakog bloka. Ovo razdvajanje ima posledice na način na koji računamo veličinu bloka i za određene kriptografske obaveze, ali osnovna ideja ostaje ista: zaglavlje mora na kompaktan način obuhvatiti sav sadržaj bloka.



### Zaglavlje bloka



Zaglavlje bloka je dugo 80 bajtova i sadrži tačno 6 polja. Upravo će ovih šest elemenata biti heširano prilikom pretrage za proof of work (vidi sledeće poglavlje):





- Verzija (`version`): Ovo označava kojim pravilima ili signalima ažuriranja blok pripada. Služi kao mehanizam za održavanje kompatibilnosti protokola i evolucije.




- Hash prethodnog bloka (`previousblockhash`): Ovo je hash zaglavlja prethodnog bloka. Ovo je ono što povezuje blokove zajedno. Bez ovog polja, imali bismo nezavisne blokove. Uključivanjem hash-a zaglavlja prethodnog bloka, dobijamo lanac, gde svaki novi blok nadograđuje prethodni.





- Merkle root (`merkleroot`): Ovo je otisak svih transakcija u bloku (preko Merkle stabla). Povezuje zaglavlje sa sadržajem: ako rudar promeni izbor ili redosled transakcija, koren se menja.





- [Vremenska oznaka](https://planb.academy/resources/glossary/timestamp): Ovo je vremenska oznaka (Unix vreme) koju bira rudar (sa ograničenjima validnosti), koja mora naznačiti kada je blok iskopan. Ne mora biti savršeno tačna u sekundu, ali mora ispunjavati određene uslove da bi ostala prihvatljiva za mrežu.





- Kodirana [meta težina](https://planb.academy/resources/glossary/difficulty-target) (`nbits`): Ovo polje kodira trenutnu meta težinu. Detaljnije ćemo objasniti u poglavlju o težini, ali zapamtite da je ovaj parametar deo zaglavlja.





- [Nonce](https://planb.academy/resources/glossary/nonce) (`nonce`): Ovo je vrednost koju rudar može slobodno menjati. Služi kao podesiva varijabla tokom proof-of-work. Objasniću njegovu ulogu detaljnije u sledećem poglavlju, ali je važno razumeti da je nonce deo zaglavlja bloka i dizajniran je da omogući uzastopne pokušaje.



Da bi ovo bilo lakše vizualizovati, evo primera zaglavlja bloka u heksadecimalnom formatu (80 bajtova):



```text
00e0ff3f5ffe3b0d9247dc437e18edc19252e4517cee941752d501000000000000000000206b
de3a10826e2acb2f28fba70463601c789293d0c9c4348d7a0d06711e97c0bcb13a64b2e00517
43f09a40
```



Evo analize po poljima:



```text
version: 00e0ff3f
previousblockhash: 5ffe3b0d9247dc437e18edc19252e4517cee941752d501000000000000000000
merkleroot: 206bde3a10826e2acb2f28fba70463601c789293d0c9c4348d7a0d06711e97c0
time: bcb13a64
nbits: b2e00517
nonce: 43f09a40
```



Ovaj kandidat za zaglavlje bloka, konstruisan od strane rudara, čini osnovu njihovog rada. Kada se traži važeći proof-of-work, nije cela lista transakcija ta koja se direktno hešira u petlji, već ovaj blok od 80 bajtova, koji sadrži sve što je potrebno da se blok poveže sa prošlošću i potvrdi njegov sadržaj, dok takođe uključuje parametre neophodne za mining mehanizam, koji ćemo istražiti u narednom poglavlju.



## Hash, cilj i nonce


<chapterId>d054323b-16bd-4556-bac5-4878654e59a3</chapterId>



U prethodnim poglavljima pratili ste putanju Bitcoin transakcije: kreirana i potpisana od strane wallet, preneta od strane čvorova, uskladištena u mempoolovima, zatim potvrđena kada je rudar uključi u blok prihvaćen od strane mreže. Ali još nismo videli kako rudar može dodati svoj blok u blockchain. Koji je proces iza mining?



Razumevanje mining procesa je prilično jednostavno. Sastoji se od 3 koncepta koji idu ruku pod ruku: heš funkcija, ciljana vrednost i promenljiva koju rudar može menjati. Hajde da pogledamo kako sve to funkcioniše.



### Hash funkcija



Heš funkcija je alat koji uzima poruku kao ulaz i proizvodi izlaz fiksne veličine, nazvan "*otiska prsta*" ili "*heš*".



![Image](assets/fr/010.webp)



Heš funkcija je zanimljiva u računarskim sistemima jer ima određene osobine:





- Ako promenite jedan bit ulaza, rezultujući izlazni heš se menja potpuno i nepredvidivo;



![Image](assets/fr/011.webp)





- Nemoguće je preći sa izlaza na ulaz: funkcija je ireverzibilna;



![Image](assets/fr/012.webp)





- Nemoguće je pronaći dve različite poruke koje daju potpuno isti heš.



![Image](assets/fr/013.webp)



Heš funkcija korišćena u Bitcoin za mining je `SHA256`, primenjena dva puta uzastopno. Ovo je poznato kao dupli [SHA256](https://planb.academy/resources/glossary/sha256), ili `SHA256d`. Upravo ovo duplo heširanje proizvodi otisak bloka.



```text
hash = SHA256(SHA256(message))
```



U našem slučaju, `message` zapravo odgovara zaglavlju bloka, koje ste videli u prethodnom poglavlju. Kao podsetnik, zaglavlje je mala struktura koja rezimira sve u bloku.



![Image](assets/fr/014.webp)



### Dokaz o radu: pronalaženje heša manjeg od cilja



Proof-of-Work se često opisuje kao rešenje složenog problema. U stvarnosti, to nije toliko problem koliko potraga metodom pokušaja i pogrešaka: rudar mora pronaći verziju zaglavlja čiji heš (nakon prolaska kroz `SHA256d` heš funkciju) poštuje jednostavan uslov: mora biti manji od određenog cilja.



Ovo stanje je formulisano na sledeći način:




- heš zaglavlja bloka se izračunava korišćenjem heš funkcije;
- tumačimo ovaj heš kao broj;
- da bi blok bio važeći, ovaj broj mora biti manji ili jednak vrednosti koja se zove "*ciljna težina*".



Drugim rečima, blok je važeći ako:



```text
SHA256d(block_header) <= target
```



![Image](assets/fr/015.webp)



Cilj je 256-bitni broj. Pošto je heš koji proizvodi `SHA256d` takođe 256 bita, mogu se porediti kao dva broja. Što je cilj niži, to je uslov teži, jer postoji manje mogućih rezultata ispod ovog praga. Suprotno tome, što je cilj viši, to je uslov lakše ispuniti, i lakše je iskopati blok. Detaljnije ćemo razmotriti kako se ovaj cilj određuje u kasnijim poglavljima.



U ovom sistemu, heš funkcija je zanimljiva. Zapamtite da je lako izračunati izlaz iz ulaza, ali je nemoguće pronaći ulaz znajući samo izlaz funkcije. U mining, od rudara se ne traži da pronađu precizan heš, već da pronađu heš ispod ciljne vrednosti. Jedini način da se to postigne je da se napravi veoma veliki broj pokušaja, sve dok određeni zaglavlje njihovog kandidata bloka, kada se hešira, ne proizvede heš manji od ove ciljne vrednosti.



Kada je cilj dovoljno nizak, ovaj proces postaje skup. Rudar izračunava heš zaglavlja svog kandidatskog bloka, proverava rezultat i, ako uslov nije ispunjen, menja zaglavlje i ponavlja izračunavanje. Ova petlja se ponavlja dok se ne pronađe važeće zaglavlje. Kada heš zaglavlja konačno zadovolji uslov, uspostavlja se proof of work, blok se smatra važećim i može se emitovati na Bitcoin mreži kako bi čvorovi dodali u svoj blokčejn. Pobednički rudar tada prima povezanu nagradu (detaljićemo njen sastav kasnije), dok svi rudari odmah kreću u potragu za novim, važećim zaglavljem za sledeći blok.



Fundamentalna prednost ovog mehanizma leži u njegovoj asimetriji. Proizvodnja proof of work je skupa za rudare, jer zahteva veliki broj hash proračuna. S druge strane, za verifikatore, tj. mrežne čvorove, verifikacija je izuzetno jednostavna: sve što treba da urade je da hashiraju zaglavlje bloka koje je obezbedio rudar i provere da li je dobijeni hash zaista niži od cilja. Pronalaženje dokaza stoga zahteva mnogo rada i resursa, dok je verifikacija njegove validnosti brza i jeftina. Upravo ova osobina definiše efikasan proof-of-work sistem.



### Nonce



Praktično pitanje ostaje: ako zaglavlje kandidatskog bloka koje je konstruisao rudar ne daje važeći heš, kako rudar može pokušati ponovo? On treba da izmeni nešto u zaglavlju kako bi dobio drugačiji heš. Upravo je to uloga nonce-a.



Zapamtite prvo svojstvo heš funkcije: promena jednog bita ulaza je dovoljna da se proizvede potpuno drugačiji i nepredvidiv izlazni heš. Svaka kalkulacija heša je stoga slična nasumičnom izvlačenju.



![Image](assets/fr/016.webp)



Da ponovo okuša svoju sreću, rudar ne mora da menja celu zaglavlje svog kandidatskog bloka: potrebno je samo da promeni mali deo njega, jer čak i jedan drugačiji bit će rezultirati potpuno novim hešom, potencijalno validnim ako je manji od cilja.



Upravo zbog toga zaglavlje bloka sadrži nonce. Nonce je 32-bitna vrednost, koja se koristi jednom i zatim zamenjuje. U praktičnom smislu, za isti kandidat blok, rudar može testirati oko 4.29 milijardi mogućih vrednosti (od `0` do `2^32 - 1`). Svaka varijacija nonce-a menja zaglavlje bloka i, posledično, potpuno menja heš koji se dobija nakon primene `SHA256d` heš funkcije.



mining proces je veoma jednostavan:




- rudar gradi kandidatski blok (transakcije + zaglavlje);
- zatim izračunava heš od `SHA256d(header)`;
- ako je rezultat veći od cilja, menja nonce;
- počinje ponovo;
- itd.



![Image](assets/fr/017.webp)



Zapravo, nonce nije jedino polje koje se može modifikovati. Bilo kakva izmena unutar transakcija bloka rezultira promenom korena Merkle stabla, a samim tim i izmenom zaglavlja tog bloka. Sa savremenom računarskom snagom, prolazak kroz 4,29 milijardi mogućih vrednosti nonce-a može se obaviti relativno brzo. Zato postoji još jedno polje, koje se obično naziva "*[extra-nonce](https://planb.academy/resources/glossary/extra-nonce)*", koje dodatno umnožava mogućnosti varijacije zaglavlja. Vratit ćemo se na ovaj mehanizam detaljnije u kasnijem poglavlju.



### Koja je svrha proof of work?



Nazivamo ga "dokaz" jer je rezultat odmah proverljiv: kada je blok proizveden, bilo koji čvor može proveriti, u deliću sekunde, da li je kriptografski heš njegovog zaglavlja zaista ispod potrebne mete. Nazivamo ga "rad" jer postizanje ovog heša zahteva mnoštvo pokušaja, i stoga pravi trošak u smislu računanja i energije.



U Bitcoin [Belom Papiru](https://planb.academy/resources/glossary/white-paper), Satoshi Nakamoto iznosi dve prednosti korišćenja proof-of-work sistema u Bitcoin:





- Sealing ekonomsku istoriju:**



Jednom kada je računarsko opterećenje potrošeno, blok je zaključan: njegova modifikacija bi zahtevala ponovno izvođenje tog bloka proof of work. A kako su blokovi povezani zajedno, menjanje starog bloka bi takođe značilo preračunavanje svih narednih blokova, a zatim dostizanje i prestizanje tekućeg rada poštenog lanca.



Drugim rečima, proof-of-work služi kao okosnica sistema vremenskog žigosanja, čineći falsifikovanje prošlosti sve skupljim kako se blokovi gomilaju. Kada se iskopa novi blok, sigurnost koju pruža proof of work primenjuje se istovremeno i ravnomerno na sve postojeće UTXO. Sa svakim dodanim blokom, svaki UTXO tako akumulira dodatnu količinu sigurnosti od Proof-of-Work.





- Definišite pravilo većine ([konsenzus](https://planb.academy/resources/glossary/consensus)) i neutralizujte Sybil:**



Proof-of-Work takođe omogućava da Bitcoin postigne konsenzus bez oslanjanja na pravilo glasanja "jedan ID = jedan glas", koje bi se lako moglo izmanipulisati masovnim stvaranjem identiteta (IP adrese, čvorovi, ključevi...).



U Bitcoin, "*većina*" nije najveći broj učesnika, već **lanac koji akumulira najviše rada**. Kao što Satoshi kaže, ovo je princip "jedan CPU = jedan glas", tj. glas koji je ponderisan stvarnom računarskom snagom potrošenom za proizvodnju validnih blokova. Dakle, postavljanje hiljada čvorova samo po sebi ne donosi prednost u odnosu na Bitcoin. Bez dodatne računarske snage, ne akumulira se više dokaza rada, i [Sybil napad](https://planb.academy/resources/glossary/sybil-attack) postaje beskoristan, dok pravilo odlučivanja ostaje objektivno i ne zahteva identifikaciju učesnika.



![Image](assets/fr/018.webp)



[Nakamoto, S. (2008). *Bitcoin: A Peer-to-Peer Electronic Cash System.*](https://bitcoin.org/bitcoin.pdf)



Principi koji se odnose na korisnost i ovlašćenja maloletnika su veoma složena tema, u koju neću ulaziti u većem detalju na ovom kursu. Međutim, vratićemo se ovoj temi detaljno u budućim obukama MIN 201.



Za sada, možete sumirati kako mining funkcioniše ovako: rudari prave kandidatski blok sa transakcijama koje čekaju u mempool-ovima, zatim traže hash njegovog zaglavlja (putem `SHA256d`) koji je manji ili jednak cilju. Ovo postižu testiranjem nonce-ova metodom pokušaja i greške.



U sledećem poglavlju, napravićemo kratak istorijski izlet u princip proof-of-work kako bismo razumeli njegovu pozadinu, a zatim ćemo pogledati kako sistem određuje cilj težine.



## Istorija proof of work


<chapterId>919d9f3e-8b3b-41d9-b45a-54df4f3c31a3</chapterId>



Proof-of-work nije izmišljen za Bitcoin. [Satoshi Nakamoto](https://planb.academy/resources/glossary/nakamoto-satoshi) je preuzeo i sastavio nekoliko starijih ideja, koje su već istražene u različitim kontekstima.



### Hashcash



Krajem 1990-ih, problem neželjene e-pošte postao je značajan. Naime, ako slanje e-pošte košta gotovo ništa, spammer može poslati milione. Ali ako svaka poruka zahteva mali računski napor, slanje jedne legitimne poruke ostaje lako za normalnog korisnika, dok slanje miliona poruka postaje veoma skupo.



Ovo je cilj [Hashcash](https://planb.academy/resources/glossary/hashcash), koji je predložio Adam Back 1997. godine, a koji se smatra izumom proof-of-work principa. Princip Hashcash je veoma sličan mining: proizvesti hash koji poštuje određeni uslov (ima određeni broj nula na početku hasha). Dokaz zatim prati poruku i primalac ga može vrlo brzo verifikovati. Ako se primi e-mail koji ne sadrži ovaj dokaz, može se odmah smatrati spamom i stoga filtrirati. Spameri su tada primorani da troše znatnu količinu energije da bi poslali milione poruka, što drastično smanjuje (ili čak potpuno poništava) profitabilnost ove vrste operacije, bilo da je reč o marketingu ili prevari.



Danas se Hashcash ne koristi za e-mail. Filtriranje neželjene pošte sada se uglavnom zasniva na centralizovanim sistemima. Prednost Hashcash-a u odnosu na trenutna rešenja leži u činjenici da ne zahteva centralizovano filtriranje: svako može prilagoditi parametre prema sopstvenim kriterijumima. Takođe ne zahteva identifikaciju, jer se pretraga hešom može obaviti anonimno. Iznad svega, ne oslanja se na sistem reputacije, koji obično uvodi subjektivne oblike filtriranja.



Hashcash nije bio o stvaranju novca. Cilj mu je bio da nametne marginalni trošak na lako automatizovanu digitalnu akciju.



![Image](assets/fr/008.webp)



### Bit Gold



Krajem 1990-ih i početkom 2000-ih, Nick Szabo je istraživao ideju digitalne oskudice zasnovane na proof of work. Njegov konceptualni projekat, nazvan Bit Gold, predviđa stvaranje jedinica vrednosti rešavanjem skupog proof of work, a zatim beleženje ovih dokaza u registar kako bi se uspostavio oblik vlasništva.



Bit Gold nije rezultirao implementiranim sistemom kao Bitcoin, ali sadrži nekoliko važnih uvida: ideju da računanje može proizvesti oskudicu i ideju vremenskog označavanja elemenata tokom vremena kako bi se stvorila istorija koju je teško prepisati.



### RPOW



2004. godine, Hal Finney je predložio RPOW (*Reusable Proofs of Work*). Ideja je bila da se proizvedu dokazi o radu koji bi se zatim mogli razmenjivati, umesto da se jednostavno troše. RPOW je imao za cilj da stvori digitalne token zasnovane na proof of work, sa sistemom za verifikaciju i prenos ovih token bez njihovog dupliranja. RPOW, opet, nije zadovoljavajuće rešio problem potpuno decentralizovanog registra kao što će to kasnije učiniti Bitcoin, ali ostaje jedan od velikih prethodnika Bitcoin.



![Image](assets/fr/009.webp)



Hashcash, Bit Gold i RPOW koriste proof-of-work da nametnu trošak i stvore oblik oskudice. Bitcoin preuzima ovaj mehanizam, ali mu daje centralnu i kolektivnu ulogu: proof-of-work se ne koristi samo za stvaranje nečega, već i za odlučivanje ko ima pravo da napiše sledeću stranicu registra (sledeći blok), i da učini ovaj registar skupim za falsifikovanje.



## Podešavanje ciljne težine


<chapterId>528bcaa8-351e-4eae-887a-426a78a223e3</chapterId>



U prethodnim poglavljima, videli ste srce proof-of-work: rudari heširaju zaglavlje svog kandidatskog bloka sa `SHA256d`, i blok se smatra validnim samo ako je dobijeni heš numerički manji ili jednak referentnoj vrednosti koja se zove cilj. Pitanje koje ostaje je: odakle dolazi ovaj cilj i kako sistem osigurava da ostane konzistentan tokom vremena?



Bitcoin ima za cilj prosečnu stopu pronalaženja jednog bloka svakih 10 minuta. Očigledno, ova brzina nije zagarantovana u sekundu. U praksi, neki blokovi se pronađu nekoliko sekundi nakon prethodnog, dok se drugi pronađu nakon više od sat vremena. Ono što je važno ovde je prosek tokom dovoljno dugog perioda.



![Image](assets/fr/019.webp)



Ova varijabilnost proizlazi iz probabilističke prirode mining: svaki hash je nezavisni pokušaj, sa konstantnom verovatnoćom (pod pretpostavkom da cilj ostaje nepromenjen) da se proizvede rezultat ispod cilja. Stoga se može uporediti sa lutrijom sa kontinuiranim izvlačenjem: što više hashova rudari naprave po sekundi, to je kraće očekivano kašnjenje pre pojave važećeg bloka, ali bez ikakvog eliminisanja nasumičnosti od jednog izvlačenja do sledećeg.



### Zašto ciljati na 10 minuta između blokova?



Iako ne postoje dokazi za to, Satoshi Nakamoto je sigurno izabrao 10 minuta kao praktičan kompromis između efikasnosti i sigurnosti. Kraći interval bi omogućio češće potvrde, ali bi izazvao više privremenih podela mreže. Da bismo razumeli ovu tačku, moramo se vratiti na način na koji se blok propagira.



Kada rudar pronađe važeći blok, odmah ga distribuira svojim vršnjacima. Čvorovi koji ga prime proveravaju njegovu validnost (transakcije, proof of work, pravila konsenzusa, itd.), a zatim ga prosleđuju dalje. Ova propagacija traje određeno vreme, ograničeno internet latencijom, širinom pojasa i sposobnošću svakog čvora da verifikuje blok.



![Image](assets/fr/020.webp)



Ako, tokom ovog kašnjenja u difuziji, drugi rudar takođe otkrije važeći blok na istoj visini, mreža može biti privremeno podeljena: jedan deo čvorova i rudara oslanja se na blok A, dok se drugi oslanja na blok B. Ovo je privremena podela mreže.



![Image](assets/fr/021.webp)



Ove podele nisu katastrofalne. Nakamoto konsenzus predviđa da će, na duži rok, samo jedna grana prevladati: ona koja akumulira najviše rada. Zaista, čim se novi blok iskopa na vrhu bloka A, na primer, cela mreža se resinhronizuje na ovoj grani i napušta blok B, koji tada postaje "*[zastareli blok](https://planb.academy/resources/glossary/stale-block)*", ponekad pogrešno nazvan "*napušteni blok*" u svakodnevnom jeziku.



![Image](assets/fr/022.webp)



S druge strane, oni imaju cenu: nekoliko minuta, deo rudara radi na grani koja će biti napuštena. Ovaj rad je tada izgubljen sa stanovišta ukupne sigurnosti, jer nije doprineo konačnom lancu. Što je brži interval između svakog bloka, veća je verovatnoća takvih podela, jer vreme propagacije predstavlja veći deo vremena između svakog bloka.



Interval od 10 minuta generalno omogućava dovoljno vremena da se pobednički blok široko propagira pre nego što se pronađe konkurentski blok na istoj visini. To je kompromis koji ograničava podele, smanjuje potrošnju računarske snage i pomaže mreži da ostane sinhronizovana na globalnom nivou.



### Razumevanje hashrate



*"[Hashrate](https://planb.academy/resources/glossary/hashrate)*" se odnosi na količinu hash proračuna proizvedenog po sekundi, bilo od strane jednog rudara, grupe rudara, ili svih rudara u Bitcoin. Izražava se u `H/s` (hashovi po sekundi), sa višekratnicima kao što su `TH/s` (terahashovi po sekundi) ili `EH/s` (eksahashovi po sekundi). Ovo predstavlja broj pokušaja koje rudari mogu napraviti svake sekunde da pokušaju dobiti hash niži od cilja.



Ako cilj ostane fiksiran, onda:




- svaki pokušaj ima fiksnu verovatnoću uspeha;
- pravljenje više pokušaja u sekundi povećava verovatnoću da će se dobitni pokušaj brzo pojaviti


Drugim rečima, ako sutrašnja Bitcoin mreža udvostruči svoju računarsku snagu povezivanjem dvostruko više mining mašina, bez korektivnog mehanizma, blokovi bi se pronalazili u proseku dvostruko brže. Cilj se stoga mora prilagoditi kako bi se kompenzovale varijacije hashrate.



### Podešavanje ciljne težine



Bitcoin rešava ovaj problem sa periodičnim mehanizmom za podešavanje cilja, koji podešava težinu mining. Princip je sledeći: svakih 2016 blokova (otprilike svake 2 nedelje), svaki čvor preračunava cilj težine posmatrajući koliko je vremena zapravo bilo potrebno za proizvodnju ovih 2016 blokova.



Cilj ovog mehanizma je da smanji prosečno vreme proizvodnje bloka na oko 10 minuta, dok se ukupni hashrate mreže konstantno menja, zbog isključivanja mašina ili, naprotiv, dodavanja novih mašina.



![Image](assets/fr/023.webp)



Izračun se zasniva na posmatranom vremenu za protekli period:




- ako su poslednja 2016 bloka pronađena prebrzo, to znači da je hashrate porastao tokom ovog perioda; Bitcoin zatim otežava uslov snižavanjem cilja za sledeći period;
- ako su blokovi iz 2016. pronađeni previše sporo, to znači da je hashrate opao; Bitcoin olakšava uslov povećanjem cilja.



Formula je sledeća:



```txt
Tn = To * (Ta / Tt)
```



Sa:




- `tn`: nova meta
- `to`: stara meta
- `Ta`: proteklo stvarno vreme za poslednjih 2016 blokova
- `Tt`: ciljno vreme (u sekundama)



Sa ciljnim vremenom od dve nedelje, tj. `Tt = 1,209,600` sekundi:



```txt
Tn = To * (Ta / 1 209 600)
```



Da biste razumeli kako prilagoditi težinu Bitcoin mining, evo primera sa izmišljenim vrednostima:



```txt
Tn = To * (Ta / 1 209 600)
Tn = 18 045 755 102 * (1 000 000 / 1 209 600)
Tn = 14 918 779 020
```


Sa:



- `**To = 18,045,755,102**`: Stara meta, tj. referentna vrednost pre prilagođavanja.
- `**ta = 1,000,000 sekundi**`: Vreme stvarno provedeno u proizvodnji poslednjih 2016 blokova. Pošto je ovo vreme manje od ciljanog vremena, mreža je kopala prebrzo.
- `**1.209.600 sekundi**`: Ciljno vreme koje odgovara 10 minuta po bloku za 2016 blokova, koristi se kao referenca za prilagođavanje.
- `**tn = 14,918,779,020**`: Novi cilj izračunat nakon [prilagođavanja težine](https://planb.academy/resources/glossary/difficulty-adjustment).



Ovde je novi cilj niži od starog, što znači da mining postaje teži kako bi usporio proizvodnju blokova u narednom periodu.


*Ciljne vrednosti u ovom primeru su pojednostavljene i skalirane za potrebe učenja; stvarna ciljna vrednost korišćena u Bitcoin je 256-bitni ceo broj potpuno drugačijeg reda veličine.*



Ovaj proračun se obavlja lokalno od strane svakog čvora, na osnovu vremenskih oznaka unetih u blokove. Kako svi čvorovi primenjuju ista pravila, dolaze do istog rezultata, i nova meta postaje zajednička referenca za narednih 2016 blokova.



Postoji važan detalj koji treba napomenuti u vezi sa ovom prilagodbom: **ona je ograničena**. Bitcoin ograničava varijaciju u težini po periodu kako bi se izbegle previše nagle promene koje bi je mogle blokirati. U stvari, stvarno vreme koje se uzima u obzir je ograničeno da ostane unutar opsega ekvivalentnog faktoru 4 (minimum jedna četvrtina stare mete, maksimum četiri puta stara meta). Ovo sprečava ekstremno ponovno ciljanje ako su vremenske oznake veoma atipične ili manipulirane.



Napomenimo takođe da u stvarnosti prilagođavanje težine Bitcoina nije savršeno tačno. Zaista, videli smo da je predviđeno ponovno izračunavanje težine na svakih 2016 blokova, poređenjem stvarnog proteklog vremena sa ciljanim vremenom od 14 dana (2016 × 10 minuta). Međutim, Satošijev originalni kod sadrži grešku zvanu "*off-by-one*": umesto da meri vreme između poslednjih blokova svakog perioda (odnosno 2016 intervala), on meri vreme između prvog i poslednjog bloka, što je samo 2015 intervala. Konkretno, težina se izračunava kao da period sadrži samo 2015 blokova umesto 2016. Posledica je da je težina sistematski vrlo blago precenjena, što dovodi do toga da se blokovi u proseku rudare malo sporije od ciljanih 10 minuta (oko 0,05% sporije). Ovaj bag je dobro poznat, ali nikada nije ispravljen, jer bi njegova izmena zahtevala hard fork, a njegov uticaj u praksi ostaje zanemarljiv, osim kod teoretskog napada zvanog "*time warp*".

### Ciljana reprezentacija



U zaglavlju bloka, cilj se ne pojavljuje u svom punom 256-bitnom obliku, jer bi to zauzelo previše prostora. Umesto toga, 32-bitno polje `nBits` kodira cilj u kompaktnom formatu, uporedivom sa naučnom notacijom baze 256: eksponent (1 bajt) i koeficijent (3 bajta). Kompletan cilj se zatim rekonstruiše iz ove dve vrednosti. Nećemo ulaziti u detalje ovde, jer je tema relativno složena i ne doprinosi razumevanju mining. Samo zapamtite da cilj nije sačuvan u sirovom obliku u zaglavlju bloka, već u kompaktnom obliku.



Sa ovim poslednjim poglavljem Prvog dela, obišli smo kako proof-of-work funkcioniše u Bitcoin: rudar gradi kandidatski blok birajući transakcije iz svog mempool-a, izračunava zaglavlje kandidatskog bloka, hešira ga, upoređuje dobijeni heš sa ciljem perioda, zatim počinje ponovo modifikujući nonce dok se ne dobije važeći heš. Na kraju, svakih 2016 blokova, mreža ponovo izračunava novi cilj kako bi održala prosečno vreme od oko 10 minuta po bloku, uprkos konstantnim varijacijama u hashrate.




# Bitcoin mining sistem podsticaja


<partId>27fb10c1-d53b-4dc2-90fa-3cb0309b74c1</partId>



## Block reward


<chapterId>b316fb89-9c18-417e-917b-ab98f1722646</chapterId>



Kao što možete zamisliti, Bitcoin mining nije altruistička aktivnost. Miner-i imaju stvarne troškove: električnu energiju za rad njihovih mining računara, kupovinu specijalizovane opreme, plate za održavanje, ponekad prostorije i sisteme za hlađenje. Da bi Bitcoin sistem funkcionisao, privatni interesi rudara moraju biti usklađeni sa kolektivnim interesima mreže. Upravo je to uloga mining nagrade. Ona podstiče rudare da investiraju u proof of work, da uključuju validne transakcije i da poštuju pravila protokola umesto da pokušavaju da ga korumpiraju.



Ova logika se zasniva na teoriji igara: protokol čini poštenje racionalnim. Rudar zarađuje novac kada proizvede važeći blok koji prihvataju čvorovi. Suprotno tome, ako pokuša da vara, njegov blok će biti odbijen od strane čvorova i neće dobiti ništa. Pošto proizvodnja bloka ima trošak, odbijeni blok predstavlja direktan gubitak. U konkurentnom okruženju gde hiljade igrača istovremeno traže važeći blok, najprofitabilnija strategija, većinu vremena, je stoga striktno poštovati pravila i maksimalno povećati svoj prihod pošteno.



Da bi se to postiglo, protokol Bitcoin propisuje da rudar koji pronađe važeći blok osvaja pravo da u njega uključi određenu transakciju, što rudaru dodeljuje određeni iznos BTC. Ovo je poznato kao **[nagrada za blok](https://planb.academy/resources/glossary/block-reward)**. U ovom prvom poglavlju ovog odeljka, cilj je razumeti od čega se sastoji i kako se određuje. Kasnije ćemo videti kako se deo kreiranja novca razvija tokom vremena (sa prepolovljenjima) i kako se tehnički zapravo prikuplja (putem coinbase transakcije).



### Od čega se sastoji nagrada za blok?



U prethodnim poglavljima, videli smo kako rudari uspevaju da pronađu važeći blok. Kada rudar pronađe zaglavlje čiji je heš manji od cilja, njegov kandidat blok se smatra važećim. On tada može da ga distribuira celokupnoj Bitcoin mreži. Blok se dodaje ostatku blokčejna, potvrđujući transakcije koje sadrži.



Upravo ovaj događaj (stvarno dodavanje bloka u blockchain) pokreće davanje nagrade pobedničkom rudaru. Ova nagrada se sastoji od dva različita elementa koja se sabiraju:




- [subvencija bloka](https://planb.academy/resources/glossary/block-subsidy)**;
- naknade za transakcije**.



![Image](assets/fr/024.webp)



Hajde da pogledamo na šta se odnose ova dva dela nagrade.



### Subvencija bloka



Subvencija bloka odgovara delu nagrade koji se odnosi na kreiranje novca. Kada rudar proizvede važeći blok, protokol mu odobrava da kreira određeni broj novih bitkoina i da ih dodeli sebi kao nagradu. Ovi bitkoini su kreirani ex nihilo. Nisu postojali ranije.



Međutim, količina novostvorenih bitkoina ni u kom slučaju nije proizvoljna. Strogo je definisana pravilima Bitcoin protokola i identična je za sve rudare. Detaljnije ćemo razmotriti ovaj mehanizam u narednom poglavlju, jer subvencija nije fiksna vrednost beskonačno: periodično se deli prema preciznom rasporedu. Za sada, samo zapamtite da:




- blok subvencija je jedna od dve komponente nagrade za blok;
- ograničeno je i određeno protokolom, a ne rudarom (iako rudar tehnički može zahtevati manje od maksimalnog iznosa);
- stvara bitkoine ni iz čega.



Ova subvencija ima dve glavne uloge unutar Bitcoin protokola. Prva je da podstakne igrače da učestvuju u mining. U ranim godinama Bitcoin (a ponekad i danas), transakcione naknade su bile veoma niske. Subvencija je stoga garantovala dovoljnu kompenzaciju da privuče rudare i održi nivo sigurnosti sistema.



Druga uloga se odnosi na distribuciju valute. Svaka nova valuta suočava se s pitanjem kako pravedno distribuirati monetarne jedinice populaciji. Blok subvencija pruža odgovor na ovaj problem. Kreiranjem bitkoina putem mining, omogućava njihovu početnu distribuciju na otvoren i neutralan način: svako ih može dobiti, pod uslovom da učestvuje u mining, bez potrebe za prethodnom autorizacijom ili identifikacijom.



S druge strane, pošto su ovi bitkoini stvoreni ni iz čega, njihova vrednost nije bez osnova. Povećanjem količine novca u opticaju, subvencija mehanički razređuje vrednost postojećih bitkoina. Stoga uvodi oblik monetarne inflacije. Međutim, videćemo u narednom poglavlju da je ova subvencija predodređena da postepeno nestane i da će inflacija na kraju prestati.



![Image](assets/fr/025.webp)



### Naknade za transakcije



Druga komponenta nagrade za blok je povezana sa korišćenjem sistema: kada korisnik pošalje transakciju, želi da ona bude potvrđena. Međutim, prostor u bloku je ograničen, a blokovi se u proseku pojavljuju tek na svakih 10 minuta. Prostor u bloku je stoga oskudan resurs. Kada potražnja premaši ponudu, cena raste: ovo je tržište naknada za transakcije. Svaki rudar koji uspe da proizvede važeći blok dobija pravo da prikupi, za svoj račun, sve naknade za transakcije povezane sa svim transakcijama koje je uključio u svoj blok.



Možete to zamisliti kao aukcijski sistem: svaka transakcija predlaže iznos naknade, a rudari daju prioritet onima koje maksimiziraju njihov prihod, u okviru prostornih ograničenja. Ovaj mehanizam prirodno usklađuje interese:




- korisnici u žurbi plaćaju više da bi bili brzo uključeni;
- rudari su podstaknuti da uključe transakcije koje plaćaju najviše naknade za prostor u bloku.
- mreža izbegava spam, jer objavljivanje transakcije ima cenu.



#### Kako se obračunavaju naknade za transakcije?



Suprotno uvreženom mišljenju, naknade nisu izlaz u Bitcoin transakciji. Zapravo, transakcija troši ulaze i stvara izlaze. Ulazi predstavljaju izvor korišćenih bitkoina, dok izlazi predstavljaju odredište uplata. Transakcione naknade su jednostavno **razlika između ukupnih ulaza i ukupnih izlaza**.



Drugim rečima, korisnikovi bitcoin inputi, koji pripadaju njima, stvaraju outpute za primaoce, ali ne reprodukuju pun iznos koji su inputi potrošili. Razlika između ta dva predstavlja transakcione naknade koje rudar može prikupiti.



Hajde da uzmemo primer. Transakcija troši dva ulaza, jedan od `100,000 sats` i drugi od `150,000 sats`, i stvara tri izlaza od `35,000 sats`, `42,000 sats` i `170,000 sats`.



![Image](assets/fr/027.webp)



Zbir ulaza je stoga `250,000 sats`, dok je zbir izlaza `247,000 sats`. To znači da je `3,000 sats` potrošeno u ulazima bez da su ponovo stvoreni u izlazima: ovaj iznos odgovara naknadama predloženim ovom transakcijom.



![Image](assets/fr/028.webp)



Ako rudar uključi ovu transakciju u važeći blok, imaće pravo da povrati ovih `3,000 sats`, pored naknada svih drugih transakcija uključenih u blok. Međutim, ne postoji direktna on-chain veza između transakcije koja plaća naknadu i sats koje rudar zapravo prikupi. Tehnički, `3,000 sats` u naknadama se uništava, a zauzvrat, rudar dobija pravo da ponovo kreira isti iznos za sebe.



#### Odnos naknade



Blok nije ograničen brojem transakcija, već njegovim ukupnim kapacitetom (danas, u praksi, težinom bloka). Neke transakcije zauzimaju više prostora od drugih: transakcija sa mnogo ulaza i izlaza biće veća od jednostavne transakcije sa jednim ulazom i dva izlaza. Skripte koje se koriste takođe će uticati na veličinu.



![Image](assets/fr/026.webp)



Dve transakcije mogu stoga platiti isti iznos naknada u apsolutnim terminima, ali ne biti ekonomski ekvivalentne sa stanovišta rudara. Ako je jedna dvostruko veća, košta dvostruko više prostora u bloku. Prostor je oskudan, pa rudar nastoji maksimizirati svoj prihod po jedinici prostora.



Zato u praksi izražavamo konkurentnost transakcije odnosom naknade, obično u `sats/vB` ([satoshis](https://planb.academy/resources/glossary/satoshi-sat) po virtualnom bajtu). Izračunavanje ovog odnosa je jednostavno:



```text
fee rate = fee / weight (in vB)
```



Na primer, ako imamo transakciju težine `141 vB` i dodeljuje `1,974 sats` u naknadama, imaće stopu naknade od `14 sats/vB`.



```text
1 974 / 141 ≈ 14 sats/vB
```



Ovaj odnos objašnjava ekonomske izbore koje donose rudari: pri fiksnom kapacitetu, uključivanje transakcija sa visokim stopama maksimizira ukupne naknade bloka, a samim tim i kompenzaciju rudara. Takođe objašnjava zašto transakcije sa niskim troškovima ostaju u redovima čekanja u mempool-ovima duže vreme: one se takmiče sa drugim transakcijama koje plaćaju više po jedinici prostora.



### Zaštita mreže od neželjene pošte



Naknade takođe služe svrsi operativne bezbednosti: one uvode trošak za umnožavanje transakcija. Ako bi objavljivanje transakcije bilo besplatno, bilo bi lako preplaviti mrežu beskorisnim transakcijama i zasićiti mempool-ove, povećavajući opterećenje na čvorovima.



U praksi, čvorovi primenjuju lokalne politike prosleđivanja (pravila mempool-a) i često postavljaju minimalni prag naknade ispod kojeg neće prosleđivati transakciju (podrazumevano, `0.1 sat/vB` u Bitcoin Core putem `minRelayTxFee`). Transakcija može biti validna u strogom smislu pravila konsenzusa, ali neće biti prosleđena od strane većine čvorova ako su njene naknade preniske. Kao rezultat toga, ne cirkuliše, ne stiže do rudara i ima vrlo male šanse da bude potvrđena.



U ovom trenutku, shvatili ste suštinu nagrade za blok: ona odgovara kompenzaciji za pobedničkog rudara i sastoji se od dva različita elementa. S jedne strane, subvencija za blok, definisana pravilima protokola, koja stvara nove bitkoine ex nihilo. A s druge strane, naknade za transakcije uključene u iskopani blok.



U sledećem poglavlju, fokusiraćemo se detaljnije na blok subvenciju, kako bismo precizno razumeli kako se ona izračunava i kako se razvija tokom vremena prema pravilima Bitcoin protokola.



## Halving


<chapterId>7cdca211-7300-48f8-a1e4-53e5c2678cd8</chapterId>



U prethodnom poglavlju smo videli da rudari koji proizvedu važeći blok dobijaju nagradu koja se sastoji od naknada za transakcije uključene u blok, plus subvencija za blok. Međutim, još nismo objasnili kako se određuje iznos ove subvencije. Mehanizam koji postavlja i razvija ovu vrednost poznat je kao ***[prepolovljavanje](https://planb.academy/resources/glossary/halving)***.



### Šta je prepolovljavanje?



Halving je događaj programiran u Bitcoin protokol koji prepolovljava subvenciju bloka, tj. maksimalni iznos novih bitkoina koje pobednički rudar sme da kreira sa svakim blokom. Ne utiče na naknade za transakcije: naknade postoje nezavisno i ostaju određene aktivnošću korisnika i konkurencijom za prostor u bloku.



Kada je Bitcoin lansiran 2009. godine, subvencija po bloku je postavljena na 50 BTC za svaki iskopani blok. Od tada, ova subvencija je prepolovljena nekoliko puta za svako prepolovljavanje.



![Image](assets/fr/029.webp)



Halving nije pokrenut datumom, već visinom bloka. Izvršava se **svakih 210.000 blokova**. Pošto Bitcoin cilja prosečan interval od oko 10 minuta po bloku, 210.000 blokova odgovara otprilike četiri godine.



```cpp
CAmount GetBlockSubsidy(int nHeight, const Consensus::Params& consensusParams)
{
int halvings = nHeight / consensusParams.nSubsidyHalvingInterval;
// Force block reward to zero when right shift is undefined.
if (halvings >= 64)
return 0;

CAmount nSubsidy = 50 * COIN;
// Subsidy is cut in half every 210,000 blocks which will occur approximately every 4 years.
nSubsidy >>= halvings;
return nSubsidy;
}
```



Dakle, ako označimo `n` kao broj već izvršenih prepolovljenja, subvencija po bloku u BTC može se izračunati na sledeći način:



```text
subsidy(n) = 50 / 2^n
```



### Prethodna prepolovljavanja



Evo sažeta tabela prepolovljenja koja su se već dogodila, sa njihovom visinom bloka, datumom i novom subvencijom po bloku koja važi nakon događaja:



| Event               |   Height  | Date                        | Subsidy    |
| ------------------- | --------: | --------------------------- | ---------: |
| Halving 1           |   210 000 | 28 novembre 2012            |     25 BTC |
| Halving 2           |   420 000 | 9 july 2016                 |   12,5 BTC |
| Halving 3           |   630 000 | 11 may 2020                 |   6,25 BTC |
| Halving 4           |   840 000 | 20 april 2024               |  3,125 BTC |
| Halving 5 (upcoming) | 1 050 000 | Spring   2028 (estimation) | 1,5625 BTC |

### Kada i kako se subvencija završava?



Halving se ponavlja sve dok se subvencija može izraziti u minimalnoj jedinici sistema: satoshi.



```text
1 BTC = 100 000 000 sats
```



Kako se subvencija prepolovi, na kraju dolazimo do delova bitcoina koji su toliko mali da postaju manji od 1 satoshi. U tom trenutku više nije moguće stvoriti pola jedinice satoshi. Stvaranje novca putem blok subvencije prestaje, a rudari se nadoknađuju isključivo na osnovu naknada za transakcije. Od tog trenutka, svi bitcoini će biti u opticaju i više neće biti moguće proizvoditi nove jedinice.



Definitivni kraj subvencija za blokove će doći na nivou bloka 6,930,000, tj. na 33. i poslednjem prepolovljavanju. Ovaj događaj se očekuje oko godine 2140, iako je nemoguće dati tačan datum, jer će zavisiti od stvarne brzine kojom se blokovi pronalaze između sada i tada.



Pošto subvencija bloka prati geometrijski niz sa odnosom 1/2 pri svakom prepolovljavanju, kreiranje novca je bilo izuzetno visoko u ranim danima Bitcoin, a zatim se vrlo brzo smanjuje. Do 7. prepolovljavanja, preko 99% bitkoina će već biti pušteno u opticaj. Očekuje se da će prag od 99% biti pređen između 2032. i 2036. godine. To znači da će zatim biti potrebno preko 100 godina da se iskopa preostalih 1% bitkoina. Dok je monetarna inflacija bila veoma visoka kada je Bitcoin pokrenut, kako bi se omogućila široka distribucija valute, sada je veoma niska i nastaviće da opada, dok ne dostigne nivo prave čvrste valute, čija cirkulišuća ponuda više ne može da se poveća.



![Image](assets/fr/030.webp)



### Zašto nikada neće biti 21 milion BTCs?



Maksimalna monetarna ponuda Bitcoin često se predstavlja kao 21 milion BTC. Ovo je dobra aproksimacija za razumevanje njene monetarne politike, ali sa strogo tehničke tačke gledišta, ukupna ponuda nikada zapravo neće dostići tačno 21,000,000 bitkoina.



Glavni razlog je mehanički. Kroz sukcesivna prepolovljavanja, subvencija za blok na kraju pada ispod minimalne vrednosti od 1 sat, što završava izdavanje pre nego što se dostigne tačan teoretski ukupni iznos. Kao rezultat ove minimalne granularnosti i pravila zaokruživanja, ukupan broj bitkoina stvorenih subvencijom je nešto manji od 21 milion.



Pored toga, marginalna odstupanja povezana sa protokolom takođe mogu doprineti ovome. Na primer, u retkim slučajevima, neki rudari možda nisu preuzeli svoju punu subvenciju, što definitivno smanjuje količinu stvarno izdatih bitkoina. Takođe možemo pomenuti [genesis blok](https://planb.academy/resources/glossary/genesis-block), proizveden od strane Satoshi 3. januara 2009. godine, čiji kreirani bitkoini nisu deo [UTXO set](https://planb.academy/resources/glossary/utxo-set), kao i određene istorijske događaje povezane sa greškama, kao što su duplikati identifikatora coinbase transakcija.



Konačno, moramo uzeti u obzir i sve bitkoine koji su uništeni ili blokirani:




- bitcoini zaključani u nerešivim skriptama;
- one namerno uništene skriptama `OP_RETURN`;
- ili gubitak privatnih ključeva na nivou aplikacije.



U teoriji, snabdevanje Bitcoin je stoga ograničeno na 21 milion. U praksi, međutim, nikada neće biti stvarno 21 milion bitkoina u opticaju.



## Coinbase transakcija


<chapterId>69476700-3616-4aab-b006-367aba059de9</chapterId>



U prethodnim poglavljima, predstavili smo dve važne tačke. Prvo, rudar koji uspe u proizvodnji i distribuciji validnog bloka dobija nagradu. S druge strane, videli smo da se ova nagrada sastoji od dva različita elementa:




- subvencija bloka (bitkoini stvoreni ex nihilo, čiji je maksimalni iznos postavljen protokolom i postepeno se smanjuje putem prepolovljavanja);
- sve naknade za transakcije plaćene od strane korisnika čije su transakcije uključene u blok.



Međutim, ostaje jedno pitanje: kojim mehanizmom rudar prikuplja ovu nagradu u Bitcoin? Ovo je upravo uloga određene transakcije koja se zove "coinbase".



### Kako funkcioniše coinbase transakcija



Kao što smo videli u prvom delu kursa, svaki Bitcoin blok sadrži listu transakcija na čekanju koje će potvrditi. Prva od njih je uvek [coinbase transakcija](https://planb.academy/resources/glossary/coinbase-transaction). Ona omogućava pobedničkom rudaru da primi svoju nagradu.



![Image](assets/fr/031.webp)



Na prvi pogled, izgleda kao klasična Bitcoin transakcija: ima [TXID](https://planb.academy/resources/glossary/txid-transaction-identifier), izlaze i uključena je u Merkle stablo bloka. Međutim, razlikuje se u jednom važnom pogledu: ne troši nijedan postojeći UTXO.



U klasičnoj Bitcoin transakciji, `inputs` referenciraju prethodne neutrošene izlaze (UTXOs), koji obezbeđuju ulaznu vrednost. Izlazi zatim preraspodeljuju ovu vrednost na nove UTXOs, sa novim uslovima trošenja. Drugim rečima, da biste poslali bitkoine, morate ih već posedovati. S druge strane, coinbase transakcija ne troši bitkoine na ulazu: ona stvara bitkoine na izlazu direktno od nule.



Upravo ovaj mehanizam omogućava da se novi bitkoini uvedu u cirkulaciju putem blok subvencije i pripisuje rudaru naknade povezane sa transakcijama uključenim u blok. Transakcija coinbase ne može referencirati stvarni postojeći UTXO (u stvari, referencira fiktivni UTXO), jer je njena uloga upravo da stvori deo vrednosti (subvenciju) i povrati drugi deo (naknade), bez primanja iz prethodne transakcije. Da bi ceo sistem ostao konzistentan, deo koji odgovara naknadama mora tačno odgovarati sumi bitkoina potrošenih u ulazima, ali ne i ponovo stvorenih u izlazima u drugim transakcijama bloka.



![Image](assets/fr/032.webp)



Ova transakcija nije opcionalna. Blok koji ne sadrži coinbase transakciju je nevažeći i biće sistematski odbijen od strane mrežnih čvorova.



⚠️ Please note: the term "*coinbase*" has no connection with the exchange platform of the same name. In Bitcoin, "*coinbase*" historically refers to the transaction that creates the block reward. The company has simply adopted this term for its name.



Transakcija coinbase zapravo ispunjava nekoliko uloga istovremeno:




- Prvi je onaj koji smo upravo detaljno opisali: dodeljuje rudaru nagradu na koju ima pravo za proizvodnju važećeg bloka.
- Njegova druga, tehničkija uloga je da usidri kriptografski angažman prema svedocima (potpisima) transakcija SegWit uključenih u blok.
- Treća uloga, ovoga puta nije direktno povezana sa protokolom, već sa modernom industrijalizacijom mining, jeste da se coinbase sada često koristi za sidrenje proizvoljnih tehničkih podataka. Ovi podaci su generalno povezani sa radom mining bazena i njihovom unutrašnjom organizacijom.



Da bismo vam pomogli da razumete ove različite upotrebe, sada ćemo detaljnije pogledati strukturu coinbase transakcije.



### Osnovna struktura coinbase transakcije



Transakcija coinbase mora sadržati tačno jedan ulaz. Radi jednostavnosti, ponekad kažemo da nema ulaz, jer ovaj ulaz ne troši pravi UTXO. U stvarnosti, postoji ulaz sa referenciranim izvorom, ali namerno ukazuje na nepostojeći UTXO.



Kao što smo već videli, svaka Bitcoin transakcija mora koristiti UTXO kao ulaz kako bi kreirala validne izlaze. U Bitcoin transakciji, ovo korišćenje se odvija u obliku referenciranja postojećeg UTXO kao ulaza. Ovo referenciranje se jednostavno vrši navođenjem identifikatora prethodne transakcije (one u kojoj je UTXO kreiran), kao i njenog indeksa među izlazima te transakcije. Konkretno, UTXO je definisan hešom (prethodni TXID) i indeksom.



Ali u slučaju coinbase transakcije, umesto da se referiše na stvarni postojeći UTXO, ulaz mora nužno ukazivati na ovaj određeni lažni UTXO, sa TXID-om punim nula, koji ne odgovara nijednom stvarnom TXID-u:



```text
0000000000000000000000000000000000000000000000000000000000000000
```


Neposredno praćen lažnim indeksom:


```text
0xffffffff
```


![Image](assets/fr/033.webp)



U osnovnom Bitcoin protokolu, kako je opisano u Satoshi Nakamoto, ovaj lažni unos je jedino ograničenje nametnuto na coinbase transakciju.



Kao i svaki UTXO referenciran u ulazu transakcije, povezan je sa poljem `scriptSig`. U konvencionalnoj transakciji, ovo polje `scriptSig` sadrži elemente potrebne za ispunjavanje `scriptPubKey` i time otključavanje potrošenog UTXO. Ali u posebnom slučaju coinbase-a, pošto je referencirani UTXO namerno fiktivan, polje `scriptSig` je potpuno slobodno. Miners stoga mogu uneti bilo koje podatke koje žele. Kasnije ćemo pogledati kako se ova sloboda koristi.


Pored ovog lažnog unosa, postoji jedan ili više potpuno standardnih izlaza, koji omogućavaju rudaru da prikupi bitkoine iz nagrade na jednoj od njihovih Bitcoin adresa. Ovi izlazi su UTXO zaključani pomoću `scriptPubKey` (npr. skripta koja pokazuje na adresu koju kontroliše rudar ili bazen). Jedina posebnost ovde leži u pravilu za izračunavanje njihove vrednosti: ukupna suma izlaza coinbase-a nikada ne sme premašiti maksimalnu dozvoljenu subvenciju, kojoj se dodaju naknade za blok.



Istorijski gledano, coinbase transakcija se svodi na ovu jednostavnu šemu: lažni ulaz koji referencira nepostojeći UTXO, i jedan ili više izlaza dizajniranih da distribuiraju nagradu za blok pobedničkom rudaru. Danas, međutim, coinbase više nije ograničen na ovu ulogu distribucije. Njegova posebna pozicija u bloku i velika fleksibilnost njegove strukture doveli su do novih upotreba, kako u samom protokolu, tako i u mehanizmima upravljanja mining bazenom.



### Druge upotrebe coinbase-a



Tokom vremena, coinbase transakcija je postala posebno pogodno mesto za integraciju različitih informacija korisnih za mining i za samu strukturu bloka. Hajde da ih pogledamo kako bismo bolje razumeli celokupnu organizaciju coinbase-a.



#### The BIP-34



[BIP-34](https://planb.academy/resources/glossary/bip0034) je fork soft uveden u martu 2013, počevši sa blokom 227,930, koji je uveo verziju 2 Bitcoin blokova. Ova nova verzija zahteva da svaki blok uključi, u `scriptSig` coinbase transakcije, visinu bloka koji se kreira.



S jedne strane, ova evolucija pojašnjava način na koji mreža pristaje da razvija strukturu blokova i pravila konsenzusa. S druge strane, osigurava jedinstvenost svakog bloka i coinbase transakcije.



Dakle, `scriptSig` coinbase-a nije potpuno slobodan. Od aktivacije BIP-34, jednostavno je ograničen da počinje visinom bloka u kojem je ova coinbase transakcija uključena.



![Image](assets/fr/035.webp)



#### Dodatni-nonce



Kao što smo videli u prvim poglavljima ovog kursa, rudar ima 32-bitno polje nonce u zaglavlju bloka, koje modifikuje metodom pokušaja i greške kako bi pronašao hash manji ili jednak cilju. Ovaj 32-bitni prostor već omogućava istraživanje veoma velikog broja kombinacija, ali kada je težina mining visoka, ovaj opseg može biti potpuno iscrpljen u relativno kratkom vremenu i stoga možda neće dati nijednu kombinaciju koja proizvodi važeći hash. Ako su sve moguće vrednosti `nonce` testirane bez uspeha, rudar tada mora modifikovati drugi element kako bi promenio zaglavlje bloka i započeo novu seriju pokušaja.



Kako transakcija coinbase nudi slobodno polje putem `scriptSig` svog ulaza, rešenje koje se koristi za proširenje prostora nonce-a je iskorišćavanje dela ovog `scriptSig`. Ovo se obično naziva extra-nonce. Menjanjem extra-nonce, rudar menja coinbase-ov `scriptSig`, tj. identifikator transakcije, zatim Merkle koren bloka, i na kraju sam header bloka. Na ovaj način, oni dobijaju novi prostor pretrage heševa za istraživanje, bez potrebe da menjaju druge komponente svog kandidata bloka.



![Image](assets/fr/036.webp)



#### Identifikacija bazena i rudara



Danas je veoma veliki deo svetskog hashrate organizovan u mining bazene. Ove strukture okupljaju pojedinačne rudare kako bi udružili svoj rad i smanjili varijabilnost svojih prihoda.



Iz operativnih razloga, mining bazeni takođe koriste slobodno polje `scriptSig` ulaza coinbase-a za umetanje različitih informacija. Ove informacije variraju od bazena do bazena i od mrežnog protokola do mrežnog protokola, ali generalno uključuju jedinstveni identifikator (često dodatni nonce strukturiran u nekoliko poddelova) dodeljen svakom rudaru, kako bi se izbeglo dupliranje posla unutar bazena. Obično se dodaje oznaka za identifikaciju bazena, koja se koristi za javno pripisivanje pronađenih blokova, mining statistike i druge svrhe praćenja.



![Image](assets/fr/037.webp)



#### Posvećenost SegWit



Od kada je SegWit soft fork omogućen 2017. godine, podaci svedoka (tj. generalno potpisi) su odvojeni od glavnih podataka transakcije, posebno da bi se ispravio problem [promenljivosti Bitcoin transakcija](https://planb.academy/resources/glossary/malleability-transaction). Ovo razdvajanje stoga uvodi novi element koji treba uključiti u blok.



Da bi se to uradilo, svedoci su grupisani zajedno u drugo posvećeno Merkle stablo, čiji se koren zatim povezuje sa coinbase transakcijom putem `OP_RETURN` izlaza.



![Image](assets/fr/038.webp)



Neću ulaziti u više detalja o ovom mehanizmu u ovom kursu, jer je izvan okvira ovog članka, ali samo zapamtite da od uvođenja SegWit, coinbase transakcija služi kao sredstvo za sidrenje u bloku otiska prsta koji sumira sve SegWit svedoke. Svedoci su smešteni u nezavisno Merkle stablo, koren ovog stabla je upisan u izlaz coinbase transakcije, a sama coinbase transakcija je uključena u glavno Merkle stablo zajedno sa svim ostalim transakcijama, čiji se koren pojavljuje u zaglavlju bloka. Ovako su svedoci, koji su odvojeno skladišteni od glavnih podataka transakcije, i dalje povezani sa zaglavljem bloka.



![Image](assets/fr/039.webp)



#### Arbitrarne poruke



Pošto `scriptSig` omogućava slobodno umetanje proizvoljnih informacija koje bira rudar, neki su iskoristili priliku da dodaju poruke ličnije prirode, umesto tehničkih. Najpoznatiji slučaj je naravno Satoshi Nakamoto, sa njegovom sada već ikoničnom porukom:



> The Times 03/Jan/2009 Kancelar na ivici drugog paketa pomoći za banke

Ova poruka, prisutna u Genesis bloku (prvom bloku Bitcoin), zapravo je kodirana u heksadecimalnom formatu u `scriptSig` coinbase transakcije:



```text
5468652054696d65732030332f4a616e2f32303039204368616e63656c6c6f72206f6e206272696e6b206f66207365636f6e64206261696c6f757420666f722062616e6b73
```


![Image](assets/fr/034.webp)



### Period dospeća


Jednom kada je blok iskopan i distribuiran, coinbase transakcija se pojavljuje na blockchain-u kao i svaka druga transakcija. Ona kreira UTXOs za pobedničkog rudara, omogućavajući mu da prikupi svoju nagradu. Međutim, ovi UTXOs nisu odmah raspoloživi za trošenje: podložni su [periodu sazrevanja](https://planb.academy/resources/glossary/maturity-period). Ovo sazrevanje je postavljeno na 100 blokova nakon bloka koji sadrži coinbase. Konkretno, coinbase transakcija mora imati ukupno 101 potvrdu da bi njeni izlazi postali raspoloživi za trošenje od strane pobedničkog rudara.


![Image](assets/fr/040.webp)


Cilj ovog pravila je da ograniči uticaj reorganizacija lanca na ekonomiju. Kao što smo videli u prethodnim poglavljima, može se desiti da se na istoj visini, dva različita validna bloka pronađu gotovo istovremeno od strane različitih rudara. Na kratko, mreža se može podeliti: neki čvorovi prvo prime blok A, dok drugi prvo vide blok B. Zatim, tokom narednih blokova, jedna od dve grane akumulira više rada i postaje referentna grana. Druga grana se napušta i njeni blokovi postaju zastareli. Transakcije koje je sadržala mogu se tada, teoretski, vratiti u mempoolove čekajući potvrdu.



U praksi se ovo retko dešava, jer tržište naknada često rezultira time da se gotovo iste transakcije pojavljuju u dva konkurentska bloka na istoj visini. Ovo je jedan od razloga zašto se transakcija Bitcoin obično smatra nepromenljivom nakon šest potvrda: reorganizacije od više od šest blokova su toliko malo verovatne da se razumno mogu smatrati nemogućim.



![Image](assets/fr/041.webp)



Problem sa ovim reorganizacijama u slučaju coinbase transakcije je što to nije obična transakcija. Ona uvodi potpuno nove bitkoine u opticaj. Ako bi se nagrada za blok mogla odmah potrošiti, mogla bi nastati problematična kaskadna situacija:




- rudar troši bitkoine iz coinbase-a,
- ovi bitkoini cirkulišu u ekonomiji,
- tada je originalni blok konačno napušten tokom reorganizacije.



Bitkoini u opticaju tada nikada ne bi postojali u konačnom lancu, a niz transakcija koje su bile važeće u trenutku izdavanja postale bi nevažeće a posteriori.



Period dospeća nameće vremenski okvir dovoljno dug da ovaj scenario učini nerealnim. Reorganizacija od 101 bloka se smatra, u praksi, nemogućom (čak i ako ostaje beskonačno mala verovatnoća). Ne znamo tačno zašto je Satoshi izabrao tako visoku vrednost za dospeće, ali je verovatno da je izabrana kako bi mehanizam ostao funkcionalan, čak i u slučaju velikih kvarova mreže.



Ovo pravilo sprečava da novostvoreni novac iz nagrade za blok počne da cirkuliše pre nego što blok koji generated bude sigurno zakopan pod velikom količinom akumuliranog rada.



---

Sada smo došli do kraja našeg objašnjenja kako Bitcoin mining funkcioniše. Trebalo bi da sada imate jasnu sliku osnovnih mehanizama koji su uključeni.



U poslednjem delu kursa, vratićemo se konkretnijim aspektima, kako bismo vam pokazali kako se Bitcoin mining materijalizuje u stvarnom svetu: njegova industrijalizacija, korišćene mašine, grupisanje igrača, i tako dalje. Cilj će biti da vam pružimo celokupan pregled Bitcoin mining, kako sa teorijske i protokolarne perspektive koju smo upravo videli, tako i sa praktične i operativne strane.



# Industrija Bitcoin mining


<partId>906a6e18-4718-4a1f-85f5-18854cebdf7c</partId>



## Evolucija mining mašina


<chapterId>2d2f9055-75fd-4630-b493-a577d708a39f</chapterId>



U ranim danima Bitcoin, mining nije bila industrijska aktivnost. Bila je deo Bitcoin softvera, pokrenutog na ličnom računaru, često iz radoznalosti, ponekad da bi se podržala mreža, a sekundarno da bi se dobili bitkoini koji tada praktično nisu imali tržišnu vrednost.



Tokom godina, ova aktivnost je doživela transformaciju: mašine su se promenile, težina je eksplodirala, a mining je postao industrija za sebe. Hajde da pogledamo operativne aspekte Bitcoin mining.



### Početak: mining sa CPU-om



Godine 2009. i u ranim godinama, mining se uglavnom izvodio koristeći CPU konvencionalnog računara. Bitcoin je tada bio samo jednostavan softver, koji je služio kao wallet, čvor i rudar. Jednostavno pokretanje Satoshi Nakamoto softvera na ličnom računaru bilo je dovoljno da se učestvuje u mining procesu i, u mnogim slučajevima, da se pronađu blokovi.



CPU može da uradi sve, ali nije optimizovan ni za šta. Izvršava veoma opšte instrukcije, sa složenom logikom. Za zadatak kao što je ponavljajuće heširanje zaglavlja blokova, nije idealan alat, ali na početku mreže, težina je toliko niska da je više nego dovoljan za pronalaženje blokova.



Ovaj period je važan, jer nas podseća na važnu tačku: proof of work ne zavisi od određene kategorije opreme. Ono što je važno je sposobnost računanja heševa brže od drugih, po datoj ceni. Čim se pojavi tehnička prednost, ona se automatski pretvara u ekonomsku prednost. Ali u apsolutnim terminima, i dalje je moguće danas pokušati pronaći Bitcoin blokove koristeći konvencionalni CPU. Ovo je pristup koji je usvojio projekat NerdMiner, na primer. Šanse za pronalaženje bloka su praktično nikakve, ali i dalje postoji infinitesimalna verovatnoća.



https://planb.academy/tutorials/mining/hardware/nerdminer-c9826fd9-c2b4-4d1e-8c78-809122de1654

### Prelazak na GPU-ove



Ubrzo su rudari shvatili da usko grlo nije bila snaga, već sposobnost da se izvrši ogroman broj sličnih operacija paralelno. Upravo to su grafičke procesorske jedinice (GPU) mogle da urade. Prvobitno, GPU je bio dizajniran da izvršava iste operacije na velikim količinama podataka. Ova arhitektura je bila savršeno prilagođena za zadatak poput ponovljenog heširanja: umesto da imate nekoliko visoko svestranih jezgara, imate stotine, pa čak i hiljade jedinica sposobnih da istovremeno izvršavaju iste instrukcije.



Uz uporedivu potrošnju energije, GPU može proizvesti mnogo više heševa po sekundi nego CPU. U isto vreme, bitcoin je imao kurs u odnosu na dolar, njegova vrednost je rasla, a platforme za razmenu su se pojavljivale. Od tada, priroda mining počela je da se menja. Više se nije radilo samo o učestvovanju, već o zarađivanju novca. Pojavile su se posvećene konfiguracije: mašine izgrađene oko nekoliko grafičkih kartica, ponekad bez ekrana, sa minimalnim sistemom i specijalizovanim softverom, čija je jedina svrha bila rudarenje.



U ovom trenutku je težina mining počela da eksplodira. Između sredine 2010. i sredine 2011. godine, čak se povećala za faktor 1.000. Mehanički, počinje specijalizacija, baš kao rani oblici industrijalizacije, i obični korisnici—koji su zadovoljni da pokreću Bitcoin softver na svojim ličnim računarima—sada imaju samo vrlo malu šansu da pronađu važeći blok.



![Image](assets/fr/044.webp)



*Izvor: [CoinWarz.com](https://www.coinwarz.com/mining/bitcoin/hashrate-chart)*



Između ere GPU-a i moderne ere [ASIC](https://planb.academy/resources/glossary/asic), postojala je međufaza: korišćenje FPGA-a. FPGA je reprogramabilna komponenta: može se konfigurisati da direktno implementira logičko kolo posvećeno određenom proračunu, u ovom slučaju `SHA256d`. Ideja je bila da se još više udalji od hardvera opšte namene (CPU/GPU) kako bi se postigla energetska efikasnost. Ali ubrzo, poboljšanja napravljena virtuelno na FPGA-ima bila bi primenjena fizički na same čipove: to je dolazak ASIC.



### Dolazak ASIC



Završna faza u specijalizaciji mining hardvera bila je pojava ASICs (*Application-Specific Integrated Circuits*). ASIC je čip dizajniran za jedan zadatak. U slučaju Bitcoin mining, ovaj zadatak je precizno izvršavanje `SHA256d` pri maksimalnoj brzini i sa optimalnom energetskom efikasnošću. Za razliku od GPU-a, ASIC se ne koristi za pokretanje igara, 3D renderovanje ili AI. Namenjen je za heširanje, i to je sve.



![Image](assets/fr/045.webp)



*ASIC S21 XP proizveden od strane Bitmain*



Ova specijalizacija ima dve glavne posledice:




- Prvi je skok u performansama i efikasnosti. Za uređaje uporedive generacije, ASIC proizvodi daleko više heševa po sekundi nego GPU, dok troši manje energije. Mining sa GPU-om brzo je postao nekonkurentan: iako je tehnički radio, trošak električne energije daleko je nadmašio očekivani prihod u većini konteksta;
- Druga promena je promena modela: investicije su se uglavnom preusmerile na industrijski hardver. Mining sada podrazumeva kupovinu mašina dizajniranih za ovu svrhu, njihovo kontinuirano napajanje, hlađenje, održavanje i apsorbovanje njihove zastarelosti. Jer ASIC nije ekonomski večan: kada nova, efikasnija generacija izađe na tržište, stare mašine postaju progresivno manje profitabilne, čak i ako ostanu funkcionalne.



Od tog trenutka nadalje, više ne govorimo samo o hobiju. Govorimo o sektoru gde konkurentnost zavisi od jednačine:




- trošak električne energije;
- troškovi opreme i amortizacija;
- sposobnost hlađenja i rada u velikim razmerama;
- dostupnost i pouzdanost mašine;
- brzina komunikacija;
- itd.



### Mining farme



Izolovana mašina može da rudari, ali grupisanjem stotina, pa čak i hiljada ASIC na jednoj lokaciji, delimo fiksne troškove, optimizujemo logistiku i približavamo se modelu specijalizovanog data centra.



[Farma mining](https://planb.academy/resources/glossary/mining-farm), u svom najjednostavnijem obliku, je zgrada (ili skup kontejnera) ispunjena ASIC-ovima koji rade 24/7. Izazov sada je održavanje stabilnih uslova rada:




- snabdevanje velikim količinama jeftine, stabilne električne energije;
- upravljajte toplotom kako biste izbegli smanjenje performansi, jer je gustina energije značajna;
- filtriraj prašinu, kontroliši vlažnost, očisti;
- praćenje performansi mašina u realnom vremenu (temperature, hardverske greške, hashrate padovi, itd.).



![Image](assets/fr/043.webp)



*Jedna od sedam zgrada posvećenih Bitcoin mining na lokaciji Riot Platforms u Rockdaleu, blizu Austina, Teksas. Ova je posebno posvećena uranjanju mining*



Mining sada pokreću industrijski igrači, neki od njih su na berzi, koji grade i upravljaju farmama veoma velikih razmera. To uključuje MARA Holdings (Nasdaq: `MARA`) i Riot Platforms (Nasdaq: `RIOT`).



![Image](assets/fr/042.webp)



Čak i bez ulaska u detalje modela profitabilnosti, važno je razumeti zašto je mining poprimio ovaj oblik. Proof-of-work je konkurentski mehanizam: verovatnoća pronalaženja bloka, i samim tim ostvarivanja zarade, proporcionalna je udelu hashrate koji raspoređujete. Kao rezultat toga, postoji konstantan pritisak da se poveća računarska snaga, smanji cena po jedinici računanja i ograniče gubici. Kao rezultat toga, okruženja koja nude jeftiniju struju, klimu pogodnu za hlađenje ili obilnu energetsku infrastrukturu, prirodno postaju privlačnija.



Mining Bitcoin je tako evoluirao iz aktivnosti dostupne svima u svojim ranim danima, do one kojom dominira specijalizovana oprema i profesionalne operacije. Ovo ne menja pravila protokola. U teoriji, svako može da rudari sa bilo kojim uređajem. Ali u praksi, nivo težine i efikasnosti ASIC učinio je domaći mining uglavnom nekonkurentnim u većini konteksta.



Naravno, još uvek postoje situacije u kojima kućni mining može biti zanimljiv, na primer ako imate koristi od veoma jeftine struje, ili ako koristite toplotu generated od vašeg majnera za grejanje doma zimi. Ali u svakom slučaju, i dalje ćete morati da kupite mašinu opremljenu sa ASIC čipom. Štaviše, pošto će vaša mining snaga ostati izuzetno mala u odnosu na Bitcoin mrežu, moraćete da pronađete način da smanjite varijansu vašeg prihoda: upravo je to uloga mining bazena, o čemu ćemo diskutovati u sledećem poglavlju.



Ako želite da istražite kućna mining rešenja sa povratom toplote, imamo tutorijale o raznim alatima, kako gotovim tako i "uradi sam":



https://planb.academy/tutorials/mining/hardware/canaan-avalon-mini-f2185435-10a3-4d7b-b88f-f1a489babab7

https://planb.academy/tutorials/mining/hardware/canaan-avalon-nano-3f6ac96e-ea8a-4dee-9b9b-13875824c9a6

https://planb.academy/tutorials/mining/hardware/attakai-0d177e6b-e167-4b25-8e38-4ec74213d1fb

## Grupisanje u mining grupe


<chapterId>c871bece-eebe-4ef4-9789-d47251f16c8b</chapterId>



Mining Bitcoin uključuje stalne i neizbežne troškove, među kojima je najvažnija potrošnja energije mašina. Ovi troškovi nastaju nezavisno od bilo kakvih rezultata, iako su prihodi od mining, po svojoj prirodi, retki i nasumični. Otkrivanje bloka zavisi isključivo od udelа rudara u hashrate, što čini zaradu nepredvidljivijom što je taj udeo manji. Upravo ovaj praktični problem je brzo doveo do široke upotrebe [mining bazena](https://planb.academy/resources/glossary/pool-mining). U ovom poslednjem poglavlju kursa MIN 101, nudim uvod u principe i rad mining bazena u Bitcoin.



### Šta je mining bazen?



mining bazen je organizacija (često online usluga) koja agregira računarsku snagu mnogih nezavisnih rudara, kako bi povećala učestalost kojom njihova grupa pronalazi blokove. Kada bazen pronađe blok, nagrada za blok se zatim redistribuira među učesnicima prema internim pravilima bazena (koja će biti pokrivena u kursu MIN 201, jer su previše složena za MIN 101).



Učesnici u mining bazenu se često nazivaju "[hashers](https://planb.academy/resources/glossary/hasher)", umesto "miners", jer više ne obavljaju sav mining posao, već samo heširaju podatke koje im prenosi bazen.



Pazite da ne pomešate bazen mining sa farmom mining. Ovo su dva različita pojma. Kao što smo videli u prethodnom poglavlju, farma je fizička lokacija gde jedan entitet upravlja brojnim mining mašinama. Bazen, s druge strane, je pre svega virtuelna grupa: hiljade mašina, često geografski rasprostranjenih, rade pod zajedničkom koordinacijom. Međutim, farma može, i često učestvuje, u bazenu.



![Image](assets/fr/048.webp)



### Smanjenje varijance prihoda



Pa zašto se pridružiti bazenu? Jednostavno zato što je rezultat aktivnosti mining probabilistički: sa svakim pokušajem heširanja, postoji vrlo mala šansa da će ispuniti cilj težine i stoga proizvesti važeći blok.



Tokom veoma dugog perioda, vaša prosečna zarada treba da bude proporcionalna vašem udelu u ukupnom hashrate. Ovaj princip direktno proizlazi iz zakona verovatnoće: svaka hash kalkulacija predstavlja nezavisno slučajno izvlačenje, i, prema zakonu velikih brojeva, učestalost sa kojom otkrivate blokove matematički se približava vašem delu ukupnog hashrate mreže. Međutim, na kratki do srednji rok, vaša stvarna zarada može biti izuzetno neredovna. Upravo ovu razliku između teoretskog proseka i slučajne stvarnosti nazivamo **varijansa** u matematici.



Evo jednostavan primer da ilustruje princip:




- Bitcoin mreža proizvodi u proseku 144 bloka dnevno (otprilike jedan blok svakih 10 minuta);
- Ako imate `0.0001 %` od ukupnog hashrate, vaša očekivanja su `144 × 0.000001`, ili `0.000144` blokova/dan;
- Drugim rečima, trebalo bi da pronađete blok u proseku svakih `1 / 0.000144` dana, tj. svakih 6,944 dana, ili otprilike svakih 19 godina.



Ali ova vrednost odgovara samo matematičkom očekivanju: distribucija vremena otkrivanja prati slučajni zakon, tako da je u praksi sasvim moguće nikada ne otkriti ni jedan blok, čak i tokom veoma dugog perioda. Možete biti nesrećni i ne pronaći ništa veoma dugo, dok plaćate stalne troškove (struja, održavanje, amortizacija opreme...).



mining bazen menja prirodu ovog problema: kombinovanjem hashrate, bazen češće pronalazi blokove. Svaki učesnik se zatim slaže da primi samo deo svakog pronađenog bloka, ali mnogo češće. To je transformacija iz visoko nestabilnog, široko raspoređenog prihoda u redovniji, po cenu deljenja nagrada i plaćanja naknada za usluge.



### Zašto varijansa opada kada se grupišete zajedno?



Što je veća vaša računska snaga, to je veća očekivana učestalost pronađenih blokova. Još važnije, što su događaji češći, to su posmatrani rezultati bliži statističkom proseku tokom datog perioda.



Na solo osnovi, mali rudar može godinama raditi bez ijednog bloka, a onda jednog dana dobiti veliku isplatu, pa opet ništa. U bazenu, ista probabilistička stvarnost i dalje važi, ali je izravnana na kolektivnom nivou: bazen češće pronalazi blokove, a redistribucija pretvara te događaje u redovnije isplate za svakog učesnika. **Bazen mining stoga prodaje predvidljivost na aktivnosti mining**.



### Istorijske znamenitosti



Kao što smo videli u prethodnom poglavlju, na samom početku, mining je mogao biti urađen solo sa konvencionalnim računarom, jer je težina bila vrlo niska. Ali kako je globalni hashrate eksplodirao (GPU, zatim ASIC), solo mining je postao vrlo vremenski zahtevan rizik za većinu učesnika.



Prvi bazeni su stvoreni upravo kao odgovor na ovu novu stvarnost. Braiins Pool (ranije Slush Pool / Bitcoin.cz) je prvi Bitcoin mining bazen: iskopao je svoj prvi blok 16. decembra 2010. Uspeh ovog prvog mining bazena bio je brz, jer je za samo nekoliko dana osvojio skoro 3,5% globalnog hashrate.



![Image](assets/fr/047.webp)



Sa tehničke strane, bazeni su tada bili strukturirani oko specijalizovanih komunikacionih protokola između bazena i rudara (npr. [Stratum](https://planb.academy/resources/glossary/stratum), zatim Stratum V2), kako bi se efikasno organizovao distribuirani rad. Detaljnije ćemo razmotriti ove koncepte u našem kursu obuke MIN 201.



### Moderna situacija



U vreme pisanja (početkom 2026), globalni Bitcoin hashrate je na nivou reda veličine zeta-heš po sekundi (= 1,000 EH/s = 1,000,000,000,000,000,000 heševa po sekundi), i skoro svi pronađeni blokovi dolaze iz mining bazena.



Evo rangiranje, do danas, glavnih mining bazena i njihovog odgovarajućeg udela u hashrate. Ovo rangiranje će se verovatno promeniti do trenutka kada budete čitali ovaj kurs. Za najnovije podatke, molimo posetite [mempool.space](https://mempool.space/graphs/mining/pools).



![Image](assets/fr/046.webp)



| Ranking    | Pool           | Blocks found  | Hashrate share   |
| ---------: | -------------- | ------------: | ---------------: |
|          1 | Foundry USA    |          1297 |           29.57% |
|          2 | AntPool        |           755 |           17.21% |
|          3 | ViaBTC         |           514 |           11.72% |
|          4 | F2Pool         |           467 |           10.65% |
|          5 | SpiderPool     |           349 |            7.96% |
|          6 | MARA Pool      |           229 |            5.22% |
|          7 | SECPOOL        |           197 |            4.49% |
|          8 | Luxor          |           128 |            2.92% |
|          9 | Binance Pool   |           105 |            2.39% |
|         10 | OCEAN          |            78 |            1.78% |
|         11 | SBI Crypto     |            70 |            1.60% |
|         12 | Braiins Pool   |            54 |            1.23% |
|         13 | WhitePool      |            33 |            0.75% |
|         14 | Mining Squared |            26 |            0.59% |
|         15 | BTC.com        |            16 |            0.36% |
|         16 | Poolin         |            14 |            0.32% |
|         17 | ULTIMUSPOOL    |            14 |            0.32% |
|         18 | GDPool         |            12 |            0.27% |
|         19 | Innopolis Tech |            11 |            0.25% |
|         20 | NiceHash       |             8 |            0.18% |
|         21 | RedRock Pool   |             8 |            0.18% |
|         22 | Unknown        |             2 |            0.05% |
|         23 | Public Pool    |             1 |            0.02% |

*Izvor [mempool.space](https://mempool.space/graphs/mining/pools), podaci za jedan mesec, 16. decembar 2025. do 16. januar 2025.*



U naprednijem kursu, detaljnije ćemo istražiti unutrašnje funkcionisanje bazena (deonice, mrežni protokoli, metode plaćanja...), jer se ovde nalaze detalji koji određuju i profitabilnost rudara i potencijalne implikacije za Bitcoin.



---

Sada smo došli do kraja MIN 101. Hvala vam što ste pratili do kraja. Ako želite da procenite veštine koje ste stekli tokom kursa, završni ispit vas čeka u sledećem odeljku.



Sa osnovnim znanjem koje ste upravo stekli, sada možete pohađati naprednije kurseve na mining na Plan ₿ Academy, bilo u teoriji, kao što je ovaj, ili praktičnije kurseve, kako biste i vi mogli početi učestvovati u Bitcoin mining!



# Finalni deo


<partId>eced8ca1-971d-4a22-9254-dbf8bce15d1b</partId>



## Recenzije i Ocene


<chapterId>dc005a96-f4b4-42be-ab72-d4624c110716</chapterId>


<isCourseReview>true</isCourseReview>

## Završni ispit


<chapterId>959f06cf-fd66-4f29-b7ee-665bfedfea0d</chapterId>


<isCourseExam>true</isCourseExam>

## Zaključak


<chapterId>f16a4e42-c16e-466b-ad16-f42b5360f510</chapterId>


<isCourseConclusion>true</isCourseConclusion>