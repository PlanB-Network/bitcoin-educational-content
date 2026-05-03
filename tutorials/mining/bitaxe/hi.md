---
name: Bitaxe
description: BitAxe को कैसे सेट अप करें?
---
![video](https://youtu.be/tvLSK8v0MK8)


## परिचय


BitAxe एक ओपन-सोर्स प्रोजेक्ट है जिसे Skot द्वारा बनाया गया है और यह GitHub पर उपलब्ध है (https://github.com/skot/bitaxe) जो लागत प्रभावी mining प्रयोग की अनुमति देता है।


इसने बिटकॉइन mining के लिए विशेष मशीनों, ASIC के बाज़ार में अग्रणी Bitmain के प्रसिद्ध Antminer S19 की कार्यप्रणाली को रिवर्स-इंजीनियर किया है। अब, इन शक्तिशाली चिप्स का उपयोग नए ओपन-सोर्स प्रोजेक्ट्स में किया जा सकता है। Nerdminer के विपरीत, BitAxe में mining pool से कनेक्ट होने के लिए पर्याप्त कंप्यूटिंग शक्ति है, जिससे आप नियमित रूप से कुछ satoshi कमा सकते हैं। दूसरी ओर, Nerdminer को केवल सोलोपूल से कनेक्ट किया जा सकता है, जो एक लॉटरी टिकट की तरह काम करता है: आपके पास पूरे ब्लॉक रिवॉर्ड को जीतने का बहुत कम मौका होता है।


BitAxe के कई संस्करण हैं, जिनमें अलग-अलग चिप्स और प्रदर्शन क्षमताएं हैं:


| Bitaxe Model Series      | ASIC Chip | Used On                     | Expected Hash Rate          | Ideal For                                                                                                  |
| ------------------------ | --------- | --------------------------- | --------------------------- | ---------------------------------------------------------------------------------------------------------- |
| Bitaxe Max (Series 100)  | 1 x BM1397| Antminer Series 17          | 400 GH/s (up to 450 GH/s)   | Bitcoin mining beginners, offering a solid hash rate with moderate power consumption.                      |
| Bitaxe Ultra (Series 200)| 1 x BM1366| Antminer S19 XP and S19k Pro| 500 GH/s (up to 550 GH/s)   | Serious miners aiming to balance efficiency and higher hash rate.                                          |
| Bitaxe Hex (Series 300)  | 6 x BM1366| Antminer S19k Pro and S19 XP| 3.0 TH/s (up to 3.3 TH/s)   | Miners seeking scalability and high performance without sacrificing efficiency.                             |
| Bitaxe Supra (Series 400)| 1 x BM1368| Antminer S21                | 600 GH/s (up to 700 GH/s)   | Serious enthusiasts seeking the highest hash rates and efficiency.                                         |

इस ट्यूटोरियल में, हम BitAxe Ultra 204 का उपयोग करेंगे जिसमें BM1366 चिप लगी है, जिसका उपयोग Antminer S19XP के लिए किया जाता है। यह चिप विक्रेता द्वारा पहले से ही असेंबल और फ्लैश की हुई है।


[पुनर्विक्रेताओं की सूची इस पृष्ठ पर उपलब्ध है](https://bitaxe.org/legit.html)


![signup](assets/2.webp)


आम तौर पर, इसके साथ पावर सप्लाई भी दी जाती है। यदि नहीं, तो आपको 5V जैक केबल और कम से कम 4A की पावर सप्लाई खरीदनी होगी।


![signup](assets/1.webp)


## विन्यास

जब आप पहली बार अपने BitAxe को प्लग इन करेंगे, तो यह डिफ़ॉल्ट रूप से वाई-फ़ाई नेटवर्क से कनेक्ट होने का प्रयास करेगा। पाँच प्रयासों के बाद, यह अपने स्वयं के वाई-फ़ाई नेटवर्क का नाम प्रदर्शित करेगा ताकि आप उससे कनेक्ट होकर उसे कॉन्फ़िगर कर सकें।

इसके लिए आप किसी भी कंप्यूटर या स्मार्टफोन का इस्तेमाल कर सकते हैं। अपने वाई-फाई सेटिंग्स में जाएं, नए नेटवर्क खोजें और आपको Bitaxe_XXXX नाम का एक वाई-फाई नेटवर्क दिखाई देगा। यहां, यह `Bitaxe_A859` है। इस वाई-फाई नेटवर्क से कनेक्ट करें, और एक विंडो अपने आप खुल जाएगी।


![signup](assets/3.webp)


इस विंडो में, ऊपर बाईं ओर स्थित तीन छोटी क्षैतिज पट्टियों पर क्लिक करें, फिर 'सेटिंग्स' पर क्लिक करें।


![signup](assets/4.webp)


आपको अपने वाई-फाई नेटवर्क की जानकारी मैन्युअल रूप से दर्ज करनी होगी, क्योंकि इसमें कोई स्वचालित खोज प्रणाली नहीं है।


![signup](assets/5.webp)


इसलिए, वाई-फाई का SSID यानी अपने नेटवर्क का नाम, पासवर्ड और साथ ही आपके द्वारा चुने गए mining pool की जानकारी दें। ध्यान दें, यहां पूल का URL अलग-अलग तरीके से दिया जाता है। उदाहरण के लिए, Braiins के लिए, दिया गया पूल URL है: `stratum+tcp://eu.stratum.braiins.com:3333`।


![signup](assets/6.webp)


जैसा कि आप स्क्रीन पर देख सकते हैं, आपको `stratum+tcp://` और `:3333` वाले हिस्से को हटाना होगा, केवल `eu.stratum.braiins.com` को रहने देना होगा। फिर, `पोर्ट` फ़ील्ड में, पूल द्वारा दिए गए URL के अंत में मौजूद 4 अंक दर्ज करें, लेकिन बिना `:` के। यहाँ, यह `3333` है।


इस ट्यूटोरियल में हम ब्रेन्स mining pool का उपयोग कर रहे हैं, लेकिन आप चाहें तो कोई दूसरा भी चुन सकते हैं। आप mining pool पर हमारे ट्यूटोरियल [Plan ₿ Academy वेबसाइट पर](https://planb.academy/en/tutorials/mining) देख सकते हैं।


इसके बाद, `यूज़र` में अपना आइडेंटिफ़ायर और फिर `पासवर्ड` दर्ज करें, आमतौर पर यह `"x"` या `"Anything123"` होता है।


कोर वोल्टेज सेटिंग को डिफ़ॉल्ट रूप से 1200 पर ही रहने दें, और फ़्रीक्वेंसी को भी शुरुआत में डिफ़ॉल्ट मान पर ही रहने दें। बाद में कंप्यूटिंग क्षमता बढ़ाने के लिए इस सेटिंग को समायोजित किया जा सकता है। हालांकि, यह सुनिश्चित करना महत्वपूर्ण है कि चिप का तापमान 65-70°C से अधिक न हो, क्योंकि BitAxe में ज़्यादा गरम होने पर परफ़ॉर्मेंस कम करने का कोई सिस्टम नहीं है। यदि तापमान 65°C से बहुत अधिक हो जाता है, तो इससे आपकी BitAxe को नुकसान हो सकता है।


![signup](assets/7.webp)


सभी सेटिंग्स सही ढंग से दर्ज करने के बाद, नीचे दिए गए 'सेव' बटन पर क्लिक करें, फिर अपने बिटएक्स को अनप्लग करके और फिर से प्लग इन करके रीस्टार्ट करें।

यदि आपने अपनी जानकारी सही दर्ज की है, तो डिवाइस शीघ्र ही आपके वाई-फाई से कनेक्ट हो जाएगा, फिर mining pool से कनेक्ट होगा और अपनी छोटी स्क्रीन पर कुछ जानकारी प्रदर्शित करना शुरू कर देगा। mining pool के डैशबोर्ड पर यह जानकारी दिखने में संभवतः कुछ मिनट लगेंगे।

## डैशबोर्ड और स्क्रीन


तीन अलग-अलग डिस्प्ले स्क्रॉल होंगे। तीसरे पेज पर आपको `IP` जानकारी दिखाई देगी, जो वह IP एड्रेस है जिसके द्वारा आप डैशबोर्ड से कनेक्ट कर सकते हैं। यहां एड्रेस `192.168.1.19` है।


![signup](assets/8.webp) ![signup](assets/9.webp) ![signup](assets/10.webp)


डैशबोर्ड तक पहुंचने के लिए, बस इस पते को अपने इंटरनेट ब्राउज़र में दर्ज करें।


डैशबोर्ड पर, आपको छोटी स्क्रीन पर प्रदर्शित सभी जानकारी मिलेगी, जिसे अब हम विस्तार से देखेंगे।


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

आप बिना किसी समस्या के किसी भी समय वाई-फाई या पूल की सेटिंग्स बदल सकते हैं।

आपके कमरे के वेंटिलेशन और तापमान के आधार पर, आपको प्रदर्शन को बढ़ाना या घटाना पड़ सकता है ताकि तापमान 65°C से अधिक न हो। यदि आप प्रदर्शन बढ़ाते हैं, तो आपको अधिक satoshi मिलेंगे, लेकिन आपका BitAxe अधिक बिजली की खपत भी करेगा!