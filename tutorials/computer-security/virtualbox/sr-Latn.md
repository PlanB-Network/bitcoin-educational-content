---
name: VirtualBox
description: Instalirajte VirtualBox na Windows 11 i kreirajte svoju prvu VM
---
![cover](assets/cover.webp)



___



*Ovaj vodič je zasnovan na originalnom sadržaju Floriana Burnela objavljenom na [IT-Connect](https://www.it-connect.fr/). Licenca [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Moguće je da su napravljene izmene u originalnom tekstu.*



___




## I. Prezentacija



U ovom vodiču ćemo naučiti kako instalirati VirtualBox na Windows 11 kako bismo kreirali virtuelne mašine, bilo da pokrećemo Windows 10, Windows 11, Windows Server ili neku Linux distribuciju (Debian, Ubuntu, Kali Linux, itd.).



Ovaj uvodni vodič za VirtualBox pomoći će vam da započnete sa ovim open source rešenjem za virtualizaciju koje je razvila Oracle, a koje je potpuno besplatno. Kasnije će biti postavljeni drugi vodiči koji će vas dublje uvesti u ovu temu.



Kada je reč o virtualizaciji radne stanice, bilo za potrebe testiranja kao deo projekta ili tokom vaših IT studija, VirtualBox je očigledno dobro rešenje. Takođe je alternativa drugim rešenjima kao što su Hyper-V, koji je integrisan u Windows 10 i Windows 11 (kao i Windows Server), i VMware Workstation (naplaćuje se) / VMware Workstation Player (besplatan za ličnu upotrebu).



Moja konfiguracija: **Windows 11 radna stanica na koju ću instalirati VirtualBox**, ali možete instalirati VirtualBox na Windows 10 (ili stariju verziju), kao i na Linux. Što se tiče virtuelnih mašina, VirtualBox podržava širok spektar sistema, uključujući Windows (npr. Windows 10, Windows 11, Windows Server 2022, itd.), Linux (Debian, Rocky Linux, Ubuntu, Fedora, itd.), BSD (PfSense) i macOS.



## II. Preuzmi VirtualBox za Windows 11



Da biste preuzeli VirtualBox za instalaciju na Windows mašini, postoji samo jedan dobar Address: [zvanični sajt VirtualBox-a](https://www.virtualbox.org/wiki/Downloads) u odeljku "**Downloads**". Samo kliknite na "Windows hosts" da biste započeli preuzimanje ovog izvršnog fajla, koji je nešto veći od 100 MB.



![Image](assets/fr/025.webp)



## III. Instaliranje VirtualBox-a na Windows 11



### A. Instaliranje VirtualBox-a



Instaliranje VirtualBox** je jednostavno, a proces je isti za sve verzije Windows-a. Počnite pokretanjem VirtualBox izvršne datoteke koju ste upravo preuzeli, zatim kliknite na "**Next**".



![Image](assets/fr/026.webp)



Ova instalacija je prilagodljiva, ali preporučujem da instalirate sve funkcije: što je slučaj sa podrazumevanim izborom. Na slici ispod, možete videti različite Elements, uključujući:





- Podrška za USB u VirtualBox-u** da bi se omogućila podrška za USB uređaje u VirtualBox-u
- VirtualBox Bridged Network** za integraciju mrežne podrške u režimu "Bridge" (virtuelna mašina može se direktno povezati na vašu lokalnu mrežu)
- VirtualBox Host-Only Network** za integraciju mrežne podrške u režimu "Host-Only" (virtuelna mašina može komunicirati samo sa vašim fizičkim hostom na Windows 11 i drugim virtuelnim mašinama u ovom režimu)



Kliknite "**Next**" da nastavite.



![Image](assets/fr/001.webp)



Kliknite na "**Yes**", imajući na umu da **će mreža biti prekinuta na trenutak na vašem Windows 11 računaru**, dok VirtualBox vrši izmene mreže kako bi podržao različite tipove mreža, uključujući Bridge režim.



![Image](assets/fr/002.webp)



Kada potvrdite, instalacija će početi... I pojaviće se obaveštenje "**Da li želite da instalirate ovaj softver uređaja?**". Označite opciju "**Uvek veruj softveru kompanije Oracle Corporation**" i kliknite na "**Instaliraj**". VirtualBox zapravo treba da instalira nekoliko drajvera na vašem računaru.



![Image](assets/fr/003.webp)



Instalacija je sada završena! Označite opciju "**Pokreni Oracle VM VirtualBox 6.1.34 nakon instalacije**" i kliknite "**Klik**" da pokrenete softver.



![Image](assets/fr/004.webp)



### B. Dodajte paket ekstenzija



Još uvek na zvaničnom sajtu VirtualBox-a (pogledajte prethodni link), možete preuzeti zvanični paket ekstenzija, dostupan u odeljku "**VirtualBox 6.1.34 Oracle VM VirtualBox Extension Pack**" klikom na link "**All supported platforms**". Ovaj paket će vam omogućiti da dodate dodatne funkcionalnosti VirtualBox-u: nije obavezno da ga dodate, ali može biti korisno! Na primer, uključuje podršku za USB 3.0 u VM-ovima, podršku za veb kameru i enkripciju diska.



Otvorite VirtualBox, kliknite na "**File**" i zatim na "**Settings**" u meniju.



![Image](assets/fr/005.webp)



Kliknite na "**Extensions**" sa leve strane (1), zatim na dugme "**+**" sa desne strane (2) da **učitate VirtualBox** paket ekstenzija koji ste upravo preuzeli (3).



![Image](assets/fr/006.webp)



Potvrdite klikom na dugme "**Instalacija**".



![Image](assets/fr/007.webp)



Kliknite "**OK**": zvanični paket ekstenzija je sada instaliran na vašoj VirtualBox instanci!



![Image](assets/fr/008.webp)



Pređimo na kreiranje naše prve virtuelne mašine.



## IV. Kreiranje vaše prve VirtualBox VM



Da biste kreirali novu virtuelnu mašinu na VirtualBox-u, jednostavno kliknite na dugme "**New**" da pokrenete čarobnjak za kreiranje VM-a. Pošto je ovo prvi put da ste pokrenuli VirtualBox, želeo bih da vam dam još nekoliko detalja o Interface i ostalim dugmadima.





- Postavke**: opšta konfiguracija VirtualBox-a (podrazumevani VM folder, upravljanje ažuriranjima, jezik, NAT mreže, ekstenzije, itd.)
- Uvoz**: uvoz virtuelnog uređaja u OVF formatu
- Izvoz**: izvezite postojeću virtuelnu mašinu u OVF formatu da biste kreirali virtuelni uređaj
- Dodaj**: dodajte postojeću virtuelnu mašinu u vaš VirtualBox inventar, u standardnom VirtualBox formatu (.vbox) ili XML formatu



Sa levoj strane, odeljak "**Alati**" omogućava pristup **naprednim funkcijama, posebno za upravljanje virtuelnom mrežom, ali i za upravljanje skladištem VM-a**. Pod stavkom "**Alati**", vaše virtuelne mašine će biti dodate kasnije.



![Image](assets/fr/009.webp)



### A. Proces kreiranja VM-a



**Kao podsetnik, VirtualBox podržava mnoštvo operativnih sistema, uključujući Windows, Linux i BSD. U ovom primeru, kreiraću virtuelnu mašinu za Windows 11. Potrebno je popuniti nekoliko polja:**





- Ime**: ime virtuelne mašine (ovo je ime koje će biti prikazano u VirtualBox-u)
- Fascikla mašine**: gde čuvati virtuelnu mašinu, uzimajući u obzir da će podfascikla sa imenom VM-a biti kreirana na ovoj lokaciji
- Tip**: tip operativnog sistema, u zavisnosti od toga koji OS želite da instalirate
- Verzija**: verzija sistema koju želite instalirati, u ovom slučaju Windows 11, dakle "**Windows11_64**"



Kliknite "**Next**" da nastavite.



![Image](assets/fr/010.webp)



U zavisnosti od operativnog sistema koji odaberete u prethodnom koraku, **VirtualBox daje preporuke o resursima koje treba dodeliti virtuelnoj mašini**. Ovde govorimo o RAM-u koji želite dodeliti VM-u. Pretpostavimo 4 GB, jer se to zaista preporučuje za Windows 11, ali ako vam nedostaju resursi, navedite 2 GB umesto toga. **Nastavite



**Napomena**: resursi dodeljeni virtuelnoj mašini mogu biti izmenjeni kasnije.



![Image](assets/fr/011.webp)



Što se tiče virtuelnog Hard diska, počinjemo od nule, tako da treba da izaberemo "**Create virtual Hard disk now**" kako bi VM imao prostor za skladištenje za instalaciju operativnog sistema i čuvanje podataka. Kliknite na "**Create**".



![Image](assets/fr/012.webp)



VirtualBox podržava tri različita formata za virtuelne Hard diskove, što je velika razlika u poređenju sa drugim rešenjima kao što su VMware i Hyper-V. Postoje tri formata za izbor:





- VDI**, zvanični format za VirtualBox
- VHD**, koji je zvanični Hyper-V format, iako se novi VHDX format danas češće koristi
- VMDX** je zvanični VMware format za VMware Workstation i VMware ESXi



Da biste kreirali virtuelnu mašinu koja će se koristiti samo na ovoj instance VirtualBox-a, izaberite "**VDI**". S druge strane, ako će virtuelni Hard disk biti priključen na Hyper-V host kasnije, može biti dobra ideja da počnete sa VHD formatom kako biste izbegli potrebu za konvertovanjem. Kliknite na "**Next**".



![Image](assets/fr/013.webp)



**Virtuelni disk može biti dinamičan ili fiksne veličine**. Kada je dinamičan, fajl koji predstavlja **virtuelni disk (ovde .vdi fajl) će rasti kako se podaci upisuju na disk** dok ne dostigne svoju maksimalnu veličinu, ali se neće smanjiti ako se podaci obrišu. Suprotno tome, kada je fiksne veličine, **ukupni prostor za skladištenje se odmah dodeljuje (i stoga rezerviše)**, što omogućava nešto veću performansu, ali traje duže kada se virtuelni disk prvi put kreira.



Lično, za test virtuelne mašine sa VirtualBox-om, smatram da je režim "**Dinamički alocirano**" dovoljan.



![Image](assets/fr/014.webp)



**Sledeći korak je da navedete veličinu virtuelnog diska**, imajući na umu da će disk po defaultu biti sačuvan u VM direktorijumu (ovo se može promeniti u ovoj fazi). Naveo sam veličinu od 64 GB da bih ispunio zahteve za Windows 11, ali i ovde se može dodeliti manja veličina. Kliknite na "**Create**" da kreirate VM!



![Image](assets/fr/015.webp)



U ovom trenutku, VM je u našem inventaru, konfigurisan je, ali operativni sistem nije instaliran. Moramo finalizovati konfiguraciju VM-a pre nego što ga pokrenemo.



### B. Dodeljivanje ISO slike VirtualBox VM-u



Da bismo instalirali Windows 11 ili bilo koji drugi sistem, potrebni su nam izvori za instalaciju. U većini slučajeva koristimo disk imidž u ISO formatu za instalaciju operativnog sistema. **Potrebno je učitati Windows 11 ISO imidž u virtuelni DVD drajv naše VM**



Kliknite na VM u inventaru VirtualBox-a (1), zatim na dugme "**Configuration**" (2), što omogućava pristup opštoj konfiguraciji ove virtuelne mašine. Ovaj meni se koristi za upravljanje resursima (npr. povećanje RAM-a, konfiguracija CPU-a, itd.). Kliknite na "**Storage**" sa leve strane (3), na DVD drajv gde trenutno piše "**Empty**" (4) zatim kliknite na ikonu u obliku DVD-a (5) i "**Choose a disk file**".



![Image](assets/fr/016.webp)



Izaberite ISO sliku operativnog sistema koji želite da instalirate, zatim kliknite OK. Ovo je ono što dobijam:



![Image](assets/fr/017.webp)



Ostani u odeljku "**Configuration**" VM-a, još uvek imam nekoliko stvari da objasnim.



### C. VM mrežna veza



Idite na odeljak "**Mreža**" sa leve strane. Ovaj odeljak vam omogućava da upravljate mrežom virtuelne mašine: broj virtuelnih mrežnih interfejsa (do 4 po VM), MAC Address i režim pristupa mreži (NAT, pristup preko mosta, interna mreža, itd.). **Ako želite da vaša virtuelna mašina ima pristup internetu, izaberite "NAT" ili "Pristup preko mosta"**, ali ovaj drugi režim zahteva da DHCP server bude aktivan na vašoj mreži, ili ćete morati ručno da konfigurišete IP Address.



Napomena: Vratit ću se na deo o mreži detaljnije u posebnom članku.



![Image](assets/fr/018.webp)



### D. Broj virtuelnih procesora



Kao fizički računar, virtuelna mašina treba RAM, Hard disk i procesor da bi funkcionisala. Kada smo kreirali VM, možda ste primetili da čarobnjak nije uključio konfiguraciju procesora. Međutim, ovo se može konfigurisati u bilo kom trenutku putem kartice "**System**", zatim "**Processor**", gde možete izabrati broj virtuelnih procesora.



Napomena: opcija "**Enable VT-x/AMD-v nested**" je potrebna za ugnježdenu virtualizaciju.



U mom slučaju, virtuelna mašina ima 2 virtuelna procesora:



![Image](assets/fr/019.webp)



**Ne oklevajte da pogledate ostale delove menija za konfiguraciju.



### E. Prvo pokretanje i instalacija OS-a



Da biste pokrenuli virtuelnu mašinu, jednostavno je izaberite u inventaru i kliknite na dugme "**Start**". Otvoriće se drugi prozor koji pruža vizuelni pregled VM-a.



![Image](assets/fr/020.webp)



Jaoj, dobijam gadnu grešku i moja virtuelna mašina neće da se pokrene! Greška je "Login failed for virtual machine..." sa sledećim detaljima:



```shell
Not in a hypervisor partition (HPV=0)
AMD-V is disabled in the BIOS (or by the host OS)
```



Zapravo, ovo je normalno jer **funkcija virtualizacije nije omogućena na mom računaru**! Da biste ispravili ovaj problem, potrebno je da restartujete računar kako biste pristupili BIOS-u i omogućili virtualizaciju.



![Image](assets/fr/021.webp)



Bez čekanja, restartujem računar i **pritisnem taster "SUPPR" da pristupim BIOS-u** (taster može varirati u zavisnosti od mašine, i može biti F2, na primer) na mojoj ASUS matičnoj ploči. Da bih aktivirao virtualizaciju, "SVM Mode" mora biti omogućen u mom slučaju. I ovde, od jedne matične ploče do druge, od jednog proizvođača do drugog, naziv može da se promeni. Potražite funkciju koja se odnosi na **AMD-V** (za AMD procesor) ili **Intel VT-x** (za Intel procesor).



![Image](assets/fr/022.webp)



Jednom kada je ovo urađeno, sačuvajte izmene i restartujte fizičku mašinu... Ovog puta, **VirtualBox može pokrenuti virtuelnu mašinu** i učitati Windows ISO sliku za instalaciju operativnog sistema! 🙂



![Image](assets/fr/023.webp)



Na našem fizičkom hostu sa Windows 11, gde je instaliran VirtualBox, možemo videti da folder virtuelne mašine Windows 11 sadrži različite fajlove.





- VBOX** datoteka (u XML formatu) koja odgovara konfiguraciji VM-a (RAM, CPU, itd.)
- Datoteka VBOX-PREV** je rezervna kopija prethodne konfiguracije
- VDI** datoteka odgovara virtuelnom Hard disku u dinamičkom režimu, tako da trenutno ima samo 13 GB, dok je njegova maksimalna veličina 64 GB.
- Datoteka NVRAM** sadrži stanje BIOS-a virtuelne mašine, što je ekvivalentno neisparljivoj memoriji fizičke mašine.



![Image](assets/fr/024.webp)



## V. Zaključak



**VirtualBox je sada pokrenut na našem Windows 11 fizičkom računaru! Sve što preostaje je da ga iskoristimo i kreiramo virtuelne mašine!** Vratit ću se na instalaciju Windows 11 u VirtualBox VM u drugom članku. Za Windows 10, Windows Server ili Linux distribuciju (Ubuntu, Debian, itd.), samo nas pustite da vas vodimo!