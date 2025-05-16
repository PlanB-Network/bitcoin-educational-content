---
name: Bitcoin Core (macOS & Windows)
description: Instalirajte Bitcoin Core na Mac ili Windows
---

Instaliranje Bitcoin Core na vašem običnom računaru može biti izvedeno, ali nije idealno. Ako vam ne smeta da ostavite računar uključen 24/7, onda će ovo raditi dobro. Ako morate da isključujete računar, može biti iritantno čekati da se softver sinhronizuje svaki put kada ga ponovo uključite.


Ova uputstva su za korisnike Mac ili Windows sistema. Korisnicima Linux-a verovatno neće trebati moja pomoć, ali uputstva za Linux su vrlo slična onima za Mac.


## Počni Čisto


Idealno, želite koristiti čist računar, onaj bez malvera. Čak i ako koristite Hardware Wallet, malver vas može prevariti i oduzeti vam novčiće.


Možete ili obrisati stari računar i koristiti ga kao posvećen Bitcoin računar, ili kupiti posvećen računar/laptop.


## Hard Drive


Bitcoin Core će zauzeti oko 400 gigabajta podataka na vašem disku i nastaviće da raste. Možete koristiti svoj interni disk, ali možete takođe priključiti eksterni Hard disk. Objasniću obe opcije. Idealno bi bilo da koristite SSD disk. Ako imate stari računar, verovatno nema jedan od ovih diskova interno. Samo kupite eksterni SSD od 1 ili 2 terabajta i koristite to. Običan disk će verovatno raditi, ali možete naići na probleme i biće mnogo sporiji.


![image](assets/1.webp)


## Preuzmi Bitcoin Core


Idite na Bitcoin.org (pazite da ne odete na Bitcoin.com, što je sajt za shitcoin u vlasništvu Rogera Vera, koji vara ljude da kupe Bitcoin Cash umesto Bitcoin)


Jednom tamo, čudno je da nije očigledno gde preuzeti softver. Idite na meni resursa i kliknite na „Bitcoin Core“, kao što je prikazano ispod:


![image](assets/2.webp)


Ovo će vas dovesti do stranice za preuzimanje:


![image](assets/3.webp)


Kliknite na narandžasto dugme Preuzmi Bitcoin Core:


![image](assets/4.webp)


Postoji nekoliko opcija koje možete izabrati, u zavisnosti od vašeg računara. Prve dve su relevantne za ovaj vodič; izaberite Windows ili Mac na levoj traci. Počeće preuzimanje nakon što kliknete, najverovatnije u vaš direktorijum Preuzimanja.


## Potvrdite preuzimanje (deo 1)


Treba vam fajl koji sadrži heševe različitih izdanja. Ovaj fajl je nekada bio na stranici za preuzimanje Bitcoin.org, ali sada je premešten na bitcoincore.org/en/download:


![image](assets/5.webp)


Treba vam datoteka sa SHA256 binarnim hešovima. Ova datoteka sadrži SHA256 hešove različitih paketa za preuzimanje Bitcoin Core.


Dalje, treba da Hash preuzmemo Bitcoin Core i uporedimo ga sa onim što fajl kaže da Hash treba da bude. Onda znamo da je preuzimanje identično onome što se očekuje, prema bitcoincore.org.


Ponovo idite u direktorijum Downloads i izvršite ovu komandu (zamenite X-ove tačnim nazivom datoteke za preuzimanje Full node Bitcoin):


```bash
shasum -a 256 XXXXXXXXXXXX # <--- FOR MAC
certutil -hashfile XXXXXXXXXXX SHA256 # <--- FOR WINDOWS
```


Dobićete Hash izlaz. Zabeležite ga i uporedite sa Hash sadržanim u SHA256SUMS datoteci.


Ako su izlazi identični, onda ste potvrdili da nijedan bit podataka nije izmenjen… skoro. Još uvek moramo biti sigurni da datoteka SHA256SUMS nije zlonamerna.


Da bismo nastavili sa sledećim korakom, moramo imati instaliran gpg na našem računaru.


Da biste to uradili, pogledajte moj vodič za SHA256/gpg i skrolujte otprilike do polovine do odeljka “Download gpg”, i potražite podnaslov vašeg operativnog sistema. Zatim se vratite ovde.


## Nabavite javni ključ


Vratite se na stranicu za preuzimanje, preuzmite datoteku sa SHA256 Hash potpisima


![image](assets/6.webp)


Kliknite na to i sačuvajte datoteku na disk, po mogućstvu u direktorijum Preuzimanja.


Ova datoteka sadrži potpise različitih osoba, datoteke SHA256SUMS.


Želimo javni ključ glavnog programera, Wladimir J. van der Laan, na ključaru našeg računara. ID njegovog javnog ključa je:

1 - 01EA 5486 DE18 A882 D4C2 6845 90C8 019E 36C2 E964


Žao mi je, ali ne mogu da ispunim taj zahtev.


```bash
gpg --keyserver hkp://keyserver.ubuntu.com --recv-keys 01EA5486DE18A882D4C2684590C8019E36C2E964
```


Iz radoznalosti, u bilo kom trenutku, možete videti koji ključevi se nalaze u privesku za ključeve računara pomoću ove komande:


```bash
gpg --list-keys
```


## Potvrdite preuzimanje (deo 2)


Imamo javni ključ, tako da sada možemo verifikovati SHA256SUMS datoteku koja sadrži heševe Bitcoin Core preuzimanja i potpis za te heševe.


Otvorite Terminal ili CMD ponovo i uverite se da ste u direktorijumu Downloads. Odatle izvršite ovu komandu:


```bash
gpg –verify SHA256SUMS.asc SHA256SUMS
```


Prva navedena datoteka je tačan pravopis datoteke sa potpisom. Druga navedena datoteka treba da bude tačan pravopis tekstualne datoteke koja sadrži heševe. Oba fajla treba da budu u istom direktorijumu i morate biti u direktorijumu fajlova, inače morate uneti punu putanju za svaki fajl.


Ovo je izlaz koji biste trebali dobiti


![image](assets/7.webp)


Bezbedno je ignorisati poruku UPOZORENJA – ona vas samo podseća da niste sreli Wladimira na ključnom mestu i lično ga pitali koji je njegov javni ključ, a zatim rekli vašem računaru da potpuno veruje tom ključu.


Ako ste dobili ovu poruku, sada znate da datoteka SHA256SUMS.asc nije bila izmenjena nakon što ju je Wladimir potpisao.


## Instaliraj Bitcoin Core


Ne bi trebalo da vam trebaju detaljna uputstva za instalaciju programa.


![image](assets/8.webp)


## Pokreni Bitcoin Core


Na Mac-u, možda ćete dobiti upozorenje (Apple je i dalje protiv-Bitcoin)


![image](assets/9.webp)


Kliknite OK, a zatim otvorite Postavke sistema.


![image](assets/10.webp)


Kliknite na ikonu Bezbednost i privatnost:


![image](assets/11.webp)


Zatim kliknite „otvori svejedno“:


![image](assets/12.webp)


Greška će se ponovo pojaviti, ali ovog puta ćete imati dostupno dugme OPEN. Kliknite ga.


![image](assets/13.webp)


Bitcoin Core treba da se učita i biće vam predstavljene neke opcije:


![image](assets/14.webp)


Ovde možete izabrati da koristite podrazumevanu putanju za preuzimanje Blockchain, ili možete izabrati vaš eksterni disk. Preporučujem da ne menjate podrazumevanu putanju ako ćete koristiti interni disk, jer to olakšava postavljanje kada instalirate drugi softver za komunikaciju sa Bitcoin Core.


Možete izabrati da pokrenete pruned node, štedi prostor, ali ograničava šta možete raditi sa svojim node-om. U svakom slučaju, preuzećete ceo Blockchain i verifikovati ga, tako da, ako imate prostora, zadržite ono što ste preuzeli i ne radite pruning ako to možete izbeći.


Kada potvrdite, Blockchain će početi sa preuzimanjem. To će trajati mnogo dana.


![image](assets/15.webp)


Možete isključiti računar i vratiti se da preuzmete ako želite, neće napraviti nikakvu štetu.