---
name: COLDCARD Q - Key Teleport
description: Was ist Key Teleport und wie verwende ich ihn?
---

![cover](assets/cover.webp)




![video](https://www.youtube.com/watch?v=Bg0r0DQVcDg)




![video](https://www.youtube.com/watch?v=BRpBiK-F8VU)



Was ist die Funktion **Schlüsselteleport**, die Coinkite mit seinem Vorzeigegerät ColdCardQ anbietet?



Mit **Key Teleport** können Sie vertrauliche Daten sicher zwischen 2 ColdCardQs übertragen. Der Übertragungskanal muss nicht einmal verschlüsselt sein, sondern kann öffentlich sein.



Dies kann zur Übertragung verwendet werden:





- **gW-0-Sätze** (ColdCard Qs seed-Master oder die in ColdCardQs [seed-Gewölbe](https://coldcard.com/docs/temporary-seeds/#seed-vault) gespeicherten Geheimnisse.
- **vertrauliche Notizen und Passwörter**: Dies kann ein beliebiges Geheimnis oder das gesamte Verzeichnis [Secure Notes & Passwords] (https://coldcard.com/docs/secure_notes/) auf Ihrer ColdCardQ sein.
- eine Sicherungskopie Ihrer gesamten **ColdCardQ**: die ColdCardQ, die diese Sicherungskopie erhält, darf keinen seed Master haben, damit dies funktioniert.
- gW-3 (**Teilsignierte Bitcoin-Transaktionen**) als Teil eines Multisignatursystems.



Dazu müssen Sie Ihre [Gerätefirmware auf Version v1.3.2Q](https://coldcard.com/docs/upgrade/) oder höher aktualisiert haben.



## Wie verwende ich Key Teleport?



### 1- Zur Übertragung von Daten jeder Art



Hier geht es um die Übertragung von seed-Sätzen, Notizen, Passwörtern oder eine komplette Übertragung einer ColdCardQ-Sicherung. Der Fall von PSBT-Übertragungen für Transaktionen mit mehreren Unterschriften wird später behandelt.



#### Das Gerät für den Empfang der Geheimnisse vorbereiten



Wählen Sie im Menü **"Erweitert / Werkzeuge**" auf Ihrer ColdCardQ die Option **"Tastenteleport (Start) "**.


Auf dem nächsten Bildschirm wird ein 8-stelliges Passwort vorgeschlagen, hier "20420219". Dieses Passwort müssen Sie dem Absender mitteilen. Verwenden Sie zum Beispiel eine SMS, um dieses Passwort zu senden, oder Ihr bevorzugtes sicheres Nachrichtensystem oder sogar einen Sprachanruf.



Klicken Sie dann auf die Schaltfläche **"Enter**" auf Ihrer ColdCardQ, um zum nächsten Schritt zu gelangen.




![CCQ-key-teleport](assets/fr/01.webp)




Auf dem Bildschirm wird ein QR-Code erzeugt. Auch hier müssen Sie diesen QR-Code dem ColdCardQ-"Absender" mitteilen. Am einfachsten geht das über einen Videoanruf.



**SENDEN SIE DIESEN QR-CODE NICHT ÜBER DENSELBEN ÜBERTRAGUNGSKANAL, ÜBER DEN SIE DAS VORHERIGE 8-STELLIGE PASSWORT GESENDET HABEN**.



![CCQ-key-teleport](assets/fr/02.webp)



*Für diejenigen unter Ihnen, die es interessiert, wollen wir versuchen, den zugrunde liegenden Mechanismus zu verstehen, der die Übertragung von Geheimnissen über ungesicherte Kanäle ermöglicht*



*Was wir hier tun, ist die Übertragung von Geheimnissen mit Hilfe der Diffie-Hellman-Methode, die im BTC204-Kurs behandelt wird, den ich unten aufgeführt habe*



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

*Wir haben derzeit:*




- ein ephemeres Schlüsselpaar (öffentlich/privat bzw. Ka und ka mit Ka=G.ka, wobei G der ECDH-Generatorpunkt ist) und ein 8-stelliges Passwort erzeugt.
- verschlüsselte mit diesem Passwort den öffentlichen Schlüssel (Ka) mittels AES-256-CTR und übermittelte dieses Passwort über einen Kommunikationskanal A an die "sendende" ColdCardQ.
- schließlich übermittelten wir das verschlüsselte Paket über den oben genannten QR-Code an den Absender, wobei wir einen zweiten Kommunikationskanal B verwendeten, der sich vom ersten unterschied.



#### Bereiten Sie das Gerät vor, das die Geheimnisse senden soll



Klicken Sie auf dem sendenden Gerät auf die Schaltfläche **"QR "**, um den QR-Code zu scannen, den Sie vom empfangenden Gerät erhalten haben, und geben Sie dann über einen separaten Kanal das 8-stellige Passwort ein, das Ihnen im vorherigen Schritt mitgeteilt wurde. Jetzt können wir mit dem Senden von Daten vom "sendenden" Gerät beginnen.



**Bitte geben Sie das 8-stellige Passwort nicht falsch ein, da sonst keine Fehlermeldung angezeigt wird und der Vorgang fortgesetzt wird. Die endgültige Datenübertragung schlägt jedoch fehl und Sie müssen erneut beginnen**.



![CCQ-key-teleport](assets/fr/03.webp)



*Für die Neugierigen unter Ihnen: Schauen wir uns noch einmal an, was wir im Bereich der Kryptographie und der Übertragung von Geheimnissen vorhaben:*




- haben wir die verschlüsselten Daten durch Scannen des QR-Codes auf dem Empfangsgerät importiert.
- dann entschlüsselten wir sie mit dem 8-stelligen Passwort, das uns über einen zweiten Kanal übermittelt wurde.
- wir sind also im Besitz des öffentlichen Schlüssels (Ka), den der Empfänger ursprünglich generiert hat.
- Anschließend erzeugen wir auf dem sendenden Gerät generate ein neues ephemeres Schlüsselpaar (Kb/kb, mit Kb=G.kb), das wir zur Anwendung von ECDH auf Ka verwenden. Wir führen also die Operation kb.Ka=Ks durch, wobei Ks als **"Sitzungsschlüssel "** bezeichnet wird




Sie werden nun aufgefordert, die Art der Geheimnisse auszuwählen, die zwischen den beiden ColdCardQs übertragen werden sollen (vertrauliche Notizen, Kennwort, vollständige Sicherung, Seeds in Ihrem Tresor, seed-Gerätestamm).



![CCQ-key-teleport](assets/fr/04.webp)



Hier wird unser Geheimnis eine kurze Nachricht sein, indem Sie **"Quick Text Message "** wählen. Geben Sie Ihre Nachricht ein (in unserem Fall "PlanB Network rocks") und drücken Sie **"ENTER "**.


Das Gerät generiert dann ein neues Zufallspasswort mit der Bezeichnung **"Teleport-Passwort "**, im Beispiel "NE XG BT SK".



![CCQ-key-teleport](assets/fr/05.webp)



Drücken Sie **"ENTER "** und es wird ein neuer QR-Code angezeigt. Lassen Sie ihn von dem empfangenden Gerät scannen. Und übermitteln Sie auf einem anderen Kommunikationskanal das **"Teleport-Passwort "** an den Empfänger.



![CCQ-key-teleport](assets/fr/06.webp)



*Hier noch einmal für Neugierige, während dieser Phase:*




- nach der Auswahl der zu übertragenden Geheimnisse wird mit generate ein neues Zufallspasswort mit der Bezeichnung **"Teleport Password"** erstellt.
- dann verschlüsseln wir die Geheimnisse mittels AES-256-CTR unter Verwendung des **"Sitzungsschlüssels "**, "Ks", der im vorherigen Schritt erzeugt wurde
- wir stellen dem bereits mit dem **"Sitzungsschlüssel "** verschlüsselten Paket unseren öffentlichen Kb-Schlüssel voran und fügen dann einen weiteren Layer der AES-256-CTR-Verschlüsselung mit dem **"Teleport-Passwort "** hinzu. Das Ganze wird dann als QR-Code verschlüsselt




#### Abschluss der Übertragung von Geheimnissen an das empfangende Gerät



Drücken Sie die Taste **"QR "**, um den QR-Code zu scannen, den das Sendegerät über den Visio-Kanal präsentiert. Sie werden aufgefordert, Ihr **"Teleport-Passwort "** für uns "NE XG BT SK" einzugeben.



![CCQ-key-teleport](assets/fr/07.webp)





Die Daten werden dann entschlüsselt und für das empfangende Gerät verständlich gemacht. Die empfangene Nachricht lautet tatsächlich "PlanB Network rocks". Das ist alles.



![CCQ-key-teleport](assets/fr/08.webp)



*Was geschah eigentlich in dieser letzten Phase :*?




- wir haben die vom Absender übermittelten Daten mit dem **"Teleport-Passwort "** entschlüsselt
- wir haben also den öffentlichen Schlüssel Kb und unsere geheime Nachricht, die mit dem **"Sitzungsschlüssel "**, "Ks", verschlüsselt ist. Aber wie können wir dies tun, da wir als Empfänger den vom Absender erstellten Schlüssel Ks nicht kennen?
- Wir müssen unseren privaten Schlüssel "ka" aus dem ersten Schritt **"Bereiten Sie das Gerät vor, das die Daten empfangen wird "** auf den öffentlichen Schlüssel Kb anwenden
- Indem man ka.Kb = ka.kb.G=kb.ka.G=kb.Ka=Ks berechnet, erhält man Ks. Diese wird schließlich zur Entschlüsselung der geheimen Nachricht verwendet.



### 2- Übertragung von PSBT auf Multisig (fortgeschritten)



Dies setzt voraus, dass Ihr Wallet Multisig bereits erstellt wurde und dass Ihr ColdCardQ-Gerät bereits so voreingestellt ist, dass es Transaktionen mit mehreren Unterschriften durchführen kann. Sollte dies nicht der Fall sein, finden Sie Erläuterungen [hier](https://coldcard.com/docs/Multisig/) auf der Coinkite-Website.



Eine kurze Erinnerung daran, was eine Multi-Signatur Wallet (Multisig) ist.



Um Ihre Wallet-Gelder auszugeben, benötigen Sie normalerweise nur einen privaten Schlüssel, um die mit Ihren Adressen verbundenen UTXOs zu entsperren.


Im Falle eines Wallet Multisig können bis zu 15 private Schlüssel und somit 15 Unterschriften erforderlich sein, um die Mittel auszugeben. Dies wird als "M aus N"-Portfolio bezeichnet, wobei N zwischen 1 und 15 und M die Anzahl der Unterschriften ist, die erforderlich sind, damit die Mittel ausgegeben werden können. Für ein Wallet Multisig 3 von 5 sind beispielsweise mindestens 3 von 5 möglichen Unterschriften erforderlich.



Die Herausforderung besteht dann darin, sich zwischen den Unterzeichnern abzustimmen, um ein "PSBT" für "Partially Signed Bitcoin Transaction" zu unterzeichnen. In diesem Zusammenhang kann "**Key Teleport**" verwendet werden, um die PSBT zwischen den Mitunterzeichnern auf einfache und vertrauliche Weise zu übertragen. Ein einfacher Videoanruf zwischen den Mitunterzeichnern reicht aus.



So wird es bei einem Multisig 3 von 4 gemacht.



**Unterzeichner 1:**



Unterzeichner 1 importiert und unterzeichnet den PSBT. Schließlich klickt er auf **"T "**, um mit **"Key Teleport "** den PSBT an Unterzeichner 2 zu übermitteln.



![CCQ-key-teleport](assets/fr/09.webp)




Nach Auswahl des Unterzeichners 2 durch Anklicken von **"ENTER "** wird ein "TELEPORT PASSWORD" (hier JJ YC AB 6A) bereitgestellt, das dem Unterzeichner 2 über einen anderen Kommunikationskanal übermittelt werden muss. Zum Beispiel eine SMS oder ein Sprachanruf, aber **nicht** ein Videoanruf.



Drücken Sie erneut **"ENTER "** und es erscheint ein QR-Code, der den PSBT darstellt, der mit 1 unterzeichnet und dann mit dem "TELEPORT PASSWORD" verschlüsselt ist.



![CCQ-key-teleport](assets/fr/10.webp)



**Unterzeichner 2:**



Unterzeichner 2 scannt den QR-Code, der ihm von Unterzeichner 1 vorgelegt wird. Anschließend gibt er das über den sekundären Kommunikationskanal übermittelte "TELEPORT PASSWORT" ein, um die übermittelten Daten zu entschlüsseln.



Unterzeichner 2 unterzeichnet die Transaktion und klickt dann auf **"T "**, um den PSBT über "Key Teleport" an Unterzeichner 3 zu übermitteln.


Offensichtlich sind bereits 2 Unterschriften geleistet worden. Es fehlt nur noch die des Unterzeichners 3, damit die Transaktion gültig ist. Wählen Sie Unterzeichner 3 aus, indem Sie auf **"ENTER "** klicken.



![CCQ-key-teleport](assets/fr/11.webp)



Und es wird ein neues "TELEPORT PASSWORD" erstellt, gefolgt von einem QR-Code, der den PSBT verschlüsselt, der von 1 und 2 unterzeichnet und dann mit diesem neuen "TELEPORT PASSWORD" verschlüsselt wird (GW YQ K3 LL).



![CCQ-key-teleport](assets/fr/12.webp)



**Unterzeichner 3:**



Wiederholen Sie denselben Schritt wie oben.


Der Unterzeichner 3 scannt den QR-Code, der ihm vom Unterzeichner 2 vorgelegt wird. Dann gibt er das über den sekundären Kommunikationskanal übermittelte "TELEPORT PASSWORT" ein.



Unterzeichner 3 unterschreibt die Transaktion, und da dieses Mal 3 von 4 Unterschriften geleistet wurden, wird die Transaktion als abgeschlossen angezeigt und kann über verschiedene Medien (SD-Karte, NFC, QR usw.) verteilt werden.



![CCQ-key-teleport](assets/fr/13.webp)



Wenn die "Push Tx"-Funktion Ihrer ColdCardQ aktiviert ist, befestigen Sie Ihre ColdCardQ einfach auf der Rückseite eines beliebigen NFC-fähigen, mit dem Internet verbundenen Geräts (Smartphone/Tablet), um die Transaktion über das Bitcoin-Netz zu übertragen.



![CCQ-key-teleport](assets/fr/14.webp)



*Für PSBT-Übertragungen von einem Unterzeichner zum anderen wird "Key Teleport" einfach über ein "Teleport-Passwort" in jeder Phase verwendet, das den PSBT verschlüsselt, während er von einem Unterzeichner zum anderen übertragen wird. Da die übertragenen Daten nicht zum Diebstahl von Geldern verwendet werden können, ist kein Diffie-Hellman-Verfahren erforderlich, wie es bei der Übermittlung streng vertraulicher Geheimnisse (seed, Passwort usw.)* der Fall ist.



![CCQ-key-teleport](assets/fr/15.webp)



*Quelle: [ColdCard offizielle Website](https://coldcard.com/)*