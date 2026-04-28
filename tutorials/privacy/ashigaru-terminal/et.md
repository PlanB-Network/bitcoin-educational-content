---
name: Ashigaru Terminal
description: Kasutage Ashigaru töölaual, et teha coinjoins
---

![cover](assets/cover.webp)



Ashigaru Terminal on Ashigaru meeskonna poolt kohandatud Sparrow Server, mis rakendab Whirlpool coinjoin-protokolli. See tarkvara on jätkuks Samourai Wallet poolt alustatud tööle, eelkõige Whirlpool GUI-le, mille aluspõhimõtteid ta võtab üle: isehaldamine ja konfidentsiaalsuse säilitamine.



See tarkvara on Sparrow serveri fork, mis on muudetud ja optimeeritud täielikuks integreerimiseks Whirlpool ökosüsteemiga, ZeroLink coinjoin-protokolliga, mis on algselt välja töötatud Samourai meeskondade poolt.



Ashigaru Terminal töötab minimalistliku TUI-liidesega ja seda saab kasutada personaalarvutis või spetsiaalses serveris. See võimaldab teil suhelda otse Whirlpool-ga, et algatada "*Tx0*", hallata "*Deposit*", "*Premix*", "*Postmix*" ja "*Badbank*" kontosid ning teostada automaatseid remixe, et tugevdada oma osade konfidentsiaalsust.



Lühidalt öeldes on Ashigaru Terminal eriti kasulik, kui soovite luua coinjoine'i, kasutades Whirlpool.



Selles esimeses õpetuses tutvustan teile Ashigaru terminali paigaldamist ja kasutamist. Teine, edasijõudnute õpetus on siis pühendatud tegelikule coinjoinide loomisele.



https://planb.academy/tutorials/privacy/on-chain/ashigaru-whirlpool-e566803d-ab3f-4d98-9136-5462009262ef

## 1. Ashigaru terminali paigaldamine



Ashigaru Terminal'i paigaldamiseks on vaja Tor Browser'i, kuna binaarkoode levitatakse ainult Tor-võrgu kaudu. Kui te pole seda veel teinud, [installige see oma masinasse](https://www.torproject.org/download/).



### 1.1. lae alla Ashigaru terminal



Mine Tor Browserist [nende Git-repositooriumi versioonide lehele](http://ashicodepbnpvslzsl2bz7l2pwrjvajgumgac423pp3y2deprbnzz7id.onion/Ashigaru/Ashigaru-Terminal/releases/), et laadida alla Ashigaru Terminal'i uusim versioon sinu operatsioonisüsteemi jaoks.



```txt
ashicodepbnpvslzsl2bz7l2pwrjvajgumgac423pp3y2deprbnzz7id.onion/Ashigaru/Ashigaru-Terminal/releases/
```



![Image](assets/fr/01.webp)



Laadige alla järgmised 2 faili oma operatsioonisüsteemi jaoks:




- Binaarsüsteem (`ashigaru_terminal_v1.0.0_amd64.deb` Debian/Ubuntu puhul, `.dmg` macOS puhul või `.zip` Windowsi puhul) ;
- Allkirjastatud hashide fail: `ashigaru_terminal_v1.0.0_signed_hashes.txt`.



### 1.2. Kontrolli Ashigaru terminali



Enne tarkvara käivitamist seadmes peate kontrollima selle autentsust ja terviklikkust. See on oluline samm, sest see hoiab ära pettuse versiooni paigaldamise, mis võib ohustada teie bitcoin'i või nakatada teie masinat.



Avage uus brauseri vahekaart ja minge [Keybase'i kontrolltööriistale](https://keybase.io/verify). Sisestage äsja alla laaditud faili `.txt` sisu ettenähtud väljale ja klõpsake seejärel nupul `Verify`.



![Image](assets/fr/02.webp)



Et mitmekesistada oma kontrolliallikat, võite võrrelda sõnumit ka clearnet [ashigaru.rs](https://ashigaru.rs/download/) saitidel, rubriigis `/download`.



![Image](assets/fr/03.webp)



Kui allkiri on kehtiv, kuvab Keybase teate, mis kinnitab, et fail on allkirjastatud Ashigaru arendajate poolt.



![Image](assets/fr/04.webp)



Võite klõpsata ka Keybase'i poolt kuvatud `ashigarudev` profiilil ja kontrollida, et nende võtme sõrmejälg vastab täpselt : `A138 06B1 FA2A 676B`.



![Image](assets/fr/05.webp)



Kui selles etapis ilmneb viga, on allkiri kehtetu. Sellisel juhul **ei tohi allalaaditud tarkvara installida**. Alustage uuesti algusest või küsige enne jätkamist abi kogukonnalt.



Keybase on andnud teile rakenduse autentitud hashi. Nüüd kontrollime, et allalaetud `.deb`, `.zip` või `.dmg` faili hash vastab Keybase'is valideeritud failile. Selleks minge [HASH FILE ONLINE](https://hash-file.online/).



Klõpsake nupul `BROWSE...` ja valige sammus 1.1 alla laetud `.deb`, `.zip` või `.dmg` fail. Seejärel valige `SHA-256` hash-funktsioon ja klõpsake `CALCULATE HASH`, et generate faili hash oleks võimalik.



![Image](assets/fr/06.webp)



Seejärel kuvab sait tarkvara hashi. Võrrelge seda Keybase.io kaudu kontrollitud hashiga. Kui need vastavad täpselt, on autentsuse ja terviklikkuse kontroll olnud edukas. Seejärel saate tarkvara kasutada.



![Image](assets/fr/07.webp)



### 1.3 Ashigaru terminali käivitamine





- Debian / Ubuntu



Tarkvara installimiseks käivitage käsk :



```bash
cd ~/Downloads
sudo apt install ./ashigaru_terminal_v1.0.0_amd64.deb
```



Muutke järjekorda vastavalt allalaaditud versioonile.



Seejärel kontrollige paigaldust:



```bash
/opt/ashigaru-terminal/bin/Ashigaru-terminal --version
```



Seejärel käivitage tarkvara:



```bash
/opt/ashigaru-terminal/bin/Ashigaru-terminal
```





- Windows**



Tehke paremklõps allalaaditud ja kontrollitud .zip-failil, seejärel valige selle sisu ekstraheerimiseks `Extract All...`.



Kui ekstraheerimine on lõppenud, tehke topeltklõps failil `Ashigaru-terminal.exe`, et käivitada tarkvara.



![Image](assets/fr/08.webp)



## 2. Ashigaru terminaliga alustamine



Ashigaru Terminal on TUI (*Text-based User Interface*) programm, st minimalistlik kasutajaliides, mis töötab otse terminalis. Te suhtlete sellega menüüde ja klaviatuurikombinatsioonide abil, kuid ilma tõelise klassikalise graafilise keskkonnata.



![Image](assets/fr/09.webp)



Seda on lihtne kasutada: kasutage menüüdes navigeerimiseks klaviatuuri nooleklahve ja vajutage tegevuse kinnitamiseks või valiku kinnitamiseks klahvi "Enter".



## 3. Oma sõlme ühendamine Ashigaru terminaliga



Vaikimisi ühendub Ashigaru Terminal avaliku Electrum serveriga. See kujutab endast ilmselgelt ohtu konfidentsiaalsusele ja suveräänsusele. Seega konfigureerime selle nii, et see ühenduks otse teie enda Electrum Server-ga.



Selleks avage menüü "Eelistused > Server".



![Image](assets/fr/10.webp)



Klõpsake nupule `< Edit >`.



![Image](assets/fr/11.webp)



Valige "Privaatne Electrum Server", seejärel klõpsake "Jätka".



![Image](assets/fr/12.webp)



Sisestage oma serveri URL ja port. Tor-aadressi saate määrata `.onion`. Seejärel klõpsake ühenduse kontrollimiseks nupule `< Test >`.



![Image](assets/fr/13.webp)



Kui ühendus on edukas, ilmub teade `Success` koos teie serveri üksikasjadega.



![Image](assets/fr/14.webp)



Kui teil ei ole veel Bitcoin sõlme, siis soovitan teil see kursus läbida:



https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426

*Minu puhul, selle õpetuse jaoks, kavatsen ma oma Electrs serverist lahti ühendada, sest ma töötan testnetis. Kuid töö jääb rangelt samaks mainnet.* peal



## 4. Loo portfoolio Ashigaru terminalis



Nüüd, kui tarkvara on õigesti konfigureeritud, saame lisada Bitcoin portfelli.



Teil on kaks võimalust:




- Saate luua uue wallet nullist ja kasutada seda ainult Ashigaru terminalis. Sellisel juhul peate selle tarkvara avama iga kord, kui soovite oma wallet-ga suhelda;
- Alternatiivina saate oma olemasoleva Ashigaru wallet otse oma telefonist Ashigaru Terminalisse importida. Selle meetodi puuduseks on see, et see vähendab veidi teie seadistuse turvalisust, kuna teie wallet on siis ühe keskkonna asemel avatud kahele riskantsele keskkonnale. Teisest küljest on selle eeliseks võimalus jätta Ashigaru Terminal pidevalt tööle, et segada oma münte, võimaldades teil samal ajal neid Ashigaru mobiilirakenduse kaudu eemalt kulutada.



Selles õpetuses valime teise meetodi. Kui soovite siiski luua täiesti uue portfelli, jääb protseduur samaks: ainus erinevus on loomise ajal, kui peate salvestama oma uue mnemofraasi ja uue passphrase.



Pange tähele, et Ashigaru Terminal ei võimalda teie bitcoine otse kulutada. Võite kas sünkroonida sama rahakoti Ashigaru Terminalis ja Ashigaru rakenduses (mida ma selles juhendis teen) või Sparrow Walletis.



Kui teil ei ole veel wallet Ashigaru rakendust, saate jälgida spetsiaalset õpetust :



https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f

Mine menüüsse "Rahakotid".



![Image](assets/fr/15.webp)



Seejärel valige "wallet loomine / taastamine...". Valik `Open Wallet...` võimaldab teil hiljem pääseda ligi Ashigaru Terminalis juba salvestatud portfellile.



![Image](assets/fr/16.webp)



Andke oma portfellile nimi.



![Image](assets/fr/17.webp)



Seejärel valige portfelli tüüp "Hot Wallet".






![Image](assets/fr/18.webp)



Selles etapis erineb menetlus sõltuvalt teie esialgsest valikust:




- Kui soovite luua uue portfelli nullist, klõpsake nupule "Uue Wallet genereerimine", määratlege passphrase BIP39, seejärel salvestage hoolikalt oma mnemooniline fraas ja passphrase füüsilisel andmekandjal ;



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270



- Kui soovite kasutada sama wallet kui teie Ashigaru rakendus, sisestage oma mnemoonilise fraasi 12 sõna ja oma passphrase BIP39 otse vastavatesse väljadesse. Kirjutage sõnad väiketähtedega, tervelt, järjekorras, tühikuga eraldatud, ilma numbrite ja lisatäheteta.



Kui see samm on lõpetatud, klõpsake nuppu `< Next >`.



*Märkus*: Kui te ei saa seda nuppu vajutada, on teie mnemooniline fraas kehtetu. Kontrollige hoolikalt, et ükski sõna ei oleks vale või valesti kirjutatud.



![Image](assets/fr/19.webp)



Seejärel peate määrama parooli. Seda kasutatakse teie Ashigaru Terminal wallet avamiseks ja selle kaitsmiseks volitamata füüsilise juurdepääsu eest. See ei ole seotud teie võtmete krüptograafilise tuletamisega: teisisõnu, isegi ilma selle salasõnata saab igaüks, kellel on teie mnemooniline fraas ja passphrase, taastada teie wallet ja pääseda ligi teie bitcoinidele.



Valige pikk, keeruline ja juhuslik parool. Hoidke koopiat turvalises kohas: ideaaljuhul füüsilisel andmekandjal või turvalises paroolihalduris.



Kui olete lõpetanud, klõpsake nuppu "OK >".



![Image](assets/fr/20.webp)



## 5. Portfelli kasutamine



Seejärel saate valida, millisele kontole soovite juurdepääsu. Hetkel ei ole me algatanud mingeid segusid, seega kasutame kontot "Deposiit".



![Image](assets/fr/21.webp)



Tegevus on siis identne Sparrow omaga, kuna Ashigaru terminal on Sparrow serveri fork. Te leiate samad menüüd:



![Image](assets/fr/22.webp)





- tehingud": võimaldab vaadata selle kontoga seotud tehingute ajalugu. Minu puhul on mõned neist juba näha, sest ma olin teinud mõned Ashigaru rakendusega samal wallet-l.



![Image](assets/fr/23.webp)





- receive`: genereerib uue, tühja kviitungi aadressi, et paigutada satss hoiukontole.



![Image](assets/fr/24.webp)





- aadressid`: kuvab kõigi teie aadresside nimekirja, olenemata sellest, kas need kuuluvad teie konto sisemisse või välisesse ahelasse.



![Image](assets/fr/25.webp)





- `UTXOs`: loetleb kõik olemasolevad UTXOd.



![Image](assets/fr/26.webp)





- `Settings`: annab ligipääsu teie portfelli *deskriptorile*. Samuti saate vaadata oma seed, reguleerida *Lõikepiirangut* või muuta oma portfelli loomise kuupäeva.



![Image](assets/fr/27.webp)



Nüüd teate, kuidas paigaldada ja kasutada Ashigaru Terminali. Järgmises õppetükis näeme, kuidas selle tarkvaraga teha coinjoine ja hallata vahendeid "*Postmix*"-is.
https://planb.academy/tutorials/privacy/on-chain/ashigaru-whirlpool-e566803d-ab3f-4d98-9136-5462009262ef
