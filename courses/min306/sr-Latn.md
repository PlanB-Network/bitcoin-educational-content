---
name: Bitaxe Open Source Mining Majstorstvo
goal: Savladajte kompletan Bitaxe ekosistem, od sklapanja hardvera do napredne prilagodbe i optimizacije performansi.
objectives: 

  - Razumeti filozofiju open source Bitcoin mining hardvera
  - Izgradnja uređaja Bitaxe mining od nule
  - Konfigurišite i optimizujte mining softver uključujući AxeOS i Public Pool
  - Implementirajte napredne optimizacije performansi uključujući overklokovanje i benchmarking

---

# Vaš Bitaxe Mining Vodič


Dobrodošli na sveobuhvatan Bitaxe kurs, gde ćete savladati revolucionarni open source Bitcoin mining hardver koji demokratizuje pristup mining tehnologiji. Ovaj kurs vas vodi od razumevanja filozofskih osnova decentralizovanog mining do naprednih tehnika prilagođavanja hardvera i optimizacije performansi.


Projekat Bitaxe predstavlja promenu paradigme u Bitcoin mining, razbijajući monopol vlasničkih proizvođača ASIC pružanjem potpuno otvorenih dizajna, firmvera i softvera. Kroz ova praktična poglavlja, steći ćete praktične veštine u sklapanju hardvera, konfiguraciji softvera, dizajnu PCB-a i optimizaciji performansi.


Nije potrebno prethodno iskustvo sa mining, iako će osnovno znanje elektronike i poznavanje GitHub-a biti od pomoći. Kurs će vas transformisati iz radoznalog posmatrača u sposobnog graditelja i saradnika na Bitaxe projektu.


+++


# Uvod


<partId>6b3cd9f0-0063-40f0-a7bb-00a48f330d88</partId>


## Pregled kursa


<chapterId>1fac9579-0e1c-48e3-9bc5-e7a2960018c8</chapterId>


Dobrodošli na kurs MIN 306 _**Bitaxe Open Source Mining Mastery**_, sveobuhvatno putovanje u svet Bitaxe mining. Ovaj kurs je dizajniran za one koji žele da razumeju, izgrade i optimizuju svoj Bitaxe mining hardver dok istražuju filozofske i tehničke osnove koje čine ovaj projekat jedinstvenim unutar Bitcoin ekosistema.


### Razumevanje Bitaxe


Prvi deo postavlja osnovne temelje: otkrićete poreklo Bitaxe projekta, njegovu evoluciju i vrednosti decentralizacije i transparentnosti koje ga definišu. Naučićete šta je zapravo Bitaxe, kako se razlikuje od vlasničkih ASIC-ova i gde pronaći resurse zajednice za produbljivanje vašeg znanja. Ovaj deo pruža kontekst potreban za razumevanje zašto Bitaxe predstavlja prekretnicu u istoriji Bitcoin mining.


### Softver i Operacije


Drugi deo se fokusira na softversko okruženje, sa detaljnom prezentacijom *AxeOS*-a: operativnog sistema otvorenog koda dizajniranog specifično za Bitaxe uređaje. Naučićete njegove glavne karakteristike i kako da konfigurišete i komunicirate sa svojim uređajem kako biste započeli svoju prvu mining operaciju.


### Zajednica i saradnja


Treći deo ističe kolaborativni aspekt projekta. Istražićete filozofiju otvorenog koda primenjenu na razvoj hardvera i softvera Bitaxe-a. Kroz praktične vežbe, naučićete kako da direktno doprinesete izvornom kodu, a takođe ćete otkriti _Public Pool_, platformu zajednice za udruživanje računarske snage. Takođe ćete naučiti kako da ga instalirate na Umbrel čvor za lokalnu i suverenu integraciju.


### Sklapanje i rešavanje problema sa hardverom


U četvrtom delu, uronićete u sam hardver. Naučićete kako da identifikujete alate potrebne za sklapanje Bitaxe-a, rešavanje problema sa lemljenjem i izvođenje kompletne dijagnostike koristeći *AxeOS* i USB alate. Ovaj deo naglašava praktičnu vežbu i duboko razumevanje kako hardverske i softverske komponente međusobno deluju.


### Napredna prilagođavanja


Peti deo je posvećen prilagođavanju. Naučićete kako da modifikujete PCB (štampana ploča), kreirate fabričku datoteku i koristite _Bitaxe Web Flasher_. Ovaj deo je namenjen onima koji žele da idu dalje od jednostavne montaže i zaista dizajniraju prilagođene verzije sopstvenog uređaja.


### Optimizacija performansi


Konačno, šesta sekcija pokriva napredne tehnike optimizacije. Naučićete kako da benchmark-ujete vaš Bitaxe kako biste procenili njegovu performansu i kako da ga efikasno overclock-ujete. Ove veštine će vam pomoći da maksimalno iskoristite vaš hardver, poštujući njegova fizička ograničenja.


Kao i kod svakog kursa na Plan ₿ Akademiji, poslednji deo uključuje evaluaciju osmišljenu da ojača vaše znanje.


Uronite se u ovu tehničku avanturu — budućnost Bitcoin mining je u vašim rukama!


# Razumevanje Bitaxe

<partId>ba1cb4ea-6a77-54fd-916c-57285c8c2418</partId>


## Istorija

<chapterId>73d928e5-72f0-5c17-a7a6-8b6ece7f9a30</chapterId>

:::video id=67d2529a-b7cb-4804-b02c-e56c12c9e66e:::

Projekat Bitaxe predstavlja revolucionarni pomak u razvoju Bitcoin mining hardvera, donoseći principe otvorenog koda u industriju kojom dominiraju vlasnička rešenja. Ova edukativna serija istražuje sveobuhvatnu istoriju, tehničke inovacije i evoluciju vođenu zajednicom Bitaxe-a, pružajući uvide u to kako se vizija jednog inženjera transformisala u napredni ekosistem decentralizovanog mining hardvera. Kroz ispitivanje porekla projekta, izazova i dostignuća, stičemo dragoceno razumevanje kako tehničkih složenosti razvoja ASIC, tako i moći saradnje otvorenog koda u Bitcoin prostoru.


### Priča o poreklu: Od otkrića Puta svile do vizije Solar Mining


Skot, osnivač Bitaxe-a, započeo je svoje putovanje u Bitcoin na studentskoj zabavi gde je prvi put saznao za Bitcoin kroz nekoga ko je kupovao predmete na Silk Road-u. Ovo početno izlaganje Bitcoin po ceni od približno $20 po novčiću izazvalo je radoznalost koja će kasnije evoluirati u revolucionarni projekat mining. Tehnička osnova za njegov budući rad postavljena je tokom njegovog vremena na univerzitetu, gde je imao pristup opsežnim FPGA resursima u laboratorijskom okruženju. Radeći zajedno sa svojim nadzornikom, Skot je počeo da eksperimentiše sa open source FPGA bitstream-ovima za Bitcoin mining, u početku sa skromnim ciljem da mining dovoljno Bitcoin da kupe picu za svoju kancelariju.


Prelazak sa akademskih eksperimenata na ozbiljan razvoj dogodio se godinama kasnije kada je Skot radio na solarnim prolazima za prikupljanje podataka na daljinu u Africi. Ovo profesionalno iskustvo sa solarnim sistemima pokrenulo je spoznaju da bi Bitcoin mining ASIC-ovi, kao uređaji koji su fundamentalno niskonaponski DC, savršeno odgovarali solarnim panelima. Koncept je delovao prirodno i elegantno. Međutim, kada je Skot počeo istraživati postojeća rešenja, otkrio je značajnu prazninu na tržištu: za razliku od ranih dana Bitcoin mining kada su FPGA dizajni bili otvoreno dostupni, pojava ASIC-ova pomerila je industriju ka potpuno vlasničkim, zatvorenim rešenjima.


Nedostatak otvorenog koda za mining hardver postao je izvor frustracije za Skota, posebno s obzirom na njegovo iskustvo u razvoju softvera otvorenog koda i njegovo uverenje da bi priroda otvorenog koda Bitcoin trebala biti proširena na njegovu mining infrastrukturu. Ova filozofska usklađenost s principima otvorenog koda, u kombinaciji s tehničkim izazovom reverznog inženjeringa vlasničkih ASIC dizajna, postavila je temelje za ono što će postati Bitaxe projekat. Početna vizija bila je ambiciozna, ali praktična: stvoriti solarni Bitcoin rudar koji bi mogao raditi samostalno bez potrebe za posebnim računarom za kontrolu, čineći ga pogodnim za postavljanje na udaljenim lokacijama ispod solarnih panela.


### Tehnički Izazovi i Proboji u Obrnutom Inženjeringu


Razvoj Bitaxe-a zahtevao je prevazilaženje značajnih tehničkih prepreka, prvenstveno usredsređenih na potpuni nedostatak dokumentacije o Bitmainovim ASIC čipovima. Skotov pristup ovom izazovu pokazao je odlučnost i domišljatost potrebnu za uspešno reverzno inženjerstvo. Bez pristupa zvaničnim tehničkim listovima ili tehničkim specifikacijama, pribegao je ispitivanju čipova pod mikroskopima, merenju razmaka pinova klještima i čak skeniranju čipova kako bi odredio njihove tačne zahteve za otisak. Ovaj mukotrpan proces rezultirao je višestrukim neuspelim prototipovima, pri čemu prve dve iteracije "dnevnog rudara" nisu funkcionisale ispravno zbog netačnih proračuna otiska.


Proboj je došao sa trećom iteracijom u maju 2022. godine, kada je Skot uspešno kreirao radni dizajn sa dva čipa koristeći BM1387 čipove izvađene iz Antminer S9 jedinica. Ovo dostignuće označilo je rođenje imena Bitaxe, inspirisanog konceptom krampova za Bitcoin mining. Uspeh ovog dizajna potvrdio je pristup reverznog inženjeringa i pokazao da nezavisni programeri mogu kreirati funkcionalni mining hardver bez podrške proizvođača. Međutim, tehnički izazovi su se proširili izvan povezivanja čipova i uključivali su složen dizajn napajanja, jer su ASIC-ovi zahtevali preciznu regulaciju napona pri visokim strujama, često radeći na naponima niskim kao 0.6 volti dok su povlačili značajnu amperažu.


Razvoj firmvera predstavio je još jedan sloj složenosti, jer je projekat zahtevao kreiranje mining softvera koji bi mogao direktno da radi na ESP32 mikrokontroleru umesto da se oslanja na spoljne računare koji pokreću softver kao što je CGMiner. Ovaj samostalni pristup bio je ključan za Skotovu viziju primenljivih, nezavisnih mining jedinica. Kombinacija reverznog inženjeringa hardvera i razvoja ugrađenog firmvera stvorila je sveobuhvatan tehnički izazov koji je zahtevao stručnost u više disciplina, od elektrotehničkog inženjeringa i dizajna PCB-a do ugrađenog programiranja i mrežnih protokola.


### Formiranje zajednice i saradnja na otvorenom kodu


Transformacija Bitaxea iz solo projekta u uspešnu zajedničku inicijativu predstavlja jedan od najznačajnijih aspekata njegovog uspeha. U početku, Skotovi pokušaji da izazove interesovanje za generate putem Bitcoin foruma i društvenih mreža naišli su na ograničen odziv i povremeni skepticizam. Proboj je nastao kada su članovi zajednice poput SirVapesAlot prepoznali potencijal otvorenog koda mining i osnovali Discord server Open Source Miners United (OSMU). Ova platforma je obezbedila kolaborativno okruženje neophodno za procvat projekta, privlačeći saradnike iz različitih sredina koji su delili zajednički interes za demokratizaciju Bitcoin mining tehnologije.


Model razvoja vođen zajednicom pokazao se izuzetno efikasnim, sa ključnim saradnicima kao što su johnny9 i Ben koji su se pojavili da reše specifične tehničke izazove. Johnny9-ova stručnost u razvoju firmvera rešila je kritične probleme implementacije softvera, dok su Benove veštine u razvoju front-end-a kreirale intuitivni AxeOS kontrolni panel koji je pojednostavio konfiguraciju i nadzor uređaja. Benovi dodatni doprinosi uključivali su uspostavljanje proizvodnih kapaciteta i kreiranje Public Pool-a, open source mining bazena optimizovanog za Bitaxe uređaje. Ovaj kolaborativni pristup pokazao je kako principi otvorenog koda mogu ubrzati razvoj izvan onoga što bi bilo koji pojedinačni saradnik mogao postići sam.


OSMU zajednica je takođe negovala inkluzivno okruženje gde su novopridošli mogli učiti i doprinositi bez obzira na njihovo početno tehničko znanje. Benovo sopstveno putovanje od početnika u lemljenju do velikog proizvođača oslikava ovaj pristup dobrodošlice razvoju veština. Posvećenost zajednice obrazovanju i međusobnoj podršci stvorila je vrlinski ciklus gde su iskusni članovi mentorisali novopridošle, koji su zatim i sami postajali saradnici. Ovaj model se pokazao ključnim za širenje projekta izvan njegovog prvobitnog obima i uspostavljanje održivog ekosistema za kontinuiranu inovaciju i rast.


### Vizija za Decentralizovani Mining i Budući Uticaj


Skotova dugoročna vizija za Bitaxe seže daleko izvan stvaranja još jednog mining uređaja: to je fundamentalna transformacija Bitcoin pejzaža mining. Ambiciozni cilj proizvodnje milion rudara sa jednim terahašom stvorio bi eksahaš distribuirane mining snage, što predstavlja značajan korak ka decentralizaciji mining. Ova vizija se bavi kritičnim pitanjima centralizacije mining, gde bi veliki bazeni i industrijske operacije potencijalno mogli biti podložni pritisku vlade ili regulatornom zahvatu. Distribucijom mining snage među bezbrojnim kućnim rudarima, mreža postaje otpornija i usklađena sa decentralizovanim principima Bitcoin.


Ekonomski model koji podržava ovu viziju oslanja se na jedinstvene karakteristike kućnog mining, gde su troškovi infrastrukture suštinski nula i rudari mogu da rade uz minimalni nadzor. Za razliku od industrijskih mining operacija koje zahtevaju masivne kapitalne investicije u objekte, energetsku infrastrukturu i sisteme hlađenja, kućni rudari mogu jednostavno priključiti uređaje u postojeće električne utičnice i internet konekcije. Ovaj pristup bi teoretski mogao doneti značajnu stopu heširanja online bez tradicionalnih prepreka za ulazak koje karakterišu velike mining operacije.


Uspeh projekta je već počeo da utiče na širi ekosistem Bitcoin mining, sa potencijalom da inspiriše druge proizvođače da prihvate modele razvoja otvorenog koda. Finansijska održivost koju su pokazali proizvođači Bitaxe dokazuje da hardver otvorenog koda može biti komercijalno uspešan, a da pritom zadrži transparentnost i uključenost zajednice. Kako projekat nastavlja da se razvija sa novim integracijama čipova, poboljšanim dizajnima i proširenim proizvodnim partnerstvima, on služi kao dokaz koncepta kako Bitcoin mining može da se vrati svojim decentralizovanim korenima dok prihvata modernu ASIC tehnologiju. Krajnji cilj prevazilazi puku distribuciju hash rate-a i uključuje obrazovni uticaj, dovodeći više ljudi u direktan kontakt sa osnovnim mining procesom Bitcoin i podstičući dublje razumevanje modela bezbednosti mreže.


## Šta je Bitaxe?

<chapterId>6a56af56-35ce-51af-999b-4bc7305e6464</chapterId>

:::video id=12b26c7a-74b1-4ea9-afc0-e3ef90cf5837:::

### Pregled hardvera i mogućnosti


Ekosistem Bitaxe obuhvata više iteracija hardvera, od kojih je svaka dizajnirana da optimizuje različite aspekte mining iskustva, dok zadržava osnovnu filozofiju otvorenog koda. Ovi uređaji služe ne samo kao funkcionalni mining hardver, već i kao edukativni alati koji omogućavaju korisnicima da razumeju složeni odnos između ASIC čipova, mikrokontrolera i Bitcoin mining procesa. Razumevanje Bitaxe-ove dizajnerske filozofije i tehničke implementacije pruža dragocene uvide u to kako moderni mining hardver funkcioniše na nivou komponenti i sistema.



### Bitaxe Max, Prva generacija implementacije


Bitaxe Max predstavlja osnovnu implementaciju Bitaxe koncepta, koristeći BM1397 ASIC čip koji je originalno razvijen od strane Bitmain-a za njihovu S17 mining seriju. Ova integracija čipa pokazuje kako open-source hardver može ponovo koristiti postojeću ASIC tehnologiju za kreiranje pristupačnih mining rešenja. Bitaxe Max isporučuje procenjeni hash rate između 300 do 400 gigahaša po sekundi, pozicionirajući ga kao edukativnu i eksperimentalnu mining platformu, a ne kao komercijalno rešenje.


Integracija BM1397 čipa u Bitaxe Max zahtevala je pažljivo razmatranje upravljanja energijom, termalne kontrole i komunikacionih protokola. Dizajn ploče prilagođava se specifičnim zahtevima ovog ASIC, dok obezbeđuje potrebne prateće sklopove za stabilan rad. Ova implementacija pokazuje kako razvoj open-source hardvera može iskoristiti postojeću poluprovodničku tehnologiju za kreiranje novih aplikacija i mogućnosti učenja unutar mining zajednice.


### Bitaxe Ultra, Advanced Chip Technology


Bitaxe Ultra predstavlja evoluciju Bitaxe platforme, uključujući napredniji BM1366 ASIC čip iz Bitmainove S19 serije. Ova novija čip tehnologija donosi poboljšanu efikasnost i performanse Bitaxe platformi, dok zadržava istu osnovnu filozofiju dizajna. Nadogradnja na BM1366 čip pokazuje prilagodljivost platforme i posvećenost zajednice u uključivanju tehnoloških napredaka u open-source mining rešenja.


Prelazak sa čipa BM1397 na BM1366 zahtevao je modifikacije sistema za isporuku energije na ploči, upravljanje toplotom i kontrolne algoritme. Ove promene ilustruju iterativnu prirodu razvoja hardvera i važnost održavanja kompatibilnosti uz unapređenje performansi. Implementacija Bitaxe Ultra korisnicima pruža pristup novijoj ASIC tehnologiji, dok zadržava obrazovnu i eksperimentalnu prirodu platforme.


### Mikrokontroler i komunikacioni sistemi


U srcu svakog Bitaxe uređaja nalazi se ESP mikrokontroler koji služi kao primarni interfejs između korisnika i ASIC čipa. Ovaj mikrokontroler pokreće specijalizovani softver razvijen od strane zajednice Open Source Miners United (OSMU), omogućavajući preciznu kontrolu nad operativnim parametrima ASIC. Komunikacija između mikrokontrolera i ASIC odvija se putem pažljivo dizajniranih serijskih komunikacionih linija koje su direktno urezane na štampanoj ploči kao vidljivi tragovi.


Uloga mikrokontrolera se proteže dalje od jednostavne ASIC kontrole: uključuje upravljanje napajanjem, praćenje temperature i funkcije korisničkog interfejsa. Kroz integrisani ekran, korisnici mogu pratiti ključne operativne parametre kao što su temperatura, hash stopa, IP adresa i druge relevantne mining statistike. Ovaj sistem povratnih informacija u realnom vremenu pruža dragocene uvide u performanse uređaja i pomaže korisnicima da optimizuju svoje mining operacije dok uče o ponašanju osnovnog hardvera.


### Upravljanje energijom i bezbednosni aspekti


Platforma Bitaxe radi na strogoj potrebi za napajanjem od 5 volti, što čini pravilan izbor napajanja ključnim za dugovečnost i bezbednost uređaja. Sistem za upravljanje napajanjem na Bitaxe pločama uključuje sofisticiranu elektroniku dizajniranu za regulisanje isporuke napona do ASIC čipa, dok prati potrošnju energije u različitim operativnim režimima. Ova sposobnost upravljanja napajanjem omogućava uređaju da efikasno radi u rasponu unutrašnjih frekvencija i napona, obično trošeći između 5 i 25 vati u zavisnosti od konfiguracije.


Razumevanje zahteva za napajanje postaje ključno kada se uzme u obzir da nepravilna primena napona može trajno oštetiti uređaj. Odnos između frekvencije, napona, potrošnje energije i hash rate-a pokazuje osnovne principe rada ASIC koji se primenjuju na sav mining hardver. Korisnici mogu eksperimentisati sa različitim postavkama napajanja kako bi razumeli kompromise u efikasnosti koji su svojstveni mining operacijama, stičući praktično iskustvo sa konceptima koji se primenjuju na veće mining implementacije.


### Solo Mining Fokus i Učešće u Mreži


Bitaxe platforma specifično cilja solo mining aplikacije, gde pojedinačni rudari pokušavaju da reše Bitcoin blokove samostalno, umesto da učestvuju u velikim mining bazenima. Iako hash stopa Bitaxe uređaja čini uspešno otkrivanje blokova statistički malo verovatnim, ovaj pristup služi važnim obrazovnim i filozofskim svrhama unutar Bitcoin zajednice. Solo mining sa Bitaxe uređajima pomaže korisnicima da razumeju osnovne mehanike Bitcoin proof-of-work sistema dok doprinose decentralizaciji mreže.


Naglasak na solo mining odražava posvećenost OSMU zajednice podsticanju individualnog učešća u bezbednosnom modelu Bitcoin. Omogućavanjem pristupačnog hardvera koji može raditi nezavisno, Bitaxe platforma omogućava korisnicima da pokreću sopstvene mining operacije bez oslanjanja na infrastrukturu bazena. Ovaj pristup podstiče dublje razumevanje konsenzusnog mehanizma Bitcoin dok podržava decentralizovanu prirodu mreže kroz povećanu raznolikost rudara.


### Evolucija hardvera i unapređenja proizvodnje


Platforma Bitaxe nastavlja da se razvija kroz povratne informacije zajednice i optimizaciju proizvodnje, pri čemu novije verzije uključuju poboljšanja koja unapređuju mogućnost proizvodnje i korisničko iskustvo. Ažuriranja verzija obično se fokusiraju na efikasnost proizvodnje, a ne na osnovne promene performansi, osiguravajući da postojeći korisnici ne budu pod pritiskom zastarevanja. Funkcije kao što su prelazak sa micro-USB na USB-C konektore i poboljšani sistemi za povezivanje napajanja odražavaju pažnju zajednice na praktična poboljšanja upotrebljivosti.


Ovaj evolucioni pristup pokazuje prednosti razvoja hardvera otvorenog koda, gde doprinos zajednice pokreće postepena poboljšanja koja koriste svim korisnicima. Filozofija "ako hešira, hešira" naglašava fokus platforme na funkcionalnost umesto na stalna unapređenja, podstičući korisnike da održavaju i koriste svoje uređaje umesto da teže najnovijim verzijama. Ovaj pristup podržava održive hardverske prakse dok održava obrazovnu vrednost Bitaxe-a.


## Gde mogu saznati više?

<chapterId>706f2fff-fa1c-5d8e-b14c-ece6e42c016f</chapterId>

:::video id=90088397-3a16-485f-bbd2-89cdbb844e4a:::

Projekat Bitaxe predstavlja sveobuhvatnu open-source mining inicijativu koja se proteže daleko izvan jednog uređaja. Razumevanje gde pronaći pouzdane informacije, tehničke resurse i podršku zajednice je ključno za svakoga ko želi da se uključi u ovaj ekosistem. Ovo poglavlje pruža kompletan vodič kroz osnovne platforme i resurse koji čine temelj zajednice Bitaxe i Open Source Miners United (OSMU).


### Bitaxe.org, Centralni Centar


Vebsajt Bitaxe.org služi kao primarni portal za sve informacije i resurse povezane sa projektom. Ova centralizovana platforma funkcioniše kao vaša prva tačka reference kad god treba da saznate više o Bitaxe uređajima ili istražite druge projekte unutar OSMU zajednice. Dizajn vebsajta daje prioritet pristupačnosti i organizaciji, predstavljajući posetiocima pažljivo odabrane linkove koji povezuju sa raznim specijalizovanim resursima širom ekosistema.


Važnost ovog centralnog čvorišta ne može se prenaglasiti, jer eliminiše konfuziju koja često prati decentralizovane open-source projekte. Umesto da pretražuju više platformi ili se oslanjaju na potencijalno zastarele informacije iz nezvaničnih izvora, korisnici mogu verovati Bitaxe.org-u da će obezbediti aktuelne, verifikovane linkove ka svim ključnim resursima. Ovaj pristup osigurava da i novajlije i iskusni članovi zajednice mogu efikasno pronaći specifične informacije koje su im potrebne za njihove projekte.


### Tehnički resursi i razvojni materijali


GitHub repozitorijum sa datotekama dizajna hardvera predstavlja jedan od najvrednijih resursa za svakoga ko je zainteresovan za razumevanje ili izradu Bitaxe uređaja. Ovaj javni repozitorijum sadrži sveobuhvatnu dokumentaciju koja pokriva svaki aspekt procesa dizajna hardvera, od početnih koncepata do konačnih specifikacija za proizvodnju. Repozitorijum uključuje detaljne slike, ciljeve projekta, opise funkcija i objašnjenja ugrađenih komponenti koja pružaju i tehničku dubinu i praktične smernice.


Za one koji su zainteresovani za proizvodnju sopstvenih uređaja, repozitorijum uključuje specifične dokumentacione fajlove kao što je building.md, koji pruža uputstva korak po korak za ceo proces proizvodnje. Ova dokumentacija pokriva softverske alate potrebne za dizajn PCB-a, procedure za slanje fajlova proizvođačima, i korake uključene u prijem i validaciju proizvedenih PCB-ova. Ovaj nivo detalja osigurava da pojedinci ili male organizacije mogu uspešno navigirati procesom proizvodnje bez obimnog prethodnog iskustva u proizvodnji hardvera.


ESP-Miner skladište služi kao centralna lokacija za sav kod i dokumentaciju vezanu za firmware. Ovo GitHub skladište sadrži svaki red koda napisan za Bitaxe firmware, zajedno sa sveobuhvatnom dokumentacijom koja objašnjava sistemske zahteve, hardverske specifikacije i opcije konfiguracije. Struktura skladišta je dizajnirana da odgovara i korisnicima koji preferiraju unapred kompajlirane binarne fajlove i programerima koji žele da izgrade firmware iz izvornog koda.


Dokumentacija unutar ovog repozitorijuma uključuje detaljne sekcije o hardverskim zahtevima, opcijama pre-konfiguracije i preporučenim vrednostima za različita podešavanja. Ove informacije su neprocenjive za korisnike koji žele da prilagode svoje uređaje ili reše specifične probleme. Pored toga, repozitorijum uključuje informacije o novijim razvojnim dostignućima, kao što je integracija sa Raspberry Pi, osiguravajući da dokumentacija ostane aktuelna sa stalnom evolucijom projekta.


### Alati za upravljanje i održavanje uređaja


Bitaxe web flasher predstavlja praktično rešenje za održavanje i ažuriranje uređaja. Ovaj alat zasnovan na vebu omogućava korisnicima da flešuju firmver na svojim uređajima bez potrebe za specijalizovanim softverom ili složenim komandnim procedurama. Flasher podržava više varijanti uređaja, uključujući Bitaxe Ultra sa različitim verzijama portova i starije modele Bitaxe Max. Korisnici mogu birati između ažuriranja postojećeg firmvera putem veb interfejsa ili izvođenja potpunih fabričkih resetovanja koristeći USB veze.


Ovaj alat rešava jedan od najčešćih izazova sa kojima se suočavaju entuzijasti za hardver: održavanje i ažuriranje firmvera uređaja. Pružajući korisnički prijatan veb interfejs, flasher eliminiše mnoge tehničke prepreke koje bi inače mogle sprečiti korisnike da svoje uređaje održavaju aktuelnim sa najnovijim izdanjima firmvera. Dizajn alata prioritizuje jednostavnost dok održava fleksibilnost potrebnu za različite konfiguracije uređaja i scenarije ažuriranja.


### Platforme zajednice i kanali komunikacije


Discord server predstavlja srce interakcije u realnom vremenu i podrške unutar Bitaxe ekosistema. Organizacija servera odražava raznolike interese i potrebe članova zajednice, sa pažljivo strukturisanim kanalima koji olakšavaju fokusirane diskusije o specifičnim temama. Novi članovi prolaze kroz proces verifikacije koji zahteva čitanje i prihvatanje pravila zajednice, osiguravajući da svi učesnici razumeju očekivanja za poštovanje i produktivnu interakciju.


Struktura kanala servera uključuje opšte diskusione oblasti koje pokrivaju teme kao što su integracija solarne energije, mining bazeni i diskusije vezane za Bitcoin. Više specijalizovani delovi fokusiraju se na specifične uređaje, uključujući posvećene kanale za Bitaxe Ultra, Hex i Supra varijante. Kanal za firmver pruža fokusiran prostor za tehničke diskusije o razvoju softvera i rešavanju problema, dok kanal za zvanična izdanja osigurava da članovi zajednice dobiju pravovremena obaveštenja o novim razvojnim događajima.


Takođe sadrži oblast za pretplatnike koja pruža dodatne pogodnosti za članove zajednice koji odluče da finansijski podrže projekat. Ovaj pristup sa nivoima omogućava zajednici da ponudi poboljšane usluge dok održava otvoren pristup osnovnim informacijama i kanalima podrške. Kanal za pomoć služi kao posvećen prostor za rešavanje problema i tehničku pomoć, osiguravajući da korisnici mogu dobiti brzu podršku kada naiđu na poteškoće.



Open Source Miners United wiki (osmu.wiki) pruža sveobuhvatnu dokumentaciju koja dopunjuje diskusije u realnom vremenu koje se odvijaju na Discord-u. Za razliku od platformi zasnovanih na četu, wiki nudi strukturiranu, pretraživu dokumentaciju koja pokriva sve aspekte Bitaxe projekta i srodnih inicijativa. Način na koji je organizovan odražava strukturu projekta, sa posebnim odeljcima za različite serije uređaja i sveobuhvatnim vodičima za postavljanje.


Otvorena priroda vikija omogućava članovima zajednice da direktno doprinose dokumentaciji. Korisnici mogu uređivati stranice, podnositi ispravke i dodavati nove informacije putem GitHub integracije, osiguravajući da baza znanja ostane aktuelna i transparentna. Ovaj kolaborativni pristup koristi kolektivnu stručnost zajednice, dok održava kontrolu kvaliteta kroz proces pregleda za podnete izmene.


Wiki uključuje praktične resurse kao što su PDF vodiči za postavljanje koji pružaju uputstva korak po korak za konfiguraciju i korišćenje uređaja. Ovi vodiči služe kao vredni referentni materijali za nove korisnike i iskusne članove zajednice koji trebaju brz pristup specifičnim procedurama ili detaljima konfiguracije.


### Informacije o kupovini i dobavljačima


Bitaxe legit lista adresira kritičnu potrebu unutar zajednice otvorenog hardvera: identifikovanje pouzdanih prodavaca i izbegavanje prevarantskih prodavaca. Ova kurirana lista uključuje verifikovane preprodavce i proizvođače koji ispunjavaju specifične kriterijume za legitimnost i podršku zajednice. Svaka stavka uključuje direktne linkove ka sajtovima prodavaca, regionalne informacije i opise kompanija koji pomažu korisnicima da donesu informisane odluke o kupovini.


Važno je da lista pokazuje da li svaki dobavljač doprinosi OSMU zajednici, bilo finansijski ili kroz druge oblike podrške. Ova transparentnost pomaže članovima zajednice da razumeju koji dobavljači aktivno podržavaju razvoj i održivost projekta. Lista takođe služi kao zaštitna mera protiv uobičajenih prevara, kao što su neovlašćene prednarudžbine za neizdate proizvode, koje su istorijski izazivale probleme unutar zajednice.


Naglasak na nepartnerskim linkovima pokazuje posvećenost zajednice pružanju nepristrasnih preporuka prodavaca. Korisnici mogu verovati da su preporuke zasnovane na legitimnosti prodavaca i doprinosu zajednice, a ne na finansijskim podsticajima, što osigurava da odluke o kupovini podržavaju kako individualne potrebe, tako i održivost zajednice.



# Softver i Operacije

<partId>04b302a9-42ba-5ad4-834c-6979950c2948</partId>


## Šta je AxeOS?

<chapterId>a0cdf10d-e007-58e2-a17b-b588fd393b5e</chapterId>

:::video id=de7bcbf2-f9ac-4057-ad40-29dc223b4798:::

AxeOS je firmver i veb interfejs za Bitaxe mining uređaje, pružajući korisnicima potpunu kontrolu i mogućnosti praćenja putem intuitivne kontrolne table zasnovane na pregledaču. Ovaj sistem pretvara složen zadatak upravljanja ASIC u pristupačno iskustvo, omogućavajući rudarima da prate performanse, podešavaju postavke i upravljaju više uređaja sa jednog interfejsa. Razumevanje AxeOS-a je ključno za maksimiziranje potencijala vašeg Bitaxe uređaja i održavanje optimalnog rada mining.


### Pregled kontrolne table i osnovne metrike


Nadzorna tabla AxeOS služi kao vaš primarni prozor u performanse vašeg Bitaxe uređaja, prikazujući ključne mining metrike u organizovanom, realnom vremenu. Kada pristupite IP adresi vašeg Bitaxe uređaja, odmah vam se prikazuju četiri ključna pokazatelja performansi koji definišu trenutno stanje vašeg mining rada. Prikaz brzine heširanja pokazuje stvarnu brzinu računanja koju vaš ASIC čip proizvodi dok obrađuje trenutni blok šablon, pružajući trenutne povratne informacije o osnovnoj funkcionalnosti vašeg uređaja.


Pored stope heširanja, brojač deonica prati svako validno rešenje koje vaš Bitaxe uređaj pošalje u mining bazen, povećavajući se sa svakim uspešnim podnošenjem i služeći kao direktna mera doprinosa vašeg uređaja naporima mining bazena. Metrička efikasnost pruža ključni uvid u performanse snage vašeg uređaja izračunavanjem odnosa stope heširanja prema potrošnji energije, pomažući vam da optimizujete profitabilnost vašeg poslovanja. Indikator najbolje težine čuva zapis o najtežoj deonici koju je vaš uređaj ikada pronašao, održavajući ovo dostignuće čak i kroz ponovna pokretanja i ažuriranja, resetujući se samo kada izvršite potpuno fabričko flešovanje.


Sistem proširivog menija na kontrolnoj tabli, kojim upravlja dugme za prebacivanje, omogućava pristup svim funkcionalnostima AxeOS-a uz održavanje čistog interfejsa. Grafikon trenutne stope heširanja predstavlja jednu od njegovih najvrednijih karakteristika, prikazujući podatke o performansama u realnom vremenu koji postaju tačniji i informativniji što duže održavate svoju sesiju. Sekcije za napajanje, toplotu i performanse pružaju sveobuhvatno praćenje operativnog statusa vašeg uređaja, uključujući upozorenja o ulaznom naponu koja vas obaveštavaju o potencijalnim problemima sa napajanjem, dok osiguravaju nastavak rada unutar sigurnih parametara.


### Napredno praćenje i informacije o sistemu


Mogućnosti praćenja AxeOS-a daleko prevazilaze osnovno praćenje hash stope, pružajući detaljan uvid u svaki aspekt rada vašeg Bitaxe uređaja. Sekcija za napajanje prikazuje izračunatu potrošnju energije dobijenu iz integrisanih kola na ploči, merenja ulaznog napona sa vaše veze za napajanje i tražene nivoe napona ASIC. Kada dođe do pada napona, AxeOS odmah prikazuje obaveštenja o upozorenju, iako to obično ne utiče na rad mining i jednostavno ukazuje na potencijalne mogućnosti optimizacije napajanja.


Praćenje temperature fokusira se na termalno upravljanje čipom ASIC, sa očitavanjima uzetim sa strateških lokacija na uređaju kako bi se obezbedili tačni termalni podaci sa odgovarajućim ofsetima za tačnost na nivou čipa. Prikazi frekvencije i napona nude povratne informacije u realnom vremenu o vašim parametrima podešavanja ASIC, pri čemu izmereni napon predstavlja najtačnije dostupno očitavanje, uzeto direktno na lokaciji čipa ASIC. Ova preciznost omogućava fino podešavanje performansi dok se održavaju bezbedni uslovi rada.


Odeljak o statusu veze pruža trenutni uvid u konfiguraciju vašeg mining bazena, prikazujući trenutni stratum URL, port i korisničku identifikaciju. Za uređaje povezane na javne bazene, AxeOS generiše praktične brze linkove koji vas direktno vode do web interfejsa vašeg bazena, gde možete pristupiti detaljnim statistikama, listama uređaja i istorijskim podacima o performansama. Ova integracija pojednostavljuje proces praćenja povezivanjem informacija na nivou uređaja i bazena u besprekornom toku rada.


### Upravljanje rojem i kontrola više uređaja


Funkcionalnost Swarm predstavlja AxeOS rešenje za složenost upravljanja više Bitaxe uređaja preko mreže, eliminišući potrebu za pamćenjem i navigacijom do brojnih IP adresa. Ovaj centralizovani sistem upravljanja omogućava vam da dodate uređaje jednostavnim unosom njihovih IP adresa, automatski detektujući aktivne Bitaxe minere i uključujući ih u jedinstvenu kontrolnu tablu. Kada se konfiguriše, Swarm pruža sveobuhvatnu kontrolu nad celokupnim mining radom sa jednog interfejsa.


Kroz Swarm interfejs, možete izvršavati ključne zadatke upravljanja na više uređaja istovremeno ili pojedinačno, uključujući promene konfiguracije pool-a, restartovanje uređaja, podešavanje frekvencije i praćenje performansi. Ovaj centralizovani pristup značajno smanjuje administrativni teret upravljanja velikim mining operacijama, dok osigurava doslednu konfiguraciju na svim uređajima. Sistem održava identitet pojedinačnih uređaja dok pruža kolektivne mogućnosti upravljanja, postižući optimalnu ravnotežu između detaljne kontrole i operativne efikasnosti.


Swarm kontrolna tabla prikazuje svaki upravljani uređaj sa njegovim trenutnim statusom, performansama i kontrolama za brzi pristup, omogućavajući brzi odgovor na probleme sa performansama ili promene konfiguracije. Ova funkcionalnost je posebno vredna za rudare koji upravljaju sa više uređaja na različitim lokacijama ili one koji često podešavaju mining parametre na osnovu tržišnih uslova ili performansi bazena.


### Upravljanje konfiguracijom i sistemska podešavanja


Odjeljak Postavke u AxeOS-u pruža sveobuhvatnu kontrolu nad svakim podesivim aspektom vašeg Bitaxe uređaja, od mrežne povezanosti do mining parametara i optimizacije hardvera. Konfiguracija mreže započinje postavljanjem Wi-Fi-ja, gde navodite ime i lozinku vaše mreže, pri čemu AxeOS preporučuje imena mreža u jednoj reči bez razmaka kako bi se osigurala pouzdana povezanost. Sistem upravlja celokupnim procesom bežične konfiguracije, omogućavajući daljinsko upravljanje i nadzor.


Mining konfiguracija se fokusira na postavke stratuma, gde navodite URL izabranog mining pool-a bez prefiksa protokola ili brojeva portova, koji se obrađuju u posebnim poljima. Polje za korisnika stratuma prilagođava se različitim zahtevima pool-a, podržavajući i Bitcoin adrese za solo mining i korisnička imena za pool mining, sa mogućnošću dodavanja identifikatora uređaja za rad sa više uređaja. Nedavno dodata funkcionalnost lozinke stratuma podržava pool-ove koji zahtevaju autentifikaciju, iako većina javnih pool-ova funkcioniše bez ovog zahteva.


Optimizacija hardvera putem podešavanja frekvencije i napona jezgra predstavlja najmoćniju mogućnost podešavanja performansi AxeOS-a. U zavisnosti od verzije vašeg uređaja i pregledača, ova podešavanja se mogu pojaviti kao padajući meniji sa unapred podešenim konfiguracijama ili kao otvorena polja koja omogućavaju unos prilagođenih vrednosti. Podrazumevana podešavanja frekvencije od 485 MHz i napona jezgra od 1200 mV obezbeđuju stabilan rad za početno testiranje, dok napredni korisnici mogu optimizovati ove parametre za maksimalne performanse ili efikasnost na osnovu svojih specifičnih zahteva i uslova rada.


### Održavanje sistema i napredne funkcije


AxeOS uključuje sofisticirane mogućnosti održavanja sistema dizajnirane da vaš Bitaxe uređaj radi na vrhunskim performansama, dok pruža dijagnostičke informacije za rešavanje problema i optimizaciju. Sistem ažuriranja pojednostavljuje upravljanje firmverom prikazivanjem najnovijeg dostupnog izdanja direktno u interfejsu i pružanjem direktnih linkova za preuzimanje zvaničnih firmverskih datoteka. Ova integracija eliminiše potrebu za ručnim navigiranjem po GitHub repozitorijumima ili upravljanjem preuzimanjima datoteka, pojednostavljujući proces ažuriranja na nekoliko klikova.


Interfejs za ažuriranje prihvata pravilno imenovane firmware datoteke, konkretno esp-miner.bin i www.bin, osiguravajući kompatibilnost i sprečavajući greške pri instalaciji. Za korisnike koji imaju poteškoća sa standardnim procesom ažuriranja, AxeOS pruža reference na sveobuhvatne procedure fabričkog flešovanja koje mogu vratiti uređaje na originalnu funkcionalnost. Ovaj dvostruki pristup omogućava i rutinska ažuriranja i scenarije oporavka.


Sistem za beleženje pruža uvid u rad uređaja u realnom vremenu, prikazujući detaljne informacije o modelima čipova ASIC, vremenu rada sistema, statusu Wi-Fi povezivanja, dostupnoj memoriji, verzijama firmvera i revizijama ploča. Ovi logovi su neprocenjivi za programere i napredne korisnike koji žele da razumeju ponašanje uređaja, dijagnostikuju probleme ili optimizuju performanse. Pregledač logova u realnom vremenu prikazuje operativne podatke uživo, uključujući obradu nonce-a, proračune težine i parametre podnošenja mining, nudeći neviđenu vidljivost u sam proces mining.


Dodatne funkcije sistema uključuju kontrolu orijentacije ekrana za uređaje korišćene u prilagođenim kućištima, inverziju polariteta ventilatora za specijalizovane konfiguracije hlađenja i automatsku kontrolu ventilatora koja prilagođava hlađenje na osnovu temperature ASIC. Ručna kontrola brzine ventilatora omogućava precizno upravljanje hlađenjem kada automatski sistemi ne ispunjavaju specifične zahteve. Sve promene konfiguracije zahtevaju čuvanje i ponovno pokretanje uređaja da bi stupile na snagu, čime se osigurava stabilan rad i sprečavaju delimična stanja konfiguracije koja bi mogla uticati na performanse mining.



# Zajednica i saradnja

<partId>eed1ce48-6752-5744-91f7-91e4e20ff6b2</partId>


## Pregled doprinosa otvorenom kodu

<chapterId>715d026e-cebc-536e-a34e-728f5653b999</chapterId>

:::video id=7298ba19-28d2-4a7c-ac0b-44ad0c4770cf:::

### GitHub i njegova uloga u razvoju softvera


GitHub predstavlja fundamentalnu promenu u načinu na koji se upravlja i deli softverskim razvojnim projektima širom globalne programerske zajednice. Kao platforma zasnovana na oblaku koja hostuje softverske razvojne projekte koristeći Git, distribuirani sistem za kontrolu verzija, GitHub omogućava programerima da besprekorno sarađuju na projektima bez obzira na njihovu fizičku lokaciju. Platforma služi kao tehnički alat i društvena mreža za programere, omogućavajući im da prate promene, spajaju ažuriranja, održavaju različite verzije svog koda i doprinose inicijativama otvorenog koda kao što je BitX projekat od Open Source Miners United.


Moć GitHub-a leži u njegovoj sposobnosti da pojednostavi složen proces kolaborativnog razvoja. Kada više programera radi na istom projektu, GitHub obezbeđuje infrastrukturu za upravljanje doprinosima, pregled promena, rešavanje problema projekta i održavanje sveobuhvatne dokumentacije. Ovaj kolaborativni pristup učinio je GitHub ključnom komponentom modernih tokova rada u razvoju softvera, transformišući način na koji i individualni programeri i velike organizacije pristupaju upravljanju projektima i deljenju koda.


### Navigacija kroz GitHub Interface i Struktura Repozitorijuma


Razumevanje GitHub interfejsa počinje prepoznavanjem ključnih elemenata koji čine bilo koju stranicu repozitorijuma. Gornja navigaciona traka sadrži nekoliko kritičnih sekcija uključujući Code, Issues, Pull Requests, Discussions, Actions, Projects, Security i Insights. Svaka sekcija služi specifičnoj svrsi u ekosistemu upravljanja projektima, pri čemu sekcija Code prikazuje stvarne fajlove i foldere koji čine projekat.


Sama struktura repozitorijuma odražava organizacioni pristup održavalaca projekta. Neki repozitorijumi sadrže samo jednu datoteku, možda jednostavan shell skript, dok drugi, poput BitX hardverskog projekta, sadrže brojne datoteke organizovane u direktorijume i poddirektorijume. Naziv repozitorijuma se ističe i služi kao identifikator i kratak opis svrhe projekta. Osnovni interaktivni elementi uključuju dugme Watch za primanje obaveštenja o ažuriranjima repozitorijuma, dugme Fork za kreiranje ličnih kopija repozitorijuma, i dugme Star koje funkcioniše kao sistem podrške zajednice sličan funkciji "palac gore".


Odeljak "O projektu" pruža ključne informacije o projektu u sažetom formatu, uključujući opis u jednoj rečenici, informacije o licenci i ključne detalje o projektu. Za BitX projekat, ovaj odeljak ga identifikuje kao "open source ASIC Bitcoin miner hardver" i navodi GPL 3.0 licencu. Razumevanje licenci je posebno važno jer GitHub funkcioniše kao open-source platforma gde su javni repozitorijumi dostupni celoj zajednici, ali se sadržaj može koristiti i distribuirati samo u skladu sa pravilima usklađenosti svake licence.


### Rad sa granama i verzijama projekta


Koncept grana predstavlja jednu od najmoćnijih funkcija GitHub-a za upravljanje različitim verzijama i razvojnim pravcima unutar jednog projekta. Grana u suštini kreira kopiju ili modifikovanu verziju glavne baze koda, omogućavajući programerima da rade na specifičnim funkcijama, ispravkama grešaka ili eksperimentalnim promenama bez uticaja na primarnu razvojnu liniju. Master grana obično služi kao podrazumevana i najstabilnija verzija projekta, dok dodatne grane prilagođavaju različite iteracije, faze testiranja ili potpuno različite varijante proizvoda.


U hardverskom projektu BitX, postoji više grana za upravljanje različitim verzijama hardvera i konfiguracijama. Na primer, grana Ultra v2 sadrži fajlove specifične za tu iteraciju hardvera, dok se grana Super 401 fokusira na implementacije koristeći S21 ASIC čip za poboljšanu efikasnost. Svaka grana može biti nekoliko commit-a ispred ili iza master grane, što ukazuje na obim promena i razvojne aktivnosti. Kada korisnici pregledaju različite grane, primetiće potpuno različite strukture fajlova, dokumentaciju, pa čak i vizuelne prikaze, što odražava jedinstvene zahteve i specifikacije svake varijante hardvera.


Sistem grana sprečava zabunu među saradnicima i korisnicima tako što jasno razdvaja različite razvojne tokove. Umesto da meša eksperimentalne funkcije sa stabilnim izdanjima, ili kombinuje različite verzije hardvera na jednom mestu, grane omogućavaju čisto razdvajanje uz održavanje mogućnosti spajanja uspešnih promena nazad u glavnu razvojnu liniju kada je to prikladno. Ovaj organizacioni pristup osigurava da korisnici mogu lako pronaći specifičnu verziju koja im je potrebna, dok programeri mogu raditi na poboljšanjima bez ometanja primarnog projekta.


### Doprinos putem problema


Odeljak "Issues" služi kao primarni kanal komunikacije između korisnika i održavatelja projekta za prijavljivanje problema, predlaganje poboljšanja i dokumentovanje grešaka. Međutim, važno je razumeti da je odeljak "Issues" specifično dizajniran za legitimne tehničke probleme, a ne za opšta pitanja ili zahteve za podršku. Kada korisnici naiđu na stvarne kvarove, neočekivano ponašanje ili identifikuju potencijalna poboljšanja, kreiranje dobro dokumentovanog problema pomaže celoj zajednici skretanjem pažnje na probleme koji mogu uticati na više korisnika.


Efektivno prijavljivanje problema zahteva detaljnu dokumentaciju problema, uključujući okolnosti koje su dovele do problema, korake za reprodukciju problema i sve relevantne tehničke detalje. Projekat BitX demonstrira ovaj princip kroz razne zatvorene probleme koji pokazuju proces rešavanja, od početne identifikacije problema preko diskusije u zajednici do konačnog rešenja. Neki problemi rezultiraju poboljšanjima hardvera, kao što je dodavanje montažnih rupa za povećanje opcija hlađenja, dok se drugi mogu rešiti kroz edukaciju korisnika ili ažuriranja softvera.


Razlika između Problema i Diskusija je važna za održavanje organizovane interakcije zajednice. Dok se Problemi fokusiraju na specifične tehničke probleme, sekcija Diskusije pruža okruženje slično forumu za pitanja, ideje i opštu angažovanost zajednice. Iako je Discord server postao primarni kanal komunikacije za BitX zajednicu, sekcija Diskusije na GitHub-u ostaje dostupna za formalnije ili pretražive razgovore koji imaju koristi od trajne dokumentacije i lakog referenciranja.


### Razumevanje Pull Request-ova


Zahtevi za povlačenje predstavljaju mehanizam putem kojeg eksterni saradnici predlažu izmene u repozitorijumu projekta. Kada neko identifikuje poboljšanje, ispravku greške ili novu funkcionalnost koja bi koristila projektu, može kreirati zahtev za povlačenje kako bi podneo svoje izmene na pregled i potencijalnu integraciju u glavnu bazu koda. Ovaj proces osigurava da sve izmene prođu pregled pre nego što postanu deo zvaničnog projekta, održavajući kvalitet koda i koherentnost projekta, dok omogućava doprinos zajednice.


Radni tok zahteva za povlačenje obično počinje kada saradnik fork-uje repozitorijum, kreira svoju kopiju gde može da izvrši izmene, a zatim te izmene podnese nazad u originalni projekat putem zahteva za povlačenje. Održavaoci projekta tada mogu pregledati predložene izmene, diskutovati o modifikacijama sa saradnikom i na kraju odlučiti da li će spojiti izmene u glavni projekat. Ovaj kolaborativni proces pregleda pomaže u održavanju standarda projekta, dok podstiče učešće zajednice i poboljšanje.


Razumevanje oznaka i izdanja dodaje još jedan sloj upravljanju projektima i kontroli verzija. Oznake služe kao markeri na vremenskoj liniji razvoja, identifikujući specifične tačke koje predstavljaju određene verzije ili prekretnice. U hardverskim projektima kao što je BitX, oznake često odgovaraju specifičnim brojevima modela ili revizijama hardvera, pružajući jasne referentne tačke za korisnike koji traže određene verzije. Izdanja, češće korišćena u softverskim projektima, predstavljaju formalne distribucije završenih funkcija i ispravki grešaka, često praćene detaljnim beleškama o izdanju i paketima za preuzimanje.


GitHub ekosistem stvara sveobuhvatno okruženje za saradnju na otvorenom kodu koje se proteže daleko izvan jednostavnog deljenja fajlova. Razumevanjem ovih različitih komponenti i njihove pravilne upotrebe, saradnici mogu efikasno učestvovati u projektima, pomoći u poboljšanju softverskih i hardverskih dizajna i imati koristi od kolektivnog znanja i truda globalne razvojne zajednice. Bilo da prijavljuju probleme, predlažu poboljšanja ili doprinose kodom, GitHub obezbeđuje alate i strukturu neophodne za značajnu saradnju u svetu otvorenog koda.


## Praktičan doprinos otvorenom kodu

<chapterId>84d033f5-7182-584f-b1a5-697172bc7a1c</chapterId>

:::video id=7d318fd0-6f0b-422a-9f30-2c470b56951d:::

Nadovezujući se na osnove kreiranja problema i istraživanja open source projekata, ovo poglavlje se fokusira na praktične aspekte direktnog doprinosa putem pull zahteva i upravljanja repozitorijumima. Razumevanje kako fork repozitorijume, vršiti izmene i podnositi pull zahteve predstavlja ključni skup veština za svakog programera koji želi značajno doprineti open source projektima, bilo da se radi o razvoju softvera ili dizajnu hardvera.


Proces doprinosa promenama u kodu prati standardizovani tok rada koji osigurava integritet projekta dok omogućava kolaborativni razvoj. Ovaj tok rada uključuje kreiranje sopstvene kopije repozitorijuma projekta, pravljenje modifikacija u kontrolisanom okruženju, a zatim predlaganje tih promena nazad originalnom projektu kroz formalan proces pregleda. Iako se primeri u ovom poglavlju prvenstveno fokusiraju na softverske doprinose, isti principi i procedure podjednako se primenjuju na hardverske projekte koji uključuju PCB dizajne, šeme i drugu tehničku dokumentaciju.


### Razumevanje Forkova i Strukture Repozitorijuma


Osnova doprinosa bilo kojem projektu otvorenog koda počinje kreiranjem fork, koji služi kao vaša lična kopija originalnog repozitorijuma. Kada odete na GitHub repozitorijum i kliknete na dugme "fork", kreirate nezavisnu kopiju pod vašim GitHub nalogom koja održava jasnu vezu sa originalnim izvorom. Ovaj forkovani repozitorijum se pojavljuje na vašem nalogu sa jasnom naznakom njegovog porekla, prikazujući tekst kao što je "forked from [original-owner]/[repository-name]" ispod naslova repozitorijuma.


Vaš forkovani repozitorijum radi nezavisno od originalnog, omogućavajući vam da pravite izmene bez uticaja na glavni projekat. Međutim, održava svest o ažuriranjima originalnog repozitorijuma putem GitHub-ovih funkcija za sinhronizaciju. Kada originalni repozitorijum primi ažuriranja koja vašem fork nedostaju, GitHub prikazuje informacije o statusu kao što su "Ova grana je X commit-a iza" ili "X commit-a ispred," pružajući jasnu vidljivost u odnos između vašeg fork i uzvodnog repozitorijuma. Možete sinhronizovati vaš fork sa originalnim repozitorijumom u bilo kom trenutku klikom na dugme "Sync fork," koje povlači najnovije izmene iz uzvodnog izvora.


Odnos između vašeg fork i originalnog repozitorijuma postaje posebno važan kada počnete da pravite izmene. Kada implementirate modifikacije i izvršite ih na vašem fork, GitHub prati te razlike i prikazuje ih kao commit-ove ispred originalnog repozitorijuma. Ovaj sistem praćenja omogućava proces pull request-a, gde možete predložiti vaše izmene za uključivanje u glavni projekat, dok održavate jasnu istoriju onoga što je modifikovano.


### Postavljanje vašeg razvojnog okruženja


Kreiranje efikasnog razvojnog okruženja zahteva pažljivo razmatranje kako opštih razvojnih alata, tako i specifičnih zahteva projekta. Visual Studio Code služi kao odličan integrisani razvojni okruženje (IDE) za većinu doprinosa otvorenom kodu, pružajući osnovne funkcije za uređivanje koda, integraciju kontrole verzija i upravljanje projektima. Prva ključna komponenta uključuje instalaciju i konfiguraciju Git ekstenzije, koja omogućava besprekornu integraciju sa GitHub repozitorijumima direktno iz vašeg razvojnog okruženja.


Savremene verzije Visual Studio Code obično uključuju podršku za Git po defaultu, ali morate se autentifikovati sa svojim GitHub nalogom da biste omogućili punu funkcionalnost. Ovaj proces autentifikacije uključuje prijavljivanje na GitHub kroz IDE, što vam zatim omogućava da klonirate repozitorijume, izvršavate promene i šaljete ažuriranja direktno iz vašeg razvojnog okruženja. GitHub integracija se pojavljuje kao ikonica u levom bočnom panelu, pružajući pristup kloniranju repozitorijuma, upravljanju granama i funkcijama sinhronizacije bez potrebe za komandno-linijskim operacijama.


Za projekte koji uključuju ugrađene sisteme ili specifične hardverske platforme, dodatni alati postaju neophodni. ESP-IDF ekstenzija predstavlja ključnu komponentu za projekte koji ciljaju ESP32 mikrokontrolere, zahtevajući specifičnu verziju kompatibilnosti kako bi se osigurala pravilna funkcionalnost. Proces instalacije uključuje odabir odgovarajuće verzije ESP-IDF, konfigurisanje putanja alata i postavljanje okruženja za razvojni kontejner. Verzija 5.1.3 trenutno predstavlja preporučenu konfiguraciju za mnoge projekte zasnovane na ESP32, iako se ovi zahtevi mogu menjati kako projekti ažuriraju svoje zavisnosti i alatne lance.


### Pravljenje Izmena i Upravljanje Komitima


Kada je vaše razvojno okruženje pravilno konfigurisano, proces davanja značajnih doprinosa počinje preuzimanjem ili kloniranjem vašeg forkovanog repozitorijuma na vaš lokalni računar. Ovo možete postići preuzimanjem ZIP fajla sa sadržajem repozitorijuma ili korišćenjem integrisane funkcionalnosti za kloniranje u Visual Studio Code-u, koja pruža efikasniji tok rada za kontinuirani razvoj. Proces kloniranja kreira lokalnu kopiju vašeg repozitorijuma koja ostaje sinhronizovana sa vašim GitHub fork, omogućavajući vam da radite offline uz održavanje mogućnosti kontrole verzija.


Kada radite sa lokalnim repozitorijumom, dobijate pristup kompletnoj strukturi projekta, uključujući fajlove izvornog koda, konfiguracione fajlove, dokumentaciju i sve fajlove dizajna hardvera. Većina firmware projekata koristi programske jezike kao što je C za osnovnu funkcionalnost, sa dodatnim komponentama napisanim u TypeScript-u za korisničke interfejse ili Java-u za specifične alate. Razumevanje strukture projekta pomaže vam da identifikujete odgovarajuće fajlove za modifikaciju i osigurava da vaše izmene budu u skladu sa arhitektonskim obrascima i standardima kodiranja projekta.


Proces potvrđivanja predstavlja osnovni aspekt kontrole verzija koji zahteva pažnju kako tehničke tačnosti, tako i jasnoće komunikacije. Pre nego što napravite bilo kakve izmene, trebalo bi da temeljno razumete postojeći kod i testirate sve izmene u vašem lokalnom okruženju. Osnovno pravilo doprinosa otvorenom kodu naglašava da nikada ne objavljujete netestirani kod, jer to može uvesti greške ili bezbednosne ranjivosti koje utiču na celu zajednicu projekta. Pored toga, nikada ne smete potvrditi osetljive informacije kao što su lozinke, API tokeni ili lične akreditive u javne repozitorijume, jer te informacije postaju trajno dostupne svakome ko ima pristup repozitorijumu.


### Kreiranje i upravljanje pull zahtevima


Kulminacija vašeg doprinosa uključuje kreiranje pull request-a, koji služi kao formalni predlog za spajanje vaših izmena u originalni repozitorijum projekta. Ovaj proces počinje u vašem GitHub fork, gde možete pregledati razlike između vašeg repozitorijuma i izvornog repozitorijuma. GitHub-ov interfejs jasno prikazuje broj commit-ova ispred ili iza, pružajući trenutni uvid u obim vaših predloženih izmena. Pre nego što kreirate pull request, trebali biste osigurati da je vaš fork usklađen sa najnovijim izmenama izvornog repozitorijuma kako biste minimizirali potencijalne konflikte.


Kreiranje efektivnog pull request-a zahteva više od prostog podnošenja vaših izmena koda. Opis pull request-a služi kao vaša prilika da komunicirate svrhu, obim i uticaj vaših modifikacija prema održavaocima projekta i zajednici. Dobro napisan opis objašnjava koje probleme vaše izmene rešavaju, kako ste implementirali rešenje i sve potencijalne implikacije za druge delove projekta. Ova dokumentacija postaje posebno važna za složene izmene koje možda nisu odmah očigledne samo iz pregleda razlika u kodu.


Proces pregleda predstavlja kolaborativni aspekt razvoja otvorenog koda gde održavaoci projekta i iskusni saradnici ocenjuju vaše predložene izmene. Možete zatražiti određene recenzente koji imaju stručnost u oblastima na koje vaše izmene utiču, osiguravajući da članovi zajednice sa znanjem pregledaju vaš rad. Proces pregleda može uključivati više iteracija, pri čemu recenzenti daju povratne informacije, traže izmene ili zahtevaju dodatno testiranje. Ovaj proces kolaborativnog usavršavanja pomaže u održavanju kvaliteta koda, dok pruža dragocene prilike za učenje saradnicima na svim nivoima iskustva.


Razumevanje da nisu svi pull zahtevi prihvaćeni pomaže u postavljanju odgovarajućih očekivanja za proces doprinosa. Održavaoci projekta mogu odbiti pull zahteve iz raznih razloga, uključujući neusaglašenost sa ciljevima projekta, nedovoljno testiranje ili postojanje alternativnih rešenja koja su već u razvoju. Umesto da se odbijanje posmatra kao neuspeh, treba ga smatrati prilikom za učenje iz povratnih informacija, usavršavanje pristupa i potencijalno doprinos alternativnim rešenjima koja bolje odgovaraju potrebama projekta. Zajednica otvorenog koda napreduje kroz ovaj iterativni proces predloga, pregleda i usavršavanja koji na kraju pokreće projekte napred kroz kolektivni trud i deljeno znanje.



## Šta je Public-Pool?

<chapterId>b461bf94-4a90-5bb8-ba3f-976d5d57be0d</chapterId>


:::video id=d4652496-1ed4-4415-8048-0b6871b9ed51:::

Public Pool predstavlja revolucionarni pristup Bitcoin mining koji rešava mnoge zabrinutosti koje rudari imaju sa tradicionalnim mining bazenima. Kao potpuno open-source solo Bitcoin mining bazen, Public Pool fundamentalno menja model distribucije nagrada na koji su rudari navikli. Za razliku od konvencionalnih mining bazena gde učesnici dele nagrade kada bilo koji rudar u bazenu pronađe blok, Public Pool funkcioniše na principu solo mining gde pojedinačni rudari zadržavaju 100% svojih nagrada za blok kada uspešno iskopaju blok.


Najprivlačnija karakteristika Public Pool-a je njegova struktura bez naknada. Kada rudari uspešno pronađu blok koristeći Public Pool, dobijaju kompletnu nagradu za blok zajedno sa svim povezanim naknadama za transakcije, bez ikakvih odbitaka za troškove rada bazena. Ovo je u oštrom kontrastu sa tradicionalnim mining bazenima koji obično naplaćuju naknade u rasponu od 1-3% mining nagrada. Model bez naknada čini Public Pool posebno privlačnim za rudare koji žele da maksimiziraju svoj potencijalni povratak dok zadržavaju potpunu kontrolu nad svojim mining operacijama.


Da biste razumeli jedinstvenu poziciju Public Pool-a, važno je shvatiti osnovnu razliku između solo mining i udruženog mining. Pravi solo mining znači da kopate nezavisno i dobijate punu nagradu za blok (trenutno 3.125 BTC + naknade) ako pronađete blok, ali je verovatnoća proporcionalna vašoj hash stopi u odnosu na celu mrežu—što stvara ekstremnu varijansu koja može trajati mesecima ili godinama između nagrada. Tradicionalni pool-ovi kombinuju hash snagu da bi češće pronalazili blokove, distribuirajući nagrade proporcionalno i obezbeđujući stabilan, predvidljiv prihod. Za rudare sa značajnim kapitalom uloženim u hardver i operativne troškove, čisti solo mining je obično nepraktičan bez obzira na njegove filozofske prednosti—varijansa čini gotovo nemogućim pokrivanje troškova električne energije i povrat investicija. Ova ekonomska realnost znači da će većina rudara izabrati udruženi mining iz praktičnih finansijskih razloga. Public Pool funkcioniše kao solo mining pool, što znači da se i dalje suočavate sa varijansom solo mining (nagrađeni ste samo kada lično pronađete blok), ali imate koristi od infrastrukture pool-a i transparentnog, operisanja bez naknada.


### Prednost otvorenog koda i tehnička implementacija


Posvećenost Public Pool-a razvoju otvorenog koda pruža rudarima neviđenu transparentnost i kontrolu nad njihovim mining operacijama. Cijela baza koda dostupna je na GitHub-u, omogućavajući rudarima da pregledaju tačno kako softver funkcioniše, modifikuju ga prema svojim potrebama, pa čak i doprinesu njegovom razvoju. Ova transparentnost rešava značajnu zabrinutost u mining zajednici u vezi sa nepoznatim konfiguracijama i praksama tradicionalnih mining bazena.


Softverska arhitektura uključuje i osnovnu funkcionalnost mining pool-a i poseban repozitorijum korisničkog interfejsa, koji su oba dostupna za besplatno preuzimanje i modifikaciju. Rudari mogu pokrenuti Public Pool u različitim konfiguracijama, uključujući Docker kontejnere, što ga čini prilagodljivim različitim hardverskim postavkama i tehničkim preferencijama. Sveobuhvatna dokumentacija dostupna u GitHub repozitorijumima nudi detaljne vodiče za instalaciju, opcije konfiguracije i uputstva za modifikaciju, čineći je dostupnom rudarima sa različitim nivoima tehničke stručnosti.


Povezivanje na javni bazen zahteva minimalnu konfiguraciju u poređenju sa tradicionalnim mining postavkama. Rudari jednostavno treba da konfigurišu svoje mining uređaje sa Stratum detaljima za povezivanje i da obezbede svoju Bitcoin adresu kao korisničko ime. Opcionalno ime radnika može se dodati nakon tačke kao separatora u svrhu organizacije.


### Zajedničke karakteristike i model održivosti


Public Pool uključuje nekoliko inovativnih funkcija koje jačaju zajednicu Bitcoin mining, dok održava svoju operaciju bez naknada. Platforma prikazuje sveobuhvatne statistike uključujući ukupnu hash stopu povezanih rudara, koja je obično bila u rasponu između 1 do 2 PetaHash po sekundi u 2024. i oko 40 PH/s u novembru 2025, i pruža detaljne informacije o povezanim mining uređajima. Posebno je značajan naglasak platforme na open-source mining hardveru, sa uređajima označenim zvezdicama koji ukazuju na potpuno open-source dizajne, zajedno sa linkovima ka njihovim odgovarajućim GitHub repozitorijumima.


Održivost rada javnog bazena bez naknada oslanja se na kreativno partnerstvo u okviru programa pridruženih članova sa dobavljačima hardvera mining. Kada rudari kupuju opremu od partnerskih kompanija koristeći kod za popust "SOLO", pedeset procenata zarade od pridruženih članova podržava operativne troškove javnog bazena, dok se preostalih pedeset procenata distribuira kao nagrade rudarima koji postignu najteže deonice svakog meseca. Ovaj model stvara simbiotski odnos gde rudari dobijaju popuste na kupovinu opreme, dobavljači stiču kupce, a javni bazen održava svoje operacije bez naplate direktnih naknada.


### Filozofija decentralizacije i najbolje prakse


Iako Public Pool nudi odličnu alternativu tradicionalnim mining bazenima, važno je razumeti njegovu ulogu u širem kontekstu decentralizacije Bitcoin. Platforma služi kao odskočna daska ka krajnjem cilju da pojedinačni rudari upravljaju sopstvenim mining bazenima. Vođenje sopstvenog mining bazena predstavlja najviši nivo decentralizacije, jer eliminiše zavisnost od bilo koje infrastrukture ili softvera treće strane, bez obzira na to koliko ta treća strana bila transparentna ili dobronamerna.


Javna priroda Public Pool-a čini ga idealnom platformom za učenje za rudare koji žele da razumeju rad bazena pre nego što implementiraju sopstvena rešenja. Dostupnost vodiča za instalaciju za više operativnih sistema i sveobuhvatna dokumentacija pružaju rudarima znanje potrebno za prelazak sa korišćenja Public Pool-a na upravljanje sopstvenom mining infrastrukturom. Ovaj obrazovni aspekt je u skladu sa osnovnim principima Bitcoin o samosuverenitetu i decentralizaciji, osnažujući pojedinačne rudare da preuzmu potpunu kontrolu nad svojim mining operacijama dok doprinose ukupnoj sigurnosti i decentralizaciji Bitcoin mreže.


Korisnički interfejs platforme pruža rudarima detaljne mogućnosti praćenja, uključujući status radnika, statistiku hash stope i metrike performansi. Ove funkcije pomažu rudarima da optimizuju svoje operacije dok uče o principima upravljanja bazenom koje kasnije mogu primeniti na sopstvene implementacije mining bazena.


## Kako instalirati Public-Pool na Umbrel

<chapterId>7f6d0307-7715-5581-89ea-f13cf8754f9a</chapterId>


:::video id=3a4fe0a9-bbf5-458a-8ec1-52c3b83afd87:::

Pokretanje sopstvenog Bitcoin mining bazena kod kuće postalo je sve dostupnije uz moderni hardver i pojednostavljena softverska rešenja. Ovo poglavlje istražuje praktičnu implementaciju javnog bazena baziranog kod kuće koristeći pristupačan mini PC hardver i pojednostavljeni softver za upravljanje čvorovima. Do kraja ovog vodiča, razumećete hardverske zahteve, proces postavljanja softvera i osnovnu konfiguraciju potrebnu za uspostavljanje sopstvene mining infrastrukture bazena.


### Hardverski Zahtevi i Postavljanje


Osnova svake kućne mining postavke bazena počinje odabirom odgovarajućeg hardvera koji balansira performanse, troškove i energetsku efikasnost. Mini PC predstavlja idealno rešenje za ovu primenu, nudeći dovoljno procesorske snage uz održavanje kompaktnog formata i razumne potrošnje energije. Preporučena konfiguracija uključuje Intel N100 procesor, koji pruža adekvatne računarske resurse za rad bazena, uparen sa najmanje jednim terabajtom NVMe skladišta za smeštaj Bitcoin blockchaina i povezane podatke.


Zahtev za skladištenjem je posebno kritičan jer pokretanje mining bazena zahteva održavanje potpuno sinhronizovanog Bitcoin čvora. Jedan terabajt NVMe disk obezbeđuje brze operacije čitanja/pisanja koje su neophodne za sinhronizaciju blockchain-a i kontinuiranu obradu transakcija. Pored toga, dovoljna alokacija RAM-a podržava nesmetan rad kako osnovnog Linux operativnog sistema, tako i softvera za upravljanje čvorovima koji će koordinisati aktivnosti bazena.


### Arhitektura softvera i upravljanje čvorovima


Softverski stek za kućni bazen mining izgrađen je na Linux osnovi, pružajući stabilnost i sigurnost neophodnu za rad Bitcoin. Na ovom osnovnom sistemu, specijalizovani softver za upravljanje čvorovima kao što je Umbrel stvara intuitivan interfejs za upravljanje infrastrukturom Bitcoin. Ovaj pristup apstrahuje mnogo složenosti tradicionalno povezane sa pokretanjem Bitcoin čvorova, čineći rad bazena dostupnim korisnicima bez opsežnog tehničkog znanja.


Umbrel služi kao sveobuhvatna platforma za upravljanje čvorovima koja rukuje instalacijom, sinhronizacijom i stalnim održavanjem Bitcoin Core-a putem web interfejsa. Model prodavnice aplikacija na platformi omogućava jednostavnu instalaciju dodatnih usluga, uključujući mining pool softver, kroz jednostavne operacije pokazivanja i klika. Ova arhitektura osigurava da korisnici mogu da se fokusiraju na rad pool-a umesto na administraciju sistema, dok i dalje zadržavaju potpunu kontrolu nad svojom Bitcoin infrastrukturom.


### Instalacija i konfiguracija javnog bazena


Instaliranje softvera za javni bazen putem Umbrel platforme pokazuje pojednostavljenu prirodu modernog Bitcoin infrastrukturnog postavljanja. Proces počinje pristupom Umbrel prodavnici aplikacija putem web interfejsa, gde jednostavna pretraga za "javnim bazenom" otkriva dostupni mining softver za bazen. Instalacija zahteva samo nekoliko klikova: odabir aplikacije, potvrdu instalacije i čekanje da se automatski proces postavljanja završi.


Proces instalacije automatski konfiguriše neophodne veze između softvera javnog bazena i osnovnog Bitcoin čvora. Ova integracija osigurava da bazen može validirati transakcije, konstruisati blok šablone i distribuirati rad povezanim rudarima bez potrebe za ručnom konfiguracijom složenih mrežnih parametara. Kada se instalacija završi, interfejs bazena postaje odmah dostupan putem lokalne mreže, pružajući mogućnosti za praćenje i upravljanje u realnom vremenu.


### Povezivanje rudara i razmatranja mreže


Povezivanje mining hardvera sa vašim novoosnovanim bazenom zahteva konfigurisanje postavki bazena rudara kako bi se usmerile ka vašoj lokalnoj infrastrukturi. Ovo podrazumeva zamenu podrazumevane adrese bazena sa vašom lokalnom IP adresom i odgovarajućim brojem porta dodeljenim tokom instalacije javnog bazena. Promena konfiguracije preusmerava računarske napore vašeg mining hardvera sa eksternih bazena na vašu kućnu infrastrukturu, omogućavajući vam da zadržite potpunu kontrolu nad operacijama mining i potencijalnim nagradama.


Konfiguracija mreže igra ključnu ulogu u pristupačnosti i funkcionalnosti bazena. Postavljanje lokalne mreže obično uključuje standardno adresiranje IP-a, ali korisnici mogu naići na varijacije u DNS rezoluciji u zavisnosti od konfiguracije njihovog rutera. Neki ruteri pružaju lokalne DNS usluge koje kreiraju prijateljska imena za lokalne usluge, dok drugi zahtevaju direktan pristup IP adresi. Za širu pristupačnost izvan lokalne mreže, može biti neophodna konfiguracija prosleđivanja portova na ruteru, iako ovo uvodi dodatne bezbednosne razmatranja koja zahtevaju pažljivu procenu povezanih rizika i koristi.


Uspešno uspostavljanje kućnog mining bazena predstavlja značajan korak ka decentralizovanoj Bitcoin infrastrukturi, pružajući i obrazovnu vrednost i praktične mining sposobnosti, dok istovremeno održava potpunu kontrolu nad vašim Bitcoin operacijama.


# Sklapanje i rešavanje problema sa hardverom

<partId>f6987088-5ba4-52e2-b2d0-aa122080940c</partId>


## Koje alate koristiti?

<chapterId>733935b5-0171-5a22-838c-e192df6f7ccf</chapterId>


:::video id=bddd0e47-7b43-4685-ba2e-bf3a8ff653c9:::

U svetu lemljenja površinski montiranih uređaja (SMD), posebno kada radite na Bitaxe projektima, posedovanje pravih alata čini razliku između frustracije i uspeha. Ovaj sveobuhvatni vodič pokriva osnovnu opremu potrebnu za efikasno rešavanje SMD lemljenja, od osnovnih ručnih alata do specijalizovane opreme koja će unaprediti vaše sposobnosti lemljenja.


Ako želite da se pozovete na neku dokumentaciju o šemama, pogledajte ovaj [GitHub repo](https://github.com/skot/bitaxe-doc/tree/main).


### Osnovni ručni alati i precizni instrumenti


Osnova svake SMD lemljenja počinje sa kvalitetnim pincetama, koje služe kao vaši primarni alati za postavljanje komponenti. Dve vrste pinceta su najvrednije u ovom radu: standardne pincete sa ravnim vrhom i one sa blagim savijanjem na vrhu. Pincete sa ravnim vrhom rukovode većinom SMD komponenti koje se nalaze u tipičnim Bitaxe kompletima, dok pincete sa savijenim vrhom briljiraju kada se radi sa izuzetno malim komponentama koje zahtevaju precizno pozicioniranje. Ovi alati često dolaze uključeni u setove za popravku, kao što su iFixit setovi dizajnirani za popravke telefona, čineći ih lako dostupnim većini hobista.


Dopunjujući pincetu, dobar par makaza postaje neophodan za sečenje električne trake, koja ima višestruku namenu u elektronskim projektima. Električna traka pruža neophodnu izolaciju za kablove i komponente, a dostupnost kvalitetne trake olakšava proces lemljenja. Ove osnovne potrepštine mogu se nabaviti u prodavnicama alata ili kod online prodavaca, bez potrebe za specijalizovanim dobavljačima elektronike.


### Primena i upravljanje pastom za lemljenje


Primena lemne paste predstavlja jedan od najkritičnijih aspekata SMD lemljenja, a pravi alati čine ovaj proces i preciznim i prijatnim. Male, neoštre šprice napunjene lemnom pastom pružaju izuzetnu kontrolu nad postavljanjem paste. Ova metoda omogućava preciznu primenu tačne količine lemne paste potrebne za svaki spoj, a većina ljudi brzo razvije odgovarajuću tehniku za kontrolu pritiska i protoka kroz praktičnu vežbu.


Izbor same lemne paste značajno utiče na uspeh lemljenja. ChipQuik TS391SNL50 se izdvaja kao izuzetna lemna pasta za Bitaxe projekte i opšti SMD rad. Ova pasta održava odgovarajuću konzistenciju i karakteristike topljenja, izbegavajući probleme povezane sa jeftinijim alternativama koje imaju previše niske tačke topljenja. Lemne paste niskog kvaliteta mogu stvoriti probleme gde prethodno zalemljeni spojevi ponovo postaju fluidni prilikom zagrevanja susednih područja, što dovodi do pomeranja komponenti i loših veza. Iako kvalitetna lemna pasta predstavlja veće početno ulaganje, poboljšani rezultati i smanjena frustracija opravdavaju trošak.


### Alati za rešavanje problema i čišćenje


Čak i iskusni lemilci nailaze na probleme koji zahtevaju ispravku, što čini opremu za odlemljivanje neophodnom za svaki kompletan alatni set. Aparat za odlemljivanje, koji je u suštini alat sa grejanjem i vakuumom, uklanja višak lema i ispravlja spojene veze između pinova komponenti. Ovi alati najefikasnije rade kada se koriste zajedno sa fluksom, koji poboljšava protok lema i pomaže da proces odlemljivanja bude efikasniji.


Fluks dolazi u raznim oblicima, uključujući čvrste i tečne varijante, i služi za više svrha osim pomoći pri odlemljivanju. Kada pasta za lemljenje počne da gubi svoju efikasnost tokom produženih radnih sesija, primena dodatnog fluksa vraća odgovarajuće karakteristike protoka i osigurava pouzdane veze. Mali alat nalik kašičici, često pronađen u kompletima za precizne popravke, omogućava preciznu primenu fluksa na određena područja bez kontaminacije okolnih komponenti.


Čišćenje ploče predstavlja završni korak u radu profesionalnog kvaliteta, zahtevajući izopropanol alkohol i posvećenu četku za čišćenje. Stara četkica za zube savršeno odgovara ovoj svrsi, a boca sa izopropanolom omogućava kontrolisanu primenu rastvora za čišćenje. Ova kombinacija uklanja ostatke fluksa i paste, ostavljajući ploče sa čistim, profesionalnim izgledom koji takođe olakšava inspekciju lemnih spojeva.


### Specijalizovana oprema i napredni alati


Za projekte koji uključuju složene integrisane kola, posebno ASIC-ove, šabloni transformišu proces lemljenja iz zamornog ručnog postavljanja u efikasnu, preciznu primenu paste. Ovi precizno isečeni šabloni obezbeđuju doslednu debljinu i postavljanje paste, dramatično smanjujući vreme potrebno za složene komponente dok poboljšavaju pouzdanost. Investicija u kvalitetne šablone donosi dividende u uštedi vremena i poboljšanim rezultatima.


Termalno upravljanje postaje ključno kada se radi sa energetskim komponentama, što čini termalnu pastu ili termalnu mast neophodnim materijalima. Ovi materijali osiguravaju pravilan prenos toplote između hladnjaka i integrisanih kola, sprečavajući termalna oštećenja i osiguravajući pouzdan rad. Kvalitetni termalni interfejs materijali predstavljaju malu investiciju koja štiti mnogo skuplje komponente.


Srce svake SMD lemljenja je stanica za prepravku vrućim vazduhom, koja obezbeđuje kontrolisanu toplotu neophodnu za rad sa površinskim montažama. Iako budžetske stanice u rasponu od $30-50 mogu raditi adekvatno, često im nedostaje pouzdanost i preciznost opreme višeg ranga. Ove osnovne stanice obično efikasno rade na 355°C i uključuju automatsko smanjenje temperature kada se ručka vrati u svoj držač. Međutim, njihova pouzdanost može biti nedosledna, sa nekim jedinicama koje prerano otkazuju. Za ozbiljan rad, ulaganje u kvalitetniju opremu od specijalizovanih dobavljača elektronike pruža bolju dugoročnu vrednost kroz poboljšanu pouzdanost i precizniju kontrolu temperature.


Kombinacija ovih alata stvara kompletnu sposobnost za SMD lemljenje koja se proteže daleko izvan Bitaxe projekata do opšteg rada na elektronici. Razumevanje uloge svakog alata i odabir kvalitetne opreme koja odgovara vašem nivou veštine i zahtevima projekta osigurava uspešne rezultate i prijatno iskustvo lemljenja.



## Popravite probleme sa lemljenjem

<chapterId>96663744-b4f7-5154-930f-a68ba7954603</chapterId>


:::video id=9286c0dc-acd6-44d9-b34e-59cfb2da9748:::


Komplet Bitaxe predajnika predstavlja jedinstvene izazove tokom sklapanja koji zahtevaju pažljivo obraćanje pažnje na orijentaciju komponenti, sprečavanje stvaranja lemnih mostova i pravilno upravljanje toplotom. Razumevanje ovih uobičajenih problema i njihovih rešenja je ključno za uspešnu izradu kompleta i izbegavanje skupih oštećenja komponenti. Ovo poglavlje ispituje najčešće probleme sa lemljenjem koji se javljaju tokom sklapanja Bitaxe-a i pruža praktične tehnike za njihovo prepoznavanje i rešavanje.


### Orijentacija i identifikacija komponenti


Pravilna orijentacija komponenti predstavlja jedan od najkritičnijih aspekata uspešne montaže Bitaxe-a, posebno sa MOSFET-ima Q1 i Q2. Ove komponente imaju karakteristične oznake za orijentaciju koje moraju biti pažljivo posmatrane tokom instalacije. Svaki MOSFET sadrži malu tačku koja odgovara specifičnim rasporedima padova na štampanoj ploči. Ključ za pravilnu orijentaciju leži u razumevanju fizičke strukture ovih komponenti, koje imaju četiri pina raspoređena sa jednim velikim padom i tri manja pada koja nemaju vezu sa velikim padom.


Kada instalirate Q1 i Q2, pažljivo pregledajte i komponentu i štampanu ploču. Raspored ploče jasno pokazuje predviđenu orijentaciju kroz konfiguraciju padova, sa četiri pina postavljena da odgovaraju strukturi MOSFET-a. Pre nego što zalemite bilo koju veliku komponentu, uvek proverite orijentaciju upoređivanjem fizičkih oznaka komponente sa rasporedom padova na ploči. Ovaj jednostavan korak provere sprečava frustraciju od odlemljivanja i ponovnog instaliranja pogrešno orijentisanih komponenti.


Posledice pogrešne orijentacije prevazilaze jednostavne probleme sa funkcionalnošću. Pogrešno orijentisani MOSFET-ovi mogu izazvati kvarove u kolu koje je teško dijagnostikovati i mogu zahtevati potpunu zamenu komponenti. Odvajanje vremena za proveru orijentacije pre primene toplote osigurava pravilno funkcionisanje kola i sprečava nepotrebno rešavanje problema kasnije u procesu sklapanja.


### Upravljanje lemnim mostovima i viškom lema


Solder mostovi predstavljaju još jedan čest izazov u sklapanju Bitaxe-a, posebno oko komponenti sa finim razmakom kao što je U10. Ove neželjene veze između susednih pinova mogu izazvati kvarove u krugu i zahtevaju pažljive tehnike uklanjanja. Najefikasniji pristup uključuje korišćenje pletenice za odlemljivanje, materijala od bakarne pletenice koji upija višak lema kada se zagreje. Ova tehnika zahteva strpljenje i pravilan izbor alata kako bi se izbeglo oštećenje osetljivih komponenti.


Kada rešavate probleme sa kratkim spojevima na integrisanim kolima, koristite držač za PCB ili zglobnu stezaljku da sigurno držite komponentu dok radite. Nanesite blagu toplotu na pogođeno područje i pažljivo povucite traku za odlemljivanje preko spojnih veza. Bakarna pletenica prirodno upija višak lema, razdvajajući neželjene spojeve. Ovaj proces može zahtevati više pokušaja, ali upornost donosi čiste, pravilno razdvojene spojeve.


Prevencija ostaje najbolji pristup upravljanju lemljenjem mostova. Korišćenje odgovarajuće količine paste za lemljenje i održavanje stabilne kontrole ruku tokom postavljanja komponenti značajno smanjuje formiranje mostova. Kada se mostovi ipak pojave, rešavajte ih odmah umesto da se nadate da neće uticati na rad kola. Čak i naizgled manji mostovi mogu izazvati značajne probleme u funkcionalnosti koje je teško dijagnostikovati kada je ploča potpuno sastavljena.


### Kritične komponente i posebna razmatranja


Pretvarač napona U9 zaslužuje posebnu pažnju zbog svoje ključne uloge u konvertovanju 5 volti na 1.2 volta za ASIC čip. Ova komponenta predstavlja jedinstvene izazove zbog svojih pet malih spojeva i sklonosti ka kvaru. Pravilna instalacija zahteva preciznu primenu lemne paste i pažljivo upravljanje toplotom. Nedovoljna količina lemne paste ispod U9 može rezultirati lošim spojevima koji sprečavaju pravilnu konverziju napona, dok višak paste može stvoriti mostove koji uzrokuju kvar kola.


U9 proizvodi prepoznatljive audio potpise kada dođe do problema sa spojem lemova, generišući visokofrekventnu buku koja se razlikuje od normalnog rada ASIC. Ova auditivna dijagnostička tehnika može pomoći u identifikaciji problema, iako zahteva dobro čulo sluha za visoke frekvencije da bi se otkrila. Kada audio dijagnoza nije moguća, vizuelna inspekcija postaje neophodna. Pažljivo pregledajte sve spojeve, tražeći mostove ili nedovoljnu pokrivenost lemom.


Ako U9 ne uspe da proizvede potrebnih 1,2 volti uprkos tome što izgleda pravilno zalemljen, razmotrite nedovoljnu količinu lemne paste kao verovatan uzrok. Uklonite komponentu, nanesite malu količinu dodatne lemne paste i ponovo je instalirajte. U slučajevima kada pojedinačni pinovi nemaju adekvatnu pokrivenost lemom, pažljivo nanesite male količine lemne paste na određena mesta koristeći pincetu. Lemna pasta će prirodno teći ispod komponente kada se zagreje, stvarajući pravilne veze kroz kapilarno delovanje.


### Upravljanje toplotom i zaštita komponenti


Pravilno upravljanje toplotom štiti osetljive komponente od termalnog oštećenja, istovremeno osiguravajući pouzdane lemne spojeve. Komponente kao što su kristalni oscilator Y1 i U1 su posebno osetljive na dugotrajnu izloženost toploti i zahtevaju pažljivu kontrolu temperature. Održavajte temperaturu lemilice na 350 stepeni Celzijusa, ali minimizirajte vreme primene toplote kako biste sprečili oštećenje komponenti. Brze i efikasne tehnike lemljenja štite ove osetljive komponente, dok se postižu pouzdane veze.


ASIC čip zahteva posebne tehnike rukovanja zbog svoje složene strukture pinova i osetljivosti na mehanički stres. Kada koristite šablone za nanošenje lemne paste, obezbedite ravnomerno prekrivanje svih pinova kako biste sprečili neravnomerno postavljanje komponenti. Ako prekomerna količina lemne paste uzrokuje da ASIC bude neravnomerno postavljen, dozvolite da se sklop potpuno ohladi pre nego što izvršite korekcije. Primenujte blagi pritisak samo na označene ivice komponente, nikada na centralno područje čipa, dok ponovo zagrevate kako biste postigli pravilno postavljanje.


Komponenta U8 predstavlja jedinstvene izazove zbog brojnih pinova i potencijala za savijene kontakte. Kada se pinovi saviju tokom rukovanja, koristite držač za PCB ili zglobnu stezaljku da osigurate komponentu i pažljivo ispravite pogođene pinove. Radite polako i strpljivo kako biste izbegli lomljenje delikatnih kontakata. Razumevanje da su određene grupe pinova na U8 interno povezane može pojednostaviti rešavanje problema, jer mostovi između ovih specifičnih pinova ne utiču na rad kola. Međutim, mostovi između drugih pinova zahtevaju pažljivo uklanjanje kako bi se osigurala ispravna funkcionalnost.


## Kako otkloniti greške na vašem Bitaxe koristeći AxeOS

<chapterId>603f5c0d-4b7c-51e1-9bad-318a8b8e9db7</chapterId>

:::video id=d23d748b-510e-4748-9617-b875da757031:::

Kada radite sa uređajima Bitaxe mining, hardverski kvarovi mogu se manifestovati na različite načine koji možda neće biti odmah očigledni. Razumevanje kako sistematski dijagnostikovati ove probleme koristeći AxeOS operativni sistem može uštedeti značajno vreme i sprečiti nepotrebne zamene komponenti. Ovo poglavlje istražuje dijagnostičke tehnike i metodologije za rešavanje problema koje iskusni tehničari koriste da identifikuju specifične hardverske probleme putem softverske analize.


### Razumevanje indikatora potrošnje energije


Prvi i najvažniji dijagnostički indikator u AxeOS-u je praćenje potrošnje energije. Normalni Bitaxe uređaji, uključujući modele Bitaxe Ultra i Bitaxe Supra, obično troše između 10 do 17 vati tokom standardnog rada. Ova osnovna merenja služe kao vaš primarni pokazatelj zdravlja celog sistema. Kada potrošnja energije značajno padne ispod ovog opsega, posebno ispod 3 vata, to ukazuje na osnovni problem sa ASIC čipom ili njegovim pratećim sklopovima.


Scenariji niske potrošnje energije zahtevaju hitnu pažnju jer ukazuju na to da je čip mining ili potpuno nefunkcionalan ili radi u ozbiljno degradiranom stanju. Ovo merenje samo po sebi može vam pomoći da brzo razlikujete probleme sa performansama od potpunih kvarova hardvera. Očitavanje potrošnje energije u AxeOS-u pruža povratne informacije u realnom vremenu koje vam omogućavaju da pratite efikasnost bilo kakvih pokušaja popravke uređaja.


### Analiziranje ASIC merenja napona


Funkcija merenja napona ASIC u AxeOS pruža ključne dijagnostičke informacije koje pomažu u preciznom određivanju prirode hardverskih problema. Kada pregledate očitavanja napona, potrebno je razumeti odnos između izmerenog napona i traženog napona kako biste pravilno dijagnostikovali probleme. Sistem prikazuje i napon koji se isporučuje čipu ASIC i napon koji čip zahteva od sistema za upravljanje napajanjem.


Kada primetite merenje napona ASIC tačno 1.2 volti u kombinaciji sa potrošnjom energije ispod 3 vata, ova specifična kombinacija ukazuje ili na problem sa lemljenjem ASIC čipa ili na potpuno otkazivanje ASIC. Ovo očitavanje napona sugeriše da struja dolazi do lokacije čipa, ali sam čip ne funkcioniše pravilno. Fizička inspekcija ASIC matrice može otkriti pukotine ili druga vidljiva oštećenja koja bi objasnila ovaj obrazac ponašanja.


Drugačiji dijagnostički scenario se pojavljuje kada vidite nisku potrošnju energije u kombinaciji sa veoma niskim očitavanjima traženog napona, kao što su 100 milivolti ili 0,5 volti. Ovaj obrazac ukazuje na to da ASIC čip ne prima adekvatno napajanje naponom, što obično ukazuje na probleme sa U9 buck konverter komponentom. Buck konverter je odgovoran za obezbeđivanje precizne regulacije napona koju ASIC čipovi zahtevaju za pravilno funkcionisanje.


### Tumačenje podataka dnevnika i komunikacija ASIC


Sistem za beleženje AxeOS pruža dragocene uvide u to da li vaš ASIC čip komunicira sa kontrolnim sistemom. Kada pristupite zapisima putem funkcije "show logs", prisustvo unosa "ASIC results" potvrđuje da čip nije samo uključen, već i aktivno obrađuje zadatke i vraća rezultate. Ova komunikacija ukazuje na to da je ASIC pravilno zalemljen i održava vezu sa kontrolnim kolima.


Odsustvo ASIC rezultata u logovima, posebno kada je kombinovano sa drugim simptomima, pomaže u sužavanju problema na specifične komponente ili probleme sa povezivanjem. Ovaj dijagnostički pristup omogućava vam da razlikujete čipove koji su potpuno neodgovarajući od onih koji mogu imati povremene probleme sa povezivanjem. Analiza logova postaje posebno vredna kada se rešavaju složeni problemi gde više simptoma može ukazivati na različite osnovne uzroke.


### Sistematski pristup rešavanju problema


Kada dijagnostikujete probleme sa Bitaxe hardverom, praćenje sistematskog pristupa sprečava previđanje kritičnih problema i osigurava efikasne procese popravke. Počnite dokumentovanjem potrošnje energije i očitavanja napona, zatim povežite ova merenja sa podacima iz dnevnika kako biste izgradili potpunu sliku ponašanja sistema. Ovaj metodičan pristup pomaže u identifikaciji da li problemi potiču od samog ASIC čipa, sistema za isporuku energije ili komunikacionih puteva između komponenti.


U slučajevima kada se čini da je U9 buck konverter problem, fizička inspekcija i potencijalno ponovno lemljenje mogu biti neophodni. Komponenta U9 je posebno podložna problemima sa lemljenjem, naročito u situacijama prve montaže. Kada se sumnja na probleme sa regulacijom napona, korišćenje multimetra za proveru da li je 1.2 volta zaista prisutno na ASIC pinovima pruža konačnu potvrdu problema sa isporukom napajanja. Ako je napon prisutan na pinovima, ali ASIC i dalje ne funkcioniše, a fizička inspekcija ne otkriva oštećenja, zamena ASIC čipa postaje sledeći logičan korak. Ako problemi i dalje postoje čak i nakon zamene ASIC, komponenta U2, koja pokreće ASIC čip, može zahtevati pažnju kao poslednji element u sekvenci rešavanja problema.


## Kako otkloniti greške pomoću USB-a?

<chapterId>f3182763-e1ef-5460-8bc0-f2ea53e3a410</chapterId>


:::video id=fe1b4b48-5f8a-4fd7-9417-ca03a36bce9f:::


Kada rešavate probleme sa Bitaxe mining uređajima, direktan pristup internom sistemu logovanja uređaja pruža neprocenjive uvide koje web-bazirani interfejsi ne mogu da ponude. Ovo poglavlje istražuje kako uspostaviti direktnu USB serijsku vezu sa vašim Bitaxe uređajem koristeći ESP-IDF okvir, omogućavajući praćenje sistemskih logova, sekvenci pokretanja i poruka o greškama u realnom vremenu. Ovaj pristup debagovanju je posebno ključan kada se bavite uređajima koji često doživljavaju ponovna pokretanja ili hardverske kvarove, jer beleži sve dijagnostičke informacije koje bi mogle biti izgubljene tokom ponovnih pokretanja sistema.


Proces otklanjanja grešaka zahteva Visual Studio Code sa ESP-IDF ekstenzijom, iako se može koristiti bilo koji kompatibilni IDE. Ova metoda radi sa svim Bitaxe varijantama koje uključuju USB port, uključujući Bitaxe Ultra 204 i druge modele u seriji. Direktna serijska veza zaobilazi potencijalna ograničenja web interfejsa i pruža nefiltrirani pristup informacijama o unutrašnjem stanju uređaja.


### Postavljanje serijske komunikacije


Uspostavljanje komunikacije sa vašim Bitaxe uređajem počinje povezivanjem USB kabla i otvaranjem ESP-IDF terminala unutar vašeg razvojnog okruženja. Komanda `idf.py monitor` pokreće proces povezivanja, automatski skenirajući dostupne COM portove kako bi uspostavila UART komunikaciju sa ESP32 čipom na vašem Bitaxe uređaju. Sistem obično prolazi kroz dostupne portove (COM3, COM4, COM16, itd.) dok ne pronađe ispravnu vezu.


Kada se poveže, terminal prikazuje kompletan redosled pokretanja i tekuće operativne zapise. Početni proces povezivanja može potrajati nekoliko trenutaka dok sistem identifikuje ispravan komunikacioni port. Ako automatsko otkrivanje porta ne uspe, možete ručno odrediti COM port putem interfejsa za izbor porta u IDE-u. Ovaj direktni komunikacioni kanal ostaje aktivan tokom celokupnog rada uređaja, pružajući kontinuirani pristup sistemskoj dijagnostici i metrikama performansi.


### Tumačenje redosleda pokretanja i dnevnika normalnog rada


Redosled pokretanja pruža ključne informacije o hardverskoj konfiguraciji i procesu inicijalizacije vašeg Bitaxe uređaja. Normalni dnevnici pokretanja počinju sa informacijama o verziji ESP-IDF, nakon čega sledi prepoznatljiva poruka "Welcome to the Bitaxe. Hack the planet" koja potvrđuje uspešno učitavanje firmvera. Sistem zatim prikazuje konfiguraciju frekvencije ASIC, identifikaciju modela uređaja i detalje o verziji ploče.


Ispravno funkcionišući uređaj će pokazati uspešnu I2C inicijalizaciju i ASIC regulaciju napona podešenu na 1.2 volti. Logovi prikazuju informacije o statusu GPIO i sekvence inicijalizacije Wi-Fi-ja, nakon čega sledi konfiguracija DHCP servera i dodela IP adrese. Jedan od najvažnijih indikatora je poruka o detekciji ASIC čipa, koja bi trebalo da prijavi "detected one ASIC chip" za uređaj sa jednim čipom. Ova potvrda validira da je mining hardver pravilno povezan i komunicira sa ESP32 kontrolerom.


Operativni dnevnici otkrivaju više istovremenih zadataka koji rade na uređaju, uključujući komunikaciju stratum API, koordinaciju glavnog zadatka, upravljanje zadacima ASIC i obradu zadataka stratum. Ovi različiti identifikatori zadataka pomažu u izolaciji problema na specifične komponente sistema. Normalan rad uključuje uspostavljanje veze sa bazenom, poruke o prilagođavanju težine, redove čekanja i uklanjanja poslova, i izveštavanje o generisanju nonce-a. Uspešne operacije mining prikazuju rezultate ASIC sa proračunima težine i potvrde o predaji mining kada akcije zadovoljavaju potrebni prag.


### Identifikacija kvarova hardvera i obrazaca grešaka


Kvarovi hardvera manifestuju se u logovima kroz specifične šablone grešaka koji ukazuju na to koji komponenti ne funkcionišu ispravno. Najčešći način kvara uključuje I2C komunikacione greške sa specifičnim integrisanim kolima na Bitaxe ploči. Na primer, DS4432U komunikacioni kvarovi se pojavljuju kao poruke "ESP_ERROR_CHECK failed" sa indikatorima isteka vremena, ukazujući na probleme sa regulacijom napona ili probleme sa lemljenjem koji utiču na U10 komponentu odgovornu za komunikaciju sa ekranom.


Ove poruke o greškama uključuju detaljne informacije za otklanjanje grešaka kao što su specifična izvorna datoteka (main_ds4432u.c), neuspeli poziv funkcije i procesorska jezgra koja obrađuje zadatak. Informacije o povratnom tragu pružaju dodatni kontekst za napredno rešavanje problema. Slični obrasci grešaka mogu se pojaviti sa EMC2101 čipom za kontrolu temperature i ventilatora, pri čemu svaki generiše prepoznatljive potpise u logovima koji pomažu u identifikaciji neispravne komponente.


Fizički problemi sa hardverom često se manifestuju kao ponovljeni ciklusi grešaka praćeni ponovnim pokretanjem sistema. Ako vaš uređaj proizvodi zvukove tokom rada, to obično ukazuje na probleme sa lemljenjem kao što su mostovi između pinova komponenti ili neadekvatni lemni spojevi. Iako ovi mehanički problemi možda nisu uvek generate specifični zapisi u logovima, oni stvaraju nestabilne uslove rada koji se manifestuju kao česti padovi sistema i ciklusi ponovnog pokretanja u izlazu monitoringa.


### Napredne strategije za rešavanje problema


Serijsko praćenje pruža nekoliko prednosti u odnosu na web-bazirane interfejse za otklanjanje grešaka, posebno za povremene kvarove ili uređaje koji često restartuju. Kontinuirano hvatanje logova osigurava da nijedna dijagnostička informacija nije izgubljena tokom ponovnog pokretanja sistema, za razliku od web interfejsa koji mogu izgubiti podatke tokom događaja prekida veze. Ova sveobuhvatna sposobnost logovanja omogućava identifikaciju obrazaca u kvarovima i povezivanje specifičnih uslova grešaka sa hardverskim ili ekološkim faktorima.


Kada analizirate problematične uređaje, fokusirajte se na redosled događaja koji vode do kvarova, a ne na izolovane poruke o greškama. Uspešna ASIC komunikacija treba da pokazuje redovno procesiranje poslova, generisanje nonce-a i cikluse podnošenja deljenja. Nedostajući ASIC rezultati u logovima ukazuju na komunikacione greške između ESP32 i mining čipa, često uzrokovane problemima sa napajanjem, oštećenim tragovima ili kvarovima komponenti.


Za sistematsko rešavanje problema, dokumentujte obrasce grešaka i kvarove specifične za komponente pre nego što potražite podršku zajednice. Detaljni dnevnici grešaka, uključujući specifične identifikatore čipova i načine kvara, omogućavaju iskusnim korisnicima da pruže ciljane smernice za popravku, kao što su procedure zamene komponenti ili korekcije lemljenja. Ovaj metodičan pristup otklanjanju hardverskih grešaka značajno poboljšava uspešnost popravki i smanjuje vreme potrebno za rešavanje složenih problema.


# Napredno prilagođavanje

<partId>8d333102-ecb5-5f05-bfb5-03a27b2d0d70</partId>


## Izmeni PCB

<chapterId>ca08d2a4-2b34-575b-aecc-7482a03c190e</chapterId>


:::video id=30fb0010-f560-4e96-a05b-c21dc172746e:::

KiCad predstavlja jedan od najmoćnijih alata otvorenog koda dostupnih za dizajn i rutiranje štampanih ploča (PCB). Ovaj softver profesionalnog nivoa omogućava inženjerima i hobistima da kreiraju složene elektronske dizajne postavljanjem komponenti na virtuelne ploče i rutiranjem složenih veza koje povezuju te komponente. Ono što čini KiCad posebno vrednim za obrazovne i razvojne svrhe je njegova potpuna priroda otvorenog koda, koja omogućava korisnicima da modifikuju, prilagođavaju i uče iz postojećih dizajna bez ograničenja licenci.


Projekat Bitaxe oslikava moć razvoja open-source hardvera, pružajući kompletan dizajn PCB-a koji korisnici mogu pregledati, modifikovati i prilagoditi prema svojim specifičnim potrebama. Ova pristupačnost stvara odličnu sredinu za učenje gde studenti i praktičari mogu istraživati stvarne PCB dizajne dok razvijaju svoje razumevanje elektronskih sistema. Mogućnost prilagođavanja vizuelnih elemenata poput logotipa pruža pristupačnu ulaznu tačku za korisnike koji mogu biti zastrašeni tehničkom složenošću elektronskog dizajna.


### Postavljanje Vašeg KiCad Okruženja


Pre nego što započnete bilo kakav rad na prilagođavanju, pravilno postavljanje vašeg razvojnog okruženja je od suštinskog značaja. Bitaxe repozitorijum mora biti preuzet na vaš lokalni računar, što se obično postiže putem GitHub-ove funkcionalnosti za preuzimanje ZIP datoteka. Ovaj repozitorijum sadrži sve potrebne projektne datoteke, uključujući KiCad projektne datoteke, biblioteke komponenti i dokumentaciju dizajna potrebnu za uspešnu modifikaciju.


Instalacija KiCad-a treba da bude završena korišćenjem zvanične distribucije sa KiCad vebsajta, kako bi se osigurala kompatibilnost sa projektnim fajlovima i pristup najnovijim funkcijama. Kada su i repozitorijum i KiCad pravilno instalirani, otvaranje projekta zahteva navigaciju do Bitaxe Ultra KiCad projektne datoteke unutar preuzete strukture repozitorijuma. Ova projektna datoteka služi kao centralni čvor koji povezuje sve povezane dizajnerske datoteke, biblioteke komponenti i podešavanja konfiguracije.


Početni pogled na složen dizajn PCB-a može delovati zastrašujuće, sa brojnim komponentama, tragovima i slojevima koji stvaraju gust vizuelni pejzaž. Međutim, KiCad-ova funkcionalnost 3D pregleda pruža neprocenjiv alat za razumevanje fizičkog rasporeda i prostornog odnosa unutar dizajna. Ova trodimenzionalna perspektiva pretvara apstraktni šematski prikaz u realističnu vizualizaciju konačnog proizvedenog proizvoda, olakšavajući razumevanje postavljanja komponenti i ukupne estetike dizajna.


### Proces prilagođavanja logotipa


Prilagođavanje logotipa na PCB dizajnima predstavlja jednu od najpristupačnijih modifikacija za korisnike koji su novi u KiCad-u, zahtevajući minimalno tehničko znanje dok pruža trenutne vizuelne rezultate. Proces počinje sa alatom za konverziju slika, koji transformiše standardne slikovne datoteke u formate otiska kompatibilne sa softverom za dizajn PCB-a. Ovaj proces konverzije zahteva pažljivo obraćanje pažnje na parametre veličine, koji se obično mere u milimetrima kako bi se osigurala pravilna skaliranje na konačno proizvedenoj ploči.


Radni tok pretvarača slika uključuje nekoliko kritičnih koraka koji određuju konačni izgled i postavljanje prilagođenih logotipa. Odabir izvorne slike treba da daje prioritet dizajnima visokog kontrasta koji će se dobro preneti na proces sito štampe koji se koristi u proizvodnji PCB-a. Specifikacija veličine postaje ključna, jer logotipi moraju biti dovoljno veliki da ostanu čitljivi nakon proizvodnje, a da ne ometaju postavljanje komponenti ili funkcionalnost. Izbor između prednjih i zadnjih slojeva sito štampe utiče i na vidljivost i na proizvodne razmatranja.


Upravljanje bibliotekom otisaka predstavlja osnovni aspekt prilagođavanja KiCad-a, što zahteva od korisnika da razumeju kako softver organizuje i pristupa elementima dizajna. Dodavanje prilagođenih logotipa uključuje kreiranje novih biblioteka otisaka ili modifikovanje postojećih, a zatim pravilno povezivanje ovih biblioteka unutar strukture projekta. Ovaj proces osigurava da prilagođeni elementi ostanu dostupni tokom različitih sesija dizajna i mogu se lako deliti sa drugim članovima tima ili saradnicima.


### Napredno istraživanje i razumevanje dizajna


Pored jednostavne prilagodbe logotipa, KiCad pruža moćne alate za istraživanje i razumevanje složenih PCB dizajna. Sistem upravljanja slojevima omogućava korisnicima selektivno pregledanje različitih aspekata dizajna, od postavljanja komponenti i rutiranja do specifikacija proizvodnje i informacija o montaži. Ovaj slojeviti pristup omogućava detaljnu analizu specifičnih elemenata dizajna bez vizuelnog nereda od nepovezanih komponenti.


Analiza rutiranja tragova predstavlja jedan od najedukativnijih aspekata istraživanja PCB-a, otkrivajući kako električne veze teku između komponenti i podsistema. Prateći pojedinačne tragove ili grupe povezanih signala, korisnici mogu razviti razumevanje funkcionalnosti kola i dizajnerskih odluka. Na primer, ispitivanje mreža za distribuciju napajanja otkriva kako komponente za regulaciju napona i filtriranje rade zajedno kako bi obezbedile čistu, stabilnu energiju za osetljive elektronske komponente.


Veza između shematskog dizajna i fizičkog rasporeda postaje očigledna kroz pažljivo ispitivanje postavljanja komponenti i odluka o rutiranju. Razumevanje zašto su određene komponente postavljene na određena mesta, kako termalni faktori utiču na odluke o rasporedu, i kako zahtevi za integritet signala usmeravaju izbore rutiranja pruža dragocene uvide u profesionalne prakse dizajna PCB-a. Ovo znanje se pokazuje neprocenjivim za korisnike koji razvijaju sopstvene dizajne ili modifikuju postojeće za specifične primene.


Sveobuhvatni alati za proveru i verifikaciju dizajnerskih pravila u KiCad-u osiguravaju da izmene zadrže električnu i proizvodnu kompatibilnost. Ovi automatizovani sistemi pomažu u sprečavanju uobičajenih grešaka u dizajnu dok istovremeno edukuju korisnike o industrijskim standardima i najboljim praksama. Integracija 3D vizualizacije sa podacima električnog dizajna stvara moćno okruženje za učenje gde teorijski koncepti postaju opipljivi kroz vizuelnu reprezentaciju i interaktivno istraživanje.


## Kako napraviti fabričku datoteku?

<chapterId>e9da631c-e6d1-50c1-bb59-bc8455c29d3e</chapterId>


:::video id=07f980bf-6052-4ed4-bf7b-75e8aba585df:::

Izrada prilagođenog firmvera za ESP-bazirane mining uređaje zahteva pažljivo obraćanje pažnje na konfiguraciju, zavisnosti i pravilan proces izgradnje. Ovaj sveobuhvatni vodič prolazi kroz kompletan proces kreiranja standardnih binarnih firmvera i fabričkih fajlova koji uključuju unapred konfigurisana podešavanja, čineći implementaciju efikasnijom i smanjujući vreme postavljanja za krajnje korisnike.


Imajte na umu da je ovo poglavlje prilično tehničko i možete ga jednostavno prelistati ako ste radoznali.


### Postavljanje razvojnog okruženja


Da biste započeli razvoj firmvera za ESP-Miner, trebali biste uspostaviti odgovarajuće razvojno okruženje u Visual Studio Code, idealno na linux distribuciji. ESP-IDF ekstenzija služi kao kamen temeljac ovog postava, pružajući potrebne alate i integraciju okvira za razvoj ESP32. Kada prvi put instalirate ESP-IDF ekstenziju, korisnici nailaze na vodič za postavljanje koji olakšava proces konfiguracije.


Kritična razmatranja u procesu postavljanja uključuju odabir odgovarajuće verzije ESP-IDF-a. Dok je verzija 5.1.3 ranije bila preporučena, praktično iskustvo je pokazalo da ova verzija može izazvati probleme pri izgradnji koji komplikuju proces razvoja. Preporučeni pristup sada uključuje korišćenje ESP-IDF verzije 5.3 Beta 1, koja se pokazala kao rešenje za ove komplikacije pri izgradnji i osigurava da Bitaxe uređaji funkcionišu ispravno. Proces instalacije zahteva odabir opcije Express instalacije i specifično biranje verzije 5.3 Beta 1 iz dostupnih opcija.


Postavljanje razvojnog okruženja prevazilazi samu instalaciju ESP-IDF-a i uključuje pravilnu konfiguraciju terminala. Visual Studio Code nudi više metoda za pristup ESP-IDF funkcionalnostima, uključujući opciju komandne palete za otvaranje ESP-IDF terminala ili korišćenje posebne ikone terminala koja se nalazi u interfejsu. Ovo specijalizovano terminalsko okruženje osigurava da svi ESP-IDF nalozi funkcionišu ispravno i omogućava pristup kompletnom alatu.


### Konfigurisanje ESP-Miner postavki


Konfiguraciona datoteka predstavlja srce procesa prilagođavanja ESP-Miner, sadržeći sve ključne parametre koji definišu kako će uređaj raditi u ciljanom okruženju. Ova konfiguracija obuhvata mrežna podešavanja, mining veze sa bazenom i parametre specifične za hardver koji moraju biti prilagođeni specifičnom scenariju implementacije.


Mreža konfiguracija čini primarnu komponentu procesa postavljanja, zahtevajući specifikaciju Wi-Fi akreditiva uključujući SSID i lozinku. Umesto korišćenja vrednosti kao što je "test," produkcijske konfiguracije treba da uključuju stvarne mrežne akreditive koje će uređaj koristiti u svom operativnom okruženju. Konfiguracija takođe podržava različite mining pool postavke, podržavajući i privatne pool konfiguracije sa specifičnim IP adresama i javne pool-ove kao što je public-pool.io sa odgovarajućim port postavkama.


Mining-specifični parametri konfiguracije uključuju postavku korisnika stratuma, koja obično odgovara adresi Bitcoin gde bi mining nagrade trebalo da budu usmerene. Dodatni hardverski parametri kao što su postavke frekvencije, konfiguracije napona i specifikacije tipa ASIC moraju biti usklađeni sa ciljanom hardverskom platformom. GitHub repozitorijum pruža unapred konfigurirane primere za različite hardverske varijante, kao što je BM1368 konfiguracija dizajnirana za Super uređaje i BM1366 postavke za Ultra varijante. Specifikacije verzije ploče, kao što je postavljanje verzije porta na 401 za novije hardverske revizije, osiguravaju kompatibilnost sa specifičnim karakteristikama ciljanog uređaja.


### Izgradnja Web Interface i Osnovnog Firmvera


Projekat ESP-Miner uključuje sofisticirani web interfejs koji zahteva zasebnu kompilaciju pre nego što proces izgradnje glavnog firmvera može da počne. Ovaj web interfejs, nazvan AxeOS firmver, korisnicima pruža sveobuhvatan upravljački interfejs za nadgledanje i kontrolu njihovih mining uređaja.


Proces izgradnje veb interfejsa počinje navigacijom do HTTP server direktorijuma unutar glavne strukture repozitorijuma, tačnije AxeOS poddirektorijuma. Ova lokacija sadrži veb aplikaciju zasnovanu na Node.js koja zahteva instalaciju zavisnosti putem npm install komande. Sistem za izgradnju pretpostavlja da je Node.js pravilno instaliran na razvojnom sistemu, jer ovo predstavlja osnovni zahtev za proces kompajliranja veb interfejsa.


Nakon instalacije zavisnosti, komanda npm run build kompajlira komponente web interfejsa, kreirajući potrebne fajlove koji će biti ugrađeni u ESP32 firmware. Ovaj proces kompajliranja generiše optimizovane web resurse koji obezbeđuju funkcionalnost korisničkog interfejsa, dok istovremeno održavaju efikasno korišćenje memorije na ograničenoj ESP32 platformi. Uspešan završetak ovog koraka izgradnje je ključan pre nego što se pređe na glavnu kompilaciju firmware-a, jer ESP-Miner firmware uključuje ove komponente web interfejsa kao integralnu funkcionalnost.


### Kreiranje fabričkih datoteka sa ugrađenom konfiguracijom


Kreiranje fabričkih datoteka predstavlja naprednu strategiju implementacije koja ugrađuje postavke konfiguracije direktno u binarni firmware, eliminišući potrebu za ručnom konfiguracijom tokom postavljanja uređaja. Ovaj pristup se pokazuje posebno vrednim za implementacije velikih razmera ili situacije gde je dosledna konfiguracija na više uređaja od suštinskog značaja.


Proces kreiranja fabričke datoteke počinje generisanjem binarne konfiguracije iz CSV konfiguracione datoteke koristeći ESP-IDF alat za generisanje NVS particije. Ovaj alat, koji se nalazi unutar ESP-IDF direktorijuma komponenti pod nvs-flash/nvs-partition-generator, konvertuje konfiguraciju čitljivu za ljude u binarni format pogodan za direktno skladištenje u fleš memoriji. Skripta nvs-partition-gen.py obrađuje config.csv datoteku i generiše config.binary datoteku koja cilja memorijski prostor na adresi 0x6000.


Konačna montaža fabričkih fajlova koristi specijalizovane skripte za spajanje koje kombinuju osnovne binarne datoteke firmvera sa podacima o konfiguraciji. Repozitorijum pruža više opcija za spajanje, uključujući standardnu skriptu za spajanje za osnovne fabričke fajlove i skriptu za spajanje sa konfiguracijom za sveobuhvatne fabričke fajlove. Skripta merge-bin-with-config.sh kreira fabričke fajlove koji uključuju i funkcionalnost firmvera i unapred podešena podešavanja, što rezultira kompletnim paketom za implementaciju. Ovaj pristup omogućava kreiranje fabričkih fajlova specifičnih za uređaje, kao što su verzije prilagođene za Bitaxe Ultra uređaje sa specifičnim revizijama ploča, dok se zadržava fleksibilnost za generate generičke fabričke fajlove bez ugrađenih konfiguracija za scenarije koji zahtevaju fleksibilnost ručnog podešavanja.


Dovršene fabričke datoteke obezbeđuju timovima za implementaciju spremne binarne datoteke za flešovanje koje uključuju sve potrebne komponente firmvera i postavke konfiguracije, pojednostavljujući proces obezbeđivanja uređaja i osiguravajući dosledne operativne parametre na svim implementiranim mining uređajima.


## Kako koristiti Bitaxe Web Flasher?

<chapterId>8c3e2d4c-c038-53ec-93cb-cc30a29e4394</chapterId>


:::video id=291757b9-f459-48f6-8766-56387f907859:::

Bitaxe Web Installer predstavlja pojednostavljen pristup upravljanju firmverom za Bitaxe uređaje, pružajući korisnicima više opcija za instalaciju putem web interfejsa. Ovaj sveobuhvatni alat eliminiše složenost koja je tradicionalno povezana sa ažuriranjima firmvera i novim instalacijama, čineći upravljanje uređajima dostupnim korisnicima bez obzira na njihovu tehničku stručnost. Razumevanje pravilne upotrebe ovog instalatera je ključno za održavanje optimalnih performansi uređaja i izbegavanje uobičajenih problema koji mogu privremeno učiniti uređaje neupotrebljivim.


### Pristup i zahtevi za kompatibilnost pretraživača


Bitaxe Web Installer je dostupan putem posvećenog URL-a [https://bitaxeorg.github.io/bitaxe-web-flasher/](https://bitaxeorg.github.io/bitaxe-web-flasher/) (onaj prikazan u videu je sada zastareo), služeći kao centralno mesto za sve aktivnosti instalacije firmvera. Međutim, uspešno funkcionisanje ovog alata zasnovanog na vebu zahteva kompatibilnost pretraživača, jer se instalater oslanja na specifične veb tehnologije koje nisu univerzalno podržane u svim pretraživačima. Chrome je primarni preporučeni pretraživač za instalater, pružajući punu kompatibilnost sa svim funkcijama i mogućnostima. Iako drugi pretraživači zasnovani na Chromium-u mogu ponuditi sličnu funkcionalnost, popularne alternative kao što su Brave i Firefox nemaju potrebnu podršku za web serial API, što ih čini nekompatibilnim sa osnovnim operacijama instalatera.


Ovo ograničenje pretraživača proizlazi iz oslanjanja instalatera na direktnu serijsku komunikaciju sa Bitaxe uređajima putem web interfejsa. Web serijski API, koji omogućava ovu komunikaciju, ostaje relativno novi web standard koji još nije postigao univerzalno usvajanje među pretraživačima. Korisnici koji pokušavaju pristupiti instalateru putem nepodržanih pretraživača će naići na probleme sa povezivanjem i nemogućnost komunikacije sa svojim uređajima, što zahteva prelazak na kompatibilni pretraživač pre nego što nastave sa bilo kakvim aktivnostima instalacije.


### Zahtevi za napajanje i priprema uređaja


Bitaxe uređaji pokazuju različite zahteve za napajanje u zavisnosti od specifičnog modela i verzije, što čini pravilno upravljanje napajanjem ključnim za uspešnu instalaciju firmvera. Uređaji koji koriste verziju 204 ili nižu mogu raditi isključivo preko USB napajanja, crpeći dovoljno struje iz povezanog računara da održe rad tokom procesa flešovanja. Ovaj pojednostavljeni aranžman napajanja čini ove ranije verzije posebno pogodnim za ažuriranja firmvera, jer korisnici trebaju samo povezati jedan USB kabl da bi započeli proces instalacije.


Međutim, uređaji koji koriste verziju 205 i novije zahtevaju spoljne izvore napajanja pored USB veze, što odražava promene u potrošnji energije i dizajnu kola u novijim revizijama hardvera. Ovi uređaji ne mogu crpiti dovoljno energije samo putem USB-a, što zahteva povezivanje sa njihovim standardnim napajanjem tokom instalacije firmvera. Nedostatak adekvatnog napajanja za ove novije uređaje dovešće do neuspeha instalacije i potencijalnog oštećenja procesa ažuriranja firmvera.


Proces fizičkog povezivanja zahteva specifično tempiranje i manipulaciju dugmićima kako bi se osigurala pravilna komunikacija između instalatera i uređaja. Korisnici moraju pritisnuti i držati boot dugme na svom Bitaxe uređaju pre nego što povežu USB-C kabl sa svojim računarom. Ova sekvenca stavlja uređaj u bootloader režim, omogućavajući instalateru da direktno komunicira sa skladištem firmvera uređaja. Povezivanje USB kabla pre aktiviranja boot dugmeta rezultiraće normalnim radom uređaja umesto potrebnog bootloader režima za instalaciju firmvera, sprečavajući instalatera da uspostavi neophodan komunikacioni kanal.


### Opcije instalacije i njihove primene


Bitaxe Web Installer pruža četiri različite opcije instalacije, svaka dizajnirana za specifične slučajeve upotrebe i konfiguracije uređaja. Bitaxe Superboard verzija 4.0.1 predstavlja najnoviji firmware za Super model uređaje, dok je verzija 4.0.2 planirana za buduće izdanje. Ova opcija uključuje i fabričke i ažurirane varijante, pružajući fleksibilnost u pristupu instalaciji na osnovu potreba korisnika i statusa uređaja.


Instalacije iz fabrike predstavljaju kompletne zamene firmvera koje odražavaju originalni proces proizvodnje, uključujući sveobuhvatne procedure samoprovere koje verifikuju funkcionalnost uređaja preko svih sistema. Kada korisnici odaberu instalaciju iz fabrike, instalater vrši potpuno brisanje postojećeg firmvera i podataka o konfiguraciji, zamenjujući ih svežom, čistom instalacijom identičnom onoj koja bi bila primenjena tokom proizvodnje. Ovaj proces uključuje automatizovanu samoproveru koja potvrđuje ispravan rad hardvera, zahtevajući od korisnika da ponovo pokrenu svoje uređaje po završetku pre nego što normalan rad može da se nastavi. Instalacije iz fabrike su posebno vredne kada uređaji imaju uporne probleme ili kada korisnici žele da vrate svoje uređaje na originalne fabričke specifikacije.


Ažuriranje instalacija pruža konzervativniji pristup, očuvajući postojeće konfiguracione podatke dok ažurira samo osnovne komponente firmvera. Ova opcija je idealna za korisnike koji su prilagodili postavke svog uređaja i žele da zadrže svoje lične konfiguracije dok istovremeno koriste poboljšanja firmvera i ispravke grešaka. Proces ažuriranja cilja samo one komponente firmvera koje zahtevaju modifikaciju, ostavljajući korisnički specifične postavke, WiFi akreditive i Bitcoin adrese netaknutim tokom celog procesa instalacije.


### Kritični razlozi za instalaciju i zaštitu podataka


Razlika između fabričkih i ažurirajućih instalacija nosi značajne implikacije za konfiguraciju uređaja i očuvanje korisničkih podataka. Fabričke instalacije vrše potpuno brisanje uređaja, uklanjajući sve korisnički konfigurisane postavke uključujući WiFi akreditive, Bitcoin adrese i bilo koje personalizovane parametre uređaja. Nakon fabričke instalacije, korisnici moraju ponovo da se povežu na podrazumevanu WiFi mrežu uređaja i rekonfigurišu sve lične postavke ispočetka, tretirajući uređaj kao da je potpuno nov od proizvođača.


Ažuriranje instalacija zahteva pažljivo obraćanje pažnje na opciju brisanja uređaja koja se prikazuje tokom procesa instalacije. Instalater će korisnicima postaviti pitanje "Da li želite da obrišete uređaj pre instalacije Bitaxe Flasher-a?" uz upozorenje da će svi podaci na uređaju biti izgubljeni. Korisnici koji vrše ažuriranje instalacija moraju odbiti ovu opciju klikom na "Next" umesto da potvrde operaciju brisanja. Prihvatanje opcije brisanja tokom ažuriranja instalacije ukloniće konfiguracioni fajl uređaja, što može učiniti uređaj nefunkcionalnim dok se ne vrati ispravna konfiguracija. Iako ova situacija ne oštećuje trajno uređaj, stvara nepotrebne komplikacije i zahteva dodatne korake konfiguracije za vraćanje normalnog rada.


Sam proces instalacije odvija se automatski kada korisnici naprave svoje izbore i potvrde svoje odluke. Instalacijski program upravlja svim tehničkim aspektima prenosa i verifikacije firmvera, pružajući indikatore napretka i ažuriranja statusa tokom celog procesa. Ovaj automatizovani pristup eliminiše potrebu da korisnici razumeju složene procedure instalacije firmvera, dok obezbeđuje pouzdane i dosledne rezultate na različitim modelima uređaja i verzijama firmvera.


## Kako kreirati i naručiti PCB?

<chapterId>566f5e06-9ec9-55c0-84f6-101d6ca4c2ff</chapterId>


:::video id=9a56ad84-d9cf-4f85-ab98-301fb3101228:::

Ovo poglavlje se fokusira na praktičan proces generisanja proizvodnih fajlova iz KiCad projekata i naručivanje profesionalnih PCB-ova od online proizvođača. Koristeći projekat Bitaxe kao naš primer, proći ćemo kroz kompletan tok rada od generisanja fajlova do postavljanja narudžbine kod proizvođača PCB-ova.


### Razumevanje procesa proizvodnje PCB-a


Put od završenog KiCad dizajna do fizičkog PCB-a uključuje nekoliko kritičnih koraka koji premošćuju jaz između digitalnog dizajna i fizičke proizvodnje. Kada radite na složenim projektima kao što je Bitaxe, PCB editor u KiCad-u pruža sveobuhvatan pregled vašeg dizajna, prikazujući sve komponente i njihove međusobne veze kroz obojene tragove. Crvene i plave linije koje vidite predstavljaju električne veze između različitih integrisanih kola i komponenti na ploči. KiCad-ova funkcija 3D pregleda omogućava vam da vizualizujete kako će konačna sastavljena ploča izgledati, pružajući dragocene uvide u postavljanje komponenti i potencijalne mehaničke sukobe.


Proces proizvodnje zahteva specifične formate fajlova koje proizvođači PCB-a mogu interpretirati i koristiti za izradu vaših ploča. Ovi fajlovi sadrže precizne informacije o slojevima bakra, bušotinama, postavljanju komponenti i drugim specifikacijama proizvodnje. Razumevanje ovog toka rada je ključno bilo da radite sa standardnim Bitaxe dizajnom ili pravite izmene kao što su dodavanje prilagođenih logotipa, promena vrednosti komponenti ili prilagođavanje rasporeda ploče kako bi ispunili specifične zahteve.


### Generisanje Gerber fajlova za proizvodnju


Gerber datoteke služe kao industrijski standard za komunikaciju informacija o dizajnu PCB-a proizvođačima. Ove datoteke sadrže sve potrebne podatke za izradu vašeg PCB-a, uključujući obrasce bakarnih slojeva, definicije maske za lemljenje i lokacije rupa za bušenje. Da biste generate ove datoteke u KiCad-u, idite na PCB editor i pristupite izlazima za izradu kroz meni Files. Softver automatski konfiguriše odgovarajuće postavke za standardne proizvodne procese, uključujući odgovarajuću strukturu izlaznog direktorijuma koja je obično organizovana kao "manufacturing files/gerbers."


Proces generisanja kreira više Gerber fajlova, od kojih svaki predstavlja različite aspekte vašeg PCB dizajna. Ovi fajlovi rade zajedno kako bi proizvođačima pružili kompletna uputstva za izradu. Kada se generišu, ovi fajlovi moraju biti kompresovani u ZIP arhivu, jer je to standardni format koji očekuje većina proizvođača PCB-a. ZIP fajl sadrži sve potrebne podatke za proizvodnju i osigurava da nijedan fajl ne bude izgubljen ili oštećen tokom procesa otpremanja na vebsajt proizvođača.


Vredi napomenuti da mnogi open-source projekti, uključujući Bitaxe, često uključuju unapred generisane proizvodne fajlove u svojim repozitorijumima. Međutim, razumevanje kako sami da generate ove fajlove je ključno kada pravite izmene u dizajnu ili radite sa različitim verzijama ploča. Ovo znanje postaje posebno vredno kada prilagođavate dizajne ili rešavate probleme u proizvodnji.


### Odabir proizvođača PCB-a i razumevanje opcija


Pejzaž proizvodnje PCB-a nudi nekoliko renomiranih opcija, pri čemu su JLCPCB i PCBWay među najpopularnijim izborima kako za hobiste, tako i za profesionalce. Oba proizvođača pružaju slične usluge sa konkurentnim cenama i pouzdanim kvalitetom, iako svaki ima specifične prednosti u zavisnosti od zahteva vašeg projekta. JLCPCB često privlači korisnike koji prvi put koriste njihove usluge promotivnim cenama i korisnički prijatnim interfejsima, dok PCBWay može ponuditi različite opcije materijala ili specijalizovane usluge.


Kada otpremate svoje Gerber fajlove na veb-sajt proizvođača, sistem automatski analizira vaš dizajn i prikazuje različite opcije proizvodnje. Podrazumevana podešavanja koja nude ove platforme obično su pogodna za većinu standardnih dizajna, i generalno se preporučuje da zadržite ova podešavanja osim ako nemate specifične zahteve. Ključni parametri uključuju debljinu PCB-a, težinu bakra, završnu obradu površine i minimalne količine. Većina proizvođača zahteva minimalne porudžbine od pet ploča, što zapravo dobro funkcioniše za projekte hobista gde je korisno imati rezervne ploče ili ih deliti sa prijateljima.


Opcije boja predstavljaju jedan od retkih estetskih izbora dostupnih tokom procesa proizvodnje. Dok zelena ostaje tradicionalna i najisplativija opcija, proizvođači obično nude alternative uključujući plavu, crvenu, žutu, ljubičastu i crnu. Izbor boje je isključivo estetski i ne utiče na električne performanse vašeg PCB-a, iako neke boje mogu imati blage troškovne implikacije ili duže vreme proizvodnje.


### Napredna razmatranja proizvodnje i opcije sklapanja


Pored osnovne izrade PCB-a, moderni proizvođači nude dodatne usluge koje mogu značajno ubrzati završetak vašeg projekta. Šabloni predstavljaju jednu od najvrednijih dodatnih usluga, posebno za dizajne sa komponentama finog rastera kao što su ASIC čipovi koji se nalaze u projektima Bitcoin mining. Šablon je u suštini precizno izrezan aluminijumski kalup sa otvorima koji tačno odgovaraju lokacijama lemljenih podloga na vašem PCB-u. Ovaj alat omogućava doslednu i preciznu primenu lemne paste, dramatično poboljšavajući kvalitet sklapanja i smanjujući verovatnoću grešaka u lemljenju.


Opcije za šablone obično uključuju pojedinačne šablone sa uzorcima za gornju i donju stranu, ili odvojene šablone za svaku stranu ploče. Za većinu projekata, kombinovana šablona se pokazuje kao pogodnija i isplativija. Debljina šablone se pažljivo izračunava kako bi se nanela odgovarajuća količina lemne paste za vaše specifične tipove komponenti i veličine padova. Korišćenje šablone pretvara ono što bi moglo biti zamoran i sklon greškama ručni proces u brz i profesionalan korak sklapanja.


Iako neki proizvođači nude usluge delimične ili potpune montaže, ove opcije zahtevaju pažljivo razmatranje za složene projekte poput Bitaxe-a. Dostupnost komponenti, troškovi i obrazovna vrednost samostalne montaže svi utiču na ovu odluku. Mnoge specijalizovane komponente potrebne za Bitcoin mining projekte možda neće biti lako dostupne putem standardnih usluga montaže PCB-a, što čini nabavku komponenti i ručnu montažu praktičnijim pristupom. Buduće epizode u ovoj seriji će pokriti strategije nabavke komponenti i tehnike montaže kako bi vam pomogle da uspešno završite vaš Bitaxe projekat od praznog PCB-a do funkcionalnog uređaja.


Proces proizvodnje i montaže predstavlja ključni most između digitalnog dizajna i fizičke implementacije. Razumevanje ovih tokova rada omogućava vam da preuzmete kontrolu nad svojim projektima, smanjite troškove i steknete dragoceno praktično iskustvo sa profesionalnim proizvodnim procesima. Bilo da pravite jedan prototip ili planirate malu serijsku proizvodnju, ovladavanje ovim veštinama otvara nove mogućnosti za oživljavanje vaših elektronskih dizajna.


# Optimizacija performansi

<partId>87b8790f-b7a9-5286-a7f8-328176ef7cb5</partId>


## Uporedite svoj Bitaxe

<chapterId>7259a4b1-93c1-5956-87d3-baaee58115af</chapterId>


:::video id=2491a783-9750-4ea5-a40c-1d1d611784d5:::

Potraga za optimalnim performansama mining zahteva sistematski pristup konfiguraciji hardvera koji balansira hashrate, efikasnost i termalno upravljanje. Bitaxe nudi brojne parametre konfiguracije koji mogu značajno uticati na performanse, ali ručno testiranje svake kombinacije podešavanja bilo bi nepraktično i vremenski zahtevno. Ovo poglavlje istražuje kako iskoristiti automatizovane alate za benchmarking da naučno optimizujete performanse vašeg Bitaxe-a, dok održavate bezbedne uslove rada.


### Razumevanje Bitaxe performansnih metrika i osnovne konfiguracije


Pre nego što se upustite u tehnike optimizacije, neophodno je razumeti ključne pokazatelje performansi koji definišu operativnu efikasnost vašeg Bitaxe-a. Primarne metrike uključuju hashrate merenu u terahašima po sekundi, energetsku efikasnost izraženu u džulima po terahašu, ASIC frekvenciju u megahercima i napon jezgra u voltima. Dobro konfigurisani Bitaxe može postići približno 1.1 terahaš sa efikasnošću od oko 17 džula po terahašu, radeći na 550 megaherca sa izmerenim ASIC naponom od 1.14 volti. Ove osnovne brojke pružaju referentnu tačku za razumevanje potencijalnih poboljšanja dostupnih kroz sistematsku optimizaciju.


Odnos između ovih metrika je složen i međuzavisan. Veće frekvencije obično povećavaju hashrate, ali takođe povećavaju potrošnju energije i generisanje toplote. Slično tome, podešavanja napona utiču i na performanse i na termalne karakteristike. Izazov leži u pronalaženju optimalne ravnoteže koja maksimizira ili hashrate ili efikasnost, dok se održava stabilan rad unutar bezbednih temperaturnih granica. Ovaj proces optimizacije zahteva metodičko testiranje kroz više kombinacija parametara, što čini automatizovane alate neprocenjivim za postizanje optimalnih rezultata.


### Bitaxe Hashrate Benchmark Tool Architecture


[Bitaxe Hashrate Benchmark](https://github.com/mrv777/Bitaxe-Hashrate-Benchmark/) alat predstavlja sofisticirano rešenje zasnovano na Python-u, koje je prvobitno razvio WhiteCookie, a kasnije unapredio mrv777. Ovaj alat otvorenog koda, distribuiran pod GPLv3 licencom, automatizuje složen proces testiranja više kombinacija konfiguracija kako bi identifikovao optimalna podešavanja za vaš specifičan hardver. Primarna snaga alata leži u njegovom sistematskom pristupu testiranju parametara, postepeno podešavajući frekvenciju i naponske postavke dok kontinuirano prati performanse i termalne uslove.


Proces benchmarking-a obično zahteva 30 do 40 minuta za završetak, tokom kojeg alat metodično testira različite kombinacije frekvencije i naponskih podešavanja ASIC. Alat počinje sa konzervativnim osnovnim podešavanjima, obično počevši od 1.15 volti i 500 megaherca, zatim postepeno povećava ove parametre dok prati hashrate, temperaturu i stabilnost. Važno je napomenuti da alat daje prioritet bezbednom radu u odnosu na maksimalne performanse, automatski smanjujući podešavanja koja uzrokuju prekomerno generisanje toplote ili nestabilnost. Ovaj konzervativni pristup osigurava da proces optimizacije ne ugrožava dugovečnost ili pouzdanost hardvera.


### Zahtevi za instalaciju i podešavanje


Implementacija alata Bitaxe Hashrate Benchmark zahteva nekoliko softverskih komponenti na vašem lokalnom računaru. Primarni zahtevi uključuju Python za izvršavanje skripti za benchmarking, Git za upravljanje repozitorijumima, i opcionalno Visual Studio Code za poboljšane mogućnosti razvojnog okruženja. Iako se alat može koristiti iz komandne linije, korišćenje integrisanog razvojnog okruženja kao što je VS Code pruža bolju preglednost procesa benchmarkinga i analize rezultata.


Proces instalacije prati standardne prakse razvoja u Python-u, počevši od kloniranja repozitorijuma sa GitHub-a na vaš lokalni računar. Kada se repozitorijum preuzme, potrebno je kreirati virtuelno okruženje kako biste izolovali zavisnosti alata od Python instalacije na vašem sistemu. Ova izolacija sprečava potencijalne konflikte sa drugim Python aplikacijama i osigurava dosledan rad. Nakon aktivacije virtuelnog okruženja, instaliraćete potrebne zavisnosti koristeći priloženi fajl sa zahtevima, koji automatski konfiguriše sve neophodne biblioteke i module za pravilno funkcionisanje alata.


### Izvršavanje benchmark testova i tumačenje rezultata


Pokretanje benchmarka zahteva izvršavanje jedne Python komande koja uključuje IP adresu vašeg Bitaxe-a kao parametar. Alat se automatski povezuje na web interfejs vašeg minera i započinje sistematski proces testiranja. Tokom izvršavanja, alat pruža detaljne informacije o logovanju koje prikazuju trenutnu iteraciju testa, primenjene postavke napona i frekvencije, rezultujući hashrate, ulazni napon, očitavanja temperature i termalne podatke sa kritičnih komponenti kao što je buck konverter. Ova povratna informacija u realnom vremenu omogućava vam da pratite napredak benchmarkinga i razumete kako različite postavke utiču na performanse vašeg minera.


Inteligentno upravljanje toplotom alata postaje očigledno kada temperature dostignu sigurnosni prag od 66 stepeni Celzijusa. Umesto da prelazi bezbedne operativne granice, referentna vrednost automatski smanjuje postavke kako bi održala toplotnu stabilnost. Ovaj konzervativni pristup osigurava da proces optimizacije daje prioritet dugoročnoj pouzdanosti hardvera nad kratkoročnim dobicima u performansama. Po završetku, alat generiše sveobuhvatne rezultate u JSON formatu, rangirajući prvih pet konfiguracija za maksimalni hashrate i optimalnu efikasnost. Ovi rezultati pružaju jasne smernice za odabir konfiguracije koja najbolje odgovara vašim operativnim prioritetima, bilo da se fokusirate na maksimalni izlaz ili energetsku efikasnost.


Alat za benchmarking takođe nudi opcije prilagođavanja za napredne korisnike koji žele da modifikuju parametre testiranja. Argumenti komandne linije omogućavaju vam da navedete prilagođene početne napone i frekvencije, omogućavajući ciljanu optimizaciju za specifične slučajeve upotrebe. Na primer, ako već znate da vaš hardver dobro radi na višim frekvencijama, možete započeti benchmark na povišenim postavkama umesto da počinjete od konzervativnih podrazumevanih vrednosti. Ova fleksibilnost čini alat vrednim i za početnike koji traže automatsku optimizaciju i za iskusne rudare koji žele da fino podešavaju specifične karakteristike performansi.


## Overklokuj svoj Bitaxe

<chapterId>6b48c0c6-51c3-51a3-b317-850a374ae61e</chapterId>


:::video id=46c7a442-cd72-477c-8c91-b2c489ada1e6:::

Overclocking a Bitaxe uređaja zahteva pažljivo razmatranje kako hardverskih ograničenja, tako i zahteva za hlađenjem. Dok mnogi korisnici preferiraju da podtaktuju svoje uređaje radi tišeg rada, razumevanje pravilnih tehnika overclockinga je ključno za one koji traže maksimalne performanse bez oštećenja hardvera. Proces uključuje povećanje frekvencije i potencijalno podešavanje naponskih postavki iznad fabričkih specifikacija, što inherentno povećava generisanje toplote i stres na komponentama.


Osnova uspešnog overklokovanja leži u adekvatnoj infrastrukturi za hlađenje. Pre nego što pokušate bilo kakve modifikacije frekvencije, morate osigurati da vaš Bitaxe ima odgovarajuće sposobnosti za odvođenje toplote. Bitaxe Gamma sa kvalitetnim hladnjakom i ventilatorom pruža neophodno termalno upravljanje za sigurno overklokovanje. Uređaji sa malim hladnjacima i neadekvatnim ventilatorima ne bi trebalo da se overklokuju, jer loše performanse hlađenja će dovesti do termalnog ograničavanja i potencijalnog oštećenja hardvera. Odnos između toplote i dugovečnosti komponenti je kritičan za razumevanje—prekomerna toplota stvara stres koji vremenom degradira elektronske komponente, značajno smanjujući operativni vek vašeg uređaja.


### Strateško postavljanje hladnjaka


Najkritičnija komponenta koja zahteva dodatno hlađenje je buck konverter, mali crni element smešten na zadnjoj strani Bitaxe-a, blizu velike zavojnice. Ovaj uređaj pretvara ulazno napajanje od 5V na odgovarajući napon za ASIC čip, obično oko 1.2V. Buck konverter, često nazivan TPS, generiše značajnu toplotu tokom rada i predstavlja termalno usko grlo koje ograničava potencijal za overkloking. Postavljanje malog lepljivog hladnjaka na ovu komponentu ne samo da omogućava veći prostor za overkloking, već i poboljšava ukupnu efikasnost smanjenjem termalnih gubitaka.


Dodatno postavljanje hladnjaka može koristiti drugim područjima ploče sa visokim strujama. Kolo za regulaciju napona doživljava značajan električni stres dok struja teče iz ulaznog dela kroz razne tragove ploče kako bi napajala ASIC čip. Mnogi iskusni overklokeri postavljaju hladnjake na prednji deo Bitaxe-a u ovim područjima sa visokim strujama kako bi dodatno poboljšali termalnu disipaciju. Iako nije strogo neophodno za umereno overklokovanje, ove dodatne mere hlađenja postaju važne kada se frekvencije guraju na ekstremne nivoe.


### Razmatranja i ograničenja rashladnog sistema


Kontroler ESP32, vidljiv kao srebrnasti deo na ploči, obično ne zahteva dodatno hlađenje. Ova komponenta sama po sebi generiše minimalnu toplotu i postaje topla samo zbog prenosa toplote sa okolnih komponenti. Postavljanje hladnjaka blizu ESP32 može potencijalno ometati susednu Wi-Fi antenu, pogoršavajući bežičnu povezanost i kvalitet signala. Usmerite napore hlađenja na komponente za regulaciju napajanja i oblast ASIC, a ne na kontrolnu elektroniku.


Dvostruke konfiguracije ventilatora predstavljaju i mogućnosti i ograničenja. Dok dodavanje drugog ventilatora koji duva vazduh preko zadnje strane Bitaxe-a može poboljšati performanse hlađenja, firmware uređaja može pravilno kontrolisati samo jedan ventilator. Bitaxe ima dva priključka za ventilatore, ali samo jedan kontroler ventilatora, što znači da povezivanje dva ventilatora može zbuniti firmware jer prima konfliktne signale o RPM-u. Ova konfiguracija će funkcionisati, ali može rezultirati nepredvidivim ponašanjem kontrole ventilatora.


### Procena Osnovnih Performansi


Pre nego što pokušate bilo kakve modifikacije overclockinga, uspostavite osnovne performanse tako što ćete pokrenuti svoj Bitaxe na fabričkim podešavanjima nekoliko sati. Pratite temperaturu ASIC, temperaturu regulatora napona i procenat brzine ventilatora putem web interfejsa. Optimalne radne temperature treba da održavaju ASIC ispod 60°C i regulator napona ispod 60°C u normalnim uslovima. Ako vaš uređaj već radi iznad 65°C na ASIC ili 70-80°C na regulatoru napona pri fabričkim podešavanjima, dodatni hardver za hlađenje je obavezan pre nego što nastavite sa overclockingom.


Sistematski pristup povećanju frekvencije uključuje inkrementalne korake koristeći unapred definisane opcije frekvencije u meniju podešavanja. Počnite tako što ćete izabrati sledeći dostupan korak frekvencije iznad vaše trenutne postavke, dok održavate podrazumevani napon jezgra. Ovaj konzervativni pristup vam omogućava da procenite termalne i stabilnosne uticaje pre nego što napravite dodatne promene. Dozvolite uređaju da radi na svakoj novoj postavci frekvencije najmanje 30 minuta do jedan sat, prateći temperaturne trendove i stabilnost hash rate-a tokom perioda evaluacije.


### Napredna prilagođena konfiguracija


Pristup prilagođenim postavkama frekvencije i napona zahteva omogućavanje naprednog interfejsa za overklokovanjem dodavanjem "?OC" na URL veb interfejsa uređaja. Ovo otključava polja za ručni unos za preciznu kontrolu frekvencije i napona, uz odgovarajuća upozorenja o rizicima rada van projektovanih parametara. Prilagođeni interfejs omogućava fino podešavanje izvan standardnih koraka frekvencije, omogućavajući iskusnim korisnicima da optimizuju performanse za svoje specifične konfiguracije hlađenja.


Kada koristite prilagođena podešavanja, održavajte konzervativne veličine povećanja od 10-15 MHz po koraku podešavanja. Ovaj metodičan pristup sprečava nagle termalne skokove i omogućava pravilno testiranje stabilnosti na svakom nivou frekvencije. Neki napredni korisnici postižu frekvencije oko 700 MHz sa naponom jezgra podešenim na 1.175V ili slične vrednosti, ali ova ekstremna podešavanja zahtevaju opsežne modifikacije hlađenja i pažljivo praćenje. Regulator napona može raditi na temperaturama do 100°C bez trenutnog oštećenja, ali više temperature smanjuju efikasnost i dugoročnu pouzdanost. Uspešno overklokovanje zahteva strpljenje, sistematsko testiranje i kontinuirano praćenje kako bi se postigla stabilna poboljšanja performansi uz očuvanje integriteta hardvera.


# Završni deo

<partId>33367393-17a7-58d4-8359-79fffc6221fb</partId>


## Proceni ovaj kurs

<chapterId>785f8b92-c8a6-5a65-aa39-e9753a7edf51</chapterId>

<isCourseReview>true</isCourseReview>

## Zaključak

<chapterId>758baee6-2404-56fb-b534-6a39e441ae29</chapterId>

<isCourseConclusion>true</isCourseConclusion>