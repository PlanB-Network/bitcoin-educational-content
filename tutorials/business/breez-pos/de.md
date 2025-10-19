---
name: Breez - POS
description: Breez macht es einfach, Bitcoin-Zahlungen für Ihr Unternehmen einzuziehen.
---

![cover](assets/cover.webp)



Seit der COVID-19-Pandemie hat sich der kontaktlose digitale Zahlungsverkehr selbst in den kleinsten Geschäften durchgesetzt. In dieser Zeit haben viele Unternehmen die Praktikabilität von Bitcoin-Bargeldlösungen entdeckt, mit denen sie Zahlungen aus der ganzen Welt empfangen können. Allerdings sind diese Lösungen manchmal schwierig zu bedienen oder für kleine Unternehmen ungeeignet. In diesem Tutorial werden wir einen Blick auf das Breez-Zahlungsterminal werfen, eine Lösung, die sich durch ihre Benutzerfreundlichkeit auszeichnet und Ihnen gleichzeitig die volle Kontrolle über die Verwaltung Ihrer Bitcoins gibt.



## Breez POS installieren



Breez POS ist ein Selbstverwahrungsdienst, der durch den Breez Wallet bereitgestellt wird. Der Nutzen dieses Dienstes besteht darin, Händlern die Möglichkeit zu geben, Zahlungen über Bitcoin einzuziehen, während sie auf einem einfachen Interface verbleiben, ähnlich wie bei den verschiedenen Lightning-Brieftaschen. Breez POS ist auf den Download-Plattformen [Google Play Store](https://play.google.com/store/apps/details?id=com.breez.client) (Android) und [App Store](https://apps.apple.com/app/breez-lightning-client-pos/id1463604142) (iOS) verfügbar.



![download](assets/fr/01.webp)



![setup](assets/fr/12.webp)



⚠️ Wir weisen darauf hin, dass sich diese Anwendungen noch in der Entwicklung befinden und dass es bei der Nutzung der Funktionalitäten zu Fehlern kommen kann. Wir empfehlen eine moderate Nutzung.



Mit dieser Anwendung gibt Ihnen Breez die vollständige Kontrolle über Netzwerkkonfigurationen und Gebühreneinstellungen und garantiert Ihnen gleichzeitig die Souveränität bei der Verwaltung Ihrer Bitcoins.



Sie können die verschiedenen Wallet-Optionen von Breez erkunden, indem Sie unserer Anleitung unten folgen. Dieser Schritt wird Ihnen helfen, das Point-of-Sale-Ökosystem besser zu verstehen und Best Practices anzuwenden, um die mit Ihrem seed verbundenen Bitcoins effektiv zu sichern.



https://planb.network/tutorials/wallet/mobile/breez-46a6867b-c74b-45e7-869c-10a4e0263c06

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270


## Verwendung von Breez POS



In diesem Tutorial konzentrieren wir uns auf den Bereich "*Point-of-Sale*", um Ihnen zu zeigen, wie Sie ihn als Zahlungsmittel in Ihr Unternehmen integrieren können.



Die Verkaufsstelle ist ein integraler Bestandteil des Breez-Portfolios und stützt sich in erster Linie auf den Lightning Network, um Zahlungen einzuziehen.



Im Menü "*Verkaufsstelle*" finden Sie einen Interface für den Einzug von Zahlungen. Es ist in zwei Teile unterteilt:



### Lastschriftverfahren



Der erste Teil ist die Tastatur für den Lastschrifteinzug. Diese Interface ist praktisch für den Einzug einer einzigen Zahlung, wenn Sie die Gesamteinkäufe Ihrer Kunden kennen oder wenn Sie in Ihrem Unternehmen keinen festen Produktkatalog benötigen (z. B. bei freiberuflichen Dienstleistungen).



![keyboard](assets/fr/02.webp)



Um die Breez-Kasse zum ersten Mal zu benutzen, müssen Sie eine Zahlung von über 2.500 Satoshis (etwa 3 Euro zum heutigen Exchange-Kurs) leisten. Dieser Betrag, der nur bei der ersten Auszahlung gezahlt wird, stellt die Kosten für die Einrichtung eines Zahlungskanals dar, damit Sie mit anderen Lightning Network-Knoten kommunizieren und Satoshis senden und empfangen können.



![channel_fee](assets/fr/03.webp)


### Produktkatalog



Der zweite Teil ist der Produktkatalog. Dieser Interface ist ideal, wenn Sie einen Produktkatalog mit vordefinierten Preisen haben. Hier können Sie Ihre Produkte vorkonfigurieren und sie dann für generate-Rechnungen verwenden, um die Rückverfolgbarkeit Ihrer Kasseneinnahmen zu verbessern.



![items](assets/fr/04.webp)



Sie können jeden Artikel aus dieser Interface manuell konfigurieren, indem Sie auf die Schaltfläche "**Plus**" klicken und dann den Namen, den Preis und eine Kennung für diesen Artikel festlegen.



![add_items](assets/fr/05.webp)



Sie können sie dann hinzufügen und ihre Menge festlegen, um die zugehörige Zahlung einzuziehen.



Wenn Ihr Katalog recht umfangreich ist, kann es kompliziert werden, Ihre Produkte einzeln hinzuzufügen. Zu diesem Zweck können Sie im Bereich **Einstellungen > Verkaufsstelleneinstellungen** im Menü "Artikelliste" Ihre Artikelliste automatisch aus CSV-Dateien importieren und exportieren.



![import](assets/fr/07.webp)



In diesem Abschnitt können Sie auch die Gültigkeitsdauer Ihrer Lightning-Rechnungen festlegen. Von nun an haben Ihre Kunden für alle Ihre Rechnungen `N` Sekunden Zeit, um ihre Zahlung zu leisten, andernfalls müssen Sie eine neue Lightning Invoice erstellen.



![invoice_time](assets/fr/08.webp)



Als Manager können Sie die Sicherheit Ihrer Bitcoins erhöhen, indem Sie ein Passwort hinzufügen, das für alle ausgehenden Zahlungen von Ihrem Wallet erforderlich ist. Diese Funktion ist besonders nützlich, wenn Sie nicht der Einzige sind, der Ihre Verkaufsstelle verwaltet.



![manager](assets/fr/09.webp)



Im Menü **Transaktionen** finden Sie eine Liste mit allen Zahlungen, die Sie eingezogen haben. Sie können die Ergebnisse auch nach einem bestimmten Zeitraum filtern, indem Sie auf die Schaltfläche **Kalender** klicken.



![transactions](assets/fr/10.webp)



Sie können auch eine tägliche Übersicht über Ihre Verkäufe und den gesammelten Gesamtbetrag einsehen, indem Sie auf die Schaltfläche **Dokument** klicken.



![summary](assets/fr/11.webp)



Sie haben nun ein vollständiges Verständnis für den Point-of-Sale, den die Breez-Anwendung für die nahtlose Integration von Bitcoin in Ihr Unternehmen bietet. Wenn Sie dieses Tutorial nützlich fanden, empfehlen wir Ihnen unser Tutorial über be-BOP, eine E-Commerce-Plattform, mit der Sie Zahlungen in Bitcoins entgegennehmen und Ihr Geschäft monetarisieren können.



https://planb.network/tutorials/business/point-of-sale/be-bop-d8c40a3b-9090-48e7-9ba7-235d0c17e5fa