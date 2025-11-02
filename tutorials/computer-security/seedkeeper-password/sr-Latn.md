---
name: Seedkeeper - Menadžer Lozinki
description: Kako sačuvati svoje lozinke pomoću Seedkeeper pametne kartice?
---

![cover](assets/cover.webp)



Seedkeeper je pametna kartica koju je razvila Satochip, belgijska kompanija specijalizovana za hardverska rešenja za upravljanje i zaštitu digitalnih tajni. Poznata po svom asortimanu pametnih kartica za Bitcoin ekosistem, Satochip je osmislio Seedkeeper kao alternativu tradicionalnim metodama čuvanja Mnemonic fraza i drugih digitalnih tajni.



U konkretnom smislu, Seedkeeper ima oblik multifunkcionalne, EAL6-certifikovane pametne kartice sa sigurnim procesorom i memorijom otpornom na neovlašćene izmene (tj. "*secure element*"). Kao što ime sugeriše, njegova uloga je da čuva mnemonike i lozinke Bitcoin portfolija na šifrovan i zaštićen način. Sa Seedkeeper-om, možete generate, uvoziti, organizovati i čuvati svoje tajne direktno u sigurnom komponentu kartice.



Po mom mišljenju, Seedkeeper ima dve glavne upotrebe, koje ćemo istražiti u 2 odvojena tutorijala:




- Bitcoin** Mnemonic skladištenje fraza: umesto da zapisujete svojih 12 ili 24 reči na papir, možete ih uneti u pametnu karticu i zaštititi PIN kodom.
- Upravljanje lozinkama**: možete generisati generate jake lozinke putem aplikacije Seedkeeper i sačuvati ih direktno na pametnoj kartici, što vam omogućava praktičan, jednostavan za korišćenje offline menadžer lozinki.



Tehnički gledano, Seedkeeper ima kapacitet od 8192 bajta, što mu omogućava da sačuva najmanje 50 odvojenih tajni (tačan broj će zavisiti od njihove veličine i metapodataka povezanih sa svakom od njih). Seedkeeper se može pristupiti ili [preko čitača pametnih kartica povezanog](https://satochip.io/accessories/) sa računarom, ili putem mobilne aplikacije sa NFC vezom. Ceo sistem radi u offline režimu, bez internet konekcije, garantujući ograničenu površinu za napad.



![Image](assets/fr/001.webp)



Posebno zanimljiva funkcija je mogućnost dupliranja sadržaja jednog Seedkeeper-a na drugi kako biste napravili rezervnu kopiju. U ovom vodiču pokazaćemo vam kako to da uradite.



U ovom vodiču pokrićemo samo upotrebu SeedKeeper-a za tradicionalne lozinke, na način menadžera lozinki. Ako želite koristiti SeedKeeper za čuvanje Bitcoin Wallet Mnemonic fraza, molimo pogledajte ovaj drugi vodič:



https://planb.network/tutorials/wallet/backup/seedkeeper-906dfff8-1826-4837-92d1-8669e216d356

## 1. Kako da dobijem Seedkeeper?



Postoje dva glavna načina da nabavite svoj Seedkeeper. Možete ga [kupiti direktno iz Satochip-ove zvanične prodavnice](https://satochip.io/product/seedkeeper/) ili od ovlašćenog prodavca. Ali pošto je [Seedkeeper applet otvorenog koda](https://github.com/Toporin/Seedkeeper-Applet), takođe imate opciju da ga sami instalirate na [praznu pametnu karticu](https://satochip.io/product/blank-javacard-for-diy-project/).



Ako želite koristiti funkcionalnost pravljenja rezervnih kopija Seedkeeper-a, očigledno ćete morati kupiti dve pametne kartice.



## 2. Instaliranje Seedkeeper klijenta



Prvi korak je instaliranje softvera na vašem računaru ili pametnom telefonu. Na računaru, potrebno je [preuzeti najnoviju verziju Satochip-Utils](https://github.com/Toporin/Satochip-Utils/releases). Na mobilnom uređaju, aplikacija Seedkeeper je dostupna na [Google Play Store](https://play.google.com/store/apps/details?id=org.satochip.seedkeeper) kao i na [Apple App Store](https://apps.apple.com/be/app/seedkeeper/id6502836060).



![Image](assets/fr/002.webp)



## 3. Inicijalizacija Seedkeeper-a



Pokrenite aplikaciju i kliknite na dugme "*Click & Scan*".



![Image](assets/fr/003.webp)



Bićete upitani za PIN kod za vaš Seedkeeper. Pošto je ovo nova kartica, PIN još nije definisan. Unesite bilo koji kod da preskočite ovaj korak, zatim kliknite na "*Next*".



![Image](assets/fr/004.webp)



Zatim postavite karticu na poleđinu svog pametnog telefona. Aplikacija će detektovati da Seedkeeper još nije inicijalizovan i zatražiće od vas da postavite PIN kod vaše pametne kartice, u dužini od 4 do 16 karaktera. Za optimalnu sigurnost, izaberite robustan PIN kod koji je što duži, nasumičan i sastavljen od širokog spektra karaktera. Ovaj PIN je jedina barijera protiv fizičkog pristupa vašim lozinkama.



**Zapamti da sada sačuvaš ovaj PIN**, na primer u menadžeru lozinki, ili na posebnom fizičkom mediju. U ovom drugom slučaju, nikada ne drži medijum koji sadrži PIN na istom mestu kao i tvoj Seedkeeper, inače će ova sigurnost postati beskorisna. Važno je imati pouzdanu rezervnu kopiju: bez PIN-a, nećeš moći da povratiš tajne sačuvane na tvom Seedkeeper-u.



![Image](assets/fr/005.webp)



Potvrdite svoj PIN kod po drugi put.



![Image](assets/fr/006.webp)



Vaš Seedkeeper je sada inicijalizovan. Možete ga otključati unosom PIN koda koji ste upravo postavili.



![Image](assets/fr/007.webp)



Sada ćete biti preusmereni na stranicu za upravljanje pametnom karticom.



![Image](assets/fr/008.webp)



## 4. Sačuvaj lozinke na Seedkeeper



Jednom kada vaš Seedkeeper bude otključan, kliknite na dugme "*+*".



![Image](assets/fr/009.webp)



Odaberite "generate secret*". Opcija "*Import a secret*" omogućava vam da sačuvate postojeću tajnu (na primer, lozinku koju ste kreirali u prošlosti).



![Image](assets/fr/010.webp)



U našem slučaju, želimo sačuvati lozinku. Kliknite na "*Password*".



![Image](assets/fr/011.webp)



Dodelite "*Oznaku*" ovoj tajni kako bi se lako identifikovala ako skladištite više informacija u vašem Seedkeeper-u. Takođe možete dodati korisničko ime povezano sa lozinkom i URL sajta.



![Image](assets/fr/012.webp)



Izaberite dužinu i parametre vaše lozinke, zatim kliknite na "*generate*", pa na "*Import*".



![Image](assets/fr/013.webp)



Postavite svoj Seedkeeper na poleđinu vašeg pametnog telefona.



![Image](assets/fr/014.webp)



Vaša lozinka je registrovana.



![Image](assets/fr/015.webp)



## 5. Pristupite svojoj Seedkeeper lozinki



Ako želite da proverite svoju lozinku, uzmite svoj Seedkeeper i kliknite na dugme "*Click & Scan*".



![Image](assets/fr/016.webp)



Unesite svoj PIN kod, zatim pritisnite "*Next*".



![Image](assets/fr/017.webp)



Postavite svoj Seedkeeper na poleđinu svog pametnog telefona.



![Image](assets/fr/018.webp)



Ovo vas vodi do liste svih vaših registrovanih tajni. U ovom primeru, želim da prikažem lozinku za moj Plan ₿ Network nalog, pa kliknem na njega.



![Image](assets/fr/019.webp)



Pritisnite dugme "*Reveal*".



![Image](assets/fr/020.webp)



Skeniraj svoj Seedkeeper ponovo.



![Image](assets/fr/021.webp)



Vaša prethodno sačuvana lozinka sada se pojavljuje na ekranu. Možete je kopirati i koristiti na odgovarajućem sajtu.



![Image](assets/fr/022.webp)



## 6. Pravljenje rezervne kopije Seedkeeper-a



Sada ćemo napraviti rezervnu kopiju mog Seedkeeper-a na drugom Seedkeeper-u kako bismo imali dve kopije. Ova redundancija može biti deo strategije za zaštitu vaših najvažnijih lozinki: na primer, čuvanje vaših Seedkeeper-a na 2 odvojene lokacije kako biste ograničili fizičke rizike, ili poveravanje kopije pouzdanom rođaku.



Da biste to uradili, ponesite svoj drugi Seedkeeper (zapamtite da jedan od njih označite kako biste izbegli bilo kakvu zabunu). Počnite tako što ćete ga inicijalizovati, kao što je opisano u koraku 3 ovog vodiča. Ponovo izaberite jak PIN kod. U zavisnosti od vaše strategije, možete se odlučiti za drugačiji PIN ili zadržati isti.



![Image](assets/fr/023.webp)



Otvorite aplikaciju, kliknite na "*Click & Scan*", unesite PIN vašeg Seedkeeper-a br. 1 (izvor), zatim ga skenirajte.



![Image](assets/fr/024.webp)



Ovo vas vodi na početnu stranicu, sa spiskom vaših tajni. Kliknite na tri male tačke u gornjem desnom uglu Interface.



![Image](assets/fr/025.webp)



Odaberite "*Make a backup*", zatim pritisnite "*Start*".



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



To je sve što treba da uradite! Sada znate kako da koristite Seedkeeper za čuvanje vaših lozinki. U budućem vodiču, pogledaćemo kako da koristite Seedkeeper za pravljenje rezervne kopije Bitcoin portfolija. Takođe vas pozivam da otkrijete njegovu kombinovanu upotrebu sa SeedSigner:



https://planb.network/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

https://planb.network/tutorials/wallet/backup/seedkeeper-906dfff8-1826-4837-92d1-8669e216d356