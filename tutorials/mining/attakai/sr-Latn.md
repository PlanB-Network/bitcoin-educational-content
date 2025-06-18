---
name: Attakaï

description: pretvaranje S9 u sistem za grejanje doma
---

![cover](assets/cover.webp)


# Attakai - omogućava da dom Mining bude moguć i dostupan!


Inicijativa "Attakaï" istražuje Bitcoin Mining koristeći generisanu toplotu. Vodič nudi rešenja kako bi rudari bili pogodni za korišćenje kao radijatori u domovima, pružajući više komfora i uštede energije. Bitcoin automatski prilagođava težinu Mining i nagrađuje rudare za njihov rad. Međutim, koncentracija Hashrate može predstavljati rizike za neutralnost mreže. "Attakaï" pruža praktičan vodič za ekonomično prilagođavanje rudara, omogućavajući učesnicima da smanje svoje račune za struju i budu nagrađeni sa Sats bez KYC.


## Uvod


"Attakaï," što znači "idealna temperatura" na japanskom, naziv je inicijative usmerene na otkrivanje Bitcoin Mining kroz ponovnu upotrebu toplote koju su pokrenuli @ajelexBTC i @BlobOnChain sa Découvre Bitcoin. Ovaj vodič za retrofitting ASIC poslužiće kao osnova za bolje razumevanje Mining, njegovog rada, nedavne istorije i osnovne ekonomije.


### Zašto ponovo koristiti toplotu iz ASIC?


Važno je razumeti odnos između energije i proizvodnje toplote u električnom sistemu.


Za ulaganje od 1 kW električne energije, električni radijator proizvodi 1 kW toplote, ni više ni manje. Novi radijatori nisu efikasniji od tradicionalnih radijatora. Njihova prednost leži u sposobnosti da kontinuirano i ravnomerno raspoređuju toplotu u prostoriji, pružajući veći komfor u poređenju sa tradicionalnim radijatorima koji naizmenično prelaze između visokog grejanja i bez grejanja, čime stvaraju redovne temperaturne varijacije i nelagodnost.


Računar, ili šire gledano elektronska ploča, ne troši energiju za obavljanje proračuna; jednostavno mu je potrebna energija da prolazi kroz njegove komponente kako bi funkcionisao. Potrošnja energije je posledica električnog otpora komponenti, što proizvodi gubitke i tako generiše toplotu, što je poznato kao Džulov efekat.

Neke kompanije su došle na ideju da objedine potrebu za računalnom snagom i potrebama za grejanjem putem radijatora/servera. Ideja je da se serveri kompanije distribuiraju u male jedinice koje bi se mogle postaviti u domove ili kancelarije. Međutim, ova ideja nailazi na nekoliko problema. Potreba za serverima nije povezana sa potrebom za grejanjem, a kompanije ne mogu fleksibilno koristiti računalni kapacitet svojih servera. Takođe postoje ograničenja u širini pojasa koju pojedinci mogu imati. Sva ova ograničenja sprečavaju kompaniju da učini ove skupe instalacije profitabilnim ili da obezbedi stabilnu ponudu online servera bez data centara sposobnih da preuzmu kada grejanje nije potrebno.


> Toplota iz vašeg računara nije uzaludna ako treba da zagrejete svoj dom. Ako koristite električno grejanje tamo gde živite, onda toplota iz vašeg računara nije uzaludna. Košta isto ako generate ovu toplotu sa vašim računarom. Ako imate jeftiniji sistem grejanja od električnog, onda je gubitak samo u razlici u ceni. Ako je leto i koristite klima uređaj, onda je dvostruko.
> Bitcoin Mining treba da se održi tamo gde je jeftinije. Možda će to biti tamo gde je klima Cold i gde je grejanje na struju, gde bi Mining postalo besplatno.

_Kao što je Satoshi Nakamoto rekao 8. avgusta 2010._


Bitcoin i njegov Proof of Work se ističu jer automatski prilagođavaju težinu Mining na osnovu količine računanja koje obavlja cela mreža, ta količina se naziva Hashrate i izražava se u hešovima po sekundi. Danas se procenjuje na 280 Eksahaša po sekundi, ili 280 milijardi milijardi hešova po sekundi. Ovaj Hashrate predstavlja rad i stoga količinu potrošene energije. Što je veći Hashrate, to se težina više povećava, i obrnuto. Tako, Bitcoin Miner može biti aktiviran ili deaktiviran u bilo kom trenutku bez ikakvog uticaja na mrežu, za razliku od radijatora/servera koji bi morali ostati stabilni da bi ponudili svoju uslugu. Miner je nagrađen za obavljeni rad u odnosu na rad drugih, bez obzira koliko mala ta participacija mogla biti.


Ukratko, električni radijator i Bitcoin Miner proizvode po 1 kW toplote za 1 kW potrošene električne energije. Međutim, Miner takođe prima bitkoine kao nagradu. Bez obzira na cenu električne energije, cenu Bitcoin ili konkurenciju aktivnosti Mining na Bitcoin mreži, ekonomski je isplativije grejati se sa Miner nego sa električnim radijatorom.


![Video presentation](https://youtu.be/gKoh44UCSnE)


### Dodata vrednost za Bitcoin


Nećemo ulaziti u detalje operacije Mining ovde (resursi su dostupni na akademiji ako je potrebno). Ono što je važno razumeti je kako Mining doprinosi decentralizaciji Bitcoin. Nekoliko postojećih tehnologija je ingeniozno kombinovano kako bi se oživeo Nakamoto konsenzus. Ovaj konsenzus ekonomski nagrađuje poštene aktere za njihovo učešće u radu Bitcoin mreže, dok obeshrabruje nepoštene aktere. Ovo je jedna od ključnih tačaka koja omogućava mreži da postoji održivo.


Pošteni akteri, oni koji rudare prema pravilima, svi se međusobno takmiče kako bi dobili što veći deo nagrade za proizvodnju novih blokova. Ovaj ekonomski podsticaj prirodno vodi ka obliku centralizacije jer kompanije biraju da se specijalizuju u ovoj unosnoj aktivnosti smanjenjem svojih troškova kroz ekonomiju obima. Ovi industrijski akteri imaju povoljan položaj za kupovinu i održavanje mašina, kao i za pregovaranje o veleprodajnim cenama električne energije.


> U početku bi većina korisnika pokretala mrežne čvorove, ali kako bi mreža rasla preko određene tačke, sve više bi to bilo prepušteno stručnjacima sa server farmama specijalizovanog hardvera. Server farmi bi bilo potrebno da pokrene samo jedan čvor na mreži, a ostatak LAN-a bi se povezivao sa tim jednim čvorom.

_Kao što je Satoshi Nakamoto naveo 2. novembra 2008._


Određeni entiteti drže značajan procenat ukupnog Hashrate u velikim Mining farmama. Možemo primetiti nedavni Cold talas u Sjedinjenim Američkim Državama gde je značajan deo Hashrate bio isključen kako bi se energija preusmerila ka domaćinstvima sa izuzetnom potrebom za električnom energijom. Tokom nekoliko dana, rudari su bili ekonomski podstaknuti da isključe svoje farme, i tako možemo videti ovo izuzetno vreme na Bitcoin Hashrate krivoj.


Ovo pitanje bi moglo postati problematično i predstavljati značajan rizik za neutralnost mreže. Akter koji poseduje više od 51% Hashrate mogao bi lakše cenzurisati transakcije ako to želi. Zato je važno distribuirati Hashrate među više aktera, a ne centralizovanim entitetima koje bi vlada, na primer, lakše mogla zapleniti.


**Ako su rudari raspoređeni širom hiljada, ili čak miliona, domaćinstava širom sveta, postaje veoma komplikovano za državu da preuzme kontrolu nad njima.**


'U fabrici, Miner nije pogodan za korišćenje kao radijator u kućištu, zbog dva glavna problema: prekomerne buke i nedostatka podešavanja. Međutim, ovi problemi se mogu lako rešiti jednostavnim modifikacijama hardvera i softvera, omogućavajući mnogo tiši Miner koji se može konfigurisati i automatizovati kao moderni električni grejači.


**Attakaï je obrazovna inicijativa koja vas uči kako da na najisplativiji način izvršite retrofitting Antminer S9.**


Ovo je odlična prilika da učite kroz praksu. Pored smanjenja računa za struju, za vaše učešće ste nagrađeni besplatnim KYC Sats.


## Poglavlje 1: Vodič za kupovinu polovnog ASIC


U ovom odeljku ćemo diskutovati o najboljim praksama za kupovinu polovnog Bitmain Antminer S9, mašine na kojoj će se zasnivati ovaj vodič za retrofitting radijatora. Ovaj vodič se takođe odnosi na druge ASIC modele jer je to opšti vodič za kupovinu polovnog Mining hardvera.


Antminer S9 je uređaj koji nudi Bitmain od maja 2016. Troši 1323W električne energije i proizvodi 13.5 TH/s. Iako se smatra starim, ostaje odlična opcija za početak Mining. Pošto je proizveden u velikim količinama, lako je pronaći rezervne delove u mnogim regionima sveta. Generalno se može nabaviti peer-to-peer na sajtovima kao što su Ebay ili LeBonCoin, jer ga profesionalni prodavci više ne nude zbog njegove niže konkurentnosti u poređenju sa novijim mašinama. Manje je efikasan od ASIC-a kao što je Antminer S19, predstavljen od marta 2020, ali to ga čini pristupačnim polovnim hardverom i pogodnijim za modifikacije koje ćemo napraviti.


Antminer S9 dolazi u nekoliko varijacija (i, j) koje donose manje izmene na hardveru prve generacije. Ne verujemo da bi ovo trebalo da utiče na vašu odluku o kupovini, i ovaj vodič će raditi za sve te varijacije.


Cena ASIC-ova varira u zavisnosti od mnogih faktora kao što su cena Bitcoin, težina mreže, efikasnost mašine i cena električne energije. Stoga je teško dati tačnu procenu za kupovinu korišćene mašine. U februaru 2023. godine, očekivana cena u Francuskoj generalno se kreće između €100 i €200, ali ove cene mogu brzo da se promene.


![image](assets/guide-achat/1.webp)


Antminer S9 se sastoji od sledećih delova:



- 3 hešborda gde se nalaze čipovi koji proizvode hešing snagu


![image](assets/guide-achat/2.webp)'



- Kontrolna ploča koja uključuje slot za SD karticu, Ethernet port i konektore za hashboardove i ventilatore. Ovo je mozak vašeg ASIC.

![image](assets/guide-achat/3.webp)



- 3 data kablova koji povezuju heš table sa kontrolnom pločom.


![image](assets/guide-achat/4.webp)



- Snaga Supply koja radi na 220V i može se priključiti kao običan kućni aparat.


![image](assets/guide-achat/5.webp)



- 2 ventilatora od 120mm.


![image](assets/guide-achat/6.webp)



- Muški C13 kabl.


![image](assets/guide-achat/7.webp)


Kada kupujete korišćenu mašinu, važno je proveriti da li su svi delovi uključeni i funkcionalni. Tokom Exchange, trebalo bi da zamolite prodavca da uključi mašinu kako biste proverili njeno pravilno funkcionisanje. Važno je proveriti da li se uređaj ispravno uključuje, a zatim proveriti internet konekciju povezivanjem Ethernet kabla i pristupom Bitmain konekciji Interface putem veb pregledača na istoj lokalnoj mreži. Možete pronaći ovu IP adresu Address povezivanjem na vaš internet ruter Interface i traženjem povezanih uređaja. Ovaj Address bi trebalo da ima sledeći format: 192.168.x.x


![image](assets/guide-achat/8.webp)


Takođe, proverite da li podrazumevane kredencijale rade (korisničko ime: root, lozinka: root). Ako podrazumevane kredencijale ne rade, biće potrebno da izvršite resetovanje mašine.


![image](assets/guide-achat/9.webp)


Jednom kada se povežete, trebali biste moći videti status svake hashboarde na kontrolnoj tabli. Ako je Miner povezan sa bazenom, trebali biste videti da sve hashboarde funkcionišu. Važno je napomenuti da rudari prave mnogo buke, što je normalno. Takođe, proverite da li ventilatori funkcionišu ispravno.


Zatim možete ukloniti Mining pool prethodnog vlasnika kako biste kasnije postavili svoj. Ako želite, možete takođe pregledati hashboardove rastavljanjem mašine. Međutim, ovaj korak je složeniji i zahteva više vremena i određene alate. Ako želite da nastavite sa ovim rastavljanjem, možete se obratiti sledećem delu ovog tutorijala koji detaljno objašnjava kako to uraditi. Važno je napomenuti da rudari sakupljaju mnogo Dust i zahtevaju redovno održavanje. Možete posmatrati ovo nakupljanje Dust i kvalitet održavanja rastavljanjem mašine.

Nakon pregleda svih ovih tačaka, možete kupiti svoju mašinu sa visokim stepenom poverenja. Ako ste u nedoumici, obratite se zajednici, a ako vam je potrebna oprema za dovršetak ovog tutorijala, slobodno nam pošaljite poruku.

Da rezimiramo ovaj vodič u jednoj rečenici:


> Ne veruj, proveri.

## Poglavlje 2: Vodič za kupovinu delova za modifikaciju


![image](assets/piece/1.webp)


### Kako transformisati svoj Antminer S9 u tihi i povezani grejač?


Ako posedujete Antminer S9, verovatno znate koliko može biti bučan i glomazan. Međutim, moguće ga je transformisati u tihi i povezani grejač prateći nekoliko jednostavnih koraka. U ovom članku predstavićemo potrebnu opremu za modifikacije, dok će kasniji članak detaljno objasniti korake koje treba pratiti kako biste izvršili ove promene.


### 1. Zamenite ventilatore


Originalni ventilatori Antminer S9 su previše bučni za korišćenje kao grejač. Rešenje je da ih zamenite tišim ventilatorima. Naš tim je testirao nekoliko modela brenda Noctua i izabrao Noctua NF-A14 iPPC-2000 PWM kao najbolji kompromis. Obavezno izaberite 12V verziju ventilatora. Ovaj ventilator od 140mm može proizvesti do 1300W toplote uz održavanje teoretskog nivoa buke od 31 dB. Da biste montirali ove ventilatore od 140mm, biće vam potreban adapter od 140mm na 120mm, koji možete pronaći u DécouvreBitcoin prodavnici. Takođe ćemo dodati zaštitne rešetke od 140mm.


![image](assets/piece/1.webp)

![image](assets/piece/2.webp)

![image](assets/piece/3.webp)


Ventilator Supply je takođe prilično bučan i potrebno ga je zameniti. Preporučujemo Noctua NF-A6x25 PWM. Imajte na umu da konektori Noctua ventilatora nisu isti kao originalni, tako da će vam biti potreban adapter za konektor da ih povežete. Dva bi trebalo da budu dovoljna. Ponovo, obavezno izaberite 12V verziju ventilatora.


![image](assets/piece/4.webp)

![image](assets/piece/5.webp)


### 2. Dodajte WIFI/Ethernet most


Umesto korišćenja Ethernet kabla, možete povezati svoj Antminer na WIFI dodavanjem WIFI/Ethernet mosta. Odabrali smo vonets vap11g-300 jer vam omogućava lako preuzimanje WIFI signala sa vaše Internet kutije i prenos do vašeg Antminera putem Ethernet-a bez kreiranja podmreže. Ako imate električarske veštine, možete ga napajati direktno sa Antminerovim napajanjem Supply bez potrebe za dodavanjem USB punjača. Za ovo će vam biti potreban ženski 5.5mmx2.1mm džek.


![image](assets/piece/6.webp)

![image](assets/piece/7.webp)


### 3. Opcionalno: Dodajte pametnu utičnicu


Ako želite da uključite/isključite svoj Antminer sa pametnog telefona i pratite njegovu potrošnju energije, možete dodati pametnu utičnicu. Testirali smo ANTELA utičnicu u verziji od 16A, kompatibilnu sa smartlife aplikacijom. Ova pametna utičnica vam omogućava da proverite dnevnu i mesečnu potrošnju energije i povezuje se direktno na vaš Internet ruter putem WIFI-ja.

![image](assets/piece/8.webp)


**Lista opreme i linkovi:**



- 2X 3D adapter komad 140mm na 120mm
- 2X NF-A14 iPPC-2000 PWM [link](https://www.amazon.fr/Noctua-nf-polarized-A14-industrialppc-PWM-2000/dp/B00KESSUDW)
- 2X 140mm fan grilles [link](https://www.amazon.fr/dp/B06XD4FTSQ)
- Noctua NF-A6x25 PWM [link](https://www.amazon.fr/Noctua-nf-a6-25-PWM-Ventilateur-Marron/dp/B00VXTANZ4)
- Električarov šećer 2.5mm2 [link](https://www.amazon.fr/Legrand-LEG98433-Borne-raccordement-Nylbloc/dp/B00BBHXLYS)
- Vonets vap11g-300 [link](https://www.amazon.fr/Vonets-VAP11G-300-Bridge-convertit-Ethernet/dp/B014SK2H6W)


## Poglavlje 3 - TUTORIJAL: Kako pretvoriti Miner u grejač?


Ako ste vešti u "uradi sam" projektima i želite da pretvorite Miner u grejač, ovaj vodič je za vas. Želimo da vas upozorimo da modifikacija elektronskog uređaja može predstavljati električne i požarne rizike. Neophodno je preduzeti sve potrebne mere predostrožnosti kako biste izbegli bilo kakvu štetu ili povredu.

Izvan fabrike, Miner nije baš upotrebljiv kao radijator u kući jer je previše bučan i nije podesiv. Međutim, moguće je napraviti jednostavne modifikacije kako bi se ovi problemi rešili.


**Napomena:** Neophodno je prethodno instalirati Braiins OS+ na vaš Miner ili bilo koji drugi softver koji može smanjiti performanse vaše mašine. Ova mera je ključna jer ćemo, kako bismo smanjili buku, instalirati **manje moćne ventilatore koji mogu raspršiti manje toplote**.


### Potrebni materijali



- 2 komada 3D adapter 140mm na 120mm
- 2 Noctua NF-A14 iPPC-2000 PWM ventilatora
- 2 rešetke za ventilatore od 140mm
- 1 Noctua NF-A6x25 PWM ventilator
- električarska kocka 2.5mm²
- Vonets VAP11G-300
- Opcionalno: ANTELA smart plug


### Zamena ventilatora


Počećemo zamenom ventilatora Supply.


**Napomena**: Prvo i najvažnije, pre nego što počnete, obavezno isključite svoj Miner kako biste izbegli bilo kakav rizik od strujnog udara.


![image](assets/hardware/1.webp)


Počećemo sa zamenom ventilatora Supply.


Prvo, uklonite 6 šrafova sa strane kućišta koji ga drže zatvorenim. Kada su šrafovi uklonjeni, pažljivo otvorite kućište da biste uklonili plastični poklopac koji štiti komponente.


![image](assets/hardware/2.webp)

![image](assets/hardware/3.webp)'

Zatim, vreme je da uklonite originalni ventilator, pazeći da ne oštetite druge komponente. Da biste to uradili, uklonite šrafove koji ga drže na mestu i pažljivo odlepite beli lepak oko konektora. Važno je postupati pažljivo kako biste izbegli oštećenje žica ili konektora.

![image](assets/hardware/4.webp)


Kada se originalni ventilator ukloni, primetićete da konektori novog Noctua ventilatora ne odgovaraju onima originalnog ventilatora. Naime, novi ventilator ima 3 žice, uključujući žutu žicu koja omogućava kontrolu brzine. Međutim, ova žica neće biti korišćena u ovom specifičnom slučaju. Za povezivanje novog ventilatora preporučuje se korišćenje specijalnog adaptera. Međutim, važno je napomenuti da ovaj adapter ponekad može biti teško pronaći.


![image](assets/hardware/5.webp)


Ako nemate ovaj adapter, i dalje možete nastaviti sa povezivanjem novog ventilatora koristeći žičanu maticu. Da biste to uradili, potrebno je da isečete kablove starog i novog ventilatora.


![image](assets/hardware/6.webp)

![image](assets/hardware/7.webp)


Na novom ventilatoru, koristite rezač i pažljivo isecite konture glavnog omotača na 1cm bez sečenja omotača kablova ispod.


![image](assets/hardware/8.webp)


Zatim, povlačenjem glavnog omotača prema dole, isecite omotače crvenog i crnog kabla na isti način kao ranije. A žuti kabl isecite ravno.


![image](assets/hardware/9.webp)


Na starom ventilatoru, delikatnije je preseći glavni omotač bez oštećenja omotača crvene i crne žice. Za to smo koristili iglu koju smo provukli između glavnog omotača i crvene i crne žice.


![image](assets/hardware/10.webp)

![image](assets/hardware/11.webp)


Kada su crvene i crne žice izložene, pažljivo isecite omotače kako ne biste oštetili električne žice.


![image](assets/hardware/12.webp)


Zatim, povežite kablove pomoću žičane kapice, crnu žicu sa crnom i crvenu žicu sa crvenom. Možete dodati i izolir traku.


![image](assets/hardware/13.webp)

![image](assets/hardware/14.webp)


Kada se uspostavi veza, vreme je da instalirate novi Noctua ventilator sa rešetkom i starim šrafovima, novi šrafovi koji su u kutiji će se ponovo koristiti kasnije. Uverite se da ga postavite sa ispravnom orijentacijom. Primetićete strelicu na jednoj strani ventilatora, koja pokazuje pravac protoka vazduha. Važno je postaviti ventilator tako da ova strelica pokazuje ka unutrašnjosti kućišta. Zatim, ponovo povežite ventilator.

![image](assets/hardware/15.webp)

![image](assets/hardware/16.webp)


**Opcionalno:** Ako ste vešti sa strujom, možete direktno dodati ženski 5.5mm džek konektor na 12V izlaz za napajanje, što će vam omogućiti da direktno napajate Vonet Wi-Fi most. Međutim, ako niste sigurni u svoje električne veštine, najbolje je koristiti USB konektor sa punjačem za pametni telefon kako biste izbegli rizik od kratkog spoja ili električnog oštećenja.


![image](assets/hardware/17.webp)


Kada su veze uspostavljene, obavezno postavite plastični poklopac preko plastičnog kućišta, a ne unutra.


![image](assets/hardware/18.webp)


Na kraju, vratite poklopac kućišta na mesto i zavrnite 6 šrafova sa strane kako biste sve čvrsto pričvrstili. I eto, vaše Supply kućište sada je opremljeno novim ventilatorom.


### Zamena 2 glavna ventilatora


1. Prvo, isključite ventilatore iz struje i odvrnite ih.

![image](assets/hardware/19.webp)


2. Konektori novih Noctua ventilatora ne odgovaraju originalnim, ali ne paničite! Uzmite svoj rezač i pažljivo isecite male plastične jezičke kako bi konektori savršeno odgovarali vašem Miner.


![image](assets/hardware/20.webp)

![image](assets/hardware/21.webp)


3. Vreme je da instalirate 3D delove!

Pričvrstite ih na obe strane Miner koristeći šrafove koje ste uklonili sa ventilatora. Zavrnite dok glava šrafa ne uđe u 3D deo i dok nije sigurno pričvršćen. Pazite da ne zategnete previše, jer biste mogli deformisati deo i jedan od šrafova bi mogao dodirnuti kondenzator! Zatim pažljivo isecite male plastične jezičke tako da konektori savršeno odgovaraju vašem Miner.


![image](assets/hardware/22.webp)


4. Sada pređimo na navijače.

Pričvrstite ih na 3D delove koristeći šrafove koji su obezbeđeni u kutiji. Obratite pažnju na pravac protoka vazduha, strelice na stranama ventilatora će pokazati pravac koji treba pratiti. Idite od strane sa Ethernet portom ka drugoj strani. Pogledajte fotografiju ispod.


![image](assets/hardware/23.webp)

![image](assets/hardware/24.webp)

![image](assets/hardware/25.webp)


5. Poslednji korak: priključite ventilatore i pričvrstite rešetke na vrh pomoću neiskorišćenih šrafova iz kutije ventilatora. Imate samo 4, ali 2 po rešetki u suprotnim uglovima će biti dovoljna. Takođe možete potražiti druge slične šrafove u prodavnici alata ako je potrebno.


![image](assets/hardware/26.webp)

![image](assets/hardware/27.webp)


Dok čekate da budete u mogućnosti da ponudite atraktivnije kućište za vaš novi grejač, možete pričvrstiti kućište i napajanje Supply zajedno sa električarskim vezicama.


![image](assets/hardware/28.webp)


I za završni dodir, povežite Vonet most na Ethernet port na njegovom napajanju Supply. Ako to već niste učinili, možete pratiti ovaj vodič da postavite svoj most.


![image](assets/hardware/29.webp)


I eto ga, čestitamo! Upravo ste zamenili ceo mehanički deo vašeg Miner. Sada bi trebalo da čujete mnogo manje buke.


## Poglavlje 4 - Modifikacija softvera - Resetovanje Antminer S9


**Serija članaka koju predlažu BlobOnChain & Ajelex - 15/02/2023**


### Resetujte putem dugmeta "Reset"


Ova metoda se može primeniti u roku od 10 minuta nakon pokretanja Miner.


Nakon što uključite Miner na 2 minuta, pritisnite dugme "Reset" na 5 sekundi, a zatim ga otpustite. Miner će biti vraćen na fabrička podešavanja u roku od 4 minuta i automatski će se ponovo pokrenuti (nema potrebe da ga isključujete).


![image](assets/software/1.webp)


Vratite putem web stranice


Prijavite se na korisnika Interface vašeg Miner, kliknite na "Upgrade" >> "Perform a reset", zatim kliknite "OK" u iskačućem prozoru.


### Originalni operativni sistem


Za ovaj deo, pretpostavićemo da mašina radi, funkcioniše, i da je njen originalni operativni sistem instaliran. Ukratko ćemo pogledati Interface originalnog operativnog sistema koji nudi Bitmain.


Prvo, povežite se sa svojom mašinom putem lokalne mreže:


![image](assets/software/2.webp)


Jednom kada ste na stranici za prijavu, potrebno je da se prijavite na ASIC koristeći podrazumevane akreditive:



- korisničko ime: root
- lozinka: root


**Kako resetovati ako podrazumevana lozinka ne radi?**


Glavni operativni sistem je relativno osnovni. Sa 4 kartice: Sistem, Miner Konfiguracija, Miner Status, Mreža. U kartici Miner Konfiguracija, možete konfigurisati do 3 Mining bazena.


![image](assets/software/3.webp)


Na kartici Status Miner, možete posmatrati različite informacije o trenutnom radu ASIC. Hashrate izražen u GH/s, detaljnije informacije o bazenu, kao i detalji o statusu svake hashboard ploče i brzini ventilatora u obrtajima/minuti.


![image](assets/software/4.webp)


### Braiins OS+


Sada ćemo proučiti softver za ASIC-e Braiins OS+ (https://braiins.com/os/plus). Softver je razvijen od strane kompanije [Braiins](https://braiins.com/), koja je matična kompanija Mining pool Braiins Pool-a (https://braiins.com/pool). Ovaj Mining pool trenutno ima 4,39% globalnog Hashrate u trenutku pisanja ovih redova. Kompanija sa sedištem u Pragu ranije je bila poznata kao Slushpool i prvi je Mining pool koji je započeo u novembru 2010. [Ovde](https://Mempool.space/Mining/pool/braiinspool) možete pronaći ažurirane Hashrate i statistike dominacije pool-a.


Danas kompanija, sa svojim raznovrsnim aktivnostima, nudi alate za studiju profitabilnosti za Mining (https://insights.braiins.com/en), rešenja za upravljanje farmama Mining paralelno sa svojom pool aktivnošću, i svoj softver za optimizaciju za ASIC-e. Takođe nudi Mining koristeći novi Stratum V2 protokol (https://braiins.com/Bitcoin-Mining-stack-upgrade).


Stoga ćemo detaljnije proučiti rad Bitmain uređaja, koji su trenutno jedini kompatibilni modeli:



- S19, S19 Pro, S19j, S19j Pro, T19,



- 17, S17 Pro, S17+, S17e, T17, T17+, T17e & S9 [i, j]


Braiins OS softver se može lako instalirati na sve gore pomenute mašine. Omogućiće precizniju kontrolu mašine dozvoljavajući overclocking ili underclocking. Takođe omogućava fino podešavanje frekvencije svakog čipa putem automatske optimizacije koja se zove autotuning. Pošto je svaki hashing čip malo drugačiji zbog svog proizvodnog procesa, softver testira optimalnu frekvenciju za svaki čip kako bi postigao maksimalnu efikasnost (W/THs). Softver tvrdi da može postići performanse koje su 25% veće od originalnih. Prema našim merenjima, moguće je postići ove rezultate.


## Instalacija Braiins OS+


Postoji nekoliko načina za instalaciju Braiins OS+ na ASIC. Možete se pozvati na ovaj vodič, kao i na zvaničnu dokumentaciju od Braiins i video tutorijale.

Instaliranje Braiins OS+ direktno na memoriju Antminer uređaja


Naučite kako lako instalirati Braiins OS+ direktno na memoriju vašeg Antminera koristeći BOS toolbox, zamenjujući originalni operativni sistem, kroz detaljne korake ispod. Ako želite da zadržite originalni OS paralelno, možete instalirati Braiins OS+ na SD karticu.


1. Uključite svoj Antminer i povežite ga sa svojim internet box-om.

2. Preuzmi BOS toolbox Windows / Linux.

3. Raspakujte preuzetu datoteku i otvorite bos-toolbox.bat datoteku, izaberite jezik, i nakon trenutka videćete ovaj prozor:

![image](assets/software/5.webp)

4. Bos toolbox će vam omogućiti da lako pronađete IP Address vašeg Antminera i instalirate Braiins OS+. Ako već znate IP Address vaše mašine, možete preskočiti na korak 8. U suprotnom, idite na karticu za skeniranje.

![image](assets/software/6.webp)

5. Obično, na kućnim mrežama, IP opseg Address je između 192.168.1.1 i 192.168.1.255, pa unesite "192.168.1.0/24" u polje za IP opseg. Ako je vaša mreža drugačija, molimo promenite ove adrese. Zatim kliknite na "Start".

6. Pažnja, ako Antminer ima lozinku, detekcija neće raditi. Ako je to slučaj, najjednostavnije rešenje je izvršiti fabričko resetovanje.

7. Trebalo bi da vidite sve Antminere na vašoj mreži, ovde je IP Address 192.168.1.37.

![image](assets/software/7.webp)

8. Kliknite na Back, zatim idite na karticu install, unesite prethodno pronađeni IP Address u polje Miner(s) i "admin" (ili "root") u polje Password, što je podrazumevana lozinka, zatim kliknite na "Start".

Ako instalacija ne funkcioniše sa "admin" ili "root" kao lozinkom, možda će biti potrebno izvršiti fabričko resetovanje i pokušati ponovo.

![image](assets/software/8.webp)

9. Nakon nekoliko trenutaka, vaš Antminer će se restartovati i moći ćete pristupiti Braiins OS+ Interface na IP Address u pitanju, ovde 192.168.1.37, direktno u Address traci vašeg pregledača. Podrazumevano korisničko ime je "root" i nema podrazumevane lozinke.

![image](assets/software/9.webp)

![image](assets/software/10.webp)


Instaliranje Braiins OS+ na SD karticu je druga metoda, koristi originalni Interface vašeg Antminera. Ova metoda radi za mašine sa operativnim sistemom koji datira pre 2019.


### Antminer Interface


1. Preuzmite novi operativni sistem koji treba instalirati.

2. Kao u prethodnom odeljku, povežite se sa vašom mašinom preko lokalne mreže.

3. Idite na karticu Sistem, a zatim na Nadogradnja.

4. Učitajte datoteku koju ste preuzeli i flešujte sliku.


![image](assets/software/11.webp)


### Micro SD Kartica


Drugi metod vam omogućava korišćenje micro SD kartice. Ovaj metod funkcioniše samo sa mašinama koje imaju operativni sistem iz perioda posle 2019. godine.


1. Preuzmite novi operativni sistem koji treba instalirati.

2. Prebacite preuzetu sliku na micro SD karticu. Za ovo možete koristiti Etcher. Jednostavno kopiranje fajla na micro SD karticu neće raditi.

3. Ako posedujete Antminer S9 i njegove varijacije (S9i, S9j), biće potrebno da podesite džampere kako biste naterali vaš ASIC da se pokrene sa fajla na micro SD kartici umesto sa NAND-a. Ako imate drugačiji model, možete preskočiti na deo 4. Džamperi se nalaze na kontrolnoj ploči na gornjem delu ASIC, blizu Ethernet porta. Biće potrebno da je uklonite tako što ćete je povući unazad. Kada je pozicija džampera izmenjena kao što je prikazano na slikama ispod BOOT FROM SD, možete ponovo umetnuti kontrolnu ploču i ponovo povezati S9.

![image](assets/software/12.webp)

![image](assets/software/13.webp)

4. Ubacite micro SD karticu u ASIC.

5. Pokrenite ASIC. Ako je korišćena verzija za automatsku instalaciju, novi operativni sistem će biti instaliran automatski. Instalacija je završena kada obe LED diode svetle istovremeno. Možete ponovo pokrenuti ASIC i ukloniti micro SD karticu. Ako je preuzeta druga verzija, potrebno je ostaviti micro SD karticu unutar ASIC.


Za više informacija o instalaciji, možete posetiti ovaj deo Braiins vebsajta.


## Interface


Trebaće da se povežete sa vašim ASIC na sličan način. Koristeći lokalni IP Address vašeg uređaja na vašoj mreži putem pregledača.


Podrazumevane akreditive su iste kao originalni operativni sistem.



- korisničko ime: root
- lozinka: root


Bićete dočekani od strane Brains OS+ kontrolne table.


### Kontrolna tabla


![image](assets/software/14.webp)


Na ovoj prvoj stranici, možete posmatrati performanse vaše mašine u realnom vremenu.



- Tri grafikona u realnom vremenu koji prikazuju temperaturu, Hashrate i opšte stanje vaše mašine.
- Sa desne strane, pravi Hashrate, prosečna temperatura čipa, procenjena efikasnost u W/THs, i potrošnja energije.
- Ispod, brzina ventilatora u procentima od maksimalne brzine i broj obrtaja u minuti.


![image](assets/software/15.webp)



- Dalje u tekstu, naći ćete detaljan prikaz svake hashboard ploče. Prosečna temperatura ploče i čipova koje sadrži, napon i frekvencija.
- Detalji o aktivnim Mining bazenima u Pools.
- Status autotuninga u Tuner Status.
- Sa desne strane, detalji o akcijama prenetim u bazen.


### Konfiguracija


![image](assets/software/16.webp)


### Sistem


![image](assets/software/17.webp)


### Brze radnje


![image](assets/software/18.webp)


Konfigurisanje bazena


Može se zamisliti Mining pool kao poljoprivrednu zadrugu. Poljoprivrednici udružuju svoju proizvodnju kako bi smanjili varijansu Supply i potražnje i tako ostvarili stabilniji prihod za svoje poslovanje. Mining pool funkcioniše na isti način, a sirovina koja se udružuje su heševi. Zapravo, otkriće jednog validnog Hash omogućava kreiranje bloka i time osvajanje coinbase-a ili nagrade, trenutno 6.25 BTC plus transakcione naknade uključene u blok. Ako kopate sami, bićete nagrađeni samo kada pronađete blok. U konkurenciji sa svim ostalim rudarima na planeti, imali biste vrlo male šanse da osvojite ovu veliku lutriju i još uvek biste morali da platite naknade povezane sa korišćenjem vašeg Miner bez ikakve garancije uspeha. Mining rešava Address ovaj problem udruživanjem računarske snage nekoliko (hiljada) rudara i deljenjem njihovih nagrada na osnovu procenta učešća u Hashrate bazenu kada se pronađe blok. Da biste vizualizovali svoje šanse za Mining blok samostalno, možete koristiti ovaj alat. Unoseći informacije o Antminer S9, možemo videti da su šanse za pronalaženje Hash koji omogućava kreiranje bloka 1 u 24,777,849 za svaki blok ili 1 u 172,068 dnevno. U proseku (sa konstantnim Hashrate i težinom), bilo bi potrebno 471 godina da se pronađe blok.


Međutim, pošto je sve u Bitcoin verovatnoća, ponekad se dešava da solo rudari budu nagrađeni za preuzimanje ovog rizika: Solo Bitcoin Miner Rešava Blok Sa Hash Brzinom od Samo 10 TH/s, Pobijajući Izuzetno Neverovatne Izglede – Decrypt


Ako volite da kockate, možete pokušati, ali naš vodič se neće fokusirati u tom pravcu. Umesto toga, koncentrisaćemo se na Mining pool koji najbolje odgovara našim potrebama za kreiranje sistema grejanja.

Razmatranja koja treba imati pri odabiru Mining pool su rad nagrada bazena, koje mogu biti različite, kao i minimalni iznos pre nego što se nagrade mogu povući na Address. Na primer, Braiins, koji nudi softver o kojem ovde govorimo, takođe nudi bazen. Ovaj bazen ima sistem nagrađivanja nazvan "Score" koji podstiče rudare da rudare duže vremenske periode. Učešće uključuje faktor vremena aktivnosti koji se izražava sa "scoring Hashrate". U našem slučaju, gde želimo sistem grejanja koji se može uključiti samo na nekoliko minuta, ovo nije idealan sistem nagrađivanja. Preferiramo sistem nagrađivanja koji nam daje jednaku nagradu za svako učešće. Pored toga, minimalni iznos za povlačenje za Braiins Pool je 100,000 Sats i On-Chain. Tako gubimo neke Sats na transakcione naknade i deo naše nagrade može biti zaključan ako ne rudimo dovoljno tokom zime.


Model nagrađivanja koji nas zanima je PPS, što znači "plaćanje po deonici". To znači da će Miner dobiti nagradu za svaku validnu deonicu. Postoji i varijanta ovog sistema, FPPS (Full Pay Per Share), koja ne samo da deli nagradu za coinbase, već i transakcione naknade uključene u blok. Mining bazeni koje preporučujemo za povezivanje vašeg Mining/grejanja su Linecoin Pool (FPPS) i Nicehash (PPS).



- Nicehash: Prednost Nicehash-a je što se povlačenje može izvršiti koristeći Lightning uz minimalne naknade. Pored toga, minimalni iznos za povlačenje je 2000 Sats. Nedostatak je što Nicehash koristi svoj Hashrate za najprofitabilniji Blockchain, bez stvarnog davanja kontrole korisniku, tako da možda neće nužno učestvovati u Bitcoin Hashrate.



- Linecoin: Prednost Linecoina je broj funkcija koje nudi, kao što su detaljna kontrolna tabla, mogućnost povlačenja sa Paynym (BIP 47) radi bolje zaštite privatnosti, i integracija Telegram bota kao i direktno konfigurisane automatizacije u mobilnoj aplikaciji. Ovaj bazen kopa samo Bitcoin blokove, ali minimalni iznos za povlačenje ostaje visok na 100.000 Sats. Detaljnije ćemo ispitati Interface jednog od ovih bazena u budućem članku.


Da biste konfigurisali pool u Braiins 0S+, potrebno je da kreirate nalog u jednom od pool-ova po vašem izboru. Ovde ćemo uzeti primer Linecoin:


![image](assets/software/19.webp)


Kada je vaš nalog kreiran, kliknite na Connect To Pool


Zatim kopirajte Stratum Address kao i vaše korisničko ime:


![image](assets/software/20.webp)


Sada se možete vratiti na Braiins OS+ Interface da unesete ove akreditive. Polje za lozinku možete ostaviti prazno.


![image](assets/software/21.webp)


### Overclocking i Underclocking


Overclocking i autotuning oba uključuju podešavanje frekvencija na hashing karticama kako bi se poboljšao ASIC učinak. Razlika između njih leži u složenosti ovih podešavanja frekvencija.


**Overclocking** je jednostavna prilagodba koja uključuje povećanje frekvencije na hashing karticama kako bi se povećala Hash stopa mašine. S druge strane, underclocking uključuje smanjenje frekvencije takta integrisanog kola ispod njegove nominalne frekvencije. Smanjenjem frekvencije takta ASIC putem underclockinga, smanjuje se i toplota koju generiše hardver. Ovo omogućava smanjenje brzine ventilatora potrebnih za hlađenje ASIC, jer ne moraju raditi kao Hard da bi održali odgovarajuću temperaturu. Smanjenjem brzine ventilatora, smanjuje se i buka koju generiše ASIC. Ovo može biti posebno korisno za korisnike koji koriste ASIC kod kuće i žele minimizirati buku koju uzrokuje Mining hardver.


Važno je napomenuti da underclocking može dovesti do smanjenja performansi ASIC, tako da je važno pronaći dobar balans između performansi i buke.


Braiins OS+ podržava overklokovanje, underklokovanje ASIC-ova i autotuning. Omogućava korisnicima da fleksibilno podešavaju frekvenciju rada svog hardvera kako bi maksimizirali performanse ili uštedeli energiju prema svojim preferencijama.


### Autotuning


Pre 2018. godine, rudari su imali dva načina da steknu prednost u svojoj aktivnosti: pronalaženje električne energije po razumnoj ceni i kupovina efikasnijeg hardvera. Međutim, 2018. godine, otkriven je novi napredak u oblasti Mining softvera i firmvera, nazvan AsicBoost. Ova tehnika omogućava rudarima da smanje svoje troškove za približno 13% modifikovanjem firmvera koji radi na njihovim uređajima.

Danas postoji novi napredak u softverskom i firmverskom sektoru Mining pod nazivom autotuning, koji nudi još veću prednost od AsicBoost-a. ASIC-i se sastoje od mnogo malih kompjuterskih čipova koji obavljaju heširanje. Ovi čipovi su napravljeni od silicijuma, istog elementa koji se široko koristi u poluprovodnicima i drugim mikroelektronskim komponentama. Ključna stvar ovde je da nisu svi silicijumski čipovi identični - svaki može malo varirati u svojim električnim svojstvima. Proizvođači hardvera to znaju i objavljuju specifikacije performansi svojih Mining mašina na osnovu donje granice njihovih tolerancija. Drugim rečima, proizvođači znaju frekvenciju koja najbolje radi za prosečne čipove i koriste ovu frekvenciju jednako za sve čipove u mašini.


Ovo postavlja gornju granicu na stopu Hash koju mašina može imati. Autotuning je proces u kojem algoritmi procenjuju optimalne frekvencije za hashiranje po čipu, umesto da tretiraju celu mašinu kao jednu jedinicu. To znači da će čip višeg kvaliteta koji može da izvrši više hashova po sekundi dobiti višu frekvenciju, dok će čip nižeg kvaliteta koji može da izvrši relativno manje hashova dobiti nižu frekvenciju. Autotuning na nivou čipa je suštinski način da se optimizuje performansa ASIC putem softvera i firmvera koji se na njemu pokreću.


Krajnji rezultat je veća stopa Hash po vatu električne energije, što znači veće profitne marže za rudare. Razlog zašto mašine nisu distribuirane sa ovom vrstom softvera je taj što je varijansa mašina nepoželjna, jer kupci žele da znaju tačno šta dobijaju, i stoga je loša ideja za proizvođače da prodaju proizvod koji nema dosledne i predvidljive performanse od jedne mašine do druge. Pored toga, autotuning na nivou čipa zahteva značajne razvojne resurse, jer je složen za implementaciju. Proizvođači već troše mnogo resursa na razvoj sopstvenih firmvera. Postoje softverska rešenja koja omogućavaju autotuning, kao što je Braiins OS+. Pored poboljšanja performansi ASIC do 20%.


Ovaj vodič je kreirao DecouvreBitcoin, više informacija na MIN201 - zasluge Jim i Ajelex