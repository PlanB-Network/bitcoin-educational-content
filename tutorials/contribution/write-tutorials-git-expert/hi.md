---
name: योगदान - गिट ट्यूटोरियल (उन्नत)
description: उन्नत उपयोगकर्ताओं के लिए यह मार्गदर्शिका Plan ₿ Academy और Git पर ट्यूटोरियल प्रदान करती है।
---
![cover](assets/cover.webp)


नया ट्यूटोरियल जोड़ने के इस ट्यूटोरियल को फॉलो करने से पहले, आपको कुछ प्रारंभिक चरण पूरे करने होंगे। यदि आपने अभी तक ऐसा नहीं किया है, तो कृपया पहले इस परिचयात्मक ट्यूटोरियल को देखें, फिर यहां वापस आएं:


https://planb.academy/tutorials/contribution/content/write-tutorials-4d142a6a-9127-4ffb-9e0a-5aba29f169e2

आप पहले से ही:



- अपने ट्यूटोरियल के लिए एक विषय चुनें;
- [Telegram समूह](https://t.me/PlanBNetwork_ContentBuilder) या paolo@planb.network के माध्यम से Plan ₿ Academy टीम से संपर्क किया गया;
- अपने योगदान के साधनों का चयन करें।


अनुभवी Git उपयोगकर्ताओं के लिए इस ट्यूटोरियल में, हम Plan ₿ Academy ट्यूटोरियल बनाने के लिए आवश्यक प्रमुख चरणों और दिशा-निर्देशों का संक्षेप में वर्णन करेंगे। यदि आप Git और GitHub से अपरिचित हैं, तो मेरा सुझाव है कि आप इसके बजाय इन दो अन्य विस्तृत ट्यूटोरियल का अनुसरण करें जो आपको चरण-दर-चरण मार्गदर्शन करेंगे:



- मध्यवर्ती (GitHub Desktop):


https://planb.academy/tutorials/contribution/content/write-tutorials-github-desktop-intermediate-4a36a052-1000-4191-890a-9a1dc65f8957


- शुरुआती लोगों के लिए (वेब ​​इंटरफ़ेस):


https://planb.academy/tutorials/contribution/content/write-tutorials-github-web-beginner-e64f8fed-4c0b-4225-9ebb-7fc5f1c01a79

## सुझाए गए उपकरण


मार्कडाउन फ़ाइलों को संपादित करने के लिए:



- ऑब्सीडियन (निःशुल्क, ओपन-सोर्स नहीं)
- मार्क टेक्स्ट (निःशुल्क, ओपन-सोर्स)
- Zettlr (निःशुल्क, ओपन-सोर्स)
- टाइपोरा (पेड सॉफ्टवेयर, लगभग €15, ओपन-सोर्स नहीं)


गिट के लिए:



- गिट (निःशुल्क, ओपन-सोर्स)
- GitHub Desktop (निःशुल्क, ओपन-सोर्स)
- सोर्सट्री (निःशुल्क, ओपन-सोर्स नहीं)


YAML फ़ाइलों को संपादित करने के लिए:



- विजुअल स्टूडियो कोड (निःशुल्क, ओपन-सोर्स)
- सबलाइम टेक्स्ट (कुछ सीमाओं के साथ निःशुल्क, ओपन-सोर्स नहीं)


आरेख और दृश्य बनाने के लिए:



- कैनवा (मुफ्त, सशुल्क विकल्पों के साथ, ओपन-सोर्स नहीं)
- इंकस्केप (निःशुल्क, ओपन-सोर्स)
- पेनपॉट (निःशुल्क, ओपन-सोर्स)


## वर्कफ़्लो


### 1 - अपने स्थानीय वातावरण को कॉन्फ़िगर करें



- आपके पास GitHub पर [Plan ₿ Academy रिपॉजिटरी](https://github.com/PlanB-Network/bitcoin-educational-content) का अपना fork होना चाहिए।
- अपने fork की मुख्य शाखा (`dev`) को स्रोत रिपॉजिटरी के साथ सिंक्रनाइज़ करें।
- अपने स्थानीय क्लोन को अपडेट करें।


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


### 2 - एक नई शाखा बनाएं



- सुनिश्चित करें कि आप `dev` ब्रांच पर हैं।
- एक वर्णनात्मक नाम के साथ एक नई शाखा बनाएं (उदाहरण के लिए `tuto-green-wallet-loic`)।
- इस शाखा को अपने ऑनलाइन fork पर प्रकाशित करें।


```
# Make sure you are on the 'dev' branch
git checkout dev

# Create a new branch with a descriptive name
git checkout -b tuto-green-wallet-loic

# Publish this branch to your online fork
git push -u origin tuto-green-wallet-loic
```


### 3 - ट्यूटोरियल दस्तावेज़ जोड़ें


***ध्यान दें:*** आप [मेरे Python GUI script](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/scripts/tutorial-related/new-tutorial-creation) का उपयोग करके चरण 3 और 4 को स्वचालित कर सकते हैं। इसे अपने स्थानीय क्लोन में इसके फ़ोल्डर से सीधे चलाएँ, फिर GUI पर आवश्यक फ़ील्ड भरें। इसे स्थापित करने और उपयोग करने के तरीके के बारे में अधिक जानकारी के लिए, [README](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/scripts/tutorial-related/new-tutorial-creation/README.md) देखें।


यदि आप इसे मैन्युअल रूप से करना पसंद करते हैं, तो इन चरणों का पालन करें:



- स्थानीय रिपॉजिटरी में उपयुक्त फ़ोल्डर का पता लगाएं (उदाहरण के लिए `tutorials/wallet`)।
- ट्यूटोरियल के लिए एक स्पष्ट नाम वाली अलग डायरेक्टरी बनाएं (उदाहरण के लिए `green-wallet`)। यह फ़ोल्डर नाम ट्यूटोरियल के URL पथ को भी निर्धारित करेगा। नाम छोटे अक्षरों में होना चाहिए, इसमें कोई विशेष वर्ण (हाइफ़न को छोड़कर) और कोई रिक्त स्थान नहीं होना चाहिए।
- इस डायरेक्टरी में निम्नलिखित आइटम जोड़ें:
    - `assets` नाम का एक सबफ़ोल्डर जिसमें निम्नलिखित शामिल हैं:
        - दो `.webp` छवियां:
            - `logo.webp`: ट्यूटोरियल का लोगो (पृष्ठभूमि सहित वर्गाकार प्रारूप)। यह लोगो प्रस्तुत सॉफ़्टवेयर या टूल का प्रतिनिधित्व करना चाहिए। यदि ट्यूटोरियल किसी विशिष्ट टूल से संबंधित नहीं है (उदाहरण के लिए: स्मरणीय वाक्यांश बनाने के लिए एक सामान्य मार्गदर्शिका), तो आप एक उपयुक्त दृश्य (उदाहरण के लिए: एक सामान्य आइकन) चुन सकते हैं।
            - `cover.webp`: ट्यूटोरियल की शुरुआत में प्रदर्शित होने वाली एक कवर छवि।
        - ट्यूटोरियल की मूल भाषा के कोड वाला एक सबफ़ोल्डर बनाएं। उदाहरण के लिए, यदि ट्यूटोरियल अंग्रेज़ी में लिखा गया है, तो इस सबफ़ोल्डर का नाम `en` होना चाहिए। ट्यूटोरियल के सभी विज़ुअल (आरेख, चित्र, स्क्रीनशॉट आदि) इस फ़ोल्डर में रखें।
    - एक `tutorial.yml` फ़ाइल जिसमें मेटाडेटा (लेखक, टैग, श्रेणी, कठिनाई स्तर आदि) शामिल हैं।
    - ट्यूटोरियल वाली एक मार्कडाउन फ़ाइल, जिसका नाम भाषा कोड के अनुसार रखा गया है (जैसे `fr.md`, `en.md`, आदि)।


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



- `tutorial.yml` फ़ाइल को निम्नानुसार पूरा करें:


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


यहां आवश्यक फ़ील्ड दिए गए हैं:



- id**: एक UUID (यूनिवर्सली यूनिक आइडेंटिफायर) जो ट्यूटोरियल को विशिष्ट रूप से पहचानता है। आप इसे [ऑनलाइन टूल](https://www.uuidgenerator.net/version4) का उपयोग करके जनरेट कर सकते हैं। एकमात्र आवश्यकता यह है कि यह UUID रैंडम हो ताकि प्लेटफ़ॉर्म पर किसी अन्य UUID के साथ टकराव से बचा जा सके;



- project_id**: ट्यूटोरियल में प्रस्तुत टूल के पीछे की कंपनी या संगठन का UUID [प्रोजेक्ट सूची से](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/projects)। उदाहरण के लिए, यदि आप Green Wallet सॉफ़्टवेयर के बारे में ट्यूटोरियल बना रहे हैं, तो आप यह `project_id` निम्न फ़ाइल में पा सकते हैं: `bitcoin-educational-content/resources/projects/blockstream/project.yml`। यह जानकारी आपके ट्यूटोरियल की YAML फ़ाइल में जोड़ी जाती है क्योंकि Plan ₿ Academy, Bitcoin या संबंधित परियोजनाओं पर काम करने वाली सभी कंपनियों और संगठनों का डेटाबेस रखता है। अपने ट्यूटोरियल से जुड़ी इकाई का `project_id` जोड़कर, आप दोनों तत्वों के बीच एक लिंक बनाते हैं;



- टैग**: ट्यूटोरियल सामग्री से संबंधित 2 या 3 प्रासंगिक कीवर्ड, विशेष रूप से [Plan ₿ Academy टैग सूची से चुने गए](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/docs/50-planb-tags.md);



- श्रेणी**: Plan ₿ Academy वेबसाइट संरचना के अनुसार ट्यूटोरियल सामग्री से संबंधित उप-श्रेणी (उदाहरण के लिए, wallet के लिए: `डेस्कटॉप`, `हार्डवेयर`, `मोबाइल`, `बैकअप`);



- स्तर**: ट्यूटोरियल का कठिनाई स्तर, जिसे निम्न में से चुना जा सकता है:
    - `शुरुआती`
    - `मध्यवर्ती`
    - `उन्नत`
    - `विशेषज्ञ`



- professor_id**: आपका `professor_id` (UUID) जैसा कि [आपके प्रोफेसर प्रोफ़ाइल](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/professors) पर प्रदर्शित होता है;



- मूल भाषा**: ट्यूटोरियल की मूल भाषा (उदाहरण के लिए, `fr`, `en`, आदि);



- प्रूफरीडिंग**: प्रूफरीडिंग प्रक्रिया के बारे में जानकारी। पहला भाग पूरा करें, क्योंकि अपने ट्यूटोरियल की प्रूफरीडिंग करना पहले सत्यापन के रूप में गिना जाता है:
    - भाषा**: प्रूफरीडिंग का भाषा कोड (उदाहरण के लिए, `fr`, `en`, आदि)।
    - last_contribution_date**: दिन की तारीख।
    - अत्यावश्यकता**: 1
    - contributor_names**: आपकी GitHub ID.
    - इनाम**: 0


अपने शिक्षक आईडी के बारे में अधिक जानकारी के लिए, कृपया संबंधित ट्यूटोरियल देखें:


https://planb.academy/tutorials/contribution/others/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4

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


### 5 - विषयवस्तु लिखें



- Markdown फ़ाइल की प्रॉपर्टीज़ को निम्न प्रकार से पूरा करें:
    - उपाधि (`नाम`)।
    - एक संक्षिप्त विवरण (`description`)।
- मार्कडाउन सिंटैक्स का उपयोग करके ट्यूटोरियल के शीर्ष पर कवर इमेज जोड़ें (यहां "green" को दिखाए गए टूल के नाम से बदलें):


```
![cover-green](assets/cover.webp)
```



- ट्यूटोरियल की सामग्री को मार्कडाउन में लिखें:
    - सुव्यवस्थित शीर्षकों (`##`), सूचियों और पैराग्राफों का उपयोग करें।
    - Markdown सिंटैक्स का उपयोग करके विज़ुअल डालें:


```
![nom-image](assets/en/001.webp)
```




- आरेखों और छवियों को संबंधित भाषा के उपफ़ोल्डर में रखें, जो `/assets` में स्थित है।


### 6 - ट्यूटोरियल को सेव करें और सबमिट करें



- एक वर्णनात्मक संदेश के साथ कमिट बनाकर अपने परिवर्तनों को स्थानीय रूप से सहेजें।
- अपने GitHub fork पर बदलावों को पुश करें।


```
# Create a commit with a descriptive message
git commit -m "Added green-wallet tutorial"

# Push your changes to your fork
git push origin tuto-green-wallet-loic
```



- एक बार कार्य पूरा हो जाने पर, अपने संशोधनों के एकीकरण का प्रस्ताव देने के लिए GitHub पर एक पुल रिक्वेस्ट (PR) बनाएं।
- पीआर में एक शीर्षक और संक्षिप्त विवरण जोड़ें। टिप्पणी में संबंधित समस्या संख्या का उल्लेख करें।


### 7 - प्रूफरीडिंग और विलय करना



- प्रशासक से पुष्टि या प्रतिक्रिया की प्रतीक्षा करें।
- यदि आवश्यक हो, तो सुधार करें और नए कमिट पुश करें।


```
# Create a commit describing the corrections made
git commit -m "Corrections following the review of the green-wallet tutorial"

# Push the corrections to your fork
git push origin tuto-green-wallet-loic
```



- पीआर मर्ज हो जाने के बाद, आप अपनी वर्किंग ब्रांच को डिलीट कर सकते हैं।


## सामग्री निर्माण मानक



- प्लेटफ़ॉर्म पर समर्थित फ़ॉर्मेटिंग**:
    - क्लासिक मार्कडाउन: सूचियाँ, लिंक, चित्र, उद्धरण, बोल्ड, इटैलिक आदि।
    - LaTeX (केवल ब्लॉक, इनलाइन नहीं): `$$` द्वारा सीमांकित।
    - इनलाइन कोड: एकल बैकटिक वाला सिंटैक्स।
    - कोड ब्लॉक: तीन बैकटिक वाले सिंटैक्स, उदाहरण के लिए:


```
print("Hello, Bitcoin!")
```



- चित्र और आरेख**:
    - सभी छवियां WebP प्रारूप में होनी चाहिए। आवश्यकता पड़ने पर इन्हें परिवर्तित करने के लिए इस निःशुल्क टूल का उपयोग करें: [ImagesConverter](https://github.com/LoicPandul/ImagesConverter)।
    - विज़ुअल को 2 या 3 अंकों से नाम दें (उदाहरण के लिए `001.webp`, `002.webp`)।
    - मोबाइल या हार्डवेयर wallet ट्यूटोरियल के लिए, मॉक-अप का उपयोग करें।
    - केवल स्वयं द्वारा निर्मित या रॉयल्टी-मुक्त विज़ुअल का ही उपयोग करें।
    - सुनिश्चित करें कि वे प्रासंगिक और उच्च गुणवत्ता वाले हों।
- ग्राफिक चार्टर**:
    - फ़ॉन्ट: [आईबीएम प्लेक्स सैंस](https://fonts.google.com/specimen/IBM+Plex+Sans).
    - कलर्स Plan ₿ Academy:
        - नारंगी: `#FF5C00`
        - काला: `#000000`
        - सफेद: `#FFFFFF`


यदि आपको अपना ट्यूटोरियल सबमिट करने में तकनीकी कठिनाइयों का सामना करना पड़ रहा है, तो कृपया [हमारे समर्पित Telegram योगदान समूह](https://t.me/PlanBNetwork_ContentBuilder) पर सहायता मांगने में संकोच न करें। बहुत-बहुत धन्यवाद!