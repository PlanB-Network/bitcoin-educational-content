---
name: Cryptomator
description: Šifrujte svoje fajlove u oblaku
---
![cover](assets/cover.webp)



___



*Ovaj vodič je zasnovan na originalnom sadržaju autora Florian BURNEL objavljenom na [IT-Connect](https://www.it-connect.fr/). Licenca [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Moguće je da su napravljene izmene u originalnom tekstu.*



___



## I. Prezentacija



U ovom vodiču ćemo koristiti aplikaciju Cryptomator za šifrovanje podataka pohranjenih u oblaku, bilo na Microsoft OneDrive, Google Drive, Dropbox, Box ili čak iCloud.



Šifrovanje podataka koje čuvate na onlajn rešenjima za skladištenje kao što je Drive je najbolji način da zaštitite svoje fajlove i svoju privatnost. Zahvaljujući šifrovanju, vi ste jedini koji može dešifrovati i pročitati vaše podatke, čak i ako su pohranjeni na serveru u SAD-u ili nekoj drugoj zemlji širom sveta.



U ovoj demonstraciji koristiće se mašina sa Windows 11 22H2 i OneDrive, ali je procedura identična na drugim verzijama Windows-a i drugim uslugama skladištenja. Sve što treba da uradite je da instalirate klijent za sinhronizaciju i dodate svoj nalog. Ovo će omogućiti Cryptomator-u da skladišti svoje podatke u trezoru.



![Image](assets/fr/020.webp)



Cryptomator je alternativa drugim aplikacijama, posebno Picocrypt predstavljen u drugom članku, koji izgleda drugačije, ali je jednako jednostavan za korišćenje. Cryptomator je takođe **open source**, usklađen sa RGPD, i **šifrira podatke koristeći AES-256 bitni algoritam za šifrovanje**. Nasuprot tome, Picocrypt se oslanja na brži XChaCha20 algoritam (takođe 256-bitni).



https://planb.academy/tutorials/computer-security/data/picocrypt-98c213bd-9ace-425b-b012-bea71ce6b38f

Aplikacija Cryptomator je dostupna na **Windows** (exe / msi), **Linux**, **macOS,** ali takođe i na **Android** i **iOS**. Inače, sve aplikacije su besplatne, osim Android aplikacije, koju morate platiti (14,99 evra).



Na vašoj mašini, **Cryptomator će kreirati folder unutar kojeg će kreirati sef**. Unutar trezora, koji može biti smešten na vašem OneDrive, Google Drive ili sličnom servisu, vaši podaci će biti enkriptovani. Dakle, ako sve vaše podatke čuvate u sefu koji je hostovan na vašem Drive skladišnom prostoru, biće zaštićeni (jer su enkriptovani).



**Napomena**: u ovom članku, usluge online skladištenja se koriste kao primer, ali Cryptomator se može koristiti za šifrovanje podataka na lokalnom disku, eksternom disku ili čak NAS-u. Zapravo, nema ograničenja.



## II. Instaliranje Cryptomatora



Da biste započeli, potrebno je da **preuzmete** i **instalirate** **Cryptomator**. Kada se preuzimanje završi, potrebno je samo nekoliko klikova da biste završili instalaciju. Kao i [Rclone](https://www.it-connect.fr/rclone-un-outil-gratuit-pour-synchroniser-vos-donnees-dans-le-cloud/), Cryptomator će se osloniti na WinFsp da **montira virtuelni disk na vašem Windows računaru**.





- [Preuzmite Cryptomator sa zvaničnog sajta](https://cryptomator.org/downloads/)



![Image](assets/fr/025.webp)



## III. Korišćenje Cryptomatora na Windows-u



### A. Kreiraj novi sef



Da biste kreirali novi sef, kliknite na dugme "**Add**" i izaberite "**New safe...**". Vaši postojeći i poznati sefovi na ovoj mašini će se zatim pojaviti u Interface, sa leve strane. **Sef kreiran na mašini A može biti otvoren i modifikovan na mašini B**, pod uslovom da je opremljena sa Cryptomator-om (i da je poznat ključ za enkripciju).



![Image](assets/fr/015.webp)



Počnite tako što ćete trezoru dati ime, npr. "**IT-Connect**". Ovo će kreirati direktorijum pod nazivom "**IT-Connect**" u mom OneDrive-u.



![Image](assets/fr/011.webp)



U sledećem koraku, verovatno će Cryptomator **detektovati "Drive "** prisutan na vašem računaru: Google Drive, OneDrive, Dropbox, itd.... kako bi vam omogućio da direktno izaberete provajdera. Pokušao sam ovo na dva različita Windows 11 računara, sa nekoliko Drive-ova, i nije bilo detektovano. To nije problem, samo definišite "**Custom location**" i izaberite root vašeg prostora za skladištenje. Na primer: **C:\Users\<Username>\OneDrive**.



![Image](assets/fr/018.webp)



Dalje, možete podesiti opciju u naprednim postavkama.



![Image](assets/fr/021.webp)



Zatim, treba da definišete **lozinku koja odgovara ključu za šifrovanje**. Ova lozinka će vam omogućiti da **otključate svoj Cryptomator sef** i pristupite njegovim podacima. **Ako je izgubite, gubite pristup svojim podacima**. Na kraju, još uvek imate opciju **kreiranja rezervnog ključa** potvrđivanjem opcije "**Da, bolje sprečiti nego lečiti**", slično kao [BitLocker] ključ za oporavak (https://www.it-connect.fr/comment-activer-bitlocker-sur-windows-11-pour-chiffrer-son-disque/). Ovo je preporučljivo, ali nemojte čuvati ovaj rezervni ključ u korenu vašeg OneDrive-a!



Kliknite na "**Kreiraj sef**".



![Image](assets/fr/019.webp)



Kopirajte ključ za oporavak i sačuvajte ga u vašem omiljenom menadžeru lozinki. Kliknite na "**Dalje**".



![Image](assets/fr/013.webp)



To je to, vaš novi prtljažnik je kreiran i spreman za korišćenje!



![Image](assets/fr/014.webp)



### B. Pristupite ciframa



Da biste pristupili sefu i njegovim podacima, bilo da **čitati postojeće podatke ili dodati nove podatke**, potrebno je da ga **otključate**. Cryptomator prikazuje poznate sefove: IT-Connect sef se pojavljuje, tako da ga jednostavno izaberite i kliknite na "**Otključaj**".



![Image](assets/fr/016.webp)



Morate uneti svoju lozinku da otključate sef. Zatim kliknite na "**Release drive**".



![Image](assets/fr/022.webp)



**Vaš sef je montiran na Windows mašinu kao virtuelni disk.** Ovaj disk, koji ovde nasleđuje slovo E, omogućava vam pristup vašim podacima (u običnom tekstu, jer je sef otključan).



![Image](assets/fr/017.webp)



Na strani OneDrive-a, ne možemo direktno pregledati trezor Cryptomator-a. Ne možemo videti podatke (ni nazive fajlova ni sadržaj). To znači da ne morate dodavati podatke u vaš Cryptomator trezor putem uobičajenog OneDrive prečice. **Morate dodati vaše podatke koristeći Cryptomator-ov virtuelni disk**



![Image](assets/fr/012.webp)



### C. Opcije prtljažnika



Podešavanja sefa se pristupaju putem dugmeta "**Opcije šifrovanog volumena**" (kada je zaključan) i omogućiće automatsko zaključavanje u slučaju neaktivnosti, baš kao što možete učiniti sa vašim sefom za lozinke. Opcija "**Otključaj šifrovani volumen pri pokretanju**", kao što ime sugeriše, otključava disk bez ikakve vaše intervencije i montira virtuelni disk. Iz bezbednosnih razloga, najbolje je izbegavati aktiviranje ove opcije.



Putem "**Mounting**" kartice takođe možete odlučiti da ga montirate samo za čitanje ili dodelite određeno slovo.



![Image](assets/fr/024.webp)



Pored toga, u postavkama Cryptomatora, možete **omogućiti automatsko pokretanje aplikacije**.



## IV. Zaključak



Sa **Cryptomator**, možete **kreirati šifrovani sef** za samo nekoliko minuta kako biste zaštitili podatke koje želite da skladištite na OneDrive i sličnim servisima. Veoma je jednostavan za korišćenje kada je u pitanju "uparivanje" sa Drive-om: iz tog razloga, dajem mu prednost u odnosu na Picocrypt.