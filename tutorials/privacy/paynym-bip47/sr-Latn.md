---
name: BIP47 - PayNym
description: Koristite višekratni kod za plaćanje na Ashigaru
---
![cover](assets/cover.webp)



Najgora greška u privatnosti koju možete napraviti na Bitcoin je ponovno korišćenje adresa. Svaki put kada ista adresa primi nekoliko uplata, te transakcije se povezuju, pružajući svetu mapu vaših transakcija. Stoga se snažno preporučuje da uvek generate jedinstvenu adresu za svaki prijem. Ali za neke Bitcoin aplikacije, ovo nije jednostavna stvar.



BIP47, koji je predložio Justus Ranvier 2015. godine, pruža elegantno rešenje za ovaj problem. Uvodi koncept **ponovno upotrebljivog koda za plaćanje**: jedinstveni identifikator koji omogućava primanje praktično neograničenog broja onchain bitcoin uplata, bez ponovnog korišćenja adrese. Zahvaljujući kriptografskom mehanizmu zasnovanom na ECDH (*Diffie-Hellman na eliptičkim krivama*) razmeni, svaka uplata na isti kod rezultira praznom adresom, specifičnom za odnos između pošiljaoca i primaoca.



![Image](assets/fr/01.webp)



Ovaj BIP47 princip je posebno implementiran od strane **PayNym**, sistema koji je prvobitno razvio Samourai Wallet, a sada ga je preuzeo Ashigaru. U ovom vodiču ćemo pogledati kako da aktivirate vaš PayNym, razmenite kodove za plaćanje sa korespondentom i obavite transakcije bez ponovnog korišćenja adrese.



Neću ulaziti u detaljno funkcionisanje BIP47 ovde. Ako želite da se dublje upustite u ovu temu, molim vas da pogledate poglavlje 6.6 mog BTC 204 kursa obuke.



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Preduslovi



Da biste pratili ovaj vodič, sve što vam treba je wallet na Ashigaru aplikaciji. Ako ne znate kako da preuzmete, verifikujete, instalirate aplikaciju ili kreirate wallet, preporučujem da prvo pogledate ovaj vodič:



https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f

## Zahtevaj PayNym



Prvi korak je da preuzmete svoj PayNym. Ova operacija treba da se izvrši samo jednom po wallet. Ona povezuje vaš BIP47 kod plaćanja izveden iz vašeg seed (`PM...`) sa jedinstvenim identifikatorom specifičnim za PayNym implementaciju. Ovaj kraći, čitljiviji identifikator može se zatim preneti vašim korespondentima kako bi se olakšale razmene, bez potrebe da delite dugačak, kompletan BIP47 kod.



Da biste to uradili, kliknite na svoju PayNym sliku u gornjem levom delu interfejsa, a zatim na vaš kod za plaćanje `PM...`.



![Image](assets/fr/02.webp)



Zatim kliknite na tri male tačke u gornjem desnom uglu i odaberite `Claim PayNym`.



![Image](assets/fr/03.webp)



Potvrdite klikom na dugme `CLAIM YOUR PAYNYM`.



![Image](assets/fr/04.webp)



Osveži stranicu: tvoj PayNym ID je sada prikazan ispod tvoje slike, odmah iznad tvog BIP47 koda za plaćanje.



![Image](assets/fr/05.webp)



Vaš PayNym je sada aktivan i spreman za korišćenje za vaše prve BIP47 transakcije.



## Poveži se sa kontaktom



Postoje dve vrste veze između PayNym: **follow** i **connect**. Operacija `follow` je potpuno besplatna. Ona uspostavlja vezu između dva PayNym putem Soroban-a, Tor-baziranog enkriptovanog komunikacionog protokola koji je razvila Samourai ekipa i usvojila Ashigaru. Ova veza omogućava dvema korisnicima koji prate jedan drugog da razmenjuju informacije privatno, posebno za koordinaciju kolaborativnih transakcija kao što su Stowaway ili StonewallX2, koje ćemo razmotriti u drugom vodiču. Ovaj korak je specifičan za PayNym i nije deo BIP47 protokola.



![Image](assets/fr/06.webp)



Operacija povezivanja (`connect`), s druge strane, zahteva on-chain transakciju. Sastoji se u izvršavanju transakcije obaveštenja kako je definisano u BIP47. Ova Bitcoin transakcija sadrži metapodatke u `OP_RETURN` izlazu, koji uspostavlja šifrovani komunikacioni kanal između platioca i primaoca. Iz ovog kanala, platilac će moći da generate jedinstvene adrese za primanje za svaku uplatu, a primalac će biti obavešten o ovim uplatama i moći će da generate privatne ključeve povezane sa adresama kako bi kasnije potrošio ova sredstva.



Ova transakcija obaveštenja ima trošak: mining naknadu i 546 sats poslato na adresu obaveštenja primaoca kako bi se signalizovala veza. Kada je veza uspostavljena, gotovo beskonačan broj uplata može se izvršiti putem BIP47.



Ukratko:




- follow": besplatno, uspostavlja šifrovanu komunikaciju putem Sorobana, korisno za Ashigaruove alate za saradnju;
- `Connect`: naplativo, obavlja BIP47 transakciju obaveštenja za aktivaciju kanala između platioca i primaoca.



Da biste stupili u interakciju sa PayNym-om, prvo ga morate *pratiti*. Ovo je prvi korak pre uspostavljanja BIP47 veze. Recimo da želite da šaljete ponavljajuće uplate PayNym-u `+instinctiveoffer10`.



Idite na svoju PayNym stranicu na Ashigaru, zatim kliknite na dugme `+` u donjem desnom uglu interfejsa.



![Image](assets/fr/07.webp)



Zatim možete ili nalepiti pun kod za plaćanje primaoca, ili skenirati njihov QR kod.



![Image](assets/fr/08.webp)



Ako imate samo njegov PayNym ID, idite na [Paynym.rs](https://paynym.rs/) da pronađete QR kod povezan sa njegovim kodom za plaćanje.



![Image](assets/fr/09.webp)



Kada skenirate QR kod, kliknite na dugme `FOLLOW` da pratite PayNym.



![Image](assets/fr/10.webp)



Radnja `FOLLOW` je dovoljna za kolaborativne transakcije (*cahoots*). Međutim, za slanje BIP47 uplata, potrebno je uspostaviti vezu: kliknite na `CONNECT` da biste izvršili transakciju obaveštavanja.



![Image](assets/fr/11.webp)



Obaveštenje o transakciji se zatim emituje na mreži. Sačekajte dok ne dobije barem jednu potvrdu pre nego što izvršite svoju prvu uplatu.



![Image](assets/fr/12.webp)



## Napravite BIP47 uplatu



Sada ste povezani sa primaocem i možete poslati uplatu na jedinstvenu adresu, automatski generisanu korišćenjem BIP47 protokola, bez ikakve prethodne razmene sa primaocem.



Sa vaše glavne stranice PayNym, kliknite na kontakt kome želite poslati uplatu.



![Image](assets/fr/13.webp)



Na vrhu desno interfejsa, kliknite na ikonu strelice.



![Image](assets/fr/14.webp)



Unesite iznos koji želite poslati. Ne morate unositi adresu primatelja: ona će biti automatski izvedena korišćenjem BIP47 protokola.



![Image](assets/fr/15.webp)



Pažljivo proverite detalje transakcije, uključujući naknade, zatim prevucite zeleni strelicu na dnu ekrana da potpišete i emitujete transakciju.



![Image](assets/fr/16.webp)



Transakcija je poslata.



![Image](assets/fr/17.webp)



U ovom primeru, uplata je izvršena na još jedan od mojih PayNym novčanika. Stoga mogu videti da je stigla na moj drugi Ashigaru wallet, bez ikakve ručne razmene adresa: korišćen je samo PayNym identifikator.



![Image](assets/fr/18.webp)



Sada znate kako da koristite BIP47 višekratne kodove za plaćanje zahvaljujući PayNym implementaciji na Ashigaru aplikaciji. Sada možete podeliti ovaj kod za plaćanje sa bilo kim ko želi da vam pošalje uplate (posebno ponavljajuće uplate). Takođe možete objaviti svoj PayNym ID na vašem sajtu ili društvenim mrežama kako biste primali donacije.



Da biste produbili svoje znanje o ovom protokolu, detaljno razumeli kako funkcioniše i njegove implikacije na poverljivost, toplo preporučujem da pohađate moj kurs BTC 204:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c