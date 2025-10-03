---
name: Electrum OP_RETURN
description: Registrieren Sie eine Nachricht über den Blockchain Bitcoin mit Electrum
---

![cover](assets/cover.webp)




Diese schrittweise Anleitung zeigt Ihnen, wie Sie eine Nachricht auf dem Blockchain Bitcoin unter Verwendung des Wallet Electrum schreiben. Bei diesem Vorgang wird die Anweisung OP_RETURN verwendet, um Text in eine Transaktion einzufügen, die auf dem Blockchain öffentlich sichtbar ist. Befolgen Sie diese einfachen Schritte für eine erfolgreiche Registrierung.



---
## Voraussetzungen





- Einen Computer (Windows, macOS oder Linux).
- Internetverbindung.
- Ein paar Satoshis (Sats) oder Bitcoins (BTC) in Ihrem Wallet, um den Transaktionsbetrag und die Gebühren zu decken.
- Ein Text-zu-Hex-Konverter (z. B. eine Online-Seite) oder ein spezielles Tool wie [dieser OP_RETURN-Skriptgenerator] (https://resources.davidcoen.it/opreturnelectrum/).



---

## Schritt 1: Electrum herunterladen und installieren



![image](assets/fr/01.webp)



1. Besuchen Sie die offizielle Electrum-Website: [electrum.org](https://electrum.org/).


2. Laden Sie die Version herunter, die Ihrem Betriebssystem entspricht (Windows, macOS, Linux).


3. Installieren Sie Electrum gemäß den Anweisungen des Installationsprogramms.


4. Überprüfen Sie die Integrität der heruntergeladenen Datei (optional, aber aus Sicherheitsgründen empfohlen), indem Sie die Signatur der Datei oder Hash vergleichen.



→ Weitere Einzelheiten zum Electrum-Tutorial :



https://planb.network/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177


---

## Schritt 2: Erstellen oder Importieren eines Wallet



1. Electrum starten.


2. Wählen Sie Neues Wallet erstellen oder Vorhandenes Wallet wiederherstellen, wenn Sie bereits eine seed-Phrase (Wiederherstellungsphrase) haben.


3. Folgen Sie den Anweisungen, um Ihr Wallet zu konfigurieren:




 - Bei einem neuen Wallet notieren Sie sich Ihren seed-Satz und bewahren Sie ihn an einem sicheren Ort auf (Papier, Safe usw.).
 - Bei einem vorhandenen Wallet geben Sie Ihren seed-Satz ein, um ihn wiederherzustellen.


4. Legen Sie ein Passwort fest, um Ihr Wallet zu sichern.



→ Weitere Einzelheiten zum Electrum-Tutorial :



https://planb.network/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177


---

## Schritt 3: Verfügbare Mittel prüfen



Stellen Sie sicher, dass Ihr Wallet genug Bitcoins (BTC) oder Satoshis (Sats) enthält, um :




- Transaktionsbetrag (zum Beispiel 0,00001 BTC oder 1000 Sats).
- Transaktionsgebühren, die je nach Größe des Netzes variieren (im Allgemeinen einige tausend Sats).



Überprüfen Sie den Kontostand in Electrum, um Ihr Guthaben zu überprüfen.



![image](assets/fr/02.webp)



Überweisen Sie bei Bedarf BTC oder Sats, um Ihren Wallet zu füttern. Gehen Sie dazu auf die Registerkarte "Empfangen" und klicken Sie auf "Anfrage erstellen":



![image](assets/fr/03.webp)



Hier wird ein Empfang Address angezeigt:



![image](assets/fr/04.webp)



→ Weitere Einzelheiten zum Electrum-Tutorial :



https://planb.network/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177


---

## Schritt 4: Vorbereiten der zu beschriftenden Nachricht



Wählen Sie die Nachricht, die Sie eingeben möchten (z. B. "Danke Satoshi"). Hinweis: OP_RETURN-Nachrichten sind auf 80 Bytes, d. h. etwa 80 ASCII-Zeichen, begrenzt.



*Denken Sie einen Moment nach: Was Sie auf den Blockchain Bitcoin schreiben, ist für die Ewigkeit und für alle zugänglich, also :*




- einen schönen Ausdruck unserer Menschlichkeit hinterlassen,
- vermeiden Sie die Eingabe von Inhalten, die Sie möglicherweise bereuen



*Blockchain-Speicherplatz und Ihre Bitcoins sind kostbar, nutzen Sie sie weise und mit Absicht*



Konvertieren Sie Ihre Nachricht in hexadezimale Werte:




- Sie können ein [Online-Tool] (https://www.rapidtables.com/convert/number/ascii-to-hex.html) verwenden, sollten aber darauf achten, dass dort keine sensiblen Daten verarbeitet werden (obwohl Informationen, die zur Veröffentlichung auf Blockchain Bitcoin über ein OP_RETURN bestimmt sind, im Prinzip keine Probleme mit der Vertraulichkeit aufwerfen);
- Um die Vertraulichkeit zu erhöhen, führen Sie die Konvertierung lokal mit einer kleinen Python :



```py
#!/usr/bin/env python3

def main():
ascii_text = input("Enter ASCII text: ")
try:
hex_output = ascii_text.encode('ascii').hex()
print(hex_output)
except UnicodeEncodeError:
print("Error: Input contains non-ASCII characters.", file=sys.stderr)

if __name__ == "__main__":
import sys
main()
```



Beispiel: `Danke Satoshi` in ASCII ergibt `5468616e6b73205361746f736869` in Hexadezimal.



Bereiten Sie das Transaktionsskript vor. Hier ist ein Beispiel für das erwartete Format:



```script
bc1q879cv4p5q6s9537orange3zss33d3turzad8, 0.00001
script(OP_RETURN 5468616e6b73205361746f736869), 0
```



die sich zusammensetzt aus :





- **Ziel Address**: Ein gültiger Bitcoin Address. Ici, `bc1q879cv4p5q6s9537orange3zss33d3turzad8`. Dies kann Ihr eigener Address sein, wenn Sie die überwiesenen Mittel an sich selbst zurückgeben möchten;
- **Überwiesener Betrag**: der Betrag der Transaktion, hier `0.00001` BTC. **Bitte beachten**: Da die in Electrum verwendete Einheit BTC ist, muss der im Transaktionsskript angegebene Betrag auch in BTC und nicht in Sats ausgedrückt werden;
- **Skript OP_RETURN**: Die in hexadezimale Werte umgewandelte Nachricht mit vorangestelltem Script(`OP_RETURN <Messsage>), 0`. Hier, `5468616e6b73205361746f736869` für die Nachricht in Hexadezimal.



⚠️ **Vorsicht**: Es ist sehr wichtig, nach dem OP_RETURN eine "0" anzugeben, da dieser Opcode das Skript als ungültig kennzeichnet und die Ausgabe dauerhaft unbrauchbar macht. Die Netzknoten löschen diese Ausgabe aus ihrem UTXO-Satz. Wenn Sie einen anderen Wert als "0" eingeben, ist dieser unwiederbringlich verloren: Ihre Bitcoins gelten dann als verbrannt. Sie sollten daher bei einem OP_RETURN immer "0" eingeben, um die gewünschten Daten aufzuzeichnen, ohne damit Geldmittel zu verknüpfen, die dann verloren wären.



Tipp: Verwenden Sie das Tool [OP_RETURN Generator] (https://resources.davidcoen.it/opreturnelectrum/), um das generate-Skript automatisch zu erstellen. Auch wenn dieses Tool vorschlägt, den Betrag in BTC einzugeben, lassen Sie die Einheit in Electrum konfiguriert.



![image](assets/fr/05.webp)



Um die von Electrum verwendete Einheit zu ändern, wählen Sie in der Menüleiste "Einstellungen" und dann auf der Registerkarte "Einheiten" BTC / mBTC / Bits oder Sats aus:



![image](assets/fr/06.webp)




---

## Schritt 5: Absenden der Transaktion



Gehen Sie in Electrum auf die Registerkarte Senden.



![image](assets/fr/07.webp)



Fügen Sie das vorbereitete Skript (z. B. das obige) in das Feld "Bezahlen an" ein.



![image](assets/fr/08.webp)



Das Feld "Zahlbar an" sollte in Green angezeigt werden, und der Transaktionsbetrag sollte in der Zeile darunter erscheinen.



Überprüfen Sie den Betrag und seine Einheit im Feld Betrag.



Klicken Sie auf "Bezahlen..." und passen Sie Ihre Transaktionsgebühren entsprechend dem Betrag an, den Sie zu zahlen bereit sind, und der Geschwindigkeit, mit der Ihre Transaktion von einem Miner bearbeitet und in einen Block integriert werden soll.



![image](assets/fr/09.webp)



Klicken Sie auf OK und bestätigen Sie die Transaktion mit Ihrem Passwort. Ein Bestätigungsfenster wird angezeigt.




---

## Schritt 6: Überprüfung der Registrierung



Sobald die Transaktion bestätigt wurde (dies kann einige Minuten dauern), gehen Sie auf die Registerkarte "Verlauf".



![image](assets/fr/10.webp)



Klicken Sie mit der rechten Maustaste auf die Transaktion und wählen Sie "Im Explorer anzeigen", um die Details zu sehen.



Alternativ können Sie den Ziel-Address (z. B. `bc1q879cv4p5q6s9537orange3zss33d3turzad8`) kopieren und auf einem Blockchain-Explorer wie [Mempool.space](https://Mempool.space/) oder [blockstream.info](https://blockstream.info/) anzeigen.



Suchen Sie in den Transaktionsdetails das Feld OP_RETURN, um Ihre Nachricht zu sehen.



![image](assets/fr/11.webp)




![image](assets/fr/12.webp)




---

## Tipps und bewährte Verfahren





- Testen Sie mit einem kleinen Betrag: Beginnen Sie mit einer kleinen Transaktion (z. B. Sats 1000), um kostspielige Fehler zu vermeiden.
- Vergewissern Sie sich, dass die Ausgabe, die OP_RETURN enthält, gleich Null ist, sonst sind Ihre Bitcoins dauerhaft verloren.
- Überprüfen Sie die Einheit: Vergewissern Sie sich, dass der eingegebene Betrag mit der in Electrum angezeigten Einheit (BTC, mBTC oder Sats) übereinstimmt.
- Transaktionsgebühr: Wenn das Netzwerk überlastet ist, erhöhen Sie die Gebühr für eine schnellere Bestätigung.
- Kurze Nachricht: OP_RETURN-Einträge sind auf 80 Bytes begrenzt. Planen Sie Ihre Nachricht entsprechend.



---

## Nützliche Ressourcen





- Electrum herunterladen: [electrum.org](https://electrum.org/)
- OP_RETURN Skript-Generator: [resources.davidcoen.it/opreturnelectrum/](https://resources.davidcoen.it/opreturnelectrum/)
- Blockchain Entdecker: [Mempool.space](https://Mempool.space/), [blockstream.info](https://blockstream.info/)