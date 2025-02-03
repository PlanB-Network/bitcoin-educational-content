---
term: CHAVE PÚBLICA COMPRIMIDA

---
Uma chave pública é utilizada em scripts (quer diretamente na forma de uma chave pública ou como um endereço) para receber e proteger bitcoins. Uma chave pública bruta é representada por um ponto numa curva elíptica, consistindo em duas coordenadas (`x, y`), cada uma com 256 bits. Em formato bruto, uma chave pública mede, portanto, 512 bits, sem contar o byte adicional para identificar o formato. Uma chave pública comprimida, por outro lado, é uma forma mais compacta de representação de chave pública. Utiliza apenas a coordenada `x` e um prefixo (`02` ou `03`) que indica a paridade da coordenada `y` (par ou ímpar).

Se simplificarmos isto para o campo dos números reais, dado que a curva elíptica é simétrica em relação ao eixo x, para qualquer ponto $P$ (`x, y`) na curva, existe um ponto $P'$ (`x, -y`) que também estará nessa mesma curva. Isto significa que para cada `x`, existem apenas dois valores possíveis de `y`, positivo e negativo. Por exemplo, para uma dada abcissa `x`, existiriam dois pontos $P1$ e $P2$ na curva elíptica, partilhando a mesma abcissa mas com ordenadas opostas:

![](../../dictionnaire/assets/29.webp)

Para escolher entre os dois pontos potenciais da curva, um prefixo especificando qual `y` escolher é adicionado a `x`. Este método permite reduzir o tamanho de uma chave pública de 520 bits para apenas 264 bits (8 bits do prefixo + 256 bits para `x`). Esta representação é conhecida como a forma comprimida da chave pública.

No entanto, no contexto da criptografia de curva elíptica, não usamos os números reais, mas um campo finito de ordem `p` (um número primo). Neste contexto, o "sinal" de `y` é determinado pela sua paridade, ou seja, se `y` é par ou ímpar. O prefixo `0x02` indica então um `y` par, enquanto que `0x03` indica um `y` ímpar.

Considere o seguinte exemplo de uma chave pública em bruto (um ponto na curva elíptica) em hexadecimal:

```plaintext
K = 04678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb649f
6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5f
```

Podemos isolar o prefixo, `x`, e `y`:

```plaintext
Prefix = 04
To determine the parity of `y`, we examine the last hexadecimal character of `y`:
```

Base 16 (hexadecimal): f

Base 10 (decimal): 15

y é ímpar

```
The prefix for the compressed public key will be `03`. The compressed public key in hexadecimal becomes:
```

K = 03678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb6

```