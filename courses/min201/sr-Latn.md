---
name: Uvod u rudarenje Bitcoin-a
goal: Razumevanje funkcionisanje industrije rudarenja kroz praktičnu vežbu ponovnog korišćenja ASIC-a.
objectives: 

  - Razumeti teoriju iza rudarenja
  - Razumeti industriju rudarenja
  - Pretvorite S9 u grejač
  - Izrudarite svoj prvi Satoshi

---

# Vaši prvi koraci u rudarenju!


U ovoj obuci, istražićemo industriju rudarenja kako bismo demistifikovali ovu složenu temu! Obuka je dostupna svima i ne zahteva početno ulaganje.


Prvi deo će biti teoretski, gde ćemo Ajelex i ja imati detaljnu diskusiju o raznim temama vezanim za rudarenje. Ovo će nam pomoći da bolje razumemo ovu industriju i ekonomska i geopolitička pitanja povezana s njom.

U drugom delu, bavićemo se praktičnim slučajem. Zaista, naučićemo kako da transformišemo korišćeni S9 mašinu za rudarenje u sistem za grejanje doma! Kroz pisane vodiče i video snimke, pokazaćemo i objasniti sve korake kako biste to postigli kod kuće :)


Kroz ovaj video, nadamo se da ćemo vam pokazati da je industrija rudarenja složenija nego što se čini, a njeno proučavanje pomaže u nijansiranju ekološke debate koja je s njom povezana!

Ako vam je potrebna pomoć oko postavljanja, kreirana je Telegram grupa za studente, a sve potrebne komponente možete pronaći na našoj e-commerce platformi!


+++

# Uvod


<partId>a99dc130-3650-563f-8d42-a0b5160af0ab</partId>


## Pregled kursa


<chapterId>7ad1abeb-a190-5c85-8bff-44df71331e4d</chapterId>


Dobrodošli na kurs MIN201: Uvod u rudarenje. Ajelex, Jim & Rogzy su uzbuđeni da vas vode kroz vaše prve korake u ovoj industriji. Nadamo se da ćete uživati u kursu i krenuti u avanturu rudarenja kod kuće!


Ova obuka vas vodi u srce industrije Bitcoin rudarenja, pružajući i teorijsko i praktično znanje. Bilo da ste početnik ili već upoznati sa temom, ovaj kurs će vam pomoći da razumete ekonomske i tehničke aspekte rudarenja, dok završavate praktični projekat prenamene ASIC-a za grejanje doma.


**Sekcija 2: Sve o rudarenju**

U ovom odeljku, pružićemo sveobuhvatno razumevanje Bitcoin rudarenja. Pokrićemo tehničko funkcionisanje rudarenja, njegovu ulogu u Bitcoin protokolu, kao i ekonomske i geopolitičke implikacije. Takođe ćete istražiti složen odnos između cene Bitcoin-a i Hashrate-a, kao i pitanja vezana za suverenitet i regulaciju u industriji.


**Sekcija 3: Kućno rudarenje i ponovna upotreba toplote**

Dalje ćemo se upustiti u praktičnu primenu Attakai koncepta, koji ima za cilj da demokratizuje rudarenje kod kuće transformacijom korišćenih S9 uređaja u uređaje za grejanje doma. Naučićete kako da kupite i modifikujete korišćeni ASIC, dok pripremate neophodnu opremu za hardverske modifikacije.


**Section 4: Attakai - Modifikovanje Antminer S9 softvera**

Ovde ćete naučiti kako da konfigurišete vaš Antminer S9 za kućnu upotrebu. Provešćemo vas kroz podešavanje Wi-Fi/Ethernet mosta, resetovanje vašeg uređaja, instalaciju BraiinsOS+, i optimizaciju za najbolju efikasnost rudarenja.


**Sekcija 5: Attakai - Modifikacije od strane fanova**

Da biste optimizovali vaš Antminer S9 za korišćenje kao pomoćni grejač, ovaj deo će vas naučiti kako da zamenite ventilatore za napajanje i glavne ventilatore. Ove modifikacije su ključne za smanjenje buke i poboljšanje termalne efikasnosti uređaja.


**Section 6: Attakai - Konfiguracija**

Konačno, naučićete kako da povežete sa pool za rudarenje (eng. mining pool) i optimizujete performanse vašeg Antminer S9. Otkrićete kako da postignete optimalnu energetsku efikasnost i efikasno iskopate svoje prve satoshije.


Spremni da otkrijete svet Bitcoin rudarenja i prihvatite praktični Attakai izazov? Hajde da počnemo!



# Sve što treba da znate o rudarenju


<partId>aa99ef2c-da29-5317-a533-2ffa4f66f674</partId>


## Objašnjenje rudarenja


<chapterId>36a82de7-87ee-5e7a-b69e-48fc30030447</chapterId>


### Objašnjenje rudarenja: analogija sa slagalicom


Da bi se koncept rudarenja objasnio na pojednostavljen način, može se koristiti relevantna analogija: slagalice. Baš kao slagalica, rudarenje je složen zadatak za izvršavanje, ali ga je lako proveriti kada je završen. U kontekstu Bitcoin rudarenja, rudari se trude da brzo reše digitalnu slagalicu. Prvi rudar koji reši slagalicu predstavlja svoje rešenje celokupnoj mreži, koja zatim lako može proveriti njegovu validnost. Ovo uspešno verifikovanje omogućava rudaru da validira novi blok i doda ga u Bitcoin Timechain (u prevodu vremenski lanac). Kao priznanje za njihov rad, koji uključuje značajne troškove, rudar dobija nagradu u određenom broju bitkoina. Ova nagrada služi kao finansijski podsticaj rudarima da nastave svoj rad na validaciji transakcija i obezbeđivanju Bitcoin mreže.


![image](assets/en/001.webp)


U početku u Bitcoin mreži, dodeljena nagrada je bila 50 bitkoina svakih deset minuta, paralelno sa otkrivanjem bloka u proseku svakih deset minuta od strane rudara. Ova nagrada se prepolovljava svakih 210.000 blokova, otprilike svake četiri godine. Ova naknada služi kao snažan podsticaj da se rudari ohrabre da učestvuju u rudarskom procesu uprkos njegovim energetskim troškovima. Bez nagrade, energetski intenzivno rudarenje bi bilo napušteno, ugrožavajući sigurnost i stabilnost cele Bitcoin mreže.

Trenutna nagrada rudarima je dvostruka. S jedne strane, uključuje kreiranje novih bitkoina, što je smanjeno sa 50 bitkoina svakih deset minuta inicijalno na 6.25 bitkoina danas (2023). S druge strane, uključuje naknade za transakcije, ili rudarske naknade, iz transakcija koje rudar odluči da uključi u svoj blok. Kada se izvrši Bitcoin transakcija, plaćaju se naknade za transakciju. Ove naknade funkcionišu kao neka vrsta aukcije gde korisnici navode koliko su spremni da plate da bi njihova transakcija bila uključena u sledeći blok. Da bi maksimizirali svoju nagradu, rudari, delujući u svom interesu, biraju najprofitabilnije transakcije koje će uključiti u svoj blok, uzimajući u obzir ograničeni raspoloživi prostor. Tako, rudarske nagrada se sastoji od generisanja novih bitkoina i naknada za transakcije, osiguravajući kontinuirani podsticaj za rudare i osiguravajući dugovečnost i sigurnost Bitcoin mreže.


### Rudari i njihovi alati: rudarenje


Proces rudarenja uključuje pronalaženje validne heš vrednosti koja je prihvatljiva za Bitcoin mrežu. Kada se izračuna i pronađe, ova heš vrednost je nepovratna, slično kao kada se krompir pretvori u pire krompir. On verifikuje određenu funkciju bez mogućnosti vraćanja unazad. Rudari, u konkurenciji, koriste mašine za izračunavanje ovih heševa. Iako je teoretski moguće pronaći ovu heš vrednost ručno, složenost operacije čini ovu opciju neizvodljivom. Računari, sposobni da brzo izvrše ove proračune, se stoga koriste, trošeći značajnu količinu električne energije.


Na početku je dominirala era CPU-a, gde su rudari koristili svoje lične računare za Bitcoin rudarenje. Otkriće prednosti GPU-ova (grafičkih kartica) za ovaj zadatak označilo je prekretnicu, značajno povećavajući [Hashrate] (https://planb.academy/resources/glossary/hashrate) i smanjujući potrošnju energije. Napredak se tu nije zaustavio, sa kasnijim uvođenjem FPGA-ova (polje-programabilnih gejt nizova). FPGA-ovi su služili kao platforma za razvoj ASIC-ova (integrisanih kola specifičnih za aplikaciju).


![image](assets/en/002.webp)


ASIC-i su čipovi, uporedivi sa CPU čipom, međutim, oni su razvijeni da obavljaju samo jednu specifičnu vrstu proračuna na najefikasniji mogući način. Drugim rečima, CPU je sposoban da obavlja mnoštvo različitih vrsta proračuna bez da je posebno optimizovan za jednu ili drugu vrstu proračuna, dok će ASIC moći da obavlja samo jednu vrstu proračuna, ali veoma efikasno. U slučaju Bitcoin ASIC-a, oni su dizajnirani za izračunavanje SHA256 algoritma.

Danas rudari isključivo koriste ASIC uređaje posvećene ovoj operaciji, optimizovane da testiraju maksimalan broj kombinacija uz najmanju moguću potrošnju energije i što je brže moguće. Ovi računari, nesposobni za obavljanje zadataka osim Bitcoin rudarenja, su opipljiv dokaz kontinuirane evolucije i sve veće specijalizacije Bitcoin industrije rudarenja. Ova stalna evolucija odražava intrinzičnu dinamiku Bitcoin-a, gde prilagođavanje težine osigurava proizvodnju bloka svakih deset minuta uprkos eksponencijalnom povećanju rudarskih kapaciteta.


Da ilustrujemo intenzitet ovog procesa, razmotrite tipičan uređaj za rudarenje sposoban da postigne 14 TeraHash-a po sekundi, ili 14 triliona pokušaja svake sekunde da pronađe ispravan heš. Na nivou Bitcoin mreže, sada dostižemo približno 300 ExaHash-a po sekundi, što ističe kolektivnu snagu mobilisanu u Bitcoin rudarenje.


### Podešavanje težine


Podešavanje težine je ključni mehanizam u radu Bitcoin mreže, osiguravajući da se blokovi rudare u proseku svakih 10 minuta. Ovo trajanje je prosečno jer je proces rudarenja zapravo igra verovatnoće, slična bacanju kockica u nadi da će se dobiti broj manji od broja definisanog težinom. Svakih 2016 blokova, mreža podešava težinu rudarenjana osnovu prosečnog vremena potrebnog za rudarenje prethodnih blokova. Ako je prosečno vreme veće od 10 minuta, težina se smanjuje, i obrnuto, ako je prosečno vreme manje, težina se povećava. Ovaj mehanizam podešavanja osigurava da vreme rudarenja novih blokove ostane konstantno tokom vremena, bez obzira na broj rudara ili ukupnu računarsku snagu mreže. Zato se Bitcoin Blockchain (u prevodu lanac blokova) takođe naziva Timechain (u prevodu vremenski lanac).


![image](assets/en/003.webp)



- Primer iz Kine:

Slučaj Kine savršeno ilustruje ovaj mehanizam prilagođavanja težine. Sa obilnom i jeftinom energijom, Kina je bila glavni globalni centar za Bitcoin rudarenje. U 2021. godini, zemlja je iznenada zabranila Bitcoin rudarenej na svojoj teritoriji, što je rezultiralo masovnim padom globalnog Hashrate Bitcoin mreže, oko 50%. Ovaj brzi pad rudarske snage mogao je ozbiljno poremetiti Bitcoin mrežu povećanjem prosečnog vremena za rudarenje bloka. Međutim, mehanizam prilagođavanja težine je stupio na snagu, smanjujući težinu rudarenja kako bi se osiguralo da frekvencija rudarenja bloka ostane u proseku na 10 minuta. Ovaj slučaj pokazuje efikasnost i otpornost mehanizma prilagođavanja težine u Bitcoinu, koji obezbeđuje stabilnost i predvidljivost mreže čak i u uslovima naglih i značajnih promena u globalnom sistemu rudarenja.


### Evolucija mašina za rudarenje Bitcoin-a


Što se tiče evolucije mašina za rudarenje Bitcoin-a, važno je napomenuti da je kontekst više orijentisan ka tradicionalnom poslovnom modelu. Rudari zarađuju svoj prihod od validacije blokova, zadatka sa relativno niskom verovatnoćom uspeha. Trenutni model u upotrebi, Antminer S9, iako stariji model lansiran oko 2016. godine, još uvek je u opticaju na tržištu polovnih uređaja, gde se prodaje za oko €100 do €200. Međutim, cena mašina za rudarenje varira u zavisnosti od vrednosti Bitcoin-a, a noviji model, Antminer S19, trenutno se procenjuje na oko €3000.


Suočeni sa stalnim tehnološkim napretkom u oblasti rudarenja, profesionalci moraju strateški da se pozicioniraju. Industrija rudarenja je podložna kontinuiranim inovacijama, što je pokazano nedavnim izdanjem J verzije S19 i očekivanim izdanjem S19 XP, koji nude značajno veće mogućnosti rudarenja. Štaviše, poboljšanja nisu vezana samo za sirove performanse mašina. Na primer, novi model S19 XP koristi Liquid sistem hlađenja, tehničku modifikaciju koja omogućava značajno poboljšanje energetske efikasnosti. Iako inovacija ostaje konstantna, budući dobici u efikasnosti verovatno će biti manji u poređenju sa onima koji su do sada zabeleženi, zbog dostizanja određenog granice za tehnološke inovacije.


![image](assets/en/004.webp)


Konačno, industrija Bitcoin rudarenja nastavlja da se prilagođava i razvija, i igrači u industriji moraju predvideti smanjenje dobitaka u efikasnosti u budućnosti i prilagoditi svoje strategije u skladu s tim. Budući tehnološki napreci, iako još uvek prisutni, verovatno će se dešavati u manjem obimu, što odražava rastuću zrelost sektora.


## Industrija rudarenja


<chapterId>0896dfc1-c97e-5bec-9bf1-8c20b3388a2c</chapterId>


### Bazeni za rudarenje


Trenutno, Bitcoin rudarenje se razvija u ozbiljnu i značajnu industriju, sa mnogim igračima koji su sada javno poznati i sve većim brojem značajnih rudara. Ova evolucija je učinila rudarenje gotovo nedostupnim za male igrače zbog visokih troškova povezanih sa nabavkom novih mašina za rudarenje. Ovo postavlja pitanje distribucije Hashrate među različitim tržišnim igračima. Situacija je složena jer je neophodno ispitati i distribuciju Hashrate među različitim kompanijama i među različitim bazenima za rudarenje (eng. [mining pools](https://planb.academy/en/resources/glossary/pool-mining).


![image](assets/en/005.webp)


Rudarski bazen je grupa rudara koji kombinuju svoje računarske resurse kako bi povećali svoje šanse za uspešno rudarenje. Ova saradnja je neophodna jer izolovana mala mašina za rudarenje takmiči se protiv industrijskih giganata, smanjujući svoje šanse za uspeh na zanemarljiv nivo. Rudarenje radi na principu lutrije, i šanse za osvajanje bloka (a samim tim i Bitcoin nagrade) svakih deset minuta su izuzetno male za pojedinačni mali uređaj. Udruživanjem, rudari mogu kombinovati svoju računarsku snagu, češće pronalaziti blokove, a zatim raspodeliti nagrade proporcionalno doprinosu svakog uređaja u bazenu.


Na primer, ako bazen pronađe blok i osvoji 6.25 bitkoina, rudar koji doprinosi sa 1% ukupne računarske snage bazena bi dobio 1% od zarađenih 6.25 bitkoina. Međutim, treba napomenuti da rudarski bazeni obično uzimaju malu proviziju (obično oko 2%) kako bi pokrili operativne troškove zadruge.


### Softver koji koristi industrija


U kontekstu Bitcoin rudarenja, uloga softvera je jednako ključna kao i hardvera. Primer za to ilustruje uloga Bitmain-a, plodnog proizvođača koji je razvio Antminer S9. Pored hardvera za rudarenje, industrija se u velikoj meri oslanja na kolaborativne rudarske bazene, kao što je Brainspool, koji kontroliše približno 5% globalnog Hashrate-a Bitcoin mreže.

Glumci u ovoj industriji stalno traže načine da povećaju efikasnost putem hardvera i softvera. Na primer, popularan softver koji se koristi u ovom kontekstu je BrainsOS Plus. Ovaj softver zamenjuje originalni operativni sistem mašine za rudarenje, omogućavajući da se iste operacije obavljaju efikasnije. Sa ovakvim softverom, rudar može povećati efikasnost svoje mašine za 25%. To znači da za ekvivalentnu količinu električne energije, mašina može proizvesti dodatnih 25% Hashrate-a, čime se povećavaju nagrade koje dobija rudar. Ova optimizacija softvera je suštinski element konkurentnosti u Bitcoin rudarenju, pokazujući važnost integrisanog pristupa koji kombinuje poboljšanja hardvera i softvera kako bi se maksimizirala efikasnost i povrat.


### Regulacija i tarife za električnu energiju


Kao što je primećeno u Kini i drugde, regulativa ima značajan uticaj na rudarenje. Iako u Francuskoj nema značajnih rudara, regulativa i visoke tarife za električnu energiju u Evropi predstavljaju glavne prepreke. Rudari stalno traže jeftinu električnu energiju kako bi maksimizirali svoj profit. Stoga, visoka cena električne energije u Evropi i Francuskoj ne privlači rudare u ove regione.


Rudari obično gravitiraju ka regionima sa niskim tarifama za električnu energiju, često u zemljama u razvoju ili zemljama sa viškom energije. Na primer, veliki deo globalnog Hashrate-a nalazi se u Teksasu, Sjedinjene Američke Države. Teksas ima nezavisnu elektroenergetsku mrežu koja ne deli svoje energetske resurse sa drugim državama. Ova jedinstvenost često dovodi do toga da Teksas proizvodi više električne energije nego što je potrebno kako bi se izbegli nedostaci, stvarajući višak. Bitcoin rudari koriste ovu prekomernu proizvodnju tako što postavljaju operacije u Teksasu, gde mogu da rudare bitkoine po vrlo niskim cenama električne energije tokom perioda viška energije. Ova situacija pokazuje značajan uticaj propisa i tarifa za električnu energiju na Bitcoin rudarenje, ističući važnost ovih faktora u donošenju odluka rudara u vezi sa lokacijom njihovih operacija za rudarenje.


### Gde idu rudari i upravljanje energijom?


Isticanjem uticaja rudara Bitcoina na globalni energetski pejzaž, jasno se uočava njihov pravac delovanja: oni neprestano traže izvore jeftine električne energije, često one koji su neiskorišćeni ili se inače rasipaju. Ovaj fenomen je evidentan u regionima sa novom električnom infrastrukturom, kao što su oni opremljeni nedavnim hidroelektričnim branama.


Hajde da uzmemo primer. U zemlji koja je u procesu izgradnje brane, proizvodnja električne energije često počinje pre nego što su distributivne linije u potpunosti operativne. Ovaj vremenski jaz može rezultirati značajnim troškovima i obeshrabriti ulaganja u takve infrastrukturne projekte. Međutim, Bitcoin rudari mogu delovati kao fleksibilan izvor potražnje, spremni da potroše ovu "napuštenu" električnu energiju, čime pomažu u smanjenju troškova infrastrukture. Implikacija ovde je da nove instalacije mogu odmah biti profitabilne, podstičući stvaranje novih izvora električne energije. Ovaj princip se takođe primenjuje na manjim razmerama. Bilo da je reč o pojedincu koji koristi hidroelektrični generator na maloj reci ili domaćinstvu opremljenom solarnim panelima, višak proizvedene električne energije može se koristiti za napajanje Bitcoin rudarskih operacija.


U Francuskoj, na primer, višak električne energije iz solarnih panela se vraća u mrežu i proizvođači su kompenzovani kreditom za potrošnju od EDF-a. Slično, može se zamisliti rudar koji radi na ovom višku električne energije, isključujući se kada lokalna potražnja izjednači ponudu. Iako ovo može delovati sebično, dajući prednost proizvodnji Bitcoina nad podrškom lokalnoj elektroenergetskoj mreži, može se posmatrati iz drugog ugala: stabilizacija elektroenergetske mreže. Kompleksno upravljanje viškom električne energije, ponekad čak i sa povezanim troškovima za odlaganje, može biti znatno pojednostavljeno. Bitcoin rudari mogu apsorbovati ove viškove, delujući kao fleksibilni regulator, prilagođavajući potražnju umesto ponude. U svetu gde proizvodnja električne energije iz obnovljivih (nekontrolisanih) izvora stalno raste, rudari mogu igrati ključnu ulogu u osiguravanju ravnoteže naših elektroenergetskih mreža, dok istovremeno koriste jeftinu ili višak električne energije za napajanje svojih rudarskih operacija.


### Centralizacija rudarenja


Centralizacija rudarenja se smatra glavnim izazovom. Veliki igrači, kao što je Foundry, dominiraju tržištem, što potencijalno može dovesti do cenzure transakcija. Ova centralizacija takođe može učiniti mrežu ranjivom na napade, uključujući napad od 51%, kada pojedinac ili grupa kontroliše više od 50% hashrate-a mreže, što im omogućava da upravljaju i manipulišu mrežom.


Rizik od regulative: Naglašava da ako bi zemlja poput Sjedinjenih Američkih Država odlučila da reguliše ili zabrani određene Bitcoin transakcije, to bi moglo imati značajan uticaj na mrežu, posebno ako je veliki deo hashing snage centralizovan u toj zemlji.


![image](assets/en/006.webp)


Da bi se suzbila ova centralizacija, razmatraju se različite strategije:



- Kućno rudarenje: Ideja kućnog rudarenja zasniva se na decentralizaciji aktivnosti rudarenja. Podstiče pojedince da učestvuju u rudarenju iz svojih domova, čime se Hashrate šire distribuira.
- Stratum V2: Protokol Stratum V2 nudi drugačiji pristup. Za razliku od svog prethodnika, Stratum V2 omogućava rudarima da biraju koje transakcije će uključiti u blokove koje rudare. Ova sposobnost jača otpornost na cenzuru i smanjuje mogućnost velikih rudarskih bazena da dominiraju mrežom. Davanjem više moći pojedinačnim rudarima, protokol Stratum V2 može igrati odlučujuću ulogu u borbi protiv centralizacije Hashrate-a.

Otvaranje izvornog koda softvera za rudarenje


- Otvaranje izvornog koda softvera za rudarenje: Ovo je još jedna potencijalno efikasna strategija. Omogućavanjem pristupa softveru za rudarenje svima, mali rudari bi imali iste mogućnosti kao i velike rudarske kompanije da učestvuju i doprinesu Blockchain mreži. Ovaj pristup bi podstakao širu distribuciju Hashrate-a, čime bi se doprinelo decentralizaciji mreže.
- Diversifikacija aktera i geografije: Podsticanje učešća različitih aktera iz različitih geografskih regiona u rudarenju kriptovalute takođe može biti efikasno. Geografskom diversifikacijom Hashrate-a postaje teže da jedan akter ili država ostvare nesrazmernu kontrolu ili uticaj nad mrežom. Ovaj pristup može pomoći u zaštiti mreže od potencijalnih napada i ojačati njenu decentralizaciju.


Opšti zaključak je da je decentralizacija ključna za sigurnost i otpornost Bitcoin mreže. Iako centralizacija može ponuditi prednosti u efikasnosti, ona izlaže mrežu značajnim rizicima, uključujući cenzuru i 51% napade. Inicijative poput Takai i usvajanje novih protokola kao što je Stratum V2 su važni koraci ka decentralizaciji i zaštiti Bitcoin mreže od ovih pretnji.


## Nijanse rudarske industrije


<chapterId>7b9ee427-316a-54e3-a2d4-4ea97839a31b</chapterId>


### Princip Attakai


U trenutnom kontekstu, Bitcoin rudarenje sa modelom S9 može delovati složeno, ali dublja analiza otvara vrata ka inovativnim alternativama. Princip Attakai zasniva se na razmatranju upotrebe instalacija za rudarenje u raznim tipovima zgrada, kao što su škole ili bolnice. Glavna ideja je postaviti nekoliko mašina za rudarenje na različite lokacije, čime bi se ponovo koristila toplota koju emituju ove mašine za grejanje objekata. Odabirom efikasnijih modela kao što je S19, bilo bi moguće distribuirati aktivnost rudarenja, čime bi se poboljšale ukupne performanse, dok bi se istovremeno korisno doprinosilo društvu. Ova inicijativa ima za cilj da se takmiči sa velikim centralizovanim rudarskim operacijama koristeći toplotu generisanu od strane mašina na produktivan i efikasan način.


Inicijativa Attakai potiče iz ličnog kućnog eksperimenta koja su sprovela dva prijatelja željna da aktivno učestvuju u Bitcoin mreži. Suočili su se sa velikim preprekama, kao što su visoki nivoi buke opreme za rudarenje, koja je dizajnirana za industrijsku, a ne za kućnu upotrebu. Da bi se rešio ovaj problem, izvršene su hardverske modifikacije na rudarskim mašinama. Efikasniji i tiši ventilatori zamenili su originalnu opremu, čineći rudarenje kod kuće pristupačnijim i manje ometajućim. Pored toga, uključivanje Wi-Fi adaptera eliminisalo je potrebu za žičanom Ethernet vezom, dodatno pojednostavljujući kućni proces rudarenja. Zimi su ovi modifikovani rudari korišćeni kao izvor grejanja, pretvarajući smetnju u korist.


Nakon što su predstavili svoj projekat Bitcoin zajednici i videli interesovanje koje je izazvao, pronalazači Attakai odlučili su da objave detaljne vodiče na platformi Découvre Bitcoin, omogućavajući svakome da replicira svoje kućno iskustvo rudarenja. Sada planiraju da prošire ovaj koncept izvan domaćeg okruženja. Cilj je da pokažu kako modifikovana mašina za rudarenje može biti transformisana u tihi pomoćni grejač koji se može koristiti tokom zime, nudeći glatku tranziciju ka drugom delu obuke, fokusiranom na praktičnu primenu ovih modifikacija, ilustrovanu objašnjavajućim video zapisima. Međutim, ostaje pitanje da li se ova inicijativa može proširiti na veću skalu, nudeći realističnu i održivu alternativu trenutnim centralizovanim rudarskim strukturama.


![image](assets/en/007.webp)


### Granica ove decentralizacije?


Iako se ideja o decentralizaciji rudarenja kroz produktivnu upotrebu generisane toplote čini obećavajućom, ona ima određena ograničenja i pitanja ostaju. Energetski intenzivni objekti kao što su saune i bazeni mogli bi imati koristi od ovog koncepta koristeći toplotu proizvedenu od strane majnera za zagrevanje vode u svojim objektima. Ova praksa se već primenjuje od strane nekih članova Bitcoin zajednice, koji istražuju različite metode za efikasno korišćenje toplote generisane opremom za rudarenje. Na primer, svečana sala bi teoretski mogla biti zagrejana sa tri ili četiri S19 uređaja, od kojih svaki troši 3000 vati i proizvodi ekvivalentnu količinu toplote.


Međutim, treba napomenuti da su potrošnja energije i proizvodnja toplote ekvivalentni, bilo da energiju koristi električni grejač ili uređaj za rudarenje. Za svaki kilovat utrošene električne energije, količina proizvedene toplote biće ista u oba slučaja. Razlika leži u činjenici da uređaj za rudaranje ne samo da obezbeđuje toplotu već i Bitcoin nagradu, čime nudi ekonomski podsticaj za korišćenje mašina za rudarenje umesto jednostavnog električnog grejača. Ova dodatna nagrada mogla bi pomoći u ublažavanju zabrinutosti oko visoke potrošnje energije rudara.


Pitanje dugoročne efikasnosti i izvodljivosti korišćenja Bitcoin uređaja za grejanje ostaje otvoreno. Stalne inovacije u hardveru za rudarenje i tehnologijama grejanja mogu potencijalno otvoriti nove puteve za efikasniju upotrebu toplote generisane od strane uređaja, čime bi se doprinelo održivosti ovog pristupa u budućnosti.


### Zašto imati BTC nagrade?


Pitanje nagrađivanja u Bitcoinu umesto u nekoj drugoj valuti je ključno u sistemu koji je zamislio Satoshi Nakamoto. Kreiranje Bitcoina karakteriše fiksna granica od 21 milion jedinica. Cilj je bio pronaći pravedan način za distribuciju ovih novo kreiranih jedinica. Rudari, pružajući svoju računarsku snagu kako bi osigurali mrežu i učinili svaki napad sve skupljim, efikasno štite Bitcoin mrežu. Kao nagradu za ovaj ključni doprinos, oni su nagrađeni novo kreiranim bitcoinima, što olakšava distribuciju novčića unutar ekosistema.


To je win-win sistem. Rudari su nagrađeni i za obezbeđivanje mreže i za odobravanje transakcija. Novo kreirani bitkoini se daju kao podsticaj za jačanje sigurnosti, a naknade za transakcije su dodatni prihod za odobravanje transakcija. Ova dva elementa zajedno čine ukupnu nagradu za rudarenje. Pitanje budućnosti rudarenje se postavlja zbog programiranog smanjenja nagrada za rudarenje, tačnije prepolovljavanje svake četiri godine, događaj poznat kao "Halving". Do 2032. godine, nagrada za izrudareni blok će biti manji od jednog Bitcoina, a do 2140. godine, neće više biti kreirani novi bitkoini. U tom trenutku, rudari će se oslanjati isključivo na naknade za transakcije za kompenzaciju. Bitcoin mreža će morati da podrži veliki broj transakcija, sa dovoljno visokim naknadama, kako bi se osigurala profitabilnost rudarenja.


Porast Lightning mreže, koja omogućava brze i niskobudžetne transakcije van glavnog Bitcoin lanca, postavlja pitanja o budućnosti rudarenja. Lightning mreža ima potencijal da značajno smanji naknade za transakcije, čime bi se uticalo na prihode rudara. Međutim, to će zavisiti od stepena usvajanja i korišćenja Lightning mreže u poređenju sa glavnom Bitcoin mrežom. U pesimističnom scenariju, rudarima bi moglo biti isplativo da rudare čak i uz gubitak ako su amortizovali svoje troškove i imaju pristup jeftinoj struji. U optimističnijem scenariju, naknade za transakcije na glavnoj Bitcoin mreži mogle bi ostati dovoljno visoke da održe profitabilnost rudarenja.


### Šta treba da bude uključeno u Bitcoin blok?


Što se tiče pitanja šta bi trebalo uključiti u Bitcoin blok, ključno je razmotriti komplementarnu prirodu različitih slojeva Bitcoin mreže. Iako Lightning mreža može omogućiti brže i jeftinije transakcije, ona i dalje zavisi od osnovnog sloja Bitcoina, koji se često naziva „sloj za poravnanje“ (eng. settlement layer), za otvaranje i zatvaranje platnih kanala.

Sa očekivanim rastom Lightning mreže i posledičnim povećanjem otvaranja i zatvaranja kanala, prostor u Bitcoin blokovima postaje sve vredniji. Bitcoin zajednica već teži da ceni očuvanje ovog prostora, prepoznajući njegovu intrinzičnu ograničenost. Ova svest je dovela do diskusija o legitimnoj upotrebi prostora unutar blokova, uz zabrinutost zbog „spama“ na blokčejnu koji potiče od transakcija koje se smatraju neesencijalnim.

![image](assets/en/008.webp)


Spekulacije okružuju buduću upotrebu prostora unutar blokova, ali se generalno prihvata da je to oskudan resurs koji treba mudro koristiti. Iako postoji želja da se popuni, neophodno je očuvati ga kako bi se osigurala dugoročna održivost Bitcoin mreže, predviđajući buduće povećanje potražnje za prostorom unutar blokova. Kao i na svakom slobodnom tržištu, ponuda i potražnja će regulisati upotrebu prostora unutar blokova. Sa ograničenom ponudom, zainteresovane strane će morati donositi informisane odluke o korišćenju ovog vrednog prostora kako bi osigurale dugoročnu efikasnost i sigurnost Bitcoin mreže.


## Bitcoin rudarenje u Bitcoin protokolu


<chapterId>879a66b0-c20a-56b5-aad0-8a21be61e338</chapterId>


Uloga rudara u Bitcoin mreži bila je predmet intenzivne debate tokom "ratova" oko veličine blokova. Iako su ključni za sigurnost i funkcionalnost mreže, rudari ne poseduju nužno ultimativnu moć u Bitcoin ekosistemu. Ravnoteža između rudara, čvorova i krajnjih korisnika osigurava integritet i distribuciju mreže.


### Ratovi oko veličine bloka


Tokom ratova oko veličine blokova, mnogi rudari su se protivili određenim razvojnim promenama u mreži, ističući tenzije između različitih aktera u ekosistemu. Pitanje ostaje kako balansirati moć među rudarima, čvorovima i korisnicima kako bi se osigurala dugoročna sigurnost Bitcoina.


![image](assets/en/009.webp)


Sigurnosna Bitcoin dilema počiva na delikatnoj ravnoteži. Dok rudari igraju ključnu ulogu u validaciji i kreiranju blokova, čvorovi održavaju integritet verifikacijom i validacijom transakcija i blokova. Neispravan ili lažan blok će biti odbijen od strane čvorova, čime se cenzuriše rudar i očuvava sigurnost mreže. Moć takođe drže čvorovi i korisnici Bitcoin mreže. Čvorovi imaju moć verifikacije i validacije, dok korisnici imaju moć da biraju koji Blockchain će koristiti. Ova distribucija moći osigurava distribuciju i integritet Bitcoin mreže.


Ratovi oko veličine blokova otkrili su nesigurnost i napetost svojstvene upravljanju Bitcoin mrežom. Iako je Bitcoin Core trenutno dominantni lanac, debata oko upravljanja i menadžmenta mreže se nastavlja.


Na kraju, odgovornost je podeljena među svim akterima u Bitcoin mreži. Smanjenje broja korisnika, čvorova ili rudara moglo bi oslabiti mrežu, povećavajući rizik od centralizacije i ranjivosti na napade. Svaki akter doprinosi robusnosti i sigurnosti mreže, naglašavajući važnost održavanja ravnoteže moći i odgovornosti.


### Moć rudara


Satoshi Nakamotova elegantna teorija igara uspostavila je situaciju u kojoj je svaki akter u Bitcoin mreži motivisan da deluje ispravno kako bi zaštitio i svoje interese i interese drugih učesnika. Ovo stvara ravnotežu u kojoj se loše ponašanje može kazniti, čime se poboljšava sigurnost i stabilnost celog sistema. Uprkos ovoj ravnoteži, države ostaju potencijalna pretnja. Kao što je navedeno u prezentaciji na Surfing Bitcoin 2022, države mogu pokušati da napadnu industriju rudarenja, izlažući Bitcoin mrežu rizicima centralizacije i napada. Hipotetički scenariji, kao što je vojni napad usmeren na pogone za proizvodnju rudarske opreme, ističu značaj geografske i industrijske diverzifikacije za otpornost Bitcoin mreže.

![image](assets/en/010.webp)


Centralizacija proizvodnje hardvera za rudarenje u Kini predstavlja još jedan rizik. Odbijanje izvoza mašina za rudarenje ili akumulacija Hashrate za potencijalni 51% napad od strane Kine naglašava potrebu za diversifikovanom proizvodnjom rudarskog hardvera. Kao odgovor na ove rizike, Bitcoin zajednica aktivno istražuje rešenja. Kompanije poput Intela razmatraju proizvodnju rudarske opreme u Sjedinjenim Državama, doprinoseći distribuciji proizvodnje. Druge inicijative, kao što je Block-ov open-source Mining Development Kit (MDK), imaju za cilj smanjenje monopola na dizajn i proizvodnju rudarskog hardvera, omogućavajući širu distribuciju Hashrate-a. U središtu ovih diskusija leži osnovna Bitcoin misija: biti mreža za razmenu vrednosti otporna na cenzuru. Bitcoin zajednica neprestano teži jačanju distribucije, otpornosti na cenzuru i antifragilnosti mreže, odbacujući predloge kao što je prelazak na "dokaz o udelu" ili na engleskom "proof of stake", koji nisu u skladu sa ovim osnovnim principima.


### Fizička veza Proof of Work vs Proof of Stake


Proof of Work (PoW) je suštinski važan jer predstavlja fizičku vezu između stvarnog sveta i Bitcoina. Iako su bitkoini nematerijalni, njihova proizvodnja zahteva opipljivu energiju, čime se uspostavlja direktna veza sa fizičkim i stvarnim svetom. Ova veza osigurava da proizvodnja i validacija bitkoina i blokova imaju stvarni energetski trošak, čime se Bitcoin mreža usidruje u fizičkoj stvarnosti i sprečava njena potpuna dominacija od strane moćnih entiteta. PoW deluje kao bedem protiv centralizacije, osiguravajući da učešće u mreži i validacija transakcija zahtevaju ulaganje u opipljive resurse. Ovo sprečava monopolizaciju mreže od strane entiteta koji bi inače mogli preuzeti kontrolu bez značajne ulazne barijere, čime se osigurava pravednija distribucija moći i uticaja unutar Bitcoin mreže.


![image](assets/en/011.webp)


### Ograničenja Proof of Stake-a


S druge strane, Proof of Stake (PoS), iako omogućava učešće u malom obimu, ne garantuje ekvivalentnu zaštitu od centralizacije. U PoS mreži, oni koji već poseduju veliku količinu valute imaju nesrazmernu moć, što odražava postojeće nejednakosti moći u društvu u celini. Ova dinamika bi potencijalno mogla da produži centralizaciju i koncentraciju moći u rukama nekolicine, suprotno osnovnim ciljevima distribucije Bitcoin mreže. Argument da svako može učestvovati u PoS, čak i u malom obimu, pridruživanjem bazenima (eng. pools), nije nužno čvrst. U PoW mreži, čak i mali doprinosilac, sa skromnom opremom, može aktivno učestvovati i doprineti bezbednosti i distribuciji mreže.


### Rekapitulacija


Da rezimiramo, rudari jačaju Bitcoin mrežu protiv cenzure koristeći električnu energiju za izračunavanje Bitcoin-ovog Proof of Work-a, i nagrađuju se novim bitkoinima i naknadama za transakcije. Sa profesionalizacijom industrije, pojavljuju se različiti igrači, igrajući različite uloge, od kreiranja čipova do upravljanja farmama za rudarenje. Pored toga, finansije takođe imaju svoju ulogu, vršeći kontrolu time što odlučuju ko će opstati tokom različitih faza tržišta. Problem centralizacije i dalje postoji, s najbogatijim entitetima koji potencijalno dominiraju tržištem. Međutim, razvijaju se alternative na hardverskom i softverskom nivou. Na svakom pojedincu je da deluje i doprinese distribuciji mreže. Bitcoin predstavlja izvanrednu priliku ne samo u smislu slobode već i energetske nezavisnosti. Uprkos kontroverzama oko potrošnje električne energije, Bitcoin nudi ekonomski podsticaj za tranziciju ka racionalnijem i obilnijem korišćenju energije, ostvarujući ono što je prethodno bilo ekološki ideal.


## Bitcoin cena i Hashrate, korelacija?


<chapterId>e6676214-007c-5181-968e-c27536231bd6</chapterId>


### Hashrate, cena i profitabilnost


Trenutna stopa Hash iliti Hashrate, uprkos tome što je cena Bitcoin na $30,000 u poređenju sa njenim prethodnim vrhuncem od $69,000, ističe opipljivu vezu između rudarenja i stvarnog sveta. Periodi rasta tržišta dovode do velike potražnje za Bitcoin rudarenjem i povećanja narudžbine mašina od proizvođača kao što su Avalon i Bitmain. Međutim, proizvodnja i isporuka nisu trenutni, što stvara nesklad između povećane potražnje i kasnije dostupnosti. Ovo može dovesti do toga da mašine naručene tokom perioda naglog rasta tržišta budu isporučene u periodu pada vrednosti na tržištu, ističući značajnu asimetriju između niske cene i visoke Hash stope.


Ova situacija takođe ilustruje otpornost Bitcoina, često procenjivanu na osnovu njegove cene. Međutim, dublja analiza zdravlja Bitcoina zahteva ispitivanje njegove Hash stope, koja meri broj proračuna u sekundi u Bitcoin mreži. Dok Bitcoin cena varira, njegov trošak, povezan sa električnom energijom potrebnom za rad mašina za rudarenje, ostaje ključan za razumevanje dinamike tržišta. Fokusiranjem na trošak umesto na cenu, dobija se konzistentnija perspektiva o stabilnosti i dugoročnoj održivosti Bitcoina. Generalno, trošak Bitcoina je proporcionalan njegovoj ceni, pružajući bolje razumevanje fluktuacija cena i budućih izgleda.


![image](assets/en/012.webp)


### Hash stopa i nagrada


Rudarenje može uspostaviti donju cenu za Bitcoin, ispod koje bi rudari prodavali sa gubitkom. Trošak rudarenja značajno utiče na cenu, kao što je ilustrovano zabranom rudarenja u Kini, gde su heš stopa i cena značajno pali, ali su se brzo oporavili. Fokusiranje isključivo na cenu može biti obmanjujuće. Proučavanje troškova, putem kalkulatora profitabilnosti, nudi uravnoteženiju perspektivu. Međutim, tržište se može ponašati iracionalno, sa rudarima koji su potencijalno primorani da prodaju sa gubitkom, što može sniziti cenu ispod troška rudarenja. Da bi se procenilo zdravlje Bitcoina i njegova decentralizacija, mogla bi se razviti jednačina koja uključuje različite faktore, kao što su broj čvorova i cena. Ovaj pristup mogao bi pružiti nijansiraniju Bitcoin analizu u poređenju sa diskusijama zasnovanim isključivo na ceni.


### Rudarenje za profit ili za mrežu?


Pitanje je duboko i obuhvata nekoliko dimenzija Bitcoin rudarenja. Ravnoteža između traženja profita i doprinosa sigurnosti i distribuciji Bitcoin mreže je stalna dilema za rudare. Debata se nastavlja u Bitcoin zajednici, sa snažnim argumentima na svakoj strani.



- Rudarenje za profit:



- Za: Rudari su prirodno privučeni potencijalnom zaradom od Bitcoin rudarenja. Ulaganje u skupu opremu za rudarenje može biti nadoknađeno nagradama za rudarenje i naknadama za transakcije, posebno kada je cena Bitcoina visoka.
- Protiv: Potraga za profitom može dovesti do centralizacije snage heširanja ako samo nekoliko velikih kompanija može priuštiti ulaganje u vrhunsku opremu za rudarenje. Pored toga, rudarenje radi profita može imati značajan uticaj na životnu sredinu.



- Rudarenje za mrežu:



- Za: Rudarenje koje doprinesi bezbednosti i decentralizaciji Bitcoin mreže je plemenita inicijativa. Pomaže u jačanju otpornosti mreže i otporu cenzuri i napadima.
- Protiv: Bez dovoljno finansijskog podsticaja, može biti teško za rudare da nastave podržavati mrežu, posebno ako posluju s gubitkom.


Inicijativa Attakai ističe važnost doprinosa mreži dok nudi rešenja za lakši pristup i smanjenje štetnosti rudarenja. Mogućnost rudarenja kod kuće, uz pristupačniju opremu i rešenja za smanjenje zagađenja bukom, može pomoći u demokratizaciji Bitcoin rudarenja. Podstiče one koji su zainteresovani za Bitcoin ne samo da investiraju i drže bitkoine, već i da aktivno učestvuju u obezbeđivanju mreže. Pružanjem testirane opreme i vodiča za montažu i instalaciju, Attakai olakšava ulazak u svet Bitcoin rudarenja. Takođe podstiče inovacije i kontinuirana poboljšanja, pozivajući zajednicu da doprinese i podeli svoje ideje i iskustva kako bi se unapredilo rudarenje kod kuće. Model Attakai je odgovor na pitanje rudarenje za profit ili za mrežu. Nije reč samo o ostvarivanju profita, već i o jačanju distribucije i sigurnosti Bitcoin mreže, omogućavajući većem broju ljudi da učestvuju u rudarenju, uče i razumeju ovu ključnu industriju. Izazov potencijalne zabrane rudarenja u Evropi ostaje otvoreno pitanje. Ovo izaziva zabrinutost za budućnost Bitcoin rudarenja u regionu i potrebu za uravnoteženom regulacijom koja prepoznaje važnost rudarenja za sigurnost i održivost Bitcoin mreže, dok se istovremeno bavi ekološkim pitanjima. Attakai i druge slične inicijative mogu igrati ključnu ulogu u ovoj debati, pokazujući da je moguće rudarenje na održiviji i odgovorniji način, dok se pozitivno doprinosi Bitcoin mreži.


## Suverenitet i regulacija


<chapterId>9d9a5908-2acc-501e-906b-a6fce9ecfebd</chapterId>


### Suverenitet pre profita?


Da bi se rešilo ključno pitanje bogatstva kroz rudarenje, važno je razmotriti različite perspektive i pristupe. Pitanja o profitabilnosti rudarenja su česta, sa upitima oko kupovine akcija u kompanijama kao što su Riot ili iznajmljivanja mašina za rudarenje u zemljama sa niskim troškovima energije kao što su Island ili Rusija. Pre nego što se upustite u rudarenje, ključna razmatranja bi bila da se uporedi profitabilnost rudarenja sa direktnom kupovinom Bitcoina. Ako trošak rudarenja Bitcoina premašuje trošak direktne kupovine, generalno je mudrije kupiti Bitcoin direktno. Ovo izbegava višestruke izazove i troškove povezane sa procesom rudarenja.


Međutim, rudarenje nudi jedinstvene načine za uključivanje u Bitcoin ekosistem. Na primer, Bitcoin rudarenje zimi može biti pametan način da zagrejete svoj dom dok generišete prihod od Bitcoina. Druga opcija je ulaganje u kompanije koje prodaju opremu za rudarenje i skladište i upravljaju mašinama na lokacijama sa niskim troškovima energije, čime se omogućava pristup povoljnim cenama električne energije bez muke oko upravljanja opremom.


Uprkos ovim opcijama, rudarenje predstavlja značajne izazove. Dobro poznata izreka u svetu kriptovaluta, "Nisu tvoji ključevi, nisu tvoji Bitcoini," nalazi sličan odjek u svetu rudarenja: "Nije tvoj Hashrate, nije tvoja nagrada." Priče o razočaranjima i isključenim mašinama su česte, sa mnogim igračima koji obećavaju izuzetne rezultate, ali ne uspevaju da ih isporuče. Problemi sa ponudom električne energije i kvarovi mašina mogu ostaviti investitore nemoćnim, sa skupom opremom koju ne kontrolišu. U ovom kontekstu, oprez i duboko razumevanje sektora rudarenja su ključni pre nego što se upustite u njega. Iako postoje mogućnosti za dobitke, rizici su značajni, i informisan i promišljen pristup je neophodan za navigaciju ovim složenim i često nepredvidivim poljem. Stoga je od vitalnog značaja sprovesti temeljno istraživanje i pažljivo razmotriti prednosti i mane pre nego što se uključite u Bitcoin rudarenje.


![image](assets/en/013.webp)


### Novokreirani Bitcoini


Aspiracija da se poseduje sopstveni Hashrate pojavljuje se kao obećavajući put u svetu rudarenja. Međutim, navigacija kroz ovaj složeni ekosistem zahteva oprezan pristup. Oblast cloud rudarenja obeležena je velikim brojem prevara, podstaknutih nedostatkom razumevanja rudarenja od strane mnogih investitora. Privlačne ponude, upakovane na različite načine, lako mogu dovesti u zabludu one koji nisu dovoljno informisani. S druge strane, posedovanje sopstvene opreme za rudarenje nudi značajne prednosti. Osim ličnog zadovoljstva aktivnim doprinosom sigurnosti Bitcoin mreže i posmatranja nagrada kako pristižu u vaš novčanik, tu je i privlačan aspekt "novokreiranih bitcoina." (eng. "virgin bitcoin") To su sveže iskopani bitcoini, koji nikada nisu potrošeni i nemaju istoriju vezanu za njih. Ovi bitcoini se često smatraju vrednijim jer nikada nisu bili "kontaminirani," nudeći određenu garanciju protiv odbijanja od strane regulatora ili velikih platformi za trgovinu, kao što su menjačnice i berze.


Mogućnost rudarenja novokreiranih bitkoina uz izbegavanje Know Your Customer (KYC) procedura je još jedna dodata vrednost. Mnogi bazeni za rudarenje ne zahtevaju identitet rudara, što omogućava sticanje bitkoina bez prolaska kroz zamorne provere identiteta. Novokreirani bitkoini se smatraju "čistim," bez prošle istorije ili asocijacija. Posebno su traženi od strane velikih institucionalnih igrača koji mogu garantovati legitimitet svojih digitalnih sredstava pred regulatornim vlastima. Međutim, uprkos ovim prednostima, ključno je prepoznati da industrija rudarenja ostaje izuzetno konkurentna i nestabilna, a nepredviđeni incidenti mogu poremetiti operacije rudarenja.


U ovom kontekstu, izbor autonomnog i obrazovanog pristupa rudarenju čini se mudrim. Sticanje sopstvenog Hashrate i ulaganje u ličnu opremu za rudarenje, uz svest o rizicima i izazovima, može potencijalno ponuditi sigurniji i zadovoljavajući put ka sticanju novokreiranih bitcoina, čime se poboljšava finansijski suverenitet pojedinca dok se podržava Bitcoin ekosistem u celini.


### Da li je rudarenje zabranjeno u Evropi?


Sa pitanjem potencijalne zabrane rudarenja u Evropi, diskusije o regulaciji postaju sve relevantnije. Promenljivi regulatorni pejzaž zaista može značajno uticati na industriju Bitcoin rudarenja. Zabrana rudarenja u Evropi je zamisliv scenario, posebno uzimajući u obzir presedane u Kini. Iako operacije rudarenja i dalje traju u Kini uprkos zabrani, Evropa bi mogla slediti sličan put. Šira distribucija Hashrate širom različitih regiona mogla bi pomoći u jačanju zajednice rudara u Evropi, omogućavajući im da efikasno suprotstave nesporazumima i zabludama o rudarenju, njegovom uticaju na životnu sredinu kao i njegovom uticaju na električnu mrežu.


![image](assets/en/014.webp)


Suočeni sa kampanjama poput onih Greenpeace-a i često obmanjujućim podacima iz nekih studija, najbolje oružje ostaje istinita informacija. Neophodno je informisati širu javnost i donosioce odluka o stvarnosti rudarenja, njegovoj složenosti i nijansama, umesto da se oslanjaju na stereotipe i netačne informacije. Što su ljudi više informisani i svesni šta rudarenje zaista jeste, to se industrija bolje može braniti od potencijalnih restriktivnih regulativa.


U zaključku, uprkos regulatornom riziku i mogućnosti zabrane rudarenja u Evropi, najmoćnije oružje ostaje obrazovanje i informisanje. Jasno i precizno razumevanje rudarenja, kako funkcioniše i njegovog uticaja može pomoći u demistifikaciji industrije i borbi protiv dezinformacija, čime se nudi bolji otpor potencijalno štetnim regulativama. Inicijativa za obuku i informisanje ljudi o rudarenju, kao što ova diskusija čini, je korak u pravom smeru kako bi se osigurala održivost i rast rudarenja u Evropi i širom sveta. Kontinuirani napori za edukaciju i informisanje su od suštinskog značaja za osiguranje sigurne i prosperitetne budućnosti za industriju Bitcoin rudarenja.


# Rudarenje kod kuće i ponovna upotreba toplote


<partId>78d22d06-2c4a-573f-86bb-1027115dad3a</partId>


## Attakai - Omogućavanje i dostupnost rudarenja kod kuće!


<chapterId>1f5d1b74-2f99-5f31-a088-a73d36491ebf</chapterId>


Attakai, što znači "idealna temperatura" na japanskom, naziv je inicijative usmerene na otkrivanje Bitcoin rudarenja kroz ponovnu upotrebu toplote koju su pokrenuli @ajelexBTC i @jimzap21 sa Découvre Bitcoin.

Ovaj vodič za prepravku ASIC uređaja poslužiće kao osnova za dublje razumevanje rudarenja, njegovog funkcionisanja i prateće ekonomije, prikazujući mogućnost prilagođavanja Bitcoin mašina za rudarenje za upotrebu kao radijatora u domaćinstvima. Ovo nudi više komfora i uštede, omogućavajući učesnicima da dobiju povrat BTC-a bez KYC-a na svom računu za električno grejanje.


Bitcoin automatski podešava težinu rudarenja i nagrađuje rudare za njihovo učešće. Međutim, koncentracija Hashrate-a može predstavljati rizike za neutralnost mreže. Korišćenje računarske snage Bitcoina za grejna rešenja direktno koristi samoj mreži povećanjem distribucije računarske snage.


### Zašto ponovo koristiti toplotu iz ASIC-a?


Važno je razumeti odnos između energije i proizvodnje toplote u električnom sistemu.


Za potrošnju od 1 kW električne energije, električni radijator proizvodi 1 kW toplote, ni više, ni manje. Novi radijatori nisu efikasniji od tradicionalnih radijatora. Njihova prednost leži u sposobnosti da kontinuirano i ravnomerno raspoređuju toplotu u prostoriji, pružajući veći komfor u poređenju sa tradicionalnim radijatorima koji naizmenično prelaze između visokog grejanja i bez grejanja, čime se stvaraju uobičajne temperaturne varijacije i nelagodnosti.


Računar, ili šire gledano elektronska ploča, ne troši energiju za obavljanje proračuna, već jednostavno treba da energija prolazi kroz njegove komponente da bi funkcionisao. Potrošnja energije je posledica električnog otpora komponenti, što proizvodi gubitke i generiše toplotu, poznatu kao Džulov efekat.


Neke kompanije su došle na ideju da kombinuju potrebe za kompujterskom snagom sa potrebama za grejanjem putem radijatora/servera. Ideja je da se serverski sistemi kompanije distribuiraju u male jedinice koje bi mogle biti postavljene u domovima ili kancelarijama. Međutim, ova ideja se suočava sa nekoliko problema. Potreba za serverima nije povezana sa potrebom za grejanjem, i kompanije ne mogu fleksibilno koristiti kompjuterske kapacitete svojih servera. Takođe postoje ograničenja propusnog opsega (eng. bandwidth) koju pojedinci mogu imati. Svi ovi faktori sprečavaju kompaniju da učini ove skupe instalacije profitabilnim ili da obezbedi stabilnu ponudu online servera bez data centara koji mogu preuzeti kada grejanje nije potrebno.


> Toplota koju generiše vaš računar nije uzaludna ako treba da grejete svoj dom. Ako koristite električno grejanje tamo gde živite, onda toplota iz vašeg računara nije uzaludna. Košta isto da generišete ovu toplotu sa vašim računarom. Ako imate jeftiniji sistem grejanja od električnog grejanja, onda je gubitak samo u razlici u ceni. Ako je leto i koristite klima uređaj, onda je to dvostruki gubitak. Bitcoin rudarenje treba da se odvija tamo gde je jeftinije. Možda će to biti tamo gde je klima hladnija i gde je grejanje električno, i gde će rudarenje postati besplatno.
>

> Satoshi Nakamoto - 8. avgust 2010.

Bitcoin i njegov Proof of Work se ističu jer automatski prilagođavaju težinu rudarenja na osnovu količine računanja koje obavlja cela mreža. Ova količina se naziva Hashrate i izražava se u hešovima po sekundi. Danas se procenjuje na 380 eksahešova po sekundi, što je 380 milijardi milijardi hešova po sekundi. Ovaj Hashrate predstavlja rad i stoga količinu utrošene energije. Što je veći Hashrate, to je veća težina, i obrnuto. Tako se Bitcoin rudarenje može aktivirati ili deaktivirati u bilo kom trenutku bez uticaja na mrežu, za razliku od radijatora/servera koji moraju ostati stabilni da bi pružili svoju uslugu. Rudar je nagrađen za svoje učešće, u odnosu na druge, bez obzira koliko malo to bilo.


Ukratko, električni radijator i Bitcoin rudarenje proizvode 1 kW toplote za 1 kW potrošene električne energije. Međutim, rudar takođe prima bitkoine kao nagradu. Bez obzira na cenu električne energije, cenu Bitcoina, ili konkurenciju u aktivnosti Bitcoin rudarenju na mreži, ekonomski je isplativije grejati se sa uređajem za rudarenje nego sa električnim radijatorom.


### Dodata vrednost za Bitcoin


Važno je razumeti kako rudarenje doprinosi decentralizaciji Bitcoina.

Nekoliko postojećih tehnologija je ingeniozno kombinovano kako bi se oživeo Nakamoto konsenzus. Ovaj konsenzus ekonomski nagrađuje poštene učesnike za njihov doprinos radu Bitcoin mreže, dok obeshrabruje nepoštene učesnike. Ovo je jedna od ključnih tačaka koja omogućava mreži da postoji održivo.

Pošteni akteri, oni koji "kopaju" u skladu sa pravilima, svi se međusobno takmiče da dobiju što veći deo nagrade za proizvodnju novih blokova. Ovaj ekonomski podsticaj prirodno vodi ka obliku centralizacije jer kompanije biraju da se specijalizuju u ovoj unosnoj aktivnosti smanjenjem svojih troškova kroz ekonomiju obima. Ovi industrijski akteri imaju povoljan položaj za kupovinu i održavanje mašina, kao i za pregovaranje o veleprodajnim cenama električne energije.


> U početku bi većina korisnika pokretala mrežne čvorove, ali kako mreža raste preko određene tačke, sve više bi to bilo prepušteno stručnjacima sa server farmama specijalizovanog hardvera. Server farmi bi bilo potrebno da ima samo jedan čvor na mreži, a ostatak lokalne mreže (LAN) bi se povezivao na taj čvor.
>

> Satoshi Nakamoto - 2. novembar 2008.

Određeni entiteti drže značajan procenat ukupnog Hashrate-a u velikim farmama za rudaranje. Možemo primetiti nedavni hladni talas u Sjedinjenim Državama gde je značajan deo Hashrate-a bio isključen kako bi se energija preusmerila ka domaćinstvima sa izuzetnom potrebom za električnom energijom. Tokom nekoliko dana, rudari su bili ekonomski podstaknuti da ugase svoje farme, a to izuzetno vremensko stanje odrazilo se na krivu Bitcoin heš stope.

Ovo pitanje bi moglo postati problematično i predstavlja značajan rizik za neutralnost mreže. Akter sa više od 51% Hashrate-a bi lakše mogao cenzurisati transakcije ako to želi. Zato je važno distribuirati Hashrate-a među više aktera, a ne centralizovanim entitetima koje bi vlada, na primer, lakše mogla zapleniti.


**Ako su rudari raspoređeni u hiljadama, ili čak milionima, domaćinstava širom sveta, postaje veoma teško za državu da preuzme kontrolu nad njima.**


Kada izađe iz fabrike, uređaj za rudarenje nije pogodan za korišćenje kao grejač u kući, zbog dva glavna problema: prekomerne buke i nedostatka podešavanja. Međutim, ovi problemi se lako mogu rešiti kroz hardverske i softverske modifikacije, omogućavajući mnogo tiši uređaj koji se može konfigurisati i automatizovati kao moderni električni grejači.


**Attakaï je obrazovna inicijativa koja vas uči kako da na najisplativiji način unapredite Antminer S9.**


Ovo je odlična prilika da učite kroz praksu dok ste nagrađeni za vaše učešće sa KYC-free satoshijima.


## Vodič za kupovinu polovnog ASIC-a


<chapterId>3b0b3bf0-859b-57f2-b92f-843ac70b7e68</chapterId>


U ovom odeljku ćemo diskutovati o najboljim praksama za kupovinu polovnog Bitmain Antminer S9, mašine na kojoj će se zasnivati ovaj vodič za ugradnju radijatora. Ovaj vodič se takođe primenjuje na druge modele ASIC-a jer je to opšti vodič za kupovinu polovnog hardvera za rudarenje.


Antminer S9 je uređaj koji nudi Bitmain od maja 2016. Troši 1400W električne energije i proizvodi 13.5 TH/s. Iako se smatra starim, ostaje odlična opcija za početak rudarenja. Pošto je proizveden u velikim količinama, lako je pronaći rezervne delove u mnogim regionima sveta. Generalno se može nabaviti peer-to-peer na sajtovima kao što su eBay ili LeBonCoin, jer ga profesionalni preprodavci više ne nude zbog njegove niže konkurentnosti u poređenju sa novijim mašinama. Manje je efikasan od ASIC-a kao što je Antminer S19, koji se nudi od marta 2020, ali to ga čini pristupačnim polovnim hardverom i pogodnijim za modifikacije koje ćemo napraviti.


Antminer S9 dolazi u nekoliko varijacija (i, j) koje čine manje modifikacije na hardveru u odnosu na prvu generaciju. Ne verujemo da ovo treba da utiče na vašu odluku o kupovini, i ovaj vodič funkcioniše za sve te varijacije.


Cena ASIC-a varira u zavisnosti od mnogih faktora kao što su cena Bitcoina, težina mreže, efikasnost mašine i trošak električne energije. Stoga je teško dati tačnu procenu za kupovinu korišćene mašine. U februaru 2023. godine, očekivana cena u Francuskoj generalno se kreće od €100 do €200, ali ove cene mogu brzo da se promene.


![image](assets/en/015.webp)


Antminer S9 se sastoji od sledećih delova:



- 3 hešborda koji sadrže čipove koji proizvode hešing snagu.


![image](assets/en/016.webp)



- Kontrolna ploča koja uključuje slot za SD karticu, Ethernet port i konektore za hashboardove i ventilatore. Ovo je mozak vašeg ASIC-a.


![image](assets/en/017.webp)



- 3 kabla za prenos podataka koji povezuju heš table sa kontrolnom pločom.


![image](assets/en/018.webp)



- Napajanje, koje radi na 220V i može se priključiti kao običan kućni aparat.


![image](assets/en/019.webp)



- 2 ventilatora od 120mm.


![image](assets/en/020.webp)



- C13 kabl.


![image](assets/en/021.webp)


Kada kupujete korišćenu mašinu, važno je proveriti da li su svi delovi uključeni i funkcionalni. Tokom kupovine, trebalo bi da zamolite prodavca da uključi mašinu kako biste proverili njeno pravilno funkcionisanje. Važno je potvrditi da se uređaj pravilno uključuje, a zatim proveriti internet konekciju priključivanjem Ethernet kabla i pristupom Bitmain login korisničkom interfejsu putem web pregledača na istoj lokalnoj mreži. Možete pronaći ovu IP adresu povezivanjem na interfejs vašeg internet ruter i traženjem povezanih uređaja. Ova adresa bi trebalo da ima sledeći format: 192.168.x.x


![image](assets/en/022.webp)


Takođe, proverite da li podrazumevani kredencijali rade (korisničko ime: root, lozinka: root). Ako podrazumevani kredencijali ne rade, biće potrebno da resetujete mašinu.


![image](assets/en/023.webp)


Kada se povežete, trebali biste moći videti status svakog hashboarde-a na kontrolnoj tabli. Ako je uređaj povezan na rudarski bazen, trebali biste videti da svi hashboarde-i funkcionišu. Važno je napomenuti da ovi uređaji prave mnogo buke, što je normalno. Takođe, proverite da li ventilatori rade ispravno.


Zatim možete ukloniti rudarski bazen prethodnog vlasnika kako biste kasnije postavili svoj. Ako želite, možete takođe pregledati hashboardove rastavljanjem mašine. Međutim, ovaj korak je složeniji i zahteva više vremena i neke alate. Ako želite da nastavite sa ovim rastavljanjem, možete se obratiti sledećem delu ovog tutorijala koji detaljno objašnjava kako to uraditi. Važno je napomenuti da ovi uređaji sakupljaju mnogo prašine i zahtevaju redovno održavanje. Možete videti nakupljenu prašinu i kvalitet održavanja rastavljanjem mašine.

Nakon što pregledate sve ove tačke, možete kupiti svoju mašinu sa visokim stepenom poverenja. Ako ste u nedoumici, konsultujte zajednicu.


Da rezimiramo ovaj vodič u jednoj rečenici: **"Ne veruj, proveri."**


[Takođe se možete obratiti profesionalcima za obnavljanje rudarskih mašina, kao što je naš partner 21energy. Oni nude testirane S9 mašine, očišćene i sa već instaliranim BraiiinOS+ softverom. Sa partnerskim kodom "decouvre," dobićete 10% popusta na kupovinu S9 i podržati Attakai projekat.](https://21energy.io/en/produkt/bitmain-antminer-s9-bundle/)


## Vodič za kupovinu hardverskih modifikacija za S9


<chapterId>fa5f5eca-bcbf-5a83-9b03-98ecbadbabd6</chapterId>


Kao vlasnik Antminer S9, verovatno znate koliko ova oprema može biti bučna i glomazna. Međutim, moguće je transformisati je u tihi i povezani grejač prateći nekoliko jednostavnih koraka. U ovom delu ćemo predstaviti potrebnu opremu za izvršenje modifikacija.


Ako ste vešt majstor i želite da transformišete uređaj u grejač, ovaj vodič je za vas. Želimo da vas upozorimo da modifikacije elektronskog uređaja mogu predstavljati električne rizike. Stoga je neophodno preduzeti sve potrebne mere predostrožnosti kako biste izbegli bilo kakvu štetu ili povredu.


1. Zamenite ventilatore


Originalni ventilatori Antminer S9 su previše bučni da biste koristili svoj Antminer kao grejač. Rešenje je da ih zamenite tišim ventilatorima. Naš tim je testirao nekoliko modela brenda Noctua i odabrao Noctua NF-A14 iPPC-2000 PWM kao najbolji kompromis. Obavezno izaberite verziju ventilatora od 12V. Ovaj ventilator od 140mm može proizvesti do 1200W grejanja uz održavanje teoretskog nivoa buke od 31 dB. Da biste instalirali ove ventilatore od 140mm, biće vam potreban adapter sa 140mm na 120mm, koji možete pronaći u DécouvreBitcoin prodavnici. Takođe ćemo dodati zaštitne rešetke od 140mm.


![image](assets/en/024.webp)

![image](assets/en/025.webp)

![image](assets/en/026.webp)


Napajanje za ventilator je takođe prilično bučan i potrebno ga je zameniti. Preporučujemo Noctua NF-A6x25 PWM. Imajte na umu da se konektori na Noctua ventilatorima razlikuju od originalnih, tako da će vam biti potreban adapter za konektor da ih povežete. Dva će biti dovoljna. Ponovo, obavezno izaberite verziju ventilatora od 12V.


![image](assets/en/027.webp)

![image](assets/en/028.webp)


2. Dodajte WIFI/Ethernet most


Umesto korišćenja Ethernet kabla, možete povezati svoj Antminer putem WIFI-ja dodavanjem WIFI/Ethernet mosta. Odabrali smo vonets vap11g-300 jer vam lako omogućava da preuzmete WIFI signal sa vašeg internet boksa (rutera/modema)i prenesete ga na vaš Antminer putem Ethernet-a bez kreiranja podmreže. Ako imate električarske veštine, možete ga napajati direktno sa napajanjem Antminera bez potrebe za dodavanjem USB punjača. Za to će vam biti potreban ženski džek od 5,5 mm x 2,1 mm.


![image](assets/en/029.webp)

![image](assets/en/030.webp)


3. Opcionalno: dodajte pametnu utičnicu


Ako želite da uključite/isključite vaš Antminer sa pametnog telefona i pratite njegovu potrošnju energije, možete dodati pametnu utičnicu. Testirali smo ANTELA utičnicu u verziji od 16A, kompatibilnu sa smartlife aplikacijom. Ova pametna utičnica vam omogućava da vidite dnevnu i mesečnu potrošnju energije i povezuje se direktno na vaš internet ruter putem WiFi-a.


![image](assets/en/031.webp)


Lista opreme i linkovi



- 2X 3D adapter komad 140mm na 120mm



- [2X NF-A14 iPPC-2000 PWM](https://www.amazon.fr/Noctua-nf-polarized-A14-industrialppc-PWM-2000/dp/B00KESSUDW)



- [2X 140 mm fan grilles](https://www.amazon.fr/dp/B06XD4FTSQ)
- [Noctua NF-A6x25 PWM](https://www.amazon.fr/Noctua-nf-a6-25-PWM-Ventilateur-Marron/dp/B00VXTANZ4)



- [Električarov šećer 2.5 mm²](https://www.amazon.fr/Legrand-LEG98433-Borne-raccordement-Nylbloc/dp/B00BBHXLYS)
- [Vonets vap11g-300](https://www.amazon.fr/Vonets-VAP11G-300-Bridge-convertit-Ethernet/dp/B014SK2H6W)
- [Opcioni ANTELA pametni utikač](https://www.amazon.fr/dp/B09YYMVXJZ)


# Attakai - Modifikacija softvera Antminer S9


<partId>afc9c29a-84aa-5f1d-82e2-5fd9ff2e1805</partId>


## Postavljanje Vonet WIFI/Ethernet mosta


<chapterId>3cf487a4-21ef-5b24-83d5-789b811f740f</chapterId>


Da biste povezali svoj ASIC putem WIFI-ja, biće vam potreban uređaj koji se zove most. Ovaj uređaj vam omogućava da preuzmete WIFI signal sa vašeg rutera i prenesete ga na drugi uređaj putem Ethernet-a.


Mnogi uređaji mogu obavljati ovu funkciju, ali preporučujemo VONETS WiFi Bridge/Repeater zbog njegove praktičnosti.


Most se napaja povezivanjem preko USB kabla.


Sa vašeg računara povežite se na VONETS\_**\*\*** WIFI mrežu sa lozinkom 12345678.


![image](assets/en/032.webp)


Prijavite se sa korisničkim imenom "admin" i lozinkom "admin".


![image](assets/en/033.webp)


Izaberi čarobnjaka (eng. wizard).


![image](assets/en/034.webp)


Izaberite WIFI mrežu na koju želite da povežete svoj uređaj za rudarenje, zatim kliknite Next za dalje.


NAPOMENA: Vonet most radi samo na frekvenciji od 2.4GHz. Danas ruteri obično nude dve WIFI mreže, jednu na 2.4GHz i jednu na 5GHz.


![image](assets/en/035.webp)


Unesite lozinku za vašu WIFI mrežu u polje "Source WIFI hotspot password". Ako ne želite da koristite vaš Vonet most za proširenje vaše WIFI mreže, označite polje "Disable Hotspot". U suprotnom, ostavite ga neoznačenim.


Zatim možete kliknuti na Save, kako biste sačuvali izmene.


Na kraju, kliknite na reboot da ponovo pokrenete most. Biće potrebno nekoliko minuta da se ponovo pokrene.


Most treba da se poveže sa vašim ruterom i pojaviće se pod imenom "[VONETS.COM](http://vonets.com/)". Ako se i dalje ne povezuje nakon nekoliko minuta, možda ćete morati da isključite/ponovo uključite most.


Kada je most povezan, povežite Ethernet kabl od mosta do vašeg ASIC-a, a zatim priključite ASIC u strujnu utičnicu. Zatim možete pristupiti ASIC korisničkom interfejsu na isti način kao da je direktno povezan sa vašim ruterom putem Ethernet-a.


## Resetovanje Antminer S9


<chapterId>b518b6bd-9dae-5136-ae3c-1fafb1cb2592</chapterId>


Pre nego što instalirate BraiinOS+, možda će biti potrebno da resetujete vaš S9 na fabrička podešavanja.

Ova metoda se može primeniti između 2 minuta i 10 minuta nakon pokretanja uređaja za rudarenje.

2 minuta nakon uključivanja uređaja, pritisnite dugme "Reset" na 5 sekundi, a zatim ga otpustite. Uređaj će biti vraćen na fabrička podešavanja u roku od 4 minuta i automatski će se ponovo pokrenuti (nema potrebe da ga isključujete).


![image](assets/en/036.webp)


## Instaliranje BraiinsOS+ na Antminer S9


<chapterId>38e8b1a8-8b1d-51ed-8b92-59d4ddb15184</chapterId>


Originalni softver koji je instalirao Antminer na njihove mašine je ograničen u funkcionalnosti. Zato ćemo u ovom vodiču instalirati drugi softver pod nazivom BraiinsOS+. To je softver treće strane razvijen od strane prvog Bitcoin rudarskog bazena (eng. mining pool) koji ima više funkcija i omogućava, na primer, modifikaciju snage mašine.


Postoji nekoliko načina za instalaciju Braiins OS+ na ASIC. Možete se pozvati na ovaj vodič kao i na [zvaničnu Braiins dokumentaciju](https://academy.braiins.com/en/braiins-os/about/).


Ovde ćemo videti kako lako instalirati Braiins OS+ direktno na memoriju vašeg Antminera koristeći BOS toolbox softver, zamenjujući originalni operativni sistem, kroz detaljne korake ispod.


1. Uključite svoj Antminer i povežite ga sa internet boksom (ruterom/modemom).

2. Preuzmite BOS toolbox za Windows / Linux.

3. Raspakujte preuzetu datoteku i otvorite bos-toolbox.bat datoteku. Izaberite jezik, i nakon nekoliko trenutaka, videćete ovaj prozor:


![image](assets/en/037.webp)


4. Bos toolbox će vam omogućiti da lako pronađete IP adresu vašeg Antminera i instalirate BraiinsOS+. Ako već znate IP adresu vaše mašine, možete preskočiti na korak 8. U suprotnom, idite na karticu za skeniranje.


![image](assets/en/038.webp)


5. Obično, na kućnim mrežama, opseg IP adresa je između 192.168.1.1 i 192.168.1.255, pa unesite "192.168.1.0/24" u polje za IP opseg. Ako je vaša mreža drugačija, molimo vas da promenite ove adrese u skladu s tim. Zatim kliknite na "Start".


6. Pažnja, ako Antminer ima lozinku, detekcija neće raditi. Ako je to slučaj, najjednostavnije rešenje je izvršiti resetovanje.


7. Trebalo bi da vidite sve Antminere na vašoj mreži kako se pojavljuju ovde, a IP adresa je 192.168.1.37.


![image](assets/en/039.webp)


8. Kliknite na "Back", a zatim na karticu "Install", unesite prethodno pronađenu IP adresu i kliknite na "Start".


> Ako instalacija ne radi, možda će biti potrebno izvršiti resetovanje i pokušati ponovo (pogledajte prethodni odeljak).

![image](assets/en/040.webp)


9. Nakon nekoliko trenutaka, vaš Antminer će se ponovo pokrenuti i moći ćete pristupiti Braiins OS+ korisničkom interfejsu na navedenoj IP adresi — ovde 192.168.1.37 — direktno u adresnoj traci vašeg pregledača. Podrazumevano korisničko ime je "root" i nema podrazumevane lozinke.


## Konfigurišite BraiinsOS+


<chapterId>36e432f2-85bc-52d0-a62a-009fc4c69338</chapterId>


Trebaće da se povežete sa svojim ASIC-om koristeći lokalnu IP adresi vašeg uređaja na vašoj mreži putem pregledača.


Možete pronaći IP adresu vaše mašine koristeći alat BOS toolbox ili direktno na veb stranici vašeg rutera.


Podrazumevani kredencijali su isti kao originalni operativni sistem.



- korisničko ime: root
- lozinka: (nema)


Zatim će vas dočekati Brains OS+ Dashboard (u prevodu kontrolna tabla).


### Kontrolna tabla


![image](assets/en/041.webp)


Na ovoj prvoj stranici možete posmatrati performanse vaše mašine u realnom vremenu.



- Tri grafikona u realnom vremenu koji prikazuju temperaturu, Hashrate i opšte stanje vaše mašine.
- Sa desne strane, pravi Hashrate, prosečna temperatura čipa, procenjena efikasnost u W/THs i potrošnja energije.
- Ispod, brzina ventilatora kao procenat maksimalne brzine i broj obrtaja u minuti.


![image](assets/en/042.webp)



- Niže ćete pronaći detaljan prikaz svake heš ploče. Prosečna temperatura ploče i čipova koje sadrži, kao i napon i frekvencija.
- Detalji o aktivnim rudarskim bazenima u Pools.
- Status automatskog podešavanja u odeljku Tuner Status.
- Sa desne strane, detalji o podacima prenetim u bazen.


### Konfiguracija


![image](assets/en/043.webp)


### Sistem


![image](assets/en/044.webp)


### Brze radnje


![image](assets/en/045.webp)


# Attakai - modifikacija ventilatora


<partId>98266a8f-3745-58a0-9f6b-26a9734e1427</partId>


## Zamenite napajanje od ventilatora


<chapterId>0c6befa7-f3ef-5bcf-ae8d-0ad5e5d41d70</chapterId>


> UPOZORENJE: Neophodno je prethodno instalirati Braiins OS+ na vaš uređaj, ili bilo koji drugi softver koji može smanjiti performanse vaše mašine. Ova mera je ključna jer ćemo, kako bismo smanjili buku, instalirati manje snažne ventilatore koji mogu raspršiti manje toplote.

![image](assets/en/046.webp)


### Potrebni materijali



- 1 Noctua NF-A6x25 PWM ventilator
- električarska kocka 2.5mm2


> UPOZORENJE: Pre svega, pre nego što počnete, uverite se da ste isključili svoj uređaj kako biste izbegli bilo kakav rizik od strujnog udara.

![image](assets/en/047.webp)


Prvo, uklonite 6 šrafova sa strane kućišta koji ga drže zatvorenim. Kada uklonite šrafove, pažljivo otvorite kućište kako biste uklonili plastičnu zaštitu koja pokriva komponente.


![image](assets/en/048.webp)

![image](assets/en/049.webp)


Zatim, vreme je da uklonite originalni ventilator, pazeći da ne oštetite druge komponente. Da biste to uradili, uklonite šrafove koji ga drže na mestu i pažljivo odlepite beli lepak koji okružuje konektor. Važno je postupati pažljivo kako biste izbegli oštećenje žica ili konektora.


![image](assets/en/050.webp)


Kada se originalni ventilator ukloni, primetićete da konektori novog Noctua ventilatora ne odgovaraju onima originalnog ventilatora. Naime, novi ventilator ima 3 žice, uključujući žutu žicu koja omogućava kontrolu brzine. Međutim, ova žica neće biti korišćena u ovom specifičnom slučaju. Da biste povezali novi ventilator, preporučuje se korišćenje specijalnog adaptera. Međutim, važno je napomenuti da ovaj adapter ponekad može teško pronaći.


![image](assets/en/051.webp)


Ako nemate ovaj adapter, i dalje možete nastaviti sa povezivanjem novog ventilatora koristeći električarsku kocku. Da biste to uradili, biće potrebno da isečete kablove starog i novog ventilatora.


![image](assets/en/052.webp)

![image](assets/en/053.webp)


Na novom ventilatoru, koristite sekač i pažljivo isecite konture glavnog omotača na 1 cm, bez sečenja omotača kablova ispod.


![image](assets/en/054.webp)


Zatim, povlačenjem glavne obloge prema dole, isecite obloge crvenog i crnog kabla na isti način kao ranije. A žuti kabl isecite u ravni.


![image](assets/en/055.webp)


Na starom ventilatoru, delikatnije je preseći glavni omotač bez oštećenja omotača crvene i crne žice. Za to smo koristili iglu koju smo provukli između glavnog omotača i crvene i crne žice.


![image](assets/en/056.webp)

![image](assets/en/057.webp)


Kada su crvene i crne žice izložene, pažljivo isecite omotače kako ne biste oštetili električne žice.


![image](assets/en/058.webp)


Zatim povežite kablove pomoću električarske kocke — crnu žicu sa crnom, a crvenu sa crvenom. Možete dodati i izolir traku.


![image](assets/en/059.webp)

![image](assets/en/060.webp)


Kada se uspostavi veza, vreme je da instalirate novi Noctua ventilator sa rešetkom i starim šrafovima. Novi šrafovi iz kutije će biti ponovo korišćeni kasnije. Uverite se da ga postavite u ispravnu orijentaciju. Primetićete strelicu na jednoj strani ventilatora, koja pokazuje pravac protoka vazduha. Važno je postaviti ventilator tako da ova strelica pokazuje ka unutrašnjosti kućišta. Zatim ponovo povežite ventilator.


![image](assets/en/061.webp)

![image](assets/en/062.webp)


> Opcionalno: Ako ste upućeni u električnu energiju, možete direktno dodati ženski džek 5.5mm konektor na 12V izlaz za napajanje, što će direktno napajati Vonet Wi-Fi most. Međutim, ako niste sigurni u svoje električarske veštine, najbolje je koristiti USB konektor sa punjačem tipa za pametni telefon kako biste izbegli bilo kakav rizik od kratkog spoja ili električnog oštećenja.

![image](assets/en/063.webp)


Kada su veze uspostavljene, postavite plastični poklopac preko kućišta plastike, a ne unutra.


![image](assets/en/064.webp)


Konačno, vratite poklopac kućišta na mesto i zavrnite 6 šrafova sa strane kako biste sve učvrstili. I eto, vaše kućište napajanja sada je opremljeno novim ventilatorom.


## Zamena glavnih ventilatora


<chapterId>a29f60f1-3fa3-57fc-a630-9c97cec30e56</chapterId>


> UPOZORENJE: Neophodno je prethodno instalirati Braiins OS+ na vaš uređaj, ili bilo koji drugi softver sposoban da smanji performanse vaše mašine. Ova mera je ključna jer ćemo, kako bismo smanjili buku, instalirati manje snažne ventilatore, koji će rasipati manje toplote.

![image](assets/en/046.webp)


### Potrebni materijali



- 2 komada 3D adapter 140mm na 120mm
- 2 Noctua NF-A14 iPPC-2000 PWM ventilatora
- 2 140mm rešetke za ventilatore


> UPOZORENJE: Prvo, pre nego što počnete, obavezno isključite svoj uređaj kako biste izbegli bilo kakav rizik od strujnog udara.

1. Prvo, isključite ventilatore i odvrnite ih.


![image](assets/en/065.webp)


2. Konektori novih Noctua ventilatora ne odgovaraju originalnim, ali ne brinite! Uzmite svoj rezač i pažljivo isecite male plastične jezičke tako da konektori savršeno odgovaraju vašem uređaju.


![image](assets/en/066.webp)

![image](assets/en/067.webp)


3. Vreme je da instalirate 3D delove!

Pričvrstite ih na obe strane uređaja koristeći šrafove koje ste uklonili sa ventilatora. Ušrafite ih dok glava šrafa ne bude u ravni sa 3D delom i dok ne bude sigurno na mestu. Pazite da ne zategnete previše, jer biste mogli deformisati deo i jedan od šrafova bi mogao dodirnuti kondenzator!


![image](assets/en/068.webp)


4. Sada pređimo na ventilatore.


Pričvrstite ih na 3D delove koristeći šrafove koji su obezbeđeni u kutiji. Obratite pažnju na pravac protoka vazduha, strelice na stranama ventilatora će pokazati pravac koji treba pratiti. Idite od strane sa Ethernet portom ka drugoj strani. Pogledajte fotografiju ispod.


![image](assets/en/069.webp)

![image](assets/en/070.webp)

![image](assets/en/071.webp)


5. Poslednji korak: povežite ventilatore i pričvrstite rešetke na vrhu pomoću šrafova koji nisu korišćeni u kutiji ventilatora napajanja. Imate samo 4, ali 2 po rešetki u suprotnim uglovima će biti dovoljna. Takođe možete potražiti slične šrafove u prodavnici alata ako je potrebno.


![image](assets/en/072.webp)

![image](assets/en/073.webp)


Dok čekate da budete u mogućnosti da ponudite stilizovanije kućište za vaš novi grejač, možete pričvrstiti kućište i napajanje električarskim vezicama.


![image](assets/en/074.webp)


I za završni detalj, povežite Vonet bridge sa Ethernet portom i njegovim napajanjem.


![image](assets/en/075.webp)


I eto ga, čestitamo! Upravo ste zamenili ceo mehanički deo vašeg uređaja za rudarenje. Sada bi trebalo da čujete mnogo manje buke.


# Attakai - Konfiguracija


<partId>9c3918a8-d9a3-5a1f-bb9a-70314f7ac175</partId>


## Pridruživanje rudarskom bazenu


<chapterId>b57a6105-0a53-5fe9-bad1-d6d9daf97c0d</chapterId>


Možete zamisliti rudarski bazen kao poljoprivrednu zadrugu. Poljoprivrednici udružuju svoju proizvodnju kako bi smanjili razlike između ponude i potražnje, te tako ostvarili stabilniji prihod za svoje poslovanje. Rudarski bazeni funkcioniše na isti način, s tim što je zajednički resurs heš. Naime, otkriće jednog validnog Hasha omogućava kreiranje bloka i osvajanje coinbase-a ili nagrade, koja trenutno iznosi 6.25 BTC plus transakcione naknade uključene u blok.


Ako kopaš sam, bićeš nagrađen samo kada pronađeš blok. U konkurenciji sa svim ostalim rudarima na planeti, imao/la bi vrlo male šanse da osvojiš ovu lutriju i još uvek bi morao/la da platiš naknade povezane sa korišćenjem svog uređaja bez ikakve garancije uspeha. Rudarenje rešava ovaj problem udruživanjem računarske snage nekoliko (hiljada) rudara i deljenjem njihovih nagrada na osnovu procenta učešća u Hashrateu bazena kada se pronađe blok. Da bi vizualizovao svoje šanse da sam pronađeš blok, možeš koristiti ovaj alat. Unoseći informacije za Antminer S9, možemo videti da su šanse za pronalaženje Hasha koji omogućava kreiranje bloka 1 u 24,777,849 za svaki blok ili 1 u 172,068 dnevno. U proseku (sa konstantnim Hashrate-om i težinom), trebalo bi najmanje 471 godina da se pronađe blok (kako težina raste).


Međutim, pošto je sve u Bitcoin zasnovano na verovatnoći, ponekad se dešava da solo rudari budu nagrađeni za preuzimanje ovog rizika: Solo Bitcoin Miner rešava blok sa Hash brzinom od samo 10 TH/s, pobedivši izuzetno male šanse – Decrypt


Ako volite da kockate, možete pokušati, ali naš vodič se neće fokusirati u tom pravcu. Umesto toga, koncentrisaćemo se na rudarske bazene koji najbolje odgovaraju našim potrebama za kreiranje sistema grejanja.


Prilikom izbora rudarskog bazena treba uzeti u obzir sistem nagrađivanja koji ima bazen, koji može varirati, kao i minimalni iznos potreban za isplatu nagrada na adresu. Na primer, Braiins, koji nudi softver o kojem ovde govorimo, takođe nudi bazen. Ovaj bazen ima sistem nagrađivanja nazvan "Score" koji podstiče rudare da rudare duže periode. Učešće uključuje faktor vremena rada izražen kao "scoring Hashrate". U našem slučaju, gde želimo sistem grejanja koji može biti uključen samo nekoliko minuta, ovo nije idealan sistem nagrađivanja. Preferiramo sistem nagrađivanja koji nam daje jednaku nagradu za svako učešće. Pored toga, minimalni iznos za isplatu sa Braiins Pool-a je 100.000 satošija, i isplata se vrši on-chain. Tako gubimo neke satošije u transakcijskim naknadama i deo naše nagrade može biti zaključan ako ne rudarimo dovoljno tokom zime.


Model nagrađivanja koji nas zanima je PPS, što znači "plaćanje po deonici". To znači da će rudar dobiti nagradu za svaku validnu deonicu. Postoji i varijanta ovog sistema, FPPS (Full Pay Per Share), koja ne samo da deli nagradu za coinbase, već i transakcione naknade uključene u blok. Rudarski bazeni koje preporučujemo za povezivanje vašeg uređaja za rudarenje i grejanje su Linecoin Pool (FPPS) i Nicehash (PPS).



- Nicehash: Prednost Nicehash-a je što se povlačenje može izvršiti koristeći Lightning uz minimalne naknade. Pored toga, minimalni iznos za povlačenje je 2000 satošija. Nedostatak je što Nicehash koristi svoju hash snagu za najprofitabilniju blokčejn mrežu, bez stvarne kontrole korisnika, tako da to ne mora nužno doprinositi Bitcoin hash snazi.



- Linecoin: Prednost Linecoina je broj funkcija koje nudi, kao što su detaljna kontrolna tabla, mogućnost povlačenja sa Paynym (BIP 47) za bolju zaštitu privatnosti, i integracija Telegram bota kao i direktno konfigurisane automatizacije u mobilnoj aplikaciji. Ovaj pool kopa samo Bitcoin blokove, ali minimalni iznos za povlačenje ostaje visok na 100,000 Sats. Detaljnije ćemo ispitati korisnički interfejs jednog od ovih bazena u budućem članku.


Da biste konfigurisali bazen u Braiins OS+, potrebno je da kreirate nalog u jednom od bazena po vašem izboru. Ovde ćemo uzeti primer Linecoin:


![image](assets/en/076.webp)


Kada je vaš nalog kreiran, kliknite na Connect To Pool


Zatim kopirajte Stratum adresu i vaše korisničko ime:


![image](assets/en/077.webp)


Sada se možete vratiti na Braiins OS+ interfejs da unesete ove kredencijale. Polje za lozinku možete ostaviti prazno.


![image](assets/en/078.webp)


## Optimizacija performansi vašeg Antminer S9


<chapterId>25380972-31c7-540d-80d8-17a06b171ca0</chapterId>


I overklokovanje i automatsko podešavanje frekvencija uključuju prilagođavanje brzina na hash pločama radi poboljšanja performansi ASIC uređaja. Razlika između njih leži u složenosti ovih podešavanja frekvencija.


Overclocking je jednostavna prilagođavanje koja uključuje povećanje frekvencije na hashing pločama kako bi se povećala Hash stopa mašine. Underclocking, s druge strane, uključuje smanjenje frekvencije takta integrisanog kola ispod njegove nominalne frekvencije. Smanjenjem frekvencije takta ASIC putem underclockinga, smanjuje se i toplota koju generiše hardver. Ovo omogućava smanjenje brzine ventilatora potrebnih za hlađenje ASIC, jer ne moraju raditi puno kako bi održali odgovarajuću temperaturu. Smanjenjem brzine ventilatora, smanjuje se i buka koju generiše ASIC. Ovo može biti posebno korisno za korisnike koji koriste ASIC kod kuće i žele minimizirati smetnje buke koje uzrokuje rudarska oprema.


Braiins OS+ podržava overklokovanje, underklokovanje ASIC-ova i automatsko podešavanje. Omogućava korisnicima da fleksibilno podešavaju frekvenciju takta svog hardvera kako bi maksimizovali performanse ili uštedeli energiju prema svojim preferencijama.


### Optimizacija performansi vašeg Antminer S9 sa automatskim podešavanjem


Pre 2018. godine, rudari su imali dva načina da steknu prednost u svojoj aktivnosti: pronalaženje električne energije po razumnoj ceni i kupovina efikasnijeg hardvera. Međutim, 2018. godine, otkriven je novi napredak u oblasti rudarskog softvera i firmvera, nazvan AsicBoost. Ova tehnika omogućava rudarima da smanje svoje troškove za približno 13% modifikovanjem firmvera koji radi na njihovim uređajima.


Danas postoji novi napredak u softverskom i firmverskom rudarskom sektoru pod nazivom autotuning, koji nudi još veću prednost od AsicBoost-a. ASIC-ovi se sastoje od mnogo malih računarskih čipova koji obavljaju heširanje. Ovi čipovi su napravljeni od silicijuma, istog elementa koji se široko koristi u poluprovodnicima i drugim mikroelektronskim komponentama. Ključno razumevanje ovde je da nisu svi silicijumski čipovi identični, svaki može blago varirati u svojim električnim svojstvima. Proizvođači hardvera su svesni toga i objavljuju specifikacije performansi svojih rudarskih mašina na osnovu donje granice njihovih tolerancija. Drugim rečima, proizvođači znaju frekvenciju koja najbolje radi za prosečne čipove i koriste ovu frekvenciju jednako za sve čipove u mašini.


Ovo postavlja gornju granicu na Hash stopu koju mašina može imati. Autotuning je proces u kojem algoritmi procenjuju optimalne frekvencije za heširanje po čipu, umesto da tretiraju celu mašinu kao jednu jedinicu. To znači da će čip višeg kvaliteta koji može da izvrši više hešova po sekundi dobiti višu frekvenciju, dok će čip nižeg kvaliteta koji može da izvrši relativno manje hešova dobiti nižu frekvenciju. Autotuning na nivou čipa je suštinski način da se optimizuje ASIC performansa putem softvera i firmvera koji se na njemu pokreću.


Krajnji rezultat je veća Hash stopa po vatu električne energije, što znači veće profitne marže za rudare. Razlog zbog kojeg se mašine ne isporučuju sa ovakvom vrstom softvera je taj što je varijabilnost mašina neželjena, jer kupci žele da tačno znaju šta dobijaju, pa je loša ideja za proizvođače da prodaju proizvod koji nema dosledne i predvidljive performanse od jedne mašine do druge. Pored toga, autotuning na nivou čipa zahteva značajne razvojne resurse, jer je složen za implementaciju. Proizvođači već troše mnogo resursa na razvoj sopstvenih firmvera. Postoje softverska rešenja koja omogućavaju autotuning, kao što je Braiins OS+. Pored toga, poboljšava performanse ASIC-a za čak 20%.


# Završni Deo


<partId>fa42ec0b-b1fd-47f6-8268-6eab684c1d2b</partId>


## Recenzije i Ocene


<chapterId>6af13742-df68-5cf4-b7aa-93dc0c2eaae9</chapterId>

<isCourseReview>true</isCourseReview>

## Završni ispit


<chapterId>f51a7c88-3b7e-48df-b45f-22bb10fe619f</chapterId>

<isCourseExam>true</isCourseExam>

## Zaključak


<chapterId>2941f29a-d6ce-4a3c-b61b-6e399f5395b1</chapterId>

<isCourseConclusion>true</isCourseConclusion>
