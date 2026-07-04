---
name: Simplicity में गहराई से उतरना
goal: Simplicity की डिज़ाइन दर्शन, टाइप सिस्टम और पूर्ण जीवनचक्र में महारत हासिल करना
objectives:
  - उन तीन मूलभूत संयोजन विधियों और नौ कॉम्बिनेटरों को समझना जो एक पूर्ण भाषा बनाते हैं
  - Simplicity के न्यूनतम टाइप सिस्टम से boolean logic, arithmetic और SHA-256 बनाना
  - यह समझना कि Failure और Reader साइड इफेक्ट वास्तविक blockchain interaction को कैसे सक्षम करते हैं
  - यह सीखना कि Simplicity programs Taproot addresses कैसे बनते हैं और witness data से कैसे redeem किए जाते हैं
---

# Simplicity में गहराई से उतरना

[Dr. Russell O'Connor](https://r6.ca/) द्वारा लिखी गई पूर्ण पाँच-भागों वाली ["Delving Simplicity"](https://delvingbitcoin.org/t/delving-simplicity-part-three-fundamental-ways-of-combining-computations/1902) लेख-श्रृंखला पर आधारित, Simplicity भाषा के पीछे के सिद्धांत और डिज़ाइन निर्णयों में गहरा अवगाहन; Dr. O'Connor Blockstream Research में Simplicity के निर्माता हैं। यह कोर्स समझाता है कि Simplicity को जिस तरह डिज़ाइन किया गया, वह *क्यों* किया गया; इसे लिखना कैसे है, यह नहीं।

यह कोर्स Dr. O'Connor के लेखों का अनुसरण करता है: computations को combine करने के तीन मूलभूत तरीकों से लेकर न्यूनतम type system और उसके completeness theorem तक, प्रथम सिद्धांतों से practical data types और arithmetic के निर्माण तक, blockchain interaction के लिए side effects के सावधानीपूर्वक परिचय तक, और अंत में programs को addresses में commit करने तथा on-chain redeem करने तक।

+++

# परिचय

<partId>c362889b-c630-435f-911b-724c4eca505b</partId>

## कोर्स का अवलोकन

<chapterId>cdcc40b6-c985-45b4-9bee-6f931e984476</chapterId>

SCR403 — Simplicity में गहराई से उतरना में आपका स्वागत है!

यह कोर्स [Dr. Russell O'Connor](https://r6.ca/) द्वारा लिखी गई **"Delving Simplicity"** लेख-श्रृंखला पर आधारित है। वे [Blockstream](https://blockstream.com/) में Infrastructure Tech Developer हैं और Simplicity के निर्माता हैं। मूल लेख [Delving Bitcoin](https://delvingbitcoin.org/u/roconnor-blockstream/summary) forum पर प्रकाशित हुए थे और इस कोर्स की प्राथमिक स्रोत सामग्री बनाते हैं। हम उनके अग्रणी कार्य के लिए आभारी हैं, जिसने इस शैक्षणिक सामग्री को संभव बनाया।

### आप क्या सीखेंगे

यह कोर्स Simplicity के पीछे की डिज़ाइन दर्शन और गणितीय नींवों की खोज करता है; Simplicity अगली पीढ़ी की scripting भाषा है, जिसे जुलाई 2025 में [Liquid Network](https://blockstream.com/press-releases/2025-07-31-blockstream-launches-simplicity/) पर सक्रिय किया गया। यह पूर्ण पाँच-भागों वाली लेख-श्रृंखला का अनुसरण करता है और दो मुख्य सामग्री खंडों में संरचित है:

1. **Simplicity की नींव** — blockchain computation को मूलतः अलग भाषा की आवश्यकता क्यों होती है, operations को combine करने के तीन तरीके (sequential, parallel, conditional), और वे नौ core combinators जो एक गणितीय रूप से पूर्ण भाषा बनाते हैं
2. **Data Types से Programs तक** — प्रथम सिद्धांतों से boolean logic, arithmetic और SHA-256 बनाना; उन Failure और Reader side effects को समझना जो blockchain interaction को सक्षम करते हैं; और यह सीखना कि programs Commitment Merkle Roots के माध्यम से Taproot addresses में कैसे commit किए जाते हैं और witness data से कैसे redeem किए जाते हैं

### पूर्वापेक्षाएँ

यह एक **expert-level** कोर्स है (लगभग 10 घंटे)। आपको इनमें सहज होना चाहिए:
- Bitcoin scripting की बुनियादी अवधारणाएँ (transaction validation क्या करता है)
- Programming की मूलभूत अवधारणाएँ (types, functions, composition)
- Mathematical notation से कुछ परिचय सहायक है, पर आवश्यक नहीं। हम आगे बढ़ते हुए सब कुछ समझाते हैं

### मुख्य संसाधन

- **मूल लेख**: Delving Bitcoin पर Dr. Russell O'Connor द्वारा ["Delving Simplicity"](https://delvingbitcoin.org/u/roconnor-blockstream/summary)
- **Simplicity repository**: [BlockstreamResearch/simplicity](https://github.com/BlockstreamResearch/simplicity) — source code और Rocq formal proofs
- **Official website**: [simplicity-lang.org](https://simplicity-lang.org/) — documentation और SimplicityHL reference
- **Blockstream blog**: [Simplicity on GitHub](https://blog.blockstream.com/en-simplicity-github/) — technical overview

Bitcoin engineering के सबसे elegant हिस्सों में से एक में उतरने के लिए तैयार हैं? चलिए शुरू करते हैं!

## Simplicity क्या है?

<chapterId>d04f3960-d7fb-44e1-b5a3-25b33d03fd38</chapterId>

यदि आप Simplicity की पृष्ठभूमि के बिना इस कोर्स में आ रहे हैं, तो गहराई में उतरने से पहले यह chapter आपको दिशा देगा।

### संक्षेप में Simplicity

Simplicity एक **Bitcoin-native smart contract language** है, जो आज Liquid Network पर live है। Dr. Russell O'Connor ने लगभग 2012 में इसकी पहली कल्पना की थी और अपने 2017 paper *Simplicity: A New Language for Blockchains* में इसे विस्तार से बताया था। वर्षों की formal verification और development के बाद इसे जुलाई 2025 में Liquid Network पर activate किया गया।

Ethereum की Solidity के विपरीत, जो एक Turing-complete, high-level contract language है, Simplicity जानबूझकर minimal है। इसमें हैं:
- **तीन type formers** (unit, sum, product)
- **नौ combinators** (basic operations और composition rules)
- **कोई loops नहीं, कोई recursion नहीं, कोई dynamic memory नहीं**

सिर्फ इन primitives से, आप transaction validation के लिए आवश्यक कोई भी computation बना सकते हैं, boolean logic से लेकर पूर्ण SHA-256 hashing तक।

### आज आप Simplicity से क्या कर सकते हैं?

Simplicity पहले से ही Liquid Network पर वास्तविक applications को power कर रही है। सबसे उल्लेखनीय [Simplicity DEX](https://docs.simplicity-lang.org/use-cases/simplicity-dex/) है, एक oracle-free options marketplace जहाँ users USDt को collateral के रूप में उपयोग करके L-BTC पर call options trade करते हैं (underlying contract puts को भी support करता है)। अन्य live Simplicity projects में SideSwap का [Swaption](https://swaption.io/) (options) और Resolvr का open-source [Deadcat](https://github.com/Resolvr-io/deadcat) (prediction markets) शामिल हैं। DeFi से परे, Simplicity vaults, covenants और complex multisig schemes जैसी advanced spending conditions सक्षम करती है, जो Bitcoin Script में असंभव या unsafe होतीं।

### यह कोर्स क्या है — और क्या नहीं है

यह hands-on coding tutorial **नहीं** है। आप यहाँ Simplicity programs नहीं लिखेंगे। यदि आप वह खोज रहे हैं, तो देखें:
- [simplicity-lang.org](https://simplicity-lang.org/) — official documentation और SimplicityHL high-level language
- [Simplicity GitHub repository](https://github.com/BlockstreamResearch/simplicity) — reference implementation, examples और Rocq proofs
- शुरू करने पर [Blockstream blog post](https://blog.blockstream.com/en-simplicity-github/)

यह कोर्स जिस बारे में **है**: Simplicity के design के पीछे की **philosophical और technical choices**। यह भाषा इस तरह क्यों बनाई गई? केवल नौ combinators क्यों? recursion क्यों नहीं? यह क्यों मायने रखता है कि type system Gentzen के sequent calculus से जुड़ता है?

इसे कार चलाना सीखने के बजाय यह समझना समझें कि **engine इस तरह क्यों बनाया गया**।

### यह किसके लिए है?

यह कोर्स इनके लिए आदर्श है:
- **Protocol developers** जो code लिखने से पहले Simplicity की foundations समझना चाहते हैं
- **Bitcoin researchers** जिन्हें formal verification और type-theoretic approach में रुचि है
- **Computer scientists** जिन्हें sequent calculus और blockchain computation के संबंध को लेकर जिज्ञासा है
- **Advanced bitcoiners** जो Liquid की scripting capabilities की सतही समझ से आगे जाना चाहते हैं

यदि "sum types", "combinators" या "sequent calculus" जैसे terms आपके लिए पूरी तरह नए हैं, तो चिंता न करें; हम सब कुछ शुरू से समझाते हैं। लेकिन एक घनी, mathematical यात्रा के लिए तैयार रहें।

### लेखों से कोर्स तक

Dr. O'Connor की मूल "Delving Simplicity" श्रृंखला पाँच technical articles के रूप में structured है। यह कोर्स उस सामग्री को quizzes के साथ एक progressive learning path में reorganize और annotate करता है, ताकि रास्ते में आपकी समझ परखी जा सके। विचार, definitions और proofs उनके हैं, और हमने format को structured education के लिए adapt किया है।

# Simplicity की नींव

<partId>a5976618-94ab-4b29-b9aa-040d35c68e5d</partId>

## Computations को combine करने के मूलभूत तरीके

<chapterId>6d46e77a-7e60-473b-b230-418da5ae44eb</chapterId>

अब जबकि Simplicity Liquid Network पर activate हो चुकी है, मैं Simplicity भाषा की philosophy और design में एक गहरा dive करना चाहता हूँ।

Bitcoin का transaction validation सामान्य programming language design से काफी अलग application है। Block space की लागत premium पर है, इसलिए programs को compact होना चाहिए। Bitcoin transactions में programs केवल एक ही input पर execute होते हैं और हर कोई program को उसी input पर execute करता है। साथ ही, transaction को authorize करने वाला agent computation का outcome पहले से जानता है: कि transaction valid है।

आमतौर पर authorizing agent transaction की validity को attest करने वाला witness data निकालने के लिए कहीं अधिक महंगे computations चलाएगा, जबकि blockchain पर चलने वाले programs को witness data की validity check करनी होती है। Validity check करना अक्सर validity prove करने से बहुत सस्ता होता है।

हमने Simplicity को ऐसे unique language design challenges को ध्यान में रखकर design किया है। उदाहरण के लिए, Simplicity requires कि unexecuted branches prune किए जाएँ ताकि वे blockchain पर दिखाई न दें। Preprocessing steps को सावधानी से design किया गया है ताकि वे Simplicity program के size में (quasi-)linear time complexity दिखाएँ। "gas" के बजाय static analysis का उपयोग किया जाता है, क्योंकि gas को prescribed तरीके से code execute किए बिना compute नहीं किया जा सकता; इससे execution model के details consensus critical नहीं बनते। Execution के दौरान कोई dynamic memory allocation नहीं। इत्यादि।

Simplicity के design details में उतरने से पहले, मैं इस series की शुरुआत basic building blocks को combine करके नई functionality बनाने के general तरीकों पर कुछ programming philosophy से करना चाहता हूँ।

### Composition

मान लीजिए कोई Bitcoin जैसी blockchain के लिए programmable transactions की भाषा design कर रहा है। विशेष रूप से, programs के पास केवल transaction data और inputs के UTXO data तक access है, और execution केवल transaction validity निर्धारित करता है (जिससे execution का result cache किया जा सकता है)। मान लें कि कोई basic operations के ऐसे set से शुरू करता है जो basic computations, transaction से data पढ़ना और/या process करना, और signature verification जैसे विभिन्न tasks कर सकते हैं। प्रत्येक operation किसी type का input (संभवतः empty) consume करता है और किसी type का output return करता है। हम इन basic operations को अधिक complex operations में combine करने के कौन-कौन से तरीके हैं?

### Sequential Composition

![क्रमिक Composition](assets/en/001.webp)

सबसे fundamental composition method sequential composition है। यदि हमारे पास दो basic operations हैं, जिनमें से एक का output data type दूसरे के input data type से match करता है, तो हम इन दोनों operations को एक नए composite operation में combine कर सकते हैं। यह नया operation इन दोनों basic operations को sequence में चलाता है: पहले operation का input लेता है, उस first operation का output second operation के input में pass करता है, और अंततः उस second operation का output return करता है।

बेशक, हमें केवल basic operations को combine करने तक सीमित रहने की आवश्यकता नहीं है। अब जब हमारे पास कुछ composite operations हैं, तो हम उन्हें भी functional composition का उपयोग करके combine कर सकते हैं।

Mathematics में, इस sequential composition को अक्सर सिर्फ "composition" कहा जाता है, और कोई सोच सकता है कि चीजों को compose करने का यही एकमात्र तरीका है। हालांकि, हमारे पास operations compose करने के अन्य तरीके भी हैं।

### Parallel Composition

![समानांतर Composition](assets/en/002.webp)

मान लीजिए हमारे पास दो operations हैं; वे basic या complex operations हो सकते हैं, और दोनों समान type का input लेते हैं। इन दोनों operations को compose करने का दूसरा fundamental तरीका है कि दोनों को उसी input पर execute किया जाए। इसे parallel composition कहा जाता है, और output का type original operations के outputs के types का "product" होता है तथा इसमें दोनों outputs की pair शामिल होती है।

हालाँकि इसे "parallel" composition कहा जाता है, और दो operations सिद्धांततः parallel execute किए जा सकते हैं, parallel execution कोई operational requirement नहीं है। हम पहले एक operation और फिर second operation execute करके parallel composition को "sequentially" implement कर सकते हैं। जब तक output समान है, हमें इस बात से फर्क नहीं पड़ता कि parallel composition कैसे implement किया गया है।

### Conditional Composition

![सशर्त Composition](assets/en/003.webp)

Conditional composition, parallel composition का dual है। इस case में हमारे पास दो operations हैं जो same output produce करते हैं, और हम उनमें से एक को execute करने के लिए चुनकर उन्हें compose करते हैं। इस composite operation का input, original operation के inputs के types का "sum" या "tagged union" होता है। इस instance में tag, "Left" या "Right", input के data में एक single bit है जो निर्धारित करता है कि कौन-से type का data carry किया जा रहा है, और इसलिए कौन-सा operation execute किया जा सकता है।

Conditional composition उसी तरह काम करता है, भले ही input दो identical types का sum हो। Sum type में फिर भी एक tag होता है, और उस tag का value निर्धारित करता है कि दोनों operations में से कौन-सा execute किया जाना है।

### Bitcoin Script में Composition

विभिन्न programming languages में इन तीन प्रकार की composition को realize करने के कई तरीके हैं। Bitcoin Script में, sequential composition दो routines की concatenation द्वारा (approximately) realize होती है (इसीलिए Bitcoin Script को concatenative programming language कहा जाता है), क्योंकि एक routine का output stack पर छोड़ दिया जाता है ताकि subsequent routine उसे consume कर सके। Parallel composition duplicate और swap operations का उपयोग करके stack को manipulate करने से achieved होती है ताकि दो routines same input पर run किए जा सकें। चीजें पूरी तरह straightforward नहीं हैं, क्योंकि types के जिस "product" की हम बात कर रहे हैं, वह typically multiple stack items का उपयोग करके realize होता है। उम्मीद है कि आप general idea देख सकते हैं।

Conditional composition, बेशक, `OP_IF` द्वारा realize होती है, जो stack पर value के आधार पर branch करता है। इस case में top stack item tag की भूमिका निभाता है, और आमतौर पर stack पर अगला item या items अलग-अलग "types" के होते हैं जो tag के value पर depend करते हैं। प्रत्येक case के लिए stack item types `OP_IF` की branches में से केवल एक द्वारा processing के लिए suitable हो सकते हैं। हालांकि `OP_ENDIF` तक पहुँचने के बाद stack items consistent "type" के होने चाहिए ताकि remaining script स्वतंत्र रूप से proceed कर सके, चाहे पहले कौन-सी branch ली गई हो।

### Simplicity में Composition

हमने Simplicity को ऐसे combinators के साथ design किया है जो composition के इन तीन forms को directly implement करते हैं। Product और sum types से संबंधित अन्य basic operations को support करने के लिए कुछ और combinators के साथ, core Simplicity language अंततः नौ combinators से बनी है, जो किसी भी finite computation को express करने के लिए पर्याप्त हैं। हम अगले chapter में इस पर और detail से चर्चा करेंगे।

### Composition का चौथा प्रकार

समाप्त करने से पहले हमें उल्लेख करना चाहिए कि Computer Science में कम-से-कम एक और प्रकार की composition मिलती है, जिसे "recursive composition" कहा जाता है। Recursive composition में एक operation को multiple times iterate किया जाता है।

ध्यान दें कि Bitcoin Script recursive composition को support नहीं करता, और इसी तरह हमने Simplicity के design से unbounded recursion को स्पष्ट रूप से exclude किया है। हमारा thesis है कि unbounded iterative computation को recursive covenants का उपयोग करके बेहतर implement किया जाता है, जो multiple transactions पर compute करते हैं। इससे users block space और standardness constraints से बच सकते हैं और transaction costs को बेहतर predict कर सकते हैं।

यह कहा जा रहा है कि Simplicity के delegation feature का abuse करके unbounded recursive composition जैसा कुछ provide करने के तरीके हैं, जिन पर हम इस series में बाद में चर्चा कर सकते हैं।

### निष्कर्ष

हमने basic operations को complex operations में transform करने के लिए composition के तीन major forms की समीक्षा की:

- sequential composition
- parallel composition
- conditional composition

हमने चर्चा की कि Bitcoin Script में composition के ये forms कैसे realize होते हैं, और संकेत दिया कि उन्होंने Simplicity language के design को कैसे influence किया है। हमने note किया कि composition का चौथा प्रकार, recursive composition, Simplicity और Bitcoin Script दोनों से विशेष रूप से excluded है।

अगले chapter में हम उन नौ combinators का वर्णन करेंगे जो Simplicity language का core बनाते हैं, वे composition के इन तीन forms को directly realize करने में कैसे काम आते हैं, और यह किसी भी finite computation को describe करने के लिए एक complete language कैसे बनाता है।

## Simplicity की Combinator Completeness

<chapterId>2a10a6ba-fada-4556-a673-3ae8c0794bf0</chapterId>

इस chapter में हम core Simplicity language का परिचय देते हैं और दिखाते हैं कि language complete है, यानी कोई भी finite computation इसके भीतर express किया जा सकता है।

### Simplicity Types

Simplicity तीन fundamental type constructors support करती है। Product type `A × B` parallel composition outputs का प्रतिनिधित्व करता है, जबकि sum type `A + B` (tagged union) conditional composition inputs को handle करता है। तीसरा type unit type है।

### Unit Type

Unit type, जिसे `𝟙` या `ONE` से denote किया जाता है, में ठीक एक value होती है: empty tuple `⟨⟩` या `()`। यह zero-bit data type कोई information carry नहीं करता।

### Sum Type

Sum type `A + B` दो types को tags के साथ combine करता है, जो "left" या "right" दर्शाते हैं। Values को left-tagged values के लिए `σᴸ(a)` या `inl(a)` और right-tagged values के लिए `σᴿ(b)` या `inr(b)` के रूप में लिखा जाता है। Tags identical types combine करने पर भी distinct रहते हैं।

#### Boolean Type

Type `𝟙 + 𝟙`, जिसे `𝟚` या `TWO` से denote किया जाता है, दो values वाला one-bit type है। Convention के अनुसार, `σᴸ⟨⟩` false/zero को represent करता है, जबकि `σᴿ⟨⟩` true/one को represent करता है।

### Product Type

Product types `A × B` में value pairs होते हैं जिन्हें `⟨a, b⟩` या `(a, b)` के रूप में लिखा जाता है। Type `𝟚 × 𝟚` में चार values होती हैं, जो `𝟚 + 𝟚` में मौजूद चार values से distinct हैं।

### Core Simplicity Expressions

Operations को `f : A ⊢ B` के रूप में denote किया जाता है, जिसका अर्थ है input type `A` और output type `B`। Simplicity "first-order" है — इसमें function types नहीं हैं।

### दो Basic Operations

Core language दो basic operations provide करती है:

**Identity (`iden`).** Identity operation अपने input को unchanged आगे pass करता है:

```
iden : A ⊢ A
⟦iden⟧(a) = a
```

**Unit (`unit`).** Unit operation अपने input को discard करता है और empty tuple return करता है:

```
unit : A ⊢ 𝟙
⟦unit⟧(a) = ⟨⟩
```

ये प्रत्येक type के लिए एक operation वाली families बनाते हैं।

### तीन Composition Combinators

Sequential composition `comp f g` (जिसे `f ⨾ g` या `f >>> g` लिखा जाता है) का उपयोग करती है:

```
If f : A ⊢ B and g : B ⊢ C, then
comp f g : A ⊢ C
⟦f ⨾ g⟧(a) = ⟦g⟧(⟦f⟧(a))
```

Parallel composition `pair f g` (जिसे `f ▵ g` या `f &&& g` लिखा जाता है) का उपयोग करती है:

```
If f : A ⊢ B and g : A ⊢ C, then
pair f g : A ⊢ B × C
⟦f ▵ g⟧(a) = ⟨⟦f⟧(a), ⟦g⟧(a)⟩
```

Conditional composition `case f g : (A + B) × C ⊢ D` का उपयोग करती है, जिससे branches को shared environment `C` तक access मिलता है:

```
If f : A × C ⊢ D and g : B × C ⊢ D, then
case f g : (A + B) × C ⊢ D
⟦case f g⟧⟨σᴸ(a), c⟩ = ⟦f⟧⟨a, c⟩
⟦case f g⟧⟨σᴿ(b), c⟩ = ⟦g⟧⟨b, c⟩
```

Conditional composition यह shape क्यों लेती है — shared environment `C` के साथ paired sum — न कि एक simple `copair f g : A + B ⊢ C`, जो केवल branch चुनता है? क्योंकि bare `copair` **distribution** express नहीं कर सकता: function `dist : (A + B) × C ⊢ A × C + B × C`, जो shared input को taken branch में push करता है। Environment `C` को सीधे `case` में build करके, Simplicity एक single combinator से conditional composition *और* distribution प्राप्त करती है — यह उन key design decisions में से एक है जो core language को नौ combinators तक सीमित रखता है।

### चार और Combinators

Product consumption `take` और `drop` का उपयोग करता है:

**take** left element extract करता है:

```
If f : A ⊢ C, then
take f : A × B ⊢ C
⟦take f⟧⟨a, b⟩ = ⟦f⟧(a)
```

**drop** right element extract करता है:

```
If f : B ⊢ C, then
drop f : A × B ⊢ C
⟦drop f⟧⟨a, b⟩ = ⟦f⟧(b)
```

Sum production `injl` और `injr` का उपयोग करता है:

**injl** left tag के साथ wrap करता है:

```
If f : A ⊢ B, then
injl f : A ⊢ B + C
⟦injl f⟧(a) = σᴸ(⟦f⟧(a))
```

**injr** right tag के साथ wrap करता है:

```
If f : A ⊢ C, then
injr f : A ⊢ B + C
⟦injr f⟧(a) = σᴿ(⟦f⟧(a))
```

### नौ Core Combinators

कुल मिलाकर, Simplicity में ठीक नौ core combinators हैं:

| कॉम्बिनेटर | उद्देश्य |
|---|---|
| `iden` | Input को pass through करना |
| `unit` | Input discard करना |
| `comp` | Sequential composition |
| `pair` | Parallel composition |
| `case` | Conditional composition |
| `take` | Product से left extract करना |
| `drop` | Product से right extract करना |
| `injl` | Sum के left में inject करना |
| `injr` | Sum के right में inject करना |

### Simplicity और Sequent Calculus

Simplicity का design Gentzen के sequent calculus के conjunctive-disjunctive fragment से derive होता है। अधिक precisely, यह sequent calculus की *functional interpretation* का एक variant है, जो स्वयं natural deduction और lambda calculus के बीच Curry-Howard correspondence के analogous है। Combinator rules "premises में conclusions की तुलना में smaller types" दिखाते हैं, जिससे Bit Machine — Simplicity का abstract stack machine interpreter — execution के दौरान data copying को minimize कर पाता है।

### Values Expressions नहीं हैं

Simplicity expressions operations को denote करती हैं, values को नहीं। Notation `scribe b : A ⊢ B` एक unique expression को represent करता है जो हमेशा value `b` return करती है; यह combinator के बजाय notational convenience के रूप में काम करती है। यह Bitcoin Script जैसा है, जहाँ `OP_1` जैसे operations values को directly express करने के बजाय push करते हैं।

### Simplicity का Completeness Theorem

सभी नौ combinators हाथ में होने पर, हम कैसे जानते हैं कि कुछ missing नहीं है — कि ये नौ सच में पर्याप्त हैं? Simplicity Completeness theorem इसका उत्तर देता है: (finite) Simplicity types के बीच किसी भी function के लिए, कोई Simplicity expression उसे denote करती है। Proof constructive है — यह दिखाता है कि expression कैसे build करनी है:

1. **Input decompose करें**: Nested `case` expressions का उपयोग करके, किसी भी type के किसी भी input को उसके constituent bits में पूरी तरह decompose करें
2. **Lookup table build करें**: हर possible input के लिए, corresponding output produce करने हेतु `scribe` का उपयोग करें
3. **Assemble करें**: Nested cases और scribes मिलकर एक विशाल lookup table बनाते हैं जो function implement करता है

यह theorem Rocq proof assistant (formerly Coq) में formally verified है। Proof official Simplicity repository का हिस्सा है और correctness के लिए machine-checked है।

हालांकि completeness theorem guarantee करता है कि Simplicity के नौ combinators (finite) Simplicity types के बीच किसी भी function को express कर सकते हैं, lookup-table construction से resulting expressions impractically large होती हैं। 256-bit inputs पर function को 2²⁵⁶ entries वाली lookup table की आवश्यकता होगी। इसी कारण अगले chapters brute-forcing everything through lookup tables के बजाय computations की structure exploit करने वाली efficient expressions बनाने पर focus करते हैं।

### निष्कर्ष

Simplicity की core language में एक type system और combinators शामिल हैं जो किसी भी finite computation को सक्षम करते हैं। हालांकि Completeness theorem expressiveness की guarantee देता है, generic construction से resulting expressions impractically large होती हैं। Practical Simplicity development में succinct expressions के लिए computational structure exploit करना शामिल है। अगले chapters data structures, transaction interactions और additional combinators explore करते हैं।

# Data Types से Programs तक

<partId>08528a6f-d310-4675-b8cd-4e9b93b3c009</partId>

## Data Types बनाना

<chapterId>9981ae62-ae50-4770-adf2-b253d1e08de3</chapterId>

पिछले chapters में हमने दिखाया कि Simplicity का core set of combinators किसी भी finite pure computation को implement करने के लिए पर्याप्त है। यह chapter दिखाता है कि इन primitives से practical data structures और computations कैसे बनाए जाएँ — उसी तरह जैसे computers logic gates से बनाए जाते हैं।

### Boolean Logic

Boolean type, जिसे `𝟚` से denote किया जाता है, `𝟙 + 𝟙` के बराबर है और इसके दो values हैं: `σᴸ⟨⟩` (false) और `σᴿ⟨⟩` (true)। Core combinators का उपयोग करके Boolean logic operators construct किए जा सकते हैं।

#### And Operation

Logical `and : 𝟚 × 𝟚 ⊢ 𝟚` operation दो bits लेता है और एक bit return करता है। Implementation first bit पर branch करता है: यदि false हो, तो false return करें; अन्यथा second bit return करें।

```
and ≔ case (injl unit) (drop iden) : 𝟚 × 𝟚 ⊢ 𝟚
```

`⟨false, false⟩` के साथ testing:

```
⟦and⟧⟨false, false⟩
 = {expand the notation for false}
⟦and⟧⟨σᴸ⟨⟩, σᴸ⟨⟩⟩
 = {expand the definition of and}
⟦case (injl unit) (drop iden)⟧⟨σᴸ⟨⟩, σᴸ⟨⟩⟩
 = {evaluate case for σᴸ}
⟦injl unit⟧⟨⟨⟩, σᴸ⟨⟩⟩
 = {evaluate injl}
σᴸ(⟦unit⟧⟨⟨⟩, σᴸ⟨⟩⟩)
 = {evaluate unit}
σᴸ⟨⟩
 = {by the notation for false}
false
```

`⟨true, true⟩` के साथ testing:

```
⟦and⟧⟨true, true⟩
 = {expand the notation for true and the definition of and}
⟦case (injl unit) (drop iden)⟧⟨σᴿ⟨⟩, σᴿ⟨⟩⟩
 = {evaluate case for σᴿ}
⟦drop iden⟧⟨⟨⟩, σᴿ⟨⟩⟩
 = {evaluate drop}
⟦iden⟧(σᴿ⟨⟩)
 = {evaluate iden}
σᴿ⟨⟩
 = {by the notation for true}
true
```

#### Other Logic Operations

`not` operation के लिए एक helper combinator की आवश्यकता होती है:

```
                   f : A ⊢ C    g : B ⊢ C
--------------------------------------------------------------
copair f g ≔ iden ▵ unit ⨾ case (take f) (take g) : A + B ⊢ C
```

Initial `iden ▵ unit : A ⊢ A × 𝟙` input में एक empty "environment" जोड़ता है, जिससे `case` combinator apply हो पाता है। दोनों branches में `take` का उपयोग इस empty environment को drop कर देता है ताकि `f` या `g` execute हो सके।

अन्य Boolean logical operations:

- `or ≔ case (drop iden) (injr unit) : 𝟚 × 𝟚 ⊢ 𝟚`
- `not ≔ copair (injr unit) (injl unit) : 𝟚 ⊢ 𝟚`
- `xor ≔ case (drop iden) (drop not) : 𝟚 × 𝟚 ⊢ 𝟚`

### Bit Adders

एक "half-adder" दो bits लेता है और उन्हें add करता है, जिससे two-bit output produce होता है: carry bit और sum bit।

```
half-adder ≔ and ▵ xor : 𝟚 × 𝟚 ⊢ 𝟚 × 𝟚
```

एक "full-adder" तीन bits add करता है, जिससे two-bit output produce होता है। Input nested tuple `(𝟚 × 𝟚) × 𝟚` का उपयोग करता है।

Nested tuples के लिए compact notation का उपयोग किया जाता है:

- `O f` denotes `take f`
- `I f` denotes `drop f`
- `H` denotes `iden`

उदाहरण के लिए, `I O H` का अर्थ है `drop (take iden) : A × (B × C) ⊢ B`, जो middle value extract करता है। यह notation binary digits की याद दिलाता है: nested tuples को binary trees के रूप में सोचते समय, notation tree positions के reversed binary digits को represent करता है। ये expressions Simplicity के लिए De Bruijn indices बनाते हैं।

**Note:** `I`, `O` और `H` notation केवल उन subexpressions पर apply होता है जो सिर्फ `take`, `drop` और `iden` से बने होते हैं।

Full-adder दो half-adders compose करता है, carry bits का logical `or` लेते हुए:

```
full-adder ≔ take half-adder ▵ I H
           ⨾ O O H ▵ (O I H ▵ I H ⨾ half-adder)
           ⨾ (O H ▵ I O H ⨾ or) ▵ I I H
           : (𝟚 × 𝟚) × 𝟚 ⊢ 𝟚 × 𝟚
```

पहली line में, `take half-adder ▵ I H : (𝟚 × 𝟚) × 𝟚 ⊢ (𝟚 × 𝟚) × 𝟚` first two bits पर half-adder चलाता है, last bit को save करते हुए।

दूसरी line में, `O O H ▵ (O I H ▵ I H ⨾ half-adder) : (𝟚 × 𝟚) × 𝟚 ⊢ 𝟚 × (𝟚 × 𝟚)` first bit (first half-adder का carry-out) save करता है और last two bits पर half-adder चलाता है।

Last line में, `(O H ▵ I O H ⨾ or) ▵ I I H: 𝟚 × (𝟚 × 𝟚) ⊢ 𝟚 × 𝟚` first two bits (दोनों half-adders के carry-outs) का logical OR लेता है और second half-adder का sum-out bit return करता है।

यह Simplicity programming को demonstrate करता है: data bits को reference करने के लिए `I`, `O` और `H` notation का उपयोग करना, sequential composition के माध्यम से other functions call करने के लिए suitable "environments" बनाना।

Users low-level operations directly define नहीं करते। इस series में आगे standard library jets पर चर्चा होगी जो common functions implement करते हैं। End users से Bitcoin Script की तरह directly Simplicity में program करने की अपेक्षा नहीं है। इसके बजाय, SimplicityHL जैसी higher-level languages Simplicity code generate करती हैं, subexpression "environments" manage करती हैं और named variables को appropriate `take` और `drop` sequences में translate करती हैं।

### Vectors

Fixed-length vectors type `A` के iterated products बनाकर define किए जाते हैं:

- `A² ≔ A × A`
- `A⁴ ≔ A² × A²`
- `A⁸ ≔ A⁴ × A⁴`
- `…`

इन्हें `A^2`, `A^4`, `A^8` आदि के रूप में लिखा जा सकता है।

Vectors केवल उन lengths के लिए define किए जाते हैं जो powers of two हैं। Other powers में bracketing conventions चुनने की आवश्यकता होती है।

Expression `f : A ⊢ B` दिए जाने पर, repeated pairing इसे fixed-length vectors पर "map" करती है:

- `f² ≔ f ▵ f : A² ⊢ B²`
- `f⁴ ≔ f² ▵ f² : A⁴ ⊢ B⁴`
- `f⁸ ≔ f⁴ ▵ f⁴ : A⁸ ⊢ B⁸`

Function `f : A × B ⊢ B` दिए जाने पर, fixed-length vectors पर iteration या "folding":

- `fold-right-2 f ≔ O O H ▵ (O I H ▵ I H ⨾ f) ⨾ f : A² × B ⊢ B`
- `fold-right-4 f ≔ fold-right-2 (fold-right-2 f) : A⁴ × B ⊢ B`
- `fold-right-8 f ≔ fold-right-2 (fold-right-4 f) : A⁸ × B ⊢ B`

कई variations मौजूद हैं। `f : A × B ⊢ C` दिए जाने पर, paired vectors पर `zip-n f : (Aⁿ × Bⁿ) ⊢ Cⁿ` के साथ "zip" करें। `f : (A × B) × C ⊢ C` दिए जाने पर, paired vectors पर `bifold-right-n f : (Aⁿ × Bⁿ) ⊢ C` के साथ fold करें। `map` और `fold-right` को combine करने से accumulating combinators बनते हैं: `f : A × C ⊢ C × B` से `map-accum-right-n f : Aⁿ × C ⊢ C × Bⁿ` मिलता है। कई और variants संभव हैं।

#### Multi-bit Words

Bit vector multi-bit integers देता है। उदाहरण के लिए, `𝟚³²` 32-bit word type है। `𝟚²⁵⁶` 256-bit word type है, जो hashes और cryptographic operations के लिए suitable है।

Full-adder का उपयोग करके, vector operations का एक variant multi-bit words पर "ripple carry adder" define करता है:

```
full-adder-n ≔ zip-accum-right-n full-adder : (𝟚ⁿ × 𝟚ⁿ) × 𝟚 ⊢ 𝟚 × 𝟚ⁿ
```

`full-adder-n` दो n-bit binary numbers और one-bit carry-input लेता है, और one-bit carry-out flag तथा n-bit sum return करता है।

#### SHA-256

Multi-bit words पर arithmetic operations — subtraction, multiplication, division — और bit-wise logical operations जैसे logical AND, OR, XOR को recursively define करके, और इन्हें बार-बार combine करके, SHA-256 का block compression function भी बनाया जा सकता है:

```
sha256-hash-block ≔ … : 𝟚²⁵⁶ × 𝟚⁵¹² ⊢ 𝟚²⁵⁶
```

SHA-256 compression को Rocq proof assistant (formerly Coq) के भीतर Simplicity का उपयोग करके formally define किया गया है, और formal proof है कि `sha256-hash-block` implementation correct है।

Raw Simplicity के रूप में compression बहुत धीमी चलती है। Jets SHA-256 compression जैसे common functions को natively execute करते हैं। Pure Simplicity implementations jets के लिए formal specifications के रूप में काम करते हैं।

### Option Types

Option types unit type के साथ sum लेने से बनते हैं:

```
Option A ≔ 𝟙 + A
```

Type `Option A` को `A?` या `𝕊 A` (जहाँ `𝕊` का अर्थ "successor" है) के रूप में लिखा जा सकता है। Functions option types पर map करते हैं:

```
                 f : A ⊢ B
------------------------------------------
f? ≔ copair (injl unit) (injr f) : A? ⊢ B?
```

Bind जैसे monadic combinators define किए जा सकते हैं:

```
              f : A ⊢ B?
---------------------------------------
bind f ≔ copair (injl unit) f : A? ⊢ B?
```

### Variable Length Buffers

"Buffers" partially filled vectors के लिए types हैं:

- `Aᑉ² ≔ A?`
- `Aᑉ⁴ ≔ A²? × Aᑉ²`
- `Aᑉ⁸ ≔ A⁴? × Aᑉ⁴`
- `…`

Type `Xᑉ⁸` expand होकर `(1 + X⁴) × ((1 + X²) × (1 + X))` बनता है। इसे polynomial के रूप में treat करके expand करने पर `1 + X + X² + X³ + X⁴ + X⁵ + X⁶ + X⁷` मिलता है। Type के रूप में interpret करने पर, यह X के सभी possible tuples के sum को represent करता है, length 7 तक, empty tuple सहित। यह exactly उन lists का type है जिनकी length strictly less than 8 है।

Vectors की तरह, buffers पर mapping और folding operations define किए जा सकते हैं। Stack operations में `push-<n : Aᑉⁿ × A ⊢ Aⁿ + Aᑉⁿ` और `pop-<n : Aᑉⁿ ⊢ (Aᑉⁿ × A)?` शामिल हैं। `push-<n` buffer में item append करता है, overflow होने पर full vector return करता है। `pop-<n` item remove करता है, smaller buffer और removed item return करता है, और यदि original buffer empty था तो optionally nothing return करता है।

`push-<n` definition, recursively:

```
push-<2 ≔ case (drop (injr (injr iden))) (injl iden)

push-<4 ≔ ((O I H ▵ IH) ⨾ push-<2) ▵ O O H
        ⨾ case (I H ▵ O H ⨾ case (injr (injr (I H) ▵ injl unit)) (injl iden))
               (injr (I H ▵ O H))

push-<8 ≔ ((O I H ▵ IH) ⨾ push-<4) ▵ O O H
        ⨾ case (I H ▵ O H ⨾ case (injr (injr (I H) ▵ (injl unit ▵ injl unit))) (injl iden))
               (injr (I H ▵ O H))

…
```

Raw Simplicity certain complexity levels के बाद follow करना कठिन हो जाती है। End users SimplicityHL जैसी higher-level languages का उपयोग करते हैं, जो ये idiomatic expressions generate करती हैं।

### निष्कर्ष

इस chapter ने दिखाया कि bits से logical operations कैसे बनाए जाएँ। इनसे bit-level arithmetic उभरी, जिससे execution के बारे में reasoning संभव हुई। Vector types विकसित किए गए, जिन्होंने arithmetic definition के लिए multi-bit words पर iteration demonstrate किया। आगे बढ़ते हुए, SHA-256 और Schnorr signature validation जैसे cryptographic operations को केवल Simplicity combinators का उपयोग करके define किया जा सकता है — ये सभी वास्तव में Simplicity का उपयोग करके define किए गए हैं।

यह chapter Simplicity में build किए जा सकने वाले सभी possible data types और operations का comprehensive guide नहीं है, बल्कि यह illustrate करता है कि Simplicity की constraints के भीतर practical functionality कैसे प्राप्त की जाती है। Finitely bounded types के बावजूद, useful vectors, buffer types, और इन structures पर iterate करने वाले operations define किए जा सकते हैं।

Actual standard library operation specifications यहाँ की definitions से थोड़े अलग हैं। उदाहरण के लिए, full-adder दो half-adders के बजाय 3-way XOR और "majority" logic function का उपयोग करता है।

Practice में, Simplicity programs arithmetic और cryptographic operations के लिए jets का उपयोग करते हैं। हालांकि, jets केवल expressions को replace करते हैं। Buffers और vectors पर iterate करने वाले combinators को jets से replace नहीं किया जा सकता, और वे actual Simplicity programs में दिखाई देते हैं। हालांकि इन्हें directly use करने के बजाय, end users SimplicityHL जैसी higher-level languages का उपयोग करते हैं, जो ऐसी expressions generate करती हैं।

Recursively defined combinators expression size में exponentially grow करते हुए दिखाई देते हैं। यह problematic नहीं है। Serialization के दौरान, expressions trees के बजाय DAGs (directed acyclic graphs) के रूप में encoded होती हैं। Actual representation केवल linearly grow करती है।

अब तक केवल pure computations पर विचार किया गया। Transactions sign करने जैसे tasks के लिए transaction data के साथ interaction हेतु कुछ ऐसा तरीका चाहिए जिससे signatures invalid होने पर programs fail हो सकें। अगला chapter Simplicity में side-effects पर चर्चा करता है।

## दो Side Effects

<chapterId>9eafe498-0765-419a-a69d-a74a9cdf3713</chapterId>

पिछले chapters में हमने दिखाया कि Simplicity के core set of combinators का उपयोग करके कुछ data structures और computations कैसे बनाए जाएँ। जैसा हमने note किया, core combinators किसी भी finite pure computation को implement करने के लिए पर्याप्त हैं। इससे सवाल उठता है: और क्या हासिल किया जा सकता है? हम अपनी expressions में additional side effects जोड़ सकते हैं।

Expressions के लिए कई तरह के possible side effects हैं: state update, log में लिखना, exception throw करना, environment से पढ़ना, continuation call करना, आदि। Simplicity में available side effects application पर depend करेंगे।

Bitcoin और Liquid applications के लिए, हमारे पास currently दो side effects हैं: Failure effect, जो एक exception effect है जहाँ exception का type `𝟙` है, और Reader effect, जो transaction environment से data access करने की अनुमति देता है। हमारे core combinators "pure" हैं; उनके कोई side effects नहीं हैं। हालांकि, jets ऐसे नए primitives introduce कर सकते हैं जिनमें side effects होते हैं।

### Effects वाले Jets

हम इस course में बाद में jets के बारे में और बात करेंगे, लेकिन यहाँ हम उनके side effects illustrate करने के लिए कुछ example jets introduce करते हैं।

#### Bip0340-verify

`bip0340-verify : (𝟚²⁵⁶ × 𝟚²⁵⁶) × 𝟚⁵¹² ⊢ 𝟙` एक expression के लिए jet है जो x-only pubkey, 256-bit message और Schnorr signature लेता है, और कुछ भी return नहीं करता! अपने type के अनुसार, इसे `unit` की तरह ही behave करना चाहिए। Difference jet के side effect में है: यदि signature validation fail होता है, तो पूरी computation exception (unit type की) throw करके abort कर दी जाती है। यह Failure effect है।

#### Verify

`verify : 𝟚 ⊢ 𝟙` Failure effect express करने के लिए barebones jet है। यदि `verify` का input `false` है, तो पूरी computation exception throw करके abort कर दी जाती है। यदि input `true` है, तो कुछ भी return नहीं होता, लेकिन computation continue कर सकती है।

#### Transaction Hashes

`sig-all-hash : 𝟙 ⊢ 𝟚²⁵⁶` एक constant function प्रतीत होता है, क्योंकि केवल एक possible input value है: empty tuple। हालांकि, यह jet transaction environment से पढ़ता है और transaction data का hash produce करता है, जो Bitcoin Script के signature verification में उपयोग किए जाने वाले `SIGHASH_ALL` message digest के analogous है। यह Reader effect का उदाहरण है: return किया गया value उस transaction environment पर depend करता है जिसके भीतर jet execute होता है। कई अन्य hashing jets हैं जो signatures के लिए custom message digests build करने में मदद करने हेतु transaction environment data के various subsets hash करते हैं।

#### Introspection Jets

`input-sequence : 𝟚³² ⊢ 𝟚³²?` एक function है जो input index लेता है और उस input के लिए transaction का sequence number return करता है, यदि index bounds से बाहर हो तो optionally nothing return करता है। फिर से, output value input index का pure function नहीं है; बल्कि operation output value determine करने के लिए transaction environment access करने हेतु Reader effect का उपयोग करता है। कई अन्य introspection jets हैं जो transaction environment data के various fragments return करते हैं।

### Effects को classify करना

सभी side effects समान नहीं बनाए जाते। कुछ side effects दूसरों से बेहतर behave करते हैं। हम effects को इस आधार पर classify कर सकते हैं कि वे program transformations के लिए कितने amenable हैं।

#### Commutative Effects

Commutative effect वह है जहाँ, यदि आप दो expressions के outputs को swap करते हैं, तो आप expression के effect को बदले बिना safely expressions को स्वयं swap कर सकते हैं। `swap = I H ▵ O H : A × B ⊢ B × A` पर विचार करें। यदि side effects वाली हर expression `f` और `g` के लिए `f ▵ g ⨾ swap = g ▵ f` है, तो effects commutative हैं।

Environment से transaction data पढ़ना commutative effect है क्योंकि environment से पढ़ने का result same होता है, चाहे हम reading को किसी भी order में execute करें।

General रूप से, exception throw करना commutative effect नहीं है। यदि `f` कोई exception `e₁` throw करता है और `g` कोई अन्य exception `e₂` throw करता है, तो `f` और `g` की pair से कौन-सा exception throw होगा यह उनके execution order पर depend करता है।

हालांकि, Failure effect के special case में, जिसमें केवल unit typed exception throw किया जा सकता है, effect commutative है। `f` या `g` में से कोई भी exception throw करे, resulting exception same होगा, क्योंकि केवल एक possible exception value है।

#### Idempotent Effects

Idempotent effect वह है जहाँ, यदि आप किसी expression के output को duplicate करते हैं, तो आप expression के effect को बदले बिना safely expression को स्वयं duplicate कर सकते हैं। `dup = iden ▵ iden : A ⊢ A × A` पर विचार करें। यदि side effects वाले हर `f` के लिए `f ⨾ dup = dup ⨾ f ▵ f` है, तो effects idempotent हैं।

Environment से transaction data पढ़ना idempotent effect है। Exception throw करना भी idempotent effect है। हालांकि दो duplicated expressions में से केवल एक execute होगी, `dup ⨾ f ▵ f` द्वारा throw किया गया कोई भी exception `f ⨾ dup` द्वारा throw किए गए exception के समान होगा।

हालांकि, log में लिखना idempotent नहीं हो सकता, क्योंकि effect को duplicate करने से log message दो बार appear होगा। लेकिन यदि log messages की _list_ के बजाय messages का _set_ हो, तो effect idempotent (और commutative) होगा क्योंकि set insertion स्वयं idempotent operation है।

#### Unitary Effects

Unitary effect वह है जहाँ, यदि आप किसी expression के output को discard करते हैं, तो आप expression के effects को बदले बिना safely expression को स्वयं discard कर सकते हैं। यदि side effects वाले हर `f` के लिए हमेशा `f ⨾ unit = unit` हो, तो आपके effects unitary हैं।

Environment से data पढ़ना unitary effects के कुछ types में से एक है। यदि transaction environment से data पढ़ने का result discard कर दिया जाता है, तो read perform करने वाली पूरी expression discard की जा सकती है।

Failure effect unitary नहीं है। यदि `f` exception throw करता है, तो `f ⨾ unit` भी करेगा; computation abort होने से पहले execution `unit` combinator तक पहुँचेगी ही नहीं। दूसरी ओर, `unit` obviously कोई exception throw नहीं करेगा, इसलिए `f ⨾ unit` और `unit` के effects अलग होंगे।

संक्षेप में, ऊपर चर्चा किए गए effects इन तीन properties के सामने इस प्रकार हैं:

| Effect | Commutative | Idempotent | Unitary |
| --- | :---: | :---: | :---: |
| Reader (transaction environment) | ✓ | ✓ | ✓ |
| Failure (unit-typed exception) | ✓ | ✓ | ✗ |
| Writer (set के रूप में log) | ✓ | ✓ | ✗ |
| General exceptions (arbitrary type) | ✗ | ✓ | ✗ |

### Simplicity में allowed effects

किसी effect type में जितनी अधिक well-behaved properties होंगी, Simplicity optimizer के पास उन effects का उपयोग करने वाले programs को transform करने की उतनी अधिक room होगी। आदर्श रूप से हम केवल ऐसे effects allow करते जिनमें तीनों properties हों: commutative, idempotent और unitary। इससे optimizer को किसी भी sort का program transformation perform करने की अनुमति मिलती। हालांकि, environment से पढ़ना ही एकमात्र effect है जो तीनों properties satisfy करता है।

इसके बजाय हम demand करते हैं कि Simplicity effects commutative और idempotent हों। Simplicity में हम जिन दोनों effects का उपयोग करते हैं, Failure effect और Reader effect, वे commutative और idempotent हैं। इससे Simplicity code पर optimizations की एक बड़ी class perform की जा सकती है।

हालांकि, ऊपर described "discard" transformation, `f ⨾ unit` को `unit` से replace करने का प्रयास, या कोई similar transformation allowed नहीं है यदि `f` Failure effect produce कर सकता है। सचमुच, कल्पना करें कि `f` में `bip0340-verify` assertion हो। उस check को optimize away करने का प्रयास disastrous होगा।

### Side Effects आखिर allow क्यों करें?

Simplicity side effects को आखिर allow क्यों करती है? क्या यह बेहतर नहीं होता कि हर program पूरे transaction को input के रूप में ले और Boolean output return करे जो decide करे कि transaction valid है या नहीं?

#### Batch Verification

Failure effect होने का एक कारण Schnorr signatures की [batch verification](https://github.com/bitcoin/bips/blob/c9a6ca6297eb8de850f6b64dafb8e60ee9b64d66/bip-0340.mediawiki#batch-verification) support करना है। Batch verification में, कई individual Schnorr signature checks को इस तरह pool किया जाता है कि यदि कोई single signature check fail होता है, तो पूरा batch fail होता है।

यह batching procedure हर signature को individually verify करने की तुलना में efficiency improve करता है। Downside यह है कि यदि batch verification fail होता है, तो हमें यह पता नहीं चलता कि कौन-सा specific signature check या checks fail हुए।

Failure side effect का उपयोग करके, `bip0340-verify` ensure करता है कि यदि signature check fail होता है, तो पूरी transaction fail हो। यदि `bip0340-verify` success या failure के लिए इसके बजाय Boolean type `𝟚` return करता, तो failing signature check अभी भी ऐसी branch तक ले जा सकता था जहाँ script succeed हो। ऐसे case में हमें जानना पड़ता कि particular signature valid है या नहीं, और इसलिए हम batch verification का advantage नहीं ले पाते।

#### Precomputed Transaction Data

Early Bitcoin Script में एक problem यह थी कि signatures के लिए message digests बनाने में उपयोग किया जाने वाला hashing function transaction के size में linear था। Typically हर input signature verification के लिए कम-से-कम एक message digest बनाता है, इसलिए overall hashing की amount transaction size में quadratic थी।

यह problem Segwit और Bitcoin Script के बाद के iterations में message digests को redefine करके fix की गई ताकि उन्हें per signature check constant time में compute किया जा सके। यह `PrecomputedTransactionData` होने पर rely करता है, जो transaction data के hashes को एक बार precompute करता है और फिर प्रत्येक input के sighash computations द्वारा share किया जाता है। Simplicity के transaction hashing jets उसी kind के precomputed transaction data पर rely करते हैं ताकि ensure हो कि jets constant time में run करें।

मान लीजिए `sig-all-hash` Reader effect का उपयोग नहीं करता। मान लीजिए हम किसी तरह transaction environment के लिए Simplicity type build करने में सफल हो गए। इसे `TxEnv` कहें, ताकि `sig-all-hash : TxEnv ⊢ 𝟚²⁵⁶` jet का type हो। ऐसी definition के लिए `sig-all-hash` jet को किसी भी transaction का hash compute करने में सक्षम होना पड़ेगा, सिर्फ उस transaction का नहीं जिसमें वह involved है। Simplicity programs दिए गए `TxEnv` को copy कर सकते थे और उसकी modified copy `sig-all-hash` को pass कर सकते थे। ऐसे case में `sig-all-hash` `PrecomputedTransactionData` पर rely नहीं कर सकता था, और हम वापस इस version of `sig-all-hash` को pass किए गए किसी भी transaction data में linear time require करने पर आ जाते।

क्योंकि `sig-all-hash : 𝟙 ⊢ 𝟚²⁵⁶` transaction data access करने के लिए Reader effect का उपयोग करता है, उसे _केवल_ fixed transaction environment तक access मिलता है। इसी कारण jet का implementation safely `PrecomputedTransactionData` का उपयोग कर सकता है और constant time में operate कर सकता है।

### Cross-Input Signature Aggregation

हालांकि इस समय न Liquid और न Bitcoin [cross-input signature aggregation](https://hrf.org/latest/cisa-research-paper/) support करते हैं, हम check करना चाहेंगे कि समय आने पर Simplicity इसके साथ compatible हो सके।

हालांकि details work out नहीं किए गए हैं, हम imagine करते हैं कि half-aggregation को Writer effect का उपयोग करके implement किया जाएगा। अर्थात, `half-agg-verify : (𝟚²⁵⁶ × 𝟚²⁵⁶) × 𝟚²⁵⁶ ⊢ 𝟙` जैसे type वाला नया jet public key, message digest और Schnorr signature के `r`-component (Schnorr signature में `r`-component और `s`-component होते हैं) लेगा और execution continue करने से पहले उसे transaction log में लिखेगा। फिर, transaction में कहीं और या transaction के साथ, सभी half-aggregated Schnorr signatures के लिए aggregate `s`-component provide किया जाएगा। Transaction केवल तब valid होगी जब सभी logged keys, messages और `r`-components के लिए ऐसा aggregate `s`-component provide किया गया हो।

Simplicity की requirements meet करने के लिए, इस Writer effect को idempotent और commutative होना चाहिए। यह writer log को key, message, `r`-component tuples के set के रूप में treat करके ensure किया जा सकता है। यह काम करता है क्योंकि set operations idempotent और commutative हैं। Log को values के set के रूप में treat करना half-aggregation verification algorithm के साथ compatible होगा।

### निष्कर्ष

इस chapter में हमने Simplicity कर सकने वाली computations में side effects जोड़ने को देखा। हमने विभिन्न kinds of effects को इस आधार पर classify किया कि वे various kinds of program transformation के संबंध में कितने well-behaved हैं। हमने Simplicity के effects को commutative और idempotent effects तक restrict करने का निर्णय लिया।

Bitcoin और Liquid applications के लिए हम जिन दो effects का उपयोग करते हैं, वे Reader effect हैं, transaction environment access करने के लिए, और Failure effect, program को abort और fail करने के लिए। कुछ jets primitive operations का उपयोग करते हैं जहाँ इस तरह के side effects occur हो सकते हैं।

Failure effect Simplicity program का output determine करता है: program या तो fail होता है, जिससे transaction invalid हो जाती है, या program succeed करता है। Reader effect Simplicity program को एक sort का input provide करता है: transaction data containing environment। लेकिन हमें digital signatures जैसे other inputs भी Simplicity programs को provide करने होते हैं।

अगले chapter में हम देखेंगे कि Simplicity programs क्या होते हैं, उन्हें addresses में कैसे बदला जाता है, और signatures जैसे other inputs को Simplicity programs में कैसे जोड़ा जाता है।

## Programs और Addresses

<chapterId>961652e3-8f7d-4c2a-8b55-9a990b91a0dd</chapterId>

पिछले chapter में हमने Simplicity में उपयोग होने वाले दो side effects describe किए: Failure effect, जो program की success या failure determine करता है, और Reader effect, जो transaction environment तक access provide करता है। अब हम practical question की ओर मुड़ते हैं: Simplicity program आखिर है क्या, और यह blockchain पर address कैसे बनता है?

### Simplicity Programs

Simplicity program को type `𝟙 ⊢ 𝟙` की Simplicity expression के रूप में define किया जाता है। इस type signature का अर्थ है कि program कोई meaningful input नहीं लेता (सिर्फ unit value) और कोई meaningful output produce नहीं करता (सिर्फ unit value)। Reader effect transaction environment input capture करता है, जबकि Failure effect success या failure indicate करता है। ये effects Simplicity types themselves के बजाय I/O handle करते हैं।

### Commitment Merkle Root

Complete programs को on-chain store करने के बजाय, Bitcoin commitments का उपयोग करता है — यह practice Pay-to-Script-Hash (P2SH) से extend होती है। Simplicity Commitment Merkle Root (CMR) का उपयोग करती है।

प्रत्येक combinator को pattern `Simplicity␟Commitment␟[identifier]` से derived SHA-256 tag मिलता है, जहाँ `␟` ASCII code 31 (unit separator) को represent करता है।

प्रत्येक tag नीचे listed corresponding pre-image string का SHA-256 hash है:

| कॉम्बिनेटर | Tag pre-image (ASCII string) |
|---|---|
| `iden` | `Simplicity␟Commitment␟iden` |
| `unit` | `Simplicity␟Commitment␟unit` |
| `comp` | `Simplicity␟Commitment␟comp` |
| `pair` | `Simplicity␟Commitment␟pair` |
| `case` | `Simplicity␟Commitment␟case` |
| `take` | `Simplicity␟Commitment␟take` |
| `drop` | `Simplicity␟Commitment␟drop` |
| `injl` | `Simplicity␟Commitment␟injl` |
| `injr` | `Simplicity␟Commitment␟injr` |

फिर Simplicity expression को प्रत्येक combinator के लिए उसके arguments के CMRs के साथ tagged SHA-256 midstate compute करके recursively 256-bit CMR में hash किया जाता है (expression `e` के CMR के लिए `#ᶜ(e)` लिखें, और byte concatenation के लिए `∥`):

| कॉम्बिनेटर | CMR नियम |
|---|---|
| `iden` | `#ᶜ(iden) = SHA-256-midstate(tag_iden ∥ tag_iden)` |
| `unit` | `#ᶜ(unit) = SHA-256-midstate(tag_unit ∥ tag_unit)` |
| `comp f g` | `#ᶜ(comp f g) = SHA-256-midstate(tag_comp ∥ tag_comp ∥ #ᶜ(f) ∥ #ᶜ(g))` |
| `pair f g` | `#ᶜ(pair f g) = SHA-256-midstate(tag_pair ∥ tag_pair ∥ #ᶜ(f) ∥ #ᶜ(g))` |
| `case f g` | `#ᶜ(case f g) = SHA-256-midstate(tag_case ∥ tag_case ∥ #ᶜ(f) ∥ #ᶜ(g))` |
| `take f` | `#ᶜ(take f) = SHA-256-midstate(tag_take ∥ tag_take ∥ 32·0x00 ∥ #ᶜ(f))` |
| `drop f` | `#ᶜ(drop f) = SHA-256-midstate(tag_drop ∥ tag_drop ∥ 32·0x00 ∥ #ᶜ(f))` |
| `injl f` | `#ᶜ(injl f) = SHA-256-midstate(tag_injl ∥ tag_injl ∥ 32·0x00 ∥ #ᶜ(f))` |
| `injr f` | `#ᶜ(injr f) = SHA-256-midstate(tag_injr ∥ tag_injr ∥ 32·0x00 ∥ #ᶜ(f))` |

Binary combinators (`comp`, `pair`, `case`) दोनों children के CMRs concatenate करते हैं; unary combinators (`take`, `drop`, `injl`, `injr`) अपने single child के CMR को 32 bytes of `0x00` padding के बाद concatenate करते हैं; और nullary leaves (`iden`, `unit`) केवल अपने tag को hash करते हैं। दो conventions इसे compute करने में cheap रखते हैं: SHA-256 midstates का उपयोग किया जाता है ताकि **प्रत्येक expression को SHA-256 compression function की अधिकतम एक call** चाहिए (assuming constant tags तक का midstate precomputed है), और one-argument constructors अपने argument से पहले 32 bytes of `0x00` padding prefix करते हैं, जिससे implementations चाहें तो थोड़ा extra precomputation कर सकती हैं।

`unit` combinator के लिए — एक nullary constructor जिसमें कोई argument sub-expressions नहीं हैं — यह rule specialize होकर `#ᶜ(unit) = SHA-256-midstate(tag_unit ∥ tag_unit)` बनता है, जहाँ `tag_unit = SHA-256(Simplicity␟Commitment␟unit)` है (tag दो बार feed किया जाता है)। Trivial `unit` program के लिए resulting CMR है:

```
0xc40a10263f7436b4160acbef1c36fba4be4d95df181a968afeab5eac247adff7
```

महत्वपूर्ण रूप से, CMR Simplicity expressions के types को commit नहीं करता; इसके बजाय redemption के दौरान type inference पर rely करता है।

### Addresses

Addresses BIP-0341 के Taproot mechanism का उपयोग करते हैं, जिसमें CMRs TapLeaf version `0xbe` के अंतर्गत committed होते हैं। Process में शामिल है:

1. Version byte, CMR length और CMR itself को combine करने वाला TapLeaf tagged hash compute करना
2. Internal public key को tweak करना (जब key-spend path desired न हो तो NUMS point का उपयोग करते हुए)
3. Bech32m format में convert करना
4. Appropriate checksums add करना

जब key-spend path desired नहीं होता, internal public key को **NUMS** ("Nothing-Up-My-Sleeve") point पर set किया जाता है: एक curve point जिसे जानबूझकर ऐसा चुना गया है कि कोई उसका discrete logarithm न जानता हो — दूसरे शब्दों में, ऐसा point जिसके लिए कोई corresponding private key नहीं है। क्योंकि कोई भी उसके लिए signature कभी produce नहीं कर सकता, key-spend path provably unusable है, और output *केवल* committed Simplicity script path के माध्यम से spend किया जा सकता है। Real application में, इस NUMS point को BIP-0341 की recommendation के अनुसार randomized किया जाना चाहिए, ताकि बिना key-spend path वाले outputs ordinary Taproot outputs से indistinguishable हों (privacy benefit)।

#### Simplicity से Address तक

आइए सबसे simple possible program के लिए पूरी derivation देखें: `unit : 𝟙 ⊢ 𝟙`, एक no-op जो हमेशा succeed करता है।

**1. Combinator tag.** पहले `unit` tag compute करें:

```
tag_unit = SHA-256(Simplicity␟Commitment␟unit)
         = 0xd723083cff3c75e29f296707ecf2750338f100591c86e0c71717f807ff3cf69d
```

**2. CMR.** Program का CMR प्राप्त करने के लिए tag को दो बार feed करें:

```
CMR = #ᶜ(unit) = SHA-256-midstate(tag_unit ∥ tag_unit)
    = 0xc40a10263f7436b4160acbef1c36fba4be4d95df181a968afeab5eac247adff7
```

**3. TapLeaf hash.** CMR को Simplicity के TapLeaf version `0xbe` और CMR length `0x20` (32 bytes) से prefix करें, फिर Elements TapLeaf tagged hash लें (tagged hash है `hash_str(x) = SHA-256(SHA-256(str) ∥ SHA-256(str) ∥ x)`):

```
hash_TapLeaf/elements(0xbe ∥ 0x20 ∥ CMR)
  = 0x44cc38311ec7e5dfb7b573baf38449496ecd334eb5509cfed1b4fd30da8dd41c
```

केवल इसी one leaf के साथ कोई TapBranches नहीं हैं, इसलिए यह hash पहले से ही TapTree root है।

**4. TapTweak.** चूँकि हम no key-spend path चाहते हैं, हम internal key के रूप में BIP-0341 NUMS point का उपयोग करते हैं और TapTree root से उसे tweak करते हैं:

```
internal_pk = 0x50929b74c1a04954b78b4b6035e97a5e078a5a0f28ec96d547bfee9ace803ac0
t = hash_TapTweak/elements(internal_pk ∥ 0x44cc38311ec7e5dfb7b573baf38449496ecd334eb5509cfed1b4fd30da8dd41c)
  = 0xb3bef172389b0937d7e5a8b15cfa41e776777f13f2f659cb06220a6ff0658285
```

**5. Output key.** Internal key को curve पर tweak करें, `output_pk = lift_x(internal_pk) ⊕ t·G` (elliptic-curve arithmetic यहाँ summarized है), जिससे x-only output key `0x2cb0c20acd7340b4d4b65f6a60e2888d0d64e3267261f3b3cf7290e5af3f9e09` मिलती है।

**6. Bech32m address.** X-only output key encode करें, `p` prefix करें (SegWit v1 witness-version character), Liquid-testnet human-readable prefix `tex1` add करें, और Bech32m checksum append करें। Final address है:

```
tex1p9jcvyzkdwdqtf49kta4xpc5g35xkfcexwfsl8v70w2gwttelncyshxjk56
```

यह बहुत काम था — लेकिन इसका बड़ा हिस्सा Taproot द्वारा ही mandated है, Simplicity द्वारा नहीं।

### Witness Expressions

एक नया combinator type Simplicity programs में input के absence को address करता है: witness expression। `witness` combinator signature data और other witness material को programs में integrate करने की अनुमति देता है।

```
      w : B
-----------------
witness w : A ⊢ B
```

Witness expression की semantics straightforward है: यह अपने input को ignore करती है और simply value `w` return करती है (जो किसी भी Simplicity type की हो सकती है), यानी `⟦witness w⟧(a) = w`। यह **कोई नई expressiveness** नहीं जोड़ता — completeness theorem के अनुसार, Simplicity पहले से ऐसी कोई भी constant function build कर सकती है (previous chapters से `scribe` macro याद करें)। `witness` combinator का point पूरी तरह उसके **CMR** में है: value `w` expression के CMR से **excluded** होती है, इसलिए `w` known होने से पहले address compute किया जा सकता है, और `w` redemption time पर supplied होता है।

यह design choice pruning support करती है — unexecuted conditional branches को on-chain reveal करने की आवश्यकता नहीं होती, उनके associated witness expressions सहित। जब कोई branch pruned होती है, verifier को pruned subtree का केवल CMR चाहिए, उसकी actual content नहीं।

### Witness Values

यह limitation लग सकती है कि witness expression केवल एक *value* hold कर सकती है, कोई अधिक general Simplicity expression नहीं। लेकिन UTXO-based blockchains के लिए programs केवल एक बार execute होते हैं। Witness node में पूरी sub-expression pass करने की आवश्यकता नहीं है: user उस sub-expression को themselves, off-chain, simply run कर सकता है, और उसी result को प्राप्त करने के लिए उसके output को witness value में transcribe कर सकता है।

(इस course में आगे हम `disconnect` combinator से मिलेंगे, जो बहुत कुछ witness expression जैसा behave करता है जो अपने argument के रूप में पूरी Simplicity expression *लेता है*।)

Alternative design यह होता कि सभी witness data को top-level Simplicity program के argument के रूप में feed किया जाए। Witness expressions दो कारणों से preferred हैं। पहला, **pruning**: `case` expressions की unexecuted branches कभी on-chain reveal नहीं होतीं, और उन branches के भीतर कोई भी witness expressions उनके साथ ही prune हो जाती हैं। दूसरा, **locality**: witness expressions हमें प्रत्येक witness value को exactly वहाँ रखने देती हैं जहाँ उसका उपयोग होता है, बजाय उसे program के top-level input से नीचे thread करने के।

### Type Inference

चूँकि CMRs types को commit नहीं करते, type system redemption के दौरान reconstruct किया जाता है। Simplicity का type inference algorithm combinator structure के आधार पर प्रत्येक subexpression के minimal types determine करता है। अधिक precisely, inference हर subexpression का *principal* (most general) type compute करता है; जो type variables free बचते हैं उन्हें फिर unit type `𝟙` से instantiate किया जाता है, जिससे program के लिए unique, minimal type मिलता है।

### निष्कर्ष

इस chapter में हमने establish किया कि Simplicity programs type `𝟙 ⊢ 𝟙` की expressions हैं, समझाया कि Commitment Merkle Roots प्रत्येक combinator के tagged SHA-256 hashes से कैसे construct होते हैं, और दिखाया कि CMRs BIP-0341 Taproot के माध्यम से on-chain addresses में कैसे बदले जाते हैं। हमने witness expressions को spending time पर signature data और other inputs provide करने के mechanism के रूप में introduce किया, बिना address creation time पर उनके values पर commit किए।

# अंतिम खंड

<partId>96952535-4aa6-4e78-91e2-d12e9df895d4</partId>

## समीक्षाएँ और रेटिंग्स

<chapterId>fb0b0133-39ea-497b-bd36-198be42c4fab</chapterId>
<isCourseReview>true</isCourseReview>

## अंतिम परीक्षा

<chapterId>2cc5e818-abcb-4a0a-9991-7a492c572e2d</chapterId>
<isCourseExam>true</isCourseExam>

## निष्कर्ष

<chapterId>8ade24bd-a84f-4d25-8f64-bdfa8b58926c</chapterId>
<isCourseConclusion>true</isCourseConclusion>
