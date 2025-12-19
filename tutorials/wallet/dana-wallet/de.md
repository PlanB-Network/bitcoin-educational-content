---
name: Dana Wallet
description: Minimalistisches Portfolio für stille Zahlungen (BIP-352)
---

![cover](assets/cover.webp)



Die Wiederverwendung von Bitcoin-Adressen ist eine der direktesten Bedrohungen für die Vertraulichkeit der Nutzer. Wenn ein Empfänger eine einzige Adresse verwendet, um mehrere Zahlungen zu erhalten, kann jeder Beobachter alle damit verbundenen Transaktionen zurückverfolgen und ihre finanzielle Geschichte rekonstruieren. Dieses Problem betrifft vor allem Urheber von Inhalten, Wohltätigkeitsorganisationen oder Aktivisten, die eine Spendenadresse öffentlich anzeigen möchten, ohne ihre Privatsphäre oder die ihrer Spender zu gefährden.



Dana Wallet antwortet auf dieses Problem mit einer eleganten Lösung: Silent Payments. Dieses minimalistische, quelloffene wallet, das 2024 auf den Markt kommt, generiert eine wiederverwendbare statische Adresse und garantiert gleichzeitig, dass jede erhaltene Zahlung auf einer separaten Adresse in der Blockchain landet. Der Absender braucht keine vorherige Interaktion mit dem Empfänger, und kein externer Beobachter kann einzelne Transaktionen miteinander verknüpfen. Auf der Blockchain sehen diese Zahlungen wie ganz normale Taproot-Transaktionen aus.



Dana Wallet ist auf Mainnet und Signet verfügbar, aber die Entwickler betrachten es noch als experimentell und empfehlen, keine Gelder einzuzahlen, die Sie nicht bereit sind zu verlieren. In diesem Tutorial werden wir die Signet-Version verwenden, um Silent Payments zu entdecken, ohne echtes Geld zu riskieren.



## Was ist Dana Wallet?



### Philosophie und Ziele



Dana Wallet verfolgt einen "SP-first"-Ansatz: Der wallet erzeugt ausschließlich Silent-Payments-Adressen und akzeptiert nur diese Art von Zahlungen. Sie können mit dieser Anwendung keine klassische Bitcoin-Adresse (Legacy, SegWit oder Taproot Standard) erstellen. Diese bewusste Einschränkung ermöglicht es Ihnen, sich voll und ganz auf das Erlernen des BIP-352-Protokolls zu konzentrieren, ohne durch andere Funktionen abgelenkt zu werden. Die übersichtliche Oberfläche bevorzugt bewusst eine einfache Bedienung gegenüber einer Fülle von Optionen, so dass das Tool auch für Benutzer zugänglich ist, die mit on-chain-Vertraulichkeitskonzepten nicht vertraut sind.



Das Projekt ist vollständig quelloffen und wurde mit Flutter für die mobile Schnittstelle und Rust für die interne kryptografische Logik entwickelt. Diese Architektur kombiniert ein flüssiges Benutzererlebnis mit optimaler Leistung für intensive Scanvorgänge.



### Wie funktionieren die stillen Zahlungen?



Silent Payments (BIP-352) basieren auf einem ausgeklügelten kryptographischen Mechanismus, der den Elliptic Curve Diffie-Hellman Key Exchange (ECDH) verwendet. Der Empfänger generiert eine statische Adresse (beginnend mit `sp1...` auf mainnet oder `tsp1...` auf Signet), die aus zwei verschiedenen öffentlichen Schlüsseln besteht: einem Scan-Schlüssel ($B_{scan}$), um eingehende Zahlungen zu erkennen, und einem Spend-Schlüssel ($B_{spend}$), um erhaltene Gelder auszugeben. Diese Trennung ermöglicht es, den Ausgabeschlüssel auf der wallet-Hardware zu belassen, während der Scan-Schlüssel auf einem angeschlossenen Gerät verwendet wird.



Wenn ein Absender eine Zahlung vornehmen möchte, kombiniert sein wallet die Summe der privaten Schlüssel seiner Eingänge mit dem öffentlichen Scan-Schlüssel des Empfängers, um ein gemeinsames ECDH-Geheimnis zu berechnen. Dieses Geheimnis erzeugt einen kryptografischen "Tweak", der zusammen mit dem Ausgabenschlüssel des Empfängers eine eindeutige Taproot-Adresse für diese Transaktion erzeugt.



Der Empfänger kann diese Berechnung mit seinem privaten Scan-Schlüssel und den in der Transaktion sichtbaren öffentlichen Schlüsseln nachvollziehen (mathematische Eigenschaft von Diffie-Hellman). Dies ermöglicht ihm, das Geld ohne vorherige Interaktion mit dem Absender zu erkennen und auszugeben.



Dieser Ansatz bietet mehrere Vorteile:




- Empfängergeheimnis**: Jede Zahlung geht an eine andere Adresse
- Absendervertraulichkeit**: keine dauerhafte Kennung zur Verknüpfung von Zahlungen
- Kein Server eines Drittanbieters**: Das Protokoll arbeitet autonom
- Ununterscheidbare Transaktionen**: Stille Zahlungen sehen aus wie normale Taproot-Transaktionen



Der größte Nachteil sind die Kosten für das Scannen: Der Empfänger muss jede neue Taproot-Transaktion analysieren, um die für ihn bestimmten Transaktionen zu erkennen.



Wenn Sie mehr über die technische Funktionsweise von Silent Payments erfahren möchten, empfehlen wir Ihnen den Kurs BTC204 zum Thema Vertraulichkeit in Bitcoin, der ein eigenes Kapitel über Silent Payments enthält:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Unterstützte Plattformen



Dana Wallet ist als Android-Anwendung verfügbar. Die APK kann über das von den Entwicklern bereitgestellte F-Droid-Repository, über Obtainium oder direkt von GitHub heruntergeladen werden. Für Linux-Nutzer ist es technisch möglich, die Flutter-Anwendung für den Desktop zu kompilieren.



Die App ist weder auf iOS noch über die offiziellen Stores (Google Play, App Store) verfügbar, was ihren experimentellen Status und ihre Ausrichtung auf ein technisches Publikum widerspiegelt.



## Einrichtung



### Wesentliche Voraussetzungen



Um Dana Wallet auf Android zu installieren, benötigen Sie ein Android-Gerät, bei dem die Option "Unbekannte Quellen" in den Sicherheitseinstellungen aktiviert ist. Es ist kein Konto oder eine Registrierung erforderlich.



### F-Cold Kaution hinzufügen



Die empfohlene Methode ist, das spezielle F-Droid-Repository von Dana Wallet hinzuzufügen. Gehen Sie zu `fdroid.silentpayments.dev`, wo Sie den Link zum Repository und einen QR-Code zum Scannen finden. Das Repository bietet derzeit 3 Anwendungen: die Mainnet-Version, Development und Signet.



![Page du dépôt F-Droid Dana Wallet avec QR code et lien](assets/fr/01.webp)



### Installation über F-Droid



Öffnen Sie die F-Droid-Anwendung auf Ihrem Android-Gerät und rufen Sie dann die Einstellungen über das Symbol unten rechts auf. Wählen Sie "Repositories", um App-Quellen zu verwalten. Drücken Sie die Schaltfläche "+", um ein neues Repository hinzuzufügen, und scannen Sie dann den QR-Code oder fügen Sie den Link "https://fdroid.silentpayments.dev/fdroid/repo" ein. Sobald das Repository hinzugefügt wurde, sehen Sie die drei verfügbaren Versionen von Dana Wallet. Wählen Sie "Dana Wallet - Lesezeichen" und drücken Sie "Installieren".



![Ajout du dépôt F-Droid et installation de Dana Wallet - Signet](assets/fr/02.webp)



## Erstmalige Konfiguration



### Erstellung eines Portfolios



Beim ersten Start zeigt Dana Wallet einen Begrüßungsbildschirm an, auf dem seine Aufgabe vorgestellt wird: "Senden und empfangen Sie Spenden ohne Zwischenhändler". Drücken Sie "Begin", um fortzufahren. Auf dem nächsten Bildschirm werden die drei wichtigsten Vorteile der Anwendung vorgestellt:




- Mühelose Spenden**: Spendeneingang in Sekundenschnelle
- Standardmäßiger Datenschutz**: keine Notwendigkeit für Server oder komplexe Infrastruktur
- E-Mail-ähnliche Erfahrung**: Senden und empfangen Sie Bitcoins so einfach wie eine E-Mail



Sie können wählen zwischen "Wiederherstellen", um ein bestehendes Portfolio wiederherzustellen, oder "Neues wallet erstellen", um ein neues Portfolio zu erstellen. Drücken Sie "Neuen wallet erstellen".



![Premier lancement de Dana Wallet et création du portefeuille](assets/fr/03.webp)



Die Anwendung generiert dann eine Wiederherstellungsphrase, die Sie sorgfältig auf einem physischen Datenträger notieren sollten. Auch bei Testgeldern, die keinen wirklichen Wert haben, sollten Sie gute Sicherungspraktiken anwenden.



### Interface und Parameter



Sobald das Portfolio erstellt wurde, gelangen Sie zur Hauptschnittstelle, die in zwei Registerkarten unterteilt ist: "Transaktionen" und "Einstellungen".



Die Registerkarte **Transaktion** zeigt Ihr Bitcoin-Guthaben (und dessen Umrechnung in Dollar), eine Liste der letzten Transaktionen und zwei Aktionsschaltflächen: "Bezahlen", um Geld zu senden, und eine Schaltfläche zum Empfangen (Download-Symbol).



Die Registerkarte **Einstellungen** bietet vier Optionen:




- seed-Phrase** anzeigen: zeigt Ihre Wiederherstellungsphrase zur sicheren Aufbewahrung an
- Fiat-Währung ändern**: Anzeigewährung ändern (standardmäßig USD)
- Backend-URL festlegen**: Konfigurieren Sie die Blindbit-Server-URL (siehe nächster Abschnitt)
- Wipe wallet**: löscht das wallet vollständig aus dem Gerät



![Interface principale Transact et menu Settings](assets/fr/04.webp)



### Der Blindbit-Server



Dana Wallet verwendet einen Indexierungsserver namens **Blindbit**, um Ihre Stillen Zahlungen zu erkennen. Das Verständnis seiner Funktionsweise ist wichtig, um das Vertrauensmodell der Anwendung zu bewerten.



**Warum brauchen wir einen Server?



Um eine stille Zahlung zu erkennen, muss Ihr wallet theoretisch alle Taproot-Transaktionen in jedem Block scannen und für jede Transaktion eine kryptografische Berechnung (ECDH) durchführen. Auf einem Mobiltelefon wäre dieser Vorgang zu rechenintensiv und zu bandbreitenaufwändig.



Der Blindbit-Server löst dieses Problem, indem er für alle Taproot-Transaktionen Zwischendaten (so genannte "Tweaks") vorberechnet. Ihr wallet lädt dann diese Tweaks (33 Byte pro Transaktion) herunter und führt die endgültige Berechnung **vor Ort** durch, um zu prüfen, ob eine Zahlung Ihnen gehört.



**Gewährleistete Vertraulichkeit**



Im Gegensatz zu einem herkömmlichen Electrum-Server, bei dem Sie Ihre Adressen preisgeben, weiß der Blindbit-Server nicht, welche Zahlungen Ihnen gehören. Er stellt allen Nutzern die gleichen Daten zur Verfügung, und es ist Ihr Telefon, das die endgültige Überprüfung durchführt. Ihre Vertraulichkeit ist also gegenüber dem Server gewahrt.



**Standard-Server



Dana Wallet verwendet den öffentlichen Server `silentpayments.dev/blindbit/signet` (für Signet) oder `silentpayments.dev/blindbit/mainnet` (für Mainnet). Sie können diese URL in den Einstellungen ändern, wenn Sie Ihren eigenen Server hosten.



**Hosten Sie Ihren eigenen Blindbit-Server**



Für Benutzer, die totale Souveränität wünschen, ist es möglich, ihren eigenen Blindbit Oracle Server zu hosten. Dies erfordert :




- Ein vollständiger Bitcoin-Kernknoten **nicht geeicht** (nicht pruned)
- Installation von Blindbit Oracle (verfügbar auf GitHub: `setavenger/blindbit-oracle`)
- Ca. 10 GB zusätzlicher Festplattenspeicher
- Technische Kenntnisse (Go-Kompilierung, Serverkonfiguration)



Für Umbrel oder Start9 gibt es noch keine verpackte Anwendung. Die Installation bleibt vorerst manuell. Dieser Bereich befindet sich in aktiver Entwicklung, und in der Zukunft könnten leichter zugängliche Lösungen auftauchen.



## Täglicher Gebrauch



### Empfang von Geldern



Um Bitcoins zu empfangen, drücken Sie auf dem Hauptbildschirm die Empfangstaste (Download-Symbol). Dana Wallet zeigt dann Ihre vollständige Silent Payment Adresse im Format `tsp1q...` auf Bookmark an. Die Schnittstelle bietet mehrere Optionen:




- QR-Code anzeigen**: zeigt den QR-Code Ihrer Adresse zum einfachen Scannen an
- Freigeben**: Geben Sie die Adresse über die Anwendungen Ihres Telefons frei
- Kopieren**: Kopiert die Adresse in die Zwischenablage



Wie auf dem Bildschirm angezeigt, können Sie diese Adresse in Ihren sozialen Netzwerken veröffentlichen, ohne Ihre Privatsphäre zu gefährden.



![Affichage de l'adresse de réception Silent Payment](assets/fr/05.webp)



Um Ihr erstes Testguthaben auf Signet zu erhalten, verwenden Sie den speziellen Silent Payments Faucet, der unter `silentpayments.dev/faucet/signet` erreichbar ist. Kopieren Sie Ihre Adresse `tsp1...`, fügen Sie sie in das dafür vorgesehene Feld des Faucets ein und validieren Sie die Anfrage. Warten Sie, bis ein Block abgebaut wird (etwa 10 Minuten auf Signet).



### Eine Zahlung senden



Um Geld zu senden, drücken Sie auf dem Hauptbildschirm die Schaltfläche "Bezahlen". Es erscheint der Bildschirm "Empfänger auswählen" mit drei Optionen zur Angabe des Empfängers:




- Zahlungsinformationen manuell eingeben
- Einfügen aus der Zwischenablage**: Einfügen einer Adresse aus der Zwischenablage
- QR-Code scannen**: Scannen Sie einen QR-Code, der die Adresse enthält



Sobald die Adresse des Empfängers bestätigt wurde, können Sie auf dem Bildschirm "Betrag eingeben" den zu sendenden Betrag in Satoshis eingeben. Ihr verfügbares Guthaben wird als Referenz angezeigt. Klicken Sie auf "Weiter zur Gebührenauswahl", um fortzufahren.



![Envoi d'un paiement : sélection du destinataire et du montant](assets/fr/06.webp)



Der nächste Bildschirm zeigt drei Gebührenstufen an, die sich nach der Dringlichkeit richten:




- Schnell** (10-30 Minuten): höhere Gebühren für schnelle Bestätigung
- Normal** (30-60 Minuten): moderate Kosten
- Langsam** (1+ Stunde): Mindestgebühr für nicht dringende Transaktionen



Nach der Auswahl der Gebührenhöhe werden auf dem Bestätigungsbildschirm "Bereit zum Senden" alle Details zusammengefasst: Zieladresse, Betrag, geschätzte Dauer und Transaktionsgebühr. Prüfen Sie diese Informationen sorgfältig und drücken Sie dann auf "Senden", um die Transaktion abzuschicken.



Nach dem Senden erscheint die Transaktion in Ihrer Historie mit dem Status "Unbestätigt", bis sie in eine Sperre aufgenommen wird. Ihr Saldo wird entsprechend aktualisiert.



![Sélection des frais, confirmation et transaction envoyée](assets/fr/07.webp)



## Vorteile und Grenzen



### Höhepunkte





- Pädagogisch**: vereinfachte Schnittstelle mit Schwerpunkt auf dem Lernen Stille Zahlungen
- Bidirektional**: unterstützt im Gegensatz zu anderen Portfolios sowohl das Senden als auch das Empfangen
- Open-Source**: vollständig überprüfbarer Code auf GitHub
- Dedizierte Faucet**: macht es einfacher, Testfinanzierung zu erhalten
- Ohne Konto**: keine Registrierung oder persönliche Daten erforderlich



### Zu berücksichtigende Zwänge





- Experimentell**: ungeprüfte Software, mit Vorsicht zu verwenden bei Mainnet
- Begrenzte Plattform**: hauptsächlich Android, keine iOS-Version
- Reduzierte Funktionalität**: keine Münzkontrolle, keine Unterkonten, kein Lightning
- Intensives Scannen**: Die Erkennung von Zahlungen verbraucht erhebliche Ressourcen



## Bewährte Praktiken



### seed Sicherheit



Auch bei Signet-Tests mit wertlosem Hintergrund sollten Sie Ihre Wiederherstellungsphrase ernst nehmen. Verwenden Sie die Option "seed-Phrase anzeigen" in den Einstellungen, um sie sorgfältig aufzuschreiben. Als gute Praxis sollten Sie völlig getrennte Geldbörsen für Signet und Mainnet verwenden: Verwenden Sie niemals einen seed, der zu Testzwecken erstellt wurde, auf einem wallet, der für den Empfang echter Gelder bestimmt ist.



### Warnung über experimentellen Status



Dana Wallet wird von seinen Entwicklern noch als experimentell angesehen. Wie sie deutlich sagen: "Verwenden Sie keine Mittel, die Sie nicht zu verlieren bereit sind". Entscheiden Sie sich zu Lernzwecken für die Signet-Version. Wenn Sie die Mainnet-Version verwenden, beschränken Sie sich auf token-Beträge.



### Sicherung und Wiederherstellung



Für die Wiederherstellung von Silent Payments-Fonds ist ein wallet erforderlich, das mit dem BIP-352-Protokoll kompatibel ist. Ein Standard-wallet kann die Blockchain nicht scannen, um Ihre stummen UTXO-Zahlungen wiederherzustellen. Lassen Sie Dana Wallet installiert oder verwenden Sie die Option "Wiederherstellen" beim ersten Start, um einen vorhandenen wallet wiederherzustellen.



## Vergleich mit BIP-47 und PayJoin



| Critère | Silent Payments (BIP-352) | BIP-47 PayNyms | PayJoin (BIP-78) |
|---------|---------------------------|----------------|------------------|
| Adresse statique | Oui (`sp1...`) | Oui (code de paiement) | Non |
| Interaction requise | Aucune | Transaction de notification initiale | À chaque paiement |
| Empreinte on-chain | Aucune (transactions normales) | OP_RETURN visible | Transaction modifiée |
| Scan côté receveur | Intensif (chaque bloc) | Léger (après notification) | Aucun |
| Confidentialité expéditeur | Excellente | Limitée (lien après notification) | Bonne (brouillage) |

Mit Silent Payments entfällt die BIP-47-Benachrichtigungstransaktion auf Kosten eines teureren Scans. PayJoin löst ein anderes Problem (Eingabekorrelation) und kann mit Silent Payments kombiniert werden.



## Schlussfolgerung



Dana Wallet ist ein wertvolles Lehrmittel, um in einer risikofreien Umgebung mehr über Silent Payments zu erfahren. Sein minimalistischer Ansatz ermöglicht es Ihnen, die grundlegenden Mechanismen des BIP-352-Protokolls zu verstehen, ohne durch sekundäre Funktionen abgelenkt zu werden. Indem Sie mit Signet experimentieren, entwickeln Sie ein praktisches Verständnis für diese vielversprechende Technologie für die Vertraulichkeit von Bitcoin-Transaktionen.



Silent Payments ist ein bedeutender Schritt nach vorn, um Benutzerfreundlichkeit und Schutz der Privatsphäre in Einklang zu bringen. Der Enthusiasmus der Community und die ersten Integrationen in verschiedene Wallets (Cake Wallet, BitBox02, BlueWallet zum Versenden) deuten auf eine Zukunft hin, in der die Veröffentlichung einer Spendenadresse die finanzielle Privatsphäre ihres Besitzers nicht mehr gefährdet.



## Ressourcen



### Offizielle Dokumentation




- Dana Wallet GitHub-Repository: https://github.com/cygnet3/danawallet
- F-Cold Kaution: https://fdroid.silentpayments.dev
- Website der Gemeinschaft für stille Zahlungen: https://silentpayments.xyz
- Spezifikation BIP-352: https://bips.dev/352



### Signet-Prüfgeräte




- Faucet Stille Zahlungen: https://silentpayments.dev/faucet/signet
- Signet Mempool Explorer: https://mempool.space/signet



### Blindbit-Server (selbst gehostet)




- Blindbit Oracle (GitHub): https://github.com/setavenger/blindbit-oracle