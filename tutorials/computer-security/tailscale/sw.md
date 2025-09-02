---
name: Mkia wa mkia
description: Mafunzo ya hali ya juu ya Tailscale
---
![cover](assets/cover.webp)



## 1. Utangulizi



Tailscale ni VPN ya kizazi kijacho ambayo huunda mtandao wa matundu uliosimbwa kwa njia fiche kati ya vifaa vyako. Inakuruhusu kuunganisha mashine za mbali kana kwamba ziko kwenye mtandao mmoja wa ndani, bila usanidi tata au ufunguzi wa mlango.



Kwa upangishaji binafsi, Tailscale hupa kila kifaa IP ya faragha isiyobadilika katika mtandao pepe, inayotoa ufikiaji thabiti kwa huduma zako hata IP yako ya umma inapobadilika. Hii inamaanisha kuwa unaweza kudhibiti seva zako ukiwa mbali, bila kufichua huduma zako moja kwa moja kwenye Mtandao.



**Maombi kuu:**




- Dhibiti seva ya kibinafsi kutoka nje
- Dhibiti nodi za Mwavuli/Umeme haraka kuliko Tor
- Ufikiaji salama wa Raspberry Pi au NAS
- Unganisha kwenye huduma zako kupitia SSH au HTTP bila usanidi changamano wa mtandao



Mbinu hii inayozingatia urahisi huwezesha wapangaji binafsi kufikia huduma zao kwa usalama, na kuepuka mitego ya VPN za kitamaduni.



## 2. Jinsi Tailscale inavyofanya kazi



Tofauti na VPN za kitamaduni, ambazo hupitisha trafiki yote kupitia seva kuu, Tailscale huunda mtandao wa matundu ambapo vifaa vinawasiliana moja kwa moja. Seva ya kati hushughulikia tu uthibitishaji na usambazaji wa ufunguo, bila kuona data ya mtumiaji.



![VPN traditionnel (hub-and-spoke)](assets/fr/01.webp)


*Kielelezo cha 1: VPN ya Jadi iliyo na usanifu wa kitovu-na-kuzungumza ambapo trafiki yote hupitia seva kuu*



Kulingana na WireGuard, kila kifaa hutengeneza funguo zake za kriptografia. Seva ya uratibu husambaza funguo za umma kwa nodi, ambazo huanzisha vichuguu vilivyosimbwa kutoka mwisho hadi mwisho moja kwa moja kati yao. Ili kupitia ngome, Tailscale hutumia NAT traversal na, kama suluhisho la mwisho, relay za DERP ambazo hudumisha usimbaji fiche.



![VPN maillé (mesh)](assets/fr/02.webp)


*Mchoro wa 2: Mtandao wa wavu wenye mikia ambapo vifaa vinawasiliana moja kwa moja*



Mawasiliano yote yamesimbwa kwa njia fiche kwa WireGuard. Tailscale huona metadata (miunganisho) pekee lakini kamwe haioni maudhui ya ubadilishanaji. Kwa uhuru zaidi, Mizani ya kichwa huwezesha seva ya uratibu kujiendesha yenyewe.



**Usalama na usiri:** Shukrani kwa WireGuard, mawasiliano yote kwenye Tailscale yamesimbwa kwa njia fiche kutoka mwanzo hadi mwisho. Tailscale haiwezi kusoma trafiki yako - ni vifaa vyako pekee vilivyo na funguo muhimu za faragha. Huduma huona metadata pekee: Anwani za IP, majina ya vifaa, mihuri ya muda ya muunganisho na kumbukumbu za muunganisho wa programu-jalizi (bila maudhui).



Hata hivyo, usanifu huu unategemea Tailscale Inc. kwa uratibu wa mtandao. Ili kuondoa utegemezi huu, Headscale inatoa mbadala wa chanzo huria ambayo inakuruhusu kupangisha seva ya udhibiti huku ukitumia wateja rasmi wa Tailscale, na hivyo kuhakikishia uhuru kamili juu ya miundombinu ya mtandao wako, kwa gharama ya usanidi wa kiufundi zaidi.



**Kwa maelezo ya kina kuhusu utendakazi wa ndani wa Tailscale, ikiwa ni pamoja na udhibiti wa udhibiti wa ndege, NAT traversal na relay za DERP, tunapendekeza makala bora [Jinsi Tailscale Inavyofanya kazi](https://tailscale.com/blog/how-tailscale-works) kwenye blogu rasmi. Nakala hii inaelezea kwa kina dhana za kiufundi zinazofanya Tailscale kuwa na nguvu sana.



## 3. Kufunga Tailscale



Tailcale huendesha kwenye **mifumo ya uendeshaji inayojulikana zaidi** (Windows, macOS, Linux, iOS, Android). Usakinishaji unasemekana kuwa "haraka na rahisi" kwenye mifumo yote. Hebu tuanze kwa kuangalia Interface na jinsi ya kuunda akaunti, kisha tuendelee kwenye taratibu za usakinishaji wa mazingira tofauti.



### 3.1 Uundaji wa akaunti ya tailscale



Nenda kwenye [https://tailscale.com/](https://tailscale.com/) na ubofye kitufe cha "Anza" kilicho juu ya ukurasa.




![Page d'accueil Tailscale](assets/fr/03.webp)


*Ukurasa wa nyumbani wa Tailscale unafafanua dhana na inatoa mwanzo bila malipo*



Ili kutumia Tailscale, kwanza unahitaji kufungua akaunti kupitia mtoa huduma za utambulisho:



![Page de connexion Tailscale](assets/fr/04.webp)


*Chaguo la mtoaji kitambulisho la kuunganisha kwenye Tailcale (Google, Microsoft, GitHub, Apple, n.k.)*



Baada ya kuingia, Tailscale itakuuliza habari fulani kuhusu matumizi yako yaliyokusudiwa:



![Questionnaire d'utilisation](assets/fr/05.webp)


*Fomu ya kuelewa vyema kesi yako ya matumizi (ya kibinafsi au ya kitaaluma)*



Ukishafungua akaunti yako, unaweza kusakinisha Tailscale kwenye vifaa vyako:



![Ajout du premier appareil](assets/fr/07.webp)


*Tailscale hukuruhusu kusakinisha programu kwenye mifumo tofauti*



### 3.2 Usakinishaji kwenye majukwaa tofauti





- Kwenye Windows na macOS:** Pakua kwa urahisi programu tumizi kutoka kwa tovuti rasmi ya Tailscale na uisakinishe (faili.msi kwenye Windows, faili ya .dmg kwenye Mac). Mara baada ya kusakinishwa, programu itazindua Interface ya mchoro ambayo hukuruhusu kuunganisha (kupitia kivinjari) kwenye akaunti yako ya Tailscale ili kuthibitisha mashine.



![Connexion d'un appareil macOS](assets/fr/08.webp)


*Unganisha MacBook kwenye tailnet*



![Connexion réussie](assets/fr/09.webp)


*Uthibitisho kwamba kifaa kimeunganishwa kwenye mtandao wa Tailscale*





- Kwenye Linux (Debian, Ubuntu, n.k.):** Una chaguo kadhaa. Njia rahisi ni kuendesha hati rasmi ya usakinishaji: kwa mfano, kwenye Debian/Ubuntu:



```bash
curl -fsSL https://tailscale.com/install.sh | sh
```



Hati hii itaongeza hazina rasmi ya Tailscale na kusakinisha kifurushi. Unaweza pia [kuongeza mwenyewe hazina ya APT](https://pkgs.tailscale.com) au kutumia Snap au vifurushi vinavyofaa. Baada ya kusakinishwa, daemon `tailscaled` itaendeshwa chinichini. Kisha utahitaji **kuthibitisha nodi** (tazama Interface CLI dhidi ya wavuti hapa chini). Kwenye usambazaji mwingine (Fedora, Arch...), kifurushi kinapatikana pia kupitia hazina za kawaida au hati ya usakinishaji ya ulimwengu wote. Kwa seva isiyo na kichwa, tumia CLI: kwa mfano `sudo tailscale up --auth-key <key>` ikiwa unatumia ufunguo wa uthibitishaji uliotolewa awali, au tu `tailscale up` kwa kuingia kwa maingiliano (ambayo itatoa URL ya kutembelea ili kuthibitisha kifaa).





- Kwenye mifumo inayotegemea ARM (Raspberry Pi, n.k.):** Kwa ujumla tuko kwenye Linux, kwa hivyo mbinu sawa na hapo juu (hati au kifurushi). Kumbuka kuwa Tailscale inasaidia usanifu wa ARM32/ARM64 bila matatizo yoyote. Watumiaji wengi husakinisha Tailscale kwenye Raspberry Pi OS kupitia apt au kwa usambazaji nyepesi (DietPi, n.k.) ili kufikia Pi zao kila mahali.





- Kwenye iOS na Android:** Tailscale hutoa **programu rasmi** za simu. Sakinisha kwa urahisi *Tailscale* kutoka kwenye [App Store](https://apps.apple.com/us/app/tailscale/id1470499037?ls=1) (iOS) au [Play Store](https://play.google.com/store/apps/details?id=com.tailscale.ipn) (Android).



![Installation sur iPhone](assets/fr/11.webp)


*Hatua za kusakinisha Tailcale kwenye iPhone: karibu, faragha, arifa, VPN*



![Connexion sur iPhone](assets/fr/12.webp)


*Unganisha kwa tailnet, chagua akaunti na uthibitishe kwenye iPhone*



Mara baada ya programu kusakinishwa, katika uzinduzi wa kwanza itakuuliza uidhinishe kupitia mtoa huduma aliyechaguliwa (Google, Apple ID, Microsoft, nk., kulingana na kile unachotumia kwa Tailscale) - ni utaratibu sawa na kwenye majukwaa mengine, kwa kawaida kuelekeza kwenye ukurasa wa wavuti wa OAuth. Baada ya hapo, programu ya simu hutengeneza VPN (kwenye iOS utahitaji kukubali programu jalizi ya usanidi wa VPN). Programu inaweza kufanya kazi chinichini, kukupa ufikiaji wa mtandao wako wa nyuma ukiwa popote. *Tafadhali kumbuka:* kwenye simu ya mkononi, unaweza tu kuwa na **VPN moja inayotumika kwa wakati mmoja** - kwa hivyo hakikisha kuwa huna VPN nyingine iliyounganishwa kwa wakati mmoja, au Tailscale haitaweza kuanzisha yake. Kwenye Android, unaweza kusanidi wasifu tofauti wa kazini ikiwa unataka kutenga matumizi fulani (k.m. wasifu wenye Tailscale unaotumika kwa programu fulani).



### 3.3 Kuongeza vifaa vingi na uthibitishaji



Kifaa chako cha kwanza kikishaunganishwa, Tailscale hukuomba uongeze vifaa vingine kwenye mtandao wako:



![Ajout d'appareils supplémentaires](assets/fr/10.webp)


*Interface inayoonyesha kifaa cha kwanza kilichounganishwa na kusubiri vifaa vingine*



Baada ya kuongeza vifaa kadhaa, unaweza kuangalia kama vinaweza kuwasiliana.



![Test de connectivité entre appareils](assets/fr/13.webp)


*Uthibitisho kwamba vifaa vinaweza kuwasiliana kupitia ping*



Tailscale kisha inapendekeza usanidi wa ziada ili kuboresha matumizi yako:



![Suggestions de configuration](assets/fr/14.webp)


*Mapendekezo ya kusanidi DNS, kushiriki vifaa na kudhibiti ufikiaji*



### 3.4 Dashibodi ya Utawala



Dashibodi ya usimamizi wa wavuti hukuruhusu kutazama na kudhibiti vifaa vyako vyote vilivyounganishwa:



![Tableau de bord des machines](assets/fr/15.webp)


*Orodha ya vifaa vilivyounganishwa na sifa na hali zao*



**Interface Web vs Interface CLI:** Tailscale inatoa njia mbili za ziada za kuingiliana na mtandao: **Interface usimamizi wa wavuti** na **mteja wa mstari wa amri (CLI)**.





- Interface Web (Dashibodi ya Msimamizi)**: inapatikana katika [https://login.tailscale.com](https://login.tailscale.com), dashibodi hii ya wavuti ndiyo dashibodi kuu ya mtandao wako wa Tailscale. Inaorodhesha vifaa vyote (*Mashine*), hali yao ya mtandaoni/nje ya mtandao, anwani zao za IP za Tailscale na zaidi. Hapa unaweza **kudhibiti vifaa** (kubadilisha jina, funguo za kuisha muda, kuidhinisha njia, kuzima nodi), **kudhibiti watumiaji** (katika muktadha wa shirika), na kufafanua sheria za usalama (ACLs). Hapa ndipo unaposanidi chaguo za kimataifa kama vile MagicDNS, lebo, au vitufe vya uthibitishaji (vifunguo vya uthibitishaji wa pre-generate kwa nyongeza ya kifaa kiotomatiki). Wavuti ya Interface ni rahisi sana kwa kupata muhtasari na kutumia mabadiliko ambayo yataenezwa kupitia seva ya uratibu kwa nodi zote. *Mfano:* Kuwasha **njia ndogo** au **nodi ya kutoka** hufanywa kwa mbofyo mmoja kwenye kiweko, mara tu nodi husika itakapojitangaza hivyo.





- Laini ya amri ya Interface (CLI):** Amri ya `kiasi cha mkia` inapatikana katika CLI kwenye kila kifaa ambapo Tailscale imesakinishwa. CLI hii hukuruhusu kufanya kila kitu ndani ya nchi: unganisha (`ongeza kiwango cha mkia`), kagua hali (`hadhi ya umbo la mkia` ili kuona ni programu zipi zingine zimeunganishwa), suluhisha (`ping ya mkia <ip>`), na kadhalika. Baadhi ya vipengele hata **havipo kwa CLI** au mahiri zaidi, kwa mfano:





  - `ongeza kiwango cha juu --advertise-routes=192.168.0.0/24` ili kutangaza njia ndogo,
  - `tailscale up --advertise-exit-node` ili kupendekeza mashine yako kama njia ya kutoka,
  - `tailscale set --accept-routes=true` (au `--exit-node=<IP>`) kutumia njia au kutumia njia ya kutoka,
  - `tailscale ip -4` ili kuonyesha IP ya kifaa cha Tailscale,
  - `kufuli/kufungua kwa umbo la mkia` (ikiwa unatumia *locknet-lock*, kipengele cha usalama cha hali ya juu),
  - au `faili ya ukubwa wa mkia tuma <nodi>` kutumia **Taidrop** (uhamisho wa faili kati ya vifaa).


CLI ni muhimu sana kwenye seva zisizo na picha za Interface, na kwa kuandika vitendo fulani. **Tofauti katika matumizi:** Mipangilio mingi ya kimsingi inaweza kufanywa kupitia Wavuti au kupitia CLI. Kwa mfano, kuongeza kifaa hufanywa ama kwa kuuliza kupitia dashibodi, au kwa kuendesha `kuongeza mkia` kwenye kifaa na kuthibitisha kupitia wavuti. Vile vile, kubadilisha jina la kifaa kunaweza kufanywa kupitia kiweko au kwa `tailscale set --hostname`. **Kwa muhtasari**, dashibodi ya wavuti ni bora kwa usimamizi wa mtandao wa kimataifa (hasa ikiwa na mashine/watumiaji wengi), wakati CLI inafaa kwa udhibiti mzuri wa mashine fulani, hati za otomatiki, au matumizi kwenye mfumo bila GUI.



## 4. Kutumia Tailscale kwenye Umbrel



Umbrel ni jukwaa maarufu la mwenyeji binafsi (haswa linatumika kwa Bitcoin/nodi za Umeme na huduma zingine zinazojisimamia, kupitia Duka lake la Programu). Ili kusakinisha na kusanidi Umbrel, tunapendekeza ufuate mafunzo yetu maalum:



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

Kutumia Umbrel na Tailscale pamoja ni kesi ya utumiaji inayovutia sana, kwani Umbrel huunganisha asili ya moduli ya Tailscale iliyo rahisi kusambaza. Hivi ndivyo jinsi Tailscale inavyounganishwa na Umbrel na kile kinacholeta:



### 4.1 Ufungaji na usanidi wa mwavuli





- Inasakinisha Tailscale kwenye Umbrel:** Umbrel ina programu rasmi ya Tailscale katika Hifadhi yake ya Programu. Usakinishaji hauwezi kuwa rahisi zaidi:



![Interface Umbrel avec l'application Tailscale](assets/fr/16.webp)


*Ukurasa wa maombi ya mkia kwenye Duka la Programu ya Umbrel*



Kutoka kwa Mwavuli wa Wavuti wa Interface, fungua Duka la Programu, tafuta **Tailscale** na ubofye *Sakinisha*. Sekunde chache baadaye, programu imewekwa kwenye Mwavuli. Unapoifungua, Umbrel huonyesha ukurasa unaokuruhusu kuunganisha nodi yako kwa Tailscale.



![Écran de login Tailscale dans Umbrel](assets/fr/17.webp)


*Skrini ya uunganisho wa sura ya mkia katika Interface ya Umbrel*



** bonyeza tu "Ingia"**, ambayo itakuelekeza kwenye ukurasa wa uthibitishaji wa Tailscale:



![Page d'authentification Tailscale](assets/fr/18.webp)


*Unganisha kwa Tailscale kupitia mtoa huduma za utambulisho*



Unaweza kuthibitisha kupitia akaunti yako ya Tailscale (Google/GitHub/etc.) au uweke barua pepe yako. Kwa kawaida, kwenye Umbrel, Interface hukuomba utembelee [https://login.tailscale.com](https://login.tailscale.com) na uingie - hii inathibitisha programu ya Umbrel Tailscale.



![Confirmation de connexion réussie](assets/fr/19.webp)


*Uthibitisho kwamba kifaa cha Umbrel kimeunganishwa kwenye mtandao wa Tailscale*



Baada ya kumaliza, Umbrel yako iko "katika" mtandao wako wa Tailscale na inaonekana kwenye kiweko chako na jina (k.m. *mwavuli*). Kisha unaweza kubofya IP Address ya vifaa vyako ili kuinakili, kupata IPv6 Address au MagicDNS yako inayohusishwa na kifaa chako.



![Console Tailscale avec appareils connectés](assets/fr/20.webp)


*Dashibodi ya usimamizi wa Tailscale inayoonyesha vifaa kadhaa vilivyounganishwa, ikiwa ni pamoja na Umbrel*




### 4.2 Ufikiaji wa mbali wa huduma za Umbrel



Mara baada ya Mwavuli kuunganishwa kwenye Tailscale, **unaweza kufikia Mwavuli wa Interface na programu zinazoendesha juu yake, kutoka popote, kana kwamba uko kwenye mtandao wa ndani**. Hii ni moja ya faida kuu juu ya Tor.



Ufikiaji ni rahisi ajabu: badala ya kutumia `umbrel.local` (ambayo inafanya kazi kwenye mtandao wa ndani pekee), unatumia Umbrel's Tailscale IP Address (`http://100.x.y.z`) moja kwa moja kutoka kwa kifaa chochote kilichounganishwa kwenye wavu wako. Hii inafanya kazi bila kujali uko wapi au unatumia muunganisho gani wa intaneti (4G, Wi-Fi ya umma, mtandao wa shirika).



**Mifano ya programu zilizopangishwa na Umbrel zinazopatikana kupitia Tailscale:**





- Mwavuli mkuu wa Interface**: Fikia dashibodi yako ya Mwavuli kwa kuandika `http://100.x.y.z` katika kivinjari chako
- Bitcoin nodi**: Dhibiti nodi yako ya Bitcoin bila kusubiri, tazama usawazishaji na takwimu
- Njia ya Umeme**: Tumia ThunderHub, RTL au violesura vingine vya usimamizi wa Umeme kwa mwitikio wa haraka
- Mempool**: Angalia miamala ya Bitcoin na Mempool bila ucheleweshaji wa Tor
- noStrudel**: Fikia huduma zako za Nostr zinazopangishwa kwenye Umbrel



**Unganisha pochi za nje kwa Bitcoin yako au nodi za umeme kupitia Tailscale:**



Tailscale pia huwezesha pochi zako za Bitcoin na Radi zilizosakinishwa kwenye vifaa vingine kuunganishwa moja kwa moja kwenye nodi yako ya Umbrel:





- Sparrow wallet (Bitcoin)**: Wallet Bitcoin hii ya nje inaweza kuunganisha moja kwa moja kwenye seva yako ya Umbrel's Electrum kwa kutumia Tailscale IP Address:



![Configuration Electrum dans Sparrow](assets/fr/21.webp)


*Kusanidi seva ya Electrum ya kibinafsi katika Sparrow wallet kwa kutumia Umbrel's Tailcale IP Address*



![Liste des serveurs Electrum dans Sparrow](assets/fr/22.webp)


*Orodha ya lakabu za seva ya Electrum katika Sparrow yenye Umbrel Tailcale IP Address*



Soma mwongozo wetu kamili wa kusanidi Sparrow wallet na nodi yako ya Bitcoin:



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d




- Zeus (Umeme)**: Umeme huu wa rununu wa Wallet unaweza kuunganisha kwenye nodi yako ya Umeme kwenye Mwavuli. Badala ya kusanidi sehemu ya mwisho kama `.onion', weka tu IP ya Tailscale ya Mwavuli wako na mlango wa API ya Umeme. Muunganisho utakuwa papo hapo ikilinganishwa na Tor.



![Configuration Zeus avec IP Tailscale](assets/fr/23.webp)


*Inasanidi Zeus ili iunganishwe na eneo la Umeme kupitia Tailscale* IP Address



Ili kusanidi Zeus na nodi yako ya Umeme, angalia mafunzo yetu ya kina:



https://planb.network/tutorials/wallet/mobile/zeus-embedded-c67fa8bb-9ff5-430d-beee-80919cac96b9

Ili kujua zaidi kuhusu Lightning Network na jinsi inavyofanya kazi kwenye Umbrel, tembelea:



https://planb.network/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16



### 4.3 Manufaa juu ya Tor



Umbrel asili hutoa ufikiaji wa mbali kupitia Tor (kwa kutoa anwani `.onion` kwa huduma zake za wavuti). Ingawa Tor ina faida ya usiri (kutokujulikana) na haitaji usajili, watumiaji wengi hupata **Tor polepole na isiyo imara** kwa matumizi ya kila siku (kurasa hupakia polepole, muda umeisha, n.k.) - *"Mwavuli kupitia Tor ni polepole sana "* wengine wanalalamika.



Tailscale hutoa muunganisho wa **kasi zaidi, wa utulivu wa chini**, trafiki inapopita moja kwa moja (au kupitia relay ya haraka) badala ya kuruka kupitia nodi 3 za Tor. Zaidi ya hayo, Tailscale hutoa matumizi ya "mtandao wa ndani": IP za kibinafsi hutumiwa, na programu zinaweza kupangwa moja kwa moja (k.m. Hifadhi ya mtandao ya SMB kwenye \100.x.y.z).



Hiyo ilisema, Tor ina faida ya kugatuliwa na "nje ya sanduku" kwenye Umbrel, wakati Tailscale inahusisha kuamini mtu wa tatu (au kichwa cha kukaribisha). Tor pia ni muhimu kwa ufikiaji usio na mteja (kutoka kwa kivinjari chochote cha Tor, unaweza kushauriana na UI ya Umbrel, wakati Tailscale inahitaji mteja kusakinishwa kwenye kifaa cha kufikia).



**Kuhitimisha**, kwa matumizi ya mwingiliano (Pochi za umeme, violesura vya mara kwa mara vya wavuti), Tailscale inatoa faraja na kasi ya kustahiki ikilinganishwa na Tor, kwa bei ya utegemezi kidogo kutoka nje. Watu wengi huchagua kutumia *zote mbili*: Tailscale kwa misingi ya kila siku, na Tor kama njia mbadala au kushiriki ufikiaji na mtu bila kuwaalika kwenye VPN yao.



### 4.4 Usalama



Kwa kutumia Tailscale na Umbrel, unaepuka kufichua Umbrel kwenye Mtandao. Nodi ya Umbrel inaweza kufikiwa tu na vifaa vyako vingine vilivyoidhinishwa kwenye tailnet, na hivyo kupunguza kwa kiasi kikubwa eneo la mashambulizi (hakuna mlango ulio wazi kwa wageni, hakuna hatari ya kushambuliwa kwenye huduma ya wavuti kupitia Mtandao).



Mawasiliano yamesimbwa kwa njia fiche (WireGuard) pamoja na usimbaji fiche wowote ambao huduma zako tayari zinafanya (k.m. hata HTTP ya ndani iko kwenye handaki). Bado unaweza kutumia ACL za Tailscale ili, kwa mfano, kuzuia kifaa fulani cha nyuma kufikia Umbrel ikiwa unataka kugawanya mtandao. Umbrel yenyewe haioni tofauti - inadhani inahudumia ndani.



---

Ili kuhitimisha sehemu hii, kuunganisha Tailscale kwenye Umbrel huchukua mibofyo michache tu na **kuboresha sana ufikivu** wa nodi yako inayopangishwa binafsi. Utaweza kusimamia Umbrel na huduma zake ukiwa popote, kwa usalama na kwa ustadi, kana kwamba uko nyumbani. Hili ni suluhisho muhimu sana kwa programu za wakati halisi (Umeme) ambazo zinakabiliwa na muda wa kusubiri wa Tor, au kwa ujumla zaidi kwa mwenyeji yeyote anayetafuta muunganisho rahisi wa faragha. Yote bila kufichua mlango mmoja** kwenye kisanduku chako, na bila usanidi changamano wa mtandao.



## 5. Usimamizi wa hali ya juu na kesi za matumizi



### 5.1 Vipengele vya kina vya mikia



**Udhibiti wa mtandao:** Dashibodi ya usimamizi (login.tailscale.com) hukuruhusu kudhibiti vifaa vyako, kutazama miunganisho na kusanidi sheria za ufikiaji.



**MagicDNS:** Hutatua majina ya vifaa kiotomatiki (k.m. `raspberrypi.tailnet.ts.net`) ili kuepuka kukariri anwani za IP.



**ACL na udhibiti wa ufikiaji:** Bainisha kwa usahihi ni nani anayeweza kufikia kile kwenye mtandao wako kupitia sheria za JSON, zinazofaa kwa kutenga baadhi ya vifaa au kudhibiti ufikiaji wa huduma mahususi.



**Kushiriki Kifaa hukuruhusu kumwalika mtu kufikia mashine mahususi bila kuwapa ufikiaji wa mtandao wako wote.



**Njia ya Subnet:** Mashine ya Tailsscale inaweza kufanya kazi kama lango la lango ndogo nzima, kuwezesha ufikiaji wa vifaa visivyo na Mizani (IoT, vichapishaji, n.k.) kupitia mashine moja iliyosanidiwa.



**Njia ya Ondoka:** Tumia mashine kama lango la Mtandao ili kutoka na IP yake. Inafaa kwa Wi-Fi ya umma au kukwepa vizuizi vya kijiografia.



**Taildrop:** Njia mbadala salama ya AirDrop, inayokuruhusu kuhamisha faili kati ya vifaa vyako vya Tailcale, bila kujali jukwaa au eneo vilipo. Tofauti na AirDrop, ambayo inapatikana tu kwa mfumo ikolojia wa Apple na ukaribu wa kimwili, Taildrop hufanya kazi kati ya vifaa vyako vyote (Windows, Mac, Linux, Android, iOS), hata kama viko katika nchi tofauti. Faili huhamishwa moja kwa moja kati ya vifaa vilivyo na usimbaji fiche kutoka mwisho hadi mwisho, bila kupitia seva kuu. Tumia safu ya amri `faili ya mkia cp` au programu tumizi ya picha ya Interface kulingana na mfumo wako.



### 5.2 Kulinganisha na masuluhisho mengine



**Vs OpenVPN:** Tailscale ni rahisi zaidi kusanidi (hakuna milango ya kufungua, hakuna usimamizi wa cheti) lakini inahusisha utegemezi kwa huduma ya mtu mwingine. OpenVPN inadhibitiwa kikamilifu, lakini inahitaji utaalamu zaidi.



**Kama mshindani wa moja kwa moja, ZeroTier hufanya kazi katika Layer 2 (Ethernet), kuwezesha utangazaji/utangazaji anuwai, huku Tailscale inafanya kazi kwa Layer 3 (IP). ZeroTier inatoa urahisi zaidi wa mtandao, wakati Tailcale inapendelea urahisi wa matumizi.



**Vs Tor:** Tor inatoa kutokujulikana ambayo Tailscale haifanyi, lakini ni ya polepole zaidi. Tor imegatuliwa na haihitaji akaunti, huku Tailscale ina kasi zaidi na inatoa matumizi kama ya LAN.



**Mwongozo dhidi ya WireGuard:** Tailscale hubadilisha kiotomatiki funguo zote na udhibiti wa muunganisho ambao WireGuard ghafi inakuhitaji kushughulikia wewe mwenyewe. Kimsingi ni WireGuard + usimamizi uliorahisishwa wa Layer.



Kwa kumalizia, Tailscale inajiweka kama suluhisho la kisasa, lenye mwelekeo wa urahisi, bora kwa matumizi ya kibinafsi na timu ndogo. Kwa watakasaji wa udhibiti kamili, Headscale inatoa mbadala wa mwenyeji binafsi.



## 6. Hitimisho



**Faida za sura ya mkia:** Tailscale inatoa faida kadhaa kwa upangishaji binafsi:





- Urahisi na utendakazi** - Usakinishaji wa haraka kwenye majukwaa yote bila usanidi changamano wa mtandao. Trafiki hufuata njia ya moja kwa moja kati ya mashine zako (P2P mesh), yenye utendakazi wa itifaki ya WireGuard na hakuna seva kuu ya kupunguza upitishaji.
- Usalama na unyumbulifu** - Usimbaji fiche kutoka mwisho hadi mwisho, sehemu ya mashambulizi iliyopunguzwa, na vipengele vya kina (ACL, SSO/MFA uthibitishaji). Inafanya kazi hata nyuma ya NATs au wakati wa kusonga, na vipanga njia ndogo na nodi za kutoka ili kurekebisha mtandao kulingana na mahitaji yako.



**Vikomo:** Pia kumbuka:





- Utegemezi wa nje** - Katika toleo lake la kawaida, huduma inategemea miundombinu ya Tailscale Inc.. Utegemezi huu unaweza kuepukwa kupitia Headscale (mbadala ya upangishaji binafsi).
- Vikwazo vingine** - Msimbo wa chanzo uliofungwa kwa kiasi, vikwazo vya toleo lisilolipishwa kwa matumizi fulani ya kina, hakuna utumiaji wa Layer 2 (matangazo/utangazaji anuwai), na hitaji la ufikiaji wa Mtandao ili kuanzisha miunganisho.



**Tailscale ni bora kwa waandaji binafsi na timu ndogo, wasanidi programu wanaohitaji ufikiaji wa rasilimali zilizotawanywa, wanaoanza VPN na watumiaji wa simu. Kwa kampuni zinazohitaji udhibiti kamili, suluhu zingine kama vile Headscale au WireGuard moja kwa moja zinaweza kufaa.



**Gundua Headscale kwa upangishaji kamili wa kibinafsi, API na viunganishi vya DevOps (Terraform), au mbadala kama vile Innernet (inayofanana lakini inayojipangisha kikamilifu) na Netmaker.



Tailscale ni zana muhimu ya kujipangisha kibinafsi, kutokana na urahisi na ufanisi wake, na kufanya miundombinu yako ya kibinafsi kufikiwa kana kwamba iko kwenye wingu, huku ukiweka udhibiti nyumbani.



## 7. Rasilimali muhimu



### Nyaraka rasmi





- Kituo cha Hati cha Tailscale**: [docs.tailscale.com](https://docs.tailscale.com) - Hati kamili za Kiingereza, miongozo ya usakinishaji, mafunzo na marejeleo ya kiufundi.
- Jinsi Tailscale inavyofanya kazi**: [Jinsi Tailscale Hufanya kazi](https://tailscale.com/blog/how-tailscale-works) - Makala ya kina yanayofafanua utendakazi wa ndani wa Tailscale.
- Changelog**: [tailscale.com/changelog](https://tailscale.com/changelog) - Ufuatiliaji masasisho na vipengele vipya.



### Miongozo ya vitendo





- Mafunzo ya Homelab**: [tailscale.com/kb/1310/homelab](https://tailscale.com/kb/1310/homelab) - Miongozo mahususi ya kujipangisha mwenyewe.
- Kusanidi Njia ya Kuondoka**: [tailscale.com/kb/1103/exit-nodes](https://tailscale.com/kb/1103/exit-nodes) - Mwongozo wa kina wa kusanidi Njia za Kutoka.
- Tumia Taildrop**: [tailscale.com/kb/1106/taildrop](https://tailscale.com/kb/1106/taildrop) - Hamisha faili kati ya vifaa vya Tailscale.



### Ulinganisho





- Tailscale dhidi ya masuluhisho mengine**: [tailscale.com/compare](https://tailscale.com/compare) - Ulinganisho wa kina na masuluhisho mengine ya VPN na mtandao (ZeroTier, OpenVPN, n.k.).



### Jumuiya





- Reddit**: [r/Tailscale](https://www.reddit.com/r/tailscale/) - Majadiliano, maswali na maoni.
- GitHub**: [github.com/tailscale/tailscale](https://github.com/tailscale/tailscale) - Msimbo wa chanzo cha Mteja, mahali pa kufuatilia maendeleo na kuripoti matatizo.
- Discord**: [discord.gg/tailscale](https://discord.gg/tailscale) - Jumuiya ya watumiaji na wasanidi.



Tailscale mara kwa mara hutoa maudhui mapya na vipengele. Tazama [blogu yao rasmi](https://tailscale.com/blog/) kwa habari za hivi punde na tafiti za matukio.