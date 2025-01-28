---
term: BIP119

---
Võtab kasutusele uue opkoodi nimega `OP_CHECKTEMPLATEVERIFY` (CTV). CTV võimaldaks luua tehingutes mittetagasiirduvaid kokkuleppeid, et kehtestada konkreetsed tingimused, kuidas antud mündi saab kulutada, sealhulgas tulevastes tehingutes. Konkreetsemalt öeldes võimaldaks see määratleda tingimusi tehingu väljundite "scriptPubKey" kohta, mis põhinevad sisendina kasutatud UTXO "scriptPubKey"-l. CheckTemplateVerify on kavandatud lihtsaks ja ilma dünaamilise olekuta. Selle rakendamise eesmärk on laiendada Bitcoini skriptimisvõimalusi, et hõlbustada erinevaid rakendusi, näiteks tehingu ülekoormuse kontrolli, mitteinteraktiivsete maksekanalite, DLC-de, maksekogumite loomist... See uus opkood võetakse kasutusele `OP_NOP4` asendajana. See muudatus tähendaks pehmet hargnemist.