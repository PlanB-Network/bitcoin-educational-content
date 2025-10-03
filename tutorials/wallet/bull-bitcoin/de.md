---
name: Bull Bitcoin Wallet
description: Finden Sie heraus, wie Sie den Wallet Bull Bitcoin verwenden
---

![cover](assets/cover.webp)



Dieser Leitfaden führt Sie durch die Installation, Konfiguration und Verwendung des Bull Bitcoin Mobile. Sie erfahren, wie Sie Geld in den drei Netzwerken Onchain, Liquid und Lightning empfangen und senden können und wie Sie Ihr Bitcoin von einem Netzwerk in ein anderes übertragen können. In den Anhängen finden Sie Ressourcen und Kontakte, Hintergrundinformationen und kurze Erklärungen zu technischen Konzepten.



## Einführung



**Bull Bitcoin Mobile**, entwickelt von **[Bull Bitcoin](https://www.bullbitcoin.com/)** ([Konto erstellen](https://app.bullbitcoin.com/registration/orangepeel)), ist ein **selbstverwaltetes** Bitcoin Wallet, was bedeutet, dass Sie die volle Kontrolle über Ihre privaten Schlüssel und somit über Ihr Geld haben, ohne von einer dritten Partei abhängig zu sein. Open-Source und verwurzelt in einer Cypherpunk-Philosophie, kombiniert dieser Wallet Einfachheit, Vertraulichkeit und fortgeschrittene Funktionen wie netzwerkübergreifende Swaps und PayJoin-Unterstützung. Es ermöglicht Ihnen die Verwaltung Ihrer Bitcoins in drei Netzwerken: **Bitcoin onchain**, **Liquid** und **Lightning**, die jeweils auf bestimmte Anwendungen zugeschnitten sind.



### Kontext der Entwicklung



Wallet ist eine Antwort auf eine große Herausforderung: Die Bitcoin-Netzgebühren sind für kleine Zahlungen oder für die Eröffnung kleiner, selbst gehosteter Lightning-Kanäle ungeeignet. Der Wallet Bull Bitcoin Mobile bietet eine selbstverwaltete Lösung und stützt sich dabei auf die 3 großen Bitcoin-Netze:





- **Bitcoin-Netzwerk (onchain)**: Ideal für die mittel- bis langfristige Speicherung von UTXOs und Transaktionen mit hohem Wert, bei denen die Gebühren verhältnismäßig vernachlässigbar sind.
- **Liquid Network**: Entwickelt für schnelle (~2 Minuten), vertraulichere (versteckte Beträge), kostengünstige Transaktionen, ideal für die Anhäufung kleiner Beträge oder zum Schutz Ihrer Privatsphäre.
- **Lightning-Netzwerk**: Optimiert für sofortige, kostengünstige Zahlungen, geeignet für tägliche Transaktionen mit kleinen bis mittleren Beträgen.



Mit Bull Bitcoin Mobile können Sie zum Beispiel kleine Beträge in den Portfolios **Liquid** oder **Lightning** ansammeln und dann, wenn Sie einen größeren Betrag erreicht haben, können Sie :





- Übertragung an das Onchain-Netzwerk zur sicheren mittel- oder langfristigen Speicherung, mit verbesserter Vertraulichkeit durch Liquid und/oder Lightning im Vorfeld und mit Onchain-Gebühren für eine einzelne Transaktion



### Kontinuierliche Entwicklung



Wallet wird ständig weiterentwickelt. Seien Sie also nicht überrascht, wenn Sie Diskrepanzen zwischen dieser Anleitung und Ihrer aktuellen Anwendung feststellen.




- Zum Beispiel sind ab dem 19.07.2025 die Schaltflächen **"Kaufen / Verkaufen / Bezahlen "** sichtbar, aber in der Anwendung ausgegraut, da diese Optionen, die auf Exchange [bullbitcoin.com] (https://app.bullbitcoin.com/registration/orangepeel) verfügbar sind, bald für ein einheitliches Erlebnis integriert werden. Ihre Verwendung bleibt völlig optional. Viele andere Entwicklungen sind im Gange oder geplant: Multi-Wallet-Management, passphrase, Kompatibilität mit Hardware-Wallets...
- Auf dem [BullBitcoin GitHub](https://github.com/orgs/SatoshiPortal/projects/49) können Sie sich über aktuelle Themen und bevorstehende Entwicklungen informieren. Da das Projekt zu 100 % quelloffen und "öffentlich gebaut" ist, können Sie uns auch Ihre Vorschläge und alle Fehler, auf die Sie stoßen, schicken.




## 1. Voraussetzungen



Bevor Sie **Bull Bitcoin Mobile** in Betrieb nehmen, vergewissern Sie sich, dass Sie die folgenden Gegenstände besitzen:





- **Kompatibles Smartphone**: Ein **iOS** (iPhone oder iPad) oder **Android** Gerät
- Internetverbindung
- **Sichere Sicherungsmedien**: Schreiben Sie Ihre **Wiederherstellungsphrase** (12 Wörter) auf Papier oder Metall und bewahren Sie sie an einem sicheren Ort auf.
- **Grundkenntnisse**: Ein Mindestmaß an Verständnis der Bitcoin-Konzepte (Adressen, Transaktionen, Gebühren) ist nützlich, auch wenn dieses Tutorial jeden Schritt für Anfänger erklärt.



## 2. Einrichtung





- **Laden Sie die Bewerbung herunter**:
- [Google Play Store](https://play.google.com/store/apps/details?id=com.bullbitcoin.mobile&pcampaignid=web_share) **Herunterladen aus dem Application Store für Android-Geräte**
- [GitHub](https://github.com/SatoshiPortal/bullbitcoin-mobile/releases) **Laden Sie die APK für Android-Geräte direkt herunter**
- [iOS](https://testflight.apple.com/join/FJbE4JPN) **Download über TestFlight für Apple-Geräte**
 - Überprüfen Sie den Namen des Entwicklers (Bull Bitcoin), um betrügerische Anträge zu vermeiden.
 - Stellen Sie sicher, dass die heruntergeladene Version der neuesten stabilen Version entspricht, die auf GitHub angegeben ist.
 - Bull Bitcoin Mobile ist **Open-Source**. Um den Code einzusehen: [BullBitcoin GitHub](https://github.com/orgs/SatoshiPortal/projects/49)





- Installieren Sie die Anwendung




## 3. Erstmalige Konfiguration



### 3.1 Starten Sie die Anwendung:



Die Anwendung verwendet für beide Portfolios eine einzigartige 12-Wörter-Wiederherstellungsphrase:




- **sichere Bitcoin Wallet**: Für Transaktionen im Bitcoin-Netz (onchain)
- **Instant Payments' Wallet**: Für sofortige Transaktionen über Liquid und Lightning-Netzwerke



Beim Öffnen werden Sie aufgefordert, eine vorhandene Wiederherstellungsphrase zu importieren oder eine neue Wallet zu erstellen:



![image](assets/fr/02.webp)



### 3.2 Satz zur Wiederherstellung :



Wenn Sie einen vorhandenen Wallet wiederverwenden möchten, klicken Sie auf "**Wallet wiederherstellen**" und geben Sie die 12 Wörter Ihres Wiederherstellungssatzes ein.



Andernfalls klicken Sie auf "**Neue Wallet erstellen**":




- Schreiben Sie Ihren Wiederherstellungssatz mit äußerster Sorgfalt auf. Schreiben Sie ihn auf Papier oder Metall und bewahren Sie ihn an einem sicheren Ort auf (Bankschließfach, Offline-Ort). Diese Phrase ist Ihr einziges Mittel, um im Falle des Verlusts Ihres Geräts oder der Löschung der Anwendung auf Ihre Bitcoins zuzugreifen.
- Es ist auch wichtig zu wissen, dass jeder, der diesen Satz kennt, alle Ihre Bitcoins stehlen kann. Bewahren Sie sie niemals digital auf:
 - Kein Bildschirmfoto
 - Keine Cloud-, E-Mail- oder Messaging-Backups
 - Kein Kopieren/Einfügen (Gefahr des Speicherns in der Zwischenablage)



**! Dieser Punkt ist entscheidend**. Für weitere Hilfe:



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

### 3.3 Sicherung des Zugangs :





- Gehen Sie zu Einstellungen und klicken Sie auf **PIN-Code**.
- Richten Sie einen zuverlässigen **PIN-Code** ein, um den Zugang zur Anwendung zu schützen.
- Dieser Schritt ist optional, wird aber dringend empfohlen, um zu verhindern, dass jemand, der Zugang zu Ihrem Telefon hat, Zugriff auf Ihr Wallet erhält.



![image](assets/fr/03.webp)



### 3.4 Anschluss an einen persönlichen Knoten (optional):



Der Wallet BullBitcoin verbindet sich standardmäßig mit Electrum-Servern: dem ersten, der von Bull Bitcoin verwaltet wird, und einem sekundären Server von Blockstream, von denen man annimmt, dass sie keine Protokolle aufbewahren, was das Risiko des Trackings verringert.



Für eine größere Vertraulichkeit können Sie die Anwendung über einen Electrum-Server mit Ihrem eigenen Bitcoin-Knoten verbinden (Anweisungen sind auf [BullBitcoins GitHub](https://github.com/orgs/SatoshiPortal/projects/49) verfügbar).




## 4. Empfang von Geldern



Der Empfang von Geldern mit **Bull Bitcoin Mobile** ist einfach und auf Ihre Bedürfnisse zugeschnitten, egal ob Sie :




  - das Netz **Bitcoin (onchain)** zur langfristigen Erhaltung,
  - das **Liquid**-Netz für schnelle, mehr Confidential Transactions,
  - das **Lightning**-Netzwerk für sofortige Zahlungen mit geringem Wert.



Die Anwendung generiert automatisch Lightning-Empfangs- oder Invoice-Adressen, je nach ausgewähltem Netz. Im Folgenden erfahren Sie, wie Sie für jedes Netz vorgehen.



### 4.1. onchain (Bitcoin-Netzwerk)



Auf dem Startbildschirm können Sie :




- oder wählen Sie das **Secure Bitcoin Wallet** und klicken Sie auf "**Empfangen "**:



![image](assets/fr/04.webp)





- oder klicken Sie auf "**Empfangen "**, und wählen Sie dann das Netz **Bitcoin**:



![image](assets/fr/05.webp)



#### 4.1.1. Option "Nur Address kopieren oder scannen" deaktiviert (Standard)



![image](assets/fr/06.webp)





- Dies ermöglicht den Zugriff auf optionale erweiterte Parameter. Sie können angeben:
 - Ein **Betrag** in BTC, Sats oder Fiat.
 - Eine **persönliche Notiz**, die in die Kopie des URI / QR-Codes aufgenommen wird.
 - Aktivierung von **PayJoin** (Einzelheiten siehe Anhang 3), das die Vertraulichkeit durch Kombination von Absender- und Empfängereinträgen verbessert.





- Beispiel für einen automatisch generierten **URI**:



```
bitcoin:bc1qyv76arrcu7bullbitcoin9mgugjvcgelcjfcycjq?amount=2.1e-7&message=Exemple+de+note&pj=HTTPS%3A%2F%2FPAYJO.IN%2FUJA9LJ6L4CMHY%23RK1QT3YSGFC6PMKRUXND2DSGQMLESTUNH29AY0305XAQ678742CVT5ES+OH1QYP87E2AVMDKXDTU6R25WCPQ5ZUF02XHNPA65JMD8ZA2W4YRQN6UUWG+EX1RRH8C6Q
```





- **Verwendung**: Kopieren Sie die URI, um sie an den Absender weiterzugeben, oder lassen Sie ihn den QR-Code scannen.



#### 4.1.2. Option "Nur Address kopieren oder scannen" aktiviert



![image](assets/fr/07.webp)





- Wenn die Option **"Nur Address kopieren oder scannen "** aktiviert ist, erzeugt die Anwendung einen einfachen Bitcoin Address im SegWit (bech32)-Format.





- Beispiel:



```
bc1qyv76arrcu7bullbitcoin9mgugjvcgelcjfcycjq
```



Auch wenn Sie einen Betrag oder eine Notiz eingeben, werden diese nicht im QR-Code oder in der Kopie des Address enthalten sein





- **Verwendung**: Kopieren Sie den Address, um ihn mit dem Absender zu teilen, oder lassen Sie ihn den QR-Code scannen.



#### 4.1.3. Erzeugen eines neuen Address





- Warum sollten Sie für jede Transaktion ein neues Address verwenden? Dies **schützt Ihre Privatsphäre**, indem verhindert wird, dass mehrere Zahlungen mit demselben Address verknüpft werden, und schränkt die Möglichkeiten der Rückverfolgung auf dem Blockchain ein.
- Standardmäßig erzeugt Bull Bitcoin automatisch einen unbenutzten **Address**.
 - Sie können die Erstellung eines neuen Address erzwingen, indem Sie auf **"Neues Address"** am unteren Rand des Bildschirms klicken.
 - Alle Ihre Adressen sind mit Ihrem seed-Satz verknüpft: Unabhängig davon, wie viele Adressen Sie verwenden, zeigt Ihr Portfolio einen einzigen Saldo an und kann die Mittel automatisch konsolidieren, wenn eine Lieferung erfolgt.





- Tipp: Verwenden Sie immer den neuen **Address**, der von Bull Bitcoin bereitgestellt wird, es sei denn, Sie haben einen besonderen Bedarf (z. B. einen öffentlichen Address, um Spenden zu erhalten).



### 4.2. Liquid



Auf dem Startbildschirm können Sie :




- oder wählen Sie die **Sofortzahlungen Wallet** und klicken Sie auf **"Empfangen "** und dann **"Liquid"**:



![image](assets/fr/08.webp)





- oder klicken Sie auf "**Empfangen "**, und wählen Sie dann das Netz **Liquid**:



![image](assets/fr/09.webp)



Sobald Sie auf dem Bildschirm **"Empfangen "** sind, kopieren Sie einen Liquid Address:





- Kein Betrag oder Vermerk. Beispiel:



```
lq1qq05k3vmnvbullbitcoinjujn6h04z9jtw53xuyktqf9mam2zpfz05j2fe2x8xhejgkga3nvmp4yyp35qynkcw2xqmy7x53ahpz
```





- Oder indem Sie einen **Betrag** (in BTC, Sats oder Fiat) und/oder eine **persönliche Notiz** angeben, die in die Kopie des URI / QR-Codes aufgenommen werden soll. Beispiel:



```
liquidnetwork:lq1qq05k3vmnvbullbitcoinjujn6h04z9jtw53xuyktqf9mam2zpfz05j2fe2x8xhejgkga3nvmp4yyp35qynkcw2xqmy7x53ahpz?amount=2.1e-7&message=Test+de+note+Liquid&assetid=6f0279e9ed041c3d710a9f57d0c02928416460c4b722ae3457a11eec381c526d
```



**Verwendung**: Kopieren Sie den Address/URI, um ihn an den Absender weiterzugeben, oder lassen Sie ihn den QR-Code scannen.



### 4.3. Blitzschlag



Auf dem Startbildschirm können Sie :




- oder wählen Sie die **Sofortzahlungen Wallet** und klicken Sie dann auf "**Empfangen "**:



![image](assets/fr/10.webp)





- oder klicken Sie auf "**Empfangen "**, und wählen Sie dann das Netz **Blitz**:



![image](assets/fr/11.webp)



#### 4.3.1. Funktionsweise, Grenzen und Vorteile





- **Mechanismus**: Bull Bitcoin Wallet ist ein Wallet, mit dem Zahlungen über Lightning getätigt und empfangen werden können. Über Lightning empfangene Gelder werden dank eines automatischen Swaps über **Boltz** im **Liquid**-Netzwerk (im Wallet Instant Payments) gespeichert. Dies gibt Ihnen die Möglichkeit, mit Lightning zu interagieren, ohne dass Sie Liquiditätskanäle verwalten müssen, während Sie selbst in der Verwahrung bleiben.





- **Grenzwerte:**
- Ein **Mindestbetrag** von 100 Satoshis (ab 19.07.2025), wenn Sie generate den Invoice.
- Sie zahlen die Kosten, die vom Absender vom gesendeten Betrag abgezogen werden, im Gegensatz zum Empfang mit Wallet Lightning native, wo nur der Absender die Überweisungskosten zusätzlich zum gesendeten Betrag zahlt. Mit Stand vom 19/07/2025 werden 47 Sats von dem gesendeten Betrag abgezogen.





- **Vorteile**:
- **Selbstverwahrend**: Ihr Geld bleibt unter Ihrer Kontrolle und wird auf der Liquid Network gespeichert.
- **Keine hohen Onchain-Gebühren**: Die Speicherung auf Liquid vermeidet kostspielige Onchain-Einzahlungen, um Ihren Lightning-Kanal zu öffnen oder Liquidität hinzuzufügen. Diese Operationen können später durchgeführt werden, wenn der auf Liquid angesammelte Betrag die Gebühren rechtfertigt.





- **Tipp:** Wenn der Absender über Wallet Bull Bitcoin verfügt, verwenden Sie direkt den Liquid Network, um Tauschgebühren zu vermeiden



#### 4.3.2. generate Invoice





- Geben Sie einen **Betrag** ein (in BTC, Sats oder Fiat)





- Fügen Sie eine **persönliche Notiz** hinzu, die in den Invoice integriert wird. Wenn der Absender den Invoice bezahlt, wird dies auch in Ihrem Wallet in den Transaktionsdetails aufgeführt.





- **Invoice Gültigkeit:** Der Lightning Invoice ist für **12 Stunden** gültig. Nach Ablauf dieser Zeit verfällt sie und kann nicht mehr bezahlt werden. Es muss eine neue Invoice erstellt werden.





- **Verwendung**: Kopieren Sie den Invoice, um ihn mit dem Absender zu teilen, oder lassen Sie ihn den QR-Code scannen.




## 5. Übermittlung von Geldern



### 5.1. Grundprinzip



Entweder über die Homepage oder über die Brieftaschen:



![image](assets/fr/12.webp)



um den Sendebildschirm aufzurufen:



![image](assets/fr/13.webp)



**Bull Bitcoin Mobile** macht das Senden von Geld einfach, indem es automatisch das Netzwerk (Bitcoin, Liquid oder Lightning) anhand des eingegebenen Address oder Invoice (kopiert oder per QR-Code gescannt) erkennt.



### 5.2. On-Chain-Übertragung (Bitcoin-Netz)



#### 5.2.1. Bildschirm senden



**Aktion**: Eingabe oder Scannen eines Bitcoin in der Kette Address





- Wenn der Betrag nicht definiert wurde, zum Beispiel :



```
bc1qyv76arrcu7bullbitcoin9mgugjvcgelcjfcycjq
```





- Dann können Sie auf dem Sendebildschirm wählen:
 - Betrag in BTC, sat oder fiat. Mindestbetrag: 546 Satoshis am 22/07/2025.
 - Eine optionale Notiz zur Identifizierung der Transaktion. Nur für Sie sichtbar, in den Transaktionsdetails.



![image](assets/fr/14.webp)





- Wenn der Betrag bereits festgelegt wurde, z. B. :



```
bitcoin:bc1qyv76arrcu7bullbitcoin9mgugjvcgelcjfcycjq?amount=0.000006&pj=HTTPS%3A%2F%2FPAYJO.IN%2F7GAEA52UMTYQ7%23RK1QVJZYR38X2MC585ZPZ60QY72DMXHWT67LERFWW6GQ4LDEA7MRP78X+OH1QYP87E2AVMDKXDTU6R25WCPQ5ZUF02XHNPA65JMD8ZA2W4YRQN6UUWG+EX1EJ78U6Q
```



Sie werden dann direkt zum unten stehenden Bestätigungsbildschirm weitergeleitet.



#### 5.2.2 Bestätigungsbildschirm



Nehmen Sie sich die Zeit, alle Parameter zu prüfen, insbesondere den Betrag, das Zielland Address und die Gebühren.


Dann können Sie die Parameter anpassen:



![image](assets/fr/15.webp)




- **Gebühren**: Sie können wählen:
- Entweder werden die **Ausführungsgeschwindigkeit** Ihrer Transaktion und die damit verbundenen Gebühren geschätzt
- Es werden entweder die **Gebühren** im Modus Absolute Gebühren (Gesamtgebühren in Satoshis) oder Relative Gebühren (Gebühren pro Byte) sowie die Geschwindigkeit Ihrer Transaktion geschätzt





- **Erweiterte Einstellungen**:





- **Replace-by-fee (RBF)**: Diese Funktion ist standardmäßig aktiviert und beschleunigt die Transaktion durch Zahlung einer höheren Gebühr (Einzelheiten siehe Anhang 4).





- Manuelle Auswahl von **UTXO**: Wenn Ihre Gelder an mehreren verschiedenen Wallet-Adressen gespeichert sind, können Sie die Adressen auswählen, von denen die Gelder gesendet werden sollen. Warum sollten Sie das tun? Mit der zunehmenden Verbreitung von Bitcoin steigen die Überweisungsgebühren. Das Senden von mehreren Adressen mit kleinen Beträgen ist teurer als das Senden von einem einzigen Address, aber wenn Sie es jetzt tun, vermeiden Sie es später, wenn die Gebühren noch höher sein werden. Dies wird als **Konsolidierung von UTXO** bezeichnet



![image](assets/fr/16.webp)





- **Versenden mit PayJoin**: Wenn die Funktion vom Empfänger, der den URI übermittelt hat, aktiviert wurde, z. B. :



```
bitcoin:bc1qyv76arrcu7bullbitcoin9mgugjvcgelcjfcycjq?amount=0.000006&pj=HTTPS%3A%2F%2FPAYJO.IN%2F7GAEA52UMTYQ7%23RK1QVJZYR38X2MC585ZPZ60QY72DMXHWT67LERFWW6GQ4LDEA7MRP78X+OH1QYP87E2AVMDKXDTU6R25WCPQ5ZUF02XHNPA65JMD8ZA2W4YRQN6UUWG+EX1EJ78U6Q
```



Das Bull Bitcoin Mobile konfiguriert dann den Sendevorgang, indem es Ihre UTXOs mit den UTXOs des Empfängers kombiniert, um die Vertraulichkeit zu verbessern (Einzelheiten siehe Anhang 3).



### 5.3. Senden an Liquid



#### 5.3.1 Bildschirm "Senden



Das **Liquid** Netzwerk ermöglicht schnelle Transaktionen (~2 Minuten dank einem Block pro Minute), vertraulicher (maskierte Beträge) als im Onchain-Netzwerk und mit sehr niedrigen Gebühren. Gelder werden von **Instant Payments Wallet** abgehoben.



**Aktion**: Eingabe oder Scannen eines Liquid Address





- Wenn der Betrag nicht definiert wurde, zum Beispiel :



```
lq1qq05k3vmnvbullbitcoinjujn6h04z9jtw53xuyktqf9mam2zpfz05j2fe2x8xhejgkga3nvmp4yyp35qynkcw2xqmy7x53ahpz
```



Dann können Sie auf dem Sendebildschirm wählen:




- Betrag in BTC, sat oder fiat. Kein Minimum, 1 Satoshi möglich;
- Eine optionale Notiz zur Identifizierung der Transaktion. Nur für Sie sichtbar, in den Transaktionsdetails.



![image](assets/fr/17.webp)





- Wenn der Betrag bereits festgelegt wurde, z. B. :



```
liquidnetwork:lq1qq05k3vmnvbullbitcoinjujn6h04z9jtw53xuyktqf9mam2zpfz05j2fe2x8xhejgkga3nvmp4yyp35qynkcw2xqmy7x53ahpz?amount=2.1e-7&message=Test+de+note+Liquid&assetid=6f0279e9ed041c3d710a9f57d0c02928416460c4b722ae3457a11eec381c526d
```



Sie werden dann direkt zum unten stehenden Bestätigungsbildschirm weitergeleitet.



#### 5.3.2 Bestätigungsbildschirm



Nehmen Sie sich die Zeit, alle Parameter zu überprüfen, insbesondere die Menge und den Bestimmungsort Address.



![image](assets/fr/18.webp)





- **Gebühren**: Proportional zur Komplexität der Transaktion, in der Regel auf einer 0,1 Sat/vB-Basis, d.h. 20-40 Satoshis für eine einfache Transaktion (33 Sats am 22.07.2025).



### 5.4. Senden an Lightning



#### 5.4.1 Bildschirm "Senden



Das **Lightning**-Netzwerk ermöglicht sofortige, kostengünstige Zahlungen für kleine Beträge, ideal für kleine tägliche Transaktionen.



**Aktion**: Eingabe oder Scannen eines Lightning Invoice





- Wenn Sie einen LN-URL Address scannen, mit dem Sie die Menge einstellen können


Beispiel: `orangepeel@walletofsatoshi.com`.


dann können Sie auf dem Sendebildschirm wählen:




 - Betrag in BTC, Sat oder Fiat. Mindestbetrag von 1000 Satoshis am 23/07/2025
 - Eine optionale Notiz zur Identifizierung der Transaktion. Sie wird an den Empfänger gesendet.



![image](assets/fr/19.webp)





- Wenn Sie einen Lightning Invoice scannen, der eine bestimmte Menge


Beispiel:



```
lnbc210n1p58hhk6bullbitcoint4a9jq34dmrmcrursjmw3wjf8elz0nxtdsw9pscqzyssp52jg9dm8vc3xy26er5rc965lxjllhd82je97au7ysvv6lpq7r7shs9q7sqqqqqqqqqqqqqqqqqqqsqqqqqysgqdqqmqz9gxqyjw5qrzjqwryaup9lh50kkranzgcdnn2fgvx390wgj5jd07rwr3vxeje0glclle6wrlm37k39uqqqqlgqqqqqeqqjqnf7w9f2evnzptm2vtdknk7483hsndkl98c4mv2kfe64v5pkq0j6x2dqt9y9wayszv3z33az7c8hkj3yqj9jd7ans7ugq8xv0xefp23gqltph72
```



Sie werden dann direkt zum unten stehenden Bestätigungsbildschirm weitergeleitet.



Anmerkung: Betrag muss größer sein als 21 Sats am 23.07.2025



#### 5.4.2 Betrieb, Grenzen und Nutzen





- **Mechanismus**: Die Mittel werden von **Instant Payments Wallet** (Liquid) abgezogen und über einen **Liquid → Lightning**-Swap mit **Boltz** umgewandelt.





- **Grenzwerte:**
- Ein **Mindestbetrag** höher als ein Wallet Lightning Native (siehe oben)
- **Kosten** plus Liquid → Blitztausch über Boltz





- **Vorteile**:
- **Selbstverwahrend**: Ihr Geld bleibt unter Ihrer Kontrolle, wird auf dem Liquid Network gespeichert und kann bei Bedarf per Lightning übertragen werden
- **Keine hohen Onchain-Gebühren**: Die Speicherung auf Liquid erspart Ihnen kostspielige Onchain-Einzahlungen, um Ihren Lightning-Kanal zu öffnen oder Liquidität hinzuzufügen. Diese Operationen können später durchgeführt werden, wenn der auf Liquid angesammelte Betrag die Gebühren rechtfertigt.





- **Tipp:** Wenn der Empfänger über Wallet Bull Bitcoin verfügt, verwenden Sie direkt den Liquid Network, um Tauschkosten zu vermeiden



#### 5.3.3 Bestätigungsbildschirm



Nehmen Sie sich die Zeit, alle Parameter zu überprüfen, insbesondere die Menge und den Bestimmungsort Address.



![image](assets/fr/20.webp)




## 6. Geschichte ansehen



Mit **Bull Bitcoin Mobile** können Sie Ihre Transaktionen in den Netzwerken **Bitcoin (onchain)**, **Liquid** und **Lightning** einfach verfolgen. Die Historie kann auf zwei Arten abgerufen werden und zeigt detaillierte Informationen für jede Art von Transaktion an. Sie können Ihre Transaktionen auch mit externen Block-Browsern überprüfen.



### 6.1. Zugang Geschichte





- **Über den Startbildschirm**:
 - Klicken Sie auf den **Secure Bitcoin Wallet**, um **onchain**-Transaktionen anzuzeigen, oder auf den **Instant Payments Wallet** für **Liquid**- und **Lightning**-Transaktionen.
 - Die Historie wird direkt unter dem Gesamtportfolio angezeigt, gefiltert nach der Art des ausgewählten Wallet.



![image](assets/fr/21.webp)





- Über die entsprechende **Seite**:
 - Klicken Sie auf der Startseite auf das **Historiensymbol** (Uhrensymbol o.ä.).
 - Rufen Sie eine Seite auf, die alle Transaktionen auflistet, mit Filtern nach Art der Aktion: **Senden**, **Empfangen**, **Tauschen**, **PayJoin**, **Verkaufen**, **Kaufen** (Hinweis: Verkaufen und Kaufen befinden sich in der Entwicklung und sind zum jetzigen Zeitpunkt, 20. Juli 2025, nicht verfügbar).



![image](assets/fr/22.webp)



### 6.2. Einzelheiten der Transaktion



Jede Transaktion zeigt je nach Netzwerk und Art der Aktion (Senden oder Empfangen) spezifische Informationen an. Hier sind die Details, die für eine **Transaktion onchain** verfügbar sind:



![image](assets/fr/23.webp)



### 6.3. Prüfen über Block explorer



Die Liste der Forscher für die Netze **Bitcoin onchain**, **Liquid** und **Lightning** befindet sich in Anhang 4.



Für **Lightning** sind die Transaktionen in öffentlichen Browsern nicht sichtbar. Überprüfen Sie die Details (einschließlich der Swap-ID für Boltz) in der Anwendung.




## 7. Einstellungen



Die Seite "Einstellungen" kann direkt von der Startseite der Bull Bitcoin-Anwendung aus aufgerufen werden und dient der Konfiguration und Verwaltung verschiedener Aspekte des Portfolios und der Benutzererfahrung.



![image](assets/fr/24.webp)





- **Wallet Sicherung**: Zeigt die Wiederherstellungsphrase des Portfolios für die sichere Sicherung an. Bewährte Verfahren für die Verwaltung und Speicherung der Wiederherstellungsphrase finden Sie in Abschnitt 3 über die Erstellung von Portfolios.





- **Wallet Details**:
- **Pubkey**: Öffentlicher Schlüssel, der mit dem Wallet verbunden ist und für generate Bitcoin-Empfangsadressen verwendet wird.
- **Ableitungspfad**: Ableitungspfad, der für generate Wallet-Adressen aus dem privaten Schlüssel verwendet wird.





- **Electrum-Server (Bitcoin-Knoten)**: Richten Sie eine Verbindung zu einem angepassten Bitcoin-Knoten für Onchain-Transaktionen ein.





- **PIN-Code**: Aktivieren und/oder ändern Sie den Sicherheitscode, um den Zugriff auf die Anwendung und die Wallet-Funktionen zu schützen.





- **Währung**: Wählen Sie, ob die Beträge in BTC oder Sats angezeigt werden sollen, sowie die Standardwährung (Dollar, Euro usw.).





- **Auto-Swap-Einstellungen**: Mit der Funktion _Auto Swap_ können Sie den Transfer Ihrer BTC vom **Instant Payments Wallet (Liquid)** zu Ihrem **Bitcoin On-Chain** Wallet automatisieren, sobald der Betrag einen Schwellenwert erreicht, den Sie für hoch genug halten, um die Transaktionsgebühr zu rechtfertigen.





- **Protokolle**: Einsehbare Aktivitätsprotokolle, die mit dem technischen Support geteilt werden können, um die Fehlersuche zu erleichtern.





- **Telegram-Zugang für Support**: Direkter Link zum offiziellen Telegram-Kanal für Benutzerunterstützung.





- **Github-Zugang**: Link zum [Bull Bitcoin Github-Repository](https://github.com/SatoshiPortal), um Open-Source-Code einzusehen oder Probleme zu melden.




## ANHÄNGE



### A1. Erläuterung zu PayJoin (P2EP)



![image](assets/fr/25.webp)



**Definition** :




- PayJoin, oder **Pay-to-EndPoint (P2EP)**, ist eine Bitcoin-Transaktionstechnik, die die Vertraulichkeit im **onchain**-Netzwerk erhöht. Es kombiniert Sender- und Empfängereinträge in einer einzigen Transaktion, wodurch Beträge und Adressen schwieriger zu verfolgen sind.



**Operation:**




- Bei einer PayJoin-Transaktion arbeiten der Sender und der Empfänger über einen kompatiblen PayJoin-Server zusammen, um eine gemeinsame Transaktion durchzuführen.
- Anstatt dass nur der Absender Einträge liefert (UTXO), trägt auch der Empfänger mit einem seiner eigenen UTXOs bei. Dadurch werden die auf der Blockchain sichtbaren Informationen verwischt: Anstelle eines einzigen Eintrags, der dem tatsächlichen Betrag entspricht, gibt es nun zwei Einträge, und die Ausgaben spiegeln den ausgetauschten Betrag nicht direkt wider.
- Die endgültige Transaktion ähnelt einer Standard-Bitcoin-Transaktion (Multi-Input/Multi-Output), verbirgt aber dank einer steganografischen Struktur den tatsächlich gesendeten Betrag und die Verbindungen zwischen den Adressen.



**Zur Verwendung in Bull Bitcoin Mobile**




- **Empfangen** (Address Supply): PayJoin ist standardmäßig aktiviert.
- **Senden**: Das Wallet erkennt automatisch einen PayJoin URI und konfiguriert die Transaktion entsprechend, zum Beispiel:



```
bitcoin:bc1qp2nxbullbticoinzt6tx7x5tlnpzhv37?amount=0.000006&pj=HTTPS%3A%2F%2FPAYJO.IN%2F475QR36G3ZCFZ%23...
```




**Vorteile**




- **Erhöhte Vertraulichkeit**: PayJoin entkräftet die Annahme, dass alle Einträge in einer Transaktion zu einer einzigen Einheit gehören. Bei PayJoin kommen die Eingaben sowohl vom Absender als auch vom Empfänger, wodurch diese Annahme gebrochen wird.
- **Maskierung des Betrags**: Der tatsächlich ausgetauschte Betrag erscheint nicht direkt in den Ausgaben. Er wird als Differenz zwischen dem eingehenden und dem ausgehenden UTXO des Empfängers berechnet, wodurch die Analyse irreführend ist.



**Grenzen**




- PayJoin setzt voraus, dass der Sender und der Empfänger kompatible Wallets verwenden, andernfalls wird eine Standard-Onchain-Transaktion verwendet.
- Die Transaktion ist etwas komplexer (mehr Inputs und Outputs), was zu etwas höheren Kosten führt.
- Obwohl sie so konzipiert sind, dass sie einer Standardtransaktion ähneln, können fortgeschrittene Heuristiken (z. B. zweideutige Ausgaben, bekannte PayJoin-Server) den Verdacht aufkommen lassen, dass sie verwendet werden, auch wenn dies nicht absolut sicher ist.



**Weitere Informationen:**




- [Glossar](https://planb.network/fr/resources/glossary/payjoin)
- Chapitre [Les transactions PayJoin](https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c/c1e90b95-f709-4574-837b-2ec26b11286f)




### A2. Erläuterung zu Replace-by-fee (RBF)



**Definition**: Replace-by-fee (RBF) ist eine Funktion des Bitcoin-Netzwerks, die es dem Absender ermöglicht, die Bestätigung einer **onchain**-Transaktion zu beschleunigen, indem er sich bereit erklärt, eine höhere Gebühr zu zahlen.



**Grenzen** :




- RBF ist nicht für Liquid oder Lightning-Transaktionen verfügbar.
- Die erste Transaktion muss bei ihrer Erstellung als RBF-kompatibel gekennzeichnet werden, was Bull Bitcoin Mobile automatisch tut, sofern es nicht deaktiviert ist.



**Weitere Informationen:**




- [Glossar](https://planb.network/fr/resources/glossary/rbf-replacebyfee)




### A3. Bewährte Praktiken



Um **Bull Bitcoin Mobile** sicher und effizient zu nutzen, befolgen Sie diese Empfehlungen. Sie werden Ihnen helfen, Ihr Geld zu schützen, Ihre Transaktionen zu optimieren und Ihre Vertraulichkeit in den **Bitcoin (onchain)**, **Liquid** und **Lightning** Netzwerken zu wahren.





- **Sichern Sie Ihre Wiederherstellungsphrase**:
 - Tutorial: [Save your Mnemonic phrase](https://planb.network/fr/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270)
 - Cours [La phrase mnémonique](https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f/8f9340c1-e6dc-5557-a2f2-26c9669987d5)





- **Verwenden Sie eine sichere Authentifizierung**:
 - Aktivieren Sie eine **starke PIN** oder **biometrische Authentifizierung** (Fingerabdruck oder Gesichtserkennung), um den Zugang zur Anwendung zu schützen.
 - Geben Sie niemals Ihre PIN oder biometrischen Daten weiter.





- **Schützen Sie Ihre Privatsphäre** :
 - generate einen neuen Address für jeden Onchain- oder Liquid-Empfang, um die Verfolgung auf dem Blockchain zu begrenzen.
 - Verwenden Sie PayJoin, wenn verfügbar, um die Vertraulichkeit des in der Kette gesendeten Betrags zu erhöhen
 - Für maximale Vertraulichkeit sollten Sie Ihr Wallet über einen Electrum-Server mit Ihrem eigenen Bitcoin-Knoten verbinden, anstatt den öffentlichen Knoten zu benutzen





- Wählen Sie das für Ihre Bedürfnisse am besten geeignete **Netz**:
- **Onchain**: Bevorzugt für langfristige Verwahrung oder Transaktionen mit hohem Wert (Gebühren im Verhältnis zum Betrag vernachlässigbar).
- **Liquid**: Für schnelle, kostengünstige Überweisungen mit erhöhter Vertraulichkeit.
- **Lightning**: Entscheiden Sie sich für sofortige, kostengünstige Überweisungen für kleine Beträge. Wenn Sie zwei Wallet Bull Bitcoin Nutzer sind, wählen Sie Liquid, um Lightning <> Liquid Swap-Gebühren über Boltz zu vermeiden.





- **Überprüfen Sie immer die Lieferadressen**:
 - Prüfen Sie den Address sorgfältig, bevor Sie Geldmittel senden. Gelder, die an einen falschen Address gesendet werden, sind für immer verloren. Verwenden Sie Kopieren/Einfügen oder QR-Code-Scannen, kopieren/verändern Sie niemals einen Address von Hand.





- **Kosten optimieren**:
 - Wählen Sie für Onchain-Transaktionen je nach Dringlichkeit und Netzüberlastung geeignete Gebühren (langsam, mittel, schnell).
 - Verwenden Sie Liquid oder Lightning für kleine Mengen.
 - Aktivieren Sie Replace-by-fee (RBF) (siehe Anhang 4) für Onchain-Sendungen, wenn Sie eine schnellere Bestätigung erwarten.





- Halten Sie die Anwendung auf dem neuesten Stand




### A4. Zusätzliche Ressourcen





- **Offizielle Links und Unterstützung:**
- [staff@bitcoinsupport.com](mailto:staff@bitcoinsupport.com), **support@bullbitcoin.com**: Unterstützung per E-Mail
- [Offizielle Website von Bull Bitcoin](https://bullbitcoin.com/): **Informationen über die Dienstleistungen von Bull Bitcoin, Einrichtung eines Kontos, Zugang zur Anwendung**
- [GitHub Bull Bitcoin Mobile](https://github.com/SatoshiPortal/bullbitcoin-mobile): **Code, Entwicklung und Roadmap einsehen, zur Entwicklung beitragen...**
- [Konto X - Twitter Bull Bitcoin](https://x.com/BullBitcoin_)
- **Telegram**-Gruppe für Wallet mobile: Gruppenchat mit Support, siehe Seite "Einstellungen".





- **Block Explorers:**
 - on chain : **[Mempool.space](https://Mempool.space/)**
 - Liquid : **[Blockstream Info](https://blockstream.info/Liquid)**
 - Blitzschlag: **[1ML (Lightning Network)](https://1ml.com/)**





- Lernen und Tutorien: **[Plan ₿ Network](https://planb.network/)**
 - Sicherung des Wiederherstellungssatzes



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270



https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f




- **Liquid Network** :
- [Glossar](https://planb.network/resources/glossary/liquid-network)




https://planb.network/courses/6d26bcff-51a3-405f-bcdd-9af8297ce727





- **Lightning Network**:
- [Glossar](https://planb.network/resources/glossary/lightning-network)




https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb


### A5. Bulle Bitcoin



#### Überblick über das Unternehmen



**[Bull Bitcoin](https://www.bullbitcoin.com/fr)**, ist die älteste nicht depotgebundene Exchange-Plattform, die sich ausschließlich dem Bitcoin widmet und 2013 in der Bitcoin-Botschaft in Montreal, Kanada, gegründet wurde. Unter der Leitung von Francis Pouliot, einem anerkannten Pionier im Bitcoin-Ökosystem, positioniert sich das Unternehmen als Hauptakteur bei der Förderung der finanziellen Souveränität und der Autonomie der Nutzer. Seine Mission ist es, Einzelpersonen zu ermöglichen, die Kontrolle über ihr Geld wiederzuerlangen, indem sie Bitcoin als Werkzeug für Freiheit und Bezahlung nutzen, während sie Fiat-Währungen und andere Kryptowährungen als Bitcoin ablehnen.



![image](assets/fr/26.webp)



[Erstellen Sie Ihr Konto] (https://app.bullbitcoin.com/registration/orangepeel) mit 0,25% Rabatt auf Bitcoin Einkäufe und Verkäufe.



#### Werte und Philosophie



Der Bulle Bitcoin zeichnet sich durch seine Commitment- bis Cypherpunk-Grundsätze und Bitcoin-Ethik aus:





- **Ausschließlicher Fokus auf Bitcoin**: Die Plattform bleibt der Vision einer dezentralen, zensurresistenten Währung treu.





- **Nicht-Verwahrstelle**: Die Nutzer behalten die volle Kontrolle über ihre Bitcoins, indem sie die Gelder in ihre eigenen Portfolios schicken.





- **Vertraulichkeit**: Minimale Erfassung von persönlichen Daten, mit KYC-freien Kaufoptionen für Transaktionen unter 999 USD. Die Daten werden im Einklang mit den Vorschriften (FINTRAC in Kanada, AMF in Frankreich) geschützt.





- **Transparenz**: Keine versteckten Gebühren, die Kosten sind in der Spanne (der Differenz zwischen Kauf- und Verkaufspreis) enthalten.





- **Finanzielle Souveränität**: Die Bulle Bitcoin fördert die Unabhängigkeit von traditionellen Bankensystemen und zentralisierten Institutionen.



#### Wichtigste Dienstleistungen





- **Fiat-Einzahlung**: Benutzer können ihr Bull Bitcoin-Konto mit Fiat-Währung (CAD, EUR usw.) per Banküberweisung oder Bargeld/Debitkarte bei ausgewählten kanadischen Postämtern aufladen.





- **Kauf von Bitcoin**: Die Nutzer können Bitcoin kaufen, das direkt an ihr nicht depotgebundenes Portfolio gesendet wird, wodurch die vollständige Kontrolle über ihre Mittel gewährleistet ist.





- **Geplanter Bitcoin-Kauf**: Bull Bitcoin bietet einen automatisierten, wiederkehrenden Kaufservice (DCA - Dollar Cost Averaging) in regelmäßigen Abständen, der auf Ihr verfügbares Guthaben zurückgreift, mit direktem Transfer von Bitcoins auf ein vom Benutzer kontrolliertes Wallet, wodurch die Auswirkungen von Preisschwankungen reduziert werden.



Beachten Sie, dass eine Option namens "AutoBuy" es Ihnen ermöglicht, Ihre Fiats umzuwandeln, sobald sie Ihr Bull Bitcoin-Guthaben berühren, und Ihre Bitcoins an Ihr eigenes Wallet zu senden. Diese Option kann auch mit einer wiederkehrenden Überweisung kombiniert werden, die mit Ihrer Bank geplant wird, um eine DCA zu machen. Diese Option automatisiert Ihre Bitcoin Akkumulation, ohne dass Sie die Anwendung öffnen müssen.






- **Bitcoin zu einem festen Preis kaufen 'Limit Order'**: Ermöglicht den Kauf von Bitcoin zu einem vom Benutzer im Voraus festgelegten Preis, der automatisch ausgeführt wird, wenn der Bull Bitcoin Indexpreis das festgelegte Limit erreicht oder unterschreitet.





- **Verkaufen von Bitcoin**: Nutzer können ihre Bitcoins verkaufen und erhalten das Geld in Fiat-Währung direkt auf ihr Bankkonto per Bank- oder SEPA-Überweisung.





- **Zahlungen von Dritten**: Bull Bitcoin ermöglicht es Nutzern, Fiat-Geld von ihren Bitcoins an Bankkonten zu senden, völlig transparent für den Empfänger.





- **Bull Bitcoin Prime**: Bull Bitcoin Prime ist ein Premium-Service für vermögende Kunden und Unternehmen, der maßgeschneiderte Lösungen und erstklassigen Support bietet. Dies beinhaltet den Zugang zu reduzierten Gebühren, einen eigenen Kundenbetreuer und maßgeschneiderte Unternehmensdienstleistungen. Dieser Service richtet sich an Institutionen, professionelle Händler und Firmenkunden, die fundiertes Fachwissen und eine bevorzugte Behandlung wünschen.





- **Mobiles Wallet**: Bull Bitcoin bietet ein quelloffenes, selbstverwaltendes mobiles Wallet an, das auf Android und iOS verfügbar ist und Onchain-, Liquid- und Lightning Network-Transaktionen unterstützt.





- **Pädagogische Unterstützung**: Kostenlose Leitfäden und persönliches Coaching, um den Nutzern bei der Erstellung, Sicherung und Verwaltung ihrer Bitcoin-Portfolios zu helfen und die finanzielle Autonomie zu stärken.



#### Einhaltung der Vorschriften und Sicherheit





- **Regulatorisch**: Bull Bitcoin ist bei FINTRAC (Kanada) und AMF (Frankreich) registriert und erfüllt die KYC/AML-Anforderungen.





- **Sicherheit**: Verwendung von sicheren Portfolios und Empfehlungen zur Offline-Speicherung. Persönliche Daten werden auf der Bitcoin-Infrastruktur von Bull gehostet, die zu 100 % selbst gehostet wird und nicht von Dritten abhängig ist.