---
name: Ledger Flex
description: Postavljanje i korišćenje Ledger Flex
---
![cover](assets/cover.webp)


Hardware Wallet je elektronski uređaj posvećen upravljanju i osiguravanju privatnih ključeva Bitcoin Wallet. Za razliku od softverskih novčanika (ili Hot novčanika) instaliranih na mašinama opšte namene koje su često povezane na Internet, hardverski novčanici omogućavaju fizičku izolaciju privatnih ključeva, smanjujući rizike od hakovanja i krađe.


Glavni cilj Hardware Wallet je minimiziranje funkcionalnosti uređaja kako bi se smanjila njegova površina napada. Manja površina napada takođe znači manje potencijalnih vektora napada, tj. manje slabih tačaka u sistemu koje napadači mogu iskoristiti za pristup bitcoinima.


Preporučuje se korišćenje Hardware Wallet za obezbeđivanje vaših bitkoina, posebno ako posedujete značajne iznose, bilo u apsolutnoj vrednosti ili kao proporciju vaših ukupnih sredstava.


Hardverski novčanici se koriste u kombinaciji sa Wallet softverom za upravljanje na računaru ili pametnom telefonu. Ovaj softver upravlja kreiranjem transakcija, ali kriptografski potpis neophodan za validaciju ovih transakcija se vrši samo unutar Hardware Wallet. To znači da privatni ključevi nikada nisu izloženi potencijalno ranjivom okruženju.


Hardverski novčanici nude dvostruku zaštitu za korisnika: s jedne strane, štite vaše bitkoine od daljinskih napada držeći privatne ključeve van mreže, a s druge strane, obično nude bolju fizičku otpornost protiv pokušaja ekstrakcije ključeva. I upravo na osnovu ova 2 sigurnosna kriterijuma može se ocenjivati i rangirati različiti modeli dostupni na tržištu.


U ovom vodiču predlažem da otkrijemo jedno od ovih rešenja: **Ledger Flex**.


![LEDGER FLEX](assets/notext/01.webp)


## Uvod u Ledger Flex


Ledger Flex je Hardware Wallet proizveden od strane francuske kompanije Ledger, koji se prodaje po ceni od 249 €.


![LEDGER FLEX](assets/notext/02.webp)


Sadrži veliki E Ink ekran osetljiv na dodir, tehnologiju crno-belog prikaza. Ovo je ista tehnologija koja se nalazi u elektronskim čitačima. E Ink ekran omogućava jasan i čitljiv prikaz, čak i na jakom suncu, i troši vrlo malo energije, ili je uopšte ne troši kada je ekran statičan. Radi tako što koristi mikrokapsule koje sadrže čestice crnog i belog pigmenta. Kada se primeni električni naboj, crne ili bele čestice se pomeraju na površinu ekrana, čime se omogućava formiranje teksta ili slika.

Ledger Flex je opremljen CC EAL6+ sertifikovanim čipom "secure element", koji vam nudi naprednu zaštitu od fizičkih napada na hardver. Ekran je direktno kontrolisan ovim čipom. Zajednička tačka kritike je da kod za ovaj čip nije open-source, što zahteva određeni nivo poverenja u integritet ove komponente. Međutim, ovaj element je revidiran od strane nezavisnih stručnjaka.


Što se tiče upotrebe, Ledger Flex nudi nekoliko opcija povezivanja: Bluetooth, USB-C i NFC. Veliki ekran omogućava lako proveravanje detalja vaših transakcija. Ledger se takođe izdvaja od svojih konkurenata brzom primenom novih funkcija Bitcoin, kao što je na primer Miniscript.


Nakon testiranja, impresioniran sam kvalitetom proizvoda. Korisničko iskustvo je odlično, a uređaj je intuitivan. To je odličan Hardware Wallet. Međutim, po mom mišljenju, ima 2 velika nedostatka: nemogućnost verifikacije koda čipa i, naravno, njegova cena, koja je značajno viša od konkurenata. Za poređenje, najnapredniji model od Foundation se prodaje za $199, Coinkite-ov za $219.99, dok se najnoviji Trezor, takođe opremljen velikim ekranom na dodir, nudi za 169€.


## Kako kupiti Ledger Flex?


Ledger Flex je dostupan za kupovinu [na zvaničnom sajtu](https://shop.Ledger.com/pages/Ledger-flex). Da biste ga kupili u fizičkoj prodavnici, možete pronaći [listu sertifikovanih prodavaca](https://www.Ledger.com/reseller) na sajtu Ledger.


## Preduslovi


Kada primite svoj Ledger Flex, prvi korak je da pregledate pakovanje kako biste se uverili da nije otvoreno.


![LEDGER FLEX](assets/notext/03.webp)


Pakovanje Ledger treba da sadrži 2 trake za zaptivanje. Ako ove trake nedostaju ili su oštećene, to može ukazivati na to da je Hardware Wallet kompromitovan i možda nije autentičan.


![LEDGER FLEX](assets/notext/04.webp)


Po otvaranju, trebalo bi da pronađete sledeće stavke u kutiji:


- Ledger Flex;
- USB-C kabl;
- Korisnički priručnik;
- Kartice za zapisivanje vaše Mnemonic fraze.


![LEDGER FLEX](assets/notext/05.webp)


Za ovaj vodič, biće vam potrebna 2 softverska programa: Ledger Live za inicijalizaciju Ledger Flex, i Sparrow Wallet za upravljanje vašim Bitcoin Wallet. Preuzmite [Ledger Live](https://www.Ledger.com/Ledger-live) i [Sparrow Wallet](https://sparrowwallet.com/download/) sa njihovih zvaničnih veb-sajtova.


![LEDGER FLEX](assets/notext/06.webp)

Uskoro ćemo ponuditi tutorijal o tome kako proveriti autentičnost i integritet softvera koji preuzimate. Toplo savetujem da to uradite ovde za Ledger Live i Sparrow.

## Kako inicijalizovati Ledger Flex sa Ledger Live?


Uključite svoj Ledger Flex pritiskom na dugme sa desne strane na nekoliko sekundi.


![LEDGER FLEX](assets/notext/07.webp)


Pomerajte se kroz različite uvodne stranice.


![LEDGER FLEX](assets/notext/08.webp)


Odaberite opciju "*Set up without Ledger Live*", zatim kliknite na dugme "*Skip Ledger Live*".


![LEDGER FLEX](assets/notext/09.webp)


Zatim će vam biti zatraženo da izaberete ime za vaš Ledger. Kliknite na "*Set name*", a zatim unesite ime po vašem izboru.


![LEDGER FLEX](assets/notext/10.webp)


Izaberite PIN kod za svoj uređaj, koji će se koristiti za otključavanje vašeg Ledger. Ovo je stoga zaštita protiv neovlašćenog fizičkog pristupa. Ovaj PIN kod ne igra ulogu u derivaciji kriptografskih ključeva vašeg Wallet. Dakle, čak i bez pristupa ovom PIN kodu, posedovanje vaše 24-reči Mnemonic fraze će vam omogućiti da ponovo dobijete pristup svojim bitcoinima.


Preporučuje se odabrati 8-cifreni PIN kod, što je moguće nasumičniji. Takođe, obavezno sačuvajte ovaj kod na drugom mestu od onog gde je vaš Ledger Flex uskladišten (na primer, u menadžeru lozinki).


![LEDGER FLEX](assets/notext/11.webp)


Unesite svoj PIN drugi put da ga potvrdite.


![LEDGER FLEX](assets/notext/12.webp)


Zatim će vam biti ponuđeno da izaberete između oporavka postojećeg Wallet ili kreiranja novog. U ovom uputstvu pokrivamo kreiranje novog Wallet od nule, pa izaberite opciju "*Postavi kao novi Ledger*" da generate novu Mnemonic frazu.


![LEDGER FLEX](assets/notext/13.webp)


Vaš Flex će pružiti uputstva o tome kako upravljati vašom frazom za oporavak.


**Ova Mnemonic fraza omogućava potpun i neograničen pristup svim vašim bitcoinima**. Svako ko poseduje ovu frazu može ukrasti vaša sredstva, čak i bez fizičkog pristupa vašem Ledger. Fraza od 24 reči omogućava vraćanje pristupa vašim bitcoinima u slučaju gubitka, krađe ili oštećenja vašeg Ledger Flex. Stoga je veoma važno pažljivo sačuvati i skladištiti je na sigurnom mestu.


Možete to zapisati na kartonski papir koji ste dobili uz vaš Ledger, ili za dodatnu sigurnost, preporučujem graviranje na medijum od nerđajućeg čelika kako biste se zaštitili od rizika požara, poplava ili urušavanja.


Možete pregledati ova uputstva i preskakati stranice dodirom ekrana.


![LEDGER FLEX](assets/notext/14.webp)

Ledger će kreirati vašu Mnemonic frazu koristeći svoj generator slučajnih brojeva. Uverite se da niste posmatrani tokom ove operacije. Zapišite reči koje obezbeđuje Ledger na fizički medijum po vašem izboru. U zavisnosti od vaše bezbednosne strategije, možete razmotriti pravljenje nekoliko potpunih fizičkih kopija fraze (ali najvažnije, nemojte je deliti). Važno je da reči budu numerisane i u sekvencijalnom redosledu.

***Očigledno, nikada ne biste trebali deliti ove reči na internetu, suprotno onome što radim u ovom vodiču. Ovaj primer Wallet će biti korišćen samo na Testnet i biće obrisan na kraju vodiča.***


![LEDGER FLEX](assets/notext/15.webp)


Da biste prešli na sledeću grupu reči, kliknite na dugme "*Next*". Kada su sve reči zabeležene, kliknite na dugme "*Done*" da biste prešli na sledeći korak.


![LEDGER FLEX](assets/notext/16.webp)


Kliknite na dugme "*Start confirmation*", zatim izaberite reči iz vaše Mnemonic fraze redosledom kojim se pojavljuju da biste potvrdili da ste ih ispravno zabeležili. Nastavite ovaj postupak do 24. reči.


![LEDGER FLEX](assets/notext/17.webp)


Ako se fraza koju potvrđujete tačno poklapa sa onom koju vam je Flex pružio u prethodnom koraku, možete nastaviti. Ako ne, to ukazuje da je vaša fizička kopija Mnemonic fraze netačna i potrebno je da ponovo pokrenete proces.


![LEDGER FLEX](assets/notext/18.webp)


I tu ga imate, vaš seed je ispravno kreiran na vašem Ledger Flex. Pre nego što nastavite sa kreiranjem novog Bitcoin Wallet iz ovog seed, hajde da zajedno istražimo postavke uređaja.


## Kako izmeniti postavke vašeg Ledger?


Da biste zaključali i otključali svoj Ledger, pritisnite bočno dugme. Zatim će vam biti zatraženo da unesete PIN kod koji ste postavili u prethodnom koraku.


![LEDGER FLEX](assets/notext/19.webp)


Da biste pristupili podešavanjima, kliknite na simbol zupčanika u donjem levom uglu vašeg uređaja.


![LEDGER FLEX](assets/notext/20.webp)


Meni "*Name*" omogućava vam da promenite ime vašeg Ledger.


![LEDGER FLEX](assets/notext/21.webp)


U "*About this Ledger*", pronaći ćete informacije o vašem Flex-u.


![LEDGER FLEX](assets/notext/22.webp)


U meniju "*Zaključani ekran*", imate opciju da promenite sliku prikazanu na zaključanom ekranu izborom "*Prilagodi sliku zaključanog ekrana*". Zahvaljujući E Ink tehnologiji ekrana uređaja, moguće je držati ekran stalno uključenim bez trošenja baterije. E Ink ekrani ne koriste energiju za održavanje statične slike. Međutim, troše energiju tokom promena prikaza.

Podmeni "*Auto-lock*" omogućava vam da konfigurišete i aktivirate automatsko zaključavanje vašeg Ledger nakon određenog perioda neaktivnosti.

![LEDGER FLEX](assets/notext/23.webp)


Meni "*Sounds*" omogućava vam da uključite ili isključite zvukove vašeg Flex uređaja. A u meniju "Language" možete promeniti jezik prikaza.


![LEDGER FLEX](assets/notext/24.webp)


Klikom na desnu strelicu, možete pristupiti drugim postavkama. "*Promeni PIN*" vam omogućava da promenite svoj PIN kod.


![LEDGER FLEX](assets/notext/25.webp)


Meniji "*Bluetooth*" i "*NFC*" omogućavaju vam upravljanje ovim komunikacijama.


![LEDGER FLEX](assets/notext/26.webp)


U "*Battery*" možete posebno postaviti automatsko isključivanje Ledger.


![LEDGER FLEX](assets/notext/27.webp)


Sekcija "*Advanced*" vam omogućava pristup naprednijim sigurnosnim postavkama. Preporučuje se da opcija "*PIN shuffle*" bude aktivirana radi poboljšanja sigurnosti. Takođe, u ovom meniju možete konfigurisati BIP39 passphrase.


![LEDGER FLEX](assets/notext/28.webp)


passphrase je opcionalna lozinka koja, u kombinaciji sa frazom za oporavak, pruža dodatni Layer sigurnosti za vaš Wallet.


Trenutno, vaš Wallet je generisan iz Mnemonic fraze koja se sastoji od 24 reči. Ova fraza za oporavak je veoma važna, jer vam omogućava da povratite sve ključeve vašeg Wallet u slučaju gubitka. Međutim, ona predstavlja jedinstvenu tačku otkaza (SPOF). Ako je kompromitovana, bitkoini su u opasnosti. Tu dolazi passphrase. To je opcionalna lozinka, koju možete proizvoljno izabrati, koja se dodaje Mnemonic frazi kako bi se ojačala sigurnost Wallet.


passphrase ne treba mešati sa PIN kodom. Ima ulogu u derivaciji vaših kriptografskih ključeva. Radi u tandemu sa frazom Mnemonic, modifikujući seed iz koje se generišu ključevi. Dakle, čak i ako neko dobije vašu frazu od 24 reči, bez passphrase ne može pristupiti vašim sredstvima. Korišćenje passphrase u suštini stvara novi Wallet sa različitim ključevima. Modifikovanje (čak i minimalno) passphrase će generate drugačiji Wallet.


passphrase je veoma moćan alat za poboljšanje sigurnosti vaših bitkoina. Međutim, veoma je važno razumeti kako funkcioniše pre nego što ga implementirate, kako biste izbegli gubitak pristupa vašem Wallet. Objasniću kako koristiti passphrase u drugom posvećenom vodiču.


![LEDGER FLEX](assets/notext/29.webp)


passphrase je veoma moćan alat za jačanje sigurnosti vaših bitkoina. Međutim, ključno je razumeti kako funkcioniše pre nego što ga implementirate, kako biste izbegli gubitak pristupa vašem Wallet. Zato sve objašnjavam u posvećenom vodiču:


https://planb.network/tutorials/wallet/backup/passphrase-ledger-9ae6d9a2-7293-438a-8fe0-e59147ef2f49

Na kraju, poslednja stranica sa podešavanjima omogućava vam da resetujete vaš Ledger. Nastavite sa ovim resetovanjem samo ako ste sigurni da ne sadrži ključeve koji obezbeđuju bitkoine, jer biste mogli trajno izgubiti pristup vašim sredstvima.

![LEDGER FLEX](assets/notext/30.webp)


## Kako instalirati aplikaciju Bitcoin?


Pokrenite Ledger Live softver na vašem računaru, zatim povežite i otključajte vaš Ledger Flex.


![LEDGER FLEX](assets/notext/31.webp)


U Ledger Live, idite na meni "*My Ledger*". Bićete zamoljeni da autorizujete pristup vašem Flex-u.


![LEDGER FLEX](assets/notext/32.webp)


Potvrdite pristup na vašem Ledger klikom na dugme "*Dozvoli*".


![LEDGER FLEX](assets/notext/33.webp)


Prvo, ako firmver vašeg Ledger Flex nije ažuriran, Ledger Live će automatski ponuditi da ga ažurira. Ako je primenljivo, kliknite na "*Update firmware*", zatim na "*Install update*" da biste započeli instalaciju.


![LEDGER FLEX](assets/notext/34.webp)


Na vašem Ledger, kliknite na dugme "*Install*", zatim sačekajte tokom instalacije.


![LEDGER FLEX](assets/notext/35.webp)


Firmware vašeg Ledger Flex je sada ažuriran.


![LEDGER FLEX](assets/notext/36.webp)


Ako želite, možete promeniti pozadinu zaključanog ekrana na vašem Ledger Flex. Da biste to uradili, kliknite na "*Add >*".


![LEDGER FLEX](assets/notext/37.webp)


Kliknite na dugme "*Otpremi sa računara*" i izaberite svoju pozadinu iz svojih fotografija.


![LEDGER FLEX](assets/notext/38.webp)


Možete obrezati svoju sliku.


![LEDGER FLEX](assets/notext/39.webp)


Izaberite kontrast iz različitih opcija, zatim kliknite na "*Potvrdi kontrast*".


![LEDGER FLEX](assets/notext/40.webp)


Na vašem Flex-u, kliknite na dugme "*Load picture*".


![LEDGER FLEX](assets/notext/41.webp)


Ako ste zadovoljni slikom, kliknite na "*Zadrži*" da biste je postavili kao pozadinu zaključanog ekrana.


![LEDGER FLEX](assets/notext/42.webp)


Konačno, dodaćemo aplikaciju Bitcoin. Da biste to uradili, na Ledger Live, kliknite na dugme "*Install*" pored "*Bitcoin (BTC)*".


![LEDGER FLEX](assets/notext/43.webp)


Aplikacija će se instalirati na vaš Flex.


![LEDGER FLEX](assets/notext/44.webp)


Od sada vam više neće biti potreban Ledger Live softver za redovno upravljanje vašim Wallet. Možete mu se povremeno vratiti kako biste ažurirali firmware kada nove verzije budu dostupne. Za sve ostalo, koristićemo Sparrow Wallet, koji je mnogo sveobuhvatniji alat za efikasno upravljanje Bitcoin Wallet.


## Kako postaviti novi Bitcoin Wallet sa Sparrow?

Otvorite Sparrow Wallet i preskočite uvodne stranice da biste pristupili početnom ekranu. Proverite da li ste pravilno povezani na čvor posmatrajući prekidač smešten u donjem desnom uglu ekrana.

![LEDGER FLEX](assets/notext/45.webp)


Preporučujem da koristite sopstveni Bitcoin čvor. U ovom uputstvu koristim javni čvor (žuti) jer sam na Testnet, ali za normalnu upotrebu, bolje je odabrati lokalni Bitcoin Core (Green) ili Electrum server povezan sa udaljenim čvorom (plavi).


Kliknite na meni "*File*" zatim "*New Wallet*".


![LEDGER FLEX](assets/notext/46.webp)


Izaberite ime za ovaj Wallet, zatim kliknite na "*Create Wallet*".


![LEDGER FLEX](assets/notext/47.webp)


U padajućem meniju "*Script Type*", izaberite tip skripta koji će se koristiti za obezbeđivanje vaših bitkoina. Preporučujem da odaberete "*Taproot*", ili ako nije dostupan, "*Native SegWit*".


![LEDGER FLEX](assets/notext/48.webp)


Kliknite na dugme "*Connected Hardware Wallet*".


![LEDGER FLEX](assets/notext/49.webp)


Povežite svoj Ledger Flex sa računarom, otključajte ga pomoću PIN koda, a zatim otvorite aplikaciju "*Bitcoin*". U ovom uputstvu koristim aplikaciju "*Bitcoin Testnet*", ali postupak ostaje isti za Mainnet.


![LEDGER FLEX](assets/notext/50.webp)


Na Sparrow-u, kliknite na dugme "*Scan*".


![LEDGER FLEX](assets/notext/51.webp)


Zatim kliknite na "*Importuj Keystore*".


![LEDGER FLEX](assets/notext/52.webp)


Sada možete videti detalje vašeg Wallet, uključujući prošireni javni ključ vašeg prvog naloga. Kliknite na dugme "*Apply*" da biste završili kreiranje Wallet.


![LEDGER FLEX](assets/notext/53.webp)


Izaberite jaku lozinku za zaštitu pristupa Sparrow Wallet. Ova lozinka će osigurati sigurnost pristupa vašim Wallet podacima na Sparrow-u, što pomaže u zaštiti vaših javnih ključeva, adresa, oznaka i istorije transakcija od bilo kakvog neovlašćenog pristupa.


Savetujem vam da sačuvate ovu lozinku u menadžeru lozinki kako je ne biste zaboravili.


![LEDGER FLEX](assets/notext/54.webp)


I eto ga, vaš Wallet je sada kreiran!


![LEDGER FLEX](assets/notext/55.webp)

Pre nego što primite svoje prve bitkoine u vaš Wallet, toplo vam savetujem da izvedete probni test oporavka. Zapišite referentni podatak, kao što je vaš xpub, zatim resetujte vaš Ledger Flex dok je Wallet još uvek prazan. Nakon toga, pokušajte da obnovite vaš Wallet na Ledger koristeći vaše papirne rezervne kopije. Proverite da li se xpub generisan nakon obnove poklapa sa onim koji ste prvobitno zabeležili. Ako je to slučaj, možete biti sigurni da su vaše papirne rezervne kopije pouzdane.


## Kako primiti bitkoine sa Ledger Flex?


Kliknite na karticu "*Receive*".


![LEDGER FLEX](assets/notext/56.webp)


Povežite svoj Ledger Flex sa računarom, otključajte ga pomoću PIN koda, a zatim otvorite aplikaciju "*Bitcoin*".


![LEDGER FLEX](assets/notext/57.webp)


Pre nego što upotrebite Address koji obezbeđuje Sparrow Wallet, proverite ga na ekranu vašeg Ledger Flex. Ova praksa vam omogućava da potvrdite da Address prikazan na Sparrow nije lažan i da Ledger zaista poseduje privatni ključ neophodan za kasnije trošenje bitkoina osiguranih ovim Address.


Da biste izvršili ovu verifikaciju, kliknite na dugme "*Display Address*".


![LEDGER FLEX](assets/notext/58.webp)


Osigurajte da Address prikazan na vašem Ledger Flex odgovara onom naznačenom na Sparrow Wallet. Takođe se preporučuje da ovu proveru izvršite neposredno pre nego što predate vaš Address pošiljaocu, kako biste bili sigurni u njegovu validnost.


![LEDGER FLEX](assets/notext/59.webp)


Možete dodati "*Label*" da opišete izvor bitkoina koji će biti osigurani ovim Address. Ovo je dobra praksa koja vam pomaže da bolje upravljate vašim UTXO-ima.


![LEDGER FLEX](assets/notext/60.webp)


Za više informacija o označavanju, takođe vam savetujem da pogledate ovaj drugi vodič:


https://planb.network/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

Zatim možete koristiti ovaj Address za primanje bitkoina.


![LEDGER FLEX](assets/notext/61.webp)


## Kako poslati bitkoine pomoću Ledger Flex?


Sada kada ste primili svoj prvi Sats u vašem Wallet osiguranom sa Flex, možete ih i potrošiti! Povežite vaš Ledger sa računarom, otključajte ga, pokrenite Sparrow Wallet, zatim idite na karticu "*Send*" da konstruirate novu transakciju.


![LEDGER FLEX](assets/notext/62.webp)


Ako želite da uradite "*kontrolu novčića*", to jest, da specifično izaberete koje UTXO-e želite da potrošite u transakciji, idite na karticu "*UTXOs*". Izaberite UTXO-e koje želite da potrošite, zatim kliknite na "*Pošalji izabrano*". Bićete preusmereni na isti ekran kartice "*Pošalji*", ali sa vašim UTXO-ima već izabranim za transakciju.

![LEDGER FLEX](assets/notext/63.webp)

Unesite odredište Address. Takođe možete uneti više adresa klikom na dugme "*+ Add*".


![LEDGER FLEX](assets/notext/64.webp)


Zabeleži "*Label*" da zapamtiš svrhu ovog troška.


![LEDGER FLEX](assets/notext/65.webp)


Izaberite iznos poslat na ovaj Address.


![LEDGER FLEX](assets/notext/66.webp)


Prilagodite stopu naknade vaše transakcije prema trenutnom tržištu.


![LEDGER FLEX](assets/notext/67.webp)


Proverite da su sva podešavanja vaše transakcije ispravna, zatim kliknite na "*Create Transaction*".


![LEDGER FLEX](assets/notext/68.webp)


Ako vam sve odgovara, kliknite na "*Finalize Transaction for Signing*".


![LEDGER FLEX](assets/notext/69.webp)


Kliknite na "*Sign*".


![LEDGER FLEX](assets/notext/70.webp)


Kliknite na "*Sign*" pored vašeg Ledger Flex.


![LEDGER FLEX](assets/notext/71.webp)


Proverite postavke transakcije na ekranu vašeg Flex-a, uključujući prijemnikov prijem Address, poslati iznos i iznos naknade.


![LEDGER FLEX](assets/notext/72.webp)


Da biste potpisali, držite prst na dugmetu "*Hold to sign*".


![LEDGER FLEX](assets/notext/73.webp)


Vaša transakcija je sada potpisana. Kliknite na "*Broadcast Transaction*" da biste je emitovali na Bitcoin mreži.


![LEDGER FLEX](assets/notext/74.webp)


Možete ga pronaći na kartici "*Transakcije*" u Sparrow Wallet.


![LEDGER FLEX](assets/notext/75.webp)


Čestitamo, sada ste upoznati sa osnovnom upotrebom Ledger Flex sa Sparrow Wallet! U budućem vodiču ćemo videti kako koristiti Ledger Flex sa Liana za korišćenje Miniscripta.


Ako ste smatrali ovaj vodič korisnim, bio bih zahvalan na podignutom palcu ispod. Slobodno podelite ovaj članak na svojim društvenim mrežama. Hvala vam puno!