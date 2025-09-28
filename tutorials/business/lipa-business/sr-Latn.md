---
name: Lipa for Business
description: Bitcoin i Lightning rešenja za plaćanje za trgovce
---

![cover](assets/cover.webp)



Trgovci su sada sve više zainteresovani za prihvatanje Bitcoin uplata putem Lightning Network. Za razliku od tradicionalnih plaćanja kreditnim karticama, koja uključuju visoke naknade i duge vreme obrade, Lightning transakcije su praktično trenutne, nisu podložne povraćaju sredstava i čuvaju poverljivost kupaca.



Da bi preduzeće lako usvojilo Bitcoin, platno rešenje mora ostati jednostavno sa intuitivnom Interface kasom, nuditi funkcije za više korisnika i idealno nuditi automatsku konverziju u lokalnu valutu kako bi se ublažila volatilnost.



**Lipa for Business** je savršeno rešenje za ove potrebe. To je švajcarsko rešenje koje je razvila Lightning Payment Services AG, dizajnirano da omogući trgovcima da prihvate Bitcoin Lightning uplate jednostavno i efikasno, dok ostaju bez starateljstva.



*Napomena: Snimci ekrana korišćeni u ovom vodiču su preuzeti sa zvanične Lipa for Business veb stranice (lipa.swiss/en/for-business) i koriste se u obrazovne svrhe*



## Predstavljamo Lipa za Biznis



Lipa for Business je mobilna aplikacija koja radi kao Bitcoin i Lightning kasa. Nudi pojednostavljeni Interface za prikupljanje uplata u Sats i integriše profesionalne funkcije: pristup zaposlenih, izvozi za računovodstvo, veb kontrolna tabla, sve to bez ikakvog preuzimanja vaših sredstava.



### Ključne karakteristike



**Instant Lightning payments**: Bitcoin Lightning fakture se generišu za nekoliko sekundi, osiguravajući praktično trenutne transakcije bez bankarskih posrednika. Naknade su niske i transparentne u poređenju sa tradicionalnim rešenjima.



**Interface POS intuitivan**: Aplikacija pruža jasan Interface POS, dizajniran za jednostavnu upotrebu u prodavnici. Unesite iznos u lokalnoj valuti, a aplikacija odmah prikazuje iznos u BTC i QR kod za plaćanje. Kompatibilna sa svim Lightning novčanicima na tržištu.



**Upravljanje sa više zaposlenih**: Svi zaposleni mogu koristiti aplikaciju za isplatu, bez pristupa sredstvima. Vlasnik zadržava potpunu kontrolu, dok sinhronizacija u oblaku osigurava da nijedna transakcija nije izgubljena. Svaki zaposleni dobija poseban pristup putem QR koda pozivnice.



**Automatska konverzija u CHF**: Za švajcarske trgovce, Lipa nudi trenutnu konverziju prodaje u švajcarske franke na bankovnom računu. Ova opcija je opcionalna: možete zadržati uplate u Bitcoin (bez naknade) ili ih konvertovati u CHF/EUR uz proviziju od 0,98%.



**Web dashboard**: Interface administrativni panel dostupan putem dashboard.lipa.swiss, omogućava vam pregled svih transakcija, filtriranje po periodu ili zaposlenom, i izvoz računovodstvenih podataka u CSV formatu. Dashboard se takođe može koristiti za generate web fakture sa QR kodovima direktno iz Interface.



## Kreiraj nalog



⚠️ **Važno** : Instalacija aplikacije zahteva prebivalište u Švajcarskoj. Ovo geografsko ograničenje primenjuje se zbog razloga usklađenosti sa propisima.



Da biste koristili Lipa za Biznis, prvo kreirajte namenski račun trgovca:





- Idite na lipa.swiss/for-business i preuzmite aplikaciju za vašu platformu (Android ili iOS)
- Instalirajte "lipa Wallet za poslovanje" sa Google Play-a ili App Store-a
- Prilikom prvog pokretanja unesite podatke o vašoj kompaniji: naziv firme, kontakt email, telefon i poslovni Address
- Email je glavni identifikator za pristup web kontrolnoj tabli.



Jednom kada je obrazac poslat, Lipa kreira vaš trgovački prostor. Može se izvršiti kratka ručna provera (pojednostavljeni KYC proces) pre konačne aktivacije. Aktivacija obično traje do 24 sata, ali vreme može varirati.



**Važno**: Nije potrebno povezivanje bankovnog računa za početak unovčavanja u Bitcoin. Bankovni podaci su potrebni samo ako se odlučite za automatsku konverziju u CHF.



## Instalacija i Interface



**Mobilna aplikacija**: Dostupna za Android/iOS pametne telefone i tablete. Interface je dizajniran za korišćenje na prodajnom mestu, sa lako čitljivim Elements i interakcijama ograničenim na ono što je neophodno. Dugme "Unovči uplatu" omogućava pristup ekranu za unos iznosa.



**Tehnički zahtevi**: Potrebna stabilna internet konekcija (minimum 3G) za obradu Lightning plaćanja u realnom vremenu.



**Web kontrolna tabla**: Besplatna kontrolna tabla dostupna putem dashboard.lipa.swiss. Sigurna email konekcija (magični link bez lozinke). Interface prikazuje sve vaše transakcije sa svim detaljima: datum, BTC/fiat iznos, Exchange kurs, zaposleni, itd. CSV izvoz za integraciju u računovodstvo.



![Dashboard Lipa Business](assets/fr/02.webp)



Kontrolna tabla se takođe može koristiti za generate veb fakture sa QR kodovima direktno iz Interface :



![Génération factures web](assets/fr/03.webp)



**Multi-terminal**: Izvorna podrška za više terminala unutar kompanije. Dodajte nove uređaje kreiranjem zaposlenih putem QR koda pozivnice. Svaki terminal je povezan sa istim trgovcem Wallet, uz održavanje mogućnosti praćenja po kasiru.



## Prihvati uplatu



Proces prikupljanja je sličan onom kod konvencionalne transakcije:



![Processus de paiement Lipa](assets/fr/01.webp)





- Unesite iznos**: Na ekranu za plaćanje unesite iznos u lokalnoj valuti (CHF ili EUR). Primer: za kafu od 4.50 CHF, unesite 4.50
- Invoice generacija** : Aplikacija trenutno konvertuje iznos u satoshije po trenutnom kursu i generiše Lightning Invoice u obliku QR koda
- Plaćanje kupca** : Kupac skenira QR kod svojim Wallet Lightning i potvrđuje plaćanje
- Potvrda** : Plaćanje je potvrđeno u roku od nekoliko sekundi, uz vizuelni prikaz uspeha



## Profesionalni alati



**Istorija i statistika**: Svaka uplata je zabeležena sa svim detaljima. Kontrolna tabla nudi pregled sa filterima po periodu ili zaposlenom, uporedivo sa klasičnim sistemom kase.



**Računovodstveni izvozi**: Izvoz podataka u CSV/Excel formatu sa svim potrebnim informacijama (Exchange stopa, transaction ID) za integraciju u vaš računovodstveni softver.



**Upravljanje zaposlenima**: Dodavanje/uklanjanje ovlašćenih korisnika putem kontrolne table. Svaki zaposleni dobija poseban pristup sa mogućnošću praćenja transakcija. Opoziv moguć u bilo kom trenutku.



**Backup**: Nekustodijalni trgovački račun sa 24 reči za oporavak radi čuvanja. Samo vlasnik glavnog Wallet treba da upravlja ovim backup-om - zaposleni nemaju pristup.



## Automatska konverzija CHF



**Dostupnost**: Usluga dostupna švajcarskim trgovcima sa plaćanjem u CHF (EUR u zavisnosti od dostupnosti).



**Konfiguracija**: Izbor između prijema u Bitcoin (besplatno) ili konverzije u fiat preko finansijskog partnera. Ako konvertujete u CHF, unesite IBAN za transfere.



**Naknade**: 0,98% provizije na konvertovane iznose (u poređenju sa 0% za uplate zadržane u BTC). Nema drugih skrivenih naknada ili pretplata.



**Kako funkcioniše** : Iznos koji primite odmah se prodaje po tržišnoj ceni i prenosi na vaš bankovni račun. Prenos se vrši u skladu sa standardnim rokovima vaše banke.



**Fleksibilnost**: Opcija reverzibilna u bilo kom trenutku u parametrima. Omogućava vam da testirate u režimu "fiat konverzije", a zatim pređete na 100% BTC kada budete sigurni.



## Sigurnost i poverljivost



**Non-custodial**: Zadržavate trajnu kontrolu nad primljenim sredstvima. Privatni/javni par ključeva se generiše tokom konfiguracije (otuda 24 reči fraza). Lipa ne čuva vaše privatne ključeve.



**Bezbednost zaposlenih**: Zaposleni mogu samo da kreiraju fakture, ne i da troše sredstva. U slučaju problema sa terminalom, vaša sredstva ostaju sigurna i možete opozvati pristup.



**Poverljivost korisnika**: pseudonimna Lightning plaćanja bez priloženih ličnih podataka. U suprotnosti sa kartičnim plaćanjima koja prolaze kroz centralizovane mreže.



**Autentifikacija**: Kontrolna tabla dostupna putem magičnog linka u emailu. Mobilna aplikacija zaštićena PIN-om ili biometrijom.



## Preporučeni slučajevi upotrebe





- Catering**: Barovi, restorani, kafići će prihvatiti dodatke u Bitcoin sa upravljanjem napojnicama
- Maloprodaja**: Prodavnice prehrambenih proizvoda, pekare za proširenje metoda plaćanja bez fiksnih troškova
- Nomadski prodavci**: kamioni sa hranom, pijace, festivali sa samo pametnim telefonom
- Događaji** : Privremeni štandovi sa gotovim rešenjima
- Services**: Konsultanti, zanatlije za jednokratno fakturisanje u Bitcoin



## Prednosti i ograničenja



### Pogodnosti




- Jednostavan Interface bez potrebnih tehničkih veština
- Rešenje bez starateljstva sa potpunom kontrolom nad sredstvima
- Upravljanje sa više zaposlenih uz mogućnost praćenja
- Izvoz knjigovodstva i veb kontrolna tabla uključeni
- Automatska opcija konverzije CHF za švajcarske trgovce
- Transparentne naknade: 0% Bitcoin, 0,98% konverzija fiat valuta
- Pozicioniranje kao inovativna kompanija u Bitcoin ekosistemu
- Zaštita od inflacije i devalvacije valute
- Sistem plaćanja otporan na cenzuru, decentralizovan



### Ograničenja




- Podrška za Lightning samo (bez Bitcoin On-Chain)
- Fiat konverzija trenutno ograničena na Švajcarsku
- Zahteva da kupci imaju kompatibilan Wallet Lightning
- Statični QR kodovi trenutno nisu dostupni
- Internet veza potrebna za sve transakcije



## Zaključak



Lipa for Business je pozicionirana kao kompletno rešenje za prihvatanje Bitcoin u prodavnici. Nije potrebna skupa infrastruktura (dovoljan je jednostavan pametni telefon), troškovi su niski i fiksni, a integracija u postojeće procese je laka.



Njegova nekustodijalna, privatnosti-prijateljska priroda, u kombinaciji sa profesionalnim alatima za upravljanje, čini ga privlačnim izborom za trgovce koji žele da usvoje Bitcoin, a da pritom zadrže jednostavnost i sigurnost.



## Resursi





- [Lipa za poslovanje zvanična veb stranica](https://lipa.swiss/en/for-business)
- [Dashboard web](https://dashboard.lipa.swiss)
- [Lipa Podrška za Poslovanje](https://help.lipa.swiss/business)
- [Lipa General Support](https://help.lipa.swiss/Wallet)
- [LinkedIn Lipa](https://www.linkedin.com/company/getlipa)
- [Twitter @lipa_btc](https://twitter.com/lipa_btc)