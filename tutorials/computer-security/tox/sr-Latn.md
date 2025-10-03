---
name: Tox
description: Otvorite razgovore bez posrednika na decentralizovanom Tox protokolu
---
![cover](assets/cover.webp)



End-to-end enkripcija je usluga koju nude mnoge aplikacije za razmenu poruka kao što su WhatsApp i Telegram. Enkripcija ovde znači da pre nego što pošiljalac pošalje poruku, ona je osigurana kriptografskom bravom za koju samo primalac ima ključ. Danas ćemo otkriti potpuno decentralizovanu, end-to-end enkriptovanu aplikaciju za razmenu poruka, zasnovanu na principima sličnim Blockchain, kako bismo ponudili sigurnu, end-to-end enkriptovanu komunikaciju bez posrednika: Tox Chat.



| Application          | E2EE 1:1       | E2EE groupes   | Inscription anonyme | Licence client open-source | Licence serveur open-source | Serveur décentralisé | Année de création |
| -------------------- | -------------- | -------------- | ------------------- | -------------------------- | --------------------------- | -------------------- | ----------------- |
| WhatsApp             | ✅              | ✅              | ❌                   | ❌                          | ❌                           | ❌                    | 2009              |
| WeChat               | ❌              | ❌              | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Facebook Messenger   | ✅              | 🟡 (optionnel) | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Telegram             | 🟡 (optionnel) | ❌              | 🟡                  | ✅                          | ❌                           | ❌                    | 2013              |
| LINE                 | ✅              | ✅              | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Signal               | ✅              | ✅              | ❌                   | ✅                          | ✅                           | ❌                    | 2014              |
| Threema              | ✅              | ✅              | ✅                   | ✅                          | ❌                           | ❌                    | 2012              |
| Element (Matrix)     | ✅              | ✅              | ✅                   | ✅                          | ✅                           | 🟡 (fédéré)          | 2016              |
| Delta Chat           | ✅              | ✅              | ✅                   | ✅                          | N/A                         | 🟡 (via email)       | 2017              |
| Conversations (XMPP) | ✅              | ✅              | ✅                   | ✅                          | ✅                           | 🟡 (fédéré)          | 2014              |
| Session              | ✅              | ✅              | ✅                   | ✅                          | ✅                           | ✅                    | 2020              |
| SimpleX              | ✅              | ✅              | ✅                   | ✅                          | ✅                           | ✅                    | 2021              |
| Olvid                | ✅              | ✅              | ✅                   | ✅                          | ❌                           | 🟡(pas d'annuaire)   | 2019              |
| Keet                 | ✅              | ✅              | ✅                   | ❌                          | N/A                         | ✅                    | 2022              |
| Jami                 | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2005              |
| Briar                | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2018              |
| **Tox**              | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2013              |

*E2EE = Šifrovanje od kraja do kraja*



## Šta je Tox?



Tox je besplatan (open source), decentralizovan komunikacioni protokol koji koristi tehnologiju *Networking and Cryptography Library* (NaCl) plus kombinacije enkripcijskih algoritama kako bi osigurao bezbednost i poverljivost svojih korisnika. Tox vam omogućava da Exchange šaljete tekstualne poruke, obavljate audio i video pozive, delite fajlove i delite ekran sa prijateljima na siguran, decentralizovan način i bez posrednika.



Tehnologija koju koristi Tox protokol je slična peer-to-peer mrežama kao što su blokčeinovi, što pogoduje decentralizaciji infrastrukture protokola. Za razliku od društvenih mreža i aplikacija za end-to-end enkriptovano dopisivanje, Tox Chat aplikacija je izgrađena na decentralizovanom protokolu koji nema centralni server. Svi korisnici komuniciraju u mreži peer-to-peer koja je otporna na cenzuru i bez posrednika. Za komunikaciju, svaki korisnik je identifikovan jedinstvenim ID-jem (ToxID) izvedenim iz njegovog ili njenog javnog ključa, koji je sačuvan u distribuiranoj Hash tabeli.



## Pridruži se Tox



Možete koristiti Tox protokol putem klijenta za instant poruke koji možete preuzeti sa [Tox Chat sajta](https://tox.chat).



![download](assets/fr/01.webp)



U zavisnosti od vašeg operativnog sistema, možete preuzeti i instalirati Tox klijent koji odgovara:





- aTox: [aTox](https://github.com/evilcorpltd/aTox), Tox klijent napisan u Kotlinu dostupan samo na Androidu



![aTox](assets/fr/02.webp)





- qTox: Tox klijent iz [open source](https://github.com/TokTok/qTox) zasnovan na Qt Framework-u (C++) dostupan na Windows, Linux, MacOs.



![qTox](assets/fr/03.webp)





- Toxic: [Toxic](https://github.com/JFreegman/toxic) je Tox klijent napisan u C jeziku koji radi na sistemima sa komandno-linijskim interfejsima.



![Toxic](assets/fr/04.webp)



U ovom vodiču, koristićemo qTox klijente na Windowsu i aTox za komunikaciju.



## Početak sa qTox



Jednom kada preuzmete, instalirajte svoj Tox klijent i kreirajte svoj profil.



![qTox-acount](assets/fr/05.webp)



Čestitamo, upravo ste se pridružili Tox protokolu. Na qTox softveru, možete pronaći informacije o svom profilu klikom na vaše korisničko ime.



![profil](assets/fr/06.webp)



Posebno ćete pronaći svoj Tox ID, koji možete sačuvati kao QR kod i podeliti sa ljudima koji žele da stupe u kontakt sa vama.



Izvezite svoju Tox profilnu datoteku kako biste imali rezervnu kopiju svog profila i kontakt informacija koje možete koristiti za obnavljanje. Kliknite na dugme **Izvezi**, zatim izaberite putanju do vaše rezervne datoteke.



![export](assets/fr/07.webp)



Iz menija **Više**, dodajte prijatelje, uvezite kontakte i upravljajte zahtevima za prijateljstvo koje primite.



![friends](assets/fr/08.webp)



Možete me kontaktirati putem ovog Tox ID-a na primer: EBC5604D9386E594CCC32943A03F96A96687FBD46788F1CD4F3337EB703C3C16BE3DC2CA6D9F



Kada je zahtev za prijateljstvo poslat, primalac će morati da prihvati ili odbije vaš zahtev pre nego što ih možete kontaktirati.



![request](assets/fr/09.webp)



Vaš Tox klijent uključuje sve opcije koje nude aplikacije za instant poruke:





- Video pozivi





- Pozivi glasom





- Deljenje fajlova





- emotikoni



![chat](assets/fr/10.webp)



### Grupe ravnopravnih članova



Vaši Tox klijenti takođe vam omogućavaju da komunicirate sa grupom ljudi na potpuno decentralizovan način: ovo se zove konferencije. U meniju **Grupe**, kreirajte novu konferenciju ili pogledajte listu pozivnica za pridruživanje konferencijama koje ste primili.



![conferences](assets/fr/11.webp)



Kada je konferencija kreirana, možete pozvati svoje prijatelje da se pridruže konferenciji na vašem Tox klijentu. U vašoj listi prijatelja, desnim klikom miša kliknite na korisničko ime prijatelja kojeg želite pozvati. Kliknite na opciju **Pozovi na konferenciju**, zatim izaberite ime konferencije koju ste kreirali. Takođe možete pozvati prijatelja implicitnim kreiranjem konferencije sa opcijom **Kreiraj novu konferenciju**.



⚠️ Tox klijenti su još uvek u razvoju, tako da možete naići na greške prilikom interakcije sa softverom. Funkcionalnosti za konferencije i video pozive još uvek nisu dostupne na Tox Android klijentu (aTox).



![invite](assets/fr/12.webp)



### Prenosi datoteka



U meniju **Prenosi datoteka**, pronaći ćete istoriju datoteka koje ste poslali i onih koje ste primili od svojih kontakata.



![files](assets/fr/13.webp)



Takođe možete prilagoditi konfiguracije deljenja fajlova za svaku diskusiju koju imate. Desnim klikom na korisničko ime primaoca izaberite "Prikaži više detalja".



![details](assets/fr/14.webp)



Iz detalja Interface, možete upravljati ovlašćenjima koja dajete primaocu za:





- Automatsko prihvatanje pozivnica za konferencije.





- Automatsko prihvatanje datoteka.





- Rezervne putanje za vaše diskusione fajlove.



![permissions](assets/fr/15.webp)



### Više parametara



U meniju **Settings** možete prilagoditi postavke svog Tox klijenta.





- U odeljku **General** promenite osnovni jezik vašeg Tox klijenta, definišite putanje za bekap fajlova i maksimalnu veličinu fajla koja će biti automatski prihvaćena.



![general](assets/fr/16.webp)





- U odeljku **Interface korisnik**, modifikujte fontove i veličine vaših poruka. Takođe možete promeniti temu vašeg Tox klijenta.



![ui](assets/fr/17.webp)





- Kartica **Privatnost** omogućava vam da definišete efemerne poruke tako što ćete poništiti izbor u polju "Zadrži istoriju ćaskanja". Takođe možete promeniti svoj Nospam kod kada primetite da vas spamuju zahtevima za prijateljstvo klikom na dugme "generate nasumični NoSpam kod".



![privacy](assets/fr/18.webp)



### Šta garantuje poverljivost na Tox-u?



Tox protokol koristi Distribuiranu Hash Tabelu za kreiranje mreže decentralizovanih čvorova. Svaki Tox klijent je deo DHT mreže i čuva informacije o drugim čvorovima. U slučaju Tox-a, DHT čuva IP adrese kao vrednosti povezane sa Tox javnim ključevima (Tox ID). Ovo omogućava lako pretraživanje Tox Klijent uređaja bez potrebe za upitom centralnog servera.



Zamislite da pišete našem korisniku `EBC5604D9386E594CCC32943A03F96A96687FBD46788F1CD4F3337EB703C16BE3DC2CA6D9F` kojeg ćemo nazvati **korisnik B**. Vaš Tox klijent će locirati ovaj identifikator u Hash distribuiranoj tabeli i pronaći povezanu IP adresu Address. Kada se IP Address pronađe, vaš Tox klijent će kreirati direktan, enkriptovan komunikacioni kanal sa mašinom našeg **korisnika B**, ili koristiti druge čvorove kao releje da dođe do **korisnika B**. Algoritmi za enkripciju osiguravaju da, bez obzira na komunikacioni kanal, samo **korisnik B** može pročitati sadržaj vaše poruke.



Ako ste uživali u otkrivanju Tox-a i uspeli da shvatite kako je koristan za jačanje vaše privatnosti, slobodno dajte ovom vodiču palac gore. Takođe preporučujemo naš vodič o Simple Login-u, alatu koji vam omogućava da anonimno primate i šaljete e-mailove.



https://planb.network/tutorials/computer-security/communication/simple-login-c17a10d6-8f84-4f97-8d50-7a83428d0f41