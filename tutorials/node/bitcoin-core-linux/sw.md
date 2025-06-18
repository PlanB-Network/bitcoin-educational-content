---
name: Bitcoin Core (Linux)
description: Kuendesha nodi yako mwenyewe na Bitcoin Core
---

![cover](assets/cover.webp)


# Kuendesha nodi yako mwenyewe na Bitcoin Core


Utangulizi wa Bitcoin na dhana ya nodi, inayokamilishwa na mwongozo wa kina wa usakinishaji kwenye Linux.


Moja ya mapendekezo ya kusisimua zaidi ya Bitcoin ni uwezo wa kuendesha programu mwenyewe, na hivyo kushiriki katika ngazi ya punjepunje katika mtandao na uthibitishaji wa shughuli za umma Ledger.


Bitcoin, mradi wa chanzo huria, umesambazwa hadharani na unapatikana bila malipo tangu 2009. Takriban miaka 15 baada ya kuanzishwa, Bitcoin sasa ni mtandao thabiti na usiozuilika wa fedha wa kidijitali, unaonufaika na athari kubwa ya mtandao wa kikaboni. Kwa juhudi na maono yao, Satoshi Nakamoto inastahili shukrani zetu. Kwa njia, tunakaribisha karatasi nyeupe ya Bitcoin hapa kwenye Agora 256 (kumbuka: pia kwenye chuo kikuu).


## Kuwa benki yako mwenyewe


Kuendesha nodi yako mwenyewe imekuwa muhimu kwa wafuasi wa axiom ya Bitcoin. Bila kuomba ruhusa ya mtu yeyote, inawezekana kupakua Blockchain tangu mwanzo na hivyo kuthibitisha shughuli zote kutoka A hadi Z kulingana na itifaki ya Bitcoin.


Programu pia inajumuisha Wallet yake mwenyewe. Kwa hivyo, tuna udhibiti wa miamala tunayotuma kwa mtandao mwingine wowote, bila mpatanishi au mtu wa tatu. Wewe ni benki yako mwenyewe.


Kwa hivyo kifungu kilichosalia ni mwongozo wa kusakinisha Bitcoin Core - toleo la programu ya Bitcoin inayotumika zaidi - haswa kwenye usambazaji wa Linux unaotangamana na Debian kama vile Ubuntu na Pop!/\_OS. Fuata mwongozo huu ili kuchukua hatua moja karibu na uhuru wako binafsi.


## Mwongozo wa Usakinishaji wa Bitcoin wa Debian/Ubuntu


**Mahitaji**


- Kiwango cha chini cha 6GB cha hifadhi ya data (nodi iliyokatwa) — 1TB ya hifadhi ya data (Full node)
- Ruhusu angalau saa 24 ili kukamilisha Upakuaji wa Kizuizi cha Awali (IBD). Operesheni hii ni ya lazima hata kwa node iliyokatwa.
- Ruhusu ~600GB ya kipimo data kwa IBD, hata kwa nodi iliyokatwa.


**Kumbuka:💡** amri zifuatazo zimefafanuliwa awali kwa toleo la Bitcoin Core 24.1.


## Inapakua na Kuthibitisha Faili


1. Pakua Bitcoin-24.1-x86_64-linux-gnu.tar.gz, pamoja na faili za SHA256SUMS na SHA256SUMS.asc. (https://bitcoincore.org/bin/Bitcoin-core-24.1/Bitcoin-24.1-x86_64-linux-gnu.tar.gz)

2. Fungua terminal kwenye saraka ambapo faili zilizopakuliwa ziko. K.m., cd ~/Vipakuliwa/.

3. Thibitisha kuwa hundi ya faili ya toleo imeorodheshwa katika faili ya hundi kwa kutumia amri sha256sum --ignore-missing --angalia SHA256SUMS.

4. Pato la amri hii linapaswa kujumuisha jina la faili ya toleo iliyopakuliwa ikifuatiwa na "Sawa". Mfano: Bitcoin-24.0.1-x86_64-linux-gnu.tar.gz: Sawa.

5. Sakinisha git kwa kutumia amri sudo install git. Kisha, linganisha hazina iliyo na funguo za PGP za watia saini wa Bitcoin Core kwa kutumia amri ya git clone https://github.com/Bitcoin-core/guix.sigs.

6. Ingiza funguo za PGP za watia sahihi wote kwa kutumia amri gpg --import guix.sigs/builder-keys//\*

7. Thibitisha kuwa faili ya hundi imetiwa saini na funguo za PGP za watia saini kwa kutumia amri gpg --verify SHA256SUMS.asc.


Kila sahihi itarejesha laini inayoanza na: gpg: Sahihi nzuri na laini nyingine inayoishia na alama ya vidole ya ufunguo Msingi: 133E AC17 9436 F14A 5CF1 B794 860F EB80 4E66 9320 (mfano wa alama ya kidole muhimu ya PGP ya Pieter Wuille).


**Kumbuka💡:** si lazima kwa vitufe vyote vya kutia sahihi kurudisha "SAWA". Kwa kweli, moja tu inaweza kuwa muhimu. Ni juu ya mtumiaji kuamua kiwango chao cha uthibitishaji kwa uthibitishaji wa PGP.


Unaweza kupuuza ujumbe ONYO:


- `Ufunguo huu haujathibitishwa kwa saini inayoaminika!`
- `Hakuna dalili kwamba saini ni ya mmiliki.`


## Ufungaji wa Bitcoin Core graphical Interface


1. Katika terminal, bado kwenye saraka ambapo faili ya toleo la Bitcoin Core iko, tumia amri tar xzf Bitcoin-24.1-x86_64-linux-gnu.tar.gz ili kutoa faili zilizomo kwenye kumbukumbu.


2. Sakinisha faili zilizotolewa hapo awali kwa kutumia amri sudo install -m 0755 -o root -g root -t /usr/local/bin Bitcoin-24.1/bin//\*


3. Sakinisha vitegemezi vinavyohitajika kwa kutumia amri sudo apt-get install libqt5gui5 libqt5core5a libqt5dbus5 qttools5-dev qttools5-dev-tools qtwayland5 libqrencode-dev


4. Anza Bitcoin-qt (Bitcoin Core graphical Interface) kwa kutumia amri Bitcoin-qt.


5. Ili kuchagua nodi iliyokatwa, angalia Hifadhi ya Kikomo ya Blockchain na usanidi kikomo cha data cha kuhifadhiwa:


![welcome](assets/1.webp)


## Hitimisho la Sehemu ya 1: Mwongozo wa Ufungaji


Mara baada ya Bitcoin Core kusakinishwa, inashauriwa kuifanya iendelee kadri inavyowezekana ili kuchangia mtandao wa Bitcoin kwa kuthibitisha miamala na kusambaza vizuizi vipya kwa wenzao wengine.


Hata hivyo, kuendesha na kusawazisha nodi yako mara kwa mara, hata kuthibitisha tu shughuli zilizopokelewa na kutumwa, bado ni mazoezi mazuri.


![Creation wallet](assets/2.webp)


# Inasanidi Tor kwa Njia ya Msingi ya Bitcoin


**Kumbuka💡:** mwongozo huu umeundwa kwa ajili ya Bitcoin Core 24.0.1 kwenye usambazaji wa Linux unaooana na Ubuntu/Debian.


## Kufunga na kusanidi Tor kwa Bitcoin Core


Kwanza, tunahitaji kusakinisha huduma ya Tor (Njia ya Vitunguu), mtandao unaotumiwa kwa mawasiliano yasiyojulikana, ambayo itatuwezesha kuficha maingiliano yetu na mtandao wa Bitcoin. Kwa utangulizi wa zana za ulinzi wa faragha mtandaoni, ikiwa ni pamoja na Tor, rejelea makala yetu kuhusu mada hii.


Ili kusakinisha Tor, fungua terminal na uingize sudo apt -y install tor. Mara usakinishaji ukamilika, huduma kwa kawaida itazinduliwa kiotomatiki chinichini. Angalia ikiwa inaendesha kwa usahihi na amri sudo systemctl status tor. Jibu linapaswa kuonyesha Imetumika: hai (imetoka). Bonyeza Ctrl+C ili kuondoka kwenye chaguo hili la kukokotoa.


**Kidokezo:** kwa hali yoyote, unaweza kutumia amri zifuatazo kwenye terminal kuanza, kusimamisha, au kuanzisha upya Tor:

```
sudo systemctl start tor
sudo systemctl stop tor
sudo systemctl restart tor
```


Ifuatayo, wacha tuzindue Bitcoin Core graphical Interface kwa amri Bitcoin-qt. Kisha, washa kipengele cha kiotomatiki cha programu ili kuelekeza miunganisho yetu kupitia seva mbadala ya Tor: Mipangilio > Mtandao, na kutoka hapo tunaweza kuangalia Unganisha kupitia seva mbadala ya SOCKS5 (proksi chaguomsingi) na pia Tumia seva mbadala ya SOCKS5 kufikia wenzako kupitia huduma za Tor vitunguu.


![option](assets/3.webp)


Bitcoin Core hutambua kiotomatiki ikiwa Tor imesakinishwa na, ikiwa ni hivyo, kwa chaguo-msingi itaunda miunganisho ya nje kwa nodi nyingine pia kwa kutumia Tor, pamoja na miunganisho ya nodi kwa kutumia mitandao ya IPv4/IPv6 (clearnet).


**Kumbuka💡:** ili kubadilisha lugha ya kuonyesha hadi Kifaransa, nenda kwenye kichupo cha Onyesho katika Mipangilio.


## Usanidi wa Kina wa Tor (si lazima)


Inawezekana kusanidi Bitcoin Core ili kutumia mtandao wa Tor pekee ili kuungana na programu zingine, hivyo basi kuboresha kutokujulikana kwetu kupitia nodi yetu. Kwa kuwa hakuna utendakazi uliojengewa ndani kwa hili katika mchoro wa Interface, tutahitaji kuunda faili ya usanidi. Nenda kwa Mipangilio, kisha Chaguzi.


![option 2](assets/4.webp)


Hapa, bofya Fungua faili ya usanidi. Ukiwa kwenye faili ya maandishi ya Bitcoin.conf, ongeza tu mstari onlynet=onion na uhifadhi faili. Unahitaji kuwasha upya Bitcoin Core ili amri hii ianze kutumika.

Kisha tutasanidi huduma ya Tor ili Bitcoin Core iweze kupokea miunganisho inayoingia kupitia proksi, na kuruhusu nodi nyingine kwenye mtandao kutumia nodi yetu kupakua data ya Blockchain bila kuathiri usalama wa mashine yetu.


Katika terminal, ingiza sudo nano /etc/tor/torrc kufikia faili ya usanidi wa huduma ya Tor. Katika faili hii, tafuta laini #ControlPort 9051 na uondoe # ili kuiwezesha. Sasa ongeza mistari miwili mipya kwenye faili: HiddenServiceDir /var/lib/tor/Bitcoin-service/ na HiddenServicePort 8333 127.0.0.1:8334. Ili kuondoka kwenye faili huku ukiihifadhi, bonyeza Ctrl+X > Y > Enter. Rudi kwenye terminal, anzisha tena Tor kwa kuingiza amri sudo systemctl restart tor.


Kwa usanidi huu, Bitcoin Core itaweza kuanzisha miunganisho inayoingia na kutoka na nodi zingine kwenye mtandao kupitia mtandao wa Tor (Kitunguu). Ili kuthibitisha hili, bofya kichupo cha Dirisha, kisha Rika.


![Nodes Window](assets/5.webp)


## Rasilimali za Ziada


Hatimaye, kutumia mtandao wa Tor pekee (onlynet=onion) kunaweza kukufanya uwe katika hatari ya kushambuliwa na Sybil. Ndiyo maana wengine wanapendekeza kudumisha usanidi wa mitandao mingi ili kupunguza aina hii ya hatari. Zaidi ya hayo, miunganisho yote ya IPv4/IPv6 itapitishwa kupitia seva mbadala ya Tor mara tu itakaposanidiwa, kama ilivyoonyeshwa hapo awali.


Vinginevyo, ili kubaki pekee kwenye mtandao wa Tor na kupunguza hatari ya shambulio la Sybil, unaweza kuongeza Address ya nodi nyingine inayoaminika kwenye faili yako ya Bitcoin.conf kwa kuongeza laini ya addnode=trusted_address.onion. Unaweza kuongeza laini hii mara kadhaa ikiwa unataka kuunganisha kwenye nodi nyingi zinazoaminika.


Ili kutazama kumbukumbu za nodi yako ya Bitcoin inayohusiana haswa na mwingiliano wake na Tor, ongeza debug=tor kwenye faili yako ya Bitcoin.conf. Sasa utakuwa na maelezo muhimu ya Tor kwenye logi yako ya utatuzi, ambayo unaweza kutazama kwenye dirisha la Habari kwa kitufe cha Faili ya Kutatua. Inawezekana pia kutazama kumbukumbu hizi moja kwa moja kwenye terminal kwa amri bitcoind -debug=tor.


**Kidokezo💡:** hapa kuna viungo vya kuvutia:


- Ukurasa wa Wiki unaoelezea Tor na uhusiano wake na Bitcoin
- Jenereta ya faili ya usanidi wa Bitcoin na Jameson Lopp
- Mwongozo wa usanidi wa Tor na Jon Atack


Kama kawaida, ikiwa una maswali yoyote, jisikie huru kuyashiriki na jumuiya ya Agora256. Tunajifunza pamoja kuwa bora kesho kuliko tulivyo leo!