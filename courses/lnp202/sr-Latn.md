---
name: Postavljanje vašeg prvog Lightning čvora
goal: Razumevanje, instalacija, konfiguracija i korišćenje Lightning čvora
objectives: 


  - Razumeti ulogu i svrhu Lightning čvora.
  - Identifikujte različita softverska rešenja dostupna.
  - Instalirajte i konfigurišite Lightning čvor (LND).
  - Povežite račun troškova.
  - Znajte rizike korišćenja Lightning čvora.


---

# Vaš prvi korak ka autonomiji na Lightningu



Već ste nabavili svoj prvi sats, osigurali sredstva za samostalno čuvanje i postavili Bitcoin čvor kako biste bili suvereni u korišćenju on-chain. Sledeći korak je sticanje iste autonomije na Lightning-u: upravo je to cilj ovog kursa.



LNP202 je namenjen korisnicima srednjeg nivoa i vodi vas korak-po-korak kroz postavljanje vašeg prvog Lightning čvora, bez naprednih tehničkih veština.



Naučićete kako da instalirate LND na Umbrel, otvorite i upravljate svojim kanalima, nadgledate svoj čvor i povežete mobilni wallet, kako biste mogli uživati u iskustvu uporedivom sa onim kod kustodijalnog wallet, dok zadržavate potpunu kontrolu nad svojim sredstvima.



+++


# Uvod


<partId>5e77c17a-0853-4f36-a988-1b4a956f49e4</partId>



## Pregled kursa


<chapterId>e0871abf-af6d-4221-9389-1a996aea9b79</chapterId>



LNP202 je praktičan kurs osmišljen da vas učini autonomnim na Lightning-u upravljanjem sopstvenim čvorom. Cilj je jednostavan: počnite sa Bitcoin čvorom koji je već postavljen, implementirajte LND na Umbrel, pravilno ga osigurajte, otvorite i upravljajte svojim prvim kanalima, a zatim koristite svoj čvor svakodnevno sa mobilnog wallet. Ovaj kurs pretpostavlja da ste već pohađali BTC 202, jer pretpostavljam da je vaš Bitcoin čvor na Umbrel postavljen i sinhronizovan. Nećemo se vraćati na to kako postaviti Bitcoin čvor ovde.



https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426

Za bolje razumevanje unutrašnjih mehanizama Lightning-a, kurs LNP 201 je takođe veoma preporučen, iako nije preduslov za ovaj kurs:



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

U prvom delu ovog kursa LNP202, pogledaćemo šta zapravo predstavlja Lightning čvor, kako se razlikuje od jednostavnog wallet, i zašto je upravljanje ličnim čvorom jedini način da koristite Lightning bez delegiranja vašeg sats pouzdanom trećem licu. Ovaj deo se završava strateškim izborom: koje rešenje je pravo za vas, od najjednostavnijih pristupa do klasičnog Lightning čvora, onog koji ćemo implementirati u ovom kursu.



U drugom delu kursa, instaliraćete LND na Umbrel, a zatim postaviti elemente koji sprečavaju najskuplje greške: realističnu strategiju bekapa i zaštitu protiv varanja putem osmatračnice. Kada su ovi osnovni elementi postavljeni, otvorićete svoj prvi kanal, kako biste mogli početi sa plaćanjem na Lightning-u koristeći sopstvenu infrastrukturu.



Dakle, vidite: u ovom kursu LNP202, postavićemo Lightning čvor u plug-and-play režimu preko Umbrel, umesto klasičnog pristupa putem komandne linije, kako bismo ga učinili pogodnim za korisnike srednjeg nivoa. Ako više volite instalaciju putem komandne linije, preporučujem da pratite tutorijal ispod. Drugi, napredniji kursevi usmereni na komandnu liniju su takođe u pripremi.



https://planb.academy/tutorials/node/lightning-network/lightning-network-daemon-linux-59d777e9-72c8-4b32-8c50-e86cdae8f2f9

Deo 3 će vas zatim odvesti od čvora koji radi do onog koji znate kako da kontrolišete. Počećete određivanjem vašeg profila operatera Lightning čvora (potrošač, trgovac ili ruter), zatim ćete se upoznati sa kompletnim softverskim paketom za upravljanje, kako biste pratili svoje kanale i delovali uredno na svojoj topologiji. Na kraju, bavićete se veoma važnom tačkom Lightning-a: kako dobiti dolaznu likvidnost, bilo putem plaćenih ili kooperativnih rešenja.



Deo 4 će se fokusirati na svakodnevnu upotrebu. Postavićete vezu između vašeg čvora i mobilnog korisnika, tako da možete plaćati i naplaćivati jednostavno sa svog pametnog telefona, bez odricanja od samostalnog čuvanja. Prvo ćemo pogledati mrežni pristup putem *Tailscale*, zatim protokolarni pristup putem *Nostr Wallet Connect*, sa njihovim odgovarajućim prednostima i kompromisima. Kurs će se završiti poslednjim poglavljem koje će vam dati prave navike za održavanje vašeg samostalnog čuvanja, kako operativno tako i pedagoški.



Ako pratite ovaj LNP202 kurs redosledom, na kraju ćete imati kompletnu konfiguraciju za vaš Lightning čvor, funkcionalnu za svakodnevnu upotrebu i, iznad svega, pod kontrolom.




## Razumevanje Lightning čvorova


<chapterId>8275dfd8-7a72-48cc-bf7f-bc2a46063003</chapterId>



Pre nego što pokrenete svoj čvor, ovo poglavlje ukratko pregledava osnovnu teoriju iza [Lightning Network](https://planb.academy/resources/glossary/lightning-network). Zaista je važno razumeti mehanizme koji su uključeni, jer će vam to omogućiti da identifikujete rizike i usvojite dobre prakse kako biste ih ograničili. Neću ulaziti u detalje ovde, međutim, jer to nije glavni cilj ovog kursa. Ako želite dublje da istražite temu, toplo preporučujem da konsultujete Fanis Michalakisov kurs LNP 201, koji je referenca u ovoj oblasti:



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

### Šta je Lightning čvor?



Hajde da se vratimo osnovama: pre nego što definišemo šta je čvor, moramo razumeti šta je Lightning Network. To je protokol najvišeg sloja, izgrađen na vrhu Bitcoin, dizajniran da omogući [vanlančane](https://planb.academy/resources/glossary/offchain) BTC transakcije koje su brze (sa skoro trenutnom finalnošću) i generalno jeftine. "Vanlančano" znači da transakcije obavljene na Lightning-u nisu namenjene da se pojave na glavnom Bitcoin [blockchain-u](https://planb.academy/resources/glossary/blockchain). Lightning je takođe delimičan odgovor na sve veću upotrebu Bitcoin i na zagušenje [na lancu](https://planb.academy/resources/glossary/onchain), što izaziva zabrinutost u vezi sa [skalabilnošću](https://planb.academy/resources/glossary/scalability) sistema.



Da bi funkcionisao, Lightning se oslanja na otvaranje [platnih kanala](https://planb.academy/resources/glossary/payment-channel) između učesnika, unutar kojih se transakcije mogu obavljati gotovo trenutno, često uz minimalne naknade, bez potrebe da se registruju jedna po jedna na Bitcoin blokčejnu. Ovi kanali mogu ostati otvoreni veoma dugo, zahtevajući onchain transakcije samo kada se otvaraju i zatvaraju.



[Čvor munje](https://planb.academy/resources/glossary/lightning-node) je učesnik u Lightning mreži, otvarajući kanale i vršeći plaćanja sa drugim čvorovima. U konkretnim terminima, čvor munje je softverski program koji se pokreće na računaru i implementira Lightning Network protokol. Primeri uključuju LND, Core Lightning ili Eclair. Glavna uloga ovog softvera je da:




- povežite se sa [Bitcoin čvorom](https://planb.academy/resources/glossary/full-node) da biste dobili informacije iz glavnog blockchaina;
- kreirajte i upravljajte dvosmernim kanalima plaćanja sa drugim čvorovima;
- razmenjivati poruke sa celom Lightning mrežom.



![Image](assets/fr/001.webp)



### Node vs. Lightning Wallet: važna razlika



Na Bitcoin (onchain), "*[wallet](https://planb.academy/resources/glossary/wallet)*" se odnosi na softver koji upravlja vašim [privatnim ključevima](https://planb.academy/resources/glossary/private-key), izračunava vaš saldo sa vaših [UTXO](https://planb.academy/resources/glossary/utxo) i kreira vaše transakcije. Ovaj wallet može biti zasnovan na vašem sopstvenom Bitcoin čvoru ili na tuđem, ali danas su uloge čvora i onchain wallet jasno različite.



Na Lightningu je teže ponovo koristiti ovu vrstu vokabulara bez stvaranja zabune. Termin "*Lightning wallet*" je prilično nejasan, jer u stvarnosti ne postoji nešto kao što je zaista samostalno-kustodijalni Lightning wallet, osim ako nije zasnovan na čvoru. Samo dve situacije su stoga moguće:



- Da biste imali pravi Lightning čvor (tj. ne-kustodijalan): softver koji koristite (npr. mobilna aplikacija kao što je Phoenix ili instanca LND na Umbrel) zapravo pokreće čvor, i vi zapravo držite ključeve za preuzimanje vaših bitkoina. U ovom slučaju, vaš "*Lightning wallet*" je zapravo samo korisnički interfejs na vrhu Lightning čvora, bilo ugrađenog ili udaljenog.



- Da biste koristili uslugu čuvanja: koristite aplikaciju koja vam prikazuje stanje u [sats](https://planb.academy/resources/glossary/satoshi-sat) na Lightning-u, ali u pozadini, sredstva su na čvoru provajdera (npr. Wallet of Satoshi). Nemate ni ključeve ni kontrolu nad kanalima. Vaše stanje je samo računovodstveni unos u bazi podataka kompanije. To je uporedivo sa ostavljanjem vaših bitcoina na platformi za razmenu, sa svim povezanim rizicima. U ovom slučaju, vaš "*Lightning wallet*" je samo pristup nalogu kojim upravlja operater koji, zauzvrat, vodi pravi Lightning čvor.



Dakle, nema sredine kod Lightning-a: ili imate čvor (čak i ugrađeni) pa ste u samostalnom staranju, ili nemate, pa kompanija poseduje vaš sats. Ali, kao što ćemo videti u narednim poglavljima, ove dve upotrebe ponekad je teško razlikovati. Na primer, Phoenix je mobilna aplikacija koja ugrađuje pravi Lightning čvor, ali korisnik nije nužno svestan toga, jer je puna složenost njenog rada gotovo potpuno skrivena.



### Podsetnik kako Lightning Network funkcioniše



U ovom odeljku, daću vam brz podsetnik o tome kako Lightning funkcioniše. Još jednom, ako želite detaljniju prezentaciju teorijskih koncepata, pozivam vas da pogledate posvećeni kurs LNP 201.



#### Kanali plaćanja: otvori, ažuriraj i zatvori



Srce Lightning mreže zasnovano je na dvosmernim kanalima plaćanja. Kanal se može otvoriti (tj. kreirati), ažurirati kako se odvijaju Lightning transakcije, i na kraju zatvoriti. Sa onchain tačke gledišta, kanal nije ništa drugo do 2/2 [multisignature](https://planb.academy/resources/glossary/multisig) [izlaz](https://planb.academy/resources/glossary/output).



![Image](assets/fr/002.webp)



Iz Lightning-ove perspektive, to je platni kanal sa [likvidnošću](https://planb.academy/resources/glossary/liquidity-lightning) podeljenom između dva učesnika.



![Image](assets/fr/003.webp)





- Otvaranje kanala:**



Dva čvora odlučuju da otvore kanal. Jedan od njih ulaže bitkoine u transakciju na lancu koja se zove *transakcija finansiranja*. Ova transakcija kreira izlaz zasnovan na [skripti](https://planb.academy/resources/glossary/script) sa više [potpisa](https://planb.academy/resources/glossary/digital-signature) 2-od-2, što znači da trošenje ovih sredstava na Bitcoin zahteva potpis oba čvora u kanalu. Pre izdavanja ove transakcije, strana koja obezbeđuje sredstva traži od druge da potpiše *transakciju povlačenja*, koja se ne izdaje na lancu, ali omogućava da povrati svoja sredstva u slučaju problema.



![Image](assets/fr/004.webp)





- Commitment transakcije:**



Stanje kanala (tj. distribucija sats između A i B) je predstavljeno *[commitment transaction](https://planb.academy/resources/glossary/commitment-transaction)*, poznatim obema čvorovima, ali nije odmah emitovano na blockchain-u. Ova transakcija opisuje kako redistribuirati sredstva kanala na lancu prema plaćanjima izvršenim na Lightning-u.



Sa svakom Lightning uplatom, dva čvora potpisuju novo stanje koje zamenjuje prethodno. Starije stanje se opoziva zahvaljujući mehanizmu ključa za opoziv: ako jedan od učesnika pokuša da emituje staro stanje, drugi može povratiti celokupan iznos sredstava kao kaznu.



Važna ideja ovde je da uvek postoji potpisana Bitcoin transakcija, koja nije emitovana na lancu, čuvana od strane čvorova, i koja omogućava redistribuciju međusobnih sats u skladu sa plaćanjima izvršenim na Lightning Network.



![Image](assets/fr/005.webp)





- Zatvaranje kanala:**



Kanal se može zatvoriti na uredan način putem kooperativnog zatvaranja, kada se obe strane slože oko konačnog stanja kanala, ili jednostrano (prisilno zatvaranje) ako jedan od učesnika prestane da sarađuje ili postane nedostupan. U svim slučajevima, zatvaranje se odvija u obliku transakcije na lancu koja troši 2/2 izlaz i raspodeljuje sredstva između učesnika prema poslednjem važećem stanju kanala.



![Image](assets/fr/006.webp)



Munja tako funkcioniše kao sekundarni sloj usidren na Bitcoin: samo određeni događaji (otvaranje i zatvaranje kanala) pojavljuju se na glavnom blokčejnu. Međuprovajni ostaju van lanca.



Pre nego što nastavimo dalje, evo dva osnovna pojma za razumevanje kako upravljati Lightning kanalom:




- Liquidity*: količina sats dostupna na jednoj strani kanala;
- *[Kapacitet](https://planb.academy/resources/glossary/lightning-channel-capacity)*: to je ukupna količina zaključana u 2/2 multisig izlazu, tj. zbir likvidnosti na obe strane kanala.



#### Mreža kanala i likvidnosti



Kanal nije samo za plaćanja između dva čvora: to je deo globalne mreže međusobno povezanih kanala. Vaš čvor može usmeravati plaćanja za druge korisnike kroz svoje kanale, i možete poslati sats na Lightning čvor sa kojim nemate direktan kanal, sve dok se može pronaći važeća putanja između vaša dva čvora.



Svaki čvor zna, putem [gossip protokola](https://planb.academy/resources/glossary/gossip), mapu ove mreže: koji kanali postoje, koji čvorovi su povezani dvosmernim kanalom i koje su kapacitete objavljene. Da biste poslali uplatu primaocu bez direktnog kanala, vaš čvor izračunava rutu koja se sastoji od nekoliko skokova: vaš čvor → čvor X → čvor Y → čvor primaoca. Na svakom skoku, uplata prolazi kroz kanal koji mora imati dovoljno likvidnosti u smeru uplate.



![Image](assets/fr/007.webp)



Likvidnost kanala stoga nije simetrična: jedna strana može biti jako opterećena, dok je druga gotovo prazna. Upravljanje ovom likvidnošću, tj. znati gde se sats nalaze i u kom pravcu mogu teći, jedan je od najvažnijih aspekata upravljanja Lightning čvorom. Detaljnije ćemo to razmotriti u praktičnim poglavljima koja slede.



#### HTLC: transportovanje plaćanja bez pljačke



Da bi omogućio plaćanja kroz posredničke čvorove bez potrebe za poverenjem, Lightning koristi [pametne ugovore](https://planb.academy/resources/glossary/smart-contract) zvane *[HTLC](https://planb.academy/resources/glossary/htlc)* (*Hashed Time-Locked Contracts*). U jednostavnim terminima, HTLC čini transfer sredstava uslovljenim otkrivanjem tajne, i uključuje vremensko ograničenje kako bi zaštitio pošiljaoca u slučaju neuspeha transakcije. Svako plaćanje je stoga podložno prezentaciji pre-slike (tajne čiji [heš](https://planb.academy/resources/glossary/hash-function) odgovara dogovorenoj vrednosti). Ako krajnji primalac pruži ovu pre-sliku, može preuzeti sredstva, što zauzvrat omogućava svakom posredničkom čvoru da povrati svoja sredstva.



![Image](assets/fr/008.webp)



Preskočiću tehničke detalje o tome kako HTLC funkcionišu, jer nisu bitni za svrhe ovog kursa. Detaljno objašnjenje ćete pronaći u kursu teorije LNP 201. Samo zapamtite da HTLC omogućavaju atomske razmene: ili se transfer završi i niko nije povređen u rutiranju, ili ne uspe i svaki učesnik povrati svoja početna sredstva. Ne postoji sredina.



### Glavne implementacije Lightning čvorova



Kao i kod Bitcoin, postoji nekoliko implementacija Lightning protokola. Brojni nezavisni timovi razvijaju svoje verzije, koje su sve međusobno interoperabilne jer se pridržavaju istih specifikacija ([BOLTs](https://planb.academy/resources/glossary/bolt)). Ovde su glavne implementacije koje se danas koriste.



#### LND (*Lightning Network Daemon*)



LND je kompletna implementacija Lightning protokola, napisana u Go jeziku i razvijena od strane Lightning Labs.



![Image](assets/fr/009.webp)



#### Core Lightning (*CLN*)



Core Lightning (prethodno *C-Lightning*) je implementacija koju je razvio Blockstream. Napisan je u C-u, sa nekim komponentama u Rust.



![Image](assets/fr/010.webp)



#### Ekler



Eclair je implementacija napisana u Scali i razvijena od strane francuske kompanije ACINQ. ACINQ upravlja jednim od najvažnijih čvorova za rutiranje u Lightning mreži sa Eclair-om, i koristi ovu implementaciju kao softversku osnovu za svoje proizvode, kao što je aplikacija Phoenix.



![Image](assets/fr/011.webp)



#### LDK (*Lightning Development Kit*)



LDK (*Lightning Development Kit*) je Rust razvojni komplet, koji održava Spiral (Block, bivši Square). To nije spreman za korišćenje daemon kao LND ili CLN, već biblioteka za programere koji žele da integrišu Lightning direktno u svoje aplikacije.



![Image](assets/fr/012.webp)



U ovom kursu LNP202, fokusiraćemo se uglavnom na LND: implementaciju koja se najčešće koristi u ključ-u-ruke rešenjima za privatne korisnike, kao što je Umbrel.



Toliko o ovom kratkom podsetniku o tome kako Lightning funkcioniše. Još jednom, ako postoje neki koncepti koje ne razumete, ili ako želite da se malo dublje upustite u temu pre nego što ih primenite u praksi, kurs Fanisa Mihalakisa je osnovna referenca na ovu temu:



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb


## Zašto pokrenuti sopstveni Lightning čvor?


<chapterId>421db24e-511c-41ed-ad68-69b0662042ea</chapterId>



Odgovor na ovo pitanje je prilično jednostavan, pošto je retoričko: bez sopstvenog čvora, više zapravo ne koristite Lightning, već samo iluziju Lightning-a preko infrastrukture kompanije.



Korišćenje Lightning kustodijalnog wallet znači da bitkoini tehnički pripadaju kompaniji koja upravlja čvorom. Vi ne držite privatne ključeve i ne kontrolišete kanale. Vaš wallet saldo je samo linija u bazi podataka provajdera usluga. Ova situacija je svakako vrlo pogodna za početnike, a korisničko iskustvo je često glatko, ali osnovno pitanje je: koja je prednost korišćenja Bitcoin i Lightning-a ako na kraju odustanete od aspekata koji ih razlikuju od tradicionalnih valuta i banaka?



Glavne dve vrednosti koje Bitcoin nudi su monetarni suverenitet (nezavisnost od centralne vlasti za izdavanje i držanje) i otpornost na cenzuru (nemogućnost treće strane da spreči ili filtrira plaćanja). Sistem skrbništva na Lightning mreži direktno se suprotstavlja ovim ciljevima: ne možete proveriti internu ponudu novca platforme, a po definiciji, operater koji drži sva sredstva i sve kanale može cenzurisati, odlagati, davati prioritet ili blokirati vaša plaćanja. U ovim uslovima, možemo se legitimno zapitati, **koja je svrha korišćenja bitkoina putem Lightning mreže ako će reprodukovati iste obrasce poverenja i zavisnosti kao tradicionalni sistemi državne valute**.



> Ono što je potrebno je elektronski sistem plaćanja zasnovan na kriptografskoj potvrdi umesto na poverenju, omogućavajući bilo koje dve voljne strane da direktno međusobno transakcionišu bez potrebe za pouzdanim trećim licem.
*Satoshi Nakamoto, Bitcoin Bela knjiga


Filozofiju na stranu, konkretniji nedostaci za vas su sledeći. Prvo, nemate način da verifikujete da kompanija zaista poseduje bitkoine koji odgovaraju prikazanim saldima. Može da posluje na osnovu frakcionalnih rezervi, bude hakovana, bankrotira ili jednostavno nestane. U tom slučaju, vi ste samo još jedan poverilac, bez stvarne garancije da ćete dobiti svoj novac nazad.



Drugo, kompanija je podložna regulatornim rizicima: zabrane, zamrzavanje sredstava, zahtevi za blokiranje korisnika ili transakcija, pojačan nadzor, ili čak potpuna zabrana aktivnosti u određenim jurisdikcijama. Svako ograničenje koje opterećuje pružaoca usluga mehanički se odražava na vas.



U smislu poverljivosti, situacija nije ništa bolja. Operater skrbnik vidi sve vaše tokove: iznose, učestalost, primaoce, stanja, navike potrošnje. U kombinaciji sa informacijama koje pruža aplikacija i mogućom osnovnom analizom lanca na Bitcoin, ove informacije mogu pružiti veoma precizan profil vaše finansijske aktivnosti. Još jednom, to je daleko od cilja Bitcoin da smanji finansijsko praćenje.



Dobra vest je da danas, upravljanje sopstvenim Lightning čvorom više nije rezervisano za tehničke stručnjake, kao što je možda bilo krajem 2010-ih. Relativno jednostavna rešenja su dostupna za kućne korisnike, što ćemo detaljno objasniti u narednom poglavlju.




## Odabir pravog rešenja za posao


<chapterId>615870e3-741d-4ec1-875d-a483e70f39d4</chapterId>



Danas je moguće imati korisničko iskustvo vrlo blisko onom kod Lightning custodial wallet, dok ostajete u samostalnom čuvanju. Cilj ovog poglavlja je pomoći vam da izaberete put koji najbolje odgovara vašem profilu.



### Opcija 1: Ne koristite Lightning direktno



Prvo rešenje je jednostavno da se Lightning ne koristi nativno, već da se koristi Bitcoin ili [Liquid](https://planb.academy/resources/glossary/liquid-network) wallet koji ugrađuju [atomske zamene](https://planb.academy/resources/glossary/atomic-swap). Na primer, Aqua ili BULL Wallet aplikacije koriste ovu metodu, omogućavajući vam da plaćate [Lightning fakture](https://planb.academy/resources/glossary/invoice-lightning) bez upravljanja Lightning čvorom sami, dok ostajete u samostalnom staranju.



Princip je jednostavan: vaša sredstva ostaju u Bitcoin, bilo on-chain ili na Liquid, a pristupate im putem wallet gde držite ključeve na tradicionalan način. Kada skenirate Lightning fakturu, vaš wallet pokreće transakciju (on-chain ili Liquid) ka servisu za atomske zamene. Ovaj servis zatim upravlja Lightning plaćanjem putem svog čvora, koristeći bitkoine koje ste obezbedili on-chain ili putem Liquid. Kao rezultat, ne morate sami upravljati bilo kojim Lightning kanalima, a ipak možete bez problema izvršavati Lightning fakture.



![Image](assets/fr/013.webp)



Glavna prednost ovog pristupa, u poređenju sa konvencionalnim Lightning kustodijalnim wallet, je što ostajete u 100% posedu svojih sredstava u svakom trenutku. Bitcoini su u vašem onchain ili Liquid wallet, sa vašom sopstvenom [mnemoničkom frazom](https://planb.academy/resources/glossary/seed). Čak i tokom zamene, ostajete u posedu svojih sredstava, jer je zamena atomska. Oslanja se na kriptografski mehanizam koji osigurava da postoje samo dva moguća ishoda: ili zamena u potpunosti uspeva, ili ne uspeva i usluga ne može prisvojiti vaša sredstva.



Većina portfolija koji nude ovu vrstu funkcionalnosti oslanja se na [Boltz](https://boltz.exchange/) za tehnički deo zamene.



Ovo rešenje takođe nudi zanimljive prednosti u pogledu poverljivosti, posebno kada se kombinuje sa Liquid. Za početnika, takođe je veoma lako postaviti i sačuvati: klasična mnemonička fraza, bez kanala, bez likvidnosti za balansiranje...



S druge strane, ovaj pristup ima svoja ograničenja. Prvo, nije neosporan: zavisite od dostupnosti i dobre volje usluge zamene. Ako više ne želi da obrađuje vaš nalog ili prestane sa radom, više ne možete plaćati Lightning fakture preko nje. Zatim, tu su i ne tako zanemarljive naknade: plaćate i onchain ili Liquid [transakcione naknade](https://planb.academy/resources/glossary/transaction-fees), kao i proviziju usluge zamene. Takođe, ako onchain naknade naglo porastu, korišćenje Lightning-a može postati veoma skupo.



Dakle, za povremenu upotrebu, to je i dalje prihvatljivo, ali za veoma aktivnog korisnika Lightning-a, bolje je raditi stvari kako treba sa pravim Lightning čvorom.



### Opcija 2: Ugrađeni Lightning čvorovi



Druga kategorija rešenja zasniva se na Lightning čvorovima ugrađenim direktno u mobilnu aplikaciju. Phoenix Wallet su pioniri ovog modela i ostaju merilo. Danas, drugi projekti nude uporedive pristupe, kao što su Zeus (u ugrađenom režimu) ili BitKit.



Ideja je jednostavna: aplikacija zapravo pokreće Lightning čvor, ali sve složene operacije se automatski obavljaju u pozadini. Imate "*Lightning wallet*" interfejs sa mnemoničkom frazom za rezervnu kopiju, vidite saldo i plaćate fakture, ali ne upravljate kanalima, likvidnošću ili većinom parametara.



![Image](assets/fr/014.webp)



Ova rešenja su uvek samostalna. Ključevi koji kontrolišu sredstva su generated i čuvaju se na vašem telefonu, a rezervna kopija je putem seed ili ekvivalentnog mehanizma. Ne posedujete samo nalog kod provajdera usluga, već zapravo posedujete bitkoine zaključane u kanalima koji pripadaju vama i ne mogu biti ukradeni.



Prednosti LN on-board čvorova su brojne:




- izuzetno lako za instalaciju i korišćenje;
- korisničko iskustvo slično onom kod skrbničkog Lightning wallet, ali sa samostalnim skrbništvom;
- nema ručnog upravljanja kanalima ili likvidnošću;
- relativno jednostavna rezervna kopija.



Ali ovi ugrađeni wallets takođe imaju značajna ograničenja. Prvo, u smislu poverljivosti, operater usluge (npr. ACINQ u slučaju Phoenix) ima prilično detaljan pregled tokova koji prolaze kroz vaš čvor: iznosi, učestalosti, primaoci, čak i ako se to mora poboljšati, posebno sa postepenim usvajanjem *Trampoline Nodes*. Drugo, u velikoj meri zavisite od ovog operatera kao vašeg glavnog Lightning partnera. Ako ACINQ čvor postane nedostupan (u slučaju Phoenix), ako kompanija dođe pod regulatorni pritisak ili promeni svoj poslovni model, vaše korisničko iskustvo može biti ozbiljno degradirano, ili čak ugroženo.



Konačno, ova jednostavnost dolazi po određenoj ceni. Usluge ugrađenih LN čvorova obično naplaćuju specifične naknade na depozite, isplate ili određene operacije upravljanja kanalima. Po mom mišljenju, ovaj model ima smisla u smislu ponuđene usluge, ali za intenzivnu upotrebu, može biti mnogo skuplji od dobro upravljanog konvencionalnog Lightning čvora.



### Opcija 3: klasični Lightning čvor



Treće rešenje, ono koje ćemo detaljnije razmatrati u ovom kursu LNP202, jeste upravljanje konvencionalnim Lightning čvorom na posvećenom serveru ili uređaju.



Pod "klasičnim" mislim da sami instalirate i konfigurišete Lightning implementaciju (npr. LND) na vrhu vašeg sopstvenog Bitcoin čvora. Birate svoje peer-ove, otvarate svoje kanale, upravljate svojom [dolaznom i odlaznom likvidnošću](https://planb.academy/resources/glossary/inbound-capacity) i postavljate svoje politike naknada za rutiranje.



U smislu suvereniteta, to je najbolje rešenje. Više niste zavisni od određene kompanije za vaše kanale ili plaćanja: ako vas peer cenzuriše ili zatvori kanal, možete otvoriti drugi sa različitim čvorom. Ako usluga nestane, vaši sats ostaju u kanalima koje kontrolišete, i možete ih repatrirati na lancu. Takođe možete optimizovati vaše dugoročne troškove: kada su vaši kanali pravilno veličine i upravljani, ukupni trošak plaćanja može postati veoma nizak.



Što se tiče poverljivosti, očigledno ste podložni ograničenjima Lightning-ovog sopstvenog modela, ali ne prepuštate čitav svoj posao jednom operateru.



Nasuprot tome, postavljanje klasičnog Lightning čvora je očigledno složenije: morate instalirati, konfigurisati, održavati, pratiti ažuriranja, razumeti logiku kanala i politike naplate, upravljati kanalima i tokovima novca, i tako dalje. Pogrešna konfiguracija, nemaran bekap ili nepažljivo upravljanje mogu lakše dovesti do gubitka sats. Čvor takođe mora raditi neprekidno.



Ovo je upravo put koji predlažem da pratite u ovom kursu, prateći vas na svakom koraku kako biste ograničili rizike i strukturirali svoj pristup.



### Koje rešenje za koji korisnički profil?



Da biste odabrali pravo rešenje za vaš Lightning korisnički profil, potrebno je da razmotrite dva faktora: koliko često koristite Lightning i vašu sklonost ka tehničkom upravljanju.



Ako ne vršite mnogo Lightning plaćanja povremeno, ali i dalje želite da možete da podmirite LN fakture sa svog telefona s vremena na vreme, bez odricanja od samostalnog čuvanja: Bitcoin ili Liquid wallet sa funkcionalnošću zamene je verovatno najbolja opcija. Zadržavate vlasništvo nad svojim sredstvima, ne upravljate čvorovima i prihvatate nešto veće naknade u zamenu za jednostavnost.



https://planb.academy/tutorials/wallet/mobile/bull-bitcoin-2c72127c-a228-4f50-b833-c6183d56aaf6

https://planb.academy/tutorials/wallet/mobile/aqua-8e6d7dd3-8c03-45cc-90dd-fe3899a7d125

Ako redovno koristite Lightning i želite prednosti pravog čvora, ali ne želite da trošite vreme na upravljanje kanalima, naknadama ili infrastrukturom, mobilni ugrađeni Lightning čvor je dobro rešenje. Zadržavate kontrolu nad svojim sredstvima, korisničko iskustvo ostaje vrlo pristupačno, a sva složenost je skrivena, po cenu izražene zavisnosti od operatera.



https://planb.academy/tutorials/wallet/mobile/phoenix-0f681345-abff-4bdc-819c-4ae800129cdf

https://planb.academy/tutorials/wallet/mobile/bitkit-a7224674-85c4-4045-9baf-37018d89550c

https://planb.academy/tutorials/wallet/mobile/zeus-embedded-c67fa8bb-9ff5-430d-beee-80919cac96b9

Ako ste korisnik srednjeg ili naprednog nivoa, spremni da uložite vreme u razumevanje i upravljanje vašom infrastrukturom, i želite maksimalnu kontrolu nad vašim kanalima, likvidnošću i troškovima: klasični server-bazirani Lightning čvor je pravi izbor. To je najzahtevnije rešenje, ali i najdoslednije sa Bitcoin idejom suvereniteta.




# Kreiranje vašeg prvog Lightning čvora


<partId>b6db225e-61ab-437a-bccb-33d07503da15</partId>



## Instaliranje LND sa Umbrel


<chapterId>a0014bf3-1bd3-4311-b15b-5ef2354ec744</chapterId>



Sada kada smo pregledali osnove Lightning-a i dostupna rešenja, vreme je da pređemo na posao. Da biste pohađali ovaj kurs, biće vam potreban Bitcoin čvor sinhronizovan sa Umbrel. Ovaj LNP202 kurs obuke je nastavak BTC 202; ako još nemate Bitcoin čvor, pozivam vas da pohađate ovaj drugi kurs obuke pre nego što se vratite ovde kada vaš čvor bude sinhronizovan. Toplo preporučujem da ga konsultujete, jer neću ulaziti u detalje o njegovom radu, konfiguraciji i merama bezbednosti.



https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426

U ovom prvom poglavlju, pogledaćemo kako instalirati LND na vaš Umbrel. Način na koji Umbrel funkcioniše čini ovaj korak veoma jednostavnim, jer sve što treba da uradite je da instalirate aplikaciju.



Sa početne stranice otvorite `App Store` na dnu interfejsa.



![Image](assets/fr/015.webp)



U traku za pretragu unesite `Lightning Node`, zatim kliknite na aplikaciju.



![Image](assets/fr/016.webp)



Zatim kliknite na dugme `Install` da pokrenete instalaciju.



![Image](assets/fr/017.webp)



Sa početne stranice kliknite na aplikaciju da je otvorite, zatim izaberite `Postavi novi čvor`.



![Image](assets/fr/018.webp)



Dobili ste frazu od 24 reči. Čuvajte je na sigurnom mestu. U sledećem poglavlju ćemo detaljnije pogledati kako da povratite pristup svom Lightning čvoru (ovo je mnogo složeniji proces nego za jednostavan Bitcoin wallet), ali za sada zapamtite da ova fraza igra ključnu ulogu i mora biti sačuvana sa najvećom pažnjom.



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Sačuvajte ovu frazu na isti način kao konvencionalnu mnemotehničku frazu: na fizičkom mediju (papir ili metal) čuvanom na sigurnom mestu, zatim kliknite na dugme `NEXT`.



![Image](assets/fr/019.webp)



Zatim unesite reči svoje rečenice da proverite da li ste ih ispravno zapisali.



![Image](assets/fr/020.webp)



Poruka upozorenja će vas podsetiti da je aplikacija u beta verziji i da Lightning Network ostaje eksperimentalna tehnologija. Očigledno, nikada ne ulažite iznose u vaš Lightning čvor koje niste spremni da izgubite.



Zatim ćete stići na glavni interfejs vašeg Lightning čvora. Sa leve strane, pronaći ćete vaš Bitcoin onchain wallet hostovan na vašem čvoru. Ovo je onaj generated iz 24 reči fraze koju ste upravo sačuvali.



U centru ćete pronaći svoj Lightning wallet. On zapravo predstavlja vaš [odlazni novac](https://planb.academy/resources/glossary/outbound-capacity), tj. bitkoine koje posedujete unutar svojih Lightning kanala.



Sa desne strane videćete nekoliko važnih informacija o vašem čvoru:




- Broj veza i otvorenih kanala;
- Vaš ukupni odlazni novčani tok, tj. ono što teoretski možete potrošiti na Lightning;
- Vaša ukupna dolazna likvidnost, tj. ono što teoretski možete primiti na Lightning-u.



![Image](assets/fr/021.webp)



Hajde da počnemo sa prilagođavanjem našeg čvora. Kliknite na tri male tačke u gornjem desnom uglu interfejsa, zatim na `Napredna podešavanja`. U podmeniju `Personalizacija`, možete definisati javno ime za vaš čvor (izbegavajte korišćenje pravog imena) i izabrati njegovu boju.



![Image](assets/fr/046.webp)



Zatim kliknite na zeleni taster `SAVE AND RESTART` da restartujete vaš čvor i primenite ove promene.



Vaš Lightning čvor je sada spreman da otvori svoje prve kanale za obavljanje plaćanja. Ali prvo, hajde da pogledamo kako da zaštitite vaš sats!



## Čuvanje vašeg Lightning čvora


<chapterId>638fa75d-62af-4bf3-ab4a-b7d10ea75815</chapterId>



Pre nego što pošaljete svoj prvi sats na vaš čvor, važno je razumeti kako funkcioniše njegova rezervna kopija i koji su povezani rizici. Za razliku od jednostavnog Bitcoin onchain portfolija, pravljenje rezervne kopije Lightning čvora je prilično složeno: pogrešna strategija može dovesti do trajnog gubitka vaših sredstava. U ovom poglavlju ćemo pogledati šta zaista treba da se sačuva, i kako Umbrel upravlja ovim procesom sa LND.



U ovom kursu ćemo koristiti implementaciju LND (*Lightning Network Daemon*). Iako su principi slični na drugim implementacijama, fajlovi za oporavak i procedure o kojima ću govoriti su specifični za LND.



### Šta treba da sačuvam na Lightning čvoru?



Na Lightning čvoru, nije dovoljno sačuvati seed i nadati se da će se sve vratiti u normalu. Nekoliko elemenata igra različite uloge, tako da je važno razlikovati ih.



#### seed (*aezeed*)



Kada inicijalizujete LND, dobijate 24-rečnu seed. Ovo je LND-specifičan format nazvan "*aezeed*". Nije klasičan seed BIP39, iako izgleda veoma slično. Iz ovog seed, LND izvodi privatne ključeve vašeg onchain wallet povezanog sa Lightning čvorom, tj. adrese na koje možete primati ili na koje možete repatrirati bitkoine nakon zatvaranja kanala.



![Image](assets/fr/019.webp)



Ovaj seed se stoga može koristiti za ponovno kreiranje onchain wallet povezanog s vašim čvorom i za povrat sredstava koja su već vraćena onchain (npr. nakon zatvaranja kanala). S druge strane, sam seed nije dovoljan za vraćanje vaših Lightning kanala koji su još uvek otvoreni, jer ne sadrži potrebne informacije o statusu vaših kanala.



#### Baza podataka kanala (`channel.db`)



LND skladišti detaljan status vaših kanala u bazi podataka pod nazivom `channel.db`. Ova baza podataka sadrži:




- lista vaših otvorenih kanala;
- vaše kolege i njihovi identifikatori;
- poslednji commitment transaction za svaki kanal (uzastopna stanja koja definišu ko šta poseduje u kanalu i omogućavaju da se sredstva na lancu povrate u slučaju problema);
- informacije potrebne za kažnjavanje vršnjaka koji pokušava da emituje stari izveštaj.



Problem sa ovom bazom podataka je što se stalno menja: svaka uplata, svako rutiranje, svako otvaranje ili zatvaranje kanala menja njen sadržaj. Zato je konvencionalna rezervna kopija (npr. periodična kopija vašeg `channel.db`) opasna. Ako vratite previše staru verziju `channel.db` i ponovo sastavite čvor sa ovim zastarelim stanjem, vaši partneri mogu smatrati da emitujete staro stanje kanala. U tom slučaju, protokol predviđa kaznu: vaš partner može povratiti celokupan iznos sredstava kanala, kao da ste pokušali da varate.



U praksi, dakle, `channel.db` nije medijum za bekap kao takav. To je živo stanje vašeg čvora. Jedina situacija u kojoj ima smisla koristiti ga za vraćanje vašeg čvora je kada oporavljate ovu bazu podataka direktno sa mašine koja je upravo otkazala (npr. disk koji je još uvek čitljiv). U ovom slučaju, oporavljate najnovije stanje i možete ponovo pokrenuti LND na drugoj mašini na osnovu ove baze podataka, sigurni u saznanju da je ovo stanje što je moguće ažurnije, s obzirom da stara mašina više ne radi. Druga situacija u kojoj ova metoda može poslužiti kao relevantan bekap je u konfiguraciji sa dva diska, sa dinamičkom, stalnom kopijom sa jednog na drugi. Međutim, ova vrsta postavke je složenija za implementaciju.



Ali pravljenje periodičnih kopija `channel.db` i čuvanje istih kao rezervnih kopija za kasnije vraćanje je veoma loša ideja: onog dana kada ih upotrebite, rizikujete da sami sebe kaznite i izgubite sve vaše sats.



#### Staticka Rezervna Kopija Kanala (SCB)



Da bi omogućio oporavak od katastrofe, LND je uveo mehanizam *Static Channel Backup* (SCB). Ovo je poseban fajl, često nazvan `channel.backup`, koji sadrži statičke informacije o vašim kanalima: ko su vaši partneri, kako ih kontaktirati i šta su vaši kanali.



Ova datoteka ne sadrži detaljan status kanala ili istoriju ažuriranja. Ne omogućava vam da ponovo otvorite kanale u tačnom stanju u kojem su bili, niti da nastavite sa radom ovog Lightning čvora. Umesto toga, njena uloga je da deluje kao sidrišna tačka kako biste zamolili svoje partnere da vam pomognu da čisto zatvorite sve svoje kanale, i tako primite svoj sats na lancu, na ključeve koje možete povratiti zahvaljujući seed. Dakle, za razliku od datoteke `channel.db`, koja se menja sa svakom uplatom ili rutiranjem, SCB datoteka se ažurira samo kada se kanal otvori ili zatvori.



Kada se oporavljate putem SCB, proces je sledeći:




- Vraćate svoj seed (*aezeed*), što rekreira vaš onchain wallet povezan sa Lightning čvorom;
- Vi pružate LND sa vašim najnovijim SCB;
- LND koristi SCB da pronađe listu vaših vršnjaka i kanale koje imate s njima;
- Kontaktira svakog partnera, kaže im da ste pretrpeli gubitak podataka i traži od njih da "prisilno zatvore" vaš kanal s njima, kako biste mogli povratiti svoj deo na lancu.



Ideja je da će vaši vršnjaci, primetivši da prijavljujete gubitak podataka, emitovati svoj poslednji commitment transaction i zatvoriti kanal sile. Kada ove transakcije budu potvrđene, vaša sredstva će se ponovo pojaviti u vašem onchain portfoliju (povezanom sa seed).



Međutim, ovaj mehanizam oporavka nije savršen. Prvo, on zapravo ne vraća vaš Lightning čvor, jer će svi kanali biti zatvoreni. Zatim ćete morati da izgradite novi Lightning čvor od nule. Drugo, ne garantuje 100% oporavak, iako značajno povećava šanse za oporavak vaših onchain salda u slučaju problema. Naime, ovaj protokol oporavka zavisi od saradnje i dostupnosti vaših partnera: ako je jedan od njih van mreže, izgubio je sopstvene podatke ili odbija da sarađuje, vaša sredstva mogu ostati blokirana, ili čak trajno izgubljena. Zato je važno da ne držite kanale otvorene na vašem Lightning čvoru sa nedostupnim partnerima tokom dužih vremenskih perioda. Ako u tom trenutku dođe do gubitka podataka i partner ostane nedostupan, oporavak putem SCB-a će biti nemoguć, i vaša sredstva će ostati izgubljena dok se taj partner ne vrati na mrežu (možda zauvek).



Da sumiramo, dobra strategija za Lightning rezervnu kopiju na LND počiva na tri stuba:




- Vaš seed (*aezeed*), za onchain sloj;
- Pouzdana automatska SCB rezervna kopija;
- Dobro upravljanje kanalom odabirom pouzdanih partnera i preventivnim zatvaranjem onih koji su često nedostupni.



### Kako Umbrel upravlja rezervnom kopijom vašeg LND čvora?



Umbrel nudi pojednostavljeni mehanizam za pravljenje rezervnih kopija za čvor LND, zasnovan tačno na SCB. Ideja je da vas oslobodi muke ručnog manipulisanja ovim fajlom, pravljenja njegove rezervne kopije i automatizuje proces koliko god je to moguće.



Kada kreirate svoj čvor na Umbrel, dobijate seed koji igra dvostruku ulogu:




- povezuje vaš Bitcoin onchain wallet povezan sa vašim Lightning čvorom;
- koristi se za dobijanje rezervnog identifikatora i ključa za šifrovanje koji se koristi za udaljene SCB rezervne kopije.



Zahvaljujući ovom mehanizmu, Umbrel automatski pravi šifrovanu rezervnu kopiju vašeg SCB-a i čuva je na svojim serverima putem Tor-a. SCB se čuva šifrovan, zahvaljujući ključu izvedenom iz vašeg seed. Dakle, u slučaju gubitka podataka, sve što treba da uradite je da ponovo kreirate Bitcoin i Lightning čvor na Umbrel, na istom ili drugom uređaju, zatim unesete vaš seed. Tada ćete moći da povratite najnoviji status SCB-a sa servera Umbrel, dešifrujete ga i započnete proces povraćaja vaših sredstava.



Ove rezervne kopije su lokalno šifrovane od strane vašeg čvora pre nego što budu poslate, što garantuje poverljivost vaših podataka: Umbrel ne može da pročita sadržaj SCB-a. Prenos se odvija putem Tor-a, što sprečava curenje vaše IP adrese. Štaviše, vaš Umbrel dodaje šum saobraćaju (nasumično popunjavanje i lažne rezervne kopije poslate u nepravilnim intervalima) kako bi se sprečilo da server precizno zaključi kada otvarate ili zatvarate kanal.



Glavna prednost ove metode je što značajno pojednostavljuje bekap vašeg Lightning čvora: morate da napravite bekap vašeg seed samo jednom tokom inicijalizacije čvora. Ovo nosi određeni rizik, jer je to samo bekap SCB-a, ali za razumne iznose to je prihvatljiv kompromis.



### Najbolje prakse za ograničavanje rizika od gubitka



Čak i uz Umbrel rezervnu kopiju, nekoliko jednostavnih dobrih praksi može značajno smanjiti rizik od gubitka sats:





- Nadgledajte dostupnost svojih kolega:



Ako se važan kanal često povezuje sa nedostupnim ili nestabilnim peer-om, sigurnije je zatvoriti ga na uredan način dok vaš čvor još uvek radi. Preventivno kooperativno ili prisilno zatvaranje eliminiše potencijalni izvor problema u slučaju SCB oporavka.





- Izbegavajte koncentrisanje previše likvidnosti na nepoznate partnere:



Što je veći kanal koji peer ima sa vama, to je važnije biti pouzdan. Birajte ozbiljne, dobro povezane i aktivne čvorove, kako bi svaki budući oporavak putem SCB mogao teći glatko.





- Dopunite Umbrel lokalnim rezervnim kopijama:



Pored automatske izrade rezervne kopije Umbrel, možete takođe čuvati šifrovanu kopiju vašeg SCB fajla (`channel.backup`) na eksternim medijima i periodično je ažurirati. Idealno bi bilo da je obnovite svaki put kada otvorite ili zatvorite kanal. Ovo vam pruža rešenje za rezervnu kopiju ukoliko, iz bilo kog razloga, automatska usluga izrade rezervne kopije Umbrel postane nedostupna.





- Upravljanje vašim seed na pravi način



Vaš seed Umbrel ne samo da obnavlja vaš onchain wallet, već i izvodi enkripcioni ključ za bekape. Napadač sa pristupom tome mogao bi stoga pokrenuti oporavak i preneti vaša sredstva na svoj wallet, čak i bez fizičkog pristupa vašem čvoru.



Dakle, ako treba da vratite svoj čvor, ali više nemate svoj seed, nećete moći da povratite ništa: sav vaš sats će biti izgubljen. Zato je veoma važno da sačuvate svoj seed sa najvećom pažnjom, isključivo na fizičkim medijima (papir ili metal), i da ga čuvate na sigurnom mestu. Za više informacija o upravljanju seed, molimo vas da pogledate ovaj vodič:



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

### Kako da sačuvam svoj Lightning čvor na Umbrel?



Sada kada ste razumeli kako teorija funkcioniše, pređimo na suštinu. Iz vaše Lightning Node aplikacije (koja je zapravo LND), kliknite na tri male tačke u gornjem desnom uglu.



![Image](assets/fr/022.webp)



Postoje tri elementa od interesa ovde za rezervnu kopiju:




- Proverite da je opcija `Automatic backups` omogućena. Ovo će automatski poslati vaš enkriptovani SCB na servere Umbrel.
- Zatim možete izabrati da li ćete poslati putem Tor-a ili clearnet-a, koristeći opciju `Backup over Tor`. Kao što je objašnjeno u prethodnim odeljcima, toplo preporučujem da koristite Tor kako biste sačuvali svoju poverljivost.
- Konačno, tu je dugme `Download channel backup file`, koje vam omogućava da preuzmete `channel.backup` fajl, tj. enkriptovani snimak vašeg SCB-a, na vaš računar. Ovo vam omogućava da povremeno pravite dodatne lokalne rezervne kopije, pored onih koje se automatski šalju na Umbrel servere.



Sada znate kako da zaštitite svoj Lightning čvor sats od gubitka podataka. U sledećem poglavlju, pogledaćemo kako da osigurate svoj čvor protiv pokušaja varanja.




## Watchtower: uloga i postavka


<chapterId>e6c654dd-26c5-4e4d-8d11-a215bac37812</chapterId>



U Lightning-u, svaki kanal se zasniva na nizu uzastopnih stanja, predstavljenih neobjavljenim commitment transactions. Sa svakom Lightning uplatom ili rutiranjem, 2 učesnika u kanalu kreiraju novi par commitment transactions, koji odražava trenutnu raspodelu sredstava u kanalu. Stari commitment transactions postaju zastareli.



Ako jedna od strana objavi zastarelo stanje, druga ima pravo da je sankcioniše i povrati celokupan iznos sredstava kanala. U ovom poglavlju ćemo ukratko pogledati kako ovaj mehanizam funkcioniše, a zatim objasniti kako postaviti ***watchtower***: sistem za zaštitu vašeg Lightning čvora od mogućih pokušaja varanja.



### Razumevanje kako stražarske kule funkcionišu


U svakom trenutku, svaka strana u kanalu ima commitment transaction koji, ako se objavi, omogućava zatvaranje kanala i povrat njihovog dela sredstava. Ovaj proces je poznat kao *prisilno zatvaranje*. Ali ako pokušaju da objave stariji commitment transaction, koji odgovara prethodnom stanju kanala gde je držao više sats, tada bi se ova transakcija smatrala pokušajem varanja. U tom slučaju, druga strana može koristiti ključ za opoziv povezan sa ovim starijim stanjem da povrati celokupni iznos sredstava u kanalu, dok je varalica privremeno blokirana vremenskim zaključavanjem.


Ovaj sistem znači da je objavljivanje starog stanja, tj. pokušaj varanja, veoma rizično: ako druga strana vidi ovu transakciju na mempool-u ili na blockchain-u pre nego što istekne vremensko zaključavanje, može koristiti ključ za opoziv i povratiti sva sredstva. **Stoga, sigurnost vašeg Lightning kanala zavisi od vaše sposobnosti da otkrijete pokušaj varanja unutar vremenskog okvira koji nameće vremensko zaključavanje**.



#### Zašto su osmatračnice neophodne?



Mehanizam kazne funkcioniše samo ako je povređena strana u mogućnosti da:




- pratiti svaki novi Bitcoin blok da vidiš da li je kanal commitment transaction objavljen;
- odrediti da li ova transakcija odgovara poslednjem važećem stanju ili opozvanom stanju;
- u slučaju opozvanog statusa, emitovati pravnu transakciju na vreme, koristeći ključ za opoziv da povratite sva sredstva pre nego što istekne vremensko zaključavanje.



![Image](assets/fr/023.webp)



U idealnom scenariju, vaš Lightning čvor je online 24/7, sinhronizovan je i kontinuirano prati blockchain. Iz tog razloga, može samostalno detektovati pokušaj varanja i reagovati. U praksi, međutim, lični Lightning čvor može se isključiti, posebno u slučaju dugotrajnog nestanka struje ili prekida Internet veze.



Upravo tokom ovih perioda zastoja rizik postaje stvaran: ako nepošteni čvor objavi stari status dok je vaš čvor van mreže, i vremenska brava istekne bez vaše reakcije, prevara postaje efektivna. Gubite deo ili sva sredstva u kanalu.



Watchtowers su uvedeni kako bi smanjili ovaj rizik. Stražarska kula je eksterni servis koji nadgleda blokčejn u vaše ime, skenirajući moguće objavljivanje starog statusa na jednom od vaših kanala, i, ako je potrebno, automatski emituje kaznenu transakciju u vaše ime. Dakle, čak i ako vaš Lightning čvor ostane van mreže duži period, sve dok je stražarska kula koju koristite operativna, biće u mogućnosti da zaštiti vaša sredstva nadgledanjem bilo kakvih pokušaja varanja i primenom odgovarajuće kazne, čim je detektuje.



#### Kako funkcioniše osmatračnica



Stražarski toranj je dizajniran da minimizira informacije koje saznaje o vašim kanalima, dok mu istovremeno daje sredstva da reaguje u slučaju problema:




- Za svako novo stanje kanala sa partnerom, vaš čvor unapred priprema potencijalnu kaznenu transakciju. U slučaju da ovaj partner vara, ova transakcija bi vam omogućila da povratite sva sredstva u kanalu;
- Vaš čvor zatim šifrira ovu kaznenu transakciju koristeći TXID odgovarajućeg commitment transaction (onog koji bi se koristio ako bi prevarant pokušao prevaru). Sve dok se ne dogodi zatvaranje, osmatračnica ne može dešifrovati ovu transakciju, jer ne zna u potpunosti TXID prevarantske transakcije;
- Vaš čvor šalje osmatračnici paket koji sadrži šifrovanu kaznenu transakciju i polovinu TXID-a potencijalne varajuće transakcije.



Kako je TXID prenet na osmatračnicu nepotpun, ona ne može dešifrovati pravosudnu transakciju. Međutim, može pratiti blokčejn za TXID koji se poklapa sa delom koji poseduje. Ako otkrije takvu transakciju, tada pokušava da koristi puni TXID te transakcije da dešifruje vašu kaznenu transakciju. Ako dešifrovanje uspe, zna da je to pokušaj varanja i odmah objavljuje kaznenu transakciju za vas.



![Image](assets/fr/024.webp)



Zbog toga osmatračnica nema uvid u detalje vaših kanala: ni identitet vaših partnera, ni stanja, ni strukturu transakcija. Ona vidi samo šifrovane pakete. Jedina informacija koju može da zaključi je stopa kojom se vaši kanali ažuriraju, pošto prima paket za svako novo stanje, ali nije u mogućnosti da zna njegov sadržaj. U slučaju varanja, sigurno će otkriti informacije o kanalu dešifrovanjem kaznene transakcije, ali barem će vaš sats biti sačuvan.



Ovaj mehanizam se zasniva na kompromisu: delegirate sposobnost objavljivanja unapred potpisane kaznene transakcije čuvaru, ali ta transakcija ostaje potpuno neprozirna za čuvara dok se ne dogodi neka prevara. Čuvar ne može ni da modifikuje primaoce niti da preusmeri sredstva, jer ima samo transakciju koja je već potpisana, sa izlazima zamrznutim u vašu korist. Takođe ne može da zna detalje kanala u legitimnom prinudnom ili kooperativnom zatvaranju, jer se TXID-ovi ne poklapaju. S druge strane, čuvar ostaje minimalno pouzdana treća strana: morate se osloniti na njega da bude online i da pravilno emituje vašu pravosudnu transakciju kada vam je potrebna.



#### Postati osmatračnica



U teoriji, bilo koji Lightning čvor može delovati kao osmatračnica za druge čvorove (ako koriste istu implementaciju, npr. LND), dok je sam zaštićen od strane drugih čvorova koji igraju ovu ulogu za njega. U sledećim praktičnim odeljcima, pokazaću vam kako da postavite ovaj jednostavan mehanizam na vašem LND pod Umbrel.


Kao posledica, zanimljiva strategija mogla bi biti da se dogovorite sa prijateljima bitkoinerima od poverenja da budete jedni drugima osmatračnica. Vi pratite njihove kanale, a oni prate vaše.



### Pronađi altruističku osmatračnicu



Ako ne poznajete nikoga u vašoj blizini ko može pružiti uslugu osmatračnice, postoji niz altruističkih javnih osmatračnica na koje se možete povezati. Na primer, u ovom kursu LNP202, predlažem da se povežete sa uslugom osmatračnice koju zajednički nude LN+ i Voltage, koja je osmatračnica za LND.


Ovde imate podatke za prijavu:



- Putem Tor:


```txt
023bad37e5795654cecc69b43599da8bd5789ac633c098253f60494bde602b60bf@iiu4epqzm6cydqhezueenccjlyzrqeruntlzbx47mlmdgfwgtrll66qd.onion:9911
```



- Preko clearnet:


```txt
023bad37e5795654cecc69b43599da8bd5789ac633c098253f60494bde602b60bf@34.216.52.158:9911
```

Da biste im zahvalili što pružaju ovu besplatnu uslugu osmatračnice, [možete donirati putem Lightning-a](https://lightningnetwork.plus/donation).


Sada kada koristimo altruističku uslugu osmatračnice, hajde da vidimo kako da je konfigurišemo na našem LND čvoru pod Umbrel.


### Postavljanje osmatračnice


Iz aplikacije `Lightning Node` kliknite na tri tačke u gornjem desnom uglu interfejsa, a zatim izaberite `Advanced Settings`.


![Image](assets/fr/025.webp)


Zatim idite na meni `Watchtower`.


![Image](assets/fr/026.webp)



Aktivirajte opciju `Watchtower Client`, zatim kliknite na dugme `SAVE AND RESTART NODE`. Sačekajte da se LND ponovo pokrene.


![Image](assets/fr/027.webp)


Jednom kada se restart završi, vratite se na isti meni i unesite ID altruističke osmatračnice po vašem izboru u predviđeno polje. Zatim kliknite na dugme `ADD` da potvrdite. Takođe možete podesiti parametar `Watchtower Client Sweep Fee Rate`: ovo je stopa naknade koju ste spremni da platite za moguću pravnu transakciju koju emituje osmatračnica. Nema potrebe da birate previše visoku stopu, ali treba izbegavati i previše nisku stopu, jer u suprotnom pravna transakcija neće biti potvrđena na vreme.


Ponovo pokrenite svoj čvor koristeći dugme `SAVE AND RESTART NODE` da biste primenili ove promene.


![Image](assets/fr/028.webp)



Ako se vratite na isti meni, videćete da je vaš Lightning čvor sada zaštićen od strane stražarnice koju ste upravo dodali.



![Image](assets/fr/029.webp)



Altruistički osmatrač je generalno dovoljan, posebno ako ne stavljate velike količine novca na vaš Lightning čvor i ako dobro upravljate svojim čvorom (ne ostavljajte ga isključenim predugo). Za još veću sigurnost, možete dodati i nekoliko ponavljanjem istog procesa.



## Otvorite svoj prvi Lightning kanal


<chapterId>00642af7-8f3d-4a25-96d7-34e85de7bd5d</chapterId>



Ako ste stigli ovako daleko, već znate da je Lightning čvor bez kanala pomalo kao prazan wallet: postoji, ali je beskoristan. Da biste mogli slati ili primati uplate, vaš čvor mora biti povezan s barem jednim drugim čvorom u Lightning mreži putem kanala. U budućnosti, snažno preporučujemo otvaranje nekoliko kanala, zbog razloga otpornosti i efikasnosti rutiranja. U narednim poglavljima, takođe ćemo pogledati kako upravljati vašim likvidnim sredstvima, optimizovati vašu topologiju kanala i koristiti naprednije alate od osnovnog LND interfejsa na Umbrel.



Ali u ovom uvodnom poglavlju, cilj je jednostavno razumeti kako izabrati dobrog Lightning partnera, gde pronaći informacije koje su vam potrebne za odabir partnera, i na kraju kako otvoriti svoj prvi kanal putem osnovnog LND interfejsa.



### Kako odabrati dobrog Lightning peer-a?



Kada otvorite kanal, morate izabrati peer: drugi Lightning čvor sa kojim će vaš čvor biti direktno povezan, putem kanala. Ovaj izbor peer-a je važan, jer će imati direktan uticaj na:




- lakoća da vaša plaćanja pronađu svoj put;
- pouzdanost vaših kanala tokom vremena;
- vaši troškovi usmeravanja.



Ne postoji savršeno podudaranje za svakoga, ali postoji niz pouzdanih kriterijuma za identifikaciju dobrih kandidata.



#### 1. Povezanost čvorova



Dobar peer je čvor koji je dobro povezan sa Lightning mrežom. To znači ne samo imati veliki broj kanala (iako to može biti pokazatelj), već pre svega biti povezan sa drugim pouzdanim čvorovima i zauzimati dovoljno centralnu poziciju u grafu mreže.



Dobro povezan čvor povećava vaše šanse za pronalaženje efikasne rute do većine odredišta za plaćanje. Takođe smanjuje broj posredničkih čvorova koji su potrebni, što održava troškove niskim.



Suprotno tome, otvaranje vašeg prvog kanala ka izolovanom ili slabo povezanom čvoru može ograničiti vaše mogućnosti: moći ćete da platite ovom peer-u, ali će biti mnogo teže platiti ostatku mreže.



#### 2. Kapitalizacija i kapacitet kanala



Dobar peer je takođe dovoljno kapitalizovan čvor. Ovo se pokazuje kroz njegov ukupni kapacitet kanala (zbir sats posvećen svim njegovim kanalima) i njegov prosečan kapacitet kanala (često je bolje imati samo nekoliko dobro kapitalizovanih kanala nego mnogo malih).



Čvor sa smešnim kapacitetom, ili čiji su svi kanali mali, neće moći da usmerava plaćanja sa velikim iznosima, što će rezultirati neuspesima u usmeravanju za vas.



#### 3. Politike troškova



Svaki čvor postavlja svoje naknade za usmeravanje (`osnovna naknada` i `stopa naknade`). Dobar peer neće naplaćivati prekomerne naknade za strateške kanale. Za prvi kanal, najbolje je izabrati čvor sa prilično umerenim naknadama, kako ne biste ometali sopstvena plaćanja.



Zapamtite da i vaše sopstvene naknade za rutiranje utiču na to kako vas drugi doživljavaju kao partnera: čvor koji stalno menja svoje naknade ili nameće apsurdne troškove retko je cenjen.



#### 4. Stabilnost i senioritet



Stabilnost čvora je veoma važan kriterijum. Dobar čvor ima visok uptime (retko je offline), drži svoje kanale otvorenim dugo vremena i ne otvara/zatvara kanale konstantno bez razloga.



Stari i još uvek aktivni kanali su dobar signal: oni sugerišu da je veza profitabilna za partnera, da čvor zna kako da upravlja svojim kapitalom i da se ne zatvara u bilo kom trenutku, tako da ne morate stalno plaćati onchain naknade za zatvaranje i ponovno otvaranje.



Suprotno tome, vršnjak koji je često van mreže ili brzo zatvara kanale može biti izvor problema za vas i dodatnih troškova za otvaranje novih kanala.



Čak i sa ovim kriterijumima, nećete napraviti savršen izbor prvi put. To je normalno: pravi kvalitet saradnika se otkriva kroz njegovu upotrebu. Zato je važno da:




- pratiti aktivnost kanala (usmereni obimi, dostupnost, itd.);
- zatvorite kanale koji ne služe svrsi ili čiji su partneri prečesto van mreže;
- preusmerite svoj kapital ka boljim partnerima tokom vremena.



Ideja nije da se kanali otvaraju i zatvaraju svaki dan (što bi bilo skupo zbog onchain troškova), već da se vaša topologija postepeno razvija kako bi se konvergirala na skup pouzdanih, dobro povezanih vršnjaka koji su kompatibilni sa vašim potrebama.



### Kako da pronađem vršnjaka?



Da biste primenili ove kriterijume, biće vam potrebni alati koji omogućavaju preglednost Lightning mreže. Dostupno je nekoliko explorera i usluga za to. Među najpoznatijim Lightning explorerima su [1ML](https://1ml.com/) i [Amboss](https://amboss.space/).



https://planb.academy/tutorials/node/lightning-network/amboss-37044cad-0f85-41eb-af18-491384af1017

https://planb.academy/tutorials/node/lightning-network/1ml-37ada2ab-7a24-4473-87fd-007cb7640e7b

Ovde, međutim, predlažem da koristite [alat Lightning Terminal od Lightning Labs](https://terminal.lightning.engineering/), koji pruža rangiranje (dodouše zasnovano delimično na subjektivnim kriterijumima) Lightning čvorova koji se smatraju najrelevantnijim za otvaranje kanala.



![Image](assets/fr/030.webp)



Problem sa veoma velikim Lightning čvorovima na vrhu ove rang liste je što većina ne prihvata otvaranje kanala ispod veoma visokih iznosa. Mnogi takođe primenjuju stroge politike upravljanja peer-ovima, što može dovesti do zatvaranja vašeg kanala. S druge strane, ovi čvorovi generalno nemaju potrebu za dolaznom likvidnošću, s obzirom na njihov broj konekcija.



Stoga bih vam savetovao da radite na spuštanju po rangu kako biste pronašli čvor koji je dobro povezan, pouzdan i dovoljno centralan u mrežnom grafu, a da nije previše veliki. Na primer, ovde sam identifikovao Lightning čvor na stacker.news, koji je veoma dobro povezan, ima visok kapacitet i zauzima centralnu poziciju u mrežnom grafu.



![Image](assets/fr/031.webp)



Još jedan zanimljiv pristup je otvaranje kanala ka čvoru kojem je potrebna dolazna likvidnost, kao što je trgovac kojeg poznajete, udruženje ili zajednica. Ova strategija ima tri prednosti:




- Pošto izabrani entitet treba dolaznu likvidnost, logično će imati manje podsticaja da zatvori vaš kanal bez razloga;
- Njegova ekonomska aktivnost povećava šanse za usmeravanje na ovom kanalu, a samim tim i za prikupljanje nekih naknada;
- Činiš uslugu ekosistemu i daješ dragocen doprinos drugim bitkoinerima.



Kada identifikujete relevantni čvor, možete preuzeti njegov ID čvora. Ovo je jednostavno konkatenacija javnog ključa čvora, separatora `@`, njegove IP ili Tor adrese i korišćenog porta. Ovaj ID je lako dostupan iz profila čvora na bilo kom Lightning pretraživaču.



### Otvorite svoj prvi kanal putem LND



Sada kada smo identifikovali čvor sa kojim ćemo otvoriti naš prvi kanal, potrebno je da sats zaključa u njega. Da biste to uradili, potrebno je da unesete Bitcoin onchain wallet povezan sa vašim LND.



Sa glavnog LND interfejsa, pronađite svoj `Bitcoin Wallet`, zatim kliknite na dugme `Deposit`. Onchain adresa za primanje je zatim generated: pošaljite sats na nju. Iznos koji treba da prenesete zavisi od kapaciteta koji želite da dodelite svom prvom kanalu, ali imajte na umu da treba da pošaljete nešto više od ciljanog kapaciteta. Na primer, ako želite da otvorite kanal od 500,000 sats, nemojte poslati tačno 500,000 sats, već veći iznos.



![Image](assets/fr/032.webp)



Jednom kada je transakcija emitovana, pojavljuje se u interfejsu. Sačekajte potvrdu pre nego što otvorite kanal. Videćete zelenu strelicu pored nje kada bude potvrđena.



![Image](assets/fr/033.webp)



Pomeri se dole do glavnog interfejsa, zatim klikni na `+ OPEN CHANNEL`.



![Image](assets/fr/034.webp)



Unesite `Node ID` čvora sa kojim želite da otvorite kanal, navedite iznos koji želite da zaključate, a zatim prilagodite naknadu za otvaranje transakcije prema stanju na tržištu naknada na lancu. Naravno, uverite se da imate dovoljno sredstava u svom LND onchain portfoliju unapred.



Kada su svi parametri postavljeni, kliknite na dugme `OPEN CHANNEL`.



![Image](assets/fr/035.webp)



Sačekajte da se početna transakcija potvrdi na lancu. Vaš prvi kanal je sada zvanično operativan: čestitamo!



Možete videti da je, za sada, 100% likvidnosti kanala na mojoj strani: to je normalno, jer sam ja taj koji je otvorio kanal. Kako se plaćanja i rutiranje razvijaju, ova distribucija će se promeniti, ali ukupni kapacitet kanala će uvek ostati isti.



![Image](assets/fr/036.webp)



Sada kada imate kanal, možete izvršiti svoje prve Lightning uplate, pod uslovom da je izabrani čvor pravilno povezan na mrežu. Naravno, u kasnijim poglavljima ćemo pogledati kako da postavite pogodniji metod plaćanja Lightning faktura sa vašeg mobilnog. Ali za sada, hajde da pokušamo izvršiti prvu uplatu direktno sa LND na Umbrel.



Da biste to uradili, u odeljku `Lightning Wallet`, kliknite na dugme `SEND`, zatim nalepite fakturu koju treba postaviti.



![Image](assets/fr/037.webp)



Iznos fakture je prikazan. Potvrdite uplatu klikom na dugme `SEND`.



![Image](assets/fr/038.webp)



Ako se pronađe važeća ruta, vaša prva Lightning uplata bi trebala biti uspešna.



![Image](assets/fr/039.webp)



Ako zatim pogledamo raspodelu likvidnosti u kanalu, vidimo da moj peer sada ima 5,002 sats na svojoj strani. Ovo odgovara na 5,000 sats plaćanja koje sam upravo izvršio, koje je on prosledio do čvora primaoca. Dodatnih 2 sats predstavljaju naknade za rutiranje koje sam platio, s obzirom da je primalac primio tačno 5,000 sats.



![Image](assets/fr/040.webp)



Da bismo poboljšali pouzdanost naših plaćanja, očigledno će biti potrebno otvoriti druge kanale. U zavisnosti od naših ciljeva, takođe ćemo morati pronaći način da omogućimo dolaznu likvidnost kako bismo mogli primati uplate putem Lightning-a. Ovo će biti tema sledećeg odeljka.



# Upravljanje vašim Lightning čvorom


<partId>e27c3e1e-487b-4414-ad6b-d67bdb91c7c5</partId>



## Definišite profil vašeg operatera čvora


<chapterId>d3b2e163-50f6-4d1d-a5fc-8fd177dfac76</chapterId>



Sada kada je vaš Lightning čvor pokrenut i radi, sledeći korak je definisanje vašeg profila trgovca. Ovo je važan izbor, jer određuje vašu strategiju otvaranja kanala, tip vršnjaka koje preferirate i način na koji upravljate likvidnošću.



Na Lightning-u, da bi ovo funkcionisalo, potrebna vam je likvidnost u pravom smeru. Odlazna likvidnost odgovara vašoj sposobnosti plaćanja (sats dostupno na vašoj strani kanala). Dolazna likvidnost odgovara vašoj sposobnosti primanja (sats dostupno na strani vaših partnera). Drugim rečima, vaš profil se svodi na jednostavno pitanje: većinu vremena, da li vaši sats napuštaju vaš čvor ili ulaze u njega?



### Potrošač



Ovo je profil velike većine korisnika. Koristite svoj čvor za obavljanje Lightning plaćanja: za kupovinu robe i usluga, plaćanje računa, slanje napojnica - ukratko, za korišćenje Lightning-a kao brzog sredstva plaćanja. S druge strane, primate malo od Lightning-a, ili samo marginalno, na primer nekoliko donacija, povraćaja između prijatelja ili nekoliko mikro-plaćanja.



Ovaj profil je najlakši za upravljanje, jer je vaša glavna potreba da budete u mogućnosti da plaćate. U praktičnom smislu, to znači da vam je potrebna odlazna likvidnost. Kada otvorite jedan ili više kanala odgovarajuće veličine ka stabilnim, dobro povezanim čvorovima, vaša odlazna plaćanja će mehanički premeštati likvidnost na drugu stranu vaših kanala. Upravo ovaj pokret prirodno stvara razumnu količinu dolazne likvidnosti. Kao rezultat, čak i ako ne planirate redovno primanje, i dalje ćete moći da primate s vremena na vreme bez implementacije složene strategije. Dakle, ne morate brinuti o svojoj dolaznoj likvidnosti.



U ovom kursu LNP202, fokusiraćemo se na ovaj profil operatera čvora "potrošač", jer on odgovara gotovo svim korisnicima Bitcoin na Lightning-u.



### Trgovac



Trgovac je, na neki način, suprotnost potrošaču. Ovde, glavni cilj nije platiti, već naplatiti. Poslovanje, pružalac usluga, online prodavnica ili prodajno mesto koje prihvata Lightning će primati mnogo dolaznih uplata, a izvršiti relativno malo odlaznih uplata sa ovog čvora.



Ovaj profil je zahtevniji, jer odbijena uplata na Lightning-u potencijalno predstavlja izgubljenu prodaju. Prioritet stoga postaje dolazna likvidnost. Ako vaš čvor nema dovoljno dolazne likvidnosti, vaši kupci će videti da njihove uplate ne uspevaju, čak i ako imaju sredstva, jednostavno zato što ne postoji ruta da se likvidnost usmeri ka vama u pravom smeru.



Glavni izazov za trgovca takođe dolazi iz prirodne evolucije kanala. Ako samo primate, vaši kanali će se postepeno popunjavati na vašoj strani. Dakle, potrebni su vam mehanizmi za održavanje i obnavljanje vaše dolazne likvidnosti.



Međutim, postoji jednostavniji slučaj: mešoviti profil potrošača/trgovca. Ako prikupljate putem Lightning-a, ali takođe trošite putem Lightning-a (poslovni troškovi, plaćanja dobavljačima ili čak lični troškovi), tada vaša odlazna plaćanja prirodno ponovo stvaraju dolazne. Upravljanje postaje lakše, jer se tokovi međusobno poništavaju, i imate manju potrebu da posežete za veštačkim mehanizmima dizajniranim isključivo za ponovno sticanje dolazne likvidnosti.



### Ruter



Ruter je specifičan profil. Ne koristi svoj Lightning čvor za plaćanje ili prikupljanje, već za usmeravanje plaćanja drugih ljudi i prikupljanje naknada. Cilj je biti korisna, pouzdana i ekonomski konkurentna ruta unutar Lightning grafa.



Da budem iskren s tobom, biti ruter na Lightning mreži je složeniji posao nego što izgleda, a profitabilnost je teško postići. Prvo, otvaranje i zatvaranje kanala je skupo zbog troškova na lancu. Da bi se efikasno rutiralo, često moraš prilagođavati svoju topologiju, testirati, zatvarati kanale koji ne donose rezultate, otvarati nove i redovno balansirati svoju likvidnost. Drugo, konkurencija je žestoka: veliki, etablirani čvorovi prirodno privlače veliki deo saobraćaja, i teško je steći uporište bez vezivanja značajnog kapitala u dobro dimenzionisanim kanalima.



Takođe postoji visok operativni zahtev. Čvor za rutiranje mora biti izuzetno stabilan, nadgledan, pravilno bekapovan i rigorozno upravljan. Morate pratiti performanse kanala, prilagoditi svoju politiku naknada, održavati uravnoteženu likvidnost, upravljati partnerima i brzo rešavati tehničke probleme. Ovaj nivo angažovanja može biti zanimljiv kao tehnički hobi ili kao doprinos infrastrukturi, ali ako je vaš cilj jednostavno koristiti Lightning na suvereni način, ulazak u rutiranje radi zarade retko je relevantan. Zato ovaj kurs LNP202 ne pokriva ovaj profil detaljno.



### Jasno se pozicionirajte pre nego što nastavite dalje.



Ako odgovarate potrošačkom profilu, vaš prioritet će biti mogućnost pouzdanog plaćanja uz jednostavno upravljanje. Ako ste trgovac, vaš prioritet će biti naplata bez greške, što podrazumeva strategiju sticanja dolazne likvidnosti. Ako razmatrate rutiranje, morate mu pristupiti kao zahtevnoj, ekonomski neizvesnoj i vremenski zahtevnoj aktivnosti.



Definisanje ovog profila sada će vam pomoći da izbegnete klasičnu zamku: primenu strategije kanala dizajnirane za trgovca ili rutera, kada ste jednostavno korisnik koji želi da plati.



## Korišćenje menadžera za Lightning čvorove


<chapterId>02eb4c09-d14b-4ff0-8b04-b90de3307d34</chapterId>



U prethodnom delu ovog LNP202 kursa obuke, koristili smo osnovni interfejs aplikacije `Lightning Node` na Umbrel. Ovaj interfejs je dovoljan za osnovne operacije (proveru stanja, pregled raspodele gotovine, otvaranje i zatvaranje kanala), ali je namerno veoma pojednostavljen. Ova jednostavnost ograničava dostupne opcije i ne omogućava pristup mnogim naprednim funkcijama vašeg LND čvora. Iz tog razloga, sada ćemo koristiti drugi, sveobuhvatniji softver za upravljanje Lightning čvorom.



Ovaj dodatni softver će jednostavno biti komplementarni upravljački interfejs za vaš čvor. To znači da možete nastaviti koristiti `Lightning Node` interfejs paralelno, pa čak i koristiti nekoliko različitih ako želite. Ovo su jednostavno različiti načini interakcije sa istim Lightning čvorom.



Među najpoznatijim softverskim programima su:




- [Alby Hub](https://albyhub.com/);
- [Vozite Munju](https://www.ridethelightning.info/);
- [ThunderHub](https://thunderhub.io/).



Sve tri su dobra rešenja. Ako želite, možete testirati sva tri sa svojim čvorom pre nego što izaberete ono koje vam najviše odgovara. Lično koristim ThunderHub iz navike i zato što mi deluje potpunije od ostalih. Ovo je alat koji ću predstaviti u ovom kursu obuke, ali možete izabrati i jednu od druge dve alternative. Imamo posvećen vodič za svaki od ovih programa na Plan ₿ Academy.



https://planb.academy/tutorials/node/lightning-network/thunderhub-16909a39-2484-408e-a118-4e34e249bb9a

https://planb.academy/tutorials/node/lightning-network/ride-the-lightning-ca007688-0653-490c-8349-81d330d744b5

https://planb.academy/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a

### Instaliraj ThunderHub



Ovi programi se mogu vrlo lako instalirati iz Umbrel App Store-a. Kao što sam rekao, ovde ćemo koristiti ThunderHub, ali ako kasnije želite da testirate neki drugi, procedura će biti slična.



![Image](assets/fr/041.webp)



Umbrel vam pruža podrazumevanu lozinku za pristup ThunderHub. Kopirajte je: trebat će vam odmah. Takođe zapamtite da je sačuvate u svom menadžeru lozinki, jer će se tražiti svaki put kada otvorite softver.



![Image](assets/fr/042.webp)



Kliknite na `Login`, zatim nalepite lozinku koju je dostavio Umbrel da biste se prijavili.



![Image](assets/fr/043.webp)



Bićete preusmereni na početnu stranicu ThunderHub, koja prikazuje glavne informacije o vašem Lightning čvoru.



![Image](assets/fr/044.webp)



Za početak, preporučujem da aktivirate dvofaktorsku autentifikaciju (2FA). U podešavanjima jednostavno kliknite na `Omogući` pored `Omogući 2FA`, zatim pratite uobičajeni proces.



![Image](assets/fr/045.webp)



### Koristi ThunderHub



ThunderHub je relativno lako naučiti. Svi meniji su dostupni iz leve kolone interfejsa. Da rezimiramo, evo šta svaki od njih radi:




- početna: pregled čvora, stanja i brze akcije;
- kontrolna tabla: prilagodljiva kontrolna tabla sa vidžetima i metrima;
- vršnjaci: pregled i upravljanje vezama s drugim Lightning čvorovima;
- kanali': kompletno upravljanje kanalima (likvidnost, naknade, zatvaranje, itd.);
- rebalance": alat za rebalansiranje kanala putem kružnih plaćanja;
- transakcije: istorija poslatih i primljenih Lightning uplata;
- forwards`: statistika usmeravanja i troškovi generated po vašem čvoru;
- `Chain`: Bitcoin onchain portfelj (UTXOs i transakcije);
- gW-201 integracija za nadgledanje i rezervnu kopiju;
- `Alati`: napredni alati (bekapi, izveštaji, makaruni, potpisi, itd.);
- zamena: Lightning/onchain zamene putem Boltz;
- `Stats`: ukupna statistika i performanse vašeg Lightning čvora.



Sa ovim skupom funkcija, imate sve alate potrebne za efikasno upravljanje vašim Lightning čvorom. Nije neophodno da odmah detaljno savladate svaku opciju: istraživaćemo ih postepeno tokom ovog kursa. Međutim, ako želite da se detaljnije upoznate sa softverom, pogledajte naš ThunderHub vodič:



https://planb.academy/tutorials/node/lightning-network/thunderhub-16909a39-2484-408e-a118-4e34e249bb9a

Meni koji nas ovde najviše zanima je `Channels`. On nudi detaljan pregled svih kanala u vašem čvoru, sa njihovom raspodelom likvidnosti. Konkretno, možete videti koji su kanali otvoreni u `Open`, koji čekaju da budu otvoreni ili zatvoreni u `Pending`, i koji su već zatvoreni u `Closed`.



![Image](assets/fr/047.webp)



Za dati kanal, možete kliknuti na ime partnera ili ID kanala da otvorite njegovu Amboss stranicu i dobijete više informacija. Takođe možete kliknuti na ikonu olovke da modifikujete parametre kanala, uključujući politiku naknada primenjenu na taj kanal ako vaš čvor usmerava uplate ka čvoru vašeg partnera.



![Image](assets/fr/048.webp)



Ako koristite svoj Lightning čvor uglavnom kao "potrošač", ne morate menjati ove naknade: možete zadržati podrazumevane vrednosti. S druge strane, ako želite bolje razumeti kako funkcionišu naknade za rutiranje na Lightning-u, preporučujem obuku LNP 201, a posebno poglavlje 4.1:



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

Klikom na mali krstić pored partnera, možete pokrenuti zatvaranje kanala. Ako primetite, na primer, da je partner redovno neaktivan, može biti prikladno zatvoriti ovaj kanal kako biste preusmerili svoj kapital na pouzdanijeg partnera.



Zatim imate dve opcije. Prva, i uvek poželjna, je kooperativno zatvaranje. Potvrđivanjem ove akcije, vaš čvor traži od vašeg partnera da zajednički zatvorite kanal. Ako on prihvati, možete emitovati transakciju zatvaranja na lancu i povratiti svoj deo sredstava. Prednosti ovog metoda su da birate naknade na lancu za transakciju, čime izbegavate nepotrebne troškove, i da se sredstva brže povrate, bez vremenskog zaključavanja.



![Image](assets/fr/049.webp)



Druga opcija je prisilno zatvaranje. U ovom slučaju, ne tražite saglasnost partnera i direktno emitujete poslednji commitment transaction koji imate. Ne bih preporučio ovu metodu osim ako nije poslednja opcija, na primer ako partner sistematski odbija kooperativna zatvaranja ili više ne odgovara. Prisilno zatvaranje ima dva glavna nedostatka: naknade su često veoma visoke, jer su unapred postavljene da predvide porast naknada na lancu, i postoji kašnjenje u povratu sredstava, jer su blokirana vremenskim zaključavanjem. Ovo vremensko zaključavanje daje vašem partneru vreme da reaguje u slučaju pokušaja varanja (što očigledno nije slučaj ovde, ali ipak morate čekati).



![Image](assets/fr/050.webp)



Konačno, da biste otvorili novi kanal, idite na meni `Home` i kliknite na `Open a Channel` u odeljku `Liquidity`. Zatim ćete moći da unesete ID izabranog čvora, kapacitet kanala, željenu Lightning naknadu za rutiranje i onchain naknadu za otvaranje transakcije.



![Image](assets/fr/051.webp)



Ovo su glavne radnje koje ćete morati izvršiti na ThunderHub. Otkrićemo druge funkcije kako budemo napredovali u ovom kursu LNP202.



## Dobijanje dolazne likvidnosti


<chapterId>b740c656-a897-4d95-af4b-116b718447cd</chapterId>



Kao što možete videti, imati odlaznu likvidnost za plaćanja na Lightning-u nije posebno složeno. Jednostavno otvorite kanale na svoju inicijativu ka drugim čvorovima i počnite slati sats. S druge strane, imati dolaznu likvidnost za primanje plaćanja na Lightning-u je komplikovanije, jer ili trebate da drugi čvorovi otvore kanale ka vama, ili trebate sami da premestite likvidnost vršenjem plaćanja.



Ako usvojite profil "potrošača", generalno nema potrebe da brinete o dolaznoj likvidnosti. Vaša upotreba Lightning čvora će biti pretežno orijentisana na plaćanja, a ne na uplatu. Jednostavnim izvršavanjem nekoliko Lightning plaćanja, prirodno ćete vremenom stvoriti dolaznu likvidnost.



S druge strane, ako imate profil "trgovca", situacija je obrnuta: uglavnom ćete prikupljati uplate i praviti ih malo. Dakle, ne možete se osloniti isključivo na sopstvene uplate za dolaznu likvidnost. Stoga postaje neophodno da drugi Lightning čvorovi otvore kanale ka vašem. Ali kako se to može postići? Kako naterati druge operatere da vežu kapital za vas? Upravo to ćemo istražiti u ovom poglavlju.



### Kupovina dolazne likvidnosti



Kao što biste očekivali, najefikasniji način da nekoga navedete da deluje jeste da ga platite. Za dolaznu likvidnost na vaš Lightning čvor, princip je potpuno isti. Najjednostavniji način da dobijete kanale za vaš čvor jeste da platite za uslugu i vezivanje kapitala koje je uključeno.



Ako ste preduzeće ili prodavac, ovaj pristup znači da možete brzo dobiti pouzdane kanale za prikupljanje uplata od svojih kupaca bez prepreka.



Postoji mnogo načina za kupovinu dolazne likvidnosti. Onaj koji lično koristim i preporučujem je Amboss-ova [Magma](https://magma.amboss.tech/) platforma. Veoma je jednostavna za korišćenje, otvaranje kanala je brzo i cene su generalno razumne. Magma funkcioniše kao tržište sa proizvođačima i korisnicima, ali verzija 2 je uveliko pojednostavila iskustvo: jednostavno kreirajte zahtev, platite cenu putem Lightning-a, i Magma ga automatski uparuje sa najboljom dostupnom ponudom. Nakon šest onchain potvrda, vaš kanal sa dolaznom likvidnošću je spreman za rad. Evo kako funkcioniše:



Idite na [Magma vebsajt](https://magma.amboss.tech/buy), u odeljak `Buy Channels`.



![Image](assets/fr/052.webp)



Ako želite, možete kreirati nalog da pratite svoje kupovine, ali to nije obavezno. Ako ne kreirate nalog, Magma će vam jednostavno dodeliti ID sesije, koji će vam omogućiti da kasnije preuzmete svoje kupovine.



Kada ste na sajtu, popunite potrebne informacije za kupovinu likvidnosti. Izaberite `Jednokratno` za jednokratnu kupovinu, zatim unesite iznos koji ste spremni da platite za dolaznu likvidnost. Što je veći plaćeni iznos, to je veći kapacitet kanala otvorenog prema vašem čvoru. Ispod se pojavljuje procena kapaciteta kanala: ovo je približna vrednost, jer će konačni iznos zavisiti od najbolje ponude koju pronađe Magma, koja je ponekad viša, ponekad niža.



![Image](assets/fr/053.webp)



Zatim unesite svoj ID čvora. Možete ga pronaći, na primer, u meniju `Node ID` aplikacije `Lightning Node` na Umbrel.



![Image](assets/fr/054.webp)



Kada su svi podaci popunjeni, kliknite na dugme `Pregledaj i otvori narudžbinu`.



![Image](assets/fr/055.webp)



Ako niste kreirali nalog, Magma će vam obezbediti sesijski ključ i rezervnu datoteku. Čuvajte ova dva elementa na sigurnom mestu, jer će vam omogućiti da kasnije preuzmete narudžbinu ili pratite njen status u slučaju problema. Kada sačuvate datoteku, kliknite na dugme `Plati sa Lightning`.



![Image](assets/fr/056.webp)



Magma zatim generates Lightning fakturu za iznos koji ste odabrali. Morate je platiti. Ako već imate kanale na vašem Lightning čvoru, možete platiti direktno sa njega, ili koristiti drugi eksterni Lightning wallet.



![Image](assets/fr/057.webp)



Jednom kada je uplata izvršena, transakcija se prikazuje kao da je u obradi u Magma interfejsu.



![Image](assets/fr/058.webp)



Nakon nekoliko minuta, zahtev je obrađen: kanal sa sats se otvara ka vašem Lightning čvoru. Kada transakcija otvaranja bude potvrđena na lancu, imaćete pristup odgovarajućoj dolaznoj likvidnosti.



![Image](assets/fr/059.webp)



Magma je takođe direktno integrisana u ThunderHub. U kartici `Home`, skrolujte dole do sekcije `Liquidity` i kliknite na `Buy Inbound Liquidity`. Sve što treba da uradite je da unesete željeni iznos i potvrdite. Ne morate ručno plaćati bilo kakve fakture, jer ThunderHub automatski preuzima brigu o plaćanju sa vašeg čvora.



![Image](assets/fr/060.webp)



Ako ste trgovac, ova vrsta usluge je posebno pogodna, jer vam omogućava da brzo dobijete veliku količinu dolazne likvidnosti od pouzdanih čvorova, garantujući da će vaši kupci moći da vam plate bez poteškoća. S druge strane, ako ste privatno lice ili ne želite da plaćate za dolaznu likvidnost, postoje i besplatna rešenja. Hajde da pogledamo.



### Kooperativna dolazna likvidnost



Ako niste trgovac, ali vam je i dalje potrebna dolazna likvidnost (na primer, da pokrenete svoj čvor pri startovanju, dok čekate da se izvrše neka plaćanja), ne morate nužno da platite za to. Jedno od mojih omiljenih rešenja je da sarađujem sa drugim operaterima čvorova kojima je takođe potrebna dolazna likvidnost, kako bismo otvarali Lightning kanale jedni za druge. Na ovaj način, otvaranje kanala vam donosi odlaznu likvidnost, dok vam istovremeno obezbeđuje dolaznu likvidnost, besplatno (uz izuzetak onchain naknada za otvaranje).



Naravno, možete to dogovoriti direktno sa kolegama bitkoinerima. Međutim, postoji platforma posvećena ovoj vrsti kružnog otvaranja: [Lightning Network +](https://lightningnetwork.plus/). Princip nije otvaranje dva kanala između istih osoba, već postavljanje kružnih otvaranja koja uključuju najmanje tri učesnika, ili čak više.



Hajde da uzmemo primer da bismo razumeli kako Lightning Network + funkcioniše:




- Operator čvora, po imenu `A`, objavljuje najavu u kojoj navodi da želi da otvori kanal od 1 milion sats sa dve druge osobe;
- Oglas ostaje aktivan dok se ne dodaju dalji učesnici;
- Kasnije, dva operatera, `B` i `C`, pridružuju se najavi čvora `A`. Trougao je sada kompletan i faza otvaranja može početi.
- Čvor `A` otvara kanal ka čvoru `B`;
- Čvor `B` otvara kanal ka čvoru `C`;
- Čvor `C` otvara kanal ka čvoru `A`.



Na kraju operacije, svaki čvor ima 1 milion sats odlazne likvidnosti i 1 milion sats dolazne likvidnosti. Ova šema se može proširiti na četiri ili pet učesnika.



Naravno, ne postoji tehnički mehanizam koji garantuje da će učesnik zaista otvoriti kanal koji je obećao da će kreirati. Zato je platforma uspostavila sistem reputacije, zasnovan na pozitivnim ocenama kada operateri ispune svoje obaveze. A u najgorem slučaju, ako naiđete na nekoga ko ne sarađuje, nećete izgubiti novac: jednostavno ćete propustiti priliku za dolaznu likvidnost.



Ovo rešenje je posebno pogodno za profil "potrošača", jer vam omogućava da besplatno dobijete dolaznu likvidnost, dok povezujete vaš čvor sa drugim malim operaterima. S druge strane, ako ste trgovac, ovaj pristup generalno nije relevantan: svaki sat dolazne likvidnosti zahteva blokiranje sata odlazne likvidnosti, a vaše velike potrebe za dolaznom likvidnošću bi tada uključivale vezivanje previše kapitala.



Da biste koristili Lightning Network +, imate dve opcije: ili koristiti aplikaciju integrisanu u Umbrel, ili koristiti klasičan vebsajt i kreirati nalog prijavljivanjem sa vašeg čvora. Preporučujem ovo drugo, jer integrisana aplikacija ne nudi pun opseg dostupnih funkcija.



Idite na vebsajt [Lightning Network +](https://lightningnetwork.plus/) i kliknite na dugme `Login` u gornjem desnom uglu interfejsa.



![Image](assets/fr/061.webp)



Da biste se autentifikovali, potrebno je da potpišete poruku pomoću privatnog ključa vašeg Lightning čvora. Sa ThunderHub, ova operacija je veoma jednostavna. Počnite kopiranjem poruke prikazane od strane LN+.



![Image](assets/fr/062.webp)



U ThunderHub, idite na karticu `Tools`, zatim kliknite na dugme `Sign` u sekciji `Messages`.



![Image](assets/fr/063.webp)



Nalepite poruku za autentifikaciju koju pruža LN+, zatim kliknite na `Potpiši`.



![Image](assets/fr/064.webp)



ThunderHub zatim potpisuje ovu poruku koristeći privatni ključ vašeg čvora. Kopirajte generated potpis.



![Image](assets/fr/065.webp)



Nalepite ovaj potpis u odgovarajuće polje na LN+ sajtu, zatim kliknite na `Prijavi se`.



![Image](assets/fr/066.webp)



Sada ste povezani sa LN+ sa svojim Lightning čvorom. Ovaj proces omogućava LN+ da verifikuje da ste vi zakoniti vlasnik čvora koji tvrdite na njihovoj platformi.



![Image](assets/fr/067.webp)



Ako želite, možete personalizovati svoj LN+ profil, na primer dodavanjem kratke biografije.



Da biste učestvovali u svom prvom otvaranju kružnog kanala, idite na meni `Swaps` na vrhu interfejsa. Ovde ćete pronaći sve trenutno dostupne zamene, u zavisnosti od karakteristika vašeg čvora.



![Image](assets/fr/068.webp)



Da biste se pridružili postojećoj ponudi za zamenu, jednostavno kliknite na nju i registrujte se. Međutim, na LN+, kreator zamene može postaviti određene uslove za učesnike, kao što su minimalan broj kanala ili minimalni ukupni kapacitet čvora. Stoga je moguće, naročito u ranim danima, da će malo ponuda biti dostupno vašem čvoru. U mom slučaju, uprkos nekoliko već otvorenih kanala, nijedna ponuda nije bila dostupna za moj čvor. Zato sam kreirao svoju zamenu, i možete učiniti isto ako ste u istoj situaciji.



Kliknite na `Start Liquidity Swap`, zatim unesite parametre vaše ponude:




- Izaberite ukupan broj učesnika (3, 4 ili 5);
- Naznačite broj kanala koji treba otvoriti (proverite da li imate bar ovaj iznos na vašem onchain wallet);
- Definišite vreme otvaranja kanala. Ovo je period tokom kojeg se učesnici slažu da ih ne zatvaraju;
- Sa desne strane, možete postaviti ograničenja za učesnike: minimalan broj kanala, minimalan ukupni kapacitet i tip prihvaćene veze.



Kada su svi parametri postavljeni, kliknite na dugme `Start Liquidity Swap`.



![Image](assets/fr/069.webp)



Vaša ponuda za zamenu je sada kreirana. Sada sve što treba da uradite je da sačekate da se drugi operateri čvorova prijave. Ako vaši uslovi nisu previše restriktivni, ovo ne bi trebalo da potraje dugo. Ne zaboravite da pratite status vaše zamene u satima ili danima koji slede.



![Image](assets/fr/070.webp)



Sva mesta za zamenu su zauzeta: sada prelazimo na fazu otvaranja kanala. Svaki učesnik može videti, sa svog LN+ interfejsa, ka kojem čvoru treba da otvori Lightning kanal.



![Image](assets/fr/084.webp)



Na vašoj strani, otvorite kanal koristeći Node ID koji je dostavio LN+ i poštujući naznačeni iznos. Kao što smo videli u prethodnim poglavljima, to možete učiniti ili putem ThunderHub, sa drugim menadžerom Lightning čvora, ili direktno iz osnovnog interfejsa aplikacije Lightning Node.



![Image](assets/fr/085.webp)



Jednom kada je otvaranje pokrenuto, možete ga videti u odeljku kanala na čekanju. U mom slučaju, to je kanal sa čvorom `Plebian_fr`.



![Image](assets/fr/086.webp)



Zatim se možete vratiti na LN+ da potvrdite da ste započeli otvaranje kanala. Jednostavno kliknite na dugme `Channel Opening Started`.



![Image](assets/fr/087.webp)



Kada svi ostali učesnici takođe otvore kanal na koji su se obavezali, ne zaboravite da im ostavite pozitivan pregled.



![Image](assets/fr/088.webp)



U slučaju poteškoća ili kašnjenja, možete direktno kontaktirati svoje kolege putem odeljka za komentare na dnu stranice.



![Image](assets/fr/089.webp)



Neki učesnici možda žele da rebalansiraju kružne kanale od samog početka, tako što će izvršiti uplatu sebi. Ovo osigurava uravnoteženu distribuciju gotovine u svakom kanalu. Ako ste u "potrošačkom" profilu, ovo nije neophodno, ali možete sami izvršiti ovo rebalansiranje ako želite, ili privremeno postaviti naknade za kanal na nulu kako biste olakšali vršnjaku koji to želi da uradi. Ponekad niko ne želi to da uradi.



![Image](assets/fr/090.webp)




# Oslobađanje potencijala vašeg Lightning čvora


<partId>8dcc24b1-6eb9-4a5f-a56b-8a823e5ac0fd</partId>



## Povežite mobilni wallet preko Tailscale


<chapterId>5fefb222-3f50-4f9d-a170-2ea628be4437</chapterId>



To je to, sada imate dobro povezan Lightning čvor, sa dolaznom i odlaznom likvidnošću. Dakle, spremni ste da koristite svoj Lightning čvor u stvarnom životu. Do sada smo uvek koristili interfejse direktno na Umbrel, bilo aplikaciju `Lightning Node` ili interfejs `ThunderHub`. Ovi alati rade za slanje i primanje uplata, ali očigledno nisu optimizovani za svakodnevne Lightning uplate. Interfejs je dizajniran za korišćenje na računaru, nepraktičan na pametnom telefonu, i takođe zahteva povezivanje na istu mrežu da bi pravilno funkcionisao (iako je tehnički moguće povezati se daljinski putem Tor-a).



U praksi, ono što tražimo kao bitkoineri je klasičan Lightning wallet interfejs na pametnom telefonu: mogućnost skeniranja faktura putem QR koda i jednostavan interfejs za plaćanje i isplatu sats. Upravo to ćemo implementirati u ovom i narednom poglavlju. Opšta ideja je da imate mobilnu Lightning wallet aplikaciju na svom pametnom telefonu, koja se može koristiti sa bilo kog mesta (ne samo sa vaše lokalne mreže), ali koja u pozadini oslanja na vaš sopstveni Lightning čvor za slanje i primanje uplata.



### Koja su rešenja za povezivanje mobilnog korisnika?



Danas postoji nekoliko načina za to, kako u smislu mobilne aplikacije, tako i u pogledu vrste veze između vašeg čvora i ove aplikacije. Tri glavna načina povezivanja su:




- putem ***Tor***;
- preko VPN-a ***Tailscale***;
- putem ***Nostr Wallet Connect***.



Pre nekoliko godina, koristio sam ***Tor*** za povezivanje, ali sam brzo prestao: broj grešaka i kašnjenja u komunikaciji bili su preveliki. U teoriji, to funkcioniše, ali u praksi, korisničko iskustvo je bilo katastrofalno. Stoga bih savetovao protiv ovog pristupa.



Alternativa koju sam tada usvojio bila je korišćenje ***Tailscale*** VPN-a kako bih osigurao komunikaciju između mobilne aplikacije i čvora. Ovo rešenje funkcioniše veoma dobro: čak i na mobilnim mrežama sa niskim protokom, moja plaćanja uvek prolaze bez poteškoća. Ovo je metoda koju ću prvo predstaviti u ovom poglavlju, sa Zeus aplikacijom.



U narednom poglavlju, pogledaćemo još jedno, novije rešenje, koje takođe veoma dobro funkcioniše: ***Nostr Wallet Connect***. Ovog puta, koristićemo aplikaciju Alby Go da vam predstavimo alternativu, iako je Zeus takođe kompatibilan sa NWC ako želite.



### Instalacija i konfiguracija Tailscale



Za ovaj prvi metod, trebaće nam Tailscale. Ovo je VPN rešenje zasnovano na WireGuard, koje vam omogućava da bezbedno povežete uređaje rasprostranjene širom Interneta, dok automatski upravlja enkripcijom, autentifikacijom i NAT prolazom. Jednostavno rečeno, to je kao da su svi vaši uređaji povezani na istu LAN mrežu kao i vaš ruter, iako mogu biti bilo gde na Internetu.



Da biste ga koristili, prvo kreirajte nalog. Idite na Tailscale vebsajt, zatim kliknite na dugme `Get Started`.



![Image](assets/fr/071.webp)



Zatim izaberite provajdera identiteta za vaš Tailscale nalog. Lično, koristio sam jedan od svojih GitHub naloga za prijavljivanje.



![Image](assets/fr/072.webp)



Kada se prijavite, bićete upitani nekoliko pitanja o vašem korišćenju. Odgovorite na njih ukratko da biste nastavili.



![Image](assets/fr/073.webp)



Tailscale zatim nudi instalaciju klijenta na vašem računaru. Trenutno, to nije ono što nas zanima: idite direktno na Umbrel i instalirajte aplikaciju Tailscale iz App Store-a.



![Image](assets/fr/074.webp)



Kada se aplikacija otvori, kliknite na `Log In`, zatim pratite proces autentifikacije, koristeći isti metod kao kada ste kreirali svoj nalog.



![Image](assets/fr/075.webp)



Kliknite `Connect` da potvrdite. Vaš Umbrel je sada povezan na vašu VPN mrežu.



![Image](assets/fr/076.webp)



Zatim preuzmite aplikaciju Tailscale na svoj pametni telefon i prijavite se koristeći isti nalog. Napomena: na Androidu nije moguće koristiti dva VPN-a istovremeno. Da bi Tailscale radio, moraćete da onemogućite bilo koji drugi aktivni VPN. Štaviše, svaki put kada želite da koristite svoj Lightning čvor putem Zeusa, moraćete da aktivirate Tailscale VPN, inače veza neće biti uspostavljena.



![Image](assets/fr/077.webp)



Na lokaciji Tailscale, sada kada su povezani najmanje dva klijenta, možete pristupiti administrativnoj konzoli sa spiskom svih vaših uređaja povezanih na mrežu i njihovim Tailscale IP adresama.



![Image](assets/fr/078.webp)



### Poveži Zeusa



Instalirajte Zeus aplikaciju na vaš telefon. Kada se otvori, izaberite `Advanced Setup`, zatim `Create or connect a wallet`.



![Image](assets/fr/079.webp)



U odeljku `Wallet interface`, izaberite `LND (REST)`. Zatim unesite Tailscale adresu vašeg Umbrel, koju možete pronaći na Tailscale kontrolnoj tabli ili direktno u Tailscale aplikaciji na Umbrel. Za port unesite `8080`.



![Image](assets/fr/080.webp)



Zeus zatim traži da obezbedite `Macaroon`. Ovo je autorizacija token koja vam omogućava da precizno definišete prava dodeljena aplikaciji (u ovom slučaju Zeus) za interakciju sa vašim Lightning čvorom. Moguće je generate macaroon iz ThunderHub, u meniju `Tools`, podmeniju `Bakery`, ali za ovu svrhu, najlakši način je da ga preuzmete direktno iz aplikacije `Lightning Node`.



Kliknite na tri male tačke u gornjem desnom uglu interfejsa, zatim na `Connect Wallet`. Izaberite `REST (Local Network)`. Tada ćete moći da kopirate macaroon sa odgovarajućim pravima.



![Image](assets/fr/081.webp)



Zalepite ga u odgovarajuće polje u Zeus, zatim kliknite na dugme `SAVE WALLET CONFIG`.



![Image](assets/fr/082.webp)



Sada možete pristupiti svom Lightning čvoru iz Zeus aplikacije. To znači da možete generate fakture za primanje uplata direktno na vaš Lightning čvor sa vašeg pametnog telefona, kao i plaćati Lightning fakture gde god se nalazite.



![Image](assets/fr/083.webp)



Savet: Tailscale nije ograničen na korišćenje vašeg Lightning čvora na daljinu. Omogućava vam pristup svim alatima vašeg Umbrel iz drugog softvera, čak i na daljinu. Na primer, možete koristiti Tailscale IP adresu vašeg Umbrel da povežete vaš Bitcoin čvor (preko Electrs ili Fulcrum) sa Sparrow Wallet, bez korišćenja Tor-a. Još jednom, ovo izbegava sporost svojstvenu Tor-u. Jednostavno instalirajte Tailscale klijent na vaš računar i povežite ga na vašu mrežu.



https://planb.academy/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

U sledećem poglavlju, pogledaćemo još jedan, podjednako efikasan način povezivanja mobilnog klijenta sa vašim Lightning čvorom: Nostr Wallet Connect. Koristićemo drugačiju aplikaciju od Zeusa (iako je Zeus takođe kompatibilan sa NWC), naime Alby Go.



## Povežite mobilni uređaj wallet putem NWC


<chapterId>f5c97e43-e66e-4ba3-bcc9-fee1a04fc7f4</chapterId>



Ako niste uvereni u vezu Tailscale, ili ako vam upravljanje dvostrukim VPN-om deluje kao prevelika gnjavaža, ovo poglavlje predlaže drugi način korišćenja udaljenog mobilnog klijenta za plaćanje i primanje sats putem vašeg Lightning čvora: ***Nostr Wallet Connect***.



Za ovaj primer, koristićemo mobilnu aplikaciju Alby Go, koja je veoma dobro dizajnirana i posebno laka za učenje. To rečeno, možete koristiti i Zeus ili bilo koju drugu mobilnu aplikaciju kompatibilnu sa NWC. Listu kompatibilnih aplikacija možete pronaći na [GitHub repozitorijumu `awesome-nwc`](https://github.com/getAlby/awesome-nwc).



### Kako funkcioniše Nostr Wallet Connect?



Nostr Wallet Connect je standardizovani protokol koji omogućava aplikaciji ili veb-sajtu da pokrene radnje na udaljenom Lightning čvoru, bez uspostavljanja direktne mrežne veze sa tim čvorom (nema API LND izloženih, nema VPN, nema `.onion` servisa...). NWC definiše kako aplikacija formuliše nameru (npr. `pay_intece`) i prima rezultat.



Radi prilično jednostavno. Inicijalizujete sesiju skeniranjem QR koda ili putem deeplinka `nostr+walletconnect:`. Ovaj string sadrži parametre sesije i autorizacioni tajni ključ. Zatim, kada aplikacija želi da izvrši plaćanje, ona serijalizuje zahtev, enkriptuje ga i objavljuje kao događaj na Nostr releju. Čvor čita događaj na releju, dekriptuje ga, proverava da li je autor ovlašćen za ovu sesiju, izvršava plaćanje, a zatim vraća enkriptovani odgovor (uspeh sa preimage-om, ili greška). Relej deluje samo kao posrednik u transportu: ne može pročitati sadržaj, ali može posmatrati vreme i učestalost zahteva.



U poređenju sa vezom putem Tailscale ili Tor-a, glavna prednost NWC-a je što vaš čvor nije direktno dostupan spolja. Ovo uveliko pojednostavljuje mobilnu upotrebu: vaš čvor ne mora prihvatati dolazne veze, već samo treba da može komunicirati sa relejem. S druge strane, uvodite funkcionalnu zavisnost od Nostr releja: ako oni nisu dostupni, iskustvo se pogoršava. Takođe, čak i ako su poruke šifrovane, relej može posmatrati određeni nivo metapodataka aktivnosti.



Razlika u sigurnosnim modelima je takođe važna. Sa Tailscale ili Tor, izlažete direktan pristup vašem čvoru (preko API ili LND) zaštićen visoko osetljivim tajnama. Ovo je moćno, jer možete upravljati svime, ali je takođe površina napada na nižem sloju. Sa NWC, pristup je više aplikativan: delegirate sesiju token koja ovlašćuje samo određene akcije.



### Instalirajte Alby Hub na vašem Lightning čvoru



Ranije je postojala aplikacija posebno posvećena NWC konekcijama u Umbrel App Store-u, ali nažalost više nije dostupna. Sada ćete morati koristiti Alby Hub za uspostavljanje ove vrste konekcije. Da biste to uradili, počnite instaliranjem Alby Hub aplikacije direktno iz prodavnice.



![Image](assets/fr/091.webp)



On opening, skip the introductory screens, then click on the `Get Started (LND)` button. It's important to check that it says `LND`, not `LDK`, in brackets. If `LND` appears, this means that Alby Hub has correctly detected your existing Lightning node and will configure itself as the interface for it. On the other hand, if `LDK` is displayed, this indicates that Alby Hub has not detected your node and is about to create a new one, which is not the aim here.



![Image](assets/fr/092.webp)



Bićete zatim zamoljeni da postavite Alby nalog. Za upotrebu ograničenu na NWC, ovo nije neophodno, ali možda ćete želeti da to uradite ako želite da iskoristite specifične usluge Alby. Ako ne, kliknite na `Možda kasnije` da nastavite.



![Image](assets/fr/093.webp)



Zatim izaberite jaku, jedinstvenu lozinku. Ovo će zaštititi pristup Alby Hub na vašem čvoru. Ne zaboravite da je sačuvate u svom menadžeru lozinki.



![Image](assets/fr/094.webp)



Ovo vas dovodi do Alby Hub interfejsa. Ne morate prolaziti kroz ceo proces konfiguracije, osim ako želite da ga koristite kao glavnog menadžera vašeg Lightning čvora. Kao što smo ranije videli, Alby Hub može zapravo zameniti upotrebu ThunderHub za administraciju vašeg čvora. Ako želite da saznate više o opcijama Alby Hub, pogledajte naš posvećeni vodič:



https://planb.academy/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a

Idite na meni `Connections`.



![Image](assets/fr/095.webp)



Ovde možete videti sve aplikacije koje se mogu povezati sa vašim Lightning čvorom putem NWC. To uključuje Zeus, već pomenut u prethodnom poglavlju. Ovde ćemo koristiti Alby Go. Kliknite na Alby Go, zatim na dugme `Connect to Alby Go` da biste započeli proces povezivanja.



![Image](assets/fr/096.webp)



### Instalacija i povezivanje Alby Go



Na svom pametnom telefonu instalirajte aplikaciju Alby Go:




- [Google Play Store](https://play.google.com/store/apps/details?id=com.getalby.mobile);
- [Apple App Store](https://apps.apple.com/us/app/alby-go/id6471335774);
- [Zapstore](https://zapstore.dev/apps/naddr1qvzqqqr7pvpzq3jhml5fvklgnq9fxpete767txn9zfzqdkc0sxfptmnchfrexje7qqfxxmmd9enk2arpd338jtndda3xjmr9pzj5tk).



U Alby Hub, konfigurišite prava koja želite da dodelite aplikaciji Alby Go na vašem Lightning čvoru. Možete, na primer, postaviti limite potrošnje po periodu, datum isteka za NWC link, ili ostaviti potpunu kontrolu. Kada postavite parametre, kliknite na dugme `Next`.



![Image](assets/fr/097.webp)



Alby Hub zatim generates QR kod da uspostavi NWC vezu između vašeg Lightning čvora i Alby Go.



![Image](assets/fr/098.webp)



Na aplikaciji Alby Go, kada se prvi put otvori, kliknite na `Poveži Wallet`, zatim skenirajte QR kod koji je dostavio Alby Hub.



![Image](assets/fr/099.webp)



Izaberite ime za identifikaciju ovog wallet. Sada imate daljinski pristup svom Lightning čvoru putem Alby Go. Možete generate fakture da primate sats na svom čvoru, ili direktno postaviti Lightning fakture sa njim.



![Image](assets/fr/100.webp)



Na primer, poslao sam 1543 sats sa interfejsa Alby Go.



![Image](assets/fr/101.webp)



Ako odem na osnovni interfejs svog Lightning čvora na Umbrel, mogu videti da je ova uplata zaista izvršena putem mog čvora.



![Image](assets/fr/102.webp)



Sada znate kako lako koristiti svoj Lightning čvor sa bilo kog mesta.



## Dugotrajna autonomija na Lightning-u


<chapterId>691a0942-b46d-482a-8fbc-fe19b3814992</chapterId>



Sada smo došli do kraja ovog LNP202 praktičnog kursa. Sada imate osnove koje su vam potrebne da koristite Lightning Network na suveren način: razumete pravu ulogu čvora, kompromise različitih pristupa, i postavili ste LND instancu na Umbrel sa doslednom strategijom bekapa i zaštite. Takođe ste otvorili svoje prve kanale, naučili kako da upravljate likvidnošću, kako bi vaša plaćanja bila pouzdana na dnevnoj bazi.



Sa operativne tačke gledišta, vaš čvor bi sada trebalo da uđe u ritam održavanja. Glavna stvar je pratiti ga (uptime, sinhronizacija, status kanala, neuspeh plaćanja, itd.), primeniti ažuriranja koja nudi Umbrel kada su dostupne stabilne verzije, i periodično proveravati da li su vaši bekapi i konfiguracija watchtower-a još uvek aktivni.



Kada su u pitanju kanali, pristupite pragmatično: zadržite one koji su vam korisni, zatvorite one koji su trajno neaktivni ili povezani sa nestabilnim partnerima, i postepeno preusmeravajte svoj kapital ka robusnijoj topologiji.



**Jedna od najčešćih zamki u ovoj fazi je alokacija previše kapitala na vaš Lightning čvor. Imajte na umu da je vaš Lightning čvor mnogo manje siguran od hardverskog wallet, i da dostupnost sredstava posvećenih vašim kanalima zavisi od rezervnih mehanizama koji su i dalje nesavršeni. Stoga je veoma važno držati se razumnih iznosa, koje možete priuštiti da izgubite u slučaju problema, i uvek držati većinu vašeg sats na onchain hardverskom wallet.



Što se tiče alata, preporučujem da ostanete radoznali i pažljivi prema novim razvojem. Na ovoj obuci smo otkrili nekoliko njih, bilo za upravljanje vašim čvorom, njegovom povezivošću ili daljinskom upotrebom za plaćanja. Međutim, Lightning je posebno dinamično polje. Svake godine se pojavljuju novi i relevantni alati, a mnoge nove aplikacije se takođe pojavljuju na Umbrel. Praćenje ovih novih razvoja može vam omogućiti da otkrijete moćnija ili praktičnija rešenja od onih predstavljenih na ovom kursu.



Na obrazovnom planu, ako to već niste učinili, toplo vam savetujem da pohađate kurs teorije LNP 201 koji vodi Fanis Michalakis, posvećen radu Lightning Network. To će vam pomoći da bolje razumete manipulacije koje se izvode u ovom kursu LNP202, i pružiti vam veće samopouzdanje u svakodnevnom upravljanju vašim čvorom.



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

U drugačijem pravcu, ali jednako bitno za vaše bitcoin putovanje, takođe preporučujem odličan kurs Ludovica Larsa o istoriji stvaranja Bitcoin.



https://planb.academy/courses/a51c7ceb-e079-4ac3-bf69-6700b985a082

Ali pre nego što pređete dalje, možete napisati recenziju ovog kursa LNP202 i, naravno, uzeti diplomu da potvrdite da ste razumeli sav njegov sadržaj.



# Završni deo


<partId>683c998f-ba0a-4ffb-a7e8-4cd8369cb9b3</partId>



## Recenzije i Ocene


<chapterId>aec048c7-7130-425d-8eca-9cd7f90c27f3</chapterId>



<isCourseReview>true</isCourseReview>

## Završni ispit


<chapterId>3951ccbb-14a3-4322-b81b-8dd2a6da19cb</chapterId>



<isCourseExam>true</isCourseExam>

## Zaključak


<chapterId>30cd6309-5139-40d9-8927-92de0f76414a</chapterId>



<isCourseConclusion>true</isCourseConclusion>