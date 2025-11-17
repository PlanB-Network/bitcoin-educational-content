---
name: Ashigaru Terminal
description: Koristite Ashigaru na desktopu za pravljenje coinjoin-a
---

![cover](assets/cover.webp)



Ashigaru Terminal je adaptacija Sparrow Servera od strane tima Ashigaru, koja implementira Whirlpool coinjoin protokol. Ovaj softver je nastavak rada započetog od strane Samourai Wallet, posebno na Whirlpool GUI, čije osnovne principe usvaja: samostalno čuvanje i očuvanje poverljivosti.



Ovaj softver je fork od Sparrow Servera, modifikovan i optimizovan za punu integraciju sa Whirlpool ekosistemom, ZeroLink coinjoin protokolom koji su originalno razvili timovi Samourai.



Ashigaru Terminal radi iz minimalističkog TUI interfejsa i može se koristiti na ličnom računaru ili na posvećenom serveru. Omogućava vam direktnu interakciju sa Whirlpool za pokretanje "*Tx0*", upravljanje "*Deposit*", "*Premix*", "*Postmix*" i "*Badbank*" nalozima, kao i izvođenje automatskih remiksa kako biste ojačali poverljivost vaših delova.



Ukratko, Ashigaru Terminal će biti posebno koristan ako želite kreirati coinjoin-ove koristeći Whirlpool.



U ovom prvom vodiču, provesti ću vas kroz instalaciju i rad Ashigaru Terminala. Drugi, napredniji vodič će biti posvećen stvarnom kreiranju coinjoin-a.



https://planb.academy/tutorials/privacy/on-chain/ashigaru-whirlpool-e566803d-ab3f-4d98-9136-5462009262ef

## 1. Instalirajte Ashigaru Terminal



Da biste instalirali Ashigaru Terminal, trebat će vam Tor Browser, jer se binarne datoteke distribuiraju samo putem Tor mreže. Ako to već niste učinili, [instalirajte ga na svoj uređaj](https://www.torproject.org/download/).



### 1.1. preuzmi Ashigaru Terminal



Iz Tor Browser-a, idite na [stranicu sa izdanjima njihovog Git repozitorijuma](http://ashicodepbnpvslzsl2bz7l2pwrjvajgumgac423pp3y2deprbnzz7id.onion/Ashigaru/Ashigaru-Terminal/releases/) da preuzmete najnoviju verziju Ashigaru Terminal-a za vaš operativni sistem.



```txt
ashicodepbnpvslzsl2bz7l2pwrjvajgumgac423pp3y2deprbnzz7id.onion/Ashigaru/Ashigaru-Terminal/releases/
```



![Image](assets/fr/01.webp)



Preuzmite sledeće 2 datoteke za vaš operativni sistem:




- Binarni fajl (`ashigaru_terminal_v1.0.0_amd64.deb` za Debian/Ubuntu, `.dmg` za macOS ili `.zip` za Windows) ;
- Potpisana datoteka heševa: `ashigaru_terminal_v1.0.0_signed_hashes.txt`.



### 1.2. Proveri Ashigaru Terminal



Pre nego što pokrenete softver na svom uređaju, potrebno je da proverite njegovu autentičnost i integritet. Ovo je važan korak, jer vas sprečava da instalirate lažnu verziju koja bi mogla ugroziti vaše bitkoine ili zaraziti vaš uređaj.



Otvorite novu karticu pregledača i idite na [Keybase verification tool](https://keybase.io/verify). Zalepite sadržaj `.txt` fajla koji ste upravo preuzeli u predviđeno polje, zatim kliknite na dugme `Verify`.



![Image](assets/fr/02.webp)



Da biste diversifikovali svoje izvore verifikacije, možete takođe uporediti poruku sa onom dostupnom na clearnet sajtu [ashigaru.rs](https://ashigaru.rs/download/), u odeljku `/download`.



![Image](assets/fr/03.webp)



Ako je potpis važeći, Keybase će prikazati poruku koja potvrđuje da su datoteku potpisali Ashigaruovi programeri.



![Image](assets/fr/04.webp)



Možete takođe kliknuti na profil `ashigarudev` prikazan od strane Keybase i proveriti da li se njihov otisak ključa tačno poklapa: `A138 06B1 FA2A 676B`.



![Image](assets/fr/05.webp)



Ako se greška pojavi u ovoj fazi, potpis je nevažeći. U tom slučaju, **ne instalirajte preuzeti softver**. Počnite ponovo od početka ili zatražite pomoć od zajednice pre nego što nastavite.



Keybase vam je obezbedio autentifikovani hash aplikacije. Sada ćemo proveriti da li se hash preuzetog `.deb`, `.zip` ili `.dmg` fajla poklapa sa onim koji je validiran na Keybase. Da biste to uradili, idite na [HASH FILE ONLINE](https://hash-file.online/).



Kliknite na dugme `BROWSE...` i izaberite `.deb`, `.zip` ili `.dmg` fajl preuzet u koraku 1.1. Zatim izaberite `SHA-256` heš funkciju i kliknite na `CALCULATE HASH` da biste generate heš za vaš fajl.



![Image](assets/fr/06.webp)



Sajt će zatim prikazati hash softvera. Uporedite ga sa hashom koji ste verifikovali na Keybase.io. Ako se ta dva savršeno poklapaju, provera autentičnosti i integriteta je uspešna. Tada možete koristiti softver.



![Image](assets/fr/07.webp)



### 1.3 Pokreni Ashigaru Terminal





- Debian / Ubuntu



Da biste instalirali softver, pokrenite komandu :



```bash
cd ~/Downloads
sudo apt install ./ashigaru_terminal_v1.0.0_amd64.deb
```



Izmeni redosled prema preuzetoj verziji.



Zatim proverite instalaciju:



```bash
/opt/ashigaru-terminal/bin/Ashigaru-terminal --version
```



Zatim pokrenite softver:



```bash
/opt/ashigaru-terminal/bin/Ashigaru-terminal
```





- Windows**



Desni klik na preuzetu i proverenu `.zip` datoteku, zatim izaberite `Extract All...` da biste izdvojili njen sadržaj.



Kada je ekstrakcija završena, dvaput kliknite na datoteku `Ashigaru-terminal.exe` da pokrenete softver.



![Image](assets/fr/08.webp)



## 2. Početak rada sa Ashigaru Terminalom



Ashigaru Terminal je TUI (*Text-based User Interface*) program, tj. minimalistički interfejs koji se pokreće direktno u terminalu. Interakcija sa njim se odvija putem menija i prečica na tastaturi, ali bez klasičnog grafičkog okruženja.



![Image](assets/fr/09.webp)



Lako je koristiti: koristite strelice na tastaturi za navigaciju kroz menije, i pritisnite taster `Enter` da potvrdite akciju ili izbor.



## 3. Povezivanje vašeg čvora sa Ashigaru Terminalom



Podrazumevano, Ashigaru Terminal se povezuje na javni Electrum server. Ovo očigledno predstavlja rizike u pogledu poverljivosti i suvereniteta. Zato ćemo ga konfigurisati da se povezuje direktno na vaš sopstveni Electrum Server.



Da biste to uradili, otvorite meni `Preferences > Server`.



![Image](assets/fr/10.webp)



Kliknite na dugme `< Edit >`.



![Image](assets/fr/11.webp)



Odaberite `Private Electrum Server`, zatim kliknite `<Continue>`.



![Image](assets/fr/12.webp)



Unesite URL i port vašeg servera. Možete navesti Tor adresu u `.onion`. Zatim kliknite na `< Test >` da biste proverili vezu.



![Image](assets/fr/13.webp)



Ako je veza uspešna, pojaviće se poruka `Success`, zajedno sa detaljima vašeg servera.



![Image](assets/fr/14.webp)



Ako još uvek nemate Bitcoin čvor, preporučujem da pohađate ovaj kurs:



https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426

*U mom slučaju, za ovaj tutorijal, odvojiću se od mog Electrs servera jer radim na testnetu. Međutim, operacija ostaje potpuno identična na mainnet.*



## 4. Kreiraj portfolio na Ashigaru Terminalu



Sada kada je softver pravilno konfigurisan, možemo dodati Bitcoin portfolio.



Imate dve opcije:




- Možete kreirati novi wallet od nule i koristiti ga isključivo na Ashigaru Terminalu. U ovom slučaju, biće potrebno da otvorite ovaj softver svaki put kada želite da komunicirate sa svojim wallet;
- Alternativno, možete uvesti svoj postojeći Ashigaru wallet direktno sa telefona u Ashigaru Terminal. Nedostatak ove metode je što blago smanjuje sigurnost vašeg sistema, jer je vaš wallet tada izložen dvema rizičnim okruženjima umesto jednom. S druge strane, nudi prednost mogućnosti da ostavite Ashigaru Terminal da radi neprekidno kako bi mešao vaše kovanice, dok vam omogućava da ih trošite na daljinu putem Ashigaru mobilne aplikacije.



U ovom vodiču, odlučićemo se za drugu metodu. Međutim, ako biste radije kreirali potpuno novi portfolio, postupak ostaje isti: jedina razlika će biti tokom kreiranja, kada ćete morati da sačuvate svoju novu mnemoniku i svoj novi passphrase.



Takođe imajte na umu da Ashigaru Terminal ne omogućava direktno trošenje vaših bitkoina. Možete sinhronizovati isti novčanik na Ashigaru Terminalu i aplikaciji Ashigaru (što ću uraditi u ovom tutorijalu), ili na Sparrow Walletu.



Ako još uvek nemate wallet na Ashigaru aplikaciji, možete pratiti posvećeni vodič :



https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f

Idite na meni `Wallets`.



![Image](assets/fr/15.webp)



Zatim izaberite `Create / restore wallet...`. Opcija `Open Wallet...` vam omogućava pristup portfoliju koji je već sačuvan u Ashigaru Terminalu za kasniji datum.



![Image](assets/fr/16.webp)



Dajte svom portfoliju ime.



![Image](assets/fr/17.webp)



Zatim izaberite tip portfolija `Hot Wallet`.






![Image](assets/fr/18.webp)



U ovoj fazi se postupak razlikuje u zavisnosti od vašeg početnog izbora:




- Ako želite da kreirate novi portfolio od nule, kliknite na `<Generate New Wallet>`, definišite passphrase BIP39, zatim pažljivo sačuvajte vašu mnemonicku frazu i vaš passphrase na fizičkom mediju ;



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270



- Ako želite da koristite isti wallet kao vašu Ashigaru aplikaciju, unesite 12 reči vaše mnemoničke fraze i vaš passphrase BIP39 direktno u odgovarajuća polja. Napišite reči malim slovima, cele, redom, odvojene razmakom, bez brojeva ili dodatnih karaktera.



Kada je ovaj korak završen, kliknite `< Next >`.



*Napomena*: Ako ne možete kliknuti na ovo dugme, vaša mnemonička fraza je nevažeća. Pažljivo proverite da nijedna reč nije netačna ili pogrešno napisana.



![Image](assets/fr/19.webp)



Zatim ćete morati postaviti lozinku. Ovo će se koristiti za otključavanje vašeg Ashigaru Terminal wallet i zaštitu od neovlašćenog fizičkog pristupa. Nije uključeno u kriptografsku derivaciju vaših ključeva: drugim rečima, čak i bez ove lozinke, svako ko ima vašu mnemoniku i passphrase moći će da obnovi vaš wallet i pristupi vašim bitcoinima.



Izaberite dugu, složenu, nasumičnu lozinku. Sačuvajte kopiju na sigurnom mestu: idealno na fizičkom mediju ili u sigurnom menadžeru lozinki.



Kliknite `< OK >` kada završite.



![Image](assets/fr/20.webp)



## 5. Koristeći portfolio



Možete zatim izabrati kojem nalogu želite pristupiti. Za sada, nismo pokrenuli nikakve mešavine, tako da ćemo pristupiti nalogu `Deposit`.



![Image](assets/fr/21.webp)



Operacija je tada identična onoj kod Sparrow, pošto je Ashigaru Terminal fork Servera Sparrow. Naći ćete iste menije:



![Image](assets/fr/22.webp)





- transakcije": omogućava vam da pregledate istoriju transakcija povezanih sa ovim nalogom. U mom slučaju, neke od njih se već pojavljuju, jer sam ih napravio sa Ashigaru aplikacijom na ovom istom wallet.



![Image](assets/fr/23.webp)





- receive`: generiše novu, praznu adresu za prijem za postavljanje satss na depozitni račun.



![Image](assets/fr/24.webp)





- addresses`: prikazuje listu svih vaših adresa, bilo da pripadaju internom ili eksternom lancu vašeg naloga.



![Image](assets/fr/25.webp)





- `UTXOs`: prikazuje sve vaše dostupne UTXO-e.



![Image](assets/fr/26.webp)





- `Settings`: daje pristup vašem portfoliju *descriptor*. Takođe možete konsultovati vaš seed, prilagoditi *Gap Limit* ili promeniti datum kreiranja vašeg portfolija.



![Image](assets/fr/27.webp)



Sada znate kako da instalirate i koristite Ashigaru Terminal. U narednom tutorijalu videćemo kako da izvršite coinjoin pomoću ovog softvera i kako da upravljate sredstvima u "*Postmix*".
https://planb.academy/tutorials/privacy/on-chain/ashigaru-whirlpool-e566803d-ab3f-4d98-9136-5462009262ef
