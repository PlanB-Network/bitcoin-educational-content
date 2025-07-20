---
name: Kadi ya Cold

description: Kuunda, kuhifadhi nakala na kutumia ufunguo wa faragha wa Bitcoin na kifaa cha Coldcard na Bitcoin Core
---

![cover](assets/cover.webp)


_Kuunda, kuhifadhi nakala, na kutumia ufunguo wa faragha wa Bitcoin wenye kifaa cha Coldcard na Bitcoin Core_


## Mwongozo kamili wa kutengeneza ufunguo wa kibinafsi kwa kutumia Coldcard na kuitumia kupitia Interface ya nodi yako ya Bitcoin Core!


Msingi wa matumizi ya mtandao wa Bitcoin ni dhana ya kriptografia isiyolinganishwa: jozi ya funguo - moja ya kibinafsi na ya umma - ambayo husimba na kusimbua data, dhana inayohakikisha usiri wa mawasiliano.


Kwa upande wa Bitcoin, kwa kuzalisha jozi hizo za funguo za kibinafsi na za umma, tunaweza kuhifadhi bitcoins (UTXO au Pato la Muamala Usiotumiwa) na kusaini miamala ili kuzitumia.


Leo, kuna zana nyingi zinazopatikana ili kuwezesha uundaji wa ufunguo wa kibinafsi bila mpangilio na uhifadhi wake katika muundo wa maandishi kwa kutumia BIP 39 - kiwango ambacho huamua jinsi pochi huhusisha maneno ya Mnemonic (maneno ya seed) na funguo za usimbaji fiche. Mara nyingi zaidi kuliko sivyo, maneno ya Mnemonic yana maneno 12 au 24, ambayo lazima yameungwa mkono kwa usalama ili kuweza kurejesha Wallet na bitcoins zake.


Katika makala hii, tutajifunza jinsi ya generate ufunguo wa kibinafsi kwa kutumia Coldcard Mk4, mojawapo ya vifaa vinavyotumiwa sana na salama katika ulimwengu wa Bitcoin, kwa kutumia njia ya kete ili kuhakikisha entropy ya kiwango cha juu, na jinsi ya kuitumia na Bitcoin Core kwa namna ya hewa!


**Kumbuka:🧰** Pata zana zifuatazo ili kutumia mwongozo:



- Kifaa cha Coldcard (Mk3 au Mk4)
- Kadi ya MicroSD (4GB inatosha)
- Kebo ya USB yenye nguvu pekee (mini-usb kwa Mk3, usb-c kwa Mk4)
- Kete moja au zaidi ya ubora


## Inazalisha maneno mapya ya Mnemonic kwa kutumia Coldcard


Tutaanza mchakato wa kuunda ufunguo wa faragha kuanzia mwanzo, kwa kuchukulia Coldcard ambayo imefunguliwa upya ambayo PIN tayari imesanidiwa (fuata hatua zilizo kwenye Coldcard wakati wa kuanzisha kifaa).


**Kumbuka🚨:** Ili kuweka upya ufunguo wa faragha wa Coldcard ambayo tayari imesanidiwa, fuata hatua hizi:

_Advanced/Zana > Eneo la Hatari > Kazi za seed > Destroy seed > ✓_


**Tahadhari:** Coldcard yako itasahau ufunguo wa faragha kufuatia hatua hizi. Hakikisha umeweka nakala rudufu ya maneno yako ya Mnemonic ipasavyo ikiwa ungependa kuweza kuirejesha baadaye.


## Hatua za kufuata:


Unganisha kwa Coldcard kwa PIN > Maneno Mapya ya seed > Dice Dice Roll 24 za Word


Tekeleza kete 100, ukiandika matokeo yaliyopatikana kutoka 1 hadi 6 kwenye Coldcard baada ya kila roll. Kwa kufanya mazoezi ya njia hii, unaunda baiti 256 za entropy, na hivyo kupendelea uundaji wa ufunguo wa kibinafsi wa nasibu. Coinkite pia hutoa hati muhimu kwa uthibitishaji huru wa mfumo wao wa kizazi cha entropy.


![Visual Cold Card Screenshot](assets/guide-agora/1.webp)


Mara tu kete 100 zimekamilika, bonyeza ✓ kisha uandike maneno 24 yaliyopatikana kwa mpangilio. Thibitisha mara mbili na ubonyeze ✓. Hatimaye, kilichosalia ni kukamilisha jaribio la uthibitishaji wa maneno 24 kwenye Coldcard, na voila, ufunguo wako mpya wa faragha umeundwa!


Ifuatayo, chagua ikiwa utawasha au la kuwezesha NFC (Mk4) na vitendaji vya USB kwa kufuata hatua zinazoonyeshwa. Mara moja kwenye menyu kuu, sasa ni wakati wa kusasisha firmware ya kifaa. Nenda kwa Advanced/Tools > Boresha Firmware > Onyesha Toleo, na uangalie tovuti rasmi ili kuthibitisha na kupakua toleo la hivi karibuni linalopatikana. Inashauriwa kusasisha Coldcard ili kufaidika na usalama wa juu zaidi.


Kabla ya kuendelea, inashauriwa kutambua Alama ya Kidole ya Ufunguo Mkuu (XFP) inayohusishwa na ufunguo wa faragha. Data hii inaruhusu uthibitisho wa haraka ikiwa uko katika Wallet sahihi katika kesi ya kurejesha, kwa mfano. Nenda kwa Kina/Zana > Tazama Kitambulisho > Alama ya Ufunguo Mkuu wa Kidole (XFP) na uandike mfululizo wa herufi nane za alphanumeric zilizopatikana. XFP inaweza kuzingatiwa mahali sawa na kifungu cha Mnemonic, sio data nyeti.


**Kumbuka:💡** inashauriwa kujaribu nakala ya maneno ya Mnemonic katika programu tofauti. Ili kufanya hivyo kwa usalama, wasiliana na makala yetu Thibitisha hifadhi rudufu ya Bitcoin Wallet yenye Mikia kwa chini ya dakika 5.


## Bonasi ya Usalama: "Neno la Siri" (hiari)


passphrase (maneno ya siri) ni kipengele kizuri cha kuongeza kwenye usanidi wa Wallet ili kuongeza Layer ya usalama ili kulinda bitcoins zako. passphrase hufanya kama aina ya neno la 25 kwa kifungu cha Mnemonic. Mara baada ya kuongezwa, Wallet mpya kabisa huundwa pamoja na ufunguo wa kibinafsi na maneno yake yanayohusiana ya Mnemonic. Sio lazima kuandika kifungu kipya cha Mnemonic, kwani hii Wallet inaweza kupatikana kwa kuchanganya kifungu cha mwanzo cha Mnemonic na passphrase iliyochaguliwa.


Lengo ni kutambua passphrase kando na maneno ya Mnemonic kwa sababu mshambuliaji ambaye anaweza kufikia vitu vyote viwili atapata pesa. Kwa upande mwingine, mshambuliaji ambaye ana ufikiaji wa moja tu ya vitu hivi hatakuwa na ufikiaji wa pesa, na ni faida hii maalum ambayo huongeza kiwango cha usalama cha usanidi wa Wallet.


![Adding a passphrase leads to a completely different wallet](assets/guide-agora/2.webp)


## Hatua za kuongeza passphrase kwa Coldcard:


passphrase > Ongeza Maneno (inapendekezwa) > Tekeleza. Kifaa kitaonyesha XFP ya Wallet iliyozalishwa hivi karibuni na passphrase, ambayo inapaswa kuzingatiwa chini na passphrase kwa sababu sawa zilizotajwa hapo awali.


**Kidokezo💡** Hapa kuna nyenzo za ziada zinazohusiana na passphrase:



- [Hapa](https://blog.trezor.io/is-your-passphrase-strong-enough-d687f44c63af) kuna ya kwanza ya _Trezor_;
- [Hapa](https://blog.coinkite.com/everything-you-need-to-know-about-passphrases/) unaweza kupata ya pili kwa _Coinkite_;
- Na [hapa](https://armantheparman.com/passphrase/) utapata ya mwisho na _armantheparman_.


## Inasafirisha Wallet hadi Bitcoin Core


Wallet sasa iko tayari kutumwa kwa programu ili kuingiliana na mtandao wa Bitcoin. Katika mwongozo huu, tutatumia Bitcoin Core (v24.1).


Rejelea miongozo yetu ya usakinishaji na usanidi wa Bitcoin Core:



- Kuendesha nodi yako mwenyewe na Bitcoin Core:** https://agora256.com/faire-tourner-son-propre-noeud-avec-Bitcoin-core/
- Inasanidi Tor kwa nodi ya Msingi ya Bitcoin:** https://agora256.com/configuration-tor-Bitcoin-core/


Kwanza, weka kadi ndogo ya SD kwenye Coldcard, kisha hamisha Wallet ya Bitcoin Core kwa kufuata hatua hizi: Advanced/Tools > Hamisha Wallet > Bitcoin Core. Faili mbili zitaandikwa kwa kadi ndogo ya SD: Bitcoin-core.sig & Bitcoin-core.txt. Ingiza kadi ndogo ya SD kwenye kompyuta ambapo Bitcoin Core imesakinishwa, na ufungue faili ya .txt. Utaona mstari "Kwa Wallet na alama za vidole kuu." Thibitisha kuwa XFP yenye herufi nane inalingana na uliyobainisha wakati wa kuunda ufunguo wako wa faragha.'

Kabla ya kufuata maagizo katika faili, hebu tuanze kwa kuandaa Wallet katika Bitcoin Core Interface kwa kufuata hatua hizi: nenda kwenye kichupo cha Faili> Unda Wallet. Chagua jina la Wallet yako (neno linaloweza kubadilishwa na "porte-monnaie" katika Core) na uangalie chaguo Zima funguo za faragha, Unda Wallet tupu, na Wallet maelezo kama inavyoonyeshwa kwenye picha hapa chini. Kisha, bonyeza kitufe cha Unda.


![create a wallet](assets/guide-agora/3.webp)


Mara tu Wallet inapoundwa katika Bitcoin Core, nenda kwenye kichupo cha Dirisha > Console na uhakikishe kuwa Wallet iliyochaguliwa juu ya ukurasa inaonyesha jina la ulilounda.


Sasa, katika faili ya .txt iliyozalishwa na Coldcard mapema, nakili laini inayoanza na vielezi vya kuagiza, kisha ubandike kwenye kiweko cha Bitcoin Core. Jibu linalojumuisha mstari "mafanikio": true inapaswa kurejeshwa.


![nodes window](assets/guide-agora/4.webp)


Iwapo jibu lina "message": "Vifafanuzi masafa havipaswi kuwa na lebo", futa ingizo "label": "Coldcard xxxx0000" katika mstari ulionakiliwa kutoka kwenye faili ya .txt, kisha ubandike laini kamili kwenye kiweko cha Bitcoin Core.


Ikihitajika, unaweza kupata usaidizi [hapa](https://github.com/Coldcard/firmware/blob/master/docs/Bitcoin-core-usage.md) kwenye Coldcard Github.


## Uthibitishaji wa uingizaji wa Wallet katika Bitcoin Core


Ili kuhakikisha kuwa operesheni ilifanikiwa, ni muhimu kuthibitisha kwamba Wallet inayotaka imeingizwa kwenye Bitcoin Core. Njia rahisi ya kuthibitisha hili ni kuthibitisha kwamba anwani zinazozalishwa katika Coldcard zinalingana na anwani zinazozalishwa katika Bitcoin Core.


Msingi wa Bitcoin: Pokea > Unda toleo jipya la Address

Coldcard: Address Explorer > Chagua Address ukianza na bc1q. Coldcard Address 'bc1q' inapaswa kuendana na Address inayoonyeshwa katika Bitcoin Core.

Kupokea na kutuma miamala katika hali ya 'hewa-pengo'


Kupokea muamala ni rahisi sana; bonyeza tu Pokea, weka lebo ya muamala (si lazima lakini inapendekezwa), na Unda Address mpya inayopokea. Kisha, kilichobaki ni kushiriki Address na mtumaji.


Sasa, kipengele muhimu cha usanidi huu wa Coldcard + Bitcoin Core ni kutuma miamala bila Coldcard na ufunguo wake wa faragha kuunganishwa kwenye mtandao, njia inayoitwa air-gapped ambayo inatumia kipengele cha TBSP (PSBT - Bitcoin Transactions) kilichotiwa Saini kwa Sehemu) cha Bitcoin.

Kimsingi, tunatumia Bitcoin Core Interface kuunda muamala, ambao tutasafirisha kupitia kadi ndogo ya SD hadi kwa Coldcard ili kusainiwa, na kisha kurudisha faili ya muamala iliyotiwa saini kwa Bitcoin Core na kutangaza muamala kwa mtandao. Tunapaswa kufanya hivyo kwa sababu Wallet iliyoagizwa kwenye Bitcoin Core haina ufunguo wa faragha, ufunguo wa umma tu (unaotuwezesha generate anwani zetu za kupokea), hivyo haiwezekani kwetu kusaini shughuli moja kwa moja kwenye programu ili kutumia bitcoins zetu.


Kabla ya kuendelea, hakikisha kuwa chaguo zifuatazo zimewashwa katika Mipangilio > Wallet:



- Washa vipengele vya udhibiti wa sarafu
- Tumia sarafu ambazo hazijathibitishwa (Si lazima)
- Washa ukaguzi wa TBPS


![option ](assets/guide-agora/5.webp)


### Hatua za kutuma katika hali iliyo na nafasi ya hewa:


Tuma > Ingizo > chagua UTXO unayotaka, kisha uweke Address ya mpokeaji katika Pay to. Ada ya muamala: Chagua... > Maalum > Weka ada ya muamala (Bitcoin Core hukokotoa katika Sats/kilobaiti badala ya sat/byte kama masuluhisho mengi mbadala ya Wallet. Kwa hivyo 4000 Sats/kilobyte = 4 Sats/baiti). Unda muamala ambao haujatiwa saini > hifadhi faili kwenye kadi yako ndogo ya SD na uiweke kwenye Coldcard.


Katika Coldcard, bonyeza Tayari kutia sahihi, thibitisha maelezo ya muamala, kisha ubonyeze ✓ na uingize kadi ndogo ya SD kwenye kompyuta mara faili zilizotiwa saini zinapotolewa.


Rudi kwenye Bitcoin Core, nenda kwenye kichupo cha Faili > Pakia TBSP kutoka kwenye faili, na uweke faili ya muamala iliyotiwa saini .PSBT. Kisanduku cha Uendeshaji cha PSBT kitaonekana kwenye skrini, na kuthibitisha kwamba shughuli hiyo imetiwa saini kikamilifu na iko tayari kutangazwa. Kilichosalia ni kubonyeza muamala wa Matangazo.


![PSBT operations](assets/guide-agora/6.webp)


### Hitimisho


Mchanganyiko wa kifaa cha Coldcard na Bitcoin Core, ambayo unaendesha nodi yako mwenyewe, ni nguvu. Ongeza kwa hilo ufunguo wa faragha unaotengenezwa kwa kete 100 na maneno ya siri, na usanidi wako wa Wallet unakuwa ngome ya kisasa na imara.


Jisikie huru kuwasiliana nasi ili kushiriki maoni na maswali yako! Lengo letu ni kubadilishana maarifa na kuongeza uelewa wetu siku baada ya siku.