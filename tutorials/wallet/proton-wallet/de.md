---
name: Proton-Geldbörse
description: Installieren und Verwenden der Proton Bitcoin Wallet
---
![cover](assets/cover.webp)

Proton ist ein Schweizer Unternehmen, das sich auf digitalen Datenschutz spezialisiert hat und 2014 von Wissenschaftlern des CERN gegründet wurde. Proton ist bekannt für seine Open-Source-Lösungen und bietet eine Reihe von Dienstleistungen an, darunter Proton Mail, Proton VPN und Proton Drive.

Proton hat vor kurzem Proton Wallet vorgestellt, eine Open-Source, selbstverwahrende Bitcoin-Wallet, die als mobile App oder Web-Client verfügbar ist und mit Ihrem Proton-Konto verbunden ist. Die Funktionalitäten der Wallet sind im Moment relativ klassisch, mit den wesentlichen Tools, die man von einer guten Bitcoin-Wallet erwartet, wie RBF (*Replace-By-Fee*), Tagging oder die Möglichkeit, eine BIP39 Passphrase hinzuzufügen.

Die Besonderheit dieser Wallet ist die Möglichkeit, Bitcoins mit der E-Mail-Adresse des Empfängers zu versenden, wofür Proton automatisch eine leere Bitcoin-Adresse generiert, die mit der Wallet des Nutzers verknüpft ist. Proton plant, in Zukunft neue Funktionen hinzuzufügen, darunter Lightning und Coinjoins (wahrscheinlich unter Verwendung von Whirlpool, wie die Aktivitäten auf ihrem GitHub-Repository nahelegen).

## Ein Proton-Konto erstellen

Um Proton Wallet nutzen zu können, benötigen Sie ein Proton-Konto. Sie können ein solches kostenlos erstellen, indem Sie die ersten Schritte dieses Tutorials zur Erstellung eines Proton-Postfachs befolgen (nur den Abschnitt "*Erstellung eines Proton-Kontos*"). Sobald Ihr Konto eingerichtet ist, können Sie mit dem Rest des Tutorials fortfahren.

https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2

## Verbindung zu Proton Wallet

Gehen Sie auf [die Proton Wallet Website] (https://proton.me/wallet) und klicken Sie auf die Schaltfläche "*Get Proton Wallet*".

![Image](assets/fr/01.webp)

Wählen Sie die Option "*Kostenlos*" und klicken Sie dann auf "*Anmelden*".

![Image](assets/fr/02.webp)

Geben Sie die E-Mail und das Passwort ein, die mit Ihrem Proton-Konto verbunden sind, um sich anzumelden.

![Image](assets/fr/03.webp)

Ihr Konto sollte nun angezeigt werden. Klicken Sie auf "*Jetzt mit Proton Wallet starten*".

![Image](assets/fr/04.webp)

## Eine Bitcoin-Brieftasche erstellen

Wählen Sie die Standardwährung für Ihr Konto und klicken Sie dann auf "*Neue Brieftasche erstellen*".

![Image](assets/fr/05.webp)

Ihre Bitcoin-Brieftasche ist nun erstellt worden. Theoretisch können Sie es sofort benutzen, aber es ist sehr wichtig, dass Sie zuerst Ihre Mnemonik sichern. Klicken Sie dazu auf "*Sichern Sie Ihre Wallet*" in der oberen rechten Ecke der Benutzeroberfläche.

![Image](assets/fr/06.webp)

Wenn Sie dies nicht bereits auf Proton getan haben, werden Sie aufgefordert, ein Backup für Ihr Konto einzurichten und es mit einer 2FA-Methode zu sichern. Diese Sicherheitsmaßnahmen gelten zwar für Ihr gesamtes Proton-Konto, sind aber umso wichtiger, wenn Ihre Bitcoin-Wallet darin integriert ist. Ich empfehle Ihnen dringend, sie zu implementieren.

![Image](assets/fr/07.webp)

Um Ihre Gedächtnisstütze zu speichern, klicken Sie auf "*Sicherung der Gedächtnisstütze für diese Brieftasche*".

![Image](assets/fr/08.webp)

Geben Sie Ihr Proton-Passwort ein.

![Image](assets/fr/09.webp)

Klicken Sie dann auf "*Wallet Seed Phrase* anzeigen", um die mnemonische Phrase Ihrer Brieftasche anzuzeigen.

![Image](assets/fr/10.webp)

Proton Wallet zeigt Ihre 12-Wort-Merkhilfe an. **Mit diesem Merksatz haben Sie vollen, uneingeschränkten Zugriff auf alle Ihre Bitcoins**. Jeder, der im Besitz dieser Phrase ist, kann Ihr Geld stehlen, auch ohne Zugang zu Ihrem Proton-Konto. Die 12-Wort-Phrase kann verwendet werden, um den Zugang zu Ihren Bitcoins wiederherzustellen, wenn Sie den Zugang zu Ihrem Konto verlieren. Es ist daher sehr wichtig, sie sorgfältig zu speichern und an einem sicheren Ort aufzubewahren.

Sie können ihn auf ein Stück Papier schreiben, oder für zusätzliche Sicherheit empfehle ich, ihn auf einen Edelstahlsockel zu gravieren, um ihn vor Feuer, Hochwasser oder Einsturz zu schützen.

![Image](assets/fr/11.webp)

Für weitere Informationen über die richtige Art und Weise, wie Sie Ihre mnemotechnische Phrase speichern und verwalten können, empfehle ich Ihnen, diese andere Anleitung zu lesen, insbesondere wenn Sie Anfänger sind:

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

natürlich sollten Sie diese Wörter niemals fotografieren, anders als ich es in diesem Tutorial tue.**_

Klicken Sie auf die Schaltfläche "*Erledigt*", sobald Sie Ihre Phrase gespeichert haben.

![Image](assets/fr/12.webp)

## Entdecken Sie die Schnittstelle

Die Oberfläche von Proton Wallet ist sehr intuitiv. Auf der linken Seite finden Sie Ihre verschiedenen Wallets und die dazugehörigen Konten. Das "*Primär*"-Konto ist Ihr Hauptkonto. Aus Gründen der Vertraulichkeit werden Bitcoins, die Sie über die Proton-E-Mail-Adresse erhalten, auf einem separaten Konto mit der Bezeichnung "*Bitcoin per E-Mail*" abgelegt.

![Image](assets/fr/13.webp)

Um ein neues Konto hinzuzufügen, klicken Sie auf "*Konto hinzufügen*".

![Image](assets/fr/14.webp)

Um ein neues Portfolio anzulegen, klicken Sie auf das Symbol "*+*" neben "*Geldbörsen*".

![Image](assets/fr/15.webp)

Hier können Sie eine BIP39-Passphrase zu einer neuen Brieftasche hinzufügen.

![Image](assets/fr/16.webp)

Um Ihr Wissen über die Passphrase zu vertiefen, empfehle ich Ihnen diesen Lehrgang:

https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

## Bitcoins erhalten

Um Bitcoins in Ihrem Wallet zu erhalten, wählen Sie das gewünschte Konto auf der linken Seite der Benutzeroberfläche aus und klicken dann auf die Schaltfläche "*Empfangen*".

![Image](assets/fr/17.webp)

Proton Wallet generiert dann automatisch eine neue, leere Adresse.

![Image](assets/fr/18.webp)

Sobald die Transaktion abgeschlossen ist, finden Sie sie in der Rubrik "*Transaktionen*". Klicken Sie auf "*+Hinzufügen*", um der Transaktion eine Bezeichnung zu geben.

![Image](assets/fr/19.webp)

## Bitcoins senden

Jetzt, wo Sie Bitcoins in Ihrer Brieftasche haben, können Sie sie verschicken. Wählen Sie das Konto Ihrer Wahl auf der linken Seite der Benutzeroberfläche aus und klicken Sie dann auf "*Senden*".

![Image](assets/fr/20.webp)

Geben Sie die Bitcoin-Adresse des Empfängers ein. Sie können einen QR-Code scannen, indem Sie auf das kleine Logo klicken. Um an eine E-Mail-Adresse zu senden, geben Sie diese direkt in dieses Feld ein. Sobald Sie die Bitcoin-Adresse eingegeben haben, klicken Sie auf den kleinen Pfeil und dann auf "*Bestätigen*".

![Image](assets/fr/21.webp)

Geben Sie den zu überweisenden Betrag ein, entweder in Fiat-Währung oder in Bitcoins, und klicken Sie dann auf "*Überprüfen*".

![Image](assets/fr/22.webp)

Wählen Sie die Transaktionsgebühr auf der Grundlage der aktuellen Marktsituation.

![Image](assets/fr/23.webp)

Fügen Sie Ihrer Transaktion ein Etikett hinzu und überprüfen Sie dann alle Details. Wenn alles korrekt ist, klicken Sie auf "*Bestätigen und senden*", um die Transaktion zu unterzeichnen und zu senden.

![Image](assets/fr/24.webp)

Ihre Transaktion wird nun in der Rubrik "*Transaktionen*" Ihres Kontos zur Bestätigung angezeigt.

![Image](assets/fr/25.webp)

## Anmeldung bei der Anwendung

Neben dem Web-Client ist die Proton Wallet auch über eine mobile Anwendung zugänglich. Wenn Sie die Wallet mit Ihrem Proton-Konto verknüpfen, können Sie Ihre Wallet zwischen dem Web-Client und der mobilen App synchronisieren.

Laden Sie Proton Wallet aus Ihrem Anwendungsspeicher herunter:


- [Im App Store] (https://apps.apple.com/us/app/proton-wallet-secure-btc/id6479609548);
- [Im Google Play Store](https://play.google.com/store/apps/details?id=me.proton.wallet.android).

![Image](assets/fr/26.webp)

Nach der Installation klicken Sie auf "*Anmelden*" und geben Ihre E-Mail-Adresse und Ihr Proton-Passwort ein.

![Image](assets/fr/27.webp)

Sie haben dann Zugriff auf Ihre Bitcoin-Brieftasche mit denselben Funktionen wie im Web-Client.

![Image](assets/fr/28.webp)

Herzlichen Glückwunsch, Sie wissen jetzt, wie Sie Proton Wallet einrichten und verwenden können. Wenn Sie diese Anleitung nützlich fanden, wäre ich Ihnen dankbar, wenn Sie unten einen grünen Daumen hinterlassen würden. Sie können diesen Artikel auch gerne in Ihren sozialen Netzwerken teilen. Vielen Dank fürs Teilen!

Um weiter zu gehen, empfehle ich dieses Tutorial über Jade Plus, die neueste Hardware-Wallet von Blockstream:

https://planb.network/tutorials/wallet/hardware/jade-plus-sparrow-938abf16-e10a-4618-860d-cd771373a262
