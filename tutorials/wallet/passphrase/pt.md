---
name: Frase-senha BIP39
description: Entendendo como uma frase-senha funciona
---
![cover](assets/cover.webp)

## O que é uma frase-senha BIP39?

Carteiras HD são tipicamente geradas a partir de uma frase mnemônica consistindo de 12 ou 24 palavras. Esta frase é muito importante porque permite a restauração de todas as chaves de uma carteira caso seu meio físico (como uma carteira de hardware, por exemplo) seja perdido. No entanto, ela constitui um único ponto de falha porque se for comprometida, um atacante poderia roubar todos os bitcoins.

![PASSPHRASE BIP39](assets/notext/01.webp)

É aqui que a frase-senha entra. É uma senha opcional que você pode escolher livremente, que é adicionada à frase mnemônica no processo de derivação de chave para aumentar a segurança da carteira.

![PASSPHRASE BIP39](assets/notext/02.webp)

Tenha cuidado para não confundir a frase-senha com o código PIN da sua carteira de hardware ou a senha usada para desbloquear o acesso à sua carteira no seu computador. Diferente de todos esses elementos, a frase-senha desempenha um papel na derivação das chaves da sua carteira. **Isso significa que sem ela, você nunca será capaz de recuperar seus bitcoins.**

A frase-senha trabalha em conjunto com a frase mnemônica, alterando a semente da qual as chaves são geradas. Assim, mesmo que alguém obtenha sua frase de 12 ou 24 palavras, sem a frase-senha, eles não podem acessar seus fundos. **Usar uma frase-senha essencialmente cria uma nova carteira com chaves distintas. Modificar (mesmo que levemente) a frase-senha gerará uma carteira diferente.**

## Por que você deveria usar uma frase-senha?

A frase-senha é arbitrária e pode ser qualquer combinação de caracteres escolhida pelo usuário. Usar uma frase-senha, portanto, oferece várias vantagens. Primeiro, ela reduz todos os riscos associados ao comprometimento da frase mnemônica exigindo um segundo fator para acessar os fundos (roubo, acesso à sua casa, etc.).

Em seguida, ela pode ser usada estrategicamente para criar uma carteira isca, para lidar com constrangimentos físicos para roubar seus fundos como o infame "*ataque da chave de fenda de $5*". Neste cenário, a ideia é ter uma carteira sem frase-senha contendo apenas uma pequena quantidade de bitcoins, o suficiente para satisfazer um potencial agressor, enquanto se tem uma carteira oculta. Esta última usa a mesma frase mnemônica mas é assegurada com uma frase-senha adicional.

Finalmente, usar uma frase-senha é interessante quando se deseja controlar a aleatoriedade da geração de semente da carteira HD.

## Como escolher uma boa frase-senha?
Para que a frase-senha seja eficaz, ela deve ser suficientemente longa e aleatória. Assim como com uma senha forte, eu recomendo escolher uma frase-senha que seja o mais longa e aleatória possível, com uma variedade de letras, números e símbolos para tornar qualquer ataque de força bruta impossível.

Também é importante salvar corretamente esta frase-senha, da mesma forma que a frase mnemônica. **Perdê-la significa perder o acesso aos seus bitcoins**. Eu aconselho fortemente contra memorizá-la somente em sua cabeça, pois isso aumenta irrazoavelmente o risco de perda. O ideal é escrevê-la em um meio físico (papel ou metal) separado da frase mnemônica. Este backup deve obviamente ser armazenado em um local diferente de onde sua frase mnemônica é mantida para prevenir que ambos sejam comprometidos simultaneamente.

## Tutoriais

Para configurar uma frase-senha em um dispositivo Ledger (Stax, Flex, ou Nano), você pode consultar este tutorial:

https://planb.network/tutorials/wallet/hardware/passphrase-ledger-9ae6d9a2-7293-438a-8fe0-e59147ef2f49