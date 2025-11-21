---
name: BIP-39 Passphrase SeedSigner
description: Wie kann ich einen passphrase zu meinem SeedSigner-Portfolio hinzufügen?
---

![cover](assets/cover.webp)



Ein passphrase BIP39 ist ein optionales Passwort, das in Kombination mit der mnemonischen Phrase eine zusätzliche Sicherheitsebene für deterministische und hierarchische Bitcoin-Geldbörsen bietet. In diesem Tutorial werden wir gemeinsam herausfinden, wie Sie ein passphrase auf Ihrem Bitcoin wallet mit einem SeedSigner einrichten.



![Image](assets/fr/01.webp)



## Voraussetzungen für das Hinzufügen einer Passphrase



Bevor Sie mit diesem Tutorial beginnen, empfehle ich Ihnen, wenn Sie nicht mit dem passphrase-Konzept vertraut sind, wie es funktioniert und welche Auswirkungen es auf Ihren Bitcoin wallet hat, diesen anderen theoretischen Artikel zu lesen, in dem ich alles erkläre (dies ist sehr wichtig, da die Verwendung eines passphrase, ohne vollständig zu verstehen, wie es funktioniert, Ihre Bitcoins gefährden kann):



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Bevor Sie mit diesem Tutorial beginnen, stellen Sie bitte sicher, dass Sie Ihren SeedSigner bereits initialisiert und Ihre mnemonische Phrase generiert haben. Wenn Sie dies noch nicht getan haben und Ihr SeedSigner brandneu ist, folgen Sie dem Tutorial auf der Plan ₿ Academy. Sobald Sie diesen Schritt abgeschlossen haben, können Sie zu diesem Lernprogramm zurückkehren:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## Wie füge ich dem SeedSigner einen passphrase hinzu?



Wenn Sie ein passphrase zu Ihrem über SeedSigner verwalteten Portfolio hinzufügen, wird ein völlig neues Portfolio erstellt, das einen völlig separaten Satz von Schlüsseln erzeugt. Wenn Sie also bereits ein Portfolio mit Satss haben, können Sie mit dem passphrase nicht mehr darauf zugreifen, da es ein völlig anderes Portfolio erzeugt.



Um einen passphrase auf Ihren SeedSigner anzuwenden, schalten Sie das Gerät ein und scannen Ihren SeedQR wie gewohnt. Der SeedSigner zeigt dann den Fingerabdruck Ihres aktuellen wallet an, der demjenigen **ohne passphrase** entspricht. Der wallet mit passphrase wird einen anderen Fingerabdruck haben.



Klicken Sie auf die Schaltfläche `BIP-39 Passphrase`.



![Image](assets/fr/02.webp)



Geben Sie dann den passphrase Ihrer Wahl in das dafür vorgesehene Feld ein, indem Sie die Tastatur auf dem Bildschirm verwenden. Stellen Sie sicher, dass Sie eine oder mehrere physische Sicherungen (Papier oder Metall) machen: Der Verlust dieser passphrase führt zu einem dauerhaften Verlust des Zugangs zu Ihren Bitcoins. **Um einen wallet wiederherzustellen, sind sowohl die Eselsbrücke als auch der passphrase erforderlich ** Wenn einer von beiden verloren geht, werden Ihre Bitcoins unwiederbringlich gesperrt.



Sobald Sie Ihre Eingabe abgeschlossen haben, bestätigen Sie sie durch Drücken der Taste `KEY3` unten rechts auf dem SeedSigner.



![Image](assets/fr/03.webp)



*In diesem Beispiel habe ich den passphrase "pba" verwendet. In Ihrem Fall sollten Sie jedoch sicherstellen, dass Sie einen robusten passphrase wählen. Um herauszufinden, wie man einen optimalen passphrase definiert, lesen Sie bitte diesen anderen Artikel:*



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Der SeedSigner zeigt dann den neuen Fingerabdruck Ihres passphrase wallet an. Fertigen Sie mehrere Kopien dieses Fingerabdrucks an: Er ist wichtig, wenn Sie ein wallet mit einem passphrase verwenden, da Sie damit jedes Mal, wenn Sie das passphrase eingeben, überprüfen können, dass Sie sich nicht vertippt haben und dass Sie auf das richtige wallet zugreifen.



Wenn ich z. B. in meinem Fall beim Starten des SeedSigners fälschlicherweise passphrase "Pba" statt "pba" eintrage, führt diese einfache Änderung von Klein- zu Großbuchstaben dazu, dass ein völlig anderes Portfolio erstellt wird als das, auf das ich zugreifen möchte.



Dieser Fingerabdruck stellt kein Risiko für die Sicherheit oder Vertraulichkeit Ihres wallet dar. Er gibt keine Informationen, weder öffentliche noch private, über Ihre Schlüssel preis. Im Gegensatz zur Eselsbrücke und dem passphrase können Sie den Fingerabdruck also auf einem digitalen Medium speichern. Ich empfehle Ihnen, eine Kopie an verschiedenen Orten aufzubewahren: auf einem Blatt Papier, in einem Passwortmanager usw.



Sobald Sie Ihren Fingerabdruck gespeichert haben, klicken Sie auf "Fertig".



![Image](assets/fr/04.webp)



Sie haben dann Zugriff auf alle Funktionen Ihres Portfolios, genau wie bei einem klassischen SeedSigner.



![Image](assets/fr/05.webp)



Sie können nun den Schlüsselspeicher in Sparrow Wallet importieren und Ihren wallet wie gewohnt verwenden. Bei jedem Neustart müssen Sie sowohl Ihren SeedQR scannen als auch Ihren passphrase erneut über die Tastatur eingeben, wie wir es hier getan haben.



Bevor Sie Ihr wallet mit dem passphrase verwenden, empfehle ich Ihnen dringend, einen vollständigen Wiederherstellungstest durchzuführen. So können Sie sich vergewissern, dass Ihre Sicherungen der mnemonischen Phrase und des passphrase gültig sind. Wie Sie diese Prüfung durchführen können, erfahren Sie in der folgenden Anleitung:



https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895