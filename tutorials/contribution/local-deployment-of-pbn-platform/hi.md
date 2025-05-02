---
name: Plan ₿ Network प्लेटफ़ॉर्म को स्थानीय रूप से चलाने के लिए मार्गदर्शिका
description: आप मेरे द्वारा सामग्री योगदान या Plan ₿ Network पर शैक्षिक सामग्री की प्रूफरीडिंग/समीक्षा का परीक्षण करने के लिए स्थानीय परिवेश में Plan ₿ Network कैसे चला सकते हैं?
---
![github](assets/cover.webp)


## सारांश


यह ट्यूटोरियल Docker, डमी कुंजियों और कस्टम रिपोजिटरी कॉन्फ़िगरेशन का उपयोग करके आपके स्थानीय मशीन पर Plan ₿ Network से Bitcoin लर्निंग मैनेजमेंट सिस्टम स्थापित करने के लिए चरण-दर-चरण निर्देश प्रदान करता है।


यदि आपको उपरोक्त भाग समझ में नहीं आया, तो चिंता न करें - यह ट्यूटोरियल आपके लिए है!


---

## **Bitcoin लर्निंग मैनेजमेंट सिस्टम को स्थानीय रूप से कैसे चलाएं**


यह ट्यूटोरियल प्लेटफ़ॉर्म सेट अप करने, डमी कुंजियों को संभालने और रिपॉजिटरी को कस्टमाइज़ करने के लिए विस्तृत चरण प्रदान करता है। आम समस्याओं से बचने और अपने स्थानीय वातावरण को ठीक से कॉन्फ़िगर करने के लिए नीचे दिए गए चरणों का पालन करें।



**1. पूर्वापेक्षाएँ**


- लिनक्स मशीन पर डॉकर और डॉकर कम्पोज़ स्थापित है (यह विंडोज़ पर भी काम करता हुआ बताया गया है)।
- पर्याप्त `nodejs` संस्करण (परीक्षण किया गया: 22.12.0)
- आपके सिस्टम पर `pnpm` स्थापित है.
- Git को रिपॉजिटरीज की क्लोनिंग के लिए कॉन्फ़िगर किया गया।



**2. रिपॉजिटरी को क्लोन करें**

रिपॉजिटरी को अपनी स्थानीय मशीन पर क्लोन करें:


गिट क्लोन [https://github.com/PlanB-Network/Bitcoin-learning-management-system](https://github.com/PlanB-Network/Bitcoin-learning-management-system￼cd)

[सीडी](https://github.com/PlanB-Network/Bitcoin-learning-management-system￼सीडी) Bitcoin-learning-management-system


```bash
git clone https://github.com/PlanB-Network/bitcoin-learning-management-system
cd bitcoin-learning-management-system
```



**3. पर्यावरण चर सेट करें**


1\. `.env.example` फ़ाइल की प्रतिलिपि बनाएँ:


```bash
cp .env.example .env
```


1. `.env` फ़ाइल को संपादित करें, नाम के .example भाग को हटा दें, अब आपको आवश्यक चरों के लिए डमी कुंजियाँ शामिल करनी होंगी। उदाहरण:


⚠️ यह एक अनिवार्य कदम है, इसे छोड़ने से कुछ कंटेनरों के बीच कनेक्शन अस्वीकार जैसी त्रुटियां हो सकती हैं।


फ़ाइल में अपना समर्पित Github PAT भी जोड़ना न भूलें



```markdown
# Dummy Keys for External Services
SBP_API_KEY=dummyApiKey
SBP_HMAC_SECRET=dummyHmacSecret
STRIPE_SECRET=sk_test_dummySecretKey12345
STRIPE_ENDPOINT_SECRET=dummyEndpointSecret12345
SENDGRID_KEY=dummySendgridKey
```


---

**4. निर्भरताएं स्थापित करें**


सुनिश्चित करें कि आपने एक उपयुक्त नोडजेएस संस्करण स्थापित किया है। 2024-12 तक, v22.12.0 (LTS) काम करने में सिद्ध हो चुका है।



⚠️ उबंटू 22.04 रिपॉजिटरी नोडज संस्करण 12.22.9 है: आपको pnpm स्थापित करने की अनुमति देने के लिए बहुत पुराना है



नोडजेएस स्थापित करने के लिए, निर्देश यहां पाएं (https://nodejs.org/en/download/package-manager); उदाहरण के लिए आप `nvm` स्थापना विधि का उपयोग करना चुन सकते हैं।


---

आवश्यक पैकेजों के pnpm इंस्टॉलेशन चरण को शुरू करने से पहले, सुनिश्चित करें कि सभी निर्भरताएं इंस्टॉल हो गई हैं, आप निम्न कमांड चलाकर ऐसा कर सकते हैं:


```bash
sudo apt install libcairo2-dev libjpeg-dev libpango1.0-dev libgif-dev build-essential g++ libpixman-1-dev
```


---

अपने `../Bitcoin-learning-management-system/` फ़ोल्डर के अंदर, `pnpm` को स्थापित करने के लिए निम्न कमांड चलाएँ


```bash
pnpm install
```


__टिप:__समय-समय पर निर्भरताओं और pnpm दोनों को अपडेट करना याद रखें



**5. कंटेनर चलाएं**

अपने `../Bitcoin-learning-management-system/` फ़ोल्डर के अंदर, Docker के साथ विकास वातावरण प्रारंभ करें:


```bash
docker compose up --build -V
```

आप इस अगले कमांड को भी इसी तरह चलाएंगे, आपको अपने टर्मिनल में लॉग दिखाई नहीं देंगे।

```bash
docker compose up -d --build -V
```


इससे डॉकर्स से सभी आवश्यक कंटेनरों का निर्माण और प्रारंभ हो जाएगा।


**6. एप्लिकेशन तक पहुंचें**

एक बार कंटेनर चलने लगे, तो फ्रंटएंड तक पहुंचें:

\[<http://localhost:8181](http://localhost:8181)>


![Plan ₿ Network Local](assets/en/1.webp)


ध्यान दें: यदि आप कोई स्रोत फ़ाइल बदलते हैं तो ऐप स्वचालित रूप से पुनः लोड हो जाएगा।



**7.** अपना डेटाबेस Schema सेट करें


पहली बार चलाने पर, आपको DB माइग्रेशन चलाने की आवश्यकता होगी।


ऐसा करने के लिए, माइग्रेशन स्क्रिप्ट चलाएँ: `pnpm run dev:db:migrate`


```markdown
pnpm run dev:db:migrate
```


**8. रिपॉजिटरी से डेटा आयात करें**

डेटाबेस में डेटा आयात करने के लिए, API से अनुरोध करें:


```markdown
curl -X POST http://localhost:3000/api/github/sync
```


**9. सिंक वॉल्यूम एक्सेस समस्याओं को ठीक करें**

यदि आपको `cdn` और `sync` वॉल्यूम के साथ पहुँच संबंधी समस्याएँ आती हैं, तो चलाएँ:


```markdown
docker exec --user=root bitcoin-learning-management-system-api-1 chmod 777 /tmp/{sync,cdn}
```


तो फिर:


```markdown
curl -X POST http://localhost:3000/api/github/sync
```


![Plan ₿ Network Local](assets/en/2.webp)



**10. रिपॉजिटरी को अनुकूलित करें (वैकल्पिक)**

यदि आपको Fork या किसी विशिष्ट शाखा का उपयोग करने की आवश्यकता है:

1. निम्नलिखित चरों को अद्यतन करने के लिए `.env` फ़ाइल को संपादित करें:


```markdown
DATA_REPOSITORY_URL=https://github.com/<your-username>/bitcoin-educational-content.git
DATA_REPOSITORY_BRANCH=<your-branch>
PRIVATE_DATA_REPOSITORY_URL=https://github.com/<your-username>/planB-premium-content.git
PRIVATE_DATA_REPOSITORY_BRANCH=<your-branch>
```


2\. Docker पुनः आरंभ करें:


```markdown
docker compose down -v
docker compose up --build -V
```


3\. रिपोजिटरी डेटा को पुनः सिंक करें:


```markdown
curl -X POST http://localhost:3000/api/github/sync
```


यह ट्यूटोरियल सुनिश्चित करता है कि प्लेटफ़ॉर्म को डमी कुंजियों, स्थापित निर्भरताओं और आवश्यकतानुसार अनुकूलित रिपॉजिटरी के साथ सही ढंग से सेट किया गया है। 🎉 आपके सेटअप के साथ शुभकामनाएँ!


**अतिरिक्त सहायता के लिए आदेश**


सभी कंटेनर बंद करो


```
docker compose down
```


सभी मौजूदा कंटेनरों और वॉल्यूम को छाँटें


```
docker container prune -f
docker volume prune --all
```


आधिकारिक गाइड और लंच सिंक स्क्रिप्ट में प्रयुक्त समान कमांड के साथ कंटेनरों को पुनः बनाएं:


```
docker-compose up --build -V
curl -X POST http://localhost:3000/api/github/sync
```