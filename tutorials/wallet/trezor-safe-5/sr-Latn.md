---
name: Trezor Safe 5
description: Konfigurisanje i korišćenje Hardware Wallet Safe 5
---
![cover](assets/cover.webp)



*Kredit za sliku: [Trezor.io](https://trezor.io/)*



Trezor Safe 5 je najnovija generacija Hardware Wallet koju je dizajnirao SatoshiLabs i lansirana je 2024. godine. Pozicionirana je kao vrhunska verzija Safe 3, sa fokusom na ergonomiju i izdržljivost. Koristi iste sigurnosne napretke kao i njen prethodnik, Safe 3, u poređenju sa Model One i Model T.



Po ceni od 169 €, Safe 5 je pozicioniran u kategoriji visokog ranga Hardware Wallet, takmičeći se sa modelima kao što su Coldcard, Ledger Nano X i Flex, Jade Plus, Passport i Bitbox.



Safe 5 se odlikuje svojim 1,54-inčnim kolor ekranom osetljivim na dodir, zaštićenim *Gorilla Glass 3* staklom, koje je otporno na udarce i ogrebotine. Takođe je opremljen *Trezor Touch* haptičkim motorom koji emituje male vibracije kada se dodirne. Kao i Safe 3, uključuje Secure Element i radi putem USB-C veze, uz dodatak Micro SD porta.



Glavna razlika između Safe 3 i Safe 5 leži u kvalitetu uređaja, osim aspekata bezbednosti. Značajno poboljšava korisničko iskustvo, sa glatkijim radom i udobnijim ekranom. U pogledu bezbednosti, ekvivalentni su.



![Image](assets/fr/01.webp)



Safe 5 ima sve osnovne funkcije koje biste očekivali od dobrog Hardware Wallet, uključujući odličnu integraciju passphrase BIP39. Međutim, još uvek ne podržava Miniscript.



Ovaj model je posebno pogodan za početnike i korisnike srednjeg nivoa. S druge strane, možda neće ispuniti sva očekivanja naprednih korisnika koji traže specifičnije funkcije dostupne na uređajima kao što je Coldcard. Ipak, ako vam nisu potrebne ove napredne opcije, Trezor Safe 5 može biti odličan izbor.



## Trezor Safe 5 sigurnosni model



Kao i Safe 3, Trezor Safe 5 je opremljen sa EAL6+ sertifikovanim **Secure Element**, što predstavlja značajan napredak u odnosu na ranije modele kao što su Model One i Model T. Ovo je OPTIGA Trust M V3 čip, koji ne skladišti seed direktno, već deluje kao kriptografska komponenta za osiguranje pristupa njemu. Secure Element zadržava tajnu kojoj se može pristupiti samo kada korisnik ispravno unese PIN. Ova tajna se zatim koristi za dešifrovanje seed, koji je enkriptovan skladišten u glavnoj memoriji uređaja.



Ovaj hibridni sigurnosni sistem nudi poboljšanu fizičku zaštitu, posebno protiv napada ekstrakcije ili invazivne analize, problema kojima je Model One bio sklon, naročito u upravljanju PIN-om. Ove ranjivosti su sada zaobiđene zahvaljujući upotrebi Secure Element-a. Ovaj model takođe održava softversku arhitekturu otvorenog koda: kod koji upravlja generisanjem i korišćenjem privatnih ključeva ostaje potpuno dostupan i proverljiv. OPTIGA čip upravlja samo PIN kodom, elementom koji je eksterni za Bitcoin Wallet upravljanje ključevima. Ograničen je na oslobađanje tajne koja se može koristiti za dešifrovanje seed. Takođe, OPTIGA Trust M V3 čip ima relativno slobodnu licencu, koja ovlašćuje SatoshiLabs da slobodno objavljuje potencijalne ranjivosti (bez NDA).



Ovaj bezbednosni model predstavlja, po mom mišljenju, jedan od najboljih kompromisa dostupnih na tržištu danas. Kombinuje prednosti Secure Element-a sa upravljanjem softverom otvorenog koda. Prethodno su korisnici morali da biraju između poboljšane fizičke sigurnosti sa čipom i transparentnosti sa otvorenim kodom; sa Trezor Safe, moguće je imati koristi od oba.



U ovom vodiču naučićete kako da konfigurišete i bezbedno koristite svoj Trezor Safe 5.



## Raspakivanje Trezor Safe 5



Kada primite svoj Safe 5, proverite da li su kutija i Seal netaknuti kako biste potvrdili da paket nije otvaran. Provera autentičnosti i integriteta uređaja putem softvera će takođe biti izvršena kada se kasnije postavi.



Sadržaj kutije uključuje :




- Trezor Safe 5;
- Torba koja sadrži karton za beleženje vaše Mnemonic fraze, nalepnice i uputstva;
- USB-C na USB-C kabl.



Kada se otvori, vaš Trezor Safe 5 treba da bude zaštićen zaštitnom plastikom, a USB-C port treba da bude osiguran holografskim Seal. Uverite se da je tu.



![Image](assets/fr/02.webp)



Navigacija na uređaju je prilično intuitivna:




- Dodirnite donju polovinu ekrana da biste se kretali napred;
- Prevucite nadole da se vratite ;
- Pritisnite i držite ekran da potvrdite operaciju.



## Preduslovi



Za ovaj vodič, pokazaću vam kako da koristite Trezor Safe 5 sa [Sparrow Wallet softverom za upravljanje portfoliom](https://sparrowwallet.com/download/). Ako još niste instalirali ovaj softver, molimo vas da to uradite sada. Ako vam je potrebna pomoć, imamo i detaljan vodič o konfigurisanju Sparrow Wallet :



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Trebaće vam i softver Trezor Suite da konfigurišete Safe 5, proverite njegovu autentičnost i instalirate firmware. Ovaj softver ćemo koristiti samo za to, a nakon toga će biti potreban samo za ažuriranja firmware-a. Za svakodnevno upravljanje Wallet, koristićemo isključivo Sparrow Wallet, jer je optimizovan za Bitcoin i lak za korišćenje, čak i za početnike (Sparrow podržava samo Bitcoin, ne altcoine).



[Preuzmite Trezor Suite sa zvaničnog sajta](https://trezor.io/trezor-suite)



![Image](assets/fr/03.webp)



Za oba ova programa, toplo preporučujem da proverite i njihovu autentičnost (sa GnuPG) i njihov integritet (preko Hash) pre nego što ih instalirate na svoj računar. Ako ne znate kako to da uradite, možete pratiti ovaj drugi vodič :



https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

## Pokretanje Trezor Safe 5



Povežite svoj Safe 5 sa računarom na kojem su već instalirani Trezor Suite i Sparrow Wallet.



![Image](assets/fr/04.webp)



Otvorite Trezor Suite, zatim kliknite na "*Set up my Trezor*".



![Image](assets/fr/05.webp)



Odaberite "*Bitcoin-only firmware*", zatim kliknite na "*Install Bitcoin-only*".



![Image](assets/fr/06.webp)



Trezor Suite će zatim instalirati firmver na vaš Safe 5. Molimo sačekajte tokom instalacije.



![Image](assets/fr/07.webp)



Kliknite na "*Continue*".



![Image](assets/fr/08.webp)



Zatim nastavite sa testom autentičnosti kako biste bili sigurni da vaš Hardware Wallet nije lažan ili kompromitovan.



![Image](assets/fr/09.webp)



Na vašem Safe 5, pritisnite ekran da potvrdite.



![Image](assets/fr/10.webp)



Ako je vaš Trezor originalan, poruka o potvrdi će se pojaviti u Trezor Suite.



![Image](assets/fr/11.webp)



Zatim možete preskočiti prozore sa osnovnim uputstvima za rad.



![Image](assets/fr/12.webp)



## Kreiranje Bitcoin portfolija



Na Trezor Suite, kliknite na dugme "*Create new Wallet*".



![Image](assets/fr/13.webp)



Da biste kreirali standardni BIP39 Wallet, započnite izborom "*Legacy Wallet backup types*" iz padajućeg menija, zatim odaberite između 12- ili 24-reči Mnemonic fraze (12 reči se trenutno preporučuje). Ovo će vam omogućiti da kreirate klasični single-sig portfolio. Savetujem vam da ovde odaberete parametre koji su u skladu sa BIP39, kako biste olakšali povrat i izbegli ograničenja na specifično okruženje. Da biste završili, kliknite na "*Create Wallet*".



Ako želite da saznate više o drugim opcijama bekapa dostupnim na Trezoru, uključujući *Multi-share Backup*, preporučujem da pogledate i ovaj vodič:



https://planb.network/tutorials/wallet/backup/trezor-shamir-backup-7f98b593-face-48fb-a643-0e811b87c94e


![Image](assets/fr/14.webp)



Prihvatite uslove korišćenja na Hardware Wallet.



![Image](assets/fr/15.webp)



Pritisnite i držite ekran da biste kreirali novi portfolio.



![Image](assets/fr/16.webp)



U Trezor Suite, kliknite na "*Continue to backup*".



![Image](assets/fr/17.webp)



Softver pruža uputstva o tome kako upravljati vašom Mnemonic frazom.



Ovaj Mnemonic vam daje potpuni, neograničeni pristup svim vašim bitcoinima. Svako ko poseduje ovu frazu može ukrasti vaša sredstva, čak i bez fizičkog pristupa vašem Trezor Safe 5.



Fraza od 12 reči vraća pristup vašim bitkoinima u slučaju gubitka, krađe ili oštećenja vašeg Hardware Wallet. Stoga je veoma važno da je pažljivo sačuvate i skladištite na sigurnom mestu.



Možete ga napisati na kartonu koji je priložen u kutiji, ili za dodatnu sigurnost, preporučujem graviranje na bazi od nerđajućeg čelika kako biste ga zaštitili od požara, poplave ili urušavanja.



Potvrdite instrukcije, zatim kliknite na dugme "*Create Wallet backup*".



![Image](assets/fr/18.webp)



Safe 5 će kreirati vašu Mnemonic frazu koristeći svoj generator slučajnih brojeva. Uverite se da vas niko ne posmatra tokom ove operacije. Zapišite reči prikazane na ekranu na fizički medij po vašem izboru. U zavisnosti od vaše sigurnosne strategije, možete razmotriti pravljenje nekoliko potpunih fizičkih kopija fraze (ali pre svega, nemojte je deliti). Važno je da reči budu numerisane i u sekvencijalnom redosledu.



***Očigledno, nikada ne smete deliti ove reči na Internetu, kao što to činim u ovom vodiču. Ovaj primer Wallet će biti korišćen samo na Testnet i biće obrisan na kraju vodiča.



Za više informacija o pravilnom načinu čuvanja i upravljanja vašom Mnemonic frazom, toplo preporučujem da pratite ovaj drugi vodič, posebno ako ste početnik:



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

![Image](assets/fr/19.webp)



Da biste prešli na sledeće reči, kliknite na dno ekrana. Možete se vratiti unazad prevlačenjem nadole. Kada zapišete sve reči, držite prst na ekranu da biste prešli na sledeći korak.



![Image](assets/fr/20.webp)



Odaberite reči u svojoj Mnemonic frazi prema njihovom redosledu da biste potvrdili da ste ih ispravno zapisali.



![Image](assets/fr/21.webp)



Kada se ovaj postupak verifikacije završi, kliknite na ekran da biste nastavili.



![Image](assets/fr/22.webp)



## Postavljanje PIN koda



Sledeći korak je unos PIN koda. PIN kod otključava vaš Trezor. Stoga pruža zaštitu protiv neovlašćenog fizičkog pristupa. Ovaj PIN kod nije uključen u izvođenje kriptografskih ključeva vašeg Wallet. Dakle, čak i bez pristupa PIN kodu, posedovanje vaše 12-reči Mnemonic fraze omogućiće vam da ponovo dobijete pristup vašim bitcoinima.



Na Trezor Suite, kliknite na "*Continue to PIN*", zatim na dugme "*Set PIN*".



![Image](assets/fr/23.webp)



Potvrdi sa Safe 5.



![Image](assets/fr/24.webp)



Preporučujemo da izaberete PIN kod koji je što je moguće nasumičniji. Obavezno sačuvajte ovaj kod na posebnom mestu od onog gde je vaš Trezor uskladišten (npr. u menadžeru lozinki). Možete definisati PIN kod između 8 i 50 cifara. Preporučujem da izaberete što duži PIN kod kako biste poboljšali sigurnost.



Koristite touchpad za unos PIN-a.



![Image](assets/fr/25.webp)



Kada završite, kliknite na Green oznaku u donjem desnom uglu, zatim potvrdite svoj PIN po drugi put.



![Image](assets/fr/26.webp)



Vaš PIN kod je registrovan.



![Image](assets/fr/27.webp)



Na Trezor Suite, kliknite na dugme "*Complete setup*".



![Image](assets/fr/28.webp)



Konfiguracija vašeg Safe 5 je sada završena. Ako želite, možete promeniti ime i početnu stranicu vašeg Hardware Wallet.



![Image](assets/fr/29.webp)



Više nam neće biti potreban softver Trezor Suite, osim za redovno ažuriranje firmvera na vašem Hardware Wallet, ili ako želite da izvršite test oporavka. Sada ćemo koristiti Sparrow za upravljanje portfoliom, jer je ovaj softver savršeno prilagođen za korišćenje isključivo sa Bitcoin.



## Postavljanje portfolija na Sparrow Wallet



Počnite preuzimanjem i instaliranjem Sparrow Wallet [sa zvaničnog sajta](https://sparrowwallet.com/) na vašem računaru, ako to već niste uradili.



Kada otvorite Sparrow Wallet, proverite da li je softver povezan sa Bitcoin čvorom, što je označeno kvačicom u donjem desnom uglu Interface. Ako imate problema sa povezivanjem Sparrow-a, preporučujem da pogledate početak ovog vodiča:



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Kliknite na karticu "*File*", zatim na "*New Wallet*".



![Image](assets/fr/30.webp)



Nazovite svoj portfolio, zatim kliknite na "*Create Wallet*".



![Image](assets/fr/31.webp)



U padajućem meniju "*Script Type*", izaberite tip skripta koji će se koristiti za obezbeđivanje vaših bitkoina. Preporučujem "*Taproot*", ili ako to nije moguće, "*Native SegWit*".



![Image](assets/fr/32.webp)



Kliknite na dugme "*Connected Hardware Wallet*". Vaš Safe 5 mora naravno biti povezan sa računarom i otključan.



Kada povežete svoj Safe 5 sa računarom sa otvorenim Sparrow Wallet, bićete upitani da unesete passphrase BIP39 na ekranu Hardware Wallet. Ova napredna opcija će biti obrađena u budućem tutorijalu. Za sada, možete jednostavno kliknuti na Green kvačicu u gornjem desnom uglu da potvrdite da želite koristiti prazan passphrase (tj. bez passphrase). Da biste sprečili da vas Trezor pita da unesete passphrase svaki put kada ga pokrenete, idite na Trezor Suite, pristupite podešavanjima i promenite opciju u "*Device*" > "*Wallet default*" na "*Standard*" umesto "*passphrase*".



![Image](assets/fr/33.webp)



Kliknite na dugme "*Scan*". Trebalo bi da se pojavi vaš Safe 5. Kliknite na "*Import Keystore*".



![Image](assets/fr/34.webp)



Sada možete videti detalje vašeg Wallet, uključujući prošireni javni ključ vašeg prvog naloga. Kliknite na dugme "*Apply*" da finalizujete kreiranje Wallet.



![Image](assets/fr/35.webp)



Izaberite jaku lozinku za osiguranje pristupa Sparrow Wallet. Ova lozinka će osigurati siguran pristup vašim Sparrow Wallet podacima, štiteći vaše javne ključeve, adrese, oznake i istoriju transakcija od neovlašćenog pristupa.



Savetujem ti da sačuvaš ovu lozinku u menadžeru lozinki kako je ne bi zaboravio.



![Image](assets/fr/36.webp)



A sada je vaš portfolio uvezen u Sparrow Wallet!



![Image](assets/fr/37.webp)



Pre nego što primite svoje prve bitkoine u vaš Wallet, **snažno vam savetujem da izvršite test praznog oporavka**. Zapišite neke referentne informacije, kao što je vaš xpub, zatim resetujte vaš Trezor Safe 5 dok je Wallet još uvek prazan. Zatim pokušajte da obnovite vaš Wallet na Trezoru koristeći vaše papirne rezervne kopije. Proverite da li se xpub generisan nakon obnove poklapa sa onim koji ste prvobitno zapisali. Ako se poklapa, možete biti sigurni da su vaše papirne rezervne kopije pouzdane.



Da biste saznali više o tome kako izvršiti test oporavka, predlažem da pogledate ovaj drugi vodič:



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Kako mogu primiti bitkoine sa Trezor Safe 5?



Na Sparrow-u, kliknite na karticu "*Receive*".



![Image](assets/fr/38.webp)



Pre nego što upotrebite Address koji predlaže Sparrow Wallet, proverite ga na ekranu vašeg Trezora. Ova praksa vam omogućava da potvrdite da Address prikazan na Sparrow nije prevarantski, i da Hardware Wallet zaista poseduje privatni ključ potreban za kasnije trošenje bitkoina osiguranih ovim Address. Ovo vam pomaže da izbegnete nekoliko vrsta napada.



Da biste izvršili ovu proveru, kliknite na dugme "*Prikaži Address*".



![Image](assets/fr/39.webp)



Proverite da li se Address prikazan na vašem Trezoru poklapa sa onim na Sparrow Wallet. Takođe je preporučljivo izvršiti ovu proveru neposredno pre nego što saopštite vaš Address pošiljaocu, kako biste bili sigurni u njegovu validnost. Možete pritisnuti ekran da potvrdite.



![Image](assets/fr/40.webp)



Zatim možete dodati "*Label*" da opišete izvor bitcoina koji će biti osiguran ovim Address. Ovo je dobra praksa koja vam omogućava bolje upravljanje vašim UTXO-ima.



![Image](assets/fr/41.webp)



Možete zatim koristiti ovaj Address za primanje bitkoina.



![Image](assets/fr/42.webp)



## Kako da pošaljem bitkoine sa Trezor Safe 5?



Sada kada ste primili svoje prve Satss na vašem Safe 5-secured Wallet, možete ih i potrošiti! Povežite vaš Trezor sa računarom, otključajte ga PIN kodom, pokrenite Sparrow Wallet, zatim idite na karticu "*Send*" da biste napravili novu transakciju.



![Image](assets/fr/43.webp)



Ako želite da koristite *Coin Control*, tj. da specifično izaberete koje UTXO-e želite da potrošite u transakciji, idite na karticu "*UTXOs*". Izaberite UTXO-e koje želite da potrošite, zatim kliknite na "*Send Selected*". Bićete preusmereni na isti ekran u kartici "*Send*", ali sa vašim već izabranim UTXO-ima za transakciju.



![Image](assets/fr/44.webp)



Unesite odredište Address. Takođe možete uneti više adresa klikom na dugme "*+ Dodaj*".



![Image](assets/fr/45.webp)



Napišite "*Oznaku*" da biste zapamtili svrhu ovog troška.



![Image](assets/fr/46.webp)



Izaberite iznos koji će biti poslat na ovaj Address.



![Image](assets/fr/47.webp)



Prilagodite stopu naknade vaše transakcije prema trenutnom tržištu. Na primer, možete koristiti [Mempool.space](https://Mempool.space/) da odaberete odgovarajuću stopu naknade.



Uverite se da su svi parametri vaše transakcije ispravni, a zatim kliknite na "*Create Transaction*".



![Image](assets/fr/48.webp)



Ako je sve po vašem zadovoljstvu, kliknite na "*Finalize Transaction for Signing*".



![Image](assets/fr/49.webp)



Kliknite na "*Sign*".



![Image](assets/fr/50.webp)



Kliknite na "*Sign*" pored vašeg Trezor Safe 5.



![Image](assets/fr/51.webp)



Proverite parametre transakcije na vašem Hardware Wallet ekranu, uključujući prijemni Address primaoca, poslati iznos i naknadu. Kada transakcija bude verifikovana na Trezoru, pritisnite i držite ekran da biste je potpisali.



![Image](assets/fr/52.webp)



Vaša transakcija je sada potpisana. Proverite još jednom da je sve u redu, a zatim kliknite na "*Broadcast Transaction*" da biste je emitovali na Bitcoin mreži.



![Image](assets/fr/53.webp)



Možete ga pronaći na kartici "*Transactions*" u Sparrow Wallet.



![Image](assets/fr/54.webp)



Čestitamo, sada ste upoznati sa osnovnom upotrebom Trezor Safe 5 sa Sparrow Wallet! Da biste otišli korak dalje, preporučujem ovaj sveobuhvatni vodič o korišćenju Trezor Hardware Wallet sa passphrase BIP39 za poboljšanje vaše sigurnosti:



https://planb.network/tutorials/wallet/backup/trezor-passphrase-0474b5bf-496f-4f97-aefe-445368fdca42

Ako ste našli ovaj vodič korisnim, bio bih zahvalan ako biste ostavili Green palac ispod. Slobodno podelite ovaj članak na vašim društvenim mrežama. Hvala vam puno!