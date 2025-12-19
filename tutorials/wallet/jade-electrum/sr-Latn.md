---
name: Jade - Electrum
description: Kako koristiti svoj Jade ili Jade Plus sa Electrum (desktop)
---

![cover](assets/cover.webp)



_Ovaj vodič je preuzet iz [Bitcoin Workshops lekcije](https://officinebitcoin.it/lezioni/jadeele/index.html)_



Tutorijal je napravljen sa Jade Classic, ali su operacije takođe validne za one koji imaju Jade Plus.



Nakon inicijalizacije Jade-a, možete ga početi koristiti i--da biste to učinili--izaberite wallet displej.



Jade je uređaj koji se može koristiti sa nekoliko wallet, ili pratećih aplikacija kako ih Blockstream navodi na svojoj stranici.



U ovom vodiču ćete videti korake za korišćenje Electrum Wallet, putem USB kablovske veze.



## Prenos javnog ključa



Uzmite i uključite vaš inicijalizovani Jade. Čim ga uključite izgleda ovako:




![img](assets/en/32.webp)



Ako izaberete _Unlock Jade_, dobićete meni u kojem morate izabrati kako da povežete svoj uređaj sa pratećom aplikacijom.



Sa Electrum možete povezati Jade samo putem USB-a, pa izaberite ovaj metod.



Pokreni Electrum, koji će otvoriti predlaganje kao podrazumevanu opciju za otvaranje poslednjeg korišćenog wallet.



Ako prvi put povezujete Jade sa Electrum, izaberite _Create New Wallet_ i zatim _Finish_.



![img](assets/en/34.webp)



Ime wallet.



![img](assets/en/35.webp)



Odaberite Standard Wallet.



![img](assets/en/36.webp)



Kada birate keystore, neophodno je odabrati _Use a hardware device_.



![img](assets/en/37.webp)



Electrum počinje skeniranje za hardverskim uređajem.



![img](assets/en/38.webp)



Povezivanjem USB-a na računar (već povezan na USB C strani sa Jade), wallet hardver se pojavljuje u režimu zaključavanja. Jade se otključava unosom šestocifrenog PIN-a postavljenog tokom podešavanja.




![img](assets/en/39.webp)



Otključan hardverski uređaj, Electrum detektuje Jade. Nastavite klikom na _Next_.



![img](assets/en/40.webp)



U ovom trenutku Electrum traži da postavite skriptu politike: izaberite _Native Segwit_.



![img](assets/en/41.webp)



Faza prenosa javnog ključa sa wallet sa Jade na prikaz Electrum počinje.



Kada je izvoz javnog ključa završen, proces je gotov.



Watch-only je spreman i Electrum obaveštava o završetku sa sledećim ekranom.



![img](assets/en/42.webp)



wallet je zapravo kreiran i možete početi da ga istražujete: možete videti _adrese_, _informacije o novčaniku_, i-najvažnije-možete videti u donjem desnom uglu indikaciju da je to Blockstream-ov uređaj. Zelena tačka pored Blockstream logotipa pokazuje da je uređaj uključen i pravilno povezan na lokalnu mrežu.



![img](assets/en/43.webp)



## Primanje i trošenje transakcija



Iz menija _Receive_ na Electrum, generate uzmite `scriptPubKey` (adresu) za primanje sredstava. Uvek počnite sa malim iznosom i uradite test primanja+trošenja.



![img](assets/en/44.webp)



Nakon što primite satss, možete proveriti njihov dolazak u meniju _History_.



![img](assets/en/45.webp)



![img](assets/en/46.webp)



Kada je transakcija potvrđena, možete potrošiti ovaj UTXO i završiti test.



Trošak uključuje korišćenje Jade za potpisivanje.



Idite na meni _Send_ u Electrum, nalepite scriptPubKey i dobro ga proverite.



![img](assets/en/47.webp)



Kada završite, pritisnite _Plati_.



Prozor za transakcije se otvara, u kojem je važno postaviti ispravne naknade za transakcije. Kada završite sa svim podešavanjima, kliknite na _Pregled_ u donjem desnom uglu.



![img](assets/en/48.webp)



Prozor transakcije prikazuje neke važne detalje, pre svega status: `Nepotpisano`.



U ovoj fazi možete videti i komandu _Sign_, na koju morate kliknuti da biste dodali potpis sa Jade.



![img](assets/en/49.webp)



Sada počinje faza komunikacije između ekrana wallet i hardverskog uređaja, u kojoj vas Electrum upozorava da pratite uputstva na hardverskom uređaju, uključenom i spremnom za potpisivanje.



![img](assets/en/50.webp)



**Prvo, ipak, bolje je da proveriš šta potpisuješ: svi parametri transakcije koju si upravo postavio, takođe se pojavljuju na Jade** i možeš ih sve proveriti.



![img](assets/en/51.webp)



Da biste nastavili, uvek se pobrinite da postavite kursor na strelicu `→` koja vodi ka sledećim koracima i nikada na `X` osim ako želite da završite operaciju bez njenog završetka.



Deo za verifikaciju se završava prikazom naknade. U ovom trenutku potvrda je ekvivalentna stavljanju vašeg potpisa.



![img](assets/en/52.webp)



Na trenutak Jade obrađuje operaciju, kada je završena vraća se na početni meni.



![img](assets/en/53.webp)



Dok možete na Electrum videti status transakcije, koji je promenjen sa `Unsigned` na `Signed` i sada je moguće, za vas, da je propagirate klikom na _Broadcast_.



![img](assets/en/54.webp)



wallet, tako testiran, može se koristiti za primanje UTXO namenjenog za sigurno skladištenje.



![img](assets/en/55.webp)



Ovaj vodič je primer kako koristiti vaš Jade, povezan putem USB-a, sa wallet satom samo za čitanje. Electrum je klasičan primer, ali možda više volite drugi wallet softver. Jade izvozi javni ključ u mnoge druge novčanike: pronađite slične funkcije o kojima ste čitali u ovom uputstvu, kako biste se vodili i pronašli način da ga koristite u vašoj omiljenoj pratećoj aplikaciji.