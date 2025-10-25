---
name: BIP-39 Passphrase Trezor
description: Wie kann ich einen passphrase zu meinem Trezor-Portfolio hinzufügen?
---
![cover](assets/cover.webp)



Ein passphrase BIP39 ist ein optionales Passwort, das in Kombination mit der Mnemonic Phrase ein zusätzliches Layer an Sicherheit für deterministische und hierarchische Bitcoin Portfolios bietet. In diesem Lernprogramm werden wir gemeinsam herausfinden, wie Sie ein passphrase auf Ihrem sicheren Bitcoin Wallet auf einem Trezor (Safe 3, Safe 5 und Model One) einrichten.



![Image](assets/fr/01.webp)



Bevor Sie mit diesem Tutorial beginnen, empfehle ich Ihnen, wenn Sie nicht mit dem passphrase-Konzept, seiner Funktionsweise und seinen Auswirkungen auf Ihren Bitcoin Wallet vertraut sind, diesen anderen theoretischen Artikel zu konsultieren, in dem ich alles erkläre (dies ist sehr wichtig, da die Verwendung eines passphrase ohne vollständiges Verständnis seiner Funktionsweise Ihre Bitcoins gefährden kann):



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

passphrase auf dem Trezor wird auf klassische Weise gehandhabt, wenn Sie sich bei der Konfiguration für den BIP39-Standard entschieden haben (was ich empfehle, wenn Sie kein *Multi-Share Backup* benötigen). Das Besondere am Trezor ist, dass man den passphrase entweder direkt am Hardware Wallet eingeben kann oder über die Tastatur des Computers mit Hilfe der Trezor Suite Software. Diese zweite Möglichkeit ist wesentlich unsicherer, da der Computer eine wesentlich größere Angriffsfläche bietet als der Hardware Wallet. Allerdings kann die Eingabe eines komplexen passphrase auf einer herkömmlichen Tastatur schneller sein als auf dem Hardware Wallet, was die Verwendung starker Passphrasen fördern könnte. Es ist also immer besser, einen passphrase zu verwenden, auch wenn er eingetippt werden muss, als gar keinen zu verwenden. Es ist jedoch wichtig, sich des erhöhten Risikos von numerischen Angriffen bewusst zu sein, das dies mit sich bringt.



Diese Optionen sind nicht bei jeder Trezor-kompatiblen Portfolioverwaltungssoftware verfügbar. Zum Beispiel kann passphrase für das Modell One über die Tastatur auf dem Sparrow Wallet eingegeben werden. Für die Modelle T, Safe 3 und Safe 5 müssen Sie entweder die Trezor Suite verwenden oder passphrase direkt auf Hardware Wallet eingeben, da die Option der Eingabe über Sparrow vor einigen Jahren von HWI deaktiviert wurde.



![Image](assets/fr/02.webp)



In der Trezor Suite haben Sie zwei verschiedene Möglichkeiten, den passphrase-Bedarf zu verwalten. Sie können die Option "*passphrase*" auf der Registerkarte "*Gerät*" aktivieren. Wenn diese Option aktiviert ist, werden die Trezor Suite und alle anderen Portfoliomanagementprogramme Sie bei jedem Start systematisch auffordern, Ihren passphrase einzugeben. Wenn Sie einen diskreteren Ansatz bei der Verwendung eines passphrase bevorzugen, können Sie die Einstellung auf "*Standard*" belassen. In diesem Fall müssen Sie manuell auf das Menü Ihres Hardware Wallet in der oberen linken Ecke zugreifen und bei jedem Start auf die Schaltfläche "*+ passphrase*" klicken.



Bevor Sie mit diesem Tutorial beginnen, vergewissern Sie sich bitte, dass Sie Ihren Trezor bereits initialisiert und Ihre Mnemonic Phrase erstellt haben. Wenn dies nicht der Fall ist und Ihr Trezor neu ist, folgen Sie dem modellspezifischen Lernprogramm auf Plan ₿ Network. Sobald Sie diesen Schritt abgeschlossen haben, können Sie zu diesem Lernprogramm zurückkehren.



https://planb.network/tutorials/wallet/hardware/trezor-safe-5-4413308a-a1b5-4ba4-bc49-72ae661cc4e0

https://planb.network/tutorials/wallet/hardware/trezor-safe-3-51d0d669-5d23-47c2-beb6-cc6fa0fb0ea0

https://planb.network/tutorials/wallet/hardware/trezor-model-one-5c250c49-ce3b-4c63-bd05-4600d7c11a02


## Hinzufügen eines passphrase zu einem Safe 3 oder Safe 5



Sobald Sie Ihr Wallet erstellt, Ihr Mnemonic gespeichert und eine PIN festgelegt haben, gelangen Sie zum Home-Menü der Trezor Suite. In der oberen linken Ecke sollte ein Fenster erscheinen, das Sie auffordert, das passphrase BIP39 zu aktivieren.



![Image](assets/fr/03.webp)



Wenn dieses Fenster nicht erscheint, müssen Sie die Option "*passphrase*" auf der Registerkarte "*Gerät*" manuell aktivieren.



![Image](assets/fr/04.webp)



In diesem Fenster werden Sie aufgefordert, Ihren passphrase einzugeben. Wählen Sie einen starken passphrase und machen Sie sofort eine physische Sicherung auf einem Medium wie Papier oder Metall. In diesem Beispiel habe ich den passphrase gewählt: `fH3&kL@9mP#2sD5qR!82`. Dies ist ein Beispiel; ich empfehle Ihnen jedoch, ein etwas längeres passphrase zu wählen. Zwischen 30 und 40 Zeichen wären ideal (wie ein gutes Passwort).



natürlich sollten Sie Ihren passphrase niemals im Internet weitergeben, wie ich es in diesem Lernprogramm tue. Dieses Beispiel Wallet wird nur auf Testnet verwendet und wird am Ende des Tutorials gelöscht.



Für weitere spezifische Empfehlungen zur Auswahl Ihres passphrase lade ich Sie erneut ein, diesen anderen Artikel zu lesen:



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Wenn Sie Ihren passphrase über die Tastatur Ihres Computers eingeben möchten, geben Sie ihn in das dafür vorgesehene Feld ein und klicken Sie dann auf "*Zugang passphrase Wallet*".



![Image](assets/fr/05.webp)



Ihr Hardware Wallet zeigt dann Ihr passphrase an. Vergewissern Sie sich, dass es mit Ihrer physischen Sicherung (Papier oder Metall) übereinstimmt, bevor Sie auf den Bildschirm klicken, um fortzufahren.



![Image](assets/fr/06.webp)



Dadurch erhalten Sie Zugang zu Ihrem passphrase-geschützten Portfolio.



![Image](assets/fr/07.webp)



Wenn Sie es vorziehen, die Sicherheit zu erhöhen, indem Sie Ihr passphrase nur auf Ihrem Trezor eingeben, klicken Sie auf "*passphrase auf Trezor eingeben*", wenn Sie dazu aufgefordert werden.



![Image](assets/fr/08.webp)



Auf Ihrem Trezor wird eine T9-Tastatur angezeigt, über die Sie Ihren passphrase eingeben können. Sobald Sie Ihre Eingabe abgeschlossen haben, klicken Sie auf das Häkchen Green, um das passphrase auf Ihr Wallet zu übertragen.



![Image](assets/fr/09.webp)



Sie werden dann Zugang zu Ihrem passphrase sicheren Wallet haben.



![Image](assets/fr/10.webp)



Für die Verwendung des Sparrow Wallet ist das Verfahren ähnlich, aber für die Modelle T, Safe 3 und Safe 5 muss passphrase am Hardware Wallet und nicht über die Computertastatur eingegeben werden.



Immer wenn Sparrow Wallet Zugriff auf Ihren Trezor benötigt und passphrase seit dem letzten Start noch nicht angewendet wurde, müssen Sie es über die T9-Tastatur eingeben.



![Image](assets/fr/11.webp)



## Hinzufügen eines passphrase zu einem Modell Eins



Beim Model One ist die Verwendung eines passphrase BIP39 fast unverzichtbar. Da dieses Gerät kein Secure Element enthält, ist es relativ einfach, sensible Informationen zu extrahieren. Es ist daher nicht resistent gegen physische Angriffe. Da das passphrase jedoch nicht auf dem Gerät verbleibt, nachdem es ausgeschaltet wurde, kann die Verwendung eines starken (nicht bruteable) passphrase Sie gegen die meisten bekannten physischen Angriffe auf dieses Modell schützen.



Beim Model One ist es nicht möglich, den passphrase direkt am Hardware Wallet einzugeben. Sie müssen ihn über die Tastatur Ihres Computers eingeben.



Sobald Sie Ihr Wallet erstellt, Ihr Mnemonic gespeichert und eine PIN festgelegt haben, gelangen Sie zum Home-Menü der Trezor Suite. In der oberen linken Ecke sollte ein Fenster erscheinen, das Sie auffordert, das passphrase BIP39 zu aktivieren.



![Image](assets/fr/12.webp)



Wenn dieses Fenster nicht erscheint, müssen Sie die Option "*passphrase*" auf der Registerkarte "*Gerät*" in den Einstellungen aktivieren.



![Image](assets/fr/13.webp)



In diesem Fenster werden Sie aufgefordert, Ihr passphrase einzugeben. Wählen Sie einen starken passphrase und machen Sie sofort eine physische Sicherung auf einem Medium wie Papier oder Metall. In diesem Beispiel habe ich den passphrase gewählt: "fH3&kL@9mP#2sD5qR!82". Dies ist nur ein Beispiel; ich empfehle jedoch, dass Sie einen etwas längeren passphrase wählen. Zwischen 30 und 40 Zeichen wären ideal (wie ein gutes Passwort).



Für weitere spezifische Empfehlungen zur Auswahl Ihres passphrase lade ich Sie erneut ein, diesen anderen Artikel zu lesen:



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Geben Sie Ihr passphrase in das vorgesehene Feld ein und klicken Sie dann auf die Schaltfläche "*Zugang passphrase Wallet*".



![Image](assets/fr/14.webp)



Ihr Hardware Wallet wird Ihr passphrase anzeigen. Vergewissern Sie sich, dass es mit Ihrer physischen Sicherung (Papier oder Metall) übereinstimmt, und klicken Sie dann auf die rechte Schaltfläche, um fortzufahren.



![Image](assets/fr/15.webp)



Dies führt Sie zu Ihrem passphrase-geschützten Portfolio.



![Image](assets/fr/16.webp)



Um das Sparrow Wallet danach zu verwenden, bleibt das Verfahren dasselbe. Jedes Mal, wenn Sparrow Zugriff auf Ihr Hardware Wallet benötigt und das passphrase seit dem letzten Einschalten des Geräts nicht eingegeben wurde, müssen Sie es eingeben.



![Image](assets/fr/17.webp)



Herzlichen Glückwunsch, Sie sind jetzt auf dem neuesten Stand, was die Verwendung des passphrase BIP39 auf Trezor-Hardware-Geldbörsen angeht. Wenn Sie die Sicherheit Ihres Wallet noch weiter erhöhen möchten, sollten Sie sich diese Anleitung zu Trezors *Multi-Share*-Backup-Systemen (*Shamir's Secret Sharing Scheme*) ansehen:



https://planb.network/tutorials/wallet/backup/trezor-shamir-backup-7f98b593-face-48fb-a643-0e811b87c94e

Wenn Sie diese Anleitung nützlich fanden, wäre ich Ihnen dankbar, wenn Sie unten einen Green-Daumen hinterlassen würden. Sie können diesen Artikel auch gerne in Ihren sozialen Netzwerken teilen. Ich danke Ihnen sehr!