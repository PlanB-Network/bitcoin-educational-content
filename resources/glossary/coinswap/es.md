---
term: COINSWAP
---

Protocolo de transferencia secreta de Ownership entre usuarios. Este método tiene como objetivo transferir la posesión de bitcoins de una persona a otra, y viceversa, sin que esta Exchange sea visible explícitamente en la Blockchain. Coinwap utiliza contratos inteligentes para realizar la transferencia sin necesidad de confianza entre las partes.


Imaginemos un ejemplo ingenuo (que no funciona) con Alice y Bob. Alice tiene 1 BTC asegurado con la clave privada $A$, y Bob también tiene 1 BTC asegurado con la clave privada $B$. Teóricamente, podrían Exchange sus claves privadas a través de un canal de comunicación externo para llevar a cabo una transferencia secreta. Sin embargo, este método ingenuo presenta un alto riesgo en términos de confianza. Nada impide que Alice conserve una copia de la clave privada $A$ después de la Exchange y la utilice más tarde para robar los bitcoins, una vez que la clave esté en manos de Bob. Es más, no hay ninguna garantía de que Alice no reciba la clave privada $B$ de Bob y nunca transmita su clave privada $A$ en la Exchange. Por lo tanto, esta Exchange se basa en una confianza excesiva entre las partes, y es ineficaz para garantizar una transferencia segura y secreta de Ownership.


Para resolver estos problemas y permitir el intercambio de monedas entre partes que no confían entre sí, vamos a utilizar sistemas Smart contract que hacen que el Exchange sea "atómico". Estos pueden ser HTLC (*Hash Time-Locked Contracts*) o PTLC (*Point Time-Locked Contracts*). Estos dos protocolos funcionan de forma similar, utilizando un sistema de bloqueo temporal que garantiza que el Exchange se complete con éxito o se cancele por completo, protegiendo así la integridad de los fondos de ambas partes. La principal diferencia entre HTLC y PTLC es que HTLC utiliza hashes y preimágenes para asegurar la transacción, mientras que PTLC utiliza Firmas Adaptadoras.


En un escenario de intercambio de monedas con una HTLC o PTLC entre Alice y Bob, la Exchange tiene lugar de forma segura: o bien tiene éxito y cada uno recibe el BTC del otro, o bien falla y cada uno se queda con su propio BTC. Esto hace imposible que cualquiera de las partes haga trampas o robe el BTC de la otra.


El uso de Firmas Adaptadoras es especialmente interesante en este contexto, ya que permite prescindir de los guiones tradicionales (un mecanismo a veces denominado "_guiones sin guiones_"). Esto reduce los costes asociados a la Exchange. Otra gran ventaja de las Firmas Adaptadoras es que no requieren el uso de una Hash común para ambas partes de la transacción, evitando así la necesidad de revelar un vínculo directo entre ellas en determinados tipos de Exchange.