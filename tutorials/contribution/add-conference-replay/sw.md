---
name: Kuongeza Marudio ya Mkutano
description: Jinsi ya kuongeza marudio ya mkutano kwenye Plan ₿ Academy?
---
![conference](assets/cover.webp)


Dhamira ya PlanB ni kutoa rasilimali za elimu za kiwango cha juu kuhusu Bitcoin katika lugha nyingi iwezekanavyo. Maudhui yote yaliyochapishwa kwenye tovuti ni chanzo huria na yamehifadhiwa kwenye GitHub, hivyo kumruhusu mtu yeyote kuchangia katika uboreshaji wa jukwaa.


Je, unataka kuongeza marudio ya mkutano wako wa Bitcoin kwenye tovuti ya Plan ₿ Academy na kutoa mwonekano wa tukio hili, lakini hujui jinsi gani? Mafunzo haya ni kwa ajili yako!


Hata hivyo, ikiwa unataka kuongeza mkutano utakaofanyika katika siku zijazo, nakushauri usome mafunzo haya mengine ambapo tunaelezea jinsi ya kuongeza tukio jipya kwenye tovuti.


https://planb.academy/tutorials/contribution/resource/add-event-1d3df554-c2d8-4e93-853f-58f672c5e097


![conference](assets/01.webp)


- Kwanza, unahitaji kuwa na akaunti kwenye GitHub. Kama hujui jinsi ya kuunda akaunti, tumeandaa mafunzo ya kina ili kukuongoza.


https://planb.academy/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c



- Nenda kwenye [hifadhi ya GitHub ya PlanB iliyojitolea kwa data](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/conference) katika sehemu ya `resources/conference/`:

![conference](assets/02.webp)


- Bonyeza juu kulia kwenye kitufe cha `Ongeza faili`, kisha kwenye `Unda faili mpya`:

![conference](assets/03.webp)


- Ikiwa hujawahi kuchangia kwenye maudhui ya Plan ₿ Academy hapo awali, utahitaji kuunda fork yako ya hazina asili. Kuweka hazina ya Fork kunamaanisha kuunda nakala ya hazina hiyo kwenye akaunti yako ya GitHub, ambayo hukuruhusu kufanya kazi kwenye mradi bila kuathiri hazina asili. Bonyeza kitufe cha `Fork hazina hii`:

![conference](assets/04.webp)


- Kisha utafika kwenye ukurasa wa uhariri wa GitHub:

![conference](assets/05.webp)


- Unda folda kwa ajili ya mkutano wako. Ili kufanya hivi, katika kisanduku cha `Taja faili yako...`, andika jina la mkutano wako kwa herufi ndogo ukiwa na vibonyezo badala ya nafasi. Kwa mfano, ikiwa mkutano wako unaitwa "Mkutano wa Paris Bitcoin", unapaswa kuandika `mkutano-wa-paris-bitcoin`. Pia ongeza mwaka wa mkutano wako, kwa mfano: `mkutano-wa-paris-bitcoin-2024`:

![conference](assets/06.webp)


- Ili kuthibitisha uundaji wa folda, andika tu mkato baada ya jina lako katika kisanduku hicho hicho, kwa mfano: `paris-bitcoin-conference-2024/`. Kuongeza mkato huunda folda kiotomatiki badala ya faili:

![conference](assets/07.webp)


- Katika folda hii, utaunda faili ya kwanza ya YAML inayoitwa `conference.yml`:

![conference](assets/08.webp)

Jaza faili hii na taarifa zinazohusiana na mkutano wako kwa kutumia kiolezo hiki:

```yaml
year:
name:
project:
location:
language:
-
links:
website:
twitter:
tags:
-
-
```


Kwa mfano, faili yako ya YAML inaweza kuonekana kama hii:


```yaml
year: 2024-08
name: Paris Bitcoin Conference 2024
project: Paris Bitcoin Conference
location: Paris, France
language:
- fr
- en
links:
website: https://paris.bitcoin.fr/conference
twitter: https://twitter.com/ParisBitcoinConference
tags:
- International
- All Public
```


![conference](assets/09.webp)


Ikiwa bado huna kitambulisho cha "*mradi*" cha shirika lako, unaweza kukiongeza kwa kufuata mafunzo haya mengine.


https://planb.academy/tutorials/contribution/resource/add-builder-b5834c46-6dcc-4064-8d68-1ef529991d3d




- Ukishamaliza kufanya mabadiliko kwenye faili hii, yahifadhi kwa kubofya kitufe cha 'Commit changes...':

![conference](assets/10.webp)


- Ongeza kichwa cha mabadiliko yako, pamoja na maelezo mafupi:

![conference](assets/11.webp)


- Bonyeza kitufe cha kijani cha `Pendekeza mabadiliko`:

![conference](assets/12.webp)


- Kisha utafika kwenye ukurasa unaofupisha mabadiliko yako yote:

![conference](assets/13.webp)


- Bonyeza picha ya wasifu wako wa GitHub upande wa juu kulia, kisha kwenye `Hazina Zako`:

![conference](assets/14.webp)


- Chagua fork yako ya hazina ya Plan ₿ Academy:

![conference](assets/15.webp)


- Unapaswa kuona arifa juu ya dirisha na tawi lako jipya. Huenda inaitwa `kiraka-1`. Bonyeza juu yake:

![conference](assets/16.webp)


- Sasa uko kwenye tawi lako la kazi:

![conference](assets/17.webp)


- Rudi kwenye folda ya `rasilimali/mkutano/` na uchague folda ya mkutano wako ambayo umeunda tu katika ahadi iliyopita:

![conference](assets/18.webp)


- Kwenye folda ya mkutano wako, bofya kitufe cha `Ongeza faili`, kisha kwenye `Unda faili mpya`:

![conference](assets/19.webp)


- Ipe jina folda hii mpya `assets` na uthibitishe uundaji wake kwa kuweka mkato `/` mwishoni:

![conference](assets/20.webp)


- Katika folda hii ya `assets`, tengeneza faili inayoitwa `.gitkeep`:

![conference](assets/21.webp)


- Bonyeza kitufe cha 'Mabadiliko ya Kujitolea...':

![conference](assets/22.webp)


- Acha kichwa cha ahadi kama chaguo-msingi, na uhakikishe kisanduku cha `Kujitoa moja kwa moja kwenye tawi la kiraka-1` kimechaguliwa, kisha bofya `Mabadiliko ya ahadi`:

![conference](assets/23.webp)


- Rudi kwenye folda ya `mali`:

![conference](assets/24.webp)


- Bonyeza kitufe cha `Ongeza faili`, kisha kwenye `Pakia faili`:

![conference](assets/25.webp)


- Ukurasa mpya utafunguliwa. Buruta na uangushe picha inayowakilisha mkutano wako na itaonyeshwa kwenye tovuti ya Plan ₿ Academy: ![conference](assets/26.webp)
- Inaweza kuwa nembo, kijipicha, au hata bango:

![conference](assets/27.webp)


- Mara tu picha inapopakiwa, hakikisha kwamba kisanduku cha `Kujitoa moja kwa moja kwenye tawi la kiraka-1` kimechaguliwa, kisha bofya `Kujitoa mabadiliko`:

![conference](assets/28.webp)


- Kuwa mwangalifu, picha yako lazima ipewe jina la `thumbnail` na lazima iwe katika umbizo la `.webp`. Kwa hivyo jina kamili la faili linapaswa kuwa: `thumbnail.webp`:

![conference](assets/29.webp)


- Rudi kwenye folda yako ya `assets` na ubofye faili ya kati ya `.gitkeep`:

![conference](assets/30.webp)


- Ukishaingia kwenye faili, bofya nukta tatu ndogo kwenye kona ya juu kulia kisha kwenye `Futa faili`:

![conference](assets/31.webp)


- Thibitisha kwamba bado uko kwenye tawi lile lile linalofanya kazi, kisha bofya kitufe cha 'Commit changes':

![conference](assets/32.webp)


- Ongeza kichwa na maelezo kwenye ahadi yako, kisha bofya 'Mabadiliko ya Kujitoa':

![conference](assets/33.webp)


- Rudi kwenye folda yako ya mkutano:

![conference](assets/34.webp)


- Bonyeza kitufe cha `Ongeza faili`, kisha kwenye `Unda faili mpya`:

![conference](assets/35.webp)


- Unda faili mpya ya alama ya chini (.md) kwa kuiita kwa kutumia kiashiria cha lugha yako ya asili. Faili hii itatumika kwa ajili ya marudio ya mkutano wako. Kwa mfano, ikiwa ninataka kuandika maelezo ya mikutano kwa Kiingereza, nitaita faili hii en.md:

![conference](assets/36.webp)


- Jaza faili hii ya alama kwa kutumia kiolezo hiki ambacho unaweza kurekebisha kulingana na usanidi wa mkutano wako:


```markdown
---
name: Paris Bitcoin Conference 2024
description: The largest Bitcoin conference in France with over 8,000 participants each year!
---

# Main Stage

## Friday morning

![video](https://youtu.be/XXXXXXXXXXXX)

## Friday afternoon

![video](https://youtu.be/XXXXXXXXXXXX)

## Saturday morning

![video](https://youtu.be/XXXXXXXXXXXX)

## Saturday afternoon

![video](https://youtu.be/XXXXXXXXXXXX)

# Workshop Room

## The Future of Bitcoin Mining: Challenges and Innovations

![video](https://youtu.be/XXXXXXXXXXXX)

Speaker: Satoshi Nakamoto, Satoshi Nakamoto

## Is Privacy Still Possible On Bitcoin?

![video](https://youtu.be/XXXXXXXXXXXX)

Speaker: Satoshi Nakamoto

## Bitcoin Core: Deep Dive into the Codebase

![video](https://youtu.be/XXXXXXXXXXXX)

Speaker: Satoshi Nakamoto, Satoshi Nakamoto, Satoshi Nakamoto, Satoshi Nakamoto

## Building and Securing Bitcoin Wallets With Miniscript

![video](https://youtu.be/XXXXXXXXXXXX)

Speaker: Satoshi Nakamoto
```


![conference](assets/37.webp)


- Mwanzoni mwa hati yako, katika "jambo la mbele," jaza sehemu ya `jina:` yenye jina la mkutano wako na mwaka wa marudio. Katika sehemu ya `maelezo:`, andika maelezo mafupi ya tukio lako katika lugha ya faili. Kwa mfano, kwa faili inayoitwa `en.md`, maelezo yanapaswa kuwa kwa Kiingereza. Timu ya Plan ₿ Academy itachukua jukumu la kutafsiri maelezo yako kwa kutumia mfumo wao.
- Majina ya ngazi ya kwanza, yenye alama ya `#`, hutumika kupanga mkutano kwa kutumia matukio. Kwa mfano, `# Jukwaa Kuu` kwa jukwaa kuu na `# Chumba cha Warsha` kwa jukwaa lililotengwa kwa ajili ya warsha.



- Vichwa vya ngazi ya pili, vilivyowekwa alama ya `##` mara mbili, hutumika kutenganisha video tofauti za marudio. Ikiwa mikutano ilirekodiwa mfululizo kwa nusu siku, onyesha, kwa mfano, `## Ijumaa asubuhi`. Ikiwa mikutano ilirekodiwa na kutangazwa moja kwa moja, ipe jina mkutano moja kwa moja kwa kutumia kichwa cha ngazi ya pili.



- Chini ya kila kichwa cha ngazi ya pili, ingiza kiungo cha video ya marudio inayolingana. Sintaksia inapaswa kuwa: `![video](https://youtu.be/XXXXXXXXXXXX)`, ikibadilisha `XXXXXXXXXXXX` na kiungo halisi cha video.



- Ikiwa muundo unaruhusu (mikutano ya mtu binafsi), unaweza kuongeza majina ya wazungumzaji. Ili kufanya hivyo, ongeza sehemu ya `Spika:` ikifuatiwa na jina au jina bandia la mzungumzaji chini ya kiungo cha video. Ikiwa kuna wazungumzaji wengi, tenganisha kila jina kwa koma, kama hii kwa mfano: `Spika: Satoshi Nakamoto, Satoshi Nakamoto, Satoshi Nakamoto, Satoshi Nakamoto`.


---


- Mara tu marekebisho yako kwenye faili hii yatakapokamilika, yahifadhi kwa kubofya kitufe cha `Commit changes...`:

![conference](assets/38.webp)


- Ongeza kichwa cha marekebisho yako, pamoja na maelezo mafupi:

![conference](assets/39.webp)


- Bonyeza 'Kufanya mabadiliko':

![conference](assets/40.webp)


- Folda yako ya mkutano sasa inapaswa kuonekana kama hii:

![conference](assets/41.webp)


- Ikiwa kila kitu kinakutosheleza, rudi kwenye chanzo cha fork yako:

![conference](assets/42.webp)


- Unapaswa kuona ujumbe unaoonyesha kwamba tawi lako limefanyiwa marekebisho. Bonyeza kitufe cha `Linganisha na uvute ombi`:

![conference](assets/43.webp)


- Ongeza kichwa na maelezo wazi kwa ajili ya PR yako:

![conference](assets/44.webp)


- Bonyeza kitufe cha 'Unda ombi la kuvuta':

![conference](assets/45.webp)

Hongera! PR yako imeundwa kwa mafanikio. Msimamizi sasa ataikagua na, ikiwa kila kitu kiko katika mpangilio, ataiunganisha kwenye hazina kuu ya Plan ₿ Academy. Unapaswa kuona marudio ya mkutano wako yakionekana kwenye tovuti siku chache baadaye.


Tafadhali hakikisha unafuatilia maendeleo ya PR yako. Inawezekana kwamba msimamizi anaweza kuacha maoni akiomba maelezo ya ziada. Mradi PR yako haijathibitishwa, unaweza kuiona chini ya kichupo cha `Maombi ya Vuta` kwenye hazina ya GitHub ya Plan ₿ Academy:

![conference](assets/46.webp)


Asante sana kwa mchango wako muhimu! :)