---
name: Yongerako ikintu ku rubuga rwa PlanB
description: Ni gute nogira iciyumviro co kwongerako ikintu gishasha ku rubuga rwa PlanB?
---
![event](assets/cover.webp)


Intumbero ya PlanB ni ugutanga ibikoresho vy’inyigisho vyo ku rwego rwo hejuru ku Bitcoin mu ndimi nyinshi zishoboka. Ibintu vyose bisohoka kuri uru rubuga ni ivy’inkomoko yuguruye kandi bishirwa kuri GitHub, bikaba biha umuntu wese akaryo ko gutanga umusanzu mu gutunganya urubuga.


Niba ushaka kwongerako inama ya Bitcoin ku rubuga rwa PlanB Network no kwongera ukugaragara kw’umusi mukuru wawe, ariko ntuzi ingene? Iyi nyigisho ni iyawe!

![event](assets/01.webp)


- Ubwa mbere, ukeneye kugira konti kuri GitHub. Niba utazi uko wokora konti, twakoze inyigisho ido n’ido kugira ngo ikuyobore.


https://planb.network/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c



- Genda kuri [ububiko bwa GitHub bwa PlanB bwihariye amakuru](https://github.com/PlanB-Ihuriro/Bitcoin-ibirimwo-ivy'inyigisho/igiti/iterambere/ibikoresho/inama) mu gice ca `ibikoresho/inama/`:

![event](assets/02.webp)


- Fyonda hejuru iburyo kuri buto `Ongera dosiye`, hanyuma kuri `Rema dosiye nshasha`:

![event](assets/03.webp)


- Niba utigeze utanga umusanzu ku birimwo PlanB Network mbere, uzokenera gukora Fork yawe y’ububiko bw’intango. Guca ububiko bisigura gukora kopi y'ubwo bubiko kuri konti yawe ya GitHub, bikagufasha gukora ku mugambi ataco uhinduye ku bubiko bw'intango. Fyonda kuri buto ya `Fork ubu bubiko`:

![event](assets/04.webp)


- Uzoca ushika kuri paji yo guhindura ya GitHub:

![event](assets/05.webp)


- Rema dosiye y'inama yawe. Kugira ngo ubikore, mu gasandugu ka `Izina rya dosiye yawe...`, wandike izina ry'inama yawe mu nyuguti ntoyi ukoresheje uturongo aho kwandika uturongo. Nk'akarorero, nimba inama yawe yitwa "Inama ya Paris Bitcoin", ukwiye kwandika `inama ya Paris-Bitcoin`. Wongereko kandi umwaka w'inama yawe, nk'akarorero: `paris-Bitcoin-inama-2024`:

![event](assets/06.webp)


- Kugira ngo wemeze ko dosiye yaremwe, ushire akarongo inyuma y'izina ryawe mu gasandugu kamwe, nk'akarorero: `paris-Bitcoin-inama-2024/`. Kwongerako akarongo bihita bikora ububiko aho kuba dosiye:

![event](assets/07.webp)


- Muri iyi dosiye, uzokora dosiye ya mbere ya YAML yitwa `events.yml`:

![event](assets/08.webp)


- Uzuza iyi dosiye amakuru yerekeye inama yawe ukoresheje iyi nkuru:


```yaml
start_date:
end_date:
address_line_1:
address_line_2:
address_line_3:
name:
project:
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


Akarorero, dosiye yawe ya YAML yoshobora gusa n'iyi:


```yaml
start_date: 2024-08-15
end_date: 2024-08-18
address_line_1: Paris, France
address_line_2:
address_line_3:
name: Paris Bitcoin Conference 2024
project: Paris Bitcoin Conference
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

Niba utararonka ikimenyetso ca "*project*" c'ishirahamwe ryawe, urashobora kugishiramwo ukurikije iyi yindi nyigisho.


https://planb.network/tutorials/contribution/resource/add-builder-b5834c46-6dcc-4064-8d68-1ef529991d3d




- Uhejeje guhindura iyi dosiye, ubike ukanda kuri buto ya `Commit changes...`:

![event](assets/10.webp)


- Wongereko umutwe w'ivyo wahinduye, hamwe n'insobanuro ngufi:

![event](assets/11.webp)


- Fyonda kuri buto ya Green `Gutanga amahinduka`:

![event](assets/12.webp)


- Uzoca ushika kuri paji ivuga mu ncamake ivyo wahinduye vyose:

![event](assets/13.webp)


- Fyonda ku ifoto yawe y'umwirondoro wa GitHub hejuru iburyo, hanyuma kuri `Ububiko bwawe`:

![event](assets/14.webp)


- Hitamwo Fork yawe y'ububiko bw'urubuga rwa PlanB:

![event](assets/15.webp)


- Ushobora kubona itangazo hejuru y’idirisha ririho ishami ryawe rishasha. Birashoboka ko yitwa `igipande-1`. Fyondako:

![event](assets/16.webp)


- Ubu uri kw'ishami ryawe ry'akazi:

![event](assets/17.webp)


- Subira kuri dosiye ya `ibikoresho/inama/` maze uhitemwo dosiye y'inama yawe uherutse kurema mu bikorwa vya kera:

![event](assets/18.webp)


- Mu bubiko bw'inama yawe, kanda kuri buto ya `Kwongerako dosiye`, hanyuma kuri `Rema dosiye nshasha`:

![event](assets/19.webp)


- Izina ry'iyi dosiye nshasha `itunga` maze wemeze ko yaremwe mu gushiramwo akarongo `/` ku mpera:

![event](assets/20.webp)


- Muri iyi `itunga` dosiye, rema dosiye yitwa `.gitkeep`:

![event](assets/21.webp)


- Fyonda kuri buto ya `Guhindura...`:

![event](assets/22.webp)


- Siga umutwe w'isezerano nk'uko mburabuzi, maze urabe neza ko `Isezerano ry'ishami rya patch-1` akazu kagenzuwe, hanyuma ukande kuri `Isezerano ry'amahinduka`:

![event](assets/23.webp)


- Subira kuri dosiye ya `itunga`:

![event](assets/24.webp)


- Fyonda kuri buto ya `Kwongerako dosiye`, hanyuma kuri `Shirako dosiye`: ![ivyabaye](itunga/25.webp)
- Paje nshasha izofunguka. Kurura ushire ishusho iserukira inama yawe kandi izogaragara ku rubuga rwa PlanB Network:

![event](assets/26.webp)


- Bishobora kuba ikimenyetso, akashusho gato, canke mbere igicapo:

![event](assets/27.webp)


- Ishusho imaze gushirwako, suzuma ko akazu ka `Kwiyemeza ku ishami rya patch-1` kashizweko akamenyetso, hanyuma ukande kuri `Kwiyemeza amahinduka`:

![event](assets/28.webp)


- Urabe maso, ishusho yawe itegerezwa kwitwa `thumbnail` kandi itegerezwa kuba iri mu buryo bwa `.webp`. Izina rya dosiye yuzuye rero rikwiye kuba: `igishushanyo gito.webp`:

![event](assets/29.webp)


- Subira muri dosiye yawe `itunga` maze ukande kuri dosiye y'umuhuza `.gitkeep`:

![event](assets/30.webp)


- Uhejeje kuri dosiye, ukande ku tudodo dutoduto 3 turi hejuru iburyo hanyuma kuri `Sukura dosiye`:

![event](assets/31.webp)


- Genzura ko ukiri ku ishami rimwe rikora, hanyuma ukande kuri buto ya `Guhindura`:

![event](assets/32.webp)


- Wongereko umutwe n'insobanuro ku vyo wiyemeje, hanyuma ukande kuri `Impinduka zo kwemeza`:

![event](assets/33.webp)


- Subira ku muzi w'ububiko bwawe:

![event](assets/34.webp)


- Ukwiye kubona ubutumwa bwerekana ko ishami ryawe ryahindutse. Fyonda kuri buto ya `Gereranya & gukuraho ibisabwa`:

![event](assets/35.webp)


- Wongereko umutwe utomoye n'insobanuro kuri PR yawe:

![event](assets/36.webp)


- Fyonda kuri buto ya `Rema ubusabe bwo gukurura`:

![event](assets/37.webp)

Urakoze cane! PR yawe yararemwe neza. Ubu umuyobozi azobisuzuma, nimba vyose biri ku rutonde, abishire mu bubiko nyamukuru bwa PlanB Network. Ushobora kubona umusi mukuru wawe uboneka ku rubuga haciye imisi mikeyi.


Raba neza ko ukurikirana ingene PR yawe itera imbere. Umuyobozi ashobora gusiga amajambo asaba ibindi bisobanuro. Igihe cose PR yawe itaremejwe, ushobora kuyibona mu `Ibisabwa vyo gukura` ku bubiko bwa GitHub bw'urubuga rwa PlanB:

![event](assets/38.webp)

Murakoze cane ku ntererano y’agaciro mwatanze! :)