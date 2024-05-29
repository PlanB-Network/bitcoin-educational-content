---
name: JoinBot
description: Verstehen und Verwenden des JoinBots
---

![DALL·E – Samurai-Roboter in einem roten Wald, 3D-Rendering](assets/cover.webp)

***ACHTUNG:** Nach der Verhaftung der Gründer von Samourai Wallet und der Beschlagnahme ihrer Server am 24. April ist **der Dienst JoinBot nicht mehr verfügbar**. Derzeit ist es daher nicht mehr möglich, dieses Werkzeug zu nutzen. Sie können jedoch weiterhin Stonewall X2 durchführen, müssen jedoch einen Partner finden und die PSBT-Austausche manuell durchführen. Dieser Dienst könnte in den kommenden Monaten abhängig vom Fortschritt des Falles wieder aufgenommen werden.*

_Wir verfolgen die Entwicklungen in diesem Fall sowie die Entwicklungen bezüglich der zugehörigen Tools genau. Seien Sie versichert, dass wir dieses Tutorial aktualisieren werden, sobald neue Informationen verfügbar sind._

_Dieses Tutorial wird nur zu Bildungs- und Informationszwecken bereitgestellt. Wir befürworten oder ermutigen die Verwendung dieser Tools zu kriminellen Zwecken nicht. Es liegt in der Verantwortung jedes Benutzers, die Gesetze in seiner Gerichtsbarkeit zu beachten._

---

JoinBot ist ein neues Tool, das mit dem neuesten Update 0.99.98f der beliebten Bitcoin-Wallet-Software Samourai Wallet eingeführt wurde. Es ermöglicht Ihnen, einfach eine gemeinsame Transaktion durchzuführen, um Ihre Privatsphäre zu optimieren, ohne einen Partner finden zu müssen.

*Vielen Dank an den ausgezeichneten Fanis Michalakis für die Idee, DALL-E für das Miniaturbild zu verwenden!*

## Was ist eine gemeinsame Transaktion bei Bitcoin?

Bitcoin basiert auf einem verteilten und transparenten Kontenbuch. Jeder kann die Transaktionen der Benutzer dieses elektronischen Bargeldsystems verfolgen. Um eine gewisse Vertraulichkeit zu gewährleisten, kann der Bitcoin-Benutzer Transaktionen mit einer spezifischen Struktur durchführen, um eine plausible Abstreitbarkeit bei der Interpretation dieser Transaktionen hinzuzufügen.

Das Ziel ist nicht, die Informationen direkt zu verbergen, sondern sie unter anderen zu verwirren. Dieses Ziel wird insbesondere bei Coinjoins verwendet, bei denen Transaktionen verwendet werden, um die Historie einer Bitcoin-Münze zu unterbrechen und ihre Rückverfolgung zu erschweren. Um dieses Ziel zu erreichen, müssen mehrere Inputs und Outputs mit dem gleichen Betrag in der Transaktion erstellt werden.

Die Inputs sind die Eingänge einer Bitcoin-Transaktion und die Outputs sind die Ausgänge. Die Transaktion verwendet ihre Eingänge, um neue Ausgänge zu erstellen und die Ausgabenbedingungen für eine Münze zu ändern. Dieser Mechanismus ermöglicht es, Bitcoins zwischen den Benutzern zu verschieben.
Ich erkläre Ihnen das im Detail in diesem Artikel: Mechanismus einer Bitcoin-Transaktion: UTXO, Inputs und Outputs.

Eine Möglichkeit, die Spuren in einer Bitcoin-Transaktion zu verwischen, besteht darin, eine gemeinsame Transaktion durchzuführen. Wie der Name schon sagt, handelt es sich dabei um eine Vereinbarung zwischen mehreren Benutzern, die jeweils einen Betrag an Bitcoins als Input in eine gemeinsame Transaktion einzahlen und einen Betrag als Output erhalten.

Wie bereits erwähnt, ist die bekannteste Struktur für gemeinsame Transaktionen der Coinjoin. Zum Beispiel werden bei Coinjoin Whirlpool 5 Teilnehmer mit dem gleichen Betrag an Bitcoins als Eingabe und Ausgabe in den Transaktionen verwendet.

![Schema einer Coinjoin-Transaktion auf Whirlpool](assets/1.webp)

Ein externer Beobachter dieser Transaktion wird nicht in der Lage sein zu wissen, welcher Output zu welchem Benutzer als Eingabe gehört. Wenn wir das Beispiel des Benutzers Nr. 4 (violett) nehmen, können wir seine UTXO als Eingabe erkennen, aber wir werden nicht wissen, welcher der 5 Outputs wirklich seiner ist. Die ursprüngliche Information wird nicht versteckt, sondern in einer Gruppe verwirrt.
Der Benutzer kann den Besitz eines bestimmten UTXO in der Ausgabe leugnen. Dieses Phänomen wird als "plausible Abstreitbarkeit" bezeichnet und ermöglicht es, Vertraulichkeit in einer transparenten Bitcoin-Transaktion zu erreichen.

Um mehr über Coinjoin zu erfahren, erkläre ich ALLES in diesem ausführlichen Artikel: Verstehen und Verwenden von CoinJoin auf Bitcoin.

Obwohl Coinjoin sehr effektiv ist, um die Rückverfolgung eines UTXO zu unterbrechen, ist es nicht für direkte Ausgaben geeignet. Tatsächlich erfordert seine Struktur die Verwendung von Inputs mit vordefinierten Beträgen und Outputs mit dem gleichen Wert (abzüglich der Mining-Gebühren). Die Ausgabetransaktion bei Bitcoin ist jedoch ein kritischer Moment für die Vertraulichkeit, da sie oft eine physische Verbindung zwischen dem Benutzer und seiner On-Chain-Aktivität herstellt. Es scheint daher unerlässlich, Vertraulichkeitstools für Ausgaben zu verwenden. Es gibt auch andere kollaborative Transaktionsstrukturen, die speziell für effektive Zahlungstransaktionen entwickelt wurden.

## Die StonewallX2-Transaktion

Unter den vielen Ausgabetools, die in der Samourai Wallet angeboten werden, gibt es die kollaborative Transaktion StonewallX2. Es handelt sich um einen Mini-Coinjoin zwischen zwei Benutzern, der für Zahlungen gedacht ist. Von außen betrachtet kann diese Transaktion zu mehreren möglichen Interpretationen führen. Es gibt also plausible Abstreitbarkeit und folglich Vertraulichkeit für den Benutzer.

Diese kollaborative StonewallX2-Transaktion ist in der Samourai Wallet und in der Sparrow Wallet verfügbar. Dieses Tool ist interoperabel zwischen den beiden Softwareprogrammen.

Der Mechanismus ist ziemlich einfach zu verstehen. Hier ist seine praktische Funktionsweise:

> - Ein Benutzer möchte eine Zahlung in Bitcoins leisten (zum Beispiel bei einem Händler).
> - Er erhält die Empfangsadresse des tatsächlichen Zahlungsempfängers (des Händlers).
> - Er erstellt eine spezifische Transaktion mit mehreren Inputs: mindestens einen, der ihm gehört, und einen, der einem externen Mitarbeiter gehört.
> - Die Transaktion hat 4 Outputs, darunter 2 mit dem gleichen Betrag: einer zur Adresse des Händlers, um ihn zu bezahlen, einer als Wechselgeld, das zum Benutzer zurückkehrt, ein Output mit dem gleichen Wert wie die Zahlung, der zum Mitarbeiter geht, und ein weiterer Output, der ebenfalls zum Mitarbeiter zurückkehrt.

Hier ist zum Beispiel eine klassische StonewallX2-Transaktion, bei der ich eine Zahlung von 50.125 Sats geleistet habe. Der erste Input von 102.588 Sats stammt aus meiner Samourai Wallet. Der zweite Input von 104.255 Sats stammt aus dem Wallet meines Mitarbeiters:

![Schema einer StonewallX2-Transaktion](assets/2.webp)

Es gibt 4 Outputs, von denen 2 den gleichen Betrag haben, um die Spuren zu verwischen:

> - 50.125 Sats, die an den tatsächlichen Empfänger meiner Zahlung gehen.
> - 52.306 Sats, die mein Wechselgeld repräsentieren und daher zu einer Adresse meiner Wallet zurückkehren.
> - 50.125 Sats, die zu meinem Mitarbeiter zurückkehren.
> - 53.973 Sats, die zu meinem Mitarbeiter zurückkehren.
>   Am Ende der Transaktion hat der Mitarbeiter sein ursprüngliches Guthaben wieder (abzüglich der Mining-Gebühren) und der Benutzer hat dem Händler bezahlt. Dadurch wird der Transaktion eine große Menge an Entropie hinzugefügt und die eindeutigen Verbindungen zwischen Absender und Zahlungsempfänger werden aufgebrochen.

Die Stärke der StonewallX2-Transaktion besteht darin, dass sie eine der empirischen Regeln der Chain-Analysten vollständig konterkariert: die gemeinsame Eigentümerschaft der Inputs in einer Multi-Input-Transaktion. Mit anderen Worten, in den meisten Fällen kann man davon ausgehen, dass alle Inputs einer Bitcoin-Transaktion einer einzigen Person gehören. Satoshi Nakamoto hatte dieses Problem der Benutzeranonymität bereits in seinem White Paper erkannt:

> "Als zusätzliche Firewall könnte für jede Transaktion ein neues Schlüsselpaar verwendet werden, um sie nicht mit einem gemeinsamen Eigentümer zu verknüpfen. Bei Multi-Input-Transaktionen ist jedoch eine Verknüpfung unvermeidlich, da sie zwangsläufig zeigen, dass ihre Inputs von einem gemeinsamen Eigentümer gehalten wurden."

Dies ist eine der vielen empirischen Regeln, die in der On-Chain-Analyse verwendet werden, um Adresscluster zu erstellen. Um mehr über diese Heuristiken zu erfahren, empfehle ich Ihnen, diese Serie von 4 Artikeln von Samourai zu lesen, die das Thema wunderbar einführen.

Die Stärke der StonewallX2-Transaktion liegt darin, dass ein externer Beobachter denken wird, dass die verschiedenen Inputs der Transaktion einem gemeinsamen Eigentümer gehören. In Wirklichkeit handelt es sich jedoch um zwei verschiedene Benutzer, die zusammenarbeiten. Die Analyse der Zahlung wird also in die Irre geführt und die Benutzeranonymität bleibt gewahrt.

Von außen betrachtet kann eine StonewallX2-Transaktion nicht von einer Stonewall-Transaktion unterschieden werden. Der einzige Unterschied besteht darin, dass Stonewall nicht kollaborativ ist. Es verwendet nur die UTXOs eines einzigen Benutzers. Aber in ihrer Struktur im Kontenbuch sind Stonewall und StonewallX2 völlig identisch. Dadurch können noch mehr mögliche Interpretationen dieser Transaktionsstruktur hinzugefügt werden, da ein externer Beobachter nicht wissen kann, ob die Inputs von einer einzigen Person oder von zwei Mitarbeitern stammen.

Darüber hinaus hat StonewallX2 den Vorteil gegenüber einem PayJoin vom Typ Stowaway, dass es in allen Situationen verwendet werden kann. Der tatsächliche Zahlungsempfänger gibt keine Inputs in die Transaktion ein. Daher kann man StonewallX2 verwenden, um bei jedem Bitcoin-Händler zu bezahlen, auch wenn dieser nicht Samourai oder Sparrow verwendet.

Der Hauptnachteil dieser Transaktionsstruktur ist hingegen, dass sie einen Mitarbeiter erfordert, der bereit ist, seine Bitcoins zu verwenden, um sich an Ihrer Zahlung zu beteiligen. Wenn Sie Bitcoin-Freunde haben, die bereit sind, Ihnen in jeder Situation zu helfen, ist das kein Problem. Wenn Sie hingegen keine anderen Samurai-Wallet-Nutzer kennen oder niemand für eine Zusammenarbeit zur Verfügung steht, dann sind Sie blockiert.

Um dieses Problem zu lösen, haben die Samourai-Teams ihrer App vor kurzem eine neue Funktion hinzugefügt: JoinBot.

# Was ist JoinBot?

Das Prinzip von JoinBot ist einfach. Wenn Sie niemanden finden, mit dem Sie bei einer StonewallX2-Transaktion zusammenarbeiten können, können Sie mit ihm zusammenarbeiten. Konkret heißt das, dass Sie tatsächlich eine kollaborative Transaktion direkt mit Samourai Wallet durchführen werden.

Dieser Service ist vor allem für unerfahrene Nutzer sehr bequem, da er rund um die Uhr verfügbar ist. Wenn Sie eine dringende Zahlung leisten müssen und eine StonewallX2 durchführen möchten, müssen Sie nicht mehr einen Freund kontaktieren oder online nach einem Mitarbeiter suchen. JoinBot wird sich um Ihre Unterstützung kümmern.

Ein weiterer Vorteil von JoinBot ist, dass die UTXOs, die er als Input liefert, ausschließlich aus Whirlpool-Postmixen stammen, was die Vertraulichkeit Ihrer Zahlung erhöht. Da JoinBot die ganze Zeit online ist, sollten Sie außerdem mit UTXOs zusammenarbeiten, die über ein großes prospektives Anonset verfügen.

Natürlich verfügt JoinBot über einige Kompromisse, auf die hingewiesen werden sollte:

Wie bei einem klassischen StonewallX2 ist Ihr Mitarbeiter zwangsläufig darüber informiert, welche UTXOs verwendet werden und wohin sie gehen. Im Fall von JoinBot kennt Samourai die Details dieser Transaktion. Das muss nicht unbedingt etwas Schlechtes sein, aber Sie sollten es im Hinterkopf behalten.

Um Spam zu vermeiden, erhebt Samourai eine Servicegebühr von 3,5 % auf den Betrag der tatsächlichen Transaktion, wobei die Höchstgrenze bei 0,01 BTC liegt. Wenn ich z. B. eine tatsächliche Zahlung von 100 Kiloats mit JoinBo

## Wie kann ich JoinBot nutzen?

Um eine JoinBot-Transaktion durchzuführen, benötigen Sie ein Samourai Wallet. Sie können es hier oder aus dem Google Playstore herunterladen.

Im Gegensatz zu den meisten von Samourai entwickelten Tools hat Sparrow Wallet bislang noch nicht angekündigt, JoinBot zu implementieren. Dieses Tool ist daher nur auf Samourai verfügbar.

Sehen Sie sich in diesem Video Schritt für Schritt an, wie Sie eine StonewallX2-Transaktion mit JoinBot durchführen können :

![Comment utiliser Joinbot](https://youtu.be/80MoMz2Ne5g)

Hier ist das Schema der Transaktion, die wir gerade im Video durchgeführt haben:

![Schéma de ma transaction StonewallX2 avec JoinBot.](assets/3.webp)

Dort lassen sich 5 Inputs entdecken:
- 3 Inputs von 100 Kiloats, die von Samourai (JoinBot) stammen.
- 2 Inputs, die aus meiner persönlichen Brieftasche stammen, von 3.524 Sats und 1,8 Megasat.

Die 4 Outputs der Transaktion sind wie folgt:
- 1 von 212 452 Sats an den eigentlichen Empfänger meiner Zahlung.
- 1 weitere über denselben Betrag, die an eine Samurai-Adresse zurückkehrt.
- 1 Wechsel, der ebenfalls an Samurai zurückkehrt, für 87.302 Sats. Dies entspricht der Differenz zwischen ihrem gesamten Input (300.000 Sats) und dem Offuscation-Output (212.452 Sats) abzüglich der Mining-Kosten.
- 1 Wechsel, der zu einer anderen Adresse in meinem Portfolio zurückkehrt. Er entspricht der Differenz zwischen der Summe meiner Inputs und der tatsächlichen Auszahlung abzüglich der Mining-Gebühren.

Zur Erinnerung: Die Mining-Gebühren stellen keinen Output der Transaktionen dar. Sie stellen lediglich die Differenz zwischen der Summe der Inputs und der Summe der Outputs dar.

## Fazit

JoinBot ist ein zusätzliches Werkzeug, das dem Samourai-Benutzer mehr Wahlmöglichkeiten und Freiheiten einräumt. Er ermöglicht es, eine kollaborative StonewallX2-Transaktion direkt mit Samurai als Mitarbeiter durchzuführen. Diese Art von Transaktion hilft, die Privatsphäre der Nutzer zu verbessern.

Wenn Sie eine klassische StonewallX2 mit einem Freund durchführen können, empfehle ich Ihnen dennoch, diese Nutzung des Tools vorzuziehen. Wenn Sie hingegen feststecken und keinen Mitarbeiter für eine Zahlung finden, wissen Sie, dass JoinBot 24 Stunden am Tag und 7 Tage die Woche zur Verfügung steht, um mit Ihnen zusammenzuarbeiten.

**Externe Ressourcen :**
- https://medium.com/oxt-research/understanding-bitcoin-privacy-with-oxt-part-1-4-8177a40a5923
- https://www.pandul.fr/post/comprendre-et-utiliser-le-coinjoin-sur-bitcoin
