---
term: NULLDUMMY

---
Konsensusregel introdusert med BIP147 i SegWit soft fork som krever at dummy-elementet som brukes i opkodene `OP_CHECKMULTISIG` og `OP_CHECKMULTISIGVERIFY` skal være en tom byte-array (`OP_0`). Dette tiltaket ble implementert for å eliminere en manipulerbarhetsvektor ved å forby enhver annen verdi enn `OP_0` for dette elementet.