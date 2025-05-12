---
name: Bitwarden
description: Kako postaviti menadžer lozinki?
---
![cover](assets/cover.webp)


U digitalnom dobu, moramo upravljati mnoštvom online naloga koji pokrivaju različite aspekte naših svakodnevnih života, uključujući bankarstvo, finansijske platforme, emailove, skladištenje fajlova, zdravlje, administraciju, društvene mreže, video igre, itd.


Da bismo se autentifikovali na svakom od ovih naloga, koristimo identifikator, često email Address, u pratnji lozinke. Suočeni sa nemogućnošću pamćenja velikog broja jedinstvenih lozinki, neko bi mogao biti u iskušenju da ponovo koristi istu lozinku ili da malo modifikuje zajedničku osnovu kako bi je lako zapamtio. Međutim, ove prakse ozbiljno ugrožavaju sigurnost vaših naloga.


Prvi princip koji treba slediti za lozinke je da ih ne koristite ponovo. Svaki online nalog treba da bude zaštićen jedinstvenom lozinkom koja je potpuno različita od ostalih. Ovo je važno jer, ako napadač uspe da kompromituje jednu od vaših lozinki, ne želite da ima pristup svim vašim nalozima. Imati jedinstvenu lozinku za svaki nalog izoluje potencijalne napade i ograničava njihov obim. Na primer, ako koristite istu lozinku za platformu za video igre i za vaš email, i ta lozinka bude kompromitovana putem phishing sajta povezanog sa platformom za igre, napadač bi tada lako mogao da pristupi vašem emailu i preuzme kontrolu nad svim vašim drugim online nalozima.


Drugi suštinski princip je jačina lozinke. Ložinka se smatra jakom ako je teško probiti je metodom grube sile, odnosno pogoditi je kroz pokušaje i greške. To znači da vaše lozinke moraju biti što nasumičnije, duge i uključivati raznovrsne karaktere (mala slova, velika slova, brojeve i simbole).


Primena ova dva principa bezbednosti lozinki (jedinstvenost i robusnost) može biti teška u svakodnevnom životu, jer je gotovo nemoguće zapamtiti jedinstvenu, nasumičnu i jaku lozinku za sve naše naloge. Tu na scenu stupa menadžer lozinki.


Menadžer lozinki generiše i sigurno čuva jake lozinke, omogućavajući vam pristup svim vašim online nalozima bez potrebe da ih pojedinačno pamtite. Potrebno je da zapamtite samo jednu lozinku, glavnu lozinku, koja vam daje pristup svim sačuvanim lozinkama u menadžeru. Korišćenje menadžera lozinki poboljšava vašu online sigurnost jer sprečava ponovno korišćenje lozinki i sistematski generiše nasumične lozinke. Ali takođe pojednostavljuje vašu svakodnevnu upotrebu naloga centralizovanjem pristupa vašim osetljivim informacijama.

U ovom vodiču ćemo istražiti kako postaviti i koristiti menadžer lozinki da poboljšate svoju online sigurnost. Upoznaću vas sa Bitwarden-om, a u drugom vodiču ćemo razmotriti drugo rešenje pod nazivom KeePass.

https://planb.network/tutorials/computer-security/authentication/keepass-f8073bb7-5b4a-4664-9246-228e307be246

Upozorenje: Menadžer lozinki je odličan za čuvanje lozinki, ali **nikada ne bi trebalo da čuvate svoju Bitcoin Wallet's Mnemonic frazu u njemu!** Zapamtite, Mnemonic fraza treba da bude isključivo sačuvana u fizičkom formatu, kao što je papir ili metal.


## Uvod u Bitwarden


Bitwarden je menadžer lozinki pogodan za početnike i napredne korisnike. Nudi brojne prednosti. Prvenstveno, Bitwarden je rešenje za više platformi, što znači da ga možete koristiti kao mobilnu aplikaciju, veb aplikaciju, ekstenziju za pregledač i desktop softver.

![BITWARDEN](assets/notext/01.webp)

Bitwarden vam omogućava da sačuvate svoje lozinke online i sinhronizujete ih na svim svojim uređajima, uz osiguranje end-to-end enkripcije sa vašom glavnom lozinkom. Ovo vam omogućava, na primer, pristup vašim lozinkama i na računaru i na pametnom telefonu, uz sinhronizaciju između njih. Pošto su vaše lozinke enkriptovane, ostaju nedostupne bilo kome, uključujući Bitwarden, bez ključa za dekripciju koji je vaša glavna lozinka.


Štaviše, Bitwarden je open-source, što znači da softver može biti revidiran od strane nezavisnih stručnjaka. Što se tiče cena, Bitwarden nudi tri plana:


- Besplatna verzija koju ćemo istražiti u ovom vodiču. Iako je besplatna, pruža nivo sigurnosti ekvivalentan onom kod plaćenih verzija. Možete čuvati neograničen broj lozinki i sinhronizovati onoliko uređaja koliko želite;
- Premium verzija za $10 godišnje koja uključuje dodatne funkcije kao što su skladištenje datoteka, backup bankovne kartice, mogućnost postavljanja 2FA sa fizičkim sigurnosnim ključem i pristup TOTP 2FA autentifikaciji direktno sa Bitwarden-om;
- I porodični plan za 40 dolara godišnje koji proširuje pogodnosti premium verzije na šest različitih korisnika.

![BITWARDEN](assets/notext/02.webp)

Po mom mišljenju, ove cene su fer. Besplatna verzija je odlična opcija za početnike, a premium verzija nudi veoma dobru vrednost za novac u poređenju sa drugim menadžerima lozinki na tržištu, dok nudi više funkcija. Pored toga, činjenica da je Bitwarden open-source je velika prednost. Stoga, to je zanimljiv kompromis, posebno za početnike.

Još jedna funkcija Bitwardena je mogućnost samostalnog hostovanja vašeg menadžera lozinki ako posedujete, na primer, NAS kod kuće. Postavljanjem ove konfiguracije, vaše lozinke nisu smeštene na Bitwardenovim serverima, već na vašim sopstvenim serverima. Ovo vam daje potpunu kontrolu nad dostupnošću vaših lozinki. Međutim, ova opcija zahteva rigorozno upravljanje rezervnim kopijama kako bi se izbegao gubitak pristupa. Stoga je Bitwardenovo samostalno hostovanje više prilagođeno naprednim korisnicima, i o tome ćemo razgovarati u drugom vodiču.

## Kako kreirati Bitwarden nalog?


Posetite [Bitwarden vebsajt](https://bitwarden.com/) i kliknite na "*Get Started*".

![BITWARDEN](assets/notext/03.webp)

Počnite unosom svoje email adrese Address kao i svog imena ili nadimka.

![BITWARDEN](assets/notext/04.webp)

Zatim, treba da postavite svoju glavnu lozinku. Kao što smo videli u uvodu, ova lozinka je veoma važna jer vam omogućava pristup svim ostalim sačuvanim lozinkama u menadžeru. Ona predstavlja dva glavna rizika: gubitak i kompromitovanje. Ako izgubite pristup ovoj lozinci, više nećete moći da pristupite svim svojim akreditivima. Ako vaša lozinka bude ukradena, napadač će moći da pristupi svim vašim nalozima.


Da biste minimizirali rizik od gubitka, preporučujem da napravite fizičku rezervnu kopiju vaše glavne lozinke na papiru i da je čuvate na sigurnom mestu. Ako je moguće, Seal ovu rezervnu kopiju u sigurnoj koverti kako biste redovno osigurali da joj niko drugi nije pristupio.


Da biste sprečili kompromitovanje vaše glavne lozinke, ona mora biti izuzetno robusna. Trebalo bi da bude što duža, koristi širok spektar karaktera i bude izabrana nasumično. U 2024. godini, minimalne preporuke za sigurnu lozinku su 13 karaktera uključujući brojeve, mala i velika slova, kao i simbole, pod uslovom da je lozinka zaista nasumična. Međutim, preporučujem da se odlučite za lozinku od najmanje 20 karaktera, uključujući sve moguće tipove karaktera, kako biste osigurali njenu sigurnost na duži period.


Unesite svoju glavnu lozinku u predviđeno polje i potvrdite je u sledećem polju.

![BITWARDEN](assets/notext/05.webp)

Ako želite, možete dodati nagoveštaj za vašu glavnu lozinku. Međutim, savetujem da to ne činite, jer nagoveštaj ne pruža pouzdan metod oporavka u slučaju da izgubite lozinku i čak može biti koristan napadačima koji pokušavaju da pogode ili nasilno probiju vašu lozinku. Kao opšte pravilo, izbegavajte kreiranje javnih nagoveštaja koji bi mogli ugroziti sigurnost vaše glavne lozinke.

![BITWARDEN](assets/notext/06.webp)

Zatim kliknite na dugme "*Create an account*".

![BITWARDEN](assets/notext/07.webp)

Sada se možete prijaviti na svoj novi Bitwarden nalog. Unesite svoj email Address.

![BITWARDEN](assets/notext/08.webp)

Zatim unesite svoju glavnu lozinku.

![BITWARDEN](assets/notext/09.webp)

Sada ste na webu Interface vašeg menadžera lozinki.

![BITWARDEN](assets/notext/10.webp)

## Kako postaviti Bitwarden?


Da bismo počeli, potvrdićemo naš email Address. Kliknite na "*Pošalji Email*".

![BITWARDEN](assets/notext/11.webp)

Zatim kliknite na dugme primljeno putem e-pošte.

![BITWARDEN](assets/notext/12.webp)

Konačno, prijavite se ponovo.

![BITWARDEN](assets/notext/13.webp)

Prvo i najvažnije, toplo vam savetujem da postavite dvofaktorsku autentifikaciju (2FA) kako biste osigurali svoj menadžer lozinki. Imate izbor između korišćenja TOTP aplikacije ili fizičkog sigurnosnog ključa. Aktiviranjem 2FA, svaki put kada se prijavite na svoj Bitwarden nalog, bićete upitani ne samo za svoju glavnu lozinku već i za dokaz vašeg drugog faktora autentifikacije. Ovo je dodatni Layer nivo sigurnosti, posebno koristan u slučaju da je vaš papirni bekap glavne lozinke kompromitovan.


Ako niste sigurni kako da postavite i koristite ove 2FA uređaje, preporučujem da pratite ova 2 druga uputstva:


https://planb.network/tutorials/computer-security/authentication/authy-a76ab26b-71b0-473c-aa7c-c49153705eb7

https://planb.network/tutorials/computer-security/authentication/security-key-61438267-74db-4f1a-87e4-97c8e673533e

Da biste to uradili, idite na karticu "*Security*" u meniju "*Settings*".

![BITWARDEN](assets/notext/14.webp)

Zatim kliknite na karticu "*Dvofaktorska prijava*".

![BITWARDEN](assets/notext/15.webp)

Ovde možete izabrati metodu 2FA koju preferirate. Na primer, izabraću 2FA sa TOTP aplikacijom klikom na dugme "*Manage*".

![BITWARDEN](assets/notext/16.webp)

Potvrdite svoju glavnu lozinku.

![BITWARDEN](assets/notext/17.webp)

Zatim skenirajte QR kod sa vašom 2FA aplikacijom.

![BITWARDEN](assets/notext/18.webp)

Unesite 6-cifreni kod zabeležen u vašoj 2FA aplikaciji, zatim kliknite na dugme "*Uključi*". ![BITWARDEN](assets/notext/19.webp)

Dvofaktorska autentifikacija je uspešno postavljena na vašem nalogu.

![BITWARDEN](assets/notext/20.webp)

Sada, ako pokušate ponovo da se prijavite u svoj menadžer, prvo ćete morati da unesete svoju glavnu lozinku, a zatim dinamički 6-cifreni kod generisan od strane vaše 2FA aplikacije. Uverite se da uvek imate pristup ovom dinamičkom kodu; bez njega, nećete moći da povratite svoje lozinke.

![BITWARDEN](assets/notext/21.webp)

U postavkama, takođe imate opciju da prilagodite svog menadžera u kartici "*Preferences*". Ovde možete promeniti trajanje pre nego što se vaš menadžer automatski zaključa, kao i jezik i temu Interface.

![BITWARDEN](assets/notext/22.webp)

Preporučujem da prilagodite dužinu lozinki koje generiše Bitwarden. Podrazumevana dužina je postavljena na 14 karaktera, što može biti nedovoljno za optimalnu sigurnost. S obzirom da sada imate menadžer koji pamti sve vaše lozinke, možete iskoristiti tu prednost da koristite veoma jake lozinke.


Za ovo, idite na meni "*Generator*".

![BITWARDEN](assets/notext/23.webp)

Ovde možete povećati dužinu svojih lozinki na 40 i označiti polje za uključivanje simbola.

![BITWARDEN](assets/notext/24.webp)

## Kako obezbediti svoje naloge pomoću Bitwarden-a?


Sada kada je vaš menadžer lozinki konfigurisan, možete početi sa čuvanjem kredencijala za vaše online naloge. Da biste dodali novu stavku, kliknite direktno na dugme "*New item*" ili na dugme "*New*" koje se nalazi u gornjem desnom uglu ekrana, zatim na "*item*".

![BITWARDEN](assets/notext/25.webp)

U obrascu koji se otvori, započnite određivanjem prirode stavke koju treba sačuvati. Da biste sačuvali podatke za prijavu, izaberite opciju "*Login*" iz padajućeg menija.

![BITWARDEN](assets/notext/26.webp)

U polje "*Name*" unesite opisni naziv za vaše akreditive. Ovo će olakšati pretragu i organizaciju vaših lozinki, posebno ako ih imate veliki broj. Na primer, ako želite da sačuvate vaše akreditive za PlanB Network sajt, možete imenovati ovu stavku na način koji će je učiniti odmah prepoznatljivom tokom vaših budućih pretraga.

![BITWARDEN](assets/notext/27.webp)

Opcija "*Folder*" omogućava vam da klasifikujete svoje akreditive u foldere. Za sada, još nismo kreirali nijedan, ali pokazaću vam kako to da uradite kasnije.

![BITWARDEN](assets/notext/28.webp)

U polje "*Username*" unesite svoje korisničko ime, koje je obično vaša email adresa Address. ![BITWARDEN](assets/notext/29.webp)

Zatim, u polje "*Password*" možete uneti svoju lozinku. Međutim, toplo preporučujem da dozvolite Bitwarden generate da generiše dugu, nasumičnu i jedinstvenu lozinku za vas. Ovo osigurava da imate jaku lozinku. Da biste koristili ovu funkciju, kliknite na ikonu sa dvostrukom strelicom iznad polja koje treba popuniti.

![BITWARDEN](assets/notext/30.webp)

Možete videti da je vaša lozinka generisana.

![BITWARDEN](assets/notext/31.webp)

U polje "*URI 1*" možete uneti naziv domena veb-sajta.

![BITWARDEN](assets/notext/32.webp)

I konačno, u polju "*Beleške*", možete dodati dodatne detalje ako je potrebno.

![BITWARDEN](assets/notext/33.webp)

Kada završite sa popunjavanjem svih ovih polja, kliknite na dugme "*Sačuvaj*".

![BITWARDEN](assets/notext/34.webp)

Vaš identifikator se sada pojavljuje u vašem Bitwarden menadžeru.

![BITWARDEN](assets/notext/35.webp)

Klikom na to možete pristupiti njegovim detaljima i izmeniti ih.

![BITWARDEN](assets/notext/36.webp)

Klikom na tri male tačke s desne strane, imate brz pristup kopiranju lozinke ili identifikatora.

![BITWARDEN](assets/notext/37.webp)

Čestitamo, uspešno ste sačuvali svoju prvu lozinku u menadžeru! Ako želite bolje organizovati svoje identifikatore, možete kreirati specifične fascikle. Da biste to uradili, kliknite na dugme "*New*" koje se nalazi u gornjem desnom uglu ekrana, a zatim izaberite "*Folder*".

![BITWARDEN](assets/notext/38.webp)

Unesite ime za vašu fasciklu.

![BITWARDEN](assets/notext/39.webp)

Zatim kliknite na "*Sačuvaj*".

![BITWARDEN](assets/notext/40.webp)

Vaša fascikla se sada pojavljuje u vašem menadžeru.

![BITWARDEN](assets/notext/41.webp)

Možete dodeliti fasciklu identifikatoru prilikom njegovog kreiranja, kao što smo to ranije uradili, ili izmenom postojećeg identifikatora. Na primer, klikom na moj identifikator za PlanB Network, zatim mogu odabrati da ga klasifikujem u fasciklu "*Bitcoin*".

![BITWARDEN](assets/notext/42.webp)

Na ovaj način, možete strukturirati svoj menadžer lozinki kako biste lakše pronašli svoje identifikatore. Možete ih organizovati u fascikle kao što su lično, profesionalno, banke, mejlovi, društvene mreže, pretplate, kupovina, administracija, striming, skladištenje, putovanja, zdravlje, itd.

Ako više volite da koristite samo veb verziju Bitwardena, potpuno je moguće ostati pri tome. Preporučujem da dodate vaš menadžer lozinki u omiljene stavke vašeg pregledača radi lakšeg pristupa i izbegavanja rizika od fišinga. Međutim, Bitwarden takođe nudi čitav niz klijenata koji vam omogućavaju da koristite vaš menadžer na različitim uređajima i da pojednostavite njegovo svakodnevno korišćenje. Konkretno, nude mobilnu aplikaciju, ekstenziju za pregledač i desktop softver. Hajde da vidimo kako ih zajedno podesiti.


![BITWARDEN](assets/notext/43.webp)


## Kako koristiti Bitwarden ekstenziju za pregledač?


Prvo, možete postaviti ekstenziju za pregledač ako želite. Ova ekstenzija radi kao smanjena verzija vašeg menadžera i nudi vam mogućnost automatskog čuvanja novih lozinki, generate sugestija za sigurne lozinke, i automatsko popunjavanje vaših kredencijala na stranicama za prijavu na web sajtove.


Svakodnevna upotreba ovog dodatka je izuzetno praktična, ali može otvoriti i nove vektore napada. Neki stručnjaci za sajber bezbednost, stoga, savetuju protiv korišćenja dodataka za pregledače za upravljanje lozinkama. Međutim, ako odlučite da koristite Bitwarden dodatak, evo kako da nastavite:


Počnite tako što ćete otići na [zvaničnu stranicu za preuzimanje Bitwarden-a](https://bitwarden.com/download/#downloads-web-browser).


![BITWARDEN](assets/notext/44.webp)


Izaberite svoj pregledač sa liste koja je pružena. Za ovaj primer, koristim Firefox, tako da sam preusmeren na zvanično Bitwarden proširenje u Firefox Add-ons prodavnici. Procedura je prilično slična za druge pregledače.


![BITWARDEN](assets/notext/45.webp)


Kliknite na dugme "*Dodaj u Firefox*".


![BITWARDEN](assets/notext/46.webp)


Zatim možete prikačiti Bitwarden na traku ekstenzija za lakši pristup. Kliknite na ekstenziju da se prijavite.


![BITWARDEN](assets/notext/47.webp)


Unesite svoj email Address.


![BITWARDEN](assets/notext/48.webp)


Zatim vaša glavna lozinka.


![BITWARDEN](assets/notext/49.webp)


I na kraju, unesite 6-cifreni kod iz vaše aplikacije za autentifikaciju.


![BITWARDEN](assets/notext/50.webp)


Sada ste povezani sa svojim Bitwarden menadžerom putem ekstenzije za pregledač.


![BITWARDEN](assets/notext/51.webp)


Na primer, ako se vratim na sajt PlanB Network i pokušam da se prijavim na svoj nalog, možete videti da Bitwarden ekstenzija integrisana u pregledač prepoznaje polja za prijavu i automatski mi nudi da izaberem identifikator koji sam prethodno sačuvao.


![BITWARDEN](assets/notext/52.webp)

Ako izaberem ovaj identifikator, Bitwarden popunjava polja za prijavu umesto mene. Ova funkcija ekstenzije omogućava brzo povezivanje sa veb sajtovima, bez potrebe za kopiranjem i lepljenjem akreditiva iz Bitwarden veb aplikacije ili softvera.

![BITWARDEN](assets/notext/53.webp)

Ekstenzija je takođe dizajnirana da detektuje kreiranje novih naloga. Na primer, kada kreirate novi nalog na PlanB Network, Bitwarden automatski predlaže čuvanje novog identifikatora.

![BITWARDEN](assets/notext/54.webp)

Klikom na ovaj predlog koji se pojavljuje, ekstenzija se otvara. Omogućava mi da unesem detalje novog identifikatora i generate jaku, jedinstvenu lozinku.

![BITWARDEN](assets/notext/55.webp)

Nakon što popunite informacije i kliknete na "*Save*", ekstenzija čuva akreditive.

![BITWARDEN](assets/notext/56.webp)

Zatim ekstenzija automatski popunjava naše akreditive u odgovarajuća polja na vebsajtu.

![BITWARDEN](assets/notext/57.webp)

## Kako koristiti Bitwarden softver?


Da biste instalirali Bitwarden desktop softver, počnite tako što ćete otići na [stranicu za preuzimanje](https://bitwarden.com/download/#downloads-desktop). Izaberite i preuzmite verziju koja odgovara vašem operativnom sistemu.

![BITWARDEN](assets/notext/58.webp)

Kada se preuzimanje završi, nastavite sa instalacijom softvera na vašem računaru. Prilikom prvog pokretanja Bitwarden softvera, biće potrebno da unesete svoje akreditive kako biste otključali vaš menadžer lozinki.

![BITWARDEN](assets/notext/59.webp)

Zatim ćete stići na početnu stranicu vašeg menadžera. Interface je skoro isti kao na veb aplikaciji.

![BITWARDEN](assets/notext/60.webp)

## Kako koristiti Bitwarden aplikaciju?


Da biste pristupili svojim lozinkama sa telefona, možete instalirati Bitwarden mobilnu aplikaciju. Počnite tako što ćete otići na [stranicu za preuzimanje](https://bitwarden.com/download/#downloads-mobile) i koristiti svoj pametni telefon da skenirate QR kod koji odgovara vašem operativnom sistemu.

![BITWARDEN](assets/notext/61.webp)

Preuzmite i instalirajte zvaničnu Bitwarden mobilnu aplikaciju. Prilikom prvog otvaranja aplikacije unesite svoje akreditive kako biste otključali pristup svom menadžeru lozinki.

![BITWARDEN](assets/notext/62.webp)

Kada se povežete, moći ćete da konsultujete i upravljate svim svojim lozinkama direktno iz aplikacije.

![BITWARDEN](assets/notext/63.webp)

Da biste poboljšali sigurnost vaše aplikacije, savetujem vam da uđete u postavke i aktivirate zaštitu PIN-om. Ovo će dodati dodatni Layer nivo sigurnosti u slučaju gubitka ili krađe vašeg telefona.

![BITWARDEN](assets/notext/64.webp)

## Kako napraviti rezervnu kopiju Bitwardena?

Da biste osigurali da nikada ne izgubite pristup svojim lozinkama, čak i u slučaju gubitka glavne lozinke ili katastrofe koja utiče na Bitwarden servere, savetujem vam da redovno vršite šifrovanu rezervnu kopiju svog menadžera na eksternom mediju.


Ideja je da šifrujete sve vaše Bitwarden akreditive sa lozinkom koja je različita od vaše glavne lozinke i da sačuvate ovu šifrovanu rezervnu kopiju na USB memoriji ili Hard disku koji čuvate kod kuće, na primer. Zatim možete čuvati fizičku kopiju lozinke za dešifrovanje na odvojenoj lokaciji od mesta gde je medijum za rezervnu kopiju uskladišten. Na primer, možete čuvati USB memoriju kod kuće i poveriti fizičku kopiju lozinke za šifrovanje pouzdanom prijatelju.


Ova metoda osigurava da čak i ako vaš medij za bekap bude ukraden, vaši podaci će ostati nedostupni bez lozinke za dešifrovanje. Slično, vaš prijatelj neće moći pristupiti vašim podacima bez fizičkog medija.


Međutim, u slučaju problema, možete koristiti lozinku i eksterni medijum da ponovo dobijete pristup svojim akreditivima, nezavisno od Bitwardena. Dakle, čak i ako bi Bitwardenovi serveri bili uništeni, i dalje biste imali mogućnost da povratite svoje lozinke.


Stoga vam savetujem da redovno pravite ove rezervne kopije kako bi uvek uključivale vaše najnovije akreditive. Da ne biste uznemiravali svog prijatelja, koji ima kopiju lozinke za šifrovanje, sa svakom novom rezervnom kopijom, možete sačuvati ovu lozinku u svom menadžeru lozinki. Ovo nije zamišljeno kao rezervna kopija, pošto vaš prijatelj već ima fizičku kopiju, već da bi se pojednostavili vaši budući postupci izvoza.


Da biste nastavili sa izvozom, prilično je jednostavno: idite na odeljak "*Alati*" vašeg Bitwarden menadžera, zatim izaberite "*Izvezi trezor*".

![BITWARDEN](assets/notext/65.webp)

Za format, izaberite "*.json (Encrypted)*".

![BITWARDEN](assets/notext/66.webp)

Zatim izaberite opciju "*Zaštićeno lozinkom*".

![BITWARDEN](assets/notext/67.webp)

Ovde je važno izabrati jaku, jedinstvenu i nasumično generisanu lozinku za šifrovanje bekapa. Ovo osigurava da, čak i u slučaju krađe vašeg šifrovanog bekapa, napadač neće moći da ga dešifruje metodom grube sile.

![BITWARDEN](assets/notext/68.webp)

Kliknite na "*Potvrdi format*" i unesite svoju glavnu lozinku da biste nastavili sa izvozom.

![BITWARDEN](assets/notext/69.webp)

Kada je izvoz završen, pronaći ćete svoju šifrovanu rezervnu kopiju u preuzimanjima. Prenesite je na siguran eksterni uređaj za skladištenje, kao što je USB stik ili Hard drajv. Ponavljajte ovu operaciju periodično u zavisnosti od vaše upotrebe. Na primer, možete obnavljati rezervnu kopiju svake nedelje ili svakog meseca, u skladu sa vašim potrebama.