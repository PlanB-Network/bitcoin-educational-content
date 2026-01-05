---
name: Bitcoin Keeper - Erbschaftsplan
description: Planen Sie Ihre Bitcoin-Übertragung mit Bitcoin Keeper
---

![cover](assets/cover.webp)



Die Übertragung von Bitcoin-Vermögenswerten ist eine der von den Inhabern am meisten unterschätzten Herausforderungen. Im Gegensatz zu einem Bankkonto, bei dem das Finanzinstitut die Gelder an die rechtmäßigen Erben weitergeben kann, beruht Bitcoin vollständig auf dem Besitz von privaten Schlüsseln. Ein rechtmäßiger Erbe wird ohne diese Schlüssel niemals auf die Gelder zugreifen können, während eine böswillige Person, die im Besitz der Geheimnisse ist, diese ohne jede Formalität ausgeben kann.



In diesem zweiten Bitcoin Keeper-Tutorial erkunden wir die Premiumfunktionen für die Nachlassplanung. Die Anwendung bietet fortschrittliche Werkzeuge für die Erstellung erweiterter Tresore mit zeitgesteuerten Schutzmechanismen dank Miniscript sowie Begleitdokumente, die Ihre Angehörigen begleiten.



Dieser Leitfaden setzt voraus, dass Sie die Grundlagen von Bitcoin Keeper (Portfolioerstellung, klassische Multisig, Hinzufügen von Hardware-Tasten), wie in unserem ersten Tutorial erklärt, bereits beherrschen:



https://planb.academy/tutorials/wallet/mobile/bitcoin-keeper-7f2a160b-10b6-4cc5-8820-514ee2eb1599

![video](https://youtu.be/tCld_-n2d30)



## Bitcoin Keeper-Abonnementpläne



Bitcoin Keeper basiert auf einem Freemium-Modell mit drei Abo-Stufen, die progressive Funktionen bieten. Um auf die Pläne zuzugreifen, gehen Sie auf die Registerkarte **Mehr** und tippen Sie dann auf Ihren aktuellen Plan (Standard ist "Pleb"), um den Bildschirm **Abonnement verwalten** zu öffnen.



![Plans d'abonnement](assets/fr/01.webp)



Der **Pleb-Tarif** (kostenlos) bietet Zugang zum Wesentlichen: unbegrenzte Erstellung von Single-Key- und Multi-Key-Wallets, Kompatibilität mit allen wichtigen Hardware-Wallets (Coldcard, Trezor, Ledger, Jade, Tapsigner...), Münzkontrolle, Etikettierung und Anbindung an einen persönlichen Electrum-Server. Dieser Plan ist für den Standardgebrauch und sogar für klassische multi-sig-Konfigurationen ausreichend.



Der **Hodler-Tarif** (9,99 €/Monat, 1 Monat kostenlos bei jährlicher Zahlung) umfasst alle Pleb-Funktionen und bietet zusätzlich verschlüsselte Backups in der Cloud (iCloud oder Google Drive), um Ihre Tresore auf jedem Gerät wiederherzustellen, Server Key, um automatische Ausgabenrichtlinien und 2FA ab einem bestimmten Schwellenwert hinzuzufügen, sowie Canary Wallets, um unbefugten Zugriff auf Ihre Schlüssel zu erkennen.



Der **Diamond Hands Plan** (29,99 €/Monat, mit 1 Monat gratis bei jährlicher Zahlung) ist das Komplettpaket für die Nachlassplanung. Es umfasst den gesamten Hodler-Plan und schaltet den Inheritance Key (aufgeschobene Aktivierung), den Emergency Key (Notfallschlüssel für die Wiederherstellung im Falle eines Verlusts), die Tools und Dokumente zur Nachlassplanung sowie einen Support-Anruf mit dem Concierge-Team zur Validierung Ihrer Konfiguration frei. Dies ist das Angebot für Bitcoiner, die ihr Erbe über mehrere Generationen weitergeben möchten.



Wichtiger Hinweis: Die von Ihnen erstellten Tresore bleiben zugänglich, auch wenn Sie wieder zum kostenlosen Tarif wechseln. Ihre Konfigurationen beruhen auf offenen Standards (BSMS, Miniscript) und funktionieren unabhängig von Ihrem Abonnement.



## Erbschaftsunterlagen



Sobald Sie Ihr Diamond Hands Abonnement aktiviert haben, rufen Sie den Abschnitt **Erbschaftsdokumente** auf der Registerkarte Mehr auf. Bitcoin Keeper bietet fünf Musterdokumente zur Strukturierung Ihres Nachlassplans sowie einen Abschnitt mit Tipps:



![Documents d'héritage](assets/fr/02.webp)





- Seed Words Template**: eine Vorlage, um Ihre Genesungsphrasen geordnet aufzuschreiben
- Vertrauenspersonen**: eine Vorlage für die Auflistung der Kontaktdaten von Vertrauenspersonen, die an Ihrem Plan beteiligt sind (Notar, Rechtsanwalt, Erben, Schlüsselpersonen)
- Zusätzlicher Freigabeschlüssel**: ein Dokument, in dem die technischen Informationen für jeden Schlüssel aufgeführt sind: PIN-Code, Ableitungspfad, physischer Standort, Gerätetyp und alle anderen Informationen, die zur Identifizierung und Verwendung des Schlüssels nützlich sind
- Rückforderungsanweisungen**: Schritt-für-Schritt-Anweisungen für den Erben oder Begünstigten zur Rückforderung von Geldern
- Brief an den Anwalt**: ein vorausgefüllter Brief, der für Ihren Anwalt oder Notar angepasst werden kann



Der Abschnitt **Erbschaftstipps** bietet praktische Ratschläge zur Sicherung der Schlüssel für die Erben und zur Optimierung Ihres Erbschaftsplans.



Passen Sie diese Dokumente an Ihre Situation an und bewahren Sie sie getrennt von den Schlüsseln an einem sicheren Ort auf.



## Konfigurieren der Cloud-Sicherung



Aktivieren Sie vor der Erstellung Ihres Legacy-Datenspeichers die Cloud-Sicherung, um Ihre Konfigurationsdateien zu schützen. Drücken Sie auf der Registerkarte "Mehr" auf **Personal Cloud Backup**.



![Configuration Cloud Backup](assets/fr/03.webp)



Wählen Sie ein sicheres Passwort, um Ihre Backups zu verschlüsseln. Dieses Passwort schützt nur die wallet Konfigurationsdateien (nicht Ihre privaten Schlüssel). Bestätigen Sie das Passwort und drücken Sie **Bestätigen**. Ihre Backups werden je nach Gerät in Ihrer iCloud oder Google Drive gespeichert. Drücken Sie **Jetzt sichern**, um Ihre erste Sicherung zu starten.



## Importieren Sie Ihre Hardware-Schlüssel



Für unser Beispiel erstellen wir einen 2-von-3-Safe mit zwei zusätzlichen Schlüsseln (Vererbung und Notfall). Beginnen wir mit dem Importieren aller erforderlichen Schlüssel in die Registerkarte **Schlüssel**.



![Import des clés hardware](assets/fr/04.webp)



Drücken Sie **Taste hinzufügen**, und wählen Sie dann **Taste von einer Hardware hinzufügen**, um ein Hardware-wallet anzuschließen. Bitcoin Keeper unterstützt viele Geräte: BitBox02, Coldcard, Blockstream Jade, Keystone, Krux, Ledger, Foundation Passport, TwentyTwo Portal, Seedsigner, und Specter Solutions.



In unserer Konfiguration importieren wir :




- 2 **Coldcard**-Tasten (MK4SP und MK4)
- 2 Tasten **Tapsigner** (Metro und Genesis)



Um eine Coldcard hinzuzufügen, wählen Sie sie aus der Liste aus und folgen Sie den Anweisungen auf dem Bildschirm, um den öffentlichen Schlüssel per QR-Code, Datei, USB oder NFC zu exportieren. Weitere Einzelheiten zur Verwendung einer Coldcard oder des Tapsigner finden Sie in unseren speziellen Anleitungen:



https://planb.academy/tutorials/wallet/hardware/tapsigner-ab2bcdf9-9509-4908-9a4a-2f2be1e7d5d2

https://planb.academy/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3

https://planb.academy/tutorials/wallet/hardware/coldcard-mk4-5d44dd94-423d-4e37-9a8c-3fc38b45ce59


Sobald Sie alle Schlüssel importiert haben, finden Sie sie auf der Registerkarte Schlüssel mit ihren eigenen Namen.



## Legacy wallet erstellen



Fahren wir mit der Erstellung des Stammes fort. Drücken Sie auf der Registerkarte **Geldbörsen** auf **Wallet hinzufügen**, wählen Sie **Bitcoin Wallet** und dann **Wallet erstellen**.



![Création du wallet](assets/fr/05.webp)



Wählen Sie den wallet-Typ. Wählen Sie für unseren Legacy-Plan **2 von 3 Mehrfachtasten**. Aktivieren Sie unten auf dem Bildschirm **Erweiterte Sicherheitsoptionen** und drücken Sie dann **Fortfahren**.



![Options de sécurité avancées](assets/fr/06.webp)



Markieren Sie im Popupfenster Erweiterte Sicherheitsoptionen :




- Vererbungsschlüssel**: ein zusätzlicher Schlüssel, der nach einer bestimmten Zeit zum Quorum hinzugefügt wird
- Notfallschlüssel**: ein Schlüssel mit aufgeschobener Gesamtkontrolle zur Wiederherstellung der Mittel im Falle eines Schlüsselverlustes



Drücken Sie **Änderungen speichern**. Wählen Sie dann aus den importierten Schlüsseln (z. B. Seed Key, Coldcard MK4SP und Tapsigner Metro) die 3 Schlüssel aus, aus denen Ihr wallet bestehen wird.



## Festlegung spezieller Schlüsseltermine



Auf dem nächsten Bildschirm können Sie den Notfallschlüssel und den Vererbungsschlüssel konfigurieren. Hier legen Sie die Verzögerungen für die Aktivierung dieser Sonderschlüssel fest.



![Configuration des délais](assets/fr/07.webp)



Für den **Notfallschlüssel** wählen Sie den Hardwareschlüssel, der als ultimatives Backup dienen soll (hier Coldcard MK4), und wählen Sie die Aktivierungsfrist (in unserem Beispiel: 2 Jahre). Im Gegensatz zum Vererbungsschlüssel trägt der Notfallschlüssel nicht zum Quorum bei: Er ermöglicht es Ihnen, die Multisig** vollständig zu umgehen, und gibt Ihnen die vollständige Kontrolle über die Mittel nach Ablauf der Frist. Er ist Ihr letzter Ausweg: Wenn mehrere Schlüssel verloren gehen oder zerstört werden, können Sie mit diesem einen Schlüssel alles wiederherstellen. Er muss daher mit äußerster Strenge geschützt werden.



Für den **Erbschaftsschlüssel** wählen Sie den für den Erben bestimmten Schlüssel (hier Coldcard MK4SP) und wählen die Verzögerung (in unserem Beispiel: 1 Jahr). Nach einem Jahr ohne Bewegung wird dieser Schlüssel **dem Signaturquorum hinzugefügt**. In der Praxis wird Ihr wallet 2-of-3 nach Ablauf dieser Frist zu einem wallet 2-of-4, so dass der Erbe neben den bestehenden Schlüsseln an der Signatur teilnehmen kann.



### Wie funktionieren Zeitschaltuhren?



Bitcoin Keeper verwendet **absolute Zeitsperren** (CLTV - CheckLockTimeVerify), die durch Miniscript ermöglicht werden. Im Gegensatz zu relativen Zeitsperren (CSV), die beim Empfang jedes UTXO beginnen, arbeiten absolute Zeitsperren mit einem **festen Ablaufdatum**, das bei der Erstellung des wallet festgelegt wird.



Konkret: Wenn Sie heute ein wallet mit einem Vererbungsschlüssel für 1 Jahr anlegen, ist das Aktivierungsdatum "heute + 1 Jahr". Alle in diesen wallet eingezahlten Gelder sind unabhängig von ihrem Einzahlungsdatum an diesem Datum über den Vererbungsschlüssel zugänglich.



Der Vorteil absoluter Zeitpläne ist, dass sie Vorlaufzeiten von mehr als 15 Monaten ermöglichen (die Grenze für relative CSV-Zeitpläne), was erklärt, warum Bitcoin Keeper Optionen wie 2 Jahre anbieten kann.



### Der Aktualisierungsmechanismus



Um die Aktivierung von Sonderschlüsseln während Ihrer Lebensdauer zu verhindern, müssen Sie Ihren wallet regelmäßig "auffrischen". Bei absoluten Zeitschlössern bedeutet dies, dass Sie **den wallet mit einem neuen, in die Zukunft verschobenen Ablaufdatum** neu erstellen und dann Ihr Guthaben auf diesen neuen wallet übertragen.



Bitcoin Keeper vereinfacht diesen Prozess mit einer integrierten Aktualisierungsfunktion. Die Anwendung bewältigt die Komplexität automatisch im Hintergrund: Sie folgen einfach den geführten Schritten, ohne manuell ein neues wallet zu erstellen oder die Mittel selbst zu übertragen. Planen Sie diesen Vorgang regelmäßig und rechtzeitig vor Ablauf des kürzesten konfigurierten Zeitrahmens. Bei einem Vererbungsschlüssel mit einer Laufzeit von 1 Jahr sollten Sie beispielsweise alle 9-10 Monate eine Aktualisierung vornehmen, um eine Sicherheitsmarge zu erhalten.



## Konfiguration speichern und exportieren



Nachdem das wallet erstellt wurde, erinnert Sie die Anwendung daran, die Konfigurationsdatei zu speichern. **Dieser Schritt ist entscheidend**: Ohne diese Datei können Ihre Erben das wallet multisig nicht wiederherstellen.



![Export de la configuration](assets/fr/08.webp)



Drücken Sie **Wallet-Wiederherstellungsdatei sichern**. Es stehen mehrere Exportoptionen zur Verfügung:




- PDF-Export**: erzeugt ein vollständiges Dokument mit allen wallet-Informationen
- QR** anzeigen: zeigt einen QR-Code an, um die Konfiguration auf ein anderes Gerät zu importieren
- Airdrop / Dateiexport**: exportiert die Datei über die Freigabeoptionen
- NFC**: Freigabe über NFC mit einem kompatiblen Gerät



Vervielfältigen Sie die Kopien: eine bei Ihrem Notar, eine in einem Banksafe, eine verschlüsselte digitale Version. Ihr neuer wallet erscheint nun in der Registerkarte "Brieftaschen" mit den Kennzeichnungen "Mehrfachschlüssel", "2 von 3", "Erbschaftsschlüssel" und "Notfallschlüssel".



## Einen Wallet-Kanarienvogel erstellen



Der Canary Wallet ist ein Frühwarnsystem. Die Idee: Jeder in einem wallet-Multischlüssel verwendete Schlüssel kann auch in einem separaten wallet-Einzelschlüssel verwendet werden. Durch Hinterlegung eines kleinen Betrags auf diesem wallet "Kanarienvogel" signalisiert jede unbefugte Bewegung eine Kompromittierung des Schlüssels.



![Canary Wallets](assets/fr/09.webp)



Es gibt zwei Möglichkeiten, einen Wallet Canary zu konfigurieren. Drücken Sie auf der Registerkarte **Mehr** im Abschnitt "Schlüssel und Geldbörsen" auf **Kanarien-Geldbörsen**. Auf dem Bildschirm wird das Prinzip erklärt: Wenn jemand auf einen Ihrer Schlüssel zugreift und Guthaben auf dem zugehörigen wallet-Einzelschlüssel findet, wird er versuchen, dieses zu entfernen, was Sie alarmiert.



![Configuration Canary depuis une clé](assets/fr/10.webp)



Sie können den Canary auch direkt über eine Taste konfigurieren. Wählen Sie auf der Registerkarte **Tasten** eine Taste aus (z. B. Tapsigner Genesis), drücken Sie das Symbol **Einstellungen** (Zahnrad) und dann **Kanarienvogel Wallet**. Der zugehörige wallet-Kanarienvogel öffnet sich und ist bereit, einige Überwachungssatoshis zu empfangen.



Hinterlegen Sie auf jedem kanarischen Wallet einen kleinen Betrag (einige tausend Satoshis). Wenn diese Gelder ohne Ihre Zustimmung bewegt werden, entfernen Sie sofort den kompromittierten Schlüssel aus Ihren Multisig-Tresoren.



## Bewährte Praktiken



**Testen Sie Ihre Konfiguration** mit einem kleinen Geldbetrag, bevor Sie eine größere Summe einzahlen. Schicken Sie ein paar tausend Satoshis in den Tresor und versuchen Sie dann eine ausgehende Ausgabe, um zu prüfen, ob Sie den Signiervorgang mit jedem Gerät beherrschen. Testen Sie auch das Importieren der Konfigurationsdatei auf einem anderen Telefon, um sicherzustellen, dass die Sicherung funktioniert.



**Verteilen Sie die Schlüssel intelligent**. Bei Tapsignern übergeben Sie sie in einem versiegelten Umschlag, wobei die PIN separat mitgeteilt wird (z. B. in dem an anderer Stelle aufbewahrten Schreiben mit den Wiederherstellungsanweisungen). Bei klassischen Hardware-Geldbörsen bewahren Sie das Gerät bei einer vertrauenswürdigen Drittperson und den seed auf Papier oder Metall bei sich oder einer anderen Drittperson auf. Notieren Sie den Fingerabdruck jedes Schlüssels und seinen Namen in der Konfigurationsdatei, um Verwechslungen zu vermeiden.



**Planen Sie regelmäßige Tests** (Brandschutzübungen). Prüfen Sie jährlich, ob Sie den Tresor anhand von Sicherungskopien auf einem leeren Telefon wiederherstellen können. Testen Sie Canary-Warnungen, indem Sie den Kontostand überprüfen. Simulieren Sie Verlustszenarien ("Was ist, wenn ich die Coldcard verliere?"), um zu bestätigen, dass die verbleibenden Schlüsselkombinationen ausreichend sind.



**Vergessen Sie nicht die Aktualisierung**. Wenn Sie Ihren Vererbungsschlüssel auf 1 Jahr eingestellt haben, aktualisieren Sie ihn alle 9-10 Monate. Das ist der Preis, den Sie für die automatische Übertragung ohne Eingreifen Dritter zahlen.



**Halten Sie den Plan auf dem neuesten Stand**. Jede Änderung (Austausch eines Schlüssels, Änderung der Erben, Änderung der Frist) muss in allen Sicherungen und Dokumenten berücksichtigt werden. Generieren Sie die PDFs nach jeder Änderung neu und verteilen Sie die neuen Versionen weiter.



## Grenzen und Überlegungen



Trotz der Leistungsfähigkeit dieser Tools ist es wichtig, ihre Grenzen zu erkennen, um sie so effektiv wie möglich zu nutzen.



Die **Komplexität** eines Multisig-Tresors mit Zeitschaltern kann ein Risiko an sich sein: Fehlkonfiguration, Missverständnis durch die Erben, Verlust eines kritischen Elements unter den vielen Komponenten. Bitcoin Keeper vereinfacht die Erfahrung so weit wie möglich, aber es bleibt eine technische Operation. Setzen Sie diesen Plan nur ein, wenn der zu schützende Betrag dies rechtfertigt. Bei kleinen Beträgen kann ein einfacherer Plan ausreichen.



Die **Anwendungsabhängigkeit** ist eine Überlegung wert. Obwohl der Code quelloffen ist und auf offenen Standards (Miniscript, BSMS) basiert, sind bestimmte Funktionalitäten vom Keeper-Ökosystem abhängig. Bewahren Sie eine Kopie der Anwendung (Android APK oder iOS IPA) auf und dokumentieren Sie in Ihren Briefen an die Erben die Möglichkeit, andere Miniscript-kompatible Geldbörsen (wie Liana) zu verwenden, um Gelder zurückzuholen.



Vertrauensmakler** stellen ein menschliches Risiko dar. Was passiert, wenn ein böswilliger Verwandter den ihm anvertrauten Schlüssel vor Ablauf der Frist benutzt? Oder wenn der Anwalt Ihre Dokumente verlegt? Wählen Sie diese Personen sorgfältig aus, klären Sie sie über ihre Verantwortlichkeiten auf und haben Sie einen Plan B. Canary Wallets, redundante Backups und die Struktur von Multisig sind nach wie vor Ihr bester Schutz gegen diese Gefahren.



## Schlussfolgerung



Bitcoin Keeper bietet mit seinem Diamond Hands-Plan einen kompletten Werkzeugkasten für die Nachlassplanung: Erweiterte Tresore mit zeitgesteuerten Schlüsseln, Begleitdokumente, Canary Wallets und persönliche Betreuung.



Es ist mehr als nur eine technische Frage: Es geht darum, die Architektur Ihres Nachlasses zu entwerfen, die Schlüssel und das Wissen intelligent zu verteilen und das System regelmäßig zu testen. Ein gut durchdachter Bitcoin-Nachlassplan verwandelt Ihre Satoshis in ein echtes, übertragbares Erbe.