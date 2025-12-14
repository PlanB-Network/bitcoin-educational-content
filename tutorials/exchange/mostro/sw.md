---
name: Mostro
description: Jukwaa la kubadilishana la Bitcoin P2P lisilo na KYC kupitia Umeme na Nostr
---

![cover](assets/cover.webp)



Je, unapata au kuuza vipi bitcoins bila kuathiri uhuru wako wa kifedha? Mifumo ya serikali kuu huweka taratibu vamizi za KYC kufichua data yako ya kibinafsi, kukiwa na uwezekano wa kufungia akaunti kiholela au ufuatiliaji wa serikali.



**Mostro P2P** inatoa mbadala uliogatuliwa unaochanganya Lightning Network, itifaki ya Nostr na kushikilia ankara. Ubunifu wake mkuu: mfumo wa otomatiki wa escrow ambapo bitcoins zako hubaki chini ya udhibiti wako wakati wote wa kubadilishana, kuondoa hatari ya wizi, kufilisika kwa kubadilishana au kunyang'anywa kiholela.



## Mostro P2P ni nini?



Mostro P2P ni itifaki ya ubadilishanaji ya Bitcoin ya chanzo huria iliyoundwa na **grunch**, msanidi programu maarufu wa Telegram bot **lnp2pbot** iliyozinduliwa mwaka wa 2021. Ingawa lnp2pbot tayari imewasha ubadilishanaji wa P2P bila KYC kupitia Umeme, iliwasilisha hatari kubwa: **Telegramu imeshindwa kwa sababu* za mawasiliano ya simu. serikali.



Mostro inawakilisha **mageuzi yaliyogatuliwa** ya dhana hii: kwa kubadilisha Telegramu na itifaki ya **Nostr** (mtandao usiopimika wa relay zinazosambazwa), Mostro huondoa hatari hii ya kimfumo. Itifaki inachanganya Lightning Network kwa miamala ya papo hapo, Nostr kwa mawasiliano yanayokinza udhibiti, na **kushikilia ankara** ili kuunda escrow ya kiotomatiki isiyolindwa.



### Usanifu wa kiufundi



Mostro hufanya kazi kupitia vipengele vitatu:




- Daemon Mostrod**: huratibu ubadilishanaji kati ya watumiaji na Lightning Network
- Umeme** nodi: huunda ankara za kushikilia (~24h kriptografia escrow)
- Wateja wengi**: miingiliano ya mtumiaji (CLI, Simu ya Mkononi, Wavuti)



Maagizo huchapishwa kwenye Nostr kama matukio ya umma (aina 38383), huku biashara za kibinafsi zikitumwa kupitia ujumbe uliosimbwa kutoka mwisho hadi mwisho (NIP-59, NIP-44). Kila mfano wa Mostro hufafanua ada zake (kwa ujumla kati ya 0.3% na 1%) na mipaka ya muamala (kuanzia elfu chache hadi laki kadhaa za sats, kulingana na mfano).



### Faida za kuamua



**Inakinza udhibiti**: Hakuna serikali inayoweza kuzima Mostro mradi tu relay za Nostr zipo mahali fulani ulimwenguni. Tofauti na lnp2pbot walio katika mazingira magumu kupitia Telegram, Mostro inaruhusu ubadilishanaji ambao ni **ushahidi wa udhibiti**.



**Escrow isiyo ya ulinzi**: Ankara za kushikilia umeme hufunga bitcoins zako bila kuzihamisha kabisa. Pesa zako zitasalia chini ya udhibiti wako na hurudishwa kwako kiotomatiki kukitokea tatizo (~24h).



**Usiri kwa muundo**: Njia mbili zinapatikana ili kukidhi mahitaji yako. Hali ya Sifa** inaunganisha sifa yako na ufunguo wako wa Nostr ili kujenga uaminifu wa kudumu. Hali Kamili ya Faragha** inapendelea kutokujulikana kabisa kwa kutumia vitufe vya muda mfupi tu.



## Sifa kuu



**Mawasiliano yaliyogatuliwa**: Maagizo yote yanachapishwa kwenye Nostr kupitia matukio yaliyotiwa saini kwa njia fiche. Mazungumzo ya faragha hupitishwa kupitia ujumbe uliosimbwa kutoka mwisho hadi mwisho, unaohakikisha usiri kamili.



**Mfumo wa sifa**: Ukadiriaji wa nyota 5 na hesabu ya kurudia iliyohifadhiwa kabisa kwenye Nostr. Inakuruhusu kujenga sifa polepole kama mfanyabiashara anayeaminika.



**Usuluhishi wa madaraka**: Katika tukio la mgogoro, msuluhishi asiyependelea huchunguza ushahidi na kutoa uamuzi kwa kuzingatia vigezo vya uwazi. Kila mzozo hutoa token ya kipekee kwa ufuatiliaji.



**Ubadilikaji wa malipo**: Usaidizi wa sarafu nyingi za fiat kupitia huduma ya kiwango cha ubadilishaji yadio.io. Inakubali uhamishaji wa SEPA, PayPal, Revolut, pesa taslimu na njia yoyote iliyokubaliwa kati ya wahusika.



## Wateja wengi wanapatikana



Mostro hutoa wateja wawili wakuu wa kufanya kazi kwa mabadilishano yako ya P2P.



### Mostro CLI - Mteja wa Line ya Amri



**Mostro CLI** ndiye mteja aliyekomaa na amilifu zaidi. Imeandikwa katika Rust, inatoa anuwai kamili ya vipengele vya Mostro kupitia kiolesura cha mstari wa amri. Inapatana na macOS, Linux na Windows.



**Vidhibiti kuu** :




- `listorders`: Onyesha maagizo yote yanayopatikana
- `neworder` : Unda agizo jipya la kununua au kuuza
- `takesell` / `takebuy`: Chukua agizo la kununua au kuuza
- `fiatsent`: Thibitisha utumaji wa malipo ya fiat
- `kutolewa`: Achilia escrow na ukamilishe kubadilishana
- `getdm`: Tazama ujumbe wa moja kwa moja
- `kiwango` : Tathmini mshirika wako baada ya kubadilishana



Inafaa kwa watumiaji wa kiufundi, otomatiki na mazingira yanayohitaji usalama wa hali ya juu.



### Mostro Mobile - Programu ya simu mahiri



**programu ya simu ya mkononi** katika toleo la alpha huwezesha biashara ya P2P moja kwa moja kutoka kwa simu yako mahiri. Mchoro angavu wa Interface iliyo na urambazaji kwa vichupo, utazamaji wa mpangilio, vichujio vya hali ya juu na gumzo iliyojumuishwa ili kuwasiliana na wenzako.



Inapatikana kwa **Android** (kupitia APK kwenye GitHub), ni chaguo bora zaidi kwa watumiaji wanaopendelea urahisi na biashara ya mara kwa mara ya rununu.



### Wavuti nyingi - Interface wavuti (inatengenezwa)



Utumizi wa juu wa JavaScript wa Interface chini ya usanidi amilifu. Imeundwa ili kutoa uzoefu kamili wa mtumiaji na utendaji wa kina wa biashara na usimamizi wa kwingineko. Fikia kupitia kivinjari bila usakinishaji unaohitajika.



## Ufungaji na usanidi



Mafunzo haya yatakuongoza kupitia usakinishaji na matumizi ya wateja wakuu wawili wa Mostro: CLI na programu ya simu.



### Masharti muhimu



Kabla ya kuanza, utahitaji:





- Lightning Network** wallet inayofanya kazi yenye ukwasi wa kutosha (au inayoendana na Umeme)
 - Imependekezwa: Phoenix, Breez, Wallet ya Satoshi...
 - Kiwango cha chini cha satoshis 1000 za ukwasi kupima



https://planb.academy/tutorials/wallet/mobile/phoenix-0f681345-abff-4bdc-819c-4ae800129cdf



- Kitufe cha kibinafsi cha Nostr** (umbizo `nsec1...`)
 - Unda ufunguo maalum wa biashara kwenye [nostrkeygen.com](https://nostrkeygen.com/)
 - Muhimu**: Kamwe usitumie kitufe chako kikuu cha kibinafsi cha Nostr
 - Weka ufunguo wako wa faragha mahali salama (kidhibiti cha nenosiri)





- Hiari lakini inapendekezwa**: Muunganisho wa VPN au Tor ili kuficha anwani yako ya IP



https://planb.academy/tutorials/computer-security/communication/mullvad-968ec5f5-b3f0-4d23-a9e0-c07a3e85aaa8

### Ufungaji wa Mostro CLI



#### Kwenye macOS



**Hatua ya 1: Angalia Rust**



Angalia kuwa Rust imesakinishwa (toleo la 1.64+ linahitajika):



```bash
rustc --version
```



Ikiwa Rust haijasakinishwa :



```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source $HOME/.cargo/env
```



**Hatua ya 2: Kufunga hazina**



```bash
git clone https://github.com/MostroP2P/mostro-cli.git
cd mostro-cli
```



![Vérification Rust et clonage](assets/fr/01.webp)



**Hatua ya 3: Usanidi**



Nakili na uhariri:



```bash
cp .env-sample .env
```



Fungua `.env` na usanidi mipangilio yako:



```bash
# Public key of the Mostro instance (choose an instance)
# Main mainnet instance (recommended):
MOSTRO_PUBKEY='npub1ykvsmrmw2hk7jgxgy64zr8tfkx4nnjhq9eyfxdlg3caha3ph0skq6jr3z0'
# Alternative/test instance:
# MOSTRO_PUBKEY='npub19m9laul6k463czdacwx5ta4ap43nlf3lr0p99mqugnz8mdz7wtvskkm5wg'

# Your Nostr private key dedicated to trading
NSEC_PRIVKEY='nsec1votre_cle...'

# List of Nostr relays (use the same ones as the mobile app for synchronization)
RELAYS='wss://nos.lol,wss://relay.damus.io,wss://nostr-pub.wellorder.net,wss://nostr.mutinywallet.com,wss://relay.nostr.band'

POW='0'
```



**Muhimu kwa ulandanishi wa CLI/Simu**: Ili kufikia maagizo sawa kwenye CLI na programu ya simu, ni lazima utumie **kifunguo hicho cha Mostro Pubkey** na **relay sawa za Nostr** katika wateja wote wawili. Angalia mipangilio hii katika Mipangilio kwenye programu ya simu.



![Configuration .env](assets/fr/02.webp)



**Hatua ya 4: Usakinishaji**



Kukusanya na kusakinisha CLI :



```bash
cargo install --path .
```



Mkusanyiko huchukua dakika 1-2. `Mostro-cli` inayoweza kutekelezeka itasakinishwa katika `~/.cargo/bin/`.



![Installation du CLI](assets/fr/03.webp)



**Hatua ya 5: Angalia**



Angalia kuwa kila kitu kinafanya kazi:



```bash
mostro-cli --help
```



Unapaswa kuona orodha kamili ya maagizo.



![Vérification avec --help](assets/fr/04.webp)



#### Kwenye Linux (Ubuntu/Debian)



Ufungaji sawa na macOS, na nyongeza ya:



```bash
sudo apt update
sudo apt install -y cmake build-essential pkg-config
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source $HOME/.cargo/env
git clone https://github.com/MostroP2P/mostro-cli.git
cd mostro-cli
cargo build --release
```



Kisha fuata hatua 3 na 4 katika sehemu ya macOS.



#### Kwenye Windows



Kwanza sakinisha Rust kupitia [rustup.rs](https://rustup.rs/), kisha utumie PowerShell :



```powershell
git clone https://github.com/MostroP2P/mostro-cli.git
cd mostro-cli
cargo build --release
```



Usanidi sawia: nakili `.env-sample` kwa `.env` na ujaze vigezo vyako.



### Inasakinisha Mostro Mobile



#### Kwenye Android



**Hatua ya 1**: Nenda kwenye [ukurasa wa matoleo ya GitHub](https://github.com/MostroP2P/mobile/releases) na upakue faili ya **app-release.apk** (takriban MB 65).



![Page GitHub Releases](assets/fr/10.webp)



**Hatua ya 2: Baada ya kupakuliwa, fungua faili ya APK kutoka kwa vipakuliwa vyako. Android itakuuliza uidhinishe usakinishaji kutoka kwa chanzo hiki.



![Téléchargement et installation APK](assets/fr/11.webp)



**Hatua ya 3**: Fuata skrini za kuabiri, zinazowasilisha utendakazi:




- Biashara Bitcoin kwa uhuru - hakuna KYC**: Biashara bila uthibitishaji wa utambulisho shukrani kwa Nostr
- Faragha kwa chaguo-msingi**: Chagua kati ya Hali ya Sifa na Hali Kamili ya faragha
- Usalama katika kila hatua**: Ulinzi na ankara zisizo za kizuizini



![Écrans d'accueil Mostro](assets/fr/12.webp)



**Hatua ya 4**: Endelea kuabiri ili kugundua :




- Gumzo lililosimbwa kwa njia fiche kikamilifu**: Mawasiliano yaliyosimbwa kutoka mwisho hadi mwisho
- Pata ofa**: Vinjari kitabu cha agizo na uchague ofa
- Je, hupati unachohitaji?** : Unda mpangilio wako uliobinafsishwa



![Suite onboarding](assets/fr/13.webp)



**Hatua ya 5: Uingizaji unapokamilika, programu hutengeneza kiotomatiki jozi za funguo za Nostr. Nenda kwenye menyu (☰) kisha **Akaunti** ili kuhifadhi **Maneno yako ya Siri** (maneno ya kurejesha akaunti). Pia ni kwenye skrini hii ambapo una chaguo la kubadilisha hali ya faragha iliyotajwa hapo awali.



![Menu et sauvegarde des clés](assets/fr/15.webp)



**Muhimu**: Andika kifungu chako cha maneno cha urejeshi mahali salama (kidhibiti cha nenosiri, salama ya karatasi).



### Usanidi wa awali wa usalama



Unatumia jukwaa lolote:





- Ufunguo maalum**: Tumia kitambulisho tofauti cha Nostr kufanya biashara
- Kiasi kidogo**: Anza na chini ya sats 10,000 ili kuanza
- Relay nyingi**: Sanidi relay 3-5 tofauti za kijiografia
- Ulinzi wa mtandao**: Washa VPN au Tor ili kuficha anwani yako ya IP
- Wallet salama**: Washa kufunga kiotomatiki kwa Umeme wako wa wallet



## Tumia na CLI



Sehemu hii inaonyesha ununuzi wa bitcoins kupitia Mostro CLI kufuatia hali halisi ya matumizi.



### Hatua ya 1: Orodhesha maagizo yanayopatikana



Amri ya `listorders` inaonyesha maagizo yote amilifu:



```bash
mostro-cli listorders
```



Utaona jedwali lenye maelezo ya kila agizo: kitambulisho, aina (nunua/uza), kiasi, sarafu, njia ya kulipa.



![Liste des ordres disponibles](assets/fr/05.webp)



Katika mfano huu, agizo la kuuza EUR 5 kupitia Revolut linaonekana (Kitambulisho: `305a59d0-dbee-4880-9b9a-44a60486ba4a`).



### Hatua ya 2: Kuchukua agizo



Ili kununua bitcoins hizi, chukua agizo na `takesell` :



```bash
mostro-cli takesell -o 305a59d0-dbee-4880-9b9a-44a60486ba4a
```



Mostro itakuomba utoe ** ankara ya umeme** ili kupokea BTC. Kiasi halisi katika satoshis kinaonyeshwa (hapa: 4715 sats).



![Prise d'ordre de vente](assets/fr/06.webp)



### Hatua ya 3: Toa ankara yako ya Umeme



Tengeneza ankara ya umeme kutoka kwa wallet yako (Phoenix, Breez, n.k.) kwa kiasi kamili, kisha utume:



```bash
mostro-cli takesell -o 305a59d0-dbee-4880-9b9a-44a60486ba4a --invoice lnbc47150n1p...
```



Mfumo unathibitisha usafirishaji na kukuambia umngoje muuzaji alipe ankara ya muda kabla ya kuwezesha malipo ya malipo.



![Envoi de la Lightning invoice](assets/fr/07.webp)



### Hatua ya 4: Wasiliana na muuzaji



Mara tu escrow ikiwashwa, tumia `dmtouser` kuomba maelezo ya malipo kutoka kwa muuzaji:



```bash
mostro-cli dmtouser --pubkey 7100aed1b44819555b34f90a6ca8dbb7263526e0c580f5ee35fe20d7b0644ae4 \
--orderid 305a59d0-dbee-4880-9b9a-44a60486ba4a \
--message "Hey what's your revtag ?"
```



![Communication avec le vendeur](assets/fr/08.webp)



### Hatua ya 5: Rejesha jibu



Angalia ujumbe wa moja kwa moja ili kuona majibu ya muuzaji:



```bash
mostro-cli getdm
```



Muuzaji anakupa kitambulisho chake cha malipo (hapa Revtag yake: `@satoshi`).



![Réception de la réponse](assets/fr/09.webp)



### Hatua ya 6: Kufanya malipo ya fiat



Tuma malipo kupitia njia iliyokubaliwa (Revolut katika mfano huu) kwa maelezo ya mawasiliano yaliyotolewa. **Weka hati zote zinazotumika** (picha za skrini, marejeleo ya miamala).



### Hatua ya 7: Thibitisha utumaji malipo



Mara tu malipo yamefanywa, wajulishe Mostro:



```bash
mostro-cli fiatsent -o 305a59d0-dbee-4880-9b9a-44a60486ba4a
```



### Hatua ya 8: Kupokea bitcoins



Mara tu muuzaji atakapothibitisha kupokea fiat na kuachilia escrow kwa amri ya `kutolewa`, utapokea bitcoins zako papo hapo kwenye ankara ya Umeme uliyotoa.



### Hatua ya 9: Tathmini



Kadiria muuzaji ili achangie katika sifa iliyogatuliwa:



```bash
mostro-cli rate -o 305a59d0-dbee-4880-9b9a-44a60486ba4a -r 5
```



### Amri muhimu



**Ghairi agizo** (kabla halijachukuliwa) :


```bash
mostro-cli cancel -o <order-id>
```



**Unda agizo jipya la mauzo** :


```bash
mostro-cli neworder -k sell -c eur -f 20 -m "Revolut" -p 2
```



**Fungua mzozo** :


```bash
mostro-cli dispute -o <order-id>
```



## Tumia na programu ya rununu



Sehemu hii inaonyesha uuzaji wa bitcoins kupitia Mostro Mobile kwa kufuata hali halisi ya matumizi.



### Interface kuu



Programu ina tabo 3 kuu:





- Kitabu cha Agizo**: Vinjari ununuzi unaopatikana (NUNUA BTC) na uuze (UZA BTC) maagizo
- Biashara Zangu**: Tazama maagizo yako amilifu na ya kihistoria
- Gumzo**: Wasiliana na wenzako kwa kutumia takwimu



![Interface principale](assets/fr/14.webp)



### Usanidi unaopendekezwa



Kabla ya kufanya biashara, sanidi mipangilio michache kupitia menyu (☰) > **Mipangilio** :





- Umeme Address** (hiari): Kupokea malipo moja kwa moja
- Relay**: Ongeza relay kadhaa za Nostr kwa uthabiti (k.m. `wss://nos.lol`, `wss://relay.damus.io`)
- Mostro Pubkey**: Angalia ufunguo wa umma wa mfano wa Mostro unaotumia



![Paramètres de l'application](assets/fr/16.webp)



**Muhimu kwa ulandanishi wa CLI/Simu**: Ikiwa unatumia CLI na programu ya simu ya mkononi, sanidi **relay sawa za Nostr na Mostro Pubkey** katika wateja wote wawili. Bila usanidi huu sawa, hutaona maagizo sawa yanayopatikana kwenye violesura vyote viwili. Relay na Mostro Pubkey zinazoonekana katika Mipangilio (picha ya skrini hapo juu) lazima zilingane na zile zilizo kwenye faili yako ya CLI `.env'.



### Hatua ya 1: Unda agizo la kuuza



Bonyeza kitufe cha kijani **"+"** chini kulia, kisha uchague **UZA** (kitufe chekundu).



![Boutons de création d'ordre](assets/fr/17.webp)



Jaza fomu ya uundaji:



1. **Fedha**: Chagua sarafu unayotaka kupokea (EUR, USD, n.k.)


2. **Kiasi** : Weka kiasi kinacholingana (k.m. EUR 1 hadi 3)


3. **Njia za malipo** : Chagua mbinu (k.m. "Revolut")


4. **Aina ya bei**: Chagua "Bei ya Soko"


5. **Premium**: Rekebisha malipo (kitelezi kutoka -10% hadi +10%, ilipendekezwa: 0% ili uuze haraka)



Bonyeza **Wasilisha** ili kuchapisha agizo lako.



### Hatua ya 2: Uthibitishaji wa uchapishaji



Agizo lako sasa limechapishwa! Itapatikana kwa masaa 24. Unaweza kughairi wakati wowote kabla ya mnunuzi kuichukua kwa kutekeleza amri ya `ghairi`.



![Ordre publié](assets/fr/18.webp)



Agizo linaonekana kwenye kichupo cha **Biashara Zangu** chenye hali ya "Inasubiri" na beji "Iliyoundwa na wewe".



### Hatua ya 3: Mnunuzi huchukua agizo lako



Wakati mnunuzi anachukua agizo lako, unapokea arifa. Tazama maelezo katika **Biashara Zangu**.



![Ordre pris par un acheteur](assets/fr/19.webp)



**Maagizo muhimu**: Ni lazima sasa **ulipe ankara ya kusimamishwa** iliyoonyeshwa ili kufunga bitcoins zako (hapa 4674 sats kwa EUR 1-5) kwenye escrow. Una **dakika 15 za juu zaidi** la sivyo ubadilishaji utaghairiwa.



Nakili ankara ya kushikilia na ulipe kutoka kwa umeme wako wa wallet (Phoenix, Breez, n.k.).



### Hatua ya 4: Wasiliana na mnunuzi



Mara tu escrow ikiwashwa, bonyeza **CONTACT** ili kufungua gumzo lililosimbwa kwa njia fiche na mnunuzi.



Mnunuzi (hapa "anonymous-gloriaZhao") atawasiliana nawe ili kuomba maelezo yako ya malipo. Tafadhali jibu na maelezo yako (Revtag, IBAN, nk.).



![Chat avec l'acheteur](assets/fr/20.webp)



### Hatua ya 5: Kupokea malipo ya fiat



Subiri hadi upokee malipo ya fiat katika akaunti yako ya Revolut (au njia nyingine iliyokubaliwa). ** Angalia kwa makini**:




- Kiasi halisi
- Mtumaji
- Rejea ikiombwa



Mnunuzi atakujulisha kupitia gumzo kwamba ametuma malipo. Mostro pia itaonyesha ujumbe unaothibitisha kuwa fiat imetumwa kwako.



![Confirmation d'envoi du paiement](assets/fr/20.webp)



### Hatua ya 6: Achilia escrow



Mara baada ya **kuidhinisha risiti** ya malipo ya fiat kwenye akaunti yako, bonyeza kitufe cha kijani **RELEASE** na uthibitishe kutuma satss kwa mnunuzi.



![Libération de l'escrow](assets/fr/20.webp)



Bitcoins huhamishwa mara moja kwa mnunuzi kupitia ankara yake ya Umeme.



### Hatua ya 7: Tathmini mazingatio



Baada ya kutolewa, bonyeza **RATE** ili kukadiria mnunuzi. Chagua kutoka nyota 1 hadi 5 (hapa 5/5) na ubonyeze **Wasilisha Ukadiriaji**.



![Évaluation de la contrepartie](assets/fr/21.webp)



Mabadilishano yameisha!



### Nunua bitcoins ukitumia programu ya simu



Mchakato wa **kununua ** bitcoins ni sawa lakini umebadilishwa:



1. Vinjari kichupo cha **Kitabu cha Kuagiza** > **NUNUA BTC** ili kuona maagizo ya mauzo


2. Bofya kwenye mpangilio unaovutia ili kuona maelezo


3. Bonyeza **Chukua Agizo**


4. Toa ankara yako ya Umeme (iliyotolewa kutoka kwa wallet yako)


5. Subiri muuzaji awezeshe escrow


6. Wasiliana na muuzaji kupitia **WASILIANA** kwa maelezo ya malipo


7. Tuma malipo ya fiat (weka ushahidi)


8. Muuzaji hutoa escrow baada ya uthibitishaji


9. Pokea bitcoins papo hapo kwenye ankara yako ya Umeme


10. Kadiria muuzaji (nyota 1-5)



### Udhibiti wa matatizo



**Ghairi agizo**: Katika **Biashara Zangu**, bonyeza agizo lako kisha kitufe cha **GHAIRI** (kinapatikana tu kabla ya kuchukuliwa).



**Fungua mzozo**: Ikiwa kutokubaliana kutatokea, bonyeza **DISPUTE** katika maelezo ya agizo. Ambatanisha ushahidi wote (picha za skrini za gumzo, marejeleo ya miamala ya benki).



## Faida na mapungufu



### Faida



**Uwezo wa kifedha**: Bitcoin zako haziachi kamwe udhibiti wako wa moja kwa moja kwa utaratibu wa kutolipa ankara, na hivyo kuondoa hatari ya kufilisika kwa ubadilishaji au uharamia.



**Inastahimili udhibiti**: Hakuna mamlaka inayoweza kuzima mtandao au kuhakiki maagizo yako. Mfumo hufanya kazi mradi tu relay za Nostr zinafanya kazi.



**Usiojua jina chaguomsingi**: Ufunguo wa Nostr usiojulikana pekee ndio unaokutambulisha, bila KYC au data ya kibinafsi. Mawasiliano yaliyosimbwa kutoka mwisho hadi mwisho.



**Ubadilikaji wa malipo**: Njia yoyote ya malipo inayokubaliwa na pande zote inawezekana (uhamisho, programu za simu, pesa taslimu, kubadilishana vitu).



### Mapungufu



**Maendeleo ya mapema**: Miingiliano ya kiolesura na mkondo wa kujifunza kiufundi unahitajika.



**Upeo mdogo**: Idadi ndogo ya maagizo, haswa kwa pesa nyingi au sarafu adimu.



**Mahitaji ya kiufundi**: Uelewa wa kimsingi wa Umeme na Nostr unahitajika.



**Wajibu wa mtu binafsi**: Hakuna usaidizi wa kati iwapo kutatokea matatizo, tahadhari inahitajika.



## Hitimisho



Mostro P2P inawakilisha njia mbadala inayoahidi kwa ubadilishanaji wa serikali kuu, ikichanganya Lightning Network, Nostr na escrow otomatiki kwa biashara iliyogatuliwa kweli. Licha ya maendeleo yake ya mapema na ukwasi mdogo, jukwaa tayari linatoa uhuru wa kifedha, upinzani wa udhibiti na kutokujulikana kwa chaguomsingi.



Kwa bitcoiners ambao wanapendelea uhuru na usiri, Mostro ni chaguo linalofaa linalostahili uchunguzi unaoendelea. Usanifu wake uliogatuliwa hudhamini jamii badala ya mageuzi ya kibiashara, na kutengeneza njia kwa mustakabali wa ubadilishanaji bila malipo wa Bitcoin.



## Rasilimali



### Nyaraka rasmi




- [Tovuti rasmi ya Mostro](https://mostro.network)
- [Nyaraka za kiufundi](https://mostro.network/docs-english/index.html)
- [Mostro Foundation](https://mostro.foundation)



### Chanzo kanuni na maendeleo




- [Hazina kuu ya GitHub](https://github.com/MostroP2P/mostro)
- [Mteja wa wavuti](https://github.com/MostroP2P/mostro-web)
- [Mteja CLI](https://github.com/MostroP2P/mostro-cli)



### Jumuiya




- [Itifaki ya Nostr](https://nostr.com)
- [Miongozo ya Lightning Network](https://lightning.network)