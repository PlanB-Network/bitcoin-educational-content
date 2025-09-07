---
name: PureOS
description: Linux distribucija koja vam daje kontrolu nad vašim digitalnim životom.
---

![cover](assets/cover.webp)



Zaštita ličnih podataka u digitalnom dobu je glavni prioritet za svakog korisnika interneta. Kompanije, organizacije, pa čak i operativni sistemi su korisni izvori informacija za definisanje vašeg profila i načina života. Odabir pravog operativnog sistema je prvi korak u jačanju vaše online privatnosti. U ovom vodiču ćemo pogledati PureOS, Linux distribuciju fokusiranu na privatnost.



https://planb.network/tutorials/computer-security/operating-system/debian-d09a57ec-8372-40ca-bcff-499415209e1f

## Početak sa PureOS-om



PureOS je operativni sistem zasnovan na Debianu koji je razvio Purism. PureOS je pogodan kako za IT profesionalce, tako i za korisnike koji traže jednostavnu distribuciju koja je laka za korišćenje. Ono što ga čini jedinstvenim je to što je *Slobodan Softver* i fokusira se na zaštitu ličnih podataka svojih korisnika postavljanjem okvira zasnovanog na privatnosti, slobodi, sigurnosti i stabilnosti koje nudi Debian.



### Zašto izabrati PureOS?





- Jednostavan, intuitivan Interface**: GNOME nudi jasan Interface desktop, dizajniran da bude jednostavan za korišćenje, čak i za ljude koji nisu sigurni u radu sa komandnom linijom.





- Besplatno**: kao većina Linux distribucija, PureOS je potpuno besplatan za korišćenje. Međutim, dostupna je mesečna pretplata za podršku programerima.





- Sigurnost i stabilnost**: Arhitektura i način rada PureOS-a čine ga veoma sigurnom distribucijom, garantujući zaštitu podataka i stabilnost sistema.





- Dokumentacija i aktivna zajednica**: PureOS ima jasnu, pristupačnu dokumentaciju i posvećenu, odgovarajuću zajednicu, što olakšava rešavanje problema i učenje sistema korak po korak.



## Instalacija i konfiguracija



Instalacija i konfiguracija PureOS-a na vašem računaru zahtevaće sledeće minimalističke karakteristike:




- USB ključ od najmanje 8GB za flešovanje sistema.
- 4 GB RAM.
- 30 GB slobodnog prostora na vašem Hard disku.



Idite na [zvaničnu veb stranicu PureOS-a](https://pureos.net/) zatim preuzmite ISO sliku operativnog sistema prema arhitekturi vašeg računara.



Da biste pokrenuli instalaciju PureOS-a, potrebno je da napravite USB ključ za pokretanje koristeći softver za flešovanje kao što je [Balena Etcher](https://www.balena.io/etcher).



U tri jednostavna koraka, dobićete USB stik sa pokrenutim PureOS operativnim sistemom.





- Priključite USB ključ i pokrenite preuzeti Balena softver.
- Zatim odaberite PureOS ISO sliku
- Izaberite USB ključ kao izlazni uređaj, zatim kliknite na dugme **Flash** i sačekajte da se proces završi.



![0_01](assets/fr/01.webp)



Kada se USB ključ pokrene, ponovo pokrenite računar na kojem želite instalirati PureOS.



Kada se pokreće, pristupite BIOS-u pritiskom na taster `ESC`, `F9` ili `F11`, u zavisnosti od vašeg uređaja. Izaberite USB ključ kao uređaj za pokretanje, zatim pritisnite `ENTER` da potvrdite.



### Ekran za pokretanje



PureOS nudi nekoliko opcija za pokretanje svog operativnog sistema. Izaberite opciju **Testiraj ili instaliraj PureOS** da biste pokrenuli instalaciju operativnog sistema.



![0_02](assets/fr/02.webp)



Podesite jezik i raspored tastature koji želite da koristite na svom računaru.



![0_03](assets/fr/03.webp)



![0_04](assets/fr/04.webp)



Dozvoli ili odbij pristup tvojoj **geografskoj lokaciji** aplikacijama za personalizovane preporuke na osnovu tvoje oblasti.



![0_05](assets/fr/05.webp)



Možete se povezati sa svojim postojećim **NextCloud** nalogom kako biste preuzeli podatke povezane sa kancelarijskim paketom koji koristite na drugom sistemu.



![0_06](assets/fr/06.webp)



Uputstvo je obezbeđeno, ali možete zatvoriti prozor ako želite da preskočite ovaj korak.



![0_08](assets/fr/08.webp)



### Pokretanje instalacije



Kliknite na meni **Activities** i istražite aplikacije i alate koji su unapred instalirani na sistemu. Kliknite na **Install PureOS** da biste započeli instalaciju.



![0_09](assets/fr/09.webp)



Podesite jezik sistema i raspored tastature prema potrebi, zatim konfigurišite Hard režim particionisanja diska.



![0_10](assets/fr/10.webp)



![0_11](assets/fr/11.webp)



![0_12](assets/fr/12.webp)



![0_13](assets/fr/13.webp)



Imate dve opcije za particionisanje vašeg Hard diska:




- Obriši disk**: Za potpunu instalaciju PureOS-a, brišući sve prethodno postojeće podatke na vašem Hard disku.



![0_14](assets/fr/14.webp)





- Ručna particija** za kreiranje sopstvenih rezultata



⚠️ Kada ručno kreirate particije za vaš operativni sistem, obavezno dodelite najmanje 2 GB particiju za rad PureOS-a, a zatim još jednu particiju za podatke.



![0_15](assets/fr/15.webp)



Aktivirajte **šifrovanje diska** ako želite da zaštitite svoje podatke. Unesite jaku, složenu lozinku.



Povežite korisnika sa svojim operativnim sistemom definišući korisničko ime i alfanumeričku lozinku od najmanje 20 karaktera kako biste pojačali sigurnost svojih podataka.



![0_16](assets/fr/16.webp)



Pregledajte postavke koje ste napravili i izmenite ih ako je potrebno.



![0_17](assets/fr/17.webp)



Kliknite na **Install** zatim **Install Now** da potvrdite da je PureOS instaliran na vašem računaru.



![0_18](assets/fr/18.webp)



![0_19](assets/fr/19.webp)



Kada je instalacija završena, označite polje **Restartuj sada** da biste ponovo pokrenuli računar, zatim potvrdite:




- Jezik.
- Raspored tastature.
- Vaš NextCloud nalog (opciono).



![0_25](assets/fr/25.webp)



## Ažuriranja



Pre nego što počnete koristiti PureOS, važno je ažurirati vaš sistem. Ovo će vam omogućiti da iskoristite najnovije funkcije i sigurnosne zakrpe, i osigurati veću stabilnost.





- Ažuriranje putem Interface grafike**:


Otvorite aplikaciju **Software**, zatim idite na karticu **Updates**. Dostupna ažuriranja se automatski prikazuju. Kliknite na **Download**, zatim na **Install** kada se preuzimanje završi.





- Ažuriranje putem terminala**:


Otvorite terminal, zatim unesite sledeću komandu da ažurirate listu dostupnih paketa:



```shell
sudo apt update
```



Unesite svoju lozinku i potvrdite. Zatim instalirajte ažuriranja sa:



```shell
sudo apt full-upgrade
```



## PureOS za razvoj



Podrazumevano, PureOS ne uključuje sve alate potrebne za razvoj.


Možete ih brzo instalirati sledećom komandom:



```shell
sudo apt install build-essential git curl
```



Ovo će instalirati alate za kompilaciju **Git** i **Curl**, korisne u većini razvojnih okruženja.



## PureOS okruženje



PureOS se ističe svojim inovativnim pristupom pravoj konvergenciji: jedan operativni sistem osigurava glatko, besprekorno funkcionisanje na različitim uređajima, uključujući laptopove, tablete, mini-PC-je i pametne telefone.



Aplikacije PureOS-a su dizajnirane da budu adaptivne: automatski se prilagođavaju veličini ekrana i načinu unosa (dodir ili tastatura/miš). Na primer, GNOME Web pregledač dinamički prilagođava svoj Interface kako bi pružio optimalno iskustvo na mobilnim i desktop uređajima.



PureOS takođe uključuje kancelarijski paket **LibreOffice**, koji obuhvata:





- Writer**: kompletan program za obradu teksta za kreiranje i uređivanje dokumenata.
- Calc**: moćan program za proračunske tabele za upravljanje vašim podacima i proračunima.
- Impress**: alat za kreiranje profesionalnih prezentacija.



Ovaj besplatni paket vam omogućava da radite efikasno bez potrebe da se oslanjate na vlasnički softver.



PureOS nudi objedinjeno, sigurno i fleksibilno okruženje, zasnovano na 100% open source distribuciji koja garantuje potpunu kontrolu i strogo poštovanje privatnosti. Njegova prava konvergencija olakšava kreiranje aplikacija kompatibilnih sa različitim tipovima uređaja, kao što su računari, tableti i pametni telefoni, bez potrebe za složenim prilagođavanjima.



Sa pristupom osnovnim alatima, robusnim upraviteljima paketa i bogatim open-source ekosistemom, PureOS pojednostavljuje razvoj aplikacija, testiranje i implementaciju u sigurnom okruženju. Njegova stabilna arhitektura i Commitment za poverljivost čine ga pouzdanom platformom za različite namene, uključujući Blockchain razvoj, brzo prototipiranje ili proizvodna okruženja.



Otkrijte naš kurs o jačanju vaše sigurnosti i zaštiti vaše digitalne privatnosti.



https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1