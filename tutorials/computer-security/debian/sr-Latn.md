---
name: Debian
description: Linux distribucija poznata po svojoj stabilnosti, robusnosti i kompatibilnosti.
---

![cover](assets/cover.webp)



Debian je besplatna GNU/Linux distribucija, poznata po svojoj robusnosti i pouzdanosti. Njegovo Linux jezgro i svi paketi su rigorozno testirani kako bi se osigurala čvrsta stabilnost i visok nivo sigurnosti. Pogodan za servere i radne stanice, Debian nudi jednostavno korisničko iskustvo i ogroman katalog softvera. Bilo da tražite siguran sistem za svakodnevnu upotrebu ili proizvodno okruženje, Debian je pravi izbor.



## Zašto odabrati Debian?





- Besplatan i otvoren**: Debian je potpuno otvorenog koda, garantujući transparentnost i bez troškova licenci.
- Stabilnost i sigurnost**: svako izdanje prolazi kroz temeljni proces testiranja, čineći Debian jednom od najpouzdanijih i najsigurnijih distribucija na tržištu.
- Aktivna zajednica**: dostupna je velika zajednica i opsežna dokumentacija da vas podrži kad god vam zatreba.
- Lagan i skalabilan**: možete instalirati Debian na mašine sa skromnim resursima uz održavanje dobre performanse.
- Opsežan katalog softvera**: preko 50.000 zvaničnih paketa je dostupno putem repozitorijuma.



## Izaberite Interface grafiku



Debian nudi nekoliko radnih okruženja koja odgovaraju vašim potrebama:





- GNOME**: moderan, intuitivan Interface, idealan za početnike. Nudi fluidan, jednostavan grafički meni za pristup aplikacijama.
- XFCE**: lagan i brz, savršen za manje moćne mašine.
- KDE Plasma**: visoko prilagodljiv, sa izgledom sličnim Windows-u.
- Cinnamon**: jednostavan, elegantan Interface, inspirisan Windows-om.
- LXDE / LXQt**: ultra-lagani, pogodan za starije računare.
- MATE**: jednostavan i klasičan, blizak starom GNOME-u.



💡 Za udobno iskustvo koje se lako drži, **GNOME se toplo preporučuje**.



## Instaliranje i konfiguracija Debiana


### Hardverski zahtevi



Pre nego što započnete instalaciju, molimo vas da se uverite da imate sledeću opremu:





- USB ključ**: minimum 8 GB za smeštaj butabilne ISO slike.
- Random Access Memory (RAM)**: 4 GB za glatku instalaciju i rad.
- Prostor na disku**: najmanje 15 GB slobodnog prostora za sistem i ažuriranja.



### Preuzmi



Izbor Debian slike zavisi od arhitekture vašeg procesora:





- AMD64**: preuzmite izdanje "live hybrid" sa [download] liste (https://debian.obspm.fr/debian-cd/12.11.0-live/amd64/iso-hybrid/).
- ARM64**: preuzmite DVD sliku sa zvanične [Debian] veb stranice (https://debian.obspm.fr/debian-cd/12.11.0/arm64/iso-dvd/).
- Druge arhitekture**: pronađite ISO koji odgovara vašoj arhitekturi [ovde](https://debian.obspm.fr/debian-cd/12.11.0/).



![download](assets/fr/01.webp)



### Kreiranje USB ključa za pokretanje sistema



Kada preuzmete odgovarajuću ISO sliku, nastavite sa kreiranjem instalacionog medija:




- Preuzmite Balena Etcher** sa [zvaničnog sajta](https://etcher.balena.io/), zatim preuzmite binarni fajl za vaš sistem i instalirajte ga.



![etcher](assets/fr/02.webp)





- Pokreni Etcher**: otvori softver i izaberi prethodno preuzetu Debian ISO sliku.
- Izaberite USB ključ**: navedite vaš ključ (8 GB+) kao cilj.
- Pokreni flash**: klikni na **Flash!** i sačekaj dok se proces ne završi.



![flash](assets/fr/03.webp)



Vaš USB ključ je sada spreman za početak instalacije Debiana.



## Instaliranje Debiana na vaš sistem



### Pokretanje sa USB ključa



Da pokrenete instalaciju sa vašeg USB ključa:




- Isključite** računar potpuno.
- Ponovo pokreni** zatim pristupi BIOS/UEFI tako što ćeš odmah pritisnuti `ESC`, `F2`, `F11` (ili odgovarajući taster u zavisnosti od brenda).
- U meniju za pokretanje, **izaberite vaš USB ključ** kao uređaj za pokretanje.
- Potvrdite** tasterom Enter za pokretanje na Debian slici: ovo će vas odvesti do ekrana dobrodošlice instalatera.



### Pokretanje instalacije



Početni ekran:



![starting](assets/fr/04.webp)



Kada se pokreće sa USB memorije, Debian početni ekran nudi nekoliko opcija:




- Live System**: pokreće Debian bez instalacije, idealno za testiranje okruženja.
- Pokreni Instalater**: pokreće instalaciju direktno na Hard disk.
- Napredne opcije instalacije**: omogućava vam pristup prilagođenim režimima instalacije.



Da biste istražili Debian u live režimu, izaberite **Live System** i potvrdite sa **Enter**. Instalaciju možete pokrenuti klikom na **Install Debian** u live okruženju.



![system](assets/fr/05.webp)





- Izbor jezika** (opciono)



Izaberite glavni jezik vašeg Debian sistema sa liste, zatim kliknite na OK.



![language](assets/fr/06.webp)





- Vremenska zona** (GMT)



Izaberite svoju geografsku zonu da automatski postavite datum i vreme.



![timezone](assets/fr/07.webp)





- Raspored tastature



Izaberite jezik i raspored tastature. Koristite ugrađeno polje za testiranje kako biste proverili da li svaki taster proizvodi očekivani znak.



![keyboard](assets/fr/08.webp)



### Particionisanje diska





- Obriši disk**: ako imate posvećenu particiju, ova opcija će obrisati sav njen sadržaj.
- Ručno particionisanje**: izaberite ovu opciju da kreirate, promenite veličinu ili obrišete particije po potrebi.



![disk](assets/fr/09.webp)





- Kreiranje korisničkog naloga



Unesite svoje puno ime, ime naloga i jaku lozinku kako biste osigurali da je vaša sesija bezbedna.



![user](assets/fr/10.webp)





- Rezime parametara**



Prikaz izbora je prikazan: proverite svaku stavku i vratite se da izmenite ako je potrebno.



![settings](assets/fr/11.webp)





- Pokretanje instalacije



Kliknite na **Install** da biste započeli kopiranje fajlova i konfigurisanje sistema, zatim sačekajte da se proces završi.



![install](assets/fr/12.webp)





- Ponovno pokretanje**



Kada je instalacija završena, ponovo pokrenite računar da primenite sve konfiguracije i pristupite vašem novom Debian sistemu.



![restart](assets/fr/13.webp)



Pri pokretanju unesite korisničko ime i lozinku za pristup sistemu.



![login](assets/fr/14.webp)



## Ažuriranje sistema



Pre nego što počnete da koristite svoj sistem, neophodno je da ga ažurirate. Ovo vam omogućava da iskoristite najnovije softverske zakrpe, ažurirane repozitorijume, a u nekim slučajevima i sigurnosne zakrpe za sam operativni sistem.



### Opcija 1: Ažuriranje putem grafičkog Interface (GNOME)



Ako ste instalirali Debian sa GNOME radnim okruženjem, možete grafički izvršiti ažuriranja. Da biste to uradili, otvorite aplikaciju **Software**, zatim idite na karticu **Updates**. Zatim kliknite na **Restart and update** da biste započeli proces.



### Opcija 2: Ažuriranje putem terminala (preporučeno)



Ova metoda nudi potpuniju kontrolu. Omogućava vam ažuriranje repozitorijuma, softverskih paketa i, ako je potrebno, kernela.




- Otvorite terminal koristeći prečicu `Ctrl + Alt + T`.
- Ažurirajte listu dostupnih paketa sledećom komandom:



```shell
sudo apt update
```



Unesite svoju lozinku kada se to zatraži (imajte na umu da se prilikom kucanja neće prikazivati nikakvi znakovi - ovo je normalno).





- Da biste instalirali dostupna ažuriranja:



```shell
sudo apt full-upgrade
```



## Otkrijte osnovne zadatke



### Pregledanje interneta



Podrazumevani veb pregledač na Debianu je **Firefox**. Ako više volite drugi pregledač, možete instalirati drugi, pod uslovom da je dostupan u Debian repozitorijumima (kao što su Chromium, Brave...).



### Obrada teksta



**LibreOffice** paket je podrazumevano instaliran na Debianu.





- Da pišete dokumente, koristite **LibreOffice Writer**, ekvivalent Microsoft Word-a.
- Za proračunske tabele, **LibreOffice Calc** deluje kao alternativa Excelu.
- Konačno, **LibreOffice Impress** vam omogućava da kreirate prezentacije, baš kao PowerPoint.



## Instaliranje aplikacija



Postoje dva načina za instaliranje aplikacija na Debian:



### Grafički metod:



Možete koristiti **menadžer softvera** (dostupan putem grafičkog Interface) za lako pretraživanje i instalaciju aplikacija.



### Metod komandne linije:



Ako se aplikacija koju tražite ne pojavljuje u grafičkom Interface, ili ako više volite terminal, koristite sledeću komandu:



```shell
sudo apt install <name>
```



Zamenite `<name>` sa imenom paketa. Na primer, za instalaciju `curl`:



```shell
sudo apt install curl
```



### Instaliranje ručno preuzetog paketa:



Ako ste preuzeli `.deb` datoteku (Debian paket), možete je instalirati sledećom komandom:



```shell
sudo apt install ./name.deb
```



https://planb.network/tutorials/computer-security/operating-system/lynis-1cf865b3-a352-4dd2-94d2-f17fa65547af

Vaš Debian sistem je sada instaliran i spreman za korišćenje u vašim svakodnevnim zadacima.


Zahvaljujući radnom okruženju **GNOME**, možete pristupiti širokom spektru aplikacija putem korisnički prijatnog grafičkog Interface, idealnog za početnike i napredne korisnike.



Moguće je promeniti vaše desktop okruženje (npr. na XFCE, KDE, itd.) bez potrebe za ponovnom instalacijom Debiana. Da biste to uradili, jednostavno koristite terminal i instalirajte novo okruženje po vašem izboru.



Da biste saznali više o Debianu, i općenitije o GNU/Linux distribucijama, preporučujem da pogledate ovaj kurs:



https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1