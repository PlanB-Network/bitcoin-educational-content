---
term: BLOQUES/REV*.DAT

---
Nombre de los archivos en Bitcoin Core que almacenan la información necesaria para revertir potencialmente los cambios realizados en el conjunto UTXO por bloques añadidos previamente. Cada archivo se identifica por un número único que es el mismo que el archivo blk*.dat al que corresponde. Los archivos rev*.dat contienen los datos de inversión correspondientes a los bloques almacenados en los archivos blk*.dat. Estos datos son esencialmente una lista de todos los UTXOs gastados como entradas en un bloque. Estos archivos de reversión permiten al nodo volver a un estado anterior en caso de que se produzca una reorganización de la blockchain que haga que se descarten bloques previamente validados.