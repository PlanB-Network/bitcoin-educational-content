---
name: Picocrypt
description: Una herramienta de código abierto para cifrar tus datos
---
![cover](assets/cover.webp)



___



*Este tutorial está basado en contenido original de Florian BURNEL publicado en [IT-Connect](https://www.it-connect.fr/). Licencia [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Se han realizado cambios en el contenido original.*



___



## I. Presentación



En este tutorial, echaremos un vistazo a Picocrypt, un software de cifrado sencillo, ligero y eficaz para cifrar datos con un alto nivel de seguridad.



Adecuado para **encriptar archivos**, puedes usarlo para proteger **datos en tu ordenador, en una memoria USB**, pero también datos almacenados en la Nube. Por ejemplo, puedes cifrar datos y almacenarlos en **Microsoft OneDrive, Google Drive, iCloud o Dropbox**, aunque para este propósito prefiero otro software que se presentará en un próximo artículo.



También puedes utilizarlo cuando necesites **compartir datos con un tercero**: gracias a Picocrypt y a la clave de descifrado, podrán descifrar los datos de su máquina. Así, si tu cuenta o tu ordenador se ven comprometidos, tus datos estarán protegidos.



Para seguir el proyecto Picocrypt, sólo hay un Address:





- [Picocrypt en GitHub](https://github.com/Picocrypt/Picocrypt)



Totalmente **gratuito y de código abierto**, PicoCrypt está disponible para **Windows,** **Linux** y **macOS**. En Windows, puedes instalarlo en tu propia máquina o utilizar la versión portable.



## II. Picocrypt, software de cifrado de código abierto



El software de cifrado Picocrypt** se presenta como **una alternativa** a otras conocidas soluciones como **VeraCrypt** y **Cryptomator** (*diseñadas para cifrar datos en entornos Cloud*), o **AxCrypt**. Por cierto, en el GitHub oficial de Picocrypt, puedes encontrar una comparativa con algunos competidores:



|                | Picocrypt                                                                          | VeraCrypt   | 7-Zip GUI | BitLocker  | Cryptomator |
| -------------- | ---------------------------------------------------------------------------------- | ----------- | --------- | ---------- | ----------- |
| Free           | ✅ Yes                                                                              | ✅ Yes       | ✅ Yes     | ✅ Bundled  | ✅ Yes       |
| Open Source    | ✅ GPLv3                                                                            | ✅ Multi     | ✅ LGPL    | ❌ No       | ✅ GPLv3     |
| Cross-Platform | ✅ Yes                                                                              | ✅ Yes       | ❌ No      | ❌ No       | ✅ Yes       |
| Size           | ✅ 3 MiB                                                                            | ❌ 20 MiB    | ✅ 2 MiB   | ✅ N/A      | ❌ 50 MiB    |
| Portable       | ✅ Yes                                                                              | ✅ Yes       | ❌ No      | ✅ Yes      | ❌ No        |
| Permissions    | ✅ None                                                                             | ❌ Admin     | ❌ Admin   | ❌ Admin    | ❌ Admin     |
| Ease-Of-Use    | ✅ Easy                                                                             | ❌ Hard      | ✅ Easy    | ✅ Easy     | 🟧 Medium   |
| Cipher         | ✅ XChaCha20                                                                        | ✅ AES-256   | ✅ AES-256 | 🟧 AES-128 | ✅ AES-256   |
| Key Derivation | ✅ Argon2                                                                           | 🟧 PBKDF2   | ❌ SHA-256 | ❓ Unknown  | ✅ Scrypt    |
| Data Integrity | ✅ Always                                                                           | ❌ No        | ❌ No      | ❓ Unknown  | ✅ Always    |
| Deniability    | ✅ Supported                                                                        | ✅ Supported | ❌ No      | ❌ No       | ❌ No        |
| Reed-Solomon   | ✅ Yes                                                                              | ❌ No        | ❌ No      | ❌ No       | ❌ No        |
| Compression    | ✅ Yes                                                                              | ❌ No        | ✅ Yes     | ✅ Yes      | ❌ No        |
| Telemetry      | ✅ None                                                                             | ✅ None      | ✅ None    | ❓ Unknown  | ✅ None      |
| Audited        | ✅ [Yes](https://github.com/Picocrypt/storage/blob/main/Picocrypt.Audit.Report.pdf) | ✅ Yes       | ❌ No      | ❓ Unknown  | ✅ Yes       |

Fuente: [Github.com](https://github.com/Picocrypt/Picocrypt)



Picocrypt es **muy ligero**, sólo pesa **3 MB**, y no necesita ser instalado: ¡es una **aplicación portátil** con la ventaja de no requerir derechos de administrador! Sin embargo, no descuida la seguridad, ya que se basa en **algoritmos robustos y fiables**:





- Algoritmo de cifrado XChaCha20**
- Función de anulación de llave **Argon2**



Más allá de las ventajas que acabamos de mencionar, lo que realmente atrae es **su facilidad de uso**



Sólo le falta una cosa: **una auditoría de código**, pero eso está previsto, como puedes ver en la tabla comparativa de arriba (última línea). Pero como es de código abierto, nada te impide echar un vistazo a su código fuente.



Aunque se compara con BitLocker en la tabla anterior, **en mi opinión BitLocker y Picocrypt están pensados para usos diferentes**: BitLocker para cifrar un volumen completo (el de Windows, por ejemplo) y Picocrypt para cifrar una estructura de árbol o espacio de almacenamiento tipo "Drive".



## III. Uso de Picocrypt



Para esta demostración se utilizará una máquina con Windows 11.



### A. Cifrado de datos con Picocrypt



En primer lugar, debes descargar Picocrypt.exe del GitHub oficial ([consulta esta página](https://github.com/Picocrypt/Picocrypt/releases)).



Abra la aplicación para visualizar su minimalista Interface en la pantalla. Para cifrar datos, ya sea **un archivo, varios archivos o una carpeta**, basta con **arrastrarlos y soltarlos en el Interface de Picocrypt**. De este modo, se seleccionarán los datos que se van a cifrar.



![Image](assets/fr/020.webp)



Luego, para la encriptación de datos, tienes acceso a varias opciones, incluida la clave de encriptación. Puede ser **una contraseña segura** o **una clave de cifrado en forma de archivo de claves**, o **ambas**. Si tomamos el ejemplo de una contraseña, puedes elegir entre crear tu propia contraseña o generar una contraseña con Picocrypt.



Esta contraseña debe ser segura, ya que puede utilizarse para descifrar los datos. Introdúcela en "**Contraseña**" y "**Confirmar contraseña**", y haz clic en "**Encriptar**" para encriptar los datos Antes de eso, puedes hacer clic en el botón "**Cambiar**" junto a "**Guardar salida como**" para especificar el directorio de salida.



**Nota**: para utilizar una clave en formato de archivo, haz clic en "**Crear**" a la derecha de "**Archivos de claves**" para crear una clave. A continuación, selecciónela haciendo clic en "**Editar**" y arrastrando y soltando el archivo de claves en el área correspondiente.



![Image](assets/fr/019.webp)



Los dos archivos seleccionados son **cifrados y agrupados** en el archivo "**Encrypted.zip.pcv**", ya que **PCV** es la extensión utilizada por Picocrypt. Este archivo ZIP es ilegible gracias a la encriptación. Para evitar que los archivos seleccionados se agrupen en un único archivo ZIP cifrado, es necesario marcar la opción "**Recursivamente**", de forma que haya tantos archivos cifrados como archivos a cifrar.



Para acceder a nuestros datos, necesitamos desencriptarlos usando Picocrypt.



![Image](assets/fr/023.webp)



Antes de hablar del descifrado de datos, le ofrecemos información sobre algunas de las opciones disponibles:





- Modo paranoico**: utiliza el máximo nivel de seguridad ofrecido por Picocrypt. La herramienta utilizará varios algoritmos de cifrado en cascada (XChaCha20 y Serpent) y HMAC-SHA3 en lugar de BLAKE2b para la autenticación de datos.
- Reed-Solomon**: implementa códigos de corrección de errores *Reed-Solomon* para facilitar la corrección de errores en datos corruptos. Esto le permite soportar un nivel de corrupción de alrededor del 3% de su archivo.
- Dividir en trozos** o **dividir en varias partes**: si estás cifrando un archivo grande, puedes pedir a Picocrypt que lo divida en varias partes. Esto puede facilitar la transferencia del archivo.
- Comprimir archivos** o **Comprimir archivos**: comprime archivos para reducir el tamaño de los archivos encriptados.
- Archivos eliminados** o **Fichiers supprimés**: elimina los archivos de origen para conservar sólo la versión cifrada



### B. Descifrado de datos con Picocrypt



Si necesitas desencriptar los datos, no es más complicado que encriptarlos. Basta con abrir Picocrypt y **arrastrar y soltar el archivo PCV a descifrar**. A continuación, introduce la contraseña y/o selecciona el archivo de claves antes de hacer clic en "**Descifrar**".



![Image](assets/fr/021.webp)



La versión sin cifrar del archivo ZIP "Encrypted.zip" ahora me permite recuperar mis dos archivos en texto claro



![Image](assets/fr/022.webp)



## IV. Conclusión



**Has sido advertido: Picocrypt es muy fácil de usar, ¡y funciona! Aunque es minimalista, incorpora algunas opciones muy útiles para personalizar el cifrado Y como está disponible en versión portátil, puedes llevártelo a todas partes para descifrar tus datos con toda confianza**



Asegúrate de utilizar contraseñas seguras para proteger los datos, y si utilizas un archivo de claves, debes acordarte de hacer una copia de seguridad, de lo contrario ya no podrás descifrar el contenedor PCV generado por Picocrypt. Por último, debes saber que también existe [una versión CLI](https://github.com/Picocrypt/CLI) (con menos funciones) que te permite ejecutar Picocrypt desde la línea de comandos: una vez más, Picocrypt abre la puerta a nuevas posibilidades.



https://planb.network/tutorials/computer-security/data/veracrypt-d5ed4c83-7c1c-4181-95ea-963fdf2d83c5