---
name: Smernice za lekturu
description: Koji su važni faktori koje treba imati na umu prilikom lekture na Plan ₿ Network?
---

![github](assets/cover.webp)


Dobrodošli u ovaj vodič o **smernicama koje treba pratiti prilikom lekture sadržaja na Plan ₿ Network**. Drago nam je što delite našu misiju da prevedemo materijale Bitcoin na što više jezika, kako bismo pomogli ljudima da steknu svest o tome kako funkcioniše i kako se može koristiti u njihovom svakodnevnom životu.


Prvo i najvažnije, doprinos Plan ₿ Network [javnom repozitorijumu](https://github.com/PlanB-Network/Bitcoin-educational-content) daje vam priliku da pišete tutorijale, lektorirate postojeći sadržaj ili čak predložite dodavanje novog jezika na platformu. Da biste saznali više, pridružite se našoj [Telegram grupi](https://t.me/PlanBNetwork_ContentBuilder) prvo, i napišite kratku prezentaciju o sebi i jezicima koje govorite.


Ovaj vodič je posvećen saradnicima koji žele da lektorišu sadržaj. Većina njih ne zna mnogo o [Github-u](https://planb.network/en/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c) ili o [Markdown jeziku](https://www.markdownguide.org/basic-syntax/) koji koristimo unutar repozitorijuma, pa je važno podeliti neka saznanja o ključnim faktorima uključenim u ovaj zadatak.


Ovde sam prikupio najčešće probleme sa kojima se lektori susreću. Slobodno predložite još, jer to može pomoći drugima da se poboljšaju.


Pre nego što pređete na detalje, prva stvar koju treba da uradite je da pročitate ovaj vodič o praktičnim akcijama koje treba pratiti na Github-u, forkovanjem Plan ₿ Network repozitorijuma, pravljenjem izmena i slanjem PR-ova:


https://planb.network/tutorials/contribution/content/contribution-proofreading-review-tutorial-1ee068ca-ddaf-4bec-b44e-b41a9abfdef6


## Šta je lektura?


Lektorisanje je završni proces pregleda pisanog teksta, kako bi se identifikovale i ispravile greške u gramatici, pravopisu, interpunkciji i formatiranju. Ono osigurava da je tekst jasan, koherentan i bez grešaka pre objavljivanja ili predaje.


Kada obavljate ovu vrstu zadatka, važno je pratiti značenje originalnog jezika (EN ili FR), ali se pobrinite da tekst na konačnom jeziku bude što tečniji za izvorne govornike.


Uvek zapamtite da je prevođenje/lektorisanje OBRAZOVANJE!


Zapravo, naš zajednički cilj je da edukujemo što više ljudi o Bitcoin, tako da je od suštinskog značaja da materijal koji čitaju bude jasan i razumljiv.

U tom smislu, svi saradnici na Plan ₿ Network su edukatori!


## Prvi koraci pre lekture na Plan ₿ Network


Pre nego što započnete novi zadatak lekture, najavite to u [Telegram grupi](https://t.me/PlanBNetwork_ContentBuilder) ili obavestite svog Plan ₿ Network koordinatora, koji će otvoriti posvećen [issue](https://github.com/orgs/PlanB-Network/projects/3). Kada dobijete link za issue, jednostavno **komentarišite da započinjete** sa zadatkom lekture tog sadržaja.


Ovaj sistem pomaže koordinatoru da prati napredak unutar repozitorijuma i omogućava da lektor "preuzme" sadržaj, sprečavajući dupliranje napora od strane nekog drugog.

Na samom pitanju, pronaći ćete linkove koji vas preusmeravaju na sadržaj za proveru. Možete jednostavno kliknuti na njih, ili, još bolje, možete se vratiti na svoj forkovani repo i raditi direktno odatle. Hajde da vidimo kako to možete uraditi!


Prvo i najvažnije, **UVEK zapamtite da SINHRONIZUJETE svoj repo, na "dev" grani**. Na ovaj način, sadržaj će uvek biti ažuriran pre nego što započnete bilo koju vrstu zadatka, i nećete stvoriti nikakve sukobe između starog i novog materijala. Obavezno kliknite na "Sync Fork" i "Update branch".



![REVIEW](assets/en/1.webp)



Nakon uspešnog sinhronizovanja, možete direktno pristupiti sadržaju od interesa i izvršiti promene na novoj grani, kao što je prikazano u ovom [uputstvu](https://planb.network/tutorials/contribution/content/contribution-proofreading-review-tutorial-1ee068ca-ddaf-4bec-b44e-b41a9abfdef6). U suprotnom, možete otvoriti novu granu na kojoj ćete raditi, klikom na "Branches", kao što je prikazano ispod.



![REVIEW](assets/en/2.webp)



Unutar ove nove stranice, pronaći ćete sve grane koje ste već otvorili pod naslovom "Vaše grane". Ovaj odeljak je veoma koristan jer vam omogućava da lako pronađete gde ste izmenili neki sadržaj. Ako želite da otvorite novu granu, možete kliknuti na "Nova grana" u gornjem desnom uglu stranice.



![REVIEW](assets/en/3.webp)



Zatim će se pojaviti iskačući prozor gde treba da unesete ime nove grane. U primeru ispod, odlučio sam da je nazovem "BTC101-FR". Na ovaj način, uvek ću se setiti da se ova specifična grana koristi za lekturu kursa BTC101 na francuskom, i **neću je koristiti za bilo koji drugi zadatak**.


Predlažem da uradiš isto: obavezno otvori novu granu svaki put kada treba da započneš novi zadatak.



![REVIEW](assets/en/4.webp)



Nakon kreiranja ove nove grane, obavezno kliknite na nju u odeljku "Vaše grane" na prethodnoj stranici i počnite rad na *.md* fajlu koji se odnosi na specifičan sadržaj (u mom slučaju, kliknuću na "courses" -> "BTC101" -> "fr.md"). Svi komitovi vezani za specifičan fajl moraju biti sačuvani unutar iste grane.



## Originalni jezik ili prevod?


Kada lektorirate sadržaj, važno je **uvek proveriti originalnu verziju na engleskom (ili francuskom)** jeziku. Imajte na umu da prevodimo koristeći AI jezičke alate, tako da prikaz na ciljanom jeziku možda neće biti tečan ili dobro razumljiv za krajnjeg čitaoca.


Stoga, slobodno izvršite prilagodbe teksta i modifikujte rečenice, ako je potrebno. Naš cilj je poboljšati tečnost, ali uvek prateći originalno značenje. U slučaju nedoumica o tome kako tretirati određenu reč, obavezno se obratite koordinatoru za prevod.


Alati LLM mogu prevesti neke reči povezane sa Bitcoin bukvalno, kao Lightning Network. To je naročito slučaj kada se radi o veoma tehničkim rečima. U ovakvim slučajevima, preporučljivo je zadržati originalnu englesku reč u vašem ciljanom jeziku radi bolje jasnoće, osim ako pravila vašeg jezika ne nalažu da prevedete svaku reč.


U ovom drugom slučaju, **uvek uradite istraživanje da vidite da li je neko drugi u vašoj Bitcoin zajednici već preveo tu reč** i da li se sada široko koristi.



- Jedno rešenje bi moglo biti da **proverite na [BitcoinWiki](https://en.Bitcoin.it/wiki/Main_Page)** na vašem ciljanom jeziku da vidite da li je reč prevedena ili ne. Ako nije, zadržavate reč na engleskom.



- U svakom slučaju, moj savet bi bio da **insert the EN word nonetheless**, dodajući odgovarajuće značenje na ciljanom jeziku unutar okruglih zagrada, prateći šemu EN (LANG), ili obrnuto. Npr. Address (indirizzo), ili indirizzo (Address).



- Još jedno dobro rešenje je da zadržite EN originalnu reč/frazu, zatim **kreirate hipervezu** koja preusmerava na [glossary](https://planb.network/en/resources/glossary) na planb.network. Da biste to uradili, potrebno je da umetnete reč/frazu unutar uglastih zagrada, a link unutar okruglih zagrada, kao što možete videti u primeru ispod:


```
[UTXO](https://planb.network/resources/glossary/utxo)
```


U konačnom rezultatu (slika ispod) nećete vizualizovati ceo link, a reč će postati kliktabilna.



![REVIEW](assets/en/5.webp)



Please note that the glossary link you will take from the website contains the language code after the word "network" (example: ``https://planb.network/resources/glossary/UTXO``-> here you can read the language code "en"). In this case, **remove the language code from the link**, like you saw in the box above. This way, the system will automatically take the reader to their designated language.


Sadržaj u repozitorijumu je pun hiperveza kao što su ove iznad. Sada kada znate šta znače, **pazite da ne obrišete nijednu vezu** koju je umetnuo originalni autor.



- Još jedna stvar vezana za prikazivanje reči je sledeća. Ako pronađete "Plan ₿ Network" u tekstu, **ostavite ga u ovom originalnom obliku**. Ne prevodite reč "plan" ili reč "network". Takođe, NE koristite član "The" kada predstavljate Plan ₿ Network: **smatrajte ga brendom**.



- Isto važi i za "₿-CERT", "BIZ SCHOOL", "TECH SCHOOL", što takođe treba zadržati u originalnom obliku.


Jedna poslednja napomena za ovaj pasus: kao što smo rekli gore, koristimo AI alate za prevođenje sadržaja, a zatim tražimo intervenciju saradnika kako bismo osigurali da je sve tečno i dobro lektorisano.


Ako koristiš AI za lekturu većine teksta, sigurno ćemo primetiti, jer smo upoznati sa tipičnim strukturama rečenica koje AI generiše. Ako ustanovimo da si se oslonio isključivo na AI za lekturu, bez primene značajnih izmena, konačna nagrada u Sats može biti smanjena za polovinu!



## Struktura zaglavlja


U jeziku markdown, zaglavlja (i naslovi paragrafa) počinju sa znakom Hash ``#``. Broj znakova Hash odgovara nivou zaglavlja. Na primer, zaglavlje nivoa tri ima tri znaka pre teksta (npr., `### Moje Zaglavlje`).


U kursevima, najvažniji delovi su predstavljeni jednim jedinim Hash znakom, dok poddelovi mogu imati od dva do četiri Hash znaka. U tutorijalima, obično koristimo samo naslove sa dva Hash znaka.



![REVIEW](assets/en/6.webp)



Pobrinite se da **NIKADA ne brišete Hash oznake** pre naslova, inače ćete stvoriti probleme sa strukturom teksta.


U isto vreme, **ne menjajte** deo chapterID koji možete videti na slici iznad, ``<chapterId>d668fdf6-fb4c-4bbf-82e1-afcb95c122e0</chapterId>`` ili reference na video kao što je ``:::video id=ba99951f-81d2-418f-b5e7-4b8c9f8b8cc8:::``.


Kada umetnemo ``#`` pre naslova, on će automatski postati podebljan u pregledu kursa, tako da **izbegavajte podebljavanje naslova tokom ispravke**.


Kao napomenu, u EN verziji kurseva, **naslovi uvedeni sa jednim ili dva ``#`` imaju sve reči koje počinju velikim slovima**, dok naslovi koji počinju sa tri ili četiri ``#`` obično ne prate ovo pravilo. Ako je moguće, osigurajte da naslovi u vašem ciljanom jeziku prate ovu strukturu.



## Početni deo kurseva


At the beginning of any content, you will find the following static lowercase words: "name", "description", "objectives". They are used by the website to decode the content itself and are **always left in EN**. As a consequence, DO NOT translate them, otherwise the content will create synchronization issues. Make sure to only proofread the part after the colon, which is automatically translated by AI.



![REVIEW](assets/en/7.webp)



U ovom istom početnom delu, zadrži format kakav jeste. Ne dodaj ništa na početku teksta. Na primer, izbegavaj dodavanje "tt" pre crtica, kao na slici ispod!



![REVIEW](assets/en/8.webp)



## Preporuke za formatiranje


Ispod možete pronaći nekoliko primera problema sa formatiranjem na koje treba obratiti pažnju prilikom lekture sadržaja na vašem ciljanom jeziku.



- Obratite pažnju na čudnu interpunkciju kao što je `\*\*\`, ili ``**`` što može predstavljati loše prikazivanje simbola za podebljavanje. Na slici ispod, možete videti da su zvezdice samo sa desne strane reči, što izgleda čudno.



![REVIEW](assets/en/9.webp)



Dakle, uvek proverite originalni engleski tekst da vidite da li bi tekst trebalo da bude podebljan. U ovom slučaju, samo dodajte dve zvezdice na početku reči, kako bi se pravilno prikazalo na vebsajtu. Zapravo, u markdown jeziku, **da biste prikazali podebljan tekst, morate umetnuti dve zvezdice ``**`` i pre i posle reči/rečenice** (pogledajte primer ispod).



![REVIEW](assets/en/10.webp)




- Isti problemi se mogu desiti sa simbolima kao što su $ i `` ` ``.

Obavezno proverite originalnu jezičku datoteku (često EN ili FR) da vidite gde bi ovi simboli trebalo da budu. Uvek možete zatražiti pomoć od koordinatora u vezi sa ovim pitanjem.



- Ako pronađete citate, obavezno istražite na internetu kako biste pronašli pravi prevod na vašem jeziku. Citati se obično ubacuju nakon simbola ``>``.



![REVIEW](assets/en/11.webp)



## Kviz lektura


Da li ste znali da možete i lektorisati pitanja za kviz u svakom kursu? Na primer, ako želite da lektorišete kvizove za BTC101 u IT-u, možete otvoriti posebnu granu i pratiti ovaj put: "courses" -> "BTC101" -> "quiz". Tamo ćete pronaći sve foldere posvećene svakom pitanju, zajedno sa pripadajućom jezičkom datotekom u _yml_ formatu.


Još jednom, uverite se da ste u posebnoj grani koju otvarate posebno za ovu svrhu, i uvek obavestite koordinatora.


Nakon pregleda pitanja, obavezno promenite status "reviewed" sa "false" na "true," kao što je prikazano na slici ispod.



![REVIEW](assets/en/12.webp)


## Lektura korekture rečnika


Baš kao i kvizove, možete lektorisati i rečnik. Originalni rečnik je napisan na francuskom, tako da ćete naći rečenice poput: "Na francuskom, ovaj izraz se može prevesti kao..."


U slučajevima poput ovog, molimo vas da prilagodite ovu rečenicu vašem ciljanom jeziku ili engleskom.


## Druge najbolje prakse



- Ako treba da pretražujete specifične reči unutar teksta, možete kliknuti na ``CTRL+F`` i pojaviće se deo za pronalaženje-zamenu. Ovaj deo je veoma koristan kada treba da skočite na određeni deo teksta, ili treba da zamenite specifične reči/rečenice u seriji, bez prelistavanja celog sadržaja.



![REVIEW](assets/en/13.webp)



Kada koristite funkciju "zameni sve", važno je dvaput proveriti rezultate kako biste osigurali da linkovi nisu takođe izmenjeni. Na primer, ako želite da promenite reč "Bitcoin" u "Bitkoin" (što može biti potrebno u nekim jezicima), korišćenje funkcije "zameni sve" može efikasno ažurirati sve instance u tekstu. Međutim, budite svesni da će ovaj alat takođe izmeniti sve linkove koji sadrže tu reč, što može dovesti do problema sa preusmeravanjem.


U primeru ispod, lektor je koristio gorenavedenu funkciju da zameni "Satoshi" sa "Satoshi(Sats)", i takođe promenio link ka tutorijalu koji sadrži samu reč. Kao posledica, link je postao nevažeći.


Uvek dvaput proverite sve hiperveze u tekstu, kako biste bili sigurni da su tačne.



![REVIEW](assets/en/14.webp)




- Prateći temu, ako autor umetne link koji se odnosi na Plan ₿ Network kurs ili tutorijal (**ne** unutar zagrada), vebsajt će automatski kreirati "kartu" koja prikazuje povezanu sličicu. Kao posledica toga, uvek se uverite da **imate razmak između teksta i samog linka**, inače biste mogli videti sledeću grešku na vebsajtu.



![REVIEW](assets/en/15.webp)





- Konačno, još jedna najbolja praksa koju treba primeniti kada završite zadatak lekture i pošaljete PR je da se vratite na originalni problem koji je otvorio koordinator i komentarišete sa "Proofreading done". **Obavezno tamo umetnite i link vašeg PR-a**.



## Zaključak


Ukratko, biti svestan uobičajenih grešaka lektora može vam zaista pomoći da poboljšate svoje veštine prilikom provere sadržaja. Lako je prevideti stvari poput konteksta ili doslednosti, a uočavanje ovih grešaka može napraviti veliku razliku.


Uvek imajte na umu da početnik može čitati ove kurseve i tutorijale, tako da je naša odgovornost da osiguramo da oni u potpunosti razumeju. Kao lektor, vi ste edukator!


Hvala što ste pročitali ovaj vodič i uživajte u svom putovanju kroz lekturu!