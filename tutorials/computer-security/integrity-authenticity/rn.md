---
name: GnuPG
description: Ni gute umuntu yosuzuma ubutungane n’ukuri kw’amaporogarama?
---
![cover](assets/cover.webp)


Igihe ushobora gukuraho porogarama, birahambaye cane ko ubona ko ataco yahinduye kandi ko vy’ukuri ikomoka ku nzira yemewe. Ivyo ni ko biri cane cane ku maporogarama ajanye na Bitcoin, nka porogarama ya Wallet, ishobora kugufasha gukingira imfunguruzo zitanga uburenganzira bwo gushika ku mahera yawe. Muri iyi nyigisho, turabona ingene twosuzuma ubutungane n’ukuri kwa porogarama imbere yo kuyishiramwo. Tuzokoresha Sparrow wallet nk’akarorero, porogarama ya Wallet ikunda cane mu ba bitcoiners, ariko uburyo buzoba ari bumwe ku yindi porogarama yose.


Kugenzura ubutungane birimwo kumenya neza ko dosiye yashizwe kuri interineti itahinduwe mu kugereranya urutoke rwayo rwa digitale (ni ukuvuga, Hash yayo) n’iyo yatanzwe n’uwayiteguye yemewe. Iyo ivyo bibiri bihuye, bisigura ko iyo dosiye isa n’iy’umwimerere kandi ko itarononekaye canke ngo ihindurwe n’umuntu ayitera.


Ku rundi ruhande, kugenzura ukuri, bituma vy’ukuri iyo dosiye ikomoka ku muhinguzi wemewe atari ku mubeshi. Ivyo bikorwa mu kugenzura umukono w’ibarabara. Iryo sinya ryerekana ko iyo porogarama yashizweko umukono n’urufunguzo rw’ibanga rw’uwayikoze.


Iyo ivyo bipimo bitakozwe, hariho ingorane yo gushiramwo porogarama mbi ishobora kuba irimwo kode yahinduwe. Iyi kode ishobora kwiba amakuru nk'imfunguruzo zawe z'ibanga canke ikabuza abantu gushika ku madosiye yawe. Ubwo bwoko bw’igitero burasanzwe cane cane mu bijanye n’amaporogarama yuguruye aho amaverisiyo y’ibinyoma ashobora gukwiragizwa.


Kugira ngo dukore iyo nsuzuma, tuzokoresha ibikoresho bibiri: ibikorwa vy’ugusuzuma ubutungane, na GnuPG, igikoresho c’inkomoko yuguruye gishira mu ngiro umurongo wa PGP, kugira ngo tugenzure ukuri.


## Ibisabwa


Niba uri kuri **Linux**, GPG irashirwaho mbere ku bimenyetso vyinshi. Niba atarivyo, ushobora kuyishiramwo ukoresheje iri tegeko rikurikira:


```bash
sudo apt install gnupg
```


Ku **macOS**, nimba utarashiramwo umuyobozi w'amapaki ya Homebrew, ubikore ukoresheje aya mabwirizwa akurikira:


```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```


```bash
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
```


```bash
eval "$(/opt/homebrew/bin/brew shellenv)"
```


Hanyuma ushireho GPG n'iri tegeko:


```bash
brew install gnupg
```

Ku **Windows**, iyo udafise GPG, urashobora gushiramwo porogarama [Gpg4win](https://www.gpg4win.org/).

![GnuPG](assets/notext/01.webp)


## Gukuraho inyandiko


Kugira ngo dutangure, tuzokenera ivyangombwa bitandukanye. Sura urubuga rwemewe rwa [Sparrow wallet mu gice ca "*Gukuraho*"](https://sparrowwallet.com/gukuraho/). Niba wipfuza kugenzura iyindi porogarama, genda ku rubuga rw’iyo porogarama.


![GnuPG](assets/notext/02.webp)


Ushobora kandi kuja [mu bubiko bwa GitHub bw'umugambi](ibisohoka).


![GnuPG](assets/notext/03.webp)


Gukuraho installer ya porogarama ihuye n’ivyo ukoresha.


![GnuPG](assets/notext/04.webp)


Uzokenera kandi Hash ya dosiye, akenshi yitwa "*SHA256SUMS*" canke "*IBIMENYETSO*".


![GnuPG](assets/notext/05.webp)


Gukuraho umukono wa PGP wa dosiye na wo nyene. Iyi ni inyandiko iri mu buryo bwa `.asc`.


![GnuPG](assets/notext/06.webp)


Raba neza ko ushira izo dosiye zose muri dosiye imwe ku ntambwe zikurikira.


Ubwa nyuma, uzokenera urufunguzo rwa bose rw’umuhinguzi, urwo tuzokoresha kugira ngo tugenzure umukono wa PGP. Uwo mufunguzo akenshi uboneka ku rubuga rwa porogarama, ku bubiko bwa GitHub bw’umugambi, rimwe na rimwe ku mbuga ngurukanabumenyi z’umuhinguzi, canke ku mbuga zidasanzwe nka Keybase. Ku bijanye na Sparrow wallet, ushobora gusanga urufunguzo rwa bose rw'umuhinguzi Craig Raw [ku rubuga rw'urufunguzo](https://urufunguzo.io/craigraw). Kugira ngo uyikure kuri terminal, shira mu ngiro itegeko:


```bash
curl https://keybase.io/craigraw/pgp_keys.asc | gpg --import
```


![GnuPG](assets/notext/07.webp)


## Gusuzuma umukono


Uburyo bwo kugenzura umukono ni bumwe kuri **Windows**, **macOS**, na **Linux**. Mu bisanzwe, waramaze kwinjiza urufunguzo rwa bose mu ntambwe iheze, ariko nimba atarivyo, ubikore n'itegeko:


```bash
gpg --import [key path]
```


Subiriza `[inzira y'urufunguzo]` n'aho dosiye y'urufunguzo rusangi y'umuhinguzi iri.


![GnuPG](assets/notext/08.webp)


Suzuma umukono ukoresheje iri tegeko rikurikira:


```bash
gpg --verify [file.asc]
```


Subiriza `[dosiye.asc]` n'inzira ya dosiye y'umukono. Ku bijanye na Sparrow, iyi dosiye yitwa "*Sparrow-2.0.0-igaragara.txt.asc*" ku verisiyo 2.0.0.


![GnuPG](assets/notext/09.webp)


Niba umukono uriho, GPG izokwereka ivyo. Ushobora rero kuja ku ntambwe ikurikira, kuko ivyo vyemeza ko dosiye ari iyo ukuri.


![GnuPG](assets/notext/10.webp)


## Gusuzuma Hash.

Ubu ko iyo porogarama yemejwe ko ari iyo ukuri, birakenewe kandi ko umuntu asuzuma ko ari iyo ukuri. Tuzogereranya Hash ya porogarama na Hash yatanzwe n’uwayikoze. Iyo ivyo bibiri bihuye, biremeza ko kode ya porogarama itahinduwe.


Ku **Windows**, fungura terminal maze ukore itegeko rikurikira:


```bash
CertUtil -hashfile [file path] SHA256 | findstr /v "hash"
```


Subiriza `[inzira ya dosiye]` n'aho uwushiramwo ari.


![GnuPG](assets/notext/11.webp)


Ico kibanza kizogarura Hash y’ivyo bikoresho vyavuye kuri interineti.


![GnuPG](assets/notext/12.webp)


Menya, kuri porogaramu zimwe zimwe, bishobora kuba ngombwa gukoresha uburyo butandukanye bwa Hash kuruta SHA256. Muri iki gihe, gusa subiriza izina ry'igikorwa ca Hash mw'itegeko.


Hanyuma ugereranye igisubizo n'agaciro kahuye muri dosiye "*Sparrow-2.0.0-manifest.txt*".


![GnuPG](assets/notext/13.webp)


Ku bijanye nanje, turabona ko izo hashes zibiri zihuye neza cane.


Ku **macOS** na **Linux**, uburyo bwo kugenzura Hash burakora. Si ngombwa gusuzuma n’amaboko ukuntu izo hashes zibiri zihuye nk’uko biri kuri Windows.


Gusa shira mu ngiro iri tegeko kuri **macOS**:


```bash
shasum --check [file name] --ignore-missing
```


Subiriza `[izina rya dosiye]` n'izina ry'uwushizeho. Nk’akarorero, ku bijanye na Sparrow wallet:


```bash
shasum --check sparrow-2.0.0-manifest.txt --ignore-missing
```


Niba hashes zihuye, ushobora kubona igisubizo gikurikira:


```bash
Sparrow-2.0.0.dmg: OK
```


Kuri **Linux**, itegeko ni nk'iryo:


```bash
sha256sum --check [file name] --ignore-missing
```


Kandi iyo hashes zihuye, ushobora kubona igisubizo gikurikira:


```bash
sparrow_2.0.0-1_amd64.deb: OK
```


Ubu urazi neza ko porogarama waronse ari iyo ukuri kandi ko ataco ihinduye. Ushobora gukomeza kuyishira ku mashine yawe.


Niwaba wabonye ko iyi nyigisho ari ngirakamaro, noshima ko woshira urukumu hejuru aha hepfo. Ntutinye gusangiza abandi iyi nkuru ku mbuga zanyu zo gusangirirako amakuru. Murakoze cane!


Ndagusavye kandi kuraba iyi yindi nyigisho kuri VeraCrypt, porogarama ishobora kugufasha gupfuka no gufungura ibikoresho vyo kubika.


https://planb.network/tutorials/computer-security/data/veracrypt-d5ed4c83-7c1c-4181-95ea-963fdf2d83c5