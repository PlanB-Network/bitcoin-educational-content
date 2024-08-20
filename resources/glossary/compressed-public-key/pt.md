---
term: CHAVE PÚBLICA COMPACTADA
---

Uma chave pública é usada em scripts (diretamente na forma de uma chave pública ou como um endereço) para receber e proteger bitcoins. Uma chave pública bruta é representada por um ponto em uma curva elíptica, consistindo de duas coordenadas (`x, y`) cada uma com 256 bits. No formato bruto, uma chave pública mede, portanto, 512 bits, sem contar o byte adicional para identificar o formato. Uma chave pública compactada, por outro lado, é uma forma mais compacta de representação da chave pública. Ela usa apenas a coordenada `x` e um prefixo (`02` ou `03`) que indica a paridade da coordenada `y` (par ou ímpar).

Se simplificarmos isso para o campo dos números reais, dado que a curva elíptica é simétrica em relação ao eixo x, para qualquer ponto $P$ (`x, y`) na curva, existe um ponto $P'$ (`x, -y`) que também estará nesta mesma curva. Isso significa que para cada `x`, existem apenas dois valores possíveis de `y`, positivo e negativo. Por exemplo, para uma abscissa `x` dada, haveria dois pontos $P1$ e $P2$ na curva elíptica, compartilhando a mesma abscissa, mas com ordenadas opostas:

![](../../dictionnaire/assets/29.png)
Para escolher entre os dois pontos potenciais na curva, um prefixo especificando qual `y` escolher é adicionado a `x`. Este método permite reduzir o tamanho de uma chave pública de 520 bits para apenas 264 bits (8 bits de prefixo + 256 bits para `x`). Esta representação é conhecida como a forma compactada da chave pública.

No entanto, no contexto da criptografia de curva elíptica, não usamos os números reais, mas um campo finito de ordem `p` (um número primo). Neste contexto, o "sinal" de `y` é determinado pela sua paridade, isto é, se `y` é par ou ímpar. O prefixo `0x02` indica então um `y` par, enquanto `0x03` indica um `y` ímpar.

Considere o seguinte exemplo de uma chave pública bruta (um ponto na curva elíptica) em hexadecimal:
```plaintext
K = 04678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb649f
6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5f
```

Podemos isolar o prefixo, `x`, e `y`:
```plaintext
Prefixo = 04
Para determinar a paridade de `y`, examinamos o último caractere hexadecimal de `y`:
```plaintext
Base 16 (hexadecimal): f
Base 10 (decimal): 15
y é ímpar
```

O prefixo para a chave pública compactada será `03`. A chave pública compactada em hexadecimal se torna:
```plaintext
K = 03678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb6
```