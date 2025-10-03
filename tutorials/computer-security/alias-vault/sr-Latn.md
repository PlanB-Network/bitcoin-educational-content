---
name: Alias Vault
description: Moćan alat za upravljanje lozinkama, dvofaktorskom autentifikacijom i aliasima (sa ugrađenim email serverom) - Takođe samostalno hostovan!
---

![cover](assets/cover.webp)



Privatnost i bezbednost na internetu je tema kojoj bi svako, bez obzira na posao kojim se bavi, trebalo da posveti posebnu pažnju.



Ova pitanja su, štaviše, deo sveta u stalnim previranjima: sve više programera učestvuje u ovoj temi, donoseći implementacije za uspostavljena rešenja i nove proizvode.



Ovo je slučaj sa **Leendert de Borst** i njegovim `Alias Vault`, revolucionarnim alatom (prvim te vrste) koji vam omogućava da upravljate i skladištite lozinke, koristite zapise lozinki za autentifikaciju na web uslugama, upravljate dvofaktorskom autentifikacijom, ali najvažnije generate stvarne _pseudonime_, sve u jednom Interface.



**Aliás Vault tu ne staje**.



## Ključne karakteristike



Alias Vault radi u oblaku na serverima programera ili je samostalno hostovan u sopstvenoj infrastrukturi, opcija za koju su dostupni Docker fajlovi i slika za instalaciju sa skriptom. Pored web Interface, ekstenzije su dostupne za sve popularne pretraživače, kao i mobilne aplikacije za iOS i Android; potonje se takođe mogu preuzeti sa F-Droid, zaobilazeći zvaničnu Google prodavnicu.



U jednom Interface Alias Vault je:




- Besplatan i otvoren izvor**
- Password Manager**, za čuvanje svih složenih lozinki. Koristeći ekstenziju za pregledač, menadžer lozinki popunjava prijave na vebsajtove
- 2FA**, da podrži dvofaktorsku autentifikaciju
- Menadžer alias-a sa ugrađenim email serverom**: Alias Vault ne kreira alias-e koji prosleđuju email korisnikovom poštanskom sandučetu; umesto toga, kreira stvarne alter-egoe, kompletne sa imenom, prezimenom, polom, korisničkim imenom, lozinkom i datumom rođenja (ako su ovi podaci potrebni).



Opsežna i temeljita dokumentacija je deo paketa, koji će pratiti novajlije u otkrivanju ovog moćnog alata.



## Bez ličnih podataka!



Počinje, kao i uvek, sa [aliasvault.net](aliasvault.net) vebsajta. Kao što je pomenuto, Alias Vault se može koristiti na sopstvenom serveru, ili iz cloud-a developera da biste se upoznali sa njim pre nego što pređete na rešenje koje se hostuje samostalno.



Sajt ima zaista upadljive i dobro održavane grafike, ali prava stvar dolazi ako počnete da ga koristite: **kreirajte svoj nalog**.



![img](assets/en/01.webp)



Na vaše ogromno iznenađenje, otkrićete da Alias Vault ne traži lične informacije: sve što vam je potrebno za kreiranje naloga je bilo koji nadimak, reč koja vam je poznata, sve dok je dostupna. Prihvatite Uslove korišćenja, izaberite reč i nastavite.



![img](assets/en/02.webp)



Postavite **`master password`** sada, što je najvažniji deo informacija u celom vašem novom sistemu. Sa ovom jednom lozinkom, zapravo, vi ćete biti jedini koji može pristupiti/oporaviti nalog, jer će ona čuvati vaš `vault` enkriptovan na serveru koji će hostovati vaše informacije.



![img](assets/en/03.webp)



Činjenica: Napravili ste sopstveni menadžer lozinki i menadžer aliasa, ali bez davanja sopstvenog funkcionalnog, privatnog emaila Address.



![img](assets/en/04.webp)



Alias Vault vas pozdravlja u siguran, nov, ličan, ali i prazan prostor. A sada počinjemo da ga malo popunjavamo.



Ako već imate menadžer lozinki, možete uvesti datoteku iz onog koji koristite, kako biste procenili razlike sa drugim provajderom, ili možda eliminisali alias menadžer kako biste sve upravljali u jednoj aplikaciji.



![img](assets/en/05.webp)



Alias Vault je izuzetno jednostavan: imate jednu glavnu stranicu, koja je `Home`, sa dva menija:




- `Credentials`: što vam omogućava da kreirate i zatim upravljate identitetima i aliasima
- `Email`: prijemno sanduče gde možete proveriti dolazne poruke za pseudonime koje ste generisali.



![img](assets/en/06.webp)



To je kreiranje prvog `alias` koji želimo da uradimo, pa idite u gornji desni ugao stranice i kliknite na _+New Alias_.



![img](assets/en/07.webp)



U početku meni izgleda minimalistički, prema filozofiji Alias Vault-a. Da biste otkrili funkcije ove opcije, kliknite na _Kreiraj putem naprednog režima_.



![img](assets/en/08.webp)



Gornji deo prvog ekrana možete koristiti za uvoz lozinki koje već koristite za usluge na koje ste pretplaćeni ili koje najčešće koristite na mreži.



Ako ste omogućili dvofaktorsku autentifikaciju na bilo kojoj (ili svim) od gore navedenih usluga, uz Alias Vault možete upravljati ovom dodatnom Layer sigurnošću uvozom `tajnog ključa`. Alias Vault će kreirati `TOTP` potreban za pristup.



![img](assets/en/09.webp)



**Upozorenje**: U prostoru rezervisanom za email Address, Alias Vault podrazumevano predlaže svoj domen; da biste koristili ispravan Address sa kojim ste prethodno kreirali naloge, kliknite na _Unesite prilagođeni domen_, kako biste mogli postaviti ispravan domen nakon `@`.



![img](assets/en/14.webp)



Donji deo ovog ekrana je najzabavniji. Kliknite na _Generate Random Alias_ i Alias Vault će kreirati zasebne identitete za vas za različite potrebe, svaki sa sopstvenim poštanskim sandučetom, veoma robusnim nivoom lozinki, dopunjenim drugim detaljima kao što su pol, datum rođenja i odgovarajući nadimak.



![img](assets/en/10.webp)



Iz odgovarajućeg menija, možete promeniti postavke koje utiču na generisanje lozinki, kao što je izbor samo malih slova i eliminisanje karaktera koji mogu biti dvosmisleni.



![img](assets/en/11.webp)



Možete koristiti alias email koji predlaže Alias Vault, ili promeniti domene ako kliknete na odgovarajući padajući meni.



![img](assets/en/12.webp)



Pre nego što koristite ovu e-poštu za prijavu na uslugu, možete testirati njenu funkcionalnost slanjem poruke sa sopstvenog Address na novokreirani poštanski sandučić.



![img](assets/en/13.webp)



**⚠️ UPOZORENJE**: Prijem emailova je moguć zahvaljujući Alias Vault-ovom ugrađenom serveru, ali ovo vam omogućava samo da primate emailove, a ne i da odgovarate ili koristite email sanduče sa "konvencionalnim" funkcijama `alias` servisa. Stoga se značajno razlikuje od Simple Login, Addy i drugih platformi koje su posvećene isključivo ovoj vrsti usluge. Za primer Simple Login-a možete pogledati posvećeni tutorijal:



https://planb.network/tutorials/computer-security/communication/simple-login-c17a10d6-8f84-4f97-8d50-7a83428d0f41

Da biste obrisali alias koji ste kreirali kao test, sve što treba da uradite je da se prijavite na svoj `Home`, zatim `Credentials` i kliknete na identitet koji želite da obrišete. Komanda _Delete_ će se pojaviti u gornjem desnom uglu kako biste nastavili.



![img](assets/en/16.webp)



## Ekstenzija za pregledač



U zavisnosti od vaših potreba, možete se osloniti na ekstenziju za pregledač, koja se može pronaći na najčešće korišćenim pregledačima.



![img](assets/en/15.webp)



Instalira se kao što ste već uradili sa svim ostalim ekstenzijama, tako da se neću zadržavati na tom detalju.



Ekstenzija pregledača je tu da olakša prijavljivanje na online usluge ili kreiranje novih pseudonima po potrebi: ako je usluga sačuvana među zapisima vašeg Alias Vault-a, automatsko popunjavanje radi ono što je potrebno.



![img](assets/en/17.webp)



Jedina oprezna napomena je da proverite da li je Alias Vault aktivan. Naime, aplikacija ima podrazumevano podešavanje prema kojem se pauzira nakon perioda neaktivnosti. Ovo je veoma korisna funkcija, **na primer, kada morate da se udaljite od računara i sprečite nekog drugog da pristupi vašim nalozima**. Pojednostavljena procedura će vam omogućiti da se ponovo prijavite unosom `glavne lozinke`, ako je prethodna sesija još u kešu. Vreme za odjavljivanje je jedan od parametara koje možete prilagoditi, skraćujući ili produžavajući ga prema vašim preferencijama.



## Mobilna aplikacija



Kao i sve aplikacije ovog tipa koje drže do sebe, Alias Vault ima verziju za mobilne uređaje, u oba okruženja, Android i iOS. Za Android, aplikaciju možete preuzeti sa [F-Droid](https://f-droid.org/packages/net.aliasvault.app/).



U vreme pisanja ovog teksta (kraj avgusta 2025), mobilna aplikacija smatra `auto-fill` eksperimentalnom funkcijom, koja radi samo sa veoma malo sajtova. Dok ne bude potpuno implementirana, korišćenje Alias Vault-a na mobilnom zahteva kopiranje/lepljenje podataka.



Kada preuzmete aplikaciju iz prodavnice, za prijavu jednostavno unesite korisnika i `glavnu lozinku` kreiranu na veb aplikaciji.



![img](assets/en/18.webp)



Kada otvorite svoj `vault`, bićete upitani da li želite da omogućite biometrijski kontrolisan pristup, dodatni Layer nivo sigurnosti kako biste sprečili nekog drugog da pristupi vašim lozinkama ako se desi da drži vaš telefon.



![img](assets/en/19.webp)



Ako odlučite da postavite biometrijsku proveru, samo napred. Ako preskočite ovaj korak i predomislite se, možete je kasnije konfigurisati iz menija _Settings_.



Kada završite prijavljivanje, pronaći ćete podatke koje ste već kreirali ponovo sinhronizovane.



![img](assets/en/20.webp)



Mobilna aplikacija može biti usmerena na link ka `vault` hostovanom na sopstvenom serveru.



![img](assets/en/22.webp)



I upravo ćemo o verziji koja se samostalno hostuje Address, ukratko, u sledećem odeljku.



## Self-Hosting: potpuna kontrola nad vašim podacima



Alias Vault, da budemo iskreni, nije prvi `menadžer lozinki` koji vam omogućava da implementirate uslugu na vašoj infrastrukturi. Postoje i drugi, ali neki ili imaju ograničenja ili su delimično zatvorenog koda.



Prilika je jedinstvena: **okončajte zavisnost od eksternih provajdera usluga ili oblaka, ali koristite sopstveni lokalni server za čuvanje i upravljanje lozinkama, aliasima i izuzetno osetljivim informacijama povezanim sa svim tim**. Sa Alias Vault-om možete takođe usmeriti email servis ka sopstvenom email serveru za dodatnu poverljivost.



Vreme je da se obratite [dokumentaciji](https://docs.aliasvault.net/installation/), kako biste saznali kako da nastavite sa samostalnim hostovanjem Alias Vault-a.



![img](assets/en/23.webp)



Alias Vault radi na Docker Compose-u, tako da je potrebno minimalno iskustvo sa Linux-om i Docker-om. Možete početi sa osnovnom instalacijom, a zatim nastaviti sa naprednijim rešenjima.



Vaš server mora raditi na 64-bitnoj mašini, sa Linux distribucijom, 1 GB RAM-a i najmanje 16 GB skladišta; verzija Dockera (CE) mora biti najmanje 20.10 ili viša, dok Docker Compose zahteva izdanje od 2.0 pa naviše.



Odlučio sam da isprobam Alias Vault sa tankim klijentom, na kojem je instaliran DietPi kao distribucija, Debian Bookworm baza, optimizovana na osnovne funkcije i već pokreće `Docker` i `Docker Compose`.



Prvo, kako biste imali neki red, kreirajte direktorijum u svom home folderu, otvorite `terminal` i nalepite komandu za pokretanje instalacionog skripta.



```bash
curl -L -o install.sh https://github.com/lanedirt/AliasVault/releases/latest/download/install.sh
```



![img](assets/en/24.webp)



![img](assets/en/25.webp)



Kada je instalacija završena, pronaći ćete svoje akreditive za pristup:


```
Admin Panel: https://localhost/admin
Username: admin
Password: yyy0xyx1yxy2zxx4
```



Proverite sadržaj direktorijuma nakon instalacije.



![img](assets/en/29.webp)



Da biste pokrenuli Alias Vault koristite komandu:



``` Pokreni-Alias-Trezor


./install.sh start


```

Alias Vault adesso gira sul tuo server personale.

![img](assets/en/30.webp)

Apri un browser e digita l'url: ti comparirà la pagina per fare login come `Admin` di Alias Vault.

![img](assets/en/26.webp)

Il più è fatto! Hai davanti a te il pannello per amministrare Alias Vault in maniera personalizzata.

![img](assets/en/27.webp)

Da questa interfaccia, potrai controllare quanti e quali utenti stanno utilizzando il servizio, limitarne l'uso, cancellare gli utenti (azione irreversibile) e soprattutto controllare tutti i `log`.

Se si tratta di una nuova installazione, non avrai altri utenti oltre ad `admin`; per crearne di nuovi, apri un'altra `tab` del browser e digita:

```


localhost/user/start


```

![img](assets/en/28.webp)

Da qui in poi, tutto procede come abbiamo visto in precedenza nella guida, con la differenza che adesso stai usando Alias Vault sul tuo server. Se la tua macchina è adeguatamente configurata e protetta, questo è un modo elegante e sicuro di gestire un tuo password e alias manager, senza servizi di terze parti.

Per fermare Alias Vault, torna al terminale e digita:

``` Stop-Alias-Vault
./install.sh stop

```



![img](assets/en/31.webp)



## Razmatranja o enkripciji i bezbednosti



![img](assets/en/32.webp)



Prema onome što Lanedirt navodi na sajtu, u dokumentaciji i na Github-u, sa Alias Vault-om **sve informacije (komponente) koje postavite na Alias Vault ostaju čvrsto vezane za uređaj, šifrovane i nedostupne bilo kome ko ne zna `master password`**.



`master password` je stoga osnovni element celog `vault`-a. Nakon što se unese, obrađuje se pomoću `Argon2id` algoritma, Hard-memory funkcije za derivaciju ključa, kako bi se sprečilo da tajna napusti uređaj.



Sve ostaje skriveno čak i od menadžera cloud ili hosting usluge. Zapravo, iz administratorskog panela ne možete pristupiti detaljima korisnika, možete samo znati da li su kreirali alijase, primili e-poštu i malo toga više.



Sav sadržaj koji se čuva je šifrovan i dešifrovan pomoću kriptografskih ključeva izvedenih iz `glavne lozinke`. **Samo šifrovani podaci se čuvaju na serveru, ništa se ne pojavljuje u običnom tekstu**. Ako korisnik zaboravi ili izgubi svoju `glavnu lozinku`, nalog povezan sa njom je nepovratno izgubljen, jer server ne može pristupiti sadržaju u običnom tekstu.



Za samohostovanu verziju postoji skripta za resetovanje `master password`, ali ovo ne sprečava gubitak podataka.



![img](assets/en/33.webp)



Pošto je Alias Vault u _Beta_ fazi, možda ćete imati poteškoća sa pristupom ako promenite/ažurirate glavnu lozinku. Predlažem da je od početka izaberete robusnu i složenu kako biste mogli eksperimentisati sa uslugom i na kraju odlučiti da li ćete je koristiti. Ako imate poteškoća sa pristupom oblaku nakon ažuriranja lozinke, molimo kontaktirajte podršku za Alias Vault.



Za potpuno razumevanje arhitekture i bezbednosti koju koristi Alias Vault, toplo preporučujem da posetite [ovu stranicu](https://docs.aliasvault.net/architecture/), koja sadrži detalje o kriptografiji koja je osnova njegovog rada.



## Plan puta


Namera programera su da učine Alias Vault zrelim i stabilnim do kraja 2025. godine, kako bi definisali njegove buduće karakteristike upotrebe.



Alias Vault je i uvek će ostati open source i besplatan, ali verovatno ne neograničeno kao u beta verziji. Neke plaćene funkcije su u procesu implementacije, kao što je već najavljeno.



Postoje planovi za tim/porodicu i podrška za hardverske ključeve, potonji za autentifikaciju sa FIDO2 ili WebAuth.



## Ko treba Alias Vault



**Alat poput ovog je idealan za svakoga ko stavlja privatnost na internetu na prvo mesto**.



Vaš identitet je, po svoj prilici, u srcu posla koji obavljate na mreži i mora biti zaštićen svim sredstvima kako bi se **ti** podaci udaljili od usluga, kompanija i brokera koji su spremni učiniti sve da dođu do vašeg ponašanja na mreži.



Alias Vault vam vraća potpunu kontrolu nad vašim akreditivima, smanjujući ili potpuno eliminišući potrebu za oslanjanjem na treće strane za čuvanje i šifrovanje vaših najosetljivijih podataka.



Arhitektura i kriptografski kapacitet Alias Vault-a su idealni za suverene pojedince, mala i srednja preduzeća, razvojne timove i sve entuzijaste **open source** aplikacija. Ako spadate u neku od ovih kategorija: uživajte u otkrivanju Alias Vault-a.