---
term: POLÍTICA (MINISCRIPT)

---
Lenguaje de alto nivel orientado al usuario que permite especificar de forma sencilla las condiciones en las que se puede desbloquear un UTXO en el marco de Miniscript. La política es una descripción abstracta de las normas de gasto. A continuación, puede compilarse en miniscript, que es un equivalente uno a uno con las operaciones del lenguaje de script nativo de Bitcoin.

![](../../dictionnaire/assets/30.webp)

El lenguaje de políticas es ligeramente diferente del lenguaje miniscript. Por ejemplo, imagina un sistema de seguridad con una ruta primaria que es la clave A y una ruta de recuperación que es la clave B, pero con un bloqueo temporal de un año (aproximadamente 52.560 bloques). En política, esto sería:

```plaintext
or(pk(A),and(pk(B),older(52560)))
```

Una vez compilado en miniscript, sería:

```plaintext
andor(pk(B),older(52560),pk(A))
```

Y una vez convertido en escritura nativa, lo sería:

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