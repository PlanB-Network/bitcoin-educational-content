---
term: PROBLEMA DOS GENERAIS BIZANTINOS

---
O problema foi formulado pela primeira vez por Leslie Lamport, Robert Shostak e Marshall Pease na revista especializada *ACM Transactions on Programming Languages and Systems, vol 4, n° 3* ["The Byzantine Generals Problem"] (https://lamport.azurewebsites.net/pubs/byz.pdf) em julho de 1982. É utilizado atualmente para ilustrar os desafios em termos de tomada de decisões quando um sistema distribuído não pode confiar em nenhum ator.

Nesta metáfora, um grupo de generais bizantinos e os seus respectivos exércitos estão acampados à volta de uma cidade que pretendem atacar ou sitiar. Os generais estão geograficamente separados uns dos outros e têm de comunicar através de um mensageiro para coordenar a sua estratégia. O facto de atacarem ou recuarem é indiferente, desde que todos os generais cheguem a um consenso.

Por conseguinte, podemos considerar os seguintes requisitos:


- Cada general deve tomar uma decisão: atacar ou retirar (sim ou não);
- Uma vez tomada a decisão, esta não pode ser alterada;
- Todos os generais devem concordar com a mesma decisão e executá-la em sincronia.

Além disso, um general só pode comunicar com outro através de mensagens transmitidas por um mensageiro, que podem ser atrasadas, destruídas, alteradas ou perdidas. E mesmo que uma mensagem seja entregue com sucesso, um ou mais generais podem decidir (por qualquer razão) trair a confiança estabelecida e enviar uma mensagem fraudulenta, semeando o caos.

Aplicando o dilema ao contexto da cadeia de blocos Bitcoin, cada general representa um nó na rede, necessitando de chegar a um consenso sobre o estado do sistema. Por outras palavras, a maioria dos participantes numa rede distribuída deve concordar e executar a mesma ação para evitar uma falha total. A única forma de chegar a um consenso neste tipo de sistema distribuído é ter pelo menos 2/3 dos nós da rede fiáveis e honestos. Por conseguinte, se a maioria da rede decidir agir de forma maliciosa, o sistema fica vulnerável.

> ► *Este dilema é por vezes também designado por "O problema da transmissão fiável"