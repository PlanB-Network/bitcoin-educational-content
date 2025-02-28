---
term: BIP12

---
Proposta de Gavin Andresen para aumentar a flexibilidade e privacidade dos scripts de transações Bitcoin. Este BIP sugere a implementação de um novo script opcode, chamado `OP_EVAL`, que permite a avaliação de um script contido nos dados de um `scriptSig` durante o processo de validação da transação. A principal modificação do BIP12 é permitir a inclusão de um script dentro de outro script. Esta técnica permite a criação de condições mais complexas que podem ser verificadas no momento do gasto, sem necessidade de as revelar aos utilizadores que enviam bitcoins para o endereço utilizado. O BIP12 foi posteriormente substituído por propostas mais seguras, nomeadamente o BIP16 (P2SH), que oferece um método diferente para atingir os mesmos objectivos do `OP_EVAL`.