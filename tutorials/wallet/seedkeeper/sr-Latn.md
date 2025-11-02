---
name: Seedkeeper
description: Kako da napravim rezervnu kopiju svog Wallet Bitcoin pomoću Seedkeeper pametne kartice?
---

![cover](assets/cover.webp)



Seedkeeper je pametna kartica koju je razvila Satochip, belgijska kompanija specijalizovana za hardverska rešenja za upravljanje i zaštitu digitalnih tajni. Poznata po svom asortimanu pametnih kartica za Bitcoin ekosistem, Satochip je dizajnirao Seedkeeper kao alternativu tradicionalnim metodama čuvanja Mnemonic fraza.



U konkretnom smislu, Seedkeeper ima oblik multifunkcionalne, EAL6-certifikovane pametne kartice sa sigurnim procesorom i memorijom otpornom na neovlašćene izmene (tj. "secure element*"). Kao što ime sugeriše, njegova uloga je da čuva Bitcoin Mnemonic fraze i lozinke na enkriptovan i zaštićen način. Sa Seedkeeper-om, možete generate, uvoziti, organizovati i sačuvati vaše tajne direktno u sigurnom komponentu kartice.



Po mom mišljenju, Seedkeeper ima dve glavne namene, koje ćemo istražiti u 2 odvojena tutorijala:




- Bitcoin** Mnemonic fraza skladištenje: umesto da zapisujete svojih 12 ili 24 reči na papir, možete ih uneti u pametnu karticu i zaštititi PIN kodom.
- Upravljanje lozinkama**: možete generisati generate jake lozinke putem aplikacije Seedkeeper i sačuvati ih direktno na pametnoj kartici, što vam omogućava praktičan, jednostavan za korišćenje offline menadžer lozinki.



Tehnički gledano, Seedkeeper ima kapacitet od 8192 bajta, što mu omogućava da čuva najmanje 50 odvojenih tajni (tačan broj će zavisiti od njihove veličine i metapodataka povezanih sa svakom od njih). Seedkeeper se može koristiti ili [preko čitača pametnih kartica povezanog](https://satochip.io/accessories/) sa računarom, ili putem mobilne aplikacije sa NFC vezom. Ceo sistem radi u offline režimu, bez internet konekcije, garantujući ograničenu površinu za napad.



![Image](assets/fr/001.webp)



Posebno zanimljiva funkcija je mogućnost dupliciranja sadržaja jednog Seedkeeper-a na drugi kako biste napravili rezervnu kopiju. U ovom vodiču, pokazaćemo vam kako to da uradite.



Seedkeeper je takođe veoma interesantan kada se kombinuje sa stateless Hardware Wallet kao što su SeedSigner ili Specter DIY. U ovom slučaju, nema potrebe za korišćenjem Satochip-ovog računara ili mobilnog klijenta. Seedkeeper čuva seed u svom secure element i može se koristiti direktno sa uređajem za potpisivanje, eliminišući potrebu za papirnim QR kodom. Neću razvijati ovaj konkretan slučaj upotrebe u ovom vodiču, jer je to tema drugog posvećenog vodiča :



https://planb.network/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

## 1. Koja je upotreba Seedkeeper-a?



U ovom uputstvu, baviću se samo slučajevima upotrebe vezanim za Bitcoin, jer se ovo uputstvo odnosi na to. Nećemo ulaziti u funkcionalnost upravljanja lozinkama, što će biti tema drugog uputstva.



U poređenju sa jednostavnom papirnom rezervnom kopijom fraze Mnemonic, korišćenje Seedkeeper-a ima nekoliko prednosti:





- Otpornan na krađu:** seed u vašem Wallet nije dostupan u čistom tekstu. Da biste ga izdvojili, morate znati Seedkeeper PIN. Lopov koji dođe do uređaja neće moći ništa da uradi s njim bez ovog koda.





- Širenje rizika na dva faktora:** možete podeliti sigurnost između digitalnog i fizičkog faktora. Na primer, ako čuvate Seedkeeper PIN u svom menadžeru lozinki, biće vam potreban i pristup ovom menadžeru i fizičko posedovanje pametne kartice da biste dobili seed (značajno smanjena verovatnoća napada).





- Centralizovano upravljanje:** Seedkeeper olakšava upravljanje višestrukim semenkama iz različitih portfolija.





- Jednostavne sigurnosne kopije:** jednostavno duplicirajte šifrovane sigurnosne kopije na druge SeedKeepers.



Međutim, postoji niz nedostataka u poređenju sa jednostavnim papirnim rezervnim primerkom vašeg seed:





- Cena:** iako skromna (oko €25), i dalje je viša od cene lista papira.





- Zavisnost od uređaja za opštu namenu:** Unos i upravljanje seed zahteva računar ili pametni telefon, što znači da vaš Mnemonic prolazi kroz mašinu sa mnogo širom površinom napada nego Hardware Wallet. Ovo može predstavljati rizik ako je radna stanica kompromitovana. Zato ne preporučujem korišćenje Seedkeeper-a za čuvanje seed od Hardware Wallet (osim za stateless upotrebu bez računara, kao sa SeedSigner-om). Uloga Hardware Wallet je upravo da čuva seed u minimalističkom, visoko sigurnom okruženju. Ručnim unosom vašeg seed na vaš uobičajeni računar, on više nije ograničen na Hardware Wallet: takođe završava na mašini za opštu namenu, izloženoj višestrukim vektorima napada. Dakle, bolje je koristiti Seedkeeper za Hot Wallet nego za Cold (osim SeedSigner / stateless Hardware Wallet).





- Rizik od gubitka povezan sa PIN-om:** direktna nepristupačnost seed, za razliku od papirne kopije, zaista pruža zaštitu protiv fizičke krađe. Ali kao i uvek, bezbednost je balansiranje između rizika od krađe i rizika od gubitka. Ako vaša kopija zahteva PIN, gubitak ovog koda će onemogućiti oporavak vaše Mnemonic fraze, a samim tim i pristup vašim bitkoinima.



Uzimajući u obzir ove prednosti i nedostatke, smatram da su najbolja upotreba za Seedkeeper (osim njegove funkcije upravljanja lozinkama), s jedne strane, čuvanje semena iz vaših **softverskih portfolija**, budući da se već nalaze na vašem telefonu ili računaru, ili iz vaših hardverskih novčanika bez ekrana kao što je Satochip, a s druge strane, korišćenje u kombinaciji sa stateless Hardware Wallet kao što je SeedSigner, gde zaista dolazi do izražaja.



Još jedan posebno zanimljiv slučaj upotrebe za Seedkeeper je mogućnost sigurnog i pouzdanog bekapovanja *Deskriptora* vaših portfolija.



## 2. Kako da dobijem Seedkeeper?



Postoje dva glavna načina da nabavite svoj Seedkeeper. Možete ga [kupiti direktno iz Satochip-ove zvanične prodavnice](https://satochip.io/product/seedkeeper/) ili od ovlašćenog prodavca. Ali pošto je [Seedkeeper applet otvorenog koda](https://github.com/Toporin/Seedkeeper-Applet), imate i opciju da ga sami instalirate na [praznu pametnu karticu](https://satochip.io/product/blank-javacard-for-diy-project/).



Ako želite da koristite funkcionalnost bekapa Seedkeeper-a, očigledno ćete morati da kupite dve pametne kartice.



## 3. Instaliranje Seedkeeper klijenta



U ovom vodiču, napravićemo rezervnu kopiju našeg seed portfolija na našem Seedkeeper-u. Prvi korak je instalacija softvera na vašem računaru ili pametnom telefonu. Na računaru, potrebno je [preuzeti najnoviju verziju Satochip-Utils](https://github.com/Toporin/Satochip-Utils/releases). Na mobilnom uređaju, aplikacija Seedkeeper je dostupna na [Google Play Store-u](https://play.google.com/store/apps/details?id=org.satochip.seedkeeper) kao i na [Apple App Store-u](https://apps.apple.com/be/app/seedkeeper/id6502836060).



![Image](assets/fr/002.webp)



## 4. Inicijalizacija Seedkeeper-a



Pokrenite aplikaciju i kliknite na dugme "*Click & Scan*".



![Image](assets/fr/003.webp)



Od vas će biti zatražen PIN kod za vaš Seedkeeper. Pošto je ovo nova kartica, PIN još nije definisan. Unesite bilo koji kod da preskočite ovaj korak, zatim kliknite na "*Next*".



![Image](assets/fr/004.webp)



Zatim postavite karticu na poleđinu svog pametnog telefona. Aplikacija će detektovati da Seedkeeper još nije inicijalizovan i zatražiće od vas da postavite PIN kod vaše pametne kartice, između 4 i 16 karaktera. Za optimalnu sigurnost, izaberite jak lozinku koja je što duža, nasumična i sastavljena od širokog spektra karaktera. Ovaj PIN kod je jedina barijera protiv fizičkog pristupa vašoj frazi za oporavak.



**Zapamtite da sada sačuvate ovaj PIN**, na primer u menadžeru lozinki ili na posebnom fizičkom medijumu. U ovom drugom slučaju, nikada ne držite medijum koji sadrži PIN na istom mestu kao vaš Seedkeeper, inače će ova sigurnost postati beskorisna. Važno je imati pouzdanu rezervnu kopiju: bez PIN-a, nećete moći da povratite tajne sačuvane na vašem Seedkeeper-u.



![Image](assets/fr/005.webp)



Potvrdite svoj PIN kod po drugi put.



![Image](assets/fr/006.webp)



Vaš Seedkeeper je sada inicijalizovan. Možete ga otključati unosom PIN koda koji ste upravo postavili.



![Image](assets/fr/007.webp)



Bićete preusmereni na stranicu za upravljanje pametnom karticom.



![Image](assets/fr/008.webp)



## 5. Registrujte seed na Seedkeeper



Kada je vaš Seedkeeper otključan, kliknite na dugme "*+*".



![Image](assets/fr/009.webp)



Odaberite "Importuj tajnu*". Opcija "*generate tajna*" vam omogućava da kreirate novu Mnemonic frazu direktno unutar aplikacije.



![Image](assets/fr/010.webp)



U našem slučaju, želimo sačuvati seed u našem portfoliju. Kliknite na "*Mnemonic*".



![Image](assets/fr/011.webp)



Dodeli "*Oznaku*" ovoj tajni kako bi se lako identifikovala ako skladištiš više informacija u svom Seedkeeper-u.



![Image](assets/fr/012.webp)



Zatim unesite svoju frazu za oporavak u predviđeno polje. Ako želite, možete dodati i passphrase BIP39 ili svoje *Deskriptore*. Zatim kliknite na "Uvezi*".



![Image](assets/fr/013.webp)



*Mnemonic prikazan na ovoj slici je izmišljen i ne pripada nikome. To je samo primer. Nikada ne otkrivajte svoj sopstveni Mnemonic nikome, ili će vaši bitkoini biti ukradeni



Postavite svoj Seedkeeper na poleđinu svog pametnog telefona.



![Image](assets/fr/014.webp)



Vaš seed je registrovan.



![Image](assets/fr/015.webp)



## 6. Pristupite vašem seed na Seedkeeper



Ako želite da proverite svoju Mnemonic frazu, uzmite svoj Seedkeeper i kliknite na dugme "*Click & Scan*".



![Image](assets/fr/016.webp)



Unesite svoj PIN kod, zatim pritisnite "*Next*".



![Image](assets/fr/017.webp)



Postavite svoj Seedkeeper na poleđinu vašeg pametnog telefona.



![Image](assets/fr/018.webp)



Ovo vas vodi do liste svih vaših registrovanih tajni. U ovom primeru, želim da prikažem seed u svom portfoliju "*BLOCKSTREAM App*", pa kliknem na njega.



![Image](assets/fr/019.webp)



Pritisnite dugme "*Reveal*".



![Image](assets/fr/020.webp)



Ponovo skeniraj svoj Seedkeeper.



![Image](assets/fr/021.webp)



Vaša prethodno snimljena Mnemonic fraza je sada prikazana na ekranu.



![Image](assets/fr/022.webp)



## 7. Pravljenje rezervne kopije Seedkeeper-a



Sada ćemo napraviti rezervnu kopiju mog Seedkeeper-a na drugom Seedkeeper-u kako bismo imali dve kopije. Ova redundancija može biti deo strategije za osiguranje vaših bitkoina: na primer, čuvanje vaše fraze na dve odvojene lokacije kako biste ograničili fizičke rizike, ili poveravanje kopije pouzdanom rođaku kao deo plana nasledstva.



Da biste to uradili, ponesite svoj drugi Seedkeeper (ne zaboravite da jedan od njih označite kako biste izbegli bilo kakvu zabunu). Počnite inicijalizacijom, kao što je opisano u koraku 4 ovog vodiča. Ponovo izaberite jaku lozinku. U zavisnosti od vaše strategije, možete se odlučiti za drugačiju lozinku ili zadržati istu.



![Image](assets/fr/023.webp)



Otvorite aplikaciju, kliknite na "*Click & Scan*", unesite lozinku vašeg Seedkeeper-a br. 1 (izvor), zatim ga skenirajte.



![Image](assets/fr/024.webp)



Ovo vas vodi na početnu stranicu sa spiskom vaših tajni. Kliknite na tri male tačke u gornjem desnom uglu Interface.



![Image](assets/fr/025.webp)



Odaberite "*Napravite rezervnu kopiju*", zatim pritisnite "*Pokreni*".



![Image](assets/fr/026.webp)



Unesite PIN kod vaše rezervne kartice (Seedkeeper br. 2).



![Image](assets/fr/027.webp)



Zatim skenirajte karticu.



![Image](assets/fr/028.webp)



Uradite isto sa glavnom karticom (Seedkeeper br. 1), zatim kliknite na "*Napravite rezervnu kopiju*".



![Image](assets/fr/029.webp)



Vaš Seedkeeper br. 2 sada sadrži sve tajne pohranjene na Seedkeeper br. 1.



![Image](assets/fr/030.webp)



Možete skenirati svoj Seedkeeper br. 2 da proverite da li su tajne kopirane.



![Image](assets/fr/031.webp)



To je sve što treba da uradite! Sada znate kako da koristite Seedkeeper za čuvanje Mnemonic fraze Bitcoin Wallet. U budućem vodiču, pogledaćemo kako da koristite Seedkeeper za čuvanje vaših lozinki. Takođe vas pozivam da otkrijete njegovu kombinovanu upotrebu sa SeedSigner :



https://planb.network/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

https://planb.network/tutorials/computer-security/authentication/seedkeeper-password-64ffaf68-53aa-43c3-bc7a-c1dc2a17fee3

U ovom vodiču, nekoliko puta smo spomenuli ***Deskriptore*** u vašem Bitcoin portfoliju. Ne znate šta su oni? U tom slučaju, preporučujem da pohađate naš besplatni CYP 201 kurs obuke, koji detaljno objašnjava sve mehanizme uključene u upravljanje HD portfolijima!



https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f