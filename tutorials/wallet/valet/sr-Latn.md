---
name: Valet Bitcoin
description: Valet donosi nekustodijalni Lightning čvor u vaš džep
---

![cover_valet](assets/cover.webp)



## Uvod


Valet je lagan, samostalni, Bitcoin i Lightning wallet koji nudi jednostavan i praktičan proces prijave za početnike. Posebno je prilagođen za Bitcoin zajednice i kružne ekonomije, posebno u udaljenim područjima.


To je fork od **Simple Bitcoin Wallet (SBW)**, sa naprednom funkcijom Hosted Lightning kanala pod nazivom **Fiat Channels**, dizajniranom da omogući svakome prihvatanje Lightning plaćanja bez rizika od volatilnosti.


Valet je trenutno dostupan samo za Android uređaje i može se preuzeti i instalirati sa nekoliko open-sourced prodavnica aplikacija. Međutim, Valet **nije** dostupan na **Google Play Store-u** zbog zabrinutosti za privatnost programera i KYC.



## Preuzmi i instaliraj Valet


Valet se može preuzeti kao APK datoteka sa Standard Sats' GitHub stranice. [Standard Sats](https://standardsats.github.io/) je kompanija koja je razvila Valet.


👉 Da biste preuzeli Valet, posetite Standard Sats [GitHub stranicu](https://github.com/standardsats/valet/releases), i pronađite **najnovije** izdanje (Ovo je često ono na vrhu).


👉 Idite na **Assets** i kliknite na datoteku sa samo **.apk** ekstenzijom. Vaše preuzimanje će automatski početi.


![Standard_Sats_GitHub_page_view](assets/en/001.webp)


👉 Kada se preuzimanje završi, idite na **Upravljač datotekama** > **Preuzimanja** na svom uređaju i odaberite Valet apk datoteku.


![Select_valet_apk](assets/en/002.webp)


👉 Instalirajte ga i za nekoliko sekundi vaša aplikacija će biti spremna i pojaviće se na vašem početnom ekranu.


![valet_icon_on_homescreen](assets/en/003.webp)


Alternativno, možete preuzeti Valet i iz **F-Droid** prodavnice aplikacija. Ako nemate F-Droid aplikaciju na svom uređaju, možete je preuzeti i instalirati [ovde](https://f-droid.org/en/).


👉 Na početnom ekranu otvorite F-Droid i potražite **Valet**. Izaberite prvu opciju sa **ljubičastom i belom ikonicom** od dve opcije koje će se pojaviti, i kliknite na **Preuzmi**.


![F-Droid_icon_on_homescreen](assets/en/004.webp)


![search_and_download_Valet](assets/en/005.webp)


👉 Nakon preuzimanja, kliknite na **Install** i pratite uputstva na ekranu. Kada je instalacija završena, možete pokrenuti Valet sa F-Droid klikom na **Open**, ili ga pokrenuti sa početnog ekrana vašeg uređaja.



## Kreiranje Bitcoin Wallet


Možete postaviti Bitcoin wallet na Valet u dva jednostavna koraka.


👉 Pokrenite Valet sa početnog ekrana vašeg uređaja ili iz aplikacije F-Droid. Pojaviće se ekran za podešavanje wallet, sa dve opcije: **Kreiraj novi Wallet** i **Vrati postojeći Wallet**.


👉 Odaberite **Create New Wallet**, i odmah će biti kreiran novi wallet, i bićete preusmereni na početnu stranicu.


![set_up_a\_new_wallet](assets/en/006.webp)



## Napravite rezervnu kopiju vaše seed fraze


👉 Na početnoj stranici wallet, kliknite na **Green karticu** koja ima natpis **"Dodirnite da sačuvate wallet frazu za oporavak u slučaju da ikada izgubite ili zamenite svoj uređaj".**


![seed_phrase_green_card](assets/en/007.webp)


👉 Niz od 12 engleskih reči će biti prikazan. Zapišite ih na papir, redosledom od 1 do 12, i čuvajte ih na sigurnom.


![the_seed_phrase](assets/en/008.webp)


### Obrati pažnju ⚠️:


Obratite pažnju na sledeće elemente:


- Kao što već znate, Valet je samostalni čuvar wallet, tako da je vaša seed fraza jedini pristup za povratak vašeg Wallet.
- Ako ikada izgubite svoju seed frazu, **nikada** nećete dobiti pristup svom wallet.
- Ako neko dobije vašu seed frazu, može nepovratno ukrasti sve vaše Bitcoin.


Dakle, treba da zapišete svoju 12-rečnu seed frazu i čuvate je na sigurnom mestu. Nikada ne bi trebalo da pravite snimak ekrana, čuvate je kao nacrt u svom emailu ili je čuvate na bilo kom elektronskom uređaju koji je ikada bio povezan na internet.


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

## Primanje i slanje Bitcoins na Valet


Valet je samostalni skrbnički wallet sa mogućnostima on-chain i Lightning Bitcoin. To znači da možete primati i slati Bitcoin iz Valeta bilo putem **On-chain** ili putem **Lightning Network**.


Međutim, da biste mogli da primate ili šaljete Bitcoin putem Lightning-a, potrebno je da postavite Lightning kanal koristeći vaše on-chain Bitcoin-ove kao Liquiditet. Ili možete kupiti nešto likvidnosti Lightning kanala od prodavaca.



## Generisanje na lancu Bitcoin Address


Da biste primili Bitcoin kroz on-chain, moraćete da generišete Bitcoin adresu.


👉 Na početnoj stranici wallet videćete **Narandžastu** i **Ljubičastu karticu**, sa oznakama **Bitcoin** i **Lightning**.


👉 Kliknite na narandžastu karticu označenu kao **Bitcoin**. Bićete preusmereni na ekran koji prikazuje adresu Bitcoin.


![click_on_Bitcoin_card](assets/en/009.webp)


👉 Možete **kopirati** adresu i poslati je osobi koja vam šalje Bitcoins, ili kliknuti na dugme **deli** da biste poslali QR kod osobi putem društvenih mreža ili drugih komunikacionih kanala.


👉 Takođe možete kliknuti na dugme **Edit** da postavite količinu Bitcoins koja treba da bude poslata na tu adresu.


**Pažnja:** Kao i faktura, funkcija uređivanja je korisna u situacijama kada želite da primite određeni broj Bitcoin na adresu u određenom trenutku; međutim, to ne znači da adresa ne može primiti veće ili manje iznose.


👉Kliknite na **Više svežih adresa**, da generišete nove nasumične adrese.


![generating_a\_bitcoin_add](assets/en/010.webp)


👉 Takođe možete generisati on-chain Bitcoin adresu klikom na dugme **Receive** na dnu vaše wallet početne stranice. Zatim izaberite **Receive to bitcoin address**, i nastavite sa istim procesom kao gore.


![click_receieve_button](assets/en/011.webp)


![receive_to_bitcoin_address](assets/en/012.webp)



## Slanje Bitcoin putem On-chain


Slanje Bitcoin iz Valet wallet preko on-chain je jednostavan zadatak.


👉 Na dnu početne stranice vašeg wallet, kliknite na dugme **Send**, unesite adresu Bitcoin, ili kliknite na **Scan**, da skenirate QR kod adrese, zatim kliknite **Ok**.


![click_send_button](assets/en/013.webp)


![enter_bitcoin_add](assets/en/014.webp)


👉 Unesite iznos Bitcoin koji želite poslati. Možete ručno uneti iznos u terminima Sats ili u terminima fiat valute, ili možete kliknuti na **Max** da iskoristite sav svoj on-chain saldo.


👉 Takođe možete prilagoditi naknade koje želite da platite za transakciju klikom na mali zeleni okvir označen kao **naknada** i zatim pomeranjem bele tačke desno ili levo da povećate ili smanjite naknade, respektivno. Kliknite **U redu** da pošaljete transakciju.


![enter_amount_and_fee_rate](assets/en/015.webp)



## Postavljanje Lightning Network kanala


Kao što je gore pomenuto, Valet je samostalni kustodijalni Bitcoin i Lightning wallet; stoga, da biste mogli slati i primati Bitcoin putem Lightning mreže, prvo ćete morati postaviti Lightning kanal, prateći ove korake:


👉 Na početnom ekranu, kliknite na **Ljubičastu karticu** označenu kao **Lightning**. Bićete preusmereni na stranicu sa sledećim opcijama:



- Skeniraj čvor QR
- Kupovina na LNBIG.COM
- Kupovina na BITREFILL.COM
- Zahtev za ponovnu sinhronizaciju grafa LN.


Kada izaberete **Purchase from lnbig.com** ili **Purchase from bitrefill.com**, bićete preusmereni na vebsajtove ovih kompanija, gde možete kupiti dolaznu likvidnost različitih kapaciteta. Za sada zanemarite poslednju opciju **Request LN graph resync**.


Dakle, naš izbor ovde je da **Skeniramo QR čvor**. U ovom trenutku, morate biti odlučili i dobili **QR kod** čvora sa kojim želite da otvorite kanal. Možete otvoriti kanale ka bilo kom javnom čvoru po vašem izboru. Pogledajte [1ML](https://1ml.com/) ili [Amboss](https://amboss.space/), izaberite bilo koji javni čvor po vašem izboru i skenirajte povezani QR kod čvora koji ste izabrali.


![channel_opening_options](assets/en/016.webp)


👉 Bićete automatski preusmereni na sledeću stranicu, gde sada morate finansirati svoj kanal. Ponovo, korišćenje samostalnog čuvanja Lightning mreže zahteva da koristite svoje Bitcoins za finansiranje kanala. To znači da morate imati Bitcoins u svom on-chain wallet sa kojima ćete finansirati Lightning kanal. Molimo vas da pogledate ovaj članak od [Hacken](https://hacken.io/discover/lightning-network/), pročitajte više o Lightning mreži.


![fund_channel](assets/en/017.webp)


👉 Unesite **količinu** Bitcoins kojom želite da finansirate kanal, ili kliknite na **Max** da iskoristite sav svoj on-chain Bitcoin balans. Možete prilagoditi **naknadu**, ili ostaviti podrazumevanu postavku naknade, i kliknite **Ok**.


**Pažnja:** Iznos kojim finansirate kanal biće kapacitet vašeg novog kanala (tj. ukupna količina Sats koja može biti transaktovana ka i od tog kanala)


Takođe je važno da koristite preko **100,000 Sats** kao iznos finansiranja prilikom otvaranja kanala. To je zato što mnogi Lightning čvorovi zahtevaju minimalni kapacitet od 100,000 Sats za otvaranje kanala ka njima. Dakle, da biste izbegli pokušaje i greške, jednostavno koristite iznose veće od tog raspona.


![enter_funding_amount](assets/en/018.webp)


![funding_approval](assets/en/019.webp)


👉 U ovom trenutku, kada proverite svoju wallet početnu stranicu, videćete da je vaš iznos finansiranja sada premešten sa **Bitcoin kartice** na **Lightning karticu**. Na vašoj istoriji transakcija, videćete da se transakcija finansiranja obrađuje.


![channel_funding_processing](assets/en/020.webp)


👉 Ako kliknete na Lightning karticu, videćete informacije koje pokazuju da se vaš Lightning kanal otvara. Takođe ćete videti **transakciju finansiranja kanala** na vašoj listi transakcija. Sačekajte da vaša transakcija finansiranja bude potvrđena na blockchain, i vaš Lightning kanal će biti spreman.


![channel_opening](assets/en/021.webp)


👉 Čim transakcija finansiranja bude potvrđena, kliknite na **Lightning karticu** na vašoj početnoj stranici, i videćete informacije o vašem Lightning kanalu kako sledi:



- NASUMIČNI SKUP BROJEVA ODVOJENIH TAČKAMA:** Ovo su IP adrese čvorova. (IPV4 i IPV6, respektivno)
- KAPACITET:** Ovo je ukupna zapremina Sats koja može biti poslata i primljena kroz ovaj kanal
- MOŽEŠ POSLATI:** Ovo je količina Sats koju možeš poslati u ovom trenutku. Primetićeš da je to gotovo ista cifra kao i **Kapacitet**. To je zato što nisi poslao/la nijednu uplatu kroz kanal.
- MOŽE PRIMATI:** Ovo je broj Sats koji trenutno možete primiti na ovom kanalu. (Biće malo ili ništa u ovom trenutku jer da biste mogli primati, prvo morate poslati neki Sats da biste stvorili dolazni Liquiditet)
- REFUNDABLE:** Ovo prikazuje iznos koji se vraća na vašu on-chain adresu kada zatvorite vaš kanal. Ovo se takođe naziva vašim **Lokalnim stanjem kanala**. Primetite da je to samo malo manje od kapaciteta kanala, a to je zato što prilikom zatvaranja kanala morate platiti naknadu za objavljivanje transakcije zatvaranja na blockchain, baš kao što ste to učinili prilikom finansiranja kanala. Dakle, sistem je odbio približno najniži iznos koji ćete platiti.)
- VREDNOST U LETU:** Kada neko pošalje neki sats na vaš kanal, ili kada pokušate poslati neki sats nekome, i iz bilo kog razloga, transakcija je odložena, često se prikazuje u ovom polju.


![channel_info](assets/en/022.webp)


## Slanje Sats Kroz Vaš Kanal


Slanje Sats kroz Lightning Network je jednostavan zadatak.


👉 Na dnu početne stranice, kliknite na **Pošalji**, i **nalepite** Lightning fakturu (morate je biti kopirali) u predviđeno polje, ili kliknite na **Skeniraj** da skenirate QR kod Lightning fakture.


![click_send_or_scan](assets/en/023.webp)


Većina Lightning faktura dolazi sa unapred unetim iznosom za plaćanje. Ali u nekoliko slučajeva, to može biti otvorena faktura gde morate uneti iznos.


👉 Unesite iznos u **Dolarima** ili **Sats**, ili kliknite na **Max**, da iskoristite sav balans na vašem Lightning kanalu, a zatim kliknite **Ok**. Čim se pronađe dobra putanja, vaša uplata će biti poslata i završena u roku od nekoliko sekundi. Pratite početnu stranicu da vidite da li je uplata završena. Dobit će zelenu oznaku kada bude završena.


![enter_the_amount](assets/en/024.webp)


## Primanje Sats Kroz Vaš Kanal


Primanje uplata na vašem Lightning kanalu u velikoj meri zavisi od toga da li imate dolazni Liquidity ili ne. Nakon otvaranja kanala, nećete moći da primate uplate dok ne pošaljete barem neki Sats da biste **kreirali dolaznu likvidnost** na drugom kraju veze kanala. Da biste potvrdili da li možete primiti Sats i koliki iznos Sats možete primiti, proverite polje **Može Primiti** u informacijama o vašem kanalu. Ovo će vam pokazati koliko Sats primate u svakom trenutku.


Sada, pretpostavimo da ste poslali neki Sats sa svog kanala, sada imate dolaznu likvidnost i možete primati Sats.


Da biste primili na Lightning kanalu, moraćete da generišete fakturu. Za razliku od Bitcoin on-chain, koji koristi adrese, Lightning mreža koristi fakture. Postoje dva načina za generisanje fakture na Valet.


#### OPCIJA 1


👉 Na dnu početne stranice, kliknite na **Primi**, izaberite **Primi na Lightning fakturu**. Unesite iznos koji treba da bude primljen u fakturi, i kliknite **Ok**. Kopirajte fakturu ili podelite QR kod sa platiocem.


![receive_to_channel](assets/en/025.webp)


![fill_invoice_amount](assets/en/026.webp)


![copy_invoice_or_share_QR](assets/en/027.webp)


#### OPCIJA 2


👉 Kliknite na ljubičastu Lightning karticu na vašoj wallet početnoj stranici. Dodirnite bilo gde na vašem kanalu, i pojaviće se lista opcija. Izaberite **Primi na kanal** i unesite iznos koji primate (bilo u Sats ili dolarima). Takođe ćete videti koliko Sats možete primiti (prihvatni kapacitet) dok popunjavate fakturu. Kliknite **Ok** i kopirajte fakturu ili podelite QR kod sa platiocem.


![receive_to_channel](assets/en/028.webp)


**Pažnja:** Prva opcija je univerzalna opcija, što znači da ako imate više od jednog aktivnog kanala i koristite prvu opciju, sistem će automatski odabrati jedan od vaših kanala za primanje Sats.


Dakle, u ovom scenariju, druga opcija je najbolja za korišćenje ako želite da primite Sats na određeni kanal.


### Vaše Opcije Iskačućih Prozorčića Kanala Objašnjene


Kada dodirnete svoj kanal, prikazaće se sledeća polja opcija:


![channel_pop_ups](assets/en/029.webp)


**Podeli detalje o Lightning kanalu:** Ovo vam omogućava da podelite detalje o vašem kanalu, kao što su ID udaljenog partnera, lokalni ID kanala, transakcija finansiranja, datum kreiranja, itd.


**ZATVORI KANAL KA NOVČANIKU:** Možete zatvoriti svoj lightning kanal kad god želite. Da biste zatvorili kanal, sistem proverava Bitcoin saldo koji imate na svojoj strani kanala (setite se polja **"Može Poslati"**, poznatog i kao vaš lokalni saldo), i vraća ga vama. U Valet-u, možete izabrati gde želite da taj Bitcoin bude poslat kada se kanal zatvori. Dakle, **Zatvori kanal ka wallet** je jedna od vaših dve opcije.


👉 Kliknite ovu opciju i izaberite **Bitcoin**. Zatvaranje kanala će početi, a vaš saldo kanala Bitcoin biće poslat nazad na on-chain adresu vašeg wallet.


![close_channel_to_wallet](assets/en/030.webp)


**CLOSE CHANNEL TO ADDRESS:** Ovo je druga opcija za zatvaranje kanala. Kada izaberete ovu opciju, bićete upitani da unesete wallet adresu na koju će biti poslat Bitcoin balans sa vašeg kanala. Imajte na umu da u ovoj opciji možete samo skenirati QR kod Bitcoin adrese na koju želite da zatvorite kanal. Trenutno ne postoji opcija za ručno lepljenje adrese.


👉 Kliknite na ovu opciju, skenirajte adresu Bitcoin i kliknite **Ok**. Zatvaranje kanala će početi, a vaš Lightning Bitcoin saldo će biti poslat na adresu koju ste skenirali.


![scan_address_and_Ok](assets/en/031.webp)


**RECEIVE TO CHANNEL:** Ovo je isto kao generisanje fakture, ali u nekim slučajevima možete imati više od jednog kanala, uključujući Fiat kanale (jedinstvena vrsta Lightning kanala dostupna u Valet wallet). Dakle, ako imate otvoreno više kanala, ova opcija osigurava da možete primiti uplatu na određeni kanal.


**DOPUNA SA DRUGIH KANALA:** Ova opcija je funkcija koja vam omogućava da dopunite jedan kanal iz drugih postojećih kanala. Na primer, ako imate 2 različita Lightning kanala (A i B), i saldo Bitcoin na kanalu A je iscrpljen, sa ovom opcijom možete lako i automatski dopuniti saldo kanala A iz kanala B.


**DIRECT NOT PRIVATE RECEIVE:** Ovo je takođe opcija za generisanje fakture za primanje uplate, ali kada koristite ovu opciju, pošiljalac vam plaća direktno. To znači da uplata ne prolazi kroz različite čvorove pre nego što stigne do vas, kao što to radi normalna Lightning uplata. Dakle, u suštini, pošiljalac zna da je vama platio, zna vaš ID kanala, itd. Ova opcija se često može koristiti kada primate uplatu od izvora kojem verujete i ne morate da održavate svoju privatnost.


## Hostovani i Fiat Kanali


Kao i mnogi drugi Bitcoin wallet, Valet je jednostavan, lagan Bitcoin i Lightning wallet. Ali ima jedinstvenu Lightning funkciju koja ga razlikuje od većine drugih Bitcoin wallet. Ta funkcija se zove **Hosted and Fiat Channels**.


Fiat kanali su vrsta Lightning implementacije koja omogućava lako uključivanje i korišćenje Lightning mreže. To je kustodijalno rešenje koje omogućava potpunu anonimnost, baš kao i sa normalnim Lightning kanalom. Tehnologija fiat kanala takođe omogućava kreiranje Bitcoin derivata na Lightning mreži. Primer je da sa fiat kanalima, trgovci mogu prihvatati Bitcoin uplate stabilne vrednosti bez brige o volatilnosti Bitcoin.


Trenutna implementacija Fiat kanala na Valet-u omogućava kreiranje stabilnih sintetičkih Fiat valuta podržanih od strane Sats. Koristi odnos Domaćin-Klijent gde je Domaćin bilo koji Lightning čvor koji nudi ovu uslugu, a klijent je korisnik Valet-a. To je skrbničko rešenje jer su svi Sats na strani Domaćina; međutim, generisanje faktura, tor rutiranje i generisanje preimage-a i dalje se dešavaju na strani klijenta kao u normalnom Lightning kanalu.


Otvaranje Fiat kanala zahteva isti proces kao i otvaranje Lightning kanala. Jedina značajna razlika je što u ovom slučaju klijent (korisnik Valet-a) ne mora da obezbedi bilo kakvu likvidnost on-chain da bi kreirao kapacitet kanala. Domaćin postavlja kapacitet kanala i usmerava sve uplate za klijenta.


👉 Da biste otvorili Fiat kanal, kliknite na ljubičastu **Lightning karticu** na vašoj wallet početnoj stranici. Izaberite **Skeniraj Node QR** (U ovom trenutku, morate imati identifikovanog Domaćina kojem želite otvoriti kanal i dobiti QR kôd čvora. Primer Domaćina čvora kojem možete otvoriti Fiat kanal je SATM čvor od strane Standard Sats.)


**Pažnja:** Važno je napomenuti da svako može biti Host. Sve što vam je potrebno je da pokrenete Lightning čvor sa **Fiat channel pluginom** i **Hedging servisom**. Fiat kanali su open-source projekat od strane *Standard Sats*. Pročitajte više o tome [ovde](https://github.com/standardsats/fiat-channels-rfc) i [ovde](https://standardsats.github.io/).


SATM čvor QR ispod:


![SATM_node_QR](assets/en/032.webp)


👉 Kada skenirate QR kod čvora, kliknite na **Request USD fiat channel** ili **Request EUR fiat channels** (Ovo je fiat denominacija u kojoj će vaši Fiat saldi biti navedeni). Za sada, izaberite USD i kliknite **OK**. Kanal će biti automatski otvoren i možete odmah početi primati Sats. Vidite, tako je jednostavno!!!


![choose_fiat_denomination](assets/en/033.webp)


![channel_confirmation_prompt](assets/en/034.webp)


👉 Idite na početnu stranicu vašeg wallet, videćete **svetlo-zelenu** karticu označenu sa **USD**, to je vaš **Fiat kanal**.


![fiat_channel_card](assets/en/035.webp)


**Pažnja:** Kada primite Sats na Fiat kanalu, fiat vrednost primljenog Sats biće zaključana kao stabilan balans, dok će volumen Sats fluktuirati sa cenom Bitcoin. Ovo rešenje je prvenstveno dizajnirano za trgovce koji žele da prihvate Sats kao sredstvo plaćanja, ali ne žele da se suoče sa izazovima volatilnosti Bitcoin. Ovo im pomaže da održe stabilnu vrednost u svakom trenutku, dok i dalje mogu da obavljaju transakcije na Lightning mreži, uživajući u globalnom dosegu i brzom poravnanju Bitcoin kao sredstva razmene na Lightning Network.


Kada je vaš Fiat kanal kreiran, evo sledećih polja Vrednosti koja ćete videti i šta svako od njih znači:


![fiat_channel_info](assets/en/036.webp)



- NASUMIČNI SKUP BROJEVA ODVOJENIH TAČKAMA:** Ovo su IP adrese čvorova. (IPV4 i IPV6, respektivno)
- STOPA SERVERA:** Ovo je tržišna cena Bitcoin po kojoj Vam Domaćin nudi usluge. Ovo će često biti malo drugačije od preovlađujuće tržišne cene, jer Domaćin može dodati malu premiju. Potpuno je na Domaćinu da odluči o ovoj stopi; stoga, ona će se razlikovati od Domaćina do Domaćina.
- FIAT BALANCE:** Ovo je zaključana stabilna fiat vrednost svakog sata koji primite na ovom kanalu. Zapamtite, kao što je ranije objašnjeno, kad god primite Sats na vašem Fiat kanalu, fiat vrednost Sats u trenutku prijema se odmah zaključava kao sintetička stabilna fiat vrednost u ovom polju. Vaša **Fiat Balance** vrednost ne fluktuira sa tržišnom cenom Bitcoin. Kad god želite da izvršite plaćanja sa ovog kanala, možete poslati samo Sats ekvivalent ovog Fiat balansa. Dakle, razmislite o ovome kao o digitalnoj fiat valuti podržanoj od strane Sats.
- KAPACITET:** Ovo je ukupna zapremina Sats koja može biti poslata i primljena kroz ovaj kanal. (Ovo takođe postavlja Host. I za razliku od normalnog Lightning kanala, ova kapacitet može biti prilagođena od strane Hosta prema potrebi.)
- MOŽEŠ POSLATI:** Ovo je količina Sats koju možeš poslati u svakoj tački na osnovu tvog fiat balansa. Ovo je potpuno drugačije od onoga što imaš u normalnom Lightning kanalu, jer ova vrednost varira sa cenom Bitcoin. Dakle, ono što ovde vidiš je vrednost Sats tvog Fiat balansa u bilo kom trenutku na osnovu **Server Rate**.
- MOŽE PRIMITI:** Ovo je broj Sats koji možete primiti na ovom kanalu trenutno. Nakon što kreirate svoj kanal, ova vrednost bi trebalo da bude ista kao kapacitet kanala.
- VREDNOST U LETU:** Kada neko pošalje neki sats na vaš kanal, ili kada pokušate da pošaljete neki sats nekome, i iz bilo kog razloga, transakcija je odložena, često se prikazuje u ovom polju.


Evo važnih stvari koje treba napomenuti o Fiat kanalima:



- Za razliku od normalnog Lightning kanala, kada otvorite fiat kanal, možete odmah početi primati Sats, ali ne možete slati. Možete slati Sats samo kada ste primili Sats.
- U svakom trenutku, sredstvo koje se šalje i prima je Sats. *Fiat Balance* je samo sintetička IOU reprezentacija Bitcoin vrednosti primljene u bilo kom trenutku. Dakle, to nije kreacija token niti nova kriptovaluta.
- Fiat kanal je uglavnom koristan za trgovce/poslovanja koja su skeptična prema prihvatanju Bitcoin uplata zbog zabrinutosti za volatilnost. Takođe može biti koristan za kompanije koje žele da isplaćuju plate svojim radnicima u Bitcoin bez snošenja posledica volatilnosti Bitcoin, što može učiniti njihov kapital za plate nestabilnim. Takođe može biti koristan za pojedince koji žive u području sa pretežnom upotrebom Bitcoin, ali imaju fiksne troškove života.
- Primetite da ne postoji polje označeno kao **REFUNDABLE**. To je zato što, tehnički, ne možete zatvoriti Fiat kanal. Možete samo prestati koristiti Fiat kanal tako što ćete isprazniti njegov saldo na vaš normalni Lightning kanal.


### Vaše Fiat opcije za iskačuće prozore objašnjene


Kada dodirnete svoj Fiat Lightning kanal, biće prikazana sledeća polja:


![fiat_channel_pop_up](assets/en/037.webp)


**Podeli Detalje Hostovanog Kanala:** Ovo vam omogućava da podelite detalje vašeg Fiat kanala, kao što su ID udaljenog partnera, lokalni ID kanala, datum kreiranja, itd.


**IZVOZ STANJA KANALA:** Ovo vam omogućava da izvezete stanje kanala u bilo kom trenutku. Ovo je obično korisno za ispravljanje grešaka kanala, a domaćin može zatražiti da to podelite ako postoji potreba za tim.


**DRAIN CHANNEL BALANCE:** Kao što je ranije pomenuto, tehnički ne možete zatvoriti Fiat kanal, ali možete isprazniti saldo vašeg kanala u vaš postojeći normalni Lightning kanal. Ovo automatski prebacuje Sat ekvivalent vašeg Fiat salda u vaš normalni Lightning kanal.


**PRIMI NA KANAL:** Ovo je isto kao generisanje fakture, ali u nekim slučajevima, korisnik može imati više od jednog Fiat kanala sa različitim Domaćinima, uključujući normalne Lightning kanale. Dakle, ako korisnik ima otvoreno više kanala, ova opcija osigurava da mogu primiti uplatu na određeni kanal.


**REFILL FROM OTHER CHANNELS:** Ova opcija je funkcija koja omogućava korisniku da dopuni jedan kanal iz drugih postojećih kanala. Dakle, sa ovom opcijom, možete dopuniti vaš Fiat kanal iz normalnog kanala ili drugih Fiat kanala koje imate, na isti način kao što biste mogli isprazniti.


**DIRECT NOT PRIVATE RECEIVE:** Ovo je takođe opcija za generisanje fakture za primanje uplate, ali kada koristite ovu opciju, pošiljalac vam plaća direktno. To znači da uplata ne prolazi kroz različite čvorove pre nego što stigne do vas. Dakle, u suštini, pošiljalac zna da je vama platio, zna vaš ID kanala, itd. Ova opcija se često može koristiti kada primate uplatu iz izvora kojem verujete i ne morate da održavate svoju privatnost.


## Postavke Valeta:


Kao i svaka druga aplikacija, Valet ima postavke aplikacije koje možete prilagoditi svom ukusu. Možete pristupiti stranici sa postavkama sa početnog ekrana.


👉 Na početnom ekranu kliknite na ikonu **Zupčanik** koja se nalazi u gornjem desnom uglu ekrana da biste pristupili podešavanjima. Ispod su komponente u odeljku podešavanja.


![settings_icon](assets/en/038.webp)


**LOKALNO BEKAPOVANJE KANALA JE OMOGUĆENO:** Ako je ovo inače **Onemogućeno,** trebalo bi da ga omogućite jer je to jedini način da povratite svoje normalne Lightning kanale ako deinstalirate i ponovo instalirate Valet. Objasnićemo ovo kasnije. Dakle, kliknite na ovo i dajte Valet-u dozvolu za pristup vašoj **medijskoj memoriji** jer se tu čuva bekap fajl.


![app_permissions](assets/en/039.webp)


![enable_media_access](assets/en/040.webp)


**GDE ČUVATI LOKALNU REZERVNU KOPIJU:** Sve dok ste dali Valetu dozvolu za pristup vašoj memoriji, ovo polje će automatski biti postavljeno da čuva lokalne rezervne kopije u vašem folderu **Preuzimanja**. Ali možete ga promeniti klikom ovde i odabirom bilo kog foldera po vašem izboru.


**UPRAVLJAJTE LANCIMA NOVČANIKA** Ovo je malo tehnički, i ne morate se time baviti osim ako niste dovoljno iskusni. Podrazumevana postavka ovde je sasvim u redu.


**DODAJ HARDVERSKI NOVČANIK:** Takođe ne treba da brinete o ovome, osim ako nemate Hardverski wallet koji želite da povežete i pratite. Sa ovom postavkom, možete skenirati i povezati vaš hardverski wallet, kao što su Trezor ili Cold Kartica, i pratiti njegove aktivnosti. Ovo je funkcija samo za posmatranje, što znači da ne možete obavljati transakcije na Hardverskom wallet odavde. Možete samo posmatrati i pratiti aktivnosti, stanja itd. wallet.


**POSTAVI PRILAGOĐENI ELECTRUM ČVOR:** Ovo je takođe tehnički, i osim ako niste dovoljno upućeni, ne bi trebalo da se zamarate ovim. Podrazumevana postavka je sasvim dovoljna.


**BITCOIN JEDINICE:** Ovo je način na koji želite da se prikaže vaš Bitcoin saldo. Prva opcija prikazuje vaš saldo u Satoshi terminima, npr. 1,000,000 Sats, dok druga opcija prikazuje u BTC decimalnim tačkama, npr. 0.01BTC


**KORISTI PIN AUTENTIFIKACIJU** Ako označite ovaj okvir, moraćete da postavite PIN ili otisak prsta pomoću kojeg ćete se prijavljivati na vaš wallet i potvrđivati transakcije.


**KORISTITE TOR VEZU:** Ako označite ovu opciju, vaše transakcije će biti usmerene preko Tor mreže. To dodaje dodatni sloj privatnosti, ali može rezultirati kašnjenjem u obradi plaćanja, posebno za Lightning plaćanja.


**PRIKAZ FRAZE ZA OPORAVAK BIP39:** Ovde možete pristupiti svojoj 12-reči seed frazi za rezervnu kopiju. Dakle, ako je ranije niste zapisali ili ne možete pronaći gde ste je zapisali, sve dok još uvek imate pristup svom Wallet, možete je kopirati odavde.


**STATISTIKA KORIŠĆENJA:** Ovo vam prikazuje rezime svih vaših transakcija i aktivnosti od kreiranja wallet


![usage_stats](assets/en/041.webp)


## Wallet Oporavak


Valet je ne-kustodijalni wallet, tako da ako izgubite svoj uređaj ili deinstalirate svoju wallet aplikaciju, biće vam potrebno da izvršite oporavak wallet kako biste povratili svoje Bitcoin i Lightning kanale. Na početku ovog tutorijala, pomenuli smo važnost zapisivanja vaše **12-reči seed fraze** jer je to ključ za oporavak vašeg wallet. Ne postoje predstavnici korisničke podrške koji vam mogu pomoći da se vratite u svoj wallet.


Postoje dva važna alata potrebna za oporavak vašeg Valet wallet, u zavisnosti od toga da li ste imali aktivan Lightning kanal ili ne. Za korisnika koji nije imao aktivan normalan Lightning kanal, sve što mu je potrebno je njegova **12-rečena seed fraza**, prateći jednostavne korake ispod:


👉 Instaliraj novu Valet aplikaciju i pokreni/startuj aplikaciju.


👉 Odaberite **Restore Existing Wallet**


![restore_existing_wallet](assets/en/042.webp)


👉 Odaberite **Samo frazu za oporavak**.


![select_recovery_phrase](assets/en/043.webp)


👉 Unesite svoju frazu za oporavak od 12 reči i kliknite **OK**.


![input_12_words](assets/en/044.webp)


Vaš wallet će biti povraćen. U ovom slučaju, samo će vaš on-chain Bitcoin balans biti obnovljen.


Međutim, ako imate aktivan normalan Lightning kanal i povratite svoj wallet samo sa frazom za oporavak, vaš Lightning kanal će biti prinudno zatvoren, a svaki Bitcoin saldo koji imate na njemu automatski će biti poslat na vaš on-chain saldo.


Drugi način da povratite svoj Valet wallet, posebno ako ste imali otvoren normalan Lightning kanal pre nego što ste deinstalirali Valet, jeste da **koristite lokalnu rezervnu kopiju sačuvanu na vašem uređaju, zajedno sa vašom 12-rečnom seed frazom**. Ako koristite ova dva, stanje vašeg Lightning kanala će biti vraćeno, te vaš Lightning kanal neće biti prinudno zatvoren.


Evo koraka:


👉 Instaliraj novu Valet aplikaciju i pokreni/startuj aplikaciju.


👉 Izaberite **Restore Existing Wallet**.


👉 Izaberite **Backup + Recovery phrase**.


![select_backup_and_recovery_seed](assets/en/045.webp)


👉 Izaberite rezervnu datoteku iz upravitelja datoteka na vašem telefonu. (Po defaultu je uvek smeštena u vašoj fascikli **Preuzimanja**.)


![local_backup_file_in_download_folder](assets/en/046.webp)


Kada je ispravna rezervna datoteka odabrana, prikazaće se poruka koja potvrđuje da je **"Rezervna datoteka prisutna"**, a zatim će vas tražiti da unesete svoju 12-rečnu seed frazu.


![enter_12_words](assets/en/047.webp)


👉 Unesite svoju frazu za oporavak od 12 reči i kliknite **OK**. Bićete preusmereni na svoju wallet početnu stranicu.


👉 Sačekajte da se završi sinhronizacija mreže Bitcoin (**SYNC**) i sinhronizacija Lightning čvora (**LN Sync**), i vaš wallet će biti potpuno obnovljen, uključujući vaše Lightning kanale.


![LN_sync](assets/en/048.webp)


## Zaključak


Valet je uzbudljivo wallet rešenje, sa funkcijama koje ga čine pogodnim za uvođenje novih korisnika. Takođe ima Fiat kanal, ne tako novu tehnologiju koja osigurava integraciju fiat-poslovanja na Bitcoin standardu.


Preuzmite Valet danas i isprobajte ga!!! 🧡