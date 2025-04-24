---
name: बिटएक्स की स्थापना
विवरण: बिटएक्स कैसे स्थापित करें?

---

### परिचय


बिटएक्स स्कॉट द्वारा निर्मित एक ओपन-सोर्स प्रोजेक्ट है और [गिटहब पर उपलब्ध है](https://github.com/skot/bitaxe) जो लागत प्रभावी Mining प्रयोग की अनुमति देता है।


इसने ASICs में मार्केट लीडर बिटमैन द्वारा प्रसिद्ध एंटमाइनर S19 के कामकाज को रिवर्स-इंजीनियर किया है, जो Bitcoin Mining के लिए विशेष मशीनें हैं। अब, इन शक्तिशाली चिप्स का उपयोग नए ओपन-सोर्स प्रोजेक्ट्स में करना संभव है। नर्डमाइनर के विपरीत, बिटएक्स में Mining pool से कनेक्ट होने के लिए पर्याप्त कंप्यूटिंग शक्ति है, जो आपको नियमित रूप से कुछ सातोशी अर्जित करने की अनुमति देगा। दूसरी ओर, नर्डमाइनर को केवल सोलोपूल नामक चीज़ से जोड़ा जा सकता है, जो लॉटरी टिकट की तरह काम करता है: आपके पास पूरा Block reward जीतने का एक छोटा सा मौका है।


बिटएक्स के कई संस्करण हैं, जिनमें अलग-अलग चिप्स और प्रदर्शन हैं:


| Bitaxe Model Series      | ASIC Chip | Used On                     | Expected Hash Rate          | Ideal For                                                                                                  |
| ------------------------ | --------- | --------------------------- | --------------------------- | ---------------------------------------------------------------------------------------------------------- |
| Bitaxe Max (Series 100)  | 1 x BM1397| Antminer Series 17          | 400 GH/s (up to 450 GH/s)   | Bitcoin mining beginners, offering a solid hash rate with moderate power consumption.                      |
| Bitaxe Ultra (Series 200)| 1 x BM1366| Antminer S19 XP and S19k Pro| 500 GH/s (up to 550 GH/s)   | Serious miners aiming to balance efficiency and higher hash rate.                                          |
| Bitaxe Hex (Series 300)  | 6 x BM1366| Antminer S19k Pro and S19 XP| 3.0 TH/s (up to 3.3 TH/s)   | Miners seeking scalability and high performance without sacrificing efficiency.                             |
| Bitaxe Supra (Series 400)| 1 x BM1368| Antminer S21                | 600 GH/s (up to 700 GH/s)   | Serious enthusiasts seeking the highest hash rates and efficiency.                                         |

इस ट्यूटोरियल में, हम एक बिटएक्स अल्ट्रा 204 का उपयोग करेंगे जो एंटमाइनर S19XP के लिए उपयोग की जाने वाली BM1366 चिप से लैस है। यह पहले से ही रिटेलर द्वारा असेंबल और फ्लैश किया गया है।


### [खुदरा विक्रेताओं की सूची इस पृष्ठ पर उपलब्ध है](https://bitaxe.org/legit.html)


![signup](assets/2.webp)


आम तौर पर, पावर Supply इसके साथ बेचा जाता है। यदि नहीं, तो आपको 5V जैक केबल और कम से कम 4A के साथ पावर Supply खरीदना होगा।


![signup](assets/1.webp)


### विन्यास

जब आप पहली बार अपना BitAxe प्लग इन करेंगे, तो यह डिफ़ॉल्ट रूप से वाई-फाई नेटवर्क से कनेक्ट होने का प्रयास करेगा। पाँच प्रयासों के बाद, यह अपने स्वयं के वाई-फाई नेटवर्क का नाम प्रदर्शित करेगा ताकि आप उससे कनेक्ट हो सकें और उसे कॉन्फ़िगर कर सकें।

ऐसा करने के लिए, आप किसी भी कंप्यूटर या स्मार्टफोन का उपयोग कर सकते हैं। अपने वाई-फाई सेटिंग्स पर जाएं, नए नेटवर्क खोजें, और आपको Bitaxe_XXXX नामक एक वाई-फाई दिखाई देगा। यहाँ, यह `Bitaxe_A859` है। इस वाई-फाई नेटवर्क से कनेक्ट करें, और एक विंडो अपने आप खुल जाएगी।


![signup](assets/3.webp)


इस विंडो में, ऊपर बाईं ओर तीन छोटी क्षैतिज पट्टियों पर क्लिक करें, फिर `सेटिंग्स` पर क्लिक करें।


![signup](assets/4.webp)


आपको अपने वाई-फाई नेटवर्क की जानकारी मैन्युअल रूप से दर्ज करनी होगी, क्योंकि इसमें कोई स्वचालित खोज प्रणाली नहीं है।


![signup](assets/5.webp)


इसलिए, वाई-फाई का SSID, यानी आपके नेटवर्क का नाम, पासवर्ड, साथ ही आपके द्वारा चुने गए Mining pool की जानकारी बताएं। सावधान रहें, यहाँ पूल का URL उसी तरह प्रस्तुत नहीं किया गया है। उदाहरण के लिए, Braiins के लिए, प्रदान किया गया पूल URL है: `stratum+tcp://eu.stratum.braiins.com:3333`।


![signup](assets/6.webp)


जैसा कि आप स्क्रीन पर देख सकते हैं, आपको `stratum+tcp://` और `:3333` भागों को हटाना होगा, केवल `eu.stratum.braiins.com` को छोड़ना होगा। फिर, `Port` फ़ील्ड में, पूल द्वारा दिए गए URL के अंत में 4 अंक दर्ज करें, लेकिन `:` के बिना। यहाँ, यह `3333` है।


इस ट्यूटोरियल में, हम Braiins Mining pool का उपयोग कर रहे हैं, लेकिन आप कोई दूसरा विकल्प चुनने के लिए स्वतंत्र हैं। आप Mining पूल पर हमारे ट्यूटोरियल [प्लानबी नेटवर्क वेबसाइट](https://planb.network/en/tutorials/Mining) पर पा सकते हैं।


इसके बाद, `User` में अपना पहचानकर्ता और फिर `Password` दर्ज करें, आमतौर पर यह `"x"` या `"Anything123"` होता है।


`कोर वोल्टेज` सेटिंग को डिफ़ॉल्ट रूप से `1200` पर छोड़ देना चाहिए, और `फ़्रीक्वेंसी` के लिए भी, शुरुआत में डिफ़ॉल्ट मान को छोड़ दें। अधिक कंप्यूटिंग शक्ति प्राप्त करने के लिए बाद में इस सेटिंग को समायोजित करना संभव होगा। हालाँकि, यह सुनिश्चित करना महत्वपूर्ण है कि चिप का तापमान 65-70°C से अधिक न हो, क्योंकि बिटएक्स में ओवरहीटिंग के मामले में प्रदर्शन को कम करने की प्रणाली नहीं है। यदि तापमान 65°C से अधिक हो जाता है, तो यह आपके बिटएक्स को नुकसान पहुंचा सकता है।


![signup](assets/7.webp)


एक बार जब आप सभी सेटिंग्स सही ढंग से दर्ज कर लें, तो नीचे दिए गए `सहेजें` बटन पर क्लिक करें, फिर अपने बिटएक्स को अनप्लग करके और फिर से प्लग करके पुनः आरंभ करें।

अगर आपने अपनी जानकारी सही तरीके से दर्ज की है, तो डिवाइस जल्दी से आपके वाई-फाई से, फिर Mining pool से कनेक्ट हो जाएगी और अपनी छोटी स्क्रीन पर कुछ जानकारी दिखाना शुरू कर देगी। Mining pool के डैशबोर्ड पर इसे दिखने में शायद कुछ मिनट लगेंगे।

### डैशबोर्ड और स्क्रीन


तीन अलग-अलग डिस्प्ले स्क्रॉल करेंगे। तीसरे पेज पर, आपको `IP` जानकारी दिखाई देगी, जो IP Address है जो आपको डैशबोर्ड से कनेक्ट करने की अनुमति देता है। यहाँ, Address `192.168.1.19` है।


![signup](assets/8.webp) ![signup](assets/9.webp) ![signup](assets/10.webp)


डैशबोर्ड तक पहुंचने के लिए, बस अपने इंटरनेट ब्राउज़र में यह Address दर्ज करें।


डैशबोर्ड पर आपको सभी जानकारी छोटी स्क्रीन पर प्रदर्शित मिलेगी, जिसे अब हम विस्तार से देखेंगे।


![signup](assets/11.webp)


| BitAxe Screen | Dashboard                                   | Description                                                                                                                                                                                                               |
| ------------- | ------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Gh            | Hashrate                                    | The current computing power, expressed in GigaHash/s                                                                                                                                                                      |
| W/THs         | Efficiency                                  | This is the efficiency of your BitAxe expressed in W/THs. It's the ratio between the electrical power consumed and the computing power produced.                                                                          |
| A/R           | Shares                                      | Quantity of `Shares` sent by your BitAxe to the pool, representing the amount of work provided.                                                                                                                          |
| UT            | Uptime                                      | Time since your BitAxe has been operating without interruption (available in the left menu under `Logs`).                                                                                                                |
| BD            | Best Difficulty                             | Maximum difficulty reached since the last restart. For comparison, the current network difficulty is about 85T.                                                                                                          |
| FAN           | FAN in the `Heat` box                       | Fan rotation speed, expressed in rotations per minute.                                                                                                                                                                    |
| Temp          | ASIC temperature in the `Heat` box          | Chip temperature, which should not exceed 65°C.                                                                                                                                                                           |
| Pwr           | Power                                       | Power in watts consumed. However, this information does not take into account the screen, the fan, or the power supply. For example, when it displays 11.7W, the total consumption is actually 15.8W.                    |
| mV mA         | Input Voltage Input Current                 | Voltage and current consumed by the machine. The power in watts is equal to the voltage multiplied by the current.                                                                                                        |
| FH            | Free Heap Memory (left menu -> `Logs`)      | The available memory.                                                                                                                                                                                                     |
| vCore         | ASIC Voltage (in the Performance box)       | Voltage measured on the ASIC chip.                                                                                                                                                                                        |
| IP            | NA                                          | IP Address.                                                                                                                                                                                                               |
| V2.1.0       | Version (left menu -> `Logs`)               | Firmware version.                                                                                                                                                                                                         |

आप बिना किसी समस्या के किसी भी समय वाई-फाई या पूल सेटिंग बदल सकते हैं।

आपके कमरे के वेंटिलेशन और तापमान के आधार पर, आपको प्रदर्शन को बढ़ाने या घटाने की आवश्यकता हो सकती है ताकि तापमान 65 डिग्री सेल्सियस से अधिक न हो। यदि आप प्रदर्शन बढ़ाते हैं, तो आप अधिक सातोशी अर्जित करेंगे, लेकिन आपका बिटएक्स भी अधिक बिजली की खपत करेगा!