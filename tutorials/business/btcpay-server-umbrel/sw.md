---
name: BTCPay Server - Umbrel
description: Kusakinisha na kutumia Seva ya BTPay kwenye Umbrel ili kukubali Bitcoin na Umeme
---

![cover](assets/cover.webp)



Katika mfumo ikolojia wa Bitcoin, kukubali malipo kunawakilisha changamoto kubwa kwa wafanyabiashara na wafanyabiashara. Suluhu za kitamaduni, iwe za benki (kadi za mkopo, Stripe, PayPal) au hata Bitcoin (BitPay, Coinbase Commerce), hutoza wapatanishi ambao hutoza ada kubwa, kukusanya data nyeti ya biashara yako, na wanaweza kuzuia au kukagua miamala yako kwa matakwa yao. Utegemezi huu unakinzana na kanuni za kimsingi za Bitcoin za ugatuaji, usiri na uhuru wa kifedha.



BTCPay Server inajitokeza kama jibu la chanzo huria kwa tatizo hili. Kichakataji hiki cha malipo kinachojipangisha kibinafsi hubadilisha node yako ya Bitcoin kuwa muundo msingi wa kitaalamu, bila mtu wa kati, hakuna ada za ziada za usindikaji na hakuna maelewano kwenye faragha. Imeundwa na jumuiya ya kimataifa ya wachangiaji tangu 2017, BTCPay Server hukuruhusu kupokea malipo ya Bitcoin na Lightning moja kwa moja kwenye wallet zako, ikibaki na udhibiti kamili wa pesa zako kila wakati.



Kijadi, kusakinisha BTCPay Server kunahitaji ujuzi wa hali ya juu wa kiufundi: usanidi wa seva ya Linux, umilisi wa Docker, udhibiti wa cheti cha SSL na usalama wa mtandao. Umbrel hubadilisha mbinu hii kwa usakinishaji wa mbofyo mmoja uliounganishwa moja kwa moja na Bitcoin yako na node ya Lightning. Urahisishaji huu hufanya kile ambacho hapo awali kilihifadhiwa kwa mafundi wenye uzoefu kupatikana kwa kila mtu.



**Muhimu kuelewa**: BTPay Server kwenye Umbrel hufanya kazi kwa chaguomsingi kwenye mtandao wa ndani pekee. Unaweza kuunda ankara, kukubali malipo ya Lightning na Bitcoin, na kudhibiti uhasibu wako kutoka kwa kifaa chochote kilichounganishwa kwenye mtandao wako wa nyumbani (kompyuta, simu mahiri, kompyuta kibao). Mipangilio hii ni bora kwa malipo ya huduma za ana kwa ana, kudhibiti malipo ya ana kwa ana au kutumia BTCPay Server kutoka mtandao wa ndani. Kwa upande mwingine, ili kujumuisha BTCPay Server kwenye duka la mtandaoni ambalo linapatikana kwa umma kwenye Mtandao, usanidi wa ziada wenye udhihirisho wa umma utahitajika (tutashughulikia suala hili mwishoni mwa mafunzo).



Mafunzo haya yanakupeleka katika usakinishaji kamili wa BTCPay Server kwenye Umbrel, kusanidi Bitcoin wallet na node ya Lightning, kuunda na kulipa ankara, na kudhibiti kuripoti uhasibu. Utagundua jinsi ya kutumia BTCPay Server kwa ufanisi kwenye mtandao wako wa karibu, na kisha tutaangalia masuluhisho ya kuonyesha hadharani ikiwa ungependa kuiunganisha na tovuti ya biashara ya mtandaoni.



## Masharti



Ili kufuata mafunzo haya, unahitaji kuwa na Umbrel iliyosakinishwa kwa usahihi na kusanidiwa. Ikiwa bado hujafanya hivyo, tafadhali tazama mafunzo yetu kuhusu usakinishaji wa Umbrel.



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

Node yako ya Bitcoin Core lazima ilandanishwe kikamilifu na blockchain (100% katika programu ya Umbrel ya Bitcoin). Usawazishaji huu wa kwanza huchukua kati ya siku 3 na wiki 2, kulingana na maunzi yako na muunganisho wa Mtandao.



Ili kukubali malipo ya papo hapo ya Lightning, utahitaji pia kusakinisha LND (Lightning Network Daemon) kwenye Umbrel. Tazama mafunzo yetu kuhusu kusakinisha na kusanidi LND kwenye Umbrel ikiwa ungependa kuwezesha kipengele hiki.



https://planb.academy/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

Ruhusu angalau GB 50 ya nafasi ya diski bila malipo kwa BTPay Server, hifadhidata zake na data ya Lightning. Muunganisho thabiti wa Mtandao kupitia kebo ya Ethaneti unapendekezwa sana ili kuepuka kukatwa.



## Kufunga BTPay Server kwenye Umbrel



Kutoka kwa kiolesura cha Umbrel (`umbrel.local`), fikia App Store na utafute "BTCPay Server" katika kategoria ya Bitcoin.



![Interface Umbrel App Store avec BTCPay Server](assets/fr/01.webp)



Bofya Sakinisha. Umbrel hukagua kiotomatiki kuwa Bitcoin Core na LND zimewekwa, kisha huanza kupeleka (dakika 2-5).



![Dépendances requises pour BTCPay Server](assets/fr/02.webp)



Mara tu ikiwa imewekwa, fungua programu. Utahitaji kuunda akaunti ya msimamizi iliyo na vitambulisho thabiti.



![Création du compte administrateur BTCPay Server](assets/fr/03.webp)



Baada ya kufungua akaunti yako, BTCPay Server itakuelekeza mara moja usanidi duka lako la kwanza. Chagua jina la biashara na uchague sarafu ya marejeleo (EUR, USD au BTC).



![Création du premier magasin BTCPay Server](assets/fr/04.webp)



## Fikia BTPay Server kwenye mtandao wako wa karibu



BTPay Server inaweza kufikiwa kutoka kwa kifaa chochote kwenye mtandao wa ndani (WiFi au Ethernet). Ufikiaji kutoka kwa kivinjari chako hadi:



```url
http://umbrel.local
```



Au moja kwa moja kwa:



```url
http://umbrel.local:3003
```



**Ufikiaji wa mbali ukitumia Tailscale**: Ili kufikia BTCPay Server kutoka popote duniani, tumia Tailscale. VPN hii salama hukuruhusu kuunganisha kwa Umbrel yako kana kwamba uko kwenye mtandao wa karibu nawe. Tazama mafunzo yetu yaliyotolewa kwa Tailscale kwenye Umbrel.



https://planb.academy/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

## Inasanidi kwingineko yako ya Bitcoin



Ili kukubali malipo, unahitaji kusanidi Bitcoin wallet. BTPay Server huonyesha chaguo za usanidi kwenye dashibodi.



![Tableau de bord avec options de configuration de portefeuille](assets/fr/05.webp)



Ili kusanidi wallet Bitcoin, nenda kwa "Wallet" > "Bitcoin".



Una chaguo mbili: kuunda kwingineko mpya moja kwa moja katika BTPay, au leta kwingineko iliyopo. Kwa kuagiza, njia kadhaa zinapatikana:




- **Unganisha Hardware wallet** (inapendekezwa): Leta funguo zako za umma kupitia programu ya Vault
- **Ingiza faili ya wallet** (inapendekezwa): Pakia faili iliyohamishwa kutoka kwa kwingineko yako
- **Weka ufunguo uliopanuliwa wa umma**: Weka XPub/YPub/ZPub yako wewe mwenyewe
- **Changanua msimbo wa wallet QR** : Changanua msimbo wa QR kutoka BlueWallet, Cobo Vault, Pasipoti au Specter DIY
- **Ingiza wallet seed** (haipendekezwi) : Andika maneno yako ya kurejesha uwezo wa kufikia maneno 12 au 24



![Options de création de portefeuille](assets/fr/06.webp)



Kwa mafunzo haya, tutaunda Hot wallet mpya: kwa hivyo ufunguo wa kibinafsi utahifadhiwa kwenye seva yetu ya Umbrel. Katika kesi hii, tunakushauri sana kuhamisha fedha mara kwa mara kwenye cold wallet ili kuepuka kuhifadhi kiasi kikubwa kwenye seva.



![Choix entre Hot wallet et Watch-only wallet](assets/fr/07.webp)



Baada ya kusanidiwa, BTPay Server inathibitisha kuwa wallet yako iko tayari kukubali malipo ya on-chain.



![Portefeuille Bitcoin configuré avec succès](assets/fr/08.webp)



## Washa Lightning Network



Ili kukubali malipo ya papo hapo ya Lightning, nenda kwenye Wallets > Lightning. Kisha, kwa vile node yako ya LND tayari iko kwenye Umbrel, bofya tu kitufe cha "Hifadhi" ili kuthibitisha muunganisho kati ya Seva yako ya BTCPay na node yako ya Lightning.



![Configuration du nœud Lightning](assets/fr/09.webp)



## Unda na ulipe ankara



Katika kiolesura cha BTCPay Server, nenda kwenye Ankara > Unda Invoice. Weka kiasi, ongeza maelezo ya hiari, na ubofye Unda.



![Création d'une nouvelle facture](assets/fr/10.webp)



Kisha unaweza kubofya kitufe cha "Checkout" ili kuonyesha ankara. Kisha BTCPay hutengeneza ankara iliyo na msimbo wa QR uliounganishwa (BIP21) iliyo na anwani ya Bitcoin na ankara ya Lightning.



![Détails de la facture générée](assets/fr/11.webp)



Mteja wako anaweza kuchanganua msimbo wa QR na wallet yoyote inayooana.



![Page de paiement avec QR code](assets/fr/12.webp)



Baada ya kulipwa, ankara inakuwa "Imetulia" katika suala la sekunde kwa Lightning.



![Confirmation de paiement réussi](assets/fr/13.webp)



## Usimamizi wa malipo na ufuatiliaji



Katika sehemu ya "Kuripoti", kichupo cha "Ankara", utapata historia kamili ya ankara zako zenye tarehe, kiasi, hali na njia ya kulipa. Unaweza kuihamisha ikiwa inahitajika.



![Section reporting avec l'historique des factures](assets/fr/14.webp)



## Usanidi wa duka



BTPay Server hukuruhusu kudhibiti maduka mengi yenye vigezo tofauti. Kila duka linawakilisha huluki tofauti ya biashara: duka la e-commerce, sehemu halisi ya mauzo, au malipo ya huduma.



Katika mipangilio ya duka, utapata sehemu kadhaa muhimu:



![Paramètres du magasin](assets/fr/15.webp)





- **Mipangilio ya Jumla**: Jina la duka, sarafu ya marejeleo (BTC, EUR, USD), muda wa mwisho wa ankara (dakika 15 chaguomsingi), idadi ya uthibitishaji wa blockchain inahitajika.
- **Viwango**: Usanidi wa vyanzo vya viwango vya ubadilishaji na ubadilishaji wa fiat/Bitcoin
- **Muonekano wa Malipo**: Geuza kukufaa mwonekano wa kurasa zako za malipo (nembo, rangi, ujumbe uliobinafsishwa)
- **Mipangilio ya Barua Pepe**: Usanidi wa arifa za barua pepe kwa malipo yaliyopokelewa
- **Token za Ufikiaji**: Usimamizi wa tokeni za API za miunganisho ya biashara ya mtandaoni (WooCommerce, Shopify, n.k.)
- **Watumiaji**: Dhibiti ufikiaji wa mtumiaji kwenye duka kwa viwango tofauti vya ruhusa (Mmiliki, Mgeni)
- **Webhook**: Usanidi wa Webhook kwa maingiliano ya wakati halisi na uhasibu wako au mfumo wa ERP



BTCPay Server pia inatoa sehemu ya programu-jalizi ili kupanua utendaji kwa miunganisho ya biashara ya mtandaoni, mifumo ya mauzo na zana za ziada.



![Gestion des plugins](assets/fr/16.webp)



## Faida na vikwazo vya matumizi ya ndani



**Faida za BTCPay Server juu ya Umbrel** :




- Mamlaka kamili: udhibiti wa kipekee wa funguo na fedha za kibinafsi, hakuna mhusika mwingine anayeweza kusimamisha au kudhibiti malipo yako.
- Akiba kubwa: gharama ya mtandao wa Bitcoin pekee (senti chache kwa Lightning) dhidi ya 2-3% kwa vichakataji vya jadi.
- Usiri wa juu zaidi: hakuna usajili, uthibitishaji wa utambulisho au kushiriki data na makampuni mengine
- Usanifu wa chanzo huria huhakikisha uwazi, ukaguzi na uendelevu kupitia jumuiya kubwa ya wasanidi programu
- Ufungaji rahisi kupitia Umbrel, bila hitaji la ujuzi wa hali ya juu wa kiufundi



**Vikwazo muhimu** :




- **Mtandao wa ndani pekee**: BTCPay Server kwenye Umbrel inapatikana tu kutoka kwa mtandao wako wa nyumbani. Ni kamili kwa malipo ya ana kwa ana, huduma za kujitegemea au biashara ndogo ndogo, lakini hazifai kwa maduka ya mtandaoni yanayopatikana kwa umma.
- Wajibu kamili wa kiufundi: matengenezo ya node, salama za mara kwa mara, ufuatiliaji wa uunganisho
- Udhibiti wa ukwasi wa Lightning: kufungua na kudhibiti chaneli zenye uwezo wa kutosha wa kuingia
- Usaidizi mdogo kwa nyaraka za jumuiya na vikao, vinavyohitaji uhuru zaidi kuliko idara ya kibiashara ya huduma kwa wateja



Kizuizi hiki cha mtandao wa ndani ndicho kikwazo kikuu cha kuunganisha BTCPay Server kwenye duka la e-commerce, ambapo wateja wanahitaji kuwa na uwezo wa kufikia kurasa za malipo kutoka popote kwenye Mtandao.



## Mbinu bora na usalama



Washa chelezo otomatiki za Umbrel na uhifadhi nakala kwenye media ya nje (USB stick, disk kuu, Encrypted cloud storage). Weka seed zako za Bitcoin (maneno ya uokoaji) katika sehemu salama, iliyo tofauti. Hifadhi nakala rudufu ya faili ya chaneli ya LND kwa uokoaji wa Lightning.



Fuatilia mara kwa mara usawazishaji wa Bitcoin Core, chaneli za Lightning na majibu ya BTCPay Server. Jaribio rahisi la kila wiki: generate na ulipe bili kwa satoshi chache. Sasisha Umbrel (viraka vya usalama, viboreshaji). Weka nakala kabla ya sasisho kuu. Kwa matumizi ya kitaaluma, zingatia ufuatiliaji wa nje (UptimeRobot) na arifa za barua pepe/SMS.



## Kufichua BTPay Server hadharani kwa duka la mtandaoni



Ili kujumuisha BTCPay Server kwenye duka la biashara ya mtandaoni (WooCommerce, Shopify, n.k.), wateja wako wanahitaji kuwa na uwezo wa kufikia kurasa za malipo kutoka popote, si tu mtandao wako wa ndani.



**Suluhisho: Kidhibiti Wakala wa Nginx**



Unaweza kufichua BTCPay Server hadharani kwa kutumia Kidhibiti Wakala wa Nginx (inapatikana katika Duka la Programu la Umbrel). Suluhisho hili linahitaji:




- Domain name (la kawaida au lisilolipishwa kupitia DuckDNS, No-IP, Afraid.org)
- Inasanidi usambazaji wa mlango (PORT 80 na 443) kwenye router yako
- Usakinishaji wa Kidhibiti Wakala wa Nginx, ambacho hudhibiti kiotomatiki vyeti vya SSL



Usanidi huu unafichua seva yako kwenye Mtandao na unahitaji umakini wa ziada (nenosiri kali, 2FA, masasisho ya mara kwa mara). Tutakuwa tunatayarisha mafunzo maalum yanayoelezea utaratibu huu kamili.



## Hitimisho



BTCPay Server kwenye Umbrel inachanganya nguvu ya node ya Bitcoin na urahisi wa Umbrel ili kuunda miundombinu ya malipo ya kitaalamu inayojiendesha yenyewe inayofikiwa na wote. Mamlaka hii ya kifedha inakuja na jukumu la matengenezo, lakini Umbrel hurahisisha mzigo wa uendeshaji ikilinganishwa na manufaa: kuondoa ada za usindikaji, ulinzi wa faragha yako, upinzani dhidi ya udhibiti na udhibiti kamili wa fedha zako.



Matumizi ya mtandao wa ndani tayari yanajumuisha aina mbalimbali za maombi: malipo ya huduma za kujitegemea, malipo ya ana kwa ana, maduka madogo ya kimwili, au kujifunza tu na kufanya majaribio ya Bitcoin na Lightning katika mazingira yanayodhibitiwa. Kwa mahitaji ya biashara ya mtandaoni yanayohitaji kufichuliwa kwa umma, suluhisho la Kidhibiti Wakala wa Nginx lipo, lakini linahitaji usanidi wa ziada wa kiufundi, ambao tutaelezea kwa undani katika mafunzo mahususi.



Iwe unaendesha biashara, mradi mpya au unajaribu tu, BTCPay Server kwenye Umbrel inatoa uhuru kamili wa kifedha. Njia huanza na duka lako la kwanza, ankara yako ya kwanza, malipo yako ya kwanza kupokea moja kwa moja kwenye miundombinu yako huru.



## Rasilimali



### Nyaraka rasmi




- [Tovuti rasmi ya BTCPay Server](https://btcpayserver.org)
- [Kamilisha hati za BTCPay Server](https://docs.btcpayserver.org)
- [Seva ya GitHub BTCPay](https://github.com/btcpayserver/btcpayserver)
- [Hati za muundo wa tail](https://tailscale.com/kb)


### Jumuiya na msaada




- [Seva ya BTCPay ya Jukwaa](https://chat.btcpayserver.org)
- [Mwavuli wa Jukwaa](https://community.getumbrel.com)
- [Reddit r/BTCPayServer](https://reddit.com/r/BTCPayServer)
