---
name: Bitcoin Keeper - Plan nasleđivanja
description: Planirajte svoj prenos bitcoina sa Bitcoin Keeper
---

![cover](assets/cover.webp)



Prenos Bitcoin imovine je jedan od izazova koji vlasnici najviše potcenjuju. Za razliku od bankovnog računa, gde finansijska institucija može preneti sredstva zakonitim naslednicima, Bitcoin se u potpunosti oslanja na posedovanje privatnih ključeva. Savršeno legitiman zakonski naslednik nikada neće moći da pristupi sredstvima bez ovih ključeva, dok će zlonamerna osoba koja poseduje tajne moći da ih potroši bez ikakve formalnosti.



U ovom drugom Bitcoin Keeper vodiču, istražujemo premium funkcije posvećene planiranju imovine. Aplikacija nudi napredne alate za kreiranje Poboljšanih Seifova, sa vremenski ograničenim mehanizmima zaštite zahvaljujući Miniscript-u, kao i prateća dokumenta koja će voditi vaše voljene.



Ovaj vodič pretpostavlja da ste već savladali osnove Bitcoin Keeper (kreiranje portfolija, klasični multisig, dodavanje hardverskih ključeva) kako je objašnjeno u našem prvom tutorijalu :



https://planb.academy/tutorials/wallet/mobile/bitcoin-keeper-22cbfb8d-790f-4a6f-a92f-93a117e1e65c

![video](https://youtu.be/tCld_-n2d30)



## Planovi pretplate za Bitcoin Keeper



Bitcoin Keeper radi na freemium modelu sa tri nivoa pretplate koji nude progresivnu funkcionalnost. Da biste pristupili planovima, idite na karticu **Više**, zatim dodirnite svoj trenutni plan (podrazumevano je "Pleb") da biste otvorili ekran **Upravljanje pretplatom**.



![Plans d'abonnement](assets/fr/01.webp)



**Pleb plan** (besplatan) pruža pristup osnovnim funkcijama: neograničeno kreiranje novčanika sa jednim ključem i više ključeva, kompatibilnost sa svim glavnim hardverskim novčanicima (Coldcard, Trezor, Ledger, Jade, Tapsigner...), kontrola novčića, označavanje i povezivanje sa ličnim Electrum serverom. Ovaj plan je dovoljan za standardnu upotrebu, pa čak i za klasične multi-sig konfiguracije.



**Hodler plan** (€9.99/mesečno, uz 1 mesec besplatno ako se plaća godišnje) uključuje sve Pleb funkcije i dodaje šifrovane rezervne kopije u oblaku (iCloud ili Google Drive) za obnavljanje vaših sefova na bilo kom uređaju, Server Key za dodavanje automatskih politika potrošnje i 2FA iznad određenog praga, i Canary Wallets za otkrivanje neovlašćenog pristupa vašim ključevima.



**Diamond Hands plan** (€29.99/month, with 1 month free if paid annually) je kompletan paket za planiranje imovine. Uključuje ceo Hodler plan i otključava Ključ za nasledstvo (odložena aktivacija), Hitni ključ (hitni ključ za oporavak u slučaju gubitka), alate i dokumente za planiranje nasledstva, kao i poziv podrške sa Concierge timom za validaciju vaše konfiguracije. Ovo je ponuda za bitkoinere koji žele da prenesu svoje nasledstvo kroz nekoliko generacija.



Važna tačka: trezori koje ste kreirali ostaće dostupni čak i ako se vratite na besplatni plan. Vaše konfiguracije su zasnovane na otvorenim standardima (BSMS, Miniscript) i funkcionišu nezavisno od vaše pretplate.



## Dokumenti o nasleđivanju



Jednom kada aktivirate svoju pretplatu na Diamond Hands, pristupite odeljku **Dokumenti o nasleđu** iz kartice Više. Bitcoin Keeper pruža pet uzoraka dokumenata za strukturiranje vašeg plana imovine, kao i odeljak sa savetima:



![Documents d'héritage](assets/fr/02.webp)





- Šablon za Seed Reči**: šablon za uredno beleženje vaših fraza za oporavak na organizovan način
- Pouzdani Kontakti**: šablon za navođenje kontakt podataka pouzdanih osoba uključenih u vaš plan (notar, advokat, naslednici, čuvari ključeva)
- Dodatni Ključ Deonice**: dokument koji sadrži tehničke informacije za svaki ključ: PIN kod, putanja derivacije, fizička lokacija, tip uređaja i bilo koje druge informacije korisne za identifikaciju i korišćenje ključa
- Uputstva za oporavak**: korak-po-korak uputstva za naslednika ili korisnika za oporavak sredstava
- Pismo advokatu**: unapred popunjeno pismo koje se može prilagoditi vašem advokatu ili notaru



Deo **Saveti o Nasleđivanju** nudi praktične savete o obezbeđivanju ključeva za naslednike i optimizaciji vašeg plana nasleđivanja.



Prilagodite ove dokumente svojoj situaciji i čuvajte ih na sigurnom mestu, odvojeno od samih ključeva.



## Konfigurisanje Cloud Backup-a



Pre nego što kreirate svoj trezor za nasleđe, aktivirajte rezervnu kopiju u oblaku kako biste zaštitili svoje konfiguracione fajlove. Na kartici Više, pritisnite **Lična Rezervna Kopija u Oblaku**.



![Configuration Cloud Backup](assets/fr/03.webp)



Izaberite jaku lozinku za šifrovanje vaših rezervnih kopija. Ova lozinka štiti samo wallet konfiguracione fajlove (ne vaše privatne ključeve). Potvrdite lozinku i pritisnite **Potvrdi**. Vaše rezervne kopije će biti sačuvane na vašem iCloud-u ili Google Drive-u u zavisnosti od vašeg uređaja. Pritisnite **Napravi rezervnu kopiju sada** da pokrenete vašu prvu rezervnu kopiju.



## Uvezite svoje hardverske ključeve



Za naš primer, kreiraćemo sef 2-od-3 sa dva dodatna ključa (Nasledstvo i Hitni slučaj). Počnimo tako što ćemo uvesti sve potrebne ključeve u karticu **Ključevi**.



![Import des clés hardware](assets/fr/04.webp)



Pritisnite **Add key**, zatim izaberite **Add key from a hardware** da povežete hardver wallet. Bitcoin Keeper podržava mnoge uređaje: BitBox02, Coldcard, Blockstream Jade, Keystone, Krux, Ledger, Foundation Passport, TwentyTwo Portal, Seedsigner, i Specter Solutions.



U našoj konfiguraciji, uvozimo:




- 2 **Coldcard** ključa (MK4SP i MK4)
- 2 ključa **Tapsigner** (Metro i Genesis)



Da biste dodali Coldcard, izaberite ga sa liste i pratite uputstva na ekranu da biste izvezli javni ključ putem QR koda, fajla, USB-a ili NFC-a. Za više detalja o tome kako koristiti Coldcard ili Tapsigner, molimo vas da pogledate naše posvećene tutorijale:



https://planb.academy/tutorials/wallet/hardware/tapsigner-ab2bcdf9-9509-4908-9a4a-2f2be1e7d5d2

https://planb.academy/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3

https://planb.academy/tutorials/wallet/hardware/coldcard-5d44dd94-423d-4e37-9a8c-3fc38b45ce59


Kada se svi vaši ključevi uvezu, pronaći ćete ih na kartici Ključevi sa njihovim prilagođenim imenima.



## Kreiraj legacy wallet



Hajde da pređemo na kreiranje trunka. Na kartici **Wallets** pritisnite **Add Wallet**, izaberite **Bitcoin Wallet**, zatim **Create Wallet**.



![Création du wallet](assets/fr/05.webp)



Izaberite tip wallet. Za naš nasleđeni plan, izaberite **2 od 3 multi-key**. Na dnu ekrana, aktivirajte **Poboljšane opcije bezbednosti** zatim pritisnite **Nastavi**.



![Options de sécurité avancées](assets/fr/06.webp)



U iskačućem prozoru Poboljšane opcije bezbednosti, označite:




- Ključ nasleđa**: dodatni ključ koji će biti dodat kvorumu nakon određenog vremenskog perioda
- Hitni ključ**: ključ sa odloženom potpunom kontrolom za povrat sredstava u slučaju gubitka ključa



Pritisnite **Save Changes**. Zatim izaberite 3 ključa koja će činiti vaš wallet od uvezenih (npr. Seed Key, Coldcard MK4SP i Tapsigner Metro).



## Postavljanje posebnih ključnih rokova



Sledeći ekran vam omogućava da konfigurišete Ključ za hitne slučajeve i Ključ za nasledstvo. Ovde definišete kašnjenja koja upravljaju aktivacijom ovih specijalnih ključeva.



![Configuration des délais](assets/fr/07.webp)



Za **Hitni ključ**, odaberite hardverski ključ koji će služiti kao krajnja rezerva (ovde Coldcard MK4) i izaberite vreme aktivacije (u našem primeru: 2 godine). Za razliku od Naslednog ključa, Hitni ključ ne dodaje se kvorumu: omogućava vam da **zaobiđete multisig** potpuno, i daje vam potpunu kontrolu nad sredstvima nakon isteka vremenskog ograničenja. To je vaše rešenje poslednje instance: ako se nekoliko ključeva izgubi ili uništi, ovaj jedini ključ vam omogućava da povratite sve. Stoga mora biti zaštićen sa najvećom pažnjom.



Za **Inheritance Key**, izaberite ključ namenjen nasledniku (ovde Coldcard MK4SP) i odaberite odlaganje (u našem primeru: 1 godina). Nakon jedne godine bez aktivnosti, ovaj ključ **će biti dodat u kvorum potpisa**. U praktičnom smislu, vaš wallet 2-od-3 će postati wallet 2-od-4 kada ovaj period istekne, omogućavajući nasledniku da učestvuje u potpisivanju zajedno sa postojećim ključevima.



### Kako funkcionišu vremenske brave?



Bitcoin Keeper koristi **apsolutne vremenske zaključavanja** (CLTV - CheckLockTimeVerify), omogućene putem Miniscript-a. Za razliku od relativnih vremenskih zaključavanja (CSV), koja počinju kada je svaki UTXO primljen, apsolutna vremenska zaključavanja rade sa **fiksnim datumom isteka** definisanim kada je wallet kreiran.



U konkretnim terminima, ako danas kreirate wallet sa 1-godišnjim Ključem Nasleđa, datum aktivacije će biti "danas + 1 godina". Sva sredstva deponovana u ovom wallet, bez obzira na datum deponovanja, biće dostupna putem Ključa Nasleđa na ovaj isti datum.



Prednost apsolutnih vremenskih zaključavanja je što omogućavaju rokove duže od 15 meseci (što je granica relativnih CSV vremenskih zaključavanja), što objašnjava zašto Bitcoin Keeper može ponuditi opcije kao što su 2 godine.



### Mehanizam osvežavanja



Da biste sprečili aktivaciju specijalnih ključeva tokom vašeg života, morate periodično "osvežavati" vaš wallet. Sa apsolutnim vremenskim zaključavanjima, ovo podrazumeva **ponovno kreiranje wallet sa novim datumom isteka** pomerenim u budućnost, a zatim prebacivanje vaših sredstava na ovaj novi wallet.



Bitcoin Keeper pojednostavljuje ovaj proces sa integrisanom funkcijom osvežavanja. Aplikacija automatski upravlja složenošću u pozadini: vi jednostavno pratite vođene korake, bez potrebe da ručno kreirate novi wallet ili sami prebacujete sredstva. Planirajte ovu operaciju redovno, mnogo pre isteka najkraćeg konfigurisanog vremenskog okvira. Na primer, sa 1-godišnjim Naslednim Ključem, osvežavajte svakih 9-10 meseci kako biste održali sigurnosnu marginu.



## Sačuvaj i izvezi konfiguraciju



Jednom kada je wallet kreiran, aplikacija vas podseća da sačuvate konfiguracionu datoteku. **Ovaj korak je kritičan**: bez ove datoteke, vaši naslednici neće moći da rekonstituišu wallet multisig.



![Export de la configuration](assets/fr/08.webp)



Pritisnite **Backup Wallet Recovery File**. Dostupno je nekoliko opcija izvoza:




- PDF izvoz**: generiše kompletan dokument sa svim wallet informacijama
- Prikaži QR**: prikazuje QR kod za uvoz konfiguracije na drugom uređaju
- Airdrop / Izvoz datoteke**: izvozi datoteku putem opcija za deljenje
- NFC**: podeli putem NFC-a sa kompatibilnim uređajem



Umnožite kopije: jedna kod vašeg notara, jedna u bankovnom sefu, jedna šifrovana digitalna verzija. Vaš novi wallet sada se pojavljuje u kartici Novčanici sa oznakama "Više ključeva", "2 od 3", "Nasledni ključ" i "Hitni ključ".



## Kreiraj Wallet Kanarinca



Kanarinac Wallet je sistem ranog upozorenja. Ideja: svaki ključ korišćen u wallet multi-ključu može se koristiti i u zasebnom wallet single-ključu. Polaganjem male sume na ovaj wallet "kanarinac", svako neovlašćeno pomeranje signalizira kompromitovanje ključa.



![Canary Wallets](assets/fr/09.webp)



Postoje dva načina za konfigurisanje Wallet Canary. Iz kartice **More**, pritisnite **Canary Wallets** u odeljku "Keys and Wallets". Ekran objašnjava princip: ako neko pristupi jednom od vaših ključeva i pronađe sredstva u povezanom wallet jednoključu, pokušaće da ih ukloni, što će vas upozoriti.



![Configuration Canary depuis une clé](assets/fr/10.webp)



Možete takođe konfigurisati Canary direktno sa ključa. U kartici **Keys**, izaberite ključ (npr. Tapsigner Genesis), pritisnite ikonu **Settings** (zupčanik), zatim **Canary Wallet**. Povezani wallet canary se otvara, spreman da primi neke nadzorne satoshije.



Depozitujte malu sumu (nekoliko hiljada satoshija) na svaki Canary Wallet. Ako se ova sredstva pomere bez vašeg pristanka, odmah uklonite kompromitovani ključ iz vaših multisig sefova.



## Najbolje prakse



**Testirajte svoju konfiguraciju** sa malom količinom novca pre nego što uložite veći iznos. Pošaljite nekoliko hiljada satoshija u trezor, zatim pokušajte sa odlaznim troškom da proverite da li ste savladali proces potpisivanja sa svakim uređajem. Takođe testirajte uvoz konfiguracione datoteke na drugom telefonu kako biste bili sigurni da bekap funkcioniše.



**Distribuirajte ključeve inteligentno**. Za Tapsigners, predajte ih u zapečaćenoj koverti sa PIN-om koji se komunicira odvojeno (npr. u pismu sa Uputstvima za oporavak koje se čuva na drugom mestu). Za klasične hardverske novčanike, držite uređaj kod pouzdane treće strane, a seed na papiru ili metalu kod vas ili druge treće strane. Zabeležite otisak prsta svakog ključa i njegovo ime u konfiguracionom fajlu kako biste izbegli zabunu.



**Planirajte periodične testove** (vežbe evakuacije). Godišnje proverite da li možete obnoviti sef iz rezervnih kopija na praznom telefonu. Testirajte Canary alarme proverom stanja. Simulirajte scenarije gubitka ("šta ako izgubim Coldcard?") da potvrdite da preostale kombinacije ključeva budu dovoljne.



**Ne zaboravite na osvežavanje**. Ako ste postavili svoj Ključ nasleđivanja na 1 godinu, osvežavajte se svakih 9-10 meseci. Ovo je cena koju plaćate za automatski prenos bez intervencije treće strane.



**Ažurirajte plan**. Svaka promena (zamena ključa, modifikacija naslednika, promena roka) mora biti odražena u svim rezervnim kopijama i dokumentima. Regenerišite PDF-ove nakon svake izmene i redistribuirajte nove verzije.



## Ograničenja i razmatranja



Uprkos moći ovih alata, važno je prepoznati njihova ograničenja kako bismo ih što efikasnije upravljali.



**Kompleksnost** multisig sefa sa vremenskim zaključavanjima može biti rizik sama po sebi: pogrešna konfiguracija, nerazumevanje od strane naslednika, gubitak kritičnog elementa među mnogim komponentama. Bitcoin Keeper pojednostavljuje iskustvo koliko god je to moguće, ali i dalje ostaje tehnička operacija. Primeni ovaj plan samo ako iznos koji treba zaštititi to opravdava. Za male iznose, jednostavniji plan može biti dovoljan.



**Zavisnost aplikacije** vredi razmotriti. Iako je kod otvorenog koda i zasnovan na otvorenim standardima (Miniscript, BSMS), određene funkcionalnosti se oslanjaju na Keeper ekosistem. Sačuvajte kopiju aplikacije (Android APK ili iOS IPA) i dokumentujte u svojim pismima naslednicima mogućnost korišćenja drugih novčanika kompatibilnih sa Miniscript-om (kao što je Liana) za povraćaj sredstava.



Pouzdani brokeri** uvode ljudski rizik. Šta se dešava ako zlonamerni rođak iskoristi ključ poveren njemu/njoj pre roka? Ili ako advokat izgubi vaša dokumenta? Pažljivo birajte ove osobe, jasno im objasnite njihove odgovornosti i imajte plan B. Canary novčanici, redundantne kopije i sama struktura multisig ostaju vaša najbolja zaštita protiv ovih opasnosti.



## Zaključak



Bitcoin Keeper, sa svojim Diamond Hands planom, nudi kompletan alat za planiranje imovine: Poboljšani Trezori sa vremenskim ključevima, prateća dokumenta, Canary Novčanici i personalizovanu podršku.



To je više od tehničkog problema: to je pitanje dizajniranja arhitekture vašeg poseda, inteligentne distribucije ključeva i znanja, i redovnog testiranja sistema. Dobro osmišljen Bitcoin plan nasleđa pretvara vaše satoshije u stvarno, prenosivo nasleđe.