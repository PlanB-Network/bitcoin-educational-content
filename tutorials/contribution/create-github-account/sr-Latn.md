---
name: GitHub nalog
description: Kako kreirati svoj nalog na GitHub-u?
---

![cover](assets/cover.webp)


Misija Plan ₿ je da obezbedi vrhunske obrazovne resurse o Bitcoin, dostupne na što više jezika. Sav sadržaj objavljen na sajtu je otvorenog koda i hostovan na GitHub-u, pružajući svakome priliku da doprinese obogaćivanju platforme. Doprinosi mogu imati različite oblike: ispravljanje i lektura postojećih tekstova, prevodi na druge jezike, ažuriranje informacija ili kreiranje novih tutorijala koji još nisu dostupni na našem sajtu.


Ako želite da doprinesete Plan ₿ Network, biće vam potrebno da koristite Git i GitHub, tako da, ako su vam ovi alati nepoznati ili vam njihovo funkcionisanje deluje nejasno, ne paničite, ovaj članak je za vas! Zajedno ćemo pregledati osnove Gita i GitHuba, kao i povezani tehnički žargon, kako bismo vam omogućili da ih efikasno koristite nakon toga.


## Šta je Git?


Git je sistem za kontrolu verzija, posebno dizajniran za upravljanje softverskim projektima. Kreiran 2005. godine od strane Linusa Torvaldsa, Git je brzo postao standard u industriji razvoja softvera za kontrolu verzija. Ali šta to tačno znači?

![git](assets/11.webp)

U svojoj suštini, Git omogućava programerima da prate promene napravljene u izvornom kodu projekta tokom vremena. To znači da sa svakom promenom u kodu, Git beleži novu verziju projekta. Ako dođe do greške ili ako eksperimentalna funkcija ne radi kako se očekuje, moguće je vratiti se na prethodno stanje koda, poput vremenske mašine, ali za fajlove.


Jedna od ključnih karakteristika Gita je upravljanje granama. Grana je vrsta paralelne linije na kojoj programeri mogu raditi nezavisno od ostatka projekta. Ovo u velikoj meri olakšava dodavanje novih funkcionalnosti ili ispravljanje grešaka bez ometanja glavnog koda. Kada se izmene testiraju i potvrde, mogu se spojiti sa glavnom granom.


Jedna od osobenosti Gita je njegova sposobnost da radi na distribuiran način. Svaki programer ima potpunu kopiju projekta na svom Hard disku računara, što im omogućava da rade offline i kasnije spoje promene kada je dostupna Internet konekcija. Ovo smanjuje rizik od konflikata i omogućava više programera da istovremeno rade na istom projektu bez međusobnog ometanja.

U početku je Git bio prvenstveno dizajniran za projekte razvoja softvera. Međutim, može se koristiti i za upravljanje projektima pisanja sadržaja. Umesto da sarađujemo na kodu, sarađujemo na tekstu. I upravo je ovaj metod Plan ₿ Network usvojio za upravljanje svojim sadržajem! Git olakšava saradnju na pisanju kurseva i tutorijala, jer omogućava precizno praćenje promena, efikasno upravljanje verzijama, a takođe omogućava pregled i poboljšanje sadržaja od strane drugih saradnika.


## Šta je GitHub?


GitHub je platforma za upravljanje izvornim kodom i hosting zasnovana na sistemu za kontrolu verzija Git o kojem smo upravo razgovarali. Pokrenut 2008. godine, GitHub je brzo stekao popularnost i postao ključna referenca za programere širom sveta. Ali kako se GitHub razlikuje od Git-a i zašto je toliko ključan u našem metodu proizvodnje sadržaja?

![github](assets/12.webp)

Prvo, važno je razumeti da je GitHub izgrađen na Gitu (o kojem smo razgovarali u prethodnom odeljku). Dok je Git alat koji prati promene u kodu, GitHub je onlajn servis koji hostuje, deli i upravlja ovim kodom.


Zamislite Git kao neku vrstu dnevnika koji svaki programer koristi na svom računaru da zabeleži sve promene u svom projektu. GitHub, s druge strane, je kao javna biblioteka gde se svi ovi dnevnici mogu deliti, upoređivati i kombinovati.


Osnovna razlika između Git-a i GitHub-a leži u njihovoj funkciji: Git je alat koji svaki programer lokalno koristi za upravljanje verzijama svog koda, dok je GitHub onlajn platforma koja hostuje te verzije i olakšava saradnju.


GitHub je mnogo više od usluge za hosting koda. To je platforma za saradnju koja omogućava programerima da rade zajedno efikasno. I zaista, Plan ₿ Network koristi ovu platformu da hostuje ne samo sav kod koji pokreće vebsajt već i, što nas interesuje, sav sadržaj (tutoriali, obuke, resursi...).


## Neki tehnički termini


Na Gitu i GitHubu, naići ćete na komande i funkcije čija imena mogu delovati složeno. U ovom poslednjem delu, daću nekoliko jednostavnih definicija kako biste razumeli tehničke termine na koje možete naići prilikom korišćenja Gita i GitHuba:



- Dohvati poreklo:** Komanda koja preuzima nedavne informacije i promene iz udaljenog repozitorijuma bez njihovog spajanja sa vašim lokalnim radom. Ažurira vaš lokalni repozitorijum sa novim granama i komitima prisutnim u udaljenom repozitorijumu.



- Povuci poreklo:** Komanda koja preuzima ažuriranja iz udaljenog repozitorijuma i odmah ih integriše u vašu lokalnu granu kako bi je sinhronizovala. Ovo kombinuje korake preuzimanja i spajanja u jednu komandu.
- Sinhronizacija Fork:** Funkcija na GitHub-u koja vam omogućava da ažurirate svoj Fork projekta sa najnovijim promenama iz izvornog repozitorijuma. Ovo osigurava da vaša kopija projekta ostane ažurirana sa glavnim razvojem.
- Push origin:** Komanda koja se koristi za slanje vaših lokalnih izmena u udaljeni repozitorijum.



- Zahtev za povlačenje:** Zahtev koji šalje saradnik kako bi naznačio da je poslao izmene na granu u udaljenom repozitorijumu i želi da te izmene budu pregledane i potencijalno spojene u glavnu granu repozitorijuma.



- Commit:** Čuvanje vaših izmena. Commit je kao trenutna snimka vašeg rada u datom trenutku, što omogućava čuvanje istorije izmena. Svaki commit uključuje opisnu poruku koja objašnjava šta je izmenjeno.



- Grana:** Paralelna verzija repozitorijuma, koja vam omogućava da radite na izmenama bez uticaja na glavnu granu (često nazvanu "main" ili "master"). Grane olakšavaju razvoj novih funkcionalnosti i ispravku grešaka bez rizika od narušavanja stabilnog koda.



- Spoji:** Spajanje se sastoji od integrisanja izmena iz jedne grane u drugu. Koristi se, na primer, za dodavanje izmena iz radne grane na glavnu granu, što omogućava dodavanje različitih doprinosa.



- Fork:** Forkovanje repozitorijuma znači kreiranje kopije tog repozitorijuma na vašem GitHub nalogu, što vam omogućava da radite na projektu bez uticaja na originalni repozitorijum. Fork može ili krenuti svojim putem i postati drugačiji projekat od originalnog, ili može redovno sinhronizovati sa originalnim projektom kako bi doprineo njemu.



- Kloniranje:** Kloniranje repozitorijuma znači pravljenje lokalne kopije na vašem računaru, što vam omogućava pristup svim fajlovima i istoriji. Ovo vam omogućava da radite na projektu direktno lokalno.



- Repozitorijum:** Prostor za skladištenje projekta na GitHub-u. Repozitorijum sadrži sve datoteke projekta kao i istoriju svih promena koje su napravljene na njemu. To je osnova za skladištenje i saradnju na GitHub-u.



- Problem:** Alat za praćenje zadataka i grešaka na GitHub-u. Problemi omogućavaju prijavljivanje problema, predlaganje poboljšanja ili diskusiju o novim funkcijama. Svaki problem može biti dodeljen, označen i komentarisati.


Ova lista očigledno nije iscrpna. Postoji mnogo drugih tehničkih termina specifičnih za Git i GitHub. Međutim, oni koji su ovde pomenuti su glavni koje ćete često sretati.


Nakon što pročitate ovaj članak, moguće je da vam neki aspekti Gita i GitHuba i dalje nisu jasni, pa vas ohrabrujem da počnete sami koristiti ove alate. Praksa je često najbolji način da shvatite kako mašina radi! A za početak, možete otkriti ova 2 druga vodiča:


## Kako kreirati GitHub nalog


Ako želite da doprinesete PlanB mreži, biće vam potreban GitHub nalog. U ovom vodiču, vodićemo vas korak po korak kako da kreirate svoj nalog, podesite ga i pravilno osigurate.



- Idi na [https://github.com/signup](https://github.com/signup).
- Unesite svoj email Address, zatim kliknite na Green `Nastavi` dugme:

![github](assets/1.webp)


- Izaberite jaku lozinku, zatim kliknite na Green dugme `Continue`:

![github](assets/12.webp)


- Dalje, izaberite svoje korisničko ime. Možete otkriti svoj pravi identitet ili koristiti pseudonim. Zatim, kliknite na Green dugme `Nastavi`:

![github](assets/3.webp)


- Dovršite Captcha:

![github](assets/4.webp)


- E-mail sa potvrdnim kodom biće poslat vama; potrebno je da ga unesete kako biste završili kreiranje svog naloga:

![github](assets/5.webp)


- Popunite pitanja ako želite da vas GitHub usmeri ka određenim alatima, ili kliknite na `preskoči personalizaciju` da preskočite:

![github](assets/6.webp)


- Izaberite besplatan plan klikom na dugme `Nastavi besplatno`:

![github](assets/7.webp)


- Bićete preusmereni na vašu kontrolnu tablu.
- Ako želite, možete prilagoditi svoj nalog klikom na svoju profilnu sliku koja se nalazi u gornjem desnom uglu ekrana, a zatim pristupite meniju `Settings`:

![github](assets/8.webp)


- U ovom odeljku imate opciju da dodate novu profilnu sliku, izaberete ime, prilagodite svoju biografiju ili dodate link ka vašem ličnom sajtu:

![github](assets/9.webp)


- Takođe preporučujem da posetite meni `Lozinka i autentifikacija` kako biste postavili autentifikaciju u dva koraka:

![github](assets/10.webp)