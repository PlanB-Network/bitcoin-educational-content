---
name: 1ML
description: Naučite kako koristiti 1ML explorer za razumevanje i analizu Bitcoin Lightning mreže.
---
![cover](assets/cover.webp)



## Uvod



Lightning Network je brzo, niskotroškovno rešenje za plaćanje izgrađeno na vrhu Bitcoin, omogućavajući trenutne, sigurne transakcije. Posmatranje ove mreže je ključno za razumevanje kako funkcioniše, njene topologije i stanja čvorova koji je čine. Lightning explorer, kao što je 1ML, koristi se za vizualizaciju javnih podataka mreže, uključujući aktivne čvorove, otvorene kanale i dostupni kapacitet, pružajući vredan pregled za korisnike, programere i operatere čvorova.



## Pristupite 1ML i razumite početnu stranicu



Da biste pristupili 1ML, jednostavno otvorite svoj web pregledač i upišite [https://1ml.com](https://1ml.com). Ovo vas vodi na početnu stranicu, koja služi kao globalna kontrolna tabla Lightning Network.



![capture](assets/fr/03.webp)



Ova stranica prikazuje nekoliko važnih statistika na vrhu ekrana, uključujući :





- Ukupan broj aktivnih čvorova na mreži, tj. računara uključenih u slanje i primanje Lightning uplata.
- **Broj otvorenih kanala**, koji odgovaraju vezama između ovih čvorova omogućavajući transfer sredstava.
- Ukupni kapacitet mreže, izražen u bitcoinima (BTC), koji označava zbir kapaciteta svih javnih kanala.



Ove brojke se redovno ažuriraju kako bi odražavale trenutno stanje mreže. One daju uvid u njenu veličinu, rast i robusnost.



![capture](assets/fr/04.webp)



Neposredno ispod, stranica nudi liste sa rangiranjima:





- **Najpovezaniji čvorovi**, koji imaju najviše otvorenih kanala ka drugim čvorovima.
- **Najveći kapaciteti** na čvorovima, označavajući koji čvorovi mogu preneti najveće količine.
- Najvažniji kanali u smislu kapaciteta.



Filteri se takođe mogu koristiti za preciziranje ovih lista prema geografskoj lokaciji ili drugim kriterijumima.



Ova stranica je idealna početna tačka za istraživanje Lightning Network i razumevanje njegove opšte topologije.



![capture](assets/fr/05.webp)



![capture](assets/fr/06.webp)



## Istraživanje Lightning čvorova



Da biste istražili čvor na 1ML, počnite korišćenjem trake za pretragu na vrhu stranice. Možete uneti **ID čvora**, tj. jedinstveni identifikator čvora, ili njegov **alias**, što je ime koje je lakše zapamtiti.



Kada se pretraga završi, kliknite na odgovarajući čvor da biste pristupili njegovoj detaljnoj stranici.



![capture](assets/fr/07.webp)



Na ovoj stranici prikazano je nekoliko važnih informacija:





- ID čvora**: ovaj jedinstveni identifikator je dugačak niz karaktera koji omogućava da se čvor precizno identifikuje u celoj mreži.



![capture](assets/fr/08.webp)





- Alias**: ovo je ime koje je vlasnik čvora izabrao da ga javno predstavlja.



![capture](assets/fr/09.webp)





- **Broj kanala** označava koliko veza čvor ima otvoreno sa drugim čvorovima, dok **ukupni kapacitet** predstavlja zbir bitkoina dostupnih u tim kanalima. Čvor sa velikim brojem kanala i visokim kapacitetom je generalno dobro povezan i sposoban za brzo prenošenje velikih količina novca preko mreže.



![capture](assets/fr/10.webp)





- **Uptime**, ili dostupnost, meri koliko dugo je čvor ostao aktivan i dostupan na mreži, odražavajući njegovu pouzdanost. **Starost** čvora, s druge strane, pokazuje koliko dugo je prisutan na mreži, odražavajući njegovu stabilnost i iskustvo unutar Lightning Network.



![capture](assets/fr/11.webp)



Ovi podaci pomažu vam da razumete važnost i pouzdanost čvora u Lightning Network. Na primer, čvor sa velikim brojem kanala, visokim kapacitetom i visokim vremenom rada često je glavni igrač u mreži.



## Istraživanje kanala munje



### Šta je Lightning kanal?



Lightning kanal je direktna veza između dva mrežna čvora. Omogućava ovim čvorovima razmenu trenutnih, niskotarifnih uplata bez prolaska kroz Bitcoin glavni lanac za svaku transakciju. Kanali su osnova koja čini Lightning Network brzim i skalabilnim.



### Pročitajte informacije o kanalu na 1ML



Na 1ML, svaki kanal ima svoju stranicu ili opisni list koji sadrži niz važnih podataka:



Sa stranice čvora, možete pristupiti listi njegovih kanala. Klikom na kanal, 1ML prikazuje posebnu stranicu sa nekoliko ključnih informacija.



![capture](assets/fr/12.webp)



![capture](assets/fr/13.webp)



Glavni vidljivi podaci su sledeći:





- Čvorovi partneri**: svaki kanal povezuje dva čvora. 1ML prikazuje oba identifikatora i njihove odgovarajuće alijase.



![capture](assets/fr/14.webp)





- Kapacitet kanala**: ovo je ukupna količina bitkoina zaključanih u ovom kanalu. Ovaj kapacitet predstavlja maksimalni limit plaćanja koja mogu proći kroz ovaj kanal.



![capture](assets/fr/15.webp)





- Starost kanala**: označava koliko dugo je kanal otvoren. Stari kanal je često znak stabilnog odnosa između dva čvora.



![capture](assets/fr/16.webp)



### Ograničenja vidljivosti kanala



Važno je razumeti da 1ML prikazuje samo **deo** Lightning Network. Explorer prikazuje samo **javne kanale**, tj. one koji su najavljeni na mreži. Privatni kanali, koji se često koriste iz razloga poverljivosti ili strategije, nisu vidljivi. Nadalje, 1ML ne prikazuje tačnu raspodelu sredstava na svakoj strani kanala, niti izvršene uplate, niti stvarno dostupnu likvidnost u datom trenutku. Prikazane informacije se stoga mogu koristiti za analizu **opšte strukture mreže**, ali ne i njene stvarne finansijske aktivnosti ili detaljnog statusa likvidnosti.



## Istraži Lightning Network po lokaciji



### Čvorovi po zemljama i regionima



1ML vam omogućava da istražujete Lightning Network prema **geografskoj podeli**. Sa početne stranice ili putem posebnih sekcija, moguće je prikazati čvorove po zemlji ili regionu. Ova funkcija se zasniva na informacijama o lokaciji koje su prijavili operateri čvorova.


U navigacionoj traci, videćete link **Lokacija**. Na stranici, čvorovi su grupisani po kontinentu, državi i gradu.



![capture](assets/fr/17.webp)



Odabirom zemlje, 1ML prikazuje listu povezanih čvorova, zajedno sa agregiranim statistikama kao što su broj čvorova i ukupni vidljivi kapacitet za tu geografsku oblast.



#### Šta ovo govori o lokalnom usvajanju





- Usvajanje tehnologije**: Veliki broj čvorova u regionu ukazuje na to da korisnici Bitcoin, kompanije ili usluge aktivno usvajaju Lightning Network. Ovo pokazuje tehnološku zrelost i spremnost da se iskoriste prednosti Lightning-a (brze transakcije, niži troškovi).
- Ekonomski ekosistem** : Gusta prisutnost čvorova može takođe signalizirati lokalnu ekonomsku strukturu oko Bitcoin: trgovci koji prihvataju Lightning, startupi koji razvijaju alate, događaji zajednice, itd.
- Bezbednost i otpornost**: Raznovrsna geografska distribucija poboljšava otpornost mreže u slučaju lokalnih prekida ili ograničenja. Što su čvorovi rasprostranjeniji, mreža je decentralizovanija i teže ju je cenzurisati.
- Politike i propisi**: Neke zemlje mogu brže usvojiti zahvaljujući povoljnom regulatornom okviru ili proaktivnoj zajednici. Suprotno tome, u područjima gde su propisi strogi ili neprijateljski, broj čvorova će biti manji.



#### Granice geografskih podataka



Međutim, imajte na umu da geolokacija Lightning čvorova ima svoja ograničenja i pristrasnosti:





- Približna IP lokacija**: 1ML generalno koristi javnu IP adresu čvorova za procenu njihove lokacije. Međutim, ovaj metod može biti iskrivljen korišćenjem VPN-ova, cloud servera (AWS, Google Cloud), ili hostovanjem u zemljama koje se razlikuju od stvarnog prebivališta vlasnika čvora.
- Virtuelni čvorovi**: Neki operateri hostuju svoje čvorove na udaljenim serverima zbog pouzdanosti i dostupnosti, što može dati lažni osećaj fizičke lokacije.
- Mobilnost korisnika**: Operater čvora može promeniti lokaciju, premestiti svoju infrastrukturu ili otvoriti nekoliko čvorova u različitim regionima, što čini čitanje podataka složenijim.
- Nevidljivost privatnih čvorova**: Neki čvorovi ne objavljuju svoju IP adresu ili koriste metode za skrivanje svoje lokacije, što onemogućava geolokaciju.



## 1ML slučajevi upotrebe betona



### Razumevanje mrežne topologije



1ML vam omogućava da vizualizujete **opštu strukturu Lightning Network**. Posmatranjem veza između čvorova, broja kanala i ukupnog kapaciteta, moguće je razumeti kako je mreža organizovana, koji čvorovi igraju centralnu ulogu i kako tokovi plaćanja teoretski mogu cirkulisati.



Ovo razumevanje je ključno ako želimo da razumemo kako Lightning Network funkcioniše, i ne samo za korišćenje u portfoliju.



### Identifikujte važne čvorove



Zahvaljujući rangiranju koje nudi 1ML (najpovezaniji čvorovi, najveći kapacitet, starost), moguće je identifikovati čvorove koji zauzimaju važno mesto u mreži. Ovi čvorovi često služe kao glavne kapije za Lightning uplate.



![capture](assets/fr/18.webp)



### Proverite javnu vidljivost čvora



Za operatera čvora, 1ML omogućava da proverite da li je vaš čvor **javno oglašen** na Lightning Network. Ako se čvor pojavljuje na 1ML, to znači da je vidljiv i dostupan drugim čvorovima za otvaranje javnih kanala.


Ovo može biti korisno za dijagnostikovanje problema sa vidljivošću ili povezivanjem.



### Posmatranje kako se Lightning Network razvija tokom vremena



Upoređivanjem globalnih statistika tokom različitih perioda, 1ML nam omogućava da posmatramo evoluciju Lightning Network: povećanje ili smanjenje broja čvorova, varijacije u ukupnom kapacitetu ili promene u geografskoj distribuciji.


Ova zapažanja nude zanimljivu perspektivu o rastu, zrelosti i trendovima Lightning Network.



## 1ML najbolje prakse i ograničenja



### Javni podaci ≠ potpuna stvarnost



1ML se zasniva isključivo na **javno objavljenim** podacima o Lightning Network. To znači da alat prikazuje samo deo stvarnosti. Mnogi kanali mogu biti privatni, neki čvorovi možda nisu oglašeni, a stvarna likvidnost dostupna u kanalima nije vidljiva. Stoga je neophodno koristiti 1ML kao alat za globalnu analizu, a ne kao iscrpnu reprezentaciju mreže.



### Privatnost i Lightning



Lightning Network je dizajniran sa snažnim fokusom na **privatnost plaćanja**. Pojedinačne transakcije nisu vidljive na 1ML, a tačni saldi kanala nisu javni. Ovo ograničenje nije greška istraživača, već osnovna karakteristika Lightning Network, dizajnirana da zaštiti privatnost korisnika.



### Ne donosi zaključke prebrzo



Čvor sa visokim kapacitetom ili mnogo kanala nije nužno "pouzdaniji" ili "efikasniji" u svim slučajevima. Slično tome, privremeni pad ukupnog kapaciteta mreže ne znači nužno strukturni problem. Brojke treba uvek tumačiti sa retrospektivom i staviti u kontekst.



### Komplementarnost sa drugim alatima



1ML je odlična početna tačka za istraživanje Lightning Network, ali je najbolje koristiti ga u kombinaciji sa drugim alatima kao što su Lightning portfoliji, interfejsi za upravljanje čvorovima i drugi istraživači. Ovaj pristup pruža potpuniji i nijansiraniji pogled na mrežu.



## 1ML opcija povezivanja (napredna funkcionalnost)



1ML nudi opciju **prijave / kreiranja naloga**, vidljivu na sajtu, ali ovo **nije neophodno** za pregled Lightning Network podataka. Sve funkcije o kojima je do sada bilo reči u ovom vodiču dostupne su **bez naloga**.



Veza je prvenstveno namenjena **operaterima Lightning čvorova**. Konkretno, omogućava da čvor bude povezan sa 1ML nalogom kako bi se upravljalo određenim javnim informacijama, kao što su prezentacija čvora, kontakt linkovi i drugi metapodaci. Ova funkcija je dizajnirana da poboljša vidljivost i identifikaciju čvora unutar istraživača.



Važno je napomenuti da 1ML **nije usluga čuvanja sredstava**. Kreiranje naloga ne omogućava pristup sredstvima, kanalima ili plaćanjima čvora. Služi samo za interakciju sa pretraživačem sa deklarativnog i informativnog stanovišta.



U kontekstu učenja ili otkrivanja Lightning Network, ova opcija se stoga može smatrati **opcijom** i rezervisana je za napredniju upotrebu.



## Zaključak



1ML je vredan alat za posmatranje i razumevanje Lightning Network iz njegovih javnih podataka. Omogućava vam da istražite strukturu mreže, analizirate čvorove i kanale, i pratite celokupnu evoluciju usvajanja Lightning Network tokom vremena. Bez potrebe za nalogom ili rukovanjem sredstvima, 1ML nudi pristupačan pristup za svakoga ko želi da produbi svoje razumevanje kako Lightning funkcioniše.


Ako želite da idete dalje sa Lightning Network, preporučujem kompletan kurs Uvod u Lightning Network:



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb