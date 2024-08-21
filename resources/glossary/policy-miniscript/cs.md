---
term: POLICY (MINISCRIPT)
---

Vysokoúrovňový, uživatelsky orientovaný jazyk, který umožňuje jednoduchou specifikaci podmínek, za kterých lze UTXO odemknout v rámci frameworku Miniscript. Policy je abstraktní popis pravidel pro výdaje. Poté může být zkompilována do miniscriptu, který je jednoznačně ekvivalentní s operacemi z nativního skriptovacího jazyka Bitcoinu.

![](../../dictionnaire/assets/30.png)

Jazyk policy se mírně liší od jazyka miniscript. Představte si například bezpečnostní systém s primární cestou klíčem A a záložní cestou klíčem B, ale pod časovým zámkem jednoho roku (přibližně 52 560 bloků). V policy by to bylo:

```plaintext
or(pk(A),and(pk(B),older(52560)))
```

Po kompilaci do miniscriptu by to bylo:

```plaintext
andor(pk(B),older(52560),pk(A))
```

A po převedení do nativního skriptu by to bylo:

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