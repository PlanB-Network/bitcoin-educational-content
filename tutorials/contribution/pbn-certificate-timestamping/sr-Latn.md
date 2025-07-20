---
name: Vremensko označavanje Plan ₿ Network sertifikata i diploma
description: Razumite kako Plan ₿ Network izdaje proverljive dokaze za vaše sertifikate i diplome
---

![cover](assets/cover.webp)


Ako čitate ovo, postoji velika verovatnoća da ste dobili ili ₿-CERT test sertifikat ili diplomu o završenom jednom od kurseva koje ste pohađali na planb.network, pa čestitamo na ovom postignuću!


U ovom vodiču ćemo otkriti kako Plan ₿ Network izdaje verifikovane dokaze za vaš ₿-CERT test sertifikat ili bilo koju Diplomu u vezi sa Završetkom Kursa. Zatim ćemo u drugom delu opisati kako da proverite autentičnost ovih dokaza.


# Plan ₿ Network mehanizam dokazivanja


Na Plan ₿ Network, mi kriptografski potpisujemo sertifikate i diplome, i vremenski ih označavamo koristeći Timechain (tj. The Bitcoin Blockchain), kroz mehanizam dokaza koji se oslanja na dve kriptografske operacije:


1. GPG-potpis na tekstualnoj datoteci koja sintetizuje vaša dostignuća

2. Vremensko označavanje istog potpisanog fajla putem [opentimestamps](https://opentimestamps.org/).


Prva operacija omogućava vam da potvrdite izdavaoca sertifikata (ili diplome), dok vam druga operacija omogućava da proverite datum njegovog izdavanja.

Verujemo da nam ovaj jednostavan mehanizam dokazivanja omogućava izdavanje sertifikata i diploma sa nepobitnim dokazima koje svako može nezavisno da proveri.


![image](./assets/proof-mechanism.webp)


Zahvaljujući ovom mehanizmu dokazivanja, svaki pokušaj izmene čak i najmanjeg detalja vašeg sertifikata ili diplome rezultiraće potpuno drugačijim SHA-256 Hash potpisom datoteke, što će odmah otkriti bilo kakvo neovlašćeno menjanje, jer ni potpis ni Timestamp više neće biti važeći. Štaviše, ako neko pokuša zlonamerno da falsifikuje sertifikate ili diplome u ime Plan ₿ Network, jednostavna provera potpisa će otkriti prevaru.


## Kako funkcioniše GPG-potpis?


GPG potpis je generisan korišćenjem softvera otvorenog koda pod nazivom GNU Privacy Guard. Ovaj softver omogućava korisnicima da lako kreiraju privatne ključeve, potpisuju i verifikuju potpise, kao i da enkriptuju i dekriptuju fajlove. Za potrebe ovog tutorijala, važno je napomenuti da Plan ₿ Network koristi GPG za kreiranje svojih privatnih/javnih ključeva i za potpisivanje svih ₿-CERT Sertifikata i Diploma o Završetku Kursa.


S druge strane, ako neko želi da proveri autentičnost potpisane datoteke, može koristiti GPG za uvoz javnog ključa izdavača i njegovu verifikaciju.


Za one koji su radoznali i žele da saznaju više o ovom fantastičnom softveru, možete se obratiti ["The GNU Privacy Handbook"](https://www.gnupg.org/gph/en/manual/x135.html)


## Kako funkcioniše vremensko označavanje?


Bilo ko može koristiti OpenTimestamps za Timestamp datoteku i dobiti verifikovani dokaz o njenom postojanju. Drugim rečima, ne pruža dokaz o tome kada je datoteka kreirana, već dokaz da je datoteka postojala najkasnije u određenom trenutku.

OpenTimestamps pruža ovu uslugu besplatno koristeći visoko efikasan metod za čuvanje dokaza u Bitcoin Blockchain. Koristi algoritam SHA-256 Hash za kreiranje jedinstvenog identifikatora za vaš fajl, i konstruira Merkle Tree koristeći heševe fajlova koje su poslali drugi korisnici. Samo Hash strukture Merkle Tree je usidren u OP_RETURN transakciji, osiguravajući siguran i kompaktan način za verifikaciju postojanja fajla.

Kada ova transakcija uđe u blok, svako ko ima početni fajl i `.ots` fajl povezan sa njim može verifikovati autentičnost vremenskog žiga. U drugom delu tutorijala, videćemo kako da verifikujete vaš Bitcoin Sertifikat ili bilo koju Diplomu o Završetku Kursa putem terminala i putem grafičkog Interface na vebsajtu OpenTimestamps.


# Kako verifikovati Plan ₿ Network ₿-CERT sertifikat ili diplomu


## Korak 1. Preuzmite svoj Sertifikat ili Diplomu


Prijavite se na svoju ličnu/studentsku kontrolnu tablu na planb.network.


![image](./assets/login.webp)


Idite na "Credentials" klikom na meni sa leve strane i izaberite svoju ispitnu sesiju ili svoju Diplomu.


![image](./assets/credential.webp)


Preuzmi zip datoteku.


![image](./assets/download.webp)


Izdvojite sadržaj desnim klikom na `.zip` datoteku i odabirom opcije "Extract". Naći ćete tri različite datoteke:



- Potpisana tekstualna datoteka (npr. certificate.txt)
- Otvorite Timestamp (OTS) datoteku (npr. certificate.txt.ots)
- PDF sertifikat (npr. certificate.pdf)


## Korak 2: Kako možete verifikovati potpis tekstualne datoteke?


Prvo, idite u folder gde ste raspakovali fajlove i otvorite terminal (desni klik na prozor foldera i kliknite na "Open in Terminal"). Zatim, pratite instrukcije ispod.


1. Uvezite Plan ₿ Network javni PGP ključ sledećom komandom:


```bash
curl -s https://raw.githubusercontent.com/Asi0Flammeus/pgp-public-keys/master/planb-network-pk.asc | gpg --import
```


Trebalo bi da vidite poruku poput sledeće ako ste uspešno uvezli PGP ključ


```
gpg: key 8F12D0C63B1A606E: public key "PlanB Network (used for PBN platform) <admin@planb.network>" imported
gpg: Total number processed: 1
gpg:               imported: 1
```


NAPOMENA: ako vidite da je 1 ključ obrađen i 0 ključeva uvezeno, to verovatno znači da ste već prethodno uvezli isti ključ, što je sasvim u redu.


2. Verifikujte potpis sertifikata ili diplome koristeći sledeću komandu:


```bash
gpg --verify certificate.txt
```


Ova komanda treba da vam pokaže detalje o potpisu, uključujući:



- Ko je potpisao (Plan ₿ Network)
- Kada je potpisano
- Da li je potpis važeći ili ne


Ovo je primer rezultata:


```
gpg: Signature made lun 11 nov 2024, 00:39:04 CET
gpg:                using RSA key 5720CD577E7894C98DBD580E8F12D0C63B1A606E
gpg:                issuer "admin@planb.network"
gpg: Good signature from "PlanB Network (used for PBN platform) <admin@planb.network>" [unknown]
```


Ako vidite poruku poput "BAD signature", to znači da je datoteka bila izmenjena.


## Korak 3: Verifikacija Open Timestamp


### Verifying via a Graphical Interface


1. Posetite OpenTimestamps vebsajt: https://opentimestamps.org/

2. Kliknite na karticu "Stamp & Verify".

3. Prevucite i otpustite OTS datoteku (npr. `certificate.txt.ots`) u predviđeno područje.

4. Prevucite i ispustite datoteku sa vremenskom oznakom (npr. `certificate.txt`) u određeno područje.

5. Vebsajt će automatski verifikovati otvoreni Timestamp i prikazati rezultat.


Ako vidite poruku poput sledeće, Timestamp je važeći:


![cover](assets/opentimestamp_wegui_verified.webp)


### CLI Metoda


NAPOMENA: ovaj postupak **će zahtevati pokrenut lokalni Bitcoin čvor**


1. Instalirajte OpenTimestamps klijent iz zvaničnog [repozitorijuma](https://github.com/opentimestamps/opentimestamps-client) pokretanjem sledeće komande:


```
pip install opentimestamps-client
```


2. Idite do direktorijuma koji sadrži izdvojene datoteke sertifikata.


3. Pokrenite sledeću komandu da biste verifikovali otvoreni Timestamp:


```
ots verify certificate.txt.ots
```


Ova komanda će:



- Proveri Timestamp u odnosu na Bitcoin-ov Blockchain
- Pokaži vam tačno kada je datoteka vremenski označena
- Potvrdite autentičnost Timestamp


### Konačni rezultati


Verifikacija je uspešna ako su **obe** sledeće poruke prikazane:


1. GPG potpis je prijavljen kao **"Good signature from Plan ₿ Network"**

2. OpenTimestamps verifikacija pokazuje specifičan Bitcoin blok Timestamp i izveštava **"Uspeh! Bitcoin blok [blockheight] potvrđuje da su podaci postojali od [Timestamp]"**


Sada kada znate kako Plan ₿ Network izdaje verifikovane dokaze za bilo koji ₿-CERT sertifikat i diplomu, možete lako proveriti njihov integritet.