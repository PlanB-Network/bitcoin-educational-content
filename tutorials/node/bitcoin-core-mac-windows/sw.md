---
name: Bitcoin Core (macOS & Windows)
description: Sakinisha Bitcoin Core kwenye Mac au Windows
---

Kufunga Bitcoin Core kwenye kompyuta yako ya kawaida inaweza kufanywa, lakini sio bora. Ikiwa hujali kuacha kompyuta yako 24/7, basi hii itafanya kazi vizuri. Ikiwa unahitaji kuzima kompyuta, inakera kusubiri programu kusawazisha kila wakati unapoiwasha tena.


Maagizo haya ni kwa Watumiaji wa Mac au Windows. Watumiaji wa Linux hawatahitaji msaada wangu zaidi, lakini maagizo ya Linux yanafanana sana na Mac.


## Anza Safi


Kwa kweli, ungependa kutumia kompyuta safi, isiyo na programu hasidi. Hata kama unatumia Hardware Wallet, programu hasidi inaweza kukuhadaa kutoka kwa sarafu zako.


Unaweza kufuta kabisa kompyuta ya zamani, na uitumie kama kompyuta maalum ya Bitcoin, au ununue kompyuta/laptop iliyojitolea.


## Hifadhi ya Hard


Bitcoin Core itachukua takriban gigabaiti 400 za data kwenye hifadhi yako, na itaendelea kukua. Unaweza kutumia kiendeshi chako cha ndani, lakini pia unaweza ambatisha kiendeshi cha nje cha Hard. Nitaelezea chaguzi zote mbili. Kwa kweli, unapaswa kutumia gari la hali ngumu. Ikiwa una kompyuta ya zamani, labda haina moja ya hizi ndani. Nunua tu SSD ya nje ya terabyte 1 au 2 na utumie hiyo. Hifadhi ya kawaida labda itafanya kazi, lakini unaweza kuishia kuwa na maswala na itakuwa polepole zaidi.


![image](assets/1.webp)


## Pakua Bitcoin Core


Nenda kwa Bitcoin.org (hakikisha huendi Bitcoin.com, ambayo ni tovuti ya shitcoin inayomilikiwa na Roger Ver, inayohadaa watu kununua Bitcoin Cash badala ya Bitcoin)


Mara baada ya hapo, ni ajabu si dhahiri wapi kupata programu. Nenda kwenye menyu ya rasilimali na ubofye "Bitcoin Core", kama inavyoonyeshwa hapa chini:


![image](assets/2.webp)


Hii itakuleta kwenye ukurasa wa kupakua:


![image](assets/3.webp)


Bofya kitufe cha Pakua Bitcoin Core chungwa:


![image](assets/4.webp)


Kuna chaguzi kadhaa za kuchagua, kulingana na kompyuta yako. Mbili za kwanza ni muhimu kwa mwongozo huu; chagua Windows au Mac kwenye upau wa kushoto. Itaanza kupakua baada ya kuibofya, uwezekano mkubwa kwenye saraka yako ya Vipakuliwa.


## Thibitisha upakuaji (sehemu ya 1)


Unahitaji faili ambayo ina heshi ya matoleo mbalimbali. Faili hii ilikuwa kwenye ukurasa wa upakuaji wa Bitcoin.org, lakini sasa imehamia bitcoincore.org/en/download:


![image](assets/5.webp)


Unahitaji faili ya heshi ya binary ya SHA256. Faili hii ina heshi SHA256 za vifurushi mbalimbali vya upakuaji vya Bitcoin Core.


Ifuatayo, tunahitaji kupakua Hash Core ya Bitcoin na kuilinganisha na kile ambacho faili inasema Hash inapaswa kuwa. Kisha tunajua upakuaji ni sawa na kile kinachotarajiwa, kulingana na bitcoincore.org.


Nenda kwenye saraka ya Vipakuliwa tena na utekeleze amri hii (badilisha X na jina la faili la upakuaji la Full node Bitcoin haswa):


```bash
shasum -a 256 XXXXXXXXXXXX # <--- FOR MAC
certutil -hashfile XXXXXXXXXXX SHA256 # <--- FOR WINDOWS
```


Utapata pato la Hash. Iandike, na uilinganishe na Hash iliyo katika faili ya SHA256SUMS.


Ikiwa matokeo yanafanana, basi umethibitisha kuwa hakuna data iliyoingiliwa... karibu. Bado tunahitaji kuhakikisha kuwa faili ya SHA256SUMS si hasidi.


Ili kuendelea na hatua inayofuata, lazima tuwe na gpg iliyosakinishwa kwenye kompyuta yetu.


Ili kufanya hivyo, angalia mwongozo wangu wa SHA256/gpg, na usogeze karibu nusu ya sehemu ya "Pakua gpg", na utafute kichwa kidogo cha mfumo wako wa kufanya kazi. Kisha urudi hapa.


## Pata Ufunguo wa Umma


Ukirudi kwenye ukurasa wa upakuaji, pata faili ya sahihi ya SHA256 Hash


![image](assets/6.webp)


Bofya na uhifadhi faili kwenye diski, ikiwezekana saraka ya Upakuaji.


Faili hii ina saini za watu mbalimbali, za faili ya SHA256SUMS.


Tunataka ufunguo wa umma wa msanidi programu mkuu, Wladimir J. van der Laan kwenye kitufe cha kompyuta yetu. Kitambulisho chake cha ufunguo wa umma ni:

1 - 01EA 5486 DE18 A882 D4C2 6845 90C8 019E 36C2 E964


Nakili maandishi hayo kwa amri ifuatayo:


```bash
gpg --keyserver hkp://keyserver.ubuntu.com --recv-keys 01EA5486DE18A882D4C2684590C8019E36C2E964
```


Kwa kupendeza, wakati wowote, unaweza kuona ni vitufe gani vilivyo kwenye ufunguo wa kompyuta na amri hii:


```bash
gpg --list-keys
```


## Thibitisha upakuaji (sehemu ya 2)


Tuna ufunguo wa umma, kwa hivyo tunaweza kuthibitisha faili ya SHA256SUMS ambayo ina heshi za upakuaji wa Bitcoin Core, na saini ya heshi hizo.


Fungua Kituo au CMD tena, na uhakikishe kuwa uko kwenye saraka ya Vipakuliwa. Kutoka hapo, toa amri hii:


```bash
gpg –verify SHA256SUMS.asc SHA256SUMS
```


Faili ya kwanza iliyoorodheshwa ni tahajia halisi ya faili sahihi. Faili ya pili iliyoorodheshwa inapaswa kuwa tahajia halisi ya faili ya maandishi iliyo na heshi. Faili zote mbili zinapaswa kuwa kwenye saraka sawa na unahitaji kuwa kwenye saraka ya faili, vinginevyo, itabidi uandike njia kamili kwa kila faili.


Hili ndilo pato unapaswa kupata


![image](assets/7.webp)


Ni salama kupuuza ujumbe wa ONYO - hilo linakukumbusha tu kwamba hujakutana na Wladimir kwenye sehemu muhimu na ukamuuliza kibinafsi ufunguo wake wa umma ni nini, na kisha ukaiambia kompyuta yako kuamini ufunguo huu kabisa.


Iwapo ulipata ujumbe huu, sasa unajua kuwa faili ya SHA256SUMS.asc haijachezewa baada ya Wladimir kutia saini.


## Weka Bitcoin Core


Haupaswi kuhitaji maagizo ya kina juu ya jinsi ya kusanikisha programu.


![image](assets/8.webp)


## Endesha Bitcoin Core


Kwenye Mac, unaweza kupata onyo (Apple bado inapinga Bitcoin)


![image](assets/9.webp)


Bonyeza Sawa, na kisha ufungue Mapendeleo ya Mfumo wako


![image](assets/10.webp)


Bofya ikoni ya Usalama na Faragha:


![image](assets/11.webp)


Kisha bofya "fungua hata hivyo":


![image](assets/12.webp)


Hitilafu itaonekana tena, lakini wakati huu utakuwa na kitufe cha FUNGUA. Bofya.


![image](assets/13.webp)


Bitcoin Core inapaswa kupakia na utawasilishwa na chaguzi kadhaa:


![image](assets/14.webp)


Hapa unaweza kuchagua kutumia njia chaguo-msingi ambapo Blockchain itapakuliwa, au unaweza kuchagua hifadhi yako ya nje. Ninapendekeza usibadilishe njia chaguo-msingi ikiwa utatumia hifadhi ya ndani, hurahisisha mambo kusanidi unaposakinisha programu nyingine ili kuwasiliana na Bitcoin Core.


Unaweza kuchagua kuendesha nodi iliyokatwa, inaokoa nafasi, lakini inapunguza kile unachoweza kufanya na nodi yako. Vyovyote vile, utakuwa unapakua Blockchain nzima na kuithibitisha hata hivyo, kwa hivyo ikiwa una nafasi, weka ulichopakua, na usikate ikiwa unaweza kuiepuka.


Baada ya kuthibitisha, Blockchain itaanza kupakua. Itachukua siku nyingi.


![image](assets/15.webp)


Unaweza kuzima kompyuta na kurudi kupakua ikiwa unataka, haitafanya uharibifu wowote.