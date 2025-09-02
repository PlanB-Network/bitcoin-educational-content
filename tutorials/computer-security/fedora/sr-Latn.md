---
name: Fedora
description: Linux distribucija koja vam pruža besplatan, potpun i siguran radni prostor.
---


![cover](assets/cover.webp)





Fedora je besplatan, open-source operativni sistem zasnovan na Linuxu, pokrenut 2003. godine, razvijen od strane zajednice **Fedora Project** i podržan od strane **Red Hat Linux**. Poznat je po svojoj stabilnosti, dobrom performansu i jednostavnosti korišćenja, što ga čini odličnim izborom za početnike i napredne korisnike. Sistem radi na većini modernih procesorskih arhitektura, što ga čini jednostavnim za instalaciju na gotovo bilo koji računar. Fedora je takođe dostupna u nekoliko unapred konfigurisanih izdanja, nazvanih "Fedora Spins" ili "Fedora Editions", dizajniranih za specifične potrebe (video igre, astronomija, razvoj...).



## Fedora Linux arhitektura



Kao što ste ranije pročitali, Fedora je besplatan operativni sistem zasnovan na Linux kernelu. Linux kernel je deo operativnog sistema koji komunicira sa hardverom računara i upravlja sistemskim resursima kao što su memorija i procesorska snaga.



Fedora Linux uključuje razne softverske alate i aplikacije koje su potrebne za pokretanje operativnog sistema na vrhu Linux kernela. Modularna arhitektura Fedore znači da se uglavnom sastoji od kolekcije pojedinačnih komponenti koje se mogu lako dodati, ukloniti ili zameniti po potrebi. Ovo vam omogućava da oblikujete operativni sistem koristeći samo resurse koji su vam potrebni.



Fedora takođe uključuje radno okruženje, koje je Interface kroz koje korisnici obavljaju zadatke i pristupaju aplikacijama. Fedora-ino podrazumevano radno okruženje je GNOME, korisnički prijatno, lako za korišćenje i visoko prilagodljivo radno okruženje.



## Zašto odabrati Fedoru?



Među mnoštvom dostupnih Linux distribucija, Fedora se posebno ističe zbog:





- Modularnost**: Kompatibilan sa različitim arhitekturama procesora, Fedora se može instalirati na većinu računara, čak i na one sa slabijim performansama, savršeno se prilagođavajući vašim potrebama.





- Jednostavan, intuitivan Interface**: Fedora kombinuje moderan grafički Interface sa moćnim komandnim Interface, što ga čini jednostavnim za korišćenje za sve profile.





- Stabilnost kernela**: Na osnovu Red Hat-a, Fedora je poznata po pouzdanosti svojih ažuriranja, posebno ažuriranja kernela, koja se sprovode bez većih grešaka zahvaljujući besplatnim doprinosima velike zajednice.





- Brza, laka instalacija**: sa veličinom slike od samo 3 GB, instalacija je brza i laka, čak i na mašinama sa ograničenim resursima.



## Fedora izdanja



U zavisnosti od vašeg profila i upotrebe, Fedora nudi izdanja koja odgovaraju vašim potrebama. Uglavnom ćete pronaći:





- Fedora Workstation**: Idealna za ličnu i/ili profesionalnu upotrebu na vašim računarima, ova verzija dolazi instalirana sa generičkim alatima kao što su pregledači, kancelarijski paket (uređivači teksta) i softver za reprodukciju medija.





- Fedora Server**: Ovo izdanje je posvećeno upravljanju serverima. Fedora Server uključuje razne alate koji vam pomažu da implementirate i upravljate serverima prema vašim potrebama.





- Fedora CoreOS**: Želite li jednostavno pokretati i implementirati cloud aplikacije? Fedora CoreOS je izdanje koje vam daje alate za kreiranje i upravljanje slikama pomoću Docker-a i Kubernets-a, na primer.



U ovom vodiču, preuzećemo kontrolu nad Fedora Workstation izdanjem. Međutim, procesi opisani u nastavku su slični za ostala izdanja.



## Instalacija i konfiguracija Fedora Workstation



Instalacija Fedora Workstation zahteva sledeću hardversku konfiguraciju:




- USB ključ od najmanje **8 GB** za pokretanje operativnog sistema.
- Najmanje **40 GB slobodnog prostora** na Hard disku vašeg računara.
- 4 GB RAM** za glatko iskustvo.



### Preuzmi Fedora Workstation



Možete preuzeti izdanje [Fedora Workstation] (https://fedoraproject.org/fr/workstation/download) sa zvanične veb stranice Fedora projekta. Zatim odaberite verziju koja odgovara arhitekturi vašeg procesora (32-bit - 64-bit) i kliknite na ikonu **Download**.



![download](assets/fr/01.webp)



![telecharger](assets/fr/02.webp)


### Kreirajte USB ključ za pokretanje sistema



Da biste instalirali Fedoru, potrebno je da kreirate USB ključ za pokretanje koristeći softver kao što je [Balena Etcher](https://etcher.balena.io/).



![flashOs](assets/fr/03.webp)



![flash](assets/fr/04.webp)



Kada završite sa instalacijom Balena Etcher-a, otvorite aplikaciju i izaberite preuzetu Fedora Workspace ISO sliku. Izaberite vaš USB ključ kao odredišni medij i kliknite na dugme **Flash** da biste započeli kreiranje bootable ključa.



![boot](assets/fr/05.webp)


### Instaliranje Fedore



Kada završite sa pokretanjem USB ključa, isključite računar.


Uključite računar, zatim pristupite BIOS-u tokom pokretanja pritiskom na taster `F2`, `F12` ili `ESC`, u zavisnosti od vašeg računara.



U opcijama pokretanja, izaberite vaš USB ključ kao primarni uređaj za pokretanje. Potvrđivanjem ovog izbora, vaš računar će se ponovo pokrenuti i automatski pokrenuti Fedora instalacioni program** prisutan na USB ključu.



Kada se vaš računar pokrene sa USB memorije, pojavljuje se **GRUB ekran**.



U ovoj fazi, imate sledeće opcije:




- Testiraj medij**: Ova opcija vam omogućava da proverite integritet USB memorije i osigurate da su sve zavisnosti potrebne za ispravnu instalaciju prisutne. Ovo je opcioni korak, ali se preporučuje ako imate bilo kakve sumnje u vezi sa USB memorijom.



![install](assets/fr/06.webp)



![testing](assets/fr/07.webp)





- Pokreni Fedoru**: Ovo pokreće Fedoru u "live" režimu, bez instalacije.



Na Fedora desktopu (live mode), kliknite na **Install Fedora** (ili Install on Hard disk) da biste započeli proces instalacije. Možete odabrati da instalirate kasnije i testirate Fedoru bez potrebe za instalacijom.



![install-live](assets/fr/08.webp)



Prvi korak je odabir **jezika instalacije** i **rasporeda tastature** za Fedoru.



![language](assets/fr/10.webp)





- Odabir diska za instalaciju:



Izaberite Hard disk na koji želite da instalirate Fedoru.



Ako je disk prazan, Fedora će automatski koristiti sav raspoloživi prostor. U suprotnom, možete prilagoditi particionisanje (ručno ili automatski).



![disk](assets/fr/11.webp)





- Enkripcija:



U ovoj fazi, Fedora predlaže šifrovanje vašeg diska kako bi se dodao dodatni Layer nivo sigurnosti. Ovo osigurava da vaše podatke može čitati samo vaš Fedora sistem.



![chiffrement](assets/fr/12.webp)



Pre nego što pokrenete instalaciju, Fedora prikazuje rezime vaših izbora. Potvrdite i kliknite na dugme za instalaciju da biste započeli instalaciju Fedore.



![resume](assets/fr/13.webp)



Tokom instalacije, Fedora kopira fajlove i konfiguriše sistem. Kada završi, računar se automatski restartuje.



![installation](assets/fr/14.webp)



### Osnovna konfiguracija


Prilikom prve upotrebe, potrebno je da završite nekoliko podešavanja:




- Promenite jezik sistema ako je potrebno.



![language](assets/fr/15.webp)





- Izaberite raspored tastature koji odgovara vašim preferencijama.



![keyboard](assets/fr/16.webp)





- Izaberite svoju vremensku zonu tako što ćete upisati ime svog grada u traku za pretragu, a zatim kliknuti na odgovarajući predlog.



![timezone](assets/fr/17.webp)





 - Omogući ili onemogući pristup tvojoj lokaciji za aplikacije kojima je to potrebno, kao i automatsko slanje izveštaja o greškama.



![location](assets/fr/18.webp)





- Odlučite da li želite omogućiti spremišta softvera trećih strana.



![logs](assets/fr/19.webp)





- Unesite svoje puno ime i definišite korisničko ime za svoj nalog.



![name](assets/fr/20.webp)





- Kreirajte sigurnu lozinku za vašu sesiju: što dužu (minimum 20 karaktera), što nasumičniju i sa različitim karakterima (mala slova, velika slova, brojevi i simboli). Zapamtite da sačuvate vašu lozinku.



![mdp](assets/fr/21.webp)



Kada su svi ovi koraci završeni, pokrenite Fedoru i počnite je koristiti odmah, bez daljeg ponovnog pokretanja.



![welcome](assets/fr/22.webp)



![start](assets/fr/23.webp)



Kada je vaša instalacija završena, možete se posavetovati sa svojim Interface domom pomoću nekoliko unapred instaliranih alata.



![install-now](assets/fr/09.webp)



## Otkrijte osnovne zadatke



### Pregledanje interneta


Podrazumevani pregledač na Fedori je **Firefox**. Lako se koristi i pogodan je za većinu potreba.


Ako više volite drugi pregledač, možete ga instalirati iz **menadžera softvera** ili putem **terminala**.


### Obrada teksta


Fedora uključuje kancelarijski paket **LibreOffice** po podrazumevanoj postavci, koji nudi nekoliko korisnih alata:




- Pisac** za obradu teksta.
- Calc** za proračunske tabele.
- Impress** za kreiranje prezentacija.


## Instaliranje aplikacija


Da biste instalirali nove aplikacije, možete koristiti Fedora-in **menadžer softvera** (nazvan _Software_), koji čini instalaciju lakom i vizuelnom. Međutim, korišćenje **terminala** je često brže i preciznije.



Pre nego što instalirate bilo koji softver, uvek se setite da ažurirate **repozitorijume** kako biste bili sigurni da imate pristup najnovijim dostupnim verzijama.



Zatim koristite sledeću komandu da pokrenete instalaciju željene aplikacije:


sudo dnf install software_name`


## Ažuriranje vašeg operativnog sistema


Nakon instalacije, važno je ažurirati Fedoru kako biste iskoristili najnovije sigurnosne zakrpe i ažuriranja softvera.


### Opcija 1: Preko Interface grafike




- Otvorite Fedora **Settings**, zatim idite na odeljak **System**.
- Kliknite na **Ažuriranje softvera**.
- Počnite preuzimanje ažuriranja i sačekajte da se proces završi.



Možda će biti potrebno **ponovno pokretanje** nakon što se ažuriranja instaliraju.


### Opcija 2: Preko terminala




- Otvorite terminal i započnite ažuriranjem **repozitorijuma** kako biste bili sigurni da imate najnovije verzije:



```shell
sudo dnf check-update
```





- Zatim, ažurirajte sav instalirani softver sledećom komandom:



```shell
sudo dnf upgrade
```



Sada je vaš Fedora sistem ažuriran i spreman za korišćenje u svim vašim svakodnevnim zadacima. Otkrijte naš vodič o Linux Mint-u, još jednoj Linux distribuciji, i kako postaviti zdravo i sigurno okruženje za vaše Bitcoin transakcije.



https://planb.network/tutorials/computer-security/operating-system/linux-mint-da44852e-513f-4004-949a-8fde60c1bca5