---
name: Kuongeza Mjenzi
description: Jinsi ya kupendekeza kuongezwa kwa mjenzi mpya kwenye PlanB Network?
---
![builder](assets/cover.webp)


Dhamira ya PlanB ni kutoa nyenzo za elimu za kiwango cha juu kwenye Bitcoin, katika lugha nyingi iwezekanavyo. Maudhui yote yaliyochapishwa kwenye tovuti ni chanzo-wazi na yamepangishwa kwenye GitHub, ambayo inaruhusu mtu yeyote kushiriki katika kuimarisha jukwaa.


Je, ungependa kuongeza "mjenzi" mpya wa Bitcoin kwenye tovuti ya PlanB Network na kutoa mwonekano kwa kampuni au programu yako, lakini hujui jinsi gani? Mafunzo haya ni kwa ajili yako!

![builder](assets/01.webp)


- Kwanza, unahitaji kuwa na akaunti ya GitHub. Ikiwa hujui jinsi ya kuunda akaunti, tumekuandalia mafunzo ya kina.


https://planb.network/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c



- Nenda kwenye [hakuna ya GitHub ya PlanB iliyowekwa kwa data](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/resources/builders) katika sehemu ya `rasilimali/mjenzi/`:

![builder](assets/02.webp)


- Bofya sehemu ya juu kulia kwenye kitufe cha `Ongeza faili`, kisha kwenye `Unda faili mpya`:

![builder](assets/03.webp)


- Ikiwa hujawahi kuchangia yaliyomo kwenye PlanB Network hapo awali, utahitaji kuunda Fork yako ya hazina asili. Kuunda hazina inamaanisha kuunda nakala ya hazina hiyo kwenye akaunti yako ya GitHub, ambayo hukuruhusu kufanya kazi kwenye mradi bila kuathiri hazina asili. Bonyeza kitufe cha `Fork hazina hii`:

![builder](assets/04.webp)


- Kisha utafika kwenye ukurasa wa uhariri wa GitHub:

![builder](assets/05.webp)


- Unda folda ya kampuni yako. Ili kufanya hivyo, katika kisanduku cha `Taja faili yako...`, andika jina la kampuni yako kwa herufi ndogo kwa vistari badala ya nafasi. Kwa mfano, kama kampuni yako inaitwa "Bitcoin Baguette", unapaswa kuandika `Bitcoin-baguette`:

![builder](assets/06.webp)


- Ili kuthibitisha uundaji wa folda, ongeza tu kufyeka baada ya jina lako kwenye kisanduku sawa, kwa mfano: `Bitcoin-baguette/`. Kuongeza slash moja kwa moja huunda folda badala ya faili:

![builder](assets/07.webp)


- Katika folda hii, utaunda faili ya kwanza ya YAML inayoitwa `builder.yml`:

![builder](assets/08.webp)


- Jaza faili hii maelezo kuhusu kampuni yako kwa kutumia kiolezo hiki:


```yaml
name:

address_line_1:
address_line_2:
address_line_3:

language:
-

links:
website:
twitter:
Github:
youtube:
nostr:

tags:
-
-

category:
```


Hapa ni nini cha kujaza kwa kila ufunguo:


- `jina`: Jina la kampuni yako (lazima);
- `Address` : Eneo la biashara yako (si lazima);
- `lugha` : Nchi ambazo biashara yako inafanya kazi au lugha zinazotumika (si lazima);
- `viungo` : Viungo mbalimbali rasmi vya biashara yako (si lazima);
- `tags` : Masharti 2 ambayo yanahitimu biashara yako (lazima);
- `category` : Kategoria inayofafanua vyema sehemu ambayo biashara yako inafanya kazi kati ya chaguo zifuatazo:
 - `Wallet`,
 - `miundombinu`,
 - `Exchange`,
 - `elimu`,
 - `huduma`,
 - `jumuiya`,
 - `mkutano`,
 - `faragha`,
 - `uwekezaji`,
 - `nodi`,
 - `Mining`,
 - `habari`,
 - `mtengenezaji`.


Kwa mfano, faili yako ya YAML inaweza kuonekana kama hii:


```yaml
name: Bitcoin Baguette

address_line_1: Paris, France
address_line_2:
address_line_3:

language:
- fr
- en

links:
website: https://bitcoin-baguette.com
twitter: https://twitter.com/bitcoinbaguette
Github:
youtube:
nostr:

tags:
- bitcoin
- education

category: education
```


![builder](assets/09.webp)


- Mara tu unapomaliza kufanya mabadiliko kwenye faili hii, yahifadhi kwa kubofya kitufe cha `Fanya mabadiliko...`:

![builder](assets/10.webp)


- Ongeza kichwa cha mabadiliko yako, pamoja na maelezo mafupi:

![builder](assets/11.webp)


- Bofya kwenye kitufe cha Green `Pendekeza mabadiliko`:

![builder](assets/12.webp)


- Kisha utafika kwenye ukurasa unaofupisha mabadiliko yako yote:

![builder](assets/13.webp)


- Bofya kwenye picha yako ya wasifu ya GitHub juu kulia, kisha kwenye `Hazina Zako`:

![builder](assets/14.webp)


- Chagua Fork yako ya hazina ya Mtandao wa PlanB:

![builder](assets/15.webp)


- Unapaswa kuona arifa juu ya dirisha na tawi lako jipya. Pengine inaitwa `kiraka-1`. Bonyeza juu yake:

![builder](assets/16.webp)


- Sasa uko kwenye tawi lako linalofanya kazi (**hakikisha uko kwenye tawi sawa na marekebisho yako ya awali, hii ni muhimu!**):

![builder](assets/17.webp)


- Rudi kwenye folda ya `rasilimali/wajenzi/` na uchague folda ya biashara yako ambayo umeunda hivi punde katika ahadi iliyotangulia:

![builder](assets/18.webp)


- Katika folda ya biashara yako, bofya kitufe cha `Ongeza faili`, kisha kwenye `Unda faili mpya`:

![builder](assets/19.webp)


- Ipe jina folda hii mpya `assets` na uthibitishe uundaji wake kwa kuweka kufyeka `/` mwishoni:

![builder](assets/20.webp)


- Katika folda hii ya `asethi`, unda faili inayoitwa `.gitkeep`:

![builder](assets/21.webp)


- Bonyeza kitufe cha `Fanya mabadiliko...`:

![builder](assets/22.webp)


- Acha jina la ahadi kama chaguo-msingi, na uhakikishe kuwa kisanduku cha `Weka moja kwa moja kwenye kiraka-1` kimetiwa alama, kisha ubofye `Fanya mabadiliko`: ![builder](assets/23.webp)
- Rudi kwenye folda ya `asethi`:

![builder](assets/24.webp)


- Bonyeza kitufe cha `Ongeza faili`, kisha kwenye `Pakia faili`:

![builder](assets/25.webp)


- Ukurasa mpya utafunguliwa. Buruta na udondoshe picha ya kampuni yako au programu yako kwenye eneo hilo. Picha hii itaonyeshwa kwenye tovuti ya PlanB Network:

![builder](assets/26.webp)


- Inaweza kuwa nembo au ikoni:

![builder](assets/27.webp)


- Mara tu picha inapopakiwa, thibitisha kuwa kisanduku cha `Jikabidhi moja kwa moja kwenye tawi la 1` kimetiwa alama, kisha ubofye `Fanya mabadiliko`:

![builder](assets/28.webp)


- Kuwa mwangalifu, picha yako lazima iwe ya mraba, lazima iitwe `nembo`, na lazima iwe katika umbizo la `.webp`. Kwa hivyo jina kamili la faili linafaa kuwa: `logo.webp`:

![builder](assets/29.webp)


- Rudi kwenye folda yako ya `asethi` na ubofye faili ya kati ya `.gitkeep`:

![builder](assets/30.webp)


- Mara tu kwenye faili, bofya kwenye vitone vitatu vidogo juu kulia kisha kwenye `Futa faili`:

![builder](assets/31.webp)


- Thibitisha kuwa bado uko kwenye tawi moja linalofanya kazi, kisha ubofye kitufe cha `Fanya mabadiliko`:

![builder](assets/32.webp)


- Ongeza kichwa na maelezo kwa ahadi yako, kisha ubofye `Fanya mabadiliko`:

![builder](assets/33.webp)


- Rudi kwenye folda ya kampuni yako:

![builder](assets/34.webp)


- Bonyeza kitufe cha `Ongeza faili`, kisha kwenye `Unda faili mpya`:

![builder](assets/35.webp)


- Unda faili mpya ya YAML kwa kuipa jina kwa kiashirio cha lugha yako asili. Faili hii itatumika kwa maelezo ya mjenzi. Kwa mfano, ikiwa ninataka kuandika maelezo yangu kwa Kiingereza, nitaita faili hii `en.yml`:

![builder](assets/36.webp)


- Jaza faili hii ya YAML kwa kutumia kiolezo hiki:

```yaml
description: |

contributors:
-
```



- Kwa kitufe cha `wachangiaji`, unaweza kuongeza kitambulisho chako cha mchangiaji kwenye PlanB Network ikiwa unayo. Usipofanya hivyo, acha uga huu tupu.
- Kwa kitufe cha `maelezo`, unahitaji tu kuongeza aya fupi inayoelezea kampuni yako au programu yako. Maelezo lazima yawe katika lugha sawa na jina la faili. Huhitaji kutafsiri maelezo haya katika lugha zote zinazotumika kwenye tovuti, kwani timu za PlanB zitafanya hivyo kwa kutumia muundo wao. Kwa mfano, hii ndio faili yako inaweza kuonekana kama:

```yaml
description: |
Founded in 2017, Bitcoin Baguette is a Paris-based association dedicated to organizing Bitcoin meetups and technical workshops. We bring together enthusiasts, experts, and curious minds to explore and discuss the intricacies of Bitcoin technology. Our events provide a platform for knowledge sharing, networking, and fostering a deeper understanding of Bitcoin's inner workings. Join us at Bitcoin Baguette to be a part of Paris's Bitcoin community and stay updated with the latest advancements in the field.

contributors:
-
```

![builder](assets/37.webp)


- Bonyeza kitufe cha `Fanya mabadiliko`:

![builder](assets/38.webp)


- Hakikisha kisanduku cha `Jitolee moja kwa moja kwenye tawi-1` kimetiwa alama, ongeza kichwa, kisha ubofye `Fanya mabadiliko`:

![builder](assets/39.webp)


- Folda ya kampuni yako sasa inapaswa kuonekana kama hii:

![builder](assets/40.webp)


- Ikiwa kila kitu ni cha kuridhika kwako, rudi kwenye mzizi wa Fork yako:

![builder](assets/41.webp)


- Unapaswa kuona ujumbe unaoonyesha kuwa tawi lako limefanyiwa mabadiliko. Bonyeza kitufe cha `Linganisha & vuta ombi`:

![builder](assets/42.webp)


- Ongeza kichwa na maelezo wazi kwa PR yako:

![builder](assets/43.webp)


- Bonyeza kitufe cha `Unda ombi la kuvuta`:

![builder](assets/44.webp)

Hongera! PR yako imeundwa. Msimamizi sasa atakagua na, ikiwa kila kitu kiko sawa, ataunganisha kwenye hazina kuu ya PlanB Network. Unapaswa kuona wasifu wako wa mjenzi ukionekana kwenye tovuti siku chache baadaye.


Hakikisha unafuata maendeleo ya PR yako. Msimamizi anaweza kuacha maoni akiuliza maelezo ya ziada. Maadamu PR yako haijathibitishwa, unaweza kuishauri kwenye kichupo cha `Vuta maombi` kwenye hazina ya PlanB Network GitHub:

![builder](assets/45.webp)

Asante sana kwa mchango wako muhimu! :)