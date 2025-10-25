---
name: Blue Wallet

description: Bitcoin Radikalno Jednostavan i Moćan Portfolio
---
![cover](assets/cover.webp)



Početak rada sa Bitcoin čini se velikim izazovom za ljude koji su skeptični u pogledu jednostavnosti njegove upotrebe. Pronalaženje pravih alata za osiguranje te jednostavnosti stoga postaje od najveće važnosti za bolje prihvatanje Bitcoin kao medijuma Exchange, a ne samo kao skladišta vrednosti.



U ovom vodiču ćemo pogledati Blue Wallet, jednostavan ali veoma efikasan Bitcoin Wallet koji vam omogućava da lično upravljate svojim bitcoinima i takođe da kreirate upravljačke zadruge zasnovane na [Multisig](https://planb.network/resources/glossary/multisig) (ne brinite, vratićemo se na to).



![Vidéo tutoriel Blue Wallet](https://www.youtube.com/watch?v=UCAtFgkdJtM)



## Početak sa Blue Wallet



Plavi Wallet je open source, samostalni Bitcoin Wallet koji vam omogućava da preuzmete kontrolu nad svojim bitcoinima. Dostupan je kao mobilna aplikacija na Android i iOS platformama. U ovom vodiču ćemo se bazirati na Android verziji, međutim, svi procesi koji će biti razvijeni jednako su validni na iOS-u.



![download](assets/fr/01.webp)



⚠️ Please make sure to download the Blue Wallet Bitcoin Wallet application on an official platform to guarantee its authenticity and protect your bitcoins from possible leaks and hacks.



Kada instalirate, možete kreirati novi Wallet i sačuvati 12 reči za oporavak, ili uvesti postojeći Bitcoin Wallet. Saznajte kako da napravite efikasan bekap vaših ključnih reči kako ne biste izgubili pristup vašim bitkoinima.



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Sa Blue Wallet možete kreirati odvojene, posvećene Bitcoin portfelje. Na primer, možete imati jedan Wallet za vašu štednju i drugi za vaše dnevne troškove, sve u istoj aplikaciji.



![home](assets/fr/02.webp)



## Tipovi portfolija



U Blue Wallet, pronaći ćete dve izvorne Bitcoin vrste portfolija.



### Bitcoin portfolio



Ako ste navikli na druge Bitcoin portfelje kao što su Phoenix ili Aqua, uopšte nećete biti van koraka na Interface sa Blue Wallet Bitcoin portfeljem.



https://planb.network/tutorials/wallet/mobile/phoenix-0f681345-abff-4bdc-819c-4ae800129cdf


https://planb.network/tutorials/wallet/mobile/aqua-8e6d7dd3-8c03-45cc-90dd-fe3899a7d125

Plavi Wallet's Bitcoin Wallet predstavlja standardni Wallet u ekosistemu Bitcoin. Možete trošiti bitkoine sve dok posedujete reči za oporavak koje će obezbediti važeći potpis na mreži kako bi se potvrdilo da posedujete bitkoine.



Da biste kreirali Bitcoin portfolio, kliknite na dugme **Dodaj sada**, unesite naziv vašeg portfolija i izaberite tip Bitcoin.



![bitcoin-wallet](assets/fr/03.webp)



Kada kliknete na pregled Bitcoin Wallet, moći ćete da vidite istoriju transakcija i šaljete i primate bitkoine.



⚠️ Sve transakcije u vašem Bitcoin Wallet su na glavnom lancu protokola Bitcoin (Mainnet).





- Primanje bitkoina sa Bitcoin Blue Wallet Wallet je intuitivno. Na dnu ekrana, kliknite na dugme **Receive**. Podelite QR kod ili vaš Bitcoin Address sa pošiljaocem kako bi vam mogli poslati bitkoine.



Takođe možete konfigurisati unapred definisanu količinu da biste odredili količinu Bitcoin koju želite da primite.



![receive-bitcoin](assets/fr/04.webp)





- Na dugmetu **Pošalji**, pošaljite bitkoine na Bitcoin Address, postavljajući željeni iznos i potvrđujući transakciju.



![send-bitcoin](assets/fr/05.webp)



Plavi Wallet vam omogućava da konfigurišete parametre vaše Bitcoin pošiljke kako želite.



Stoga možete odabrati odnos naknade za transakciju koji vam odgovara ako želite da vaša transakcija bude brzo potvrđena u Mempool i uključena u blok od strane rudara. U zavisnosti od odnosa koji odaberete, rudari će vašu transakciju prioritetizovati u većoj ili manjoj meri. Saznajte više u našem Mempool Space vodiču.



https://planb.network/tutorials/privacy/analysis/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f

![feerate](assets/fr/06.webp)





- Sa Blue Wallet, možete dodati više primalaca u jednu pošiljku.



Kada dodate Bitcoin Address vašeg prvog primaoca, u opcijama kliknite na **Dodaj primaoca**, dodajte Bitcoin Address i zatim postavite iznos koji će biti poslat ovom primaocu, i tako dalje. Plavi Wallet će poslati bitkoine za više pošiljki na osnovu vaše jedne akcije.



![add-recipients](assets/fr/07.webp)



Možete ukloniti jednog ili sve primaoce klikom na **Ukloni primaoca** i **Ukloni sve primaoce**.



![remove-recipient](assets/fr/08.webp)





- **Povećaj naknade**: Da li ste napravili transakciju kojoj treba dugo da bude potvrđena? Omogućavanjem povećanja naknada možete dodati dodatne naknade za transakciju koja je na čekanju kako biste ubrzali njenu potvrdu.



![bumping](assets/fr/09.webp)



### Multisig Portfolio



Multisig (multi-signature) Wallet predstavlja Wallet kreiran iz grupisanja određenog broja (minimum 2) Bitcoin novčanika. U ovoj vrsti Wallet, u zavisnosti od konfiguracije i odabrane metode, trošenje bitkoina postaje kolektivna i kooperativna akcija.



U Blue Wallet, možete kreirati portfelje sa više potpisa za vaše udruženje, vašu porodicu, vašu kompaniju. Kroz ovaj deo, istražićemo svaki aspekt ovog posebnog tipa portfelja.



Dodajte novi portfolio i izaberite tip **Multisig Vault** za kreiranje portfolija sa više potpisa.



![multisig-vault](assets/fr/10.webp)



Definišite m-de-n konfiguraciju u vašoj organizaciji sa više potpisa klikom na **Vault Settings**.



⚠️ U m-of-n konfiguraciji, **m** predstavlja minimalan broj potpisa potrebnih za odobravanje transakcije, a **n** broj portfolija u vašoj organizaciji.



Obavezno definišite minimalan broj potpisa (m) za većinu vaše organizacije. Na primer, konfiguracija sa više potpisa 2-od-3 zahteva da dva novčanika u vašoj organizaciji potpišu transakciju pre nego što se može izvršiti.



❗Definisanje m-of-n konfiguracije gde je n jednako m predstavlja veliki rizik. Kada član izgubi pristup svom Wallet, gubite ovlašćenje za trošenje bitkoina u Wallet.



Evo nekoliko primera optimalnih konfiguracija za obezbeđivanje sigurnosti i pristupačnosti bitkoina:





- 2-od-3 multi signature.





- 5-od-7 multi signature.



![vault-settings](assets/fr/11.webp)



Pridržavajte se najbolje prakse odabirom P2WSH formata.



❗ **[P2WSH](https://planb.network/resources/glossary/p2wsh) ili Pay to Witness Script Hash** je metoda zaključavanja koja zaključava odlazne bitkoine vaše transakcije (Izlazi) na Hash prilagođenog skripta koji postavlja Blue Wallet. Glavna prednost ovog tipa zaključavanja je što smanjuje veličinu podataka transakcije i implicitno vam omogućava da platite niže naknade za transakciju.



Kreirajte ili uvezite svaki od **n** portfolija u vašoj konfiguraciji. U našem vodiču ćemo koristiti konfiguraciju sa više potpisa 2-od-3. Obavezno sačuvajte reči za oporavak za svaki portfolio pojedinačno.



![vault-keys](assets/fr/12.webp)





- Primite bitkoine



Na vašoj Multisig Wallet stranici, pronaći ćete istoriju transakcija i dugmad za Primanje i Slanje.



Primanje bitkoina u multi-signature Wallet je isti proces kao kada ste u standardnom Bitcoin Wallet.





- Pošalji **bitkoine**:



Upravljanjem multi-potpisom Wallet, trošenje bitkoina postaje složena akcija, bilo sa drugim ljudima ili sa drugim vašim Wallet. Jedan potpis vašeg Wallet više nije dovoljan. Ovo dodaje Layer sigurnosti vašim bitkoinima, jer zlonamerna osoba neće moći da potroši te bitkoine kada dođe u posed samo jednog od vaših privatnih ključeva.



Kao standardni Bitcoin portfelj Blue Wallet, možete definisati više primalaca u opciji **Dodaj primaoce**.



Kada validirate svoju transakciju, biće vam potreban drugi potpis da biste odobrili trošenje bitkoina. Zapamtite, nalazimo se u 2-od-3 multi-potpisnoj konfiguraciji.



Drugi potpisnik Wallet, ako je i korisnik, može potpisati transakciju čak i ako nije povezan na Internet (nema Wi-Fi, nema mobilne podatke) skeniranjem QR koda [delimično potpisane transakcije](https://planb.network/resources/glossary/psbt) koju ste upravo kreirali.



![mutisig-send](assets/fr/13.webp)





- Idite dalje sa portfoliom sa više potpisa:



Na Interface vašeg multi-signature Wallet, kliknite na dugme **Manage keys**.



Zaboravljanjem jedne od reči za oporavak jednog od portfelja potpisnika (**Zaboravi ovaj seed...**), obaveštavate Plavi Wallet da izbriše rezervnu kopiju ovih reči iz svoje memorije. Stoga ćete napraviti eksternu rezervnu kopiju.



![revoke-key](assets/fr/14.webp)



Izvođenjem ove radnje zadržavate samo javni ključ povezan sa ovim rečima za oporavak.



⚠️ Čuvanje samo javnih ključeva (XPUB) omogućava vam dodavanje dodatnog nivoa sigurnosti vašoj 2-od-3 multi-potpisnoj konfiguraciji. Zaista, može biti štetno držati sve reči za oporavak na jednom mestu kada je vaš telefon pod napadom. Napadači sa pristupom samo jednom **VAULT** (ključna reč) koji koristite za potpisivanje vaših transakcija, neće moći da ukradu vaše bitkoine (potrebno je najmanje 02 potpisa) jer se javni ključevi ne mogu koristiti za potpisivanje transakcija.



## Više opcija sa Blue Wallet



### Poboljšanje sigurnosti pristupa portfoliju



U podešavanjima, opcija **Bezbednost** omogućava vam da definišete korišćenje otiska prsta za obavljanje transakcije, izvoz ili brisanje vašeg Wallet. Ovo potvrđuje identitet osobe koja koristi vaš pametni telefon.



![biometry](assets/fr/15.webp)



## Aktiviraj Lightning Network



Lightning Network više nije nativno podržan u aplikaciji Blue Wallet.



U Podešavanjima > **Lightning Podešavanja**, možete ručno povezati vaš Lightning Wallet kada pokrećete Lightning Network Daemon (LND) čvor. Instalirajte LND Hub, zatim povežite vaš Wallet unosom linka generisanog od strane Huba.



![ln](assets/fr/16.webp)



https://planb.network/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

https://planb.network/tutorials/node/lightning-network/lightning-network-daemon-linux-59d777e9-72c8-4b32-8c50-e86cdae8f2f9

Sada ste završili obilazak Blue Wallet, spremni da koristite Bitcoin u svoj njegovoj jednostavnosti i snazi. Preporučujemo da napravite sledeći korak i saznate kako možete prihvatiti Bitcoin uplate u vašim prodavnicama, zahvaljujući snazi Lightning-a.



https://planb.network/tutorials/wallet/mobile/breez-46a6867b-c74b-45e7-869c-10a4e0263c06