---
name: Voltz
description: Sve-u-jednom Lightning wallet za vaše poslovanje.
---

![cover](assets/cover.webp)



Ideja za Voltz platformu potekla je od grupe bitkoin entuzijasta koji su želeli da pruže sopstvenu bitkoin wallet uslugu. Rezultat je bila kompletna infrastruktura za prihvatanje bitkoina u maloprodaji. U ovom vodiču, vodimo vas kroz obilazak Voltz-a i mogućnosti integracije bitkoina koje platforma nudi.



## Početak sa Voltz



Osim što je skrbnički Lightning wallet koji vam omogućava slanje, primanje i svakodnevno plaćanje, Voltz je kompletna platforma koja pruža brojne ekstenzije za integraciju bitcoina kao prodajnog mesta ili tržišta u vašem poslovanju.



Idite na platformu [Voltz] (https://www.voltz.com/en) i kreirajte nalog klikom na dugme "Try now".



![voltz](assets/fr/01.webp)



![login](assets/fr/02.webp)



⚠️ Važno je postaviti jaku alfanumeričku lozinku kako biste povećali šanse protiv brute-force napada, i proveriti da ste zaista na zvaničnom Voltz sajtu pre nego što unesete svoje podatke za prijavu kako biste se zaštitili od phishinga.



Voltz interfejs je veoma sličan onom na LnBits platformi.



https://planb.academy/tutorials/business/others/lnbits-cdfe1e38-069a-4df9-a86b-ce01ef28f4c2

Voltz je zapravo izgrađen na LnBits serveru; pogledajte naš vodič da naučite kako da postavite sopstvene LnBits servere i izgradite svoja rešenja na njima.



https://planb.academy/tutorials/business/others/lnbits-server-6a406046-3cef-4a64-a82b-8d8f0f82a192

Platforma vam omogućava efikasno upravljanje višestrukim portfolijima. Podrazumevano, kada se prijavite, automatski imate Lightning portfolio. Međutim, možete dodati i druge portfolije.



![wallets](assets/fr/03.webp)



### Prenosivost



Voltz nije ograničen na veb interfejs: u odeljku **Mobilni pristup**, možete povezati svoj aktivni Voltz wallet sa aplikacijama kao što su Zeus ili Blue Wallet.



https://planb.academy/tutorials/wallet/mobile/zeus-embedded-c67fa8bb-9ff5-430d-beee-80919cac96b9

https://planb.academy/tutorials/wallet/mobile/blue-wallet-2f4093da-6d03-4f26-8378-b9351d0dbc90

Da biste to uradili, potrebno je da instalirate i aktivirate ekstenziju **LndHub** na platformi.



![lndhub](assets/fr/04.webp)



Izaberite svoj aktivni Voltz portfolio i, u zavisnosti od prava koja želite da dodelite, skenirajte odgovarajući QR kod.




- QR kod fakture vam omogućava samo da pročitate istoriju svog portfolija i generate nove fakture.
- Admin QR kod omogućava vam da pregledate istoriju, generate fakture i takođe platite Lightning fakture.



![qrs](assets/fr/05.webp)



U ovom vodiču povezujemo naš Voltz wallet sa aplikacijom Blue Wallet.



![connect](assets/fr/06.webp)



Kada je naš portfolio povezan, sve akcije koje se izvrše biće sinhronizovane između Blue Wallet i Voltz. Na primer, kada generate fakturu na Blue Wallet, takođe imate istoriju na Voltz.



![sync](assets/fr/07.webp)



U odeljku **Konfiguracija portfolija**, pronaći ćete minimalne parametre kao što su prilagođavanje imena portfolija i valuta u kojoj želite da primate svoje uplate.



![config](assets/fr/08.webp)



### Ekstenzije



Jedna od posebnih karakteristika Voltz platforme je njena modularnost, koja vam omogućava da aktivirate ekstenzije koje su vam potrebne. Lista ekstenzija može se pronaći u meniju **Extensions**.



![extensions](assets/fr/09.webp)



Među ovim ekstenzijama je TPoS, terminal za prodajno mesto koji možete koristiti za vođenje inventara i prikupljanje uplata od vaših kupaca.



![tpos](assets/fr/10.webp)



Sa terminalu prodajnog mesta, možete:




- Dobijte veb stranicu koju možete deliti sa svojim kupcima i partnerima;
- Upravljaj zalihama proizvoda;
- Generiši Lightning fakture;
- Gotovinska plaćanja putem Bolt kartica.



Ekstenzija je dostupna kao besplatna verzija i kao plaćena verzija za naprednije funkcije. Da biste kreirali POS terminal, kliknite na dugme **Open** ispod logotipa ekstenzije, zatim kliknite na **New POS**.



![new_tpos](assets/fr/11.webp)



Definišite naziv vaše prodajne tačke, zatim povežite vaš Voltz wallet sa vašim terminalom za prikupljanje uplata. Možete aktivirati napojnice označavanjem polja **Aktiviraj napojnice**. Takođe aktivirajte opciju štampanja faktura ako želite izdavati račune vašim kupcima (ova funkcionalnost je još u razvoju, pa može doći do kvarova).



Terminal prodajnog mesta takođe uključuje konfiguraciju poreza kada želite da primenite porez vaše zemlje direktno na vaše proizvode.



![tpos](assets/fr/12.webp)



Kada vaš POS terminal bude kreiran, možete dodati unapred konfigurisane proizvode i usluge kako biste osigurali glatko plaćanje i računovodstveno iskustvo za vas i vaše kupce.



![product](assets/fr/13.webp)



Kreirajte svoje proizvode definišući njihovo ime, dodajući sliku i postavljajući prodajnu cenu. Možete kategorizovati svoje proizvode radi lakšeg praćenja. Možete primeniti poreze direktno na određeni proizvod. Ako proizvod nema primenjen porez, porez konfigurisan u fazi kreiranja terminala za prodaju će se automatski primeniti.



![products](assets/fr/14.webp)



Možete automatski uvesti svoju listu proizvoda iz JSON formata klikom na dugme **Import/Export**.



![exports](assets/fr/15.webp)



Pristupite području za naplatu putem linka klikom na ikonu **New Tab**, ili podelite svoju POS platformu putem QR koda sa svojim kupcima klikom na ikonu **QR code**.



![lien](assets/fr/16.webp)



![qr](assets/fr/17.webp)



Vaši kupci mogu pregledati vaš katalog i izvršiti uplatu putem ovog interfejsa.



![pos](assets/fr/18.webp)



![chose](assets/fr/19.webp)



![pay](assets/fr/20.webp)



![checkout](assets/fr/21.webp)



U grupi dostupnih ekstenzija, takođe ćete pronaći alate kao što su ekstenzije **Invoice** i **Payment Link**, koje vam omogućavaju da generate fakture sa specifičnim proizvodima kako biste prikupili izolovane uplate bez prolaska kroz POS terminal.



## Pratite svoje uplate



U meniju **Payments**, Voltz vam pruža pregled uplata na vaše različite portfelje.


Možete pratiti svoje uplate pomoću :




- Status.
- Oznaka: na primer **TPOS** za plaćanja na prodajnom mestu i **lnhub** putem mobilne veze u Zeus i Blue Wallet novčanicima.
- Kolekcija portfolija.
- Ukupna dolazna i odlazna plaćanja.
- Dobro definisan period.



![payments](assets/fr/22.webp)



## Više opcija



Voltz je takođe infrastruktura na kojoj možete izgraditi sopstvena rešenja. U odeljku **Extensions** pronaći ćete vodič za razvoj sopstvenih ekstenzija unutar Voltz i LnBits ekosistema.



![build](assets/fr/23.webp)



U slučaju da želite razvijati rešenja van ekosistema, ali i dalje koristiti njihovu infrastrukturu, u odeljku **URL čvora** pronaći ćete API ključeve i informacije o dokumentaciji sa primerom šta možete uraditi sa ovim podacima.



Možete kreirati Lightning fakture iz svojih aplikacija koristeći svoj Voltz wallet, plaćati Lightning fakture, dekodirati i verifikovati fakture.



![keys](assets/fr/24.webp)



Sada imate dobro razumevanje Voltz-a. Ako vam se dopao ovaj vodič, sigurni smo da ćete naučiti više o najboljim metodama i alatima za integraciju bitcoina u vaše poslovanje uz naš kurs: Bitcoin za preduzeća.



https://planb.academy/courses/a804c4b6-9ff5-4a29-a530-7d2f5d04bb7a