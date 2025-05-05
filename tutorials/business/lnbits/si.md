---
name: LNbits

description: වෙළඳ ගිණුම්කරණ වේදිකාව
---

![presentation](assets/lnbits-intro.webp)

# ගිණුම් පද්ධතිය


LNbits ඔබේ ආදායම් සහ වියදම් අරමුදල් පාලනය කිරීම සහ නාලිකාගත කිරීම, ඔබේ වෙබ් අඩවිය හෝ ඔබම ගොඩනැගූ Hardware Wallet හෝ ATM වැනි උපාංග සම්බන්ධ කිරීම සඳහා මෙවලම් බොහොමයක් සමඟ සම්පූර්ණ වේ. පරිශීලක වර්ගයන් ඇතුළත් වේ:


- Wallet හිමියන් තම මුදල් කළමනාකරණය සඳහා මෙන්ම එහි අමතර විශේෂාංග සඳහා LNbits Interface ලෙස භාවිතා කිරීමට අවශ්‍යයි.
- Bitcoin ඔන්චේන් සහ Lightning Network ගෙවීම් පිළිගැනීමට කැමති මාර්ගගත සහ මාර්ගයෙන් බැහැර වෙළඳුන් හෝ සේවා සපයන්නන්.
- Lightning Network යෙදුම් නිර්මාණය කිරීමට කැමති සංවර්ධකයින්.
- නෝඩ් ක්‍රියාකාරකයන්, තම නෝඩ් එක ගිණුම්කරණ අරමුණු සඳහා LNbits පද්ධතිය සමඟ ඒකාබද්ධ කිරීමට අවශ්‍යයි.
- එම සියල්ලටම විවිධ අවශ්‍යතා ඇත. අපි LNbits මොඩියුලාර ලෙස ගොඩනඟන අතර, එය සෑම පරිශීලකයෙකුටම අපගේ විශේෂාංග ඔබට වඩාත් සුදුසු ආකාරයෙන් භාවිතා කළ හැකි වේ.


# Wallet මෙනේජර්


LNbits යනු නොමිලේ සහ විවෘත මූලාශ්‍ර ගිණුම්කරණ පද්ධතියක් වන අතර, නෝඩ් කළමනාකරු නොවේ. නාලිකා කළමනාකරණය යනු LND හෝ c-lightning වැනි මූල්‍ය මූලාශ්‍රයක් ලෙස LNbits සමඟ සම්බන්ධ වූ Lightning නෝඩ් එකක ව්‍යාපාරයයි. LNbits පද්ධතියේ අධිපරිශීලකයා හෝ පරිපාලක පරිශීලකයින් ගිණුම්කරණ විශේෂාංග සහ අභ්‍යන්තර දිගුවන්ගේ සමස්ත ප්‍රවේශය සහ වින්‍යාසය කළමනාකරණය කිරීම සඳහා වගකිව යුතුය.


LNbits පරිශීලකයා සහ Lightning node අතර Interface ලෙස ක්‍රියා කරමින් ගෙවීම් ජාලය කළමනාකරණය කිරීමට සහ අන්තර්ක්‍රියා කිරීමට සරල, පරිශීලක හිතකාමී ක්‍රමයක් සපයයි.


LNbits ගැන සිතන්න ඔබේ node සඳහා “wordpress මොඩියුලර් රාමුවක්” ලෙස. ඔබට විවිධ භාවිතා කේස් සඳහා එකතු කළ හැකි දිගුවල මත පදනම් වූ, කළමනාකරණය කිරීමට පහසු වේදිකාවක්.


LNbits ගැන සිතන්න ඔබේම බැංකු මූල්‍ය කළමනාකරණ මෘදුකාංගයක් ලෙස. ඔබේ නියුඩ් එක හරහා ගෙවීම් කිරීමට නාලිකා ලබා දෙන අතර LNbits ඔබේ නියුඩ් එක Wallet වඩා වැඩි විදුලි ආලෝකන නියුඩ් එකක් ලෙස ක්‍රියාත්මක කිරීමට පුළුවන් වේ. මෙම පසුම්බි අනිවාර්යයෙන්ම ඔබට අයත් විය යුතු නැත. ඔබ, LN නියුඩ් ධාවකයා ලෙස, දැනටමත් ප්‍රමාණවත් නාලිකා ද්‍රවශීලතාව සහ අරමුදල් ඇති අතර දැන් ඔබේ මිතුරන්, පවුල, තමන්ගේ වෙළඳසැල හෝ වෙනත් සාමාන්‍ය වෙළෙන්දන් සඳහා Bitcoin බැංකු සේවා ලබා දීමට අවශ්‍ය නම්, එය සිදු කළ හැක.


ඔබේ නෝඩ් එකේ වෙනත් වොලට් වලට ප්‍රවේශය නොමැතිව, ඔවුන්ට "බැංකු ගිණුමක්" විවෘත කිරීමට සරල ක්‍රමයක් ඔබ ලබා දෙනු ඇත. නමුත් ඔවුන්ගේ කොටසට පමණක්. ඔබේ නෝඩ් එක (බැංකුව) ඔවුන්ගේ ගෙවීම් (ආ/පි) සඳහා ප්‍රවාහන සපයන්නා ලෙස පමණක් ක්‍රියා කරයි.


OPOMBA: vsa sredstva, ki jih vaši "stranke" položijo na svoje LNbits bančne račune na vašem vozlišču, bodo šla neposredno v kanale vašega vozlišča LN. To pomeni, da ste VI dejanski lastnik teh sredstev. Imeli boste veliko odgovornost za njihova sredstva. Ne bodite zlobni in ne pobegnite s sredstvi, ne bodite zlobni in ne zaračunavajte visokih provizij. Želimo uničiti fiat bankirje, ne pa uničiti drug drugega (uporabniki Bitcoin).


# ඩෙමෝ වේදිකාව


ඩෙමෝව [https://legend.lnbits.com](https://legend.lnbits.com) හි සොයා ගත හැක. එය සම්පූර්ණ ක්‍රියාකාරී වන අතර Lightning Network සහ LNbits සහ LNURL හි විශේෂාංග ගැන ඉගෙන ගැනීමට භාවිතා කළ හැක. ඔබව එය භාවිතා කිරීමෙන් වළක්වා ගැනීමට අපට නොහැකි වුවද, ඔබේ නිෂ්පාදන සැකසීම සඳහා එය භාවිතා නොකරන ලෙස අපි ඔබගෙන් ඉල්ලා සිටිමු. අපි නව විශේෂාංග පරීක්ෂා කිරීමට සර්වරයන් මත නිතරම වැඩ කරන්නේ පමණක් නොව, ඔබේම නෝඩයක් සහ LNbits ස්වෛරී ලෙස ක්‍රියාත්මක කිරීමට ඔබව උත්සාහ දක්වන්නට අපි කැමතියි. නෝඩයක් ක්‍රියාත්මක කිරීම මේ මොහොතේ ඉතාමත් ඉල්ලීමක් යැයි ඔබ සිතන්නේ නම්, Opennode, Luna හෝ Votage වැනි වාණිජ මූල්‍ය සේවාවකට හෝ Telegram හි Lightning Tipbot වෙත LNbits සම්බන්ධ කළ හැක, කිහිපයක් නම් කිරීමට.


# LNbits ප්‍රචාරක පත්‍රය


ඔබේ වෙළෙන්දෙකුට හෝ ගොඩනැගිලි මිතුරෙකුට මූලික තොරතුරු කිහිපයක් භාරදීමට අවශ්‍යද? සෑම කෙනෙකුටම භාවිතා කිරීමට අපගේ පළමු පත්‍රිකාව ප්‍රකාශයට පත් කිරීමට අපි ඉතා සතුටු වෙමු. ප්‍රමාණය ගෝලීයව සාමාන්‍ය පත්‍රිකා ආකාරයකි, පිටු 6ක් (මැදහත් 2ක්) සහ පළල 3508 සහ උස 2480px.


LNbits සඳහා වෙළඳුන්: [EN](/assets/lnbits-merchants-en.pdf) | [DE](/assets/lnbits-merchants-de.pdf) | [ES](/assets/lnbits-merchants-es.pdf) | [IT](/assets/lnbits-merchants-it.pdf) | [PL](/assets/lnbits-merchants-pl.pdf)


LNbits for builders: [EN](/assets/lnbits-builders-en.pdf) | [DE](/assets/lnbits-builders-de.pdf) | [ES](/assets/lnbits-builders-es.pdf) | [IT](/assets/lnbits-builders-it.pdf) | [PL](/assets/lnbits-builders-pl.pdf)


# සමහර මූලික කරුණු


LNbits, LNURL ප්‍රොටෝකෝලය මත පදනම්ව ක්‍රියා කරයි, එය අර්ථ දක්වන්නේ ඉල්ලීම් වලංගු වන්නේ ආකාර දෙකකින්: https:// clearnet සබැඳියක් ලෙස (ස්වයං-අත්සන් කළ සහතික වලට ඉඩ නොදේ) හෝ http:// v2/v3 onion සබැඳියක් ලෙස. LNURLp/w QR කේත හෝ NFC කාඩ්පත් වැනි LNbits සේවා වනවල්වල භාවිතා කළ හැකි ලෙස ලබා දීමට, ඔබට LNbits clearnet (https) වෙත විවෘත කළ යුතු වේ.


LNbits ස්ථාපනය කිරීමට පෙර LNbits යනු කුමක්ද සහ එය ඔබට විවෘත කරන හැකියාවන් කුමක්ද යන්න පිළිබඳ සාමාන්‍ය මාර්ගෝපදේශ පහත දැක්කොට ඇති බවට සහ ඒවා අවබෝධ කරගෙන ඇති බවට වග බලා ගන්න.



- [LND මාර්ගෝපදේශය](https://docs.lightning.engineering/) | LND ස්ථාපනය කිරීම
- [LND Config Example](https://github.com/lightningnetwork/LND/blob/master/sample-LND.conf) | LND සැකසුම්
- [CLN Guide](https://docs.corelightning.org/docs/installation) | CLN ස්ථාපනය කිරීම
- [LUDs](https://github.com/lnurl/luds) LNURL Spec | [NIPs](https://github.com/nostr-protocol/nips) Nostr Spec
- [Zaženi Watchtower](https://docs.lightning.engineering/lightning-network-tools/LND/Watchtower) | Zelo pomembno!


LNbits භාවිතා කරමින් විශේෂිත භාවිතා කේස් තත්ත්වයන් සඳහා වඩා විස්තරාත්මක මාර්ගෝපදේශ මෙතැන:



- [LNbits සමඟ ආරම්භ කිරීම](https://darthcoin.substack.com/p/getting-started-lnbits) | Substack මාර්ගෝපදේශය
- [ඔබේ ආරක්ෂාව සඳහා LNbits සමඟ ToDos](https://youtu.be/i5FQf96e6zg) | Youtube වීඩියෝ
- [පෞද්ගලික බැංකු Lightning Network](https://darthcoin.substack.com/p/Bitcoin-private-banks-over-lightning) | Substack මාර්ගෝපදේශය
- [ඔබේ මිතුරන් සහ පවුලේ අය සඳහා භාරකාර පසුම්බි ක්‍රියාත්මක කරන්න](https://darthcoin.substack.com/p/the-bank-of-lnbits) | Substack මාර්ගෝපදේශය
- [LNbits for a small restaurant / hotel](https://darthcoin.substack.com/p/lnbits-for-small-merchants) | Substack guide
- [LNbits Streamer copilot භාවිතා කිරීම](https://darthcoin.substack.com/p/lnbits-streamer-copilot) | Substack මාර්ගෝපදේශය
- [ඔබේ NOSTR වෙළඳපොළ LNbits සමඟ ආරම්භ කරන්න](https://darthcoin.substack.com/p/lnbits-nostr-market) | Substack මාර්ගෝපදේශය
- [LNbits භාවිතා කිරීම පාසල් ව්‍යාපෘති හෝ උත්සව අවස්ථා සඳහා](https://darthcoin.substack.com/p/lnbits-saas-a-solution-for-schools) Substack මාර්ගෝපදේශය



# LNbits ස්ථාපනය කරන්න


## මූලික ස්ථාපන මාර්ගෝපදේශය


LNbits ඕනෑම Linux OS යන්ත්‍රයක ස්ථාපනය කළ හැක. එය ශක්තිමත් යන්ත්‍රයක් හෝ සේවාදායකයක් අවශ්‍ය නොවේ, මතක RAM ප්‍රමාණයක් සහ දත්ත සමුදාය සඳහා ඩිස්ක් අවකාශයක් පමණක් ප්‍රමාණවත් වේ. එය BTC/LN නියුඩ් (දේශීය පරිගණකය හෝ දුරස්ථ VPS) වලින් වෙනම ක්‍රියාත්මක කළ හැකි අතර, නියුඩ් සමඟ එකම යන්ත්‍රයේ හෝ දැනටම ස්ථාපිත බන්ඩල් නියුඩ් මෘදුකාංග යන්ත්‍රයක ක්‍රියාත්මක කළ හැක.


Izberete lahko med najpogostejšimi upravitelji paketov, kot sta poetry in nix. Privzeto bo LNbits uporabljal SQLite kot svojo bazo podatkov. Uporabite lahko tudi PostgreSQL, ki je priporočljiv za aplikacije z visoko obremenitvijo. [Tukaj je vodnik za osnovno namestitev z uporabo poetry ali nix](https://github.com/lnbits/lnbits/blob/main/docs/guide/installation.md).


Za vse, ki ste novi pri tem, boste našli podrobnejša navodila po korakih za zagon vašega LNbits v specifičnih okoljih:


- [LNbits on clearnet](https://ereignishorizont.xyz/lnbits-server/en/) by Axel
- [LNbits on a VPS](https://github.com/TrezorHannes/vps-lnbits) by Hannes
- [LNbits on cloudflare](https://www.nodeacademy.org/lnbits) විසින් ලියෝ


ඔබට [PostgreSQ, LightningTipBot මඟින් මුල්‍ය මූලාශ්‍රයක් ලෙස nginx භාවිතා කරමින් VPS මත dockerised සැකසීම පිළිබඳ වීඩියෝවක්](https://www.massmux.com/howto-complete-lightningtipbot-lnbits-setup-vps/) ද සොයා ගත හැක.


[තවත් ස්ථාපන තත්‍යාවස්ථා මෙතැන](https://darthcoin.substack.com/p/build-your-own-lnbits-app-server).


බණ්ඩල් මෘදුකාංග නෝඩ් සඳහා, කරුණාකර LNbits පිළිබඳව ඔවුන්ගේ විශේෂිත ලේඛනවලට යොමු වන්න: [Citadel](https://runcitadel.space) | [Umbrel](https://umbrel.com) | [MyNode](https://mynodebtc.com) | [RaspiBlitz](https://raspiblitz.org/) | [RaspiBolt](https://raspibolt.org)


## LNbits SaaS


When you´re not into the technical stuff and neither want to host your funding source nor your lnbits yourself there is a [LNbits SaaS version](https://saas.lnbits.com) (Software-as-a-service) you can use. It is basically like LNbits in a cloud but you can define the funding source (e.g. your Node, a LNbits Wallet, the LNtipbot, fakewallet etc) and environmnent variables yourself - which mostly is not the case on other cloud-solutions.


[මෙන්න විශේෂිත භාවිතා කේස් සඳහා LNbits SaaS භාවිතා කරන ආකාරය පිළිබඳ විස්තරාත්මක මාර්ගෝපදේශයක්](https://darthcoin.substack.com/p/lnbits-saas-a-solution-for-schools).


## මූල්‍ය ආධාර මූලාශ්‍ර


LNbits යනු node කළමනාකරණ මෘදුකාංගයක් නොවන අතර LND හෝ CLN මූල්‍ය මූලාශ්‍රයක් මත LN මූලික ගිණුම් පද්ධතියකි. පළමු ස්ථාපනයෙන් පසු ඔබට http://localhost:5000/ හිදී ඔබේ LNbits වෙත පිවිසිය හැක.


Če želite spremeniti vir financiranja, pojdite na svoj super-user-URL in izberite vir financiranja znotraj "Manage Server" ali uredite datoteko .env tako, da spremenite `LNBITS_BACKEND_WALLET_CLASS` na želeni vir, če ste nastavili `adminUI=TRUE` v `.env`.


ඔබේ lnbits/ හෝ lnbits/apps/data ෆෝල්ඩරය තුළ .env ගොනුව සොයා ගත හැකි අතර, ඔබේ ඩිරෙක්ටරිය තුළ ගොනු ලැයිස්තුගත කිරීමට විධානය `ls -a` දක්වා දිගු කිරීමෙන්.


ඔබට අමතර පැකේජ ස්ථාපනය කිරීමට හෝ අමතර පිහිටුම් පියවරයන් සිදු කිරීමටද අවශ්‍ය විය හැක, අවශ්‍ය මූල්‍ය මූලාශ්‍රය තෝරා ගැනීම. නැවත ආරම්භ කිරීමෙන් පසු ඔබේ නව පිහිටුම ක්‍රියාත්මක වනු ඇත.


LNbits සඳහා මම භාවිතා කළ හැකි අරමුදල් මූලාශ්‍ර මොනවාද?


LNbits lahko deluje na številnih virih financiranja lightning omrežja. Trenutno je podpora za CoreLightning, LND, LNbits, LNPay, OpenNode, z rednimi dodatki novih.

ආරම්භයක් තෝරා ගැනීමේදී හොඳ දියරතාවයක් සහ හොඳ සමානවරුන් සම්බන්ධිත ආරම්භයක් තෝරා ගැනීම වැදගත් වේ. ඔබේ පරිශීලකයන්ගේ ගෙවීම් සතුටින් දෙපසටම ගලා යා හැකි වන්නේ ඔබ පොදු සේවා සඳහා LNbits භාවිතා කරන විට පමණි.


`.env` ගොනුවේ හෝ ඔබේ අධිපරිශීලක ගිණුමේ පරිපාලන-සේවාදායක කොටස යටතේ පහත LNbits පරිසර විචල්‍ය භාවිතයෙන් පසුබැසී Wallet (මුල්‍ය මූලාශ්‍රය) වින්‍යාස කළ හැකිය.

Če želite uporabiti različico .env, lahko parametre najdete tukaj:



### CoreLightning


- CLN
  - `LNBITS_BACKEND_WALLET_CLASS`: **CoreLightningWallet**
  - `CORELIGHTNING_RPC`: /file/path/lightning-RPC
- Spark (c-lightning)
  - `LNBITS_BACKEND_WALLET_CLASS`: **SparkWallet**
  - `SPARK_URL`: http://10.147.17.230:9737/RPC
   - `SPARK_TOKEN`: secret_access_key

### Lightning Network Daemon


- LND (REST)
  - `LNBITS_BACKEND_WALLET_CLASS`: **LndRestWallet**
  - `LND_REST_ENDPOINT`: http://10.147.17.230:8080/
  - `LND_REST_CERT`: /file/path/tls.cert
  - `LND_REST_MACAROON`: /file/path/admin.macaroon or Bech64/Hex
  - `LND_REST_MACAROON_ENCRYPTED`: eNcRyPtEdMaCaRoOn
- LND (gRPC)
  - `LNBITS_BACKEND_WALLET_CLASS`: **LndWallet**
  - `LND_GRPC_ENDPOINT`: ip_address
  - `LND_GRPC_PORT`: පෝට්
  - `LND_GRPC_CERT`: /file/path/tls.cert
  - `LND_GRPC_MACAROON`: /file/path/admin.macaroon or Bech64/Hex

AES-එන්ක්‍රිප්ට් කළ මැකරූන් (වැඩි විස්තර) වෙනුවට භාවිතා කළ හැක


  - `LND_GRPC_MACAROON_ENCRYPTED`: eNcRyPtEdMaCaRoOn

ඔබේ මැකරූන් කේතනය කිරීමට, `./venv/bin/python lnbits/wallets/macaroon/macaroon.py` ක්‍රියාත්මක කරන්න.


### LNbits (še en primerek LNbits)



- LNbits ආදානය මেঘ සේවාදායකයක හෝ ඔබේම ගෘහ සේවාදායකයක සත්කාරකය.
  - `LNBITS_BACKEND_WALLET_CLASS`: **LNbitsWallet**
  - `LNBITS_ENDPOINT`: https://lnbits.mydomain.com
  - `LNBITS_KEY`: my-lnbits-AdminKey
- LNbits Legend ඩෙමෝ සේවාදායකය (!! නිෂ්පාදන / වාණිජ අරමුණු සඳහා මෙය භාවිතා නොකරන්න, පරීක්ෂා කිරීම සඳහා පමණක් !!)
  - `LNBITS_BACKEND_WALLET_CLASS`: **LNbitsWallet**
  - `LNBITS_ENDPOINT`: https://legend.lnbits.com
  - `LNBITS_KEY`: legend-lnbits-AdminKey

### Lightning TipBot


Telegram-დან ඔබේ [Lightning Tipbot](https://t.me/LightningTipBot) დასაკავშირებლად, თქვენ უნდა დააყენოთ შემდეგი პარამეტრი:


  - `LNBITS_BACKEND_WALLET_CLASS`: **LnTipsWallet**
  - `LNBITS_ENDPOINT`: https://LN.tips
  - `LNBITS_KEY`: ඔබට යතුර ලබා ගැනීමට Telegram හි LightningTipbot සමඟ පුද්ගලික කතාබස්වල /api ක්‍රියාත්මක කළ යුතුය.


මෙම උපකාරකයද බලන්න [LNbits with LightningTipBot via vps](https://www.massmux.com/howto-complete-lightningtipbot-lnbits-setup-vps/) ස්ථාපනය කරන ආකාරය.


### IBEX HUB


[यहाँ](https://ibexpay.ibexmercado.com/onboard) रजिस्टर करें फिर वहां से अपनी कुंजियाँ/टोकन प्राप्त करें, एन्डपॉइंट है https://ibexpay-api.ibexmercado.com।

වැඩි විස්තර සඳහා [IBEX API-ප්‍රලේඛනය](https://ibexpay-api.readme.io/reference/getting-started-with-your-api) බලන්න.


### LNPay

Invoice listener ක්‍රියාත්මක වීමට ඔබට ඔබේ LNbits හි මහජන ප්‍රවේශය ඇති URL එකක් තිබිය යුතු අතර `<your LNbits host>/Wallet/webhook` වෙත සූචිත් කරන [LNPay webhook](https://dashboard.lnpay.co/webhook/) එකක් "Wallet Receive" සිදුවීම සමඟ සහ කිසිදු රහසක් නොමැතිව පිහිටුවිය යුතුය. `https://mylnbits/Wallet/webhook` සැකසීම යනු ගෙවීම් පිළිබඳව දැනුම් දෙන අවසාන ලක්ෂ්‍ය url එක වේ.


  - `LNBITS_BACKEND_WALLET_CLASS`: **LNPayWallet**
  - `LNPAY_API_ENDPOINT`: https://api.lnpay.co/v1/
  - `LNPAY_API_KEY`: sak_apiKey
  - `LNPAY_WALLET_KEY`: waka_apiKey


### OpenNode

Invoice ක්‍රියාත්මක වීමට, ඔබේ LNbits හි මහජන ප්‍රවේශය ඇති URL එකක් තිබිය යුතුය. වෙබ් හුක් සැකසීම විකල්පයකි.


  - `LNBITS_BACKEND_WALLET_CLASS`: **OpenNodeWallet**
  - `OPENNODE_API_ENDPOINT`: https://api.opennode.com/
  - `OPENNODE_KEY`: opennodeAdminApiKey


### ඇල්බි


ඇල්බි යනු LN Wallet ක්‍රියාකාරිතාවන් සහ LNDHUB ගිණුමක් සහිත බ්‍රවුසර විශේෂාංගයක් වන අතර එය LNbits සඳහා මූල්‍ය ආධාර මූලාශ්‍රයක් ලෙස භාවිතා කළ හැක. [වැඩි විස්තර මෙතන](https://getalby.com/).


Za delovanje Invoice morate imeti javno dostopen URL v vašem LNbits. Ročna nastavitev webhook ni potrebna. Tukaj lahko generate Alby dostopni žeton: https://getalby.com/developer/access_tokens/new



- `LNBITS_BACKEND_WALLET_CLASS`: AlbyWallet
- `ALBY_API_ENDPOINT`: https://api.getalby.com/
- `ALBY_ACCESS_TOKEN`: AlbyAccessToken


## අමතර / ගැටලු විසඳුම් මාර්ගෝපදේශ


මෙහි ඔබට අවශ්‍ය විය හැකි අමතර උපදෙස් කිහිපයක් ඇත. විස්තරය විහිදුවීමට ඊතලය මත ක්ලික් කරන්න.


### The Killswitch 🚨


මෑතකදී සම්පූර්ණ අවකාශය තුළ පමණක් නොව LNbits තුළද අනතුරුදායක දෝෂ බහුලව පවතින බැවින් අපි එය පිළිබඳව කිසියම් ක්‍රියාවක් ගන්නට තීරණය කළෙමු. දැන් ඔබට අනතුරු ඇඟවීම් සඳහා සහ/හෝ මුදල් අහිමිවීමකට හේතු විය හැකි අවලංගුතාවයක් හෝ දෝෂයක් නැවත සිදුවූ විට සෘජු ක්‍රියාවක් ගැනීමට තෝරා ගත හැක.


![killswitchn](assets/lnbits-killswitch.webp)


Če preklopite na void-Wallet, bodo vsi uporabniški tipi na instanci videli rumeni pas, kjer bi običajno našli obvestilo "LNbits je v Beta" poleg območja teme/jezika zgoraj desno - in je najbolj očiten namig, da se je nekaj zgodilo. Oglejte si svoj novi zavihek strežnika, označen v Green v levem delu okna.


Kako deluje? Ko je killswitch omogočen, se bo v določenem intervalu X minut (ki ga je mogoče določiti) preverjal skrivni github repozitorij, ki je na voljo samo osnovni ekipi LNbits. Če je v tem repozitoriju objavljena ranljiva napaka, to služi kot signal, ki sproži killswitch na vseh namestitvah, ki so se naročile, in preklopi vašo LNbits instanco na uporabo void Wallet. Če so se oblaki razjasnili in ste namestili varnostno posodobitev, lahko svoj vir financiranja nastavite nazaj na svoj node, Wallet ali karkoli že uporabljate, tudi prek razdelka Upravljanje strežnika. Ta wiki ima razdelek o preklapljanju virov financiranja, če ne veste, kaj konfigurirati.



### පරිපාලක සහ අධිපරිශීලක අතර වෙනසක්


LNbits පරිපාලක UI ඔබට LNbits ඉදිරිපස හරහා LNbits සැකසුම් වෙනස් කිරීමට ඉඩ සලසයි. එය පෙරනිමි ලෙස අක්‍රිය කර ඇත සහ ඔබ පළමු වරට `.env` ගොනුවේ `LNBITS_ADMIN_UI=true` පරිසර විචල්‍යය සකසන විට, සැකසුම් ආරම්භ කරනු ලැබේ සහ භාවිතා කෙරේ. එතැන් පටන් .env ගොනුවේ ඒවා වෙනුවට දත්ත සමුදායෙන් අදාළ සැකසුම් භාවිතා කෙරේ.


### සුපර් පරිශීලක


Admin UI සමඟ අපි සේවාදායකයට ප්‍රවේශ විය හැකි සුපිරි පරිශීලකයා හඳුන්වා දුන්නෙමු, එමඟින් මුල්ම පරිශීලකයාට ඉදිරිපස සහ API හරහා සේවාදායකය ක්‍රැෂ් විය හැකි හෝ ප්‍රතිචාර නොදක්වන ලෙස සැකසීම් වෙනස් කළ හැක, උදා. මූල්‍ය මූලාශ්‍රය වෙනස් කිරීම. සුපිරි පරිශීලකයා දත්ත සමුදායේ සැකසීම් වගුව තුළ පමණක් ගබඩා වේ. "පෙරනිමි ලෙස නැවත සකසන්න" සහ නැවත ආරම්භ කිරීමෙන් පසු නව සුපිරි පරිශීලකයෙකු නිර්මාණය වේ. අපි API මාර්ග සඳහා සුපිරි පරිශීලකයෙකු සිටින බව පරීක්ෂා කිරීම සඳහා අලංකාරකයෙකුද එකතු කළෙමු. එහි හැඳුනුම්පත API සහ ඉදිරිපස හරහා කිසිවිටෙක යවන නොමැති අතර ඔබ සුපිරි පරිශීලකයෙකුද නැද්ද යන්න bool (ඔව්/නැත) පමණක් ලැබේ.


"Top Up" अनुभाग मार्फत विभिन्न वालेटहरूमा सतोशीहरू बrrrr गर्न मात्र सुपर प्रयोगकर्तालाई अनुमति छ।


ඔබට එසේම සූපර් පරිශීලකයා තැනූ විට එය වෙනත් සේවාවකට webhook හරහා පළ කළ හැක. වැඩි විස්තර සඳහා මෙහි බලන්න https://github.com/lnbits/lnbits/blob/main/lnbits/settings.py `class SaaSSettings`


ඉදිරිපස අන්තර්ගතයේදී "Wallet නිර්මාණය කරන්න" පිටුවේ පෙන්වනු ලබන වෙළඳසැල් රූපය වෙනස් කිරීමේ හැකියාව ද ඔබට සොයා ගත හැකිය. එය කළ හැක්කේ සේවාදායක කළමනාකරණ කොටස විවෘත කර Theme -> Custom Logo තේරීමෙන් වේ.


### පරිපාලක පරිශීලකයින්


Enviroment variable: `LNBITS_ADMIN_USERS`, comma-seperated list of user IDs. Admin Users can change settings in the admin ui - with the exception of funding source settings, because this would require a server restart and could potentially make the server inaccessable. Also they have access to all the extensions dedicaated to them in `LNBITS_ADMIN_EXTENSIONS`.


### අනුමත පරිශීලකයින්


පරිසර විචල්‍යය: `LNBITS_ALLOWED_USERS`, පරිශීලක හැඳුනුම් අංක වල කොමා-වෙන් කළ ලැයිස්තුවක්. මෙම පරිශීලකයන් නිර්වචනය කිරීමෙන් පසු LNbits මහජනතාවට භාවිතා කළ නොහැක. එවිට නිර්වචිත පරිශීලකයන් සහ පරිපාලකයන්ට පමණක් LNbits ඉදිරිපසට ප්‍රවේශ විය හැක.




#### LNbits යාවත්කාලීන කරන්න

LNbits ස්ථානීය උදාහරණය සාමාන්‍ය ලෙස යාවත්කාලීන කිරීම සරලව පහත CLI විධාන පිටපත් කර අලවීමෙන් සිදු වේ:


```
cd lnbits
## Stop LNbits with `ctrl + x`
git pull
## Keep your poetry install up to date, this can be done with
poetry self update
poetry install --only main
## or
git checkout main && git pull && poetry install
## Start LNbits with
poetry run lnbits
```


Če uporabljate Raspiblitz ali MyNode, boste morda dodatno potrebovali

```
sudo systemctl restart lnbits
```

අවසානයේදී, එය සේවාවක් ලෙස LNbits ක්‍රියාත්මක කරන බැවිනි.


Umbrel/Citadel මත විධාන වන්නේ

```
cd ~/apps/lnbits
git pull upstream main
sudo ~/scripts/app start lnbits
```


#### SQLite to PostgreSQL migration


ඔබට දැනටමත් SQLite දත්ත සමුදායක ස්ථාපනය කර LNbits ක්‍රියාත්මක කර ඇති නම්, LNbits විශාල පරිමාණයකින් ක්‍රියාත්මක කිරීමට සැලසුම් කරන්නේ නම් postgres වෙත මාරු වීමට අපි ඉතාමත්ම නිර්දේශ කරමු.


ස්ක්‍රිප්ටුවක් ඇතුළත් වේ, එය මයිග්‍රේෂන් පහසුවෙන් කළ හැක. ඔබට Postgres දැනටමත් ස්ථාපනය කර තිබිය යුතු අතර පරිශීලකයා සඳහා මුරපදයක් තිබිය යුතුය (ඉහත Postgres ස්ථාපන මාර්ගෝපදේශය බලන්න). අමතරව, මයිග්‍රේෂන් ක්‍රියාත්මක වීමට පෙර ඔබේ LNbits ආකෘතිය Postgres මත වරක් ක්‍රියාත්මක විය යුතු අතර දත්ත ගබඩාව Schema ක්‍රියාත්මක කළ යුතුය:


```
# STOP LNbits

# add the database connection string to .env 'nano .env' LNBITS_DATABASE_URL=
# postgres://<user>:<password>@<host>/<database> - alter line bellow with your user, password and db name
LNBITS_DATABASE_URL="postgres://postgres:postgres@localhost/lnbits"
# save and exit

# START LNbits
# STOP LNbits
poetry run python tools/conv.py
# or
make migration
```

ආශාවෙන් දැන් හැමදේම ක්‍රියාත්මක වේ සහ මාරු වේ... LNbits නැවත ආරම්භ කරන්න සහ හැමදේම නිවැරදිව ක්‍රියාත්මක වනවාද කියා පරීක්ෂා කරන්න.



#### දත්ත සමුදායේ උපස්ථ සහ ප්‍රතිස්ථාපනය


කරුණාකර [ඉතා විස්තරාත්මක මාර්ගෝපදේශය](https://ereignishorizont.xyz/lnbits-server/en/#94_LNbits_-_Databases_Backup_Restore) මත පසුපසට සහ නැවත ස්ථාපනය කිරීමේ ක්‍රියාවලිය පිළිබඳව සළකා බලන්න.



#### LNbits Wallet මගේ නියැදියෙන් මූල්‍යය කිරීම ක්‍රියා නොකරයි


ඔබේ LNbits හි මූල්‍ය ආරම්භක මූලාශ්‍රය වන එකම නෝඩ් එකෙන් Sats යැවීමට අවශ්‍ය නම්, ඔබට LND.conf ගොනුව සංස්කරණය කළ යුතුය.


සැපයුම්කරු ඇතුළත් කළ යුතු පරාමිතීන්: `allow-circular-route=1`


කරුණාකර LND.conf හි Application options කොටස තුළ එය කරන්න. නැතහොත්, සමහර bundle node මත LND ආරම්භ කිරීම අසාර්ථක විය හැක.


නොට්: "TopUp" විකල්පය සමඟ නව adminUI දිගුව භාවිතා කිරීමට නිර්දේශිතය, LNbits ගිණුමකට මුදල් එක් කිරීමට.


#### දෝෂය 426

මට දෝෂය ලැබුණි: "lnurl සමාජ වශයෙන් ප්‍රවේශ කළ හැකි https වසමක් හෝ tor මඟින් ලබා දිය යුතුය. 426 උත්ශ්‍රේණි කිරීම අවශ්‍යයි"


මෙම දෝෂය සාමාන්‍යයෙන් සිදුවන්නේ ඔබේ LNbits ngnix සංගමයක් පිටුපස ඇති අතර LNURL Address නිවැරදිව යොමු නොකිරීම නිසා වේ. ඔබේ LNbits නවතා .env ගොනුව සංස්කරණය කර මෙම පේළිය එක් කරන්න:

`FORWARDED_ALLOW_IPS=*`


Tudi če uporabljate nastavitev ngnix, se prepričajte, da imate te glave v konfiguraciji ngnix:


```
RequestHeader set "X-Forwarded-Proto" expr=%{REQUEST_SCHEME}
RequestHeader set "X-Forwarded-SSL" expr=%{HTTPS}
```


#### ජාල දෝෂය

QR කේතයක් ස්කෑන් කිරීමේදී මට "https දෝෂයක්", ජාල දෝෂයක්" හෝ වෙනත් දේවල් ලැබුණි</summary>


නරක පුවතක්, මෙය මාර්ගගත කිරීමේ දෝෂයක් වන අතර එයට හේතු බොහෝ විය හැක. පළමුව [Lightning Decoder](https://lightningdecoder.com/) සමඟ QR හි LNURL පරීක්ෂා කරන්න, එහි විකාරයක් සොයාගත හැකි නම්. අපි ඉතාමත් සම්භාව්‍ය ගැටළු සහ ඒවායේ විසඳුම් කිහිපයක් උත්සාහ කරමු.


LNbits Tor හරහා පමණක් ක්‍රියාත්මක වන අතර, ඔබට එය lnbits.yourdomain.com වැනි මහජන වසමක විවෘත කළ නොහැක.



- මෙම විධානය ඔබේ සැකසීම මෙසේම තබා ගැනීමට අවශ්‍ය නම්, ඔබේ LNbits Wallet .onion URI භාවිතයෙන් විවෘත කර නැවත නිර්මාණය කරන්න. මෙසේ QR එක .onion URI හරහා ප්‍රවේශ විය හැකි ලෙස ජනනය වේ, එබැවින් tor හරහා පමණක්. .local URI එකකින් එම QR එක generate නොකරන්න, මන්ද එය අන්තර්ජාලය හරහා ප්‍රවේශ විය නොහැක - ඔබේ නිවසේ LAN තුළින් පමණක්.
- ඔබ භාවිතා කළ LN Wallet යෙදුම විවෘත කරන්න එම QR පරිලෝකනය කිරීමට සහ මෙම වතාවේ tor භාවිතා කිරීමෙන් (Wallet යෙදුම් සැකසුම් බලන්න). යෙදුම tor ලබා නොදෙන්නේ නම්, ඔබට Orbot (Android) භාවිතා කළ හැක. ඔබේ LNbits clearnet/https සඳහා විවෘත කරන ආකාරය පිළිබඳ විස්තරාත්මක උපදෙස් සඳහා ස්ථාපන අංශය බලන්න.



#### LNbits මත අන් අය වෝලට් ජනනය කිරීම වැළැක්වන්න


ඔබේ LNbits clearnet මත ක්‍රියාත්මක වන විට මූලිකවම හැමෝටම එය මත generate ක Wallet කළ හැක. ඔබේ node හි මුදල් මෙම පසුම්බි වලට බැඳී ඇති බැවින් ඔබට එය වළක්වා ගැනීමට අවශ්‍ය විය හැක. එය කිරීමට ක්‍රම දෙකක් ඇත:


`.env` ගොනුවේ අවසර ලත් පරිශීලකයින් සහ දිගුවන් වින්‍යාස කරන්න ([මෙහි env උදාහරණය බලන්න](https://github.com/lnbits/lnbits/blob/main/.env.example)). මෙය ක්‍රියා කරන්නේ ඔබ .env හි `adminUI=FALSE` සැකසීම භාවිතා කරන විට පමණි, නැතහොත් ඔබට එය සේවාදායකය කළමනාකරණය කිරීමේ කොටස -> පරිශීලකයින් -> අවසර ලත් පරිශීලකයින් යන තැනදී කළ යුතුය. අනෙක් සියලු දෙනාට පසුව අවසර නොලැබේ.




#### Invoice කල් ඉකුත් වීමේ කාලසීමාව අභිරුචිකරණය කරන්න.


Zdaj lahko generate račune z lastnim potekom. Združljivo z zaledji: LndRestWallet, LndWallet, CoreLightningWallet, EclairWallet, LnbitsWallet, SparkWallet do sedaj!


ඔබේ .env ගොනුවේ `LIGHTNING_INVOICE_EXPIRY` සකසා හෝ සියලුම ඉන්වොයිස සඳහා පෙරනිමි අගය වෙනස් කිරීමට AdminUI භාවිතා කළ හැක. JSON දත්තයේ කල් ඉකුත් වීම සකසන්න පුළුවන් /api/v1/payments අන්තර්ගතයේ නව ක්ෂේත්‍රයක් ද ඇත.




## Wallet-URL izbrisano


### Wallet on demo server legend.lnbits


ඔබේම පසුම්බි සඳහා Wallet-URL, Export2phone-QR හෝ LNDhub පිටපතක් සුරක්ෂිත ස්ථානයක සුරකින්න. LNbits ඔබට ඒවා අහිමි වූ විට නැවත ලබා ගැනීමට උපකාර නොකරයි.


### Wallet ඔබේම මූල්‍ය මූලාශ්‍රය/නියුඩය මත

Vedno shranite kopijo svojega Wallet-URL, Export2phone-QR ali LNDhub za svoje denarnice na varnem mestu. Vse uporabnike LNbits in Wallet-ID-je lahko najdete v svojem LNbits upravitelju uporabnikov ali v svoji sqlite bazi podatkov. Za urejanje ali branje baze podatkov LNbits pojdite v mapo LNbits /data in poiščite datoteko z imenom sqlite.db. Odprete in urejate jo lahko z excelom ali s posebnim SQL-urejevalnikom, kot je [SQLite browser](https://sqlitebrowser.org/).


ඔබට CLI හරහා පසුම්බි දමන්නත්, ඔබේ දත්ත සමුදාය තුළ ඇති සෑම Walletක්ම බලන්නත් හැක.


```
cd ~/app-data/lnbits/data
sqlite3 database.sqlite3
.dump wallets
```


ප්‍රතිදානය මෙහෙමක් පෙනේවි


```
INSERT INTO wallets VALUES('f8a43fc363ea428db5c53b3559935f1f','NAME OF WALLET','1280ff5910a9c485a782a2376f338b6c','33b95b099ce848e3b484124373f681e5','2cca208ae6d94d438227b9487ff216f9');
```

ඔබට මෙම අගයන් මෙවන් url එකකට දමන්න අවශ්‍යයි


```
https://your.lnbits.com/wallet?usr=1280ff5910a9c485a782a2376f338b6c&wal=f8a43fc363ea428db5c53b3559935f1f
```


Whereby you replace f8a43fc363ea428db5c53b3559935f1f with the value that comes before the name (in our example f8a43fc363ea428db5c53b3559935f1f) and 1280ff5910a9c485a782a2376f338b6c is your user and should become the value shown after the name. To quit sqlite3 put in


```
.quit
```

#### LNURL za lightning-Address obratno


මෙය [encoder](https://lnurl-codec.netlify.app/) fiatjaf වෙතින් හෝ [මෙය](https://lightningdecoder.com/) උත්සාහ කරන්න. LNURLp ගෙවීමට හෝ පරීක්ෂා කිරීමට [LNurlpay](https://wwww.lnurlpay.com/) ද භාවිතා කළ හැක. එය HTTPS NOT HTTP ලෙස සඳහන් විය යුතුය.



#### මගේ LNURLp QR වෙත ගෙවීමක් කරන විට ජනතාවට පෙනෙන විශේෂාංගයක් සකසන්න.

Ko ustvarite LNURL-p, privzeto polje za komentar ni izpolnjeno. To pomeni, da komentarji niso dovoljeni pri plačilih.


අදහස් ලබා දීම සඳහා, පෙට්ටියේ අකුරු දිග 1 සිට 250 දක්වා එකතු කරන්න. ඔබ එහි සංඛ්‍යාවක් දැමූ විට, ගෙවීම් ක්‍රියාවලියේ අදහස් පෙට්ටිය පෙන්වනු ඇත. ඔබ දැනටමත් නිර්මාණය කළ LNURL-p එකක් සංස්කරණය කර එම සංඛ්‍යාව එකතු කළ හැක.


![lnbits comments](assets/lnbits-comments.webp)


#### ඔන්චේන් BTC LNbits වෙත තැන්පතු කරන්න

Exchange Sats සිට onchain BTC සිට LN BTC (ප්‍රතිචාර ලෙස LNbits වෙත) යන දෙකේම ක්‍රම දෙකක් ඇත.


##### බාහිර හුවමාරු සේවාවක් හරහා.


අනෙකුත් පරිශීලකයින්ට ඔබේ LNb වෙත ප්‍රවේශය නොමැති නම්, ඔවුන්ට [Boltz](https://boltz.Exchange/), [FixedFloat](https://fixedfloat.com/), [DiamondHands](https://swap.diamondhands.technology/) හෝ [ZigZag](https://zigzag.io/) වැනි හුවමාරු සේවාවක් භාවිතා කළ හැක. ඔබේ LNbits ආකෘතියෙන් LNURL/LN ඉන්වොයිසයන් පමණක් ලබා දෙන විට, ගෙවීම්කරුට onchain Sats පමණක් තිබේ නම්, ඔවුන්ට පළමුව ඔවුන්ගේ පාර්ශවයෙන් එම Sats හුවමාරු කළ යුතු වේ. ක්‍රියාවලිය සරලයි: පරිශීලකයා හුවමාරු සේවාවට onchain btc යවයි සහ හුවමාරුවේ ගමනාන්තය ලෙස LNbits වෙතින් LNURL / LN Invoice ලබා දේ.


##### Onchain සහ Boltz LNbits දිගුව භාවිතා කිරීම.


Imejte v mislih, da je to ločen Wallet, ne LN btc, ki ga LNbits predstavlja kot "vaš Wallet" na vašem viru financiranja LN. Ta onchain Wallet se lahko uporablja tudi za zamenjavo LN btc (npr. vaša strojna denarnica) z uporabo razširitve LNbits Boltz ali Deezy. Če upravljate spletno trgovino, ki je povezana z vašim LNbits za LN plačila, je zelo priročno redno prenašati vse Sats iz LN v onchain. To vodi do več prostora v vaših LN kanalih, da lahko prejmete nove sveže Sats.


Bitcoin Hardware Wallet නොමැති අය සඳහා ක්‍රමවේදය:



- ඉලෙක්ට්රම් හෝ ස්පැරෝ Wallet භාවිතා කර නව ඔන්චේන් Wallet එකක් සාදන්න සහ ආපසු සුරැකුම seed ආරක්ෂිත ස්ථානයක සුරකින්න.
- Pojdite na informacije Wallet in kopirajte xpub.
- LNbits - Onchain විස්තාරණය වෙත ගොස් එම xpub සමඟ නව Watch-only walletක් සාදන්න.
- LNbits - Tipjar විස්තාරණය වෙත ගොස් නව Tipjar එකක් සාදන්න. LN Wallet අමතරව onchain විකල්පයද තෝරන්න.
- Izbirno - Pojdite na LNbits - razširitev SatsPay in ustvarite novo obremenitev za onchain btc. Izbirate lahko med onchain in LN ali obema. Nato bo ustvaril Invoice, ki ga je mogoče deliti.
- විකල්ප - ඔබේ LNbits එක Wordpress + Woocommerce පිටුවකට සම්බන්ධ කරන්නේ නම්, ඔබේ LN btc වෙළඳසැල Wallet වෙත Watch-only wallet එකක් නිර්මාණය/සම්බන්ධ කිරීමෙන් පසු, ගනුදෙනුකරුට එකම තිරයේදී ගෙවීම් කිරීමට විකල්ප දෙකම ලබා ගත හැක.


Ko prejmete plačilo v LNbits, bo dnevnik transakcij prikazal le povzetek vrste transakcije.


![lnbits payment details](assets/lnbits-payment-details.webp)


ඔබේ ගනුදෙනු සාරාංශයේදී ඔබට ලැබුණු Green කුඩා ඊතලයක් සහ යවන ලද මුදල් සඳහා රතු ඊතලයක් සොයා ගත හැක.


Če kliknete na te puščice, se prikaže pojavno okno s podrobnostmi, ki prikazuje priložena sporočila ter ime pošiljatelja, če je navedeno.


LNbits තුළ ගෙවීම් තුළ නමක් පෙනෙන පරිදි වින්‍යාස කිරීම මේ වන විට කළ නොහැක - නමුත් ලබා ගැනීමට හැක. මෙය සිදු කළ හැක්කේ යැවීමේ LN Wallet [LUD-18](https://github.com/lnurl/luds/blob/luds/18.md) (nameDesc) [OBW, Blixt, Alby, ZBD, BitBanana](https://github.com/lnurl/luds?tab=readme-ov-file#lnurl-documents) වැනි සහය දක්වන්නේ නම් පමණි.


ඔබේ LNbits ගනුදෙනු විස්තර කොටස (ඊතල මත ක්ලික් කරන්න) තුළ ඔබට පසුනම්/අන්වර්ථ නාමයක් දැකිය හැක. ඔබට එහි ඕනෑම නමක් ලබා දිය හැකි බවත්, එය ඔබට එවෙන නම් සත්‍ය යවන්නාගේ නමට සම්බන්ධ නොවිය හැකි බවත් සලකන්න.


![lnbits namedesc](assets/lnbits-namedesc.webp)


ඔබේ LNbits ගිණුම Wallet යෙදුමක ආයාත කිරීමට, ඔබ භාවිතා කිරීමට අවශ්‍ය ගිණුම / Wallet සමඟ ඔබේ LNbits විවෘත කර "manage extensions" වෙත ගොස් LNDHUB දිගුව සක්‍රීය කරන්න. LNDHUB දිගුව විවෘත කර, ඔබ භාවිතා කිරීමට අවශ්‍ය Wallet තෝරා "admin" හෝ "Invoice only" QR එක පරික්ෂා කරන්න, ඔබට එම Wallet සඳහා අවශ්‍ය ආරක්ෂක මට්ටම අනුව.


ඔබට [Zeus](https://zeusln.app/) හෝ [Bluewallet](https://bluewallet.io/) භාවිතා කළ හැකි අතර BW එකක් වඩා වැඩි Wallet මට්ටමක් සහය දක්වයි.


මෙය කරන විට අපි ඔබේම නෝඩ් එකකට LN ජාල URI එක සකසන්නත් නිර්දේශ කරමු. ඔබේ LNbits ආකෘතිය Tor පමණක් නම්, ඔබට Tor සක්‍රීය කළ තත්වයෙන් ඒ යෙදුම් භාවිතා කළ යුතුය. මෙම අවස්ථාවේදී ඔබට LNbits පිටුව ඔබේ Tor .onion Address හරහා විවෘත කළ යුතුය.


Če imate napako "unsupported Hash type" pri uporabi ypub v razširitvi On-Chain, preverite, ali vaša LNbits instanca uporablja python 3.10, saj bi lahko bila prizadeta zaradi [te težave](https://stackoverflow.com/questions/72409563/unsupported-Hash-type-ripemd160-with-hashlib-in-python). Uredite openssl.cnf, kot je opisano v odgovoru na stackoverflow, in ponovno zaženite vaš LNbits.



## LNbits සමඟ මෙවලම් සහ ගොඩනැගීම


LNbits සතු [විවෘත API](https://legend.lnbits.com/docs) සහ මෙවලම් විවිධ උපාංග සඳහා වැඩසටහන්ගත කිරීම සහ සම්බන්ධ කිරීම සඳහා විවිධ භාවිතා කේස් සඳහා ඇත.


Ko začnete z gradnjo, začnite s temi [MakerBits predstavitvami](https://www.youtube.com/channel/UCZhKfzK6_KWZ-CFC2wXQVBw/videos) od Ben Arc o gradnji naprav na osnovi LNbits.


### MAHATVAPŪRṆA:


- LNbits LNURL ප්‍රොටෝකෝලය මත පදනම්ව ක්‍රියා කරයි, ඉල්ලීම් වලංගු වන්නේ ආකාර දෙකකින්: https:// clearnet සබැඳියක් ලෙස (ස්වයං-අත්සන් කළ සහතික අවසර නොමැත) හෝ http:// v2/v3 onion සබැඳියක් ලෙස. LNURLp/w QR කේත හෝ NFC කාඩ්පත් වැනි LNbits සේවා වනාහි භාවිතා කළ හැකි වන පරිදි ලබා දීමට, ඔබට LNbits clearnet (https) වෙත විවෘත කළ යුතුය.
- ESP32 को पावर गर्न केवल DATA-केबलहरू प्रयोग गर्नुहोस्। सबै केबलहरूले esp लाई पावर दिनुका साथै डाटा समर्थन गर्दैनन्। यदि esp सँग आएको केबल पावर-मात्र केबल हो भने तपाईं पहिलो हुनुहुनेछैन।
- Poskrbite, da ne uporabljate USB-razdelilnika z drugimi priključenimi napravami. To lahko povzroči nenavadne učinke, ki jih je Hard težko odpravljati (npr. ne zažene ali ustavi).
- Če želite uresničiti esp projekte z MacOS, boste potrebovali UART Bridge Driver. Če imate težave z gonilnikom na sistemih Mac ali Linux, jih lahko najdete tukaj ali, če je vključen TTGO Display, tega. Če ste na Windows in imate težave s povezovanjem, se prepričajte, da prenesete STARO različico 11.1.0, ker novejša ne deluje! Tukaj lahko najdete tudi serijski terminal za preverjanje vaše povezave - nastavite na baudrate 115200.
- යදත් Platform.io භාවිතා කිරීම වඩාත් පහසු (උදාහරණයක් ලෙස, අනුයෝජිතතා ස්වයංක්‍රීයව ස්ථාපනය වේ) නමුත් නවකයින් සඳහා Arduino භාවිතා කිරීම අපි නිර්දේශ කරමු.
- TT-Go Display S3: اسڪرين پروٽيڪٽر فلم جي ٽيب جو رنگ توهان کي ٻڌائي ٿو ته ڪهڙو ڪنٽرولر صحيح طور تي (ST7735_redtab, ST7735_blacktag, ST7735_greetab, greentab128, ..) ان کي ٺاهڻ لاءِ استعمال ڪيو ويو آهي. ان کي رکو ته جيئن توهان پاڻ پروگرام ڪريو ۽ اسڪرين صحيح طور تي گرافڪس نه ڏيکاري، مثال طور، رنگ غلط، تصويرون آئيني ٿيل، يا ڪنارن تي پکسلز ڀٽڪيل. جيڪڏهن توهان کي ڪڏهن به اهو ڪرڻ جي ضرورت پوي، ته مختلف ڊسپليز لاءِ ترتيب ڏيڻ تي هڪ شاندار گائيڊ موجود آهي.
- vedno uporabljajte male črke lnurl239xx namesto LNURLl239xx
- Adding lightning:lnurl1234xyz will create a QR that requests to open the users Wallet for this Invoice on scan (last installed lightning app on iOS, setting in Android)
- Če utripate esp32 prek spleta, bo delovalo samo s temi brskalniki (TL:DR Chrome, Edge & Opera).
- කරුණාකර esp සඳහා මෙම PIN-OUT යොමු කිරීම සලකන්න
- ඔබ FOSSoftware හෝ FOSGuides භාවිතා කරන විට කරුණාකර සෑම විටම කතුවරයාට සබැඳියක් ලබා දෙන්න. සියලු දෙනාම තමන්ගේ දරුවා වර්ධනය වන ආකාරය නරඹීමට කැමතියි සහ එය නරඹීමට ඉතා අගනා ගොඩනැගීමේ දාමයක් ආරම්භ කරයි :)


ඔබට ව්‍යාපෘතියක් සඳහා උදව් අවශ්‍ය නම් [Makerbits Telegram Group](https://t.me/makerbits) වෙත පැමිණෙන්න - අපි ඔබට සහය වන්නෙමු!


![lnbits hackathlon](assets/lnbits-hackathlon.webp)


මෙන්න LNbits සමඟ ගොඩනගා ගත හැකි ව්‍යාපෘති ප්‍රවර්ග කිහිපයක්:



- [Nostr Signing Device](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#nostr-signing-device)
- [Archade Machine](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#arcade-machine)
- [Gerty](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#gerty)
- [Nostr Zap Lamp](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#zap-lamp)
- [BTC/LN ATM](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#atm)
- [LNPoS](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#lnpos-terminal)
- [Lightning Piggy](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#lightning-piggy)
- [Hardware Wallet](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#hardware-Wallet)
- [Bitcoin Switch](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#Bitcoin-switch)
- [වෙන්ඩින් යන්ත්‍රය](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#vending-machine)
- [Bolty](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#bolty)
- [Nerdminer](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#Nerdminer)
- [Bitcoin Ticker](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#Bitcoin-ticker)
- [BTClock](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#btclock)
- [Lora සහ Mesh ජාලකරණය](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#lora)



- [HELPERS & RESOURCES](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#resources)
- [LNbits මඟින් බලගැන්වෙන ව්‍යාපෘතිවල වැඩිදුර උදාහරණ මෙතන](https://github.com/lnbits/lnbits/wiki/Powered-by-LNbits).
- [LNbits සඳහා භාවිතා කරන ක්‍රම](https://github.com/lnbits/lnbits/wiki/Use-Cases-of-LNbits)