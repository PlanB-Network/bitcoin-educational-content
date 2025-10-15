---
name: Alias Vault
description: Leistungsstarkes Tool zur Verwaltung von Passwörtern, Zwei-Faktor-Authentifizierung und Aliasen (mit integriertem E-Mail-Server) - Auch selbst gehostet!
---

![cover](assets/cover.webp)



Datenschutz und Sicherheit im Internet ist ein Thema, dem jeder, unabhängig von seinem Unternehmen, große Aufmerksamkeit schenken sollte.



Diese Fragen sind zudem Teil einer Welt, die sich in ständiger Bewegung befindet: Immer mehr Entwickler beteiligen sich an diesem Thema und bringen Implementierungen für etablierte Lösungen und neue Produkte ein.



Dies ist der Fall bei **Leendert de Borst** und seinem `Alias Vault`, einem revolutionären Tool (dem ersten seiner Art), das es Ihnen ermöglicht, Passwörter zu verwalten und zu speichern, Passwortdatensätze für die Authentifizierung bei Webdiensten zu verwenden, die Zwei-Faktor-Authentifizierung zu verwalten, aber vor allem generate echte _Aliase_, alles in einem einzigen Interface.



**Aber Alias Vault ist damit noch nicht zu Ende**.



## Wesentliche Merkmale



Alias Vault funktioniert in der Cloud auf den Servern des Entwicklers oder selbst gehostet in seiner eigenen Infrastruktur, eine Option, für die Docker-Dateien und -Images zur Installation mit einem Skript verfügbar sind. Zusätzlich zum Web-Interface sind Erweiterungen für alle gängigen Browser sowie mobile Apps für iOS und Android verfügbar; letztere können auch von F-Droid heruntergeladen werden, wodurch der offizielle Google-Store umgangen wird.



In einem Interface ist Alias Vault:




- Frei und quelloffen**
- Password Manager**, um alle komplexen Passwörter zu speichern. Mit der Browser-Erweiterung vervollständigt der Passwort-Manager die Anmeldungen bei Websites
- 2FA**, zur Unterstützung der Zwei-Faktor-Authentifizierung
- Alias-Manager mit integriertem E-Mail-Server**: Alias Vault erstellt keine Aliase, die E-Mails an die Mailbox eines Benutzers weiterleiten, sondern echte Alter-Egos, komplett mit Vorname, Nachname, Geschlecht, Benutzername, Passwort und Geburtstag (falls diese Informationen erforderlich sind).



Eine umfangreiche und gründliche Dokumentation ist Teil des Pakets, die Neulinge bei der Entdeckung dieses leistungsstarken Tools begleitet.



## Keine persönlichen Daten!



Ausgangspunkt ist wie immer die Website [aliasvault.net](aliasvault.net). Wie bereits erwähnt, kann Alias Vault auf dem eigenen Server oder in der Cloud des Entwicklers genutzt werden, um sich mit der Software vertraut zu machen, bevor man zur selbst gehosteten Lösung wechselt.



Die Website hat wirklich auffällige und gut gepflegte Grafiken, aber das Beste kommt erst, wenn man sie in die Hand nimmt: **Erstellen Sie Ihr Konto**.



![img](assets/en/01.webp)



Zu Ihrer großen Überraschung werden Sie feststellen, dass Alias Vault nicht nach persönlichen Daten fragt: Alles, was Sie brauchen, um das Konto zu erstellen, ist ein beliebiger Spitzname, ein Ihnen bekanntes Wort, sofern es verfügbar ist. Stimmen Sie den Nutzungsbedingungen zu, wählen Sie das Wort und fahren Sie fort.



![img](assets/en/02.webp)



Legen Sie jetzt das **"Master-Passwort "** fest, das die wichtigste Information in Ihrem gesamten neuen System ist. Mit diesem einen Passwort werden Sie der Einzige sein, der auf das Konto zugreifen bzw. es wiederherstellen kann, da Ihr "Tresor" auf dem Server, der Ihre Daten beherbergen wird, verschlüsselt bleibt.



![img](assets/en/03.webp)



Tatsache: Sie haben Ihren eigenen Passwort- und Alias-Manager erstellt, ohne jedoch Ihre eigene funktionierende, private E-Mail Address anzugeben.



![img](assets/en/04.webp)



Alias Vault heißt Sie in einem sicheren, neuen, persönlichen, aber auch leeren Raum willkommen. Und jetzt beginnen wir, ihn ein wenig zu bevölkern.



Wenn Sie bereits einen Passwort-Manager haben, können Sie die Datei aus dem von Ihnen verwendeten importieren, um die Unterschiede zu anderen Anbietern zu bewerten, oder vielleicht den Alias-Manager entfernen, damit Sie alles in einer Anwendung verwalten können.



![img](assets/en/05.webp)



Alias Vault ist extrem einfach: Sie haben eine Hauptseite, die "Home" heißt, mit zwei Menüs:




- berechtigungsnachweise": damit können Sie Identitäten und Aliase erstellen und verwalten
- e-Mail": ein Posteingang, in dem Sie eingehende Nachrichten auf von Ihnen erstellte Aliase überprüfen können.



![img](assets/en/06.webp)



Wir wollen einen ersten "Alias" erstellen, also gehen Sie oben rechts auf der Seite und klicken Sie auf _+Neuer Alias_.



![img](assets/en/07.webp)



Zunächst sieht das Menü minimalistisch aus, wie es der Philosophie von Alias Vault entspricht. Um die Funktionen dieser Funktion zu entdecken, klicken Sie auf _Erstellen im erweiterten Modus_.



![img](assets/en/08.webp)



Im oberen Teil des ersten Bildschirms können Sie Kennwörter importieren, die Sie bereits für Dienste verwenden, die Sie abonniert haben, oder die Sie häufig online nutzen.



Wenn Sie die Zwei-Faktor-Authentifizierung für einen (oder alle) der oben genannten Dienste aktiviert haben, können Sie mit Alias Vault auch diesen zusätzlichen Layer der Sicherheit verwalten, indem Sie den "geheimen Schlüssel" importieren. Alias Vault erstellt den für den Zugriff erforderlichen "TOTP".



![img](assets/en/09.webp)



**Achtung**: In dem für die E-Mail Address reservierten Feld schlägt Alias Vault standardmäßig seine eigene Domäne vor; um die korrekte Address zu verwenden, mit der Sie zuvor Konten erstellt haben, klicken Sie auf _Benutzerdefinierte Domäne eingeben_, damit Sie die korrekte Domäne nach `@` eingeben können.



![img](assets/en/14.webp)



Der untere Teil dieses Bildschirms macht am meisten Spaß. Klicken Sie auf _Zufälligen Alias generieren_ und Alias Vault erstellt für Sie getrennte Identitäten für verschiedene Bedürfnisse, jede mit einem eigenen Postfach, sehr robusten Level-Passwörtern, ergänzt durch andere Details wie Geschlecht, Geburtsdatum und einen passenden Spitznamen.



![img](assets/en/10.webp)



Über ein entsprechendes Menü können Sie die Einstellungen ändern, die sich auf die Kennworterstellung auswirken, z. B. nur Kleinbuchstaben auswählen und mehrdeutige Zeichen ausschließen.



![img](assets/en/11.webp)



Sie können die von Alias Vault vorgeschlagene Alias-E-Mail verwenden oder die Domänen ändern, indem Sie auf das entsprechende Dropdown-Menü klicken.



![img](assets/en/12.webp)



Bevor Sie diese E-Mail für einen Anmeldedienst verwenden, können Sie die Funktionalität testen, indem Sie eine Nachricht von einem eigenen Address an das neu erstellte Postfach senden.



![img](assets/en/13.webp)



**⚠️ WARNUNG**: Der Empfang von E-Mails ist dank des in Alias Vault eingebauten Servers möglich, aber dieser erlaubt nur den Empfang von E-Mails, nicht aber deren Beantwortung oder die Nutzung des E-Mail-Postfachs mit den "herkömmlichen" Funktionen eines "Alias"-Dienstes. Damit unterscheidet sich Alias Vault stark von Simple Login, Addy und anderen Plattformen, die ausschließlich für diese Art von Diensten bestimmt sind. Für das Beispiel von Simple Login können Sie sich das entsprechende Tutorial ansehen:



https://planb.network/tutorials/computer-security/communication/simple-login-c17a10d6-8f84-4f97-8d50-7a83428d0f41

Um einen Alias zu löschen, den Sie zu Testzwecken erstellt haben, müssen Sie sich nur bei "Home" anmelden, dann "Anmeldeinformationen" wählen und auf die Identität klicken, die Sie löschen möchten. Der Befehl _Löschen_ wird in der oberen rechten Ecke angezeigt, damit Sie fortfahren können.



![img](assets/en/16.webp)



## Browser-Erweiterung



Je nach Bedarf können Sie auf eine Browsererweiterung zurückgreifen, die in den gängigsten Browsern zu finden ist.



![img](assets/en/15.webp)



Die Installation erfolgt wie bei allen anderen Erweiterungen auch, so dass ich auf dieses Detail nicht näher eingehen werde.



Die Browsererweiterung dient dazu, die Anmeldung bei Online-Diensten zu erleichtern oder bei Bedarf neue Aliasnamen zu erstellen: Wenn der Dienst in Ihren Alias Vault-Datensätzen gespeichert ist, übernimmt die automatische Ausfüllung die erforderlichen Aufgaben.



![img](assets/en/17.webp)



Die einzige Vorsichtsmaßnahme besteht darin, zu überprüfen, ob Alias Vault aktiv ist. Die Anwendung verfügt nämlich über eine Standardeinstellung, bei der sie nach einer gewissen Zeit der Inaktivität pausiert. Dies ist eine sehr nützliche Funktion, **wenn Sie sich z. B. von Ihrem Computer entfernen müssen, um zu verhindern, dass jemand anderes auf Ihre Konten zugreift**. Ein vereinfachtes Verfahren ermöglicht es Ihnen, sich erneut anzumelden, indem Sie das "Hauptkennwort" eingeben, wenn die vorherige Sitzung noch im Cache gespeichert ist. Die Zeit für die Abmeldung ist einer der Parameter, die Sie anpassen können, indem Sie sie je nach Ihren Wünschen verkürzen oder verlängern.



## Mobile App



Wie alle seriösen Apps dieser Art gibt es auch von Alias Vault eine Version für mobile Geräte, sowohl für Android als auch für iOS. Für Android können Sie die App von [F-Droid](https://f-droid.org/packages/net.aliasvault.app/) herunterladen.



Zum Zeitpunkt der Erstellung dieses Artikels (Ende August 2025) betrachtet die mobile App das "automatische Ausfüllen" als eine experimentelle Funktion, die nur bei sehr wenigen Websites funktioniert. Bis sie vollständig implementiert ist, muss man bei der Verwendung von Alias Vault auf dem Handy Daten kopieren und einfügen.



Sobald Sie die App aus dem Store heruntergeladen haben, geben Sie zur Anmeldung einfach den Benutzer und das "Master-Passwort" ein, die Sie in der Web-App erstellt haben.



![img](assets/en/18.webp)



Wenn Sie Ihren "Tresor" öffnen, werden Sie gefragt, ob Sie den biometrisch kontrollierten Zugang aktivieren möchten. Dies ist eine zusätzliche Sicherheitsstufe, die verhindert, dass jemand anderes auf Ihre Passwörter zugreifen kann, wenn er Ihr Telefon in der Hand hält.



![img](assets/en/19.webp)



Wenn Sie sich entscheiden, die biometrische Prüfung einzurichten, fahren Sie fort. Wenn Sie den Schritt überspringen und es sich anders überlegen, können Sie ihn auch später über das Menü _Einstellungen_ konfigurieren.



Sobald Sie sich eingeloggt haben, werden die von Ihnen bereits angelegten Daten wieder synchronisiert.



![img](assets/en/20.webp)



Die mobile App kann auf den Link zu dem auf dem eigenen Server gehosteten "Tresor" weitergeleitet werden.



![img](assets/en/22.webp)



Und genau diese selbstgehostete Version werden wir im nächsten Abschnitt kurz Address vorstellen.



## Self-Hosting: volle Kontrolle über Ihre Daten



Alias Vault ist, um fair zu sein, nicht der erste Passwort-Manager, der es Ihnen ermöglicht, den Dienst in Ihrer Infrastruktur einzusetzen. Es gibt andere, aber einige haben entweder Einschränkungen oder sind teilweise Closed Source.



Die Gelegenheit ist einzigartig: **Beenden Sie die Abhängigkeit von externen Dienstleistern oder Clouds, sondern nutzen Sie Ihren eigenen lokalen Server, um die damit verbundenen Passwörter, Aliase und äußerst sensiblen Informationen zu schützen und zu verwalten**. Mit Alias Vault können Sie den E-Mail-Dienst auch auf Ihren eigenen E-Mail-Server verweisen lassen, um die Vertraulichkeit zu erhöhen.



Es ist an der Zeit, sich an [Dokumentation] (https://docs.aliasvault.net/installation/) zu wenden, um herauszufinden, wie man Alias Vault selbst hosten kann.



![img](assets/en/23.webp)



Alias Vault läuft auf Docker Compose, so dass nur minimale Erfahrung mit Linux und Docker erforderlich ist. Sie können mit der Basisinstallation beginnen und dann mit fortgeschritteneren Lösungen vervollständigen.



Ihr Server muss auf einem 64-Bit-Rechner mit einer Linux-Distribution, 1 GB RAM und mindestens 16 GB Speicherplatz laufen; die Version von Docker (CE) muss mindestens 20.10 oder höher sein, während Docker Compose eine Version ab 2.0 erfordert.



Ich beschloss, Alias Vault mit einem Thin Client auszuprobieren, auf dem DietPi als Distribution installiert ist, eine Debian Bookworm-Basis, die auf das Wesentliche optimiert ist und auf der bereits `Docker` und `Docker Compose` laufen.



Um etwas Ordnung zu schaffen, erstellen Sie zunächst ein Verzeichnis in Ihrem Zuhause, öffnen Sie das `Terminal` und fügen Sie den Befehl zum Ausführen des Installationsskripts ein.



```bash
curl -L -o install.sh https://github.com/lanedirt/AliasVault/releases/latest/download/install.sh
```



![img](assets/en/24.webp)



![img](assets/en/25.webp)



Wenn die Installation abgeschlossen ist, finden Sie Ihre Zugangsdaten:


```
Admin Panel: https://localhost/admin
Username: admin
Password: yyy0xyx1yxy2zxx4
```



Überprüfen Sie den Inhalt des Verzeichnisses nach der Installation.



![img](assets/en/29.webp)



Um Alias Vault zu starten, verwenden Sie den Befehl:



```` Launch-Alias-Gewölbe


./install.sh starten


```

Alias Vault adesso gira sul tuo server personale.

![img](assets/en/30.webp)

Apri un browser e digita l'url: ti comparirà la pagina per fare login come `Admin` di Alias Vault.

![img](assets/en/26.webp)

Il più è fatto! Hai davanti a te il pannello per amministrare Alias Vault in maniera personalizzata.

![img](assets/en/27.webp)

Da questa interfaccia, potrai controllare quanti e quali utenti stanno utilizzando il servizio, limitarne l'uso, cancellare gli utenti (azione irreversibile) e soprattutto controllare tutti i `log`.

Se si tratta di una nuova installazione, non avrai altri utenti oltre ad `admin`; per crearne di nuovi, apri un'altra `tab` del browser e digita:

```


localhost/user/start


```

![img](assets/en/28.webp)

Da qui in poi, tutto procede come abbiamo visto in precedenza nella guida, con la differenza che adesso stai usando Alias Vault sul tuo server. Se la tua macchina è adeguatamente configurata e protetta, questo è un modo elegante e sicuro di gestire un tuo password e alias manager, senza servizi di terze parti.

Per fermare Alias Vault, torna al terminale e digita:

``` Stop-Alias-Vault
./install.sh stop

```



![img](assets/en/31.webp)



## Überlegungen zu Verschlüsselung und Sicherheit



![img](assets/en/32.webp)



Laut den Angaben von Lanedirt auf der Website, in der Dokumentation und auf Github bleiben mit Alias Vault **alle Informationen (Komponenten), die Sie auf Alias Vault ablegen, fest an das Gerät gebunden, verschlüsselt und unzugänglich für jeden, der das "Master-Passwort" nicht kennt**.



Das "Master-Passwort" ist somit das grundlegende Element des gesamten "Tresors". Nach seiner Eingabe wird es mit dem "Argon2id"-Algorithmus verarbeitet, einer Hard-Speicher-Schlüsselableitungsfunktion, um zu verhindern, dass das Geheimnis das Gerät verlässt.



Selbst für den Verwalter der Cloud oder des Hosting-Dienstes bleibt alles verborgen. Über das Admin-Panel haben Sie keinen Zugriff auf die Benutzerdaten, Sie können nur feststellen, ob sie Aliase erstellt und E-Mails erhalten haben, und sonst nichts.



Alle gespeicherten Inhalte werden mit kryptografischen Schlüsseln ver- und entschlüsselt, die aus dem "Master-Passwort" abgeleitet werden. **Nur verschlüsselte Daten werden auf dem Server gespeichert, nichts erscheint im Klartext**. Wenn ein Benutzer sein "Hauptkennwort" vergisst oder verliert, geht das damit verbundene Konto unwiderruflich verloren, da der Server keinen Zugriff auf die Klartextinhalte hat.



Für die selbst gehostete Version gibt es das Skript zum Zurücksetzen des "Master-Passworts", das jedoch keinen Datenverlust verhindert.



![img](assets/en/33.webp)



Da sich Alias Vault in der _Beta-Phase_ befindet, kann es zu Schwierigkeiten beim Zugriff kommen, wenn Sie das Hauptkennwort ändern/aktualisieren. Ich schlage vor, dass Sie es von Anfang an robust und komplex wählen, damit Sie den Dienst ausprobieren und schließlich entscheiden können, ob Sie ihn nutzen möchten. Wenn Sie nach der Passwortaktualisierung Schwierigkeiten beim Zugriff auf die Cloud haben, wenden Sie sich bitte an den Alias Vault-Support.



Für ein vollständiges Verständnis der Architektur und der Sicherheit von Alias Vault empfehle ich Ihnen dringend, [diese Seite] (https://docs.aliasvault.net/architecture/) zu konsultieren, die Details zur Kryptographie enthält, die dem Betrieb zugrunde liegt.



## Straßenkarte


Die Entwickler haben die Absicht, Alias Vault bis Ende 2025 ausgereift und stabil zu machen, um seine zukünftigen Nutzungsmerkmale zu definieren.



Alias Vault ist und bleibt quelloffen und kostenlos, aber wahrscheinlich nicht unbegrenzt wie in der Betaphase. Einige kostenpflichtige Funktionen werden derzeit implementiert, da sie bereits angekündigt wurden.



Es gibt Team-/Familienpläne und Unterstützung für Hardware-Schlüssel, letztere für die Authentifizierung mit FIDO2 oder WebAuth.



## Wer braucht Alias Vault



**Ein Tool wie dieses ist ideal für alle, denen die Privatsphäre im Internet wichtig ist.



Ihre Identität ist höchstwahrscheinlich das Herzstück Ihrer Online-Geschäfte und muss mit allen Mitteln geschützt werden, um **diese** Daten von Diensten, Unternehmen und Brokern fernzuhalten, die alles tun, um Ihr Online-Verhalten in die Finger zu bekommen.



Alias Vault gibt Ihnen die vollständige Kontrolle über Ihre Anmeldedaten zurück, so dass Sie sich nicht mehr auf Dritte verlassen müssen, um Ihre sensiblen Daten zu schützen und zu verschlüsseln, oder sogar ganz darauf verzichten können.



Die Architektur und die kryptografischen Möglichkeiten von Alias Vault sind ideal für souveräne Einzelpersonen, kleine und mittlere Unternehmen, Entwicklungsteams und alle Liebhaber von **Open-Source**-Anwendungen. Wenn Sie in eine dieser Kategorien fallen: viel Spaß beim Entdecken von Alias Vault.