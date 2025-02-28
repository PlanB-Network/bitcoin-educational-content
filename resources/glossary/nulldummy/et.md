---
term: NULLDUMMY

---
SegWit soft forki BIP147-ga kasutusele võetud konsensusreegel, mis nõuab, et opkoodides `OP_CHECKMULTISIG` ja `OP_CHECKMULTISIGVERIFY` kasutatav dummy-element oleks tühi baidimassiiv (`OP_0`). See meede võeti kasutusele, et kõrvaldada võltsimisvektor, keelates selle elemendi jaoks mis tahes muu väärtuse kui `OP_0`.