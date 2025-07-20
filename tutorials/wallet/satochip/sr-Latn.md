---
name: Satochip
description: Postavljanje i korišćenje Satochip pametne kartice
---
![cover](assets/cover.webp)


Hardware Wallet je elektronski uređaj posvećen upravljanju i zaštiti privatnih ključeva Bitcoin Wallet. Za razliku od softverskih novčanika (ili Hot novčanika) instaliranih na mašinama opšte namene koje su često povezane na Internet, hardverski novčanici omogućavaju fizičku izolaciju privatnih ključeva, smanjujući rizike od hakovanja i krađe.


Glavni cilj Hardware Wallet je minimizirati funkcionalnosti uređaja kako bi se smanjila njegova površina napada. Manja površina napada takođe znači manje potencijalnih vektora napada, tj. manje slabosti u sistemu koje napadači mogu iskoristiti za pristup bitcoinima.


Preporučuje se korišćenje Hardware Wallet za osiguranje vaših bitkoina, posebno ako posedujete značajne iznose, bilo u apsolutnoj vrednosti ili kao proporciju vaših ukupnih sredstava.


Hardverski novčanici se koriste u kombinaciji sa Wallet softverom za upravljanje na računaru ili pametnom telefonu. Ovaj softver upravlja kreiranjem transakcija, ali kriptografski potpis neophodan za validaciju ovih transakcija se vrši isključivo unutar Hardware Wallet. To znači da privatni ključevi nikada nisu izloženi potencijalno ranjivom okruženju.


Hardverski novčanici nude dvostruku zaštitu za korisnika: s jedne strane, štite vaše bitkoine od daljinskih napada držeći privatne ključeve van mreže, a s druge strane, obično nude bolju fizičku otpornost protiv pokušaja ekstrakcije ključeva. I upravo na osnovu ova 2 sigurnosna kriterijuma može se oceniti i rangirati različiti modeli dostupni na tržištu.


U ovom vodiču predlažem da otkrijemo jedno od ovih rešenja: Satochip.


## Uvod u Satochip


Satochip je Hardware Wallet u obliku kartice sa čipom sertifikovanim na *EAL6+*, što predstavlja veoma visok sigurnosni standard (*NXP JCOP*). Proizvodi ga belgijska kompanija.


![SATOCHIP](assets/notext/01.webp)


Ova pametna kartica se prodaje za €25, što je vrlo pristupačno u poređenju sa drugim hardverskim novčanicima na tržištu. Čip je sigurnosni element koji osigurava vrlo dobru otpornost protiv fizičkih napada. Štaviše, njen kod je otvorenog tipa (*AGPLv3*).

Međutim, zbog svog formata, Satochip ne nudi toliko opcija kao drugi hardver. Očigledno nema bateriju, kameru, niti čitač micro SD kartica, jer je to kartica. Njegov najveći nedostatak, po mom mišljenju, je nedostatak ekrana na Hardware Wallet, što ga čini ranjivijim na određene vrste daljinskih napada. Zaista, ovo prisiljava korisnika da potpisuje naslepo i da veruje onome što vidi na ekranu svog računara.


Uprkos svojim ograničenjima, Satochip ostaje zanimljiv zbog svoje smanjene cene. Ovaj Wallet se može koristiti za poboljšanje sigurnosti potrošnje Wallet, pored štednog Wallet zaštićenog Hardware Wallet opremljenim ekranom. Takođe predstavlja dobro rešenje za one koji drže male količine bitkoina i ne žele da ulože stotinu evra u sofisticiraniji uređaj. Štaviše, upotreba Satochipova u Multisig konfiguracijama, ili potencijalno u Wallet sistemima sa vremenskim zaključavanjem u budućnosti, može ponuditi zanimljive prednosti.


Kompanija Satochip takođe nudi 2 druga proizvoda. Tu je Satodime, koji je kartica na donosioca dizajnirana za offline čuvanje bitcoina, ali ne omogućava transakcije. To je neka vrsta papirnog Wallet koji je mnogo sigurniji, a može se koristiti, na primer, za poklon. Na kraju, tu je Seedkeeper, koji je menadžer fraza Mnemonic. Može se koristiti za sigurno čuvanje našeg seed bez da je direktno zabeležen na papiru.


## Kako kupiti Satochip?


Satochip je dostupan za prodaju [na zvaničnom sajtu](https://satochip.io/product/satochip/). Da biste ga kupili u fizičkoj prodavnici, možete pronaći [listu sertifikovanih prodavaca](https://satochip.io/resellers/) na Satochip sajtu.


Da biste komunicirali sa vašim Wallet softverom za upravljanje, Satochip nudi dve mogućnosti: putem NFC komunikacije ili preko čitača pametnih kartica. Za NFC opciju, uverite se da je vaš uređaj kompatibilan sa ovom tehnologijom ili nabavite eksterni NFC čitač. Satochip radi na standardnoj frekvenciji od 13.56 MHz. U suprotnom, možete kupiti i čitač pametnih kartica. Možete ga pronaći na Satochip vebsajtu ili na drugom mestu.


![SATOCHIP](assets/notext/02.webp)


## Kako postaviti Satochip sa Sparrow?


Kada primite svoj Satochip, prvi korak je da pregledate pakovanje kako biste se uverili da nije otvoreno. Pakovanje Satochipa treba da sadrži nalepnicu za zaptivanje. Ako ova nalepnica nedostaje ili je oštećena, to može ukazivati na to da je pametna kartica kompromitovana i možda nije autentična.

![SATOCHIP](assets/notext/03.webp)

Unutra ćete pronaći Satochip.


![SATOCHIP](assets/notext/04.webp)


Da biste upravljali Wallet, u ovom vodiču predlažem korišćenje Sparrow-a. Ako još nemate softver, [posetite zvaničnu veb stranicu da ga preuzmete](https://sparrowwallet.com/download/). Takođe možete pogledati naš vodič o Sparrow Wallet (uskoro dolazi).


![SATOCHIP](assets/notext/05.webp)


Umetnite svoj Satochip u čitač pametnih kartica ili ga postavite na NFC čitač, i povežite čitač sa računarom na kojem je otvoren Sparrow.


![SATOCHIP](assets/notext/06.webp)


Otvorite Sparrow Wallet i uverite se da ste pravilno povezani na Bitcoin čvor. Da biste to uradili, proverite oznaku u donjem desnom uglu: trebalo bi da bude žuta ako ste povezani na javni čvor, Green za vezu sa Bitcoin Core, ili plava za Electrum.


![SATOCHIP](assets/notext/07.webp)


Na Sparrow Wallet, kliknite na karticu "*File*".


![SATOCHIP](assets/notext/08.webp)


Zatim na meniju "*New Wallet*".


![SATOCHIP](assets/notext/09.webp)


Izaberite ime za vaš Wallet, a zatim kliknite na "*Create Wallet*".


![SATOCHIP](assets/notext/10.webp)


Kliknite na dugme "*Connected Hardware Wallet*".


![SATOCHIP](assets/notext/11.webp)


Kliknite na dugme "*Skeniraj...*".


![SATOCHIP](assets/notext/12.webp)


Vaš Satochip bi trebalo da se pojavi. Kliknite na "*Import Keystore*".


![SATOCHIP](assets/notext/13.webp)


Zatim, treba da postavite PIN kod za otključavanje vašeg Satochip-a. Izaberite jaku lozinku, između 4 i 16 karaktera. Napravite rezervnu kopiju ove lozinke.


Imajte na umu, ova lozinka nije passphrase. To znači da čak i bez ove lozinke, vaša Mnemonic fraza će vam omogućiti da ponovo uvezete vaš Wallet u softver ako je potrebno. Lozinka se koristi samo za osiguranje pristupa samom Satochip-u. Ona je ekvivalentna PIN kodu koji se nalazi na drugim hardverskim novčanicima.


Kada unesete lozinku, ponovo kliknite na dugme "*Import Keystore*".


![SATOCHIP](assets/notext/14.webp)


Zapišite lozinku ponovo, zatim kliknite na dugme "*Initialize*".


![SATOCHIP](assets/notext/15.webp)


Zatim stižete na prozor za generisanje vaše Mnemonic fraze. Kliknite na dugme "*generate New*".


![SATOCHIP](assets/notext/16.webp)

Napravite jednu ili više fizičkih kopija vaše fraze za oporavak tako što ćete je zapisati na papir ili metalni medijum. Budite svesni da ova fraza omogućava potpuni pristup vašim bitcoinima bez dodatne zaštite. Dakle, ako je neko otkrije, mogao bi odmah ukrasti vaše bitcoine, čak i bez pristupa vašem Satochip-u ili njegovom PIN kodu. Stoga je važno osigurati ove rezervne kopije. Štaviše, ova fraza vam omogućava da ponovo dobijete pristup vašim bitcoinima u slučaju gubitka, oštećenja Satochip-a ili ako zaboravite svoj PIN kod.

![SATOCHIP](assets/notext/17.webp)


Vaš Bitcoin Wallet je uspešno kreiran.


![SATOCHIP](assets/notext/18.webp)


Ponovo kliknite na dugme "*Import Keystore*".


![SATOCHIP](assets/notext/19.webp)


Vaš Wallet je sada kreiran. Vaši privatni ključevi su sada pohranjeni na pametnoj kartici vašeg Satochip-a. Kliknite na dugme "*Apply*" da nastavite.


![SATOCHIP](assets/notext/20.webp)


Preporučuje se postavljanje dodatne lozinke za zaštitu javnih informacija kojima upravlja Sparrow Wallet, pored PIN koda vašeg Satochip-a. Ova lozinka će osigurati bezbednost pristupa Sparrow Wallet, što pomaže u zaštiti vaših javnih ključeva, adresa i istorije transakcija od bilo kakvog neovlašćenog pristupa.


![SATOCHIP](assets/notext/21.webp)


Unesite svoju lozinku u dva polja, zatim kliknite na dugme "*Set Password*".


![SATOCHIP](assets/notext/22.webp)


I eto ga, vaš Satochip je sada konfigurisan na Sparrow Wallet.


![SATOCHIP](assets/notext/23.webp)


Sada kada je vaš Wallet kreiran, možete isključiti vaš Satochip. Čuvajte ga na sigurnom mestu!


## Kako primiti bitkoine sa Satochip-om?


Jednom kada ste u vašem Wallet, kliknite na karticu "*Receive*".


![SATOCHIP](assets/notext/24.webp)


Sparrow Wallet generiše Address za vaš Wallet. Obično, za druge hardverske novčanike, savetuje se da kliknete na "*Prikaži Address*" kako biste verifikovali Address direktno na ekranu uređaja. Nažalost, ova opcija nije dostupna sa Satochip-om, ali obavezno je koristite za vaše druge novčanike.


![SATOCHIP](assets/notext/25.webp)


Možete dodati "*Label*" da opišete izvor bitkoina koji će biti osiguran ovim Address. Ovo je dobra praksa koja vam pomaže da bolje upravljate vašim UTXO-ima.


![SATOCHIP](assets/notext/26.webp)


Za više informacija o označavanju, preporučujem da pogledate i ovaj drugi vodič:


https://planb.network/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

Zatim možete koristiti ovaj Address za primanje bitkoina.


![SATOCHIP](assets/notext/27.webp)

## Kako poslati bitkoine sa Satochip?

Sada kada ste primili svoj prvi Sats u vašem sigurnom Wallet sa Satochip-om, možete ih i potrošiti! Povežite vaš Satochip sa računarom, pokrenite Sparrow Wallet, a zatim idite na karticu "*Send*" da konstruirate novu transakciju.


![SATOCHIP](assets/notext/28.webp)


Ako želite da izvršite kontrolu novčića, tj. da specifično izaberete koje UTXO-e ćete koristiti u transakciji, idite na karticu "*UTXOs*". Izaberite UTXO-e koje želite da potrošite, zatim kliknite na "*Send Selected*". Bićete preusmereni na isti ekran kartice "*Send*", ali sa vašim već izabranim UTXO-ima za transakciju.


![SATOCHIP](assets/notext/29.webp)


Unesite odredište Address. Takođe možete uneti više adresa klikom na dugme "*+ Dodaj*".


![SATOCHIP](assets/notext/30.webp)


Zabeleži "*Label*" da zapamtiš svrhu ovog troška.


![SATOCHIP](assets/notext/31.webp)


Izaberite iznos poslat ovom Address.


![SATOCHIP](assets/notext/32.webp)


Prilagodite stopu naknade vaše transakcije prema trenutnom tržištu.


![SATOCHIP](assets/notext/33.webp)


Uverite se da su svi parametri vaše transakcije tačni, zatim kliknite na "*Create Transaction*".


![SATOCHIP](assets/notext/34.webp)


Ako je sve po vašem zadovoljstvu, kliknite na "*Finalize Transaction for Signing*".


![SATOCHIP](assets/notext/35.webp)


Kliknite na "*Sign*".


![SATOCHIP](assets/notext/36.webp)


Kliknite na "*Sign*" ponovo pored vašeg Satochip-a.


![SATOCHIP](assets/notext/37.webp)


Unesite PIN kod vašeg Satochip-a, zatim ponovo kliknite na "*Sign*" da biste potpisali vašu transakciju.


![SATOCHIP](assets/notext/38.webp)


Vaša transakcija je sada potpisana. Kliknite na "*Broadcast Transaction*" da biste je emitovali na Bitcoin mrežu.


![SATOCHIP](assets/notext/39.webp)


Možete ga pronaći u kartici "*Transactions*" na Sparrow Wallet.


![SATOCHIP](assets/notext/40.webp)


Čestitamo, sada ste upoznati sa korišćenjem Satochip-a! Ako vam je ovaj vodič bio od pomoći, bio bih zahvalan na palcu gore ispod. Slobodno podelite ovaj članak na vašim društvenim mrežama. Hvala vam puno!