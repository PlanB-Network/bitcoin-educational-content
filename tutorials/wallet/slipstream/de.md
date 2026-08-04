---
name: Slipstream
description: Sending a signed transaction directly to a miner with Slipstream, without broadcasting it to the Bitcoin network
---

![cover](assets/cover.webp)

Normalerweise wird eine Transaktion, sobald du sie signierst, automatisch an jeden Bitcoin-Node im Netzwerk übertragen (Broadcast). Danach wartet sie darauf, gemined zu werden.

Solange sie sich jedoch nicht in einem Block befindet, könnte ein Angreifer, der deinen Private Key erlangt hat, sie ersetzen und die Gelder stehlen. Das ist typischerweise der Fall, wenn du eine ColdCard-Hardware-Wallet verwendest.

Das Slipstream-Tool des Mining-Unternehmens MARA erlaubt es dir, den Broadcast der Transaktion an das Netzwerk zu umgehen: Sie wird direkt (und ausschließlich) an einen Miner gesendet, was sie privat hält und eine Offenlegung im Netzwerk vermeidet. Die Transaktion wird wahrscheinlich länger brauchen, um gemined zu werden, ist dafür aber vor einem Replacement-Angriff geschützt.

Im Folgenden bieten wir ein Tutorial an, das es Nutzern von [Liana](https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04) sowie Nutzern der [Sparrow](https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d)-Wallet ermöglicht, das Slipstream-Tool des Miners MARA über die Seite [outofband.wizardsardine.com](https://outofband.wizardsardine.com/) zu nutzen.

⚠️ **Warnung**: Dieses Tool ist nur für bestimmte Profile gedacht, hauptsächlich Liana-Wallets, Miniscript-Wallets und einige Arten von Multisig. Wizardsardine **rät ausdrücklich davon ab**, es für Wallets zu verwenden, deren Gelder bereits akut diebstahlgefährdet sind – zum Beispiel solche, deren Recovery-Phrase auf einem ColdCard-Gerät generiert wurde, das von der Zufallszahlengenerator-Schwachstelle betroffen ist. In dieser Situation ist das Wettrennen gegen den Angreifer eine Sache von Sekunden, und eine an einen einzigen Miner gesendete Transaktion braucht weit länger zur Bestätigung als eine normal übertragene. Wenn dich das betrifft, lies zuerst unser dediziertes Tutorial:

https://planb.academy/tutorials/wallet/hardware/coldcard-seed-vulnerability-1348b153-89db-429c-80af-b5d3d8506b9a

## Für Liana-Nutzer

Liana wird von Wizardsardine gepflegt, dem Herausgeber der Seite [outofband.wizardsardine.com](https://outofband.wizardsardine.com/), daher ist der Weg direkt: Du exportierst einfach die signierte PSBT-Datei, statt sie zu broadcasten.

*Voraussetzung: Du hast Guthaben auf deiner Liana-Wallet.*

### Schritt 1: Erstelle deine Transaktion mit Liana

Baue wie gewohnt deine Transaktion auf, indem du die Zieladresse, die Beschreibung und den Betrag hinzufügst (hier den in der Wallet maximal verfügbaren Betrag).

Um die Gebührenrate festzulegen:

- wähle die Coins aus, die du ausgeben möchtest, indem du auf das kleine Kästchen unten links unter "Coins selection" klickst;
- gib dann die Gebührenrate ein. Denk daran, die Gebühren deutlich höher als die vorgeschlagene Rate einzustellen, wie auf dieser Seite beschrieben: [outofband.wizardsardine.com](https://outofband.wizardsardine.com/).

Klicke abschließend auf "Next".

![Building the transaction in Liana](assets/fr/01.webp)

### Schritt 2: Überprüfe die Details deiner Transaktion

Bevor du auf "Sign" klickst, überprüfe die Details deiner Transaktion; insbesondere:

- den gesendeten Betrag;
- die Anzahl der Satoshis, die für die Transaktionsgebühren vorgesehen sind;
- vor allem aber die Adresse, an die du die Gelder sendest (denk daran, die ersten 5/6 Zeichen, die letzten 5/6 sowie 5/6 Zeichen in der Mitte der Adresse zu überprüfen, um "Address-Poisoning"-Angriffe zu vermeiden).

![Checking the transaction details](assets/fr/02.webp)

### Schritt 3: Wähle die signierenden Wallets aus

Wähle als Nächstes die Software- und/oder Hardware-Wallets aus, mit denen du deine Transaktion signieren musst. Kurze Erinnerung: Bei einer 2-von-2-Multisig-Wallet benötigst du 2 von 2 Signaturen.

### Schritt 4: Exportiere die PSBT-Datei deiner Transaktion

Die Bitcoin-Transaktion ist nun mit den entsprechenden Keys signiert. Klicke nicht auf "Broadcast", andernfalls wird sie mit dem gesamten Netzwerk geteilt, und falls du eine ColdCard-Hardware-Wallet verwendest, wird deine Transaktion öffentlich sichtbar und deine Gelder sind gefährdet.

Du kannst nun auf "Export" klicken und die PSBT-Datei lokal auf deinem Computer speichern.

![Exporting the PSBT file from Liana](assets/fr/03.webp)

### Schritt 5: Sende die Transaktion über outofband.wizardsardine.com an den Miner

Nun zu den letzten Schritten. Um die Transaktion an den Miner zu senden, musst du nur die PSBT-Datei nehmen und per Drag-and-drop in den dafür vorgesehenen Bereich ziehen.

![Dropping the PSBT file on outofband.wizardsardine.com](assets/fr/04.webp)

Die Transaktion wird daraufhin wie unten gezeigt angezeigt.

![Transaction in the queue](assets/fr/05.webp)

### Schritt 6: Sende die Transaktion über Slipstream

Zum Schluss musst du nur noch auf "Send" klicken, damit die Transaktion über Slipstream an MARA gesendet wird.

![Sending the transaction via Slipstream](assets/fr/06.webp)

Innerhalb weniger Sekunden wechselt die Transaktion dann von "Sending" zu "Accepted":

![Transaction accepted by Slipstream](assets/fr/07.webp)

Jetzt musst du nur noch die Transaktions-ID (TXID) kopieren und sie in [mempool.space](https://mempool.space/) einfügen, um zu verfolgen, wie sie gemined wird:

![Looking up the TXID on mempool.space](assets/fr/08.webp)

Bitte beachte: Die Transaktion wird als "Transaction not found" angezeigt, bis der Miner MARA einen Block mined und deine Transaktion darin aufnimmt. Das kann mehrere Dutzend Minuten oder sogar Stunden dauern, da MARA nur etwa 4,5 % der Hashrate des Bitcoin-Netzwerks hält. Stand 4. August 2026 entspricht das ungefähr einem gemineten Block alle 3 Stunden und 45 Minuten.

## Für Nutzer anderer Wallets

Wenn du nicht [Liana](https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04) verwendest, aber das Tool dennoch nutzen möchtest, findest du hier ein Tutorial mit einer 2-von-2-Multisig-Wallet. Dazu verwenden wir die Software-Wallet [Sparrow](https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d).

*Voraussetzung: Du hast Guthaben auf deiner Sparrow-Wallet.*

### Schritt 1: Erstelle deine Transaktion

Erstelle mit [Sparrow](https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d) die Transaktion auf deiner Multisig-Wallet. Denk daran, die Gebühren deutlich höher als die vorgeschlagene Rate einzustellen, wie auf dieser Seite beschrieben: [outofband.wizardsardine.com](https://outofband.wizardsardine.com/).

Klicke nach dem Erstellen auf "Create Transaction".

![Creating the transaction in Sparrow](assets/fr/09.webp)

### Schritt 2: Finalisiere deine Transaktion

Um deine Transaktion zu finalisieren, musst du sie nun signieren. Klicke dazu auf "Finalize Transaction for Signing".

![Finalizing the transaction for signing](assets/fr/10.webp)

### Schritt 3: Signiere deine Transaktion mit deinen verschiedenen Keys

Nun kommt der Moment, die Transaktion zu signieren. Signiere sie dazu einfach mit der Software- oder Hardware-Wallet bzw. den Wallets, die du verwendest.

![Signing the transaction with the multisig keys](assets/fr/11.webp)

### Schritt 4: Lade die signierte Transaktion herunter und broadcaste sie nicht an das Netzwerk

Die Bitcoin-Transaktion ist nun mit beiden Keys unserer 2-von-2-Multisig signiert. Klicke nicht auf "Broadcast Transaction", andernfalls wird sie mit dem gesamten Netzwerk geteilt, und falls du eine ColdCard-Hardware-Wallet verwendest, wird deine Transaktion öffentlich sichtbar und deine Gelder sind gefährdet.

![Signed transaction, ready but not broadcast](assets/fr/12.webp)

### Schritt 5: Zeige das signierte Transaktions-Skript an oder lade die PSBT-Datei herunter

Um die signierte Bitcoin-Transaktion anzuzeigen, klicke jetzt auf "View Final Transaction". Du kannst dann das signierte Bitcoin-Transaktions-Skript kopieren:

*02000000000101ade28cc43b2f51e09c88a87dfaeda8a601a78cddb458e47d99f0651020c1aaa60000000000fdffffff010b370000000000002200201810640a195e5a992d1f6da58a9781f77db47ac63a332b072580cc5b57dd1c2e04004730440220320777c52799cc8015be7c3f724a3d77906ce3d551205c893347910279ed796a02204ee45912623c1c45bf3d93d6558d878737f88f20dcbd152dc28fac80e788f2aa01473044022008bf6ea8432e3fee0eaa7edb923f60e44bb5eb37e52a93d8fdb4e30814340b0f0220473f8fcfbadda9c86fdfc4d3dd55c7883f62312794361e4d4d93f52964bce6520147522102bd28ad9b52829baf62621821abb49339262c7ef32f8adf15bf01b4d91fb5a9a72103ace1a518996275cbf9ebdbeaa4703318a50d5ab7f0fe22b9e566d2f2f644ed3752ae9fa90e00*

![Displaying the signed transaction script](assets/fr/13.webp)

Wenn du die Transaktionsdatei herunterladen möchtest, kannst du entweder:

- auf "File" und dann auf "Save transaction…" klicken;
- oder auf die Netzwerkverbindungs-Schaltfläche unten rechts (gelbe Schaltfläche) und dann auf "Save Final Transaction" klicken.

Die Transaktion wird dann lokal auf deinem Computer gespeichert.

![Saving the final transaction locally](assets/fr/14.webp)

### Schritt 6: Sende die Transaktion über outofband.wizardsardine.com an den Miner

Nun zu den letzten Schritten. Um die Transaktion an den Miner zu senden, musst du nur:

- zu [outofband.wizardsardine.com](https://outofband.wizardsardine.com/) gehen;
- das im vorherigen Schritt kopierte signierte Transaktions-Skript einfügen und dann unten auf "ADD TO QUEUE" klicken;

![Pasting the transaction script into the tool](assets/fr/15.webp)

- oder die Datei nehmen und per Drag-and-drop in den dafür vorgesehenen Bereich ziehen.

![Dropping the transaction file on the tool](assets/fr/16.webp)

Die Transaktion wird daraufhin wie unten gezeigt angezeigt.

![Transaction in the queue](assets/fr/17.webp)

Wenn eine Meldung darauf hinweist, dass der gesamte Eingangsbetrag an Satoshis in deiner Transaktion unbekannt ist (und dass dadurch die Anzahl der Satoshis für die Gebühren nicht berechnet werden kann), musst du einfach den gesamten Eingangsbetrag an Satoshis manuell eingeben. Um ihn herauszufinden, klicke einfach auf die Anzeige deiner Transaktion in Sparrow, in der Mitte des Diagramms:

![Total input amount shown in Sparrow](assets/fr/18.webp)

Gib dann diesen Betrag (in unserem Beispiel 15.904 Sats) in das Tool [outofband.wizardsardine.com](https://outofband.wizardsardine.com/) ein:

![Manually entering the total input amount](assets/fr/19.webp)

Überprüfe zum Schluss, ob die Gebührenrate korrekt ist.

### Schritt 7: Sende die Transaktion über Slipstream

Zum Schluss musst du nur noch auf "Send" klicken, damit die Transaktion über Slipstream an MARA gesendet wird.

![Sending the transaction via Slipstream](assets/fr/20.webp)

Innerhalb weniger Sekunden wechselt die Transaktion dann von "Sending" zu "Accepted":

![Transaction accepted by Slipstream](assets/fr/21.webp)

Jetzt musst du nur noch die Transaktions-ID (TXID) kopieren und sie in [mempool.space](https://mempool.space/) einfügen, um zu verfolgen, wie sie gemined wird:

![Looking up the TXID on mempool.space](assets/fr/22.webp)

Bitte beachte: Die Transaktion wird als "Transaction not found" angezeigt, bis der Miner MARA einen Block mined und deine Transaktion darin aufnimmt. Das kann mehrere Dutzend Minuten oder sogar Stunden dauern, da MARA nur etwa 4,5 % der Hashrate des Bitcoin-Netzwerks hält. Stand 4. August 2026 entspricht das ungefähr einem gemineten Block alle 3 Stunden und 45 Minuten.
</content>
<parameter name="i">Write German translation of Slipstream tutorial