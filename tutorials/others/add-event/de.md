---
name: Ein Event im Plan B Network hinzufügen
description: Wie schlage ich vor, ein neues Event im Plan B Network hinzuzufügen?
---
![event](assets/cover.webp)

PlanBs Mission ist es, erstklassige Bildungsressourcen über Bitcoin in möglichst vielen Sprachen bereitzustellen. Alle Inhalte, die auf der Website veröffentlicht werden, sind Open-Source und werden auf GitHub gehostet, was jedem die Möglichkeit bietet, zur Bereicherung der Plattform beizutragen.

Wenn Sie eine Bitcoin-Konferenz zum PlanB Network-Website hinzufügen und die Sichtbarkeit Ihres Events erhöhen möchten, aber nicht wissen wie? Dieses Tutorial ist für Sie!
![event](assets/01.webp)
- Zuerst müssen Sie ein Konto auf GitHub haben. Wenn Sie nicht wissen, wie Sie ein Konto erstellen, haben wir ein detailliertes Tutorial erstellt, um Sie anzuleiten.

https://planb.network/tutorials/others/create-github-account


- Gehen Sie zu [dem GitHub-Repository von PlanB, das den Daten gewidmet ist](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/conference) im Abschnitt `resources/conference/`:
![event](assets/02.webp)
- Klicken Sie oben rechts auf den Button `Add file`, dann auf `Create new file`:
![event](assets/03.webp)
- Wenn Sie noch nie zu den Inhalten des PlanB Network beigetragen haben, müssen Sie Ihren Fork des Original-Repositorys erstellen. Ein Repository zu forken bedeutet, eine Kopie dieses Repositorys auf Ihrem eigenen GitHub-Konto zu erstellen, was Ihnen ermöglicht, am Projekt zu arbeiten, ohne das Original-Repository zu beeinflussen. Klicken Sie auf den Button `Fork this repository`:
![event](assets/04.webp)
- Sie gelangen dann zur GitHub-Bearbeitungsseite:
![event](assets/05.webp)
- Erstellen Sie einen Ordner für Ihre Konferenz. Um dies zu tun, schreiben Sie in das Feld `Name your file...` den Namen Ihrer Konferenz in Kleinbuchstaben mit Bindestrichen anstelle von Leerzeichen. Zum Beispiel, wenn Ihre Konferenz "Paris Bitcoin Conference" heißt, sollten Sie `paris-bitcoin-conference` notieren. Fügen Sie auch das Jahr Ihrer Konferenz hinzu, zum Beispiel: `paris-bitcoin-conference-2024`:
![event](assets/06.webp)
- Um die Erstellung des Ordners zu bestätigen, notieren Sie einfach einen Schrägstrich nach Ihrem Namen im selben Feld, zum Beispiel: `paris-bitcoin-conference-2024/`. Das Hinzufügen eines Schrägstrichs erstellt automatisch einen Ordner anstelle einer Datei:
![event](assets/07.webp)
- In diesem Ordner erstellen Sie eine erste YAML-Datei mit dem Namen `events.yml`:
![event](assets/08.webp)
- Füllen Sie diese Datei mit Informationen über Ihre Konferenz anhand dieser Vorlage aus:

```yaml
- start_date:
  end_date:
  address_line_1:
  address_line_2: 
  address_line_3: 
  name:
  builder:
  type: conference
  book_online: false
  book_in_person: false
  price_dollars: 0
  description:
  language: 
    - 
  links:
    website:
    replay_url:    
    live_url :
  tags: 
    - 
```

Zum Beispiel könnte Ihre YAML-Datei so aussehen:

```yaml
- start_date: 2024-08-15
  end_date: 2024-08-18
  address_line_1: Paris, Frankreich
  address_line_2: 
  address_line_3: 
  name: Paris Bitcoin Konferenz 2024
  builder: Paris Bitcoin Konferenz
  type: conference
  book_online: false
  book_in_person: false
  price_dollars: 0
  description: Die größte Bitcoin-Konferenz in Frankreich mit über 8.000 Teilnehmern jedes Jahr!
  language:
- fr    - en
    - es
    - it
  links:
    website: https://paris.bitcoin.fr/conference
    replay_url:
    live_url :
  tags: 
    - Bitcoiner
    - Allgemein
    - International
```
![event](assets/09.webp)
Wenn Sie noch keinen "*builder*" Identifikator für Ihre Organisation haben, können Sie diesen durch Befolgen dieses anderen Tutorials hinzufügen.

https://planb.network/tutorials/others/add-builder



- Sobald Sie mit den Änderungen an dieser Datei fertig sind, speichern Sie diese, indem Sie auf den `Commit changes...` Button klicken:
![event](assets/10.webp)
- Fügen Sie einen Titel für Ihre Änderungen hinzu, sowie eine kurze Beschreibung:
![event](assets/11.webp)
- Klicken Sie auf den grünen `Propose changes` Button:
![event](assets/12.webp)
- Sie gelangen dann auf eine Seite, die alle Ihre Änderungen zusammenfasst:
![event](assets/13.webp)
- Klicken Sie oben rechts auf Ihr GitHub-Profilbild, dann auf `Your Repositories`:
![event](assets/14.webp)
- Wählen Sie Ihren Fork des PlanB Network Repositories aus:
![event](assets/15.webp)
- Sie sollten eine Benachrichtigung oben im Fenster mit Ihrem neuen Branch sehen. Er heißt wahrscheinlich `patch-1`. Klicken Sie darauf:
![event](assets/16.webp)
- Sie befinden sich jetzt auf Ihrem Arbeitsbranch:
![event](assets/17.webp)
- Gehen Sie zurück zum `resources/conference/` Ordner und wählen Sie den Ordner Ihrer Konferenz aus, den Sie im vorherigen Commit erstellt haben:
![event](assets/18.webp)
- Im Ordner Ihrer Konferenz klicken Sie auf den `Add file` Button, dann auf `Create new file`:
![event](assets/19.webp)
- Benennen Sie diesen neuen Ordner `assets` und bestätigen Sie dessen Erstellung, indem Sie am Ende ein Slash `/` setzen:
![event](assets/20.webp)
- In diesem `assets` Ordner erstellen Sie eine Datei namens `.gitkeep`:
![event](assets/21.webp)
- Klicken Sie auf den `Commit changes...` Button:
![event](assets/22.webp)
- Lassen Sie den Commit-Titel als Standard und stellen Sie sicher, dass das Kästchen `Commit directly to the patch-1 branch` angekreuzt ist, dann klicken Sie auf `Commit changes`:
![event](assets/23.webp)
- Kehren Sie zum `assets` Ordner zurück:
![event](assets/24.webp)
- Klicken Sie auf den `Add file` Button, dann auf `Upload files`: ![event](assets/25.webp)
- Eine neue Seite wird geöffnet. Ziehen Sie ein Bild, das Ihre Konferenz repräsentiert und auf der PlanB Network Seite angezeigt wird, per Drag-and-Drop:
![event](assets/26.webp)
- Es kann das Logo, ein Thumbnail oder sogar ein Poster sein:
![event](assets/27.webp)
- Sobald das Bild hochgeladen ist, überprüfen Sie, ob das Kästchen `Commit directly to the patch-1 branch` angekreuzt ist, dann klicken Sie auf `Commit changes`:
![event](assets/28.webp)
- Achten Sie darauf, dass Ihr Bild `thumbnail` benannt sein muss und im `.webp` Format vorliegen muss. Der vollständige Dateiname sollte daher lauten: `thumbnail.webp`:
![event](assets/29.webp)
- Kehren Sie zu Ihrem `assets` Ordner zurück und klicken Sie auf die Zwischendatei `.gitkeep`:
![event](assets/30.webp)
- Einmal bei der Datei angekommen, klicken Sie auf die 3 kleinen Punkte oben rechts und dann auf `Delete file`:
- Stellen Sie sicher, dass Sie sich noch immer auf dem gleichen Arbeitsbranch befinden, dann klicken Sie auf den `Commit changes`-Button:
![event](assets/31.webp)
- Fügen Sie Ihrem Commit einen Titel und eine Beschreibung hinzu, dann klicken Sie auf `Commit changes`:
![event](assets/33.webp)
- Gehen Sie zurück zur Wurzel Ihres Repositories:
![event](assets/34.webp)
- Sie sollten eine Nachricht sehen, die darauf hinweist, dass Ihr Branch Änderungen erfahren hat. Klicken Sie auf den `Compare & pull request`-Button:
![event](assets/35.webp)
- Fügen Sie Ihrem PR einen klaren Titel und eine Beschreibung hinzu:
![event](assets/36.webp)
- Klicken Sie auf den `Create pull request`-Button:
![event](assets/37.webp)
Herzlichen Glückwunsch! Ihr PR wurde erfolgreich erstellt. Ein Administrator wird ihn nun überprüfen und, wenn alles in Ordnung ist, in das Hauptrepository des PlanB Network mergen. Sie sollten Ihr Event ein paar Tage später auf der Webseite sehen.

Vergewissern Sie sich, den Fortschritt Ihres PR zu verfolgen. Ein Administrator könnte einen Kommentar hinterlassen, der nach zusätzlichen Informationen fragt. Solange Ihr PR nicht validiert ist, können Sie ihn im `Pull requests`-Tab im GitHub-Repository des PlanB Network einsehen:
![event](assets/38.webp)
Vielen Dank für Ihren wertvollen Beitrag! :)

