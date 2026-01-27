---
name: Coin Wallet
description: Mafunzo kuhusu Coin Wallet na njia za kuimarisha faragha na usalama
---

![cover](assets/cover.webp)


Mafunzo haya yanashughulikia [Coin Wallet](https://coin.space/) - mfumo wa siri wa wallet unaojihifadhi kwa vifaa vya mkononi, na jinsi ya kuongeza usalama na faragha unapotumia programu za simu za wallet.



## Kuhusu Coin Wallet


**Coin Wallet** ni wallet inayojilinda/isiyo ya ulinzi, chanzo huria iliyoundwa na timu ya wapenzi wa Bitcoin mnamo 2015. Ilianza kama programu ya wavuti, ikifuatiwa na programu ya iOS mnamo 2017, na programu ya Android mnamo 2020 - inapatikana kwenye Google Play, Duka la Samsung Galaxy, na Huawei AppGallery.


Faida muhimu:


- Usanifu usio wa ulinzi
- [Msimbo wa chanzo huria] kikamilifu (https://github.com/CoinSpace/CoinSpace/blob/master/LICENSE)
- Muundo rahisi na safi
- Kuzingatia lengo kuu - kuhifadhi sarafu za kidijitali kwa usalama, bila vipengele visivyo vya lazima
- Usaidizi wa mifumo mbalimbali: simu (iOS na Android), kompyuta ya mezani, wavuti
- Usaidizi wa RBF (Badilisha-Kwa-Ada) - ongeza kasi ya miamala iliyokwama wakati wowote
- Vifaa 2FA vyenye [YubiKey](https://www.yubico.com/works-with-yubikey/catalog/coin-wallet/) / ufunguo wa FIDO2
- Usaidizi wa Tor uliojengewa ndani - elekeza trafiki yote kupitia mtandao wa Tor kwa faragha ya juu zaidi



## 1️⃣ Kusakinisha Coin Wallet

Coin Wallet inapatikana kwenye mifumo yote mikubwa.



- [Duka la Programu la iOS](https://apps.apple.com/app/coin-wallet-bitcoin-crypto/id980719434)



- [Google Play ya Android](https://play.google.com/store/apps/details?id=com.coinspace.app)



- [Android (Duka la Galaxy)](https://galaxystore.samsung.com/detail/com.coinspace.app)



- [Android (Huawei AppGallery)](https://appgallery.huawei.com/app/C112183767)



- [Android (Uptodown)](https://coin-wallet.en.uptodown.com/android)



- [APK ya Android](https://coin.space/api/v3/download/android-apk/any)



- [Viungo vyote vya kutolewa](https://github.com/CoinSpace/CoinSpace/releases)


Inapatikana pia kwa kompyuta za mezani (Windows, Linux, macOS), kama programu ya wavuti na kupitia Tor.


![image](assets/en/01.webp)


## 2️⃣ Kuunda Wallet na Kuweka PIN


wallet imeundwa kwa kutumia passphrase - mfuatano nasibu wa maneno 12 yaliyotenganishwa na nafasi, yaliyotokana na [orodha ya maneno 2048](https://github.com/paulmillr/scure-bip39/blob/main/src/wordlists/english.ts).

Coin Wallet inasaidia manenosiri 12, 15, 18, 21, au 24 yaliyoingizwa kutoka kwa pochi zingine.


passphrase ni umbo linaloweza kusomwa na binadamu la ufunguo mkuu wa faragha. Lazima lihifadhiwe kwa usalama. passphrase ndiyo inayohitajika tu ili kufikia au kurejesha wallet. Ikiwa passphrase itapotea, wallet na fedha zote zitapotea kabisa. passphrase haipaswi kamwe kushirikiwa. Coin Wallet haihifadhi funguo kwenye seva au hifadhidata yoyote.


**Je, passphrase yenye maneno 12 iko salama?**

Kwa maneno 2048 yanayowezekana kwa kila nafasi, kuna michanganyiko ya 2048¹² ≈ 10³⁹ — inayotoa biti ~128 za usalama, zinazolingana na funguo za kibinafsi za Bitcoin. Kiwango hiki kinachukuliwa kuwa cha kutosha sana.


![image](assets/en/02.webp)


Baada ya passphrase kuandikwa na kuthibitishwa, programu inaomba kuweka PIN ya tarakimu 4** kwa ufikiaji wa kila siku. Kwa urahisi zaidi, unaweza kuwezesha uthibitishaji wa kibiometriki (alama ya vidole au utambuzi wa uso) badala ya kutumia PIN.


![image](assets/en/03.webp)



Hakuna akaunti, hakuna urejeshaji wa funguo, hakuna uwekaji upya wa passphrase, na hakuna ubadilishaji wa muamala. Usalama ni jukumu kamili la mtumiaji.


Kwa maelezo zaidi kuhusu mbinu bora za kuhifadhi kifungu cha kumbukumbu:


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270


## 3️⃣ Nenosiri + PIN. Wakati na Jinsi Zinatumika


**passphrase inahitajika lini?**

Ni katika visa hivi adimu tu:


- Kusanidi wallet kwenye kifaa kipya
- Kusakinisha upya programu ya Coin Wallet
- Kufuta data ya programu/kivinjari (Hifadhi ya Ndani)
- Kuondoa ufunguo wa vifaa kutoka kwa akaunti
- Kuingiza PIN isiyo sahihi mara tatu (programu hufunga kwa usalama)


Katika matumizi ya kila siku, PIN ya tarakimu 4 inatosha kufungua wallet.


**Nenosiri + PIN: Jinsi Inavyofanya Kazi**

passphrase ndiyo ufunguo mkuu wa kibinafsi na inafanya kazi kwenye kifaa chochote.

Kwa kuwa kuandika maneno 12–24 kila wakati itakuwa vigumu, Coin Wallet hutumia PIN ya tarakimu 4 kwa ufikiaji wa haraka na wa kila siku kwenye kifaa cha sasa.

PIN rahisi pekee haina usalama wa kutosha kulinda ufunguo mkuu moja kwa moja, kwa hivyo haitumiki kamwe kwa usimbaji fiche. Badala yake:



- PIN hutumwa kwa seva na kubadilishwa kwa token ndefu ya usimbaji fiche.
- token hii huondoa msimbo wa siri wa ufunguo mkuu uliosimbwa kwa njia fiche uliohifadhiwa kwenye kifaa pekee.


Ikiwa PIN imeingizwa vibaya mara tatu, seva hufuta kabisa token. Kitufe kilichohifadhiwa ndani huwa hakitumiki, na njia pekee ya kurejesha wallet ni kwa kuingiza passphrase ya asili.

Muundo huu hutoa urahisi na ulinzi imara wa kurudi nyuma.



## 4️⃣ Kupokea ₿itcoin - Aina za Address na Faragha


Coin Wallet inasaidia miundo yote mitatu ya anwani ya Bitcoin:



- SegWit Asili (Bech32)** – huanza na **bc1q** – ada za chini kabisa, zinazopendekezwa
- SegWit iliyo na kiota (P2SH)** – huanza na **3**
- Legacy (P2PKH)** – huanza na **1**


![image](assets/en/04.webp)


**Kwa nini anwani hubadilika baada ya kila amana?**

Hii ni kwa makusudi na inalinda faragha. Kila wakati sarafu zinapopokelewa, Coin Wallet hutoa kiotomatiki anwani mpya isiyotumika. Ikiwa anwani hiyo hiyo ingetumika tena (kwa mfano, kwa mshahara wa kila mwezi), mtu yeyote angeweza kujumlisha kwa urahisi miamala yote inayoingia kwenye blockchain explorer na kujua jumla ya mapato.


Anwani za zamani hubaki halali milele - bado unaweza kuzipokea - lakini kutumia anwani mpya kila wakati ndio njia bora ya faragha inayopendekezwa.


**Jinsi ya kupokea Bitcoin:**

1. Fungua sarafu

2. Gusa **Pokea**

3. Chagua aina ya anwani unayotaka (ikiwezekana **bc1q** – `Native SegWit`)

4. Onyesha msimbo wa QR au nakili anwani na uitumie kwa mlipaji


**Si lazima - Mecto (kwa malipo ya ana kwa ana):**

Kwenye skrini hiyo hiyo ya Kupokea kuna kitufe cha `Mecto`.

Unapoiwasha:


- Utaulizwa kuingiza jina la utani la **** (gravatar)
- Eneo lako la sasa na anwani ya kupokea zinashirikiwa kwa muda na watumiaji wengine wa Coin Wallet ambao pia wamewasha Mecto
- Wanaweza kukugundua kwenye ramani ndogo na kutuma sarafu bila kuandika au kuchanganua


Data inaonekana tu kwa watumiaji wengine wa Mecto na hufutwa kiotomatiki baada ya saa 1 (au mara tu unapoizima).

Mecto ni hiari kabisa - achana nayo ikiwa unapendelea faragha ya hali ya juu.


![image](assets/en/05.webp)


## 5️⃣ Kutuma ₿itcoin


Kutuma Bitcoin:


1. Fungua sarafu → gusa **Tuma**

2. Bandika anwani au changanua msimbo wa QR

3. Ingiza kiasi (au gusa **Kiwango cha Juu**)

4. Chagua kasi ya muamala:


| Speed   | Approx. confirmation time | Fee level     |
|---------|---------------------------|---------------|
| **Slow**    | ~120 minutes              | Lowest
| **Default** | ~60 minutes               | Medium
| **Fast**    | ~20 minutes               | Higher

5. Thibitisha kwa kutumia PIN yako ya tarakimu 4 → muamala unatangazwa


### Jinsi ya kuharakisha muamala unaosubiriwa wa ₿itcoin (RBF)


Ukichagua ada ya polepole na muamala umekwama:


1. Nenda kwenye kichupo cha **Historia**

2. Gusa muamala unaosubiri kushughulikiwa

3. Gusa **Accelerate** (Badilisha kwa Ada)

4. Thibitisha → muamala utatangazwa tena kwa ada ya juu zaidi


Kuongeza kasi kwa RBF kwa sasa kunaungwa mkono kwa:

Bitcoin • Banguko • Mnyororo Mahiri wa Binance • Ethereum • Ethereum Classic • Poligoni


Zaidi kuhusu Replace-by-fee (RBF): https://bitcoinops.org/en/topics/replace-by-fee/


## 6️⃣ Kuhamisha Funguo za Kibinafsi


**Unahitaji ufunguo wa faragha lini hasa?**

(Asilimia 99 ya watumiaji hawafanyi hivyo kamwe — passphrase yenye maneno 12 inatosha)


| Situation                                      | Why you need the private key                     |
|------------------------------------------------|--------------------------------------------------|
| Sweeping an old paper wallet                   | To move funds to your current wallet             |
| Importing into a hardware signer (e.g. Coldcard) | For offline signing                              |
| Emergency recovery (lost seed but app still open) | To rescue coins before the app is gone           |
| Using tools that don’t accept seed phrases     | Some watch-only or signing utilities             |

### Jinsi ya kusafirisha funguo za kibinafsi katika Coin Wallet


1. Fungua **Bitcoin (BTC)**

2. Sogeza hadi chini ya ukurasa - gusa **Hamisha funguo za faragha**

3. Programu inaonyesha kila anwani yenye salio + ufunguo wake wa faragha katika umbizo la **WIF** (huanza na 5, K, au L) na msimbo wa QR.


Anwani zisizo tupu pekee ndizo zinazoonekana.


**Mfano wa ufunguo wa WIF**

`L2v1eK4i9j3k3j4k3j4k3j4k3j4k3j4k3j4k3j4k3j4k3j4k3j4k3j4k`


**Cha kufanya baadaye (inapendekezwa)**


- Fungua Electrum, Sparrow, BlueWallet au vifaa vyovyote vya wallet
- Ingiza/Futa ufunguo wa faragha
- Fedha zote huhamishiwa mara moja kwenye anwani mpya salama chini ya seed yako ya sasa


Usihifadhi ufunguo wa faragha kidijitali katika maandishi wazi. Baada ya kufagia, unaweza kufutwa kwa usalama.


Kwa mwongozo kamili kuhusu funguo za kibinafsi na njia za uundaji: [Jinsi ya Kufanya Kazi na Funguo za Kibinafsi: Mwongozo wa Mwisho](https://coin.space/how-to-work-with-private-keys-the-ultimate-guide/)



## 7️⃣ Maelezo ya Kiufundi - BIP39, BIP32 na Njia za Utoaji


Coin Wallet inafuata kikamilifu viwango rasmi vya Bitcoin ambavyo hutumiwa na karibu pochi zote kubwa.


`BIP39` - jinsi passphrase inavyokuwa ufunguo mkuu wa faragha


- Idadi chaguo-msingi ya maneno: 12
- passphrase/nenosiri la hiari: hakuna ("")
- Entropi ya awali: biti 128 (maneno 12) → biti 256 (maneno 24)
- Utekelezaji wa programu huria: https://github.com/paulmillr/scure-bip39
- Orodha ya maneno: orodha ya kawaida ya Kiingereza yenye maneno 2048
- Inasaidia uingizaji wa vifungu vya maneno 12, 15, 18, 21 na 24 kutoka kwa BIP39 wallet nyingine yoyote.


`BIP32 + BIP44/BIP49/BIP84` - kizazi cha anwani zote kwa njia ya uhakika

Kutoka kwa ufunguo mmoja mkuu, wallet inaweza kutoa anwani bilioni 82 za generate kwa mpangilio maalum. Hii ndiyo sababu maneno yaleyale 12 yaliyoingizwa katika Electrum, Sparrow, Trezor, Ledger, BlueWallet, n.k. yataonyesha anwani na mizani sawa kabisa.


**Njia za uondoaji zinazotumika katika Coin Wallet kwa Bitcoin**


| Address type              | Standard | Derivation path       | Starts with | Comment                              |
|---------------------------|----------|-----------------------|-------------|--------------------------------------|
| Native SegWit (Bech32)    | BIP84    | `m/84'/0'/0'`         | bc1q…       | Modern format, lowest fees           |
| Nested SegWit (P2SH)      | BIP49    | `m/49'/0'/0'`         | 3…          | Compatibility wrapper for old services |
| Legacy (P2PKH)            | BIP44    | `m/44'/0'/0'`         | 1…          | Oldest format, highest fees          |

Ndani ya kila njia:


- `/0` — mnyororo wa nje (anwani unazoonyesha ili kupokea malipo)
- `/1` — mnyororo wa ndani (badilisha anwani ambazo wallet hutumia yenyewe)


Kwa sababu Coin Wallet inafuata viwango hivi vya umma bila mabadiliko yoyote, fedha zako zitabaki kupatikana katika wallet nyingine yoyote inayolingana hata katika miaka 10-20-30.


## 8️⃣ Kuimarisha Kutokujulikana kwa Tor


**Kwa nini utumie Tor katika Coin Wallet**

Tor huficha anwani yako halisi ya IP kutoka kwa nodi za Bitcoin, kubadilishana, na waangalizi.

Trafiki zote (salio, miamala, ubadilishaji) hupitia mtandao wa Tor - hakuna miunganisho ya moja kwa moja, hakuna uvujaji wa IP.

Hii inatekelezwa moja kwa moja katika msimbo chanzo wa programu (tazama [usanidi wa .env](https://github.com/CoinSpace/CoinSpace/blob/master/web/.env#L31)).


Coin Wallet ina anwani ya .onion iliyofichwa na, tangu v6.6.3 (Desemba 2024), **Tor iliyojengewa ndani inasaidia moja kwa moja kwenye programu ya simu**.


### Jinsi ya kuwezesha Tor kwenye Android na iOS


1. **Sakinisha Orbot** - programu rasmi ya Tor Project (bila malipo)


   - Android → [Google Play](https://play.google.com/store/apps/details?id=org.torproject.android) / [F-Droid](https://orbot.app/en/)
   - iPhone / iPad → [Duka la Programu](https://apps.apple.com/us/app/orbot/id1609461599)


2. **Fungua Orbot → gusa Anza**

Chagua **Coin Wallet** kutoka kwenye orodha ili wallet pekee ndiyo inatumia Tor (hiari lakini inapendekezwa)

Subiri hadi itakaposema **"Imeunganishwa"** (sekunde 10–30)


3. **Fungua Coin Wallet → Mipangilio → Mtandao**

Washa **Tumia Tor**


4. **Angalia hali**

Aikoni ya kitunguu cha **zambarau cha Tor** inaonekana kwenye upau wa juu → trafiki yote sasa inapitia Tor


![image](assets/en/06.webp)


Hiyo ndiyo yote - Coin Wallet yako ya mkononi haina jina kabisa.


Furahia usimamizi wa crypto binafsi!


## 📝 Hitimisho


[Coin Wallet](https://coin.space/) - mmoja wa waanzilishi wa kweli wa Bitcoin wallet mwenye historia ya maendeleo ya miaka 10.

Ni rahisi kimakusudi na inabaki ikizingatia lengo lake kuu: kuhifadhi sarafu yako ya kidijitali kwa usalama.

Hakuna matangazo, hakuna habari, hakuna usajili, hakuna vipengele vya kijamii, hakuna visumbufu - ni wallet safi, ya haraka, na inayojilinda yenyewe ambayo hufanya kile inachopaswa kufanya.

Coin Wallet inaweka urahisi na usalama kwanza - daima imekuwa, daima itakuwa.


## 📖 Rasilimali


https://coin.space/


https://support.coin.space/hc/en-us


https://sw.bitcoin.it/wiki/Wallet


https://bitcoinops.org/


https://github.com/CoinSpace/CoinSpace/


https://www.yubico.com/works-with-yubikey/catalog/coin-wallet/


https://github.com/paulmillr/scure-bip39/blob/main/src/wordlists/english.ts


https://github.com/paulmillr/scure-bip39