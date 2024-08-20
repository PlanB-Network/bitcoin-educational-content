---
term: BLOCKS/REV*.DAT
---

Nombre de los archivos en Bitcoin Core que almacenan la información necesaria para potencialmente revertir los cambios realizados al conjunto de UTXO por bloques previamente añadidos. Cada archivo es identificado por un número único que es el mismo que el archivo blk*.dat al que corresponde. Los archivos rev*.dat contienen los datos de reversión correspondientes a los bloques almacenados en los archivos blk*.dat. Estos datos son esencialmente una lista de todos los UTXOs gastados como entradas en un bloque. Estos archivos de reversión permiten al nodo volver a un estado anterior en caso de una reorganización de la blockchain que cause que bloques previamente validados sean descartados.