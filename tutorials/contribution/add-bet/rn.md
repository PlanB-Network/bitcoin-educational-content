---
name: Kwongerako ibikoresho vy'inyigisho
description: Ni gute twokwongerako ibikoresho bishasha vy’inyigisho kuri Plan ₿ Academy?
---
![event](assets/cover.webp)


Intumbero ya PlanB ni ugutanga ibikoresho vy’inyigisho bihambaye ku bijanye na Bitcoin, mu ndimi nyinshi zishoboka. Ibintu vyose bisohoka kuri uru rubuga ni open-source kandi bishirwa kuri GitHub, ivyo bikaba bituma umuntu wese agira uruhara mu gutunganya urubuga.


Uretse inyigisho n’amahugurwa, Plan ₿ Academy kandi itanga ububiko bunini bw’ibintu vy’inyigisho bitandukanye kuri Bitcoin, bishobora gushikirwa na bose, [mu gice ca "BET" (_Igikoresho c’inyigisho ca Bitcoin_)](https://planb.academy/resources/bet). Iyi database irimwo amafoto y’inyigisho, ama memes, amafoto y’ivy’iterabwoba, ibishushanyo vy’ubuhinga, ibimenyetso, n’ibindi bikoresho vy’abakoresha. Intumbero y’iyi nzira ni ugushigikira abantu ku giti cabo n’imiryango yigisha Bitcoin kw’isi yose mu kubaha ibikoresho bikenewe vyo kubona.


Woba ushaka kugira uruhara mu gutunganya uru rubuga, ariko ntuzi ingene wobikora? Iyi nyigisho ni iyawe!


*Ni ngombwa ko ibirimwo vyose vyinjijwe kuri uru rubuga bitagira uburenganzira canke vyubahiriza uruhusha rwa dosiye y’inkomoko. Vyongeye, amashusho yose yasohowe kuri Plan ₿ Academy araboneka hakurikijwe uruhusha [CC-BY-SA](https://creativecommons.org/licenses/by-sa/4.0/).*

![event](assets/01.webp)


- Ubwa mbere, ukeneye kugira konti kuri GitHub. Niba utazi uko wokora konti, twakoze inyigisho ido n’ido kugira ngo ikuyobore.


https://planb.academy/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c



- Genda kuri [ububiko bwa GitHub bwa PlanB bwihariye ku makuru](https://github.com/Urubuga rwa PlanB/ibirimwo-ivy’inyigisho/igiti/iterambere/ibikoresho/bet) mu gice ca `ibikoresho/bet/`:

![event](assets/02.webp)


- Fyonda hejuru iburyo kuri buto `Ongera dosiye`, hanyuma kuri `Rema dosiye nshasha`:

![event](assets/03.webp)


- Niba utigeze utanga umusanzu ku birimwo Plan ₿ Academy mbere, uzokenera gukora fork yawe y’ububiko bw’intango. Forking ububiko bisigura gukora kopi y'ubwo bubiko kuri konti yawe bwite ya GitHub, ivyo bikaba bigufasha gukora ku mugambi ataco uhinduye ku bubiko bw'intango. Fyonda kuri buto ya `Fork ubu bubiko`:

![event](assets/04.webp)


- Uzoca ushika kuri paji yo guhindura ya GitHub:

![event](assets/05.webp)


- Rema ububiko bw'ibirimwo. Kugira ngo ubikore, mu gasandugu ka `Izina rya dosiye yawe...`, wandike izina ry'ibirimwo mu nyuguti ntoyi ukoresheje uturongo aho kwandika uturongo. Mu karorero kanje, reka tuvuge ko nshaka kwongerako igishushanyo ca PDF c’urutonde rw’amajambo 2048 BIP39. Rero, nzohamagara dosiye yanje `bip39-urutonde rw'amajambo`: ![ivyabaye](itunga/06.webp)
- Kugira ngo wemeze ko dosiye yaremwe, wongereko gusa akarongo inyuma y'izina mu gasandugu kamwe, nk'akarorero: `bip39-wordlist/`. Kwongerako akarongo bihita bikora ububiko aho kuba dosiye:

![event](assets/07.webp)


- Muri iyi dosiye, uzokora dosiye ya mbere ya YAML yitwa `bet.yml`:

![event](assets/08.webp)


- Uzuza iyi dosiye amakuru ajanye n'ibirimwo ukoresheje iyi nkuru:


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


Akira ibisobanuro vyo kwuzuza kuri buri kibanza:



- `umugambi`**: Erekana ikimenyetso c'ishirahamwe ryawe kuri Plan ₿ Academy. Niba utararonka ikimenyetso c'"umugambi" c'ishirahamwe ryawe, urashobora kugikora ukurikije iyi nyigisho.


https://planb.academy/tutorials/contribution/resource/add-builder-b5834c46-6dcc-4064-8d68-1ef529991d3d

Nimba udafise, urashobora gusa gukoresha izina ryawe, izina ryawe ry’uruyeri canke izina ry’ishirahamwe ryawe utakoze urutonde rw’umugambi.



- `ubwoko`**: Hitamwo uburyo bw'ibirimwo muri ibi bibiri bikurikira:
 - `Ibirimwo vy'inyigisho` ku birimwo vy'inyigisho.
 - `Ibirimwo bigaragara` ku bindi birimwo bitandukanye.



- `amahuza`**: Tanga amahuza ku birimwo. Ufise uburyo bubiri:
 - Niwahitamwo kwakira ibirimwo vyawe ku GitHub ya PlanB, uzokenera kwongerako amahuza kuri iyi dosiye mu ntambwe zikurikira.
 - Niba ibirimwo vyacu bishizwe ahandi, nk'uko biri ku rubuga rwawe bwite, werekane amahuza ahuye hano:
     - `download`: Ihuza ryo gukuraho ibirimwo.
     - `view`: Ihuza ryo kuraba ibirimwo (rishobora kuba rimwe n'ihuza ryo gukuraho). Nimba ibirimwo vyawe biri mu ndimi nyinshi, wongereko uruja n’uruza rw’ururimi rumwe rumwe.



- `tags`**: Wongereko ama tags abiri afitaniye isano n'ibirimwo. Ingero:
 - ibikoni
 - ubuhinga
 - ubutunzi
 - inyigisho
 - meme...



- `abaterankunga`**: Vuga ikimenyetso c'umuterankunga wawe nimba ufise.


Akarorero, dosiye yawe ya YAML yoshobora gusa n'iyi:


```yaml
project: Plan ₿ Academy
type: Educational Content
links:
download: https://workspace.planb.network/s/fojeJa7ZbftQTwo
view:
```



- Mu karorero kanje, nzosiga amahuza ubusa ubu, kuko nzokwongerako PDF yanje kuri GitHub:

![event](assets/09.webp)


- Igihe ivyo wahinduye muri iyi dosiye birangiye, ubibike ukanda kuri buto ya `Commit changes...`:

![event](assets/10.webp)


- Wongereko umutwe w'ivyo wahinduye, hamwe n'insobanuro ngufi:

![event](assets/11.webp)


- Fyonda kuri buto y'icatsi kibisi `Gutanga amahinduka`:

![event](assets/12.webp)


- Uzoca ushika kuri paji ivuga mu ncamake ivyo wahinduye vyose:

![event](assets/13.webp)


- Fyonda ku ifoto yawe y'umwirondoro wa GitHub hejuru iburyo, hanyuma kuri `Ububiko bwawe`:

![event](assets/14.webp)


- Hitamwo fork yawe mu bubiko bwa Plan ₿ Academy:

![event](assets/15.webp)


- Ushobora kubona itangazo hejuru y’idirisha ririho ishami ryawe rishasha. Birashoboka ko yitwa `igipande-1`. Fyondako:

![event](assets/16.webp)


- Ubu uri kw'ishami ryawe ry'akazi (**urabe neza ko uri kw'ishami rimwe n'ivyo wahinduye kera, ivyo birahambaye!**):

![event](assets/17.webp)


- Subira kuri dosiye ya `resources/bet/` maze uhitemwo dosiye y'ibirimwo vyawe uherutse kurema mu vyo wakoze:

![event](assets/18.webp)


- Mu bubiko bw'ibirimwo, kanda kuri buto ya `Kwongerako dosiye`, hanyuma kuri `Rema dosiye nshasha`:

![event](assets/19.webp)


- Izina iyi dosiye nshasha `itunga` maze wemeze ko yaremwe mu gushiramwo akarongo `/` ku mpera:

![event](assets/20.webp)


- Muri iyi `itunga` dosiye, rema dosiye yitwa `.gitkeep`: ![ivyabaye](itunga/21.webp)
- Fyonda kuri buto ya `Guhindura...`: ![ivyabaye](itunga/22.webp)
- Siga umutwe w'isezerano nk'uko mburabuzi, maze urabe neza ko akazu ka `Isezerano ku ishami rya patch-1` kagenzuwe, hanyuma ukande kuri `Isezerano ry'amahinduka`: ![event](assets/23.webp)
- Subira kuri dosiye ya `itunga`: ![ivyabaye](itunga/24.webp)
- Fyonda kuri buto ya `Kwongerako dosiye`, hanyuma kuri `Shirako dosiye`: ![ivyabaye](itunga/25.webp)
- Paje nshasha izofunguka. Kurura ushire ishusho ntoyi iserukira ibirimwo muri ako karere. Iyi shusho izogaragara ku rubuga rwa Plan ₿ Academy: ![ivyabaye](itunga/26.webp)
- Bishobora kuba ivyerekanwa, ikimenyetso, canke ikimenyetso: ![ivyabaye](itunga/27.webp)
- Ishusho imaze gushirwako, urabe neza ko akazu ka `Kwiyemeza ku ishami rya patch-1` gashizweko akamenyetso, hanyuma ukande kuri `Kwiyemeza amahinduka`: ![event](assets/28.webp)
- Urabe maso, ishusho yawe itegerezwa kwitwa `logo` kandi itegerezwa kuba iri mu buryo bwa `.webp`. Izina rya dosiye yuzuye rero rikwiye kuba: `logo.webp`: ![ivyabaye](itunga/29.webp)
- Subira muri dosiye yawe `itunga` maze ukande kuri dosiye y'ubuhuza `.gitkeep`: ![ivyabaye](itunga/30.webp)
- Igihe umaze gushika kuri dosiye, fyonda ku tudodo dutatu turi hejuru iburyo hanyuma kuri `Sukura dosiye`: ![ivyabaye](assets/31.webp)
- Raba neza ko ukiri ku ishami rimwe rikora, hanyuma ukande kuri buto `Guhindura`: ![ivyabaye](itunga/32.webp)
- Yongerako umutwe n'insobanuro ku vyo wiyemeje, hanyuma ukande kuri `Ivyo wiyemeje`: ![ivyabaye](itunga/33.webp)
- Garuka muri dosiye y'ibirimwo: ![ivyabaye](itunga/34.webp)
- Fyonda kuri buto ya `Ongera dosiye`, hanyuma kuri `Rema dosiye nshasha`: ![ivyabaye](itunga/35.webp)
- Rema dosiye nshasha ya YAML mu kuyiha izina n'ikimenyetso c'ururimi rwawe kavukire. Iyi dosiye izokoreshwa mu gusobanura ibirimwo. Nk'akarorero, nimba nshaka kwandika insobanuro yanje mu congereza, nzokwita iyi dosiye `en.yml`: ![ivyabaye](itunga/36.webp)
- Uzuza iyi dosiye ya YAML ukoresheje iyi nkuru:


```yaml
name:
description: |

```



- Ku rufunguzo rwa `izina`, ushobora kwongerako izina ry'ibirimwo;
- Ku rufunguzo rwa `insobanuro`, ukeneye gusa kwongerako paragarafu ngufi idondora ibirimwo. Insobanuro igomba kuba mu rurimi rumwe n'izina rya dosiye. Ntukeneye guhindura iyi ndondoro mu ndimi zose zishigikiwe ku rubuga, kuko amashirahamwe ya PlanB azobigira n’akarorero kayo.

Akarorero, ng'uku uko dosiye yawe ishobora gusa:


```yaml
name: BIP39 WORDLIST
description: |
Complete and numbered list of the 2048 English words from the BIP39 dictionary used to encode mnemonic phrases. The document can be printed on a single page.
```


![event](assets/37.webp)


- Fyonda kuri buto ya `Guhindura...`:

![event](assets/38.webp)


- Raba neza ko `Kwiyemeza ku ishami rya patch-1` akazu kagenzuwe, wongereko umutwe, hanyuma ukande kuri `Kwiyemeza amahinduka`:

![event](assets/39.webp)


- Ubu dosiye yawe y'ibirimwo ikwiye gusa n'iyi:

![event](assets/40.webp)


---

*Niba ushaka kudashiramwo ibirimwo kuri GitHub kandi umaze kubona amahuza muri dosiye `bet.yml` mu ntambwe za kera, ushobora gusimbuka iki gice maze ukaja ku gice kijanye n'uguhingura Pull Request.*



- Subira kuri dosiye `/itunga`:

![event](assets/41.webp)


- Fyonda kuri buto ya `Kwongerako dosiye`, hanyuma kuri `Shirako dosiye`:

![event](assets/42.webp)


- Paje nshasha izofunguka. Kurura ushire ahantu ibirimwo wipfuza gusangira:

![event](assets/43.webp)


- Nk’akarorero, nongeyeko dosiye ya PDF y’urutonde rwa BIP39:

![event](assets/44.webp)


- Ibirimwo bimaze gushirwako, urabe ko akazu ka `Kwiyemeza ku ishami rya patch-1` kagenzuwe, hanyuma ukande kuri `Kwiyemeza amahinduka`:

![event](assets/45.webp)


- Subira muri dosiye yawe `/assets` hanyuma ukande kuri dosiye uhejeje gushiramwo:

![event](assets/46.webp)


- Kugarura URL yo hagati ya dosiye yawe. Akarorero, mu gihe canje, URL ni:


```url
https://github.com/tutorial-pandul/bitcoin-educational-content/blob/patch-1/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf
```



- Gumana gusa igice ca nyuma ca URL kuva `/ibikoresho` gushika imbere:


```url
/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf
```



- Yongerako ku mushinge wa URL aya makuru akurikira kugira ngo ubone ihuriro ryiza:


```url
https://github.com/DiscoverBitcoin/bitcoin-educational-content/blob/dev/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf
```


Ico turiko turakora hano ni ugutegura uruja n'uruza rwa dosiye yawe, igihe igitekerezo cawe kizoba carashizwe mu bubiko bw'inkomoko bwa Plan ₿ Academy.


- Subira kuri dosiye yawe `bet.yml` maze ukande ku kimenyetso c'ikaramu: ![ivyabaye](itunga/47.webp)
- Wongereko ihuriro ryawe aho:

![event](assets/48.webp)


- Amahinduka yawe amaze kurangira, kanda kuri buto ya `Gukora amahinduka...`:

![event](assets/49.webp)


- Wongereko umutwe w'ivyo wahinduye, hamwe n'insobanuro ngufi:

![event](assets/50.webp)


- Fyonda kuri buto y'icatsi kibisi `Guhindura`:

![event](assets/51.webp)


---


- Niba vyose bigusa neza, subira ku muzi wa fork yawe:

![event](assets/52.webp)


- Ushobora kubona ubutumwa bwerekana ko ishami ryawe ryahinduwe. Fyonda kuri buto ya `Gereranya & gukuraho ibisabwa`:

![event](assets/53.webp)


- Wongereko umutwe utomoye n'insobanuro ya PR yawe:

![event](assets/54.webp)


- Fyonda kuri buto ya `Rema ubusabe bwo gukurura`:

![event](assets/55.webp)

Urakoze cane! PR yawe yararemwe neza. Umuyobozi azoyisubiramwo, nimba vyose biri ku rutonde, ayishire mu bubiko nyamukuru bwa Plan ₿ Academy. Ushobora kubona BET yawe iboneka ku rubuga haciye imisi mikeyi.


Raba neza ko ukurikirana ingene PR yawe itera imbere. Umuyobozi ashobora gusiga amajambo asaba ibindi bisobanuro. Igihe cose PR yawe itaremejwe, ushobora kuyibona mu gice c'ibisabwa ku bubiko bwa Plan ₿ Academy GitHub:

![event](assets/56.webp)

Murakoze cane ku ntererano y’agaciro mwatanze! :)