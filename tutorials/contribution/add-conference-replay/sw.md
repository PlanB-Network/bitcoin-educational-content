---
name: Inaongeza Urudiaji wa Mkutano
description: Jinsi ya kuongeza uchezaji wa mkutano kwenye PlanB Network?
---
![conference](assets/cover.webp)


Dhamira ya PlanB ni kutoa nyenzo za elimu za kiwango cha juu kwenye Bitcoin katika lugha nyingi iwezekanavyo. Maudhui yote yaliyochapishwa kwenye tovuti ni chanzo huria na yamepangishwa kwenye GitHub, ikiruhusu mtu yeyote kuchangia katika uboreshaji wa jukwaa.


Je, ungependa kuongeza uchezaji tena wa mkutano wako wa Bitcoin kwenye tovuti ya PlanB Network na kutoa mwonekano wa tukio hili, lakini hujui jinsi gani? Mafunzo haya ni kwa ajili yako!


Hata hivyo, ikiwa ungependa kuongeza mkutano utakaofanyika siku zijazo, nakushauri usome somo hili lingine ambalo tunaeleza jinsi ya kuongeza tukio jipya kwenye tovuti.


https://planb.network/tutorials/contribution/resource/add-event-1d3df554-c2d8-4e93-853f-58f672c5e097


![conference](assets/01.webp)


- Kwanza, unahitaji kuwa na akaunti kwenye GitHub. Ikiwa hujui jinsi ya kufungua akaunti, tumekuandalia mafunzo ya kina.


https://planb.network/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c



- Nenda kwenye [hakuna ya GitHub ya PlanB iliyowekwa kwa data](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/resources/conference) katika sehemu ya `rasilimali/mkutano/`:

![conference](assets/02.webp)


- Bofya sehemu ya juu kulia kwenye kitufe cha `Ongeza faili`, kisha kwenye `Unda faili mpya`:

![conference](assets/03.webp)


- Ikiwa hujawahi kuchangia yaliyomo kwenye PlanB Network hapo awali, utahitaji kuunda Fork yako ya hazina asili. Kuunda hazina inamaanisha kuunda nakala ya hazina hiyo kwenye akaunti yako ya GitHub, ambayo hukuruhusu kufanya kazi kwenye mradi bila kuathiri hazina asili. Bonyeza kitufe cha `Fork hazina hii`:

![conference](assets/04.webp)


- Kisha utafika kwenye ukurasa wa uhariri wa GitHub:

![conference](assets/05.webp)


- Unda folda ya mkutano wako. Ili kufanya hivyo, katika kisanduku cha `Taja faili yako...`, andika jina la mkutano wako kwa herufi ndogo na vistari badala ya nafasi. Kwa mfano, ikiwa mkutano wako unaitwa "Paris Bitcoin Conference", unapaswa kuzingatia `paris-Bitcoin-conference`. Pia ongeza mwaka wa mkutano wako, kwa mfano: `paris-Bitcoin-conference-2024`:

![conference](assets/06.webp)


- Ili kuthibitisha uundaji wa folda, kumbuka tu kufyeka baada ya jina lako kwenye kisanduku sawa, kwa mfano: `paris-Bitcoin-conference-2024/`. Kuongeza slash moja kwa moja huunda folda badala ya faili:

![conference](assets/07.webp)


- Katika folda hii, utaunda faili ya kwanza ya YAML inayoitwa `conference.yml`:

![conference](assets/08.webp)

Jaza faili hii habari inayohusiana na mkutano wako kwa kutumia kiolezo hiki:

```yaml
year:
name:
builder:
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
builder: Paris Bitcoin Conference
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


Ikiwa bado huna kitambulisho cha "*mjenzi*" cha shirika lako, unaweza kukiongeza kwa kufuata mafunzo haya mengine.


https://planb.network/tutorials/contribution/resource/add-builder-b5834c46-6dcc-4064-8d68-1ef529991d3d




- Mara tu unapomaliza kufanya mabadiliko kwenye faili hii, yahifadhi kwa kubofya kitufe cha `Fanya mabadiliko...`:

![conference](assets/10.webp)


- Ongeza kichwa cha mabadiliko yako, pamoja na maelezo mafupi:

![conference](assets/11.webp)


- Bofya kwenye kitufe cha Green `Pendekeza mabadiliko`:

![conference](assets/12.webp)


- Kisha utafika kwenye ukurasa unaofupisha mabadiliko yako yote:

![conference](assets/13.webp)


- Bofya kwenye picha yako ya wasifu ya GitHub juu kulia, kisha kwenye `Hazina Zako`:

![conference](assets/14.webp)


- Chagua Fork yako ya hazina ya Mtandao wa PlanB:

![conference](assets/15.webp)


- Unapaswa kuona arifa juu ya dirisha na tawi lako jipya. Pengine inaitwa `kiraka-1`. Bonyeza juu yake:

![conference](assets/16.webp)


- Sasa uko kwenye tawi lako la kufanya kazi:

![conference](assets/17.webp)


- Rudi kwenye folda ya `rasilimali/mkutano/` na uchague folda ya mkutano wako ambayo umeunda hivi punde katika ahadi iliyotangulia:

![conference](assets/18.webp)


- Kwenye folda ya mkutano wako, bofya kitufe cha `Ongeza faili`, kisha kwenye `Unda faili mpya`:

![conference](assets/19.webp)


- Ipe jina folda hii mpya `assets` na uthibitishe uundaji wake kwa kuweka kufyeka `/` mwishoni:

![conference](assets/20.webp)


- Katika folda hii ya `asethi`, unda faili inayoitwa `.gitkeep`:

![conference](assets/21.webp)


- Bofya kitufe cha `Fanya mabadiliko...`:

![conference](assets/22.webp)


- Acha kichwa cha ahadi kama chaguo-msingi, na uhakikishe kuwa kisanduku cha `Weka moja kwa moja kwenye tawi-1` kimetiwa alama, kisha ubofye `Fanya mabadiliko`:

![conference](assets/23.webp)


- Rudi kwenye folda ya `asethi`:

![conference](assets/24.webp)


- Bonyeza kitufe cha `Ongeza faili`, kisha kwenye `Pakia faili`:

![conference](assets/25.webp)


- Ukurasa mpya utafunguliwa. Buruta na uangushe picha inayowakilisha mkutano wako na itaonyeshwa kwenye tovuti ya PlanB Network: ![conference](assets/26.webp)
- Inaweza kuwa nembo, kijipicha, au hata bango:

![conference](assets/27.webp)


- Mara tu picha inapopakiwa, hakikisha kuwa kisanduku cha `Jikabidhi moja kwa moja kwenye tawi la 1` kimetiwa alama, kisha ubofye `Fanya mabadiliko`:

![conference](assets/28.webp)


- Kuwa mwangalifu, ni lazima picha yako iitwe `kijipicha` na lazima iwe katika umbizo la `.webp`. Kwa hivyo jina kamili la faili linafaa kuwa: `thumbnail.webp`:

![conference](assets/29.webp)


- Rudi kwenye folda yako ya `asethi` na ubofye faili ya kati ya `.gitkeep`:

![conference](assets/30.webp)


- Ukiwa kwenye faili, bofya kwenye vitone 3 vidogo kwenye kona ya juu kulia kisha kwenye `Futa faili`:

![conference](assets/31.webp)


- Thibitisha kuwa bado uko kwenye tawi moja linalofanya kazi, kisha ubofye kitufe cha `Fanya mabadiliko`:

![conference](assets/32.webp)


- Ongeza kichwa na maelezo kwa ahadi yako, kisha ubofye `Fanya mabadiliko`:

![conference](assets/33.webp)


- Rudi kwenye folda yako ya mkutano:

![conference](assets/34.webp)


- Bonyeza kitufe cha `Ongeza faili`, kisha kwenye `Unda faili mpya`:

![conference](assets/35.webp)


- Unda alama mpya (.md) faili kwa kuipa jina kwa kiashirio cha lugha yako asili. Faili hii itatumika kwa marudio ya mkutano wako. Kwa mfano, ikiwa ninataka kuandika maelezo ya mikutano kwa Kiingereza, nitaita faili hii en.md:

![conference](assets/36.webp)


- Jaza faili hii ya alama kwa kutumia kiolezo hiki ambacho unaweza kurekebisha kwa usanidi wa mkutano wako:


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


- Mwanzoni mwa hati yako, katika "jambo la mbele," jaza sehemu ya `jina:` yenye jina la mkutano wako na mwaka wa marudio. Katika sehemu ya `maelezo:`, andika maelezo mafupi ya tukio lako katika lugha ya faili. Kwa mfano, kwa faili inayoitwa `en.md`, maelezo yanapaswa kuwa katika Kiingereza. Timu ya PlanB Network itachukua jukumu la kutafsiri maelezo yako kwa kutumia muundo wao.
- Majina ya ngazi ya kwanza, yaliyowekwa alama ya `#`, yanatumiwa kuandaa mkutano kwa matukio. Kwa mfano, `# Jukwaa Kuu` kwa jukwaa kuu na `# Chumba cha Warsha` kwa jukwaa maalum kwa warsha.



- Vichwa vya kiwango cha pili, vilivyowekwa alama kwa `##` mara mbili, vinatumika kutenganisha video tofauti za kucheza tena. Ikiwa makongamano yalirekodiwa mfululizo kwa muda wa nusu siku, onyesha, kwa mfano, `## Ijumaa asubuhi`. Ikiwa makongamano yalirekodiwa na kutangazwa kibinafsi, taja mkutano huo moja kwa moja na mada ya kiwango cha pili.



- Chini ya kila mada ya kiwango cha pili, weka kiungo cha video inayolingana ya kucheza tena. Sintaksia inapaswa kuwa: `![video](https://youtu.be/XXXXXXXXXXXX)`, ikibadilisha `XXXXXXXXXXXX` na kiungo halisi cha video.



- Ikiwa muundo unaruhusu (mikutano ya mtu binafsi), unaweza kuongeza majina ya wasemaji. Ili kufanya hivyo, ongeza sehemu ya `Spika:` ikifuatiwa na jina au jina bandia la spika chini ya kiungo cha video. Ikiwa kuna wasemaji wengi, tenganisha kila jina kwa koma, kama hii kwa mfano: `Spika: Satoshi Nakamoto, Satoshi Nakamoto, Satoshi Nakamoto, Satoshi Nakamoto`.


---


- Mara tu marekebisho yako kwenye faili hii yanapokamilika, yahifadhi kwa kubofya kitufe cha `Fanya mabadiliko...`:

![conference](assets/38.webp)


- Ongeza kichwa cha marekebisho yako, pamoja na maelezo mafupi:

![conference](assets/39.webp)


- Bonyeza kwa `Fanya mabadiliko`:

![conference](assets/40.webp)


- Folda yako ya mkutano inapaswa sasa kuonekana kama hii:

![conference](assets/41.webp)


- Ikiwa kila kitu ni cha kuridhika kwako, rudi kwenye mzizi wa Fork yako:

![conference](assets/42.webp)


- Unapaswa kuona ujumbe unaoonyesha kuwa tawi lako limefanyiwa marekebisho. Bonyeza kitufe cha `Linganisha & vuta ombi`:

![conference](assets/43.webp)


- Ongeza kichwa na maelezo wazi kwa PR yako:

![conference](assets/44.webp)


- Bonyeza kitufe cha `Unda ombi la kuvuta`:

![conference](assets/45.webp)

Hongera! PR yako imeundwa. Msimamizi sasa atakagua na, ikiwa kila kitu kiko sawa, aiunganishe kwenye hazina kuu ya PlanB Network. Unapaswa kuona marudio ya mkutano wako yakionekana kwenye tovuti siku chache baadaye.


Tafadhali hakikisha unafuata maendeleo ya PR yako. Inawezekana kwamba msimamizi anaweza kuacha maoni akiuliza maelezo ya ziada. Maadamu PR yako haijathibitishwa, unaweza kuiona chini ya kichupo cha `Vuta maombi` kwenye hazina ya GitHub ya Mtandao wa PlanB:

![conference](assets/46.webp)


Asante sana kwa mchango wako muhimu! :)