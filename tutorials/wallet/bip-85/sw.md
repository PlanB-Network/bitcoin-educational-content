---
name: BIP-85
description: Ninawezaje kutumia maneno mengi ya mbegu ya BIP-85 hadi generate kutoka kwa seed kuu?
---
![cover](assets/cover.webp)



## 1. Kuelewa BIP-85



### 1.1 BIP-85 ni nini?



BIP-85 ni chaguo la kukokotoa la hali ya juu linalokuwezesha kuunda maneno kadhaa ya upili ya **seed** kutoka kwa kifungu kimoja kikuu cha **seed**.



Kila sentensi ya upili ya seed inaweza kutumika kuunda kwingineko huru kabisa ya Bitcoin. Portfolios hizi zinaweza kutumika kwa madhumuni mbalimbali: Hot Wallet kwenye simu ya mkononi, kwingineko kwa jamaa, kwingineko tofauti ya akiba, nk.



Vifungu vidogo vyote vya seed **vinatokana na hisabati**, lakini **haiwezekani kurejea kwenye kishazi kikuu cha seed** kutoka katika kifungu kidogo cha maneno. Hii inahakikisha utengano kamili kati ya kila kwingineko.



Alimradi una idhini ya kufikia kishazi chako kikuu cha seed (na passphrase inayohusishwa ikiwa unatumia moja), unaweza kuunda upya kifungu chochote cha pili cha seed **kwa kufanana**, bila kulazimika kuihifadhi kando.



### 1.2 Kwa nini utumie BIP-85?



BIP-85 ni muhimu ikiwa unataka:





- Unda portfolio kadhaa huru za Bitcoin bila chelezo nyingi
- Dhibiti pesa zako kulingana na matumizi tofauti (akiba, gharama, familia, miradi)
- Ulinzi wa dhamana kwa jamaa (kazi ya "Mjomba Jim")
- Futa kwingineko bila kupoteza ufikiaji wa pesa zako
- Rahisisha usalama wako: kifungu kimoja cha maneno muhimu cha seed ili kulinda



### 1.3 Faida zaidi ya BIP-32



Kwa BIP-32, sentensi moja ya seed inaweza kutumika kwa generate safu kamili ya akaunti na anwani za Bitcoin, kwa kutumia njia za utokaji (kwa mfano: `m/44'/0'/0'/0/0`). Kila njia inaweza kuwakilisha akaunti tofauti, lakini **zote hubaki zimeunganishwa kwa sentensi sawa ya seed**. Kwa hivyo, ikiwa kifungu hiki cha maneno cha seed kitaathiriwa, **akaunti zote zinazotolewa zitaweza kufikiwa**.



Kwa BIP-85, sentensi kuu ya seed inaweza kutumika kwa generate sentensi kadhaa za upili za seed zinazojitegemea kabisa: **ikiwa moja ya mbegu hizi za upili imeathiriwa, mshambuliaji hataweza kamwe kurudi kwenye seed kuu au kufikia portfolio nyingine**.


Hii inafanya uwezekano wa kugawanya hatari:





- Unaweza kutumia seed ya pili kwa Hot Wallet au matumizi ya muda, ukikubali kukabiliwa na mwonekano wa juu zaidi.
- Hata kama Hot Wallet hii imeathiriwa, fedha zako nyingine, zikilindwa na mbegu nyingine au kuwekwa nje ya mtandao, **zinabaki salama**.



Kwa upande mwingine, kwa BIP-32 na BIP-85, ikiwa seed kuu inakabiliwa, **fedha zote ziko hatarini**. Kwa hivyo ni muhimu kuilinda kwa usalama wa hali ya juu.



![image](assets/fr/02.webp)


## 2. Kesi za matumizi ya vitendo kwa BIP-85



BIP-85 hukuruhusu kuunda jalada nyingi za Bitcoin kutoka kwa kifungu kimoja cha msingi cha seed, kila moja ikiwa na kifungu chake cha pili cha seed. Hapa kuna kesi tano za utumiaji za kivitendo za kupanga na kupata pesa zako za Bitcoin. Kila kesi inaeleza kwa nini kutumia BIP-85 ni ya vitendo zaidi kuliko kudhibiti akaunti nyingi kwa kifungu kimoja cha seed kupitia BIP-32.



### 2.1 Kupunguza hatari ya kwingineko isiyo salama sana





- Hali**: Unatumia "Hot Wallet" Wallet (iliyosakinishwa kwenye kifaa kilichounganishwa kwenye Intaneti), kwa shughuli za kila siku.
- Suluhisho BIP-85**: Unaunda maneno ya upili ya seed yaliyowekwa kwa kwingineko hii.
- Manufaa zaidi ya BIP-32**: Huhitaji kuleta kifungu cha msingi cha seed kwenye simu yako, hivyo basi kupunguza hatari ya kudukuliwa. Ni maneno ya pili ya seed pekee ndiyo yameathiriwa, kulinda pochi zako zingine. Ukiwa na BIP-32, unahitaji kutumia kifungu kikuu cha seed na njia ya kupita, ikionyesha pesa zako zote.



### 2.2 Unda kwingineko kwa mwanafamilia





- Hali**: Umeweka Bitcoin Wallet kwa mtu wa karibu nawe (k.m. mama yako), huku ukiweza kuirejesha akiipoteza.
- Suluhisho BIP-85**: Unaunda sentensi ya upili ya seed iliyojitolea na kushiriki hii pekee.
- Manufaa zaidi ya BIP-32**: Ukiwa na BIP-32, kuunda akaunti kwa ajili ya mpendwa kunahitaji ama kushiriki kifungu chako kikuu cha seed, kuhatarisha pesa zako zote na kutatiza usimamizi wa mpendwa wako (kusimamia njia za matawi), au kuunda kifungu kipya cha seed ili kuhifadhi pamoja na kifungu chako kikuu cha seed.



### 2.3 Kuwezesha usimamizi wa portfolios tofauti





- Hali**: Unatenganisha bitcoins zako kwa madhumuni tofauti (k.m. akiba ya muda mrefu, fedha zisizo za KYC).
- Suluhisho BIP-85**: Unaunda misemo ya upili ya seed iliyowekwa kwa kila lengo.
- Manufaa zaidi ya BIP-32**: Kwa BIP-32, akaunti zote zinatumia maneno yale yale ya seed, ambayo yanatatiza usimamizi katika portfolio za wahusika wengine kwa kuhitaji njia za utokaji kama vile `m/44'/0'/0'` zidhibitiwe. Kwa kuongeza, haiwezekani kugawa akaunti tofauti kwa kila kifaa (k.m. "akiba kwenye Coldcard", "kila siku kwenye simu", "likizo kwenye Trezor"). BIP-85 hukabidhi maneno ya upili ya seed kwa kila lengo, ambayo ni rahisi kutambua na kuleta kivyake kwenye kila kifaa.



### 2.4 Kutumia Wallet ya muda kwa miamala





- Hali**: Unahitaji kwingineko ya muda kwa ajili ya ununuzi wa mara moja au kuhifadhi usiri (k.m.: kuchanganya fedha, mwingiliano na Exchange KYC, n.k.).
- Suluhisho la BIP-85**: Unaunda sentensi ya sekondari ya seed, tumia kwa shughuli, kisha uiharibu ikiwa ni lazima, ukijua kwamba inaweza kuzaliwa upya.
- Manufaa zaidi ya BIP-32**: Ukiwa na BIP-32, akaunti ya muda inategemea sentensi kuu ya seed, kufichua pesa zako zote ikiwa itaathiriwa.





## 3. Kabla ya kuanza





- Maunzi** (ya hiari)
 - Coldcard Mk4 au Q1
 - Kadi ya MicroSD





- Maarifa ya msingi
 - Kuelewa misemo ya Mnemonic (BIP-39): orodha ya maneno 12 hadi 24 ili kuhifadhi kwingineko.
 - Jua nini Bitcoin Wallet ni: programu au kifaa cha kusimamia bitcoins zako, na jinsi ya kurejesha kwa maneno ya Mnemonic.
 - Nyenzo zaidi katika Viambatisho.





- Programu inayolingana**
 - Sparrow wallet (kompyuta, kwa usimamizi wa saa pekee au wa hali ya juu)
 - Nunchuck (simu ya rununu, kwa saini nyingi)
 - BlueWallet (simu ya rununu)
 - ...





- 3.4 Usanidi wa Coldcard**
 - Anzisha sentensi ya seed ya maneno 24 kwenye Coldcard.
 - Hiari: Ongeza passphrase ili kupata ufikiaji salama wa matawi ya BIP-85.
 - Washa chaguo muhimu: NFC (ya kusafirisha nje), zima USB kwenye betri (usalama).




## 4. Mafunzo ya hatua kwa hatua



Fuata hatua hizi ili kuunda, kutumia na kurejesha Mnemonic ya pili yenye BIP-85 kwenye Coldcard yako.



### 4.1 generate sentensi ya upili ya seed



Utaunda kishazi cha pili cha seed kutoka kwa kifungu chako kikuu cha seed.


Washa Coldcard yako, weka PIN yako.





- 1. Ikiwa umetumia passphrase kwa seed yako kuu:**
 - Kutoka kwa Skrini ya kwanza, nenda kwa `passphrase`.
    - Chagua `Ongeza Neno` na uweke nenosiri lako.
    - Bonyeza `Tuma`.
    - Angalia utambulisho wa Wallet: Nenda kwa `Advanced > View Identity` ili kutambua alama ya kidole ya Wallet.





- 2. Nenda kwenye menyu ya BIP-85**
 - Kutoka kwa Skrini ya kwanza, nenda kwa `Advanced > Pata seed B85`
 - Soma onyo na uthibitishe.



ColdCard inakufahamisha kwamba mbegu zinazozalishwa zimetokana na kihisabati kutoka kwa seed yako kuu, lakini huru kisirisiri kabisa.


![image](assets/fr/03.webp)





- 3. Chagua umbizo


Chagua umbizo la maneno ya seed: maneno 12, 18 au 24. Angalia idadi ya maneno yanayokubaliwa na Wallet ambayo ungependa kuingiza maneno yako ya seed.


![image](assets/fr/04.webp)





- 4. Chagua index
 - Weka faharasa kati ya 0 na 9999.
 - Faharasa hii ni muhimu kwa kuunda upya seed ya sekondari baadaye. Itunze kwa uangalifu na lebo kama vile: "Index 1 = Wallet mobile", "Index 2 = family project", "Index 4 = test mix", ...
 - Ukiipoteza, hutapoteza uwezo wa kufikia pesa zako, lakini itakubidi ujaribu michanganyiko kutoka 0 hadi 9999 ili kuzipata.


![image](assets/fr/05.webp)





- 5. Kumbuka au safirisha sentensi ya pili ya seed**


ColdCard sasa inaonyesha sentensi mpya ya upili ya seed. Unaweza:




 - ** noti kwa mikono**.
 - Bonyeza:
     - 1` ili kuihifadhi kwenye kadi ya SD
     - `2` ili **kuingiza "tumia hali hii ya seed"** kwenye ColdCard (muhimu kwa kusafirisha au kusaini muamala)
     - 3` ili kuonyesha **msimbo wa QR** (ili kuchanganuliwa kwa programu ya simu kama vile BlueWallet au Nunchuck)
     - 4` kuituma kwa **NFC**



💡 Katika hatua hii, una kishazi huru cha seed, kinachoweza kutumika katika Wallet BIP39 yoyote (Trezor, Ledger, BlueWallet, Nunchuck...).


![image](assets/fr/06.webp)


![image](assets/fr/07.webp)


### 4.2 Kwa kutumia seed ya sekondari



Sasa unaweza kutumia seed hii ili kuunda kwingineko mpya katika :




- programu ya simu
- nyingine Hardware Wallet
- kwingineko ya Multisig



### 4.3 Kurejesha maneno ya upili ya seed yaliyopotea



Ili kurejesha seed ya pili wakati wowote, rudia mchakato:


1. Anzisha tena ColdCard yako


2. Weka PIN yako


3. Ingiza passphrase yako, ikiwa imefafanuliwa


4. Nenda kwenye `Advanced > Pata seed B85`


5. Chagua umbizo (maneno 12/18/24)


6. Weka faharasa sawa (k.m. `1`)


7. Utapata seed ya sekondari sawa kabisa




## 5. Mipaka, hatari na mazoea bora



### 5.1 Kutegemea hukumu kuu ya seed + passphrase



Matumizi ya BIP85 yanategemea kabisa sentensi kuu ya seed yenye maneno 24, na pia passphrase ikiwa umetumia moja.




- Kutoka kwa Elements hizi mbili, misemo yote ya upili ya seed inaweza kuzaliwa upya.
- Bila mojawapo ya hizi 2 Elements, unapoteza uwezo wa kufikia portfolios zote zinazotoka.



### 5.2 Hatari katika usanidi wa saini nyingi



Tunashauri sana dhidi ya kutumia vifungu vya pili vya seed vinavyotokana na maneno yale yale ya msingi ya seed katika usanidi wa multi-sig: ikiwa kifaa au maneno msingi ya seed yataathiriwa, funguo zote za multi-sig zinaweza kutolewa upya na mvamizi.



### 5.3 Upatanifu wa programu



Sio programu zote zinazotumia moja kwa moja utokezi wa BIP85. Hata hivyo, mbegu zinazozalishwa kupitia BIP85 ni mbegu za kawaida za BIP39 (maneno 12, 18 au 24), na kwa hivyo zinaweza kutumika katika kwingineko yoyote inayotangamana na BIP39.



### 5.4 Rejesta ya akaunti ya BIP85



Inapendekezwa kuweka rejista ya kibinafsi iliyosasishwa ya misemo ya upili ya seed.




- Inakuruhusu kujua haraka ni faharisi gani ya BIP85 inalingana na kwingineko gani, bila kulazimika kuweka misemo ya upili ya seed.
- Rejesta hii inapaswa kubaki kuwa ya kiwango cha chini, bila kutajwa wazi kwa Bitcoin, na inapaswa kuhifadhiwa kando na seed kuu. Kumbuka kutaja katika mpango wako wa urithi.



Rejesta inaweza kuwa na:




- faharisi ya bIP85 imetumika (nambari kutoka 0 hadi 9999)
- jina la matumizi au rejeleo (k.m. Hot Wallet, akiba ya kibinafsi, Wallet kutoka kwa Mama)
- ikibidi, alama ya vidole ya Wallet kwa uthibitishaji katika ColdCard



### 5.5 Hifadhi rudufu



Hifadhi rudufu lazima zijumuishe:




- kuu seed
- gW-76 (ikiwa inatumika)



Kamwe usihifadhi pamoja:




- kuu seed na passphrase
- seed kuu na rejista ya akaunti ya BIP85



Nyenzo zaidi katika Viambatisho.




## VIAMBATISHO



## A.1 Faharasa





- [BEEP](https://planb.network/resources/glossary/bip)
- [BIP-32](https://planb.network/resources/glossary/bip0032)
- [BIP-39](https://planb.network/resources/glossary/bip0039)
- [BIP-85](https://planb.network/resources/glossary/bip0085)
- [maneno ya seed](https://planb.network/resources/glossary/recovery-phrase)
- [passphrase](https://planb.network/resources/glossary/passphrase-bip39)
- [Multisig](https://planb.network/resources/glossary/multisig)




### A.2 Hifadhi maneno yako ya urejeshaji



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270


### A.3 Kuelewa passphrase BIP39



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7


### A.4 Jinsi portfolios za Bitcoin zinavyofanya kazi



https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f