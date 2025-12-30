---
name: PearPass
description: Povratite kontrolu nad svojim lozinkama uz lokalni, peer-to-peer, cloud-free menadžer lozinki
---

![cover](assets/cover.webp)



U vreme kada svaki pojedinac upravlja desetinama, čak i stotinama online naloga, bezbednost prijavljivanja postala je centralno pitanje u IT bezbednosti. Društvene mreže, sistemi za razmenu poruka, profesionalne usluge, finansijske platforme: svaki od ovih pristupa oslanja se na tajnu, čiji kompromis može imati ozbiljne posledice po vaš život.



Ipak, uprkos porastu broja napada, loše prakse i dalje su široko rasprostranjene među stanovništvom: slabe lozinke, ponovo korišćene lozinke, lozinke sačuvane u čistom tekstu ili zapamćene približno. Da bi se ovi problemi rešili bez komplikovanja svakodnevnog života, rešenje je korišćenje menadžera lozinki.



Već postoji na desetine menadžera lozinki, a Plan ₿ Academy nudi tutorijal za većinu njih. Ali u ovom tutorijalu, želeo bih da vas upoznam sa jednim koji se jasno izdvaja od ostalih po načinu na koji funkcioniše: **PearPass**.



**PearPass je peer-to-peer menadžer lozinki, local-first i otvorenog koda, osmišljen da korisniku vrati potpunu kontrolu nad njegovim podacima.**



![Image](assets/fr/01.webp)



## Zašto izabrati PearPass?



Menadžer lozinki je softverski program koji generiše, čuva i organizuje sve vaše lozinke na siguran način. Umesto da pamtite ili ponovo koristite lozinke, imate samo jednu tajnu koju treba zaštititi: glavnu lozinku, koja šifruje vaš čitav sef. Ovaj pristup omogućava korišćenje jedinstvenih, dugih, nasumičnih lozinki za svaku uslugu, smanjujući rizik od zaboravljanja i kompromitovanja, dok ograničava uticaj bilo kakvog mogućeg curenja. Danas je to osnovni IT alat koji bi svi trebalo da koriste.



Postoje dve glavne kategorije menadžera lozinki. S jedne strane, tu je softver koji radi isključivo lokalno, što je veoma sigurno jer se podaci nikada ne čuvaju na centralnom serveru, ali nije baš praktično, jer ne omogućava lako sinhronizovanje vaših kredencijala između više uređaja (računar, pametni telefon, tablet...). S druge strane, menadžeri lozinki zasnovani na oblaku čuvaju vaše kredencijale na svojim serverima i sinhronizuju ih na svim vašim uređajima. Njihova glavna prednost je praktičnost, ali uključuju kompromis po pitanju sigurnosti, jer su vaše lozinke pohranjene na infrastrukturama nad kojima nemate kontrolu.



PearPass namerno prekida sa oba modela. Pozicionira se između lokalnih menadžera i cloud rešenja: omogućava sinhronizaciju vaših lozinki, uz garanciju da nikada nisu uskladištene na udaljenim serverima. Kao rezultat, sve vaše akreditive su uskladištene lokalno na vašim uređajima, a sinhronizacija između više mašina je isključivo peer-to-peer. Ova arhitektura eliminiše jedinstvene tačke otkaza povezane sa centralizovanim bazama podataka: nema servera koje treba kompromitovati, niti infrastrukture treće strane za pristup vašim akreditivima. Komunikacije između vaših uređaja su end-to-end enkriptovane, osiguravajući da samo ključevi koje posedujete omogućavaju pristup podacima.



![Image](assets/fr/02.webp)



Da bi ovo bilo moguće, kao što ime sugeriše, PearPass se oslanja na **Pears**, ekosistem peer-to-peer tehnologije posvećen kreiranju i izvršavanju serverless aplikacija. Pears obezbeđuje okruženje za izvršavanje, mehanizme distribucije i mrežne slojeve potrebne za pokretanje potpuno decentralizovanih aplikacija, sposobnih za direktnu sinhronizaciju između korisnika, bez ikakve centralne infrastrukture. U slučaju PearPass-a, Pears omogućava otkrivanje uređaja, uspostavljanje enkriptovane veze i sinhronizaciju trezora lozinki između vaših mašina. Ovaj pristup osigurava da PearPass ostane funkcionalan, otporan i nezavisan od bilo koje spoljne vlasti.



https://planb.academy/tutorials/computer-security/communication/pears-6d42b312-c69f-4504-8f71-b03b56c42fdd

Pored ove inovativne arhitekture, PearPass je potpuno open-source, a sve njegove funkcije su besplatne. Softver je takođe nezavisno revidiran od strane Secfault Security. Pored svoje specifične arhitekture, PearPass naravno nudi sve klasične funkcije koje se očekuju od dobrog menadžera lozinki, koje ćemo otkriti tokom ovog tutorijala.



Ukratko, dok tradicionalni menadžeri lozinki traže da verujete kompaniji i njenim serverima, PearPass usvaja logiku suvereniteta: nema oblaka, nema centralizovanih naloga, nema posrednika. Zadržavate isključivu kontrolu nad svojim akreditivima, dok istovremeno imate koristi od sinhronizacije između svojih uređaja.



## Kako da instaliram PearPass?



PearPass je dostupan na svim platformama: Windows, Linux, macOS, Android, iOS i ekstenzije za pretraživače. Nema potrebe instalirati Pears na vaš uređaj: PearPass radi samostalno.



### Instalacija na Windows



Na Windows-u, PearPass je dostupan kao klasični instalacioni program. Idite na [zvaničnu stranicu za preuzimanje](https://pass.pears.com/download), zatim kliknite na dugme `Download Windows installer`.



Kada se datoteka preuzme, otvorite instalacioni program i pratite korake koje navodi čarobnjak. Aplikaciji se zatim može pristupiti iz `Start Menu` ili putem prečice na radnoj površini.



![Image](assets/fr/03.webp)



### Instalacija na macOS



Na macOS-u, PearPass se distribuira kao disk imidž (`.dmg`). Idite na [zvaničnu stranicu za preuzimanje](https://pass.pears.com/download) i izaberite verziju koja odgovara arhitekturi vašeg Mac-a (Intel ili Apple Silicon). Nakon preuzimanja, otvorite `.dmg` fajl i pokrenite aplikaciju iz foldera `Applications`.



Prilikom prvog pokretanja, macOS će prikazati sigurnosnu poruku koja ukazuje da aplikacija dolazi s Interneta: jednostavno potvrdite za nastavak.



### Instalacija na Linux-u



Na Linuxu, PearPass je dostupan u formatu `.AppImage`, što garantuje široku kompatibilnost sa većinom distribucija bez ikakvih specifičnih zavisnosti. Preuzmite `.AppImage` datoteku sa [zvanične stranice za preuzimanje](https://pass.pears.com/download), zatim je pokrenite direktno dvostrukim klikom.



U zavisnosti od vašeg okruženja, možda ćete morati da učinite datoteku izvršnom putem svojstava datoteke (desni klik) ili pomoću komande `chmod +x`. Kada je autorizovan, PearPass se pokreće kao samostalna aplikacija.



### Instalacija ekstenzije za pregledač



PearPass nudi ekstenziju za pretraživač za automatsko prijavljivanje i brz pristup vašem sefu dok pretražujete internet. Ekstenzija je trenutno dostupna za Google Chrome i kompatibilne pretraživače. Da biste je instalirali, idite na [zvaničnu stranicu za preuzimanje](https://chromewebstore.google.com/detail/pearpass/pdeffakfmcdnjjafophphgmddmigpejh).



![Image](assets/fr/04.webp)



Kada se doda, možete ga zakačiti na alatnu traku za brz pristup. Aktiviranje ekstenzije zatim zahteva vezu sa PearPass aplikacijom instaliranom lokalno na vašem računaru (vratićemo se na ovo kasnije u tutorijalu).



### Instalacija na iOS i Android



Na iPhone i Androidu, jednostavno preuzmite aplikaciju iz svoje prodavnice aplikacija:




- [Google Play Store](https://play.google.com/store/apps/details?id=com.pears.pass);
- [App Store](https://apps.apple.com/us/app/pearpass/id6752954830).



![Image](assets/fr/05.webp)



Pored ovih klasičnih metoda instalacije, moguće je preuzeti softver direktno sa GitHub repozitorijuma, za svaki :




- [Desktop](https://github.com/tetherto/pearpass-app-desktop);
- [Mobile](https://github.com/tetherto/pearpass-app-mobile);
- [Ekstenzija za pregledač](https://github.com/tetherto/pearpass-app-browser-extension).



Kada je PearPass instaliran na jednoj ili više platformi, možete preći na početnu konfiguraciju. U ovom vodiču, počećemo konfigurisanjem softvera na desktopu, zatim ga sinhronizovati sa ekstenzijom za pregledač i mobilnom aplikacijom.



## Kako da napravim PearPass sef?



Kada prvi put pokrenete PearPass na svom računaru, aplikacija vas vodi kroz dva koraka: postavljanje glavne lozinke i zatim kreiranje vašeg prvog sefa.



### Postavite glavnu lozinku



Kada se aplikacija prvi put pokrene na desktopu, kliknite na dugme `Preskoči`, a zatim `Nastavi` da biste prošli kroz uvodni ekran i stigli do faze podešavanja glavne lozinke.



![Image](assets/fr/06.webp)



Sledeći važan korak je odabir vaše glavne lozinke. Kao što smo videli u uvodu, ova lozinka je veoma važna, jer vam omogućava pristup svim ostalim lozinkama sačuvanim u menadžeru. Tehnički, koristi se za izvođenje kriptografskih ključeva koji se koriste za šifrovanje vaših podataka.



Glavna lozinka nosi dva glavna rizika: gubitak i kompromitaciju. Ako izgubite pristup ovoj lozinci, više nećete moći da pristupite svojim akreditivima. Naime, PearPass nikada ne čuva vašu glavnu lozinku: **ako se izgubi, vaši akreditivi su trajno izgubljeni**. Ne postoji nikakav mehanizam oporavka. Suprotno tome, ako je ova lozinka kompromitovana i napadač dobije pristup jednom od vaših uređaja, moći će da pristupi svim vašim nalozima.



Da biste ograničili rizik od gubitka, možete napraviti fizičku rezervnu kopiju vaše glavne lozinke, na primer na papiru, i čuvati je na sigurnom mestu. Idealno bi bilo da ovu rezervnu kopiju zapečatite u kovertu kako biste povremeno mogli proveriti da joj nije pristupljeno. S druge strane, nikada nemojte praviti digitalnu rezervnu kopiju ove lozinke.



Da biste smanjili rizik od kompromitovanja, vaša glavna lozinka mora biti jaka. Trebalo bi da bude što duža, da uključuje širok spektar karaktera i da bude izabrana na potpuno nasumičan način. U 2025. godini, minimalne preporuke zahtevaju najmanje 13 karaktera uključujući velika i mala slova, brojeve i simbole, pod uslovom da je lozinka nasumična. Međutim, preporučio bih lozinku od najmanje 20 karaktera, ako ne i više, sa svim vrstama karaktera, kako biste osigurali dugotrajniji nivo sigurnosti.



Unesite svoju glavnu lozinku u predviđeno polje, potvrdite je još jednom, a zatim kliknite na dugme `Nastavi`.



![Image](assets/fr/07.webp)



Bićete preusmereni na ekran za prijavu: unesite svoju glavnu lozinku da proverite da li sve radi ispravno.



![Image](assets/fr/08.webp)



### Kreirajte svoj prvi sef



Kada se prijavite, PearPass će vas podstaći da kreirate svoj prvi sef. Sef je šifrovani kontejner u kojem se čuvaju vaše lozinke, identifikacije, sigurnosne beleške i druge informacije. Svaki sef je izolovan i može se identifikovati po jedinstvenom imenu, što vam omogućava da organizujete svoje podatke prema vašim potrebama (lične, profesionalne, specifični projekti...).



Kliknite na dugme `Create a new vault`.



![Image](assets/fr/09.webp)



Izaberite ime za ovaj trezor, zatim kliknite na `Kreiraj novi trezor` ponovo da završite kreiranje.



![Image](assets/fr/10.webp)



Vaš sef je odmah spreman za upotrebu. Možete odmah početi dodavati lozinke, prijave ili sigurne beleške.



![Image](assets/fr/11.webp)



## Kako da dodam prijavu na PearPass?



Jednom kada kreirate svoj sef, možete početi da čuvate svoje predmete u njemu. PearPass podržava registraciju mnogih vrsta predmeta:




- prijavite se na sajt ili uslugu ;
- identitet: vaši lični podaci za brzo popunjavanje obrazaca, ali i za čuvanje identifikacionih dokumenata direktno u PearPass ;
- kreditna kartica: brojevi vaše kreditne kartice za brže plaćanje prilikom kupovine na mreži;
- Wi-Fi: lozinke za vaše Wi-Fi mreže ;
- PassPhrase: tajna fraza sastavljena od nekoliko reči (upozorenje: snažno savetujem da je ne koristite za wallet Bitcoin mnemoničke fraze);
- napomena: kreiranje sigurnih beleški ;
- prilagođeno: ova funkcija vam omogućava da kreirate prilagođeni tip elementa, prilagođen vašim specifičnim potrebama.



Pokrenite PearPass i prijavite se koristeći svoju glavnu lozinku.



![Image](assets/fr/12.webp)



Izaberite sef u koji želite da sačuvate ovaj identifikator.



![Image](assets/fr/13.webp)



Na početnoj stranici, kliknite na dugme za dodavanje nove stavke, u zavisnosti od tipa informacija koje želite da zabeležite. U mom slučaju, želim da dodam prijavu za svoj nalog na Plan ₿ Academy vebsajtu: tako da kliknem na dugme `Create a Login`.



![Image](assets/fr/14.webp)



Kada odaberete tip stavke koju želite da dodate, pojavljuje se formular koji vam omogućava da unesete informacije povezane sa dotičnom uslugom. U zavisnosti od vaših potreba, možete uneti naziv usluge, korisničko ime, lozinku i, ako je potrebno, adresu veb-sajta i dodatne beleške.



PearPass takođe ima generator lozinki, omogućavajući vam da kreirate jaku lozinku direktno iz forme. Da biste ga koristili, kliknite na ikonu koja predstavlja tri male tačke u polju `Password`, izaberite željenu dužinu, zatim kliknite na `Insert password`.



Kada su sva polja popunjena, kliknite na dugme `Save` da sačuvate identifikator u sefu.



![Image](assets/fr/15.webp)



Identifikator je sada sačuvan. Pojavljuje se na listi stavki u odabranom sefu i može se pregledati klikom na njega.



![Image](assets/fr/16.webp)



Možete lako izmeniti element klikom na njega, a zatim na dugme `Edit`. Takođe ga možete obrisati klikom na tri male tačke u gornjem desnom uglu interfejsa, a zatim na `Delete element`.



![Image](assets/fr/22.webp)



Na mobilnom uređaju, logika ostaje ista, iako je interfejs prilagođen. Nakon prijavljivanja, izaberite željeni sef, dodirnite dugme `+`, izaberite tip stavke koja će biti kreirana, a zatim popunite potrebne informacije.



![Image](assets/fr/17.webp)



## Kako organizovati PearPass?



Kao što smo videli u prethodnim odeljcima, PearPass vam omogućava da kreirate nekoliko različitih trezora. Ovo omogućava razdvajanje različitih upotreba i predstavlja prvi nivo organizacije za vaš menadžer lozinki. Sa početne stranice, možete lako preći iz jednog trezora u drugi klikom na strelicu u gornjem levom uglu interfejsa.



![Image](assets/fr/18.webp)



Još jedan način organizovanja vaših lozinki, čak i unutar trezora, jeste kreiranje fascikli. Da biste to uradili, u levom stupcu interfejsa kliknite na simbol `+` pored `Sve fascikle`, zatim unesite ime fascikle koju želite da kreirate.



![Image](assets/fr/19.webp)



Možete zatim sačuvati identifikatore po vašem izboru, bilo direktno prilikom kreiranja stavke, ili kasnije klikom na `Edit`. Sve što treba da uradite je da izaberete željeni folder u gornjem levom uglu forme.



![Image](assets/fr/20.webp)



Nakon otvaranja stavke, kao što je prijava, možete kliknuti na ikonu zvezde u gornjem desnom uglu interfejsa da biste je dodali u omiljene. Omiljene stavke se mogu brzo pronaći u posebnom folderu, pored njihovog osnovnog foldera.



![Image](assets/fr/21.webp)



Konačno, tu je traka za pretragu na vrhu interfejsa, tako da možete brzo pronaći stavku koju tražite, čak i ako vaš trezor sadrži mnogo identifikatora.



## Kako da sinhronizujem PearPass na svom mobilnom?



Sada kada imate funkcionalni trezor sa stavkama pohranjenim na vašem računaru, verovatno ćete želeti da pristupite svojim lozinkama sa svog pametnog telefona ili drugog uređaja. PearPass vam omogućava da sinhronizujete vaš menadžer na više uređaja sigurno koristeći Pears. Hajde da saznamo kako.



Da biste započeli, na izvornom računaru (na primer, vašem računaru), prijavite se u svoj trezor koristeći svoju glavnu lozinku. Kada ste na početnoj stranici, kliknite na dugme `Dodaj uređaj`, koje se nalazi u donjem desnom uglu interfejsa.



![Image](assets/fr/23.webp)



PearPass zatim generiše pozivni link, takođe dostupan kao QR kod, za sinhronizaciju izabranog trezora na uređaju po vašem izboru.



![Image](assets/fr/24.webp)



Ako želite da sinhronizujete na svom mobilnom uređaju, prvo instalirajte aplikaciju, a zatim je pokrenite. Od vas će se tražiti da kreirate glavnu lozinku za vaš mobilni menadžer. Možete izabrati da koristite istu lozinku kao na vašem računaru, ili drugačiju. U svim slučajevima, pratite iste preporuke: jaka, nasumična lozinka sačuvana na fizičkom medijumu.



![Image](assets/fr/25.webp)



Zatim možete aktivirati biometrijsku autentifikaciju ako želite, kako biste izbegli ručno unošenje glavne lozinke svaki put kada otključavate svoj mobilni.



![Image](assets/fr/26.webp)



Ponovo unesite svoju glavnu lozinku, zatim kliknite na dugme `Nastavi`.



![Image](assets/fr/27.webp)



Odaberite opciju `Load a vault`, zatim kliknite `Scan QR Code` i skenirajte pozivni QR kod prikazan od strane PearPass-a na vašem izvornom uređaju (računaru).



![Image](assets/fr/28.webp)



Vaši trezori na računaru i mobilnom uređaju su sada sinhronizovani. Svaki ID dodat na jednom uređaju biće sigurno sačuvan i repliciran na drugom.



![Image](assets/fr/29.webp)



Na mobilnom uređaju možete takođe, ukoliko to želite, aktivirati automatsko popunjavanje polja. Da biste to uradili, idite na `Settings > Advanced`, a zatim kliknite na dugme `Set as Default` u odeljku `Autofill`.



![Image](assets/fr/30.webp)



## Kako da sinhronizujem PearPass sa ekstenzijom za pregledač?



Imati menadžer lozinki koji je sinhronizovan između vašeg računara i pametnog telefona već je veoma praktično, ali integrisati ga direktno u vaš pregledač je još praktičnije. Da biste to uradili, počnite tako što ćete [dodati zvanično PearPass proširenje u vaš pregledač](https://chromewebstore.google.com/detail/pearpass/pdeffakfmcdnjjafophphgmddmigpejh).



![Image](assets/fr/31.webp)



Iz softvera PearPass instaliranog na vašem lokalnom računaru, idite na `Settings > Advanced`, zatim aktivirajte opciju `Activate browser extension`.



![Image](assets/fr/32.webp)



PearPass generiše token fajl za uparivanje. Kopiraj ga.



![Image](assets/fr/33.webp)



Zatim otvorite PearPass ekstenziju u vašem pregledaču, zalepite token uparivanje i kliknite na dugme `Verify`, a zatim na `Complete`.



![Image](assets/fr/34.webp)



Vaš menadžer lozinki je sada sinhronizovan sa ekstenzijom pregledača.



![Image](assets/fr/35.webp)



Sada ga možete koristiti za jednostavno povezivanje sa vašim raznim web nalozima.



![Image](assets/fr/36.webp)



Sada znate kako da koristite PearPass menadžer lozinki. Pored ovog alata, svakodnevna digitalna sigurnost zavisi od pravilne upotrebe odgovarajućih rešenja. Ako želite da naučite kako da postavite sigurno, stabilno i efikasno lično digitalno okruženje, pozivam vas da otkrijete naš kurs obuke posvećen ovoj temi:



https://planb.academy/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1