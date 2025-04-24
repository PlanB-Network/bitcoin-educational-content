---
name: Ongeza tukio kwenye PlanB Network
description: Je, ninapendekezaje kuongeza tukio jipya kwenye PlanB Network?
---
![event](assets/cover.webp)


Dhamira ya PlanB ni kutoa nyenzo za elimu za kiwango cha juu kwenye Bitcoin katika lugha nyingi iwezekanavyo. Maudhui yote yaliyochapishwa kwenye tovuti ni chanzo-wazi na yamepangishwa kwenye GitHub, yakimpa mtu yeyote fursa ya kuchangia katika uboreshaji wa jukwaa.


Ikiwa ungependa kuongeza mkutano wa Bitcoin kwenye tovuti ya PlanB Network na kuongeza mwonekano wa tukio lako, lakini hujui jinsi gani? Mafunzo haya ni kwa ajili yako!

![event](assets/01.webp)


- Kwanza, unahitaji kuwa na akaunti kwenye GitHub. Ikiwa hujui jinsi ya kufungua akaunti, tumekuandalia mafunzo ya kina.


https://planb.network/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c



- Nenda kwenye [hakuna ya GitHub ya PlanB iliyowekwa kwa data](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/resources/conference) katika sehemu ya `rasilimali/mkutano/`:

![event](assets/02.webp)


- Bofya sehemu ya juu kulia kwenye kitufe cha `Ongeza faili`, kisha kwenye `Unda faili mpya`:

![event](assets/03.webp)


- Ikiwa hujawahi kuchangia yaliyomo kwenye PlanB Network hapo awali, utahitaji kuunda Fork yako ya hazina asili. Kuunda hazina inamaanisha kuunda nakala ya hazina hiyo kwenye akaunti yako ya GitHub, kukuruhusu kufanya kazi kwenye mradi bila kuathiri hazina asili. Bonyeza kitufe cha `Fork hazina hii`:

![event](assets/04.webp)


- Kisha utafika kwenye ukurasa wa uhariri wa GitHub:

![event](assets/05.webp)


- Unda folda ya mkutano wako. Ili kufanya hivyo, katika kisanduku cha `Taja faili yako...`, andika jina la mkutano wako kwa herufi ndogo na vistari badala ya nafasi. Kwa mfano, ikiwa mkutano wako unaitwa "Paris Bitcoin Conference", unapaswa kuzingatia `paris-Bitcoin-conference`. Pia ongeza mwaka wa mkutano wako, kwa mfano: `paris-Bitcoin-conference-2024`:

![event](assets/06.webp)


- Ili kuthibitisha uundaji wa folda, kumbuka tu kufyeka baada ya jina lako kwenye kisanduku sawa, kwa mfano: `paris-Bitcoin-conference-2024/`. Kuongeza slash moja kwa moja huunda folda badala ya faili:

![event](assets/07.webp)


- Katika folda hii, utaunda faili ya kwanza ya YAML inayoitwa `events.yml`:

![event](assets/08.webp)


- Jaza faili hii habari kuhusu mkutano wako kwa kutumia kiolezo hiki:


```yaml
start_date:
end_date:
address_line_1:
address_line_2:
address_line_3:
name:
builder:
type: conference
book_online: false
book_in_person: false
price_dollars: 0
description:
language:
-
links:
website:
replay_url:
live_url :
tags:
-
```


Kwa mfano, faili yako ya YAML inaweza kuonekana kama hii:


```yaml
start_date: 2024-08-15
end_date: 2024-08-18
address_line_1: Paris, France
address_line_2:
address_line_3:
name: Paris Bitcoin Conference 2024
builder: Paris Bitcoin Conference
type: conference
book_online: false
book_in_person: false
price_dollars: 0
description: The largest Bitcoin conference in France with over 8,000 participants each year!
language:
- fr
- en
- es
- it
links:
website: https://paris.bitcoin.fr/conference
replay_url:
live_url :
tags:
- Bitcoiner
- General
- International
```

![event](assets/09.webp)

Ikiwa bado huna kitambulisho cha "*mjenzi*" cha shirika lako, unaweza kukiongeza kwa kufuata mafunzo haya mengine.


https://planb.network/tutorials/contribution/resource/add-builder-b5834c46-6dcc-4064-8d68-1ef529991d3d




- Mara tu unapomaliza kufanya mabadiliko kwenye faili hii, yahifadhi kwa kubofya kitufe cha `Fanya mabadiliko...`:

![event](assets/10.webp)


- Ongeza kichwa cha mabadiliko yako, pamoja na maelezo mafupi:

![event](assets/11.webp)


- Bofya kwenye kitufe cha Green `Pendekeza mabadiliko`:

![event](assets/12.webp)


- Kisha utafika kwenye ukurasa unaofupisha mabadiliko yako yote:

![event](assets/13.webp)


- Bofya kwenye picha yako ya wasifu ya GitHub juu kulia, kisha kwenye `Hazina Zako`:

![event](assets/14.webp)


- Chagua Fork yako ya hazina ya Mtandao wa PlanB:

![event](assets/15.webp)


- Unapaswa kuona arifa juu ya dirisha na tawi lako jipya. Pengine inaitwa `kiraka-1`. Bonyeza juu yake:

![event](assets/16.webp)


- Sasa uko kwenye tawi lako la kufanya kazi:

![event](assets/17.webp)


- Rudi kwenye folda ya `rasilimali/mkutano/` na uchague folda ya mkutano wako ambayo umeunda hivi punde katika ahadi iliyotangulia:

![event](assets/18.webp)


- Kwenye folda ya mkutano wako, bofya kitufe cha `Ongeza faili`, kisha kwenye `Unda faili mpya`:

![event](assets/19.webp)


- Ipe jina folda hii mpya `assets` na uthibitishe uundaji wake kwa kuweka kufyeka `/` mwishoni:

![event](assets/20.webp)


- Katika folda hii ya `asethi`, unda faili inayoitwa `.gitkeep`:

![event](assets/21.webp)


- Bofya kitufe cha `Fanya mabadiliko...`:

![event](assets/22.webp)


- Acha kichwa cha ahadi kama chaguo-msingi, na uhakikishe kuwa kisanduku cha `Weka moja kwa moja kwenye tawi-1` kimetiwa alama, kisha ubofye `Fanya mabadiliko`:

![event](assets/23.webp)


- Rudi kwenye folda ya `asethi`:

![event](assets/24.webp)


- Bofya kwenye kitufe cha `Ongeza faili`, kisha kwenye `Pakia faili`: ![tukio](assets/25.webp)
- Ukurasa mpya utafunguliwa. Buruta na uangushe picha inayowakilisha mkutano wako na itaonyeshwa kwenye tovuti ya PlanB Network:

![event](assets/26.webp)


- Inaweza kuwa nembo, kijipicha, au hata bango:

![event](assets/27.webp)


- Pindi picha inapopakiwa, hakikisha kuwa kisanduku cha `Jikabidhi moja kwa moja kwenye tawi la 1` kimetiwa alama, kisha ubofye `Fanya mabadiliko`:

![event](assets/28.webp)


- Kuwa mwangalifu, ni lazima picha yako iitwe `kijipicha` na lazima iwe katika umbizo la `.webp`. Kwa hivyo jina kamili la faili linafaa kuwa: `thumbnail.webp`:

![event](assets/29.webp)


- Rudi kwenye folda yako ya `asethi` na ubofye faili ya kati `.gitkeep`:

![event](assets/30.webp)


- Ukiwa kwenye faili, bofya kwenye vitone 3 vidogo juu kulia kisha kwenye `Futa faili`:

![event](assets/31.webp)


- Thibitisha kuwa bado uko kwenye tawi moja linalofanya kazi, kisha ubofye kitufe cha `Fanya mabadiliko`:

![event](assets/32.webp)


- Ongeza kichwa na maelezo kwa ahadi yako, kisha ubofye `Fanya mabadiliko`:

![event](assets/33.webp)


- Rudi kwenye mzizi wa hazina yako:

![event](assets/34.webp)


- Unapaswa kuona ujumbe unaoonyesha kuwa tawi lako limefanyiwa mabadiliko. Bonyeza kitufe cha `Linganisha & vuta ombi`:

![event](assets/35.webp)


- Ongeza kichwa wazi na maelezo kwa PR yako:

![event](assets/36.webp)


- Bonyeza kitufe cha `Unda ombi la kuvuta`:

![event](assets/37.webp)

Hongera! PR yako imeundwa. Msimamizi sasa ataiangalia na, ikiwa kila kitu kiko sawa, aiunganishe kwenye hazina kuu ya PlanB Network. Unapaswa kuona tukio lako likionekana kwenye tovuti siku chache baadaye.


Hakikisha unafuata maendeleo ya PR yako. Msimamizi anaweza kuacha maoni akiuliza maelezo ya ziada. Maadamu PR yako haijathibitishwa, unaweza kuishauri kwenye kichupo cha `Vuta maombi` kwenye hazina ya PlanB Network GitHub:

![event](assets/38.webp)

Asante sana kwa mchango wako muhimu! :)