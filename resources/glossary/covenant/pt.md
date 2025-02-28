---
term: CONVENÇÃO

---
Um mecanismo que permite a imposição de condições específicas sobre a forma como uma determinada moeda pode ser gasta, incluindo em transacções futuras. Para além das condições normalmente permitidas pela linguagem de script de um UTXO, o covenant impõe restrições adicionais sobre a forma como esta Bitcoin pode ser gasta em transacções subsequentes. Tecnicamente, o estabelecimento de um covenant ocorre quando a `scriptPubKey` de um UTXO define restrições na `scriptPubKey` dos outputs de uma transação que gasta o referido UTXO. Ao alargar o âmbito do script, os covenants permitiriam inúmeros desenvolvimentos na Bitcoin, como a ancoragem bilateral de drivechains, a implementação de vaults ou a melhoria de sistemas de sobreposição como o Lightning. As propostas de convénio são diferenciadas com base em três critérios:


- O seu âmbito de aplicação;
- A sua aplicação;
- A sua recursividade.

Existem muitas propostas que permitiriam a utilização de pactos sobre a Bitcoin. As mais avançadas no processo de implementação são: `OP_CHECKTEMPLATEVERIFY` (CTV), `SIGHASH_ANYPREVOUT` (APO), e `OP_VAULT`. Entre outras propostas, temos: `OP_TX`, `OP_TAPLEAFUPDATEVERIFY` (TLUV), `OP_EVICT`, `OP_CHECKSIGFROMSTACKVERIFY` (CSFSV), `OP_CAT`, etc.

Para compreender melhor o conceito de pacto, considere a seguinte analogia: imagine um cofre que contém 500 euros em notas pequenas. Se conseguir abrir esse cofre com a chave certa, pode utilizar esse dinheiro como quiser. Esta é a situação normal da Bitcoin. Agora, imagine que o mesmo cofre não contém 500 euros em notas, mas sim vales de refeição de valor equivalente. Se conseguir abrir esse cofre, pode utilizar essa quantia. No entanto, a sua liberdade de gastar é limitada, pois só pode utilizar esses vales para pagar em determinados restaurantes. Assim, há uma primeira condição para gastar este dinheiro, que é conseguir abrir o cofre com a chave adequada. Mas há também uma condição adicional relativamente à utilização futura deste montante: deve ser gasto exclusivamente em restaurantes parceiros, e não livremente. Este sistema de restrições às transacções futuras é o que se chama um pacto.

> ► *Em francês, não existe um termo que capte com precisão o significado da palavra "covenant". Poder-se-ia falar de "cláusula", "pacto" ou "compromisso", mas estes não corresponderiam exatamente ao termo "covenant". Este termo é emprestado da terminologia jurídica que permite descrever uma cláusula contratual que impõe obrigações persistentes a uma propriedade.*