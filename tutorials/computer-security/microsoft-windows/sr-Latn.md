---
name: Windows 11
description: Automatska instalacija Microsoft Windows 11 putem konfiguracione datoteke
---
![cover](assets/cover.webp)


U ovom vodiču ćemo naučiti kako automatski instalirati Windows 11 koristeći metodu koja se razlikuje od standardnog procesa instalacije Windows-a.


## Preuzmi!


Prva stvar koja će vam trebati je instalaciona datoteka. Najsigurnije i najpouzdanije mesto za preuzimanje je direktno sa zvanične Microsoft-ove veb stranice.


Jednostavno posetite link naveden ispod i pratite uputstva za preuzimanje [Windows 11 ISO fajla](https://www.microsoft.com/en-us/software-download/windows11)


![Image](assets/en/02.webp)


Kada ste na stranici za preuzimanje, skrolujte dole do odeljka za preuzimanje ISO fajla.


![Image](assets/en/01.webp)


I odaberite odgovarajuću verziju.


![Image](assets/en/03.webp)


Nakon što odaberete Windows 11, kliknite na dugme Potvrdi.


Na ovom koraku, može potrajati nekoliko sekundi da se obradi zahtev, a zatim ćete videti sledeću stranicu:


![Image](assets/en/04.webp)


Nakon potvrđivanja zahteva, potrebno je da izaberete željeni jezik.


![Image](assets/en/05.webp)


Nakon odabira jezika i klika na dugme Potvrdi, zahtev će biti obrađen. Ovaj korak može potrajati nekoliko sekundi.


Kada se zahtev uspešno obradi, videćete stranicu sa linkom za preuzimanje .iso fajla. Kliknite na dugme Preuzmi 64-bitnu verziju da biste započeli preuzimanje.


Veličina datoteke je oko 5.5 GB, a generisani link će važiti 24 sata.


## Automatizacija!


U ovoj fazi, potrebno je izvršiti izmene u standardnoj Windows instalaciji. U ovoj fazi, koristeći Unattended instalaciju, određujemo koji će se elementi instalirati, bez kasnijeg unosa korisnika. Zapravo, u ovom metodu, koristi se XML fajl za konfigurisanje koraka instalacije i servisa instaliranih u Windowsu. Drugim rečima, korišćenje Unattended.xml fajla stvara proces automatizacije tokom instalacije, sprečavajući potrebu za izborom više opcija i izbegavajući zamorne korake koji su obično potrebni tokom podešavanja. Ovaj metod je neobičan, ali standardni metod koji je uveo Microsoft. Više informacija je dostupno na [Microsoft-ovoj zvaničnoj veb stranici](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/update-windows-settings-and-scripts-create-your-own-answer-file-sxs?view=windows-11).


Na internetu su dostupni različiti alati za generisanje Unattended fajlova. Neki od njih su online, dok su drugi offline. Jedan od online alata za kreiranje ovog fajla je [ovaj sajt](https://schneegans.de/windows/unattend-generator). Nakon otvaranja, prikazana nam je sledeća stranica:


![Image](assets/en/06.webp)


Kao što je pomenuto na vrhu stranice, ova metoda se može koristiti za instalaciju Windows 10 i 11. U prvom koraku biramo jezik za Windows. Ako treba da dodamo drugi ili čak treći jezik na listu jezika za prikaz i tastaturu u Windows-u, možemo koristiti polje ispod:


![Image](assets/en/07.webp)


U sledećem koraku, biramo željenu lokaciju.


![Image](assets/en/08.webp)


U ovoj fazi, možemo takođe odrediti arhitekturu procesora za računar. U ovom koraku, možemo:

1. Odlučite da li da ignorišete Windows sigurnosne funkcije, kao što su TPM i Secure Boot. Funkcija Secure Boot osigurava da, ako bilo koji osnovni Windows fajlovi budu izmenjeni tokom procesa pokretanja, problem bude otkriven i njihovo izvršavanje bude sprečeno. Ova funkcija takođe pomaže u zaštiti sistema od instaliranja zlonamernih ažuriranja na Windowsu. Omogućavanje opcije za zaobilaženje ovih funkcija je ponekad neizbežno na određenim računarima, posebno starijim modelima. Međutim, generalno se preporučuje da funkcije poput Secure Boot budu omogućene.

2. Ignorišite zahtev za internet konekcijom da biste završili proces. Ovo je korisno u situacijama kada žičana LAN veza nije dostupna, jer u većini slučajeva, bežična kartica još nije prepoznata tokom instalacije Windows-a, i pristup internetu putem kabla je potreban. Aktiviranje ove opcije rešava probleme vezane za ovaj korak.


U sledećem koraku, možemo izabrati ime za računar.


![Image](assets/en/09.webp)


Takođe možemo dozvoliti Windows-u da izabere ime za sistem. U ovom koraku možemo izabrati tip Windows-a, bilo kompresovan ili nekompresovan, ili dozvoliti Windows-u da odredi odgovarajuću verziju na osnovu specifikacija računara. Vremenska zona se takođe može podesiti u ovoj fazi.


Sledeći korak uključuje postavke particije:


![Image](assets/en/10.webp)


U ovoj fazi možemo odrediti tip particije za instalaciju Windows-a, kao i potrebna podešavanja za instalaciju Windows Recovery Environment-a. Odabirom prve opcije, izbor particije i particionisanje se odlažu do vremena instalacije Windows-a, a tokom podešavanja, ova pitanja će biti postavljena kao i u normalnom načinu instalacije.


U ovom koraku biramo verziju Windows-a za instalaciju:


![Image](assets/en/11.webp)


Ako je ključ proizvoda dostupan, može se uneti i u ovoj fazi.


Sledeći korak uključuje konfigurisanje Windows naloga za prijavu:


![Image](assets/en/12.webp)


## Postavke naloga


U ovoj fazi:


1. Možemo definisati ime i lozinku za administratorski nalog. Takođe je moguće kreirati više korisničkih ili administratorskih naloga.

2. Ovde navodimo na koji nalog se prijaviti prvi put nakon instalacije Windows-a. Različite opcije za ovaj deo prikazane su na slici.

3. Ako ne želite da se kreiraju bilo kakvi nalozi, obrišite sve naloge i izaberite ovu opciju. U tom slučaju, nakon instalacije Windows-a, automatski ćete biti prijavljeni na Windows Administrator nalog.


Sledeći korak uključuje konfigurisanje postavki lozinke i host datoteke:


![Image](assets/en/13.webp)


U ovoj fazi određujemo da li lozinke treba da imaju period isteka. Pored toga, ovaj deo uključuje bezbednosna podešavanja vezana za neuspešne pokušaje prijavljivanja, koja se mogu omogućiti ili onemogućiti u zavisnosti od vaših potreba.


Na dnu ovog odeljka nalaze se podešavanja za prikaz datoteka. Nijedna od ovih opcija nije dostupna tokom standardne instalacije Windows-a i mora se konfigurisati nakon instalacije. Nasuprot tome, sa metodom instalacije bez nadzora, ova podešavanja su lako dostupna.


Sledeći korak uključuje konfigurisanje Windows sigurnosnih postavki:


![Image](assets/en/14.webp)


## Postavke bezbednosti


U ovoj fazi:


1. Windows Defender može biti omogućen ili onemogućen. Ova funkcija deluje kao sigurnosni softver u Windows-u i pomaže u sprečavanju izvršavanja zlonamernih fajlova, određenih mrežnih napada i još mnogo toga.

2. Automatska ažuriranja za Windows mogu biti onemogućena. Ovo je jedan od uobičajenih izazova sa kojima se suočavaju korisnici Windows-a!

3. Ovaj odeljak omogućava uključivanje ili isključivanje UAC-a (Kontrola korisničkog naloga). Ova funkcija sprečava sumnjive aplikacije da se pokreću sa povišenim dozvolama za čitanje i pisanje.

4. Ovu funkciju koristi Windows za otkrivanje potencijalno štetnog softvera.

5. Omogućite ili onemogućite podršku za duge putanje u Windows aplikacijama, kao što su PowerShell i druge.

6. Omogućite ili onemogućite Udaljenu radnu površinu za daljinski pristup sistemu.


U zavisnosti od verzije Windows-a koja se koristi, neke od ovih funkcija mogu ili ne moraju biti podržane.


Sledeći korak uključuje konfigurisanje ikona:


![Image](assets/en/15.webp)


U ovom odeljku:


1. Ikone na radnoj površini su navedene, koje se mogu dodati ili ukloniti po potrebi.

2. Ikonice u meniju Start su navedene, koje se takođe mogu dodati ili ukloniti prema zahtevima.

3. Ovaj odeljak omogućava konfiguraciju da li će alati povezani sa virtualizacijom biti instalirani ili ne. Ova opcija je specifična za Windows 11 i ne odnosi se na Windows 10.


Sledeći korak uključuje konfigurisanje Wi-Fi podešavanja:


![Image](assets/en/16.webp)


U ovom odeljku mogu se konfigurisati podešavanja Wi-Fi mreže. Kao što je ranije pomenuto, u većini slučajeva Wi-Fi kartica nije prepoznata tokom instalacije Windows-a, tako da povezivanje tokom podešavanja obično nije moguće. Međutim, konfigurisajući ovaj odeljak, ako je bežična kartica detektovana, sistem se može povezati na internet.


Sledeći korak uključuje važnu postavku:


![Image](assets/en/17.webp)


U ovom odeljku navodimo da li informacije o problemu sistema treba poslati Microsoftu ili ne.


Sledeći korak uključuje konfigurisanje podrazumevanih aplikacija:


![Image](assets/en/18.webp)


## Podrazumevani softver omogući/onemogući


U ovom delu možemo izabrati bilo koje aplikacije koje ne želimo da budu instalirane po defaultu. Na primer, možemo odlučiti da ne instaliramo Cortana ili Copilot.


Sledeći korak uključuje sigurnosne postavke vezane za izvršavanje aplikacije:


![Image](assets/en/19.webp)


Primjenom WDAC postavki može se spriječiti izvršavanje određenih aplikacija.


Konačno, nakon primene željenih postavki, generisani XML fajl može biti preuzet:


![Image](assets/en/20.webp)


Klikom na Download XML File, datoteka autounattend.xml će biti preuzeta. Da biste koristili ovu datoteku, jednostavno montirajte preuzeti ISO na USB drajv, postavite datoteku autounattend.xml u korenski direktorijum, i zatim nastavite sa instalacijom Windows-a.


Jedan od alata dostupnih za kreiranje USB diska za pokretanje je Rufus. Rufus može napraviti USB fleš disk za instalaciju Windows-a, sa datom ISO datotekom za instalaciju Windows-a. Brz je i jednostavan, možete ga preuzeti [ovde](https://rufus.ie/en/#download)


![Image](assets/en/21.webp)


U ovom softveru, nakon odabira željenog USB diska i odgovarajuće ISO datoteke, kliknemo na Start.


![Image](assets/en/22.webp)


U ovoj fazi, onemogućavamo sve opcije, jer njihovo omogućavanje može izazvati sukobe prilikom korišćenja generisanog Unattend fajla. Nakon što se fajlovi kopiraju na USB drajv, postavljamo autounattend.xml fajl u korenski direktorijum:


![Image](assets/en/23.webp)


U ovom trenutku, USB drajv je spreman za korišćenje za automatsku instalaciju Windows-a, i instalacija se može započeti korišćenjem ovog drajva.


## ISO uređivanje


Ako treba da instalirate Windows na virtuelnu mašinu, možete koristiti softver za kreiranje i uređivanje ISO fajlova. Jedan takav softver je AnyBurn. Nakon što ekstrahujete sadržaj ISO fajla preuzetog sa Microsoft sajta, postavite autounattend.xml fajl u korenski direktorijum. Zatim, koristeći AnyBurn, kreirajte novi ISO sa ažuriranim sadržajem.


AnyBurn je multifunkcionalni softver za rad sa ISO fajlovima. Nudi razne funkcije za rukovanje ISO fajlovima, od kojih je jedna kreiranje bootabilnih ISO slika; [ovde](https://www.anyburn.com/download.php) je originalni sajt.


Na glavnoj stranici softvera, izaberite "Create Image from File/Folder":


![Image](assets/en/24.webp)


Na sledećoj stranici, izaberite sve datoteke izdvojene iz ISO-a zajedno sa datotekom autounattend.xml.


![Image](assets/en/25.webp)


U ovom koraku konfigurišemo postavke kako bismo ISO datoteku učinili butabilnom:


![Image](assets/en/26.webp)


U ovoj fazi, putanja do bootfix.bin fajla mora biti postavljena kako bi ISO bio butabilan. Ovaj fajl se nalazi u root-u ISO-a, unutar boot foldera. Takođe se preporučuje omogućavanje obe ISO9660 i UDF opcije u sekciji Properties.


![Image](assets/en/27.webp)


Nakon ovog koraka, klikom na Dalje kreiraće se ISO fajl. Ovaj fajl može se koristiti u softveru za virtualizaciju kao što je Oracle VirtualBox. Ispod ćete pronaći tutorijal o VirtualBox:


https://planb.academy/tutorials/computer-security/operating-system/virtualbox-6472f5be-10ce-4a07-8b24-097bfbcedd65