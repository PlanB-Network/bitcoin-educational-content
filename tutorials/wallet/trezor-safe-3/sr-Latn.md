---
name: Trezor Safe 3
description: Konfigurisanje i korišćenje Hardware Wallet Safe 3
---
![cover](assets/cover.webp)



*Kredit za sliku: [Trezor.io](https://trezor.io/)*



Trezor Safe 3 je Hardware Wallet koji je dizajnirao SatoshiLabs i kreiran 2023. godine. To je veoma kompaktan, lagan model (14 grama) namenjen kako početnicima, tako i korisnicima srednjeg nivoa. Naslednik je poznatog Modela One, sa značajnim dodacima, dok zadržava pristup otvorenog koda koji ga izdvaja od glavnog konkurenta, Ledger. Safe 3 je cenjen na €79. Stoga je pozicioniran u srednjem segmentu Hardware Wallet, u direktnoj konkurenciji sa Ledger Nano S Plus.



Safe 3 nema bateriju i radi isključivo putem USB-C veze, koja se koristi za napajanje i komunikaciju. Ima mali 0,96-inčni monohromatski OLED ekran i dva fizička dugmeta.



![Image](assets/fr/01.webp)



Safe 3 nudi sve osnovne funkcije koje se očekuju od dobrog Hardware Wallet, uključujući odličnu integraciju passphrase BIP39. Međutim, još uvek ne podržava Miniscript.



Ovaj model je posebno pogodan za početnike, i možda bi čak bio Hardware Wallet koji bih preporučio novom korisniku. Takođe je dobro prilagođen za korisnike srednjeg nivoa. S druge strane, možda neće ispuniti sva očekivanja naprednih korisnika koji traže specifičnije funkcije, dostupne na uređajima kao što je Coldcard. Ipak, ako vam nisu potrebne ove napredne opcije, Trezor Safe 3 može biti odličan izbor.



## Trezor Safe 3 sigurnosni model



Trezor Safe 3 je sada opremljen sa EAL6+ sertifikovanim **Secure Element**, što predstavlja značajan napredak u odnosu na prethodne modele kao što su Model One i Model T. Ovo je OPTIGA Trust M V3 čip, koji ne skladišti direktno seed, već deluje kao kriptografska komponenta za obezbeđivanje pristupa njemu. Secure Element zadržava tajnu kojoj se može pristupiti samo kada korisnik ispravno unese PIN. Ova tajna se zatim koristi za dešifrovanje seed, koji je enkriptovan skladišten u glavnoj memoriji uređaja.



Ovaj hibridni sigurnosni sistem nudi poboljšanu fizičku zaštitu, posebno protiv napada ekstrakcije ili invazivne analize, problema kojima je Model One bio sklon, naročito u upravljanju PIN-om. Ove ranjivosti su sada zaobiđene zahvaljujući upotrebi Secure Element-a. Ovaj model takođe održava softversku arhitekturu otvorenog koda: kod koji upravlja generisanjem i korišćenjem privatnih ključeva ostaje potpuno dostupan i proverljiv. OPTIGA čip upravlja samo PIN kodom, elementom koji je eksterni za Bitcoin Wallet upravljanje ključevima. On samo oslobađa tajnu koja se može koristiti za dešifrovanje seed. Takođe, OPTIGA Trust M V3 čip ima relativno slobodnu licencu, koja ovlašćuje SatoshiLabs da slobodno objavljuje potencijalne ranjivosti.



Ovaj sigurnosni model predstavlja, po mom mišljenju, jedan od najboljih kompromisa dostupnih na tržištu danas. Kombinuje prednosti Secure Element-a sa upravljanjem softverom otvorenog koda. Prethodno su korisnici morali birati između poboljšane fizičke sigurnosti sa čipom i transparentnosti sa otvorenim kodom; sa Trezor Safe 3, moguće je imati koristi od oba.



U ovom vodiču pokazaćemo vam kako da bezbedno postavite i koristite vaš Trezor Safe 3.



## Raspakivanje Trezor Safe 3



Kada primite svoj Safe 3, proverite da li su kutija i Seal netaknuti kako biste potvrdili da paket nije otvoren. Softverska verifikacija autentičnosti i integriteta uređaja će takođe biti izvršena kada se kasnije postavi.



Sadržaj kutije uključuje :




- Trezor Safe 3;
- Torba koja sadrži karton za beleženje vaše Mnemonic fraze, nalepnice i uputstva;
- USB-C na USB-C kabl.



![Image](assets/fr/02.webp)



Kada se otvori, vaš Trezor Safe 3 treba da bude zaštićen zaštitnom plastikom, a USB-C port treba da bude osiguran holografskim Seal. Uverite se da je tu.



![Image](assets/fr/03.webp)



Navigacija na uređaju je jednostavna: koristite desno dugme za pomeranje udesno, a levo dugme za pomeranje ulevo. Pritisnite oba dugmeta istovremeno da potvrdite akciju.



![Image](assets/fr/04.webp)



## Preduslovi



Za ovaj vodič, pokazaću vam kako da koristite Trezor Safe 3 sa [Sparrow Wallet softverom za upravljanje portfoliom](https://sparrowwallet.com/download/). Ako već niste instalirali ovaj softver, molimo vas da to učinite sada. Ako vam je potrebna pomoć, imamo i detaljan vodič o konfigurisanju Sparrow Wallet :



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Trebaće vam i softver Trezor Suite da konfigurišete Safe 3, proverite njegovu autentičnost i instalirate firmware. Ovaj softver ćemo koristiti samo za to, a nakon toga će biti potreban samo za ažuriranja firmware-a. Za svakodnevno upravljanje Wallet koristićemo isključivo Sparrow Wallet, jer je optimizovan za Bitcoin i lak za korišćenje, čak i za početnike (Sparrow podržava samo Bitcoin, ne i altcoine).



[Preuzmite Trezor Suite sa zvaničnog sajta](https://trezor.io/trezor-suite)



![Image](assets/fr/05.webp)



Za oba ova programa, toplo preporučujem da proverite i njihovu autentičnost (sa GnuPG) i njihov integritet (preko Hash) pre nego što ih instalirate na svoj računar. Ako ne znate kako to da uradite, možete pratiti ovaj drugi vodič :



https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

## Pokretanje Trezor Safe 3



Povežite svoj Safe 3 sa računarom na kojem su već instalirani Trezor Suite i Sparrow Wallet.



![Image](assets/fr/06.webp)



Otvorite Trezor Suite, zatim kliknite na "*Set up my Trezor*".



![Image](assets/fr/07.webp)



Odaberite "*Bitcoin-only firmware*", zatim kliknite na "*Install Bitcoin-only*".



![Image](assets/fr/08.webp)



Trezor Suite će zatim instalirati firmver na vaš Safe 3. Molimo sačekajte tokom instalacije.



![Image](assets/fr/09.webp)



Kliknite na "*Continue*".



![Image](assets/fr/10.webp)



Zatim nastavite sa testom autentičnosti kako biste bili sigurni da vaš Hardware Wallet nije lažan ili kompromitovan.



![Image](assets/fr/11.webp)



Na vašem Safe 3, pritisnite desno dugme da potvrdite.



![Image](assets/fr/12.webp)



Ako je vaš Trezor originalan, poruka o potvrdi će se pojaviti u Trezor Suite.



![Image](assets/fr/13.webp)



Zatim možete preskočiti prozore sa osnovnim uputstvima za rad.



![Image](assets/fr/14.webp)



## Kreiranje Bitcoin portfolija



Na Trezor Suite, kliknite na dugme "*Create new Wallet*".



![Image](assets/fr/15.webp)



Za standardni portfolio, možete se odlučiti za podrazumevani tip rezervne kopije. Ovo kreira klasični single-sig portfolio sa 12 reči Mnemonic fraze. Kliknite na "*Create Wallet*".



Ako želite da saznate više o drugim opcijama bekapa dostupnim na Trezoru, uključujući *Multi-share Backup*, preporučujem da pogledate i ovaj vodič :



https://planb.network/tutorials/wallet/backup/trezor-shamir-backup-7f98b593-face-48fb-a643-0e811b87c94e

![Image](assets/fr/16.webp)



Prihvatite uslove korišćenja na Hardware Wallet.



![Image](assets/fr/17.webp)



Pritisnite desno dugme ponovo da kreirate novi portfolio.



![Image](assets/fr/18.webp)



U Trezor Suite, kliknite na "*Continue to backup*".



![Image](assets/fr/19.webp)



Softver pruža uputstva o tome kako upravljati vašom Mnemonic frazom.



Ovaj Mnemonic vam daje potpuni, neograničeni pristup svim vašim bitcoinima. Svako ko poseduje ovu frazu može ukrasti vaša sredstva, čak i bez fizičkog pristupa vašem Trezor Safe 3.



Fraza od 12 reči vraća pristup vašim bitkoinima u slučaju gubitka, krađe ili oštećenja vašeg Hardware Wallet. Stoga je veoma važno da je pažljivo sačuvate i skladištite na sigurnom mestu.



Možete ga napisati na kartonu koji je priložen u kutiji, ili za dodatnu sigurnost, preporučujem graviranje na bazi od nerđajućeg čelika kako biste ga zaštitili od požara, poplave ili urušavanja.



Potvrdite instrukcije, zatim kliknite na dugme "*Create Wallet backup*".



![Image](assets/fr/20.webp)



Safe 3 će kreirati vašu Mnemonic frazu koristeći svoj generator slučajnih brojeva. Uverite se da vas niko ne posmatra tokom ove operacije. Zapišite reči prikazane na ekranu na fizički medij po vašem izboru. U zavisnosti od vaše sigurnosne strategije, možete razmotriti pravljenje nekoliko potpunih fizičkih kopija fraze (ali nipošto je ne delite). Važno je da reči budu numerisane i u sekvencijalnom redosledu.



***Očigledno, nikada ne smete deliti ove reči na Internetu, kao što ja radim u ovom vodiču. Ovaj primer Wallet će biti korišćen samo na Testnet i biće obrisan na kraju vodiča.



Za više informacija o pravilnom načinu čuvanja i upravljanja vašom Mnemonic frazom, toplo preporučujem da pratite ovaj drugi vodič, posebno ako ste početnik:



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

![Image](assets/fr/21.webp)



Da pređete na sledeće reči, kliknite desnim tasterom miša. Možete se vratiti unazad klikom na levi taster. Kada zapišete sve reči, držite pritisnut desni taster da pređete na sledeći korak.



![Image](assets/fr/22.webp)



Odaberite reči u svojoj Mnemonic frazi prema njihovom redosledu da biste potvrdili da ste ih ispravno zapisali. Koristite leve i desne tastere za navigaciju između predloga, a zatim odaberite tačnu reč klikom na 2 tastera istovremeno.



![Image](assets/fr/23.webp)



Kada se ovaj postupak verifikacije završi, kliknite na dugme sa desne strane.



![Image](assets/fr/24.webp)



## Postavljanje PIN koda



Sledeći korak je unos PIN koda. PIN kod otključava vaš Trezor. Stoga pruža zaštitu protiv neovlašćenog fizičkog pristupa. Ovaj PIN kod nije uključen u derivaciju kriptografskih ključeva vašeg Wallet. Dakle, čak i bez pristupa PIN kodu, posedovanje vaše 12-reči Mnemonic fraze omogućiće vam da ponovo dobijete pristup vašim bitcoinima.



Na Trezor Suite, kliknite na "*Continue to PIN*", zatim na dugme "*Set PIN*".



![Image](assets/fr/25.webp)



Potvrdite sa Safe 3.



![Image](assets/fr/26.webp)



Preporučujemo da izaberete PIN kod koji je što je moguće nasumičniji. Obavezno sačuvajte ovaj kod na posebnom mestu od onog gde je vaš Trezor uskladišten (npr. u menadžeru lozinki). Možete definisati PIN kod od 8 do 50 cifara. Preporučujem da izaberete što duži PIN kod kako biste poboljšali sigurnost.



Koristite leve i desne tastere da izaberete svaku cifru. Da potvrdite svoj izbor i pređete na sledeću cifru, pritisnite oba tastera istovremeno.



![Image](assets/fr/27.webp)



Kada završite, kliknite na "*ENTER*" kvačicu na početku cifara, zatim potvrdite svoj PIN drugi put.



![Image](assets/fr/28.webp)



Vaš PIN kod je registrovan.



![Image](assets/fr/29.webp)



Na Trezor Suite, kliknite na dugme "*Complete setup*".



![Image](assets/fr/30.webp)



Konfiguracija vašeg Safe 3 je sada završena. Ako želite, možete promeniti ime i početnu stranicu vašeg Hardware Wallet.



![Image](assets/fr/31.webp)



Više nam neće trebati softver Trezor Suite, osim za redovno ažuriranje firmvera na vašem Hardware Wallet, ili ako želite da izvršite test oporavka. Sada ćemo koristiti Sparrow za upravljanje portfoliom, jer je ovaj softver savršeno prilagođen za korišćenje isključivo sa Bitcoin.



## Postavljanje portfolija na Sparrow Wallet



Počnite preuzimanjem i instaliranjem Sparrow Wallet [sa zvaničnog sajta](https://sparrowwallet.com/) na vašem računaru, ako to već niste učinili.



Kada otvorite Sparrow Wallet, proverite da li je softver povezan sa Bitcoin čvorom, što je označeno kvačicom u donjem desnom uglu Interface. Ako imate problema sa povezivanjem Sparrow-a, preporučujem da pročitate početak ovog vodiča:



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Kliknite na karticu "*File*", zatim na "*New Wallet*".



![Image](assets/fr/32.webp)



Imenujte svoj portfelj, zatim kliknite na "*Create Wallet*".



![Image](assets/fr/33.webp)



U padajućem meniju "*Script Type*", izaberite tip skripta koji će se koristiti za obezbeđivanje vaših bitkoina. Preporučujem "*Taproot*", ili ako to nije moguće, "*Native SegWit*".



![Image](assets/fr/34.webp)



Kliknite na dugme "*Connected Hardware Wallet*". Vaš Safe 3 naravno mora biti povezan sa računarom i otključan.



![Image](assets/fr/35.webp)



Kliknite na dugme "*Scan*". Vaš Safe 3 bi trebalo da se pojavi. Kliknite na "*Import Keystore*".



![Image](assets/fr/36.webp)



Sada možete videti detalje vašeg Wallet, uključujući prošireni javni ključ vašeg prvog naloga. Kliknite na dugme "*Apply*" da finalizujete kreiranje Wallet.



![Image](assets/fr/37.webp)



Izaberite jaku lozinku za siguran pristup Sparrow Wallet. Ova lozinka će osigurati siguran pristup vašim podacima na Sparrow Wallet, štiteći vaše javne ključeve, adrese, oznake i istoriju transakcija od neovlašćenog pristupa.



Preporučujem ti da sačuvaš ovu lozinku u menadžeru lozinki kako je ne bi zaboravio.



![Image](assets/fr/38.webp)



A sada je vaš portfolio uvezen u Sparrow Wallet!



![Image](assets/fr/39.webp)



Pre nego što primite svoje prve bitkoine u vaš Wallet, **snažno vam savetujem da izvršite test praznog oporavka**. Zapišite neke referentne informacije, kao što je vaš xpub, zatim resetujte vaš Trezor Safe 3 dok je Wallet još uvek prazan. Zatim pokušajte da obnovite vaš Wallet na Trezoru koristeći vaše papirne rezervne kopije. Proverite da li se xpub generisan nakon obnove poklapa sa onim koji ste prvobitno zapisali. Ako se poklapa, možete biti sigurni da su vaše papirne rezervne kopije pouzdane.



Da biste saznali više o tome kako izvršiti test oporavka, predlažem da pogledate ovaj drugi vodič:



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Kako mogu primiti bitkoine sa Trezor Safe 3?



Na Sparrow-u, kliknite na karticu "*Receive*".



![Image](assets/fr/40.webp)



Pre nego što upotrebite Address predložen od strane Sparrow Wallet, proverite ga na ekranu vašeg Trezora. Ova praksa vam omogućava da potvrdite da Address prikazan na Sparrow nije prevarantski, i da Hardware Wallet zaista poseduje privatni ključ potreban za kasnije trošenje bitkoina osiguranih ovim Address. Ovo vam pomaže da izbegnete nekoliko vrsta napada.



Da biste izvršili ovu proveru, kliknite na dugme "*Display Address*".



![Image](assets/fr/41.webp)



Proverite da li se Address prikazan na vašem Trezoru poklapa sa onim na Sparrow Wallet. Takođe je preporučljivo izvršiti ovu proveru neposredno pre nego što saopštite vaš Address pošiljaocu, kako biste bili sigurni u njegovu validnost. Možete koristiti dugmad za potvrdu.



![Image](assets/fr/42.webp)



Zatim možete dodati "*Label*" da opišete izvor bitkoina koji će biti osiguran ovim Address. Ovo je dobra praksa koja vam omogućava bolje upravljanje vašim UTXO-ima.



![Image](assets/fr/43.webp)



Zatim možete koristiti ovaj Address za primanje bitkoina.



![Image](assets/fr/44.webp)



## Kako da pošaljem bitkoine sa Trezor Safe 3?



Sada kada ste primili svoje prve Satss na vašem Safe 3-osiguranom Wallet, možete ih i potrošiti! Povežite vaš Trezor sa računarom, otključajte ga koristeći PIN kod, pokrenite Sparrow Wallet, zatim idite na karticu "*Send*" da biste napravili novu transakciju.



![Image](assets/fr/45.webp)



Ako želite da koristite *Coin Control*, tj. da specifično izaberete koje UTXO-e želite da potrošite u transakciji, idite na karticu "*UTXOs*". Izaberite UTXO-e koje želite da potrošite, zatim kliknite na "*Send Selected*". Bićete preusmereni na isti ekran u kartici "*Send*", ali sa već izabranim UTXO-ima za transakciju.



![Image](assets/fr/46.webp)



Unesite odredište Address. Takođe možete uneti više adresa klikom na dugme "*+ Dodaj*".



![Image](assets/fr/47.webp)



Napišite "*Oznaku*" da biste zapamtili svrhu ovog troška.



![Image](assets/fr/48.webp)



Izaberite iznos koji će biti poslat na ovaj Address.



![Image](assets/fr/49.webp)



Prilagodite stopu naknade vaše transakcije prema trenutnom tržištu. Na primer, možete koristiti [Mempool.space](https://Mempool.space/) da odaberete odgovarajuću stopu naknade.



Proverite da su svi parametri vaše transakcije ispravni, a zatim kliknite na "*Create Transaction*".



![Image](assets/fr/50.webp)



Ako vam sve odgovara, kliknite na "*Finalize Transaction for Signing*".



![Image](assets/fr/51.webp)



Kliknite na "*Sign*".



![Image](assets/fr/52.webp)



Kliknite na "*Sign*" pored vašeg Trezor Safe 3.



![Image](assets/fr/53.webp)



Proverite parametre transakcije na vašem Hardware Wallet ekranu, uključujući primaočev prijemni Address, poslati iznos i naknadu. Kada je transakcija verifikovana na Trezoru, kliknite na oba dugmeta istovremeno da je potpišete.



![Image](assets/fr/54.webp)



Vaša transakcija je sada potpisana. Proverite još jednom da je sve u redu, a zatim kliknite na "*Broadcast Transaction*" da biste je emitovali na Bitcoin mreži.



![Image](assets/fr/55.webp)



Možete ga pronaći u kartici "*Transactions*" na Sparrow Wallet.



![Image](assets/fr/56.webp)



Čestitamo, sada ste upoznati sa osnovnom upotrebom Trezor Safe 3 sa Sparrow Wallet! Da biste otišli korak dalje, preporučujem ovaj sveobuhvatan vodič o korišćenju Hardware Wallet Trezora sa passphrase BIP39 kako biste poboljšali svoju sigurnost:



https://planb.network/tutorials/wallet/backup/trezor-passphrase-0474b5bf-496f-4f97-aefe-445368fdca42

Ako ste smatrali ovaj vodič korisnim, bio bih zahvalan ako biste ostavili Green palac ispod. Slobodno podelite ovaj članak na svojim društvenim mrežama. Hvala vam puno!