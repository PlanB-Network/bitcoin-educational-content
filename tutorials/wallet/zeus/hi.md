---
name: ज़ीउस

description: मल्टी-नोड सेल्फ-कस्टोडियल Wallet
---

![Zeus](assets/zeus_intro.webp)


ZEUS एक मोबाइल Bitcoin Wallet और नोड प्रबंधन ऐप है जिसमें Bitcoin लाइटनिंग Wallet की पूर्ण कार्यक्षमताएं हैं जो Bitcoin भुगतान को सरल बनाती हैं, उपयोगकर्ताओं को उनके वित्त पर पूर्ण नियंत्रण देती हैं, और अधिक उन्नत उपयोगकर्ताओं को अपनी हथेली से अपने लाइटनिंग नोड्स का प्रबंधन करने की अनुमति देती हैं।


## ज़ीउस किसके लिए है?

वर्तमान में ZEUS उन लोगों के लिए है जो अपने स्वयं के [Lightning Network Daemon (LND)](https://lightning.engineering/) या [कोर लाइटनिंग लाइटनिंग (CLN)](https://blockstream.com/lightning/) होम / बिजनेस नोड्स चलाते हैं और उन्हें दूरस्थ रूप से Zeus के माध्यम से प्रबंधित करते हैं।


[BTCPay](https://btcpayserver.org/) या [LNBits](https://lnbits.com/) या [Alby](https://getalby.com/) (या कोई अन्य LNDhub खाता) का उपयोग करने वाले व्यापारी भी ZEUS से अपने नोड्स / खातों से जुड़ सकते हैं, उनका उपयोग कर सकते हैं और उनका प्रबंधन कर सकते हैं।


[v0.8 से शुरू होकर](https://blog.zeusln.com/zeus-v0-8-0-open-beta/), ZEUS उन औसत उपयोगकर्ताओं की सेवा करना शुरू कर देगा जो अपने मोबाइल डिवाइस से तेज़, सस्ते Bitcoin भुगतान करने का एक सरल तरीका चाहते हैं, जिसमें एक एकीकृत [लाइटनिंग सेवा प्रदाता (LSP)](https://docs.zeusln.app/category/embedded-node) के साथ एक [अंतर्निहित मोबाइल लाइटनिंग नोड](https://docs.zeusln.app/lsp/intro) होगा।


## महत्वपूर्ण ज़ीउस संसाधन:


- ज़ीउस आधिकारिक वेबपेज - [https://zeusln.app/](https://zeusln.app/)
- ज़ीउस दस्तावेज़ीकरण - [https://docs.zeusln.app/](https://docs.zeusln.app/)
- [ज़ीउस गिटहब रिपॉजिटरी](https://github.com/ZeusLN/zeus)
- [ज़ीउस टेलीग्राम सहायता समूह](https://t.me/ZeusLN)
- [NOSTR पर ज़ीउस](https://iris.to/zeus@zeusln.app)
- [ज़ीउस ब्लॉग घोषणाएँ](https://blog.zeusln.com)


## ज़ीउस विशेषताएँ

### सामान्य सुविधाएँ:


- स्व-संरक्षित, Bitcoin और केवल लाइटनिंग Wallet
- कोई प्रोसेसिंग फीस नहीं, कोई केवाईसी नहीं
- पूर्णतः खुला स्रोत (APGLv3)
- बहु नोड / खाते समर्थित (आप अपने स्वयं के होम नोड का प्रबंधन कर सकते हैं, एम्बेडेड LND नोड चला सकते हैं, कई LNDhub खातों से कनेक्ट कर सकते हैं)
- उपयोग में आसान गतिविधि मेनू
- पिन या passphrase एन्क्रिप्शन, गोपनीयता मोड - अपना संवेदनशील डेटा छिपाएँ
- संपर्क पुस्तिका, बहु विषय, बहु भाषा


### तकनीकी सुविधाओं


- Tor से जुड़ें
- पूर्ण LNURL समर्थन (भुगतान, निकासी, प्रमाणीकरण, चैनल), लाइटनिंग पतों पर भेजें
- विस्तृत प्रकाश चैनल प्रबंधन, एमपीपी/एएमपी समर्थन, कीसेंड, रूटिंग शुल्क प्रबंधन
- Replace-by-fee (RBF) और चाइल्ड-पेज़-फॉर-पैरेंट (CPFP) सहायता
- एनएफसी भुगतान और अनुरोध, संदेशों पर हस्ताक्षर और सत्यापन
- SegWit और Taproot समर्थन
- सरल Taproot चैनल
- स्व-संरक्षित लाइटनिंग पते (@zeuspay.com)
- स्क्वायर द्वारा बिक्री केन्द्र (जल्द ही खुलेगा PoS)


## गाइड और वीडियो ट्यूटोरियल

ज़ीउस का उपयोग करने और लाइटनिंग चैनल, तरलता, शुल्क आदि का प्रबंधन करने में सक्षम होने के लिए, पहले Lightning Network के बारे में कुछ महत्वपूर्ण मार्गदर्शिकाएँ पढ़ना बेहतर है।


### मार्गदर्शक:


- [LND - Lightning Network Daemon दस्तावेज़ीकरण](https://docs.lightning.engineering/)
- [CLN - कोर लाइटनिंग डॉक्यूमेंटेशन](https://lightning.readthedocs.io/index.html)
- [शुरुआती लाइटनिंग गाइड](https://bitcoiner.guide/lightning/) – Bitcoin Q&A द्वारा
- [लाइटनिंग नोड प्रबंधन](https://www.lightningnode.info/) – openoms द्वारा
- [Lightning Network और हवाई अड्डे का सादृश्य](https://darthcoin.substack.com/p/the-lightning-network-and-the-airport)
- [लाइटनिंग नोड लिक्विडिटी का प्रबंधन](https://darthcoin.substack.com/p/managing-lightning-node-liquidity)
- [लाइटनिंग नोड रखरखाव](https://darthcoin.substack.com/p/lightning-node-maintenance)


### बीटीसी सेशंस द्वारा वीडियो ट्यूटोरियल


![Zeus Bitcoin Lightning Wallet - Mobile Node Management](https://youtu.be/hmmehTnV3ys)