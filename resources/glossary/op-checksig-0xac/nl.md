---
term: OP_CHECKSIG (0XAC)
definition: Opcode die de geldigheid van een handtekening controleert ten opzichte van een openbare sleutel.
---

Verifieert de geldigheid van een handtekening tegen een gegeven openbare sleutel. Het neemt de bovenste twee Elements van de stack: de handtekening en de openbare sleutel, en evalueert of de handtekening correct is voor de transactie Hash en de opgegeven openbare sleutel. Als de verificatie succesvol is, duwt het de waarde `1` (true) op de stack, anders `0` (false). Deze opcode is aangepast in Tapscript om Schnorr-handtekeningen te verifiëren.