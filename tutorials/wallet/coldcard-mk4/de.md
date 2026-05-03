---
name: COLDCARD Mk4
description: Eine Anleitung zur Einrichtung und Verwendung eines COLDCARD Mk4 mit Sparrow Wallet
---

![cover-mk4](assets/cover.webp)


**Hardware-wallet** sind physische Geräte, die speziell für die sichere Speicherung des privaten Schlüssels von Bitcoin entwickelt wurden. Sie speichern die privaten Schlüssel offline, was bedeutet, dass Hacker sie nicht über das Internet erreichen können. Während **Software-wallet** hauptsächlich für alltägliche Transaktionen verwendet werden, werden **Hardware-wallet** oft dazu verwendet, größere Mengen an Bitcoins sicher und über einen langen Zeitraum zu speichern. Wenn eine Bitcoin-Transaktion mit **Hardware-wallet** durchgeführt wird, kann der wallet die Transaktionen innerhalb des Geräts signieren, so dass der private Schlüssel niemals einer mit dem Internet verbundenen Umgebung ausgesetzt ist.


In diesem Tutorial werden wir einen der beliebtesten Hardware-wallet von Coinkite, den Coldcard Mk4, untersuchen. Wir werden uns ansehen, wie man diesen Hardware-wallet einrichtet und verwendet, um Bitcoin-Transaktionen durchzuführen.


## Coldcard Mk4 Übersicht


Coldcard Mk4 ist eine Bitcoin-only Hardware wallet hergestellt von Coinkite. Dieses Gerät ist mit einem Bildschirm, einer numerischen Tastatur und einer schützenden Schiebeabdeckung ausgestattet. Darüber hinaus bietet das Gerät mehrere Verbindungs- und Interaktionsmöglichkeiten, darunter USB-C, Air-Gapped-Betrieb mit einer MicroSD-Karte, NFC und einen virtuellen Festplattenmodus. Das Mk4 umfasst auch erweiterte Sicherheitsfunktionen wie das BIP39 passphrase und Trick-PINs, die den Nutzern mehr Kontrolle und Schutz über ihr Bitcoin bieten.


## Ersteinrichtung: PIN und Anti-Phishing-Wörter


Die Coldcard Mk4 kann direkt auf der [Coinkite-Website] (https://store.coinkite.com/store) erworben werden, um loszulegen. Die Käufer können auch mit Fiat-Währung oder Bitcoin bezahlen. Darüber hinaus benötigen Sie eine MicroSD-Karte (4 GB ist ausreichend) und eine Stromquelle, die über ein USB-C-Kabel angeschlossen werden kann (die Coldcard Mk4 hat nur einen USB-C-Stromanschluss). Beachten Sie, dass der Mk4 keinen eingebauten Akku hat und daher während der Nutzung immer an die Stromquelle angeschlossen sein muss.


Sie erhalten Ihr Mk4 in einer manipulationssicheren Tasche. Bitte stellen Sie sicher, dass die Tasche nicht beschädigt wurde. Wenn Sie etwas entdecken, das ein Problem darstellen könnte, wie z. B. eine Beschädigung oder einen Riss in der Tasche, können Sie Coinkite darüber informieren, indem Sie eine E-Mail an support@coinkite.com senden. Außerdem finden Sie auf dem manipulationssicheren Beutel eine 12-stellige Nummer, die wir als die Beutelnummer des Mk4 bezeichnen werden. Diese Tütennummer wird später verwendet, um zu überprüfen, dass das Gerät während des Versands nicht manipuliert wurde und direkt von Coinkite stammt. Die Taschennummer wird sicher im secure element der Cold-Karte in einem OTP-Flash-Speicher (One-Time-Programmable) gespeichert, was bedeutet, dass sie nach der Programmierung nicht mehr geändert werden kann. Wenn Sie das Gerät zum ersten Mal einschalten, muss die auf dem Bildschirm angezeigte Nummer mit der Nummer auf der Tasche übereinstimmen. Dadurch wird sichergestellt, dass das Mk4, das Sie erhalten haben, das Originalgerät aus dem Werk ist und nicht ausgetauscht oder verändert wurde. Während diese Überprüfung nur die Integrität des Geräts zum Zeitpunkt des ersten Einschaltens bestätigt, schützt das secure element weiterhin Ihre privaten Schlüssel, Ihre PIN und Ihr passphrase, was es extrem schwierig macht, Ihr Bitcoin durch Manipulationen zu gefährden. Darüber hinaus tragen gute Praktiken, wie die ordnungsgemäße Sicherung Ihrer wallet-bezogenen Daten, zur allgemeinen Sicherheit der Cold-Karte selbst bei. Weitere Informationen finden Sie in diesem [Artikel] (https://blog.coinkite.com/understanding-mk4-security-model/), in dem das Sicherheitsmodell der Cold-Karte erläutert wird.


Die Tastatur besteht aus 10 Zifferntasten, einer OK-Taste (`✓`) und einer Abbruchtaste (`✕`). Einige Zifferntasten können auch zur Navigation verwendet werden: `5` für die Navigation nach oben (`^`), `7` für die Navigation nach links (`<`), `8` für die Navigation nach unten `˅` und `9` für die Navigation nach rechts (`>`).


![01](assets/en/01.webp)


Wenn es keine Probleme mit der Verpackung gibt, können Sie den Beutel öffnen. Dem Mk4 liegt eine wallet-Sicherungskarte bei, auf der Sie Informationen zur PIN des Geräts, Anti-Phishing-Wörter und seedphrase speichern können. Führen Sie die folgenden Schritte für die Initialisierung durch:


1. Bereiten Sie ein Blatt Papier und einen Stift vor.

2. Schließen Sie das Mk4 an eine Stromquelle an (USB-C-Kabel) und legen Sie die MicroSD-Karte ein.

3. Sobald das Gerät zum ersten Mal eingeschaltet wird, erscheint auf dem Bildschirm eine Meldung über die Verkaufs- und Nutzungsbedingungen von Coldcard. Navigieren Sie nach unten und drücken Sie dann "✓", um fortzufahren.

4. Anschließend wird auf dem Bildschirm eine 12-stellige Nummer angezeigt. Überprüfen Sie diese Nummer mit der Nummer auf dem manipulationssicheren Beutel und der zusätzlichen Kopie der Beutelnummer, die im manipulationssicheren Beutel enthalten war, um sicherzustellen, dass das Gerät nicht manipuliert wurde. Wenn die Nummern nicht übereinstimmen, wenden Sie sich sofort an den Coinkite-Support, bevor Sie fortfahren. Andernfalls drücken Sie `✓`, um fortzufahren.


![02](assets/en/02.webp)


5. Wählen Sie "PIN-Code wählen".

6. Navigieren Sie nach unten, während Sie die Anweisungen lesen, um mit dem nächsten Schritt fortzufahren.


![03](assets/en/03.webp)


7. Erstellen Sie auf dem Mk4 das PIN-Präfix (2 bis 6 Zeichen lang), geben Sie es ein und notieren Sie es, dann drücken Sie "✓", um fortzufahren.

8. Schreiben Sie die beiden Wörter auf, die auf dem Bildschirm angezeigt werden. Dies sind die Anti-Phishing-Wörter. Drücken Sie "✓", um fortzufahren.


![04](assets/en/04.webp)


9. Erstellen und geben Sie das PIN-Suffix (oder den Rest der PIN, muss 2 bis 6 Zeichen lang sein) ein und notieren Sie es. Drücken Sie "✓", um fortzufahren.

10. Geben Sie Ihr PIN-Präfix erneut ein. Drücken Sie "✓", um fortzufahren.


![05](assets/en/05.webp)


11. Überprüfen Sie, ob die Anti-Phishing-Wörter mit denen übereinstimmen, die Sie in Schritt 8 geschrieben haben. Drücken Sie "✓", um fortzufahren.

12. Geben Sie das Suffix Ihrer PIN (oder den Rest der PIN) erneut ein. Drücken Sie "✓", um fortzufahren.


![06](assets/en/06.webp)


13. Die PIN und die Anti-Phishing-Wörter Ihres Mk4 wurden nun erfolgreich erstellt und vom Gerät gespeichert.


![07](assets/en/07.webp)


Beachten Sie, dass Mk4 Sie bei jedem Einschalten Ihres Geräts zur Eingabe Ihrer PIN auffordert. Ohne diese PIN können Sie nicht auf Ihr Coldcard Mk4 zugreifen. Stellen Sie also sicher, dass Sie eine ausreichende Sicherung der PIN und der Anti-Phishing-Wörter anlegen.


## Einrichten Ihres Wallet


Der nächste Schritt ist die Einrichtung Ihres wallet. Es gibt drei Möglichkeiten, dies zu tun:


- Erstellen eines neuen wallet (Standard)
- Erstellen eines neuen wallet mit Würfelwürfen
- Importieren eines wallet


### Erstellen eines neuen wallet (Standard)


Um einen neuen wallet zu erstellen, führen Sie einfach die folgenden Schritte aus.


1. Wählen Sie "New Wallet" (oder "New Seed Words") > Wählen Sie "12 Word" oder "24 Word (Standard)", je nachdem, was Sie bevorzugen.


![08](assets/en/08.webp)


2. Das Gerät erzeugt je nach Ihrer Wahl 12 oder 24 Wörter als seedphrase. Navigieren Sie nach unten, während Sie sorgfältig jedes Wort in der richtigen Reihenfolge aufschreiben. Drücken Sie dann "✓", um fortzufahren.


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

3. Das Gerät fordert Sie auf, Ihr seedphrase zu überprüfen, indem es die Fragen in einer zufälligen Reihenfolge stellt (z. B. "Wort 1 ist...", dann "Wort 5 ist...", dann "Wort 12 ist..." usw.), und für jede Frage stehen drei Wörter zur Auswahl. Beachte den Hinweis aus Schritt 2 und wähle die richtigen Wörter aus (indem du "1", "2" oder "3" drückst, je nachdem, was dem richtigen Wort entspricht), um die Erstellung des wallet abzuschließen.


![09](assets/en/09.webp)


4. Das Mk4 fragt dann, ob Sie NFC/Tap aktivieren möchten oder nicht. Wählen Sie zunächst "✕" für diese Option. Dies kann in den Einstellungen in Zukunft geändert werden.

5. Schließlich fragt das Mk4 auch, ob Sie den USB-Anschluss deaktivieren möchten (der für die Datenübertragung ohne Luftabdeckung verwendet werden kann). Wählen Sie für diese Option zunächst `✓`. Dies kann in den Einstellungen in Zukunft geändert werden.

6. Auf dem Bildschirm erscheint nun das Hauptmenü mit "Unterschriftsbereit" am oberen Rand. Dies markiert den Abschluss des wallet-Erstellungsprozesses.


![10](assets/en/10.webp)


### Erstellen eines neuen wallet mit Würfelwurf


Alternativ können Sie sich auch dafür entscheiden, das neue seedphrase mit Entropie zu erzeugen. Tun Sie dies, wenn Sie dem frisch generierten seedphrase von Mk4 nicht trauen.


Das Verfahren bei der Coldcard Mk4 ist wie folgt:


1. Wählen Sie "Neue Wallet" (oder "Neue Saatwörter") > Wählen Sie "12-Wort-Würfelwurf" oder "24-Wort-Würfelwurf", je nachdem, was Sie bevorzugen.

2. Sie werden aufgefordert, die Ergebnisse Ihrer Würfelwürfe einzugeben. Jeder Würfelwurf fügt dem wallet-Erstellungsprozess einen Zufallsfaktor hinzu, der sicherstellt, dass Ihr seedphrase auf völlig sichere und unvorhersehbare Weise erstellt wird. Die Mindestanzahl der Würfe beträgt 50 für seedphrase mit 12 Wörtern und 99 für seedphrase mit 24 Wörtern. Drücken Sie `✓`, nachdem Sie mindestens 99 Würfelwerte eingegeben haben.


![11](assets/en/11.webp)


3. Das Gerät erzeugt je nach Ihrer Wahl 12 oder 24 Wörter als seedphrase. Navigieren Sie nach unten, während Sie sorgfältig jedes Wort in der richtigen Reihenfolge aufschreiben. Drücken Sie dann "✓", um fortzufahren.

4. Das Gerät fordert Sie auf, Ihren seedphrase zu überprüfen, indem es die Fragen in einer zufälligen Reihenfolge stellt (z. B. "Wort 1 ist...", dann "Wort 5 ist...", dann "Wort 12 ist..." usw.), und für jede Frage stehen drei Wörter zur Auswahl. Beachte den Hinweis aus Schritt 3 und wähle die richtigen Wörter aus (indem du auf "1", "2" oder "3" drückst, je nachdem, was dem richtigen Wort entspricht), um die Erstellung des wallet abzuschließen.


![12](assets/en/12.webp)


5. Das Mk4 fragt dann, ob Sie NFC/Tap aktivieren möchten oder nicht. Wählen Sie zunächst "✕" für diese Option. Dies kann in den Einstellungen in Zukunft geändert werden.

6. Schließlich fragt das Mk4 auch, ob Sie den USB-Anschluss deaktivieren möchten (der für die Datenübertragung ohne Luftabdeckung verwendet werden kann). Wählen Sie für diese Option zunächst `✓`. Dies kann in den Einstellungen in Zukunft geändert werden.

7. Auf dem Bildschirm wird nun das Hauptmenü mit "Unterschriftsbereit" am oberen Rand angezeigt. Damit ist der Prozess der wallet-Erstellung abgeschlossen.


![13](assets/en/13.webp)


### Importieren eines wallet


Die letzte Option ist der Import eines wallet. Dies können Sie tun, wenn Sie ein wallet aus einem bereits vorhandenen seedphrase wiederherstellen möchten. Sie können diese Schritte ausführen:


1. Wählen Sie "Vorhandenes importieren".

2. Wählen Sie "24 Wörter", "18 Wörter" oder "12 Wörter", je nachdem, wie viele Wörter Ihr seedphrase haben soll.


![14](assets/en/14.webp)


3. Coldcard Mk4 fragt Sie dann nach den einzelnen Wörtern in fortlaufender Reihenfolge. Navigieren Sie für jedes Wort nach unten oder oben, bis Sie die Schreibvorsilbe für jedes Wort finden. Das Gerät grenzt die Möglichkeiten ein, bis Sie das richtige Wort gefunden haben. Verfahren Sie so mit den übrigen Wörtern.

4. Für das letzte Wort zeigt Coldcard Mk4 nur eine begrenzte Anzahl von möglichen Wörtern an. Wenn es keine Übereinstimmungen gibt, haben Sie die Wörter möglicherweise falsch eingegeben. Andernfalls wählen Sie das Wort aus, das mit dem Wort auf Ihrem seedphrase übereinstimmt.


![15](assets/en/15.webp)


5. Das Mk4 fragt dann, ob Sie NFC/Tap aktivieren möchten oder nicht. Wählen Sie zunächst "✕" für diese Option. Dies kann in den Einstellungen in Zukunft geändert werden.

6. Schließlich fragt das Mk4 auch, ob Sie den USB-Anschluss deaktivieren möchten (der für die Datenübertragung ohne Luftabdeckung verwendet werden kann). Wählen Sie für diese Option zunächst `✓`. Dies kann in den Einstellungen in Zukunft geändert werden.

7. Auf dem Bildschirm erscheint nun das Hauptmenü mit "Unterschriftsreif" am oberen Rand. Dies markiert den Abschluss des wallet-Erstellungsprozesses.


![16](assets/en/16.webp)


Bitte beachten Sie, dass das seedphrase der einzige Zugang zur Wiederherstellung Ihres wallet ist. Erstellen Sie ein Backup Ihres seedphrase und bewahren Sie es an einem sicheren Ort auf. **Nicht Ihre Schlüssel, nicht Ihre Münzen**, wer auch immer Ihr seedphrase hat, hat Zugang zu Ihren Bitcoins!


## Einrichten Ihres passphrase


Eine der besten Praktiken bei Bitcoin ist die Verwendung eines passphrase. Der passphrase fungiert als 13. oder 25. Wort zusätzlich zum seedphrase. Der Unterschied besteht darin, dass Sie jede beliebige Phrase wählen können, während der seedphrase aus einer vorgegebenen Liste von 2048 Wörtern ausgewählt wird. Nach dem Einrichten Ihres wallet beginnen Sie standardmäßig mit einem wallet mit einem leeren passphrase. Um einen nicht leeren passphrase einzurichten, führen Sie einfach die folgenden Schritte aus:


1. Gehen Sie zu `Passphrase`.

2. Navigieren Sie nach unten, um die Beschreibung über passphrase zu lesen, und drücken Sie dann auf "✓", um fortzufahren.

3. Wählen Sie "Phrase bearbeiten".


![17](assets/en/17.webp)


4. Geben Sie Ihren passphrase ein:


   - Drücken Sie "1" (Buchstaben), "2" (Zahlen) oder "3" (Symbole), um den Zeichentyp auszuwählen.
   - Drücken Sie "4", um zwischen Klein- und Großbuchstaben zu wechseln (kann nur bei der Eingabe von Buchstaben verwendet werden).
   - Navigieren Sie mit `^` oder `˅`, um das Zeichen für Ihren passphrase auszuwählen.
   - Navigieren Sie mit `<` oder `>`, um zwischen den Zeichen zu wechseln. Sie können auch `>` verwenden, um Leerzeichen hinzuzufügen.
   - Drücken Sie `✕`, um die Zeichen zu löschen.
   - Drücken Sie "✓", wenn Sie die Bearbeitung des passphrase abgeschlossen haben.

5. Die anderen Optionen haben zusätzlich die folgenden Funktionalitäten:


   - Mit "Wort hinzufügen" oder "Zahlen hinzufügen" können Sie Buchstaben/Zahlen an den passphrase anhängen, den Sie gerade bearbeiten.
   - Drücken Sie "Alle löschen", um den passphrase, den Sie gerade bearbeiten, zurückzusetzen.
   - Drücken Sie `CANCEL`, um zum Hauptmenü zurückzukehren.

6. Schreiben Sie Ihren passphrase als Backup auf.

7. Drücken Sie "AKZEPT", um den wallet mit dem soeben eingestellten passphrase aufzurufen.

8. Mk4 zeigt dann einen 8-stelligen Hauptschlüssel-Fingerabdruck an. Dieser kann als die "ID" des wallet angesehen werden. Notieren Sie sich diesen Fingerabdruck und drücken Sie `✓`, um fortzufahren.


![18](assets/en/18.webp)


9. Nun zeigt das wallet das Hauptmenü des wallet mit dem von Ihnen eingegebenen passphrase an.

10. Es ist wichtig zu beachten, dass ein wallet Ihnen nicht sagen wird, dass Sie den falschen passphrase eingegeben haben, da jeder passphrase jedem eigenen wallet mit einer einzigartigen Identität (Hauptschlüssel-Fingerabdruck) entspricht. Daher ist es eine gute Praxis, denselben passphrase erneut einzugeben und zu prüfen, ob er denselben wallet-Fingerabdruck erzeugt, um sicherzustellen, dass Sie ihn richtig eingegeben haben. Führen Sie dazu die Schritte 11 bis 14 aus.

11. Wählen Sie im Hauptmenü "Master wiederherstellen" und drücken Sie "✓". Sie befinden sich nun wieder im Hauptmenü des wallet mit dem leeren passphrase.


![19](assets/en/19.webp)


12. Gehen Sie erneut zu "Passphrase" und drücken Sie dann "✓", um fortzufahren.

13. Geben Sie den passphrase, den Sie in Schritt 6 aufgeschrieben haben, erneut ein und drücken Sie dann auf "AKPLY".

14. Vergleichen Sie den 8-stelligen Fingerabdruck des Hauptschlüssels mit dem, den Sie in Schritt 8 aufgeschrieben haben. Wenn die beiden Fingerabdrücke nicht übereinstimmen, haben Sie sich möglicherweise vertippt. Sie können stattdessen einen neuen passphrase auswählen und den Vorgang ab Schritt 1 wiederholen. Wenn jedoch beide Fingerabdrücke übereinstimmen, bedeutet dies, dass Sie den passphrase korrekt eingegeben haben.

15. Das wallet mit dem von Ihnen gewählten passphrase ist einsatzbereit.


## Exportieren des Wallet zum Sparrow


Wie andere Hardware-wallet kann auch die Coldcard Mk4 nicht allein verwendet werden. Sie muss mit einem Software-wallet verbunden werden, das als Schnittstelle dient. Das Software-wallet ermöglicht es Ihnen, Ihren Kontostand einzusehen, Transaktionen zu erstellen und Adressen zu verwalten, während die Cold-Karte diese Transaktionen sicher signiert, ohne jemals Ihre privaten Schlüssel preiszugeben.


In diesem Lernprogramm werden wir Sparrow und Wallet als Schnittstelle verwenden. Das Verfahren zum Exportieren des wallet ist wie folgt:


1. Vergewissern Sie sich, dass Sie eine MicroSD-Karte in den Mk4 eingelegt haben.

2. Führen Sie die Schritte unter "Einrichten des passphrase" auf dem wallet mit dem passphrase durch, das Sie exportieren möchten. Wenn Sie das wallet mit dem leeren passphrase exportieren möchten, können Sie diesen Schritt überspringen.

3. Gehen Sie zu "Erweitert/Tools" > Wählen Sie "Wallet exportieren" > Wählen Sie "JSON generisch" > Blättern Sie nach unten, während Sie die Anweisungen lesen, und drücken Sie dann "✓".


![20](assets/en/20.webp)


4. Mk4 hat nun eine Datei mit dem Format `.json` auf der MicroSD-Karte erstellt.


![21](assets/en/21.webp)


5. Nehmen Sie die MicroSD-Karte aus dem Cold und legen Sie sie in das Gerät ein, in dem der Sparrow Wallet installiert ist.

6. Sparrow Wallet öffnen.

7. Klicken Sie auf `Datei`


![22](assets/en/22.webp)


Klicken Sie anschließend auf "Neues Wallet"


![23](assets/en/23.webp)


Geben Sie dann den Namen für das wallet ein


![24](assets/en/24.webp)


Danach klicken Sie auf "Wallet erstellen"


![25](assets/en/25.webp)


8. Wählen Sie den "Skripttyp".


![26](assets/en/26.webp)


9. Wählen Sie im Abschnitt Keystore die Option "Airgapped Hardware Wallet".


![27](assets/en/27.webp)


10. Suchen Sie nach Coldcard und klicken Sie auf "Datei importieren...".


![28](assets/en/28.webp)


11. Wählen Sie die in Schritt 4 erstellte Datei aus (die Datei mit dem Format "json").


![29](assets/en/29.webp)


12. Kehren Sie auf dem Mk4 zum Hauptmenü zurück und navigieren Sie zu `Erweitert/Tools` > `Identität anzeigen`. Vergewissern Sie sich, dass der auf dem Bildschirm des Mk4 angezeigte Fingerabdruck mit dem des Sparrow Wallet übereinstimmt (der Master-Fingerabdruck im Abschnitt "Keystore")

13. Klicken Sie auf die Schaltfläche "Anwenden" in der rechten unteren Ecke.


![30](assets/en/30.webp)


14. Optional können Sie auch ein Passwort für das exportierte wallet hinzufügen. Dieses Kennwort wird jedes Mal benötigt, wenn Sie die Anwendung Sparrow Wallet öffnen, um auf das wallet zuzugreifen. Wenn Sie das Passwort in Zukunft vergessen, können Sie einfach die Schritte 1-13 wiederholen und ein neues Passwort wählen.


![31](assets/en/31.webp)


15. Das wallet wurde nun erfolgreich exportiert und ist nun einsatzbereit.


![32](assets/en/32.webp)


## Empfang von Bitcoin


Als nächstes werden wir lernen, wie man Bitcoin mit dem Mk4 empfängt. Dieser Prozess ist recht einfach, da Sie das Mk4-Gerät selbst nicht verwenden müssen. Solange Sie Ihr wallet bereits in Sparrow exportiert haben, können Sie Bitcoin direkt über Sparrow Wallet empfangen. Folgen Sie diesen Schritten, um Bitcoins mit Mk4 zu empfangen:


1. Sparrow Wallet öffnen.

2. Wählen Sie "Wallet öffnen" > Wählen Sie die wallet-Datei, an die Sie Bitcoin senden möchten > Geben Sie das Passwort für dieses wallet ein.


![33](assets/en/33.webp)


3. Klicken Sie auf der Benutzeroberfläche des Sparrow auf die Registerkarte "Empfangen" auf der linken Seite der Benutzeroberfläche.


![34](assets/en/34.webp)


4. Oben wird eine Adresse zusammen mit einem QR-Code angezeigt. Sie können die Adresse kopieren und einfügen oder den QR-Code mit dem wallet scannen, den Sie zum Senden von Bitcoin an Sparrow Wallet verwenden werden. Optional können Sie eine Bezeichnung für die empfangenen Bitcoins eingeben.


![35](assets/en/35.webp)


5. Nachdem Sie die Bitcoins gesendet haben, klicken Sie auf der Sparrow-Oberfläche auf die Registerkarte "Transaktionen" auf der linken Seite der Oberfläche. Oben in der Transaktionshistorie sehen Sie einen neuen Eintrag, der der Transaktion entspricht, die Sie gerade durchgeführt haben.


![36](assets/en/36.webp)


6. Sie können auch auf die Registerkarte "UTXOs" auf der linken Seite der Schnittstelle navigieren, um die Bitcoin zu sehen, die Sie gerade erhalten haben.


![37](assets/en/37.webp)


## Bitcoin verschicken


Im Gegensatz zum Empfang von Bitcoins müssen Sie beim Ausgeben von Bitcoins, die mit Ihrer Coldcard verbunden sind, die Coldcard zum Signieren der Transaktionen verwenden. Das Verfahren zum Senden von Bitcoins mit Mk4 ist wie folgt:


1. Setzen Sie die MicroSD-Karte in das Gerät ein, in dem Ihr Sparrow Wallet installiert ist.

2. Sparrow Wallet öffnen.

3. Wählen Sie "Wallet öffnen" > Wählen Sie die wallet-Datei, mit der Sie Bitcoins versenden möchten > Geben Sie das Passwort für diesen wallet ein.


![38](assets/en/38.webp)


4. Klicken Sie auf der Benutzeroberfläche des Sparrow auf die Registerkarte "Senden" auf der linken Seite der Benutzeroberfläche.


![39](assets/en/39.webp)


5. Auf der Registerkarte "Bezahlen an" geben Sie die Adresse ein, an die Sie die Bitcoins senden möchten.

6. Fügen Sie ein Etikett für die Transaktion hinzu.

7. Geben Sie den Betrag an Bitcoins ein, den Sie senden möchten.

8. Geben Sie die Gebühr ein, indem Sie den "Bereich" umschalten oder direkt eine Zahl in das Feld "Gebühr" eingeben.


![40](assets/en/40.webp)


9. Klicken Sie in der rechten unteren Ecke auf "Transaktion erstellen".


![41](assets/en/41.webp)


10. Sie gelangen auf eine neue Registerkarte für die Transaktion, deren Name die Bezeichnung ist, die Sie in Schritt 6 eingegeben haben. Klicken Sie auf "Transaktion zur Unterzeichnung abschließen".


![42](assets/en/42.webp)


11. Klicken Sie auf "Transaktion speichern" und speichern Sie die Transaktion auf der MicroSD-Karte. Benennen Sie die Datei bei Bedarf um. In diesem Schritt wird die Transaktion als PSBT-Datei gespeichert.


![43](assets/en/43.webp)


12. Nehmen Sie die MicroSD-Karte heraus und legen Sie sie in Ihr Coldcard Mk4 ein.

13. Schalten Sie Ihr Mk4 ein, indem Sie es an eine Stromquelle anschließen.

14. Geben Sie Ihre PIN ein.

15. Gehen Sie zu "Passphrase" und geben Sie das passphrase des wallet ein, mit dem Sie die Bitcoins versenden möchten. Wenn Sie das wallet mit dem leeren passphrase verwenden möchten, überspringen Sie diesen Schritt.

16. Stellen Sie sicher, dass der Fingerabdruck des Hauptschlüssels mit dem Ihres Sparrow Wallet übereinstimmt. Sie können dies auf der Registerkarte "Einstellungen" des Sparrow Wallet auf der linken Seite der Benutzeroberfläche überprüfen. Drücken Sie dann die Taste "✓" auf Ihrem Mk4, um fortzufahren. Dadurch gelangen Sie in das Hauptmenü.

17. Wählen Sie im Hauptmenü des Mk4 "Unterschriftsbereit". Auf dem Bildschirm wird die Meldung "OKAY TO SEND" angezeigt. Vergewissern Sie sich, dass der Betrag der Bitcoins, den Sie senden möchten, und die Empfängeradresse korrekt sind. Drücken Sie "✓" zum Bestätigen oder "✕" zum Abbrechen.

18. Wenn mehrere PSBT-Dateien zur Auswahl stehen, zeigt Mk4 die Meldung "Wählen Sie die zu signierende PSBT-Datei" an. Drücken Sie "✓", um fortzufahren. Wählen Sie dann die PSBT-Datei aus, die Sie signieren möchten, indem Sie nach unten oder oben navigieren. Führen Sie Schritt 17 für diese Transaktion aus.


![44](assets/en/44.webp)


19. Mk4 zeigt nun die Meldung `PSBT Signed` zusammen mit dem Namen der Datei des signierten PSBT an. Drücken Sie "✓", um fortzufahren.

20. Nehmen Sie die MicroSD-Karte aus dem Cold und legen Sie sie in das Gerät ein, in dem das Sparrow Wallet installiert ist.

21. Klicken Sie auf Sparrow Wallet auf "Transaktion laden".


![45](assets/en/45.webp)


22. Wählen Sie die Datei mit demselben Namen wie die in Schritt 19 erstellte Datei.


![46](assets/en/46.webp)


23. Klicken Sie auf "Transaktion verbreiten".


![47](assets/en/47.webp)


24. Ihre Transaktion wurde übertragen und wird derzeit bearbeitet. Sie können die Registerkarte "Transaktionen" aufrufen, um den Bestätigungsstatus Ihrer Transaktion anzuzeigen.


![48](assets/en/48.webp)


## Firmware-Upgrade


### Überprüfen der Firmware-Version


Die Firmware der Coldcard Mk4 kann jederzeit auf eine neuere Version aktualisiert werden. Um zu überprüfen, ob Ihr Mk4 auf die neueste Version aktualisiert wurde oder nicht, führen Sie die folgenden Schritte aus:

1. Schalten Sie Ihr Mk4 ein, indem Sie es an eine Stromquelle anschließen.

2. Geben Sie Ihre PIN ein.

3. Gehen Sie zu "Erweitert/Tools" > Wählen Sie "Firmware aktualisieren" > Wählen Sie "Version anzeigen".


![49](assets/en/49.webp)


Überprüfen Sie die auf dem Bildschirm des Mk4 angezeigte Version mit der Version auf der [Coinkite-Website] (https://coldcard.com/downloads). Wenn die Version unterschiedlich ist, können Sie die Firmware auf die neuere Version aktualisieren.


![50](assets/en/50.webp)


### Aktualisieren der Firmware


Wenn Sie die Firmware auf die neueste Version aktualisieren möchten, führen Sie die folgenden Schritte aus:


1. Legen Sie die MicroSD-Karte in Ihren Laptop/PC ein.

2. Gehen Sie zur [Coinkite-Website] (https://coldcard.com/downloads) und laden Sie die neueste Firmware auf Ihre MicroSD-Karte herunter (die rote Schaltfläche rechts neben dem Mk4-Bild mit der Versionsnummer).


![51](assets/en/51.webp)


Sie können auch andere Versionen herunterladen, indem Sie auf "Alle Dateien auf Mk4" klicken und die gewünschte Version auswählen. Die heruntergeladene Datei hat das Format `.dfu`.


![52](assets/en/52.webp)


3. Nehmen Sie die MicroSD-Karte heraus und legen Sie sie in Ihr Mk4 ein.

4. Schalten Sie Ihr Mk4 ein, indem Sie es an eine Stromquelle anschließen.

5. Geben Sie Ihre PIN ein.

6. Gehen Sie zu "Erweitert/Tools" > Wählen Sie "Firmware aktualisieren" > Wählen Sie "Von MicroSD" > Blättern Sie nach unten, während Sie die Anweisungen lesen, und drücken Sie dann "✓".


![53](assets/en/53.webp)


7. Wählen Sie die in Schritt 2 heruntergeladene Datei `.dfu`.

8. Coldcard Mk4 zeigt die Meldung "Diese neue Firmware installieren" an. Scrollen Sie nach unten, während Sie die Anweisungen lesen, und drücken Sie "✓".


![54](assets/en/54.webp)


9. Warten Sie, bis der Mk4 die Installation der neuen Firmware abgeschlossen hat. Trennen Sie das Gerät während der Installation nicht von der Stromversorgung.

10. Nach Abschluss des Vorgangs startet sich das Mk4 neu. Sie können Ihre PIN eingeben und die Schritte "Prüfen der Firmware-Version" ausführen, um zu prüfen, ob die Firmware aktualisiert wurde oder nicht.


## Erweiterte Funktionen


### Ändern Sie Ihre PIN


Wenn Sie Ihre Anmelde-PIN ändern möchten, führen Sie einfach die folgenden Schritte aus:


1. Halten Sie einen Stift und ein Blatt Papier bereit.

2. Schalten Sie Ihr Mk4 ein, indem Sie es an eine Stromquelle anschließen.

3. Geben Sie Ihre PIN ein.

4. Gehen Sie zu "Einstellungen" > Wählen Sie "Anmeldeeinstellungen" > Wählen Sie "Haupt-PIN ändern"

5. Navigieren Sie nach unten, während Sie die Nachricht lesen, und drücken Sie dann "✓", um fortzufahren.


![55](assets/en/55.webp)


6. Geben Sie Ihre alte PIN ein.

7. Geben Sie Ihr neues PIN-Präfix ein (es muss 2 bis 6 Zeichen lang sein) und notieren Sie es.

8. Mk4 zeigt nun zwei neue Anti-Phishing-Wörter an. Schreiben Sie sie auf und drücken Sie dann auf "✓", um fortzufahren.

9. Geben Sie Ihr neues PIN-Suffix (oder den Rest der PIN, muss 2 bis 6 Zeichen lang sein) ein und notieren Sie es.


![56](assets/en/56.webp)


10. Geben Sie Ihr neues PIN-Präfix erneut ein.

11. Überprüfen Sie, ob die Anti-Phishing-Wörter mit denen übereinstimmen, die Sie in Schritt 8 geschrieben haben.

12. Geben Sie Ihre neue PIN-Endung (oder den Rest der PIN) erneut ein.


![57](assets/en/57.webp)


13. Ihre PIN wurde erfolgreich geändert.


### Trick-PINs - Neuen Trick hinzufügen


Eine Trick-PIN ist ein alternativer PIN-Code, der sich von dem unterscheidet, den Sie bei der Ersteinrichtung Ihres Coldcard Mk4 verwenden. Wenn Sie Ihr Mk4 einschalten, können Sie die Trick-PIN(s) anstelle Ihrer Haupt-PIN eingeben, um bestimmte Aktionen auszulösen. Um die Trick-PIN in Mk4 zu konfigurieren, können Sie die folgenden Schritte durchführen:


1. Halten Sie einen Stift und ein Blatt Papier bereit.

2. Schalten Sie Ihr Mk4 ein, indem Sie es an eine Stromquelle anschließen.

3. Geben Sie Ihre PIN ein.

4. Gehen Sie zu "Einstellungen" > Wählen Sie "Anmeldeeinstellungen" > Wählen Sie "Trick-PINs" > Wählen Sie "Neuen Trick hinzufügen".


![58](assets/en/58.webp)


5. Geben Sie Ihren Trick-PIN-Präfix ein (er muss 2 bis 6 Zeichen lang sein) und notieren Sie ihn.

6. Mk4 zeigt nun zwei neue Anti-Phishing-Wörter an. Schreiben Sie sie auf und drücken Sie dann auf "✓", um fortzufahren.

7. Geben Sie das Suffix Ihrer Trick-PIN ein (oder den Rest der PIN, muss 2 bis 6 Zeichen lang sein) und notieren Sie es.


![59](assets/en/59.webp)


8. Navigieren Sie nach unten oder oben, um die Aktion auszuwählen, die Sie mit der gerade erstellten Trick-PIN verknüpfen möchten. Die Liste der Aktionen sind:


    - brick Self", wenn ausgewählt, werden die Chips Ihres Mk4 nach Eingabe der PIN zerstört, wodurch Ihr Mk4 dauerhaft unbrauchbar wird.
    - saatgut löschen" können Sie zwischen den folgenden Aktionen wählen:
      - löschen und neu starten": Das seed wird gelöscht und die Cold-Karte wird nach Eingabe der PIN neu gestartet.
      - stille Löschung": Das seed wird stillschweigend gelöscht, die Cold-Karte verhält sich jedoch so, als ob die PIN falsch eingegeben worden wäre.
      - wischen -> Wallet": Das seed wird stillschweigend gelöscht, und die Cold-Karte bringt Sie in ein Zwang-wallet.
    - wenn Sie die Option "Zwang Wallet" auswählen, wird Ihr Mk4 nach Eingabe der PIN zu einem Zwang wallet führen.
    - login Countdown" können Sie zwischen folgenden Aktionen wählen:
      - wischen & Countdown": Das seed wird sofort gelöscht, dann beginnt das Mk4 mit der Anzeige eines Countdowns.
      - countdown & Ziegelstein": Der Countdown beginnt und Mk4 wird sich nach Ablauf der Zeit selbst zerstören.
      - nur Countdown": Mk4 beginnt den Countdown und startet sich nach Ablauf der Zeit selbst neu.
    - wenn die Option "Blanko aussehen" ausgewählt wird, verhält sich die Cold-Karte nach der Eingabe der Trick-PIN so, als sei das seedphrase gelöscht worden, obwohl es in Wirklichkeit noch im Speicher vorhanden ist.
    - just Reboot": Wenn diese Option ausgewählt ist, startet sich das Coldcard nach Eingabe der Trick-PIN selbst neu.
    - diese erweiterte Funktion ist für erfahrene Benutzer gedacht und soll vor ernsthaften Bedrohungen schützen, z. B. vor der Nötigung durch jemanden mit Insiderwissen. Wenn der Delta-Modus aktiviert ist, scheint die COLDCARD das echte wallet zu öffnen, so dass der Angreifer es durchsuchen und bestätigen kann, dass es echt aussieht. Sie blockiert jedoch heimlich alle Transaktionssignierungen, so dass keine Bitcoins gesendet werden können. Außerdem wird der Zugriff auf den seed-Satz deaktiviert, und jeder Versuch, ihn einzusehen, löscht ihn vollständig. Um den gefälschten wallet überzeugender aussehen zu lassen, muss die für den Delta-Modus verwendete Trick-PIN mit denselben Zahlen beginnen wie die echte PIN (damit sie dieselben Anti-Phishing-Worte zeigt), aber anders enden.
    - policy Unlock", wenn ausgewählt, wird die Single Signer Spending Policy (SSSP) deaktiviert, nachdem die Trick-PIN eingegeben wurde.
    - wenn Sie die Option "Policy Unlock & Wipe" auswählen, wird vorgetäuscht, dass SSSP deaktiviert wird, aber das seedphrase wird dabei gelöscht.

9. Nachdem Sie die Aktion ausgewählt haben, die Sie mit der Trick-PIN koppeln möchten, bestätigen Sie Ihre Wahl durch Drücken von "✓". Ihre Trick-PIN ist erfolgreich konfiguriert.

10. Unter "Einstellungen" > "Anmeldeeinstellungen" > "Trick-PINs" sehen Sie die Liste der von Ihnen erstellten Trick-PINs und der damit verbundenen Aktionen. Sie haben die Möglichkeit, die Trick-PINs und die damit verbundenen Aktionen neu zu konfigurieren. Sie können sie auch ausblenden oder löschen, indem Sie die PIN auswählen und dann "Trick ausblenden" oder "Trick löschen" wählen.


![60](assets/en/60.webp)


### Trick-PINs - Hinzufügen, wenn falsch


Alternativ können Sie eine Aktion "Hinzufügen, wenn falsch" hinzufügen, die ausgelöst wird, wenn die falsche PIN eine bestimmte Anzahl von Malen eingegeben wird. Sie können dies mit den folgenden Schritten konfigurieren:


1. Schalten Sie Ihr Mk4 ein, indem Sie es an eine Stromquelle anschließen.

2. Geben Sie Ihre PIN ein.

3. Gehen Sie zu "Einstellungen" > Wählen Sie "Anmeldeeinstellungen" > Wählen Sie "Trick-PINs" > Wählen Sie "Hinzufügen, wenn falsch".


![61](assets/en/61.webp)


4. Mk4 zeigt eine Meldung zu dieser Einstellung an. Navigieren Sie nach unten, während Sie die Erklärung lesen, und drücken Sie dann "✓", um fortzufahren.

5. Geben Sie die Anzahl der Fehlversuche ein, die erforderlich sind, um die Aktion auszulösen. Hinweis: Die maximale Anzahl von Versuchen ist `12`. Dies liegt daran, dass das Mk4 so konzipiert ist, dass sich das Gerät selbst blockiert, wenn die falsche PIN 13 Mal eingegeben wird, wodurch es dauerhaft unbrauchbar wird. Nachdem Sie die Nummer eingegeben haben, drücken Sie "✓", um fortzufahren.

6. Navigieren Sie nach oben oder unten, um die Aktion auszuwählen. Die folgenden Aktionen sind verfügbar:


   - wischen, Stopp": Das seedphrase wird gelöscht und das Gerät zeigt "Seed is wiped, Stop" an
   - löschen und neu starten": Das seedphrase wird gelöscht und das Gerät startet neu, ohne dass eine Meldung erscheint.
   - stille Löschung": Das seedphrase wird leise gelöscht und das Gerät verhält sich wie ein Falsch-PIN-Versuch (keine offensichtliche Wipe-Meldung).
   - brick Self": Das Gerät ist dauerhaft deaktiviert und zeigt nur "Bricked" an
   - letzte Chance": Das seedphrase wird gelöscht, aber Sie erhalten einen letzten PIN-Versuch; geben Sie erneut eine falsche PIN ein und das Gerät wird gebrannt.
   - einfach neu starten": Das Gerät wird einfach neu gestartet und es ändert sich nichts weiter.

Wählen Sie die gewünschte Aktion und drücken Sie "✓", um fortzufahren


![62](assets/en/62.webp)


7. Sie gelangen zurück in das Verzeichnis "Einstellungen > Anmeldeeinstellungen > Trick-PINs". Unter "Trick-PINs" finden Sie die Liste der Trick-Pins mit der Aktion "Falsche PIN". Sie können sie auch ausblenden oder löschen, indem Sie die PIN auswählen und dann "Trick ausblenden" oder "Trick löschen" wählen.


![63](assets/en/63.webp)



## Schlussfolgerung


Dieses Tutorial zeigt Ihnen, wie Sie Mk4 einrichten, wie Sie Bitcoin-Transaktionen mit Mk4 durchführen und wie Sie einige erweiterte Funktionen von Mk4 nutzen. Es bietet sichere und flexible Möglichkeiten zur Speicherung und Verwaltung Ihrer Bitcoins. Sein Design stellt sicher, dass private Schlüssel das Gerät nie verlassen, während Funktionen wie passphrase, Trick-PINs und Air-Gapped-Transaktionen den Benutzern die volle Kontrolle über ihre Sicherheitseinstellungen geben. Es kann mit Sparrow und Wallet gekoppelt werden, um eine benutzerfreundliche Erfahrung beim Erstellen, Signieren und Verwalten von Bitcoin-Transaktionen zu ermöglichen, ohne die Privatsphäre oder Sicherheit zu beeinträchtigen.


Wenn Sie weitere Funktionen erkunden möchten, können Sie die Dokumentation auf der Coinkite-Website [hier](https://coldcard.com/docs/) einsehen. Ich hoffe, Sie finden diese Anleitung nützlich, wenn Sie Ihre Coldcard Mk4 verwenden. Vielen Dank und bis zum nächsten Mal!