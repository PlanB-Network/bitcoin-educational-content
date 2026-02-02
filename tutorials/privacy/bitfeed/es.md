---
name: Bitfeed
description: Explora la cadena de protocolos principal de Bitcoin.
---

![cover](assets/cover.webp)



Bitfeed es una plataforma para visualizar la capa onchain del protocolo Bitcoin. Fue iniciada por uno de los colaboradores del proyecto Mempool.space y destaca principalmente por su aspecto minimalista y su facilidad de uso.



https://planb.academy/tutorials/privacy/explorer/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f

En este tutorial, echaremos un vistazo a esta herramienta, que te permite explorar todas las transacciones y bloques de la red.



## Primeros pasos con Bitfeed



Bitfeed es una plataforma que se centra en tres puntos principales:





- Consulta Blockchain**,
- Búsqueda de transacciones**,
- Visualizar el mempool**.



### Consultar la cadena de bloques



En la página de inicio de Bitfeed encontrará principalmente :





- La barra de búsqueda: Esta sección es el punto de entrada para las consultas de blockchain. Aquí puede buscar un bloque específico por su número o hash. También puedes buscar transacciones específicas y direcciones Bitcoin para verificar cierta información de transacciones en la red.



![searchBar](assets/fr/01.webp)



En la esquina superior izquierda, puede ver el precio actual del bitcoin, estimado en dólares estadounidenses (USD).



![price](assets/fr/02.webp)



En la barra lateral derecha se encuentra el menú de la plataforma. Desde este menú puedes personalizar la interfaz de la plataforma a tu gusto, añadir o eliminar elementos y personalizar los filtros de visualización. Por ejemplo, ver el tamaño de cada bloque por valor o por peso en bytes virtuales (vBytes).



![menu](assets/fr/03.webp)



En el centro de la página está el último bloque minado, con una vista de todas las transacciones incluidas en ese bloque. Esta sección proporciona información sobre la marca de tiempo, el número total de bitcoins implicados en el bloque, el tamaño del bloque en bytes, el número de transacciones y el ratio de coste medio de transacción por byte virtual en el bloque.



![block](assets/fr/04.webp)



Puede retroceder en el historial del canal buscando un bloque concreto en la barra de búsqueda y visualizarlo según sus criterios.



Por ejemplo, queremos ver las transacciones del bloque `879488`.



![bloc](assets/fr/05.webp)



La primera transacción de este bloque representa la transacción **coinbase** que permite al minero de este bloque ganar la recompensa mining, que sólo puede gastarse después de minar 100 bloques, compuesta por las tasas de transacción incluidas y la subvención del bloque. Esta transacción es la que permite la emisión de nuevos bitcoins en el sistema.



![coinbase](assets/fr/06.webp)



https://planb.academy/courses/f3e3843d-1a1d-450c-96d6-d7232158b81f

Por defecto, las transacciones de un bloque se representan según dos criterios:




- El tamaño, que puede variar entre el valor y el peso (vBytes) ;
- El color puede variar en función de la edad y de la proporción de tasas de transacción por byte virtual.



![options](assets/fr/07.webp)



Por tanto, podemos concluir que todas las transacciones incluidas en el mismo bloque tienen el mismo número de confirmaciones en la blockchain. Los cubos más grandes representan las transacciones que contienen la mayor cantidad de bitcoins.



Esta interpretación se ve confirmada por la opción de menú **"Info "**, que nos informa de la traducción del color y el tamaño de las transacciones del bloque.



![infos](assets/fr/08.webp)



También puedes ver las transacciones de un bloque por bytes virtuales y ratio de comisión. Esta vista puede diferir de la anterior, ya que el valor en bitcoins incluido en una transacción no define su tamaño.



![visualisation](assets/fr/09.webp)



### Ver transacciones



Puede buscar una transacción utilizando su identificador a través de la barra de búsqueda. También puede hacer clic en un cubo para ver la información relacionada con esa transacción.



En nuestro caso, tomemos la transacción que ocupa el mayor espacio en el bloque `879488`.



![biggest](assets/fr/10.webp)



Verás que esta transacción tiene `42,989`, que representa la diferencia entre el último bloque minado y nuestro bloque elegido. Estas confirmaciones ayudan a reforzar la seguridad de la red Bitcoin, ya que para modificar maliciosamente esta transacción, los atacantes necesitarían poseer la potencia de cálculo equivalente para reescribir toda la cadena de bloques principal.



El tamaño de esta transacción es de `57.088 vBytes`, debido principalmente al gran número de UTXOs utilizados en su construcción (842 entradas). Sorprendentemente, el ratio de tasas aplicado sigue siendo relativamente bajo (sólo 4 sats/vByte) en comparación con la media global de bloques de 5,82 sats/vByte.



Por lo tanto, la transacción que ocupa más espacio no es necesariamente la transacción con el mayor ratio de coste de transacción.



![transaction](assets/fr/11.webp)



Si sigue la escala del menú **Info**, la transacción con el mayor ratio de coste de transacción es la de color morado. Se trata de la transacción [bfd81fdde02055ced809419b4fae094576bc4384a1d0444c723b3ba052e99a35](https://bitfeed.live/tx/bfd81fdde02055ced809419b4fae094576bc4384a1d0444c723b3ba052e99a35) con un ratio de coste de transacción de `147.49 sats/vBytes`.



![mostfeerate](assets/fr/12.webp)



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

### Visualización Mempool



El [mempool] es el lugar virtual donde se agrupan las transacciones de Bitcoin que esperan ser incluidas en un bloque. Bitfeed permite consultar el [mempool](https://planb.academy/resources/glossary/mempool) de varios mineros Bitcoin, ofreciendo un amplio seguimiento de las transacciones.



![mempool](assets/fr/13.webp)



En esta sección, puede realizar un seguimiento de todas las transacciones válidas y aún no confirmadas en la cadena principal de la red Bitcoin.



![unconfirmed](assets/fr/14.webp)



Ya tienes una guía para utilizar la plataforma Bitfeed para analizar bloques y transacciones con el fin de visualizar la información disponible en la cadena principal de la red Bitcoin, al tiempo que te beneficias de una interfaz minimalista y fácil de usar. Si te ha gustado este tutorial, te recomendamos que des el siguiente paso: descubrir Lightning Network a través del proyecto Amboss.



https://planb.academy/tutorials/node/lightning-network/amboss-37044cad-0f85-41eb-af18-491384af1017