---
name: Lightning Smoke Machine
description: ESP32 के माध्यम से लाइटनिंग पेमेंट का उपयोग करके स्मोक मशीन को चालू करें।
---

![cover-lightning-smoke-machine](assets/cover.webp)



## परिचय



एक क्लासिक स्मोक मशीन को Lightning Network के माध्यम से Bitcoin में भुगतान योग्य उपकरण में बदल देता है। प्रत्येक भुगतान स्वचालित रूप से धुएं की एक धार उत्पन्न करता है!





- स्तर: मध्यवर्ती
- अनुमानित समय: 2-3 घंटे
- उपयोग के उदाहरण: Bitcoin इवेंट्स, कलात्मक प्रदर्शन, लाइटनिंग डेमो, स्वचालित स्टेज इफेक्ट्स



## आवश्यक शर्तें



### ज्ञान





 - बुनियादी इलेक्ट्रॉनिक्स (वायरिंग, रिले)
 - वेल्डिंग (या डुपोंट कनेक्टर्स का उपयोग)
 - नेटवर्क कॉन्फ़िगरेशन (वाईफ़ाई, वेबसॉकेट)



### खाते आवश्यक हैं





- BTCPay सर्वर: कार्यात्मक इंस्टेंस (स्व-होस्टेड या होस्टेड)
- Blink Wallet : खाता + पहुँच API



### पहुँच





- BTCPay सर्वर पर व्यवस्थापक पहुंच
- ESP32 के लिए वाईफाई कनेक्शन



## सामग्री की आवश्यकता



### हार्डवेयर - इलेक्ट्रॉनिक घटक





- 1 माइक्रोकंट्रोलर - ESP32-WROOM-32


*ESP32-WROOM-32 एक कॉम्पैक्ट, कम लागत वाला वाईफाई/ब्लूटूथ माइक्रोकंट्रोलर है जिसका उपयोग इलेक्ट्रॉनिक उपकरणों को इंटरनेट से जोड़ने और उन्हें दूरस्थ रूप से नियंत्रित करने के लिए किया जाता है।*



![ESP32](assets/fr/1.webp)





- 1 रिले मॉड्यूल - ऑप्टोकपलर सहित 5V


*रिले एक स्विच की तरह होता है जिसे ESP32 स्मोक मशीन को चालू या बंद करने के लिए संचालित कर सकता है।*



![relay](assets/fr/2.webp)





- लगभग 10 डुपोंट केबल - मेल/मेल और मेल/फीमेल



![dupont-cables](assets/fr/3.webp)





- 1. ESP32 के लिए बिजली आपूर्ति - 5V USB या Li-Po बैटरी



![battery](assets/fr/4.webp)





- 1 माइक्रो-यूएसबी केबल - ESP32 और बिजली आपूर्ति के बीच कनेक्शन



![micro-usb-cables](assets/fr/5.webp)





- 12V बैटरी रिमोट कंट्रोल के साथ 1220V फॉग मशीन



![remote-and-smoke-machine](assets/fr/6.webp)





- आपकी स्मोक मशीन के अनुकूल तरल पदार्थ की 1 बोतल



### हार्डवेयर - उपकरण





- सोल्डरिंग आयरन + टिन (यदि सोल्डरिंग कर रहे हों)
- पेंच चालक
- मल्टीमीटर (अनुशंसित)



### Software





- फर्मवेयर Bitcoin स्विच : **[https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/)**
- वेबसीरियल-संगत वेब ब्राउज़र (क्रोम/एज/Brave)
- BTCPay सर्वर कॉन्फ़िगर किया गया है। BTCPay सर्वर इंस्टेंस बनाने के बारे में अधिक जानकारी के लिए, इस ट्यूटोरियल पर जाएँ: https://planb.academy/fr/tutorials/business/point-of-sale/btcpay-server-928eb01e-824b-4b57-a3e8-8727633beddc



## सिस्टम आर्किटेक्चर



![architecture-lightning-smoke-machine](assets/fr/7.webp)



---


**⚠️** **सुरक्षा चेतावनी - आगे बढ़ने से पहले पढ़ें** **⚠️**



इस परियोजना में एक फॉग मशीन का उपयोग किया जाता है जो **220V मेन सप्लाई** से जुड़ी होती है। इसके अनुचित संचालन से **घातक विद्युतविद्युत क्षति** या **आग** लग सकती है।



**अपरिवर्तनीय नियम:**



1. रिमोट कंट्रोल खोलने या वायरिंग से छेड़छाड़ करने से पहले स्मोक मशीन को हमेशा मेन पावर से डिस्कनेक्ट करें।


2. रिमोट कंट्रोल को छूने से पहले उसमें से बैटरी निकाल दें (शॉर्ट सर्किट और पुर्जों को नुकसान होने का खतरा है)।


3. किसी भी कनेक्शन को दोबारा जोड़ने से पहले **सुनिश्चित करें कि आपके सभी कनेक्शन अलग-थलग हैं।**


4. रिमोट कंट्रोल बॉक्स को बंद और सुरक्षित किए जाने तक 220V का कनेक्शन दोबारा न जोड़ें।



यदि आप इस तरह के व्यवहार से सहज नहीं हैं, तो अपने साथ किसी ऐसे व्यक्ति को ले जाएं जो सहज हो।



---

## भाग 1: हार्डवेयर असेंबली



### चरण 1: रिमोट कंट्रोल तैयार करना



उद्देश्य: रिले को रिमोट कंट्रोल के चालू/बंद बटन से जोड़ना


1. रिमोट कंट्रोल खोलें




    - चालू/बंद बटन को पहचानें
    - रिमोट कंट्रोल को खोलने के लिए केस के पेंच खोलें


2. कनेक्शनों का पता लगाएं




 - + और - टर्मिनलों का पता लगाएं
 - मल्टीमीटर से निरंतरता की जांच करें (वैकल्पिक)



![smoke-machine-remote](assets/fr/8.webp)



3. बटन की वायरिंग (सोल्डर या कनेक्टर)




    - बटन के - टर्मिनल पर एक काली केबल को सोल्डर करें।
    - कॉमन + टर्मिनल पर एक लाल केबल को सोल्डर करें।



![smoke-machine-remote](assets/fr/9.webp)



### चरण 2: रिले मॉड्यूल से कनेक्ट करना



**याद दिलाना: रिले शब्दावली**




| **Terminal**         | **Description**           | **Function**                        |
| -------------------- | ------------------------- | ----------------------------------- |
| NO (Normally Open)   | Circuit open by default | Closes when the relay is activated |
| NC (Normally Closed) | Circuit closed by default  | Opens when the relay is activated  |
| COM (Common)         | Central terminal          | Switches between NO and NC              |

**रिमोट कंट्रोल से रिले मॉड्यूल तक की वायरिंग:**




- चालू/बंद बटन से काला तार **→** बंद (सामान्यतः खुला)
- लाल तार (सामान्य) **→** कॉम (सामान्य)



**तर्क:**


जब ESP32 रिले को सक्रिय करता है, तो यह COM और NO को जोड़ता है, जो बिल्कुल रिमोट कंट्रोल बटन दबाने के समान है।


जब ESP32 रिले को काटता है, तो COM और NO अलग हो जाते हैं, जो बटन को छोड़ने के बराबर है।



![remote-relay](assets/fr/10.webp)



### चरण 3: ESP32 को रिले मॉड्यूल से जोड़ना



**वायरिंग का नक्शा:**




| **ESP32** | **→** | **Relay Module** |
| --------- | ----- | ----------------- |
| V5 (5V)   | **→** | VCC               |
| GND       | **→** | GND               |
| GPIO 21   | **→** | IN (Input)        |

**सत्यापन:**




- VCC और GND सही ढंग से जुड़े हुए हैं (ध्रुवीयता के अनुसार)।
- GPIO 21 का उपयोग नियंत्रण संकेत के लिए किया जाता है।
- कोई स्पष्ट शॉर्ट सर्किट नहीं



![relay-esp32](assets/fr/11.webp)



**चेकपॉइंट हार्डवेयर**


सॉफ्टवेयर पर स्विच करने से पहले, जांच लें:




- सही ढंग से वायर्ड रिमोट कंट्रोल
- रिले मॉड्यूल ESP32 से जुड़ा हुआ है
- कोई भी नंगा तार अन्य घटकों को स्पर्श न करे।
- 220V हमेशा डिस्कनेक्ट रहता है



![relay-esp32](assets/fr/12.webp)





---


## भाग 2: Software कॉन्फ़िगरेशन



हम उदाहरण के तौर पर *Blink* का उपयोग करेंगे, लेकिन यदि आप कोई अन्य विकल्प पसंद करते हैं तो *BTCPay Server* *Strike, Breez और Boltz* भी प्रदान करता है।



### चरण 1: प्लगइन्स, इंस्टॉलेशन *Bitcoin स्विच* + *Blink



1 - एडमिन अकाउंट से अपने *BTCPay सर्वर* इंस्टेंस पर जाएं



2 - अपना पहला ब्लाइंड बनाएं



3 - *BTCPay सर्वर* के बाईं ओर, नीचे स्क्रॉल करें और *"प्लगइन प्रबंधित करें"* पर जाएं।



![btcpay-plugins](assets/fr/13.webp)



4 - हम *BitcoinSwitch* प्लगइन के साथ-साथ *Blink* भी इंस्टॉल करने जा रहे हैं।



![btcpay-plugins](assets/fr/14.webp)



5 - प्लगइन की सूची में नीचे स्क्रॉल करें और *"इंस्टॉल"* पर क्लिक करें: *BitcoinSwitch और Blink* (या आपकी पसंद का उपलब्ध wallet)



![btcpay-plugins](assets/fr/15.webp)



6 - इंस्टॉलेशन पूरा होने के बाद, *BTCPay सर्वर* को रीस्टार्ट करें और इंस्टेंस के रीस्टार्ट होने के लिए 1 मिनट प्रतीक्षा करें।



![btcpay-plugins](assets/fr/16.webp)



7 - जब आप *"प्लगइन प्रबंधित करें"* पर वापस जाएं, तो जांच लें कि दोनों प्लगइन इंस्टॉल हो गए हैं।



![btcpay-plugins](assets/fr/17.webp)



### चरण 2: बैकएंड: *BTCPay सर्वर + Blink* कॉन्फ़िगरेशन



**1 - एक wallet *Blink बनाएं***




- https://www.blink.sv पर जाएं
- अपना खाता बनाएं। कृपया ट्यूटोरियल देखें:



[https://planb.academy/tutorials/wallet/mobile/blink-7ea5f5a4-e728-4ff9-b3f9-cf20aa6fc2bd)



**2 - API कुंजी जनरेट करें *Blink***




- API इंटरफ़ेस पर जाएं: **[https://www.blink.sv/en/api](https://www.blink.sv/en/api)** और उसी खाते से लॉग इन करें जिसका उपयोग आपने अपना wallet *Blink* बनाने के लिए किया था।



![blink-api](assets/fr/18.webp)





   - एक बार कनेक्ट हो जाने के बाद, *API Keys* टैब पर जाएं



![blink-api](assets/fr/19.webp)





   - अपने API कुंजी कॉन्फ़िगरेशन तक पहुँचने के लिए ऊपरी दाएं कोने में *" + "* पर क्लिक करें



![blink-api](assets/fr/20.webp)





   - अपनी API कुंजी को एक नाम दें और डिफ़ॉल्ट सेटिंग्स को वैसे ही रहने दें। फिर, तीसरे चरण में, अपनी API कुंजी को नोट कर लें - यह आपको केवल एक बार दिखाई देगी: `blink_mZ5KxxxxxxxxxxxxxNbmX`



![blink-api](assets/fr/21.webp)





   - एक बार बन जाने के बाद, यह आपकी सक्रिय API कुंजी सूची में दिखाई देना चाहिए।



![blink-api](assets/fr/22.webp)



**3 - *Blink* को *BTCPay सर्वर* से कनेक्ट करें**




- अपना *BTCPay सर्वर* खोलें
- यहां जाएं: *Wallet* **→** *लाइटनिंग*



![btcpay-server](assets/fr/23.webp)





- *कस्टम नोड का उपयोग करें* पर क्लिक करें
- निम्नलिखित कनेक्शन स्ट्रिंग को पेस्ट करें:



```
type=blink;server=https://api.blink.sv/graphql;api-key=blink_mZ5KxxxxxxxxNbmX;wallet-id=0a3fc465-082xxxxxxxxxx-2545595d856f
```



**⚠️** **महत्वपूर्ण** :




- पहले भाग को संशोधित न करें: `type=blink;server=https://api.blink.sv/graphql`;
- केवल बदलें:
    - api-key= *आपके API Blink* कुंजी द्वारा
    - wallet-id= *आपके wallet Blink* ID द्वारा
- फिर *कनेक्शन टेस्ट करें* पर क्लिक करें, फिर *सेव करें* पर क्लिक करें।



![btcpay-server](assets/fr/24.webp)





 - सुनिश्चित करें कि कनेक्शन स्थापित हो गया है (हरा स्टेटस)।



![btcpay-server](assets/fr/25.webp)



**4 - प्वाइंट ऑफ सेल (पीओएस) बनाएं**




- BTCPay सर्वर में, *प्लगइन्स* टैब पर जाएं और *पॉइंट ऑफ सेल* पर क्लिक करें।



![btcpay-server](assets/fr/26.webp)





- अपने PoS को एक नाम दें और *बनाएँ* पर क्लिक करें।



![btcpay-server](assets/fr/27.webp)





- पीओएस कॉन्फ़िगरेशन:
    - बिक्री केंद्र का प्रकार चुनें = *प्रिंट डिस्प्ले*
    - मुद्रा = *सैट्स*
    - *सेव* पर क्लिक करें



![btcpay-server](assets/fr/28.webp)





- उत्पाद कॉन्फ़िगरेशन :
    - सभी डिफ़ॉल्ट उत्पादों को हटाएँ
    - फिर *आइटम जोड़ें* पर क्लिक करें।



![btcpay-server](assets/fr/29.webp)



![btcpay-server](assets/fr/30.webp)





- उत्पाद को कॉन्फ़िगर करें:
    - शीर्षक: *धुआं मशीन*
    - मूल्य: *10 sats*
    - Bitcoin GPIO स्विच : 21
    - Bitcoin स्विच की अवधि (मिलीसेकंड में): 5000
    - नए उत्पाद को सहेजने के लिए *बंद करें* पर क्लिक करें और फिर *सहेजें* पर क्लिक करें।



![btcpay-server](assets/fr/31.webp)



### चरण 3: फर्मवेयर: ESP32 को Flash से अपडेट करना



**1 - फ्लैश साइट पर जाएं




- यहां जाएं: [https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/)



![bitcoinswitch-lnbits](assets/fr/32.webp)



**2 - Flash Bitcoin स्विच फर्मवेयर**




- अपने ESP32 को USB/Micro-USB केबल से अपने कंप्यूटर से कनेक्ट करें।
- फिर *डिवाइस से कनेक्ट करें* पर क्लिक करें।
- एक विंडो खुलेगी, अपने ESP32 पर USB पोर्ट चुनें, फिर *कनेक्ट* पर क्लिक करें।



![bitcoinswitch-lnbits](assets/fr/33.webp)





- एक बार आपका ESP32 कनेक्ट हो जाए, तो हम BitcoinSwitch फर्मवेयर फ्लैश करेंगे। *T-Display* सेक्शन में, उपलब्ध नवीनतम संस्करण (वर्तमान में: *bitcoinSwitch T-Display v1.0.1*) के लिए *Upload Firmware* पर क्लिक करें।



![bitcoinswitch-lnbits](assets/fr/34.webp)





- अपलोड होने का इंतज़ार करें, जब लॉग में *"लीविंग..."* दिखाई दे, तब प्रक्रिया पूरी हो जाएगी।


![bitcoinswitch-lnbits](assets/fr/35.webp)





- ESP32 को अनप्लग करें



**3 - BitcoinSwitch फर्मवेयर इंस्टॉलेशन की जांच करें




- पेज रीलोड करें: [https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/)
- अपने USB/Micro-USB केबल का उपयोग करके ESP32 को अपने कंप्यूटर से दोबारा कनेक्ट करें।
- फिर *डिवाइस से कनेक्ट करें* पर क्लिक करें।
- अपने ESP32 पर USB पोर्ट चुनें, फिर ऊपर बताए अनुसार *कनेक्ट* पर क्लिक करें।
- एक बार कनेक्ट हो जाने पर, ESP32 पर **रीसेट** बटन दबाएँ।
- लॉग्स में जांचें कि अंतिम पंक्तियाँ क्या दर्शाती हैं:



```
Welcome to BitcoinSwitch! (v1.0.1)
Config file does not exist.
Entering config mode. until we receive /config-done.
```



(यह सामान्य है, इसका मतलब है कि अभी तक कोई कॉन्फ़िगरेशन नहीं है, लेकिन फ़र्मवेयर इंस्टॉल हो चुका है।)



![bitcoinswitch-lnbits](assets/fr/36.webp)



**4 - वेबसॉकेट LNURL जनरेट करें** URL



अपेक्षित अंतिम प्रारूप:



```
https://XXXXv/apps/46XXXXXXXXXXXXXXXXXXXXwFB/pos
```



उत्पादन के चरण:




- अपने BTCPay सर्वर इंस्टेंस को खोलें, फिर उस PoS पर जाएं जिसे हमने बाद में बनाया था।
- फिर ब्राउज़र में अपना पीओएस खोलने के लिए "व्यू" पर क्लिक करें।



![btcpay-server-https](assets/fr/37.webp)





- पेज का यूआरएल कॉपी करें, उदाहरण के लिए:



![btcpay-server-https](assets/fr/38.webp)



आइए इस यूआरएल को समझते हैं:



```
https://XXXXv/apps/46XXXXXXXXXXXXXXXXXXXXwFB/pos
```





- `XXXXv` → आपके BTCPay सर्वर इंस्टेंस का डोमेन
- `46XXXXXXXXXXXXXXXXXXXXXXwFB` → आपका PoS विशिष्ट पहचानकर्ता
- `/pos` → बिक्री केंद्र को दर्शाता है



इसे रूपांतरित करें:




- `https://` को `wss://` से बदलें
- अंत में `/bitcoinswitch` जोड़ें



परिणाम:



```
wss://XXXXv/apps/46XXXXXXXXXXXXXXXXXXXXwFB/pos/bitcoinswitch
```



भविष्य में कॉन्फ़िगरेशन के लिए इस URL को सुरक्षित रखें, क्योंकि इससे आपका ESP32 BTCPay सर्वर के साथ वास्तविक समय में संचार कर सकेगा। वेबसॉकेट प्रोटोकॉल (`wss://`) दोनों के बीच एक स्थायी कनेक्शन स्थापित करता है: जैसे ही आपके PoS पर लाइटनिंग भुगतान की पुष्टि होती है, BTCPay तुरंत ESP32 को जानकारी भेज देता है, जिससे आपका स्मोक मशीन चालू हो जाता है।



**5 - वाईफाई और वेबसॉकेट को कॉन्फ़िगर करना




- अपने ESP32 को कनेक्ट करके इस पेज पर वापस जाएँ: [https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/)
- *डिवाइस कॉन्फ़िगर करें* → *वाईफ़ाई सेटिंग्स* पर जाएं



सूचित करना :




- वाईफाई एसएसआईडी: आपके वाईफाई नेटवर्क का नाम
- वाईफाई पासवर्ड: आपका वाईफाई पासवर्ड



![bitcoinswitch-lnbits](assets/fr/39.webp)





- *LNbits डिवाइस URL* सेक्शन में, पिछले चरण में बनाए गए वेबसॉकेट URL को पेस्ट करें।
- *कॉन्फ़िगरेशन अपलोड करें* पर क्लिक करें



![bitcoinswitch-lnbits](assets/fr/40.webp)





- अपलोड पूरा होने तक प्रतीक्षा करें; लॉग में आपके द्वारा दर्ज किए गए पैरामीटर (एसएसआईडी, पासवर्ड और वेबसॉकेट यूआरएल) प्रदर्शित होने चाहिए।



![bitcoinswitch-lnbits](assets/fr/41.webp)





- ESP32 द्वारा वेबसॉकेट कनेक्शन स्थापित होने तक प्रतीक्षा करें। आपको यह दिखाई देगा:



```
WiFi connection established!

[WebSocket] Connected to url: ...
```



![bitcoinswitch-lnbits](assets/fr/42.webp)





- अब आप ESP32 को डिस्कनेक्ट कर सकते हैं।



---
## चेकपॉइंट Softवेयर



अंतिम परीक्षा से पहले, जाँच लें:





- Blink, BTCPay से जुड़ा हुआ है
- कम से कम 1 आइटम के साथ पीओएस बनाया गया
- ESP32 को Bitcoin स्विच से फ्लैश किया गया।
- ESP32 पर वाईफाई कॉन्फ़िगर किया गया
- वेबसॉकेट यूआरएल सही है
- त्रुटि रहित ESP32 लॉग



---

## परीक्षण और डिबगिंग



### अंतिम परीक्षा पूरी करें



1. स्मोक मशीन (220V) को प्लग में लगाएं और उसे चालू करें।


2. ESP32 को पावर दें (बैटरी या USB के माध्यम से)


3. अपने ब्राउज़र में BTCPay PoS खोलें।


4. "स्मोक-मशीन" आइटम को स्कैन करें


5. wallet लाइटनिंग (Blink या अन्य wallet) से भुगतान करें।


6. अवलोकन करें:




 - रिले क्लिक करता है (श्रव्य ध्वनि और रिले एलईडी लाइट जलती है)
 - धुआँ मशीन सक्रिय हो गई है
 - धुआं उत्पन्न हुआ!



### निष्पक्षता से जुड़ी समस्याएं और उनके समाधान




| **Problem**                        | **Probable Cause**              | **Solution**                                                                                 |
| ----------------------------------- | ------------------------------- | -------------------------------------------------------------------------------------------- |
| ESP32 does not connect            | Missing USB driver             | Install [CH340 drivers](https://learn.sparkfun.com/tutorials/how-to-install-ch340-drivers) |
| Relay does not click                | Wrong GPIO wiring            | Check GPIO 21 → IN                                                                        |
| Smoke machine does not respond         | Remote control improperly wired         | Check NO/NC/COM                                                                           |
| WebSocket timeout                   | Incorrect URL                  | Check wss:// and /bitcoinswitch                                                            |
| WiFi does not connect             | SSID/Password incorrect            | Re-flash WiFi config                                                                    |
| Payment received but nothing happens | ESP32 not connected to WebSocket | Check RESET logs                                                                      |

## संसाधन



### उपयोगी कड़ियां





- Bitcoin स्विच फर्मवेयर: [https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/)
- BTCPay सर्वर दस्तावेज़: [https://docs.btcpayserver.org/](https://docs.btcpayserver.org/)
- Blink API : [https://dev.blink.sv/](https://dev.blink.sv/)
- ESP32 पिनआउट : [https://randomnerdtutorials.com/esp32-pinout-reference-gpios/](https://randomnerdtutorials.com/esp32-pinout-reference-gpios/)



### समुदाय का समर्थन





- BTCPay सर्वर** : [chat.btcpayserver.org](https://chat.btcpayserver.org/) - आधिकारिक मैटरमोस्ट
- BTCPay सर्वर Telegram** : [t.me/btcpayserver](https://t.me/btcpayserver)
- LNbits** : [t.me/lnbits](https://t.me/lnbits) - आधिकारिक Telegram, सक्रिय समुदाय
- BitcoinSwitch (फर्मवेयर बग)**: [github.com/lnbits/bitcoinswitch/issues](https://github.com/lnbits/bitcoinswitch/issues)



### सोर्स कोड





- BitcoinSwitch फर्मवेयर स्रोत कोड: [https://github.com/lnbits/bitcoinswitch](https://github.com/lnbits/bitcoinswitch)



---

**⚡** sats को इकट्ठा करो, धुआं उड़ाओ, मजे करो, विनम्र रहो! **⚡**