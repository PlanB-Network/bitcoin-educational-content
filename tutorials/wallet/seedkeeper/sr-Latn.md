---
name: Seedkeeper
description: Kako da napravim rezervnu kopiju svog wallet Bitcoin pomoću Seedkeeper pametne kartice?
---

![cover](assets/cover.webp)



Seedkeeper je pametna kartica koju je razvila Satochip, belgijska kompanija specijalizovana za hardverska rešenja za upravljanje i zaštitu digitalnih tajni. Poznata po svom asortimanu pametnih kartica za Bitcoin ekosistem, Satochip je dizajnirao Seedkeeper kao alternativu tradicionalnim metodama čuvanja mnemoničkih fraza.



U konkretnim terminima, Seedkeeper ima oblik multifunkcionalne, EAL6-certifikovane pametne kartice sa sigurnim procesorom i memorijom otpornom na neovlašćene izmene (tzv. "Secure Element"). Kao što ime sugeriše, njegova uloga je da čuva Bitcoin wallet mnemoničke fraze i lozinke na enkriptovan i zaštićen način. Sa Seedkeeper-om, možete generate, uvoziti, organizovati i sačuvati vaše tajne direktno u sigurnoj komponenti kartice.



Po mom mišljenju, Seedkeeper ima dve glavne namene, koje ćemo istražiti u 2 odvojena tutorijala:




- Bitcoin** skladištenje mnemoničke fraze: umesto da zapisujete svojih 12 ili 24 reči na papir, možete ih uneti u pametnu karticu i zaštititi PIN kodom.
- Upravljanje lozinkama**: možete generisati generate jake lozinke putem aplikacije Seedkeeper i sačuvati ih direktno na pametnoj kartici, što vam omogućava praktičan, jednostavan za korišćenje offline menadžer lozinki.



Tehnički gledano, Seedkeeper ima kapacitet od 8192 bajta, što mu omogućava da čuva najmanje 50 odvojenih tajni (tačan broj će zavisiti od njihove veličine i metapodataka povezanih sa svakom od njih). Seedkeeper se može koristiti ili [preko čitača pametnih kartica povezanog](https://satochip.io/accessories/) sa računarom, ili putem mobilne aplikacije sa NFC vezom. Ceo sistem radi u offline režimu, bez internet konekcije, garantujući ograničenu površinu za napad.



![Image](assets/fr/001.webp)



Posebno zanimljiva funkcija je mogućnost dupliranja sadržaja jednog Seedkeeper-a na drugi kako biste napravili rezervnu kopiju. U ovom vodiču ćemo vam pokazati kako to da uradite.



Seedkeeper je takođe veoma interesantan kada se kombinuje sa wallet stateless hardverom kao što su SeedSigner ili Specter DIY. U ovom slučaju, nema potrebe za korišćenjem Satochip klijenta na računaru ili mobilnom telefonu. Seedkeeper čuva seed u svom secure element i može se koristiti direktno sa uređajem za potpisivanje, eliminišući potrebu za papirnim QR kodom. Neću razvijati ovaj konkretan slučaj upotrebe u ovom vodiču, jer je to tema drugog posvećenog vodiča :



https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

## 1. Koja je upotreba Seedkeeper-a?



U ovom vodiču baviću se samo slučajevima upotrebe vezanim za Bitcoin, jer se ovaj vodič odnosi na to. Nećemo ulaziti u funkcionalnost upravljanja lozinkama, koja će biti tema drugog vodiča.



U poređenju sa jednostavnim papirnim bekapom mnemoničke fraze, korišćenje Seedkeeper-a ima nekoliko prednosti:





- Otpornо na krađu:** seed u vašem wallet nije dostupan u čistom tekstu. Da biste ga izdvojili, morate znati Seedkeeper PIN. Lopov koji dođe do uređaja neće moći ništa da uradi s njim bez ovog koda.





- Širenje rizika na dva faktora:** možete podeliti sigurnost između digitalnog i fizičkog faktora. Na primer, ako čuvate Seedkeeper PIN u svom menadžeru lozinki, biće vam potreban i pristup ovom menadžeru i fizičko posedovanje pametne kartice da biste dobili seed (značajno smanjena verovatnoća napada).





- Centralizovano upravljanje:** Seedkeeper olakšava upravljanje višestrukim semenkama iz različitih portfolija.





- Jednostavne sigurnosne kopije:** jednostavno duplicirajte šifrovane sigurnosne kopije na druge SeedKeepers.



Međutim, postoji niz nedostataka u poređenju sa jednostavnom papirnom rezervnom kopijom vašeg seed:





- Cena:** iako skromna (oko €25), i dalje je viša od cene lista papira.





- Zavisnost od uređaja za opštu namenu:** unos i upravljanje seed zahteva računar ili pametni telefon, što znači da vaša mnemotehnička šifra prolazi kroz mašinu sa mnogo širim površinama za napad nego wallet hardver. Ovo može predstavljati rizik ako je mašina kompromitovana. Zato ne preporučujem korišćenje Seedkeeper-a za čuvanje seed od wallet hardvera (osim u stateless upotrebi bez računara, kao kod SeedSigner-a). Uloga wallet hardvera je upravo da čuva seed u minimalističkom, visoko sigurnom okruženju. Ručnim unosom vašeg seed na vaš uobičajeni računar, on više nije ograničen na wallet hardver: takođe završava na mašini za opštu namenu, izloženoj višestrukim vektorima napada. Stoga je bolje koristiti Seedkeeper za vrući wallet nego za hladni (osim SeedSigner / stateless wallet hardvera).





- Rizik od gubitka povezan sa PIN-om:** direktna nepristupačnost seed, za razliku od papirne kopije, zaista pruža zaštitu od fizičke krađe. Ali kao i uvek, bezbednost je balansiranje između rizika od krađe i rizika od gubitka. Ako vaša kopija zahteva PIN, gubitak ovog koda će onemogućiti oporavak vaše mnemoničke fraze, a samim tim i pristup vašim bitkoinima.



S obzirom na ove prednosti i nedostatke, smatram da su najbolja upotreba za Seedkeeper (osim njegove funkcije upravljanja lozinkama), s jedne strane, čuvanje semena iz vaših **softverskih portfolija**, budući da se već nalaze na vašem telefonu ili računaru, ili iz vašeg hardvera bez ekrana wallet kao što je Satochip, a s druge strane, korišćenje u kombinaciji sa stateless wallet hardverom kao što je SeedSigner, gde zaista dolazi do izražaja.



Još jedan posebno zanimljiv slučaj upotrebe za Seedkeeper je mogućnost sigurnog i pouzdanog bekapovanja *Deskriptora* vaših portfolija.



## 2. Kako da dobijem Seedkeeper?



Postoje dva glavna načina da nabavite svoj Seedkeeper. Možete ga [kupiti direktno iz Satochip-ove zvanične prodavnice](https://satochip.io/product/seedkeeper/) ili od ovlašćenog prodavca. Ali pošto je [Seedkeeper applet otvorenog koda](https://github.com/Toporin/Seedkeeper-Applet), takođe imate opciju da ga sami instalirate na [praznu pametnu karticu](https://satochip.io/product/blank-javacard-for-diy-project/).



Ako želite koristiti funkcionalnost Seedkeeper-ove sigurnosne kopije, očigledno ćete morati kupiti dve pametne kartice.



## 3. Instaliranje Seedkeeper klijenta



U ovom vodiču, napravićemo rezervnu kopiju našeg seed portfolija na našem Seedkeeper-u. Prvi korak je instalacija softvera na vašem računaru ili pametnom telefonu. Na računaru, potrebno je [preuzeti najnoviju verziju Satochip-Utils](https://github.com/Toporin/Satochip-Utils/releases). Na mobilnom uređaju, aplikacija Seedkeeper je dostupna na [Google Play Store](https://play.google.com/store/apps/details?id=org.satochip.seedkeeper) kao i na [Apple App Store](https://apps.apple.com/be/app/seedkeeper/id6502836060).



![Image](assets/fr/002.webp)



## 4. Inicijalizacija čuvara semena



Pokrenite aplikaciju i kliknite na dugme "*Click & Scan*".



![Image](assets/fr/003.webp)



Od vas će biti zatražen PIN kod za vaš Seedkeeper. Pošto je ovo nova kartica, PIN još nije definisan. Unesite bilo koji kod da preskočite ovaj korak, zatim kliknite na "*Dalje*".



![Image](assets/fr/004.webp)



Zatim postavite karticu na poleđinu svog pametnog telefona. Aplikacija će detektovati da Seedkeeper još nije inicijalizovan i zatražiće od vas da postavite PIN kod vaše pametne kartice, između 4 i 16 karaktera. Za optimalnu sigurnost, izaberite jak lozinku koja je što duža, nasumična i sastavljena od širokog spektra karaktera. Ovaj PIN kod je jedina barijera protiv fizičkog pristupa vašoj frazi za oporavak.



**Zapamti da sada sačuvaš ovaj PIN**, na primer u menadžeru lozinki ili na posebnom fizičkom medijumu. U ovom drugom slučaju, nikada ne drži medijum koji sadrži PIN na istom mestu kao i tvoj Seedkeeper, inače će ova sigurnost postati beskorisna. Važno je imati pouzdanu rezervnu kopiju: bez PIN-a, nećeš moći da povratiš tajne sačuvane na tvom Seedkeeper-u.



![Image](assets/fr/005.webp)



Potvrdite svoj PIN kod po drugi put.



![Image](assets/fr/006.webp)



Vaš Seedkeeper je sada inicijalizovan. Možete ga otključati unosom PIN koda koji ste upravo postavili.



![Image](assets/fr/007.webp)



Sada ćete biti preusmereni na stranicu za upravljanje pametnom karticom.



![Image](assets/fr/008.webp)



## 5. Registrujte seed na Seedkeeper



Jednom kada vaš Seedkeeper bude otključan, kliknite na dugme "*+*".



![Image](assets/fr/009.webp)



Odaberite "Uvezi tajnu*". Opcija "*Generiši tajnu*" vam omogućava da kreirate novu mnemonicku frazu direktno unutar aplikacije.



![Image](assets/fr/010.webp)



U našem slučaju, želimo sačuvati seed u našem portfoliju. Kliknite na "*Mnemonic*".



![Image](assets/fr/011.webp)



Dodeli "*Oznaku*" ovoj tajni kako bi se lako identifikovala ako skladištiš više informacija u svom Seedkeeper-u.



![Image](assets/fr/012.webp)



Zatim unesite svoju frazu za oporavak u predviđeno polje. Ako želite, možete dodati i passphrase BIP39 ili svoje *Deskriptore*. Zatim kliknite na "Uvezi*".



![Image](assets/fr/013.webp)



*Mnemonik prikazan na ovoj slici je fiktivan i ne pripada nikome. To je samo primer. Nikada ne otkrivajte svoj sopstveni mnemonik nikome, ili će vaši bitkoini biti ukradeni



Postavite svoj Seedkeeper na poleđinu vašeg pametnog telefona.



![Image](assets/fr/014.webp)



Vaš seed je registrovan.



![Image](assets/fr/015.webp)



## 6. Pristupite svom seed na Seedkeeper



Ako želite da proverite svoju mnemoničku frazu, uzmite svoj Seedkeeper i kliknite na dugme "*Click & Scan*".



![Image](assets/fr/016.webp)



Unesite svoj PIN kod, zatim pritisnite "*Next*".



![Image](assets/fr/017.webp)



Postavite svoj Seedkeeper na poleđinu vašeg pametnog telefona.



![Image](assets/fr/018.webp)



Ovo vas vodi do liste svih vaših registrovanih tajni. U ovom primeru, želim da prikažem seed iz mog portfolija "*Blockstream App*", pa kliknem na njega.



![Image](assets/fr/019.webp)



Pritisnite dugme "*Reveal*".



![Image](assets/fr/020.webp)



Ponovo skeniraj svoj Seedkeeper.



![Image](assets/fr/021.webp)



Vaša prethodno zabeležena mnemonička fraza sada je prikazana na ekranu.



![Image](assets/fr/022.webp)



## 7. Pravljenje rezervne kopije Seedkeeper-a



Sada ćemo napraviti rezervnu kopiju mog Seedkeeper-a na drugom Seedkeeper-u kako bismo imali dve kopije. Ova redundancija može biti deo strategije za osiguranje vaših bitkoina: na primer, čuvanje vaše fraze na dve odvojene lokacije kako biste ograničili fizičke rizike, ili poveravanje kopije pouzdanom rođaku kao deo plana nasledstva.



Da biste to uradili, ponesite svoj drugi Seedkeeper (zapamtite da jedan od njih obeležite kako biste izbegli bilo kakvu zabunu). Počnite inicijalizacijom, kako je opisano u koraku 4 ovog vodiča. Ponovo izaberite jaku lozinku. U zavisnosti od vaše strategije, možete se odlučiti za drugačiju lozinku ili zadržati istu.



![Image](assets/fr/023.webp)



Otvorite aplikaciju, kliknite na "*Click & Scan*", unesite lozinku vašeg Seedkeeper-a br. 1 (izvor), zatim ga skenirajte.



![Image](assets/fr/024.webp)



Ovo vas vodi na početnu stranicu, sa spiskom vaših tajni. Kliknite na tri male tačke u gornjem desnom uglu interfejsa.



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



To je sve što treba da uradite! Sada znate kako da koristite Seedkeeper za čuvanje mnemoničke fraze Bitcoin wallet. U budućem vodiču, pogledaćemo kako da koristite Seedkeeper za čuvanje vaših lozinki. Takođe vas pozivam da otkrijete njegovu kombinovanu upotrebu sa SeedSigner :



https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

https://planb.academy/tutorials/computer-security/authentication/seedkeeper-password-64ffaf68-53aa-43c3-bc7a-c1dc2a17fee3

U ovom vodiču, nekoliko puta smo spomenuli ***Deskriptore*** u vašem Bitcoin portfoliju. Ne znate šta su oni? U tom slučaju, preporučujem da pohađate naš besplatni CYP 201 kurs obuke, koji detaljno objašnjava sve mehanizme uključene u upravljanje HD portfolijima!



https://planb.academy/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f