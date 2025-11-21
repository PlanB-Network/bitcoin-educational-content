---
term: PROVERA ZBIRA
---

Kontrolni zbir je vrednost izračunata iz skupa podataka, koja se koristi za proveru integriteta i validnosti tih podataka tokom prenosa ili skladištenja. Algoritmi za kontrolni zbir su dizajnirani da otkriju slučajne greške ili nenamerne izmene podataka, kao što su greške u prenosu ili oštećenje datoteka. Postoje različite vrste algoritama za kontrolni zbir, kao što su paritetne provere, modularni kontrolni zbir, kriptografske Hash funkcije ili BCH (*Bose, Ray-Chaudhuri i Hocquenghem*) kodovi.


Na Bitcoin, kontrolni zbirovi se koriste na nivou aplikacije kako bi se osigurala integritet primajućih adresa. Kontrolni zbir se izračunava iz korisnikovog Address sadržaja, a zatim se dodaje tom Address kako bi se otkrile greške u unosu. Kontrolni zbir je takođe prisutan u frazama za oporavak (mnemonici).


> ► *Opšte je prihvaćeno koristiti engleski termin "checksum" direktno u francuskom.*