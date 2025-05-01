---
term: BCH KOD
---

Klasa kodova za ispravljanje grešaka koja se koristi za detekciju i ispravljanje grešaka u nizu podataka. Drugim rečima, BCH kodovi za ispravljanje grešaka koriste se za pronalaženje i ispravljanje slučajnih grešaka u prenetim informacijama, kako bi se osiguralo da one stignu neoštećene na svoje odredište. Akronim "BCH" predstavlja inicijale imena pronalazača ovih kodova: Bose, Ray-Chaudhuri i Hocquenghem.


Ovaj alat se koristi u mnogim oblastima računarstva, uključujući SSD-ove, DVD-ove i QR kodove. Na primer, zahvaljujući ovim kodovima za ispravljanje grešaka, čak i ako je QR kod delimično pokriven, i dalje je moguće preuzeti informacije koje kodira.


Kao deo Bitcoin, BCH kodovi se koriste za kontrolni zbir u Bech32 i Bech32m (posle-SegWit) Address formatima. Oni predstavljaju bolji kompromis između veličine kontrolnog zbira i sposobnosti detekcije grešaka u poređenju sa jednostavnim Hash funkcijama koje su prethodno korišćene na Legacy adresama. U kontekstu Bitcoin, BCH kodovi se koriste samo za detekciju grešaka, ne za ispravljanje grešaka. Dakle, Bitcoin softver za portfelj će identifikovati i prijaviti korisniku sve greške u primanju Address, ali neće automatski menjati netačan Address. Ovaj izbor je motivisan činjenicom da integracija ispravljanja grešaka neizbežno utiče na sposobnosti algoritma za detekciju grešaka.