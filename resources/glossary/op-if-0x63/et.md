---
term: OP_IF (0X63)
---

Täidab skripti järgmise osa, kui väärtus virna tipus on mitte-null (tõene). Kui väärtus on null (väär), jäetakse need toimingud vahele, liikudes otse `OP_ELSE` järel toimuvatele toimingutele, kui see on olemas. `OP_IF` võimaldab skriptis tingimusliku kontrollstruktuuri käivitamist. See määrab skriptis kontrolli voo tingimuse alusel, mis on esitatud tehingu täitmisel. `OP_IF` kasutatakse koos `OP_ELSE` ja `OP_ENDIF`-iga järgmisel viisil:

```text
<tingimus>
OP_IF
<toimingud, kui tingimus on tõene>
OP_ELSE
<toimingud, kui tingimus on väär>
OP_ENDIF
```