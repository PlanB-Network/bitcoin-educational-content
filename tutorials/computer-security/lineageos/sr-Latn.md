---
name: LineageOS
description: Besplatan, nelepljen Android operativni sistem za pametne telefone
---

![cover](assets/cover.webp)



Konvencionalni Android sistemi unapred instalirani na našim pametnim telefonima predstavljaju niz dobro poznatih problema: intenzivna integracija Google usluga koja dovodi do stalnog praćenja podataka, neželjene sponzorisane aplikacije (bloatware) koje nameću proizvođači i napuštanje praćenja ažuriranja nakon nekoliko godina, osuđujući još uvek funkcionalne uređaje na programiranu zastarelost.



LineageOS se predstavlja kao elegantan odgovor na ove probleme. Proizvod open source zajednice i direktni naslednik CyanogenMod-a (ukinut krajem 2016. godine), LineageOS je besplatan mobilni operativni sistem zasnovan na Androidu koji vraća korisnicima kontrolu nad njihovim pametnim telefonima. Zvanično pokrenut u decembru 2016. godine, projekat sada ima preko 4,4 miliona aktivnih instalacija širom sveta i podržava stotine modela telefona od preko 20 različitih brendova.



![lineageos-homepage](assets/fr/01.webp)



*Zvanična LineageOS veb stranica koja predstavlja projekat i njegove ciljeve*



## Šta je LineageOS?



### Filozofija i ciljevi



LineageOS je operativni sistem otvorenog koda za mobilne uređaje zasnovan na Android Open Source Project (AOSP), koji razvija velika zajednica volontera širom sveta. Njegov nezvanični moto mogao bi biti "Vaš uređaj, vaša pravila": projekat ima za cilj da produži životni vek pametnih telefona, dok nudi pojednostavljeno Android iskustvo koje je prijateljsko prema privatnosti.



Projekat je iznikao iz pepela CyanogenMod-a, jednog od najpopularnijih alternativnih Android ROM-ova u istoriji. Kada je CyanogenMod Inc. zatvorio svoja vrata u decembru 2016. godine, zajednica se mobilisala kako bi kreirala LineageOS, zadržavajući duh inovacije i filozofiju otvorenog koda koja je karakterisala svog prethodnika.



Za razliku od OEM Android distribucija, LineageOS ne instalira unapred nijednu Google aplikaciju po defaultu i potpuno eliminiše bloatware. Korisnici počinju sa minimalističkim sistemom koji uključuje samo osnovne aplikacije (telefon, poruke, kamera, pregledač) i slobodni su da kasnije dodaju šta žele.



### Uticaj i zajednica



Zvanična statistika otkriva razmere projekta: sa preko 4,4 miliona aktivnih instalacija u 224 zemlje, LineageOS predstavlja jednu od najšire prihvaćenih Android alternativa na svetu. Brazil prednjači sa preko 2 miliona korisnika, a slede Kina i SAD, što pokazuje univerzalnu privlačnost besplatnog, prilagodljivog Androida.




## Glavne karakteristike



### Interface i korisničko iskustvo



**Čisti Android**: LineageOS nudi autentično Android iskustvo blisko AOSP-u, bez proizvođačkih slojeva ili suvišnih aplikacija. Interface ostaje poznat korisnicima Androida dok nudi optimalnu fluidnost zahvaljujući odsustvu bloatware-a.



**Podrazumevano bez Google-a**: Nema unapred instaliranih Google usluga, iz pravnih i etičkih razloga. Ovaj pristup "bez Google-a" garantuje potpunu kontrolu nad vašim ličnim podacima i poboljšava performanse izbegavanjem usluga koje rade u pozadini.



### Prilagođavanje i bezbednost



**Napredna prilagođavanja**: LineageOS otključava mnoge opcije koje nisu dostupne na standardnom Androidu: rekonfiguracija navigacionih dugmadi, prilagodljive sistemske teme, profili korišćenja prilagođeni različitim kontekstima (posao, lično, igranje).



**Outil Trust**: Integrisana funkcionalnost koja prati status bezbednosti vašeg uređaja i upozorava vas na potencijalne pretnje, pružajući uvid u bezbednost vašeg sistema u realnom vremenu.



**Produžena ažuriranja**: Zajednica LineageOS posvećena je pružanju mesečnih bezbednosnih zakrpa, omogućavajući uređajima koje su njihovi proizvođači obustavili da nastave da primaju najnovije Android bezbednosne zakrpe.



## Kompatibilni uređaji



LineageOS podržava stotine uređaja od preko 20 proizvođača: Samsung, Xiaomi, OnePlus, Motorola, Sony, Google Pixel, Fairphone i mnogi drugi. Ova široka kompatibilnost je jedna od glavnih prednosti projekta u odnosu na alternative kao što je GrapheneOS, koji su ograničeni na Pixel uređaje.



![devices-compatibility](assets/fr/02.webp)



*Stranica uređaja kompatibilnih sa LineageOS-om sa filterima po proizvođaču*



![google-devices](assets/fr/03.webp)



*Podržani Google uređaji, uključujući Pixel 4 (kodno ime "flame")*



### Popularni uređaji



Prema zvaničnim statistikama, najčešće korišćeni modeli uključuju razne uređaje koji pokrivaju različite cenovne i starosne kategorije, što pokazuje sposobnost LineageOS-a da udahne novi život starijim pametnim telefonima, kao i da optimizuje novije.



### Ključne tačke pre instalacije



**Otključiv bootloader**: Proverite da li vaš proizvođač/operator dozvoljava otključavanje. Neki brendovi, kao što je Huawei, su ukinuli ovu mogućnost na novijim modelima, dok drugi nameću specifične procedure.



**Tačan model**: Ključno je preuzeti ROM koji tačno odgovara vašem uređaju. Dva modela sa sličnim trgovačkim imenima mogu se tehnički razlikovati (na primer Galaxy S10 vs S10 5G) i zahtevaju različite slike.



**Skalabilna podrška**: Noviji uređaji možda neće biti odmah podržani, jer je za portovanje potreban volonter programer koji će se time baviti. S druge strane, podrška može prestati ako se održavalac uređaja povuče iz projekta.



## Instalacija



### Osnovni preduslovi



⚠️ **Pročitajte ova uputstva u potpunosti pre nego što počnete** kako biste izbegli bilo kakve probleme!



**Vratite se na fabrički firmware (ako je potrebno) :**




- Android Flash Tool**: Koristite zvanični Google alat [flash.android.com](https://flash.android.com) da lako vratite vaš Pixel uređaj na originalni Android iz vašeg web pregledača (potreban je Chrome/Edge)
- Alternative**: Ručno preuzmite fabričke slike sa [developers.google.com/android/images](https://developers.google.com/android/images)



**Obavezni preduslovni testovi:**




- Pokrenite svoj uređaj barem jednom** sa originalnim stock sistemom
- Testiraj sve funkcije**: SMS, pozivi, Wi-Fi, mobilni podaci
- Važno**: Proverite da li možete slati/primati SMS poruke i obavljati/primati pozive (uključujući putem WiFi i 4G/5G). Ako to ne funkcioniše na osnovnom sistemu, neće raditi ni na LineageOS!
- Nedavni uređaji**: Neki zahtevaju da se VoLTE/VoWiFi koristi barem jednom na osnovnom sistemu kako bi se omogućio IMS



**Priprema sistema:**




- Uklonite sve Google** naloge sa svog uređaja kako biste izbegli zaštitu od vraćanja na fabrička podešavanja, koja može blokirati aktivaciju.
- Potpuna sigurnosna kopija** : Proces će potpuno obrisati vaš telefon. Napravite rezervnu kopiju fotografija, kontakata, aplikacija i važnih fajlova



**ADB i Fastboot alati:** Pratite [zvanični LineageOS vodič](https://wiki.lineageos.org/adb_fastboot_guide#installing-adb-and-fastboot) za instalaciju Android SDK Platform Tools. Proverite instalaciju sa `adb version` i `fastboot --version`.



**Konfiguracija telefona:**




- Aktiviraj **Opcije za programere**: Podešavanja > O telefonu > dodirni "Broj izrade" 7 puta



![android-version](assets/fr/06.webp)



*Idite na Podešavanja > O telefonu da biste aktivirali režim za programere*





- Omogući **USB debugging** u opcijama za programere
- Aktiviraj **OEM otključavanje** (neophodno za otključavanje bootloader-a)



![developer-options](assets/fr/07.webp)



*Omogući Opcije za programere, USB ispravljanje grešaka i OEM otključavanje*



### Detaljna instalacija



⚠️ **Ova uputstva su specifična za LineageOS 22.2. Pratite svaki korak precizno. Ne prelazite dalje ako nešto ne uspe!



#### Korak 1: Provera firmvera



**Potreban firmver**: Vaš uređaj mora imati instaliran Android 13 pre nego što nastavite (za Pixel 4). Firmver se odnosi na slike specifične za uređaj koje su uključene u fabrički sistem.



![pixel4-info](assets/fr/04.webp)



*Zvanična stranica za Pixel 4 sa linkovima za preuzimanje i uputstvima za instalaciju*



![downloads-page](assets/fr/05.webp)



*Stranica za preuzimanje LineageOS build-a i datoteke*



**Preuzimanja specifična za Pixel 4:**




- Build LineageOS**: [download.lineageos.org/devices/flame/builds](https://download.lineageos.org/devices/flame/builds)
- Potrebne datoteke**: Preuzmite 3 potrebne datoteke sa ove stranice (biće korišćene u narednim koracima):
  - `lineage-22.2-YYYYMMDD-nightly-flame-signed.zip` (glavni ROM)
  - dtbo.img` (particija uređajnog stabla blob)
  - `boot.img` (recovery LineageOS)



⚠️ **Važno**: Proverite verziju Androida, a ne verziju proizvođačevog OS-a. Korišćenje prilagođenog ROM-a (čak i LineageOS) ne garantuje da je ovaj zahtev ispunjen.



💡 **Savjet**: Ako ste u nedoumici oko vašeg firmvera, vratite se na osnovni sistem pre nego što nastavite!



#### Korak 2: Otključavanje bootloadera



⚠️ **Ovaj korak briše sve vaše podatke!





- Testirajte ADB konekciju**: Povežite vaš uređaj putem USB-a i testirajte komandom `adb devices` iz terminala na vašem računaru



![adb-devices](assets/fr/08.webp)



*Proverite ADB vezu sa komandom `adb devices`*





- Autorizujte vezu** na vašem telefonu



![usb-debugging-auth](assets/fr/09.webp)



*USB debagovanje omogućeno sa RSA otiskom prsta računara*





- Pokreni u režimu bootloader-a** :


```
adb -d reboot bootloader
```


Ili držite **Volume Down + Power** uređaj isključen





- Proveri fastboot** konekciju:


```
fastboot devices
```



![fastboot-mode](assets/fr/10.webp)



*Fastboot komande u terminalu za proveru veze*



![bootloader-screen](assets/fr/11.webp)



*Prikaz fastboot-a na Pixel 4 sa sistemskim informacijama*





- Otključaj bootloader** :


```
fastboot flashing unlock
```


Na uređaju koristite tastere za jačinu zvuka za navigaciju i pritisnite dugme **Power** da biste izabrali "Unlock the bootloader" i potvrdili operaciju.



![unlock-bootloader](assets/fr/12.webp)



*Potvrda otključavanja bootloadera na uređaju*



⚠️ **Telefon će se automatski restartovati** nakon potvrde otključavanja





- Nakon automatskog ponovnog pokretanja**, ponovo omogućite USB ispravljanje grešaka u opcijama za programere




#### Korak 3: Flash dodatnih particija



⚠️ **Potrebno za pravilno funkcionisanje oporavka**





- Ponovno pokreni bootloader**: Smanji zvuk + Napajanje
- Flash** (zamenite `/path/to/` sa fasciklom u kojoj ste preuzeli datoteku) :


```
fastboot flash dtbo /chemin/vers/dtbo.img
```



![flash-partitions](assets/fr/13.webp)



*Blicanje dtbo i boot.img particija putem fastboot-a*



#### Korak 4: Instaliranje LineageOS recovery





- Flash recovery** (zameni `/path/to/` sa fasciklom gde si preuzeo datoteku) :


```
fastboot flash boot /chemin/vers/boot.img
```




- Ponovo pokreni u recovery** da proveriš



#### Korak 5: Instaliranje LineageOS-a





- Ponovno pokretanje u recovery**: Smanjenje zvuka + Napajanje → Recovery Mode



![recovery-mode](assets/fr/14.webp)



*Interface iz LineageOS oporavka sa glavnim menijem*





- Factory Reset** : Ukucajte "Factory Reset" → "Format data / factory reset"



![factory-reset](assets/fr/15.webp)



*Proces vraćanja na fabrička podešavanja u LineageOS* recovery





- Povratak na glavni meni**
- Sideload LineageOS** :
   - Na uređaju: "Primeni ažuriranje" → "Primeni sa ADB-a"
   - Na PC-u: `adb -d sideload /path/to/lineageos.zip`



![apply-update](assets/fr/16.webp)



*Izaberite "Apply Update" zatim "Apply from ADB" u recovery*



![sideload-process](assets/fr/17.webp)



*Instalacija LineageOS-a u toku putem sideloada*



![sideload-terminal](assets/fr/18.webp)



*Komanda za bočno učitavanje u terminalu sa napretkom instalacije*



💡 **Normalno**: Proces se može zaustaviti na 47% ili prikazati greške "Uspešno" - ovo je normalno!



#### Korak 6: Prvo pokretanje





- Reboot**: "Ponovo pokreni sistem sada"
- Prvo pokretanje**: Može potrajati do 15 minuta



🎉 **Instalacija završena!**



### Tačke pažnje



⚠️ **Upozorenje**: LineageOS se pruža "kao što jeste" bez garancije. Iako činimo sve napore da osiguramo da sve funkcioniše, instalirate ovo na sopstveni rizik!



**Kritične provere:**




- Kompatibilnost firmvera**: Obavezno proverite verziju firmvera koja je potrebna na stranici za preuzimanje vašeg modela
- Nikada ponovo ne zaključavajte** bootloader nakon instalacije LineageOS-a
- Pratite specifična uputstva** za vaš uređaj



## Konfiguracija i aplikacije



### Prvi start-up


Pojednostavljen Interface, blizak osnovnom Androidu, bez Google-a. Jednostavna konfiguracija: jezik, Wi-Fi, nije potreban nalog.



### Alternativne aplikacije



**Osigurani izvori aplikacija:**



**F-Droid** : Referentna prodavnica aplikacija otvorenog koda, unapred instalirana sa LineageOS za microG ili dostupna za direktno preuzimanje. F-Droid nudi samo softver otvorenog koda koji je verifikovan i kompajliran transparentno, garantujući odsustvo tragača ili zlonamernih komponenti.



**Aurora Store**: Anonimni klijent za pristup Google Play Store-u bez Google naloga. Aurora koristi deljene anonimne naloge, omogućavajući vam preuzimanje popularnih aplikacija uz očuvanje vaše privatnosti.



**Suštinske alternativne aplikacije:**





- Navigacija**: Organic Maps (offline mape bazirane na OpenStreetMap)
- Komunikacija**: Signal (end-to-end šifrovane poruke), K-9 Mail (besplatan email klijent)
- Media**: NewPipe (bez reklama, bez praćenja YouTube), VLC (univerzalni medija plejer)
- Produktivnost**: Nextcloud (samo-hosting cloud), Simple Calendar (CalDAV sinhronizacija)
- Bezbednost**: Bitwarden (upravljač lozinkama), Aegis Authenticator (2FA kodovi)



Ove aplikacije, od kojih je većina dostupna putem F-Droid-a, čine koherentan ekosistem koji može u potpunosti zameniti Google usluge, a pritom nude moderno i funkcionalno korisničko iskustvo.



## Upotreba i održavanje



### Dnevno iskustvo



LineageOS transformiše Android iskustvo, dajući prioritet fluidnosti i odzivnosti. Pojednostavljeni Interface je posebno efikasan na starijim uređajima, kojima se daje novi životni vek, sa performansama koje su generalno superiornije u odnosu na proizvođačke ROM-ove zahvaljujući odsustvu teških slojeva i suvišnih procesa.



Osnovne funkcionalnosti (pozivi, SMS, fotografije, pretraživanje) rade besprekorno, dok alati za prilagođavanje omogućavaju da sistem bude fino podešen prema individualnim preferencijama bez ugrožavanja stabilnosti.



### sistem za ažuriranje OTA



LineageOS ima posebno jednostavan sistem ažuriranja putem Over-The-Air. Nove verzije se automatski predlažu putem obaveštenja, a instalacija zahteva samo nekoliko klikova, bez potrebe za složenim tehničkim intervencijama. Proces u potpunosti čuva vaše instalirane podatke i aplikacije.



Ova redovna ažuriranja su velika prednost, posebno za uređaje koje su njihovi proizvođači prestali da podržavaju, jer mogu nastaviti da koriste najnovije Android bezbednosne zakrpe.



### Preporučene najbolje prakse



**Sigurnost nakon instalacije:**




- Postavite jak PIN ili lozinku za otključavanje
- Proverite da je enkripcija skladišta omogućena (obično podrazumevano)
- Instalirajte menadžer lozinki kao što je Bitwarden putem F-Droid-a



**Preventivno održavanje:**




- Redovna OTA ažuriranja za sigurnost
- Ograničite instalaciju aplikacija na pouzdane izvore (F-Droid, Aurora Store)
- Periodično pregledajte dozvole dodeljene aplikacijama
- Povremena ponovna pokretanja optimizuju performanse i oslobađaju memoriju



## Prednosti i ograničenja



✅ **Prednosti:**




- Podrazumevana privatnost (bez praćenja od strane Google-a)
- Široka kompatibilnost (300+ modela)
- Superiorna performansa (bez bloatware-a)
- Produžena ažuriranja na starijim uređajima



❌ **Ograničenja:**




- Tehnička instalacija
- Nema Android Auto/Google Pay
- Bankarske aplikacije mogu biti problematične



## GrapheneOS vs LineageOS: Koja je razlika?



### Različiti pristupi



**GrapheneOS** se fokusira isključivo na maksimalnu sigurnost i radi samo na Google Pixel uređajima kako bi iskoristio njihove posvećene sigurnosne čipove. Sistem uključuje brojne napredne mere protiv eksploatacija i značajno pojačava peskovnik aplikacija.



**LineageOS** balansira bezbednost, privatnost i pogodnost na što više uređaja. Pristup je pragmatičniji, sa ciljem proširene kompatibilnosti umesto apsolutne bezbednosti.



### Upravljanje Google uslugama



**GrapheneOS**: Nudi opcioni sistem za Google Play u peskovniku. Google Play može biti instaliran, ali radi u strogom peskovniku, bez posebnih sistemskih privilegija. Ovaj jedinstveni pristup omogućava korišćenje Google ekosistema uz održavanje stroge kontrole bezbednosti.



**LineageOS**: Omogućava korisniku da izabere instalaciju Google servisa (GApps), microG (besplatna alternativa), ili da ostane potpuno bez Google-a. Maksimalna fleksibilnost da odgovara vašim potrebama.



### Tehnička uporedba




| **Aspekt** | **GrapheneOS** | **LineageOS** |
|------------|----------------|---------------|
| **Kompatibilnost** | Samo Pixels | Stotine uređaja |
| **Bezbednost** | Napredna ublažavanja | Standardna AOSP bezbednost |
| **Google Play** | Opciono sandboxing | Klasična instalacija moguća |
| **Instalacija** | Veb interfejs + USB | Tehnička ručna procedura |
| **Filozofija** | Bezbednost iznad svega | Ravnoteža i sloboda izbora |

### Preporuke za upotrebu



**Izaberite GrapheneOS** ako posedujete Pixel, ako vam je maksimalna sigurnost glavni prioritet i ako prihvatate ograničenja radi poboljšane zaštite.



**Odlučite se za LineageOS** ako imate uređaj koji nije Pixel, tražite dobar balans između privatnosti i praktičnosti, ili želite slobodu da izaberete svoj nivo kompromisa sa Google ekosistemom.



## Zaključak



LineageOS nudi zrelu alternativu za ponovno preuzimanje kontrole nad vašim Android pametnim telefonom. Oslobođeno iskustvo, optimalne performanse, široka kompatibilnost: idealan izbor za kombinovanje privatnosti i svakodnevne praktičnosti.



## Resursi



### Zvanična dokumentacija




- [LineageOS zvanična veb stranica](https://lineageos.org)
- [LineageOS Wiki](https://wiki.lineageos.org) - Uputstva za instalaciju po modelu
- [LineageOS za microG](https://lineage.microg.org) - Verzija sa integrisanim microG



### Zajednica




- [Subreddit r/LineageOS](https://reddit.com/r/LineageOS)
- [Mastodon nalog @LineageOS](https://fosstodon.org/@LineageOS)



https://planb.academy/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1