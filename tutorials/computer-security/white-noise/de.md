---
name: White Noise
description: Eine private, dezentrale Messaging-Anwendung, die auf den Protokollen Nostr und MLS basiert
---

![cover](assets/cover.webp)




## Einführung



"Mitten in der Schwierigkeit liegt die Chance". Dieses Zitat von Albert Einstein erinnert uns daran, dass Probleme nicht endgültig sind, sondern den Keim für neue, innovative Lösungen in sich tragen.



Die Beweggründe für die Einführung der Lösung, die wir in diesem Lernprogramm vorstellen, veranschaulichen dies perfekt. Es ist **White Noise**, geboren aus der Notwendigkeit.



In den Worten seines Gründers Max Hillebrand, über den das *Bitcoin Magazin* berichtet: "Wir haben dieses Projekt aus Mangel an Alternativen ins Leben gerufen." Er erklärt, dass "bestehende Verschlüsselungsanwendungen im großen Maßstab ineffizient sind: Wenn man 100 Personen zu einer Gruppenkonversation hinzufügt, verlangsamt sich die Verschlüsselung erheblich. Dezentrale Plattformen bieten unterdessen keine privaten Nachrichten an. Das offene Relay-Netzwerk von Nostr schließlich erlaubt es jedem, Ideen zu verbreiten, aber der Schutz direkter Nachrichten bleibt dramatisch unzureichend. Uns wurde klar: Um die Freiheit zu schützen, müssen wir diese Systeme zusammenführen."



## Was ist White Noise?



White Noise ist eine Open-Source-Messaging-Anwendung, die von einem gemeinnützigen Team entwickelt wurde. Die Anwendung fördert Sicherheit, Datenschutz und Dezentralisierung. Anders als herkömmliche Anwendungen erfordert sie weder eine Telefonnummer noch eine E-Mail-Adresse.


White Noise zeichnet sich durch die Integration von zwei grundlegenden Protokollen - Nostr und MLS - aus, die seine technische Grundlage bilden.



Nostr (Notes and Other Stuff Transmitted by Relays) ist ein dezentralisiertes, quelloffenes Protokoll, das darauf ausgelegt ist, der Zensur zu widerstehen.  Das Protokoll verwendet Relais, Schlüsselpaare und Clients.



https://planb.academy/tutorials/node/others/nostr-f6d21a64-9b04-4f21-ba1c-02c98cc91f98

Bei weißem Rauschen können Sie sogar Ihre eigenen Relaiseinstellungen wählen, um die Privatsphäre zu maximieren.



MLS (Messaging Layer Security) hingegen ist ein Sicherheitsprotokoll, das eine Ende-zu-Ende-Verschlüsselung von Nachrichten ermöglicht. Mit anderen Worten, die Nachrichten sind nur an den Endpunkten, d. h. dem Absender und dem Empfänger der Nachricht, zugänglich. Dies bedeutet, dass Relais, die an der Weiterleitung von Nachrichten beteiligt sind, keinen Zugriff auf deren Inhalt haben.



Hier ist ein kurzer Vergleich zwischen White Noise und einer Reihe der bekanntesten Messaging-Anwendungen.





| Vergleichspunkte            | White Noise | Telegram   | Whatsapp (Meta) | Bitchat | iMessage | Messenger (Meta) | Signal |
| --------------------------- | ----------- | ---------- | --------------- | ------- | -------- | ---------------- | ------ |
| E2EE-Verschlüsselung / 1:1  | ✅ Ja         | Optional   | ✅ Ja             | ✅ Ja    | ✅ Ja     | ✅ Ja              | ✅ Ja   |
| Gruppen-E2EE-Verschlüsselung| ✅ Ja         | ❌ Nein     | ✅ Ja             | ✅ Ja    | ✅ Ja     | Optional          | ✅ Ja   |
| Anonymisierung der Identität| ✅ Ja         | Optional   | ❌ Nein           | ✅ Ja    | ❌ Nein   | ❌ Nein            | ❌ Nein |
| Open-Source-Server          | ✅ Ja         | ❌ Nein     | ❌ Nein           | ✅ Ja    | ❌ Nein   | ❌ Nein            | ✅ Ja   |
| Open-Source-Client          | ✅ Ja         | ✅ Ja        | ❌ Nein           | ✅ Ja    | ❌ Nein   | ❌ Nein            | ✅ Ja   |
| Dezentraler Server          | ✅ Ja         | ❌ Nein     | ❌ Nein           | ✅ Ja    | ❌ Nein   | ❌ Nein            | ❌ Nein |
| Gründungsjahr               | 2025        | 2013       | 2009            | 2025    | 2011     | 2011             | 2014   |

## Erste Schritte mit White Noise



### White Noise Einbau



Rufen Sie die [White Noise-Website](https://www.whitenoise.chat/) auf, und klicken Sie auf **Download**.



![screen](assets/fr/03.webp)



White Noise ist derzeit nur auf mobilen Geräten verfügbar.


Drücken Sie auf der neu erscheinenden Oberfläche die Taste :





- die Schaltfläche **Zapstore** oder **Android APK**, wenn Sie es auf Android herunterladen möchten;
- auf die Schaltfläche **iOS TestFlight**, wenn Sie ein iPhone verwenden.



![screen](assets/fr/04.webp)



In diesem Lernprogramm werden wir einen Android-Download durchführen.


Wenn Sie sich für den Download über **Zapstore** entscheiden, werden Sie dorthin weitergeleitet. Geben Sie im Zapstore **White Noise** in die Suchleiste ein. Fahren Sie dann mit dem Download fort, indem Sie auf **Installieren** klicken.



![screen](assets/fr/05.webp)



![screen](assets/fr/06.webp)



Wenn Sie sich für den Download der APK-Datei entscheiden, werden Sie zum White Noise GitHub-Repository weitergeleitet, um die richtige Version für Ihr Smartphone auszuwählen.



Die verfügbaren APK-Dateien sind:





- whitenoise-0.2.1-arm64-v8a.apk** (57,7 MB), geeignet für aktuelle Handys mit 64-Bit-Prozessoren;
- whitenoise-0.2.1-armeabi-v7a.apk** (47,5 MB) geeignet für ältere Handys mit 32-Bit-Prozessoren.



Außerdem gibt es **.sha256**-Dateien, bei denen es sich nur um Prüfsummen handelt, um die Integrität des Downloads zu überprüfen.



![screen](assets/fr/07.webp)



Sobald der Download abgeschlossen ist, installieren und öffnen Sie die Anwendung.



![screen](assets/fr/08.webp)



### Erstmalige Einrichtung eines Benutzerkontos



Für Ihre erste Verbindung zum White Noise drücken Sie die Taste **Registrieren**.



![screen](assets/fr/09.webp)



Als Nächstes konfigurieren Sie Ihr Profil, indem Sie ein Profilfoto und einen Namen auswählen und eine kurze Beschreibung Ihrer Person hinzufügen. Sie müssen nicht Ihre echte Identität (Name und Foto) angeben.


Beachten Sie, dass White Noise automatisch einen Namen (Pseudonym) für Sie wählt, den Sie behalten oder ändern können. Drücken Sie abschließend die Schaltfläche **Ende**.



![screen](assets/fr/10.webp)



Sie werden zum **Startbildschirm** von White Noise weitergeleitet, wo Ihre Unterhaltungen aufgelistet sind. Ihr Konto ist nun eingerichtet und einsatzbereit. Sie können Ihr Profil teilen oder nach Freunden suchen, um einen Chat zu beginnen.



![screen](assets/fr/11.webp)




### Erkennung von White Noise-Schnittstellen



Auf der Hauptschnittstelle sehen Sie am oberen Rand des Bildschirms :



Das Profilsymbol in der oberen linken Ecke ist eine Miniaturansicht Ihres Profilfotos oder der erste Buchstabe Ihres Profilnamens. Klicken Sie darauf, um Ihre Kontoeinstellungen aufzurufen.



![screen](assets/fr/12.webp)



![screen](assets/fr/13.webp)



In der oberen rechten Ecke finden Sie das Symbol zum Starten einer neuen Unterhaltung.



![screen](assets/fr/14.webp)



![screen](assets/fr/15.webp)




## Einstellungen des Benutzerkontos



Drücken Sie auf das Profilsymbol in der oberen linken Ecke, um die Einstellungen aufzurufen.



![screen](assets/fr/16.webp)



Oben auf der Oberfläche **Einstellungen** finden Sie Ihr Foto und Ihren Profilnamen, gefolgt von Ihrem öffentlichen Schlüssel, den Sie mithilfe des daneben stehenden QR-Codes freigeben können.



![screen](assets/fr/17.webp)



Direkt darunter finden Sie die Schaltfläche **Konto ändern**, mit der Sie eine Verbindung zu einem anderen Profil innerhalb der Anwendung herstellen können.



![screen](assets/fr/18.webp)



Dann haben Sie einen ersten Abschnitt mit vier (4) Untermenüs wie z. B. :





- Profil ändern**



In diesem Untermenü können Sie den Profilnamen, die Nostr-Adresse (NIP-05)... ändern. Vergessen Sie nicht, auf **Speichern** zu klicken, um Ihre Änderungen zu speichern.



![screen](assets/fr/19.webp)





- Profilschlüssel**



Hier haben Sie Zugang zu Ihrem öffentlichen und privaten (geheimen) Schlüssel. White Noise erinnert Sie daran, dass Ihr privater Schlüssel unter keinen Umständen weitergegeben werden darf.



![screen](assets/fr/20.webp)





- Netzrelais



In diesem Untermenü können Sie **allgemeine Relais** (Relais, die für die Verwendung in allen Ihren Nostr-Anwendungen definiert sind), **Inbox-Relais** und **Schlüsselpaket-Relais** hinzufügen oder entfernen.



Tippen Sie dazu auf das Symbol **Müll** vor einem Relais, um es zu löschen, oder tippen Sie auf das Symbol **+** (Plus), um ein neues Relais hinzuzufügen.



![screen](assets/fr/21.webp)





- Trennen der Verbindung**



Klicken Sie auf dieses Untermenü, um die Verbindung Ihres Kontos mit der Anwendung zu trennen. Stellen Sie jedoch sicher, dass Sie Ihre privaten Schlüssel offline gespeichert haben, da Sie sich sonst später nicht mehr anmelden können.



![screen](assets/fr/22.webp)




Ein zweiter Bereich bietet Untermenüs:





- Einstellungen der Anwendung



Hier können Sie das Erscheinungsbild (Thema und Anzeigesprache) der Anwendung festlegen und sogar Daten löschen, wenn Sie das Gefühl haben, dass sie kompromittiert wurden oder wenn Sie sich selbst gefährdet fühlen.



![screen](assets/fr/23.webp)





- Spenden Sie für White Noise



Sie können das Team hinter White Noise (eine gemeinnützige Organisation) mit Spenden über ihre Lightning-Adresse oder ihre Bitcoin-Adresse für stille Zahlungen unterstützen.



![screen](assets/fr/24.webp)



Ganz unten finden Sie schließlich die **Entwicklereinstellungen**.



![screen](assets/fr/25.webp)




## Beginnen Sie ein Gespräch



Schauen wir uns nun an, wie man ein Gespräch beginnt. Zum Zeitpunkt der Erstellung dieses Artikels bietet White Noise drei Kommunikationsoptionen. Nacheinander werden wir **Private Gespräche** (**Chat 1:1**), d. h. nur zwischen Ihnen und einer anderen Person, **Gruppengespräche** und **Senden von Multimedia-Dateien** erkunden.




### Katze 1:1



Um einen neuen Korrespondenten hinzuzufügen, klicken Sie in der Hauptschnittstelle auf das Symbol für den Beginn einer neuen Unterhaltung.


Scannen Sie dann den QR-Code des öffentlichen Schlüssels (1) oder fügen Sie den öffentlichen Schlüssel (2) Ihres neuen Ansprechpartners in die Suchleiste ein, um ihn zu finden.



![screen](assets/fr/26.webp)



Tippen Sie dann auf die Schaltfläche **Gespräch beginnen**, um ein Gespräch mit Ihrem Gesprächspartner zu beginnen. Sie können auch **Ihrem Gesprächspartner folgen** oder ihn/sie zu einem Gruppengespräch einladen, indem Sie auf die Schaltfläche **Zur Gruppe hinzufügen** tippen.



![screen](assets/fr/27.webp)



Ihre erste Nachricht an einen neuen Korrespondenten ist eine Art Einladungsanfrage. Diese Anfrage muss von Ihrem Korrespondenten angenommen werden, bevor Sie mit ihm kommunizieren können. Lehnt er ab, ist kein Gespräch möglich.



![screen](assets/fr/28.webp)



Solange sie Ihre Einladung nicht annehmen, können sie auch den Inhalt Ihrer ersten Nachricht nicht lesen.



Wenn er Ihre Einladung annimmt, kann er Ihnen nun antworten, und Sie beide können nahtlos und sicher miteinander kommunizieren.



![screen](assets/fr/29.webp)



Darüber hinaus haben Sie in einer Diskussion zusätzliche Funktionen.



Sie können lange auf eine bestimmte Nachricht drücken, um Optionen wie z. B. anzuzeigen:




- auf die Nachricht mit einem Emoji (1) reagieren;
- ein **direktes Zitat** erstellen, um auf die Nachricht zu antworten, indem Sie **Antworten** (2) drücken;
- kopieren Sie die Nachricht, indem Sie **Kopieren** (3) drücken.



![screen](assets/fr/30.webp)





- eine Nachricht mit der Schaltfläche **Löschen** nur dann löschen, wenn sie von Ihnen stammt.



![screen](assets/fr/31.webp)



Sie können innerhalb einer Unterhaltung suchen.



Klicken Sie auf den Avatar des Gesprächspartners am oberen Bildschirmrand, um zu den "Gesprächsinformationen" zu gelangen, und tippen Sie auf die Schaltfläche **Im Gespräch suchen**.



![screen](assets/fr/32.webp)



![screen](assets/fr/33.webp)



Geben Sie in die angezeigte Suchleiste das Wort ein, nach dem Sie suchen möchten, und starten Sie die Suche. Ihre Suchbegriffe werden dann in **fett** hervorgehoben.



![screen](assets/fr/34.webp)




### Gruppengespräche



Konversationsgruppen können auf White Noise erstellt werden.



Berühren Sie dazu das Symbol in der Startoberfläche für neue Unterhaltungen und klicken Sie dann auf **Neue Gruppenunterhaltung**. Geben Sie dann in der Suchleiste den öffentlichen Schlüssel des ersten Mitglieds ein, das Sie zu Ihrer Gruppe hinzufügen möchten.



![screen](assets/fr/35.webp)



![screen](assets/fr/36.webp)



Wenn diese Option nicht funktioniert, geben Sie in der Schnittstelle **Eine neue Unterhaltung beginnen** den öffentlichen Schlüssel des ersten Mitglieds, das Sie der Gruppe hinzufügen möchten, in die Suchleiste ein. Sie können auch den QR-Code scannen, der mit seinem öffentlichen Schlüssel verbunden ist.



Anstatt auf die Schaltfläche **Gespräch beginnen** zu tippen, klicken Sie diesmal auf die Schaltfläche **Zur Gruppe hinzufügen**.



![screen](assets/fr/37.webp)



Tippen Sie im angezeigten Popup-Menü auf **Neue Gruppenunterhaltung**.



![screen](assets/fr/38.webp)



Drücken Sie dann **Fortfahren** (Sie müssen den öffentlichen Schlüssel nicht erneut eingeben).



![screen](assets/fr/39.webp)



Als Ersteller der Gruppe sind Sie automatisch deren Administrator. Geben Sie die Details der Gruppe ein, wie **Gruppenname und Beschreibung**, und klicken Sie dann auf die Schaltfläche **Gruppe erstellen**.



![screen](assets/fr/40.webp)



Der Benutzer, den Sie als erstes Mitglied hinzufügen, und alle anderen, die Sie später hinzufügen, erhalten eine Benachrichtigung, in der sie eingeladen werden, der Gruppe beizutreten. Sie müssen die Einladung annehmen, indem sie auf **Akzeptieren** klicken, um der Gruppe beizutreten.



![screen](assets/fr/41.webp)



Es ist auch möglich, ein neues Mitglied, mit dem Sie bereits chatten, zu einer bestehenden Gruppe hinzuzufügen. Klicken Sie dazu auf den Avatar des Gesprächspartners am oberen Bildschirmrand, um die "Gesprächsinformationen" aufzurufen, und tippen Sie auf die Schaltfläche **Zur Gruppe hinzufügen**.



![screen](assets/fr/42.webp)



Markieren Sie auf der nun erscheinenden Oberfläche die Gruppe, der Sie ihn hinzufügen möchten, und tippen Sie auf **Zur Gruppe hinzufügen**. Nun müssen Sie nur noch darauf warten, dass er der Gruppe beitritt.



![screen](assets/fr/43.webp)



Beachten Sie, dass nur ein Gruppenadministrator Gruppeninformationen ändern und Mitglieder hinzufügen oder ausschließen kann. Außerdem verhindert die Schlüsselrotation, dass gesperrte Mitglieder zukünftige Nachrichten entschlüsseln können.



Um ein Mitglied zu entfernen, tippen Sie in der Hauptgruppenoberfläche auf das Gruppensymbol oben, um die Gruppeninformationsoberfläche aufzurufen.



![screen](assets/fr/44.webp)



![screen](assets/fr/45.webp)



Klicken Sie dann auf den Namen des Mitglieds und **Aus der Gruppe entfernen**. Von dieser Schnittstelle aus können Sie ihm auch eine Nachricht schicken, ihm folgen oder ihn zu einer anderen Gruppe hinzufügen.



![screen](assets/fr/46.webp)



### Versenden von Multimedia-Dateien



Im Moment können nur Fotos zwischen Nutzern auf White Noise ausgetauscht werden. Egal, ob Sie sich in einer privaten Unterhaltung oder in einem Gruppenchat befinden, Sie müssen dazu :





- drücken Sie das Symbol **plus (+)** auf der linken Seite des Eingabefeldes für die Textnachricht.



![screen](assets/fr/47.webp)





- klicken Sie dann auf das Feld **Fotos** am unteren Rand, um auf Ihre Galerie zuzugreifen.



![screen](assets/fr/48.webp)





- wählen Sie das/die zu versendende(n) Foto(s) aus.



![screen](assets/fr/49.webp)



![screen](assets/fr/50.webp)



![screen](assets/fr/51.webp)





## Wichtige Punkte, die zu beachten sind



White Noise bietet ein hohes Maß an Vertraulichkeit und überlegener Sicherheit. Andererseits handelt es sich um eine sehr junge Anwendung, die noch nicht sehr weit verbreitet ist und noch in den Kinderschuhen steckt. Daher ist es noch zu früh, um aktive Schlussfolgerungen zu ziehen. Es ist möglich, dass während der Nutzung einige Fehlfunktionen auftreten.



Derzeit fehlen ihm im Vergleich zu gängigen Messaging-Anwendungen bestimmte Funktionen (keine Audio- oder Videoanrufe, kein Versand von Audio- oder Video-Multimedia-Dateien).



Nichtsdestotrotz bleibt White Noise eine interessante Option für Gespräche, bei denen Vertraulichkeit an erster Stelle steht (z. B. mit der Familie, engen Freunden oder Aktivisten in einer gemeinsamen Sache), auch wenn es ein wenig Aufwand für die Installation (über alternative Anwendungsstores oder APK-Dateien) und das Erlernen (Beherrschen des Konzepts der Schlüsselpaare, Clients und Relais mit dem Nostr-Protokoll) erfordert.



Jetzt wissen Sie, wie Sie White Noise verwenden können, um sicher mit Ihren Freunden und Ihrer Familie zu kommunizieren. Bitte geben Sie uns einen Daumen hoch, wenn Sie diese Anleitung nützlich finden.



Wir empfehlen unser Tutorial über Tox Chat, eine Anwendung, mit der Sie ohne Vermittler über das dezentrale Tox Protokoll chatten können.



https://planb.academy/tutorials/computer-security/communication/tox-027bc897-8c98-4265-b85b-e78b7ab607f3