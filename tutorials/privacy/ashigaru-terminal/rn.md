---
name: Ashigaru Terminal
description: Koresha Ashigaru ku biro kugira ngo ukore amafaranga
---

![cover](assets/cover.webp)



Igikoresho ca Ashigaru ni ikigo ca Ashigaru gihindura Server ya Sparrow, gishira mu ngiro uburyo bwo gukorana na Whirlpool. Iyi porogarama ni ugukomeza igikorwa catangujwe na Samourai Wallet, cane cane ku bijanye na Whirlpool GUI, iyo ngingo ngenderwako zayo z’ishimikiro yemera: ukwizigama no kuzigama ibanga.



Iyi porogaramu ni fork ya Sparrow Server, yahinduwe kandi itunganywa neza kugira ngo ikoreshe neza n’ibidukikije vya Whirlpool, umurongo wa ZeroLink coinjoin wa mbere wateguwe n’imigwi ya Samourai.



Ashigaru Terminal ikora ikoresheje interface ya TUI kandi ishobora gukoreshwa kuri mudasobwa y’umuntu ku giti ciwe canke kuri server yihariye. Bigufasha gukorana na Whirlpool ataco uhinduye kugira ngo utangure "*Tx0*", ucunge amakonti ya "*Deposit*", "*Premix*", "*Postmix*" na "*Badbank*", kandi ukore amakonti yiwe kugira ngo ukomeze ibanga ry'ibice vyawe.



Muri make, Ashigaru Terminal izoba ngirakamaro cane cane nimba ushaka gukora amafaranga ukoresheje Whirlpool.



Muri iyi nyigisho ya mbere, nzobajana mu gushiramwo no gukoresha Ashigaru Terminal. Inyigisho ya kabiri, iteye imbere cane izoca igenewe kurema vy’ukuri ama coinjoins.



https://planb.academy/tutorials/privacy/on-chain/ashigaru-whirlpool-e566803d-ab3f-4d98-9136-5462009262ef

## 1. Shiraho ikibanza ca Ashigaru



Kugira ngo ushiremwo Ashigaru Terminal, uzokenera Tor Browser, kuko ama binaire akwiragizwa gusa biciye ku rubuga rwa Tor. Niba utarabikora, [bishire ku mashini yawe](https://www.torproject.org/download/).



### 1.1. gukuraho ikibanza ca Ashigaru



Kuva ku Mucukumbuzi wa Tor, genda kuri [paji y’ibisohoka vy’ububiko bwabo bwa Git] (http://ashicodepbnpvslzsl2bz7l2pwrjvajgumgac423pp3y2deprbnzz7id.



```txt
ashicodepbnpvslzsl2bz7l2pwrjvajgumgac423pp3y2deprbnzz7id.onion/Ashigaru/Ashigaru-Terminal/releases/
```



![Image](assets/fr/01.webp)



Gukuraho amadosiye 2 akurikira kuri sisitemu yawe:




- Ivyo bibiri (`.dmg` ku macOS canke `.zip` ku Windows) ;
- Dosiye y'amajambo yashizweko umukono: `ashigaru_iherezo_v1.0.0_amajambo_yashizweko umukono.txt`.



### 1.2. Suzuma ikibanza c'indege ca Ashigaru



Imbere y’uko ukoresha iyo porogarama ku gikoresho cawe, urakeneye kumenya nimba ari iyo ukuri be n’uko idakora neza. Iyi ni intambwe ihambaye, kuko ikubuza gushiramwo verisiyo y’ubuhendanyi ishobora gutuma bitcoins zawe zihungabana canke zigatera indwara imashini yawe.



Gufungura urubuga rushasha rw’umucukumbuzi maze uje kuri [Igikoresho co kugenzura urufunguzo](https://urufunguzo.io/verify). Nimushire ibiri muri dosiye `.txt` mu kibanza catanzwe, hanyuma mukande kuri buto ya `Verify`.



![Image](assets/fr/02.webp)



Kugira ngo uhindure amasoko yawe yo kugenzura, urashobora kandi kugereranya ubutumwa n’ubwo buri ku rubuga rwa clearnet [ashigaru.rs](https://ashigaru.rs/download/), mu gice ca `/gukuraho`.



![Image](assets/fr/03.webp)



Iyo umukono uriho, Keybase izokwerekana ubutumwa bwemeza ko dosiye yashizweko umukono n'abahinguzi ba Ashigaru.



![Image](assets/fr/04.webp)



Ushobora kandi gukanda ku rubuga rwa `ashigarudev` rwerekanwa na Keybase maze ukagenzura ko urutoke rwabo rw'urufunguzo ruhuye neza : `A138 06B1 FA2A 676B`.



![Image](assets/fr/05.webp)



Iyo ikosa riboneka muri iyi ntambwe, umukono ntugira akamaro. Muri ivyo, **ntimushiremwo porogaramu mwaronse**. Subira utangure kuva mu ntango, canke usabe abarundi ngo bagufashe imbere y’uko ukomeza.



Keybase yaguhaye hash yemewe y'ikoreshwa. Ubu turaza kugenzura ko hash ya dosiye `.deb`, `.zip` canke `.dmg` wavuyeko ihuye n'iyo yemejwe kuri Keybase. Kugira ngo ubikore, genda kuri [DOSIYE YA HASH KU RUBUGA](https://dosiye-ya-hash.ku rubuga/).



Fyonda kuri buto ya `BROWSE...` hanyuma uhitemwo dosiye `.deb`, `.zip` canke `.dmg` yavanwe mu ntambwe ya 1.1. Hanyuma uhitemwo `SHA-256` igikorwa ca hash, hanyuma ukande kuri `HARA HASH` kugira ngo generate hash ya dosiye yawe.



![Image](assets/fr/06.webp)



Urubuga ruzoca rwerekana hash ya porogarama. Gereranya n’ivyo mwasuzumye kuri Keybase.io. Iyo ivyo bibiri bihuye neza, isuzuma ry’ukuri n’ubunyankamugayo ryarabaye ryiza. Ushobora rero gukoresha iyo porogarama.



![Image](assets/fr/07.webp)



### 1.3 Gutanguza ikibanza c'indege ca Ashigaru





- Debiyani / Ubuntu



Kugira ngo ushiremwo porogaramu, koresha itegeko :



```bash
cd ~/Downloads
sudo apt install ./ashigaru_terminal_v1.0.0_amd64.deb
```



Guhindura urutonde bivanye n’ivyo mwaronse.



Hanyuma usuzume uko vyashizweho:



```bash
/opt/ashigaru-terminal/bin/Ashigaru-terminal --version
```



Hanyuma utangure porogaramu:



```bash
/opt/ashigaru-terminal/bin/Ashigaru-terminal
```





- Amadirisha**



Fyonda iburyo kuri dosiye `.zip` waronse maze uyisuzume, hanyuma uhitemwo `Extract All...` kugira ngo ukuremwo ibirimwo.



Igihe gukuraho birangiye, fyonda ku dosiye `Ashigaru-terminal.exe` kugira ngo utangure porogarama.



![Image](assets/fr/08.webp)



## 2. Gutangura n'Ikibuga c'Indege ca Ashigaru



Ashigaru Terminal ni porogaramu ya TUI (*Ukoresha ashingiye ku nyandiko Interface*), ni ukuvuga interface y'ubuhinga bukeyi ikora mu buryo butaziguye mu terminal. Ukorana nayo ukoresheje menus n'inzira ngufi za klavye, ariko ata bidukikije vy'ukuri vy'ibishushanyo.



![Image](assets/fr/09.webp)



Biroroshe gukoresha: koresha imfunguruzo z'umwampi za klavye yawe kugira ngo ugende mu bimenyetso, hanyuma ukande urufunguzo `Enter` kugira ngo wemeze igikorwa canke wemeze ihitamwo.



## 3. Guhuza urudodo rwawe n'Ikigo ca Ashigaru



Ku mburabuzi, Igikoresho ca Ashigaru gifatanya na server ya Electrum ya bose. Ivyo biragaragara ko bitera ingorane mu bijanye n’ibanga n’ubusegaba. Rero tugiye kuyitunganya kugira ngo ihuze na Electrum Server yawe.



Kugira ngo ubikore, fungura `Ivyo ukunda > Serveri`.



![Image](assets/fr/10.webp)



Fyonda kuri buto ya `< Guhindura >`.



![Image](assets/fr/11.webp)



Hitamwo `Ibanga Electrum Server`, hanyuma ukande `<Bandanya>`.



![Image](assets/fr/12.webp)



Injira URL n'icuma ca server yawe. Ushobora gutanga aderesi ya Tor muri `.onion`. Hanyuma ukande kuri `< Test >` kugira ngo ugenzure ko hariho ihuriro.



![Image](assets/fr/13.webp)



Iyo ihuriro ryiza, ubutumwa `Success` buzoboneka, hamwe n'ibisobanuro vya server yawe.



![Image](assets/fr/14.webp)



Niba utaragira node ya Bitcoin, ndagusavye gufata iri shure:



https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426

*Mu vyerekeye jewe, kuri iyi nyigisho, ngiye guca kuri server yanje ya Electrs kuko ndiko ndakora kuri testnet. Ariko rero, igikorwa kiguma ari kimwe cane ku mainnet.*



## 4. Rema igitabo ku kibuga ca Ashigaru



Ubu ko iyo porogarama itunganijwe neza, turashobora kwongerako igitabu ca Bitcoin.



Ufise uburyo bubiri:




- Ushobora gukora wallet nshasha uhereye ku ntango ukayikoresha gusa kuri Terminal ya Ashigaru. Muri ivyo, uzokenera gufungura iyo porogarama igihe cose wipfuza gukorana na wallet yawe;
- Canke, ushobora kwinjiza Ashigaru wallet yawe isanzweho uyikuye kuri telefone yawe ukayishira mu kibanza ca Ashigaru. Ikibi c’ubu buryo ni uko bugabanya gatoyi umutekano w’ivyo ushizeho, kuko wallet yawe rero ishobora gushikirwa n’ibidukikije bibiri bishobora gutera ingorane aho gushikirwa n’ikimwe. Ku rundi ruhande, itanga akamaro ko gushobora gusiga Ashigaru Terminal ikora ubudasiba kugira ngo uvange amafaranga yawe, mu gihe ushobora kuyakoresha uri kure biciye ku rubuga rwa Ashigaru mobile app.



Muri iyi nyigisho, tuzohitamwo uburyo bwa kabiri. Ariko rero, nimba ushaka gukora igitabu gishasha, uburyo bwo kubikora buraguma ari bumwe: itandukaniro ryonyene rizoba mu gihe co kurema, igihe uzokenera kubika ijambo ryawe rishasha ry'ukwibuka na passphrase yawe nshasha.



Icyitonderwa kandi ni uko Ashigaru Terminal itakwemerera gukoresha bitcoin zawe mu buryo butaziguye. Ushobora guhuza ububiko bumwe kuri Ashigaru Terminal no kuri porogaramu ya Ashigaru (icyo nzakora muri iri somo), cyangwa kuri Sparrow Wallet.



Niba utaragira wallet ku rubuga rwa Ashigaru, ushobora gukurikira inyigisho yihariye :



https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f

Genda ku rutonde rwa `Ibipapuro`.



![Image](assets/fr/15.webp)



Hanyuma uhitemwo `Rema / gusubizaho wallet...`. Ihitamwo rya `Gufungura Wallet...` rigufasha kuronka ibitabo vyamaze kubikwa muri Terminal ya Ashigaru mu gihe kizoza.



![Image](assets/fr/16.webp)



Ha igitabu cawe izina.



![Image](assets/fr/17.webp)



Hanyuma uhitemwo ubwoko bw'ibitabo `Hot Wallet`.






![Image](assets/fr/18.webp)



Ni muri iyo ntambwe aho uburyo bwo kubikora butandukanye bivanye n’ivyo wahisemwo mu ntango:




- Niba wipfuza gukora igitabu gishasha uhereye ku ntango, kanda kuri `<Generate New Wallet>`, usobanure passphrase BIP39, hanyuma ubike witonze ijambo ryawe ry'ukwibuka n'iry'umubiri wawe ku gikoresho c'umubiri ;



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270



- Niba wipfuza gukoresha wallet imwe n’iyo ukoresha muri porogarama yawe ya Ashigaru, shiramwo amajambo 12 y’invugo yawe y’ukwibuka be na passphrase BIP39 yawe ataco uhinduye mu bibanza bihuye. Wandike amajambo mu nyuguti ntoyi, yose, mu buryo bukurikiranye, atandukanijwe n’umwanya, ata mibare canke inyuguti z’inyongera.



Iyi ntambwe imaze kurangira, kanda `< Ibikurikira >`.



*Iciyumviro*: Niba udashobora gukanda kuri iyi buto, ijambo ryawe ry'ukwibuka ntaco rimaze. Suzuma neza ko ata majambo na rimwe muri ayo majambo atari yo canke ko yanditswe nabi.



![Image](assets/fr/19.webp)



Uzoca ukenera gushinga ijambobanga. Ivyo bizokoreshwa mu gufungura Ashigaru Terminal wallet yawe no kuyikingira umuntu ata wemerewe kuyironka. Ntaco bihuriyeko mu gukuraho imfunguruzo zawe mu buryo bw’ibanga: mu yandi majambo, naho ata iri jambobanga, umuntu wese afise ijambo ryawe ry’ukwibuka na passphrase azoshobora kugarura wallet yawe no gushika ku bitcoins vyawe.



Hitamwo ijambobanga rirerire, rigoye, ry’imburakimazi. Bika kopi ahantu hatagira umutekano: vyiza ni uko wobikoresha mu buryo buboneka canke mu gikoresho co gucungera ijambobanga ry’umutekano.



Fyonda `< OK >` niwaheza.



![Image](assets/fr/20.webp)



## 5. Gukoresha igitabo



Ushobora rero guhitamwo konti uzokoresha. Kugeza ubu, nta mivumba twatanguye, rero tuzoshika kuri konti ya `Deposit`.



![Image](assets/fr/21.webp)



Ivyo rero birasa n’ivya Sparrow, kuko Terminal ya Ashigaru ari fork ya Server ya Sparrow. Uzosanga izo menyu nyene:



![Image](assets/fr/22.webp)





- transactions": bigufasha kuraba amateka y'ibikorwa bifitaniye isano n'iyi konti. Ku bijanye nanje, bimwe muri vyo birasanzwe bigaragara, nk'uko nari nabikoze bimwe n'ikoreshwa rya Ashigaru kuri iyi wallet nyene.



![Image](assets/fr/23.webp)





- receive`: itanga aderesi nshasha, y'inyandiko y'ukwakira yo gushiramwo satss muri konti y'ibiziga.



![Image](assets/fr/24.webp)





- amaderesi`: yerekana urutonde rw'amaderesi yawe yose, yaba ari mu ruhererekane rw'imbere canke rw'inyuma rwa konti yawe.



![Image](assets/fr/25.webp)





- `UTXOs`: itanga urutonde rw'ama UTXO yawe yose ariho.



![Image](assets/fr/26.webp)





- `Imiterere`: itanga uburenganzira bwo gushika ku bitabo vyawe *ibisobanuro*. Ushobora kandi kuraba seed yawe, ugahindura *Gap Limit* canke ugahindura itariki y'irema ry'igitabu cawe.



![Image](assets/fr/27.webp)



Ubu none urazi uburyo bwo kwinjiza no gukoresha Ashigaru Terminal. Mu isomo rikurikira, tuzareba uburyo bwo gukora coinjoin ukoresheje iri porogaramu no kuyobora amafaranga muri "*Postmix*".
https://planb.academy/tutorials/privacy/on-chain/ashigaru-whirlpool-e566803d-ab3f-4d98-9136-5462009262ef
