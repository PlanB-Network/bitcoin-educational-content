---
name: शैक्षिक उपकरण जोड़ना
description: प्लानबी नेटवर्क पर नई शैक्षिक सामग्री कैसे जोड़ें?
---
![event](assets/cover.webp)


प्लानबी का मिशन Bitcoin पर अग्रणी शैक्षिक संसाधन उपलब्ध कराना है, जितना संभव हो उतनी भाषाओं में। साइट पर प्रकाशित सभी सामग्री ओपन-सोर्स है और GitHub पर होस्ट की गई है, जो किसी को भी प्लेटफ़ॉर्म को समृद्ध बनाने में भाग लेने की अनुमति देती है।


ट्यूटोरियल और प्रशिक्षण से परे, प्लानबी नेटवर्क Bitcoin पर विविध शैक्षिक सामग्री की एक विशाल लाइब्रेरी भी प्रदान करता है, जो सभी के लिए सुलभ है, ["BET" (_बिटकॉइन एजुकेशनल टूलकिट_) अनुभाग में](https://planb.network/resources/bet)। इस डेटाबेस में शैक्षिक पोस्टर, मीम्स, विनोदी प्रचार पोस्टर, तकनीकी आरेख, लोगो और उपयोगकर्ताओं के लिए अन्य उपकरण शामिल हैं। इस पहल का लक्ष्य दुनिया भर में Bitcoin पढ़ाने वाले व्यक्तियों और समुदायों को आवश्यक दृश्य संसाधन प्रदान करके उनका समर्थन करना है।


क्या आप इस डेटाबेस को समृद्ध बनाने में भाग लेना चाहते हैं, लेकिन नहीं जानते कि कैसे? यह ट्यूटोरियल आपके लिए है!


*यह ज़रूरी है कि साइट में एकीकृत सभी सामग्री अधिकारों से मुक्त हो या स्रोत फ़ाइल के लाइसेंस का सम्मान करे। साथ ही, PlanB Network पर प्रकाशित सभी विज़ुअल [CC-BY-SA](https://creativecommons.org/licenses/by-sa/4.0/) लाइसेंस के तहत उपलब्ध कराए जाते हैं।*

![event](assets/01.webp)


- सबसे पहले, आपके पास GitHub पर एक अकाउंट होना चाहिए। अगर आपको नहीं पता कि अकाउंट कैसे बनाया जाता है, तो हमने आपको मार्गदर्शन करने के लिए एक विस्तृत ट्यूटोरियल बनाया है।


https://planb.network/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c



- [डेटा के लिए समर्पित PlanB के GitHub रिपॉजिटरी](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/resources/bet) पर जाएं, `resources/bet/` अनुभाग में:

![event](assets/02.webp)


- ऊपर दाईं ओर स्थित `फ़ाइल जोड़ें` बटन पर क्लिक करें, फिर `नई फ़ाइल बनाएँ` पर क्लिक करें:

![event](assets/03.webp)


- यदि आपने पहले कभी PlanB Network की सामग्री में योगदान नहीं दिया है, तो आपको मूल रिपॉजिटरी का अपना Fork बनाना होगा। रिपॉजिटरी को फ़ॉर्क करने का मतलब है अपने GitHub खाते पर उस रिपॉजिटरी की एक प्रति बनाना, जो आपको मूल रिपॉजिटरी को प्रभावित किए बिना प्रोजेक्ट पर काम करने की अनुमति देता है। `Fork this repository` बटन पर क्लिक करें:

![event](assets/04.webp)


- इसके बाद आप GitHub संपादन पृष्ठ पर पहुंचेंगे:

![event](assets/05.webp)


- अपनी सामग्री के लिए एक फ़ोल्डर बनाएँ। ऐसा करने के लिए, `अपनी फ़ाइल का नाम दें...` बॉक्स में, अपनी सामग्री का नाम लोअरकेस में स्पेस के बजाय डैश के साथ लिखें। मेरे उदाहरण में, मान लें कि मैं 2048-शब्द BIP39 सूची का एक PDF विज़ुअल जोड़ना चाहता हूँ। इसलिए, मैं अपने फ़ोल्डर को `bip39-wordlist` कहूँगा: ![event](assets/06.webp)
- फ़ोल्डर के निर्माण की पुष्टि करने के लिए, उसी बॉक्स में नाम के बाद एक स्लैश जोड़ें, उदाहरण के लिए: `bip39-wordlist/`. स्लैश जोड़ने से फ़ाइल के बजाय स्वचालित रूप से एक फ़ोल्डर बन जाता है:

![event](assets/07.webp)


- इस फ़ोल्डर में, आप `bet.yml` नाम से पहली YAML फ़ाइल बनाएंगे:

![event](assets/08.webp)


- इस टेम्पलेट का उपयोग करके अपनी सामग्री से संबंधित जानकारी से यह फ़ाइल भरें:


```yaml
builder:
type:
links:
download:
view:
- en:
tags:
-
-
contributors:
-
```


प्रत्येक फ़ील्ड में भरने हेतु विवरण इस प्रकार हैं:



- `बिल्डर`**: प्लानबी नेटवर्क पर अपने संगठन का पहचानकर्ता इंगित करें। यदि आपके पास अभी तक अपनी कंपनी के लिए "बिल्डर" पहचानकर्ता नहीं है, तो आप इस ट्यूटोरियल का पालन करके एक बना सकते हैं।


https://planb.network/tutorials/contribution/resource/add-builder-b5834c46-6dcc-4064-8d68-1ef529991d3d

यदि आपके पास बिल्डर प्रोफाइल नहीं है, तो आप बिल्डर प्रोफाइल बनाए बिना अपना नाम, अपना छद्म नाम या अपनी कंपनी का नाम उपयोग कर सकते हैं।



- `type`**: निम्नलिखित दो विकल्पों में से अपनी सामग्री की प्रकृति का चयन करें:
 - शैक्षिक सामग्री के लिए `शैक्षिक सामग्री`.
 - अन्य प्रकार की विविध सामग्री के लिए `दृश्य सामग्री`.



- `लिंक`**: अपनी सामग्री के लिए लिंक प्रदान करें। आपके पास दो विकल्प हैं:
 - यदि आप अपनी सामग्री को सीधे प्लानबी के गिटहब पर होस्ट करना चुनते हैं, तो आपको निम्नलिखित चरणों के दौरान इस फ़ाइल में लिंक जोड़ने होंगे।
 - यदि आपकी सामग्री कहीं और होस्ट की गई है, जैसे कि आपकी व्यक्तिगत वेबसाइट पर, तो संबंधित लिंक यहां इंगित करें:
     - `download`: आपकी सामग्री को डाउनलोड करने के लिए एक लिंक.
     - `view`: आपकी सामग्री देखने के लिए एक लिंक (डाउनलोड लिंक के समान हो सकता है)। यदि आपकी सामग्री कई भाषाओं में उपलब्ध है, तो प्रत्येक भाषा के लिए एक लिंक जोड़ें।



- `tags`**: अपनी सामग्री से जुड़े दो टैग जोड़ें। उदाहरण:
 - जीडब्ल्यू-4
 - तकनीकी
 - अर्थव्यवस्था
 - शिक्षा
 - मेम...



- `योगदानकर्ता`**: यदि आपके पास योगदानकर्ता पहचानकर्ता है तो उसका उल्लेख करें।


उदाहरण के लिए, आपकी YAML फ़ाइल इस तरह दिख सकती है:


```yaml
builder: PlanB-Network
type: Educational Content
links:
download: https://workspace.planb.network/s/fojeJa7ZbftQTwo
view:
- In my example, I will leave the links empty for now, as I will add my PDF directly on GitHub:
![event](assets/09.webp)
- Once your modifications to this file are complete, save them by clicking on the `Commit changes...` button:
![event](assets/10.webp)
- Add a title for your modifications, as well as a short description:
![event](assets/11.webp)
- Click on the green `Propose changes` button:
![event](assets/12.webp)
- You will then arrive on a page that summarizes all your changes:
![event](assets/13.webp)
- Click on your GitHub profile picture at the top right, then on `Your Repositories`:
![event](assets/14.webp)
- Select your fork of the PlanB Network repository:
![event](assets/15.webp)
- You should see a notification at the top of the window with your new branch. It is probably called `patch-1`. Click on it:
![event](assets/16.webp)
- You are now on your working branch (**make sure you are on the same branch as your previous modifications, this is important!**):
![event](assets/17.webp)
- Go back to the `resources/bet/` folder and select the folder of your content that you just created in the previous commit:
![event](assets/18.webp)
- In the folder of your content, click on the `Add file` button, then on `Create new file`:
![event](assets/19.webp)
- Name this new folder `assets` and confirm its creation by putting a slash `/` at the end:
![event](assets/20.webp)
- In this `assets` folder, create a file named `.gitkeep`: ![event](assets/21.webp)
- Click on the `Commit changes...` button: ![event](assets/22.webp)
- Leave the commit title as default, and make sure the `Commit directly to the patch-1 branch` box is checked, then click on `Commit changes`: ![event](assets/23.webp)
- Return to the `assets` folder: ![event](assets/24.webp)
- Click on the `Add file` button, then on `Upload files`: ![event](assets/25.webp)
- A new page will open. Drag and drop a thumbnail that represents your content into the area. This image will be displayed on the PlanB Network site: ![event](assets/26.webp)
- It can be a preview, a logo, or an icon: ![event](assets/27.webp)
- Once the image is uploaded, make sure the `Commit directly to the patch-1 branch` box is checked, then click on `Commit changes`: ![event](assets/28.webp)
- Be careful, your image must be named `logo` and must be in `.webp` format. The full file name should therefore be: `logo.webp`: ![event](assets/29.webp)
- Return to your `assets` folder and click on the intermediary file `.gitkeep`: ![event](assets/30.webp)
- Once on the file, click on the three small dots at the top right then on `Delete file`: ![event](assets/31.webp)
- Make sure you are still on the same working branch, then click on the `Commit changes` button: ![event](assets/32.webp)
- Add a title and a description to your commit, then click on `Commit changes`: ![event](assets/33.webp)
- Return to the folder of your content: ![event](assets/34.webp)
- Click on the `Add file` button, then on `Create new file`: ![event](assets/35.webp)
- Create a new YAML file by naming it with the indicator of your native language. This file will be used for the content description. For example, if I want to write my description in English, I will name this file `en.yml`: ![event](assets/36.webp)
- Fill out this YAML file using this template:

```

name:
description: |

```

- For the `name` key, you can add the name of your content;
- For the `description` key, you simply need to add a short paragraph that describes your content. The description must be in the same language as the file name. You do not need to translate this description into all the supported languages on the site, as the PlanB teams will do so with their model.
For example, here is what your file might look like:

```

name: BIP39 WORDLIST
description: |
Mnemonic वाक्यांशों को एनकोड करने के लिए उपयोग किए जाने वाले BIP39 शब्दकोश से 2048 अंग्रेजी शब्दों की पूरी और क्रमांकित सूची। दस्तावेज़ को एक ही पृष्ठ पर मुद्रित किया जा सकता है।

```

![event](assets/37.webp)
- Click on the `Commit changes...` button:
![event](assets/38.webp)
- Ensure that the `Commit directly to the patch-1 branch` box is checked, add a title, then click on `Commit changes`:
![event](assets/39.webp)
- Your content folder should now look like this:
![event](assets/40.webp)

---

*If you prefer not to add the content on GitHub and you have already noted the links in the `bet.yml` file during the previous steps, you can skip this section and go directly to the part concerning the creation of the Pull Request.*

- Return to the `/assets` folder:
![event](assets/41.webp)
- Click on the `Add file` button, then on `Upload files`:
![event](assets/42.webp)
- A new page will open. Drag and drop into the area the content you wish to share:
![event](assets/43.webp)
- For example, I added the PDF file of the BIP39 list:
![event](assets/44.webp)
- Once the content is uploaded, ensure that the `Commit directly to the patch-1 branch` box is checked, then click on `Commit changes`:
![event](assets/45.webp)
- Return to your `/assets` folder and click on the file you just uploaded:
![event](assets/46.webp)
- Retrieve the intermediate URL of your file. For example, in my case, the URL is:

```

https://github.com/tutorial-pandul/Bitcoin-educational-content/blob/patch-1/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf

```

- Keep only the last part of the URL from `/resources` onwards:

```

/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf

```

- Add to the base of the URL the following information to have the correct link:

```

https://github.com/DiscoverBitcoin/Bitcoin-educational-content/blob/dev/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf

```