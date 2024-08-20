---
term: EXCLUSIVE OR
---

Uma função fundamental da lógica Booleana. O "Ou Exclusivo" ou XOR ("*Exclusive or*") recebe dois operandos Booleanos, cada um sendo verdadeiro ou falso, e produz uma saída verdadeira apenas quando os dois operandos são diferentes. Em outras palavras, a saída da operação `XOR` é verdadeira se exatamente um (mas não ambos) dos operandos for verdadeiro. Por exemplo, a operação `XOR` entre `1` e `0` resultará em `1`. Notamos: $1 \oplus 0 = 1$. Da mesma forma, a operação `XOR` pode ser realizada em sequências mais longas de bits. Por exemplo, $10110 \oplus 01110 = 11000$. Cada bit da sequência é comparado com seu correspondente, e a operação `XOR` é aplicada. Aqui está a tabela verdade para a operação `XOR`:

<div align="center">

| $A$ | $B$ | $A \oplus B$ |
|:---:|:---:|:------------:|
| $0$ | $0$ |      $0$     |
| $0$ | $1$ |      $1$     |
| $1$ | $0$ |      $1$     |
| $1$ | $1$ |      $0$     |

</div>

A operação `XOR` é usada em muitas áreas da ciência da computação, especialmente em criptografia, por seus atributos interessantes, tais como:
* Sua comutatividade: a ordem dos operandos não afeta o resultado. Para duas variáveis dadas $D$ e $E$: $D \oplus E = E \oplus D$;
* Sua associatividade: o agrupamento dos operandos não afeta o resultado. Para três variáveis dadas $A$, $B$ e $C$: $(A \oplus B) \oplus C = A \oplus (B \oplus C)$;
* Tem um elemento neutro `0`: um operando xored com 0 sempre será igual ao operando. Para uma variável dada $A$: $A \oplus 0 = A$;
* Cada elemento é seu próprio inverso. Para uma variável dada $A$: $A \oplus A = 0$.

No contexto do Bitcoin, a operação `XOR` é obviamente usada em muitos lugares. Por exemplo, `XOR` é massivamente usado na função `SHA256`, que é amplamente utilizada no protocolo Bitcoin. Alguns protocolos como o *SeedXOR* da Coldcard também usam essa primitiva para outras aplicações. Também é encontrado no BIP47 para criptografar o código de pagamento reutilizável durante sua transmissão.
No campo mais amplo da criptografia, `XOR` pode ser usado como está como um algoritmo de criptografia simétrica. Este algoritmo é chamado de "One-Time Pad" ou "Cifra de Vernam", nomeado após seu inventor. Embora impraticável devido ao comprimento da chave, este algoritmo é um dos únicos algoritmos de criptografia reconhecidos como incondicionalmente seguros.