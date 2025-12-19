---
name: COLDCARD - Co-Sign
description: Entdecken Sie die Co-Sign-Funktion und nutzen Sie sie auf Ihrer COLDCARD
---

![cover](assets/cover.webp)


*NB: Dieses Tutorial richtet sich an Personen, die bereits einige Erfahrung mit Multisignatur-Geldbörsen, Coinkite-Geräten und Software wie Sparrow wallet oder Nunchuk.* haben



![video](https://youtu.be/MjMPDUWWegw)




**Warum ColdCard Co-Sign?



Mit dieser Funktion können Sie Ihrem ColdCard-Gerät (Q oder Mk4) **Ausgabebedingungen** in der Art eines Hardware-Sicherheitsmoduls (HSM) hinzufügen, um Ihre Gelder zu schützen und gleichzeitig ein hohes Maß an Flexibilität und Kontrolle über sie zu behalten.



Ausgabenbedingungen können zum Beispiel sein:





- Betragsbegrenzungen**: Begrenzen Sie die Menge der Bitcoins, die Sie in einer einzigen Transaktion ausgeben können.
- Geschwindigkeitsbeschränkungen:** entscheiden, wie viele Transaktionen Sie pro Zeiteinheit (pro Stunde, Tag, Woche usw.) durchführen können, wobei eine Mindestanzahl von Blöcken zwischen den Transaktionen erforderlich ist.
- Vorab genehmigte Adressen:** Lassen Sie nur Bitcoins zu, die an vorab genehmigte Adressen gesendet werden.
- Zwei-Faktor-Authentifizierung:** Erfordert die Bestätigung durch eine mobile 2FA-Anwendung eines Drittanbieters (TOTP [RFC 6238](https://www.rfc-editor.org/rfc/rfc6238)) auf einem NFC-fähigen Smartphone/Tablet mit Internetzugang.



**Wie es funktioniert



Durch Hinzufügen eines zweiten seed zu Ihrem ColdCard Mk4- oder Q-Gerät, dem so genannten "Spending Policy Key", den wir in diesem Lernprogramm als "C Key" bezeichnen werden.


Zusätzlich zu diesem zusätzlichen seed werden Sie aufgefordert, Supply mindestens einen zusätzlichen Schlüssel (XPUB) zu erstellen, den wir als "Backup Key" bezeichnen, um einen Wallet Multisig 2-on-N zu erstellen.



Zusammenfassend lässt sich sagen, dass wir eine Wallet Multisig erstellen werden, und dass Ihr ColdCard-Gerät zwei der privaten Schlüssel enthält, die für die Ausgabe der Mittel erforderlich sind: den seed-Master des Geräts und den "Spending Policy Key".



Jedes Mal, wenn der "C-Schlüssel" zur Unterschrift aufgefordert wird, gelten die angegebenen Ausgabebedingungen, und die ColdCard unterschreibt nur, wenn die Transaktion diesen Bedingungen entspricht.



Wenn Sie auf diese Ausgabenbedingungen verzichten möchten, können Sie dies tun:




- indem Sie mit einer der Ersatztasten und der seed-Hand unterschreiben, oder mit 2 Ersatztasten, je nach Größe Ihres Multisig.
- durch Eingabe des "Ausgaberegelungsschlüssels" oder des "C-Schlüssels" im Menü "Mitunterzeichnung". **Letztere kann nicht direkt am Gerät abgefragt werden, da sonst jeder die konfigurierten Ausgabenbedingungen aufheben könnte




## ColdCard Co-Sign konfigurieren



![video](https://youtu.be/MjMPDUWWegw)



### 1- Aktivieren der Funktionalität



Stellen Sie zunächst sicher, dass Ihr Gerät mindestens die neueste Firmware-Version hat:




- Mk4: v5.4.2
- Q: v1.3.2Q




Gehen Sie auf Ihrer Mk4 oder ColdCardQ zu *Advanced Tools > ColdCard Co-Signing*.



![Co-Sign](assets/fr/01.webp)



*In der folgenden Anleitung werden die Screenshots der Einfachheit halber auf einer ColdCardQ gemacht, aber die Schritte und Menüs sind identisch zwischen der Mk4 und der Q.*



Es wird eine Zusammenfassung der Funktionen angezeigt.


Die Terminologie, die zur Bezeichnung der Schlüssel verwendet wird und die wir auch in dem 2-auf-3-Multisignatur-Wallet verwenden werden, das wir gleich erstellen werden, lautet:



Taste A = Coldcard Master seed


Taste B = Sicherungsschlüssel


Schlüssel C = Schlüssel für die Ausgabenpolitik



Klicken Sie auf **"ENTER "**.



![Co-Sign](assets/fr/02.webp)



Der nächste Schritt ist die Entscheidung, welcher private Schlüssel als "Spending Policy Key" oder "Key C" fungieren soll.



Wir sehen, dass uns mehrere Möglichkeiten offen stehen:





- Oder drücken Sie **"ENTER "**, um generate einen neuen seed-Satz mit 12 Wörtern zu erstellen.





- Klicken Sie entweder auf **"(1) "**, um eine bestehende seed mit 12 Wörtern zu importieren, oder wählen Sie **"(2) "**, um eine bestehende seed mit 24 Wörtern zu importieren.





- Oder drücken Sie **"(6) "**, um einen seed aus dem Tresor Ihres Geräts zu importieren.



Für die Zwecke dieses Tutorials haben wir uns entschieden, einen bestehenden seed mit 12 Wörtern zu importieren, indem wir **"(1) "** drücken. Dies kann ein beliebiges seed BIP39 sein, das Sie bereits besitzen und von dem Sie natürlich eine Sicherungskopie haben.



Geben Sie die 12 Wörter Ihres seed über die Tastatur ein. Für dieses Beispiel wählen wir die seed gültige Phrase beef x 12. Drücken Sie dann **"ENTER "**.


*NB: Wenn Sie keine Sicherungskopie dieses seed haben, können Sie die "Co-Sign"-Einstellungen auf Ihrem Gerät nicht mehr ändern, um Ihre Ausgabenbedingungen zu ändern*



Die Funktion "Mitunterzeichnen" ist nun auf dem Gerät aktiviert. Als Nächstes müssen wir unsere Ausgabenbedingungen auswählen und dann die Erstellung des Wallet mit mehreren Unterschriften abschließen.



![Co-Sign](assets/fr/03.webp)



### 2- Wählen Sie die Ausgabenbedingungen oder "*Ausgabenpolitik*"



Hier werden die Ausgabenbedingungen festgelegt, die erfüllt sein müssen, wenn der **"C-Schlüssel "** oder **"Schlüssel für Ausgabenpolitik**" eine Transaktion unterzeichnet.



Klicken Sie im Menü **"Mitunterzeichnung "** auf **"Ausgabenpolitik**".



Sie können dann den maximalen Betrag wählen, d.h. die maximale Anzahl von Satoshis, die in einer einzigen Transaktion ausgegeben werden können.



Für dieses Beispiel wählen wir eine maximale Magnitude von **21212** Satoshis. Klicken Sie zur Bestätigung auf **"ENTER "**.




![Co-Sign](assets/fr/04.webp)



Dann legen wir die maximale Geschwindigkeit fest, d. h. die Anzahl der Transaktionen, die das Gerät pro Zeiteinheit abschließen kann. Für dieses Tutorial wählen wir eine unbegrenzte Geschwindigkeit, d. h. keine Begrenzung der Anzahl der Transaktionen.




![Co-Sign](assets/fr/05.webp)



### 3- Erstellen Wallet Multisig 2-on-N



Wir müssen noch den dritten Schlüssel für unseren Wallet Multisig wählen, d. h. den **"Backup Key "** (Schlüssel B), zusätzlich zum **Master-seed** (Schlüssel A) des Geräts und dem **"Spending Policy Key "** (Schlüssel C).



Unser "B-Key" muss entweder über eine SD-Karte oder im Falle von ColdCardQ über einen QR-Code importiert werden.


Dazu benötigen wir ein zweites ColdCard Mk4- oder Q-Gerät, auf dem unser "Key B" verwendet wird.



Gehen Sie auf diesem zweiten Gerät, das Ihren **"Backup Key "** enthält, in diesem Beispiel eine ColdCard Mk4, vom Hauptmenü zu **"Einstellungen "**, dann zu **"Multisig Wallet"** und schließlich zu **"Export Xpub "**.


(Wenn Ihr zweites Gerät eine ColdCardQ ist, haben Sie natürlich die Möglichkeit, Ihr Xpub per QR-Code zu exportieren).





![Co-Sign](assets/fr/06.webp)





Legen Sie auf dem nächsten Bildschirm eine SD-Karte ein und klicken Sie unten rechts auf die Schaltfläche **"validieren "**. Klicken Sie dann auf **"(1) "**, um die Datei auf der SD-Karte zu speichern.



Die Datei enthält den Fingerabdruck des öffentlichen Schlüssels (*fingerprint*) in ihrem Namen und hat die Form `ccxp-0F056943.json`.




![Co-Sign](assets/fr/07.webp)



Stecken Sie dann die SD-Karte in die "ursprüngliche" ColdCardQ, um unseren "Backup Key" (Schlüssel B) zu importieren.


Wählen Sie im Menü "ColdCard Co-Signing" die Option "Build 2-of-N", und klicken Sie auf dem nächsten Bildschirm auf **"ENTER "** und dann erneut auf **"ENTER "**, um den "Backup Key" von der SD-Karte zu importieren.



![Co-Sign](assets/fr/08.webp)



Lassen Sie auf dem nächsten Bildschirm "Kontonummer" leer (es sei denn, Sie wissen genau, was Sie tun) und klicken Sie erneut auf **"ENTER "**.



![Co-Sign](assets/fr/09.webp)



Endlich sind wir bereit, unseren neuen Wallet Multisig 2-sur-3 einzusetzen, der wie folgt zusammengesetzt ist:



Taste A= Coldcard Q master seed


Schlüssel B= Backup-Schlüssel (gerade von einem zweiten Coldcard-Gerät importiert)


Schlüssel C= Schlüssel für die Ausgabenpolitik (wird zur Unterzeichnung verwendet und legt vordefinierte Ausgabenbedingungen fest)



## Mitunterzeichnen mit Sparrow wallet



Falls erforderlich, machen Sie sich anhand der nachstehenden Anleitungen mit der Sparrow wallet-Software vertraut:



https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

https://planb.academy/tutorials/wallet/desktop/sparrow-multisig-5860333b-6dd8-4aaa-8ab6-89ebc6276f1f

### 1- Ausfuhr Wallet Multisig 2-sur-3 bis Sparrow wallet



Wir müssen nun unseren Wallet Multisig nach Sparrow exportieren, damit wir dort unsere ersten Satoshis platzieren können.



Wählen Sie im Hauptmenü Ihrer ColdCardQ **"Einstellungen "**, dann **"Multisig Wallets "**.


Der Satz der Ihrer ColdCard bekannten Multisig-Geldbörsen wird nun angezeigt, wobei die Anzahl der beteiligten Schlüssel "2/3" (2-sur3) beträgt. Wählen Sie die soeben erstellte Multisig **"ColdCard Co-Sign "** und klicken Sie dann auf **"ColdCard Export "**.



![Co-Sign](assets/fr/10.webp)




Wählen Sie schließlich die Methode, mit der Sie den Wallet in den Sparrow exportieren können. In unserem Fall wählen wir die SD-Karte und klicken auf **"(1) "**, nachdem Sie eine SD-Karte in Slot A des Geräts eingelegt haben.



![Co-Sign](assets/fr/11.webp)



Wählen Sie dann in Sparrow wallet "Wallet importieren".



![Co-Sign](assets/fr/12.webp)



Klicken Sie dann auf **"Datei importieren "**. Wählen Sie dann die Datei **"export-Coldcard_Co-sign.txt "** auf Ihrer SD-Karte.



![Co-Sign](assets/fr/13.webp)



Geben Sie Ihrem Wallet einen Namen, wie er in Sparrow erscheinen wird, und wählen Sie ein Passwort, um Ihren Wallet zu verschlüsseln (oder auch nicht).



![Co-Sign](assets/fr/14.webp)



![Co-Sign](assets/fr/15.webp)



Wir sind nun bereit, unsere ersten Satoshis zu erhalten und die Ausgabenbedingungen zu testen, die wir für unseren Wallet festgelegt haben.



![Co-Sign](assets/fr/16.webp)



### 2- Prüfung der vordefinierten Ausgabenpolitik



Zur Erinnerung: Wir hatten uns für unseren Wallet Multisig für eine maximale Höhe von 21212 Satoshis entschieden. Das bedeutete, dass jedes Mal, wenn der Spending Policiy Key (Schlüssel C) eine Transaktion signierte, diese nur gültig war, wenn der ausgegebene Betrag kleiner oder gleich 21212 Satoshis war.



Testen wir es.


Klicken Sie zunächst auf die Registerkarte "Empfangen" in Sparrow und legen Sie ein paar Satss auf Wallet ab, die wir in diesem Lernprogramm verwenden werden.



![Co-Sign](assets/fr/17.webp)



![Co-Sign](assets/fr/18.webp)



Dann versuchen wir, mehr als die 21212 erlaubten Satoshis auszugeben, indem wir eine Transaktion von 50.000 Sats simulieren.



![Co-Sign](assets/fr/19.webp)



![Co-Sign](assets/fr/20.webp)



![Co-Sign](assets/fr/21.webp)



![Co-Sign](assets/fr/22.webp)



Nach dem Scannen des QR-Codes, der die *unsignierte* Transaktion mit unserer ColdCardQ repräsentiert, um die Transaktion zu importieren, wird uns Folgendes auf dem Bildschirm angezeigt. Eine Warnmeldung teilt uns mit, dass die Ausgabenbedingungen nicht erfüllt sind. Wenn wir die Transaktion trotzdem signieren, wird nur einer der beiden Schlüssel (der seed Master auf dem Gerät, aber nicht "Schlüssel C") signieren.




![Co-Sign](assets/fr/23.webp)



Hier, nach dem Import unserer Transaktion in Sparrow, sehen wir, dass nur eine der Signaturen auf die Transaktion angewendet wurde.



![Co-Sign](assets/fr/24.webp)




Wiederholen wir nun das Experiment, aber für eine Transaktion von 21.000 Satoshis, d.h. weniger als die maximale Größenordnung (21212 Sats), die wir für diesen Wallet festgelegt haben.




![Co-Sign](assets/fr/25.webp)



![Co-Sign](assets/fr/26.webp)



![Co-Sign](assets/fr/27.webp)



![Co-Sign](assets/fr/28.webp)



Lassen Sie uns versuchen, diese Transaktion mit unserer ColdCardQ zu unterschreiben.



Diesmal gibt es keine Probleme, es erscheint keine Warnmeldung, und wenn wir die signierte Transaktion in Sparrow wallet importieren, sind diesmal die beiden Signaturen angebracht worden, so dass die Transaktion gültig und bereit für die Verteilung ist.




![Co-Sign](assets/fr/29.webp)




![Co-Sign](assets/fr/30.webp)






## Mit dem Nunchuk mitzeichnen



https://planb.academy/tutorials/wallet/mobile/nunchuk-6cbcb406-ec84-478f-afac-bb4da366a6fa

### 1- Web 2FA und Adressen auf der Whitelist



In diesem Abschnitt werden wir unser Wallet Multisig Co-Sign mit Nunchuk verwenden und die Gelegenheit nutzen, neue Ausgabenbedingungen anzuwenden, um zu sehen, wie es läuft.



Gehen Sie zu *Erweiterte Tools > ColdCard Mitunterzeichnung*.


Wir werden aufgefordert, unseren "Ausgabenpolitik-Schlüssel" einzugeben, um auf das Menü zuzugreifen, das uns erlaubt, die Ausgabenbedingungen zu ändern. In unserem Fall geben wir 12 x "Rindfleisch" ein.



Wir haben uns aus praktischen Gründen, die mit diesem Tutorial zusammenhängen, für eine Größenordnung von 21212 Sats und eine maximale "Limit Velocity" entschieden. Auf der anderen Seite werden wir das Menü **"Whitelist-Adressen "** verwenden, um die Adressen festzulegen, für die unsere Mittel ausgegeben werden können.




![Co-Sign](assets/fr/31.webp)




Scannen Sie die QR-Codes der Adressen (wir wählen 2), die Sie zu Ihrer Whitelist hinzufügen möchten, und klicken Sie dann auf **"ENTER "**. Nachdem Sie Ihre Adressen durch wiederholtes Drücken von **"ENTER "** bestätigt haben, sehen Sie, dass die Beschränkungen für die Größenordnung und die Empfängeradressen angewendet wurden.



![Co-Sign](assets/fr/32.webp)



Um ein vollständiges Bild von den Möglichkeiten zu erhalten, die "Co-Sign" bietet, sollten wir die Option "Web 2FA" aktivieren.


Mit dieser Funktion können Sie eine TOTP RFC-6238-konforme Anwendung wie Google Authenticator / Ente Auth / Proton Authenticator / Authy 2FA / oder Aegis Authenticator verwenden, um einen zusätzlichen Layer an Sicherheit hinzuzufügen.



https://planb.academy/tutorials/computer-security/authentication/ente-auth-1928e65a-3b43-40f3-9efd-457ee2d79bb9

https://planb.academy/tutorials/computer-security/authentication/proton-authenticator-047ca2eb-a922-4e0e-8f75-1b89d23951ae

https://planb.academy/tutorials/computer-security/authentication/aegis-authenticator-22cc4d35-fb46-4e54-8833-bc4b411518bc

Konkret heißt das: Bevor Sie eine Transaktion unterschreiben, müssen Sie Ihr NFC-fähiges, internetfähiges Gerät in die Nähe Ihrer Coldcard bringen. Dadurch werden Sie automatisch auf eine Webseite von coldcard.com weitergeleitet, wo Sie aufgefordert werden, den 6-stelligen Code für Ihre Anwendung einzugeben. Wenn Sie den richtigen Code eingeben, zeigt Ihnen die Webseite entweder einen QR-Code, den Sie für die ColdCardQ scannen müssen, oder einen 8-stelligen Code, den Sie auf Ihrem Mk4 eingeben müssen, um Ihr Gerät zum Unterschreiben zu autorisieren.





![Co-Sign](assets/fr/33.webp)



Nach dem Scannen des QR-Codes, der in Ihrer Anwendung zur doppelten Authentifizierung angezeigt wird, und dem Hinzufügen Ihres ColdCard Co-Sign (CCC)-Kontos werden Sie aufgefordert, durch Eingabe Ihres 2FA-Codes zu bestätigen, dass alles in Ordnung ist.



Geben Sie Ihre ColdCard auf der Rückseite Ihres NFC-Geräts ein.



![Co-Sign](assets/fr/34.webp)



Geben Sie auf der sich öffnenden Webseite den 2FA-Code Ihrer bevorzugten Anwendung ein. Scannen Sie dann den mit Ihrer ColdCardQ angezeigten QR-Code (oder geben Sie den 8-stelligen Code ein, der in Ihrem Mk4 angezeigt wird).



![Co-Sign](assets/fr/35.webp)




Wir haben jetzt eine Begrenzung des Umfangs (21212 Sats), der Zieladressen und der doppelten Authentifizierung eingeführt.



![Co-Sign](assets/fr/36.webp)



### 2- Export Wallet Multisig 2-on-3 an Nunchuk



Lassen Sie uns diesmal Wallet Multisig 2-on-3 in Nunchuk exportieren, wie wir es zuvor mit Sparrow gemacht haben.


Gehen Sie zu *Einstellungen > Multisig Brieftaschen > 2/3: ColdCard Mitunterzeichnung > ColdCard Export*.



![Co-Sign](assets/fr/10.webp)



Wählen Sie dieses Mal die NFC-Option für den Export aus, indem Sie auf die gleichnamige Schaltfläche **"NFC "** auf der ColdcardQ klicken.



![Co-Sign](assets/fr/37.webp)



Wenn Sie die Anwendung zum ersten Mal öffnen, klicken Sie im Nunchuk auf **"Vorhandenen Wallet wiederherstellen "**.



![Co-Sign](assets/fr/38.webp)



Wenn Sie bereits einen Wallet in der Anwendung haben, klicken Sie auf das **"+"** oben rechts und dann auf **"Vorhandenen Wallet wiederherstellen "**.



![Co-Sign](assets/fr/39.webp)




Wählen Sie dann **"Wallet von COLDCARD wiederherstellen "** und dann **"Multisig Wallet"**.



![Co-Sign](assets/fr/40.webp)



Tippen Sie schließlich mit der Rückseite Ihres Smartphones auf den Bildschirm Ihrer ColdCardQ, um das Wallet über NFC zu importieren.



![Co-Sign](assets/fr/41.webp)



Unser Konto und die zuvor über Sparrow wallet eingezahlten Satoshis sind wieder da.



![Co-Sign](assets/fr/42.webp)



### 3- Prüfung der vordefinierten Ausgabenpolitik



Versuchen wir nun, eine Transaktion durchzuführen, die gegen die 2 festgelegten Ausgabenbedingungen verstößt. **Wir werden versuchen, mehr als 21212 Sats an einen Address auszugeben, der noch nicht genehmigt wurde.** Versuchen wir, 22 222 Sats an einen zufälligen Address zu senden.



![Co-Sign](assets/fr/43.webp)



Sobald die Transaktion erstellt wurde, klicken Sie auf die 3 kleinen Punkte in der oberen rechten Ecke, um sie in Ihre ColdCard zu exportieren.



![Co-Sign](assets/fr/44.webp)



Wählen Sie dann **"Export via BBQR "**, und scannen Sie den mit Ihrer ColdCardQ angezeigten QR-Code.



![Co-Sign](assets/fr/45.webp)



Ihre ColdcardQ zeigt dann eine Warnung an, die beim Scrollen zum unteren Rand des Bildschirms klarstellt, dass die Transaktion wie erwartet gegen die Ausgabenbedingungen verstößt.



**Beachten Sie, dass das Gerät nicht angibt, welche Ausgabenbedingungen gelten, um zu verhindern, dass ein potenzieller Angreifer versucht, die Beschränkungen zu umgehen




![Co-Sign](assets/fr/46.webp)



Wenn Sie trotzdem durch Drücken von **"ENTER "** bestätigen, erscheint der QR-Code, der die signierte Transaktion darstellt. Wenn Sie ihn auf dem Nunchuk importieren, können Sie sehen, dass nur eine Signatur angewendet wurde.



![Co-Sign](assets/fr/47.webp)



![Co-Sign](assets/fr/48.webp)






Führen wir genau die gleiche Operation durch, aber dieses Mal mit einer Transaktion, die die Größenbeschränkung (21212 Sats) beachtet und die Satoshis an eine der beiden vorkonfigurierten Adressen ausgibt.



Wir senden das Nunchuk 12121 Sats an eine unserer 2 Adressen. Dann exportieren wir die Transaktion in unsere ColdCard, wie zuvor geschehen.



![Co-Sign](assets/fr/49.webp)




Nachdem wir die unsignierte Transaktion in unsere ColdCardQ importiert haben, sehen wir uns an, was uns dieses Mal angezeigt wird.



Eine Warnung ist immer vorhanden, aber dieses Mal, wenn wir zum unteren Ende des Bildschirms scrollen, sehen wir, dass es darum geht, die Transaktion über 2FA zu validieren. Das Gerät fordert uns auf, unsere ColdcardQ in die Nähe unseres mit dem Internet verbundenen NFC-Terminals (Smartphone oder Tablet) zu bringen, was wir auch tun.



![Co-Sign](assets/fr/50.webp)



Auf unserem Smartphone öffnet sich eine Webseite, die uns auffordert, unseren 2FA-Code einzugeben, was wir dank Proton Authenticator auch tun.



![Co-Sign](assets/fr/51.webp)





Scannen Sie dann den QR-Code, der auf der Webseite erscheint, um Ihre ColdCard zur Unterzeichnung der Transaktion zu autorisieren.


Die Transaktion ist nun von den 2 Schlüsseln signiert und somit gültig.



Wenn "Push Tx" auf Ihrer ColdCardQ aktiviert ist, können Sie die Transaktion mit einem einfachen Tippen auf die Rückseite Ihres Smartphones direkt an das Netzwerk senden.



![Co-Sign](assets/fr/52.webp)




Wenn Sie "Push tx" nicht aktiviert haben, drücken Sie die "QR"-Taste auf Ihrer ColdCardQ, um die signierte Transaktion als QR-Code anzuzeigen, und importieren Sie sie auf dieselbe Weise wie im vorherigen Beispiel auf den Nunchuk.



![Co-Sign](assets/fr/53.webp)



Diesmal wurden 2 Signaturen angebracht, so dass die Transaktion bereit ist, im Bitcoin-Netz übertragen zu werden.



![Co-Sign](assets/fr/54.webp)




Wir sind am Ende dieses Tutorials angelangt, das Ihnen einen Überblick über die Möglichkeiten der Co-Sign-Funktionalität gibt, die in die ColdCardQ- und Mk4-Geräte von Coinkite integriert ist, sowie über ihre Verwendung durch Geldbörsen wie Sparrow und Nunchuk.