---
term: BIP35
---

Proposta que permite a um nó Bitcoin abrir informações sobre seu mempool, ou seja, as transações que aguardam confirmação. Graças a isso, outros participantes podem receber dados em tempo real sobre transações não confirmadas enviando uma mensagem específica a um nó. Antes da adoção do BIP35, os nós só podiam acessar informações sobre transações já confirmadas. Esta melhoria oferece às carteiras SPV a capacidade de receber informações sobre transações não confirmadas, permite a um minerador evitar perder transações com taxas altas durante um reinício e facilita a análise de informações do mempool por serviços externos.