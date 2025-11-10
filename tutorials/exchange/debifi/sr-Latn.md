---
name: Debifi
description: Dobijte nekustodijalni zajam garantovan od strane Bitcoin.
---

![cover](assets/cover.webp)




## Uvod



Već vekovima, tradicionalno kreditiranje omogućava finansiranje mnogih projekata. Međutim, ono ostaje sporo, skupo i nije baš inkluzivno, posebno za one koji nemaju pristup solidnoj bankarskoj infrastrukturi.



Uspon Bitcoin protokola označio je početak nove finansijske ere, donoseći sa sobom niz izazova. Jedan od tih izazova bio je kako obezbediti likvidnost bez potrebe za prodajom Bitcoin, čime bi se izgubila izloženost njegovom potencijalu rasta.



Rezultat je **Debifi**, platforma koja se pozicionira kao moderna alternativa bankama. Cilj je jasan: učiniti kredit što jednostavnijim i transparentnijim, kombinovanjem prednosti tradicionalnog finansijskog sistema sa slobodom koju nudi Bitcoin. Ime Debifi odražava ovu viziju: ***Decentralizovana Bitcoin Finansija***, kontrakcija koja ilustruje susret decentralizovane finansije i Bitcoin inovacije.



Debifi je platforma za pozajmljivanje podržana Bitcoin bez starateljstva, što znači da zadržavate kontrolu nad svojim privatnim ključevima. Omogućava korisnicima da otključaju likvidnost u Exchange za svoje zaključane bitkoine kao zalog. Za razliku od tradicionalnih bankarskih kredita, Debifi koristi sistem eskrouta sa više potpisa (3 od 4) i ne prihvata zalaganje kolaterala, garantujući veću sigurnost i transparentnost.



U praksi, to znači da ni Debifi ni pojedinačni zajmodavac ne mogu potrošiti vaš BTC bez saglasnosti tri strane (vas, zajmodavca i pouzdane treće strane). Ovo čini sistem sigurnijim: ako pozajmite na Debifi, zadržavate Ownership svog Bitcoin dok zajam ne bude u potpunosti otplaćen.



## Prednosti Debifi



Sa Debifi, to su zajmovi sa kolateralom, Blockchain sigurnost (multisignature, 2FA), izbor stabilnih valuta/likvidnosti, poverljivost i totalna Bitcoin kontrola. Debifi "vam omogućava da zadržite svoj novac" (vaši ključevi, vaši novčići), dok nudi konkurentne stope i globalni pristup zajmovima podržanim BTC-om.



Evo brze uporedbe između Debifi kredita i tradicionalnog bankarskog kredita:



| Caractéristiques       | Prêt via Debifi                                                       | Prêt bancaire traditionnel                                                 |
| ---------------------- | --------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| Accessibilité          | ✔️ Ouvert à tout détenteur de Bitcoin (même sans historique bancaire) | ❌ Souvent réservé aux clients avec garanties physiques et dossiers solides |
| Vitesse d’obtention    | ✔️ Liquide en quelques minutes/heures                                 | ❌ Processus long (jours ou semaines)                                       |
| Garanties exigées      | ✔️ Collatéral en Bitcoin uniquement                                   | ❌ Garanties physiques (maisons, terrains, revenus stables)                 |
| Contrôle de l’actif    | ✔️ Vous conservez l’exposition au Bitcoin et son potentiel de hausse  | ❌ Vous n’avez aucun lien entre le prêt et vos actifs financiers            |
| Souplesse géographique | ✔️ Disponible partout (sans contrainte géographique bancaire)         | ❌ Limité à la juridiction de la banque                                     |
| Risque principal       | ❌ Risque de liquidation si le prix du BTC chute trop                  | ❌ Risque de saisie de biens ou impact négatif sur la cote de crédit        |

Pre nego što vam pokažem korak po korak kako da pozajmite na Debifi, postoji nekoliko stvari koje mislim da treba da znate.




## Definicije





- Naknade za odobravanje** su jednokratne naknade koje se naplaćuju prilikom odobravanja zajma i izračunavaju se kao procenat iznosa pozajmice. Ove naknade pokrivaju administrativne, operativne i troškove upravljanja.





- Kolateral** je imovina koju deponujete da biste osigurali zajam. U slučaju Debifi-ja, kolateral je Bitcoin (BTC), koji zajmoprimac deponuje u Multisig 3/4 eskrou.





- Sistem Multisig escrow (3/4)** je siguran mehanizam depozita gde se bitkoini zajmoprimca smeštaju u multi-potpis Address. Konkretno, četiri (4) strane poseduju ključ (zajmoprimac, zajmodavac, Debifi, nezavisna treća strana). Za premeštanje sredstava, potrebna su najmanje 3 od 4 potpisa.





- Stablecoin** je kriptovaluta čija je vrednost vezana za stabilnu imovinu (npr. američki dolar), što izbegava volatilnost Bitcoin. Na primer, 1 USDC uvek vredi ~$1, jer je podržan fiat rezervama.





- Odnos zajma prema vrednosti (LTV)** određuje koliko gotovine možete pozajmiti kao zalog za vaš Bitcoin. LTV odnos = Iznos zajma / Iznos zaloga * 100. Na primer, LTV od 50% znači da je vrednost zajma jednaka 50% vrednosti deponovanog Bitcoin.




BTC Sessions video tutorijal :



![Vidéo tutoriel de BTC Sessions](https://youtu.be/02gzg-en8n0)



## Početak sa Debifi



Da biste započeli sa Debifi, biće vam potrebno nekoliko preduslova.


### Preduslovi



Pre nego što možete pozajmiti od Debifi, molimo vas da se uverite da imate sledeće stavke:





- Bitcoin Wallet: gde držite svoj BTC (idealno ne-kustodijalni, npr. Hardware Wallet ili pouzdani mobilni Wallet). Iz ovog Wallet ćete poslati Bitcoin kolateral na Debifi i primiti sredstva.





- Stablecoins ili fiat: Debifi pozajmljuje u stablecoinima i nekim fiat valutama. Glavni korišćeni stablecoini su USDT i USDC.



Možete koristiti Aqua, Bitcoin i Liquid Wallet koji takođe podržava upravljanje USDT stablecoin-om na različitim mrežama. Ili COLDCARD (Mk4 ili Q), trenutno jedini hardver koji podržava Debifi.



https://planb.academy/tutorials/wallet/mobile/aqua-8e6d7dd3-8c03-45cc-90dd-fe3899a7d125

https://planb.academy/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3



- KYC (*Know Your Customer*): u zavisnosti od izabrane ponude zajma, može biti potreban proces verifikacije identiteta. Na Debifi, svaka ponuda označava da li je KYC potreban ili ne. Stoga se pripremite u skladu s tim. KYC sprovode pouzdani pružaoci usluga trećih strana kao što je Sumsub.



![image](assets/fr/03.webp)





- Aplikacija za dvofaktorsku autentifikaciju: Debifi zahteva Authenticator kod za svaku važnu radnju. To je dodatni Layer nivo sigurnosti. U ovom vodiču koristićemo Google Authenticator. Alternativno, možete koristiti druge po želji.



https://planb.academy/tutorials/computer-security/authentication/proton-authenticator-047ca2eb-a922-4e0e-8f75-1b89d23951ae

https://planb.academy/tutorials/computer-security/authentication/aegis-authenticator-22cc4d35-fb46-4e54-8833-bc4b411518bc



- Debifi vebsajt i mobilna aplikacija: Debifi je i vebsajt i mobilna aplikacija, i oba rade u tandemu. Mobilna aplikacija postaje Wallet, koja čuva vaš privatni ključ i upravlja potpisivanjem ugovora. Pored toga, potrebno je koristiti vebsajt za sklapanje ugovora (veliki Interface vam daje opšti pregled ugovora o zajmu i njihove specifičnosti).





- Mobilna aplikacija Debifi (iOS/Android) je potrebna za uzimanje kredita. Morate preuzeti aplikaciju, kreirati nalog i "povezati" svoj uređaj (registrovati uređaj na svoj nalog). Aplikacija Debifi podržava dvofaktorsku autentifikaciju (2FA) i bez pametnog telefona ne možete potvrditi transakcije na Debifi.



### Kreiraj nalog



Posetite [Debifijevu zvaničnu veb stranicu](https://debifi.com/app).



![image](assets/fr/04.webp)



Instalirajte svoju aplikaciju prema vrsti pametnog telefona koji imate, a zatim je otvorite.



![image](assets/fr/05.webp)



![image](assets/fr/06.webp)



Jednom u aplikaciji, kliknite na meni **Settings**.



![image](assets/fr/07.webp)



Zatim kliknite na **Prijavi se ili kreiraj nalog** da biste kreirali nalog sa vašim e-mailom Address.



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



Kada završite ove korake, kliknite na meni **Ponude** da biste videli dostupne ponude za zajam. Kada kliknete na ponudu, ona vas preusmerava na veb-sajt Debifi.



![image](assets/fr/17.webp)



### Pristupite veb-sajtu i istražite ponude za zajam



Kada je vaš uređaj povezan, idite na [Debifi website](https://debifi.com/). Prijavite se kako biste uspostavili sigurnu vezu između Debifi mobilne aplikacije i web platforme. Ovo vam olakšava interakciju sa dostupnim ponudama zajmova (jasan pregled detalja svake ponude) i upravljanje vašim nalogom.



![image](assets/fr/18.webp)



![image](assets/fr/19.webp)



![image](assets/fr/20.webp)



![image](assets/fr/21.webp)




Video tutorijal o tome kako se prijaviti sa svojim nalogom na platformi :



![video](https://youtu.be/cUwCfTKDAOo)



## Zahtev za kredit



Platforma vas povezuje sa likvidnošću institucionalnog kvaliteta i nudi niz opcija koje odgovaraju vašim potrebama. Pregledajte kako biste saznali šta je dostupno. Takođe imate fleksibilnost da prilagodite parametre zajma prema vašoj individualnoj toleranciji rizika i finansijskoj situaciji.



![image](assets/fr/22.webp)



Fiat valute koje Debifi trenutno nudi mogu se pogledati na platformi.



![image](assets/fr/23.webp)



### Jasne, fleksibilne ugovorne klauzule



Debifi se oslanja na transparentne i fleksibilne uslove zajma kako bi zadovoljio potrebe svake strane (zajmodavca i zajmoprimca). Ključne klauzule uključuju :



#### Odnos kredita i vrednosti (LTV)


Bitcoin tranše zajma su generalno tri (3) po broju:





- Konzervativno (20% - 40% LTV), što odgovara zajmu niskog rizika, idealno je za maksimiziranje sigurnosti protiv volatilnosti cena Bitcoin;





- Izbalansirano (50% LTV) ;





- Agresivno (70% - 85% LTV), što nudi veću likvidnost, ali nosi vrlo visok rizik od likvidacije tokom pada tržišta. Aktivno praćenje uslova na tržištu Bitcoin je neophodno prilikom odabira ove tranše.



#### Kamate



Postavljanje kamatnih stopa generalno zavisi od izabranog LTV-a, dužine trajanja zajma, volatilnosti kolaterala i procene rizika specifične za platformu. Stope ostaju fiksne tokom trajanja zajma.



#### Rok otplate i fleksibilnost otplate



Rasporedi otplate za zajmove su često fleksibilni i prilagođeni potrebama korisnika. Uplate se mogu izvršiti u bilo koje vreme sve dok su ispunjeni zahtevi za kolateral. Uplate za zajam su uglavnom kamate tokom trajanja zajma, dok je glavnica dospela na naplatu po dospeću.



#### Prava likvidacije (Margin pozivi)



Kako je cena Bitcoin nestabilna, odgovoran zajam uključuje specifične politike margin poziva u sporazumu. Ova politika omogućava zajmoprimcu da bude obavešten da ili obezbedi dodatni kolateral, ili otplati deo zajma.



### Pokretanje procesa zajma



Da biste odabrali ponudu kredita koja odgovara vašim potrebama, kliknite na nju da biste videli njene karakteristike.



![image](assets/fr/24.webp)



Možete videti :


1. Naziv institucije za pozajmljivanje ;


2. Raspon iznosa zajma;


3. Da ćete primiti sredstva u USDC Ethereum ;


4. Period otplate kredita, kamatna stopa i LTV odnos;


5. KYC je potreban za ovu ponudu;


6. Tačan iznos koji vam je potreban mora biti unet (ovaj iznos mora biti unutar opsega, vidi 2);


7. Ethereum USDC Address koji će se koristiti za primanje sredstava mora biti unet.



Kada budete zadovoljni ponudom i popunite potrebne informacije, kliknite na "Contract request".



![image](assets/fr/25.webp)



Vratite se na mobilnu aplikaciju za ''**Provide public key**''.



![image](assets/fr/26.webp)



Pritisnite '' **Provide public key** '', zatim izaberite izvor javnog ključa. Zajmodavac će takođe morati da Supply javni ključ.



![image](assets/fr/27.webp)



![image](assets/fr/28.webp)



![image](assets/fr/29.webp)



![image](assets/fr/30.webp)



Sledeći korak je potpisivanje Contract. Još uvek u mobilnoj aplikaciji, pritisnite '' **Sign Contract** ''



![image](assets/fr/31.webp)



![image](assets/fr/32.webp)



Kada završite sa potpisivanjem Contract, Debifi automatski kreira jedinstveni multi-potpis Bitcoin Address (escrow 3-sur-4) za vaš Contract. Dokle god su vaši bitkoini u escrow-u, ne mogu se koristiti na drugom mestu.



### Depozit garancije i prijem vaših sredstava



Poslednji korak je da položite svoj Bitcoin kolateral u sistem skrbništva sa više potpisa. Debifi vam zatim prikazuje skrbništvo Address (B) i količinu BTC (A) koja treba biti poslata kao (kolateral + provizija).



![image](assets/fr/33.webp)



Takođe ćete primiti ovo obaveštenje u vašoj mobilnoj aplikaciji.



![image](assets/fr/34.webp)



Čim vaš depozit bude potvrđen, zajmodavac će isplatiti iznos zajma na navedeni Address, čime će se transakcija finalizirati i omogućiti vam pristup potrebnim sredstvima.



Zatim ćete primiti obaveštenje od Debifi, tražeći od vas da platite naknade za zajam ili provizije kako biste unapredili status vašeg zajma.



U stvarnosti, kada je Contract kreiran, naknade za zajam se automatski odbijaju iz kolaterala koji je deponentirao zajmoprimac u multi-potpisnom escrow-u Address.



Sve što treba da uradite je da potpišete transakciju koja će omogućiti Debifi-ju da odbije svoju proviziju od garancije. Sa svoje strane, vaš zajmodavac će takođe morati da potpiše transakciju za odbijanje provizije, inače Debifi neće moći da primi svoju proviziju.



![image](assets/fr/35.webp)



Primjenjive naknade za pozajmljivanje su 1.5-2%, u zavisnosti od trajanja Contract. Platforma naplaćuje provizije samo u Bitcoin.



## Praćenje zajma



Jednom kada je zajam u toku, Debifi vam omogućava da pratite vaš Contract u realnom vremenu. U Interface, videćete :





- Iznos pozajmljenog novca i preostali rok.
- Trenutni LTV (Loan-to-Value) odnos: LTV se povećava ako cena BTC padne (pošto vaša kolaterala vredi manje). Postavljen je prag upozorenja (obično 90%). Ako vaš LTV pređe ovaj prag, postoji rizik od prinudne likvidacije. Debifi će vam tada dati 24 sata da reagujete.



Zajmoprimci će biti obavešteni o smanjenju cene. Ove informacije će takođe biti dostupne na Contract stranici sažetka. Da bi se vratio originalni odnos zajma prema vrednosti, zajmoprimac mora:





- ili položiti dodatnu garanciju ;
- otplatiti ceo ili deo duga.



U slučaju povećanja cene kolaterala, zajmoprimac zadržava sve kapitalne dobitke na kolateralu. On duguje samo iznos zajma, koji je unapred određen i nezavisan od cene Bitcoin.




## Otplata i povraćaj kolaterala



Na kraju dogovorenog roka (ili ranije, ako želite), morate vratiti zajam.


U Debifiju :





- Idite na svoj Contract i kliknite na **Make a repayment**. Unesite ukupan iznos duga (glavnica + kamata).





- Pošaljite stablecoine sa vašeg Wallet na Address zajmodavca koji je naveden, i vratite se da potvrdite otplatu na platformi kopiranjem **ID**-a transakcije otplate u posvećenu karticu. Ovo olakšava Debifi-ju da izvrši svoje provere.



Kada uplata bude potvrđena od strane zajmodavca (i od vas), Debifi će vas zatim zamoliti da **refundirate**. Vaš Bitcoin kolateral će biti oslobođen i možete ga vratiti iz escrow-a u svoj portfelj. Ne zaboravite da prikupite sve svoje Bitcoine.



Čim primite svoje bitkoine, zajam Contract se menja u **Contract završeno**.



Čestitamo! Završili ste proces.




## Najbolje prakse i bezbednost



Koji god da su vaši ciljevi ili motivacije - finansiranje projekta, kupovina nekretnine, kupovina bitkoina, itd. - budite izuzetno oprezni pre nego što uzmete zajam podržan Bitcoin. - budite izuzetno oprezni pre nego što uzmete zajam podržan Bitcoin. Odvojite vreme da pažljivo razmotrite svoju odluku, jer Bitcoin ostaje nestabilna imovina. **Oštar pad njegove cene mogao bi rezultirati prinudnom likvidacijom vaših bitkoina**.



Pratite svoj odnos zajma i kolaterala (LTV). Postavite upozorenja (cena BTC, LTV) ako je moguće. Ne dozvolite da vaš odnos priđe 90%. Ako ste u nedoumici, povećajte kolateral ili vratite ranije.



Kontrolišite svoje ključeve. Čuvajte svoj BTC u sigurnom Wallet (idealno hardverskom ili renomiranom Wallet). Nemojte postavljati PIN kod povezan sa važnim datumom u vašem životu i nikada ne delite svoju frazu za oporavak. Na Debifi, vi generate svoj privatni ključ u aplikaciji - Debifi ga ne zna.



Počnite sa malim iznosom ako je moguće. Za vaš prvi kredit, testirajte skroman iznos kako biste se upoznali sa procesom.



Koristite samo zvaničnu Debifi veb stranicu da biste bili u toku sa vestima o Debifi-ju, i izbegavajte nepoznate ili phishing linkove. Ažurirajte aplikaciju, zaštitite svoj pametni telefon PIN kodom, i izaberite kompatibilan Hardware Wallet.



Alternativno, ako ste zajmodavac, ovaj video vodič će vas voditi kroz korišćenje Debifi platforme. Od odabira zajmoprimaca zainteresovanih za vašu ponudu, do pružanja javnih ključeva, potpisivanja ugovora, prenosa stablecoina i još mnogo toga.



![video](https://youtu.be/g8iLxwI4xT0)



Sada znate kako koristiti Debifi platformu za dobivanje zajma.



Preporučujem da pohađate ovaj kurs, koji detaljno razmatra Bitcoin, stabilne kovanice i njihov doprinos suverenitetu.



https://planb.academy/courses/fdc41e06-ea63-4bf0-a5ac-a0185fe30e46