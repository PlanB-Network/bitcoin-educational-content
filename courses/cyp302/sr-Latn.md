---
name: Uvod u formalnu Kriptografiju
goal: Duboko uranjanje u nauku i praksu kriptografije.
objectives: 

  - Istražite Beale šifre i moderne kriptografske metode kako biste razumeli osnovne i istorijske koncepte kriptografije.
  - Uronite se u teoriju brojeva, grupe i polja kako biste savladali ključne matematičke pojmove koji su osnova kriptografije.
  - Proučite RC4 stream šifru i AES sa 128-bitnim ključem da biste saznali više o simetričnim kriptografskim algoritmima.
  - Istražite RSA kriptosistem, distribuciju ključeva i Hash funkcije kako biste istražili asimetričnu kriptografiju.


---
# Duboko zaronite u kriptografiju


Teško je pronaći mnogo materijala koji nude dobru sredinu u obrazovanju o kriptografiji.


S jedne strane, postoje dugački, formalni traktati, zaista dostupni samo onima sa jakom pozadinom u matematici, logici ili nekoj drugoj formalnoj disciplini. S druge strane, postoje veoma uvodne prezentacije koje zaista skrivaju previše detalja za svakoga ko je makar malo radoznao.


Ovaj uvod u kriptografiju nastoji da zauzme srednji put. Iako bi trebalo da bude relativno izazovan i detaljan za svakoga ko je nov u kriptografiji, nije zečja rupa tipičnog osnovnog traktata.


+++

# Uvod

<partId>bbed2f46-d64c-5fb5-b892-d726032f2494</partId>


## Pregled kursa

<chapterId>bb8a8b73-7fb2-50da-bf4e-98996d79887b</chapterId>

Dobrodošli na kurs CYP302!


Ova knjiga nudi dubinsko uvodno proučavanje nauke i prakse kriptografije. Gde god je moguće, fokusira se na konceptualno, a ne formalno izlaganje materijala.



Ovaj obrazovni sadržaj je adaptiran iz knjige i repo [JWBurgers](https://github.com/JWBurgers/An_Introduction_to_Cryptography). Iako je autor ljubazno dozvolio njegovu obrazovnu upotrebu, sva prava intelektualne svojine ostaju kod originalnog stvaraoca.

**Motivacija i ciljevi**


Teško je pronaći mnogo materijala koji nude dobru sredinu u obrazovanju o kriptografiji.


S jedne strane, postoje dugački, formalni traktati, zaista dostupni samo onima sa snažnom pozadinom u matematici, logici ili nekoj drugoj formalnoj disciplini. S druge strane, postoje vrlo uvodne prezentacije na visokom nivou koje zaista skrivaju previše detalja za svakoga ko je makar malo radoznao.


Ovaj uvod u kriptografiju nastoji da zauzme srednji put. Iako bi trebalo da bude relativno izazovan i detaljan za svakoga ko je nov u kriptografiji, nije zečja rupa tipičnog osnovnog traktata.



**Ciljna publika**


Od programera do intelektualno radoznalih, ova knjiga je korisna za svakoga ko želi više od površnog razumevanja kriptografije. Ako vam je cilj da ovladate poljem kriptografije, onda je ova knjiga takođe dobra početna tačka.



**Uputstva za čitanje**


Knjiga trenutno sadrži sedam poglavlja: "Šta je kriptografija?" (Poglavlje 1), "Matematičke osnove kriptografije I" (Poglavlje 2), "Matematičke osnove kriptografije II" (Poglavlje 3), "Simetrična kriptografija" (Poglavlje 4), "RC4 i AES" (Poglavlje 5), "Asimetrična kriptografija" (Poglavlje 6) i "RSA kriptosistem" (Poglavlje 7). Završno poglavlje, "Kriptografija u praksi," će još biti dodato. Ono se fokusira na razne kriptografske primene, uključujući sigurnost transporta Layer, onion routing i Bitcoin-ov sistem vrednosti Exchange.


Osim ako nemate snažnu pozadinu u matematici, teorija brojeva je verovatno najteža tema u ovoj knjizi. Nudim pregled u Poglavlju 3, a pojavljuje se i u izlaganju AES-a u Poglavlju 5 i RSA kriptosistema u Poglavlju 7.


Ako se zaista mučite sa formalnim detaljima u ovim delovima knjige, preporučujem da se prvi put zadovoljite čitanjem na visokom nivou.



**Zahvalnice**


Najuticajnija knjiga koja je oblikovala ovu je _Introduction to Modern Cryptography_ Jonathana Katza i Yehude Lindella, CRC Press (Boca Raton, FL), 2015. Prateći kurs je dostupan na Courseri pod nazivom "Cryptography."


Glavni dodatni izvori koji su bili od pomoći u kreiranju pregleda u ovoj knjizi su Simon Singh, _The Code Book_, Fourth Estate (London, 1999); Christof Paar i Jan Pelzl, _Understanding Cryptography_, Springer (Heidelberg, 2010) i [kurs zasnovan na knjizi Paar pod nazivom “Introduction to Cryptography”](https://www.youtube.com/channel/UC1usFRN4LCMcfIV7UjHNuQg); i Bruce Schneier, Applied Cryptography, 2nd edn, 2015 (Indianapolis, IN: John Wiley & Sons).


Navešću samo vrlo specifične informacije i rezultate koje preuzimam iz ovih izvora, ali želim ovde da izrazim svoju opštu zahvalnost prema njima.


Za one čitaoce koji žele da potraže naprednije znanje o kriptografiji nakon ovog uvoda, toplo preporučujem knjigu Katza i Lindella. Katzov kurs na Courseri je donekle pristupačniji od knjige.



**Doprinosi**


Molimo pogledajte [datoteku sa doprinosima u spremištu](https://github.com/JWBurgers/An_Introduction_to_Cryptography/blob/master/Contributions.md) za neke smernice o tome kako podržati projekat.



**Notacija**


**Ključni pojmovi:**


Ključni pojmovi u priručnicima se uvode tako što se podebljavaju. Na primer, uvođenje šifre Rijndael kao ključnog pojma bi izgledalo ovako: **šifra Rijndael**.


Ključni pojmovi su eksplicitno definisani, osim ako su vlastita imena ili je njihovo značenje očigledno iz diskusije.


Bilo koja definicija se obično daje prilikom uvođenja ključnog pojma, iako je ponekad pogodnije ostaviti definiciju za kasniji trenutak.



**Naglašene reči i fraze:**


Reči i fraze su naglašene putem italika. Na primer, fraza "Remember your password" bi izgledala ovako: *Remember your password*.



**Formalna notacija:**


Formalna notacija se uglavnom odnosi na promenljive, slučajne promenljive i skupove.



- Varijable: One su obično označene malim slovom (npr. "x" ili "y"). Ponekad su velikim slovima radi jasnoće (npr. "M" ili "K").
- Nasumične promenljive: One su uvek označene velikim slovom (npr., "X" ili "Y")
- Skupovi: Uvek su označeni podebljanim, velikim slovima (npr., **S**)


Spremni da istražimo fascinantan svet kriptografije? Krenimo!


# Šta je Kriptografija?

<partId>48e4d6d5-cd00-5c00-8adb-ae8477ff47c4</partId>


## Beale šifre

<chapterId>ae674346-4789-5ab1-9b6f-c8989d83be89</chapterId>


Hajde da započnemo naše istraživanje u oblasti kriptografije jednim od šarmantnijih i zabavnijih epizoda u njenoj istoriji: onom o Beale šiframa. [1]


Priča o Beale šiframa je, po mom mišljenju, verovatnije fikcija nego stvarnost. Ali navodno se dogodila ovako.


I tokom zime 1820. i 1822. godine, čovek po imenu Thomas J. Beale boravio je u gostionici koju je posedovao Robert Morriss u Lynchburgu (Virginia). Na kraju Bealeovog drugog boravka, predao je Morrissu gvozdenu kutiju sa vrednim dokumentima na čuvanje.


Nekoliko meseci kasnije, Morriss je primio pismo od Bealea datirano na 9. maj 1822. U njemu je naglašena velika vrednost sadržaja gvozdene kutije i navedena su neka uputstva za Morrissa: ako ni Beale ni bilo koji od njegovih saradnika nikada ne dođu da preuzmu kutiju, trebalo bi da je otvori tačno deset godina od datuma pisma (to jest, 9. maja 1832). Neki od papira unutra biće napisani u običnom tekstu. Nekoliko drugih, međutim, biće „nerazumljivi bez pomoći ključa.“ Taj „ključ“ bi, zatim, trebalo da bude dostavljen Morrissu od strane neimenovanog Bealeovog prijatelja u junu 1832.


Uprkos jasnim instrukcijama, Morriss nije otvorio kutiju u maju 1832. godine i Bealeov misteriozni prijatelj se nikada nije pojavio u junu te godine. Tek 1845. godine gostioničar je konačno odlučio da otvori kutiju. U njoj je Morriss pronašao belešku koja objašnjava kako su Beale i njegovi saradnici otkrili zlato i srebro na Zapadu i zakopali ih, zajedno sa nekim nakitom, radi sigurnosti. Pored toga, kutija je sadržala tri **šifrovana teksta**: to jest, tekstove napisane u kodu koji zahtevaju **kriptografski ključ**, ili tajnu, i prateći algoritam za otključavanje. Ovaj proces otključavanja šifrovanog teksta poznat je kao **dešifrovanje**, dok je proces zaključavanja poznat kao **šifrovanje**. (Kao što je objašnjeno u Poglavlju 3, termin šifra može imati različita značenja. U nazivu "Bealeove šifre", to je skraćenica za šifrovane tekstove.)


Tri šifrovana teksta koja je Morriss pronašao u gvozdenoj kutiji sastoje se od niza brojeva odvojenih zarezima. Prema Bealeovoj belešci, ovi šifrovani tekstovi zasebno pružaju lokaciju blaga, sadržaj blaga i spisak imena sa zakonitim naslednicima blaga i njihovim udelima (poslednja informacija je relevantna u slučaju da Beale i njegovi saradnici nikada ne dođu da preuzmu kutiju).


Morris je pokušavao da dešifruje tri šifrovana teksta dvadeset godina. Ovo bi bilo lako sa ključem. Ali Morris nije imao ključ i nije bio uspešan u svojim pokušajima da povrati originalne tekstove, ili **otvorene tekstove** kako se obično nazivaju u kriptografiji.


Pred kraj svog života, Morriss je 1862. godine predao kutiju prijatelju. Taj prijatelj je kasnije, 1885. godine, objavio pamflet pod pseudonimom J.B. Ward. U njemu je bio opisan (navodni) istorijat kutije, tri šifrovana teksta i rešenje koje je pronašao za drugi šifrovani tekst. (Izgleda da postoji jedan ključ za svaki šifrovani tekst, a ne jedan ključ koji funkcioniše za sva tri šifrovana teksta, kao što je Beale prvobitno izgleda sugerisao u svom pismu Morrissu.)


Možete videti drugi šifrovani tekst na *Slici 2* ispod. [2] Ključ za ovaj šifrovani tekst je Deklaracija nezavisnosti Sjedinjenih Američkih Država. Procedura dešifrovanja se svodi na primenu sledeća dva pravila:



- Za bilo koji broj n u šifrovanom tekstu, pronađite n-tu reč u Deklaraciji nezavisnosti Sjedinjenih Američkih Država.
- Zameni broj n prvim slovom reči koju si pronašao.



*Slika 1: Beale šifra br. 2*


![Figure 1: Beale cipher no 2.](assets/Figure1-1.webp "Figure 1: Beale cipher no. 2")



Na primer, prvi broj drugog šifrovanog teksta je 115. 115. reč u Deklaraciji nezavisnosti je „instituted“, tako da je prvo slovo otvorenog teksta „i“. Šifrovani tekst ne ukazuje direktno na razmake između reči i velika slova. Ali nakon dešifrovanja prvih nekoliko reči, možete logično zaključiti da je prva reč otvorenog teksta jednostavno bila „I.“ (Otvoreni tekst počinje frazom „I have deposited in the county of Bedford.“)


Nakon dešifrovanja, druga poruka pruža detaljan sadržaj blaga (zlato, srebro i dragulji), i sugeriše da je zakopano u gvozdenim loncima i prekriveno kamenjem u okrugu Bedford (Virdžinija). Ljudi vole dobru misteriju, pa su uloženi veliki napori u dešifrovanje druga dva Beale šifra, posebno onog koji opisuje lokaciju blaga. Čak su i razni istaknuti kriptografi pokušali da ih reše. Međutim, do sada niko nije uspeo da dešifruje druga dva šifrovana teksta.



**Beleške:**


[1] Za dobar rezime priče, pogledajte Simon Singh, *The Code Book*, Fourth Estate (London, 1999), str. 82-99. Kratki film o priči snimio je Andrew Allen 2010. godine. Film možete pronaći, “The Thomas Beale Cipher,” [na njegovoj veb stranici](http://www.thomasbealecipher.com/).


[2] Ova slika je dostupna na Wikipedia stranici za Beale šifre.



## Moderna kriptografija

<chapterId>d07d576f-8a4b-5890-b182-2e5763f550f4</chapterId>


Šarene priče poput one o Beale šiframa su ono što većina nas povezuje sa kriptografijom. Ipak, moderna kriptografija se razlikuje na najmanje četiri važna načina od ovih tipova istorijskih primera.


Prvo, istorijski gledano, kriptografija se bavila samo **tajnošću** (ili poverljivošću). [3] Šifrovani tekstovi bi bili kreirani kako bi se osiguralo da samo određene strane mogu imati pristup informacijama u otvorenim tekstovima, kao u slučaju Beale-ovih šifara. Da bi šema enkripcije dobro služila ovoj svrsi, dešifrovanje šifrovanog teksta trebalo bi da bude izvodljivo samo ako imate ključ.


Moderna kriptografija se bavi širim spektrom tema od same tajnosti. Ove teme uključuju prvenstveno (1) **integritet poruke**—odnosno, osiguranje da poruka nije izmenjena; (2) **autentičnost poruke**—odnosno, osiguranje da poruka zaista dolazi od određenog pošiljaoca; i (3) **neporecivost**—odnosno, osiguranje da pošiljalac kasnije ne može lažno poreći da je poslao poruku. [4]


Važno je imati na umu razliku između **šeme enkripcije** i **kriptografske šeme**. Šema enkripcije se bavi samo tajnošću. Iako je šema enkripcije kriptografska šema, obrnuto nije tačno. Kriptografska šema može služiti i drugim glavnim temama kriptografije, uključujući integritet, autentičnost i neporecivost.


Teme integriteta i autentičnosti su jednako važne kao i tajnost. Naši moderni komunikacioni sistemi ne bi mogli da funkcionišu bez garancija u vezi sa integritetom i autentičnošću komunikacija. Neporecivost je takođe važna briga, kao na primer za digitalne ugovore, ali je manje sveprisutno potrebna u kriptografskim aplikacijama nego tajnost, integritet i autentičnost.


Drugo, klasične šeme šifrovanja kao što su Beale šifre uvek uključuju jedan ključ koji je deljen među svim relevantnim stranama. Međutim, mnoge moderne kriptografske šeme uključuju ne samo jedan, već dva ključa: **privatni** i **javni ključ**. Dok prvi treba da ostane privatan u svim aplikacijama, drugi je obično javno poznat (otuda i njihova imena). U okviru šifrovanja, javni ključ može biti korišćen za šifrovanje poruke, dok se privatni ključ može koristiti za dešifrovanje.


Grana kriptografije koja se bavi šemama gde sve strane dele jedan ključ poznata je kao **simetrična kriptografija**. Jedan ključ u takvoj šemi obično se naziva **privatni ključ** (ili tajni ključ). Grana kriptografije koja se bavi šemama koje zahtevaju par privatnog i javnog ključa poznata je kao **asimetrična kriptografija**. Ove grane se ponekad nazivaju i **kriptografija privatnog ključa** i **kriptografija javnog ključa**, respektivno (iako to može izazvati zabunu, jer šeme javne kriptografije takođe imaju privatne ključeve).


Pojava asimetrične kriptografije krajem 1970-ih bila je jedan od najvažnijih događaja u istoriji kriptografije. Bez nje, većina naših modernih komunikacionih sistema, uključujući Bitcoin, ne bi bila moguća, ili bi barem bila veoma nepraktična.


Važno je napomenuti da moderna kriptografija nije isključivo proučavanje simetričnih i asimetričnih kriptografskih šema (iako to pokriva veći deo oblasti). Na primer, kriptografija se takođe bavi Hash funkcijama i generatorima pseudorandom brojeva, i možete izgraditi aplikacije na ovim primitivima koje nisu povezane sa simetričnom ili asimetričnom kriptografijom ključeva.


Treće, klasične šeme šifrovanja, poput onih korišćenih u Beale šiframa, bile su više umetnost nego nauka. Njihova percipirana sigurnost uglavnom se zasnivala na intuicijama u vezi sa njihovom složenošću. Obično bi bile zakrpljene kada bi se saznalo za novi napad na njih, ili bi bile potpuno odbačene ako je napad bio posebno ozbiljan. Međutim, moderna kriptografija je rigorozna nauka sa formalnim, matematičkim pristupom kako razvoju, tako i analizi kriptografskih šema. [5]


Specifično, moderna kriptografija se fokusira na formalne **dokaze sigurnosti**. Bilo koji dokaz sigurnosti za kriptografski sistem odvija se u tri koraka:


1.	Izjava o **kriptografskoj definiciji sigurnosti**, odnosno, skup sigurnosnih ciljeva i pretnja koju predstavlja napadač.

2.	Izjava o bilo kojim matematičkim pretpostavkama u vezi sa računarskom složenošću šeme. Na primer, kriptografska šema može sadržati generator pseudorandom brojeva. Iako ne možemo dokazati da oni postoje, možemo pretpostaviti da postoje.

3.	Izlaganje matematičkog **dokaza sigurnosti** šeme na osnovu formalnog pojma sigurnosti i bilo kojih matematičkih pretpostavki.


Četvrto, dok se istorijski kriptografija prvenstveno koristila u vojnim okruženjima, ona je prožela naše svakodnevne aktivnosti u digitalnom dobu. Bilo da obavljate bankarske poslove putem interneta, objavljujete na društvenim mrežama, kupujete proizvod na Amazonu sa svojom kreditnom karticom ili dajete napojnicu prijatelju Bitcoin, kriptografija je sine qua non našeg digitalnog doba.


S obzirom na ova četiri aspekta moderne kriptografije, mogli bismo okarakterisati modernu **kriptografiju** kao nauku koja se bavi formalnim razvojem i analizom kriptografskih šema za zaštitu digitalnih informacija od napada protivnika. [6] Bezbednost ovde treba široko shvatiti kao sprečavanje napada koji narušavaju tajnost, integritet, autentifikaciju i/ili neporecivost u komunikacijama.


Kriptografija se najbolje posmatra kao poddisciplina **kibernetičke sigurnosti**, koja se bavi sprečavanjem krađe, oštećenja i zloupotrebe računarskih sistema. Imajte na umu da mnogi problemi kibernetičke sigurnosti imaju malo ili samo delimičnu vezu sa kriptografijom.


Na primer, ako kompanija lokalno smešta skupe servere, možda će biti zabrinuta za obezbeđivanje ovog hardvera od krađe i oštećenja. Iako je ovo pitanje sajber bezbednosti, ima malo veze sa kriptografijom.


Za još jedan primer, **phishing napadi** su čest problem u našem modernom dobu. Ovi napadi pokušavaju da prevare ljude putem e-maila ili nekog drugog medija za poruke kako bi otkrili osetljive informacije kao što su lozinke ili brojevi kreditnih kartica. Iako kriptografija može pomoći Address phishing napadima do određenog stepena, sveobuhvatan pristup zahteva više od samog korišćenja neke kriptografije.



**Beleške:**


[3] Da budemo precizni, važne primene kriptografskih šema su bile povezane sa tajnošću. Deca, na primer, često koriste jednostavne kriptografske šeme za „zabavu“. Tajnost zapravo nije zabrinutost u tim slučajevima.


[4] Bruce Schneier, *Applied Cryptography*, 2nd edn, 2015 (Indianapolis, IN: John Wiley & Sons), str. 2.


[5] Videti Jonathan Katz i Yehuda Lindell, *Introduction to Modern Cryptography*, CRC Press (Boca Raton, FL: 2015), posebno str. 16–23, za dobar opis.


[6] Uporedi Katz i Lindell, ibid., str. 3. Mislim da njihova karakterizacija ima nekih problema, pa ovde predstavljam malo drugačiju verziju njihove izjave.



## Otvorene komunikacije

<chapterId>cb23d0a6-ba9a-5dc6-a55a-258405ae4117</chapterId>


Moderna kriptografija je dizajnirana da pruži sigurnosne garancije u **otvorenom komunikacionom** okruženju. Ako je naš komunikacioni kanal toliko dobro zaštićen da prisluškivači nemaju šanse da manipulišu ili čak samo posmatraju naše poruke, onda je kriptografija suvišna. Većina naših komunikacionih kanala, međutim, nije ovako dobro čuvana.


Kičma komunikacije u modernom svetu je ogromna mreža optičkih kablova. Obavljanje telefonskih poziva, gledanje televizije i pretraživanje interneta u modernom domaćinstvu uglavnom se oslanja na ovu mrežu optičkih kablova (mali procenat može se oslanjati isključivo na satelite). Istina je da možete imati različite podatkovne veze u svom domu, kao što su koaksijalni kabl, (asimetrična) digitalna pretplatnička linija i optički kabl. Ali, barem u razvijenom svetu, ovi različiti mediji za prenos podataka brzo se spajaju izvan vaše kuće na čvor u ogromnoj mreži optičkih kablova koja povezuje ceo svet. Izuzeci su neka udaljena područja razvijenog sveta, kao što su Sjedinjene Američke Države i Australija, gde podatkovni saobraćaj može i dalje prelaziti značajne udaljenosti preko tradicionalnih bakarnih telefonskih žica.


Bilo bi nemoguće sprečiti potencijalne napadače da fizički pristupe ovoj mreži kablova i njenoj pratećoj infrastrukturi. Zapravo, već znamo da većinu naših podataka presreću razne nacionalne obaveštajne agencije na ključnim tačkama preseka Interneta.[7] Ovo uključuje sve, od poruka na Facebook-u do adresa veb-sajtova koje posećujete.


Dok nadzor nad podacima u velikim razmerama zahteva moćnog protivnika, kao što je nacionalna obaveštajna agencija, napadači sa samo nekoliko resursa mogu lako pokušati da špijuniraju na lokalnijem nivou. Iako se to može desiti na nivou prisluškivanja žica, daleko je lakše jednostavno presresti bežične komunikacije.


Većina podataka u našim lokalnim mrežama—bilo kod kuće, u kancelariji ili u kafiću—sada putuje putem radio talasa do bežičnih pristupnih tačaka na sve-u-jednom ruterima, umesto kroz fizičke kablove. Tako napadaču treba malo resursa da presretne bilo koji vaš lokalni saobraćaj. Ovo je posebno zabrinjavajuće jer većina ljudi čini vrlo malo da zaštiti podatke koji putuju preko njihovih lokalnih mreža. Pored toga, potencijalni napadači mogu takođe ciljati naše mobilne širokopojasne veze, kao što su 3G, 4G i 5G. Sve ove bežične komunikacije su laka meta za napadače.


Stoga, ideja o čuvanju komunikacija u tajnosti zaštitom komunikacionog kanala je beznadežno iluzorna težnja za veći deo modernog sveta. Sve što znamo opravdava ozbiljnu paranoju: uvek treba pretpostaviti da neko prisluškuje. A kriptografija je glavni alat koji imamo za postizanje bilo kakve sigurnosti u ovom modernom okruženju.



**Beleške:**


[7] Videti, na primer, Olga Khazan, “The creepy, long-standing practice of undersea cable tapping”, *The Atlantic*, 16. jul 2013 (dostupno na [The Atlantic](https://www.theatlantic.com/international/archive/2013/07/the-creepy-long-standing-practice-of-undersea-cable-tapping/277855/)).



# Matematičke osnove kriptografije 1

<partId>1bf9f0aa-0f68-5493-83fb-2167238ff9de</partId>



## Nasumične promenljive

<chapterId>b623a7d0-3dff-5803-bd4e-8257ff73dd69</chapterId>


Kriptografija se oslanja na matematiku. I ako želite da izgradite više od površnog razumevanja kriptografije, morate biti komforni sa tom matematikom.


Ovo poglavlje uvodi većinu osnovne matematike s kojom ćete se susresti prilikom učenja kriptografije. Teme uključuju slučajne varijable, modulo operacije, XOR operacije i pseudonasumičnost. Trebalo bi da savladate materijal u ovim sekcijama za bilo kakvo nesuperficijalno razumevanje kriptografije.


Sledeći deo se bavi teorijom brojeva, što je mnogo izazovnije.


### Nasumične promenljive


Nasumična promenljiva se obično označava nenaglašenim, velikim slovom. Tako, na primer, možemo govoriti o nasumičnoj promenljivoj $X$, nasumičnoj promenljivoj $Y$, ili nasumičnoj promenljivoj $Z$. Ovo je notacija koju ću takođe koristiti od sada pa nadalje.


**Nasumična promenljiva** može imati dve ili više mogućih vrednosti, svaka sa određenom pozitivnom verovatnoćom. Moguće vrednosti su navedene u **skupu ishoda**.


Svaki put kada **uzorkujete** slučajnu varijablu, izvlačite određenu vrednost iz njenog skupa ishoda prema definisanim verovatnoćama.


Hajde da pređemo na jednostavan primer. Pretpostavimo promenljivu X koja je definisana na sledeći način:



- X ima skup ishoda $\{1,2\}$


$$
Pr[X = 1] = 0.5
$$


$$
Pr[X = 2] = 0.5
$$


Lako je videti da je $X$ slučajna varijabla. Prvo, postoje dve ili više mogućih vrednosti koje $X$ može da uzme, naime $1$ i $2$. Drugo, svaka moguća vrednost ima pozitivnu verovatnoću da se pojavi kada uzorkujete $X$, naime $0.5$.


Sve što je potrebno za slučajnu varijablu je skup ishoda sa dve ili više mogućnosti, gde svaka mogućnost ima pozitivnu verovatnoću da se dogodi prilikom uzorkovanja. U principu, dakle, slučajna varijabla može biti definisana apstraktno, bez ikakvog konteksta. U ovom slučaju, možete zamisliti „uzorkovanje“ kao izvođenje nekog prirodnog eksperimenta kako biste odredili vrednost slučajne varijable.


Promenljiva $X$ iznad je definisana apstraktno. Stoga, možete zamisliti uzorkovanje promenljive $X$ kao bacanje poštenog novčića i dodeljivanje “2” u slučaju glave i “1” u slučaju pisma. Za svaki uzorak $X$, ponovo bacate novčić.


Alternativno, možete zamisliti uzorkovanje $X$, kao bacanje poštene kocke i dodeljivanje “2” u slučaju da kocka pokaže $1$, $3$, ili $4$, i dodeljivanje “1” u slučaju da kocka pokaže $2$, $5$, ili $6$. Svaki put kada uzorkujete $X$, ponovo bacate kocku.


Zaista, bilo koji prirodni eksperiment koji bi vam omogućio da definišete verovatnoće mogućih vrednosti $X$ iznad može se zamisliti u vezi sa crtanjem.


Često, međutim, slučajne promenljive nisu samo apstraktno uvedene. Umesto toga, skup mogućih vrednosti ishoda ima eksplicitno značenje u stvarnom svetu (umesto samo kao brojevi). Pored toga, ove vrednosti ishoda mogu biti definisane u odnosu na neku specifičnu vrstu eksperimenta (umesto kao bilo koji prirodni eksperiment sa tim vrednostima).


Hajde sada da razmotrimo primer promenljive $X$ koja nije apstraktno definisana. X je definisana na sledeći način kako bi se odredilo koji od dva tima započinje fudbalsku utakmicu:



- $X$ ima skup ishoda {red kicks off,blue kicks off}
- Bacite određeni novčić $C$: pismo = „crveni počinje“; glava = „plavi počinje“


$$
Pr [X = \text{red kicks off}] = 0.5
$$


$$
Pr [X = \text{blue kicks off}] = 0.5
$$


U ovom slučaju, skup ishoda X je obezbeđen sa konkretnim značenjem, naime koji tim počinje u fudbalskoj utakmici. Pored toga, mogući ishodi i njihove pridružene verovatnoće su određeni konkretnim eksperimentom, naime bacanjem određenog novčića $C$.


U okviru diskusija o kriptografiji, slučajne promenljive se obično uvode u odnosu na skup ishoda sa značenjem u stvarnom svetu. To može biti skup svih poruka koje bi mogle biti šifrovane, poznat kao prostor poruka, ili skup svih ključeva koje strane koje koriste šifrovanje mogu izabrati, poznat kao prostor ključeva.


Nasumične promenljive u diskusijama o kriptografiji, međutim, obično nisu definisane u odnosu na neki specifičan prirodni eksperiment, već u odnosu na bilo koji eksperiment koji bi mogao dati odgovarajuće raspodele verovatnoće.


Nasumične promenljive mogu imati diskretne ili kontinuirane raspodele verovatnoće. Nasumične promenljive sa **diskretnom raspodelom verovatnoće**—odnosno, diskretne nasumične promenljive—imaju konačan broj mogućih ishoda. Nasumična promenljiva $X$ u oba do sada data primera bila je diskretna.


**Kontinuirane slučajne promenljive** mogu umesto toga uzimati vrednosti u jednom ili više intervala. Možete reći, na primer, da će slučajna promenljiva, prilikom uzorkovanja, uzeti bilo koju realnu vrednost između 0 i 1, i da je svaki realan broj u ovom intervalu podjednako verovatan. Unutar ovog intervala, postoji beskonačno mnogo mogućih vrednosti.


Za kriptografske diskusije, potrebno je razumeti samo diskretne slučajne promenljive. Svaka diskusija o slučajnim promenljivama od sada nadalje treba, dakle, da se razume kao da se odnosi na diskretne slučajne promenljive, osim ako nije izričito navedeno drugačije.



### Grafikovanje slučajnih varijabli


Moguće vrednosti i pridružene verovatnoće za slučajnu promenljivu mogu se lako vizualizovati putem grafa. Na primer, razmotrimo slučajnu promenljivu $X$ iz prethodnog odeljka sa skupom ishoda $\{1, 2\}$, i $Pr [X = 1] = 0.5$ i $Pr [X = 2] = 0.5$. Takvu slučajnu promenljivu bismo obično prikazali u obliku stubičastog grafa kao u *Figure 1*.


*Slika 1: Slučajna promenljiva X*


![Figure 1: Random variable X.](assets/Figure2-1.webp)


Široke trake u *Figure 1* očigledno ne znače da nasumična varijabla $X$ zapravo ima kontinuiranu distribuciju. Umesto toga, trake su napravljene širokim kako bi bile vizuelno privlačnije (samo linija koja ide pravo gore pruža manje intuitivnu vizualizaciju).



### Uniformne varijable


U izrazu „slučajna varijabla“, termin „slučajna“ samo znači „verovatnosna“. Drugim rečima, to samo znači da se dva ili više mogućih ishoda varijable javljaju sa određenim verovatnoćama. Ovi ishodi, međutim, *ne moraju nužno* biti podjednako verovatni (iako termin „slučajna“ zaista može imati to značenje u drugim kontekstima).


**Uniformna promenljiva** je poseban slučaj slučajne promenljive. Može poprimiti dve ili više vrednosti, sve sa jednakom verovatnoćom. Slučajna promenljiva $X$ prikazana na *Slici 1* je očigledno uniformna promenljiva, jer se oba moguća ishoda javljaju sa verovatnoćom $0.5$. Međutim, postoji mnogo slučajnih promenljivih koje nisu primeri uniformnih promenljivih.


Razmotrimo, na primer, slučajnu promenljivu $Y$. Ona ima skup ishoda {1, 2, 3, 8, 10} i sledeću raspodelu verovatnoće:


$$
\Pr[Y = 1] = 0.25
$$


$$
\Pr[Y = 2] = 0.35
$$


$$
\Pr[Y = 3] = 0.1
$$


$$
\Pr[Y = 8] = 0.25
$$


$$
\Pr[Y = 10] = 0.05
$$



Iako dve moguće ishoda zaista imaju jednaku verovatnoću da se dogode, naime $1$ i $8$, $Y$ takođe može poprimiti određene vrednosti sa različitim verovatnoćama od $0.25$ prilikom uzorkovanja. Dakle, iako je $Y$ zaista slučajna promenljiva, ona nije uniformna promenljiva.


Grafički prikaz $Y$ je dat na *Slici 2*.


*Slika 2: Slučajna promenljiva Y*


![Figure 2: Random variable Y.](assets/Figure2-2.webp "Figure 2: Random variable Y")


Za konačni primer, razmotrite slučajnu promenljivu Z. Ima skup ishoda {1,3,7,11,12} i sledeću raspodelu verovatnoće:


$$
\Pr[Z = 2] = 0.2
$$


$$
\Pr[Z = 3] = 0.2
$$


$$
\Pr[Z = 9] = 0.2
$$


$$
\Pr[Z = 11] = 0.2
$$


$$
\Pr[Z = 12] = 0.2
$$


Možete ga videti prikazanog na *Figure 3*. Nasumična promenljiva Z je, za razliku od Y, uniformna promenljiva, jer su sve verovatnoće za moguće vrednosti pri uzorkovanju jednake.



*Slika 3: Slučajna promenljiva Z*


![Figure 3: Random variable Z.](assets/Figure2-3.webp "Figure 3: Random variable Z")



### Uslovna verovatnoća


Pretpostavimo da Bob namerava da ravnomerno izabere dan iz poslednje kalendarske godine. Šta treba da zaključimo da je verovatnoća da izabrani dan bude u letu?


Sve dok mislimo da će Bobov proces zaista biti potpuno uniforman, trebali bismo zaključiti da postoji verovatnoća od 1/4 da Bob izabere dan u letu. Ovo je **bezuslovna verovatnoća** da nasumično izabrani dan bude u letu.


Pretpostavimo sada da Bob umesto da nasumično bira kalendarski dan, bira samo nasumično među onim danima kada je podnevna temperatura na Crystal Lake-u (New Jersey) bila 21 stepen Celzijusa ili viša. S obzirom na ove dodatne informacije, šta možemo zaključiti o verovatnoći da će Bob izabrati dan u letu?


Zaista bismo trebali izvući drugačiji zaključak nego ranije, čak i bez ikakvih dodatnih specifičnih informacija (npr., temperatura u podne svakog dana prošle kalendarske godine).


Znajući da je Crystal Lake u New Jerseyju, sigurno ne bismo očekivali da temperatura u podne bude 21 stepen Celzijusa ili viša zimi. Umesto toga, mnogo je verovatnije da je to topao dan u proleće ili jesen, ili dan negde u leto. Dakle, znajući da je temperatura u podne na Crystal Lakeu na odabrani dan bila 21 stepen Celzijusa ili viša, verovatnoća da je dan koji je Bob odabrao u leto postaje mnogo veća. Ovo je **uslovna verovatnoća** da je nasumično odabrani dan u leto, s obzirom na to da je temperatura u podne na Crystal Lakeu bila 21 stepen Celzijusa ili viša.


Za razliku od prethodnog primera, verovatnoće dva događaja takođe mogu biti potpuno nepovezane. U tom slučaju, kažemo da su **nezavisni**.


Pretpostavimo, na primer, da je određeni pošten novčić pao na glavu. S obzirom na ovu činjenicu, kolika je, onda, verovatnoća da će sutra padati kiša? Uslovna verovatnoća u ovom slučaju treba da bude ista kao i bezuslovna verovatnoća da će sutra padati kiša, jer bacanje novčića generalno nema uticaja na vreme.


Koristimo simbol "|" za pisanje izjava o uslovnoj verovatnoći. Na primer, verovatnoća događaja $A$ pod uslovom da se dogodio događaj $B$ može se napisati na sledeći način:


$$
Pr[A|B]
$$


Dakle, kada su dva događaja, $A$ i $B$, nezavisna, onda:


$$
Pr[A|B] = Pr[A] \text{ and } Pr[B|A] = Pr[B]
$$


Uslov za nezavisnost može se pojednostaviti na sledeći način:


$$
Pr[A, B] = Pr[A] \cdot Pr[B]
$$



Ključni rezultat u teoriji verovatnoće poznat je kao **Bayesova teorema**. Ona u suštini kaže da se $Pr[A|B]$ može prepisati na sledeći način:



$$
Pr[A|B] = \frac{Pr[B|A] \cdot Pr[A]}{Pr[B]}
$$



Umesto korišćenja uslovnih verovatnoća sa specifičnim događajima, možemo takođe posmatrati uslovne verovatnoće povezane sa dve ili više slučajnih promenljivih preko skupa mogućih događaja. Pretpostavimo dve slučajne promenljive, $X$ i $Y$. Možemo označiti bilo koju moguću vrednost za $X$ sa $x$, i bilo koju moguću vrednost za $Y$ sa $y$. Mogli bismo reći, onda, da su dve slučajne promenljive nezavisne ako važi sledeća izjava:


$$
Pr[X = x, Y = y] = Pr[X = x] \cdot Pr[Y = y]
$$


za sve $x$ i $y$.


Hajde da budemo malo eksplicitniji o tome šta ova izjava znači.


Pretpostavimo da su skupovi ishoda za $X$ i $Y$ definisani na sledeći način: **X** = $\{x_1, x_2, \ldots, x_i, \ldots, x_n\}$ i **Y** = $\{y_1, y_2, \ldots, y_i, \ldots, y_m\}$. (Uobičajeno je da se skupovi vrednosti označavaju podebljanim velikim slovima.)


Sada pretpostavimo da uzorkujete $Y$ i posmatrate $y_1$. Gornja izjava nam govori da je verovatnoća da sada dobijemo $x_1$ iz uzorkovanja $X$ potpuno ista kao da nikada nismo posmatrali $y_1$. Ovo važi za bilo koji $y_i$ koji bismo mogli izvući iz našeg početnog uzorkovanja $Y$. Na kraju, ovo važi ne samo za $x_1$. Za bilo koji $x_i$, verovatnoća pojavljivanja nije pod uticajem ishoda uzorkovanja $Y$. Sve ovo važi i za slučaj kada se prvo uzorkuje $X$.


Završimo našu diskusiju na nešto filozofskijoj tački. U bilo kojoj stvarnoj situaciji, verovatnoća nekog događaja se uvek procenjuje u odnosu na određeni skup informacija. Ne postoji „bezuslovna verovatnoća“ u bilo kom vrlo strogom smislu te reči.


Na primer, pretpostavimo da sam vas pitao za verovatnoću da će svinje leteti do 2030. godine. Iako vam ne dajem dodatne informacije, očigledno znate mnogo o svetu što može uticati na vašu procenu. Nikada niste videli svinje da lete. Znate da većina ljudi neće očekivati da lete. Znate da nisu baš građene za letenje. I tako dalje.


Dakle, kada govorimo o „bezuslovnoj verovatnoći“ nekog događaja u kontekstu stvarnog sveta, taj termin zaista može imati značenje samo ako ga shvatimo kao „verovatnoću bez ikakvih daljih eksplicitnih informacija“. Svako razumevanje „uslovne verovatnoće“ treba, dakle, uvek shvatiti u odnosu na neku specifičnu informaciju.


Mogao bih, na primer, da vas pitam kolika je verovatnoća da će svinje leteti do 2030. godine, nakon što vam dam dokaze da su neke koze na Novom Zelandu naučile da lete nakon nekoliko godina obuke. U tom slučaju, verovatno ćete prilagoditi svoju procenu verovatnoće da će svinje leteti do 2030. godine. Dakle, verovatnoća da će svinje leteti do 2030. godine je uslovljena ovim dokazima o kozama na Novom Zelandu.



## Operacija modulo

<chapterId>709b34e5-b155-53d2-abbd-97d67e56db00</chapterId>


### Modulo


Najosnovniji izraz sa **modulo operacijom** je sledećeg oblika: $x \mod y$.


Promenljiva $x$ se naziva deljenik, a promenljiva $y$ delilac. Da biste izvršili modulo operaciju sa pozitivnim deljenikom i pozitivnim deliocem, jednostavno odredite ostatak deljenja.


Na primer, razmotrimo izraz $25 \mod 4$. Broj 4 ide u broj 25 ukupno 6 puta. Ostatak te deljenja je 1. Dakle, $25 \mod 4$ je jednako 1. Na sličan način, možemo izračunati izraze ispod:



- $29 \mod 30 = 29$ (jer 30 ide u 29 ukupno 0 puta i ostatak je 29)
- $42 \mod 2 = 0$ (jer 2 ide u 42 ukupno 21 put i ostatak je 0)
- $12 \mod 5 = 2$ (jer 5 ide u 12 ukupno 2 puta i ostatak je 2)
- $20 \mod 8 = 4$ (jer 8 ide u 20 ukupno 2 puta i ostatak je 4)


Kada je deljenik ili delilac negativan, programski jezici mogu različito obrađivati modulo operacije.


Definitivno ćete naići na slučajeve sa negativnim deliocem u kriptografiji. U tim slučajevima, tipičan pristup je sledeći:



- Prvo odredite najbližu vrednost *manju ili jednaku* deliocu u koju delilac deli sa ostatkom nula. Nazovite tu vrednost $p$.
- Ako je dividenda $x$, onda je rezultat operacije modulo vrednost $x – p$.


Na primer, pretpostavimo da je dividenda $–20$ a delilac 3. Najbliža vrednost manja ili jednaka $–20$ u koju 3 deli ravnomerno je $–21$. Vrednost $x – p$ u ovom slučaju je $–20 – (–21)$. Ovo je jednako 1 i, prema tome, $–20 \mod 3$ je jednako 1. Na sličan način, možemo izračunati izraze ispod:



- $–8 \mod 5 = 2$
- $–19 \mod 16 = 13$
- $–14 \mod 6 = 4$


U vezi sa notacijom, obično ćete videti sledeće tipove izraza: $x = [y \mod z]$. Zbog zagrada, operacija modulo u ovom slučaju se primenjuje samo na desnu stranu izraza. Ako je $y$ jednako 25, a $z$ jednako 4, na primer, tada $x$ iznosi 1.


Without brackets, the modulo operation acts on *both sides* of an expression. Suppose, for instance, the following expression: $x = y \mod z$. If $y$ equals 25 and $z$ equals 4, then all we know is that $x \mod 4$ evaluates to 1. This is consistent with any value for $x$ from the set $\{\ldots,–7, –3, 1, 5, 9,\ldots\}$.


Grana matematike koja uključuje modulo operacije na brojevima i izrazima naziva se **modularna aritmetika**. Možete misliti na ovu granu kao na aritmetiku za slučajeve u kojima brojna linija nije beskonačno dugačka. Iako obično nailazimo na modulo operacije za (pozitivne) cele brojeve unutar kriptografije, možete takođe izvoditi modulo operacije koristeći bilo koje realne brojeve.


### Šifriranje pomakom


Operacija modulo se često sreće u kriptografiji. Da bismo ilustrovali, razmotrimo jednu od najpoznatijih istorijskih šema šifrovanja: šifru pomaka.


Hajde prvo da ga definišemo. Pretpostavimo rečnik *D* koji izjednačava sva slova engleske abecede, redom, sa skupom brojeva $\{0, 1, 2, \ldots, 25\}$. Pretpostavimo prostor poruka **M**. **Šifriranje pomakom** je, dakle, šema šifrovanja definisana na sledeći način:



- Izaberite ravnomerno ključ $k$ iz prostora ključeva **K**, gde je **K** = $\{0, 1, 2, \ldots, 25\}$ [1]
- Šifrujte poruku $m \in \mathbf{M}$, na sledeći način:
    - Razdvoj $m$ na njegova pojedinačna slova $m_0, m_1, \ldots, m_i, \ldots, m_l$
    - Pretvori svaki $m_i$ u broj prema *D*
    - Za svaki $m_i$, $c_i = [(m_i + k) \mod 26]$
    - Pretvori svaki $c_i$ u slovo prema *D*
    - Zatim kombinujte $c_0, c_1, \ldots, c_l$ da biste dobili šifrat $c$
- Dekriptuj šifrat $c$ na sledeći način:
    - Pretvori svaki $c_i$ u broj prema *D*
    - Za svaki $c_i$, $m_i = [(c_i – k) \mod 26]$
    - Pretvori svaki $m_i$ u slovo prema *D*
    - Zatim kombinujte $m_0, m_1, \ldots, m_l$ da biste dobili originalnu poruku $m$


Operator modulo u šifri pomaka osigurava da se slova rotiraju, tako da su sva šifrovana slova definisana. Da bismo ilustrovali, razmotrimo primenu šifre pomaka na reč „DOG“.


Pretpostavimo da ste ravnomerno odabrali ključ da ima vrednost 17. Slovo „O“ odgovara broju 15. Bez modulo operacije, zbir ovog broja iz otvorenog teksta sa ključem bi iznosio broj šifrovanog teksta 32. Međutim, taj broj šifrovanog teksta ne može biti pretvoren u slovo šifrovanog teksta, jer engleska abeceda ima samo 26 slova. Modulo operacija osigurava da broj šifrovanog teksta zapravo bude 6 (rezultat $32 \mod 26$), što odgovara slovu šifrovanog teksta „G“.


Celaokupna enkripcija reči „DOG“ sa ključnom vrednošću 17 je sledeća:



- Poruka = PAS = P,A,S = 3,15,6
- $c_0 = [(3 + 17) \mod 26] = [(20) \mod 26] = 20 = U$
- $c_1 = [(15 + 17) \mod 26] = [(32) \mod 26] = 6 = G$
- $c_2 = [(6 + 17) \mod 26] = [(23) \mod 26] = 23 = X$
- $c = UGX$


Svi mogu intuitivno razumeti kako šifriranje pomakom funkcioniše i verovatno ga sami koriste. Međutim, za unapređenje vašeg znanja o kriptografiji, važno je da počnete da se osećate prijatnije sa formalizacijom, jer će šeme postati mnogo teže. Zato su koraci za šifriranje pomakom formalizovani.



**Beleške:**


[1] Možemo tačno definisati ovu izjavu, koristeći terminologiju iz prethodnog odeljka. Neka uniformna promenljiva $K$ ima $K$ kao svoj skup mogućih ishoda. Dakle:


$$
Pr[K = 0] = \frac{1}{26}
$$


$$
Pr[K = 1] = \frac{1}{26}
$$


...i tako dalje. Uzorak uniformne promenljive $K$ jednom da bi se dobio određeni ključ.



## Operacija XOR

<chapterId>22f185cc-c516-5b33-950b-0908f2f881fe</chapterId>


Svi računarski podaci se obrađuju, skladište i šalju preko mreža na nivou bitova. Bilo koje šeme kriptografije koje se primenjuju na računarske podatke takođe funkcionišu na nivou bitova.


Na primer, pretpostavimo da ste otkucali e-mail u svojoj e-mail aplikaciji. Bilo koje šifrovanje koje primenite ne dešava se direktno na ASCII karakterima vašeg e-maila. Umesto toga, primenjuje se na bit-reprezentaciju slova i drugih simbola u vašem e-mailu.


Ključna matematička operacija koju treba razumeti za modernu kriptografiju, pored modulo operacije, jeste **XOR operacija**, ili operacija "isključivo ili". Ova operacija uzima kao ulaze dva bita i daje kao izlaz drugi bit. XOR operacija će jednostavno biti označena kao "XOR". Daje 0 ako su dva bita ista i 1 ako su dva bita različita. Možete videti četiri mogućnosti ispod. Simbol $\oplus$ predstavlja "XOR":



- $0 \oplus 0 = 0$
- $0 \oplus 1 = 1$
- $1 \oplus 0 = 1$
- $1 \oplus 1 = 0$


Na primer, pretpostavimo da imate poruku $m_1$ (01111001) i poruku $m_2$ (01011001). XOR operacija ovih dvaju poruka može se videti ispod.



- $m_1 \oplus m_2 = 01111001 \oplus 01011001 = 00100000$


Proces je jednostavan. Prvo izvršite XOR na krajnje levim bitovima $m_1$ i $m_2$. U ovom slučaju to je $0 \oplus 0 = 0$. Zatim izvršite XOR na drugom paru bitova s leva. U ovom slučaju to je $1 \oplus 1 = 0$. Nastavljate ovaj proces sve dok ne izvršite XOR operaciju na krajnje desnim bitovima.


Lako je videti da je XOR operacija komutativna, naime da $m_1 \oplus m_2 = m_2 \oplus m_1$. Pored toga, XOR operacija je takođe asocijativna. To jest, $(m_1 \oplus m_2) \oplus m_3 = m_1 \oplus (m_2 \oplus m_3)$.


XOR operacija na dva niza različitih dužina može imati različita tumačenja, u zavisnosti od konteksta. Ovdje se nećemo baviti XOR operacijama na nizovima različitih dužina.


XOR operacija je ekvivalentna posebnom slučaju izvođenja modulo operacije na sabiranju bitova kada je delilac 2. Ekvivalentnost možete videti u sledećim rezultatima:



- $(0 + 0) \mod 2 = 0 \oplus 0 = 0$
- $(1 + 0) \mod 2 = 1 \oplus 0 = 1$
- $(0 + 1) \mod 2 = 0 \oplus 1 = 1$
- $(1 + 1) \mod 2 = 1 \oplus 1 = 0$


## Pseudonasumičnost

<chapterId>20463fc5-3e92-581f-a1b7-3151279bd95e</chapterId>


U našoj diskusiji o slučajnim i uniformnim varijablama, napravili smo specifičnu razliku između "slučajnih" i "uniformnih". Ta razlika se obično održava u praksi kada se opisuju slučajne varijable. Međutim, u našem trenutnom kontekstu, ova razlika treba biti zanemarena i "slučajno" i "uniformno" se koriste kao sinonimi. Objasniću zašto na kraju odeljka.


Da bismo počeli, možemo nazvati binarni niz dužine $n$ **slučajnim** (ili **uniformnim**), ako je rezultat uzorkovanja uniformne varijable $S$ koja daje svakom binarnom nizu te dužine $n$ jednaku verovatnoću izbora.


Pretpostavimo, na primer, skup svih binarnih nizova dužine 8: $\{0000\ 0000, 0000\ 0001, \ldots, 1111\ 1111\}$. (Tipično je pisati 8-bitni niz u dva kvarteta, od kojih se svaki naziva **nibble**.) Nazovimo ovaj skup nizova **$S_8$**.


Prema definiciji iznad, možemo, dakle, nazvati određeni binarni niz dužine 8 nasumičnim (ili uniformnim), ako je rezultat uzorkovanja uniformne varijable $S$ koja daje svakom nizu u **$S_8$** jednaku verovatnoću izbora. S obzirom da skup **$S_8$** uključuje $2^8$ Elements, verovatnoća izbora pri uzorkovanju bi morala biti $1/2^8$ za svaki niz u skupu.


Ključni aspekt nasumičnosti binarnog niza je da je definisan u odnosu na proces kojim je izabran. Oblik bilo kog određenog binarnog niza sam po sebi, dakle, ne otkriva ništa o njegovoj nasumičnosti u izboru.


Na primer, mnogi ljudi intuitivno imaju ideju da niz kao što je $1111\ 1111$ nije mogao biti izabran nasumično. Ali ovo je očigledno netačno.


Definišući uniformnu varijablu $S$ preko svih binarnih nizova dužine 8, verovatnoća odabira $1111\ 1111$ iz skupa **$S_8$** je ista kao i za niz kao što je $0111\ 0100$. Dakle, ne možete ništa reći o nasumičnosti niza, samo analizirajući sam niz.


Takođe možemo govoriti o nasumičnim nizovima bez specifičnog misljenja na binarne nizove. Na primer, možemo govoriti o nasumičnom heksadecimalnom nizu $AF\ 02\ 82$. U ovom slučaju, niz bi bio nasumično izabran iz skupa svih heksadecimalnih nizova dužine 6. Ovo je ekvivalentno nasumičnom izboru binarnog niza dužine 24, jer svaka heksadecimalna cifra predstavlja 4 bita.


Tipično, izraz „nasumičan niz“, bez kvalifikacije, odnosi se na niz nasumično odabran iz skupa svih nizova iste dužine. Ovako sam ga opisao gore. Niz dužine $n$ može, naravno, biti nasumično odabran i iz drugog skupa. Na primer, iz skupa koji čini samo podskup svih nizova dužine $n$, ili možda iz skupa koji uključuje nizove različitih dužina. U tim slučajevima, međutim, ne bismo ga nazvali „nasumičnim nizom“, već „nizom koji je nasumično odabran iz nekog skupa **S**“.


Ključni koncept u kriptografiji je pseudonasumičnost. **Pseudonasumični niz** dužine $n$ izgleda *kao da* je rezultat uzorkovanja uniformne varijable $S$ koja svakom nizu u **$S_n$** daje jednaku verovatnoću izbora. Međutim, niz je zapravo rezultat uzorkovanja uniformne varijable $S'$ koja samo definiše raspodelu verovatnoće—ne nužno onu sa jednakim verovatnoćama za sve moguće ishode—na podskupu **$S_n$**. Ključna tačka ovde je da niko ne može zaista razlikovati uzorke iz $S$ i $S'$, čak i ako ih uzmete mnogo.


Pretpostavimo, na primer, slučajnu promenljivu $S$. Njeno skup ishoda je **$S_{256}$**, to je skup svih binarnih nizova dužine 256. Ovaj skup ima $2^{256}$ Elements. Svaki element ima jednaku verovatnoću izbora, $1/2^{256}$, prilikom uzorkovanja.


Pored toga, pretpostavimo nasumičnu promenljivu $S'$. Njeno skup ishoda uključuje samo $2^{128}$ binarnih nizova dužine 256. Ona ima neku verovatnosnu distribuciju nad tim nizovima, ali ta distribucija nije nužno uniformna.


Pretpostavimo da sam sada uzeo 1000-e uzoraka iz $S$ i 1000-e uzoraka iz $S'$ i dao ti dva skupa ishoda. Kažem ti koji skup ishoda je povezan sa kojom slučajnom promenljivom. Zatim, uzimam uzorak iz jedne od dve slučajne promenljive. Ali ovaj put ti ne kažem iz koje slučajne promenljive uzimam uzorak. Ako je $S'$ pseudonasumičan, ideja je da je tvoja verovatnoća da tačno pogodiš iz koje slučajne promenljive sam uzeo uzorak praktično ne bolja od $1/2$.


Tipično, pseudonasumičan niz dužine $n$ se proizvodi nasumičnim odabirom niza veličine $n – x$, gde je $x$ pozitivan ceo broj, i korišćenjem tog niza kao ulaza za ekspanzivni algoritam. Ovaj nasumičan niz veličine $n – x$ je poznat kao **seed**.


Pseudorandom nizovi su ključni koncept za praktičnu primenu kriptografije. Razmotrite, na primer, strim šifre. Kod strim šifre, nasumično odabrani ključ se ubacuje u ekspanzivni algoritam kako bi se proizveo mnogo veći pseudorandom niz. Ovaj pseudorandom niz se zatim kombinuje sa otvorenim tekstom putem XOR operacije kako bi se proizveo šifrovani tekst.


Ako ne bismo mogli da proizvedemo ovu vrstu pseudonasumičnog niza za tok šifru, onda bismo trebali ključ koji je dug koliko i poruka za njenu sigurnost. Ovo nije baš praktična opcija u većini slučajeva.


Pojam pseudonasumičnosti o kojem se raspravlja u ovom odeljku može se formalnije definisati. Takođe se proširuje na druge kontekste. Ali ne moramo ulaziti u tu raspravu ovde. Sve što zaista treba intuitivno da razumete za veći deo kriptografije je razlika između nasumičnog i pseudonasumičnog niza. [2]


Razlog za ukidanje razlike između "nasumičan" i "uniforman" u našoj diskusiji sada bi takođe trebalo da bude jasan. U praksi, svi koriste termin pseudonasumičan da označe niz koji izgleda **kao da** je rezultat uzorkovanja uniformne promenljive $S$. Strogo govoreći, takav niz bismo trebali nazvati "pseudo-uniforman," usvajajući naš raniji jezik. Pošto je termin "pseudo-uniforman" i nezgrapan i niko ga ne koristi, nećemo ga uvoditi ovde radi jasnoće. Umesto toga, jednostavno ćemo izostaviti razliku između "nasumičan" i "uniforman" u trenutnom kontekstu.



**Beleške**


[2] Ako ste zainteresovani za formalniji prikaz ovih tema, možete konsultovati Katz i Lindellovu *Introduction to Modern Cryptography*, posebno poglavlje 3.



# Matematičke Osnove Kriptografije 2

<partId>d7245cc9-bb6d-5403-b3d5-9c703d9a2f81</partId>



## Šta je teorija brojeva?

<chapterId>c0051c34-fd5d-539c-93e2-5c6dfd4c3355</chapterId>


Ovo poglavlje pokriva napredniju temu o matematičkim osnovama kriptografije: teoriju brojeva. Iako je teorija brojeva važna za simetričnu kriptografiju (kao što je u Rijndael šifri), posebno je važna u kontekstu kriptografije sa javnim ključem.


Ako vam se detalji teorije brojeva čine zamornim, preporučio bih da prvi put pročitate na višem nivou. Uvek se možete vratiti na to kasnije.


___


Možete okarakterisati **teoriju brojeva** kao proučavanje svojstava celih brojeva i matematičkih funkcija koje rade sa celim brojevima.


Razmotrimo, na primer, da su bilo koja dva broja $a$ i $N$ **koprimi** (ili **relativno prosti**) ako je njihov najveći zajednički delilac jednak 1. Pretpostavimo sada određeni ceo broj $N$. Koliko je celih brojeva manjih od $N$ koji su koprimi sa $N$? Možemo li dati opšte izjave o odgovorima na ovo pitanje? Ovo su tipične vrste pitanja na koja teorija brojeva nastoji da odgovori.


Moderna teorija brojeva oslanja se na alate apstraktne algebre. Oblast **apstraktne algebre** je poddisciplina matematike gde su glavni objekti analize apstraktni objekti poznati kao algebarske strukture. **Algebarska struktura** je skup Elements povezan sa jednom ili više operacija, koji ispunjava određene aksiome. Kroz algebarske strukture, matematičari mogu steći uvid u specifične matematičke probleme, apstrahujući se od njihovih detalja.


Polje apstraktne algebre se ponekad naziva i modernom algebrom. Možete naići i na pojam **apstraktne matematike** (ili **čiste matematike**). Ovaj poslednji termin nije referenca na apstraktnu algebru, već označava proučavanje matematike radi nje same, a ne samo sa ciljem potencijalnih primena.


Skupovi iz apstraktne algebre mogu se baviti mnogim tipovima objekata, od transformacija koje čuvaju oblik na jednakostraničnom trouglu do šara na tapetama. Za teoriju brojeva, razmatramo samo skupove Elements koji sadrže cele brojeve ili funkcije koje rade sa celim brojevima.



## Grupe

<chapterId>3209b270-f9cd-5224-803e-0ed19fbf7826</chapterId>


Osnovni koncept u matematici je koncept skupa Elements. Skup se obično označava znakovima vitičastih zagrada sa Elements odvojenim zarezima.


Na primer, skup svih celih brojeva je $\{…, -2, -1, 0, 1, 2, …\}$. Tri tačke ovde znače da se određeni obrazac nastavlja u određenom pravcu. Dakle, skup svih celih brojeva takođe uključuje $3, 4, 5, 6$ i tako dalje, kao i $-3, -4, -5, -6$ i tako dalje. Ovaj skup svih celih brojeva se obično označava sa $\mathbb{Z}$.


Još jedan primer skupa je $\mathbb{Z} \mod 11$, ili skup svih celih brojeva modulo 11. Za razliku od celog skupa $\mathbb{Z}$, ovaj skup sadrži samo konačan broj Elements, naime $\{0, 1, \ldots, 9, 10\}$.


Uobičajena greška je misliti da skup $\mathbb{Z} \mod 11$ zapravo jeste $\{-10, -9, \ldots, 0, \ldots, 9, 10\}$. Ali to nije slučaj, s obzirom na način na koji smo ranije definisali operaciju modula. Bilo koji negativni celi brojevi smanjeni modulom 11 prelaze u skup $\{0, 1, \ldots, 9, 10\}$. Na primer, izraz $-2 \mod 11$ prelazi u $9$, dok izraz $-27 \mod 11$ prelazi u $5$.


Još jedan osnovni koncept u matematici je koncept binarne operacije. Ovo je bilo koja operacija koja uzima dva Elements da bi proizvela treći. Na primer, iz osnovne aritmetike i algebre, bili biste upoznati sa četiri osnovne binarne operacije: sabiranje, oduzimanje, množenje i deljenje.


Ova dva osnovna matematička koncepta, skupovi i binarne operacije, koriste se za definisanje pojma grupe, najosnovnije strukture u apstraktnoj algebri.


Specifično, pretpostavimo neku binarnu operaciju $\circ$. Pored toga, pretpostavimo neki skup Elements **S** opremljen tom operacijom. Sve što "opremljen" ovde znači je da se operacija $\circ$ može izvršiti između bilo koja dva Elements u skupu **S**.


Kombinacija $\langle \mathbf{S}, \circ \rangle$ je, dakle, **grupa** ako ispunjava četiri specifična uslova, poznata kao aksiomi grupe.


1. Za bilo koje $a$ i $b$ koji su Elements od $\mathbf{S}$, $a \circ b$ je takođe element od $\mathbf{S}$. Ovo je poznato kao **uslov zatvorenosti**.

2. Za bilo koje $a$, $b$ i $c$ koji su Elements od $\mathbf{S}$, važi da je $(a \circ b) \circ c = a \circ (b \circ c)$. Ovo je poznato kao **uslov asocijativnosti**.

3. Postoji jedinstveni element $e$ u $\mathbf{S}$, takav da za svaki element $a$ u $\mathbf{S}$, sledeća jednačina važi: $e \circ a = a \circ e = a$. Kako postoji samo jedan takav element $e$, on se naziva **neutralni element**. Ovaj uslov je poznat kao **uslov neutralnosti**.

4. Za svaki element $a$ u $\mathbf{S}$, postoji element $b$ u $\mathbf{S}$, takav da važi sledeća jednačina: $a \circ b = b \circ a = e$, gde je $e$ identitetni element. Element $b$ ovde je poznat kao **inverzni element**, i obično se označava kao $a^{-1}$. Ovaj uslov je poznat kao **uslov inverznosti** ili **uslov invertibilnosti**.


Hajde da dalje istražimo grupe. Označimo skup svih celih brojeva sa $\mathbb{Z}$. Ovaj skup u kombinaciji sa standardnim sabiranjem, ili $\langle \mathbb{Z}, + \rangle$, očigledno odgovara definiciji grupe, jer ispunjava četiri gore navedene aksiome.


1. Za bilo koje $x$ i $y$ koji su Elements od $\mathbb{Z}$, $x + y$ je takođe element od $\mathbb{Z}$. Dakle, $\langle \mathbb{Z}, + \rangle$ ispunjava uslov zatvorenosti.

2. Za bilo koje $x$, $y$ i $z$ koji su Elements od $\mathbb{Z}$, $(x + y) + z = x + (y + z)$. Tako $\langle \mathbb{Z}, + \rangle$ ispunjava uslov asocijativnosti.

3. Postoji neutralni element u $\langle \mathbb{Z}, + \rangle$, naime 0. Za bilo koje $x$ u $\mathbb{Z}$, važi: $0 + x = x + 0 = x$. Dakle, $\langle \mathbb{Z}, + \rangle$ ispunjava uslov neutralnog elementa.

4. Konačno, za svaki element $x$ u $\mathbb{Z}$, postoji $y$ tako da je $x + y = y + x = 0$. Ako je $x$ na primer 10, $y$ bi bio $-10$ (u slučaju da je $x$ 0, $y$ je takođe 0). Dakle, $\langle \mathbb{Z}, + \rangle$ ispunjava uslov inverza.


Važno je napomenuti da činjenica da skup celih brojeva sa operacijom sabiranja čini grupu ne znači da on čini grupu sa operacijom množenja. Ovo možete proveriti testiranjem $\langle \mathbb{Z}, \cdot \rangle$ u odnosu na četiri aksioma grupe (gde $\cdot$ označava standardno množenje).


Prva dva aksioma očigledno važe. Pored toga, pod množenjem element 1 može služiti kao identitetni element. Bilo koji ceo broj $x$ pomnožen sa 1, naime daje $x$. Međutim, $\langle \mathbb{Z}, \cdot \rangle$ ne ispunjava uslov inverza. To jest, ne postoji jedinstveni element $y$ u $\mathbb{Z}$ za svaki $x$ u $\mathbb{Z}$, tako da je $x \cdot y = 1$.


Na primer, pretpostavimo da je $x = 22$. Koja vrednost $y$ iz skupa $\mathbb{Z}$ pomnožena sa $x$ bi dala neutralni element 1? Vrednost $1/22$ bi odgovarala, ali to nije u skupu $\mathbb{Z}$. Zapravo, nailazite na ovaj problem za bilo koji ceo broj $x$, osim za vrednosti 1 i -1 (gde bi $y$ morao biti 1 i -1 respektivno).


Ako bismo dozvolili realne brojeve za naš skup, tada bi naši problemi uglavnom nestali. Za bilo koji element $x$ u skupu, množenje sa $1/x$ daje 1. Pošto su razlomci uključeni u skup realnih brojeva, inverz se može naći za svaki realni broj. Izuzetak je nula, jer bilo koje množenje sa nulom nikada neće dati identitetni element 1. Dakle, skup realnih brojeva različitih od nule opremljen množenjem zaista je grupa.


Neke grupe ispunjavaju peti opšti uslov, poznat kao **uslov komutativnosti**. Ovaj uslov je sledeći:



- Pretpostavimo da grupa $G$ sa skupom **S** i binarnim operatorom $\circ$. Pretpostavimo da su $a$ i $b$ Elements od **S**. Ako važi da je $a \circ b = b \circ a$ za bilo koja dva Elements $a$ i $b$ u **S**, onda $G$ ispunjava uslov komutativnosti.


Bilo koja grupa koja ispunjava uslov komutativnosti poznata je kao **komutativna grupa**, ili **Abelova grupa** (po Nilsu Henriku Abelu). Lako je proveriti da su i skup realnih brojeva nad sabiranjem i skup celih brojeva nad sabiranjem Abelove grupe. Skup celih brojeva nad množenjem uopšte nije grupa, pa samim tim ne može biti Abelova grupa. Skup nenultih realnih brojeva nad množenjem, nasuprot tome, takođe je Abelova grupa.


Trebalo bi da obratite pažnju na dve važne konvencije u vezi sa notacijom. Prvo, znakovi „+“ ili „×“ će često biti korišćeni da simbolizuju grupne operacije, čak i kada Elements nisu, zapravo, brojevi. U tim slučajevima, ne bi trebalo da tumačite ove znakove kao standardno aritmetičko sabiranje ili množenje. Umesto toga, to su operacije sa samo apstraktnom sličnošću sa ovim aritmetičkim operacijama.


Osim ako se konkretno ne odnosiš na aritmetičko sabiranje ili množenje, lakše je koristiti simbole kao što su $\circ$ i $\diamond$ za grupne operacije, jer oni nemaju veoma ukorenjene kulturne konotacije.


Drugo, iz istog razloga zbog kojeg se “+” i “×” često koriste za označavanje ne-aritmetičkih operacija, identitet Elements grupa se često simbolizuje sa “0” i “1”, čak i kada Elements u tim grupama nisu brojevi. Osim ako se ne referišete na identitet elementa grupe sa brojevima, lakše je koristiti neutralniji simbol kao što je “$e$” za označavanje identitet elementa.


Mnoge različite i veoma važne skupove vrednosti u matematici, opremljene određenim binarnim operacijama, čine grupe. Kriptografske aplikacije, međutim, rade samo sa skupovima celih brojeva ili barem Elements koji su opisani celim brojevima, to jest, unutar domena teorije brojeva. Stoga se skupovi sa realnim brojevima osim celih brojeva ne koriste u kriptografskim aplikacijama.


Hajde da završimo pružanjem primera Elements koji može biti „opisan celim brojevima“, iako oni nisu celi brojevi. Dobar primer su tačke eliptičkih krivih. Iako bilo koja tačka na eliptičkoj krivoj očigledno nije ceo broj, takva tačka je zaista opisana sa dva cela broja.


Eliptičke krive su, na primer, ključne za Bitcoin. Bilo koji standardni Bitcoin privatni i javni par ključeva se bira iz skupa tačaka koje su definisane sledećom eliptičkom krivom:


$$
x^3 + 7 = y^2 \mod 2^{256} – 2^{32} – 29 – 28 – 27 – 26 - 24 - 1
$$


(najveći prost broj manji od $2^{256}$). $x$-koordinata je privatni ključ, a $y$-koordinata je vaš javni ključ.


Transakcije u Bitcoin obično uključuju zaključavanje izlaza na jedan ili više javnih ključeva na neki način. Vrednost iz ovih transakcija može se, zatim, otključati pravljenjem digitalnih potpisa sa odgovarajućim privatnim ključevima.




## Ciklične grupe

<chapterId>bfa5c714-7952-5fef-88b1-ca5b07edd886</chapterId>


Glavna razlika koju možemo povući je između **konačne** i **beskonačne grupe**. Prva ima konačan broj Elements, dok druga ima beskonačan broj Elements. Broj Elements u bilo kojoj konačnoj grupi poznat je kao **red grupe**. Sva praktična kriptografija koja uključuje upotrebu grupa oslanja se na konačne (brojčano-teorijske) grupe.


U okviru kriptografije sa javnim ključem, određena klasa konačnih Abelovih grupa poznata kao ciklične grupe je posebno važna. Da bismo razumeli ciklične grupe, prvo moramo razumeti koncept potenciranja elemenata grupe.


Pretpostavimo da je $G$ grupa sa grupnom operacijom $\circ$, i da je $a$ element grupe $G$. Izraz $a^n$ treba, dakle, interpretirati kao element $a$ kombinovan sam sa sobom ukupno $n – 1$ puta. Na primer, $a^2$ znači $a \circ a$, $a^3$ znači $a \circ a \circ a$, i tako dalje. (Napomena: potenciranje ovde nije nužno potenciranje u standardnom aritmetičkom smislu.)


Okrenimo se primeru. Pretpostavimo da je $G = \langle \mathbb{Z} \mod 7, + \rangle$, i da naša vrednost za $a$ iznosi 4. U ovom slučaju, $a^2 = [4 + 4 \mod 7] = [8 \mod 7] = 1 \mod 7$. Alternativno, $a^4$ bi predstavljao $[4 + 4 + 4 + 4 \mod 7] = [16 \mod 7] = 2 \mod 7$.


Neke abelove grupe imaju jedan ili više Elements, koji mogu proizvesti sve druge grupe Elements kroz kontinuirano potenciranje. Ovi Elements se nazivaju **generatori** ili **primitivni Elements**.


Jedna važna klasa takvih grupa je $\langle \mathbb{Z}^* \mod N, \cdot \rangle$, gde je $N$ prost broj. Oznaka $\mathbb{Z}^*$ ovde znači da grupa sadrži sve nenulte, pozitivne cele brojeve manje od $N$. Takva grupa, dakle, uvek ima $N – 1$ Elements.


Razmotrimo, na primer, $G = \langle \mathbb{Z}^* \mod 11, \cdot \rangle$. Ova grupa ima sledeći Elements: $\{1, 2, 3, 4, 5, 6, 7, 8, 9, 10\}$. Red ove grupe je 10 (što je zaista jednako $11 – 1$).


Hajde da istražimo potenciranje elementa 2 iz ove grupe. Izračunavanja do $2^{12}$ su prikazana ispod. Imajte na umu da se na levoj strani jednačine eksponent odnosi na potenciranje grupnog elementa. U našem konkretnom primeru, ovo zaista uključuje aritmetičko potenciranje na desnoj strani jednačine (ali je moglo uključivati, na primer, sabiranje). Da bih pojasnio, napisao sam ponovljenu operaciju, umesto eksponentnog oblika na desnoj strani.



- $2^1 = 2 \mod 11$
- $2^2 = 2 \cdot 2 \mod 11 = 4 \mod 11$
- $2^3 = 2 \cdot 2 \cdot 2 \mod 11 = 8 \mod 11$
- $2^4 = 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 16 \mod 11 = 5 \mod 11$
- $2^5 = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 32 \mod 11 = 10 \mod 11$
- $2^6 = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 64 \mod 11 = 9 \mod 11$
- $2^7 = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 128 \mod 11 = 7 \mod 11$
- $2^8 = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 256 \mod 11 = 3 \mod 11$
- $2^9 = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 512 \mod 11 = 6 \mod 11$
- $2^{10} = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 1024 \mod 11 = 1 \mod 11$
- $2^{11} = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 2048 \mod 11 = 2 \mod 11$
- $2^{12} = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 4096 \mod 11 = 4 \mod 11$


Ako pažljivo pogledaš, možeš videti da izvođenje eksponenciranja na elementu 2 prolazi kroz sve Elements od $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$ u sledećem redosledu: 2, 4, 8, 5, 10, 9, 7, 3, 6, 1. Nakon $2^{10}$, nastavak eksponenciranja elementa 2 ponovo prolazi kroz sve Elements i to u istom redosledu. Dakle, element 2 je generator u $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$.


Iako $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$ ima više generatora, nisu svi Elements ove grupe generatori. Razmotrimo, na primer, element 3. Prolazeći kroz prvih 10 eksponencijacija, bez prikazivanja zamornih proračuna, dobijamo sledeće rezultate:



- $3^1 = 3 \mod 11$
- $3^2 = 9 \mod 11$
- $3^3 = 5 \mod 11$
- $3^4 = 4 \mod 11$
- \(3^5 = 1 \mod 11\)
- $3^6 = 3 \mod 11$
- $3^7 = 9 \mod 11$
- $3^8 = 5 \mod 11$
- $3^9 = 4 \mod 11$
- $3^{10} = 1 \mod 11$


Umesto da prolazi kroz sve vrednosti u $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$, eksponenciranje elementa 3 vodi samo do podskupa tih vrednosti: 3, 9, 5, 4 i 1. Nakon petog eksponenciranja, ove vrednosti počinju da se ponavljaju.


Sada možemo definisati **cikličnu grupu** kao bilo koju grupu sa barem jednim generatorom. To jest, postoji barem jedan element grupe iz kojeg možete proizvesti sve druge elemente grupe Elements kroz eksponenciranje.


Možda ste primetili u našem gornjem primeru da su i $2^{10}$ i $3^{10}$ jednaki $1 \mod 11$. U stvari, iako nećemo izvoditi proračune, potenciranje sa 10 bilo kog elementa u grupi $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$ će dati $1 \mod 11$. Zašto je to slučaj?


Ovo je važno pitanje, ali zahteva malo truda da se odgovori.


Da počnemo, pretpostavimo dva pozitivna cela broja $a$ i $N$. Važna teorema u teoriji brojeva kaže da $a$ ima multiplikativni inverz modulo $N$ (to jest, ceo broj $b$ tako da $a \cdot b = 1 \mod N$) ako i samo ako je najveći zajednički delilac između $a$ i $N$ jednak 1. To jest, ako su $a$ i $N$ međusobno prosti.


Dakle, za bilo koju grupu celih brojeva opremljenu množenjem po modulu $N$, samo manji brojevi koji su međusobno prosti sa $N$ su uključeni u skup. Ovaj skup možemo označiti sa $\mathbb{Z}^c \mod N$.


Na primer, pretpostavimo da je $N$ 10. Samo su celi brojevi 1, 3, 7 i 9 međusobno prosti sa 10. Tako skup $\mathbb{Z}^c \mod 10$ uključuje samo $\{1, 3, 7, 9\}$. Ne možete kreirati grupu sa celobrojnom multiplikacijom modulo 10 koristeći bilo koje druge cele brojeve između 1 i 10. Za ovu specifičnu grupu, inverzi su parovi 1 i 9, i 3 i 7.


U slučaju kada je $N$ sam po sebi prost, svi celi brojevi od 1 do $N – 1$ su uzajamno prosti sa $N$. Takva grupa, dakle, ima red $N – 1$. Koristeći našu raniju notaciju, $\mathbb{Z}^c \mod N$ je jednako $\mathbb{Z}^* \mod N$ kada je $N$ prost. Grupa koju smo odabrali za naš raniji primer, $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$, je poseban primer ove klase grupa.


Zatim, funkcija $\phi(N)$ izračunava broj međusobno prostih brojeva do broja $N$, i poznata je kao **Eulerova Phi funkcija**. [1] Prema **Eulerovoj teoremi**, kada su dva cela broja $a$ i $N$ međusobno prosta, važi sledeće:



- $a^{\phi(N)} \mod N = 1 \mod N$


Ovo ima važnu implikaciju za klasu grupa $\langle \mathbb{Z}^* \mod N, \cdot \rangle$ gde je $N$ prost broj. Za ove grupe, eksponenciranje elemenata grupe predstavlja aritmetičko eksponenciranje. To jest, $a^{\phi(N)} \mod N$ predstavlja aritmetičku operaciju $a^{\phi(N)} \mod N$. Kako je bilo koji element $a$ u ovim multiplikativnim grupama relativno prost sa $N$, to znači da je $a^{\phi(N)} \mod N = a^{N – 1} \mod N = 1 \mod N$.


Eulerova teorema je zaista važan rezultat. Za početak, ona implicira da svi Elements u $\langle \mathbb{Z}^* \mod N, \cdot \rangle$ mogu ciklusirati samo kroz broj vrednosti eksponenciranjem koji deli $N – 1$. U slučaju $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$, to znači da svaki element može ciklusirati samo kroz 2, 5, ili 10 Elements. Grupne vrednosti kroz koje bilo koji element ciklusira prilikom eksponenciranja poznate su kao **red elementa**. Element sa redom ekvivalentnim redu grupe je generator.


Štaviše, Eulerova teorema implicira da uvek možemo znati rezultat $a^{N – 1} \mod N$ za bilo koju grupu $\langle \mathbb{Z}^* \mod N, \cdot \rangle$ gde je $N$ prost. Ovo važi bez obzira na to koliko složene stvarne kalkulacije mogu biti.


Na primer, pretpostavimo da je naša grupa $\mathbb{Z}^* \mod 160,481,182$ (gde je 160,481,182 zaista prost broj). Znamo da svi brojevi od 1 do 160,481,181 moraju biti Elements ove grupe, i da je $\phi(n) = 160,481,181$. Iako ne možemo napraviti sve korake u proračunima, znamo da izrazi kao što su $514^{160,481,181}$, $2,005^{160,481,181}$ i $256,212^{160,481,181}$ moraju svi evaluirati na $1 \mod 160,481,182$.


**Beleške:**


[1] Funkcija radi na sledeći način. Bilo koji ceo broj $N$ može se rastaviti na proizvod prostih brojeva. Pretpostavimo da je određeni $N$ rastavljen na sledeći način: $p_1^{e1} \cdot p_2^{e2} \cdot \ldots \cdot p_m^{em}$ gde su svi $p$ prosti brojevi i svi $e$ celi brojevi veći ili jednaki 1. Tada:


$$
\phi(N) = \sum_{i=1}^m \left[p_i^{e_i} - p_i^{e_i - 1}\right]
$$


Formula Eulero-ve Phi funkcije za prostu faktorizaciju $N$.



## Polja

<chapterId>fad52d86-3a22-5c9f-979e-3bec9eaa008e</chapterId>


Grupa je osnovna algebarska struktura u apstraktnoj algebri, ali postoji mnogo više. Jedina druga algebarska struktura sa kojom treba da budete upoznati je struktura **polja**, posebno **konačnog polja**. Ova vrsta algebarske strukture se često koristi u kriptografiji, kao što je u Advanced Encryption Standard. Potonji je glavni simetrični šifarski sistem sa kojim ćete se susresti u praksi.


Polje je izvedeno iz pojma grupe. Konkretno, **polje** je skup Elements **S** opremljen sa dva binarna operatora $\circ$ i $\diamond$, koji ispunjava sledeće uslove:


1. Skup **S** opremljen sa $\circ$ je Abelova grupa.

2. Skup **S** opremljen sa $\diamond$ je Abelova grupa za „nenula“ Elements.

3. Skup **S** opremljen sa dva operatora ispunjava ono što je poznato kao distributivni uslov: Pretpostavimo da su $a$, $b$ i $c$ Elements od **S**. Tada **S** opremljen sa dva operatora ispunjava distributivno svojstvo kada je $a \circ (b \diamond c) = (a \circ b) \diamond (a \circ c)$.


Imajte na umu da je, kao i kod grupa, definicija polja veoma apstraktna. Ona ne postavlja nikakve tvrdnje o tipovima Elements u **S**, niti o operacijama $\circ$ i $\diamond$. Samo navodi da je polje bilo koji skup Elements sa dve operacije za koje važe tri gore navedena uslova. („Nulti“ element u drugoj Abelovoj grupi može se apstraktno interpretirati.)


Dakle, šta bi mogao biti primer polja? Dobar primer je skup $\mathbb{Z} \mod 7$, ili $\{0, 1, \ldots, 7\}$ definisan preko standardnog sabiranja (umesto $\circ$ gore) i standardnog množenja (umesto $\diamond$ gore).


Prvo, $\mathbb{Z} \mod 7$ ispunjava uslov da bude Abelova grupa preko sabiranja, i ispunjava uslov da bude Abelova grupa preko množenja ako uzmete u obzir samo nenulte Elements. Drugo, kombinacija skupa sa dva operatora ispunjava distributivni uslov.


Didaktički je korisno istražiti ove tvrdnje koristeći neke posebne vrednosti. Uzmimo eksperimentalne vrednosti 5, 2 i 3, neke nasumično odabrane Elements iz skupa $\mathbb{Z} \mod 7$, da bismo ispitali polje $\langle \mathbb{Z} \mod 7, +, \cdot \rangle$. Koristićemo ove tri vrednosti redom, prema potrebi, da istražimo posebne uslove.


Hajde prvo da istražimo da li je $\mathbb{Z} \mod 7$ opremljen sabiranjem Abelova grupa.


1. **Uslov zatvorenosti**: Uzmimo 5 i 2 kao naše vrednosti. U tom slučaju, $[5 + 2] \mod 7 = 7 \mod 7 = 0$. Ovo je zaista element skupa $\mathbb{Z} \mod 7$, tako da je rezultat u skladu sa uslovom zatvorenosti.

2. **Asocijativni uslov**: Uzmimo 5, 2 i 3 kao naše vrednosti. U tom slučaju, $[(5 + 2) + 3] \mod 7 = [5 + (2 + 3)] \mod 7 = 10 \mod 7 = 3$. Ovo je u skladu sa asocijativnim uslovom.

3. **Identitetni uslov**: Uzmimo 5 kao našu vrednost. U tom slučaju, $[5 + 0] \mod 7 = [0 + 5] \mod 7 = 5$. Dakle, 0 izgleda kao identitetni element za sabiranje.

4. **Inverzni uslov**: Razmotrimo inverz od 5. Potrebno je da važi $[5 + d] \mod 7 = 0$, za neku vrednost $d$. U ovom slučaju, jedinstvena vrednost iz $\mathbb{Z} \mod 7$ koja ispunjava ovaj uslov je 2.

5. **Uslov komutativnosti**: Uzmimo 5 i 3 kao naše vrednosti. U tom slučaju, $[5 + 3] \mod 7 = [3 + 5] \mod 7 = 1$. Ovo je u skladu sa uslovom komutativnosti.


Skup $\mathbb{Z} \mod 7$ opremljen sabiranjem očigledno izgleda kao Abelova grupa. Hajde sada da istražimo da li je $\mathbb{Z} \mod 7$ opremljen množenjem Abelova grupa za sve nenulte Elements.


1. **Uslov zatvorenosti**: Uzmimo 5 i 2 kao naše vrednosti. U tom slučaju, $[5 \cdot 2] \mod 7 = 10 \mod 7 = 3$. Ovo je takođe element skupa $\mathbb{Z} \mod 7$, tako da je rezultat u skladu sa uslovom zatvorenosti.

2. **Asocijativni uslov**: Uzmimo 5, 2 i 3 kao naše vrednosti. U tom slučaju, $[(5 \cdot 2) \cdot 3] \mod 7 = [5 \cdot (2 \cdot 3)] \mod 7 = 30 \mod 7 = 2$. Ovo je u skladu sa asocijativnim uslovom.

3. **Uslov identiteta**: Uzmimo 5 kao našu vrednost. U tom slučaju, $[5 \cdot 1] \mod 7 = [1 \cdot 5] \mod 7 = 5$. Dakle, 1 izgleda kao identitetni element za množenje.

4. **Inverzni uslov**: Razmotrimo inverz od 5. Potrebno je da važi $[5 \cdot d] \mod 7 = 1$, za neku vrednost $d$. Jedinstvena vrednost iz $\mathbb{Z} \mod 7$ koja ispunjava ovaj uslov je 3. Ovo je u skladu sa inverznim uslovom.

5. **Uslov komutativnosti**: Uzmimo 5 i 3 kao naše vrednosti. U tom slučaju, $[5 \cdot 3] \mod 7 = [3 \cdot 5] \mod 7 = 15 \mod 7 = 1$. Ovo je u skladu sa uslovom komutativnosti.


Skup $\mathbb{Z} \mod 7$ očigledno izgleda da ispunjava pravila za Abelovu grupu kada se spoji sa sabiranjem ili množenjem nad nenultim Elements.


Konačno, čini se da ovaj skup u kombinaciji sa oba operatora zadovoljava distributivni uslov. Uzmimo 5, 2 i 3 kao naše vrednosti. Vidimo da je $[5 \cdot (2 + 3)] \mod 7 = [5 \cdot 2 + 5 \cdot 3] \mod 7 = 25 \mod 7 = 4$.


Sada smo videli da $\mathbb{Z} \mod 7$ opremljen sa sabiranjem i množenjem ispunjava aksiome za konačno polje kada se testira sa posebnim vrednostima. Naravno, možemo to pokazati i uopšteno, ali ovde to nećemo uraditi.


Ključna razlika je između dve vrste polja: konačna i beskonačna polja.


**Beskonačno polje** uključuje polje gde je skup **S** beskonačno velik. Skup realnih brojeva $\mathbb{R}$ opremljen sabiranjem i množenjem je primer beskonačnog polja. **Konačno polje**, takođe poznato kao **Galoisovo polje**, je polje gde je skup **S** konačan. Naš primer iznad $\langle \mathbb{Z} \mod 7, +, \cdot \rangle$ je konačno polje.


U kriptografiji, prvenstveno smo zainteresovani za konačna polja. Generalno, može se pokazati da konačno polje postoji za neki skup Elements **S** ako i samo ako ima $p^m$ Elements, gde je $p$ prost broj i $m$ pozitivan ceo broj veći ili jednak jedan. Drugim rečima, ako je red nekog skupa **S** prost broj ($p^m$ gde je $m = 1$) ili neka stepena prostog broja ($p^m$ gde je $m > 1$), onda možete pronaći dva operatora $\circ$ i $\diamond$ takva da su ispunjeni uslovi za polje.


Ako neko konačno polje ima prost broj Elements, onda se naziva **prostim poljem**. Ako je broj Elements u konačnom polju stepen prostog broja, onda se polje naziva **proširenim poljem**. U kriptografiji, interesujemo se za oba, i prosta i proširena polja. [2]


Glavna prostoprimna polja od interesa u kriptografiji su ona gde je skup svih celih brojeva modulisan nekim prostim brojem, a operatori su standardno sabiranje i množenje. Ova klasa konačnih polja bi uključivala $\mathbb{Z} \mod 2$, $\mathbb{Z} \mod 3$, $\mathbb{Z} \mod 5$, $\mathbb{Z} \mod 7$, $\mathbb{Z} \mod 11$, $\mathbb{Z} \mod 13$, i tako dalje. Za bilo koje prostoprimno polje $\mathbb{Z} \mod p$, skup celih brojeva polja je sledeći: $\{0, 1, \ldots, p – 2, p – 1\}$.


U kriptografiji, takođe smo zainteresovani za proširena polja, posebno bilo koja polja sa $2^m$ Elements gde je $m > 1$. Takva konačna polja se, na primer, koriste u Rijndael šifri, koja čini osnovu za Advanced Encryption Standard. Dok su prosti brojevi relativno intuitivni, ova proširena polja baze 2 verovatno nisu za one koji nisu upoznati sa apstraktnom algebrom.


Za početak, zaista je tačno da bilo koji skup celih brojeva sa $2^m$ Elements može biti dodeljen sa dva operatora koji bi njihovu kombinaciju učinili poljem (sve dok je $m$ pozitivan ceo broj). Ipak, samo zato što polje postoji ne znači nužno da ga je lako otkriti ili da je posebno praktično za određene primene.


Ispostavlja se da su posebno primenljiva proširenja polja $2^m$ u kriptografiji ona definisana nad posebnim skupovima polinomskih izraza, a ne nekim skupom celih brojeva.


Na primer, pretpostavimo da želimo prošireno polje sa $2^3$ (tj. 8) Elements u skupu. Iako može postojati mnogo različitih skupova koji se mogu koristiti za polja te veličine, jedan takav skup uključuje sve jedinstvene polinome oblika $a_2x^2 + a_1x + a_0$, gde je svaki koeficijent $a_i$ ili 0 ili 1. Dakle, ovaj skup **S** uključuje sledeće Elements:


1. $0$: Slučaj kada je $a_2 = 0$, $a_1 = 0$, i $a_0 = 0$.

2. $1$: Slučaj gde je $a_2 = 0$, $a_1 = 0$, i $a_0 = 1$.

3. $x$: Slučaj kada je $a_2 = 0$, $a_1 = 1$, i $a_0 = 0$.

4. $x + 1$: Slučaj kada je $a_2 = 0$, $a_1 = 1$, i $a_0 = 1$.

5. $x^2$: Slučaj gde je $a_2 = 1$, $a_1 = 0$, i $a_0 = 0$.

6. $x^2 + 1$: Slučaj gde je $a_2 = 1$, $a_1 = 0$, i $a_0 = 1$.

7. $x^2 + x$: Slučaj gde je $a_2 = 1$, $a_1 = 1$, i $a_0 = 0$.

8. $x^2 + x + 1$: Slučaj gde je $a_2 = 1$, $a_1 = 1$, i $a_0 = 1$.


Dakle, **S** bi bio skup $\{0, 1, x, x + 1, x^2, x^2 + 1, x^2 + x, x^2 + x + 1\}$. Koje dve operacije mogu biti definisane nad ovim skupom Elements da bi se osiguralo da njihova kombinacija čini polje?


Prva operacija na skupu **S** ($\circ$) može se definisati kao standardno sabiranje polinoma modulo 2. Sve što treba da uradite je da saberete polinome kao što biste to inače uradili, a zatim primenite modulo 2 na svaki od koeficijenata rezultujućeg polinoma. Evo nekoliko primera:



- $[(x^2) + (x^2 + x + 1)] \mod 2 = [2x^2 + x + 1] \mod 2 = x + 1$
- $[(x^2 + x) + (x)] \mod 2 = [x^2 + 2x] \mod 2 = x^2$
- $[(x + 1) + (x^2 + x + 1)] \mod 2 = [x^2 + 2x + 2] \mod 2 = x^2 + 1$


Druga operacija na skupu **S** ($\diamond$) koja je potrebna za kreiranje polja je složenija. To je neka vrsta množenja, ali ne standardno množenje iz aritmetike. Umesto toga, svaki element treba posmatrati kao vektor i razumeti operaciju kao množenje tih vektora modulo ireducibilni polinom.


Hajde prvo da se okrenemo ideji ireducibilnog polinoma. **Ireducibilni polinom** je onaj koji ne može biti faktorizovan (baš kao što prost broj ne može biti faktorizovan na komponente osim 1 i samog prostog broja). Za naše potrebe, interesuju nas polinomi koji su ireducibilni u odnosu na skup svih celih brojeva. (Imajte na umu da možda možete faktorizovati određene polinome, na primer, realnim ili kompleksnim brojevima, čak i ako ih ne možete faktorizovati koristeći cele brojeve.)


Na primer, razmotrite polinom $x^2 - 3x + 2$. Ovo se može prepisati kao $(x – 1)(x – 2)$. Dakle, ovo nije ireducibilno. Sada razmotrite polinom $x^2 + 1$. Koristeći samo cele brojeve, ne postoji način da se ovaj izraz dalje faktoriše. Dakle, ovo je ireducibilan polinom u odnosu na cele brojeve.


Sledeće, okrenimo se konceptu množenja vektora. Nećemo detaljno istraživati ovu temu, ali treba da razumete osnovno pravilo: Bilo koja podela vektora može se izvršiti sve dok deljenik ima stepen viši ili jednak stepenu delioca. Ako deljenik ima niži stepen od delioca, tada deljenik više ne može biti podeljen deliocem.


Na primer, razmotrite izraz $x^6 + x + 1 \mod x^5 + x^2$. Ovo se očigledno dalje redukuje jer je stepen delioca, 6, veći od stepena delitelja, 5. Sada razmotrite izraz $x^5 + x + 1 \mod x^5 + x^2$. Ovo se takođe dalje redukuje, jer su stepen delioca, 5, i delitelja, 5, jednaki.


Međutim, sada razmotrite izraz $x^4 + x + 1 \mod x^5 + x^2$. Ovo se ne može dalje redukovati, jer je stepen delioca, 4, manji od stepena delitelja, 5.


Na osnovu ovih informacija, sada smo spremni da pronađemo našu drugu operaciju za skup $\{0, 1, x, x + 1, x^2, x^2 + 1, x^2 + x, x^2 + x + 1\}$.


Već sam rekao da se druga operacija treba razumeti kao vektorsko množenje po modulu nekog ireducibilnog polinoma. Taj ireducibilni polinom treba da osigura da druga operacija definiše Abelovu grupu nad **S** i da je konzistentna sa distributivnim uslovom. Dakle, koji bi to ireducibilni polinom trebalo da bude?


Kako su svi vektori u skupu stepena 2 ili nižeg, nerazloživi polinom treba da bude stepena 3. Ako bilo koje množenje dva vektora u skupu daje polinom stepena 3 ili višeg, znamo da modulo polinom stepena 3 uvek daje polinom stepena 2 ili nižeg. Ovo je slučaj zato što je svaki polinom stepena 3 ili višeg uvek deljiv polinomom stepena 3. Pored toga, polinom koji funkcioniše kao delilac mora biti nerazloživ.


Ispostavlja se da postoji nekoliko ireducibilnih polinoma stepena 3 koje bismo mogli koristiti kao naš delilac. Svaki od ovih polinoma definiše različito polje u kombinaciji sa našim skupom **S** i sabiranjem modulo 2. To znači da imate više opcija kada koristite proširena polja $2^m$ u kriptografiji.


Za naš primer, pretpostavimo da odaberemo polinom $x^3 + x + 1$. Ovo je zaista nerazloživo, jer ga ne možete faktorisati koristeći cele brojeve. Pored toga, obezbediće da bilo koje množenje dva Elements da polinom stepena 2 ili manje.


Hajde da prođemo kroz primer druge operacije koristeći polinom $x^3 + x + 1$ kao delilac da bismo ilustrovali kako to funkcioniše. Pretpostavimo da množite Elements $x^2 + 1$ sa $x^2 + x$ u našem skupu **S**. Zatim, treba da izračunamo izraz $[(x^2 + 1) \cdot (x^2 + x)] \mod x^3 + x + 1$. Ovo se može pojednostaviti na sledeći način:



- $[(x^2 + 1) \cdot (x^2 + x)] \mod x^3 + x + 1 =$
- $[x^2 \cdot x^2 + x^2 \cdot x + 1 \cdot x^2 + 1 \cdot x] \mod x^3 + x + 1 =$
- $[x^4 + x^3 + x^2 + x] \mod x^3 + x + 1$


Znamo da se $[x^4 + x^3 + x^2 + x] \mod x^3 + x + 1$ može redukovati jer deljenik ima viši stepen (4) od delitelja (3).


Za početak, možete videti da izraz $x^3 + x + 1$ ulazi u $x^4 + x^3 + x^2 + x$ ukupno $x$ puta. Ovo možete proveriti množenjem $x^3 + x + 1$ sa $x$, što je $x^4 + x^2 + x$. Kako je poslednji član istog stepena kao i deljenik, naime 4, znamo da ovo funkcioniše. Ostatak ove deljenja po $x$ možete izračunati na sledeći način:



- $[(x^4 + x^3 + x^2 + x) - (x^4 + x^2 + x)] \mod x^3 + x + 1 =$
- $[x^3] \mod x^3 + x + 1 =$
- $x^3$


Dakle, nakon deljenja $x^4 + x^3 + x^2 + x$ sa $x^3 + x + 1$ ukupno $x$ puta, imamo ostatak $x^3$. Može li se ovo dalje deliti sa $x^3 + x + 1$?


Intuitivno, može biti privlačno reći da se $x^3$ više ne može deliti sa $x^3 + x + 1$, jer se čini da je ovaj drugi član veći. Međutim, setite se naše ranije diskusije o deljenju vektora. Sve dok deljenik ima stepen veći ili jednak deliocu, izraz se može dalje redukovati. Konkretno, izraz $x^3 + x + 1$ može ući u $x^3$ tačno 1 put. Ostatak se izračunava na sledeći način:


$$
[(x^3) - (x^3 + x + 1)] \mod x^3 + x + 1 = [x + 1] \mod x^3 + x + 1 = x + 1
$$


Možda se pitate zašto $(x^3) - (x^3 + x + 1)$ daje $x + 1$ a ne $-x - 1$. Zapamtite da je prva operacija našeg polja definisana modulo 2. Dakle, oduzimanje dva vektora daje potpuno isti rezultat kao i sabiranje dva vektora.


Da sumiramo množenje $x^2 + 1$ i $x^2 + x$: Kada pomnožite ta dva člana, dobijate polinom stepena 4, $x^4 + x^3 + x^2 + x$, koji treba da se redukuje modulo $x^3 + x + 1$. Polinom stepena 4 je deljiv sa $x^3 + x + 1$ tačno $x + 1$ puta. Ostatak nakon deljenja $x^4 + x^3 + x^2 + x$ sa $x^3 + x + 1$ tačno $x + 1$ puta je $x + 1$. Ovo je zaista element u našem skupu $\{0, 1, x, x + 1, x^2, x^2 + 1, x^2 + x, x^2 + x + 1\}$.


Zašto bi proširena polja sa bazom 2 nad skupovima polinoma, kao u gornjem primeru, bila korisna za kriptografiju? Razlog je taj što koeficijente u polinomima takvih skupova, bilo 0 ili 1, možete posmatrati kao Elements binarnih nizova određene dužine. Skup **S** u našem gornjem primeru, na primer, mogao bi se posmatrati kao skup **S** koji uključuje sve binarne nizove dužine 3 (000 do 111). Operacije na **S**, zatim, mogu se koristiti za izvođenje operacija na ovim binarnim nizovima i proizvodnju binarnog niza iste dužine.


**Beleške:**


[2] Proširena polja postaju veoma kontraintuitivna. Umesto da imaju Elements celih brojeva, ona imaju skupove polinoma. Pored toga, sve operacije se izvode modulo nekog neprelaznog polinoma.



## Apstraktna algebra u praksi

<chapterId>ed35b98d-18b4-5790-9911-1078e0f84f92</chapterId>


Uprkos formalnom jeziku i apstraktnosti diskusije, koncept grupe ne bi trebalo da bude previše težak za razumevanje. To je samo skup Elements zajedno sa binarnom operacijom, gde izvršavanje te binarne operacije na tim Elements ispunjava četiri opšta uslova. Abelova grupa ima samo dodatni uslov poznat kao komutativnost. Ciklična grupa, zauzvrat, je posebna vrsta Abelove grupe, naime ona koja ima generator. Polje je samo složenija konstrukcija iz osnovnog pojma grupe.


Ali ako ste praktično nastrojena osoba, mogli biste se zapitati u ovom trenutku: Koga briga? Da li poznavanje nekog skupa Elements sa operatorom kao grupe, ili čak Abelove ili ciklične grupe, ima ikakvu relevantnost u stvarnom svetu? Da li je važno znati da je nešto polje?


Bez ulaženja u previše detalja, odgovor je „da“. Grupe su prvi put stvorene u 19. veku od strane francuskog matematičara Evarista Galoisa. On ih je koristio da donese zaključke o rešavanju polinomskih jednačina stepena višeg od pet.


Od tada je koncept grupe pomogao da se rasvetli niz problema u matematici i drugim oblastima. Na njihovoj osnovi, na primer, fizičar Murray-Gellman je bio u stanju da predvidi postojanje čestice pre nego što je ona zapravo primećena u eksperimentima. [3] Za još jedan primer, hemičari koriste teoriju grupa za klasifikaciju oblika molekula. Matematičari su čak koristili koncept grupe da izvuku zaključke o nečemu tako konkretnom kao što je tapeta!


U suštini, pokazivanje da je skup Elements sa nekim operatorom grupa znači da ono što opisujete ima određenu simetriju. Ne simetriju u uobičajenom smislu te reči, već u apstraktnijem obliku. I ovo može pružiti značajne uvide u određene sisteme i probleme. Složeniji pojmovi iz apstraktne algebre samo nam daju dodatne informacije.


Najvažnije je da ćete videti značaj brojevnih teorijskih grupa i polja u praksi kroz njihovu primenu u kriptografiji, posebno u kriptografiji javnog ključa. Već smo videli u našoj diskusiji o poljima, na primer, kako se proširena polja koriste u Rijndael šifri. Taj primer ćemo razraditi u *Poglavlju 5*.


Za dalju diskusiju o apstraktnoj algebri, preporučio bih odličan serijal video zapisa o apstraktnoj algebri od Socratica. [4] Posebno bih preporučio sledeće video zapise: „Šta je apstraktna algebra?“, „Definicija grupe (prošireno)“, „Definicija prstena (prošireno)“ i „Definicija polja (prošireno).“ Ova četiri video zapisa će vam pružiti dodatni uvid u većinu gore navedene diskusije. (Nismo diskutovali o prstenovima, ali polje je samo poseban tip prstena.)


Za dalju diskusiju o modernoj teoriji brojeva, možete se konsultovati sa mnogim naprednim diskusijama o kriptografiji. Kao predloge bih ponudio Introduction to Modern Cryptography Jonathana Katza i Yehude Lindella ili Understanding Cryptography Christofa Paara i Jana Pelzla za dalju diskusiju. [5]


**Beleške:**


[3] Pogledajte [YouTube Video](https://www.youtube.com/watch?v=NOMUnMuxDZY&feature=youtu.be)


[4] Socratica, [Apstraktna algebra](https://www.socratica.com/subject/abstract-algebra)


[5] Katz i Lindell, *Introduction to Modern Cryptography*, 2. izd., 2015 (CRC Press: Boca Raton, FL). Paar i Pelzl, *Understanding Cryptography*, 2010 (Springer-Verlag: Berlin).




# Simetrična kriptografija

<partId>ef768d0e-fe7b-510c-87d6-6febb3de1039</partId>



## Alice i Bob

<chapterId>47345330-be2d-5faf-afd0-d289a8d21bf1</chapterId>


Jedna od dve glavne grane kriptografije je simetrična kriptografija. Ona uključuje šeme šifrovanja, kao i šeme koje se bave autentifikacijom i integritetom. Do 1970-ih, cela kriptografija bi se sastojala od simetričnih šema šifrovanja.


Glavna diskusija počinje razmatranjem simetričnih šema šifrovanja i pravljenjem ključne razlike između strujnih šifara i blok šifara. Zatim se okrećemo kodovima za autentifikaciju poruka, koji su šeme za osiguranje integriteta i autentičnosti poruka. Na kraju, istražujemo kako se simetrične šeme šifrovanja i kodovi za autentifikaciju poruka mogu kombinovati kako bi se osigurala sigurna komunikacija.


Ovo poglavlje usputno razmatra različite simetrične kriptografske šeme iz prakse. Sledeće poglavlje nudi detaljno izlaganje enkripcije pomoću strujne šifre i blokovske šifre iz prakse, naime RC4 i AES respektivno.


Pre nego što započnemo našu diskusiju o simetričnoj kriptografiji, želim ukratko da dam nekoliko napomena o ilustracijama Alise i Boba u ovom i narednim poglavljima.


___


U ilustrovanju principa kriptografije, ljudi često koriste primere koji uključuju Alisu i Boba. I ja ću to učiniti.


Posebno ako ste novi u kriptografiji, važno je shvatiti da su ovi primeri sa Alisom i Bobom namenjeni samo kao ilustracije kriptografskih principa i konstrukcija u pojednostavljenom okruženju. Međutim, principi i konstrukcije su primenljivi na mnogo širi spektar stvarnih konteksta.


Sledećih pet ključnih tačaka treba imati na umu kada su u pitanju primeri koji uključuju Alisu i Boba u kriptografiji:


1. Oni se lako mogu prevesti u primere sa drugim tipovima aktera kao što su kompanije ili vladine organizacije.

2. Oni se lako mogu proširiti da uključe tri ili više aktera.

3. U primerima, Bob i Alice su obično aktivni učesnici u kreiranju svake poruke i u primeni kriptografskih šema na tu poruku. Ali u stvarnosti, elektronske komunikacije su uglavnom automatizovane. Kada posetite veb-sajt koristeći transportnu Layer sigurnost, na primer, kriptografija se obično u potpunosti obrađuje od strane vašeg računara i veb servera.

4. U kontekstu elektronske komunikacije, „poruke“ koje se šalju preko komunikacionog kanala obično su TCP/IP paketi. Oni mogu pripadati e-mailu, Facebook poruci, telefonskom razgovoru, prenosu fajlova, vebsajtu, otpremi softvera i slično. Oni nisu poruke u tradicionalnom smislu. Ipak, kriptografi će često pojednostaviti ovu stvarnost navodeći da je poruka, na primer, e-mail.

5. Primeri se obično fokusiraju na elektronsku komunikaciju, ali se takođe mogu proširiti na tradicionalne oblike komunikacije kao što su pisma.



## Simetrične šeme šifrovanja

<chapterId>41bfdbe1-6d41-5272-98bb-81f24b2fd6af</chapterId>


Možemo slobodno definisati **simetričnu šemu šifrovanja** kao bilo koju kriptografsku šemu sa tri algoritma:


1. **Algoritam za generisanje ključeva**, koji generiše privatni ključ.

2. **Algoritam za šifrovanje**, koji uzima privatni ključ i otvoreni tekst kao ulaze i daje šifrovani tekst kao izlaz.

3. **Algoritam dešifrovanja**, koji uzima privatni ključ i šifrovani tekst kao ulaze i daje originalni otvoreni tekst kao izlaz.


Tipično, šema enkripcije—bilo simetrična ili asimetrična—nudi šablon za enkripciju zasnovan na osnovnom algoritmu, a ne tačnu specifikaciju.


Na primer, razmotrite Salsa20, simetričnu šemu šifrovanja. Može se koristiti sa dužinama ključa od 128 i 256 bita. Izbor dužine ključa utiče na neke manje detalje algoritma (tačnije, na broj rundi u algoritmu).


Ali ne bi se reklo da je korišćenje Salsa20 sa 128-bitnim ključem drugačija šema enkripcije od Salsa20 sa 256-bitnim ključem. Osnovni algoritam ostaje isti. Samo kada se osnovni algoritam promeni, zaista bismo govorili o dve različite šeme enkripcije.


Simetrične šeme šifrovanja su obično korisne u dve vrste slučajeva: (1) One u kojima dva ili više agenata komuniciraju na daljinu i žele da zadrže sadržaj svojih komunikacija tajnim; i (2) one u kojima jedan agent želi da zadrži sadržaj poruke tajnim kroz vreme.


Možete videti prikaz situacije (1) u *Figure 1* ispod. Bob želi da pošalje poruku $M$ Alisi preko određene distance, ali ne želi da drugi mogu da pročitaju tu poruku.


Bob prvo šifrira poruku $M$ privatnim ključem $K$. Zatim šalje šifrat $C$ Alisi. Kada Alisa primi šifrat, može ga dešifrovati koristeći ključ $K$ i pročitati otvoreni tekst. Sa dobrim šifarskim sistemom, svaki napadač koji presretne šifrat $C$ ne bi trebalo da može saznati ništa od stvarnog značaja o poruci $M$.


Možete videti prikaz situacije (2) na *Slici 2* ispod. Bob želi da spreči druge da vide određene informacije. Tipična situacija može biti da je Bob zaposleni koji čuva osetljive podatke na svom računaru, koje ni autsajderi ni njegove kolege ne bi trebalo da čitaju.


Bob šifruje poruku $M$ u trenutku $T_0$ sa ključem $K$ da bi proizveo šifrat $C$. U trenutku $T_1$ mu ponovo treba poruka, i dešifruje šifrat $C$ sa ključem $K$. Bilo koji napadač koji bi mogao naići na šifrat $C$ u međuvremenu ne bi trebalo da može da zaključi ništa značajno o $M$ iz njega.



*Slika 1: Tajnost kroz prostor*


![Figure 1: Secrecy across space](assets/Figure4-1.webp "Figure 1: Secrecy across space")



*Slika 2: Tajnost kroz vreme*



![Figure 2: Secrecy across time](assets/Figure4-2.webp "Figure 2: Secrecy across time")




## Primer: Šifriranje pomakom

<chapterId>7b179ae8-8d15-5e80-a43f-22c970d87b5e</chapterId>


U Poglavlju 2, susreli smo se sa šifrom pomaka, koja je primer veoma jednostavne simetrične šeme šifrovanja. Hajde da je ponovo pogledamo ovde.


Pretpostavimo rečnik *D* koji izjednačava sva slova engleske abecede, redom, sa skupom brojeva $\{0,1,2,\dots,25\}$. Pretpostavimo skup mogućih poruka **M**. Šifrovanje pomakom je, zatim, šema šifrovanja definisana na sledeći način:



- Nasumično izaberi ključ $k$ iz skupa mogućih ključeva **K**, gde je **K** = $\{0,1,2,\dots,25\}$
- Šifrujte poruku $m \in$ **M**, na sledeći način:
    - Razdvoj $m$ na njegova pojedinačna slova $m_0, m_1,\dots, m_i, \dots, m_l$
    - Pretvori svaki $m_i$ u broj prema *D*
    - Za svaki $m_i$, $c_i = [(m_i + k) \mod 26]$
    - Pretvori svaki $c_i$ u slovo prema *D*
    - Zatim kombinujte $c_0, c_1,\dots, c_l$ da biste dobili šifrat $c$
- Dekriptuj šifrovani tekst $c$ na sledeći način:
    - Pretvori svaki $c_i$ u broj prema *D*
    - Za svaki $c_i$, $m_i = [(c_i - k) \mod 26]$
    - Pretvorite svaki $m_i$ u slovo prema *D*
    - Zatim kombinujte $m_0, m_1,\dots, m_l$ da biste dobili originalnu poruku $m$


Ono što čini šifru pomaka simetričnom šemom enkripcije je to što se isti ključ koristi i za proces enkripcije i za proces dekripcije. Na primer, pretpostavimo da želite da šifrujete poruku "DOG" koristeći šifru pomaka, i da ste nasumično odabrali "24" kao ključ. Šifrovanje poruke ovim ključem bi dalo "BME". Jedini način da se povrati originalna poruka je korišćenjem istog ključa, "24", za proces dekripcije.


Ovaj Shift šifra je primer **monoalfabetske supstitucione šifre**: šema šifrovanja gde je alfabet šifrovanog teksta fiksiran (tj. koristi se samo jedan alfabet). Pod pretpostavkom da je algoritam dešifrovanja deterministički, svaki simbol u šifrovanom tekstu supstitucije može se odnositi na najviše jedan simbol u otvorenom tekstu.


Sve do 1700-ih, mnoge primene enkripcije su se u velikoj meri oslanjale na monoalfabetske supstitucione šifre, iako su često bile mnogo složenije od Šifrove šifre. Mogli ste, na primer, nasumično izabrati slovo iz alfabeta za svako originalno slovo teksta pod uslovom da se svako slovo pojavljuje samo jednom u alfabetu šifrovanog teksta. To znači da biste imali faktorijel od 26 mogućih privatnih ključeva, što je bilo ogromno u doba pre računara.


Imajte na umu da ćete često naići na termin **cipher** u kriptografiji. Budite svesni da ovaj termin ima različita značenja. Zapravo, znam najmanje pet različitih značenja ovog termina unutar kriptografije.


U nekim slučajevima se odnosi na šemu šifrovanja, kao što je to slučaj kod Shift šifre i monoalfabetske supstitucione šifre. Međutim, termin se takođe može odnositi specifično na algoritam šifrovanja, privatni ključ, ili samo na šifrat bilo koje takve šeme šifrovanja.


Na kraju, termin šifra može se odnositi i na osnovni algoritam iz kojeg možete konstruisati kriptografske šeme. Ovo može uključivati različite algoritme za šifrovanje, ali i druge tipove kriptografskih šema. Ovaj smisao termina postaje relevantan u kontekstu blok šifara (pogledajte odeljak „Blok šifre“ ispod).


Možda ćete naići i na termine **encipher** ili **decipher**. Ovi termini su samo sinonimi za enkripciju i dekripciju.



## Napadi grubom silom i Kerckhoffov princip

<chapterId>2d73ef97-26c5-5d11-8815-0ddbe89c8003</chapterId>


Šifarska zamena je veoma nesigurna simetrična šema šifrovanja, barem u modernom svetu. [1] Napadač bi mogao jednostavno pokušati dešifrovanje bilo kog šifrovanog teksta sa svih 26 mogućih ključeva da vidi koji rezultat ima smisla. Ova vrsta napada, gde napadač samo prolazi kroz ključeve da vidi šta funkcioniše, poznata je kao **brute force napad** ili **iscrpna pretraga ključeva**.


Da bi bilo koja šema enkripcije ispunila minimalni pojam sigurnosti, mora imati skup mogućih ključeva, ili **ključni prostor**, koji je toliko veliki da su napadi grubom silom neizvodljivi. Sve moderne šeme enkripcije ispunjavaju ovaj standard. To je poznato kao **princip dovoljnog ključnog prostora**. Sličan princip se obično primenjuje u različitim vrstama kriptografskih šema.


Da biste stekli osećaj o veličini prostora ključeva u modernim šemama enkripcije, pretpostavimo da je fajl enkriptovan sa 128-bitnim ključem koristeći napredni standard enkripcije. To znači da napadač ima skup od $2^{128}$ ključeva koje treba da prođe za napad grubom silom. Šansa od 0.78% uspeha sa ovom strategijom zahtevala bi da napadač prođe kroz otprilike $2.65 \times 10^{36}$ ključeva.


Pretpostavimo da optimistično pretpostavimo da napadač može pokušati $10^{16}$ ključeva u sekundi (tj. 10 kvadriliona ključeva u sekundi). Da bi testirala 0,78% svih ključeva u prostoru ključeva, njen napad bi morao trajati $2,65 \times 10^{20}$ sekundi. To je oko 8,4 triliona godina. Dakle, čak ni napad grubom silom od strane apsurdno moćnog protivnika nije realističan sa modernom 128-bitnom šemom enkripcije. Ovo je princip dovoljnog prostora ključeva na delu.


Da li je šifrovanje pomakom sigurnije ako napadač ne zna algoritam šifrovanja? Možda, ali ne mnogo.


U svakom slučaju, moderna kriptografija uvek pretpostavlja da sigurnost bilo koje simetrične šeme šifrovanja zavisi samo od čuvanja privatnog ključa u tajnosti. Pretpostavlja se da napadač zna sve ostale detalje, uključujući prostor poruka, prostor ključeva, prostor šifrovanog teksta, algoritam za izbor ključa, algoritam za šifrovanje i algoritam za dešifrovanje.


Ideja da sigurnost simetrične šeme šifrovanja može zavisiti samo od tajnosti privatnog ključa poznata je kao **Kerckhoffsov princip**.


Kako je prvobitno zamislio Kerckhoffs, princip se odnosi samo na simetrične šeme šifrovanja. Međutim, opštija verzija principa takođe se primenjuje na sve druge savremene tipove kriptografskih šema: Dizajn bilo koje kriptografske šeme ne sme biti potreban da bude tajan kako bi bila sigurna; tajnost se može odnositi samo na neke nizove informacija, obično privatni ključ.


Kerckhoffsovo načelo je ključno za modernu kriptografiju iz četiri razloga. [2] Prvo, postoji samo ograničen broj kriptografskih šema za određene tipove aplikacija. Na primer, većina modernih simetričnih enkripcijskih aplikacija koristi Rijndael šifru. Dakle, vaša tajnost u vezi sa dizajnom šeme je veoma ograničena. Međutim, postoji mnogo više fleksibilnosti u čuvanju neke privatne ključeve za Rijndael šifru tajnom.


Drugo, lakše je zameniti neki niz informacija nego čitavu kriptografsku šemu. Pretpostavimo da svi zaposleni u jednoj kompaniji koriste isti softver za enkripciju i da svaki par zaposlenih ima privatni ključ za poverljivu komunikaciju. Kompromitovanje ključeva je problem u ovom scenariju, ali barem bi kompanija mogla zadržati softver uprkos takvim sigurnosnim propustima. Ako bi kompanija zavisila od tajnosti šeme, tada bi svaki propust te tajnosti zahtevao zamenu celog softvera.


Treće, Kerckhoffsov princip omogućava standardizaciju i kompatibilnost između korisnika kriptografskih šema. Ovo ima ogromne prednosti za efikasnost. Na primer, teško je zamisliti kako bi milioni ljudi mogli sigurno da se povežu na Google-ove veb servere svakog dana, ako bi ta sigurnost zahtevala čuvanje kriptografskih šema u tajnosti.


Četvrto, Kerckhoffov princip omogućava javnu proveru kriptografskih šema. Ova vrsta provere je apsolutno neophodna za postizanje sigurnih kriptografskih šema. Ilustrativno, glavni osnovni algoritam u simetričnoj kriptografiji, Rijndael šifra, bio je rezultat takmičenja organizovanog od strane Nacionalnog instituta za standarde i tehnologiju između 1997. i 2000. godine.


Bilo koji sistem koji pokušava da postigne **sigurnost kroz skrivanje** je onaj koji se oslanja na čuvanje detalja svog dizajna i/ili implementacije u tajnosti. U kriptografiji, ovo bi bio specifično sistem koji se oslanja na čuvanje detalja dizajna kriptografskog šema u tajnosti. Dakle, sigurnost kroz skrivanje je u direktnom kontrastu sa Kerckhoffsovim principom.


Sposobnost otvorenosti da poboljša kvalitet i sigurnost takođe se šire odnosi na digitalni svet, a ne samo na kriptografiju. Besplatne i otvorene Linux distribucije kao što je Debian, na primer, generalno imaju nekoliko prednosti u odnosu na svoje Windows i MacOS pandane u smislu privatnosti, stabilnosti, sigurnosti i fleksibilnosti. Iako to može imati više uzroka, najvažniji princip je verovatno, kako je Eric Raymond izrazio u svom poznatom eseju "Katedrala i bazar," da "ako dovoljno ljudi gleda, svi bagovi su plitki." [3] Upravo ovaj princip mudrosti mase dao je Linuxu njegov najznačajniji uspeh.


Nikada se ne može nedvosmisleno tvrditi da je kriptografska šema "sigurna" ili "nesigurna." Umesto toga, postoje različiti pojmovi sigurnosti za kriptografske šeme. Svaka **definicija kriptografske sigurnosti** mora specificirati (1) ciljeve sigurnosti, kao i (2) sposobnosti napadača. Analiziranje kriptografskih šema prema jednom ili više specifičnih pojmova sigurnosti pruža uvid u njihove primene i ograničenja.


Iako nećemo ulaziti u sve detalje različitih pojmova kriptografske sigurnosti, trebali biste znati da su dve pretpostavke sveprisutne u svim modernim kriptografskim pojmovima sigurnosti koji se odnose na simetrične i asimetrične šeme (i u nekom obliku na druge kriptografske primitive):



- Napadačevo znanje o šemi je u skladu sa Kerckhoffsovim principom.
- Napadač ne može izvodljivo izvršiti brute force napad na šemu. Konkretno, modeli pretnji kriptografskih pojmova sigurnosti obično čak ni ne dozvoljavaju brute force napade, jer pretpostavljaju da oni nisu relevantna razmatranja.



**Beleške:**


[1] Prema Seutoniju, šifru pomaka sa konstantnom ključnom vrednošću od 3 koristio je Julije Cezar u svojim vojnim komunikacijama. Tako bi A uvek postajalo D, B uvek E, C uvek F, i tako dalje. Ova posebna verzija šifre pomaka je, stoga, postala poznata kao **Cezarova šifra** (iako to zapravo nije šifra u modernom smislu reči, jer je ključna vrednost konstantna). Cezarova šifra je možda bila sigurna u prvom veku pre nove ere, ako su neprijatelji Rima bili veoma neupoznati sa enkripcijom. Ali očigledno ne bi bila veoma sigurna šema u modernim vremenima.


[2] Jonathan Katz i Yehuda Lindell, _Introduction to Modern Cryptography_, CRC Press (Boca Raton, FL: 2015), str. 7f.


[3] Eric Raymond, “The Cathedral and the Bazaar,” paper was presented at the Linux Kongress, Würzburg, Germany (May 27, 1997). There are a number of subsequent versions available as well as a book. My citations are from page 30 in the book: Eric Raymond, _The Cathedral and the Bazaar: Musings on Linux and Open Source by an Accidental Revolutionary_, revised edn. (2001), O’Reilly: Sebastopol, CA.



## Stream šifre

<chapterId>479aa6f4-45c4-59ca-8616-8cf8e61fc871</chapterId>


Simetrične šeme šifrovanja standardno se dele na dva tipa: **strujni šifri** i **blok šifri**. Ova razlika je donekle problematična, međutim, jer ljudi koriste ove termine na nedosledan način. U narednih nekoliko odeljaka, izložiću razliku na način za koji mislim da je najbolji. Trebalo bi da budete svesni, međutim, da će mnogi ljudi koristiti ove termine donekle drugačije nego što sam izložio.


Okrenimo se prvo ka strim šiframa. **Strim šifra** je simetrična šema šifrovanja gde se šifrovanje sastoji iz dva koraka.


Prvo, niz dužine otvorenog teksta se proizvodi putem privatnog ključa. Ovaj niz se naziva **keystream**.


Zatim se keystream matematički kombinuje sa otvorenim tekstom kako bi se proizveo šifrovani tekst. Ova kombinacija je obično XOR operacija. Za dešifrovanje, možete jednostavno obrnuti operaciju. (Napomena da $A \oplus B = B \oplus A$, u slučaju kada su $A$ i $B$ nizovi bitova. Dakle, redosled XOR operacije u strim šifri nije bitan za rezultat. Ovo svojstvo je poznato kao **komutativnost**.)


Tipična XOR strim šifra prikazana je na *Slici 3*. Prvo uzimate privatni ključ $K$ i koristite ga za generate generisanje ključa toka. Ključ toka se zatim kombinuje sa otvorenim tekstom putem XOR operacije kako bi se proizveo šifrovani tekst. Bilo koji agent koji primi šifrovani tekst može ga lako dešifrovati ako ima ključ $K$. Sve što treba da uradi je da kreira ključ toka iste dužine kao šifrovani tekst prema specificiranoj proceduri šeme i primeni XOR sa šifrovani tekst.



*Slika 3: XOR tokovna šifra*


![Figure 3: An XOR stream cipher](assets/Figure4-3.webp "Figure 3: An XOR stream cipher")


Podsetite se da je šema šifrovanja obično šablon za šifrovanje sa istim osnovnim algoritmom, a ne tačna specifikacija. Po analogiji, strim šifra je obično šablon za šifrovanje u kojem možete koristiti ključeve različitih dužina. Iako dužina ključa može uticati na neke manje detalje šeme, neće uticati na njen suštinski oblik.


Šifarski sistem pomaka je primer veoma jednostavnog i nesigurnog strim šifra. Koristeći jedno slovo (privatni ključ), možete proizvesti niz slova dužine poruke (keystream). Ovaj keystream se zatim kombinuje sa otvorenim tekstom putem modulo operacije kako bi se proizveo šifrovani tekst. (Ova modulo operacija može biti pojednostavljena u XOR operaciju kada se slova predstavljaju u bitovima).


Još jedan poznati primer toka šifre je **Vigenere šifra**, nazvana po Blaise de Vigenereu koji ju je u potpunosti razvio krajem 16. veka (iako su drugi uradili mnogo prethodnog rada). To je primer **polialfabetske supstitucione šifre**: šema šifrovanja gde se alfabet šifrovanog teksta za simbol otvorenog teksta menja u zavisnosti od njegove pozicije u tekstu. Za razliku od monoalfabetske supstitucione šifre, simboli šifrovanog teksta mogu biti povezani sa više od jednog simbola otvorenog teksta.


Kako je enkripcija postajala popularna u renesansnoj Evropi, tako je i **kriptanaliza**—odnosno, razbijanje šifrovanih tekstova—posebno korišćenjem **analize frekvencije**. Ova poslednja koristi statističke pravilnosti u našem jeziku za razbijanje šifrovanih tekstova, a otkrili su je arapski učenjaci već u devetom veku. To je tehnika koja posebno dobro funkcioniše sa dužim tekstovima. Čak ni najsloženije monoalfabetske supstitucione šifre više nisu bile dovoljne protiv analize frekvencije do 1700-ih u Evropi, posebno u vojnim i bezbednosnim okruženjima. Kako je Viženerova šifra nudila značajan napredak u sigurnosti, postala je popularna u ovom periodu i bila je široko rasprostranjena do kasnih 1700-ih.


Neformalno govoreći, šema enkripcije funkcioniše na sledeći način:


1. Izaberite višeslovnu reč kao privatni ključ.

2. Za bilo koju poruku, primeni šifru pomaka na svako slovo poruke koristeći odgovarajuće slovo u ključnoj reči kao pomak.

3. Ako ste prošli kroz ključnu reč, ali još uvek niste potpuno šifrovali otvoreni tekst, ponovo primenite slova ključne reči kao šifru pomaka na odgovarajuća slova u preostalom delu teksta.

4. Nastavite ovaj proces dok cela poruka ne bude šifrovana.


Na primer, pretpostavimo da je vaš privatni ključ "GOLD" i želite da šifrujete poruku "CRYPTOGRAPHY". U tom slučaju, postupili biste na sledeći način prema Vigenère šifri:



- $c_0  = [(2 + 6) \mod 26] = 8 = I$
- $c_1  = [(17 + 14) \mod 26] = 5 = F$
- $c_2  = [(24 + 11) \mod 26] = 9 = J$
- $c_3  = [(15 + 3) \mod 26] = 18 = S$
- $c_4  = [(19 + 6) \mod 26] = 25 = Z$
- $c_5  = [(14 + 14) \mod 26] = 2 = C$
- $c_6  = [(6 + 11) \mod 26] = 17 = R$
- $c_7  = [(17 + 3) \mod 26] = 20 = U$
- $c_8  = [(0 + 6) \mod 26] = 6 = G$
- $c_9  = [(15 + 14) \mod 26] = 3 = D$
- $c_{10} = [(7 + 11) \mod 26] = 18 = S$
- $c_{11} = [(24 + 3) \mod 26] = 1 = B$


Dakle, šifrat $c$ = "IFJSZCRUGDSB".


Još jedan poznati primer toka šifre je **one-time pad**. Sa one-time pad-om, jednostavno kreirate niz nasumičnih bitova dužine kao što je poruka u otvorenom tekstu i proizvodite šifrovani tekst putem XOR operacije. Dakle, privatni ključ i tok ključeva su ekvivalentni sa one-time pad-om.


Iako su Šifarski šifra i Viženerove šifre veoma nesigurne u modernom dobu, jednokratna šifra je veoma sigurna ako se pravilno koristi. Verovatno najpoznatija primena jednokratne šifre bila je, barem do 1980-ih, za **Vašington-Moskva vruću liniju**. [4]


Hotline je direktna komunikaciona veza između Vašingtona i Moskve za hitna pitanja koja je instalirana nakon Kubanske raketne krize. Tehnologija za nju se transformisala tokom godina. Trenutno, uključuje direktni optički kabl kao i dve satelitske veze (za redundanciju), koje omogućavaju e-mail i slanje tekstualnih poruka. Veza se završava na raznim mestima u SAD. Pentagon, Bela kuća i Raven Rock Mountain su poznate krajnje tačke. Suprotno popularnom mišljenju, hotline nikada nije uključivao telefone.


U suštini, šema jednokratnog bloka funkcionisala je na sledeći način. I Vašington i Moskva bi imali dva seta nasumičnih brojeva. Jedan set nasumičnih brojeva, kreiran od strane Rusa, odnosio se na šifrovanje i dešifrovanje bilo koje poruke na ruskom jeziku. Jedan set nasumičnih brojeva, kreiran od strane Amerikanaca, odnosio se na šifrovanje i dešifrovanje bilo koje poruke na engleskom jeziku. S vremena na vreme, više nasumičnih brojeva bi bilo dostavljeno drugoj strani putem poverljivih kurira.


Vašington i Moskva su, tada, mogli tajno komunicirati koristeći ove nasumične brojeve za kreiranje jednokratnih blokova. Svaki put kada je bilo potrebno komunicirati, koristili biste sledeći deo nasumičnih brojeva za vašu poruku.


Iako veoma siguran, jednokratna šifra suočava se sa značajnim praktičnim ograničenjima: ključ mora biti dug koliko i poruka i nijedan deo jednokratne šifre ne sme se ponovo koristiti. To znači da morate pratiti gde se nalazite u jednokratnoj šifri, skladištiti ogroman broj bitova i povremeno razmenjivati Exchange nasumičnih bitova sa svojim partnerima. Kao posledica toga, jednokratna šifra se ne koristi često u praksi.


Umesto toga, pretežno korišćeni strim šifri u praksi su **pseudorandom strim šifri**. Salsa20 i blisko povezana varijanta nazvana ChaCha su primeri često korišćenih pseudorandom strim šifri.


Kod ovih pseudonasumičnih strim šifara, prvo nasumično birate ključ K koji je kraći od dužine otvorenog teksta. Takav nasumični ključ K obično kreira naš računar na osnovu nepredvidivih podataka koje prikuplja tokom vremena, kao što su vreme između mrežnih poruka, pokreti miša, i tako dalje.


Ovaj nasumični ključ $K$ se zatim ubacuje u algoritam ekspanzije koji stvara pseudonasumični tok ključeva dužine poruke. Možete precizno odrediti koliko dugo tok ključeva treba da bude (npr., 500 bita, 1000 bita, 1200 bita, 29,117 bita, itd.).


Pseudonasumični tok ključeva izgleda *kao da* je izabran potpuno nasumično iz skupa svih nizova iste dužine. Stoga, šifrovanje sa pseudonasumičnim tokom ključeva izgleda kao da je urađeno sa jednokratnom podlogom. Ali to, naravno, nije slučaj.


Pošto je naš privatni ključ kraći od toka ključeva i naš algoritam za proširenje mora biti deterministički kako bi proces šifrovanja/dešifrovanja funkcionisao, nije svaki tok ključeva te određene dužine mogao biti rezultat našeg operacije proširenja.


Pretpostavimo, na primer, da naš privatni ključ ima dužinu od 128 bita i da možemo da ga ubacimo u ekspanzivni algoritam kako bismo kreirali mnogo duži keystream, recimo od 2.500 bita. Pošto naš ekspanzivni algoritam mora biti deterministički, naš algoritam može najviše da izabere $1/2^{128}$ stringova sa dužinom od 2.500 bita. Dakle, takav keystream nikada ne bi mogao biti izabran potpuno nasumično iz svih stringova iste dužine.


Naša definicija strim šifre ima dva aspekta: (1) keystream dužine kao što je otvoreni tekst se generiše uz pomoć privatnog ključa; i (2) ovaj keystream se kombinuje sa otvorenim tekstom, obično putem XOR operacije, da bi se proizveo šifrovani tekst.


Ponekad ljudi definišu uslov (1) strožije, tvrdeći da keystream mora biti specifično pseudorandom. To znači da ni shift šifra, ni one-time pad ne bi bili smatrani stream šiframa.


Po mom mišljenju, šire definisanje uslova (1) pruža lakši način za organizovanje šema enkripcije. Pored toga, to znači da ne moramo prestati nazivati određenu šemu enkripcije strim šifrom samo zato što saznamo da se zapravo ne oslanja na pseudonasumične ključeve.


**Beleške:**


[4] Crypto Museum, "Washington-Moscow hotline," 2013, dostupno na [https://www.cryptomuseum.com/crypto/hotline/index.htm](https://www.cryptomuseum.com/crypto/hotline/index.htm).




## Blok šifre

<chapterId>2df52d51-943d-5df7-9d49-333e4c5d97b7</chapterId>


Prvi način na koji se **blok šifra** obično razume jeste kao nešto primitivnije od strim šifre: Osnovni algoritam koji izvodi transformaciju uz očuvanje dužine na nizu odgovarajuće dužine uz pomoć ključa. Ovaj algoritam se može koristiti za kreiranje šema enkripcije i možda drugih tipova kriptografskih šema.


Često, blok šifra može primati ulazne nizove različitih dužina kao što su 64, 128 ili 256 bita, kao i ključeve različitih dužina kao što su 128, 192 ili 256 bita. Iako se neki detalji algoritma mogu promeniti u zavisnosti od ovih varijabli, osnovni algoritam se ne menja. Ako bi se menjao, govorili bismo o dve različite blok šifre. Napomena da je upotreba termina osnovni algoritam ovde ista kao i za šeme šifrovanja.


Prikaz kako blok šifra funkcioniše može se videti na *Slici 4* ispod. Poruka $M$ dužine $L$ i ključ $K$ služe kao ulazi za blok šifru. Ona izlazno daje poruku $M'$ dužine $L$. Ključ ne mora nužno biti iste dužine kao $M$ i $M'$ za većinu blok šifara.


*Slika 4: Blok šifra*


![Figure 4: A block cipher](assets/Figure4-4.webp "Figure 4: A block cipher")


Blok šifra sama po sebi nije šema šifrovanja. Ali blok šifra se može koristiti sa različitim **modovima rada** da bi se proizvele različite šeme šifrovanja. Mod rada jednostavno dodaje neke dodatne operacije izvan blok šifre.


Da bismo ilustrovali kako ovo funkcioniše, pretpostavimo blok šifru (BC) koja zahteva ulazni niz od 128 bita i privatni ključ od 128 bita. Slika 5 ispod prikazuje kako se ta blok šifra može koristiti sa **modom elektronske šifre knjige** (**ECB mod**) za kreiranje šeme enkripcije. (Elipse na desnoj strani ukazuju na to da možete ponavljati ovaj obrazac koliko god je potrebno).


*Slika 5: Blok šifra sa ECB režimom*


![Figure 5: A block cipher with ECB mode](assets/Figure4-5.webp "Figure 5: A block cipher with ECB mode")


Proces za šifrovanje elektronske knjige kodova sa blokovskom šifrom je sledeći. Proverite da li možete podeliti svoju otvorenu poruku na blokove od 128 bita. Ako ne možete, dodajte **popunu** poruci, tako da rezultat može biti ravnomerno podeljen veličinom bloka od 128 bita. Ovo su vaši podaci koji se koriste za proces šifrovanja.


Sada podelite podatke na delove od 128-bitnih nizova ($M_1$, $M_2$, $M_3$, i tako dalje). Provedite svaki 128-bitni niz kroz blok šifru sa vašim 128-bitnim ključem da biste proizveli 128-bitne delove šifrovanog teksta ($C_1$, $C_2$, $C_3$, i tako dalje). Ovi delovi, kada se ponovo spoje, formiraju kompletan šifrovani tekst.


Dekriptovanje je samo obrnut proces, iako primalac treba da ima neki prepoznatljiv način da ukloni bilo kakvo popunjavanje iz dekriptovanih podataka kako bi proizveo originalnu tekstualnu poruku.


Iako relativno jednostavan, blok šifrar sa režimom elektronske kodne knjige nedostaje sigurnost. Ovo je zato što dovodi do **determinističkog šifrovanja**. Bilo koja dva identična 128-bitna niza podataka su šifrovana na potpuno isti način. Te informacije se mogu iskoristiti.


Umesto toga, svaka šema šifrovanja konstruisana od blok šifre treba da bude **probabilistička**: to jest, šifrovanje bilo koje poruke $M$, ili bilo kog specifičnog dela $M$, generalno bi trebalo da daje različit ishod svaki put. [5]


**Način ulančavanja šifarskih blokova** (**CBC način**) je verovatno najčešće korišćen način rada sa blokovskom šifrom. Kombinacija, ako se pravilno uradi, proizvodi verovatnosnu šemu šifrovanja. Prikaz ovog načina rada možete videti na *Slici 6* ispod.


*Slika 6: Blok šifra sa CBC režimom*


![Figure 6: A block cipher with CBC mode](assets/Figure4-6.webp "Figure 6: A block cipher with CBC mode")


Pretpostavimo da je veličina bloka ponovo 128 bita. Dakle, za početak, ponovo biste morali osigurati da vaša originalna tekstualna poruka dobije neophodno popunjavanje.


Zatim, izvršite XOR prve 128-bitne porcije vašeg otvorenog teksta sa **inicijalizacionim vektorom** od 128 bita. Rezultat se stavlja u blok šifru kako bi se proizveo šifrovani tekst za prvi blok. Za drugi blok od 128 bita, prvo izvršite XOR otvorenog teksta sa šifrovanim tekstom iz prvog bloka, pre nego što ga ubacite u blok šifru. Nastavljate ovaj proces dok ne šifrujete celu poruku otvorenog teksta.


Kada završite, pošaljete šifrovanu poruku zajedno sa nešifrovanim inicijalizacionim vektorom primaocu. Primalac mora znati inicijalizacioni vektor, inače ne može dešifrovati šifrat.


Ova konstrukcija je mnogo sigurnija od režima elektronske šifre kada se pravilno koristi. Prvo, treba da osigurate da je inicijalizacioni vektor nasumičan ili pseudonasumičan niz. Pored toga, treba da koristite različit inicijalizacioni vektor svaki put kada koristite ovu šemu enkripcije.


Drugim rečima, vaš inicijalizacioni vektor treba da bude nasumičan ili pseudonasumičan Nonce, gde **Nonce** označava "broj koji se koristi samo jednom." Ako se pridržavate ove prakse, CBC režim sa blokovskom šifrom osigurava da će bilo koja dva identična bloka otvorenog teksta generalno biti šifrovana drugačije svaki put.


Konačno, usmerimo našu pažnju na **output feedback mode** (**OFB mode**). Možete videti prikaz ovog režima na *Slici 7*.


*Slika 7: Blok šifra sa OFB režimom*


![Figure 7: A block cipher with OFB mode](assets/Figure4-7.webp "Figure 7: A block cipher with OFB mode")


Sa OFB režimom takođe birate vektor inicijalizacije. Ali ovde, za prvi blok, vektor inicijalizacije se direktno ubacuje u blok šifru sa vašim ključem. Rezultujućih 128-bitova se zatim tretira kao keystream. Ovaj keystream se XOR-uje sa otvorenim tekstom da bi se proizveo šifrovani tekst za blok. Za naredne blokove, koristite keystream iz prethodnog bloka kao ulaz u blok šifru i ponavljate korake.


Ako pažljivo pogledaš, ono što je zapravo kreirano ovde iz blok šifre sa OFB režimom je strim šifra. Generišeš generate keystream delove od 128-bitova dok ne dobiješ dužinu otvorenog teksta (odbacujući bitove koji ti nisu potrebni iz poslednjeg 128-bitnog keystream dela). Zatim, XOR-uješ keystream sa svojim otvorenim tekstom da dobiješ šifrat.


U prethodnom odeljku o strim šiframa, naveo sam da se generiše keystream uz pomoć privatnog ključa. Tačnije, ne mora biti kreiran samo sa privatnim ključem. Kao što možete videti u OFB modu, keystream se proizvodi uz podršku i privatnog ključa i inicijalizacionog vektora.


Imajte na umu da, kao i kod CBC režima, važno je odabrati pseudonasumičan ili nasumičan Nonce za inicijalizacioni vektor svaki put kada koristite blok šifru u OFB režimu. U suprotnom, isti 128-bitni niz poruka poslat u različitim komunikacijama biće enkriptovan na isti način. Ovo je jedan od načina da se kreira probabilistička enkripcija sa strim šifrom.


Neki strim šifri koriste samo privatni ključ za kreiranje keystream-a. Za te strim šifre, važno je da koristite nasumični Nonce za odabir privatnog ključa za svaku instancu komunikacije. U suprotnom, rezultati enkripcije sa tim strim šiframa će takođe biti deterministički, što dovodi do sigurnosnih problema.


Najpopularnija moderna blok šifra je **Rijndael šifra**. Bila je pobednički rad od petnaest prijava na takmičenju koje je organizovao Nacionalni institut za standarde i tehnologiju (NIST) između 1997. i 2000. godine kako bi se zamenio stariji standard za šifrovanje, **standard za šifrovanje podataka** (**DES**).


Rijndael šifra može se koristiti sa različitim specifikacijama za dužine ključeva i veličine blokova, kao i u različitim režimima rada. Komitet za NIST takmičenje usvojio je ograničenu verziju Rijndael šifre—naime onu koja zahteva veličine blokova od 128 bita i dužine ključeva od 128 bita, 192 bita ili 256 bita—kao deo **naprednog standarda za šifrovanje** (**AES**). Ovo je zaista glavni standard za aplikacije simetričnog šifrovanja. Toliko je siguran da je čak i NSA očigledno spremna da ga koristi sa ključevima od 256 bita za dokumente najviše tajnosti. [6]


AES blok šifra će biti detaljno objašnjena u *Poglavlju 5*.



**Beleške:**


[5] Značaj probabilističkog šifrovanja prvi su istakli Shafi Goldwasser i Silvio Micali, „Probabilistic encryption,“ _Journal of Computer and System Sciences_, 28 (1984), 270–99.


[6] Pogledajte NSA, "Commercial National Security Algorithm Suite", [https://apps.nsa.gov/iaarchive/programs/iad-initiatives/cnsa-suite.cfm](https://apps.nsa.gov/iaarchive/programs/iad-initiatives/cnsa-suite.cfm).




## Raščišćavanje konfuzije

<chapterId>121c1858-27e3-5862-b0ce-4ff2f70f9f0f</chapterId>


Zbrka oko razlike između blok šifara i strim šifara nastaje jer ponekad ljudi razumeju termin blok šifra kao da se odnosi specifično na *blok šifru sa blok režimom enkripcije*.


Razmotrite ECB i CBC režime u prethodnom odeljku. Ovi režimi specifično zahtevaju da podaci za šifrovanje budu deljivi veličinom bloka (što znači da ćete možda morati koristiti popunjavanje za originalnu poruku). Pored toga, podaci u ovim režimima se takođe direktno obrađuju blokovskom šifrom (a ne samo kombinovanjem sa rezultatom operacije blokovske šifre kao u OFB režimu).


Stoga, alternativno, možete definisati **blok šifru** kao bilo koju šemu enkripcije koja operiše na blokovima fiksne dužine poruke u jednom trenutku (gde bilo koji blok mora biti duži od bajta, inače se pretvara u strim šifru). I podaci za enkripciju i šifrat moraju se ravnomerno deliti na ovu veličinu bloka. Tipično, veličina bloka je 64, 128, 192 ili 256 bita u dužini. Nasuprot tome, strim šifra može enkriptovati bilo koje poruke u delovima od jednog bita ili bajta u isto vreme.


Sa ovim specifičnijim razumevanjem blok šifre, zaista možete tvrditi da su moderni šifarski sistemi ili strujne ili blok šifre. Od sada nadalje, pod pojmom blok šifra misliću u opštijem smislu, osim ako nije drugačije navedeno.


Diskusija o OFB modu u prethodnom odeljku takođe pokreće još jednu zanimljivu tačku. Neki strim šifri su izgrađeni od blok šifri, kao što je Rijndael sa OFB. Neki, kao što su Salsa20 i ChaCha, nisu kreirani od blok šifri. Možete ih nazvati **primitivnim strim šifrima**. (Ne postoji zaista standardizovan termin za označavanje takvih strim šifri.)


Kada ljudi govore o prednostima i nedostacima strim šifara i blok šifara, obično upoređuju primitivne strim šifre sa šemama šifrovanja zasnovanim na blok šiframa.


Iako uvek možete lako konstruisati strim šifru iz blok šifre, obično je veoma teško izgraditi neku vrstu konstrukta sa blok modom enkripcije (kao što je CBC mod) iz primitivne strim šifre.


Iz ove diskusije, sada bi trebalo da razumete *Slika 8*. Ona pruža pregled simetričnih šema šifrovanja. Koristimo tri vrste šema šifrovanja: primitivne strujne šifre, blok šifre u strujnom režimu, i blok šifre u blok režimu (takođe nazvane „blok šifre“ na dijagramu).


*Slika 8: Pregled simetričnih šema šifrovanja*


![Figure 8: Overview of symmetric encryption schemes](assets/Figure4-8.webp "Figure 8: Overview of symmetric encryption schemes")



## Kodovi za autentifikaciju poruka

<chapterId>19fa7c00-db59-56a0-9654-5350a137939d</chapterId>


Šifrovanje se bavi tajnošću. Ali kriptografija se takođe bavi širim temama, kao što su integritet poruke, autentičnost i nemogućnost poricanja. Takozvani **kodovi za autentifikaciju poruka** (MACs) su simetrične kriptografske šeme koje podržavaju autentičnost i integritet u komunikacijama.


Zašto je išta, osim tajnosti, potrebno u komunikaciji? Pretpostavimo da Bob šalje Alisi poruku koristeći praktično neprobojnu enkripciju. Svaki napadač koji presretne ovu poruku neće moći da utvrdi bilo kakve značajne uvide u vezi sa sadržajem. Međutim, napadač i dalje ima najmanje dva druga vektora napada na raspolaganju:


1. Mogla bi presresti šifrovani tekst, izmeniti njegov sadržaj i poslati izmenjeni šifrovani tekst Alisi.

2. Ona je mogla potpuno blokirati Bobovu poruku i poslati svoj vlastiti kreirani šifrat.


U oba ova slučaja, napadač možda neće imati nikakve uvide u sadržaj šifrovanih tekstova (1) i (2). Ali i dalje bi mogla prouzrokovati značajnu štetu na ovaj način. Ovde postaju važni kodovi za autentifikaciju poruka.


Kodovi za autentifikaciju poruka su labavo definisani kao simetrične kriptografske šeme sa tri algoritma: algoritam za generisanje ključa, algoritam za generisanje oznake i algoritam za verifikaciju. Siguran MAC osigurava da su oznake **egzistencijalno nekrivotvorive** za bilo kog napadača—odnosno, oni ne mogu uspešno kreirati oznaku na poruci koja se verifikuje, osim ako nemaju privatni ključ.


Bob i Alice mogu se boriti protiv manipulacije određenom porukom koristeći MAC. Pretpostavimo za trenutak da im nije stalo do tajnosti. Oni samo žele osigurati da je poruka koju je primila Alice zaista od Boba i da nije ni na koji način promenjena.


Proces je prikazan na *Figure 9*. Da bi koristili **MAC** (Message Authentication Code), prvo bi generate privatni ključ $K$ koji je deljen između njih dvoje. Bob kreira oznaku $T$ za poruku koristeći privatni ključ $K$. Zatim šalje poruku kao i oznaku poruke Alisi. Ona tada može verifikovati da je Bob zaista napravio oznaku, tako što će provući privatni ključ, poruku i oznaku kroz verifikacioni algoritam.


*Slika 9: Pregled simetričnih šema šifrovanja*


![Figure 9: Overview of symmetric encryption schemes](assets/Figure4-9.webp "Figure 9: Overview of symmetric encryption schemes")


Zbog **egzistencijalne nekrivotvorivosti**, napadač ne može na bilo koji način izmeniti poruku $M$ niti kreirati svoju poruku sa važećom oznakom. Ovo važi čak i ako napadač posmatra oznake mnogih poruka između Boba i Alise koje koriste isti privatni ključ. U najgorem slučaju, napadač bi mogao blokirati Alisu da primi poruku $M$ (problem koji kriptografija ne može Address).


MAC garantuje da je poruku zaista kreirao Bob. Ova autentičnost automatski podrazumeva integritet poruke—odnosno, ako je Bob kreirao neku poruku, onda, ipso facto, ona nije bila izmenjena ni na koji način od strane napadača. Dakle, od sada nadalje, svaka briga za autentifikaciju treba automatski da podrazumeva brigu za integritet.


Iako sam napravio razliku između autentičnosti i integriteta poruke u svojoj diskusiji, takođe je uobičajeno koristiti te termine kao sinonime. Oni se, dakle, odnose na ideju poruka koje su kreirane od strane određenog pošiljaoca i nisu ni na koji način izmenjene. U tom duhu, kodovi za autentifikaciju poruka se često nazivaju i **kodovi za integritet poruka**.



## Autentifikovano šifrovanje

<chapterId>33f2ec9b-9fb4-5c61-8fb4-50836270a144</chapterId>


Tipično, želite da garantujete i tajnost i autentičnost u komunikaciji i, stoga, šeme šifrovanja i MAC šeme se obično koriste zajedno.


Šema **autentifikovanog šifrovanja** je šema koja kombinuje šifrovanje sa MAC-om na veoma siguran način. Konkretno, mora da ispunjava standarde za egzistencijalnu nekrivotvorivost, kao i veoma snažan pojam tajnosti, odnosno onaj koji je otporan na **napade odabirom šifro-teksta**. [7]


Da bi šema šifrovanja bila otporna na napade sa izabranim šifratom, mora ispunjavati standarde za **nepromenljivost**: to jest, svaka modifikacija šifrata od strane napadača treba da rezultira ili nevažećim šifratom ili šifratom koji se dešifruje u otvoreni tekst koji nema veze sa originalnim. [8]


Kao što šema za autentifikovano šifrovanje osigurava da je šifrovani tekst koji je kreirao napadač uvek nevažeći (jer oznaka neće biti verifikovana), ona ispunjava standarde za otpornost na napade sa izabranim šifrovanim tekstom. Zanimljivo je da možete dokazati da se šema za autentifikovano šifrovanje uvek može kreirati kombinacijom egzistencijalno nekrivotvorivog MAC-a i šeme šifrovanja koja ispunjava manje jači pojam sigurnosti, poznat kao **sigurnost protiv napada sa izabranim otvorenim tekstom**.


Nećemo ulaziti u sve detalje konstruisanja šema za autentifikovano šifrovanje. Ali je važno znati dva detalja njihove konstrukcije.


Prvo, šema autentifikovanog šifrovanja prvo obrađuje šifrovanje, a zatim kreira oznaku poruke na šifrovanom tekstu. Ispostavlja se da su drugi pristupi—kao što je kombinovanje šifrovanog teksta sa oznakom na otvorenom tekstu, ili prvo kreiranje oznake, a zatim šifrovanje i otvorenog teksta i oznake—nesigurni. Pored toga, obe operacije imaju svoj nasumično odabrani privatni ključ, inače je vaša sigurnost ozbiljno ugrožena.


Navedeni princip se primenjuje opštije: *uvek treba da koristite različite ključeve kada kombinujete osnovne kriptografske šeme*.


Šema autentifikovane enkripcije je prikazana na *Slici 10*. Bob prvo kreira šifrat $C$ iz poruke $M$ koristeći nasumično odabrani ključ $K_C$. Zatim kreira oznaku poruke $T$ tako što pokreće šifrat i drugačiji nasumično odabrani ključ $K_T$ kroz algoritam za generisanje oznake. I šifrat i oznaka poruke se šalju Alisi.


Alisa sada prvo proverava da li je oznaka važeća s obzirom na šifrat $C$ i ključ $K_T$. Ako je važeća, može dešifrovati poruku koristeći ključ $K_C$. Ne samo da je uverena u veoma jak pojam tajnosti u njihovoj komunikaciji, već takođe zna da je poruku kreirao Bob.


*Slika 10: Šema autentifikovanog šifrovanja*


![Figure 10: An authenticated encryption scheme](assets/Figure4-10.webp "Figure 10: An authenticated encryption scheme")


Kako se kreiraju MAC-ovi? Iako se MAC-ovi mogu kreirati na više načina, uobičajen i efikasan način za njihovo kreiranje je putem **kriptografskih Hash funkcija**.


Kriptografske funkcije Hash ćemo detaljnije predstaviti u *Poglavlju 6*. Za sada, samo znajte da je **Hash funkcija** funkcija koja se može efikasno izračunati, prima ulaze proizvoljne veličine i daje izlaze fiksne dužine. Na primer, popularna Hash funkcija **SHA-256** (sigurni Hash algoritam 256) uvek generiše izlaz od 256 bita bez obzira na veličinu ulaza. Neke Hash funkcije, kao što je SHA-256, imaju korisne primene u kriptografiji.


Najčešći tip oznake proizveden kriptografskom funkcijom Hash je **Hash zasnovan kod za autentifikaciju poruka** (HMAC). Proces je prikazan na *Slici 11*. Strana proizvodi dva različita ključa iz privatnog ključa $K$, unutrašnji ključ $K_1$ i spoljašnji ključ $K_2$. Otvoreni tekst $M$ ili šifrovani tekst $C$ se zatim hešira zajedno sa unutrašnjim ključem. Rezultat $T'$ se zatim hešira sa spoljašnjim ključem kako bi se proizvela oznaka poruke $T$.


Postoji paleta Hash funkcija koje se mogu koristiti za kreiranje HMAC-a. Najčešće korišćena Hash funkcija je SHA-256.



*Slika 11: HMAC*


![Figure 11: HMAC](assets/Figure4-11.webp "Figure 11: HMAC")


**Beleške:**


[7] Specifični rezultati diskutovani u ovom delu su iz Katz i Lindell, str. 131–47.


[8] Tehnički, definicija napada odabranim šifrovanim tekstom je drugačija od pojma nepromenljivosti. Ali možete pokazati da su ta dva pojma sigurnosti ekvivalentna.




## Sigurne komunikacione sesije

<chapterId>c7f7dcd3-bbed-53ed-a43d-039da0f180c5</chapterId>


Pretpostavimo da dve strane učestvuju u komunikacionoj sesiji, tako da šalju više poruka napred-nazad.


Šema autentifikovane enkripcije omogućava primaocu poruke da verifikuje da ju je kreirao njen partner u komunikacionoj sesiji (pod uslovom da privatni ključ nije procureo). Ovo funkcioniše dovoljno dobro za jednu poruku. Međutim, obično dve strane šalju poruke napred-nazad u komunikacionoj sesiji. U tom kontekstu, obična šema autentifikovane enkripcije, kao što je opisana u prethodnom odeljku, nije dovoljna za obezbeđivanje sigurnosti.


Glavni razlog je taj što šema autentifikovane enkripcije ne pruža nikakve garancije da je poruku zaista poslao agent koji ju je kreirao unutar komunikacione sesije. Razmotrite sledeća tri vektora napada:


1. **Napad ponovnim puštanjem (Replay attack)**: Napadač ponovo šalje šifrat i oznaku koje je presrela između dve strane u ranijem trenutku.

2. **Napad preuređivanjem**: Napadač presreće dve poruke u različito vreme i šalje ih primaocu obrnutim redosledom.

3. **Napad refleksije**: Napadač posmatra poruku poslatu od A ka B, i takođe šalje tu poruku ka A.


Iako napadač nema saznanja o šifrovanom tekstu i ne može kreirati lažne šifrovane tekstove, gore navedeni napadi i dalje mogu izazvati značajnu štetu u komunikacijama.


Pretpostavimo, na primer, da određena poruka između dve strane uključuje transfer finansijskih sredstava. Napad ponovnim puštanjem mogao bi preneti sredstva drugi put. Obična šema autentifikovanog šifrovanja nema odbranu protiv takvih napada.


Srećom, ove vrste napada mogu se lako ublažiti u komunikacionoj sesiji koristeći **identifikatore** i **indikatore relativnog vremena**.


Identifikatori se mogu dodati u običnu tekstualnu poruku pre enkripcije. Ovo bi sprečilo bilo kakve refleksione napade. Relativni vremenski indikator može, na primer, biti redni broj u određenoj komunikacionoj sesiji. Svaka strana dodaje redni broj poruci pre enkripcije, tako da primalac zna kojim redosledom su poruke poslate. Ovo eliminiše mogućnost napada preuređivanjem. Takođe eliminiše napade ponavljanjem. Bilo koja poruka koju napadač pošalje niz liniju imaće stari redni broj, i primalac će znati da ne procesuira poruku ponovo.


Da ilustrujemo kako funkcionišu sesije sigurne komunikacije, pretpostavimo opet Alisu i Boba. Oni šalju ukupno četiri poruke napred-nazad. Možete videti kako bi šema autentifikovane enkripcije sa identifikatorima i rednim brojevima funkcionisala ispod u *Figure 11*.


Sesija komunikacije počinje tako što Bob šalje šifrat $C_{0,B}$ Alisi sa oznakom poruke $T_{0,B}$. Šifrat sadrži poruku, kao i identifikator (BOB) i redni broj (0). Oznaka $T_{0,B}$ je napravljena preko celog šifrata. U njihovim narednim komunikacijama, Alisa i Bob održavaju ovaj protokol, ažurirajući polja po potrebi.



*Slika 12: Sigurna komunikaciona sesija*


![Figure 12: A secure communication session](assets/Figure4-12.webp "Figure 12: A secure communication sessesion")







# RC4 i AES

<partId>a48c4a7d-0a41-523f-a4ab-1305b4430324</partId>





## RC4 strim šifra

<chapterId>5caec5bd-5a77-56c9-b5e6-1e86f0d294aa</chapterId>


U ovom poglavlju ćemo diskutovati o detaljima šeme enkripcije sa modernim primitivnim strim šifrom, RC4 (ili "Rivest šifra 4"), i modernom blok šifrom, AES. Iako je RC4 šifra pala u nemilost kao metoda enkripcije, AES je standard za modernu simetričnu enkripciju. Ova dva primera bi trebalo da pruže bolju ideju o tome kako simetrična enkripcija funkcioniše ispod haube.


___


Kako bismo stekli uvid u to kako moderni pseudonasumični strim šifri rade, fokusiraću se na RC4 strim šifru. To je pseudonasumična strim šifra koja je korišćena u WEP i WAP sigurnosnim protokolima za bežične pristupne tačke, kao i u TLS-u. Kako RC4 ima mnogo dokazanih slabosti, pao je u nemilost. Zapravo, Internet Engineering Task Force sada zabranjuje upotrebu RC4 paketa od strane klijentskih i serverskih aplikacija u svim instancama TLS-a. Ipak, dobro funkcioniše kao primer za ilustrovanje kako primitivna strim šifra radi.


Da počnemo, prvo ću pokazati kako da šifrujemo običnu tekstualnu poruku pomoću baby RC4 šifre. Pretpostavimo da je naša obična tekstualna poruka "SOUP." Šifrovanje sa našom baby RC4 šifrom, zatim, odvija se u četiri koraka.


### Korak 1


Prvo, definiši niz **S** sa $S[0] = 0$ do $S[7] = 7$. Niz ovde jednostavno znači promenljivu kolekciju vrednosti organizovanih po indeksu, takođe nazvanu lista u nekim programskim jezicima (npr. Python). U ovom slučaju, indeks ide od 0 do 7, a vrednosti takođe idu od 0 do 7. Dakle, **S** je sledeći:



- $S = [0, 1, 2, 3, 4, 5, 6, 7]$


Vrednosti ovde nisu ASCII brojevi, već decimalne vrednosti predstavljene kao 1-bajtni nizovi. Dakle, vrednost 2 bi bila jednaka $0000 \ 0011$. Dužina niza **S** je, dakle, 8 bajtova.


### Korak 2


Drugo, definišite ključni niz **K** dužine 8 bajtova tako što ćete izabrati ključ između 1 i 8 bajtova (bez dozvoljenih delova bajta). Pošto svaki bajt ima 8 bita, možete izabrati bilo koji broj između 0 i 255 za svaki bajt vašeg ključa.


Pretpostavimo da izaberemo naš ključ **k** kao $[14, 48, 9]$, tako da ima dužinu od 3 bajta. Svaki indeks našeg niza ključeva je, zatim, postavljen prema decimalnoj vrednosti za taj određeni element ključa, redom. Ako prođete kroz ceo ključ, počnite ponovo od početka, dok ne popunite svih 8 slotova niza ključeva. Dakle, naš niz ključeva je sledeći:



- $K = [14, 48, 9, 14, 48, 9, 14, 48]$


### Korak 3


Treće, transformisaćemo niz **S** koristeći ključni niz **K**, u procesu poznatom kao **planiranje ključa**. Proces je sledeći u pseudokodu:



- Kreiraj promenljive **j** i **i**
- Postavite promenljivu $j = 0$
- Za svaki $i$ od 0 do 7:
    - Postavi $j = (j + S[i] + K[i]) \mod 8$
    - Zameni $S[i]$ i $S[j]$


Transformacija niza **S** je prikazana u *Tabeli 1*.


Da počnemo, možete videti početno stanje **S** kao $[0, 1, 2, 3, 4, 5, 6, 7]$ sa početnom vrednošću 0 za **j**. Ovo će biti transformisano koristeći ključni niz $[14, 48, 9, 14, 48, 9, 14, 48]$.


The for loop starts with $i = 0$. According to our pseudocode above, the new value of **j** becomes 6 ($j = (j + S[0] + K[0]) \mod 8 = (0 + 0 + 14) \mod 8 = 6 \mod 8$). Swapping $S[0]$ and $S[6]$, the state of **S** after 1 round becomes $[6, 1, 2, 3, 4, 5, 0, 7]$.


U sledećem redu, $i = 1$. Prolazeći ponovo kroz for petlju, **j** dobija vrednost 7 ($j = (j + S[1] + K[1]) \mod 8 = (6 + 1 + 48) \mod 8 = 55 \mod 8 = 7 \mod 8$). Zamenom $S[1]$ i $S[7]$ iz trenutnog stanja **S**, $[6, 1, 2, 3, 4, 5, 0, 7]$, dobija se $[6, 7, 2, 3, 4, 5, 0, 1]$ nakon 2. runde.


Nastavljamo s ovim procesom sve dok ne proizvedemo poslednji red na dnu za niz **S**, $[6, 4, 1, 0, 3, 7, 5, 2]$.



*Tabela 1: Ključna tabela rasporeda*


| Round   | i   | j   |     | S[0] | S[1] | S[2] | S[3] | S[4] | S[5] | S[6] | S[7] |
| ------- | --- | --- | --- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
|         |     |     |     |      |      |      |      |      |      |      |      |
| Initial |     | 0   |     | 0    | 1    | 2    | 3    | 4    | 5    | 6    | 7    |
| 1       | 0   | 6   |     | 6    | 1    | 2    | 3    | 4    | 5    | 0    | 7    |
| 2       | 1   | 7   |     | 6    | 7    | 2    | 3    | 4    | 5    | 0    | 1    |
| 3       | 2   | 2   |     | 6    | 7    | 2    | 3    | 4    | 5    | 0    | 1    |
| 4       | 3   | 3   |     | 6    | 7    | 2    | 3    | 4    | 5    | 0    | 1    |
| 5       | 4   | 3   |     | 6    | 7    | 2    | 0    | 3    | 5    | 4    | 1    |
| 6       | 5   | 6   |     | 6    | 4    | 2    | 0    | 3    | 7    | 5    | 1    |
| 7       | 6   | 1   |     | 6    | 4    | 2    | 0    | 3    | 7    | 5    | 2    |
| 8       | 7   | 2   |     | 6    | 4    | 1    | 0    | 3    | 7    | 5    | 2    |

### Korak 4


Kao četvrti korak, proizvodimo **keystream**. Ovo je pseudonasumični niz dužine jednake poruci koju želimo poslati. Ovo će se koristiti za šifrovanje originalne poruke "SOUP." Pošto keystream treba da bude dug koliko i poruka, potreban nam je onaj koji ima 4 bajta.


Keystream se proizvodi sledećim pseudokodom:



- Kreiraj promenljive **j**, **i**, i **t**.
- Postavi $j = 0$.
- Za svaki $i$ otvorenog teksta, počevši od $i = 1$ i idući do $i = 4$, svaki bajt toka ključeva se proizvodi na sledeći način:
    - $j = (j + S[i]) \mod 8$
    - Zameni $S[i]$ i $S[j]$.
    - $t = (S[i] + S[j]) \mod 8$
    - $i^{ti}$ bajt keystream-a = $S[t]$


Možete pratiti proračune u *Tabeli 2*.


Početno stanje **S** je $S = [6, 4, 1, 0, 3, 7, 5, 2]$. Postavljanjem $i = 1$, vrednost **j** postaje 4 ($j = (j + S[i]) \mod 8 = (0 + 4) \mod 8 = 4$). Zatim menjamo mesta $S[1]$ i $S[4]$ da bismo dobili transformaciju **S** u drugom redu, $[6, 3, 1, 0, 4, 7, 5, 2]$. Vrednost **t** je tada 7 ($t = (S[i] + S[j]) \mod 8 = (3 + 4) \mod 8 = 7$). Na kraju, bajt za keystream je $S[7]$, ili 2.


Zatim nastavljamo da proizvodimo ostale bajtove dok ne dobijemo sledeća četiri bajta: 2, 6, 3 i 7. Svaki od ovih bajtova se zatim može koristiti za šifrovanje svakog slova otvorenog teksta, "SOUP".


Da bismo počeli, koristeći ASCII tabelu, možemo videti da je “SOUP” kodiran decimalnim vrednostima osnovnih bajt nizova kao “83 79 85 80”. Kombinacija sa keystream-om “2 6 3 7” daje “85 85 88 87”, što ostaje isto nakon operacije modulo 256. U ASCII, šifrovani tekst “85 85 88 87” odgovara “UUXW”.


Šta se dešava ako je reč za šifrovanje duža od niza **S**? U tom slučaju, niz **S** se samo nastavlja transformisati na način prikazan gore za svaki bajt **i** otvorenog teksta, sve dok ne dobijemo broj bajtova u keystream-u jednak broju slova u otvorenom tekstu.



*Tabela 2: Generisanje keystream-a*


| i   | j   | t   | Keystream | S[0] | S[1] | S[2] | S[3] | S[4] | S[5] | S[6] | S[7] |
| --- | --- | --- | --------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
|     |     |     |           |      |      |      |      |      |      |      |      |
|     | 0   |     |           | 6    | 4    | 1    | 0    | 3    | 7    | 5    | 2    |
| 1   | 4   | 7   | 2         | 6    | 3    | 1    | 0    | 4    | 7    | 5    | 2    |
| 2   | 5   | 0   | 6         | 6    | 3    | 7    | 0    | 4    | 1    | 5    | 2    |
| 3   | 5   | 1   | 3         | 6    | 3    | 7    | 1    | 4    | 0    | 5    | 2    |
| 4   | 1   | 7   | 2         | 6    | 4    | 7    | 1    | 3    | 0    | 5    | 2    |

Primer koji smo upravo diskutovali je samo razblažena verzija **RC4 strim šifre**. Prava RC4 strim šifra ima **S** niz dužine 256 bajtova, a ne 8 bajtova, i ključ koji može biti između 1 i 256 bajtova, a ne između 1 i 8 bajtova. Niz ključeva i strimovi ključeva se zatim proizvode uzimajući u obzir dužinu od 256 bajtova **S** niza. Izračuni postaju izuzetno složeniji, ali principi ostaju isti. Koristeći isti ključ, [14,48,9], sa standardnom RC4 šifrom, otvorena poruka "SOUP" je enkriptovana kao 67 02 ed df u heksadecimalnom formatu.


Šifarnik toka u kojem se tok ključeva ažurira nezavisno od otvorenog teksta ili šifrovanog teksta je **sinhroni šifarnik toka**. Tok ključeva zavisi samo od ključa. Jasno je da je RC4 primer sinhronog šifarnika toka, jer tok ključeva nema veze sa otvorenim tekstom ili šifrovanim tekstom. Svi naši primitivni šifarnici toka pomenuti u prethodnom poglavlju, uključujući šifru pomaka, Vigenèreovu šifru i jednokratnu podlogu, takođe su bili sinhronog tipa.


Nasuprot tome, **asinhroni strim šifra** ima keystream koji se proizvodi i pomoću ključa i prethodnog Elements šifrovanog teksta. Ova vrsta šifre se takođe naziva **samosinhronizujuća šifra**.


Važno je da se keystream proizveden sa RC4 tretira kao jednokratna šifra, i ne možete proizvesti keystream na potpuno isti način sledeći put. Umesto menjanja ključa svaki put, praktično rešenje je kombinovati ključ sa **Nonce** da bi se proizveo bytestream.




## AES sa 128-bitnim ključem

<chapterId>0b30886f-e620-5b8d-807b-9d84685ca8ff</chapterId>


Kao što je pomenuto u prethodnom poglavlju, Nacionalni institut za standarde i tehnologiju (NIST) održao je takmičenje između 1997. i 2000. godine kako bi odredio novi standard za simetrično šifrovanje. **Rijndael šifra** se pokazala kao pobednički unos. Ime je igra reči na osnovu imena belgijskih tvoraca, Vincent Rijmen i Joan Daemen.


Rijndael šifra je **blok šifra**, što znači da postoji osnovni algoritam koji se može koristiti sa različitim specifikacijama za dužine ključeva i veličine blokova. Možete je, zatim, koristiti sa različitim režimima rada za konstruisanje šema šifrovanja.


Komitet za NIST takmičenje usvojio je ograničenu verziju Rijndael šifre—naime onu koja zahteva veličine blokova od 128 bita i dužine ključeva od 128 bita, 192 bita ili 256 bita—kao deo **Naprednog standarda za šifrovanje (AES)**. Ova ograničena verzija Rijndael šifre može se koristiti i u više režima rada. Specifikacija za standard je ono što je poznato kao **Napredni standard za šifrovanje (AES)**.


Da bih pokazao kako funkcioniše Rijndael šifra, jezgro AES-a, ilustrovaću proces enkripcije sa 128-bitnim ključem. Veličina ključa utiče na broj rundi koje se sprovode za svaki blok enkripcije. Za 128-bitne ključeve, potrebno je 10 rundi. Sa 192 bita i 256 bita, bilo bi potrebno 12 i 14 rundi, respektivno.


Pored toga, pretpostaviću da se AES koristi u **ECB-modu**. Ovo čini izlaganje malo lakšim i nije važno za Rijndael algoritam. Da budemo sigurni, ECB mod nije bezbedan u praksi jer dovodi do determinističkog šifrovanja. Najčešće korišćeni bezbedni mod sa AES-om je **CBC** (Cipher Block Chaining).


Hajde da nazovemo ključ $K_0$. Konstrukcija sa gore navedenim parametrima, zatim, izgleda kao na *Slici 1*, gde $M_i$ označava deo otvorenog teksta od 128 bita, a $C_i$ deo šifrovanog teksta od 128 bita. Dodaje se popunjavanje otvorenom tekstu za poslednji blok, ako otvoreni tekst ne može biti ravnomerno podeljen veličinom bloka.



*Slika 1: AES-ECB sa 128-bitnim ključem*


![Figure 1: AES-ECB with a 128-bit key](assets/Figure5-1.webp "Figure 1: AES-ECB with a 128-bit key")


Svaki 128-bitni blok teksta prolazi kroz deset rundi u Rijndael šemi šifrovanja. Ovo zahteva poseban ključ za svaku rundu ($K_1$ do $K_{10}$). Oni se proizvode za svaku rundu iz originalnog 128-bitnog ključa $K_0$ koristeći **algoritam za proširenje ključa**. Dakle, za svaki blok teksta koji treba da bude šifrovan, koristićemo originalni ključ $K_0$ kao i deset posebnih ključeva za runde. Imajte na umu da se ovih istih 11 ključeva koristi za svaki 128-bitni blok otvorenog teksta koji zahteva šifrovanje.


Algoritam za proširenje ključa je dug i složen. Rad na njemu ima malo didaktičke koristi. Možete sami pregledati algoritam za proširenje ključa, ako želite. Kada se proizvedu ključevi rundi, Rijndael šifra će manipulisati prvim 128-bitnim blokom otvorenog teksta, $M_1$, kao što je prikazano na *Slici 2*. Sada ćemo proći kroz ove korake.


*Slika 2: Manipulacija $M_1$ sa Rijndael šifrom:*


**Runda 0:**


- XOR $M_1$ i $K_0$ da bi se dobio $S_0$


---

**Runda n za n = {1,...,9}:**


- XOR $S_{n-1}$ i $K_n$
- Zamena bajtova
- Shift Rows
- Mešaj Kolone
- XOR $S$ i $K_n$ da bi se proizveo $S_n$


---

**Runda 10:**


- XOR $S_9$ i $K_{10}$
- Zamena bajtova
- Pomeraj Redove
- XOR $S$ i $K_{10}$ da bi se proizveo $S_{10}$
- $S_{10}$ = $C_1$



### Runda 0


Runda 0 Rijndael šifre je jednostavna. Niz $S_0$ se proizvodi XOR operacijom između 128-bitnog otvorenog teksta i privatnog ključa. To jest,



- $S_0 = M_1 \oplus K_0$


### Runda 1


U rundi 1, niz $S_0$ se prvo kombinuje sa rundskim ključem $K_1$ koristeći XOR operaciju. Ovo proizvodi novo stanje $S$.


Drugo, operacija **zamene bajtova** se izvodi na trenutnom stanju $S$. Ona funkcioniše tako što uzima svaki bajt iz 16-bajtne $S$ niske i zamenjuje ga bajtom iz niske koja se zove **Rijndaelova S-kutija**. Svaki bajt ima jedinstvenu transformaciju, i kao rezultat se proizvodi novo stanje $S$. Rijndaelova S-kutija je prikazana na *Slici 3*.


*Slika 3: Rijndaelova S-Kutija*


|     | 00  | 01  | 02  | 03  | 04  | 05  | 06  | 07  | 08  | 09  | 0A  | 0B  | 0C  | 0D  | 0E  | 0F  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 00  | 63  | 7C  | 77  | 7B  | F2  | 6B  | 6F  | C5  | 30  | 01  | 67  | 2B  | FE  | D7  | AB  | 76  |
| 10  | CA  | 82  | C9  | 7D  | FA  | 59  | 47  | F0  | AD  | D4  | A2  | AF  | 9C  | A4  | 72  | C0  |
| 20  | B7  | FD  | 93  | 26  | 36  | 3F  | F7  | CC  | 34  | A5  | E5  | F1  | 71  | D8  | 31  | 15  |
| 30  | 04  | C7  | 23  | C3  | 18  | 96  | 05  | 9A  | 07  | 12  | 80  | E2  | EB  | 27  | B2  | 75  |
| 40  | 09  | 83  | 2C  | 1A  | 1B  | 6E  | 5A  | A0  | 52  | 3B  | D6  | B3  | 29  | E3  | 2F  | 84  |
| 50  | 53  | D1  | 00  | ED  | 20  | FC  | B1  | 5B  | 6A  | CB  | BE  | 39  | 4A  | 4C  | 58  | CF  |
| 60  | D0  | EF  | AA  | FB  | 43  | 4D  | 33  | 85  | 45  | F9  | 02  | 7F  | 50  | 3C  | 9F  | A8  |
| 70  | 51  | A3  | 40  | 8F  | 92  | 9D  | 38  | F5  | BC  | B6  | DA  | 21  | 10  | FF  | F3  | D2  |
| 80  | CD  | 0C  | 13  | EC  | 5F  | 97  | 44  | 17  | C4  | A7  | 7E  | 3D  | 64  | 5D  | 19  | 73  |
| 90  | 60  | 81  | 4F  | DC  | 22  | 2A  | 90  | 88  | 46  | EE  | B8  | 14  | DE  | 5E  | 0B  | DB  |
| A0  | E0  | 32  | 3A  | 0A  | 49  | 06  | 24  | 5C  | C2  | D3  | AC  | 62  | 91  | 95  | E4  | 79  |
| B0  | E7  | C8  | 37  | 6D  | 8D  | D5  | 4E  | A9  | 6C  | 56  | F4  | EA  | 65  | 7A  | AE  | 08  |
| C0  | BA  | 78  | 25  | 2E  | 1C  | A6  | B4  | C6  | E8  | DD  | 74  | 1F  | 4B  | BD  | 8B  | 8A  |
| D0  | 70  | 3E  | B5  | 66  | 48  | 03  | F6  | 0E  | 61  | 35  | 57  | B9  | 86  | C1  | 1D  | 9E  |
| E0  | E1  | F8  | 98  | 11  | 69  | D9  | 8E  | 94  | 9B  | 1E  | 87  | E9  | CE  | 55  | 28  | DF  |
| F0  | 8C  | A1  | 89  | 0D  | BF  | E6  | 42  | 68  | 41  | 99  | 2D  | 0F  | B0  | 54  | BB  | 16  |


Ovaj S-Box je jedno mesto gde apstraktna algebra dolazi do izražaja u Rijndael šifri, konkretno **Galoisova polja**.


Da biste započeli, definišete svaki mogući bajt element od 00 do FF kao 8-bitni vektor. Svaki takav vektor je element **Galoisovog polja GF(2^8)** gde je ireducibilni polinom za operaciju modula $x^8 + x^4 + x^3 + x + 1$. Galoisovo polje sa ovim specifikacijama se takođe naziva **Rijndaelovo konačno polje**.


Zatim, za svaki mogući element u polju, kreiramo ono što se zove **Nyberg S-Box**. U ovoj kutiji, svaki bajt se preslikava na svoj **multiplikativni inverz** (tj. tako da njihov proizvod bude jednak 1). Zatim te vrednosti iz Nyberg S-kutije preslikavamo u Rijndaelovu S-kutiju koristeći **afinu transformaciju**.


Treća operacija na nizu **S** je operacija **shift rows**. Ona uzima stanje **S** i prikazuje svih šesnaest bajtova u matrici. Popunjavanje matrice počinje u gornjem levom uglu i nastavlja se tako što ide od vrha ka dnu, a zatim, svaki put kada se kolona popuni, pomera se jedna kolona udesno i na vrh.


Kada je matrica **S** konstruisana, četiri reda se pomeraju. Prvi red ostaje isti. Drugi red se pomera za jedno mesto ulevo. Treći se pomera za dva mesta ulevo. Četvrti se pomera za tri mesta ulevo. Primer procesa je prikazan na *Slici 4*. Originalno stanje **S** je prikazano na vrhu, a rezultat stanja nakon operacije pomeranja redova je prikazan ispod njega.


*Slika 4: Operacija pomeranja redova*


| F1   | A0   | B1   | 23   |
|------|------|------|------|
| 59   | EF   | 09   | 82   |
| 97   | 01   | B0   | CC   |
| D4   | 72   | 04   | 21   |
| F1   | A0   | B1   | 23   |
|------|------|------|------|
| EF   | 09   | 82   | 59   |
| B0   | CC   | 97   | 01   |
| 21   | D4   | 72   | 04   |


U četvrtom koraku, **Galoisova polja** se ponovo pojavljuju. Za početak, svaka kolona **S** matrice se množi sa kolonom 4 x 4 matrice prikazane na *Slici 5*. Ali umesto običnog množenja matrica, to je množenje vektora **modulo ireducibilni polinom**, $x^8 + x^4 + x^3 + x + 1$. Koeficijenti rezultujućeg vektora predstavljaju pojedinačne bitove bajta.


*Slika 5: Matrica mešanja kolona*


| 02   | 03   | 01   | 01   |
|------|------|------|------|
| 01   | 02   | 03   | 01   |
| 01   | 01   | 02   | 03   |
| 03   | 01   | 01   | 02   |

Množenje prve kolone matrice **S** sa 4 x 4 matricom iznad daje rezultat u *Slici 6*.


*Slika 6: Množenje prve kolone:*


$$
\begin{matrix}
02 \cdot F1 + 03 \cdot EF + 01 \cdot B0 + 01 \cdot 21 \\
01 \cdot F1 + 02 \cdot EF + 03 \cdot B0 + 01 \cdot 21 \\
01 \cdot F1 + 01 \cdot EF + 02 \cdot B0 + 03 \cdot 21 \\
03 \cdot F1 + 01 \cdot EF + 01 \cdot B0 + 02 \cdot 21
\end{matrix}
$$


Kao sledeći korak, svi termini u matrici bi morali biti pretvoreni u polinome. Na primer, F1 predstavlja 1 bajt i postao bi $x^7 + x^6 + x^5 + x^4 + 1$, a 03 predstavlja 1 bajt i postao bi $x + 1$.


Sve množenje se zatim izvodi **modulo** $x^8 + x^4 + x^3 + x + 1$. Ovo rezultira sabiranjem četiri polinoma u svakoj od četiri ćelije kolone. Nakon izvođenja tih sabiranja **modulo 2**, dobićete četiri polinoma. Svaki od ovih polinoma predstavlja 8-bitni niz, ili 1 bajt, **S**. Nećemo ovde izvoditi sve ove proračune na matrici u *Figure 6* jer su opsežni.


Kada je prva kolona obrađena, ostale tri kolone matrice **S** obrađuju se na isti način. Na kraju, to će dati matricu sa šesnaest bajtova koja se može transformisati u niz.


Kao poslednji korak, niz **S** se ponovo kombinuje sa rund ključem u **XOR** operaciji. Ovo proizvodi stanje $S_1$. To jest,



- $S_1 = S \oplus K_0$


### Runde 2 do 10


Runde 2 do 9 su samo ponavljanje runde 1, *mutatis mutandis*. Završna runda izgleda veoma slično prethodnim rundama, osim što je korak **mešanja kolona** eliminisan. To jest, runda 10 se izvodi na sledeći način:



- $S_9 \oplus K_{10}$
- Zamena bajtova
- Shift Rows
- $S_{10} = S \oplus K_{10}$


Država $S_{10}$ je sada postavljena na $C_1$, prvih 128 bita šifrovanog teksta. Prolazeći kroz preostale blokove otvorenog teksta od 128 bita dobija se kompletan šifrovani tekst **C**.


### Operacije Rijndael šifre


Koje je obrazloženje iza različitih operacija viđenih u Rijndael šifri?


Bez ulaska u detalje, šeme šifrovanja se procenjuju na osnovu stepena u kojem stvaraju konfuziju i difuziju. Ako šema šifrovanja ima visok stepen **konfuzije**, to znači da šifrat izgleda drastično drugačije od otvorenog teksta. Ako šema šifrovanja ima visok stepen **difuzije**, to znači da bilo koja mala promena u otvorenom tekstu proizvodi drastično drugačiji šifrat.


Razlog za operacije iza Rijndael šifre je što one proizvode visok stepen konfuzije i difuzije. Konfuzija se proizvodi operacijom zamene bajtova, dok se difuzija proizvodi operacijama pomeranja redova i mešanja kolona.


# Asimetrična kriptografija

<partId>868bd9dd-6e1c-5ea9-9ece-54affc13ba05</partId>



## Problem distribucije i upravljanja ključevima

<chapterId>1bb651ba-689a-5a89-a7d3-0b9cc3b694f7</chapterId>


Kao i kod simetrične kriptografije, asimetrične šeme mogu se koristiti za obezbeđivanje tajnosti i autentifikacije. Međutim, za razliku od simetričnih, ove šeme koriste dva ključa umesto jednog: privatni i javni ključ.


Počinjemo našu istragu otkrićem asimetrične kriptografije, posebno problema koji su je podstakli. Zatim, raspravljamo o tome kako asimetrične šeme za enkripciju i autentifikaciju funkcionišu na visokom nivou. Potom, uvodimo Hash funkcije, koje su ključne za razumevanje asimetričnih šema autentifikacije, a takođe imaju značaj u drugim kriptografskim kontekstima, kao što su Hash zasnovani kodovi za autentifikaciju poruka koje smo diskutovali u Poglavlju 4.


___



Pretpostavimo da Bob želi da kupi novi kišni mantil od Jim’s Sporting Goods, online prodavnice sportske opreme sa milionima kupaca u Severnoj Americi. Ovo će biti njegova prva kupovina od njih i želi da koristi svoju kreditnu karticu. Dakle, Bob će prvo morati da kreira nalog kod Jim’s Sporting Goods, što zahteva slanje ličnih podataka kao što su njegov Address i informacije o kreditnoj kartici. Zatim može proći kroz potrebne korake za kupovinu kišnog mantila.


Bob i Jim’s Sporting Goods će želeti da osiguraju da njihove komunikacije budu bezbedne tokom ovog procesa, s obzirom na to da je Internet otvoren komunikacioni sistem. Oni će želeti da osiguraju, na primer, da nijedan potencijalni napadač ne može saznati Bobove podatke o kreditnoj kartici i Address, i da nijedan potencijalni napadač ne može ponoviti njegove kupovine ili kreirati lažne u njegovo ime.


Napredna šema autentifikovane enkripcije, kao što je diskutovano u prethodnom poglavlju, svakako bi mogla učiniti komunikaciju između Boba i Jim's Sporting Goods sigurnom. Ali očigledno postoje praktične prepreke za implementaciju takve šeme.


Da bismo ilustrovali ove praktične prepreke, pretpostavimo da živimo u svetu u kojem postoje samo alati simetrične kriptografije. Šta bi tada Jim’s Sporting Goods i Bob mogli da urade kako bi osigurali sigurnu komunikaciju?


U tim okolnostima, suočiće se sa značajnim troškovima za bezbednu komunikaciju. Kako je Internet otvoren komunikacioni sistem, ne mogu jednostavno Exchange skup ključeva preko njega. Stoga će Bob i predstavnik Jim's Sporting Goods morati da naprave ključ Exchange lično.


Jedna mogućnost je da Jim’s Sporting Goods kreira posebne lokacije za ključeve Exchange, gde Bob i drugi novi kupci mogu preuzeti set ključeva za sigurnu komunikaciju. Ovo bi očigledno došlo uz značajne organizacione troškove i znatno smanjilo efikasnost sa kojom novi kupci mogu obavljati kupovine.


Alternativno, Jim’s Sporting Goods može poslati Bobu par ključeva putem visoko pouzdanog kurira. Ovo je verovatno efikasnije nego organizovanje lokacija ključeva Exchange. Ali to bi i dalje dolazilo uz značajne troškove, posebno ako mnogi kupci obave samo jednu ili nekoliko kupovina.


Dalje, simetrična šema za autentifikovano šifrovanje takođe primorava Jim’s Sporting Goods da čuva odvojene skupove ključeva za sve svoje kupce. Ovo bi bio značajan praktičan izazov za hiljade kupaca, a kamoli za milione.


Da biste razumeli ovu poslednju tačku, pretpostavimo da Jim’s Sporting Goods svakom kupcu daje isti par ključeva. To bi omogućilo svakom kupcu—ili bilo kome drugom ko bi mogao da dobije ovaj par ključeva—da čita, pa čak i manipuliše svim komunikacijama između Jim’s Sporting Goods i njegovih kupaca. Možda bi, onda, bilo bolje da uopšte ne koristite kriptografiju u vašim komunikacijama.


Čak i ponavljanje skupa ključeva samo za neke korisnike je užasna sigurnosna praksa. Svaki potencijalni napadač bi mogao pokušati da iskoristi tu karakteristiku šeme (setite se da se pretpostavlja da napadači znaju sve o šemi osim ključeva, u skladu sa Kerckhoffsovim principom.)


Dakle, Jim’s Sporting Goods bi morao da čuva par ključeva za svakog kupca, bez obzira na to kako su ovi parovi ključeva distribuirani. Ovo očigledno predstavlja nekoliko praktičnih problema.



- Jim’s Sporting Goods bi morao da skladišti milione parova ključeva, jedan set za svakog kupca.
- Ovi ključevi bi morali biti propisno osigurani, jer bi bili sigurna meta za hakere. Svako narušavanje sigurnosti zahtevalo bi ponavljanje skupih razmena ključeva, bilo na posebnim lokacijama ključeva Exchange ili putem kurira.
- Bilo koji kupac Jim’s Sporting Goods morao bi bezbedno čuvati par ključeva kod kuće. Gubici i krađe će se dogoditi, što zahteva ponavljanje razmene ključeva. Kupci bi takođe morali proći kroz ovaj proces za bilo koje druge online prodavnice ili druge vrste entiteta sa kojima žele komunicirati i obavljati transakcije putem Interneta.


Ova dva glavna izazova upravo opisana bila su veoma fundamentalna pitanja sve do kasnih 1970-ih. Bila su poznata kao **problem distribucije ključa** i **problem upravljanja ključem**, respektivno.


Ovi problemi su oduvek postojali, naravno, i često su stvarali glavobolje u prošlosti. Vojne snage, na primer, morale su stalno distribuirati knjige sa ključevima za sigurnu komunikaciju osoblju na terenu uz velike rizike i troškove. Ali ovi problemi su postajali sve gori kako je svet sve više prelazio na daljinsku, digitalnu komunikaciju, posebno za nevladine entitete.


Da ovi problemi nisu bili rešeni 1970-ih, efikasna i sigurna kupovina u Jim’s Sporting Goods verovatno ne bi postojala. U stvari, većina našeg modernog sveta sa praktičnim i sigurnim slanjem e-pošte, onlajn bankarstvom i kupovinom verovatno bi bila samo daleka fantazija. Nešto što bi čak i podsećalo na Bitcoin ne bi moglo uopšte da postoji.


Dakle, šta se desilo 1970-ih? Kako je moguće da možemo trenutno obavljati kupovine putem interneta i sigurno pretraživati World Wide Web? Kako je moguće da možemo trenutno slati Bitcoine širom sveta sa naših pametnih telefona?



## Novi pravci u kriptografiji

<chapterId>7a9dd9a3-496e-5f9d-93e0-b5028a7dd0f1</chapterId>


Do 1970-ih, problemi distribucije ključeva i upravljanja ključevima privukli su pažnju grupe američkih akademskih kriptografa: Whitfielda Diffieja, Martina Hellmana i Ralpha Merklea. Suočeni sa ozbiljnim skepticizmom većine svojih kolega, upustili su se u pronalaženje rešenja za to.


Barem jedna primarna motivacija za njihov poduhvat bila je predviđanje da će otvorene računarske komunikacije duboko uticati na naš svet. Kao što su Diffie i Helmann primetili 1976. godine,


> Razvoj računarski kontrolisanih komunikacionih mreža obećava lak i jeftin kontakt između ljudi ili računara na suprotnim stranama sveta, zamenjujući većinu pošte i mnoge izlete telekomunikacijama. Za mnoge primene ovi kontakti moraju biti osigurani protiv prisluškivanja i ubacivanja nelegitimnih poruka. Međutim, trenutno rešenje problema bezbednosti zaostaje za drugim oblastima komunikacione tehnologije. *Suvremena kriptografija nije u stanju da ispuni zahteve, jer bi njena upotreba nametnula tako ozbiljne neugodnosti korisnicima sistema, da bi eliminisala mnoge prednosti teleprocesiranja.* [1]

Upornost Diffieja, Hellmana i Merklea se isplatila. Prva objava njihovih rezultata bila je rad Diffieja i Helmana iz 1976. godine pod nazivom „New Directions in Cryptography.” U njemu su predstavili dva originalna načina za Address probleme distribucije ključeva i upravljanja ključevima.


Prvo rešenje koje su ponudili bilo je daljinsko *key-Exchange protokol*, odnosno skup pravila za Exchange jednog ili više simetričnih ključeva preko nesigurnog komunikacionog kanala. Ovaj protokol je sada poznat kao *Diffie-Helmann key Exchange* ili *Diffie-Helmann-Merkle key Exchange*. [2]


Sa Diffie-Helmann ključem Exchange, dve strane prvo Exchange neke informacije javno na nesigurnom kanalu kao što je Internet. Na osnovu tih informacija, zatim, nezavisno kreiraju simetrični ključ (ili par simetričnih ključeva) za sigurnu komunikaciju. Iako obe strane nezavisno kreiraju svoje ključeve, informacije koje su podelili javno osiguravaju da ovaj proces kreiranja ključa daje isti rezultat za obe strane.


Važno je napomenuti da, iako svako može posmatrati informacije koje strane razmenjuju javno preko nesigurnog kanala, samo dve strane koje učestvuju u informacijama Exchange mogu kreirati simetrične ključeve iz njih.


Ovo, naravno, zvuči potpuno kontraintuitivno. Kako bi dve strane Exchange mogle javno da podele informacije koje bi im omogućile da samo one kreiraju simetrične ključeve iz njih? Zašto niko drugi ko posmatra informacije Exchange ne bi mogao da kreira iste ključeve?


Oslanja se naravno na neku lepu matematiku. Diffie-Helmann ključ Exchange radi putem jednosmerne funkcije sa skrivenim prolazom. Hajde da redom diskutujemo značenje ova dva termina.


Pretpostavimo da vam je data neka funkcija $f(x)$ i rezultat $f(a) = y$, gde je $a$ određena vrednost za $x$. Kažemo da je $f(x)$ **jednosmerna funkcija** ako je lako izračunati vrednost $y$ kada su dati $a$ i $f(x)$, ali je računarski neizvodljivo izračunati vrednost $a$ kada su dati $y$ i $f(x)$. Naziv **jednosmerna funkcija**, naravno, potiče iz činjenice da je takvu funkciju praktično izračunati samo u jednom smeru.


Neke jednosmerne funkcije imaju ono što je poznato kao **trapdoor**. Dok je praktično nemoguće izračunati $a$ samo na osnovu $y$ i $f(x)$, postoji određeni deo informacije $Z$ koji omogućava da se izračuna $a$ iz $y$ na računarski izvodljiv način. Ovaj deo informacije $Z$ je poznat kao **trapdoor**. Jednosmerne funkcije koje imaju trapdoor poznate su kao **trapdoor funkcije**.


Nećemo ulaziti u detalje Diffie-Helmann ključa Exchange ovde. Ali u suštini, svaki učesnik kreira neke informacije, od kojih je jedan deo javno podeljen, dok neki ostaju tajni. Svaka strana zatim uzima svoj tajni deo informacija i javne informacije koje je podelila druga strana kako bi kreirala privatni ključ. I na neki način, oba učesnika će završiti sa istim privatnim ključem.


Bilo koja strana koja posmatra samo javno deljene informacije između dve strane u Diffie Helmann ključu Exchange nije u mogućnosti da replicira ove proračune. Potrebne su im privatne informacije od jedne od dve strane da bi to uradili.


Iako osnovna verzija Diffie-Helmann ključa Exchange predstavljena u radu iz 1976. godine nije veoma sigurna, sofisticirane verzije osnovnog protokola su svakako i dalje u upotrebi danas. Najvažnije je da je svaki ključ Exchange protokola u najnovijoj verziji transportnog Layer sigurnosnog protokola (verzija 1.3) suštinski obogaćena verzija protokola koju su predstavili Diffie i Hellman 1976. godine. Transportni Layer sigurnosni protokol je preovlađujući protokol za sigurno razmenjivanje informacija formatiranih prema hipertekstualnom transfer protokolu (http), standardu za razmenu Web sadržaja.


Važno je napomenuti da Diffie-Helmann ključ Exchange nije asimetrična šema. Strogo govoreći, može se tvrditi da pripada oblasti simetrične kriptografije ključa. Ali pošto se i Diffie-Helmann ključ Exchange i asimetrična kriptografija oslanjaju na jednosmerne brojevno-teorijske funkcije sa zamkama, obično se razmatraju zajedno.


Drugi način koji su Diffie i Helmann ponudili Address za problem distribucije i upravljanja ključevima u svom radu iz 1976. godine bio je, naravno, putem asimetrične kriptografije.


Nasuprot njihovoj prezentaciji Diffie-Hellman ključa Exchange, oni su pružili samo opšte konture kako bi asimetrične kriptografske šeme mogle biti konstruisane. Nisu ponudili nikakvu jednosmernu funkciju koja bi specifično mogla ispuniti uslove potrebne za razumnu sigurnost u takvim šemama.


Praktična implementacija asimetrične šeme je, međutim, pronađena godinu dana kasnije od strane tri različita akademska kriptografa i matematičara: Ronald Rivest, Adi Shamir i Leonard Adleman. [3] Kriptosistem koji su predstavili postao je poznat kao **RSA kriptosistem** (po njihovim prezimenima).


Funkcije sa skrivenim vratima korišćene u asimetričnoj kriptografiji (i Diffie Helmann ključ Exchange) su sve povezane sa dva glavna **računska Hard problema**: faktorizacija prostih brojeva i izračunavanje diskretnih logaritama.


**Faktorizacija prostih brojeva** zahteva, kao što ime implicira, razlaganje celog broja na njegove proste faktore. RSA problem je daleko najpoznatiji primer kriptosistema povezanog sa faktorizacijom prostih brojeva.


**Problem diskretnog logaritma** je problem koji se javlja u cikličkim grupama. Dat je generator u određenoj cikličkoj grupi, i potrebno je izračunati jedinstveni eksponent potreban da se iz generatora proizvede drugi element u grupi.


Šeme zasnovane na diskretnom logaritmu oslanjaju se na dve glavne vrste cikličnih grupa: multiplikativne grupe celih brojeva i grupe koje uključuju tačke na eliptičkim krivama. Originalni Diffie Helmann ključ Exchange, kako je predstavljen u “New Directions in Cryptography”, radi sa cikličnom multiplikativnom grupom celih brojeva. Bitcoin-ov algoritam digitalnog potpisa i nedavno uvedena Schnorr šema potpisa (2021) zasnovani su na problemu diskretnog logaritma za određenu cikličnu grupu eliptičke krive.


Zatim ćemo preći na pregled tajnosti i autentifikacije na visokom nivou u asimetričnom okruženju. Međutim, pre nego što to učinimo, potrebno je da napravimo kratku istorijsku napomenu.


Sada se čini verovatnim da je grupa britanskih kriptografa i matematičara koji su radili za Vladin komunikacioni štab (GCHQ) nezavisno došla do gore pomenutih otkrića nekoliko godina ranije. Ova grupa se sastojala od Džejmsa Elisa, Kliforda Koksa i Malkolma Vilijamsona.


Prema njihovim sopstvenim izveštajima i izveštaju GCHQ-a, Džejms Elis je prvi osmislio koncept kriptografije javnog ključa 1969. Navodno je Kliford Koks zatim otkrio RSA kriptografski sistem 1973. godine, a Malkolm Vilijamson koncept Diffie Helmann ključa Exchange 1974. godine. [4] Njihova otkrića, međutim, navodno nisu bila otkrivena sve do 1997. godine, s obzirom na tajnu prirodu rada u GCHQ-u.



**Beleške:**


[1] Whitfield Diffie i Martin Hellman, “New directions in cryptography,” _IEEE Transactions on Information Theory_ IT-22 (1976), pp. 644–654, at p. 644.


[2] Ralph Merkle takođe diskutuje o ključnom Exchange protokolu u “Secure communications over insecure channels”, _Communications of the Association for Computing Machinery_, 21 (1978), 294–99. Iako je Merkle zapravo predao ovaj rad pre rada Diffieja i Hellmana, objavljen je kasnije. Merkleovo rešenje nije eksponencijalno sigurno, za razliku od Diffie-Hellmanovog.


[3] Ron Rivest, Adi Shamir, and Leonard Adleman, “A method for obtaining digital signatures and public-key cryptosystems”, _Communications of the Association for Computing Machinery_, 21 (1978), pp. 120–26.


[4] Dobra istorija ovih otkrića je data od strane Simon Singh, _The Code Book_, Fourth Estate (London, 1999), Poglavlje 6.





## Asimetrično šifrovanje i autentifikacija

<chapterId>2f6f0f03-3c3d-5025-90f0-5211139bc0cc</chapterId>


Pregled **asimetrične enkripcije** uz pomoć Boba i Alise dat je na *Slici 1*.


Alisa prvo kreira par ključeva, koji se sastoje od jednog javnog ključa ($K_P$) i jednog privatnog ključa ($K_S$), gde “P” u $K_P$ označava “public” (javni) a “S” u $K_S$ označava “secret” (tajni). Ona zatim slobodno distribuira ovaj javni ključ drugima. Detaljima ovog procesa distribucije ćemo se vratiti malo kasnije. Ali za sada, pretpostavimo da bilo ko, uključujući Boba, može sigurno dobiti Alisin javni ključ $K_P$.


U nekom kasnijem trenutku, Bob želi da napiše poruku $M$ Alisi. Pošto uključuje osetljive informacije, želi da sadržaj ostane tajna za sve osim za Alisu. Dakle, Bob prvo šifruje svoju poruku $M$ koristeći $K_P$. Zatim šalje dobijeni šifrat $C$ Alisi, koja dešifruje $C$ sa $K_S$ kako bi dobila originalnu poruku $M$.


*Slika 1: Asimetrična enkripcija*


![Figure 1: Asymmetric encryption](assets/Figure6-1.webp "Figure 1: Asymmetric encryption")



Bilo koji protivnik koji prisluškuje komunikaciju između Boba i Alise može da posmatra $C$. Ona takođe zna $K_P$ i algoritam za šifrovanje $E(\cdot)$. Međutim, važno je napomenuti da ove informacije ne omogućavaju napadaču da na izvodljiv način dešifruje šifrat $C$. Dešifrovanje specifično zahteva $K_S$, koji napadač ne poseduje.


Simetrične šeme šifrovanja generalno treba da budu sigurne protiv napadača koji može validno šifrovati tekstualne poruke (poznato kao sigurnost protiv napada sa izabranim šifro tekstom). Međutim, nije dizajnirano sa eksplicitnom svrhom omogućavanja kreiranja takvih validnih šifro tekstova od strane napadača ili bilo koga drugog.


Ovo je u oštroj suprotnosti sa asimetričnom šemom enkripcije, gde je cela njena svrha da omogući bilo kome, uključujući napadače, da proizvedu validne šifrovane tekstove. Asimetrične šeme enkripcije se, stoga, mogu označiti kao **šifre sa višestrukim pristupom**.


Da biste bolje razumeli šta se dešava, zamislite da umesto da šalje poruku elektronski, Bob želi da pošalje fizičko pismo u tajnosti. Jedan način da se obezbedi tajnost bio bi da Alisa pošalje siguran katanac Bobu, ali da zadrži ključ za njegovo otključavanje. Nakon što napiše pismo, Bob bi mogao da stavi pismo u kutiju i zatvori je Alisinim katancem. Zatim bi mogao da pošalje zaključanu kutiju sa porukom Alisi koja ima ključ da je otključa.


Dok Bob može zaključati katanac, ni on ni bilo koja druga osoba koja presretne kutiju ne može otključati katanac ako je zaista siguran. Samo ga Alisa može otključati i videti sadržaj Bobovog pisma jer ona ima ključ.


Šema asimetričnog šifrovanja je, grubo govoreći, digitalna verzija ovog procesa. Katanac je sličan javnom ključu, a ključ katanca je sličan privatnom ključu. Međutim, zato što je katanac digitalan, mnogo je lakše i nije toliko skupo za Alisu da ga distribuira svima koji bi možda želeli da joj pošalju tajne poruke.


Za autentifikaciju u asimetričnom okruženju koristimo **digitalne potpise**. Oni, dakle, imaju istu funkciju kao kodovi za autentifikaciju poruka u simetričnom okruženju. Pregled digitalnih potpisa je dat u *Figure 2*.


Bob prvo kreira par ključeva, koji se sastoje od javnog ključa ($K_P$) i privatnog ključa ($K_S$), i distribuira svoj javni ključ. Kada želi da pošalje autentifikovanu poruku Alisi, prvo uzima svoju poruku $M$ i svoj privatni ključ da kreira **digitalni potpis** $D$. Bob zatim šalje Alisi svoju poruku zajedno sa digitalnim potpisom.


Alisa ubacuje poruku, javni ključ i digitalni potpis u **algoritam za verifikaciju**. Ovaj algoritam proizvodi ili **tačno** za važeći potpis, ili **netačno** za nevažeći potpis.


Digitalni potpis je, kao što naziv jasno implicira, digitalni ekvivalent pisanog potpisa na pismima, ugovorima i slično. U stvari, digitalni potpis je obično mnogo sigurniji. Uz malo truda, možete falsifikovati pisani potpis; proces koji je olakšan činjenicom da se pisani potpisi često ne proveravaju pažljivo. Međutim, siguran digitalni potpis je, baš kao i siguran kod za autentifikaciju poruka, **egzistencijalno nefalšljiv**: to jest, sa sigurnom šemom digitalnog potpisa, niko ne može izvodljivo kreirati potpis za poruku koji prolazi proceduru verifikacije, osim ako nema privatni ključ.


*Slika 2: Asimetrična autentifikacija*


![Figure 2: Asymmetric authentication](assets/Figure6-2.webp "Figure 2: Asymmetric authentication")



Kao i kod asimetrične enkripcije, vidimo zanimljiv kontrast između digitalnih potpisa i kodova za autentifikaciju poruka. Za ove poslednje, verifikacioni algoritam može koristiti samo jedna od strana koja je upoznata sa sigurnom komunikacijom. To je zato što zahteva privatni ključ. Međutim, u asimetričnom okruženju, bilo ko može verifikovati digitalni potpis $S$ koji je napravio Bob.


Sve ovo čini digitalne potpise izuzetno moćnim alatom. Oni čine osnovu, na primer, za kreiranje potpisa na ugovorima koji se mogu verifikovati u pravne svrhe. Ako je Bob napravio potpis na Contract u gore navedenom Exchange, Alisa može pokazati poruku $M$, Contract i potpis $S$ sudu. Sud tada može verifikovati potpis koristeći Bobov javni ključ. [5]


Za još jedan primer, digitalni potpisi su važan aspekt bezbednog softvera i distribucije ažuriranja softvera. Ova vrsta javne proverljivosti nikada ne bi mogla biti kreirana korišćenjem samo kodova za autentifikaciju poruka.


Kao poslednji primer moći digitalnih potpisa, razmotrite Bitcoin. Jedna od najčešćih zabluda o Bitcoin, posebno u medijima, jeste da su transakcije šifrovane: nisu. Umesto toga, Bitcoin transakcije rade sa digitalnim potpisima kako bi se osigurala bezbednost.


Bitcoini postoje u serijama koje se nazivaju neiskorišćeni izlazi transakcija (ili **UTXO**). Pretpostavimo da primite tri uplate na određenom Bitcoin Address za po 2 bitcoina. Tehnički, sada nemate 6 bitcoina na tom Address. Umesto toga, imate tri serije od po 2 bitcoina koje su zaključane kriptografskim problemom povezanim sa tim Address. Za svaku uplatu koju izvršite, možete koristiti jednu, dve ili sve tri od ovih serija, u zavisnosti od toga koliko vam je potrebno za transakciju.


Dokaz Ownership nad neiskorišćenim izlazima transakcija obično se prikazuje putem jednog ili više digitalnih potpisa. Bitcoin funkcioniše upravo zato što je izrada važećih digitalnih potpisa na neiskorišćenim izlazima transakcija računski neizvodljiva, osim ako ne posedujete tajne informacije potrebne za njihovu izradu.


Trenutno, Bitcoin transakcije transparentno uključuju sve informacije koje treba da budu verifikovane od strane učesnika u mreži, kao što su porekla neiskorišćenih izlaza transakcija korišćenih u transakciji. Iako je moguće sakriti neke od tih informacija i dalje omogućiti verifikaciju (kao što to čine neke alternativne kriptovalute poput Monera), ovo takođe stvara određene bezbednosne rizike.


Zbunjenost ponekad nastaje oko digitalnih potpisa i pisanih potpisa uhvaćenih digitalno. U potonjem slučaju, uhvatite sliku svog pisanog potpisa i zalepite je na elektronski dokument kao što je zaposlenje Contract. Međutim, ovo nije digitalni potpis u kriptografskom smislu. Potonji je samo dugačak broj koji se može proizvesti samo posedovanjem privatnog ključa.


Baš kao u simetričnom ključnom okruženju, možete koristiti i asimetrične šeme za šifrovanje i autentifikaciju zajedno. Slični principi se primenjuju. Pre svega, trebalo bi koristiti različite parove privatnih-javnih ključeva za šifrovanje i pravljenje digitalnih potpisa. Pored toga, prvo bi trebalo šifrovati poruku, a zatim je autentifikovati.


Važno je napomenuti da se u mnogim aplikacijama asimetrična kriptografija ne koristi tokom celog procesa komunikacije. Umesto toga, obično će se koristiti samo za *Exchange simetrične ključeve* između strana putem kojih će zapravo komunicirati.


Ovo je slučaj, na primer, kada kupujete robu putem interneta. Znajući javni ključ prodavca, ona vam može poslati digitalno potpisane poruke koje možete verifikovati radi njihove autentičnosti. Na osnovu toga, možete slediti jedan od više protokola za razmenu simetričnih ključeva kako biste bezbedno komunicirali.


Glavni razlog za učestalost prethodno pomenutog pristupa je taj što je asimetrična kriptografija mnogo manje efikasna od simetrične kriptografije u postizanju određenog nivoa sigurnosti. Ovo je jedan od razloga zašto nam je i dalje potrebna simetrična kriptografija pored javne kriptografije. Pored toga, simetrična kriptografija je mnogo prirodnija u posebnim aplikacijama kao što je korisnik računara koji šifrira sopstvene podatke.


Kako tačno digitalni potpisi i enkripcija javnim ključem Address rešavaju probleme distribucije ključeva i upravljanja ključevima?


Ne postoji samo jedan odgovor ovde. Asimetrična kriptografija je alat i ne postoji samo jedan način da se taj alat koristi. Ali hajde da uzmemo naš raniji primer iz Jim's Sporting Goods da pokažemo kako bi se problemi obično rešavali u ovom primeru.


Da bi počeo, Jim’s Sporting Goods bi verovatno pristupio **autoritetu za sertifikate**, organizaciji koja podržava distribuciju javnih ključeva. Autoritet za sertifikate bi registrovao neke detalje o Jim’s Sporting Goods i dodelio mu javni ključ. Zatim bi poslao Jim’s Sporting Goods sertifikat, poznat kao **TLS/SSL sertifikat**, sa javnim ključem Jim’s Sporting Goods digitalno potpisanim koristeći sopstveni javni ključ autoriteta za sertifikate. Na ovaj način, autoritet za sertifikate potvrđuje da određeni javni ključ zaista pripada Jim’s Sporting Goods.


Ključ za razumevanje ovog procesa sa TLS/SSL sertifikatima je da, iako generalno nećete imati javni ključ Jim’s Sporting Goods-a sačuvan bilo gde na vašem računaru, javni ključevi priznatih sertifikacionih autoriteta su zaista sačuvani u vašem pregledaču ili u vašem operativnom sistemu. Oni su sačuvani u onome što se zove **root sertifikati**.


Dakle, kada vam Jim’s Sporting Goods obezbedi svoj TLS/SSL sertifikat, možete verifikovati digitalni potpis sertifikacionog tela putem root sertifikata u vašem pregledaču ili operativnom sistemu. Ako je potpis validan, možete biti relativno sigurni da javni ključ na sertifikatu zaista pripada Jim’s Sporting Goods. Na ovoj osnovi, lako je uspostaviti protokol za sigurnu komunikaciju sa Jim’s Sporting Goods.


Distribucija ključeva sada je postala znatno jednostavnija za Jim’s Sporting Goods. Nije Hard videti da je upravljanje ključevima takođe postalo znatno pojednostavljeno. Umesto da mora da skladišti hiljade ključeva, Jim’s Sporting Goods samo treba da skladišti privatni ključ koji mu omogućava da pravi potpise za javni ključ na svom SSL sertifikatu. Svaki put kada kupac poseti sajt Jim’s Sporting Goods, može uspostaviti sigurnu komunikacionu sesiju putem ovog javnog ključa. Kupci takođe ne moraju da skladište bilo kakve informacije (osim javnih ključeva priznatih sertifikacionih autoriteta u svom operativnom sistemu i pregledaču).


**Beleške:**


[5] Bilo koji planovi koji pokušavaju da postignu neporicanje, druga tema o kojoj smo diskutovali u Poglavlju 1, će u svojoj osnovi morati da uključe digitalne potpise.




## Hash funkcije

<chapterId>ea8327ab-b0e3-5635-941c-4b51f396a648</chapterId>


Funkcije Hash su sveprisutne u kriptografiji. One nisu ni simetrične ni asimetrične šeme, već spadaju u kriptografsku kategoriju za sebe.


Već smo naišli na funkcije Hash u Poglavlju 4 prilikom kreiranja poruka za autentifikaciju zasnovanih na Hash. One su takođe važne u kontekstu digitalnih potpisa, ali iz nešto drugačijeg razloga: Digitalni potpisi se naime obično prave preko Hash vrednosti neke (šifrovane) poruke, a ne stvarne (šifrovane) poruke. U ovom delu, ponudiću detaljniji uvod u funkcije Hash.


Hajde da počnemo sa definisanjem Hash funkcije. **Hash funkcija** je bilo koja efikasno izračunljiva funkcija koja prima ulaze proizvoljne veličine i daje izlaze fiksne dužine.


**kriptografska Hash funkcija** je samo Hash funkcija koja je korisna za primene u kriptografiji. Izlaz kriptografske Hash funkcije se obično naziva **Hash**, **Hash-vrednost**, ili **sažetak poruke**.


U kontekstu kriptografije, "Hash funkcija" se obično odnosi na kriptografsku Hash funkciju. Usvojiću tu praksu od sada nadalje.


Primer popularne funkcije Hash je **SHA-256** (sigurni Hash algoritam 256). Bez obzira na veličinu ulaza (npr. 15 bita, 100 bita, ili 10,000 bita), ova funkcija će dati 256-bitnu Hash vrednost. Ispod možete videti nekoliko primera izlaza funkcije SHA-256.


„Hello“: `185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969`


„52398“: `a3b14d2bf378c1bd47e7f8eaec63b445150a3d7a80465af16dd9fd319454ba90`


„Kriptografija je zabavna“: `3cee2a5c7d2cc1d62db4893564c34ae553cc88623992d994e114e344359b146c`


Svi izlazi su tačno 256 bita zapisani u heksadecimalnom formatu (svaka heksadecimalna cifra može biti predstavljena sa četiri binarna broja). Dakle, čak i da ste ubacili Tolkinovu knjigu *Gospodar prstenova* u SHA-256 funkciju, izlaz bi i dalje bio 256 bita.


Funkcije Hash kao što je SHA-256 koriste se u razne svrhe u kriptografiji. Koja svojstva su potrebna od funkcije Hash zaista zavisi od konteksta određene primene. Postoje dva glavna svojstva koja se generalno žele od funkcija Hash u kriptografiji: [6]


1.	Otpornost na sudar

2.	Skrivanje


Funkcija $H$ tipa Hash se smatra **otporna na sudare** ako je neizvodljivo pronaći dve vrednosti, $x$ i $y$, takve da je $x \neq y$, a ipak $H(x) = H(y)$.


Koliziono otporne Hash funkcije su važne, na primer, u verifikaciji softvera. Pretpostavimo da želite da preuzmete Windows izdanje Bitcoin Core 0.21.0 (serverska aplikacija za obradu Bitcoin mrežnog saobraćaja). Glavni koraci koje biste morali preduzeti, kako biste verifikovali legitimnost softvera, su sledeći:


1.	Prvo treba da preuzmete i uvezete javne ključeve jednog ili više saradnika Bitcoin Core u softver koji može da verifikuje digitalne potpise (npr. Kleopetra). Te javne ključeve možete pronaći [ovde](https://github.com/Bitcoin/Bitcoin/blob/master/contrib/builder-keys/keys.txt). Preporučuje se da verifikujete Bitcoin Core softver sa javnim ključevima od više saradnika.

2.	Zatim, treba da verifikujete javne ključeve koje ste uvezli. Barem jedan korak koji treba da preduzmete je da proverite da li su javni ključevi koje ste pronašli isti kao oni objavljeni na raznim drugim mestima. Na primer, možete konsultovati lične veb stranice, Twitter stranice ili Github stranice osoba čije ste javne ključeve uvezli. Tipično se ovo poređenje javnih ključeva vrši poređenjem kratkog Hash javnog ključa poznatog kao otisak prsta.

3.	Zatim, treba da preuzmete izvršni fajl za Bitcoin Core sa njihove [veb stranice](www.bitcoincore.org). Biće dostupni paketi za Linux, Windows i MAC operativne sisteme.

4.	Zatim, morate pronaći dve datoteke izdanja. Prva sadrži zvanični SHA-256 Hash za izvršni fajl koji ste preuzeli zajedno sa hešovima svih ostalih paketa koji su objavljeni. Druga datoteka izdanja će sadržati potpise raznih saradnika preko datoteke izdanja sa hešovima paketa. Obe ove datoteke izdanja treba da se nalaze na Bitcoin Core vebsajtu.

5.	 Next, you would need to calculate the SHA-256 Hash of the executable you downloaded from the Bitcoin Core website on your own computer. You, then, compare this result with that for the official package Hash for the executable. They should be the same.

6.	Konačno, morali biste da verifikujete da jedan ili više digitalnih potpisa nad datotekom izdanja sa zvaničnim hešovima paketa zaista odgovara jednom ili više javnih ključeva koje ste uvezli (izdanja Bitcoin Core nisu uvek potpisana od strane svih). To možete učiniti pomoću aplikacije kao što je Kleopetra.


Ovaj proces verifikacije softvera ima dve glavne prednosti. Prvo, osigurava da nije bilo grešaka u prenosu prilikom preuzimanja sa vebsajta Bitcoin Core. Drugo, osigurava da vas nijedan napadač nije mogao navesti da preuzmete izmenjeni, zlonamerni kod, bilo hakovanjem vebsajta Bitcoin Core ili presretanjem saobraćaja.


Kako tačno proces verifikacije softvera gore štiti od ovih problema?


Ako ste marljivo verifikovali javne ključeve koje ste uvezli, onda možete biti prilično sigurni da su ovi ključevi zaista njihovi i da nisu kompromitovani. S obzirom na to da digitalni potpisi imaju egzistencijalnu nekrivotvorivost, znate da su samo ovi saradnici mogli napraviti digitalni potpis preko zvaničnih heševa paketa na fajlu izdanja.


Pretpostavimo da su potpisi na datoteci za izdanje koju ste preuzeli ispravni. Sada možete uporediti Hash vrednost koju ste lokalno izračunali za Windows izvršnu datoteku koju ste preuzeli sa onom koja je uključena u pravilno potpisanu datoteku za izdanje. Kao što znate, SHA-256 Hash funkcija je otporna na kolizije, podudaranje znači da je vaša izvršna datoteka tačno ista kao zvanična izvršna datoteka.


Sada se osvrnimo na drugo zajedničko svojstvo Hash funkcija: **skrivanje**. Za bilo koju Hash funkciju $H$ se kaže da ima svojstvo skrivanja ako, za bilo koji nasumično odabrani $x$ iz veoma velikog opsega, nije izvodljivo pronaći $x$ kada je dat samo $H(x)$.


Ispod možete videti SHA-256 izlaz poruke koju sam napisao. Da bi se osigurala dovoljna nasumičnost, poruka je uključivala nasumično generisan niz karaktera na kraju. S obzirom na to da SHA-256 ima svojstvo skrivanja, niko ne bi mogao da dešifruje ovu poruku.



- `b194221b37fa4cd1cfce15aaef90351d70de17a98ee6225088b523b586c32ded`


Ali neću vas držati u neizvesnosti dok SHA-256 ne postane slabiji. Originalna poruka koju sam napisao bila je sledeća:



- "Ovo je veoma nasumična poruka, ili pa donekle nasumična. Ovaj početni deo nije, ali ću završiti sa nekim relativno nasumičnim karakterima kako bih osigurao veoma nepredvidivu poruku. XLWz4dVG3BxUWm7zQ9qS".


Uobičajen način na koji se funkcije Hash sa svojstvom skrivanja koriste jeste u upravljanju lozinkama (otpornost na koliziju je takođe važna za ovu primenu). Bilo koja pristojna onlajn usluga zasnovana na nalogu, kao što su Facebook ili Google, neće direktno čuvati vaše lozinke za upravljanje pristupom vašem nalogu. Umesto toga, oni će čuvati samo Hash te lozinke. Svaki put kada unesete svoju lozinku u pregledač, prvo se izračunava Hash. Samo taj Hash se šalje serveru provajdera usluge i poredi sa Hash koji je sačuvan u bazi podataka u pozadini. Svojstvo skrivanja može pomoći da se osigura da napadači ne mogu povratiti lozinku iz vrednosti Hash.


Upravljanje lozinkama putem hešova, naravno, funkcioniše samo ako korisnici zaista biraju teške lozinke. Svojstvo skrivanja pretpostavlja da je x izabran nasumično iz veoma velikog opsega. Biranje lozinki kao što su "1234", "mojalozinka" ili vaš datum rođenja neće pružiti nikakvu stvarnu sigurnost. Postoje dugačke liste uobičajenih lozinki i njihovih hešova koje napadači mogu iskoristiti ako ikada dobiju Hash vaše lozinke. Ove vrste napada su poznate kao **napadi rečnikom**. Ako napadači znaju neke od vaših ličnih podataka, mogli bi takođe pokušati sa informisanim pretpostavkama. Stoga, uvek su vam potrebne duge, sigurne lozinke (po mogućstvu dugi, nasumični nizovi iz menadžera lozinki).


Ponekad aplikaciji može biti potrebna Hash funkcija koja ima i otpornost na koliziju i skrivanje. Ali svakako ne uvek. Proces verifikacije softvera o kojem smo diskutovali, na primer, zahteva samo da Hash funkcija pokazuje otpornost na koliziju, skrivanje nije važno.


Iako su otpornost na koliziju i skrivanje glavna svojstva koja se traže kod Hash funkcija u kriptografiji, u određenim aplikacijama mogu biti poželjne i druge vrste svojstava.



**Beleške:**


[6] Terminologija „skrivanje“ nije uobičajen jezik, već je preuzeta specifično od Arvinda Narayanana, Josepha Bonneaua, Edwarda Feltena, Andrewa Millera i Stevena Goldfedera, *Bitcoin and Cryptocurrency Technologies*, Princeton University Press (Princeton, 2016), Poglavlje 1.



# RSA kriptosistem

<partId>864dca42-2a8d-530f-bb94-2e1f68b3f411</partId>




## Problem faktorisanja

<chapterId>a31a66e4-52ea-539c-9953-4769ad565d7e</chapterId>


Iako je simetrična kriptografija obično prilično intuitivna za većinu ljudi, to obično nije slučaj sa asimetričnom kriptografijom. Iako ste verovatno zadovoljni opisom na visokom nivou datim u prethodnim odeljcima, verovatno se pitate šta su tačno jednousmerne funkcije i kako se tačno koriste za konstruisanje asimetričnih šema.


U ovom poglavlju, ukloniću deo misterije oko asimetrične kriptografije, detaljnijim proučavanjem specifičnog primera, naime RSA kriptosistema. U prvom delu, predstaviću problem faktorizacije na kojem se zasniva RSA problem. Zatim ću pokriti niz ključnih rezultata iz teorije brojeva. U poslednjem delu, spojićemo ove informacije kako bismo objasnili RSA problem i kako se to može koristiti za kreiranje asimetričnih kriptografskih šema.


Dodavanje ove dubine našoj diskusiji nije lak zadatak. Zahteva uvođenje prilično mnogo teorema i propozicija iz teorije brojeva. Ali neka vas matematika ne obeshrabri. Rad na ovoj diskusiji će značajno poboljšati vaše razumevanje onoga što je osnova asimetrične kriptografije i predstavlja vrednu investiciju.


Hajde sada prvo da se okrenemo problemu faktorizacije.


___



Kad god pomnožite dva broja, recimo $a$ i $b$, te brojeve $a$ i $b$ nazivamo **faktorima**, a rezultat **proizvodom**. Pokušaj da se broj $N$ napiše kao množenje dva ili više faktora naziva se **faktorizacija** ili **faktorisanje**. [1] Bilo koji problem koji zahteva ovo možete nazvati **problemom faktorizacije**.


Pre oko 2.500 godina, grčki matematičar Euklid iz Aleksandrije otkrio je ključnu teoremu o faktorizaciji celih brojeva. Obično se naziva **teorema o jedinstvenoj faktorizaciji** i glasi sledeće:


**Teorema 1**. Svaki ceo broj $N$ koji je veći od 1 je ili prost broj, ili se može izraziti kao proizvod prostih činilaca.


Sav ovaj poslednji deo izjave znači da možete uzeti bilo koji složeni broj $N$ veći od 1 i zapisati ga kao proizvod prostih brojeva. Ispod su navedeni neki primeri složenih brojeva zapisanih kao proizvod prostih činilaca.



- $18 = 2 \cdot 3 \cdot 3 = 2 \cdot 3^2$
- $84 = 2 \cdot 2 \cdot 3 \cdot 7 = 2^2 \cdot 3 \cdot 7$
- $144 = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 3 \cdot 3 = 2^4 \cdot 3^2$


Za sva tri od gore navedenih celih brojeva, izračunavanje njihovih prostih faktora je relativno lako, čak i ako vam je dat samo $N$. Počinjete sa najmanjim prostim brojem, naime 2, i proveravate koliko puta je ceo broj $N$ deljiv njime. Zatim prelazite na testiranje deljivosti $N$ sa 3, 5, 7, i tako dalje. Nastavljate ovaj proces sve dok vaš ceo broj $N$ nije napisan kao proizvod samo prostih brojeva.


Uzmimo, na primer, ceo broj 84. Ispod možete videti proces određivanja njegovih prostih faktora. U svakom koraku, uzimamo najmanji preostali prosti faktor (sa leve strane) i određujemo preostali član koji treba faktorisati. Nastavljamo dok preostali član ne bude takođe prost broj. U svakom koraku, trenutna faktorizacija broja 84 prikazana je krajnje desno.



- Prosti činilac = 2: ostatak = 42 	($84 = 2 \cdot 42$)
- Prosti činilac = 2: ostatak = 21 	($84 = 2 \cdot 2 \cdot 21$)
- Prosti činilac = 3: ostatak = 7 	($84 = 2 \cdot 2 \cdot 3 \cdot 7$)
- Kako je 7 prost broj, rezultat je $2 \cdot 2 \cdot 3 \cdot 7$, ili $2^2 \cdot 3 \cdot 7$.


Pretpostavimo sada da je $N$ veoma velik. Koliko bi bilo teško rastaviti $N$ na njegove proste faktore?


To stvarno zavisi od $N$. Pretpostavimo, na primer, da je $N$ 50,450,400. Iako ovaj broj izgleda zastrašujuće, proračuni nisu toliko komplikovani i mogu se lako uraditi ručno. Kao i gore, samo počnete sa 2 i nastavite dalje. Ispod možete videti rezultat ovog procesa na sličan način kao gore.



- 2: 25,225,200 	($50,450,400 = 2 \cdot 25,225,200$)
- 2: 12,612,600 	($50,450,400 = 2^2 \cdot 12,612,600$)
- 2: 6,306,300 	($50,450,400 = 2^3 \cdot 6,306,300$)
- 2: 3,153,150 	($50,450,400 = 2^4 \cdot 3,153,150$)
- 2: 1,576,575 	($50,450,400 = 2^5 \cdot 1,576,575$)
- 3: 525,525 	($50,450,400 = 2^5 \cdot 3 \cdot 525,525$)
- 3: 175,175 	($50,450,400 = 2^5 \cdot 3^2 \cdot 175,175$)
- 5: 35,035 		($50,450,400 = 2^5 \cdot 3^2 \cdot 5 \cdot 35,035$)
- 5: 7,007		($50,450,400 = 2^5 \cdot 3^2 \cdot 5^2 \cdot 7,007$)
- 7: 1,001		($50,450,400 = 2^5 \cdot 3^2 \cdot 5^2 \cdot 7 \cdot 1,001$)
- 7: 143		($50,450,400 = 2^5 \cdot 3^2 \cdot 5^2 \cdot 7^2 \cdot 143$)
- 11: 13		($50,450,400 = 2^5 \cdot 3^2 \cdot 5^2 \cdot 7^2 \cdot 11 \cdot 13$)
- Kako je 13 prost broj, rezultat je $2^5 \cdot 3^2 \cdot 5^2 \cdot 7^2 \cdot 11 \cdot 13$.


Ručno rešavanje ovog problema oduzima dosta vremena. Računar, naravno, može sve ovo da uradi u malom deliću sekunde. Zapravo, računar često može čak i da faktoriše izuzetno velike cele brojeve u deliću sekunde.


Međutim, postoje određeni izuzeci. Pretpostavimo da prvo nasumično odaberemo dva veoma velika prosta broja. Uobičajeno je da ih označimo kao $p$ i $q$, i ja ću usvojiti tu konvenciju ovde.


Za konkretnost, recimo da su $p$ i $q$ oba prosti brojevi od 1024 bita, i da zaista zahtevaju najmanje 1024 bita da bi bili predstavljeni (tako da prvi bit mora biti 1). Dakle, na primer, 37 ne bi mogao biti jedan od prostih brojeva. Sigurno možete predstaviti 37 sa 1024 bita. Ali očigledno *ne trebate* ovoliko bita da ga predstavite. Možete predstaviti 37 bilo kojim nizom koji ima 6 bita ili više. (U 6 bita, 37 bi bio predstavljen kao $100101$).


Važno je ceniti koliko su veliki $p$ i $q$ ako su izabrani pod gore navedenim uslovima. Kao primer, izabrao sam nasumičan prost broj koji zahteva najmanje 1024 bita za predstavljanje ispod.



- 14,752,173,874,503,595,484,930,006,383,670,759,559,764,562,721,397,166,747,289,220,945,457,932,666,751,048,198,854,920,097,085,690,793,755,254,946,188,163,753,506,778,089,706,699,671,722,089,715,624,760,049,594,106,189,662,669,156,149,028,900,805,928,183,585,427,782,974,951,355,515,394,807,209,836,870,484,558,332,897,443,152,653,214,483,870,992,618,171,825,921,582,253,023,974,514,209,142,520,026,807,636,589


Pretpostavimo sada da nakon nasumičnog odabira prostih brojeva $p$ i $q$, množimo ih da dobijemo ceo broj $N$. Ovaj poslednji broj, dakle, je 2048-bitni broj koji zahteva najmanje 2048 bita za svoju reprezentaciju. On je mnogo, mnogo veći od bilo $p$ ili $q$.


Pretpostavimo da date računaru samo $N$, i zatražite od njega da pronađe dva 1024-bitna prosta faktora $N$. Verovatnoća da računar otkrije $p$ i $q$ je izuzetno mala. Može se reći da je to nemoguće za sve praktične svrhe. Ovo važi čak i ako biste koristili superračunar ili čak mrežu superračunara.


Za početak, pretpostavimo da računar pokušava da reši problem prolazeći kroz 1024-bitne brojeve, testirajući u svakom slučaju da li su prosti i da li su faktori od $N$. Skup prostih brojeva koji treba testirati je tada približno $1.265 \cdot 10^{305}$. [2]


Čak i ako uzmete sve računare na planeti i pokušate da pronađete i testirate 1024-bitne proste brojeve na ovaj način, šansa od 1 prema milijardu da uspešno pronađete prosti faktor od $N$ zahtevala bi period računanja mnogo duži od starosti Univerzuma.


Sada u praksi računar može bolje da obavi posao od grube procedure upravo opisane. Postoji nekoliko algoritama koje računar može primeniti kako bi brže došao do faktorizacije. Poenta je, međutim, da čak i korišćenjem ovih efikasnijih algoritama, zadatak računara je i dalje računarski neizvodljiv. [3]


Važno je napomenuti da se težina faktorizacije pod upravo opisanim uslovima oslanja na pretpostavku da ne postoje računarski efikasni algoritmi za izračunavanje prostih faktora. Ne možemo zapravo dokazati da efikasan algoritam ne postoji. Ipak, ova pretpostavka je vrlo verovatna: uprkos opsežnim naporima koji traju stotinama godina, još uvek nismo pronašli takav računarski efikasan algoritam.


Stoga, problem faktorizacije, pod određenim okolnostima, može se verovatno smatrati Hard problemom. Konkretno, kada su $p$ i $q$ veoma veliki prosti brojevi, njihov proizvod $N$ nije teško izračunati; ali faktorizacija samo uz dato $N$ je praktično nemoguća.



**Beleške:**


[1] Faktorizacija takođe može biti važna za rad sa drugim vrstama matematičkih objekata osim brojeva. Na primer, može biti korisno faktorisati polinomske izraze kao što je $x^2 - 2x + 1$. U našoj diskusiji, fokusiraćemo se samo na faktorizaciju brojeva, konkretno celih brojeva.


[2] Prema **teoremi o prostim brojevima**, broj prostih brojeva manjih ili jednakih $N$ je približno $N/\LN(N)$. To znači da možete aproksimirati broj prostih brojeva dužine 1024 bita pomoću:


$$ \frac{2^{1024}}{\LN(2^{1024})} - \frac{2^{1023}}{\LN(2^{1023})} $$


...što je približno jednako $1.265 \times 10^{305}$.


[3] Isto je tačno za probleme diskretnih logaritama. Dakle, zašto asimetrične konstrukcije rade sa mnogo većim ključevima nego simetrične kriptografske konstrukcije.




## Rezultati teorije brojeva

<chapterId>23cd2186-8d97-5709-a4a7-b984f1eb9999</chapterId>


Nažalost, problem faktorizacije ne može se direktno koristiti za asimetrične kriptografske šeme. Međutim, možemo koristiti složeniji, ali srodan problem u tu svrhu: RSA problem.


Da bismo razumeli RSA problem, potrebno je da razumemo niz teorema i propozicija iz teorije brojeva. Oni su predstavljeni u ovom odeljku u tri pododeljka: (1) red N, (2) invertibilnost modulo N, i (3) Eulerova teorema.


Neki od materijala u tri pododeljka već su predstavljeni u *Poglavlju 3*. Ali ću ovde ponovo izložiti taj materijal radi lakšeg snalaženja.



### Redosled N


Ceo broj $a$ je **relativno prost** ili **kopriman** sa celim brojem $N$, ako je njihov najveći zajednički delilac 1. Iako 1 po konvenciji nije prost broj, ona je kopriman broj sa svakim celim brojem (kao i $-1$).


Na primer, razmotrite slučaj kada je $a = 18$ i $N = 37$. Ovi brojevi su očigledno međusobno prosti. Najveći ceo broj koji deli i 18 i 37 je 1. Nasuprot tome, razmotrite slučaj kada je $a = 42$ i $N = 16$. Ovi brojevi očigledno nisu međusobno prosti. Obe brojeve deli 2, što je veće od 1.


Sada možemo definisati red $N$ na sledeći način. Pretpostavimo da je $N$ ceo broj veći od 1. **Red broja N** je, dakle, broj svih brojeva koji su uzajamno prosti sa $N$ tako da za svaki uzajamno prost broj $a$, važi sledeći uslov: $1 \leq a < N$.


Na primer, ako je $N = 12$, onda su 1, 5, 7 i 11 jedini koprimerni brojevi koji ispunjavaju gore navedeni uslov. Dakle, red 12 je jednak 4.


Pretpostavimo da je $N$ prost broj. Tada je svaki ceo broj manji od $N$, ali veći ili jednak 1, relativno prost sa njim. Ovo uključuje sve Elements u sledećem skupu: $\{1,2,3,....,N - 1\}$. Dakle, kada je $N$ prost, red $N$ je $N - 1$. Ovo je navedeno u propoziciji 1, gde $\phi(N)$ označava red $N$.


**Proposition 1**. $\phi(N) = N - 1$ kada je $N$ prost


Pretpostavimo da $N$ nije prost. Tada možete izračunati njegov red koristeći **Eulerovu Fi funkciju**. Dok je izračunavanje reda malog celog broja relativno jednostavno, Eulerova Fi funkcija postaje posebno važna za veće cele brojeve. Propozicija Eulerove Fi funkcije je navedena ispod.


**Teorema 2**. Neka je $N$ jednako $p_1^{e_1} \cdot p_2^{e_2} \cdot \ldots \cdot p_i^{e_i} \cdot \ldots \cdot p_n^{e_n}$, gde skup $\{p_i\}$ sadrži sve različite proste faktore od $N$ i svaki $e_i$ označava koliko puta se prosti faktor $p_i$ pojavljuje u $N$. Tada,


$$\phi(N) = p_1^{e_1 - 1} \cdot (p_1 - 1) \cdot p_2^{e_2 - 1} \cdot (p_2 - 1) \cdot \ldots \cdot p_n^{e_n - 1} \cdot (p_n - 1)$$


**Theorem 2** pokazuje da kada razložite bilo koji složeni broj $N$ na njegove različite proste faktore, lako je izračunati redosled $N$.


Na primer, pretpostavimo da je $N = 270$. Ovo očigledno nije prost broj. Razlaganje $N$ na njegove proste faktore daje izraz: $2 \cdot 3^3 \cdot 5$. Prema Ojlerovoj Fi funkciji, redosled $N$ je zatim sledeći:


$$\phi(N) = 2^{1 - 1} \cdot (2 - 1) + 3^{3 - 1} \cdot (3 - 1) + 5^{1 - 1} \cdot (5 - 1) = 1 \cdot 1 + 9 \cdot 2 + 1 \cdot 4 = 1 + 18 + 4 = 23$$


Pretpostavimo dalje da je $N$ proizvod dva prosta broja, $p$ i $q$. **Teorema 2** iznad, tada, navodi da je red $N$ sledeći:


$$p^{1 - 1} \cdot (p - 1) \cdot q^{1 - 1} \cdot (q - 1) = (p - 1) \cdot (q - 1)$$


Ovo je ključni rezultat posebno za RSA problem, i naveden je u **Propoziciji 2** ispod.


**Proposition 2**. Ako je $N$ proizvod dva prosta broja, $p$ i $q$, red $N$ je proizvod $(p - 1) \cdot (q - 1)$.


Na primer, pretpostavimo da je $N = 119$. Ovaj ceo broj može se rastaviti na dva prosta broja, naime 7 i 17. Dakle, Ojlerova Fi funkcija sugeriše da je redosled od 119 sledeći:


$$\phi(119) = (7 - 1) \cdot (17 - 1) = 6 \cdot 16 = 96$$


Drugim rečima, ceo broj 119 ima 96 međusobno prostih brojeva u opsegu od 1 do 119. Zapravo, ovaj skup uključuje sve cele brojeve od 1 do 119, koji nisu deljivi sa 7 ili 17.


Od sada, označimo skup međusobno prostih brojeva koji određuju redosled $N$ kao $C_N$. Za naš primer gde je $N = 119$, skup $C_{119}$ je previše veliki da bismo ga potpuno naveli. Ali neki od Elements su sledeći:


$$C_{119} = \{1, 2, \dots 6, 8 \dots 13, 15, 16, 18, \dots 33, 35 \dots 96\}$$


### Invertibilnost modulo N


Možemo reći da je ceo broj $a$ **invertibilan modulo N**, ako postoji bar jedan ceo broj $b$ takav da $a \cdot b \mod N = 1 \mod N$. Bilo koji takav ceo broj $b$ naziva se **inverz** (ili **multiplikativni inverz**) od $a$ pri redukciji modulo $N$.


Pretpostavimo, na primer, da je $a = 5$ i $N = 11$. Postoji mnogo celih brojeva kojima možete pomnožiti 5, tako da $5 \cdot b \mod 11 = 1 \mod 11$. Razmotrite, na primer, cele brojeve 20 i 31. Lako je videti da su oba ova cela broja inverzi od 5 za redukciju modulo 11.



- $5 \cdot 20 \mod 11 = 100 \mod 11 = 1 \mod 11$
- $5 \cdot 31 \mod 11 = 155 \mod 11 = 1 \mod 11$


Iako 5 ima mnogo inverza u redukciji modulo 11, možete pokazati da postoji samo jedan pozitivan inverz od 5 koji je manji od 11. Zapravo, ovo nije jedinstveno za naš konkretan primer, već je opšti rezultat.


**Proposition 3**. Ako je ceo broj $a$ invertibilan modulo $N$, mora biti slučaj da tačno jedan pozitivan inverz od $a$ je manji od $N$. (Dakle, ovaj jedinstveni inverz od $a$ mora dolaziti iz skupa $\{1, \dots, N - 1\}$).


Neka označimo jedinstveni inverz od $a$ iz **Propozicije 3** kao $a^{-1}$. Za slučaj kada je $a = 5$ i $N = 11$, možete videti da je $a^{-1} = 9$, s obzirom da $5 \cdot 9 \mod 11 = 45 \mod 11 = 1 \mod 11$.


Primetite da možete dobiti vrednost 9 za $a^{-1}$ u našem primeru jednostavnim redukovanjem bilo kog drugog inverza od $a$ po modulu 11. Na primer, $20 \mod 11 = 31 \mod 11 = 9 \mod 11$. Dakle, kad god je ceo broj $a > N$ invertibilan po modulu $N$, tada $a \mod N$ takođe mora biti invertibilan po modulu $N$.


Nije nužno da inverz od $a$ postoji u redukciji modulo $N$. Pretpostavimo, na primer, da je $a = 2$ i $N = 8$. Ne postoji $b$, ili bilo koji $a^{-1}$ specifično, takav da $2 \cdot b \mod 8 = 1 \mod 8$. Ovo je zato što će bilo koja vrednost $b$ uvek proizvesti višekratnik od 2, tako da nikakva podela sa 8 nikada ne može dati ostatak koji je jednak 1.


Kako tačno znamo da li neki ceo broj $a$ ima inverz za dati $N$? Kao što ste možda primetili u gornjem primeru, najveći zajednički delilac između 2 i 8 je veći od 1, tačnije 2. I ovo je zapravo ilustrativno za sledeći opšti rezultat:


**Proposition 4**. Inverz postoji za ceo broj $a$ dat redukcijom modulo $N$, i specifično jedinstven pozitivan inverz manji od $N$, ako i samo ako je najveći zajednički delilac između $a$ i $N$ jednak 1 (to jest, ako su međusobno prosti).


Za slučaj kada je $a = 5$ i $N = 11$, zaključili smo da je $a^{-1} = 9$, s obzirom na to da $5 \cdot 9 \mod 11 = 45 \mod 11 = 1 \mod 11$. Važno je napomenuti da je i obrnuto tačno. To jest, kada je $a = 9$ i $N = 11$, važi da je $a^{-1} = 5$.



### Eulerova teorema


Pre nego što pređemo na RSA problem, moramo razumeti još jedan ključni teorem, naime **Eulerov teorem**. On kaže sledeće:


**Teorema 3**. Pretpostavimo da su dva cela broja $a$ i $N$ međusobno prosti. Tada, $a^{\phi(N)} \mod N = 1 \mod N$.


Ovo je izvanredan rezultat, ali na prvi pogled malo zbunjujući. Okrenimo se primeru da bismo ga razumeli.


Pretpostavimo da je $a = 5$ i $N = 7$. Oni su zaista međusobno prosti kao što Eulerova teorema zahteva. Znamo da je red 7 jednak 6, s obzirom da je 7 prost broj (vidi **Propoziciju 1**).


Ono što sada kaže Eulerova teorema je da $5^6 \mod 7$ mora biti jednako $1 \mod 7$. Ispod su proračuni koji pokazuju da je ovo zaista tačno.



- $5^6 \mod 7 = 15,625 \mod 7 = 1 \mod N$


Ceo broj 7 deli se u 15,624 ukupno 2,233 puta. Dakle, ostatak pri deljenju 16,625 sa 7 je 1.


Dalje, koristeći Ojlerovu funkciju Fi, **Teorema 2**, možete izvesti **Propoziciju 5** ispod.


**Proposition 5**. $\phi(a \cdot b) = \phi(a) \cdot \phi(b)$ za bilo koje pozitivne cele brojeve $a$ i $b$.


Nećemo pokazati zašto je to slučaj. Ali samo napominjemo da ste već videli dokaz ove tvrdnje činjenicom da je $\phi(p \cdot q) = \phi(p) \cdot \phi(q) = (p - 1) \cdot (q - 1)$ kada su $p$ i $q$ prosti brojevi, kao što je navedeno u **Propoziciji 2**.


Eulerova teorema u vezi sa **Propozicijom 5** ima važne implikacije. Pogledajte šta se dešava, na primer, u izrazima ispod, gde su $a$ i $N$ međusobno prosti.



- $a^{2 \cdot \phi(N)} \mod N = a^{\phi(N)} \cdot a^{\phi(N)} \mod N = 1 \cdot 1 \mod N = 1 \mod N$
- $a^{\phi(N) + 1} \mod N = a^{\phi(N)} \cdot a^1 \mod N = 1 \cdot a^1 \mod N = a \mod N$
- $a^{8 \cdot \phi(N) + 3} \mod N = a^{8 \cdot \phi(N)} \cdot a^3 \mod N = 1 \cdot a^3 \mod N = a^3 \mod N$


Stoga, kombinacija Eulerove teoreme i **Propozicije 5** omogućava nam jednostavno izračunavanje niza izraza. Uopšteno, možemo sažeti uvid kao u **Propoziciji 6**.


**Proposition 6**. $a^x \mod N = a^{x \mod \phi(N)}$


Sada moramo sve sastaviti u složenom poslednjem koraku.


Baš kao što $N$ ima red $\phi(N)$ koji uključuje Elements skupa $C_N$, znamo da ceo broj $\phi(N)$ takođe mora imati red i skup međusobno prostih brojeva. Neka je $\phi(N) = R$. Tada znamo da postoji i vrednost za $\phi(R)$ i skup međusobno prostih brojeva $C_R$.


Pretpostavimo da sada biramo ceo broj $e$ iz skupa $C_R$. Znamo iz **Propozicije 3** da ovaj ceo broj $e$ ima samo jedan jedinstven pozitivan inverz manji od $R$. To jest, $e$ ima jedan jedinstven inverz iz skupa $C_R$. Nazovimo taj inverz $d$. S obzirom na definiciju inverza, to znači da je $e \cdot d = 1 \mod R$.


Možemo koristiti ovaj rezultat da bismo dali izjavu o našem originalnom celom broju $N$. Ovo je sažeto u **Propoziciji 7**.


**Proposition 7**. Suppose that $e \cdot d \mod \phi(N) = 1 \mod \phi(N)$. Then for any element $a$ of the set $C_N$ it must be the case that $a^{e \cdot d \mod \phi(N)} = a^{1 \mod \phi(N)} = a \mod N$.


Sada imamo sve rezultate teorije brojeva potrebne da jasno formulišemo RSA problem.



## RSA kriptosistem

<chapterId>0253c2f7-b8a4-5d0e-bd60-812ed6b6c7a9</chapterId>


Sada smo spremni da navedemo RSA problem. Pretpostavimo da kreirate skup promenljivih koji se sastoji od $p$, $q$, $N$, $\phi(N)$, $e$, $d$, i $y$. Nazovite ovaj skup $\Pi$. Kreira se na sledeći način:


1. generate dva nasumična prosta broja $p$ i $q$ jednake veličine i izračunaj njihov proizvod $N$.

2. Izračunajte red $N$, $\phi(N)$, pomoću sledećeg proizvoda: $(p - 1) \cdot (q - 1)$.

3. Odaberite $e > 2$ tako da je manji i uzajamno prost sa $\phi(N)$.

4. Izračunaj $d$ postavljanjem $e \cdot d \mod \phi(N) = 1$.

5. Izaberite nasumičnu vrednost $y$ koja je manja i uzajamno prosta sa $N$.


RSA problem se sastoji u pronalaženju $x$ takvog da je $x^e = y$, dok je dat samo podskup informacija u vezi sa $\Pi$, naime promenljive $N$, $e$ i $y$. Kada su $p$ i $q$ veoma veliki, obično se preporučuje da budu veličine 1024 bita, smatra se da je RSA problem Hard. Sada možete videti zašto je to slučaj s obzirom na prethodnu diskusiju.


Jednostavan način za izračunavanje $x$ kada je $x^e \mod N = y \mod N$ je jednostavno izračunavanje $y^d \mod N$. Znamo da je $y^d \mod N = x \mod N$ prema sledećim proračunima:


$$ y^d \mod N = x^{e \cdot d} \mod N = x^{e \cdot d \mod \phi(N)} \mod N = x^{1 \mod \phi(N)} \mod N = x \mod N. $$


Problem je što ne znamo vrednost $d$, jer nije data u problemu. Stoga, ne možemo direktno izračunati $y^d \mod N$ da bismo dobili $x \mod N$.


Međutim, možda ćemo moći indirektno izračunati $d$ iz reda $N$, $\phi(N)$, jer znamo da $e \cdot d \mod \phi(N) = 1 \mod \phi(N)$. Ali prema pretpostavci, problem ne daje vrednost za $\phi(N)$.


Konačno, redosled bi mogao biti izračunat indirektno sa prostim faktorima $p$ i $q$, tako da na kraju možemo izračunati $d$. Ali prema pretpostavci, vrednosti $p$ i $q$ takođe nisu bile dostupne nama.


Strogo govoreći, čak i ako je problem faktorizacije unutar RSA problema Hard, ne možemo dokazati da je i RSA problem takođe Hard. Naime, mogu postojati i drugi načini za rešavanje RSA problema osim faktorizacije. Međutim, generalno je prihvaćeno i pretpostavlja se da, ako je problem faktorizacije unutar RSA problema Hard, da je i sam RSA problem takođe Hard.


Ako je RSA problem zaista Hard, onda proizvodi jednosmernu funkciju sa zamkom. Funkcija ovde je $f(g) = g^e \mod N$. Sa znanjem o $f(g)$, svako bi lako mogao izračunati vrednost $y$ za određeni $g = x$. Međutim, praktično je nemoguće izračunati određenu vrednost $x$ samo na osnovu poznavanja vrednosti $y$ i funkcije $f(g)$. Izuzetak je kada vam je dat komad informacije $d$, zamka. U tom slučaju, možete jednostavno izračunati $y^d$ da biste dobili $x$.


Hajde da prođemo kroz konkretan primer kako bismo ilustrovali RSA problem. Ne mogu odabrati RSA problem koji bi se smatrao Hard pod gore navedenim uslovima, jer bi brojevi bili nezgrapni. Umesto toga, ovaj primer je samo da ilustruje kako RSA problem generalno funkcioniše.


Za početak, pretpostavimo da izaberete dva nasumična prosta broja 13 i 31. Dakle, $p = 13$ i $q = 31$. Proizvod $N$ ova dva prosta broja je jednak 403. Lako možemo izračunati red 403. On je ekvivalentan $(13 - 1) \cdot (31 - 1) = 360$.


Zatim, kako je navedeno u koraku 3 RSA problema, treba da izaberemo broj koji je relativno prost sa 360, veći od 2 i manji od 360. Ne moramo nasumično birati ovu vrednost. Pretpostavimo da izaberemo 103. Ovo je broj relativno prost sa 360 jer je njihov najveći zajednički delilac 1.


Korak 4 sada zahteva da izračunamo vrednost $d$ takvu da $103 \cdot d \mod 360 = 1$. Ovo nije lak zadatak ručno kada je vrednost za $N$ velika. Zahteva da koristimo proceduru koja se zove **prošireni Euklidov algoritam**.


Iako ovde ne prikazujem postupak, on daje vrednost 7 kada je $e = 103$. Možete proveriti da par vrednosti 103 i 7 zaista ispunjava opšti uslov $e \cdot d \mod \phi(n) = 1$ kroz proračune ispod.



- $103 \cdot 7 \mod 360 = 721 \mod 360 = 1 \mod 360$


Važno je napomenuti da, s obzirom na *Propoziciju 4*, znamo da nijedan drugi ceo broj između 1 i 360 za $d$ neće proizvesti rezultat da $103 \cdot d = 1 \mod 360$. Dodatno, propozicija implicira da će izbor drugačije vrednosti za $e$ dati drugačiju jedinstvenu vrednost za $d$.


U koraku 5 RSA problema, moramo odabrati neki pozitivan ceo broj $y$ koji je manji i relativno prost sa 403. Pretpostavimo da postavimo $y = 2^{103}$. Eksponencijacija broja 2 na 103 daje rezultat ispod.



- $2^{103} \mod 403 = 10,141,204,801,825,835,211,973,625,643,008 \mod 403 = 349 \mod 403$


RSA problem u ovom konkretnom primeru je sada sledeći: Dati su vam $N = 403$, $e = 103$, i $y = 349 \mod 403$. Sada morate izračunati $x$ tako da $x^{103} = 349 \mod 403$. To jest, morate pronaći da je originalna vrednost pre potenciranja sa 103 bila 2.


Bilo bi lako (barem za računar) izračunati $x$ ako bismo znali da je $d = 7$. U tom slučaju, mogli biste jednostavno odrediti $x$ kao što je prikazano ispod.



- $x = y^7 \mod 403 = 349^7 \mod 403 = 630,634,881,591,804,949 \mod 403 = 2 \mod 403$


Problem je što vam nije pružena informacija da je $d = 7$. Naravno, mogli biste izračunati $d$ iz činjenice da je $103 \cdot d = 1 \mod 360$. Problem je što vam takođe nije data informacija da je red $N = 360$. Na kraju, mogli biste izračunati red 403 računajući sledeći proizvod: $(p - 1) \cdot (q - 1)$. Ali vam takođe nije rečeno da je $p = 13$ i $q = 31$.


Naravno, računar bi i dalje mogao relativno lako rešiti RSA problem za ovaj primer, jer uključeni prosti brojevi nisu veliki. Ali kada prosti brojevi postanu veoma veliki, suočava se sa praktično nemogućim zadatkom.


Sada smo predstavili RSA problem, skup uslova pod kojima je to Hard, i osnovnu matematiku. Kako bilo šta od ovoga pomaže sa asimetričnom kriptografijom? Konkretno, kako možemo pretvoriti težinu RSA problema pod određenim uslovima u šemu šifrovanja ili šemu digitalnog potpisa?


Jedan pristup je uzeti RSA problem i izgraditi šeme na jednostavan način. Na primer, pretpostavimo da ste generisali skup promenljivih $\Pi$ kao što je opisano u RSA problemu, i osigurajte da su $p$ i $q$ dovoljno veliki. Postavite vaš javni ključ jednako $(N, e)$ i podelite ovu informaciju sa svetom. Kao što je gore opisano, držite vrednosti za $p$, $q$, $\phi(n)$, i $d$ tajnim. U stvari, $d$ je vaš privatni ključ.


Svako ko želi da vam pošalje poruku $m$ koja je element $C_N$ može je jednostavno enkriptovati na sledeći način: $c = m^e \mod N$. (Šifrat $c$ ovde je ekvivalentan vrednosti $y$ u RSA problemu.) Možete lako dekriptovati ovu poruku jednostavno izračunavanjem $c^d \mod N$.


Možda biste pokušali da kreirate šemu digitalnog potpisa na isti način. Pretpostavimo da želite da pošaljete nekome poruku $m$ sa digitalnim potpisom $S$. Mogli biste jednostavno postaviti $S = m^d \mod N$ i poslati par $(m,S)$ primaocu. Svako može verifikovati digitalni potpis samo proverom da li je $S^e \mod N = m \mod N$. Međutim, bilo kojem napadaču bi bilo veoma teško da kreira validan $S$ za poruku, s obzirom na to da ne poseduje $d$.


Nažalost, pretvaranje onoga što je samo po sebi Hard problem, RSA problem, u kriptografski šem nije tako jednostavno. Za jednostavnu šemu enkripcije, možete odabrati samo brojeve koji su uzajamno prosti sa $N$ kao vaše poruke. To nam ne ostavlja mnogo mogućih poruka, svakako ne dovoljno za standardnu komunikaciju. Pored toga, ove poruke moraju biti odabrane nasumično. To se čini pomalo nepraktičnim. Konačno, svaka poruka koja je odabrana dva puta će dati potpuno isti šifrat. Ovo je izuzetno nepoželjno u bilo kojoj šemi enkripcije i ne ispunjava nijedan rigorozan moderan standard sigurnosti u enkripciji.


Problemi postaju još gori za naš jednostavan digitalni potpisni sistem. Kako sada stoje stvari, bilo koji napadač može lako falsifikovati digitalne potpise tako što prvo izabere broj koji je relativno prost sa $N$ kao potpis, a zatim izračuna odgovarajuću originalnu poruku. Ovo očigledno narušava zahtev za egzistencijalnom nefalzifikabilnošću.


Ipak, dodavanjem malo pametne složenosti, RSA problem se može koristiti za kreiranje sigurnog šema za enkripciju javnim ključem, kao i sigurnog šema za digitalni potpis. Nećemo ulaziti u detalje takvih konstrukcija ovde. [4] Važno je, međutim, da ova dodatna složenost ne menja fundamentalni osnovni RSA problem na kojem se ove šeme zasnivaju.



**Beleške:**


[4] Videti, na primer, Jonathan Katz i Yehuda Lindell, _Introduction to Modern Cryptography_, CRC Press (Boca Raton, FL: 2015), str. 410–32 o RSA enkripciji i str. 444–41 za RSA digitalne potpise.




# Završni Deo

<partId>e538fb79-bf28-40cd-a5c3-badf864d8567</partId>


## Recenzije i Ocene

<chapterId>366d6fd0-ceb2-4299-bf37-8c6dfcb681d5</chapterId>

<isCourseReview>true</isCourseReview>

## Završni Ispit

<chapterId>44882d2b-63cd-4fde-8485-f76f14d8b2fe</chapterId>

<isCourseExam>true</isCourseExam>

## Zaključak

<chapterId>f1905f78-8cf7-5031-949a-dfa8b76079b4</chapterId>

<isCourseConclusion>true</isCourseConclusion>
