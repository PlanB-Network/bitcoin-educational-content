---
name: Jade

description: Kako postaviti svoj JADE uređaj
---

![image](assets/cover.webp)


## Video tutorijal


![video](https://www.youtube.com/watch?v=_U1jsTeqbTw)

Blockstream Jade - Mobilni Bitcoin Hardware Wallet KOMPLETAN TUTORIJAL od BTCsession


## Kompletan vodič za pisanje


![image](assets/cover2.webp)


### Pre-requisites


1. Preuzmite najnoviju verziju Blockstream Green.


2. Instalirajte ovaj drajver kako biste osigurali da vaš računar prepoznaje Jade.


### Desktop Setup


![full guide](https://youtu.be/0fPVzsyL360)


Otvorite Blockstream Green, zatim kliknite na Blockstream logo ispod Uređaji.


![image](assets/1.webp)


Priključite Jade na vaš desktop koristeći priloženi USB kabl.


**Napomena:** Ako vaš računar ne prepoznaje Jade, proverite da li su instalirani potrebni drajveri, kao i da li problem može biti povezan sa USB dozvolama.


Kada se vaš Jade pojavi u Green, ažurirajte Jade klikom na Check for updates i odaberite najnoviju verziju firmvera. Koristite točkić za skrolovanje ili prekidač na Jade-u da potvrdite i nastavite sa ažuriranjem. Uverite se da vaš Jade i dalje prikazuje dugme "Initialize", inače ćete morati da sačekate nakon podešavanja Jade-a da biste ga nadogradili. Koristite dugme za povratak da biste se vratili na ovaj ekran ako je potrebno.


![image](assets/2.webp)


Nakon što ažurirate Jadeov firmver, izaberite Postavljanje Jade-a na mrežu i sigurnosnu politiku koju želite koristiti.


**Savet:** Bezbednosna politika je navedena pod Tip na ekranu za prijavu prikazanom ispod. Ako niste sigurni da li da izaberete Singlesig ili Multisig Shield, molimo vas da pregledate naš vodič [ovde](https://help.blockstream.com/hc/en-us/articles/4403642609433)


![image](assets/3.webp)


Zatim, odaberite da kreirate Novi Wallet i izaberite 12 reči za generate vašu frazu za oporavak. Klikom na Napredno dobićete opciju fraze za oporavak od 12 i 24 reči.


![image](assets/4.webp)


Zapišite frazu za oporavak van mreže na papir (ili korišćenjem posebnog uređaja za bekap fraze za oporavak radi dodatne sigurnosti). Zatim, koristite točkić ili prekidač na vrhu vašeg Jade uređaja da verifikujete vašu frazu za oporavak. Ovaj korak osigurava da ste je ispravno zapisali.


![image](assets/5.webp)


Postavite i potvrdite svoj šestocifreni PIN. Ovo se koristi za otključavanje Blockstream Jade svaki put kada se prijavite na svoj Wallet.


![image](assets/6.webp)


Sada jednostavno izaberite Go to Wallet na Green desktop aplikaciji i videćete vaš Wallet otvoren na Blockstream Green. Blockstream Jade će takođe pokazati da je Spreman! Sada možete koristiti vaš Jade za slanje i primanje Bitcoin transakcija.


![image](assets/7.webp)


Nakon što završite sa korišćenjem vašeg Wallet, isključite vaš Blockstream Jade sa uređaja. Sledeći put kada želite da koristite Wallet na Blockstream Jade, jednostavno ponovo povežite vaš uređaj i pratite uputstva.


izvor: https://help.blockstream.com/hc/en-us/articles/17478506300825


### Aneks A - Verifikacija datoteke preuzimanja Green Wallet


Proveravanje preuzimanja znači proveriti da datoteka koju ste preuzeli nije izmenjena od kada ju je objavio programer.


To radimo tako što proveravamo da li potpis (proizveden privatnim ključem programera) zajedno sa preuzetom datotekom i javnim ključem programera vraća rezultat TRUE kada prođe kroz gpg –verify funkciju. Pokazaću vam kako to da uradite sledeće.


Prvo, dobijamo ključ za potpisivanje:


Za Linux, otvorite terminal i pokrenite ovu komandu (trebalo bi samo da kopirate i nalepite tekst, uključujući navodnike):


```bash
gpg --keyserver keyserver.ubuntu.com --recv-keys "04BE BF2E 35A2 AF2F FDF1 FA5D E7F0 54AA 2E76 E792"
```


Za Mac, uradite isto, osim što ćete prvo morati preuzeti i instalirati GPG Suite.


Za Windows, uradite isto, osim što ćete prvo morati preuzeti i instalirati GPG4Win.


Dobićete izlaz koji kaže da je javni ključ uvezen.


![image](assets/9.webp)


Ova slika ima prazan alt atribut; ime njenog fajla je image-3-1024x162.webp


Dalje, treba da preuzmemo fajl koji sadrži Hash softvera. On je smešten na Blockstream-ovoj GitHub stranici. Prvo idite na njihovu info stranicu ovde, i kliknite na link za “desktop”. To će vas odvesti na stranicu sa najnovijim izdanjem na GitHub-u i tamo ćete videti link ka SHA256SUMS.asc fajlu, koji je tekstualni dokument koji sadrži Blockstream-ov objavljeni Hash programa koji smo preuzeli.


![image](assets/10.webp)


GitHub:


![image](assets/11.webp)


Nije neophodno, ali nakon čuvanja na disk, preimenovao sam “SHA256SUMS.asc” u “SHA256.txt” kako bih lakše otvorio datoteku na Mac-u koristeći uređivač teksta. Ovo je bio sadržaj datoteke:


![image](assets/12.webp)


Tekst koji tražimo nalazi se na vrhu. U zavisnosti od toga koji fajl smo preuzeli, postoji odgovarajući Hash izlaz koji ćemo kasnije upoređivati.


Donji deo dokumenta sadrži potpis napravljen na gornjoj poruci – to je dva u jednom fajlu.


Redosled nije bitan, ali pre nego što proverimo Hash, proverićemo da li je Hash poruka autentična (tj. da nije izmenjena).


Otvorite terminal. Treba da budete u ispravnom direktorijumu gde je preuzet fajl SHA256SUMS.asc. Ako ste ga preuzeli u direktorijum „Downloads“, za Linux i Mac promenite direktorijum ovako (osetljivo na velika i mala slova):


```bash
cd Downloads
```


Naravno, morate pritisnuti <enter> nakon ovih komandi. Za Windows, otvorite CMD (command prompt), i upišite isto (iako nije osetljivo na velika i mala slova).


Za Windows i Mac, trebalo je da već preuzmete GPG4Win i GPG Suite, respektivno, kako je ranije navedeno. Za Linux, gpg dolazi sa operativnim sistemom. Iz Terminala (ili CMD za Windows), ukucajte ovu komandu:


```bash
gpg --verify SHA256SUMS.asc
```


Tačno spelovanje imena fajla (u crvenom) može biti drugačije na dan kada preuzmete fajl, zato se uverite da komanda odgovara imenu fajla kako je preuzet. Trebalo bi da dobijete ovaj izlaz, i ignorišite upozorenje o pouzdanom potpisu – to samo znači da niste ručno rekli računaru da verujete javnom ključu koji smo ranije uvezli.


![image](assets/13.webp)


Ova slika ima prazan alt atribut; naziv datoteke je image-4-1024x165.webp


Ovaj izlaz potvrđuje da je potpis dobar, i sigurni smo da je privatni ključ “info@greenaddress.it” potpisao podatke (izveštaj Hash).


Sada bismo trebali Hash naš preuzeti zip fajl i uporediti izlaz kao što je objavljeno. Napomena da u fajlu SHA256SUMS.asc postoji deo teksta koji kaže "Hash: SHA512" što me zbunjuje, jer fajl očigledno ima SHA256 izlaze unutra, pa ću to ignorisati.


Za Mac i Linux, otvorite terminal, idite do mesta gde je zip fajl preuzet (verovatno ćete morati ponovo da ukucate “cd Downloads”, osim ako niste zatvorili terminal u međuvremenu). Usput, uvek možete proveriti u kom direktorijumu se nalazite tako što ćete ukucati PWD (“print working directory”), a ako vam je sve ovo strano, korisno je pogledati brz YouTube video pretragom “how to navigate the Linux/Mac/Windows file system”.


Da biste imali datoteku, upišite ovo:


```bash
shasum -a 256 BlockstreamGreen_MacOS_x86_64.zip
```


Trebalo bi da proveriš kako se tačno zove tvoj fajl i izmeniš tekst u plavoj boji iznad ako je potrebno.


Dobićete izlaz poput ovog (vaš će se razlikovati ako je datoteka drugačija od moje):


![image](assets/14.webp)


Zatim, vizuelno uporedite izlaz Hash sa onim što je u datoteci SHA256SUMS.asc. Ako se poklapaju, onda –> USPEH! Čestitamo.


izvor: https://armantheparman.com/jade/


### Koristeći ga na Sparrow


Ako već znate kako koristiti SParrow onda je kao i uvek:


**Napomena:** to je isti proces kao sa Specter-om na primer


Preuzmite Sparrow koristeći link koji je ovde dat.


![image](assets/14.5.webp)


Kliknite Next da biste pratili vodič za podešavanje i saznali više o različitim opcijama povezivanja.


![image](assets/15.webp)


Izaberite željeni server, a zatim odaberite Kreiraj novi Wallet.


![image](assets/16.webp)


Unesite ime za vaš Wallet i kliknite Kreiraj Wallet.


![image](assets/17.webp)


Izaberite željenu politiku i tipove skripti, a zatim odaberite Connected Hardware Wallet.


**Napomena:** Ako ste ranije koristili Blockstream Jade kao Singlesig Wallet sa Blockstream Green i želite da pregledate svoje transakcije u Sparrow, uverite se da tip skripte odgovara tipu naloga koji sadrži vaša sredstva u Green. Takođe će vam biti potreban odgovarajući put derivacije.


![image](assets/18.webp)


Priključite vaš Blockstream Jade i kliknite na Skeniraj. Zatim će vam biti zatraženo da unesete vaš PIN na Jade.


**Saveti:** Pre nego što povežete svoj Jade, uverite se da aplikacija Blockstream Green nije otvorena. Ako je Green otvoren, to može izazvati probleme sa detekcijom vašeg Jade uređaja unutar Sparrow.


![image](assets/19.webp)


Odaberite Importuj Keystore da uvezete javni ključ podrazumevanog naloga, ili odaberite strelicu da ručno izaberete put derivacije koji želite da koristite.


![image](assets/20.webp)


Nakon što je željeni ključ uvezen, kliknite na Primeni.


![image](assets/21.webp)


Sada ste uspešno postavili svoj Wallet i možete početi primati, skladištiti i trošiti svoj Bitcoin koristeći Sparrow i Blockstream Jade.


**Napomena:** Ako ste ranije koristili Jade sa Blockstream Green kao Multisig Shield Wallet, ne bi trebalo da očekujete da vaš novi Sparrow Wallet pokaže isti balans - ovo su različiti novčanici. Da biste ponovo pristupili svom Multisig Shield Wallet, jednostavno povežite svoj Jade nazad na Blockstream Green.


![image](assets/22.webp)


izvor: https://help.blockstream.com/hc/en-us/articles/7559912660761-How-do-I-use-Blockstream-Jade-with-Sparrow-


### Green aplikacija


ako ste više mobilni vodič, možete ga koristiti sa Blockstream Green



- Kako postaviti Blockstream Jade sa Green | Blockstream Jade - https://youtu.be/7aacxnc6DHg
- Kako primiti Bitcoin na Jade Wallet | Blockstream Jade - https://youtu.be/CVtcDdiPqLA