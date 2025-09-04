---
name: be-BOP
description: Praktischer Leitfaden zur Monetarisierung Ihres Unternehmens mit be-BOP
---

![cover-bebop](assets/cover.webp)



**be-BOP** ist eine E-Commerce-Plattform, die für Unternehmer entwickelt wurde, die online und offline in völliger Autonomie verkaufen und dabei Zahlungen in Bitcoin, über ein Bankkonto und in bar akzeptieren möchten. Die Lösung ist auch für jede Art von Organisation nützlich, die Spenden sammeln oder ihre verschiedenen Aktivitäten monetarisieren möchte.



Die Lösung ist einfach, leicht und eigenständig. Sie ermöglicht die Einrichtung eines Online-Shops, auch in einem Umfeld, in dem traditionelle Finanzdienstleistungen nur begrenzt oder gar nicht vorhanden sind. In der Tat wurde **be-BOP** so konzipiert, dass es mit oder ohne Zugang zu Banken effizient funktioniert und Bitcoin als Zahlungsinfrastruktur verwendet.



In diesem Tutorial werden wir Sie Schritt für Schritt durch:





- Erstellen Sie Ihr erstes Online-Geschäft mit **be-BOP**
- Personalisieren Sie Ihr Schaufenster und Ihre Produkte
- Verfügbare Zahlungsarten konfigurieren
- Verstehen Sie die besten Praktiken für effektiven Online-Verkauf mit **be-BOP**



Für dieses Tutorial sind keine fortgeschrittenen technischen Kenntnisse erforderlich. Es richtet sich sowohl an Entwickler als auch an Handwerker, Händler, Genossenschaften oder Unternehmer, die souverän und widerstandsfähig in den digitalen Handel einsteigen wollen.



## Voraussetzungen für die Installation von be-BOP auf Ihrem eigenen Server



Bevor Sie mit der Installation von be-BOP beginnen, stellen Sie sicher, dass Sie über die folgende technische Infrastruktur verfügen. Diese Elements sind für die korrekte Funktion der Plattform unerlässlich:



### S3-kompatibler Speicher



be-BOP verwendet ein Speichersystem, um Dateien (z. B. Produktbilder) zu verwalten. Dies erfordert den Zugang zu einem S3-Dienst, wie z. B.:





- [MinIO](https://min.io/) selbst gehostet
- Amazon S3 (AWS)
- Scaleway Objektspeicher



Sie müssen einen Bucket konfigurieren und die folgenden Informationen angeben:





- S3_BUCKET**: Name des Eimers
- S3_ENDPOINT_URL**: Zugangslink zu Ihrem S3-Dienst
- S3_KEY_ID** und S3_KEY_SECRET: Ihre Zugangscodes
- S3_REGION**: die Region Ihres S3-Dienstes



### MongoDB-Datenbank im ReplicaSet-Modus



be-BOP verwendet MongoDB, um Speicher-, Benutzer-, Produkt- und andere Daten zu speichern.



Sie haben zwei Möglichkeiten:





- MongoDB lokal mit aktiviertem **ReplicaSet-Modus** installieren
- Verwenden Sie einen Online-Dienst wie **MongoDB Atlas**



Sie benötigen die folgenden Variablen:





- MONGODB_URL**: Datenbankverbindung Address
- MONGODB_DB**: Name der Datenbank



## Node.js-Umgebung



be-BOP arbeitet mit Node.js. Stellen Sie sicher, dass Sie **Node.js** Version 18 oder höher und **Corepack** aktiviert haben (wird benötigt, um Paketmanager wie pnpm zu verwalten). Der auszuführende Befehl ist `corepack enable`



### Git LFS installiert



Einige Ressourcen (z. B. große Bilder) werden über Git LFS (Large File Storage) verwaltet. Vergewissern Sie sich, dass Sie Git LFS mit dem Befehl `git lfs install` auf Ihrem Rechner installiert haben. Sobald diese Voraussetzungen erfüllt sind, können Sie mit dem nächsten Schritt fortfahren: dem Herunterladen und Konfigurieren von be-BOP.



**Hinweis:** Ein technischer Leitfaden für die Softwareverteilung ist in einem separaten Lernprogramm verfügbar.



## Erstellen eines Super-Admin-Kontos



Beim ersten Start von be-BOP wird ein **Super Admin**-Konto erstellt. Dieses Konto verfügt über alle Berechtigungen, die für die Verwaltung der Back-Office-Funktionen erforderlich sind. Um ein Konto zu erstellen, folgen Sie diesen Schritten:





- Gehen Sie zu "yourresiteweb/admin/login"
- Erstellen Sie ein Super-Admin-Konto mit einem sicheren Login und Passwort



Mit diesem Konto haben Sie Zugang zu allen Back-Office-Funktionen. Nach der Erstellung können Sie sich durch Eingabe Ihres Benutzernamens und Passworts anmelden.



![login](assets/fr/001.webp)



## Back-Office-Konfiguration und Sicherheit



Bevor Sie Ihre Interface-Back-Office-Verbindung konfigurieren, müssen Sie einen eindeutigen Hash erstellen. Dies bietet Schutz vor böswilligen Akteuren, die versuchen, den Verbindungslink zu Ihrem Interface-Administrator zu stehlen.



Um Hash zu erstellen, gehen Sie zu `/admin/Einstellungen`. In dem Abschnitt, der der Sicherheit gewidmet ist (z. B. "Admin Hash"), definieren Sie eine eindeutige Zeichenfolge (Hash). Nach der Registrierung wird die Back-Office-URL geändert (z. B. `/admin-yourhash/login`), um den Zugang für Unbefugte zu beschränken.



![hash-login](assets/fr/002.webp)



2.2. Aktivieren Sie den Wartungsmodus (falls erforderlich)



Aktivieren Sie in /admin/Einstellungen (Einstellungen > Allgemein über Interface-Grafiken) die Option "Wartungsmodus aktivieren" unten auf der Seite.



![maintenance-mode](assets/fr/003.webp)



Bei Bedarf können Sie eine Liste autorisierter IPv4-Adressen (durch Kommata getrennt) angeben, um den Zugriff auf das Front-Office während der Wartung zu ermöglichen. Das Backoffice bleibt für Administratoren zugänglich.



![ip-bebop](assets/fr/004.webp)



## Einrichtung der Kommunikation



Damit be-BOP Benachrichtigungen (z.B. für Bestellungen, Registrierungen oder Systemmeldungen) versenden kann, müssen Sie mindestens eine Kommunikationsmethode konfigurieren. Es stehen zwei Optionen zur Verfügung: E-Mail (SMTP) oder Nostr.



### SMTP-Konfiguration (E-Mail)



be-BOP kann E-Mails über einen SMTP-Server versenden. Sie benötigen gültige SMTP-Zugangsdaten, die oft von einem E-Mail-Dienst (z. B. Mailgun, Gmail usw.) bereitgestellt werden.



Hier ist, was Sie wissen müssen:



SMTP_HOST: SMTP-Server Address (z. B. smtp.mailgun.org)



SMTP_PORT: der zu verwendende Port (häufig 587 oder 465)



SMTP_USER: Ihr Benutzername (normalerweise eine E-Mail Address)



SMTP_PASSWORD: Ihr Passwort oder API-Schlüssel



SMTP_FROM: die E-Mail Address, die als Absender erscheinen wird




### Nostr-Konfiguration



be-BOP ermöglicht es Ihnen, Benachrichtigungen über das Nostr-Protokoll, einer dezentralen Nachrichteninfrastruktur, zu versenden. Dazu benötigen Sie generate oder Supply einen privaten Nostr-Schlüssel (NSEC). Sie können generate diesen Schlüssel direkt über den Interface von be-BOP in dem Abschnitt über Nostr erstellen. Wenn diese Elements korrekt konfiguriert sind, kann be-BOP automatisch Nachrichten und Warnungen an Ihre Benutzer senden.



## Kompatible Zahlungsmittel



be-BOP ist mit mehreren Zahlungslösungen kompatibel, so dass Sie Ihren Kunden mehr Flexibilität bieten können. Hier erfahren Sie, was Sie brauchen, um die für Sie am besten geeignete Zahlungsmethode einzurichten.



### Bitcoin Onchain



mit be-BOP können Sie Bitcoin-Zahlungen direkt auf dem Blockchain (On-Chain) akzeptieren, einfach und sicher.



**Konfigurationsschritte:**





- Gehen Sie zum Menü **Zahlungseinstellungen**
- Klicken Sie auf **Bitcoin Nodeless**, um auf die Zahlungsparameter von On-Chain zuzugreifen.
- Füllen Sie die folgenden Felder aus:



| Champ                  | Description                                               | Exemple à utiliser                              |
|------------------------|-----------------------------------------------------------|--------------------------------------------------|
| **BIP Standard**       | Le type d’adressage utilisé                               | BIP84 (pour les adresses au format bech32 commençant par `bc1`) |
| **Clé publique étendue** | Votre Zpub (ou Xpub selon le portefeuille utilisé)        | `zpub...` (extrait de votre portefeuille Bitcoin) |
| **Derivation Index**   | L’index de départ pour la génération des adresses         | `1`                                              |
| **Mempool URL**        | L’URL du service mempool utilisé pour suivre les transactions | `https://mempool.space`                         |

![payment-nodeless](assets/fr/005.webp)



**Tipp:** Um Ihren erweiterten öffentlichen Schlüssel (Zpub) zu erhalten, können Sie die erweiterten Einstellungen Ihres Bitcoin Wallet (Sparrow wallet, BlueWallet, Specter, usw.) konsultieren. Stellen Sie sicher, dass Ihr Wallet **nicht schreibgeschützt** ist, wenn Sie die Transaktionshistorie verwenden möchten.



### Lightning Network



be-BOP kann dank Lightning Network auch Bitcoin-Sofortzahlungen akzeptieren. Derzeit sind zwei Konfigurationsmöglichkeiten verfügbar:



**Phoenixd*



Gehen Sie zum Menü "Zahlungseinstellungen" und klicken Sie auf "Phoenixd"



![phoenixd](assets/fr/006.webp)



Sie müssen dann **das Passwort oder die token-Authentifizierung** eingeben, die Sie mit Ihrer Phoenixd-Instanz verbindet, einem von Acinq entwickelten Backend, mit dem Sie Lightning-Zahlungen über Ihren eigenen Knotenpunkt verwalten können, ohne die Komplexität der Verwaltung von Zahlungskanälen.



**Schweizer Bitcoin Lohn**



Wenn Sie einen Lightning-Knoten nicht selbst verwalten möchten, ist **Swiss Bitcoin Pay** eine gebrauchsfertige, einfach zu konfigurierende Lösung, die sich ideal für den Einstieg in die Akzeptanz von Lightning-Zahlungen ohne komplexe Infrastruktur eignet.



Konfigurationsschritte:





- Klicken Sie im Menü "Zahlungseinstellungen" auf "Swiss Bitcoin Pay"
- Loggen Sie sich in Ihr Schweizer Bitcoin Pay-Konto ein (oder erstellen Sie eines, wenn Sie noch keines haben).
- Geben Sie den von Swiss Bitcoin Pay gelieferten API-Schlüssel ein und klicken Sie dann auf "Speichern"



Einmal eingerichtet, erstellt be-BOP automatisch generate Lightning-Rechnungen für Ihre Kunden, und Sie erhalten die Zahlungen direkt auf Ihr Swiss Bitcoin Pay-Konto. Diese Lösung ist ideal für Benutzer, die die technische Komplexität eines persönlichen Knotens vermeiden und gleichzeitig schnelle, kostengünstige Zahlungen akzeptieren möchten.



![swissbtcpay](assets/fr/007.webp)



### PayPal



Neben Bitcoin können Sie mit be-BOP auch Barzahlungen über PayPal akzeptieren, eine bekannte und weit verbreitete internationale Lösung.



Konfigurationsschritte:





- Gehen Sie zum Menü "Zahlungseinstellungen"
- Klicken Sie auf `PayPal
- Geben Sie in Ihrem Paypal-Konto (Entwicklerbereich) die `Client ID` und das `Geheimnis` ein
- Wählen Sie die Währung Ihrer Wahl (z.B. **USD**, **EUR**, **XOF**, usw.)
- Klicken Sie auf `Speichern



![paypal](assets/fr/008.webp)



**Hinweis:** Sie müssen über ein PayPal-Geschäftskonto verfügen, um generate diese Identifikatoren zu verwenden. Sie können sie über das [Entwickler]-Portal (https://developer.paypal.com) erhalten



### SumUp



Die Software integriert jetzt die **SumUp**-Zahlungslösung, die es Ihnen ermöglicht, Kreditkartenzahlungen einfach, sicher und effizient zu akzeptieren. Um von dieser Funktionalität zu profitieren, ist eine Erstkonfiguration erforderlich. Hier sind die Schritte, die für eine klare und schrittweise Implementierung zu befolgen sind, nummeriert:





- Beginnen Sie mit der Eingabe Ihres **API-Schlüssels**, einem vertraulichen Schlüssel, den Sie von SumUp erhalten haben, als Sie Ihr Entwicklerkonto eingerichtet haben. Er stellt eine sichere Verbindung zwischen Ihrem SumUp-Konto und der Software her.
- Füllen Sie das Feld "Händlercode" mit dem eindeutigen Code aus, der Ihr Unternehmen innerhalb der SumUp-Plattform identifiziert. Dieser Code ist wichtig, um Transaktionen mit Ihrem Unternehmen zu verknüpfen.
- Wählen Sie im Feld "Währung" die Hauptwährung aus, die Sie für Ihre Transaktionen verwenden (z. B. **EUR**, **USD**, **CDF**, usw.).
- Wenn Sie alle Felder korrekt ausgefüllt haben, klicken Sie auf die Schaltfläche "Speichern", um Ihre Einstellungen zu speichern. Das System stellt dann die Verbindung zu Ihrem SumUp-Konto her, und Ihre Software ist bereit, Zahlungen zu akzeptieren.



![payment-sumup](assets/fr/009.webp)



Nach dieser Konfiguration ist die **SumUp**-Integration aktiv und einsatzbereit, so dass Sie schnell Geld auszahlen und Ihre Transaktionen direkt in der Software verfolgen können.



### Streifen



be-BOP bietet auch eine vollständige Integration mit **Stripe**, einer der beliebtesten Online-Zahlungsplattformen. Stripe ermöglicht es Ihnen, Online-Zahlungen per Kreditkarte, digitalem Wallet und verschiedenen anderen Zahlungsmethoden zu akzeptieren. Hier erfahren Sie, wie Sie es aktivieren:





- Geben Sie den **geheimen Schlüssel** ein, der im Stripe-Dashboard angegeben ist.
- Füllen Sie das Feld **Öffentlicher Schlüssel** aus, das ebenfalls von Stripe bereitgestellt wird.
- Wählen Sie die **Hauptwährung**.
- Speichern Sie die Konfiguration und klicken Sie dann auf "Speichern".



![payment-stripe](assets/fr/010.webp)



⚠️ **Bitte beachten Sie:** Es ist wichtig, die für Ihre Tätigkeit geltende Mehrwertsteuerregelung zu kennen (z.B.: Verkauf unter Mehrwertsteuer im Land des Verkäufers, Befreiung unter Rechtfertigung oder Verkauf zum Mehrwertsteuersatz des Landes des Käufers), um die Rechnungsstellungsoptionen in **be-BOP** korrekt zu konfigurieren.



## Konfiguration der Währung



**be-BOP** bietet ein fortschrittliches Währungsmanagement und ist an Mehrwährungsumgebungen und spezifische Buchhaltungsanforderungen angepasst. Um die Konsistenz der Finanzoperationen und des Berichtswesens zu gewährleisten, ist es wichtig, die verschiedenen im System verwendeten Währungen richtig zu konfigurieren. Nachfolgend finden Sie die Schritte, die für diese Konfiguration erforderlich sind:





- Wählen Sie die **Hauptwährung** (`Hauptwährung`)
- Wählen Sie `Sekundärwährung
- Definieren Sie **Referenzwährung** (`Preisreferenzwährung`)
- Buchführungswährung" angeben



Sobald alle Währungen korrekt konfiguriert sind, sorgt die Software für eine automatische und genaue Umrechnung von Transaktionen in mehreren Währungen, wobei eine strenge buchhalterische Konsistenz gewahrt bleibt.



![settings-currencies](assets/fr/011.webp)



## Konfiguration des Wiederherstellungszugangs über E-Mail oder Nostr



Vergewissern Sie sich in `/admin/settings` über das Modul **ARM**, dass der Superadmin-Account eine **email Address** oder eine **recovery pub** enthält, um die Prozedur zu erleichtern, wenn Sie Ihr Passwort vergessen haben.



![settings-users](assets/fr/012.webp)



## Spracheinstellungen



Die Software ist mehrsprachenfähig, um sich an ein internationales Publikum anzupassen und die Benutzerfreundlichkeit zu erhöhen. Um die mehrsprachige Funktionalität zu aktivieren, ist es wichtig, die verfügbaren Sprachen zu konfigurieren und eine **Standardsprache** zu definieren.



![settings-languages](assets/fr/13.webp)



## Interface und Identitätskonfiguration in be-BOP



**be-BOP** bietet Designern alle Werkzeuge, die sie für die Gestaltung einer Website benötigen. Der erste Schritt besteht darin, in den Einstellungen den Bereich "Admin > Merch > Layout" zu öffnen. Beginnen Sie damit, die **Top Bar**, die **Navbar** und den **Footer** zu konfigurieren.



### Le Top Bar



Mit der Konfiguration **Top Bar** können Sie die visuelle Identität Ihrer Software personalisieren, indem Sie die wichtigsten Informationen gleich in der ersten Zeile des Interface anzeigen. Dies stärkt den Wiedererkennungswert der Marke und bietet einen klaren Kontext für die Benutzer.



#### Konfigurationsschritte:





- Geben Sie in das Feld "Markenname" den Namen Ihres Unternehmens, Ihrer Organisation oder Ihres Produkts ein. Dieser Name wird oben auf dem Interface erscheinen und stellt Ihre wichtigste visuelle Identität dar.
- Geben Sie den Titel der Website an**: Der gewählte Titel sollte den Zweck der Plattform zusammenfassen. Dieser Titel kann in der Kopfzeile oder in der Registerkarte des Browsers erscheinen.
- Beschreibung der Website hinzufügen**: Hier können Sie eine kurze Beschreibung Ihrer Initiative eingeben. Diese Beschreibung hilft den Nutzern, das Tool in den richtigen Kontext zu setzen, und kann auch für SEO-Zwecke verwendet werden.



Nach der Eingabe dieser Informationen wird in der **Top Bar** eine klare, professionelle und kohärente Präsentation Ihrer Lösung angezeigt.



#### Links in der oberen Leiste



Mit dem Abschnitt "Links" in der Top-Leiste können Sie Verknüpfungen zu wichtigen Seiten in Ihrer Anwendung oder auf externen Websites hinzufügen. Diese Links werden direkt in der Top-Leiste angezeigt und bieten Ihren Benutzern einen schnellen, strukturierten Zugriff.



#### Konfigurationsschritte:





- Name des Links eingeben (Text)**: Geben Sie in das Feld "Text" den Namen oder die Bezeichnung des Links ein, wie er erscheinen soll (z. B. Home, Kontakt, Hilfe usw.).
- Link Address (Url)** angeben: Geben Sie in das Feld "URL" die vollständige Address der Zielseite (intern oder extern) ein.
- Fügen Sie bei Bedarf weitere Links hinzu**: In jeder Konfigurationszeile können Sie über die Felder `Text` und `Url` einen zusätzlichen Link hinzufügen.
- Links speichern**: Wenn Sie alle Links eingegeben haben, klicken Sie auf die Schaltfläche "Link zur oberen Leiste hinzufügen", um sie zu speichern.



Diese Konfiguration ermöglicht es Ihnen, eine klare, flüssige und zugängliche Navigation durch die verschiedenen Abschnitte Ihrer Website oder zu ergänzenden Ressourcen anzubieten.



![settings-topbar](assets/fr/014.webp)



### La Nav Bar



Im Abschnitt **Navbar** können Sie das Hauptnavigationsmenü Ihres be-BOP konfigurieren, das sich normalerweise an der Seite oder oben auf dem Interface befindet. Dieses Menü führt den Benutzer zu den verschiedenen Seiten und Funktionen der Anwendung. Die Konfiguration der Links ist einfach und intuitiv. So funktioniert es:





- Geben Sie den Namen des Links (`Text`)** ein: Füllen Sie in der Konfigurationszeile zunächst das Feld `Text` aus. Dies entspricht dem Namen des Links, der in der Navigationsleiste angezeigt wird (Beispiele: *Dashboard*, *Benutzer*, *Einstellungen*...).
- Geben Sie den Link Address (`Url`)** ein: Neben dem Feld `Text` befindet sich das Feld `Url`. Geben Sie in dieses Feld die Address der Seite ein, zu der der Link weiterleiten soll. Dies kann eine interne Route oder ein Link zu einer externen Seite sein.
- Fügen Sie bei Bedarf mehrere Links hinzu**: Unter der ersten Zeile stehen neue Felder `Text` und `Url` zur Verfügung, in die Sie beliebig viele Links einfügen können. Jede Zeile steht für einen zusätzlichen Navigationslink.
- Links speichern**: Wenn Sie alle Elements eingegeben haben, klicken Sie auf die Schaltfläche "Link zur Navigationsleiste hinzufügen", um die Ergebnisse zu speichern und in der Navigationsleiste anzuzeigen.



Diese Konfiguration ermöglicht eine effiziente Strukturierung des Zugriffs auf verschiedene Teile der Software und verbessert die Ergonomie und das Benutzererlebnis.



![navbar](assets/fr/015.webp)



### Die Fußzeile



Im Abschnitt **Fußzeile** können Sie die Fußzeile Ihrer Software anpassen und nützliche Informationen oder Links hinzufügen. Bevor Sie die Links konfigurieren, aktivieren Sie zunächst eine bestimmte Option:





- Aktivieren Sie die Anzeige des Labels "Powered by be-BOP "**: Aktivieren Sie die Schaltfläche "Powered by be-BOP anzeigen", um dieses Label in der Fußzeile anzuzeigen.
- Geben Sie den Namen des Links ein (`Text`)**: Füllen Sie das Feld `Text` aus, das dem Wortlaut des Links in der Fußzeile entspricht (Beispiele: *Terms*, *Privacy*, *Contact*...).
- Link Address angeben (`Url`)**: Geben Sie in das Feld `Url` die Address der Zielseite (intern oder extern) ein.
- Fügen Sie bei Bedarf weitere Links hinzu**: Verwenden Sie die zusätzlichen Zeilen, um so viele Links zu erstellen, wie Sie möchten.
- Links speichern**: Klicken Sie auf die Schaltfläche "Fußzeilenlink hinzufügen", um Links zu speichern.



![footer](assets/fr/016.webp)



### Visuelle Personalisierung



**⚠️ Vergessen Sie nicht, die Logos für die hellen und dunklen Themen sowie das Favicon über** `Admin > Merch > Bilder` einzustellen.



Hier erfahren Sie, wie Sie das Aussehen Ihrer Website anpassen können:



#### Zum Abschnitt Bilder gehen



Menü `Admin` > `Merch` > `Bilder`.



#### Ein neues Bild hinzufügen



Klicken Sie auf `Neues Bild`.



#### Wählen Sie eine lokale Datei



Klicken Sie auf "Dateien auswählen" und wählen Sie dann ein Image von Ihrer Hard-Diskette aus.



#### Wählen Sie die zu importierende Datei



Doppelklicken Sie auf das zu importierende Bild (helles Logo, dunkles Logo oder Favicon).



#### Benennung des Bildes



Füllen Sie das Feld "Name des Bildes" aus.



#### Bild hinzufügen



Klicken Sie auf "Hinzufügen", um den Import abzuschließen.



![pictures](assets/fr/017.webp)



### Einrichtung der Verkäuferidentität



#### Einstellungen zur Identität



In diesem Bereich, der über `Admin > Identität` (oder `Einstellungen > Identität`) zugänglich ist, können Sie die administrativen und rechtlichen Informationen Ihres Unternehmens konfigurieren.



#### Rechtliche Informationen





- Firmenname**: offizieller Firmenname.
- Unternehmens-ID**: gesetzliche Kennung oder Registrierungsnummer (RCCM, SIRET...).



#### Geschäft Address





- Straße**: postalische Address (Straße, Nummer...).
- Land**: Land.
- Staat**: Provinz oder Region.
- Stadt**: Stadt.
- Postleitzahl**: Postleitzahl.



#### Kontaktinformationen





- E-Mail**: Professionelle E-Mail Address.
- Telefon**: Telefonnummer des Unternehmens.



#### Bankkonto





- Name des Kontoinhabers**: Name des Kontoinhabers.
- Kontoinhaber Address**: Address des Inhabers.
- IBAN**: Internationale Bankkontonummer.
- BIC**: SWIFT/BIC-Code.



![bank-account](assets/fr/019.webp)



#### Rechnungsstellung





- Klicken Sie auf "Mit Hauptgeschäftsinformationen ausfüllen", um die Daten vorauszufüllen.
- Sehr-rechts-Ausstellerinformationen**: Feld für rechtliche/steuerliche Informationen, die auf Rechnungen sichtbar sind.
- Klicken Sie auf "Aktualisieren", um die Änderungen zu speichern.



**Hinweis:** Sie können auch zusätzliche Informationen eingeben, die auf dem Invoice angezeigt werden sollen, je nach Ihren Bedürfnissen.



![vat](assets/fr/019.webp)



![issuer-info](assets/fr/020.webp)



#### Physisches Geschäft Address



Für diejenigen, die ein physisches Geschäft haben, fügen Sie eine spezifische vollständige Address unter "Admin > Einstellungen > Identität" oder einem speziellen Abschnitt hinzu. Dadurch kann sie auf offiziellen Dokumenten und gegebenenfalls in der Fußzeile angezeigt werden.



![seller-id](assets/fr/021.webp)



## Produktmanagement



### Erstellung eines neuen Produkts



Gehen Sie zu `Admin > Merch > Produkte`, um ein Produkt hinzuzufügen oder zu ändern. Füllen Sie die folgenden Felder aus:



#### Grundlegende Informationen





- Produktname**: Name des Produkts (z. B. *BOP-T-Shirt limitierte Auflage*).
- Slug**: URL-Bezeichner ohne Leerzeichen (z. B. `tshirt-bop-edition-limitee`).
- Alias** *(optional)*: Nützlich für das schnelle Hinzufügen zum Warenkorb über ein eigenes Feld.



![product-config](assets/fr/028.webp)



#### Preisgestaltung





- Preisbetrag**: Produktpreis (z. B. "25,00").
- Preiswährung**: Währung (EUR, USD, BTC, usw.).
- Besondere Produkte**:
  - dies ist ein kostenloses Produkt.
  - dies ist ein "Pay-what-you-want"-Produkt.



#### Produkt-Optionen





- Einzelprodukt (`standalone`)**: nur ein Zusatz pro Bestellung möglich (z.B. Spende, Eintrittskarte).
- Produkt mit Variationen**:
  - Kontrollieren Sie nicht `Standalone`.
  - Prüfen Sie "Das Produkt hat leichte Abweichungen (kein Bestandsunterschied)".
  - Hinzufügen:
    - Name** (z.B. *Größe*),
    - Werte** (z. B.: S, M, L, XL),
    - Ggf. Preisunterschiede** (z. B.: "+2 USD" für XL).



![product-details](assets/fr/029.webp)



## Verwaltung der Bestände



### Erweiterte Optionen bei der Erstellung eines Produkts (Bestand, Lieferung, Tickets usw.)



#### Produkt mit begrenztem Bestand



Wenn Ihr Produkt nicht in unbegrenzten Mengen verfügbar ist, markieren Sie "Das Produkt hat einen begrenzten Bestand". Dadurch wird die automatische Verfolgung der verbleibenden Mengen aktiviert. Sobald dieses Kästchen markiert ist, erscheint ein Feld, das den **verfügbaren Bestand** anzeigt.



Das System verwaltet:





- Reservierte Bestände** → Produkte in noch nicht bezahlten Warenkörben
- Verkaufte Lagerbestände** → bereits gekaufte Produkte



**Warenkorb-Reservierungszeit**: Wenn ein Kunde ein Produkt in seinen Warenkorb legt, wird es für eine bestimmte Zeit "reserviert". Sie können diese Zeit ändern in: admin > Config > Warenkorb-Reservierung" (Wert in Minuten)



#### Das zu liefernde Produkt?



Markieren Sie "Das Produkt hat eine physische Komponente, die an den Address des Kunden versandt wird". Dies ist nützlich für alle Produkte, die physisch versandt werden (Bücher, T-Shirts usw.)



#### Andere Optionen





- Ticket**: ankreuzen, wenn das Produkt ein Ticket für eine Veranstaltung ist
- Buchung**: prüfen Sie, ob es sich um eine Reservierung handelt (z. B.: Sitzung, Termin)



![product-options](assets/fr/030.webp)



### Aktionseinstellungen (unten)



In diesem Abschnitt wird festgelegt, **wo** und **wie** das Produkt angesehen und gekauft werden kann:



| Plateforme        | Produit visible | Ajoutable au panier |
|-------------------|------------------|----------------------|
| Eshop (site public)        | ✔️              | ✔️                  |
| Retail POS (point de vente)| ✔️              | ✔️                  |
| Google Shopping            | ✔️              | ✔️                  |
| Nostr-bot (vente via bot)  | ✔️              | ✔️                  |

Überprüfen Sie nur die Kanäle, die Sie verwenden möchten.



## Erstellung und Anpassung von CMS-Seiten und Widgets



### Obligatorische CMS-Seiten



Gehen Sie zu `Admin > Merch > CMS`. Sie sehen eine Liste der vorhandenen Seiten und können mit **CMS-Seite hinzufügen** neue Seiten hinzufügen.



CMS-Seiten sind wichtig für:





- Informieren Sie Ihre Besucher (z. B. über die Nutzungsbedingungen)
- Einhaltung von Gesetzen (z. B. Datenschutzbestimmungen)
- Erklären Sie bestimmte Merkmale des Ladens (z. B. IP-Sammlung, 0% Mehrwertsteuer)



Sie können bei Bedarf weitere Seiten hinzufügen:





- Über uns / Wer wir sind
- Unterstützen Sie uns / Spenden
- FAQ
- Kontakt
- usw.



**Tipp: Klicken Sie auf jeden Link oder jedes Symbol, um den **Inhalt**, den **Titel** oder die **Sichtbarkeit** der jeweiligen Seite zu ändern.



### Layout und Grafik Elements



Gehen Sie zu: admin > Merch > Layout". Sie können das visuelle Elements Ihrer Website anpassen:



![product-options](assets/fr/032.webp)



#### Obere Leiste





- Ändern oder Löschen von Links (z.B. HOME, ABOUT US,...)
- Navigation zwischen wichtigen Bereichen der Website



#### Navbar (Hauptnavigationsleiste)





- Im grauen Bereich unterhalb der oberen Leiste vorhanden
- Enthält schnellen Zugang zu: `Konfiguration`, `Zahlungseinstellungen`, `Transaktion`, `Knotenverwaltung`, `Widgets`, etc.
- Nur Direktoren



#### Fußzeile





- Bearbeitbar über `Admin > Merch > Layout`
- Enthält: Kontaktinformationen, nützliche Links, rechtliche Hinweise...



#### Bildmaterial anpassen



Gehe zu: `Admin > Merch > Bilder`



Sie können:





- Ändern Sie das **Hauptlogo**
- Layout ändern oder hinzufügen **Bilder**



#### Beschreibung der Website



Ebenfalls unter "Bilder" änderbar, können Sie je nach Thema eine **Zusammenfassung oder einen Slogan** in der Kopf- oder Fußzeile anzeigen lassen.



**Hinweis:** Damit können Sie das Erscheinungsbild an Ihre Markenidentität (Bildung, Handel oder Gemeinschaft) anpassen.



### Integration von Widgets in CMS-Seiten



Widgets** bereichern Ihre CMS-Seiten mit dynamischen oder visuellen Elements.



#### Widget-Erstellung



Gehen Sie zu: verwaltung > Widgets"



Beispiele für verfügbare Widgets:





- Herausforderungen**: Herausforderungen oder Missionen
- Tags**: Kategorien oder Schlüsselwörter
- Schieberegler**: Bildkarussells
- Spezifikationen**: Tabellen mit Spezifikationen
- Formulare**: Formulare (Kontakt, Feedback, usw.)
- Countdowns**: Zeitschaltuhren
- Galerien**: Bildergalerien
- Bestenlisten**: Benutzer-Ranglisten



![widgets](assets/fr/033.webp)



#### Integration in CMS-Seiten



Verwenden Sie **Shortcodes** im Inhalt Ihrer CMS-Seiten:



| Objectif                 | Balise à insérer                      |
|--------------------------|---------------------------------------|
| Afficher un produit      | `[Product=slug?display=img-1]`        |
| Afficher une image       | `[Picture=slug width=100 height=100 fit=contain]` |
| Intégrer un slider       | `[Slider=slug?autoplay=3000]`         |
| Ajouter un challenge     | `[Challenge=slug]`                    |
| Ajouter un compte à rebours | `[Countdown=slug]`                 |
| Intégrer un formulaire   | `[Form=slug]`                         |

**Aktuelle Parameter**:





- slug": eindeutiger Bezeichner des Widgets
- display=img-1": produktspezifisches Bild
- `Breite`, `Höhe`, `Einpassen`: Bildabmessungen und Stil
- autoplay=3000`: Zeit in ms zwischen zwei Folien



**Vorteile**:





- Einfaches Einfügen (Kopieren und Einfügen)
- Dynamisch: jede Änderung des Widgets wird automatisch übernommen
- Kein Entwickler erforderlich



## Auftragsverwaltung und Berichterstattung



### Auftragsverfolgung



Um frühere Bestellungen einzusehen und zu verwalten, gehen Sie zu: verwaltung > Transaktion > Aufträge"



Hier finden Sie die **vollständige Liste der auf Ihrer Website aufgegebenen Bestellungen**.



![orders](assets/fr/034.webp)



#### Visualisierung und Suche



Mit dem Interface können Sie Aufträge nach verschiedenen Kriterien suchen und filtern:





- bestellnummer: Bestellnummer
- produkt-Alias: Produktidentifikator oder -name
- zahlungsmittel": verwendete Zahlungsmethode (Karte, Krypto usw.)
- e-Mail": E-Mail des Kunden



Diese Filter erleichtern die schnelle Suche und die gezielte Verwaltung.



#### Einzelheiten zu jeder Bestellung



Wenn Sie auf eine Bestellung klicken, können Sie eine vollständige Datei mit:





- Bestellte Produkte
- Informationen für Kunden
- Lieferung Address (falls zutreffend)
- Alle mit der Bestellung verbundenen Notizen



#### Mögliche Aktionen bei einer Bestellung



Sie können:





- Bestellung bestätigen (falls ausstehend)
- Eine Bestellung stornieren (im Falle eines Problems oder einer Kundenanfrage)
- **Etiketten** hinzufügen (für die interne Organisation)
- Abfragen / Hinzufügen **interner Notizen**



**Hinweis:** Dieser Abschnitt ist für eine gute Logistik und gute Kundenbeziehungen unerlässlich.



### Berichterstattung und Export



Zugriff auf Verkaufs- und Zahlungsstatistiken:


administrator > Einstellungen > Berichte



![reporting](assets/fr/035.webp)



Hier finden Sie einen Überblick über Ihr Unternehmen in Form von **Monats- und Jahresberichten**.



#### Inhalt des Berichts



Die Berichte sind in Abschnitte unterteilt:





- Auftragsdetails**: Anzahl der Aufträge, Status (bestätigt, storniert, ausstehend), Entwicklung
- Produktdetail**: verkaufte Produkte, Mengen, beliebte Produkte
- Zahlungsdetails**: eingezogene Beträge, Aufschlüsselung nach Zahlungsmethode



#### Datenexport



Jeder Abschnitt enthält eine Schaltfläche **Export CSV**, mit der Sie:





- Daten im CSV-Format herunterladen
- Öffnen Sie sie in Excel, Google Sheets usw.
- Archivierung für administrative oder buchhalterische Zwecke
- Verwenden Sie sie für interne Berichte



**Hinweis:** ideal für die Leistungsverfolgung, Buchhaltung und Präsentationen.



## Nostr Messaging-Konfiguration (optional)



![nostr-config](assets/fr/036.webp)



Die Plattform unterstützt das **Nostr**-Protokoll für bestimmte erweiterte Funktionen:





- Dezentralisierte Benachrichtigungen
- Anmeldung ohne Passwort
- Interface leichte Verwaltung



### Erzeugen und Hinzufügen des privaten Schlüssels von Nostr



Gehen Sie zu:


verwaltung > Knotenverwaltung > Nostr





- Klicken Sie auf **nsec erstellen**, wenn Sie noch keine haben.
- Das System kann es automatisch generate.
- Alternativ können Sie auch einen vorhandenen Schlüssel (z. B. von Damus oder Amethyst) verwenden.



Nächste:





- Kopieren Sie den "nsec"-Schlüssel
- Fügen Sie es zu Ihrer `.env.local` (oder `.env`) Datei hinzu: ```env NOSTR_PRIVATE_KEY=IhrNsecIciKey



### Mit Nostr aktivierte Funktionen



Einmal konfiguriert, stehen mehrere Funktionen zur Verfügung:



**Benachrichtigungen über Nostr**





- Senden Sie Warnmeldungen für Bestellungen, Zahlungen oder Systemereignisse
- Für Administratoren oder Benutzer



**Interface leichte Verwaltung**





- Zugänglich über einen Nostr-Client
- Ermöglicht schnelle, mobilfreundliche Verwaltung



**Verbindung ohne Passwort**





- Anmeldung über einen sicheren Link (über Nostr gesendet)
- Mehr Sicherheit und Flüssigkeit für den Benutzer



## Design und Themenanpassung



Um das Erscheinungsbild Ihres Shops an Ihre Grafikcharta anzupassen, gehen Sie zu: admin > Merch > Thema"



Hier finden Sie alle Optionen zum **Erstellen** und **Konfigurieren** eines benutzerdefinierten Designs.



### Ein Thema erstellen



![theme](assets/fr/037.webp)



Wenn Sie ein Thema erstellen oder ändern, können Sie:





- Farben**: für Schaltflächen, Hintergründe, Text, Links, usw.
- Schriftarten**: Auswahl an Schriftarten für Titel, Absätze, Menüs
- Grafikstile**: Rahmen, Ränder, Abstände, Blockformen



### Anpassbare Abschnitte



Jeder Teil der Website kann unabhängig eingestellt werden:





- Kopfzeile**: obere Navigationsleiste
- Körper**: Hauptinhalt
- Fußzeile**: unten auf der Seite



**Hinweis:** Diese Granularität gewährleistet die Kohärenz zwischen den visuellen Elementen der Website und der Identität Ihrer Marke.



### Thema Aktivierung



Sobald das Thema konfiguriert ist:





- Klicken Sie auf **Speichern**
- Aktivieren Sie es als das **Hauptthema** des Shops



**Hinweis:** Das aktive Thema ist dasjenige, das für die Besucher sichtbar sein wird.



## Konfigurieren von E-Mail-Vorlagen



Mit der Plattform können Sie die E-Mails, die automatisch an die Benutzer gesendet werden, personalisieren. Gehen Sie zu: `Admin > Einstellungen > Vorlagen`



![emails-templates](assets/fr/038.webp)



### Vorlagen erstellen/bearbeiten



Jede E-Mail (Bestellungsbestätigung, vergessenes Passwort, etc.) hat:





- Betreff**: der Betreff der E-Mail (z. B. "Ihre Bestellung wurde bestätigt")
- HTML-Textkörper**: HTML-Inhalt, der in der E-Mail angezeigt wird



**Hinweis:** Sie können Texte, Bilder, Links usw. nach Bedarf einfügen.



### Verwendung dynamischer Variablen



Um E-Mails dynamisch zu gestalten, fügen Sie Variablen wie:





- `{Bestellnummer}}`: ersetzt durch die aktuelle Bestellnummer
- `{invoiceLink}}`: Link zum Invoice
- `{websiteLink}}`: URL Ihrer Website



**Hinweis:** Diese Tags werden beim Versenden automatisch ersetzt.



### Erweiterte Tipps





- Erstellen Sie E-Mails, die **reaktionsschnell** sind, damit sie auf mobilen Geräten leicht zu lesen sind
- Hinzufügen von **Aktionsschaltflächen** (bezahlen, herunterladen, Bestellung verfolgen)
- Testen Sie Ihre E-Mails, indem Sie sie vor der Veröffentlichung an sich selbst senden



## Konfigurieren bestimmter Tags und Widgets



### Tag-Verwaltung



Tags können zur Strukturierung und Anreicherung Ihrer Inhalte verwendet werden. Um auf sie zuzugreifen: `Admin > Widgets > Tag`



![tags-config](assets/fr/039.webp)



### Erstellen eines Tags



Füllen Sie die folgenden Felder aus:





- Tag-Name**: angezeigter Tag-Name
- Slug**: eindeutiger Bezeichner (keine Leerzeichen oder Akzente)
- Tag-Familie**: gruppiert Tags nach Kategorie



![targsconfig](assets/fr/040.webp)



#### Verfügbare Familien:





- schöpfer": Autoren oder Produzenten
- einzelhändler: Verkaufspersonal oder Verkaufsstellen
- temporal": Zeiträume oder Daten
- ereignisse: zugehörige Ereignisse



### Optionale Felder



Diese Felder können verwendet werden, um ein Tag so anzureichern, als wäre es eine Inhaltsseite:





- Titel
- Untertitel
- Kurzer** Inhalt
- Vollständiger Inhalt** (auf Französisch)
- CTAs** (Aktionsschaltflächen)



### Verwendung von Tags



Tags können sein:





- Den Produkten zugewiesen
- Integriert in CMS-Seiten mit einem Tag: [Tag=slug?display=var-1]



## Konfiguration der herunterladbaren Dateien



Um Ihren Kunden Dokumente zum Herunterladen anzubieten: `Admin > Merch > Files`



### Hinzufügen einer Datei



1. Klicken Sie auf **Neue Datei**


2. Informieren:




   - Dateiname** (z. B. *Installationsanleitung*)
   - Hochzuladende Datei** (PDF, Bild, Word...)



**Hinweis:** Nach dem Hinzufügen erzeugt die Plattform automatisch einen **permanenten Link**.



### Über den Link



Dieser Link kann dann in:





- CMS**-Seite (als Textlink oder Schaltfläche)
- Ein **E-Mail-Client** (über eine Vorlage)
- Ein **Produktblatt** (z. B. Download der Bedienungsanleitung)



Es ist ideal für die Bereitstellung von *Benutzerhandbüchern, technischen Anleitungen, Produktdatenblättern...*, ohne dass ein externes Hosting erforderlich ist.



## Nostr-Bot



Die Plattform bietet eine erweiterte Integration mit dem **Nostr**-Protokoll über einen automatisierten Bot.



Gehen Sie zu: Knoten Management > Nostr



### Hauptmerkmale



#### Relais-Verwaltung





- Hinzufügen oder Entfernen von **Relais**, die vom Bot verwendet werden
- Optimieren Sie die **Reichweite** und **Zuverlässigkeit** der gesendeten Nachrichten



#### Automatische Einführungsmeldung





- Aktivieren Sie eine automatische Nachricht bei der **ersten Benutzerinteraktion**
- Ideal für:
  - Präsentation Ihrer Dienstleistung
  - Senden Sie einen nützlichen Link (z.B. FAQ, Kontakt, Bestellung)



#### Zertifizierung Ihrer `npub





- Fügen Sie ein **Logo** und einen **Öffentlichen Namen** hinzu
- Link zu einer **überprüften Webdomäne**
- Erhöht die Glaubwürdigkeit und den Wiedererkennungswert Ihrer Nostr-Identität



### Nostr-Bot Anwendungsfälle





- Versand von **Bestellbestätigungen** an Sie
- Automatische Reaktion auf **Ereignisse (z. B. neue Bestellung)**
- Schaffung einer **dezentralen Kundeninteraktion**



## Überladen von Übersetzungsbezeichnungen



be-BOP ist mehrsprachig (FR, EN, ES...), aber Sie können die Übersetzungen an Ihre Bedürfnisse anpassen.



Gehen Sie dazu zu: "Einstellungen > Sprache"



### Laden und Bearbeiten



Die Übersetzungsdateien sind in JSON. Sie können:





- Download** Sprachdateien
- Ändern** bestehender Texte
- Hinzufügen** Ihrer eigenen Übersetzungen



Link zu den Originaldateien:


[https://github.com/be-BOP-io-SA/be-BOP/tree/main/src/lib/translations](https://github.com/be-BOP-io-SA/be-BOP/tree/main/src/lib/translations)



**Beispiel:** Ersetzen Sie "In den Warenkorb legen" durch "In den Warenkorb legen" oder "Kaufen".



## Teamarbeit & Verkaufsstellen (POS)



### Verwaltung von Benutzer- und Zugriffsrechten



#### Rollen erstellen



Gehen Sie zu: "Admin > Einstellungen > ARM"



Klicken Sie auf **Rolle erstellen**, um eine Rolle zu erstellen (z.B. `Super Admin`, `POS`, `Ticketchecker`).



Jede Rolle enthält:





- schreibzugriff**: Schreibzugriff
- lesezugriff**: Lesezugriff
- verbotener Zugang**: Abschnitte interdites



#### Erstellung von Benutzern



Fügen Sie im gleichen Menü `Admin > Einstellungen > ARM` einen Benutzer mit:





- anmeldung
- alias
- e-Mail-Wiederherstellung
- (optional) "Wiederherstellung npub" für die Verbindung über Nostr



Eine zuvor definierte Rolle zuweisen.



![pos-users](assets/fr/045.webp)



Benutzer mit Lesezugriff** sehen die Menüs in *kursiv* und können den Inhalt nicht ändern.



## Konfiguration von Verkaufsstellen (POS)



### Zuweisung der Rolle POS



Um einem Benutzer Zugang zum POS zu gewähren, weisen Sie ihm die Rolle "Point of Sale (POS)" in: admin > Konfig > ARM



Er kann sich über die sichere URL verbinden: `/pos` oder `/pos/touch`



### POS-spezifische Merkmale



Be-BOP bietet eine Interface für den physischen Verkauf (Laden, Veranstaltung usw.).



#### Schnelles Hinzufügen über Alias



In `/cart` können Sie über ein Feld ein Produkt hinzufügen:





- Durch Scannen eines **Strichcodes** (ISBN, EAN13)
- Durch manuelle Eingabe eines **Produktalias**



**Hinweis:** Das Produkt wird automatisch in den Warenkorb gelegt.



#### Zahlungsmittel



POS unterstützt:





- Arten
- Kreditkarte
- Lightning Network (Krypto)
- Andere je nach Konfiguration



Es stehen zwei erweiterte Optionen zur Verfügung:





- MwSt.-Befreiung**: gilt für Begründungen (NGOs, Ausländer...)
- Geschenkrabatt**: außergewöhnlicher Rabatt mit obligatorischem Kommentar



#### Client-seitige Anzeige



Die URL "/pos/session" ist für einen **Sekundärbildschirm** (HDMI, Tablet...) bestimmt:



Poster:





- Laufende Produkte
- Gesamtbetrag
- Art der Zahlung
- Angewandte Rabatte



**Hinweis:** Der Kunde verfolgt die Bestellung live, während der Verkäufer sie auf `/pos` erfasst.



### POS-Zusammenfassung



| Fonction                         | Description                                             |
|----------------------------------|---------------------------------------------------------|
| Rôle POS                         | Assigné via ARM                                         |
| Interface principale             | `/pos` ou `/pos/touch`                                 |
| Affichage client (écran 2)       | `/pos/session`                                         |
| Paiement                         | Espèces, carte, Lightning, etc.                         |
| Ajout produit                    | Alias ou scan code-barres                              |
| Remises / TVA                    | Sur justification managériale obligatoire              |


Vielen Dank, dass Sie diese Anleitung aufmerksam verfolgt haben.