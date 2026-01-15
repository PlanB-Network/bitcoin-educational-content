---
name: Kali
description: वर्चुअलबॉक्स पर बूटेबल यूएसबी स्टिक के रूप में या दोहरे बूट के रूप में, चरण दर चरण काली लिनक्स स्थापित करना।
---

![cover-kali](assets/cover.webp)



## परिचय



### काली लिनक्स क्यों?



**काली लिनक्स** एक लिनक्स वितरण है जो आईटी सुरक्षा में विशेषज्ञता रखता है।


हम काली लिनक्स का उपयोग क्यों करते हैं:





- यह पेनटेस्टिंग टूल्स (सिस्टम और नेटवर्क सुरक्षा परीक्षण) की एक विस्तृत श्रृंखला के साथ पूर्व-कॉन्फ़िगर किया गया है।
- यह **ओपन सोर्स और निःशुल्क** है, इसलिए आप इसे स्वतंत्र रूप से उपयोग और संशोधित कर सकते हैं।
- यह **विश्वसनीय और सुरक्षित** है, साइबर सुरक्षा के बारे में सीखने के लिए आदर्श है।
- यह आपको परीक्षण-तैयार वातावरण में लिनक्स का उपयोग करना सीखने की सुविधा देता है।
- इसे विभिन्न तरीकों से स्थापित किया जा सकता है: **वर्चुअलबॉक्स**, **बूटेबल यूएसबी कुंजी**, या **डुअल बूट**।



## स्थापना और कॉन्फ़िगरेशन



### 1. पूर्वापेक्षाएँ



**उपकरणों की आवश्यकता:**





- 64-बिट प्रोसेसर** (इंटेल या एएमडी)।
- न्यूनतम 8 जीबी रैम** (हल्के इंस्टॉलेशन या वीएम के लिए 4 जीबी पर्याप्त हो सकती है)।
- काली लिनक्स स्थापित करने के लिए 50 जीबी मुक्त डिस्क स्थान**।
- आईएसओ छवि और अद्यतन डाउनलोड करने के लिए इंटरनेट कनेक्शन**।
- बूट करने योग्य मीडिया बनाने के लिए न्यूनतम 8 जीबी यूएसबी कुंजी** (यदि आप पीसी पर काली स्थापित करना चाहते हैं या लाइव यूएसबी पर इसका परीक्षण करना चाहते हैं)।



किसी मौजूदा पीसी पर इंस्टॉल करने से पहले अपने डेटा का बैकअप लेना महत्वपूर्ण है।



### 2. डाउनलोड करें





- [kali.org/get-kali](https://www.kali.org/get-kali/#kali-platforms) पर जाएं
- अपने अनुप्रयोग के लिए ISO छवि का चयन करें:
  - छवि स्थापित करें** : पीसी स्थापना के लिए।
  - वर्चुअल इमेज**: वर्चुअलबॉक्स या वीएमवेयर पर काली को स्थापित करने के लिए।
- ISO छवि डाउनलोड करें.



![Page de téléchargement Kali](assets/fr/01.webp)



![Sélection de la version Kali](assets/fr/02.webp)



### 3. बूट करने योग्य USB कुंजी बनाएँ



आप कई उपकरणों का उपयोग कर सकते हैं, जैसे कि बलेना एचर:





- [Balena Etcher](https://etcher.balena.io/) डाउनलोड और इंस्टॉल करें।



![Page de téléchargement Balena Etcher](assets/fr/03.webp)



![Installation de Balena Etcher](assets/fr/04.webp)





- Balena Etcher खोलें, फिर Kali ISO छवि का चयन करें।
- गंतव्य मीडिया के रूप में USB कुंजी का चयन करें.
- फ़्लैश पर क्लिक करें और प्रक्रिया समाप्त होने तक प्रतीक्षा करें।



![Utilisation de Balena Etcher](assets/fr/05.webp)



### 4. काली लिनक्स को स्थापित करना और सुरक्षित करना



#### 4.1 USB कुंजी पर बूट करना





- कंप्यूटर बंद करें.
- यूएसबी कुंजी (जिसमें काली लिनक्स है) प्लग करें।
- अपने कंप्यूटर को चालू करें। हाल ही के पीसी पर, सिस्टम को USB बूट कुंजी को स्वचालित रूप से पहचान लेना चाहिए। यदि ऐसा नहीं होता है, तो BIOS/UEFI एक्सेस कुंजी (आमतौर पर F2, F12 या Delete, ब्रांड के आधार पर) को दबाकर रीबूट करें।
  - BIOS/UEFI मेनू में, बूट डिवाइस के रूप में अपनी USB कुंजी का चयन करें।
  - सहेजें और पुनः आरंभ करें.



#### 4.2 इंस्टॉलेशन लॉन्च करना



##### स्टार्टअप स्क्रीन



यूएसबी स्टिक से बूट करते समय, Kali Linux बूट स्क्रीन दिखाई देनी चाहिए। **ग्राफ़िकल इंस्टॉलेशन** और **टेक्स्ट इंस्टॉलेशन** में से चुनें। इस उदाहरण में, हमने ग्राफ़िकल इंस्टॉलेशन चुना है।



![capture](assets/fr/06.webp)



यदि आप **लाइव** छवि का उपयोग करते हैं, तो आपको एक अन्य मोड, **लाइव** दिखाई देगा, जो डिफ़ॉल्ट स्टार्टअप विकल्प भी है।



![Mode Live](assets/fr/07.webp)



##### भाषा चयन



स्थापना और सिस्टम के लिए अपनी पसंदीदा भाषा चुनें।



![Sélection de la langue](assets/fr/08.webp)



कृपया अपना भौगोलिक स्थान बताएं।



![Options d'accessibilité](assets/fr/09.webp)



##### कीबोर्ड कॉन्फ़िगरेशन



अपना कीबोर्ड लेआउट चुनें. यह जाँचने के लिए एक परीक्षण फ़ील्ड उपलब्ध है कि कुंजियाँ आपके कॉन्फ़िगरेशन के अनुरूप हैं या नहीं.



![Configuration du clavier](assets/fr/10.webp)



##### नेटवर्क कनेक्शन



इंस्टॉलेशन अब आपके नेटवर्क इंटरफेस को स्कैन करेगा, DHCP सेवा खोजेगा, और फिर आपको अपने सिस्टम के लिए एक होस्ट नाम दर्ज करने के लिए कहेगा। नीचे दिए गए उदाहरण में, हमने होस्ट नाम के रूप में **"kali "** दर्ज किया है।



![Configuration réseau](assets/fr/11.webp)



आप वैकल्पिक रूप से एक डिफ़ॉल्ट डोमेन नाम प्रदान कर सकते हैं जिसका उपयोग यह सिस्टम करेगा (मान DHCP से प्राप्त किए जा सकते हैं या यदि कोई पूर्व-मौजूदा ऑपरेटिंग सिस्टम मौजूद है)।



![Choix du type d'installation](assets/fr/12.webp)



##### उपयोगकर्ता खाते



इसके बाद, सिस्टम के लिए उपयोगकर्ता खाता बनाएं (पूरा नाम, उपयोगकर्ता नाम और एक मजबूत पासवर्ड)।



![Création d'un utilisateur](assets/fr/13.webp)



![Mode d'installation](assets/fr/14.webp)



![Sélection des applications](assets/fr/15.webp)



##### समय क्षेत्र



सिस्टम समय सेट करने के लिए अपना भौगोलिक क्षेत्र चुनें.



![Sélection du fuseau horaire](assets/fr/16.webp)



##### विभाजन प्रकार



इसके बाद इंस्टॉलर आपकी डिस्क को स्कैन करता है और आपके कॉन्फ़िगरेशन के आधार पर कई विकल्प प्रदर्शित करता है।



इस गाइड में, हम एक **रिक्त डिस्क** से शुरू करते हैं, जिसमें **चार संभावित विकल्प** दिए गए हैं।


हम **गाइडेड - संपूर्ण डिस्क का उपयोग करें** का चयन करेंगे, क्योंकि यहाँ हम Kali Linux (एकल बूट) की एकमुश्त स्थापना कर रहे हैं। इसका मतलब है कि कोई अन्य ऑपरेटिंग सिस्टम नहीं रहेगा, और पूरी डिस्क को मिटाया जा सकता है।



यदि आपकी डिस्क में पहले से ही डेटा मौजूद है, तो एक अतिरिक्त विकल्प **निर्देशित - सबसे बड़ा सन्निहित खाली स्थान का उपयोग करें** प्रदर्शित हो सकता है।



यह विकल्प आपको मौजूदा डेटा को हटाए बिना काली लिनक्स स्थापित करने की अनुमति देता है, जिससे यह किसी अन्य सिस्टम के साथ दोहरी बूटिंग के लिए आदर्श बन जाता है।



हमारे मामले में, डिस्क खाली है, इसलिए यह विकल्प दिखाई नहीं देता है।



![Choix du partitionnement](assets/fr/17.webp)



विभाजित की जाने वाली डिस्क का चयन करें.



![capture](assets/fr/18.webp)



अपनी आवश्यकताओं के आधार पर, आप अपनी सभी फ़ाइलों को एक ही विभाजन में रखना चुन सकते हैं (डिफ़ॉल्ट व्यवहार) या एक या अधिक शीर्ष-स्तरीय निर्देशिकाओं के लिए अलग-अलग विभाजन रख सकते हैं।



यदि आप निश्चित नहीं हैं कि आप क्या चाहते हैं, तो **एकल पार्टीशन में सभी फ़ाइलें** विकल्प चुनें।



![capture](assets/fr/19.webp)



![capture](assets/fr/20.webp)



इससे पहले कि इंस्टॉलेशन प्रोग्राम कोई अपरिवर्तनीय बदलाव करे, आपके पास अपनी डिस्क कॉन्फ़िगरेशन की जाँच करने का एक आखिरी मौका होगा। _Continue_ पर क्लिक करने के बाद, इंस्टॉलेशन प्रोग्राम लॉन्च हो जाएगा और इंस्टॉलेशन लगभग पूरा हो जाएगा।



![capture](assets/fr/21.webp)



##### एन्क्रिप्टेड LVM



यदि यह विकल्प पिछले चरण में सक्षम किया गया था, तो Kali Linux अब आपसे LVM पासवर्ड मांगने से पहले एक सुरक्षित हार्ड डिस्क मिटा देगा।



कृपया मजबूत पासवर्ड का उपयोग करें, अन्यथा कमजोर passphrase के बारे में चेतावनी प्रदर्शित की जाएगी।



##### प्रॉक्सी जानकारी



काली लिनक्स अनुप्रयोगों को वितरित करने के लिए रिपॉजिटरी का उपयोग करता है। यदि आपका वातावरण किसी प्रॉक्सी का उपयोग करता है, तो आपको आवश्यक प्रॉक्सी जानकारी दर्ज करनी होगी।



अगर आप **निश्चित नहीं** हैं कि प्रॉक्सी का इस्तेमाल करना है या नहीं, तो **खाली छोड़ दें**। गलत जानकारी दर्ज करने से रिपॉजिटरी से कनेक्शन नहीं हो पाएगा।



![capture](assets/fr/22.webp)



##### मेटापेट्स



यदि नेटवर्क एक्सेस कॉन्फ़िगर नहीं किया गया है, तो आपको संकेत मिलने पर **आगे कॉन्फ़िगर** करना होगा।



यदि आप **लाइव** छवि का उपयोग कर रहे हैं, तो अगला चरण प्रदर्शित नहीं होगा।



फिर आप उन मेटापैकेजों को चुन सकते हैं जिन्हें आप इंस्टॉल करना चाहते हैं। डिफ़ॉल्ट विकल्प एक मानक Kali Linux सिस्टम इंस्टॉल करेंगे, इसलिए आपको कुछ भी बदलने की ज़रूरत नहीं होगी।



![capture](assets/fr/23.webp)



#### स्टार्ट-अप जानकारी



फिर GRUB बूट लोडर की स्थापना की पुष्टि करें।



![capture](assets/fr/24.webp)



##### पुनः आरंभ करें



अंत में, अपने नए Kali Linux इंस्टॉलेशन को पुनः आरंभ करने के लिए जारी रखें पर क्लिक करें।



![capture](assets/fr/25.webp)



#### 4.3 स्थापना के बाद Kali Linux को अद्यतन और कॉन्फ़िगर करना



नए इंस्टॉलेशन के बाद अपने सिस्टम को अपडेट करना एक महत्वपूर्ण कदम है। आपके पास दो विकल्प हैं:



##### विकल्प 1: ग्राफ़िकल यूज़र इंटरफ़ेस (GUI) के माध्यम से



डेबियन/उबंटू की तरह, काली एक एकीकृत ग्राफिकल अपडेट प्रबंधक प्रदान करता है।



1. **मुख्य मेनू** (आपके डेस्कटॉप के आधार पर ऊपर बाईं ओर या नीचे) पर क्लिक करें।


2. **"सॉफ्टवेयर अपडेटर"** खोलें।


3. यह उपकरण:




    - अद्यतन किये जाने वाले पैकेजों की जांच करें।
    - आपको एक सूची (आकार और संस्करण के साथ) दिखाई देगी।
    - आपको एक क्लिक से अपडेट लॉन्च करने की अनुमति देता है।


4. संकेत मिलने पर अपना व्यवस्थापक पासवर्ड (`sudo`) दर्ज करें।


5. इसे इंस्टॉल होने दें और यदि आवश्यक हो तो पुनः आरंभ करें।



##### विकल्प 2: टर्मिनल के माध्यम से



टर्मिनल खोलें और चलाएँ:



```bash
# Mettre à jour les dépôts et le système
sudo apt update && sudo apt full-upgrade -y

# Nettoyage
sudo apt autoremove -y && sudo apt autoclean
```



दैनिक कार्य के लिए **रूट** खाते का उपयोग करना उचित नहीं है; इसके बजाय एक गैर-रूट उपयोगकर्ता बनाएं।



अपने टर्मिनल में ये कमांड टाइप करें:



```bash
sudo adduser yourname
sudo usermod -aG sudo yourname
```



लॉग आउट करें और नए उपयोगकर्ता के साथ पुनः लॉग इन करें।



आइए कुछ बुनियादी काली लिनक्स कार्यों को एक तालिका में संक्षेपित करें।



### काली लिनक्स के अंतर्गत बुनियादी कार्य



| **Catégorie**              | **Tâche de base**                      | **Description / Objectif**                                 | **Méthode principale**                                       |
| -------------------------- | -------------------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------ |
| **Navigation système**     | Ouvrir le terminal                     | Accéder à la ligne de commande principale de Kali          | Cliquez sur l’icône du terminal ou utilisez `Ctrl + Alt + T` |
|                            | Parcourir les dossiers                 | Se déplacer dans l’arborescence du système                 | `cd /chemin/du/dossier`, `ls` pour lister les fichiers       |
|                            | Créer / supprimer un dossier           | Organiser les fichiers                                     | `mkdir nom_dossier`, `rm -r nom_dossier`                     |
| **Gestion des fichiers**   | Copier / déplacer un fichier           | Manipuler des fichiers dans le terminal                    | `cp fichier destination`, `mv fichier destination`           |
|                            | Supprimer un fichier                   | Libérer de l’espace disque                                 | `rm nom_du_fichier`                                          |
|                            | Afficher le contenu d’un fichier texte | Lire rapidement un fichier                                 | `cat fichier.txt`, `less fichier.txt`                        |
| **Gestion du système**     | Mettre à jour Kali Linux               | Installer les dernières versions et correctifs de sécurité | `sudo apt update && sudo apt full-upgrade -y`                |
|                            | Installer un logiciel                  | Ajouter un nouvel outil ou utilitaire                      | `sudo apt install nom_du_paquet`                             |
|                            | Supprimer un logiciel                  | Nettoyer le système                                        | `sudo apt remove nom_du_paquet`                              |
|                            | Nettoyer les dépendances inutiles      | Gagner de l’espace disque                                  | `sudo apt autoremove`                                        |
| **Réseau et Internet**     | Vérifier la connexion réseau           | Tester l’accès à Internet                                  | `ping google.com`                                            |
|                            | Identifier l’adresse IP                | Connaître sa configuration réseau                          | `ip a` ou `ifconfig`                                         |
|                            | Changer de réseau Wi-Fi                | Se connecter à un autre point d’accès                      | Icône réseau → Sélectionner le Wi-Fi voulu                   |
| **Comptes et permissions** | Exécuter une commande administrateur   | Obtenir les droits root temporairement                     | `sudo commande`                                              |
|                            | Créer un nouvel utilisateur            | Ajouter un compte local                                    | `sudo adduser nom_utilisateur`                               |
|                            | Modifier un mot de passe               | Sécuriser un compte                                        | `passwd`                                                     |
| **Apparence et confort**   | Changer le fond d’écran                | Personnaliser le bureau                                    | Clic droit sur le bureau → **Paramètres du bureau**          |
|                            | Modifier le thème / icônes             | Améliorer la lisibilité et l’esthétique                    | Paramètres → Apparence / Thèmes                              |
| **Outils Kali**            | Ouvrir le menu des outils              | Explorer les outils de test et de sécurité                 | Menu **Applications → Kali Linux**                           |
|                            | Lancer un outil (ex : nmap, wireshark) | Découverte pratique des utilitaires de sécurité            | `sudo nmap`, `wireshark`, etc.                               |
| **Aide et documentation**  | Obtenir de l’aide sur une commande     | Comprendre une commande avant de l’utiliser                | `man commande` ou `commande --help`                          |

## निष्कर्ष



साइबर सुरक्षा के लिए समर्पित इस शक्तिशाली वातावरण की खोज में Kali Linux को इंस्टॉल करना बस पहला कदम है। बुनियादी कार्यों और सिस्टम प्रबंधन में महारत हासिल करके, कोई भी अंतर्निहित टूल्स का अन्वेषण करना शुरू कर सकता है और Linux सिस्टम की आंतरिक कार्यप्रणाली को समझ सकता है। Kali तकनीकी कौशल को मज़बूत करने और IT सुरक्षा की एक सच्ची संस्कृति विकसित करने के लिए एक उत्कृष्ट शिक्षण मंच प्रदान करता है।