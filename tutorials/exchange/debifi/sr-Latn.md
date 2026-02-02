---
name: Debifi
description: Dobijte nekustodijalni zajam garantovan od strane Bitcoin.
---

![cover](assets/cover.webp)




## Uvod



Već vekovima, tradicionalno kreditiranje omogućava finansiranje mnogih projekata. Međutim, ono ostaje sporo, skupo i nedovoljno inkluzivno, posebno za one koji nemaju pristup solidnoj bankarskoj infrastrukturi.



Uspon protokola Bitcoin označio je početak nove finansijske ere, donoseći sa sobom niz izazova. Jedan od tih izazova bio je kako obezbediti likvidnost bez potrebe za prodajom Bitcoin, čime bi se izgubila izloženost njegovom potencijalu rasta.



Rezultat je **Debifi**, platforma koja se pozicionira kao moderna alternativa bankama. Cilj je jasan: učiniti kredit što jednostavnijim i transparentnijim, kombinovanjem prednosti tradicionalnog finansijskog sistema sa slobodom koju nudi Bitcoin. Ime Debifi odražava ovu viziju: ***Decentralizovana Bitcoin Finansija***, kontrakcija koja ilustruje susret decentralizovane finansije i Bitcoin inovacije.



Debifi je nekustodijalna platforma za pozajmljivanje podržana Bitcoin, što znači da zadržavate kontrolu nad svojim privatnim ključevima. Omogućava korisnicima da otključaju likvidnost u zamenu za svoje zaključane bitkoine kao kolateral. Za razliku od tradicionalnih bankarskih kredita, Debifi koristi sistem eskrouta sa više potpisa (3 od 4) i ne prihvata rehypotekaciju kolaterala, garantujući veću sigurnost i transparentnost.



U praksi, ovo znači da ni Debifi ni pojedinačni zajmodavac ne mogu potrošiti vaš BTC bez saglasnosti tri strane (vas, zajmodavca i pouzdane treće strane). Ovo čini sistem sigurnijim: ako pozajmljujete na Debifi, zadržavate vlasništvo nad vašim Bitcoin sve dok zajam ne bude u potpunosti otplaćen.



## Prednosti Debifi



Sa Debifi, dobijate Bitcoin podržane zajmove koji su prekomerno obezbeđeni i osigurani on-chain. Vaša sredstva ostaju sigurna uz multisignature novčanike, 2FA i potpunu kontrolu nad vašim Bitcoin — vi držite svoje ključeve, vi čuvate svoje novčiće. Pozajmljujte u nizu stabilnih kovanica ili fiat opcija, po konkurentnim stopama i globalnoj likvidnosti.



Evo brze uporedbe između Debifi kredita i tradicionalnog bankarskog kredita:


| Characteristics        | Loan via Debifi                                                        | Traditional Bank Loan                                                       |
| ---------------------- | ----------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| Accessibility          | ✔️ Open to any Bitcoin holder (even without banking history)           | ❌ Often limited to clients with physical collateral and strong records      |
| Speed of approval      | ✔️ Funds available within minutes or hours                             | ❌ Lengthy process (days or weeks)                                           |
| Required guarantees    | ✔️ Bitcoin used as the sole collateral                                 | ❌ Physical guarantees (property, land, stable income)                       |
| Asset control          | ✔️ You keep exposure to Bitcoin and its upside potential               | ❌ No connection between the loan and your financial assets                  |
| Geographic flexibility | ✔️ Available everywhere (no banking jurisdiction constraints)          | ❌ Restricted to the bank’s jurisdiction                                     |
| Main risk              | ❌ Liquidation risk if BTC price drops too sharply                      | ❌ Risk of asset seizure or negative impact on credit score                  |

Pre nego što vam pokažem korak po korak kako da pozajmite na Debifi, postoji nekoliko stvari koje mislim da treba da znate.




## Definicije





- Naknade za odobravanje kredita** su jednokratne naknade koje se naplaćuju prilikom odobravanja kredita i izračunavaju se kao procenat iznosa pozajmice. Ove naknade pokrivaju administrativne, operativne i troškove upravljanja.





- Kolateral** je imovina koju deponujete da biste osigurali zajam. U slučaju Debifi-ja, kolateral je Bitcoin (BTC), koji zajmoprimac deponuje u Multisig 3/4 eskrou.





- Multisig escrow (3/4)** sistem je siguran mehanizam depozita gde se bitkoini zajmoprimca smeštaju na adresu sa više potpisa. Konkretno, četiri (4) strane poseduju ključ (zajmoprimac, zajmodavac, Debifi, nezavisna treća strana). Za premeštanje sredstava, potrebna su najmanje 3 od 4 potpisa.





- Stablecoin** je kriptovaluta čija je vrednost vezana za stabilnu imovinu (npr. američki dolar), što izbegava volatilnost Bitcoin. Na primer, 1 USDC uvek vredi ~$1, jer je podržan fiat rezervama.





- Odnos zajma prema vrednosti (LTV)** određuje koliko gotovine možete pozajmiti kao zalog za vaš Bitcoin. LTV odnos = Iznos zajma / Iznos zaloga * 100. Na primer, LTV od 50% znači da je vrednost zajma jednaka 50% vrednosti deponovanog Bitcoin.




BTC Sessions video tutorijal :



![Vidéo tutoriel de BTC Sessions](https://youtu.be/02gzg-en8n0)



## Početak sa Debifi



Da biste započeli sa Debifi, biće vam potrebno nekoliko preduslova.


### Preduslovi



Pre nego što možete da pozajmite od Debifi, molimo vas da se uverite da imate sledeće stavke:





- Bitcoin wallet: gde držite svoj BTC (idealno ne-kustodijalni, npr. Hardware Wallet ili pouzdani mobilni wallet). Iz ovog wallet ćete poslati Bitcoin kolateral na Debifi i primiti kolateral nazad.



Možete koristiti Aqua, Bitcoin i Liquid wallet koji takođe podržavaju upravljanje USDT stablecoin-om na različitim mrežama. Ili COLDCARD (Mk4 ili Q), trenutno jedini hardver koji podržava Debifi.



https://planb.academy/tutorials/wallet/mobile/aqua-8e6d7dd3-8c03-45cc-90dd-fe3899a7d125

https://planb.academy/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3



- KYC (*Know Your Customer*): u zavisnosti od izabrane ponude zajma, može biti potreban proces verifikacije identiteta. Na Debifi, svaka ponuda pokazuje da li je KYC potreban ili ne. Stoga se pripremite u skladu s tim. KYC sprovode pouzdani pružaoci usluga trećih strana kao što je Sumsub.



![image](assets/fr/03.webp)





- Aplikacija za dvofaktorsku autentifikaciju: Debifi zahteva Authenticator kod za svaku važnu radnju. To je dodatni sloj sigurnosti. U ovom uputstvu koristićemo Google Authenticator. Alternativno, možete koristiti druge po želji.



https://planb.academy/tutorials/computer-security/authentication/proton-authenticator-047ca2eb-a922-4e0e-8f75-1b89d23951ae

https://planb.academy/tutorials/computer-security/authentication/aegis-authenticator-22cc4d35-fb46-4e54-8833-bc4b411518bc



- Debifi vebsajt i mobilna aplikacija: Debifi je i vebsajt i mobilna aplikacija, i oba rade u tandemu. Mobilna aplikacija postaje wallet, koji čuva vaš privatni ključ i upravlja potpisivanjem ugovora. Pored toga, potrebno je koristiti vebsajt za sklapanje ugovora (veliki Interface vam daje opšti pregled ugovora o zajmu i njihove specifičnosti).





- Mobilna aplikacija Debifi (iOS/Android) je potrebna za uzimanje kredita. Morate preuzeti aplikaciju, kreirati nalog i "povezati" svoj uređaj (registrovati uređaj na svoj nalog). Aplikacija Debifi podržava dvofaktorsku autentifikaciju (2FA) i bez pametnog telefona ne možete potvrditi transakcije na Debifi.



### Kreiraj nalog



Posetite [Debifijevu zvaničnu veb stranicu](https://debifi.com/app).



![image](assets/fr/04.webp)



Instalirajte svoju aplikaciju prema vrsti pametnog telefona koji imate, a zatim je otvorite.



![image](assets/fr/05.webp)



![image](assets/fr/06.webp)



Jednom u aplikaciji, kliknite na meni **Settings**.



![image](assets/fr/07.webp)



Zatim kliknite na **Prijavi se ili kreiraj nalog** da biste kreirali nalog sa svojom e-mail adresom.



![image](assets/fr/08.webp)



![image](assets/fr/09.webp)



![image](assets/fr/10.webp)



Dobićete verifikacioni kod putem e-pošte. Kopirajte i nalepite ovaj kod u aplikaciju. Zatim otvorite Debifi aplikaciju na svom pametnom telefonu i prijavite se.



![image](assets/fr/11.webp)



### Osiguravanje vašeg naloga



Radi bezbednosti, Debifi će vas zamoliti da pratite tri koraka.



![image](assets/fr/12.webp)





- Prvo, treba da postavite jak PIN kod kako biste kasnije pristupili svojoj aplikaciji.



![image](assets/fr/13.webp)





- Zatim postavite dvofaktorsku autentifikaciju (2FA) da povežete svoj uređaj sa svojim nalogom koristeći 2FA kod.



![image](assets/fr/14.webp)





- Na kraju, sačuvajte 12 reči vašeg privatnog ključa tako što ćete ih zapisati na pouzdan medijum i čuvati na sigurnom mestu. Ova faza je ključna za oporavak vašeg naloga i upravljanje vašim sredstvima.



![image](assets/fr/15.webp)





- Za dodatnu sigurnost, možete čak dodati passphrase.



![image](assets/fr/16.webp)



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Imajte na umu da će samo vaš registrovani pametni telefon moći da otvori vaš nalog (dodatna sigurnosna mera).



Kada završite ove korake, kliknite na meni **Ponude** da biste videli dostupne ponude za zajam. Kada kliknete na ponudu, bićete preusmereni na veb-sajt Debifi.



![image](assets/fr/17.webp)



### Pristupite vebsajtu i istražite ponude za kredite



Kada je vaš uređaj povezan, idite na [Debifi website](https://debifi.com/). Prijavite se kako biste uspostavili sigurnu vezu između Debifi mobilne aplikacije i web platforme. Ovo vam olakšava interakciju sa dostupnim ponudama zajmova (jasan pregled detalja svake ponude) i upravljanje vašim nalogom.



![image](assets/fr/18.webp)



![image](assets/fr/19.webp)



![image](assets/fr/20.webp)



![image](assets/fr/21.webp)




Video tutorijal o tome kako se prijaviti sa svojim nalogom na platformu :



![video](https://youtu.be/cUwCfTKDAOo)



## Zahtev za kredit



Platforma vas povezuje sa likvidnošću institucionalnog kvaliteta i nudi niz opcija koje odgovaraju vašim potrebama. Pregledajte da biste saznali šta je dostupno. Takođe imate fleksibilnost da prilagodite parametre zajma prema vašoj individualnoj toleranciji rizika i finansijskoj situaciji.



![image](assets/fr/22.webp)



Fiat valute koje Debifi trenutno nudi mogu se pogledati na platformi.



![image](assets/fr/23.webp)



### Jasne, fleksibilne ugovorne klauzule



Debifi se oslanja na transparentne i fleksibilne uslove zajma kako bi zadovoljio potrebe svake strane (zajmodavca i zajmoprimca). Ključne klauzule uključuju :



#### Odnos kredita prema vrednosti (LTV)


Bitcoin tranše zajma su generalno tri (3) po broju:





- Konzervativno (30% - 40% LTV), što odgovara zajmu niskog rizika, idealno je za maksimiziranje sigurnosti protiv volatilnosti cena Bitcoin;





- Balanced (50% LTV) ;





- Agresivno (70% LTV), koje nudi veću likvidnost, ali nosi vrlo visok rizik od likvidacije tokom tržišnih padova. Aktivno praćenje uslova Bitcoin tržišta je obavezno prilikom odabira ove tranše.



#### Kamate



Postavljanje kamatnih stopa generalno zavisi od izabranog LTV-a, dužine trajanja zajma, volatilnosti kolaterala i procene rizika specifične za platformu. Stope ostaju fiksne tokom trajanja zajma.



#### Rok otplate i fleksibilnost otplate



Rasporedi otplate su fleksibilni i dizajnirani da odgovaraju potrebama zajmoprimca. Zajmovi se mogu u potpunosti ili delimično otplatiti u bilo kom trenutku bez dodatnih naknada, pod uslovom da su zahtevi za kolateralom ispunjeni. Tokom trajanja zajma, kamata se obično plaća periodično, dok se glavnica izmiruje na dospeću.



#### Prava likvidacije (Margin pozivi)



S obzirom na volatilnost Bitcoin, zajmovi uključuju jasno definisanu politiku margin poziva. Margin poziv se dešava kada LTV poraste zbog pada vrednosti kolaterala. Debifi obaveštava zajmoprimca putem e-pošte i kroz aplikaciju, omogućavajući im da dodaju kolateral ili otplate deo zajma.


75% LTV — Prvo upozorenje

80% LTV — Drugo upozorenje

85% LTV — Konačno upozorenje

90% LTV — Kolateral je likvidiran



### Pokretanje procesa zajma



Da biste odabrali ponudu kredita koja odgovara vašim potrebama, kliknite na nju da biste videli njene karakteristike.



![image](assets/fr/24.webp)



Možete videti :


1. Naziv kreditne institucije ;


2. Raspon iznosa zajma;


3. Da ćete primiti sredstva u USDC Ethereum ;


4. Period otplate, kamatna stopa i LTV odnos;


5. KYC je potreban za ovu ponudu;


6. Tačan iznos koji vam je potreban mora biti unet (ovaj iznos mora biti unutar opsega, vidi 2);


7. Ethereum USDC adresa koja će se koristiti za primanje sredstava mora biti uneta.



Kada budete zadovoljni ponudom i popunite potrebne informacije, kliknite na "Contract request".



![image](assets/fr/25.webp)



Vratite se na mobilnu aplikaciju za ''**Provide public key**''.



![image](assets/fr/26.webp)



Pritisnite '' **Provide public key** '', zatim izaberite izvor javnog ključa. Zajmodavac će takođe morati da obezbedi javni ključ.



![image](assets/fr/27.webp)



![image](assets/fr/28.webp)



![image](assets/fr/29.webp)



![image](assets/fr/30.webp)



Sledeći korak je potpisivanje ugovora. Još uvek u mobilnoj aplikaciji, pritisnite '' **Sign Contract** ''



![image](assets/fr/31.webp)



![image](assets/fr/32.webp)



Kada završite sa potpisivanjem ugovora, Debifi automatski kreira jedinstvenu multi-potpisnu Bitcoin adresu (escrow 3-sur-4) za vaš ugovor. Dokle god su vaši bitkoini u escrow-u, ne mogu se koristiti na drugom mestu.



### Depozit garancije i prijem vaših sredstava



Poslednji korak je da položite svoj Bitcoin kolateral u sistem skrbništva sa više potpisa. Debifi vam prikazuje adresu skrbništva (B) i količinu BTC (A) koja treba biti poslata kao (kolateral + provizija).



![image](assets/fr/33.webp)



Takođe ćete primiti ovu obaveštenje u vašoj mobilnoj aplikaciji.



![image](assets/fr/34.webp)



Čim vaš depozit bude potvrđen, zajmodavac će isplatiti iznos zajma na adresu primatelja koju ste naveli, čime će se transakcija finalizirati i omogućiti vam pristup potrebnim sredstvima.



Zatim ćete primiti obaveštenje od Debifi, koje će vas tražiti da platite naknade za zajam ili provizije kako biste unapredili status vašeg zajma.



U stvarnosti, kada je ugovor kreiran, naknade za zajam se automatski odbijaju od kolaterala koji je deponentirao zajmoprimac na adresi depozita sa više potpisa.



Sve što treba da uradite je da potpišete transakciju koja će omogućiti Debifi-ju da odbije svoju proviziju od garancije. Sa svoje strane, vaš zajmodavac će takođe morati da potpiše transakciju za odbijanje provizije, inače Debifi neće moći da primi svoju proviziju.



![image](assets/fr/35.webp)



Primjenjive naknade za pozajmljivanje su 1.5-2%, u zavisnosti od trajanja ugovora. Platforma naplaćuje provizije samo u Bitcoin.



## Praćenje zajma



Jednom kada je zajam aktivan, Debifi vam omogućava praćenje vašeg ugovora u realnom vremenu. U interfejsu ćete pronaći:



- Iznos pozajmljenog novca i preostali rok.
- Trenutni LTV (Loan-to-Value) odnos, koji raste kada cena BTC opada i vrednost vašeg kolaterala pada.




Zajmoprimci su obavešteni kada se vrednost kolaterala smanji, a ove informacije su takođe prikazane na stranici sažetka ugovora. Da bi se povratio originalni odnos zajma prema vrednosti, zajmoprimac mora ili:



- deponovati dodatni kolateral;
- otplatiti ceo ili deo duga.




U slučaju povećanja cene kolaterala, zajmoprimac zadržava sve kapitalne dobitke na kolateralu. On duguje samo iznos zajma, koji je unapred određen i nezavisan od cene Bitcoin.




## Otplata i povraćaj kolaterala



Na kraju dogovorenog roka (ili ranije, ako želite), morate vratiti zajam.


U Debifiju :





- Idite na svoj ugovor i kliknite na **Izvrši uplatu**. Unesite ukupan iznos duga (glavnica + kamata).





- Pošaljite stablecoine sa vašeg wallet na navedenu adresu zajmodavca, i vratite se da potvrdite otplatu na platformi kopiranjem **ID**-a transakcije otplate u posvećenu karticu. Ovo olakšava Debifi-ju da izvrši svoje provere.



Kada uplata bude potvrđena od strane zajmodavca (i od vas), Debifi će vas zatim zamoliti da **refundirate**. Vaš Bitcoin kolateral će biti oslobođen i možete ga vratiti iz escrow-a na vaš sopstveni wallet. Ne zaboravite da pokupite sve vaše Bitcoine.



Čim primite svoje bitkoine, ugovor o zajmu se menja u **Contract completed**.



Čestitamo! Završili ste proces.




## Najbolje prakse i bezbednost



Bez obzira na vaše ciljeve ili motive—finansiranje projekta, sticanje nekretnine, kupovina bitkoina, itd.—budite veoma oprezni pre nego što uzmete zajam podržan Bitcoin. Odvojite vreme da pažljivo procenite svoju odluku, jer Bitcoin ostaje nestabilna imovina. **Oštar pad njegove cene mogao bi rezultirati prinudnom likvidacijom vaših bitkoina.**



Pratite svoj odnos zajma i kolaterala (LTV). Postavite upozorenja (cena BTC, LTV) ako je moguće. Ne dozvolite da vaš odnos priđe 90%. Ako ste u nedoumici, povećajte kolateral ili vratite zajam ranije.



Kontrolišite svoje ključeve. Držite svoj BTC u sigurnom wallet (idealno hardverskom ili renomiranom wallet). Nemojte postavljati PIN kod povezan sa važnim datumom u vašem životu i nikada ne delite svoju frazu za oporavak. Na Debifi, vi generate svoj privatni ključ u aplikaciji - Debifi ga ne zna.



Počnite sa malim iznosom ako je moguće. Za vaš prvi zajam, testirajte skroman iznos kako biste se upoznali sa procesom.



Koristite samo zvaničnu Debifi veb stranicu da biste bili u toku sa vestima o Debifi, i izbegavajte nepoznate ili phishing linkove. Ažurirajte aplikaciju, zaštitite svoj pametni telefon PIN kodom, i izaberite kompatibilan Hardware Wallet.



Alternativno, ako ste zajmodavac, ovaj video vodič će vas voditi kroz korišćenje Debifi platforme. Od odabira zajmoprimaca zainteresovanih za vašu ponudu, do pružanja javnih ključeva, potpisivanja ugovora, prenosa stablecoina i još mnogo toga.



![video](https://youtu.be/g8iLxwI4xT0)



Sada znate kako koristiti Debifi platformu za dobivanje zajma.



Preporučujem da pohađate ovaj kurs, koji detaljno razmatra Bitcoin, stabilne kovanice i njihov doprinos suverenitetu.



https://planb.academy/courses/fdc41e06-ea63-4bf0-a5ac-a0185fe30e46