---
name: BIP-85
description: Ni gute nokoresha BIP-85 gushika kuri generate amajambo menshi y’imbuto avuye kuri seed nyamukuru?
---
![cover](assets/cover.webp)



## 1. Gutahura igitabu BIP-85



### 1.1 BIP-85 ni iki?



BIP-85 ni igikorwa giteye imbere kigufasha kurema amajambo menshi **seed y'inyuma** uhereye ku **Ijambo ry'ingenzi rya seed** rimwe.



Buri nteruro ya kabiri ya seed ishobora gukoreshwa mu guhingura igitabu ca Bitcoin cigenga rwose. Ivyo bitabo bishobora gukoreshwa mu bintu bitandukanye: Hot Wallet kuri telefone ngendanwa, ibitabo vy’incuti, ibitabo vy’ubuzigama bitandukanye, n’ibindi.



Amajambo mato mato yose yo muri seed **akomoka ku mibare**, ariko **ntibishoboka gusubira inyuma ku majambo nyamukuru ya seed** avuye mu majambo mato mato. Ivyo bituma habaho itandukaniro ryose hagati y’igitabu kimwekimwe cose.



Igihe cose uzoba ufise uburenganzira bwo kuronka ijambo ryawe ry'ingenzi rya seed (n'irijana na passphrase nimba uriko urakoresha rimwe), urashobora gusubiramwo ijambo ry'inyuma ryose rya seed **bisa n'ivyo**, utabwirizwa kuribika ukwaryo.



### 1.2 Kubera iki wokoresha BIP-85?



BIP-85 ni ngirakamaro nimba ushaka :





- Rema ibitabo vyinshi vyigenga vya Bitcoin ata bindi vyinshi
- Gucungera amafaranga yawe ukurikije imikoreshereze itandukanye (ukuzigama, amafaranga, umuryango, imigambi)
- Gukingira incuti (igikorwa ca "Marume Jim")
- Gukuraho ibitabo vyawe utatakaje uburenganzira bwo kuronka amahera yawe
- Yorosha umutekano wawe: ijambo rimwe gusa ry’ingenzi rya seed ryo kurinda



### 1.3 Inyungu ku BIP-32



Na BIP-32, interuro imwe ya seed irashobora gukoreshwa kugira ngo generate ikore urutonde rwuzuye rw'amakonti n'amaderesi ya Bitcoin, hakoreshejwe inzira z'ugukura (nk'akarorero: `m/44'/0'/0'/0/0`). Inzira yose ishobora guserukira inkuru itandukanye, ariko **yose iguma ifatanye n’interuro imwe ya seed**. Rero, iyo iri jambo rya seed rishungabanijwe, **amakonti yose akomoka kuri yo arashikira**.



Na BIP-85, interuro nyamukuru ya seed irashobora gukoreshwa ku generate interuro nyinshi zigenga rwose za seed: **iyo imwe muri izo mbuto zibiri zihungabanijwe, uwutera ntazokwigera ashobora gusubira kuri seed nyamukuru canke gushika ku zindi nkuru**.


Ivyo bituma bishoboka gucapura ingorane:





- Ushobora gukoresha seed ya kabiri ku Hot Wallet canke gukoresha mu gihe gito, wemera gushirwa ahabona cane.
- Naho iyi Hot Wallet yoba yahungabanijwe, ayandi mahera yawe, akinzwe n’izindi mbuto zikurikira canke agumye ataco akora, **aguma ari meza**.



Ku rundi ruhande, kuri BIP-32 na BIP-85, iyo seed nyamukuru ihungabanijwe, **amahera yose arashobora guhungabana**. Ni ngombwa rero ko tuyirinda n’umutekano wo hejuru cane.



![image](assets/fr/02.webp)


## 2. Ivyerekeye gukoresha BIP-85



BIP-85 iragufasha gukora ibitabo vyinshi vya Bitcoin ukoresheje ijambo rimwe ry’ishimikiro rya seed, rimwe ryose rifise ijambo ryaryo rya kabiri rya seed. Aha hariho ibintu bitanu vyo gukoresha mu gutunganya no gucungera amahera yawe ya Bitcoin. Ikibazo cose kirasigura igituma gukoresha BIP-85 ari vyiza kuruta gucunga amakonti menshi ukoresheje ijambo rimwe rya seed biciye kuri BIP-32.



### 2.1 Kugabanya ingorane z'itunga ridatekanye





- Ivyabaye**: Ukoresha "Hot Wallet" Wallet (ishizwe ku gikoresho gifatanye na Internet), ku bikorwa vya misi yose.
- Umuti BIP-85**: Urema ijambo rya kabiri rya seed ryerekeye iyi nkuru.
- Inyungu kuri BIP-32**: Ntukeneye kwinjiza ijambo ry’intango rya seed kuri telefone yawe, bikagabanya ingorane zo gufatwa n’abantu. Ijambo rya kabiri rya seed ryonyene ni ryo rihungabanywa, rikakingira izindi nkweto zawe. Na BIP-32, ukeneye gukoresha ijambo nyamukuru rya seed n’inzira yo guca mu nzira, ugashira ahabona amahera yawe yose.



### 2.2 Rema igitabo c'ibintu vy'umunyamuryango





- Ivyabaye**: Ushizeho Bitcoin Wallet ku muntu uri hafi (nk’akarorero mama wawe), mu gihe ushobora kuyigarura iyo ayitakaje.
- Umuti BIP-85**: Urema interuro ya kabiri yihariye seed maze ugasangira iyi gusa.
- Inyungu kuri BIP-32**: Na BIP-32, gukora konti y’umuntu ukunda bisaba gusangira ijambo ryawe ry’ingenzi rya seed, ugashira mu kaga amahera yawe yose no kugora uburongozi bw’uwo ukunda (gucungera inzira z’amashami), canke gukora ijambo rishasha rya seed kugira ngo uzigame ijambo ryawe ry’ingenzi.



### 2.3 Gufasha gucunga ibikorwa bitandukanye





- Ivyabaye**: Utandukanya amafaranga yawe y’ama bitcoins kubera intumbero zitandukanye (nk’amahera yo kuzigama igihe kirekire, amafaranga atari aya KYC).
- Umuti BIP-85**: Urema amajambo ya kabiri seed yerekeye intumbero imwe imwe.
- Inyungu kuri BIP-32**: Na BIP-32, amakonti yose asangira ijambo rimwe rya seed, ivyo bikaba bigora uburongozi mu bitabo vy'abandi mu gusaba inzira z'ugukura nk'`m/44'/0'/0'` kugira ngo zicungwe. Ikindi, ntibishoboka gutanga konti itandukanye ku gikoresho cose (nk'akarorero "ukuzigama kuri Coldcard", "ku musi kuri telefone ngendanwa", "ibiruhuko kuri Trezor"). BIP-85 itanga ijambo ry’inyuma ry’umwihariko rya seed ku ntumbero, ryoroshe kumenya no kwinjiza bitandukanye ku gikoresho cose.



### 2.4 Gukoresha Wallet y'igihe gito ku bikorwa





- Ivyabaye**: Ukeneye igitabu c’igihe gito co gukoresha rimwe canke kugira ngo uzigame ibanga (nk’akarorero: kuvanga amafaranga, gukorana na Exchange KYC, n’ibindi).
- Umuti BIP-85**: Urema interuro ya kabiri ya seed, ukayikoresha mu bijanye n’ugucuruza, hanyuma ukayisambura iyo bikenewe, uzi ko ishobora gusubirwamwo.
- Inyungu kuri BIP-32**: Na BIP-32, konti y’igihe gito ivana n’interuro nyamukuru ya seed, igaragaza amahera yawe yose iyo ashobora guhungabanywa.





## 3. Imbere y’uko utangura .





- Ibikoresho** (ntibikenewe)
 - Ikarata y’ubukonje Mk4 canke Q1.
 - Ikarata MicroSD





- Ubumenyi bw'ishimikiro
 - Gutahura amajambo yo muri Mnemonic (BIP-39): urutonde rw’amajambo 12 gushika ku 24 yo kubika igitabu.
 - Menya ico Bitcoin Wallet ari co: porogarama canke igikoresho co gucunga ama bitcoins yawe, n’ingene woyasubizaho ukoresheje ijambo Mnemonic.
 - Ibindi bikoresho biri mu Migereka.





- Porogaramu ihuye**
 - Sparrow wallet (mudasobwa, yo kuraba gusa canke uburongozi buteye imbere)
 - Nunchuck (igendagenda, ku mikono myinshi)
 - Igikapu c'ubururu (igendagenda)
 - ...





- 3.4 **Ikarata ikonje** imiterere
 - Gutangura interuro ya seed y’amajambo 24 ku Coldcard.
 - Ivyo ushobora guhitamwo: Wongereko passphrase kugira ngo ushobore gushika ku mashami ya BIP-85.
 - Gukoresha amahitamwo ngirakamaro: NFC (yo gusohora hanze), guhagarika USB kuri bateri (umutekano).




## 4. Intambwe ku yindi inyigisho



Kurikiza izi ntambwe kugira ngo ureme, ukoreshe kandi ubone Mnemonic ya kabiri iri kumwe na BIP-85 kuri Coldcard yawe.



### 4.1 generate igiharuro ca kabiri ca seed



Uzokora ijambo rya kabiri rya seed uhereye ku ijambo ryawe ry'ingenzi rya seed.


Hindukiza Coldcard yawe, winjize kode yawe ya PIN.





- 1. Niba warashizeko passphrase ku seed yawe nyamukuru:
 - Kuva ku rubuga rw'Imbere, genda kuri `passphrase`.
    - Hitamwo `Ongera Ijambo` hanyuma winjize ijambobanga ryawe.
    - Kanda `Shiraho`.
    - Suzuma akaranga ka Wallet: Genda kuri `Ivyiza > Raba akaranga` kugira ngo ubone urutoke rwa Wallet.





- 2. Genda kuri **BIP-85**
 - Kuva ku rubuga rw'intango, genda kuri `Ivyiza > Gukura seed B85`
 - Soma imburi maze wemeze.



ColdCard ikumenyesha ko imbuto zivuye mu mibare zikomoka kuri seed yawe nyamukuru, ariko mu vy’ubuhinga bw’ibanga zidashobora kwigenga.


![image](assets/fr/03.webp)





- 3. Hitamwo uburyo


Hitamwo uburyo bw’amajambo yo muri seed: amajambo 12, 18 canke 24. Suzuma umubare w’amajambo yemewe na Wallet ushaka kwinjizamwo ijambo ryawe rya seed.


![image](assets/fr/04.webp)





- 4. Hitamwo urutonde
 - Injira urutonde hagati ya 0 na 9999.
 - Ico kigereranyo ni ikintu gihambaye cane mu gusubiramwo seed ya kabiri mu gihe kizoza. Bigumye neza n'ikimenyetso nk'iki: "Index 1 = Wallet mobile", "Index 2 = umugambi w'umuryango", "Index 4 = test mix", ...
 - Iyo uyitakaje, ntuzotakaza uburenganzira bwo kuronka amahera yawe, ariko uzobwirizwa kugerageza imigwi kuva kuri 0 gushika kuri 9999 kugira uyaronke.


![image](assets/fr/05.webp)





- 5. Iyumvire canke urungike hanze interuro ya kabiri ya seed


ColdCard ubu yerekana interuro nshasha ya kabiri ya seed. Urashobora :




 - I **ikete ry'amaboko**.
 - Gucapura :
     - 1` kugira ngo ubike kuri SD card
     - `2` kugira ngo **winjire "koresha iyi seed"** uburyo kuri ColdCard (ni ngirakamaro mu gutuma hanze canke gusinya ibikorwa)
     - 3` kugira ngo ugaragaze **kode ya QR** (kugira ngo ushobore gucapura ukoresheje porogaramu yo kuri telefone ngendanwa nka BlueWallet canke Nunchuck)
     - 4` kugira ngo uyirungike kuri **NFC**



💡 Kuri iki gihe, ufise ijambo ry’ururimi rwa seed ryigenga, rikoreshwa mu rurimi rwa Wallet BIP39 urwo ari rwo rwose (Trezor, Ledger, BlueWallet, Nunchuck...).


![image](assets/fr/06.webp)


![image](assets/fr/07.webp)


### 4.2 Gukoresha igitabu ca kabiri seed



Ubu ushobora gukoresha iyi seed kugira ngo ureme igitabo gishasha muri :




- porogaramu ngendanwa
- uwundi Hardware Wallet
- igitabo ca Multisig



### 4.3 Gusubizaho ijambo rya kabiri rya seed ryazimiye



Kugira ngo ubone seed ya kabiri igihe cose, subiramwo iyo nzira:


1. Subiramwo ColdCard yawe


2. Shiramwo PIN yawe


3. Injira passphrase yawe, nimba yasobanuwe


4. Genda kuri `Ivyiza > Kuvako seed B85`


5. Hitamwo uburyo (12/18/24 amajambo)


6. Injira urutonde rumwe (nk'akarorero `1`)


7. Uzoronka neza na neza seed ya kabiri imwe.




## 5. Imipaka, ingorane n'imigenzo myiza



### 5.1 Gushingira ku nteruro nyamukuru ya seed + passphrase



Ikoreshwa rya BIP85 ryishimikije rwose ku nteruro nyamukuru y’amajambo 24 seed, be no kuri passphrase nimba warakoresheje imwe.




- Muri izo Elements zibiri, amajambo yose y’inyuma ya seed arashobora gusubirwamwo.
- Iyo udafise kimwe muri ivyo 2 Elements, uratakaza uburenganzira bwo kuronka ibiharuro vyose biva ku bindi.



### 5.2 Ivyago mu gutunganya imikono myinshi



Turahanura cane kudakoresha amajambo ya kabiri ya seed akomoka ku majambo nyene ya mbere ya seed mu ntunganyo ya multi-sig: iyo igikoresho canke amajambo ya mbere ya seed yahungabanijwe, imfunguruzo zose za multi-sig zirashobora gusubirwamwo n’uwutera.



### 5.3 Uguhuza kwa porogaramu



Si ibikorwa vyose bishigikira ata guca ku ruhande BIP85 derivation. Ariko rero, imbuto zivuye muri BIP85 ni imbuto za BIP39 zisanzwe (amajambo 12, 18 canke 24), kandi rero zishobora gukoreshwa mu gitabu cose gihuye na BIP39.



### 5.4 Ukwandika konti ya BIP85



Ni vyiza ko umuntu agumana igitabu c’amajambo y’inyuma y’ururimi rwa seed kiri ku gihe.




- Bigufasha kumenya ningoga urutonde rwa BIP85 rujanye n’igitabu ikihe, ataco ubwirizwa kubika amajambo y’inyuma ya seed.
- Iryo kete rikwiye kuguma ari ritoyi, ataco rivuze mu buryo butomoye kuri Bitcoin, kandi rikwiye kubikwa ritandukanye na seed nyamukuru. Ibuka kubivuga mu mugambi wawe w’iragi.



Igitabo gishobora kubamwo :




- Urutonde rwa bIP85 rwakoreshejwe (umubare kuva kuri 0 gushika kuri 9999)
- izina ry'ikoreshwa canke ry'ishingiro (nk'akarorero Hot Wallet, amafaranga umuntu azigamye, Wallet ya Mama)
- iyo bikenewe, urutoke rwa Wallet rwo kugenzura muri ColdCard



### 5.5 Gusubiza inyuma



Ivyo gusubiza inyuma bitegerezwa kubamwo :




- seed nyamukuru
- gW-76 (niba ikoreshwa)



Ntimwigere mubika hamwe:




- ivy'ingenzi seed na passphrase
- seed nyamukuru n'igitabu ca konti ya BIP85



Ibindi bikoresho biri mu Migereka.




## UMUGEREKA



## A.1 Insobanuro y'amajambo





- [BEEP](urubuga/ibikoresho/insobanuro y'amajambo/BIP)
- [BIP-32](urubuga rw'umugambi/ibikoresho/insobanuro y'amajambo/bip0032)
- [BIP-39](urubuga rw'umugambi/ibikoresho/insobanuro y'amajambo/bip0039)
- [BIP-85](urubuga rw'umugambi/ibikoresho/insobanuro y'amajambo/bip0085)
- [Ijambo seed](https://planb.urubuga/ibikoresho/insobanuro/ijambo ry'ugusubirana)
- [passphrase](urubuga rw'umugambi/ibikoresho/insobanuro y'amajambo/passphrase-bip39)
- [Multisig](urubuga/ibikoresho/insobanuro y'amajambo/Multisig)




### A.2 Bika amajambo yawe yo gukira



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270


### A.3 Gutahura passphrase BIP39



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7


### A.4 Uko ibitabo vya Bitcoin bikora



https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f