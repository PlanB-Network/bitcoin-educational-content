---
name: Raspberry Pi Zero
description: Kako napraviti minimalan, izolovan i jeftin računar koristeći Raspberry Pi Zero i komplet dodataka.
---
![cover](assets/cover.webp)



Ako ste već neko vreme na stranicama Plan ₿ Academy, već ste naučili da je jedno od najzastupljenijih sigurnosnih podešavanja, gotovo obavezno, **upravljanje sredstvima putem offline skladištenja vaših privatnih ključeva**.



Ako to još niste otkrili, kroz ovaj vodič ćete pronaći linkove ka resursima otvorenog koda pomoću kojih možete saznati više o tome.



Za offline upravljanje privatnim ključevima potreban je uređaj trajno isključen sa mreže, bilo da je to [hardverski novčanik](https://planb.academy/resources/glossary/hardware-wallet) ili računar sa airgap-om, posvećen ovoj specifičnoj funkciji.



Kako to uraditi ako, na primer, nemate mogućnost da kupite hardver koji obavlja samo ovaj zadatak, ali ne želite da odustanete od ovog sigurnosnog koraka?



## Rešenje


Šta ako bih vam rekao da možete napraviti offline uređaj u obliku airgap računara koji je veličine i težine USB fleš drajva i košta 35 evra? Zar ne biste verovali?



Nastavite čitanje.



Reći ću ti više: pročitaj sve do kraja. Predloženo rešenje je jeftino, ali nije baš najlakše. Prvo dobiješ opštu ideju, zatim odlučiš da uložiš nešto svog vremena u lično istraživanje i izabereš, sa što više mira, da li i kako da nastaviš.



## Zahtevi


**1** [Raspberry PI Zero](https://www.raspberrypi.com/products/raspberry-pi-zero/): PI Zero (bez ikakvog sufiksa) predstavlja osnovu za izradu računara sa minimalnim performansama, ali pre svega nema Wi-Fi i Bluetooth kartice, što su neophodni zahtevi za svrhu ove vežbe.





- **Cena**: oko 15.00 u vreme pisanja ovog vodiča (avgust 2025).
- **Kontinuitet proizvodnje**: Raspberry garantuje proizvodnju do januara 2030.



PI Zero bez Wi-Fi i Bluetooth-a, nažalost su postali gotovo nedostupni. Možda ćete moći lakše pronaći PI Zero W i PI Zero 2W alternative. U tom slučaju, možete onemogućiti funkcije povezivanja promenom konfiguracionog fajla. Nakon instalacije operativnog sistema, potrebno je dodati ove stavke u konfiguraciju:



```
dtoverlay=disable-wifi
dtoverlay=disable-bt
```



deo jednog vodiča pokazaće vam kako i gde to da uradite. Međutim, ako zaista želite da budete sigurni, možete pronaći nekoliko tutorijala na internetu za uklanjanje Wi-Fi čipa malim rezačem, onim koji je pogodan za rad na elektronskim pločama.



**2** Početni _starter kit_ za Raspberry PI Zero: kao što je praksa u Raspberry svetu, osnovna verzija, bez spoljašnjeg kućišta. Pored toga, ograničeni resursi tako male ploče uslovljavaju mogućnosti povezivanja sa spoljnim svetom.



Kada sam odlučio da nastavim, pronašao sam [ovaj komplet](https://www.amazon.it/-/en/GeeekPi-Raspberry-Aluminum-Passive-Heatsink/dp/B0BJ1WWHGF?crid=1NAFFVHG3IFBU&sprefix=raspberry+pi+zero+kit+geeek+pi%2Caps%2C88&sr=8-65) pun dodataka, kako bih u potpunosti iskoristio puni potencijal PI Zero. Naime, komplet sadrži USB A -> micro USB napajanje Supply, mali USB hub, mini-HDMI -> HDMI adapter, bakarni hladnjak i aluminijumsko spoljašnje kućište. Takođe, uz komplet dolaze i šrafovi i imbus ključ potrebni za postavljanje PI Zero u novo kućište.





- **Cena**: 19.99 eura.



**3** Ovaj vodič ne zahteva da trošite velike budžete na airgap računar. Ipak, trebalo bi da znate da će vam biti potrebna USB tastatura i miš (strogo žičani, izbegavajte Bluetooth) i monitor. U zavisnosti od ulaza na vašem monitoru, možda će vam biti potreban adapter sa mini-HDMI, jedinog izlaza dostupnog na PI Zero. Na kraju, pogledajte Hard za činjenicu da svi imamo negde u kući žičanu tastaturu i miš - vreme je da ih Dust.



## Dodatni Budžet



**4** Možete nabaviti originalni Supply napajanje od Raspberry, po ceni od oko 15,00 eura.



**5** Lično sam odlučio da koristim napajanje koje Supply pruža u _starter kitu_, kombinujući ga, međutim, sa USBA → miniUSB takozvanim `no data` kablom, koji košta 3.70 evra.



**6** Mikro SD kartica, da ima najmanje 32 GB memorije; ako je industrijski kvalitet/nivo, to je bolje.



**7** Trebaće vam sistem, USB na micro SD adapter, kao onaj koji vidite na slici. Operativni sistem vašeg PI Zero i njegova memorija će, zapravo, raditi na tom mediju.



![img](assets/it/06.webp)



## Instalacija operativnog sistema


Pre nego što zatvorite svoj PI Zero u kućište, preporučujem da instalirate operativni sistem. Tada ćete moći odmah da proverite LED koji pokazuje rad.



Da bih izabrao i snimio operativni sistem, odlučio sam se za najlakši način: korišćenje Raspberry-jevog alata `PI Imager`.



![img](assets/it/01.webp)



Idi na [Raspberry Github](https://github.com/raspberrypi/rpi-imager/releases) da preuzmeš najnovije izdanje Imagera, birajući ono koje je najprikladnije za tvoj operativni sistem (v. 1.9.6 u vreme pisanja). Primetićeš da pored svakog fajla stoji i heš odgovarajućeg fajla. To će nam biti korisno za verifikaciju.



![img](assets/it/02.webp)



Preporučujem da proverite operativni sistem koji ćete koristiti na svom airgap računaru, radi ličnog mira. Ovo će vam dati sigurnost da koristite legitimnu (ne zlonamernu) verziju Imager-a i, samim tim, Raspi OS-a.



Izvršite verifikaciju odmah nakon preuzimanja, sa vašim mašinom koju obično koristite povezanom na Internet.



Zatim otvorite Linux terminal i pripremite preuzimanje, kreirajući direktorijum `raspios` koji će biti koristan za rad sa njim.



![img](assets/it/19.webp)



Preuzmite Imager za vašu Linux distribuciju pomoću `wget`.



![img](assets/it/20.webp)



Konačno, pokrenite komandu `sha256sum` za datoteku i uporedite Hash sa onim koji je obezbedio Raspberry na svom Github-u.



![img](assets/it/21.webp)



Ili, ako imate Windows, otvorite Power Shell i upišite sledeću komandu:



```
Get-FileHash -Path <yourpath>\imager-1.9.6.exe
```



![img](assets/it/04.webp)



Dobićete Hash koji mora odgovarati onom objavljenom na Raspberry Github-u.



Kada verifikujete preuzimanje, možete instalirati Imager na vaš svakodnevni računar i otvoriti ga. Imager je alat koji vam je potreban da snimite operativni sistem na micro SD, koji će biti "sistemski disk" PI Zero.



Proces je izuzetno jednostavan: prvo izaberite Raspberry uređaj koji ćete koristiti (zato obratite pažnju na **vaš model** Raspi Zero), zatim verziju OS-a, i na kraju tačku montiranja micro SD kartice na koju ćete flešovati OS.



### Prvi korak



![img](assets/it/03.webp)



### Drugi korak



![img](assets/it/07.webp)



**Napomena**: izaberite `PI OS 32-bit`, jedini koji radi sa PI Zero.



### Treći korak



![img](assets/it/08.webp)



(Pazite da ostavite _Exclude System Drive_ izabrano kako biste izbegli da budete upitani da instalirate Raspi-jev operativni sistem na vašem računaru.)



Kada je sve postavljeno, Imager će vas pitati da li želite da koristite prilagođene postavke. Izaberite šta želite, ili kliknite na _Ne_ da nastavite sa podrazumevanim opcijama.



![img](assets/it/09.webp)



Potvrdite da želite obrisati sadržaj micro SD kartice



![img](assets/it/10.webp)



Imager počinje da flešuje operativni sistem na micro SD, traka za pomeranje će vas obavestiti o napretku.



![img](assets/it/11.webp)



Na kraju postoji automatska verifikacija, savetujem vam da je ne zaustavljate.



![img](assets/it/12.webp)



Na kraju se na ekranu pojavljuje poruka, i ako je sve bilo uspešno, izgleda kao ono što čitate na slici.



![img](assets/it/13.webp)



Sada zaista možeš izvaditi micro SD iz čitača i staviti ga u slot PI Zero. Uključi mali Raspberry i posmatraj LED: očekujemo da je zelen i da treperi, što označava normalno učitavanje operativnog sistema, a zatim da ostane stalno upaljen. Ako imaš druge indikacije, na primer ako LED treperi u pravilnom ritmu ili je crven, pogledaj FAQ ili [stranice foruma podrške](https://forums.raspberrypi.com/).



## Prva Konfiguracija


Prvo pokretanje Raspi OS-a je malo sporije nego obično jer mora obaviti nekoliko stvarnih zadataka instalacije. Ali ako je sve prošlo dobro, naći ćete ekran dobrodošlice.



![img](assets/it/14.webp)



Kliknite na _Next_ da biste postavili geografsku regiju, posebno za učitavanje ispravne tastature. Obratite posebnu pažnju na ovo poslednje.



![img](assets/it/15.webp)



Kliknite na _Next_ i bićete zamoljeni da kreirate svog korisnika, zapišite svoje akreditive i čuvajte ih dobro.



![img](assets/it/16.webp)



Čarobnjak vas pita da izaberete podrazumevani veb pregledač, između Chromium i Firefox; takođe vas može pitati o podešavanjima Wi-Fi mreže ako radite sa Zero W ili 2W PI. Nastavite i kliknite na _Preskoči_.



U nekom trenutku bićete pozvani da nadogradite softver i operativni sistem na brodu. Izaberite _Preskoči_: za potrebe ove vežbe mi zapravo pravimo offline mašinu, koja mora ostati offline u ovom trenutku.



Na kraju, može vas zamoliti da omogućite `ssh`, ali odbijte i ovaj korak, jer je to Zero airgap IP.



![img](assets/it/17.webp)



Nema mnogo više za konfigurisanje. Kada završite, restartujte Raspberry kako bi promene stupile na snagu.



![img](assets/it/18.webp)



## Novi kompjuterski vazdušni jaz


Nakon ponovnog pokretanja, vaš novi airgap računar je spreman. PI Zero vam prikazuje novu radnu površinu, sa kojom možete raditi ili putem GUI-ja ili iz komandne linije.



![img](assets/it/22.webp)



### Prvi koraci za PI Zero W ili 2W


Ako radite sa Raspberry PI Zero W ili 2W serijom, vaša ploča ima čipove za Wi-Fi i Bluetooth. Tokom prve postavke preskočili ste konfiguraciju veze, tako da PI Zero nije povezan na Internet. Sada možete trajno onemogućiti dva čipa putem softvera.



Zapravo, Raspi OS pruža datoteku `config.txt` koju možete urediti po želji. `config` se nalazi u `boot` particiji, u direktorijumu `firmware`, i možete je urediti i sačuvati sa `root` privilegijama.



Otvorite terminal sa ikone u gornjem levom uglu i postaje `root`.(1)



![img](assets/it/23.webp)



(1) Ako Raspi OS nije zahtevao da kreirate lozinku za `root` tokom prethodnih koraka, preporučujem da to uradite sada, koristeći komandu `passwd`. Omogućavanje `root` korisniku da funkcioniše nezavisno od vašeg ličnog korisnika može biti veoma korisno u situacijama oporavka.



Sa terminalom, proverite da li postoji fajl `config.txt` i budite spremni da ga uredite pomoću uređivača `nano`.



![img](assets/it/24.webp)



Uređivanje treba obaviti na dnu celog `config`, nakon reči `[All]`. Na ovom mestu ćete dodati `dtoverlay` komande prikazane na početku tutorijala.



![img](assets/it/25.webp)



Sačuvaj, zatvori i ponovo pokreni. U sledećem koraku ćemo preći na istraživanje malog Raspberry-ja.



## Šta očekivati od ovog uređaja?


Prema [tehničkim specifikacijama](https://www.raspberrypi.com/products/raspberry-pi-zero/) sa sajta Raspberry, PI Zero ima jednokoreni BCM2835 procesor i 512 MB RAM-a, pa se ne čini naročito moćnim.



Pošto je terminal lakši, koristićemo komandnu liniju za istraživanje konfiguracija sistema.



Kada uključite uređaj, videćete kratki ekran u duginim bojama, nakon čega sledi poruka dobrodošlice od Raspberry-ja, a u donjem levom uglu poruke kernela vezane za pokretanje sistema.



Kada se pojavi PI OS desktop, otvorite terminal i upišite:



```bash
uname -a
```


Ova komanda će vam prikazati verziju kernela koja je trenutno u upotrebi na ekranu, plus druge informacije.



![img](assets/it/26.webp)



Takođe možete videti informacije o CPU-u i hardveru tako što ćete otkucati:



```bash
lscpu
```



![img](assets/it/27.webp)



I takođe pogledajte `proc/mem/info`.



![img](assets/it/28.webp)



Da biste saznali verziju Debiana i kodno ime izdanja:



``` bash


lsb_release -a


```

![img](assets/it/29.webp)

Infine, due comandi per controllare la memoria di massa e i dischi:

``` bash
fdisk -l
```



![img](assets/it/31.webp)



``` bash


df


```
![img](assets/it/30.webp)

Per controllare come lavora la CPU:

``` bash
top
```



![img](assets/it/32.webp)



## Koristi


Iako performanse deluju ograničeno (na papiru i u poređenju sa snagom današnjih mašina) PI Zero je efikasan, posebno kao terminal.





- Prvo možete otići do glavnih menija i inspirišite se panelom _Dodaj/Ukloni softver_, gde ćete pronaći brojne alate za programiranje i vežbanje. Zapamtite da to možete uraditi i iz terminala, ali uvek sa `root` privilegijama.



![img](assets/it/33.webp)





- Možete "usvojiti" ovaj offline uređaj za čuvanje različitih poverljivih dokumenata, koji će ostati dostupni kada su potrebni, bez ikakvog izlaganja internetu.
- Možete koristiti ovu konfiguraciju da bezbedno generate vaše GPG ključeve.
- Mogao bi čak da iskoristiš ovu novu „igračkicu“ kao airgap uređaj za potpisivanje, [prateći savete Arman The Parman-a](https://armantheparman.medium.com/how-to-set-up-a-raspberry-pi-zero-air-gapped-running-latest-version-of-electrum-desktop-wallet-85e59ecaddc0).



Među novčanicima sa kojima sam upoznat, jedini koji pruža 32-bitno izdanje je Electrum. Pa: Zero IP kako smo ga pripremili u ovom vodiču omogućio bi vam da privatne ključeve držite van mreže, postavka za Wallet airgap koju smo pokrili u ovom vodiču:



https://planb.academy/tutorials/wallet/desktop/electrum-airgap-62b5a4c6-a221-4d41-9a62-4618c53d8223

## Zaključci


Postavka ima, verovatno, jednu veliku slabost: micro SD je medijum koji bi mogao da izazove probleme. Podložan je intenzivnoj upotrebi; možda već imate iskustva s tim, koristeći ga sa svojim telefonom. Nakon instalacije celokupnog softvera koji želite da koristite na Zero airgap IP, napravite dobru rezervnu kopiju dragocenog micro SD-a, koristeći Raspi OS alat koji imate na raspolaganju.



![img](assets/it/34.webp)



Kako vaše potrebe rastu, a s njima i vaše budžetske mogućnosti, možete istražiti druge Raspberry ili slične solucije. Govoreći o memoriji, na primer, PI 5 nudi mogućnost sastavljanja M2 NVME drajva, koji je svakako robusniji od microSD.



Ne zaboravi da beležiš i dokumentuješ svaki korak instalacije uslužnog softvera koji ćeš koristiti offline. **pre ili kasnije će izaći ažurirana verzija Raspi OS-a** koju ćeš sigurno želeti da iskoristiš. U tom trenutku ćeš morati da obrišeš sve i uradiš sve ispočetka (možda sa novom micro SD karticom 😂).



Vežba koju smo upravo uradili, pod pretpostavkom da je i vaš prvi eksperiment, pamtićete dugo. Nije uvek moguće posvetiti hardver `embedded` operacijama van mreže, a da se ne zanemari pažnja prema mašini koja nije povezana na mrežu, koju treba s vremena na vreme uključiti i proveriti.



Uspeo si, ipak, čestitam! I moći ćeš da predložiš ovo rešenje svima onima koji treba da drže svoje budžete pod kontrolom.