---
name: Bitcoin Core (Linux)
description: Kuendesha nodi yako mwenyewe na Bitcoin core kwenye Linux
---

![cover](assets/cover.webp)


## Kuendesha nodi yako mwenyewe na Bitcoin core


Utangulizi wa Bitcoin na dhana ya nodi, inayokamilishwa na mwongozo wa kina wa usakinishaji kwenye Linux.


Moja ya mambo ya kusisimua zaidi ya Bitcoin ni uwezo wa kuendesha programu mwenyewe, na hivyo kushiriki katika ngazi ya punjepunje katika mtandao na uthibitishaji wa shughuli za umma Ledger.


Bitcoin, kama mradi wa chanzo huria, imekuwa ikipatikana bila malipo na kusambazwa hadharani tangu 2009. Takriban miaka 17 baada ya kuanzishwa, Bitcoin sasa ni mtandao thabiti na usiozuilika wa fedha wa kidijitali, unaonufaika kutokana na athari kubwa ya mtandao wa kikaboni. Kwa juhudi na maono yao, Satoshi Nakamoto inastahili shukrani zetu. Kwa njia, tunakaribisha karatasi nyeupe ya Bitcoin hapa kwenye Agora 256 (kumbuka: pia kwenye chuo kikuu).


### Kuwa benki yako mwenyewe


Kuendesha nodi yako mwenyewe imekuwa muhimu kwa wafuasi wa maadili ya Bitcoin. Bila kuomba ruhusa ya mtu yeyote, inawezekana kupakua Blockchain tangu mwanzo na hivyo kuthibitisha shughuli zote kutoka A hadi Z kulingana na itifaki ya Bitcoin.


Programu pia inajumuisha Wallet yake mwenyewe. Kwa hivyo, tuna udhibiti wa miamala tunayotuma kwa mtandao mwingine wowote, bila mpatanishi au mtu wa tatu. Wewe ni benki yako mwenyewe.


Kwa hivyo makala haya mengine ni mwongozo wa kusakinisha Bitcoin core - toleo la programu inayotumika zaidi ya Bitcoin - haswa kwenye usambazaji wa Linux unaotangamana na Debian kama vile Ubuntu na Pop!OS. Fuata mwongozo huu ili kuchukua hatua moja karibu na uhuru wako binafsi.


## Mwongozo wa Usakinishaji wa Bitcoin core kwa Debian/Ubuntu


**Mahitaji**


- Kiwango cha chini cha 6GB cha hifadhi ya data (nodi ya pruned) — 1TB ya hifadhi ya data (Full node)
- Tarajia *Upakuaji wa Kizuizi cha Awali* (IBD) kuchukua angalau saa 24. Operesheni hii ni ya lazima hata kwa node ya pruned.
- Ruhusu ~600GB ya kipimo data kwa IBD, hata kwa nodi ya pruned.


**Kumbuka:💡** amri zifuatazo zimefafanuliwa mapema kwa toleo la 24.1 la Bitcoin core.


### Inapakua na Kuthibitisha Faili



- [Pakua](https://bitcoincore.org/en/download/) `Bitcoin-24.1-x86_64-linux-gnu.tar.gz`, pamoja na faili za `SHA256SUMS` na `SHA256SUMS.asc` (bila shaka unahitaji kupakua toleo jipya zaidi la programu).



- Fungua terminal kwenye saraka ambapo faili zilizopakuliwa ziko. Mfano: `cd ~/Vipakuliwa/`.



- Thibitisha kuwa hundi ya faili ya toleo imeorodheshwa katika faili ya hundi kwa kutumia amri `sha256sum --ignore-missing --check SHA256SUMS`.



- Matokeo ya amri hii inapaswa kujumuisha jina la faili ya toleo iliyopakuliwa ikifuatiwa na `Sawa`. Mfano: `Bitcoin-24.0.1-x86_64-linux-gnu.tar.gz: SAWA`.



- Sakinisha git kwa kutumia amri `sudo apt install git`. Kisha, linganisha hazina iliyo na funguo za PGP za watia saini wa Bitcoin core kwa kutumia amri `git clone https://github.com/Bitcoin-core/guix.sigs`.



- Ingiza funguo za PGP za watia saini wote kwa kutumia amri `gpg --import guix.sigs/builder-keys/*`



- Thibitisha kuwa faili ya hundi imetiwa saini na vitufe vya PGP vya watia saini kwa kutumia amri `gpg --verify SHA256SUMS.asc`.



Kila sahihi sahihi itaonyesha mstari unaoanza na: `gpg: Sahihi nzuri` na mstari mwingine unaoishia na: `Alama ya vidole ya ufunguo wa msingi: 133E AC17 9436 F14A 5CF1 B794 860F EB80 4E66 9320` (mfano wa alama ya vidole ya Pieter Wuille ya PGP).


**Kumbuka💡:** si lazima kwa vitufe vyote vya kutia sahihi kurudisha "SAWA". Kwa kweli, moja tu inaweza kuwa muhimu. Ni juu ya mtumiaji kuamua kiwango chao cha uthibitishaji kwa uthibitishaji wa PGP.


Unaweza kupuuza maonyo:



- `Ufunguo huu haujathibitishwa kwa saini inayoaminika!`



- `Hakuna dalili kwamba saini ni ya mmiliki.`


### Ufungaji wa Bitcoin core ya picha ya Interface



- Katika terminal, bado katika saraka ambapo faili ya toleo la Bitcoin core iko, tumia amri `tar xzf Bitcoin-24.1-x86_64-linux-gnu.tar.gz` ili kutoa faili zilizo kwenye kumbukumbu.



- Sakinisha faili zilizotolewa hapo awali kwa kutumia amri `sudo install -m 0755 -o root -g root -t /usr/local/bin Bitcoin-24.1/bin/*`



- Sakinisha utegemezi unaohitajika kwa kutumia amri `sudo apt-get install libqt5gui5 libqt5core5a libqt5dbus5 qttools5-dev qttools5-dev-tools qtwayland5 libqrencode-dev`



- Anza _bitcoin-qt_ (Bitcoin core mchoro Interface) kwa kutumia amri `Bitcoin-qt`.



- Ili kuchagua nodi ya pruned, angalia _Limit Blockchain storage_ na usanidi kikomo cha data cha kuhifadhiwa:


![welcome](assets/fr/02.webp)


### Hitimisho la Sehemu ya 1: Mwongozo wa Ufungaji


Mara baada ya Bitcoin core kusakinishwa, inashauriwa kuifanya iendelee iwezekanavyo ili kuchangia mtandao wa Bitcoin kwa kuthibitisha miamala na kusambaza vizuizi vipya kwa wenzao wengine.


Hata hivyo, kuendesha na kusawazisha nodi yako mara kwa mara, hata kuthibitisha tu shughuli zilizopokelewa na kutumwa, bado ni mazoezi mazuri.


![Creation wallet](assets/fr/03.webp)


## Inasanidi Tor kwa Njia ya Bitcoin core


**Kumbuka💡:** mwongozo huu umeundwa kwa ajili ya Bitcoin core 24.0.1 kwenye usambazaji wa Linux unaooana na Ubuntu/Debian.


### Kufunga na kusanidi Tor kwa Bitcoin core


Kwanza, tunahitaji kusakinisha huduma ya Tor (Njia ya Vitunguu), mtandao unaotumiwa kwa mawasiliano yasiyojulikana, ambayo itatuwezesha kuficha maingiliano yetu na mtandao wa Bitcoin. Kwa utangulizi wa zana za ulinzi wa faragha mtandaoni, ikiwa ni pamoja na Tor, rejelea makala yetu kuhusu mada hii.


Ili kusakinisha Tor, fungua terminal na uweke `sudo apt -y install tor`. Mara usakinishaji ukamilika, huduma kwa kawaida itazinduliwa kiotomatiki chinichini. Angalia kuwa inaendeshwa kwa usahihi na amri `sudo systemctl status tor`. Jibu linapaswa kuonyesha `Inayotumika: hai (imetoka)`. Bonyeza `Ctrl+C` ili kuondoka kwenye chaguo hili la kukokotoa.


**Kidokezo:** kwa hali yoyote, unaweza kutumia amri zifuatazo kwenye terminal kuanza, kusimamisha, au kuanzisha upya Tor:


```shell
sudo systemctl start tor
sudo systemctl stop tor
sudo systemctl restart tor
```


Ifuatayo, hebu tuzindue Bitcoin core mchoro Interface kwa amri `Bitcoin-qt`. Kisha, washa kipengele cha kiotomatiki cha programu ili kuelekeza miunganisho yetu kupitia seva mbadala ya Tor: _Mipangilio > Network_, na kutoka hapo uangalie _Unganisha kupitia seva mbadala ya SOCKS5 (proksi chaguomsingi)_ na pia _Tumia seva mbadala ya SOCKS5 kufikia wenzako kupitia huduma za Tor onion_.


![option](assets/fr/04.webp)


Bitcoin core hutambua kiotomatiki ikiwa Tor imesakinishwa na, ikiwa ni hivyo, kwa chaguo-msingi itaunda miunganisho ya nje kwa nodi nyingine pia kwa kutumia Tor, pamoja na miunganisho ya nodi kwa kutumia mitandao ya IPv4/IPv6 (clearnet).


**Kumbuka💡:** ili kubadilisha lugha ya kuonyesha hadi Kifaransa, nenda kwenye kichupo cha Onyesho katika Mipangilio.


### Usanidi wa Kina wa Tor (si lazima)


Inawezekana kusanidi Bitcoin core ili tu kutumia mtandao wa Tor kuungana na wenzao, hivyo basi kuboresha kutokujulikana kwetu kupitia nodi yetu. Kwa kuwa hakuna utendakazi uliojengewa ndani kwa hili katika mchoro wa Interface, tutahitaji kuunda faili ya usanidi. Nenda kwa Mipangilio, kisha Chaguzi.


![option 2](assets/fr/05.webp)


Hapa, bofya _Fungua faili ya usanidi_. Ukiwa kwenye faili ya maandishi ya `Bitcoin.conf`, ongeza tu mstari `onlynet=onion` na uhifadhi faili. Unahitaji kuanzisha upya Bitcoin core ili amri hii ianze kutumika.


Kisha tutasanidi huduma ya Tor ili Bitcoin core iweze kupokea miunganisho inayoingia kupitia proksi, na kuruhusu nodi nyingine kwenye mtandao kutumia nodi yetu kupakua data ya Blockchain bila kuathiri usalama wa mashine yetu.


Kwenye terminal, ingiza `sudo nano /etc/tor/torrc` ili kufikia faili ya usanidi wa huduma ya Tor. Katika faili hii, tafuta mstari `#ControlPort 9051` na uondoe `#` ili kuiwezesha. Sasa ongeza mistari miwili mpya kwenye faili:


```
HiddenServiceDir /var/lib/tor/bitcoin-service/
HiddenServicePort 8333 127.0.0.1:8334
```


Ili kuondoka kwenye faili huku ukiihifadhi, bonyeza `Ctrl+X > Y > Enter`. Rudi kwenye terminal, anzisha tena Tor kwa kuingiza amri `sudo systemctl restart tor`.


Kwa usanidi huu, Bitcoin core itaweza kuanzisha miunganisho inayoingia na inayotoka na nodi zingine kwenye mtandao kupitia mtandao wa Tor (Kitunguu). Ili kuthibitisha hili, bofya kichupo cha _Window_, kisha _Peers_.


![Nodes Window](assets/fr/06.webp)


### Rasilimali za Ziada


Hatimaye, kutumia mtandao wa Tor pekee (`onlynet=onion`) kunaweza kukufanya uwe hatarini kwa Sybil Attack. Ndiyo maana wengine wanapendekeza kudumisha usanidi wa mitandao mingi ili kupunguza aina hii ya hatari. Zaidi ya hayo, miunganisho yote ya IPv4/IPv6 itapitishwa kupitia seva mbadala ya Tor mara tu itakaposanidiwa, kama ilivyoonyeshwa hapo awali.


Vinginevyo, ili kubaki pekee kwenye mtandao wa Tor na kupunguza hatari ya Sybil Attack, unaweza kuongeza Address ya nodi nyingine inayoaminika kwenye faili yako ya `Bitcoin.conf` kwa kuongeza laini `addnode=trusted_address.onion`. Unaweza kuongeza laini hii mara kadhaa ikiwa unataka kuunganisha kwa nodi nyingi zinazoaminika.


Ili kutazama kumbukumbu za nodi yako ya Bitcoin inayohusiana haswa na mwingiliano wake na Tor, ongeza `debug=tor` kwenye faili yako ya `Bitcoin.conf`. Sasa utakuwa na taarifa muhimu ya Tor kwenye logi yako ya utatuzi, ambayo unaweza kutazama kwenye dirisha la _Information_ kwa kitufe cha _Debug File_. Inawezekana pia kutazama kumbukumbu hizi moja kwa moja kwenye terminal kwa amri `bitcoind -debug=tor`.


**Kidokezo💡:** hapa kuna viungo vya kuvutia:


- [Ukurasa wa Wiki unaoeleza Tor na uhusiano wake na Bitcoin](https://en.Bitcoin.it/wiki/Tor)
- [Jenereta ya faili ya usanidi ya Bitcoin core na Jameson Lopp](https://jlopp.github.io/Bitcoin-core-config-generator/)
- [Mwongozo wa usanidi wa Jon Atack](https://github.com/Bitcoin/Bitcoin/blob/master/doc/tor.md)


Kama kawaida, ikiwa una maswali yoyote, jisikie huru kuyashiriki na jumuiya ya Agora256. Tunajifunza pamoja kuwa bora kesho kuliko tulivyo leo!