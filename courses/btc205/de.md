---
name: Lösung für den Peer-to-Peer-Kauf und -Verkauf von Bitcoin
goal: Erkundung von Lösungen für den Kauf und Verkauf von Bitcoin ohne KYC
objectives:
  - Verständnis für die verschiedenen Arten von KYC, deren Risiken und Vorteile
  - Verständnis für die Vorteile eines Peer-to-Peer-Kaufs
  - Implementierung der Lösung, die Ihren Bedürfnissen entspricht
  - Verbesserung des UTXO-Managements (KYC und nicht KYC)
---

# Eine Reise in die Welt des nicht-KYC

Pierre bietet uns diesen Kurs an, der uns in die verschiedenen vorhandenen Lösungen für den Peer-to-Peer-Kauf und -Verkauf von Bitcoins einführt. Der Peer-to-Peer-Kauf ist völlig legal und ermöglicht mehr Anonymität, da diese Lösungen nicht KYC sind. KYC (Know Your Customer) ist eine Regel der Marktregulierungsbehörden (AMF), die den Kunden, der Bitcoin kaufen oder verkaufen möchte, um eine Identitätsprüfung bittet. Diese Regeln sollen Geldwäsche, Terrorismusfinanzierung und Steuerhinterziehung verhindern. Mit dem Risiko schwerwiegender Konsequenzen für den Benutzer hat KYC das Ziel, den Benutzer zu verteidigen und zu schützen, obwohl oft das Gegenteil beobachtet wird.

Wir werden also die verschiedenen Arten von KYC (vollständiges KYC wie in Frankreich, KYC Light wie in der Schweiz und nicht-KYC wie Peer-to-Peer) erkunden. Pierre wird uns mehr als 6 Lösungen vorstellen, so dass Sie alle Karten in der Hand haben, um herauszufinden, welche für Sie geeignet ist. Wenn Sie eine KYC-Lösung wünschen, finden Sie diese in der BTC 102-Formation.

+++

# Einführung

## Erklärung & Art des KYC

KYC, für "Know Your Customer" (Kennen Sie Ihren Kunden), ist eine regulatorische Norm, die die Sammlung von privaten Informationen der Kunden erfordert, wie ihre physische Adresse, ihre Identitätsdokumente oder ihre Bankauszüge. Diese Praxis ist auf Handelsplattformen üblich, die ein vollständiges KYC verlangen können, einschließlich detaillierter Informationen wie Identitätsdokumente, Fotos, Adressnachweise, Gehaltsabrechnungen usw.

Das Hauptziel von KYC ist es, Geldwäsche, Terrorismusfinanzierung und Steuerhinterziehung zu bekämpfen. Es handelt sich um ein Gesetz, das von der AMF (Autorité des marchés financiers), der französischen Marktregulierungsbehörde, erlassen wurde. Die Anwendung von KYC führt jedoch zur Zentralisierung sehr sensibler Datenbanken, die persönliche Informationen der Benutzer enthalten. Diese Informationen, die einen gewissen Wert haben, können an bösartige Entitäten verkauft werden.
Zudem verlangen Handelsplattformen oft eine übermäßige Menge an persönlichen Informationen, was die Benutzer gefährdet und die Compliance-Kosten erhöht. Diese regulatorischen Kosten können französische Unternehmen entmutigen und ihre Wettbewerbsfähigkeit auf internationaler Ebene beeinträchtigen.
Es gibt drei Arten von KYC, darunter das Full KYC, das eine vollständige und regulierte Sammlung von Informationen erfordert, um auf den Service zugreifen zu können. In der Schweiz ermöglicht eine Alternative namens "KYC light" den Kauf und Verkauf von Bitcoins ohne Vorlage eines Ausweises, solange der Kaufbetrag 1000 Euro pro Tag nicht übersteigt. Lösungen wie Relay ermöglichen die Verwendung dieser Methode.

In diesem Zusammenhang können die Schweizer Behörden auf Bankinformationen zugreifen, um Personen zu untersuchen, die als risikobehaftet gelten. Bitcoin-Lieferadressen sind auch über das Bankensystem nachverfolgbar. KYC light wird im Allgemeinen als einfacher und kostengünstiger als das französische System angesehen.

In Frankreich erfordert der Online-Kauf von Bitcoins das Senden von Geld an einen Dritten per SEPA-Überweisung oder Paypal. Für diejenigen, die Anonymität, Sicherheit und Privatsphäre bevorzugen, stehen auch Lösungen für den Kauf von Bitcoins in bar zur Verfügung. Für geringe Volumina ist der Kauf von Bitcoins in bar eine einfache und legale Option.

Um täglich Bitcoin-PLT im Wert von 100 Euro an jeden verkaufen zu können, ist eine Regulierung durch die AMF (Autorité des Marchés Financiers) erforderlich. In Frankreich gilt diese Regulierung hauptsächlich für Privatpersonen, die hohe Transaktionsvolumina durchführen. Die beiden anderen Methoden zum Kauf von Bitcoin umfassen die Verwendung von Geldautomaten (ATM) und den Austausch zwischen Freunden. Geldautomaten sind reguliert und erfordern eine Identitätsprüfung für Transaktionen über 500 Euro. Der Austausch zwischen Freunden bietet eine diskretere Möglichkeit, Bitcoin zu nutzen.

Diese regulatorischen Maßnahmen sind zur Bekämpfung der Finanzierung von Terrorismus, Steuerhinterziehung und Geldwäsche vorgesehen. Bitcoin als vollständig nachverfolgbare Datenbank macht Geldwäsche besonders schwierig. Die Verwendung von Bitcoin durch Kriminelle kann zurückverfolgt werden, was Bitcoin zu einem wenig effektiven Werkzeug für Geldwäsche macht.
Es ist wichtig zu beachten, dass diese Schulung verschiedene Alternativen sowie Werkzeuge präsentiert, die für böswillige oder nicht böswillige Zwecke genutzt werden können. Darüber hinaus bietet sie Erklärungen zum Funktionieren von Orderbüchern zwischen Makern (Auftragsanbietern) und Takern (Auftragsnehmern).

Es ist auch wichtig zu beachten, dass die hier präsentierte Information keine bestimmte Lösung befürwortet. Es geht lediglich darum, die verfügbaren Optionen für ein besseres Verständnis des Themas darzustellen. Bei weiteren Fragen zum Bitcoin sollten Online-Ressourcen wie www.découvrebitcoin.com konsultiert werden.

## Vergleich der Peer-to-Peer-Kauf- und Verkaufslösungen

P2P-Lösungen zum Kauf von Bitcoin: Bisq, RoboSat, LNP2PBot, Peach und HodlHodl

Der Kauf von Bitcoin im Peer-to-Peer-Modus (P2P) ist eine bevorzugte Option für Investoren, die zentralisierte Börsen vermeiden möchten. Dieser Teil des Kurses untersucht verschiedene verfügbare P2P-Lösungen, einschließlich Bisq, RoboSat, LNP2PBot, Peach und HodlHodl.
Vergleich der Vor- und Nachteile der verschiedenen Lösungen

Jede P2P-Lösung hat ihre eigenen Vor- und Nachteile. Wir bieten unten einen Überblick über die wichtigsten Merkmale jeder Lösung.

### Bisq

[Bisq](https://bisq.network/) ist eine nicht verwahrte P2P-Lösung mit einem DAO-System (Dezentrale Autonome Organisation) und verwendet Multisign zur Streitbeilegung. Sein Code ist Open Source, was zu seiner Robustheit und zum Schutz der Privatsphäre der Benutzer beiträgt.

| Vorteile                                     | Nachteile                                                                                             |
| -------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| - P2P-Lösung, nicht verwahrt, Multisign, DAO | - Die Anwendung ist ziemlich schwer und nicht sehr benutzerfreundlich, nur auf dem Computer verfügbar |
| - Robust und sicher                          | - Kauf- und Verkaufslimits sowie die Kontoverwaltung mit Signaturen sind zweischneidig.               |
| - Open Source                                |                                                                                                       |

### RoboSat

[RoboSat](https://learn.robosats.com/) ist eine einfach zu bedienende, schnelle Lösung, die unter TOR funktioniert und kein Konto erfordert. Es ist Open Source und verwendet das Lightning Network für schnelle Transaktionen.

| Vorteile                                                     | Nachteile                                                                       |
| ------------------------------------------------------------ | ------------------------------------------------------------------------------- |
| - Einfach zu bedienen                                        | - Das Protokoll ist mit einem einzigen Koordinator fragil.                      |
| - Geringe Transaktionsgebühren                               | - Erfordert technisches Wissen und Verständnis für Datenschutz.                 |
| - Verwendet das Lightning Network für schnelle Transaktionen | - Die Umbrell-Anwendung ermöglicht die Verwaltung einer eigenen Client-Instanz. |
| - Open Source                                                |                                                                                 |

### LNP2PBot

[LNP2PBot](https://lnp2pbot.com/) ist über Telegram für den nicht-KYC-Kauf von Bitcoin zugänglich. Es bietet schnelle Transaktionen dank des Lightning Network und niedrige Gebühren.

| Vorteile                                                              | Nachteile                                                                                 |
| --------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| - Über Telegram zugänglich                                            | - Weniger robust und sicher als andere Lösungen.                                          |
| - Schnelligkeit dank des Lightning Network                            | - Weniger schnell und weniger benutzerfreundlich als Robosat.                             |
| - Geringe Transaktionsgebühren                                        | - Kann mit der Telegram-Identität des Benutzers verknüpft werden.                         |
| - Interne Streitbeilegung                                             | - Mangelnde Liquidität und Fragilität der Anwendung.                                      |
| - Vorschläge von Gemeinschaften, um das Vertrauensproblem einzudämmen | - LNP2Pbot sollte bei der Bearbeitung von Streitfällen Vertrauen entgegengebracht werden. |

### Peach

[Peach](https://peachbitcoin.com/) ist eine mobile Anwendung, die sich auf den Handel mit Bitcoin spezialisiert hat. Sie zeichnet sich durch ihre Einfachheit aus und erfordert keine Kontoerstellung, um zu funktionieren. Die Trades sind schnell, auch ohne Lightning Network. Darüber hinaus beschleunigen Benachrichtigungen auf Mobiltelefonen den Transaktionsprozess.

| Vorteile                                                         | Nachteile                                                                                                                         |
| ---------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| - Einfache Bedienung: Keine Kontoerstellung erforderlich.        | - Sicherheit und Robustheit: Da Peach mit einem Unternehmen verbunden ist, hat es potenzielle Schwächen in Bezug auf Sicherheit.  |
| - Transaktionsgeschwindigkeit: Der Handel ist schnell.           | - Fehlen von Lightning Network: Diese Technologie, die schnellere Bitcoin-Transaktionen ermöglicht, wird von Peach nicht genutzt. |
| - Benachrichtigungen: Sie beschleunigen den Transaktionsprozess. |                                                                                                                                   |

### HodlHodl

[HodlHodl](https://hodlhodl.com/) ist eine nicht verwahrte Lösung für den Bitcoin-Handel. Es bietet viele Vorteile wie hohe Liquidität, die Möglichkeit von privaten Trades, ein Empfehlungssystem sowie Konten mit Handelshistorie und Bewertungssystem. Die Trades sind jedoch mit der E-Mail-Adresse und der digitalen Identität des Benutzers verbunden, die bei HodlHodl gespeichert sind. Darüber hinaus ist der Quellcode von HodlHodl nicht öffentlich und die Anwendung kann nicht mit Tor verwendet werden.

| Vorteile                                                                                                                   | Nachteile                                                                                                                              |
| -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| - Nicht verwahrt: Der Benutzer behält die Kontrolle über seine privaten Schlüssel.                                         | - Speicherung persönlicher Informationen: Die E-Mail-Adresse und die digitale Identität des Benutzers werden von HodlHodl gespeichert. |
| - Liquidität: HodlHodl bietet eine breite Palette von Handelsmöglichkeiten.                                                | - Geschlossener Quellcode: Der Code von HodlHodl ist nicht öffentlich.                                                                 |
| - Möglichkeit von privaten Trades: Der Benutzer kann wählen, mit wem er handeln möchte.                                    | - Inkompatibilität mit Tor: HodlHodl kann nicht mit diesem auf Datenschutz ausgerichteten Netzwerk verwendet werden.                   |
| - Empfehlungssystem: HodlHodl belohnt Mundpropaganda.                                                                      | - Möglichkeit der erzwungenen KYC: In einigen Situationen kann HodlHodl Identifikationsinformationen verlangen, um Gelder abzurufen.   |
| - Handelshistorie und Bewertungssystem: Diese Funktionen ermöglichen es, die Zuverlässigkeit anderer Benutzer zu bewerten. |                                                                                                                                        |

## Fazit zu P2P-Lösungen

Zusammenfassend hat jede P2P-Lösung ihre Vor- und Nachteile. Bisq gilt als die robusteste und sicherste, aber weniger zugänglich. RoboSat ist Open Source, aber weniger robust als Bisq. LNP2PBot ist weniger robust und sicher als andere Lösungen, weniger schnell und weniger benutzerfreundlich als RoboSat, aber mehr als Bisq. Peach ist die einfachste und schnellste Anwendung zum Kauf von Bitcoin ohne KYC, aber es gibt ein Unternehmen dahinter, also Schwächen in Bezug auf Sicherheit und Robustheit. HodlHodl ist ein von einem Unternehmen verwaltetes und geschlossenes Protokoll, daher Schwächen in Bezug auf Sicherheit und Robustheit und etwas komplizierter als Peach.

Das gute alte Bargeld von Angesicht zu Angesicht bleibt immer eine Lösung für kleine Beträge.

Neben P2P-Lösungen gibt es auch andere Kryptowährungsaustauschoptionen. kycnot.me bietet Dienste wie VPN, VPS, SMS usw. an. Bitrefil ermöglicht den Kauf von Geschenkkarten. Jede Lösung auf [kycnotme](https://kycnot.me/) wird mit ihren Vor- und Nachteilen vorgestellt.

# Tutorials zu P2P-Kauf-/Verkaufslösungen

## Robosats

![robosats](https://tube.nuagelibre.fr/videos/watch/1978a2e0-64a0-4437-9229-7614cdf5bf61?start=0s)

[RoboSat](https://learn.robosats.com/) ist ein Open-Source-Projekt von Reckless Satoshi, um Bitcoins gegen nationale Währungen privat zu tauschen. Es vereinfacht das Peer-to-Peer-Erlebnis und verwendet Lightning-Rechnungen, um die Notwendigkeit von Custody und Vertrauen auf ein Minimum zu reduzieren. Um es zu verwenden, benötigen wir Tor, ein anonymes Kommunikationsnetzwerk.

Das erste, was Sie tun müssen, ist Tor herunterzuladen. Sie können es auf GitHub oder direkt auf der offiziellen Website unter folgender Adresse finden: tor.org/download.
Sobald Tor heruntergeladen und installiert ist:

- Drücken Sie "Connect", um die Verbindung herzustellen.
- Gehen Sie zur [Robosats-Zwiebeladresse](http://robosats6tkf3eva7x2voqso3a5wcorsnw34jveyxfqi2fu7oyheasid.onion/).
- Kopieren Sie den Token, um Ihre Identität zu sichern.

Hier sind nun die Schritte zum Kauf von Bitcoins mit Robosats:

- Überprüfen Sie das Orderbuch, Sie können nach Währung und Zahlungsmethode filtern - zum Beispiel Bitcoin in Euro mit Revolut kaufen.
- Überprüfen Sie vor dem Kauf das Ablaufdatum des Angebots, den Preis in Euro und den Aufschlag (Sie können auch Angebote nach Aufschlag filtern).
- Wählen Sie vorzugsweise ein Angebot mit einem aktiven Benutzer und einem Aufschlag unter dem Durchschnitt.
- Überprüfen Sie die Zusammenfassung der Bestellung mit dem Betrag, der Zahlungsmethode, dem Aufschlag, der Bestell-ID und dem Ablaufdatum.
- Sie können Ihre Satoshis auf eine Bitcoin-Adresse mit einem Swap-Out-Gebühr (von LN zu BTC-Onchain) von etwa 1% erhalten (Sie können die On-Chain-Mining-Gebühren ändern).- Andernfalls erstellen Sie eine Rechnung mit einer LN-Brieftasche aus dieser [Liste](https://learn.robosats.com/docs/wallets/) und kopieren Sie die Rechnung auf Robosats.
- Kontaktieren Sie den Verkäufer über verschlüsselten Chat, um die Fiat-Zahlung zu besprechen.

Lassen Sie uns nun die Schritte für den Verkauf von Bitcoins auf Robosats betrachten:

- Passen Sie Ihr Angebot an, indem Sie die Zahlungsmethode, den Premium, die Verfallszeit usw. wählen.
- Die Fidelity Bond Size entspricht der Kaution auf BISC. Legen Sie 15% oder 10% Kaution fest, um die andere Partei zu ermutigen, fair zu spielen.
- Sperren Sie die Satoshis, um die Erstellung der Bestellung zu bestätigen und Spam zu vermeiden.
- Wenn jemand Ihr Verkaufsangebot annimmt, sprechen Sie mit dem Partner, um die Fiat-Zahlung abzuwickeln. Sobald die Zahlung erfolgt ist, ist der Handel abgeschlossen und die Satoshis verkauft!

## BISQ: Peer-to-Peer-Kauflösung

[Bisq](https://bisq.network/) ist eine dezentralisierte Handelsplattform für digitale Assets, hauptsächlich Bitcoin. Es ermöglicht direkte, sichere und private Transaktionen zwischen Benutzern auf der ganzen Welt ohne einen Vermittler.

🚨 Bitte seien Sie vorsichtig bei der Verwendung von Bisq, da es sich um eine fortgeschrittene Lösung handelt. Es ist möglicherweise nicht für Anfänger geeignet. Stellen Sie sicher, dass Sie etwas Erfahrung und Verständnis haben, bevor Sie loslegen. 🚨

Für diejenigen, die sich auskennen, gibt es hier eine kurze Anleitung, die die wesentlichen Schritte schnell beschreibt:

1. Herunterladen und Installieren: Besuchen Sie die Bisq-Website und laden Sie die Anwendung herunter. Installieren Sie es auf Ihrem System.
2. Zahlungsmodus einrichten: Öffnen Sie die Anwendung und gehen Sie zu "Konto". Fügen Sie die Details Ihrer Zahlungsmethode hinzu.
3. Füllen Sie Ihre Bisq-Brieftasche auf: Klicken Sie auf "Fonds" und "Fonds erhalten", um Ihre Bisq-Adresse zu erhalten. Senden Sie Bitcoins an diese Adresse.
4. Eine Transaktion durchführen: Klicken Sie auf "Kaufen/Verkaufen" und wählen Sie die gewünschte Transaktion aus. Folgen Sie den Anweisungen, um die Transaktion abzuschließen.
5. Bestätigen Sie den Empfang: Sobald Sie die Zahlung erhalten haben, bestätigen Sie diese in der Bisq-App. Dadurch wird das Bitcoin aus der Treuhand freigegeben.

   Vergessen Sie nicht, alle Details Ihrer Transaktionen zu überprüfen und nur mit vertrauenswürdigen Parteien zu handeln.

Hier ist ein umfassender Leitfaden, der Sie durch alle Schritte führt, um Bisq zu nutzen.

BISQ ist ein dezentrales und sicheres Netzwerk, das Ihr Eigentum respektiert. Es ist nicht verwahrend, was bedeutet, dass Sie immer noch Ihre Mittel besitzen. Darüber hinaus verwendet BISQ einen Token, den BSQ, mit dem Sie niedrigere Transaktionsgebühren zahlen und an der DAO (dezentralen autonomen Organisation) teilnehmen können. Um Verkäufer bei Bitcoin-Fiat-Transaktionen zu schützen, hat BISQ ein Signatur- und Kontolimit-System eingeführt. Als Käufer müssen Sie ein signiertes Konto erhalten, um Ihr Kauflimit zu erhöhen. Die Signatur ist auch eine Möglichkeit, das Handelshistorie zu überprüfen und die Sicherheit der Transaktionen zu gewährleisten.

Um Bisq zu installieren und Ihre Daten zu sichern, befolgen Sie diese einfachen Schritte:

- Gehen Sie zur bisc.network-Website, um die Software herunterzuladen (Screenshot der Download-Seite)
- Überprüfen Sie die Integrität der Software mit Tools wie denen von Loïc Morel für Windows-Benutzer.
- Sobald der Installer überprüft wurde, starten Sie BISQ, gewähren Sie die erforderlichen Berechtigungen und akzeptieren Sie die Nutzungsbedingungen. (Screenshot der Nutzungsbedingungen)
- BISQ wird über Tor mit dem Bitcoin-Netzwerk und sich selbst verbunden, was einige Zeit in Anspruch nehmen kann.
- Konfigurieren Sie Ihr Zahlungskonto und sichern Sie Ihre SID (Secure Identifier) Ihrer Brieftasche, um Verlust oder Diebstahl zu vermeiden. (Screenshot der Kontokonfigurationsseite)
- Legen Sie auch ein Passwort fest, um Ihre Informationen zu verschlüsseln.

Je nach Betriebssystem werden die BISQ-Daten an verschiedenen Orten gespeichert. Sie finden sie im Ordner "Data Directory". Achtung, wenn Sie diesen Ordner löschen, gehen alle Ihre BISQ-Daten verloren.
Um Ihre Daten mithilfe einer Sicherung wiederherzustellen:

- Kopieren Sie den Sicherungsordner in den Ordner "Benutzer / Anwendungsunterstützung / BISQ".
- Benennen Sie den Sicherungsordner in "BISQ" um.
- Starten Sie BISQ neu, und alle Ihre Daten sollten wiederhergestellt werden.

Bevor Sie mit dem Kauf oder Verkauf von Bitcoin auf BISQ beginnen, ist es entscheidend, Ihr Zahlungskonto zu konfigurieren. Sie können beispielsweise ein Konto in Ihrer nationalen Währung wie ein SEPA-Konto, ein REVOLUT-Konto oder ein PAYPAL-Konto einrichten.
Um Ihr REVOLUT-Konto zu konfigurieren:

- Fügen Sie ein Konto hinzu und wählen Sie REVOLUT aus der Liste der Optionen aus. (Screenshot der Liste der Kontooptionen)
- Sie können verschiedene Währungen wählen: Euro, Pfund Sterling, US-Dollar oder Schweizer Franken.
- La maximale Transaktionsdauer beträgt einen Tag und das Kauflimit beträgt 0,25 Bitcoin.
- Verwenden Sie Ihren persönlichen REVOLUT-Kontonamen, um Verwechslungen zu vermeiden.
- Stellen Sie sicher, dass Sie Ihre Konten signieren und Kaufgrenzen festlegen, um mehr Sicherheit zu gewährleisten.

Um Bitcoin auf BISQ zu kaufen:

- Gehen Sie zum Abschnitt "Kaufen", wo Sie verschiedene Märkte auswählen können. (Screenshot des Abschnitts "Kaufen")
- Um von reduzierten Gebühren zu profitieren, empfehlen wir den Kauf von BSQ, den Sie mit Bitcoin kaufen können.
- Sie können aus verschiedenen Angeboten je nach Preis, Menge, Zahlungsart usw. wählen.
- Um BSQ zu kaufen, legen Sie zuerst Bitcoin in Ihre Brieftasche.
- Wählen Sie ein Angebot mit niedrigem Aufschlag und geringer Menge für den Kauf von BSQ.
- BISQ überprüft die Gültigkeit des Angebots und die Verbindung des Paares.
- Wenn der Verkäufer nicht verbunden ist, wählen Sie einen anderen.
- Überprüfen Sie das Angebot und akzeptieren Sie einen Aufschlag von 5%.
- Bestätigen Sie die Gebühren und den BSQ-Austausch und warten Sie dann auf die Bestätigung der Transaktion, um Bitcoins mit BSQ zu kaufen.

Um Bitcoin auf BISQ zu verkaufen:

- Erstellen Sie ein neues Angebot im Tab "Verkaufen". (Screenshot des Tabs "Verkaufen")
- Sie können wählen, ob Sie die Anzahl der zu verkaufenden Bitcoins oder den Eurobetrag festlegen möchten, den Sie erhalten möchten.
- Sie können einen Aufschlag in Prozent über dem Marktpreis festlegen.
- Sie können einen Verkaufsbereich erstellen oder dem Käufer die Wahl lassen.
- Sie können auch einen Preis festlegen, um das Angebot zu stoppen.
- Wählen Sie den Mindestbetrag der Einzahlung und die Transaktionsgebühren.
- Finanzieren Sie die Bestellung, indem Sie die zu verkaufenden Bitcoins, den Betrag der Kaution und die Gebühren hinterlegen.
- Sobald Sie das Angebot erstellt haben, warten Sie, bis sich ein Käufer meldet.

Sobald der Käufer die Transaktion auf BISQ abgeschlossen hat, werden die Bitcoins automatisch an den Käufer gesendet und Sie erhalten das Geld. Das Konto wird nach einer Transaktion mit einem signierten Konto überprüft.

## LNP2PBOT

![LNp2pbot Tutorial](https://tube.nuagelibre.fr/videos/watch/57ed232d-6149-4267-be38-92b0f32800f7)

[Telegram](https://telegram.org/) ist eine Messaging-Plattform, die Ihnen mit Hilfe des Bots [Lnp2pbot](https://lnp2pbot.com/) ermöglicht, Bitcoins schnell und einfach zu kaufen und zu verkaufen. So geht's:

Um Bitcoins über den LNP2PBOT-Bot auf Telegram zu kaufen, befolgen Sie diese Schritte:

- Beginnen Sie damit, zum Twitter-Account des Bots Lnp2pbot zu gehen und auf den Link in der Bio zu klicken. (Screenshot des Twitter-Accounts des Bots und des Links in der Bio)
- Verwenden Sie in Telegram die Befehle "/buy" oder "/sell", um Kauf- oder Verkaufsaufträge zu veröffentlichen. (Screenshot der Verwendung der Befehle "/buy" oder "/sell")
- Gehen Sie zum P2P Lightning-Kanal, um Kauf- und Verkaufsangebote nach Ihren Kriterien zu finden. (Screenshot des P2P Lightning-Kanals)
- Erstellen Sie ein Kaufangebot mit dem Lnp2pbot und dem Befehl "/buy".
- Wählen Sie die gewünschte Währung, geben Sie den Betrag, den Preis (mit einem Premium, wenn gewünscht) an und wählen Sie Ihre Zahlungsmethode.
- Warten Sie, bis sich ein potenzieller Verkäufer bei Ihnen meldet.

Um Bitcoins über Revolut zu verkaufen, müssen Sie Folgendes tun:

- Klicken Sie auf "Satoshi verkaufen", um eine Benachrichtigung auf LNP2PBot zu öffnen. (Screenshot der Option "Satoshi verkaufen")
- Erhalten Sie eine Lightning-Rechnung, um die Satoshis zu verkaufen. (Screenshot der Lightning-Rechnung)
- Warten Sie, bis der Käufer eine Rechnung mit den Satoshis sendet, um die Zahlungen zu erhalten.
- Nehmen Sie direkt Kontakt mit dem Käufer über Telegram auf, um die Zahlungsmethode zu vereinbaren und die erforderlichen Informationen auszutauschen.
- Bestätigen Sie die Transaktion mit einer Notiz.

Wenn Sie Bitcoins kaufen möchten, indem Sie eine LN-Rechnung senden, befolgen Sie diese Schritte:

- Kopieren Sie die Rechnung und senden Sie sie an den Bot, um Satoshis zu kaufen.
- Nehmen Sie Kontakt mit dem Verkäufer auf, um den Kauf von Bitcoins abzuschließen.
- Im Falle eines Problems schlagen Sie vor, zu warten oder einen Abbruch zu versuchen.
- Stornieren Sie das Angebot und suchen Sie bei Bedarf ein neues.
- Wählen Sie ein Angebot, das sofortige CPA-Zahlungen für den Kauf von Satoshis akzeptiert.
- Senden Sie die Rechnung und warten Sie auf die Zahlungsbestätigung des Verkäufers.
- Sobald die Zahlung erfolgt ist, senden Sie die Bestätigung an den Bot.
- Warten Sie auf die Bestätigung des Empfangs von Euro und den Versand von Satoshis durch den Verkäufer.

Mit diesen Methoden können Sie Bitcoins sicher auf Telegram kaufen und verkaufen.

## Peach Bitcoin

Website: https://peachbitcoin.com/

Wir werden diese Lösung in BTC 205 von @pivi\_ im Detail betrachten. Hier sind die Video-Tutorials:

[Peach](https://peachbitcoin.com/) ist eine Schweizer mobile Anwendung, mit der Sie Bitcoins peer-to-peer kaufen und verkaufen können. Diese einfach zu bedienende Lösung bietet eine intuitive Benutzeroberfläche, die ideal für Kryptowährungstransaktionen ist.

Die Benutzeroberfläche der Peach-Anwendung besteht aus vier Registerkarten: Kaufen, Verkaufen, Historie und Einstellungen. (Screenshot der Anwendungsoberfläche)
Der Kauf von Bitcoins auf Peach ist vereinfacht. Um zu beginnen, müssen Sie ein Angebot erstellen. Dies ist möglich, indem Sie auf die Registerkarte "Kaufen" zugreifen. (Screenshot der Registerkarte "Kaufen") Durchsuchen Sie dann die verfügbaren Angebote, indem Sie wischen, bis Sie dasjenige finden, das Ihnen passt. Die akzeptierten Zahlungsmethoden sind vielfältig und umfassen Banküberweisung, Online-Wallet, Geschenkkarte und lokale Option. (Screenshot der verfügbaren Zahlungsmethoden)
Nachdem Sie ein Angebot ausgewählt haben, können Sie über den in der Anwendung integrierten Chat mit dem Verkäufer sprechen. (Screenshot des Anwendungs-Chats)
Nach der Zahlung, die vom Verkäufer bestätigt wird, ist die Transaktion abgeschlossen. Die Bitcoins werden dann an den Käufer gesendet, der eine Benachrichtigung erhält, die den Erhalt der Mittel bestätigt. (Screenshot der Benachrichtigung über den Erhalt von Bitcoins)

Peach ist eine nicht verwahrte Anwendung, was bedeutet, dass die Bitcoins während des gesamten Prozesses in Ihrem Besitz bleiben. Mögliche Streitigkeiten werden jedoch zentralisiert behandelt. Es ist daher wichtig, die Informationen zur Transaktion und Ihre persönlichen Informationen mithilfe der Backup-Funktion zu sichern. (Screenshot der Backup-Funktion)
Da Peach immer noch in der Beta-Version ist, können einige Fehler auftreten. Es wird empfohlen, alle Informationen vor Abschluss einer Transaktion zu überprüfen.
Insgesamt bietet die mobile Anwendung Peach eine zugängliche Lösung zum Kauf und Verkauf von Bitcoins im Peer-to-Peer-Modus. Eine sichere und optimale Nutzung von Peach ist der Schlüssel zum erfolgreichen Abschluss Ihrer Transaktionen.

## Hold Hodl

[HodlHodl](https://hodlhodl.com/) ist ein dezentralisierter Bitcoin-Marktplatz, der die Kontrolle und Sicherheit der Benutzer priorisiert. Im Gegensatz zu traditionellen Börsen arbeitet es nach einem Peer-to-Peer-Modell, das direkte Transaktionen zwischen Benutzern ermöglicht. Dank seines Multi-Signatur-Treuhand-Systems garantiert Hodl Hodl die Sicherheit von Mitteln während Transaktionen. Die Plattform unterstützt auch verschiedene Zahlungsmethoden und bietet Handelsoptionen wie Differenzkontrakte (CFD).

In diesem Tutorial erklären wir Ihnen, wie Sie auf der HodlHodl-Plattform Bitcoins im Peer-to-Peer-Modus kaufen und verkaufen können.

Bevor Sie die HodlHodl-Plattform nutzen können, sind einige Vorbereitungsschritte erforderlich:

- Öffnen Sie die HodlHodl-Website.
- Erstellen Sie ein Konto mit einer E-Mail-Adresse, um ein Protokoll Ihrer Transaktionen zu führen.
- Lesen Sie den Sicherheitsleitfaden sorgfältig durch, bevor Sie mit dem Handel beginnen.
- Beachten Sie, dass die Plattform nicht Open Source ist und einige Ihrer persönlichen Informationen speichert.

So kaufen Sie auf der HodlHodl-Plattform:

- Verwenden Sie die Filterfunktion, um Angebote zu finden, die Ihnen gefallen.
- Klicken Sie auf das Angebot, das Sie interessiert.
- Füllen Sie die erforderlichen Felder aus, um den Vertrag zu akzeptieren. - In unserem Beispiel haben wir Revolut als Zahlungsmethode verwendet.

Die Einrichtung des Multisig-Vertrags für die Transaktion erfolgt auf HodlHodl wie folgt:

- Sobald das Angebot akzeptiert wurde, leisten Sie die Zahlung über die gewählte Methode (in unserem Fall Revolut).
- Erstellen Sie einen Multisig-Vertrag, indem Sie ein Passwort generieren.
- Warten Sie auf die Einzahlung von Bitcoins an die Multisig-Adresse.
- Wählen Sie die Anzahl der Bestätigungen für den Vertrag.
- Leisten Sie die vereinbarte Zahlung an den Verkäufer und bestätigen Sie diese auf HodlHodl.
- Seien Sie geduldig, da die Einzahlungsdauer je nach verwendeter Bank lang sein kann.
- Warten Sie auf die Bestätigung des Verkäufers, bevor Sie die Bitcoins nach dem Kauf freigeben.

Das Erstellen eines Angebots zum Kauf oder Verkauf von Bitcoins auf HodlHodl erfolgt wie folgt:

- Geben Sie auf der HodlHodl-Website die Freigabeadresse für Kaufangebote an.
- Geben Sie den Betrag, den Preis und die Zahlungsmethode an.
- Sie können auch optionale Einstellungen wie Transaktionslimits oder einen Titel für das Angebot hinzufügen.
- Sobald das Angebot erstellt wurde, können Sie es nach Belieben anzeigen, bearbeiten, duplizieren oder löschen.

## Bonus: Side Shift.AI

Hier ist eine kurze Anleitung zur Verwendung von [SideShift AI](https://sideshift.ai/), einem sehr praktischen Tool zum Konvertieren von Shitcoins in Bitcoin. Es ist das ideale Tool für diejenigen, die alle ihre persönlichen Börsen geschlossen haben. Es ist kein Bestellsystem erforderlich und Liquidität ist verfügbar. Bitte beachten Sie jedoch, dass eine Gebühr von 2,5% pro Transaktion anfällt.

Wenn Sie Kryptowährungen mit KYC gekauft haben, wird empfohlen, Monero zu verwenden, um diese Kryptowährungen in Bitcoin umzuwandeln. Monero bietet eine höhere Privatsphäre als Bitcoin. Für zusätzliche Sicherheit wird auch die CoinJoin-Operation empfohlen. CoinJoin mischt Ihre Transaktionen mit denen anderer Benutzer, um die Rückverfolgbarkeit Ihrer Transaktionen zu erschweren.

Ich möchte Ihnen auch ein Open-Source-Tool für den Kauf und Verkauf von Bitcoins vorstellen. Mit diesem Tool können Sie aus vielen Blockchains wählen. Geben Sie einfach Ihre Bitcoin-Adresse ein und wählen Sie die Menge, die Sie senden möchten. Es ist nicht erforderlich, ein Konto zu erstellen oder Ihre Brieftasche mit dem Tool zu verbinden. Sie können einen festen Wechselkurs verwenden, um einen bestimmten Betrag zu senden oder zu empfangen. Darüber hinaus ermöglicht dieses Tool auch den Verkauf von Bitcoins gegen USDC.

### Unterstütze uns

Dieser Kurs sowie der gesamte Inhalt dieser Universität wurden Ihnen kostenlos von unserer Community zur Verfügung gestellt. Um uns zu unterstützen, können Sie ihn teilen, Mitglied der Universität werden und sogar über GitHub zu ihrer Entwicklung beitragen. Im Namen des gesamten Teams vielen Dank!

### Beachten Sie die Schulung

Ein Bewertungssystem für die Schulung wird bald in diese neue E-Learning-Plattform integriert! In der Zwischenzeit vielen Dank für das Absolvieren des Kurses und wenn Sie ihn genossen haben, denken Sie daran, ihn zu teilen.

# Um weiter zu gehen

## Interview mit Steph von Peach Bitcoin

Hier ist eine Zusammenfassung des Interviews:

Pitch Bitcoin ist eine nicht-custodial mobile Anwendung, die den Kauf und Verkauf von Bitcoin peer-to-peer ermöglicht. Derzeit besteht das Pitch Bitcoin-Team mit Sitz in der Schweiz aus acht Mitgliedern und bemüht sich, die Anwendung auch als Wallet zu nutzen. Das einzigartige Modell von Pitch Bitcoin basiert auf einer zentralisierten Unternehmensstruktur und behält gleichzeitig ein dezentrales Kauf- und Verkaufsbuch bei. Darüber hinaus bietet die Anwendung eine Option für Barzahlungen bei persönlichen Treffen.

Einer der Hauptvorteile von Pitch Bitcoin ist das Sicherheitsniveau, das es den Benutzern bietet. Das Deskrow-System mit Multisignatur und Time Lock ist so konzipiert, dass Konflikte behandelt und Transaktionen gesichert werden. Darüber hinaus hat Pitch Bitcoin einen priorisierten Zugang zum Geld der Multisignatur, was es ihm ermöglicht, die Bitcoins an den Käufer zu übertragen, falls der Verkäufer bösartiges Verhalten zeigt. Das Unternehmen plant, alle europäischen Währungen sowie andere Zahlungsmethoden bei seinem Start im Open Beta im Januar zu integrieren.

Die Idee von Pitch Bitcoin entstand aus der persönlichen Erfahrung seiner Gründerin in der Bitcoin-Branche. Nachdem sie Bitcoin im Jahr 2017 entdeckt und an mehreren Meetups und Konferenzen teilgenommen hatte, wurde sie zu einer Bitcoin-Maximalistin und sah die Möglichkeit, eine Plattform zu schaffen, auf der Bitcoiner sich treffen und Bartransaktionen durchführen können. Darüber hinaus enthält die Anwendung einen verschlüsselten Chat, um mit anderen Benutzern zu kommunizieren und die Anonymität der Benutzer zu wahren.

Derzeit entwickelt Pitch Bitcoin mehrere Funktionen, um die Arbeit der Verkäufer zu erleichtern, einschließlich der Erstellung einer API für Verkäufer, einer Plattform für große Verkäufer und der Integration von BTC Pay Server zur Automatisierung von Überweisungen. Die Anwendung wird im Januar 2023 im Open Beta gestartet.

Abschließend betont die Gründerin von Pitch Bitcoin die Bedeutung des Wettbewerbs im Bitcoin-Ökosystem, da das, was gut für Bitcoin ist, für alle von Vorteil ist. Sie ermutigt auch Vielfalt und Inklusion in der Bitcoin-Branche und darüber hinaus.

## Interview mit Pierre

Hier ist eine Zusammenfassung des Interviews:

Dieses Interview schließt die Schulung Bitcoin 205 ab, in der das Thema der Lösungen für den Peer-to-Peer-Kauf von Bitcoin behandelt wird. Diese von Pierre organisierte Schulung soll das französischsprachige Publikum über die technischen Lösungen für den Peer-to-Peer-Kauf von Bitcoin aufklären, ein Bereich, der bislang vernachlässigt wurde. Dank der erzielten Fortschritte ist es nun möglich, Bitcoin unter Wahrung der Privatsphäre zu kaufen und zu nutzen, sogar mit einem einfachen Telefon und der Telegram-Anwendung.

Eine der hervorgehobenen Methoden ist die Verwendung von CoinJoin mit Samurai, um die Sicherheit zu erhöhen. Diese Lösung minimiert die Risiken, die von zentralisierten Stellen ausgehen, die persönliche Informationen über Bitcoin-Nutzer speichern. Es wird empfohlen, Bitcoins in Nicht-KYC zu kaufen, eine Methode, die die Anonymität erhöht. Außerdem bieten einige Handelsplattformen wie Kraken niedrigere Abhebungsgebühren als andere, was den Grundsätzen von Bitcoin entgegenkommt.

Bisq, Robosat und Peach werden als demokratische Lösungen für den Handel mit Bitcoin dargestellt. Insbesondere Peach wird wegen seiner einfachen Zugänglichkeit als mobile Anwendung hervorgehoben. Auf der anderen Seite gibt es Herausforderungen, wie die Regulierung von Kryptowährungen und die Notwendigkeit, bestimmte Grenzen einzuhalten, um eine Überregulierung zu vermeiden.

Die Nutzung von Bitcoin-ATM-Automaten wird ebenfalls thematisiert, da diese eine kostengünstige Methode darstellen, um nicht-KYC-fähige Bitcoins zu erhalten. Je nach örtlicher Regulierung können diese Automaten zu Hause oder an öffentlichen Orten aufgestellt werden und können verwendet werden, um Bitcoins an seine Lieben zu verschenken oder für Zahlungen in Bars.

In der Ausbildung wird die wichtige Rolle der Bildung für das Verständnis von Bitcoin hervorgehoben. Es wird angedeutet, dass Bitcoin eine Lösung für den Fall einer Rezession oder Hyperinflation bieten kann und dass es wichtig ist, die Menschen über das Potenzial von Bitcoin aufzuklären, bevor es zu spät ist. Darüber hinaus wird betont, dass die Trennung von Staat und Geld genauso wesentlich ist wie die Trennung von Staat und Religion.

Abschließend wird Bitcoin als dezentralisierte Währung dargestellt, die öffentliche Bildung und Offenheit erfordert, um vollständig verstanden und genutzt zu werden. Die Schulung soll den Teilnehmern helfen, die verschiedenen Lösungen für Peer-to-Peer-Käufe zu verstehen und diese Werkzeuge zu nutzen, um ihre Anonymität und Sicherheit bei der Nutzung von Bitcoin zu erhöhen.

## Bonusartikel zum Thema Privatsphäre.

Ein toller [Artikel](https://decouvrebitcoin.fr/tribune-sur-le-kyc-et-lidentification-des-bitcoins-onchain/) von Loïc Morel über KYC und Identifikation.

Übersetzt mit www.DeepL.com/Translator (kostenlose Version)Dieser ausführliche Artikel untersucht die Herausforderungen und Lösungen zur Wahrung der Privatsphäre bei der Beschaffung und Verwendung von Bitcoins. Loïc entlarvt einige gängige Vorstellungen über die KYC-Identifikation (Know Your Customer), erläutert die mit diesem Prozess verbundenen Risiken und bietet Techniken zur Aufrechterhaltung der Anonymität von Transaktionen an. Es ist ein unverzichtbarer Lesestoff für diejenigen, die die Feinheiten der Privatsphäre in der Welt von Bitcoin verstehen und lernen möchten, wie man Tools wie CoinJoin, Stonewall und PayJoin verwendet, um die Verfolgung von Transaktionen zu verschleiern und so ihre Privatsphäre zu schützen.
