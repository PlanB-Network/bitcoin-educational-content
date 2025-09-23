---
name: RGB Lightning Node
description: मैं RLN के साथ RGB-संगत लाइटनिंग नोड कैसे लॉन्च करूं?
---
![cover](assets/cover.webp)


इस चरण-दर-चरण ट्यूटोरियल में, आप सीखेंगे कि Regtest वातावरण पर लाइटनिंग RGB नोड कैसे सेट करें। हम देखेंगे कि RGB टोकन कैसे बनाएं और उन्हें चैनलों में कैसे प्रसारित करें।


## आरएलएन परियोजना


बिटफ़ाइनेक्स की RGB टीम 2022 से एक संपूर्ण प्रौद्योगिकी स्टैक विकसित करके RGB पारिस्थितिकी तंत्र को समृद्ध करने के लिए काम कर रही है। किसी एकल वाणिज्यिक उत्पाद के लक्ष्य के बजाय, इसके प्रयास ओपन-सोर्स सॉफ़्टवेयर ब्रिक उपलब्ध कराने, RGB प्रोटोकॉल विनिर्देशों में योगदान देने और कार्यान्वयन संदर्भ बनाने पर केंद्रित हैं।


RGB पारिस्थितिकी तंत्र में बिटफिनेक्स के उल्लेखनीय योगदानों में से एक है [*RGBlib* लाइब्रेरी](https://github.com/RGB-Tools/RGB-lib), जिसे Rust में लिखा गया है और कोटलिन और पायथन में बाइंडिंग के माध्यम से सुलभ है, जो जटिल सत्यापन और जुड़ाव तंत्रों को समाहित करके RGB अनुप्रयोगों के विकास को बहुत सरल बनाता है।


बिटफिनेक्स टीम ने एक RGB मोबाइल Wallet भी डिज़ाइन किया है, जिसे "[*Iris Wallet*](https://iriswallet.com/)" कहा जाता है, जो Android पर उपलब्ध है। यह Wallet RGB प्रॉक्सी सर्वर के उपयोग को एकीकृत करता है ताकि RGB पर *Client-side Validation* के लिए off-chain डेटा एक्सचेंज (*कंसाइनमेंट*) को आसानी से प्रबंधित किया जा सके।


बिटफिनेक्स ने `RGB-lightning-node` (RLN) प्रोजेक्ट भी विकसित किया है। यह `Rust-lightning` (LDK) के Fork पर आधारित Rust daemon है, जिसे चैनल में RGB संपत्तियों के अस्तित्व को ध्यान में रखते हुए संशोधित किया गया है। जब कोई चैनल खोला जाता है, तो RGB टोकन की उपस्थिति निर्दिष्ट की जा सकती है, और हर बार जब चैनल की स्थिति अपडेट की जाती है, तो एक State Transition बनाया जाता है जो लाइटनिंग आउटपुट में टोकन के वितरण को दर्शाता है। यह सक्षम बनाता है:




- उदाहरण के लिए, USDT में लाइटनिंग चैनल खोलें;
- इन टोकन को नेटवर्क के माध्यम से रूट करें, बशर्ते रूटिंग पथ में पर्याप्त तरलता हो;
- बिना किसी संशोधन के लाइटनिंग की सजा और टाइमलॉक तर्क का फायदा उठाएं: बस Anchor को Commitment Transaction के अतिरिक्त आउटपुट में RGB संक्रमण में बदलें।


आरएलएन कोड अभी भी अपने अल्फा चरण में है: हम इसे केवल **रेगटेस्ट** या **Testnet** पर उपयोग करने की अनुशंसा करते हैं।


## RGB प्रोटोकॉल अनुस्मारक


RGB एक प्रोटोकॉल है जो Bitcoin के शीर्ष पर चलता है और Smart contract कार्यक्षमता और डिजिटल एसेट प्रबंधन का अनुकरण करता है, बिना Blockchain को ओवरलोड किए जिस पर यह आधारित है। पारंपरिक On-Chain स्मार्ट कॉन्ट्रैक्ट्स (जैसे कि एथेरियम पर, उदाहरण के लिए) के विपरीत, RGB एक "*Client-side Validation*" सिस्टम पर निर्भर करता है: अधिकांश डेटा और स्थिति इतिहास का आदान-प्रदान और भंडारण विशेष रूप से शामिल प्रतिभागियों द्वारा किया जाता है, जबकि Bitcoin Blockchain केवल छोटी क्रिप्टोग्राफ़िक प्रतिबद्धताओं (जैसे *टैप्रेट* या *ओप्रेट* जैसे तंत्रों के माध्यम से) को होस्ट करता है। RGB प्रोटोकॉल में, Bitcoin Blockchain इसलिए केवल टाइम-स्टैम्पिंग सर्वर और Double-spending सुरक्षा प्रणाली के रूप में कार्य करता है।


RGB Contract को एक विकासवादी राज्य मशीन की तरह संरचित किया गया है। यह एक Genesis से शुरू होता है जो एक सख्त टाइप और संकलित Schema के अनुसार प्रारंभिक स्थिति (उदाहरण के लिए, Supply, टिकर या अन्य मेटाडेटा का वर्णन) को परिभाषित करता है। राज्य संक्रमण और, यदि आवश्यक हो, तो राज्य विस्तार को इस स्थिति को संशोधित या विस्तारित करने के लिए लागू किया जाता है। प्रत्येक ऑपरेशन, चाहे वह फ़ंजिबल एसेट्स (RGB20) को स्थानांतरित करना हो या अद्वितीय एसेट्स (RGB21) बनाना हो, इसमें *सिंगल-यूज़ सील* शामिल हैं। ये Bitcoin UTXO को off-chain राज्यों से जोड़ते हैं और गोपनीयता और मापनीयता सुनिश्चित करते हुए दोहरे खर्च को रोकते हैं।


RGB प्रोटोकॉल कैसे काम करता है, इसके बारे में अधिक जानने के लिए, मैं आपको यह व्यापक प्रशिक्षण पाठ्यक्रम लेने की सलाह देता हूं:


https://planb.network/courses/3ce1d37c-05ba-4f54-aa15-7586d37b2bb7

## RGB-संगत लाइटनिंग नोड स्थापना


`RGB-lightning-node` बाइनरी को संकलित और स्थापित करने के लिए, हम रिपोजिटरी और उसके उप-मॉड्यूल को क्लोन करके शुरू करते हैं, फिर हम चलाते हैं:


```bash
git clone https://github.com/RGB-Tools/rgb-lightning-node --recurse-submodules --shallow-submodules
```


![RLN](assets/fr/01.webp)




- `--recurse-submodules` विकल्प आवश्यक उप-उपकरणों (`Rust-lightning` के संशोधित संस्करण सहित) का क्लोन भी बनाता है;
- `--shallow-submodules` विकल्प डाउनलोडिंग की गति बढ़ाने के लिए क्लोन की गहराई को सीमित करता है, जबकि आवश्यक कमिट्स तक पहुंच प्रदान करता है।


प्रोजेक्ट रूट से, बाइनरी को संकलित और स्थापित करने के लिए निम्नलिखित कमांड चलाएँ:


```bash
cargo install --locked --debug --path .
```


![RLN](assets/fr/02.webp)




- `--locked` यह सुनिश्चित करता है कि निर्भरताओं के संस्करण का सम्मान किया जाता है;
- `--debug` अनिवार्य नहीं है, लेकिन यह आपको ध्यान केंद्रित करने में मदद कर सकता है (यदि आप चाहें तो `--release` का उपयोग कर सकते हैं) ;
- `--path .` `cargo install` को वर्तमान निर्देशिका से इंस्टॉल करने के लिए कहता है।


इस कमांड के अंत में, आपके `$CARGO_HOME/bin/` में एक `RGB-lightning-node` निष्पादन योग्य उपलब्ध होगा। सुनिश्चित करें कि यह पथ आपके `$PATH` में है ताकि आप किसी भी निर्देशिका से कमांड को लागू कर सकें।


## आवश्यक शर्तें


कार्य करने के लिए, `RGB-lightning-node` daemon को निम्नलिखित की उपस्थिति और विन्यास की आवश्यकता है:




- एक **`bitcoind`** नोड


प्रत्येक RLN इंस्टेंस को अपने On-Chain लेनदेन को प्रसारित करने और निगरानी करने के लिए `bitcoind` के साथ संचार करने की आवश्यकता होगी। प्रमाणीकरण (लॉगिन/पासवर्ड) और URL (होस्ट/पोर्ट) daemon को प्रदान करने की आवश्यकता होगी।




- एक **इंडेक्सर** (इलेक्ट्रम या एस्पलोरा)


daemon को On-Chain लेनदेन को सूचीबद्ध करने और एक्सप्लोर करने में सक्षम होना चाहिए, विशेष रूप से उस UTXO को खोजने के लिए जिस पर किसी परिसंपत्ति को लंगर डाला गया है। आपको अपने इलेक्ट्रम सर्वर या एस्प्लोरा का URL निर्दिष्ट करना होगा।




- एक **RGB** प्रॉक्सी


प्रॉक्सी सर्वर एक घटक है (वैकल्पिक, लेकिन अत्यधिक अनुशंसित) जो लाइटनिंग पीयर के बीच Exchange या RGB *कंसाइनमेंट* को सरल बनाता है। एक बार फिर, एक URL निर्दिष्ट किया जाना चाहिए।


जब daemon को API के माध्यम से *अनलॉक* किया जाता है, तो आईडी और URL दर्ज किए जाते हैं।


## रेगटेस्ट लॉन्च


सरल उपयोग के लिए, एक `regtest.sh` स्क्रिप्ट है जो स्वचालित रूप से Docker के माध्यम से सेवाओं का एक सेट शुरू करती है: `bitcoind`, `electrs` (इंडेक्सर), `RGB-proxy-server`।


![RLN](assets/fr/03.webp)


यह आपको एक स्थानीय, पृथक, पूर्व-कॉन्फ़िगर किए गए वातावरण को लॉन्च करने की अनुमति देता है। यह प्रत्येक रीबूट पर कंटेनर और डेटा निर्देशिकाएँ बनाता और नष्ट करता है। हम इसे शुरू करके शुरू करेंगे:


```bash
./regtest.sh start
```


यह स्क्रिप्ट:




- संग्रहीत करने के लिए एक `docker/` निर्देशिका बनाएँ;
- regtest में `bitcoind` चलाएँ, साथ ही इंडेक्सर `eletrs` और `RGB-proxy-server` भी चलाएँ;
- तब तक प्रतीक्षा करें जब तक सब कुछ उपयोग के लिए तैयार न हो जाए।


![RLN](assets/fr/04.webp)


इसके बाद, हम कई RLN नोड्स लॉन्च करेंगे। अलग-अलग शेल में, उदाहरण के लिए, चलाएँ (3 RLN नोड्स लॉन्च करने के लिए):


```bash
# 1st shell
rgb-lightning-node dataldk0/ --daemon-listening-port 3001 \
--ldk-peer-listening-port 9735 --network regtest
# 2nd shell
rgb-lightning-node dataldk1/ --daemon-listening-port 3002 \
--ldk-peer-listening-port 9736 --network regtest
# 3rd shell
rgb-lightning-node dataldk2/ --daemon-listening-port 3003 \
--ldk-peer-listening-port 9737 --network regtest
```


![RLN](assets/fr/05.webp)




- `--network regtest` पैरामीटर regtest कॉन्फ़िगरेशन के उपयोग को इंगित करता है;
- `--daemon-listening-port` इंगित करता है कि लाइटनिंग नोड किस REST पोर्ट पर API कॉल (JSON) सुनेगा;
- `--ldk-peer-listening-port` निर्दिष्ट करता है कि किस लाइटनिंग P2P पोर्ट पर सुनना है;
- `dataldk0/`, `dataldk1/` भंडारण निर्देशिकाओं के पथ हैं (प्रत्येक नोड अपनी जानकारी अलग से संग्रहीत करता है)।


अब आप अपने ब्राउज़र से अपने RLN नोड्स पर कमांड निष्पादित कर सकते हैं, API की बदौलत। विशेष रूप से, यह वह जगह है जहाँ आप डेमॉन को *अनलॉक* कर सकते हैं। बस अपने नोड्स के समान कंप्यूटर पर एक ब्राउज़र खोलें, और URL दर्ज करें:


```url
https://rgb-tools.github.io/rgb-lightning-node/
```


किसी नोड को चैनल खोलने के लिए, सबसे पहले उसके पास Address पर बिटकॉइन होना चाहिए, जो निम्न कमांड द्वारा उत्पन्न किया गया हो (उदाहरण के लिए, नोड n°1 के लिए):


```bash
curl -X POST http://localhost:3001/address
```


इसका उत्तर आपको Address प्रदान करेगा।


![RLN](assets/fr/06.webp)


`bitcoind` रेगटेस्ट पर, हम कुछ बिटकॉइन माइन करने जा रहे हैं। चलाएँ :


```bash
./regtest.sh mine 101
```


![RLN](assets/fr/07.webp)


ऊपर उत्पन्न नोड Address पर धनराशि भेजें:


```bash
./regtest.sh sendtoaddress <address> <amount>
```


![RLN](assets/fr/08.webp)


फिर लेनदेन की पुष्टि करने के लिए एक ब्लॉक माइन करें:


```bash
./regtest.sh mine 1
```


![RLN](assets/fr/09.webp)


## Testnet का प्रक्षेपण (डॉकर के बिना)


यदि आप अधिक यथार्थवादी परिदृश्य का परीक्षण करना चाहते हैं, तो आप Regtest के बजाय Testnet पर RLN नोड्स लॉन्च कर सकते हैं, जो सार्वजनिक सेवाओं या आपके द्वारा नियंत्रित सेवाओं की ओर इशारा करते हैं:


```bash
rgb-lightning-node dataldk0/ --daemon-listening-port 3001 \
--ldk-peer-listening-port 9735 --network testnet
rgb-lightning-node dataldk1/ --daemon-listening-port 3002 \
--ldk-peer-listening-port 9736 --network testnet
rgb-lightning-node dataldk2/ --daemon-listening-port 3003 \
--ldk-peer-listening-port 9737 --network testnet
```


डिफ़ॉल्ट रूप से, यदि कोई कॉन्फ़िगरेशन नहीं मिलता है, तो daemon इसका उपयोग करने का प्रयास करेगा:




- `bitcoind_rpc_host`: `electrum.iriswallet.com`
- `bitcoind_rpc_port`: `18332`
- indexer_url`: `ssl://electrum.iriswallet.com:50013`
- `प्रॉक्सी_एंडपॉइंट`: `rpcs://proxy.iriswallet.com/0.2/json-RPC`


लॉगिन के साथ:




- `bitcoind_rpc_username`: `उपयोगकर्ता`
- `bitcoind_rpc_username`: `पासवर्ड`


आप इन Elements को `init`/`unlock` API के माध्यम से भी अनुकूलित कर सकते हैं।


## RGB टोकन जारी करना


टोकन जारी करने के लिए, हम "रंगीन" UTXOs बनाकर शुरुआत करेंगे:


```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"up_to": false,
"num": 4,
"size": 2000000,
"fee_rate": 4.2,
"skip_sync": false
}' \
http://localhost:3001/createutxos
```


![RLN](assets/fr/10.webp)


आप निश्चित रूप से ऑर्डर को अनुकूलित कर सकते हैं। लेनदेन की पुष्टि करने के लिए, हम एक माइन करते हैं:


```bash
./regtest.sh mine 1
```


अब हम एक RGB एसेट बना सकते हैं। कमांड उस एसेट के प्रकार पर निर्भर करेगा जिसे आप बनाना चाहते हैं और उसके पैरामीटर। यहाँ मैं 1000 इकाइयों के Supply के साथ "PBN" नामक एक NIA (*नॉन इन्फ्लेटेबल एसेट*) टोकन बना रहा हूँ। `परिशुद्धता` आपको इकाइयों की विभाज्यता को परिभाषित करने की अनुमति देता है।


```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"amounts": [
1000
],
"ticker": "PBN",
"name": "Plan B Network",
"precision": 0
}' \
http://localhost:3001/issueassetnia
```


![RLN](assets/fr/11.webp)


प्रतिक्रिया में नई बनाई गई संपत्ति की आईडी शामिल है। इस पहचानकर्ता को नोट करना याद रखें। मेरे मामले में, यह है:


```txt
rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10
```


![RLN](assets/fr/12.webp)


फिर आप इसे On-Chain में ट्रांसफर कर सकते हैं, या इसे लाइटनिंग चैनल में आवंटित कर सकते हैं। अगले सेक्शन में हम यही करने जा रहे हैं।


## चैनल खोलना और RGB परिसंपत्ति स्थानांतरित करना


आपको सबसे पहले `/connectpeer` कमांड का उपयोग करके अपने नोड को Lightning Network पर एक पीयर से कनेक्ट करना होगा। मेरे उदाहरण में, मैं दोनों नोड्स को नियंत्रित करता हूँ। इसलिए मैं इस कमांड के साथ अपने दूसरे लाइटनिंग नोड की सार्वजनिक कुंजी प्राप्त करूँगा:


```bash
curl -X 'GET' \
'http://localhost:3002/nodeinfo' \
-H 'accept: application/json'
```


कमांड मेरे नोड n°2 की सार्वजनिक कुंजी लौटाता है:


```txt
031e81e4c5c6b6a50cbf5d85b15dad720fec92c62e84bafb34088f0488e00a8e94
```


![RLN](assets/fr/13.webp)


इसके बाद, हम संबंधित एसेट (`PBN`) निर्दिष्ट करके चैनल खोलेंगे। `/openchannel` कमांड आपको चैनल का आकार सातोशी में परिभाषित करने और RGB एसेट को शामिल करने का विकल्प चुनने देता है। यह इस बात पर निर्भर करता है कि आप क्या बनाना चाहते हैं, लेकिन मेरे मामले में, कमांड है:


```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"peer_pubkey_and_opt_addr": "031e81e4c5c6b6a50cbf5d85b15dad720fec92c62e84bafb34088f0488e00a8e94@localhost:9736",
"capacity_sat": 1000000,
"push_msat": 10000000,
"asset_amount": 500,
"asset_id": "rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10",
"public": true,
"with_anchors": true,
"fee_base_msat": 1000,
"fee_proportional_millionths": 0,
"temporary_channel_id": "a8b60c8ce3067b5fc881d4831323e24751daec3b64353c8df3205ec5d838f1c5"
}' \
http://localhost:3001/openchannel
```


यहां अधिक जानकारी प्राप्त करें:




- `peer_pubkey_and_opt_addr`: उस पीयर का पहचानकर्ता जिससे हम जुड़ना चाहते हैं (सार्वजनिक कुंजी जो हमें पहले मिली थी);
- `capacity_sat`: कुल चैनल क्षमता सतोशी में;
- `push_msat`: चैनल खुलने पर प्रारंभ में सहकर्मी को हस्तांतरित की गई मिलीसाटोशी में राशि (यहां मैं तुरंत 10,000 Sats हस्तांतरित करता हूं ताकि वह बाद में RGB हस्तांतरित कर सके) ;
- `asset_amount`: चैनल के लिए प्रतिबद्ध की जाने वाली RGB परिसंपत्तियों की राशि;
- `asset_id` : चैनल में लगे RGB परिसंपत्ति का विशिष्ट पहचानकर्ता;
- `public`: यह इंगित करता है कि क्या चैनल को नेटवर्क पर रूटिंग के लिए सार्वजनिक किया जाना चाहिए।


![RLN](assets/fr/14.webp)


लेनदेन की पुष्टि के लिए, 6 ब्लॉकों का खनन किया जाता है:


```bash
./regtest.sh mine 6
```


![RLN](assets/fr/15.webp)


लाइटनिंग चैनल अब खुला है और इसमें नोड n°1 की तरफ़ 500 `PBN` टोकन भी हैं। यदि नोड n°2 `PBN` टोकन प्राप्त करना चाहता है, तो उसे generate या Invoice करना होगा। इसे करने का तरीका यहां बताया गया है:


```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"amt_msat": 3000000,
"expiry_sec": 420,
"asset_id": "rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10",
"asset_amount": 100
}' \
http://localhost:3002/lninvoice
```


साथ :




- `amt_msat`: मिलीसाटोशी में Invoice मात्रा (न्यूनतम 3000 Sats) ;
- `expiry_sec` : सेकंड में Invoice समाप्ति समय;
- `asset_id` : Invoice से संबद्ध RGB परिसंपत्ति का पहचानकर्ता;
- `asset_amount`: इस Invoice के साथ स्थानांतरित की जाने वाली RGB परिसंपत्ति की राशि।


जवाब में, आपको RGB Invoice मिलेगा:


```txt
lnbcrt30u1pncgd4rdqud3jxktt5w46x7unfv9kz6mn0v3jsnp4qv0grex9c6m22r9ltkzmzhddwg87eykx96zt47e5pz8sfz8qp28fgpp5jksvqtleryhvwr299qdz96qxzm24augy5agkdhltudk463lt9dassp5d6n0sqgl0c4gx52fdmutrdtqamt0y4xuz2rcgel4hpjwne08gmls9qyysgqcqpcxqzdylz5wfnkywnxvvmkvnt2x4fj6wre0gshvjtv95ervvzzg4592t2gdgchx6mkf5k45jrrdfn8j73d2f2xx4mrxycq7qzry4v4jan6uxhhacyqa4gn6plggwpq9j74tu74f2zsamtz6ymt600p8su4c4ap9g9d8ku2x3wdh6fuc8fd8pff2yzpjrf24ys3cltca9fgqut6gzj
```


![RLN](assets/fr/16.webp)


अब हम इस Invoice का भुगतान पहले नोड से करेंगे, जिसमें `PBN` टोकन के साथ आवश्यक नकदी मौजूद है:


```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"invoice": "lnbcrt30u1pncgd4rdqud3jxktt5w46x7unfv9kz6mn0v3jsnp4qv0grex9c6m22r9ltkzmzhddwg87eykx96zt47e5pz8sfz8qp28fgpp5jksvqtleryhvwr299qdz96qxzm24augy5agkdhltudk463lt9dassp5d6n0sqgl0c4gx52fdmutrdtqamt0y4xuz2rcgel4hpjwne08gmls9qyysgqcqpcxqzdylz5wfnkywnxvvmkvnt2x4fj6wre0gshvjtv95ervvzzg4592t2gdgchx6mkf5k45jrrdfn8j73d2f2xx4mrxycq7qzry4v4jan6uxhhacyqa4gn6plggwpq9j74tu74f2zsamtz6ymt600p8su4c4ap9g9d8ku2x3wdh6fuc8fd8pff2yzpjrf24ys3cltca9fgqut6gzj"
}' \
http://localhost:3001/sendpayment
```


![RLN](assets/fr/17.webp)


भुगतान हो गया है। इसे निम्न आदेश निष्पादित करके सत्यापित किया जा सकता है:


```bash
curl -X 'GET' \
'http://localhost:3001/listpayments' \
-H 'accept: application/json'
```


![RLN](assets/fr/18.webp)


RGB परिसंपत्तियों को ले जाने के लिए संशोधित लाइटनिंग नोड को तैनात करने का तरीका यहां बताया गया है। यह प्रदर्शन निम्न पर आधारित है:




- एक regtest वातावरण (`./regtest.sh` के माध्यम से) या Testnet;
- एक लाइटनिंग नोड (`RGB-lightning-node`) जो `bitcoind`, एक इंडेक्सर और एक `RGB-proxy-server` पर आधारित है;
- चैनल खोलने/बंद करने, टोकन जारी करने, लाइटनिंग के माध्यम से परिसंपत्तियों को स्थानांतरित करने आदि के लिए JSON REST API की एक श्रृंखला।


इस प्रक्रिया के लिए धन्यवाद:




- लाइटनिंग एंगेजमेंट लेनदेन में RGB संक्रमण की एंकरिंग के साथ एक अतिरिक्त आउटपुट (OP_RETURN या Taproot) शामिल है;
- स्थानान्तरण बिल्कुल पारंपरिक लाइटनिंग भुगतानों की तरह ही किया जाता है, लेकिन इसमें RGB टोकन जोड़ा जाता है;
- कई आरएलएन नोड्स को मार्ग से जोड़ा जा सकता है और कई नोड्स में भुगतान के साथ प्रयोग किया जा सकता है, बशर्ते मार्ग में बिटकॉइन और परिसंपत्ति RGB दोनों में पर्याप्त तरलता हो।


अगर आपको यह ट्यूटोरियल उपयोगी लगा, तो मैं बहुत आभारी रहूंगा अगर आप नीचे Green थंब लगाएंगे। कृपया इस लेख को अपने सोशल नेटवर्क पर शेयर करें। आपका बहुत-बहुत धन्यवाद!


मैं इस अन्य ट्यूटोरियल की भी अनुशंसा करता हूं जिसमें मैं समझाता हूं कि RGB Contract बनाने के लिए LNP/BP एसोसिएशन द्वारा विकसित RGB CLI टूल का उपयोग कैसे करें:


https://planb.network/tutorials/node/others/rgb-cli-1f8a28d4-fa99-4261-9d80-48275b496fd4