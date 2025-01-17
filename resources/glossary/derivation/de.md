---
term: DERIVATION

---
Bezieht sich auf den Prozess der Erzeugung von Kind-Schlüsselpaaren aus einem Eltern-Schlüsselpaar (privater Schlüssel und öffentlicher Schlüssel) und einem Kettencode innerhalb einer deterministischen und hierarchischen (HD) Brieftasche. Dieser Prozess ermöglicht die Segmentierung von Zweigen und die Organisation einer Brieftasche in verschiedene Ebenen mit zahlreichen untergeordneten Schlüsselpaaren, die alle wiederhergestellt werden können, wenn man nur die grundlegenden Wiederherstellungsinformationen (die mnemonische Phrase und eine mögliche Passphrase) kennt. Zur Ableitung eines untergeordneten Schlüssels wird die Funktion `HMAC-SHA512` mit dem übergeordneten Kettencode und der Verkettung des übergeordneten Schlüssels und eines 32-Bit-Index verwendet. Es gibt zwei Arten von Ableitungen:


- Normale Ableitung, bei der der übergeordnete öffentliche Schlüssel als Grundlage für die Funktion `HMAC-SHA512` verwendet wird;
- Gehärtete Ableitung, die den übergeordneten privaten Schlüssel als Grundlage für die Funktion `HMAC-SHA512` verwendet;

Das Ergebnis von HMAC-SHA512 wird in zwei Teile geteilt: Die ersten 256 Bits werden zum Child-Schlüssel (privat oder öffentlich nach der Verarbeitung durch ECDSA), und die restlichen 256 Bits werden zum Child-Chain-Code.