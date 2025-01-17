---
term: OP_NUMEQUALVERIFY (0X9D)

---
Kombinerer operasjonene `OP_NUMEQUAL` og `OP_VERIFY`. Den sammenligner de to øverste elementene i stakken numerisk. Hvis verdiene er like, fjerner `OP_NUMEQUALVERIFY` det sanne resultatet fra stakken og fortsetter kjøringen av skriptet. Hvis verdiene ikke er like, blir resultatet false, og skriptet mislykkes umiddelbart.