---
name: Kwagura BTCPay Server
description: Shira ku rubuga rwawe rwa BTCPay Server ukwagura kw'umutekano hanyuma uhindure ivyemezo vyo kwinjira vy'ingenzi
---

![cover](assets/cover.webp)

Kwikorera ubwawe uburyo bwo kwishuza bisigura ko uri na wewe nyene umugwi wawe w'umutekano. Igihe abacungera BTCPay Server basohoye version y'umutekano, nta n'umwe azogukosorera urubuga rwawe: ukwagura, ugusuzuma, n'ukuhindura ivyemezo vyo kwinjira bikurikira, ni wewe ubwirizwa kubikora.

Iyi nyigisho iraca mu nzira yose, uburyo waba warashizemwo BTCPay Server bwose: suzuma version iriko irakora, ushire ukwagura hisunzwe ubwoko bw'ishirwaho ryawe, wemeze ko kwashitse vy'ukuri, hanyuma uhindure amabanga umugizi wa nabi ashobora kuba yarafashe mu gihe urubuga rwawe rwari rufise intege nke.

Nimba utarashira BTCPay Server ahantu na hamwe, tangura ku nyigisho yo kuyishiramwo:

https://planb.academy/tutorials/business/point-of-sale/btcpay-server-928eb01e-824b-4b57-a3e8-8727633beddc

## Ikinenge gikomeye co muri Myandagaro 2026

⚠️ **Inkuru ihutirwa yerekeye umutekano (itariki 7 Myandagaro 2026):** hari ikinenge gikomeye kiri muri BTCPay Server kirimo gukoreshwa nabi n'abagizi ba nabi, kandi gishobora gutuma uta amahera yawe. Nuce ushira urubuga rwawe kuri **version 2.4.2** ata gutebagana, uciye kuri `Admin Dashboard > Server > Maintenance > Update`, hanyuma wihweze ko epfo y'urupapuro heretse `2.4.2`. Nimba udashobora kuvyagura ubu nyene, zimya BTCPay Server yawe. Iyo umaze kuvyagura, urakwiye kandi guhindura burundu macaroons yawe hamwe na `macaroons.db` yawe, guhindura burundu imirongo y'ukwemezwa (authentication strings) y'ubundi buryo bwose bwa Lightning ukoresha, kandi, nimba waratanguje ikibindi (hot wallet) co on-chain muri BTCPay Server, imura ayo mahera hanyuma wongere uremeko ikibindi gishasha. Abashira hamwe za sisiteme (integrators) bakwiye kandi kwagura NBXplorer bakayishira kuri version 2.6.10. Aho vyavuye: [Ivyanditswe ku gusohorwa kwa BTCPay Server 2.4.2](https://github.com/btcpayserver/btcpayserver/releases/tag/v2.4.2).

Version 2.4.2 yasohotse ku wa 7 Myandagaro 2026. Ivyanditswe ku gusohorwa bivuga ko ikosora ikinenge gikomeye cari kimaze gukoreshwa nabi mu buzima busanzwe, catangajwe na `brunoerg` na `benthecarman` biciye ku gikorwa ca Bitcoin Red Team. Iyo version nyene irakosora kandi uburyo bwo kurenga ku kwemeza kabiri kwa TOTP biciye kuri Greenfield Basic authentication, kandi izimya Greenfield Basic authentication mu buryo bwisanzwe inyuma y'iminota itanu konti ivutse.

Ingaruka zibiri zikurikira ayo majambo "kiriko kirakoreshwa nabi":

- **Kwagura si ico guhitamwo kandi si ico kurindiriza indwi iza.** Urubuga rutarakosorwa rushobora gushikirwa kuri internet rutegerezwa canke kwagurwa canke kuzimywa.
- **Kwagura kwonyene ntibihagije.** Nimba urubuga rwawe rwarahungabanijwe imbere y'uko ukosora, umugizi wa nabi ashobora kuba asanzwe afise kopi z'ivyemezo vyawe vya Lightning n'iz'imfunguruzo zose za hot wallet BTCPay Server yagukoreye. Ayo mabanga aguma akora inyuma y'ukwagura gushika uyahinduye. Igice co guhindura ivyemezo kiri hasi ni co abantu basimba, kandi ni co vy'ukuri gikingira amahera yawe.

## Intambwe ya 1 — Menya version uriko urakoresha

Injira muri BTCPay Server yawe hanyuma uraba **epfo y'urupapuro urwo ari rwo rwose**: umurongo werekana version werekanwa ng'aho. Urashobora kandi gufungura `Admin Dashboard > Server > Maintenance`, hakwereka version iriho ubu n'utuboneza two kwagura.

Nimba urubuga rwawe rwugururiye Greenfield API, `GET /api/v1/server/info` na yo yerekana version.

Ikintu cose kiri munsi ya `2.4.2` gifise intege nke.

## Intambwe ya 2 — Kwagura

### Ishirwaho rya Docker wiyakiriye (uburyo busanzwe bwo gushiramwo)

Ivyo bijanye n'ishirwaho rya Docker ryemewe, ari ryo uronka mu vyandiko vya BTCPay Server, mu gatuboneza ka LunaNode ko gukanda rimwe, no mu bwinshi bw'ishirwaho ku ma VPS.

Inzira yoroshe kuruta ni interface y'urubuga:

1. Genda kuri `Admin Dashboard > Server > Maintenance`.
2. Kanda kuri **Update**.
3. Rindira ko ama container amanurwa hanyuma agasubira gutangurwa. Interface izobura mu minota mikeyi.

Nimba interface y'urubuga idashikirwa, canke ukunda kubona ama logs, bikore uciye kuri SSH:

```bash
sudo su -
cd "$BTCPAY_BASE_DIRECTORY/btcpayserver-docker"
. ./btcpay-update.sh
```

Ku ishirwaho risanzwe `$BTCPAY_BASE_DIRECTORY` ni `/root`, ku buryo dosiye ari `/root/btcpayserver-docker`. Iyo script imanura ama images aheruka, ikongera igakora ama container, hanyuma ikandika za version zavuyemwo.

Ishirwaho rya Docker rizana NBXplorer kumwe na BTCPay Server, ku buryo ukwagura gusanzwe kuzana na NBXplorer kuri `2.6.10` ihanurwa. Nimba ukoresha NBXplorer ukwayo — nk'uko bisanzwe ku bashira hamwe za sisiteme (integrators) no ku ntunganyo zihariye — uyagure ku buryo bwiyerekana.

### Umbrel

Fungura urubuga rwa Umbrel, genda muri **App Store**, urondere BTCPay Server hanyuma ushire ukwagura nimba kuriho.

⚠️ **Ikintu gihambaye:** ama paki yo muri app-store apakirwa bushasha n'umugwi wa Umbrel kandi ashobora gusigara inyuma y'aho ivyo bikorwa bivuye ku masaha canke ku misi. Suzuma version epfo y'urupapuro rwa BTCPay Server inyuma yo kwagura. Nimba ikiri munsi ya `2.4.2`, **hagarika iyo app** uhereye ku rubuga rwa Umbrel maze urindire iyo paki isohoka aho kureka urubuga rufise intege nke rugakora.

Inyigisho yihariye ya Umbrel iravuga kuri iyo app ubwayo:

https://planb.academy/tutorials/business/point-of-sale/btcpay-server-umbrel-68e1c535-4322-4507-a69c-9dfcbc36dfd1

### Start9 / StartOS

Ni ukwo nyene: agura BTCPay Server uhereye kuri marketplace ya StartOS, hanyuma wemeze version epfo y'urupapuro. Nimba version yapakiwe itari `2.4.2`, hagarika iyo service gushika ivyo bishitse.

### Ubwakiranyi bucungerwa n'abandi

Nimba uwundi muntu ari we acungera urubuga rwawe (uwutanga ubwakiranyi, ishirahamwe, server y'umugenzi), uracakeneye ivyemezo. Baza uwo abicungera umurongo wa version werekanwa epfo y'urupapuro, kandi umubaze ku mugaragaro nimba ukuhindura ivyemezo vyo kwinjira inyuma y'ukwagura, kwasobanuwe hasi, kwarakozwe. "Twaraguye" si inyishu imwe na "Twarahinduye macaroons zawe".

## Intambwe ya 3 — Wemeze ko ukwagura kwashitse vy'ukuri

Subira utangure interface ya BTCPay Server hanyuma usome version epfo y'urupapuro. Itegerezwa kwerekana `2.4.2` canke iyirenga.

Ntiwizigire gusa ko itegeko ryo kwagura ryasozeye ata kosa: ku mashini zifise ububasha buke, ukumanura image gushobora gutsitara mu bwitonzi hanyuma bigasiga container ya kera iriko irakora. Soma version, igihe cose.

## Intambwe ya 4 — Hindura ivyemezo vyawe vyo kwinjira

Iyi ni yo ntambwe ihindura "kwakosowe" ikakugira "utekanye". Kubera ko ikinenge cariko gikoreshwa nabi imbere y'uko ugukosora gusohoka, ibanga ryose urubuga rwawe rwari rufise urifate nk'aho umugizi wa nabi ashobora kuba ariryizi.

### Lightning: LND

Subira ukore macaroons **na** dosiye `macaroons.db`. Gufuta amadosiye ya macaroon gusa ntibihagije — LND ikura macaroons ku rufunguzo shingiro rubitswe muri `macaroons.db`, ku buryo umugizi wa nabi afise kopi ya macaroon ya kera aguma yinjira gushika iyo database yongeye gukorwa.

Inzira ni iyi: hagarika LND, ukure `macaroons.db` n'amadosiye `*.macaroon` muri dosiye y'urubuga (ku mainnet, `data/chain/bitcoin/mainnet/` muri dosiye y'amakuru ya LND), hanyuma usubire utangure kandi ufungure LND, na yo izosubira kubikora. Banza ukore backup ya iyo dosiye, kandi usubire uhuze porogaramu zose zakoresha macaroons za kera — BTCPay Server ubwayo, Zeus, Thunderhub, RTL, Alby, na script iyo ari yo yose wanditse.

Nimba kandi wugururiye LND kuri internet, suzuma icemezo cayo ca TLS n'ivyemezo vyo kwinjira vyose vyo muri `lnd.conf` ico gihe nyene.

### Lightning: ubundi buryo

Ikintu cose cinjira kuri node yawe gikoresheje umurongo w'inyuguti gitegerezwa kuronka umurongo mushasha:

- **Core Lightning**: subira ukore rune canke ivyemezo vyo kwinjira bikoreshwa n'uko guhuza.
- **Phoenixd**: hindura ijambobanga rya HTTP.
- **LNbits n'ibisa na yo**: kuraho hanyuma usubire utange imfunguruzo za admin n'iza invoice.
- **Imirongo yo guhuza na node iri kure** ibitswe mu ntunganyo z'iduka muri BTCPay Server: yandike bushasha ukoresheje amabanga mashasha.

### Hot wallet yo ku murunga (on-chain) yakorewe muri BTCPay Server

Nimba waretse BTCPay Server igukorera agakofero ko ku murunga (on-chain) — aho guhuza hardware wallet canke kwinjiza xpub imfunguruzo zayo zitigeze zikora kuri server — iyo seed yabaye kuri iyo mashini.

Yifate nk'iyononekaye burundu:

1. Kora agakofero gashasha, nivyoshoboka ukoresheje hardware wallet kugira imfunguruzo ntizosubire kuguma kuri server.
2. Kubura amahera yose uyakuye mu gakofero ka kera uyashira muri ka gashasha.
3. Subiriza derivation scheme iri mu ntunganyo z'iduka ushiremwo iy'agakofero gashasha.
4. Ntuze usubire gukoresha seed ya kera.

Intunganyo za watch-only (xpub canke hardware wallet) ntizibikeneye: imfunguruzo z'ibanga ntizigeze ziba kuri server. Ni co gituma nyene inyigisho yo gushiramwo izihanura.

### Konti za BTCPay Server n'imfunguruzo za API

Mu gihe uri muri ivyo:

- Hindura amajambobanga ya konti zose z'abakoresha ziri kuri urwo rubuga.
- Kuraho hanyuma usubire utange **imfunguruzo za API** zose za Greenfield.
- Subira wiyandikishe mu kwemeza kabiri, kubera ko 2.4.2 ikosora uburyo bwo kurenga kuri 2FA.
- Fungura `Admin Dashboard > Server > Users` maze usuzume ko ata konti itategekanijwe iriho.
- Suzuma **payouts**, **pull payments** na **refunds** vya vuba kugira urabe ko ata vyanditswe utakoze biriho.
- Suzuma ama webhooks yawe n'amabanga yayo.

## Intambwe ya 5 — Guma umenyeshwa ku bwa rikurikira

Ugusohorwa kw'umutekano gufasha gusa abacungera bakumva ko kwabaye:

- Kurikirana [ugusohorwa kwa BTCPay Server kuri GitHub](https://github.com/btcpayserver/btcpayserver/releases) — GitHub irashobora kukwandikira imeri ku gusohorwa kwose kushasha kw'ububiko.
- Kurikira imiyoboro y'amatangazo y'uwo mugambi na [blog yemewe](https://blog.btcpayserver.org/).
- Gumiza urubuga rwawe kuri version ushobora kwagura ningoga: uko urushiriza gusigara inyuma, ni ko ukwagura kw'ihutirwa kurushiriza kugora.

Kwiyakirira ubwawe biguha ubusegaba ku vyo wishuzwa. Igiciro c'ubwo busegaba ni ico nyene: gusoma ivyanditswe ku gusohorwa no kuba uwo akosora.

