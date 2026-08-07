---
name: Kusasisha BTCPay Server
description: Tekeleza sasisho la usalama kwenye mfano wako wa BTCPay Server na uhuishe vitambulisho muhimu
---

![jalada](assets/cover.webp)

Kuendesha kichakataji chako mwenyewe cha malipo kunamaanisha kwamba wewe pia ni timu yako mwenyewe ya usalama. Watunzaji wa BTCPay Server wanapochapisha toleo la usalama, hakuna mtu atakayebandika kiraka kwenye mfano wako kwa niaba yako: sasisho, uthibitishaji, na uhuishaji wa vitambulisho unaofuata ni jukumu lako kufanya.

Mafunzo haya yanapitia utaratibu mzima, bila kujali njia uliyotumia kupeleka BTCPay Server: angalia toleo linaloendeshwa, tekeleza sasisho kulingana na aina yako ya upelekaji, thibitisha kuwa limefika kweli, na uhuishe siri ambazo mshambuliaji huenda alizinasa wakati mfano wako ulikuwa hatarini.

Ikiwa bado hujapeleka BTCPay Server, anza na mwongozo wa usakinishaji:

https://planb.academy/tutorials/business/point-of-sale/btcpay-server-928eb01e-824b-4b57-a3e8-8727633beddc

## Udhaifu mkubwa wa Agosti 2026

⚠️ **Tahadhari muhimu ya usalama (7 Agosti 2026):** udhaifu mkubwa unaoathiri BTCPay Server unatumiwa vibaya kwa sasa na unaweza kusababisha upotevu wa fedha. Sasisha mfano wako hadi **toleo 2.4.2** mara moja kupitia `Admin Dashboard > Server > Maintenance > Update`, kisha hakiki kuwa sehemu ya chini ya ukurasa inaonyesha `2.4.2`. Ikiwa huwezi kusasisha papo hapo, zima BTCPay Server yako. Baada ya kusasisha, ni lazima pia uhuishe kabisa macaroons zako na `macaroons.db` yako, uhuishe kabisa nyuzi za uthibitishaji za mfumo wowote mwingine wa nyuma wa Lightning, na, ikiwa ulitengeneza pochi ya moto ya on-chain ndani ya BTCPay Server, hamisha fedha hizo na uunde upya pochi hiyo. Waunganishaji wanapaswa pia kusasisha NBXplorer hadi toleo 2.6.10. Chanzo: [Maelezo ya toleo la BTCPay Server 2.4.2](https://github.com/btcpayserver/btcpayserver/releases/tag/v2.4.2).

Toleo 2.4.2 lilichapishwa tarehe 7 Agosti 2026. Maelezo ya toleo yanasema kuwa linasahihisha udhaifu mkubwa uliokuwa tayari unatumiwa vibaya hadharani, ulioripotiwa na `brunoerg` na `benthecarman` kupitia juhudi za Bitcoin Red Team. Toleo hilo hilo pia linasahihisha njia ya kukwepa uthibitishaji wa hatua mbili wa TOTP kupitia uthibitishaji wa Greenfield Basic, na huzima uthibitishaji wa Greenfield Basic kwa chaguomsingi dakika tano baada ya akaunti kuundwa.

Matokeo mawili yanafuata kutoka kwa "unatumiwa vibaya kwa sasa":

- **Kusasisha si hiari na si jambo la kupanga kwa wiki ijayo.** Mfano usio na kiraka unaoweza kufikiwa kutoka kwenye intaneti lazima ama usasishwe au uzimwe.
- **Kusasisha pekee hakutoshi.** Ikiwa mfano wako uliathiriwa kabla ya kuweka kiraka, mshambuliaji huenda tayari ana nakala za vitambulisho vyako vya Lightning na za nyenzo zozote za funguo za pochi ya moto ambazo BTCPay Server ilikutengenezea. Siri hizo hubaki halali baada ya sasisho hadi uziuhuishe. Sehemu ya uhuishaji hapa chini ndiyo sehemu ambayo watu huruka, na ndiyo sehemu inayolinda fedha zako kweli.

## Hatua ya 1 — Tambua ni toleo gani unaendesha

Ingia kwenye BTCPay Server yako na uangalie **sehemu ya chini ya ukurasa wowote**: mfuatano wa toleo unaonyeshwa hapo. Unaweza pia kufungua `Admin Dashboard > Server > Maintenance`, ambayo inaonyesha toleo la sasa na vidhibiti vya sasisho.

Ikiwa mfano wako unaonyesha Greenfield API, `GET /api/v1/server/info` pia hurejesha toleo.

Chochote kilicho chini ya `2.4.2` kina udhaifu.

## Hatua ya 2 — Sasisha

### Upelekaji wa Docker unaojipangisha mwenyewe (usakinishaji wa kawaida)

Hii inashughulikia upelekaji rasmi wa Docker, ambao ndio unaopata kutoka kwenye nyaraka za BTCPay Server, kutoka kwa kizindua cha mbofyo mmoja cha LunaNode, na kutoka kwa usakinishaji mwingi wa VPS.

Njia rahisi zaidi ni kiolesura cha wavuti:

1. Nenda kwenye `Admin Dashboard > Server > Maintenance`.
2. Bofya **Update**.
3. Subiri containers zivutwe na kuanzishwa upya. Kiolesura hakitapatikana kwa dakika chache.

Ikiwa kiolesura cha wavuti hakifikiwi, au unapendelea kuona kumbukumbu, fanya kupitia SSH:

```bash
sudo su -
cd "$BTCPAY_BASE_DIRECTORY/btcpayserver-docker"
. ./btcpay-update.sh
```

Kwenye usakinishaji wa chaguomsingi `$BTCPAY_BASE_DIRECTORY` ni `/root`, kwa hivyo saraka ni `/root/btcpayserver-docker`. Script huvuta images za hivi karibuni, huunda upya containers, na kuchapisha matoleo yanayotokana nayo.

Upelekaji wa Docker huja na NBXplorer pamoja na BTCPay Server, kwa hivyo sasisho la kawaida pia huleta NBXplorer kwenye `2.6.10` linalopendekezwa. Ikiwa unaendesha NBXplorer kando — jambo la kawaida kwa waunganishaji na kwa stacks maalum — isasishe waziwazi.

### Umbrel

Fungua dashibodi ya Umbrel, nenda kwenye **App Store**, tafuta BTCPay Server na tekeleza sasisho ikiwa linapatikana.

⚠️ **Muhimu:** vifurushi vya app-store hufungashwa upya na timu ya Umbrel na vinaweza kuchelewa nyuma ya upstream kwa saa au siku. Angalia toleo kwenye sehemu ya chini ya ukurasa ya BTCPay Server baada ya kusasisha. Ikiwa bado liko chini ya `2.4.2`, **simamisha app** kutoka kwenye dashibodi ya Umbrel na usubiri toleo lililofungashwa badala ya kuacha mfano wenye udhaifu ukiendelea kufanya kazi.

Mwongozo maalum wa Umbrel unashughulikia app yenyewe:

https://planb.academy/tutorials/business/point-of-sale/btcpay-server-umbrel-68e1c535-4322-4507-a69c-9dfcbc36dfd1

### Start9 / StartOS

Mantiki ni ile ile: sasisha BTCPay Server kutoka marketplace ya StartOS, kisha thibitisha toleo kwenye sehemu ya chini ya ukurasa. Ikiwa toleo lililofungashwa bado si `2.4.2`, simamisha huduma hadi liwe hilo.

### Hosting inayosimamiwa na ya wahusika wengine

Ikiwa mtu mwingine anaendesha mfano wako (mtoa hosting, chama, seva ya rafiki), bado unahitaji uthibitisho. Muulize mwendeshaji mfuatano wa toleo unaoonyeshwa kwenye sehemu ya chini ya ukurasa, na uliza waziwazi kama uhuishaji wa vitambulisho baada ya sasisho ulioelezwa hapa chini umefanywa. "Tumesasisha" si jibu sawa na "tumehuisha macaroons zako".

## Hatua ya 3 — Thibitisha kuwa sasisho limefika kweli

Pakia upya kiolesura cha BTCPay Server na soma toleo kwenye sehemu ya chini ya ukurasa. Lazima lionyeshe `2.4.2` au la juu zaidi.

Usitegemee amri ya kusasisha kumalizika bila hitilafu: kwenye mashine zenye rasilimali finyu, kuvuta image kunaweza kushindwa kimyakimya na kuacha container iliyopita ikiendelea kufanya kazi. Soma toleo, kila mara.

## Hatua ya 4 — Huisha vitambulisho vyako

Hii ndiyo hatua inayobadilisha "imewekewa kiraka" kuwa "salama". Kwa sababu udhaifu ulikuwa unatumiwa vibaya kabla ya marekebisho kutolewa, chukulia kila siri ambayo mfano wako ulikuwa nayo kama kitu ambacho huenda kinajulikana na mshambuliaji.

### Lightning: LND

Tengeneza upya macaroons **na** faili ya `macaroons.db`. Kufuta faili za macaroon pekee hakutoshi — LND hutengeneza macaroons kutoka kwa ufunguo mzizi uliohifadhiwa kwenye `macaroons.db`, kwa hivyo mshambuliaji mwenye nakala ya macaroon ya zamani anaendelea kuwa na ufikiaji hadi hifadhidata hiyo iundwe upya.

Utaratibu ni: simamisha LND, ondoa `macaroons.db` na faili za `*.macaroon` kutoka kwenye saraka ya mtandao (kwa mainnet, `data/chain/bitcoin/mainnet/` ndani ya saraka ya data ya LND), kisha anzisha upya na ufungue LND, ambayo itaziunda upya. Hifadhi nakala ya saraka kwanza, na unganisha upya kila programu iliyotumia macaroons za zamani — BTCPay Server yenyewe, Zeus, Thunderhub, RTL, Alby, na script yoyote uliyoandika.

Ikiwa pia unaonyesha LND kwenye intaneti, hakiki cheti chake cha TLS na vitambulisho vyovyote vya `lnd.conf` kwa wakati huo huo.

### Lightning: mifumo mingine ya nyuma

Chochote kinachojithibitisha kwenye nodi yako kwa mfuatano lazima kipate mfuatano mpya:

- **Core Lightning**: tengeneza upya rune au vitambulisho vya ufikiaji vinavyotumiwa na muunganisho.
- **Phoenixd**: badilisha nenosiri la HTTP.
- **LNbits na zinazofanana**: batilisha na utoe upya funguo za admin na za invoisi.
- **Nyuzi za muunganisho wa nodi ya mbali** zilizohifadhiwa kwenye mipangilio ya duka la BTCPay Server: ziandike upya kwa siri mpya.

### Pochi ya moto ya on-chain iliyotengenezwa ndani ya BTCPay Server

Ikiwa uliruhusu BTCPay Server ikutengenezee pochi ya on-chain — tofauti na kuunganisha hardware wallet au kuingiza xpub ambayo funguo zake hazijawahi kugusa seva — seed hiyo iliishi kwenye mashine.

Ichukulie kama imeungua:

1. Unda pochi mpya, kwa ubora zaidi kwa hardware wallet ili funguo zisikae tena kwenye seva.
2. Sweep fedha kutoka pochi ya zamani kwenda kwenye mpya.
3. Badilisha mpango wa derivation kwenye mipangilio ya duka kwa pochi mpya.
4. Usiwahi kutumia tena seed ya zamani.

Mipangilio ya watch-only (xpub au hardware wallet) haihitaji hili: funguo za siri hazikuwa kamwe kwenye seva. Hii ndiyo hasa sababu mwongozo wa usakinishaji unazipendekeza.

### Akaunti za BTCPay Server na funguo za API

Wakati uko hapo:

- Badilisha manenosiri ya kila akaunti ya mtumiaji kwenye mfano huo.
- Batilisha na utoe upya **funguo zote za API** za Greenfield.
- Jiandikishe upya kwa uthibitishaji wa hatua mbili, kwa kuwa 2.4.2 husahihisha njia ya kukwepa 2FA.
- Fungua `Admin Dashboard > Server > Users` na hakiki kuwa hakuna akaunti isiyotarajiwa iliyopo.
- Hakiki **payouts**, **pull payments** na **refunds** za hivi karibuni kwa maingizo ambayo hukuunda.
- Hakiki webhooks zako na siri zake.

## Hatua ya 5 — Endelea kupata taarifa kwa tukio lijalo

Matoleo ya usalama huwasaidia tu waendeshaji wanaoyasikia:

- Fuatilia [matoleo ya BTCPay Server kwenye GitHub](https://github.com/btcpayserver/btcpayserver/releases) — GitHub inaweza kukutumia barua pepe kwa kila toleo jipya la repository.
- Fuata njia za matangazo za mradi na [blogu rasmi](https://blog.btcpayserver.org/).
- Weka mfano wako kwenye toleo unaloweza kusasisha haraka: kadiri unavyokuwa nyuma zaidi, ndivyo sasisho la dharura linavyozidi kuwa chungu.

Kujipangisha mwenyewe hukupa mamlaka juu ya malipo yako. Gharama ya mamlaka hiyo ni hasa hii: kusoma maelezo ya toleo na kuwa mtu anayebandika viraka.
