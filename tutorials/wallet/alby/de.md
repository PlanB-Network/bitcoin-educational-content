---
name: Alby

description: Browser-Erweiterung für Bitcoin und Lightning Network
---

![cover](assets/cover.webp)




Zahlungen mit Bitcoin immer einfacher zu machen, ist die Herausforderung, vor der viele Unternehmen in diesem Sektor stehen. Alby hebt sich mit seiner Alby wallet-Erweiterung für Browser von der Masse ab. Diese Erweiterung zielt darauf ab, einen flüssigen Rahmen einzurichten, der automatisch Adressen erkennt und es Ihnen ermöglicht, reibungslose Bitcoin-Zahlungen durchzuführen. In diesem Tutorial lernen wir die Alby-Erweiterung kennen und testen, wie sie Zahlungen über den Browser ermöglicht.




![video](https://youtu.be/nd5fX2vHuDw)




## Alby-Verlängerung



Die Alby-Erweiterung ist ein Werkzeug, das es Ihrem Webbrowser ermöglicht, einfach und sicher mit dem Bitcoin-Netz und seiner Lightning Network-Schicht zu interagieren. Sie zeichnet sich durch drei Aspekte aus:




- Lightning Network wallet: Verknüpfen Sie Ihren Alby-Knoten oder Ihr Konto, um Bitcoin schnell und kostengünstig über die Lightning Network-Schicht zu senden und zu empfangen.
- Flüssige Zahlungen über das Web: Für Bitcoin-Zahlungen auf Websites, die Lightning unterstützen, müssen Sie keine QR-Codes scannen oder zwischen Anwendungen wechseln. Es ermöglicht reibungslose Transaktionen mit einem einzigen Klick, oder ohne Bestätigung, wenn Sie ein Budget festgelegt haben.
- Ein Nostr-Manager: Die Erweiterung verwaltet Ihre Nostr-Schlüssel und macht es einfach, sich mit Nostr-Anwendungen zu verbinden und mit ihnen zu interagieren, indem sie als sicherer Unterzeichner fungiert, ohne dass Ihr privater Schlüssel für jede Plattform offengelegt wird.



https://planb.academy/tutorials/node/others/nostr-f6d21a64-9b04-4f21-ba1c-02c98cc91f98

https://planb.academy/tutorials/node/others/umbrel-nostr-7ae147e8-f5cd-46e1-861b-17c2ea1e08fd

## Verbindung mit der Nebenstelle



In diesem Tutorial werden wir die Alby-Erweiterung im Firefox-Browser unter einem Ubuntu-Betriebssystem verwenden. Sie ist jedoch auch unter Windows und mit Browsern wie Chrome verfügbar.



Sie können die Alby-Erweiterung zu Ihrem Browser hinzufügen, indem Sie den Erweiterungsspeicher [Firefox](https://addons.mozilla.org/fr/firefox/addon/alby/) oder den Erweiterungsspeicher [Chrome](https://chromewebstore.google.com/detail/alby-bitcoin-wallet-for-l/iokeahhehimjnekafflcihljlcjccdbe) besuchen.



![firefox](assets/fr/01.webp)



![chrome](assets/fr/02.webp)



ℹ️ Es ist wichtig zu überprüfen, dass der Autor der Erweiterung tatsächlich das offizielle Alby-Konto ist, um jegliche Form von Piraterie oder Diebstahl Ihrer Bitcoins zu vermeiden.



Fügen Sie die Erweiterung zu Ihrem Browser hinzu, indem Sie auf die Schaltfläche auf der rechten Seite klicken.


Erteilen Sie die erforderlichen Berechtigungen für die Installation und Verwendung der Erweiterung, und heften Sie die Erweiterung dann an die Symbolleiste, damit sie leicht abgerufen werden kann.



![pin](assets/fr/03.webp)



Sie sollten auch einen Freischaltcode festlegen (sehr wichtig), der einen sicheren Zugang zu Ihrem Lightning wallet über Ihren Browser gewährleistet. Wir empfehlen Ihnen, ein starkes alphanumerisches Passwort festzulegen.



ℹ️ Bewahren Sie dieses Passwort an einem sicheren Ort auf, damit Sie darauf zugreifen können, falls Sie es vergessen, da es zwar geändert, aber nicht wiederhergestellt werden kann.



https://planb.academy/tutorials/computer-security/authentication/seedkeeper-password-64ffaf68-53aa-43c3-bc7a-c1dc2a17fee3

![pass](assets/fr/04.webp)



Alby beweist seine Anpassungsfähigkeit, indem es Ihnen zwei Wahlmöglichkeiten bietet:




- Fahren Sie mit einem Alby-Konto fort, wenn Sie die Anwendungen nutzen und gleichzeitig die Kontrolle über Ihre Bitcoins behalten möchten.
- Schließen Sie Ihren eigenen wallet- oder Lightning-Knoten an, wenn Sie bereits einen haben, der von der Erweiterung unterstützt wird.



https://planb.academy/tutorials/wallet/mobile/blink-7ea5f5a4-e728-4ff9-b3f9-cf20aa6fc2bd

https://planb.academy/tutorials/node/lightning-network/lightning-network-daemon-linux-59d777e9-72c8-4b32-8c50-e86cdae8f2f9

https://planb.academy/tutorials/business/point-of-sale/btcpay-server-928eb01e-824b-4b57-a3e8-8727633beddc


In diesem Lernprogramm entscheiden wir uns, mit dem Alby-Konto fortzufahren, um die Vorteile des Alby-Ökosystems zu nutzen.



https://planb.academy/tutorials/wallet/mobile/alby-go-40202802-b346-4a3c-9863-465c3bde9903

https://planb.academy/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a

Melden Sie sich bei Ihrem Alby-Konto an, oder erstellen Sie eines, wenn Sie noch keines haben.



![signup](assets/fr/05.webp)



## Ihre ersten Zahlungen



Wenn Sie angemeldet sind, können Sie auf die Erweiterung Alby in der Symbolleiste klicken, um auf Ihr Portfolio zuzugreifen.



![buzzin](assets/fr/06.webp)



Sobald Sie Ihr Alby-Konto erstellt haben, müssen Sie es mit einem wallet verbinden, um Satoshis auszugeben. Um den Bitcoin-wallet mit Ihrem Alby-Konto zu verbinden, empfehlen wir Ihnen, einen Alby Hub-Knoten zu verwenden, den Sie entweder auf Ihrem Computer einrichten oder einen von Alby angebotenen Plan abonnieren können.



![hubplan](assets/fr/13.webp)




In diesem Lernprogramm wird unser Alby-Konto durch eine lokale Installation auf unserem Rechner unterstützt.


Um Ihren eigenen Alby-Knoten zu bauen, empfehlen wir unser Alby Hub-Tutorial.



https://planb.academy/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a

Mit diesem Knoten können Sie selbstverwaltete Lightning-Portfolios erstellen und Ihre Lightning-Kanäle effizient verwalten, um Satoshis zu senden und zu empfangen.



![channels](assets/fr/14.webp)



Öffnen Sie Empfangskanäle, die die Gesamtzahl der Satoshis festlegen, die Sie empfangen können.



![receivechanal](assets/fr/15.webp)



Öffnen Sie Sendekanäle, indem Sie Satoshis für eine Bitcoin-Onchain-Adresse blockieren. Die Satoshis, die Sie blockiert haben, bestimmen die Gesamtzahl der Satoshis, die Sie ausgeben können.



![spend](assets/fr/16.webp)



Sie können jetzt Satoshis über die Alby-Erweiterung senden und empfangen.



![exchange](assets/fr/08.webp)



Ab diesem Zeitpunkt ist die Alby-Erweiterung in der Lage, Lightning-Adressen und Rechnungen zu erkennen, die auf den von Ihnen besuchten Webseiten verfügbar sind, und schlägt vor, dass Sie diese in Bitcoin oder Lightning direkt von Ihrer Erweiterung aus bezahlen.



![suggest](assets/fr/09.webp)



![pay](assets/fr/10.webp)




## Sichern von Wiederherstellungsschlüsseln mit dem Hauptschlüssel



Der von der Alby-Erweiterung angebotene Hauptschlüssel fungiert als Schutzschicht, die eine sichere Kommunikation mit der Bitcoin-Hauptnetzebene (Onchain) und dem Nostr-System ermöglicht und die Aktivierung der Lightning-Verbindung mit Nostr-Anwendungen erlaubt.



![masterKey](assets/fr/11.webp)



Dieser Hauptschlüssel besteht aus 12 Wörtern, die Ihrer Wiederherstellungsphrase ähneln. Wir empfehlen Ihnen daher, ihn mit sicheren Methoden zu speichern, um sicherzustellen, dass Sie jederzeit darauf zugreifen können.



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270


![masterKey](assets/fr/12.webp)



Sie können jetzt reibungslose Bitcoin- und Lightning-Zahlungen mit der Alby-Erweiterung erleben. Wenn Ihnen dieses Tutorial gefallen hat, empfehlen wir Ihnen unser Alby Hub-Tutorial, um Ihren eigenen Alby-Knoten einzurichten und alle Aspekte Ihrer Alby-Wallets über eine reibungslose und leistungsstarke Schnittstelle zu steuern.



https://planb.academy/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a