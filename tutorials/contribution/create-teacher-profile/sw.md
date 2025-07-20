---
name: Profesa Plan ₿ Network
description: Je, ninawezaje kuongeza au kurekebisha wasifu wangu wa mwalimu kwenye Plan ₿ Network?
---
![cover](assets/cover.webp)


Ikiwa unapanga kuchangia Plan ₿ Network kwa kuandika mafunzo au kozi mpya, utahitaji wasifu wa mwalimu. Wasifu huu utakuwezesha kupokea mikopo inayofaa kwa maudhui unayochangia kwenye jukwaa.


Kwa wale ambao tayari wamehusika katika kuunda maudhui ya elimu kwenye Plan ₿ Network, labda tayari una wasifu wa mwalimu. Unaweza kuipata kwenye folda ya `/maprofesa` [kwenye hazina yetu ya GitHub](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/professors). Ikiwa wasifu wako tayari upo, tafuta kuingia kwako katika faili ya `professor.yml`.


Ili kufanya mabadiliko kwenye wasifu wako, nenda kwenye sehemu ya "Hariri wasifu wako wa mwalimu" mwishoni mwa mafunzo haya.


## Ongeza mwalimu mpya na programu yetu


Njia rahisi zaidi ya kuunda wasifu wako wa mwalimu kwenye Plan ₿ Network ni kutumia zana iliyojumuishwa ya Python. Hivi ndivyo inavyofanya kazi.


### 1 - Sanidi mazingira ya eneo lako


Ni lazima uwe na Fork yako mwenyewe kutoka [Plan ₿ Network hazina kwenye GitHub](https://github.com/PlanB-Network/Bitcoin-educational-content).


Sawazisha tawi kuu (`dev`) la Fork yako na hazina ya chanzo.


Sasisha mshirika wako wa karibu.


```bash
# Cloner votre fork (si ce n'est pas déjà fait)
git clone https://github.com/<username>/bitcoin-educational-content.git
cd bitcoin-educational-content
# Ajouter le dépôt source en tant que remote upstream
git remote add upstream https://github.com/PlanB-Network/bitcoin-educational-content.git
# Récupérer les dernières modifications depuis le dépôt source
git fetch upstream
# Se positionner sur la branche principale 'dev'
git checkout dev
# Fusionner les modifications de la branche 'dev' du dépôt source dans votre fork
git merge upstream/dev
# Pousser les mises à jour vers votre fork sur GitHub
git push origin dev
```


### 2 - Unda tawi jipya


Hakikisha uko kwenye tawi la `dev`. Unda tawi jipya kwa jina la maelezo (k.m. `add-professor-loic-morel`).


Chapisha tawi hili kwenye Fork yako mtandaoni.


```bash
# Assurez-vous d’être sur la branche 'dev'
git checkout dev
# Créez une nouvelle branche avec un nom descriptif
git checkout -b add-professor-loic-morel
# Publiez cette branche sur votre fork en ligne
git push -u origin add-professor-loic-morel
```


### 3 - Unda wasifu wako wa mwalimu


Nenda kwenye folda ya `scripts/tutorial-related/data-creator/` kwenye clone yako ya karibu. Hakikisha umeweka utegemezi wote unaohitajika kwa programu, baada ya kusakinisha kwanza Python :


```bash
pip install -r requirements.txt
```


Kisha uzindua programu na amri:


```bash
python3 main.py
```


Ukiwa kwenye ukurasa wa nyumbani, ingiza njia ya ndani ya hifadhi yako, lugha unayoandika na kitambulisho chako cha GitHub. Ikiwa unaunda wasifu huu kwa ajili ya mtu mwingine na tayari una wasifu wa Profesa, weka kitambulisho chako katika sehemu ya "*Kitambulisho cha Profesa wa PBN*". Ikiwa unaunda wasifu wako mwenyewe, bado hutakuwa na kitambulisho cha Profesa, kwa kuwa uko katika harakati za kuunda, kwa hivyo acha sehemu hii wazi.


Kisha bonyeza kitufe cha "*Profesa Mpya*".


![Image](assets/fr/01.webp)


Jaza maelezo yanayohitajika (tafadhali kumbuka kuwa maelezo haya yote yatakuwa hadharani kwenye jukwaa letu na pia kwenye GitHub) :




- Jina la faili yako ya mwalimu (tumia jina lako la kwanza na la mwisho au jina bandia, kwa herufi ndogo);
- Jina lako au lakabu;
- Tovuti yako na wasifu X (hiari);
- Umeme Address kupokea michango kutoka kwa wasomaji (hiari);
- Chagua vitambulisho 2 au 3 kutoka kwenye orodha;
- Bofya kwenye "*Chagua Picha*" ili kuchagua picha ya wasifu kutoka kwa folda zako za karibu (jina na umbizo lolote linaweza kutumika kwa picha hiyo, na programu itairekebisha kiotomatiki. Hakikisha tu kwamba picha ni ya mraba);
- Andika maelezo mafupi ya wasifu wako.


Maliza uundaji kwa kubofya "*Unda Profesa*". Hii itaweka kiotomatiki generate faili zote zinazohitajika kwa wasifu wako.


![Image](assets/fr/02.webp)


Hifadhi mabadiliko yako ndani ya nchi kwa kuunda ahadi na ujumbe wa ufafanuzi. Sukuma mabadiliko kwenye Fork GitHub yako.


```bash
# Créez un commit avec un message descriptif
git commit -m "*new professor Loïc Morel*"
# Poussez vos modifications sur votre fork
git push origin add-professor-loic-morel
```


Mara baada ya kumaliza, unda Ombi la Kuvuta (PR) kwenye GitHub ili kupendekeza ujumuishaji wa marekebisho yako. Ongeza kichwa na maelezo mafupi kwa PR.


### 4 - Kusahihisha na kuunganisha


Subiri uthibitisho au maoni kutoka kwa msimamizi. Ikiwa ni lazima, fanya marekebisho na sukuma ahadi mpya.


```bash
# Créez un commit décrivant les corrections apportées
git commit -m "*Corrections suite à la revue du tutoriel green-wallet*"
# Poussez les corrections sur votre fork
git push origin add-professor-loic-morel
```


Mara tu PR imeunganishwa, unaweza kufuta tawi lako linalofanya kazi.


## Rekebisha wasifu wako wa mwalimu


Ikiwa umefahamu matumizi ya Git, rekebisha wasifu wako wa mwalimu kwa kuunda tawi jipya na kuhariri faili husika moja kwa moja kwenye folda yako iliyopo. Mabadiliko yanaweza kufanywa katika faili ya `professor.yml` au katika faili ya alama, kulingana na maelezo ya kusahihishwa. Ukishafanya mabadiliko yako ndani ya nchi, yasukume kwa Fork yako na uwasilishe PR.


Kwa wanaoanza, ninapendekeza kufanya marekebisho moja kwa moja kupitia mtandao wa Interface wa GitHub. Hakikisha una akaunti ya GitHub. Ikiwa hujui jinsi ya kuunda moja, fuata mafunzo haya:


https://planb.network/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c
Nenda kwenye [hakuna ya Plan ₿ Network ya GitHub iliyowekwa kwa data](https://github.com/PlanB-Network/Bitcoin-educational-content/graphs/contributors).


![Image](assets/fr/03.webp)


Bofya kwenye folda ya "*maprofesa*", kisha uende kwenye folda yako ya kibinafsi.


![Image](assets/fr/04.webp)


Ili kubadilisha metadata yako ya wasifu, kama vile Lightning Address, jina au viungo, chagua faili ya "*professor.yml*". Ili kubadilisha maelezo yako, bofya faili ya YAML ya lugha yako (k.m. "*en.yml*" au "*fr.yml*").


Ukirekebisha maelezo yako, kumbuka kuondoa tafsiri zote za kizamani. Kisha unaweza kutunza kutafsiri maelezo yako katika lugha nyingine kwa usaidizi wa LLM, au kuacha tu maelezo katika lugha yako ya asili na kutaja katika Ombi lako la Kuvuta ambayo maelezo yako yanahitaji kutafsiriwa na timu yetu.


![Image](assets/fr/05.webp)


Mara tu kwenye faili unayotaka kurekebisha, bonyeza kwenye ikoni ya penseli.


![Image](assets/fr/06.webp)


Ikiwa tayari huna Fork kutoka hazina ya Plan ₿ Network, GitHub itapendekeza uunde moja. Bonyeza "*Fork hazina hii*".


![Image](assets/fr/07.webp)


Fanya mabadiliko unayotaka kwenye faili. Baada ya kumaliza, bofya "*Fanya mabadiliko*".


![Image](assets/fr/08.webp)


Ingiza ujumbe unaoelezea mabadiliko yako, kisha uchague "*Pendekeza mabadiliko*".


![Image](assets/fr/09.webp)


Muhtasari wa mabadiliko yako utaonyeshwa. Ikiwa ungependa kufanya mabadiliko zaidi kwenye wasifu wako, unaweza kurudi kwenye folda na kufanya ahadi zaidi. Ukimaliza, bofya "*Unda ombi la kuvuta*".


Ombi la Kuvuta ni ombi linalofanywa ili kujumuisha mabadiliko kutoka kwa tawi lako hadi tawi kuu la hazina ya Plan ₿ Network, ikiruhusu ukaguzi na majadiliano ya mabadiliko kabla ya kuunganishwa.


![Image](assets/fr/10.webp)


Hakikisha, katika sehemu ya juu ya Interface, kwamba tawi lako la kazi limeunganishwa na tawi la `dev` la hazina ya Plan ₿ Network (ambalo ndilo tawi kuu).


Weka jina ambalo linatoa muhtasari wa mabadiliko unayotaka kuunganisha na hazina ya chanzo. Ongeza maoni mafupi yanayoelezea mabadiliko haya, kisha ubofye kitufe cha Green "*Unda ombi la kuvuta*" ili kuthibitisha ombi la kuvuta:


![Image](assets/fr/11.webp)


PR yako kisha itaonekana kwenye kichupo cha "*Vuta Ombi*" cha hazina kuu ya Plan ₿ Network. Unachotakiwa kufanya sasa ni kusubiri msimamizi aunganishe urekebishaji wako.


![Image](assets/fr/12.webp)


Ukikumbana na matatizo yoyote ya kiufundi katika kuwasilisha mabadiliko yako, tafadhali usisite kuomba usaidizi kwenye [kikundi chetu cha Telegram kinachojitolea kwa michango](https://t.me/PlanBNetwork_ContentBuilder). Asante sana!