---
term: BIP8

---
BIP8 wurde im Anschluss an die Debatten über SegWit entwickelt, das BIP9 für seine Aktivierung nutzte. BIP8 ist eine Soft-Fork-Aktivierungsmethode, die von Haus aus einen automatischen UASF-Mechanismus (*User-Activated Soft Fork*) einschließt. Wie BIP9 nutzt BIP8 die Signalisierung der Miner, fügt aber den Parameter `LOT` (*Lock-in On Time out*) hinzu. Wenn `LOT` auf `true` gesetzt ist, wird nach Ablauf der Signalisierungsperiode ohne Erreichen des erforderlichen Schwellenwerts automatisch ein UASF ausgelöst und die Aktivierung der Soft Fork erzwungen. Dieser Ansatz zwingt die Miner zur Kooperation oder sie riskieren eine von den Nutzern auferlegte UASF. Darüber hinaus definiert BIP8 im Gegensatz zu BIP9 die Signalisierungsperiode auf der Grundlage der Blockhöhe, wodurch mögliche Manipulationen durch die Hash-Rate seitens der Miner ausgeschlossen werden. BIP8 ermöglicht auch die Festlegung einer variablen Abstimmungsschwelle und führt einen Parameter für eine Mindestblockhöhe für die Aktivierung ein, so dass die Miner Zeit haben, sich vorzubereiten und ihre Zustimmung im Voraus zu signalisieren, ohne unbedingt bereit zu sein. Wenn eine Soft Fork über BIP8 mit dem Parameter "LOT=true" aktiviert wird, wird eine sehr aggressive Methode gegen Miner angewandt, die sofort unter den Druck eines potenziellen UASF gesetzt werden. In der Tat lässt es ihnen nur 2 Möglichkeiten:


- Seien Sie kooperativ und erleichtern Sie so den Aktivierungsprozess;
- Unkooperativ sein, in diesem Fall führen die Benutzer automatisch eine UASF durch, um die Soft Fork zu erzwingen.