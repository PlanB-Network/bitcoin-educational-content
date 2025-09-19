---
name: RGB
description: RGB पर परिचय और परिसंपत्ति निर्माण
---

![cover](assets/cover.webp)


## परिचय


3 जनवरी 2009 को Satoshi नाकामोटो ने पहला Bitcoin नोड लॉन्च किया, उस क्षण से नए नोड्स जुड़ गए और Bitcoin ने ऐसा व्यवहार करना शुरू कर दिया जैसे कि यह जीवन का एक नया रूप हो, जीवन का एक ऐसा रूप जिसने विकसित होना बंद नहीं किया है, धीरे-धीरे यह अपने अद्वितीय डिजाइन के परिणामस्वरूप दुनिया का सबसे सुरक्षित नेटवर्क बन गया है, जिसे Satoshi द्वारा बहुत अच्छी तरह से सोचा गया है, क्योंकि आर्थिक प्रोत्साहन के माध्यम से, यह उपयोगकर्ताओं को आमतौर पर खनिकों को ऊर्जा और कंप्यूटिंग शक्ति में निवेश करने के लिए आकर्षित करता है जो नेटवर्क सुरक्षा में योगदान देता है।


जैसे-जैसे Bitcoin का विकास और अपनापन जारी है, यह स्केलेबिलिटी के मुद्दों का सामना कर रहा है, Bitcoin नेटवर्क 10 मिनट के अनुमानित समय में लेनदेन के साथ एक नया ब्लॉक खनन करने की अनुमति देता है, यह मानते हुए कि हमारे पास एक दिन में 144 ब्लॉक हैं, जिनमें प्रति ब्लॉक अधिकतम 2700 लेनदेन हैं, Bitcoin ने प्रति सेकंड केवल 4.5 लेनदेन की अनुमति दी होगी, Satoshi को इस सीमा के बारे में पता था, हम इसे मार्च 2011 में माइक हर्न को भेजे गए एक ईमेल1 में देख सकते हैं जहाँ वह बताते हैं कि आज हम जिसे भुगतान चैनल के रूप में जानते हैं वह कैसे काम करता है। पुष्टिकरण की प्रतीक्षा किए बिना जल्दी और सुरक्षित रूप से माइक्रोपेमेंट। यहीं पर off-chain प्रोटोकॉल आते हैं।


क्रिश्चियन डेकर2 के अनुसार off-chain प्रोटोकॉल आम तौर पर ऐसे सिस्टम होते हैं जिनमें उपयोगकर्ता Blockchain से डेटा का उपयोग करते हैं और अंतिम क्षण तक Blockchain को छुए बिना इसे प्रबंधित करते हैं। इस अवधारणा के आधार पर, Lightning Network का जन्म हुआ, एक नेटवर्क जो off-chain प्रोटोकॉल का उपयोग करके Bitcoin भुगतानों को लगभग तुरंत करने की अनुमति देता है और चूंकि ये सभी ऑपरेशन ब्लॉक चेन पर नहीं लिखे जाते हैं, इसलिए यह प्रति सेकंड हजारों लेनदेन की अनुमति देता है और Bitcoin को स्केल करता है।


Bitcoin पर off-chain प्रोटोकॉल के क्षेत्र में अनुसंधान और विकास ने एक भानुमती का पिटारा खोल दिया है, आज हम जानते हैं कि हम विकेन्द्रीकृत तरीके से मूल्य हस्तांतरण से कहीं अधिक हासिल कर सकते हैं, गैर-लाभकारी LNP/BP मानक एसोसिएशन Bitcoin और Lightning Network पर Layer 2 और 3 प्रोटोकॉल के विकास पर ध्यान केंद्रित करता है, इन परियोजनाओं में RGB सबसे अलग है।


## जीडब्ल्यू-16 क्या है?


RGB पीटर टोड3 द्वारा सिंगल-यूज़-सील्स और क्लाइंट-साइड-वैलिडेशन पर किए गए शोध से सामने आया है, जिसे 2016-2019 में जियाकोमो ज़ुको और समुदाय द्वारा Bitcoin और Lightning Network के लिए बेहतर एसेट प्रोटोकॉल के रूप में गढ़ा गया था। इन विचारों के आगे विकास ने RGB को मैक्सिम ओरलोव्स्की द्वारा एक पूर्ण विकसित Smart contract प्रणाली में विकसित किया, जो 2019 से सामुदायिक भागीदारी के साथ इसके कार्यान्वयन का नेतृत्व कर रहे हैं।


हम RGB को ओपन सोर्स प्रोटोकॉल के एक सेट के रूप में परिभाषित कर सकते हैं जो हमें जटिल स्मार्ट कॉन्ट्रैक्ट को स्केलेबल और गोपनीय तरीके से निष्पादित करने की अनुमति देता है। यह कोई विशेष नेटवर्क नहीं है (जैसे Bitcoin या लाइटनिंग); प्रत्येक Smart contract केवल Contract प्रतिभागियों का एक सेट है जो विभिन्न संचार चैनलों (डिफ़ॉल्ट रूप से Lightning Network) का उपयोग करके बातचीत कर सकते हैं। RGB Bitcoin Blockchain को Commitment राज्य के Layer के रूप में उपयोग करता है और Smart contract और डेटा off-chain के कोड को बनाए रखता है, जो इसे स्केलेबल बनाता है, स्मार्ट कॉन्ट्रैक्ट के लिए Ownership नियंत्रण प्रणाली के रूप में Bitcoin लेनदेन (और स्क्रिप्ट) का लाभ उठाता है; जबकि Smart contract का विकास off-chain योजना द्वारा परिभाषित किया गया है, अंत में यह ध्यान रखना महत्वपूर्ण है कि क्लाइंट साइड पर सब कुछ मान्य है।


सरल शब्दों में, RGB एक ऐसी प्रणाली है जो उपयोगकर्ता को किसी भी समय Smart contract का ऑडिट करने, उसे निष्पादित करने और व्यक्तिगत रूप से सत्यापित करने की अनुमति देती है, वह भी बिना किसी अतिरिक्त लागत के, क्योंकि इसके लिए यह "पारंपरिक" प्रणालियों की तरह Blockchain का उपयोग नहीं करती है, जटिल स्मार्ट अनुबंध प्रणालियों का बीड़ा एथेरियम द्वारा उठाया गया था, लेकिन क्योंकि इसमें उपयोगकर्ता को प्रत्येक ऑपरेशन के लिए महत्वपूर्ण मात्रा में गैस खर्च करने की आवश्यकता होती है, इसलिए वे कभी भी उस स्केलेबिलिटी को प्राप्त नहीं कर पाए जिसका उन्होंने वादा किया था, परिणामस्वरूप वर्तमान वित्तीय प्रणाली से बाहर किए गए उपयोगकर्ताओं को बैंकिंग करना कभी भी एक विकल्प नहीं था।


वर्तमान में, Blockchain उद्योग यह बढ़ावा देता है कि स्मार्ट कॉन्ट्रैक्ट्स के कोड और डेटा दोनों को Blockchain में संग्रहीत किया जाना चाहिए और नेटवर्क के प्रत्येक नोड द्वारा निष्पादित किया जाना चाहिए, चाहे आकार में अत्यधिक वृद्धि हो या कम्प्यूटेशनल संसाधनों का दुरुपयोग हो। RGB द्वारा प्रस्तावित योजना बहुत अधिक बुद्धिमान और कुशल है क्योंकि यह Blockchain प्रतिमान के साथ स्मार्ट कॉन्ट्रैक्ट्स और डेटा को Blockchain से अलग करके काटती है और इस प्रकार अन्य प्लेटफ़ॉर्म में देखी गई नेटवर्क की संतृप्ति से बचती है, बदले में यह प्रत्येक नोड को प्रत्येक Contract को निष्पादित करने के लिए बाध्य नहीं करती है, बल्कि इसमें शामिल पक्षों को बाध्य करती है जो गोपनीयता को पहले कभी नहीं देखे गए स्तर तक बढ़ाती है।


![RGB vs Ethereum](assets/1.webp)


## RGB में स्मार्ट अनुबंध


RGB में Smart contract डेवलपर एक योजना को परिभाषित करता है जिसमें Contract के समय के साथ विकसित होने के नियमों को निर्दिष्ट किया जाता है। यह योजना RGB में स्मार्ट अनुबंधों के निर्माण के लिए मानक है, और जारी करने के लिए Contract और Wallet या Exchange को परिभाषित करते समय जारीकर्ता को एक विशेष योजना का पालन करना चाहिए जिसके विरुद्ध उन्हें Contract को मान्य करना चाहिए। केवल तभी जब सत्यापन सही हो, प्रत्येक पक्ष अनुरोध स्वीकार कर सकता है और परिसंपत्ति के साथ काम कर सकता है।


RGB में Smart contract राज्य परिवर्तनों का Directed Acyclic Graph (DAG) है, जहाँ ग्राफ़ का केवल एक भाग हमेशा ज्ञात होता है और बाकी तक कोई पहुँच नहीं होती है। RGB योजना इस ग्राफ़ के विकास के लिए नियमों का एक मुख्य सेट है जिससे Smart contract शुरू होता है। प्रत्येक Contract Participant उन नियमों में कुछ जोड़ सकता है (यदि Schema द्वारा इसकी अनुमति है) और परिणामी ग्राफ़ उन नियमों के पुनरावृत्त अनुप्रयोग से बनाया जाता है।


## परिवर्तनीय परिसंपत्तियां


RGB में परिवर्तनीय परिसंपत्तियाँ LNPBP RGB-20 विनिर्देश4 का पालन करती हैं, जब RGB-20 को परिभाषित किया जाता है, तो परिसंपत्ति डेटा जिसे "Genesis डेटा" के रूप में जाना जाता है, Lightning Network के माध्यम से वितरित किया जाता है, जिसमें परिसंपत्ति का उपयोग करने के लिए आवश्यक चीजें शामिल होती हैं। परिसंपत्तियों का सबसे बुनियादी रूप द्वितीयक जारीकरण, टोकन बर्निंग, पुनर्नामांकन या प्रतिस्थापन की अनुमति नहीं देता है।


कभी-कभी जारीकर्ता को भविष्य में और अधिक टोकन जारी करने की आवश्यकता होगी, जैसे कि USDT जैसे स्थिर सिक्के, जो प्रत्येक टोकन के मूल्य को USD जैसी मुद्रास्फीति वाली मुद्रा के मूल्य से जोड़े रखते हैं। इसे प्राप्त करने के लिए अधिक जटिल RGB-20 स्कीमाटा मौजूद है, और Genesis डेटा के अलावा उन्हें जारीकर्ता को खेप का उत्पादन करने की आवश्यकता होती है, जो Lightning Network में भी प्रसारित होगी; इस जानकारी से हम परिसंपत्ति के कुल परिसंचारी Supply को जान सकते हैं। यही बात परिसंपत्तियों को जलाने या उसका नाम बदलने पर भी लागू होती है।


संपत्ति से संबंधित जानकारी सार्वजनिक या निजी हो सकती है: यदि जारीकर्ता को गोपनीयता की आवश्यकता है, तो वह टोकन के बारे में जानकारी साझा न करने और पूर्ण गोपनीयता में संचालन करने का विकल्प चुन सकता है, लेकिन हमारे पास विपरीत मामला भी है जिसमें जारीकर्ता और धारकों को पूरी प्रक्रिया पारदर्शी होने की आवश्यकता होती है। यह टोकन डेटा साझा करके हासिल किया जाता है।


## RGB-20 प्रक्रियाएं


बर्निंग प्रक्रिया टोकन को निष्क्रिय कर देती है, बर्न किए गए टोकन का अब उपयोग नहीं किया जा सकता।


प्रतिस्थापन प्रक्रिया तब होती है जब टोकन को जला दिया जाता है और उसी टोकन की एक नई मात्रा बनाई जाती है। यह परिसंपत्ति के ऐतिहासिक डेटा के आकार को कम करने में मदद करता है, जो परिसंपत्ति की गति को बनाए रखने के लिए महत्वपूर्ण है।


ऐसे उपयोग के मामले का समर्थन करने के लिए जहां परिसंपत्तियों को बदले बिना उन्हें जलाना संभव है, RGB-20 की एक उप-योजना का उपयोग किया जाता है जो केवल परिसंपत्तियों को जलाने की अनुमति देता है।


## गैर-परिवर्तनीय परिसंपत्तियां


RGB में गैर-परिवर्तनीय संपत्ति LNPBP RGB-21 विनिर्देशन5 का पालन करती है, जब हम NFT के साथ काम करते हैं तो हमारे पास एक मुख्य योजना और एक उप-योजना भी होती है। इन योजनाओं में एक उत्कीर्णन प्रक्रिया होती है, जो हमें टोकन स्वामी के हिस्से द्वारा कस्टम डेटा संलग्न करने की अनुमति देती है, आज NFT में हम जो सबसे आम उदाहरण देखते हैं वह टोकन से जुड़ी डिजिटल कला है। टोकन जारीकर्ता RGB-21 उप-योजना का उपयोग करके इस डेटा उत्कीर्णन को प्रतिबंधित कर सकता है। अन्य NFT Blockchain प्रणालियों के विपरीत, RGB बड़े आकार के मीडिया टोकन डेटा को पूरी तरह से विकेन्द्रीकृत और सेंसरशिप-प्रतिरोधी तरीके से वितरित करने की अनुमति देता है, जो कि Bifrost नामक लाइटनिंग P2P नेटवर्क के विस्तार का उपयोग करता है, जिसका उपयोग RGB-विशिष्ट Smart contract कार्यात्मकताओं के कई अन्य रूपों के निर्माण के लिए भी किया जाता है।


इसके अतिरिक्त, फंगसिबल एसेट्स और एनएफटी के अलावा, जीडब्ल्यू-61 और बिफ्रॉस्ट का उपयोग स्मार्ट कॉन्ट्रैक्ट्स के अन्य रूपों का उत्पादन करने के लिए किया जा सकता है, जिसमें डीईएक्स, लिक्विडिटी पूल, एल्गोरिथम स्टेबल कॉइन आदि शामिल हैं, जिन्हें हम भविष्य के लेखों में कवर करेंगे।


## RGB से NFT बनाम अन्य प्लेटफार्मों से NFT



- महंगे Blockchain भंडारण की कोई आवश्यकता नहीं
- IPFS की आवश्यकता नहीं है, इसके बजाय Lightning Network एक्सटेंशन (जिसे Bifrost कहा जाता है) का उपयोग किया जाता है (और यह पूरी तरह से एंड-टू-एंड एन्क्रिप्टेड है)
- किसी विशेष डेटा प्रबंधन समाधान की आवश्यकता नहीं - फिर से, बिफ्रॉस्ट यह भूमिका निभाता है
- एनएफटी टोकन या जारी परिसंपत्तियों / जीडब्ल्यू-65 एबीआई के बारे में डेटा बनाए रखने के लिए वेबसाइटों पर भरोसा करने की आवश्यकता नहीं है
- अंतर्निहित DRM एन्क्रिप्शन और Ownership प्रबंधन
- Lightning Network (बिफ्रोस्ट) का उपयोग करके बैकअप के लिए बुनियादी ढांचा
- सामग्री से पैसा कमाने के तरीके (न केवल NFT को बेचना, बल्कि कई बार सामग्री तक पहुंच बनाना)


## निष्कर्ष


लगभग 13 वर्ष पहले Bitcoin के लॉन्च के बाद से इस क्षेत्र में बहुत सारे शोध और प्रयोग हुए हैं, सफलताओं और गलतियों दोनों ने हमें थोड़ा और समझने की अनुमति दी है कि विकेन्द्रीकृत प्रणालियाँ व्यवहार में कैसे व्यवहार करती हैं, क्या उन्हें वास्तव में विकेन्द्रित बनाता है और कौन सी क्रियाएँ उन्हें केंद्रीकरण की ओर ले जाती हैं, इन सबने हमें यह निष्कर्ष निकालने के लिए प्रेरित किया है कि वास्तविक विकेन्द्रीकरण एक दुर्लभ और कठिन घटना है, वास्तविक विकेन्द्रीकरण केवल Bitcoin द्वारा प्राप्त किया गया है और यह इस कारण से है कि हम इसके शीर्ष पर निर्माण करने के लिए अपने प्रयासों पर ध्यान केंद्रित करते हैं।


RGB के पास Bitcoin खरगोश छेद के भीतर अपना स्वयं का खरगोश छेद है, जबकि मैं उनके माध्यम से नीचे गिर रहा हूं, मैं जो कुछ सीखा है उसे पोस्ट करूंगा, अगले लेख में हमारे पास LNP और RGB नोड्स का परिचय होगा और उनका उपयोग कैसे करें।



- 1 https://plan99.net/~mike/Satoshi-emails/thread4.html
- 2 https://btctransscripts.com/चेनकोड-लैब्स/चेनकोड-रेसिडेंसी/2018-10-22-christian-decker-history-of-lightning/
- 3 https://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2016-जून/012773.html
- 4 https://github.com/LNP-BP/LNPBPs/blob/master/lnpbp-0020.md
- 5 https://github.com/LNP-BP/LNPBPs/blob/master/lnpbp-0021.md


# RGB-नोड ट्यूटोरियल


## परिचय


इस ट्यूटोरियल में हम बताएंगे कि फंगसिबल टोकन बनाने के लिए RGB-नोड का उपयोग कैसे करें और इसे कैसे स्थानांतरित करें, यह दस्तावेज़ RGB-नोड डेमो पर आधारित है और इसमें अंतर यह है कि यह ट्यूटोरियल वास्तविक Testnet डेटा का उपयोग करता है और इसके लिए, हमें अब से अपना स्वयं का Partially Signed Bitcoin Transaction, PSBT बनाना होगा।


## आवश्यकताएं


लिनक्स वितरण का उपयोग अनुशंसित है, यह ट्यूटोरियल Pop!OS का उपयोग करके लिखा गया है, जो उबंटू पर आधारित है और आपको इसकी आवश्यकता होगी:



- माल
- Bitcoin कोर
- गिट


नोट: यह ट्यूटोरियल लिनक्स टर्मिनल में कमांड के निष्पादन को दर्शाता है, उपयोगकर्ता क्या लिखता है और टर्मिनल में उसे क्या प्रतिक्रिया मिलती है, इसके बीच अंतर करने के लिए, हमने $ को bash प्रॉम्प्ट का प्रतीक के रूप में शामिल किया है।


आपको कुछ निर्भरताएं स्थापित करने की आवश्यकता होगी:


```
$ sudo apt install -y build-essential pkg-config libzmq3-dev libssl-dev libpq-dev libsqlite3-dev cmake
```


निर्माण और संचालन


RGB-नोड कार्य प्रगति पर है (WIP), यही कारण है कि हमें इसे सही ढंग से संकलित और उपयोग करने में सक्षम होने के लिए खुद को एक विशिष्ट कमिट (3f3c520c19d84c66d430e76f0fc68c5a66d79c84) में स्थित करना होगा, इसके लिए हम निम्नलिखित कमांड निष्पादित करते हैं।


```
$ git clone https://github.com/rgb-org/rgb-node.git
$ cd rgb-node
$ git checkout 3f3c520c19d84c66d430e76f0fc68c5a66d79c84
```


अब हम इसे संकलित करते हैं, --locked फ्लैग का उपयोग करना न भूलें क्योंकि क्लैप के एक संस्करण में एक महत्वपूर्ण परिवर्तन किया गया है।


```
$ cargo install --path . --all-features --locked

....
....
Finished release [optimized] target(s) in 2m 14s
Installing /home/user/.cargo/bin/fungibled
Installing /home/user/.cargo/bin/rgb-cli
Installing /home/user/.cargo/bin/rgbd
Installing /home/user/.cargo/bin/stashd
Installed package `rgb_node v0.4.2 (/home/user/dev/rgb-node)` (executables `fungibled`, `rgb-cli`, `rgbd`, `stashd`)

```


जैसा कि Rust कंपाइलर हमें बताता है, बाइनरी को $HOME/.cargo/bin निर्देशिका में कॉपी किया गया था, यदि आपके कंपाइलर ने उन्हें किसी अलग स्थान पर कॉपी किया है तो आपको यह सुनिश्चित करना होगा कि वह निर्देशिका $PATH में शामिल होनी चाहिए।


स्थापित बाइनरी में हम तीन डेमॉन या सेवाएँ (वे फ़ाइलें जो d में समाप्त होती हैं) और एक CLI (कमांड लाइन Interface) देख सकते हैं, CLI हमें मुख्य rgbd daemon के साथ बातचीत करने की अनुमति देता है। जैसा कि इस ट्यूटोरियल में हम दो नोड्स चलाने जा रहे हैं, हमें दो क्लाइंट की भी आवश्यकता होगी, प्रत्येक को अपने स्वयं के नोड से कनेक्ट होना चाहिए, इसके लिए हम दो उपनाम बनाते हैं।


```
alias rgb0-cli="$HOME/.cargo/bin/rgb-cli -d $HOME/rgbdata/data0 -n testnet"
alias rgb1-cli="$HOME/.cargo/bin/rgb-cli -d $HOME/rgbdata/data1 -n testnet"
```


हम केवल उपनामों को चला सकते हैं या उन्हें $HOME/.bashrc फ़ाइल के अंत में जोड़ सकते हैं और स्रोत $HOME/.bashrc चला सकते हैं।

आधार


RGB-नोड किसी भी तरह की Wallet-संबंधित कार्यक्षमता को संभालता नहीं है, यह केवल Bitcoin कोर जैसे बाहरी Wallet द्वारा प्रदान किए जाने वाले डेटा पर RGB-विशिष्ट कार्य करता है। विशेष रूप से, जारी करने और हस्तांतरण के साथ एक बुनियादी वर्कफ़्लो का प्रदर्शन करने के लिए, हमें निम्न की आवश्यकता होगी:



- एक issuance_utxo जिससे RGB-node-0 नई जारी की गई संपत्ति को बांध देगा
- एक received_utxo जहां RGB-node-1 परिसंपत्ति प्राप्त करता है
- एक change_utxo जहां RGB-node-0 परिसंपत्ति परिवर्तन प्राप्त करता है
- एक Partially Signed Bitcoin Transaction (tx.PSBT), जिसकी आउटपुट सार्वजनिक कुंजी को स्थानांतरण में Commitment को शामिल करने के लिए संशोधित किया जाएगा।


हम Bitcoin कोर CLI का उपयोग करेंगे, हमें bitcoind daemon को Testnet पर चलाने की आवश्यकता है, इससे हमें अंतर-संचालन क्षमता मिलेगी और अंत में हम अपनी स्वयं की परिसंपत्तियों को अन्य RGB उपयोगकर्ताओं को भेजने में सक्षम होंगे जिन्होंने इस ट्यूटोरियल का पालन किया है।


सरलता के लिए हम इस उपनाम को अपनी ~/.bashrc फ़ाइल के अंत में जोड़ देंगे।


```
alias bcli="bitcoin-cli -testnet"
```


आइए अपने अप्रयुक्त आउटपुट लेनदेन को सूचीबद्ध करें और दो का चयन करें, एक issuance_utxo होगा और दूसरा change_utxo, इससे कोई फर्क नहीं पड़ता कि कौन सा क्या है, महत्वपूर्ण बात यह है कि जारीकर्ता के पास इन दो UTXO का नियंत्रण है।


```
$ bcli listunspent
[
{
"txid": "4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893",
"vout": 1,
"address": "tb1qn4w9u5x0hxgm30hx6q2rhdwz58xr4ekqdq0vgm",
"label": "",
"scriptPubKey": "00149d5c5e50cfb991b8bee6d0143bb5c2a1cc3ae6c0",
"amount": 0.01703963,
"confirmations": 62432,
"spendable": true,
"solvable": true,
"desc": "wpkh([ec924f82/0'/0'/5']031e0fc9a03e69326c3deeabfd749a7f7b094e3151ada90cd13019efac663c5663)#dj7rhpdt",
"safe": true
},
{
"txid": "cd66d3b77dfc1c2ecf958847c16a8a1311bba84ee7bf9dd55592a7b97b13028f",
"vout": 1,
"address": "tb1qyd537gf0xmm9ehmhaf3nv0a230crg56mhp9ap3",
"scriptPubKey": "001423691f212f36f65cdf77ea63363faa8bf034535b",
"amount": 0.02877504,
"confirmations": 189184,
"spendable": true,
"solvable": true,
"desc": "wpkh([ec924f82/0'/1'/0']03ae333417e86840145e95ab2852c8f7ca8b8f82cd910883f7ce0c69649403cef2)#jlcj23vw",
"safe": true
}
]
```


आगे बढ़ने से पहले हमें आउटपॉइंट्स के बारे में बात करने की ज़रूरत है, एक एकल लेनदेन में कई आउटपुट शामिल हो सकते हैं, आउटपॉइंट में 32-बाइट txid और 4-बाइट आउटपुट इंडेक्स नंबर (vout) दोनों शामिल हैं जो कोलन से अलग किए गए विशिष्ट आउटपुट को संदर्भित करते हैं: हमारे लिस्टअनस्पेंट आउटपुट में हम दो UTXO पा सकते हैं, प्रत्येक पर हम txid और vout देख सकते हैं, वे आउट issuance_utxo और change_utxo आउटपॉइंट हैं।


get_utxo एक UTXO है जिसे रिसीवर द्वारा नियंत्रित किया जाता है, इस मामले में हम e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0 का उपयोग करेंगे जो कि दूसरे Wallet का एक आउटपॉइंट है।



- जारी_utxo: 4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1
- Change_utxo: cd66d3b77dfc1c2ecf958847c16a8a1311bba84ee7bf9dd55592a7b97b13028f:1
- रिसीव_यूटीएक्सओ: e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0


अब हम आंशिक रूप से हस्ताक्षरित लेनदेन (tx.PSBT) बनाने जा रहे हैं, जिसके आउटपुट को स्थानांतरित करने के लिए प्रतिबद्धता को शामिल करने के लिए संशोधित किया जाएगा, txid और vout को अपने स्वयं के साथ बदलना याद रखें, गंतव्य Address वास्तव में मायने नहीं रखता है, यह आपका हो सकता है या किसी अन्य व्यक्ति का हो सकता है, इससे कोई फर्क नहीं पड़ता कि वे Sats कहां जाते हैं, महत्वपूर्ण बात यह है कि हम issuance_utxo का उपयोग करते हैं।


```
$ bcli walletcreatefundedpsbt "[{/"txid/":/"4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893/",/"vout/":1}]" "[{/"tb1q9crtjp0y6rt00c4fcrmuamrylzkcalcxls80j9/":/"0.00050000/"}]"
{
"psbt": "cHNidP8BAHECAAAAAZM4E58uD9auiZ7esJkFbmD5p/7PcgBTn5UwiQ0hhRdMAQAAAAD/////ArM7GQAAAAAAFgAU4xQr/g1lgG2P9+gZudpFD8mOGGRQwwAAAAAAABYAFC4GuQXk0Nb34qnA987sZPitjv8GAAAAAAABAHECAAAAAYiK0TdTiaEs4oDovRokqspfLZr5EHYH8Pnj/Tv5GFB5AQAAAAD+////Av8Bh80AAAAAFgAUsLjOd30aRkUna41LAT5c3CnAz5obABoAAAAAABYAFJ1cXlDPuZG4vubQFDu1wqHMOubAyw8gAAEBHxsAGgAAAAAAFgAUnVxeUM+5kbi+5tAUO7XCocw65sAiBgMeD8mgPmkybD3uq/10mn97CU4xUa2pDNEwGe+sZjxWYxDskk+CAAAAgAAAAIAFAACAACICA2J21wOqW6bj7/ePTVI7QGvU6e4Sk8DhN5pmd9hrwSd7EOyST4IAAACAAQAAgAcAAIAAAA==",
"fee": 0.00000280,
"changepos": 0
}
```


आउटपुट ने हमें बेस64 एनकोडिंग में PSBT दिया, जिसका उपयोग हम tx.PSBT बनाने के लिए करेंगे।


```
$ echo "cHNidP8BAHECAAAAAZM4E58uD9auiZ7esJkFbmD5p/7PcgBTn5UwiQ0hhRdMAQAAAAD/////ArM7GQAAAAAAFgAU4xQr/g1lgG2P9+gZudpFD8mOGGRQwwAAAAAAABYAFC4GuQXk0Nb34qnA987sZPitjv8GAAAAAAABAHECAAAAAYiK0TdTiaEs4oDovRokqspfLZr5EHYH8Pnj/Tv5GFB5AQAAAAD+////Av8Bh80AAAAAFgAUsLjOd30aRkUna41LAT5c3CnAz5obABoAAAAAABYAFJ1cXlDPuZG4vubQFDu1wqHMOubAyw8gAAEBHxsAGgAAAAAAFgAUnVxeUM+5kbi+5tAUO7XCocw65sAiBgMeD8mgPmkybD3uq/10mn97CU4xUa2pDNEwGe+sZjxWYxDskk+CAAAAgAAAAIAFAACAACICA2J21wOqW6bj7/ePTVI7QGvU6e4Sk8DhN5pmd9hrwSd7EOyST4IAAACAAQAAgAcAAIAAAA==" | base64 -d > tx.psbt
```


आइए rgbdata नामक एक नई निर्देशिका बनाएं जिसमें प्रत्येक नोड की डेटा निर्देशिका संग्रहीत होगी।


```
$ mkdir $HOME/rgbdata
$ cd $HOME/rgbdata
```


पहले से ही $HOME/rgbdata में स्थित हम प्रत्येक नोड को अलग-अलग टर्मिनलों में शुरू करते हैं, जहां ~/.cargo/bin वह निर्देशिका है जहां कार्गो ने RGB-नोड स्थापना के बाद सभी बाइनरीज़ की प्रतिलिपि बनाई है।


```
$ rgbd -vvvv -b ~/.cargo/bin -d ./data0 -n testnet
$ rgbd -vvvv -b ~/.cargo/bin -d ./data1 -n testnet
```


## जारी करना


किसी परिसंपत्ति को जारी करने के लिए हम फंगिबल इश्यू उपकमांड के साथ rgb0-CLI चलाते हैं, फिर तर्क, टिकर USDT, नाम "USD Tether" और आवंटन में हम जारी करने की राशि और issuance_utxo का उपयोग करेंगे जैसा कि हम नीचे देखते हैं:


```
$ rgb0-cli fungible issue USDT "USD Tether" 1000@4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1
```


संपत्ति सफलतापूर्वक जारी की गई। साझा करने के लिए इस जानकारी का उपयोग करें:

परिसंपत्ति की जानकारी:


```
genesis: genesis1qyfe883hey6jrgj2xvk5g3dfmfqfzm7a4wez4pd2krf7ltsxffd6u6nrvjvvnc8vt9llmp7663pgututl9heuwaudet72ay9j6thc6cetuvhxvsqqya5xjt2w9y4u6sfkuszwwctnrpug5yjxnthmr3mydg05rdrpspcxysnqvvqpfvag2w8jxzzsz9pf8pjfwf0xvln5z7w93yjln3gcnyxsa04jsf2p8vu4sxgppfv0j9qerppqxhvztpqscnjsxvq5gdfy5v6j3wvpjxxqzcerxuglngnfvpxjkgqusct7cyx8zzezcfpqv3nxjxm2kjj4d0zu0ta6fjmpr8a0calk6h88h4ap5e4nucj0ch07aa73qsh3lj5sd89a32kwy0eq7tsa5zqqjpdqvqq5s46r0
id: rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6
ticker: USDT
name: USD Tether
description: ~
knownCirculating: 1000
isIssuedKnown: ~
issueLimit: 0
chain: testnet
decimalPrecision: 0
date: "2022-02-23T20:53:26"
knownIssues:
- id: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
amount: 1000
origin: ~
knownInflation: {}
knownAllocations:
- nodeId: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
index: 0
outpoint: "4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1"
revealedAmount:
value: 1000
blinding: "0000000000000000000000000000000000000000000000000000000000000001"


genesis1qyfe883hey6jrgj2xvk5g3dfmfqfzm7a4wez4pd2krf7ltsxffd6u6nrvjvvnc8vt9llmp7663pgututl9heuwaudet72ay9j6thc6cetuvhxvsqqya5xjt2w9y4u6sfkuszwwctnrpug5yjxnthmr3mydg05rdrpspcxysnqvvqpfvag2w8jxzzsz9pf8pjfwf0xvln5z7w93yjln3gcnyxsa04jsf2p8vu4sxgppfv0j9qerppqxhvztpqscnjsxvq5gdfy5v6j3wvpjxxqzcerxuglngnfvpxjkgqusct7cyx8zzezcfpqv3nxjxm2kjj4d0zu0ta6fjmpr8a0calk6h88h4ap5e4nucj0ch07aa73qsh3lj5sd89a32kwy0eq7tsa5zqqjpdqvqq5s46r0
```


हमें assetId मिल जाती है, हमें संपत्ति को स्थानांतरित करने के लिए इसकी आवश्यकता होती है।


```
$ rgb0-cli fungible list

- name: USD Tether
id: rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6
ticker: USDT
```


## जीडब्ल्यू-110 जीडब्ल्यू-111 जीडब्ल्यू-112


नया USDT प्राप्त करने के लिए, RGB-node-1 को परिसंपत्ति को धारण करने के लिए received_utxo के अनुरूप generate और blinded UTXO की आवश्यकता होती है।


```
$ rgb1-cli fungible blind e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0

Blinded outpoint: utxob16az597vp5nkr66nfzsykf8ngdnvzep5050rm00l7vv8wm7vew4jqj7jhhf
Outpoint blinding secret: 1679197189805229975
```


इस UTXO से संबंधित स्थानान्तरण स्वीकार करने में सक्षम होने के लिए, हमें मूल received_utxo और blinding_factor की आवश्यकता होगी।


## स्थानांतरण


एसेट की कुछ मात्रा को RGB-node-1 में स्थानांतरित करने के लिए हमें इसे blinded UTXO पर भेजना होगा, RGB-node-0 को Consignment और एक प्रकटीकरण बनाना होगा, और इसे Bitcoin लेनदेन में प्रतिबद्ध करना होगा। फिर हमें PSBT की आवश्यकता होगी जिसे हम प्रतिबद्ध को शामिल करने के लिए संशोधित करेंगे। इसके अलावा, -i और -a विकल्प हमें एक इनपुट आउटपॉइंट प्रदान करने की अनुमति देते हैं जो एसेट का मूल होगा और एक आवंटन जहां हम परिवर्तन प्राप्त करेंगे, हमें इसे निम्नलिखित तरीके से इंगित करना होगा @<change_utxo>.


```
$ rgb0-cli fungible transfer utxob16az597vp5nkr66nfzsykf8ngdnvzep5050rm00l7vv8wm7vew4jqj7jhhf 100 rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6 tx.psbt consignment.rgb disclosure.rgb witness.psbt -i 4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1 -a 900@cd66d3b77dfc1c2ecf958847c16a8a1311bba84ee7bf9dd55592a7b97b13028f:1

Transfer succeeded, consignments and disclosure are written to "consignment.rgb" and "disclosure.rgb", partially signed witness transaction to "witness.psbt"
Consignment data to share:consignment1qxz4g7ec6da33llaxe97u9hx8p9wcgp2yv46ycudwy7ytjf4gdh88x6upcdmjfy3mp4y0n669j5ar5y6e04zfr7255kynff6eymx9tdfc7jux5jk6tgn4xm6lttlh3lh08070ltuh60l07mamlns2qyy984mg4m5dz0x6s5sy5edls2zjlmnvw708sh7fy2vuph745jcpgp92qrw27s73vm4ghrx57vammyf8wautwu5euujd8w3dupdtgp4px36gz8z0ywnuty45uqdwk672qqzjp3j77yl7urft6gewqksqgppczezn5c7gyux6gzgpye0wgyjp85ufdqlzy5cd8zwfg3q9550xq2hyf24qqz92wqskpgq8qsr8kp5p9dt49evmqlze9ylrx2sqpwpvpqp45lpvgjkgk542pks9850w5jquq3qqsj4xsqn9nu6w30lgpmrhdqs6jj0ez3myhj74kp223f0wg2y7vupczdq5pa23mzhzc6l647nl6ftrru0mjrh739yhgztsdhl2cdmhf0qm7du9n20up4rnnsp0tlp8665xldkq9z9u85tgh6nxmkfg3pc6wzk2t90pekj2d6l0km09vyt4vut24vhzg9qhrdsgr7dws828p6ejk7ddy0zkz3a2fq5648664w3se2egwvh904lzmpnc7a7wy4fayznunt6j4ndmm68y24tjje4qxnxs70w4lr9vz9q9qca903edtjd6c5f37jagafsqnhnlsuwvnqwc7uly4dw2rnlyxp4zcfqrfpkpez54c0lc3tmvppmv06ge97heevgt0acrq0ezgjr6ck9waqpanypl8dzrqdzjd05h735tdgv2wjjjucheur40h4wjw4pcdpc8pqlh7ef95rj2al8v3eexkgty8j2ne7kk2zxpe0wypq8ra0x76rt6cu00cw4w05v0u3ng6zhfrttz2c3m5nx64s8w98wa26dx79jwhne44gp9lmg6vkhxq98meslyr4zqtxjsg27xzj80m0csd77lr047vwycvdw0z8mwudm3uvlry9p9da4su72k9q84pphw4n0fyeet0ujzrdgacm6p777jun0y0v397mp4drafr6q7994kdl96m388xp6ggf5arn4d4ed53rv9tlkerckqvkng92uhdvngwcl3m6yqhxdjjnkca62tckxfnrae4cx4e6wx6ww5649v4hvuwkkajanllc38wavqy83xhn555l708354nt2quscchexsxjgezdxfnmxgue0cn4ktghd6xd2le76k5cw3t0p0nurs4h5rjz0j7twj9ulwkp7cmhhgl23r7g677gk36r5jw8panh2sq5966m08sa5632egd5ms6h0e504dtwskct3x6a93uutaumtc8aam8yyt66lrmrhcssw9ga2yg0496s6sdmaexa49064g3syc888egnwa8racrwwwwemknqamarpqlmqa5mg8zgt0dts8ehuwmgz4j3cjltr8gv78e7p84zm8pylann7dmss5suf4htqc04qx5trnk59m305ah2qp4mvkxwy6ts84sa30d80jzk9s6n40e4j8dcvq79ncg5e3z5g4esxyawmxk7lvm5efc30vtw8qqhe9xx3773djez6hjjx0x962z2radnvdmazkrmlqw7guxz29qvahcx79h33ncqhzhvekwaqqnrz3wxnp2qy3u83zdgdcgq27n5n22h7jjedrh28m8c6mn42xhfjasm5njsxtufqjxefnhc2n5zr0um0xlqk62cu25cjwuwwrcv3e4vhh2tdzn8rnlaefj98fvslg7sun95wpt2a4vcg4ua62v97aeqstvjegmlem5crnsamrhm3a2pcma2s22atr43lgx9vh7kn9lzymfe83a4vhe9rc6xl5pmy5hjw4t88k0fwh6lzmjtjvqtczq47ny7hv8ytdqdy2c7ce3gegnufkzwphkwtz6xqzklyw7e7f76fwfewfuyqal7dl8r9476jerrl40mav38sun2u8jvftw33x3r20dmeka34znmkgaz29ppk5hz3ldttw8zyz4k6q0gts8utqh53tuc7vtajl26rq2fnxr0vxcwlx9rfvn6v8ar8c73qkc3zca4mlgl7qu36sk7e
```


इससे तीन नई फाइलें लिखी जाएंगी, Consignment, डिस्क्लोजर और PSBT जिसमें ट्वीक भी शामिल है, इस PSBT को Witness Transaction कहा जाता है, Consignment को RGB-नोड-1 पर भेजा जाता है।


## गवाह


Witness Transaction को हस्ताक्षरित और प्रसारित किया जाना चाहिए, इसके लिए हमें इसे वापस बेस64 एनकोड करना होगा।


```
$ base64 -w0 witness.psbt

cHNidP8BAHECAAAAAe2pydT0BqfK5nBCdBSbm3W/vNKE/QxTr4eJcjwjDLDjAQAAAAD/////AiWbAAAAAAAAFgAUO1Bi4v2VHUJPmq5iyYhDv1tyTCcQJwAAAAAAABYAFPwfm3skdSeMnOfcDqBpgVjwuwESAAAAAAABAHECAAAAAeSwUiZ+p3/NM7yt3BAoDkm/afi//lplsffwwpTqjd+CAQAAAAD/////AlDDAAAAAAAAFgAULga5BeTQ1vfiqcD3zuxk+K2O/wbDwgAAAAAAABYAFLsvLLowx0NR5NyFKj9wl3IFvNcPAAAAAAEBH8PCAAAAAAAAFgAUuy8sujDHQ1Hk3IUqP3CXcgW81w8iBgKIYFEbYKvRj25inaA0/c0PMIZD/BFAgFbjrBJe8cZ+cxDskk+CAAAAgAEAAIADAACAACICAsnwAXsMVlPXi/2ExgqtLoIN4TncWVW0EImSo9YwyhNmEOyST4IAAACAAQAAgAUAAIAG/ANSR0IBIQLJ8AF7DFZT14v9hMYKrS6CDeE53FlVtBCJkqPWMMoTZgb8A1JHQgIgMD8j8bQGB8NgEobv3NUJr7aERA/FkGgQ5w2KwF+daDgAAA==
```


इसे walletprocesspsbt उपकमांड के साथ हस्ताक्षरित करें।


```
$ bcli walletprocesspsbt "cHNidP8BAHECAAAAAe2pydT0BqfK5nBCdBSbm3W/vNKE/QxTr4eJcjwjDLDjAQAAAAD/////AiWbAAAAAAAAFgAUO1Bi4v2VHUJPmq5iyYhDv1tyTCcQJwAAAAAAABYAFPwfm3skdSeMnOfcDqBpgVjwuwESAAAAAAABAHECAAAAAeSwUiZ+p3/NM7yt3BAoDkm/afi//lplsffwwpTqjd+CAQAAAAD/////AlDDAAAAAAAAFgAULga5BeTQ1vfiqcD3zuxk+K2O/wbDwgAAAAAAABYAFLsvLLowx0NR5NyFKj9wl3IFvNcPAAAAAAEBH8PCAAAAAAAAFgAUuy8sujDHQ1Hk3IUqP3CXcgW81w8iBgKIYFEbYKvRj25inaA0/c0PMIZD/BFAgFbjrBJe8cZ+cxDskk+CAAAAgAEAAIADAACAACICAsnwAXsMVlPXi/2ExgqtLoIN4TncWVW0EImSo9YwyhNmEOyST4IAAACAAQAAgAUAAIAG/ANSR0IBIQLJ8AF7DFZT14v9hMYKrS6CDeE53FlVtBCJkqPWMMoTZgb8A1JHQgIgMD8j8bQGB8NgEobv3NUJr7aERA/FkGgQ5w2KwF+daDgAAA=="
{
"psbt": "cHNidP8BAHECAAAAAe2pydT0BqfK5nBCdBSbm3W/vNKE/QxTr4eJcjwjDLDjAQAAAAD/////AiWbAAAAAAAAFgAUO1Bi4v2VHUJPmq5iyYhDv1tyTCcQJwAAAAAAABYAFPwfm3skdSeMnOfcDqBpgVjwuwESAAAAAAABAHECAAAAAeSwUiZ+p3/NM7yt3BAoDkm/afi//lplsffwwpTqjd+CAQAAAAD/////AlDDAAAAAAAAFgAULga5BeTQ1vfiqcD3zuxk+K2O/wbDwgAAAAAAABYAFLsvLLowx0NR5NyFKj9wl3IFvNcPAAAAAAEBH8PCAAAAAAAAFgAUuy8sujDHQ1Hk3IUqP3CXcgW81w8BCGsCRzBEAiAZud+YVf1FyZq0IDQ+/oAE34TKypedrJGUcYx0QIpaygIgZJO7xvN0dOQXbXTRYE0QxGIWsfo85Dhwne0/whoO06kBIQKIYFEbYKvRj25inaA0/c0PMIZD/BFAgFbjrBJe8cZ+cwAiAgLJ8AF7DFZT14v9hMYKrS6CDeE53FlVtBCJkqPWMMoTZhDskk+CAAAAgAEAAIAFAACABvwDUkdCASECyfABewxWU9eL/YTGCq0ugg3hOdxZVbQQiZKj1jDKE2YG/ANSR0ICIDA/I/G0BgfDYBKG79zVCa+2hEQPxZBoEOcNisBfnWg4AAA=",
"complete": true
}
```


अब इसे अंतिम रूप दें और हेक्स प्राप्त करें।


```
$ bcli finalizepsbt "cHNidP8BAHECAAAAAe2pydT0BqfK5nBCdBSbm3W/vNKE/QxTr4eJcjwjDLDjAQAAAAD/////AiWbAAAAAAAAFgAUO1Bi4v2VHUJPmq5iyYhDv1tyTCcQJwAAAAAAABYAFPwfm3skdSeMnOfcDqBpgVjwuwESAAAAAAABAHECAAAAAeSwUiZ+p3/NM7yt3BAoDkm/afi//lplsffwwpTqjd+CAQAAAAD/////AlDDAAAAAAAAFgAULga5BeTQ1vfiqcD3zuxk+K2O/wbDwgAAAAAAABYAFLsvLLowx0NR5NyFKj9wl3IFvNcPAAAAAAEBH8PCAAAAAAAAFgAUuy8sujDHQ1Hk3IUqP3CXcgW81w8BCGsCRzBEAiAZud+YVf1FyZq0IDQ+/oAE34TKypedrJGUcYx0QIpaygIgZJO7xvN0dOQXbXTRYE0QxGIWsfo85Dhwne0/whoO06kBIQKIYFEbYKvRj25inaA0/c0PMIZD/BFAgFbjrBJe8cZ+cwAiAgLJ8AF7DFZT14v9hMYKrS6CDeE53FlVtBCJkqPWMMoTZhDskk+CAAAAgAEAAIAFAACABvwDUkdCASECyfABewxWU9eL/YTGCq0ugg3hOdxZVbQQiZKj1jDKE2YG/ANSR0ICIDA/I/G0BgfDYBKG79zVCa+2hEQPxZBoEOcNisBfnWg4AAA="
{
"hex": "02000000000101eda9c9d4f406a7cae6704274149b9b75bfbcd284fd0c53af8789723c230cb0e30100000000ffffffff02259b0000000000001600143b5062e2fd951d424f9aae62c98843bf5b724c271027000000000000160014fc1f9b7b2475278c9ce7dc0ea0698158f0bb011202473044022019b9df9855fd45c99ab420343efe8004df84caca979dac9194718c74408a5aca02206493bbc6f37474e4176d74d1604d10c46216b1fa3ce438709ded3fc21a0ed3a90121028860511b60abd18f6e629da034fdcd0f308643fc11408056e3ac125ef1c67e7300000000",
"complete": true
}
```


## प्रसारण


इसे Blockchain में पुष्टि करने के लिए sendrawtransaction उपकमांड का उपयोग करके प्रसारित करें।


```
$ bcli sendrawtransaction "02000000000101eda9c9d4f406a7cae6704274149b9b75bfbcd284fd0c53af8789723c230cb0e30100000000ffffffff02259b0000000000001600143b5062e2fd951d424f9aae62c98843bf5b724c271027000000000000160014fc1f9b7b2475278c9ce7dc0ea0698158f0bb011202473044022019b9df9855fd45c99ab420343efe8004df84caca979dac9194718c74408a5aca02206493bbc6f37474e4176d74d1604d10c46216b1fa3ce438709ded3fc21a0ed3a90121028860511b60abd18f6e629da034fdcd0f308643fc11408056e3ac125ef1c67e7300000000"
8e3787fe40b5feb3044f892e739bdb4043e10de384255a915a37725811abc3fe
```


## स्वीकार करना


आने वाले स्थानांतरण को स्वीकार करने के लिए RGB-node-1 को RGB-node-0 से Consignment फ़ाइल प्राप्त करनी चाहिए, UTXO पीढ़ी को ब्लाइंड करने के दौरान received_utxo और संबंधित blinding_factor उत्पन्न होना चाहिए।


```
$ rgb1-cli fungible accept consignment.rgb e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0 1679197189805229975

Asset transfer successfully accepted.
```


अब हम (knownAllocations फ़ील्ड में) <receive_utxo> में 100 परिसंपत्ति इकाइयों का नया आवंटन देख सकते हैं:


```
$ rgb1-cli fungible list -l

- genesis: genesis1qyfe883hey6jrgj2xvk5g3dfmfqfzm7a4wez4pd2krf7ltsxffd6u6nrvjvvnc8vt9llmp7663pgututl9heuwaudet72ay9j6thc6cetuvhxvsqqya5xjt2w9y4u6sfkuszwwctnrpug5yjxnthmr3mydg05rdrpspcxysnqvvqpfvag2w8jxzzsz9pf8pjfwf0xvln5z7w93yjln3gcnyxsa04jsf2p8vu4sxgppfv0j9qerppqxhvztpqscnjsxvq5gdfy5v6j3wvpjxxqzcerxuglngnfvpxjkgqusct7cyx8zzezcfpqv3nxjxm2kjj4d0zu0ta6fjmpr8a0calk6h88h4ap5e4nucj0ch07aa73qsh3lj5sd89a32kwy0eq7tsa5zqqjpdqvqq5s46r0
id: rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6
ticker: USDT
name: USD Tether
description: ~
knownCirculating: 1000
isIssuedKnown: ~
issueLimit: 0
chain: testnet
decimalPrecision: 0
date: "2022-02-23T20:53:26"
knownIssues:
- id: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
amount: 1000
origin: ~
knownInflation: {}
knownAllocations:
- nodeId: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
index: 0
outpoint: "4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1"
revealedAmount:
value: 1000
blinding: "0000000000000000000000000000000000000000000000000000000000000001"
- nodeId: 28f82e2dcfa91282c28a8805ff0c7fde4bd4e0bdbd40c6ba55e191666e45327b
index: 1
outpoint: "e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0"
revealedAmount:
value: 100
blinding: 224561f10229eb9ebbdf05f497132d2b8344d70971c80510eddc607d615ee2a0
```


चूंकि स्थानांतरण के समय get_utxo blinded था, इसलिए भुगतानकर्ता RGB-node-0 को इस बारे में कोई जानकारी नहीं है कि 100 USDT कहां भेजा गया था, इसलिए स्थान knownAllocations में नहीं दिखाया गया है।


```
$ rgb0-cli fungible list -l

- genesis: genesis1qyfe883hey6jrgj2xvk5g3dfmfqfzm7a4wez4pd2krf7ltsxffd6u6nrvjvvnc8vt9llmp7663pgututl9heuwaudet72ay9j6thc6cetuvhxvsqqya5xjt2w9y4u6sfkuszwwctnrpug5yjxnthmr3mydg05rdrpspcxysnqvvqpfvag2w8jxzzsz9pf8pjfwf0xvln5z7w93yjln3gcnyxsa04jsf2p8vu4sxgppfv0j9qerppqxhvztpqscnjsxvq5gdfy5v6j3wvpjxxqzcerxuglngnfvpxjkgqusct7cyx8zzezcfpqv3nxjxm2kjj4d0zu0ta6fjmpr8a0calk6h88h4ap5e4nucj0ch07aa73qsh3lj5sd89a32kwy0eq7tsa5zqqjpdqvqq5s46r0
id: rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6
ticker: USDT
name: USD Tether
description: ~
knownCirculating: 1000
isIssuedKnown: ~
issueLimit: 0
chain: testnet
decimalPrecision: 0
date: "2022-02-23T20:53:26"
knownIssues:
- id: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
amount: 1000
origin: ~
knownInflation: {}
knownAllocations:
- nodeId: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
index: 0
outpoint: "4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1"
revealedAmount:
value: 1000
blinding: "0000000000000000000000000000000000000000000000000000000000000001"
```


लेकिन जैसा कि आप देख सकते हैं कि RGB-node-0 900 एसेट परिवर्तन को नहीं देख सकता है जिसे हमने -a तर्क के साथ ट्रांसफर कमांड में दिया था। परिवर्तन को पंजीकृत करने के लिए RGB-node-0 को प्रकटीकरण को स्वीकार करने की आवश्यकता है।


```
$ rgb0-cli fungible enclose disclosure.rgb

Disclosure data successfully enclosed.
```


यदि RGB-node-0 सफल रहा तो आप परिसंपत्ति को सूचीबद्ध करके परिवर्तन देख सकते हैं।


```
$ rgb0-cli fungible list -l

- genesis: genesis1qyfe883hey6jrgj2xvk5g3dfmfqfzm7a4wez4pd2krf7ltsxffd6u6nrvjvvnc8vt9llmp7663pgututl9heuwaudet72ay9j6thc6cetuvhxvsqqya5xjt2w9y4u6sfkuszwwctnrpug5yjxnthmr3mydg05rdrpspcxysnqvvqpfvag2w8jxzzsz9pf8pjfwf0xvln5z7w93yjln3gcnyxsa04jsf2p8vu4sxgppfv0j9qerppqxhvztpqscnjsxvq5gdfy5v6j3wvpjxxqzcerxuglngnfvpxjkgqusct7cyx8zzezcfpqv3nxjxm2kjj4d0zu0ta6fjmpr8a0calk6h88h4ap5e4nucj0ch07aa73qsh3lj5sd89a32kwy0eq7tsa5zqqjpdqvqq5s46r0
id: rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6
ticker: USDT
name: USD Tether
description: ~
knownCirculating: 1000
isIssuedKnown: ~
issueLimit: 0
chain: testnet
decimalPrecision: 0
date: "2022-02-23T20:53:26"
knownIssues:
- id: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
amount: 1000
origin: ~
knownInflation: {}
knownAllocations:
- nodeId: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
index: 0
outpoint: "4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1"
revealedAmount:
value: 1000
blinding: "0000000000000000000000000000000000000000000000000000000000000001"
- nodeId: 28f82e2dcfa91282c28a8805ff0c7fde4bd4e0bdbd40c6ba55e191666e45327b
index: 0
outpoint: "cd66d3b77dfc1c2ecf958847c16a8a1311bba84ee7bf9dd55592a7b97b13028f:1"
revealedAmount:
value: 900
blinding: ddba9e0efdd614614420fa0b68ecd2d3376a05dd3d809b2ad1f5fe0f6ed75ea2
```


## निष्कर्ष


हम एक परिवर्तनीय परिसंपत्ति बनाने और इसे एक लेनदेन से दूसरे लेनदेन में निजी तरीके से स्थानांतरित करने में सक्षम हैं, अगर हम Block explorer में पुष्टि किए गए लेनदेन की जांच करते हैं तो हमें नियमित लेनदेन से कुछ भी अलग नहीं मिलेगा, यह इस तथ्य के कारण है कि RGB लेनदेन को बदलने के लिए एकल-उपयोग मुहरों का उपयोग करता है, इस पोस्ट में, मैं एक परिचय देता हूं कि RGB कैसे काम करता है।


इस पोस्ट में कुछ बग हो सकते हैं, अगर आपको कुछ मिलता है तो कृपया मुझे बताएं ताकि इस गाइड को बेहतर बनाया जा सके, सुझाव और आलोचनाओं का भी स्वागत है, हैप्पी हैकिंग! 🖖