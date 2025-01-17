---
term: EXCLUSIVO OU

---
Uma função fundamental da lógica booleana. A operação "Exclusive Or" ou XOR ("*Exclusive or*") recebe dois operandos booleanos, sendo cada um deles verdadeiro ou falso, e produz um resultado verdadeiro apenas quando os dois operandos diferem. Por outras palavras, o resultado da operação `XOR` é verdadeiro se exatamente um (mas não ambos) dos operandos for verdadeiro. Por exemplo, a operação `XOR` entre `1` e `0` resultará em `1`. Notamos que: $1 \oplus 0 = 1$. Da mesma forma, a operação `XOR` pode ser realizada em seqüências maiores de bits. Por exemplo, $10110 \oplus 01110 = 11000$. Cada bit da sequência é comparado com o seu equivalente, e a operação `XOR` é aplicada. Aqui está a tabela verdade para a operação `XOR`:

<div align="center">

| $A$ | $B$ | $A \oplus B$ |

|:---:|:---:|:------------:|

| $0$ | $0$ | $0$ |

| $0$ | $1$ | $1$ |

| $1$ | $0$ | $1$ |

| $1$ | $1$ | $0$ |

</div>

A operação `XOR` é utilizada em muitas áreas da ciência da computação, especialmente na criptografia, por seus atributos interessantes, tais como:


- A sua comutatividade: a ordem dos operandos não afecta o resultado. Para duas variáveis dadas $D$ e $E$: $D \oplus E = E \oplus D$;
- A sua associatividade: o agrupamento de operandos não afecta o resultado. Para três variáveis dadas $A$, $B$ e $C$: $(A \oplus B) \oplus C = A \oplus (B \oplus C)$;
- Tem um elemento neutro `0`: um operando xorado com 0 será sempre igual ao operando. Para uma dada variável $A$: $A \oplus 0 = A$;
- Cada elemento é o seu próprio inverso. Para uma dada variável $A$: $A \oplus A = 0$.

No contexto do Bitcoin, a operação `XOR` é obviamente usada em muitos lugares. Por exemplo, o `XOR` é massivamente utilizado na função `SHA256`, que é amplamente utilizada no protocolo Bitcoin. Alguns protocolos como o *SeedXOR* da Coldcard também utilizam esta primitiva para outras aplicações. Encontra-se também no BIP47 para encriptar o código de pagamento reutilizável durante a sua transmissão.

No domínio mais vasto da criptografia, o `XOR` pode ser utilizado como um algoritmo de encriptação simétrica. Este algoritmo é designado por "One-Time Pad" ou "Vernam Cipher", em homenagem ao seu inventor. Embora impraticável devido ao comprimento da chave, este algoritmo é um dos únicos algoritmos de encriptação reconhecidos como incondicionalmente seguros.