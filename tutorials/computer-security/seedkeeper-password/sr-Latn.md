---
name: Seedkeeper - Menadžer lozinki
description: Kako sačuvati svoje lozinke pomoću Seedkeeper pametne kartice?
---

![cover](assets/cover.webp)



Seedkeeper je pametna kartica koju je razvila Satochip, belgijska kompanija specijalizovana za hardverska rešenja za upravljanje i zaštitu digitalnih tajni. Poznata po svom asortimanu pametnih kartica za Bitcoin ekosistem, Satochip je osmislio Seedkeeper kao alternativu tradicionalnim metodama čuvanja mnemoničkih fraza i drugih digitalnih tajni.



U konkretnom smislu, Seedkeeper ima oblik multifunkcionalne, EAL6-certifikovane pametne kartice sa sigurnim procesorom i memorijom otpornom na neovlašćene izmene (tzv. "Secure Element"). Kao što ime sugeriše, njegova uloga je da čuva mnemonike i lozinke Bitcoin portfolija na enkriptovan i zaštićen način. Sa Seedkeeper-om, možete generate, uvoziti, organizovati i sačuvati vaše tajne direktno u sigurnoj komponenti kartice.



Po mom mišljenju, Seedkeeper ima dve glavne namene, koje ćemo istražiti u 2 odvojena tutorijala:




- Bitcoin** skladištenje mnemoničke fraze: umesto da zapisujete svojih 12 ili 24 reči na papir, možete ih uneti u pametnu karticu i zaštititi PIN kodom.
- Upravljanje lozinkama**: možete generisati generate jake lozinke putem aplikacije Seedkeeper i sačuvati ih direktno na pametnoj kartici, što vam omogućava praktičan, jednostavan za korišćenje offline menadžer lozinki.



Tehnički gledano, Seedkeeper ima kapacitet od 8192 bajta, što mu omogućava da pohrani najmanje 50 odvojenih tajni (tačan broj će zavisiti od njihove veličine i metapodataka povezanih sa svakom od njih). Seedkeeper se može pristupiti ili [preko čitača pametnih kartica povezanog](https://satochip.io/accessories/) sa računarom, ili putem mobilne aplikacije sa NFC vezom. Ceo sistem radi u offline režimu, bez internet konekcije, garantujući ograničenu površinu napada.



![Image](assets/fr/001.webp)



Posebno zanimljiva funkcija je mogućnost dupliciranja sadržaja jednog Seedkeeper-a na drugi kako biste napravili rezervnu kopiju. U ovom vodiču ćemo vam pokazati kako to da uradite.



U ovom vodiču pokrićemo samo korišćenje SeedKeeper-a za tradicionalne lozinke, na način menadžera lozinki. Ako želite da koristite SeedKeeper za čuvanje Bitcoin wallet mnemoničkih fraza, molimo vas da pogledate ovaj drugi vodič:



https://planb.academy/tutorials/wallet/backup/seedkeeper-906dfff8-1826-4837-92d1-8669e216d356

## 1. Kako da nabavim Seedkeeper?



Postoje dva glavna načina da nabavite svoj Seedkeeper. Možete ga [kupiti direktno iz Satochip-ove zvanične prodavnice](https://satochip.io/product/seedkeeper/) ili od ovlašćenog prodavca. Ali pošto je [Seedkeeper applet otvorenog koda](https://github.com/Toporin/Seedkeeper-Applet), takođe imate opciju da ga sami instalirate na [praznu pametnu karticu](https://satochip.io/product/blank-javacard-for-diy-project/).



Ako želite da koristite funkcionalnost bekapa Seedkeeper-a, očigledno ćete morati da kupite dve pametne kartice.



## 2. Instaliranje Seedkeeper klijenta



Prvi korak je instaliranje softvera na vašem računaru ili pametnom telefonu. Na računaru, potrebno je [preuzeti najnoviju verziju Satochip-Utils](https://github.com/Toporin/Satochip-Utils/releases). Na mobilnim uređajima, aplikacija Seedkeeper je dostupna na [Google Play Store](https://play.google.com/store/apps/details?id=org.satochip.seedkeeper) i na [Apple App Store](https://apps.apple.com/be/app/seedkeeper/id6502836060).



![Image](assets/fr/002.webp)



## 3. Inicijalizacija čuvara semena



Pokrenite aplikaciju i kliknite na dugme "*Click & Scan*".



![Image](assets/fr/003.webp)



Od vas će biti zatražen PIN kod za vaš Seedkeeper. Pošto je ovo nova kartica, PIN još nije definisan. Unesite bilo koji kod da preskočite ovaj korak, zatim kliknite na "*Next*".



![Image](assets/fr/004.webp)



Zatim postavite karticu na poleđinu vašeg pametnog telefona. Aplikacija će detektovati da Seedkeeper još nije inicijalizovan i zatražiće od vas da postavite PIN kod vaše pametne kartice, u dužini od 4 do 16 karaktera. Za optimalnu sigurnost, izaberite robustan PIN kod koji je što duži, nasumičan i sastavljen od širokog spektra karaktera. Ovaj PIN je jedina barijera protiv fizičkog pristupa vašim lozinkama.



**Zapamtite da sada sačuvate ovaj PIN**, na primer u menadžeru lozinki ili na posebnom fizičkom medijumu. U ovom drugom slučaju, nikada ne držite medijum koji sadrži PIN na istom mestu kao vaš Seedkeeper, inače će ova sigurnost postati beskorisna. Važno je imati pouzdanu rezervnu kopiju: bez PIN-a, nećete moći da povratite tajne pohranjene na vašem Seedkeeper-u.



![Image](assets/fr/005.webp)



Potvrdite svoj PIN kod po drugi put.



![Image](assets/fr/006.webp)



Vaš Seedkeeper je sada inicijalizovan. Možete ga otključati unosom PIN koda koji ste upravo postavili.



![Image](assets/fr/007.webp)



Bićete preusmereni na stranicu za upravljanje pametnom karticom.



![Image](assets/fr/008.webp)



## 4. Sačuvaj lozinke na Seedkeeper



Kada vaš Seedkeeper bude otključan, kliknite na dugme "*+*".



![Image](assets/fr/009.webp)



Izaberite "Generiši tajnu*". Opcija "*Uvezi tajnu*" omogućava vam da sačuvate postojeću tajnu (na primer, lozinku koju ste kreirali ranije).



![Image](assets/fr/010.webp)



U našem slučaju, želimo sačuvati lozinku. Kliknite na "*Password*".



![Image](assets/fr/011.webp)



Dodeli "*Oznaku*" ovoj tajni kako bi se lako identifikovala ako skladištiš više informacija u svom Seedkeeper-u. Takođe možeš dodati identifikator povezan sa lozinkom i URL-om sajta.



![Image](assets/fr/012.webp)



Izaberite dužinu i parametre vaše lozinke, zatim kliknite na "*Generate*", pa na "*Import*".



![Image](assets/fr/013.webp)



Postavite svoj Seedkeeper na poleđinu svog pametnog telefona.



![Image](assets/fr/014.webp)



Vaša lozinka je registrovana.



![Image](assets/fr/015.webp)



## 5. Pristupite svojoj Seedkeeper lozinki



Ako želite da proverite svoju lozinku, uzmite svoj Seedkeeper i kliknite na dugme "*Click & Scan*".



![Image](assets/fr/016.webp)



Unesite svoj PIN kod, zatim pritisnite "*Next*".



![Image](assets/fr/017.webp)



Postavite svoj Seedkeeper na poleđinu vašeg pametnog telefona.



![Image](assets/fr/018.webp)



Ovo vas vodi do liste svih vaših registrovanih tajni. U ovom primeru, želim da prikažem lozinku za svoj Plan ₿ Academy nalog, pa kliknem na nju.



![Image](assets/fr/019.webp)



Pritisnite dugme "*Reveal*".



![Image](assets/fr/020.webp)



Ponovo skeniraj svoj Seedkeeper.



![Image](assets/fr/021.webp)



Vaša prethodno sačuvana lozinka sada se pojavljuje na ekranu. Možete je kopirati i koristiti na odgovarajućem veb sajtu.



![Image](assets/fr/022.webp)



## 6. Pravljenje rezervne kopije Seedkeeper-a



Sada ćemo napraviti rezervnu kopiju mog Seedkeeper-a na drugom Seedkeeper-u kako bismo imali dve kopije. Ova redundancija može biti deo strategije za osiguranje vaših najvažnijih lozinki: na primer, čuvanjem vaših Seedkeeper-a na 2 odvojene lokacije kako biste ograničili fizičke rizike, ili poveravanjem kopije pouzdanom rođaku.



Da biste to uradili, ponesite svoj drugi Seedkeeper (zapamtite da jedan od njih označite kako biste izbegli bilo kakvu zabunu). Počnite inicijalizacijom, kako je opisano u koraku 3 ovog vodiča. Ponovo izaberite jak PIN kod. U zavisnosti od vaše strategije, možete se odlučiti za drugačiji PIN ili zadržati isti.



![Image](assets/fr/023.webp)



Otvorite aplikaciju, kliknite na "*Click & Scan*", unesite PIN vašeg Seedkeeper-a br. 1 (izvor), zatim ga skenirajte.



![Image](assets/fr/024.webp)



Ovo vas vodi na početnu stranicu, sa spiskom vaših tajni. Kliknite na tri male tačke u gornjem desnom uglu interfejsa.



![Image](assets/fr/025.webp)



Izaberite "*Napravite rezervnu kopiju*", zatim pritisnite "*Pokreni*".



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



To je sve što treba da uradite! Sada znate kako da koristite Seedkeeper za čuvanje vaših lozinki. U budućem vodiču, pogledaćemo kako da koristite Seedkeeper za pravljenje rezervne kopije Bitcoin wallet. Takođe vas pozivam da otkrijete njegovu kombinovanu upotrebu sa SeedSigner :



https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

https://planb.academy/tutorials/wallet/backup/seedkeeper-906dfff8-1826-4837-92d1-8669e216d356