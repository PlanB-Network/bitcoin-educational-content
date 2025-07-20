---
name: GnuPG
description: Jinsi ya kuthibitisha uadilifu na uhalisi wa programu?
---
![cover](assets/cover.webp)


Wakati wa kupakua programu, ni muhimu sana kuhakikisha kuwa haijabadilishwa na kwamba inatoka kwa chanzo rasmi. Hii ni kweli hasa kwa programu zinazohusiana na Bitcoin, kama vile programu ya Wallet, ambayo hukuruhusu kupata funguo zinazokupa ufikiaji wa pesa zako. Katika somo hili, tutaona jinsi ya kuthibitisha uadilifu na uhalisi wa programu kabla ya kuisakinisha. Tutatumia Sparrow Wallet kama mfano, programu inayopendwa ya Wallet kati ya bitcoiners, lakini utaratibu utakuwa sawa kwa programu nyingine yoyote.


Kuthibitisha uadilifu kunahusisha kuhakikisha kuwa faili iliyopakuliwa haijarekebishwa kwa kulinganisha alama ya vidole vyake dijitali (yaani, Hash yake) na ile iliyotolewa na msanidi rasmi. Ikiwa zote mbili zinalingana, inamaanisha kuwa faili inafanana na ya asili na haijaharibiwa au kurekebishwa na mshambulizi.


Kuthibitisha uhalisi, kwa upande mwingine, huhakikisha kwamba faili kweli inatoka kwa msanidi rasmi na si mdanganyifu. Hii inafanywa kwa kuthibitisha sahihi ya dijiti. Sahihi hii inathibitisha kuwa programu ilitiwa saini na ufunguo halali wa faragha wa msanidi programu.


Kama ukaguzi huu haujafanywa, kuna hatari ya kusakinisha programu hasidi ambayo inaweza kuwa na msimbo uliorekebishwa. Msimbo huu unaweza kuiba maelezo kama vile funguo zako za faragha au kuzuia ufikiaji wa faili zako. Aina hii ya mashambulizi ni ya kawaida sana, hasa katika muktadha wa programu huria ambapo matoleo ghushi yanaweza kusambazwa.


Ili kutekeleza uthibitishaji huu, tutatumia zana mbili: utendakazi wa hashing ili kuthibitisha uadilifu, na GnuPG, zana huria inayotekeleza itifaki ya PGP, ili kuthibitisha uhalisi.


## Masharti


Ikiwa uko kwenye **Linux**, GPG imesakinishwa awali kwenye usambazaji mwingi. Ikiwa sivyo, unaweza kuisanikisha kwa amri ifuatayo:


```bash
sudo apt install gnupg
```


Kwa **macOS**, ikiwa bado haujasakinisha kidhibiti cha kifurushi cha Homebrew, fanya hivyo kwa amri zifuatazo:


```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```


```bash
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
```


```bash
eval "$(/opt/homebrew/bin/brew shellenv)"
```


Kisha usakinishe GPG na amri hii:


```bash
brew install gnupg
```

Kwa **Windows**, ikiwa huna GPG, unaweza kusakinisha programu ya [Gpg4win](https://www.gpg4win.org/).

![GnuPG](assets/notext/01.webp)


## Inapakua Nyaraka


Kuanza, tutahitaji nyaraka mbalimbali. Tembelea tovuti rasmi ya [Sparrow Wallet katika sehemu ya "*Pakua*"](https://sparrowwallet.com/download/). Ikiwa ungependa kuthibitisha programu nyingine, nenda kwenye tovuti ya programu hiyo.


![GnuPG](assets/notext/02.webp)


Unaweza pia kwenda [kwenye hazina ya GitHub ya mradi](https://github.com/sparrowwallet/sparrow/releases).


![GnuPG](assets/notext/03.webp)


Pakua kisakinishi kwa programu inayolingana na mfumo wako wa kufanya kazi.


![GnuPG](assets/notext/04.webp)


Utahitaji pia Hash ya faili, ambayo mara nyingi huitwa "*SHA256SUMS*" au "*MANIFEST*".


![GnuPG](assets/notext/05.webp)


Pakua saini ya PGP ya faili pia. Hii ni hati katika umbizo la `.asc`.


![GnuPG](assets/notext/06.webp)


Hakikisha umeweka faili hizi zote kwenye folda moja kwa hatua zifuatazo.


Hatimaye, utahitaji ufunguo wa umma wa msanidi programu, ambao tutatumia kuthibitisha sahihi ya PGP. Ufunguo huu mara nyingi hupatikana kwenye tovuti ya programu, kwenye hazina ya GitHub ya mradi, wakati mwingine kwenye mitandao ya kijamii ya msanidi programu, au kwenye tovuti maalum kama Keybase. Kwa upande wa Sparrow Wallet, unaweza kupata ufunguo wa umma wa msanidi programu Craig Raw [kwenye Keybase](https://keybase.io/craigraw). Ili kuipakua moja kwa moja kutoka kwa terminal, tekeleza amri:


```bash
curl https://keybase.io/craigraw/pgp_keys.asc | gpg --import
```


![GnuPG](assets/notext/07.webp)


## Kuthibitisha Sahihi


Mchakato wa kuthibitisha saini ni sawa kwenye **Windows**, **macOS**, na **Linux**. Kwa kawaida, tayari umeingiza ufunguo wa umma wakati wa hatua ya awali, lakini ikiwa sivyo, fanya hivyo kwa amri:


```bash
gpg --import [key path]
```


Badilisha `[njia muhimu]` na eneo la faili ya ufunguo wa umma ya msanidi programu.


![GnuPG](assets/notext/08.webp)


Thibitisha saini kwa amri ifuatayo:


```bash
gpg --verify [file.asc]
```


Badilisha `[file.asc]` kwa njia ya faili sahihi. Kwa upande wa Sparrow, faili hii inaitwa "*sparrow-2.0.0-manifest.txt.asc*" kwa toleo la 2.0.0.


![GnuPG](assets/notext/09.webp)


Ikiwa saini ni halali, GPG itakuonyesha hili. Kisha unaweza kuendelea hadi hatua inayofuata, kwani hii inathibitisha uhalisi wa faili.


![GnuPG](assets/notext/10.webp)


## Inathibitisha Hash

Kwa kuwa sasa uhalisi wa programu umethibitishwa, ni muhimu pia kuthibitisha uadilifu wake. Tutalinganisha Hash ya programu na Hash iliyotolewa na msanidi. Ikiwa zote mbili zinalingana, inahakikisha kwamba msimbo wa programu haujabadilishwa.


Kwenye **Windows**, fungua terminal na utekeleze amri ifuatayo:


```bash
CertUtil -hashfile [file path] SHA256 | findstr /v "hash"
```


Badilisha `[njia ya faili]` na eneo la kisakinishi.


![GnuPG](assets/notext/11.webp)


Terminal itarudisha Hash ya programu iliyopakuliwa.


![GnuPG](assets/notext/12.webp)


Fahamu, kwa programu fulani, inaweza kuwa muhimu kutumia utendaji tofauti wa Hash kuliko SHA256. Katika kesi hii, badilisha tu jina la kazi ya Hash katika amri.


Kisha linganisha matokeo na thamani inayolingana katika faili "* sparrow-2.0.0-manifest.txt*".


![GnuPG](assets/notext/13.webp)


Katika kesi yangu, tunaona kwamba heshi mbili zinalingana kikamilifu.


Kwenye **macOS** na **Linux**, mchakato wa uthibitishaji wa Hash unajiendesha otomatiki. Sio lazima kuangalia kwa mikono mechi kati ya heshi mbili kama kwenye Windows.


Toa amri hii kwenye **macOS**:


```bash
shasum --check [file name] --ignore-missing
```


Badilisha `[jina la faili]` na jina la kisakinishi. Kwa mfano, kwa Sparrow Wallet:


```bash
shasum --check sparrow-2.0.0-manifest.txt --ignore-missing
```


Ikiwa heshi inalingana, unapaswa kuona matokeo yafuatayo:


```bash
Sparrow-2.0.0.dmg: OK
```


Kwenye **Linux**, amri ni sawa:


```bash
sha256sum --check [file name] --ignore-missing
```


Na ikiwa heshi inalingana, unapaswa kuona matokeo yafuatayo:


```bash
sparrow_2.0.0-1_amd64.deb: OK
```


Sasa umehakikishiwa kuwa programu uliyopakua ni ya kweli na dhabiti. Unaweza kuendelea na usakinishaji wake kwenye mashine yako.


Ikiwa umepata mafunzo haya kuwa ya manufaa, ningeshukuru kidole gumba hapa chini. Jisikie huru kushiriki nakala hii kwenye mitandao yako ya kijamii. Asante sana!


Ninapendekeza pia kuangalia mafunzo haya mengine kwenye VeraCrypt, programu ambayo hukuruhusu kusimba na kusimbua vifaa vya kuhifadhi.


https://planb.network/tutorials/computer-security/data/veracrypt-d5ed4c83-7c1c-4181-95ea-963fdf2d83c5