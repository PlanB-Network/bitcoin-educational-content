---
term: P2MS

---
P2MS significa *Pay to Multisig*, que se traduz em "pagar para múltiplas assinaturas". É um modelo de script padrão utilizado para estabelecer condições de despesa num UTXO. Permite o bloqueio de bitcoins com várias chaves públicas. Para gastar esses bitcoins, é necessária uma assinatura com um número predefinido de chaves privadas associadas. Por exemplo, um `P2MS 2/3` envolve `3` chaves públicas com `3` chaves privadas secretas associadas. Para gastar os bitcoins bloqueados com este script P2MS, é necessária uma assinatura com pelo menos `2` das `3` chaves privadas. Este é um sistema de segurança de limiar.

Este script foi inventado em 2011 por Gavin Andresen quando assumiu a manutenção do principal cliente Bitcoin. Atualmente, o P2MS é apenas marginalmente utilizado por algumas aplicações. A grande maioria das multisignatures modernas usam outros scripts como P2SH ou P2WSH. Comparado com estes, o P2MS é extremamente trivial. As chaves públicas em que consiste são reveladas aquando da receção da transação. A utilização de um P2MS é também mais dispendiosa do que outros scripts de assinatura múltipla.

> ► *Os P2MS são frequentemente designados por "bare-multisig", que pode ser traduzido por "naked multisignature" ou "raw multisignature". No início de 2023, os scripts P2MS estiveram no centro de uma controvérsia devido à sua utilização indevida no âmbito do protocolo Stamps. O seu impacto no conjunto UTXO foi notoriamente assinalado