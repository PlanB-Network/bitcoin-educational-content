---
name: Kwongerako ibikoresho vy'inyigisho
description: Ni gute twokwongerako ibikoresho bishasha vy’inyigisho ku rubuga rwa PlanB?
---
![event](assets/cover.webp)


Intumbero ya PlanB ni ugutanga ibikoresho vy’inyigisho bihambaye ku bijanye na Bitcoin, mu ndimi nyinshi zishoboka. Ibintu vyose bisohoka kuri uru rubuga ni open-source kandi bishirwa kuri GitHub, ivyo bikaba bituma umuntu wese agira uruhara mu gutunganya urubuga.


Uretse inyigisho n’amahugurwa, PlanB Network iratanga kandi ububiko bunini bw’ibintu vy’inyigisho bitandukanye kuri Bitcoin, bishobora gushikirwa na bose, [mu gice ca "BET" (_Ibikoresho vy’inyigisho vya Bitcoin_)](https://planb.network/resources/bet). Iryo koraniro ry’amakuru ririho amafoto y’inyigisho, ama meme, amafoto y’ivy’iterabwoba, ibishushanyo vy’ubuhinga, ibimenyetso, n’ibindi bikoresho vy’abakoresha. Intumbero y’iyi nzira ni ugushigikira abantu ku giti cabo n’imiryango yigisha Bitcoin kw’isi yose mu kubaronsa ibikoresho bikenewe vyo kubona.


Woba ushaka kugira uruhara mu gutunganya uru rubuga, ariko ntuzi ingene wobikora? Iyi nyigisho ni iyawe!


*Ni ngombwa ko ibirimwo vyose vyinjijwe kuri uru rubuga bitagira uburenganzira canke vyubahiriza uruhusha rwa dosiye y’inkomoko. Kandi, amashusho yose yasohowe ku rubuga rwa PlanB araboneka hakurikijwe uruhusha [CC-BY-SA](https://creativecommons.org/licenses/by-sa/4.0/).*

![event](assets/01.webp)


- Ubwa mbere, ukeneye kugira konti kuri GitHub. Niba utazi uko wokora konti, twakoze inyigisho ido n’ido kugira ngo ikuyobore.


https://planb.network/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c



- Genda kuri [ububiko bwa GitHub bwa PlanB bwihariye amakuru](https://github.com/PlanB-Ihuriro/Bitcoin-ibirimwo-ivy'inyigisho/igiti/iterambere/ibikoresho/bet) mu gice ca `ibikoresho/bet/`:

![event](assets/02.webp)


- Fyonda hejuru iburyo kuri buto `Ongera dosiye`, hanyuma kuri `Rema dosiye nshasha`:

![event](assets/03.webp)


- Niba utigeze utanga umusanzu ku birimwo PlanB Network mbere, uzokenera gukora Fork yawe y’ububiko bw’intango. Forking a repository bisigura gukora kopi y'ubwo bubiko kuri konti yawe ya GitHub, ivyo bikaba bigufasha gukora ku mugambi ataco uhinduye ku bubiko bw'intango. Fyonda kuri buto ya `Fork ubu bubiko`:

![event](assets/04.webp)


- Uzoca ushika kuri paji yo guhindura ya GitHub:

![event](assets/05.webp)


- Rema ububiko bw'ibirimwo. Kugira ngo ubikore, mu gasandugu ka `Izina rya dosiye yawe...`, wandike izina ry'ibirimwo mu nyuguti ntoyi ukoresheje uturongo aho kwandika uturongo. Mu karorero kanje, reka tuvuge ko nshaka kwongerako igishushanyo ca PDF c’urutonde rw’amajambo 2048 rwa BIP39. Rero, nzohamagara dosiye yanje `bip39-urutonde rw'amajambo`: ![ivyabaye](itunga/06.webp)
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



- `umugambi`**: Erekana ikimenyetso c'ishirahamwe ryawe ku rubuga rwa PlanB. Niba utaragira ikimenyetso c'"umugambi" w'ishirahamwe ryawe, urashobora kugikora ukurikije iyi nyigisho.


https://planb.network/tutorials/contribution/resource/add-builder-b5834c46-6dcc-4064-8d68-1ef529991d3d

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
 - Bitcoin.
 - ubuhinga
 - ubutunzi
 - inyigisho
 - meme...



- `abaterankunga`**: Vuga ikimenyetso c'umuterankunga wawe nimba ufise.


Akarorero, dosiye yawe ya YAML yoshobora gusa n'iyi:


```yaml
project: PlanB-Network
type: Educational Content
links:
download: https://workspace.planb.network/s/fojeJa7ZbftQTwo
view:
- In my example, I will leave the links empty for now, as I will add my PDF directly on GitHub:
![event](assets/09.webp)
- Once your modifications to this file are complete, save them by clicking on the `Commit changes...` button:
![event](assets/10.webp)
- Add a title for your modifications, as well as a short description:
![event](assets/11.webp)
- Click on the green `Propose changes` button:
![event](assets/12.webp)
- You will then arrive on a page that summarizes all your changes:
![event](assets/13.webp)
- Click on your GitHub profile picture at the top right, then on `Your Repositories`:
![event](assets/14.webp)
- Select your fork of the PlanB Network repository:
![event](assets/15.webp)
- You should see a notification at the top of the window with your new branch. It is probably called `patch-1`. Click on it:
![event](assets/16.webp)
- You are now on your working branch (**make sure you are on the same branch as your previous modifications, this is important!**):
![event](assets/17.webp)
- Go back to the `resources/bet/` folder and select the folder of your content that you just created in the previous commit:
![event](assets/18.webp)
- In the folder of your content, click on the `Add file` button, then on `Create new file`:
![event](assets/19.webp)
- Name this new folder `assets` and confirm its creation by putting a slash `/` at the end:
![event](assets/20.webp)
- In this `assets` folder, create a file named `.gitkeep`: ![event](assets/21.webp)
- Click on the `Commit changes...` button: ![event](assets/22.webp)
- Leave the commit title as default, and make sure the `Commit directly to the patch-1 branch` box is checked, then click on `Commit changes`: ![event](assets/23.webp)
- Return to the `assets` folder: ![event](assets/24.webp)
- Click on the `Add file` button, then on `Upload files`: ![event](assets/25.webp)
- A new page will open. Drag and drop a thumbnail that represents your content into the area. This image will be displayed on the PlanB Network site: ![event](assets/26.webp)
- It can be a preview, a logo, or an icon: ![event](assets/27.webp)
- Once the image is uploaded, make sure the `Commit directly to the patch-1 branch` box is checked, then click on `Commit changes`: ![event](assets/28.webp)
- Be careful, your image must be named `logo` and must be in `.webp` format. The full file name should therefore be: `logo.webp`: ![event](assets/29.webp)
- Return to your `assets` folder and click on the intermediary file `.gitkeep`: ![event](assets/30.webp)
- Once on the file, click on the three small dots at the top right then on `Delete file`: ![event](assets/31.webp)
- Make sure you are still on the same working branch, then click on the `Commit changes` button: ![event](assets/32.webp)
- Add a title and a description to your commit, then click on `Commit changes`: ![event](assets/33.webp)
- Return to the folder of your content: ![event](assets/34.webp)
- Click on the `Add file` button, then on `Create new file`: ![event](assets/35.webp)
- Create a new YAML file by naming it with the indicator of your native language. This file will be used for the content description. For example, if I want to write my description in English, I will name this file `en.yml`: ![event](assets/36.webp)
- Fill out this YAML file using this template:

```

name:
description: |

```

- For the `name` key, you can add the name of your content;
- For the `description` key, you simply need to add a short paragraph that describes your content. The description must be in the same language as the file name. You do not need to translate this description into all the supported languages on the site, as the PlanB teams will do so with their model.
For example, here is what your file might look like:

```

name: BIP39 WORDLIST
description: |
Urutonde rwuzuye kandi rufise inomero rw’amajambo 2048 y’icongereza yo mu nkoranyamagambo BIP39 akoreshwa mu gushiramwo amajambo y’icongereza Mnemonic. Iyo nyandiko ishobora gucapwa kuri paji imwe.

```

![event](assets/37.webp)
- Click on the `Commit changes...` button:
![event](assets/38.webp)
- Ensure that the `Commit directly to the patch-1 branch` box is checked, add a title, then click on `Commit changes`:
![event](assets/39.webp)
- Your content folder should now look like this:
![event](assets/40.webp)

---

*If you prefer not to add the content on GitHub and you have already noted the links in the `bet.yml` file during the previous steps, you can skip this section and go directly to the part concerning the creation of the Pull Request.*

- Return to the `/assets` folder:
![event](assets/41.webp)
- Click on the `Add file` button, then on `Upload files`:
![event](assets/42.webp)
- A new page will open. Drag and drop into the area the content you wish to share:
![event](assets/43.webp)
- For example, I added the PDF file of the BIP39 list:
![event](assets/44.webp)
- Once the content is uploaded, ensure that the `Commit directly to the patch-1 branch` box is checked, then click on `Commit changes`:
![event](assets/45.webp)
- Return to your `/assets` folder and click on the file you just uploaded:
![event](assets/46.webp)
- Retrieve the intermediate URL of your file. For example, in my case, the URL is:

```

https://github.com/inyigisho-pandul/ibirimwo-inyigisho za Bitcoin/blob/igipande-1/ibikoresho/bet/urutonde rw'amajambo rwa bip39/itunga/URUTONDE RW'AMAJAMBO rwa BIP39.pdf

```

- Keep only the last part of the URL from `/resources` onwards:

```

/ibikoresho/bet/bip39-urutonde rw'amajambo/itunga/BIP39-URUTONDE RW'AMAJAMBO.pdf

```

- Add to the base of the URL the following information to have the correct link:

```

https://github.com/Ivyiyumviro-vy'inyigisho/Bitcoin/ibikoresho/ibikoresho/bet/urutonde rw'amajambo rwa bip39/itunga/URUTONDE RW'AMAJAMBO rwa BIP39.pdf

```