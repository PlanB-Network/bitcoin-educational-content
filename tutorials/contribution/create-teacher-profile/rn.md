---
name: Porofeseri Plan ₿ Network.
description: Nokwongerako canke guhindura gute urutonde rw’umwigisha wanje kuri Plan ₿ Network?
---
![cover](assets/cover.webp)


Niba utegura gutanga umusanzu muri Plan ₿ Network mu kwandika inyigisho canke inyigisho nshasha, uzokenera urutonde rw’umwigisha. Iyi nkuru izotuma uronka amahera akwiye ku bintu utanga kuri iyo nzira.


Namwe mwamaze kwifatanya mu guhingura ibintu vy’inyigisho kuri Plan ₿ Network, birashoboka ko musanzwe mufise urutonde rw’umwigisha. Ushobora kubisanga muri dosiye `/abaporofeseri` [ku bubiko bwacu bwa GitHub](https://github.com/Umugambi-Umurongo/Bitcoin-ibirimwo-ivy’inyigisho/igiti/dev/abaporofeseri). Niba urutonde rwawe rusanzwe ruriho, rondera inzira yawe yo kwinjira muri dosiye `professor.yml`.


Kugira ngo uhindure urutonde rwawe, genda ku gice kivuga ngo "Guhindura urutonde rw'umwigisha wawe" kiri ku mpera y'iyi nyigisho.


## Yongerako umwigisha mushasha ukoresheje porogaramu yacu


Uburyo bworoshe bwo gukora urutonde rw’umwigisha wawe kuri Plan ₿ Network ni ugukoresha igikoresho cacu ca Python gihuriweko. Ehe ingene bigenda.


### 1 - Gutunganya ibidukikije vyawe


Utegerezwa kuba ufise Fork yawe bwite iva [ububiko bwa Plan ₿ Network kuri GitHub]


Guhuza ishami ry'ingenzi (`dev`) rya Fork yawe n'ububiko bw'inkomoko.


Vugurura clone yawe yo mu karere.


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


### 2 - Gukora ishami rishasha


Raba neza ko uri kw'ishami rya `dev`. Rema ishami rishasha rifise izina ridondora (nk'akarorero `wongere-umwigisha-loic-morel`).


Sohora iri shami kuri Fork yawe kuri Internet.


```bash
# Assurez-vous d’être sur la branche 'dev'
git checkout dev
# Créez une nouvelle branche avec un nom descriptif
git checkout -b add-professor-loic-morel
# Publiez cette branche sur votre fork en ligne
git push -u origin add-professor-loic-morel
```


### 3 - Rema urutonde rw'umwigisha wawe


Genda kuri `inyandiko/ibijanye n'inyigisho/umuremyi w'amakuru/` dosiye kuri clone yawe yo mu karere. Raba neza ko washizeho ibikenewe vyose kuri porogaramu, umaze gushiramwo Python:


```bash
pip install -r requirements.txt
```


Hanyuma utangure porogarama ukoresheje itegeko:


```bash
python3 main.py
```


Igihe ugeze kuri paji y'intango, shiramwo inzira y'aho uba ku bubiko bwawe, ururimi wandikamwo n'Indangamuntu yawe ya GitHub. Niba uriko urakorera uwundi muntu iyi profile kandi usanzwe ufise profile ya Professeur, shiramwo ID yawe mu kibanza ca "*PBN Professor's ID*". Niba uriko urakora urutonde rwawe, ntuzoba ufise indangamuntu ya Professeur, kuko uriko urayikora, rero reka iki kibanza kibe ubusa.


Hanyuma ukande kuri buto ya "*Professeur mushasha*".


![Image](assets/fr/01.webp)


Uzuza amakuru asabwa (umenye ko aya makuru yose azomenyekana ku rubuga rwacu no kuri GitHub):




- Izina rya dosiye yawe y’umwigisha (koresha izina ryawe rya mbere n’iry’umuryango canke izina ry’uruyeri, mu nyuguti ntoya) ;
- Izina ryawe canke izina ry'akataraboneka ;
- Urubuga rwawe n’ivyo ukoresha X (ntibikenewe) ;
- A Lightning Address yo kwakira intererano zivuye ku basomyi (ntibikenewe) ;
- Hitamwo 2 canke 3 mu rutonde;
- Fyonda kuri "*Hitamwo ishusho*" kugira uhitemwo ishusho y'umwirondoro mu madosiye yawe yo mu karere (izina ryose n'uburyo bwose bishobora gukoreshwa ku ishusho, kandi porogarama izoyihindura ubwayo. Urabe neza ko ishusho ari inzira y'inzira);
- Wandike insobanuro ngufi y’ivy’ubuzima bwawe.


Sozera kurema ukanda kuri "*Rema Porofeseri*". Ivyo bizotuma generate amadosiye yose asabwa ku rutonde rwawe.


![Image](assets/fr/02.webp)


Bika amahinduka yawe mu karere mu gukora isezerano rifise ubutumwa busobanura. Sunika amahinduka kuri Fork GitHub yawe.


```bash
# Créez un commit avec un message descriptif
git commit -m "*new professor Loïc Morel*"
# Poussez vos modifications sur votre fork
git push origin add-professor-loic-morel
```


Uhejeje, rema Pull Request (PR) kuri GitHub kugira ngo usabe ugushiramwo ivyo wahinduye. Wongereko umutwe n’insobanuro ngufi kuri PR.


### 4 - Gukosora no gufatanya


Rindira kwemezwa canke inyishu iva ku muyobozi. Niba ari ngombwa, nukosore kandi usunike amasezerano mashasha.


```bash
# Créez un commit décrivant les corrections apportées
git commit -m "*Corrections suite à la revue du tutoriel green-wallet*"
# Poussez les corrections sur votre fork
git push origin add-professor-loic-morel
```


Iyo PR imaze guhurizwa hamwe, urashobora gukuraho ishami ryawe rikora.


## Guhindura umwirondoro w'umwigisha wawe


Niba waramenye neza gukoresha Git, hindura urutonde rw'umwigisha wawe mu kurema ishami rishasha no guhindura dosiye ibereye mu dosiye yawe isanzwe. Impinduka zishobora gukorwa haba muri dosiye `professor.yml` canke muri dosiye y'ikimenyetso, bivanye n'amakuru azokosorwa. Umaze guhindura ivyo mu karere, ubisunikire kuri Fork yawe maze ushiremwo PR.


Ku batangura, ndabagira inama yo guhindura biciye ku rubuga rwa GitHub rwa Interface. Raba neza ko ufise konti ya GitHub. Niba utazi uko woyikora, kurikiza iyi nyigisho:


https://planb.network/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c
Genda kuri [ububiko bwa Plan ₿ Network bwa GitHub bwihariye amakuru](https://github.com/Umugambi-w'Umugambi/Bitcoin-ibirimwo-ivy'inyigisho/ibishushanyo/abatanga).


![Image](assets/fr/03.webp)


Fyonda kuri dosiye "*professeurs*", hanyuma ugende kuri dosiye yawe bwite.


![Image](assets/fr/04.webp)


Kugira ngo uhindure amakuru yawe, nka Lightning Address, izina canke amahuza, hitamwo dosiye "*professor.yml*". Kugira ngo uhindure insobanuro yawe, kanda kuri dosiye ya YAML y'ururimi rwawe (nk'akarorero "*en.yml*" canke "*fr.yml*").


Niwahindura insobanuro yawe, wibuke gukuraho ubuhinduzi bwose bwa kera. Hanyuma ushobora kwitwararika guhindura insobanuro yawe mu zindi ndimi ufashijwe na LLM, canke ugasiga insobanuro gusa mu rurimi rwawe kavukire maze ukavuga mu Pull Request yawe ko insobanuro yawe isaba guhindurwa n’umugwi wacu.


![Image](assets/fr/05.webp)


Igihe umaze gushika kuri dosiye wipfuza guhindura, ukande ku kimenyetso c’ikaramu.


![Image](assets/fr/06.webp)


Niba udasanzwe ufise Fork ivuye mu bubiko bwa Plan ₿ Network, GitHub izogusaba ko woyihingura. Fyonda kuri "*Fork ubu bubiko*".


![Image](assets/fr/07.webp)


Guhindura ivyo wipfuza muri dosiye. Niwaheza, ukande kuri "*Guhindura*".


![Image](assets/fr/08.webp)


Injira ubutumwa budondora ihinduka ryawe, hanyuma uhitemwo "*Gusaba ihinduka*".


![Image](assets/fr/09.webp)


Incamake y'ivyo wahinduye izogaragara. Niba wipfuza guhindura ibindi ku rubuga rwawe, urashobora gusubira mu madosiye maze ugakora ibindi bikorwa. Niwaheza, ukande kuri "*Rema ubusabe bwo gukurura*".


Igisabwa co gukura ni igisabwa gikorwa co gushiramwo amahinduka ava mw’ishami ryawe mw’ishami ry’ingenzi ry’ububiko bwa Plan ₿ Network, bikaba vyemerera gusubiramwo no kuganira ku mahinduka imbere y’uko ahurizwa hamwe.


![Image](assets/fr/10.webp)


Raba neza, hejuru ya Interface, ko ishami ryawe rikora ryifatanijwe n'ishami rya `dev` ry'ububiko bwa Plan ₿ Network (ari ryo shami nyamukuru).


Injira umutwe uvuga muri make amahinduka wipfuza gufatanya n'ububiko bw'inkomoko. Yongerako amajambo make adondora ayo mahinduka, hanyuma ukande kuri buto ya Green "*Rema ubusabe bwo gukurura*" kugira ngo wemeze ubusabe bwo gukurura:


![Image](assets/fr/11.webp)


PR yawe izoca iboneka mu gice ca "*Pull Request*" c'ububiko nyamukuru bwa Plan ₿ Network. Ico ubwirizwa gukora ubu ni ukurindira ko umuyobozi afatanya ivyo wahinduye.


![Image](assets/fr/12.webp)


Niwahura n’ingorane z’ubuhinga mu gutanga ihinduka ryawe, ntukekeranye gusaba imfashanyo kuri [umugwi wacu wa Telegramu wihariye ku ntererano](https://t.me/PlanBNetwork_ContentBuilder). Murakoze cane!