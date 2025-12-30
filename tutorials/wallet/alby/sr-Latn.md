---
name: Alby

description: Ekstenzija pregledača za Bitcoin i Lightning Network
---

![cover](assets/cover.webp)




Olakšavanje plaćanja bitcoinom je izazov sa kojim se suočava mnogo kompanija u sektoru. Alby se izdvaja iz mase sa svojom Alby wallet ekstenzijom za pretraživače. Ova ekstenzija ima za cilj postavljanje fluidnog okvira koji automatski detektuje adrese i omogućava vam da izvršite plaćanja bitcoinom bez trenja. U ovom vodiču otkrivamo Alby ekstenziju i testiramo kako olakšava plaćanja iz pretraživača.




![video](https://youtu.be/nd5fX2vHuDw)




## Alby ekstenzija



Alby ekstenzija je alat koji omogućava vašem veb pregledaču da lako i sigurno komunicira sa Bitcoin mrežom i njenim Lightning Network slojem. Karakterišu je tri aspekta:




- Lightning Network wallet: Povežite svoj Alby čvor ili nalog za brzo i jeftino slanje i primanje bitcoina putem Lightning Network sloja.
- Fluidna plaćanja putem Weba: Eliminira potrebu za skeniranjem QR kodova ili prebacivanjem između aplikacija za bitcoin plaćanja na web stranicama koje podržavaju Lightning. Omogućava glatke transakcije jednim klikom, ili bez potvrde ako ste postavili budžet.
- Nostr menadžer: Ekstenzija upravlja vašim Nostr ključevima, olakšavajući povezivanje i interakciju sa Nostr aplikacijama koje deluju kao siguran potpisnik bez izlaganja vašeg privatnog ključa svakoj platformi.



https://planb.academy/tutorials/node/others/nostr-f6d21a64-9b04-4f21-ba1c-02c98cc91f98

https://planb.academy/tutorials/node/others/umbrel-nostr-7ae147e8-f5cd-46e1-861b-17c2ea1e08fd

## Povežite se na ekstenziju



U ovom vodiču, koristićemo ekstenziju Alby u pretraživaču Firefox pod operativnim sistemom Ubuntu. Međutim, dostupna je i na Windows-u i sa pretraživačima kao što je Chrome.



Možete dodati ekstenziju Alby u vaš pretraživač tako što ćete posetiti prodavnicu ekstenzija [Firefox] (https://addons.mozilla.org/fr/firefox/addon/alby/) ili prodavnicu ekstenzija [Chrome] (https://chromewebstore.google.com/detail/alby-bitcoin-wallet-for-l/iokeahhehimjnekafflcihljlcjccdbe).



![firefox](assets/fr/01.webp)



![chrome](assets/fr/02.webp)



ℹ️ Važno je proveriti da li je autor ekstenzije zaista zvanični Alby nalog, kako biste izbegli bilo kakav oblik piraterije ili krađe vaših bitkoina.



Dodajte ekstenziju u vaš pregledač klikom na dugme sa desne strane.


Dodelite potrebne dozvole za instalaciju i korišćenje ekstenzije, zatim zakačite ekstenziju na alatnu traku radi lakšeg pristupa.



![pin](assets/fr/03.webp)



Trebalo bi da definišete i kod za otključavanje (veoma važno), koji će garantovati siguran pristup vašem Lightning wallet iz vašeg pregledača. Predlažemo da postavite jaku alfanumeričku lozinku.



ℹ️ Sačuvajte ovu lozinku na sigurnom mestu kako biste mogli da joj pristupite ako je zaboravite, jer se može promeniti, ali ne i povratiti.



https://planb.academy/tutorials/computer-security/authentication/seedkeeper-password-64ffaf68-53aa-43c3-bc7a-c1dc2a17fee3

![pass](assets/fr/04.webp)



Alby pokazuje svoju prilagodljivost nudeći vam dva izbora:




- Nastavite sa Alby nalogom ako želite da uživate u aplikacijama dok zadržavate kontrolu nad svojim bitcoinima.
- Povežite svoj wallet ili Lightning čvor ako već imate jedan koji je podržan od strane ekstenzije.



https://planb.academy/tutorials/wallet/mobile/blink-7ea5f5a4-e728-4ff9-b3f9-cf20aa6fc2bd

https://planb.academy/tutorials/node/lightning-network/lightning-network-daemon-linux-59d777e9-72c8-4b32-8c50-e86cdae8f2f9

https://planb.academy/tutorials/business/point-of-sale/btcpay-server-928eb01e-824b-4b57-a3e8-8727633beddc


U ovom vodiču odlučujemo da nastavimo sa Alby nalogom kako bismo iskoristili prednosti funkcija Alby ekosistema.



https://planb.academy/tutorials/wallet/mobile/alby-go-40202802-b346-4a3c-9863-465c3bde9903

https://planb.academy/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a

Prijavite se na svoj Alby nalog ili kreirajte jedan ako ga još nemate.



![signup](assets/fr/05.webp)



## Pravljenje vaših prvih uplata



Kada se prijavite, možete kliknuti na Alby ekstenziju u alatnoj traci da pristupite svom portfoliju.



![buzzin](assets/fr/06.webp)



Kada kreirate svoj Alby nalog, biće potrebno da ga povežete sa wallet kako biste trošili satoshije. Da biste povezali bitcoin wallet sa svojim Alby nalogom, predlažemo da koristite Alby Hub čvor, koji možete ili postaviti na svom računaru ili se pretplatiti na plan koji nudi Alby.



![hubplan](assets/fr/13.webp)




U ovom vodiču, naš Alby nalog je podržan lokalnom instalacijom na našem računaru.


Da biste napravili svoj Alby čvor, preporučujemo naš Alby Hub vodič.



https://planb.academy/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a

Ovaj čvor vam omogućava da kreirate samostalne Lightning portfelje i efikasno upravljate vašim Lightning kanalima za slanje i primanje satoshija.



![channels](assets/fr/14.webp)



Otvorite kanale prijema koji definišu ukupan broj satoshija koje možete primiti.



![receivechanal](assets/fr/15.webp)



Otvorite kanale za slanje blokiranjem satoshija na bitcoin onchain adresi. Satoshiji koje ste blokirali definišu ukupne satoshije koje možete potrošiti.



![spend](assets/fr/16.webp)



Sada možete slati i primati satoshije putem Alby ekstenzije.



![exchange](assets/fr/08.webp)



Od ovog trenutka, ekstenzija Alby može da detektuje Lightning adrese i fakture dostupne na veb stranicama koje posećujete, i predložiće vam da ih platite u bitkoinima ili putem Lightning-a direktno iz vaše ekstenzije.



![suggest](assets/fr/09.webp)



![pay](assets/fr/10.webp)




## Osiguravanje ključeva za oporavak glavnim ključem



Glavni ključ koji nudi ekstenzija Alby deluje kao zaštitni sloj koji vam omogućava da komunicirate sigurno sa glavnim Bitcoin mrežnim slojem (Onchain), sistemom Nostr i omogućava vam da aktivirate Lightning vezu sa Nostr aplikacijama.



![masterKey](assets/fr/11.webp)



Ovaj glavni ključ ima oblik 12 reči sličnih vašoj frazi za oporavak. Stoga preporučujemo da ga čuvate koristeći sigurne metode kako biste osigurali da mu možete pristupiti u bilo kom trenutku.



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270


![masterKey](assets/fr/12.webp)



Sada možete iskusiti besprekorno plaćanje bitcoinom i Lightning-om uz Alby ekstenziju. Ako vam se dopao ovaj vodič, preporučujemo naš Alby Hub vodič za postavljanje sopstvenog Alby čvora i kontrolu svih aspekata vaših Alby novčanika putem glatkog i moćnog interfejsa.



https://planb.academy/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a