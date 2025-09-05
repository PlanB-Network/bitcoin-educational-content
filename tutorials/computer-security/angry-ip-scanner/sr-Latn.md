---
name: Angry IP Scanner
description: Jednostavan način za skeniranje vaše mreže
---
![cover](assets/cover.webp)



___



*Ovaj vodič je zasnovan na originalnom sadržaju autora Florian BURNEL objavljenom na [IT-Connect](https://www.it-connect.fr/). Licenca [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Moguće je da su napravljene izmene u originalnom tekstu.*



___



## I. Prezentacija



Kako brzo i jednostavno skenirati Windows mrežu za povezane mašine? Odgovor je Angry IP Scanner. Ovaj open source projekat vam omogućava da lako skenirate mrežu, koristeći jednostavan grafički Interface.



Ovaj alat mogu koristiti pojedinci za **skeniranje svoje lokalne mreže**, ali i IT profesionalci za istu svrhu. Dokaz da je **ovaj alat veoma praktičan** je to što su ga već koristile **neke grupe sajber kriminalaca** za skeniranje korporativnih mreža (na isti način kao Nmap). Dobar primer je [ransomware grupa RansomHub](https://www.it-connect.fr/deja-210-victimes-pour-le-groupe-de-ransomware-ransomhub-lance-en-fevrier-2024/). I dalje je to dobar softver, ali kao i sa drugim alatima orijentisanim na mrežu i bezbednost, njegova upotreba može biti zloupotrebljena.



Ovde ćemo ga koristiti na **Windows 11**, ali je sasvim moguće koristiti ga na drugim verzijama **Windows**, kao i na **Linux** i **macOS**.



Manje sveobuhvatan od Nmap-a, **Angry IP** Scanner je i dalje zanimljiv za brzu, osnovnu analizu mreže, ali i zato što je dostupan svima. On će **detektovati hostove povezane na mrežu** i identifikovati **imena hostova** i **otvorene portove**.



Ako želite da idete dalje, pogledajte tutorijal o Nmap:



https://planb.network/tutorials/computer-security/communication/nmap-862300d7-6dfb-4660-970d-f56a9f58f60d

## II. Početak rada sa Angry IP Scanner



### A. Preuzmite i instalirajte Angry IP Scanner



Možete preuzeti najnoviju verziju Angry IP Scanner sa zvanične veb stranice aplikacije ili sa GitHub-a. Koristićemo drugu opciju. Kliknite na donji link i preuzmite EXE verziju: "**ipscan-3.9.1-setup.exe**".





- [Angry IP Scanner GitHub](https://github.com/angryip/ipscan/releases/latest)



![Image](assets/fr/016.webp)



Pokrenite izvršnu datoteku da biste nastavili sa instalacijom. Nema ničeg posebnog što treba uraditi tokom instalacije.



![Image](assets/fr/013.webp)



### B. Pokreni početno skeniranje mreže



Prilikom prvog pokretanja, odvojite vreme da pročitate uputstva u prozoru "**Početak rada**" kako biste saznali više o tome kako alat funkcioniše. Usput, postoji nekoliko pojmova koje treba razmotriti:





- Feeder**: modul odgovoran za generisanje lista IP adresa koje treba skenirati, iz nasumičnog IP opsega ili iz datoteke sa listom IP adresa.
- Fetcher**: skup modula za preuzimanje informacija o hostovima na mreži. Na primer, postoje fetcheri za detekciju MAC adresa, skeniranje portova, detekciju imena hostova ili slanje HTTP zahteva.



![Image](assets/fr/018.webp)



Da biste skenirali IP podmrežu, jednostavno unesite **početni IP Address** i **krajnji IP Address** u polje "**IP opseg**" (u suprotnom, promenite tip sa desne strane). Zatim kliknite na dugme "**Start**".



![Image](assets/fr/019.webp)



Nekoliko desetina sekundi kasnije, rezultat će biti vidljiv u softveru Interface. **Za svaki IP Address u analiziranom opsegu, videćete da li je Angry IP Scanner detektovao host ili ne.** Na ekranu će se takođe pojaviti rezime, koji pokazuje broj aktivnih hostova (u ovom slučaju 6) i broj hostova sa otvorenim portovima.



![Image](assets/fr/020.webp)



Ovde možemo videti prisustvo hosta pod nazivom "**OPNsense.local.domain**", povezanog sa IP Address "**192.168.10.1**" i dostupnog na **portovima 80** i **443** (HTTP i HTTPS). Desnim klikom na host pristupa se dodatnim komandama, kao što su pingovanje, praćenje rute i otvaranje pregledača putem ovog IP Address.



![Image](assets/fr/012.webp)



### C. Dodaj skeniranje portova



Podrazumevano, **Angry IP Scanner** će skenirati 3 porta: **80** (HTTP), **443** (HTTPS) i **8080**. Možete dodati više portova za skeniranje iz postavki aplikacije. Kliknite na meni "**Tools**", zatim na karticu "**Ports**".



Ovde možete izmeniti listu portova putem opcije "**Izbor porta**". Možete **navesti specifične brojeve portova odvojene zarezom, ili opsege portova**. Primer ispod dodaje dva porta: **445** (SMB) i **389** (LDAP). Da biste skenirali portove od 1 do 1000, unesite "**1-1000**". Nije navedeno da li se skeniranje portova vrši u TCP, UDP ili oba.



![Image](assets/fr/021.webp)



Ako ponovo pokrenete skeniranje, verovatno ćete dobiti nove informacije. U primeru ispod, Angry IP Scanner mi govori da su portovi 389 i 445 otvoreni na hostovima "**SRV-ADDS-01**" i "**SRV-ADDS-02**", zahvaljujući novoj konfiguraciji portova za skeniranje.



![Image](assets/fr/022.webp)



**Napomena**: iz menija "**Skeniranje**", možete izvesti rezultate skeniranja u tekstualnu datoteku.



Ako želite da nastavite sa skeniranjem, kliknite na meni "**Alati**", zatim kliknite na "**Fetcher-i**". Ovo dodaje "sposobnosti" skeniranju. Jednostavno izaberite fetcher i pomerite ga ulevo da ga aktivirate. Ovo će dodati dodatnu kolonu u rezultat skeniranja.



![Image](assets/fr/014.webp)



Primer ispod prikazuje funkcije "**NetBIOS info**" i "**Web detection**". Prva pruža dodatne informacije kao što su MAC Address mašine i ime domena, dok druga prikazuje naslov web stranice (što može dati neku indikaciju o tipu web servera ili aplikacije).



![Image](assets/fr/011.webp)



Konačno, iz preferenci, možete promeniti i metodu koja se koristi za "**ping**", tj. da razmotrite da li je host aktivan ili ne. Pošto neki hostovi ne odgovaraju na pingove, ovo vam omogućava da isprobate druge metode (UDP paket, TCP port probe, ARP, kombinacija UDP + TCP, itd.).



## III. Zaključak



Jednostavan i efikasan: Angry IP Scanner detektuje hostove povezane na mrežu i omogućava vam da konfigurišete skeniranje portova. Što se tiče opcija, nije tako fleksibilan kao Nmap i ne ide tako daleko, ali je dobar početak za brzo skeniranje.



Ako želite koristiti **Nmap** sa grafičkim Interface, možete koristiti **aplikaciju Zenmap** (pogledajte pregled ispod).



![Image](assets/fr/015.webp)



https://planb.network/tutorials/computer-security/communication/nmap-862300d7-6dfb-4660-970d-f56a9f58f60d