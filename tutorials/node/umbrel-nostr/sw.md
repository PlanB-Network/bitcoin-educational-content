---
name: Mwavuli Nostr
description: Kusanidi na kutumia programu za Nostr kwenye Umbrel
---

![cover](assets/cover.webp)



## Mahitaji: Ufungaji wa mwavuli



Umbrel ni jukwaa la chanzo huria ambalo hukuruhusu kukaribisha kwa urahisi programu za Bitcoin na huduma zingine kwenye seva yako ya kibinafsi. Ni suluhisho la kila moja ambalo hurahisisha upangishaji wa kibinafsi wa nodi za Bitcoin na programu zilizogatuliwa.



Hakikisha umesakinisha Umbrel kwa kufuata mwongozo wetu wa usakinishaji:



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

## Utangulizi wa Nostr



**Nostr** ni itifaki ya mtandao iliyo wazi, iliyogatuliwa iliyoundwa kwa ajili ya mitandao ya kijamii. Jina lake linasimama kwa _"Vidokezo na Mambo Mengine Yanayotumwa kwa Relays"_. Huruhusu mtu yeyote kuchapisha ujumbe (madokezo), kusimamiwa kama matukio ya JSON, na kuyaeneza kupitia seva za upeanaji badala ya jukwaa kuu. Kila mtumiaji ana jozi ya funguo za kriptografia (za faragha/za umma) ambazo hutumika kama kitambulisho: ufunguo wa umma (npub) humtambulisha mtumiaji, na ufunguo wa faragha (nsec) huwezesha ujumbe kusainiwa. Shukrani kwa usanifu huu uliosambazwa, **Nostr inatoa upinzani wa udhibiti** na unyumbufu mkubwa: unaweza kutumia wateja kadhaa na kuunganisha kwa relay nyingi upendavyo, bila kutegemea seva moja.



Kwa kifupi, Nostr ni itifaki ya mawasiliano iliyogatuliwa ambapo **wateja** (programu za mtumiaji) hutuma na kupokea matukio kupitia **relayers** (seva). Itifaki hii imekuwa maarufu hasa kwa jumuiya ya Bitcoin tangu 2023, kutokana na maadili yake ya ugatuaji na mamlaka ya data.



**Kumbuka:** Ili kutumia Nostr, utahitaji ufunguo wako wa faragha (uliotolewa na mteja wa Nostr au kupitia kiendelezi maalum). **Usishiriki kamwe ufunguo wako wa faragha**, kwa kuwa utamruhusu mtu yeyote kukuiga. Iweke mahali salama na utumie zana salama za udhibiti muhimu (ona Kidokezo hapa chini).



## Maombi ya mwavuli kwa Nostr



Umbrel hutoa mfumo ikolojia wa programu zilizojumuishwa kuchukua faida kamili ya Nostr kwenye nodi yako ya kibinafsi. Tutaelezea kwa undani matumizi ya programu kuu zinazohusiana na Nostr: **Nostr Relay**, **noStrudel**, **Snort** na **Nostr Wallet Connect**. Kila moja inakidhi hitaji mahususi: _Nostr Relay_ ni **seva ya relay ya kibinafsi**, _noStrudel_ na _Snort_ ni **Wateja wa Nostr** (violesura vya kusoma/kuchapisha madokezo), huku _Nostr Wallet Connect_ ni zana ya kuunganisha **kwingineko lako la Umeme** na Nostr.



### Relay ya Nostr - Relay yako ya kibinafsi kwenye Umbrel



![Page d'installation de Nostr Relay sur l'App Store Umbrel](assets/fr/01.webp)



**Nostr Relay** ni programu rasmi ya Umbrel ya kuendesha **relay yako mwenyewe ya Nostr** kwenye nodi yako. Lengo kuu ni kuwa na upeanaji wa **faragha** na unaotegemeka wa **kuhifadhi nakala ya shughuli zako zote za Nostr** kwa wakati halisi. Kwa maneno mengine, kwa kutumia upeanaji huu wa kibinafsi pamoja na reli za umma, unahakikisha kwamba madokezo, ujumbe na maoni yako yote yamenakiliwa nyumbani, salama dhidi ya udhibiti au upotevu wa data.



**Usakinishaji:** Kutoka kwa Umbrel App Store (kitengo _Social_), sakinisha _Nostr Relay_. Mara baada ya kuzinduliwa, programu inaendesha nyuma (huduma ya docker).



![Interface de Nostr Relay avec l'URL du relais](assets/fr/02.webp)



Utaona wavuti yake ya Interface kupitia Umbrel: inatoa maelezo ya msingi na, zaidi ya yote, URL ya upeanaji mkondo wako (juu kulia), ambayo utahitaji kunakili kwa matumizi zaidi. Kitufe cha kusawazisha (ikoni ya dunia) kinapatikana pia.



**Ili kuchukua fursa ya relay yako ya Umbrel :



**Ongeza relay kwa mteja wako wa Nostr:** Katika programu ya mteja wako (k.m. Damus kwenye iOS, Amethyst kwenye Android, Snort au noStrudel on Umbrel, n.k.), ongeza URL ya upeanaji wako wa faragha ambao ulinakili hapo awali. Kwa chaguo-msingi, relay ya Umbrel inasikiza kwenye bandari **4848**. Ukiifikia kwenye mtandao wa ndani, hii inatoa URL kama: `ws://umbrel.local:4848` (au tumia IP ya ndani ya Umbrel).



Ikiwa unatumia Tailscale (tazama hapa chini), unaweza hata kutumia lakabu ya MagicDNS DNS (kawaida `mwavuli` au jina linalozalishwa kiotomatiki) ili kuipata ukiwa popote, kila mara kwenye bandari 4848.



Ukipendelea Tor, pata Umbrel's .onion Address yako na uitumie na port 4848 kupitia kivinjari au kiteja kinachooana na Tor (angalia sehemu ya Tor)



Mara tu URL imeongezwa kwenye usanidi wa Relay ya mteja wako wa Nostr, unganisha kwenye upeanaji huu. Unapaswa kuona katika mteja wako kwamba relay ya Umbrel imeunganishwa (kawaida inaonyeshwa na dot ya Green au sawa).



**Sawazisha historia (si lazima)**: Katika wavuti ya Interface ya _Nostr Relay_ kwenye Umbrel, bofya kwenye aikoni ya **globe** 🌐 (juu ya ukurasa). Kitendo hiki kitalazimisha upeanaji wako wa Umbrel kuunganishwa kwenye relay zako zingine (zilizosanidiwa katika mteja wako) ili **kuagiza shughuli zako za zamani za umma**. Hii ina maana kwamba madokezo ya awali ambayo umechapisha au kusoma kupitia relay za umma pia yatapakuliwa na kuhifadhiwa kwenye relay yako ya faragha. Tafadhali subiri ulandanishi ufanyike.



**Tumia Nostr kama kawaida:** Kuanzia sasa na kuendelea, shughuli yoyote mpya (madokezo yaliyochapishwa, miitikio, ujumbe wa faragha uliosimbwa kwa njia fiche, n.k.) utakayoifanya kwenye Nostr itasambazwa kama kawaida kwa reli za umma **na sambamba na upeanaji wa Umbrel** wako. Ikiwa mteja wako wa Nostr amesanidiwa ipasavyo, itatuma kila tukio kwa relay zote (pamoja na yako). Relay yako ya kibinafsi itafanya kama nakala ya wakati halisi. Hata katika tukio la kukatwa kwa muda, wateja wako wataweza kusawazisha data iliyokosekana baadaye kutokana na upeanaji huu. hii inakupa udhibiti kamili wa data yako ya Nostr



Huku nyuma, _Nostr Relay_ ya Umbrel inatokana na mradi wa chanzo huria **nostr-rs-relay** (utekelezaji wa itifaki ya Rust). Inasaidia itifaki nzima ya Nostr na NIP nyingi za kawaida (NIP-01, 02, 03, 09, 11, 12, 15, 16, 20, 22, 26, 28, 33, nk), kuhakikisha utangamano wa juu na wateja.



### noStrudel - mteja wa Nostr kwa wachunguzi



![Page d'installation de noStrudel sur l'App Store Umbrel](assets/fr/03.webp)



**noStrudel** ni mteja wa wavuti wa Nostr anayeelekezwa na mtumiaji, bora kwa kuelewa na kuchunguza mtandao wa Nostr kwa undani. Ni aina ya kisanduku cha mchanga kwa ajili ya kukagua matukio na relays, na kwa ajili ya kujaribu vipengele vya kina vya itifaki. Interface iko katika Kiingereza na kiufundi kiasi, na kuifanya kuwa bora kwa watumiaji wenye uzoefu na udadisi kuhusu utendakazi wa ndani wa Nostr.



**Usakinishaji:** Sakinisha _noStrudel_ kutoka kwa Umbrel App Store (kitengo _Social_). Mara baada ya kuzinduliwa, inaweza kufikiwa kupitia kivinjari chako katika Mwavuli Address yako (k.m. `http://umbrel.local` au kupitia .onion/Tailscale yake, angalia sehemu ya ufikiaji wa nje).



![Page d'accueil de noStrudel avec le bouton Setup Relays](assets/fr/04.webp)



**Sanidi relays:** Unapofungua noStrudel, utaona kitufe cha "Weka Relays" kwenye kona ya juu kulia. Bofya juu yake ili kusanidi relays zako.



![Page de configuration des relais dans noStrudel](assets/fr/05.webp)



Kwenye ukurasa huu, bandika URL ya relay yako ya Umbrel ambayo ulinakili hapo awali. Unaweza pia kuongeza relay nyingine zilizopendekezwa na chaguo-msingi na programu. Mara baada ya kusanidi relays zako, bofya "Ingia" chini kushoto ili kuendelea.



![Options de connexion dans noStrudel](assets/fr/06.webp)



**Muunganisho:** noStrudel hukupa chaguzi kadhaa za unganisho. Kwa upande wetu, tutachagua "Ufunguo wa Kibinafsi" na ubandike katika ufunguo wako wa faragha wa Nostr uliotengenezwa hapo awali. Ikiwa bado huna ufunguo, unaweza kusakinisha kiendelezi cha [Nostr Connect] (https://chromewebstore.google.com/detail/nostr-connect/ampjiinddmggbhpebhaegmjkbbeofoaj) ili kuunda na/au kuhifadhi vitufe vyako vya Nostr na hivyo kuwasiliana kwa usalama zaidi na programu mbalimbali za Nostr.



![Interface principale de noStrudel](assets/fr/07.webp)



Mara tu imeunganishwa, unaweza kutumia noStrudel kushiriki madokezo yako kupitia Nostr. Interface inakupa ufikiaji wa:





- Kamilisha dashibodi ya Nostr iliyo na ratiba ya madokezo, arifa, ujumbe, utafutaji wa wasifu
- Usimamizi wa relay na hali ya uunganisho
- Zana za kina za kukagua matukio na maudhui yake ya JSON
- Chaguo za usanidi wa vichujio vya kalenda ya matukio na PIN



**Kidokezo:** Kwenye _noStrudel_, unaweza kusanidi _vichujio vya kalenda ya matukio_ au ujaribu _NIP tofauti (Uwezekano wa Utekelezaji wa Nostr)_. Kwa mfano, angalia usaidizi wa NIP-05 (vitambulishi vilivyogatuliwa) au vipengele vya hivi majuzi zaidi. Hii hufanya _noStrudel_ kuwa zana bora ya majaribio katika mazingira yaliyodhibitiwa.



### Koroma - Mteja wa Kisasa wa Nostr kwenye Umbrel



![Page d'installation de Snort sur l'App Store Umbrel](assets/fr/08.webp)



**Snort** ni mteja mwingine wa mtandao wa Nostr anayepatikana kwenye Umbrel, anayetoa **Interface** ya kisasa, ya haraka na isiyo na vitu vingi kwa kuingiliana na mtandao wa kijamii uliogatuliwa. Tofauti na noStrudel, ambayo inalenga watumiaji wa nishati, _Snort_ inalenga urahisi wa matumizi bila kuacha utendakazi. Imeundwa katika React, na inatoa UX nadhifu inayowakumbusha mitandao ya kijamii ya kawaida, na kuifanya ifae kwa matumizi ya kila siku.



**Usakinishaji:** Sakinisha _Snort_ kutoka kwa Umbrel App Store (kitengo _Social_).



![Page d'accueil de Snort avec le bouton S'inscrire](assets/fr/09.webp)



Unapofungua Snort, utaona kitufe cha "Jisajili" kwenye kona ya chini kushoto.



![Options de connexion dans Snort](assets/fr/10.webp)



Unaweza kuchagua kusajili au kuunganisha kwa akaunti iliyopo (ambayo ndiyo tutafanya kwa mafunzo haya).



![Méthodes de connexion dans Snort](assets/fr/11.webp)



Snort hutoa njia kadhaa za uunganisho. Unaweza kutumia kiendelezi cha Nostr Connect kilichosakinishwa hapo awali au mbinu zingine zinazopatikana. Ukishaunganishwa, utaweza kutumia programu kikamilifu.



Interface kutoka _Snort_ inatoa :





- Onyesho la **Machapisho/Mazungumzo/Ulimwenguni** ili kuabiri kati ya madokezo yako, mijadala ya mazungumzo au mipasho ya kimataifa
- Vichupo vya **Arifa**, **Ujumbe** (DM), **Tafuta**, **Wasifu**, n.k.
- Kitufe cha **+** au _Andika_ ili kuchapisha dokezo jipya
- Usimamizi wa **usajili (ufuatao)** na **orodha**
- Menyu ya usimamizi wa relay ili kuongeza/kuondoa relay na kufuatilia upatikanaji wao



**Usanidi unaopendekezwa wa relay:** Ili kuongeza relay yako ya Umbrel, nenda kwenye Mipangilio - Relays. Weka URL ya relay yako (`ws://umbrel:4848` au URL nyingine kulingana na usanidi wako) katika orodha ya Snort ya relays. Kwa njia hii, Snort itachapisha madokezo yako kwenye relay yako ya faragha pamoja na yale ya umma.



### Nostr Wallet Unganisha - Unganisha Umeme wako Wallet kwa Nostr



**Nostr Wallet Connect (NWC)** ni programu ambayo **inaunganisha nodi yako ya Mwavuli (Umeme)** kwa programu zinazooana za Nostr za kufanya malipo ya Radi (kwa mfano, kutuma _zaps_, malipo hayo madogo kwa maudhui ya "kupenda"). Katika somo hili, tutaangalia jinsi ya kuunganisha noStrudel kwenye nodi yako ya Umeme ili kufanya malipo moja kwa moja kutoka kwa Interface.



**Ufungaji na usanidi:**



![Page d'installation de Nostr Wallet Connect sur l'App Store Umbrel](assets/fr/12.webp)



Sakinisha _Nostr Wallet Connect_ kutoka duka la Alby kwenye Umbrel.



![Configuration de NWC dans noStrudel - Étape 1](assets/fr/13.webp)



Katika noStrudel, bofya wasifu wako kwenye kona ya juu ya kulia, kisha kwenye kitufe cha "kusimamia".



![Configuration de NWC dans noStrudel - Étape 2](assets/fr/14.webp)



Bofya kwenye "Umeme" kisha "unganisha Wallet".



![Configuration de NWC dans noStrudel - Étape 3](assets/fr/15.webp)



Kati ya chaguzi zinazopatikana za uunganisho, chagua "Umbrel".



![Configuration de NWC dans noStrudel - Étape 4](assets/fr/16.webp)



Bofya kwenye "Unganisha" ili uelekezwe upya kiotomatiki kwenye kipindi chako cha Kuunganisha Umbrel Nostr Wallet.



![Page de configuration des autorisations NWC](assets/fr/17.webp)



Kwenye ukurasa wa Nostr Wallet Connect, unaweza:




   - Bainisha bajeti yako ya juu zaidi
   - Thibitisha uidhinishaji
   - Weka muda wa kuisha kwa muunganisho


Bonyeza "kuunganisha" ili kukamilisha.



![Confirmation de connexion dans noStrudel](assets/fr/18.webp)



Umeelekezwa kwenye noStrudel kwa ujumbe wa uthibitisho: sasa unaweza kusambaza ulimwengu mzima kutoka kwa nodi yako ya Wallet/LND!



Shukrani kwa NWC, **malipo yako ya umeme kupitia Nostr** (zaps za kutuza machapisho, _Thamani ya malipo ya Thamani_, n.k.) huanzia **nodi yako mwenyewe**. Huhitaji tena kuelekeza miamala yako kupitia huduma za nje au kuchanganua QR kutoka kwa simu yako kila wakati. Hali ya matumizi ya mtumiaji imeimarishwa sana, huku ikisalia _isiyojaliwa_ na ni rafiki wa faragha.



Ikiwa unataka kujua jinsi ya kusanidi nodi yako ya Umeme kwenye Umbrel, ninapendekeza uangalie mafunzo haya mengine ya kina:



https://planb.network/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

## Usanidi wa hali ya juu na usalama



Kutumia Umbrel na Nostr pamoja katika kiwango cha juu kunahitaji umakini maalum kwa **usalama** na **muunganisho**. Hapa kuna vidokezo vichache vya jinsi ya kulinda usanidi wako na kuufikia kikamilifu, popote ulipo.



### Salama ufikiaji wa nje: Tor na Tailscale



Kwa sababu za usalama, Mwavuli wako unapatikana tu kwa chaguomsingi kwenye mtandao wako wa karibu (na kupitia Tor). Ili kuingiliana na Nostr ukiwa mbali na nyumbani, una masuluhisho mawili unayopendelea: **Tor** (ufikiaji usiojulikana kupitia mtandao wa vitunguu) na **Tailscale** (mavu ya faragha ya VPN).





- Ufikiaji kupitia Tor:** Umbrel husanidi kiotomatiki huduma ya **Tor (.onion)** kwa wavuti na programu zake za Interface. Hii inamaanisha kuwa unaweza kufikia Mwavuli wa Interface (pamoja na _noStrudel_ au _Snort_) kutoka mahali popote, kwa kutumia kivinjari cha Tor, bila kufichua IP yako ya umma. _Tor inatumiwa kufikia huduma zako za Umbrel kutoka nje ya mtandao wako wa karibu, bila kuanika kifaa chako kwenye Mtandao ([Setup Tor on your system - Guides - Umbrel Community](https://community.umbrel.com/t/setup-tor-on-your-system/7509#:~:text=Rasmi%20website%3A%20_kwenda kwa Umbrel chaguo hili). mipangilio na urejeshe URL yako ya .onion ya Umbrel (au changanua msimbo wa QR uliotolewa). Kwenye kivinjari cha Tor, fikia hii .onion Address: utapata Interface sawa na ndani. Kisha unaweza kutumia programu zako za Nostr kama vile nyumbani.


**Relay ya Nostr kupitia Tor:** Ikiwa ungependa relay yako ya Nostr ipatikane kupitia Tor na wateja wako (au marafiki walioidhinishwa), hii inawezekana. Mwavuli haitoi relay ya .onion Address moja kwa moja, lakini kwa kuwa inaendeshwa kwenye bandari 4848, unaweza ama :





    - Tumia UI Umbrel's .onion Address na usanidi mteja wako kuunganishwa kupitia Interface hii (haiwezekani kwa WebSocket),





    - Au** onyesha bandari 4848 kama huduma tofauti ya vitunguu. Hii inahitaji kugombana na usanidi wa Tor kwenye Umbrel (iliyohifadhiwa kwa watumiaji wa hali ya juu wanaostarehesha na SSH). Vinginevyo, zingatia **Tor handaki** kwenye seva nyingine ambayo inaelekeza upya kwa Umbrel: hata hivyo, kwa matumizi ya kibinafsi, ni rahisi kutumia Tailscale.





- Fikia kupitia Tailscale:** [Tailscale](https://tailscale.com/) ni suluhisho la wavu la VPN ambalo huunda mtandao pepe wa kibinafsi kati ya vifaa vyako na Umbrel. Faida: inafanya kazi kana kwamba uko kwenye LAN, lakini kwenye mtandao, iliyosimbwa na bila usanidi tata. **Tailcale hupatia Umbrel yako IP isiyobadilika na jina la kikoa cha faragha, bila kujali eneo la mtandao wake ([Tailscale | Umbrel App Store](https://apps.umbrel.com/app/tailscale#:~:text=Tailscale%20is%20zero%20config%20VPN,imekaguliwa%20na%20imeaminika) Kwa mazoezi, pindi tu utakaposakinisha Tailscale kwenye Umbrel (kutoka Umbrel App Store, kitengo _Networking_) **na** kwenye vifaa vyako (simu ya mkononi, Kompyuta...), utaweza kufikia Umbrel kupitia Address kama `100.x.y.z` (Tailscale IP) au jina kama `umbrel.3.tail.net2`.


kwa Nostr_, Tailscale ni muhimu sana: simu yako ya mkononi, ikiwa ina Tailscale amilifu, itaweza kuunganishwa kwenye `ws://umbrel:4848` (shukrani kwa MagicDNS) au moja kwa moja kwenye IP ya Tailscale na mlango 4848 ili kutumia upeanaji. Wateja kama Damus au Amethyst wataona Mwavuli wako kana kwamba uko kwenye mtandao sawa wa karibu. **Kidokezo:** Washa chaguo la **MagicDNS** katika Tailscale ili kutumia jina la mpangishaji `mwavuli` badala ya kukariri IP. Hii inahakikisha muunganisho mzuri kwenye relay yako hata unaposafiri ([Nostr Relay | Umbrel App Store](https://apps.umbrel.com/app/nostr-relay#:~:text=client%20%28e,That%27s%20it%21%20Your%20past)).


Zaidi ya hayo, Tailscale hukuruhusu kufikia Mwavuli wa Interface (na hivyo wateja wa wavuti _noStrudel/Snort_) kupitia kivinjari rahisi, kwa kutumia IP ya kibinafsi au jina la kikoa ulilopewa. Hakuna haja ya Kivinjari cha Tor, na kasi ya kuhamisha data kwa ujumla ni bora kuliko kupitia mtandao wa Tor.




**Kumbuka: Tor na Tailscale hazitengani. Unaweza kuweka Tor amilifu kwa ufikiaji usiojulikana au huduma mahususi, na utumie Tailscale siku hadi siku kwa urahisi wake. Katika hali zote mbili, huna haja ya kufungua bandari kwenye router yako, ambayo huimarisha usalama.



### Kulinda relay yako ya Nostr (mazoea yanayopendekezwa)



Ikiwa unakaribisha upeanaji wa Nostr kwenye Umbrel, haswa katika muktadha wa hali ya juu, hakikisha kuwa umetumia mazoea machache mazuri:





- Relay ya faragha au yenye vikwazo:** Kwa chaguomsingi, relay yako ya Umbrel ni ya faragha (haijatangazwa hadharani) na, ukiifikia tu kupitia Tailscale au LAN yako, itaendelea kutoweza kufikiwa na wageni. **Weka kiungo kwa siri ** Usitangaze kwenye mitandao ya umma ya Nostr isipokuwa ungependa kupangisha watumiaji wengine kwa hiari, ambalo ni suala jingine zima (ukadiriaji, kipimo data, n.k.). Kwa matumizi ya kibinafsi, tunapendekeza uzuie ufikiaji kwako mwenyewe na, ikiwa ni lazima, kwa marafiki na familia chache unaowaamini.





- Orodha iliyoidhinishwa / Uthibitishaji**: Utekelezaji wa nostr-rs-relay unaauni utaratibu wa uthibitishaji **NIP-42** pamoja na _idhini_ za funguo za umma. Kwa kuwezesha chaguo hizi, unaweza kuzuia upeanaji mkondo wako ili **ikubali tu matukio yaliyotiwa saini na funguo fulani (zako)**, au kwamba wateja lazima waidhinishe ili kuchapisha. kusanidi hii kunahitaji kuhariri faili ya usanidi ya relay `config.toml` katika Umbrel (kupitia SSH kwenye chombo cha Docker)._ Ni upotoshaji wa hali ya juu, lakini kwa mfano unaweza kuorodhesha matangazo yanayoruhusiwa (`pubkey_whitelist`). Kwa njia hii, hata mtu akigundua relay yako, hataweza kuchapisha chochote hapo ikiwa hayumo kwenye orodha.





- Masasisho na matengenezo:** Sasisha Umbrel yako na programu ya _Nostr Relay_. Masasisho yanaweza kujumuisha uboreshaji wa utendakazi (k.m. ushughulikiaji bora wa barua taka) na marekebisho ya usalama. Kwenye Umbrel, angalia App Store mara kwa mara kwa masasisho kwa _Nostr Relay_, na uyatumie inapohitajika.





- Ufuatiliaji na vikomo:** Angalia jinsi upeanaji mkondo wako unavyotumika. Ukiifungua kwa wengine, weka jicho kwenye mzigo (uhifadhi wa CPU/RAM) kwenye Mwavuli wako, kwani relay inaweza kukusanya data nyingi haraka. nostr-rs-relay inatoa **viwango na vikomo vya uhifadhi vinavyoweza kusanidiwa** (`vikomo` katika usanidi, k.m. idadi ya matukio kwa sekunde, ukubwa wa juu zaidi wa tukio, uondoaji wa matukio ya zamani...). Kwa matumizi ya kibinafsi, labda hautahitaji kugusa hizi, lakini fahamu kuwa vigezo hivi vipo ikiwa unavihitaji ([nostr-rs-relay/config.toml at master - scsibug/nostr-rs-relay - GitHub](https://github.com/scsibug/nostr-rs-relay/blob/master/config.:toml=text)#).





- Kupata vitufe vya Nostr:** Hatua hii tayari imetajwa, lakini ni muhimu: usiwahi kuingiza funguo zako za faragha za Nostr kwenye Interface usiyoiamini kikamilifu. Badala yake, tumia viendelezi vya kivinjari au vifaa vya nje (kama vile Nostr _signers_ kwenye simu tofauti) kutia sahihi kwa vitendo nyeti. Kwenye Umbrel, wateja wako wa wavuti kama _Snort_ na _noStrudel_ wanaweza kufanya kazi bila kujua ufunguo wako wa siri, kupitia NIP-07. Tumia fursa hii kuchanganya faraja na usalama.




Kwa kufuata vidokezo hivi, ujumuishaji wako wa nodi ya Umbrel na Nostr itakuwa na nguvu **na** salama. Utakuwa na mazingira kamili: nodi ya Bitcoin ya malipo ya Umeme, upeanaji wa kibinafsi wa Nostr kwa uhuru wa data, na wateja wa wavuti wa Nostr wa utendaji wa juu ili kuvinjari mtandao huu mpya wa kijamii uliogatuliwa. Furahia kuchunguza Nostr kwa Umbrel!