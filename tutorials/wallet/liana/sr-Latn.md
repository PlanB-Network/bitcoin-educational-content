---
name: Liana
description: Postavljanje i korišćenje Wallet na Liana
---
![cover](assets/cover.webp)


U ovom vodiču, objasnićemo korak-po-korak kako koristiti Liana aplikaciju na računaru. Između ostalog, naučićete kako postaviti automatizovani plan sukcesije, primati i slati bitkoine u normalnim situacijama, i povratiti sredstva iz postojećeg Wallet nakon određenog perioda.


U januaru 2025. godine, hardverski novčanici kompatibilni sa Liana bili su: BitBox02, Blockstream Jade, Blockstream Jade Plus, COLDCARD MK4, COLDCARD Q, Ledger Nano S, Ledger Nano S Plus, Ledger Nano X, Ledger Flex, Specter DIY.


Ako želite da povratite sredstva sa postojećeg Liana Wallet, pročitajte prezentaciju ispod i idite direktno na odeljak "Povratak bitkoina".


## Predstavljamo Liana softver


Liana je softverski paket otvorenog koda dizajniran za kreiranje i upravljanje naprednim novčanicima, posebno kao deo automatizovanog sistema nasleđivanja ili robusnog mehanizma za bekap. Projekat je razvijan od 2022. godine od strane Wizardsardine, kompanije koju su osnovali Kévin Loaec i Antoine Poinsot. Na zvaničnom sajtu, Liana je predstavljen kao "jednostavan Wallet za ličnu kuraciju, sa funkcionalnostima oporavka i nasleđivanja". Softver radi na računarima -- Linux, MacOS, Windows -- a njegov (otvoreni) izvorni kod je dostupan [na GitHub-u](https://github.com/wizardsardine/Liana).


Liana se nadovezuje na programabilnost Bitcoin kako bi stvorio napredni Wallet. Konkretno, koristi vremenske brave (*timelocks*), koje omogućavaju da se sredstva troše tek nakon što prođe određeni vremenski period, i koje su uključene u oporavak Bitcoina. Liana Wallet se tako sastoji od nekoliko puteva potrošnje:




- Glavni put trošenja, koji je uvek dostupan;
- Barem jedan put oporavka, koji postaje dostupan nakon određenog vremena.


Dijagram ispod ilustruje rad Wallet sa dve putanje trošenja:


![Schéma explicatif](assets/fr/01.webp)


Ova operacija vam omogućava da postavite različite konfiguracije, uključujući :




- Plan sukcesije (ili nasleđa), koji omogućava naslednicima da povrate sredstva u slučaju smrti korisnika. Za više informacija o ovoj temi, preporučujemo čitanje [dela 4](https://planb.network/courses/f3e3843d-1a1d-450c-96d6-d7232158b81f/233c88d3-2e8e-5eba-ac06-efe67a209038) kursa BTC102.
- Ojačana rezervna kopija sa vremenom oporavka, koja korisniku daje mogućnost korišćenja njegovog Wallet bez potrebe da čuva odgovarajuću tajnu frazu i rizikuje da bude ukradena, na primer tokom provale.
- Sigurnosna mreža za ljude koji počinju sa Bitcoin: oni će upravljati svojim Wallet, a njihov "čuvar" (na primer, rođak) će zadržati pravo da povrati njihova sredstva nakon određenog perioda.
- Šema sa više potpisa (*Multisig*) sa smanjenim zahtevima tokom vremena, kako bi se izborila sa nestankom jednog ili više učesnika, kao što su partneri kompanije.


Velika snaga Liana je što uvodi standardizovan način garantovanja povraćaja sredstava u slučaju gubitka glavnog ključa, koji se koristi za tekuće troškove. Ovo predstavlja ogromnu inovaciju za čisto čuvanje sredstava, koje je prepuno rizika, posebno ako niste dobro informisani o toj temi. Liana bi stoga mogao podstaći čak i korisnike koji izbegavaju rizik da prestanu koristiti skrbnika (kao što je Exchange platforma) za držanje svojih sredstava i povrate Ownership svog novca, u skladu sa Bitcoin-ovom Cypherpunk etikom.


Naravno, Liana ima svoje nedostatke. Prvi je taj što morate redovno ažurirati svoj Wallet tako što ćete izvršiti transakciju na Bitcoin Blockchain. Ovo može biti naporno (u zavisnosti od toga koliko često koristite softver) i skupo (u zavisnosti od nivoa naknada u to vreme), ali to je cena koju plaćate za dodatnu sigurnost.


Druga negativna tačka može biti poverljivost. Kada uključite drugu osobu u konfiguraciju, ona ima pristup svim vašim adresama i stoga može pratiti vašu aktivnost. Međutim, ovo neće biti problem ako se odlučite za pojačanu rezervnu kopiju ili za plan sukcesije u kojem vaš naslednik nema neposredno znanje o detaljima Wallet.


## Priprema


U ovom vodiču, postavićemo plan sukcesije. Koristićemo:




- Ledger Nano S Plus, za svakodnevne troškove;


https://planb.network/tutorials/wallet/hardware/ledger-nano-s-plus-75043cb3-2e8e-43e8-862d-ca243b8215a4


- Blockstream Jade, korišćen za povraćaj sredstava;


https://planb.network/tutorials/wallet/hardware/jade-7d62bf0c-f460-4e68-9635-af9b731dabc3


- Dva skladišna medija (USB stikovi) za čuvanje Wallet deskriptora;
- Pismo o sukcesiji, koje sadrži uputstva za povraćaj sredstava;
- Numerisana zapečaćena vrećica, kako bi se osiguralo da uređaj za oporavak (Jade) nije korišćen.


## Instalacija i konfiguracija


Posetite zvaničnu Wizardsardine veb stranicu i preuzmite Liana na https://wizardsardine.com/Liana/. Takođe možete preuzeti najnoviju verziju [sa GitHub repozitorijuma](https://github.com/wizardsardine/Liana/releases), gde možete proveriti autentičnost softvera. Verzija korišćena u ovom vodiču je 0.9.


![Télécharger Liana](assets/fr/02.webp)


Da biste saznali kako ručno proveriti autentičnost i integritet softvera pre instalacije, preporučujemo da pogledate ovaj vodič :


https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

Instalirajte softver na svoj uređaj i pokrenite ga. Izaberite opciju "*Create a new Liana Wallet*" da biste konfigurisali svoj Wallet.


![Accueil Liana](assets/fr/03.webp)


Izaberite svoj Wallet tip. Ako želite da postavite poboljšanu rezervnu kopiju sa vremenom oporavka, možete odabrati opciju "*Izgradi svoj*" i odlučiti se za podrazumevanu šemu. Ovo će funkcionisati na sličan način, osim što nećete morati da zadržite Hardware Wallet frazu za oporavak.


Ovde zanemarujemo slučaj *Expanding Multisig*, koji postavlja složeniju konfiguraciju.


Za potrebe ovog tutorijala, koristićemo jednostavno nasleđivanje.


![Choisir type de portefeuille](assets/fr/04.webp)


Brzo objašnjenje sledi.


![Rapide explication](assets/fr/05.webp)


Jednom kada pročitate objašnjenje, moći ćete da postavite ključeve za vaš Liana Wallet. Ovo je ključni korak, jer određuje karakteristike trošenja vašeg naloga.


![Configurer clés](assets/fr/06.webp)


Prvo, u meniju "Advanced Settings" možete odlučiti o "descriptor type", tj. načinu na koji će Contract biti napisan na lancu. Možete birati između dve vrste: P2WSH (SegWit) ili Taproot. U oba slučaja, semantika uslova trošenja će biti ista. Dok P2WSH čini Contract lakšim za razumevanje, Taproot je superiorniji jer skriva neiskorišćene uslove i štedi troškove tokom preuzimanja.


Ovaj izbor je opcionalan: ako ste u nedoumici, ostavite podrazumevanu opciju (P2WSH u slučaju verzije 0.9, ali ovo je podložno promenama).


![Choisir le type de descripteur](assets/fr/07.webp)


Zatim, konfigurišite svoj primarni ključ (*primary key*). Ovaj ključ (ili tačnije, ovaj skup ključeva) će se koristiti za trenutnu potrošnju sredstava, koja nije podložna vremenskim uslovima. Klikom na "*Set*", možete odabrati odgovarajući *uređaj za potpisivanje*. U našem slučaju, odabrali smo Ledger Nano S Plus Hardware Wallet.


Autorizujte deljenje proširenog javnog ključa sa uređaja. Dajte ovom ključu smisleno ime (u ovom slučaju, "Nano S+"). Imajte na umu da će sve aplikacije instalirane na uređaju nastaviti da funkcionišu normalno.


![Configurer clé principale](assets/fr/08.webp)


Zatim, postavite kašnjenje isplate, tj. vreme nakon kojeg sredstva mogu biti potrošena od strane *ključa nasledstva*. Ovo kašnjenje je definisano u terminima blokova, pri čemu je svaki blok razdvojen prosečno 10 minuta. Može se kretati od 10 minuta (1 blok) do oko 15 meseci (65.535 blokova). Ovo gornje ograničenje je ograničenje Bitcoin protokola, jer je vreme zaključavanja kodirano na 16 bita.


Osim u posebnim okolnostima, odlučite se za najduži rok isporuke: 15 meseci ili 65.535 blokova. Ovo će vam uštedeti troškove. Međutim, preporučujemo da sprovedete postupak ažuriranja (opisan u odeljku "Ažuriranje Wallet") jednom godišnje, uvek u isto vreme godine, kako biste "ritualizovali" ovu praksu i izbegli zaboravljanje.


Ovde smo postavili vreme oporavka od jednog sata (6 blokova) da bismo sproveli naše testove.


![Configurer temps de verrouillage](assets/fr/09.webp)


Konačno, postavite ključ za imovinu. Ovaj ključ (ili bolje rečeno, skup ključeva) će se koristiti za povrat sredstava u slučaju vašeg nestanka. Kliknite na "*Postavi*", izaberite uređaj za potpisivanje i potvrdite deljenje proširenog javnog ključa na njemu.


Za ovaj vodič, odabrali smo Jade. Dajte ključu sugestivno ime (ovde "Jade"). Kao i kod prvog uređaja, konvencionalni nalozi će nastaviti da funkcionišu.


![Configurer clé de succession](assets/fr/10.webp)


Kada su sve ove radnje završene, proverite da li je sve u redu i kliknite na "*Nastavi*" da potvrdite svoje izbore.


![Confirmer clés](assets/fr/11.webp)


Sledeći korak je da sačuvate svoj Wallet deskriptor. Ovo su informacije koje su vam potrebne da pronađete sredstva na svom računu. Suprotno Mnemonic frazi, deskriptor vam ne omogućava da trošite sredstva, tako da njegovo otkrivanje predstavlja samo problem poverljivosti (osoba će znati sve vaše transakcije).


Sačuvajte dve kopije deskriptora na elektronskim medijima, kao što su USB stikovi. Uverite se da takođe odštampate dve kopije na papiru, kako biste mogli da im pristupite u slučaju oštećenja elektronskih medija. Svaka rezervna kopija mora biti povezana sa uređajem za potpisivanje.


![Sauvegarder descripteur](assets/fr/12.webp)


Naš deskriptor (koji se analizira na kraju tutorijala) je sledeći:


```plaintext
wsh(or_d(pk([3689a8e7/48'/0'/0'/2']xpub6FKYNH4XbbdADV98yTVxgZZrtB4eE2tiUPreEv5iJAS3U1CvXGAtQGFXSHyFYdYNn9wNa9KU1pwfYoxQhwq4sPXGihD725VncdSy66v9WQa/<0;1>/*),and_v(v:pkh([42e629dd/48'/0'/0'/2']xpub6DpQGv9LkwAQXvghWASvsfA7t1BVj7bGDQ939v32iB6aUJsMRB6inckim26gRp74NBdS2zuyfHNXDZ9dTuNXkFFiz6QvwEeVvBuC2cnRWQd/<0;1>/*),older(6))))#8alrve5h
```


Poslednji korak u početnoj konfiguraciji Wallet je da proverite opis u svakom od hardverskih novčanika koji služe kao uređaji za potpisivanje.


![Enregistrer descripteur](assets/fr/13.webp)


Uradite isto za svaki uređaj za potpisivanje. Trebaće da proverite i potvrdite da je opis dodan svakom Hardware Wallet.


![Enregistrer descripteur Nano S Plus](assets/fr/14.webp)


Vaša Wallet informacija je sada registrovana, i sve što preostaje je da konfigurišete kako želite da se povežete na Bitcoin mrežu. Možete izabrati da koristite svoj čvor (lokalni ili udaljeni) ili da koristite WizardSardine infrastrukturu. U ovom poslednjem slučaju, biće potrebno da povežete e-mail Address sa vašim Wallet, što će vam omogućiti da preuzmete opisivač. WizardSardine će imati pristup svim vašim transakcijama. Stoga se preporučuje prva opcija.


![Sélectionner connexion réseau](assets/fr/15.webp)


Odlučili smo da koristimo naš sopstveni čvor. Možete koristiti postojeći čvor ili instalirati *pruned node* na vašem računaru. Ako nemate pristup nijednom drugom čvoru, instalirajte svoj sopstveni čvor na vašem računaru, što bi trebalo da potraje neko vreme (reda nekoliko dana).


![Choisir type de nœud](assets/fr/16.webp)


Za ovaj vodič, koristili smo postojeći (javni) Electrum server. Ali budite oprezni! Imao je pristup svim našim aktivnostima sa Liana Wallet. Zato koristite svoj čvor ako želite da zaštitite svoju privatnost.


![Connexion serveur Electrum public](assets/fr/17.webp)


Kada je konfiguracija čvora završena, glavni ekran bi trebalo da se otvori, prikazujući vaš sveže kreirani Liana Wallet.


Iskoristite priliku da uskladištite jedinicu za oporavak na sigurnom mestu. Trebalo bi da bude uskladištena na strateškoj lokaciji, kako bi je vaši naslednici mogli pronaći u slučaju vaše smrti.


Za dodatnu sigurnost, možete staviti komponente koje se koriste za oporavak u zapečaćenu vrećicu (*vrećica sa zaštitom od neovlašćenog otvaranja*) i negde zabeležiti njen serijski broj. Ovo osigurava da niko nije pristupio komponentama i da vaš uređaj ostaje važeći.


U našem primeru, sastavili smo sledeći Elements:




- Blockstream Jade kao uređaj za potpisivanje za imovinu;
- USB kabl za povezivanje i punjenje uređaja;
- Papirna kopija rečenice u slučaju kvara ili oštećenja uređaja (imajte na umu da medijum može biti i metal, i stoga zaštićen od Elements, kao što je slučaj sa Cryptosteel kapsulama, na primer);
- USB ključ koji sadrži Wallet opis ;
- Papirna kopija deskriptora, u slučaju kvara ili oštećenja USB ključa (ova kopija nije fotografisana ovde);
- Pismo o sukcesiji koje opisuje korake koje treba preduzeti za povraćaj sredstava.


![Éléments de récupération](assets/fr/18.webp)


I stavili smo ove stavke pod Seal!


![Sachet scellé récupération](assets/fr/19.webp)


## Prijem sredstava


Glavni ekran Liana prikazuje vaš saldo i transakcije (prošle i trenutne) povezane sa vašim Wallet. U našem slučaju, saldo je nula, što je normalno.


![Écran principal](assets/fr/20.webp)


Da biste primili sredstva, idite na karticu "*Receive*" i kliknite na "*generate Address*". Novi Address bi trebalo da se pojavi na vašem ekranu. Duži je nego u konvencionalnim novčanicima: to je Address povezan sa samostalnim Contract (P2WSH ili Taproot).


![Générer nouvelle adresse](assets/fr/21.webp)


Morate da verifikujete ovaj Address na vašem Hardware Wallet klikom na "*Verify on hardware device*".


![Vérifier adresse portefeuille matériel](assets/fr/22.webp)


Jednom kada su sredstva poslana, transakcija se pojavljuje na glavnom ekranu (prvo kao nepotvrđena, zatim kao potvrđena). Ovde smo poslali 50.000 satoshija (nešto više od $50 u vreme transfera) za ovaj test. Podrazumeva se da će iznos koji se prenosi u vašem slučaju morati biti za red veličine veći od ove vrednosti, zbog naknada za transakciju.


![Vérifier solde](assets/fr/23.webp)


Možete proveriti status isteka vaših sredstava odlaskom na karticu "*Coins*". Ova kartica vam prikazuje različite novčiće (UTXO) u vašem Wallet. Ovde možemo videti da novčić od 50,000 satoshija kreiran našom transakcijom ističe istog dana (za jedan sat).


![Obtenir informations pièce](assets/fr/24.webp)


Da biste bolje razumeli model reprezentacije UTXO korišćen u Bitcoin, možete se konsultovati sa prvim delom kursa o poverljivosti u Bitcoin koji je napisao Loïc Morel :


https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Trenutni izdaci


Trenutna potrošnja je normalna situacija za korišćenje Liana. Slanje bitcoina sa glavnim ključem funkcioniše kao u svim klasičnim Bitcoin novčanicima kao što su Electrum ili Sparrow.


Da biste izvršili naplatu, idite na karticu "*Pošalji*" i unesite osnovne informacije: BTC Address primaoca, iznos koji se šalje i željenu stopu naplate. Opis (sačuvan lokalno) takođe može biti dodat za vašu ličnu pogodnost. U našem primeru, poslali smo 10.000 satoshija određenom Bobu, po stopi naplate od 4 sat/ov, ili $0.67 u vreme transakcije.


Liana takođe nudi "kontrolu novčića": vi označavate koji novčić (UTXO) želite da potrošite. Ovde smo odabrali novčić od 50,000 satoshija koji je prethodno kreiran.


![Envoyer fonds clé principale](assets/fr/25.webp)


Zatim potpišite transakciju svojim uređajem za potpisivanje povezanim sa glavnim ključem klikom na "*Potpiši*". Moraćete da verifikujete i potvrdite transakciju na vašem Hardware Wallet. Ovde smo koristili Nano S Plus za potpisivanje transakcije.


![Signer transaction clé principale](assets/fr/26.webp)


Na kraju, emitujte transakciju preko mreže klikom na "*Emituj*". Imajte na umu da će slanje sredstava resetovati vreme oporavka za korišćene novčiće.


![Diffuser transaction clé principale](assets/fr/27.webp)


Transakcija će se pojaviti na glavnom ekranu i vaše stanje će biti ažurirano.


![Solde après dépense](assets/fr/28.webp)


## Ažuriranje portfolija


Kao što je gore objašnjeno, Liana Wallet zahteva da redovno ažurirate svoja sredstva obavljanjem transakcije na Blockchain. Ako to ne učinite, vaša sredstva mogu biti povraćena od strane vašeg naslednika (ili od strane vašeg drugog uređaja u slučaju poboljšane sigurnosne kopije). Ova situacija nije izuzetno opasna, ali poništava svrhu postavljanja ovog mehanizma: da ostanete u kontroli svojih bitkoina bez pribegavanja pouzdanoj trećoj strani, dok istovremeno imate sigurnosnu mrežu.


Prikazaće se upozorenje pre nego što vaša sredstva (ili deo njih) isteknu i mogu biti potrošena putem ključa za oporavak. To će ukazati da će vaš "put oporavka" (*recovery path*) uskoro biti dostupan. S obzirom na kratkoću našeg vremena za oporavak (jedan sat), ova poruka se prikazuje direktno u našem slučaju.


![Avertissement chemin récupération](assets/fr/29.webp)


Kada se rok približi, pojaviće se dugme koje će vas pozvati da ažurirate dotična sredstva.


![Actualiser pièces depuis l'écran principal](assets/fr/30.webp)


Da biste ažurirali svoje novčiće, idite na karticu "*Coins*" i kliknite na "*Refresh coin*" u odgovarajućem polju za novčiće. Ako imate nekoliko novčića, trebalo bi da ih osvežavate jedan po jedan, i to u relativno kratkim intervalima, zbog razloga poverljivosti. Da biste smanjili troškove, možete konsolidovati svoja sredstva slanjem celog Wallet na novi prijemni Address, ali to će uticati na vašu poverljivost.


![Actualiser pièce](assets/fr/31.webp)


Naznačite željenu stopu naknade za transakciju. Pošto je ovo transfer ka sebi, možete postaviti prilično nisku stopu naknade, posebno ako to radite nekoliko dana pre isteka.


![Transfert à soi-même](assets/fr/32.webp)


Transakcija (označena kao "*samoprenos*") biće vidljiva samo na kartici "*Transakcije*".


![Transactions après auto-transfert](assets/fr/33.webp)


Kada se potvrdi, vaš novčić je siguran! Možete biti bez brige do sledećeg datuma isteka.


## Bitcoin oporavak


Kada povraćate sredstva sa Liana Wallet, možete se suočiti sa jednom od dve situacije. Možda imate pristup računaru na kojem je softver instaliran, u tom slučaju sve što treba da uradite je da ga otvorite (što će se desiti u slučaju poboljšanog modela bekapa). Međutim, možda nemate pristup ovom računaru, pa ćemo ovde početi od nule. Imajte na umu da je procedura oporavka ista u oba slučaja.


Da biste započeli, preuzmite Liana sa [zvanične Wizardsardine veb stranice](https://wizardsardine.com/Liana/), ili sa [GitHub repozitorijuma](https://github.com/wizardsardine/Liana/releases), gde možete proveriti autentičnost softvera. Instalirajte softver i pokrenite ga. Verzija korišćena u našem slučaju je 0.9, tako da se vizuali mogu promeniti. Na ekranu dobrodošlice, izaberite opciju "Dodaj postojeći Liana Wallet".


![Ajouter portefeuille existant](assets/fr/34.webp)


Konfigurišite kako želite da se povežete na mrežu. Možete izabrati da koristite svoj čvor (lokalni ili udaljeni) ili da koristite WizardSardine infrastrukturu. U ovom slučaju, biće vam potrebna e-mail adresa Address koju je koristio kreator Wallet, kako bi sredstva mogla biti automatski locirana. Ako nemate ove informacije, izaberite prvu opciju.


![Sélectionner connexion réseau](assets/fr/35.webp)


Ako koristite svoj čvor, uvezite Wallet deskriptor. Ovo je tehnički opis naloga, koji vam omogućava da povratite sredstva koja se u njemu nalaze. U našem slučaju, to su sledeće informacije:


```plaintext
wsh(or_d(pk([3689a8e7/48'/0'/0'/2']xpub6FKYNH4XbbdADV98yTVxgZZrtB4eE2tiUPreEv5iJAS3U1CvXGAtQGFXSHyFYdYNn9wNa9KU1pwfYoxQhwq4sPXGihD725VncdSy66v9WQa/<0;1>/*),and_v(v:pkh([42e629dd/48'/0'/0'/2']xpub6DpQGv9LkwAQXvghWASvsfA7t1BVj7bGDQ939v32iB6aUJsMRB6inckim26gRp74NBdS2zuyfHNXDZ9dTuNXkFFiz6QvwEeVvBuC2cnRWQd/<0;1>/*),older(6))))#8alrve5h
```


![Importer descripteur](assets/fr/36.webp)


Liana zatim traži da unesete Mnemonic frazu. Ako imate ispravan uređaj za potpisivanje (Hardware Wallet), preskočite ovaj deo. Ako vam uređaj nedostaje ili je oštećen, ali imate odgovarajućih 12 ili 24 reči, i dalje možete koristiti ovu opciju. Da biste bili sigurni (ako je iznos koji treba povratiti visok), i dalje predlažemo da nabavite novi Hardware Wallet i koristite Mnemonic za obnavljanje ključeva na njemu.


U našem slučaju, koristimo Blockstream Jade Hardware Wallet kao uređaj za oporavak i odlučujemo da preskočimo ("*Skip*") ovaj korak.


![Passer phrase mnémotechnique](assets/fr/37.webp)


Proverite i sačuvajte opis u svom uređaju za potpisivanjem tako što ćete ga odabrati na ekranu. Ako se vaš Hardware Wallet ne pojavljuje, proverite da li je povezan i otključan. Proverite i potvrdite da su ove informacije dodate na vaš uređaj.


![Enregistrer descripteur sur l'appareil de récupération](assets/fr/38.webp)


Konfigurišite svoj čvor. Možete koristiti postojeći čvor ili instalirati *pruned node* na vašem računaru. U našem slučaju, koristili smo postojeći čvor.


![Choisir type de nœud](assets/fr/39.webp)


Za ovaj vodič koristili smo javni Electrum server. Međutim, imao je pristup svim našim aktivnostima sa Liana Wallet. Ako želite zaštititi svoju privatnost, bolje je da koristite svoj vlastiti čvor.


![Connexion serveur Electrum public](assets/fr/17.webp)


Jednom kada postavite svoj čvor, bićete preusmereni na glavni ekran Wallet, gde možete videti stanje i prethodne transakcije povezane sa nalogom. Takođe možete videti da li sredstva mogu biti povučena. Ovde vidimo da novčić može biti povučen.


![Accueil Liana récupération](assets/fr/40.webp)


Da biste povratili sredstva u Wallet, idite na Podešavanja ("*Settings*") u donjem levom uglu i kliknite na "*Recovery*".


![Récupération dans paramètres](assets/fr/41.webp)


Potrošite novčić u Wallet označavanjem odgovarajućeg polja. Naznačite BTC Address na koji želite poslati sredstva, kao i stopu naknade za transakciju. Zatim kliknite na "*Next*".


![Récupération des pièces](assets/fr/42.webp)


Potpišite transakciju klikom na "*Sign*" i validacijom transakcije na vašem Hardware Wallet.


![Signer transaction clé de récupération](assets/fr/43.webp)


Zatim emitujte preko mreže klikom na "*Emituj*".


![Diffuser transaction clé de récupération](assets/fr/44.webp)


Transakcija bi trebalo da se pojavi na glavnom ekranu. Kada se potvrdi, oporavak je završen!


![Écran principal après récupération](assets/fr/45.webp)


## Bonus: analiza deskriptora


Opisivač je čitljiv niz karaktera koji iscrpno opisuje skup adresa. Kombinuje nekoliko ključnih informacija za preuzimanje delova (UTXO) naprednog Wallet. Način na koji je opisivač napisan zasnovan je na [Miniscript sintaksi](https://bitbox.swiss/blog/understanding-Bitcoin-miniscript-part-2/), skriptnom jeziku koji su razvili Andrew Poelstra, Pieter Wuille i Sanket Kanjalkar 2019. godine.


Da bismo bolje razumeli zašto je ovaj niz karaktera važan, hajde da analiziramo opis u našem primeru, koji je :


```plaintext
wsh(or_d(pk([3689a8e7/48'/0'/0'/2']xpub6FKYNH4XbbdADV98yTVxgZZrtB4eE2tiUPreEv5iJAS3U1CvXGAtQGFXSHyFYdYNn9wNa9KU1pwfYoxQhwq4sPXGihD725VncdSy66v9WQa/<0;1>/*),and_v(v:pkh([42e629dd/48'/0'/0'/2']xpub6DpQGv9LkwAQXvghWASvsfA7t1BVj7bGDQ939v32iB6aUJsMRB6inckim26gRp74NBdS2zuyfHNXDZ9dTuNXkFFiz6QvwEeVvBuC2cnRWQd/<0;1>/*),older(6))))#8alrve5h
```


Iz sledećeg opisa mogu se izvući sledeće informacije:




- `wsh` (skraćenica za *witness script Hash*): Ovo je tip transakcijskog izlaza koji je kreiran. Da smo odlučili koristiti Taproot, identifikator bi bio `tr`.
- `or_d`: Ovo je logički operator koji označava da *jedan od sledeća dva* uslova mora biti ispunjen da bi trošak bio prihvaćen ( `_d` označava posebnu sintaksu).
- `pk` (skraćeno za *public key*): Ovaj operator proverava dati potpis u odnosu na sledeći javni ključ i daje odgovor kao Boolean (TRUE ili FALSE).
- `[3689a8e7/48'/0'/0'/2']`: Ovaj element uključuje *otisak prsta* glavnog ključa za glavni Hardware Wallet (u ovom slučaju Nano S Plus), i put derivacije do povezanog proširenog privatnog ključa (od kojeg su izvedeni svi ostali privatni ključevi).
- `xpub6FKY ... WQa`: Ovo je prošireni javni ključ povezan sa glavnim Hardware Wallet (ovde Nano S Plus)
- `/<0;1>/*`: Ovo su putanje derivacije za dobijanje jednostavnih ključeva i adresa: `0` za prijem, `1` za interne operacije (*promena*), sa "džokerom" (`*`) koji omogućava sekvencijalnu derivaciju nekoliko adresa na podesiv način, slično upravljanju "gap limit" u klasičnom Wallet softveru.
- and_v`: Ovo je logički operator koji označava da *sledeća dva* uslova moraju biti ispunjena da bi trošak bio prihvaćen (oznaka `_v` ukazuje na posebnu sintaksu).
- `v:pkh` (skraćeno za *verify: public key Hash*): Ovaj operator verifikuje dati potpis i javni ključ u odnosu na javni ključ Hash (*Hash*) koji sledi. Ovo je suštinski ista provera kao za P2PKH i P2WPKH skripte.
- `[42e629dd/48'/0'/0'/2']`: Ovo je isti element kao gore (sastoji se od traga i putanje derivacije), osim što je naznačen trag glavnog ključa hardverskog oporavka Wallet (u ovom slučaju Jade).
- `xpub6DpQ ... WQd`: Ovo je prošireni javni ključ povezan sa hardverskim oporavkom Wallet (ovde Jade).
- `older(6)` : Ovaj operator proverava da transakcioni izlaz mora imati starost strogo veću od 6 blokova kako bi mogao biti potrošen.


Poslednja stavka podataka (`8alrve5h`) je kontrolni zbir deskriptora i odgovara identifikatoru Wallet.


Skripte koje kreira ovaj Wallet imaće sledeći oblik:


```plaintext
<primary_key> CHECKSIG IFDUP NOTIF DUP HASH160 <recovery_key_hash> EQUALVERIFY CHECKSIGVERIFY <locktime> CHECKSEQUENCEVERIFY ENDIF
```


Pošto sigurnost vašeg Bitcoin Wallet takođe zavisi od vašeg razumevanja kako funkcioniše, predlažem da detaljno proučite mehanizme determinističkih i hijerarhijskih novčanika pohađanjem ovog besplatnog kursa obuke na Plan ₿ Network :


https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f