---
term: OP_IF (0X63)

---
Käivitab skripti järgmise osa, kui virna ülaosas olev väärtus ei ole null (true). Kui väärtus on null (false), jäetakse need operatsioonid vahele ja minnakse otse nende juurde, mis järgnevad `OP_ELSE`-le, kui see on olemas. `OP_IF` võimaldab skripti sees tingimusliku juhtimisstruktuuri käivitamist. See määrab skripti kontrollivoolu, mis põhineb tehingu täitmise ajal esitatud tingimusel. `OP_IF` kasutatakse koos `OP_ELSE` ja `OP_ENDIF`ga järgmiselt:

```text
<condition>
OP_IF
<operations if the condition is true>
OP_ELSE
<operations if the condition is false>
OP_ENDIF
```