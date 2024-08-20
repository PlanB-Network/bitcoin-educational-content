---
term: POLICY (MINISCRIPT)
---

Un lenguaje de alto nivel y orientado al usuario que permite la especificación simple de condiciones bajo las cuales un UTXO puede ser desbloqueado dentro del marco de Miniscript. La política es una descripción abstracta de las reglas de gasto. Luego, puede ser compilada en miniscript, que es un equivalente uno a uno con operaciones del lenguaje de script nativo de Bitcoin.

![](../../dictionnaire/assets/30.png)

El lenguaje de política es ligeramente diferente del lenguaje miniscript. Por ejemplo, imagina un sistema de seguridad con un camino primario siendo la llave A, y un camino de recuperación siendo la llave B, pero bajo un bloqueo de tiempo de un año (aproximadamente 52,560 bloques). En política, esto sería:

```plaintext
or(pk(A),and(pk(B),older(52560)))
```

Una vez compilado en miniscript, sería:

```plaintext
andor(pk(B),older(52560),pk(A))
```

Y una vez convertido en script nativo, sería:

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