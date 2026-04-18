---
name: BTC Pay Server meistern
goal: Eine BTC Pay Server-Instanz für ein lokales Unternehmen konfigurieren
objectives:
- Die Grundlagen der Rolle von BTCPay Server bei der Zahlungsabwicklung verstehen
- Die innere Funktionsweise des BTCPay Server-Konfigurationsprozesses beherrschen
- BTCPay Server in Cloud- und Node-basierten Umgebungen bereitstellen
- Ein BTC Pay Server-Betreiber werden
---
# Reise zur finanziellen Souveränität

Vertrauen ist zerbrechlich, besonders wenn es um Geld geht. Dieser Einführungskurs führt Sie durch BTCPay Server, ein leistungsstarkes Tool, mit dem Sie Bitcoin-Zahlungen akzeptieren können, ohne sich auf Dritte verlassen zu müssen. Sie lernen die Grundlagen, um ein BTCPay Server-Betreiber zu werden

Erstellt von Alekos und Bas und angepasst von melontwist und asi0, zeigt dieser Kurs, wie Einzelpersonen und Unternehmen Alternativen zu traditionellen Zahlungssystemen aufbauen. Egal, ob Sie neugierig auf Bitcoin sind oder bereit, Zahlungsinfrastrukturen für Unternehmen zu betreiben – Sie werden praktische Fähigkeiten entdecken, die den Status quo in Frage stellen. Bereit zu erkunden, wie finanzielle Unabhängigkeit tatsächlich aussieht?
+++
# Einführung


<partId>59e43fe3-b494-5da6-b4b4-9df5bdf08916</partId>


## Überblick über den Kurs


<chapterId>785ed2bc-94ae-4962-a26a-edf5742a3c72</chapterId>


Willkommen zum POS 305 Kurs auf BTCPay Server!


Ziel dieser Schulung ist es, Ihnen beizubringen, wie Sie BTCPay Server in Ihrem Unternehmen oder Ihrer Organisation installieren, konfigurieren und verwenden. BTCPay Server ist eine Open-Source-Lösung, mit der Sie Bitcoin-Zahlungen eigenständig, sicher und kostengünstig abwickeln können. Dieser Kurs richtet sich in erster Linie an fortgeschrittene Benutzer, die BTCPay Server selbst hosten und vollständig in ihre täglichen Abläufe integrieren möchten.


**Abschnitt 1: Einführung in den BTCPay Server**

Wir beginnen mit einer allgemeinen Präsentation von BTCPay Server, einschließlich des Anmeldebildschirms, der Verwaltung von Benutzerkonten und der Erstellung eines neuen Shops. Diese Einführung wird Ihnen helfen, den BTCPay Server Interface zu verstehen und die grundlegenden Funktionen zu begreifen, die Sie benötigen, um dieses Tool zu nutzen.


**Abschnitt 2: Einführung in die Sicherung von Bitcoin-Schlüsseln**

Die Sicherheit Ihrer Bitcoin-Gelder ist sehr wichtig. In diesem Abschnitt werden wir die Erzeugung von kryptografischen Schlüsseln, die Verwendung von Hardware-Wallets zur Sicherung dieser Schlüssel und die Interaktion mit Ihren Schlüsseln über BTCPay Server untersuchen. Sie erfahren auch, wie Sie einen BTCPay Server Lightning Wallet konfigurieren, um Ihre Transaktionen zu optimieren.


**Abschnitt 3: BTCPay Server Interface**

Dieser Teil führt Sie durch den BTCPay Server Benutzer Interface. Sie werden lernen, wie Sie durch das Dashboard navigieren, Shop- und Servereinstellungen konfigurieren, Zahlungen verwalten und die Vorteile integrierter Plugins nutzen können. Das Ziel ist es, Ihnen die notwendigen Werkzeuge an die Hand zu geben, um Ihre Installation an Ihre spezifischen Bedürfnisse anzupassen.


**Abschnitt 4: BTCPay Server konfigurieren**

Schließlich werden wir uns auf die praktische Installation von BTCPay Server in verschiedenen Umgebungen konzentrieren. Unabhängig davon, ob Sie LunaNode, Voltage oder einen Umbrel-Knoten verwenden, werden Sie die wesentlichen Schritte zur Bereitstellung und Konfiguration Ihres BTCPay-Servers erlernen, wobei die Besonderheiten der jeweiligen Umgebung berücksichtigt werden.


Sind Sie bereit, BTCPay Server zu beherrschen und Ihr Geschäft auszubauen? Los geht's!


## Kritischer Beifall für Bitcoin und BTCPay Server des Autors


<chapterId>e1fe6294-3c82-5203-9537-779f9087c35a</chapterId>


Beginnen wir damit, zu verstehen, was BTCPay Server ist und wie er entstanden ist. Wir legen Wert auf Transparenz und bestimmte Standards, um Vertrauen im Bitcoin-Raum zu schaffen.

Ein Projekt in diesem Bereich brach diese Werte. Der leitende Entwickler von BTCPay Server, Nicolas Dorier, nahm dies persönlich und gab das Versprechen, sie zu überholen. Hier sind wir nun, viele Jahre später, und arbeiten jeden Tag an dieser Zukunft, vollständig quelloffen.


> Das ist eine Lüge, mein Vertrauen in dich ist gebrochen, ich werde dich überflüssig machen.
> Nicolas Dorier

Nach den Worten von Nicolas war es an der Zeit, mit dem Bau zu beginnen. Eine beträchtliche Menge an Arbeit floss in das, was wir jetzt BTCPay Server nennen. Mehr Leute wollten zu dieser Anstrengung beitragen. Die bekanntesten sind r0ckstardev, MrKukks, Pavlenex und der erste Händler, der die Software benutzt hat, astupidmoose.


Was bedeutet Open Source, und was gehört zu einem solchen Projekt?


[FOSS](https://planb.academy/resources/glossary/foss) steht für Free & Open-Source Software. Ersteres bezieht sich auf Begriffe, die es jedem erlauben, die Software zu kopieren, zu verändern und sogar zu vertreiben (sogar mit Gewinn). Letzteres bezieht sich auf die offene Freigabe des Quellcodes und ermutigt die Öffentlichkeit, Beiträge zu leisten und die Software zu verbessern.

Dies zieht erfahrene Benutzer an, die mit Begeisterung einen Beitrag zu der Software leisten, die sie bereits benutzen und aus der sie einen Nutzen ziehen, und die sich letztendlich als erfolgreicher in der Annahme erweist als proprietäre Software. Es steht im Einklang mit dem Bitcoin-Ethos, dass "Information frei sein will" Es bringt leidenschaftliche Menschen zusammen, die eine Gemeinschaft bilden, und es macht einfach mehr Spaß. Wie Bitcoin ist auch FOSS unvermeidlich.


### Bevor wir beginnen


Dieser Kurs besteht aus mehreren Teilen. Viele davon werden von Ihrem Klassenlehrer betreut, Demo-Umgebungen, zu denen Sie Zugang erhalten, ein gehosteter Server für Sie selbst und möglicherweise ein Domain-Name. Wenn Sie diesen Kurs eigenständig absolvieren, beachten Sie bitte, dass Ihnen die als DEMO gekennzeichneten Umgebungen nicht zur Verfügung stehen werden.

NB. Wenn Sie diesen Kurs in einem Klassenzimmer absolvieren, können sich die Servernamen je nach Einrichtung des Klassenzimmers unterscheiden. Aus diesem Grund können die Variablen in den Servernamen unterschiedlich sein.


### Aufbau des Kurses


Zu jedem Kapitel gehören Ziele und Wissensüberprüfungen. In diesem Kurs werden wir jedes dieser Ziele behandeln und am Ende jedes Lektionsblocks (d. h. Kapitels) eine Zusammenfassung der wichtigsten Merkmale geben. Illustrationen werden verwendet, um visuelles Feedback zu geben und die wichtigsten Konzepte zu veranschaulichen. Zu Beginn jedes Lektionsblocks werden Ziele festgelegt. Diese Ziele gehen über eine Checkliste hinaus. Sie bieten Ihnen einen Leitfaden für neue Fähigkeiten. Die Wissensüberprüfungen werden nach und nach anspruchsvoller, wenn die Einrichtung Ihres BTCPay-Servers abgeschlossen ist.


### Was erhalten die Studierenden im Rahmen des Kurses?


Mit dem BTCPay-Server-Kurs können die Teilnehmer die technischen und nichttechnischen Grundlagen von Bitcoin verstehen. Die umfassende Schulung in der Verwendung von Bitcoin durch BTCPay Server ermöglicht es den Teilnehmern, ihre eigene Bitcoin-Infrastruktur zu betreiben.


### Wichtige Webadressen oder Kontaktmöglichkeiten


Die BTCPay Server Foundation, die es Alekos und Bas ermöglicht hat, diesen Kurs zu schreiben, befindet sich in Tokio, Japan. Die BTCPay Server Foundation kann über die angegebene Website erreicht werden.



- https://foundation.btcpayserver.org
- Nehmen Sie an den offiziellen Chat-Kanälen teil: https://chat.btcpayserver.org


## Einführung in Bitcoin


<chapterId>5c0bc234-c188-5b4a-94d5-adee87a120e2</chapterId>


### Verstehen von Bitcoin durch Übungen im Klassenzimmer


Dies ist eine Klassenraumübung. Wenn Sie diesen Kurs selbst besuchen, können Sie ihn nicht durchführen, aber Sie können diese Übung trotzdem durchlaufen. Um diese Aufgabe zu lösen, sind mindestens 9 bis 11 Personen erforderlich.


Die Übung beginnt nach dem Anschauen der Einführung "How Bitcoin and the [Blockchain](https://planb.academy/resources/glossary/blockchain) works" von der BBC.


:::video id=c20b6df7-0c3a-4785-94b9-42ef59093acc:::


Diese Übung erfordert eine Mindestanzahl von neun Teilnehmern. Diese Übung zielt darauf ab, ein physisches Verständnis dafür zu vermitteln, wie Bitcoin funktioniert. Indem Sie jede Rolle im Netzwerk spielen, können Sie auf interaktive und spielerische Weise lernen. Diese Übung beinhaltet nicht [Lightning Network](https://planb.academy/resources/glossary/lightning-network).


### Beispiel: Benötigt 9 / 11 Personen


Die Rollen sind:



- 1 Kunde
- 1 Händler
- 7 bis 9 Bitcoin-Knoten


**Der Aufbau ist wie folgt:**


Kunden kaufen ein Produkt im Laden mit Bitcoin.


**Szenario 1 - Traditionelles Bankensystem**



- Einrichten:
  - Siehe Diagramme/Erläuterungen im beigefügten Figjam - [Aktivitätsschema](https://www.figma.com/file/ckmvMq02Jm2MegSsVCDFhc/Day-1-Classroom-Activity?type=whiteboard&node-id=0-1&t=KR31ofMaJX6S95UL-0).
  - Bitten Sie drei freiwillige Schüler, die Rollen des Kunden (Alice), des Händlers (Bob) und der Bank zu übernehmen.
- Spielen Sie die Abfolge der Ereignisse nach:
  - Ein Kunde, der online im Laden stöbert und einen Artikel für 25 $ findet, den er haben möchte, informiert den Händler, dass er ihn kaufen möchte
  - Händler - bittet um Bezahlung.
  - Kunde - sendet Karteninformationen an den Händler
  - Händler - leitet Informationen an die Bank weiter (mit Angabe der eigenen und der Identität/Informationen) und fordert die Zahlung von
  - Die Bank sammelt Informationen über den Kunden und den Händler (Alice und Bob) und prüft, ob das Guthaben des Kunden ausreichend ist.
  - Zieht \$25 von Alice's Konto ab, fügt \$24 zu Bob's Konto hinzu, nimmt \$1 für die Dienstleistung
  - Der Händler erhält von der Bank ein "Daumen hoch" und versendet den Artikel an den Kunden.
- Kommentare:
  - Bob und Alice müssen eine Beziehung zu einer Bank haben.
  - Die Bank sammelt identifizierende Informationen sowohl über Bob als auch über Alice.
  - Bank nimmt einen Schnitt.
  - Die Bank muss darauf vertrauen können, dass sie das Geld der Teilnehmer jederzeit aufbewahrt.


**Szenario 2 - Bitcoin-System**



- Einrichten:
  - Siehe Diagramme/Erläuterungen im beigefügten Figjam - [Aktivitätsschema](https://www.figma.com/file/ckmvMq02Jm2MegSsVCDFhc/Day-1-Classroom-Activity?type=whiteboard&node-id=0-1&t=KR31ofMaJX6S95UL-0).
  - Ersetzen Sie die Bank durch neun Schüler, die die Rolle eines Computers (Bitcoin-Knoten/Miners) in einem Netzwerk spielen, das die Bank ersetzen soll.
- Jeder der 9 Computer verfügt über eine vollständige historische Aufzeichnung aller jemals getätigten Transaktionen (daher genaue Bilanzen ohne Fälschungen) sowie über ein Regelwerk:
  - Überprüfen Sie, ob die Transaktion ordnungsgemäß signiert ist (thekeyfitsthelock)
  - Senden und Empfangen von gültigen Transaktionen an Peers im Netzwerk, Verwerfen von ungültigen Transaktionen (einschließlich solcher, die versuchen, denselben Betrag zweimal auszugeben)
- Regelmäßige Aktualisierung/Hinzufügung von Datensätzen mit neuen Transaktionen, die vom "Zufalls"-Computer empfangen werden, sofern alle Inhalte gültig sind (Anmerkung: wir ignorieren der Einfachheit halber die [Proof of Work](https://planb.academy/resources/glossary/proof-of-work)-Komponente bei all dem), andernfalls werden diese zurückgewiesen und wie zuvor fortgesetzt, bis der nächste "Zufalls"-Computer eine Aktualisierung sendet
  - Der richtige Betrag wurde belohnt, wenn der Inhalt gültig war.
- Spielen Sie die Abfolge der Ereignisse nach:
  - Ein Kunde, der online im Laden stöbert und einen Artikel für 25 $ findet, den er haben möchte, informiert den Händler, dass er ihn kaufen möchte
  - Händler - bittet um Zahlung, indem er dem Kunden ein Invoice/Address von seinem [Wallet](https://planb.academy/resources/glossary/wallet) aus schickt.
  - Der Kunde führt eine Transaktion durch (Senden von BTC im Wert von 25 $ an ein vom Händler bereitgestelltes Address) und sendet sie an das Bitcoin-Netzwerk.
- Computer - empfangen die Transaktion und überprüfen sie:
  - Im Address befinden sich mindestens 25 $ BTC, die von
  - Die Transaktion wird ordnungsgemäß signiert ("freigeschaltet" durch den Kunden)
  - Ist dies nicht der Fall, wird die Transaktion nicht über das Netz weitergegeben, und wenn doch, wird sie weitergegeben und in Wartestellung gehalten.
  - Die Händler können überprüfen, ob die Transaktion noch nicht abgeschlossen ist und warten.
- Ein Computer wird "zufällig" ausgewählt, um vorzuschlagen, die vorgeschlagene Transaktion abzuschließen, indem er einen "[Block](https://planb.academy/resources/glossary/block)" sendet, der sie enthält; wenn sie erfolgreich ist, erhält er eine BTC-Belohnung.
  - OPTIONAL/ERWEITERT - anstatt einen Computer zufällig auszuwählen, simulieren Sie Mining, indem Sie die Computer würfeln lassen, bis ein bestimmtes Ergebnis eintritt (z. B. der erste, der zwei Sechsen würfelt, wird ausgewählt)
  - Es kann auch durchspielen, was passieren würde, wenn zwei Computer ungefähr gleichzeitig gewinnen, was zu einer Kettenaufteilung führt.
  - Die Computer prüfen die Gültigkeit, aktualisieren die Datensätze in ihren Hauptbüchern, wenn die Regeln erfüllt sind, und senden den Transaktionsblock an die Peers.
  - Der zufällig ausgewählte Computer erhält eine Belohnung für das Vorschlagen eines gültigen Blocks.
  - Die Transaktion wurde abgeschlossen, d. h. das Geld ist eingegangen, und die Ware wurde an den Kunden versandt.
- Kommentare:
  - Beachten Sie, dass keine Bankbeziehung bestehen muss.
  - Keine dritte Partei zur Erleichterung erforderlich; ersetzt durch Code/Anreize.
  - Keine Datenerhebung durch irgendjemanden außerhalb des direkten Exchange, und nur die notwendige Menge muss zwischen den Teilnehmern ausgetauscht werden (z. B. Versand Address).
  - Es ist kein Vertrauen zwischen den Personen erforderlich (außer dem Händler, der den Artikel versendet), wie bei einem Barkauf in vielerlei Hinsicht.
  - Das Geld ist direkt im Besitz der Personen.
  - Der Bitcoin Ledger ist der Einfachheit halber in Dollar angegeben, in Wirklichkeit handelt es sich aber um BTC.
  - Wir simulieren, dass eine einzige Transaktion übertragen wird, aber in Wirklichkeit stehen mehrere Transaktionen im Netz an, und die Blöcke umfassen Tausende von Transaktionen auf einmal. Die Knoten überprüfen auch, dass keine Transaktionen mit doppelten Ausgaben anhängig sind (in diesem Fall würde ich alle bis auf eine verwerfen).
- Betrugsszenarien:
  - Was wäre, wenn der Kunde keine 25 $ BTC hätte?
    - Sie wären nicht in der Lage, die Transaktion zu erstellen, da "Entsperren" und "Ownership" dasselbe sind und Computer prüfen, ob die Transaktion ordnungsgemäß signiert ist; andernfalls weisen sie sie zurück
  - Was ist, wenn der zufällig ausgewählte Computer versucht, "den Ledger zu ändern"?
    - Die Sperre würde zurückgewiesen, da jeder andere Computer einen vollständigen Verlauf hat und die Änderung bemerken würde, was gegen eine ihrer Regeln verstößt.
    - Der Zufallscomputer würde keine Belohnung erhalten, und es würden keine Transaktionen aus seinem Block abgeschlossen werden.


## Bewertung der Kenntnisse


<chapterId>1461f064-933d-50ea-8935-324b68ec5d5f</chapterId>


### KA Diskussion im Klassenzimmer


Diskutieren Sie einige Vereinfachungen, die in der Übung im Klassenzimmer unter dem zweiten Szenario gemacht wurden, und beschreiben Sie, was das tatsächliche Bitcoin-System im Detail tut.


### KA Wortschatzüberprüfung


Definieren Sie die folgenden, im vorherigen Abschnitt eingeführten Schlüsselbegriffe:



- Knotenpunkt
- [Mempool](https://planb.academy/resources/glossary/mempool)
- [Schwierigkeit](https://planb.academy/resources/glossary/difficulty) Ziel
- Block


**Diskutieren Sie in der Gruppe die Bedeutung einiger zusätzlicher Begriffe:**


Blockchain, Transaktion, Doppelausgabe, Byzantinisches Problem der Generäle, [Mining](https://planb.academy/resources/glossary/mining), Proof of Work (PoW), Hash Funktion, Block reward, Blockchain, Längste Kette, 51%-Angriff, Ausgabe, Ausgabesperre, Änderung, [Satoshis](https://planb.academy/resources/glossary/satoshi-sat), Öffentlicher/Privater Schlüssel, Address, Public-Key-[Kryptographie](https://planb.academy/resources/glossary/cryptography), [Digitale Signatur](https://planb.academy/resources/glossary/digital-signature), Wallet


# Einführung von BTCPay Server


<partId>9c8a2d0c-9ba1-5c39-874c-f9eaf1bba663</partId>


## Verständnis des BTCPay Server Anmeldebildschirms


<chapterId>14aad54c-9bd8-54f2-9455-178b8ae63408</chapterId>


### Arbeiten mit BTCPay Server


Das Ziel dieses Kursblocks ist es, ein allgemeines Verständnis der BTCPay Server Software zu erlangen. In einer gemeinsamen Umgebung wird empfohlen, der Demonstration des Kursleiters zu folgen und das BTCPay Server Kursbuch zu Rate zu ziehen, um dem Kursleiter zu folgen. Sie werden lernen, wie Sie einen Wallet mit verschiedenen Methoden erstellen können. Beispiele sind Hot Wallet-Setups und Hardware-Wallets, die über BTCPay Server Vault verbunden sind. Diese Ziele werden in der Demo-Umgebung erreicht, die von Ihrem Kursleiter angezeigt wird und zu der Sie Zugang haben.


Wenn Sie diesen Kurs selbst absolvieren, finden Sie unter https://directory.btcpayserver.org/filter/hosts eine Liste von Drittanbieter-Hosts für Demozwecke. Wir raten dringend davon ab, diese Drittanbieteroptionen als Produktionsumgebungen zu verwenden; sie dienen jedoch dem richtigen Zweck, um die Verwendung von Bitcoin und BTCPay Server einzuführen.


Als BTCPay Server Rockstar Trainee haben Sie vielleicht schon Erfahrung mit der Einrichtung eines Bitcoin Nodes. Dieser Kurs ist speziell auf den BTCPay Server Software Stack zugeschnitten.


Viele der Optionen in BTCPay Server gibt es in der einen oder anderen Form auch in anderer Bitcoin Wallet-bezogener Software.


### BTCPay Server Anmeldebildschirm


Wenn Sie in der Demo-Umgebung begrüßt werden, werden Sie aufgefordert, sich anzumelden oder ein Konto zu erstellen Server-Administratoren können die Funktion zur Erstellung neuer Konten aus Sicherheitsgründen deaktivieren. Die Logos und Schaltflächenfarben von BTCPay Server können geändert werden, da BTCPay Server eine Open-Source-Software ist. Ein Drittanbieter-Host kann die Software mit einem White-Label versehen und das gesamte Erscheinungsbild ändern.


![image](assets/en/001.webp)


### Fenster "Konto erstellen


Das Erstellen von Konten auf dem BTCPay-Server erfordert gültige E-Mail-Address-Strings; example@email.com wäre ein gültiger String für E-Mail.


Das Passwort muss mindestens 8 Zeichen lang sein, einschließlich Buchstaben, Zahlen und Zeichen. Nachdem Sie das Passwort einmal festgelegt haben, müssen Sie überprüfen, ob das Passwort mit dem im ersten Passwortfeld eingegebenen Passwort übereinstimmt.


Wenn die Felder E-Mail und Passwort korrekt ausgefüllt sind, klicken Sie auf die Schaltfläche "Konto erstellen". Dadurch werden die E-Mail und das Passwort auf der BTCPay Server-Instanz des Lehrers gespeichert.


![image](assets/en/002.webp)


**!Hinweis!**


Wenn Sie diesen Kurs eigenständig absolvieren, wird die Erstellung dieses Kontos wahrscheinlich auf einem Drittanbieter-Host erfolgen; daher betonen wir nochmals, dass diese nicht als Produktionsumgebungen, sondern nur zu Schulungszwecken verwendet werden sollten.


### Kontoerstellung durch BTCPay Server Administrator


Der Administrator der BTCPay Server-Instanz kann auch Konten für BTCPay Server erstellen. Der Administrator der BTCPay-Server-Instanz kann auf "Servereinstellungen" (1) klicken, dann auf die Registerkarte "Benutzer" (2) und auf die Schaltfläche "+ Benutzer hinzufügen" (3) oben rechts auf der Registerkarte "Benutzer". In Ziel (4.3) erfahren Sie mehr über die administrative Kontrolle von Konten.


![image](assets/en/003.webp)


Als Administrator benötigen Sie die E-Mail Address des Benutzers und legen ein Standardpasswort fest. Es wird empfohlen, dass der Administrator den Benutzer darüber informiert, dass er dieses Kennwort vor der Verwendung des Kontos aus Sicherheitsgründen ändern muss. Wenn der Administrator kein Kennwort festlegt und SMTP auf dem Server konfiguriert wurde, erhält der Benutzer eine E-Mail mit einem Einladungslink, um sein Konto zu erstellen und selbst ein Kennwort festzulegen.


### Beispiel


Wenn Sie den Kurs mit einem Ausbilder besuchen, folgen Sie dem vom Ausbilder angegebenen Link und erstellen Sie Ihr Konto in der Demo-Umgebung. Vergewissern Sie sich, dass Ihre E-Mail Address und Ihr Passwort sicher gespeichert sind; Sie benötigen diese Anmeldedaten für den Rest der Demo-Ziele in diesem Kurs.


Möglicherweise hat Ihr Ausbilder die E-Mail Address im Vorfeld gesammelt und einen Einladungslink vor dieser Übung verschickt. Prüfen Sie auf Anweisung Ihre E-Mail.


Wenn Sie den Kurs ohne Lehrer absolvieren, erstellen Sie Ihr Konto mit der BTCPay Server-Demoumgebung; gehen Sie zu


https://Mainnet.demo.btcpayserver.org/login.


Dieses Konto sollte nur für Demonstrations-/Schulungszwecke und niemals für geschäftliche Zwecke verwendet werden.


### Zusammenfassung der Fertigkeiten


In diesem Abschnitt haben Sie Folgendes gelernt:



- So erstellen Sie ein Konto auf einem gehosteten Server über den Interface.
- Wie ein Serveradministrator manuell Benutzer in den Servereinstellungen hinzufügen kann.


### Bewertung der Kenntnisse


#### KA Konzeptuelle Überprüfung


Nennen Sie Gründe, warum die Verwendung eines Demo-Servers für Produktionszwecke eine schlechte Idee ist.


## Benutzerkonto(s) verwalten


<chapterId>b58ca6ee-b7fc-5e81-a6aa-c8ff212b4c55</chapterId>


### Kontoführung auf dem BTCPay-Server


Nachdem ein Shop-Besitzer sein Konto erstellt hat, kann er es unten links auf der BTCPay-Server-Benutzeroberfläche verwalten. Unterhalb der Schaltfläche "Konto" befinden sich mehrere übergeordnete Einstellungen.



- Dunkel-/Hell-Modus.
- Sensible Informationen ausblenden.
- Konto verwalten.


![image](assets/en/004.webp)


### Dunkler und heller Modus


Benutzer von BTCPay Server können zwischen einer hellen und einer dunklen Version der Benutzeroberfläche wählen. Kundenseitige Seiten ändern sich nicht. Sie verwenden die vom Kunden bevorzugten Einstellungen für den dunklen oder hellen Modus.


### Sensible Informationen ausblenden Toggle


Die Schaltfläche Sensible Informationen ausblenden bietet einen schnellen und einfachen Layer der Sicherheit. Wann immer Sie Ihren BTCPay-Server bedienen müssen, Ihnen aber an einem öffentlichen Ort jemand über die Schulter schauen könnte, schalten Sie Sensible Informationen ausblenden ein, und alle Werte in BTCPay-Server werden ausgeblendet. Man kann Ihnen zwar über die Schulter schauen, aber die Werte, mit denen Sie arbeiten, sind nicht mehr sichtbar.


### Konto verwalten


Sobald das Benutzerkonto erstellt wurde, können Sie hier Passwörter, 2FA oder API-Schlüssel verwalten.


### Konto verwalten - Konto


Optional können Sie Ihr Konto mit einer anderen E-Mail Address aktualisieren. Um sicherzustellen, dass Ihre E-Mail Address korrekt ist, können Sie mit BTCPay Server eine Verifizierungs-E-Mail senden. Klicken Sie auf "Speichern", wenn der Benutzer eine neue E-Mail Address einstellt und bestätigt, dass die Überprüfung funktioniert hat. Der Benutzername bleibt derselbe wie bei der vorherigen E-Mail.


Ein Benutzer kann sich entscheiden, sein gesamtes Konto zu löschen. Dies kann durch Klicken auf die Schaltfläche "Löschen" auf der Registerkarte "Konto" erfolgen.


![image](assets/en/005.webp)


**!Hinweis!**


Nach der Änderung der E-Mail wird der Benutzername für das Konto nicht geändert. Die zuvor angegebene E-Mail Address bleibt der Anmeldename.


### Konto verwalten - Passwort


Ein Schüler möchte vielleicht sein Passwort ändern. Er kann dies tun, indem er die Registerkarte Passwort aufruft. Hier muss er sein altes Passwort eingeben und kann es durch ein neues ersetzen.


![image](assets/en/006.webp)


### Zwei-Faktoren-Authentifizierung (2fa)


Um die Folgen eines gestohlenen Passworts zu begrenzen, können Sie die Zwei-Faktor-Authentifizierung (2FA) verwenden, eine relativ neue Sicherheitsmethode. Sie können die Zwei-Faktor-Authentifizierung über das Konto verwalten und die Registerkarte für die Zwei-Faktor-Authentifizierung aktivieren. Nach der Anmeldung mit Ihrem Benutzernamen und Passwort müssen Sie einen zweiten Schritt durchführen.


BTCPay Server unterstützt zwei Methoden zur Aktivierung von 2FA: App-basierte 2FA (Authy, Google, Microsoft Authenticators) oder über Sicherheitsgeräte (FIDO2 oder LNURL Auth).


### Zwei-Faktoren-Authentifizierung - App-basiert


Je nach Betriebssystem Ihres Mobiltelefons (Android oder iOS) können Sie zwischen den folgenden Apps wählen;


1. Laden Sie einen Zwei-Faktor-Authentifikator herunter.


   - Authy für [Android](https://play.google.com/store/apps/details?id=com.authy.authy) oder [iOS](https://apps.apple.com/us/app/authy/id494168017)
   - Microsoft Authenticator für [Android](https://play.google.com/store/apps/details?id=com.azure.authenticator) oder [iOS](https://apps.apple.com/us/app/microsoft-authenticator/id983156458)
   - Google Authenticator für [Android](https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2&hl=e%C2%80) oder [iOS](https://apps.apple.com/us/app/google-authenticator/id388497605)

2. Nach dem Herunterladen und Installieren der Authenticator App.


   - Scannen Sie den vom BTCPay-Server bereitgestellten QR-Code
   - Oder geben Sie den vom BTCPay-Server generierten Schlüssel manuell in Ihre Authenticator-App ein.

3. Die Authenticator-App wird Ihnen einen eindeutigen Code mitteilen. Geben Sie den eindeutigen Code in BTCPay Server ein, um die Einrichtung zu bestätigen, und klicken Sie auf "Bestätigen", um den Vorgang abzuschließen.


![image](assets/en/007.webp)


### Zusammenfassung der Fertigkeiten


In diesem Abschnitt haben Sie Folgendes gelernt:



- Kontoverwaltungsoptionen und die verschiedenen Möglichkeiten, ein Konto auf einer BTCPay Server-Instanz zu verwalten.
- So richten Sie app-basierte 2FA ein.


### Bewertung der Kenntnisse


#### KA Konzeptuelle Überprüfung


Beschreiben Sie, wie App-basierte 2FA Ihr Konto schützen kann.


## Einen neuen Shop erstellen


<chapterId>463b3634-b49f-5512-a711-3b2e096fc2e0</chapterId>


### Assistent zum Erstellen Ihres Shops


Wenn sich ein neuer Benutzer bei BTCPay Server anmeldet, ist die Umgebung leer und benötigt einen ersten Shop. Der Einführungsassistent von BTCPay Server bietet dem Benutzer die Option "Erstellen Sie Ihren Store" (1). Ein Store kann als ein Zuhause für Ihre Bitcoin-Bedürfnisse angesehen werden. Ein neuer BTCPay Server-Knoten beginnt mit der Synchronisierung des Bitcoin mit dem Blockchain (2). Je nachdem, auf welcher Infrastruktur Sie BTCPay Server betreiben, kann dies zwischen einigen Stunden und ein paar Tagen dauern. Die aktuelle Version der Instanz wird in der unteren rechten Ecke der BTCPay-Server-Benutzeroberfläche angezeigt. Dies ist bei der Fehlersuche nützlich.


![image](assets/en/008.webp)


### Assistent zum Erstellen Ihres Shops


Wenn Sie diesen Kurs verfolgen, sehen Sie zunächst einen etwas anderen Bildschirm als auf der vorherigen Seite. Da Ihr Kursleiter die Demo-Umgebung vorbereitet hat, wurde der Bitcoin Blockchain bereits synchronisiert, so dass Sie den Synchronisierungsstatus der Knoten nicht sehen.


Ein Benutzer kann sich entscheiden, sein gesamtes Konto zu löschen. Dies kann durch Klicken auf die Schaltfläche "Löschen" auf der Registerkarte "Konto" erfolgen.


![image](assets/en/009.webp)


**!Hinweis!**


BTCPay Server-Konten können eine unbegrenzte Anzahl von Geschäften erstellen. Jeder Shop ist ein Wallet oder "Zuhause".


### Beispiel


Klicken Sie zunächst auf "Erstellen Sie Ihren Shop".


![image](assets/en/010.webp)


Dies wird Ihr erstes Home und Dashboard für die Verwendung von BTCPay Server erstellen.


(1) Nachdem Sie auf "Create your store" geklickt haben, werden Sie von BTCPay Server aufgefordert, einen Namen für den Shop anzugeben.


![image](assets/en/011.webp)


(2) Als Nächstes muss eine Standard-Speicherwährung festgelegt werden, entweder eine Fiat-Währung oder eine Währung, die auf Bitcoin oder Sats lautet. Für die Demo-Umgebung setzen wir sie auf USD.


![image](assets/en/012.webp)


(3) Als letzten Parameter bei der Einrichtung des Shops verlangt BTCPay Server, dass Sie eine "bevorzugte Preisquelle" festlegen, um den Bitcoin-Preis mit dem aktuellen Fiat-Preis zu vergleichen, damit Ihr Shop den korrekten Exchange-Kurs zwischen Bitcoin und der im Shop eingestellten Fiat-Währung anzeigt. Wir bleiben bei der Standardeinstellung im Demo-Beispiel und setzen diese auf den Kraken Exchange. BTCPay Server verwendet die Kraken-API, um die Exchange-Kurse zu überprüfen.


![image](assets/en/013.webp)


(4) Nachdem Sie diese Shop-Parameter festgelegt haben, klicken Sie auf die Schaltfläche "Erstellen" und BTCPay Server wird das Dashboard Ihres ersten Shops erstellen, wo der Assistent fortgesetzt wird.


![image](assets/en/014.webp)


Herzlichen Glückwunsch, Sie haben Ihr erstes Geschäft erstellt, und damit ist diese Übung abgeschlossen.


![image](assets/en/015.webp)


### Zusammenfassung der Fertigkeiten


In diesem Abschnitt haben Sie gelernt:



- Erstellen von Geschäften und Konfigurieren einer Standardwährung in Verbindung mit Preisquellenpräferenzen.
- Jeder "Store" ist ein neues Zuhause, das von anderen Stores auf dieser Installation von BTCPay Server getrennt ist.


# Einführung in die Sicherung von Bitcoin-Schlüsseln


<partId>25da22d8-fd37-51c5-af2a-58b9f3b046b2</partId>


## Verstehen der Bitcoin-Schlüsselerzeugung


<chapterId>d162735b-847b-578e-83b8-a044ab703ec5</chapterId>


### Wie werden Bitcoin-Schlüssel erzeugt?


Bitcoin-Geldbörsen erzeugen, wenn sie erstellt werden, einen so genannten "[seed](https://planb.academy/resources/glossary/seed)". Im letzten Ziel haben Sie einen "seed" erstellt. Die zuvor erzeugte Wortfolge ist auch als Mnemonic-Phrase bekannt. Der seed wird zur Ableitung individueller Bitcoin-Schlüssel verwendet und zum Senden oder Empfangen von Bitcoin genutzt. seed-Phrasen sollten niemals an Dritte oder nicht vertrauenswürdige Peers weitergegeben werden.


Die seed-Generierung erfolgt nach dem Industriestandard "Hierarchical Deterministic" (HD).


![image](assets/en/016.webp)


### Adressen


BTCPay Server ist auf generate einen neuen Address aufgebaut. Dadurch wird das Problem der Wiederverwendung von öffentlichen Schlüsseln oder Address gemildert. Die Verwendung desselben öffentlichen Schlüssels macht die Verfolgung Ihrer gesamten Zahlungshistorie sehr einfach. Wenn man sich die Schlüssel als einmalig verwendbare Gutscheine vorstellt, würde dies Ihre Privatsphäre erheblich verbessern. Wir verwenden auch Bitcoin-Adressen, die nicht mit öffentlichen Schlüsseln zu verwechseln sind.


Ein Address wird durch einen "Hashing-Algorithmus" aus dem öffentlichen Schlüssel abgeleitet Die meisten Geldbörsen und Transaktionen zeigen jedoch eher Adressen als diese öffentlichen Schlüssel an. Adressen sind im Allgemeinen kürzer als öffentliche Schlüssel und beginnen normalerweise mit "1", "3" oder "bc1", während öffentliche Schlüssel mit "02", "03" oder "04" beginnen.



- Adressen, die mit `1.....` beginnen, sind immer noch sehr gebräuchliche Adressen. Wie im Kapitel "Erstellen eines neuen Geschäfts" erwähnt, handelt es sich dabei um alte Adressen. Dieser Address-Typ ist für P2PKH-Transaktionen gedacht. P2Pkh verwendet die Base58-Kodierung, so dass bei Address die Groß- und Kleinschreibung eine Rolle spielt. Seine Struktur basiert auf dem öffentlichen Schlüssel mit einer zusätzlichen Ziffer als Identifikator.



- Adressen, die mit `bc1...` beginnen, werden langsam zu den sehr verbreiteten Adressen. Diese sind als (native) [SegWit](https://planb.academy/resources/glossary/segwit)-Adressen bekannt. Diese bieten eine bessere Gebührenstruktur als die anderen genannten Adressen. Native SegWit-Adressen verwenden die Bech32-Kodierung und lassen nur Kleinbuchstaben zu.



- Adressen, die mit `3...` beginnen, werden häufig noch von Börsen für Einzahlungsadressen verwendet. Diese Adressen werden im Kapitel "Erstellen einer neuen Filiale" erwähnt, umhüllte oder verschachtelte SegWit-Adressen. Sie können jedoch auch als "Multisig Address" verwendet werden. Wenn sie als SegWit Address verwendet werden, ergeben sich einige Einsparungen bei den [Transaktionsgebühren](https://planb.academy/resources/glossary/transaction-fees), allerdings weniger als bei den nativen SegWit. P2SH-Adressen verwenden die Base58-Kodierung. Dies macht sie, wie die alten Address, case-sensitiv.



- Adressen, die mit `2...` beginnen, sind Testnet-Adressen. Sie sind für den Empfang von Testnet Bitcoin (tBTC) gedacht. Sie sollten dies niemals verwechseln und Bitcoin an diese Adressen senden. Für Entwicklungszwecke können Sie generate ein Testnet Wallet. Es gibt online mehrere Möglichkeiten, Testnet Bitcoin zu erhalten. Kaufen Sie niemals Testnet Bitcoin. Testnet Bitcoin wird abgebaut. Dies könnte ein Grund für einen Entwickler sein, stattdessen Regtest zu verwenden. Dies ist eine Spielumgebung für Entwickler, der bestimmte Netzwerkkomponenten fehlen. Bitcoin ist jedoch für Entwicklungszwecke sehr nützlich.


### Öffentliche Schlüssel


Öffentliche Schlüssel werden heute in der Praxis weniger häufig verwendet. Mit der Zeit haben Bitcoin-Benutzer sie durch Adressen ersetzt. Es gibt sie aber immer noch und sie werden auch gelegentlich verwendet. Öffentliche Schlüssel sind im Allgemeinen viel längere Zeichenfolgen als Adressen. Genau wie bei Adressen beginnen sie mit einer bestimmten Kennung.



- Erstens sind "02..." und "03..." sehr standardmäßige Kennungen für öffentliche Schlüssel, die im SEC-Format kodiert sind. Diese können verarbeitet und in Empfangsadressen umgewandelt, zur Erstellung von multi-sig-Adressen oder zur Verifizierung einer Signatur verwendet werden. Die ersten Bitcoin-Transaktionen verwendeten öffentliche Schlüssel als Teil von P2PK-Transaktionen.



- HD-Wallets verwenden jedoch eine andere Struktur. [xpub](https://planb.academy/resources/glossary/xpub)...`, `ypub...` oder `zpub...` werden als erweiterte öffentliche Schlüssel, oder xpubs, bezeichnet. Diese Schlüssel werden zur Ableitung vieler öffentlicher Schlüssel als Teil des HD Wallet verwendet. Da Ihr xpub die Aufzeichnungen Ihrer gesamten Historie, d. h. vergangener und zukünftiger Transaktionen, enthält, sollten Sie diese niemals mit nicht vertrauenswürdigen Parteien teilen.


### Zusammenfassung der Fertigkeiten


In diesem Abschnitt haben Sie Folgendes gelernt:



- Die Unterschiede zwischen Adressen und öffentlichen Schlüsseldatentypen und die Vorteile der Verwendung von Adressen gegenüber öffentlichen Schlüsseln.


### Bewertung der Kenntnisse


Beschreiben Sie den Vorteil der Verwendung neuer Adressen für jede Transaktion im Vergleich zur Wiederverwendung von Address oder Methoden mit öffentlichen Schlüsseln.


## Sichern von Schlüsseln mit einem Hardware Wallet


<chapterId>c54a6d61-5a43-5fdb-93ae-c6750de9c612</chapterId>


### Aufbewahrung von Bitcoin-Schlüsseln


Nach der Erstellung einer seed-Phrase muss die in diesem Buch erstellte Liste von 12 bis 24 Wörtern ordnungsgemäß gesichert werden, da diese Wörter die einzige Möglichkeit sind, den Zugriff auf einen Wallet wiederherzustellen. Die Struktur von HD Wallets und die Art und Weise, wie Adressen deterministisch mit einem einzigen seed generiert werden, bedeutet, dass alle von Ihnen erstellten Adressen mit dieser einen Liste von Mnemonic-Wörtern gesichert werden, die Ihr seed oder Ihre Wiederherstellungsphrase darstellt.


Bewahren Sie Ihren Wiederherstellungssatz sicher auf. Wenn jemand darauf zugreift, insbesondere in böswilliger Absicht, kann er Ihr Geld bewegen. Bewahren Sie den seed sicher auf und bedenken Sie dabei, dass er auf Gegenseitigkeit beruht. Es gibt verschiedene Methoden zur Speicherung der privaten Bitcoin-Schlüssel, jede mit ihren eigenen Vor- und Nachteilen in Bezug auf Sicherheit, Datenschutz, Bequemlichkeit und physische Aufbewahrung. Aufgrund der Bedeutung [privater Schlüssel](https://planb.academy/resources/glossary/private-key) neigen Bitcoin-Nutzer dazu, diese Schlüssel selbst zu verwahren und sicher aufzubewahren, anstatt "Verwahrungsdienste" wie Banken zu nutzen. Je nach Benutzer müssen sie entweder eine Cold-Speicherlösung oder ein Hot-Wallet verwenden.


### Hot und Cold Speicherung von Bitcoin-Schlüsseln


In der Regel sind Bitcoin-Geldbörsen in Hot-Wallet oder Cold-Wallet denominiert. Die meisten Kompromisse liegen in der Bequemlichkeit, der Benutzerfreundlichkeit und den Sicherheitsrisiken. Jede dieser Methoden kann auch in einer Verwahrungslösung gesehen werden. Allerdings sind die Kompromisse hier meist sicherheits- und datenschutzbezogen und würden den Rahmen dieses Kurses sprengen.


### Hot Wallet


Hot-Geldbörsen sind die bequemste Art der Interaktion mit Bitcoin über Mobil-, Web- oder Desktop-Software. Das Wallet ist immer mit dem Internet verbunden und ermöglicht es den Benutzern, Bitcoin zu senden oder zu empfangen. Dies ist jedoch auch sein Schwachpunkt: Da das Wallet immer online ist, ist es nun anfälliger für Angriffe von Hackern oder Malware auf Ihrem Gerät. In BTCPay Server speichern Hot-Geldbörsen die privaten Schlüssel auf der Instanz. Jeder, der auf Ihren BTCPay Server-Speicher zugreift, könnte potenziell Geld von diesem Address stehlen, wenn er böswillig ist. Wenn BTCPay Server in einer gehosteten Umgebung läuft, sollten Sie dies immer in Ihrem Sicherheitsprofil berücksichtigen und in einem solchen Fall vorzugsweise keinen Hot verwenden. Wenn BTCPay Server auf Hardware installiert ist, die Ihnen gehört und die Sie sichern, sinkt das Risikoprofil erheblich, verschwindet aber nie ganz.


### Cold Wallet


Privatpersonen setzen ihren Bitcoin in einen [Cold Wallet](https://planb.academy/resources/glossary/cold-wallet) um, weil dieser die privaten Schlüssel vom Internet isolieren kann und sie so vor potenziellen Online-Bedrohungen schützt. Das Entfernen der Internetverbindung aus der Gleichung reduziert das Risiko von Malware, Spyware und SIM-Austausch. Man geht davon aus, dass die Cold-Speicherung der Hot-Speicherung in Bezug auf Sicherheit und Autonomie überlegen ist, vorausgesetzt, es werden angemessene Vorkehrungen getroffen, um den Verlust der privaten Bitcoin-Schlüssel zu verhindern. Die Cold-Speicherung eignet sich am besten für große Mengen von Bitcoin, die aufgrund der Komplexität der Wallet-Einrichtung nicht oft ausgegeben werden sollen.


Es gibt verschiedene Methoden zur Speicherung von Bitcoin-Schlüsseln in Cold-Speichern, von Papiergeldbörsen über Brain Wallets bis hin zu Hardware-Wallets oder, von Anfang an, einer Wallet-Datei. Die meisten Geldbörsen verwenden [BIP](https://planb.academy/resources/glossary/bip) 39, um den generate Satz zu speichern. Innerhalb der Bitcoin core-Software muss jedoch noch ein Konsens über die Verwendung dieses Begriffs erzielt werden. Die Bitcoin core-Software erstellt weiterhin eine Wallet.dat-Datei, die Sie an einem sicheren Offline-Speicherort aufbewahren müssen.


### Zusammenfassung der Fertigkeiten


In diesem Abschnitt haben Sie gelernt:



- Die Unterschiede zwischen Hot- und Cold-Geldbörsen in Bezug auf die Funktionalität und ihre Kompromisse.


### Wissensbewertung Konzeptuelle Überprüfung



- Was ist ein Wallet?



- Was ist der Unterschied zwischen den Brieftaschen Hot und Cold?



- Beschreiben Sie, was mit der "Erzeugung eines Wallet" gemeint ist?


## Verwendung der Tasten des Bitcoin


<chapterId>bff488de-5052-56e6-b696-97e896f762ae</chapterId>


### BTCPay-Server Wallet


BTCPay Server besteht aus den folgenden Standard-Wallet-Funktionen:



- Transaktionen
- Senden Sie
- Empfangen Sie
- Neu scannen
- Zahlungen ziehen
- Auszahlungen
- [PSBT](https://planb.academy/resources/glossary/psbt)
- Allgemeine Einstellungen


### Transaktionen


Administratoren können in der Transaktionsansicht die eingehenden und ausgehenden Transaktionen für die On-Chain Wallet sehen, die mit diesem spezifischen Speicher verbunden sind. Bei jeder Transaktion wird zwischen den empfangenen und gesendeten Beträgen unterschieden. Empfangene Transaktionen sind Green, und ausgehende Transaktionen sind rot. In der Transaktionsansicht des BTCPay-Servers sehen Administratoren auch eine Reihe von Standardetiketten.



| Transaktionstyp | Beschreibung                                        |
| --------------- | ---------------------------------------------------- |
| App             | Zahlung wurde über eine von einer App erstellte Rechnung empfangen |
| Rechnung        | Zahlung wurde über eine Rechnung empfangen           |
| [Payjoin](https://planb.academy/resources/glossary/payjoin)         | Nicht bezahlt, der Rechnungs-Timer ist noch nicht abgelaufen |
| Payjoin-offengelegt | [UTXO](https://planb.academy/resources/glossary/utxo) wurde über einen Payjoin-Vorschlag in einer Rechnung offengelegt |
| Zahlungsanforderung | Zahlung wurde über eine Zahlungsanforderung empfangen |
| Auszahlung      | Zahlung wurde über eine Auszahlung oder Rückerstattung gesendet |

### Wie man sendet


Die Sendefunktion des BTCPay-Servers sendet Transaktionen von Ihrem BTCPay-Server On-Chain Wallet. BTCPay Server ermöglicht mehrere Möglichkeiten, Ihre Transaktionen zu signieren, um Geld auszugeben. Eine Transaktion kann signiert werden mit;



- Hardware Wallet
- Geldbörsen, die PSBT unterstützen
- Privater HD-Schlüssel oder Recovery Seeds.
- Hot Wallet


#### Hardware Wallet


BTCPay Server verfügt über eine integrierte Hardware Wallet-Unterstützung, die es Ihnen ermöglicht, Ihr Hardware Wallet mit BTCPay Vault zu verwenden, ohne dass Informationen an Anwendungen oder Server von Drittanbietern weitergegeben werden. Die Hardware Wallet-Integration in BTCPay Server ermöglicht es Ihnen, Ihr Hardware Wallet zu importieren und eingehende Gelder mit einer einfachen Bestätigung auf Ihrem Gerät auszugeben. Ihre privaten Schlüssel verlassen nie das Gerät, und alle Gelder werden mit Ihrem Full node abgeglichen, sodass keine Daten nach außen dringen können.


#### Unterzeichnung mit einem Wallet, der PSBT unterstützt


PSBT (Partially Signed Bitcoin Transactions) ist ein Austauschformat für Bitcoin Transaktionen, die noch vollständig signiert werden müssen. PSBT wird von BTCPay Server unterstützt und kann mit kompatiblen Hardware- und Software-Wallets signiert werden.


Der Aufbau einer vollständig signierten Bitcoin-Transaktion erfolgt in folgenden Schritten:



- Ein PSBT wird mit bestimmten Ein- und Ausgängen, aber ohne Signaturen konstruiert
- Das exportierte PSBT kann von einem Wallet importiert werden, das dieses Format unterstützt
- Die Transaktionsdaten können mit dem Wallet geprüft und signiert werden
- Die signierte PSBT-Datei wird aus dem Wallet exportiert und in den BTCPay-Server importiert
- Der BTCPay-Server erzeugt die letzte Bitcoin-Transaktion
- Sie überprüfen das Ergebnis und senden es an das Netzwerk


#### Signieren mit HD Private Key oder Mnemonic seed


Wenn Sie vor der Verwendung von BTCPay Server eine Wallet erstellt haben, können Sie das Geld ausgeben, indem Sie Ihren privaten Schlüssel in ein entsprechendes Feld eingeben. Legen Sie einen korrekten "AccountKeyPath" in Wallet> Einstellungen fest, sonst können Sie nicht ausgeben.


#### Signieren mit einem Hot Wallet


Wenn Sie bei der Einrichtung Ihres Shops einen neuen Wallet erstellt und ihn als Hot aktiviert haben, wird er automatisch den auf einem Server gespeicherten seed zum Signieren verwenden.


### RBF (Replace-by-fee)


Replace-by-fee (RBF) ist eine Funktion des Bitcoin-Protokolls, die es Ihnen ermöglicht, eine zuvor gesendete Transaktion zu ersetzen (während sie noch unbestätigt ist). Dies ermöglicht es, den Transaktionsfingerabdruck Ihres Wallet nach dem Zufallsprinzip zu verändern oder ihn durch einen höheren Gebührensatz zu ersetzen, um die Transaktion in der Warteschlange der Bestätigungspriorität (Mining) nach oben zu verschieben. Dadurch wird die ursprüngliche Transaktion effektiv ersetzt, da der höhere Gebührensatz Vorrang hat, und sobald er bestätigt ist, wird die ursprüngliche Transaktion ungültig (keine Doppelausgaben).


Drücken Sie die Schaltfläche "Erweiterte Einstellungen", um die Optionen des RBF anzuzeigen.


![image](assets/en/017.webp)



- Randomize for higher privacy (Randomisierung für mehr Datenschutz) ermöglicht die automatische Ersetzung der Transaktion, um den Fingerabdruck der Transaktion zu randomisieren.
- Ja, Transaktion für RBF kennzeichnen und explizit ersetzen (nicht standardmäßig ersetzt, nur durch Eingabe)
- Nein, erlauben Sie nicht, dass die Transaktion ersetzt wird.


### Coin Auswahl


Die Coin-Auswahl ist eine fortschrittliche Funktion zur Verbesserung der Privatsphäre, mit der Sie die Münzen auswählen können, die Sie ausgeben möchten, wenn Sie eine Transaktion durchführen. Zum Beispiel können Sie mit Münzen bezahlen, die frisch aus einer gemeinsamen Mischung stammen.


Die Coin-Auswahl funktioniert nativ mit der Wallet-Etikettenfunktion. Damit können Sie eingehende Mittel für eine reibungslosere UTXO-Verwaltung und -Ausgabe kennzeichnen.


BTCPay Server unterstützt BIP-329 für die Etikettenverwaltung. Wenn Sie von einem Wallet umziehen, der BIP-329 unterstützt, und bereits [Labels](https://planb.academy/resources/glossary/label) gesetzt haben, erkennt und importiert BTCPay Server diese automatisch. Bei der Migration von Servern können diese Informationen auch exportiert und in die neue Umgebung importiert werden.


### Wie man empfängt


Wenn Sie auf die Schaltfläche "Empfangen" in BTCPay Server klicken, wird ein unbenutzter Address generiert, der für den Empfang von Zahlungen verwendet werden kann. Administratoren können auch generate einen neuen Address erstellen, indem sie einen neuen "Invoice" anlegen


BTCPay Server wird Sie immer auffordern, generate das nächste verfügbare Address zu verwenden, um die Wiederverwendung von Address zu verhindern. Nach einem Klick auf "generate nächster verfügbarer BTC Address", generiert BTCPay Server einen neuen Address und QR. Außerdem können Sie zur besseren Verwaltung Ihrer Adressen direkt ein Label auf den Address setzen.


![image](assets/en/018.webp)


![image](assets/en/019.webp)


#### Neu scannen


Die Rescan-Funktion stützt sich auf Bitcoin core 0.17.0's "Scantxoutset", um den aktuellen Status des Blockchain (genannt UTXO Set) nach Münzen zu scannen, die zum konfigurierten Ableitungsschema gehören. Ein Wallet-Rescan behebt zwei häufige Probleme, auf die BTCPay-Server-Benutzer häufig stoßen.


1. Problem der Lückenbegrenzung - Die meisten Geldbörsen von Drittanbietern sind leichte Geldbörsen, die sich einen Knoten mit vielen Benutzern teilen. Leichte und Full node-abhängige Wallets begrenzen die Anzahl (normalerweise 20) der Adressen ohne Guthaben, die sie auf dem Blockchain verfolgen, um Leistungsprobleme zu vermeiden. BTCPay Server generiert einen neuen Address für jeden Invoice. Nachdem BTCPay Server 20 aufeinanderfolgende unbezahlte Rechnungen generiert hat, hört der externe Wallet auf, die Transaktionen abzurufen, vorausgesetzt, es sind keine neuen Transaktionen aufgetreten. Ihr externer Wallet wird sie nicht mehr anzeigen, wenn die Rechnungen am 21., 22. usw. bezahlt werden. Der interne Wallet des BTCPay-Servers hingegen verfolgt jeden Address, den er generiert, zusammen mit einem deutlich höheren Gap-Limit. Er ist nicht von einer dritten Partei abhängig und kann immer einen korrekten Saldo ausweisen.

2. Die Gap-Limit-Lösung - Wenn Ihr [externer/existierender Wallet](https://docs.btcpayserver.org/WalletSetup/#use-an-existing-Wallet) die Konfiguration des Gap-Limits zulässt, ist die einfache Lösung, es zu erhöhen. Die Mehrheit der Geldbörsen erlaubt dies jedoch nicht. Die einzigen uns bekannten Geldbörsen, die derzeit eine Gap-Limit-Konfiguration unterstützen, sind Electrum, Wasabi und Sparrow wallet. Leider werden Sie bei vielen anderen Geldbörsen wahrscheinlich auf ein Problem stoßen. Für die beste Benutzererfahrung und den besten Datenschutz sollten Sie den internen Wallet des BTCPay-Servers anstelle von externen Wallets verwenden.


#### BTCPay Server verwendet "mempoolfullrbf=1"


BTCPay Server verwendet "mempoolfullrbf=1"; wir haben dies als Standardeinstellung zu Ihrer BTCPay Server-Einrichtung hinzugefügt. Allerdings können Sie diese Funktion auch selbst deaktivieren. Ohne "mempoolfullrbf=1" würde der Händler erst nach der Bestätigung erfahren, wenn ein Kunde eine Zahlung mit einer Transaktion, die nicht RBF signalisiert, doppelt ausgibt.


Ein Administrator möchte diese Einstellung möglicherweise deaktivieren. Mit der folgenden Zeichenfolge können Sie die Standardeinstellung ändern.


```
BTCPAYGEN_EXCLUDE_FRAGMENTS="$BTCPAYGEN_EXCL UDE_FRAGMENTS;opt-mempoolfullrbf"
. btcpay-setup.sh -i
```


### BTCPay Server Wallet Einstellungen


Die Wallet-Einstellungen in BTCPay Server bieten einen klaren und präzisen Überblick über die allgemeinen Einstellungen Ihres Wallet. Alle diese Einstellungen sind vorausgefüllt, wenn das Wallet mit BTCPay Server erstellt wurde.


![image](assets/en/020.webp)


Die Wallet-Einstellungen in BTCPay Server bieten einen klaren und präzisen Überblick über die allgemeinen Einstellungen Ihres Wallet. Alle diese Einstellungen sind vorausgefüllt, wenn das Wallet mit BTCPay Server erstellt wurde. Die Wallet-Einstellungen von BTCPay Server beginnen mit dem Wallet-Status. Handelt es sich um einen reinen Watch- oder einen Hot-Wallet? Je nach Wallet-Typ können unterschiedliche Maßnahmen ergriffen werden, z. B. das erneute Scannen des Wallet auf fehlende Transaktionen, das Entfernen alter Transaktionen aus der Historie, das Registrieren des Wallet für Zahlungslinks oder das Ersetzen und Löschen des aktuellen Wallet, der mit dem Shop verbunden ist. In den Wallet-Einstellungen von BTCPay Server können Administratoren zur besseren Wallet-Verwaltung ein Label für den Wallet festlegen. Hier kann der Administrator auch das Ableitungsschema, den Kontoschlüssel (xpub), den Fingerabdruck und den Keypath sehen. Zahlungen in den Wallet-Einstellungen haben nur zwei Haupteinstellungen. Die Zahlung ist ungültig, wenn die Transaktion nicht innerhalb (festgelegter Minuten) nach Ablauf von Invoice bestätigt wird. Der Invoice gilt als bestätigt, wenn die Zahlungstransaktion X Bestätigungen erhalten hat. Administratoren können auch einen Schalter setzen, um empfohlene Gebühren auf dem Zahlungsbildschirm anzuzeigen oder ein manuelles Bestätigungsziel in der Anzahl der Blöcke festzulegen.


![image](assets/en/021.webp)


**!Hinweis!**


Wenn Sie diesen Kurs eigenständig absolvieren, wird die Erstellung dieses Kontos wahrscheinlich auf einem fremden Host erfolgen. Daher schlagen wir erneut vor, dass diese nicht als Produktionsumgebungen verwendet werden sollten, sondern nur zu Schulungszwecken.


### Beispiel


#### Einrichten eines Bitcoin Wallet in BTCPay Server


BTCPay Server bietet zwei Methoden zum Einrichten eines Wallet. Eine Möglichkeit ist der Import eines bestehenden Bitcoin Wallet. Der Import kann durch den Anschluss eines Hardware Wallet, den Import einer Wallet-Datei, die Eingabe eines erweiterten öffentlichen Schlüssels, das Scannen des QR-Codes eines Wallet oder - am ungünstigsten - durch die manuelle Eingabe eines zuvor erstellten Wallet Recovery seed erfolgen. In BTCPay Server ist es auch möglich, eine neue Wallet zu erstellen. Es gibt zwei Möglichkeiten, BTCPay Server bei der Erstellung einer neuen Wallet zu konfigurieren.


Die Option Hot Wallet in BTCPay Server ermöglicht Funktionen wie "PayJoin" oder "Liquid". Es gibt jedoch einen Nachteil: Die für diese Wallet generierte Wiederherstellungs-seed wird auf dem Server gespeichert, wo jeder mit Admin-Kontrolle sie abrufen kann. Da Ihr privater Schlüssel von Ihrer Wiederherstellungs-seed abgeleitet ist, könnte ein böswilliger Akteur Zugang zu Ihren aktuellen und zukünftigen Geldern erhalten!


Um dieses Risiko in BTCPay Server zu verringern, kann ein Administrator den Wert in Servereinstellungen > Richtlinien > "Nicht-Administratoren das Erstellen von Hot-Brieftaschen für ihre Geschäfte erlauben" auf "nein" setzen, da dies der Standardwert ist. Um die Sicherheit dieser Hot-Brieftaschen zu erhöhen, sollte der Serveradministrator die 2FA-Authentifizierung für Konten aktivieren, die Hot-Brieftaschen haben dürfen. Die Speicherung von privaten Schlüsseln auf einem öffentlichen Server ist eine gefährliche Praxis und birgt erhebliche Risiken. Einige davon ähneln den Lightning Network-Risiken (siehe das nächste Kapitel über Lightning Network-Risiken).


Die zweite Möglichkeit, die BTCPay Server zur Generierung eines neuen Wallet bietet, ist die Erstellung eines Watch-only wallet. BTCPay Server wird generate Ihre privaten Schlüssel einmal. Nachdem der Benutzer bestätigt hat, dass er seine seed Phrase aufgeschrieben hat, löscht BTCPay Server die privaten Schlüssel vom Server. Infolgedessen hat Ihr Geschäft jetzt einen Watch-only wallet, der mit ihm verbunden ist. Um die erhaltenen Gelder auf Ihrem Watch-only wallet auszugeben, lesen Sie bitte das Kapitel "Senden", indem Sie entweder den BTCPay Server Vault, PSBT (Partially Signed Bitcoin Transaction) oder, was am wenigsten empfohlen wird, die seed Phrase manuell eingeben.


Im letzten Teil haben Sie einen neuen "Store" erstellt. Der Installationsassistent fährt mit der Aufforderung fort, "einen Wallet einzurichten" oder "einen Lightning-Knoten einzurichten". In diesem Beispiel folgen Sie dem Prozess des Assistenten "Einrichten eines Wallet" (1).


![image](assets/en/022.webp)


Nachdem Sie auf "Wallet einrichten" geklickt haben, fragt Sie der Assistent, wie Sie fortfahren möchten. BTCPay Server bietet nun die Möglichkeit, einen bestehenden Bitcoin mit Ihrem neuen Shop zu verbinden. Wenn Sie keinen Wallet haben, schlägt BTCPay Server vor, einen neuen zu erstellen. In diesem Beispiel werden die Schritte für "Erstellen eines neuen Wallet" (2) ausgeführt. Folgen Sie den Schritten, um zu erfahren, wie Sie "einen bestehenden Wallet anschließen" (1).


![image](assets/en/023.webp)


**!Hinweis!**


Wenn Sie diesen Kurs in einem Klassenzimmer absolvieren, beachten Sie bitte, dass das aktuelle Beispiel und seed, die wir erstellt haben, nur für Ausbildungszwecke dienen. In den Übungen zu diesen Adressen sollte nie ein größerer Betrag als erforderlich verwendet werden.


(1) Fahren Sie mit dem Assistenten "Neues Wallet" fort, indem Sie auf die Schaltfläche "Ein neues Wallet erstellen" klicken.


![image](assets/en/024.webp)


(2) Nachdem Sie auf "Create a new Wallet" geklickt haben, bietet das nächste Fenster des Assistenten die Optionen "Hot Wallet" und "Watch-only wallet" Wenn Sie mit einem Ausbilder zusammenarbeiten, ist Ihre Umgebung eine gemeinsame Demo, und Sie können nur ein Watch-only wallet erstellen. Beachten Sie den Unterschied zwischen den beiden Abbildungen unten. Wenn Sie sich in der Demo-Umgebung befinden und dem Ausbilder folgen, erstellen Sie ein "Watch-only wallet" und fahren mit dem Assistenten "Neues Wallet" fort.


![image](assets/en/025.webp)


![image](assets/en/026.webp)


(3) Fahren Sie mit dem neuen Wallet-Assistenten fort, und Sie befinden sich nun im Abschnitt BTC Watch-only wallet erstellen. Hier können wir den Wallet "Address-Typ" festlegen BTCPay Server erlaubt es Ihnen, Ihren bevorzugten Address-Typ zu wählen; zum Zeitpunkt der Erstellung dieses Kurses wird immer noch empfohlen, bech32-Adressen zu verwenden. Sie können mehr über Adressen im ersten Kapitel dieses Teils erfahren.



- SegWit (bech32)
  - Native SegWit-Adressen beginnen mit "bc1q".
  - Beispiel: "bc1qXXXXXXXXXXXXXXXXXXXXXXXXXX"
- Erbe
  - Legacy-Adressen sind Adressen, die mit der Zahl "1" beginnen.
  - Beispiel: "15e15hXXXXXXXXXXXXXXXXXXXXXX"
- Taproot (für fortgeschrittene Benutzer)
  - Taproot-Adressen beginnen mit "bc1p".
  - Beispiel: "bc1pXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
- SegWit verpackt
  - SegWit-umhüllte Adressen beginnen mit "3".
  - Beispiel: "37BBXXXXXXXXXXXXXXXXX"


Wählen Sie SegWit (empfohlen) als Ihren bevorzugten Wallet Address-Typ.


![image](assets/en/027.webp)


(4) Beim Einstellen der Parameter für das Wallet erlaubt BTCPay Server den Benutzern, ein optionales passphrase über BIP39 einzustellen; achten Sie darauf, Ihr Passwort zu bestätigen.


![image](assets/en/028.webp)


(5) Nachdem Sie den Wallet-Typ festgelegt und möglicherweise einige erweiterte Optionen eingestellt haben, klicken Sie auf Erstellen, und BTCPay Server wird Ihr neues generate erstellen. Beachten Sie, dass dies der letzte Schritt vor der Erstellung Ihrer seed-Phrase ist. Stellen Sie sicher, dass Sie dies nur in einer Umgebung tun, in der jemand nicht in der Lage ist, die seed-Phrase durch einen Blick auf Ihren Bildschirm zu stehlen.


![image](assets/en/029.webp)


(6) Im folgenden Bildschirm des Assistenten zeigt Ihnen BTCPay Server die Recovery seed Phrase für Ihre neu generierte Wallet; dies sind die Schlüssel zur Wiederherstellung Ihrer Wallet und zur Signierung von Transaktionen. BTCPay Server generiert eine seed-Phrase mit 12 Wörtern. Diese Wörter werden nach diesem Einrichtungsbildschirm vom Server gelöscht. Dieser Wallet ist eigentlich ein Watch-only wallet. Es wird empfohlen, diese seed-Phrase nicht digital oder als Foto zu speichern. Die Benutzer können im Assistenten nur weitergehen, wenn sie aktiv bestätigen, dass sie ihren seed-Satz aufgeschrieben haben.


![image](assets/en/030.webp)


(7) Nachdem Sie auf Fertig geklickt und den neu generierten Bitcoin-seed-Satz gesichert haben, aktualisiert der BTCPay-Server Ihren Shop mit dem angehängten neuen Wallet und ist bereit, Zahlungen zu empfangen. In der Benutzer-Interface im linken Navigationsmenü ist die Bitcoin nun hervorgehoben und unter der Wallet aktiviert.


![image](assets/en/031.webp)


### Beispiel: Aufschreiben eines seed-Satzes


Dies ist ein besonders sicherer Zeitpunkt für die Verwendung von Bitcoin. Wie bereits erwähnt, sollten nur Sie Zugang zu Ihrem seed-Satz haben oder diesen kennen. Da Sie einen Kursleiter und ein Klassenzimmer begleiten, sollte der generierte seed nur in diesem Kurs verwendet werden. Zu viele Faktoren, einschließlich neugieriger Blicke von Mitschülern, unsichere Systeme und andere, machen diese Schlüssel nur lehrreich und nicht vertrauenswürdig. Die erzeugten Schlüssel sollten jedoch für Kursbeispiele aufbewahrt werden.


Die erste Methode, die wir in dieser Situation anwenden werden und die auch die unsicherste ist, ist das Aufschreiben der seed-Phrase in der richtigen Reihenfolge. Eine seed-Phrasenkarte ist in den Kursunterlagen enthalten, die den Studenten zur Verfügung gestellt werden, oder kann auf dem BTCPay Server GitHub gefunden werden. Wir werden diese Karte verwenden, um die im vorherigen Schritt generierten Wörter aufzuschreiben. Achten Sie darauf, sie in der richtigen Reihenfolge aufzuschreiben. Nachdem Sie sie aufgeschrieben haben, vergleichen Sie sie mit den Angaben der Software, um sicherzustellen, dass Sie sie in der richtigen Reihenfolge aufgeschrieben haben. Sobald Sie sie aufgeschrieben haben, klicken Sie auf das Kontrollkästchen, um zu bestätigen, dass Sie Ihren seed-Satz richtig aufgeschrieben haben.


### Beispiel: Speichern eines seed-Satzes auf einem Hardware Wallet


In diesem Kurs geht es um die Speicherung eines seed-Satzes auf einem Hardware Wallet. Die Teilnahme an diesem Kurs mit einem Ausbilder könnte manchmal ein solches Gerät beinhalten. In den Kursunterlagen wurde eine Liste von Hardware-Geldbörsen zusammengestellt, die für diese Übung geeignet sind.


In diesem Beispiel werden wir den BTCPay Server Tresor und einen Blockstream Jade Hardware Wallet verwenden.


Sie können auch eine Videoanleitung für den Anschluss eines Hardware Wallet verwenden.

:::video id=8e61664b-e0c0-416d-8ef9-b631bf28ec4d:::


BTCPay Server Vault herunterladen: https://github.com/btcpayserver/BTCPayServer.Vault/releases


Vergewissern Sie sich, dass Sie die richtigen Dateien für Ihr spezifisches System herunterladen. Windows-Benutzer sollten das Paket [BTCPayServerVault-2.0.5-setup.exe](https://github.com/btcpayserver/BTCPayServer.Vault/releases/download/Vault%2Fv2.0.5/BTCPayServerVault-2.0.5-setup.exe) herunterladen, Mac-Benutzer das Paket [BTCPayServerVault-osx-x64-2.0.5.dmg](https://github.com/btcpayserver/BTCPayServer.Vault/releases/download/Vault%2Fv2.0.5/BTCPayServerVault-osx-x64-2.0.5.dmg), und Linux-Benutzer sollten [BTCPayServerVault-Linux-2.0.5.tar.gz](https://github.com/btcpayserver/BTCPayServer.Vault/releases/download/Vault%2Fv2.0.5/BTCPayServerVault-Linux-2.0.5.tar.gz) herunterladen


Nach der Installation von BTCPay Server Vault starten Sie die Software, indem Sie auf das Symbol auf Ihrem Desktop klicken. Wenn BTCPay Server Vault ordnungsgemäß installiert ist und zum ersten Mal gestartet wird, fragt es nach der Erlaubnis, mit Webanwendungen verwendet zu werden. Sie werden aufgefordert, den Zugriff auf den spezifischen BTCPay Server, mit dem Sie arbeiten, zu erlauben. Akzeptieren Sie diese Bedingungen. BTCPay Server Vault sucht nun nach dem Hardware-Gerät. Sobald das Gerät gefunden wurde, erkennt BTCPay Server, dass Vault ausgeführt wird und Ihr Gerät abgerufen hat.


**!Hinweis!**


Geben Sie Ihre SSH-Schlüssel oder Ihr Server-Administratorkonto nicht an andere Personen als die Administratoren weiter, wenn Sie einen Hot Wallet verwenden. Jeder, der Zugriff auf diese Konten hat, hat auch Zugriff auf die Mittel im Hot Wallet.


### Zusammenfassung der Fertigkeiten


In diesem Abschnitt haben Sie Folgendes gelernt:



- Die Transaktionsansicht des Bitcoin Wallet und seine verschiedenen Einstufungen.
- Beim Senden von einem Bitcoin Wallet stehen verschiedene Optionen zur Verfügung, von Hardware bis hin zu Hot Geldbörsen.
- Das Gap-Limit-Problem, das bei den meisten Geldbörsen auftritt, und wie man es beheben kann.
- Wie man generate ein neues Bitcoin Wallet innerhalb des BTCPay Servers erstellt, einschließlich der Speicherung der Schlüssel in einem Hardware Wallet und der Sicherung der Recovery Phrase.


In diesem Ziel haben Sie gelernt, wie man generate ein neues Bitcoin Wallet innerhalb des BTCPay-Servers erstellt. Wir haben uns noch nicht damit befasst, wie man diese Schlüssel sichert oder verwendet. In einem kurzen Überblick über dieses Ziel haben Sie gelernt, wie Sie den ersten Shop einrichten. Sie haben gelernt, wie man generate eine Bitcoin Recovery seed Phrase erstellt.


### Wissensbewertung Praktische Überprüfung


Beschreiben Sie eine Methode zur Erzeugung von Schlüsseln und ein Schema zu deren Sicherung sowie die Nachteile/Risiken des Sicherheitsschemas.


## BTCPay Server Lightning Wallet


<chapterId>1bbece7e-0197-57e6-a93a-561cf384d946</chapterId>


Wenn ein Serveradministrator eine neue BTCPay Server-Instanz einrichtet, kann er eine Lightning Network-Implementierung wie LND, Core Lightning oder Eclair einrichten; genauere Anweisungen zur Installation finden Sie im Teil Konfiguration von BTCPay Server.


Die Verbindung eines Lightning-Knotens mit Ihrem BTCPay-Server funktioniert über einen benutzerdefinierten Knoten, wenn Sie ein Klassenzimmer besuchen. Ein Benutzer, der kein Server-Administrator auf BTCPay Server ist, kann den internen Lightning-Knoten standardmäßig nicht verwenden. Dies dient dazu, den Serverbesitzer vor dem Verlust seiner Gelder zu schützen. Server-Administratoren können ein Plugin installieren, um den Zugriff auf ihren Lightning-Knoten über LNBank zu ermöglichen; dies ist jedoch nicht Gegenstand dieses Buches. Weitere Informationen zu LNBank finden Sie auf der offiziellen Plugin-Seite.


### Internen Knoten verbinden (Server-Administrator)


Der Server-Administrator kann den internen Lightning-Knoten von BTCPay Server verwenden. Unabhängig von der Lightning-Implementierung ist die Verbindung zum internen Lightning-Knoten identisch.


Gehen Sie zu einem früheren Einrichtungsspeicher, und klicken Sie im linken Menü auf den Wallet "Lightning". BTCPay Server bietet zwei Einrichtungsmöglichkeiten: Verwendung des internen Knotens (standardmäßig nur Server-Administrator) oder eines benutzerdefinierten Knotens (externe Verbindung). Server-Administratoren können auf die Option "Internen Knoten verwenden" klicken. Es ist keine weitere Konfiguration erforderlich. Klicken Sie auf die Schaltfläche "Speichern" und beachten Sie die Meldung "BTC Lightning node updated". Der Shop hat nun erfolgreich Lightning Network-Fähigkeiten erhalten.


### Externen Knoten verbinden (Server-Benutzer/Speicherbesitzer)


Standardmäßig ist es Ladenbesitzern nicht erlaubt, den Lightning Node des Serveradministrators zu verwenden. Die Verbindung muss zu einem externen Knoten hergestellt werden, entweder zu einem Knoten, der dem Shop-Besitzer gehört, bevor er einen BTCPay-Server einrichtet, zu einem LNBank-Plugin, wenn es vom Server-Administrator zur Verfügung gestellt wird, oder zu einer Verwahrungslösung wie Alby.


Gehen Sie zu einem bereits eingerichteten Shop und klicken Sie im linken Menü unter Geldbörsen auf "Blitz". Da Ladenbesitzer den internen Knoten standardmäßig nicht verwenden dürfen, ist diese Option ausgegraut. Die Verwendung eines benutzerdefinierten Knotens ist die einzige standardmäßig verfügbare Option für Shop-Besitzer.


BTCPay Server benötigt Verbindungsinformationen; die vorgefertigte (oder Depotlösung) wird diese Informationen speziell für eine Lightning-Implementierung liefern. Innerhalb des BTCPay Servers können Store-Besitzer die folgenden Verbindungen nutzen;



- C-lightning über TCP- oder Unix-Domainsocket-Verbindung.
- Blitzaufladung über HTTPS
- Eclair über HTTPS
- LND über den REST-Proxy
- LNDhub über die REST-API


![image](assets/en/032.webp)


Klicken Sie auf "Verbindung testen", um sicherzustellen, dass Sie die Verbindungsdetails korrekt eingegeben haben. Nachdem die Verbindung als gut bestätigt wurde, klicken Sie auf "Speichern" und BTCPay Server zeigt an, dass der Shop mit einem Lightning-Knoten aktualisiert wurde.


### Verwaltung des internen Lightning-Knotens LND (Server-Administrator)


Nach dem Anschluss des internen Lightning-Knotens werden Server-Administratoren neue Kacheln auf dem Dashboard bemerken, die speziell für Lightning-Informationen gedacht sind.



- Lightning Balance
- BTC in Kanälen
  - BTC-Öffnungskanäle
  - BTC lokaler Saldo
  - BTC-Fernguthaben
  - BTC schließt Kanäle
- BTC On-Chain
  - BTC bestätigt
  - BTC unbestätigt
  - BTC reserviert
- Blitzdienste
  - Ride the Lightning (RTL).


Mit einem Klick auf das Lightning-Logo in der Kachel "Lightning-Dienste" oder auf "Lightning" unterhalb der Geldbörsen im linken Menü gelangen Server-Administratoren zu RTL für die Verwaltung der Lightning-Knoten.


**Anmerkung!**


Verbindung zum internen Lightning Node schlägt fehl - Wenn die interne Verbindung fehlschlägt, bestätigen Sie dies:


1. Der Bitcoin On-Chain-Knoten ist vollständig synchronisiert

2. Der interne Blitzknoten ist "Aktiviert" unter "Blitz" > "Einstellungen" > "BTC Blitzeinstellungen"


Wenn Sie nicht in der Lage sind, eine Verbindung zu Ihrem Lightning-Knoten herzustellen, können Sie versuchen, Ihren Server neu zu starten, oder lesen Sie weitere Details in der offiziellen Dokumentation des BTCPay-Servers; https://docs.btcpayserver.org/Troubleshooting/. Sie können keine Lightning-Zahlungen in Ihrem Shop akzeptieren, bis Ihr Lightning-Knoten "Online" ist. Versuchen Sie, Ihre Lightning-Verbindung zu testen, indem Sie auf den Link "Public Node Info" klicken.


### Blitz Wallet


Unter der Option Lightning Wallet in der linken Menüleiste finden Server-Administratoren einfachen Zugang zu RTL, ihren öffentlichen Knotenpunkt-Informationen und Lightning-Einstellungen, die für ihren BTCPay Server Store spezifisch sind.


#### Interne Knoteninformationen


Serveradministratoren können auf die internen Knoteninformationen klicken, um ihren Serverstatus (Online/Offline) und die Verbindungszeichenfolge für Clearnet oder [Tor](https://planb.academy/resources/glossary/tor) anzuzeigen.


![image](assets/en/033.webp)


#### Verbindung ändern


Um den externen Lightning-Knoten zu ändern, gehen Sie zu "Lightning Settings" und klicken Sie auf "Change connection" (neben "Public Node info"). Dadurch wird die bestehende Einrichtung zurückgesetzt. Geben Sie die neuen Node-Details ein, klicken Sie auf "Speichern", und der Store wird entsprechend aktualisiert.


![image](assets/en/034.webp)


#### Dienstleistungen


Wenn der Serveradministrator beschließt, mehrere Dienste für die Lightning-Implementierung zu installieren, werden diese hier aufgeführt. Bei einer Standard-LND-Implementierung steht den Administratoren Ride The Lightning (RTL) als Standardwerkzeug für die Knotenverwaltung zur Verfügung.


#### BTC Lightning Wallet Einstellungen


Nach dem Hinzufügen des Lightning-Knotens zum Shop in einem früheren Schritt können Shop-Besitzer immer noch wählen, ob sie ihn für ihren Shop deaktivieren möchten, indem sie den Umschalter oben in den Lightning-Einstellungen verwenden.


![image](assets/en/035.webp)


#### Lightning Zahlungsoptionen


Ladenbesitzer können die folgenden Parameter einstellen, um das Lightning-Erlebnis für ihre Kunden zu verbessern.



- Anzeige der Blitzzahlungsbeträge in Satoshis.
- Hinzufügen von Hop-Hints für private Kanäle zum Lightning Invoice.
- Vereinheitlichen Sie On-Chain- und Lightning-Zahlungs-URL/QR-Codes an der Kasse.
- Legen Sie eine Beschreibungsvorlage für Blitzrechnungen fest.


#### LNURL


Shop-Betreiber können wählen, ob sie LNURL verwenden oder nicht. Eine Lightning Network-URL oder LNURL ist ein vorgeschlagener Standard für die Interaktion zwischen Lightning Payer und Zahlungsempfänger. Kurz gesagt, eine LNURL ist eine bech32-kodierte URL mit dem Präfix LNURL. Es wird erwartet, dass der Lightning Wallet die URL dekodiert, die URL kontaktiert und ein JSON-Objekt mit weiteren Anweisungen erwartet, vor allem ein Tag, das das Verhalten der LNURL definiert.



- LNURL aktivieren
- LNURL Klassischer Modus
  - Für Wallet Kompatibilität, Bech32 verschlüsselt (klassisch) vs. Klartext URL (demnächst)
- Erlauben Sie dem Zahlungsempfänger, einen Kommentar abzugeben.


### Beispiel 1


#### Verbindung zu Lightning mit dem internen Knoten (Administrator)


Diese Option ist nur verfügbar, wenn Sie der Administrator dieser Instanz sind oder wenn der Administrator die Standardeinstellungen so geändert hat, dass Benutzer den internen Blitzknoten verwenden können.


Klicken Sie als Administrator auf den Lightning Wallet in der linken Menüleiste. BTCPay Server fordert Sie auf, eine von zwei Optionen für den Anschluss eines Lightning-Knotens auszuwählen: einen internen Knoten oder einen benutzerdefinierten externen Knoten. Klicken Sie auf "Internen Knoten verwenden" und dann auf "Speichern"


#### Verwaltung Ihres Lightning-Knotens (RTL)


Nach der Verbindung mit dem internen Lightning-Knoten wird der BTCPay-Server aktualisiert und zeigt eine Benachrichtigung "BTC Lightning-Knoten aktualisiert" an, die bestätigt, dass Sie Lightning jetzt mit Ihrem Shop verbunden haben.


Die Verwaltung des Blitzknotens ist eine Aufgabe für den Serveradministrator. Dazu gehören die folgenden Aufgaben:


- Transaktion verwalten
- Verwaltung der Liquidität
  - Liquidität im Eingang
  - Ausgehende Liquidität
- Verwaltung von Peers und Kanälen
  - Vernetzte Peers
  - Kanalgebühren
  - Kanalstatus
- Häufige Erstellung von Sicherungskopien der Kanalzustände.
- Überprüfung der Routing-Berichte
- Alternativ können Sie auch Dienste wie Loop nutzen.


Die gesamte Verwaltung der Lightning-Knoten erfolgt standardmäßig über RTL (vorausgesetzt, Sie arbeiten mit einer LND-Implementierung). Administratoren können auf ihren Lightning Wallet in BTCPay Server klicken und eine Schaltfläche zum Öffnen von RTL finden. Das Haupt-Dashboard von BTCPay Server wird nun mit den Lightning Network-Kacheln aktualisiert, einschließlich des schnellen Zugriffs auf RTL.


### Beispiel 2


#### Verbindung zum Blitz mit Alby


Wenn Sie eine Verbindung zu einem Verwahrer wie Alby herstellen möchten, sollten Ladenbesitzer zunächst ein Konto erstellen und https://getalby.com/ besuchen


![image](assets/en/036.webp)


Nachdem Sie das Alby-Konto erstellt haben, gehen Sie zu Ihrem BTCPay Server-Shop.


Schritt 1: Klicken Sie auf dem Dashboard auf "Lightning-Knoten einrichten" oder auf "Lightning" unterhalb der Geldbörsen.


![image](assets/en/037.webp)


Schritt 2: Geben Sie Ihre Wallet-Verbindungsdaten ein, die Sie von Alby erhalten haben. Klicken Sie auf dem Dashboard von Alby auf Wallet. Hier finden Sie "Wallet Connection Credentials". Kopieren Sie diese Anmeldeinformationen. Fügen Sie die Anmeldedaten von Alby in das Feld für die Verbindungskonfiguration in BTCPay Server ein.


![image](assets/en/038.webp)


Schritt 3: Nachdem Sie dem BTCPay-Server die Verbindungsdaten mitgeteilt haben, klicken Sie auf die Schaltfläche "Verbindung testen", um sicherzustellen, dass die Verbindung ordnungsgemäß funktioniert. Beachten Sie die Meldung "Verbindung zum Blitzknoten erfolgreich" am oberen Rand Ihres Bildschirms. Dies bestätigt, dass alles wie erwartet funktioniert.


![image](assets/en/039.webp)


Schritt 4: Klicken Sie auf "Speichern", und Ihr Shop ist nun mit einem Lightning-Knoten von Alby verbunden.


![image](assets/en/040.webp)


**!Hinweis!**


Vertrauen Sie einer Lightning-Lösung niemals mehr Wert an, als Sie zu verlieren bereit sind.


### Zusammenfassung der Fertigkeiten


In diesem Abschnitt haben Sie gelernt:



- So verbinden Sie einen internen oder externen Lightning-Knoten
- Inhalt und Funktion der verschiedenen Kacheln im Dashboard, die sich auf Blitze beziehen
- So konfigurieren Sie das Lightning Wallet mit Voltage Surge oder Alby


### Wissensbewertung Praktische Überprüfung


Beschreiben Sie einige der verschiedenen Optionen für den Anschluss eines Lightning Wallet an Ihr Geschäft.


# BTCPay-Server Interface


<partId>25e88b81-e1ab-515f-a035-09f2a3075556</partId>


## Übersicht über das Dashboard


<chapterId>410ff28b-a272-5c91-93e0-48d5b28c53ab</chapterId>


BTCPay Server ist ein modulares Softwarepaket. Es gibt jedoch Standards, die jeder BTCPay Server einhalten muss, und diese Standards regeln die Interaktion zwischen dem Administrator und den Benutzern. Beginnend mit dem Dashboard. Der Haupteinstiegspunkt eines jeden BTCPay Servers nach dem Einloggen. Das Dashboard bietet einen Überblick über die Leistung Ihres Shops, den aktuellen Kontostand des Wallet und die Transaktionen der letzten 7 Tage. Da es sich um eine modulare Ansicht handelt, können Plugins diese Ansicht zu ihrem Vorteil nutzen und eigene Kacheln auf dem Dashboard erstellen. In diesem Kurs werden wir nur die Standard-Plugins und -Apps zusammen mit ihren jeweiligen Ansichten im BTCPay Server besprechen.


### Dashboard-Kacheln


In der Hauptansicht des BTCPay Server Dashboards sind einige Standardkacheln verfügbar. Diese Kacheln sind für den Shop-Besitzer oder Administrator gedacht, um ihren Shop schnell in einer Übersicht zu verwalten.



- Wallet Gleichgewicht
- Transaktionsaktivität
- Lightning Balance (wenn Lightning im Shop aktiviert ist)
- Lightning Services (wenn Lightning im Shop aktiviert ist)
- Jüngste Transaktionen.
- Neueste Rechnungen
- Derzeit aktive Crowdfunds
- Leistung der Filiale / meistverkaufte Artikel.


### Wallet Gleichgewicht


Die Wallet-Bilanzkachel gibt einen schnellen Überblick über das Guthaben und die Leistung Ihres Wallet. Sie kann entweder in BTC oder Fiat-Währung in einer wöchentlichen, monatlichen oder jährlichen Grafik angezeigt werden.


![image](assets/en/041.webp)


### Transaktionsaktivität


Neben der Kachel Wallet Saldo zeigt BTCPay Server einen schnellen Überblick über ausstehende Auszahlungen, die Anzahl der Transaktionen in den letzten 7 Tagen und ob Ihr Shop Rückerstattungen ausgegeben hat. Mit einem Klick auf die Schaltfläche Verwalten gelangen Sie in die Verwaltung der ausstehenden Auszahlungen (mehr über Auszahlungen erfahren Sie im Kapitel BTCPay Server - Zahlungen).


![image](assets/en/042.webp)


### Lightning Balance


Dies ist nur sichtbar, wenn Lightning aktiviert ist.


Wenn der Administrator den Zugriff auf Lightning Network erlaubt hat, enthält das Dashboard des BTCPay-Servers jetzt eine neue Kachel mit Informationen zu Ihrem Lightning-Knoten. Wie viel BTC befindet sich in Kanälen, wie wird dies lokal oder aus der Ferne ausgeglichen (eingehende oder ausgehende Liquidität), wenn Kanäle geschlossen oder geöffnet werden und wie viel Bitcoin wird On-Chain auf dem Lightning-Knoten gehalten.


![image](assets/en/043.webp)


### Blitzdienste


Dies ist nur sichtbar, wenn der Blitz aktiv ist.


Neben der Anzeige des Lightning-Guthabens auf dem BTCPay Server-Dashboard sehen Administratoren auch die Kachel für Lightning Services. Hier finden Administratoren Schnellschaltflächen für Tools, die sie zur Verwaltung ihres Lightning-Knotens verwenden. Ride the Lightning ist zum Beispiel eines der Standardtools von BTCPay Server für die Verwaltung von Lightning-Knoten.


![image](assets/en/044.webp)


### Jüngste Transaktionen


Die Kachel "Letzte Transaktionen" zeigt die letzten Transaktionen Ihres Shops an. Mit einem Klick kann der Administrator der BTCPay Server-Instanz nun die letzte Transaktion sehen und feststellen, ob sie beachtet werden muss.


![image](assets/en/045.webp)


### Aktuelle Rechnungen


Die Kachel "Letzte Rechnungen" zeigt die 6 letzten von Ihrem BTCPay-Server generierten Rechnungen an, einschließlich Status und Invoice-Betrag. Die Kachel enthält auch eine Schaltfläche "Alle anzeigen", um die vollständige Invoice-Übersicht einfach aufzurufen.


![image](assets/en/046.webp)


### Verkaufsstellen und Crowdfunds


Da BTCPay Server eine Reihe von Standard-Plugins oder Apps liefert, sind Point Of Sale und Crowdfund die beiden wichtigsten Plugins von BTCPay Server. Mit jedem Shop und Wallet kann ein BTCPay Server-Benutzer generate so viele Point Of Sales oder Crowdfunds einrichten, wie er für richtig hält. Jedes Plugin erstellt eine neue Dashboard-Kachel, die die Leistung der Plugins anzeigt.


![image](assets/en/047.webp)


Beachten Sie den kleinen Unterschied zwischen einer Point of Sale- und einer Crowdfunding-Kachel. Der Administrator sieht die meistverkauften Artikel in der Kachel "Verkaufsstelle". In der Crowdfunding-Kachel sind dies die Top Perks. Beide Kacheln verfügen über Schnellschaltflächen zur Verwaltung der jeweiligen App und zur Anzeige der letzten Rechnungen, die durch die Top-Artikel oder Top-Perks erstellt wurden.


![image](assets/en/048.webp)


**Anmerkung*


Saldengrafiken und letzte Transaktionen sind nur für On-Chain-Zahlungsarten verfügbar. Informationen über Lightning Network-Salden und -Transaktionen stehen auf der To-Do-Liste. Ab der BTCPay Server Version 1.6.0 sind grundlegende Lightning Network-Salden verfügbar.


### Zusammenfassung der Fertigkeiten


In diesem Abschnitt haben Sie Folgendes gelernt:



- Das Hauptlayout der Kacheln auf der Haupt-Landingpage wird als Dashboard bezeichnet.
- Ein grundlegendes Verständnis des Inhalts der einzelnen Kacheln.


### Überprüfung der Wissensbewertung


Listen Sie so viele Kacheln aus dem Speicher auf, wie Sie vom Dashboard aus erfassen können.


## BTCPay Server - Einstellungen speichern


<chapterId>e8faef7b-278d-550e-a511-bc3a442daf64</chapterId>


Innerhalb der BTCPay Server Software gibt es zwei Arten von Einstellungen. BTCPay Server Store-spezifische Einstellungen, die Schaltfläche "Einstellungen" in der linken Menüleiste unter dem Dashboard, und BTCPay Server-Einstellungen, die Sie unten in der Menüleiste direkt über "Konto" finden. Die BTCPay Server-spezifischen Einstellungen können nur von Server-Administratoren eingesehen werden.


Die Speichereinstellungen bestehen aus vielen Registerkarten, um die einzelnen Einstellungssätze zu kategorisieren.



- Allgemein
- Preise
- Erscheinungsbild der Kasse
- Zugangstoken
- Benutzer
- Rollen
- Webhaken
- Auszahlungsprozessoren
- E-Mails
- Formulare


### Allgemein


Auf der Registerkarte "Allgemeine Einstellungen" legen die Ladenbesitzer ihr Branding und ihre Zahlungsvorgaben fest. Bei der Ersteinrichtung des Ladens wurde ein Ladenname angegeben; dieser wird in den Allgemeinen Einstellungen unter Ladenname angezeigt. Hier kann der Geschäftsinhaber auch seine Website so einstellen, dass sie mit dem Branding übereinstimmt, und eine Geschäfts-ID angeben, die der Administrator in der Datenbank erkennen kann.


#### Branding


Da BTCPay Server FOSS ist, kann ein Shop-Besitzer ein individuelles Branding erstellen, das zu seinem Shop passt. Legen Sie die Markenfarbe fest, speichern Sie die Logos Ihrer Marke und fügen Sie benutzerdefinierte CSS für öffentliche/kundenorientierte Seiten hinzu (Rechnungen, Zahlungsanfragen, Pull-Zahlungen)


#### Zahlung


In den Zahlungseinstellungen können die Ladenbesitzer die Standardwährung ihres Ladens festlegen (entweder Bitcoin oder eine beliebige Fiat-Währung).


#### Jedem die Möglichkeit geben, Rechnungen zu erstellen


Diese Einstellung ist für Entwickler oder Erbauer von BTCPay Server gedacht. Wenn diese Einstellung für Ihren Shop aktiviert ist, kann die Außenwelt Rechnungen auf Ihrer BTCPay Server-Instanz erstellen.


#### Hinzufügen einer zusätzlichen Gebühr (Netzwerkgebühr) zu den Rechnungen


Eine Funktion innerhalb von BTCPay, die Händler vor Dust-Angriffen oder Kunden davor schützt, dass später hohe Gebühren anfallen, wenn der Händler eine große Menge an Bitcoin auf einmal transferieren muss. Ein Beispiel: Der Kunde hat einen Invoice für 20$ erstellt und diesen teilweise bezahlt, indem er 20 Mal 1$ bezahlt hat, bis der Invoice vollständig bezahlt war. Der Händler hat nun eine größere Transaktion, was die Mining-Kosten erhöht, wenn der Händler beschließt, diese Mittel später zu verschieben. Standardmäßig wendet BTCPay zusätzliche Netzwerkkosten auf den gesamten Invoice-Betrag an, um diese Kosten für den Händler zu decken, wenn der Invoice in mehreren Transaktionen gezahlt wird. BTCPay bietet mehrere Optionen zur Anpassung dieser Schutzfunktion. Sie können eine Netzwerkgebühr anwenden:



- Nur wenn der Kunde mehr als eine Zahlung für den Invoice leistet (im obigen Beispiel, wenn der Kunde einen Invoice für 20\$ erstellt und 1\$ bezahlt hat, beträgt der fällige Gesamtbetrag des Invoice nun 19\$ + die Netzgebühr. Die Netzgebühr wird nach der ersten Zahlung erhoben)
- Bei jeder Zahlung (einschließlich der ersten Zahlung, in unserem Beispiel beträgt die Gesamtsumme sofort 20\$ + Netzgebühr, sogar bei der ersten Zahlung)
- Keine Netzgebühr hinzufügen (deaktiviert die Netzgebühr vollständig)


Sie schützt zwar vor Dust-Transaktionen, kann sich aber auch negativ auf Unternehmen auswirken, wenn sie nicht richtig kommuniziert wird. Die Kunden könnten zusätzliche Fragen haben und denken, dass Sie ihnen zu viel Geld abverlangen.


#### Invoice verfällt, wenn der volle Betrag nicht bezahlt wurde, nachdem?


Der Invoice-Timer ist standardmäßig auf 15 Minuten eingestellt. Der Timer dient als Schutzmechanismus gegen Volatilität, da er den Bitcoin-Betrag entsprechend den Bitcoin-to-fiat Exchange-Sätzen sperrt. Zahlt der Kunde den Invoice nicht innerhalb der festgelegten Frist, gilt der Invoice als verfallen. Der Invoice gilt als "bezahlt", sobald die Transaktion auf dem Blockchain sichtbar ist (mit null Bestätigungen), und ist "abgeschlossen", wenn die vom Händler festgelegte Anzahl von Bestätigungen erreicht ist (normalerweise 1-6). Der Timer ist in Minuten anpassbar.


#### Betrachten Sie den Invoice als gezahlt, auch wenn der gezahlte Betrag um X % niedriger ist als erwartet?


Wenn ein Kunde ein Exchange Wallet verwendet, um direkt für ein Invoice zu bezahlen, nimmt das Exchange eine kleine Gebühr. Dies bedeutet, dass ein solcher Invoice nicht als vollständig abgeschlossen betrachtet wird. Der Invoice wird als "teilweise bezahlt" gekennzeichnet. Sie können hier den Prozentsatz festlegen, wenn ein Händler unterbezahlte Rechnungen akzeptieren möchte.


### Preise


Wenn in BTCPay Server ein Invoice generiert wird, benötigt er immer den aktuellsten und genauesten Bitcoin-to-fiat-Preis. Beim Erstellen eines neuen Shops in BTCPay Server werden Administratoren aufgefordert, ihre bevorzugte Preisquelle festzulegen. Nachdem der Shop eingerichtet ist, können Shop-Besitzer ihre Preisquelle auf dieser Registerkarte jederzeit ändern.


#### Erweiterte Skripterstellung für Tarifregeln


Hauptsächlich von Power-Usern verwendet. Wenn diese Funktion aktiviert ist, können Ladenbesitzer Skripte zum Preisverhalten und zur Abrechnung mit ihren Kunden erstellen.


#### Prüfung


Ein schneller Testplatz für Ihre bevorzugten Währungspaare. Diese Funktion umfasst auch die Möglichkeit, Standard-Währungspaare über eine REST-Abfrage zu prüfen.


### Erscheinungsbild der Kasse


Die Registerkarte "Checkout Appearance" beginnt mit Invoice-spezifischen Einstellungen und einer Standardzahlungsmethode und aktiviert spezifische Zahlungsmethoden, wenn die festgelegten Anforderungen erfüllt sind.


#### Invoice Einstellungen


Standard-Zahlungsmethoden. Der BTCPay-Server bietet in seiner Standardkonfiguration drei Optionen.



- BTC (On-Chain)
- BTC (LNURL-pay)
- BTC (off-chain und Lightning)


Wir können Parameter für unseren Shop festlegen, bei denen ein Kunde nur mit Lightning interagiert, wenn der Preis unter X liegt, und umgekehrt für On-Chain-Transaktionen, wenn X größer als Y ist, immer die On-Chain-Zahlungsoption präsentiert.


![image](assets/en/049.webp)


#### Kasse


Mit dem BTCPay Server Release 1.7 wurde ein neuer Checkout Interface, Checkout V2, eingeführt. Da die Version 1.9 standardisiert wurde, können Administratoren und Shop-Betreiber den Checkout immer noch auf die vorherige Version einstellen. Mit dem Toggle "Use the classic checkout" kann ein Shop-Besitzer den Shop auf seine vorherige Checkout-Erfahrung zurücksetzen. BTCPay Server verfügt auch über eine Reihe von Voreinstellungen für den Online-Handel oder für die Verwendung in Geschäften.


![image](assets/en/050.webp)


Wenn ein Kunde mit dem Shop interagiert und ein Invoice generiert, gibt es eine Verfallszeit für das Invoice. BTCPay Server setzt diese standardmäßig auf 5 Minuten fest, und Administratoren können sie nach ihren Wünschen anpassen. Die Kassenseite kann weiter angepasst werden, indem die folgenden Parameter überprüft werden:



- Feiern Sie die Zahlung mit Konfetti
- Anzeigen der Kopfzeile des Shops (Name und Logo)
- Die Schaltfläche "In Wallet bezahlen" anzeigen
- Vereinheitlichung von On-Chain und off-chain Zahlungen URL/QR
- Anzeige der Blitzzahlungsbeträge in Satoshis
- Automatische Erkennung der Sprache beim Checkout


![image](assets/en/051.webp)


Wenn die automatische Erkennung der Sprache nicht eingestellt ist, zeigt BTCPay Server standardmäßig Englisch an. Ein Shop-Besitzer kann diese Voreinstellung in seine bevorzugte Sprache ändern.


![image](assets/en/052.webp)


Klicken Sie auf die Dropdown-Liste, und die Shop-Besitzer können einen benutzerdefinierten HTML-Titel festlegen, der auf der Kassenseite angezeigt wird.


![image](assets/en/053.webp)


Um sicherzustellen, dass die Kunden ihre Zahlungsmethode kennen, kann ein Shop-Besitzer explizit einstellen, dass die Benutzer immer ihre bevorzugte Zahlungsmethode wählen müssen. Sobald der Invoice bezahlt ist, ermöglicht BTCPay Server dem Kunden die Rückkehr zum Webshop. Ladenbesitzer können diese Weiterleitung so einstellen, dass sie automatisch erfolgt, nachdem der Kunde bezahlt hat.


![image](assets/en/054.webp)


#### Öffentlicher Empfang


In den Einstellungen für öffentliche Bons kann der Geschäftsinhaber die Bonseiten als öffentlich kennzeichnen, so dass die Zahlungsliste auf der Bonseite und der QR-Code angezeigt werden, damit der Kunde sie leicht aufrufen kann.


![image](assets/en/055.webp)


### Zugangstoken


Zugangstoken werden für die Kopplung mit bestimmten E-Commerce-Integrationen oder benutzerdefinierten Integrationen verwendet.


![image](assets/en/056.webp)


### Benutzer


Unter Shop-Benutzer kann der Shop-Besitzer seine Mitarbeiter, deren Konten und den Zugang zum Shop verwalten. Nachdem die Mitarbeiter ihre Konten erstellt haben, kann der Geschäftsinhaber bestimmte Benutzer als Gastbenutzer oder Eigentümer zum Geschäft hinzufügen. Um die Rolle des Mitarbeiters weiter zu definieren, lesen Sie den nächsten Abschnitt "BTCPay Server Store-Einstellungen - Rollen"


![image](assets/en/057.webp)


### Rollen


Einem Geschäftsinhaber sind die Standardrollen des Benutzers vielleicht nicht wichtig genug. In den Einstellungen für benutzerdefinierte Rollen kann ein Geschäftsinhaber die genauen Anforderungen für jede Rolle in seinem Geschäft definieren.


(1) Um eine neue Rolle zu erstellen, klicken Sie auf die Schaltfläche "+ Rolle hinzufügen".


![image](assets/en/058.webp)


(2) Geben Sie einen Rollennamen ein, z. B. "Kassierer".


![image](assets/en/059.webp)


(3) Konfigurieren Sie die einzelnen Berechtigungen für die Rolle.



- Ändern Sie Ihre Geschäfte.
- Verwalten Sie Exchange-Konten, die mit Ihren Geschäften verbunden sind.
  - Exchange-Konten anzeigen, die mit Ihren Geschäften verbunden sind.
- Verwalten Sie Ihre Abschlagszahlungen.
- Pull-Zahlungen erstellen.
  - Erstellen Sie nicht genehmigte Abrufzahlungen.
- Ändern Sie Rechnungen.
  - Rechnungen einsehen.
  - Erstellen Sie einen Invoice.
  - Erstellen Sie Rechnungen aus den Blitzknoten, die mit Ihren Geschäften verbunden sind.
- Sehen Sie sich Ihre Geschäfte an.
  - Rechnungen einsehen.
  - Ihre Zahlungsaufforderungen einsehen.
  - Ändern Sie die Webhooks der Geschäfte.
- Ändern Sie Ihre Zahlungsaufforderungen.
  - Ihre Zahlungsaufforderungen einsehen.
- Verwenden Sie die Blitzknoten, die mit Ihren Geschäften verbunden sind.
  - Zeigen Sie die Blitzrechnungen an, die mit Ihren Geschäften verbunden sind.
  - Erstellen Sie Rechnungen aus den Blitzknoten, die mit Ihren Geschäften verbunden sind.
- Zahlen Sie Geld auf Exchange-Konten ein, die mit Ihren Geschäften verbunden sind.
- Überweisen Sie Gelder von Exchange-Konten auf Ihr Geschäft.
- Handel mit Geldmitteln auf den Exchange-Konten Ihres Geschäfts.


Wenn die Rolle erstellt wird, ist der Name fest und kann nicht mehr geändert werden, wenn sie sich im Bearbeitungsmodus befindet.


![image](assets/en/060.webp)


### Webhaken


Innerhalb von BTCPay Server ist es relativ einfach, einen neuen "Webhook" zu erstellen. In den BTCPay Server Shop-Einstellungen - Registerkarte "Webhooks" kann ein Shop-Besitzer ganz einfach einen neuen Webhook erstellen, indem er auf das Symbol "+ Webhook erstellen" klickt. Webhooks ermöglichen es BTCPay Server, HTTP-Ereignisse im Zusammenhang mit Ihrem Shop an andere Server oder E-Commerce-Integrationen zu senden.


![image](assets/en/061.webp)


Sie befinden sich nun in der Ansicht zum Erstellen eines Webhooks. Stellen Sie sicher, dass Sie Ihre Payload-URL kennen und fügen Sie diese in Ihren BTCPay-Server ein. Während Sie die Payload-URL eingefügt haben, wird darunter das Webhook-Geheimnis angezeigt. Kopieren Sie das Webhook-Geheimnis und geben Sie es am Endpunkt an. Wenn alles eingestellt ist, können Sie in BTCPay Server auf "Automatic redelivery" umschalten BTCPay Server wird versuchen, jede fehlgeschlagene Übermittlung nach 10 Sekunden, 1 Minute und bis zu 6 Mal nach 10 Minuten erneut zuzustellen. Sie können zwischen jedem Ereignis umschalten oder die Ereignisse für Ihre Bedürfnisse festlegen. Stellen Sie sicher, dass Sie den Webhook aktivieren und klicken Sie auf die Schaltfläche "Webhook hinzufügen", um ihn zu speichern.


![image](assets/en/062.webp)


Webhooks sind nicht dafür gedacht, mit der Bitpay-API kompatibel zu sein. Es gibt zwei separate IPNs (in BitPay-Begriffen: "Instant Payment Notifications") in BTCPay Server.



- Webhookp
- Benachrichtigungen


Verwenden Sie die Benachrichtigungs-URL nur, wenn Sie Rechnungen über die Bitpay-API erstellen.


### Auszahlungsprozessoren


Auszahlungsprozessoren arbeiten mit dem Auszahlungskonzept in BTCPay Server zusammen. Ein Auszahlungsaggregator, um mehrere Transaktionen zu bündeln und sie auf einmal zu senden. Mit Auszahlungsprozessoren kann ein Shop-Betreiber die gebündelten Auszahlungen automatisieren. BTCPay Server bietet zwei Methoden für automatisierte Auszahlungen: On-Chain und off-chain (LN).


Der Geschäftsinhaber kann beide Auszahlungsprozessoren separat anklicken und konfigurieren. So kann es sein, dass der Ladenbesitzer den On-Chain-Prozessor nur einmal alle X Stunden laufen lassen möchte, während der off-chain-Prozessor alle paar Minuten laufen könnte. Für On-Chain können Sie auch ein Ziel festlegen, in welchem Block er enthalten sein soll. Standardmäßig ist dies auf 1 (oder den nächsten verfügbaren Block) eingestellt. Beachten Sie, dass die Einstellung des off-chain-Auszahlungsprozessors nur den Intervalltimer und kein Blockziel enthält. Lightning Network-Auszahlungen erfolgen sofort.


![image](assets/en/063.webp)

![image](assets/en/064.webp)


Ladenbesitzer können den On-Chain-Prozessor nur konfigurieren, wenn ein Hot Wallet an ihren Laden angeschlossen ist.


![image](assets/en/065.webp)


Nachdem Sie einen Auszahlungsprozessor eingerichtet haben, können Sie ihn schnell entfernen oder ändern, indem Sie zur Registerkarte Auszahlungsprozessor in den Einstellungen des BTCPay Server Stores zurückkehren.


**Anmerkung**


Auszahlungsprozessor On-Chain - Der Auszahlungsprozessor On-Chain kann nur in einem Shop funktionieren, der mit einem Hot Wallet konfiguriert ist. Wenn kein Hot Wallet angeschlossen ist, verfügt der BTCPay-Server nicht über die Wallet-Schlüssel und kann keine Auszahlungen automatisch verarbeiten.


### E-Mails


BTCPay Server kann E-Mails für Benachrichtigungen oder, wenn richtig eingestellt, zur Wiederherstellung von auf der Instanz erstellten Konten verwenden. Standardmäßig sendet BTCPay Server keine E-Mail, wenn z. B. das Passwort verloren geht.


![image](assets/en/066.webp)


Bevor ein Shop-Betreiber E-Mail-Regeln festlegen kann, um bestimmte Ereignisse in seinem Shop auszulösen, muss er zunächst einige grundlegende E-Mail-Einstellungen vornehmen. BTCPay Server benötigt diese Einstellungen, um E-Mails für Ereignisse im Zusammenhang mit Ihrem Shop oder für Passwortrücksetzungen zu senden.


BTCPay Server hat das Ausfüllen dieser Informationen durch die "Quick Fill"-Option erleichtert:



- Gmail.com
- Yahoo.de
- Mailgun
- Büro365
- SendGrid


Wenn Sie die Schnellausfülloption verwenden, füllt BTCPay Server die Felder für den SMTP-Server und den Port bereits aus. Jetzt muss der Shop-Betreiber nur noch seine Anmeldedaten eingeben, einschließlich einer E-Mail-Address, Login (was in der Regel gleich Ihrer E-Mail-Address ist) und seinem Passwort. Die erweiterte Option in den E-Mail-Einstellungen des BTCPay-Servers besteht darin, die Sicherheitsüberprüfung des TLS-Zertifikats zu deaktivieren; standardmäßig ist diese Option aktiviert.


![image](assets/en/067.webp)


Mit E-Mail-Regeln kann ein Shop-Betreiber bestimmte Ereignisse festlegen, die E-Mails an bestimmte E-Mail-Adressen auslösen.



- Invoice Erstellt
- Invoice Erhaltene Zahlung
- Invoice Verarbeitung
- Invoice Abgelaufen
- Invoice Erledigt
- Invoice Ungültig
- Invoice Zahlung abgewickelt


Wenn der Kunde eine E-Mail Address angegeben hat, können diese Auslöser die Informationen auch an den Kunden senden. Ladenbesitzer können die Betreffzeile vorab ausfüllen, um deutlich zu machen, warum diese E-Mail passiert ist und was sie ausgelöst hat.


![image](assets/en/068.webp)


### Formulare


Da BTCPay Server keine Daten sammelt, möchte ein Shop-Betreiber vielleicht ein benutzerdefiniertes Formular zu seinem Checkout-Erlebnis hinzufügen; auf diese Weise kann der Shop-Betreiber zusätzliche Informationen von seinem Kunden sammeln. Der BTCPay Server Form Builder besteht aus zwei Teilen: einer visuellen und einer erweiterten Codeansicht der Formulare.


Bei der Erstellung eines neuen Formulars öffnet BTCPay Server ein neues Fenster, in dem grundlegende Informationen zu den Fragen abgefragt werden, die Sie in Ihrem neuen Formular stellen möchten. Zunächst muss der Geschäftsinhaber einen eindeutigen Namen für sein neues Formular angeben; dieser Name kann nicht mehr geändert werden.


![image](assets/en/069.webp)


Nachdem der Geschäftsinhaber dem Formular einen Namen gegeben hat, können Sie auch den Schalter für "Formular für öffentliche Nutzung zulassen" auf EIN stellen, und es wird Green. Dadurch wird sichergestellt, dass das Formular an jedem Standort mit Kundenkontakt verwendet wird. Wenn zum Beispiel ein Ladenbesitzer ein separates Invoice nicht über seine Verkaufsstelle erstellt, möchte er vielleicht trotzdem Informationen vom Kunden erfassen. Mit dieser Umschaltfunktion können diese Informationen erfasst werden.


![image](assets/en/070.webp)


Jedes Formular beginnt mit mindestens einem neuen Formularfeld. Ein Ladenbesitzer kann auswählen, welche Art von Feld es sein soll.



- Text
- Nummer
- Passwort
- E-Mail
- URL
- Telefonnummern
- Datum
- Ausgeblendete Felder
- Feldsatz
- Ein Textbereich für offene Kommentare.
- Wahlschalter


Jeder Typ hat seine eigenen Parameter, die es auszufüllen gilt. Der Ladenbesitzer kann sie nach seinen Wünschen einstellen. Unterhalb des ersten erstellten Feldes können Ladenbesitzer neue Felder zu diesem Formular hinzufügen.


![image](assets/en/071.webp)


#### Erweiterte benutzerdefinierte Formulare


Mit BTCPay Server können Sie auch Formulare im Code erstellen. JSON, insbesondere. Statt auf den Editor zu schauen, können Shop-Betreiber auf die CODE-Schaltfläche direkt neben dem Editor klicken und in den Code ihrer Formulare einsteigen. In einer Felddefinition können nur die folgenden Felder festgelegt werden; die Werte der Felder werden in den Metadaten des Invoice gespeichert:



| Feld | Beschreibung |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| .fields.constant | Wenn true, muss .value in der Formulardefinition festgelegt werden und der Benutzer kann den Wert des Feldes nicht ändern. (Beispiel: die Version der Formulardefinition) |
| .fields.type | Der HTML-Input-Typ: text, radio, checkbox, password, hidden, button, color, date, datetime-local, month, week, time, email, number, range, search, url, select, tel |
| .fields.options | Wenn .fields.type gleich select ist, die Liste der auswählbaren Werte |
| .fields.options.text | Der für diese Option angezeigte Text |
| .fields.options.value | Der Wert des Feldes, wenn diese Option ausgewählt ist |
| .fields.type=fieldset | Erstellt ein HTML-fieldset um die untergeordneten .fields.fields (siehe unten) |
| .fields.name | Der JSON-Eigenschaftsname des Feldes, wie er in den Metadaten der Rechnung erscheint |
| .fields.value | Der Standardwert des Feldes |
| .fields.required | Wenn true, ist das Feld ein Pflichtfeld |
| .fields.label | Die Beschriftung des Feldes |
| .fields.helpText | Zusätzlicher Text zur Erläuterung des Feldes. |
| .fields.fields | Sie können Ihre Felder in einer Hierarchie organisieren, sodass untergeordnete Felder in den Metadaten der Rechnung verschachtelt werden können. Diese Struktur hilft Ihnen, die gesammelten Informationen besser zu organisieren und zu verwalten, was den Zugriff und die Interpretation erleichtert. Wenn Sie beispielsweise ein Formular haben, das Kundeninformationen sammelt, können Sie die Felder unter einem übergeordneten Feld namens customer gruppieren. Innerhalb dieses übergeordneten Feldes können Sie untergeordnete Felder wie name, Email und address haben. |

Der Feldname stellt den JSON-Eigenschaftsnamen dar, der den vom Benutzer bereitgestellten Wert in den Metadaten des Invoice speichert. Einige bekannte Namen können interpretiert und geändert werden, um die Einstellungen des Invoice anzupassen.



| Feldname         | Beschreibung          |
| ---------------- | ---------------------- |
| invoice_amount   | Betrag der Rechnung   |
| invoice_currency | Währung der Rechnung  |

Sie können die Felder eines Invoice automatisch ausfüllen, indem Sie Abfragezeichenfolgen zur URL des Formulars hinzufügen, z. B. "?your_field=value".


Hier sind einige Anwendungsfälle für diese Funktion:



- Unterstützung der Benutzereingabe: Füllen Sie Felder mit bekannten Kundeninformationen aus, um dem Kunden das Ausfüllen des Formulars zu erleichtern. Wenn Sie z. B. die E-Mail-Adresse Address eines Kunden bereits kennen, können Sie das E-Mail-Feld vorausfüllen, um dem Kunden Zeit zu sparen.
- Personalisierung: Passen Sie das Formular auf der Grundlage von Kundenpräferenzen oder Segmentierung an. Wenn Sie z. B. verschiedene Kundenebenen haben, können Sie das Formular mit relevanten Daten, wie z. B. der Mitgliedsstufe oder bestimmten Angeboten, ausfüllen.
- Nachverfolgung: Verfolgen Sie die Quelle der Kundenbesuche mit versteckten Feldern und vorausgefüllten Werten. Sie können zum Beispiel Links mit vorausgefüllten utm_media-Werten für jeden Marketingkanal (z. B. Twitter, Facebook, E-Mail) erstellen. So können Sie die Wirksamkeit Ihrer Marketingmaßnahmen analysieren.
- A/B-Tests: Füllen Sie Felder mit unterschiedlichen Werten aus, um verschiedene Formularversionen zu testen und so das Benutzererlebnis und die Konversionsraten zu optimieren.


### Zusammenfassung der Fertigkeiten


In diesem Abschnitt haben Sie Folgendes gelernt:



- Das Layout und die Funktionen der Registerkarten in den Shop-Einstellungen
- Eine Vielzahl von Optionen für die Feinabstimmung des Umgangs mit zugrunde liegenden Exchange-Sätzen, Teilzahlungen, geringfügigen Unterzahlungen und mehr.
- Passen Sie das Erscheinungsbild der Kasse an, einschließlich preisabhängiger Hauptkette vs. Lightning-Aktivierung auf Rechnungen.
- Verwalten Sie rollenübergreifende Zugriffsebenen und Berechtigungen für den Speicher.
- Konfigurieren Sie automatische E-Mails und deren Auslöser
- Erstellen Sie benutzerdefinierte Formulare für die Erfassung zusätzlicher Kundeninformationen beim Checkout.


### Wissensbilanzierung


#### KA-Kritik


Was ist der Unterschied zwischen Speichereinstellungen und Servereinstellungen?


#### KA Hypothetisch


Beschreiben Sie einige Optionen, die Sie in Checkout Appearance > Invoice Settings auswählen könnten, und warum.


## BTCPay Server - Server-Einstellungen


<chapterId>1dd858a2-49ea-586b-9bc1-75a65f508df6</chapterId>


BTCPay Server besteht aus zwei verschiedenen Einstellungsansichten. Die eine ist den Store-Einstellungen gewidmet, die andere den Server-Einstellungen. Letztere ist nur für Serveradministratoren und nicht für Ladenbesitzer verfügbar. Serveradministratoren können Benutzer hinzufügen, benutzerdefinierte Rollen erstellen, den E-Mail-Server konfigurieren, Richtlinien festlegen, Wartungsaufgaben ausführen, alle mit BTCPay Server verbundenen Dienste überprüfen, Dateien auf den Server hochladen oder Protokolle überprüfen.


### Benutzer


Wie bereits erwähnt, können Serveradministratoren Benutzer zu ihrem Server einladen, indem sie sie auf der Registerkarte Benutzer hinzufügen.


### Serverweite benutzerdefinierte Rollen


BTCPay Server verfügt über zwei Arten von benutzerdefinierten Rollen: Store-spezifische benutzerdefinierte Rollen und serverweite benutzerdefinierte Rollen in den BTCPay Server-Einstellungen. Beide enthalten einen ähnlichen Satz von Berechtigungen; wenn sie jedoch über die Registerkarte "BTCpay Server Settings - Roles" (BTCPay Server-Einstellungen - Rollen) festgelegt werden, ist die angewandte Rolle serverweit und gilt für mehrere Filialen. Beachten Sie die Markierung "Serverweit" bei den benutzerdefinierten Rollen in den Servereinstellungen.


![image](assets/en/072.webp)


### Serverweite benutzerdefinierte Rollen


Serverweite Berechtigung für benutzerdefinierte Rollen;



- Ändern Sie Ihre Geschäfte.
- Verwalten Sie Exchange-Konten, die mit Ihren Geschäften verbunden sind.
  - Exchange-Konten anzeigen, die mit Ihren Geschäften verknüpft sind.
- Verwalten Sie Ihre Abschlagszahlungen.
- Pull-Zahlungen erstellen.
  - Erstellen Sie nicht genehmigte Abrufzahlungen.
- Ändern Sie Rechnungen.
  - Rechnungen einsehen.
  - Erstellen Sie einen Invoice.
  - Erstellen Sie Rechnungen aus den Blitzknoten, die mit Ihren Geschäften verbunden sind.
- Sehen Sie sich Ihre Geschäfte an.
  - Rechnungen einsehen.
  - Ihre Zahlungsaufforderungen einsehen.
  - Ändern Sie die Webhooks der Geschäfte.
- Ändern Sie Ihre Zahlungsaufforderungen.
  - Ihre Zahlungsaufforderungen einsehen.
- Verwenden Sie die Blitzknoten, die mit Ihren Geschäften verbunden sind.
  - Zeigen Sie die Blitzrechnungen an, die mit Ihren Geschäften verbunden sind.
  - Erstellen Sie Rechnungen aus den Blitzknoten, die mit Ihren Geschäften verbunden sind.
- Zahlen Sie Geld auf Exchange-Konten ein, die mit Ihren Geschäften verbunden sind.
- Überweisen Sie Geld von Exchange-Konten auf Ihr Geschäft.
- Handel mit Geldmitteln auf den Exchange-Konten Ihres Geschäfts.


**Anmerkung*


Wenn die Rolle erstellt wird, ist der Name fest und kann nicht mehr geändert werden, wenn sie sich im Bearbeitungsmodus befindet.


### E-Mail


Die serverweiten E-Mail-Einstellungen sehen ähnlich aus wie die filialspezifischen E-Mail-Einstellungen. Allerdings werden hier nicht nur Auslöser für Geschäfte oder Administratorprotokolle, sondern auch Auslöser für andere Ereignisse behandelt. Diese E-Mail-Einstellung macht auch die Passwortwiederherstellung auf dem BTCPay-Server bei der Anmeldung verfügbar. Es funktioniert ähnlich wie die Store-spezifischen Einstellungen; Administratoren können schnell ihre E-Mail-Parameter ausfüllen und ihre E-Mail-Anmeldedaten eingeben, damit der Server E-Mails senden kann.


![image](assets/en/073.webp)


### Politiken


Administratoren von BTCPay Server-Richtlinien können verschiedene Einstellungen zu Themen wie Einstellungen für bestehende Benutzer, Einstellungen für neue Benutzer, Benachrichtigungseinstellungen und Wartungseinstellungen vornehmen. Diese sind dafür gedacht, neue Benutzer als Administratoren oder normale Benutzer zu registrieren oder den BTCPay-Server vor Suchmaschinen zu verstecken, indem Sie ihn zu Ihrem Server-Header hinzufügen.


![image](assets/en/074.webp)


#### Bestehende Benutzer Einstellungen


Die hier verfügbaren Optionen sind von den benutzerdefinierten Rollen getrennt. Diese zusätzlichen Berechtigungen können einen Shop oder seinen Besitzer anfällig für Angriffe machen. Richtlinien, die zu bestehenden Benutzern hinzugefügt werden können:



- Erlauben Sie Nicht-Administratoren, den internen Lightning-Knoten in ihren Geschäften zu verwenden.
  - Dies würde es den Ladenbesitzern ermöglichen, den Lightning-Knoten des Server-Administrators und damit seine Gelder zu nutzen! Achtung, dies ist keine Lösung, um Zugang zu Lightning zu erhalten.
- Erlauben Sie Nicht-Administratoren, Hot-Geldbörsen für ihre Geschäfte zu erstellen.
  - Dies würde es jedem, der ein Konto auf Ihrer BTCPay-Serverinstanz hat, ermöglichen, Hot-Geldbörsen zu erstellen und deren Rückgewinnungs-seed auf dem Server des Administrators zu speichern. Dies könnte dazu führen, dass der Administrator für das Halten von Geldern Dritter haftet!
- Erlauben Sie Nicht-Administratoren, Hot-Geldbörsen für ihre Geschäfte zu importieren.
  - Ähnlich wie bei der Erstellung von Hot-Geldbörsen erlaubt diese Richtlinie den Import eines Hot Wallet mit denselben Gefahren, die im Abschnitt über die Erstellung von Hot-Geldbörsen erwähnt wurden.


![image](assets/en/075.webp)


#### Neue Benutzereinstellungen


Wir können einige wichtige Einstellungen vornehmen, um neue Benutzer auf dem Server zu verwalten. Wir können eine Bestätigungs-E-Mail für neue Registrierungen festlegen, die Erstellung neuer Benutzer über den Anmeldebildschirm deaktivieren und den Zugriff von Nicht-Administratoren auf die Benutzererstellung über die API beschränken.



- Für die Registrierung ist eine Bestätigungs-E-Mail erforderlich.
  - Der Serveradministrator muss einen E-Mail-Server eingerichtet haben.
- Deaktivieren Sie die Registrierung neuer Benutzer auf dem Server
- Deaktivieren Sie den Zugriff von Nicht-Administratoren auf den API-Endpunkt für die Benutzererstellung.


Standardmäßig hat BTCPay Server die Option "Disable new user registration on the server" (Registrierung neuer Benutzer auf dem Server deaktivieren) aktiviert und den Zugriff von Nicht-Administratoren auf den API-Endpunkt zur Benutzererstellung deaktiviert. Dies dient der Sicherheit, damit zufällige Personen, die über Ihren BTCPay-Login stolpern, keine Konten erstellen können.


![image](assets/en/076.webp)


#### Einstellungen für Benachrichtigungen


![image](assets/en/077.webp)


#### Wartungseinstellungen


BTCPay Server ist ein Open-Source-Projekt, das auf GitHub lebt. Wann immer BTCPay Server eine neue Version der Software veröffentlicht, können Administratoren benachrichtigt werden, dass eine neue Version verfügbar ist. Administratoren können auch verhindern, dass Suchmaschinen (wie Google, Yahoo und DuckDuckGo) die BTCPay Server-Domain indexieren. Da BTCPay Server FOSS ist, können Entwickler weltweit neue Funktionen entwickeln. BTCPay Server verfügt über eine experimentelle Funktion, die, wenn sie aktiviert ist, es Administratoren ermöglicht, Funktionen zu nutzen, die nicht für die Produktion, sondern für Testzwecke vorgesehen sind.



- Prüfen Sie Releases auf GitHub und lassen Sie sich benachrichtigen, wenn eine neue BTCPay Server-Version verfügbar ist.
- Suchmaschinen von der Indizierung dieser Website abhalten
- Aktivieren Sie experimentelle Funktionen.


![image](assets/en/078.webp)


#### Plugins


BTCPay Server kann Plugins hinzufügen und seinen Funktionsumfang erweitern. Die Plugins werden standardmäßig aus dem BTCPay Server Plugin-Builder-Repository geladen. Ein Administrator kann sich jedoch dafür entscheiden, Plugins in einem Pre-Release-Status zu sehen, und wenn der Plugin-Entwickler es erlaubt, kann der Server-Administrator jetzt Beta-Versionen von Plugins installieren.


![image](assets/en/079.webp)


##### Anpassungseinstellungen


Ein Standard-BTCPay-Server-Einsatz ist über die bei der Installation eingerichtete Domäne zugänglich. Ein Server-Administrator kann jedoch die Stammdomäne neu zuordnen und eine der erstellten Apps aus einem bestimmten Store anzeigen. Der Server-Administrator kann auch bestimmte Domänen bestimmten Anwendungen zuordnen.



- Anzeige der App im Stammverzeichnis der Website
  - Zeigt eine Liste möglicher Anwendungen an, die in der Stammdomäne angezeigt werden sollen.


![image](assets/en/080.webp)



- Ordnen Sie bestimmte Domänen bestimmten Anwendungen zu.
  - Wenn Sie auf klicken, um eine bestimmte Domäne für bestimmte Anwendungen einzurichten, kann der Administrator so viele Domänen einrichten, die auf bestimmte Anwendungen verweisen, wie erforderlich.


![image](assets/en/081.webp)


#### Block-Entdecker


BTCPay Server verfügt standardmäßig über Mempool.space als Block explorer für Transaktionen. Wenn BTCPay Server einen neuen Invoice generiert und eine Transaktion damit verknüpft ist, kann der Shop-Betreiber darauf klicken, um die Transaktion zu öffnen. BTCPay Server verweist standardmäßig auf Mempool.space als Block explorer; ein Server-Administrator kann dies jedoch auf seine bevorzugte Option ändern.


![image](assets/en/082.webp)


### Dienstleistungen


Die Registerkarte "BTCPay Server-Einstellungen: Dienste" bietet einen Überblick über die Komponenten, die Ihr BTCPay-Server verwendet. Die Dienste, die Ihr BTCPay Server bereitstellt, können je nach Bereitstellungsmethode variieren.


Ein BTCPay-Server-Administrator kann auf die "Siehe Informationen" hinter jedem Dienst klicken, um ihn zu öffnen und spezifische Einstellungen vorzunehmen.


![image](assets/en/083.webp)


#### LND (gRPC)


BTCPay stellt den GRPC-Dienst des LND für den externen Verbrauch zur Verfügung; Verbindungsinformationen finden Sie in diesem spezifischen Einstellungsmenü; kompatible Geldbörsen sind hier aufgelistet. BTCPay Server bietet auch einen QR-Code für die Verbindung, die gescannt und in einem mobilen Wallet angewendet werden kann.


Serveradministratoren können weitere Details einsehen.



- Details zum Gastgeber
- Verwendung von SSL
- Makrone
- AdminMacaroon
- RechnungMacaroon
- ReadonlyMacaroon
- GRPC SSL-Chiffre-Suite (GRPC_SSL_CIPHER_SUITES)


#### LND (REST)


BTCPay stellt den REST-Service von LND für externe Nutzer zur Verfügung; Verbindungsinformationen finden Sie [hier](https://docs.btcpayserver.org/FAQ/LightningNetwork/#how-to-find-node-info-and-open-a-direct-channel-with-a-store-using-btcpay); kompatible Wallets sind [hier](https://docs.btcpayserver.org/FAQ/Wallet/#can-i-use-a-hardware-wallet-with-btcpay-server) aufgelistet. Zu den kompatiblen Wallets gehören Joule, Alby und ZeusLN. BTCPay Server bietet einen QR-Code für die Verbindung, der gescannt und in einem kompatiblen Wallet angewendet werden kann.



- REST-URI
- Makrone
- AdminMacaroon
- RechnungMacaroon
- ReadonlyMacaroon


#### LND seed Sicherung


Die LND-seed-Sicherung ist nützlich für die Wiederherstellung von Geldern von Ihrem LND-Wallet im Falle einer Serverbeschädigung. Da der Lightning-Knoten ein Hot-Wallet ist, finden Sie die vertraulichen seed-Informationen auf dieser Seite.


Die LND dokumentiert den Wiederherstellungsprozess. Siehe https://github.com/lightningnetwork/LND/blob/master/docs/recovery.md für die Dokumentation.


#### Ride The Lightning


Ride the Lightning ist ein Lightning-Node-Management-Tool, das als Open-Source-Software entwickelt wurde. BTCPay Server verwendet RTL als Lightning-Node-Management-Komponente in seinem Stack. BTCPay Server-Administratoren können RTL über die Server-Einstellungen - Registerkarte Dienste oder durch Klicken auf den Lightning Wallet erreichen.


#### Full node P2P


Serveradministratoren möchten möglicherweise ihren Bitcoin-Knoten mit einem mobilen Wallet verbinden. Auf dieser Seite finden Sie Informationen darüber, wie Sie über das P2P-Protokoll eine Fernverbindung zu Ihrem Full node herstellen können. Zum Zeitpunkt der Erstellung dieses Kurses listet BTCPay Server Blockstream Green und Wasabi Wallets als kompatible Wallets auf. BTCPay Server stellt einen QR-Code für die Verbindung bereit, der gescannt und in einem kompatiblen Wallet angewendet werden kann.


#### Full node RPC


Auf dieser Seite finden Sie Informationen zur Fernverbindung mit Ihrem Full node über das RPC-Protokoll.


#### SSH


SSH wird für Wartungszwecke verwendet. BTCPay Server zeigt den anfänglichen Verbindungsbefehl an, um Ihren Server zu erreichen, sowie die öffentlichen SSH-Schlüssel, die zur Verbindung mit Ihrem Server berechtigt sind. Server-Administratoren können SSH-Änderungen über die BTCPay Server-Benutzeroberfläche deaktivieren.


#### Dynamisches DNS


Dynamisches DNS ermöglicht es Ihnen, einen stabilen DNS-Namen zu haben, der auf Ihren Server zeigt, auch wenn sich Ihre IP Address regelmäßig ändert. Dies wird empfohlen, wenn Sie BTCPay Server zu Hause hosten und eine eindeutige Domain für den Zugriff auf Ihren Server haben möchten.


Beachten Sie, dass Sie Ihre NAT- und BTCPay-Server-Installation richtig konfigurieren müssen, um das HTTPS-Zertifikat zu erhalten.


### Thema


BTCPay Server wird standardmäßig mit zwei Themen geliefert: Helle und dunkle Modi. Diese können durch Klicken auf Konto unten links und Umschalten zwischen dem dunklen und dem hellen Thema umgeschaltet werden. BTCPay Server-Administratoren können ihr eigenes Thema hinzufügen, indem sie ein benutzerdefiniertes CSS-Thema bereitstellen.


Administratoren können das Hell/Dunkel-Thema erweitern, indem sie ihr eigenes benutzerdefiniertes CSS hinzufügen oder ihr benutzerdefiniertes Thema als vollständig benutzerdefiniert festlegen.


![image](assets/en/084.webp)


#### Server-Branding


Server-Administratoren können das Branding von BTCPay Server ändern, indem sie ein serverweites Branding für Ihr Unternehmen festlegen. Da BTCPay Server FOSS ist, können Server-Administratoren die Software mit einem White-Label versehen und das Aussehen an ihr Unternehmen anpassen.


![image](assets/en/085.webp)


### Wartung


Als Server-Administrator erwarten Ihre Benutzer, dass Sie sich gut um den Server kümmern. Auf der Registerkarte "Wartung" von BTCPay Server kann der Administrator einige wichtige Wartungsarbeiten durchführen. Legen Sie den Domainnamen für die BTCPay Server-Instanz fest, starten Sie den Server neu oder bereinigen Sie ihn. Möglicherweise am wichtigsten: Updates ausführen.


BTCPay Server ist ein Open-Source-Projekt und wird häufig aktualisiert. Jede neue Version wird entweder über Ihre BTCPay Server-Benachrichtigungen oder über die offiziellen Kanäle, über die BTCPay Server kommuniziert, angekündigt.


![image](assets/en/086.webp)


#### Domänenname


Nach der Einrichtung von BTCPay Server kann es vorkommen, dass ein Administrator seine ursprüngliche Domain ändern möchte. Auf der Registerkarte "Wartung" kann der Administrator die Domain ändern. Nachdem er auf "Bestätigen" geklickt und die richtigen DNS-Einträge für die Domain eingerichtet hat, wird BTCPay Server aktualisiert und neu gestartet, um zur neuen Domain zurückzukehren.


![image](assets/en/087.webp)


#### Neustart


Starten Sie den BTCPay-Server und die zugehörigen Dienste neu.


![image](assets/en/088.webp)


#### Sauber


BTCPay Server wird mit Docker-Komponenten ausgeführt. Bei Aktualisierungen können Reste von Docker-Images, temporäre Dateien usw. übrig bleiben. Serveradministratoren können den Speicherplatz durch Ausführen des Skripts "Clean" freigeben.


![image](assets/en/089.webp)


#### Update


Dies ist die wichtigste Option auf der Registerkarte "Wartung". Da BTCPay Server von der Community entwickelt wird, sind die Aktualisierungszyklen häufiger als bei den meisten Softwareprodukten. Wenn es eine neue Version von BTCPay Server gibt, werden die Administratoren in ihrem Benachrichtigungszentrum benachrichtigt. Wenn Sie auf die Schaltfläche "Aktualisieren" klicken, wird BTCPay Server auf GitHub nach der neuesten Version suchen, den Server aktualisieren und neu starten. Vor der Aktualisierung sollten Server-Administratoren immer die Versionshinweise lesen, die über die offiziellen Kanäle von BTCPay Server verteilt werden.


![image](assets/en/090.webp)


### Protokolle


Mit einem Problem konfrontiert zu sein, ist nie lustig. Dieses Dokument beschreibt die häufigsten Arbeitsabläufe und Schritte, um Ihr Problem effizient zu identifizieren und zu lösen, entweder eigenständig oder mit Hilfe der Community.


Die Identifizierung des Problems ist entscheidend.


#### Replizieren des Problems


Versuchen Sie zuallererst herauszufinden, wann das Problem auftritt. Versuchen Sie, das Problem zu reproduzieren. Versuchen Sie, Ihren Server zu aktualisieren und neu zu starten, um zu überprüfen, ob Sie das Problem reproduzieren können. Wenn es Ihr Problem besser beschreibt, machen Sie einen Screenshot.


##### Aktualisierung des Servers


Überprüfen Sie Ihre Version von BTCPay Server, wenn sie viel älter ist als die [neueste Version](https://github.com/btcpayserver/btcpayserver/releases) von BTCPay Server. Eine Aktualisierung Ihres Servers kann das Problem beheben.


##### Neustart des Servers


Ein Neustart Ihres Servers ist eine einfache Möglichkeit, viele der häufigsten Probleme mit dem BTCPay-Server zu lösen. Möglicherweise müssen Sie sich per SSH in Ihren Server einloggen, um ihn neu starten zu können.


##### Neustart eines Dienstes


Es kann vorkommen, dass Sie nur einen bestimmten Dienst in Ihrer BTCPay Server-Installation neu starten müssen, z.B. den letsencrypt-Container neu starten, um das SSL-Zertifikat zu erneuern.


```bash
sudo su -
cd btcpayserver-docker
docker restart letsencrypt-nginx-proxy-companion
```


Verwenden Sie docker ps, um den Namen eines anderen Dienstes zu finden, den Sie neu starten möchten.


#### Durchsicht der Protokolle


Logs können wichtige Informationen liefern. In den folgenden Abschnitten wird beschrieben, wie Sie die Protokollinformationen für verschiedene Teile von BTCPay erhalten.


##### BTCPay-Protokolle


Seit v1.0.3.8 können Sie die BTCPay-Serverprotokolle ganz einfach über das Frontend abrufen. Wenn Sie ein Server-Administrator sind, gehen Sie zu Server-Einstellungen > Logs und öffnen Sie die Logs-Datei. Wenn Sie nicht wissen, was ein bestimmter Fehler in den Protokollen bedeutet, erwähnen Sie ihn bei der Fehlersuche.


Wenn Sie detailliertere Protokolle wünschen und eine Docker-Bereitstellung verwenden, können Sie die Protokolle bestimmter Docker-Container über die Befehlszeile anzeigen. Siehe diese [Anweisungen für ssh](https://docs.btcpayserver.org/FAQ/ServerSettings/#how-to-ssh-into-my-btcpay-running-on-vp%C2%80) in eine Instanz von BTCPay, die auf einem VPS läuft.


Auf der nächsten Seite finden Sie eine allgemeine Liste der Containernamen, die für BTCPay Server verwendet werden.


Führen Sie die folgenden Befehle aus, um Protokolle nach Containernamen zu drucken. Ersetzen Sie den Containernamen, um andere Containerprotokolle anzuzeigen.


```bash
sudo su -
cd btcpayserver-docker
docker ps
docker logs --tail 100 generated_btcpayserver_1
```



| Protokolle für | Containername                      |
| ------------ | --------------------------------- |
| BTCPayServer | generated_btcpayserver_1          |
| NBXplorer    | generated_nbxplorer_1             |
| Bitcoind     | btcpayserver_bitcoind             |
| Postgres     | generated_postgres_1              |
| proxy        | letsencrypt-nginx-proxy-companion |
| Nginx        | nginx-gen                         |
| Nginx        | nginx                             |
| c-lightning  | btcpayserver_clightning_bitcoin   |
| LND          | btcpayserver_lnd_bitcoin          |
| RTL          | generated_lnd_bitcoin_rtl_1       |
| Thunderhub   | generated_bitcoin_thub_1          |
| LibrePatron  | librepatron                       |
| Tor          | tor-gen                           |
| Tor          | tor                               |

###### Lightning Network LND - Docker


Es gibt mehrere Möglichkeiten, auf Ihre LND-Protokolle zuzugreifen, wenn Sie Docker verwenden. Melden Sie sich zunächst als root an:


```bash
sudo su -
Navigate to the correct directory:
cd btcpayserver-docker
# Find container name:
docker ps
Print logs by container name:
docker logs --tail 100 btcpayserver_lnd_bitcoin
```


Alternativ können Sie Protokolle schnell ausdrucken, indem Sie die Container-ID verwenden (es werden nur die ersten eindeutigen ID-Zeichen benötigt, z. B. die beiden am weitesten links stehenden Zeichen):


```bash
docker logs 'add your container ID'
```


Wenn Sie aus irgendeinem Grund mehr Protokolle benötigen


```bash
sudo su -
cd /var/lib/docker/volumes/generated_lnd_bitcoin_datadir/\_data/logs/ bitcoin/mainnet/
ls
```


Sie sehen dann etwas wie


```bash
lnd.log lnd.log.13 lnd.log.15 lnd.log.16.gz lnd.log.17.gz
```


Um auf unkomprimierte Protokolle dieser Protokolle zuzugreifen, verwenden Sie `cat LND.log` oder, wenn Sie ein anderes Protokoll wünschen, `cat LND.log.15`.


Um auf komprimierte Protokolle in `.gzip` zuzugreifen, verwenden Sie `gzip -d LND.log.16.gz` (in diesem Fall greifen wir auf `LND.log.16.gz` zu). Dadurch sollten Sie eine neue Datei erhalten, in der Sie `cat LND.log.16` ausführen können. Falls dies nicht funktioniert, müssen Sie eventuell zuerst gzip mit `sudo apt-get install gzip` installieren.


###### Lightning Network c-lightning - Docker


```bash
sudo su -
docker ps
# Find the c-lightning container ID.
docker logs 'add your container ID here'
```


Alternativ können Sie auch dies verwenden:


```bash
docker logs --tail 100 btcpayserver_clightning_bitcoin
```


Sie können auch mit dem Befehl c-lightning CLI Protokollinformationen abrufen.


```bash
bitcoin-lightning-cli.sh getlog
```


#### Bitcoin-Knotenprotokolle


Zusätzlich zum [Einsehen von Protokollen](https://docs.btcpayserver.org/Troubleshooting/#2-looking-through-the-logs) Ihres bitcoind-Containers können Sie auch einen der [bitcoin-cli-Befehle](https://developer.Bitcoin.org/reference/RPC/index.html) verwenden


[(öffnet ein neues Fenster)](https://developer.Bitcoin.org/reference/RPC/index.html), um Informationen von Ihrem Bitcoin-Knoten zu erhalten. BTCPay enthält ein Skript, mit dem Sie problemlos mit Ihrem Bitcoin-Knoten kommunizieren können.


Rufen Sie im Ordner btcpayserver-docker die Blockchain-Informationen über Ihren Knoten ab:


```bash
bitcoin-cli.sh getblockchaininfo
```


### Dateien


BTCPay Server verfügt über ein lokales Dateisystem, das es ermöglicht, Store- (Produkt-) Assets, Logos und Branding direkt auf den Server hochzuladen. Das Dateisystem des Servers ist nur für Server-Administratoren zugänglich; Shop-Besitzer können ihre Logos oder Branding auf der Ebene des Shops hochladen.


Wenn sich der Server-Administrator auf der Registerkarte Dateispeicher befindet, ist es möglich, direkt auf Ihren Server hochzuladen oder den Dateispeicheranbieter in ein lokales Dateisystem oder Azure Blob Storage zu ändern.


![image](assets/en/091.webp)


![image](assets/en/092.webp)


### Zusammenfassung der Fertigkeiten


In diesem Abschnitt haben Sie Folgendes gelernt:



- Der Unterschied zwischen Speicher- und Servereinstellungen, insbesondere in Bezug auf Benutzer, Rollen und E-Mails
- Legen Sie serverweite Richtlinien für die Verwendung und Erstellung von Lightning oder Bitcoin Hot Wallet, die Registrierung neuer Benutzer und E-Mail-Benachrichtigungen fest.
- Hinzufügen benutzerdefinierter Themen (anstelle der einfachen Hell/Dunkel-Optionen) sowie Erstellen benutzerdefinierter Logos
- Durchführung einfacher Server-Wartungsaufgaben über die mitgelieferte GUI
- Behebung von Problemen, einschließlich des Abrufs von Details für einen der Docker-Container oder Ihren Knoten
- Verwalten der Dateiablage


### Bewertung der Kenntnisse


#### KA Konzeptuelle Überprüfung


Worin besteht der Unterschied zwischen Rollen, die über Server- und Speichereinstellungen zugewiesen werden, und worin besteht der mögliche Vorteil der einen gegenüber der anderen?


#### KA Praktische Überprüfung


Beschreiben Sie einige mögliche Anwendungsfälle, die auf der Registerkarte "Richtlinien" aktiviert sind.


#### KA Praktische Überprüfung


Beschreiben Sie einige Aktionen, die ein Administrator routinemäßig auf der Registerkarte "Wartung" durchführen könnte.


## BTCPay Server - Zahlungen


<chapterId>e2b71ff9-3f4f-5e71-9771-8e03fbbef00f</chapterId>


Ein Invoice ist ein Dokument, das der Verkäufer einem Käufer ausstellt, um die Zahlung einzuziehen.


In BTCPay Server stellt ein Invoice ein Dokument dar, das innerhalb eines bestimmten Zeitraums zu einem festen Exchange-Kurs bezahlt werden muss. Rechnungen haben ein Verfallsdatum, weil sie den Exchange-Kurs innerhalb eines bestimmten Zeitrahmens festschreiben und den Empfänger vor Preisschwankungen schützen.


Das Herzstück von BTCPay Server ist die Fähigkeit, als Bitcoin Invoice-Verwaltungssystem zu fungieren. Ein Invoice ist ein unverzichtbares Werkzeug für die Verfolgung und Verwaltung eingegangener Zahlungen.


Sofern Sie nicht ein integriertes [Wallet](https://docs.btcpayserver.org/Wallet/) verwenden, um Zahlungen manuell zu empfangen, werden alle Zahlungen innerhalb eines Geschäfts auf der Seite Rechnungen angezeigt. Diese Seite sortiert die Zahlungen kumulativ nach Datum und dient als zentrale Ressource für die Invoice-Verwaltung und die Fehlerbehebung bei Zahlungen.


![image](assets/en/093.webp)


### Allgemein


#### Invoice-Status


In der folgenden Tabelle werden die Standard-Invoice-Status in BTCPay aufgelistet und beschrieben, zusammen mit Vorschlägen für allgemeine Maßnahmen. Die Maßnahmen sind lediglich Empfehlungen. Es liegt an den Benutzern, die beste Vorgehensweise für ihren Anwendungsfall und ihr Unternehmen zu definieren.



| Rechnungsstatus | Beschreibung | Aktion |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| New | Nicht bezahlt, Rechnungstimer ist noch nicht abgelaufen | Keine |
| New (paidPartial) | Teilweise bezahlt, Rechnungstimer ist noch nicht abgelaufen | Keine |
| Expired | Nicht bezahlt, Rechnungstimer abgelaufen | Keine |
| Expired (paidPartial) ** | Teilweise bezahlt und abgelaufen | Käufer kontaktieren, um Rückerstattung zu vereinbaren oder Restzahlung anfordern. Optional Rechnung als settled oder invalid markieren |
| Expired (paidLate) | Vollständig bezahlt, nachdem der Rechnungstimer abgelaufen war | Käufer kontaktieren, um Rückerstattung zu vereinbaren oder Bestellung bearbeiten, falls späte Bestätigungen akzeptabel sind. |
| Settled (paidOver) | Mehr als den Rechnungsbetrag bezahlt, abgerechnet, ausreichend Bestätigungen erhalten | Käufer kontaktieren, um Rückerstattung des Mehrbetrags zu vereinbaren, oder optional warten, bis der Käufer Sie kontaktiert |
| Processing | Vollständig bezahlt, aber noch nicht ausreichend Bestätigungen gemäß Shopeinstellungen erhalten | Käufer kontaktieren, um Rückerstattung des Mehrbetrags zu vereinbaren, oder optional warten, bis der Käufer Sie kontaktiert |
| Processing (paidOver) | Mehr als den Rechnungsbetrag bezahlt, noch nicht ausreichend Bestätigungen erhalten | Warten, bis der Status auf settled wechselt, dann Käufer für Rückerstattung kontaktieren oder auf Kontaktaufnahme warten |
| Settled | Vollständig bezahlt, ausreichend Bestätigungen im Shop erhalten | Bestellung ausführen |
| Settled (marked) | Status wurde manuell von processing oder invalid auf settled geändert | Shop-Admin hat die Zahlung als settled markiert |
| Invalid* | Bezahlt, aber innerhalb der Shopeinstellungen nicht ausreichend Bestätigungen erhalten | Transaktion im Blockchain-Explorer prüfen; falls ausreichend Bestätigungen vorliegen, als settled markieren |
| Invalid (marked) | Status wurde manuell von settled oder expired auf invalid geändert | Shop-Admin hat die Zahlung als invalid markiert |
| Invalid (paidOver) | Mehr als Rechnungsbetrag bezahlt, aber nicht ausreichend Bestätigungen innerhalb der Zeitvorgabe erhalten | Transaktion im Blockchain-Explorer prüfen; falls ausreichend Bestätigungen vorliegen, als settled markieren |

#### Invoice Einzelheiten


Die Detailseite des Invoice enthält alle Informationen zu einem Invoice.


Invoice-Informationen werden automatisch auf der Grundlage des Invoice-Status, des Exchange-Satzes usw. erstellt. Produktinformationen werden automatisch erstellt, wenn das Invoice mit Produktinformationen erstellt wurde, z. B. in der Point-of-Sale-App.


#### Invoice-Filterung


Rechnungen können über die Schnellfilter neben der Schaltfläche "Suchen" oder die erweiterten Filter gefiltert werden, die durch Klicken auf den Link (Hilfe) am oberen Rand umgeschaltet werden können. Benutzer können Rechnungen nach Filiale, Bestell-ID, Artikel-ID, Status oder Datum filtern.


#### Invoice Ausfuhr


BTCPay Server-Rechnungen können im CSV- oder JSON-Format exportiert werden. Für weitere Informationen über Invoice Export und Buchhaltung.


#### Erstattung eines Invoice


Wenn Sie aus irgendeinem Grund eine Erstattung ausstellen möchten, können Sie eine Erstattung ganz einfach über die Ansicht Invoice erstellen.


#### Archivierung von Rechnungen


Da BTCPay Server keine Address-Wiederverwendung zulässt, werden häufig viele abgelaufene Rechnungen auf der Invoice-Seite Ihres Shops angezeigt. Um diese auszublenden, wählen Sie sie in der Liste aus und markieren Sie sie als archiviert. Rechnungen, die als archiviert markiert wurden, werden nicht gelöscht. Die Zahlung auf eine archivierte Invoice wird weiterhin von Ihrem BTCPay-Server erkannt (paidLate-Status). Sie können die archivierten Rechnungen des Shops jederzeit einsehen, indem Sie archivierte Rechnungen aus dem Suchfilter-Dropdown auswählen.


#### Standardwährung


Standardwährung der Filiale, die im Assistenten zur Filialerstellung festgelegt wurde.


#### Jedem erlauben, einen Invoice zu erstellen


Sie sollten diese Option aktivieren, wenn Sie es der Außenwelt erlauben wollen, Rechnungen in Ihrem Shop zu erstellen. Diese Option ist nur sinnvoll, wenn Sie die Zahlungstaste verwenden oder wenn Sie Rechnungen über eine API oder eine HTML-Website eines Drittanbieters ausstellen. Die PoS-App ist vorautorisiert und erfordert nicht, dass diese Einstellung aktiviert wird, damit ein zufälliger Besucher Ihren POS-Shop öffnen und eine Invoice erstellen kann.


#### Hinzufügen einer zusätzlichen Gebühr (Netzgebühr) zum Invoice



- Nur wenn der Kunde mehr als eine Zahlung für das Invoice leistet
- Bei jeder Zahlung
- Niemals eine Netzgebühr hinzufügen


#### Invoice verfällt, wenn der volle Betrag nicht nach ... Minuten gezahlt wurde.


Der Timer des Invoice ist standardmäßig auf 15 Minuten eingestellt. Der Timer dient als Schutzmechanismus gegen Volatilität, da er den Kryptowährungsbetrag auf der Grundlage der Krypto-zu-Fiat-Kurse sperrt. Wenn der Kunde die Invoice nicht innerhalb des festgelegten Zeitraums bezahlt, wird die Invoice als verfallen betrachtet. Die Invoice gilt als "bezahlt", sobald die Transaktion auf der Blockchain sichtbar ist (mit null Bestätigungen), und wird als "abgeschlossen" betrachtet, wenn sie die vom Händler festgelegte Anzahl von Bestätigungen erreicht hat (normalerweise 1-6). Der Timer ist anpassbar.


#### Betrachten Sie den Invoice als gezahlt, auch wenn der gezahlte Betrag um ..% geringer ist als erwartet.


Wenn ein Kunde einen Exchange Wallet verwendet, um direkt für einen Invoice zu bezahlen, nimmt der Exchange eine kleine Gebühr. Dies bedeutet, dass ein solcher Invoice nicht als vollständig abgeschlossen gilt. Die Invoice wird als "teilweise bezahlt" gekennzeichnet Wenn ein Händler unterbezahlte Rechnungen akzeptieren möchte, können Sie hier den Prozentsatz festlegen


### Anfragen an


Zahlungsanfragen sind eine Funktion, mit der BTCPay-Shop-Besitzer langlebige Rechnungen erstellen können. Gelder werden entsprechend der Zahlungsanforderung mit dem zum Zeitpunkt der Zahlung gültigen Exchange-Kurs gezahlt. Dies ermöglicht es den Benutzern, Zahlungen nach eigenem Ermessen vorzunehmen, ohne dass sie zum Zeitpunkt der Zahlung Exchange-Kurse mit dem Geschäftsinhaber aushandeln oder überprüfen müssen.


Benutzer können für Anfragen in Teilbeträgen bezahlen. Die Zahlungsanforderung bleibt so lange gültig, bis sie vollständig bezahlt ist, oder wenn der Geschäftsinhaber eine Verfallszeit vorschreibt. Adressen werden nicht wiederverwendet. Jedes Mal, wenn der Benutzer auf "Bezahlen" klickt, wird eine neue Address generiert, um eine Invoice für die Zahlungsanforderung zu erstellen.


Ladenbesitzer können Zahlungsanforderungen ausdrucken (oder Invoice-Daten exportieren), um Aufzeichnungen und Buchhaltung zu führen. BTCPay kennzeichnet Rechnungen automatisch als Zahlungsanforderung in der Invoice-Liste Ihres Shops.


#### Anpassen Ihrer Zahlungsaufforderungen



- Invoice Betrag - Angeforderten Zahlungsbetrag festlegen
- Denomination - Angeforderten Betrag in Fiat oder Kryptowährung anzeigen
- Zahlungsmenge - Nur Einzelzahlungen oder Teilzahlungen zulassen
- Verfallszeit - Zahlungen bis zu einem bestimmten Datum oder ohne Verfallsdatum zulassen
- Beschreibung - Texteditor, Datentabellen, Fotos und Videos einbetten
- Erscheinungsbild - Farbe und Stil mit CSS-Themen


![image](assets/en/094.webp)


#### Eine Zahlungsanforderung erstellen


Gehen Sie im linken Menü auf Zahlungsantrag und klicken Sie auf "Zahlungsantrag erstellen".


![image](assets/en/095.webp)


Geben Sie den Anforderungsnamen, den Betrag, die angezeigte Stückelung, das zugehörige Geschäft, die Ablaufzeit und die Beschreibung an (optional)


Wählen Sie die Option Zahlungsempfängern erlauben, Rechnungen in ihrer Stückelung zu erstellen, wenn Sie Teilzahlungen zulassen möchten.


Klicken Sie auf Speichern & Anzeigen, um Ihren Zahlungsantrag zu überprüfen.


BTCPay erstellt eine URL für die Zahlungsanforderung. Geben Sie diese URL frei, um Ihre Zahlungsanforderung anzuzeigen. Benötigen Sie mehrere Anfragen der gleichen Art? Sie können Zahlungsanfragen duplizieren, indem Sie die Option "Klonen" im Hauptmenü verwenden.


![image](assets/en/096.webp)


**WARNUNG**


Zahlungsanordnungen sind filialabhängig, d. h. jede Zahlungsanordnung wird bei der Erstellung mit einer Filiale verknüpft. Stellen Sie sicher, dass ein Wallet mit der Filiale verbunden ist, zu der die Zahlungsanforderung gehört.


#### Bezahlte Anfrage


Der Zahlungsempfänger und der Antragsteller können den Status der Zahlungsanforderung einsehen, nachdem die Zahlung gesendet wurde. Der Status lautet "Beglichen", wenn die Zahlung in voller Höhe eingegangen ist. Wurden nur Teilzahlungen geleistet, wird unter Fälliger Betrag der Restsaldo angezeigt.


![image](assets/en/097.webp)


#### Zahlungsaufforderungen anpassen


Der Inhalt der Beschreibung kann mit dem Texteditor der Zahlungsanforderung bearbeitet werden. Beide Optionen sind verfügbar, wenn Sie zusätzliche Farbthemen oder benutzerdefiniertes CSS-Styling verwenden möchten.


Nicht-technische Benutzer können ein [bootstrap theme](https://docs.btcpayserver.org/Development/Theme/#2-bootstrap-themes) verwenden. Weitere Anpassungen können durch die Bereitstellung von zusätzlichem CSS-Code vorgenommen werden, wie unten gezeigt.


```css
:root {
--btcpay-font-family-base: "Source Sans Pro", -apple-system,
BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
--btcpay-primary: #7d4698;
--btcpay-primary-accent: #59316b;
--btcpay-body-text: #333a41;
--btcpay-body-bg: #fff;
--btcpay-bg-tile: #f8f9fa;
}

#mainNav {
color: white;
background: linear-gradient(#59316b, #331840);
}

#mainNav .btn-link {
color: white;
}
```


### Zahlungen abrufen


Traditionell gibt ein Empfänger sein Bitcoin Address frei, um eine Bitcoin-Zahlung zu tätigen, und der Sender sendet später Geld an dieses Address. Ein solches System wird als Push-Zahlung bezeichnet, da der Absender die Zahlung initiiert, während der Empfänger möglicherweise nicht verfügbar ist, und die Zahlung an den Empfänger schiebt.


Aber wie wäre es, die Rolle umzukehren?


Wie wäre es, wenn der Sender die Zahlung nicht schiebt, sondern dem Empfänger erlaubt, die Zahlung zu einem Zeitpunkt abzuziehen, den der Empfänger für richtig hält? Das ist das Konzept der Pull-Zahlung. Dies ermöglicht mehrere neue Anwendungen, wie zum Beispiel:



- Ein Abonnementdienst (bei dem der Abonnent dem Dienst erlaubt, alle x Jahre Geld abzuheben)
- Rückerstattungen (wenn der Händler dem Kunden erlaubt, das Geld für die Rückerstattung auf seinen Wallet zu ziehen, wenn er es für richtig hält)
- Zeitabhängige Abrechnung für Freiberufler (wobei der Auftraggeber dem Freiberufler erlaubt, Geld in seinen Wallet einzuziehen, wenn die Zeit gemeldet wird)
- Mäzenatentum (wenn der Mäzen dem Empfänger erlaubt, jeden Monat Geld abzuheben, um seine Arbeit weiterhin zu unterstützen)
- Automatischer Verkauf (wenn ein Kunde eines Exchange einem Exchange erlaubt, jeden Monat automatisch Geld von seinem Wallet abzuziehen, um zu verkaufen)
- System zur Abhebung von Guthaben (ein Dienst mit hohem Volumen ermöglicht es den Nutzern, Abhebungen von ihrem Guthaben anzufordern; der Dienst kann dann problemlos alle Auszahlungen an viele Nutzer in festen Abständen vornehmen)


### Auszahlungen


Die Auszahlungsfunktion ist an die Funktion [Pull Payments](https://docs.btcpayserver.org/PullPayments/) gebunden. Diese Funktion ermöglicht es Ihnen, Auszahlungen innerhalb Ihres BTCPay zu erstellen. Mit dieser Funktion können Sie Pull-Zahlungen (Erstattungen, Gehaltsauszahlungen oder Abhebungen) verarbeiten.


#### Beispiel 1: Erstattung


Beginnen wir mit dem Beispiel der Rückerstattung. Der Kunde hat einen Artikel in Ihrem Geschäft gekauft, muss ihn aber leider zurückgeben. Er möchte eine Rückerstattung. Innerhalb von BTCPay können Sie eine [Rückerstattung](https://docs.btcpayserver.org/Refund/) erstellen und dem Kunden den Link zur Verfügung stellen, über den er sein Geld anfordern kann. Sobald der Kunde seine Address angegeben und das Geld eingefordert hat, wird es im Abschnitt Auszahlungen angezeigt.


Der erste Status, den es hat, ist Warten auf Genehmigung. Die Mitarbeiter in der Filiale können prüfen, ob mehrere Anträge vorliegen, und nachdem sie eine Auswahl getroffen haben, verwenden sie die Schaltfläche "Aktionen".


Optionen auf der Aktionsschaltfläche



- Ausgewählte Auszahlungen genehmigen
- Ausgewählte Auszahlungen genehmigen und versenden
- Ausgewählte Auszahlungen stornieren


Der nächste Schritt besteht darin, ausgewählte Auszahlungen zu genehmigen und zu senden, da wir dem Kunden den Betrag erstatten wollen. Überprüfen Sie den Address des Kunden, der den Betrag anzeigt und angibt, ob die Gebühren von der Erstattung abgezogen werden sollen oder nicht. Wenn Sie die Prüfungen abgeschlossen haben, müssen Sie die Transaktion nur noch unterschreiben.


Der Kunde wird nun auf der Claiming-Seite aktualisiert. Er kann die Transaktion verfolgen, da er einen Link zu einem Block explorer und seiner Transaktion erhält. Sobald die Transaktion bestätigt wurde, ändert sich ihr Status in "Abgeschlossen".


#### Beispiel 2: Gehalt


Kommen wir nun zur Auszahlung von Gehältern, da diese von der Filiale aus gesteuert wird und nicht auf Anfrage des Kunden erfolgt. Das zugrundeliegende Konzept ist dasselbe; es verwendet Pull-Zahlungen. Aber anstatt eine Rückzahlung zu erstellen, werden wir eine [Pull-Zahlung](https://docs.btcpayserver.org/PullPayments/) vornehmen.


Gehen Sie auf die Registerkarte Pull-Zahlungen auf Ihrem BTCPay-Server. Klicken Sie oben rechts auf die Schaltfläche Pull-Zahlung erstellen.


Jetzt sind wir bei der Erstellung der Auszahlung, geben Sie ihr einen Namen und den gewünschten Betrag in der gewählten Währung. Füllen Sie die Beschreibung aus, damit der Mitarbeiter weiß, worum es sich handelt. Der nächste Teil ist ähnlich wie bei Erstattungen. Der Mitarbeiter füllt das Ziel Address und den Betrag aus, den er von dieser Auszahlung beanspruchen möchte. Er kann sich dafür entscheiden, zwei getrennte Anträge zu stellen, die an verschiedene Adressen gerichtet sind, oder sogar einen Teil des Anspruchs über einen Blitz abzurechnen.


Wenn mehrere Auszahlungen anstehen, können Sie diese stapelweise unterschreiben und versenden. Nach der Unterzeichnung werden die Auszahlungen in die Registerkarte "In Bearbeitung" verschoben und zeigen die Transaktion an. Wenn die Auszahlung vom Netzwerk akzeptiert wurde, wird sie auf die Registerkarte "Abgeschlossen" verschoben. Die Registerkarte "Erledigt" dient nur zu historischen Zwecken. Er enthält die verarbeiteten Auszahlungen und die dazugehörigen Transaktionen


### Zahlungen abrufen


#### Konzept


Wenn ein Absender eine Pull-Zahlung konfiguriert, kann er eine Reihe von Eigenschaften einstellen:



- Pull-Anfrage Name
- Ein Grenzbetrag
- Eine Einheit (z. B. BTC, SAT, USD)
- Zahlungsarten
  - BTC On-Chain
  - BTC off-chain
- Beschreibung
- Benutzerdefiniertes CSS
- Enddatum (fakultativ für Lightning Network BOLT11)


Danach kann der Sender die Pull-Zahlung über einen Link mit dem Empfänger teilen, so dass der Empfänger eine Auszahlung erstellen kann. Der Empfänger wählt seine Auszahlung aus:



- Welche Zahlungsmethode ist zu verwenden?
- Wohin soll das Geld geschickt werden?


Sobald eine Auszahlung erstellt ist, wird sie auf das Limit der Abrufzahlung für den aktuellen Zeitraum angerechnet. Der Absender genehmigt dann die Auszahlung, indem er den Satz festlegt, zu dem die Auszahlung gesendet werden soll, und führt die Zahlung durch.


Für den Absender bieten wir eine einfach zu bedienende Methode für das Stapeln von mehreren Auszahlungen aus dem [BTCPay Internal Wallet](https://docs.btcpayserver.org/Wallet/).


#### Greenfield API


BTCPay Server bietet eine vollständige API sowohl für den Sender als auch für den Empfänger, die auf der Seite `/docs` Ihrer Instanz dokumentiert ist. (oder auf der Dokumentations-Website https://docs.btcpayserver.org)


Da unsere API die volle Leistungsfähigkeit von Pull-Zahlungen bietet, kann ein Absender die Zahlungen nach seinen eigenen Bedürfnissen automatisieren.


### Zusammenfassung der Fertigkeiten


In diesem Abschnitt haben Sie Folgendes gelernt:



- Eingehendes Verständnis der Invoice-Status des BTCPay-Servers sowie der Aktionen, die mit ihnen durchgeführt werden können
- Anpassen und Verwalten von Invoice-Mechanismen mit verlängerter Lebensdauer, den so genannten Requests.
- Die zusätzlichen flexiblen Zahlungsmöglichkeiten, die sich mit der einzigartigen Pull-Payment-Funktion von BTCPay Server eröffnen, insbesondere bei der Abwicklung von Rückzahlungen und Gehaltszahlungen.


### Bewertung der Kenntnisse


#### KA Konzeptuelle Überprüfung


Worin bestehen die Unterschiede zwischen Rechnungen und Zahlungsaufforderungen, und was könnte ein guter Grund für die Verwendung der letzteren sein?


#### KA Konzeptuelle Überprüfung


Wie erweitern Pull-Zahlungen das, was normalerweise mit On-Chain gemacht werden kann? Beschreiben Sie einige Anwendungsfälle, die sie ermöglichen.


## BTCPay Server Standard-Plugins


<chapterId>7d673dc4-bd5d-5411-819b-f135f1d86636</chapterId>


### Standard-Plugins und Anwendungen


BTCPay Server wird mit einem Standardsatz von Plugins (Apps) geliefert, die BTCPay Server in ein E-Commerce-Zahlungsgateway verwandeln können. Mit der Hinzufügung eines Point of Sale, einer Crowdfunding-Plattform und einer einfachen Bezahlfunktion wird BTCPay Server zu einer einfach zu implementierenden Lösung.


### Verkaufsstelle


Eines der Standard-Plugins von BTCPay Server ist Point of Sale (PoS). Mit dem PoS-Plugin kann ein Ladenbesitzer einen Webshop direkt von BTCPay Server aus erstellen; der Ladenbesitzer benötigt keine E-Commerce-Lösungen von Dritten, um einen Webshop zu betreiben. Die webbasierte PoS-App ermöglicht es Nutzern mit stationären Geschäften, Bitcoin einfach und ohne Gebühren oder einen Dritten direkt in ihr Wallet zu akzeptieren. Der PoS kann einfach auf Tablets oder anderen Geräten angezeigt werden, die Webbrowsing unterstützen. Benutzer können einfach eine Verknüpfung auf dem Startbildschirm erstellen, um schnell auf die Web-App zuzugreifen.


#### So erstellen Sie einen neuen Point of Sale


BTCPay Server ermöglicht es Ladenbesitzern, schnell einen Point of Sale in verschiedenen Layouts zu erstellen. BTCPay Server erkennt an, dass nicht jedes Geschäft E-Commerce ist, und nicht jedes Geschäft ist eine Bar oder ein Restaurant, und es kommt mit mehreren Standard-Setups für Ihre PoS.


Wenn der Shop-Betreiber in der linken Menüleiste auf "Point of Sale" klickt, fragt BTCPay Server nun nach einem Namen, der in der linken Menüleiste sichtbar ist. Klicken Sie auf Erstellen, um den PoS zu erstellen.


![image](assets/en/098.webp)


#### Aktualisieren Sie den neu erstellten Point of Sale


Nachdem Sie einen neuen PoS erstellt haben, können Sie auf dem folgenden Bildschirm Ihren Point of Sale aktualisieren und Artikel für Ihr Geschäft hinzufügen.


##### App-Name


Der hier vergebene Name Ihres Point of Sale wird im Hauptmenü des BTCPay Servers sichtbar sein.


##### Titel anzeigen


Die Öffentlichkeit wird den Titel oder den Namen Ihres Shops sehen, wenn sie ihn besucht. BTCPay Server nennt Ihren Shop standardmäßig "Tee-Shop" Ersetzen Sie dies durch den Namen Ihres Shops.


![image](assets/en/099.webp)


#### Wählen Sie den Verkaufsstellenstil


BTCPay Server ist in der Lage, seinen Point of Sale auf mehrere Arten darzustellen.



- Produktliste
  - Eine Shop-Ansicht, in der Kunden jeweils nur 1 Produkt kaufen können.
- Produktliste mit einem Warenkorb.
  - Eine Shop-Ansicht, in der Kunden mehrere Artikel auf einmal kaufen können und eine Warenkorbübersicht auf der rechten Seite ihres Bildschirms erhalten.
- Nur Tastenfeld
  - Keine Produktliste, nur ein Tastenfeld für die direkte Rechnungsstellung.
- Druckanzeige (Druckbare Produktliste mit QR)
  - Wenn Sie Ihre Produktliste nicht immer digital anzeigen können, benötigen Sie eine "Offline"-Lösung für Produkte; BTCPay Server verfügt über eine Druckanzeige, die als Offline-Store funktioniert.


![image](assets/en/100.webp)


#### Point Of Sale Style - Produktliste


![image](assets/en/101.webp)


#### Point of Sale Style - Produktliste + Warenkorb


![image](assets/en/102.webp)


#### Point of Sale Style - nur Tastenfeld


![image](assets/en/103.webp)


#### Point of Sale Style - Druckanzeige


![image](assets/en/104.webp)


#### Währung


Der Geschäftsinhaber kann für seinen Point of Sale eine andere Währung als die allgemein festgelegte Standardwährung festlegen. Die Standardwährung des Ladens füllt dieses Feld automatisch aus.


#### Beschreibung


Erzählen Sie der Welt von Ihrem Geschäft; was verkaufen Sie und für wie viel? Alles, was Ihr Geschäft erklärt, gehört hierher.


![image](assets/en/105.webp)


#### Produkte


Wenn ein Point of Sale erstellt wird, fügt ein Standard-BTCPay-Server dem Shop eine Reihe von Artikeln als Referenz hinzu. Klicken Sie auf die Schaltfläche "Bearbeiten" bei einem der Standardartikel, um die einzelnen möglichen Optionen für einen Artikel besser zu verstehen.


Das Anlegen eines neuen Produkts in Ihrem Geschäft umfasst die folgenden Felder;



- Titel
- Preis (Festpreis, Mindestpreis oder individuell)
- Bild-URL
- Beschreibung
- Bestandsaufnahme
- ID
- Kaufen Sie Button Text.
- Aktivieren/Deaktivieren


Sobald der Ladenbesitzer alle neuen Produktfelder ausgefüllt hat, klicken Sie auf "Speichern", und Sie werden feststellen, dass der Abschnitt "Produkte" in der Verkaufsstelle jetzt ausgefüllt wird. Speichern Sie immer in der oberen rechten Ecke Ihres Bildschirms, um zu verhindern, dass Ladenbesitzer ihren Fortschritt beim Hinzufügen von Produkten verlieren können.


Ladenbesitzer können auch den "Raw Editor" verwenden, um ihre Produkte zu konfigurieren. Der Raw-Editor erfordert ein grundlegendes Verständnis der JSON-Strukturen.


![image](assets/en/106.webp)


#### Kasse


BTCPay Server ermöglicht eine kleine PoS-spezifische Anpassung der Kasse. Der Shop-Betreiber kann den "Kaufen für x"-Text einstellen oder spezifische Kundendaten abfragen, indem er sie zu den Formularen hinzufügt.


#### Tipps


Nur einige Geschäfte benötigen die Option für Tipps zu ihren Verkäufen. Ladenbesitzer können dies ein- oder ausschalten, wie sie es für ihren Laden für richtig halten. Wenn der Shop die Option Trinkgeld aktiviert hat, kann der Shop-Betreiber den Text im Feld für das Trinkgeld selbst festlegen. BTCPay Server Trinkgelder basieren auf einem prozentualen Betrag. Shop-Besitzer können mehrere Prozentsätze, getrennt durch Kommas, eingeben.


#### Ermäßigungen


Als Geschäftsinhaber können Sie dem Kunden an der Kasse einen individuellen Rabatt gewähren; der Schalter für Rabatte wird an der Kasse Ihres Geschäfts verfügbar. Von der Verwendung von Self-Checkout-Systemen wird jedoch dringend abgeraten.


#### Kundenspezifische Zahlungen


Wenn die Option Benutzerdefinierte Zahlungen aktiviert ist, kann der Kunde einen Preis eingeben, der gleich oder höher ist als der ursprüngliche Invoice, der vom Geschäft generiert wurde.


#### Zusätzliche Optionen


Nachdem Sie alles für Ihren Point of Sale eingerichtet haben, bleiben noch einige zusätzliche Optionen übrig. Ladenbesitzer können ihren PoS einfach über einen Iframe einbetten oder eine Zahlungsschaltfläche einbetten, die mit einem bestimmten Ladenartikel verknüpft ist. Um den soeben erstellten PoS-Shop zu stylen, können die Besitzer am Ende der zusätzlichen Optionen benutzerdefinierte CSS hinzufügen.


#### Diese App löschen


Wenn der Ladenbesitzer den Point of Sale vollständig von seinem BTCPay-Server löschen möchte, kann er am Ende der Aktualisierung des PoS auf die Schaltfläche "Diese App löschen" klicken, um seine PoS-App vollständig zu löschen. Wenn Sie auf "Diese App löschen" klicken, bittet der BTCPay Server um eine Bestätigung, indem er "DELETE" eintippt und mit einem Klick auf die Schaltfläche "Löschen" bestätigt. Nach dem Löschen kehrt der Shop-Betreiber zum BTCPay Server Dashboard zurück.


### BTCPay Server - Crowdfunding


Neben dem Point-of-Sale-Plugin bietet BTCPay Server die Möglichkeit, einen Crowdfunding zu erstellen. Wie bei jeder anderen Crowdfunding-Plattform können Shop-Betreiber ein Ziel festlegen, Vergünstigungen für Beiträge erstellen und die Plattform an ihre Bedürfnisse anpassen.


#### Wie man einen neuen Crowdfunding-Fonds einrichtet


Klicken Sie auf das Crowdfund-Plugin im Hauptmenü auf der linken Seite Ihres BTCPay Servers, unterhalb der Rubrik Plugin. BTCPay Server fragt nun nach einem Namen für den Crowdfund; dieser Name wird auch in der linken Menüleiste angezeigt.


![image](assets/en/107.webp)


#### Aktualisieren Sie den neu erstellten Point of Sale


Sobald der App ein Name gegeben wurde, besteht der nächste Bildschirm darin, die App zu aktualisieren, damit sie einen Kontext hat.


#### App Name


Der Name, den Sie Ihrem Crowdfund gegeben haben, wird im Hauptmenü des BTCPay Servers sichtbar sein.


#### Titel anzeigen


Der Titel wird dem Crowdfunding für die Öffentlichkeit gegeben.


#### Tagline


Geben Sie dem Crowdfunding einen Einzeiler, um zu erkennen, worum es bei der Spendenaktion geht.


![image](assets/en/108.webp)


#### URL des vorgestellten Bildes


Jeder Crowdfund hat sein Hauptbild, das Banner, das Sie direkt erkennen. Dieses Bild kann auf Ihrem Server gespeichert werden, wenn Sie über administrative Rechte verfügen. Admins können es unter den BTCPay Server-Einstellungen - Dateien hochladen. Wenn Sie ein Store-Besitzer sind, muss das Bild über einen Drittanbieter-Host (z. B. Imgur) ins Internet hochgeladen werden.


#### Crowdfunding öffentlich machen


Mit diesem Schalter wird Ihr Crowdfunding öffentlich und damit für die Außenwelt sichtbar. Zu Testzwecken oder um zu sehen, ob Ihr Thema korrekt angewandt wird, lassen Sie diese Option für die Dauer der Erstellung des Crowdfundings auf AUS.


#### Beschreibung


Erzählen Sie der Welt von Ihrem Crowdfunding. Wofür sammeln Sie? Hier finden Sie alle Informationen zu Ihrem Crowdfunding.


![image](assets/en/109.webp)


#### Crowdfunding-Ziel


Legen Sie ein Ziel fest, was die Spendensammler für das Projekt einnehmen sollen und in welcher Währung das Ziel angegeben werden soll. Stellen Sie sicher, dass, wenn Ihre Ziele zwischen verschiedenen Daten festgelegt sind, diese Ziel- und Enddaten unter Ziele in Crowdfunding angegeben werden.


![image](assets/en/110.webp)


#### Vergünstigungen


Perks können Ihre Crowdfunding-Bemühungen erheblich verbessern. Der Grund dafür ist, dass Perks den Menschen eine Möglichkeit bieten, sich an Ihrer Kampagne zu beteiligen. Sie sprechen sowohl egoistische als auch wohlwollende Motivationen an. Und sie ermöglichen Ihnen den Zugriff auf die Ausgaben Ihrer Unterstützer, nicht nur auf deren philanthropischen Geldbeutel - Sie können sich denken, was wichtiger ist.


Die Erstellung einer neuen Vergünstigung umfasst die folgenden Felder.



- Titel
- Preis (Festpreis, Mindestpreis oder individuell)
- Bild-URL
- Beschreibung
- Bestandsaufnahme
- ID
- Kaufen Sie Button Text.
- Aktivieren/Deaktivieren


Sobald der Shop-Betreiber alle Felder der neuen Vergünstigung ausgefüllt hat, klicken Sie auf "Speichern" und Sie werden feststellen, dass der Abschnitt "Vergünstigungen" in der Crowdfunding-Datenbank nun ausgefüllt wird.


![image](assets/en/111.webp)


### BTCPay Server - Verkaufsstelle


#### Beiträge


Die Ladenbesitzer können wählen, wie sie die Perks anzeigen, wie sie sortiert werden oder sie sogar mit anderen Perks vergleichen. Sobald die Crowdfunding-Ziele erreicht sind, möchte der Shop-Betreiber jedoch möglicherweise den Spendenfluss für diese Spendenaktion stoppen. Daher kann er die Option "Nach Erreichen des Ziels keine weiteren Beiträge zulassen" aktivieren. Dadurch wird verhindert, dass der Crowdfund Spenden annimmt.


##### Crowdfunding-Verhalten


Der Standard von Crowdfund zählt nur Rechnungen, die mit Crowdfund erstellt wurden, für das Ziel. Es kann jedoch Fälle geben, in denen der Ladenbesitzer möchte, dass alle in diesem Laden erstellten Rechnungen für das Crowdfunding gezählt werden.


#### Zusätzliche Optionen für Anpassungen


BTCpay Server bietet eine Reihe von zusätzlichen Anpassungen. Fügen Sie dem Crowdfund Sounds, Animationen oder sogar Diskussionsstränge hinzu. Shop-Besitzer können auch das Erscheinungsbild des Crowdfunding ändern, indem sie ihr eigenes CSS eingeben.


#### Diese App löschen


Wenn der Shop-Betreiber den Crowdfund vollständig von seinem BTCPay-Server löschen möchte, kann er am Ende der Aktualisierung des Crowdfunds auf die Schaltfläche "Diese App löschen" klicken, um seine Crowdfund-App vollständig zu entfernen. Wenn er auf "Diese App löschen" klickt, bittet der BTCPay-Server um eine Bestätigung, indem er "DELETE" eintippt und mit einem Klick auf die Schaltfläche "Löschen" bestätigt. Nach dem Löschen kehrt der Shop-Betreiber zum BTCPay Server Dashboard zurück.


### BTCPay Server - Schaltfläche "Bezahlen


Einfach einzubettende HTML- und hochgradig anpassbare Zahlungsschaltflächen ermöglichen es Shop-Betreibern, Trinkgelder und Spenden zu erhalten. In der linken Menüleiste von BTCPay Server, unterhalb des Abschnitts "Plugins", können Shop-Betreiber auf "Bezahlbutton" und "Aktivieren" klicken, um einen Bezahlbutton zu erstellen.


#### Allgemeine Einstellungen


In den allgemeinen Einstellungen für den Zahlungsbutton können Ladenbesitzer Folgendes einstellen



- Standardpreis
- Standardwährung
- Standard-Zahlungsmethode
  - Standardeinstellungen des Ladens verwenden
  - BTC On-Chain
  - BTC off-chain (Blitz)
  - BTC off-chain (LNURL-pay)
- Beschreibung des Checkouts
- Bestell-ID


#### Optionen anzeigen


Die Zahlungsschaltfläche von BTCPay Server kann für verschiedene Stile konfiguriert werden. Die Schaltflächen können einen festen oder benutzerdefinierten Betrag haben, der entweder mit einem Schieberegler oder mit Plus- und Minus-Kippschaltern angezeigt wird.


#### Modal verwenden


Bei der Erstellung des Zahlungsbuttons können Shop-Betreiber das Verhalten beim Anklicken durch einen Kunden auswählen und ihn in einem Modal oder als neue Seite anzeigen.


**Anmerkung*


Warnung: Die Schaltfläche Zahlung sollte nur für Trinkgelder und Spenden verwendet werden


Die Verwendung des Zahlungsbuttons für E-Commerce-Integrationen wird nicht empfohlen, da der Benutzer bestellrelevante Informationen ändern kann. Für E-Commerce sollten Sie unsere Greenfield-API verwenden. Wenn dieser Shop kommerzielle Transaktionen verarbeitet, empfehlen wir, einen separaten Shop zu erstellen, bevor Sie die Zahlungsschaltfläche verwenden.


#### Text der Schaltfläche "Bezahlen" anpassen


Standardmäßig steht auf der Zahlungsschaltfläche von BTCPay Server "Mit BTCPay bezahlen". Shop-Besitzer können diesen Text nach ihren Wünschen einstellen und das BTCPay Server-Logo durch ihr eigenes ersetzen. Legen Sie den Text mit dem "Bezahlbutton-Text" fest und fügen Sie die Bild-URL unter "Bezahlbutton-Bild-URL" ein.


##### Bildgröße


Die Größe des Bildes auf der Schaltfläche kann nur auf drei Standardwerte eingestellt werden.



- 146x40px
- 168x46px
- 209x57px


#### Taste Typ


Der BTCPay Server kennt drei Zustände für den Payment Button.



- Fester Betrag
  - Der zuvor eingestellte Preis steht in den allgemeinen Einstellungen der Schaltfläche.
- Benutzerdefinierter Betrag
  - Die Schaltfläche "Bezahlen" auf dem BTCPay-Server verfügt über die Schaltflächen "+" und "-", um einen individuellen Preis festzulegen.
  - Wenn Sie den benutzerdefinierten Betrag verwenden, fragt der BTCPay-Server nach einem Minimal- und Maximalwert sowie nach dem Grad der Erhöhung.
  - Die Schaltflächen können auf "Einfache Eingabe" eingestellt werden, wodurch die +/- Toggles wegfallen.
  - Schaltfläche inline einpassen, wo Schaltfläche und Kippschalter inline erscheinen.
- Schieberegler
  - Ähnlich wie der benutzerdefinierte Betrag, jedoch ist er visuell anders, da er einen Schieberegler anstelle der +/- Kippschalter hat.
  - Wenn Sie den Schieberegler verwenden, fragt der BTCPay-Server nach einem Minimal- und Maximalwert sowie nach dem Grad der Erhöhung.


**Anmerkung*


Die Schaltfläche "Zahlung" kann oben in der Beschreibung der Warnung gelöscht werden.


#### Zahlungsbenachrichtigungen


Server IPN (Instant Payment Notification) ist für Webhooks konzipiert und kann mit einer URL zu Post-Purchase-Daten konfiguriert werden.


#### E-Mail-Benachrichtigungen


Wann immer eine Zahlung erfolgt ist, kann der BTCPay-Server den Geschäftsinhaber benachrichtigen.


#### Browser-Umleitung


Wenn der Kunde den Kauf abschließt, wird er zu diesem Link weitergeleitet, sofern der Geschäftsinhaber ihn eingerichtet hat.


#### Erweiterte Optionen für Zahlungsschaltflächen


Geben Sie zusätzliche Query-String-Parameter an, die an die Kassenseite angehängt werden sollen, sobald der Invoice erstellt ist. So würde zum Beispiel `lang=da-DK` die Kassenseite standardmäßig in Dänisch laden.


#### App als Endpunkt verwenden


Sie können die Zahlungstaste direkt mit einem Artikel in einer der PoS- oder Crowdfunding-Apps verknüpfen, die Sie bereits verwendet haben.


Ladenbesitzer können auf das Dropdown-Menü klicken und die gewünschte App auswählen. Sobald die App ausgewählt ist, kann der Ladenbesitzer den Artikel hinzufügen, der verknüpft werden soll.


#### Erstellter Code


Da es sich bei der Zahlungsschaltfläche von BTCPay Server um eine leicht einzubettende HTML-Datei handelt, zeigt BTCPay Server unten den generierten Code an, den Sie nach der Konfiguration der Zahlungsschaltfläche in eine Website kopieren können.


Ladenbesitzer können den generierten Code in ihre Website kopieren, und die Zahlungsschaltfläche vom BTCPay-Server ist direkt auf ihrer Website aktiv.


#### Zahlungsbenachrichtigungen


Server IPN (Instant Payment Notification) ist für Webhooks konzipiert und kann mit einer URL konfiguriert werden, um Kaufdaten zu veröffentlichen.


#### E-Mail-Benachrichtigungen


Jedes Mal, wenn eine Zahlung getätigt wird, kann der BTCPay-Server den Ladenbesitzer benachrichtigen.


#### Browser-Umleitung


Wenn der Kunde den Kauf abschließt, wird er zu diesem Link weitergeleitet, sofern der Geschäftsinhaber ihn eingerichtet hat.


#### Erweiterte Optionen für Zahlungsschaltflächen


Geben Sie zusätzliche Query-String-Parameter an, die an die Kassenseite angehängt werden sollen, sobald der Invoice erstellt ist. So würde zum Beispiel `lang=da-DK` die Kassenseite standardmäßig in Dänisch laden.


#### App als Endpunkt verwenden


Sie können die Zahlungstaste direkt mit einem Artikel in einer der PoS- oder Crowdfunding-Apps verknüpfen, die Sie zuvor verwendet haben. Ladenbesitzer können auf das Dropdown-Menü klicken und die gewünschte App auswählen. Sobald die App ausgewählt ist, kann der Ladenbesitzer den Artikel hinzufügen, der verknüpft werden soll.


#### Erstellter Code


Da es sich bei der Zahlungsschaltfläche von BTCPay Server um eine leicht einzubettende HTML-Datei handelt, zeigt BTCPay Server unten nach der Konfiguration der Zahlungsschaltfläche den generierten Code zum Kopieren in eine Website an. Shop-Betreiber können den generierten Code in ihre Website kopieren, und die Zahlungsschaltfläche von BTCPay Server ist direkt auf ihrer Website aktiv.


### Zusammenfassung der Fertigkeiten


In diesem Abschnitt haben Sie gelernt:



- Wie Sie mit dem integrierten PoS-Plugin von BTCPay Server ganz einfach einen eigenen Shop erstellen können
- Wie Sie mit dem integrierten Crowdfund-Plugin von BTCPay Server ganz einfach eine eigene Crowdfunding-App erstellen können
- Generierung von Code für eine benutzerdefinierte Bezahlschaltfläche mit dem Pay Button Plugin


### Bewertung der Kenntnisse


#### KA-Kritik


Welche drei integrierten Plugins sind standardmäßig in BTCPay Server enthalten? Beschreiben Sie in wenigen Worten, wie sie verwendet werden können.


# BTCPay-Server konfigurieren


<partId>ff38596c-7de3-5e5c-ba50-9b9edbbbb5eb</partId>


## Grundlegendes Verständnis der Installation von BTCPay Server auf einer LunaNode-Umgebung


<chapterId>d0a28514-ffcf-529b-9156-29141f0b060a</chapterId>


### Installation des BTCPay-Servers auf einer gehosteten Umgebung (LunaNode)


Diese Schritte liefern alle notwendigen Informationen, um mit der Nutzung von BTCPay Server auf LunaNode zu beginnen. Es gibt viele Möglichkeiten, die Software zu installieren.

Alle Details zum BTCPay Server finden Sie unter https://docs.btcpayserver.org.


#### Wo sollen wir anfangen?


In diesem Teil machen Sie sich mit LunaNode als Hosting-Anbieter vertraut, lernen die ersten Schritte zur Nutzung Ihres BTCPay-Servers kennen und erfahren, wie Sie Lightning Network nutzen können. Nachdem wir alle Schritte durchlaufen haben, können Sie einen Webshop oder eine Crowdfunding-Plattform betreiben, die Bitcoin akzeptiert!


Dies ist eine von vielen Möglichkeiten, den BTCPay Server einzusetzen. Lesen Sie unsere Dokumentation für weitere Details.


https://docs.btcpayserver.org.


### BTCPay Server - LunaNode Einsatz


#### LunaNode-Einsatz


Gehen Sie zunächst auf die Website von LunaNode.com, wo wir ein neues Konto erstellen werden. Klicken Sie auf "Sign Up" oben rechts oder verwenden Sie den "Get Started"-Assistenten auf der Homepage.


![image](assets/en/112.webp)


Nachdem Sie Ihr neues Konto erstellt haben, sendet LunaNode eine Bestätigungs-E-Mail. Sobald Sie das Konto verifiziert haben, wird Ihnen im Vergleich zu Voltage sofort die Möglichkeit geboten, Ihr Kontoguthaben aufzuladen. Dieses Guthaben ist notwendig, um den Serverplatz und die Hosting-Kosten zu decken.


![image](assets/en/113.webp)


#### Guthaben auf Ihr LunaNode-Konto aufladen


Sobald Sie auf "Guthaben einzahlen" geklickt haben, können Sie festlegen, mit wie viel Sie Ihr Konto aufladen und wie Sie dafür bezahlen möchten. LunaNode und BTCPay Server kosten zwischen $ 10 und $ 20 pro Monat.

Im Vergleich zu Voltage.cloud erhalten Sie vollen Zugriff auf Ihren Virtual Private Server (VPS) und haben somit mehr Kontrolle über Ihren Server. Nachdem Sie Ihr neues Konto erstellt haben, sendet LunaNode eine Bestätigungs-E-Mail.

Sobald Sie das Konto im Vergleich zu Voltage verifiziert haben, wird Ihnen sofort die Möglichkeit geboten, Ihr Guthaben aufzuladen. Dieses Guthaben ist notwendig, um die Kosten für den Serverplatz und das Hosting zu decken.


#### Wie wird ein neuer Server bereitgestellt?


In dieser Anleitung werden wir Sie durch den Einrichtungsprozess führen, indem wir eine Reihe von API-Schlüsseln erstellen und den von LunaNode entwickelten BTCPay Server Launcher verwenden.


Klicken Sie in Ihrem LunaNode-Dashboard oben rechts auf API. Daraufhin öffnet sich eine neue Seite. Wir müssen nur einen Namen für den API-Schlüssel festlegen. Der Rest wird von LunaNode erledigt und wird in diesem Leitfaden nicht behandelt. Klicken Sie auf die Schaltfläche API-Zugangsdaten erstellen.

Nach der Erstellung der API-Anmeldeinformationen erhalten Sie eine lange Reihe von Buchstaben und Zeichen. Dies ist Ihr API-Schlüssel.


![image](assets/en/114.webp)


#### Wie wird ein neuer Server bereitgestellt?


Diese Anmeldedaten bestehen aus zwei Teilen, dem API-Schlüssel und der API-ID; wir benötigen beide. Bevor wir zum nächsten Schritt übergehen, öffnen wir einen zweiten Tab im Browser und gehen auf https://launchbtcpay.lunanode.com/


Hier werden Sie aufgefordert, Ihren API-Schlüssel und Ihre API-ID anzugeben. Dies dient dazu, Sie wissen zu lassen, dass Sie derjenige sind, der diesen neuen Server bereitgestellt hat. Der API-Schlüssel sollte noch in Ihrem vorherigen Tab geöffnet sein; wenn Sie in der Tabelle unten nach unten scrollen, finden Sie die API-ID.


Sie können zur Seite mit dem Launcher zurückkehren, die Felder mit Ihrem API-Schlüssel und Ihrer ID ausfüllen und auf "Weiter" klicken.


![image](assets/en/115.webp)


Im nächsten Schritt können Sie einen Domainnamen angeben. Wenn Sie bereits eine Domain besitzen und diese für BTCPay Server verwenden möchten, stellen Sie sicher, dass Sie auch den DNS-Eintrag (genannt `A`-Eintrag) auf Ihrer Domain hinzufügen. Wenn Sie keine Domain besitzen, verwenden Sie stattdessen die von LunaNode zur Verfügung gestellte Domain (Sie können dies später in den BTCPay Server-Einstellungen ändern) und klicken Sie auf Weiter.


Lesen Sie mehr über das Einrichten oder Ändern eines DNS-Eintrags für BTCPay Server; https://docs.btcpayserver.org/FAQ/Deployment/#how-to-change-your-btcpay-server-domain-name


#### BTCPay-Server auf LunaNode starten


Nachdem wir die vorherigen Schritte durchgeführt haben, können wir alle Optionen für unseren neuen Server einstellen. Hier werden wir Bitcoin (BTC) als unterstützte Währung auswählen. Wir können auch eine E-Mail einrichten, um Benachrichtigungen über Verschlüsselungszertifikate für Erneuerungszwecke zu erhalten, was optional ist.


Dieser Leitfaden zielt darauf ab, eine Mainnet-Umgebung einzurichten (in der realen Welt Bitcoin); LunaNode ermöglicht jedoch auch die Einstellung auf Testnet oder Regtest für Entwicklungszwecke. Für diese Anleitung belassen wir es bei der Option Mainnet.


Sie können Ihre Lightning-Implementierung wählen. LunaNode bietet zwei verschiedene Implementierungen an, LND und Core Lightning. Für diesen Leitfaden werden wir LND verwenden. Es gibt nur wenige, aber echte Unterschiede zwischen den beiden Implementierungen; um mehr darüber zu erfahren, empfehlen wir die Lektüre der umfangreichen Dokumentation: https://docs.btcpayserver.org/LightningNetwork#getting-started-with-btcpay-server-and-core-lightning-cln


![image](assets/en/116.webp)


LunaNode bietet mehrere Virtual Machine (VM)-Pläne an. Diese unterscheiden sich in Bezug auf die Preisspanne und die Serverspezifikationen. Für diesen Leitfaden reicht ein m2-Plan aus; wenn Sie jedoch mehr als nur Bitcoin als Währung gewählt haben, sollten Sie mindestens einen m4-Plan in Betracht ziehen.


Beschleunigen Sie die anfängliche Blockchain-Synchronisierung; dies ist optional und hängt von Ihren Bedürfnissen ab. Es gibt erweiterte Optionen wie das Festlegen eines Lightning-Alias, das Verweisen auf eine bestimmte GitHub-Version oder das Festlegen von SSH-Schlüsseln, die in diesem Leitfaden nicht behandelt werden.


Nachdem Sie das Formular ausgefüllt haben, klicken Sie auf "Launch VM" und Lunanode beginnt mit der Erstellung Ihrer neuen VM, einschließlich des darauf installierten BTCPay Servers. Dieser Prozess dauert ein paar Minuten; sobald Ihr Server fertig ist, gibt LunaNode Ihnen den Link zu Ihrem neuen BTCPay Server.


Nach dem Erstellungsprozess klicken Sie auf den Link zu Ihrem BTCPay-Server; hier werden Sie aufgefordert, ein Administratorkonto zu erstellen.


![image](assets/en/117.webp)


### Zusammenfassung der Fertigkeiten


In diesem Abschnitt haben Sie gelernt:



- Ein Konto auf LunaNode erstellen und finanzieren
- Verwenden Sie den BTCPay Server Launcher, um Ihren eigenen Server zu erstellen


### Bewertung der Kenntnisse


#### KA Konzeptuelle Überprüfung


Beschreiben Sie einige der Unterschiede zwischen dem Betrieb einer Instanz von BTCPay Server auf einem VPS und der Erstellung eines Kontos auf einer gehosteten Instanz.


## Installation von BTCPay Server in einer Spannungsumgebung


<chapterId>11c7d284-b4d2-5542-872c-df9bd9c1491b</chapterId>


Sie werden mit Voltage.cloud als Hosting-Provider vertraut gemacht, lernen die ersten Schritte zur Nutzung Ihres BTCPay-Servers kennen und erfahren, wie Sie das Lightning Network verwenden. Nachdem wir alle Schritte durchlaufen haben, können Sie einen Webshop oder eine Crowdfunding-Plattform betreiben, die Bitcoin akzeptiert!


Dies ist eine von vielen Möglichkeiten, den BTCPay Server einzusetzen. Lesen Sie unsere Dokumentation für weitere Details.

https://docs.btcpayserver.org.


### BTCPay Server - Voltage.cloud Bereitstellung


Rufen Sie zunächst die Website Voltage.cloud auf und melden Sie sich für ein neues Konto an. Wenn Sie ein Konto erstellen, können Sie sich für eine kostenlose 7-Tage-Testversion anmelden. Klicken Sie entweder auf "Sign Up" oben rechts oder nutzen Sie die Option "Try a free 7-day trial" auf der Homepage.


![image](assets/en/118.webp)


Nachdem Sie ein Konto erstellt haben, klicken Sie auf Ihrem Dashboard auf die Schaltfläche "NODES". Sobald wir Nodes ausgewählt und einen neuen Node erstellt haben, werden wir mit den möglichen Node-Angeboten von Voltage konfrontiert. Da in diesem Leitfaden auch der Lightning Network behandelt wird, müssen wir bei Voltage zunächst unsere Lightning-Implementierung auswählen, bevor wir einen BTCPay-Server erstellen. Klicken Sie auf LightningNode.


![image](assets/en/119.webp)


Hier müssen Sie auswählen, welche Art von Beleuchtungsknoten Sie wünschen. Voltage bietet eine Vielzahl von Optionen für Ihre Beleuchtungseinrichtung. Dies ist anders, wenn Sie z. B. mit LunaNode arbeiten. Für den Zweck dieses Leitfadens ist ein Lite Node ausreichend. Lesen Sie mehr über die Unterschiede in Voltage.cloud.


![image](assets/en/120.webp)


Geben Sie Ihrem Knoten einen Namen, legen Sie ein Kennwort fest, und sichern Sie dieses Kennwort. Wenn dieses Kennwort verloren geht, verlieren Sie den Zugriff auf Ihre Backups, und Voltage kann es nicht wiederherstellen. Erstellen Sie den Knoten, und Voltage zeigt Ihnen den Fortschritt an. Voltage hat Ihren Lightning-Knoten erstellt. Wir können nun die BTCPay Server-Instanz erstellen und direkt auf den Lightning Network zugreifen.


Klicken Sie oben links in Ihrem Dashboard auf Nodes. Hier können Sie den nächsten Teil Ihrer BTCPay Server-Instanz einrichten. Klicken Sie auf "Neu erstellen", sobald Sie sich in der Knotenübersicht befinden. Sie erhalten einen ähnlichen Bildschirm wie zuvor. Anstelle von Lightning Node wählen wir jetzt BTCPay Server.


Voltage zeigt Ihnen die Geolokation Ihres BTCPay-Servers, der in der Region US West gehostet wird. Hier sehen Sie auch die Kosten für das Hosting des Servers. Klicken Sie auf Erstellen und geben Sie Ihrem BTCPay-Server einen Namen. Aktivieren Sie Lightning und Voltage zeigt Ihnen den im vorherigen Schritt erstellten Lightning-Knoten an. Klicken Sie auf Create (Erstellen), und Voltage erstellt eine BTCPay Server-Instanz.


![image](assets/en/121.webp)


Nachdem Sie auf "Erstellen" geklickt haben, zeigt Voltage Ihnen den Standardbenutzernamen und das Standardkennwort an. Diese sind ähnlich wie Ihr zuvor festgelegtes Passwort in Voltage. Klicken Sie auf die Schaltfläche "Login to Account", um Sie zu Ihrem BTCPay-Server weiterzuleiten.


Willkommen auf Ihrer neuen BTCPay Server-Instanz. Da wir Lightning bereits während des Erstellungsprozesses eingerichtet haben, zeigt es Ihnen, dass Lightning bereits aktiviert ist!


### Zusammenfassung der Fertigkeiten


In diesem Kapitel haben Sie gelernt:



- Erstellen eines Kontos auf Voltage.cloud
- Schritte, um BTCPay Server zusammen mit einem Lightning Node auf dem Konto zum Laufen zu bringen


### Bewertung der Kenntnisse


#### KA Konzeptuelle Überprüfung


Was sind die Hauptunterschiede zwischen den Voltage- und LunaNode-Konfigurationen?


## Installation des BTCPay-Servers auf einem Umbrel-Knoten


<chapterId>3298e292-6476-5fe0-836c-7fa021348799</chapterId>


Am Ende dieser Schritte können Sie Blitzzahlungen für Ihren BTCPay-Shop in Ihrem lokalen Netzwerk akzeptieren. Dieser Prozess gilt auch, wenn Sie einen Umbrella-Knoten in einem Restaurant oder Geschäft betreiben. Wenn Sie diesen Shop mit einer öffentlichen Website verbinden möchten, folgen Sie der Übung für Fortgeschrittene, um Ihren Umbrella-Knoten der Öffentlichkeit zugänglich zu machen.


https://umbrel.com/


![image](assets/en/122.webp)


### BTCPay Server - Einsatz von Umbrel


Nachdem Ihr Umbrel-Knoten vollständig mit dem Bitcoin Blockchain synchronisiert ist, gehen Sie in den Umbrel App Store und suchen Sie unter Apps nach BTCPay Server.


![image](assets/en/123.webp)


Klicken Sie auf BTCPay Server, um die Details der App anzuzeigen. Wenn die Details für BTCPay Server geöffnet sind, zeigt die untere rechte Ecke die Anforderungen an, damit die App ordnungsgemäß ausgeführt werden kann. Es wird angezeigt, dass ein Bitcoin und ein Lightning-Knoten erforderlich sind. Wenn Sie den Lightning Node nicht auf Ihrem Umbrel installiert haben, klicken Sie auf Installieren. Dieser Vorgang kann ein paar Minuten dauern.


![image](assets/en/124.webp)


Nach der Installation Ihres Lightning Node:


1. Klicken Sie auf Öffnen in den App-Details oder auf die App im Umbrels-Dashboard.

2. Klicken Sie auf Einrichten eines neuen Knotens; Ihnen werden 24 Wörter für die Wiederherstellung Ihres Blitzknotens angezeigt.

3. Schreiben Sie diese auf.


![image](assets/en/125.webp)


Umbrel wird Sie bitten, die soeben aufgeschriebenen Worte zu bestätigen. Nachdem der Lightning-Knoten eingerichtet wurde, kehren Sie zum Umbrel App Store zurück und suchen Sie BTCPay Server. Klicken Sie auf die Schaltfläche Installieren und Umbrel zeigt an, ob die erforderlichen Komponenten installiert sind und dass BTCPay Server Zugriff auf diese Komponenten benötigt. Nach der Installation klicken Sie oben rechts in den App-Details auf Öffnen oder öffnen Sie BTCPay Server über Ihr Umbrels Dashboard.


Umbrel bittet um Überprüfung der soeben aufgeschriebenen Worte.


![image](assets/en/126.webp)


**Anmerkung*


Achten Sie darauf, dass Sie diese an einem sicheren Ort aufbewahren, wie Sie es bereits bei der Aufbewahrung von Schlüsseln gelernt haben.


Nachdem der Lightning-Knoten eingerichtet wurde, kehren Sie zum Umbrel App Store zurück und suchen Sie BTCPay Server. Klicken Sie auf die Schaltfläche "Installieren" und Umbrel zeigt an, ob die erforderlichen Komponenten installiert sind und dass BTCPay Server Zugriff auf diese Komponenten benötigt.


![image](assets/en/127.webp)


Nach der Installation klicken Sie oben rechts in den App-Details auf Öffnen oder öffnen Sie BTCPay Server über Ihr Umbrels-Dashboard.


![image](assets/en/128.webp)


### Zusammenfassung der Fertigkeiten


In diesem Abschnitt haben Sie gelernt:



- Schritte zur Installation von BTCPay Server mit Lightning-Funktionalität auf einem Umbrel-Knoten


### Bewertung der Kenntnisse


#### KA Konzeptuelle Überprüfung


Inwiefern unterscheidet sich die Einrichtung bei Umbrel von den beiden anderen Hosting-Optionen?


# Letzter Abschnitt


<partId>d72e6fa5-0870-5f00-9143-9466ed22e2bd</partId>




## Rezensionen und Bewertungen

<chapterId>d90bb93d-b894-551e-9fd6-6855c739a904</chapterId>

<isCourseReview>true</isCourseReview>

## Abschluss des Kurses


<chapterId>c07ac2a5-f97e-5c57-8a80-4955b48128d4</chapterId>

<isCourseConclusion>true</isCourseConclusion>