---
term: BLK*.DAT

---
Nombre de los archivos en Bitcoin Core que almacenan los datos de bloque en bruto del blockchain. Cada archivo se identifica por un número único en su nombre. Así, los bloques se registran en orden cronológico, empezando por el archivo blk00000.dat. Cuando este archivo alcanza su capacidad máxima, los siguientes bloques se registran en blk00001.dat, luego blk00002.dat, y así sucesivamente. Cada archivo blk tiene una capacidad máxima de 128 mebibytes (MiB), lo que equivale a algo más de 134 megabytes (MB). Estos archivos se han trasladado a la carpeta `/blocks` desde la versión 0.8.0.