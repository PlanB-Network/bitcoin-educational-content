---
name: VeraCrypt
description: Kako lako enkriptovati uređaj za skladištenje?
---
![cover](assets/cover.webp)


Danas je važno implementirati strategiju kako bi se osigurala pristupačnost, sigurnost i backup vaših fajlova, kao što su vaši lični dokumenti, fotografije ili važni projekti. Gubitak ovih podataka može biti katastrofalan.


Da biste sprečili ove probleme, savetujem vam da održavate više rezervnih kopija vaših fajlova na različitim medijima. Uobičajena strategija u računarstvu je strategija rezervne kopije "3-2-1", koja osigurava zaštitu vaših fajlova:


- 3** kopije vaših fajlova;
- Sačuvano na najmanje **2** različite vrste medija;
- Sa najmanje **1** kopijom čuvanom van lokacije.


Drugim rečima, preporučljivo je čuvati vaše fajlove na 3 različite lokacije, koristeći medije različite prirode, kao što su vaš računar, eksterni Hard disk, USB stik ili online uslugu skladištenja. I na kraju, imati kopiju van lokacije znači da bi trebalo da imate rezervnu kopiju pohranjenu izvan vašeg doma ili poslovnog prostora. Ova poslednja tačka pomaže da se izbegne potpuni gubitak vaših fajlova u slučaju lokalnih katastrofa kao što su požari ili poplave. Eksterna kopija, udaljena od vašeg doma ili poslovnog prostora, osigurava da će vaši podaci preživeti nezavisno od lokalnih rizika.


Da biste lako implementirali ovu 3-2-1 strategiju bekapa, možete se odlučiti za rešenje za skladištenje na mreži, automatskim ili periodičnim sinhronizovanjem fajlova sa vašeg računara sa onima u vašem oblaku. Među ovim rešenjima za bekap na mreži, očigledno su i ona od velikih digitalnih kompanija koje poznajete: Google Drive, Microsoft OneDrive ili Apple iCloud. Međutim, ovo nisu najbolja rešenja za zaštitu vaše privatnosti. U prethodnom tutorijalu, predstavio sam vam alternativu koja šifruje vaše dokumente za bolju poverljivost: Proton Drive.


https://planb.network/tutorials/computer-security/data/proton-drive-03cbe49f-6ddc-491f-8786-bc20d98ebb16

Usvajanjem ove strategije lokalne i cloud sigurnosne kopije, već imate koristi od dve različite vrste medija za vaše podatke, od kojih je jedan van lokacije. Da biste kompletirali strategiju 3-2-1, jednostavno treba da dodate dodatnu kopiju. Ono što vam savetujem je da periodično izvozite vaše podatke prisutne lokalno i na vašem cloudu na fizički medij, kao što je USB stik ili eksterni Hard disk. Na taj način, čak i ako su serveri vašeg online rešenja za skladištenje uništeni i vaš računar se istovremeno pokvari, i dalje imate ovu treću kopiju na eksternom mediju kako ne biste izgubili vaše podatke.

![VeraCrypt](assets/notext/01.webp)

Ali je takođe važno razmisliti o sigurnosti vašeg skladištenja podataka kako biste osigurali da niko osim vas ili vaših voljenih ne može pristupiti njima. I lokalni i online podaci su obično sigurni. Na vašem računaru, verovatno ste postavili lozinku, a Hard diskovi modernih računara su često šifrovani po defaultu. Što se tiče vašeg online skladišta (oblaka), pokazao sam vam u prethodnom vodiču kako da osigurate svoj nalog jakom lozinkom i dvofaktorskom autentifikacijom. Međutim, za vašu treću kopiju koja je pohranjena na fizičkom mediju, jedina sigurnost je njeno fizičko posedovanje. Ako provalnik uspe da ukrade vaš USB stik ili vaš eksterni Hard disk, mogao bi lako pristupiti svim vašim podacima.

![VeraCrypt](assets/notext/02.webp)

Da biste sprečili ovaj rizik, preporučljivo je šifrovati vaš fizički medijum. Tako će svaki pokušaj pristupa podacima zahtevati unos lozinke za dešifrovanje sadržaja. Bez ove lozinke, biće nemoguće pristupiti podacima, čime se vaši lični fajlovi obezbeđuju čak i u slučaju krađe vašeg USB stika ili vašeg eksternog Hard drajva.

![VeraCrypt](assets/notext/03.webp)

U ovom vodiču, pokazaću vam kako lako enkriptovati eksterni skladišni medijum koristeći VeraCrypt, alat otvorenog koda.


## Uvod u VeraCrypt


VeraCrypt je softver otvorenog koda dostupan na Windows, macOS i Linux sistemima, koji vam omogućava da šifrujete vaše podatke na različite načine i na različitim medijima.

![VeraCrypt](assets/notext/04.webp)

Ovaj softver omogućava kreiranje i održavanje šifrovanih volumena u hodu, što znači da se vaši podaci automatski šifruju pre nego što budu sačuvani i dešifruju pre nego što budu pročitani. Ova metoda osigurava da vaši fajlovi ostanu zaštićeni čak i u slučaju krađe vašeg skladišnog medija. VeraCrypt ne šifruje samo fajlove, već i nazive fajlova, metapodatke, foldere, pa čak i slobodan prostor na vašem skladišnom mediju.


VeraCrypt se može koristiti za šifrovanje fajlova lokalno ili čitavih particija, uključujući sistemski disk. Takođe se može koristiti za potpuno šifrovanje spoljnog medija kao što je USB stik ili disk, kao što ćemo videti u ovom uputstvu.


Glavna prednost VeraCrypt-a u odnosu na vlasnička rešenja je ta što je potpuno otvorenog koda, što znači da njegov kod može biti verifikovan od strane bilo koga.


## Kako instalirati VeraCrypt?


Idite na [zvaničnu VeraCrypt veb stranicu](https://www.veracrypt.fr/en/Downloads.html) u kartici "*Downloads*".

![VeraCrypt](assets/notext/05.webp)

Preuzmite verziju koja odgovara vašem operativnom sistemu. Ako koristite Windows, izaberite "*EXE Installer*".

![VeraCrypt](assets/notext/06.webp)

Izaberite jezik za vaš Interface.

![VeraCrypt](assets/notext/07.webp)

Prihvatite uslove licence.

![VeraCrypt](assets/notext/08.webp)

Odaberite "*Install*".

![VeraCrypt](assets/notext/09.webp)

Na kraju, izaberite fasciklu u koju će softver biti instaliran, zatim kliknite na dugme "*Install*".

![VeraCrypt](assets/notext/10.webp)

Sačekajte da se instalacija završi.

![VeraCrypt](assets/notext/11.webp)

Instalacija je završena.

![VeraCrypt](assets/notext/12.webp)

Ako želite, možete donirati bitkoine kako biste podržali razvoj ovog alata otvorenog koda.

![VeraCrypt](assets/notext/13.webp)

## Kako enkriptovati uređaj za skladištenje pomoću VeraCrypt-a?


Po prvom pokretanju, stići ćete na ovaj Interface:

![VeraCrypt](assets/notext/14.webp)

Da biste šifrovali uređaj za skladištenje po vašem izboru, počnite tako što ćete ga povezati sa vašim računarom. Kao što ćete kasnije videti, proces kreiranja novog šifrovanog volumena na USB memoriji ili Hard disku će trajati mnogo duže ako uređaj već sadrži podatke koje ne želite da obrišete. Stoga, preporučujem korišćenje prazne USB memorije ili prethodno pražnjenje uređaja kako biste kreirali šifrovani volumen, kako biste uštedeli vreme.


Na VeraCrypt-u, kliknite na karticu "*Volumes*".

![VeraCrypt](assets/notext/15.webp)

Zatim na meniju "*Create New Volume...*".

![VeraCrypt](assets/notext/16.webp)

U novom prozoru koji se otvori, izaberite opciju "*Šifruj particiju/drajv koji nije sistemski*" i kliknite na "*Dalje*".

![VeraCrypt](assets/notext/17.webp)

Zatim ćete morati da izaberete između "*Standard VeraCrypt volume*" i "*Hidden VeraCrypt Volume*". Prva opcija kreira standardni enkriptovani volumen na vašem uređaju. Opcija "*Hidden VeraCrypt Volume*" omogućava kreiranje skrivenog volumena unutar standardnog VeraCrypt volumena. Ova metoda vam omogućava da negirate postojanje ovog skrivenog volumena u slučaju prinude. Na primer, ako vas neko fizički prisili da dešifrujete vaš uređaj, možete dešifrovati samo standardni deo da biste zadovoljili napadača, ali ne i otkriti skriveni deo. U mom primeru, zadržaću se na standardnom volumenu.

![VeraCrypt](assets/notext/18.webp)

Na sledećoj stranici, kliknite na dugme "*Select Device...*".

![VeraCrypt](assets/notext/19.webp)

Otvara se novi prozor gde možete izabrati particiju vašeg skladišnog uređaja sa liste diskova dostupnih na vašem računaru. Obično će particija koju želite da šifrujete biti navedena ispod linije sa naslovom "*Removable Disk N*". Nakon što izaberete odgovarajuću particiju, kliknite na dugme "*OK*".

![VeraCrypt](assets/notext/20.webp)

Izabrana podrška se pojavljuje u okviru. Sada možete kliknuti na dugme "*Next*". ![VeraCrypt](assets/notext/21.webp)

Zatim ćete morati da izaberete između opcija "*Create encrypted volume and format it*" ili "*Encrypt partition in place*". Kao što je ranije pomenuto, prva opcija će trajno obrisati sve podatke na vašem USB stiku ili Hard disku. Izaberite ovu opciju samo ako je vaš uređaj prazan; u suprotnom, izgubićete sve podatke koje sadrži. Ako želite da zadržite postojeće podatke, možete ih privremeno prebaciti na drugo mesto, izabrati "*Create encrypted volume and format it*" za brži proces koji briše sve, ili se odlučiti za "*Encrypt partition in place*". Ova poslednja opcija omogućava šifrovanje volumena bez brisanja već prisutnih podataka, ali će proces biti mnogo duži. Za ovaj primer, pošto je moj USB stik prazan, biram "*Create encrypted volume and format it*", opciju koja briše sve.

![VeraCrypt](assets/notext/22.webp)

Dalje, imaćete opciju da izaberete algoritam za enkripciju i funkciju Hash. Osim ako nemate specifične potrebe, savetujem vam da zadržite podrazumevane opcije. Kliknite na "*Next*" da nastavite.

![VeraCrypt](assets/notext/23.webp)

Proverite da je naznačena veličina za vaš volumen tačna, kako biste šifrovali ceo raspoloživi prostor na USB memoriji, a ne samo deo. Kada potvrdite, kliknite na "*Next*".

![VeraCrypt](assets/notext/24.webp)

U ovoj fazi, potrebno je da postavite lozinku za šifrovanje i dešifrovanje vašeg uređaja. Važno je odabrati jaku lozinku kako biste sprečili napadača da dešifruje vaš sadržaj koristeći brute force napade. Lozinka treba da bude nasumična, što duža, i da uključuje nekoliko tipova karaktera. Savetujem vam da se odlučite za nasumičnu lozinku od najmanje 20 karaktera, uključujući mala slova, velika slova, brojeve i simbole.


Takođe vam savetujem da sačuvate svoju lozinku u menadžeru lozinki. Ovo olakšava pristup i eliminiše rizik od zaboravljanja. Za naš specifičan slučaj, menadžer lozinki je poželjniji od papirnog medija. Naime, u slučaju provale, iako vaš uređaj za skladištenje može biti ukraden, lozinka u menadžeru ne može biti pronađena od strane napadača, što će sprečiti pristup podacima. Suprotno tome, ako je vaš menadžer lozinki kompromitovan, fizički pristup uređaju je i dalje neophodan da bi se iskoristila lozinka i pristupilo podacima.


Za više informacija o upravljanju lozinkama, savetujem vam da otkrijete ovaj drugi kompletan vodič:


https://planb.network/tutorials/computer-security/authentication/bitwarden-0532f569-fb00-4fad-acba-2fcb1bf05de9

Unesite svoju lozinku u 2 predviđena polja, zatim kliknite na "*Dalje*". ![VeraCrypt](assets/notext/25.webp)

VeraCrypt će vas zatim pitati da li planirate da skladištite fajlove veće od 4 GiB u šifrovanom volumenu. Ovo pitanje omogućava softveru da izabere najpogodniji fajl sistem. Generalno, koristi se FAT sistem jer je kompatibilan sa većinom operativnih sistema, ali nameće maksimalno ograničenje veličine fajla od 4 GiB. Ako trebate da upravljate većim fajlovima, možete se odlučiti za exFAT sistem.

![VeraCrypt](assets/notext/26.webp)

Dalje, doći ćete do stranice koja vam omogućava da generate nasumični ključ. Ovaj ključ je važan, jer će se koristiti za šifrovanje i dešifrovanje vaših podataka. Biće sačuvan u specifičnom delu vašeg medija, koji je sam po sebi zaštićen lozinkom koju ste prethodno postavili. Da bi se generate jak ključ za šifrovanje, VeraCrypt zahteva entropiju. Zato vas softver traži da pomerate miš nasumično preko prozora; ovi pokreti se zatim koriste za generate ključa. Nastavite da pomerate miš dok se merač entropije potpuno ne napuni. Zatim, kliknite na "*Format*" da biste započeli kreiranje šifrovanog volumena.

![VeraCrypt](assets/notext/27.webp)

Sačekajte dok se formatiranje ne završi. Ovo može potrajati dugo za velike količine.

![VeraCrypt](assets/notext/28.webp)

Tada ćete primiti potvrdu.

![VeraCrypt](assets/notext/29.webp)

## Kako koristiti enkriptovani disk sa VeraCrypt-om?


Za sada je vaš medij šifrovan i stoga ga ne možete otvoriti. Da biste ga dešifrovali, idite na VeraCrypt.

![VeraCrypt](assets/notext/30.webp)

Izaberite slovo drajva sa liste. Na primer, ja sam izabrao "*L:*".

![VeraCrypt](assets/notext/31.webp)

Kliknite na dugme "*Select Device...*".

![VeraCrypt](assets/notext/32.webp)

Sa liste svih diskova na vašem računaru, izaberite šifrovani volumen na vašem mediju, zatim kliknite na dugme "*OK*".

![VeraCrypt](assets/notext/33.webp)

Možete videti da je vaš volumen dobro odabran.

![VeraCrypt](assets/notext/34.webp)

Kliknite na dugme "*Mount*".

![VeraCrypt](assets/notext/35.webp)

Unesite lozinku izabranu tokom kreiranja volumena, zatim kliknite na "*OK*".

![VeraCrypt](assets/notext/36.webp)

Možete videti da je vaš volumen sada dešifrovan i dostupan na slovu drajva "*L:*".

![VeraCrypt](assets/notext/37.webp)

Da biste pristupili, otvorite istraživač datoteka i idite na drajv "*L:*" (ili drugo slovo u zavisnosti od onog koje ste izabrali u prethodnim koracima). ![VeraCrypt](assets/notext/38.webp)

Nakon što dodate svoje lične fajlove u medij, da biste ponovo enkriptovali volumen, jednostavno kliknite na dugme "*Dismount*".

![VeraCrypt](assets/notext/39.webp)

Vaš volumen se više ne pojavljuje pod slovom "*L:*". Tako je ponovo šifrovan.

![VeraCrypt](assets/notext/40.webp)

Sada možete ukloniti svoj medij za skladištenje.


Čestitamo, sada imate šifrovani medijum za sigurno čuvanje vaših ličnih podataka, čime imate kompletnu 3-2-1 strategiju pored kopije na vašem računaru i vašeg rešenja za skladištenje na mreži.


Ako želite podržati razvoj VeraCrypt-a, možete donirati bitcoine [na ovoj stranici](https://www.veracrypt.fr/en/Donation.html).