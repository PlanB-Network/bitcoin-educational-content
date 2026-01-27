---
name: Ashigaru
description: fork iz Samourai Wallet za osiguranje, upravljanje i mešanje vaših bitkoina
---

![cover](assets/cover.webp)



Ashigaru je Bitcoin mobilna wallet aplikacija koja je nastavak projekta Samourai Wallet, ali u novom obliku. Ovaj softver je nastao u posebnom kontekstu: u aprilu 2024. godine, osnivači Samourai Wallet su uhapšeni od strane američkih vlasti, a njihovi serveri su zaplenjeni. Iako je sama aplikacija Samurai ostala upotrebljiva, trenutno se više ne održava. Ashigaru je besplatna fork verzija Samurai Wallet, koju održava anonimni tim kako bi se garantovao kontinuitet funkcionalnosti Samurai-a i očuvala njegova originalna filozofija: odbrana privatnosti i suvereniteta Bitcoin korisnika.



Ashigaru preuzima veliki deo DNK Samuraija: sličan interfejs, očigledno samostalni pristup, otvoreni kod i fokus na privatnost. Kod je distribuiran pod GNU GPLv3 licencom, što osigurava da svako može da pregleda, modifikuje ili redistribuira softver.



Aplikacija Ashigaru integriše skup naprednih alata za poverljivost i upravljanje vašim UTXO-ima:




- Whirlpool**, coinjoin protokol zasnovan na Zerolink-u, omogućava vam da prekinete determinističke veze između ulaza i izlaza transakcija, bez gubitka suvereniteta nad vašim sredstvima.
- PayNym**, koji implementira višekratne kodove za plaćanje (BIP47), sada je predstavljen putem sistema avatara "*Pepehash*".
- Ricochet**, funkcija koja dodaje posredne skokove transakcijama kako bi ih učinila težim za praćenje.
- I naravno ***Coin Control*** za precizno odabiranje, zamrzavanje i označavanje vaših UTXO-a.
- Grupno Trošenje***, za smanjenje troškova grupisanjem nekoliko uplata u jednu transakciju.
- **Stealth Mode**, koji sakriva aplikaciju na vašem mobilnom telefonu iza lažnog pokretača kako bi ostao neprimećen tokom fizičke inspekcije vašeg telefona.
- Napredni alati za trošenje za optimizaciju vaše poverljivosti (payjoin, stonewall...).
- Optimizovani sistem oporavka koristeći Passphrase BIP39.
- Sistem za automatsku optimizaciju izbora transakcijskih naknada.



![Image](assets/fr/01.webp)



Ashigaru je stoga namenjen korisnicima koji su svesni problema u vezi sa praćenjem transakcija na Bitcoin. Bilo da ste korisnik koji vodi računa o privatnosti, iskusan bitkoiner posvećen samostalnom čuvanju sredstava, ili pojedinac izložen rizicima povećanog nadzora, ova wallet aplikacija vam pruža alate potrebne za ponovno preuzimanje kontrole nad vašim aktivnostima na Bitcoin.



Ashigaru je dostupan u mobilnoj verziji putem svoje aplikacije, koju ćemo istražiti u ovom vodiču. Ali se takođe može koristiti na računaru sa ***Ashigaru Terminalom***, koji ćemo predstaviti u budućem vodiču.



![Image](assets/fr/02.webp)



U ovom vodiču, želeo bih da vas upoznam sa osnovnom upotrebom Ashigaru-a: instalacija, povezivanje sa Dojo-om, bekap, primanje i slanje bitkoina. Napredni alati će biti predstavljeni u drugim posvećenim vodičima.



## 1. Preduslovi za Ašigaru



Aplikacija zahteva nekoliko preduslova da bi ispravno radila. Pre svega, to nije aplikacija dostupna na klasičnim prodavnicama kao što su Google Play Store ili App Store. Instalira se ručno na vaš telefon samo iz njegove `.apk` datoteke, koja se može preuzeti putem Tor mreže. Dakle, ako koristite iPhone, ovaj metod neće raditi: biće vam potreban Android uređaj.



Da biste preuzeli `.apk` datoteku putem Tor-a, potreban vam je pregledač sposoban za pristup `.onion` sajtovima. Najlakši način je instalirati Tor Browser aplikaciju na vaš telefon, dostupnu na [Google Play Store](https://play.google.com/store/apps/details?id=org.torproject.torbrowser) ili direktno [putem njenog `.apk`](https://www.torproject.org/download/#android).



![Image](assets/fr/03.webp)



Većina najnovijih pametnih telefona po defaultu blokira instalaciju aplikacija iz nepoznatih izvora. Moraćete privremeno aktivirati ovu opciju za Tor Browser u podešavanjima vašeg uređaja kako biste omogućili instalaciju. Kada aplikacija bude instalirana, ne zaboravite da deaktivirate ovu funkciju kako biste pojačali sigurnost vašeg telefona.



Još jedan bitan preduslov za korišćenje Ashigaru je Bitcoin Dojo čvor. Iz razloga bezbednosti i suvereniteta, Ashigaru tim ne održava centralizovani server za povezivanje vaše aplikacije. Dakle, biće potrebno da pokrenete sopstvenu Dojo instancu ili da se povežete na pouzdanu.



Dojo omogućava vašoj Ashigaru aplikaciji da konsultuje informacije sa blockchain-a, pregleda stanja vaših adresa i emituje vaše transakcije na Bitcoin mreži.



Da biste saznali više o Dojo-u i naučili kako da ga instalirate, pozivam vas da pratite ovaj posvećeni vodič:



https://planb.academy/tutorials/node/bitcoin/dojo-aa818a21-e701-48a2-8421-63c6186ed23f

Ako stvarno ne možete priuštiti da vodite svoj Dojo, možete pronaći ljude koji su voljni da podele svoju instancu besplatno na [dojobay.pw](https://www.dojobay.pw/mainnet/). Ovo može biti privremeno rešenje, ali na duže staze, preporučujem da koristite svoj Dojo kako biste garantovali svoj suverenitet i poverljivost.



## 2. Proverite i instalirajte Ashigaru aplikaciju



### 2.1. Preuzmite Ashigaru aplikaciju



Na svom telefonu, otvori Tor Browser i idi na [zvaničnu Ashigaru veb stranicu](https://ashigaru.rs/download/), u odeljku `Download`. Zatim klikni na dugme `Download for Android` da preuzmeš instalacionu datoteku.



![Image](assets/fr/04.webp)



Pre nego što instalirate aplikaciju na svoj uređaj, proverićemo njenu autentičnost i integritet. Ovo je veoma važan korak, posebno kada instalirate aplikaciju direktno iz `.apk' fajla.



### 2.2. Proveri Ashigaru aplikaciju



Vratite se na [zvaničnu Ashigaru veb stranicu](https://ashigaru.rs/download/) u odeljku `Download`, zatim kopirajte poruku prikazanu ispod naslova `SHA-256 Hash of the APK file`. Kopirajte ceo blok, od `BEGIN PGP SIGNED MESSAGE` do `END PGP SIGNATURE`.



![Image](assets/fr/05.webp)



Još uvek na svom telefonu, otvorite novu karticu u Tor Browser-u i idite na [alatku za verifikaciju Keybase](https://keybase.io/verify). Zalepite poruku koju ste upravo kopirali u predviđeno polje, zatim kliknite na dugme `Verify`.



![Image](assets/fr/06.webp)



Ako je potpis originalan, Keybase će prikazati poruku koja potvrđuje da su datoteku potpisali Ashigaru programeri. Takođe možete kliknuti na profil `ashigarudev` koji je označen od strane Keybase-a i proveriti da li njihov otisak ključa tačno odgovara: `A138 06B1 FA2A 676B`.



Međutim, ako se u ovoj fazi pojavi greška, to znači da je potpis nevažeći. U tom slučaju, **ne instalirajte APK**. Počnite ponovo od početka ili zatražite pomoć od zajednice pre nego što nastavite.



![Image](assets/fr/07.webp)



Keybase vam je obezbedio heš aplikacije. Sada ćemo proveriti da li se heš `.apk` fajla koji ste preuzeli poklapa sa onim verifikovanim na Keybase. Da biste to uradili, idite na [HASH FILE ONLINE](https://hash-file.online/).



![Image](assets/fr/08.webp)



Kliknite na dugme `BROWSE...` i odaberite `.apk` datoteku preuzetu u koraku 2.1.


Zatim izaberite heš funkciju `SHA-256`, i kliknite `CALCULATE HASH` da izračunate heš vaše datoteke.



![Image](assets/fr/09.webp)



Sajt će prikazati hash vaše `.apk` datoteke. Uporedite ga sa hashom koji ste verifikovali na Keybase.io. Ako su dva hasha identična, provera autentičnosti i integriteta je uspešna. Sada možete nastaviti sa instalacijom aplikacije.



![Image](assets/fr/10.webp)



### 2.3. instalirajte aplikaciju Ashigaru



Da biste instalirali aplikaciju, otvorite upravitelj datoteka na svom telefonu i idite u fasciklu preuzimanja. Zatim kliknite na `.apk` datoteku koju ste upravo proverili i potvrdite instalaciju kada se to zatraži.



![Image](assets/fr/11.webp)



Ashigaru je sada instaliran na vašem telefonu.



## 3. Inicijalizujte aplikaciju i kreirajte Bitcoin portfolio



Kada prvi put pokrećete aplikaciju, izaberite `MAINNET`.



![Image](assets/fr/12.webp)



Zatim kliknite na `Get Started`.



![Image](assets/fr/13.webp)



Sada ćemo kreirati novi Bitcoin portfolio. Pritisnite dugme `Create a new wallet`.



![Image](assets/fr/14.webp)



### 3.1. kreiraj Bitcoin portfolio



Ashigaru zahteva passphrase BIP39. Izaberite svoj passphrase i unesite ga u odgovarajuća polja. Mora biti što duži i nasumičan kako bi odoleo brute-force napadu.



Napravite fizičku rezervnu kopiju ovog passphrase odmah. Ovo je veoma važan korak: ako izgubite svoj telefon, **ako više nemate ovaj passphrase, više nećete moći da pristupite svojim bitkoinima** sačuvanim sa vašim Ashigaru wallet. Ovaj isti passphrase se takođe koristi za šifrovanje wallet fajla za oporavak.



Ako ne znate šta je passphrase, ili ne razumete u potpunosti kako funkcioniše, toplo preporučujem da pročitate ovaj dodatni vodič. Ovo je važno, jer je passphrase ključni element vaše sigurnosti: pogrešno razumevanje njegove upotrebe može rezultirati trajnim gubitkom vaših sredstava.



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Kada unesete svoj passphrase, kliknite na `NEXT`.



![Image](assets/fr/15.webp)



Zatim izaberite PIN kod. Ovaj kod će se koristiti za otključavanje vašeg Ashigaru wallet, štiteći ga od neovlašćenog fizičkog pristupa. Nije uključen u kriptografsku derivaciju vaših wallet ključeva. To znači da će, čak i bez poznavanja PIN koda, svako ko ima vašu mnemoniku i passphrase moći ponovo da pristupi vašim bitcoinima.



Odaberite dug, nasumičan PIN kod. Zapamtite da čuvate rezervnu kopiju na drugom mestu od vašeg telefona, kako biste sprečili da budu ugroženi istovremeno.



![Image](assets/fr/16.webp)



Kada je PIN kod kreiran, Ashigaru prikazuje vašu wallet mnemoničku frazu. Upozorenje: ova fraza, u kombinaciji sa vašim passphrase, daje potpuni pristup vašim bitcoinima. Svako ko je poseduje može preuzeti vaše fondove, čak i ako nema pristup vašem telefonu. Ova sekvenca od 12 reči može se koristiti za obnavljanje vašeg wallet u slučaju gubitka, krađe ili loma vašeg telefona. Stoga je važno da je sačuvate sa najvećom pažnjom na fizičkom mediju (papir ili metal).



Nikada ne čuvajte ovu frazu u digitalnom obliku, jer rizikujete da izložite svoja sredstva krađi. U zavisnosti od vaše sigurnosne strategije, možete napraviti nekoliko fizičkih kopija, ali je nikada ne delite. Čuvajte reči u tačnom redosledu i obavezno ih numerišite.



Na kraju, nikada ne čuvajte mnemonik i passphrase na istom mestu. Ako bi oba bila istovremeno ugrožena, napadač bi mogao dobiti pristup vašem wallet.



![Image](assets/fr/17.webp)



Da biste saznali više o tome kako da osigurate svoju mnemonicku frazu, pogledajte ovaj dodatni vodič :



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Ashigaru vas zatim zamoli da ponovo potvrdite vaš passphrase. Iskoristite ovu priliku da proverite da li je vaša fizička rezervna kopija ispravna.



![Image](assets/fr/18.webp)



### 3.2. poveži dojo



Sledeći korak je povezivanje sa vašim Dojo-om. Kao što je objašnjeno u uvodu, Ashigaru mora biti povezan sa Dojo-om kako bi mogao da komunicira sa Bitcoin mrežom.



Prijavite se na "Maintenance Tool" vašeg Dojo-a i otvorite meni `PAIRING`.



![Image](assets/fr/19.webp)



Na Ashigaru, pritisnite dugme `Scan QR`, zatim skenirajte QR kod za povezivanje koji prikazuje vaš DMT. Zatim kliknite `Continue` da potvrdite.



![Image](assets/fr/20.webp)



Unesite svoj PIN kod da otključate wallet. Ovo će vas odvesti na stranicu za sinhronizaciju. Normalno je da vidite greške *PayNym* u ovoj fazi, jer je wallet nov. Jednostavno kliknite na `Nastavi`.



![Image](assets/fr/21.webp)



Bićete preusmereni na početnu stranicu vašeg portfolija.



![Image](assets/fr/22.webp)



Pre nego što nastavite dalje, preporučujem da izvršite test oporavka dok wallet još uvek ne sadrži bitcoin. Ovo će vam omogućiti da proverite da li vaši papirni bekapi rade ispravno. Da biste saznali kako, pratite ovaj vodič:



https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## 4. Postavljanje Ashigaru aplikacije



Da biste pristupili postavkama aplikacije, kliknite na sliku vašeg *PayNym* u gornjem levom uglu, a zatim odaberite `Settings`.



![Image](assets/fr/23.webp)



Ovde ćete pronaći nekoliko opcija za prilagođavanje rada Ashigaru vašim potrebama. Međutim, toplo preporučujem da odmah od početka aktivirate 2 važna parametra.



Počnite otvaranjem menija `Security > Stealth mode`, zatim aktivirajte ovu funkciju ako vam je potrebna. Ona skriva Ashigaru aplikaciju iza imena, logotipa i interfejsa obične aplikacije instalirane na vašem telefonu. Cilj je sprečiti bilo koga da identifikuje Ashigaru u slučaju fizičkog pregleda vašeg telefona.



![Image](assets/fr/24.webp)



Svaka lažna aplikacija u ponudi ima specifičnu metodu za otključavanje pravog Ashigaru interfejsa. Na primer, ako izaberete kalkulator, Ashigaru aplikacija nestaje sa vašeg početnog ekrana i zamenjuje je lažni kalkulator. Kada ga otvorite, vidite klasičan radni interfejs kalkulatora, ali da biste pristupili Ashigaru, sve što treba da uradite je da brzo pet puta dodirnete simbol `=`.



Drugi važan parametar koji treba aktivirati je [**RBF** (*Replace-by-Fee*)](https://planb.academy/resources/glossary/rbf-replacebyfee). Ova opcija vam omogućava da povećate trošak transakcije ako se zaglavi u mempool-ovima jer je trošak prenizak. Možete ga aktivirati putem menija `Transakcije > Potroši koristeći RBF`.



![Image](assets/fr/25.webp)



Savet: Možete promeniti jedinicu prikaza vašeg portfolija sa `BTC` na `sat` jednostavnim klikom na ukupan saldo prikazan na početnoj stranici.



## 5. Primite bitkoine na Ashigaru



Sada kada je vaš portfolio operativan, možete primati satse. Da biste to učinili, pritisnite dugme `+` u donjem desnom uglu interfejsa, a zatim zeleno dugme `Receive`.



![Image](assets/fr/26.webp)



Ashigaru zatim prikazuje prvu neiskorišćenu adresu za primanje u vašem wallet, kako bi se sprečilo ponovno korišćenje adrese (ponovno korišćenje adrese je veoma loša praksa za vašu privatnost). Zatim možete proslediti ovu adresu osobi ili servisu koji treba da vam pošalje bitkoine.



![Image](assets/fr/27.webp)



Jednom kada transakcija bude emitovana na mreži, automatski će se pojaviti na početnoj stranici aplikacije.



![Image](assets/fr/28.webp)



## 6. Pošalji bitkoine sa Ashigaru



Sada kada imate bitkoine u vašem Ashigaru wallet, možete ih i poslati. Da biste to uradili, pritisnite dugme `+` u donjem desnom uglu, zatim izaberite crveno dugme `Send`.



![Image](assets/fr/29.webp)



Zatim izaberite račun sa kojeg želite izvršiti trošak. Za sada se još nismo bavili `Postmix` računom, rezervisanim za coinjoin transakcije, koji ćemo obraditi u kasnijem tutorijalu. Dakle, poslaćemo sredstva sa glavnog depozitnog računa.



![Image](assets/fr/30.webp)



Unesite detalje transakcije: iznos koji treba poslati i Bitcoin adresu primaoca.



![Image](assets/fr/31.webp)



Klikom na tri male tačke u gornjem desnom uglu, zatim na `Prikaži nepotrošene izlaze`, možete takođe precizno odabrati koje UTXO-ove želite da potrošite, kako biste poboljšali svoju privatnost.



![Image](assets/fr/32.webp)



Kada popunite sve detalje, kliknite na belu strelicu na dnu interfejsa da nastavite.



Zatim ćete biti prebačeni na stranicu sa sažetkom koja prikazuje sve detalje vaše transakcije. Prikazano je nekoliko važnih elemenata:




- U bloku `Destination`, proverite još jednom da li su adresa primaoca i poslata suma tačne;
- U bloku `Fees` možete videti stopu naknade koju je automatski odabrao Ashigaru i, ako je potrebno, izmeniti je klikom na `MANAGE` ;
- Blok `Transaction` označava tip transakcije koju ćete izvršiti. Ovde govorimo o jednostavnoj transakciji, ali Ashigaru takođe podržava druge tipove transakcija optimizovanih za privatnost, koje ćemo detaljno obraditi u budućem vodiču;
- Crveni blok `Transaction Alert` upozorava vas ako vaša transakcija pokazuje obrasce koje alati za analizu lanca mogu prepoznati, a koji bi mogli ugroziti vašu privatnost. Klikom na njega možete pogledati detalje. Na primer, u mom slučaju, Ashigaru mi kaže da je poslata suma okrugla (`3000 sats`), što mi omogućava da zaključim koji izlaz odgovara trošku, a koji razmeni. Da biste saznali više o ovim heuristikama analize lanca, pozivam vas da pratite moju BTC 204 obuku na Plan ₿ Academy ;
- Konačno, možete dodati oznaku svojoj transakciji kako biste zabeležili njenu svrhu.



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Kada proverite sve informacije, koristite zelenu strelicu da pošaljete bitkoine. Držite strelicu, zatim je prevucite udesno da potvrdite otpremu.



![Image](assets/fr/33.webp)



Vaša transakcija je emitovana na Bitcoin mreži.



![Image](assets/fr/34.webp)



## 7. Oporavak vašeg Ashigaru wallet



Oporavak Ashigaru wallet se malo razlikuje od klasičnog Bitcoin wallet, jer aplikacija koristi iste metode kao Samurai Wallet. Ako izgubite pristup svom wallet (bilo zato što ste zaboravili svoj PIN, deinstalirali ga ili izgubili telefon), postoji nekoliko načina da povratite svoje bitkoine.



Ako još uvek imate pristup svom telefonu, ili ako ste napravili rezervnu kopiju ove datoteke, najjednostavnija metoda je da koristite rezervnu datoteku `ashigaru.txt`. Ova datoteka sadrži sve informacije koje su vam potrebne da obnovite svoj portfolio na novoj instanci Ashigaru (ili na Sparrow Wallet), ali je šifrovana sa passphrase koji ste definisali u koraku 3.1 ovog uputstva. Stoga morate imati i datoteku `ashigaru.txt` i vaš passphrase da biste koristili ovu metodu.



Sa ova dva elementa, možete, na primer, obnoviti svoj portfolio na Sparrow Wallet.



![Image](assets/fr/35.webp)



Ako nemate pristup datoteci `ashigaru.txt`, i dalje možete povratiti pristup svojim sredstvima koristeći svoju passphrase mnemonicku frazu, kao što biste to učinili za bilo koji drugi Bitcoin portfelj. Preporučujem da ovaj povratak izvršite ili na novoj Ashigaru instanci, ili direktno na Sparrow Wallet, kako biste lako povratili zaobilazne putanje sa Whirlpool ako ste ga koristili. Alternativno, možete uneti ove informacije u bilo koji drugi softver kompatibilan sa BIP39 ručnim unosom putanja derivacije.



Za više informacija o ovom procesu, molimo vas da pogledate kompletan vodič koji sam napisao o oporavku Wallet Samurai wallet. Pošto je Ashigaru fork, procedura je identična:



https://planb.academy/tutorials/wallet/backup/samourai-recover-23bb6221-ea3e-42e6-a5b7-e6dbef5073c3

Kao što možete videti, bez obzira na metodu restauracije koju koristite, passphrase je neophodan. Zato ga obavezno pažljivo sačuvajte. Takođe možete napraviti nekoliko kopija, u zavisnosti od vaše strategije bezbednosti.



## 8. Ažuriraj aplikaciju



Da biste ažurirali Ashigaru aplikaciju, pošto ste je instalirali iz `.apk` fajla, a ne preko Play Store-a kao regularnu aplikaciju, potrebno je da preuzmete novi `.apk` fajl koji odgovara ažuriranoj verziji, a zatim ga ručno instalirate.



Ponovite korake opisane u odeljku 2 ovog vodiča, osim što kada kliknete na `.apk` datoteku da pokrenete instalaciju, **vaš Android telefon treba da vam ponudi opciju `Update`, a ne `Install`**.



![Image](assets/fr/41.webp)



Ovo je veoma važna tačka: ako Android prikazuje `Install` umesto `Update`, verovatno instalirate lažnu verziju. U tom slučaju, odmah prekinite proceduru instalacije.



Kao i kod prve instalacije, molimo proverite autentičnost i integritet `.apk` datoteke pre nego što nastavite sa ažuriranjem.



Da biste saznali kada je dostupna nova verzija, povremeno proveravajte zvaničnu Ashigaru veb stranicu. Budite sigurni, Ashigaru je stabilna, zrela aplikacija, nasleđena od Samourai Wallet, a ažuriranja su relativno retka u poređenju sa mlađim softverom.



## 9. Donirajte za projekat Ashigaru



Ashigaru je projekat otvorenog koda. Ako želite da podržite njegov razvoj, možete donirati direktno iz aplikacije putem PayNym-a.



Da biste to uradili, kliknite na vaš PayNym u gornjem desnom uglu interfejsa, zatim izaberite vaš kod plaćanja koji počinje sa `PM...`.



![Image](assets/fr/36.webp)



Zatim pritisnite dugme `+` u donjem desnom uglu ekrana.



![Image](assets/fr/37.webp)



Izaberite `Ashigaru Open Source Project` kao primaoca.



![Image](assets/fr/38.webp)



Kliknite na dugme `CONNECT` da uspostavite BIP47 komunikacioni kanal (više o ovom protokolu u tutorijalu ispod).



https://planb.academy/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093

![Image](assets/fr/39.webp)



Kada transakcija obaveštenja bude potvrđena, možete poslati svoje donacije projektu klikom na malu belu strelicu u gornjem desnom uglu interfejsa.



![Image](assets/fr/40.webp)



Sada znate kako da koristite osnovne funkcije Ashigaru aplikacije. U budućim tutorijalima, pogledaćemo kako da iskoristite napredne transakcije trošenja, kao i Whirlpool, implementaciju coinjoin-a nasleđenu od Samurai Wallet.
https://planb.academy/tutorials/privacy/on-chain/ashigaru-terminal-9a0d46d3-33b9-4c64-84c5-bfa25b3a0add
