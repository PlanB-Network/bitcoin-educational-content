---
name: Whonix
description: Hifadhi faragha na usiri wako.
---

![cover](assets/cover.webp)



**Whonix** ni usambazaji wa Linux kulingana na **Debian**, iliyoundwa ili kutoa mazingira yanayochanganya **usalama**, **kutokujulikana** na **faragha**. Rahisi kujifunza, na inaoana na violesura tofauti (mashine pepe, Qubes OS, Hali ya Moja kwa Moja), inajumuisha kwa uelekezaji chaguo-msingi wa trafiki wa mtandao kupitia **Tor**, **firewall mara mbili** (ngozo moja kwenye Lango na nyingine kwenye Kituo cha Kazi), **ulinzi kamili dhidi ya uvujaji wa IP/DNS** na zana za kuficha shughuli zako kwa waangalizi wa mtandao, ikijumuisha kwa ufanisi waangalizi wa ISP. Zaidi ya mfumo usiojulikana, **Whonix** ni mazingira salama kabisa ya maendeleo.



## Kwa nini kuchagua Whonix?





- Bila malipo**: Kama ugawaji mwingi wa Linux, Whonix ni mfumo wa chanzo huria uliopewa leseni bila malipo kabisa. Inatengenezwa katika chanzo wazi, na jumuiya inayofanya kazi na ya uwazi.
- Faragha, usalama na kutokujulikana**: Lengo kuu la Whonix ni kutoa mazingira salama kabisa, ambapo data yako yote inalindwa na mawasiliano yako yamesimbwa kwa njia fiche kupitia mtandao wa Tor.
- Rahisi kutumia**: Whonix inatoa angavu, iliyosanidiwa awali ya Interface, inayofaa hata kwa watumiaji wapya. Hakuna haja ya kuwa mtaalam ili kufaidika na ulinzi wa hali ya juu.
- Mazingira yanayofaa kwa maendeleo salama**: Whonix hukuruhusu kuunda, kujaribu, kukagua au kuendesha programu bila kamwe kufichua IP yako halisi ya Address au kufichua tabia zako za kuvinjari au mawasiliano ya mtandao.
- Vipindi vinavyoweza kutumika na Hali ya Moja kwa Moja**: Whonix inaweza kuzinduliwa katika Hali ya Moja kwa Moja au kupitia mashine zinazoweza kutumika (k.m. kupitia **Qubes OS**), kuwezesha majukumu muhimu kutekelezwa bila kuacha ufuatiliaji unaoendelea punde tu kipindi kitakapokamilika.
- Usakinishaji rahisi kiasi**: Picha zilizo tayari kutumika hutolewa kwa usakinishaji wa haraka katika mashine pepe (VirtualBox, KVM, Qubes). Mfumo umeandikwa na kusasishwa mara kwa mara.



## Ufungaji na usanidi



Kabla ya kuendelea na usakinishaji wa Whonix, ni muhimu kutambua kwamba usambazaji huu **bado haujapatikana rasmi** kama mfumo mkuu unaoweza kusakinishwa moja kwa moja kwenye diski ya Hard (katika hali ya chuma tupu). Kwa maneno mengine, **bado huwezi kusakinisha Whonix kama mfumo wa uendeshaji wa seva pangishi**, kama vile Ubuntu au Debian ya kawaida.



Hata hivyo, matoleo kadhaa yanapatikana, na kuruhusu Whonix kutumika **tete** (Hali ya moja kwa moja, vipindi vya muda) au **inayoendelea** (kupitia mashine pepe au ujumuishaji katika Qubes OS).



Kwa matumizi ya muda mrefu, thabiti, **utumiaji mtandaoni ndio njia pekee inayopendekezwa rasmi**. Unaweza kuendesha Whonix kwa kutumia **VirtualBox** (Whonix-Gateway na Whonix-Workstation) au kuiunganisha kwenye mfumo kama **Qubes OS**. Katika somo hili, tutazingatia usakinishaji wa VirtualBox.



### Masharti



Kabla ya kusakinisha Whonix katika hali pepe, hakikisha kwamba mashine yako inatimiza mahitaji ya chini zaidi ya kiufundi. Virtualization inahitaji rasilimali fulani ambazo sio kompyuta zote zinaweza kutoa. Kwa hivyo ni muhimu kwamba kichakataji chako kikubali teknolojia ya uboreshaji (Intel VT-x au AMD-V), na kwamba chaguo hili limewezeshwa katika BIOS/UEFI.



Hapa kuna vipimo vilivyopendekezwa vya matumizi laini na dhabiti na Whonix:





- Kumbukumbu ya Ufikiaji Nasibu (RAM)**: kiwango cha chini cha **GB** kinapendekezwa sana. Kadiri unavyokuwa na RAM zaidi, ndivyo rasilimali nyingi unavyoweza kutenga kwa mashine pepe (Lango na Kituo cha Kazi), kuboresha utendaji.
- Nafasi ya diski inayopatikana**: tafadhali ruhusu angalau GB 30 ya nafasi ya bure ya diski**. Hii inajumuisha nafasi inayohitajika kwa mashine mbili pepe, faili za mfumo na data au vijipicha vyovyote.
- Kichakataji**: kichakataji chenye angalau **viini 4** (nyuzi 8 za kimantiki) kinapendekezwa, haswa ikiwa unataka kuendesha huduma au zana zingine kwa sambamba.



### Pakua Whonix



Whonix inapatikana katika matoleo kadhaa, kulingana na aina ya mazingira unayotaka kuitumia. Kwa watumiaji wengi (Windows, Linux au MacOs), toleo la VirtualBox ndilo rahisi zaidi kusanidi. Unaweza kupakua picha moja kwa moja kutoka [tovuti rasmi](https://www.whonix.org/wiki/VirtualBox).



⚠️ Whonix **haioani** na MacBook zinazotumia vichakataji vya Apple Silicon (usanifu wa ARM).



## Inaweka VirtualBox



Ili kuendesha Whonix, utahitaji **hypervisor** kama VirtualBox, Qubes au KVM.



Mara tu unapopakua faili, isakinishe kama ungefanya programu nyingine yoyote. Kubali chaguo-msingi isipokuwa kama una mahitaji maalum. Je, umepotea? Angalia mwongozo wetu wa kutumia VirtualBox.



https://planb.network/tutorials/computer-security/operating-system/virtualbox-6472f5be-10ce-4a07-8b24-097bfbcedd65
### Inaleta Whonix



Baada ya VirtualBox kusakinishwa, unaweza kuleta faili za Whonix `.ova` ulizopakua awali (`Whonix-Gateway-Xfce.ova` na `Whonix-Workstation-Xfce.ova`).



Fungua VirtualBox, kisha ubofye kwenye **Faili → Ingiza kifaa **.


Chagua faili inayolingana ya `.ova` (anza na Lango).



![0_03](assets/fr/03.webp)



Chagua mahali ambapo faili za mashine pepe ya Whonix zitahifadhiwa.



![0_04](assets/fr/04.webp)



Kubali masharti ya matumizi, kisha uzindue uletaji na usubiri mchakato ukamilike.



![0_05](assets/fr/05.webp)



![0_06](assets/fr/06.webp)


### Usanidi wa Whonix



Kabla ya kuanza Whonix, ni muhimu kurekebisha baadhi ya **mipangilio ya mfumo** ili kuhakikisha utendakazi bora:



Chagua mashine pepe ya **Whonix-Workstation-Xfce**, kisha ubofye **Usanidi**.



![0_06](assets/fr/07.webp)



Nenda kwenye kichupo cha **Mfumo**, ambapo mgao chaguomsingi wa RAM ni 2048 MB. Tunapendekeza **uiongeze hadi 4096 MB (GB 4)** kwa usaidizi zaidi, hasa ikiwa unanuia kufungua programu kadhaa au kufanya kazi kwa vipindi virefu. Lango linaweza kubaki 2048 MB, isipokuwa unatumia miunganisho mingi ya Tor sambamba.



![0_08](assets/fr/08.webp)



### Anza na Whonix



Ili Whonix ifanye kazi vizuri na kwa usalama, **ni lazima ufuate mlolongo huu wa uanzishaji**:



Kwanza, anza mashine ya **Whonix-Gateway-Xfce**. Mashine hii inawajibika kuelekeza trafiki yote kupitia mtandao wa **Tor**. Bila lango linaloendelea, hakuna trafiki itakayopitishwa kupitia Tor na utapoteza jina lako litajwe.



![0_09](assets/fr/09.webp)



Mara Lango litakapozinduliwa kikamilifu (utaona Tor imeunganishwa), unaweza kuanza **Whonix-Workstation-Xfce**, ambayo itaunganishwa kiotomatiki kupitia Lango.



![0_10](assets/fr/10.webp)



![0_11](assets/fr/11.webp)



### Sasisho la mfumo



Ingiza terminal, weka amri ifuatayo ili kusasisha orodha ya vifurushi:



```shell
sudo apt update
```



Kisha endesha amri ifuatayo ili kusasisha sasisho zinazopatikana:



```shell
sudo apt full-upgrade
```



## Gundua Whonix



**Whonix** ni mfumo ulioundwa ili kutoa mazingira ya kompyuta **salama**, **bila jina** na **siri**, bora kwa kutumia Intaneti bila kuhatarisha utambulisho wako au data yako. Ili kufanikisha hili, inakuja na idadi ya programu muhimu za kila siku zilizoundwa ili kuimarisha usalama wako wa kidijitali tangu mwanzo.


### KeepassXC



**KeePassXC** ni kidhibiti jumuishi cha nenosiri cha Whonix. Inakuruhusu **kuunda, kuhifadhi na kudhibiti** manenosiri yako kwa usalama, bila kulazimika kuyakumbuka yote wewe mwenyewe. Nenosiri huhifadhiwa katika **database iliyosimbwa kwa njia fiche**, iliyolindwa na nenosiri kuu.



### Kivinjari cha Tor



**Tor Browser** ni kivinjari chaguo-msingi cha Whonix. Inategemea mtandao wa **Tor**, ambao huelekeza upya trafiki yako kupitia relay kadhaa duniani, hivyo kufanya iwe vigumu kutambua IP yako halisi ya Address.



https://planb.network/tutorials/computer-security/communication/tor-browser-a847e83c-31ef-4439-9eac-742b255129bb

### Electrum Bitcoin Wallet



**Electrum** ni Bitcoin Wallet nyepesi na ya haraka, iliyosakinishwa awali kwenye Whonix ili kukuruhusu kudhibiti **miamala ya cryptocurrency** bila kujulikana. Haipakui Blockchain nzima lakini hutumia seva za mbali kupata habari muhimu, na kuifanya iwe nyepesi zaidi kuliko Wallet kamili.



https://planb.network/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177

Whonix ni zaidi ya mfumo wa uendeshaji tu: ni **mazingira salama** yaliyoundwa ili kulinda kutokujulikana kwako, faragha yako na shughuli zako nyeti. Shukrani kwa usanifu wake unaotegemea Tor, ugawaji wa akili kati ya Gateway na Workstation, na zana zilizosakinishwa awali kama vile Tor Browser, KeePassXC na Electrum, inatoa suluhisho la ufunguo wa kugeuza kwa yeyote anayetaka **kuvinjari bila kujulikana**, **kufanya kazi kwa usalama** au **kushughulikia data ya siri**.



Ili kuimarisha usalama wako kwenye mfumo wako wa Unix, angalia mafunzo yetu kuhusu kukagua mashine yako: angalia mashimo ya usalama kwenye mfumo wako wa uendeshaji na uhakikishe kuwa data yako haijaathirika.



https://planb.network/tutorials/computer-security/operating-system/lynis-1cf865b3-a352-4dd2-94d2-f17fa65547af