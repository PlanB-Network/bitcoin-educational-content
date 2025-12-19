---
name: Satodime
description: Finden Sie heraus, wie Sie den Satodime mit der mobilen Anwendung nutzen können
---
![cover](assets/cover.webp)



Dieser Leitfaden führt Sie durch die Installation, Konfiguration und Nutzung der mobilen Anwendung von Satodime. Sie erfahren, wie Sie Ihre Karte in Besitz nehmen, Tresore erstellen, Geldmittel hinzufügen, Ihre privaten Schlüssel entsiegeln und wiederherstellen können. In den Anhängen finden Sie Ressourcen, bewährte Verfahren und technische Erklärungen.



## Einführung



**Satodime**, entwickelt von **[Satochip](https://satochip.io/fr/)**, ist eine sichere Trägerkarte für die Speicherung von Bitcoin auf eine greifbare und einfache Weise. Sie fungiert als selbstverwahrende wallet-Hardware, bei der Sie die volle Kontrolle über Ihre privaten Schlüssel haben, ohne von einer dritten Partei abhängig zu sein. Sie ist Open-Source und EAL6+-zertifiziert und unterstützt bis zu drei unabhängige Tresore.



### Hintergrund des Produkts



Satodime, eine **carte au porteur, gehört demjenigen, der sie physisch besitzt**, ohne dass eine vorherige Registrierung oder Identifizierung erforderlich ist. Sie erfüllt den Bedarf an sicherer, tragbarer Bitcoin-Aufbewahrung und ermöglicht es jedem, der die Karte besitzt, sie zu benutzen oder Bitcoins zu übertragen, indem er sie über die mobile App scannt, um sie in Besitz zu nehmen oder Tresore zu entsperren. Im Gegensatz zu einer Papierrechnung verwendet sie einen sicheren Chip, um die privaten Schlüssel zu versiegeln, die erst nach dem Entsiegeln offengelegt werden, wodurch die Karte dem Bargeld ähnelt, bei dem der Besitz durch den physischen Besitz bestimmt wird. Sie eignet sich ideal zum Verschenken von Bitcoins und erleichtert die sichere Übertragung von Bitcoins von Hand zu Hand, während die mobile Anwendung NFC für die Interaktion mit dem Smartphone nutzt.





- Sicherheit**: Erzeugung und Speicherung privater Schlüssel im manipulationssicheren Chip; sichtbarer Status (versiegelt, entsiegelt, leer).
- Funktionen**: Bitcoins direkt über die App kaufen (Paybis-Partner); Mainnet und Testnet verwalten.
- Open-Source**: Code unter AGPLv3-Lizenz, überprüfbar auf GitHub.



### Kontinuierliche Entwicklung



Die Anwendung wird regelmäßig weiterentwickelt. Informieren Sie sich auf der Satochip-Website oder in den Geschäften über Aktualisierungen. Es können zum Beispiel neue Blockchains oder Kauffunktionen hinzugefügt werden. Überprüfen Sie die [Satochip GitHub](https://github.com/Toporin/Satodime-Applet) für laufende Entwicklungen.



## 1. Voraussetzungen



Bevor Sie mit **Satodime** beginnen, vergewissern Sie sich, dass Sie die folgenden Gegenstände besitzen:





- Kompatibles Smartphone**: Android- oder iOS-Gerät mit NFC-Funktion.
- Satodime**-Karte: Neu oder uninitialisiert.
- Internetverbindung**: Zum Herunterladen der App.
- Grundkenntnisse**: Verständnis für private/öffentliche Schlüssel und die Risiken des Verlusts (irreversibel).
- Sicheres Medium**: Ein sicherer Ort, um private Schlüssel zu speichern, sobald sie entsiegelt sind (Papier, Metall; niemals digital).



## 2. Einrichtung





- Laden Sie die Bewerbung herunter** :
 - [App Store](https://apps.apple.com/be/app/satodime/id1672273462)** (iOS)
 - [Google Play Store](https://play.google.com/store/apps/details?id=org.satochip.satodimeapp)** (Android)
 - Überprüfen Sie den Entwickler (Satochip), um Betrug zu vermeiden.
 - Satodime ist **Open-Source**. Quellcode: [Satochip's GitHub](https://github.com/Toporin/Satodime-Applet).





- Installieren und starten Sie die Anwendung**: Aktivieren Sie NFC auf Ihrem Telefon, falls erforderlich.



![image](assets/fr/01.webp)



## 3. Erstmalige Konfiguration



### 3.1 Anwendung starten und scannen



Öffnen Sie die App und folgen Sie den Anweisungen des Assistenten. Legen Sie die Satodime-Karte auf den NFC-Leser Ihres Telefons (normalerweise auf der Rückseite). Halten Sie sie während des gesamten Vorgangs gedrückt, um eine stabile Verbindung zu gewährleisten.





- Wenn NFC nicht funktioniert, überprüfen Sie die Einstellungen Ihres Telefons.
- Ein Trinkspruch bestätigt den Erfolg: "Erfolgreiche Lektüre".



![image](assets/fr/02.webp)



In der Regel **müssen alle folgenden Vorgänge durch Scannen der Satodime-Karte bestätigt werden**



### 3.2 Inbesitznahme der Karte (*Ownership*)



Bei der ersten Verwendung müssen Sie Eigentümer der Karte werden, um sie zu sichern:





- Klicken Sie in der App auf "*Ownership* nehmen".
- Bestätigen Sie den Vorgang: Dadurch wird ein eindeutiger Eigentümerschlüssel erzeugt.
- Scannen Sie die Karte erneut, um die Änderungen zu übernehmen.
- Warnung**: Dieser Schritt ist unumkehrbar. Bitte lesen Sie [den Artikel über *Eigentum*] (https://satochip.io/satodime-ownership-explained/).



![image](assets/fr/03.webp)




## 4. Einen sicheren Ort schaffen



Satodime unterstützt bis zu 3 Tresore. Erstellen Sie einen, um Bitcoin zu speichern:





- Wählen Sie einen leeren Safe (z. B. Safe 01).
- Wählen Sie Blockchain (Bitcoin).
- Klicken Sie auf "*Erstellen & Seal*".
- Scannen Sie die Karte zum generate und versiegeln Sie den privaten Schlüssel (unbekannt, bis er entsiegelt wird).
- Glückwunsch**: Ihr Tresor ist nun versiegelt und bereit für den Geldempfang.



![image](assets/fr/04.webp)



![image](assets/fr/05.webp)



## 5. Mittel hinzufügen



Sobald er versiegelt ist, laden Sie den Safe mit Bitcoins:





- Wählen Sie den Safe.
- Klicken Sie auf "*Geldmittel hinzufügen*".
- Kopieren Sie die öffentliche Adresse oder scannen Sie den QR-Code.
- Senden Sie Geld von einem anderen wallet.
- Überprüfen Sie den Saldo nach der Bestätigung auf der Blockchain.
- Kaufoption: Klicken Sie auf "*Kaufen*", um direkt über Paybis (Visa, Mastercard, etc.) zu kaufen. Anwendbare Gebühren.



![image](assets/fr/06.webp)



## 6. Tresor entsiegeln



Um auf den privaten Schlüssel zuzugreifen und das Geld an einen anderen Ort zu überweisen, müssen Sie den Tresor entsperren:





- Wählen Sie den versiegelten Safe.
- Klicken Sie auf "Entsiegeln".
- Bestätigen Sie die Warnung: Dieser Vorgang ist nicht umkehrbar.
- Scannen Sie die Karte, um sie zu entsiegeln.
- Der Safe wird auf "*Unsealed*" gesetzt; der private Schlüssel kann nun eingesehen/exportiert werden.
- Warnung**: Sobald die Versiegelung entfernt wurde, ist der private Schlüssel zugänglich. Wenn jemand in den Besitz Ihres Smartphones gelangt, kann er auf diesen Schlüssel zugreifen und so die Gelder in Ihrem Safe wiederherstellen (unwiderruflich).



![image](assets/fr/07.webp)



## 7. Privaten Schlüssel wiederherstellen



Nach dem Entsiegeln exportieren Sie den Schlüssel zur Verwendung in einem anderen wallet:





- Vergewissern Sie sich, dass Sie sich in einer sicheren Umgebung befinden.
- Klicken Sie auf "*Privaten Schlüssel anzeigen*".
- Wählen Sie das Format: Legacy, SegWit, WIF, usw.
- Kopieren Sie den Schlüssel oder scannen Sie den QR-Code.
- Sicherheit**: Geben Sie Ihren privaten Schlüssel niemals weiter. Speichern Sie ihn offline.
- Importieren Sie sie in ein wallet-Softwareprogramm, das mit der Fondsverwaltung kompatibel ist (z. B. Sparrow Wallet oder Electrum).



![image](assets/fr/08.webp)





## 8. Kofferraum zurücksetzen



Durch das Zurücksetzen des Safes wird der zugehörige private Schlüssel unwiderruflich gelöscht. Mit anderen Worten: Wenn Sie keine Kopie Ihres privaten Schlüssels gesichert oder ihn in ein anderes wallet importiert haben, führt das Zurücksetzen des Tresors zum unwiderruflichen Verlust der darin enthaltenen Mittel.



![image](assets/fr/09.webp)



Durch das Zurücksetzen des Rüssels wird der Steckplatz leer und bereit für einen neuen Rüssel.



## 9. Eigentum übertragen



Um - zum Beispiel - Bitcoins über Satodime anzubieten, müssen Sie :




- Übernehmen Sie das Eigentum an der Karte,
- Erstellen Sie einen Bitcoin-Tresor,
- Die Übertragung ist abgeschlossen,
- Übertragung des Kartenbesitzes: Die nächste Person, die die Karte scannt, wird ihr Besitzer,
- Geben Sie die Satodime-Karte einer Person Ihrer Wahl und fordern Sie sie auf, die Anwendung herunterzuladen und die Karte zu scannen, um sie in Besitz zu nehmen - und damit Zugriff auf die darauf "gespeicherten" Bitcoins zu erhalten.



![image](assets/fr/10.webp)




## ANHÄNGE



### A1. Bewährte Praktiken



So verwenden Sie **Satodime** sicher:





- Sichern Sie die Karte**: Behandeln Sie sie wie Bargeld; Verlust = verlorenes Geld, wenn nicht der Besitzer.
- Schlüssel-Backup**: Nach der Entsiegelung sind die privaten Schlüssel auf einem sicheren physischen Medium zu speichern. Niemals digital.
- Status prüfen**: Scannen Sie immer, um den Kartenbesitz und den versiegelten/unversiegelten Status der Tresore zu überprüfen.
- Vertraulichkeit**: Verwenden Sie neue Adressen; vermeiden Sie einen zentralen Austausch für Überweisungen.
- Aktualisierungen**: Halten Sie die App über die Stores auf dem neuesten Stand.
- Wiederherstellung**: Wenn die Karte verloren geht, aber noch vorhanden ist, befinden sich die Gelder in der Blockchain; verwenden Sie den privaten Schlüssel, wenn sie entsiegelt wurde.



### A2. Zusätzliche Ressourcen



Spezifisch für Satodime :




- [Satodime-Produkt](https://satochip.io/fr/product/satodime/)
- [Mobile Guide](https://satochip.io/wp-content/uploads/2024/11/Satodime-FR-Short-tuto-app-mobile.pdf)



[Plan ₿ Academy] (https://planb.academy/) für Tutorials zu Selbstverwahrung, privaten Schlüsseln usw.



**Speichern Sie Ihre Wiederherstellungsphrase**:



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

**Anleitung zum Satochip (dem ersten Produkt der Marke) :**



https://planb.academy/tutorials/wallet/hardware/satochip-e9bc81d9-d59b-420d-9672-3360212237ba

**Saatgutbetreuer-Tutorials:**



https://planb.academy/tutorials/wallet/backup/seedkeeper-906dfff8-1826-4837-92d1-8669e216d356

https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

https://planb.academy/tutorials/computer-security/authentication/seedkeeper-password-64ffaf68-53aa-43c3-bc7a-c1dc2a17fee3

### A3. Über Satochip



**Offizielle Links** :




- [Site Satochip](https://satochip.io/fr/)
- [GitHub](https://github.com/Toporin/Satodime-Applet)
- Unterstützung: info@satochip.io



**Satochip** ist ein belgisches Unternehmen, das Hardware- und Softwarelösungen für die Verwaltung und Speicherung von Bitcoins und anderen Kryptowährungen entwickelt. Das Flaggschiffprodukt, die Satochip-Hardware wallet, ist eine NFC-Karte, die mit einem EAL6+-zertifizierten secure element ausgestattet ist. Ergänzt durch den Seedkeeper, einen Manager für Merksätze und Geheimnisse, und den Satodime, eine Inhaberkarte, bietet Satochip ein umfassendes Angebot, das auf die Bedürfnisse der Nutzer zugeschnitten ist. Seine Geräte, die auf Open-Source-Software basieren, zielen darauf ab, die Sicherheit auf Bitcoin zu demokratisieren.