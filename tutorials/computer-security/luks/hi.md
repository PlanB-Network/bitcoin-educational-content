---
name: LUKS
description: LUKS और क्रिप्टसेटअप के साथ USB फ्लैश ड्राइव को एन्क्रिप्ट करना
---
![cover](assets/cover.webp)



___



*यह ट्यूटोरियल [IT-Connect](https://www.it-connect.fr/) पर प्रकाशित मिकेल डोरिग्नी की मूल सामग्री पर आधारित है। लाइसेंस [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)। मूल पाठ में बदलाव किए गए हो सकते हैं।*



___



## I. प्रस्तुति



USB स्टिक को एन्क्रिप्ट करना आपके संवेदनशील डेटा की सुरक्षा का एक अच्छा तरीका है। **इस ट्यूटोरियल में, हम देखेंगे कि Linux सिस्टम पर USB स्टिक को एन्क्रिप्ट करने के लिए cryptsetup के साथ LUKS (*Linux Unified Key Setup*) का उपयोग कैसे करें।** यह विधि आपको अपने डेटा को सुरक्षित रखने में सक्षम बनाएगी, विशेष रूप से आपकी USB स्टिक के खो जाने या चोरी हो जाने की स्थिति में।



[**LUKS**](https://fr.wikipedia.org/wiki/LUKS) (*Linux Unified Key Setup*) एक डिस्क एन्क्रिप्शन मानक है जिसका उपयोग मुख्यतः Linux सिस्टम पर किया जाता है। यह मज़बूत एल्गोरिदम के साथ डिस्क विभाजनों को एन्क्रिप्ट करके डेटा को सुरक्षित करता है। Linux सिस्टम पर इसका समर्थन एन्क्रिप्शन कुंजियों और पासवर्ड के प्रबंधन को आसान बनाता है, मानकीकृत Interface और विभिन्न प्रबंधन उपकरणों के साथ संगतता प्रदान करता है।



इस ट्यूटोरियल का अनुसरण करने के लिए आपको आवश्यकता होगी:





- यूएसबी की;
- एक लिनक्स सिस्टम जिसमें "**cryptsetup**" इंस्टॉल हो (अक्सर यह डिफ़ॉल्ट रूप से उपलब्ध होता है, अन्यथा हम देखेंगे कि इसे कैसे प्राप्त किया जाए)।



## II. क्रिप्टसेटअप स्थापित करना



सबसे पहले, हमें यह सुनिश्चित करना होगा कि हमारे सिस्टम पर "**cryptsetup**" कमांड मौजूद है:



```
# Vérifier la présence de la commande cryptsetup
which cryptsetup
```



यदि आपको इस आदेश पर कोई प्रतिक्रिया नहीं मिलती है, तो आपको "**cryptsetup**" स्थापित करना होगा:



```
# Installer cryptsetup
# Sous Debian et dérivés
apt-get install cryptsetup

# Sous Redhat et dérivés
sudo yum install cryptsetup
# ou
sudo dnf install cryptsetup
```



अब हमारे पास LUKS के माध्यम से एन्क्रिप्टेड USB कुंजी बनाने के लिए आवश्यक सभी चीजें मौजूद हैं।



वास्तव में, यह "dm-crypt" उपयोगिता है जो एन्क्रिप्शन का कार्य करेगी। "cryptsetup" एक कमांड-लाइन Interface है जो dm-crypt की विशेषताओं और क्रियाओं का प्रबंधन करता है।



## III. LUKS विभाजन और फ़ाइल सिस्टम बनाना



### A. USB कुंजी की पहचान करें



अब हम अपनी USB स्टिक पर एक एन्क्रिप्टेड LUKS पार्टीशन बनाने जा रहे हैं। अगर आपने इसे अभी तक अपने सिस्टम से कनेक्ट नहीं किया है, तो अब ऐसा करने का समय आ गया है।



इस ट्यूटोरियल के लिए, मैं अपनी पूरी USB स्टिक को एन्क्रिप्ट कर रहा हूँ, सिर्फ़ एक पार्टिशन को नहीं। यह जानना भी ज़रूरी है कि इस प्रक्रिया के दौरान, **कुंजी से सारा मौजूदा डेटा मिटा दिया जाएगा**।



पहला कदम "**/dev/**" निर्देशिका में अपनी USB स्टिक से संबंधित डिवाइस फ़ाइल ढूँढना है। अपनी USB स्टिक डालें और उसका डिवाइस नाम पहचानें। स्टोरेज डिवाइस की सूची बनाने के लिए आप निम्न कमांड का उपयोग कर सकते हैं:



```
$ lsblk
```



अपनी USB कुंजी ढूँढ़ें, उदाहरण के लिए "**/dev/sdb**"। आप USB कुंजी मॉडल का नाम प्रदर्शित करने के लिए "**fdisk -l**" कमांड का भी उपयोग कर सकते हैं (गलती न करना ही बेहतर है), और डिवाइस के स्टोरेज साइज़ को संकेतक के रूप में उपयोग करें:



![Image](assets/fr/019.webp)



"**lsblk**" और "**fdisk**" के साथ एन्क्रिप्ट की जाने वाली USB कुंजी की पहचान करें।



मेरे उदाहरण में, मेरी USB कुंजी "**/dev/sdb**" में स्थित है। अगर आपको "**/dev/sdb1**", "**/dev/sdb2**", आदि दिखाई देते हैं, तो ये आपके ड्राइव पर मौजूद पार्टिशन हैं। ये आपकी कुंजी पर मौजूद पार्टिशन हैं। इन्हें हमारे द्वारा किए गए हेरफेर से हटा दिया जाएगा।



### B. मौजूदा डेटा हटाएं



अब हम अपनी USB स्टिक का सारा डेटा डिलीट करने जा रहे हैं। इस प्रक्रिया में हमारी USB स्टिक के डिस्क स्पेस को 0 से भरना शामिल है।



**सुनिश्चित करें कि आप सही डिवाइस फ़ाइल को लक्षित कर रहे हैं!**



```
# Remplir la clé USB de 0
$ sudo dd if=/dev/zero of=/dev/sdb bs=1M

7911+0 records in
7910+0 records out
8294236160 bytes (8.3 GB, 7.7 GiB) copied, 1556.22 s, 5.3 MB/s
```



इससे यह सुनिश्चित होता है कि हमारी कुंजी पर कोई स्थायी सादा पाठ डेटा नहीं होगा।



### C. USB कुंजी को LUKS के साथ एन्क्रिप्ट करें



अब हम अपनी USB कुंजी पर LUKS पार्टीशन को इनिशियलाइज़ करेंगे। इसमें LUKS पार्टीशन बनाना शामिल है:



```
# Formattage d'une partition LUKS sur la clé USB
$ sudo cryptsetup luksFormat /dev/sdb

WARNING!
========
This will overwrite data on /dev/sdb irrevocably.

Are you sure? (Type 'yes' in capital letters): YES
Enter passphrase for /dev/sdb:
Verify passphrase:
```



यहाँ, "`luksFormat`" उपकमांड डिवाइस को LUKS एन्क्रिप्शन का उपयोग करने के लिए आरंभीकृत और स्वरूपित करता है। आपको बड़े अक्षरों में `YES` लिखकर इस ऑपरेशन की पुष्टि करने के लिए कहा जाएगा, फिर एक *passphrase* परिभाषित करें। **एक मज़बूत** *passphrase* **चुनें ताकि यह सुनिश्चित हो सके कि नुकसान की स्थिति में, हमलावर उसे क्रूत-बल हमलों के ज़रिए न खोज सके।**



इसके बाद, "**/dev/sdb**" डिस्क LUKS के साथ फॉर्मेट हो जाएगी और एन्क्रिप्टेड वॉल्यूम के रूप में उपयोग के लिए तैयार हो जाएगी।



### D. एन्क्रिप्टेड वॉल्यूम को फ़ॉर्मेट करें



हम लगभग वहाँ पहुँच गए हैं, और अब हमें अपने LUKS पार्टीशन में एक वैध पार्टीशन बनाना होगा। इस तरह, अनलॉक होने के बाद, हम इसे किसी भी अन्य फ़ाइल सिस्टम की तरह इस्तेमाल कर सकते हैं। ऐसा करने के लिए, हमें एन्क्रिप्टेड पार्टीशन को खोलना होगा:



```
# Ouverture de la partition LUKS sur la clé USB
$ sudo cryptsetup luksOpen /dev/sdb usbkey1
Enter passphrase for /dev/sdb:

# Lister les disques
$ sudo fdisk -l
[...]

Disk /dev/sdb: 7.72 GiB, 8294236160 bytes, 16199680 sectors
Disk model: Flash Disk
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes


Disk /dev/mapper/usbkey1: 7.71 GiB, 8277458944 bytes, 16166912 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
```



यहाँ, "**usbkey1**" वह नाम है जो मैं अपने संदर्भ में विभाजन माउंट को देता हूँ। आप अपनी पसंद का कोई भी नाम चुन सकते हैं। फिर हमें LUKS विभाजन में शामिल इस विभाजन को, उदाहरण के लिए, यहाँ **ext4** के रूप में फ़ॉर्मेट करना होगा:



```
# Formattage de la partition en ext4
$ sudo mkfs.ext4 /dev/mapper/usbkey1

mke2fs 1.47.0 (5-Feb-2023)
Creating filesystem with 2020864 4k blocks and 505920 inodes
Filesystem UUID: cfa607d3-c31f-475d-bcfe-fa951b60a591
Superblock backups stored on blocks:
32768, 98304, 163840, 229376, 294912, 819200, 884736, 1605632

Allocating group tables: done
Writing inode tables: done
Creating journal (16384 blocks):
done
Writing superblocks and filesystem accounting information:
done
```



**यहाँ, लक्ष्य स्थान** को "**/dev/mapper/usbkey1**" के रूप में निर्दिष्ट किया गया है, क्यों?



"**/dev/mapper/usbkey1**" वह "शॉर्टकट" है जो हमने अपनी USB कुंजी को दिया है ("**/dev/mapper**" मैपिंग के लिए Linux में सामान्य है)। इसलिए यह हमारे डिक्रिप्टेड पार्टीशन तक पहुँच प्रदान करता है। अब आपको यह देखना चाहिए:



```
# Liste des périphériques et leurs partition
$ lsblk
NAME      MAJ:MIN RM  SIZE RO TYPE  MOUNTPOINTS
sda         8:0    0  200G  0 disk
├─sda1      8:1    0  199G  0 part  /
├─sda2      8:2    0    1K  0 part
└─sda5      8:5    0  975M  0 part  [SWAP]
sdb         8:16   1  7.7G  0 disk
└─usbkey1 254:0    0  7.7G  0 crypt
sr0        11:0    1 1024M  0 rom
```



## IV. एन्क्रिप्टेड USB कुंजी का उपयोग करना



### A. LUKS वॉल्यूम खोलें और संपादित करें



**Interface ग्राफ़िक के माध्यम से** **:**



डेबियन में, "**dm-crypt**" डिफ़ॉल्ट रूप से मौजूद होता है। इसलिए, ज़्यादातर मामलों में, इंस्टॉलेशन सीधे USB कुंजी प्लग इन करने पर ही होता है। फिर आपको एक पॉप-अप विंडो में अपना passphrase दर्ज करने के लिए कहा जाएगा, जैसे कि यह:



![Image](assets/fr/018.webp)



LUKS विभाजन के लिए डिक्रिप्शन passphrase दर्ज करने का अनुरोध।



एक बार passphrase दर्ज हो जाने पर, आपका सिस्टम कुंजी पर फ़ाइल सिस्टम को पढ़ने में सक्षम हो जाएगा और फिर इस फ़ाइल सिस्टम को माउंट कर देगा, जो हमारे माउंटेड विभाजन को दिखाएगा:



```
$ lsblk
NAME                                        MAJ:MIN RM  SIZE RO TYPE  MOUNTPOINTS
sda                                           8:0    0  200G  0 disk
├─sda1                                        8:1    0  199G  0 part  /
├─sda2                                        8:2    0    1K  0 part
└─sda5                                        8:5    0  975M  0 part  [SWAP]
sdb                                           8:16   1  7.7G  0 disk
└─luks-425f7800-e461-47e9-b8cc-f76d0cefb853 254:0    0  7.7G  0 crypt /media/mickael/cfa607d3-c31f-475d-bcfe-fa95
sr0                                          11:0    1 1024M  0 rom
```



**कमांड लाइन पर:**



हालाँकि, यह जानना ज़रूरी है कि कमांड लाइन पर ऑपरेशन कैसे किया जाता है। आइए "**crypsetup**" और "**luksOpen**" सब-कमांड का उपयोग करके एन्क्रिप्टेड पार्टीशन को डिक्रिप्ट करके शुरू करें:



```
# Ouverture de la partition LUKS sur la clé USB
$ sudo cryptsetup luksOpen /dev/sdb usbkey1
Enter passphrase for /dev/sdb:

# Liste des périphériques et leurs partition
$ lsblk
NAME      MAJ:MIN RM  SIZE RO TYPE  MOUNTPOINTS
[...]
sdb         8:16   1  7.7G  0 disk
└─usbkey1 254:0    0  7.7G  0 crypt
sr0        11:0    1 1024M  0 rom
```



अब, हमारे USB फ्लैश ड्राइव का डिक्रिप्टेड वॉल्यूम एक वॉल्यूम प्रस्तुत करता है जिसे हमारा फ़ाइल सिस्टम और OS उपयोग कर सकता है, इसलिए हम इसकी सामग्री को किसी भी फ़ोल्डर में माउंट करेंगे, उदाहरण के लिए मेरे मामले में "**/home/mickael/mnt**":



```
# Monter le volume déchiffré sur notre système de fichier
$ mkdir /home/mickael/mnt
$ sudo mount /dev/mapper/usbkey1 /home/mickael/mnt

$ ls /home/mickael/mnt -al
total 24
drwxr-xr-x  3 root    root     4096 Jun 11 14:38 .
drwx------ 31 mickael mickael  4096 Jun 11 21:44 ..
drwx------  2 root    root    16384 Jun 11 14:38 lost+found

```



इसका मतलब यह है कि हम अपने यूएसबी स्टिक पर डेटा को स्वतंत्र और पारदर्शी तरीके से एक्सेस कर सकते हैं।



### B. LUKS वॉल्यूम बंद करें और निकालें



एक बार हमारा ऑपरेशन पूरा हो जाने के बाद, यह सुनिश्चित करने के लिए कि हमारा वॉल्यूम दूषित न हो, सब कुछ ठीक से बंद करना न भूलें। पहला चरण है:



```
# Démontage du volume contenu dans la partition chiffrée
sudo umount /home/mickael/mnt
```



फिर एन्क्रिप्टेड पार्टीशन को बंद करें:



```
# Fermeture de la partition chiffrée
sudo cryptsetup luksClose usbkey1
```



अब, हमारी यूएसबी कुंजी का उपयोग करने वाले किसी भी व्यक्ति को एन्क्रिप्टेड डेटा के अलावा इसकी सामग्री में कुछ भी दिखाई नहीं देगा।



## V. निष्कर्ष



ग्राफ़िकल यूज़र इंटरफ़ेस इस प्रक्रिया को पारदर्शी बनाते हैं, लेकिन कमांड लाइन से एन्क्रिप्टेड LUKS पार्टीशन को फ़ॉर्मेट करना, बनाना, खोलना और बंद करना जानना अभी भी उपयोगी है। फ़ॉर्मेट हो जाने के बाद, LUKS पार्टीशन को खोलने और बंद करने के लिए ज़रूरी बदलाव सुरक्षा लाभों की तुलना में न्यूनतम होते हैं।