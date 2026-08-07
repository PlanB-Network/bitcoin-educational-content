---
name: BTCPay Server යාවත්කාලීන කිරීම
description: ඔබේ BTCPay Server instance එකට ආරක්ෂක යාවත්කාලීනයක් යොදා, වැදගත් අක්තපත්‍ර rotate කරන්න
---

![කවරය](assets/cover.webp)

ඔබේම payment processor එක ක්‍රියාත්මක කිරීම යනු ඔබම ඔබේ ආරක්ෂක කණ්ඩායමද වීමයි. BTCPay Server නඩත්තුකරුවන් ආරක්ෂක release එකක් ප්‍රකාශ කළ විට, ඔබ වෙනුවෙන් කිසිවෙකු ඔබේ instance එක patch කරන්නේ නැත: යාවත්කාලීනය, සත්‍යාපනය, සහ ඉන්පසු සිදුකෙරෙන අක්තපත්‍ර rotation ඔබ විසින්ම කළ යුතු දේවල් වේ.

ඔබ BTCPay Server deploy කර ඇති ආකාරය කුමක් වුවත්, මෙම නිබන්ධනය සම්පූර්ණ ක්‍රියාවලිය හරහා ඔබව ගෙන යයි: ක්‍රියාත්මක වන version එක පරීක්ෂා කිරීම, ඔබේ deployment වර්ගය මත යාවත්කාලීනය යෙදීම, එය ඇත්තටම සාර්ථකව යෙදී ඇති බව තහවුරු කිරීම, සහ ඔබේ instance එක අවදානමට ලක්ව තිබූ කාලයේ ප්‍රහාරකයෙකු ලබාගෙන තිබිය හැකි secrets rotate කිරීම.

ඔබ තවමත් BTCPay Server deploy කර නැත්නම්, installation guide එකෙන් ආරම්භ කරන්න:

https://planb.academy/tutorials/business/point-of-sale/btcpay-server-928eb01e-824b-4b57-a3e8-8727633beddc

## 2026 අගෝස්තු මාසයේ තීරණාත්මක දුර්වලතාව

⚠️ **තීරණාත්මක ආරක්ෂක අනතුරු ඇඟවීම (2026 අගෝස්තු 7):** BTCPay Server වෙත බලපාන තීරණාත්මක දුර්වලතාවක් සක්‍රීයව exploit කරමින් පවතින අතර, එය අරමුදල් අහිමි වීමට හේතු විය හැක. `Admin Dashboard > Server > Maintenance > Update` හරහා ඔබේ instance එක **version 2.4.2** වෙත වහාම යාවත්කාලීන කරන්න, ඉන්පසු footer එක `2.4.2` පෙන්වන බව පරීක්ෂා කරන්න. ඔබට වහාම යාවත්කාලීන කළ නොහැකි නම්, ඔබේ BTCPay Server වසා දමන්න. යාවත්කාලීන කිරීමෙන් පසු, ඔබේ macaroons සහ ඔබේ `macaroons.db` සම්පූර්ණයෙන්ම refresh කළ යුතුය, වෙනත් ඕනෑම Lightning backend එකක authentication strings සම්පූර්ණයෙන්ම refresh කළ යුතුය, සහ ඔබ BTCPay Server තුළ hot on-chain wallet එකක් ජනනය කර තිබේ නම්, එම අරමුදල් මාරු කර wallet එක නැවත නිර්මාණය කළ යුතුය. Integrators NBXplorer ද version 2.6.10 වෙත යාවත්කාලීන කළ යුතුය. මූලාශ්‍රය: [BTCPay Server 2.4.2 release notes](https://github.com/btcpayserver/btcpayserver/releases/tag/v2.4.2).

Version 2.4.2 2026 අගෝස්තු 7 වනදා ප්‍රකාශයට පත් කරන ලදී. Release notes පවසන්නේ Bitcoin Red Team උත්සාහය හරහා `brunoerg` සහ `benthecarman` විසින් වාර්තා කරන ලද, දැනටමත් සජීවී පරිසරයේ exploit කරමින් තිබූ තීරණාත්මක දුර්වලතාවක් එය සවි කරන බවයි. එම release එක TOTP two-factor authentication bypass එකක්ද Greenfield Basic authentication හරහා සවි කරන අතර, account creation කිරීමෙන් විනාඩි පහකට පසු Greenfield Basic authentication පෙරනිමියෙන් අක්‍රීය කරයි.

"actively exploited" යන්නෙන් ප්‍රතිඵල දෙකක් අනුගමනය වේ:

- **යාවත්කාලීන කිරීම විකල්පයක් නොවේ, එය ලබන සතියට කල් දාන්නට දෙයක්ද නොවේ.** අන්තර්ජාලයෙන් ළඟා විය හැකි unpatched instance එකක් යාවත්කාලීන කළ යුතුය, නැතහොත් වසා දැමිය යුතුය.
- **යාවත්කාලීන කිරීම පමණක් ප්‍රමාණවත් නොවේ.** ඔබ patch කිරීමට පෙර ඔබේ instance එක compromised වී තිබුණේ නම්, ප්‍රහාරකයා ඔබේ Lightning credentials වල පිටපත් සහ BTCPay Server ඔබ වෙනුවෙන් ජනනය කළ ඕනෑම hot wallet key material දැනටමත් අතේ තබාගෙන සිටිය හැක. ඔබ ඒවා rotate කරන තුරු එම secrets යාවත්කාලීනයෙන් පසුවත් වලංගු වේ. පහත rotation කොටස මිනිසුන් මඟහැර යන කොටස වන අතර, ඔබේ අරමුදල් සැබවින්ම ආරක්ෂා කරන්නේද එම කොටසයි.

## පියවර 1 — ඔබ ක්‍රියාත්මක කරන version එක සොයා ගන්න

ඔබේ BTCPay Server වෙත log in වී **ඕනෑම පිටුවක footer එක** බලන්න: version string එක එහි පෙන්වයි. වත්මන් version එක සහ update controls පෙන්වන `Admin Dashboard > Server > Maintenance` ද ඔබට විවෘත කළ හැක.

ඔබේ instance එක Greenfield API expose කරන්නේ නම්, `GET /api/v1/server/info` ද version එක ආපසු ලබා දෙයි.

`2.4.2` ට පහළ ඕනෑම එකක් vulnerable වේ.

## පියවර 2 — යාවත්කාලීන කරන්න

### Self-hosted Docker deployment (standard install එක)

මෙය නිල Docker deployment එක ආවරණය කරයි; එය BTCPay Server documentation එකෙන්, LunaNode one-click launcher එකෙන්, සහ බොහෝ VPS installs වලින් ඔබට ලැබෙන දේ වේ.

සරලම මාර්ගය web interface එකයි:

1. `Admin Dashboard > Server > Maintenance` වෙත යන්න.
2. **Update** ක්ලික් කරන්න.
3. containers pull කර restart වන තෙක් රැඳී සිටින්න. interface එක මිනිත්තු කිහිපයකට ලබාගත නොහැකි වනු ඇත.

web interface එකට ළඟා විය නොහැකි නම්, නැතහොත් logs දැකීමට ඔබ කැමති නම්, SSH හරහා එය කරන්න:

```bash
sudo su -
cd "$BTCPAY_BASE_DIRECTORY/btcpayserver-docker"
. ./btcpay-update.sh
```

Default install එකක `$BTCPAY_BASE_DIRECTORY` `/root` වන බැවින් directory එක `/root/btcpayserver-docker` වේ. Script එක නවතම images pull කරයි, containers නැවත නිර්මාණය කරයි, සහ ලැබුණු versions print කරයි.

Docker deployment එක BTCPay Server සමඟ NBXplorer ද ship කරයි, එබැවින් standard update එකක් NBXplorer ද නිර්දේශිත `2.6.10` වෙත ගෙන යයි. ඔබ NBXplorer වෙනම run කරන්නේ නම් — integrators සහ custom stacks සඳහා සාමාන්‍යයි — එය පැහැදිලිව යාවත්කාලීන කරන්න.

### Umbrel

Umbrel dashboard එක විවෘත කර, **App Store** වෙත ගොස්, BTCPay Server සොයා, update එකක් ඉදිරිපත් කර ඇත්නම් එය යොදන්න.

⚠️ **වැදගත්:** app-store packages Umbrel කණ්ඩායම විසින් නැවත package කරනු ලබන අතර upstream ට වඩා පැය ගණනක් හෝ දින ගණනක් පසු විය හැක. යාවත්කාලීන කිරීමෙන් පසු BTCPay Server footer එකේ version එක පරීක්ෂා කරන්න. එය තවමත් `2.4.2` ට පහළ නම්, vulnerable instance එකක් ක්‍රියාත්මකව තබා නොගෙන Umbrel dashboard එකෙන් **app එක නවත්වන්න** සහ packaged release එක සඳහා බලා සිටින්න.

කැපවූ Umbrel guide එක app එකම ආවරණය කරයි:

https://planb.academy/tutorials/business/point-of-sale/btcpay-server-umbrel-68e1c535-4322-4507-a69c-9dfcbc36dfd1

### Start9 / StartOS

එම logic එකමයි: StartOS marketplace එකෙන් BTCPay Server යාවත්කාලීන කර, පසුව footer එකේ version එක තහවුරු කරන්න. Packaged version එක තවමත් `2.4.2` නොවේ නම්, එය වන තුරු service එක නවත්වන්න.

### Managed and third-party hosting

ඔබේ instance එක වෙනත් කෙනෙකු ක්‍රියාත්මක කරන්නේ නම් (hosting provider කෙනෙකු, association එකක්, මිතුරෙකුගේ server එකක්), තවමත් ඔබට තහවුරු කිරීම අවශ්‍ය වේ. Footer එකේ පෙන්වන version string එක operator වෙතින් ඉල්ලන්න, සහ පහත විස්තර කර ඇති post-update credential rotation සිදු කර තිබේදැයි පැහැදිලිව අසන්න. "අපි යාවත්කාලීන කළා" යන්න "අපි ඔබේ macaroons rotate කළා" යන පිළිතුරට සමාන නොවේ.

## පියවර 3 — යාවත්කාලීනය ඇත්තටම යෙදී ඇති බව තහවුරු කරන්න

BTCPay Server interface එක reload කර footer එකේ version එක කියවන්න. එය `2.4.2` හෝ ඊට ඉහළ පෙන්විය යුතුය.

Update command එක error එකක් නොමැතිව exit වීම මත පමණක් විශ්වාස නොකරන්න: සීමිත machines වල image pull එකක් නිහඬව fail වී, පෙර container එක තවමත් running ලෙස තබා යා හැක. සෑම වතාවකම version එක කියවන්න.

## පියවර 4 — ඔබේ අක්තපත්‍ර rotate කරන්න

මෙම පියවර "patched" යන්න "safe" බවට පත් කරයි. Fix එක ship වීමට පෙර දුර්වලතාව exploit කරමින් තිබූ බැවින්, ඔබේ instance එක තබාගෙන සිටි සෑම secret එකක්ම ප්‍රහාරකයෙකු දැන සිටිය හැකි එකක් ලෙස සලකන්න.

### Lightning: LND

macaroons **සහ** `macaroons.db` file එක නැවත generate කරන්න. macaroon files පමණක් delete කිරීම ප්‍රමාණවත් නොවේ — LND, `macaroons.db` හි ගබඩා කර ඇති root key එකෙන් macaroons derive කරන බැවින්, පැරණි macaroon එකක copy එකක් අතේ තබාගෙන සිටින ප්‍රහාරකයෙකුට එම database එක නැවත නිර්මාණය කරන තුරු access තවදුරටත් පවතී.

ක්‍රියාවලිය මෙයයි: LND නවත්වන්න, network directory එකෙන් `macaroons.db` සහ `*.macaroon` files ඉවත් කරන්න (mainnet සඳහා, LND data directory එක තුළ `data/chain/bitcoin/mainnet/`), පසුව LND නැවත start කර unlock කරන්න; එවිට ඒවා නැවත නිර්මාණය වේ. පළමුව directory එක backup කරන්න, සහ පැරණි macaroons භාවිත කළ සෑම application එකක්ම නැවත pair කරන්න — BTCPay Server එකම, Zeus, Thunderhub, RTL, Alby, සහ ඔබ ලියා ඇති ඕනෑම script එකක්.

ඔබ LND ද අන්තර්ජාලය හරහා expose කරන්නේ නම්, එහි TLS certificate එක සහ ඕනෑම `lnd.conf` credentials එකම අවස්ථාවේ review කරන්න.

### Lightning: වෙනත් backends

String එකක් සමඟ ඔබේ node එකට authenticate කරන ඕනෑම දෙයකට නව string එකක් ලැබිය යුතුය:

- **Core Lightning**: connection එක භාවිත කරන rune හෝ access credentials නැවත generate කරන්න.
- **Phoenixd**: HTTP password එක rotate කරන්න.
- **LNbits and similar**: admin සහ invoice keys revoke කර නැවත issue කරන්න.
- **Remote node connection strings** BTCPay Server store settings තුළ ගබඩා කර ඇත්නම්: ඒවා නව secrets සමඟ rewrite කරන්න.

### BTCPay Server තුළ ජනනය කළ hot on-chain wallet

Hardware wallet එකක් connect කිරීම හෝ keys කිසි විටෙකත් server එකට නොපැමිණි xpub එකක් import කිරීම වෙනුවට, ඔබ වෙනුවෙන් on-chain wallet එකක් ජනනය කිරීමට BTCPay Server ට ඉඩ දුන්නේ නම් — එම seed එක machine එකේ තිබුණි.

එය compromise වූ එකක් ලෙස සලකන්න:

1. Keys නැවත server එකේ නොසිටින පරිදි, හැකි නම් hardware wallet එකක් සමඟ, නව wallet එකක් නිර්මාණය කරන්න.
2. පැරණි wallet එකෙන් නව එකට අරමුදල් sweep කරන්න.
3. Store settings තුළ derivation scheme එක නව wallet එකෙන් ප්‍රතිස්ථාපනය කරන්න.
4. පැරණි seed එක කිසිවිටෙකත් නැවත භාවිත නොකරන්න.

Watch-only setups (xpub හෝ hardware wallet) සඳහා මෙය අවශ්‍ය නොවේ: private keys කිසි විටෙකත් server එකේ නොතිබුණි. Installation guide එක ඒවා නිර්දේශ කරන්නේ නිවැරදිව මේ නිසාය.

### BTCPay Server accounts සහ API keys

එසේ කරන අතරතුර:

- Instance එකේ සෑම user account එකකම passwords වෙනස් කරන්න.
- සියලු Greenfield **API keys** revoke කර නැවත issue කරන්න.
- 2.4.2 2FA bypass එකක් සවි කරන බැවින්, two-factor authentication නැවත enroll කරන්න.
- `Admin Dashboard > Server > Users` විවෘත කර අනපේක්ෂිත account එකක් නොමැති බව පරීක්ෂා කරන්න.
- ඔබ නිර්මාණය නොකළ entries සඳහා මෑත **payouts**, **pull payments** සහ **refunds** review කරන්න.
- ඔබේ webhooks සහ ඒවායේ secrets review කරන්න.

## පියවර 5 — ඊළඟ එක සඳහා දැනුවත්ව සිටින්න

Security releases ඒවා ගැන අසන operators ලාට පමණක් උපකාරී වේ:

- [BTCPay Server releases on GitHub](https://github.com/btcpayserver/btcpayserver/releases) watch කරන්න — repository එකක සෑම නව release එකක් ගැනම GitHub ඔබට email කළ හැක.
- Project එකේ announcement channels සහ [official blog](https://blog.btcpayserver.org/) follow කරන්න.
- ඔබේ instance එක ඉක්මනින් යාවත්කාලීන කළ හැකි version එකක තබා ගන්න: ඔබ වැඩි දුරට පසුපස සිටින තරමට, emergency update එකක් වැඩි වේදනාකාරී වේ.

Self-hosting ඔබේ payments පිළිබඳ sovereignty ඔබට ලබා දෙයි. එම sovereignty එකේ වියදම හරියටම මෙයයි: release notes කියවීම සහ patch කරන පුද්ගලයා ඔබම වීම.
