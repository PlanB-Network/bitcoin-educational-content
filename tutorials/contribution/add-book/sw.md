---
name: Kuongeza Kitabu kwenye Mtandao wa PlanB
description: Jinsi ya kuongeza kitabu kipya kwenye Mtandao wa PlanB?
---
![book](assets/cover.webp)


Dhamira ya PlanB ni kutoa nyenzo za elimu za kiwango cha juu kwenye Bitcoin katika lugha nyingi iwezekanavyo. Maudhui yote yaliyochapishwa kwenye tovuti ni chanzo huria na yamepangishwa kwenye GitHub, ikiruhusu mtu yeyote kuchangia katika uboreshaji wa jukwaa.


**Je, ungependa kuongeza kitabu kinachohusiana na Bitcoin kwenye tovuti ya PlanB Network na kuongeza mwonekano wa kazi yako, lakini hujui jinsi gani? Mafunzo haya ni kwa ajili yako!**

![book](assets/01.webp)


- Kwanza, unahitaji kuwa na akaunti ya GitHub. Ikiwa hujui jinsi ya kufungua akaunti, tumekuandalia mafunzo ya kina.


https://planb.network/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c



- Nenda kwenye [hakuna ya GitHub ya PlanB iliyowekwa kwa data](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/resources/books) katika sehemu ya `resources/books/`:

![book](assets/02.webp)


- Bofya sehemu ya juu kulia kwenye kitufe cha `Ongeza faili`, kisha kwenye `Unda faili mpya`:

![book](assets/03.webp)


- Ikiwa hujawahi kuchangia yaliyomo kwenye PlanB Network hapo awali, utahitaji kuunda Fork yako ya hazina asili. Kuunda hazina inamaanisha kuunda nakala ya hazina hiyo kwenye akaunti yako ya GitHub, kukuruhusu kufanya kazi kwenye mradi bila kuathiri hazina asili. Bonyeza kitufe cha `Fork hazina hii`:

![book](assets/04.webp)


- Kisha utafika kwenye ukurasa wa uhariri wa GitHub:

![book](assets/05.webp)


- Unda folda ya kitabu chako. Ili kufanya hivyo, katika kisanduku cha `Taja faili yako...`, andika jina la kitabu chako kwa herufi ndogo na vistari badala ya nafasi. Kwa mfano, ikiwa kitabu chako kinaitwa "*Kitabu changu cha Bitcoin*", unapaswa kuzingatia `kitabu changu-Bitcoin`:

![book](assets/06.webp)


- Ili kuhalalisha uundaji wa folda, ongeza tu kufyeka baada ya jina la kitabu chako kwenye kisanduku kimoja, kwa mfano: `my-Bitcoin-book/`. Kuongeza slash moja kwa moja huunda folda badala ya faili:

![book](assets/07.webp)


- Katika folda hii, utaunda faili ya kwanza ya YAML inayoitwa `book.yml`:

![book](assets/08.webp)


- Jaza faili hii maelezo kuhusu kitabu chako kwa kutumia kiolezo hiki:


```yaml
author:
level:
tags:
-
-
```


Hapa kuna maelezo ya kujaza kwa kila sehemu:


- `mwandishi`**: Onyesha jina la mtunzi wa kitabu.
- `ngazi`**: Onyesha kiwango kinachohitajika ili kuweza kusoma na kuelewa kitabu vizuri. Chagua kiwango kati ya zifuatazo:
 - `Mwanzo`
 - `katikati`
- `advanced` - `mtaalam`
- `tagi`**: Ongeza lebo mbili au tatu zinazohusiana na kitabu chako. Kwa mfano:
    - `Bitcoin`
    - `historia`
    - `teknolojia`
    - `uchumi`
    - `elimu`...


Kwa mfano, faili yako ya YAML inaweza kuonekana kama hii:


```yaml
author: Loïc Morel
level: beginner
tags:
- bitcoin
- technology
```


![book](assets/09.webp)


- Mara tu unapomaliza kufanya mabadiliko kwenye faili hii, yahifadhi kwa kubofya kitufe cha `Fanya mabadiliko...`:

![book](assets/10.webp)


- Ongeza kichwa cha mabadiliko yako, pamoja na maelezo mafupi:

![book](assets/11.webp)


- Bofya kwenye kitufe cha Green `Pendekeza mabadiliko`:

![book](assets/12.webp)


- Kisha utafika kwenye ukurasa unaofupisha mabadiliko yako yote:

![book](assets/13.webp)


- Bofya kwenye picha yako ya wasifu ya GitHub juu kulia, kisha kwenye `Hazina Zako`:

![book](assets/14.webp)


- Chagua Fork yako ya hazina ya Mtandao wa PlanB:

![book](assets/15.webp)


- Unapaswa kuona arifa juu ya dirisha na tawi lako jipya. Pengine inaitwa `kiraka-1`. Bonyeza juu yake:

![book](assets/16.webp)


- Sasa uko kwenye tawi lako la kufanya kazi:

![book](assets/17.webp)


- Rudi kwenye folda ya `rasilimali/vitabu/` na uchague folda ya kitabu chako ambayo umeunda hivi punde katika ahadi iliyotangulia:

![book](assets/18.webp)


- Katika folda ya kitabu chako, bofya kitufe cha `Ongeza faili`, kisha kwenye `Unda faili mpya`:

![book](assets/19.webp)


- Ipe jina folda hii mpya `assets` na uthibitishe uundaji wake kwa kuweka kufyeka `/` mwishoni:

![book](assets/20.webp)


- Katika folda hii ya `asethi`, unda faili inayoitwa `.gitkeep`:

![book](assets/21.webp)


- Bofya kitufe cha `Fanya mabadiliko...`:

![book](assets/22.webp)


- Acha kichwa cha ahadi kama chaguo-msingi, na uhakikishe kuwa kisanduku cha `Weka moja kwa moja kwenye tawi-1` kimetiwa alama, kisha ubofye `Fanya mabadiliko`:

![book](assets/23.webp)


- Rudi kwenye folda ya `asethi`:

![book](assets/24.webp)


- Bonyeza kitufe cha `Ongeza faili`, kisha kwenye `Pakia faili`:

![book](assets/25.webp)


- Ukurasa mpya utafunguliwa. Buruta na udondoshe picha ya jalada la kitabu chako kwenye eneo. Picha hii itaonyeshwa kwenye tovuti ya PlanB Network:

![book](assets/26.webp)


- Kuwa mwangalifu, picha lazima iwe katika muundo wa kitabu, ili kukabiliana vyema na tovuti yetu, kama kwa mfano:

![book](assets/27.webp)


- Mara tu picha inapopakiwa, hakikisha kisanduku cha `Jikabidhi moja kwa moja kwenye tawi la 1` kimetiwa alama, kisha ubofye `Fanya mabadiliko`:

![book](assets/28.webp)- Please note, your image must be named `cover_en` if the cover is in English and must be in `.webp` format. Therefore, the complete file name should be `cover_en.webp`, `cover_fr.webp`, `cover_it.webp`, etc. If you wish to use a different cover image for each language, for example in the case of a book translation, you can place them in the same location in the `assets` folder:

![book](assets/29.webp)


- Rudi kwenye folda yako ya `asethi` na ubofye faili ya mpatanishi ya `.gitkeep`:

![book](assets/30.webp)


- Ukiwa kwenye faili, bofya kwenye vitone 3 vidogo kwenye sehemu ya juu kulia kisha kwenye `Futa faili`:

![book](assets/31.webp)


- Hakikisha bado uko kwenye tawi lile lile linalofanya kazi, kisha ubofye kitufe cha `Fanya mabadiliko...`:

![book](assets/32.webp)


- Ongeza kichwa na maelezo kwenye ahadi yako, kisha ubofye `Fanya mabadiliko`:

![book](assets/33.webp)


- Rudi kwenye folda ya kitabu chako:

![book](assets/34.webp)


- Bonyeza kitufe cha `Ongeza faili`, kisha kwenye `Unda faili mpya`:

![book](assets/35.webp)


- Unda faili mpya ya YAML kwa kuipa jina kwa kiashirio cha lugha cha kitabu. Faili hii itatumika kwa maelezo ya kitabu. Kwa mfano, ikiwa ninataka kuandika maelezo yangu kwa Kiingereza, nitaita faili hii `en.yml`:

![book](assets/36.webp)


- Jaza faili hii ya YAML kwa kutumia kiolezo hiki:

```yaml
title: ""
publication_year:
cover: cover_en.webp
original: true
description: |

contributors:
-
```


Hapa kuna maelezo ya kujaza kwa kila sehemu:


- `kichwa`**: Onyesha jina la kitabu katika nukuu.
- `mwaka_wa_chapisho`**: Onyesha mwaka ambao kitabu kilichapishwa.
- `kifuniko`**: Onyesha jina la faili linalolingana na picha ya jalada, kwa mujibu wa lugha ya faili ya YAML unayohariri sasa. Kwa mfano, ikiwa unahariri faili ya `en.yml` na hapo awali umeongeza picha ya jalada ya Kiingereza inayoitwa `cover_en.webp`, onyesha kwa urahisi `cover_en.webp` katika sehemu hii.
- `maelezo`**: Ongeza aya fupi inayoelezea kitabu. Maelezo lazima yawe katika lugha sawa na ilivyoonyeshwa katika kichwa cha faili ya YAML.
- `wachangiaji`**: Ongeza kitambulisho chako cha mchangiaji ikiwa unacho.


Kwa mfano, faili yako ya YAML inaweza kuonekana kama hii:


```yaml