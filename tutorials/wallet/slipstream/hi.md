---
name: Slipstream
description: Slipstream के साथ signed transaction को Bitcoin network पर broadcast किए बिना सीधे miner को भेजना
---

![कवर](assets/cover.webp)

आम तौर पर, जब आप किसी transaction पर sign करते हैं, तो वह network के हर Bitcoin node पर अपने-आप broadcast हो जाता है। फिर वह mined होने का इंतज़ार करता है।

हालाँकि, जब तक वह किसी block में शामिल नहीं होता, कोई attacker जिसने आपकी private key हासिल कर ली हो, उसे replace करके funds चुरा सकता है। ऐसा आम तौर पर तब हो सकता है जब आप ColdCard hardware wallet का उपयोग करते हैं।

Mining company MARA का Slipstream tool आपको transaction को network पर broadcast करने से bypass करने देता है: इसे सीधे (और केवल) एक miner को भेजा जाता है, जो इसे private रखता है और network पर expose होने से बचाता है। Transaction को mine होने में शायद ज़्यादा समय लगेगा, लेकिन यह replacement attack से सुरक्षित रहेगा।

नीचे, हम एक tutorial दे रहे हैं जिससे [Liana](https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04) users, साथ ही [Sparrow](https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d) wallet users, [outofband.wizardsardine.com](https://outofband.wizardsardine.com/) page के ज़रिए miner MARA के Slipstream tool का उपयोग कर सकें।

⚠️ **चेतावनी**: यह tool केवल कुछ profiles के लिए है, मुख्य रूप से Liana wallets, miniscript wallets और कुछ प्रकार के multisig। Wizardsardine **स्पष्ट रूप से सलाह देता है कि** इसे ऐसे wallets के लिए इस्तेमाल न करें जिनके funds पहले से theft के critical risk में हैं, उदाहरण के लिए वे wallets जिनकी recovery phrase किसी ऐसे ColdCard device पर generate की गई थी जो random number generator vulnerability से प्रभावित है। ऐसी स्थिति में attacker के खिलाफ race seconds की होती है, और single miner को भेजी गई transaction normally broadcast की गई transaction की तुलना में confirm होने में कहीं ज़्यादा समय लेती है। अगर यह बात आप पर लागू होती है, तो पहले हमारा dedicated tutorial पढ़ें:

https://planb.academy/tutorials/wallet/hardware/coldcard-seed-vulnerability-1348b153-89db-429c-80af-b5d3d8506b9a

## Liana users के लिए

Liana को Wizardsardine maintain करता है, जो [outofband.wizardsardine.com](https://outofband.wizardsardine.com/) page का publisher है, इसलिए रास्ता सीधा है: आप transaction को broadcast करने के बजाय बस signed PSBT file export करते हैं।

*Prerequisite: आपके Liana wallet में funds होने चाहिए।*

### Step 1: Liana के साथ अपना transaction बनाएँ

हमेशा की तरह, destination address, description और amount जोड़कर अपना transaction build करें (यहाँ, wallet में उपलब्ध maximum amount)।

Fee rate set करने के लिए:

- नीचे बाईं ओर, "Coins selection" के नीचे छोटे box पर click करके वे coins select करें जिन्हें आप spend करना चाहते हैं;
- फिर fee rate enter करें। याद रखें कि fees को suggested rate से काफ़ी ज़्यादा set करना है, जैसा इस page पर बताया गया है: [outofband.wizardsardine.com](https://outofband.wizardsardine.com/)।

अंत में, "Next" पर click करें।

![Liana में transaction build करना](assets/fr/01.webp)

### Step 2: अपने transaction details check करें

"Sign" पर click करने से पहले, अपने transaction details check करें; ख़ास तौर पर:

- भेजी गई amount;
- transaction fees के लिए allocate किए गए satoshis की संख्या;
- लेकिन सबसे ज़रूरी, वह address जिस पर आप funds भेज रहे हैं ("address poisoning" attacks से बचने के लिए address के पहले 5/6 characters, आख़िरी 5/6, और address के बीच के 5/6 characters check करना याद रखें)।

![Transaction details check करना](assets/fr/02.webp)

### Step 3: Signing wallets select करें

इसके बाद, वे software और/या hardware wallets select करें जिनसे आपको अपना transaction sign करना है। एक quick reminder: 2-of-2 multisig wallet के मामले में, आपको 2 में से 2 signatures चाहिए।

### Step 4: अपने transaction की PSBT file export करें

Bitcoin transaction अब appropriate keys से signed है। "Broadcast" पर click न करें, वरना यह पूरे network के साथ share हो जाएगा और, अगर आप ColdCard hardware wallet का उपयोग करते हैं, तो आपका transaction publicly expose हो जाएगा और आपके funds risk में होंगे।

अब आप "Export" पर click कर सकते हैं, फिर PSBT file को अपने computer पर locally save कर सकते हैं।

![Liana से PSBT file export करना](assets/fr/03.webp)

### Step 5: outofband.wizardsardine.com के ज़रिए transaction miner को भेजें

अब final steps। Transaction को miner को भेजने के लिए, आपको बस PSBT file लेनी है और उसे designated area में drag and drop करना है।

![PSBT file को outofband.wizardsardine.com पर drop करना](assets/fr/04.webp)

Transaction फिर नीचे दिखाए गए रूप में display होता है।

![Queue में transaction](assets/fr/05.webp)

### Step 6: Slipstream के ज़रिए transaction भेजें

अंत में, आपको बस "Send" पर click करना है ताकि transaction Slipstream के ज़रिए MARA को भेजा जा सके।

![Slipstream के ज़रिए transaction भेजना](assets/fr/06.webp)

कुछ seconds के भीतर, transaction "Sending" से "Accepted" में बदल जाता है:

![Slipstream द्वारा transaction accepted](assets/fr/07.webp)

अब बस transaction identifier (TXID) copy करना है, फिर उसे [mempool.space](https://mempool.space/) में paste करना है ताकि आप उसे mined होते हुए watch कर सकें:

![mempool.space पर TXID देखना](assets/fr/08.webp)

कृपया ध्यान दें: transaction "Transaction not found" के रूप में दिखेगा जब तक कि miner, MARA, कोई block mine करके आपकी transaction को उसमें include नहीं कर देता। इसमें कई tens of minutes, या hours भी लग सकते हैं, क्योंकि MARA के पास Bitcoin network के hash rate का केवल लगभग 4.5% है। 4 August 2026 तक, यह लगभग हर 3 hours और 45 minutes में mine किए गए एक block के बराबर है।

## Other wallets के users के लिए

अगर आप [Liana](https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04) use नहीं करते लेकिन फिर भी tool use करना चाहते हैं, तो यहाँ 2-of-2 multisig wallet का उपयोग करने वाला tutorial है। इसके लिए हम [Sparrow](https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d) software wallet का उपयोग करेंगे।

*Prerequisite: आपके Sparrow wallet में funds होने चाहिए।*

### Step 1: अपना transaction बनाएँ

[Sparrow](https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d) के साथ, अपने multisig wallet पर transaction बनाएँ। याद रखें कि fees को suggested rate से काफ़ी ज़्यादा set करना है, जैसा इस page पर बताया गया है: [outofband.wizardsardine.com](https://outofband.wizardsardine.com/)।

बनाने के बाद, "Create Transaction" पर click करें।

![Sparrow में transaction बनाना](assets/fr/09.webp)

### Step 2: अपना transaction finalize करें

अपने transaction को finalize करने के लिए, अब आपको इसे sign करना होगा। ऐसा करने के लिए, "Finalize Transaction for Signing" पर click करें।

![Signing के लिए transaction finalize करना](assets/fr/10.webp)

### Step 3: अपनी अलग-अलग keys से transaction sign करें

अब transaction sign करने का समय है। ऐसा करने के लिए, बस उसे उन software या hardware wallet(s) से sign करें जिनका आप उपयोग करते हैं।

![Multisig keys से transaction sign करना](assets/fr/11.webp)

### Step 4: Signed transaction download करें, और उसे network पर broadcast न करें

Bitcoin transaction अब हमारे 2-of-2 multisig की दोनों keys से signed है। "Broadcast Transaction" पर click न करें, वरना यह पूरे network के साथ share हो जाएगा और, अगर आप ColdCard hardware wallet का उपयोग करते हैं, तो आपका transaction publicly expose हो जाएगा और आपके funds risk में होंगे।

![Signed transaction, ready but broadcast नहीं](assets/fr/12.webp)

### Step 5: Signed transaction script display करें, या PSBT file download करें

Signed Bitcoin transaction display करने के लिए, अब "View Final Transaction" पर click करें। फिर आप signed Bitcoin transaction script copy कर सकते हैं:

*02000000000101ade28cc43b2f51e09c88a87dfaeda8a601a78cddb458e47d99f0651020c1aaa60000000000fdffffff010b370000000000002200201810640a195e5a992d1f6da58a9781f77db47ac63a332b072580cc5b57dd1c2e04004730440220320777c52799cc8015be7c3f724a3d77906ce3d551205c893347910279ed796a02204ee45912623c1c45bf3d93d6558d878737f88f20dcbd152dc28fac80e788f2aa01473044022008bf6ea8432e3fee0eaa7edb923f60e44bb5eb37e52a93d8fdb4e30814340b0f0220473f8fcfbadda9c86fdfc4d3dd55c7883f62312794361e4d4d93f52964bce6520147522102bd28ad9b52829baf62621821abb49339262c7ef32f8adf15bf01b4d91fb5a9a72103ace1a518996275cbf9ebdbeaa4703318a50d5ab7f0fe22b9e566d2f2f644ed3752ae9fa90e00*

![Signed transaction script display करना](assets/fr/13.webp)

अगर आप transaction file download करना चाहते हैं, तो आप या तो:

- "File" पर click करें, फिर "Save transaction…" पर;
- या नीचे दाईं ओर network connection button (yellow button) पर click करें, फिर "Save Final Transaction" पर click करें।

Transaction फिर आपके computer पर locally save हो जाएगा।

![Final transaction को locally save करना](assets/fr/14.webp)

### Step 6: outofband.wizardsardine.com के ज़रिए transaction miner को भेजें

अब final steps। Transaction को miner को भेजने के लिए, आपको बस यह करना है:

- [outofband.wizardsardine.com](https://outofband.wizardsardine.com/) पर जाएँ;
- पिछले step में copy किया गया signed transaction script paste करें, फिर नीचे "ADD TO QUEUE" पर click करें;

![Transaction script को tool में paste करना](assets/fr/15.webp)

- या file लें और उसे designated area में drag and drop करें।

![Transaction file को tool पर drop करना](assets/fr/16.webp)

Transaction फिर नीचे दिखाए गए रूप में display होता है।

![Queue में transaction](assets/fr/17.webp)

अगर कोई message आपको बताता है कि आपकी transaction में satoshis का total input amount unknown है (और परिणामस्वरूप, fees के लिए satoshis की संख्या compute नहीं की जा सकती), तो आपको बस satoshis का total input amount manually enter करना होगा। इसे find करने के लिए, Sparrow में अपनी transaction के display पर, diagram के बीच में, बस click करें:

![Sparrow में दिखाया गया total input amount](assets/fr/18.webp)

फिर उस amount (हमारे example में 15,904 sats) को [outofband.wizardsardine.com](https://outofband.wizardsardine.com/) tool में enter करें:

![Total input amount manually enter करना](assets/fr/19.webp)

अंत में, check करें कि fee rate सही है।

### Step 7: Slipstream के ज़रिए transaction भेजें

अंत में, आपको बस "Send" पर click करना है ताकि transaction Slipstream के ज़रिए MARA को भेजा जा सके।

![Slipstream के ज़रिए transaction भेजना](assets/fr/20.webp)

कुछ seconds के भीतर, transaction "Sending" से "Accepted" में बदल जाता है:

![Slipstream द्वारा transaction accepted](assets/fr/21.webp)

अब बस transaction identifier (TXID) copy करना है, फिर उसे [mempool.space](https://mempool.space/) में paste करना है ताकि आप उसे mined होते हुए watch कर सकें:

![mempool.space पर TXID देखना](assets/fr/22.webp)

कृपया ध्यान दें: transaction "Transaction not found" के रूप में दिखेगा जब तक कि miner, MARA, कोई block mine करके आपकी transaction को उसमें include नहीं कर देता। इसमें कई tens of minutes, या hours भी लग सकते हैं, क्योंकि MARA के पास Bitcoin network के hash rate का केवल लगभग 4.5% है। 4 August 2026 तक, यह लगभग हर 3 hours और 45 minutes में mine किए गए एक block के बराबर है।
