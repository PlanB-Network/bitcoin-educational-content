---
term: COINSWAP
---

Protocolo de transferência secreta de Ownership entre utilizadores. Este método tem como objetivo transferir a posse de bitcoins de uma pessoa para outra, e vice-versa, sem que este Exchange seja explicitamente visível no Blockchain. O Coinwap utiliza contratos inteligentes para efetuar a transferência sem a necessidade de confiança entre as partes.


Imaginemos um exemplo ingénuo (que não funciona) com Alice e Bob. Alice possui 1 BTC protegido com uma chave privada $A$ e Bob também possui 1 BTC protegido com uma chave privada $B$. Teoricamente, poderiam usar as suas chaves privadas através de um canal de comunicação externo para efetuar uma transferência secreta. No entanto, este método ingénuo apresenta um risco elevado em termos de confiança. Nada impede Alice de manter uma cópia da chave privada de $A$ após o Exchange e usá-la mais tarde para roubar os bitcoins, uma vez que a chave está nas mãos de Bob. Para além disso, não há qualquer garantia de que Alice não receba a chave privada $B$ de Bob e nunca passe a sua chave privada $A$ no Exchange. Este Exchange depende, portanto, de uma confiança excessiva entre as partes e é ineficaz para garantir uma transferência segura e secreta do Ownership.


Para resolver estes problemas e permitir a troca de moedas entre partes que não confiam umas nas outras, vamos utilizar sistemas Smart contract que tornam o Exchange "atómico". Estes podem ser HTLC (*Hash Time-Locked Contracts*) ou PTLC (*Point Time-Locked Contracts*). Estes dois protocolos funcionam de forma semelhante, utilizando um sistema de bloqueio de tempo que garante que o Exchange seja concluído com êxito ou completamente cancelado, protegendo assim a integridade dos fundos de ambas as partes. A principal diferença entre o HTLC e o PTLC é que o HTLC utiliza hashes e pré-imagens para proteger a transação, enquanto o PTLC utiliza assinaturas de adaptador.


Num cenário de troca de moedas utilizando um HTLC ou PTLC entre Alice e Bob, o Exchange tem lugar de forma segura: ou é bem sucedido e cada um recebe as BTC do outro, ou falha e cada um mantém as suas próprias BTC. Isto torna impossível que uma das partes faça batota ou roube as BTC da outra.


A utilização de Assinaturas de Adaptadores é particularmente interessante neste contexto, pois permite dispensar os scripts tradicionais (um mecanismo por vezes designado por "scripts sem scripts"). Isto permite reduzir os custos associados ao Exchange. Outra grande vantagem das Assinaturas de Adaptadores é que não requerem a utilização de um Hash comum a ambas as partes da transação, evitando assim a necessidade de revelar uma ligação direta entre elas em certos tipos de Exchange.