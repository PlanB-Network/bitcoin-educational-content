---
name: Tapsigner
description: Postavljanje i korišćenje Tapsigner-a sa Nunchuk-om
---
![cover](assets/cover.webp)


Hardware Wallet je elektronski uređaj posvećen upravljanju i sigurnosti privatnih ključeva Bitcoin Wallet. Za razliku od softverskih novčanika (ili Hot novčanika) instaliranih na mašinama opšte namene koje su često povezane na Internet, hardverski novčanici omogućavaju fizičku izolaciju privatnih ključeva, smanjujući rizike od hakovanja i krađe.


Glavni cilj Hardware Wallet je minimizirati funkcionalnosti uređaja kako bi se smanjila njegova površina napada. Manja površina napada takođe znači manje potencijalnih vektora napada, tj. manje slabih tačaka u sistemu koje napadači mogu iskoristiti za pristup bitcoinima.


Preporučuje se korišćenje Hardware Wallet za osiguranje vaših bitkoina, posebno ako posedujete značajne iznose, bilo u apsolutnoj vrednosti ili kao proporciju vaših ukupnih sredstava.


Hardverski novčanici se koriste u kombinaciji sa Wallet softverom za upravljanje na računaru ili pametnom telefonu. Ovaj softver upravlja kreiranjem transakcija, ali kriptografski potpis neophodan za validaciju ovih transakcija se vrši isključivo unutar Hardware Wallet. To znači da privatni ključevi nikada nisu izloženi potencijalno ranjivom okruženju.


Hardverski novčanici nude dvostruku zaštitu za korisnika: s jedne strane, štite vaše bitkoine od daljinskih napada držeći privatne ključeve van mreže, a s druge strane, obično nude bolju fizičku otpornost protiv pokušaja ekstrakcije ključeva. I upravo na osnovu ova 2 sigurnosna kriterijuma može se suditi i rangirati različiti modeli dostupni na tržištu.


U ovom vodiču predlažem da otkrijemo jedno od ovih rešenja: Tapsigner od Coinkite.


## Uvod u Tapsigner


Tapsigner je Hardware Wallet dizajniran u obliku NFC kartice od strane kompanije Coinkite, koja je takođe poznata po proizvodnji Coldcards.


![TAPSIGNER NUNCHUK](assets/notext/01.webp)


Tapsigner omogućava skladištenje para koji se sastoji od master privatnog ključa i lanca koda u skladu sa BIP32, za izvođenje stabla kriptografskih ključeva. Ovi ključevi mogu se koristiti za potpisivanje transakcija postavljanjem Tapsignera uz telefon ili NFC čitač kartica.

Ova NFC kartica se prodaje za $19.99, što je veoma pristupačno u poređenju sa drugim hardverskim novčanicima dostupnim na tržištu. Međutim, zbog svog formata, Tapsigner ne nudi toliko opcija kao drugi uređaji. Očigledno je da nema bateriju, kameru, niti čitač micro SD kartica, jer je to kartica. Po mom mišljenju, njen najveći nedostatak je nedostatak ekrana na Hardware Wallet, što je čini podložnijom određenim vrstama daljinskih napada. Naime, ovo primorava korisnika da potpisuje naslepo i da veruje onome što vidi na ekranu svog računara.


Uprkos svojim ograničenjima, Tapsigner može biti zanimljiv zbog svoje smanjene cene. Ovaj Wallet se može posebno koristiti za poboljšanje sigurnosti potrošnje Wallet uz dodatak štednog Wallet zaštićenog Hardware Wallet opremljenim ekranom. Takođe predstavlja dobro rešenje za one koji drže male količine bitkoina i ne žele da ulože stotinu evra u sofisticiraniji uređaj. Štaviše, upotreba Tapsignera u Multisig konfiguracijama, ili potencijalno u Wallet sistemima sa vremenskim zaključavanjem u budućnosti, može ponuditi zanimljive prednosti.


## Kako kupiti Tapsigner?


Tapsigner je dostupan za kupovinu [na zvaničnom Coinkite sajtu](https://store.coinkite.com/store/category/tapsigner). Da biste ga kupili u fizičkoj prodavnici, možete pronaći [listu sertifikovanih prodavaca](https://coinkite.com/resellers) na sajtu.


Trebaće vam i telefon kompatibilan sa NFC komunikacijama, ili USB uređaj za čitanje NFC kartica na standardnoj frekvenciji od 13,56 MHz.


## Kako inicijalizovati Tapsigner sa Nunchuk?


Kada primite svoj Tapsigner, prvi korak je da pregledate pakovanje kako biste se uverili da nije otvoreno. Ako je paket oštećen, to može ukazivati na to da je kartica kompromitovana i možda nije autentična. CoinKite će isporučiti vaš Tapsigner sa futrolom koja blokira radio talase. Uverite se da je prisutna u vašem paketu.


![TAPSIGNER NUNCHUK](assets/notext/02.webp)


Da bismo upravljali Wallet, koristićemo mobilnu aplikaciju **Nunchuk Wallet**. Uverite se da vaš pametni telefon podržava NFC, zatim preuzmite Nunchuk sa [Google Play Store](https://play.google.com/store/apps/details?id=io.nunchuk.android), [App Store](https://apps.apple.com/us/app/nunchuk-Bitcoin-Wallet/id1563190073) ili direktno putem [`.apk` fajla](https://github.com/nunchuk-io/nunchuk-android/releases).


![TAPSIGNER NUNCHUK](assets/notext/03.webp)

Ako prvi put koristite Nunchuk, aplikacija će vas podstaći da kreirate nalog. Za potrebe ovog tutorijala, nije neophodno kreirati ga. Dakle, izaberite "*Nastavi kao gost*" da biste nastavili bez naloga.

![TAPSIGNER NUNCHUK](assets/notext/04.webp)


Zatim kliknite na "*Unassisted Wallet*".


![TAPSIGNER NUNCHUK](assets/notext/05.webp)


Zatim kliknite na dugme "*Istražiću sam*".


![TAPSIGNER NUNCHUK](assets/notext/06.webp)


Jednom u Nunchuk-u, kliknite na dugme "*+*" pored kartice "*Keys*".


![TAPSIGNER NUNCHUK](assets/notext/07.webp)


Izaberite "*Dodaj NFC ključ*".


![TAPSIGNER NUNCHUK](assets/notext/08.webp)


Zatim kliknite na "*Add TAPSIGNER*".


![TAPSIGNER NUNCHUK](assets/notext/09.webp)


Kliknite na "*Continue*" i zatim prislonite vašu Tapsigner NFC karticu uz vaš pametni telefon.


![TAPSIGNER NUNCHUK](assets/notext/10.webp)


Ako je vaš Tapsigner nov, Nunchuk će ponuditi da ga inicijalizuje. Kliknite na "*Da*".


![TAPSIGNER NUNCHUK](assets/notext/11.webp)


Sada ćete morati da izaberete kako da generate vaš glavni lančani kod.


Tapsigner koristi BIP32 standard. To znači da derivacija vaših kriptografskih ključeva koji osiguravaju vaše bitkoine ne oslanja se na Mnemonic frazu kao BIP39 novčanici, već direktno na master privatni ključ i master lančani kod. Ova 2 Elements prolaze kroz HMAC funkciju kako bi deterministički i hijerarhijski derivirali ostatak vaših Wallet.


Glavni privatni ključ generiše direktno TRNG (*True Random Number Generator*) integrisan u vaš Tapsigner. Glavni lančani kod, s druge strane, mora biti obezbeđen spolja. Na ovom koraku imate izbor: dozvolite Nunchuk generate da to uradi automatski klikom na "*Automatic*", ili generate to uradite sami odabirom "*Advanced*" i unosom u predviđeno polje.


![TAPSIGNER NUNCHUK](assets/notext/12.webp)


Zatim, treba da izaberete PIN kod. U oblasti "*Početni PIN*", unesite PIN kod napisan na poleđini vašeg Tapsigner-a.


![TAPSIGNER NUNCHUK](assets/notext/13.webp)


Izaberite PIN kod za zaštitu fizičkog pristupa vašem Tapsigner-u. Ovaj PIN kod nema ulogu u Wallet procesu oporavka. Njegova jedina funkcija je da otključa vaš Tapsigner za potpisivanje transakcija. Obavezno sačuvajte ovaj PIN kod kako ga ne biste zaboravili. Kliknite na "*Nastavi*" da biste nastavili.


![TAPSIGNER NUNCHUK](assets/notext/14.webp)

Postavite svoju Tapsigner karticu na zadnju stranu telefona sada da biste je inicijalizovali.

![TAPSIGNER NUNCHUK](assets/notext/15.webp)


Nunchuk će zatim generate fajl za oporavak za vaš Wallet, što vam omogućava da ponovo dobijete pristup svojim bitkoinima u slučaju da izgubite svoju NFC karticu. Ovaj fajl je šifrovan sa rezervnim kodom napisanim na poleđini vašeg Tapsignera. Da biste povratili svoje bitkoine, apsolutno će vam biti potreban ovaj fajl kao i kod za njegovo dešifrovanje. Stoga je važno napraviti papirnu kopiju ovog koda, jer ako izgubite svoju NFC karticu, pristup ovom kodu će takođe biti izgubljen, pošto je trenutno napisan samo na kartici. Obavezno napravite i nekoliko rezervnih kopija vašeg šifrovanog fajla za oporavak.


![TAPSIGNER NUNCHUK](assets/notext/16.webp)


Izaberite ime za vaš Wallet.


![TAPSIGNER NUNCHUK](assets/notext/17.webp)


Osnova vašeg Wallet je sada postavljena. Da biste proverili autentičnost vašeg Tapsigner-a, u bilo kom trenutku možete kliknuti na dugme "*Run health check*".


![TAPSIGNER NUNCHUK](assets/notext/18.webp)


Unesite svoj PIN.


![TAPSIGNER NUNCHUK](assets/notext/19.webp)


Zatim postavite svoju karticu na zadnju stranu telefona.


![TAPSIGNER NUNCHUK](assets/notext/20.webp)


## Kako kreirati Wallet na Tapsigneru?


Na početnoj stranici Nunchuk-a, možete videti da je vaš Tapsigner registrovan u dostupnim uređajima za potpisivanje.


![TAPSIGNER NUNCHUK](assets/notext/21.webp)


Sada ćete morati da generate ključeve za vaš Bitcoin Wallet. Da biste to uradili, kliknite na dugme "*+*" desno od kartice "*Wallets*".


![TAPSIGNER NUNCHUK](assets/notext/22.webp)


Kliknite na "*Create new Wallet*".


![TAPSIGNER NUNCHUK](assets/notext/23.webp)


Zatim izaberite opciju "*Kreiraj novi Wallet koristeći postojeće ključeve*".


![TAPSIGNER NUNCHUK](assets/notext/24.webp)


Izaberite ime za vaš Wallet i zatim kliknite na "*Nastavi*".


![TAPSIGNER NUNCHUK](assets/notext/25.webp)


Izaberite svoj Tapsigner kao uređaj za potpisivanje za ovaj novi skup ključeva, zatim kliknite na "*Nastavi*".


![TAPSIGNER NUNCHUK](assets/notext/26.webp)


Ako je sve po vašem zadovoljstvu, potvrdite kreiranje.


![TAPSIGNER NUNCHUK](assets/notext/27.webp)

Zatim možete sačuvati konfiguracionu datoteku vašeg Wallet. Ova datoteka sadrži isključivo vaše javne ključeve, što znači da čak i ako neko pristupi njoj, ne može ukrasti vaše bitkoine. Međutim, može pratiti sve vaše transakcije. Stoga, ova datoteka predstavlja rizik samo za vašu privatnost. U nekim slučajevima, može biti neophodna za oporavak vašeg Wallet.

![TAPSIGNER NUNCHUK](assets/notext/28.webp)


I eto ga, vaš Wallet je uspešno kreiran!


![TAPSIGNER NUNCHUK](assets/notext/29.webp)


Kada ne koristite svoj Tapsigner, zapamtite da ga čuvate u futroli koju je obezbedio Coinkite, koja blokira radio talase kako bi zaštitila od neovlašćenih očitavanja.


## Kako primiti bitkoine na Tapsigner?


Da biste primili bitkoine, kliknite na vaš Wallet.


![TAPSIGNER NUNCHUK](assets/notext/30.webp)


Zatim koristite generisani Address za primanje bitkoina. Ako ste prethodno primili bitkoine na ovom Wallet, potrebno je da kliknete na dugme "*Receive*" da generate napravite novi prazan prijemni Address.


![TAPSIGNER NUNCHUK](assets/notext/31.webp)


Jednom kada pošiljalac pošalje transakciju, videćete je na vašem Wallet.


![TAPSIGNER NUNCHUK](assets/notext/32.webp)


Kliknite na "*View coins*".


![TAPSIGNER NUNCHUK](assets/notext/33.webp)


Odaberite svoj novi UTXO.


![TAPSIGNER NUNCHUK](assets/notext/34.webp)


Kliknite na "*+*" pored "*Oznake*" da dodate oznaku vašem UTXO. Ovo je dobra praksa, jer vam pomaže da se setite porekla vaših novčića i optimizujete vašu privatnost za buduće trošenje.


![TAPSIGNER NUNCHUK](assets/notext/35.webp)


Odaberite postojeću oznaku ili kreirajte novu, zatim kliknite na "*Sačuvaj*". Takođe imate opciju da kreirate "*kolekcije*" kako biste organizovali svoje novčiće na strukturiraniji način.


![TAPSIGNER NUNCHUK](assets/notext/36.webp)


## Kako poslati bitkoine sa Tapsignerom?


Sada kada imate bitkoine u svom Wallet, možete ih i poslati. Da biste to uradili, kliknite na Wallet po vašem izboru.


![TAPSIGNER NUNCHUK](assets/notext/37.webp)


Kliknite na dugme "*Pošalji*".


![TAPSIGNER NUNCHUK](assets/notext/38.webp)


Izaberite iznos za slanje, zatim kliknite na "*Nastavi*".


![TAPSIGNER NUNCHUK](assets/notext/39.webp)


Dodajte "*napomena*" svojoj budućoj transakciji da biste se setili njene svrhe.


![TAPSIGNER NUNCHUK](assets/notext/40.webp)

Zatim ručno unesite Address primaoca u određeno polje.

![TAPSIGNER NUNCHUK](assets/notext/41.webp)


Takođe možete skenirati QR kod kodiran sa Address klikom na ikonu koja se nalazi u gornjem desnom uglu ekrana.


![TAPSIGNER NUNCHUK](assets/notext/42.webp)


Kliknite na dugme "*Create Transaction*".


![TAPSIGNER NUNCHUK](assets/notext/43.webp)


Proverite detalje vaše transakcije, zatim kliknite na dugme "*Sign*" pored vašeg Tapsigner-a.


![TAPSIGNER NUNCHUK](assets/notext/44.webp)


Unesite svoj PIN da ga otključate.


![TAPSIGNER NUNCHUK](assets/notext/45.webp)


Zatim postavite Tapsigner na zadnju stranu vašeg pametnog telefona.


![TAPSIGNER NUNCHUK](assets/notext/46.webp)


Vaša transakcija je sada potpisana. Proverite još jednom da je sve ispravno, zatim kliknite na "*Broadcast Transaction*" da biste je emitovali na Bitcoin mreži.


![TAPSIGNER NUNCHUK](assets/notext/47.webp)


Vaša transakcija sada čeka potvrdu.


![TAPSIGNER NUNCHUK](assets/notext/48.webp)


## Kako povratiti Wallet u slučaju gubitka Tapsignera?


Ako ste izgubili svoj Tapsigner, možete povratiti svoj Wallet koristeći kod zabeležen na poleđini kartice. Stoga je važno sačuvati ovaj kod odvojeno od Tapsignera, jer ako se kartica izgubi, pristup ovom kodu će takođe biti izgubljen. Takođe će vam biti potreban šifrovani bekap Wallet.


Za oporavak ćemo koristiti aplikaciju Nunchuk, ali imajte na umu da to znači privremeno osiguranje vaših sredstava u Hot Wallet. Ako je vaš Tapsigner osiguravao značajne iznose, razmislite o praćenju istog procesa oporavka sa novim Coldcard-om umesto toga.


Otvorite aplikaciju Nunchuk i kliknite na dugme "*+*" pored kartice "*Keys*".


![TAPSIGNER NUNCHUK](assets/notext/49.webp)


Izaberite "*Dodaj NFC ključ*".


![TAPSIGNER NUNCHUK](assets/notext/50.webp)


Izaberite opciju "*Recover TAPSIGNER key from backup*".


![TAPSIGNER NUNCHUK](assets/notext/51.webp)


Zatim ćete biti preusmereni na istraživač datoteka vašeg uređaja. Pronađite i izaberite šifrovanu rezervnu datoteku vašeg Wallet. Obično ime ove datoteke počinje sa `backup...`.


![TAPSIGNER NUNCHUK](assets/notext/52.webp)


Unesite lozinku koja dešifruje rezervnu datoteku. Ova lozinka odgovara onoj koja je prvobitno zabeležena na poleđini vašeg Tapsignera.


![TAPSIGNER NUNCHUK](assets/notext/53.webp)

Zatim izaberite ime za vaš oporavak Wallet.

![TAPSIGNER NUNCHUK](assets/notext/54.webp)


Sada ste ponovo dobili pristup svojim bitcoinima. Vaš Wallet je sada upravljan kao Hot Wallet vidljiv u kartici "*Keys*" u aplikaciji Nunchuk. Zatim, treba da kreirate novi set kriptografskih ključeva u odeljku "*Wallets*" tako što ćete povezati ovaj ključ sa njim. Da biste to uradili, možete ponovo pratiti korake u delu "*How to create a Wallet on a Tapsigner?*" ovog tutorijala.


![TAPSIGNER NUNCHUK](assets/notext/55.webp)


Ako ste izgubili svoj Tapsigner, toplo vam savetujem da odmah prebacite svoje bitkoine na drugi Wallet koji posedujete, idealno zaštićen Hardware Wallet. Naime, Tapsigner koji ste izgubili mogao bi potencijalno biti u pogrešnim rukama. Stoga je važno isprazniti Wallet koji ste upravo povratili i prestati ga koristiti.


Čestitamo, sada ste u toku sa korišćenjem Tapsignera! Ako vam je ovaj vodič bio od pomoći, bio bih zahvalan ako biste mogli ostaviti palac gore ispod. Slobodno podelite ovaj članak na svojim društvenim mrežama. Hvala vam puno!