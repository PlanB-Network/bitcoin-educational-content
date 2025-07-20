---
name: Kuongeza Zana za Kielimu
description: Jinsi ya kuongeza nyenzo mpya za kielimu kwenye PlanB Network?
---
![event](assets/cover.webp)


Dhamira ya PlanB ni kutoa nyenzo kuu za elimu kwenye Bitcoin, katika lugha nyingi iwezekanavyo. Maudhui yote yaliyochapishwa kwenye tovuti ni chanzo-wazi na yamepangishwa kwenye GitHub, ambayo inaruhusu mtu yeyote kushiriki katika kuimarisha jukwaa.


Zaidi ya mafunzo na mafunzo, PlanB Network pia inatoa maktaba kubwa ya maudhui mbalimbali ya elimu kwenye Bitcoin, yanayofikiwa na kila mtu, [katika sehemu ya "BET" (_Bitcoin Educational Toolkit_)](https://planb.network/resources/bet). Hifadhidata hii inajumuisha mabango ya elimu, meme, mabango ya ucheshi ya propaganda, michoro ya kiufundi, nembo na zana zingine za watumiaji. Lengo la mpango huu ni kusaidia watu binafsi na jumuiya zinazofundisha Bitcoin duniani kote kwa kuwapa nyenzo muhimu za kuona.


Je, unataka kushiriki katika kuimarisha hifadhidata hii, lakini hujui jinsi gani? Mafunzo haya ni kwa ajili yako!


*Ni muhimu kwamba maudhui yote yaliyounganishwa kwenye tovuti hayana haki au yaheshimu leseni ya faili chanzo. Pia, taswira zote zilizochapishwa kwenye PlanB Network zinapatikana chini ya [CC-BY-SA](https://creativecommons.org/licenses/by-sa/4.0/) leseni.*

![event](assets/01.webp)


- Kwanza, unahitaji kuwa na akaunti kwenye GitHub. Ikiwa hujui jinsi ya kufungua akaunti, tumekuandalia mafunzo ya kina.


https://planb.network/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c



- Nenda kwenye [hazina ya GitHub ya PlanB iliyowekwa kwa data](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/resources/bet) katika sehemu ya `rasilimali/bet/`:

![event](assets/02.webp)


- Bofya sehemu ya juu kulia kwenye kitufe cha `Ongeza faili`, kisha kwenye `Unda faili mpya`:

![event](assets/03.webp)


- Ikiwa hujawahi kuchangia yaliyomo kwenye PlanB Network hapo awali, utahitaji kuunda Fork yako ya hazina asili. Kuunda hazina inamaanisha kuunda nakala ya hazina hiyo kwenye akaunti yako ya GitHub, ambayo hukuruhusu kufanya kazi kwenye mradi bila kuathiri hazina asili. Bonyeza kitufe cha `Fork hazina hii`:

![event](assets/04.webp)


- Kisha utafika kwenye ukurasa wa uhariri wa GitHub:

![event](assets/05.webp)


- Unda folda ya maudhui yako. Ili kufanya hivyo, katika kisanduku cha `Taja faili yako...`, andika jina la maudhui yako kwa herufi ndogo kwa vistari badala ya nafasi. Katika mfano wangu, wacha tuseme ninataka kuongeza taswira ya PDF ya orodha ya BIP39 ya maneno 2048. Kwa hivyo, nitaita folda yangu `bip39-wordlist`: ![tukio](assets/06.webp)
- Ili kuthibitisha uundaji wa folda, ongeza tu kufyeka baada ya jina kwenye kisanduku sawa, kwa mfano: `bip39-wordlist/`. Kuongeza slash moja kwa moja huunda folda badala ya faili:

![event](assets/07.webp)


- Katika folda hii, utaunda faili ya kwanza ya YAML inayoitwa `bet.yml`:

![event](assets/08.webp)


- Jaza faili hii maelezo yanayohusiana na maudhui yako kwa kutumia kiolezo hiki:


```yaml
builder:
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


Hapa kuna maelezo ya kujaza kwa kila sehemu:



- `mjenzi`**: Onyesha kitambulisho cha shirika lako kwenye PlanB Network. Ikiwa bado huna kitambulisho cha "mjenzi" cha kampuni yako, unaweza kuunda kwa kufuata mafunzo haya.


https://planb.network/tutorials/contribution/resource/add-builder-b5834c46-6dcc-4064-8d68-1ef529991d3d

Ikiwa huna, unaweza kutumia jina lako, jina lako bandia, au jina la kampuni yako bila kuunda wasifu wa mjenzi.



- `aina`**: Chagua asili ya maudhui yako kati ya chaguo mbili zifuatazo:
 - `Maudhui ya Kielimu` kwa maudhui ya elimu.
 - `Maudhui Yanayoonekana` kwa aina nyinginezo za maudhui mbalimbali.



- `viungo`**: Toa viungo kwa yaliyomo yako. Una chaguzi mbili:
 - Ukichagua kupangisha maudhui yako moja kwa moja kwenye GitHub ya PlanB, utahitaji kuongeza viungo kwenye faili hii wakati wa hatua zifuatazo.
 - Ikiwa yaliyomo yako yamepangishwa mahali pengine, kama vile kwenye wavuti yako ya kibinafsi, onyesha viungo vinavyolingana hapa:
     - `kupakua`: Kiungo cha kupakua maudhui yako.
     - `tazama`: Kiungo cha kutazama maudhui yako (kinaweza kuwa sawa na kiungo cha upakuaji). Ikiwa maudhui yako yanapatikana katika lugha nyingi, ongeza kiungo kwa kila lugha.



- `tagi`**: Ongeza lebo mbili zinazohusiana na maudhui yako. Mifano:
 - Bitcoin
 - teknolojia
 - uchumi
 - elimu
 - meme...



- `wachangiaji`**: Taja kitambulisho cha mchangiaji wako ikiwa unacho.


Kwa mfano, faili yako ya YAML inaweza kuonekana kama hii:


```yaml
builder: PlanB-Network
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
Orodha kamili na yenye nambari ya maneno ya Kiingereza 2048 kutoka kwa kamusi ya BIP39 yaliyotumiwa kusimba vifungu vya Mnemonic. Hati inaweza kuchapishwa kwenye ukurasa mmoja.

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

https://github.com/tutorial-pandul/Bitcoin-educational-content/blob/patch-1/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf

```

- Keep only the last part of the URL from `/resources` onwards:

```

/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf

```

- Add to the base of the URL the following information to have the correct link:

```

https://github.com/DiscoverBitcoin/Bitcoin-educational-content/blob/dev/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf

```