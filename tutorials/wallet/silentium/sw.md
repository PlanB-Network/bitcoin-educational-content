---
name: Silentium
description: wallet ya wavuti inayoendelea yenye usaidizi wa Malipo ya Kimya (BIP-352)
---

![cover](assets/cover.webp)



Matumizi tena ya anwani za Bitcoin ni mojawapo ya vitisho vya moja kwa moja kwa usiri wa mtumiaji. Mpokeaji anaposhiriki anwani moja ili kupokea malipo mengi, mtazamaji yeyote anaweza kufuatilia miamala yote inayohusiana na kujenga upya historia yake ya kifedha. Tatizo hili huathiri hasa waundaji wa maudhui, mashirika ya kutoa misaada au wanaharakati wanaotaka kuonyesha hadharani anwani ya michango bila kuhatarisha faragha yao.



Silentium hujibu tatizo hili kwa suluhisho maridadi linalopatikana moja kwa moja kutoka kwa kivinjari chako. Programu hii ya wavuti inayoendelea ya chanzo huria (PWA), iliyozinduliwa Mei 2024 na Louis Singer, inatekeleza Malipo ya Kimya (BIP-352): anwani tuli inayoweza kutumika tena ambapo kila malipo huishia kwenye anwani tofauti ya blockchain, bila mwingiliano wa awali au kiungo kinachoonekana kati ya miamala.



**Onyo muhimu**: Silentium ni mradi wa majaribio unaotumika kama *uthibitisho wa dhana* kwa wallet nyepesi za Malipo ya Kimya. Haipaswi kutumika kama wallet ya kila siku au kwa kuhifadhi kiasi kikubwa. Wasanidi programu wanasema waziwazi:



> Tumia kwa hatari yako mwenyewe.

Kumbuka kwamba wallet hii inaweza kutumika kama jaribio la majaribio au jaribio la kawaida.



## Silentium ni nini?



### Falsafa na malengo



Silentium hutumika kama onyesho la kiufundi la kutekeleza Malipo ya Kimya katika kivinjari chepesi cha wallet. Ingawa pia inasaidia anwani za kawaida za Bitcoin, msisitizo uko kwenye Malipo ya Kimya ili kuwawezesha watumiaji kujaribu teknolojia hii ya faragha kwa njia rahisi.



### Malipo ya Kimya hufanyaje kazi?



Malipo ya Kimya (BIP-352) hutumia Ufunguo wa Elliptic Curve Diffie-Hellman Exchange (ECDH). Mpokeaji hutoa anwani tuli (`sp1...` kwenye mainnet, `tsp1...` kwenye testnet) inayojumuisha funguo mbili za umma: ufunguo wa kuchanganua ili kugundua malipo, na ufunguo wa kutumia ili kuyatumia.



Mtumaji huchanganya funguo zake za kuingiza data binafsi na ufunguo wa kuchanganua wa mpokeaji ili kuhesabu siri iliyoshirikiwa inayozalisha "tweak" ya kimtandao. Urekebishaji huu, ulioongezwa kwenye ufunguo wa matumizi, huunda anwani ya kipekee ya Taproot kwa kila muamala. Mpokeaji huiga tena hesabu hii kwa ufunguo wake wa kuchanganua data binafsi ili kugundua na kutumia pesa bila mwingiliano wowote wa awali.



Faida: usiri ulioimarishwa kwa mtumaji na mpokeaji, hakuna seva ya mtu wa tatu inayohitajika, miamala isiyoweza kutofautishwa na malipo ya kawaida ya Taproot. Hasara kuu: uchanganuzi wa kina wa blockchain ili kugundua malipo.



Ili kujua zaidi kuhusu utendaji kazi wa kinadharia wa Malipo ya Kimya, tazama sehemu ya mwisho ya kozi ya BTC,204 kuhusu Plan ₿ Academy:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Mifumo inayoungwa mkono



Silentium ni Programu ya Wavuti Inayoendelea (PWA) inayopatikana kutoka kwa kivinjari chochote cha kisasa (simu ya mkononi au kompyuta ya mezani). Itumie moja kwa moja kwenye `app.silentium.dev`, isakinishe kama programu asilia kupitia kivinjari chako, au itumie ndani. Usakinishaji unafanywa moja kwa moja kutoka kwa kivinjari, bila kupitia maduka rasmi.



## Kutumia Programu ya Wavuti



### Ufikiaji na usakinishaji



[Nenda kwenye `https://app.silentium.dev/` kutoka kwa kivinjari chako](https://app.silentium.dev/). Programu hupakia papo hapo na kuonyesha skrini ya nyumbani.



Ili kuisakinisha kama programu asilia kwenye iOS, bonyeza kitufe cha kushiriki (mraba wenye mshale unaoelekea juu) kisha uchague "Kwenye skrini ya nyumbani". Kwenye Android, kivinjari kwa kawaida hutoa arifa ya "Ongeza kwenye skrini ya nyumbani" moja kwa moja. Mara tu ikiwa imewekwa, Silentium inaonekana na aikoni yake maalum na inafanya kazi kama programu asilia, lakini inahitaji muunganisho wa intaneti ili kusawazisha miamala.



![Installation de Silentium comme PWA sur iOS](assets/fr/01.webp)



### Uundaji wa kwingineko



Katika uzinduzi wa kwanza, chagua "Unda Wallet" ili kutoa wallet mpya, au "Rejesha Wallet" ili kurejesha kutoka kwa kifungu cha urejeshaji kilichopo.



Chagua "Unda Wallet". Programu hutoa kifungu cha maneno 12 ambacho lazima uandike kwa uangalifu. Kifungu hiki cha maneno ndiyo njia pekee ya kurejesha pesa zako. Hata kwenye testnet, fuata mbinu nzuri za kuhifadhi nakala rudufu. Bonyeza "Endelea" baada ya kuhifadhi kifungu chako cha maneno.



Kisha programu inakuomba uweke nenosiri ili kupata ufikiaji salama wa wallet. Chagua nenosiri thabiti na ulithibitishe.



![Création d'un nouveau wallet avec phrase de récupération](assets/fr/02.webp)



Mara tu kifungu cha maneno kitakapothibitishwa na nenosiri limewekwa, utaelekezwa kwenye kiolesura kikuu.



### Vigezo vikuu na Interface



Kiolesura kikuu kinaonyesha salio lako katika satoshis (hapo awali 0 sats), na vifungo vitatu chini:




- Sawazisha**: husawazisha wallet na blockchain
- Pokea**: kupokea fedha
- Tuma**: kutuma bitcoins



Fikia Mipangilio kupitia aikoni iliyo juu kulia (mipau mitatu ya mlalo). Menyu ya Mipangilio inatoa chaguo kadhaa:





- Kuhusu**: taarifa ya maombi
- Hifadhi nakala rudufu**: kifungu cha nakala rudufu cha urejeshaji
- Kichunguzi**: chagua kichunguzi cha blockchain (kwa chaguo-msingi Mempool) na seva ya Silentiumd
- Mtandao**: uteuzi wa mtandao (mainnet/testnet)
- Nenosiri**: badilisha nenosiri
- Pakia upya**: kupakia upya wallet
- Weka upya**: kamilisha kuweka upya
- Mandhari**: badilisha mandhari



![Interface principale et paramètres avec Explorer](assets/fr/03.webp)



Sehemu ya **Explorer** ni muhimu sana: hukuruhusu kuchagua kichunguzi cha blockchain kinachotumika (Mempool kwa chaguo-msingi) na pia huonyesha URL ya seva ya Silentiumd (`https://bitcoin.silentium.dev/v1` kwa mainnet). Ukihifadhi seva yako ya Silentiumd au unataka kutumia testnet, hapa ndipo unaposanidi vigezo hivi.



### Kupokea fedha



Kutoka kwenye kiolesura kikuu, bonyeza kitufe cha "Pokea". Kwa chaguo-msingi, Silentium huonyesha anwani ya Malipo ya Kimya yenye msimbo wake wa QR. Anwani huanza na `sp1...` kwenye mainnet au `tsp1...` kwenye testnet.



Unaweza kubadilisha kati ya anwani za Malipo ya Kimya na anwani za kawaida za Bitcoin kwa kutumia kitufe cha "Badilisha hadi anwani ya kawaida" / "Badilisha hadi anwani ya kimya" chini ya skrini.



![Réception de fonds avec Silent Payment et adresse classique](assets/fr/04.webp)




Mara tu muamala utakapotangazwa, tafadhali subiri dakika chache. Kwa Malipo ya Kimya, Silentium huchanganua kiotomatiki blockchain kwa miamala inayokusudiwa wewe. Miamala huonekana ikiwa na hali ya "Haijathibitishwa" kabla ya kuthibitishwa hatua kwa hatua.



### Tuma malipo



Kutoka kwenye kiolesura kikuu, bonyeza kitufe cha "Tuma". Skrini ya kutuma itakuuliza:



1. **Address**: bandika anwani ya Malipo ya Kimya (`sp1...` au `tsp1...`) au anwani ya kawaida ya Bitcoin. Unaweza kutumia aikoni ya uchanganuzi wa QR kuchanganua anwani.


2. **Kiasi**: ingiza kiasi katika satoshi zitakazotumwa. Kibodi cha nambari kinaonyeshwa kwa urahisi wa kuingiza. Salio lako linalopatikana linaonyeshwa juu kwa marejeleo.



![Envoi de fonds depuis Silentium](assets/fr/05.webp)



Ukishaingiza anwani na kiasi, bonyeza "Endelea" ili kuendelea. Programu itakuomba uchague kiwango cha ada unachotaka kabla ya kuthibitisha muamala.



## wallet inayojiendesha yenyewe



### Kwa nini mwenyeji binafsi?



Uhifadhi wa ndani wa Silentium hutoa uhuru kamili, uthibitishaji wa msimbo, mazingira ya maendeleo na ustahimilivu wakati wa hitilafu za tovuti rasmi.



### Masharti ya awali



Node.js (toleo la 14+), npm au uzi, Git, na takriban nafasi ya diski ya MB 500.



### Usakinishaji wa ndani



Badilisha hazina na usakinishe:



```bash
git clone https://github.com/louisinger/silentium.git
cd silentium
yarn install
```



### Zindua na utumie



Anza programu katika hali ya usanidi:



```bash
yarn start
```



Nenda kwenye `http://localhost:3000` kwenye kivinjari chako. Kwa toleo bora la uzalishaji:



```bash
yarn build
```



Faili zinazozalishwa katika `build/` zinaweza kutumiwa na nginx, Apache au seva yoyote ya wavuti. Kwa chaguo-msingi, Silentium huunganishwa na seva ya umma ya `bitcoin.silentium.dev`. Rekebisha mpangilio huu katika vigezo ili kutumia testnet au seva yako mwenyewe.



## Seva ya Silentiumd



### Jukumu na uendeshaji



Silentium hutumia seva ya uorodheshaji ya **Silentiumd** ili kuboresha ugunduzi wa malipo. Kuchanganua miamala yote ya Taproot itakuwa ngumu sana kwa kivinjari au simu ya mkononi.



Silentiumd huhesabu mapema data ya kati (tweaks) kwa kila muamala wa Taproot. wallet yako hupakua marekebisho haya (baiti chache kwa kila muamala) na kufanya hesabu ya mwisho ndani ya eneo, ikithibitisha umiliki wa malipo. Seva haijui kamwe funguo zako au inaweza kutambua miamala yako, tofauti na seva za kawaida za Electrum.



Vichujio vidogo vya BIP158 huruhusu wallet yako kubaini ni vitalu vipi vya kuchanganua bila kufichua anwani zako, hivyo kuhifadhi usiri wako.



### Seva ya umma



Seva ya umma `bitcoin.silentium.dev` (mainnet), inayofadhiliwa na Vulpem Ventures, inatoa uzoefu rahisi na wa haraka. Ingawa usiri huhifadhiwa, mbinu hii inaashiria imani ya kiasi katika miundombinu ya wahusika wengine.



### Panga seva yako ya Silentiumd



Kwa uhuru kamili, weka seva yako ya Silentiumd. Mahitaji ya awali: Nodi ya Bitcoin Core isiyo na elagged yenye `txindex=1` na `blockfilterindex=1`, Go 1.21+, nafasi ya diski ya GB 10-20, ujuzi wa usimamizi wa mfumo.



**Ufungaji:**



```bash
git clone https://github.com/louisinger/silentiumd.git
cd silentiumd
make build
./build/silentium-[OS]-[ARCH]
```



Sanidi kupitia vigezo vya mazingira (tazama `config.md` ya hazina kwa maelezo zaidi). Seva huweka blockchain kwenye faharasa na kufichua API ambayo inaweza kuulizwa na wallet yako.



Hakuna suluhisho zilizofungashwa za Umbrel au Start9 zilizopo kwa sasa, na hivyo kupunguza ufikiaji kwa watumiaji wasio wa kiufundi.



## Faida na mapungufu



### Vivutio





- Ufikiaji wa kiwango cha juu**: matumizi kutoka kwa kivinjari chochote, hakuna usakinishaji mzito unaohitajika
- Mifumo mingi**: inafanya kazi kwenye simu (Android/iOS) na kompyuta ya mezani kutokana na teknolojia ya PWA
- Uhifadhi rahisi wa kibinafsi**: usakinishaji wa ndani unawezekana kwa amri chache
- Chanzo huria**: msimbo unaoweza kukaguliwa kikamilifu kwenye GitHub
- Inalenga faragha**: hakuna ufuatiliaji, hakuna uchanganuzi, hesabu za kriptografia za ndani
- Usanifu tofauti**: utenganisho wazi kati ya wallet (mteja) na seva ya uorodheshaji
- Bila akaunti**: hakuna usajili au data binafsi inayohitajika



### Vikwazo vya kuzingatia





- Mradi wa majaribio**: uthibitisho wa dhana pekee, haukusudiwa matumizi ya kila siku au uzalishaji
- Hakuna dhamana**: hatari ya hitilafu, udhaifu, uwezekano wa kupoteza fedha
- Usaidizi mdogo**: nyaraka ndogo za watumiaji, jumuiya ndogo, hakuna usaidizi rasmi
- Utegemezi wa seva**: inahitaji seva ya Silentiumd inayofanya kazi (ya umma au inayojiendesha yenyewe)
- Uchanganuzi wa kina**: Ugunduzi wa Malipo Kimya hutumia kipimo data
- Utendaji uliopunguzwa**: hakuna udhibiti wa sarafu, hakuna umeme, hakuna asili za multi-sig



## Mbinu bora



### Usalama wa seed



Hata kwenye testnet, chukua kifungu chako cha urejeshaji kwa uzito. Kiandike na ukiweke mahali salama. Weka wallet tofauti kwa testnet na mainnet: usitumie kamwe seed ya jaribio kwenye wallet iliyokusudiwa kwa fedha halisi.



### Uthibitishaji wa msimbo chanzo



Mojawapo ya faida za kujipangia programu ni uwezo wa kuangalia msimbo chanzo kabla ya kuuendesha. Ikiwa unapanga kutumia Silentium kwa pesa halisi, chukua muda kukagua msimbo au pata msanidi programu anayeaminika kufanya hivyo. Pia linganisha hash ya msimbo uliowekwa kwenye `app.silentium.dev` na ule wa hazina ya GitHub ili kuhakikisha uhalisi.



### Hifadhi nakala rudufu na urejeshaji



Urejeshaji wa fedha za Malipo ya Kimya unahitaji wallet inayoendana na itifaki ya BIP-352. wallet ya kawaida haiwezi kuchanganua blockchain ili kurejesha Malipo yako ya Kimya ya UTXO. Weka Silentium ikiwa imewekwa au hakikisha una ufikiaji wa wallet nyingine inayoendana (kama vile Cake Wallet au utekelezaji mwingine wa siku zijazo) ili kurejesha fedha zako ikiwa ni lazima.



## Hitimisho



Silentium hutoa eneo la majaribio linaloweza kupatikana kwa ajili ya kuelewa Malipo ya Kimya bila msuguano wa kiufundi. Kama uthibitisho wa dhana, inaonyesha jinsi teknolojia hii ya faragha inaweza kuunganishwa kwenye kivinjari cha wallet huku ikihifadhi uangalizi wa kibinafsi. Jaribu kwenye testnet ili kugundua mafanikio haya ya kuahidi kwa faragha ya on-chain.



## Rasilimali



### Nyaraka rasmi




- Silentium Hifadhi ya GitHub (wallet): https://github.com/louisinger/silentium
- Silentiumd Hifadhi ya GitHub (seva): https://github.com/louisinger/silentiumd
- Programu ya wavuti: https://app.silentium.dev/
- Tovuti ya jumuiya ya Malipo ya Kimya: https://silentpayments.xyz
- Vipimo BIP-352: https://bips.dev/352



### Makala na rasilimali




- Tangazo rasmi (Twitter): https://x.com/TheSingerLouis/status/1790824126472667227
- NoBS Bitcoin: https://www.nobsbitcoin.com/silentium-silent-payments/
- Bitcoin Optech - Malipo ya Kimya: https://bitcoinops.org/en/topics/silent-payments/



### Vifaa vya Testnet




- Bomba la Testnet: https://testnet-faucet.com/
- Kichunguzi cha Mempool testnet: https://mempool.space/testnet