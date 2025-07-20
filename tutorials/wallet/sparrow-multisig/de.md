---
name: Sperling Wallet - Multisig
description: Erstellen Sie ein Portfolio mit mehreren Unterschriften auf Sparrow
---
![cover](assets/cover.webp)



Ein Multi-Signatur-Wallet (oft "*Multisig*" genannt) ist eine Bitcoin-Wallet-Struktur, die mehrere kryptografische Signaturen von verschiedenen Schlüsseln erfordert, um eine Ausgabe zu genehmigen. Im Gegensatz zu einem herkömmlichen ("*singlesig*") Wallet, bei dem ein einziger privater Schlüssel ausreicht, um einen UTXO zu entsperren, basiert der Multisig auf einem **m-von-n**-Modell: Von den _n_ Schlüsseln, die mit dem Wallet verbunden sind, müssen _m_ zwingend jede Transaktion mitsignieren.



Mit diesem Mechanismus kann die Kontrolle über ein Portfolio auf mehrere Stellen oder Geräte aufgeteilt werden. In einer 2-von-3-Konfiguration werden beispielsweise drei unabhängige Schlüsselsätze generiert, aber nur zwei werden zur Freigabe von Mitteln benötigt. Durch diese Architektur werden die Risiken im Zusammenhang mit der Kompromittierung oder dem Verlust eines Schlüssels drastisch reduziert: Ein Dieb, der nur Zugang zu einem Schlüssel hat, kann das Wallet nicht leeren, und ein Benutzer, der einen Schlüssel verliert, kann mit den verbleibenden zwei Schlüsseln immer noch auf sein Geld zugreifen.



![Image](assets/fr/01.webp)



Diese größere Sicherheit geht jedoch mit einer größeren Komplexität einher. Die Einrichtung eines Multisig Wallet erfordert die Sicherung mehrerer Mnemonic-Phrasen (eine pro Signaturfaktor) und erweiterter öffentlicher Schlüssel ("*xpub*"). Wenn Sie ein Multisig 2-of-3 Wallet verwenden, müssen Sie entweder alle drei Mnemonic-Sätze oder mindestens zwei der drei Sätze haben, um das Wallet abzurufen. Wenn Sie aber nur zwei der drei Phrasen haben, brauchen Sie auch Zugang zu den drei *xpubs*, ohne die es unmöglich ist, die öffentlichen Schlüssel abzurufen, die für den Zugriff auf die Bitcoins benötigt werden, die sie schützen.



Zusammenfassend lässt sich sagen, dass Sie ein Multisig-Portfolio wiederherstellen müssen, wenn Sie :




- Oder greifen Sie auf alle Mnemonic-Sätze zu, die mit jedem Signaturfaktor verbunden sind;
- Sie müssen entweder über die Mindestanzahl von Mnemonic-Sätzen verfügen, die der Schwellenwert erfordert, um signieren zu können, und außerdem Zugang zu den xpubs aller Faktoren haben, um die erforderlichen öffentlichen Schlüssel abrufen zu können.



![Image](assets/fr/02.webp)



Diese Verwaltung von Multisig-Portfolio-Backups wird durch *Output Script Descriptors* erleichtert, die alle für den Zugriff auf die Fonds erforderlichen öffentlichen Daten zusammenfassen. Diese Funktion ist jedoch noch nicht in allen Portfoliomanagement-Softwareprogrammen implementiert.



Multisig eignet sich besonders für Bitcoiner, die eine erhöhte Sicherheit oder eine kollektive Verwaltung von Geldern anstreben: Unternehmen, Verbände, Familien oder einzelne Nutzer, die eine beträchtliche Menge an Bitcoins besitzen. Es kann verwendet werden, um dezentralisierte Verwaltungssysteme zu schaffen, z. B. um die Unterschriftsberechtigung auf mehrere Manager oder Teammitglieder zu verteilen.



In diesem Tutorial werden wir lernen, wie man ein klassisches Multisignatur-Wallet mit **Sparrow Wallet** erstellt und verwendet. Wenn Sie ein individuelles Multisignatur-Portfolio mit Timelocks erstellen möchten, empfehle ich Ihnen, stattdessen Liana zu verwenden:



https://planb.network/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04

## Voraussetzungen



In diesem Tutorial zeige ich Ihnen, wie Sie einen Multisig mit der [Sparrow Wallet Portfolio Management Software] (https://sparrowwallet.com/download/) erstellen können. Wenn Sie diese Software noch nicht installiert haben, sollten Sie dies jetzt tun. Wenn Sie Hilfe benötigen, haben wir auch eine ausführliche Anleitung zur Konfiguration von Sparrow Wallet:



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d)

Um einen Wallet mit mehreren Unterschriften einzurichten, benötigen Sie verschiedene Hardware-Geldbörsen. Für einen Multisig 2-de-3 könnten Sie zum Beispiel :




- Ein Trezor Modell Eins;
- Ledger Flex;
- Eine Coldcard MK3.



![Image](assets/fr/03.webp)



Es ist eine gute Idee, verschiedene Marken von Hardware Wallet in Ihrer Multisig-Konfiguration zu verwenden. Dadurch wird sichergestellt, dass die Gesamtsicherheit Ihres Multisig nicht beeinträchtigt wird, wenn bei einem bestimmten Modell ein ernsthaftes Problem auftritt. Außerdem können Sie so von den spezifischen Vorteilen der einzelnen Geräte profitieren. Zum Beispiel in meiner Konfiguration:





- Das Trezor Model One ist vollständig quelloffen, so dass die seed-Generation überprüft werden kann. Da er jedoch nicht mit einem Secure Element ausgestattet ist, bleibt er anfällig für physische Angriffe;





- Der Ledger Flex hingegen profitiert von einer nicht verifizierbaren proprietären Firmware, verfügt aber über ein Secure Element, das einen hervorragenden physischen Schutz bietet;





- Die Coldcard ist mit einem Secure Element ausgestattet und ihr Code ist durchsuchbar. Sie ist eine interessante Wahl für unsere Konfiguration, da sie Verifikationsfunktionen bietet, die bei anderen Modellen nicht verfügbar sind.



Bevor Sie Ihr Multisig Wallet konfigurieren, stellen Sie sicher, dass jedes Hardware Wallet korrekt konfiguriert ist (Erstellung und Speicherung von Mnemonic, PIN-Definition). Detaillierte Anweisungen finden Sie in unseren Anleitungen für jedes Hardware Wallet, zum Beispiel :



https://planb.network/tutorials/wallet/hardware/trezor-model-one-5c250c49-ce3b-4c63-bd05-4600d7c11a02

https://planb.network/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a

https://planb.network/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3

Wie wir später in diesem Tutorial sehen werden, ist es auch möglich, in Ihre Multisig-Konfiguration einen Faktor zu integrieren, der nicht mit einem Hardware Wallet verbunden ist, dessen private Schlüssel aber auf Ihrem PC gespeichert sind. Diese Methode ist natürlich weniger sicher als die ausschließliche Verwendung von Hardware-Wallets, aber sie kann in bestimmten Fällen sinnvoll sein. Bei einem Multisig 2-de-3 könnten Sie sich zum Beispiel für zwei Hardware-Wallets und einen Software Wallet entscheiden.



## Erstellung eines Multisig-Portfolios



Öffnen Sie Sparrow Wallet, klicken Sie auf die Registerkarte "*Datei*" und wählen Sie dann "*Neuer Wallet*".



![Image](assets/fr/04.webp)



Vergeben Sie einen Namen für Ihr Portfolio mit mehreren Unterschriften und klicken Sie dann zur Bestätigung auf "*Wallet erstellen*".



![Image](assets/fr/05.webp)



Wählen Sie im Dropdown-Menü "*Policy Type*" die Option "*Multi Signature*".



![Image](assets/fr/06.webp)



In der oberen rechten Ecke können Sie nun die Gesamtzahl der Schlüssel in Ihrem Multisig sowie die Anzahl der Mitunterzeichner festlegen, die zur Genehmigung einer Ausgabe erforderlich sind. In meinem Beispiel ist dies ein 2-von-3-Schema.



![Image](assets/fr/07.webp)



Am unteren Rand des Fensters zeigt Sparrow Wallet drei "*Keystore*" an. Jeder steht für einen Satz von Schlüsseln. Hier verwende ich drei Hardware-Portfolios, so dass jeder "*Keystore*" einem von ihnen entspricht. Wir werden sie nun konfigurieren.



Ich beginne mit der Coldcard. Auf der Registerkarte "*Keystore 1*" wähle ich die Option "*Airgapped Hardware Wallet*".



![Image](assets/fr/08.webp)



Auf der Coldcard gehe ich nach dem Entsperren des Geräts in das Menü "*Einstellungen*" und dann auf "*Multisig Wallets*".



![Image](assets/fr/09.webp)



In diesem Menü können Sie die Multisig-Portfolios verwalten, an denen die Coldcard beteiligt ist. Ich möchte ein neues erstellen und wähle daher "*Export XPUB*".



![Image](assets/fr/10.webp)



Wenn Sie nur ein Konto verwalten, können Sie das Feld "*Kontonummer*" leer lassen und direkt durch Drücken der Bestätigungstaste bestätigen.



![Image](assets/fr/11.webp)



Die Coldcard wird dann generate eine Datei mit Ihrem xpub auf der Micro SD-Karte speichern.



![Image](assets/fr/12.webp)



Legen Sie diese Micro SD-Karte in Ihren Computer ein. Klicken Sie in Sparrow Wallet auf die Schaltfläche "*Datei importieren...*" neben "*Coldcard Multisig*" und wählen Sie dann die von der Coldcard auf der Karte erstellte Datei aus.



![Image](assets/fr/13.webp)



Ihre xpub wurde erfolgreich importiert. Wir wiederholen den Vorgang nun mit den beiden anderen Hardware-Geldbörsen.



![Image](assets/fr/14.webp)



Für das Ledger Flex wähle ich "*Keystore 2*" und klicke dann auf "*Verbundenes Hardware Wallet*". Stellen Sie sicher, dass das Ledger mit dem Computer verbunden und entsperrt ist und dass die Bitcoin-Anwendung geöffnet ist.



![Image](assets/fr/15.webp)



Klicken Sie dann auf die Schaltfläche "*Scan...*".



![Image](assets/fr/16.webp)



Klicken Sie neben dem Namen Ihres Hardwareportfolios auf "*Import Keystore*".



![Image](assets/fr/17.webp)



Der zweite Unterzeichner ist nun korrekt in Sparrow Wallet registriert.



![Image](assets/fr/18.webp)



Ich wiederhole genau den gleichen Vorgang mit dem Trezor One, um die Konfiguration des Multisig abzuschließen.



![Image](assets/fr/19.webp)



In meiner Konfiguration decken wir diesen Fall nicht ab, aber wenn Sie eine Unterschrift über einen Software Wallet in Sparrow (Hot Wallet) in Ihren Multisig einfügen möchten, klicken Sie einfach auf die Schaltfläche "*Neuer oder importierter Software Wallet*".



Nachdem Sie nun alle Ihre Signaturgeräte in Sparrow Wallet importiert haben, können Sie die Erstellung von Multisig abschließen, indem Sie auf "*Anwenden*" klicken.



![Image](assets/fr/20.webp)



Wählen Sie ein sicheres Passwort, um den Zugang zu Ihrem Sparrow Wallet Wallet zu schützen. Dieses Passwort schützt Ihre öffentlichen Schlüssel, Adressen, Etiketten und den Transaktionsverlauf vor unbefugtem Zugriff.



Denken Sie daran, dieses Passwort an einem sicheren Ort zu speichern, z. B. in einem Passwort-Manager, damit es nicht verloren geht.



![Image](assets/fr/21.webp)



## Sicherung eines Multisig-Portfolios



Wir werden nun unseren *Output Script Descriptor* auf der Coldcard speichern (dies gilt nur für Benutzer mit einer Coldcard in ihrem Multisig), und vor allem werden wir eine Sicherungskopie davon auf einem unabhängigen Medium aufbewahren.



Der *Deskriptor* enthält alle xpubs in Ihrem Multisig-Portfolio sowie die Ableitungspfade, die für die generate-Schlüssel verwendet wurden. Erinnern Sie sich an Teil 1: Um ein Multisig-Portfolio wiederherzustellen, müssen Sie entweder **alle** Mnemonic-Phrasen haben oder nur die Mindestanzahl, die erforderlich ist, um die Signaturschwelle zu erreichen. Im letzteren Fall ist es jedoch auch wichtig, **die xpubs** der fehlenden Unterzeichner zu haben. Der *Deskriptor* enthält alle xpubs Ihres Multisig.



Falls dies nicht klar ist, denken Sie einfach daran: Um einen Multisig abzurufen, benötigen Sie die Mindestanzahl von Mnemonic-Sätzen für jeden verwendeten Hardware Wallet, je nach Schwellenwert (in meinem Fall: 2 Sätze), sowie den *Descriptor*.



Dieser *Deskriptor* enthält keine privaten Schlüssel, sondern nur öffentliche Schlüssel. Das bedeutet, dass er keinen Zugang zu den Geldmitteln gewährt. Er ist daher nicht so kritisch wie Mnemonic-Sätze, die vollen Zugang zu Ihren Bitcoins geben. Das Risiko mit dem *Descriptor* bezieht sich ausschließlich auf die Vertraulichkeit: Im Falle einer Kompromittierung könnte eine dritte Partei alle Ihre Transaktionen beobachten, aber Ihre Gelder nicht ausgeben.



Ich empfehle Ihnen dringend, mehrere Kopien dieses *Deskriptors* zu erstellen und sie bei jedem Signiergerät auf Ihrem Multisig aufzubewahren. In meinem Fall drucke ich den *Descriptor* beispielsweise auf Papier aus und bewahre eine Kopie mit der Coldcard, eine weitere mit dem Trezor und eine mit dem Ledger auf. Außerdem speichere ich diesen *Descriptor* als PDF-Datei auf drei USB-Sticks, die jeweils mit einem der Hardware-Portfolios aufbewahrt werden. Auf diese Weise maximiere ich meine Chancen, diesen *Deskriptor* nie zu verlieren, und ich bin sicher, dass ich zwei Kopien (eine physische und eine digitale) bei jedem Gerät habe.



Sobald Ihr Multisig-Portfolio erstellt wurde, stellt Sparrow Ihnen automatisch diesen *Deskriptor* zur Verfügung. Klicken Sie auf die Schaltfläche "*PDF speichern...*", um ihn sowohl als Text als auch als QR-Code zu speichern.



![Image](assets/fr/22.webp)



Sie können diese PDF-Datei dann ausdrucken und auf Ihren USB-Stick kopieren.



![Image](assets/fr/23.webp)



Wir werden diesen *Deskriptor* auch in der Coldcard registrieren (falls Sie eine in Ihrer Konfiguration verwenden). Dadurch kann die Coldcard überprüfen, ob jede später signierte Transaktion dem ursprünglichen Wallet entspricht: korrekte xpubs, korrektes Address-Format, korrekter Ableitungspfad... Ohne diesen importierten *Deskriptor* kann Coldcard nicht bestätigen, dass Exchange-Adressen nicht gekapert oder PSBT nicht manipuliert wurden.



Das ist es, was die Coldcard in einem Multisig so interessant macht: Sie bietet zusätzliche Kontrollen gegen bestimmte ausgeklügelte Angriffe, die andere Hardware-Geldbörsen nicht zulassen (vorausgesetzt natürlich, dass Sie sie zum Signieren verwenden).



Rufen Sie in Sparrow das Menü "*Einstellungen*" auf, und klicken Sie dann auf "*Exportieren...*".



![Image](assets/fr/24.webp)



Klicken Sie neben der Option "*Coldcard Multisig*" auf "*Export File...*" und speichern Sie die Textdatei auf der Micro SD-Karte.



![Image](assets/fr/25.webp)



Legen Sie dann die Karte in die Coldcard ein. Gehen Sie zum Menü "*Einstellungen*", dann "*Multisig Brieftaschen*" und wählen Sie "*Import von SD*".



![Image](assets/fr/26.webp)



Wählen Sie die entsprechende Datei aus und bestätigen Sie den Import.



![Image](assets/fr/27.webp)



Klicken Sie auf den Namen Ihres neu importierten Multisig.



![Image](assets/fr/28.webp)



Überprüfen Sie die Konfigurationsparameter des Multisig und bestätigen Sie die Registrierung.



![Image](assets/fr/29.webp)



Ihr Multisig ist nun korrekt in Ihrer Coldcard gespeichert. Wenn Sie mehrere Coldcards in demselben Multisig haben, wiederholen Sie diesen Vorgang für jede einzelne.



Vergessen Sie nicht, neben dem *Deskriptor* vor allem die Mnemonic-Sätze für jede Ihrer Signaturgeräte zu speichern. Wenn Sie gerade erst anfangen, empfehle ich Ihnen dringend, dieses andere Tutorial zu lesen, um zu lernen, wie man sie richtig speichert und verwaltet:



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Bevor Sie Ihre ersten Bitcoins auf Ihrem Multisig empfangen, **empfehle ich Ihnen dringend, einen Test zur Wiederherstellung der leeren Geldbörse durchzuführen**. Notieren Sie sich einige Referenzinformationen, wie z. B. das erste empfangene Address, und setzen Sie dann Ihre Hardware-Wallets zurück, während das Wallet noch leer ist. Versuchen Sie dann, Ihre Multisig Wallet auf den Hardware-Geldbörsen mit Hilfe Ihrer Mnemonic Phrasen-Papier-Backups wiederherzustellen, dann auf Sparrow mit Hilfe des *Deskriptors*. Überprüfen Sie, ob der erste Address, der nach der Wiederherstellung erzeugt wird, mit dem übereinstimmt, den Sie ursprünglich aufgeschrieben haben. Wenn dies der Fall ist, können Sie sicher sein, dass Ihre Sicherungskopien zuverlässig sind.



Um mehr darüber zu erfahren, wie man einen Wiederherstellungstest durchführt, empfehle ich Ihnen, diesen anderen Lehrgang zu lesen:



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Empfangen Sie Bitcoins auf Ihrem Multisig



Ihr Wallet ist nun bereit, Bitcoins zu empfangen. Klicken Sie in Sparrow auf die Registerkarte "*Empfangen*".



![Image](assets/fr/30.webp)



Bevor Sie den von Sparrow Wallet generierten Address verwenden, nehmen Sie sich die Zeit, ihn direkt auf dem Bildschirm Ihrer Hardware-Geldbörsen zu überprüfen. Dadurch wird sichergestellt, dass der Address nicht verändert wurde und dass Ihre Geräte über die privaten Schlüssel verfügen, die zum Ausgeben der entsprechenden Mittel erforderlich sind. Auf diese Weise sind Sie gegen eine Reihe von Angriffsvektoren geschützt.



Klicken Sie dazu auf "*Address anzeigen*", um den Address auf Ihrem Trezor oder Ledger anzuzeigen, wenn dieser per Kabel angeschlossen ist.



![Image](assets/fr/31.webp)



Mit Coldcard kann diese Überprüfung ohne jegliche Interaktion mit Sparrow durchgeführt werden. Öffnen Sie einfach das Menü "*Address Explorer*" und wählen Sie dann ganz unten Ihren Multisig aus.



![Image](assets/fr/32.webp)



Sie sehen dann die vom Multisig generierten Empfangsadressen.



![Image](assets/fr/33.webp)



Prüfen Sie, ob die auf jedem Hardware Wallet angezeigte Address genau mit der in Sparrow Wallet übereinstimmt. Es ist ratsam, dies kurz vor der Weitergabe der Address an den Zahler zu tun, um sicher zu sein, dass sie vollständig ist.



Sie können diesem Address dann ein "*Label*" zuweisen, um die Herkunft der erhaltenen Bitcoins anzugeben. Dies ist eine gute Möglichkeit, die Verwaltung Ihrer UTXOs zu organisieren.



![Image](assets/fr/34.webp)



Sobald dies verifiziert wurde, können Sie den Address verwenden, um Bitcoins zu erhalten.



![Image](assets/fr/35.webp)



## Versenden von Bitcoins mit Ihrem Multisig



Jetzt, wo du deine ersten Satss auf deinem Multisig Wallet erhalten hast, kannst du sie auch ausgeben! Gehen Sie in Sparrow auf die Registerkarte "*Senden*", um eine neue Transaktion zu erstellen.



![Image](assets/fr/36.webp)



Wenn Sie die *Münzenkontrolle* verwenden möchten, d. h. die UTXOs, die Sie ausgeben möchten, manuell auswählen möchten, gehen Sie zur Registerkarte "*UTXOs*". Wählen Sie die UTXOs, die Sie ausgeben möchten, und klicken Sie dann auf "*Ausgewählte senden*". Sie werden automatisch zur Registerkarte "*Senden*" weitergeleitet, in der die UTXOs bereits vorausgefüllt sind.



![Image](assets/fr/37.webp)



Geben Sie den Ziel-Address ein. Mehrere Adressen können durch Klicken auf "*+ Hinzufügen*" hinzugefügt werden.



![Image](assets/fr/38.webp)



Fügen Sie ein "*Label*" hinzu, um den Zweck dieser Ausgabe zu beschreiben, damit Sie Ihre Transaktionen leichter verfolgen können.



![Image](assets/fr/39.webp)



Geben Sie den Betrag ein, der an das ausgewählte Address gesendet werden soll.



![Image](assets/fr/40.webp)



Passen Sie die Laderate an die aktuellen Netzbedingungen an. Schauen Sie zum Beispiel unter [Mempool.space] (https://Mempool.space/) nach, um eine geeignete Ladestufe auszuwählen.



Nachdem Sie alle Transaktionsparameter überprüft haben, klicken Sie auf "*Transaktion erstellen*".



![Image](assets/fr/41.webp)



Wenn Sie mit allem zufrieden sind, klicken Sie auf "*Transaktion zur Unterzeichnung abschließen*".



![Image](assets/fr/42.webp)



Am unteren Rand des Bildschirms sehen Sie, dass Sparrow auf 2 Unterschriften wartet. Das ist normal: Der hier verwendete Wallet ist ein Multisig 2-de-3.



![Image](assets/fr/43.webp)



Ich beginne die Unterzeichnung mit meiner Coldcard. Dazu stecke ich eine Micro-SD-Karte in den Computer und klicke dann auf "*Transaktion speichern*".



![Image](assets/fr/44.webp)



Es gibt 3 Möglichkeiten, die zu signierende Transaktion an Ihr Hardware Wallet zu übertragen und sie dann von Sparrow abzurufen. Die erste ist die Verwendung einer Micro-SD-Karte, wie wir es hier für die Coldcard tun werden. Die zweite Möglichkeit ist eine Kabelverbindung, die wir für die zweite Signatur (Ledger und Trezor) verwenden werden. Schließlich gibt es noch die Möglichkeit der QR-Code-Kommunikation für Geräte, die mit einer Kamera ausgestattet sind, wie die Coldcard Q, Jade Plus oder Passport V2.



Sobald der PSBT (*Partially Signed Bitcoin Transaction*) auf der Micro SD-Karte gespeichert ist, stecke ich sie in die Coldcard MK3 und wähle das Menü *Unterschriftsreif*.



![Image](assets/fr/45.webp)



Überprüfen Sie auf Ihrem Hardware Wallet-Bildschirm sorgfältig die Transaktionsparameter: den Address des Empfängers, den gesendeten Betrag und die Gebühren. Sobald die Transaktion bestätigt wurde, bestätigen Sie, um zur Unterschrift überzugehen.



![Image](assets/fr/46.webp)



Legen Sie dann die Micro SD-Karte zurück auf Ihren Computer und klicken Sie in Sparrow auf "*Transaktion laden*". Wählen Sie den von Coldcard signierten PSBT aus Ihren Dateien aus.



![Image](assets/fr/47.webp)



Sie können sehen, dass die Coldcard-Signatur hinzugefügt wurde. Ich werde nun ein zweites Gerät, in diesem Fall das Ledger, verwenden, um die zweite erforderliche Signatur durchzuführen. Ich schließe es an, entsperre es und klicke dann auf "*Sign*" auf Sparrow.



![Image](assets/fr/48.webp)



Klicken Sie auf "*Unterschreiben*" neben dem Namen Ihres Hardware Wallet.



![Image](assets/fr/49.webp)



Wenn Sie Ihren Ledger zum ersten Mal mit diesem Multisig verwenden, werden Sie von Sparrow aufgefordert, die erweiterten öffentlichen Schlüssel (xpubs) der Mitunterzeichner zu verifizieren. Wie bei der Coldcard verhindert dieser Schritt, dass Sie später blindlings unterschreiben. Um diese Informationen zu validieren, vergleichen Sie die auf dem Ledger-Bildschirm angezeigten xpub mit denen, die direkt von Ihren anderen Hardware-Geldbörsen bereitgestellt werden.



![Image](assets/fr/50.webp)



Überprüfen Sie den Address des Empfängers, den überwiesenen Betrag und die Transaktionsgebühr und unterschreiben Sie dann die Transaktion.



![Image](assets/fr/51.webp)



Drücken Sie auf den Bildschirm, um zu unterschreiben.



![Image](assets/fr/52.webp)



Sparrow hat nun die beiden Unterschriften, die zur Freigabe der Mittel aus dem Multisig-Portfolio erforderlich sind. Überprüfen Sie die Transaktion ein letztes Mal, und wenn alles in Ordnung ist, klicken Sie auf "*Transaktion senden*", um sie über das Netzwerk zu senden.



![Image](assets/fr/53.webp)



Sie finden diese Transaktion auf der Registerkarte "*Transaktionen*" des Sparrow Wallet.



![Image](assets/fr/54.webp)



Herzlichen Glückwunsch, Sie wissen jetzt, wie Sie einen Wallet mit mehreren Unterschriften auf Sparrow einrichten und verwenden können. Wenn Sie diese Anleitung nützlich fanden, wäre ich Ihnen dankbar, wenn Sie unten einen Green-Daumen hinterlassen würden. Sie können diesen Artikel auch gerne in Ihren sozialen Netzwerken teilen. Vielen Dank fürs Teilen!



Um noch weiter zu gehen, empfehle ich Ihnen, diese Anleitung über eine andere Methode zur Erhöhung der Sicherheit Ihres Bitcoin Wallet, das passphrase BIP39 , zu lesen:



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7