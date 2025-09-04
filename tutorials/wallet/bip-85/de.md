---
name: BIP-85
description: Wie kann ich das BIP-85 verwenden, um mehrere Seedphrases von einem Haupt-seed zu generate zu machen?
---
![cover](assets/cover.webp)



## 1. Das BIP-85 verstehen



### 1.1 Was ist BIP-85?



BIP-85 ist eine erweiterte Funktion, mit der Sie mehrere **seed-Nebenphrasen** aus einer **seed-Hauptphrase** erstellen können.



Jeder seed-Sekundärsatz kann verwendet werden, um ein völlig unabhängiges Bitcoin-Portfolio zu erstellen. Diese Portfolios können für eine Vielzahl von Zwecken verwendet werden: ein Hot Wallet auf dem Handy, ein Portfolio für einen Verwandten, ein separates Sparportfolio usw.



Alle seed-Unterphrasen sind **mathematisch abgeleitet**, aber es ist **unmöglich, von einer Unterphrase auf die seed-Hauptphrase** zurückzugehen. Dies gewährleistet eine vollständige Trennung zwischen den einzelnen Portfolios.



Solange Sie Zugriff auf Ihren seed-Hauptsatz (und den zugehörigen passphrase, falls Sie einen verwenden) haben, können Sie jeden seed-Nebensatz **identisch** neu generieren, ohne ihn separat speichern zu müssen.



### 1.2 Warum BIP-85 verwenden?



BIP-85 ist nützlich, wenn Sie :





- Erstellen Sie mehrere unabhängige Bitcoin-Portfolios ohne mehrere Backups
- Verwalten Sie Ihr Geld nach verschiedenen Verwendungszwecken (Sparen, Ausgaben, Familie, Projekte)
- Gewährleistung von Schutzmaßnahmen für Angehörige ("Onkel Jim"-Funktion)
- Löschen Sie ein Portfolio, ohne den Zugriff auf Ihre Fonds zu verlieren
- Vereinfachen Sie Ihre Sicherheit: nur eine seed-Schlüsselphrase zum Schutz



### 1.3 Vorteile gegenüber BIP-32



Mit BIP-32 kann ein einziger seed-Satz verwendet werden, um eine vollständige Hierarchie von Bitcoin-Konten und -Adressen mit Hilfe von Ableitungspfaden (zum Beispiel: "m/44'/0'/0'/0/0") zu bilden. Jeder Pfad kann ein eigenes Konto darstellen, aber **alle bleiben mit demselben seed-Satz verknüpft**. Wenn also dieser seed-Satz kompromittiert wird, werden **alle abgeleiteten Konten zugänglich**.



Mit BIP-85 kann ein seed-Hauptsatz verwendet werden, um mehrere völlig unabhängige seed-Nebensätze zu erzeugen: **Wenn einer dieser sekundären Sätze kompromittiert wird, kann der Angreifer niemals zum Haupt-seed zurückkehren oder auf die anderen Portfolios zugreifen**.


Dies ermöglicht eine Aufteilung der Risiken:





- Sie können ein sekundäres seed für Hot Wallet oder eine vorübergehende Verwendung verwenden und dabei eine höhere Belastung in Kauf nehmen.
- Selbst wenn dieser Hot Wallet kompromittiert wird, bleiben Ihre anderen Gelder, die durch andere sekundäre Seeds geschützt oder offline gehalten werden, **sicher**.



Andererseits sind sowohl bei BIP-32 als auch bei BIP-85 **alle Fonds angreifbar**, wenn das Haupt-seed kompromittiert wird. Daher ist es von entscheidender Bedeutung, ihn mit der höchsten Sicherheitsstufe zu schützen.



![image](assets/fr/02.webp)


## 2. Praktische Anwendungsfälle für BIP-85



BIP-85 ermöglicht es Ihnen, mehrere Bitcoin-Portfolios aus einem einzigen seed-Kernsatz zu erstellen, jedes mit seinem eigenen seed-Sekundärsatz. Hier sind fünf praktische Anwendungsfälle für die Organisation und Sicherung Ihrer Bitcoin-Fonds. Jeder Fall erklärt, warum die Verwendung von BIP-85 praktischer ist als die Verwaltung mehrerer Konten mit einem einzigen seed-Satz über BIP-32.



### 2.1 Begrenzung des Risikos eines unsicheren Portfolios





- Szenario**: Sie verwenden einen "Hot Wallet" Wallet (installiert auf einem mit dem Internet verbundenen Gerät) für tägliche Transaktionen.
- Lösung BIP-85**: Sie erstellen einen sekundären seed-Satz für dieses Portfolio.
- Vorteil gegenüber BIP-32**: Sie müssen den seed-Primärsatz nicht in Ihr Telefon importieren, wodurch das Risiko eines Hackerangriffs verringert wird. Nur der seed-Sekundärsatz ist gefährdet und schützt Ihre anderen Geldbörsen. Bei BIP-32 müssen Sie die seed-Hauptphrase und einen Umgehungspfad verwenden, wodurch alle Ihre Geldmittel offengelegt werden.



### 2.2 Erstellen Sie ein Portfolio für ein Familienmitglied





- Szenario**: Sie richten für eine Ihnen nahestehende Person (z. B. Ihre Mutter) einen Bitcoin Wallet ein und können ihn wiedererlangen, wenn sie ihn verliert.
- Lösung BIP-85**: Sie erstellen einen eigenen seed-Sekundärsatz und teilen nur diesen.
- Vorteil gegenüber BIP-32**: Bei BIP-32 muss man bei der Einrichtung eines Kontos für einen geliebten Menschen entweder seinen Haupt-seed-Satz mitbenutzen, wodurch man sein gesamtes Guthaben riskiert und die Verwaltung für den geliebten Menschen erschwert (Verwaltung von Verzweigungspfaden), oder einen neuen seed-Satz anlegen, den man zusätzlich zu seinem Haupt-seed-Satz speichert.



### 2.3 Erleichterung der Verwaltung von getrennten Portfolios





- Szenario**: Sie trennen Ihre Bitcoins für verschiedene Zwecke (z. B. langfristige Ersparnisse, Nicht-KYC-Fonds).
- Lösung BIP-85**: Sie erstellen seed sekundäre Phrasen für jedes Ziel.
- Vorteil gegenüber BIP-32**: Bei BIP-32 teilen sich alle Konten denselben seed-Satz, was die Verwaltung in Portfolios von Drittanbietern erschwert, da Ableitungspfade wie `m/44'/0'/0'` verwaltet werden müssen. Außerdem ist es nicht möglich, jedem Gerät ein eigenes Konto zuzuweisen (z. B. "Sparen auf Coldcard", "täglich auf Handy", "Urlaub auf Trezor"). BIP-85 weist jedem Ziel eine eindeutige seed-Sekundärphrase zu, die leicht zu identifizieren ist und für jedes Gerät separat importiert werden kann.



### 2.4 Verwendung eines temporären Wallet für Transaktionen





- Szenario**: Sie benötigen ein temporäres Portfolio für eine einmalige Transaktion oder zur Wahrung der Vertraulichkeit (z. B.: Vermischung von Fonds, Interaktion mit einem Exchange KYC usw.).
- Lösung BIP-85**: Sie erstellen einen seed-Sekundärsatz, verwenden ihn für die Transaktion und vernichten ihn dann, wenn nötig, in dem Wissen, dass er wiederhergestellt werden kann.
- Vorteil gegenüber BIP-32**: Bei BIP-32 hängt ein temporäres Konto vom seed-Hauptsatz ab, so dass bei einer Kompromittierung alle Ihre Gelder gefährdet sind.





## 3. Bevor Sie beginnen





- Hardware** (optional)
 - Coldcard Mk4 oder Q1
 - MicroSD-Karte





- Grundlegende Kenntnisse
 - Mnemonic-Sätze verstehen (BIP-39): eine Liste von 12 bis 24 Wörtern zum Speichern eines Portfolios.
 - Wissen, was ein Bitcoin Wallet ist: Software oder Gerät zur Verwaltung Ihrer Bitcoins, und wie man es mit einem Mnemonic-Satz wiederherstellt.
 - Weitere Ressourcen in den Anhängen.





- Kompatible** Software
 - Sparrow wallet (Computer, für reine Überwachung oder erweiterte Verwaltung)
 - Nunchuck (mobil, für Mehrfachsignaturen)
 - BlueWallet (mobil)
 - ...





- 3.4 Coldcard**-Konfiguration
 - Initialisieren Sie einen seed-Satz mit 24 Wörtern auf der Coldcard.
 - Optional: Fügen Sie einen passphrase hinzu, um den Zugang zu BIP-85-Zweigstellen zu sichern.
 - Aktivieren Sie nützliche Optionen: NFC (für den Export), USB am Akku deaktivieren (Sicherheit).




## 4. Schritt-für-Schritt-Anleitung



Befolgen Sie diese Schritte, um ein sekundäres Mnemonic mit BIP-85 auf Ihrer Coldcard zu erstellen, zu verwenden und abzurufen.



### 4.1 generate a seed Nebensatz



Sie erstellen aus Ihrem seed-Hauptsatz einen seed-Nebensatz.


Schalten Sie Ihre Coldcard ein, geben Sie Ihren PIN-Code ein.





- 1. Wenn Sie einen passphrase an Ihrem Haupt-seed angebracht haben:**
 - Gehen Sie auf dem Startbildschirm zu "passphrase".
    - Wählen Sie "Wort hinzufügen" und geben Sie Ihr Passwort ein.
    - Drücken Sie "Anwenden".
    - Überprüfen Sie die Identität des Wallet: Gehen Sie zu "Erweitert > Identität anzeigen", um sich den Fingerabdruck des Wallet zu merken.





- 2. Zum Menü BIP-85** gehen
 - Gehen Sie auf dem Startbildschirm zu "Erweitert > seed B85 ableiten"
 - Lesen Sie die Warnung und bestätigen Sie sie.



Die ColdCard informiert Sie darüber, dass die erzeugten Seeds mathematisch von Ihrem Haupt-seed abgeleitet, aber kryptografisch völlig unabhängig sind.


![image](assets/fr/03.webp)





- 3. Wählen Sie ein Format


Wählen Sie das seed Phrasenformat: 12, 18 oder 24 Wörter. Prüfen Sie die Anzahl der Wörter, die der Wallet akzeptiert, in den Sie Ihren seed-Satz importieren möchten.


![image](assets/fr/04.webp)





- 4. Index auswählen
 - Geben Sie einen Index zwischen 0 und 9999 ein.
 - Dieser Index ist entscheidend für die spätere Regeneration des sekundären seed. Bewahren Sie ihn sorgfältig auf und beschriften Sie ihn wie folgt: "Index 1 = Wallet mobil", "Index 2 = Familienprojekt", "Index 4 = Testmischung", ...
 - Wenn Sie ihn verlieren, haben Sie zwar weiterhin Zugriff auf Ihr Guthaben, aber Sie müssen Kombinationen von 0 bis 9999 ausprobieren, um es zu finden.


![image](assets/fr/05.webp)





- 5. seed Nebensatz notieren oder exportieren**


ColdCard zeigt jetzt einen neuen seed Nebensatz an. Sie können :




 - Die **Note manuell**.
 - Presse:
     - 1", um sie auf der SD-Karte zu speichern
     - 2", um **den Modus "diesen seed verwenden "** auf der ColdCard zu aktivieren (nützlich zum Exportieren oder Signieren einer Transaktion)
     - 3", um einen **QR-Code** anzuzeigen (der mit einer mobilen Anwendung wie BlueWallet oder Nunchuck zu scannen ist)
     - 4", um es per **NFC** zu senden



💡 An diesem Punkt haben Sie einen unabhängigen seed-Satz, der in jedem Wallet BIP39 (Trezor, Ledger, BlueWallet, Nunchuck...) verwendet werden kann.


![image](assets/fr/06.webp)


![image](assets/fr/07.webp)


### 4.2 Verwendung des sekundären seed



Sie können nun diese abgeleitete seed verwenden, um ein neues Portfolio in :




- eine mobile App
- ein weiterer Hardware Wallet
- ein Multisig-Portfolio



### 4.3 Wiederherstellen eines verlorenen seed-Sekundärsatzes



Um ein sekundäres seed zu einem beliebigen Zeitpunkt abzurufen, wiederholen Sie den Vorgang:


1. Starten Sie Ihre ColdCard neu


2. Geben Sie Ihre PIN ein


3. Geben Sie Ihren passphrase ein, falls definiert


4. Gehen Sie zu "Erweitert > seed B85 ableiten"


5. Format wählen (12/18/24 Wörter)


6. Geben Sie denselben Index ein (z. B. "1")


7. Sie erhalten genau das gleiche sekundäre seed




## 5. Grenzen, Risiken und bewährte Verfahren



### 5.1 Abhängigkeit von seed Hauptsatz + passphrase



Die Verwendung von BIP85 beruht vollständig auf dem 24-Wörter-Hauptsatz seed sowie auf passphrase, falls Sie einen solchen verwendet haben.




- Aus diesen beiden Elements können alle seed-Sekundärphrasen regeneriert werden.
- Ohne einen dieser 2 Elements verlieren Sie den Zugang zu allen Derivateportfolios.



### 5.2 Risiken bei der Konfiguration von Mehrfachsignaturen



Wir raten dringend davon ab, sekundäre seed-Phrasen, die aus derselben primären seed-Phrase generiert wurden, in einer multi-sig-Konfiguration zu verwenden: Wenn das Gerät oder die primäre seed-Phrase kompromittiert wird, können alle multi-sig-Schlüssel von einem Angreifer neu generiert werden.



### 5.3 Software-Kompatibilität



Nicht alle Anwendungen unterstützen die BIP85-Ableitung direkt. Die mit BIP85 erzeugten Seeds sind jedoch Standard-BIP39-Seeds (12, 18 oder 24 Wörter) und können daher in jedem BIP39-kompatiblen Portfolio verwendet werden.



### 5.4 BIP85-Kontoregister



Es wird empfohlen, ein aktuelles persönliches Verzeichnis der seed-Sekundärphrasen zu führen.




- Sie ermöglicht es Ihnen, schnell herauszufinden, welcher BIP85-Index welchem Portfolio entspricht, ohne dass Sie ständig seed-Sekundärphrasen verwenden müssen.
- Dieses Register sollte minimalistisch bleiben, ohne ausdrückliche Erwähnung von Bitcoin, und sollte getrennt vom Haupt-seed gespeichert werden. Denken Sie daran, es in Ihrem Nachlassplan zu erwähnen.



Das Register kann enthalten:




- bIP85-Index verwendet (Zahl von 0 bis 9999)
- einen Verwendungs- oder Referenznamen (z. B. Hot Wallet, persönliche Ersparnisse, Wallet von Mama)
- gegebenenfalls den Wallet-Fingerabdruck zur Überprüfung in ColdCard



### 5.5 Sicherung



Die Backups müssen enthalten:




- der Haupt-seed
- gW-76 (falls verwendet)



Niemals zusammen lagern:




- die wichtigsten seed und passphrase
- die Haupt-seed und das BIP85-Kontoregister



Weitere Ressourcen in den Anhängen.




## ANHÄNGE



## A.1 Glossar





- [BEEP](https://planb.network/resources/glossary/bip)
- [BIP-32] (https://planb.network/resources/glossary/bip0032)
- [BIP-39] (https://planb.network/resources/glossary/bip0039)
- [BIP-85](https://planb.network/resources/glossary/bip0085)
- [seed-Satz] (https://planb.network/resources/glossary/recovery-phrase)
- [passphrase] (https://planb.network/resources/glossary/passphrase-bip39)
- [Multisig] (https://planb.network/resources/glossary/multisig)




### A.2 Speichern Sie Ihre Wiederherstellungsphrase



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270


### A.3 Das Verständnis des passphrase BIP39



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7


### A.4 Wie Bitcoin-Portfolios funktionieren



https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f