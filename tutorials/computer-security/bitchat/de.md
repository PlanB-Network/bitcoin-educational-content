---
name: Bitchat
description: Dezentralisiertes, internetfreies Messaging für freie Kommunikation
---

![cover](assets/cover.webp)


![video](https://youtu.be/WfzcKAzgB9s)


*Dieses Video-Tutorial von BTC Sessions führt Sie durch den Prozess der Einrichtung und Verwendung des Bitchat!


Bitchat ist aus einem schnellen Prototyping hervorgegangen, bei dem [@jack](https://primal.net/jack) das ursprüngliche Konzept während einer Wochenend-Codierungssitzung entwickelte. [@calle](https://primal.net/calle) trat dem Projekt kurz darauf bei, um die Android-Implementierung mitzuentwickeln. Jack leitet derzeit die Entwicklung der iOS-Version, während Calle die Android-Version mit der Unterstützung vieler anderer Mitwirkender betreut.


## Einführung: Frei chatten, ohne Raster


Stellen Sie sich vor, Sie könnten Nachrichten versenden, wenn das Internet ausfällt, während einer Naturkatastrophe oder an Orten, an denen die Kommunikation eingeschränkt ist. Bitchat macht dies möglich. Es ist eine dezentralisierte Peer-to-Peer-Nachrichten-App, die zentrale Server überspringt und Geräte direkt miteinander kommunizieren lässt, und zwar völlig offline über Bluetooth und Mesh-Netzwerke. Bitchat wurde mit Blick auf Datenschutz und Ausfallsicherheit entwickelt und eignet sich ideal für den Einsatz in Bereichen, in denen herkömmliche Konnektivität unzuverlässig oder nicht verfügbar ist, z. B. in Katastrophenszenarien, an abgelegenen Orten oder für diejenigen, die eine Überwachung vermeiden möchten. Im Kern verwendet Bitchat Kryptographie, um sicherzustellen, dass jede Nachricht Ende-zu-Ende verschlüsselt, verifiziert und manipulationssicher ist.


In diesem Tutorial zeigen wir Ihnen, wie Bitchat funktioniert und wie Sie es für wirklich private, offline-fähige Kommunikation nutzen können.


## 🚀 Hauptmerkmale


Bitchat ermöglicht Offline-Messaging durch diese [Funktionen] (https://github.com/permissionlesstech/bitchat-android?tab=readme-ov-file#features):



- Plattformübergreifende Kompatibilität**: Volle Protokollkompatibilität zwischen iOS und Android.
- Dezentrales Mesh-Netzwerk**: Automatische Peer-Erkennung und Multi-Hop-Nachrichtenübertragung über Bluetooth Low Energy (BLE)
- Ende-zu-Ende-Verschlüsselung**: X25519-Schlüsselaustausch + AES-256-GCM für private Nachrichten
- Kanal-basierte Chats**: Themenbasierte Gruppennachrichten mit optionalem Passwortschutz
- Speichern und Weiterleiten**: Nachrichten werden für Offline-Peers zwischengespeichert und zugestellt, wenn sie sich wieder verbinden
- Datenschutz zuerst**: Keine Konten, keine Telefonnummern, keine dauerhaften Identifikatoren
- IRC-ähnliche Befehle: Vertraute Schnittstelle im Stil von `/join, /msg, /who`.
- Nachrichtenaufbewahrung**: Optionale kanalweite Nachrichtenspeicherung, die von den Kanalbesitzern gesteuert wird
- Notfall-Löschen**: Dreimaliges Tippen auf das Logo löscht sofort alle Daten
- Moderne Android UI**: Jetpack Compose mit Material Design 3
- Dunkle/Helle Themen**: Terminal-inspirierte Ästhetik passend zur iOS-Version
- Akku-Optimierung**: Adaptives Scannen und Energiemanagement


## 1️⃣ Wie Bitchat funktioniert - einfach


Mit dem Bitchat können Sie Telefone in der Nähe direkt über Bluetooth (wie folgt: "BLE") benachrichtigen, ohne dass ein Internet- oder Mobilfunksignal erforderlich ist. Wenn Sie einen Chat beginnen, führen die Telefone einen sicheren Handshake durch, um einen eindeutigen, temporären Verschlüsselungsschlüssel für Ihr Gespräch zu erstellen. Jede Nachricht ist mit einer Ende-zu-Ende-Verschlüsselung geschützt, und für jede Nachricht wird ein neuer Schlüssel verwendet, um sicherzustellen, dass frühere Nachrichten sicher bleiben, selbst wenn Ihr Telefon später kompromittiert wird. Schließlich teilt die App die Nachrichten in kleine Teile auf und vermischt sie mit zufälligen Dummy-Daten, um Ihre Nachrichtenaktivitäten zu verbergen. Bei direkten Chats von Gerät zu Gerät funktioniert die App nur innerhalb einer Reichweite von bis zu 100 Metern. Es ist, als würde man verschlüsselte Notizen in einem überfüllten Raum weitergeben - die Geräte flüstern direkt miteinander und schreddern die Schlüssel nach jeder Nachricht.


Mit Bitchat können Sie auch ortsbezogenen Chat-Räumen beitreten, indem Sie das Nostr-Protokoll und "#geohashes" verwenden. Ein Geohash ist ein kurzer Code, wie z.B. "#u33d", der ein bestimmtes geografisches Gebiet repräsentiert, von einer einzelnen Nachbarschaft bis hin zu einer ganzen Stadt oder Region. Sie können sich in jeden Geohash-Chatraum auf der ganzen Welt "teleportieren", indem Sie einfach den entsprechenden Tag eingeben. Ihre Nachrichten werden über ein dezentrales Netzwerk von Relais gesendet, das Ihren genauen Standort schützt. Außerdem erhalten Sie jedes Mal, wenn Sie einem Geohash-Raum beitreten, eine neue, vorübergehende Identität, die Ihre ortsbezogenen Unterhaltungen zusätzlich schützt.


Genauere technische Einzelheiten entnehmen Sie bitte dem [offiziellen Whitepaper] (https://github.com/permissionlesstech/bitchat/blob/main/WHITEPAPER.md).


## 2️⃣ Installation und Einrichtung


### Wo erhalten Sie Bitchat?


Sie können Bitchat über installieren:



- [Apple App Store](https://apps.apple.com/us/app/bitchat-mesh/id6748219622) (für iOS-Geräte)
- [Google Play Store](https://play.google.com/store/apps/details?id=com.bitchat.droid) (für Android-Geräte)


Android-Nutzer haben auch andere Möglichkeiten:



- Lade die APK direkt von der [GitHub Releases](https://github.com/permissionlesstech/bitchat-android/releases) Seite herunter oder
- Installation über den Nostr-kompatiblen [Zapstore] (https://zapstore.dev/apps/naddr1qvzqqqr7pvpzq7xwd748yfjrsu5yuerm56fcn9tntmyv04w95etn0e23xrczvvraqqgkxmmd9e3xjarrdpshgtnywfhkjeqxtfkcr)


![image](assets/en/01.webp)


**Hinweis**: dieses Tutorial konzentriert sich hauptsächlich auf die Android-Implementierung. Die iOS-Version kann abweichen


### Einrichtungsprozess


Nach der Installation öffnen Sie Bitchat, um diesen Bildschirm mit den ersten Berechtigungen zu sehen. Sie müssen Folgendes tun:


1. **Erteilen Sie diese erforderlichen Genehmigungen:**


   - Bluetooth-Zugang** (um Bitchat-Benutzer in der Nähe zu finden)
   - Genauer Standort** (Android benötigt dies für die Bluetooth-Funktionalität)
   - Benachrichtigungen** (um private Nachrichten zu erhalten)

2. **Akku-Optimierung deaktivieren**:


   - Dadurch kann Bitchat im Hintergrund laufen
   - Hält Mesh-Netzwerkverbindungen kontinuierlich aufrecht


Tippen Sie auf "Berechtigungen erteilen", folgen Sie den "Anweisungen" und "Batterieoptimierung deaktivieren", um zum nächsten Bildschirm zu gelangen.


![image](assets/en/02.webp)


Willkommen auf dem Hauptbildschirm des Bitchat. Orientieren wir uns:


### Einstellungen


Das Wichtigste zuerst. Das Einstellungsmenü kann durch Tippen auf das Bitchat-Logo geöffnet werden.  Die folgenden Optionen sind verfügbar:



- Stellen Sie das Erscheinungsbild ein (System/Hell/Dunkel).
- arbeitsnachweis" für Geohash zur Spam-Abwehr aktivieren (optional)
- Schalten Sie `Tor` ein, um die Privatsphäre zu verbessern.


![image](assets/en/16.webp)


### Ihre Identität festlegen


Tippen Sie oben auf das Feld "Bitchat/anonXXXX", um Ihren Benutzernamen auszuwählen. Unter diesem Namen werden Sie von anderen sowohl im Bluetooth- als auch im Internetmodus gesehen. Sie könnten zum Beispiel "anon2022" in einen Benutzernamen Ihrer Wahl ändern.


![image](assets/en/03.webp)


### Netzwerk-Kanäle auswählen


Verwenden Sie das Menü "#Ortskanäle" (rechts vom Benutzernamen), um zwischen den Verbindungsarten zu wechseln:



- BLE Mesh***: Standard-Bluetooth-Modus (kein Internet, Reichweite von 10 bis 50 Metern)
- #geohashes**: Internetfähige geografische Gemeinschaften mit [Nostr-Protokoll] (https://nostr.com/)


Wenn Sie den Modus `#geohashes` wählen, integriert sich Bitchat in das Nostr-Protokoll, um geografische Gemeinschaften zu ermöglichen. Ihre Nachrichten werden an "dezentralisierte Nostr-Relais" statt an das Peer-to-Peer-Netzwerk von Bitchat weitergeleitet, was breitere, aber standortgefilterte Konversationen ermöglicht. Entscheidend ist, dass Ihre Bitchat-Identitätsschlüssel alle Nostr-Ereignisse kryptografisch signieren, um die Authentifizierung aufrechtzuerhalten, während Geohash-Tags (wie `#u4pruyd` für eine Nachbarschaft) Nachrichten auf den von Ihnen gewählten Präzisionsgrad filtern. Das bedeutet, dass Sie an lokalen Diskussionen teilnehmen können, ohne Ihre genauen Koordinaten preisgeben zu müssen, obwohl ein Internetzugang erforderlich ist.


![image](assets/en/04.webp)


### Peers überwachen

lizenz: CC-BY-SA-V4

Der Peer-Zähler zeigt die Benutzer an:



- In der Nähe (BLE Mesh) oder
- In Ihrer Geohash-Zone (#geohashes)


![image](assets/en/05.webp)


## 3️⃣ Globaler Chat & Private Nachrichten


Das Bitchat bietet zwei verschiedene Kommunikationsmodi, um unterschiedlichen Anforderungen gerecht zu werden:



- Öffentliche Kanäle:** Für offene Unterhaltungen mit anderen. Sie können sich entweder über das lokale BLE-Mesh-Netzwerk für Benutzer in der Nähe oder über ein globales #geohash für internetfähige, standortbasierte Gemeinschaften verbinden.
- Private Nachrichten:** Für sichere Unterhaltungen unter vier Augen. Diese stellen eine direkte, verschlüsselte Verbindung her, damit Ihr Austausch vertraulich bleibt.


Die Kenntnis beider Modi wird Ihnen helfen, sich in Ihren Gesprächen zurechtzufinden.


### Öffentliche Kanäle: Das Gemeinschaftszentrum


Das Menü "#Standortkanäle" (oben rechts) steuert Ihre öffentliche Sichtbarkeit. Wenn Sie "Mesh" auswählen, werden Sie mit allen Nutzern in der Nähe über das BLE-Mesh verbunden, in der Regel mit Geräten im Umkreis von 10-50 Metern. So entsteht ein offenes Forum, in dem Nachrichten an alle in Reichweite gesendet werden, ideal für Veranstaltungsankündigungen oder lokale Warnungen.


Um eine größere geografische Reichweite zu erzielen, wählen Sie ein beliebiges `#geohash`-Tag, um internetgestützten Gemeinschaften beizutreten, die nach Standort gefiltert sind. Diese Kanäle verwenden Nostr-Protokollrelais, die eine Kommunikation über Städte oder Regionen hinweg ermöglichen und gleichzeitig die standortbezogene Relevanz beibehalten. Ihre Nachrichten erscheinen live für andere im selben Kanal, und neue Teilnehmer sehen automatisch den aktuellen Nachrichtenverlauf, sobald sie beitreten.


![image](assets/en/06.webp)


### Private Unterhaltungen: Sicher & verschlüsselt


Um ein privates Gespräch zu beginnen, tippen Sie einfach auf einen beliebigen "Benutzernamen", der in der "Übersicht der Kontakte" angezeigt wird. Sie können auch auf das "Sternsymbol" tippen, um diesen Benutzer als Favoriten zu markieren, wodurch er in Ihrer Kontaktliste sichtbar bleibt, auch wenn er offline ist.


![image](assets/en/07.webp)


Bitchat initiiert automatisch seinen "Sicherheits-Handshake", wenn Sie einen privaten Chat beginnen. Die Geräte tauschen ephemere Schlüssel aus, um einen verschlüsselten Tunnel speziell für Ihr Gespräch zu erstellen. Dieser Prozess stellt sicher, dass alle Ihre Nachrichten und freigegebenen Dateien dank der kontinuierlichen Ende-zu-Ende-Verschlüsselung vertraulich bleiben. Private Nachrichten unterstützen den Austausch von Text und Dateien.


![image](assets/en/08.webp)


## 4️⃣ Zusätzliche Merkmale


Sie können das Aktionsfeld sofort aufrufen, indem Sie irgendwo im Bitchat `/` eingeben. Dadurch wird ein Befehlsmenü für schnelle Aktionen angezeigt.



- Verbindungen verwalten**: benutzer sperren" oder "Peers freischalten"
- Kanalsteuerung**: kanäle anzeigen" oder "Kanal hinzufügen/erstellen"
- Soziale Interaktionen**: "Umarmung" oder "Klaps mit der Forelle" 🎣
- Chat-Wartung**: chat-Nachrichten löschen"
- Datenschutz-Tools**: "Sehen, wer online ist" oder "Private Nachricht senden"


Befehle werden sofort ausgeführt - wie "Satoshi blockieren", um Kritiker zum Schweigen zu bringen, oder "Hal umarmen", um positive Stimmung zu verbreiten 🫂.


![image](assets/en/09.webp)


## 5️⃣ Einen Kanal erstellen


Kanäle in Bitchat ermöglichen eine organisierte Kommunikation über Themen, Standorte oder Gemeinschaften. Um Ihre eigenen Kanäle zu erstellen, folgen Sie diesem Arbeitsablauf:


### Schritt 1: Einen Kanal erstellen


Um einen Kanal zu erstellen, tippen Sie `/j` oder `/join` gefolgt von dem Kanalnamen in einem beliebigen Chat (z.B. `/j <Kanalname>`). Nach der Erstellung erscheint ein neues `Icon ⧉`, das den neuen Kanal anzeigt. Andere Benutzer können dem Kanal beitreten, indem sie denselben Befehl eingeben (z. B. `/j bitchat_tutorial`).


![image](assets/en/10.webp)


### Schritt 2: Einstellungen konfigurieren


Zusätzlich zu den Standardbefehlen sind die folgenden Einstellungen innerhalb eines Kanals verfügbar:



- `/save` zum lokalen Speichern von Nachrichten
- `/transfer`, um das Eigentum an den Kanälen zu übertragen und
- /pass", um das Kanalpasswort zu ändern.


Für private Gemeinschaften aktiviert dieser Befehl den Passwortschutz, so dass zugelassene Mitglieder vor dem Beitritt ein benutzerdefiniertes Passwort eingeben müssen.


## 6️⃣ Panikmodus


Reden wir über den "Panikmodus": Durch dreimaliges Tippen auf das "Bitchat-Logo" werden alle lokalen Nachrichten und Daten in der App vollständig gelöscht. Dies ist der ultimative Schutz Ihrer Privatsphäre, perfekt für Situationen, die sofortige Diskretion erfordern.


**Wichtige Erinnerung:** _Panikmodus ist permanent. Sobald er aktiviert ist, können die Daten nicht wiederhergestellt werden. Mit Vorsicht verwenden.**


![image](assets/en/11.webp)


## 7️⃣ Geohashes


Geohash-Kanäle ermöglichen gezielte Unterhaltungen, die auf "geografischen Standorten" und nicht auf traditionellen Netzwerkverbindungen basieren. Diese Funktion verwandelt bitchat in ein standortbezogenes Kommunikationstool, das sich ideal für die lokale Koordination, den Aufbau von Gemeinschaften und standortspezifische Diskussionen eignet.


### Wie funktionieren `#geohashes`?


Das System unterteilt die Welt in Rasterquadrate unter Verwendung des [Geohash-Systems] (https://en.wikipedia.org/wiki/Geohash), wobei jedes Zeichen in der Raute eine größere Genauigkeit darstellt:



- Ebene 4** (z. B. "u33d"): Deckt etwa 25 km × 25 km ab - ideal für stadtweite Diskussionen
- Ebene 6** (z. B. "u33d8z"): Erfasst etwa 1,2 km × 1,2 km - Genauigkeit in der Nachbarschaft
- Ebene 8** (z. B. "u33d8z1k"): Erfasst etwa 150 m × 150 m - Straßenabschnittsgenauigkeit


Die Präzisionsauswahl schafft ein Gleichgewicht zwischen Privatsphäre und Nutzen: Höhere Stufen schaffen exklusivere Zonen, zeigen aber auch Ihren Standort genauer an.


### Beitritt zu `#geohash`-Kanälen


1. Rufen Sie das Menü "#Ortskanäle" auf.

2. Wählen Sie den gewünschten Genauigkeitsgrad und geben Sie die "#geohash" ein (z.B. #u33d)

3. Tippen Sie auf die Schaltfläche "Teleport", um dem "#Ortskanal" beizutreten.


![image](assets/en/12.webp)


Alternativ können Sie auf das "Kartensymbol" tippen, um in der Kartenansicht den Genauigkeitsgrad zu bestimmen, und auf "Auswählen" tippen, um dem "Standortkanal" beizutreten.


![image](assets/en/13.webp)


**Wichtige Erinnerung**: _#geohash-Funktionalität erfordert eine aktive Internetverbindung - im Gegensatz zu BLE-Mesh, das offline über Bluetooth funktioniert


## 8️⃣ Heatmaps


Heatmaps sind eine tolle Möglichkeit, Bitchat-Ereignisse und -Kanäle auf der ganzen Welt zu entdecken. [Bitmap](https://bitmap.lat/) visualisiert und verfolgt anonyme, ortsbezogene Nachrichten im Nostr-Netzwerk und zeigt kurzlebige Nostr-Ereignisse an. Werfen Sie einen Blick darauf und treten Sie standortspezifischen Kanälen und Chats bei.


![image](assets/en/15.webp)


## 🎯 Schlussfolgerung


Bitchat ermöglicht eine sichere, dezentralisierte Kommunikation für Szenarien, in denen herkömmliche Nachrichtenübermittlung versagt. Es kann ohne Internet-Infrastruktur mit BLE-Mesh-Netzwerken betrieben werden und eignet sich daher für Proteste, Katastrophengebiete und abgelegene Gebiete, in denen die Konnektivität eingeschränkt oder zensiert ist. Die App gewährleistet den Datenschutz durch Verschlüsselung mit ephemeren Schlüsseln, geohash-basierte Standortkanäle und einen Panikmodus zur Datenlöschung.


Die App befindet sich noch im Anfangsstadium der Entwicklung, aber sie ist bereits vielversprechend. Nutzer sollten mit gelegentlichen Fehlern rechnen und Probleme über [GitHub](https://github.com/permissionlesstech/bitchat-android/issues) melden. Verbesserungen sind geplant, darunter die Integration von "Cash" für private In-App-Transaktionen über das Cashu-Protokoll.


![image](assets/en/14.webp)


## 📚 Bitchat Ressourcen


[Github](https://github.com/permissionlesstech) | [Website ](https://bitchat.free/)| [Whitepaper](https://github.com/permissionlesstech/bitchat/blob/main/WHITEPAPER.md)