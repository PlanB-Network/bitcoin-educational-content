---
name: Seedkeeper x SeedSigner
description: Kako da koristim Seedkeeper sa svojim SeedSigner-om?
---

![cover](assets/cover.webp)



*Zahvaljujući timu [Satochip](https://satochip.io/) za pristajanje na ponovnu upotrebu [njihovih video zapisa](https://www.youtube.com/@satochip/videos) u ovom vodiču. Takođe zahvaljujemo [Crypto Guide](https://www.youtube.com/@CryptoGuide/) za njegov Fork firmware SeedSigner-a, koji omogućava podršku za pametne kartice.



---

SeedSigner je Hardware Wallet koji sami sastavljate od standardnog hardvera, obično oko Raspberry Pi Zero. Ovaj Wallet se naziva "*bez stanja*": za razliku od većine drugih modela na tržištu (Coldcard, Trezor, Ledger, itd.), ne čuva nikakve podatke u trajnoj memoriji i radi samo uživo iz RAM-a. Kao rezultat toga, seed vašeg portfolija nikada nije sačuvan na SeedSigner-u. Svaki put kada ga ponovo pokrenete, moraćete da ga popunite kako biste omogućili uređaju da potpiše vaše transakcije. Najčešći metod je da sačuvate vaš seed kao QR kod, koji zatim skenirate svaki put kada ga koristite (*SeedQR*).



Ovaj pristup, međutim, predstavlja značajan rizik: seed mora ostati dostupan u čistom tekstu kako bi mogao biti skeniran. U slučaju krađe ili upada, napadač bi lako mogao doći do njega i ukrasti vaše bitkoine.



Da bi se prevazišla ova slabost, SeedSigner se može kombinovati sa [**Seedkeeper**](https://satochip.io/product/seedkeeper/), pametnom karticom koju je razvio Satochip. Ovo omogućava da se Mnemonic fraze (ili druge tajne) čuvaju u secure element zaštićenom PIN kodom. Seedkeeper applet je open-source, a njegov secure element ima EAL6+ sertifikaciju. Korišćen u kombinaciji sa SeedSigner-om, nudi veoma zanimljivu sigurnosnu funkciju: vaši ključevi ostaju potpuno van mreže, potpisujete svoje transakcije na pouzdanom ekranu, a seed je fizički zaštićen u pametnoj kartici otpornom na fizičke napade.



Sve što vam je potrebno za dovršetak instalacije su sledeći predmeti:




- Uobičajena oprema potrebna za klasični SeedSigner: Raspberry Pi Zero, Waveshare 1.3" ekran, kompatibilna kamera i microSD kartica (više detalja ćete pronaći u SeedSigner uputstvu ispod);
- Komplet za proširenje SeedSigner, dostupan [na zvaničnoj Satochip prodavnici](https://satochip.io/product/seedsigner-extension-kit/), omogućava vam da čitate i pišete na pametnu karticu direktno sa vašeg SeedSigner-a. Druga opcija je korišćenje eksternog čitača pametnih kartica, koji se može povezati kablom na Micro-USB port na Raspberry Pi-ju. Međutim, nisam lično testirao ovo rešenje;
- Seedkeeper, ili alternativno prazna pametna kartica na koju se može instalirati Seedkeeper applet (komplet za proširenje koji prodaje Satochip već uključuje praznu pametnu karticu).



![Image](assets/fr/01.webp)



Ovaj vodič pokriva dva scenarija:




- Ako već imate Bitcoin portfelj upravljan putem vašeg SeedSigner-a, jednostavno instalirajte novi firmware. Zatim možete nastaviti koristiti vaš postojeći Wallet, ovaj put koristeći Seedkeeper za dodatnu sigurnost.
- Ako još uvek nemate Bitcoin Wallet povezan sa vašim SeedSigner-om, moraćete da pratite korake **5** i **6** iz tutorijala pomenutog ispod. Ovi delovi objašnjavaju kako da generate Mnemonic frazu sa SeedSigner-om, sačuvate je putem *SeedQR*-a, a zatim povežete ovaj Wallet sa Sparrow wallet da biste ga upravljali. Neću ulaziti u ove procedure ovde i **pretpostavljam da već imate funkcionalan Bitcoin Wallet, konfigurisan sa Sparrow i vašim SeedSigner-om**.



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 1. Instaliraj firmware



Da biste koristili SeedSigner sa Seedkeeper-om, potrebno je instalirati alternativni firmware, različit od originalnog SeedSigner-a, kako bi se podržalo čitanje pametnih kartica. Za ovo, [preporučujem korišćenje Fork od "*3rdIteration*"](https://github.com/3rdIteration/seedsigner). Preuzmite [najnoviju verziju slike](https://github.com/3rdIteration/seedsigner/releases) (`.zip`) koja odgovara modelu Raspberry Pi koji koristite.



![Image](assets/fr/02.webp)



Ako već nemate, preuzmite softver [Balena Etcher] (https://etcher.balena.io/), zatim nastavite na sledeći način:




- Umetnite microSD karticu u vaš računar;
- Pokreni Etcher ;
- Odaberite datoteku `.zip` koju ste upravo preuzeli;
- Izaberite microSD karticu kao cilj;
- Kliknite na `Flash!`.



![Image](assets/fr/03.webp)



Sačekajte dok se proces ne završi: vaša microSD kartica je sada spremna za korišćenje. Sada možete preći na sklapanje vašeg uređaja.



Za više detalja o instalaciji firmvera i verifikaciji softvera (korak koji vam toplo preporučujem da preduzmete), pogledajte sledeći vodič:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 2. Sastavljanje čitača pametnih kartica



![video](https://youtu.be/jqE8HDMCImA)



Počnite instaliranjem kamere na Raspberry Pi Zero, pažljivo je umetnite u pin za kameru i zaključajte crnom zaklopkom. Zatim postavite Pi na dno kućišta, pazeći da poravnate portove sa odgovarajućim otvorima.



![Image](assets/fr/04.webp)



Zatim priključite čitač pametnih kartica na GPIO pinove Raspberry Pi Zero.



![Image](assets/fr/05.webp)



Prevucite plastični poklopac preko čitača pametnih kartica dok ne bude pravilno postavljen.



![Image](assets/fr/06.webp)



Zatim dodajte ekran na GPIO pinove ekstenzije.



![Image](assets/fr/07.webp)



Na kraju, ubacite microSD karticu koja sadrži firmware u bočni port na Raspberry Pi Zero.



![Image](assets/fr/08.webp)



Sada možete povezati svoj SeedSigner ili putem Micro-USB porta na Raspberry Pi Zero, ili putem USB-C porta na ekstenziji. Oba načina funkcionišu. Sačekajte nekoliko sekundi za pokretanje, zatim bi trebalo da se pojavi ekran dobrodošlice.



![Image](assets/fr/09.webp)



Za više detalja o početnom podešavanju vašeg SeedSigner-a, preporučujem sledeći vodič:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 3. Flash-ovati smart karticu sa Seedkeeper applet-om (opciono)



![video](https://youtu.be/NF4HemyEcOY)



Ako već posedujete Seedkeeper, možete preskočiti ovaj korak i preći direktno na korak 4. U ovom delu ćemo pogledati kako instalirati Seedkeeper aplet na praznu pametnu karticu (uradi sam metoda).



Da biste započeli, otvorite meni `Tools > Smartcard Tools` na vašem SeedSigner-u.



![Image](assets/fr/10.webp)



Zatim izaberite `DIY Tools > Install Applet`.



![Image](assets/fr/11.webp)



Umetnite svoju pametnu karticu u SeedSigner čitač, čip okrenut nadole, zatim izaberite `SeedKeeper` aplet.



![Image](assets/fr/12.webp)



Molimo vas da budete strpljivi tokom instalacije: proces može potrajati nekoliko desetina sekundi.



![Image](assets/fr/13.webp)



Kada je aplet uspešno instaliran, možete preći na korak 4.



![Image](assets/fr/14.webp)



## 4. Sačuvaj postojeći SeedQR na Seedkeeper



![video](https://youtu.be/X-vmFHU9Ec8)



Sada kada je vaš Seedkeeper operativan, možete sačuvati vaš Bitcoin Wallet Mnemonic na smart kartici. Da biste započeli, uključite vaš SeedSigner kao i obično, zatim skenirajte *SeedQR* vašeg Wallet da biste ga učitali u uređaj. Kada je seed uvezen, jednostavno izaberite `Done`.



![Image](assets/fr/15.webp)



Kada je seed učitan, pristupite meniju `Backup seed`.



![Image](assets/fr/16.webp)



Zatim umetnite svoj Seedkeeper u SeedSigner drajv i izaberite opciju `To SeedKeeper`.



![Image](assets/fr/17.webp)



SeedSigner će vas zatim zamoliti da unesete PIN kod za vaš Seedkeeper. Pošto je ovo prazna kartica, kod još nije definisan. Unesite bilo koji kod da preskočite ovaj korak, a zatim potvrdite.



![Image](assets/fr/18.webp)



SeedSigner detektuje da Seedkeeper još nije inicijalizovan (tj. lozinka nije postavljena). Kliknite `Razumem` da nastavite.



![Image](assets/fr/19.webp)



Sada izaberite novi PIN kod za vaš Seedkeeper, između 4 i 16 karaktera. Za dodatnu sigurnost, izaberite dug, nasumičan kod: to je jedina barijera koja štiti fizički pristup vašoj Mnemonic frazi.



Zapamtite da sačuvate ovaj PIN čim bude kreiran, bilo u pouzdanom menadžeru lozinki, ili na posebnom fizičkom mediju u zavisnosti od vaše strategije. U ovom drugom slučaju, pazite da nikada ne držite medij koji sadrži PIN na istom mestu kao vaš Seedkeeper, inače će zaštita postati neefikasna. Važno je imati rezervnu kopiju: **Bez ovog PIN-a, nećete moći da pristupite svom seed, i vaši bitkoini će biti izgubljeni**.



![Image](assets/fr/20.webp)



Zatim možete definisati `Label` povezan sa vašom Mnemonic frazom. Ova oznaka je korisna ako čuvate nekoliko tajni na Seedkeeper-u, kako biste ih lako mogli identifikovati.



![Image](assets/fr/21.webp)



Vaša Mnemonic fraza je sada sačuvana na pametnoj kartici.



![Image](assets/fr/22.webp)



U smislu bezbednosne strategije, moguće je nekoliko pristupa, u zavisnosti od vaših potreba i nivoa izloženosti riziku. Lično, preporučujem da zadržite najmanje 2 kopije vašeg seed:




- Ovo je prvi put za pametne kartice, koje možete držati lako dostupnim za svakodnevne operacije, kao što su verifikacija adresa ili potpisivanje transakcija. Ova metoda je praktična (kao što ćemo videti u delu 5) i ostaje sigurna zahvaljujući zaštiti koju nudi PIN kod, tako da je možete držati dostupnom bez većeg rizika;
- Druga kopija vaše nešifrovane Mnemonic fraze, koja služi kao krajnja rezervna kopija vašeg portfolija, da se koristi samo u slučaju gubitka ili krađe Seedkeeper-a. Pošto je ova verzija nešifrovana, mora se čuvati na odvojenom, sigurnijem mestu, kako bi se sprečila istovremena kompromitacija 2 rezervne kopije.



U zavisnosti od vaše strategije zaštite i profila rizika, možete takođe duplicirati seed na nekoliko različitih Seedkeeper-a, ili kreirati nekoliko fizičkih kopija Mnemonic. Da biste saznali više o ovim praksama, pogledajte sledeći tutorijal:



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270


## 5. Učitavanje seed iz Seedkeeper-a



![video](https://youtu.be/ms0Iq_IyaoE)



Sada možete koristiti svoj Seedkeeper za učitavanje vaše Mnemonic fraze u SeedSigner pri pokretanju, i tako potpisati vaše Bitcoin transakcije. Da biste započeli, uključite vaš SeedSigner tako što ćete ga priključiti, zatim otvorite meni `Seeds`.



![Image](assets/fr/23.webp)



Zatim izaberite opciju `From SeedKeeper`.



![Image](assets/fr/24.webp)



Umetnite svoj Seedkeeper u čitač pametnih kartica, zatim unesite svoj PIN kod da ga otključate. Potvrdite unos pritiskom na donje-desno dugme za potvrdu, `KEY3`.



![Image](assets/fr/25.webp)



Seedkeeper može sadržati nekoliko tajni, tako da SeedSigner zatim traži da izaberete onu koju želite učitati. Prikazana oznaka odgovara imenu koje ste definisali u koraku 4. Ako ste, kao u mom slučaju, registrovali samo jedan seed, biće dostupna samo jedna opcija.



![Image](assets/fr/26.webp)



Vaš seed je sada učitan. Proverite da li je ovo ispravan Wallet upoređivanjem otiska prsta prikazanog na ekranu sa onim navedenim u vašim Sparrow wallet podešavanjima. Ovaj otisak prsta je takođe obezbeđen kada je Wallet prvi put kreiran.



Ako koristite passphrase, možete ga primeniti u ovoj fazi (pogledajte deo 6 ovog tutorijala). U suprotnom, jednostavno kliknite na `Done`.



![Image](assets/fr/27.webp)



Zatim možete koristiti svoj Wallet kao i obično: proverite adrese za dostavu i potpišite transakcije, baš kao sa klasičnim SeedSigner-om. Da biste saznali više o tome kako ga koristiti, pogledajte posvećeni vodič :



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 6. Korišćenje Seedkeeper-a sa passphrase BIP39



Da li koristite passphrase da zaštitite svoj Bitcoin portfolio? Takođe ga možete registrovati u svom Seedkeeper-u, zajedno sa vašim seed. Ovo rešenje će vam omogućiti da brzo učitate svoj Wallet na SeedSigner, bez potrebe da ručno unosite passphrase na maloj tastaturi svaki put kada ga koristite.



Smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram smatram sm




- Čuvajte svoj seed i passphrase u Seedkeeper-u, zaštićeni jakim PIN kodom (ovo je važno). Ova rezervna kopija će vam omogućiti da lako koristite svoj Wallet na dnevnoj bazi. Ako želite, možete duplicirati ove informacije na drugom Seedkeeper-u;
- Takođe, čuvajte jasnu kopiju vašeg Mnemonic i passphrase, na papiru ili metalu. Ovo je vaša rezervna kopija poslednjeg izbora ako izgubite Seedkeeper ili njegov PIN. Obavezno čuvajte ove kopije na različitim lokacijama, kako ne bi mogle biti ugrožene istovremeno.



U ovoj konfiguraciji, ako neko dođe do vašeg otvorenog teksta Mnemonic samog, neće moći da ukrade ništa bez poznavanja passphrase (pod uslovom, naravno, da je dovoljno jak da izdrži napad grube sile). S druge strane, ako neko otkrije vaš otvoreni tekst passphrase, on će ostati neupotrebljiv bez odgovarajuće fraze Mnemonic.



Konačno, ako neko uspe da fizički pristupi vašem Seedkeeper-u koji sadrži seed i passphrase, neće moći da izvuče ništa bez poznavanja PIN koda. Za razliku od passphrase, ovaj kod ne može biti probijen metodom grube sile, jer se smart kartica automatski zaključava nakon 5 nevažećih pokušaja.



Bezbednost ove konfiguracije se stoga zasniva na 2 suštinske tačke:




- **passphrase strong**: mora biti dugačka, nasumična i sadržavati širok spektar karaktera. Njena složenost nije problem za vas, jer ćete je uneti samo jednom na tastaturi tokom inicijalizacije, nakon čega će je prenositi Seedkeeper;
- **Jak PIN kod** za Seedkeeper: takođe nasumičan i sastavljen od 16 karaktera.



Da biste postavili ovu postavku, počnite tako što ćete učitati svoj passphrase u SeedSigner na uobičajen način. Možete pratiti postupak detaljno opisan u ovom vodiču:



https://planb.academy/tutorials/wallet/backup/seedsigner-passphrase-7a61f64d-aa03-4bcf-8308-00c89a74cffe

Kada je vaš portfolio sa passphrase ispravno učitan na SeedSigner, otvorite meni `Seeds` i izaberite otisak koji odgovara ovom portfoliju. Imajte na umu da se ovaj otisak razlikuje od onog portfolija bez passphrase.



![Image](assets/fr/28.webp)



Zatim kliknite na `Backup seed`, umetnite Seedkeeper u drajv i izaberite `To SeedKeeper`.



![Image](assets/fr/29.webp)



Unesite svoj PIN da otključate Seedkeeper, zatim dodelite oznaku ovoj tajni. Možete ostaviti otisak prsta kao oznaku da zadržite neki oblik uverljive poricljivosti, ili eksplicitno navesti `passphrase Wallet`, na primer.



![Image](assets/fr/30.webp)



Vaš passphrase portfolio je sada registrovan na Seedkeeper.



![Image](assets/fr/31.webp)



Sledeći put kada pokrenete, jednostavno umetnite vaš Seedkeeper u drajv, zatim idite na `Seeds > From SeedKeeper`.



![Image](assets/fr/32.webp)



Unesite svoj PIN kod da otključate pametnu karticu, zatim izaberite Wallet koji odgovara vašem passphrase.



![Image](assets/fr/33.webp)



Proveri passphrase i svoj otisak Wallet, zatim potvrdi.



![Image](assets/fr/34.webp)



Sada možete pristupiti svom portfoliju sa passphrase i potpisivati svoje transakcije kao što to obično radite na SeedSigner-u.



## 7. Dodatne opcije



U meniju `Alati > Alati za pametne kartice`, pronaći ćete nekoliko opcija za upravljanje vašim Seedkeeper-om:





- U meniju `Common Tools` možete:
 - Proveri autentičnost kartice;
 - Promeni PIN kod ;
 - Promenite oznake povezane sa vašim tajnama ;
 - Onemogući NFC funkciju (preporučuje se ako koristite samo čitač čipova) ;
 - Izvrši fabričko resetovanje.





- U meniju `SeedKeeper Functions`, možete :
 - Konsultujte listu registrovanih tajni ;
 - Sačuvaj novu tajnu ;
 - Izbriši postojeću tajnu ;
 - Sačuvaj ili učitaj svoje deskriptore (korisna funkcija za Multisig portfolije).





- U meniju `DIY Tools`, možete :
 - Kompilacija Seedkeeper apleta ;
 - Instalirajte aplet na praznu karticu ;
 - Izbrišite Seedkeeper aplet da biste ga resetovali i ponovo učinili praznim.



Sada znate kako koristiti Seedkeeper za sigurno pravljenje rezervne kopije vašeg portfolija u kombinaciji sa SeedSigner-om.



Ako vas je ova postavka uverila, ne oklevajte da podržite projekte koji je omogućavaju:




- Kupovinom vaše opreme direktno [na Satochip vebsajtu](https://satochip.io/shop/);
- Doniranjem [projektu SeedSigner](https://seedsigner.com/donate/);
- Pretplatom na [YouTube kanal Crypto Guide](https://www.youtube.com/@CryptoGuide/), koji vodi osoba koja održava GitHub repozitorijum sa modifikovanim firmverom.