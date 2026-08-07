---
name: BTCPay Server अपडेट करना
description: अपने BTCPay Server इंस्टेंस पर सुरक्षा अपडेट लागू करें और ज़रूरी क्रेडेंशियल्स रोटेट करें
---

![कवर](assets/cover.webp)

अपना पेमेंट प्रोसेसर खुद चलाने का मतलब है कि अपनी सुरक्षा टीम भी आप ही हैं। जब BTCPay Server के मेंटेनर कोई सुरक्षा रिलीज़ प्रकाशित करते हैं, तो आपका इंस्टेंस कोई और पैच नहीं करेगा: अपडेट, सत्यापन और उसके बाद होने वाला क्रेडेंशियल रोटेशन आपको ही करना होता है।

यह ट्यूटोरियल पूरी प्रक्रिया समझाता है, चाहे आपने BTCPay Server किसी भी तरीके से डिप्लॉय किया हो: चल रहा संस्करण जांचना, अपने डिप्लॉयमेंट प्रकार पर अपडेट लागू करना, यह सत्यापित करना कि अपडेट सच में लागू हुआ है, और उन सीक्रेट्स को रोटेट करना जिन्हें किसी हमलावर ने तब कैप्चर कर लिया हो सकता है जब आपका इंस्टेंस असुरक्षित था।

अगर आपने अभी तक BTCPay Server डिप्लॉय नहीं किया है, तो इंस्टॉलेशन गाइड से शुरू करें:

https://planb.academy/tutorials/business/point-of-sale/btcpay-server-928eb01e-824b-4b57-a3e8-8727633beddc

## अगस्त 2026 की गंभीर भेद्यता

⚠️ **गंभीर सुरक्षा चेतावनी (7 अगस्त 2026):** BTCPay Server को प्रभावित करने वाली एक गंभीर भेद्यता का सक्रिय रूप से दुरुपयोग किया जा रहा है और इससे धन की हानि हो सकती है। `Admin Dashboard > Server > Maintenance > Update` के ज़रिए अपने इंस्टेंस को तुरंत **संस्करण 2.4.2** पर अपडेट करें, फिर जांचें कि फुटर में `2.4.2` दिख रहा है। अगर आप तुरंत अपडेट नहीं कर सकते, तो अपना BTCPay Server बंद कर दें। अपडेट होने के बाद, आपको अपने Macaroon और अपने `macaroons.db` को भी पूरी तरह नया बनाना होगा, किसी भी अन्य Lightning बैकएंड की प्रमाणीकरण स्ट्रिंग्स को पूरी तरह नया बनाना होगा, और अगर आपने BTCPay Server के अंदर कोई हॉट ऑन-चेन वॉलेट बनाया था, तो उस धन को स्थानांतरित करके वॉलेट फिर से बनाना होगा। इंटीग्रेटर्स को NBXplorer को भी संस्करण 2.6.10 पर अपडेट करना चाहिए। स्रोत: [BTCPay Server 2.4.2 रिलीज़ नोट्स](https://github.com/btcpayserver/btcpayserver/releases/tag/v2.4.2)।

संस्करण 2.4.2 7 अगस्त 2026 को प्रकाशित किया गया था। रिलीज़ नोट्स बताते हैं कि यह एक गंभीर भेद्यता को ठीक करता है जिसका वास्तविक दुनिया में पहले से ही दुरुपयोग हो रहा था, और जिसकी रिपोर्ट `brunoerg` और `benthecarman` ने Bitcoin Red Team प्रयास के ज़रिए की थी। यही रिलीज़ Greenfield Basic authentication के ज़रिए TOTP two-factor authentication bypass को भी ठीक करती है, और खाता बनने के पांच मिनट बाद Greenfield Basic authentication को डिफ़ॉल्ट रूप से अक्षम कर देती है।

"सक्रिय रूप से दुरुपयोग किया जा रहा है" से दो परिणाम निकलते हैं:

- **अपडेट करना वैकल्पिक नहीं है और इसे अगले सप्ताह के लिए टालने वाली चीज़ नहीं है।** इंटरनेट से पहुंच योग्य कोई भी unpatched इंस्टेंस या तो अपडेट किया जाना चाहिए या बंद किया जाना चाहिए।
- **सिर्फ अपडेट करना अपने आप में पर्याप्त नहीं है।** अगर पैच करने से पहले आपका इंस्टेंस compromise हो गया था, तो हमलावर के पास आपके Lightning क्रेडेंशियल्स और BTCPay Server द्वारा आपके लिए बनाई गई किसी भी हॉट वॉलेट कुंजी-सामग्री की कॉपियां पहले से हो सकती हैं। ये सीक्रेट्स अपडेट के बाद भी तब तक मान्य रहते हैं जब तक आप उन्हें रोटेट नहीं करते। नीचे दिया गया रोटेशन सेक्शन वही हिस्सा है जिसे लोग छोड़ देते हैं, और यही वह हिस्सा है जो वास्तव में आपके धन की रक्षा करता है।

## चरण 1 — पता करें कि आप कौन सा संस्करण चला रहे हैं

अपने BTCPay Server में लॉग इन करें और **किसी भी पेज के फुटर** को देखें: संस्करण स्ट्रिंग वहीं दिखाई जाती है। आप `Admin Dashboard > Server > Maintenance` भी खोल सकते हैं, जहां मौजूदा संस्करण और अपडेट नियंत्रण दिखते हैं।

अगर आपका इंस्टेंस Greenfield API expose करता है, तो `GET /api/v1/server/info` भी संस्करण लौटाता है।

`2.4.2` से नीचे की कोई भी चीज़ vulnerable है।

## चरण 2 — अपडेट करें

### Self-hosted Docker deployment (मानक इंस्टॉल)

यह आधिकारिक Docker deployment को कवर करता है, जो आपको BTCPay Server documentation, LunaNode one-click launcher और अधिकांश VPS installs से मिलता है।

सबसे सरल रास्ता वेब इंटरफ़ेस है:

1. `Admin Dashboard > Server > Maintenance` पर जाएं।
2. **Update** पर क्लिक करें।
3. containers के pull और restart होने की प्रतीक्षा करें। इंटरफ़ेस कुछ मिनटों के लिए उपलब्ध नहीं रहेगा।

अगर वेब इंटरफ़ेस reachable नहीं है, या आप logs देखना पसंद करते हैं, तो इसे SSH पर करें:

```bash
sudo su -
cd "$BTCPAY_BASE_DIRECTORY/btcpayserver-docker"
. ./btcpay-update.sh
```

डिफ़ॉल्ट इंस्टॉल पर `$BTCPAY_BASE_DIRECTORY` `/root` होता है, इसलिए directory `/root/btcpayserver-docker` होती है। script latest images pull करती है, containers को फिर से बनाती है, और resulting versions print करती है।

Docker deployment BTCPay Server के साथ NBXplorer भी ship करता है, इसलिए मानक अपडेट NBXplorer को भी recommended `2.6.10` पर ले आता है। अगर आप NBXplorer अलग से चलाते हैं — जो integrators और custom stacks के लिए typical है — तो उसे स्पष्ट रूप से अपडेट करें।

### Umbrel

Umbrel dashboard खोलें, **App Store** पर जाएं, BTCPay Server खोजें और अगर अपडेट उपलब्ध हो तो उसे लागू करें।

⚠️ **महत्वपूर्ण:** app-store packages Umbrel team द्वारा repackage किए जाते हैं और upstream से घंटों या दिनों पीछे रह सकते हैं। अपडेट करने के बाद BTCPay Server footer में संस्करण जांचें। अगर यह अभी भी `2.4.2` से नीचे है, तो vulnerable instance को चालू छोड़ने के बजाय Umbrel dashboard से **app बंद करें** और packaged release की प्रतीक्षा करें।

समर्पित Umbrel guide app को ही कवर करती है:

https://planb.academy/tutorials/business/point-of-sale/btcpay-server-umbrel-68e1c535-4322-4507-a69c-9dfcbc36dfd1

### Start9 / StartOS

वही तर्क: StartOS marketplace से BTCPay Server अपडेट करें, फिर footer में संस्करण सत्यापित करें। अगर packaged version अभी तक `2.4.2` नहीं है, तो service को तब तक बंद रखें जब तक वह हो नहीं जाता।

### Managed और third-party hosting

अगर कोई और आपका इंस्टेंस operate करता है (hosting provider, association, किसी मित्र का server), तब भी आपको पुष्टि चाहिए। operator से footer में दिखने वाली version string पूछें, और स्पष्ट रूप से पूछें कि नीचे वर्णित post-update credential rotation किया गया है या नहीं। "हमने अपडेट किया" और "हमने आपके Macaroon रोटेट किए" एक ही जवाब नहीं हैं।

## चरण 3 — सत्यापित करें कि अपडेट सच में लागू हुआ

BTCPay Server interface को reload करें और footer में संस्करण पढ़ें। इसमें `2.4.2` या उससे ऊपर दिखना चाहिए।

update command के बिना error के exit करने पर निर्भर न रहें: constrained machines पर image pull चुपचाप fail हो सकता है और previous container चलता रह सकता है। हर बार version पढ़ें।

## चरण 4 — अपने क्रेडेंशियल्स रोटेट करें

यही चरण "patched" को "safe" बनाता है। क्योंकि fix ship होने से पहले vulnerability का दुरुपयोग हो रहा था, इसलिए आपके इंस्टेंस में मौजूद हर secret को attacker को संभावित रूप से ज्ञात मानें।

### Lightning: LND

Macaroon **और** `macaroons.db` file को regenerate करें। केवल macaroon files delete करना पर्याप्त नहीं है — LND `macaroons.db` में stored root key से macaroons derive करता है, इसलिए पुराने macaroon की copy रखने वाला attacker तब तक access बनाए रखता है जब तक वह database recreate नहीं किया जाता।

प्रक्रिया यह है: LND रोकें, network directory से `macaroons.db` और `*.macaroon` files हटाएं (mainnet के लिए, LND data directory के अंदर `data/chain/bitcoin/mainnet/`), फिर LND restart और unlock करें, जो इन्हें recreate करता है। पहले directory का backup लें, और पुराने Macaroon इस्तेमाल करने वाली हर application को फिर से pair करें — BTCPay Server खुद, Zeus, Thunderhub, RTL, Alby, और आपकी लिखी कोई भी script।

अगर आप LND को internet पर भी expose करते हैं, तो उसी समय उसके TLS certificate और किसी भी `lnd.conf` credentials की review करें।

### Lightning: अन्य backends

आपके node से string के ज़रिए authenticate होने वाली हर चीज़ को नई string मिलनी चाहिए:

- **Core Lightning**: connection द्वारा उपयोग किए गए rune या access credentials को regenerate करें।
- **Phoenixd**: HTTP password रोटेट करें।
- **LNbits and similar**: admin और invoice keys को revoke और reissue करें।
- **Remote node connection strings** जो BTCPay Server store settings में stored हैं: उन्हें नए secrets के साथ rewrite करें।

### BTCPay Server के अंदर बनाया गया hot on-chain wallet

अगर आपने BTCPay Server को अपने लिए on-chain wallet generate करने दिया था — hardware wallet connect करने या ऐसा xpub import करने के विपरीत जिसकी keys ने कभी server को touch नहीं किया — तो वह seed machine पर मौजूद था।

इसे burned मानें:

1. नया wallet बनाएं, ideally hardware wallet के साथ ताकि keys फिर कभी server पर न रहें।
2. पुराने wallet से funds को नए wallet में sweep करें।
3. store settings में derivation scheme को नए wallet से replace करें।
4. पुराने seed को कभी reuse न करें।

Watch-only setups (xpub या hardware wallet) को इसकी ज़रूरत नहीं है: private keys कभी server पर थीं ही नहीं। यही कारण है कि installation guide उनकी recommendation करती है।

### BTCPay Server accounts और API keys

जब आप यह कर ही रहे हैं:

- instance पर हर user account के passwords बदलें।
- सभी Greenfield **API keys** revoke और reissue करें।
- two-factor authentication को फिर से enroll करें, क्योंकि 2.4.2 एक 2FA bypass ठीक करता है।
- `Admin Dashboard > Server > Users` खोलें और जांचें कि कोई unexpected account मौजूद नहीं है।
- हाल की **payouts**, **pull payments** और **refunds** की review करें, ऐसी entries के लिए जिन्हें आपने create नहीं किया।
- अपने webhooks और उनके secrets की review करें।

## चरण 5 — अगली बार के लिए सूचित रहें

Security releases केवल उन operators की मदद करती हैं जिन्हें उनके बारे में पता चलता है:

- [GitHub पर BTCPay Server releases](https://github.com/btcpayserver/btcpayserver/releases) देखें — GitHub आपको repository की हर new release पर email कर सकता है।
- project के announcement channels और [official blog](https://blog.btcpayserver.org/) को follow करें।
- अपने instance को ऐसे version पर रखें जिसे आप जल्दी update कर सकें: आप जितने ज्यादा पीछे होंगे, emergency update उतना ही painful बन जाएगा।

Self-hosting आपको अपने payments पर sovereignty देता है। उस sovereignty की cost ठीक यही है: release notes पढ़ना और patch करने वाला व्यक्ति खुद होना।
