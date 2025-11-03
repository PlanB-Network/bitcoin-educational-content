---
name: LN VPN

description: Gushiraho LN VPN n'umuravyo ku VPN itazwi kandi isaba
---

![image](assets/cover.webp)


LN VPN ni umukozi wa VPN ushobora guhindurwa wemera gusa amahera y’umuravyo. Uyu musi, nzokwereka ingene woyikoresha kandi ugasiga ibimenyetso bike iyo uriko urarondera ama interwebs.


Hariho abatanga ubuhinga bwa VPN benshi, kandi twakoze isuzuma ry’ibintu vyose muri iyi nkuru (hyperlink). Ariko rero, LN VPN iratandukanye, kandi ntitwashobora gutakaza akaryo ko kubamenyesha.


Benshi mu batanga ubuhinga bwa VPN nka ProtonVPN na Mullvad batanga uburenganzira bwo kwishura n’amahera ya bitcoins ariko bisaba gukora konti no kugura umugambi w’igihe kirekire canke gito, ivyo bishobora kutajanye n’ingengo y’imari y’umuntu wese.


LN VPN ishoboza gukoresha VPN ku vyo usaba mu gihe gito nk’isaha imwe, bivuye ku gushirwa mu ngiro kwayo kw’ukwishurwa kwa Bitcoin biciye ku Lightning Network. Ivyishyurwa vy’umuravyo bihita kandi bitamenyekana, bifungura isi y’ubushobozi bwo kwishura bike.


Iciyumviro💡: **Iyi nkuru idondora ingene ukoresha LN VPN ukoresheje ubuhinga bwa Linux Ubuntu 22.04 LTS.**


## Ibisabwa: Umurinzi w'intsinga


Mu majambo yoroshe, Wireguard ikoreshwa mu gukora umugende utekanye hagati ya mudasobwa yawe na server iri kure uzocamwo kugira ngo ukoreshe Internet. Ni IP Address y’iyi server izoboneka nk’iyawe mu kiringo cose c’ubukode uzokoresha Contract ukurikije iyi nsiguro.


Inyigisho yemewe yo gushiramwo Wireguard: https://www.wireguard.com/shiramwo/


```
Wireguard installation
$ sudo apt-get update
$ sudo apt install wireguard
```


## Ibisabwa: Umuravyo Bitcoin Wallet


Niba utararonka Lightning Bitcoin Wallet, ntuhagarike umutima, twagukoreye uburongozi bworoshe cane hano. (igice c’inyigisho za LN kirashobora kugufasha)


## Intambwe ya 1: Contract ubukode


Kuva kuri https://lnvpn.com, uzokenera guhitamwo igihugu IP y’isohoka ry’umugende wa VPN n’igihe uzomara. Ivyo bipimo bimaze gushirwaho, ukande kuri Pay with lightning.


![image](assets/1.webp)


Umuravyo Invoice uzokwerekanwa, kandi ukeneye gusa kuwucapura n'umuravyo wawe Wallet.


Invoice imaze kwishurwa, uzokenera kurindira amasegonda makeyi gushika ku minota ibiri kugira ngo amasetingi yawe y’imiterere ya Wireguard aboneke. Nivyafata igihe gitoyi, ntimuhagarike umutima, iyo nzira twayikoze incuro amajana, kandi rimwe na rimwe bifata igihe kirekire gusa.

Icanditswe gikurikira carahinduwe mu congereza mu gihe cagumye gifise uburyo bwo gushiramwo ikimenyetso nk’icanditswe c’intango:


Igishushanyo gikurikira kizoboneka kandi ubwirizwa gusa gukanda kuri "Download as File" kugira ngo ubone dosiye yawe ya config, izogira izina risa na lnvpn-xx-xx.conf aho "xx" izohuye n'itariki uriko urakoresha.

![image](assets/2.webp)


## Intambwe ya 2: Gukoresha umugende


Ubwa mbere, uzokenera guhindura izina rya dosiye ya config waronse mu ntambwe iheze kugira ngo ishobore kumenyekana ubwayo na Wireguard.


Genda muri dosiye yawe yo gukuraho, haba mw'idirisha ry'iherezo canke n'umushakashatsi wa dosiye, hanyuma uhindure izina rya dosiye lnvpn-xx-xx.conf uyihindure wg0.conf nk'ibi:


```
$ sudo ln -s usrbin/resolvectl usrlocal/bin/resolvconf
$ sudo wg-quick up ~/Downloads/wg0.conf
```


Ni ho rero! Ico kinogo kirakora!


## Intambwe ya 3: Suzuma


Koresha service yo kuri internet nka whatismyip kugira ngo umenye neza ko IP yawe ya bose Address ubu ari iyo iva kuri VPN uherutse gukoresha.


## Intambwe ya 4: Guhagarika


Igihe ubukode bwawe buzoba burangiye, uzokenera guhagarika iyo nzira kugira ngo wongere ukoreshe internet. Ushobora rero gusubiramwo intambwe 1 gushika ku 3 igihe cose ushaka gushinga ubukode na LN VPN.


Zima umugende:


```
$ sudo ip link delete dev wg0
```


Aho ni ho ufise! Ubu urazi gukoresha LN VPN, ni igikorwa kidasanzwe ca VPN!