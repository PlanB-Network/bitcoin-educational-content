---
name: Inaongeza Podcast kwenye PlanB Network
description: Jinsi ya kuongeza podikasti mpya kwenye Mtandao wa PlanB?
---
![podcast](assets/cover.webp)


Dhamira ya PlanB ni kutoa nyenzo za elimu za kiwango cha juu kwenye Bitcoin katika lugha nyingi iwezekanavyo. Maudhui yote yaliyochapishwa kwenye tovuti ni chanzo huria na yamepangishwa kwenye GitHub, kuruhusu mtu yeyote kushiriki katika kuimarisha jukwaa.


Je, unatazamia kuongeza podikasti ya Bitcoin kwenye tovuti ya PlanB Network na kuongeza mwonekano wa kipindi chako, lakini hujui jinsi gani? Mafunzo haya ni kwa ajili yako!

![podcast](assets/01.webp)


- Kwanza, unahitaji kuwa na akaunti ya GitHub. Ikiwa hujui jinsi ya kuunda moja, tumefanya mafunzo ya kina ili kukuongoza.


https://planb.network/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c



- Nenda kwenye [hakuna ya GitHub ya PlanB iliyowekwa kwa data](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/resources/podcasts) katika sehemu ya `rasilimali/podcast/`:

![podcast](assets/02.webp)


- Bofya sehemu ya juu kulia kwenye kitufe cha `Ongeza faili`, kisha kwenye `Unda faili mpya`:

![podcast](assets/03.webp)


- Ikiwa hujawahi kuchangia maudhui ya PlanB Network hapo awali, utahitaji kuunda Fork yako ya hazina asili. Kuunda hazina inamaanisha kuunda nakala ya hazina hiyo kwenye akaunti yako ya GitHub, kukuruhusu kufanya kazi kwenye mradi bila kuathiri hazina asili. Bonyeza kitufe cha `Fork hazina hii`:

![podcast](assets/04.webp)


- Kisha utafika kwenye ukurasa wa uhariri wa GitHub:

![podcast](assets/05.webp)


- Unda folda ya podcast yako. Ili kufanya hivyo, katika kisanduku cha `Ipe jina faili yako...`, andika jina la podikasti yako kwa herufi ndogo na vistari badala ya nafasi. Kwa mfano, ikiwa kipindi chako kinaitwa "Super Podcast Bitcoin", unapaswa kuandika `super-podcast-Bitcoin`:

![podcast](assets/06.webp)


- Ili kuhalalisha uundaji wa folda, ongeza tu kufyeka baada ya jina la podikasti yako kwenye kisanduku kimoja, kwa mfano: `super-podcast-Bitcoin/`. Kuongeza slash moja kwa moja huunda folda badala ya faili:

![podcast](assets/07.webp)


- Katika folda hii, utaunda faili ya kwanza ya YAML inayoitwa `podcast.yml`:

![podcast](assets/08.webp)


- Jaza faili hii maelezo kuhusu podikasti yako kwa kutumia kiolezo hiki:


```yaml
name:
host:
language:
links:
podcast:
twitter:
website:
description: |

tags:
-
-
contributors:
-
```


Hapa kuna maelezo ya kujaza kwa kila sehemu:



- `jina`**: Onyesha jina la podikasti yako.
- `mwenyeji`**: Orodhesha majina au majina bandia ya spika au mwenyeji wa podikasti. Kila jina linapaswa kutengwa kwa koma.
- `lugha`**: Onyesha msimbo wa lugha ya lugha inayozungumzwa katika podikasti yako. Kwa mfano, kwa Kiingereza, kumbuka `en`, kwa Kiitaliano `it`...



- `viungo`**: Toa viungo kwa maudhui yako. Una chaguzi mbili:
 - `podcast`: kiungo cha podikasti yako,
 - `twitter`: kiungo cha wasifu wa Twitter wa podikasti au shirika linaloitayarisha,
 - `tovuti`: kiungo cha tovuti ya podikasti au shirika linaloitayarisha.



- `maelezo`**: Ongeza aya fupi inayoelezea podikasti yako. Maelezo lazima yawe katika lugha sawa na ilivyoonyeshwa katika sehemu ya `lugha:`.



- `tagi`**: Ongeza lebo mbili zinazohusiana na podikasti yako. Mifano:
    - `Bitcoin`
    - `teknolojia`
    - `uchumi`
    - `elimu`...



- `wachangiaji`**: Taja kitambulisho chako cha mchangiaji ikiwa unacho.


Kwa mfano, faili yako ya YAML inaweza kuonekana kama hii:


```yaml
name: Super Podcast Bitcoin
host: Rogzy, JohnOnChain, Lounes, Fanis, Ajlex, Guillaume, Pantamis, Sosthene, Loic
language: en
links:
podcast: https://podcasts.apple.com/us/podcast/decouvrebitcoin-replay/id1693844092
twitter: https://twitter.com/decouvrebitcoin
website: https://decouvrebitcoin.fr
description: |
Super Podcast Bitcoin is a technical LIVE session held once a week on Twitter to delve deep into the Bitcoin protocol, layer two solutions, and all things that blow minds. Our hosts Lounes, Pantamis, Loïc, and Sosthene will answer your questions and offer the most technical show on Bitcoin in the world.

tags:
- bitcoin
- technology
contributors:
- rabbit-hole
```


![podcast](assets/09.webp)



- Mara tu unapomaliza kufanya mabadiliko kwenye faili hii, yahifadhi kwa kubofya kitufe cha `Fanya mabadiliko...`:

![podcast](assets/10.webp)


- Ongeza kichwa cha mabadiliko yako, pamoja na maelezo mafupi:

![podcast](assets/11.webp)


- Bofya kwenye kitufe cha Green `Pendekeza mabadiliko`:

![podcast](assets/12.webp)


- Kisha utafika kwenye ukurasa ambao unatoa muhtasari wa mabadiliko yako yote:

![podcast](assets/13.webp)


- Bofya kwenye picha yako ya wasifu ya GitHub juu kulia, kisha kwenye `Hazina Zako`:

![podcast](assets/14.webp)


- Chagua Fork yako ya hazina ya Mtandao wa PlanB:

![podcast](assets/15.webp)


- Unapaswa kuona arifa juu ya dirisha na tawi lako jipya. Pengine inaitwa `kiraka-1`. Bonyeza juu yake:

![podcast](assets/16.webp)


- Sasa uko kwenye tawi lako la kufanya kazi:

![podcast](assets/17.webp)


- Rudi kwenye folda ya `rasilimali/podcast/` na uchague folda ya podikasti ambayo umeunda hivi punde katika ahadi iliyotangulia: ![podcast](assets/18.webp)
- Katika folda yako ya podcast, bofya kitufe cha `Ongeza faili`, kisha kwenye `Unda faili mpya`:

![podcast](assets/19.webp)


- Taja folda hii mpya `mali` na uthibitishe uundaji wake kwa kuongeza kufyeka `/` mwishoni:

![podcast](assets/20.webp)


- Katika folda hii ya `asethi`, unda faili inayoitwa `.gitkeep`:

![podcast](assets/21.webp)


- Bonyeza kitufe cha `Fanya mabadiliko...`:

![podcast](assets/22.webp)


- Acha kichwa cha ahadi kama chaguo-msingi, na uhakikishe kuwa kisanduku cha `Weka moja kwa moja kwenye tawi-1` kimetiwa alama, kisha ubofye `Fanya mabadiliko`:

![podcast](assets/23.webp)


- Rudi kwenye folda ya `asethi`:

![podcast](assets/24.webp)


- Bonyeza kitufe cha `Ongeza faili`, kisha kwenye `Pakia faili`:

![podcast](assets/25.webp)


- Ukurasa mpya utafunguliwa. Buruta na udondoshe nembo yako ya podikasti kwenye eneo. Picha hii itaonyeshwa kwenye tovuti ya PlanB Network:

![podcast](assets/26.webp)


- Kuwa mwangalifu, picha lazima iwe ya mraba, ili kutoshea vyema tovuti yetu:

![podcast](assets/27.webp)


- Mara tu picha inapopakiwa, thibitisha kuwa kisanduku cha `Jikabidhi moja kwa moja kwenye tawi la 1` kimetiwa alama, kisha ubofye `Fanya mabadiliko`:

![podcast](assets/28.webp)


- Kuwa mwangalifu, picha yako lazima iitwe `nembo` na lazima iwe katika umbizo la `.webp`. Kwa hivyo jina kamili la faili linafaa kuwa: `logo.webp`:

![podcast](assets/29.webp)


- Rudi kwenye folda yako ya `asethi` na ubofye faili ya kati `.gitkeep`:

![podcast](assets/30.webp)


- Mara tu kwenye faili, bofya kwenye vitone vitatu vidogo juu kulia kisha kwenye `Futa faili`:

![podcast](assets/31.webp)


- Thibitisha kuwa bado uko kwenye tawi moja linalofanya kazi, kisha ubofye kitufe cha `Fanya mabadiliko`:

![podcast](assets/32.webp)


- Ongeza kichwa na maelezo kwenye ahadi yako, kisha ubofye `Fanya mabadiliko`:

![podcast](assets/33.webp)


- Rudi kwenye mzizi wa hazina yako:

![podcast](assets/34.webp)


- Unapaswa kuona ujumbe unaoonyesha kuwa tawi lako limefanyiwa mabadiliko. Bonyeza kitufe cha `Linganisha & vuta ombi`:

![podcast](assets/35.webp)


- Ongeza kichwa na maelezo wazi kwa PR yako:

![podcast](assets/36.webp)


- Bonyeza kitufe cha `Unda ombi la kuvuta`:

![podcast](assets/37.webp)

Hongera! PR yako imeundwa. Msimamizi sasa atakagua na, ikiwa kila kitu kiko sawa, aiunganishe kwenye hazina kuu ya PlanB Network. Unapaswa kuona podikasti yako ikitokea kwenye tovuti siku chache baadaye.


Tafadhali hakikisha unafuata maendeleo ya PR yako. Msimamizi anaweza kuacha maoni akiuliza maelezo ya ziada. Maadamu PR yako haijathibitishwa, unaweza kuiona kwenye kichupo cha `Vuta maombi` kwenye hazina ya PlanB Network GitHub:

![podcast](assets/38.webp)

Asante sana kwa mchango wako muhimu! :)