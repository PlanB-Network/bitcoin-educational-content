---
name: Stonewall
description: Compreensão e uso de transações Stonewall
---

![capa stonewall](assets/cover.jpeg)

> *"Quebre as suposições da análise de blockchain com dúvida matematicamente comprovável entre remetente e destinatário de suas transações."*

## O que é uma transação Stonewall?
Stonewall é uma forma específica de transação Bitcoin que visa aumentar a privacidade do usuário durante um gasto, imitando uma coinjoin entre duas pessoas, sem realmente ser uma. De fato, essa transação não é colaborativa. Um usuário pode construí-la sozinho, envolvendo apenas suas próprias UTXOs como entradas. Portanto, você pode criar uma transação Stonewall para qualquer ocasião sem precisar sincronizar com outro usuário.

A operação de uma transação Stonewall é a seguinte: como entrada para a transação, o remetente usa 2 UTXOs que lhe pertencem. Como saída, a transação produz 4 saídas, das quais 2 serão exatamente do mesmo valor. As outras 2 serão troco. Entre as 2 saídas do mesmo valor, apenas uma irá para o destinatário do pagamento.

Portanto, existem apenas 2 papéis em uma transação Stonewall:
- O remetente, que faz o pagamento real;
- O destinatário, que pode ignorar a natureza específica da transação e simplesmente esperar um pagamento do remetente.

Vamos pegar um exemplo para entender essa estrutura de transação. Alice está na padaria para comprar sua baguete, que custa 4.000 sats. Ela quer pagar em bitcoins mantendo um certo nível de privacidade para seu pagamento. Portanto, ela decide construir uma transação Stonewall para o pagamento.
![transação stonewall padaria](assets/fr/1.png)
Ao analisar essa transação, podemos ver que o padeiro realmente recebeu 4.000 sats como pagamento pela baguete. Alice usou 2 UTXOs como entradas: um de 10.000 sats e outro de 15.000 sats. Como saída, ela recebeu 3 UTXOs: um de 4.000 sats, um de 6.000 sats e um de 11.000 sats. Alice, portanto, tem um saldo líquido de -4.000 sats nesta transação, que corresponde ao preço da baguete.

Neste exemplo, eu negligenciei intencionalmente as taxas de mineração para facilitar o entendimento. Na realidade, as taxas de transação são totalmente cobertas pelo remetente.

Qual é a diferença entre Stonewall e Stonewall x2?
A transação Stonewall opera da mesma forma que a transação StonewallX2, com a exceção de que esta última requer colaboração, ao contrário da transação Stonewall clássica, daí a designação "x2". De fato, a transação Stonewall pode ser executada sem cooperação externa: o remetente pode concluí-la sem a ajuda de outra pessoa. No entanto, para uma transação Stonewall x2, um participante adicional, chamado "colaborador", junta-se ao processo. O colaborador contribui com seus próprios bitcoins como entradas, juntamente com os do remetente, e recebe a soma total como saídas (menos as taxas de mineração).

Vamos revisitar nosso exemplo com Alice na padaria. Se ela quisesse fazer uma transação Stonewall x2, Alice teria que colaborar com Bob (um terceiro) durante a criação da transação. Cada um deles teria fornecido uma UTXO como entrada. Bob então teria recebido a totalidade de sua contribuição como saída. O padeiro teria recebido o pagamento pela baguete da mesma forma que na transação Stonewall, enquanto Alice teria recebido seu saldo inicial, menos o custo da baguete.
![Stonewall Tutorial - Sparrow Wallet](https://youtu.be/mlRtZvWGuk0?si=e_lSKJLvybWUna1j)
Como um tradutor profissional qualificado, minha principal tarefa é traduzir com precisão o conteúdo técnico do inglês para o meu idioma nativo, o português. Por favor, siga as seguintes diretrizes para garantir uma tradução de alta qualidade:

Idioma Original: O conteúdo é originalmente em inglês.
Natureza do Conteúdo: Você encontrará material técnico, potencialmente incluindo terminologia específica da indústria.
Links e Palavras Técnicas: Não traduza URLs ou termos técnicos altamente específicos. Se estiver incerto, mantenha o termo original.
Consistência de Formatação: Mantenha o mesmo layout e formatação de markdown do texto original. A consistência da estrutura é crucial.
Propriedades YML: Se uma linha começa com uma propriedade YML (por exemplo, 'name:', 'goal:', 'objectives:'), mantenha o nome da propriedade em inglês.
Contexto Cultural: Para referências culturais ou específicas do contexto que possam não ser traduzidas diretamente, parafraseie para preservar o significado pretendido ou forneça uma breve explicação.
O foco deve ser em manter a integridade do conteúdo técnico, garantindo que a tradução seja compreensível e contextualmente precisa em português.

Este é o texto a ser traduzido:
![Tutorial Stonewall - Sparrow Wallet](https://youtu.be/su89ljkV_OI?si=1jNaSJGvECUYe6Or)

**Recursos externos:**
- https://docs.samourai.io/en/spend-tools#stonewall;
- https://samouraiwallet.com/stonewall.
