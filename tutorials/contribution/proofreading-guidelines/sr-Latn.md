---
name: Smernice za lekturu
description: Koji su važni faktori koje treba imati na umu prilikom lekture na Plan ₿ Academy?
---

![github](assets/cover.webp)


Dobrodošli u ovaj vodič o **smernicama koje treba pratiti prilikom lekture sadržaja na Plan ₿ Akademiji**. Drago nam je što delite našu misiju da prevedemo Bitcoin materijale na što više jezika, kako bismo pomogli ljudima da steknu svest o tome kako funkcioniše i kako se može koristiti u njihovom svakodnevnom životu.


Prvo i najvažnije, doprinos Plan ₿ Akademiji [javni repozitorijum](https://github.com/PlanB-Network/bitcoin-educational-content) daje vam priliku da pišete tutorijale, lektorirate postojeći sadržaj ili čak predložite dodavanje novog jezika na platformu. Da biste saznali više, pridružite se našoj [Telegram grupi](https://t.me/PlanBNetwork_ContentBuilder) prvo, i napišite kratku prezentaciju o sebi i jezicima koje govorite.


Ovaj vodič je posvećen saradnicima koji žele da lektorišu sadržaj. Većina njih ne zna mnogo o [Github-u](https://planb.academy/en/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c) ili [Markdown jeziku](https://www.markdownguide.org/basic-syntax/) koji koristimo unutar repozitorijuma, pa je važno podeliti neka saznanja o ključnim faktorima uključenim u ovaj zadatak.


Ovde sam prikupio najčešće probleme sa kojima se lektori susreću. Slobodno predložite još, jer to može pomoći drugima da se poboljšaju.


Pre nego što pređete na specifičnosti, prva stvar koju treba uraditi je pročitati ovaj vodič o praktičnim akcijama koje treba pratiti na Github-u, forkovanjem Plan ₿ Academy repozitorijuma, pravljenjem izmena i slanjem PR-ova:


https://planb.academy/tutorials/contribution/content/proofreading-review-tutorial-28236c98-23b2-4efd-9563-953f08707017


## Šta je lektura?


Lektorisanje je završni proces pregleda pisanog teksta, kako bi se identifikovale i ispravile greške u gramatici, pravopisu, interpunkciji i formatiranju. Osigurava da je tekst jasan, koherentan i bez grešaka pre objavljivanja ili predaje.


Kada obavljate ovu vrstu zadatka, važno je pratiti značenje originalnog jezika (EN ili FR), ali se pobrinite da tekst na konačnom jeziku bude što tečniji za izvorne govornike.


Uvek zapamtite da je prevođenje/lektorisanje OBRAZOVANJE!


Zapravo, naš zajednički cilj je da edukujemo što više ljudi o Bitcoin, tako da je od suštinskog značaja da materijal koji čitaju bude jasan i razumljiv.

U tom smislu, svi saradnici na Plan ₿ Akademiji su edukatori!


## Prvi koraci pre lekture na Plan ₿ Academy


Pre nego što započnete novi zadatak lekture, najavite to u [Telegram grupi](https://t.me/PlanBNetwork_ContentBuilder) ili obavestite svog koordinatora Plan ₿ Akademije, koji će otvoriti posvećen [issue](https://github.com/orgs/PlanB-Network/projects/3). Kada dobijete link za issue, jednostavno **komentarišite da započinjete** sa zadatkom lekture tog sadržaja.


Ovaj sistem pomaže koordinatoru da prati napredak unutar repozitorijuma i omogućava da sadržaj bude "preuzet" od strane lektora, sprečavajući dupliranje napora od strane nekog drugog.

Na samom pitanju, pronaći ćete linkove koji vas preusmeravaju na sadržaj za proveru. Možete jednostavno kliknuti na njih, ili, još bolje, možete se vratiti na svoj forkovani repo i raditi direktno odatle. Hajde da vidimo kako to možete uraditi!


Prvo i najvažnije, **UVEK zapamtite da SINHRONIZUJETE svoj repo, na "dev" grani**. Na ovaj način, sadržaj će uvek biti ažuriran pre nego što započnete bilo koju vrstu zadatka, i nećete stvoriti nikakve konflikte između starog i novog materijala. Obavezno kliknite na "Sync fork" i "Update branch".



![REVIEW](assets/en/1.webp)



Nakon uspešnog sinhronizovanja, možete direktno pristupiti sadržaju od interesa i izvršiti promene na novoj grani, kao što je prikazano u ovom [uputstvu](https://planb.academy/tutorials/contribution/content/proofreading-review-tutorial-28236c98-23b2-4efd-9563-953f08707017). U suprotnom, možete otvoriti novu granu na kojoj ćete raditi, klikom na "Branches", kao što je prikazano ispod.



![REVIEW](assets/en/2.webp)



Unutar ove nove stranice, pronaći ćete sve grane koje ste već otvorili pod naslovom "Vaše grane". Ovaj deo je veoma koristan jer vam omogućava da lako pronađete gde ste izmenili neki sadržaj. Ako želite da otvorite novu granu, možete kliknuti na "Nova grana" u gornjem desnom uglu stranice.



![REVIEW](assets/en/3.webp)



Zatim će se pojaviti iskačući prozor gde treba da unesete ime nove grane. U primeru ispod, odlučio sam da je nazovem "BTC101-FR". Na ovaj način, uvek ću se setiti da se ova specifična grana koristi za lekturu kursa BTC101 na francuskom, i **neću je koristiti za bilo koji drugi zadatak**.


Predlažem da uradiš isto: obavezno otvori novu granu svaki put kada treba da započneš novi zadatak.



![REVIEW](assets/en/4.webp)



Nakon kreiranja ove nove grane, obavezno kliknite na nju u odeljku "Vaše grane" na prethodnoj stranici i počnite da radite na *.md* fajlu koji se odnosi na specifičan sadržaj (u mom slučaju, kliknuću na "courses" -> "BTC101" -> "fr.md"). Svi komitovi vezani za specifičan fajl moraju biti sačuvani unutar iste grane.



## Originalni jezik ili prevod?


Kada lektorirate sadržaj, važno je **uvek proveriti originalnu verziju na engleskom (ili francuskom)** jeziku. Imajte na umu da prevodimo koristeći AI jezičke alate, tako da prikaz na ciljanom jeziku možda neće biti tečan ili dobro razumljiv za krajnjeg čitaoca.


Stoga, slobodno izvršite prilagodbe teksta i modifikujte rečenice, ako je potrebno. Naš cilj je poboljšati tečnost, ali uvek prateći originalno značenje. U slučaju nedoumica oko tretiranja određene reči, obavezno se obratite koordinatoru za prevod.


Alati LLM mogu prevesti neke reči povezane sa Bitcoin bukvalno, kao Lightning Network. To je posebno slučaj kada se radi o veoma tehničkim rečima. U ovakvim slučajevima, preporučljivo je zadržati originalnu englesku reč u vašem ciljanom jeziku radi bolje jasnoće, osim ako pravila vašeg jezika ne nalažu da prevedete svaku reč.


U ovom drugom slučaju, **uvek istražite da li je neko drugi u vašoj Bitcoin zajednici već preveo tu reč** i da li se sada široko koristi.



- Jedno rešenje bi moglo biti da **proverite na [BitcoinWiki](https://en.bitcoin.it/wiki/Main_Page)** na vašem ciljanom jeziku da vidite da li je reč prevedena ili ne. Ako nije, zadržavate reč na engleskom.



- U svakom slučaju, moj savet bi bio da **insert the EN word nonetheless**, dodajući odgovarajuće značenje na ciljanom jeziku unutar okruglih zagrada, prateći šemu EN (LANG), ili obrnuto. Npr. Address (indirizzo), ili indirizzo (address).



- Još jedno dobro rešenje je da zadržite EN originalnu reč/frazu, zatim **kreirate hipervezu** koja preusmerava na [glosar](https://planb.academy/en/resources/glossary) na planb.network. Da biste to uradili, potrebno je da umetnete reč/frazu unutar uglastih zagrada, a link unutar okruglih zagrada, kao što možete videti u primeru ispod:


```
[UTXO](https://planb.academy/resources/glossary/utxo)
```


U konačnom rezultatu (slika ispod) nećete videti ceo link, a reč će postati kliktabilna.



![REVIEW](assets/en/5.webp)



Imajte na umu da link do rečnika koji ćete preuzeti sa veb-sajta sadrži kod jezika nakon reči "network" (primer: ``https://planb.academy/en/resources/glossary/utxo``-> ovde možete pročitati kod jezika "en"). U ovom slučaju, **uklonite kod jezika iz linka**, kao što ste videli u gornjem okviru. Na taj način, sistem će automatski odvesti čitaoca na njihov određeni jezik.


Sadržaj u repozitorijumu je pun hiperveza kao što su ove iznad. Sada kada znate šta znače, **pazite da ne obrišete nijednu vezu** koju je umetnuo originalni autor.



- Još jedna stvar vezana za prikazivanje reči je sledeća. Ako pronađete "Plan ₿ Academy" u tekstu, **ostavite ga u ovom originalnom obliku**. Nemojte prevoditi reč "plan" ili reč "network". Takođe, NE koristite član "The" kada predstavljate Plan ₿ Academy: **smatrajte ga brendom**.



- Isto važi i za "₿-CERT", "BIZ SCHOOL", "TECH SCHOOL", što takođe treba zadržati u originalnom obliku.


Jedna konačna napomena za ovaj pasus: kao što smo rekli gore, koristimo AI alate za prevođenje sadržaja, a zatim tražimo intervenciju saradnika kako bismo osigurali da je sve tečno i dobro lektorisano.


Ako koristite veštačku inteligenciju za lekturu većine teksta, sigurno ćemo primetiti, jer smo upoznati sa tipičnim strukturama rečenica koje generiše veštačka inteligencija. Ako ustanovimo da ste se oslanjali isključivo na veštačku inteligenciju za lekturu, bez primene značajnih izmena, konačna nagrada u sats može biti smanjena za polovinu!



## Struktura zaglavlja


U jeziku markdown, zaglavlja (i naslovi paragrafa) počinju sa znakom tarabe ``#``. Broj znakova tarabe odgovara nivou zaglavlja. Na primer, zaglavlje nivoa tri ima tri znaka tarabe pre teksta (npr., `### Moje Zaglavlje`).


U kursevima, najvažniji delovi su predstavljeni jednim znakom tarabe, dok poddelovi mogu imati od dva do četiri znaka tarabe. U tutorijalima, obično koristimo zaglavlja sa dva znaka tarabe.



![REVIEW](assets/en/6.webp)



Uverite se da **NIKADA ne brišete znakove tarabe** pre naslova, inače ćete stvoriti probleme sa strukturom teksta.


U isto vreme, **ne menjajte** deo chapterID koji možete videti na slici iznad, ``<chapterId>d668fdf6-fb4c-4bbf-82e1-afcb95c122e0</chapterId>`` ili reference na video kao što je ``:::video id=ba99951f-81d2-418f-b5e7-4b8c9f8b8cc8:::``.


Kada umetnemo ``#`` pre naslova, on će automatski postati podebljan u pregledu kursa, tako da **izbegavajte podebljavanje naslova tokom ispravke**.


Kao napomenu, u EN verziji kurseva, **naslovi uvedeni sa jednim ili dva ``#`` imaju sve reči koje počinju velikim slovima**, dok naslovi koji počinju sa tri ili četiri ``#`` obično ne prate ovo pravilo. Ako je moguće, pobrinite se da naslovi u vašem ciljanom jeziku prate ovu strukturu.



## Početni deo kurseva


Na početku bilo kog sadržaja, pronaći ćete sledeće statične reči malim slovima: "name", "description", "objectives". One se koriste od strane vebsajta za dekodiranje samog sadržaja i **uvek ostaju na EN**. Kao posledica toga, NEMOJTE ih prevoditi, inače će sadržaj stvoriti probleme sa sinhronizacijom. Uverite se da samo lektorirate deo posle dvotačke, koji automatski prevodi AI.



![REVIEW](assets/en/7.webp)



U ovom istom početnom delu, zadrži format kakav jeste. Ne dodaj ništa na početku teksta. Na primer, izbegavaj dodavanje "tt" pre crtica, kao na slici ispod!



![REVIEW](assets/en/8.webp)


## Kako se nositi sa slikama kursa


Naš vebsajt sada sadrži prevedene slike za skoro svaki kurs!


Kada lektoriraš, uvek proveri da su sve slike prisutne i ispravno prikazane. U `code view`, ako pronađeš ovakvu liniju `![IMAGE](assets/en/001.webp)`, to znači da će tu biti prikazana slika.


Uverite se da uvek dodajete novi red između koda slike i teksta. Primer ispod:


```
WRONG CONFIGURATION:
- to start translating, click on the button `Translate`: ![language](assets/08.webp)
To save, click on `save`!


RIGHT CONFIGURATION:

- to start translating, click on the button `Translate`:

![language](assets/08.webp)

To save, click on `save`!
```



Osim toga, zapamtite da pročitate sadržaj svake slike. Ako primetite bilo kakve probleme sa prevodom teksta unutar slika, obavestite svog koordinatora i dobićete priliku da ih i vi lektorišete!


Možete vizualizovati sliku u odeljku `Preview` na Github-u (ili na našem sajtu, otvorite u drugoj kartici). Zatim, vratite se u odeljak `code` pored njega za lekturu.


![REVIEW](assets/en/9.webp)


## Preporuke za formatiranje


Ispod možete pronaći nekoliko primera problema sa formatiranjem na koje treba obratiti pažnju prilikom lekture sadržaja na vašem ciljanom jeziku.



- Obratite pažnju na čudnu interpunkciju kao što je `\*\*\`, ili ``**`` što može predstavljati loše prikazivanje simbola za podebljavanje. Na slici ispod, možete videti da su zvezdice samo sa desne strane reči, što izgleda čudno.



![REVIEW](assets/en/10.webp)



Dakle, uvek proverite originalni engleski tekst da vidite da li je podebljan tekst predviđen. U tom slučaju, samo dodajte dve zvezdice na početku reči, da bi se ispravno prikazalo na vebsajtu. Zapravo, u markdown jeziku, **da biste prikazali podebljan tekst, morate umetnuti dve zvezdice ``**`` i pre i posle reči/rečenice** (pogledajte primer ispod).



![REVIEW](assets/en/11.webp)




- Isti problemi se mogu desiti sa simbolima kao što su $ i `` ` ``.

Obavezno proverite originalnu jezičku datoteku (često EN ili FR) da vidite gde bi ovi simboli trebalo da budu. Uvek možete zatražiti pomoć od koordinatora u vezi sa ovim pitanjem.



- Ako pronađete citate, obavezno istražite na internetu kako biste pronašli pravi prevod na vašem jeziku. Citati se obično ubacuju nakon simbola ``>``.



![REVIEW](assets/en/12.webp)




## Lektura tutorijala


Ako odlučite da lektorirate tutorijale, koordinator će otvoriti poseban zadatak za **ceo odeljak tutorijala**. Kada završite svoj zadatak, možete dokumentovati svoj napredak komentarišući u zadatku sa listom pregledanih tutorijala: na ovaj način kreirate jasan sistem praćenja za buduću referencu, što je važno jer se novi sadržaj dodaje svakog meseca. Primer ovog pristupa možete videti [ovde](https://github.com/PlanB-Network/bitcoin-educational-content/issues/3023#issuecomment-3364923190).


![REVIEW](assets/en/13.webp)


Pošto se novi tutorijali dodaju mesečno, vaša grana može postati zastarela tokom procesa lekture. Neki lektori su pristupili ovom problemu sinhronizacijom tačne grane na kojoj rade: **molimo vas da to NIKADA ne radite! Ako to uradite, rizikujete da izgubite sav napredak koji ste postigli do tog trenutka!**


Umesto toga, prvo bi trebalo da završiš lekturu tutorijala u svom trenutnom fork. Zatim, **sinhronizuj `dev`**, i kreiraj novu granu gde ćeš se fokusirati na lekturu novododatih tutorijala (samo onih koji nedostaju iz tvoje prethodne grane).


U uputstvima, postoji šansa da **slike možda neće biti prevedene**. Pošto je većina uputstava **originalno napisana na francuskom ili engleskom**, verovatno ćete naići na slike koje sadrže komande ili instrukcije na njihovom originalnom jeziku. Uzmimo primer iz uputstva o Sparrow na holandskom, tako što ćemo navesti i tekst i povezanu sliku.


```
Verbinding maken met een openbaar knooppunt is heel eenvoudig. Klik op het tabblad "_Publieke server_".
```


![REVIEW](assets/en/14.webp)


Kao što možete videti, slika jasno ukazuje na `Public Server`, na engleskom, dok tekst pominje izraz `_Publieke server_`. U ovom slučaju, postoji problem sa koherentnošću, jer čitalac nailazi na konfliktne informacije kada uporedi sliku sa tekstom.


Da biste rešili ovaj problem, možete uneti komandu kako se pojavljuje na slici (na engleskom ili francuskom), praćenu prevodom na vaš jezik unutar zagrada, kao što je prikazano ispod:


```
Verbinding maken met een openbaar knooppunt is heel eenvoudig. Klik op het tabblad "_Public Server_" (Publieke server).
```



## Kviz lektura


Da li ste znali da možete i lektorisati pitanja za kviz u svakom kursu? Na primer, ako želite da lektorišete kvizove za BTC101 u IT-u, možete otvoriti posebnu granu i pratiti ovaj put: "courses" -> "BTC101" -> "quiz". Tamo ćete pronaći sve foldere posvećene svakom pitanju, zajedno sa odgovarajućom jezičkom datotekom u _yml_ formatu.


Još jednom, uverite se da ste u posebnoj grani koju otvarate specifično za ovu svrhu, i uvek obavestite koordinatora.


Važna stvar koju treba imati na umu prilikom lekture ove vrste _yml_ datoteke je izbegavanje dodavanja dvotački ``:`` ili navodnika unutar teksta. Zapravo, dvotačka se koristi **samo** za razdvajanje parova ključ-vrednost kao što je "wrong_answers" od ostatka. Primer možete videti na slici ispod:


![REVIEW](assets/en/15.webp)


After reviewing the question, make sure you change the "reviewed" status from "false" to "true," as shown in the image below. Make sure to **keep these status words in English**, no matter what language you are working on!



![REVIEW](assets/en/16.webp)


Ako nedostaje statusna linija "reviewed:true", obavezno je **dodajte na kraj kviza**.


## Lektura korekture rečnika


Baš kao i kvizove, možete i lektorisati rečnik. Originalni rečnik je napisan na francuskom, tako da ćete naći rečenice poput: "Na francuskom, ovaj izraz se može prevesti kao..."


U slučajevima poput ovog, molimo vas da prilagodite rečenicu ciljanom jeziku ili engleskom. Na primer, možete napisati "Na engleskom, ovaj izraz...".

Ako je naslov ostavljen na engleskom, možete prilagoditi rečenicu svom jeziku: "Na svahiliju, ovaj izraz..."


Dodatno, pobrinite se da naslove pišete VELIKIM SLOVIMA.


![REVIEW](assets/en/17.webp)



## Naslov i opis vašeg PR-a


Kada pošaljete svoj PR, bilo bi sjajno ako biste ga nazvali koristeći ovaj format: [PROOFREADING] CONTENT NAME - LANGUAGE:


```
[PROOFREADING] BTC101 - ENGLISH
```


Pored toga, u **odeljku za komentare PR-a**, možete napisati "closes" + broj problema koji vam je koordinator poslao kada ste započeli zadatak lekture, prethodno dodajući ``#``.

Na primer, ako ste upravo poslali PR sa lekturom cyp201 + kvizova, možete napisati "closes [#2934](https://github.com/PlanB-Network/bitcoin-educational-content/issues/2934)".


Na ovaj način, PR i problem će biti povezani, i svako ko čita javni Github repozitorijum može lako pronaći informacije.



## Druge najbolje prakse



- Ako treba da pretražujete specifične reči unutar teksta, možete kliknuti na ``CTRL+F`` i pojaviće se deo za pronalaženje-zamenu. Ovaj deo je veoma koristan kada treba da skočite na određeni deo teksta, ili treba da zamenite specifične reči/rečenice u seriji, bez listanja celog sadržaja.



![REVIEW](assets/en/18.webp)



Kada koristite funkciju "zameni sve", važno je dvaput proveriti rezultate kako biste osigurali da linkovi nisu takođe izmenjeni. Na primer, ako želite da promenite reč "Bitcoin" u "Bitkoin" (što može biti potrebno u nekim jezicima), korišćenje funkcije "zameni sve" može efikasno ažurirati sve instance u tekstu. Međutim, budite svesni da će ovaj alat takođe izmeniti sve linkove koji sadrže tu reč, što potencijalno može dovesti do problema sa preusmeravanjem.


U primeru ispod, lektor je koristio gorenavedenu funkciju da zameni "satoshi" sa "satoshi(sats)", i takođe promenio link ka tutorijalu koji sadrži samu reč. Kao posledica, link je postao nevažeći.


Uvek dvaput proverite sve hiperveze u tekstu, kako biste bili sigurni da su tačne.



![REVIEW](assets/en/19.webp)




- Slijedeći temu, ako autor umetne link koji se odnosi na kurs ili tutorijal Plan ₿ Akademije (**ne** unutar zagrada), vebsajt će automatski kreirati "karticu" koja prikazuje povezanu sličicu. Kao posledica toga, uvek se pobrinite da **dodate novi red između teksta i samog linka**, inače biste mogli videti sledeću grešku na vebsajtu.



![REVIEW](assets/en/20.webp)



## Zaključak


Da sumiramo, biti svestan uobičajenih grešaka lektora zaista može pomoći u poboljšanju vaših veština prilikom provere sadržaja. Lako je prevideti stvari poput konteksta ili doslednosti, a uočavanje ovih grešaka može napraviti veliku razliku.


Uvek imajte na umu da početnik može čitati ove kurseve i tutorijale, tako da je naša odgovornost da osiguramo da oni u potpunosti razumeju. **Kao lektor, vi ste edukator!**


Sada ste spremni da počnete sa kursevima lekture, tutorijalima, kvizovima i rečima iz rečnika. Ostanite u toku kako biste počeli sa proverom transkripata video zapisa!


Hvala što ste pročitali ovaj vodič i uživajte u svom putovanju lekture!