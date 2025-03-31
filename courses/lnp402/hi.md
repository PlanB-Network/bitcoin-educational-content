---
name: लाइटनिंग के साथ SDK पर विकास करना
goal: अपने लाइटनिंग विकास कौशल को उन्नत करें मध्यम स्तर के Rust और SDK प्रशिक्षण के साथ।
objectives: 

  - आपको Rust भाषा की आदत डालनी होगी।
  - Bitcoin को विकसित करने के लिए Rust का उपयोग क्यों करें, इसे समझें।
  - SDK का आधार प्राप्त करें

---
# अपने LN डेवलपमेंट स्किल्स को आगे बढ़ाना

SDK के साथ आपके LN सफर में आपका स्वागत है।

इस कोर्स में, आप Rust किताब की बुनियादी बातें सीखेंगे, फिर कुछ LN प्रोग्रामिंग को SDKs के साथ समझेंगे, और अंत में कुछ व्यावहारिक अभ्यास करेंगे। हमारे विभिन्न पृष्ठभूमियों से आए शिक्षक आपको व्यावहारिक कौशल की ओर मार्गदर्शन करेंगे और आज के LN इंजीनियरों को अक्सर जिन चुनौतियों का सामना करना पड़ता है, उन्हें समझाएंगे।

यह कोर्स अक्टूबर 2023 में LN टस्कनी इवेंट के दौरान Fulgur'Ventures द्वारा आयोजित एक लाइव सेमिनार में फिल्माया गया था।

कोर्स का आनंद लें!

+++
# परिचय

<partId>594ab43f-7216-5326-ab41-f92b85be4581</partId>

## पाठ्यक्रम का पाठ्यक्रम और परिचय

<chapterId>36526df2-66a2-58df-8f38-378fb553f08c</chapterId>

### परिचय

इस उन्नत प्रोग्रामिंग कोर्स में आपका स्वागत है, जो एसडीके पर आधारित है। इस प्रशिक्षण में, आप सबसे पहले Rust की बुनियादी बातें सीखेंगे, फिर BTC और Rust पर ध्यान केंद्रित करेंगे, और अंत में एसडीके का उपयोग करके कुछ व्यावहारिक अभ्यास करेंगे।

यह प्रशिक्षण फिलहाल केवल अंग्रेज़ी में उपलब्ध होगा और यह पिछले अक्टूबर में टस्कनी में फुलगुर वेंचर द्वारा आयोजित एक लाइव सेमिनार का हिस्सा था। लाइव इवेंट का कार्यक्रम नीचे दिया गया है, और यह प्रशिक्षण केवल पहले सप्ताह पर केंद्रित होगा। दूसरी छमाही RGB पर लक्षित थी और इसे RGB कोर्स में पाया जा सकता है।

### शिक्षक

इस कार्यक्रम का हिस्सा बनने वाले हमारे शिक्षकों का बहुत-बहुत धन्यवाद:


- अलेकोस: "अरे, मैं एक इतालवी कोडर और हैकर हूँ। मैंने बिटकॉइनडेवकिट, मैजिकलबिटकॉइन और h4ckbs जैसे विभिन्न प्रोजेक्ट्स पर काम किया है।"
- आंद्रेई: "LIPA में बिजली विशेषज्ञ"
- गैब्रियल: "मैं कोड लिखता हूँ और कुछ काम करता हूँ।"
- जेसी डी विट: "Lightning Network उत्साही | डेवलपर | ब्रीज़"

### सेमिनार का कार्यक्रम

LN टस्कनी इवेंट का पहला हफ्ता

![image](assets/1.webp)

इस कोर्स को पूरा करने के बाद, अगर आप आगे की ट्रेनिंग में रुचि रखते हैं, तो यहाँ कार्यक्रम का दूसरा हिस्सा है:

![image](assets/2.webp)

आपकी पढ़ाई के लिए शुभकामनाएँ।

# Rust किताब के साथ कोडिंग करना सीखें।

<partId>152b58c9-fb33-5d3b-9c15-64919869aa34</partId>

## Rust का परिचय (1/7)

<chapterId>af7108eb-4974-5ac2-9784-d2a5c0d77a45</chapterId>

आपका प्रशिक्षण अक्टूबर 2023 तक के डेटा पर आधारित है।

![video](https://www.youtube.com/watch?v=aZYhDXE_Gas)

## Rust का परिचय (2/7)

<chapterId>918ca359-c123-5414-af01-253016670f3a</chapterId>

![video](https://youtu.be/Xm8eCv4LQPc)

## Rust का परिचय (3/7)

<chapterId>0278ed13-68b6-59e1-97c5-f8dde505549b</chapterId>

![video](https://youtu.be/R8NeHvHT0uc)

## Rust का परिचय (4/7)

<chapterId>915e523a-8fbd-5789-ab42-99b56a2a16c3</chapterId>

![video](https://youtu.be/et8pKvYiO4c)

## Rust का परिचय (5/7)

<chapterId>96d54999-cdbc-5601-acac-1bc7acbe2eb7</chapterId>

![video](https://youtu.be/PxQkVmxOc40)

## परिचय Rust (6/7)

<chapterId>a66c63ed-9514-51d1-b3a0-c8edb57603bb</chapterId>

![video](https://youtu.be/3C6hl9BW-Ho)

## Rust का परिचय (7/7)

<chapterId>21cf8dab-239a-580a-85cd-34326aeb1b26</chapterId>

![video](https://youtu.be/SBDcb_AauHM)

# Rust और BTC

<partId>0f4f2ff0-7f41-5ce3-8f64-9ecff69c5355</partId>

## Rust को Bitcoin पर क्यों चुना गया?

<chapterId>92f13f36-70bd-5b00-8c6c-fcd1a1bd1531</chapterId>

![video](https://youtu.be/veLj2w6ulpc)

## त्रुटि मॉडल

<chapterId>1a648363-0aff-54dd-a79d-ead75231e5d6</chapterId>

![video](https://youtu.be/X3VKhLtKTRU)

## आपको अक्टूबर 2023 तक के डेटा पर प्रशिक्षित किया गया है।

<chapterId>fe1be3e3-2288-5a10-b64b-9ba72fb985d1</chapterId>

![video](https://youtu.be/zro9GQpJrH0)

## ऐसिंक ट्रेट्स

<chapterId>e1610abe-574c-5995-abe4-a92b0dca4c93</chapterId>

![video](https://youtu.be/cz66eTfk0lw)

# SDK के साथ LNP/BP विकसित करना

<partId>42e8e0f8-1c07-5c71-8378-c57afb38e25d</partId>

## SDK पर LN नोड

<chapterId>643e4670-bb1f-581f-a102-f84e8e5d2a02</chapterId>

![video](https://youtu.be/aEzpxuhLdeo)

## ब्रीज़ एसडीके

<chapterId>52f20a4d-7d81-58e4-be00-9d39334352af</chapterId>

![video](https://youtu.be/M3ad9BE6ovo)

## लिपा के लिए हरी झंडी

<chapterId>7ba30435-d26e-5e6f-a973-94080d44bf27</chapterId>

![video](https://youtu.be/gKiIPF4apeE)

## ब्रीज़ एसडीके लिपा के लिए

<chapterId>93d87d63-dd7b-5e05-ad2e-dda12915ea32</chapterId>

![video](https://youtu.be/6VaIVvBKjLY)

# निष्कर्ष

<partId>aff1e861-e6a3-58ad-af6a-33ceaedbda99</partId>

## समीक्षाएँ और रेटिंग्स

<chapterId>9331e519-9e5c-5639-9d0d-055587d8ba4c</chapterId>

<isCourseReview>true</isCourseReview>
## निष्कर्ष

<chapterId>d47b792e-d269-595b-9290-4788aba6e298</chapterId>

<isCourseConclusion>true</isCourseConclusion>