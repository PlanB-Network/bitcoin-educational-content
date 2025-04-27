---
name: Uwekaji muhuri wa nyakati wa vyeti na diploma za Plan ₿ Network
description: Elewa jinsi Plan ₿ Network hutoa uthibitisho unaoweza kuthibitishwa wa vyeti na diploma zako
---

![cover](assets/cover.webp)


Ikiwa unasoma haya, kuna uwezekano mkubwa kwamba ulipokea cheti cha mtihani wa ₿-CERT au diploma ya kumaliza mojawapo ya kozi ulizohudhuria kwenye planb.network, kwa hivyo pongezi kwa mafanikio haya!


Katika somo hili, tutagundua jinsi Plan ₿ Network hutoa uthibitisho unaoweza kuthibitishwa kwa cheti chako cha mtihani wa ₿-CERT au Diploma yoyote kuhusu Kukamilisha Kozi. Kisha, katika sehemu ya pili tutaeleza jinsi ya kuthibitisha ukweli wa thibitisho hizi.


# Utaratibu wa uthibitisho wa Plan ₿ Network


Katika Plan ₿ Network, tunatia sahihi vyeti na diploma kwa njia fiche, na kuziweka muhuri kwa wakati kwa kutumia Timechain (yaani Bitcoin Blockchain), kupitia mbinu ya uthibitisho ambayo inategemea utendakazi wa siri mbili:


1. Sahihi ya GPG kwenye faili ya maandishi ambayo husanikisha mafanikio yako

2. Uwekaji muhuri wa nyakati wa faili sawa iliyotiwa saini kupitia [opentimestamps](https://opentimestamps.org/).


Operesheni ya kwanza inakuwezesha kuthibitisha mtoaji wa cheti (au diploma), wakati operesheni ya pili inakuwezesha kuthibitisha tarehe ya utoaji wake.

Tunaamini kuwa utaratibu huu rahisi wa uthibitisho unatupa uwezo wa kutoa vyeti na diploma zenye ushahidi usiopingika ambao mtu yeyote anaweza kuthibitisha kwa kujitegemea.


![image](./assets/proof-mechanism.webp)


Shukrani kwa utaratibu huu wa uthibitisho, jaribio lolote la kubadilisha hata maelezo madogo kabisa ya cheti au diploma yako litasababisha SHA-256 Hash tofauti kabisa ya faili iliyotiwa saini, na kufichua papo hapo udukuzi wowote, kwani saini na Timestamp hazitakuwa halali tena. Zaidi ya hayo, mtu yeyote akijaribu kughushi vyeti au diploma kwa niaba ya Plan ₿ Network, uthibitishaji rahisi wa sahihi utafichua ulaghai huo.


## Je, saini ya GPG inafanyaje kazi?


Sahihi ya GPG inatolewa kwa kutumia programu huria iitwayo GNU Privacy Guard. Programu hii huruhusu watumiaji kuunda funguo za faragha kwa urahisi, kutia sahihi na kuthibitisha sahihi, na kusimba kwa njia fiche na kusimbua faili. Kwa madhumuni ya mafunzo haya, ni muhimu kutambua kwamba Plan ₿ Network hutumia GPG kuunda funguo zake za faragha/umma na kutia sahihi Vyeti vyote vya ₿-CERT na Diploma za Kumaliza Kozi.


Kwa upande mwingine, ikiwa mtu anataka kuthibitisha uhalisi wa faili iliyotiwa saini, anaweza kutumia GPG kuleta ufunguo wa umma wa mtoaji na kuuthibitisha.


Kwa wale ambao wana hamu ya kujua na wanataka kujifunza zaidi kuhusu programu hii nzuri, unaweza kurejelea ["Mwongozo wa Faragha wa GNU"](https://www.gnupg.org/gph/en/manual/x135.html)


## Je, kuweka muhuri kwa wakati hufanyaje kazi?


Mtu yeyote anaweza kutumia OpenTimestamps ili Timestamp faili na kupata uthibitisho unaoweza kuthibitishwa wa kuwepo kwake. Kwa maneno mengine, haitoi uthibitisho wa wakati faili iliundwa, lakini badala ya uthibitisho kwamba faili haikuwepo baadaye kuliko wakati maalum kwa wakati.

OpenTimestamps hutoa huduma hii bila malipo kwa kutumia njia bora sana ya kuhifadhi uthibitisho katika Bitcoin Blockchain. Inatumia algoriti ya SHA-256 Hash kuunda kitambulisho cha kipekee cha faili yako, na huunda Merkle Tree kwa kutumia heshi za faili zilizowasilishwa na watumiaji wengine. Hash pekee ya muundo wa Merkle Tree ndiyo iliyounganishwa katika shughuli ya OP_RETURN, kuhakikisha njia salama na fupi ya kuthibitisha kuwepo kwa faili.

Mara tu muamala huu unapoingia kwenye kizuizi, mtu yeyote aliye na faili ya awali na faili ya `.ots` inayohusishwa nayo anaweza kuthibitisha uhalisi wa muhuri wa nyakati. Katika sehemu ya pili ya mafunzo, tutaona jinsi ya kuthibitisha Cheti chako cha Bitcoin au Stashahada yoyote ya Kumaliza Kozi kupitia teminali na kupitia mchoro wa Interface kwenye tovuti ya OpenTimestamps.


# Jinsi ya kuthibitisha cheti cha Plan ₿ Network ₿-CERT au Diploma


## Hatua ya 1. Pakua Cheti au Diploma yako


Ingia kwenye dashibodi yako ya kibinafsi/ya mwanafunzi kwenye planb.network.


![image](./assets/login.webp)


Nenda kwenye "Vitambulisho" kwa kubofya menyu ya upande wa kushoto, na uchague kipindi chako cha mtihani au Diploma yako.


![image](./assets/credential.webp)


Pakua faili ya zip.


![image](./assets/download.webp)


Toa yaliyomo kwa kubofya kulia kwenye faili ya `.zip` na kuchagua "Dondoo". Utapata faili tatu tofauti:



- Faili ya maandishi iliyotiwa saini (k.m. certificate.txt)
- Faili ya Fungua Timestamp (OTS) (k.m. certificate.txt.ots)
- Cheti cha PDF (k.m. cheti.pdf)


## Hatua ya 2: Unawezaje kuthibitisha Sahihi ya Faili ya Maandishi?


Kwanza, nenda kwenye folda ambapo ulitoa faili na ufungue terminal (bonyeza-kulia kwenye dirisha la folda na ubofye "Fungua kwenye Teminal"). Kisha, fuata maagizo hapa chini.


1. Ingiza kitufe cha umma cha Plan ₿ Network cha PGP kwa amri ifuatayo:


```bash
curl -s https://raw.githubusercontent.com/Asi0Flammeus/pgp-public-keys/master/planb-network-pk.asc | gpg --import
```


Unapaswa kuona ujumbe kama ufuatao ikiwa umefaulu kuleta Ufunguo wa PGP


```
gpg: key 8F12D0C63B1A606E: public key "PlanB Network (used for PBN platform) <admin@planb.network>" imported
gpg: Total number processed: 1
gpg:               imported: 1
```


KUMBUKA: ukiona kwamba ufunguo 1 umechakatwa na funguo 0 zimeletwa, inaelekea inamaanisha kuwa tayari umeingiza ufunguo huo hapo awali, ambayo ni sawa kabisa.


2. Thibitisha saini ya cheti au diploma kwa kutumia amri ifuatayo:


```bash
gpg --verify certificate.txt
```


Amri hii inapaswa kukuonyesha maelezo kuhusu saini, pamoja na:



- Nani alitia saini (Plan ₿ Network)
- Iliposainiwa
- Ikiwa saini ni halali au la


Huu ni mfano wa matokeo:


```
gpg: Signature made lun 11 nov 2024, 00:39:04 CET
gpg:                using RSA key 5720CD577E7894C98DBD580E8F12D0C63B1A606E
gpg:                issuer "admin@planb.network"
gpg: Good signature from "PlanB Network (used for PBN platform) <admin@planb.network>" [unknown]
```


Ukiona ujumbe kama "saini MBAYA", hiyo inamaanisha kuwa faili imechezewa.


## Hatua ya 3: Kuthibitisha Open Timestamp


### Inathibitisha kupitia Graphical Interface


1. Tembelea tovuti ya OpenTimestamps: https://opentimestamps.org/

2. Bofya kwenye kichupo cha "Stamp & Thibitisha".

3. Buruta na udondoshe faili ya OTS (k.m. `certificate.txt.ots`) kwenye eneo lililoteuliwa.

4. Buruta na udondoshe faili iliyopigwa chapa (k.m. `certificate.txt`) kwenye eneo lililoteuliwa.

5. Tovuti itathibitisha kiotomatiki Timestamp iliyo wazi na kuonyesha matokeo.


Ukiona ujumbe kama ufuatao, Timestamp ni halali:


![cover](assets/opentimestamp_wegui_verified.webp)


### Njia ya CLI


KUMBUKA: utaratibu huu **utahitaji nodi ya ndani ya Bitcoin **


1. Sakinisha mteja wa OpenTimestamps kutoka [harusi] rasmi (https://github.com/opentimestamps/opentimestamps-client) kwa kutekeleza amri ifuatayo:


```
pip install opentimestamps-client
```


2. Nenda kwenye saraka iliyo na faili za cheti zilizotolewa.


3. Tekeleza amri ifuatayo ili kuthibitisha Timestamp iliyofunguliwa:


```
ots verify certificate.txt.ots
```


Amri hii itakuwa:



- Angalia Timestamp dhidi ya Blockchain ya Bitcoin
- Onyesha ni lini faili iliwekwa muhuri wa wakati
- Thibitisha uhalisi wa Timestamp


### Matokeo ya mwisho


Uthibitishaji umefaulu ikiwa **jumbe zote mbili** zitaonyeshwa:


1. Sahihi ya GPG imeripotiwa kama **"Sahihi nzuri kutoka kwa Plan ₿ Network"**

2. Uthibitishaji wa OpenTimestamps unaonyesha kitalu mahususi cha Bitcoin Timestamp na kuripoti **"Mafanikio! Kizuizi cha Bitcoin [blockheight] kinathibitisha data ilikuwepo tangu [Timestamp]"**


Kwa kuwa sasa unajua jinsi Plan ₿ Network hutoa uthibitisho unaoweza kuthibitishwa kwa Cheti na Diploma yoyote ya ₿-CERT, unaweza kuthibitisha kwa urahisi uaminifu wao.