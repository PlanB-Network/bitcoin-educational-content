---
name: Zorin OS
description: Potpuni vodič za instalaciju i korišćenje Zorin OS-a kao moderne alternative za Windows
---

![cover](assets/cover.webp)



## Uvod



Operativni sistem (OS) je osnovni softver koji omogućava računaru da funkcioniše: upravlja hardverom, softverom, bezbednošću i korisničkim interfejsom.


Zorin OS je Linux distribucija dizajnirana posebno da olakša prelazak sa Windows-a, dok nudi prednosti softvera otvorenog koda: sigurnost, stabilnost, privatnost i performanse.



Na osnovu Ubuntu LTS, Zorin OS kombinuje visoku softversku kompatibilnost sa poznatim, prilagodljivim interfejsom, čineći ga kredibilnom i pristupačnom alternativom za Windows.



## Zašto Zorin OS?





- Interface poznat**: Izgled sličan Windows-u (start meni, taskbar)
- Laka tranzicija**: dizajnirano za korisnike koji dolaze sa Windows-a
- Poboljšana sigurnost**: Linux arhitektura, manje izložena virusima
- Poštovanje privatnosti**: bez nametljivog prikupljanja podataka
- Optimizovana performansa**: radi dobro na skromnim mašinama
- Ubuntu LTS** baza: stabilnost, redovna ažuriranja i široka kompatibilnost
- Napredna personalizacija**: putem alata Zorin Appearance.



## Instalacija i konfiguracija



### 1. Preduslovi



**Oprema potrebna:**





- USB ključ od najmanje **8 GB** (preporučeno 12 GB);
- Računar sa najmanje **25 GB slobodnog prostora na disku**
- Internet konekcija (preporučeno).



### 2. Preuzmi Zorin OS





- Posetite zvaničnu veb stranicu: [https://zorin.com/os](https://zorin.com/os)



![Page de téléchargement Balena Etcher](assets/fr/03.webp)





- Izaberite **Zorin OS Core** (preporučena besplatna verzija)



![Page de téléchargement Balena Etcher](assets/fr/04.webp)





- Preuzmi ISO sliku



Zorin OS takođe nudi :





- Zorin OS Lite** (stariji računari)
- Zorin OS Pro** (uz naknadu, sa naprednim funkcijama i podrškom)



## Kreiranje USB ključa za pokretanje sistema



Možete koristiti nekoliko alata, kao što je Balena Etcher :





- Preuzmite i instalirajte [Balena Etcher](https://etcher.balena.io/).
- Otvorite Balena Etcher, zatim odaberite Zorin ISO sliku.
- Izaberite USB ključ kao odredišni medij.
- Kliknite Flash i sačekajte da se proces završi.



![Utilisation de Balena Etcher](assets/fr/05.webp)



## Ključ za pokretanje i pristup BIOS-u



Isključite računar na koji želite da instalirate Zorin OS, a zatim priključite USB ključ.


Kada se vaš računar pokrene, pristupite BIOS-u (`ESC`, `F9` ili `F11` u zavisnosti od brenda) i izaberite USB ključ kao uređaj za pokretanje, zatim pritisnite `Enter` da započnete proces pokretanja.





- Na pokretanju, izaberite **Pokušaj ili instaliraj Zorin OS**.



![capture](assets/fr/08.webp)





- Ako imate NVIDIA grafičku karticu, izaberite **Try or Install Zorin OS (modern NVIDIA drivers)**.
- Molimo sačekajte dok se datoteke proveravaju.



![capture](assets/fr/09.webp)





- U instalacionom programu Zorin OS, izaberite jezik **French** zatim kliknite na Install **Zorin OS**.



![capture](assets/fr/10.webp)





- Izaberite raspored tastature.



![capture](assets/fr/11.webp)





- Označite okvire **Preuzmi ažuriranja tokom instalacije Zorin OS-a** i **Instaliraj softver treće strane za grafički i Wi-Fi hardver i dodatne medijske formate**.



![capture](assets/fr/12.webp)





- Da biste instalirali Zorin OS na ceo disk: izaberite **Erase disk and install Zorin OS**.



![capture](assets/fr/14.webp)



Da instalirate Zorin OS pored Windows-a (dual-boot) :





- Odaberite **Instaliraj Zorin OS pored Windows Boot Manager-a**.



![capture](assets/fr/15.webp)





- Ako niste particionisali svoj disk, izaberite prostor na disku koji želite da dodelite Zorin OS-u, zatim kliknite na **Install now**.



![capture](assets/fr/16.webp)





- Potvrdite promene na disku dvaput.



![capture](assets/fr/16.webp)



![capture](assets/fr/17.webp)





- Odaberite geografsku oblast **Pariz**.



![capture](assets/fr/18.webp)





- Kreirajte svoj korisnički nalog i dajte svom računaru ime.



![capture](assets/fr/19.webp)





- Molimo sačekajte dok se Zorin OS instalira.



![capture](assets/fr/20.webp)





- Kada je instalacija završena, kliknite na **Restartuj sada**.



![capture](assets/fr/21.webp)





- Uklonite USB instalacioni ključ i pritisnite Enter.



![capture](assets/fr/22.webp)



## Otkrivanje i korišćenje Zorin OS



### Prvi start-up



Kada pokrenete računar, bićete prebačeni na GRUB - Linux menadžer za pokretanje. Podrazumevano, **Zorin OS** je izabran; nakon 30 sekundi, pokreće se automatski.



![capture](assets/fr/23.webp)



Ako ste instalirali Zorin OS kao dual-boot sa Windows-om, možete pokrenuti Windows odabirom **Windows Boot Manager**.



Prijavite se sa svojim korisničkim nalogom :



![capture](assets/fr/24.webp)



Prilikom prvog pokretanja, aplikacija **Dobrodošli u Zorin OS** se pokreće kako bi vam pomogla da otkrijete vaš novi operativni sistem.



![capture](assets/fr/25.webp)



![capture](assets/fr/26.webp)



![capture](assets/fr/27.webp)



![capture](assets/fr/28.webp)



![capture](assets/fr/29.webp)



![capture](assets/fr/30.webp)



![capture](assets/fr/31.webp)



![capture](assets/fr/32.webp)





### Ažuriraj sistem



Menadžer ažuriranja će se uskoro otvoriti kako bi vas obavestio da su ažuriranja dostupna. Instalirajte ih klikom na dugme **Instaliraj sada**.



![capture](assets/fr/33.webp)



Možete ručno proveriti ažuriranja u aplikaciji **Software** > Updates:



![capture](assets/fr/34.webp)



### Personalizacija



Prva stvar koju treba uraditi u Zorin OS je da izaberete **izgled radne površine** koji vam najviše odgovara. Naći ćete izglede slične onima na Windowsu (a još više sa Pro verzijom).



Da biste to uradili, otvorite **Zorin Appareance** > **Type** :



![capture](assets/fr/35.webp)



Zatim otvorite **Settings** da prilagodite svoj sistem:


**Zvuk - Postavke - Zorin OS



![capture](assets/fr/36.webp)



**Online nalozi - Postavke - Zorin OS



![capture](assets/fr/37.webp)



### Aplikacije



Postoji nekoliko načina za instalaciju aplikacija:





- Software**, prodavnica aplikacija za Zorin OS. Aplikacije dolaze iz nekoliko izvora: apt, Flatpak i Snap.



![capture](assets/fr/38.webp)



![capture](assets/fr/39.webp)





- apt** install (command line) :



```bash
sudo apt install gparted
```



![capture](assets/fr/40.webp)



Za više informacija o instaliranju aplikacija u Zorin OS, pogledajte ovu stranicu: [Install Apps (zorin.com)](https://zorin.com/help/install-apps/).



### Windows aplikacije



Da biste instalirali Windows aplikacije, počnite instaliranjem paketa **zorin-windows-app-support** putem Terminala :



```bash
sudo apt install zorin-windows-app-support
```



Za listu kompatibilnih Windows aplikacija i njihovih nivoa kompatibilnosti, pogledajte stranicu [Wine Application Database] (https://appdb.winehq.org/). Tamo ćete pronaći sledeće oznake, koje odgovaraju nivou kompatibilnosti (od najboljeg ka najgorem): Platinum, Gold, Silver, Bronze i Garbage.



Da biste instalirali Windows .exe ili .msi aplikaciju, imate dve opcije:





- Otvorite **PlayOnLinux** i kliknite na dugme **Install** da biste pregledali kompatibilne aplikacije i igre.



![capture](assets/fr/41.webp)





- Dvaput kliknite na **.exe ili .msi** datoteku aplikacije i dozvolite instalacionom programu da vas vodi.



![capture](assets/fr/42.webp)



![capture](assets/fr/43.webp)



## Zaključak i dodatni resursi



Zorin OS je solidna, pristupačna alternativa Windows-u, kombinujući jednostavnost, sigurnost i privatnost.



Omogućava nesmetan prelazak na Linux, bez žrtvovanja udobnosti ili produktivnosti.



Da biste dodatno zaštitili svoj digitalni život, preporučujemo korišćenje usluga koje poštuju privatnost, posebno za šifrovanu komunikaciju:



https://planb.academy/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2