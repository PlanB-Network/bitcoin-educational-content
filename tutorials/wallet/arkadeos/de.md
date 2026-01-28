---
name: ArkadeOS
description: Vollständiger Leitfaden für das Arkade-Portfolio und das Ark-Protokoll
---

![cover](assets/cover.webp)



Das Bitcoin-Netz steht vor einer großen Herausforderung: der Skalierbarkeit. Während die Hauptschicht (Schicht 1) unübertroffene Sicherheit und Dezentralisierung bietet, kann sie nur eine begrenzte Anzahl von Transaktionen pro Sekunde verarbeiten. Lightning Network hat sich als vielversprechende Lösung für die zweite Schicht (Layer 2) herauskristallisiert, die schnelle und kostengünstige Zahlungen ermöglicht. Lightning unterliegt jedoch eigenen Beschränkungen: Kanalmanagement, die Notwendigkeit eingehender Liquidität und eine technische Komplexität, die neue Nutzer abschrecken könnte.



Dies ist der Hintergrund von **Ark**, einem neuen Schicht-2-Protokoll, das eine vereinfachte Benutzererfahrung bieten soll, ohne die Souveränität zu opfern. **ArkadeOS** (oder Arkade) ist die erste große Implementierung dieses Protokolls und bietet ein Bitcoin-Portfolio der nächsten Generation.



Dieses Tutorial wird Sie durch die Welt von Arkade führen. Wir werden erkunden, wie das Ark-Protokoll funktioniert, wie man den Arkade wallet installiert und konfiguriert und wie man ihn benutzt, um Bitcoins sofort, vertraulich und ohne die üblichen Lightning Network-Reibungen zu senden und zu empfangen.



## Das Arche-Protokoll verstehen



Bevor wir uns mit der Nutzung von Arkade beschäftigen, ist es wichtig, die Schlüsselkonzepte des Ark-Protokolls zu verstehen, auf dem es basiert. Ark ist keine separate Blockchain, sondern ein intelligenter Koordinationsmechanismus, der auf Bitcoin aufsetzt.



### Das VTXO-Konzept


Das Herzstück von Ark ist der **VTXO** (Virtual UTXO). Ein VTXO ist ein UTXO, der noch nicht auf der Bitcoin-Blockchain veröffentlicht wurde: Er existiert außerhalb der Hauptkette (off-chain), ist aber durch auf der Blockchain vorsignierte Transaktionen abgesichert.



Im Gegensatz zu einem Guthaben auf einer zentralisierten Börse gehört ein VTXO wirklich Ihnen. Sie besitzen einen kryptografischen Beweis, der es Ihnen ermöglicht, jederzeit die entsprechenden echten Bitcoins auf der Blockchain einzufordern, selbst wenn der Ark-Server verschwindet. Mit VTXOs können Sie Werte sofort zwischen Benutzern übertragen, ohne auf Blockbestätigungen zu warten.



### Die Rolle des ASP (Ark Service Provider)


Das Ark-Protokoll arbeitet nach einem Client-Server-Modell. Der Server wird **ASP** (Ark Service Provider) genannt. Der ASP spielt die Rolle des Dirigenten:




- Sie sorgt für die notwendige Liquidität des Netzes.
- Es koordiniert die Transaktionen zwischen den Nutzern.
- Es organisiert Abrechnungsrunden" auf der Blockchain.



Es ist wichtig zu wissen, dass ASP **nicht-verwahrend** ist. Sie ist weder im Besitz Ihrer privaten Schlüssel, noch kann sie Ihre Gelder stehlen. Seine Rolle ist rein technischer und logistischer Natur. Wenn ein ASP Ihre Transaktionen zensiert oder ausfällt, können Sie Ihre Gelder jederzeit über ein einseitiges Ausstiegsverfahren zurückerhalten.



### Runden und Privatsphäre


Transaktionen auf Ark werden in Stapeln abgeschlossen, die **Runden** genannt werden. In regelmäßigen Abständen (z. B. alle paar Sekunden) sammelt der ASP alle ausstehenden Transaktionen und verankert sie in der Bitcoin-Blockchain in einer einzigen optimierten Transaktion.


Dieser Mechanismus bietet zwei große Vorteile:




- Skalierbarkeit**: Eine einzige on-chain-Transaktion kann Tausende von off-chain-Zahlungen validieren, was die Kosten für die Benutzer drastisch reduziert.
- Vertraulichkeit**: Jede Runde funktioniert wie ein **CoinJoin**. Die Gelder aller Teilnehmer werden in einen gemeinsamen Pool gemischt, bevor sie in Form von neuen VTXOs weiterverteilt werden. Dadurch wird die Verbindung zwischen Sender und Empfänger unterbrochen, was es für einen außenstehenden Beobachter extrem schwierig, wenn nicht gar unmöglich macht, Zahlungen zurückzuverfolgen.



## ArkadeOS-Präsentation



ArkadeOS ist die konkrete Anwendung, die das Ark-Protokoll für die Allgemeinheit zugänglich macht. Es wurde von Ark Labs entwickelt und ist ein vollständiges Ökosystem, das ein Portfolio (Wallet), einen Server (Operator) und Entwicklerwerkzeuge umfasst.



Für den Endnutzer hat Arkade die Form einer eleganten, intuitiven Web-wallet (PWA - Progressive Web App). Es verbirgt die kryptografische Komplexität von VTXOs und Runden hinter einer vertrauten Oberfläche. Mit Arkade haben Sie eine Adresse zum Empfangen, eine Schaltfläche zum Senden und eine Transaktionshistorie, genau wie ein klassischer wallet, aber mit der Leistung der Unmittelbarkeit und Vertraulichkeit von Ark.



## Installation und Konfiguration



Da es sich bei Arkade um eine Progressive Web App handelt, ist sie besonders einfach zu installieren und erfordert nicht zwangsläufig den Einsatz herkömmlicher Anwendungsspeicher.



### Zugang und Installation


Sie können mit jedem modernen Webbrowser (Chrome, Safari, Brave) direkt auf Arkade zugreifen, egal ob auf dem Computer oder dem Handy.





- Besuchen Sie die offizielle Website der Anwendung: **[arkade.money](https://arkade.money)**.



![arkade homepage](assets/fr/01.webp)



Sie werden von einer Reihe von Einführungsbildschirmen begrüßt, die Sie in die Schlüsselkonzepte von Arkade einführen: ein neues Ökosystem für Bitcoin, die Bedeutung der Selbstverwahrung und die Vorteile von Stapeltransaktionen.



![arkade onboarding](assets/fr/02.webp)





- Unter Android (Chrome/Brave)** : Drücken Sie das Browsermenü (drei Punkte) und wählen Sie "Anwendung installieren" oder "Zum Startbildschirm hinzufügen".
- Unter iOS (Safari)**: Drücken Sie die Freigabetaste (Quadrat mit Pfeil nach oben) und wählen Sie "Auf dem Startbildschirm".



Nach der Installation wird Arkade wie eine native Anwendung gestartet, im Vollbildmodus und ohne Adressleiste.



### Erstellung eines Portfolios


Beim ersten Start werden Sie aufgefordert, Ihr Portfolio zu konfigurieren.





- Klicken Sie auf **"Neues Wallet erstellen "**.



![create wallet](assets/fr/03.webp)





- Die wallet wird sofort erstellt. Im Gegensatz zu herkömmlichen Bitcoin-Geldbörsen verwendet **Arkade keine 12- oder 24-Wort-Wiederherstellungsphrase**. Stattdessen generiert Arkade automatisch einen **privaten Schlüssel** im Nostr (nsec)-Format, der für die Sicherung und Wiederherstellung Ihres wallet verwendet wird. Denken Sie daran, diesen Schlüssel sofort zu speichern (siehe nächster Abschnitt).





- Sie sehen den Bildschirm "Ihr neues wallet ist live!", der Ihnen bestätigt, dass Ihr wallet einsatzbereit ist. Klicken Sie auf **"GO TO WALLET "**, um die Hauptschnittstelle aufzurufen.



Sobald Sie sich in Ihrem wallet befinden, werden Sie zur Hauptschnittstelle von Arkade weitergeleitet. Hier finden Sie Ihren Kontostand, Schaltflächen zum Senden und Empfangen von Geldern und eine Registerkarte "Apps", die Zugriff auf integrierte Anwendungen wie Boltz (Blitzbörse), LendaSat und LendaSwap (Kreditvergabe) und Fuji Money (synthetische Vermögenswerte) bietet.



![wallet interface](assets/fr/04.webp)



### Verbindung zu ASP


Standardmäßig ist das Portfolio automatisch so konfiguriert, dass es sich mit dem offiziellen Arkade Labs ASP verbindet. Sie können überprüfen, mit welchem Server Sie verbunden sind, indem Sie auf **Einstellungen** > **Über** gehen, wo Sie die Serveradresse sehen (derzeit `https://arkade.computer`).



In der aktuellen Version von Arkade (Beta) ist es nicht möglich, den ASP-Server manuell zu ändern. Die Anwendung verbindet sich automatisch mit dem offiziellen Arkade Labs ASP. In Zukunft können Benutzer möglicherweise zwischen verschiedenen ASPs je nach ihren Präferenzen wählen, aber diese Funktion ist noch nicht verfügbar.



### Sichern Sie Ihren privaten Schlüssel


**Arkade verwendet einen privaten Schlüssel im Nostr (nsec) Format als Sicherungs- und Wiederherstellungsmethode. Zum Sichern Ihres privaten Schlüssels :





- Gehen Sie auf dem Hauptbildschirm zu **Einstellungen**.
- Wählen Sie **"Sicherung und Datenschutz "**.
- Sie sehen Ihren **privaten Schlüssel** im Format "nsec...`" angezeigt. Diese lange Zeichenfolge ist Ihr einziges Mittel, um Ihr wallet wiederherzustellen.
- Drücken Sie **"COPY NSEC TO CLIPBOARD "**, um Ihren privaten Schlüssel zu kopieren.
- Bewahren Sie diesen Schlüssel an einem sicheren Ort auf**: Schreiben Sie ihn auf, speichern Sie ihn in einem sicheren Passwort-Manager oder verwenden Sie eine andere Sicherungsmethode, die Ihnen zusagt.
- Arkade bietet auch die Option **"Nostr-Backups aktivieren "**. Diese Funktion verwendet das Nostr-Protokoll (ein dezentralisiertes Netzwerk), um automatisch bestimmte Daten Ihres wallet in verschlüsselter Form auf Nostr-Relais zu sichern. Dies erleichtert die Synchronisation zwischen mehreren Geräten und bietet eine einfachere Wiederherstellung des Status Ihres wallet.



**Wichtig**: Nostr-Backups sind nur eine **Komfort**-Funktion. Sie ersetzen nicht die Sicherung Ihres nsec-Schlüssels. Nostr-Relais garantieren keine dauerhafte Datenspeicherung. Ihr privater nsec-Schlüssel bleibt Ihr einziges garantiertes Mittel, um Ihre Gelder wiederzuerlangen.



![backup private key](assets/fr/05.webp)




## Arkade verwenden



Sobald Sie Ihr wallet eingerichtet haben, können Sie die Möglichkeiten von Arkade erkunden. Die Schnittstelle ist so konzipiert, dass die verschiedenen Arten von Bitcoin-Zahlungen (On-Chain, Lightning, Ark) nahtlos zusammengeführt werden.



### Empfang von Geldern



Um Ihr Portfolio zu finanzieren, drücken Sie **"Empfangen "**. Arkade bietet drei Empfangsmethoden an:





- Ark-Zahlung**: Wenn der Absender ebenfalls Arkade verwendet, teilen Sie ihm Ihre Ark-Adresse für eine sofortige, vertrauliche und praktisch kostenlose Überweisung mit.
- Einzahlung in der Kette (Boarding)**: Verwenden Sie die Bitcoin-Adresse (`bc1p...`), um von einem klassischen wallet oder einer Börse zu empfangen. Warten Sie auf eine Bestätigung (~10 Minuten), bevor das Geld in VTXOs umgewandelt wird.
- Lightning Swap**: Erstellen Sie eine Lightning-Rechnung und bezahlen Sie sie mit einem externen wallet Lightning. Das Geld kommt sofort über einen automatischen Swap an.



![receive amount](assets/fr/06.webp)



Der Quittungsbildschirm zeigt alle verfügbaren Optionen an: QR-Code, Ark-Adresse, Bitcoin (BIP21)-Adresse und Lightning-Rechnung. Für Lightning-Zahlungen lassen Sie die Anwendung während der Transaktion geöffnet.



![receive confirmation](assets/fr/07.webp)



### Übermittlung von Geldern



Um Geld zu senden, drücken Sie **"Senden "** und fügen Sie die Adresse des Empfängers ein oder scannen Sie den QR-Code. Arkade erkennt automatisch die Art der erforderlichen Zahlung:





- Ark**-Zahlung: An eine Ark-Adresse ist die Überweisung sofort, privat und praktisch kostenlos (0 SATS-Gebühr). Der Empfänger muss nicht online sein.
- Lightning**-Zahlung: Scannen Sie eine Lightning-Rechnung (`lnbc...`) und Arkade führt automatisch einen Tausch durch. Der ASP bezahlt die Rechnung für Sie und belastet Ihr Arkade-Guthaben.
- On-Chain-Zahlung**: Gegenüber einer klassischen Bitcoin-Adresse (`bc1q...` oder `bc1p...`) initiiert Arkade einen "Collaborative Output", der in die nächste on-chain-Runde aufgenommen wird.



Überprüfen Sie die Angaben auf dem Bildschirm "Transaktion unterzeichnen" und bestätigen Sie dann mit **"ZUR UNTERZEICHNUNG ANTippen "**.



![send payment](assets/fr/08.webp)



**Aktuelle Einschränkung (Beta)**: VTXOs, die vor weniger als 24 Stunden erstellt wurden, können nicht für on-chain-Ausgänge verwendet werden. Wenn Sie auf einen Fehler stoßen, warten Sie bitte, bis Ihre VTXOs "reif" sind.



**on-chain Vertraulichkeit der Ausgabe**: Das folgende Beispiel zeigt eine [Ark-Ausgabe-Transaktion auf mempool.space](https://mempool.space/fr/tx/153a70384d1c8a183c0e408e29b0a11820fd71a8bd5b4b00b12bc9b7f9decacb). Wir beobachten einen verteilten Input zu 4 verschiedenen Outputs, wie ein CoinJoin. Für einen externen Beobachter ist es unmöglich, festzustellen, welcher Betrag zu welchem Benutzer gehört.



![transaction ark mempool](assets/fr/11.webp)



## Erweiterte Funktionen



### Verwaltung des VTXO-Ablaufs


Eine technische Besonderheit des Ark-Protokolls ist, dass VTXOs eine **begrenzte Lebensdauer** haben. Diese zeitliche Beschränkung ist in das Design des Protokolls integriert. Die Ablaufzeit ist von jedem ASP-Server konfigurierbar; auf dem offiziellen ASP von Arkade Labs beträgt dieser Zeitraum etwa **4 Wochen (≈30 Tage)**.



**Diese Einschränkung ermöglicht es dem Ark-Server, die Liquidität effizient zu verwalten und VTXOs von inaktiven Benutzern zu bereinigen. Nach Ablauf der Frist kann der Ark-Server technisch gesehen die verbleibenden Mittel im VTXO-Baum beanspruchen.



**Damit Ihre VTXOs aktiv bleiben, müssen sie "aufgefrischt" werden, bevor sie auslaufen. Die Auffrischung besteht in der Teilnahme an einer neuen "Runde", in der Ihre VTXOs, die kurz vor dem Ablauf stehen, gegen neue VTXOs mit einer neuen vollen Gültigkeitsdauer (≈30 Tage auf Arkade Labs ASP) ausgetauscht werden.



Das Arkade-Portfolio verwaltet diesen Prozess automatisch: Die Anwendung überwacht ständig den Status Ihrer VTXOs und aktualisiert sie automatisch einige Tage vor ihrem Ablauf. Solange Sie Ihre Anwendung regelmäßig öffnen (mindestens einmal pro Woche), werden Ihre VTXOs automatisch aktiv gehalten.



**Wenn Sie Ihr Portfolio mehr als 4 Wochen lang nicht öffnen, verfallen Ihre VTXOs. Sie verlieren Ihre Gelder jedoch nicht: Sie haben weiterhin die Möglichkeit, sie über einen **einseitigen Ausstieg** (siehe nächster Abschnitt) zurückzuholen. Dieses Verfahren ist kostspieliger und langwieriger, aber es gewährleistet, dass Sie Ihre Gelder wiedererlangen können.



Die Notwendigkeit, die Anwendung regelmäßig zu öffnen, macht Arkade zu einem **"Hot Wallet"**, der für die täglichen Ausgaben konzipiert ist, nicht zu einem Safe für langfristige Ersparnisse. Um Bitcoins zu speichern, ohne sie für lange Zeiträume zu verwenden, bevorzugen eine kalte wallet Hardware.



**Überprüfen Sie den Status Ihrer VTXOs**: Sie können den Status Ihrer VTXOs unter **Einstellungen** > **Erweitert** überwachen. Unter "Nächste Erneuerung" sehen Sie, wann die nächste automatische Erneuerung stattfinden wird, und unter "Virtuelle Münzen" sehen Sie eine detaillierte Liste aller Ihrer VTXOs mit deren Ablaufdatum.



![vtxo management](assets/fr/09.webp)



### Sortie Unilatérale (Einseitiger Ausstieg)



Der einseitige Ausstieg ist eine **grundlegende kryptografische Garantie** des Ark-Protokolls, die sicherstellt, dass Sie Ihr Geld zurückbekommen, selbst wenn der ASP verschwindet, Ihre Transaktionen zensiert oder die Zusammenarbeit verweigert. Technisch gesehen sind Ihre VTXOs **vorab signierte Bitcoin-Transaktionen**, die Ihnen gehören. Im absoluten Notfall können Sie diese Transaktionen auf der Bitcoin-Blockchain übertragen, um Ihre Gelder ohne die Genehmigung anderer zurückzuholen.



**Wie funktioniert es? Der Prozess erfolgt in zwei Stufen. Erstens die **Abwicklung**: Sie übertragen nacheinander die vorab signierten Transaktionen, aus denen Ihre VTXOs bestehen, in den Transaktionsbaum. Dann die **Finalisierung**: Sobald die Zeitsperren abgelaufen sind (normalerweise 24 Stunden), holen Sie Ihre Bitcoins von einer Standardadresse ab.



**Aktueller Stand in Arkade**: In der Beta-Version gibt es noch keine Schaltfläche oder einfache Benutzeroberfläche für die einseitige Ausgabe. Diese Funktionalität erfordert derzeit die Verwendung des Arkade SDK und technische Kenntnisse der TypeScript-Programmierung.



**Selbst wenn das Verfahren nicht auf Knopfdruck zugänglich ist, ist die kryptografische Garantie vorhanden. Ihre VTXOs enthalten vorsignierte Transaktionen, die rechtmäßig Ihnen gehören. Es ist diese technische Garantie, die Ark zu einem **nicht-pfändbaren** Protokoll macht: Selbst im schlimmsten Fall bleiben Ihre Gelder technisch wiederherstellbar. Eine vereinfachte Schnittstelle wird wahrscheinlich in zukünftigen Versionen von Arkade hinzugefügt werden.



## Vorteile und Grenzen



Um Arkade in den richtigen Kontext zu stellen, fassen wir seine derzeitigen Stärken und Schwächen zusammen.



### Höhepunkte




- Benutzerfreundlichkeit (UX)**: Kein Channel-Management, keine eingehende Kapazität oder komplexe Channel-Backups wie bei Lightning. Einfach installieren und nutzen.
- Datenschutz** : Die Standard-CoinJoin-Architektur bietet ein wesentlich höheres Maß an Anonymität als Standard-on-chain- oder Lightning-Transaktionen.
- Interoperabilität**: Bezahlen Sie jeden Bitcoin QR-Code (On-Chain oder Lightning) über eine einzige Schnittstelle.



### Zwänge




- Junges Protokoll**: Ark ist eine sehr junge Technologie. Es können Bugs existieren. Es ist nicht ratsam, Ark zur Speicherung von Beträgen zu verwenden, deren Verlust kritisch wäre.
- ASP-Abhängigkeit**: Obwohl das System nicht abhängig ist, hängt es von der Verfügbarkeit des ASP ab, um einen reibungslosen Ablauf zu gewährleisten. Wenn der ASP offline ist, können Sie keine sofortigen Transaktionen mehr durchführen (nur Ihre on-chain-Gelder ausgeben).
- Nur Hot Wallet** : Die Notwendigkeit, die Anwendung regelmäßig zu öffnen, um die VTXOs zu aktualisieren, ist für die kalte Lagerung nicht geeignet (Cold Lagerung).



## Vergleich: Arkade vs. Lightning vs. Cashu



Um die Positionierung von Arkade besser zu verstehen, sollten wir es mit den beiden anderen großen Skalierungslösungen vergleichen.




| Kriterium | Arkade (Ark) | Lightning Network | Cashu (E-cash) |
| :--- | :--- | :--- | :--- |
| **Modell** | Gemeinsames UTXO, koordiniert durch Server (ASP) | P2P-Netzwerk von Zahlungskanälen | Von einer Bank (Mint) ausgegebene Blind Tokens |
| **Verwahrung** | **Non-custodial** (Sie haben die Schlüssel) | **Non-custodial** (Sie haben die Schlüssel) | **Custodial** (Der Mint hält die Mittel) |
| **Privatsphäre** | **Hoch** (Natives CoinJoin, blind für die Öffentlichkeit) | **Mittel** (Onion-Routing, aber Kanäle sichtbar) | **Sehr hoch** (Blind sogar für den Mint) |
| **Skalierbarkeit** | Exzellent (Massives Batching On-Chain) | Exzellent (Unendliche Transaktionen Off-Chain) | Exzellent (Einfache Serversignaturen) |
| **Erfahrung** | Einfach (ähnlich einer On-Chain-Wallet) | Komplex (Kanalverwaltung, Liquidität) | Sehr einfach (wie digitales Bargeld) |
| **Hauptrisiko** | Verfügbarkeit des ASP & Ablauf | Kanalverwaltung & Backups | Vertrauen in den Mint (Diebstahlrisiko) |

**Arkade** ist der ideale Kompromiss: die Einfachheit und Vertraulichkeit von Cashu, aber mit der Souveränität (ohne Verwahrung) von Lightning.



## Unterstützung und Hilfe



Wenn Sie bei der Verwendung von Arkade auf Probleme stoßen oder Fragen haben, bietet die Anwendung mehrere Support-Optionen:





- Gehen Sie zu **Einstellungen** > **Support**.
- Hier finden Sie mehrere Optionen:
  - Kundenbetreuung**: Erhalten Sie Hilfe zu Ihrem Portfolio, melden Sie Fehler oder stellen Sie Fragen.
  - Sicherer Chat**: Ihre Unterhaltungen sind sicher und privat, wobei der Verlauf zwischen den Sitzungen erhalten bleibt.
  - Fehlerberichte**: Berichten Sie über alle Probleme, auf die Sie stoßen, einschließlich der Schritte, um sie zu reproduzieren.
  - Fortschritte verfolgen**: Behalten Sie jederzeit den Überblick über Ihre Supportanfragen und -gespräche.



![support](assets/fr/10.webp)



Das Arkade-Team ist auch auf Telegram über den Kanal @arkade_os für Support und Integrationsmöglichkeiten aktiv.



## Wichtiger Hinweis: Anwendung im Beta-Stadium



**⚠️ Arkade befindet sich derzeit in der öffentlichen Betaphase auf dem mainnet Bitcoin**. Obwohl die Anwendung mit echten Bitcoins funktioniert, ist es wichtig, bestimmte Vorsichtsmaßnahmen zu treffen.



### Empfehlungen für die Verwendung




- Verwenden Sie kleine Beträge**: Vermeiden Sie es, große Summen auf Arkade zu speichern. Verwenden Sie dieses wallet für Ihre täglichen Ausgaben und bewahren Sie Ihre Ersparnisse auf einer kalten wallet Hardware auf.
- Mögliche Bugs und Einschränkungen**: Wie bei jeder Anwendung, die sich in aktiver Entwicklung befindet, können auch bei Arkade Fehler oder unerwartetes Verhalten auftreten. Melden Sie alle Probleme über den integrierten Support.
- Schnelle Entwicklung** : Die Anwendung und das Protokoll werden ständig verbessert. Einige Funktionen können sich in zukünftigen Versionen ändern oder hinzugefügt werden.



### Derzeit bekannte Einschränkungen




- 24 Stunden Verzögerung bei VTXOs** : Neu erstellte VTXOs können nicht sofort für on-chain-Ausgänge verwendet werden.
- ASP einzigartig**: Es ist noch nicht möglich, den ASP-Server in der Anwendung zu ändern.
- Technische unilaterale Ausgabe**: Noch keine vereinfachte Schnittstelle für unilaterale Ausgabe (erfordert SDK).



Das Arkade Labs Team arbeitet aktiv daran, diese Einschränkungen in zukünftigen Versionen zu lockern.



## Schlussfolgerung



ArkadeOS stellt einen wichtigen Durchbruch im Bitcoin-Ökosystem dar. Durch die Implementierung des Ark-Protokolls beweist es, dass es möglich ist, die Einfachheit der Nutzung mit den Grundprinzipien von Bitcoin in Einklang zu bringen: Don't trust, verify.



Obwohl Arkade noch in den Kinderschuhen steckt, bietet es einen faszinierenden Einblick, wie die Zukunft der Bitcoin-Zahlungen aussehen könnte: sofort, privat und für alle zugänglich, ohne technische Voraussetzungen. Es ist das perfekte Werkzeug für Ihre täglichen Ausgaben und ergänzt Ihre sichere Sparlösung (Cold Wallet).



Wir ermutigen Sie, Arkade mit kleinen Beträgen zu testen, um dieses neue Protokoll für sich selbst zu entdecken. Das Ökosystem entwickelt sich schnell weiter, und Arkade steht an der Spitze dieser Innovation.



## Ressourcen



Weitere Informationen finden Sie in den offiziellen Quellen:





- Arkade** Website: [arkadeos.com](https://arkadeos.com)
- Dokumentation**: [docs.arkadeos.com](https://docs.arkadeos.com)
- Ark**-Protokoll: [ark-protocol.org](https://ark-protocol.org)
- Quellcode** : [GitHub Arkade](https://github.com/arkade-os)