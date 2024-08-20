---
termo: COVENANT
---

Um mecanismo que permite a imposição de condições específicas sobre como uma determinada quantia de moeda pode ser gasta, incluindo em transações futuras. Além das condições normalmente permitidas pela linguagem de script em um UTXO, o covenant impõe restrições adicionais sobre como esse Bitcoin pode ser gasto em transações subsequentes. Tecnicamente, o estabelecimento de um covenant ocorre quando o `scriptPubKey` de um UTXO define restrições sobre o `scriptPubKey` das saídas de uma transação que gasta o referido UTXO. Ao expandir o escopo do script, os covenants possibilitariam diversos desenvolvimentos no Bitcoin, como a ancoragem bilateral de drivechains, a implementação de cofres ou a melhoria de sistemas de sobreposição como o Lightning. As propostas de covenant são diferenciadas com base em três critérios:
* Seu escopo;
* Sua implementação;
* Sua recursividade.

Existem muitas propostas que permitiriam o uso de covenants no Bitcoin. As mais avançadas no processo de implementação são: `OP_CHECKTEMPLATEVERIFY` (CTV), `SIGHASH_ANYPREVOUT` (APO) e `OP_VAULT`. Entre outras propostas, há: `OP_TX`, `OP_TAPLEAFUPDATEVERIFY` (TLUV), `OP_EVICT`, `OP_CHECKSIGFROMSTACKVERIFY` (CSFSV), `OP_CAT`, etc.

Para entender melhor o conceito de um covenant, considere esta analogia: imagine um cofre contendo 500€ em notas pequenas. Se você conseguir desbloquear este cofre com a chave certa, então você está livre para usar este dinheiro como desejar. Esta é a situação normal com o Bitcoin. Agora, imagine que o mesmo cofre não contém 500€ em notas bancárias, mas sim vouchers de refeição de valor equivalente. Se você conseguir abrir este cofre, pode usar esta soma. No entanto, sua liberdade para gastar é restrita, pois você só pode usar esses vouchers para pagar em certos restaurantes. Assim, há uma primeira condição para gastar esse dinheiro, que é conseguir abrir o cofre com a chave apropriada. Mas também há uma condição adicional quanto ao uso futuro dessa soma: ela deve ser gasta exclusivamente em restaurantes parceiros, e não livremente. Esse sistema de restrições em transações futuras é o que se chama de covenant.

> ► *Em francês, não há um termo que capture precisamente o significado da palavra "covenant". Poder-se-ia falar sobre "cláusula", "pacto" ou "compromisso", mas estes não corresponderiam exatamente ao termo "covenant". Este termo é emprestado da terminologia jurídica que permite descrever uma cláusula contratual impondo obrigações persistentes sobre uma propriedade.*