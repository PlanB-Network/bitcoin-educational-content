---
name: Kuongeza Zana za Kielimu
description: Jinsi ya kuongeza nyenzo mpya za kielimu kwenye Plan ₿ Academy?
---
![event](assets/cover.webp)


Dhamira ya PlanB ni kutoa rasilimali zinazoongoza za kielimu kuhusu Bitcoin, katika lugha nyingi iwezekanavyo. Maudhui yote yaliyochapishwa kwenye tovuti ni chanzo huria na yanahifadhiwa kwenye GitHub, ambayo inaruhusu mtu yeyote kushiriki katika kuimarisha jukwaa.


Zaidi ya mafunzo na mafunzo, Plan ₿ Academy pia inatoa maktaba kubwa ya maudhui mbalimbali ya kielimu kwenye Bitcoin, yanayopatikana kwa kila mtu, [katika sehemu ya "BET" (_Bitcoin Educational Toolkit_)](https://planb.academy/resources/bet). Hifadhidata hii inajumuisha mabango ya kielimu, meme, mabango ya propaganda za ucheshi, michoro ya kiufundi, nembo, na zana zingine kwa watumiaji. Lengo la mpango huu ni kuwasaidia watu binafsi na jamii zinazofundisha Bitcoin kote ulimwenguni kwa kuwapa rasilimali zinazohitajika za kuona.


Je, unataka kushiriki katika kuboresha hifadhidata hii, lakini hujui jinsi ya kufanya hivyo? Mafunzo haya ni kwa ajili yako!


*Ni muhimu kwamba maudhui yote yaliyojumuishwa kwenye tovuti hayana haki au yanaheshimu leseni ya faili chanzo. Pia, picha zote zilizochapishwa kwenye Plan ₿ Academy zinapatikana chini ya leseni ya [CC-BY-SA](https://creativecommons.org/licenses/by-sa/4.0/).*

![event](assets/01.webp)


- Kwanza, unahitaji kuwa na akaunti kwenye GitHub. Kama hujui jinsi ya kuunda akaunti, tumeandaa mafunzo ya kina ili kukuongoza.


https://planb.academy/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c



- Nenda kwenye [hifadhi ya GitHub ya PlanB iliyojitolea kwa data](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/bet) katika sehemu ya `resources/bet/`:

![event](assets/02.webp)


- Bonyeza juu kulia kwenye kitufe cha `Ongeza faili`, kisha kwenye `Unda faili mpya`:

![event](assets/03.webp)


- Ikiwa hujawahi kuchangia kwenye maudhui ya Plan ₿ Academy hapo awali, utahitaji kuunda fork yako ya hazina asili. Kuweka hazina ya Fork kunamaanisha kuunda nakala ya hazina hiyo kwenye akaunti yako ya GitHub, ambayo hukuruhusu kufanya kazi kwenye mradi bila kuathiri hazina asili. Bonyeza kitufe cha `Fork hazina hii`:

![event](assets/04.webp)


- Kisha utafika kwenye ukurasa wa uhariri wa GitHub:

![event](assets/05.webp)


- Unda folda ya maudhui yako. Ili kufanya hivi, katika kisanduku cha `Taja faili yako...`, andika jina la maudhui yako kwa herufi ndogo ukitumia vibonyezo badala ya nafasi. Katika mfano wangu, tuseme nataka kuongeza taswira ya PDF ya orodha ya BIP39 yenye maneno 2048. Kwa hivyo, nitaita folda yangu `bip39-wordlist`: ![event](assets/06.webp)
- Ili kuthibitisha uundaji wa folda, ongeza tu mkato baada ya jina katika kisanduku hicho hicho, kwa mfano: `bip39-wordlist/`. Kuongeza mkato huunda folda kiotomatiki badala ya faili:

![event](assets/07.webp)


- Katika folda hii, utaunda faili ya kwanza ya YAML inayoitwa `bet.yml`:

![event](assets/08.webp)


- Jaza faili hii na taarifa zinazohusiana na maudhui yako kwa kutumia kiolezo hiki:


```yaml
project:
type:
links:
download:
view:
- en:
tags:
-
-
contributors:
-
```


Hapa kuna maelezo ya kujaza kwa kila sehemu:



- `mradi`**: Onyesha kitambulisho cha shirika lako kwenye Plan ₿ Academy. Ikiwa bado huna kitambulisho cha "mradi" kwa kampuni yako, unaweza kuunda kimoja kwa kufuata mafunzo haya.


https://planb.academy/tutorials/contribution/resource/add-builder-b5834c46-6dcc-4064-8d68-1ef529991d3d

Kama huna moja, unaweza kutumia tu jina lako, jina lako bandia, au jina la kampuni yako bila kuunda wasifu wa mradi.



- `aina`**: Chagua aina ya maudhui yako kati ya chaguo mbili zifuatazo:
 - `Maudhui ya Kielimu` kwa maudhui ya kielimu.
 - `Maudhui Yanayoonekana` kwa aina nyingine za maudhui mbalimbali.



- `viungo`**: Toa viungo vya maudhui yako. Una chaguo mbili:
 - Ukichagua kuhifadhi maudhui yako moja kwa moja kwenye GitHub ya PlanB, utahitaji kuongeza viungo kwenye faili hii wakati wa hatua zifuatazo.
 - Ikiwa maudhui yako yamehifadhiwa kwingineko, kama vile kwenye tovuti yako binafsi, onyesha viungo vinavyolingana hapa:
     - `pakua`: Kiungo cha kupakua maudhui yako.
     - `view`: Kiungo cha kutazama maudhui yako (kinaweza kuwa sawa na kiungo cha kupakua). Ikiwa maudhui yako yanapatikana katika lugha nyingi, ongeza kiungo kwa kila lugha.



- `lebo`**: Ongeza lebo mbili zinazohusiana na maudhui yako. Mifano:
 - bitcoin
 - teknolojia
 - uchumi
 - elimu
 - meme...



- `wachangiaji`**: Taja kitambulisho chako cha mchangiaji ikiwa unaye.


Kwa mfano, faili yako ya YAML inaweza kuonekana kama hii:


```yaml
project: Plan ₿ Academy
type: Educational Content
links:
download: https://workspace.planb.network/s/fojeJa7ZbftQTwo
view:
```



- Katika mfano wangu, nitaacha viungo vikiwa tupu kwa sasa, kwani nitaongeza PDF yangu moja kwa moja kwenye GitHub:

![event](assets/09.webp)


- Mara tu marekebisho yako kwenye faili hii yatakapokamilika, yahifadhi kwa kubofya kitufe cha `Commit changes...`:

![event](assets/10.webp)


- Ongeza kichwa cha marekebisho yako, pamoja na maelezo mafupi:

![event](assets/11.webp)


- Bonyeza kitufe cha kijani cha `Pendekeza mabadiliko`:

![event](assets/12.webp)


- Kisha utafika kwenye ukurasa unaofupisha mabadiliko yako yote:

![event](assets/13.webp)


- Bonyeza picha ya wasifu wako wa GitHub upande wa juu kulia, kisha kwenye 'Hazina Zako':

![event](assets/14.webp)


- Chagua fork yako ya hazina ya Plan ₿ Academy:

![event](assets/15.webp)


- Unapaswa kuona arifa juu ya dirisha na tawi lako jipya. Huenda inaitwa `kiraka-1`. Bonyeza juu yake:

![event](assets/16.webp)


- Sasa uko kwenye tawi lako linalofanya kazi (**hakikisha uko kwenye tawi lile lile kama marekebisho yako ya awali, hili ni muhimu!**):

![event](assets/17.webp)


- Rudi kwenye folda ya `rasilimali/dau/` na uchague folda ya maudhui yako ambayo umeunda tu katika ahadi iliyopita:

![event](assets/18.webp)


- Kwenye folda ya maudhui yako, bofya kitufe cha `Ongeza faili`, kisha kwenye `Unda faili mpya`:

![event](assets/19.webp)


- Ipe jina folda hii mpya `assets` na uthibitishe uundaji wake kwa kuweka mkato `/` mwishoni:

![event](assets/20.webp)


- Katika folda hii ya `assets`, tengeneza faili inayoitwa `.gitkeep`: ![event](assets/21.webp)
- Bonyeza kitufe cha `Mabadiliko ya Kujitoa...`: ![event](assets/22.webp)
- Acha kichwa cha ahadi kama chaguo-msingi, na uhakikishe kisanduku cha `Kujitoa moja kwa moja kwenye tawi la kiraka-1` kimechaguliwa, kisha bofya `Kujitoa mabadiliko`: ![event](assets/23.webp)
- Rudi kwenye folda ya `assets`: ![event](assets/24.webp)
- Bonyeza kitufe cha `Ongeza faili`, kisha kwenye `Pakia faili`: ![event](assets/25.webp)
- Ukurasa mpya utafunguliwa. Buruta na uangushe kijipicha kinachowakilisha maudhui yako katika eneo hilo. Picha hii itaonyeshwa kwenye tovuti ya Plan ₿ Academy: ![event](assets/26.webp)
- Inaweza kuwa onyesho la kuchungulia, nembo, au aikoni: ![event](assets/27.webp)
- Mara tu picha inapopakiwa, hakikisha kisanduku cha `Kujitoa moja kwa moja kwenye tawi la kiraka-1` kimechaguliwa, kisha bofya `Kujitoa mabadiliko`: ![event](assets/28.webp)
- Kuwa mwangalifu, picha yako lazima ipewe jina la `logo` na lazima iwe katika umbizo la `.webp`. Kwa hivyo jina kamili la faili linapaswa kuwa: `logo.webp`: ![event](assets/29.webp)
- Rudi kwenye folda yako ya `assets` na ubofye faili ya kati `.gitkeep`: ![event](assets/30.webp)
- Ukishaingia kwenye faili, bofya nukta tatu ndogo zilizo juu kulia kisha kwenye `Futa faili`: ![event](assets/31.webp)
- Hakikisha bado uko kwenye tawi lile lile linalofanya kazi, kisha bofya kitufe cha `Commit changes`: ![event](assets/32.webp)
- Ongeza kichwa na maelezo kwenye ahadi yako, kisha bofya `Commit changes`: ![event](assets/33.webp)
- Rudi kwenye folda ya maudhui yako: ![event](assets/34.webp)
- Bonyeza kitufe cha `Ongeza faili`, kisha kwenye `Unda faili mpya`: ![event](assets/35.webp)
- Unda faili mpya ya YAML kwa kuiita kwa kutumia kiashiria cha lugha yako ya asili. Faili hii itatumika kwa maelezo ya maudhui. Kwa mfano, ikiwa ninataka kuandika maelezo yangu kwa Kiingereza, nitaita faili hii jina `en.yml`: ![event](assets/36.webp)
- Jaza faili hii ya YAML kwa kutumia kiolezo hiki:


```yaml
name:
description: |

```



- Kwa kitufe cha `jina`, unaweza kuongeza jina la maudhui yako;
- Kwa ufunguo wa `maelezo`, unahitaji tu kuongeza aya fupi inayoelezea maudhui yako. Maelezo lazima yawe katika lugha sawa na jina la faili. Huna haja ya kutafsiri maelezo haya katika lugha zote zinazoungwa mkono kwenye tovuti, kwani timu za PlanB zitafanya hivyo kwa kutumia mfumo wao.

Kwa mfano, hii ndiyo jinsi faili yako inaweza kuonekana:


```yaml
name: BIP39 WORDLIST
description: |
Complete and numbered list of the 2048 English words from the BIP39 dictionary used to encode mnemonic phrases. The document can be printed on a single page.
```


![event](assets/37.webp)


- Bonyeza kitufe cha 'Mabadiliko ya Kujitolea...':

![event](assets/38.webp)


- Hakikisha kwamba kisanduku cha `Kujitoa moja kwa moja kwenye tawi la kiraka-1` kimechaguliwa, ongeza kichwa, kisha bofya `Kujitoa mabadiliko`:

![event](assets/39.webp)


- Folda yako ya maudhui sasa inapaswa kuonekana kama hii:

![event](assets/40.webp)


---

*Ikiwa hupendi kuongeza maudhui kwenye GitHub na tayari umeandika viungo kwenye faili ya `bet.yml` wakati wa hatua zilizopita, unaweza kuruka sehemu hii na kwenda moja kwa moja kwenye sehemu inayohusu uundaji wa Ombi la Kuvuta.*



- Rudi kwenye folda ya `/assets`:

![event](assets/41.webp)


- Bonyeza kitufe cha `Ongeza faili`, kisha kwenye `Pakia faili`:

![event](assets/42.webp)


- Ukurasa mpya utafunguliwa. Buruta na uangushe kwenye eneo maudhui unayotaka kushiriki:

![event](assets/43.webp)


- Kwa mfano, niliongeza faili ya PDF ya orodha ya BIP39:

![event](assets/44.webp)


- Mara tu maudhui yanapopakiwa, hakikisha kwamba kisanduku cha `Kujitoa moja kwa moja kwenye tawi la kiraka-1` kimechaguliwa, kisha bofya `Kujitoa mabadiliko`:

![event](assets/45.webp)


- Rudi kwenye folda yako ya `/assets` na ubofye faili uliyopakia hivi punde:

![event](assets/46.webp)


- Rejesha URL ya kati ya faili yako. Kwa mfano, katika kesi yangu, URL ni:


```url
https://github.com/tutorial-pandul/bitcoin-educational-content/blob/patch-1/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf
```



- Weka sehemu ya mwisho ya URL kuanzia `/resources` na kuendelea:


```url
/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf
```



- Ongeza kwenye msingi wa URL taarifa ifuatayo ili uwe na kiungo sahihi:


```url
https://github.com/DiscoverBitcoin/bitcoin-educational-content/blob/dev/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf
```


Tunachofanya hapa ni kutarajia kiungo cha baadaye cha faili yako, mara tu pendekezo lako litakapounganishwa na hazina chanzo ya Plan ₿ Academy.


- Rudi kwenye faili yako ya `bet.yml` na ubofye aikoni ya penseli: ![event](assets/47.webp)
- Ongeza kiungo chako hapo:

![event](assets/48.webp)


- Mara tu mabadiliko yako yatakapokamilika, bofya kitufe cha 'Kufanya mabadiliko...':

![event](assets/49.webp)


- Ongeza kichwa cha mabadiliko yako, pamoja na maelezo mafupi:

![event](assets/50.webp)


- Bonyeza kitufe cha kijani cha `Mabadiliko ya Kujitoa`:

![event](assets/51.webp)


---


- Ikiwa kila kitu kinaonekana kizuri kwako, rudi kwenye chanzo cha fork yako:

![event](assets/52.webp)


- Unapaswa kuona ujumbe unaoonyesha kwamba tawi lako limebadilishwa. Bonyeza kitufe cha `Linganisha na uvute ombi`:

![event](assets/53.webp)


- Ongeza kichwa wazi na maelezo kwa ajili ya PR yako:

![event](assets/54.webp)


- Bonyeza kitufe cha 'Unda ombi la kuvuta':

![event](assets/55.webp)

Hongera! PR yako imeundwa kwa mafanikio. Msimamizi sasa ataikagua na, ikiwa kila kitu kiko katika mpangilio, ataiunganisha kwenye hazina kuu ya Plan ₿ Academy. Unapaswa kuona BET yako ikionekana kwenye tovuti siku chache baadaye.


Hakikisha unafuatilia maendeleo ya PR yako. Msimamizi anaweza kuacha maoni akiomba maelezo ya ziada. Mradi tu PR yako haijathibitishwa, unaweza kuiangalia kwenye kichupo cha Maombi ya Kuvuta kwenye hazina ya Plan ₿ Academy GitHub:

![event](assets/56.webp)

Asante sana kwa mchango wako muhimu! :)