---
name: Hinzufügen eines Buches zum PlanB Netzwerk
description: Wie fügt man ein neues Buch zum PlanB Netzwerk hinzu?
---
![book](assets/cover.webp)

Die Mission von PlanB ist es, erstklassige Bildungsressourcen über Bitcoin in möglichst vielen Sprachen bereitzustellen. Alle Inhalte, die auf der Seite veröffentlicht werden, sind Open-Source und werden auf GitHub gehostet, was es jedem ermöglicht, zur Bereicherung der Plattform beizutragen.

**Möchten Sie ein Buch zum Thema Bitcoin auf der PlanB Netzwerkseite hinzufügen und die Sichtbarkeit Ihrer Arbeit erhöhen, wissen aber nicht wie? Dieses Tutorial ist für Sie!**
![book](assets/01.webp)
- Zuerst benötigen Sie ein GitHub-Konto. Wenn Sie nicht wissen, wie Sie ein Konto erstellen, haben wir ein detailliertes Tutorial erstellt, um Sie anzuleiten.

https://planb.network/tutorials/others/contribution/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c


- Gehen Sie zu [dem GitHub-Repository von PlanB, das den Daten gewidmet ist](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/books) im Abschnitt `resources/books/`:
![book](assets/02.webp)
- Klicken Sie oben rechts auf den Button `Add file`, dann auf `Create new file`:
![book](assets/03.webp)
- Wenn Sie noch nie zu den Inhalten des PlanB Netzwerks beigetragen haben, müssen Sie Ihren Fork des Original-Repositorys erstellen. Ein Repository zu forken bedeutet, eine Kopie dieses Repositorys auf Ihrem eigenen GitHub-Konto zu erstellen, was es Ihnen ermöglicht, am Projekt zu arbeiten, ohne das Original-Repository zu beeinflussen. Klicken Sie auf den Button `Fork this repository`:
![book](assets/04.webp)
- Sie gelangen dann zur GitHub-Bearbeitungsseite:
![book](assets/05.webp)
- Erstellen Sie einen Ordner für Ihr Buch. Um dies zu tun, schreiben Sie in das Feld `Name your file...` den Namen Ihres Buches in Kleinbuchstaben mit Bindestrichen anstelle von Leerzeichen. Wenn Ihr Buch zum Beispiel "*Mein Bitcoin Buch*" heißt, sollten Sie `mein-bitcoin-buch` notieren:
![book](assets/06.webp)
- Um die Erstellung des Ordners zu bestätigen, fügen Sie einfach einen Schrägstrich nach Ihrem Buchnamen in dasselbe Feld ein, zum Beispiel: `mein-bitcoin-buch/`. Das Hinzufügen eines Schrägstrichs erstellt automatisch einen Ordner anstelle einer Datei:
![book](assets/07.webp)
- In diesem Ordner erstellen Sie eine erste YAML-Datei mit dem Namen `book.yml`:
![book](assets/08.webp)
- Füllen Sie diese Datei mit Informationen über Ihr Buch mit dieser Vorlage aus:

```yaml
author: 
level: 
tags:
  - 
  - 
```

Hier sind die Details, die für jedes Feld ausgefüllt werden müssen:
- **`author`**: Geben Sie den Namen des Autors des Buches an.
- **`level`**: Geben Sie das erforderliche Niveau an, um das Buch gut lesen und verstehen zu können. Wählen Sie ein Niveau aus den folgenden:
	- `beginner`
	- `intermediate`
- `advanced` - `expert`
- **`tags`**: Fügen Sie zwei oder drei Tags hinzu, die zu Ihrem Buch passen. Zum Beispiel:
    - `bitcoin`
    - `history`
    - `technology`
    - `economy`
    - `education`...

Zum Beispiel könnte Ihre YAML-Datei so aussehen:

```yaml
author: Loïc Morel
level: beginner
tags:
  - bitcoin
  - technology
```

![book](assets/09.webp)
- Sobald Sie mit den Änderungen an dieser Datei fertig sind, speichern Sie sie, indem Sie auf den Button `Commit changes...` klicken:
![book](assets/10.webp)
- Fügen Sie einen Titel für Ihre Änderungen sowie eine kurze Beschreibung hinzu: ![book](assets/11.webp)
- Klicken Sie auf den grünen Button `Propose changes` (Änderungen vorschlagen): ![book](assets/12.webp)
- Sie gelangen dann auf eine Seite, die alle Ihre Änderungen zusammenfasst: ![book](assets/13.webp)
- Klicken Sie oben rechts auf Ihr GitHub-Profilbild und dann auf `Your Repositories` (Ihre Repositories): ![book](assets/14.webp)
- Wählen Sie Ihren Fork des PlanB Network-Repository aus: ![book](assets/15.webp)
- Sie sollten oben im Fenster eine Benachrichtigung mit Ihrem neuen Branch sehen. Er heißt wahrscheinlich `patch-1`. Klicken Sie darauf: ![book](assets/16.webp)
- Sie befinden sich jetzt auf Ihrem Arbeitsbranch: ![book](assets/17.webp)
- Gehen Sie zurück zum Ordner `resources/books/` und wählen Sie den Ordner Ihres Buches aus, den Sie im vorherigen Commit erstellt haben: ![book](assets/18.webp)
- Klicken Sie im Ordner Ihres Buches auf den Button `Add file` (Datei hinzufügen), dann auf `Create new file` (Neue Datei erstellen): ![book](assets/19.webp)
- Benennen Sie diesen neuen Ordner `assets` und bestätigen Sie dessen Erstellung, indem Sie am Ende ein Schrägstrich `/` setzen: ![book](assets/20.webp)
- Erstellen Sie in diesem `assets`-Ordner eine Datei mit dem Namen `.gitkeep`: ![book](assets/21.webp)
- Klicken Sie auf den Button `Commit changes...` (Änderungen übernehmen): ![book](assets/22.webp)
- Belassen Sie den Commit-Titel wie vorgegeben und stellen Sie sicher, dass das Kästchen `Commit directly to the patch-1 branch` (Direkt in den Branch patch-1 übernehmen) angekreuzt ist, dann klicken Sie auf `Commit changes` (Änderungen übernehmen): ![book](assets/23.webp)
- Kehren Sie zum `assets`-Ordner zurück: ![book](assets/24.webp)
- Klicken Sie auf den Button `Add file` (Datei hinzufügen), dann auf `Upload files` (Dateien hochladen): ![book](assets/25.webp)
- Eine neue Seite wird geöffnet. Ziehen Sie das Coverbild Ihres Buches in den Bereich. Dieses Bild wird auf der PlanB Network-Website angezeigt: ![book](assets/26.webp)
- Achten Sie darauf, dass das Bild im Format eines Buches sein muss, um sich am besten unserer Website anzupassen, wie zum Beispiel: ![book](assets/27.webp)
- Sobald das Bild hochgeladen ist, stellen Sie sicher, dass das Kästchen `Commit directly to the patch-1 branch` (Direkt in den Branch patch-1 übernehmen) angekreuzt ist, dann klicken Sie auf `Commit changes` (Änderungen übernehmen): ![book](assets/28.webp)- Bitte beachten Sie, dass Ihr Bild `cover_en` benannt sein muss, wenn das Cover auf Englisch ist und im `.webp`-Format sein muss. Daher sollte der vollständige Dateiname `cover_en.webp`, `cover_fr.webp`, `cover_it.webp` usw. lauten. Wenn Sie für jede Sprache ein unterschiedliches Coverbild verwenden möchten, zum Beispiel im Falle einer Buchübersetzung, können Sie diese am gleichen Ort im `assets`-Ordner platzieren: ![book](assets/29.webp)
- Gehen Sie zurück zu Ihrem `assets`-Ordner und klicken Sie auf die Zwischendatei `.gitkeep`: ![book](assets/30.webp)
- Einmal auf der Datei, klicken Sie auf die 3 kleinen Punkte oben rechts und dann auf `Delete file` (Datei löschen): ![book](assets/31.webp)
- Stellen Sie sicher, dass Sie immer noch auf dem gleichen Arbeitsbranch sind, dann klicken Sie auf den Button `Commit changes...` (Änderungen übernehmen): ![book](assets/32.webp)
- Fügen Sie Ihrem Commit einen Titel und eine Beschreibung hinzu, dann klicken Sie auf `Commit changes` (Änderungen übernehmen): ![book](assets/33.webp)
- Kehren Sie zurück zum Ordner Ihres Buches: ![book](assets/34.webp)
- Klicken Sie auf den `Add file`-Button und dann auf `Create new file`:
![book](assets/35.webp)
- Erstellen Sie eine neue YAML-Datei, indem Sie sie mit dem Sprachkürzel des Buches benennen. Diese Datei wird für die Beschreibung des Buches verwendet. Wenn ich zum Beispiel meine Beschreibung auf Englisch schreiben möchte, benenne ich diese Datei `en.yml`:
![book](assets/36.webp)
- Füllen Sie diese YAML-Datei mit dieser Vorlage aus:
```yaml
title: ""
publication_year: 
cover: cover_en.webp
original: true
description: |

contributors:
  - 
```

Hier sind die Details, die für jedes Feld ausgefüllt werden müssen:
- **`title`**: Geben Sie den Namen des Buches in Anführungszeichen an.
- **`publication_year`**: Geben Sie das Jahr der Veröffentlichung des Buches an.
- **`cover`**: Geben Sie den Namen der Datei an, die dem Coverbild entspricht, in Übereinstimmung mit der Sprache der YAML-Datei, die Sie gerade bearbeiten. Wenn Sie zum Beispiel die `en.yml`-Datei bearbeiten und zuvor das englische Coverbild mit dem Titel `cover_en.webp` hinzugefügt haben, geben Sie einfach `cover_en.webp` in diesem Feld an.
- **`description`**: Fügen Sie einen kurzen Absatz hinzu, der das Buch beschreibt. Die Beschreibung muss in der gleichen Sprache sein, wie im Titel der YAML-Datei angegeben.
- **`contributors`**: Fügen Sie Ihre Mitwirkenden-ID hinzu, falls Sie eine haben.

Zum Beispiel könnte Ihre YAML-Datei so aussehen:

```yaml
title: "Mein Bitcoin-Buch"
publication_year: 2021
cover: cover_en.webp
original: true
description: |
Entdecken Sie die bahnbrechende Welt von Bitcoin mit diesem umfassenden Leitfaden für Anfänger. Mein Bitcoin-Buch entmystifiziert die Komplexitäten von Bitcoin und bietet eine klare und prägnante Einführung in die Funktionsweise des Protokolls. Von seiner revolutionären Technologie bis hin zu seinem potenziellen Einfluss auf die Weltwirtschaft bietet dieses Buch wertvolle Einblicke und praktisches Wissen. Perfekt für Bitcoin-Neulinge, deckt es die Grundlagen, Sicherheitstipps und die Zukunft der digitalen Finanzen ab. Tauchen Sie ein in die Zukunft des Geldes und stärken Sie sich mit dem Wissen, das digitale Zeitalter selbstbewusst zu navigieren.

contributors:
  - pretty-private

![book](assets/37.webp)
- Klicken Sie auf den `Commit changes...`-Button:
![book](assets/38.webp)
- Stellen Sie sicher, dass das Kästchen `Commit directly to the patch-1 branch` angekreuzt ist, fügen Sie einen Titel hinzu und klicken Sie auf `Commit changes`:
![book](assets/39.webp)
- Der Buchordner sollte jetzt so aussehen:
![book](assets/40.webp)
- Wenn alles für Sie gut aussieht, kehren Sie zurück zur Wurzel Ihres Forks:
![book](assets/41.webp)
- Sie sollten eine Nachricht sehen, die darauf hinweist, dass Ihr Branch geändert wurde. Klicken Sie auf den `Compare & pull request`-Button:
![book](assets/42.webp)
- Fügen Sie einen klaren Titel und eine Beschreibung zu Ihrem PR hinzu:
![book](assets/43.webp)
- Klicken Sie auf den `Create pull request`-Button:
![book](assets/44.webp)
Herzlichen Glückwunsch! Ihr PR wurde erfolgreich erstellt. Ein Administrator wird ihn nun überprüfen und, wenn alles in Ordnung ist, in das Hauptrepository des PlanB-Netzwerks zusammenführen. Sie sollten Ihr Buch ein paar Tage später auf der Website sehen.

Folgen Sie unbedingt dem Fortschritt Ihres PR. Ein Administrator könnte einen Kommentar hinterlassen, der nach zusätzlichen Informationen fragt. Solange Ihr PR nicht validiert ist, können Sie ihn im `Pull requests`-Tab im GitHub-Repository des PlanB-Netzwerks einsehen.
Vielen Dank für Ihren wertvollen Beitrag! :)
