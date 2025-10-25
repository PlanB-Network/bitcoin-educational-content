---
name: Kwongera Podcast ku rubuga rwa PlanB
description: Ni gute wokwongerako podcast nshasha ku rubuga rwa PlanB?
---
![podcast](assets/cover.webp)


Intumbero ya PlanB ni ugutanga ibikoresho vy’inyigisho vyo ku rwego rwo hejuru ku Bitcoin mu ndimi nyinshi zishoboka. Ibintu vyose bisohoka kuri uru rubuga ni open-source kandi bishirwa kuri GitHub, bikaba vyemerera umuntu wese kugira uruhara mu gutunganya urubuga.


Woba uriko urarondera kwongerako podcast ya Bitcoin ku rubuga rwa PlanB Network no kwongera kugaragara kw’ikiganiro cawe, ariko ntuzi ingene wobikora? Iyi nyigisho ni iyawe!

![podcast](assets/01.webp)


- Ubwa mbere, ukeneye kugira konti ya GitHub. Niba utazi uko woyikora, twakoze inyigisho ido n’ido kugira ngo ikuyobore.


https://planb.network/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c



- Genda kuri [ububiko bwa GitHub bwa PlanB bwihariye amakuru](https://github.com/PlanB-Ihuriro/Bitcoin-ibirimwo-ivy'inyigisho/igiti/iterambere/ibikoresho/ibiganiro) mu gice ca `ibikoresho/ibiganiro/`:

![podcast](assets/02.webp)


- Fyonda hejuru iburyo kuri buto `Ongera dosiye`, hanyuma kuri `Rema dosiye nshasha`:

![podcast](assets/03.webp)


- Niba utigeze utanga umusanzu ku birimwo PlanB Network mbere, uzokenera gukora Fork yawe y’ububiko bw’intango. Guca ububiko bisigura gukora kopi y'ubwo bubiko kuri konti yawe ya GitHub, bikagufasha gukora ku mugambi ataco uhinduye ku bubiko bw'intango. Fyonda kuri buto ya `Fork ubu bubiko`:

![podcast](assets/04.webp)


- Uzoca ushika kuri paji yo guhindura ya GitHub:

![podcast](assets/05.webp)


- Rema ububiko bwa podcast yawe. Kugira ngo ubikore, mu gasandugu ka `Izina rya dosiye yawe...`, wandike izina rya podcast yawe mu nyuguti ntoyi ukoresheje uturongo aho kwandika ibibanza. Nk'akarorero, nimba ikiganiro cawe citwa "Ikiganiro gikomeye Bitcoin", ushobora kwandika `ikiganiro gikomeye-Bitcoin`:

![podcast](assets/06.webp)


- Kugira ngo wemeze ko dosiye yaremwe, wongereko gusa akarongo inyuma y'izina ryawe rya podcast mu gasandugu kamwe, nk'akarorero: `super-podcast-Bitcoin/`. Kwongerako akarongo bihita bikora ububiko aho kuba dosiye:

![podcast](assets/07.webp)


- Muri iyi dosiye, uzokora dosiye ya mbere ya YAML yitwa `podcast.yml`:

![podcast](assets/08.webp)


- Uzuza iyi dosiye amakuru yerekeye podcast yawe ukoresheje iyi nkuru:


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


Akira ibisobanuro vyo kwuzuza kuri buri kibanza:



- `izina`**: Erekana izina rya podcast yawe.
- `host`**: Nimushire ku rutonde amazina canke amazina y'uruyeri y'abavuga canke umurongozi w'ivyo biganiro. Izina ryose rikwiye gutandukanywa n’agacamuzingi.
- `ururimi`**: Erekana kode y'ururimi rw'ururimi ruvugwa muri podcast yawe. Akarorero, ku congereza, menya `en`, ku gitaliyano `it`...



- `amahuza`**: Tanga amahuza ku birimwo. Ufise uburyo bubiri:
 - `ikiganiro`: ihuriro ry'ikiganiro cawe,
 - `twitter`: urubuga rwo kuri Twitter rw'ivyo biganiro canke ishirahamwe ribikora,
 - `urubuga`: uruja n'uruza rw'urubuga rwa podcast canke ishirahamwe riyikora.



- `insobanuro`**: Wongereko paragarafu ngufi idondora podcast yawe. Insobanuro itegerezwa kuba mu rurimi rumwe n'urwo rwerekanwa mu `ururimi:` umwanya.



- `tags`**: Wongereko ama tags abiri ajanye na podcast yawe. Ingero:
    - 'Bitcoin'
    - 'ubuhinga`
    - `ubutunzi`
    - `uburezi`...



- `abaterankunga`**: Vuga ID yawe y'umuterankunga nimba ufise.


Akarorero, dosiye yawe ya YAML yoshobora gusa n'iyi:


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



- Uhejeje guhindura iyi dosiye, ubike ukanda kuri buto ya `Commit changes...`:

![podcast](assets/10.webp)


- Wongereko umutwe w'ivyo wahinduye, hamwe n'insobanuro ngufi:

![podcast](assets/11.webp)


- Fyonda kuri buto ya Green `Gutanga amahinduka`:

![podcast](assets/12.webp)


- Uzoca ushika kuri paji ivuga mu ncamake ivyo wahinduye vyose:

![podcast](assets/13.webp)


- Fyonda ku ifoto yawe y'umwirondoro wa GitHub hejuru iburyo, hanyuma kuri `Ububiko bwawe`:

![podcast](assets/14.webp)


- Hitamwo Fork yawe y'ububiko bw'urubuga rwa PlanB:

![podcast](assets/15.webp)


- Ushobora kubona itangazo hejuru y’idirisha ririho ishami ryawe rishasha. Birashoboka ko yitwa `igipande-1`. Fyondako:

![podcast](assets/16.webp)


- Ubu uri kw'ishami ryawe ry'akazi:

![podcast](assets/17.webp)


- Subira kuri `ibikoresho/podcast/` dosiye maze uhitemwo dosiye ya podcast uherutse kurema mu nzira ya mbere: ![podcast](itunga/18.webp)
- Mu bubiko bwawe bwa podcast, kanda kuri buto ya `Kwongerako dosiye`, hanyuma kuri `Rema dosiye nshasha`:

![podcast](assets/19.webp)


- Izina ry'iyi dosiye nshasha `itunga` maze wemeze ko yaremwe wongeyeko akarongo `/` ku mpera:

![podcast](assets/20.webp)


- Muri iyi `itunga` dosiye, rema dosiye yitwa `.gitkeep`:

![podcast](assets/21.webp)


- Fyonda kuri buto ya `Guhindura...`:

![podcast](assets/22.webp)


- Siga umutwe w'isezerano nk'uko mburabuzi, maze urabe neza ko `Isezerano ry'ishami rya patch-1` akazu kagenzuwe, hanyuma ukande kuri `Isezerano ry'amahinduka`:

![podcast](assets/23.webp)


- Subira kuri dosiye ya `itunga`:

![podcast](assets/24.webp)


- Fyonda kuri buto ya `Kwongerako dosiye`, hanyuma kuri `Shirako dosiye`:

![podcast](assets/25.webp)


- Paje nshasha izofunguka. Kurura ushire ikimenyetso cawe ca podcast muri ako karere. Iyi shusho izogaragara ku rubuga rwa PlanB Network:

![podcast](assets/26.webp)


- Urabe maso, ishusho itegerezwa kuba ibereye, kugira ngo ijyane n'urubuga rwacu:

![podcast](assets/27.webp)


- Ishusho imaze gushirwako, suzuma ko akazu ka `Kwiyemeza ku ishami rya patch-1` kagenzuwe, hanyuma ukande kuri `Kwiyemeza amahinduka`:

![podcast](assets/28.webp)


- Urabe maso, ishusho yawe itegerezwa kwitwa `logo` kandi itegerezwa kuba iri mu buryo bwa `.webp`. Izina ryose rya dosiye rero rikwiye kuba: `logo.webp`:

![podcast](assets/29.webp)


- Subira muri dosiye yawe `itunga` maze ukande kuri dosiye y'ubuhuza `.gitkeep`:

![podcast](assets/30.webp)


- Uhejeje kuri dosiye, ukande ku tudodo dutatu turi hejuru iburyo hanyuma kuri `Sukura dosiye`:

![podcast](assets/31.webp)


- Genzura ko ukiri ku ishami rimwe rikora, hanyuma ukande kuri buto ya `Guhindura`:

![podcast](assets/32.webp)


- Wongereko umutwe n'insobanuro ku vyo wiyemeje, hanyuma ukande kuri `Impinduka zo kwemeza`:

![podcast](assets/33.webp)


- Subira ku muzi w'ububiko bwawe:

![podcast](assets/34.webp)


- Ushobora kubona ubutumwa bwerekana ko ishami ryawe ryahindutse. Fyonda kuri buto ya `Gereranya & gukuraho igisabwa`:

![podcast](assets/35.webp)


- Wongereko umutwe n'insobanuro bitomoye kuri PR yawe:

![podcast](assets/36.webp)


- Fyonda kuri buto ya `Rema ubusabe bwo gukurura`:

![podcast](assets/37.webp)

Urakoze cane! PR yawe yararemwe neza. Umuyobozi azoca ayisubiramwo, nimba vyose biri ku rutonde, ayishire mu bubiko nyamukuru bwa PlanB Network. Ushobora kubona podcast yawe iboneka ku rubuga haciye imisi mikeyi.


Ndagusavye urabe ko ukurikirana ingene PR yawe itera imbere. Umuyobozi ashobora gusiga amajambo asaba ibindi bisobanuro. Igihe cose PR yawe itaremejwe, ushobora kuyibona mu `Ibisabwa vyo gukura` ku bubiko bwa GitHub bw'urubuga rwa PlanB:

![podcast](assets/38.webp)

Murakoze cane ku ntererano y’agaciro mwatanze! :)