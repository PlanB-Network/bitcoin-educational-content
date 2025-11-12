---
name: Keki Wallet
description: Mafunzo kuhusu Keki Wallet na Malipo ya Kimya
---

![cover](assets/cover.webp)


Mwongozo huu unachunguza [**Keki Wallet**](https://cakewallet.com/): wallet ya chanzo huria, isiyo ya ulezi, inayozingatia ufaragha inayopatikana kwa Android, iOS, macOS, Linux na Windows. Tutachunguza vipengele vyake vya faragha vya Bitcoin mahususi, tutapitia kutuma/kupokea Bitcoin kupitia **Malipo ya Kimya** (itifaki iliyoboreshwa ya faragha ya on-chain) na tutaangalia utekelezaji wa PayJoin v2 kwa miamala isiyolingana.


## 🎉 Sifa Muhimu



- [**Malipo ya Kimya (BIP-352)**](https://bips.dev/352/) kuboresha nambari za awali za malipo za [BIP 47](https://silentpayments.xyz/docs/comparing-proposals/bip47/) pia huitwa "PayNyms" yenye anwani ya siri inayoweza kutumika tena. Mtumaji anapotumia anwani yako ya Malipo ya Kimya, wallet yake hupata anwani ya kipekee ya mara moja kwa kutumia funguo tofauti ambazo zitaunganishwa kuwa anwani ya kipekee ya mara moja ya Taproot. Rekodi za blockchain zinaonyesha shughuli zisizohusiana, kuzuia uhusiano wa malipo yanayoingia. Malipo ya Kimya hutoa manufaa mbalimbali, ikiwa ni pamoja na:
    - Anwani zinazoweza kutumika tena: Hakuna haja ya generate anwani mpya kwa kila shughuli, kutoa matumizi bora ya mtumiaji na kuongezeka kwa faragha.
    - Ongezeko la gharama sifuri: Malipo ya Kimya hayaongezi ukubwa au gharama ya miamala.
    - Hali ya kutokujulikana iliyoimarishwa: Waangalizi wa nje hawawezi kuunganisha miamala na anwani ya Malipo ya Kimya.
    - Hakuna mwingiliano wa mtumaji na mpokeaji unaohitajika: Miamala inaweza kufanywa bila mawasiliano yoyote kati ya wahusika.
    - Anwani za kipekee kwa kila malipo: Kuondoa hatari ya kutumia tena anwani kimakosa.
    - Hakuna seva inayohitajika: Malipo ya Kimya yanaweza kufanywa bila hitaji la seva iliyojitolea.
- PayJoin v2** hupunguza uchanganuzi wa grafu ya shughuli kwa kuunganisha ingizo za watumaji na wapokeaji katika muamala mmoja. Keki Wallet inatekeleza maendeleo mawili muhimu:
    - Miamala Isiyolingana**: Mtumaji na mpokeaji hahitaji tena kuwa mtandaoni kwa wakati mmoja ili kukamilisha muamala wa faragha.
    - Mawasiliano Isiyo na Seva**: Hakuna mhusika anayehitaji kuendesha seva ya Payjoin, na kuondoa kizuizi kikubwa cha kiufundi.
- Udhibiti wa Coin** huwasha uteuzi wa UTXO wakati wa miamala. Hii inazuia muunganisho wa kiajali wa anwani wakati wa kutumia UTXO nyingi zenye asili tofauti.
- Msaada wa TOR**, kuruhusu watumiaji kuelekeza trafiki ya mtandao wao kupitia mtandao wa Tor
- RBF** (Replace-By.Fee) hukuwezesha kurekebisha ada baada ya kutuma muamala.


## 1️⃣ Kuweka Wallet Yako


Keki Wallet inatoa anuwai ya usaidizi wa jukwaa. Unaweza kuchagua kati ya `Android`, `iOS / macOS` , `Linux` na `Windows`.  Ili kuanza, tembelea https://docs.cakewallet.com/get-started/ na uchague mfumo wako wa uendeshaji.


![image](assets/en/01.webp)


Baada ya kusakinisha, weka `PIN`  (tarakimu 4 au 6). Kisha utaona:


1. `Unda Wallet Mpya` (kwa watumiaji wapya)

2. `Rejesha Wallet` (kwa pochi zilizopo)


![image](assets/en/02.webp)


Kwenye skrini inayofuata unaweza kuchagua kati ya aina mbalimbali za fedha taslimu. Chagua `Bitcoin` na uguse `Inayofuata` na utoe `jina la Wallet` ili kutambua wallet. Kwa kugonga `Mipangilio ya Kina` anuwai ya `Mipangilio ya Faragha` huonekana. Fanya mabadiliko haya:



- Fiat API:** chagua `Tor Only` (hutuma maombi ya bei kupitia Tor)
- Badili:** chagua `Tor Only` (haitambulishi trafiki ya ubadilishanaji)


Aina ya BIP-39 seed inazalishwa kwa chaguo-msingi, na chaguo la kubadilisha kwa aina ya Electrum seed. Njia za uundaji ni zifuatazo:



- Electrum: `m/0'`
- BIP-39: `m/84'/0'/0`


Ikiwa ungependa kuongeza safu ya ziada ya usalama, unaweza kusanidi `passphrase`.  Kusudi kuu la passphrase ni kutoa ulinzi wa ziada dhidi ya mashambulizi ya kimwili. Hata kama mshambuliaji atapata maneno ya seed, hawezi kufikia wallet yako bila passphrase sahihi. Kwa maneno mengine, maneno ya seed pekee yanawakilisha wallet moja, wakati maneno ya seed pamoja na passphrase yanaunda wallet tofauti kabisa na hakuna uhusiano na asili. Kipengele hiki pia huwezesha `pochi za siri` zinazolindwa na passphrase, na hukupa ukanusho unaokubalika. Katika hali ya kulazimisha, unaweza kufichua maneno ya seed huku ukiweka vipengee vikubwa salama katika passphrase-iliyolindwa wallet.


Ikiwa tayari unaendesha nodi yako mwenyewe, geuza `Ongeza Nodi Mpya Maalum` na utoe `Node Address` yako ili kuthibitisha miamala na vizuizi ndani ya miundombinu yako mwenyewe. Mara baada ya kumaliza gonga kwenye `Endelea` na `Inayofuata` ili kuunda wallet yako.


![image](assets/en/03.webp)


Kwenye skrini inayofuata, unapata kanusho:


```
On the next page you will see a series of words. This is your unique and private seed and it is the ONLY way to recover your wallet in case of lass or malfunction. It is YOUR responsibility to write it down and store it in a safe place outside of the Cake Wallet app.
```


![image](assets/en/04.webp)


Ili kujifunza mbinu bora za kuhifadhi maneno yako ya mafumbo, tafadhali soma mafunzo haya:


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Gusa `Ninaelewa. Nionyeshe seed yangu` na uhifadhi maneno haya mahali salama! Kisha uguse `Thibitisha seed` na baada ya uthibitishaji `Fungua Wallet`.


## 2️⃣ Mipangilio


Kabla hatujazama zaidi, hebu tuangalie `Skrini ya Nyumbani` na `Mipangilio`.


Kwenye Skrini ya Nyumbani tunaweza kuona vipengee tofauti vinavyoonyeshwa:



- `Menyu ya Hamburger` inatuleta kwenye `mipangilio`
- Salio Inapatikana
- Kadi ya Malipo ya Kimya ili Kuanza kuchanganua miamala inayotumwa kwa anwani yako ya Malipo ya Kimya
- Kadi ya kujiunga na malipo ya `Wezesha` Payjoin kama kipengele cha kuhifadhi faragha na kuokoa ada
- chini kuna Njia za mkato za `Muhtasari wa Wallet`, `Pokea`, `Badilisha` kati ya Bitcoin na sarafu nyinginezo, `Tuma` na `Nunua`


![image](assets/en/11.webp)


Kugonga aikoni ya `Menyu ya Hamburger` hufungua menyu ya mipangilio. Hebu tuangalie chaguzi.


![image](assets/en/05.webp)


### A - Muunganisho na usawazishaji 🔗


Hapa, tunaweza kuunganisha tena wallet, kudhibiti nodi, na kuunganisha kwenye nodi yetu wenyewe (inapendekezwa). `Uchanganuzi wa Malipo ya Kimya` huturuhusu kubinafsisha uchanganuzi kwa kubainisha ama `Changanua kutoka urefu wa kizuizi` au `Changanua kuanzia tarehe`.


![image](assets/en/06.webp)


Kama kipengele cha `Alpha` pia kuna chaguo la `Kuwezesha Tor iliyojengewa ndani` ili kuelekeza trafiki kupitia mtandao wa Tor.


### B - Mipangilio ya Malipo ya Kimya 🔈


Tunaweza kugeuza kadi ya Malipo ya Kimya kwenye Skrini ya kwanza ili kuonyesha kipengele hiki. Kuwasha `Kuchanganua kila wakati` huruhusu wallet kufuatilia mfululizo blockchain kwa Malipo ya Kimya yanayoingia. Tunaweza kubainisha vigezo vya kuchanganua ili kubinafsisha mchakato wa kuchanganua kulingana na mahitaji yetu kama ilivyoelezwa hapo juu.


![image](assets/en/07.webp)


### C - Usalama na chelezo 🗝️


Ili kulinda wallet yetu, tunaweza kuunda hifadhi rudufu kwa kufuata madokezo ya ndani ya programu. Hii itahakikisha kuwa tuna nakala salama ya funguo zetu za faragha, na kuturuhusu kurejesha wallet yetu ikiwa itapotea au kuibiwa. Zaidi ya hayo, tunaweza kuona maneno yetu ya seed na funguo za faragha, kubadilisha PIN yetu, kuwezesha uthibitishaji wa kibayometriki, Saini / Thibitisha na usanidi 2FA kwa safu ya ziada ya ulinzi.


![image](assets/en/08.webp)


**Kumbuka**: Kuanzia Septemba 2025, uthibitishaji wa bayometriki wa alama za vidole kwenye vifaa vya Android unahitajika ili kufanya kazi na angalau utekelezaji wa kibayometriki wa Daraja la 2, kwa maelezo zaidi angalia [hapa](https://source.android.com/docs/security/features/biometric/measure#biometric-classes). Walakini, hitaji hili linaweza kubadilika katika siku zijazo.


### D - Mipangilio ya Faragha 🔒


Tunaweza pia kuimarisha usalama wa wallet yetu kwa kutumia Tor kusimba muunganisho wetu wa intaneti kwa njia fiche na kulinda faragha yetu tunapofikia vyanzo vya nje. Zaidi ya hayo, tunaweza kuzuia picha za skrini ili kuweka maelezo yetu ya wallet kuwa siri, kuwezesha anwani zinazozalishwa kiotomatiki kuunda mpya kwa kila muamala, na kuzima vitendo vya kununua/kuuza ili kuzuia miamala ambayo haijaidhinishwa. Zaidi ya hayo tunaweza `Kuwezesha PayJoin`, ambacho ni kipengele kingine cha faragha tutakagua baadaye.


![image](assets/en/09.webp)


### E - Mipangilio mingine 🔧


Mipangilio mingine huturuhusu kudhibiti kipaumbele cha ada na kuweka kiwango cha ada chaguo-msingi kwa miamala yetu. Hii hutuwezesha kudhibiti ada za muamala zinazohusiana na Malipo yetu ya Kimya, kwa kuzingatia matumizi ya sasa ya mtandao.


![image](assets/en/10.webp)


## 3️⃣ Kupokea ₿itcoin kwa kutumia Malipo ya Kimya


Kuna chaguo kadhaa na aina za anwani zinazopatikana kwa kupokea Bitcoin. `Segwit (P2WPKH)` *(kuanzia na bc1q....)* ndilo chaguo-msingi.  Hebu tuchague `Malipo ya Kimya` katika mfano huu.


Ili kupokea Malipo ya Kimya, gusa kwanza aikoni ya `Pokea` katika Keki ya Wallet. Ifuatayo, weka kiasi unachotarajia kupokea. Ili kubainisha aina ya anwani, gusa `Pokea` tena juu ya skrini, kisha uchague `Malipo ya Kimya` kutoka kwa chaguo.


Kwenye skrini kuu, msimbo na anwani yako ya Malipo ya Kimya inayoweza kutumika tena itaonyeshwa. Kama inavyotarajiwa, anwani ni ndefu sana:


`sp1qq0ryu780uwragyk06prxn29830a9csnl3wvr4as6fwh73rzn28zzcqmc6ve36vadllfztaa403ty9et0rlzup7kt55qh486gxzrde6y25p8s`.


![image](assets/en/12.webp)


Sasa, tumia wallet inayooana ya BIP-352 (kama vile Blue Wallet) kuchanganua msimbo huu wa QR na kutuma malipo. Utaona kwamba wallet inapata anwani ya kipekee lengwa kutoka kwa anwani yako ya kimya.


![image](assets/en/13.webp)


## 4️⃣ Kutuma ₿itcoin kwa kutumia Malipo ya Kimya


Kwa vile Blue Wallet inaweza `Kutuma` Malipo ya Kimya tu, tutatumia BIP 352 nyingine inayooana ya wallet kama mhusika anayepokea. Mchakato huu ni sawa na ule wa muamala wa kawaida wa Bitcoin.



- Gusa `Tuma` kwenye Skrini ya Kwanza
- ama kubandika anwani yetu ya `sp1qq...` inayoweza kutumika tena au kuchanganua msimbo wa QR moja kwa moja ndani ya programu.
- Chagua ni kiasi gani ungependa kutumia kutoka kwenye salio lako linalopatikana
- Gonga kwenye `Tuma` chini ya skrini ili kuthibitisha muamala


Mara tu tunapoweka anwani `sp1qq...`, wallet itapata kiotomatiki `bc1p...` anwani inayolingana ya Taproot (P2TR) chinichini, ambayo itatumika kwa Malipo ya Kimya.


Tunaweza kwa hiari kuandika dokezo la ndani kwa kila muamala, kurekebisha mipangilio ya ada au kuchagua UTXO fulani kwa muamala kwa kutumia kipengele cha `Coin Control`.


![image](assets/en/14.webp)


`Telezesha kidole kulia ili kuthibitisha muamala.


Ukishatuma muamala, utaulizwa ikiwa ungependa kuongeza mtu huyu kwenye kitabu chako cha anwani.


![image](assets/en/15.webp)


## 5️⃣ PayJoin


Hebu tuangalie PayJoin ni nini [kuhusu](https://docs.cakewallet.com/cryptos/bitcoin/#payjoin):


_Payjoin v2 ni kipengele cha kuhifadhi faragha na kuokoa ada katika Bitcoin ambacho huruhusu mtumaji na mpokeaji wa muamala kufanya kazi pamoja ili kuunda muamala mmoja. Muamala huu una mchango kutoka kwa *wote* mtumaji na mpokeaji, na kuvunja mbinu za kawaida za uchunguzi dhidi ya Bitcoin na kuruhusu uokoaji bora wa ada na uokoaji katika hali fulani pia._


Ili kufahamu zaidi kuhusu PayJoin unaweza pia kutembelea mafunzo yafuatayo.


https://planb.academy/tutorials/privacy/on-chain/payjoin-848b6a23-deb2-4c5f-a27e-93e2f842140f

Ili kutumia PayJoin pande zote mbili kunahitaji wallet inayooana ya PayJoin, na mpokeaji anahitaji kuwa na angalau sarafu moja au pato katika wallet yao. Ili kuanza tafadhali fuata hatua hizi:


1. Gusa `Menyu ya Hamburger` na uguse kitufe cha `Faragha`

2. Geuza Chaguo la `Tumia Payjoin`

3. Gonga kwenye `Pokea` kwenye Skrini ya kwanza na utawasilishwa na PayJoin QR Code na kitufe cha kunakili (ukichaguliwa Segwit)


![image](assets/en/16.webp)


## 6️⃣ Vipengele vingine


Kuna vipengele vingine kadhaa kama vile chaguo za `Kubadilishana` kwa sarafu nyingi, `Nunua na Uuze` zilizo na miunganisho tofauti ya wachuuzi na programu mahususi za Keki kama vile `Cake Pay`, ambayo hukuwezesha kununua kadi za kulipia kabla au kadi za zawadi.


![image](assets/en/17.webp)


## 🎯 Hitimisho


Haya ni mapitio yetu ya Keki Wallet, ambayo inatoa shukrani za faragha za Bitcoin kwa vipengele kama vile Malipo ya Kimya (BIP-352) na Payjoin v2.


Malipo ya Kimya hubadilisha anwani zinazoweza kutumika kwa anwani za siri zinazoweza kutumika tena ili kuzuia muunganisho wa on-chain wa miamala inayoingia. Ingawa masuala ya kusawazisha matoleo ya awali yameboreshwa sana, kuna baadhi ya mahitaji ya hesabu yaliyoongezeka ya kuchanganua na kugundua Malipo ya Kimya yanayohitajika, na kudai rasilimali zaidi na kipimo data.


Payjoin v2 inatatiza uchanganuzi wa msururu kwa kuunganisha pembejeo za mtumaji na mpokeaji katika miamala moja bila ada za ziada au uratibu mkuu. Hii inavunja kanuni ya kawaida ya umiliki wa pembejeo, ambayo ni faida kubwa kwani inamaanisha huwezi kudhani kuwa ingizo zote ni za mtumaji.


Kwa watumiaji wanaotanguliza kutokujulikana kwa fedha, Keki Wallet ni chaguo linalofaa. Inajumuisha itifaki za faragha moja kwa moja katika utendakazi wake mkuu, na kuzifanya zipatikane bila utata wowote wa kiufundi. Kadiri ufuatiliaji kwenye blockchains za umma unavyoongezeka, zana kama huu husaidia kudumisha ufaragha wa shughuli ambapo ni muhimu zaidi. Utekelezaji mpana wa viwango hivi ndani ya mandhari ya wallet itakuwa maendeleo yanayokaribishwa.


## 📚 Rasilimali


https://cakewallet.com


https://docs.cakewallet.com/


https://github.com/cake-tech/cake_wallet


https://blog.cakewallet.com/


[https://silentpayments.xyz/](https://silentpayments.xyz/)


[ttps://bips.dev/352/](https://bips.dev/352/)


https://payjoin.org/