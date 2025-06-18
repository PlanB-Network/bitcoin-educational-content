---
name: BitBox02

description: Postavljanje i korišćenje BitBox02
---

![cover](assets/cover.webp)


BitBox02 (https://bitbox.swiss/) je fizički Wallet švajcarske proizvodnje, posebno dizajniran za zaštitu vaših Bitcoina. Neke od njegovih ključnih karakteristika uključuju jednostavno pravljenje rezervnih kopija i obnavljanje pomoću microSD kartice, minimalistički i diskretan dizajn, kao i sveobuhvatnu podršku za Bitcoin.


![device](assets/1.webp)


Nudi vrhunsku sigurnost koju su osmislili stručnjaci, sa dizajnom sa dva čipa koji uključuje sigurnosni čip. Njegov izvorni kod je u potpunosti pregledan od strane istraživača sigurnosti i potpuno je otvorenog koda. BitBox02 dolazi sa jednostavnom, ali moćnom BitBoxApp aplikacijom, koja omogućava sigurno upravljanje vašim Bitcoinima. Podržava Full node za Bitcoin i osigurava end-to-end šifrovanu komunikaciju između aplikacije i uređaja. Proizveden u Švajcarskoj, BitBox02 je stekao pozitivnu reputaciju među svojim korisnicima.


![video](https://youtu.be/sB4b2PbYaj0)


Evo su specifikacije za Wallet:



- Povezivanje: USB-C
- Kompatibilnost: Windows 7 i noviji, macOS 10.13 i noviji, Linux, Android
- Ulaz: Kapacitivni senzori na dodir
- Mikrokontroler: ATSAMD51J20A; 120 Mhz 32-bit Cortex-M4F; Pravi generator slučajnih brojeva
- Siguran čip: ATECC608B; Pravi generator slučajnih brojeva (NIST SP 800-90A/B/C)
- Prikaz: 128 x 64 px bela OLED
- Materijal: Polikarbonat
- Veličina: 54.5 x 25.4 x 9.6 mm uključujući USB-C priključak
- Težina: Uređaj 12g; sa pakovanjem i dodacima 160g


Preuzmite podatkovne listove na njihovoj veb stranici https://bitbox.swiss/bitbox02/


## Kako koristiti BitBox02 Hardware Wallet


### Postavljanje BitBox02


BitBox02 ima USB-C konekciju povezanu sa kućištem. Ako vaš računar koristi standardni USB port, moraćete da koristite adapter koji dolazi uz uređaj.


Povežite ga sa računarom i uređaj će se uključiti (nemojte to još raditi).


Ima senzore iznad i ispod, i podstaknuće vas da dodirnete vrh ili dno kako biste postavili ekran onako kako želite.


![image](assets/2.webp)


### Preuzmi BitBox02 aplikaciju


Posetite https://shiftcrypto.ch/ i kliknite na link „App“ na vrhu da biste došli do stranice za preuzimanje:


![image](assets/3.webp)


Kliknite plavo dugme Preuzmi:


![image](assets/4.webp)


Da biste verifikovali preuzimanje (dodaje složenost, ali se preporučuje, posebno ako skladištite mnogo Bitcoin), pogledajte Dodatak A.


Nakon preuzimanja, možete raspakovati fajl. Na Mac-u, samo dvaput kliknite na preuzeti fajl i BitBox App ikonica će se pojaviti u vašem direktorijumu za preuzimanja. Možete je prevući na desktop (ili bilo gde) za lakši pristup.


Dvaput kliknite na aplikaciju da je pokrenete (ne „instalira“ se).


Na Mac-u, vaša dadilja za računar će vam dati upozorenje. Samo ga ignorišite i kliknite „otvori“:


![image](assets/5.webp)


Videćete zatim ovo:


![image](assets/6.webp)


Poveži uređaj sa računarom.


Pokazaće vam kod za uparivanje. Proverite da li se podudaraju, a zatim dodirnite senzor da biste izabrali oznaku za potvrdu. Zatim se vratite na ekran, dugme za nastavak će vam postati dostupno.


![image](assets/7.webp)


Imaćete opciju da kreirate novi seed, ili da obnovite seed. Pokazaću kako se kreira novi seed (Važno je takođe obnoviti seed koji ste kreirali da biste testirali kvalitet vaše rezervne kopije, pre nego što učitate bilo koji Bitcoin na Wallet).


![image](assets/8.webp)


Uređaj je došao sa microSD karticom. Slobodno je umetnite ako već niste.


![image](assets/9.webp)


Imenujte svoj uređaj i kliknite na Nastavi, zatim potvrdite na uređaju.


![image](assets/10.webp)


Bićete zamoljeni da postavite lozinku za uređaj. Ovo nije deo vašeg seed. Nije ni passphrase (to je deo vašeg seed). To je jednostavno lozinka za zaključavanje uređaja. Kada uključite uređaj, bićete zamoljeni da unesete ovu lozinku svaki put. Imate dozvoljeno 10 uzastopnih neuspeha pre nego što uređaj obriše svu memoriju, pa budite pažljivi. Animacija na ekranu će vas naučiti kako da koristite kontrole uređaja za postavljanje lozinke.


![image](assets/11.webp)


Pročitajte sledeći ekran i označite svaki okvir, zatim nastavite.


![image](assets/12.webp)

![image](assets/13.webp)

![image](assets/14.webp)


I ovako izgleda Wallet kada je spreman za upotrebu.


![image](assets/15.webp)


### NE TAKO BRZO!!


Prilično je čudno, ali BitBox02 nam govori da smo spremni za korišćenje uređaja, ali nas nije podstakao da zapišemo seed reči! JEDINA rezervna kopija koju imamo je fajl sačuvan na microSD kartici. Ovo je neadekvatno. Ovi uređaji za skladištenje ne traju zauvek (zbog "bit rot"). Potreban nam je papirni bekap, i duplikati, čuvani u sefovima (kao što je objašnjeno u opštem vodiču za korišćenje hardverskih novčanika).


Da biste dobili našu seed frazu i zapisali je, idite na karticu „upravljanje uređajem“ sa leve strane, a zatim kliknite na „prikaži reči za oporavak“


![image](assets/16.webp)


Zatim možete proći kroz potvrdu, a uređaj će vam prikazati reči. Zapišite ih uredno i nikada ne dozvolite nikome da vidi te reči.


![image](assets/17.webp)


Nakon toga, možete kliknuti na karticu Bitcoin s leve strane da biste dobili svoje adrese za primanje.


![image](assets/18.webp)


Prikazuje jedan po jedan, ali vam barem omogućava da izaberete koji Address da koristite od prvih 20:


![image](assets/19.webp)


Klikom na plavo dugme prikazaće se ceo Address, i bićete upitani da proverite da li Address odgovara prikazu na ekranu. Ovo je dobra praksa da potvrdite da vas nijedan malver na vašem računaru ne vara da pošaljete Bitcoin napadačevom Address.


![image](assets/20.webp)


Da biste poslali Bitcoin na ovaj Wallet, možete kopirati Address i nalepiti ga na stranicu za povlačenje Exchange gde su vaši novčići. Preporučujem da prvo pošaljete mali testni iznos, a zatim vežbate trošenje ili nazad na Exchange ili na drugi Address u vašem Wallet.


Za veće iznose, predlažem da napravite passphrase (pogledajte ispod). Originalni Wallet (bez passphrase) može se koristiti kao vaš lažni Wallet (potrebno je da ima razuman iznos kako bi bio uverljiv kao lažni).


### Poveži se na čvor


BitBox02 će se automatski povezati na čvor. Hajde da vidimo gde se povezuje. Kliknite na karticu sa podešavanjima sa leve strane, a zatim na „poveži svoj Full node“.


![image](assets/21.webp)


I ovde možemo videti da se povezuje na shiftcrypto-ov čvor. Nije sjajno. Izdali smo sve naše Bitcoin adrese njima, i naš IP Address (naravno, ne seed; mogu videti naše adrese/salda, ali ih ne mogu trošiti). Možemo uneti detalje našeg čvora na ovoj stranici (izvan okvira ovog konkretnog vodiča), ili možemo koristiti bolji softver kao što su Sparrow Bitcoin Wallet, Electrum Desktop Wallet, ili Specter Desktop. Pokazaću Sparrow Bitcoin Wallet kasnije u vodiču.


![image](assets/22.webp)


Dodajte passphrase


Sada kada smo postavili uređaj sa BitBox02 aplikacijom (i otkrili naše adrese, što je neizbežno sa ovim posebnim Hardware Wallet), možemo dodati passphrase našoj seed frazi. Ovo će nam omogućiti da kreiramo novi Wallet koristeći isti seed, a ShiftCrypto nikada neće videti naše nove adrese. Povezivaćemo ovaj Wallet samo sa našim softverom.


### Omogući passphrase


Sada nastavite i „omogućite“ funkciju passphrase (ali još ne postavljamo passphrase). Idite na karticu „upravljanje uređajem“ i kliknite na „omogući passphrase“ (crveni krug ispod).


![image](assets/23.webp)


Pročitajte korake…


![image](assets/24.webp)

![image](assets/25.webp)

![image](assets/26.webp)


Sada isključite uređaj i ugasite BitBox02 aplikaciju.


KRAJ odeljka bitbox02 od Parman.


Vaš uređaj je sada potpuno operativan za korišćenje na bilo kom desktop rešenju kao što su specter, sparrow i korišćenje bitbox Interface.