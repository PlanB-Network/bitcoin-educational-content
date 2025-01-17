---
term: POLICY (MINISCRIPT)
---

Langage de haut niveau orienté utilisateur permettant de spécifier simplement des conditions sous lesquelles un UTXO peut être débloqué dans le cadre de Miniscript. La policy est une description abstraite des règles de dépense. Elle peut ensuite être compilée en miniscript, qui est équivalent un pour un avec des opérations du langage script natif de Bitcoin. 

![](../../dictionnaire/assets/30.webp)

Le langage de policies est légèrement différent du langage miniscript. Par exemple, imaginons un système de sécurisation avec en chemin primaire, la clé A, et en chemin de récupération, la clé B, mais sous un timelock d'un an (environ 52 560 blocs). En policy, cela donnerait :

```plaintext
or(pk(A),and(pk(B),older(52560)))
```

Une fois compilé en miniscript, cela donnerait : 

```plaintext
andor(pk(B),older(52560),pk(A))
```

Et une fois converti en script natif, cela donnerait :

```plaintext
<B>
OP_CHECKSIG
OP_NOTIF
<A>
OP_CHECKSIG
OP_ELSE
<50cd00>
OP_CHECKSEQUENCEVERIFY
OP_ENDIF
```


