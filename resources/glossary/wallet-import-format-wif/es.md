---
term: FORMATO DE IMPORTACIÓN DE CARTERA (WIF)

---
Un método para codificar una clave privada de Bitcoin de forma que pueda ser importada o exportada más fácilmente entre diferentes monederos. El WIF se basa en la codificación `Base58Check`, que incluye información sobre la versión, la compresión de la clave pública correspondiente y una suma de comprobación para la detección de errores en la escritura. Una clave privada WIF comienza con los caracteres `5` para claves sin comprimir, o `K` y `L` para claves comprimidas, y contiene todos los caracteres necesarios para reconstruir la clave privada original. El formato WIF proporciona un medio estandarizado para transferir una clave privada entre distintos programas de monedero.