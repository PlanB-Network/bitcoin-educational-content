---
name: Samourai Wallet - Wiederherstellung
description: Wie kann man auf Samourai Wallet feststeckende Bitcoins wiederherstellen?
---
![cover](assets/cover.webp)

Nach der Verhaftung der Gründer von Samourai Wallet und der Beschlagnahmung ihrer Server am 24. April sind einige Funktionen der Anwendung nun inoperativ, und Benutzer, die keinen eigenen Dojo besitzen, können keine Transaktionen mehr senden.

Nachdem ich in den letzten Tagen mehreren Benutzern bei der Wiederherstellung ihrer Bitcoins geholfen habe, glaube ich, auf die meisten Probleme gestoßen zu sein, die während der Wiederherstellung eines Samourai Wallets auftreten können. Daher wird dieses Tutorial mit einem Lagebericht beginnen, um die Funktionen zu identifizieren, die innerhalb des Samourai Wallet-Ökosystems und der von diesem Vorfall betroffenen Software noch betriebsfähig sind und welche nicht mehr zur Verfügung stehen. Anschließend werden wir Schritt für Schritt vorgehen, um ein Samourai Wallet mit der Sparrow Wallet-Software wiederherzustellen. Wir werden alle potenziellen Hindernisse untersuchen, die während dieses Prozesses auftreten können, und Lösungen zur Behebung dieser sehen. Schließlich werden Sie im letzten Teil die potenziellen Risiken für Ihre Privatsphäre nach der Beschlagnahmung der Server entdecken.

*Ein großes Dankeschön an [@Louferlou](https://twitter.com/Louferlou), der mehreren Benutzern bei ihrer Wiederherstellung geholfen und seine Erfahrungen mit mir geteilt hat und der auch Tests durchgeführt hat, um festzustellen, was noch funktioniert.*

## Funktioniert Samourai Wallet noch?

Ja, **die Samourai Wallet-App funktioniert noch**, aber unter bestimmten Bedingungen.

Zunächst ist es notwendig, dass die App zuvor auf Ihrem Smartphone installiert wurde. Der Google Play Store hat die App entfernt, und die APK wurde auf der beschlagnahmten Website gehostet. Daher ist es momentan kompliziert, Samourai zu installieren. Sie könnten APKs online finden, aber ich rate davon ab, sie herunterzuladen, es sei denn, Sie sind sich der Quelle sicher.

Da die Samourai Wallet-Seite nicht mehr im Google Play Store verfügbar ist, ist es nicht möglich, automatische Updates zu deaktivieren. Wenn die App zu den Download-Plattformen zurückkehrt, wäre es klug, **automatische Updates zu deaktivieren**, bis mehr Informationen über die Entwicklung des Falls verfügbar sind.

Wenn Samourai Wallet bereits auf Ihrem Smartphone installiert ist, sollten Sie immer noch in der Lage sein, auf die App zuzugreifen. Um die Wallet-Funktionalität von Samourai zu nutzen, ist es wesentlich, einen Dojo anzuschließen. Früher waren Benutzer ohne einen persönlichen Dojo auf Samourais Server angewiesen, um auf Bitcoin-Blockchain-Informationen zuzugreifen und Transaktionen zu senden. Mit der Beschlagnahmung dieser Server kann die App nicht mehr auf diese Daten zugreifen.
Wenn Sie vorher keinen angeschlossenen Dojo hatten, aber jetzt einen haben, können Sie ihn einrichten, um Ihre Samourai-App wieder zu verwenden. Dies beinhaltet das Überprüfen Ihrer Backups, das Löschen der Wallet (die Wallet, nicht die Anwendung) und die Wiederherstellung der Wallet, indem Sie Ihren Dojo mit der Anwendung verbinden. Für weitere Details zu diesen Schritten können Sie [dieses Tutorial im Abschnitt "_Vorbereitung Ihrer Samourai Wallet_" : COINJOIN - DOJO](https://planb.network/de/tutorials/privacy/coinjoin-dojo) konsultieren.
Wenn Ihre Samourai-App bereits mit Ihrem eigenen Dojo verbunden war, dann funktioniert der Wallet-Teil perfekt für Sie. Sie können immer noch Ihr Guthaben sehen und Transaktionen senden. Trotz allem, was passiert, denke ich, dass Samourai Wallet derzeit die beste mobile Wallet-Software ist. Persönlich plane ich, sie weiterhin zu verwenden.
Das Hauptproblem, auf das Sie stoßen könnten, ist die Unzugänglichkeit von Whirlpool-Konten über die App. Normalerweise versucht Samourai, eine Verbindung mit Ihrem Whirlpool CLI herzustellen und die CoinJoin-Zyklen zu starten, bevor Sie Zugang zu diesen Konten erhalten. Da diese Verbindung jedoch nicht mehr möglich ist, sucht die App unendlich weiter, ohne Ihnen jemals Zugang zu den Whirlpool-Konten zu gewähren. In diesem Fall können Sie diese Konten auf einer anderen Wallet-Software wiederherstellen, während Sie das Einzahlungskonto nur bei Samourai behalten.
### Welche Werkzeuge sind auf Samourai noch verfügbar?

Andererseits sind einige Werkzeuge entweder durch die Serverabschaltung betroffen oder vollständig nicht verfügbar.

Bezüglich der individuellen Ausgabewerkzeuge funktioniert alles normal, vorausgesetzt natürlich, dass Sie Ihr eigenes Dojo haben. Normale Stonewall-Transaktionen (und nicht Stonewall x2) funktionieren ohne Probleme.

Kommentare auf Twitter haben hervorgehoben, dass die durch eine Stonewall-Transaktion gebotene Privatsphäre jetzt reduziert sein könnte. Der Mehrwert einer Stonewall-Transaktion liegt in der Tatsache, dass sie strukturell von einer Stonewall x2-Transaktion nicht zu unterscheiden ist. Wenn ein Analyst auf dieses spezifische Muster stößt, kann er nicht bestimmen, ob es sich um eine Standard-Stonewall mit einem einzelnen Benutzer oder eine Stonewall x2 mit zwei Benutzern handelt. Wie wir jedoch in den folgenden Absätzen sehen werden, ist die Durchführung von Stonewall x2-Transaktionen aufgrund der Nichtverfügbarkeit von Soroban komplexer geworden. Einige denken daher, dass ein Analyst jetzt annehmen könnte, dass jede Transaktion mit dieser Struktur eine normale Stonewall ist. Persönlich teile ich diese Annahme nicht. Obwohl Stonewall x2-Transaktionen möglicherweise weniger häufig sind (und ich denke, sie waren es bereits vor diesem Vorfall), kann die Tatsache, dass sie immer noch möglich sind, eine gesamte Analyse basierend auf der Annahme, dass sie es nicht sind, ungültig machen.
**[-> Erfahren Sie mehr über Stonewall-Transaktionen.](https://planb.network/tutorials/privacy/on-chain/stonewall-033daa45-d42c-40e1-9511-cea89751c3d4)**
Bezüglich Ricochet konnte ich nicht überprüfen, ob der Dienst noch betriebsbereit ist, da ich kein Dojo im Testnet besitze, und ich möchte es vermeiden, `100 000 Sats` an eine Wallet zu senden, die von den Behörden kontrolliert werden könnte. Wenn Sie kürzlich die Gelegenheit hatten, dieses Werkzeug zu testen, lade ich Sie ein, mich zu kontaktieren, damit wir diesen Artikel aktualisieren können.

Wenn Sie Ricochet verwenden müssen, beachten Sie, dass Sie diese Operation immer manuell mit jeder Wallet-Software durchführen können. Um zu lernen, wie man die verschiedenen Sprünge richtig manuell durchführt, empfehle ich, diesen anderen Artikel zu konsultieren: [**RICOCHET**](https://planb.network/tutorials/privacy/on-chain/ricochet-e0bb1afe-becd-44a6-a940-88a463756589).

Das JoinBot-Werkzeug ist nicht mehr betriebsbereit, da es vollständig von der Teilnahme einer von Samourai verwalteten Wallet abhängig war.

Bezüglich anderer Arten von kollaborativen Transaktionen, oft als "Cahoots" bezeichnet, bleiben sie möglich, aber nur manuell. Vor der Serverabschaltung hatten Sie zwei Optionen für die Durchführung von Stonewall x2- oder Stowaway (PayJoin)-Transaktionen:
- Verwenden Sie das Soroban-Netzwerk, um die PSBTs automatisch und remote auszutauschen;
- Oder führen Sie diese Austausche manuell durch, indem Sie mehrere QR-Codes scannen.

Nach mehreren Tests scheint es, dass Soroban nicht mehr funktioniert. Um diese kollaborativen Transaktionen durchzuführen, muss der Datenaustausch daher manuell erfolgen. Hier sind zwei Optionen für diesen Austausch:
- Wenn Sie physisch nahe bei Ihrem Kollaborateur sind, können Sie die QR-Codes nacheinander scannen;
- Wenn Sie von Ihrem Mitarbeiter entfernt sind, können Sie die PSBTs über einen externen Kommunikationskanal zur Anwendung austauschen. Seien Sie jedoch vorsichtig, da die Daten in diesen PSBTs in Bezug auf die Privatsphäre sensibel sind. Ich empfehle die Verwendung eines verschlüsselten Nachrichtendienstes, um die Vertraulichkeit des Austauschs zu gewährleisten.
**[-> Erfahren Sie mehr über Stonewall x2 Transaktionen.](https://planb.network/tutorials/privacy/on-chain/stonewall-033daa45-d42c-40e1-9511-cea89751c3d4-x2)**

**[-> Erfahren Sie mehr über Stowaway Transaktionen.](https://planb.network/tutorials/privacy/on-chain/payjoin-samourai-wallet-48a5c711-ee3d-44db-b812-c55913080eab)**

Was Whirlpool betrifft, so scheint das Protokoll nicht mehr zu funktionieren, selbst für Benutzer, die ihren eigenen Dojo haben. Ich habe in den letzten Tagen mein RoninDojo überwacht und einige grundlegende Manipulationen versucht, aber das Whirlpool CLI konnte seit der Serverabschaltung nicht mehr verbinden.

Dennoch bleibe ich hoffnungsvoll, dass dieses Protokoll reaktiviert oder vielleicht in den kommenden Wochen anders neu gedacht werden kann, je nachdem, wie sich die Situation entwickelt. Diese Pause könnte eine Gelegenheit sein, neue Ansätze oder potenzielle Verbesserungen an diesem System zu erkunden.
### Welche externen Tools sind noch verfügbar?
Bezüglich anderer Tools, die mit der Samourai-Umgebung verbunden sind, sind einige noch verfügbar, während andere es nicht sind.

Die kostenlose Chain-Analyse-Website OXT.me ist leider vorerst nicht mehr verfügbar.

Das Whirlpool Stats Tool ist nicht mehr zum Download verfügbar, da es auf Samourais GitLab gehostet wurde. Selbst wenn Sie dieses Python-Tool zuvor lokal auf Ihrem Rechner heruntergeladen oder es auf Ihrem RoninDojo-Knoten installiert hatten, wird WST vorerst nicht funktionieren. Tatsächlich hing es von Daten ab, die von OXT.me für seinen Betrieb bereitgestellt wurden, und diese Seite ist nicht mehr zugänglich. Derzeit ist WST nicht besonders nützlich, da das Whirlpool-Protokoll inaktiv ist.

Die Website KYCP.org ist derzeit ebenfalls nicht mehr zugänglich.

Das GitLab, das den Code für das Boltzmann Calculator Python-Tool gehostet hat, wurde ebenfalls beschlagnahmt. Derzeit ist es daher nicht mehr möglich, dieses Tool herunterzuladen. Aber wenn Sie ein RoninDojo haben, können Sie den Boltzmann Calculator weiterhin wie zuvor verwenden.

Was RoninDojo betrifft, so funktioniert diese Node-in-Box-Software trotz der Nichtverfügbarkeit bestimmter spezifischer Tools wie Whirlpool CLI und WST weiterhin korrekt. Sie kann immer noch für andere Wallet-Software dank Fulcrum oder Electrs verwendet werden. Wenn Sie mehr Informationen über RoninDojo erhalten möchten oder spezifische Fragen haben, ermutige ich Sie, [ihrer Telegram-Gruppe beizutreten](https://t.me/RoninDojoNode).

Der Quellcode für RoninDojo ist jedoch derzeit ebenfalls nicht zugänglich, da er auf Samourais GitLab gehostet wurde. Es ist daher momentan nicht möglich, ihn manuell auf einem Raspberry Pi zu installieren.

Was die Watch-Only-Wallet-Software Sentinel betrifft, so ist die Situation ähnlich wie bei der Samourai-App. Wenn Sie Ihren eigenen Dojo haben, können Sie Sentinel ohne Probleme weiter verwenden. Wenn Sie jedoch keinen Dojo haben, werden Sie keine Verbindung herstellen können. Im Gegensatz zu Samourai ist die Sentinel-Website noch online zugänglich. Aber seien Sie vorsichtig mit dieser Seite und der dort angebotenen APK, da unklar ist, wer derzeit diese Ressourcen kontrolliert.

### Ist Sparrow Wallet betroffen?
Sparrow Wallet funktioniert weiterhin normal, mit Ausnahme der Samourai-Tools, die nicht mehr verfügbar sind. Derzeit ist es nicht mehr möglich, CoinJoins über Sparrow durchzuführen. Ebenso sind Tools für gemeinschaftliche Ausgaben nicht mehr zugänglich, da Sparrow nicht die Option des manuellen Austauschs von PSBTs bietet, im Gegensatz zu Samourai. Für alle anderen Funktionalitäten funktioniert Sparrow ohne Probleme. Sie können diese Software auch verwenden, um bei Bedarf ein Samourai-Wallet wiederherzustellen.

## Wie stellt man ein Samourai-Wallet wieder her?
Wie wir in den vorherigen Abschnitten gesehen haben, ist es, wenn Sie Ihr eigenes Dojo besitzen, nicht unbedingt erforderlich, die Software zu wechseln. **Samourai bleibt eine ausgezeichnete Wahl für ein Hot Wallet** für Ihre täglichen Ausgaben. Wenn Sie jedoch kein Dojo haben oder sich für eine andere Software entscheiden möchten, erkläre ich den vollständigen Wiederherstellungsprozess und gehe auf mögliche Hindernisse ein, die Sie dabei antreffen könnten.

In jedem Fall ist es wichtig, sich Zeit zu nehmen und darauf zu achten, keine Fehler zu machen. Denken Sie daran, es eilt nicht, da Sie Ihre privaten Schlüssel besitzen und die Beschlagnahmung der Server von Samourai dies in keiner Weise beeinflusst. Was auch immer passiert, offensichtlich können sie nicht auf Ihre privaten Schlüssel zugreifen.

### Überprüfen Sie die Passphrase

Um Ihr Wallet wiederherzustellen, müssen Sie Ihre Passphrase haben, auch wenn Sie sich für die Wiederherstellung über die Backup-Datei entscheiden. Beginnen Sie damit, die Gültigkeit dieser Passphrase zu überprüfen. Öffnen Sie Ihre Samourai Wallet-App, klicken Sie oben links auf Ihr Paynym-Symbol und dann auf `Einstellungen`.

![samourai](assets/1.webp)

Klicken Sie als Nächstes auf `Fehlerbehebung` und dann auf `Passphrase/Backup-Test`.

![samourai](assets/2.webp)

Geben Sie Ihre Passphrase ein und klicken Sie auf `Ok`. Wenn sie korrekt ist, wird Samourai dies bestätigen. Sie haben auch die Möglichkeit, die Backup-Datei zu überprüfen, falls Sie diese später verwenden möchten.

![samourai](assets/3.webp)

Dieser Schritt ist optional, aber empfohlen. Er bestätigt, dass die Passphrase korrekt ist und eliminiert eine potenzielle Fehlerquelle für später. Wenn Samourai an dieser Stelle angibt, dass die Passphrase falsch ist, wird eine Wiederherstellung nicht möglich sein. Stellen Sie sicher, dass Sie die Passphrase korrekt eingegeben haben und überprüfen Sie sie erneut.

### Option 1: Das Wallet mit der Backup-Datei auf Sparrow wiederherstellen

Seit Version 1.8.6 von Sparrow Wallet ist es möglich, Ihr Samourai-Wallet direkt mit der Backup-Textdatei namens `samourai.txt`, die Ihre Anwendung automatisch generiert, zu importieren. Diese Datei enthält alle notwendigen Informationen zur Wiederherstellung Ihres Wallets und ist aus Sicherheitsgründen mit Ihrer Passphrase verschlüsselt.

Wenn Sie diese Option wählen, benötigen Sie Ihre aktuelle `samourai.txt`-Datei und Ihre Passphrase. Um diese Datei auf Samourai Wallet zu generieren, klicken Sie auf die drei kleinen Punkte oben rechts und wählen Sie dann `Export wallet backup`.

![samourai](assets/4.webp)
Wählen Sie anschließend `Export to Clipboard`. Danach müssen Sie diese Datei sicher auf Ihren PC übertragen. Da die Datei verschlüsselt ist, aber die Passphrase allein ausreicht, um sie zu entschlüsseln, ist es wichtig, während der Übertragung Vorsichtsmaßnahmen zu treffen. Wenn Sie sich für eine direkte Übertragung als Klartext entscheiden, müssen Sie auf Ihrem PC eine `samourai.txt`-Datei erstellen und den Inhalt der Zwischenablage hineinkopieren. Eine Alternative wäre, die `samourai.txt`-Datei direkt aus den auf Ihrem Telefon gespeicherten Dateien abzurufen.
Sobald Sie Zugriff auf die Datei auf Ihrem PC haben, öffnen Sie Sparrow Wallet, klicken Sie auf den Tab `Datei` und wählen Sie `Import Wallet`, um den Import Ihres Wallets zu starten.

![samourai](assets/5.webp)
Scrollen Sie nach unten zu `Samourai Backup`, klicken Sie auf `Import File` und wählen Sie dann Ihre `samourai.txt` Datei aus.
![samourai](assets/6.webp)

Sparrow wird Sie dann nach einem Passwort fragen, um die Datei zu entschlüsseln. Dieses Passwort ist tatsächlich Ihre Passphrase. Geben Sie es in das entsprechende Feld ein und klicken Sie auf `Import`.

![samourai](assets/7.webp)

Wenn in diesem Stadium Ihre Wallet nicht erscheint, ist es möglich, dass Sie einen Fehler beim Kopieren der `samourai.txt` Datei oder beim Eingeben der Passphrase gemacht haben. Sie können den Abschnitt zur Fehlerbehebung konsultieren, um weitere Hilfe zu erhalten.

![samourai](assets/8.webp)

Bezüglich des Skripttyps, wenn Sie in Samourai keine anderen Skripte konfiguriert haben, sollten Sie normalerweise nur SegWit V0 (Native SegWit / P2WPKH) verwenden. Behalten Sie dieses Standardskript bei und klicken Sie auf `Import`.

![samourai](assets/9.webp)

Benennen Sie Ihre Wallet, zum Beispiel "Samourai Recovery", und klicken Sie dann auf `Create Wallet`.

![samourai](assets/10.webp)

Sparrow wird Sie dann bitten, ein Passwort zu wählen. Dieses Passwort schützt nur den Zugang zu Ihrer Wallet auf diesem PC und bezieht sich nicht auf die Ableitung der Schlüssel Ihrer Wallet. Wählen Sie sicherheitshalber ein starkes Passwort, notieren Sie es, um es sich zu merken, und klicken Sie auf `Set Password`.

![samourai](assets/11.webp)

Sparrow wird dann die Schlüssel Ihrer Wallet ableiten und nach den entsprechenden Transaktionen suchen.

![samourai](assets/12.webp)

Vorerst ist nur Ihr Einzahlungskonto zugänglich. Wenn Sie Samourai nur für dieses Konto verwendet haben, sollten Sie alle Ihre Geldmittel sehen. Wenn Sie jedoch auch Whirlpool verwendet haben, müssen Sie die `premix`, `postmix` und `badbank` Konten ableiten. Klicken Sie in Sparrow einfach auf den Tab `Settings`, dann auf `Add Accounts...`.

![samourai](assets/13.webp)
In dem sich öffnenden Fenster wählen Sie `Whirlpool Accounts` aus dem Dropdown-Menü und klicken dann auf `OK`.
![samourai](assets/14.webp)

Dann werden Ihre verschiedenen Whirlpool-Konten angezeigt, und Sparrow wird die notwendigen Schlüssel ableiten, um die zugehörigen Bitcoins zu verwenden.

![samourai](assets/15.webp)

Wenn Sie eine andere Software als Sparrow verwenden, wie Electrum, um Ihre Samourai-Wallet wiederherzustellen, hier sind die Whirlpool-Kontoindizes für die manuelle Wiederherstellung:
- Einzahlung: `m/84'/0'/0'`
- Bad Bank: `m/84'/0'/2147483644'`
- Premix: `m/84'/0'/2147483645'`
- Postmix: `m/84'/0'/2147483646'`

Sie haben jetzt Zugang zu Ihren Bitcoins auf Sparrow. Wenn Sie Hilfe bei der Verwendung von Sparrow Wallet benötigen, können Sie auch [unser spezielles Tutorial](https://planb.network/tutorials/wallet/desktop/sparrow-7e9a77c0-013d-4f8e-a811-408b71dc7607) auschecken.

Ich empfehle auch, die Labels, die Sie mit Ihren UTXOs auf Samourai verknüpft hatten, manuell zu importieren. Dies ermöglicht Ihnen später eine effektive Kontrolle über Ihre Coins auf Sparrow.

### Option 2: Die Wallet auf Sparrow mit dem mnemonischen Ausdruck wiederherstellen

Wenn Sie die Wiederherstellung mit der Backup-Datei nicht durchführen möchten, können Sie sich für eine traditionellere Methode entscheiden, indem Sie einfach Ihren 12-Wort-Wiederherstellungsausdruck und Ihre Passphrase verwenden. Diese zweite Option ist oft einfacher.
Um zu beginnen, stellen Sie sicher, dass Sie Ihren Wiederherstellungsphrase und Ihren Passphrase zur Hand haben. Öffnen Sie dann die Sparrow Wallet-Software, klicken Sie auf den `Datei`-Tab und wählen Sie `Wallet importieren`, um mit dem Import Ihrer Wallet zu beginnen.
![samourai](assets/16.webp)

Wählen Sie `Mnemonic Words (BIP39)` und klicken Sie im Dropdown-Menü auf `12 Wörter verwenden`.

![samourai](assets/17.webp)

Geben Sie die 12 Wörter Ihres Wiederherstellungsphrases in der richtigen Reihenfolge ein.

![samourai](assets/18.webp)

Wenn Sparrow eine `Ungültige Prüfsumme`-Nachricht anzeigt, deutet dies darauf hin, dass die Prüfsumme des Wiederherstellungsphrases nicht gültig ist, was wahrscheinlich bedeutet, dass Sie einen Fehler beim Eingeben der Wörter gemacht haben.

![samourai](assets/19.webp)

Wenn Ihr Phrase korrekt ist, markieren Sie das Kästchen `Passphrase verwenden?` und geben Sie Ihren Passphrase in das dafür vorgesehene Feld ein. Wenn alles korrekt erscheint, klicken Sie auf den `Wallet entdecken`-Button.

![samourai](assets/20.webp)

Benennen Sie Ihre Wallet, zum Beispiel "Samourai Recovery", und klicken Sie dann auf `Wallet erstellen`.

![samourai](assets/21.webp)
Sparrow wird Sie dann auffordern, ein Passwort zu wählen. Dieses Passwort schützt nur den Zugang zu Ihrer Wallet auf diesem PC und steht nicht in Beziehung zur Ableitung der Schlüssel Ihrer Wallet. Stellen Sie sicher, dass Sie ein starkes Passwort wählen, schreiben Sie es auf, um es sich zu merken, und klicken Sie auf `Passwort festlegen`.
![samourai](assets/22.webp)

Sparrow wird dann die Schlüssel für Ihre Wallet ableiten und nach entsprechenden Transaktionen suchen.

![samourai](assets/23.webp)

Wenn in diesem Stadium Ihre Wallet nicht erscheint, ist es möglich, dass Sie einen Fehler beim Eingeben des Passphrases oder des Wiederherstellungsphrases gemacht haben. Sie können den speziellen Fehlerbehebungsabschnitt für weitere Hilfe konsultieren.

Vorerst ist nur Ihr Einzahlungskonto zugänglich. Wenn Sie Samourai nur für dieses Konto verwendet haben, sollten Sie alle Ihre Geldmittel sehen. Wenn Sie jedoch auch Whirlpool verwendet haben, müssen Sie die `premix`, `postmix` und `badbank` Konten ableiten. Klicken Sie in Sparrow einfach auf den `Einstellungen`-Tab und dann auf `Konten hinzufügen...`.

![samourai](assets/24.webp)

Im sich öffnenden Fenster wählen Sie `Whirlpool-Konten` aus der Dropdown-Liste und klicken dann auf `OK`.

![samourai](assets/25.webp)

Dann werden Ihre verschiedenen Whirlpool-Konten angezeigt, und Sparrow wird die notwendigen Schlüssel ableiten, um die zugehörigen Bitcoins zu verwenden.

![samourai](assets/26.webp)

Wenn Sie eine andere Software wie Electrum verwenden, um Ihre Samourai-Wallet wiederherzustellen, hier sind die Whirlpool-Kontoindizes für die manuelle Wiederherstellung:
- Einzahlung: `m/84'/0'/0'`
- Bad Bank: `m/84'/0'/2147483644'`
- Premix: `m/84'/0'/2147483645'`
- Postmix: `m/84'/0'/2147483646'`

Sie haben jetzt Zugang zu Ihren Bitcoins auf Sparrow. Wenn Sie Hilfe bei der Verwendung von Sparrow Wallet benötigen, können Sie auch [unser spezielles Tutorial](https://planb.network/tutorials/wallet/desktop/sparrow-7e9a77c0-013d-4f8e-a811-408b71dc7607) konsultieren.

Ich empfehle auch, die Labels, die Sie mit Ihren UTXOs auf Samourai verknüpft hatten, manuell zu importieren. Dies ermöglicht Ihnen später eine effektive Kontrolle über Ihre Coins auf Sparrow.

### Was sind die häufigsten Probleme?
Nachdem ich in den letzten Tagen mehreren Personen geholfen habe, glaube ich, dass ich auf die meisten Probleme gestoßen bin, die die Wiederherstellung Ihrer Wallet verhindern können. Wenn Sie trotz der vorherigen Anleitungen immer noch nicht auf Ihre Wallet zugreifen können, finden Sie hier einige zusätzliche Empfehlungen. Zuerst und vor allem, für die Wiederherstellung ist es absolut wesentlich, dass die Wiederherstellungsphrase korrekt ist. Wenn Sie Ihre 12-Wort-Phrase nicht finden können, können Sie *Option 1* verwenden, um von Samourais Backup-Datei wiederherzustellen. Sie können auch direkt in Samourai Wallet auf Ihre Wiederherstellungsphrase zugreifen, indem Sie zu `Einstellungen`, dann `Wallet` navigieren und schließlich `12-Wort-Wiederherstellungsphrase anzeigen` auswählen.

Als Nächstes wird ein Tippfehler in Ihrer Passphrase während der Wiederherstellung zu falsch abgeleiteten Schlüsseln führen, was die Wiederherstellung Ihrer Wallet auf Sparrow verhindert. **Die Passphrase muss absolut genau sein!**

Um dies zu lösen, rate ich Ihnen zunächst, die Gültigkeit Ihrer Passphrase in der Samourai-Anwendung zu überprüfen, wie im Abschnitt "_Passphrase überprüfen_" dieses Artikels beschrieben:
1. **Validierung in Samourai:** Wenn Samourai bestätigt, dass die Passphrase korrekt ist, versuchen Sie die Wiederherstellung erneut von Anfang an, und stellen Sie sicher, dass Sie die Passphrase in Sparrow ohne Fehler genau eingeben;
2. **Passphrase-Fehler:** Wenn Samourai angibt, dass die Passphrase falsch ist, ist es sinnlos, Versuche auf Sparrow fortzusetzen. Solange die korrekte Passphrase nicht gefunden wird, ist die Wiederherstellung Ihrer Wallet unmöglich. Wenn Sie Ihre Passphrase dauerhaft verloren haben, bewahren Sie Ihre Samourai-Anwendung sicher auf. Alles, was Sie tun können, ist zu hoffen, dass die Server neu gestartet werden, sodass Sie direkt aus der Anwendung Ausgaben tätigen können, ohne eine Wiederherstellung zu benötigen. **Versuchen Sie in diesem Fall nicht, ein Dojo zu verbinden**, da dies implizieren würde, Ihre Wallet auf Samourai zurückzusetzen, was den Zugriff auf die Passphrase erfordert.

Unter den anderen aufgetretenen Fehlern sind viele mit der Netzwerkkonfiguration auf Sparrow verbunden.

Stellen Sie zunächst sicher, dass Sparrow korrekt im `mainnet` Modus konfiguriert ist, anstatt im `testnet` Modus. Tatsächlich, wenn Sparrow nach Ihren Transaktionen im Testnet sucht, wird es nichts finden, weil Ihre Wallet im Mainnet ist. Das Testnet ist eine alternative Version von Bitcoin, die ausschließlich für Tests und Entwicklung verwendet wird und auf einem separaten Netzwerk vom Hauptnetzwerk (Mainnet) betrieben wird, mit eigenen Blöcken und Transaktionen. Um zu überprüfen, in welchem Netzwerk Sie sich befinden, klicken Sie auf die Registerkarte `Tools`, dann auf `Neustart in`. Wenn die Option `Mainnet` angezeigt wird, sind Sie nicht im Hauptnetzwerk. Wählen Sie es aus, um Sparrow im Mainnet neu zu starten, und beginnen Sie dann Ihren Wiederherstellungsprozess erneut.

![samourai](assets/27.webp)
Einige hatten auch Schwierigkeiten, Sparrow mit ihrem Knoten zu verbinden. Unten rechts bei Sparrow zeigt ein farbiger Schalter an, ob Ihre Software korrekt mit einem Bitcoin-Knoten verbunden ist. Um Ihre Samourai-Transaktionen abzurufen, ist es wesentlich, dass die Software gut verbunden ist. Überprüfen Sie, ob der Schalter aktiviert ist, wie in meinem Bild unten (gelb für einen öffentlichen Knoten, grün für Bitcoin Core und blau für einen Electrum-Server).
![samourai](assets/28.webp)

Wenn der Schalter nicht aktiviert ist, klicken Sie darauf, um die Verbindung zu reaktivieren.

![samourai](assets/29.webp)

Wenn das Problem weiterhin besteht, finden Sie hier einige mögliche Lösungen:
- Wenn Sie versuchen, sich mit Ihrem eigenen Electrum-Server (blau) oder Ihrem Bitcoin Core (grün) zu verbinden und Sparrow keine Verbindung herstellen kann, überprüfen Sie die Verbindungsinformationen unter `Datei > Einstellungen... > Server`;

![samourai](assets/30.webp)
- Wenn das Verbindungsproblem weiterhin besteht, könnte dies an einer unvollständigen Synchronisation Ihres Knotens liegen. Stellen Sie sicher, dass Ihr Knoten und Ihr Indexer zu 100% synchronisiert sind. Wenn nötig, als letztes Mittel, trennen Sie Ihren Knoten von Sparrow und verbinden Sie sich mit einem öffentlichen Knoten; - Wenn Sie bereits mit einem öffentlichen Knoten verbunden waren und die Verbindung fehlschlägt, versuchen Sie, den Knoten zu wechseln, indem Sie einen anderen aus der Dropdown-Liste auswählen.

![samourai](assets/31.webp)

Wenn Sie Ihre Wallet erfolgreich wiederhergestellt haben, aber sie scheint unvollständig zu sein, könnte es ein Problem im Zusammenhang mit der Ableitung geben.

Ein Problem könnte auftreten, wenn Sie Ihr Samourai-Einzahlungskonto mit einem anderen Skripttyp als `P2WPKH` verwendet haben. Standardmäßig verwendet Samourai diesen Skripttyp, aber wenn Sie ihn manuell geändert haben, müssen Sie dies auch bei der Wiederherstellung auf Sparrow anpassen.

Um Zweige für andere Skripttypen abzuleiten, müssen Sie den Wiederherstellungsprozess für jeden verwendeten Skripttyp wiederholen. Gehen Sie dazu auf `Datei > Neue Wallet` in Sparrow, wählen Sie einen anderen Skripttyp aus der Dropdown-Liste, klicken Sie auf `Neue oder importierte Software-Wallet` und folgen Sie den gleichen Schritten wie im anfänglichen Tutorial.

![samourai](assets/32.webp)

Ein weiteres Ableitungsproblem, auf das ich gestoßen bin, steht im Zusammenhang mit dem Gap-Limit-Wert. Dieser Wert teilt Sparrow mit, nach wie vielen leeren Adressen es aufhören sollte, neue Adressen abzuleiten. Wenn Sie nach der Wiederherstellung bemerken, dass einige Transaktionen fehlen, könnte dies an einem zu niedrigen Gap-Limit liegen. Um dies zu lösen, gehen Sie zum Konto, das das Problem verursacht, zum Beispiel zum Postmix-Konto (wenn mehrere Konten betroffen sind, wiederholen Sie diesen Vorgang für jedes).

![samourai](assets/33.webp)

Klicken Sie auf den Tab `Einstellungen` und dann auf den Button `Erweitert...`.
![samourai](assets/34.webp)
Erhöhen Sie schrittweise den Wert des Gap-Limits, zum Beispiel habe ich es hier auf `400` gesetzt. Dann klicken Sie auf den Button `Schließen`.

![samourai](assets/35.webp)

Klicken Sie auf `Anwenden`, um abzuschließen. Sparrow wird dann eine größere Anzahl von Adressen ableiten und nach Geldern darauf suchen, was helfen sollte, alle Ihre Transaktionen wiederherzustellen.

![samourai](assets/36.webp)

Das deckt die verschiedenen Wiederherstellungsprobleme ab, auf die ich in den letzten Tagen gestoßen bin. Wenn Sie nach dem Ausprobieren all dieser Lösungen immer noch Probleme haben, lade ich Sie ein, dem [Discover Bitcoin Discord](https://discord.gg/xKKm29XGBb) beizutreten, um um Hilfe zu bitten. Ich besuche dieses Discord regelmäßig und würde mich freuen zu helfen, wenn ich die Lösung habe. Andere Bitcoiner werden auch in der Lage sein, ihre Erfahrungen zu teilen und ihre Unterstützung anzubieten. **In jedem Fall ist es wesentlich, Ihre Wiederherstellungsphrase, Ihre Sicherungsdatei und Ihre Passphrase vertraulich zu behandeln**. Teilen Sie sie mit niemandem, da dies es ihnen ermöglichen könnte, Ihre Bitcoins zu stehlen.

Sobald die Wiederherstellung abgeschlossen ist, haben Sie jetzt Zugang zu Ihren Bitcoins. Das ist eine gute Sache, aber es könnte nicht ausreichen. Tatsächlich bringt die Beschlagnahmung von Servern neue potenzielle Risiken für Ihre Privatsphäre mit sich. Im folgenden Abschnitt werden wir diese Risiken im Detail untersuchen und die Vorsichtsmaßnahmen skizzieren, die Sie ergreifen sollten, um Ihre Privatsphäre zu schützen.

## Was sind die Konsequenzen für die Privatsphäre Ihrer Transaktionen?

### Als Samourai-Nutzer ohne Dojo

Wenn Sie Samourai Wallet verwendet haben, ohne Ihr eigenes Dojo verbunden zu haben, mussten Ihre xpubs an die Server von Samourai übermittelt werden, damit die App funktioniert. Mit der Beschlagnahmung dieser Server ist es möglich, dass die Behörden jetzt Zugang zu diesen xpubs haben.
Dieses Szenario bleibt hypothetisch. Wir wissen nicht, ob diese xpubs aufgezeichnet wurden, ob ein möglicher Speicher zerstört wurde, ob die Behörden sie wiederhergestellt haben und ob sie planen, sie für die Kettenanalyse zu verwenden. In einer solchen Situation ist es jedoch klug, das Worst-Case-Szenario zu betrachten, in dem die Behörden die xpubs von Benutzern haben, die ihren eigenen Dojo nicht verbunden haben. Zur Referenz: Ein xpub ist eine Zeichenfolge, die alle notwendigen Elemente zur Generierung von untergeordneten öffentlichen Schlüsseln (öffentlicher Schlüssel + Kettencode) enthält. Es wird in hierarchisch deterministischen Wallets verwendet, um Empfangsadressen zu generieren und Transaktionen eines Kontos zu beobachten, ohne die zugehörigen privaten Schlüssel preiszugeben. Dies ermöglicht beispielsweise die Erstellung einer "Watch-Only"-Wallet. Die Offenlegung von xpubs kann jedoch die Privatsphäre des Benutzers gefährden, da sie Dritten das Verfolgen von Transaktionen und das Einsehen der Salden zugehöriger Konten ermöglichen.

Jeder, der Ihre xpubs kennt, kann somit alle Empfangsadressen Ihrer Wallet sehen, die in der Vergangenheit verwendet wurden und die in Zukunft generiert werden.

Für Benutzer ohne einen Dojo hat ein potenzieller Leak Ihrer xpubs zwei wesentliche Konsequenzen:
- Die CoinJoins, die Sie möglicherweise durchgeführt haben, werden aus Datenschutzsicht für jeden, der Ihre xpubs kennt, unwirksam, sodass Ihre Coins jeglichen Anonset verlieren;
- Diese Person kann auch alle Empfangsadressen Ihrer Samourai Wallet verfolgen.

Es ist daher wichtig, das Worst-Case-Szenario zu betrachten und sich von dieser Wallet, die möglicherweise in Bezug auf die Privatsphäre kompromittiert ist, zu trennen. Um dies zu tun, erstellen Sie eine neue Wallet von Grund auf mit einer anderen Software, wie Sparrow Wallet. Nachdem Sie die Gültigkeit Ihrer Backups überprüft haben, übertragen Sie alle Ihre Mittel durch Transaktionen. Obwohl diese Operation den Rückverfolgbarkeitslink Ihrer Coins nicht bricht, wird sie verhindern, dass die Behörden mit Sicherheit die Adressen Ihrer neuen Wallet kennen.

Während dieser Übertragungsoperation empfehle ich, die Konsolidierung Ihrer Coins zu vermeiden. Wenn wir davon ausgehen, dass Ihre xpubs kompromittiert sind, hat die Konsolidierung keinen Einfluss aus der Sicht der Person, die Zugang zu diesen xpubs hat, da Ihre Privatsphäre mit ihnen bereits kompromittiert ist. Ich rate Ihnen jedoch, Ihre Coins hauptsächlich zum Schutz Ihrer Privatsphäre vor anderen Personen nicht zu sehr zu konsolidieren. Im schlimmsten Fall könnten nur die Behörden Zugang zu Ihren xpubs haben, aber der Rest der Welt weiß nichts darüber. Somit könnte aus der Sicht anderer die Konsolidierung Ihrer Coins Ihre Privatsphäre erheblich schädigen aufgrund der Common Input Ownership Heuristic (CIOH).

Schließlich, um das Tracking endgültig zu unterbrechen, erwägen Sie auch, CoinJoins von dieser neuen Wallet aus durchzuführen.
**Warnung:** Es reicht nicht aus, einfach Ihre Samourai-Wallet auf Sparrow Wallet abzurufen. Es ist notwendig, eine völlig neue Wallet mit einer neuen Wiederherstellungsphrase zu erstellen, wenn Sie vermeiden möchten, xpubs zu verwenden, die möglicherweise geleakt sind. Wenn Sie Ihren bestehenden Seed in Sparrow importieren, ändern Sie nur die Wallet-Verwaltungssoftware, aber die Wallet bleibt dieselbe.

### Als Benutzer von Sparrow oder Samourai mit Dojo

Wenn Ihre Wallet nur auf Sparrow Wallet verwaltet wird, könnten Ihre xpubs nicht geleakt sein, egal ob Sie einen öffentlichen Knoten oder Ihren eigenen Bitcoin-Knoten verwenden. Ebenso, wenn Sie die Samourai-App verwenden und diese App seit der Erstellung Ihrer Wallet immer mit Ihrem eigenen Dojo verbunden haben, sind Ihre xpubs ebenfalls sicher.
Allerdings, wenn Sie dieselbe Wallet in einer Periode **ohne Ihren eigenen Dojo** und dann mit Ihrem eigenen Dojo verwendet haben, ist es möglich, dass die Samourai-Server Zugang zu Ihren xpubs hatten und daher könnten die Behörden diese kennen. Wenn Sie sich in dieser spezifischen Situation befinden, rate ich Ihnen, den Empfehlungen des vorherigen Abschnitts zu folgen und Ihre xpubs als kompromittiert zu betrachten.
Für diejenigen, die immer Sparrow oder Samourai mit ihrem eigenen Dojo verwendet haben, besteht das Hauptrisiko darin, dass die Anonsets Ihrer Münzen potenziell reduziert werden könnten. Nehmen wir im schlimmsten Fall an, dass alle Benutzer ohne ein Dojo ihre xpubs in den Händen der Behörden haben, dann könnte der Weg ihrer Münzen durch die Coinjoin-Zyklen von diesen Behörden nachverfolgt werden.

Um dies zu veranschaulichen, nehmen wir ein konkretes Beispiel. Stellen Sie sich vor, Sie haben an einem ersten Coinjoin-Zyklus teilgenommen, gefolgt von zwei weiteren nachgelagerten Coinjoin-Zyklen. Wenn die xpubs der Benutzer ohne ein Dojo nicht durchgesickert sind, dann wäre der voraussichtliche Anonset Ihrer Münze 13.

![samourai](assets/37.webp)

Wenn wir jedoch davon ausgehen, dass die xpubs durchgesickert sind und dass Sie während des anfänglichen Coinjoin auf einen Benutzer ohne Dojo gestoßen sind und dann auf 2 während des ersten nachgelagerten Coinjoin, dann wäre Ihr voraussichtlicher Anonset aus Sicht der Behörde nur 10 statt 13.

![samourai](assets/38.webp)
Diese potenzielle Verringerung des Anonsets ist schwer zu quantifizieren, da sie von zahlreichen Faktoren abhängt und jede Münze unterschiedlich betroffen ist. Zum Beispiel wirkt sich ein Benutzer ohne Dojo, der in den frühen Zyklen angetroffen wird, viel mehr auf den voraussichtlichen Anonset aus als einer, der in den späteren Zyklen angetroffen wird. Um Ihnen eine Vorstellung von der Situation zu geben, die hypothetisch bleibt, haben die neuesten Statistiken, die von Samourai bereitgestellt wurden, angegeben, dass zwischen 85% und 90% der Münzen, die an Coinjoins beteiligt waren, von Benutzern mit Dojo, Sparrow oder Bitcoin Keeper kamen, das heißt, Benutzer, die selbst im schlimmsten Fall ihre xpubs nicht hätten durchsickern sehen.

Obwohl diese Zahlen schwer zu überprüfen sind, scheinen sie mir aus zwei Gründen konsistent:
- Sparrow Wallet wird weit verbreitet verwendet;
- Die meisten Node-in-Box-Software bieten Dojo-Implementierungen an, und diese Mainstream-Software wie Umbrel sind heutzutage sehr beliebt.

Somit müssen mehrere Aspekte berücksichtigt werden. Wenn die Privatsphäre Ihrer Münzen gegenüber den Behörden für Sie äußerst wichtig ist, wäre es klug, sich auf das schlimmste Szenario vorzubereiten, und es ist schwierig zu garantieren, dass Ihre Whirlpool-Coinjoin-Zyklen aufgrund des potenziellen Durchsickerns von xpubs von Benutzern ohne Dojo nicht nachverfolgt werden könnten. Obwohl diese Annahme höchst unwahrscheinlich ist, ist sie nicht unmöglich.

Andererseits, wenn die Privatsphäre Ihrer Münzen gegenüber der Behörde, die möglicherweise im Besitz dieser xpubs ist, nicht entscheidend für Sie ist, dann kann die Situation anders betrachtet werden.

Ich spezifiziere "gegenüber der Behörde", weil es wichtig ist zu bedenken, dass nur die Behörde, die die Server beschlagnahmt hat, potenziell von diesen xpubs weiß. Wenn Ihr Ziel bei der Verwendung von Coinjoin darin bestand, zu verhindern, dass Ihr Bäcker Ihren Geldern folgen kann, dann ist er nicht besser informiert als vor der Serverbeschlagnahmung.
Schließlich ist es wesentlich, den ursprünglichen Anonset Ihrer Münze zu berücksichtigen, bevor der Server beschlagnahmt wurde. Nehmen wir das Beispiel einer Münze, die einen prospektiven Anonset von 40.000 erreicht hatte; die potenzielle Verringerung dieses Anonsets ist wahrscheinlich vernachlässigbar. Tatsächlich ist es bei einem bereits sehr hohen Basis-Anonset unwahrscheinlich, dass die Anwesenheit einiger weniger Benutzer ohne Dojo die Situation radikal ändern könnte. Wenn Ihre Münze jedoch einen Anonset von 40 hatte, könnte diese potenzielle Lücke Ihre Anonsets ernsthaft beeinträchtigen und möglicherweise eine Nachverfolgung ermöglichen. Mit dem WST-Tool, das nun nach der Abschaltung von OXT.me außer Betrieb ist, können Sie diese Anonsets nur schätzen. Für den retrospektiven Anonset gibt es nicht allzu viel zu befürchten, da das Whirlpool-Modell sicherstellt, dass er vom ersten Coinjoin an sehr hoch ist, dank des Erbes Ihrer Peers. Das einzige Problem könnte auftreten, wenn Ihre Münze seit mehreren Jahren nicht neu gemischt wurde und sie zu Beginn des Starts eines Pools gemischt wurde. Hinsichtlich des prospektiven Anonsets können Sie die Dauer untersuchen, die Ihre Münze für Coinjoins verfügbar war. Wenn es mehrere Monate waren, dann hat sie wahrscheinlich einen extrem hohen prospektiven Anonset. Im Gegensatz dazu, wenn sie nur wenige Stunden vor der Beschlagnahme der Server zu einem Pool hinzugefügt wurde, dann ist ihr prospektiver Anonset wahrscheinlich sehr niedrig.
[**-> Erfahren Sie mehr über Anonsets und ihre Berechnungsmethode.**](https://planb.network/tutorials/privacy/analysis/wst-anonsets-0354b793-c301-48af-af75-f87569756375)

Ein weiterer Aspekt, den es zu berücksichtigen gilt, ist die Auswirkung von Konsolidierungen auf die Anonsets von Münzen, die gemischt wurden. Da die Whirlpool-Konten nicht mehr über die Samourai-App zugänglich sind, ist es wahrscheinlich, dass viele Benutzer ihre Wallet auf andere Software übertragen und versucht haben, ihre Gelder aus Whirlpool abzuheben. Insbesondere letztes Wochenende, als die Transaktionsgebühren im Bitcoin-Netzwerk relativ hoch waren, gab es einen starken technischen und wirtschaftlichen Anreiz, Post-Mix-Münzen zu konsolidieren. Das bedeutet, dass es wahrscheinlich ist, dass viele Benutzer signifikante Konsolidierungen vorgenommen haben.

Das Problem mit diesen Post-Mix-Konsolidierungen ist, dass sie immer die Anonsets reduzieren, nicht nur für den Benutzer, der sie durchführt, sondern auch für die Benutzer, denen sie während ihrer Coinjoin-Zyklen begegnet sind. Obwohl ich dieses Phänomen nicht genau verifizieren oder quantifizieren konnte, können uns die wirtschaftlichen Anreize im Zusammenhang mit den Transaktionsgebühren zu dieser Zeit annehmen lassen, dass die Anonsets potenziell niedriger sind.

### Als Sentinel-Benutzer

Die Netzwerkoperation der Watch-Only-Wallet-Anwendung Sentinel ähnelt der von Samourai. Um auf Ihre Wallet-Informationen zuzugreifen, muss die Anwendung die xpubs, öffentlichen Schlüssel und Adressen, die Sie bereitgestellt haben, an ein Dojo übermitteln. Wenn Sie immer Ihr eigenes Dojo auf Sentinel verwendet haben, gibt es kein Problem, und Sie können die Anwendung ohne Sorgen weiter verwenden. Wenn Sie jedoch von den Servern von Samourai für Ihr Sentinel abhängig waren, ist es möglich, dass Ihre xpubs exponiert wurden. In diesem Fall ist es ratsam, demselben Wallet-Wechselprozess zu folgen, der für Samourai Wallet empfohlen wird, wenn es mit den Servern von Samourai verbunden ist.

Für den unwahrscheinlichen Fall, dass Sie Ihr Dojo mit Samourai, aber nicht mit Sentinel verwendet haben, wäre es klüger zu betrachten, dass Ihre xpubs kompromittiert sind.

## Schlussfolgerung
Vielen Dank, dass Sie diesen Artikel bis zum Ende gelesen haben. Falls Sie denken, dass Informationen fehlen oder wenn Sie Vorschläge haben, zögern Sie bitte nicht, mich zu kontaktieren, um Ihre Gedanken zu teilen. Zusätzlich, wenn Sie weitere Unterstützung bei der Wiederherstellung Ihres Samourai Wallets trotz dieses Tutorials benötigen, lade ich Sie ein, dem [Discover Bitcoin Discord](https://discord.gg/xKKm29XGBb) beizutreten, um um Hilfe zu bitten. Ich besuche diesen Discord regelmäßig und wäre erfreut, Ihnen zu helfen, falls ich die Lösung habe. Andere Bitcoiner werden ebenfalls in der Lage sein, ihre Erfahrungen zu teilen und ihre Unterstützung anzubieten. **In jedem Fall ist es essenziell, Ihre Wiederherstellungsphrase, Ihre Sicherungsdatei und Ihre Passphrase vertraulich zu behandeln**. Teilen Sie diese mit niemandem, da dies anderen ermöglichen könnte, Ihre Bitcoins zu stehlen.