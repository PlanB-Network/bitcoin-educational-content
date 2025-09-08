---
name: Picocrypt
description: Alat otvorenog koda za šifrovanje vaših podataka
---
![cover](assets/cover.webp)



___



*Ovaj vodič je zasnovan na originalnom sadržaju Floriana BURNEL-a objavljenom na [IT-Connect](https://www.it-connect.fr/). Licenca [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Izmene su izvršene u originalnom sadržaju.*



___



## I. Prezentacija



U ovom vodiču ćemo pogledati Picocrypt, jednostavan, lagan i efikasan softver za šifrovanje podataka sa visokim nivoom sigurnosti.



Pogodan za **šifrovanje fajlova**, možete ga koristiti za zaštitu **podataka na vašem računaru, na USB memoriji**, ali i podataka pohranjenih u Cloud-u. Na primer, možete šifrovati podatke i pohraniti ih na **Microsoft OneDrive, Google Drive, iCloud ili Dropbox**, iako za ovu svrhu preferiram drugi softver koji će biti predstavljen u budućem članku.



Možete ga koristiti i kada trebate **podeliti podatke sa trećom stranom**: zahvaljujući Picocrypt-u i ključu za dešifrovanje, oni će moći da dešifruju podatke na svom računaru. Tako da, ako je vaš nalog ili računar kompromitovan, vaši podaci su zaštićeni.



Da biste pratili projekat Picocrypt, postoji samo jedan Address:





- [Picocrypt na GitHub-u](https://github.com/Picocrypt/Picocrypt)



Potpuno **besplatan i otvorenog koda**, PicoCrypt je dostupan za **Windows**, **Linux** i **macOS**. Na Windows-u, možete ga instalirati na svoj računar ili koristiti prenosivu verziju.



## II. Picocrypt, open source softver za šifrovanje



Picocrypt** softver za šifrovanje predstavlja se kao **alternativa** drugim poznatim rešenjima kao što su **VeraCrypt** i **Cryptomator** (*dizajniran za šifrovanje podataka u Cloud okruženjima*), ili **AxCrypt**. Usput, na zvaničnom GitHub-u Picocrypt-a možete pronaći poređenje sa nekim konkurentima:



|                | Picocrypt                                                                          | VeraCrypt   | 7-Zip GUI | BitLocker  | Cryptomator |
| -------------- | ---------------------------------------------------------------------------------- | ----------- | --------- | ---------- | ----------- |
| Free           | ✅ Yes                                                                              | ✅ Yes       | ✅ Yes     | ✅ Bundled  | ✅ Yes       |
| Open Source    | ✅ GPLv3                                                                            | ✅ Multi     | ✅ LGPL    | ❌ No       | ✅ GPLv3     |
| Cross-Platform | ✅ Yes                                                                              | ✅ Yes       | ❌ No      | ❌ No       | ✅ Yes       |
| Size           | ✅ 3 MiB                                                                            | ❌ 20 MiB    | ✅ 2 MiB   | ✅ N/A      | ❌ 50 MiB    |
| Portable       | ✅ Yes                                                                              | ✅ Yes       | ❌ No      | ✅ Yes      | ❌ No        |
| Permissions    | ✅ None                                                                             | ❌ Admin     | ❌ Admin   | ❌ Admin    | ❌ Admin     |
| Ease-Of-Use    | ✅ Easy                                                                             | ❌ Hard      | ✅ Easy    | ✅ Easy     | 🟧 Medium   |
| Cipher         | ✅ XChaCha20                                                                        | ✅ AES-256   | ✅ AES-256 | 🟧 AES-128 | ✅ AES-256   |
| Key Derivation | ✅ Argon2                                                                           | 🟧 PBKDF2   | ❌ SHA-256 | ❓ Unknown  | ✅ Scrypt    |
| Data Integrity | ✅ Always                                                                           | ❌ No        | ❌ No      | ❓ Unknown  | ✅ Always    |
| Deniability    | ✅ Supported                                                                        | ✅ Supported | ❌ No      | ❌ No       | ❌ No        |
| Reed-Solomon   | ✅ Yes                                                                              | ❌ No        | ❌ No      | ❌ No       | ❌ No        |
| Compression    | ✅ Yes                                                                              | ❌ No        | ✅ Yes     | ✅ Yes      | ❌ No        |
| Telemetry      | ✅ None                                                                             | ✅ None      | ✅ None    | ❓ Unknown  | ✅ None      |
| Audited        | ✅ [Yes](https://github.com/Picocrypt/storage/blob/main/Picocrypt.Audit.Report.pdf) | ✅ Yes       | ❌ No      | ❓ Unknown  | ✅ Yes       |

Izvor: [Github.com](https://github.com/Picocrypt/Picocrypt)



Picocrypt je **veoma lagan**, teži samo **3 MB**, i ne treba da se instalira: to je **prenosiva aplikacija** sa prednošću da ne zahteva administratorska prava! Međutim, ne zanemaruje bezbednost, jer se oslanja na **robustne i pouzdane algoritme**:





- XChaCha20** algoritam šifrovanja
- Funkcija zaobilaženja ključa **Argon2**



Pored gore pomenutih prednosti, ono što zaista privlači je **njegova jednostavnost korišćenja**!



Potrebna je samo jedna stvar: **revizija koda**, ali to je planirano, kao što možete videti iz tabele poređenja iznad (poslednji red). Ali pošto je otvorenog koda, ništa vas ne sprečava da pogledate njegov izvorni kod.



Iako je u tabeli iznad upoređen sa BitLocker-om, **po mom mišljenju BitLocker i Picocrypt su namenjeni za različite upotrebe**: BitLocker za šifrovanje kompletnog volumena (na primer, Windows-a) i Picocrypt za šifrovanje strukture stabla ili skladišnog prostora tipa "Drive".



## III. Korišćenje Picocrypt



Za ovu demonstraciju koristiće se mašina sa Windows 11.



### A. Šifrovanje podataka sa Picocrypt



Prvo, treba da preuzmete Picocrypt.exe sa zvaničnog GitHub-a ([pogledajte ovu stranicu](https://github.com/Picocrypt/Picocrypt/releases)).



Otvorite aplikaciju da prikažete njen minimalistički Interface na ekranu. Da biste šifrovali podatke, bilo da je to **datoteka, nekoliko datoteka ili fascikla**, jednostavno **prevucite i ispustite u Picocryptov Interface**. Ovo će odabrati podatke za šifrovanje.



![Image](assets/fr/020.webp)



Zatim, za šifrovanje podataka, imate pristup nekoliko opcija, uključujući šifrovni ključ. To može biti **jaka lozinka** ili **šifrovni ključ u obliku datoteke ključa**, ili **oboje**. Ako uzmemo primer lozinke, imate izbor između kreiranja sopstvene lozinke, ili generisanja lozinke sa Picocrypt-om.



Ova lozinka mora biti jaka, jer se može koristiti za dešifrovanje podataka. Unesite je pod "**Lozinka**" i "**Potvrdi lozinku**", zatim kliknite na "**Šifruj**" da šifrujete podatke! Pre toga, možete kliknuti na dugme "**Promeni**" pored "**Sačuvaj izlaz kao**" da biste odredili izlazni direktorijum.



**Napomena**: da biste koristili ključ u formatu datoteke, kliknite na "**Kreiraj**" desno od "**Ključne datoteke**" da biste kreirali ključ. Zatim ga odaberite klikom na "**Uredi**" i prevucite i otpustite datoteku ključa na odgovarajuće područje.



![Image](assets/fr/019.webp)



Dve izabrane datoteke su **šifrovane i grupisane zajedno** u datoteci "**Encrypted.zip.pcv**", pošto je **PCV** ekstenzija koju koristi Picocrypt. Ovaj ZIP fajl je nečitljiv zahvaljujući šifrovanju. Da biste sprečili da izabrane datoteke budu grupisane zajedno u jednoj šifrovanoj ZIP datoteci, potrebno je da označite opciju "**Recursively**", tako da ima onoliko šifrovanih datoteka koliko ima datoteka koje treba šifrovati.



Da bismo pristupili našim podacima, moramo ih dešifrovati koristeći Picocrypt.



![Image](assets/fr/023.webp)



Pre nego što razgovaramo o dešifrovanju podataka, evo nekih informacija o dostupnim opcijama:





- Paranoid mode**: koristite najviši nivo sigurnosti koji nudi Picocrypt. Alat će koristiti nekoliko kaskadnih algoritama za šifrovanje (XChaCha20 i Serpent) i HMAC-SHA3 umesto BLAKE2b za autentifikaciju podataka.
- Reed-Solomon**: implementirajte *Reed-Solomon* kodove za ispravljanje grešaka kako biste omogućili ispravljanje grešaka na oštećenim podacima. Ovo vam omogućava da podržite nivo oštećenja od oko 3% vašeg fajla.
- Podeli na delove** ili **razdeli na nekoliko delova**: ako šifrujete veliku datoteku, možete zatražiti od Picocrypt-a da je podeli na nekoliko delova. Ovo može olakšati prenos datoteke.
- Kompresuj Fajlove** ili **Kompresuj fajlove**: kompresuj fajlove da smanjiš veličinu enkriptovanih fajlova.
- Izbrisane datoteke** ili **Fichiers supprimés**: izbrišite izvorne datoteke kako biste zadržali samo šifrovanu verziju



### B. Dešifrovanje podataka sa Picocrypt



Ako treba da dešifrujete podatke, nije ništa komplikovanije od njihovog šifrovanja. Jednostavno otvorite Picocrypt i **prevucite i otpustite PCV datoteku koju treba dešifrovati**. Zatim unesite lozinku i/ili izaberite ključ datoteku pre nego što kliknete na "**Decrypt**".



![Image](assets/fr/021.webp)



Nekriptovana verzija ZIP arhive "Encrypted.zip" sada mi omogućava da povratim svoje dve datoteke u čistom tekstu!



![Image](assets/fr/022.webp)



## IV. Zaključak



**Upozoreni ste: Picocrypt je veoma lak za korišćenje, i radi! Iako je Interface minimalistički, uključuje neke veoma korisne opcije za prilagođavanje enkripcije! A pošto je dostupan u prenosivoj verziji, možete ga poneti sa sobom gde god da idete, tako da možete dešifrovati svoje podatke sa poverenjem**



Obavezno koristite jake lozinke za zaštitu podataka, a ako koristite ključnu datoteku, morate se setiti da je napravite rezervnu kopiju, inače više nećete moći da dešifrujete PCV kontejner generisan od strane Picocrypt-a. Na kraju, trebalo bi da znate da postoji i [CLI verzija](https://github.com/Picocrypt/CLI) (sa manje funkcija) koja vam omogućava da pokrenete Picocrypt iz komandne linije: i ovde, Picocrypt otvara vrata ka novim mogućnostima.



https://planb.network/tutorials/computer-security/data/veracrypt-d5ed4c83-7c1c-4181-95ea-963fdf2d83c5