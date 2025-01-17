---
term: SECP256K1

---
Nome dado a uma curva elíptica específica utilizada no protocolo Bitcoin para a implementação dos algoritmos de assinatura digital ECDSA (*Elliptic Curve Digital Signature Algorithm*) e Schnorr. A curva `secp256k1` foi escolhida pelo inventor do Bitcoin, Satoshi Nakamoto. Tem algumas propriedades interessantes, nomeadamente vantagens em termos de desempenho.

O uso do `secp256k1` no Bitcoin significa que cada chave privada (um número aleatório de 256 bits) é mapeada para uma chave pública correspondente através da adição e duplicação do ponto da chave privada pelo ponto gerador da curva `secp256k1`. Essa operação é fácil de ser realizada em uma direção, mas praticamente impossível de ser revertida, o que forma a base da segurança das assinaturas digitais no Bitcoin.

A curva `secp256k1` é especificada pela equação da curva elíptica $y^2 = x^3 + 7$, o que significa que tem coeficientes $a$ iguais a $0$ e $b$ iguais a $7$ na forma geral da equação de uma curva elíptica $y^2 = x^3 + ax + b$. A curva `secp256k1` é definida num campo finito cuja ordem é um número primo muito grande, especificamente $p = 2^{256} - 2^{32} - 977$. A curva também tem uma ordem de grupo, que é o número de pontos distintos na curva, um ponto gerador predefinido (ou ponto $G$), que é utilizado em operações criptográficas para gerar pares de chaves, e um cofator igual a $1$.

> ► *"SEC" significa "Standards for Efficient Cryptography" (Normas para Criptografia Eficiente). "P256" indica que a curva é definida sobre um campo $\mathbb{Z}_p$ em que $p$ é um número primo de 256 bits. "K" refere-se ao nome do seu inventor, Neal Koblitz. Finalmente, "1" indica que esta é a primeira versão desta curva.*