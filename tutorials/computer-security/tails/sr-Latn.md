---
name: Repovi

description: Instalirajte Tails na USB ključ
---

![image](assets/cover.webp)


Prijenosan i amnezijski operativni sistem koji vas štiti od nadzora i cenzure.


## Zašto imati USB ključ sa instaliranim Tails-om?


Tails (https://tails.boum.org/) je najlakši način da uvek imate siguran računar na raspolaganju, koji neće ostaviti nikakav trag na računaru koji koristite.


Da biste koristili Tails, isključite računar kojem imate pristup (kod roditelja, prijatelja, u Internet kafeu...) i pokrenite ga sa vašim Tails USB ključem umesto Windows-a, macOS-a ili Linux-a.


Nakon toga, imaćete radni prostor i komunikaciono okruženje koje je nezavisno od uobičajenog operativnog sistema i nikada ne koristi Hard disk.


Tails nikada ne piše na Hard disk i koristi samo RAM računara za funkcionisanje. Ova memorija se potpuno briše kada se Tails isključi, čime se uklanjaju svi mogući tragovi.


## Neki konkretni slučajevi upotrebe


Da bismo vam dali konkretne ideje o prednostima stalnog posedovanja USB ključa sa Tails-om, ovde je mala neiscrpna lista koju je sastavio tim Agora256:



- Povežite se na Internet i Tor na necenzurisan i anoniman način kako biste pregledali veb stranice bez ostavljanja tragova;
- Otvorite PDF sa sumnjivog sajta;
- Testirajte vašu Bitcoin privatnu kopiju ključa sa Electrum Wallet;
- Koristite kancelarijski paket (LibreOffice) i radite na računaru koji ne pripada vama;
- Napravi svoje prve korake u Linux okruženju da naučiš kako napustiti svet Microsofta i Apple-a.


## Kako verovati Tails-u?


U korišćenju softvera uvek postoji element poverenja, ali ono ne mora biti slepo. Alat kao što je Tails mora težiti da svojim korisnicima pruži sredstva da bude pouzdan. Za Tails, ovo znači:



- Javni izvorni kod: https://gitlab.tails.boum.org/;
- Projekat zasnovan na uglednim projektima: Tor i Debian;
- Verifikabilna i reproduktivna preuzimanja;
- Preporuke različitih pojedinaca i organizacija.


## Vodič za instalaciju i korišćenje


Svrha ovog vodiča za instalaciju je da vas vodi kroz svaki korak instalacije. Nećemo opisivati radnje koje treba preduzeti više od zvaničnog vodiča, ali ćemo vas usmeriti u pravom smeru dok vam dajemo savete i trikove.


Iz praktičnih razloga, ovi saveti će biti fokusirani na macOS i Linux platforme.

🛠️

Pre nego što započnete ovu proceduru, molimo vas da se uverite da imate USB ključ sa minimalnom brzinom čitanja od 150 MB/s i kapacitetom od najmanje 8 GB, idealno USB 3.0.


Preduslovi:



- 1 USB ključ, samo za Tails, kapaciteta najmanje 8 GB
- Računar povezan na Internet sa Linux, macOS, (ili Windows)
- Otprilike jedan sat slobodnog vremena, u zavisnosti od brzine vaše internet veze, uključujući ½ sata za instalaciju (datoteka od 1,3 GB za preuzimanje)


## Korak 1: Preuzmite Tails sa svog računara


![image](assets/1.webp)


🔗 **Official Tails section:** https://tails.boum.org/install/linux/index.fr.html#download


Preuzimanje instalacione datoteke sa ekstenzijom .img može potrajati u zavisnosti od brzine vašeg internet preuzimanja, pa planirajte unapred. Sa modernom i efikasnom vezom, trajaće manje od 5 minuta.


Sačuvajte datoteku u poznatom folderu, kao što je Preuzimanja, jer će to biti potrebno za sledeći korak.


## Korak 2: Verifikujte vaše preuzimanje


![image](assets/2.webp)


🔗 **Official Tails section:** https://tails.boum.org/install/linux/index.fr.html#verify


Provera preuzimanja osigurava da ga izdaju Tails programeri i da nije oštećeno ili presretnuto tokom preuzimanja.


Moguće je ručno verifikovati da je datoteka koju ste upravo preuzeli ona očekivana koristeći PGP, ali bez naprednog znanja, ova verifikacija nudi isti nivo sigurnosti kao JavaScript verifikacija na stranici za preuzimanje, dok je mnogo komplikovanija i sklona greškama.


Da biste verifikovali datoteku, koristite dugme "Odaberite vaše preuzimanje..." koje se nalazi u zvaničnom delu!


## Korak 3: Instalirajte Tails na vaš USB ključ


![image](assets/3.webp)


🔗 **Zvanični Tails odeljak:**



- Linux:** https://tails.boum.org/install/linux/index.fr.html#install
- macOS:** https://tails.boum.org/install/mac/index.fr.html#etcher i https://tails.boum.org/install/mac/index.fr.html#install


Ovaj korak instaliranja Tails-a na vaš USB ključ je najteži u celom vodiču, posebno ako to nikada ranije niste radili. Najvažnija stvar je da odaberete ispravan postupak u zvaničnom odeljku za vaš operativni sistem: Linux ili macOS.


Kada su alati instalirani i pripremljeni prema preporukama, fajl sa ekstenzijom .img može biti kopiran na vaš ključ (brišući sve postojeće podatke) kako bi postao "bootabilan" nezavisno.


Srećno! i vidimo se na koraku 4.


## Korak 4: Ponovo pokrenite na vašem Tails USB ključu


![image](assets/4.webp)


🔗 **Official Tails section:** https://tails.boum.org/install/linux/index.en.html#restart


Vreme je da pokrenete jedan od vaših računara koristeći vaš novi USB stik. Ubacite ga u jedan od USB portova i restartujte!


**Napomena💡: Većina računara ne pokreće automatski sa Tails USB-a, ali možete pritisnuti taster za boot meni da prikažete listu mogućih uređaja za pokretanje.**


Da biste utvrdili koji taster treba da pritisnete kako biste osigurali da imate meni za pokretanje koji vam omogućava da izaberete USB stik umesto vašeg uobičajenog Hard drajva, ovde je neiscrpna lista po proizvođaču:


| Manufacturer | Key              |
| ------------ | ---------------- |
| Acer         | F12, F9, F2, Esc |
| Apple        | Option           |
| Asus         | Esc              |
| Clevo        | F7               |
| Dell         | F12              |
| Fujitsu      | F12, Esc         |
| HP           | F9               |
| Huawei       | F12              |
| Intel        | F10              |
| Lenovo       | F12              |
| MSI          | F11              |
| Samsung      | Esc, F12, F2     |
| Sony         | F11, Esc, F10    |
| Toshiba      | F12              |
| others...    | F12, Esc         |

Jednom kada je USB stik odabran, trebalo bi da vidite ovaj novi ekran za pokretanje, što je vrlo dobar znak, pa pustite računar da nastavi sa pokretanjem...


![image](assets/5.webp)


## Korak 5: Dobrodošli u Tails!


![image](assets/6.webp)


🔗 **Zvanična Tails sekcija:** https://tails.boum.org/install/linux/index.en.html#tails


Jedan ili dva minuta nakon boot loader-a i ekrana za učitavanje, pojavljuje se ekran dobrodošlice.


![image](assets/7.webp)


Na ekranu dobrodošlice, izaberite svoj jezik i raspored tastature u odeljku Jezik i region. Kliknite na Start Tails.


![image](assets/8.webp)


Ako vaš računar nije povezan sa mrežom, molimo vas da pogledate zvanična Tails uputstva kako biste se povezali na mrežu bez Wi-Fi-ja (odeljak "Testiraj svoj Wi-Fi").


Kada se povežete na lokalnu mrežu, pojavljuje se čarobnjak za Tor povezivanje koji vam pomaže da se povežete na Tor mrežu.


![image](assets/9.webp)


Možete početi da pretražujete anonimno, istražite opcije i softver uključen u Tails. Uživajte, imate dovoljno prostora za greške, jer ništa nije izmenjeno na USB sticku... Vaše sledeće restartovanje će zaboraviti sva vaša iskustva!


## U budućem vodiču...


Kada budete još malo eksperimentisali sa svojim Tails USB stikom, istražićemo druge naprednije teme u drugom članku, kao što su:



- Ažurirajte ključ sa **najnovijom verzijom Tails-a**;
- Konfigurišite i koristite **persistent storage**;
- Instaliraj **dodatni softver**.


Do tada, kao i uvek, ako imate bilo kakva pitanja, slobodno ih podelite sa zajednicom Agora256. Učimo zajedno da sutra budemo bolji nego što smo danas!