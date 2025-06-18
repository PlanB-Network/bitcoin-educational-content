---
name: Trezor Model One
description: Postavljanje i korišćenje Hardware Wallet Model One
---
![cover](assets/cover.webp)



*Image credit: [Trezor.io](https://trezor.io/)*



Trezor Model One je prvi Hardware Wallet ikada objavljen, lansiran 2014. godine od strane SatoshiLabs. Nakon više od deset godina postojanja, ostaje zanimljiv izbor, posebno za korisnike koji traže Hardware Wallet koji je pristupačan kako tehnički, tako i u smislu budžeta. Zapravo, cena mu je €49 na zvaničnom Trezor sajtu. To je jedan od retkih hardverskih novčanika u ovom cenovnom rangu. Nalazi se između uređaja početnog nivoa oko €20, kao što je Tapsigner, koji često nemaju ekran, i uređaja srednjeg ranga oko €80, kao što su Ledger Nano S Plus ili Trezor Safe 3.



Model One ima 0,96-inčni monohromatski OLED ekran i dva fizička dugmeta. Radi bez baterije, koristeći samo mikro-USB konekciju za napajanje i podatke Exchange.



![Image](assets/fr/01.webp)



Glavni nedostatak Modela One je nedostatak Secure Element-a, što ga čini ranjivim na razne fizičke napade, od kojih su neki relativno jednostavni za izvođenje. Ovi napadi mogu uključivati analizu pomoćnih kanala kako bi se odredio PIN uređaja, ili naprednije tehnike za ekstrakciju šifrovanog seed kako bi se kasnije izvršio brute-force napad. Imajte na umu da ovi napadi zahtevaju fizički pristup uređaju. Međutim, ova ranjivost se može značajno smanjiti korišćenjem solidnog passphrase BIP39. Ako se odlučite za ovaj Hardware Wallet, toplo vam savetujem da konfigurišete passphrase.



Model One nudi dve važne prednosti:




- Zasniva se na potpuno otvorenoj arhitekturi. Za razliku od novijih modela sa Secure Element, svi hardverski i softverski komponenti Model One su proverljivi;
- Opremljen je ekranom. Koliko je meni poznato, ovo je jedini Hardware Wallet na tržištu u ovom cenovnom rangu sa displejom. Ovo je veoma važna karakteristika, jer omogućava proveru potpisanih informacija i adresa za prijem, čime se sprečavaju mnogi digitalni napadi.



Trezor Model One može stoga predstavljati mudar izbor za početnike i korisnike srednjeg nivoa sa ograničenim budžetom. Međutim, važno je biti svestan njegovih ograničenja u pogledu fizičke zaštite, zbog odsustva Secure Element-a. Ako vam je budžet ograničen, ovo je dobra opcija, ali ako možete priuštiti superiorniji model, kao što je Trezor Safe 3 po ceni od €79, to je poželjnije, jer uključuje Secure Element.



## Raspakivanje Trezor Model One



Kada primite svoj Model One, proverite da li su kutija i Seal netaknuti kako biste potvrdili da paket nije otvaran. Softverska verifikacija autentičnosti i integriteta uređaja će takođe biti izvršena kada se kasnije postavi.



Sadržaj kutije uključuje :




- Trezor Model One;
- Kartonski papir za beleženje vaše Mnemonic fraze, nalepnice i uputstva;
- USB-A to micro-USB kabl.



![Image](assets/fr/02.webp)



Navigacija uređajem je veoma jednostavna:




- Desni klik da potvrdite i pređete na sledeće korake;
- Koristite levi taster da se vratite nazad.



## Preduslovi



Za ovaj vodič, pokazaću vam kako da koristite Trezor Model One sa [Sparrow Wallet softverom za upravljanje portfoliom](https://sparrowwallet.com/download/). Ako još niste instalirali ovaj softver, molimo vas da to učinite sada. Ako vam je potrebna pomoć, imamo i detaljan vodič o konfigurisanju Sparrow Wallet :



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Trebaće vam i softver Trezor Suite da biste konfigurisali Model One, proverili njegovu autentičnost i instalirali firmver. Ovaj softver ćemo koristiti samo za to, a nakon toga će biti potreban samo za ažuriranja firmvera. Za svakodnevno upravljanje Wallet koristićemo isključivo Sparrow Wallet, jer je optimizovan za Bitcoin i lak za korišćenje, čak i za početnike (Sparrow podržava samo Bitcoin, ne altcoine).



[Preuzmite Trezor Suite sa zvaničnog sajta](https://trezor.io/trezor-suite)



![Image](assets/fr/03.webp)



Za oba ova programa, toplo preporučujem da proverite i njihovu autentičnost (pomoću GnuPG) i njihov integritet (preko Hash) pre nego što ih instalirate na svoj računar. Ako ne znate kako to da uradite, možete pratiti ovaj drugi vodič :



https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

## Pokretanje Trezor Model One



Povežite svoj Model One sa računarom na kojem su već instalirani Trezor Suite i Sparrow Wallet.



![Image](assets/fr/04.webp)



Otvorite Trezor Suite, zatim kliknite na "*Set up my Trezor*".



![Image](assets/fr/05.webp)



Odaberite "*Bitcoin-only firmware*", zatim kliknite na "*Install Bitcoin-only*".



![Image](assets/fr/06.webp)



Trezor Suite će zatim instalirati firmware na vaš Model One. Molimo sačekajte tokom instalacije.



![Image](assets/fr/07.webp)



Kliknite na "*Continue*".



![Image](assets/fr/08.webp)



## Kreiranje Bitcoin portfolija



Na Trezor Suite, kliknite na dugme "*Create new Wallet*".



![Image](assets/fr/09.webp)



Prihvatite uslove korišćenja na Hardware Wallet.



![Image](assets/fr/10.webp)



U Trezor Suite, kliknite na "*Nastavi sa pravljenjem rezervne kopije*".



![Image](assets/fr/11.webp)



Softver pruža uputstva o tome kako upravljati vašom Mnemonic frazom.



Ovaj Mnemonic vam daje potpuni, neograničeni pristup svim vašim bitcoinima. Svako ko poseduje ovu frazu može ukrasti vaša sredstva, čak i bez fizičkog pristupa vašem Trezor Model One.



Fraza od 24 reči vraća pristup vašim bitcoinima u slučaju gubitka, krađe ili loma vašeg Hardware Wallet. Stoga je veoma važno da je pažljivo sačuvate i skladištite na sigurnom mestu.



Možete ga napisati na kartonu koji je priložen u kutiji, ili za dodatnu sigurnost, preporučujem graviranje na bazi od nerđajućeg čelika kako biste ga zaštitili od požara, poplave ili urušavanja.



Potvrdite instrukcije, zatim kliknite na dugme "*Create Wallet backup*".



![Image](assets/fr/12.webp)



Model One će kreirati vašu Mnemonic frazu koristeći svoj generator slučajnih brojeva. Uverite se da vas niko ne posmatra tokom ove operacije. Zapišite reči prikazane na ekranu na fizički medij po vašem izboru. U zavisnosti od vaše sigurnosne strategije, možete razmotriti pravljenje nekoliko potpunih fizičkih kopija fraze (ali pre svega, nemojte je deliti). Važno je da reči budu numerisane i u sekvencijalnom redosledu.



***Očigledno, nikada ne smete deliti ove reči na Internetu, kao što ja činim u ovom uputstvu. Ovaj primer Wallet će biti korišćen samo na Testnet i biće obrisan na kraju uputstva.



Za više informacija o pravilnom načinu čuvanja i upravljanja vašom Mnemonic frazom, toplo preporučujem da pratite ovaj drugi vodič, posebno ako ste početnik:



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Da biste prešli na sledeće reči, kliknite desnim tasterom miša. Kada zapišete sve reči, ponovo kliknite desnim tasterom da pređete na sledeći korak.



![Image](assets/fr/13.webp)



Vaš Hardware Wallet vam ponovo prikazuje sve vaše reči. Proverite da li ste ih sve zapisali.



![Image](assets/fr/14.webp)



## Postavljanje PIN koda



Sledeći korak je unos PIN koda. PIN kod otključava vaš Trezor. Stoga pruža zaštitu od neovlašćenog fizičkog pristupa. Ovaj PIN kod nije uključen u izvođenje kriptografskih ključeva vašeg Wallet. Dakle, čak i bez pristupa PIN kodu, posedovanje vaše 12-reči Mnemonic fraze omogućiće vam da ponovo dobijete pristup vašim bitcoinima.



Na Trezor Suite, kliknite na "*Continue to PIN*", zatim na dugme "*Set PIN*".



![Image](assets/fr/15.webp)



Potvrdi na Model One.



![Image](assets/fr/16.webp)



Preporučujemo da izaberete PIN kod koji je što je moguće nasumičniji. Obavezno sačuvajte ovaj kod na posebnom mestu od onog gde je vaš Trezor uskladišten (npr. u menadžeru lozinki). Možete definisati PIN kod od 8 do 50 cifara. Preporučujem da izaberete što duži PIN kod kako biste poboljšali sigurnost.



PIN kod mora biti unet u Trezor Suite na vašem računaru klikom na tačke koje odgovaraju ciframa, prema konfiguraciji tastature prikazanoj na Trezor Model One.



Ova specifična metoda unosa PIN-a je potrebna svaki put kada otključavate svoj Trezor Model One, bilo putem Trezor Suite ili Sparrow Wallet.



![Image](assets/fr/17.webp)



Kada završite, kliknite na dugme "*Unesite PIN*".



![Image](assets/fr/18.webp)



Ponovo unesite svoj PIN za potvrdu.



![Image](assets/fr/19.webp)



Na Trezor Suite, kliknite na dugme "*Complete setup*".



![Image](assets/fr/20.webp)



Konfiguracija vašeg Model One je sada završena. Ako želite, možete promeniti ime i početnu stranicu vašeg Hardware Wallet.



![Image](assets/fr/21.webp)



Više nam neće trebati softver Trezor Suite, osim za redovno ažuriranje firmvera na vašem Hardware Wallet, ili ako želite da izvršite test oporavka. Sada ćemo koristiti Sparrow za upravljanje portfoliom, jer je ovaj softver savršeno prilagođen za korišćenje isključivo sa Bitcoin.



## Postavljanje portfolija na Sparrow Wallet



Počnite preuzimanjem i instaliranjem Sparrow Wallet [sa zvaničnog sajta](https://sparrowwallet.com/) na vašem računaru, ako to već niste učinili.



Kada otvorite Sparrow Wallet, proverite da li je softver povezan sa Bitcoin čvorom, što je označeno kvačicom u donjem desnom uglu Interface. Ako imate problema sa povezivanjem Sparrow-a, preporučujem da pogledate početak ovog vodiča:



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Kliknite na karticu "*File*", zatim na "*New Wallet*".



![Image](assets/fr/22.webp)



Nazovite svoj portfolio, zatim kliknite na "*Create Wallet*".



![Image](assets/fr/23.webp)



U padajućem meniju "*Script Type*", izaberite tip skripta koji će se koristiti za obezbeđivanje vaših bitkoina. Preporučujem "*Taproot*", ili ako to nije moguće, "*Native SegWit*".



![Image](assets/fr/24.webp)



Kliknite na dugme "*Connected Hardware Wallet*". Vaš Model One mora naravno biti povezan sa računarom.



![Image](assets/fr/25.webp)



Kliknite na dugme "*Scan*". Vaš Model One bi trebalo da se pojavi.



Kada povežete svoj Model One sa računarom sa otvorenim Sparrow Wallet, bićete upitani da unesete passphrase BIP39 na Sparrow. Ova napredna opcija će biti pokrivena u budućem vodiču. Za sada, možete jednostavno izabrati "*Toggle passphrase Off*" da sprečite vaš Trezor da vas pita da unesete passphrase svaki put kada pokrenete uređaj.



https://planb.network/tutorials/wallet/backup/trezor-passphrase-0474b5bf-496f-4f97-aefe-445368fdca42

![Image](assets/fr/26.webp)



Kliknite na "*Importuj Keystore*".



![Image](assets/fr/27.webp)



Sada možete videti detalje vašeg Wallet, uključujući prošireni javni ključ vašeg prvog naloga. Kliknite na dugme "*Apply*" da završite kreiranje Wallet.



![Image](assets/fr/28.webp)



Izaberite jaku lozinku za osiguranje pristupa Sparrow Wallet. Ova lozinka će osigurati siguran pristup vašim podacima na Sparrow Wallet, štiteći vaše javne ključeve, adrese, oznake i istoriju transakcija od neovlašćenog pristupa.



Preporučujem da sačuvaš ovu lozinku u menadžeru lozinki kako je ne bi zaboravio.



![Image](assets/fr/29.webp)



A sada je vaš portfolio uvezen u Sparrow Wallet!



![Image](assets/fr/30.webp)



Pre nego što primite svoje prve bitkoine u vaš Wallet, **snažno vam savetujem da izvršite test praznog oporavka**. Zapišite neke referentne informacije, kao što je vaš xpub, zatim resetujte vaš Trezor Model One dok je Wallet još uvek prazan. Zatim pokušajte da obnovite vaš Wallet na Trezoru koristeći vaše papirne rezervne kopije. Proverite da li se xpub generisan nakon obnove poklapa sa onim koji ste prvobitno zapisali. Ako se poklapa, možete biti sigurni da su vaše papirne rezervne kopije pouzdane.



Da biste saznali više o tome kako izvesti test oporavka, predlažem da pogledate ovaj drugi vodič:



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Kako primiti bitkoine sa Trezor Model One?



Na Sparrow-u, kliknite na karticu "*Receive*".



![Image](assets/fr/31.webp)



Pre nego što upotrebite Address koji predlaže Sparrow Wallet, proverite ga na ekranu vašeg Trezora. Ova praksa vam omogućava da potvrdite da Address prikazan na Sparrow nije prevaran, i da Hardware Wallet zaista poseduje privatni ključ potreban za kasnije trošenje bitkoina osiguranih ovim Address. Ovo vam pomaže da izbegnete nekoliko tipova napada.



Da biste izvršili ovu proveru, kliknite na dugme "*Display Address*".



![Image](assets/fr/32.webp)



Proverite da li se Address prikazan na vašem Trezoru poklapa sa onim na Sparrow Wallet. Takođe je preporučljivo izvršiti ovu proveru neposredno pre nego što saopštite vaš Address pošiljaocu, kako biste bili sigurni u njegovu validnost. Možete pritisnuti desno dugme za potvrdu.



![Image](assets/fr/33.webp)



Takođe možete dodati "*Label*" da opišete izvor bitkoina koji će biti osigurani ovim Address. Ovo je dobra praksa koja vam omogućava bolje upravljanje vašim UTXO-ima.



![Image](assets/fr/34.webp)



Zatim možete koristiti ovaj Address za primanje bitkoina.



![Image](assets/fr/35.webp)



## Kako poslati bitkoine pomoću Trezor Model One?



Sada kada ste primili svoje prve Satss u vašem Model One-osiguranom Wallet, možete ih i potrošiti! Povežite vaš Trezor sa računarom, pokrenite Sparrow Wallet, zatim idite na karticu "*Send*" da biste napravili novu transakciju.



![Image](assets/fr/36.webp)



Ako želite da koristite *Coin Control*, tj. da specifično izaberete koje UTXO-e želite da potrošite u transakciji, idite na karticu "*UTXOs*". Izaberite UTXO-e koje želite da potrošite, zatim kliknite na "*Send Selected*". Bićete preusmereni na isti ekran u kartici "*Send*", ali sa već izabranim UTXO-ima za transakciju.



![Image](assets/fr/37.webp)



Unesite odredište Address. Takođe možete uneti više adresa klikom na dugme "*+ Dodaj*".



![Image](assets/fr/38.webp)



Napišite "*Oznaku*" da biste zapamtili svrhu ovog troška.



![Image](assets/fr/39.webp)



Izaberite iznos koji će biti poslat na ovaj Address.



![Image](assets/fr/40.webp)



Prilagodite stopu naknade vaše transakcije prema trenutnom tržištu. Na primer, možete koristiti [Mempool.space](https://Mempool.space/) da odaberete odgovarajuću stopu naknade.



Proverite da su svi parametri vaše transakcije tačni, zatim kliknite na "*Create Transaction*".



![Image](assets/fr/41.webp)



Ako vam sve odgovara, kliknite na "*Finalize Transaction for Signing*".



![Image](assets/fr/42.webp)



Kliknite na "*Sign*".



![Image](assets/fr/43.webp)



Kliknite na "*Sign*" pored vašeg Trezor Model One.



![Image](assets/fr/44.webp)



Proverite parametre transakcije na vašem Hardware Wallet ekranu, uključujući primateljev prijemni Address, poslati iznos i naknadu. Kada je transakcija verifikovana na Trezoru, desnim klikom je potpišite.



![Image](assets/fr/45.webp)



Vaša transakcija je sada potpisana. Proverite još jednom da je sve u redu, a zatim kliknite na "*Broadcast Transaction*" da biste je emitovali na Bitcoin mreži.



![Image](assets/fr/46.webp)



Možete ga pronaći u kartici "*Transactions*" na Sparrow Wallet.



![Image](assets/fr/47.webp)



Čestitamo, sada ste upoznati sa osnovnom upotrebom Trezor Model One sa Sparrow Wallet! Da biste otišli korak dalje, preporučujem ovaj sveobuhvatni vodič o korišćenju Hardware Wallet Trezora sa passphrase BIP39 kako biste ojačali svoju sigurnost :



https://planb.network/tutorials/wallet/backup/trezor-passphrase-0474b5bf-496f-4f97-aefe-445368fdca42

Ako ste našli ovaj vodič korisnim, bio bih zahvalan ako biste ostavili Green palac ispod. Slobodno podelite ovaj članak na vašim društvenim mrežama. Hvala vam puno!