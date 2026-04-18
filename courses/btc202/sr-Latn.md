---
name: Postavljanje vašeg prvog Bitcoin čvora
goal: Razumevanje, instalacija, konfiguracija i korišćenje Bitcoin čvora
objectives: 


  - Razumevanje uloge i svrhe Bitcoin čvora.
  - Identifikovanje različitih dostupnih hardverskih i softverskih rešenja.
  - Instaliranje i konfiguracija full node-a (Bitcoin Core-a).
  - Korišćenje Umbrel grafičkog interfejsa i dodavanje korisnih aplikacija.
  - Povezivanje ličnog novčanika na full node.
  - Istraživanje naprednih podešavanja i najboljih bezbednosnih praksi.


---
# Postanite suvereni bitkoiner



Verovatno ste upoznati sa izrekom "Nisu tvoji ključevi, nisu tvoji novčići", koja podstiče samostalno čuvanje vaših bitkoina. Držanje sopstvenih ključeva je zaista osnovni prvi korak, ali nije dovoljno. Da biste postigli pravu monetarnu suverenost, takođe treba da instalirate i koristite sopstveni Bitcoin čvor. Ovaj kurs je dizajniran da vas vodi kroz ovaj osnovni korak na vašem Bitcoin putovanju!



BTC 202 je pristupačna obuka osmišljena da vas nauči kako da pokrenete sopstveni Bitcoin čvor, čak i ako niste tehnički stručnjak. Počećemo definisanjem šta je Bitcoin čvor, čemu služi i zašto je apsolutno neophodno da ga sami pokrenete. Zatim ću vas korak po korak voditi kroz izbor hardvera, instalaciju potrebnog softvera, povezivanje vašeg softverskog novčanika i prve moguće optimizacije za dalji napredak.



Pokretanje Bitcoin čvora nije samo opcija za stručnjake; to je nužnost. To je alat za otpornost koji svaki korisnik treba da razume i primeni. Ovaj kurs je vaša početna tačka ka tome da postanete suvereni bitkoiner!




+++




# Uvod


<partId>fc46ccd7-5d6d-40c3-9e9f-fbbb323c760a</partId>




## Pregled kursa


<chapterId>916b1f86-38a4-4ede-bdb7-83841d5a7abe</chapterId>



Dobrodošli u BTC 202, gde ćete naučiti kako da instalirate, konfigurišete i koristite Bitcoin čvor lako i samostalno. Ali to nije sve: takođe ćete saznati više o mestu i funkciji čvorova u Bitcoin sistemu. Kurs kombinuje teoriju sa vođenom praktičnom vežbom.



### Deo 1 - Uvod



U ovom prvom delu kursa, razjasnićemo osnovne pojmove, a zatim preći na preciznije definicije. Šta je čvor? Koje su razlike između čvora (eng. node), novčanika (eng. wallet) i rudara (eng. miner)? Zatim ćete naučiti o Bitcoin Core-u i implementacijama protokola. Cilj je govoriti istim jezikom, izbeći zabunu i uspostaviti čvrstu teorijsku osnovu.



### Deo 2 - Postati suvereni bitkoiner



U ovom drugom delu, počeću objašnjavajući zašto je važno pokrenuti sopstveni Bitcoin čvor. Zatim ćemo istražiti različite tipove čvorova koji postoje (kompletni, pruned - (čvor sa skraćenom istorijom blokova), SPV...), kako funkcionišu i njihove tehničke implikacije.



Zatim ćemo vam pružiti pregled softvera dostupnog za pokretanje Bitcoin čvora, uključujući njegove prednosti i nedostatke. Na kraju, zaključićemo sa nekoliko veoma praktičnih preporuka za odabir pravog hardvera prema vašim potrebama i budžetu.



Ovaj odeljak, dakle, ilustruje put suverenog bitkoinera: razumevanje zašto je neophodno pokrenuti čvor, izbor tipa čvora, i na osnovu ovog izbora odabir softvera, i u zavisnosti od izabranog softvera, izbor odgovarajućeg hardvera.



### Deo 3 - Jednostavna instalacija Bitcoin čvora



Kada je ova priprema završena, vreme je za praktičan deo u 3. poglavlju posvećenom Umbrel-u: kućnom cloud operativnom sistemu koji pojednostavljuje samostalno hostovanje i instalaciju Bitcoin i Lightning čvora.



Nakon kratkog uvoda u Umbrel, pružićemo detaljan vodič koji će vas voditi kroz proces instalacije i konfiguracije na vašoj sopstvenoj DIY mašini. Cilj ovog dela je jasan: imati vaš prvi potpuno funkcionalan i sinhronizovan Bitcoin čvor.



### Deo 4 - Povezivanje vašeg novčanika sa vašim čvorom



Sada kada ste postavili Bitcoin čvor, vreme je da ga koristite! U ovom odeljku ćete naučiti kako da povežete svoj softver za upravljanje novčanikom (kao što je Sparrow novčanik) sa vašim sopstvenim indeksatorom adresa (Electrs ili Fulcrum), ili direktno sa Bitcoin core-om, tako da više ne zavisite od javnih servera.



Takođe ćemo ispitati ulogu indeksatora i različite metode povezivanja sa vašim čvorom (LAN, Tor, Tailscale, itd.). Na kraju, u poslednjem poglavlju, pregledaćemo najkorisnije aplikacije dostupne na Umbrel-u koje svakodnevni korisnici Bitcoina mogu koristiti.



### Deo 5 - Napredni koncepti i najbolje prakse



U ovom završnom delu BTC 202, cilj je produbiti vaše znanje. Prvo ćemo pogledati najbolje prakse koje treba usvojiti sa vašim novim Bitcoin čvorom i kako ga održavati na duži rok.



Zatim ćemo odvojiti vreme da pregledamo neke od teorija obrađenih ranije u kursu, uključujući razumevanje IBD procesa i peer discovery (pronalaženje drugih čvorova) detaljnije, istraživanje anatomije čvora, i na kraju učenje kako koristiti `Bitcoin.conf` fajl za fino podešavanje postavki.



### Deo 6 - Završni deo



Kao i kod svih Plan ₿ Academy kurseva, u poslednjem delu ćete pronaći završni ispit za testiranje vašeg znanja o Bitcoin čvorovima.



Dakle, jeste li spremni da uključite svoj prvi Bitcoin čvor? Kreni putem suvereniteta!



## Šta je Bitcoin čvor?


<chapterId>0a9fd4e0-94ab-405e-924c-023397393027</chapterId>



Kako je opisao njegov tvorac, Satoshi Nakamoto, Bitcoin se predstavlja kao peer-to-peer elektronski novčani sistem. Ova jednostavna rečenica, koja je ujedno i naslov White Paper-a, sadrži mnoge naznake o prirodi Bitcoina:




- Prvo, Satoshi opisuje Bitcoin kao "sistem", drugim rečima, koherentan skup hardverskih i softverskih komponenti koje međusobno deluju kako bi pružile određenu uslugu ili izvršile određenu funkciju;
- Dalje, on objašnjava da ovaj sistem omogućava korišćenje elektronskog novca, tj. oblika nematerijalne valute;
- Na kraju, on ističe da ovaj sistem nije zavisan od bilo kojeg centralnog entiteta: on je "peer-to-peer", što znači da su sami korisnici ti koji upravljaju sistemom.



Pošto je Bitcoin sistem, mora se nužno pokretati na računarima i zbog svoje peer-to-peer prirode, sami korisnici preuzimaju odgovornost za pokretanje ovih mašina. Ono što nazivamo "Bitcoin čvor" je upravo taj računar na kojem se pokreće softver koji implementira Bitcoin protokol (kao Bitcoin core, ali o tome ćemo kasnije). Ovo je ono što omogućava Bitcoinu da funkcioniše bez centralnog autoriteta: validacija se sprovodi na distribuiran način, od strane hiljada nezavisnih mašina koje pripadaju hiljadama korisnika.



![Image](assets/fr/047.webp)



Nakamoto, S. (2008). *Bitcoin: A Peer-to-Peer Electronic Cash System*. https://Bitcoin.org/Bitcoin.pdf



Upravo ti korisnici osiguravaju bezbednost Bitcoina. Kako Eric Voskuil objašnjava u svojoj knjizi *Cryptoeconomics*, bezbednost Bitcoina ne zavisi ni od blockchaina, ni od [snage heširanja](https://planb.academy/resources/glossary/hashrate), ni od validacije, decentralizacije, kriptografije, otvorenog koda, niti teorije igara. Bezbednost Bitcoina zavisi prvenstveno od pojedinaca koji su spremni da se izlože ličnom riziku. Decentralizacija omogućava da se ovaj rizik raspodeli na veliki broj pojedinaca, a upravo njihova sposobnost da pruže otpor obezbeđuje otpornost sistema.


Ovaj princip je lako razumeti: kada bi Bitcoin zavisio od jednog jedinog čvora u vlasništvu jedne osobe, bilo bi dovoljno tu osobu zatvoriti da bi se mreža ugasila, jer bi ona sama snosila sav rizik. Sa desetinama hiljada čvorova rasprostranjenih širom sveta, rizik je raspršen: svaki od ovih operatera bi morao biti neutralisan da bi se ugasio Bitcoin.



![Image](assets/fr/048.webp)



Možemo tako razlikovati i imenovati nekoliko pojmova kako bismo razjasnili stvari za ostatak ovog kursa:




- Bitcoin valuta: jedinica obračuna koja se koristi za transakcije unutar ovog sistema;
- Bitcoin mreža: skup svih povezanih čvorova;
- Bitcoin čvorovi: mašine koje pokreću Bitcoin implementaciju;
- Bitcoin implementacije: softver koji prevodi protokol u izvršne instrukcije;
- Bitcoin protokol: skup pravila koja upravljaju radom sistema;
- Bitcoin sistem: koherentna kombinacija svih ovih elemenata.



### Uloga Bitcoin čvora



Bitcoin čvorovi zajedno formiraju ono što je poznato kao Bitcoin mreža. Oni omogućavaju celom sistemu da radi autonomno, bez oslanjanja na centralni autoritet ili hijerarhiju servera.



Od samog početka, Bitcoin je dizajniran da omogući svakom korisniku da pokrene lični čvor. Ovaj slučaj ostaje važeći i sa današnjim Bitcoin core softverom, koji kombinuje uloge novčanika i čvora. Ali danas se ova funkcija često razdvaja: mnogi moderni Bitcoin novčanici su samo novčanici koji se povezuju na eksterne čvorove (u vlasništvu iste osobe ili ne).



### Održavanje kopije blockchaina



Prvi zadatak čvora je da održava lokalnu kopiju blockchaina. Da bi se sprečila dvostruka potrošnja na Bitcoinu bez uključivanja centralnog autoriteta, svaki korisnik mora proveriti da ne postoji transakcija u sistemu. Jedini način da se u to bude siguran je da se poznaju sve transakcije napravljene na Bitcoinu. Iz tog razloga, sve transakcije su vremenski označene i grupisane u blokove, a svaki čvor skladišti ceo blockchain.



> Jedini način da potvrdite odsustvo transakcije je da budete svesni svih transakcija.

Nakamoto, S. (2008). *Bitcoin: A Peer-to-Peer Electronic Cash System*. https://Bitcoin.org/Bitcoin.pdf



Blockchain je stoga evoluirajući registar: svaki put kada rudar objavi novi blok, čvor proverava njegovu validnost pre nego što doda blok svojoj lokalnoj kopiji lanca. Zaključno sa današnjim danom (jul 2025), kompletan blockchain premašuje 675 GB, a ova veličina nastavlja da raste, jer se u proseku novi blok dodaje svakih 10 minuta.



![Image](assets/fr/049.webp)



Čvor takođe održava lokalni zapis svih UTXO-a koji postoje u bilo kom trenutku, poznat kao **UTXO skup**. Ova baza podataka sadrži sve nepotrošene Bitcoin fragmente. Ovu temu ćemo detaljno razmotriti u završnom delu kursa.



### Verifikacija i distribucija transakcija



Druga uloga čvora je da osigura verifikaciju i propagaciju transakcija. Kada nova transakcija stigne do čvora (bilo putem softver za upravljanje novčanikom ili drugog čvora), proveriće da li je u skladu sa skupom pravila (pravila konsenzusa (eng. consensus rules) i pravila prenosa (eng. relay rules)). Na primer:




- potrošeni bitkoini moraju postojati u svom UTXO skupu (bazi podataka nepotrošenih izlaza);
- potpis mora biti važeći, i svi uslovi potrošnje moraju biti ispunjeni (važeća skripta);
- ukupna vrednost izlaza ne sme premašiti ukupnu vrednost ulaza, što znači da troškovi naknada ne mogu biti negativni.



![Image](assets/fr/050.webp)



Nakon validacije, transakcija se čuva u [mempool-u](https://planb.academy/resources/glossary/mempool) čvora, privremenom memorijskom prostoru rezervisanom za nepotvrđene transakcije, a zatim se prenosi drugim mrežnim čvorovima na koje je povezan. Ovaj mehanizam distribucije i validacije nastavlja se od čvora do čvora. Na ovaj način, transakcija se propagira kroz Bitcoin mrežu, i svaki čvor je čuva u mempool-u dok nije uključena u važeći blok od strane rudara, nakon čega ona stupa na snagu sa prvim potvrđivanjem.



### Provera i distribucija blokova



Treća uloga čvora uključuje upravljanje "izrudarenim" blokovima. Kada rudar otkrije novi blok sa važećim [Proof of Work-om](https://planb.academy/resources/glossary/proof-of-work), on se emituje na mreži. Čvorovi ga primaju, proveravaju da li je u skladu sa svim pravilima protokola, i zatim ga, ako je važeći, integrišu u svoju lokalnu kopiju blockchaina. Kao i kod transakcija, novo potvrđeni blokovi se zatim prenose svim čvorovima povezanim na čvor. Ovaj proces se nastavlja dok svi čvorovi na Bitcoin mreži ne budu obavešteni o novom bloku.



![Image](assets/fr/051.webp)



## Koja je razlika između čvora i novčanika?


<chapterId>de5af634-a628-4b90-b869-468c208e178b</chapterId>



Važno je razlikovati dve različite vrste softvera kada koristite Bitcoin: čvor i novčanik.



Bitcoin čvor, kao što je gore pomenuto, je deo softvera koji aktivno učestvuje u [peer-to-peer](https://planb.academy/resources/glossary/peertopeer-p2p) mreži. Obavlja tri glavna zadatka:




- pravljenje rezervne kopije (eng. backup) blockchaina,
- validaranje i prosleđivanje transakcija,
- validaranje i prosleđivanje blokova.



S druge strane, Bitcoin novčanik je softverski alat dizajniran za čuvanje i upravljanje vašim privatnim ključevima. Ovi ključevi omogućavaju vam da trošite svoje bitkoine ispunjavanjem skripti za zaključavanje (obično putem potpisa). Novčanik može da se poveže sa čvorom (bilo lokalnim ili udaljenim) kako bi proverio status blockchaina i emitovao transakcije koje kreira, ali kao takav nije učesnik u mreži.



U nekim slučajevima, ove dve funkcije koegzistiraju unutar istog softvera, kao što je slučaj sa Bitcoin Core-om, koji služi i kao potpuni (eng. full) node i kao novčanik. Međutim, mnogi popularni programi za upravljanjem novčanikom (Sparrow, BlueWallet, itd.) zahtevaju vezu sa eksternim čvorom (bilo vašim ili treće strane) za emitovanje transakcija i određivanje raspoloživih sredstava novčanika.



![Image](assets/fr/052.webp)



## Koja je razlika između čvora i rudara?


<chapterId>d2992614-7ab7-4bf9-81b1-f548cda67257</chapterId>



Pojmovi čvora i rudara se često mešaju. Ipak, ova dva elementa obavljaju radikalno različite funkcije unutar sistema.



U početku, kada je Bitcoin lansiran od strane Satoshi Nakamoto 2009. godine, očekivalo se da svaki korisnik učestvuje u mreži kao celini. Tako je originalni Bitcoin softver kombinovao nekoliko funkcija odjednom: delovao je kao novčanik, čvor, i takođe kao rudar, sposoban za generisanje novih blokova. U to vreme, [težina rudarenja](https://planb.academy/resources/glossary/difficulty) (eng. mining difficulty) je bila veoma niska. Sve što je trebalo da uradite bilo je da pokrenete Bitcoin softver na svom računaru kako biste pronašli blokove i dobili bitkoine kao nagradu.



Međutim, kako je Bitcoin postajao sve popularniji i broj rudara se povećavao, konkurencija među rudarima doživela je radikalnu promenu. Danas je rudarenje postala izuzetno konkurentna aktivnost, kojom dominiraju industrijski igrači opremljeni specijalizovanom infrastrukturom. Snaga potrebna za rudarenje novog bloka sada je toliko velika da je praktično nemoguće da pojedinačni korisnik to postigne koristeći samo konvencionalni računar. Kao rezultat toga, rudarenje se sada prvenstveno obavlja korišćenjem specijalizovanih mašina nazvanih ASICs (*Application-Specific Integrated Circuits*). Ovi čipovi su optimizovani isključivo za izvršavanje dvostrukog heširanja koristeći SHA-256, algoritma koji se koristi za Bitcoin rudarenje.



![Image](assets/fr/053.webp)



Suočeni sa ovom evolucijom, uloge Bitcoin čvora i rudara postale su jasno odvojene. Kao što je prikazano gore, uloga Bitcoin čvora je isključivo informativna i zasnovana na validaciji. Uloga rudara je drugačija:




- Odabira transakcija koje su na čekanju u mempool-u.
- Pravi blok-kandidata koji uključuje ove transakcije.
- Traži metodom pokušaja i greške validan Proof of Work.
- Ako pronađe važeći dokaz, emituje blok putem svog čvora ka ostalim čvorovima.



Rudaru treba Bitcoin čvor za interakciju sa mrežom.



Uloga rudara se ponekad takođe razlikuje od uloge sekača blokova (na francuskom hacheur). Sekač blokova je mašina čiji je zadatak da hešira (u bukvalnom prevodu seče) predložene blokove koje obezbeđuje server [rudarskog bazena](https://planb.academy/resources/glossary/pool-mining) (eng. mining pool), tražeći heševe koji zadovoljavaju [cilj težine](https://planb.academy/resources/glossary/difficulty-target) definisan za [šerove](https://planb.academy/resources/glossary/shares) (eng. shares), a ne za Bitcoin. Ostatak rudarskog procesa, koji uključuje stvarnu izgradnju blokova, izbor transakcija ili Proof-of-Work pretragu prema stvarnoj težini rudarenja Bitcoina, kao i distribuciju, direktno obavljaju bazeni.



![Image](assets/fr/054.webp)



Konačno, postoji važna razlika u smislu ekonomskog podsticaja između rudara i čvora. Pokretanje Bitcoin čvora ne donosi direktnu novčanu korist. S druge strane, učešće u rudarenju donosi nagrade (subvencije i naknade za transakcije) za svaki pronađeni blok.



U Delu 2, istražićemo detaljnije praktične i lične prednosti instaliranja i korišćenja Bitcoin čvora, izvan isključivo finansijskih.



## Bitcoin Core i implementacije protokola


<chapterId>72381876-9317-4faa-8d41-2b252a945b8a</chapterId>



Bitcoin protokol nije softver: to je skup nepisanih pravila koja dele korisnici mreže. On definiše uslove za validnost transakcija, mehanizme kreiranja novca, format bloka, Proof-of-Work uslove i mnoge druge specifikacije. Da bi mogli da koriste ovaj protokol, korisnici moraju pokretati softver koji sprovodi ova pravila: to je poznato kao **implementacija** Bitcoina.



Implementacija je stoga softver čvora: program sposoban za interakciju sa drugim mašinama na Bitcoin mreži, preuzimanje, verifikaciju, skladištenje i propagaciju blokova i transakcija, i lokalno sprovođenje konsenzusnih pravila i pravila prosleđivanja. Svaka implementacija je konkretna interpretacija protokola, napisana u određenom programskom jeziku, sa svojom arhitekturom, performansama i ergonomijom. Svaka implementacija će takođe imati svoju razvojnu organizaciju, sa sopstvenom podelom odgovornosti.



Među ovim implementacijama, jedna daleko dominira: **Bitcoin Core**.



![Image](assets/fr/055.webp)



### Istorijska implementacija koja je postala merilo



Bitcoin Core je referentni softver za Bitcoin protokol. Izveden je iz originalnog koda koji je napisao Satoshi Nakamoto 2008-2009. godine i predstavlja direktan nastavak tog koda. U početku poznat kao "*Bitcoin*", zatim "*Bitcoin QT*" (zbog dodavanja grafičkog interfejsa putem Qt biblioteke), preimenovan je u "*Bitcoin Core*" 2014. godine kako bi se jasno razlikovao softver od mreže. Od verzije 0.5, distribuira se sa dve komponente: `Bitcoin-qt` (grafički interfejs) i `bitcoind` (komandno-linijski interfejs).



U teoriji, Bitcoin Core ne predstavlja Bitcoin protokol; već je samo jedna implementacija među mnogima. Međutim, odlikuje se masovnim usvajanjem, svojom starošću, robusnošću svog koda i rigoroznošću svog razvojnog procesa. Shodno tome, u praksi, pravila koja primenjuje Bitcoin Core su de facto pravila Bitcoin protokola: korisnici, programeri, rudari i različiti servisi unutar ekosistema se gotovo isključivo na njega pozivaju.



### Trenutna raspodela implementacija



Prema [podacima prikupljenim u avgustu 2025. od strane Luke Dashjr](https://luke.dashjr.org/programs/Bitcoin/files/charts/software.html) (poznatog programera u ekosistemu), distribucija implementacija među javnim čvorovima mreže je sledeća:




- **Bitcoin Core**: 87.3% čvorova
- **Bitcoin Knots**: 12.5
- **Ostale kumulativne implementacije**: 0.2% (btcsuite, Bcoin, BTCD...)



![Image](assets/fr/056.webp)



Drugim rečima, oko 9 od 10 javnih čvorova koristi Bitcoin Core. Ostatak mreže se oslanja na marginalnije klijente (iako je udeo Knots-a naglo porastao u poslednjim mesecima, posebno nakon debata o ograničenju veličine `OP_RETURN`). Ove alternativne implementacije često održava jedna osoba ili mali tim.



**Napomena:** Ove brojke su i dalje procene, jer se zasnivaju prvenstveno na *čvorovima koja slušaju*, tj. čvorovima koja prihvataju dolazne veze (sa otvorenim portom 8333). *Čvorovi koja ne slušaju* su mnogo složeniji za brojanje, jer je nemoguće direktno se povezati sa njima: morate čekati da inicijativa dođe od njih, u obliku odlazne veze. Sajt Luke Dashjr tvrdi da pokušava da broji i ove *čvorove koja ne slušaju*, ali ostaje nemoguće dobiti potpuno tačne podatke o njima, a ažuriranje ovih statistika neizbežno zaostaje za stvarnošću.



### Unutrašnje funkcionisanje Bitcoin Core-a



Bitcoin Core je softver napisan u C++. To je takođe open-source projekat koji održava zajednica programera — volontera ili onih koje finansiraju različiti subjekti (često kompanije iz ekosistema koje imaju interes da se razvoj Core-a odvija povoljno). [Kôd je hostovan na GitHubu](https://github.com/bitcoin/bitcoin), a razvoj prati rigorozan model:




- **Doprinosioci** podnose predloge u obliku _pull request_ (PR). U principu, svako može da predloži izmenu, ali ona mora biti testirana, dokumentovana i proći kroz proces recenzije (eng. review) od strane kolega.
- **Održavaoci** imaju pravo da odobravaju i spajaju PR-ove. Oni su ti koji garantuju koherentnost i stabilnost projekta. U julu 2025. godine, ima ih ukupno pet i oni su: Hennadii Stepanov, Michael Ford, Andrew Chow, Gloria Zhao i Ryan Ofsky.
- Nije bilo **glavnog održavaoca** od februara 2023. Ovu ulogu je u početku imao Satoshi Nakamoto prilikom lansiranja Bitcoina, zatim Gavin Andresen nakon Nakamotovog odlaska početkom 2011, i na kraju Wladimir J. Van Der Laan od 2014. do 2023.



![Image](assets/fr/057.webp)



Razvoj Bitcoin Core-a prati meritokratsku logiku: novi saradnici se podstiču da pregledaju i testiraju kôd pre nego što sami predlože bilo kakve izmene. Odluke se donose na osnovu tehničkog konsenzusa, a veće izmene (posebno u oblastima konsenzusa) zahtevaju prethodne rasprave na javnim kanalima, kao što su mejling liste ili PR review klubovi.



### Druge implementacije Bitcoina



Iako marginalni u smislu usvajanja, postoje i drugi klijenti. Glavni je Bitcoin Knots, koji je razvio Luke Dashjr, koji je [fork](https://planb.academy/en/resources/glossary/fork-git) od Bitcoin Core-a koji uključuje dodatne opcije i konzervativniji pristup razvoju. Ovo uključuje strožija ograničenja na formate transakcija.



![Image](assets/fr/058.webp)



Možemo takođe pomenuti:




- **Libbitcoin**: modularna C++ biblioteka koju je razvio Amir Taaki i održava Eric Voskuil;
- **Bcoin**: JavaScript implementacija, više se ne održava;
- **BTCD/btcsuite** : implementacija u Go-u.



Ovi projekti doprinose raznolikosti ekosistema, ali se koriste u vrlo maloj meri, zbog čega Bitcoin Core u praksi ima dominantnu ulogu, što otežava da se razvija nezavisno od ostatka mreže.



### Moć Core programera



Možda mislite da Bitcoin Core developeri imaju direktnu kontrolu nad Bitcoinom, ali to nije slučaj. Oni ne mogu nametnuti promenu u protokolu. Njihova uloga je da predlože kôd. Na svakom korisniku je, putem njihovog čvora, da odluči da li će koristiti taj kôd ili ne.



To znači da ako promena u Bitcoin Core-u ne postigne konsenzus, čvorovi je mogu ignorisati, bilo tako što neće ažurirati Bitcoin Core ili jednostavno promenom implementacije. Suprotno tome, ako je funkcija koju korisnici žele blokirana u procesu razvoja Core-a, uvek je moguće preći na drugu implementaciju ili forkovati projekat.



Kao što ćemo kasnije diskutovati u ovom kursu, čvorovi, prema njihovoj ekonomskoj težini (tj. trgovci), su ti koji daju vrednost i upotrebljivost određenoj verziji protokola (i stoga odgovarajućoj valuti), prihvatajući jedinice koje poštuju njegova pravila. Prava moć upravljanja nad Bitcoinom, stoga, leži kod ovih trgovaca, a ne kod programera.




# Postanite suvereni bitkoiner


<partId>df64cad2-e92d-4949-9cca-14394aad0bc6</partId>




## Zašto pokrenuti sopstveni čvor?


<chapterId>39c0cd19-67f9-4c64-bfb3-dbd6eec0bf42</chapterId>



Postoji široko rasprostranjeno verovanje da je upravljanje Bitcoin čvorom isključivo altruistički čin, bez lične koristi, samo u službi decentralizacije mreže. Neki smatraju da je za bitkoinere svojevrsna dužnost da podržavaju sistem i pokažu zahvalnost Bitcoinu.



Kao što smo istakli u prethodnim poglavljima, pokretanje čvora ne donosi direktnu finansijsku dobit. Moglo bi se, dakle, pomisliti da nema lične koristi u tome. Ipak, korišćenje sopstvenog čvora donosi brojne individualne prednosti. Da bih vas uverio u to, u ovom poglavlju ću predstaviti sve razloge, tehničke i strateške, koji bi trebalo da vas podstaknu da instalirate i koristite sopstveni Bitcoin čvor.



### Poverljivija distribucija transakcija



Kada se softver za upravljanje novčanikom poveže sa spoljnim čvorom, on prenosi svoje transakcije na infrastrukturu koja nije pod vašom kontrolom. Ovo generiše očigledne rizike od nadzora: operater udaljenog čvora može analizirati detalje vaših transakcija, uključujući iznose i učestalost, i ukrštanjem određenih metapodataka (kao što su IP adrese, vremena i lokacije), potencijalno ih povezati sa vašim identitetom.



Zaista, kao što je istaknuto u prethodnom poglavlju, novčanici ne komuniciraju sa Bitcoin mrežom magijom; moraju se povezati sa čvorom kako bi proverili stanja ili emitovali transakcije. Ako nikada niste postavili svoj čvor, to znači da vaš novčanik zavisi od infrastrukture treće strane (obično kompanije koja stoji iza softvera). Ova treća strana, posebno ako je kompanija, može posmatrati, iskoristiti ili čak otkriti ove podatke: bilo iz komercijalnih razloga, pod zakonskim pritiskom, ili kao rezultat piraterije.



![Image](assets/fr/059.webp)



Korišćenjem sopstvenog čvora, direktno emitujete svoje transakcije na mrežu, zaobilazeći posrednike. Pod uslovom da pravilno obezbedite svoj čvor (o čemu ćemo kasnije razgovarati) ili se pridržavate određenih standarda, nijedna informacija nije izložena: ni vaša IP adresa niti detalji vaših transakcija ne prolaze kroz entitet koji ne kontrolišete. Ovo je osnovni preduslov za očuvanje vaše poverljivosti na Bitcoinu.



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

### Transakcije koje se ne mogu cenzurisati



Iz istih razloga navedenih gore, softver za upravljanje novčanikom zasnovan na čvoru treće strane je podložan riziku cenzure: operater udaljenog čvora može odbiti da prosledi određene transakcije iz raznih razloga. Može ih smatrati sumnjivim ili suprotnim svojoj politici. Transakcija takođe može biti blokirana ako nije u skladu sa pravilima prosleđivanja čvora. Na kraju, operater može specifično ciljati vašu IP adresu kako bi blokirao emitovanje vaših transakcija.



Suprotno tome, korišćenjem sopstvenog čvora, obezbeđujete propagaciju svojih transakcija unutar peer-to-peer mreže. To znači da zadržavate potpunu kontrolu nad distribucijom svojih transakcija, bez zavisnosti od posrednika. Sve dok transakcija poštuje konsenzus i pravila prosleđivanja čvorova povezanih sa vašim, biće emitovana na mreži, a zatim, pod uslovom da su uključene dovoljne naknade, biće uključena u blok od strane rudara. Posedovanje sopstvenog čvora omogućava neutralno potvrđivanje vaših transakcija bez potrebe za dozvolom.



### Nezavisna verifikacija podataka



Bez ličnog čvora, ostajete zavisni od treće strane za pristup informacijama, kao što su vaš saldo na adresi, status potvrde transakcije i validnost bloka. Ovo podrazumeva implicitno poverenje u tačnost i integritet eksternog čvora.



![Image](assets/fr/060.webp)



Pokretanje full node-a znači da možete sami proveriti sva pravila protokola, za svaku transakciju i svaki blok. Kao rezultat, saldo prikazan na vašem novčaniku nije podatak primljen sa udaljenog servera, već rezultat koji se lokalno izračunava iz vaše potpune kopije blockchaina, validirane blok po blok. Ovaj pristup daje puno značenje maksimi bitkoinera:



> Ne veruj, proveri.

### Bolja raspodela sigurnosti sistema



Svaki čvor koji se pridruži mreži pojačava redundanciju i otpornost Bitcoina. Olakšava širenje informacija i omogućava novim čvorovima da se međusobno povežu. Bez čvorova, sistem bi jednostavno bio neoperativan.



Kao što smo videli, bezbednost Bitcoina nije zasnovana na decentralizaciji, rudarenju, ili kriptografiji: kao i kod svakog sistema, oslanja se na pojedince. Tačnije, zavisi od sposobnosti operatera čvorova da se odupru prinudi.



Ono što razlikuje decentralizovane sisteme poput Bitcoina je raspodela rizika među svim učesnicima u njihovom radu. Pokretanje sopstvenog Bitcoin čvora znači da preuzimate deo ovog rizika time što obezbeđujete bezbednost svoje instance; istovremeno, na taj način olakšavate teret rizika za ostale operatere čvorova.


Dakle, to nije direktna lična korist: pokretanje čvora čini vas delimično odgovornim za bezbednost mreže. Iznad svega, to je kolektivna korist, jer vaše učešće pomaže u raspodeli rizika. Zauzvrat, povećavate sopstvenu sposobnost pouzdanog korišćenja Bitcoina.



### Produbite svoje razumevanje sistema



Instalacija full node-a nije trivijalan zadatak. Uključuje instalaciju softvera, razumevanje osnovnog rada, praćenje sinhronizacije, pregledanje logova u slučaju problema, pa čak i korišćenje terminala. Ovo će vas nužno navesti da produbite svoje razumevanje protokola. Ovo je indirektna, ali ne i beznačajna prednost.



Sticanje ovog znanja jača vaše poverenje u alat i može smanjiti rizik od grešaka ili izloženosti prevarama. Pokretanje sopstvenog čvora znači i učenje.



### Odabir pravila koja će se primeniti



Važan aspekt, koji se često pogrešno shvata, jeste da upravljanje čvorom omogućava da izaberete pravila koja primenjujete lokalno. Postoje dve glavne vrste pravila:





- **Pravila konsenzusa**:



Ovo su osnovna pravila Bitcoin protokola, koja osiguravaju integritet sistema i uspostavljaju kriterijume za validaciju transakcija i blokova. Bilo koja transakcija koja ne ispunjava ova pravila konsenzusa nikada ne može biti uključena u važeći blok. Na primer, transakcija sa nevažećim potpisom na jednom od svojih unosa će biti sistematski isključena.



Promena ovih pravila je ekvivalentna promeni protokola, a samim tim i valute ([Hard Fork](https://planb.academy/en/resources/glossary/hard-fork)). Međutim, čak i bez pokušaja da ih modifikujemo, sama činjenica striktne primene postojećih pravila daje određenu moć: ako blok krši pravila, čvor ga odmah odbacuje.





- **Pravila prosleđivanja (eng. relay rules)**:



To su pravila koja važe za svaki Bitcoin čvor i koja se nadovezuju na konsenzus pravila, kako bi definisala strukturu nepotvrđenih transakcija prihvaćenih u mempool-u i prosleđivanih drugim čvorovima. Svaki čvor konfiguriše i primenjuje ova pravila lokalno, što objašnjava zašto se mogu razlikovati od jednog čvora do drugog. Ona se primenjuju samo na nepotvrđene transakcije: transakcija koju čvor smatra "nestandardnom" biće prihvaćena samo ako se već pojavljuje u važećem bloku. Promena ovih pravila ne isključuje čvor iz Bitcoin sistema.



Na primer, transakcija bez naknada je, prema pravilima konsenzusa, potpuno validna, ali će biti odbijena po defaultu prema Bitcoin Core politici prosleđivanja, jer je parametar `minRelayTxFee` postavljen na `0.00001` (u BTC/kB). Međutim, moguće je, na vašem sopstvenom čvoru, smanjiti ovaj prag kako bi se prosleđivale transakcije sa nižim naknadama, ili, obrnuto, povećati limit, na primer, na 2 Sats/vB, kako bi se izbeglo prosleđivanje transakcija sa niskim naknadama.



Pokretanje sopstvenog čvora znači tvrditi: *"Validiram ono što odlučim da validiram, prema pravilima koja sam sam usvojio"*. Tako postajete akter u upravljanju sistemom, sposoban da odbacite promenu koja vam se čini neprihvatljivom, ili da odobrite ažuriranje prema sopstvenim kriterijumima.



Na taj način možemo brzo proceniti koliko uticaja imate na pravila zahvaljujući svom čvoru. Obim tog uticaja, međutim, zavisi od vrste pravila.



#### Pravila prosleđivanja (releja)



Što se tiče pravila prosleđivanja, suštinska stvar je jednostavno posedovanje čvora, bez obzira na njegovu ekonomsku aktivnost. Ono što je ovde u pitanju jeste da li se slažete da prenosite određene tipove transakcija.



Ako, na primer, verujete da transakcije sa naknadama manjim od 1 sat/vB treba da budu prihvaćene na Bitcoinu, možete prilagoditi ovo pravilo na svom čvoru tako da emituje te transakcije, olakšavajući njihovo širenje kroz mrežu dok ih rudar na kraju ne uključi u važeći blok. U suštini, to je pitanje moći nad širenjem transakcija: svaki čvor ima moć donošenja odluka, jer pristajanjem na prosleđivanje određenog tipa transakcije je jednako promovisanju njenog prihvatanja na Bitcoin mreži. Kao rezultat toga, ako upravljate sa nekoliko čvorova, imate veći uticaj na politiku prosleđivanja, jer svaki čvor ima svoje veze i oblasti uticaja na mreži.



Zaista, imati jedan ili više čvorova konfigurisanih sa specifičnim pravilima prosleđivanja znači odrediti koji deo mreže prihvata da propagira određeni tip transakcije. Širenje poruke u peer-to-peer grafu, kao što je slučaj za Bitcoin transakcije, prati logiku teorije perkolacije. Zamislite svaki čvor kao mesto koje može biti aktivno (`p` = prenosi) ili neaktivno (`1-p`). Čim proporcija `p` pređe kritični prag (`p_c`), pojavljuje se džinovska komponenta: transakcija uspeva da pređe mrežu i ima velike šanse da stigne do rudara. U mreži kao što je Bitcoin, gde svaki čvor održava u proseku 8 odlaznih veza, prag `p_c` je generalno postavljen na samo nekoliko procenata, čak i niže ako neki čvorovi imaju veoma veliki broj veza.



![Image](assets/fr/061.webp)



Sve dok je `p` ispod `p_c`, transakcija ostaje ograničena na izolovane džepove i ne stiže do rudara. Čim se ovaj prag prekorači, širi se gotovo trenutno kroz celu mrežu.



Na kraju, uvek su rudari ti koji odlučuju da li će uključiti transakciju u blok ili ne. Međutim, čvorovi intervenišu "uzvodno" utičući na distribuciju transakcija: oni određuju da li će rudari biti svesni određene transakcije ili ne. Ako transakcija nije prosleđena rudarima, očigledno je nemoguće da će je uključiti u blok.



Dodavanje još nekoliko čvorova će stoga imati samo marginalni uticaj ako je mreža već u fazi perkolacije za dati tip transakcije, ali može biti presudno kako se prag perkolacije približava. Posedovanje ili uticaj na nekoliko čvorova, posebno ako su dobro povezani, može povećati ili smanjiti vrednost `p` i, posledično, indirektno usmeriti pravila prosleđivanja koja određuju koje transakcije se vide i na kraju prihvataju od strane rudara.



#### Pravila konsenzusa



Kada je reč o uticaju vašeg čvora na pravila konsenzusa, njegova ekonomska težina je, pre svega, ono što će biti presudno. Ovo je ključni koncept: vrednost bilo koje valute je direktno povezana sa njenom sposobnošću da olakšava razmenu. Zaista, ako neki predmet nije prihvaćen od strane bilo koga u razmeni za robu ili usluge, teoretski nema monetarnu korisnost. Na primer, ako nijedan trgovac ne prihvata kamenčiće kao sredstvo plaćanja, oni nemaju upotrebu kao novac. Naravno, korisnost ostaje subjektivni pojam na individualnom nivou, ali na datoj teritoriji, što je veći broj trgovaca koji prihvataju neki predmet kao sredstvo razmene, veća je verovatnoća da taj predmet ima monetarnu korisnost za ljude koji žive na toj teritoriji.



Uzmimo primer sela gde mnogi trgovci prihvataju zlato u razmeni za robu: verovatno je da zlato ima monetarnu korisnost za seljane. Ovo ukazuje da korisnost valute direktno zavisi od odluka trgovaca da je prihvate ili odbiju.



Ovaj koncept je ključan za razumevanje dinamike moći u Bitcoin sistemu. Satoshi jasno pokazuje: Bitcoin je elektronski sistem gotovine; drugim rečima, pruža uslugu koja nudi oblik valute, Bitcoin (ili BTC). Kada se pravila protokola modifikuju na način koji nije unazad kompatibilan (hard fork), to znači stvaranje novog sistema i stoga nove valute. Uspeh ili neuspeh ovog forka zatim zavisi od veličine njegove ekonomije, koja je zauzvrat određena brojem trgovaca koji prihvataju ovaj novi oblik valute.



![Image](assets/fr/062.webp)



Hajde da uzmemo primer: pretpostavimo da Bitcoin doživi hard fork. Tada bi postojala 2 različita oblika valute: BTC-1 (originalna, nepromenjena verzija) i BTC-2 (nova valuta sa različitim pravilima konsenzusa). Ako svi trgovci koji su prihvatali BTC-1 nastave da to čine, ali odbiju BTC-2, onda bi potonja, u teoriji, imala veoma ograničenu monetarnu korisnost. Kao korisnik, ne bih imao interes da zadržim i koristim BTC-2, znajući da ga nijedan trgovac ne bi želeo u razmeni za robu ili usluge. Suprotno tome, ako 50% trgovaca odluči da prihvati isključivo BTC-2, a preostalih 50% uzima samo BTC-1, tada bi korisnost BTC-1, u teoriji, bila prepolovljena. Koristim termin "u teoriji" jer korisnost ostaje subjektivna na individualnom nivou i zavisi od mnoštva faktora (kao što su teritorija i potrošačke navike) koje je teško razumeti na pojedinačnoj osnovi.



Na Bitcoin, uloga "trgovca", shvaćena kao bilo koji entitet s određenom ekonomskom težinom, naravno uključuje preduzeća (fizičke prodavnice, sajtove za online prodaju, pružaoce usluga, itd.), ali takođe i menjačnice, budući da prihvataju Bitcoin u razmenu za druge valute, i rudare, budući da prihvataju Bitcoin putem naknada u zamenu za uslugu uključivanja transakcije u blok.



Što se tiče pravila konsenzusa, vaš čvor vam omogućava da usmerite svoju ekonomsku aktivnost ka jednoj ili drugoj valuti. Na primer, ako imate 10 punih čvorova kod kuće, ali nemate značajnu ekonomsku aktivnost, vaš uticaj tokom forka će biti gotovo nikakav. Suprotno tome, jedan čvor koji se koristi za upravljanje lancem od 200 prodavnica koje prihvataju Bitcoin daje značajnu ekonomsku težinu.



Dakle, nije važan broj čvorova, već važnost ekonomske aktivnosti koju podržavaju. Štaviše, ako vaša ekonomska aktivnost zavisi od čvora koji ne kontrolišete, njegov vlasnik će odlučiti koju valutu koristite, sve dok ostanete povezani s tim čvorom. Zato je pokretanje i korišćenje sopstvenog čvora posebno važno u kontekstu upravljanja sistemom:



> Nije tvoj čvor, nisu tvoja pravila.


## Različite vrste Bitcoin čvorova


<chapterId>be8f0baa-41f2-4b54-b011-092f4ccc93aa</chapterId>



Bitcoin čvor  je, dakle, mašina koja pokreće implementaciju Bitcoin protokola. Iza ove uobičajene definicije čvorova, postoji nekoliko mogućih konfiguracija, od kojih ne nude sve isti nivo autonomije, potrošnje resursa i korisnosti za mrežu. U ovom poglavlju pokušaćemo da razumemo ove razlike kako bismo vam pomogli da izaberete arhitekturu čvora koja odgovara vašoj upotrebi i hardverskim ograničenjima.



### Potpuni (eng. full) čvor



Full node je jednostavno Bitcoin čvor koji preuzima ceo blockchain iz Genesis bloka, nezavisno validira svaki blok i lokalno čuva istoriju celog tog blockchaina. Ovo je "normalan" oblik Bitcoin čvora, kako ga je zamislio Satoshi Nakamoto.



![Image](assets/fr/063.webp)



Full node ne mora da veruje nikome jer validira i zna sve informacije u sistemu. To je tip čvora koji vam pruža najviše garancija: znate, bez oslanjanja na treću stranu, da li je uplata validna, da li je blok validan, da li je reorganizacija legitimna, i tako dalje.



U praksi, full node zahteva netrivijalne resurse, uključujući nekoliko stotina gigabajta za blok fajlove, procesor sposoban za validaciju skripti, RAM za mempool i keš memoriju, kao i stabilnu propusnost. Prva sinhronizacija (*IBD*) čita i verifikuje kompletnu istoriju: to je intenzivno, ali se dešava samo jednom. Full node aktivno učestvuje u mreži, prosleđuje blokove i transakcije, i može prihvatiti dolazne konekcije kako bi pomogao drugim čvorovima.



U zavisnosti od vaših potreba, možete dodati indeksator na vaš full node. Bitcoin Core nudi indeksiranje transakcija kao opcionalnu funkciju (deaktiviranu po defaultu), što može biti korisno za specifične svrhe. Međutim, ne uključuje indeksator adresa, koji je često najtraženija funkcija za individualne korisnike. Da biste to rešili, možete instalirati specijalizovani softver na vaš čvor, kao što su Electrs ili Fulcrum, kako bi se ubrzali upiti za proveru stanja sredstava na jednoj adresi na osnovu povezanih UTXO-a. Vratit ćemo se na ulogu indeksatora detaljnije u posebnom poglavlju.



### Pruned čvor



Pruned čvor validira sve kao full node, od Genesis bloka do vrha lanca sa najviše "rada", ali **čuva samo najnoviji deo blok fajlova**. Kada se stari blokovi provere, postepeno ih briše kako bi ostao ispod ograničenja prostora koje možete postaviti. Ova konfiguracija je idealna ako imate ograničenja u prostoru na disku: zadržavate nezavisnost validacije blokova, bez čuvanja kompletne arhive istorije blockchaina. Ova opcija je posebno korisna ako jednostavno želite da instalirate Bitcoin Core na svom ličnom računaru, bez korišćenja specijalizovane mašine.



![Image](assets/fr/064.webp)



Tehničke implikacije ove opcije su prilično jednostavne: pruned čvor je savršeno sposoban da emituje vaše transakcije, učestvuje u prosleđivanju, verifikuje blokove i transakcije, i prati lanac blokova. S druge strane, ne može služiti kao izvor istorijskih podataka izvan svojih granica za druge aplikacije (npr. kompletan blok-istraživač, indeksatori, novčanici...). Funkcije koje zahtevaju arhivu (ili globalni indeks) stoga neće biti dostupne.



U praktičnom smislu, možete koristiti pruned čvor za povezivanje softvera za upravljanje novčanikom kao što je Sparrow novčanik. Međutim, nećete moći skenirati transakcije na vašem novčaniku koje su starije od granice orezivanja (pruning-a). Na primer, ako imate transakciju registrovanu u bloku 901 458, ali vaš čvor čuva samo blokove od 905 402 pa naviše (jer su najstariji izbrisani), nećete moći da skenirate ovu transakciju. S druge strane, ako ste je već skenirali kada je vaš čvor još uvek imao ovu visinu bloka, tada će vaš softver za upravljanje novčanikom sačuvati informacije i prikazati saldo odgovarajućih UTXO-a ispravno.



Ukratko, praćenje novčanika radi glatko na pruned node-u ako napravite novi novčanik dok je softver povezan na taj čvor. Međutim, pri obnavljanju starog novčanika mogu se pojaviti problemi, jer čvor više ne čuva stare transakcije, pa one neće biti dostupne.



### Lagani čvor / SPV



SPV (*Simplified Payment Verification*) čvor, ili lagani čvor, zadržava samo zaglavlja blokova, a ne detalje transakcija, i oslanja se na druge potpune čvorove da dobije dokaz da je transakcija u bloku (Merkle dokazi putem stabala) za koji ima zaglavlje. Koncept pojednostavljene verifikacije plaćanja nije nov, predložio ga je Satoshi Nakamoto lično u delu 8 White paper-a.



![Image](assets/fr/066.webp)



Nakamoto, S. (2008). *Bitcoin: A Peer-to-Peer Electronic Cash System*. https://Bitcoin.org/Bitcoin.pdf



Ovaj tip čvora je očigledno mnogo lakši u pogledu skladištenja i korišćenja CPU-a od potpunog node-a ili čak pruned čvora. SPV čvor je stoga dobro prilagođen manjim uređajima i povremenim vezama. Zapravo, često je direktno integrisan u novčanik, posebno u mobilni softver kao što je Blockstream App.



Kompromis je poverenje i poverljivost: SPV klijent ne proverava skripte ili politike validacije sam; pretpostavlja da je lanac sa najviše rada validan i zavisi od jednog ili više punih čvorova za odgovore. Korišćenje ovog tipa čvora je stoga bolja opcija nego povezivanje sa čvorom treće strane; međutim, i dalje je manje povoljno nego imati potpuni čvor ili čak pruned čvor.



![Image](assets/fr/065.webp)



### Koji čvor je za koju potrebu?





- Mobilni / početni korisnik



Za početnika koji koristi samo novčanik na mobilnoj aplikaciji, korišćenje SPV čvora je sigurno najbolji način za početak. Instalacija je brza, zahteva malo resursa, a iskustvo je jednostavno i fluidno. To znači da možete sami verifikovati određene informacije i, stoga, manje se oslanjati na čvorove trećih strana dok istovremeno postajete nezavisniji kada je u pitanju emitovanje transakcija.





- PC / srednji korisnik



Korisnik srednjeg nivoa sa PC-jem može instalirati pruned čvor kako bi iskoristio gotovo sve prednosti full node-a, bez svakodnevnog preopterećenja svog računara: puna validacija, umerena upotreba diska i jednostavno održavanje. To je idealno rešenje za povezivanje vaših desktop novčanika i ostajanje nezavisnim u distribuciji vaših transakcija, bez ulaganja u specijalizovanu mašinu ili preopterećenja prostora na disku.





- Suvereni Bitcoiner / napredno



Puni čvor ostaje najbolje rešenje ako želite da budete potpuno nezavisni u korišćenju Bitcoina i da se kasnije ne ograničavate u naprednijim upotrebama, poput indeksera, Lightning čvora ili čak pretraživača blokova. Upravo to ćemo istražiti u ovom kursu!



## Pregled softverskih rešenja


<chapterId>0d48b89a-e8b5-441e-a707-537a035fc15e</chapterId>



Sa softverske strane, postoje 2 glavna načina za pokretanje Bitcoin čvora:




- direktno instalirajte implementaciju protokola, kao što je Bitcoin Core (preporučeno), ili Bitcoin Knots,
- ili koristiti turnkey distribuciju (često nazvanu "_node-in-a-box_") koja uključuje Bitcoin implementaciju na isti način, ali takođe uključuje sistem za administraciju preko interfejsa, prodavnicu aplikacija i alate spremne za upotrebu (Lightning, pretraživače, indekser servere (eng. index servers), čak i aplikacije za samostalno hostovanje izvan Bitcoina...).



Oba pristupa vode istom cilju: imati svoj čvor, ali se razlikuju u pogledu instalacije i korišćenja grafičkog interfejsa, održavanja, proširivosti i troškova. To ćemo istražiti u ovom poglavlju.



### Osnovne implementacije Bitcoin čvorova



Instaliranje osnovne implementacije znači direktno korišćenje softvera sa implementacijom Bitcoin protokola (kao što je Core), bez dodatnog softverskog sloja. Sami upravljate konfiguracijom, ažuriranjima i povezanim uslugama (indeksiranje, API, Lightning, bekapovi, itd.) prema vašim potrebama.



Ovo je najviše suvereni i fleksibilni pristup: tačno znate šta se pokreće, gde su podaci i kako sve funkcioniše. S druge strane, postaje složenije čim želite da pređete dalje od samog osnovnog rada Bitcoin čvora. Ako vam je cilj samo da imate čvor, složenost je uporediva sa čvorom tipa 'node-in-a-box', pa čak i manja, jer se radi jednostavno o instaliranju softvera.



#### Bitcoin Core (dominantni klijent)



[Bitcoin Core je klijent koji koristi ogromna većina mreže.](https://bitcoincore.org/). Preuzima, validira i održava blockchain, pruža RPC/REST API-je i može integrisati novčanik. Ako preferirate standardne alate i osećate se prijatno da sami dodajete usluge (kao što su Electrum server, explorer i LND), bolje je da koristite Core kakav jeste.



**Prednosti:** Maksimalna stabilnost, predvidljivo ponašanje, iskustvo iz prve ruke, lako za instalaciju i konfiguraciju.



**Nedostaci:** Morate ručno izgraditi ostatak softverskog sloja kako biste kreirali kompletno aplikaciono okruženje, a ne samo Bitcoin čvor.



https://planb.academy/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

https://planb.academy/tutorials/node/bitcoin/bitcoin-core-mac-windows-9684ab02-e0af-41c9-8102-86ac7c7727f3

#### Bitcoin Knots (glavni alternativni klijent)



[Bitcoin Knots je fork od Bitcoin Core-a](https://bitcoinknots.org/), koji održava Luke Dashjr. To je glavni alternativni klijent za Core za implementaciju Bitcoin protokola. Potpuno kompatibilan sa ostatkom mreže (nikako nije hard fork kao Bitcoin Cash), ipak nudi dodatne funkcije, uključujući opcije za definisanje pravila prosleđivanja (eng. relay rules) koje su odsutne iz Core-a, ili se primenjuju strožije po defaultu kako bi se ograničilo ono što neki smatraju spamom (neželjeni sadržaj).



Postoje 2 moguća razloga za odabir Knots-a umesto Core-a:




- **Tehnički**: Različite opcije iz Core-a, posebno u smislu upravljanja relejima (prosleđivanjima), određivanjem koje transakcije prihvata i emituje vaš čvor.
- **Politički**: Neki ljudi preferiraju korišćenje alternativnih klijenata kao što je Knots iz netehničkih razloga, posebno da bi podržali alternativu Core-u i tako smanjili njegov monopol. Ako bi Core ikada bio kompromitovan, bilo bi korisno ne samo imati solidne, dobro održavane alternativne klijente već i znati kako ih efikasno koristiti. Drugi koriste Knots iz protesta, jer su izgubili poverenje u Core-ove programere ili ne odobravaju način upravljanja većinskim klijentom.


https://planb.academy/tutorials/node/bitcoin/bitcoin-knots-e04b2196-4df2-4246-86ef-c02269c29098

Lično, preporučujem da izaberete Core, prvenstveno da biste brže iskoristili sigurnosne zakrpe. Naime, neke ranjivosti otkrivene u Knots-u se ispravljaju sa zakašnjenjem. Generalno gledano, razvojni proces Core-a je solidno strukturiran i podržan od strane velikog broja saradnika, dok Knots održava jedna osoba i ima mnogo manju zajednicu. S druge strane, pravila releja danas imaju tendenciju da gube svoju korisnost, posebno kada ih primenjuje samo mali deo mreže (prema teoriji perkolacije).



### Node-in-a-box distribucije



_Node-in-a-box_ kombinuje Bitcoin Core (ili Knots) sa unapred konfiguriranim operativnim sistemom, web interfejsom, i App Store-om za samohostujuće usluge (Lightning, explorers, Electrum server, Mempool, BTCPay Server, Nextcloud, itd.). Samo jednim klikom možete instalirati, ažurirati i međusobno povezati ove različite module.



To je mnogo jednostavnije rešenje za pokretanje i upravljanje brojnim pomoćnim aplikacijama na dnevnoj bazi. Nedostatak je što kada se pojavi problem (npr. sukob Docker slika, neispravna ažuriranja, oštećena baza podataka), otklanjanje grešaka može postati veoma složeno, jer zavisite od integracije same distribucije. Štaviše, podrška zajednice ili zvanična podrška često je komplikovana.



Dakle, node-in-a-box je izuzetno lak za korišćenje sve dok sve radi kako treba, ali u slučaju greške, morate biti spremni da sprovedete dugotrajne pretrage, čekate pomoć i "zaprljate ruke".



Većina ovih rešenja dostupna je u dva formata:




- Unapred sastavljena mašina: kompletan računar sa već instaliranim operativnim sistemom. Ove mašine na principu "plati kako koristiš" jednostavno treba priključiti na struju i povezati na internet da bi bile operativne. Ako vaš budžet to dozvoljava, ova opcija ima prednost što je vrlo jednostavna za postavljanje, često nudi prioritetnu podršku i doprinosi finansiranju razvoja, s obzirom da je poslovni model ovih kompanija uglavnom zasnovan na prodaji hardvera.
- "Uradi sam": instaliraj distribucioni OS na svoju mašinu (stari PC, NUC, Raspberry Pi, kućni server...). Ovo je najekonomičnije rešenje, jer možete reciklirati staru mašinu ili odabrati hardver koji tačno odgovara vašim potrebama i budžetu. Takođe je najfleksibilnija opcija i najzadovoljavajuća za konfigurisanje. Ovaj pristup ćemo istražiti u praktičnom delu kursa.



Evo pregled glavnih dostupnih node-in-a-box rešenja (2025. godine):



### Umbrel (umbrelOS & Umbrel Home)



[Danas je Umbrel lider u rešenjima za node-in-a-box (https://umbrel.com/). Njegov uspeh je u velikoj meri zahvaljujući jednostavnosti instalacije (kada je pokrenut na običnom Raspberry Pi uređaju), njegovom elegantnom i intuitivnom interfejsu, i ekosistemu aplikacija koji je brzo rastao i sada je izuzetno obiman.



![Image](assets/fr/067.webp)



Pokrenut 2020. godine kao jednostavan Bitcoin čvor praćen nekolicinom pomoćnih aplikacija, Umbrel je postepeno evoluirao u potpuno opremljen, moderan kućni oblak (eng. cloud).



Neću ulaziti u više detalja ovde o tome kako funkcioniše i njegovim specifičnim karakteristikama, jer ćemo ih detaljnije ispitati u prvom poglavlju sledećeg dela. Zaista, za potrebe ovog BTC 202 kursa, odlučio sam da koristim umbrelOS, za koji verujem da je trenutno najbolje rešenje za node-in-a-box za početnike i korisnike srednjeg nivoa.



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

### Start9 (StartOS)



[Start9 nudi StartOS (https://start9.com/), sistem dizajniran za "suvereno računarstvo": cilj je da svako poseduje i upravlja sopstvenim privatnim serverom, unapređen tržištem aplikacija koje se samostalno hostuju. Možete kupiti Start9 server (Server One za $619, Server Pure za $899) ili sastaviti svoj u DIY režimu na sopstvenoj mašini.



Na strani Bitcoina, StartOS vam omogućava instalaciju full node-a, Lightning čvora, BTCPay Servera, Electrs-a i mnogih drugih servisa. Međutim, privlačnost Start9 seže dalje od ovoga: nudi mogućnost pregleda, konfiguracije i izlaganje različitih softverskih servisa (oblak za fajlove, poruke, nadgledanje) na jedinstven način, uz potpunu kontrolu. Projekat je stoga namenjen korisnicima koji žele robusnu platformu za samostalno hostovanje, a ne samo jednostavan Bitcoin čvor. Verovatno je najkompletniji ekosistem posle Umbrel-a.



![Image](assets/fr/068.webp)



Glavna razlika sa Umbrelom leži u interfejsu. Umbrel se oslanja na visoko uglađen UX, dok Start9 nudi grublji, funkcionalniji interfejs. Ekosistem aplikacija Start9 je manje bogat od Umbrelovog, ali to nadoknađuje sa nekoliko tehničkih prednosti: pristup naprednim postavkama aplikacija je pojednostavljen, dok Umbrel brzo postaje restriktivan ako željena opcija nije obezbeđena od strane interfejsa. Start9 je takođe veoma dobar u upravljanju bekapovima: osim Umbrelovog dobrog rešenja za LND, ne postoji objedinjeni sistem kao što to ima Start9. Štaviše, nudi pristupačnije alate za nadgledanje i šifrovanu daljinsku vezu (`https`), dok je lokalni pristup Umbrelu putem `http`.



Ukratko, ako vam jednostavno trebaju osnovne aplikacije za Bitcoin, bez posebnog interesa za Umbrel-ov vrlo bogat ekosistem, i korisnički interfejs nije prioritet, onda je Start9 bolja opcija. U suprotnom, Umbrel je bolji izbor.



https://planb.academy/tutorials/node/bitcoin/start9-8c8b6827-8423-4929-bcba-89057670ed6a

### MyNode



[MyNode je distribucija fokusirana isključivo na Bitcoin i Lightning](https://mynodebtc.com/), koja nudi web interfejs, prodavnicu aplikacija i nadogradnje jednim klikom. Možete kupiti gotov hardver (*Model Two* dostupan za $549) ili instalirati MyNode besplatno na sopstvenoj mašini. Projekat takođe nudi *Premium* verziju softvera ($94), koja uključuje prioritetnu podršku i napredne funkcije.



![Image](assets/fr/069.webp)



U praksi, MyNode okuplja sve osnovne komponente potrebne za rad full node-a, kao i aplikacije neophodne Bitcoin korisnicima. Stoga je to prikladno rešenje ako vam nisu potrebne aplikacije izvan Bitcoin ekosistema, kao što su aplikacije koje se samostalno hostuju i koje se nalaze u Start9 i Umbrel sistemima.



https://planb.academy/tutorials/node/bitcoin/mynode-a481fef3-2fd3-4df3-91c0-112cffa094eb

### RaspiBlitz



[RaspiBlitz je 100% open source projekat](https://docs.raspiblitz.org/) (MIT licenca) za montiranje Bitcoin čvora i Lightning čvora na Raspberry Pi. Jednostavno preuzmite sliku, pokrenite je, a zatim pratite čarobnjaka da biste imali funkcionalan node-in-a-box na vašem Raspberry Pi-ju. Unapred sastavljeni kompleti su takođe dostupni od trećih strana, obično između $300 i $400, u zavisnosti od hardvera. RaspiBlitz takođe nudi niz dodatnih, lako instalirajućih aplikacija.



![Image](assets/fr/070.webp)



Ako posedujete Raspberry Pi, ovo je odlična opcija, jer sve kompletniji sistemi poput Umbrel-a postaju sve zahtevniji za ovakve mini-PC uređaje.



https://planb.academy/tutorials/node/bitcoin/raspiblitz-d8cdba2e-a682-46cf-9fdc-d8602fbeac02

### RoninDojo



[RoninDojo je node-in-a-box fokusiran na privatnost](https://wiki.ronindojo.io/en/home) koji automatizuje implementaciju Samurai Dojo-a i Whirlpool-a, sa posvećenim grafičkim interfejsom i dodacima posebno dizajniranim za Samurai ekosistem.



Princip je jednostavan: ako koristite Ashigaru Wallet (naslednik forkovane verzije Samurai Wallet-a, nakon hapšenja njegovih programera) ili ako želite da iskoristite napredne alate za privatnost, RoninDojo je za vas.



![Image](assets/fr/071.webp)



Projekat je ranije nudio unapred konfigurisan uređaj pod nazivom Tanto, ali trenutno nije dostupan. Možda će se vratiti kasnije. U međuvremenu, moguće je lako instalirati RoninDojo na Rock5B+ ili Rockpro64, ili čak indirektno na Raspberry Pi.



https://planb.academy/tutorials/node/bitcoin/ronin-dojo-v2-0ddb3854-6f38-4466-b4e2-f66c028e0dd8

### Nodl



Još jedno [rešenje "node-in-a-box" je Nodl](https://www.nodl.eu/). Kao i kod prethodnih projekata, možete ili kupiti unapred konfigurisan hardver (između €599 i €799, u zavisnosti od modela) ili ga sami instalirati u DIY režimu.



Na softverskoj strani, Nodl integriše Bitcoin core, LND, BTCPay Server, Electrs, Dojo, Whirlpool, Lightning Terminal, RTL, kao i BTC RPC Explorer, sve sa integrisanim lancem ažuriranja i open-source kodom pod MIT licencom.



![Image](assets/fr/072.webp)



Nakon što ste istražili različita softverska rešenja, sada je vreme da izaberete mašinu koja će ugostiti vaš čvor!




## Pregled hardverskih rešenja


<chapterId>245d6add-9cda-46b9-9343-31dcdd70456e</chapterId>



Sada kada smo istražili sve softverske mogućnosti, usredsredimo se na hardver potreban za vaš čvor. Pružiću vam konkretne savete o izboru komponenti, zajedno sa konfiguracijama prilagođenim različitim budžetima. Naravno, ovo je moje lično mišljenje i povratna informacija iz iskustva: sigurno postoje i druge relevantne alternative pored onih predstavljenih ovde. Nadalje, neću ponovo razmatrati unapred sastavljene mašine koje nude projekti node-in-a-box, koje smo već pokrili u prethodnom poglavlju. Ovde ćemo se isključivo fokusirati na DIY rešenja.



### Da li vam zaista treba namenska mašina?



Tokom proteklih nekoliko godina, bitkoineri su postali sve svesniji uobičajene zablude, posebno sa popularizacijom node-in-a-box početkom 2020-ih: Bitcoin čvor treba nužno da radi na mašini posvećenoj isključivo ovoj svrsi. Ali to nije tačno. Ne treba vam nužno posvećen računar za pokretanje Bitcoin čvora: Bitcoin Core je savršeno sposoban da radi na vašem svakodnevnom računaru. Ako imate dovoljno prostora na disku za blockchain ili omogućite pruning, možete validirati lanac, povezati svoj novčanik, pa čak i zatvoriti program kada završite sa korišćenjem. Prednost ovog pristupa je značajna: nulta početna investicija i minimalna složenost.



![Image](assets/fr/074.webp)



S tim u vezi, korišćenje namenske mašine je često praktičnije. Namenska mašina može raditi neprekidno (24/7), biti daljinski dostupna u svakom trenutku, neće monopolizovati resurse vaše glavne mašine, i, iznad svega, izolovanje upotrebe (dobra sigurnosna praksa: ako vaš lični računar naiđe na problem, vaš čvor nastavlja da funkcioniše, i obrnuto). Dakle, pitanje nije "Da li treba da ima posebnu mašinu?", već "Da li mi treba čvor koji je stalno online, dostupan drugim uređajima, i koji je prilagodljiv i može da se unapređuje?" (Lightning, indeksatori, dodatne aplikacije...). Ako je odgovor da, izbor zasebne mašine će stvari učiniti mnogo jednostavnijim.



### 3 metode nabavke: reciklaža, polovno i novo



#### Recikliranje starog PC-ja



To je najekonomičnije rešenje. Većina nas ima stari PC koji skuplja prašinu kod kuće, ili kod prijatelja i porodice: ovo je savršena prilika da ga vratite u upotrebu! Da biste ga prilagodili za korišćenje kao Bitcoin čvor, jednostavno dodajte 2TB SSD i, u zavisnosti od vaših potreba, zamenite ili dodajte RAM memorijske module kako biste povećali RAM. Očekujte da ćete platiti između €100 i €200 za potpuno funkcionalnu mašinu.



Pre nego što kupite bilo koji hardver, proverite broj dostupnih slotova za diskove, tip konekcije (M.2 ili SATA), format RAM-a (SODIMM ili DIMM) i njegovu generaciju (DDR4, itd.). Takođe, iskoristite priliku da očistite mašinu, posebno ventilator, kako biste osigurali optimalne performanse.



Međutim, budite oprezni ako koristite laptop: baterija može postati problem tokom vremena (više o tome kasnije u poglavlju).



#### Obnovljeno ili polovno



Tržište je puno obnovljenih poslovnih mini-PC-ja kao što su *Lenovo ThinkCentre Tiny*, *HP EliteDesk Mini* ili *Dell OptiPlex Micro*. Ove mašine su čvrste, kompaktne, tihe i energetski efikasne. Njihova cena je znatno niža od novih, i lako je pronaći modele opremljene sa 6. do 10. generacijom i5/i7 procesora i 8 do 16 GB RAM-a, sve po vrlo atraktivnim cenama, uglavnom između €70 i €200, u zavisnosti od konfiguracije. Po mom mišljenju, ovo je verovatno najbolja opcija ako tražite posvećenu mašinu za vaš Bitcoin čvor.



![Image](assets/fr/075.webp)



Takođe je moguće pronaći polovne računare i laptopove starih nekoliko godina, sa zanimljivim konfiguracijama i odličnim odnosom cene i kvaliteta.



**Napomena:** mašine iz korporativnih flota, kao što je *ThinkCentre Tiny*, često su opremljene samo sa *DisplayPort* (DP) priključkom za ekran, bez HDMI izlaza. Zato ne zaboravite da ponesete adapter ili DP-u-HDMI kabl ako vam je potreban.



#### Kupovina novog



Ako vaš budžet dozvoljava, možete se odlučiti i za novu mašinu. Ovo je dobra opcija ako želite da imate nedavni hardver sa dobrim performansama, posebno ako planirate da koristite Umbrel ili Start9 sa dodatnim aplikacijama van Bitcoin ekosistema za samohostovanje.



### Koju vrstu mašine treba da izaberem?



#### Mini-PC "NUC" / barebone (osnovna konfiguracija bez RAM-a i diska)



Mini-PC-ovi, po mom mišljenju, nude najbolji kompromis za hostovanje Bitcoin čvora kod kuće. Štede prostor, lako se uklapaju na policu, troše minimalnu energiju i omogućavaju jednostavne hardverske modifikacije, kao što su dodavanje RAM-a ili zamena SSD-a.



Lično, više volim *Lenovo ThinkCentre Tiny*, koji je veoma rasprostranjen na tržištu polovnih uređaja (iz korporativnih flota); posebno su robusni i laki za modifikaciju. Naravno, postoje mnogi ekvivalenti od drugih proizvođača: *Dell OptiPlex Micro*, *HP ProDesk / EliteDesk Mini / Micro*, *Intel NUC*, *Gigabyte BRIX*, *MSI Cubi*..



![Image](assets/fr/001.webp)



**Ističe se:** kompaktne dimenzije, umerena potrošnja energije, nizak nivo buke, skalabilnost (u zavisnosti od modela) i pouzdanost.



**Slabosti:** malo skuplji od SBC-a tipa Raspberry Pi, nema ugrađen ekran (daljinski pristup ili putem spoljnog monitora), nema bateriju (iznenadno gašenje u slučaju nestanka struje).



#### Posvećen laptop



Posvećen laptop je odlična jeftina alternativa mini-PC-ju: danas možete pronaći polovne ili čak nove laptopove po niskim cenama, opremljene pristojnim procesorima, brojnim portovima, kao i integrisanim ekranom i tastaturom (veoma praktično za početnu instalaciju). Iznad svega, baterija deluje kao prirodni UPS: u slučaju nestanka struje, čvor se ne gasi naglo i može ostati operativan čak nekoliko sati.



![Image](assets/fr/076.webp)



**Istaknuto:** Sve-u-jednom rešenje, baterija deluje kao UPS (bez prekida napajanja), pojednostavljena instalacija zahvaljujući integrisanom ekranu i tastaturi, integrisana Wi-Fi kartica, kao i velikom izboru na tržištu polovnih i novih uređaja (što često znači da možete pregovarati o cenama).



**Slabosti:** nešto veća potrošnja energije u poređenju sa barebone Mini-PC-jem, postepeno trošenje baterije pri 24/7 radu uz gubitak kapaciteta, retki ali stvarni rizik je da s vremenom može doći do naduvavanja baterije ili termalne nestabilnosti (pregrevanje i rizik od samopropadanja). Upravo ovaj aspekt me navodi da smatram mini-PC boljom opcijom od laptopa: postepena degradacija baterije i povezani rizici.



Ako izaberete ovo rešenje, preporučujem da pažljivo pratite stanje baterije kako biste sprečili bilo kakvu opasnost. Obratite pažnju na prekomernu toplotu, neobične mirise, nestabilnost ili deformisanu školjku. U slučaju alarma, odmah isključite i odspojite računar, a zatim odložite bateriju u specijalizovani centar za reciklažu.



**Savet:** Ako BIOS/UEFI ili alat proizvođača to omogućava, postavite ograničenje opterećenja (npr. 60% ili 80%) kako biste produžili vek trajanja baterije.



#### Raspberry Pi i drugi SBC-ovi: pogrešna ideja



Početkom 2020-ih, sa porastom softvera node-in-a-box, Raspberry Pi manija se takođe pojavila kao sredstvo za pokretanje Bitcoin čvora. Ideja je delovala privlačno: jeftino, kompaktno i pristupačno.



![Image](assets/fr/073.webp)



U praksi, ako je vaš cilj isključivo pokretanje Bitcoin čvora bez dodatnih aplikacija, Raspberry Pi može biti dovoljan. Ali čim želite koristiti Umbrel, Start9 ili bogatiji ekosistem (block explorer, indeksator adresa, Lightning čvor, aplikacije za samostalno hostovanje...), mašina brzo dostiže svoje granice.



Raspberry Pi ima nekoliko nedostataka:




- procesori koji su previše tanki, sa ARM arhitekturom koja je ponekad nekompatibilna sa određenim softverom ili zahteva više rukovanja;
- zalemljeni RAM, nemoguće ga je nadograditi, sa ograničenim konfiguracijama (često maksimalno 8 GB);
- eksterna kućišta za SSD-ove povezana kablom, česti izvori grešaka, zahtevaju kupovinu specifične kartice za stabilan SSD;
- tendencija brzog zagrevanja i poteškoće u osiguravanju pravilnog hlađenja;
- treba kupiti dodatni hardver (kućište, ventilator, SSD kartica, itd.);
- veoma ograničena povezanost.



Istorijski gledano, velika prednost SBC-ova poput Raspberry Pi-ja bila je njihova cena: za nekoliko desetina evra mogli ste dobiti namenski uređaj. Međutim, danas su cene naglo porasle, i kada dodate sav neophodan dodatni hardver, trošak se približava ceni prvih polovnih ili obnovljenih x86 mini-PC-jeva, koji, po mom mišljenju, nude mnogo više prednosti. Iz tog razloga, ne preporučujem izbor SBC-a.



### Odabir komponenti



#### Skladištenje na disku: SSD obavezno, minimum 2 TB



Tehnički, moguće je pokrenuti Bitcoin čvor na HDD-u. Problem je što će se sve znatno usporiti, posebno IBD, koji će postati izuzetno dug zbog intenzivne upotrebe diska kao keša od strane Bitcoin Core-a (posebno za UTXO set). Zato snažno savetujem protiv korišćenja HDD-a: stvara pravo usko grlo, značajno ograničava buduće mogućnosti nadogradnje (npr. za Lightning čvor), i može čak izazvati probleme u sinhronizaciji sa najnovijim blokom na blockchainu. Štaviše, konstantan stres na mehaničkom disku povećava rizik od prevremenog habanja.



SSD-ovi radikalno menjaju vaše korisničko iskustvo: sve postaje brže i glađe, uz daleko veću pouzdanost. Korišćenje SSD-a je stoga (gotovo) obavezno za vaš čvor, i nećete zažaliti, posebno jer su modeli velikog kapaciteta sada relativno pristupačni.



![Image](assets/fr/077.webp)



U smislu kapaciteta, 2TB se postepeno uspostavlja kao nova razumna minimalna vrednost. U leto 2025. godine, blockchain već dostiže 700 GB, a ako dodate Umbrel, indeksator adresa i nekoliko aplikacija, 1 TB SSD će ubrzo biti iskorišćen do kraja. Sa 2TB, imate udobnu marginu za godine koje dolaze (u širokoj proceni, između 5 i 15 godina). Takođe možete odabrati 4TB ako planirate koristiti mnogo aplikacija na Umbrel-u, skladištiti velike fajlove u samostalnom hostingu, ili ako želite da u velikoj meri predvidite svoje potrebe za prostorom na disku.



![Image](assets/fr/078.webp)



Što se tiče formata, to će zavisiti od portova dostupnih na vašem uređaju; međutim, ako je moguće, preporučujem korišćenje NVMe M.2 SSD-a.



#### Memorija (RAM): 8 do 16 GB



Za Bitcoin Core sam (bez Umbrel sloja), preporuke programera ukazuju na minimum od 256 MB RAM-a sa podešavanjima prilagođenim na najniže postavke, 512 MB sa podrazumevanim podešavanjima i 1 GB za normalnu upotrebu.



S druge strane, ako koristite sistem "node-in-a-box" kao što su Umbrel ili Start9, zahtevi za RAM-om su značajno veći. Programeri Umbrela preporučuju minimum od 4 GB RAM-a. Ovo može biti dovoljno samo za pokretanje Core-a, ali ćete uskoro biti ograničeni. Stoga preporučuju 8 GB, što i ja smatram minimumom za osnovnu konfiguraciju oko Bitcoina (Core, LND, indeksator i nekoliko aplikacija). Po mom iskustvu, sa Umbrelom i nekoliko dodatnih usluga, 8 GB je i dalje malo tesno. Da biste bili zaista komforni i imali neku rezervu, preporučio bih 16 GB RAM-a.



#### Procesor (CPU)



Za Umbrel čvor, minimalni zahtev je dvojezgarni 64-bitni procesor od Intela ili AMD-a. Ako želite da koristite nekoliko aplikacija pored Bitcoin Core-a, četvorojezgarni (ili jači) procesor će napraviti stvarnu razliku u pogledu fluidnosti. Na primer, procesori i5/i7 od 6. do 10. generacije su odlične opcije na tržištu polovnih uređaja.



### Primeri konkretnih konfiguracija



Ispod predlažem tri konkretne konfiguracije, prilagođene različitim budžetima i potrebama, sa preciznim modelima koji ih podržavaju. Ovi izbori su dati kao primeri da ilustruju informacije u ovom poglavlju; niste obavezni da izaberete tačno ove modele. Kako smatram da je mini-PC najbolja opcija na duži rok, oslanjaću se na ovaj format za tri predložene konfiguracije.



*Cene prikazane ispod su samo indikativne i mogu varirati u zavisnosti od regiona, prodavca i perioda*



Prvo i najvažnije, potreban vam je SSD koji je dovoljno velik da primi blockchain, a da pritom ostane prostora za manevrisanje. SSD-ovi imaju ograničen vek trajanja u smislu ciklusa pisanja i ukupne količine podataka koji se pišu. Međutim, Bitcoin čvor stavlja značajno opterećenje na disk prilikom pisanja. Zato ne preporučujem modele početnog nivoa; umesto toga, predlažem NVMe SSD, koji nudi značajno bolje performanse.



Kao primer, za potrebe ovog kursa, izabrao sam sledeći model: *Samsung 990 EVO Plus NVMe M.2 SSD 2Tb*, dostupan za oko €120 na Amazonu. Takođe možete odabrati druge poznate brendove kao što su Crucial, Western Digital ili Kingston.



![Image](assets/fr/046.webp)



#### Konfiguracija niskog budžeta



Očigledno, ako je vaš budžet veoma ograničen (ispod €200), savetovao bih vam da ne investirate u namenski uređaj, već da instalirate Bitcoin Core direktno na vaš svakodnevni PC (u pruned modu ako vam nedostaje prostora na disku).



Inače, za početni budžet preporučujem *HP EliteDesk 800 G2 Mini*. Našao sam obnovljeni model za 96 € na Amazonu, opremljen Intel Core i5 procesorom 6. generacije i 8 GB RAM-a. Ovo je posebno zanimljiva opcija za početnike: ovaj procesor i ova količina memorije su više nego dovoljni za pokretanje Core-a na Umbrel-u, kao i nekoliko aplikacija istovremeno, kao što su Electrs indeksator, Lightning čvor i Mempool instanca, pod uslovom da ne dodelite previše keša za Core. Štaviše, ovaj tip mini-PC-a omogućava lako povećanje RAM-a na 16 GB, na primer, ako se ukaže potreba (očekujte da ćete platiti oko 30-40 € dodatno za jedan ili dva kvalitetna RAM modula).



![Image](assets/fr/045.webp)



Zatim jednostavno dodajte SSD u budžet. Počevši sa Samsung 2TB po ceni od €120, dobijamo ukupni trošak od €216 za kompletnu, funkcionalnu mašinu.



#### Konfiguracija srednjeg budžeta



Ako imate prosečan budžet od oko €300 za mašinu koja će hostovati vaš čvor, preporučujem *Lenovo ThinkCentre Tiny*, na primer, opremljen procesorom visokih performansi i dovoljnom količinom RAM-a. Našao sam obnovljeni model na Amazonu za €180, sa Intel Core i7 procesorom 6. generacije i 16GB RAM-a. Uz dodatak 2TB SSD-a po ceni od €120, ukupni trošak iznosi €300.



![Image](assets/fr/044.webp)



Sa ovom mašinom, imate udobnu konfiguraciju: brz IBD i mogućnost pokretanja brojnih aplikacija na vašem Umbrel-u ili Start9 bez poteškoća. Ovo je upravo konfiguracija koju koristim za ovaj BTC 202 kurs.



#### Visokokvalitetna konfiguracija



Sa većim budžetom, mogućnosti postaju značajno šire. Možete izabrati DIY konfiguraciju, ili čak odabrati unapred sastavljenu mašinu koju nudi direktno projekat node-in-a-box.



Na primer, *ASUS NUC 14 Pro* je dostupan nov na Amazonu za €540. Za ovu cenu, dobijate Intel Core Ultra 5 procesor (noviji i posebno visokih performansi), praćen sa 16 GB DDR5 RAM-a. Sa takvom konfiguracijom, moći ćete da završite IBD u rekordnom vremenu i instalirate zahtevne aplikacije bez poteškoća.



Ovo je izuzetno udobna konfiguracija, čak i preterana ako je početni cilj jednostavno pokretanje Bitcoin čvora. S druge strane, ako želite da u potpunosti iskoristite sve aplikacije za samostalno hostovanje dostupne na Umbrel i Start9, ovaj nivo snage je upravo pravi za vas.



![Image](assets/fr/043.webp)



U zavisnosti od vaše namene, možete se odlučiti za SSD od 2TB, kao u drugim konfiguracijama, ili direktno za SSD od 4TB po ceni od €260 ako takođe želite da skladištite lične fajlove i proširite svoje samostalno hostovanje. Sa SSD-om od 2TB, ukupna cena konfiguracije je €660, dok sa SSD-om od 4TB dostiže €800.



### Još nekoliko saveta





- Ako želite da kupite polovnu opremu i platite u bitkoinima, pridružite se okupljanju u vašoj blizini! Razgovarajući sa drugim učesnicima, sigurno ćete pronaći odgovarajuću opremu po povoljnoj ceni, dok pomažete da se održi cirkularna ekonomija oko Bitcoina. To je takođe prilika da dobijete korisne savete od zajednice.





- Za internet konekciju, biće vam potreban RJ45 Ethernet kabl, barem za instalaciju sistema.





- Neka okruženja, kao što je Umbrel, omogućavaju korišćenje Wi-Fi-ja, ali performanse će generalno biti lošije (posebno ako želite da koristite svoj Lightning čvor na daljinu, jer to može imati uticaj). Ako izaberete Wi-Fi, osigurajte da vaš uređaj ima ugrađenu karticu ili dodajte kompatibilni adapter.





- Uvek koristite originalno proizvođačevo napajanje za vašu mašinu. Ovo je ključno kako biste sprečili oštećenje vaše opreme i rizik od izbijanja požara.





- Ako vaša mašina nema ugrađenu bateriju, dobra je ideja uložiti u inverter kako biste izbegli iznenadna gašenja.





- U zavisnosti od vrednosti vaše opreme i vaše geografske lokacije, sistem protiv udara groma takođe može biti prikladan, bilo direktno na razvodnoj ploči, bilo na produžnoj utičnici





- Na kraju, zapamtite da optimizujete hlađenje vaše mašine: redovno je čistite i instalirajte na hladnom, dobro provetrenom, urednom mestu kako biste izbegli pregrevanje, što može dovesti do smanjenja performansi (throttling - namerno smanjenje brzine procesora).



# Jednostavna instalacija Bitcoin čvora


<partId>ca6cf2a5-0bcc-41d9-b556-0d38865bf98f</partId>




## Umbrel: mnogo više od Bitcoin čvora


<chapterId>dd4c04f1-924a-43e1-94f3-ea9fbc83dd43</chapterId>



Umbrel je operativni sistem za lične servere dizajniran da učini samostalno hostovanje pristupačnim: instalirate Umbrel, otvorite pregledač na `umbrel.local` i upravljate svime putem jednostavnog daljinskog interfejsa.



Projekat je prvo popularizovao ideju o Bitcoin i Lightning čvoru na jedan klik, a zatim se proširio u pravi "kućni oblak": skladištenje fajlova i fotografija, multimedijalni streaming, mrežni alati, kućna automatizacija, lokalni AI i stotine aplikacija koje se mogu instalirati iz integrisane prodavnice aplikacija.



U Umbrelu, svaka aplikacija radi u Docker containeru (izolacija, atomska ažuriranja, nezavisno pokretanje/zaustavljanje). Interfejs centralizuje pristup svim ovim aplikacijama, nudeći jedinstvenu prijavu (sa opcionalnim 2FA), ažuriranja OS i aplikacija jednim klikom, praćenje rada mašine u realnom vremenu (CPU, RAM, temperatura, skladište), upravljanje dozvolama između aplikacija i pregled njihove potrošnje.



Umbrel ima za cilj da vam vrati kontrolu i poverljivost vaših podataka bez oslanjanja na cloud servise — i ne svodeći se samo na pokretanje Bitcoin čvora.


### Umbrel Home vs umbrelOS



Umbrel nudi dva različita pristupa:





- [**Umbrel Home**](https://umbrel.com/umbrel-home): ovo je mini-server spreman za upotrebu, posebno dizajniran i optimizovan za umbrelOS. Kompaktan, tih, povezan putem ethernet kabla, opremljen je NVMe SSD-om (opciono do 4TB), 16GB RAM-a i četvorojezgarnim CPU-om. Naručite ga, priključite i idete na `umbrel.local`. Možete imati operativni Umbrel u funkciji za nekoliko minuta. To je plug-and-play opcija.



![Image](assets/fr/081.webp)





- [**umbrelOS**](https://umbrel.com/umbrelos): ovo je operativni sistem koji možete sami instalirati na svoj hardver (mini-PC, NUC, klasični desktop u velikom kućištu, posvećeni laptop...). Imate isti interfejs i isti App Store kao na Umbrel Home.



![Image](assets/fr/080.webp)



U oba slučaja, korisničko iskustvo je identično sa softverske strane: administracija putem pregledača, ažuriranja jednim klikom, instalacija aplikacija na zahtev... DIY rešenje je često ekonomičnije od kupovine Umbrel Home-a (u zavisnosti od korišćene mašine). Međutim, ne bih nužno preporučio da uvek birate DIY opciju, jer **kupovina Umbrel Home-a direktno doprinosi finansiranju razvoja projekta**, s obzirom da je njegov poslovni model zasnovan na prodaji hardvera. I iskreno, po ceni od 389 € za 2TB skladišta, cena ostaje vrlo razumna s obzirom na kvalitet mašine koja se nudi.



![Image](assets/fr/079.webp)



U sledećem poglavlju, istražićemo kako instalirati umbrelOS DIY na vašoj sopstvenoj mašini. Međutim, možete pratiti ovaj BTC 202 kurs na isti način ako ste se odlučili za Umbrel Home.



### Primena: od Bitcoin čvora do kućnog cloud servera



Umbrel može ostati vrlo minimalistički i fokusiran isključivo na Bitcoin, ili se razviti u pravi multifunkcionalni lični server, u zavisnosti od vaših potreba. Ovde su glavne upotrebe za Umbrel:





- **Jednostavan Bitcoin čvor**: ovo je osnova na kojoj se Umbrel oslanjao od samog početka. Možete pokrenuti Bitcoin Core (ili Knots), direktno povezati svoje novčanike sa svojim čvorom, pokrenuti Electrum server, hostovati svoj Mempool block explorer za pregled blockchaina i procenu naknada... Na ove upotrebe ćemo se fokusirati u ovom kursu.



![Image](assets/fr/082.webp)





- **Lightning Network**: Umbrel vam takođe omogućava da implementirate LND ili Core Lightning, dve implementacije Lightning mreže, kako biste upravljali sopstvenim Lightning čvorom. Moći ćete da otvarate kanale, upravljate svojom likvidnošću, vršite plaćanja, automatizujete balansiranje, nudite usluge, povežete udaljeni novčanik, ili koristiti napredni interfejs za upravljanje zahvaljujući mnogim dostupnim aplikacijama. Ovaj specifičan slučaj upotrebe ćemo razmatrati u našem sledećem LNP 202 kursu.



![Image](assets/fr/083.webp)





- **Opšte samostalno hostovanje**: sa Nextcloud, Immich, Jellyfin/Plex, sistemi za blokiranje reklama na DNS nivou (za celu mrežu) (Pi-hole/AdGuard), VPN-ovima (WireGuard, Tailscale), kućnom automatizacijom (Home Assistant), rezervnim kopijama, upravljanjem beleškama, kancelarijskim alatima, lokalnom veštačkom inteligencijom (Ollama + Open WebUI)... Umbrel može postati vaš lični server, omogućavajući vam da povratite kontrolu nad vašim podacima. Sami pokrećete servise koje koristite svaki dan, sa korisničkim iskustvom sličnim komercijalnim rešenjima, ali uz potpunu kontrolu nad podacima i privatnošću.


Korišćenjem aplikacija u kontejnerima, možete oblikovati Umbrel po želji: počnite sa jednostavnim Bitcoin čvorom i nekoliko aplikacija povezanih sa njegovim ekosistemom, zatim instalirajte Lightning čvor pored vašeg Bitcoin čvora, i postepeno obogatite svoju instancu sa aplikacijama za samostalno hostovanje koje su vam potrebne.



### Zajednica i uzajamna pomoć



Jedna od ključnih prednosti Umbrela u odnosu na konkurenciju je njegova velika i veoma aktivna zajednica korisnika. Možete ih kontaktirati uglavnom putem [njihovog Discorda](https://discord.gg/efNtFzqtdx) i [njihovog online foruma](https://community.umbrel.com/). Ovde ćete pronaći ne samo praktične savete već, pre svega, rešenja za rešavanje problema ili ispravljanje grešaka. To je odlično mesto za početak, napredovanje i, na kraju, pomoć drugim korisnicima, tako da niste sami sa svojim Coin.



![Image](assets/fr/084.webp)



### Licenca za UmbrelOS



Umbrelov kod je javno dostupan (možete ga pregledati, forkovati, i modifikovati), ali nije pod pravom open-source licencom. Zapravo, umbrelOS se distribuira pod [*PolyForm Noncommercial 1.0*] licencom (https://polyformproject.org/licenses/noncommercial/1.0.0/), iako su neki povezani alati za razvoj dostupni pod MIT licencom.



U praktičnom smislu, možete raditi gotovo sve što želite sa umbrelOS, sve dok je to za ličnu, nekomercijalnu upotrebu: modifikacija, redistribucija u neprofitne svrhe, pravljenje prilagođenih verzija za sebe ili za neprofitne organizacije, pod uslovom da poštujete pravne napomene.



Međutim, zabranjeno je prodavati Umbrel ili njegove izvedene verzije (na primer, unapred sastavljenu mašinu sa unapred instaliranim umbrelOS-om), nuditi usluge povezane sa Umbrelom komercijalno, ili integrisati njegov kȏd u proizvod radi profita.



Tehnički, ova licenca ne ograničava instalaciju, reviziju ili prilagođavanje Umbrela za ličnu upotrebu. Pravno, štiti projekat od neovlašćene preprodaje ili komercijalnog hostinga, posebno od strane cloud provajdera. Umbrel stoga nije open source, iako je njegov kod javno dostupan.



Međutim, svaka aplikacija u App Store-u zadržava svoju licencu, često otvorenog koda.




## Instalacija potpunog čvora sa Umbrel-om


<chapterId>61bc09c7-787d-4649-b142-457ec018b0f4</chapterId>



Sada kada imamo sve potrebne informacije, vreme je da se upustimo u detalje. U ovom vodiču pokazaćemo vam kako da instalirate kompletan Bitcoin čvor koristeći UmbrelOS.



### Potrebni materijali



Ovde ćemo koristiti UmbrelOS x86 sliku (tačnije, x86_64 verziju). Moći ćete da pratite ovaj vodič na bilo kojoj mašini koju izaberete, sve dok nije opremljena procesorom ARM arhitekture (bez Apple Silicon, Raspberry Pi, itd.). To znači da će bilo koji računar sa Intel ili AMD 64-bitnim procesorom biti dovoljan, sve dok ispunjava minimalne zahteve, u zavisnosti od toga kako nameravate da koristite svoj Umbrel (preporučuje se barem dvojezgarni procesor).



Ako ste se odlučili za Raspberry Pi 5 (opcija koju ne preporučujem, kao što je pomenuto u prethodnom odeljku), instalacija je malo drugačija. Zatim možete pratiti ovaj posvećeni vodič i vratiti se na moj kurs kada budete na `http://umbrel.local` web interfejsu:



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

Kao što je pomenuto u prethodnom delu, odlučio sam da pokrenem ovaj tutorijal na malom obnovljenom računaru koji sam pronašao po povoljnoj ceni: *Lenovo ThinkCentre M900 Tiny* opremljen Intel Core i7 procesorom i 16 GB RAM-a. Ovo je veoma udobna konfiguracija za pokretanje Umbrel-a, posebno za Bitcoin čvor. Međutim, izabrao sam ovu konfiguraciju jer želim da instaliram Lightning čvor i druge zahtevnije aplikacije kasnije. Takođe sam dodao 2TB SSD svom ThinkCentre-u kako bih zadržao puni blockchain i i dalje imao solidnu rezervu prostora. Sa ovom konfiguracijom, ukupni trošak je 270 €, uključujući sve troškove.



![Image](assets/fr/001.webp)



Posebno mi se sviđa Lenovo ThinkCentre Tiny serija, jer su to kompaktne, tihe i veoma robusne mašine. Ovi računari su veoma popularni među preduzećima i stoga su brojni na tržištu polovnih uređaja, gde možete pronaći zanimljive konfiguracije između €70 i €200.



Ako ste, poput mene, odabrali PC bez monitora, **trebaće vam da povežete monitor i tastaturu** samo tokom trajanja instalacije. Nakon toga, moći ćete da mu pristupite daljinski sa drugog računara na istoj mreži (ili putem drugih metoda koje ćemo pokriti u kasnijim poglavljima). Takođe će vam biti potreban RJ45 Ethernet kabl da povežete vaš uređaj na lokalnu mrežu, i USB priključak od najmanje 4 GB za čuvanje instalacione slike.



Da rezimiramo, ovde su zahtevi za opremu:




- Računar sa x86_64 procesorom (minimalno dvojezgarni, preporučeno četvorojezgarni);
- RAM memorija (minimum 4 GB, preporučeno 8 GB ili više za produženu upotrebu);
- SSD (preporučeno + 2 TB);
- USB ključ (+ 4 GB) za instalaciju UmbrelOS slike;
- Monitor i tastatura (korisno samo za početnu instalaciju ako računar nije opremljen jednim);
- RJ45 Ethernet kabl.



### Korak 1 - Montiranje računara



U zavisnosti od hardvera koji ste odabrali, prvi korak je sastavljanje različitih komponenti vašeg računara. Na primer, u mom slučaju, originalni SSD je imao kapacitet od samo 256 GB, pa ću ga reciklirati za drugu upotrebu i zameniti sa SSD-om od 2 TB. Ako takođe želite da zamenite RAM module, sada je vreme da to uradite.



### Korak 2: Pripremite USB ključ za pokretanje



Pre nego što instalirate UmbrelOS na vaš uređaj, potrebno je da napravite USB ključ sa kojeg se može pokrenuti operativni sistem. Svi koraci u koraku 2 moraju biti izvedeni na vašem ličnom računaru (a ne direktno na računaru koji će postati vaš čvor).





- Najpre preuzmite najnoviju verziju UmbrelOS-a kao USB sliku:



Idite na [zvaničnu Umbrel veb stranicu da preuzmete ISO sliku](https://download.umbrel.com/release/latest/umbrelos-amd64-usb-installer.iso) za instalaciju putem USB ključa. Uverite se da ste izabrali verziju kompatibilnu sa x86_64 arhitekturom (datoteka nazvana `umbrelos-amd64-usb-installer.iso`). Preuzimanje može potrajati, jer je slika prilično velika.



![Image](assets/fr/002.webp)





- Instalirajte Balena Etcher:



Za kreiranje USB uređaja za pokretanje sistema (eng. bootable USB), koristićete jednostavan alat koji radi na više platformi, pod nazivom [Balena Etcher](https://www.balena.io/etcher/). Preuzmite ga i instalirajte na vašem računaru.



![Image](assets/fr/003.webp)





- Umetnite prazan USB ključ od najmanje 4 GB:



Priključite USB ključ u svoj računar (onaj na koji ste upravo preuzeli UmbrelOS i Balena Etcher sliku). **Upozorenje: svi podaci na ključu će biti obrisani**. Uverite se da ne sadrži važne fajlove.





- Prebacite (upišite) ISO sliku na USB stik pomoću alata Balena Etcher.



Pokrenite Balena Etcher i izaberite ISO datoteku `umbrelos-amd64-usb-installer.iso` koju ste upravo preuzeli klikom na dugme "*Flash from file*". Zatim, izaberite USB ključ kao ciljni uređaj i kliknite na "*Flash!*" da započnete pisanje.



![Image](assets/fr/004.webp)



Kada se postupak završi, imaćete butabilni USB uređaj sa UmbrelOS-om, spreman za pokretanje i instalaciju Umbrela na vaš računar.



![Image](assets/fr/005.webp)



### Korak 3: Pokretanje računara sa USB ključa



Sada kada je vaš USB stik sa UmbrelOS-om spreman, možete pokrenuti računar sa njega kako biste započeli instalaciju sistema. Isključite USB ključ iz vašeg glavnog računara i umetnite ga u uređaj na koji želite instalirati Umbrel i vaš Bitcoin čvor.



Kao što je objašnjeno na početku ovog poglavlja, za dovršetak instalacije biće vam potreban uređaj za prikaz i uređaj za unos. Povežite uređaj za prikaz putem HDMI (ili drugog porta, u zavisnosti od vašeg računara) i povežite tastaturu putem USB-a sa vašom mašinom. Ovi uređaji su potrebni samo za instalaciju; neće vam biti potrebni kasnije, jer će se Umbrel pristupati daljinski sa drugog računara. Povežite ova dva uređaja sa vašim računarom.



**Savet:** Ako kod kuće nemate periferni ekran, možete koristiti svoj TV. Sa svojim HDMI (ili drugim) ulazom, može se koristiti kao privremeni ekran dok instalirate operativni sistem.



Umbrel očigledno zahteva internet konekciju. Povežite RJ45 Ethernet kabl između vašeg uređaja i vašeg rutera.



![Image](assets/fr/006.webp)



Uključite svoju mašinu. U većini slučajeva, ona bi automatski trebalo da detektuje USB ključ i pokrene se sa njega. Zatim će se pojaviti instalacioni ekran UmbrelOS-a.



Ako se uređaj pokrene na drugom sistemu ili prikaže poruku o grešci, to verovatno znači da se ne pokreće automatski sa USB ključa. U tom slučaju, ponovo pokrenite uređaj i uđite u BIOS/UEFI podešavanja (obično se pristupa pritiskom na `DEL`, `F2`, `F12`, ili `ESC`, u zavisnosti od proizvođača računara). Zatim promenite redosled pokretanja kako biste dali prioritet USB ključu. Potom ponovo pokrenite uređaj da biste pokrenuli UmbrelOS.



### Korak 4: Instalirajte UmbrelOS na vaš računar



Kada se uređaj pokrene sa USB memorije, dočekaće vas instalacioni ekran UmbrelOS-a. Ovaj korak podrazumeva instaliranje sistema direktno na interni hard disk vaše mašine.



Ekran koji se pojavljuje prikazuje sve interne uređaje za skladištenje koje je računar detektovao. Svaki disk je praćen brojem, imenom i kapacitetom skladištenja. Pronađite disk na koji želite instalirati Umbrel. **Upozorenje: svi fajlovi na ovom disku će biti trajno obrisani.**



![Image](assets/fr/007.webp)



Jednom kada identifikujete ispravan disk (obično onaj sa najvećim kapacitetom, da smestite blockchain), zabeležite broj koji mu je dodeljen. Na primer, ako se disk koji ste odabrali pojavljuje pod brojem `2`, jednostavno unesite `2`, zatim pritisnite taster `Enter` na tastaturi.



![Image](assets/fr/008.webp)



Program će formatirati izabrani disk, instalirati UmbrelOS i automatski konfigurisati sistem. Ovo može potrajati nekoliko minuta. Pustite proces da teče bez prekida.



![Image](assets/fr/009.webp)



Kada je instalacija završena, bićete upitani da isključite uređaj. Pritisnite bilo koji taster da isključite računar.



![Image](assets/fr/010.webp)



Sada možete ukloniti USB ključ, tastaturu i ekran, koji više nisu potrebni za vaš Umbrel. Sve što ostaje od vašeg čvora je napajanje i RJ45 Ethernet kabl.



![Image](assets/fr/011.webp)



Pre nego što ponovo pokrenete uređaj, proverite sledeće dve tačke:





- **USB ključ je isključen**: ako ostane povezan, sistem se može ponovo pokrenuti na njemu umesto na internom disku;
- **Ethernet kabl je priključen**: uređaj mora biti povezan sa vašim ruterom da bi radio.



Pritisnite dugme za napajanje. Sistem se automatski pokreće sa internog diska gde je UmbrelOS instaliran. Prvo pokretanje može trajati približno **5 minuta**. Tokom ovog vremena, Umbrel inicijalizuje svoje servise i interfejs.



Sa drugog računara (vaš svakodnevni PC) povezanog na **istu lokalnu mrežu**, otvorite web pregledač (Firefox, Chrome...) i idite na:



```
http://umbrel.local
```



Ova adresa se koristi za pristup Umbrel grafičkom korisničkom interfejsu na daljinu i započinjanje konfiguracije.



Ako `http://umbrel.local` adresa ne radi na vašem pregledaču nakon čekanja od najmanje 5 minuta, jednostavno pokušajte:



```
http://umbrel
```



Ako ovo i dalje ne radi, unesite lokalnu IP adresu vašeg Umbrela direktno u pregledač. Na primer (zamenite `42` brojem vaše mašine koja hostuje Umbrel na lokalnoj mreži):



```
http://192.168.1.42
```



Da biste identifikovali IP adresu vašeg Umbrel-a, postoji nekoliko metoda, od najjednostavnijih do najnaprednijih:





- Pristupite administrativnom interfejsu rutera i pronađite IP adresu Umbrel uređaja na lokalnoj mreži.





- Koristite softver za skeniranje mreže kao što je Angry IP Scanner da biste otkrili povezane uređaje i locirali IP adresu vašeg Umbrela.



![Image](assets/fr/012.webp)



https://planb.academy/tutorials/computer-security/communication/angry-ip-scanner-47f7c943-53b7-4098-b167-4cec8e747b5d



- Kao poslednje rešenje, ponovo povežite monitor i tastaturu na uređaj, prijavite se (podrazumevani login: `umbrel`, lozinka: `umbrel`), zatim unesite sledeću komandu:



```
hostname -I
```



Sada ste spremni da koristite Umbrel!



### Korak 5: Početak rada sa Umbrelom



Da biste započeli konfiguraciju svog Umbrela, kliknite na dugme "*Start*".



![Image](assets/fr/013.webp)



#### Kreiraj nalog



Izaberite pseudonim ili unesite svoje ime, zatim postavite jaku lozinku. Budite pažljivi: ova lozinka je jedina barijera koja štiti pristup vašem Umbrelu sa vaše mreže (i stoga, potencijalno, vašim bitkoinima ako pokrećete Lightning čvor na Umbrelu). Takođe štiti daljinski pristup putem Tor-a ili VPN-a, ako su ove usluge omogućene.



Izaberite jaku lozinku i obavezno sačuvajte barem jednu rezervnu kopiju (preporučuje se menadžer lozinki).



https://planb.academy/tutorials/computer-security/authentication/bitwarden-0532f569-fb00-4fad-acba-2fcb1bf05de9

https://planb.academy/tutorials/computer-security/authentication/keepass-f8073bb7-5b4a-4664-9246-228e307be246

Kada unesete svoju lozinku, kliknite na dugme "*Create*".



![Image](assets/fr/014.webp)



Vaša Umbrel konfiguracija je sada završena.



![Image](assets/fr/015.webp)



#### Upoznavanje sa interfejsom UmbrelOS-a



Umbrelov interfejs je prilično intuitivan:





- Na početnoj stranici možete videti vaše instalirane aplikacije i widgete.



![Image](assets/fr/016.webp)





- "*App Store*" vam omogućava instaliranje novih aplikacija,



![Image](assets/fr/017.webp)





- Meni "*Files*" centralizuje sva dokumenta sačuvane na vašem Umbrelu.



![Image](assets/fr/018.webp)





- Meni "*Settings*" vam omogućava da izmenite postavke vašeg Umbrela i pristupite njegovim informacijama, uključujući:
    - Ažuriraranje, ponovo pokretanje ili zaustavljanje mašine;
    - Proveru dostupnog prostora za skladištenje, korišćenje RAM-a i temperature procesora;
    - Promenu pozadine;
    - Upravljanje daljinskim pristupom putem Tor-a, aktiviranje Wi-Fi ili 2FA.



![Image](assets/fr/019.webp)



#### Bezbednosna i mrežna podešavanja



Prvo i najvažnije, toplo preporučujem omogućavanje dvofaktorske autentifikacije (2FA). Ovo dodaje dodatni sloj sigurnosti vašoj lozinki. Gotovo je neophodno ako planirate koristiti svoj Umbrel za čuvanje ličnih fajlova, pokretanje Lightning čvora ili obavljanje bilo koje druge osetljive aktivnosti.



https://planb.academy/tutorials/computer-security/authentication/authy-a76ab26b-71b0-473c-aa7c-c49153705eb7

Da biste to uradili, kliknite na odgovarajuće polje u podešavanjima.



![Image](assets/fr/020.webp)



Zatim skenirajte prikazani QR kod koristeći vašu aplikaciju za autentifikaciju. Zatim unesite 6-cifreni dinamički kod u predviđeno polje na vašem Umbrel-u.



Od sada će svaka nova veza na vaš Umbrel zahtevati i lozinku i 6-cifreni kod generisan od strane vaše aplikacije za dvofaktorsku autentifikaciju (2FA).



![Image](assets/fr/021.webp)



Što se tiče daljinskog pristupa putem Tor-a, ako vam nije potreban, preporučujem da ovu opciju ostavite onemogućenu kako biste ograničili površinu napada na vaš Umbrel. Podrazumevano, vaš čvor može biti pristupljen samo sa mašine povezane na istu lokalnu mrežu. Omogućavanje pristupa putem Tor-a će vam ipak omogućiti da upravljate vašim Umbrel-om u pokretu.



Ako omogućite ovu funkciju, teoretski postaje moguće da bilo koja mašina na svetu pokuša da se poveže sa vašim čvorom, pod uslovom da zna Tor adresu. Međutim, vaša lozinka i 2FA će vas i dalje štititi.



Ako aktivirate ovu opciju, osigurajte da imate omogućenu dvofaktorsku autentifikaciju (2FA), jaku lozinku i nikada ne otkrivajte vašu Tor adresu za povezivanje.



Jednostavno unesite ovu Tor adresu u vaš Tor pregledač da biste pristupili Umbrelovom interfejsu sa bilo koje mreže.



![Image](assets/fr/026.webp)



Konačno, na ovoj stranici sa podešavanjima, možete takođe aktivirati Wi-Fi konekciju. Ako vaša mašina koja hostuje Umbrel ima Wi-Fi mrežnu karticu ili Wi-Fi adapter, ovo vam omogućava pristup internetu bez korišćenja RJ45 kabla. Međutim, u zavisnosti od vaše konfiguracije, ovo rešenje može usporiti konekciju, što može uticati na inicijalnu sinhronizaciju (IBD) i buduće korišćenje čvora (npr. za Lightning transakcije). Lično, ne preporučujem ovu opciju, jer čvor nije namenjen za mobilnu upotrebu: uvek mu se pristupa na daljinu, pa ga možete ostaviti priključenim.



### Korak 6: Instalirajte Bitcoin čvor na Umbrel



Sada kada je UmbrelOS ispravno instaliran i konfigurisan na vašem uređaju, možete nastaviti sa instalacijom vašeg Bitcoin čvora. Ništa lakše: idite u App Store, otvorite kategoriju "*Bitcoin*", zatim izaberite aplikaciju "*Bitcoin Node*" (zapravo je Bitcoin Core).



![Image](assets/fr/022.webp)



Zatim kliknite na dugme "*Install*".



![Image](assets/fr/023.webp)



Kada je instalacija završena, vaš Bitcoin čvor će pokrenuti svoj IBD (*Initial Block Download*): preuzeće i validirati sve transakcije i blokove od kada je Bitcoin kreiran 2009. godine.



![Image](assets/fr/024.webp)



Ova faza je posebno vremenski zahtevna, jer njeno trajanje zavisi od nekoliko faktora, uključujući količinu RAM-a koja je dodeljena kešu čvora, brzinu diska, brzinu internet konekcije i snagu procesora. Opseg trajanja je stoga veoma širok, u zavisnosti od konfiguracije. Sa visokoperformansnim računarom (NVMe SSD, +32 GB RAM, snažan procesor i dobra internet konekcija), IBD se može završiti za oko deset sati. S druge strane, stari procesor, mala količina RAM-a ili, još gore, mehanički hard disk (strogo se ne preporučuje) mogu produžiti ovu operaciju na nekoliko nedelja.



Sa PC-jem normalne konfiguracije (pristojan procesor, 8 do 16 GB RAM-a i SSD), moguće je za oko 2 do 7 dana.



Da biste malo ubrzali IBD, možete povećati RAM dodeljen kešu čvora (koji se prvenstveno koristi za UTXO set, koji ćemo kasnije ponovo razmotriti na kursu) putem `dbcache` parametra. Na Umbrel-u, ova izmena se vrši u parametrima vašeg čvora, u kartici "*Optimization*".



![Image](assets/fr/025.webp)



Podrazumevano, vrednost parametra `dbcache` u Bitcoin Core-u je postavljena na 450 MiB, ili oko 472 MB. Povećanjem ove vrednosti, možete blago ubrzati IBD. Međutim, ne bih nužno preporučio da ovaj parametar postavite previše visoko: čak i postavljanje na 4 GiB će samo učiniti sinhronizaciju oko 10% bržom, i može uzrokovati gubitak vremena u slučaju prekida tokom IBD.



Budite oprezni da ne dodelite vrednost koja je prevelika za vašu mašinu. Ako ponestane RAM dostupan za UmbrelOS, vaš čvor može naglo prestati sa radom, prekidajući IBD i zahtevajući da ga ručno ponovo pokrenete, što može rezultirati značajnim gubitkom vremena.



Da biste saznali više o uticaju parametra `dbcache` na početnu sinhronizaciju, preporučujem ovu analizu Jamesona Loppa: [*Effects of DBcache Size on Bitcoin Node Sync Speed*](https://blog.lopp.net/effects-dbcache-size-Bitcoin-node-sync-speed/)



Kada je IBD vašeg čvora završen (100% sinhronizacija), sada imate potpuno operativan Bitcoin čvor. Čestitamo, sada ste integralni deo Bitcoin mreže!



![Image](assets/fr/027.webp)



U sledećem delu, istražićemo praktičnu upotrebu vašeg novog čvora: kako povezati vaš novčanik sa njim i koje aplikacije treba da instalirate da biste postali suvereni Bitcoiner.





# Povezivanje vašeg novčanika sa vašim čvorom


<partId>418d0afd-3a61-4b5a-9db4-203c0335fd29</partId>



## Indekseri: uloga, rad i rešenja


<chapterId>4f93c07a-f0cb-435f-8b68-162f316d7039</chapterId>



Ako ste već istraživali Bitcoin čvorove pre nego što ste pohađali ovaj kurs, možda ste naišli na termin "indekser". To su alati kao što su Electrs ili Fulcrum, koji se mogu dodati na Bitcoin Core čvor. Ali koja je tačno njihova uloga? Kako funkcionišu u praksi? I da li bi trebalo da instalirate jedan na vaš novi Bitcoin čvor? To je ono što ćemo istražiti u ovom poglavlju.



### Šta je indeksator?



Generalno govoreći, indeksator je program koji skenira skup sirovih podataka, izdvaja relevantne ključeve (kao što su reči, identifikatori i adrese), i gradi pomoćnu datoteku, nazvanu "indeks", gde se svaki ključ odnosi na tačnu lokaciju podataka u korpusu. Ova faza predobrade koristi CPU vreme i zahteva određeni prostor na disku, ali eliminiše potrebu za obradom celog korpusa svaki put kada se baza podataka pretražuje; jednostavno ispitivanje indeksa daje gotovo trenutni odgovor.



U laičkim terminima, to je isti princip kao indeks u knjizi: ako tražite određenu informaciju, umesto da ponovo čitate celu knjigu, konsultujete indeks da direktno pronađete stranicu na kojoj se pojavljuje informacija koju tražite.



U Bitcoin čvoru, kao što je Bitcoin Core, blockchain podaci se čuvaju u svom sirovom, hronološkom obliku. Svaki blok sadrži transakcije, koje zauzvrat sadrže ulaze i izlaze, bez ikakve posebne klasifikacije po adresi, identifikatoru, ili novčaniku. Ova linearna organizacija je optimizovana za validaciju blokova, ali nije pogodna za ciljane pretrage. Na primer, ako želite pronaći sve transakcije povezane sa određenom adresom u neindeksiranom čvoru, morali biste ručno pregledati ceo blockchain, blok po blok i transakciju po transakciju. Upravo tu dolazi indeksator na vašem Bitcoin čvoru.



![Image](assets/fr/085.webp)



Indekser je specijalizovani softverski program koji analizira ovu masu sirovih podataka (Blockchain, Mempool, UTXO set) i izvlači ključeve, kao što su identifikatori transakcija, adrese i visine blokova. Iz ovih ključeva, on gradi svoj indeks, povezujući svaki ključ sa tačnom lokacijom informacija u skladištu čvora.



![Image](assets/fr/086.webp)



Indeksiranje vam omogućava da brzo, precizno i efikasno pretražujete informacije na vašem čvoru. Na primer, kada povežete novčanik kao što je Sparrow sa vašim čvorom, može gotovo trenutno prikazati stanje adresa. Konkretno, postavljanje upita indeksatoru sa zahtevom kao što je: "_Koji UTXO-ovi su povezani sa ovim script-hash-om?_" Indeksator odgovara gotovo odmah, bez potrebe da ponovo čita ceo blockchain, jer su ovi podaci već navedeni u njegovoj bazi podataka.



### Da li Bitcoin Core ima indeksator?



Bez dodavanja dodatnog softvera, Bitcoin Core, strogo govoreći, ne nudi kompletan indeksator adresa uporediv sa onima koji se nalaze u softverima kao što su Electrs ili Fulcrum. Ipak, on uključuje nekoliko internih mehanizama za indeksiranje, kao i opcione opcije za proširenje svojih mogućnosti upita. Da bismo u potpunosti shvatili situaciju, potrebno je da se nakratko osvrnemo na istoriju projekta.



Do verzije Bitcoin Core 0.8.0, validacija transakcija se zasnivala na globalnom indeksu transakcija, poznatom kao `txindex`. Ovaj indeks je referencirao sve blockchain transakcije i njihove izlaze. Kada bi čvor primio novu transakciju, konsultovao bi ovaj indeks da verifikuje da li iskorišćeni izlazi (u ulazima) zaista postoje i da nisu već potrošeni. `txindex` je stoga bio neophodan za validaciju transakcija u to vreme.



Međutim, ovaj pristup imao je svoja ograničenja: bio je spor, skup u pogledu skladištenja i suvišan u pogledu informacija. Da bi se to rešilo, verzija 0.8.0 uvodi prepravku modela validacije pod nazivom ***Ultraprune***. Umesto da skladišti sve u obliku indeksa transakcija, Bitcoin Core održava jednostavnu bazu podataka posvećenu isključivo UTXO-ima, nazvanu `chainstate` (u svakodnevnom jeziku, ovo je poznato kao "UTXO set"), i ažurira svoju listu kako se izlazi troše i kreiraju.



Ova metoda je mnogo brža i čuva samo trenutno stanje registra, čineći `txindex` indeksator nepotrebnim. Međutim, umesto brisanja `txindex` koda, programeri su odlučili da zadrže ovu funkcionalnost iza jednostavnog parametra (`txindex=1`). Omogućavanjem ove opcije na svom čvoru, možete pretraživati bilo koju transakciju po njenom `txid`.



Suprotno uvreženom mišljenju, Bitcoin Core ne nudi indeksiranje zasnovano na adresama kao što to čine Electrs ili Fulcrum. Postoji nekoliko razloga za ovaj izbor:





- Uloga Bitcoin Core-a nije da postane potpuni Block explorer, niti da obezbedi API prilagođen svakoj upotrebi. Dodavanje indeksa po adresama zahtevalo bi dugoročno održavanje, što izlazi iz okvira prvobitnog dizajna softvera.





- Većina slučajeva upotrebe može se već pokriti na druge načine. Na primer, da biste procenili stanje neke adrese, možete koristiti komandu `scantxoutset`, koja direktno ispituje UTXO skup bez potrebe za punim indeksom.





- Svaki softverski program ima specifične zahteve u vezi sa formatom ili tipom podataka koji treba indeksirati (adresa, hash skripta, vlasnički tag, itd.). Fleksibilnije je i logičnije dozvoliti tim programima da izgrade sopstvene prilagođene indekse nego primeniti generičko rešenje u Bitcoin Core-u.



Bitcoin Core ima opcioni indeksator transakcija (`txindex`), ostatak iz njegove istorijske operacije, ali ne pruža indeks adresa, niti direktan interfejs za složene pretrage. U nekim slučajevima, stoga, može biti korisno dodati eksterni indeksator.



### Da li treba da dodate indeksator adresa na vaš čvor?



Dodavanje indeksatora adresa, kao što su Electrs ili Fulcrum, nije obavezno; zavisi od vaših specifičnih potreba.



Ako jednostavno želite da povežete novčanik, kao što je Sparrow, sa svojim čvorom da biste pregledali stanja i emitovali transakcije, ovo je potpuno moguće direktno putem RPC interfejsa Bitcoin Core-a, bilo lokalno ili na daljinu putem Tor-a.



S druge strane, za korišćenje naprednijeg softvera, kao što je lokalno mempool.space pokretanje, instalacija indeksatora adresa postaje neophodna za block explorer.



Indekser zahteva određeno vreme za sinhronizaciju (manje od IBD) i zauzeće dodatni prostor na disku. Ako vaš SSD i dalje ima dovoljno slobodnog prostora nakon preuzimanja blockchaina, možete lako dodati indekser.



### Koji indeksator odabrati?



Dva softverska programa se obično koriste za izradu ove vrste indeksa adresa i omogućavanje pristupa: **Electrs** i **Fulcrum**. Ovi alati indeksiraju blockchain prema script-hash-u (adresama) i zatim predlažu standardizovani interfejs (Electrum protokol), na koji se povezuje mnoštvo novčanika, kao što su Electrum Wallet, Sparrow, ili Phoenix.



![Image](assets/fr/087.webp)



Jednostavno rečeno, Electrs je prilično kompaktan: indeksira blockchain brže i zauzima manje prostora na disku, ali ima nešto slabije performanse u upitima u poređenju sa Fulcrumom. Nasuprot tome, Fulcrum troši više prostora na disku i duže traje indeksiranje, ali nudi superiorne performanse upita.



Za individualnu upotrebu, preporučujem Electrs: zauzima manje prostora, dobro je održavan, i, iako je malo sporiji kod određenih zahteva u poređenju sa Fulcrumom, i dalje je više nego dovoljan za svakodnevnu upotrebu. Ako imate vremena i prostora na disku, možete isprobati i Fulcrum, koji će raditi značajno bolje, posebno na novčanicima sa brojnim adresama za verifikaciju.



U konkretnim terminima, u avgustu 2025. godine, Electrs će zahtevati približno 56 GB skladišta, u poređenju sa približno 178 GB za Fulcrum. Vaš izbor indeksatora, dakle, takođe zavisi od vašeg kapaciteta skladišta:




- Ako vam je prostor na disku veoma ograničen, moraćete da se snađete sa Bitcoin Core bez spoljnog indeksatora adresa.
- Ako želite da koristite indeksator, ali ste i dalje ograničeni kapacitetom, odlučite se za Electrs.
- Ako imate dovoljno prostora na disku, Fulcrum može biti upravo ono što tražite.



Za ostatak ovog BTC 202 kursa, koristiću Electrs, ali možete lako pratiti sa Fulcrum: postupak instalacije je isti, kao i način povezivanja interfejsa sa novčanikom, jer oba koriste Electrum server.



### Kako da instaliram indeksator na Umbrel?



Da biste instalirali Electrs (ili Fulcrum) na vaš Umbrel, postupak je jednostavan: idite u App Store, potražite odgovarajuću aplikaciju (nalazi se na kartici Bitcoin), a zatim kliknite na dugme "*Install*".



![Image](assets/fr/028.webp)



Kada je instalacija završena, Electrs će nastaviti sa fazom sinhronizacije (indeksiranja), koja može potrajati nekoliko sati.



![Image](assets/fr/029.webp)



Kada je sinhronizacija završena, možete povezati svoj softver za upravljanje novčanikom sa vašim Electrum serverom, koji je hostovan na Umbrel-u.



## Kako da povežem svoj novčanik sa svojim Bitcoin čvorom?


<chapterId>35519b1a-f681-4a69-a652-9fbe510cd17f</chapterId>



Sada kada imate kompletan Bitcoin čvor, vreme je da ga iskoristite na pravi način! U sledećem poglavlju, istražićemo druge potencijalne upotrebe za vašu Umbrel instancu. Međutim, počnimo sa osnovama: povezivanje vašeg softvera za upravljanje novčanikom kako biste koristili informacije sa vašeg sopstvenog blockchaina i distribuirali transakcije kroz vaš sopstveni čvor.



Kao što je gore pomenuto, postoje dva glavna interfejsa za povezivanje:




- Direktna veza sa Bitcoin Core-om preko RPC;
- Ili se povežite na Electrum server (Electrs ili Fulcrum).



U ovom vodiču, fokusiraćemo se na povezivanje sa vašim čvorom putem Tor-a, jer je ovo jednostavno i sigurno rešenje za početnike. Snažno savetujem protiv izlaganja RPC porta vašeg čvora u otvorenom obliku (clear net), jer pogrešna konfiguracija predstavlja značajan rizik za sigurnost i poverljivost vaših podataka. Glavni nedostatak komunikacije putem Tor-a je njegova sporost. U sledećem poglavlju, istražićemo brzu i sigurnu alternativu za Tor za daljinski pristup vašem čvoru: VPN.



Koristićemo Sparrow kao primer u ovom poglavlju, ali procedura je ista za sav ostali softver za upravljanje novčanikom koji prihvata veze sa Electrum serverima. Jednostavno pronađite odgovarajuće podešavanje u parametrima vaše aplikacije (obično u "*Server*", "*Network*", "*Node*"...).



Na Sparrow, otvorite karticu "*File*" i idite na meni "Settings".



![Image](assets/fr/030.webp)



Zatim kliknite na "*Server*" da pristupite parametrima veze.



![Image](assets/fr/031.webp)



Zatim ćete videti tri opcije za povezivanje vašeg softvera sa Bitcoin čvorom:




- *Public server* (žuto): po podrazumevanoj postavci, ako ne posedujete Bitcoin čvor, ova opcija vas povezuje sa javnim čvorom koji ne posedujete (obično kompanijskim). Ova opcija nije relevantna ovde, jer imate svoj čvor na Umbrelu.
- *Bitcoin core* (zeleno): ova opcija odgovara povezivanju putem RPC interfejsa, tj. direktno na Bitcoin core.
- *Private Electrum* (plavo): ova opcija vam omogućava povezivanje putem Electrum Server interfejsa vašeg indeksatora (Electrs ili Fulcrum).



### Povezivanje sa Bitcoin Core RPC interfejsom



Ako vaš Umbrel čvor nema indeksator, ovo je opcija koju treba da odaberete. Na Sparrow-u, kliknite na "*Bitcoin core*".



![Image](assets/fr/032.webp)



Trebaće da unesete nekoliko informacija kako biste uspostavili vezu sa vašim čvorom. Svim ovim podacima može se pristupiti iz aplikacije "*Bitcoin Node*" na Umbrel-u klikom na dugme "*Connect*" u gornjem desnom uglu grafičkog interfejsa.



![Image](assets/fr/033.webp)



Kartica "*RPC Details*" prikazuje sve potrebne informacije za povezivanje. Izaberite povezivanje putem Tor adrese (u `.onion`).



![Image](assets/fr/034.webp)



Unesite ove podatke u odgovarajuća polja na Sparrow novčaniku, zatim kliknite na dugme "*Test Connection*".



![Image](assets/fr/035.webp)



Ako je veza uspešna, pojaviće se zelena oznaka i poruka o potvrdi.



![Image](assets/fr/036.webp)



Kvačica u donjem desnom uglu interfejsa Sparrow novčanika sada će biti zelena (što označava direktnu vezu sa Bitcoin Core-om).


**Napomena:** Da bi veza bila uspešna, vaš čvor mora biti 100% sinhronizovan. Ako to nije slučaj, molimo vas da sačekate do kraja IBD-a.



### Povezivanje na Electrs



Ako vaš čvor ima indeksator, bolje je povezati se s njim nego koristiti Bitcoin Core direktno, jer će vaši upiti biti obrađeni brže.



Na Sparrow-u, idite na karticu "*Private Electrum*".



![Image](assets/fr/037.webp)



Zatim ćete morati uneti nekoliko informacija kako biste uspostavili vezu sa vašim indeksatorom. Ove podatke ćete pronaći u aplikaciji "*Electrs*" (ili, gde je primenljivo, "*Fulcrum*") na Umbrel-u.



Odaberite karticu "*Tor*" da biste dobili `.onion` adresu. Ako želite da povežete mobilni novčanik, možete direktno skenirati QR kod.



![Image](assets/fr/038.webp)



Jednostavno unesite Tor adresu vašeg Electrum servera u polje "*URL*", zatim kliknite na dugme "*Test Connection*".



![Image](assets/fr/039.webp)



Ako je veza uspešna, biće prikazana oznaka za potvrdu i poruka o potvrdi.



![Image](assets/fr/040.webp)



Oznaka u donjem desnom uglu grafičkog interfejsa Sparrow novčanika će postati plava (boja povezana sa povezivanjem na Electrum server).



**Napomena:** Da bi veza funkcionisala, vaš indeksator mora biti 100% sinhronizovan. Ako to nije slučaj, sačekajte da se proces indeksiranja završi.



Sada znate kako da povežete svoj novčanik sa svojim Bitcoin čvorom! U sledećem poglavlju, predstaviću vam nekoliko dodatnih aplikacija dostupnih na Umbrel-u koje su mi posebno drage, a koje će vam omogućiti da unapredite svakodnevno korišćenje Bitcoina preko vašeg čvora.




## Pregled dostupnih aplikacija


<chapterId>2a5ccfbe-0b17-44c9-863c-b7e8cb4b4594</chapterId>



Umbrel nudi opsežnu prodavnicu aplikacija. Kao što ćete videti, postoji mnogo alata povezanih sa Bitcoinom, ali i širok spektar aplikacija u veoma različitim oblastima: rešenja za samostalno hostovanje servisa i fajlova, aplikacije za produktivnost, opštiji finansijski alati, upravljanje medijima, bezbednost i administracija mreže, razvoj softvera, veštačka inteligencija, društvene mreže, pa čak i automatizacija doma.



U ovom kursu BTC 202, fokusiraćemo se isključivo na aplikacije povezane sa Bitcoinom. Međutim, slobodno istražite ostatak kataloga za alate koji vam mogu biti od koristi.



Naravno, bilo bi nemoguće navesti sve Bitcoin aplikacije ovde. U ovom poglavlju, želeo bih da vas upoznam sa osnovnim alatima koji će olakšati i obogatiti vašu svakodnevnu upotrebu Bitcoina.



### Mempool.space



U svakodnevnoj upotrebi Bitcoina, ako postoji jedan alat koji je zaista nezamenljiv, to je block explorer. Bilo da je dostupan online ili instaliran lokalno, on transformiše sirove blockchain podatke u strukturiran, jasan i lako čitljiv format. Takođe poseduje pretraživač koji omogućava korisnicima da brzo pronađu određeni blok, transakciju ili adresu.



U konkretnim terminima, istraživač vam omogućava da procenite naknade potrebne za uključivanje vaše transakcije u blok, zatim pratite njen napredak: saznajte da li će verovatno biti uključena u bliskoj budućnosti, u zavisnosti od tržišta naknada, i konačno potvrdite da je zaista uključena u blok. Takođe nudi mogućnost analize vaših prošlih transakcija i konsultovanja njihove istorije. Ukratko, to je švajcarski nož za bitkoinere.



Kao što je ranije pomenuto, istraživač blokova (eng. explorer) može biti hostovan online na vebsajtu ili pokrenut lokalno na vašem računaru. Glavni nedostatak online usluga je što mogu ugroziti vašu privatnost. Bez VPN-a ili Tor-a, server koji hostuje explorer može povezati vašu IP adresu sa transakcijama koje pregledate, što može pružiti idealnu ulaznu tačku za analizu lanca.



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Štaviše, vaš Internet provajder (ISP) može znati da pregledate određenu transakciju putem block explorer sajta. Ovo takođe postavlja pitanje poverenja: morate se osloniti na onlajn servis da vam pruži tačne informacije o vašim transakcijama, bez mogućnosti da sami proverite njihovu istinitost.



Zato je uvek najbolje koristiti svoj lokalni block explorer. Na ovaj način, nijedan podatak vezan za vašu pretragu neće procuriti, jer se svi upiti obrađuju direktno na mašini koju kontrolišete, bez prolaska kroz internet. Štaviše, lokalni istraživač blokova se oslanja na podatke sa vašeg sopstvenog Bitcoin čvora, koji ste sami validirali, prema sopstvenim pravilima, i kojem možete verovati.



Umbrel nudi nekoliko istraživača blokova:




- Mempool.Space
- Bitfeed
- BTC RPC Explorer



Posebno mi se sviđa Mempool.Space, koji sam instalirao na svom čvoru. Imajte na umu: za korišćenje većine blok istraživača na Umbrel-u, potreban je indeksator adresa. Stoga vam je potrebna aplikacija Bitcoin Node (ili Bitcoin Knots), koja ima 100% sinhronizovan blockchain, kao i indeksator kao što su Electrs ili Fulcrum, koji je takođe 100% sinhronizovan.



Jednom kada je aplikacija instalirana, jednostavno je otvorite da biste pristupili svom istraživaču.



![Image](assets/fr/041.webp)



Da biste saznali više o korišćenju Mempool.Space explorera, preporučujem ovaj sveobuhvatan vodič:



https://planb.academy/tutorials/privacy/explorer/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f

### Lightning čvor



Sada kada imate svoj Bitcoin čvor, možete postaviti i svoj Lightning čvor za obavljanje [off-chain](https://planb.academy/resources/glossary/offchain) transakcija, bez oslanjanja na infrastrukturu treće strane.



Umbrel nudi brojne aplikacije koje će vam pomoći da pokrenete vaš Lightning čvor. Već možete birati između dve glavne implementacije:




- LND, putem aplikacije *Lightning Node*;
- Core Lightning.



https://planb.academy/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

Zatim možete upravljati svojim čvorom sa glavnog interfejsa, ili, za još veću funkcionalnost i napredne opcije, instalirati *Ride The Lightning* ili *ThunderHub*. Ovi alati će vam pružiti znatno sveobuhvatniji web interfejs za upravljanje vašim čvorom.


https://planb.academy/tutorials/node/lightning-network/ride-the-lightning-ca007688-0653-490c-8349-81d330d744b5

https://planb.academy/tutorials/node/lightning-network/thunderhub-16909a39-2484-408e-a118-4e34e249bb9a

![Image](assets/fr/088.webp)



Na kraju, preporučujem aplikaciju *Lightning Network+*, koja vam omogućava pronalaženje partnera sa kojima možete otvoriti kanale, omogućavajući i odlazne i dolazne novčane transakcije.



![Image](assets/fr/089.webp)



Zahvaljujući Umbrelu, upravljanje ličnim Lightning čvorom je pojednostavljeno, ali i dalje ostaje relativno složeno. Iz tog razloga preporučujem da pohađate kurs LNP 202, koji predstavlja logičan nastavak kursa BTC 202, i u okviru kojeg vas korak po korak pratim u postavljanju i upravljanju vašim Lightning čvorom na Umbrelu.



https://planb.academy/courses/593e483e-1785-4e83-aa7e-32b99056844c

### Tailscale



Još jedna aplikacija koja mi se posebno sviđa na Umbrel-u je Tailscale. To je VPN aplikacija dizajnirana da pojednostavi kreiranje sigurnih mreža između više uređaja, gde god da se nalaze u svetu. Za razliku od tradicionalnih VPN-ova, koji se oslanjaju na centralizovane servere, Tailscale koristi WireGuard protokol za uspostavljanje end-to-end enkriptovanih veza između vaših različitih mašina. To znači da možete postaviti funkcionalan VPN za samo nekoliko minuta, bez potrebe za komplikovanim mrežnim konfiguracijama.



Na Umbrel-u, instalacija Tailscale-a povezuje vaš Bitcoin čvor sa vašom sopstvenom virtuelnom privatnom mrežom. Kada se konfiguriše, vaš čvor dobija privatnu Tailscale IP adresu, dostupnu samo sa drugih uređaja povezanih na istu Tailscale mrežu (kao što su računari, pametni telefoni i tableti). Ova veza je end-to-end enkriptovana i ne prolazi kroz nezaštićenu javnu mrežu, što značajno poboljšava sigurnost u poređenju sa neenkriptovanom vezom.



![Image](assets/fr/090.webp)



U konkretnim terminima, Tailscale vam nudi nekoliko prednosti kada koristite vaš Umbrel:





- Možete upravljati Umbrel interfejsom ili pristupiti aplikacijama povezanim s vašim čvorom (kao što su Mempool, Ride The Lightning, ThunderHub...) s bilo kojeg mesta, kao da ste na istoj lokalnoj mreži, bez otvaranja portova na internetu i bez korišćenja Tor-a, koji je veoma spor;





- Možete se povezati sa svojim Electrum serverom (Electrs ili Fulcrum) ili direktno na Bitcoin Core putem vašeg VPN-a, zaobilazeći Tor. Ovo pruža sigurnu vezu, uporedivu sa korišćenjem Tor-a, ali sa mnogo većom brzinom i smanjenom latencijom. Ukratko, dobijate privatnost i sigurnost Tora, ali uz brzinu klasične internet veze (clearnet). Za on-chain novčanik, ova prednost može delovati marginalno, ali ako planirate da kasnije pokrenete sopstveni Lightning čvor, razlika je značajna. Naime, plaćanja putem vašeg čvora u pokretu na Tor-u su izuzetno spora zbog brojnih razmena koje su potrebne, dok sa Tailscale-om, radi savršeno.





- Nema potrebe za konfigurisanje NAT pravila, otvaranje portova ili postavljanje konvencionalnog VPN servera. Kada je aplikacija instalirana na Umbrelu i vašim uređajima, mreža se automatski uspostavlja.



Tailscale na Umbrelu je stoga veoma interesantno rešenje ako želite da pristupite svom čvoru sa bilo kog mesta na svetu na siguran, visokoperformansan i jednostavan način za konfiguraciju, bez žrtvovanja privatnosti ili sigurnosti.



Da biste instalirali i konfigurisali Tailscale na vašem Umbrelu, pogledajte ovaj vodič, odeljak 4: "*Korišćenje Tailscale-a na Umbrelu*":



https://planb.academy/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

### Nostr



Nostr, akronim za "*Notes and Other Stuff Transmitted by Relays*", je otvoreni, decentralizovani protokol dizajniran da omogući objavljivanje i razmenu poruka na internetu bez oslanjanja na centralizovanu platformu. Svaki korisnik ima par kriptografskih ključeva: javni ključ (`npub`), koji služi kao identifikator, i privatni ključ (`nsec`), koji se koristi za potpisivanje poruka i garantovanje njihove autentičnosti.



Poruke se prenose putem mreže nezavisnih releja. Ova distribuirana arhitektura čini Nostr otpornim na cenzuru: nijedan pojedinačni server ne kontroliše pristup ili distribuciju, a korisnik se može povezati sa onoliko releja koliko želi.



Ovaj protokol je veoma popularan unutar Bitcoin zajednice jer, kao i Bitcoin, Nostr rešava pitanja digitalnog suvereniteta i kontrole podataka. Njegov tvorac, Fiatjaf, programer koji je već prepoznat u ekosistemu po svojim brojnim doprinosima.



Sa vašim Umbrelom, možete optimizovati korišćenje Nostr-a. Instaliranjem aplikacije ***Nostr Relay***, možete hostovati sopstveni privatni relej direktno na vašem uređaju, osiguravajući da svi vaši postovi i interakcije na Nostr-u budu sačuvani lokalno i ne mogu biti izgubljeni brisanjem od strane javnih releja.



Nostr klijenti ***noStrudel*** ili ***Snort*** su takođe dostupni na Umbrel-u. Zahvaljujući ovim aplikacijama, možete objavljivati, čitati, pretraživati profile i komunicirati sa Nostr ekosistemom direktno preko web interfejsa na svom Umbrelu.



Na kraju, postoji aplikacija ***Nostr Wallet Connect*** na Umbrel-u, koja omogućava obavljanje izvornih Lightning plaćanja unutar Nostra. Konkretno, možete povezati svoj budući Lightning čvor sa Nostr klijentima kako biste slali mikroplaćanja, nazvana "*zaps*", da nagradite sadržaj ili da ostvarite monetizovanu interakciju, bez korišćenja usluga trećih strana. Ove uplate idu direktno sa vašeg ličnog čvora preko vaših kanala.



Da biste saznali kako koristiti sve ove aplikacije, preporučujem da pogledate ovaj kompletan vodič:



https://planb.academy/tutorials/node/others/umbrel-nostr-7ae147e8-f5cd-46e1-861b-17c2ea1e08fd

### BTCPay Server



BTCPay Server je besplatan, open-source procesor plaćanja koji vam omogućava da prihvatate uplate putem Bitcoin i Lightning mreže bez posrednika, dok i dalje zadržavate punu kontrolu nad svojim sredstvima.



Arhitektura BTCPay Server-a zasnovana je na Bitcoin čvoru, a za Lightning na kompatibilnoj implementaciji (LND, Core Lightning...), što ga čini jednim od retkih potpuno ne-kastodijalnih PoS rešenja. Takođe je najopsežniji softver za praćenje i računovodstvo.



![Image](assets/fr/091.webp)



Ako posedujete biznis i želite da prihvatate Bitcoin uplate direktno putem vašeg Umbrel čvora, BTCPay Server aplikacija je idealna za vas. Da biste saznali više o ovoj temi, preporučujem da konsultujete sledeće resurse:





- Kurs BIZ 101 o korišćenju Bitcoina u vašem poslovanju:



https://planb.academy/courses/a804c4b6-9ff5-4a29-a530-7d2f5d04bb7a



- Kurs POS 305 o korišćenju BTCPay Servera:



https://planb.academy/courses/6fc12131-e464-4515-9d3f-9255365d5fa1



- BTCPay Server vodič:



https://planb.academy/tutorials/business/point-of-sale/btcpay-server-928eb01e-824b-4b57-a3e8-8727633beddc


# Napredni koncepti i najbolje prakse


<partId>fc77a62a-8d9f-4144-9080-3057b04db2c6</partId>



## Održavanje Umbrel čvora


<chapterId>06d77d09-bf24-4555-b2ba-c08bbda477c7</chapterId>



Za početak ove završne sekcije, pre nego što pređemo na naprednu teoriju, u ovom kratkom poglavlju pogledaćemo najbolje prakse i konkretne korake koje možete preduzeti kada je vaš Umbrel čvor instaliran, sinhronizovan i pravilno konfigurisan. Kako održavati Umbrel svakodnevno?



### Održavanje opreme zdravom



Pouzdani čvor počinje sa stabilnim hardverom. Osigurajte da je mašina koja sadrži vaš čvor pravilno ventilisana, bez prašine, i instalirana u suvom okruženju, daleko od bilo kakvih izvora toplote i vlage. Izbegavajte da je smestite u skučen prostor i odlučite se za dobro ventilisanu lokaciju.



Na Raspberry Pi i mini-PC-jevima, prašina na kraju začepljuje hladnjake, podižući temperaturu i dovodeći do usporavanja (dobrovoljno ograničenje korišćenja resursa), što zauzvrat rezultira padom efikasnosti vašeg čvora. Zato preporučujem periodično čišćenje ulaza za vazduh i ventilatora, idealno svakih nekoliko meseci.



Osigurajte da koristite visokokvalitetno napajanje, jer nestabilan napon može dovesti do oštećenja sistema, pa čak i predstavljati opasnost od požara. Idealno bi bilo da koristite originalno napajanje koje je isporučio proizvođač vaše mašine. Takođe, budite oprezni zbog mogućeg pregrevanja produžnih kablova usled Joule-ovog efekta: uvek se pridržavajte maksimalno dozvoljene snage i nikada ne spajajte više produžnih kablova jedan za drugim.



Takođe preporučujem ulaganje u UPS. Ovo štiti vaš čvor od naglih gašenja, omogućava Umbrelu da se ispravno isključi u slučaju nestanka struje i osigurava kontinuitet rada tokom mikro prekida ili kratkotrajnih kvarova.



Na strani skladištenja, pratite napredak: ako se disk približava zasićenju, razmislite o oslobađanju prostora (deinstalirajte neiskorišćene aplikacije, prilagodite postavke indeksatora) ili o prelasku na veći SSD. Mane punog Bitcoin čvora su što se zahtevi za skladištenjem stalno povećavaju, jer se novi blok generiše na svakih 10 minuta, a stari blokovi se ne mogu brisati (osim ako čvor nije u pruned režimu). Stoga vam savetujem da planirate dovoljno veliki kapacitet prilikom kupovine vaše opreme (minimum 2 TB).



### Ažuriranje



Ažuriranja (eng. updates) čvorova su važna iz tri glavna razloga: prvo, bezbednost (zakrpe za ranjivosti, jačanje mreže i zaštita od DoS napada); drugo, kompatibilnost (promene u politici prenosa, promene formata i nadogradnje protokola); i treće, pouzdanost i performanse (ispravke grešaka, potrošnja resursa i druga poboljšanja). Zato periodično proveravajte da li su UmbrelOS i vaše aplikacije ažurirane:





- Da biste ažurirali sistem: otvorite meni sa podešavanjima (eng. settings), zatim kliknite na dugme "*Check for Update*" pored parametra "*UmbrelOS*".



![Image](assets/fr/042.webp)





- Da biste ažurirali aplikacije: idite na App Store. Ako neka od vaših aplikacija zahteva ažuriranje, dugme sa crvenim mehurićem će se pojaviti u gornjem desnom uglu interfejsa. Jednostavno kliknite na njega, a zatim ažurirajte svaku aplikaciju.



Redovno izvodite ovu operaciju kako biste održavali vaš operativni sistem i aplikacije ažurnim.



### Bekapovi (rezervne kopije)



Ako koristite samo svoj Bitcoin čvor za validaciju i distribuciju vaših transakcija, ali su vaši novčanici upravljani izvan Umbrel-a (npr. sa hardware novčanikom i Sparrow novčanikom), nema ničega što bi se direktno bekapovalo na Umbrel. U ovom slučaju, ključna rezervna kopija ostaje [seed fraza](https://planb.academy/resources/glossary/recovery-phrase) i [deskriptor vašeg eksternog novčanika](https://planb.academy/resources/glossary/output-script-descriptors), bez obzira na to da li koristite sopstveni čvor. Drugim rečima, u odnosu na prethodnu postavku, ništa se ne menja.


S druge strane, u zavisnosti od dodatnih aplikacija koje koristite na Umbrel-u, mogu biti potrebne dodatne rezervne kopije. Ovo je posebno slučaj ako upravljate Lightning čvorom na Umbrel-u. U ovom slučaju, apsolutno je neophodno napraviti rezervnu kopiju seed fraze koja je generisana kada ste instalirali vaš Lightning čvor. Pored seed fraze, potrebno je imati ažuriranu ***Static Channel Backup (SCB)*** kako biste mogli da povratite vaš Lightning čvor u slučaju problema. SCB vam omogućava da povratite svoja sredstva prisilnim zatvaranjem kanala. Ako nedostaje ili seed ili SCB, nemoguće je povratiti Lightning čvor.



Umbrel takođe nudi opciju automatskog i dinamičkog bekapovanja ovog SCB-a na njihovim serverima, putem Tor-a, kako bi se osiguralo da je uvek dostupan ažuriran fajl. U ovom slučaju, potreban je samo seed za vraćanje čvora.



Ponovo ćemo razmotriti ove aspekte detaljno u sledećem LNP202 kursu.



### Svakodnevna operativna bezbednost



U pogledu bezbednosti, koristite dugu, jedinstvenu i nasumično generisanu lozinku za Umbrel interfejs, i ne zaboravite da aktivirate dvofaktorsku autentifikaciju (2FA). Za aplikacije koje nude zaštitu lozinkom i 2FA, uvek aktivirajte obe opcije i promenite podrazumevane lozinke.



Nikada ne izlažite kontrolnu tablu (eng. dashboard) internetu bez korišćenja sigurnog prolaza (kao što su VPN, Tor, ili samo lokalni pristup). Ograničite broj aplikacija koje instalirate i redovno brišite one koje vam više nisu potrebne, kako biste smanjili površinu napada.



Da biste produbili svoje znanje o računarskoj bezbednosti uopšte, toplo preporučujem da pogledate ovaj drugi besplatni kurs:



https://planb.academy/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1

### Dijagnoza i samopomoć



U slučaju greške na vašem Umbrelu, prvo generišite dijagnostički paket preko sekcije za rešavanje problema u UmbrelOS-u ili odgovarajućoj aplikaciji, a zatim uredno restartujte aplikaciju. Ako je potrebno, pokušajte i sa potpunim restartovanjem sistema.



Ako problem potraje, preporučujem da [pristupite Umbrel korisničkoj zajednici na njihovom Discord-u](https://discord.gg/efNtFzqtdx). Počnite pretragom kako biste utvrdili da li je neko već naišao na isti problem i pronašao rešenje. Ako nije, možete postaviti poruku u `general-support` kanalu. Takođe možete koristiti [Umbrel forum](https://community.umbrel.com/).



Ova područja će vam omogućiti ne samo da pratite sigurnosne najave i ažuriranja, već i da postavljate pitanja i, na kraju, da pomažete drugim korisnicima. Često se u tim razmenama otkrivaju najbolje prakse.



Uz ove jednostavne navike, vaš Umbrel čvor će ostati stabilan, siguran i koristan, kako za vas tako i za Bitcoin mrežu.




## Razumevanje IBD-a i pronalaženja peer-ova (drugih čvorova u mreži)


<chapterId>175ac9d1-ea23-45d9-9918-d3e7352435cd</chapterId>



Vaš Bitcoin čvor se pokreće bez ikakvog prethodnog znanja o istoriji transakcija. U početku, to je samo računar koji pokreće softver (Bitcoin Core ili sličan). Da bi postao potpuno sinhronizovan i operativan Bitcoin čvor, mora lokalno rekonstruisati stanje blockchaina proveravajući sve blokove objavljene od Genesis bloka (blok 0, objavljen od strane Satoshi Nakamoto 3. januara 2009). Ovaj korak se zove **IBD (_Initial Block Download_)**.



IBD se sastoji od preuzimanja i verifikacije svakog bloka i transakcije pojedinačno, primenjujući pravila konsenzusa, kako bi se izgradila sopstvena verzija blockchaina. Cilj nije samo preuzimanje kopije neproverenih podataka, već dolazak do istog zaključka potpuno nezavisno, kao poštena većina mreže.



![Image](assets/fr/092.webp)



### Glavne faze IBD-a



Sinhronizacija počinje sa korakom _**headers-first**_. Vaš čvor traži niz zaglavlja blokova od više drugih čvorova u mreži i za svaki blok proverava proof of work u odnosu na difficulty (cilj težine), sintaksu, kao i pravila vezana za vremensku oznaku i broj verzije. Ukratko, osigurava da svako primljeno zaglavlje ispunjava pravila konsenzusa.



![Image](assets/fr/093.webp)



Kao podsetnik, Bitcoin blok se sastoji od zaglavlja od 80 bajtova i liste transakcija. Jedinstveni identifikator bloka ili otisak bloka se dobija primenom dvostrukog SHA-256 heš algoritma na ovo zaglavlje, koje sadrži 6 polja:




- verzija
- Heš vrednost prethodnog bloka
- Merkle Root (glavni heš) svih transakcija u bloku
- Timestamp (veće od srednjeg vremena prethodnih 11 blokova)
- ciljna težina (eng. difficulty target)
- Nonce



![Image](assets/fr/094.webp)



Transakcije se organizuju u Merkle stablo. Ovo je struktura koja sumira veliki skup podataka (u ovom slučaju, sve transakcije u bloku) agregiranjem njihovih heševa progresivno dva po dva do jednog "korena", čime se dokazuje da element pripada skupu (i otkriva bilo kakva modifikacija). Na ovaj način, svaka modifikacija transakcije takođe menja koren Merkle Tree-a i stoga menja i otisak (jedinstveni heš) zaglavlja bloka. SegWit je uveo poseban dodatni zapis za witness (potpise), koji se nalazi u coinbase transakciji.



![Image](assets/fr/095.webp)



Ovaj korak _**headers-first**_ omogućava čvoru da identifikuje granu sa najviše rada (bez obzira na broj blokova), što je grana na kojoj se Bitcoin čvorovi sinhronizuju. Kada je ova grana identifikovana, čvor preuzima sadržaj blokova paralelno sa nekoliko veza, zatim validira svaku transakciju: format, validnost skripti (osim `assumevalid=1`), iznose i odsustvo dvostrukog trošenja. Sa svakom uspešnom proverom, trenutno stanje nepotrošenih novčića (UTXO set) se ažurira u `chainstate/` bazi podataka: potrošeni izlazi se uklanjaju, dok se novi validni izlazi dodaju.



Mempool se aktivira tek kada se čvor približi najnovijem bloku lanca: dok je čvor još u zaostatku, nema transakcija na čekanju koje bi trebalo da čuva.



Kada je IBD završen, čvor ulazi u svoju normalnu fazu: validira nove blokove kako se objavljuju, održava svoj mempool sa transakcijama na čekanju prema svojim pravilima prenosa, prenosi transakcije i blokove, i upravlja bilo kakvim reorganizacijama lanca.



### AssumeValid



Bitcoin Core uključuje mehanizam dizajniran da smanji potrebno vreme pre nego što čvor postane potpuno operativan, dok zadržava suštinu principa autonomne verifikacije: AssumeValid.



Parametar `assumevalid` zasniva se na prethodnom referentnom bloku, čiji je hash integrisan u svaku verziju softvera. Tokom IBD-a, ako vaš čvor ustanovi da se ovaj blok zaista nalazi na grani sa najviše rada, može ignorisati verifikaciju skripti za sve transakcije pre ove tačke.



Sva ostala pravila (blok struktura, Proof of Work, ograničenja veličine, iznosi transakcija, UTXO-i, itd.) ostaju potpuno verifikovana. Samo se izračunavanje skripti pre ovog referentnog bloka ignoriše. Dobitak u performansama je značajan na IBD-u, jer verifikacija potpisa čini veliki deo CPU opterećenja. Nakon ovog referentnog bloka, verifikacija se vraća u svoje normalno stanje.



Možete primorati punu validaciju svih skripti onemogućavanjem ovog mehanizma, po cenu mnogo dužeg IBD, koristeći parametar `assumevalid=0` u `Bitcoin.conf` fajlu.



### AssumeUTXO



`assumeutxo` je još jedan postojeći parametar, ali za razliku od `assumevalid`, nije aktiviran po defaultu. Ovaj mehanizam omogućava softveru da učita snimak UTXO seta, zajedno sa njegovim metapodacima, i privremeno ga smatra referentnim stanjem, nakon što potvrdi da zaglavlja zaista vode do blockchaina sa najviše rada.



Čvor tako brzo postaje operativan za uobičajene upotrebe (RPC, povezivanje novčanika, itd.), dok istovremeno pokreće kompletnu, verifikovanu rekonstrukciju sopstvenog UTXO seta u pozadini. Kada je ova faza završena, početni snimak se zamenjuje lokalno rekonstruisanim stanjem. Ovaj pristup odvaja brzo obezbeđivanje čvora od potpune verifikacije, bez kompromitovanja iste.



### Otkrivanje peer-ova: Kako vaš čvor povezuje i pronalazi druge čvorove u Bitcoin mreži?



Kada se čvor prvi put pokrene, još uvek ne zna za nijedan drugi čvor. Međutim, mora pronaći druge Bitcoin čvorove na internetu kako bi zatražio zaglavlja, a zatim blokove, i samim tim da bi završio svoj IBD. Da bi uspostavio ove veze, Bitcoin Core prati prioritetnu logiku.



![Image](assets/fr/096.webp)



Kada se čvor ponovo pokrene nakon što je već bio korišćen, Core prvo pokušava da se ponovo poveže sa odlaznim čvorovima registrovanim pre gašenja, informacijama koje su sačuvane u datoteci `anchors.dat`. Zatim konsultuje svoju knjigu IP adresa **`peers.dat`**, koja čuva listu prethodno susretanih čvorova, kako bi se ponovo povezao sa njima. Ovo je jednostavno lokalna datoteka, koju Core ažurira i održava. S druge strane, za novi čvor koji je tek pokrenut, ove 2 datoteke su prazne, jer čvor još uvek nije komunicirao sa drugim Bitcoin čvorovima.



U ovom slučaju, softver pretražuje _**DNS seed-ove**_. To su [serveri koje održavaju priznati programeri ekosistema](https://github.com/Bitcoin/Bitcoin/blob/master/src/kernel/chainparams.cpp), koji vraćaju listu IP adresa pretpostavljenih aktivnih čvorova. Ove adrese omogućavaju novom čvoru da započne svoje prve konekcije i zatraži potrebne podatke za IBD. Evo liste *DNS seeds* aktivnih do danas (avgust 2025):




- Pieter Wuille: `seed.Bitcoin.sipa.be.`
- Matt Corallo: `dnsseed.bluematt.me.`
- Luke Dashjr: `dnsseed.Bitcoin.dashjr-list-of-P2P-nodes.us.`
- Jonas Schnelli: `seed.Bitcoin.jonasschnelli.ch.`
- Peter Todd: `seed.btc.petertodd.net.`
- Sjors Provoost: `seed.Bitcoin.sprovoost.nl.`
- Stephan Oeste: `dnsseed.emzy.de.`
- Jason Maurice: `seed.Bitcoin.wiz.biz.`
- Ava Chow: `seed.Mainnet.achownodes.xyz.`



U velikoj većini slučajeva, *DNS seeds* korak je dovoljan za uspostavljanje prvih veza sa drugim čvorovima. Ako, izuzetno, ovi serveri ne odgovore u roku od 60 sekundi, čvor prelazi na drugi metod: [statistička lista sa preko 1.000 adresa](https://github.com/Bitcoin/Bitcoin/blob/master/src/chainparamsseeds.h) _seed čvorova_ je ugrađena u kȏd Bitcoin Core-a i redovno se ažurira. Ako prva dva metoda dobijanja IP adresa ne uspeju, ovo poslednje rešenje uspostavlja početnu vezu, od koje čvor može zatim zatražiti nove IP adrese.



![Image](assets/fr/097.webp)



Kao poslednja opcija, možete ručno uneti IP adrese u fajl `peers.dat` kako biste forsirali povezivanje sa određenim čvorovima.


Jednom kada se pokrene, interni menadžer adresa diversifikuje izvore (odvojene autonomne mreže, clearnet i Tor, kao i različite geografske oblasti) kako bi smanjio rizik od topološke izolacije. Čvor uspostavlja ove odlazne veze (veze koje sam bira, i koje su stoga sigurnije).



Ako vaš čvor sluša na otvorenom portu (po defaultu, 8333), on prihvata i dolazne veze. Ovi mehanizmi povećavaju otpornost mreže, jer omogućavaju novim nodovima da se povežu, ali ne pružaju direktnu korist vašem sopstvenom inicijalnom preuzimanju blokova (IBD). Ako vaš čvor radi na Tor-u, logika ostaje ista, ali korišćene adrese su `.onion` servisi.




## Anatomija Bitcoin čvora


<chapterId>b420bd9d-7e2a-4984-bc70-2b732a94c8ce</chapterId>



Kada vaš čvor završi svoju početnu sinhronizaciju, lokalno skladišti nekoliko komplementarnih skupova podataka, omogućavajući mu da validira blokove i transakcije, opslužuje mrežne peer-ove i da se brzo restartuje zadržavajući svoje stanje.. Tri ključna temelja čvora su::




- **blokovi** blockchaina sačuvani na disku,
- **UTXO set** održavan u key-value bazi podataka,
- i **mempool** koji se čuva u RAM-u i povremeno serijalizuje.



Pored toga, nekoliko pomoćnih fajlova (peers, procene naknada, liste isključenja, novčanici, itd.) upotpunjuju sliku. Hajde da otkrijemo ulogu svih ovih fajlova.



### Gde se podaci čvora zapravo nalaze?



Podrazumevano, Bitcoin Core čuva svoje podatke u specifičnom radnom direktorijumu. U GNU/Linux-u, to je obično u `~/.Bitcoin/`, u Windows-u u `%APPDATA%\Bitcoin/`, a u macOS-u u `~/Library/Application Support/Bitcoin/`. Ako koristite spremno rešenje (npr. unutar node distribucije), ovaj direktorijum može biti montiran na drugom mestu, ali njegova struktura ostaje ista. Važni pod-folderi i fajlovi opisani u nastavku i dalje se nalaze ovde.



![Image](assets/fr/098.webp)



### Blokovi



Blockchain je, dakle, kolekcija blokova. Full node skladišti ove blokove kao sekvencijalne flat fajlove i održava paralelni indeks za brzo preuzimanje. Kada je potrebno (reorganizacija, ponovno skeniranje novčanika, usluga drugom čvoru), ovi podaci se ponovo čitaju u izvornom obliku.



**Napomena:** Reorganizacija, ili resinhronizacija, je fenomen u kojem blockchain prolazi kroz modifikaciju svoje strukture zbog postojanja konkurentskih blokova na istoj visini. Ovo se dešava kada se deo blockchaina zameni drugim lancem sa većom količinom akumuliranog rada. Ove resinhronizacije su prirodni deo rada Bitcoina, gde različiti rudari mogu pronaći nove blokove gotovo istovremeno, čime se Bitcoin mreža deli na dva dela. U takvim slučajevima, mreža se može privremeno podeliti na konkurentske lance. Na kraju, kako jedan od ovih lanaca akumulira više rada, drugi lanci bivaju napušteni od strane čvorova, a njihovi blokovi postaju poznati kao "zastareli blokovi" ili "blokovi siročad". Ovaj proces zamene jednog lanca drugim naziva se resinhronizacija.



#### Blk*.dat datoteke (sirovi blok podaci)



Primljeni i validirani blokovi se upisuju u sekvencijalne kontejnere nazvane `blkNNNNN.dat`, smeštene u fascikli `blocks/`. Svaka datoteka se popunjava redom dok ne dostigne maksimalnu veličinu od 128 MiB, nakon čega Core otvara sledeću datoteku. Unutra, svaki blok je serijalizovan u mrežnom formatu, prethodi mu magični identifikator i dužina. Ova organizacija omogućava brzo pisanje na disk i olakšava serviranje blokova drugim čvorovima koji se sinhronizuju.



![Image](assets/fr/099.webp)



U pruned režimu, čvor zadržava samo nedavni prozor ovih datoteka kako bi ograničio otisak na disku. Briše najstarije `blk*.dat` kontejnere čim se dostigne konfigurisana ciljana veličina prostora, dok zadržava dovoljno istorije da ostane konzistentan sa najbolje poznatim lancem. Indeks i UTXO set ostaju normalni, omogućavajući validaciju sledećih transakcija i blokova.



#### Rev*.dat fajlovi (podaci o otkazivanju)



Kako bi mogao da se vrati u prošlost tokom reorganizacije, Core čuva, paralelno sa svakim `blk` fajlom, `revNNNNN.dat` fajl u `blocks/`. Ovaj fajl sadrži informacije potrebne za poništavanje efekta bloka na UTXO skup: za svaki izlaz koji blok potroši, prethodno stanje odgovarajućeg UTXO se čuva (iznos, skripta, visina...). U slučaju napuštanja bloka, čvor može brzo rekonstituisati prethodno stanje bez potrebe za ponovnim skeniranjem celog lanca.



![Image](assets/fr/100.webp)



#### Indeks blokova (blocks/index)



Pretraživanje bloka direktno u flat fajlovima bi bilo previše vremenski zahtevno. Core stoga održava LevelDB bazu podataka u `blocks/index/` koja navodi, za svaki poznati blok, metapodatke kao što su heš vrednost, visina, status validacije, `blk` fajl i pomeraj (eng. offset) gde se nalazi. Kada peer zatraži blok, ili kada interna komponenta treba da pristupi specifičnom bloku, ovaj indeks omogućava brz pristup. Bez ovog indeksa, bilo bi potrebno previše operacija.



![Image](assets/fr/101.webp)



#### Opcionalni indeksi (indexes/)



Neki indeksi su opcionalni i po defaultu su onemogućeni, jer povećavaju zauzeće diska:




- `indexes/txindex/`, koji smo već pomenuli, pruža tabelu mapiranja transakcija → lokacija, omogućavajući pronalaženje bilo koje potvrđene transakcije bez poznavanja bloka koji je sadrži. Ova opcija je korisna za RPC pozive poput `getrawtransaction` koji nisu vezani za konkretan novčanik, ali troši dosta resursa.
- `indexes/blockfilter/` koji može sadržati kompaktne blok filtere (BIP157/158) za SPV klijente. Ove strukture ubrzavaju verifikaciju na strani klijenta na račun dodatnog skladištenja na indekserskom čvoru.



### UTXO set (tzv. chainstate, baza trenutnog stanja lanca)



UTXO model  (*Unspent Transaction Output*) je računovodstveni prikaz Bitcoina: svaki neutrošeni izlaz je dostupan "novčić" ili na engleskom "coin" koji se može koristiti kao ulaz za buduću transakciju.



![Image](assets/fr/102.webp)



Ukupnost svih ovih delova u datom trenutku T čini UTXO set: veliku listu svih delova koji su sada dostupni. Ovo je stanje koje čvor konsultuje da odluči da li transakcija troši legitimne jedinice koje nisu već korišćene u prethodnoj transakciji (da bi se izbegla dvostruka potrošnja).



![Image](assets/fr/103.webp)



UTXO set je smešten u fascikli `chainstate/` kao kompaktna LevelDB baza podataka. Svaki unos povezuje ključ izveden iz heša transakcije i izlaznog indeksa sa vrednošću koja sadrži: iznos, `scriptPubKey` zaključavanje, visinu bloka kreiranja (eng. block height) i indikator coinbase-a.



![Image](assets/fr/104.webp)



Čvor održava keš memoriju iznad LevelDB-a kako bi apsorbovao učestale operacije čitanja i pisanja. Parametar `dbcache` može se koristiti za modifikaciju veličine ove keš memorije: što je veća, to više koristi IBD i trenutna validacija imaju od pristupa memoriji, po cenu veće potrošnje RAM-a. Kada rudar pronađe novi blok, čvor briše iz skupa UTXO izlaze koji su potrošeni (ili konzumirani) transakcijama uključenim u blok i dodaje novo kreirane izlaze.



Teoretski, mogli bismo potvrditi transakciju ponovnim skeniranjem istorije blokova kako bismo proverili da izlaz nikada nije potrošen. U praksi, međutim, ovo bi bilo previše zahtevno vremenski, jer bi ceo blockchain morao biti skeniran za svaku novu transakciju. UTXO set, stoga, pruža minimalni pregled potreban da se lokalno i u razumnom vremenskom periodu dokaže odsustvo dvostruke potrošnje.



Imajte na umu da je UTXO set često u centru zabrinutosti oko decentralizacije Bitcoina, jer se njegova veličina prirodno brzo povećava. Ovo je delimično zbog rastuće cene Bitcoina, koja podstiče fragmentaciju delova, a delimično zbog sve veće usvajanja sistema: što je više korisnika, veća je potražnja za UTXO-ima.



![Image](assets/fr/105.webp)



Rast UTXO seta takođe proizlazi iz strukture jednostavnih platnih transakcija na Bitcoinu. Zaista, kada izvršite uplatu, koristite jedan UTXO kao ulaz i kreirate 2 nova UTXO-a kao izlaz (jedan za uplatu i drugi za kusur). Na kraju, heuristika analize lanca, nazvana CIOH (*Common Input Ownership Heuristic*), pruža dodatni podsticaj da se izbegne konsolidacija "novčića".



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Pošto se deo toga mora čuvati u RAM-u kako bi se transakcije verifikovale u razumnom vremenu, UTXO set može postepeno učiniti rad full node-a previše skupim. Da bi se rešio ovaj problem, već postoji nekoliko predloga, posebno [Utreexo](https://planb.academy/resources/glossary/utreexo).



### Mempool



Mempool je lokalni skup važećih transakcija koje su primljene, ali još nisu potvrđene. Kao podsetnik, "potvrđena transakcija" je ona koja je uključena u važeći blok. Svaki čvor održava svoj mempool, koji može da se razlikuje od onog drugih čvorova u mreži u zavisnosti od:




- veličina dodeljena mempool-u putem parametra `maxmempool`: čvor sa većim mempool-om moći će da drži više transakcija nego čvor sa manjim mempool-om (osim ako se potonji ne isprazni);
- pravila mempool-a: ona predstavljaju podskup pravila prosleđivanja čvora i definišu karakteristike koje nepotvrđena transakcija mora ispuniti da bi bila prihvaćena u mempool;
- perkolacija transakcija: zbog različitih faktora, određena transakcija može biti distribuirana jednom delu mreže, ali još uvek nije stigla do drugog.



Važno je napomenuti da mempool-ovi čvorova nemaju konsenzusnu vrednost. Bitcoin radi savršeno čak i ako svaki čvor ima različit mempool. Na kraju, autoritativni blokovi su uvek oni dodati u blockchain. Na primer, čak i ako čvor u početku odbije određenu transakciju u svom mempool-u (validnu prema pravilima konsenzusa), biće obavezan da je prihvati ako je na kraju uključena u blok sa validnim Proof of Work-om. Ako to ne učini i odbije ovaj blok, iako je u skladu sa pravilima konsenzusa, to bi pokrenulo hard fork, tj. stvaranje novog, odvojenog Bitcoina na kojem bi bio sam.



#### Politika i upravljanje memorijom



Kada se transakcija prihvati, Core primenjuje niz provera prema pravilima konsenzusa (sintaksa, validni skriptovi, bez dvostrukog trošenja, itd.) i mempool pravilima, koja su lokalna politika (RBF, minimalni pragovi naplate, ograničenje podataka u `OP_RETURN`, itd.). Ako transakcija poštuje ova pravila, ona se čuva u memoriji.



Veličina mempool-a je ograničena parametrima `maxmempool` u datoteci `Bitcoin.conf` (više o tome u sledećem poglavlju). Podrazumevano, ograničenje je 300 MB. Kada je popunjen, čvor dinamički podiže svoj minimalni prag naplate i izbacuje najmanje profitabilne transakcije prvo (tj. zadržava transakcije koje bi trebalo prvo da budu izrudarene). Transakcije koje su previše stare takođe mogu isteći nakon podešenog kašnjenja.



#### Mempool postojanost na disku



Da bi se ubrzala ponovna pokretanja, Core periodično serijalizuje stanje mempool-a u datoteku `Mempool.dat` kada se čvor isključi. Pored stvarnog mempool-a, koji ostaje u memoriji, Core čuva ovu datoteku `Mempool.dat` na disku. Sledeći put kada se čvor pokrene, on ponovo učitava ovu snimku i briše sve što više nije važeće za trenutni blockchain.



### Pomoćne datoteke i baze podataka



Nekoliko drugih fajlova na istom nivou kao `blocks/`, `chainstate/` i `indexes/` učestvuju u pravilnom funkcionisanju:




- `peers.dat` čuva spisak IP adresa potencijalnih peer-ova, dopunjenu inicijalnim DNS otkrivanjem, mrežnim razmenama i ručnim dodavanjima. Kada se čvor pokrene, može koristiti ovu datoteku za uspostavljanje odlaznih veza.
- Kada je čvor isključen, `anchors.dat` čuva adrese odlaznih peer-ova, tako da možete brzo pokušati da ih kontaktirate ponovo sledeći put kada pokrenete sistem.
- `banlist.json` sadrži lokalne zabrane koje je odredio operater ili čvor (ponovljeno nevažeće ponašanje), kako bi se sprečilo da se čvor ponovo poveže ili prihvati veze od ovih specifičnih peer-ova.
- `fee_estimates.dat` skladišti statistiku vremenskog horizonta o posmatranim potvrđivanjima, koju koristi procenjivač naknada za predlaganje stopa naknada u skladu sa ciljevima kašnjenja izabranim prilikom kreiranja transakcije.
- `bitcoin.conf` sadrži parametre konfiguracije vašeg čvora. Upravo u ovoj datoteci mogu se podesiti pravila prosleđivanja. O tome ću detaljnije govoriti u sledećem poglavlju;
- Datoteka `settings.json` sadrži dodatne parametre za `Bitcoin.conf`.
- `debug.log` je dijagnostički tekstualni log, koji se može koristiti za razumevanje aktivnosti čvora u slučaju greške.
- `bitcoind.pid` beleži identifikator procesa tokom izvršavanja, što omogućava drugim aplikacijama ili skriptama da lako identifikuju Bitcoind (*Bitcoin Daemon*) i po potrebi komuniciraju sa njim. Kreira se pri pokretanju čvora i briše pri gašenju;
- `ip_asn.map` je tabela koja povezuje IP adrese sa ASN‑ovima (autonomnim sistemima) i koristi se za grupisanje i diverzifikaciju peer‑ova(opcija `-asmap`).
- `onion_v3_private_key` čuva privatni ključ Tor v3 servisa kada je opcija `-listenonion` omogućena, kako bi se održala stabilna onion adresa između ponovnih pokretanja.
- `i2p_private_key` čuva I2P privatni ključ kada se koristi `-i2psam=`, za uspostavljanje odlaznih i moguće dolaznih veza na I2P.
- `.cookie` sadrži efemerni RPC autentifikacioni token (kreiran pri pokretanju, obrisan pri gašenju) kada se koristi autentifikacija putem kolačića. Ovo se može koristiti, na primer, za povezivanje softvera za upravljanje novčanikom.
- `.lock` je zaključavanje direktorijuma podataka, koje sprečava više instanci da istovremeno pišu u isti datadir.
- `guisettings.ini.bak` je automatsko čuvanje GUI podešavanja (*Bitcoin Qt*) kada se koristi opcija `-resetguisettings`.



Kao što smo videli u prvim delovima ovog BTC 202 kursa, Bitcoin Core je i softver Bitcoin čvora i novčanika. Međutim, to nije nužno softver koje bih preporučio za upravljanje vašim novčanicima, jer njegov interfejs ostaje osnovni i njegove funkcionalnosti su ograničene u poređenju sa modernim softverom kao što su Sparrow ili Liana. Core takođe uključuje fajlove za upravljanje vašim novčanicima:





- `wallets/` je podrazumevani direktorijum koji sadrži jedan ili više novčanika;
- `wallets/<name>/Wallet.dat` je SQLite baza podataka za novčanik (ključevi, deskriptori, metapodaci transakcija, itd.);
- `wallets/<name>/wallet.dat-journal` je SQLite rollback log — beleži promene koje se mogu poništiti u slučaju greške.



Da rezimiramo, ovde je struktura Bitcoin Core datoteke:



```
~/.bitcoin/
├── bitcoin.conf
├── blocks/
│   ├── blk00000.dat
│   ├── blk00001.dat
│   ├── rev00000.dat
│   ├── rev00001.dat
│   └── index/
├── chainstate/
├── indexes/
│   ├── txindex/
│   ├── blockfilter/
│   │   └── basic/
│   │       ├── db/
│   │       └── fltrNNNNN.dat
│   └── coinstats/
│       └── db/
├── wallets/
│   └── <wallet_name>/
│       ├── wallet.dat
│       └── wallet.dat-journal
├── peers.dat
├── anchors.dat
├── banlist.json
├── mempool.dat
├── fee_estimates.dat
├── bitcoind.pid
├── debug.log
├── ip_asn.map
├── onion_v3_private_key
├── i2p_private_key
├── settings.json
├── guisettings.ini.bak
├── .cookie
└── .lock
```



### Put za validaciju novog bloka



Po prijemu novog bloka, vaš čvor proverava Proof of Work i, generalno, usklađenost sa pravilima konsenzusa. Ako je sve u redu, primenjuje promene transakciju po transakciju na svoj UTXO set: proverava da svaki unos troši postojeće UTXO-e sa važećom skriptom, briše te UTXO-e i dodaje nove izlaze. Ako je sve validno, promene se primenjuju na `chainstate/`.



Paralelno, podaci za poništavanje se upisuju u `rev*.dat`, a metapodaci u indeks `blocks/index/`. Blok se zatim serijalizuje u odgovarajući `blk*.dat` fajl. U slučaju reorganizacije, čvor čita `rev*.dat` unazad kako bi čisto diskonektovao napuštene blokove, obnovio UTXO set, a zatim povezao blokove novog najboljeg lanca.





## Razumevanje bitcoin.conf fajla


<chapterId>c54a629a-ddb1-41cb-9a88-21dfd9be50ca</chapterId>



Fajl `bitcoin.conf` predstavlja glavni konfiguracioni fajl za interfejs Bitcoin Core-a. Omogućava vam da prilagodite ponašanje i parametre vašeg čvora bez potrebe za rekompajliranjem izvornog koda ili pravljenjem izmena u komandnoj liniji. Konkretno, to je obična tekstualna datoteka strukturirana u parovima ključ-vrednost, što znači da svaka linija datoteke referencira određeni parametar (ključ) i njegovu pridruženu vrednost, koja se može modifikovati da bi se prilagodio taj parametar.



U fajlu `bitcoin.conf` mogu se definisati parametri mreže, releja transakcija, performansi, indeksiranja, beleženja (logovanja) ili pristupa preko RPC-a. Međutim, ovaj konfiguracioni fajl nikada ne menja pravila konsenzusa protokola: on određuje isključivo lokalnu politiku čvora (pravila releja), način na koji se povezuje, indeksira i stavlja na raspolaganje svoje servise ili funkcionalnosti drugim čvorovima ili aplikacijama.



### Lokacija i prioritet



Podrazumevano, fajl `bitcoin.conf` se nalazi u Bitcoin Core direktorijumu podataka. Ovo je čuveni direktorijum koji smo pomenuli u prethodnom poglavlju. Međutim, ovaj fajl se ne kreira automatski u Bitcoin Core‑u, osim kada se koristi u određenim okruženjima, kao što je, na primer, Umbrel. Ako već ne postoji, moraćete ga generisati sami tako što ćete jednostavno kreirati fajl pod nazivom `bitcoin.conf`, a zatim ga otvoriti u tekst editoru da biste izvršili svoje izmene.



Parametri definisani u `bitcoin.conf` mogu biti prepisani (overridden) sa 2 sloja:




- `settings.json` (dinamički generisan od strane grafičkog interfejsa ili nekog RPC poziva),
- i opcije modifikovane putem komandne linije.



Imajte na umu da svaka izmena u `bitcoin.conf` zahteva ponovno pokretanje čvora da bi stupila na snagu.



### Format i struktura



Format `bitcoin.conf` je stoga veoma jednostavan: jedna linija po opciji, u obliku `opcija=vrednost`. Nepotrebni razmaci i prazne linije se ignorišu, a komentari u kodu počinju sa `#`.



Većinu Boolean opcija možete isključiti tako što ćete im dodati prefiks `no`. Na primer, `listen=0` i `nolisten=1` su ekvivalentni u zavisnosti od verzije.



Da biste segmentirali konfiguraciju po mreži, možete koristiti sekcije: `[main]`, `[test]` (testnet3), `[testnet4]`, `[bookmark]`, `[regtest]`. Alternativno, možete prefiksirati naziv opcije sa `regtest.maxmempool=100`.



### Šta bitcoin.conf može, a šta ne može da uradi



Kao što je objašnjeno gore, pravila konsenzusa očigledno nisu konfigurisana u `bitcoin.conf`, jer bi to moglo stvoriti hard fork. S druge strane, mnogi drugi aspekti su konfigurisani. Postoje 3 korisne klase koje treba imati na umu:




- Isključivo lokalni parametri. Oni utiču samo na vaš čvor: veličina keša (`dbcache`), pruned režim (`prune`), opcioni indeksi... Oni utiču na performanse vaše mašine, ali ne i na mrežu.
- Prosleđivanje i mempool politika. Oni odlučuju šta vaš čvor prihvata, zadržava i prosleđuje pre potvrde: minimalni prag naknade (`minrelaytxfee`), veličina i vreme zadržavanja u mempool-u (`maxmempool`, `mempoolexpiry`), zamena transakcija (RBF)... Ova pravila nisu deo konsenzusa, tako da dva različita čvora mogu imati različite politike i dalje biti potpuno kompatibilni. S druge strane, ovi parametri će imati uticaj na Bitcoin mrežu (kao što je objašnjeno u prvom delu, naročito sa teorijom perkolacije).
- Povezivanje na mrežu. Ove opcije određuju kako vaš čvor pronalazi peer-ove, sluša, uspostavlja vezu kroz NAT, koristi Tor ili proxy, ili ograničava svoj propusni opseg. One oblikuju vašu topologiju, ali ne menjaju prosleđivanje transakcija.



Razumevanje ove razdvojenosti je ključno: ako transakcija ne poštuje pravila konsenzusa, vaš čvor će je u svakom slučaju odbiti. Ali stroža lokalna politika može odbiti da prosledi transakciju koja je validna u smislu konsenzusa.



### Mreža i topologija



Prvo i najvažnije, važno je jasno razlikovati između 2 tipa veze koje Bitcoin čvor može imati:




- Izlazne veze, koje inicira naš čvor prema drugom čvoru;



![Image](assets/fr/106.webp)





- Dolazne veze, inicirane od strane drugog čvora ka našem.



![Image](assets/fr/107.webp)



Ove dve vrste veza su savršeno sposobne za razmenu istih podataka u oba smera; nije pitanje ograničavanja smera protoka, već samo razlike u inicijatoru veze. Sa stanovišta našeg čvora, odlazne veze se generalno smatraju sigurnijim, jer ih mi iniciramo i precizno biramo sa kojim čvorom ćemo se povezati, što čini malo verovatnim da je veza zlonamerna. Po defaultu, Bitcoin core održava 10 odlaznih veza (8 "*full-relay*" + 2 "*block-relay-only*").



Full node dodaje veću vrednost mreži prihvatanjem dolaznih konekcija. Parametar `listen=1` omogućava slušanje na podrazumevanom portu 8333 mreže o kojoj je reč, omogućavajući prijem ovih dolaznih konekcija na clearnet-u. Da bi ovo funkcionisalo, ovaj port mora biti otvoren i na vašem ruteru. Ako nije, vaš čvor će nastaviti da radi samo sa odlaznim konekcijama, što neće imati uticaja na vašu ličnu upotrebu Bitcoina. Izbor da li ćete dozvoliti dolazne konekcije je vaš; ne postoji "najbolji izbor."



Ako ne želite da otvorite port na svom ruteru, ali i dalje želite da prihvatate dolazne konekcije, možete aktivirati parametar `listenonion=1`. Ovo će postići isti rezultat, ali samo preko Tor mreže umesto preko clearnet-a.



Na nivou mreže, takođe imamo:




- `addnode`: dodaje prijateljski peer za kontakt pored uobičajenog otkrivanja (može se navesti više puta).
- `connect`: strogo ograničava veze na navedenu adresu (može se navesti više puta). Core se neće povezivati ni sa jednim drugim čvorom;
- `seednode`: se koristi samo za popunjavanje liste adresa povezivanjem na jedan čvor, zatim se prekida veza.
- `maxconnections`: definiše globalni plafon za dolazne + odlazne konekcije. Po podrazumevanim postavkama, ovaj parametar je postavljen na 125, što znači da vaš čvor nikada neće prihvatiti više od 125 konekcija.
- `maxuploadtarget` : ograničava brzinu upload-a kako bi se kontrolisala propusnost tokom pomičnog (sliding) perioda od 24 sata. Ovo ograničenje ne ugrožava širenje najnovijih, ključnih elemenata.
- `onlynet`: ograničava odlazne veze samo na odabrane mreže (`ipv4`, `ipv6`, `onion`, `i2p`, `cjdns`). Na primer, ako želite da se vaš čvor povezuje na Bitcoin mrežu samo putem Tor-a, možete omogućiti `onlynet=onion` parametar i onemogućiti dolazne veze (ili dozvoliti veze samo putem Tor-a).
- `dnsseed`: Dozvoljava ili ne dozvoljava slanje zahteva _DNS seed-ovima_ kako bi se dobili peer‑ovi kada je lokalni rezervni spisak adresa mali (podrazumevano: `1`, osim ako je `-connect` ili `-maxconnections=0`).
- `forcednsseed`: forsira slanje zahteva _DNS seed-ovima_ pri pokretanju, čak i ako već imate adrese na raspolaganju (podrazumevano: `0`).
- `fixedseeds`: dozvoljava korišćenje *seed čvorova* (hardkodirana lista adresa) ako _DNS seed-ovi ne uspeju ili su onemogućena (podrazumevano: `1`).
- `dns`: dozvoljava opšte DNS rezolucije (npr. za `-addnode`/`-seednode`/`-connect`).



Podrazumevano, vaš čvor komunicira preko clearnet-a, Tor-a i I2P-a. To znači da peer-ovi sa kojima se povezuje na clearnet-u mogu videti vašu javnu IP adresu, a vaš ISP će verovatno moći da otkrije da pokrećete Bitcoin čvor (čak iako P2P Transport V2 otežava pasivno praćenje od strane provajdera (ISP-a)). Ovo nije nužno problem, ali ako želite da izbegnete bilo kakvo curenje ovih informacija, možete povezati svoj čvor isključivo putem Tor mreže.



Da bi bio upotpunosti omogućen Tor, potrebno je prisiliti Bitcoin Core da koristi samo ovu mrežu i da kreira skriveni servis za dolazne veze (ako želite da ih omogućite). U `bitcoin.conf`, potrebno je dodati ovu konfiguraciju:




- `onlynet=onion`,
- `proxy=127.0.0.1:9050`,
- `listenonion=1`,
- `torcontrol=127.0.0.1:9051`,
- `proxyrandomize=1`,
- `listen=1`,
- `bind=127.0.0.1`,
- `upnp=0`,
- `natpmp=0`.



Na taj način, sve vaše P2P konekcije prolaze kroz Tor, vaš čvor dobija `.onion` adresu za dolazne veze, nijedan port ne mora da bude otvoren na ruteru, vaš internet provajder vidi isključivo Tor saobraćaj, a vaši peer‑ovi ne znaju vašu javnu IP adresu. 


Ako želite da izbegnete svaku DNS rezoluciju u otvorenom (nešifrovanom) obliku, možete dodati `dnsseed=0` i `dns=0` u vašu konfiguraciju. Zatim ćete morati ručno da obezbedite `.onion` čvorove putem `seednode=` ili `addnode=`, jer će otkrivanje novih čvorova inače biti teško.



Očigledno, ako ste početnik, savetovao bih vam da za sada ostavite sva ova mrežna podešavanja na miru. Podrazumevana konfiguracija je često dovoljna.



### Mempool i politika releja



#### Osnovni parametri



Evo osnovnih parametara koje možete modifikovati u vašem `bitcoin.conf` fajlu u vezi sa upravljanjem vašim mempool-om i prosleđivanjem nepotvrđenih transakcija:





- `maxmempool=<n>`: Ograničava maksimalnu veličinu lokalnog mempool-a na `<n>` megabajta (podrazumevano: `300`). Kada se dostigne limit, vaš čvor dinamički povećava svoj efektivni prag naknade i daje prioritet najmanje profitabilnim transakcijama (na osnovu stope naknade, a ne apsolutne vrednosti) kako bi ostao ispod limita. Možete ostaviti ovo podešavanje kao podrazumevano. Povećanje može biti korisno ako rudarite samostalno, ili ako želite da dobijete tačniji prikaz zagušenja mempool-a i poboljšate procenu naknada. Suprotno tome, smanjenje će uštedeti RAM i, u manjoj meri, druge sistemske resurse.





- `mempoolexpiry=<n>`: Maksimalno vreme zadržavanja nepotvrđenih transakcija u mempool-u (u satima, podrazumevano: `336`). Nakon ovog vremena, transakcije se uklanjaju čak i ako ima dostupnog prostora.





- `persistmempool=1`: Čuva snimak mempool-a u stanju mirovanja i ponovo ga učitava pri ponovnom pokretanju (podrazumevano: `1`). Ovo ubrzava oporavak nakon ponovnog pokretanja, izbegavajući potrebu za ponovnim učenjem stanja putem mreže.





- `maxorphantx=<n>`: Maksimalan broj sačuvanih "siročadi transakcija" (transakcije čiji inputi zavise od UTXO‑ova koji još nisu viđeni u UTXO setu, podrazumevano: `100`). Preko ovog praga, najstarije transakcije se brišu kako bi se izbegao nekontrolisani rast keša.





- `blocksonly=1` : Onemogućava prihvatanje i prosleđivanje nepotvrđenih transakcija primljenih od peer‑ova (osim u slučaju posebnih dozvola). Čvor sada preuzima i objavljuje samo blokove. Transakcije kreirane lokalno i dalje se mogu slati (kako biste i dalje mogli koristiti čvor sa vašim softverom za novčanike). Ovo značajno smanjuje propusnost i zahteve za RAM‑om, ali smanjuje korisnost čvora za relej i dovodi do potpune nepoznanice o mempool‑u.




- `minrelaytxfee=<n>`: Minimalna stopa naknade (u BTC/kvB) ispod koje transakcije nisu prihvaćene u mempool čvora i ne prosleđuju se peer‑ovima.(podrazumevano: `0.00001` = 1 sat/vB). Što je ova vrednost viša, vaš čvor agresivnije filtrira transakcije niskih troškova.





- `mempoolfullrbf=1`: Prihvata RBF transakcije čak i bez eksplicitnog označavanja RBF u transakciji koja se zamenjuje. Sa ovom politikom, nazvanom "*full-RBF*", transakcija sa višom stopom naknade može zameniti drugu u mempool‑u ako su ispunjeni ostali uslovi za zamenu.



Kao podsetnik, RBF je transakcioni mehanizam koji omogućava pošiljaocu da zameni transakciju onom koja ima veće naknade kako bi ubrzao potvrdu. Ako transakcija sa preniskom naknadom ostane blokirana, pošiljalac može koristiti *Replace-by-fee* da poveća naknadu i prioritizuje svoju zamensku transakciju u mempool-ovima i kod rudara.



#### Napredna i specifična podešavanja



Evo su napredna podešavanja za mempool i politiku releja. Ako ste početnik, ne bi trebalo da menjate ova podešavanja:





- `datacarrier=1` : Dozvoljava prosleđivanje i (ako se rudari preko čvora) uključivanje transakcija koje nose nefinansijske podatke putem `OP_RETURN` izlaza (eng. output) (podrazumevano: `1`). Onemogućavanje ovog parametra blago smanjuje mogućnost spama nefinansijskim podacima, ali smanjuje kompatibilnost sa određenim upotrebama. U svakom slučaju, moraćete da prihvatite izrudarene `OP_RETURN`.





- `datacarriersize=<n>`: Maksimalna veličina (u bajtovima) `OP_RETURN` koju čvor prenosi (podrazumevano: `83`). Smanjenje ove vrednosti ograničava količinu podataka koja se može prenositi putem `OP_RETURN`. Napomena: podrazumevano, ovo ograničenje biće uklonjeno u jednoj od narednih verzija Bitcoin Core-a.




- `bytespersigop=<n>`: Parametar koji konvertuje operacije potpisivanja (signature operations) u ekvivalentne bajtove radi procene ograničenja releja (podrazumevano: `20`). Ovo će uticati na prihvatanje transakcija koje imaju veliki broj `sigops` prema lokalnim pravilima politike.





- `permitbaremultisig=1`: Dozvoljava relej transakcija bare-multisig P2MS. (tj. transakcije koje koriste Pay-to-Multi-Sig bez skrivenog P2SH omota, direktno u scriptPubKey) (podrazumevano: `1`). Ovo je najstariji skript šablon za uspostavljanje multisignature uslova na UTXO (izumljen 2011. od strane Gavina Andresena).





- `whitelistrelay=1`:Automatski dodeljuje dozvolu za relej peer‑ovima koji su stavljeni na whitelist (podrazumevano: `1`). Ovi peer‑ovi vide svoje transakcije prihvaćene za relej čak i ako vaš čvor nije u opštem režimu releja.





- `whitelistforcerelay=1`: Dodeljuje dozvolu "*forcerelay*" saa whitelist-e i podrazumevanim dozvolama (podrazumevano: `0`). Čvor tada relejuje njihove transakcije čak i ako su one već u mempool‑u, čime se zaobilaze mehanizmi protiv dupliranja.





- `whitebind=<[permissions@]addr>` / `whitelist=<[permissions@]CIDR>`: Povezuje interfejs ili opseg adresa i dodeljuje detaljne dozvole odgovarajućim peer‑ovima: `relay`, `forcerelay`, `mempool` ((zahtev za sadržajem mempool-a)), `noban`, `download`, `addr`, `bloomfilter`. Ovo može biti korisno za davanje privilegovanog tretmana pouzdanim peer-ovima (npr. gateway-ima, LAN-u, internim servisima…).





- `peerbloomfilters=1` : Omogućava podršku za Bloom filtere (BIP37) radi pružanja filtriranih blokova/transakcija laganim klijentima (podrazumevano: `0`). Pažnja, ovo povećava opterećenje na vaše resurse.





- `peerblockfilters=1` : Pruža kompaktne BIP157 (*Neutrino*) filtere peerovima (podrazumevano: `0`).





- `blockreconstructionextratxn=<n>`: Dodatni broj transakcija zadržanih u memoriji za rekonstrukciju kompaktnih blokova (podrazumevano: `100`). Poboljšava uspeh rekonstrukcija tokom kompaktnih sinhronizacija, uz cenu malo memorije.



Kao podsetnik, sva ova pravila releja nemaju uticaj na validnost transakcija uključenih u važeći blok. Ona služe za prilagođavanje vašeg doprinosa releju, zaštitu vaših resursa i čine vaš čvor predvidljivim u ograničenim okruženjima, ali nikada ne dozvoljavaju da odbijete blokove koji poštuju pravila konsenzusa.



### Novčanici



Takođe možete prilagoditi način na koji se vaši novčanici upravljaju u datoteci `bitcoin.conf`. Ako ne koristite direktno novčanik Core-a, već eksterni softver za upravljanje kao što su Sparrow ili Liana, ovi parametri će biti od male važnosti:





- `addresstype=<legacy|p2sh-segwit|bech32|bech32m>` : Definiše format adresa koje novčanik generiše za prijem.





- `changetype=<legacy|P2SH-SegWit|bech32|bech32m>`: Prisiljava korišćenje određenog formata adresa za kusur (eng. change), tj. ostatak sa inputa kod jednostavne transakcije.





- `Wallet=<path>`: Učitava postojeći novčanik pri pokretanju (može se ponoviti za učitavanje više novčanika).





- `walletdir=<dir>`: Direktorijum koji sadrži novčanike (podrazumevano: `<datadir>/wallets` ako postoji, u suprotnom `<datadir>`). Ovo može biti korisno ako želite da čuvate novčanike na određenom ili enkriptovanom volumenu.





- `walletbroadcast=1`: Automatski emituje transakcije kreirane od strane učitanih novčanika (podrazumevano: `1`). Postavite na `0` ako želite da upravljate emitovanjem putem drugog kanala.





- `walletrbf=1`: Omogućava opt-in RBF-a kako bi se RBF signalizirao na svim transakcijama. (podrazumevano: `1`). Omogućava vam da kasnije povećate naknade u slučaju blokirane transakcije u mempool-u.





- `txconfirmtarget=<n>`: Ciljni broj blokova za potvrdu transakcije (u broju blokova, podrazumevano: `6`). Novčanik će automatski postaviti naknadu za transakciju kako bi bila potvrđena unutar ovog broja blokova.





- `paytxfee=<amt>`: Fiksna stopa naknade (BTC/kvB) primenjena na novčanik transakcije. Generalno izbegavati: koristiti adaptivnu procenu putem `txconfirmtarget`.





- `fallbackfee=<amt>` : Rezervna naknada (BTC/kvB) koja se koristi ako procenitelj nema dovoljno podataka (podrazumevano: `0.00`). Postavljanje na 0 potpuno onemogućava rezervnu funkciju.





- `mintxfee=<amt>`: Minimalni prag (BTC/kvB) za novčanik da kreira transakcije (podrazumevano: `0.00001`). Wallet će odbiti da napravi transakciju ispod ovog praga.





- `maxtxfee=<amt>`: Apsolutni maksimum ukupnih naknada za transakciju iz novčanika (podrazumevano: `0.10` BTC). Štiti od neobično visokih naknada koje bi nepotrebno potrošile bitkoine.




- `avoidpartialspends=1`: Bira UTXO‑ove po grupama adresa kako bi se izbeglo delimično trošenje sredstava.




- `spendzeroconfchange=1`: Dozvoljava ponovnu upotrebu nepotvrđenog UTXO-a za kusur (eng. change) kao input u novoj transakciji. (podrazumevano: `1`).





- `consolidatefeerate=<amt>`: Maksimalna stopa (BTC/kvB) iznad koje novčanik izbegava dodavanje više ulaza nego što je potrebno za konsolidaciju. Ovo omogućava oportunističke konsolidacije po niskim cenama i smanjuje troškove kada su troškovi visoki.





- `maxapsfee=<n>`: Dodatni budžet za naknade (u BTC, apsolutna vrednost) koje novčanik pristaje da plati da bi aktivirao opciju "*izbegni delimična trošenja*".





- `discardfee=<amt>`: Stopa (u BTC/kvB) koja pokazuje vašu toleranciju da „žrtvujete“ kusur tako što ga dodajete u naknade. Output-i čije trošenje po ovoj stopi košta više od trećine njihove vrednosti se zanemaruju.





- `keypool=<n>`: Veličina rezervoara unapred generisanih adresa (podrazumevano: `1000`). Previše male vrednosti povećavaju rizik od nepotpunog obnavljanja novčanika.





- `disablewallet=1`: Pokreće Bitcoin Core bez podsistema za novčanik i onemogućava povezane RPC pozive. Time se smanjuje površina napada i potrošnja resursa ako čvor služi isključivo za validaciju i/ili relej.



### Skladištenje, indeksiranje i performanse



Fajl konfiguracije takođe vam omogućava da prilagodite parametre vezane za vaš uređaj. Ovo može biti posebno relevantno ako imate ograničene resurse, ili, naprotiv, veliku količinu dostupnog kapaciteta:





- `datadir=<dir>`: Postavlja glavni direktorijum podataka za Bitcoin Core.





- `blocksdir=<dir>`: Razdvaja lokaciju blok fajlova (`blocks/blk*.dat` i `blocks/rev*.dat`) od `datadir`. Ovo može biti korisno za postavljanje arhive blokova na drugi volumen, dok se osnovno stanje (`chainstate/`) drži na bržem medijumu, na primer.





- `dbcache=<n>`: Alocira `<n>` MiB za keš baze podataka (*LevelDB*) koje koriste indeks blokova i `chainstate` (podrazumevano: `450`). Što je veća vrednost, brži su IBD i trenutna validacija, uz cenu veće potrošnje RAM-a.





- `prune=<n>`: Omogućava orezivanje (pruning) fajlova sa blokovima i postavlja ciljnu količinu prostora na disku u MiB (podrazumevano: `0` = onemogućeno; `1` = ručno orezivanje putem RPC; `>=550` = automatsko orezivanje (pruning) ispod zadate ciljne vrednosti). Nekompatibilno sa `txindex=1`. Čvor ostaje potpuno validirajući čvor, ali više ne može da pruži stariju istoriju (stare blokove/transakcije). Ova opcija je posebno korisna ako je vaš prostor na disku ograničen, na primer, kada instalirate čvor na vašem kućnom računaru.





- `txindex=1` : Kreira i održava globalni indeks potvrđenih transakcija. Neophodno za određene upite (`getrawtransaction` za transakcije koje ne pripadaju vašem novčaniku) i za istraživačke svrhe, ali značajno povećava upotrebu diska. Nije kompatibilno sa režimom orezivanja.





- `assumevalid=<hex>`: Označava blok koji se smatra validnim, omogućavajući vam da preskočite provere skripti za njegove pretke (postavite `0` da proverite sve). Pogledajte prethodno poglavlje za više informacija.





- `reindex=1`: Rekonstruiše indekse blokova i stanje (`chainstate`) na osnovu `blk*.dat` fajlova koji se nalaze na disku. Takođe ponovo izgrađuje opcione aktivne indekse. Ovo je vremenski zahtevan proces koji se koristi za popravku oštećene baze podataka ili za čisto aktiviranje/deaktiviranje zahtevnih (teških) indeksa.





- `reindex-chainstate=1`: Ponovno izgrađuje samo `chainstate` iz trenutnog indeksa blokova. Preporučuje se kada su blok fajlovi ispravni.





- `blockfilterindex=<type>`: Održava indekse kompaktnih blok filtera (npr. `basic`) koje koriste lagani klijenti (BIP157/158) i neki RPC-ovi. Podrazumevano je onemogućeno (`0`). Troši dodatni prostor na disku i vreme za indeksiranje.





- `coinstatsindex=1`: Održava indeks statistika UTXO seta koji koristi RPC poziv `gettxoutsetinfo`. Korisno za revizije i metrike, eliminiše potrebu za skupim preračunavanjem. Onemogućeno po defaultu.





- `loadblock=<file>`: Prilikom pokretanja uvozi blokove iz eksternog `blk*.dat` fajla. Služi za predučitavanje (preload) istorije iz offline izvora (lokalna kopija, eksterni medij) kako bi se ubrzala inicijalizacija čvora.





- `par=<n>`: Postavlja broj niti (eng. threads) za verifikaciju skripte (od `-10` do `15`, `0` = automatski, `<0` = ostavlja ovaj broj jezgara slobodnim). Omogućava podešavanje CPU paralelizma tokom validacije transakcija i blokova. Automatski režim je obično dovoljan u većini slučajeva.





- `debuglogfile=<file>`: Specificira lokaciju `debug.log` fajla.





- `shrinkdebugfile=1`: Smanjuje veličinu `debug.log` fajla pri pokretanju (podrazumevano: `1` kada `-debug` nije aktivan).





- `settings=<file>`: Putanja do datoteke sa dinamičkim postavkama `settings.json`.



### RPC pristup i operativna sigurnost



Konačno, datoteka `bitcoin.conf` takođe vam omogućava da konfigurišete parametre pristupa za vaš čvor. Budite oprezni sa ovim postavkama, posebno ako ste tek počeli: izbegavajte njihovo menjanje bez potpunog razumevanja posledica, jer to može uvesti ranjivosti.





- `server=1`: Aktivira JSON-RPC server. Neophodno ako upravljate `bitcoind` putem `bitcoin-cli` ili aplikacije treće strane. Onemogućite (`0`) na čvoru koji isključivo vrši validaciju i ne izlaže nikakav API, ili već koristi Electrum server.





- `rpcbind=<addr>[:port]`: Adresa/port na kojem RPC server osluškuje. Podrazumevano, sluša se samo lokalno (`127.0.0.1` i `::1`). Ovaj parametar se ignoriše ako `rpcallowip` nije takođe definisan. Koristite ga da eksplicitno ograničite interfejs.





- `rpcport=<port>`: RPC port (default: `8332` na Mainnet, `18332` na Testnet, `38332` na bookmark, `18443` na regtest).





- `rpcallowip=<ip|cidr>`: Dozvoljava RPC klijentima sa određene IP adrese ili podmreže da se povežu na čvor (može se koristiti više puta za različite adrese/podmreže). Koristite u kombinaciji sa `rpcbind` da izložite API samo pouzdanom segmentu (LAN/VPN).





- `rpcauth=<USERNAME>:<SALT>$<Hash>`: Preporučeni RPC metod autentifikacije (heširana lozinka). Omogućava više unosa i izbegava čuvanje tajne u čistom tekstu.





- `rpccookiefile=<path>`: Putanja do kolačića za autentifikaciju (podrazumevano: `.cookie` datoteka u okviru `datadir/`). Ovo se koristi za lokalni pristup od strane istog korisnika bez upravljanja trajnim lozinkama. Na primer, možete ga koristiti za povezivanje Liana Wallet-a sa vašim Bitcoin Core-om na istom računaru.





- `rpcuser=<user>` / `rpcpassword=<pw>`: Klasična RPC autentifikacija sa lozinkom u običnom tekstu. Treba izbegavati i koristiti umesto toga `rpcauth` ili cookie autentifikaciju. 





- `rpcthreads=<n>`: Broj niti za opsluživanje RPC poziva (podrazumevano: `4`). Povećajte ovu vrednost ako imate velike skokove u broju poziva sa strane monitoring sistema ili spoljnog alata.





- `rpcwhitelist=<USERNAME>:<rpc1>,<rpc2>,...`: Lista dozvoljenih API-ja. Smanjuje površinu napada ograničavanjem dostupnih metoda.





- `rpcwhitelistdefault=1|0`: Podrazumevano ponašanje whitelist lista: ako je omogućena i koristi se whitelist, pozivi koji nisu na listi se odbijaju. Takođe, može podrazumevano primorati praznu listu (nijedan poziv nije dozvoljen) dok se nešto eksplicitno ne doda na listu.




- `rest=1`: Omogući javni REST API (podrazumevano onemogućen). Treba da bude izložen samo na pouzdanoj mreži (ista opreznost kao kod JSON-RPC).





- `conf=<file>`: Specifikuje, samo preko komandne linije, fajl konfiguracije koji se učitava samo za čitanje. Korisno za zamrzavanje izvršnog profila (nepromenljiv) sa operativne strane.





- `includeconf=<file>`: Učitava dodatni konfiguracioni fajl (putanja relativna u odnosu na `datadir/`). Omogućava razdvajanje uloga: zajednička baza + lokalna osetljiva prepiska (override).





- `daemon=1` / `daemonwait=1`: Pokreće `bitcoind` u pozadini i, sa `daemonwait`, čeka da se inicijalizacija završi pre nego što preda kontrolu. Ovo olakšava integraciju sa nadzornicima (systemd, runit).





- `pid=<file>`: Lokacija PID datoteke.





- `sandbox=<log-and-abort|abort>`: Omogućava eksperimentalno sandboxovanje sistemskih poziva (syscalls): dozvoljeni su samo očekivani syscalls.





- `startupnotify=<cmd>` / `shutdownnotify=<cmd>`: Izvršava komandu pri pokretanju ili gašenju.





- `alertnotify=<cmd>`: Pokreće komandu pri prijemu upozorenja.





- `blocknotify=<cmd>`: Izvršava komandu za svaki novi blok.





- `debug=<category>|1` / `debugexclude=<category>`: Omogućava/onemogućava detaljne kategorije logova (npr. `net`, `Mempool`, `RPC`, `validation`...).





- `logips=1`: Beleži IP adrese.





- `logsourcelocations=1` / `logthreadnames=1` / `logtimestamps=1`: Dodaje lokacije izvora, imena niti i precizne vremenske oznake u logove, respektivno.





- `printtoconsole=1`: Šalje trace/debug poruke na konzolu (*stdout*).





- `help-debug=1`: Prikazuje pomoć za debug opcije i zatim izlazi iz programa.





- `uacomment=<cmt>`: Dodaje komentar u P2P User-Agent. (Tj. omogućava da čvor u svom identifikatoru P2P protokola uključi dodatnu napomenu ili oznaku.)



Sada smo završili sa nabrajanjem većine parametara konfiguracije. Ovaj `bitcoin.conf` fajl stoga predstavlja pravu komandnu tablu vašeg čvora: definiše mrežnu konfiguraciju, upravljanje mempool-om, korišćenje diska i memorije, indeksiranje i opštu administraciju. Ako želite da saznate više o ovom fajlu i kreirate jedan prilagođen vašim potrebama, preporučujem korišćenje [Jameson Lopp-ovog generatora](https://jlopp.github.io/Bitcoin-core-config-generator/).



Došli smo do zaključka ovog BTC 202 kursa, koji će vam omogućiti ne samo da razumete osnove kako čvorovi funkcionišu i kako međusobno deluju unutar sistema, već i da postavite svoj sopstveni. Sada ste suvereni Bitcoiner, sa sopstvenim samostalnim čuvanjem novčanika, emitujući svoje transakcije putem svog čvora. Čestitamo!



Sada možete preći na poslednji deo kursa, gde ćete moći da ocenite BTC 202, a zatim uzmete svoju diplomu da proverite da li ste savladali sve obuhvaćene koncepte.



Sada vam se otvara više puteva. Sledeći logičan korak jeste postavljanje sopstvenog Lightning čvora, kako biste bili potpuno nezavisni za svoje off-chain transakcije. Upravo je to tema još jednog kursa na Plan ₿ Academy:



https://planb.academy/courses/593e483e-1785-4e83-aa7e-32b99056844c

Pozivam vas takođe da otkrijete obuku BTC 204, koja će vam omogućiti da razumete i savladate principe zaštite privatnosti u vašem korišćenju Bitcoina:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c


# Finalni deo


<partId>679169f5-b990-47e1-9a00-45098ba8096b</partId>





## Recenzije i Ocene


<chapterId>c18f672d-1074-427e-9505-eecd7ae43e71</chapterId>




<isCourseReview>true</isCourseReview>


## Završni ispit


<chapterId>a4c97701-996c-4cc5-81fa-37d2dc4ee856</chapterId>




<isCourseExam>true</isCourseExam>


## Zaključak


<chapterId>28c5cf1f-7b9c-4b68-8b8f-eee109629764</chapterId>




<isCourseConclusion>true</isCourseConclusion>
