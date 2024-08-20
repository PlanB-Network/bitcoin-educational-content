---
term: PROBLEMA DOS GENERAIS BIZANTINOS
---

O problema foi formulado pela primeira vez por Leslie Lamport, Robert Shostak e Marshall Pease na revista especializada *ACM Transactions on Programming Languages and Systems, vol 4, n° 3* ["The Byzantine Generals Problem"](https://lamport.azurewebsites.net/pubs/byz.pdf) em julho de 1982. É usado hoje para ilustrar os desafios em termos de tomada de decisão quando um sistema distribuído não pode confiar em nenhum ator.

Nesta metáfora, um grupo de generais bizantinos e seus respectivos exércitos estão acampados ao redor de uma cidade que desejam atacar ou cercar. Os generais estão geograficamente separados uns dos outros e devem se comunicar via mensageiro para coordenar sua estratégia. Não importa se eles atacam ou recuam, desde que todos os generais cheguem a um consenso.

Portanto, podemos considerar os seguintes requisitos:
* Cada general deve tomar uma decisão: atacar ou recuar (sim ou não);
* Uma vez tomada a decisão, ela não pode ser alterada;
* Todos os generais devem concordar com a mesma decisão e executá-la sincronamente.

Além disso, um general só pode se comunicar com outro através de mensagens transmitidas por um mensageiro, que podem ser atrasadas, destruídas, alteradas ou perdidas. E mesmo que uma mensagem seja entregue com sucesso, um ou mais generais podem escolher (por qualquer motivo) trair a confiança estabelecida e enviar uma mensagem fraudulenta, semeando o caos.

Aplicando o dilema ao contexto do blockchain do Bitcoin, cada general representa um nó na rede, precisando chegar a um consenso sobre o estado do sistema. Em outras palavras, a maioria dos participantes em uma rede distribuída deve concordar e executar a mesma ação para evitar a falha total. A única maneira de alcançar um consenso neste tipo de sistema distribuído é ter pelo menos 2/3 dos nós da rede confiáveis e honestos. Portanto, se a maioria da rede decidir agir maliciosamente, o sistema fica vulnerável.

> ► *Este dilema é às vezes também chamado de "O Problema da Transmissão Confiável".*