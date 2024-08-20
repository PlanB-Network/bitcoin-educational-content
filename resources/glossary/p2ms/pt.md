---
term: P2MS
---

P2MS significa *Pay to Multisig*, que se traduz para "pagar para múltiplas assinaturas". É um modelo de script padrão usado para estabelecer condições de gasto em um UTXO. Ele permite o bloqueio de bitcoins com múltiplas chaves públicas. Para gastar esses bitcoins, é necessária uma assinatura com um número pré-definido de chaves privadas associadas. Por exemplo, um `P2MS 2/3` envolve `3` chaves públicas com `3` chaves privadas secretas associadas. Para gastar os bitcoins bloqueados com este script P2MS, é necessária uma assinatura com pelo menos `2` das `3` chaves privadas. Este é um sistema de segurança de limiar.

Este script foi inventado em 2011 por Gavin Andresen quando ele assumiu a manutenção do cliente principal do Bitcoin. Hoje, o P2MS é usado apenas marginalmente por algumas aplicações. A grande maioria das multisignaturas modernas usa outros scripts como P2SH ou P2WSH. Comparado a estes, o P2MS é extremamente trivial. As chaves públicas que ele contém são reveladas ao receber a transação. Usar um P2MS também é mais caro do que outros scripts de multisignatura.

> ► *Os P2MS são frequentemente chamados de "bare-multisig", que poderia ser traduzido como "multisignatura nua" ou "multisignatura crua". No início de 2023, os scripts P2MS estavam no centro de uma controvérsia devido ao seu uso indevido dentro do protocolo Stamps. Seu impacto no conjunto de UTXO foi notavelmente apontado.*