---
name: Kituo cha Ashigaru
description: Tumia Ashigaru kwenye eneo-kazi ili kutengeneza viunga
---

![cover](assets/cover.webp)



Ashigaru Terminal ni urekebishaji wa timu ya Ashigaru wa Seva ya Sparrow, ambayo hutekeleza itifaki ya Whirlpool sanjari. Programu hii ni mwendelezo wa kazi iliyoanzishwa na Samourai Wallet, haswa kwenye Whirlpool GUI, ambayo kanuni zake za msingi inakubali: kujitunza na kuhifadhi usiri.



Programu hii ni fork ya Seva ya Sparrow, iliyorekebishwa na kuboreshwa ili kuunganishwa kikamilifu na mfumo ikolojia wa Whirlpool, itifaki sanjari ya ZeroLink iliyoanzishwa awali na timu za Samourai.



Kituo cha Ashigaru kinafanya kazi kutoka kwa kiolesura cha TUI cha kiwango kidogo na kinaweza kutumwa kwenye kompyuta ya kibinafsi au kwenye seva maalum. Inakuruhusu kuingiliana moja kwa moja na Whirlpool ili kuanzisha "*Tx0*", kudhibiti akaunti za "*Amana*", "*Premix*", "*Postmix*" na "*Badbank*", na kufanya michanganyiko ya kiotomatiki ili kuimarisha usiri wa sehemu zako.



Kwa kifupi, Kituo cha Ashigaru kitakuwa muhimu sana ikiwa unataka kuunda coinjoins kwa kutumia Whirlpool.



Katika somo hili la kwanza, nitakupeleka kupitia usakinishaji na uendeshaji wa Ashigaru Terminal. Mafunzo ya pili, ya kina zaidi yatatolewa kwa uundaji halisi wa satifu.



https://planb.academy/tutorials/privacy/on-chain/ashigaru-whirlpool-e566803d-ab3f-4d98-9136-5462009262ef

## 1. Weka Ashigaru Terminal



Ili kusakinisha Kituo cha Ashigaru, utahitaji Kivinjari cha Tor, kwani jozi hizo husambazwa tu kupitia mtandao wa Tor. Ikiwa bado hujafanya hivyo, [isakinishe kwenye mashine yako](https://www.torproject.org/download/).



### 1.1. pakua Ashigaru Terminal



Kutoka kwa Kivinjari cha Tor, nenda kwa [ukurasa wa matoleo ya hazina yao ya Git](http://ashicodepbnpvslzsl2bz7l2pwrjvajgumgac423pp3y2deprbnzz7id.onion/Ashigaru/Ashigaru-Terminal/releases/) ili kupakua toleo jipya zaidi la Mfumo wako wa uendeshaji wa Ashiga.



```txt
ashicodepbnpvslzsl2bz7l2pwrjvajgumgac423pp3y2deprbnzz7id.onion/Ashigaru/Ashigaru-Terminal/releases/
```



![Image](assets/fr/01.webp)



Pakua faili 2 zifuatazo za mfumo wako wa kufanya kazi:




- Mfumo wa jozi (`ashigaru_terminal_v1.0.0_amd64.deb` kwa Debian/Ubuntu, `.dmg` kwa macOS au `.zip` kwa Windows);
- Faili ya heshi iliyotiwa saini: `ashigaru_terminal_v1.0.0_signed_hashes.txt`.



### 1.2. Angalia Kituo cha Ashigaru



Kabla ya kuendesha programu kwenye kifaa chako, unahitaji kuangalia uhalisi na uadilifu wake. Hii ni hatua muhimu, kwani hukuzuia kusakinisha toleo la ulaghai ambalo linaweza kuhatarisha bitcoins zako au kuambukiza mashine yako.



Fungua kichupo kipya cha kivinjari na uende kwenye [zana ya uthibitishaji wa msingi](https://keybase.io/verify). Bandika yaliyomo kwenye faili ya `.txt` ambayo umepakua kwenye sehemu iliyotolewa, kisha ubofye kitufe cha `Thibitisha`.



![Image](assets/fr/02.webp)



Ili kubadilisha vyanzo vyako vya uthibitishaji, unaweza pia kulinganisha ujumbe na ule unaopatikana kwenye tovuti ya clearnet [ashigaru.rs](https://ashigaru.rs/download/), katika sehemu ya `/kupakua`.



![Image](assets/fr/03.webp)



Ikiwa sahihi ni halali, Keybase itaonyesha ujumbe unaothibitisha kuwa faili imetiwa saini na wasanidi wa Ashigaru.



![Image](assets/fr/04.webp)



Unaweza pia kubofya wasifu wa `ashigarudev` unaoonyeshwa na Keybase na uangalie kuwa alama zao za vidole zinalingana kabisa : `A138 06B1 FA2A 676B`.



![Image](assets/fr/05.webp)



Ikiwa hitilafu inaonekana katika hatua hii, sahihi ni batili. Katika kesi hii, ** usisakinishe programu iliyopakuliwa **. Anza tena tangu mwanzo, au iombe jumuiya usaidizi kabla ya kuendelea.



Keybase imekupa heshi iliyothibitishwa ya programu. Sasa tutaangalia kwamba heshi ya `.deb`, `.zip` au `.dmg` faili ambayo umepakua inalingana na ile iliyoidhinishwa kwenye Keybase. Ili kufanya hivyo, nenda kwenye [HASH FILE ONLINE](https://hash-file.online/).



Bofya kitufe cha `BROWSE...` na uchague faili ya `.deb`, `.zip` au `.dmg` iliyopakuliwa katika hatua ya 1.1. Kisha chagua chaguo za kukokotoa za `SHA-256`, na ubofye `CALCULATE HASH` hadi generate heshi ya faili yako.



![Image](assets/fr/06.webp)



Tovuti hiyo itaonyesha heshi ya programu. Linganisha na heshi uliyoithibitisha kwenye Keybase.io. Ikiwa zote mbili zinalingana kikamilifu, ukaguzi wa uhalisi na uadilifu umefaulu. Kisha unaweza kutumia programu.



![Image](assets/fr/07.webp)



### 1.3 Zindua Kituo cha Ashigaru





- Debian / Ubuntu



Ili kusakinisha programu, endesha amri:



```bash
cd ~/Downloads
sudo apt install ./ashigaru_terminal_v1.0.0_amd64.deb
```



Badilisha mpangilio kulingana na toleo lililopakuliwa.



Kisha angalia usakinishaji:



```bash
/opt/ashigaru-terminal/bin/Ashigaru-terminal --version
```



Kisha uzindua programu:



```bash
/opt/ashigaru-terminal/bin/Ashigaru-terminal
```





- Windows**



Bofya kulia kwenye faili ya `.zip` uliyopakua na kukagua, kisha uchague `Nyoa Zote...` ili kutoa yaliyomo.



Uchimbaji ukikamilika, bofya mara mbili kwenye faili ya `Ashigaru-terminal.exe` ili kuzindua programu.



![Image](assets/fr/08.webp)



## 2. Kuanza na Ashigaru Terminal



Kituo cha Ashigaru ni programu ya TUI (*Mtumiaji Interface* inayotegemea Maandishi), yaani, kiolesura cha chini kabisa kinachofanya kazi moja kwa moja kwenye terminal. Unaingiliana nayo kwa kutumia menyu na mikato ya kibodi, lakini bila mazingira halisi ya picha ya kawaida.



![Image](assets/fr/09.webp)



Ni rahisi kutumia: tumia vitufe vya vishale vya kibodi yako kusogeza kwenye menyu, na ubonyeze kitufe cha `Enter` ili kuthibitisha kitendo au kuthibitisha chaguo.



## 3. Kuunganisha nodi yako kwenye Kituo cha Ashigaru



Kwa chaguo-msingi, Kituo cha Ashigaru huunganisha kwa seva ya umma ya Electrum. Hii ni dhahiri inatoa hatari katika suala la usiri na uhuru. Kwa hivyo tutaisanidi ili kuunganisha moja kwa moja kwa Electrum Server yako mwenyewe.



Ili kufanya hivyo, fungua menyu ya `Mapendeleo > Seva`.



![Image](assets/fr/10.webp)



Bonyeza kitufe cha `< Hariri >`.



![Image](assets/fr/11.webp)



Chagua `Faragha Electrum Server`, kisha ubofye `<Endelea>`.



![Image](assets/fr/12.webp)



Ingiza URL na mlango wa seva yako. Unaweza kubainisha anwani ya Tor katika `.onion`. Kisha ubofye `< Jaribio >` ili kuthibitisha muunganisho.



![Image](assets/fr/13.webp)



Ikiwa muunganisho umefaulu, ujumbe `Mafanikio` utaonekana, pamoja na maelezo ya seva yako.



![Image](assets/fr/14.webp)



Ikiwa bado huna nodi ya Bitcoin, ninapendekeza uchukue kozi hii:



https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426

*Kwa upande wangu, kwa mafunzo haya, nitatenganisha kutoka kwa seva yangu ya Electrs kwa sababu ninafanya kazi kwenye testnet. Hata hivyo, operesheni inasalia kuwa sawa kwenye mainnet.*



## 4. Unda kwingineko kwenye Kituo cha Ashigaru



Sasa kwa kuwa programu imeundwa kwa usahihi, tunaweza kuongeza kwingineko ya Bitcoin.



Una chaguzi mbili:




- Unaweza kuunda wallet mpya kutoka mwanzo na uitumie kwenye Kituo cha Ashigaru pekee. Katika kesi hii, utahitaji kufungua programu hii kila wakati unapotaka kuingiliana na wallet yako;
- Vinginevyo, unaweza kuleta Ashigaru wallet yako iliyopo moja kwa moja kutoka kwa simu yako hadi kwenye Kituo cha Ashigaru. Ubaya wa njia hii ni kwamba inapunguza kidogo usalama wa usanidi wako, kwani wallet yako inaonyeshwa mazingira mawili hatari badala ya moja. Kwa upande mwingine, inatoa faida ya kuweza kuondoka Ashigaru Terminal ikiendelea ili kuchanganya sarafu zako, huku ikikuruhusu kuzitumia ukiwa mbali kupitia programu ya simu ya Ashigaru.



Katika somo hili, tutachagua njia ya pili. Hata hivyo, ikiwa ungependelea kuunda kwingineko mpya kabisa, utaratibu unasalia uleule: tofauti pekee itakuwa wakati wa uundaji, wakati utahitaji kuhifadhi maneno yako mapya ya mnemonic na passphrase yako mpya.



Pia kumbuka kuwa Ashigaru Terminal hairuhusu kutumia bitcoins zako moja kwa moja. Unaweza kusawazisha pochi ile ile kwenye Ashigaru Terminal na programu ya Ashigaru (ambayo nitafanya katika mafunzo haya), au kwenye Sparrow Wallet.



Ikiwa bado huna wallet kwenye programu ya Ashigaru, unaweza kufuata mafunzo maalum:



https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f

Nenda kwenye menyu ya `Pochi`.



![Image](assets/fr/15.webp)



Kisha chagua `Unda/rejesha wallet...`. Chaguo la `Fungua Wallet...` hukuwezesha kufikia kwingineko ambayo tayari imehifadhiwa kwenye Kituo cha Ashigaru hapo baadaye.



![Image](assets/fr/16.webp)



Ipe kwingineko yako jina.



![Image](assets/fr/17.webp)



Kisha chagua aina ya kwingineko `Hot Wallet`.






![Image](assets/fr/18.webp)



Ni katika hatua hii kwamba utaratibu hutofautiana kulingana na chaguo lako la awali:




- Iwapo ungependa kuunda jalada jipya kutoka mwanzo, bofya `<Tengeneza Wallet Mpya>`, fafanua passphrase BIP39, kisha uhifadhi kwa makini kifungu chako cha maneno ya mnemonic na passphrase yako kwenye nyenzo halisi ;



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270



- Iwapo ungependa kutumia wallet sawa na programu yako ya Ashigaru, weka maneno 12 ya maneno yako ya mnemonic na passphrase BIP39 yako moja kwa moja kwenye sehemu zinazolingana. Andika maneno kwa herufi ndogo, nzima, kwa mpangilio, ikitenganishwa na nafasi, bila nambari au herufi za ziada.



Mara tu hatua hii ikikamilika, bofya `< Inayofuata >`.



*Kumbuka*: Ikiwa huwezi kubofya kitufe hiki, kishazi chako cha kumbukumbu ni batili. Angalia kwa uangalifu kwamba hakuna neno moja ambalo si sahihi au limeandikwa vibaya.



![Image](assets/fr/19.webp)



Kisha utahitaji kuweka nenosiri. Hii itatumika kufungua Kituo chako cha Ashigaru wallet na kukilinda dhidi ya ufikiaji wa kimwili ambao haujaidhinishwa. Haihusiki katika derivation ya kriptografia ya funguo zako: kwa maneno mengine, hata bila nenosiri hili, mtu yeyote aliye na maneno yako ya mnemonic na passphrase ataweza kurejesha wallet yako na kufikia bitcoins zako.



Chagua nenosiri refu, ngumu, nasibu. Weka nakala mahali salama: haswa kwenye njia halisi au katika kidhibiti salama cha nenosiri.



Bofya `< SAWA >` ukimaliza.



![Image](assets/fr/20.webp)



## 5. Kutumia kwingineko



Kisha unaweza kuchagua ni akaunti gani ya kufikia. Kwa sasa, hatujaanzisha michanganyiko yoyote, kwa hivyo tutafikia akaunti ya `Amana`.



![Image](assets/fr/21.webp)



Operesheni basi inafanana na ile ya Sparrow, kwa kuwa Kituo cha Ashigaru ni fork ya Seva ya Sparrow. Utapata menyu sawa:



![Image](assets/fr/22.webp)





- miamala": inakuruhusu kutazama historia ya miamala iliyounganishwa kwenye akaunti hii. Kwa upande wangu, baadhi yao tayari yanaonekana, kama nilivyofanya kwa kutumia ombi la Ashigaru kwenye wallet hii hiyo.



![Image](assets/fr/23.webp)





- receive`: hutengeneza anwani mpya ya stakabadhi tupu ya kuweka satss kwenye akaunti ya amana.



![Image](assets/fr/24.webp)





- anwani`: huonyesha orodha ya anwani zako zote, ziwe ni za msururu wa ndani au nje wa akaunti yako.



![Image](assets/fr/25.webp)





- `UTXOs`: huorodhesha UTXO zako zote zinazopatikana.



![Image](assets/fr/26.webp)





- `Mipangilio`: inatoa ufikiaji wa kwingineko *kielezi* chako. Unaweza pia kushauriana na seed yako, kurekebisha *Kikomo cha Pengo* au kubadilisha tarehe ya kuunda kwingineko yako.



![Image](assets/fr/27.webp)



Sasa unajua jinsi ya kusakinisha na kutumia Ashigaru Terminal. Katika mafunzo yajayo, tutaona jinsi ya kufanya coinjoin kwa programu hii na jinsi ya kusimamia fedha katika "*Postmix*".
https://planb.academy/tutorials/privacy/on-chain/ashigaru-whirlpool-e566803d-ab3f-4d98-9136-5462009262ef
