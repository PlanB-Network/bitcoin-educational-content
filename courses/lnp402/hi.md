---
name: लाइटनिंग पर SDK के साथ डेवलपिंग
goal: अपनी लाइटनिंग डेवलपमेंट स्किल्स को इंटरमीडिएट Rust और SDK ट्रेनिंग के साथ आगे बढ़ाएं।
objectives: 

  - Rust भाषा की आदत डालो
  - समझिए कि Bitcoin को विकसित करने के लिए Rust का उपयोग क्यों करें
  - एसडीके का आधार प्राप्त करें

---
# अपने LN डेव स्किल्स को आगे बढ़ाएं

आपके LN सफर में SDK के साथ स्वागत है।

इस कोर्स में, आप Rust बुक की बेसिक्स सीखेंगे, फिर कुछ LN प्रोग्रामिंग SDKs का उपयोग करके करेंगे, और आखिर में कुछ प्रैक्टिकल एक्सरसाइज के साथ खत्म करेंगे। हमारे अलग-अलग बैकग्राउंड के टीचर्स आपको प्रैक्टिकल स्किल्स की तरफ गाइड करेंगे और आजकल के LN इंजीनियर्स के सामने आने वाली चुनौतियों के बारे में समझाएँगे।

यह कोर्स अक्टूबर 2023 में LN टस्कनी इवेंट के दौरान Fulgur'Ventures द्वारा आयोजित एक LIVE सेमिनार के दौरान फिल्माया गया था।

कोर्स का मजा लो!

+++
# परिचय

<partId>594ab43f-7216-5326-ab41-f92b85be4581</partId>

## कोर्स पाठ्यक्रम और परिचय

<chapterId>36526df2-66a2-58df-8f38-378fb553f08c</chapterId>

### परिचय

Rust पर इस एडवांस्ड प्रोग्रामिंग कोर्स में आपका स्वागत है। इस ट्रेनिंग में, आप पहले Rust की बेसिक्स सीखेंगे, फिर BTC और Rust पर फोकस करेंगे, और आखिर में SDKs का इस्तेमाल करके प्रैक्टिकल एक्सरसाइज के साथ खत्म करेंगे।

यह ट्रेनिंग अभी के लिए सिर्फ़ अंग्रेज़ी में उपलब्ध होगी और यह पिछले अक्टूबर में टस्कनी में Fulgure Venture द्वारा आयोजित एक लाइव सेमिनार का हिस्सा थी। लाइव इवेंट का प्रोग्राम नीचे दिया गया है, और यह ट्रेनिंग सिर्फ़ पहले हफ़्ते पर केंद्रित होगी। दूसरा हिस्सा RGB के लिए था और उसे RGB कोर्स में देखा जा सकता है।

### गुरु / शिक्षक

इस कार्यक्रम का हिस्सा रहे हमारे सभी शिक्षकों को बहुत-बहुत धन्यवाद:


- अलेकोस : "अरे, मैं एक इटैलियन कोडर और हैकर हूँ। मैंने बिटकॉइनडेवकिट, मैजिकलबिटकॉइन और हैकबीएस जैसे कई प्रोजेक्ट्स पर काम किया है।"
- अंद्रेई : "लिपा में बिजली के विशेषज्ञ"
- गेब्रियल: "मैं कोड लिखता हूँ और वगैरह करता हूँ।"
- जेस्से डी विट : "Lightning Network उत्साही | डेवलपर | ब्रीज़"

### सेमिनार शेड्यूल

जीडब्ल्यू-12 टस्कनी इवेंट का पहला हफ्ता

![image](assets/1.webp)

एक बार जब आप यह कोर्स पूरा कर लें, और अगर आप आगे की ट्रेनिंग में दिलचस्पी रखते हैं, तो यह रहा शेड्यूल का दूसरा हिस्सा:

![image](assets/2.webp)

पढ़ाई में अच्छी किस्मत मिले।

# Rust किताब से कोडिंग सीखो

<partId>152b58c9-fb33-5d3b-9c15-64919869aa34</partId>

## जीडब्ल्यू-14 का परिचय (1/7)

<chapterId>af7108eb-4974-5ac2-9784-d2a5c0d77a45</chapterId>

<professorId>e7e63d59-ea19-4960-9446-61bd4dcc98f0</professorId>  

(Note: Since this is a unique identifier code, it remains unchanged in translation as per technical/conventional practices. In Hindi context, we'd pronounce it as "प्रोफेसर आईडी: ई-7-ई-63-डी-59...")

:::video id=12a518cf-64be-43f1-b6d4-f6592a1324ea:::

## Rust का परिचय (2/7)

<chapterId>918ca359-c123-5414-af01-253016670f3a</chapterId>

:::video id=8ed76bae-7c30-4aac-9f28-bb4cbb9180e4:::

## जीडब्ल्यू-16 का परिचय (3/7)

<chapterId>0278ed13-68b6-59e1-97c5-f8dde505549b</chapterId>

:::video id=c78a543f-1462-43a1-9845-889d310d31a4:::

## Rust का परिचय (4/7)

<chapterId>915e523a-8fbd-5789-ab42-99b56a2a16c3</chapterId>

:::video id=0f2f6f68-52ca-474f-a64f-ba61cdc92821:::

## Rust का परिचय (5/7)

<chapterId>96d54999-cdbc-5601-acac-1bc7acbe2eb7</chapterId>

:::video id=5514da77-5b71-4763-96b8-49eb21291c2b:::

## Rust का परिचय (6/7)

<chapterId>a66c63ed-9514-51d1-b3a0-c8edb57603bb</chapterId>

:::video id=44c681d1-d154-4240-b3e8-15590cbfcbd2:::

## जीडब्ल्यू-20 का परिचय (7/7)

<chapterId>21cf8dab-239a-580a-85cd-34326aeb1b26</chapterId>

:::video id=5e96914d-df02-4781-ae54-b06008952301:::

# जीडब्ल्यू-21 और बीटीसी

<partId>0f4f2ff0-7f41-5ce3-8f64-9ecff69c5355</partId>

## Rust per Bitcoin का मतलब क्या है?

<chapterId>92f13f36-70bd-5b00-8c6c-fcd1a1bd1531</chapterId>

:::video id=f59c4951-e109-4c70-b7da-41721e50ab04:::

## त्रुटि मॉडल

<chapterId>1a648363-0aff-54dd-a79d-ead75231e5d6</chapterId>

:::video id=9fac0184-8443-4c36-8afd-8acb21fb43c3:::

## अनफिट

<chapterId>fe1be3e3-2288-5a10-b64b-9ba72fb985d1</chapterId>

:::video id=b1a0f5f6-fc29-4b83-9c09-0b24711654e2:::

## एसिंक ट्रेट्स

<chapterId>e1610abe-574c-5995-abe4-a92b0dca4c93</chapterId>

:::video id=8926dd48-3613-43b6-a509-60ba26ec337f:::

# LNP/BP को SDK के साथ विकसित करना

<partId>42e8e0f8-1c07-5c71-8378-c57afb38e25d</partId>

## जीडब्ल्यू-24 नोड एसडीके पर

<chapterId>643e4670-bb1f-581f-a102-f84e8e5d2a02</chapterId>

:::video id=94b9bee6-154e-4b9c-a8ce-5e2d9e9656a2:::

## ब्रीज़ एसडीके

<chapterId>52f20a4d-7d81-58e4-be00-9d39334352af</chapterId>

:::video id=68d1f253-6210-4eab-8329-b676e5772eac:::

## लिपा के लिए हरी झंडी

<chapterId>7ba30435-d26e-5e6f-a973-94080d44bf27</chapterId>

:::video id=c3dec3df-1416-4761-b7c8-e1d66d27e390:::

## लिपा के लिए ब्रीज़ एसडीके

<chapterId>93d87d63-dd7b-5e05-ad2e-dda12915ea32</chapterId>

:::video id=f2770a37-a22f-43d7-9334-8de60eaacff8:::

# समापन

<partId>aff1e861-e6a3-58ad-af6a-33ceaedbda99</partId>

## समीक्षाएँ और रेटिंग्स

<chapterId>9331e519-9e5c-5639-9d0d-055587d8ba4c</chapterId>

<isCourseReview>true</isCourseReview>
## अंत

<chapterId>d47b792e-d269-595b-9290-4788aba6e298</chapterId>

<isCourseConclusion>true</isCourseConclusion>