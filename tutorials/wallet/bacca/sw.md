---
name: Bacca
description: Inasanidi Ledger bila programu ya Ledger Live
---
![cover](assets/cover.webp)


Ikiwa unatumia Ledger, labda umegundua kwamba unapaswa kupitia programu ya Ledger Live, angalau kwa usanidi wa awali wa kifaa, ili kuangalia uhalisi wake na kusakinisha programu ya Bitcoin juu yake. Walakini, baada ya usanidi huu, bitcoiners wengi wanapendelea kutumia programu maalum ya usimamizi ya Bitcoin Wallet kama vile Sparrow au Liana badala ya Ledger Live. Ingawa Ledger inazalisha pochi bora za maunzi ambazo hujumuisha kwa haraka vipengele vya hivi punde vya Bitcoin, programu yao si lazima ibadilishwe kulingana na mahitaji mahususi ya wapiga bitcoins. Hakika, Ledger Live inajumuisha vipengele vingi vinavyotengenezwa kwa altcoins, wakati chaguo zinazotolewa kwa usimamizi wa Bitcoin Wallet ni mdogo. Lakini tatizo la Sparrow na Liana (kwa sasa), ni kwamba hawakuruhusu kusakinisha programu ya Bitcoin kwenye Ledger.


Ili kukwepa hitaji la kutumia Ledger Live wakati wa usanidi wa awali wa Ledger yako, unaweza kutumia zana ya Bacca, (au "Ledger Installer"). Programu hii hukuruhusu kusakinisha na kusasisha programu ya Bitcoin, kuthibitisha uhalisi wa Ledger yako, na hata baadaye kusasisha programu dhibiti ya kifaa. Bacca iliundwa na Antoine Poinsot (Darosior), msanidi wa Bitcoin Core katika Chaincode Labs, mwanzilishi mwenza [wa Revault na Liana](https://wizardsardine.com/), na Pythcoiner.


Katika somo hili, nitakuonyesha jinsi ya kutumia zana hii, ili uweze kufanya bila programu ya Ledger Live kwa manufaa, na bado kufurahia vifaa vya Ledger. Inafanya kazi kwenye vifaa vyote: Nano S Classic, Nano S Plus, Nano X, Flex na Stax.


---
*Tafadhali kumbuka kuwa zana hii ni mpya kabisa, na wasanidi wake wanabainisha kuwa bado iko **katika awamu ya majaribio**. Wanapendekeza kuitumia kwa madhumuni ya majaribio pekee, na si kwa kifaa kinachokusudiwa kupangisha Bitcoin Wallet halisi, ingawa inawezekana kufanya hivyo. Kuhusiana na hili, ninapendekeza ufuate mapendekezo ya wasanidi wa zana hii, ambayo yamebainishwa [kwenye README ya hazina yao ya GitHub](https://github.com/darosior/ledger_installer).*


---
## Masharti


Kwenye kompyuta yako, utahitaji zana mbili ili kutumia Bacca:




- Git ;
- Rust.


Ikiwa tayari umezisakinisha, unaweza kuruka hatua hii.


**Linux:**


Kwenye usambazaji wa Linux, Git kwa ujumla huwekwa mapema. Kuangalia ikiwa Git imewekwa kwenye mfumo wako, unaweza kuandika amri ifuatayo kwenye terminal :


```bash
git --version
```


Ikiwa huna Git iliyosanikishwa kwenye mfumo wako, hapa kuna amri ya kuisakinisha kwenye Debian :


```bash
sudo apt install git
```


Hatimaye, ili kusakinisha mazingira yako ya ukuzaji ya Rust, tumia amri:


```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```


**Windows:**


Ili kusakinisha Git, nenda kwa [tovuti rasmi ya mradi](https://git-scm.com/). Pakua programu na ufuate maagizo ya usakinishaji.


![BACCA](assets/fr/01.webp)


Endelea kwa njia ile ile ya kusakinisha Rust kutoka [tovuti rasmi](https://www.Rust-lang.org/tools/install).


![BACCA](assets/fr/02.webp)


**MacOS:**


Ikiwa Git haijasanikishwa tayari kwenye mfumo wako, fungua terminal na uendeshe amri ifuatayo ili kuisakinisha:


```bash
git --version
```


Ikiwa Git haijasanikishwa kwenye mfumo wako, dirisha litafungua kukupa kusakinisha Xcode, ambayo inajumuisha Git. Fuata tu maagizo kwenye skrini ili kuendelea na usakinishaji.


Ili kusakinisha Rust, endesha amri ifuatayo:


```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```


## Ufungaji wa Bacca


Fungua terminal na uende kwenye folda ambapo unataka kuhifadhi programu, kisha endesha amri ifuatayo:


```bash
git clone https://github.com/darosior/ledger_installer.git
```


Nenda kwenye saraka ya programu:


```bash
cd ledger_installer
```


Kisha tumia Cargo kuunda mradi na kuendesha Bacca GUI:


```bash
cargo run -p ledger_manager_gui
```


Sasa unaweza kufikia programu ya Interface.


![BACCA](assets/fr/03.webp)


## Kusanidi Ledger


Kabla ya kuanza, ikiwa Ledger yako ni mpya, hakikisha kuwa umeweka msimbo wa PIN na kuhifadhi maneno ya kurejesha akaunti. Huhitaji Ledger Live kwa hatua hizi za mwanzo. Unganisha tu Ledger yako kupitia kebo ya USB ili kuiwasha. Ikiwa huna uhakika jinsi ya kuendelea na hatua hizi mbili, unaweza kurejelea mwanzo wa mafunzo maalum kwa mfano wako:


https://planb.network/tutorials/wallet/hardware/ledger-c6fc7d82-91e7-4c74-bad7-cbff7fea7a88

https://planb.network/tutorials/wallet/hardware/ledger-nano-s-plus-75043cb3-2e8e-43e8-862d-ca243b8215a4

https://planb.network/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a

## Kwa kutumia Bacca


Unganisha Ledger yako kwenye kompyuta yako na uifungue kwa kutumia nambari ya siri uliyoweka. Bacca inapaswa kutambua kiotomatiki Ledger yako.


![BACCA](assets/fr/04.webp)


Ili kuthibitisha uhalisi wa Ledger yako, bofya kitufe cha "*Angalia*". Utahitaji kuidhinisha muunganisho kwenye kifaa chako cha Ledger ili kuendelea.


![BACCA](assets/fr/05.webp)


Bacca itakujulisha ikiwa Ledger yako ni ya kweli. Ikiwa sivyo, hii inaonyesha kuwa kifaa kimeathiriwa, au kwamba ni ghushi. Katika kesi hii, acha kuitumia mara moja.


![BACCA](assets/fr/06.webp)


Katika menyu ya "*Programu*", unaweza kuangalia orodha ya programu ambazo tayari zimesakinishwa kwenye Ledger yako.


![BACCA](assets/fr/07.webp)


Ili kusakinisha programu ya Bitcoin, bofya "*Sakinisha*", kisha uidhinishe usakinishaji kwenye Ledger yako.


![BACCA](assets/fr/08.webp)


Programu imewekwa vizuri.


![BACCA](assets/fr/09.webp)


Iwapo huna toleo jipya zaidi la programu ya Bitcoin iliyosakinishwa, Bacca itaonyesha kitufe cha "*Sasisha*" badala ya kiashiria cha "*Mpya*". Bonyeza tu kwenye kitufe hiki ili kusasisha programu.


![BACCA](assets/fr/10.webp)


Sasa kwa kuwa Ledger yako imesanidiwa ipasavyo kwa toleo jipya zaidi la programu ya Bitcoin, uko tayari kuleta na kutumia Wallet yako kwenye programu ya usimamizi kama vile Sparrow au Liana, bila kulazimika kupitia Ledger Live!


Ikiwa umepata mafunzo haya kuwa ya manufaa, ningeshukuru ikiwa utaacha kidole gumba cha Green hapa chini. Jisikie huru kushiriki nakala hii kwenye mitandao yako ya kijamii. Asante sana!


Ninapendekeza pia uangalie mafunzo haya kwenye GnuPG, ambayo yanaelezea jinsi ya kuangalia uadilifu na uhalisi wa programu yako kabla ya kuisakinisha. Hili ni zoezi muhimu, hasa wakati wa kusakinisha programu ya usimamizi ya Wallet kama vile Liana au Sparrow :


https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc