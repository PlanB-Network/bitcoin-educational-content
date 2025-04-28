---
term: CISA
---

Acrónimo de "Cross-Input Signature Aggregation". Trata-se de uma proposta técnica destinada a otimizar a dimensão das transacções Bitcoin, reduzindo o número de assinaturas necessárias para as validar.


Atualmente, no Bitcoin, cada entrada numa transação tem de ter uma assinatura individual antes de poder ser consumida. Isto prova que o proprietário do UTXO em questão autorizou a transação. Com a CISA, o objetivo é combinar as assinaturas de todos os inputs de uma única transação numa única assinatura que abranja todos os inputs. Isto permitiria reduzir a dimensão das transacções com muitos inputs, reduzindo assim também os seus custos. Isto seria particularmente útil para aqueles que realizam coinjoins ou consolidações, ao mesmo tempo que permitiria que mais transacções fossem confirmadas no Bitcoin sem alterar os tamanhos ou intervalos dos blocos. A CISA é baseada no protocolo Schnorr, que permite a agregação linear de assinaturas. Isto significa que uma única assinatura pode provar a posse de várias chaves independentes.


No entanto, a implementação da CISA no Bitcoin é muito complexa, uma vez que requer alterações profundas na forma como os scripts funcionam. Atualmente, a verificação de scripts no Bitcoin é feita entrada a entrada. Passar para um modelo em que uma transação inteira é verificada de uma só vez, como proposto pela CISA, está longe de ser uma mudança trivial.