---
name: Aqua
description: Bitcoin, Lightning und Liquid in einer einzigen Wallet
---
![cover](assets/cover.webp)

Aqua ist eine mobile Anwendung, die es einfach macht, eine Hot Wallet für Bitcoin und Liquid zu erstellen, und bietet auch die Möglichkeit, Lightning ohne die Komplexität der Verwaltung eines Nodes zu nutzen, dank integrierter Swaps. Es ermöglicht auch die Verwaltung von USDT-Stablecoins auf verschiedenen Netzwerken.

Entwickelt von der JAN3-Firma unter der Leitung von Samson Mow, wurde die Aqua-App zunächst speziell für die Bedürfnisse von Nutzern in Lateinamerika entwickelt, ist aber für jeden Nutzer weltweit geeignet. Sie ist besonders interessant für Anfänger und diejenigen, die Bitcoin täglich für ihre Zahlungen verwenden.

In diesem Tutorial werden wir herausfinden, wie man die vielen Funktionen von Aqua nutzt. Aber bevor wir das tun, nehmen wir uns einen Moment Zeit, um zu verstehen, was eine Sidechain in Bitcoin ist und wie Liquid funktioniert, damit wir den vollen Wert von Aqua verstehen.

![AQUA](assets/fr/01.webp)

## Was ist eine Sidechain?

Das Bitcoin-Protokoll hat absichtlich technische Beschränkungen, die dazu beitragen, die Dezentralisierung des Netzwerks aufrechtzuerhalten und sicherzustellen, dass die Sicherheit auf alle Nutzer verteilt wird. Diese Beschränkungen können jedoch manchmal frustrierend für die Nutzer sein, insbesondere bei Überlastung durch ein hohes Volumen an gleichzeitigen Transaktionen. Die Debatte über die Skalierbarkeit von Bitcoin hat die Gemeinschaft lange gespalten, insbesondere während des Blocksize War. Seitdem ist es in der Bitcoin-Community weit verbreitet, dass die Skalierbarkeit durch Off-Chain-Lösungen und Second-Layer-Systeme sichergestellt werden muss. Zu diesen Lösungen gehören Sidechains, die im Vergleich zu anderen Systemen wie dem Lightning Network noch relativ unbekannt und wenig genutzt sind.

Eine Sidechain ist eine unabhängige Blockchain, die parallel zur Haupt-Bitcoin-Blockchain läuft. Sie verwendet Bitcoin als Rechnungseinheit, dank eines Mechanismus namens "Two-Way Peg". Dieses System ermöglicht es, Bitcoins auf der Hauptkette zu sperren, um ihren Wert auf der Sidechain zu reproduzieren, wo sie in Form von Tokens zirkulieren, die durch die ursprünglichen Bitcoins gedeckt sind. Diese Token behalten normalerweise den Wertparität mit den auf der Hauptkette gesperrten Bitcoins, und der Prozess kann umgekehrt werden, um Mittel auf Bitcoin zurückzuerhalten.

Ziel der Sidechains ist es, zusätzliche Funktionen oder technische Verbesserungen wie schnellere Transaktionen, niedrigere Gebühren oder Unterstützung für Smart Contracts anzubieten. Diese Innovationen können nicht immer direkt auf der Bitcoin-Blockchain implementiert werden, ohne die Dezentralisierung oder Sicherheit zu gefährden. Sidechains ermöglichen es also, neue Lösungen zu testen und zu erkunden, während die Integrität von Bitcoin erhalten bleibt. Diese Protokolle erfordern jedoch oft Kompromisse, insbesondere in Bezug auf Dezentralisierung und Sicherheit, abhängig vom Governance-Modell und dem gewählten Konsensmechanismus.

## Was ist Liquid?

Liquid ist eine föderierte Sidechain-Overlay für Bitcoin, die von Blockstream entwickelt wurde, um die Transaktionsgeschwindigkeit, Privatsphäre und Funktionalität zu verbessern. Sie verwendet einen bilateralen Ankermechanismus, der auf einer Föderation eingerichtet ist, um Bitcoins auf der Hauptkette zu sperren und im Gegenzug Liquid-Bitcoins (L-BTC) zu erstellen, Tokens, die auf Liquid zirkulieren, während sie durch die ursprünglichen Bitcoins gedeckt bleiben.

![AQUA](assets/fr/02.webp)

Das Liquid-Netzwerk basiert auf einer Föderation von Teilnehmern, die aus anerkannten Einheiten des Bitcoin-Ökosystems bestehen, die Blöcke validieren und bilaterale Verankerungen verwalten. Neben L-BTC ermöglicht Liquid auch die Ausgabe anderer digitaler Vermögenswerte, wie USDT-Stablecoin und andere Kryptowährungen.

![AQUA](assets/fr/03.webp)

## Aqua installieren

Der erste Schritt ist natürlich, die Aqua-App herunterzuladen. Gehe zu deinem App-Store:

- [Für Android](https://play.google.com/store/apps/details?id=io.aquawallet.android);
- [Für Apple](https://apps.apple.com/us/app/aqua-wallet/id6468594241).
![AQUA](assets/fr/04.webp)

Für Android-Nutzer besteht auch die Möglichkeit, die Anwendung über die .apk-Datei zu installieren, die auf ihrem GitHub verfügbar ist. (https://github.com/AquaWallet/aqua-wallet/releases).

![AQUA](assets/fr/05.webp)

Starte die Anwendung und prüfe dann das Kästchen *"Ich habe die Nutzungsbedingungen und Datenschutzrichtlinien gelesen und stimme ihnen zu".*

![AQUA](assets/fr/06.webp)

## Wallet in Aqua erstellen

Klicke auf die Schaltfläche "*Create Wallet*".

![AQUA](assets/fr/07.webp)

Und voilà, deine Wallet ist bereits erstellt!

![AQUA](assets/fr/08.webp)

Da es sich um eine selbstverwahrende Wallet handelt, ist es unerlässlich, eine physische Sicherung deiner Mnemonic-Phrase durchzuführen. **Diese Mnemonic-Phrase gibt dir vollen, unbeschränkten Zugang zu allen deinen Bitcoins.** Jeder, der diese Mnemonic-Phrase besitzt, kann deine Mittel stehlen, selbst ohne physischen Zugriff auf dein Telefon.

Sie ermöglicht es dir, den Zugriff auf deine Bitcoins im Falle von Verlust, Diebstahl oder Bruch deines Telefons wiederherzustellen. Es ist daher sehr wichtig, sie sorgfältig auf einem physischen Medium (nicht digital) zu speichern und an einem sicheren Ort aufzubewahren. Du kannst sie auf ein Stück Papier schreiben oder, für zusätzlichen Schutz, falls es sich um eine große Wallet handelt, empfehle ich, sie auf einen Edelstahlträger zu gravieren, um sie vor Feuer-, Überschwemmungs- oder Einsturzrisiko zu schützen (für eine Hot Wallet, die zur Sicherung einer kleinen Menge Bitcoins konzipiert ist, ist eine einfache Papier-Sicherung wahrscheinlich ausreichend).

Dazu klicke auf das Einstellungsmenü.

![AQUA](assets/fr/09.webp)

Klicke dann auf _"Seed-Phrase anzeigen"_. Mach eine physische Sicherung dieser 12-wörtigen Phrase.

![AQUA](assets/fr/10.webp)

In demselben Einstellungsmenü kannst du auch die Anwendungssprache und die verwendete Fiat-Währung ändern.

![AQUA](assets/fr/11.webp)

Bevor du deine ersten Bitcoins in deiner Wallet empfängst, **rate ich dir dringend, eine leere Wiederherstellungstest durchzuführen**. Notiere dir einige Referenzinformationen, wie deine xpub oder deine erste Empfangsadresse, lösche dann deine Wallet in der Aqua-App, während sie noch leer ist. Versuche dann, deine Wallet mit deinem Papier-Backup wiederherzustellen. Überprüfe, ob die nach der Wiederherstellung erzeugten Informationen mit denen übereinstimmen, die du ursprünglich notiert hast. Wenn ja, kannst du sicher sein, dass dein Papier-Backup zuverlässig ist. Weitere Informationen dazu, wie man einen Wiederherstellungstest durchführt, findest du in diesem anderen Tutorial:

https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

Du kannst es auf meinem Bildschirm nicht sehen, da ich einen Emulator verwende, aber in den Einstellungen findest du eine Option, um die App mit einem biometrischen Authentifizierungssystem zu sperren. Ich empfehle dringend, dieses Sicherheitsmerkmal zu aktivieren, da ohne es jeder, der Zugriff auf dein entsperrtes Telefon hat, deine Bitcoins stehlen könnte. Du kannst Face ID auf iOS oder deinen Fingerabdruck auf Android verwenden. Falls diese Methoden während der Authentifizierung fehlschlagen, kannst du die App immer noch mit dem PIN-Code deines Telefons aufrufen.


## Bitcoins auf Aqua empfangen

Jetzt, da deine Wallet eingerichtet ist, bist du bereit, deine ersten Sats zu empfangen! Klicke einfach auf die "*Empfangen*"-Schaltfläche im "*Wallet*"-Menü.

![AQUA](assets/fr/12.webp)

Du kannst wählen, Bitcoins On-Chain, auf Liquid oder über Lightning zu empfangen.

![AQUA](assets/fr/13.webp)

Für On-Chain-Transaktionen wird Aqua eine spezifische Empfangsadresse generieren, an die du deine Sats empfangen kannst.

![AQUA](assets/fr/14.webp)

Ebenso wird Aqua dir, wenn du Liquid wählst, eine Liquid-Adresse zur Verfügung stellen.

![AQUA](assets/fr/15.webp)

Falls du die Mittel lieber über Lightning empfangen möchtest, musst du zunächst den gewünschten Betrag angeben.

![AQUA](assets/fr/16.webp)

Klicke dann auf "*Invoice erstellen*".

![AQUA](assets/fr/17.webp)

Aqua wird eine Invoice erstellen, um Guthaben von einer Lightning-Wallet zu empfangen. Beachte, dass, im Gegensatz zu den Optionen On-Chain und Liquid, die über Lightning empfangenen Guthaben automatisch in L-BTC auf Liquid umgewandelt werden, unter Verwendung des Boltz-Tools, da Aqua kein Lightning-Node ist. Dieser Prozess ermöglicht es dir, Guthaben über Lightning zu empfangen und zu senden, ohne deine Bitcoins jemals auf Lightning zu speichern.

![AQUA](assets/fr/18.webp)

Ich werde mit dem Senden von Bitcoins über Lightning an Aqua beginnen. Sobald die Transaktion mit der bereitgestellten Invoice abgeschlossen ist, erhalten wir eine Bestätigung.

![AQUA](assets/fr/19.webp)

Um den Fortschritt des Swaps zu verfolgen, gehe zur Startseite deiner Wallet und klicke auf das "L2 Bitcoin"-Konto, das Lightning (über Swap) und Liquid-Transaktionen auflistet.

![AQUA](assets/fr/20.webp)

Hier kannst du deine Transaktion und dein L-BTC-Guthaben einsehen.

![AQUA](assets/fr/21.webp)

## Bitcoin Swap mit Aqua

Jetzt, da du Vermögenswerte in deiner Aqua-Wallet hast, kannst du sie direkt über die App swappen, um sie auf die Haupt-Bitcoin-Blockchain oder auf Liquid zu übertragen. Du kannst auch deine Bitcoins in USDT-Stablecoin (oder andere) umtauschen. Gehe dazu in das Menü "*Marketplace*".

![AQUA](assets/fr/22.webp)

Klicke auf "*Swaps*".

![AQUA](assets/fr/23.webp)

Wähle im Feld "*Transfer von*" den Vermögenswert aus, en du handeln möchtest. Derzeit besitze ich nur L-BTC, also wähle ich dies aus.

![AQUA](assets/fr/24.webp)

Wähle im Feld "*Transfer to*" den Zielwert für den Swap aus. Ich habe mich für USDT im Liquid-Netzwerk entschieden.

![AQUA](assets/fr/25.webp)

Gib den Betrag ein, den du umtauschen möchtest.

![AQUA](assets/fr/26.webp)

Bestätige mit einem Klick auf "*Fortfahren*".

![AQUA](assets/fr/27.webp)

Stelle sicher, dass du mit den Swap-Einstellungen zufrieden bist, und bestätige, indem du den "Swap"-Button unten auf dem Bildschirm nach rechts ziehst.

![AQUA](assets/fr/28.webp)

Dein Swap ist jetzt bestätigt.

![AQUA](assets/fr/29.webp)

Schau zurück auf deine Wallet, und du wirst sehen, dass wir jetzt USDT auf Liquid haben.

![AQUA](assets/fr/30.webp)

## Bitcoins mit Aqua senden

Jetzt, da du Bitcoins in deiner Aqua-Wallet hast, kannst du sie senden. Klicke auf die "*Senden*"-Schaltfläche.

![AQUA](assets/fr/31.webp)

Wähle den Vermögenswert oder das Netzwerk, um die Transaktion durchzuführen. Ich werde Bitcoins über Lightning senden.

![AQUA](assets/fr/32.webp)

Gib dann die für die Zahlung benötigten Informationen ein: Für On-Chain- oder Liquid-Bitcoins musst du eine Empfangsadresse eingeben; für Lightning ist eine Invoice erforderlich. Du kannst diese Informationen direkt in das bereitgestellte Feld einfügen oder das QR-Code-Symbol verwenden, um deine Kamera zu öffnen und die Adresse oder Rechnung zu scannen. Klicke dann auf "*Weiter*".

![AQUA](assets/fr/33.webp)

Klicke auf "Weiter", falls alle Informationen korrekt zu sein scheinen.

![AQUA](assets/fr/34.webp)

Aqua zeigt dir dann eine Zusammenfassung der Transaktion. Stelle sicher, dass alle Informationen korrekt sind, einschließlich der Zieladresse, Gebühren und des Betrags. Um die Transaktion zu bestätigen, ziehe den "Ziehen zum Senden"-Button unten auf dem Bildschirm nach rechts.

![AQUA](assets/fr/35.webp)

Du erhältst dann eine Bestätigung des Versands.

![AQUA](assets/fr/36.webp)

Jetzt weißt du, wie du die Aqua-App nutzen kannst, um Mittel auf Bitcoin, Lightning und Liquid zu empfangen und auszuzahlen, alles von einer einzigen Schnittstelle aus.

Falls dir dieses Tutorial hilfreich war, wäre ich dankbar, wenn du unten einen grünen Daumen hinterlässt. Teile diesen Artikel gerne in deinen sozialen Netzwerken. Vielen Dank!

Ich empfehle dir auch, dieses andere umfassende Tutorial über die Blockstream Green Mobile App zu lesen, das eine weitere interessante Lösung für die Einrichtung deiner Liquid Wallet ist:

https://planb.academy/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a

