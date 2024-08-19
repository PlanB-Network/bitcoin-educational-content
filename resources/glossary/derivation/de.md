---
term: DERIVATION
---

Bezieht sich auf den Prozess der Erzeugung von Kind-Schlüsselpaaren aus einem Eltern-Schlüsselpaar (privater Schlüssel und öffentlicher Schlüssel) und einem Ketten-Code innerhalb einer deterministischen und hierarchischen (HD) Wallet. Dieser Prozess ermöglicht die Segmentierung von Zweigen und die Organisation einer Wallet in verschiedene Ebenen mit zahlreichen Kind-Schlüsselpaaren, die alle durch das Wissen nur der grundlegenden Wiederherstellungsinformationen (die mnemonische Phrase und jede potenzielle Passphrase) wiederhergestellt werden können. Um einen Kind-Schlüssel abzuleiten, wird die Funktion `HMAC-SHA512` verwendet mit dem Eltern-Ketten-Code und der Verkettung des Eltern-Schlüssels und eines 32-Bit-Index. Es gibt zwei Arten von Ableitungen:
* Normale Ableitung, die den öffentlichen Schlüssel der Eltern als Basis der `HMAC-SHA512` Funktion verwendet;
* Verstärkte Ableitung, die den privaten Schlüssel der Eltern als Basis der `HMAC-SHA512` Funktion verwendet;

Das Ergebnis von HMAC-SHA512 wird in zwei Teile geteilt: die ersten 256 Bits werden zum Kind-Schlüssel (privat oder öffentlich nach Verarbeitung durch ECDSA), und die verbleibenden 256 Bits werden zum Kind-Ketten-Code.