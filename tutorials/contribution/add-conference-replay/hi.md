---
name: कॉन्फ्रेंस रीप्ले जोड़ना
description: Plan ₿ Academy पर कॉन्फ्रेंस रीप्ले कैसे जोड़ें?
---
![conference](assets/cover.webp)


PlanB का उद्देश्य Bitcoin विषय पर यथासंभव अधिक से अधिक भाषाओं में उच्च स्तरीय शैक्षिक संसाधन उपलब्ध कराना है। साइट पर प्रकाशित सभी सामग्री ओपन-सोर्स है और GitHub पर होस्ट की गई है, जिससे कोई भी व्यक्ति प्लेटफ़ॉर्म को समृद्ध बनाने में योगदान दे सकता है।


क्या आप अपने Bitcoin सम्मेलन का रीप्ले Plan ₿ Academy साइट पर जोड़ना चाहते हैं और इस इवेंट को सबके सामने लाना चाहते हैं, लेकिन नहीं जानते कि यह कैसे करें? यह ट्यूटोरियल आपके लिए है!


हालांकि, यदि आप भविष्य में होने वाले किसी सम्मेलन को जोड़ना चाहते हैं, तो मैं आपको इस अन्य ट्यूटोरियल को पढ़ने की सलाह देता हूं जिसमें हम साइट पर एक नया इवेंट जोड़ने का तरीका बताते हैं।


https://planb.academy/tutorials/contribution/resource/add-event-1d3df554-c2d8-4e93-853f-58f672c5e097


![conference](assets/01.webp)


- सबसे पहले, आपको GitHub पर एक अकाउंट बनाना होगा। अगर आपको अकाउंट बनाने का तरीका नहीं पता, तो हमने आपकी मदद के लिए एक विस्तृत ट्यूटोरियल तैयार किया है।


https://planb.academy/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c



- PlanB के डेटा से संबंधित GitHub रिपॉजिटरी (https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/conference) पर जाएं और `resources/conference/` सेक्शन में जाएं:

![conference](assets/02.webp)


- ऊपरी दाएं कोने पर स्थित `फ़ाइल जोड़ें` बटन पर क्लिक करें, फिर `नई फ़ाइल बनाएँ` पर क्लिक करें:

![conference](assets/03.webp)


- यदि आपने पहले कभी Plan ₿ Academy की सामग्री में योगदान नहीं दिया है, तो आपको मूल रिपॉजिटरी का fork बनाना होगा। किसी रिपॉजिटरी को Fork करने का अर्थ है अपने GitHub खाते पर उस रिपॉजिटरी की एक प्रति बनाना, जिससे आप मूल रिपॉजिटरी को प्रभावित किए बिना प्रोजेक्ट पर काम कर सकते हैं। `इस रिपॉजिटरी को Fork करें` बटन पर क्लिक करें:

![conference](assets/04.webp)


- इसके बाद आप GitHub के संपादन पृष्ठ पर पहुँच जाएँगे:

![conference](assets/05.webp)


- अपनी कॉन्फ्रेंस के लिए एक फ़ोल्डर बनाएँ। ऐसा करने के लिए, `अपनी फ़ाइल का नाम दें...` बॉक्स में, अपनी कॉन्फ्रेंस का नाम छोटे अक्षरों में लिखें और स्पेस की जगह डैश का इस्तेमाल करें। उदाहरण के लिए, यदि आपकी कॉन्फ्रेंस का नाम "Paris Bitcoin Conference" है, तो आपको `paris-bitcoin-conference` लिखना चाहिए। साथ ही, अपनी कॉन्फ्रेंस का वर्ष भी जोड़ें, जैसे: `paris-bitcoin-conference-2024`।

![conference](assets/06.webp)


- फोल्डर बनने की पुष्टि करने के लिए, उसी बॉक्स में अपने नाम के बाद एक स्लैश लगा दें, उदाहरण के लिए: `paris-bitcoin-conference-2024/`। स्लैश लगाने से फ़ाइल के बजाय स्वचालित रूप से एक फोल्डर बन जाता है।

![conference](assets/07.webp)


- इस फोल्डर में, आप `conference.yml` नाम की पहली YAML फ़ाइल बनाएंगे:

![conference](assets/08.webp)

इस टेम्पलेट का उपयोग करके इस फ़ाइल में अपने सम्मेलन से संबंधित जानकारी भरें:

```yaml
year:
name:
project:
location:
language:
-
links:
website:
twitter:
tags:
-
-
```


उदाहरण के लिए, आपकी YAML फ़ाइल कुछ इस तरह दिख सकती है:


```yaml
year: 2024-08
name: Paris Bitcoin Conference 2024
project: Paris Bitcoin Conference
location: Paris, France
language:
- fr
- en
links:
website: https://paris.bitcoin.fr/conference
twitter: https://twitter.com/ParisBitcoinConference
tags:
- International
- All Public
```


![conference](assets/09.webp)


यदि आपके संगठन के लिए अभी तक कोई "*प्रोजेक्ट*" पहचानकर्ता नहीं है, तो आप इस अन्य ट्यूटोरियल का अनुसरण करके इसे जोड़ सकते हैं।


https://planb.academy/tutorials/contribution/resource/add-builder-b5834c46-6dcc-4064-8d68-1ef529991d3d




- इस फ़ाइल में बदलाव करने के बाद, `बदलाव सेव करें...` बटन पर क्लिक करके उन्हें सेव करें:

![conference](assets/10.webp)


- अपने बदलावों के लिए एक शीर्षक और साथ ही एक संक्षिप्त विवरण जोड़ें:

![conference](assets/11.webp)


- हरे रंग के `प्रस्तावित परिवर्तन` बटन पर क्लिक करें:

![conference](assets/12.webp)


- इसके बाद आप एक ऐसे पेज पर पहुंचेंगे जहां आपके सभी बदलावों का सारांश दिया गया होगा:

![conference](assets/13.webp)


- ऊपर दाएं कोने में अपनी GitHub प्रोफ़ाइल तस्वीर पर क्लिक करें, फिर `Your Repositories` पर क्लिक करें:

![conference](assets/14.webp)


- Plan ₿ Academy रिपॉजिटरी में से अपना fork चुनें:

![conference](assets/15.webp)


- विंडो के शीर्ष पर आपको अपनी नई शाखा के साथ एक सूचना दिखाई देगी। इसका नाम संभवतः `patch-1` होगा। इस पर क्लिक करें:

![conference](assets/16.webp)


- आप अब अपनी कार्यशील शाखा पर हैं:

![conference](assets/17.webp)


- `resources/conference/` फोल्डर पर वापस जाएं और उस कॉन्फ्रेंस के फोल्डर का चयन करें जिसे आपने पिछले कमिट में बनाया था:

![conference](assets/18.webp)


- अपने सम्मेलन के फ़ोल्डर में, `फ़ाइल जोड़ें` बटन पर क्लिक करें, फिर `नई फ़ाइल बनाएँ` पर क्लिक करें:

![conference](assets/19.webp)


- इस नए फोल्डर का नाम `assets` रखें और इसके निर्माण की पुष्टि करने के लिए अंत में एक स्लैश `/` लगाएं:

![conference](assets/20.webp)


- इस `assets` फोल्डर में, `.gitkeep` नाम की एक फाइल बनाएं:

![conference](assets/21.webp)


- `परिवर्तनों को सेव करें...` बटन पर क्लिक करें:

![conference](assets/22.webp)


- कमिट का शीर्षक डिफ़ॉल्ट ही रहने दें, और सुनिश्चित करें कि `पैच-1 शाखा में सीधे कमिट करें` बॉक्स चेक किया हुआ है, फिर `परिवर्तन कमिट करें` पर क्लिक करें:

![conference](assets/23.webp)


- `assets` फ़ोल्डर पर वापस जाएँ:

![conference](assets/24.webp)


- `फ़ाइल जोड़ें` बटन पर क्लिक करें, फिर `फ़ाइलें अपलोड करें` पर क्लिक करें:

![conference](assets/25.webp)


- एक नया पेज खुलेगा। अपनी कॉन्फ्रेंस को दर्शाने वाली इमेज को ड्रैग करके ड्रॉप करें और यह इमेज Plan ₿ Academy साइट पर प्रदर्शित होगी: ![conference](assets/26.webp)
- यह एक लोगो, एक थंबनेल या यहां तक ​​कि एक पोस्टर भी हो सकता है:

![conference](assets/27.webp)


- इमेज अपलोड हो जाने के बाद, यह सुनिश्चित करें कि `Commit directly to the patch-1 branch` बॉक्स चेक किया हुआ है, फिर `Commit changes` पर क्लिक करें:

![conference](assets/28.webp)


- ध्यान दें, आपकी छवि का नाम `thumbnail` होना चाहिए और यह `.webp` प्रारूप में होनी चाहिए। इसलिए, फ़ाइल का पूरा नाम `thumbnail.webp` होना चाहिए।

![conference](assets/29.webp)


- अपने `assets` फोल्डर पर वापस जाएं और `.gitkeep` इंटरमीडिएट फाइल पर क्लिक करें:

![conference](assets/30.webp)


- फ़ाइल पर पहुँचने के बाद, ऊपरी दाएँ कोने में मौजूद तीन छोटे बिंदुओं पर क्लिक करें और फिर 'फ़ाइल हटाएं' पर क्लिक करें:

![conference](assets/31.webp)


- सुनिश्चित करें कि आप अभी भी उसी कार्यशील शाखा पर हैं, फिर `परिवर्तनों को कमिट करें` बटन पर क्लिक करें:

![conference](assets/32.webp)


- अपने कमिट में एक शीर्षक और विवरण जोड़ें, फिर `परिवर्तन कमिट करें` पर क्लिक करें:

![conference](assets/33.webp)


- अपने कॉन्फ्रेंस फोल्डर पर वापस जाएं:

![conference](assets/34.webp)


- `फ़ाइल जोड़ें` बटन पर क्लिक करें, फिर `नई फ़ाइल बनाएँ` पर क्लिक करें:

![conference](assets/35.webp)


- अपनी मातृभाषा के संकेत के साथ एक नई मार्कडाउन (.md) फ़ाइल बनाएँ। इस फ़ाइल का उपयोग आपके सम्मेलन के रीप्ले के लिए किया जाएगा। उदाहरण के लिए, यदि मैं सम्मेलनों का विवरण अंग्रेज़ी में लिखना चाहता हूँ, तो मैं इस फ़ाइल का नाम en.md रखूँगा।

![conference](assets/36.webp)


- इस मार्कडाउन फ़ाइल को इस टेम्पलेट का उपयोग करके भरें, जिसे आप अपने सम्मेलन के स्वरूप के अनुसार अनुकूलित कर सकते हैं:


```markdown
---
name: Paris Bitcoin Conference 2024
description: The largest Bitcoin conference in France with over 8,000 participants each year!
---

# Main Stage

## Friday morning

![video](https://youtu.be/XXXXXXXXXXXX)

## Friday afternoon

![video](https://youtu.be/XXXXXXXXXXXX)

## Saturday morning

![video](https://youtu.be/XXXXXXXXXXXX)

## Saturday afternoon

![video](https://youtu.be/XXXXXXXXXXXX)

# Workshop Room

## The Future of Bitcoin Mining: Challenges and Innovations

![video](https://youtu.be/XXXXXXXXXXXX)

Speaker: Satoshi Nakamoto, Satoshi Nakamoto

## Is Privacy Still Possible On Bitcoin?

![video](https://youtu.be/XXXXXXXXXXXX)

Speaker: Satoshi Nakamoto

## Bitcoin Core: Deep Dive into the Codebase

![video](https://youtu.be/XXXXXXXXXXXX)

Speaker: Satoshi Nakamoto, Satoshi Nakamoto, Satoshi Nakamoto, Satoshi Nakamoto

## Building and Securing Bitcoin Wallets With Miniscript

![video](https://youtu.be/XXXXXXXXXXXX)

Speaker: Satoshi Nakamoto
```


![conference](assets/37.webp)


- अपने दस्तावेज़ के प्रारंभ में, "प्रारंभिक भाग" में, `नाम:` फ़ील्ड में अपने सम्मेलन का नाम और रीप्ले का वर्ष भरें। `विवरण:` फ़ील्ड में, फ़ाइल की भाषा में अपने कार्यक्रम का संक्षिप्त विवरण लिखें। उदाहरण के लिए, `en.md` नामक फ़ाइल के लिए, विवरण अंग्रेज़ी में होना चाहिए। Plan ₿ Academy टीम अपने मॉडल का उपयोग करके आपके विवरण का अनुवाद करेगी।
- प्रथम स्तर के शीर्षक, जिन्हें `#` से चिह्नित किया जाता है, का उपयोग सम्मेलन को विभिन्न दृश्यों के अनुसार व्यवस्थित करने के लिए किया जाता है। उदाहरण के लिए, मुख्य मंच के लिए `# मुख्य मंच` और कार्यशालाओं के लिए समर्पित मंच के लिए `# कार्यशाला कक्ष`।



- दो बार `##` लगाकर चिह्नित किए गए द्वितीय-स्तरीय शीर्षकों का उपयोग विभिन्न रीप्ले वीडियो को अलग करने के लिए किया जाता है। यदि सम्मेलनों को आधे दिन तक लगातार फिल्माया गया था, तो उदाहरण के लिए, `## शुक्रवार सुबह` लिखें। यदि सम्मेलनों को अलग-अलग फिल्माया और प्रसारित किया गया था, तो द्वितीय-स्तरीय शीर्षक के साथ सीधे सम्मेलन का नाम लिखें।



- प्रत्येक दूसरे स्तर के शीर्षक के नीचे, संबंधित रीप्ले वीडियो का लिंक डालें। सिंटेक्स इस प्रकार होना चाहिए: `![video](https://youtu.be/XXXXXXXXXXXX)`, जिसमें `XXXXXXXXXXXX` को वास्तविक वीडियो लिंक से बदलें।



- यदि प्रारूप अनुमति देता है (व्यक्तिगत सम्मेलन), तो आप वक्ताओं के नाम जोड़ सकते हैं। ऐसा करने के लिए, वीडियो लिंक के नीचे `वक्ता:` फ़ील्ड में वक्ता का नाम या उपनाम लिखें। यदि एक से अधिक वक्ता हैं, तो प्रत्येक नाम को अल्पविराम से अलग करें, उदाहरण के लिए: `वक्ता: Satoshi Nakamoto, Satoshi Nakamoto, Satoshi Nakamoto, Satoshi Nakamoto`।


---


- इस फ़ाइल में आपके द्वारा किए गए बदलाव पूरे हो जाने के बाद, `बदलावों को सेव करें...` बटन पर क्लिक करके उन्हें सेव करें:

![conference](assets/38.webp)


- अपने द्वारा किए गए संशोधनों के लिए एक शीर्षक और साथ ही एक संक्षिप्त विवरण जोड़ें:

![conference](assets/39.webp)


- `परिवर्तनों को सेव करें` पर क्लिक करें:

![conference](assets/40.webp)


- अब आपका कॉन्फ्रेंस फोल्डर इस तरह दिखना चाहिए:

![conference](assets/41.webp)


- यदि सब कुछ आपकी संतुष्टि के अनुरूप है, तो अपने fork के मूल पर वापस लौटें:

![conference](assets/42.webp)


- आपको एक संदेश दिखाई देगा जो यह बताएगा कि आपकी शाखा में बदलाव किए गए हैं। `Compare & pull request` बटन पर क्लिक करें:

![conference](assets/43.webp)


- अपने जनसंपर्क के लिए एक स्पष्ट शीर्षक और विवरण जोड़ें:

![conference](assets/44.webp)


- `पुल रिक्वेस्ट बनाएं` बटन पर क्लिक करें:

![conference](assets/45.webp)

बधाई हो! आपका पीआर सफलतापूर्वक बन गया है। एक प्रशासक इसकी समीक्षा करेगा और यदि सब कुछ ठीक रहा, तो इसे Plan ₿ Academy के मुख्य रिपॉजिटरी में मर्ज कर देगा। कुछ दिनों बाद आपको अपनी कॉन्फ्रेंस के रीप्ले वेबसाइट पर दिखाई देने लगेंगे।


कृपया अपने पीआर की प्रगति पर नज़र रखें। संभव है कि कोई प्रशासक अतिरिक्त जानकारी मांगने के लिए टिप्पणी छोड़ दे। जब तक आपका पीआर मान्य नहीं हो जाता, आप इसे Plan ₿ Academy के GitHub रिपॉजिटरी पर `पुल रिक्वेस्ट` टैब के अंतर्गत देख सकते हैं।

![conference](assets/46.webp)


आपके बहुमूल्य योगदान के लिए बहुत-बहुत धन्यवाद! :)