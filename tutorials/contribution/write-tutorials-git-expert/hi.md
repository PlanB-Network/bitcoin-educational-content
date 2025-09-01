---
name: योगदान - Git ट्यूटोरियल (उन्नत)
description: उन्नत उपयोगकर्ताओं के लिए Git के साथ Plan ₿ Network पर ट्यूटोरियल प्रदान करने हेतु मार्गदर्शिका
---
![cover](assets/cover.webp)


नया ट्यूटोरियल जोड़ने के इस ट्यूटोरियल का अनुसरण करने से पहले, आपको कुछ प्रारंभिक चरण पूरे करने होंगे। यदि आपने अभी तक ऐसा नहीं किया है, तो कृपया पहले इस परिचयात्मक ट्यूटोरियल पर एक नज़र डालें, फिर यहाँ वापस आएँ:


https://planb.network/tutorials/contribution/content/write-tutorials-4d142a6a-9127-4ffb-9e0a-5aba29f169e2

आप पहले से ही:



- अपने ट्यूटोरियल के लिए एक विषय चुनें;
- [टेलीग्राम समूह](https://t.me/PlanBNetwork_ContentBuilder) या paolo@planb.network के माध्यम से Plan ₿ Network टीम से संपर्क किया;
- अपने योगदान उपकरण चुनें.


अनुभवी Git उपयोगकर्ताओं के लिए इस ट्यूटोरियल में, हम एक नया Plan ₿ Network ट्यूटोरियल पेश करने के लिए मुख्य चरणों और आवश्यक दिशा-निर्देशों का संक्षेप में वर्णन करेंगे। यदि आप Git और GitHub से अपरिचित हैं, तो मेरा सुझाव है कि आप इन 2 अन्य विस्तृत ट्यूटोरियल में से किसी एक का अनुसरण करें जो आपको चरण दर चरण आगे ले जाएगा:



- मध्यवर्ती (GitHub डेस्कटॉप):


https://planb.network/tutorials/contribution/content/write-tutorials-github-desktop-intermediate-4a36a052-1000-4191-890a-9a1dc65f8957


- शुरुआती (वेब ​​Interface):


https://planb.network/tutorials/contribution/content/write-tutorials-github-web-beginner-e64f8fed-4c0b-4225-9ebb-7fc5f1c01a79

## सुझाए गए उपकरण


मार्कडाउन फ़ाइलों को संपादित करने के लिए:



- ओब्सीडियन (मुक्त, खुला स्रोत नहीं)
- मार्क टेक्स्ट (निःशुल्क, मुक्त स्रोत)
- ज़ेटलर (निःशुल्क, मुक्त स्रोत)
- टाइपोरा (पेवेयर, ~€15, ओपन सोर्स नहीं)


गिट के लिए:



- Git (निःशुल्क, खुला स्रोत)
- GitHub डेस्कटॉप (निःशुल्क, मुक्त स्रोत)
- सोर्सट्री (निःशुल्क, ओपन-सोर्स नहीं)


YAML फ़ाइलों को संपादित करने के लिए:



- विज़ुअल स्टूडियो कोड (निःशुल्क, ओपन-सोर्स)
- सबलाइम टेक्स्ट (सीमाओं के साथ मुफ़्त, ओपन-सोर्स नहीं)


चित्र और दृश्य बनाने के लिए:



- कैनवा (मुफ़्त, भुगतान विकल्प सहित, ओपन-सोर्स नहीं)
- इंकस्केप (निःशुल्क, मुक्त स्रोत)
- पेनपोट (निःशुल्क, खुला स्रोत)


## वर्कफ़्लो


### 1 - अपना स्थानीय वातावरण कॉन्फ़िगर करें



- आपके पास [GitHub पर Plan ₿ Network रिपॉजिटरी](https://github.com/PlanB-Network/Bitcoin-educational-content) का अपना Fork होना चाहिए।
- अपने Fork की मुख्य शाखा (`dev`) को स्रोत रिपोजिटरी के साथ सिंक्रनाइज़ करें।
- अपने स्थानीय क्लोन को अद्यतन करें.


```
# Clone your fork (if not already done)
git clone https://github.com/<your-username>/bitcoin-educational-content.git
cd bitcoin-educational-content

# Add the source repository as a remote upstream
git remote add upstream https://github.com/PlanB-Network/bitcoin-educational-content.git

# Fetch the latest changes from the source repository
git fetch upstream

# Switch to the main 'dev' branch
git checkout dev

# Merge the changes from the source repository's 'dev' branch into your fork
git merge upstream/dev

# Push the updates to your fork on GitHub
git push origin dev
```


### 2 - एक नई शाखा बनाएँ



- सुनिश्चित करें कि आप `dev` शाखा पर हैं।
- वर्णनात्मक नाम (जैसे `tuto-Green-Wallet-loic`) के साथ एक नई शाखा बनाएँ।
- इस शाखा को अपने ऑनलाइन Fork पर प्रकाशित करें।


```
# Make sure you are on the 'dev' branch
git checkout dev

# Create a new branch with a descriptive name
git checkout -b tuto-green-wallet-loic

# Publish this branch to your online fork
git push -u origin tuto-green-wallet-loic
```


### 3 - ट्यूटोरियल दस्तावेज़ जोड़ें


***नोट:*** आप [मेरी पायथन GUI स्क्रिप्ट](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/scripts/tutorial-related/new-tutorial-creation) का उपयोग करके चरण 3 और 4 को स्वचालित कर सकते हैं। इसे अपने स्थानीय क्लोन में इसके फ़ोल्डर से सीधे चलाएँ, फिर GUI पर आवश्यक फ़ील्ड भरें। इसे इंस्टॉल करने और उपयोग करने के तरीके के बारे में अधिक जानकारी के लिए, [README](https://github.com/PlanB-Network/Bitcoin-educational-content/blob/dev/scripts/tutorial-related/new-tutorial-creation/README.md) देखें।


यदि आप इसे मैन्युअल रूप से करना पसंद करते हैं, तो इन चरणों का पालन करें:



- स्थानीय रिपोजिटरी में उपयुक्त फ़ोल्डर का पता लगाएं (उदाहरण के लिए `tutorials/Wallet`).
- ट्यूटोरियल को समर्पित एक निर्देशिका बनाएँ जिसका नाम स्पष्ट हो (उदाहरण के लिए `Green-Wallet`)। यह फ़ोल्डर नाम ट्यूटोरियल का URL पथ भी निर्धारित करेगा। यह लोअर केस में होना चाहिए, जिसमें कोई विशेष वर्ण (हाइफ़न को छोड़कर) और कोई स्पेस न हो।
- इस निर्देशिका में निम्नलिखित आइटम जोड़ें:
    - `assets` नामक एक सबफ़ोल्डर जिसमें निम्न शामिल है:
        - दो `.webp` छवियाँ:
            - `logo.webp`: ट्यूटोरियल लोगो (पृष्ठभूमि के साथ वर्गाकार प्रारूप)। यह लोगो प्रस्तुत किए गए सॉफ़्टवेयर या टूल का प्रतिनिधित्व करना चाहिए। यदि ट्यूटोरियल किसी टूल के लिए विशिष्ट नहीं है (उदाहरण: Mnemonic वाक्यांश बनाने के लिए एक सामान्य मार्गदर्शिका), तो आप एक उपयुक्त दृश्य चुन सकते हैं (उदाहरण: एक सामान्य आइकन)।
            - `cover.webp`: ट्यूटोरियल के प्रारंभ में प्रदर्शित कवर छवि।
        - ट्यूटोरियल की मूल भाषा का कोड रखने वाला एक सबफ़ोल्डर। उदाहरण के लिए, अगर ट्यूटोरियल अंग्रेज़ी में लिखा गया है, तो इस सबफ़ोल्डर का नाम `en' होना चाहिए। ट्यूटोरियल के सभी विज़ुअल (आरेख, चित्र, स्क्रीनशॉट, आदि) इस फ़ोल्डर में रखें।
    - मेटाडेटा (लेखक, टैग, श्रेणी, कठिनाई स्तर, आदि) युक्त `tutorial.yml` फ़ाइल.
    - ट्यूटोरियल युक्त मार्कडाउन फ़ाइल, जिसका नाम भाषा कोड के अनुसार रखा गया है (उदाहरण के लिए `fr.md`, `en.md`, आदि).


```
# Navigate to the appropriate folder
cd tutorials/wallet

# Create the directory dedicated to the tutorial
mkdir green-wallet
cd green-wallet

# Create the 'assets' subfolder
mkdir -p assets

# Create the subfolder for the original language code (e.g., 'en' for English)
mkdir -p assets/en

# Create the metadata file and the Markdown tutorial file (e.g., 'en.md' for English)
touch tutorial.yml en.md
```


### 4 - YAML फ़ाइल भरें



- `tutorial.yml` फ़ाइल को निम्न प्रकार पूरा करें:


```
id:

project_id:

tags:
-
-
-

category:

level:

professor_id:

# Proofreading metadata

original_language:
proofreading:
- language:
last_contribution_date:
urgency:
contributor_names:
-
reward:
```


आवश्यक फ़ील्ड इस प्रकार हैं:



- id**: एक UUID (_यूनिवर्सली यूनिक आइडेंटिफ़ायर_) जो ट्यूटोरियल को विशिष्ट रूप से पहचानता है। आप इसे [ऑनलाइन टूल](https://www.uuidgenerator.net/version4) का उपयोग करके generate कर सकते हैं। एकमात्र आवश्यकता यह है कि यह UUID प्लेटफ़ॉर्म पर किसी अन्य UUID के साथ टकराव से बचने के लिए यादृच्छिक हो;



- project_id**: ट्यूटोरियल में प्रस्तुत टूल के पीछे कंपनी या संगठन का UUID [प्रोजेक्ट सूची से](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/resources/projects)। उदाहरण के लिए, यदि आप Green Wallet सॉफ़्टवेयर के बारे में एक ट्यूटोरियल बना रहे हैं, तो आप इस `project_id` को निम्न फ़ाइल में पा सकते हैं: `Bitcoin-educational-content/resources/projects/blockstream/project.yml`। यह जानकारी आपके ट्यूटोरियल की YAML फ़ाइल में इसलिए जोड़ी जाती है क्योंकि Plan ₿ Network Bitcoin या संबंधित प्रोजेक्ट पर काम करने वाली सभी कंपनियों और संगठनों का डेटाबेस बनाए रखता है। अपने ट्यूटोरियल से जुड़ी इकाई का `project_id` जोड़कर, आप दो Elements के बीच एक लिंक बनाते हैं;



- टैग**: ट्यूटोरियल सामग्री से संबंधित 2 या 3 प्रासंगिक कीवर्ड, विशेष रूप से [Plan ₿ Network टैग सूची से](https://github.com/PlanB-Network/Bitcoin-educational-content/blob/dev/docs/50-planb-tags.md) चुने गए;



- श्रेणी**: Plan ₿ Network वेबसाइट संरचना के अनुसार ट्यूटोरियल सामग्री के अनुरूप उप-श्रेणी (उदाहरण के लिए, वॉलेट के लिए: `डेस्कटॉप`, `हार्डवेयर`, `मोबाइल`, `बैकअप`);



- स्तर**: ट्यूटोरियल का कठिनाई स्तर, निम्न में से चुना गया:
    - `शुरुआती`
    - `मध्यवर्ती`
    - `उन्नत`
    - `विशेषज्ञ`



- professor_id**: आपका `professor_id` (UUID) जैसा कि [आपके प्रोफेसर प्रोफ़ाइल](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/professors) पर प्रदर्शित है;



- original_language**: ट्यूटोरियल की मूल भाषा (जैसे, `fr`, `en`, आदि);



- प्रूफ़रीडिंग**: प्रूफ़रीडिंग प्रक्रिया के बारे में जानकारी। पहला भाग पूरा करें, क्योंकि अपने स्वयं के ट्यूटोरियल को प्रूफ़रीडिंग करना प्रथम सत्यापन के रूप में गिना जाता है:
    - भाषा**: प्रूफ़रीडिंग का भाषा कोड (जैसे, `fr`, `en`, आदि).
    - last_contribution_date**: दिन की तारीख.
    - तात्कालिकता**: 1
    - योगदानकर्ता_नाम**: आपकी GitHub आईडी.
    - इनाम**: 0


अपने शिक्षक आईडी के बारे में अधिक जानकारी के लिए कृपया संबंधित ट्यूटोरियल देखें:


https://planb.network/tutorials/contribution/others/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4

```
id: e84edaa9-fb65-48c1-a357-8a5f27996143

project_id: 3b2f45e6-d612-412c-95ba-cf65b49aa5b8

tags:
- wallets
- software
- keys

category: mobile

level: beginner

professor_id: 6516474c-c190-41f2-b2ab-3d452ce7bdf0

# Proofreading metadata

original_language: fr
proofreading:
- language: fr
last_contribution_date: 2024-11-20
urgency: 1
contributor_names:
- LoicPandul
reward: 0
```


### 5 - सामग्री लिखें



- मार्कडाउन फ़ाइल गुणों को पूरा करें:
    - शीर्षक (`नाम`).
    - एक संक्षिप्त विवरण (`विवरण`).
- मार्कडाउन सिंटैक्स का उपयोग करके ट्यूटोरियल के शीर्ष पर कवर छवि जोड़ें (दिखाए गए टूल के नाम के साथ "Green" को प्रतिस्थापित करें):


```
![cover-green](assets/cover.webp)
```



- ट्यूटोरियल सामग्री को मार्कडाउन में लिखें:
    - अच्छी तरह से संरचित शीर्षकों (`##`), सूचियों और पैराग्राफों का उपयोग करें।
    - मार्कडाउन सिंटैक्स का उपयोग करके दृश्य सम्मिलित करें:


```
![nom-image](assets/en/001.webp)
```




- आरेखों और छवियों को `/assets` में संबंधित भाषा सबफ़ोल्डर में रखें।


### 6 - ट्यूटोरियल को सेव करें और सबमिट करें



- वर्णनात्मक संदेश के साथ कमिट बनाकर अपने परिवर्तनों को स्थानीय रूप से सहेजें।
- परिवर्तनों को अपने GitHub Fork पर पुश करें.


```
# Create a commit with a descriptive message
git commit -m "Added green-wallet tutorial"

# Push your changes to your fork
git push origin tuto-green-wallet-loic
```



- एक बार काम पूरा हो जाने पर, अपने संशोधनों के एकीकरण का प्रस्ताव देने के लिए GitHub पर एक पुल अनुरोध (PR) बनाएं।
- पी.आर. में शीर्षक और संक्षिप्त विवरण जोड़ें। टिप्पणी में संबंधित अंक संख्या का उल्लेख करें।


### 7 - प्रूफरीडिंग और विलय



- किसी व्यवस्थापक से सत्यापन या फीडबैक की प्रतीक्षा करें।
- यदि आवश्यक हो तो सुधार करें और नई प्रतिबद्धताएं प्रस्तुत करें।


```
# Create a commit describing the corrections made
git commit -m "Corrections following the review of the green-wallet tutorial"

# Push the corrections to your fork
git push origin tuto-green-wallet-loic
```



- एक बार पीआर विलय हो जाने पर, आप अपनी कार्यशील शाखा को हटा सकते हैं।


## सामग्री निर्माण मानक



- प्लेटफ़ॉर्म पर समर्थित स्वरूपण**:
    - क्लासिक मार्कडाउन: सूचियाँ, लिंक, चित्र, उद्धरण, बोल्ड, इटैलिक्स, आदि।
    - LaTeX (केवल ब्लॉक, इनलाइन नहीं): `$$` द्वारा सीमांकित.
    - इनलाइन कोड: एकल बैकटिक वाला वाक्यविन्यास।
    - कोड ब्लॉक: तीन बैकटिक्स के साथ वाक्यविन्यास, उदाहरण के लिए:


```
print("Hello, Bitcoin!")
```



- चित्र एवं आरेख**:
    - सभी छवियाँ WebP प्रारूप में होनी चाहिए। यदि आवश्यक हो तो उन्हें परिवर्तित करने के लिए इस निःशुल्क टूल का उपयोग करें: [ImagesConverter](https://github.com/LoicPandul/ImagesConverter)।
    - विज़ुअल को 2 या 3 अंकों वाला नाम दें (उदाहरण के लिए `001.webp`, `002.webp`).
    - मोबाइल या Hardware Wallet ट्यूटोरियल के लिए, मॉक-अप का उपयोग करें।
    - केवल स्व-निर्मित या रॉयल्टी-मुक्त दृश्यों का ही उपयोग करें।
    - सुनिश्चित करें कि वे प्रासंगिक और उच्च गुणवत्ता वाले हों।
- ग्राफिक चार्टर**:
    - फ़ॉन्ट: [रूबिक](https://fonts.google.com/specimen/IBM+Plex+Sans).
    - रंग Plan ₿ Network:
        - नारंगी: `#FF5C00`
        - काला: `#000000`
        - सफेद: `#FFFFFF`


यदि आपको अपना ट्यूटोरियल सबमिट करने में तकनीकी कठिनाइयाँ आ रही हैं, तो कृपया [योगदान के लिए हमारे समर्पित टेलीग्राम समूह](https://t.me/PlanBNetwork_ContentBuilder) पर मदद माँगने में संकोच न करें। बहुत-बहुत धन्यवाद!