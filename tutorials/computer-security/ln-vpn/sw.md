---
name: LN VPN

description: Sanidi VPN yako
---

![image](assets/cover.webp)


LN VPN ni huduma ya VPN inayoweza kubinafsishwa ambayo inakubali malipo ya umeme pekee. Leo, nitakuonyesha jinsi ya kuitumia na kuacha alama chache wakati wa kuvinjari miingiliano.


Kuna watoa huduma wengi wa ubora wa VPN, na tumefanya mapitio ya kina katika makala hii (hyperlink). Hata hivyo, LN VPN ni ya kipekee, na hatukuweza kukosa fursa ya kuitambulisha kwako.


Watoa huduma wengi wa VPN kama ProtonVPN na Mullvad hutoa chaguo la kulipa kwa bitcoins lakini wanahitaji kuunda akaunti na kununua mpango kwa muda mrefu au mfupi, ambao unaweza kutoshea bajeti ya kila mtu.


LN VPN huwezesha matumizi ya VPN unapohitaji kwa muda wa saa moja, kutokana na utekelezaji wake wa malipo ya Bitcoin kupitia Lightning Network. Malipo ya papo hapo na yasiyojulikana, ya umeme hufungua ulimwengu wa uwezekano wa malipo madogo.


Kumbuka💡: **Mwongozo huu unaeleza jinsi ya kutumia LN VPN kutoka kwa mfumo wa Linux Ubuntu 22.04 LTS.**


## Mahitaji: Wireguard


Kwa maneno rahisi, Wireguard hutumiwa kuunda handaki salama kati ya kompyuta yako na seva ya mbali ambayo kupitia kwayo utavinjari Mtandao. Ni IP Address ya seva hii ambayo itaonekana kama yako kwa muda wa kukodisha utakayotumia Contract kwa kufuata mwongozo huu.


Mwongozo rasmi wa usakinishaji wa Wireguard: https://www.wireguard.com/install/


```
Wireguard installation
$ sudo apt-get update
$ sudo apt install wireguard
```


## Mahitaji: Umeme Bitcoin Wallet


Ikiwa bado huna Lightning Bitcoin Wallet, hakuna wasiwasi, tumekuundia mwongozo rahisi sana hapa. (sehemu ya mafunzo ya LN inaweza kukusaidia)


## Hatua ya 1: Contract ya Kukodisha


Kutoka https://lnvpn.com, utahitaji kuchagua nchi ya kuondoka kwa IP ya handaki ya VPN na muda. Mara tu vigezo hivi vimewekwa, bofya Lipa kwa umeme.


![image](assets/1.webp)


Invoice ya umeme itaonyeshwa, na unahitaji tu kuichanganua kwa umeme wako wa Wallet.


Mara baada ya Invoice kulipwa, utahitaji kusubiri kwa sekunde chache hadi dakika mbili ili mipangilio yako ya usanidi ya Wireguard itengenezwe. Ikichukua muda mrefu zaidi, usiogope, tumefanya utaratibu huu mara kadhaa, na wakati mwingine inachukua muda mrefu zaidi.

Maandishi yafuatayo yametafsiriwa kwa Kiingereza huku ikidumisha mpangilio sawa wa alama kama maandishi asilia:


Skrini inayofuata itatokea na itabidi ubofye tu "Pakua kama Faili" ili kupokea faili yako ya usanidi, ambayo itakuwa na jina linalofanana na lnvpn-xx-xx.conf ambapo "xx" italingana na tarehe ya sasa.

![image](assets/2.webp)


## Hatua ya 2: Washa handaki


Kwanza, utahitaji kubadilisha jina la faili ya usanidi iliyopatikana katika hatua ya awali ili iweze kutambuliwa kiotomatiki na Wireguard.


Nenda kwenye folda yako ya upakuaji, ama kwenye kidirisha cha mwisho au na kichunguzi cha faili, na ubadilishe jina la faili ya lnvpn-xx-xx.conf kuwa wg0.conf kama hii:


```
$ sudo ln -s usrbin/resolvectl usrlocal/bin/resolvconf
$ sudo wg-quick up ~/Downloads/wg0.conf
```


Haya basi! Mfereji umewashwa!


## Hatua ya 3: Thibitisha


Tumia huduma ya mtandaoni kama whatismyip ili kuthibitisha kwamba IP yako ya umma ya Address sasa ndiyo kutoka kwa VPN ambayo umewasha hivi punde.


## Hatua ya 4: Zima


Muda wa kukodisha kwako unapoisha, utahitaji kuzima muunganisho ili kurejesha ufikiaji wa mtandao. Kisha unaweza kurudia hatua ya 1 hadi 3 wakati wowote unapotaka kuanzisha ukodishaji na LN VPN.


Zima handaki:


```
$ sudo ip link delete dev wg0
```


Hapo unayo! Sasa unajua jinsi ya kutumia LN VPN, huduma ya kipekee ya VPN!