---
name: Coinjoin समन्वयक - वाबीसाबी
description: WabiSabi प्रोटोकॉल (Wasabi Wallet 2.0 में प्रयुक्त) का पालन करते हुए कॉइनजॉइन कोऑर्डिनेटर को कैसे सेटअप और रन करें
---

![cover](assets/cover.webp)


---

## परिचय 👋


इस विशेषज्ञ गाइड में हम आपको कॉइनजॉइन कोऑर्डिनेटर स्थापित करने में मदद करेंगे, जो मूल रूप से एक ऐसा सर्वर है जो उन लोगों को एक साथ लाता है जो लेन-देन शुल्क बचाना चाहते हैं या सहयोगी लेन-देन में अपनी ऑनचेन गोपनीयता बढ़ाना चाहते हैं। चूंकि Wasabi Wallet के साथ अब कोई कंपनी द्वारा संचालित कोऑर्डिनेटर नहीं आता है, इसलिए उपयोगकर्ताओं को अपना पसंदीदा कोऑर्डिनेटर सर्वर ढूंढना और चुनना होगा। कुछ ही कोऑर्डिनेटर ऐसे हैं जो शून्य समन्वय शुल्क लेते हैं, इसलिए Wasabi Wallet के डेवलपर्स आपके लिए अपना खुद का कम्युनिटी कोऑर्डिनेटर शुरू करना जितना संभव हो उतना आसान बनाने के लिए कड़ी मेहनत कर रहे हैं (Raspberry Pi5 जैसे छोटे हार्डवेयर पर भी!)। वर्तमान में सक्रिय कोऑर्डिनेटर जो शून्य समन्वय शुल्क लेते हैं, उन्हें [LiquiSabi](https://liquisabi.com) और उससे भी महत्वपूर्ण बात, [nostr](https://github.com/Kukks/WasabiNostr) पर पाया जा सकता है।


## आवश्यकताएँ 🫴



- वीपीएस (होस्टेड नोड) या कंप्यूटर/सर्वर (सेल्फ-होस्टेड नोड)
- प्रून्ड/फुल Bitcoin कोर नोड (v29.0 के साथ परीक्षण किया गया)


वैकल्पिक:


- (उप)डोमेन नोड पर ट्रैफ़िक अग्रेषित करता है (उदाहरण के लिए coinjoin.[yourdomain].io)


कमांडलाइन प्रॉम्प्ट और बैश का कुछ अनुभव होना अनुशंसित है, क्योंकि सभी चरणों को स्वचालित नहीं किया जा सकता है।


हार्डवेयर के लिहाज से, निम्नलिखित सुविधाओं वाला सिस्टम होना उचित है:


- 4 कोर
- 16 जीबी रैम
- 2 TB SSD या NVMe (फुल-नोड के लिए) / 128 GB SSD (pruned-नोड के लिए)


ऐसी आवश्यकताओं को मात्र 120 डॉलर में एक रास्पबेरी पाई 5 द्वारा पूरा किया जा सकता है, जिसमें स्टोरेज की लागत शामिल नहीं है, जो 2TB NVMe स्टिक के लिए लगभग 100 डॉलर है।


सस्ते वीपीएस में आमतौर पर केवल 1 कोर और 4 जीबी रैम होती है, जो मैंने पाया है कि ब्लॉकहाइट 911817 पर पूरे बिटकॉइन blockchain को सिंक और सत्यापित करने के लिए बहुत कम है।


स्टोरेज के लिहाज से, एक फुल-नोड के लिए कम से कम 2TB डिस्क स्टोरेज की आवश्यकता होगी, अधिमानतः SSD या NVMe प्रकार की। blockchain को छोटा करते समय इससे भी छोटी स्टोरेज ड्राइव (जैसे 128GB SSD) स्वीकार्य है।


यदि आप बड़े (300+ इनपुट) कॉइनजॉइन के लिए एक कोऑर्डिनेटर चलाने का इरादा रखते हैं, तो सभी हस्ताक्षर सत्यापन के लिए उच्च प्रदर्शन वाले तेज/नए कोर वाले सिस्टम का चयन करने की सलाह दी जाती है।


## स्थापना 🛠️


जिस नोड पर हम Wasabi Wallet का नवीनतम संस्करण डाउनलोड और इंस्टॉल करना चाहते हैं, उसमें wallet के साथ-साथ बैकएंड और कोऑर्डिनेटर भी स्टैंडअलोन निष्पादन योग्य फ़ाइलों के रूप में शामिल हैं।


नवीनतम संस्करण [Wasabi Wallet](https://github.com/WalletWasabi/WalletWasabi/releases) खोजें और इस रिलीज़ के PGP हस्ताक्षर को इन कुंजियों के साथ सत्यापित करें: [PGP.txt](https://raw.githubusercontent.com/WalletWasabi/WalletWasabi/refs/heads/master/PGP.txt)


हार्डवेयर (सीपीयू आर्किटेक्चर) और ऑपरेटिंग सिस्टम के चुनाव के आधार पर डिप्लॉयमेंट की प्रक्रिया अलग-अलग होती है। नीचे रास्पबेरी पाई (ARM-64) के लिए Debian आधारित RaspiBlitz को शुरुआती बिंदु मानते हुए विभिन्न विवरण दिए गए हैं। Nix का उपयोग करके (X86-64) Ubuntu ऑपरेटिंग सिस्टम को डिप्लॉय करने के लिए आगे बढ़ें।


स्थापना संबंधी निर्देश यहां देखें: [वासाबी दस्तावेज़](https://docs.wasabiwallet.io/using-wasabi/InstallPackage.html)


### RaspiBlitz/Debian तैनाती


RaspiBlitz (v1.11 के साथ परीक्षण किया गया) नोड्स के लिए, स्रोत कोड से निर्मित script परिनियोजन का उपयोग किया जा सकता है: [home.admin/config.scripts/bonus.wasabi.sh](https://github.com/kravens/raspiblitz/blob/dev/home.admin/config.scripts/bonus.wasabi.sh)



### आसान तैनाती


न्यूनतम तैनाती के लिए, आपको बस अपने प्लेटफ़ॉर्म के लिए निष्पादन योग्य फ़ाइलों को एक फ़ोल्डर में निकालना होगा।

Debian/Ubuntu के लिए उदाहरण कमांडलाइन कोड:


```
wget https://github.com/WalletWasabi/WalletWasabi/releases/download/v2.7.2/Wasabi-2.7.2.deb
wget https://github.com/WalletWasabi/WalletWasabi/releases/download/v2.7.2/Wasabi-2.7.2.deb.asc
wget https://raw.githubusercontent.com/WalletWasabi/WalletWasabi/refs/heads/master/PGP.txt
gpg --import PGP.txt
gpg --verify Wasabi-2.7.2.deb.asc Wasabi-2.7.2.deb
```


इसके परिणामस्वरूप निम्नलिखित वैध हस्ताक्षर संदेश प्राप्त होना चाहिए:


```
gpg: Signature made Mon Nov 17 01:33:09 2025 CET
gpg:                using RSA key 6FB3872B5D42292F59920797856348328949861E
gpg: Good signature from "zkSNACKs <zksnacks@gmail.com>" [unknown]
gpg: WARNING: This key is not certified with a trusted signature!
gpg:          There is no indication that the signature belongs to the owner.
Primary key fingerprint: 6FB3 872B 5D42 292F 5992  0797 8563 4832 8949 861E
```


और अब आप डाउनलोड किए गए पैकेज को इंस्टॉल कर सकते हैं:


```
sudo apt install ./Wasabi-2.7.2.deb
```



## कॉन्फ़िगरेशन 🧾


कोऑर्डिनेटर चलाने से पहले आपको Config.json फ़ाइल को अपने अनुसार संपादित करना होगा:


- Bitcoin RPC प्रमाण पत्र
- पसंदीदा दौर पैरामीटर
- समन्वयक विस्तारित सार्वजनिक कुंजी (एकत्रित धूल प्राप्त करने के लिए एक नया SegWit wallet बनाएं)

**चेतावनी**: Taproot और wallet का उपयोग करने से UTXO नष्ट हो जाएगा! कृपया यहाँ नेटिव सेगविट wallet का उपयोग करें।


- अनुमत इनपुट और आउटपुट पता प्रकार
- nostr पर प्रकाशन के लिए उद्घोषक कॉन्फ़िगरेशन (नाम, विवरण, यूआरआई, न्यूनतम इनपुट, nostr रिले, nostr निजी कुंजी)


आप कोऑर्डिनेटर को केवल .onion पते के माध्यम से ही एक्सेस करने योग्य बना सकते हैं, या अपने कस्टम क्लियरनेट डोमेन का उपयोग कर सकते हैं।


इस पथ पर कॉन्फ़िगरेशन फ़ाइल ढूंढें या बनाएं:


`~/.walletwasabi/coordinator/Config.json`


इसे इस कमांड से संपादित करें:


```
sudo nano ~/.walletwasabi/coordinator/Config.json
```


इस उदाहरण Config.json को देखें:


```
{
"Network": "Main",
"MainNetBitcoinRpcUri": "http://localhost:8332",
"TestNetBitcoinRpcUri": "http://localhost:48332",
"RegTestBitcoinRpcUri": "http://localhost:18443",
"BitcoinRpcConnectionString": "your_bitcoin_rpcuser:your_bitcoin_rpcpassword",
"ConfirmationTarget": 21,
"DoSSeverity": "0.02",
"DoSMinTimeForFailedToVerify": "1d 21h 0m 0s",
"DoSMinTimeForCheating": "1d 0h 0m 0s",
"DoSPenaltyFactorForDisruptingConfirmation": 0.2,
"DoSPenaltyFactorForDisruptingSignalReadyToSign": 1.0,
"DoSPenaltyFactorForDisruptingSigning": 1.0,
"DoSPenaltyFactorForDisruptingByDoubleSpending": 3.0,
"DoSMinTimeInPrison": "0d 0h 20m 0s",
"MinRegistrableAmount": "0.000021",
"MaxRegistrableAmount": "1000.00",
"AllowNotedInputRegistration": true,
"StandardInputRegistrationTimeout": "0d 0h 21m 0s",
"BlameInputRegistrationTimeout": "0d 0h 3m 0s",
"ConnectionConfirmationTimeout": "0d 0h 1m 0s",
"OutputRegistrationTimeout": "0d 0h 1m 0s",
"TransactionSigningTimeout": "0d 0h 1m 0s",
"FailFastOutputRegistrationTimeout": "0d 0h 3m 0s",
"FailFastTransactionSigningTimeout": "0d 0h 1m 0s",
"RoundExpiryTimeout": "0d 0h 5m 0s",
"MaxInputCountByRound": 100,
"MinInputCountByRoundMultiplier": 0.21,
"MinInputCountByBlameRoundMultiplier": 0.21,
"RoundDestroyerThreshold": 375,
"CoordinatorExtPubKey": "xpub_fill_in_your_new_wallet_here",
"CoordinatorExtPubKeyCurrentDepth": 0,
"MaxSuggestedAmountBase": "100.00",
"RoundParallelization": 1,
"CoordinatorIdentifier": "CoinJoinCoordinatorIdentifier",
"AllowP2wpkhInputs": true,
"AllowP2trInputs": true,
"AllowP2wpkhOutputs": true,
"AllowP2trOutputs": true,
"AllowP2pkhOutputs": true,
"AllowP2shOutputs": true,
"AllowP2wshOutputs": true,
"DelayTransactionSigning": false,
"AnnouncerConfig": {
"CoordinatorName": "Your Coordinator Name",
"IsEnabled": true,
"CoordinatorDescription": "Privacy is a human right!",
"CoordinatorUri": "https://coinjoin.yourdomain/",
"AbsoluteMinInputCount": 21,
"ReadMoreUri": "https://coinjoin.yourdomain/",
"RelayUris": [
"wss://relay.primal.net"
],
"Key": "nsec_your_coordinator_nostr_privatekey"
},
"PublishAsOnionService": true,
"OnionServicePrivateKey": your_onion_service_private_key
}
```

### टोर कॉन्फ़िगरेशन 🧅


अपनी OnionServicePrivateKey भरने के लिए, संभवतः आपको पहले एक कुंजी जनरेट करनी होगी।


यदि आप Config.json फ़ाइल में ```"PublishAsOnionService": true,``` सेट करके पहली बार Wasabi Wallet चलाते हैं, तो यह आपके लिए एक निजी कुंजी उत्पन्न करेगा।


इस कमांड के साथ कोऑर्डिनेटर को एक बार चलाएं:


```
ASPNETCORE_URLS="http://localhost:5001" wcoordinator
```


अपने ओनियन हिडन सर्विस एड्रेस को देखने के लिए, कोऑर्डिनेटर लॉग्स को निम्न प्रकार से जांचें:


```
cat ~/.walletwasabi/coordinator/Logs.txt | grep .onion
```


और आपको कुछ इस तरह का मिलेगा:


```
2026-01-09 21:21:21.210 [14] INFO       TorProcessManagerService.StartAsync (50)        Coordinator server listening on http://acoo3vgmo4rawaeujh6wckurymm2fp4ojauoag6zwov3pryyopis47qd.onion
```


.onion पर समाप्त होने वाला लंबा URL आपका हिडन सर्विस एड्रेस या कोऑर्डिनेटरयूआरआई है।


या फिर अपने कोऑर्डिनेटर कॉन्फ़िगरेशन फ़ाइल को दोबारा जांचें:


```
cat ~/.walletwasabi/coordinator/Config.json | grep CoordinatorUri
```


जो अब अपने आप भर जाना चाहिए।


## दौड़ना ⚡


सभी कॉन्फ़िगरेशन पैरामीटर सेट हो जाने के बाद, आप कोऑर्डिनेटर सेवा चला सकते हैं और अपने पहले राउंड की घोषणा शुरू कर सकते हैं 🕶️


कोऑर्डिनेटर को बस इस कमांड से शुरू करें:


```
ASPNETCORE_URLS="http://localhost:5001" wcoordinator
```


आप Tor ब्राउज़र में .onion फ़ाइल की जाँच करके वर्तमान दौर और पंजीकृत UTXO/सिक्कों की संख्या की निगरानी कर सकते हैं:


```
http://coinjoin.yourdomain/wabisabi/human-monitor/
```


![detected](assets/en/01.webp)


### वैकल्पिक: डिबगिंग समन्वयक सर्वर


आप `~/.walletwasabi/backend/Logs.txt` पर स्थित लॉग फ़ाइल में किसी भी समस्या या त्रुटि की निगरानी कर सकते हैं।


सामान्य समस्याओं में RPC कनेक्शन संबंधी समस्याएं शामिल हैं, इसे ```~/.bitcoin/bitcoin.conf``` में निम्न प्रकार से सक्षम करना होगा:


```
[main] # or [test] for testnet
rpcbind=127.0.0.1
rpcuser=your_bitcoin_rpcuser
rpcpassword=your_bitcoin_rpcpassword
```


### वैकल्पिक: बैकएंड सर्वर चलाना


समन्वयक के साथ मिलकर आप उन उपयोगकर्ताओं के लिए एक बैकएंड सर्वर भी प्रदान कर सकते हैं जिनके पास शुल्क अनुमान और ब्लॉकफ़िल्टर के लिए कनेक्ट करने हेतु अपना स्वयं का बिटकॉइन नोड नहीं है।


इस सेवा को निम्न कमांड से प्रारंभ करें:


```
wbackend
```


## वासाबी उपयोगकर्ताओं को अपने समन्वयक में आमंत्रित करें 🫂


अन्य उपयोगकर्ताओं को आपकी सेवा ढूंढने में मदद करने के लिए आप नोस्ट्र उद्घोषक पर भरोसा कर सकते हैं, या अपने डोमेन (क्लियरनेट) या छिपी हुई सेवा (.onion लिंक) के साथ एक मैजिक लिंक साझा कर सकते हैं और इस तरह के पैरामीटर का उपयोग कर सकते हैं:


```
name=Your%20Coordinator%20Name&network=main&coordinatorUri=https://coinjoin.yourdomain&coordinationFeeRate=0&readMore=https://coinjoin.yourdomain/&absoluteMinInputCount=21
```


जब कोई उपयोगकर्ता मैजिक लिंक को कॉपी करता है और अपना Wasabi Wallet खोलता है, तो सॉफ़्टवेयर स्वचालित रूप से आपके डोमेन और मापदंडों के साथ समन्वयक संवाद प्रदर्शित करेगा।


![detected](assets/en/02.webp)


💚🍣 बिटकॉइन की गोपनीयता को विकेंद्रीकृत करने पर हार्दिक बधाई 🕶️


अपना प्रशिक्षण याद रखें [wasabika](https://docs.wasabiwallet.io/FAQ/FAQ-Contribution.html#you-can-become-a-wasabika), Wasabi Wallet केवल रक्षा के लिए है 🛡️