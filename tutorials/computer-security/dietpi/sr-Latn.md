---
name: DietPi
description: Lagan operativni sistem optimizovan za mašine sa slabijim performansama. Sa preferencijom za samostalno hostovanje.
---

![cover](assets/cover.webp)



U ne-tehničkim krugovima, brendovi kao što su `Odroid`, `Raspberry Pi`, `Orange Pi` ili `Radxa`, su malo poznati. Ali dovoljno je pogledati u tehničke krugove, da bi se otkrilo da **SBC** računari--izgrađeni na jednoj matičnoj ploči, često mikroskopske veličine u poređenju sa uobičajeno korišćenim računarima--postaju neophodni, kao podrška za bilo koji lični projekat.



Ovo su računari proizvedeni u širokom spektru modela. Oni preferiraju da koriste Linux distribucije, često prilagođene da glatko rade na ovim slabijim mašinama.



**DietPi nije izuzetak**: to je operativni sistem zasnovan na Debian-u, optimizovan da bude što lakši i da čak i najmanje performantni `SBC` učini veoma brzim. Prešao je sa Debian12 Bookworm na Debian13 Trixie baš dok je ovaj vodič pisan, a sada takođe podržava `RISC-V` procesore zasnovane na otvorenom kodu za SBC-ove. DietPi je prijatno otkriće koje zaslužuje dalje proučavanje.



## Snage



Ovo nije "uobičajeni duplikat" Debiana za male ploče tipa Raspberry. DietPi je:




- Optimizovan za brzinu i lakoću**: [poređenje sa drugim Debian distribucijama za SBC](https://dietpi.com/blog/?p=888), DietPi je lakši u svemu. DietPi ISO slika teži manje od 1 GB, što je daleko najmanje među onima posvećenim starijim modelima Raspberry ili Orange PI (na primer). Zahtevi za RAM i CPU resursima su veoma niski, tako da uvek izvlači najbolje iz ploča, čak i starijih.
- Ugrađene automatizacije i instalateri**: Paket posvećenih komandi pomaže korisnicima da prate sistemske resurse, kao i da automatizuju zadatke za instalaciju i pokretanje programa, ažuriranje verzija, pravljenje rezervnih kopija i proveru svih logova.
- Snažna zajednica orijentisana na eksperimentisanje**: [tutorijali](https://dietpi.com/forum/c/community-tutorials/8) i projekti iz DietPi zajednice, idealni su za inspiraciju softverom koji možete instalirati jednim klikom, zahvaljujući DietPi-ju.



**Iskoristiti svaki deo vašeg SBC-a nikada nije bilo lakše**.



## Automatizacije za samostalno hostovanje


Želite da eksperimentišete sa sopstvenim serverom za pokretanje naprednih mrežnih rešenja ili alatki za unapređenje vašeg Bitcoin znanja? DietPi može biti rešenje koje ste tražili. Iako mnogi ljudi znaju kako da upravljaju sopstvenom infrastrukturom i pokreću savršeno konfigurisane i zaštićene servere, DietPi je odgovarajući korak za one koji žele da počnu od nule.



Umesto da ručno obavljate sve složene zadatke koje takav zadatak zahteva, DietPi vam omogućava da ih izgradite pomoću `wizard`-a i sopstvene komandne linije. Ovde možete eksperimentisati sa sopstvenim ličnim cloud-om, upravljanjem uređajima za _smart home_, automatizovanim bekapovima i crontab-om, kao i sa naprednijim rešenjima.



![img](assets/en/01.webp)



## Instalacija



### Preuzmi



DietPi nudi bezbroj ISO slika, za snimanje operativnog sistema na mnoge različite uređaje. Neki su samo podržani: ISO za Raspberry PI5 je još u fazi testiranja, na primer, ali sigurno možete pronaći onaj koji odgovara vašoj ploči.



Za ovaj vodič sam izabrao da ga instaliram na tanki klijent, tako da je izbor pao na _PC/VM_ a zatim na _Native PC_. Postoje dve ISO slike za ove uređaje, koje se razlikuju u generaciji bootloader-a. Mašina korišćena u tutorijalu je prilično stara, tako da je izbor pao na _BIOS/CSM_ verziju. Ako imate noviju mašinu, ispravna verzija bi mogla biti `UEFI`.



![img](assets/en/02.webp)



Sletećete na stranicu koja sadrži `sliku instalatera`, `sha256` i `potpise`.



![img](assets/en/03.webp)



Pripremite direktorijum u `home` vašeg svakodnevnog računara, kako biste mogli preuzeti potrebne fajlove, pomoću `wget`.



![img](assets/en/04.webp)



Javni ključ programera zahtevao je minimalno istraživanje, ali ga možete pronaći na ovom linku: https://github.com/MichaIng.gpg.



![img](assets/en/05.webp)



Proverite sadržaj direktorijuma sa `ls -la` i uvezite MichaIng ključ u vaš ključni prsten, koristeći `gpg --import`.



### Verifikacija i blic



Konačno, deo koji najviše preporučujem: utvrdite autentičnost operativnog sistema koji ste preuzeli i koji ćete instalirati na vaš SBC.



![img](assets/en/06.webp)



Ako ste takođe dobili rezultat `Good signature` i istu Hash kontrolu sa sha256sum komandom, možete nastaviti sa flešovanjem ISO-a na USB stik. Koristite aplikacije kao što je Whale Etcher za to.



![img](assets/en/07.webp)



## Instalacija DietPi



![img](assets/en/09.webp)



Prenesite fleš disk na uređaj koji će hostovati DietPi i započnite instalaciju operativnog sistema lime Green. U ovoj vežbi koristimo tanki klijent sa 16 GB RAM-a, 128 GB SSD za operativni sistem i drugi disk od 1 TB za podatke. Instalacija je trajala manje od 30 minuta, ali ako ćete koristiti, na primer, Raspberry, resursi mogu biti manji i trajati duže. Tokom instalacije će vam biti prikazan napredak.



![img](assets/en/08.webp)



Budući da je dizajniran za Raspberries i slične uređaje, prava priroda DietPi-ja je takozvana `headless` instalacija, bez grafičkog okruženja i sa native `shsh` pristupom. U vodiču ćete umesto toga videti grafičko okruženje, tačnije LXDE.



Tokom ovog koraka bićete zamoljeni da odlučite koji veb pregledač želite da koristite kao podrazumevani, između Chromium-a i Firefox-a. Obe opcije funkcionišu dobro; nema posebnih kontraindikacija za bilo koji, osim vaših ličnih preferencija.



Pred kraj, instalacioni program može vas pitati da li već želite da instalirate neke programe, ali ovde **savjetujem da ništa ne pre-učitavate**. Trebalo bi da znate da ćete nakon ovog koraka biti zamoljeni da promenite podrazumevane lozinke za dva korisnika, iz sigurnosnih razloga. Najvažnije je da ćete biti obavezni da **postavite `Global Software Password (GSP)`**, što će osigurati pristup različitim softverima na kontrolisan način. **Ako preuzmete bilo koji softver tokom instalacije OS-a, bez postavljenog `GSP`, oni će ostati praktično nedostupni**. Moraćete da ih deinstalirate i ponovo instalirate nakon postavljanja `Global Software Password`: stoga, **ne stavljajte ništa kako biste izbegli dupli posao**. (Nezgoda je verovatna, ali ne 100% sigurna).



Instalacija se završava zahtevom za aktivaciju DietPi-Survey, automatizovane usluge prikupljanja podataka koja se koristi za podršku razvoju operativnog sistema. Prema vebsajtu, prikupljanje podataka se aktivira kada preuzmete bilo koji softver iz automatizacije koju pruža DietPi, ili kada nadogradite na sledeće izdanje. Svi imaju opciju da se uključe (_Opt IN_) ili isključe (_Opt OUT_).



![img](assets/en/23.webp)



Nakon završetka instalacije i naknadnog ponovnog pokretanja, DietPi se pojavljuje na ekranu dok ga postavljate. Za tutorijal, kao što je pomenuto, izabrao sam `LXDE` grafičko okruženje. Na desktopu sam pronašao prečicu za pokretanje `htop` i otvoreni terminal.



![img](assets/en/10.webp)



### "Alati" iz operativnog sistema



Zaboravite većinu programa koje koristite na svojoj Linux distribuciji-DietPi je toliko optimizovan da ste izostavili prilično mnogo njih. U suštini, morali biste ručno instalirati mnogo komandi, ali ako ga samo isprobavate, oduprite se iskušenju i pokušajte staviti DietPi-ove automatizacije na test.



To je definitivno terminal koji je prvi koristan alat za početak rada sa vašim novim operativnim sistemom, i automatski se otvara svaki put kada ga uključite.



![img](assets/en/11.webp)



Na ekranu terminala, pronaći ćete niz komandi koje su prethodene sa `dietpi-` predstavljajući [alatke](https://dietpi.com/docs/dietpi_tools/) ovog operativnog sistema:




- `dietpi-launcher`: za pristup operativnom sistemu, upravitelju datoteka, itd.
- `dietpi-Software`: što predstavlja alat pomoću kojeg možete instalirati sav softver koji je već dostupan u paketu
- `dietpi-config`: za pristup sistemskim konfiguracijama, čak i onim najnaprednijim.



![img](assets/en/14.webp)



### Bekap



Pravljenje rezervne kopije servera je rutina koju sistem administrator treba da predvidi od prvog pokretanja.



Sa DietPi postoji komanda `dietpi-Backup`, koju preporučujem da istražite kako biste pronašli idealno rešenje: omogućava vam da postavite redovan bekap, inkrementalni ili ne, u zavisnosti od korišćenih aplikacija, i sve opcije za prilagođavanje rutine.



![img](assets/en/22.webp)



Izaberite odredište za rezervnu kopiju, na primer drugi disk, pokretanjem `dietpi-Drive_Manager` da montirate odredišni disk i koristite ga za ovu funkciju.



## Konfiguracija



Samostalno hostovanje je preporučljivo iskustvo za svakoga, bilo da ste radoznali ili jednostavno entuzijastični. Međutim, postavljanje i konfiguracija servera uključuje neke ne tako zanemarljive tehnološke izazove. Tu dolazi **jednostavnost DietPi-ja**, koja vam omogućava da konfigurišete sistem prilagođen vašim potrebama u nekoliko jednostavnih koraka.



![img](assets/en/24.webp)



Osnovna i napredna podešavanja, sve na dohvat ruke u jednom Interface dostupnom sa komandom:



```dietpi-config


sudo dietpi-config


```

Che cosa si può fare ora? Automatizzare i processi da avviare all'accensione del server, configurare il `Locale` e tutte le impostazioni correlate alla Time Zone, impostare le schede di rete, le password e le periferiche audio/video, ad esempio.

## I Pacchetti Software

Tra le caratteristiche di semplicità di DietPi, vi è anche la dettagliata pagina dei Software che - oltre all'elenco delle applicazioni - mostra i primi passi da compiere per installarli e interagire con loro. Prendiamo ad esempio il caso di **Docker**:

![img](assets/en/15.webp)

Cliccando sulla sua "icona" compare in alto una finestra, dove è possibile cliccare i link che portano a una spiegazione di massima. La finestra mostra dove si trovano i file più importanti, come accedere all'interfaccia web e tanti altri suggerimenti per un'installazione fluida.

![img](assets/en/16.webp)

Le applicazioni che prevedono l'interazione dell'utente hanno un'interfaccia web pensata per questo scopo, accessibile all'indirizzo IP che va sempre sotto la sintassi `indirizzo-IP-localhost:porta`. Anche l'URL dell'interfaccia web la trovi se hai cliccato _View_.

Tutti [i software disponibili con DietPi](https://dietpi.com/dietpi-software.html), si installano da terminale, digitando:

```


sudo dietpi-software


```