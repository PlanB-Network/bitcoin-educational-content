---
name: BIP-85
description: ¿Cómo puedo utilizar el BIP-85 para generate múltiples frases-semilla de un seed principal?
---
![cover](assets/cover.webp)



## 1. Comprender el PIF-85



### 1.1 ¿Qué es la BIP-85?



BIP-85 es una función avanzada que permite crear varias **Frases secundarias seed** a partir de una **Frase principal seed**.



Cada sentencia secundaria seed puede utilizarse para crear una cartera Bitcoin completamente independiente. Estas carteras pueden utilizarse para diversos fines: una Hot Wallet en el móvil, una cartera para un familiar, una cartera de ahorros independiente, etc.



Todas las subfrases de seed son **derivadas matemáticamente**, pero es **imposible remontarse a la frase principal de seed** a partir de una subfrase. Esto garantiza una separación completa entre cada cartera.



Siempre que tenga acceso a su frase principal seed (y a la passphrase asociada si está utilizando una), puede regenerar cualquier frase secundaria seed **idénticamente**, sin tener que guardarla por separado.



### 1.2 ¿Por qué utilizar la BIP-85?



BIP-85 es útil si desea :





- Cree varias carteras Bitcoin independientes sin múltiples copias de seguridad
- Gestiona tus fondos según diferentes usos (ahorro, gastos, familia, proyectos)
- Garantizar la protección de los familiares (función "Tío Jim")
- Elimine una cartera sin perder el acceso a sus fondos
- Simplifique su seguridad: sólo tiene que proteger una frase clave seed



### 1.3 Ventajas sobre BIP-32



Con BIP-32, una única sentencia seed puede utilizarse para generate una jerarquía completa de cuentas y direcciones Bitcoin, utilizando rutas de derivación (por ejemplo: `m/44'/0'/0'/0/0`). Cada ruta puede representar una cuenta independiente, pero **todas permanecen vinculadas a la misma frase seed**. Así, si esta frase seed se ve comprometida, **todas las cuentas derivadas se vuelven accesibles**.



Con BIP-85, una sentencia principal seed puede utilizarse para generate varias sentencias secundarias seed totalmente independientes: **si una de estas semillas secundarias se ve comprometida, el atacante nunca podrá volver a la seed principal ni acceder a las otras carteras**.


Esto permite compartimentar los riesgos:





- Puede utilizar una seed secundaria para Hot Wallet o uso temporal, aceptando una mayor exposición.
- Incluso si esta Hot Wallet se ve comprometida, sus otros fondos, protegidos por otras semillas secundarias o mantenidos fuera de línea, **permanecen seguros**.



Por otra parte, tanto para el BIP-32 como para el BIP-85, si el seed principal se ve comprometido, **todos los fondos son vulnerables**. Por lo tanto, es crucial protegerlo con el máximo nivel de seguridad.



![image](assets/fr/02.webp)


## 2. Casos prácticos de utilización de la BIP-85



BIP-85 le permite crear varias carteras Bitcoin a partir de una única frase principal seed, cada una con su propia frase secundaria seed. He aquí cinco casos prácticos de uso para organizar y asegurar sus fondos Bitcoin. Cada caso explica por qué el uso de BIP-85 es más práctico que la gestión de múltiples cuentas con una única frase seed a través de BIP-32.



### 2.1 Limitar el riesgo de una cartera menos segura





- Escenario**: Usted utiliza un Wallet "Hot" (instalado en un dispositivo conectado a Internet), para las transacciones diarias.
- Solución BIP-85**: Se crea una frase secundaria seed dedicada a esta cartera.
- Ventaja sobre BIP-32**: No necesitas importar la frase primaria seed a tu teléfono, reduciendo el riesgo de hackeo. Sólo se compromete la frase secundaria de seed, protegiendo sus otros monederos. Con BIP-32, necesitas utilizar la frase principal seed y una ruta de bypass, exponiendo todos tus fondos.



### 2.2 Crear una cartera para un familiar





- Escenario**: Creas un Bitcoin Wallet para alguien cercano (por ejemplo, tu madre), pudiendo recuperarlo si lo pierde.
- Solución BIP-85**: Creas una sentencia secundaria seed dedicada y compartes sólo ésta.
- Ventaja sobre BIP-32**: Con BIP-32, crear una cuenta para un ser querido requiere o bien compartir su frase principal de seed, arriesgando todos sus fondos y complicando la gestión para su ser querido (gestión de rutas de ramificación), o bien crear una nueva frase de seed para guardar además de su frase principal de seed.



### 2.3 Facilitar la gestión de carteras separadas





- Escenario**: Usted separa sus bitcoins para diferentes propósitos (por ejemplo, ahorros a largo plazo, fondos no KYC).
- Solución BIP-85**: Creas frases secundarias seed dedicadas a cada objetivo.
- Ventaja sobre BIP-32**: Con BIP-32, todas las cuentas comparten la misma frase seed, lo que complica la gestión en carteras de terceros al tener que gestionar rutas de derivación como `m/44'/0'/0'`. Además, no es posible asignar una cuenta separada por dispositivo (por ejemplo, "ahorros en Coldcard", "diario en móvil", "vacaciones en Trezor"). BIP-85 asigna una única frase secundaria seed por objetivo, que es fácil de identificar e importar por separado en cada dispositivo.



### 2.4 Utilización de una Wallet temporal para las transacciones





- Escenario**: Necesita una cartera temporal para una transacción puntual o para preservar la confidencialidad (por ejemplo: mezcla de fondos, interacción con un Exchange KYC, etc.).
- Solución BIP-85**: Se crea una sentencia secundaria seed, se utiliza para la transacción y luego se destruye si es necesario, sabiendo que se puede regenerar.
- Ventaja sobre BIP-32**: Con BIP-32, una cuenta temporal depende de la sentencia principal seed, exponiendo todos sus fondos si se ve comprometida.





## 3. Antes de empezar





- Hardware** (opcional)
 - Coldcard Mk4 o Q1
 - Tarjeta MicroSD





- Conocimientos básicos
 - Comprensión de frases Mnemonic (BIP-39): una lista de 12 a 24 palabras para guardar una carpeta.
 - Sepa qué es un Bitcoin Wallet: software o dispositivo para gestionar sus bitcoins, y cómo restaurarlo con una frase Mnemonic.
 - Más recursos en los Anexos.





- Software compatible
 - Sparrow wallet (ordenador, para sólo vigilancia o gestión avanzada)
 - Nunchuck (móvil, para multifirmas)
 - BlueWallet (móvil)
 - ...





- 3.4 Configuración Coldcard
 - Inicializar una frase seed de 24 palabras en la Coldcard.
 - Opcional: Añada un passphrase para asegurar el acceso a las sucursales BIP-85.
 - Activar opciones útiles: NFC (para exportar), desactivar USB en batería (seguridad).




## 4. Tutorial paso a paso



Siga estos pasos para crear, utilizar y recuperar un Mnemonic secundario con BIP-85 en su Coldcard.



### 4.1 generate a seed frase secundaria



Creará una frase secundaria seed a partir de su frase principal seed.


Encienda su tarjeta Coldcard, introduzca su código PIN.





- 1. Si has aplicado una passphrase a tu seed principal:**
 - En la pantalla de inicio, vaya a `passphrase`.
    - Elija `Añadir palabra` e introduzca su contraseña.
    - Pulse "Aplicar".
    - Compruebe la identidad de Wallet: Vaya a `Avanzado > Ver identidad` para anotar la huella digital de Wallet.





- 2. Ir al menú BIP-85
 - En la pantalla de inicio, vaya a `Avanzado > Derivar seed B85`
 - Lea la advertencia y confirme.



La ColdCard le informa de que las semillas generadas se derivan matemáticamente de su seed principal, pero son criptográficamente totalmente independientes.


![image](assets/fr/03.webp)





- 3. Elija un formato


Seleccione el formato de frase seed: 12, 18 ó 24 palabras. Compruebe el número de palabras aceptadas por la Wallet en la que desea importar su frase seed.


![image](assets/fr/04.webp)





- 4. Seleccionar índice
 - Introduzca un índice entre 0 y 9999.
 - Este índice es crucial para regenerar el seed secundario más adelante. Guárdelo cuidadosamente con una etiqueta como: "Índice 1 = Wallet móvil", "Índice 2 = proyecto familiar", "Índice 4 = mezcla de prueba", ...
 - Si lo pierdes, no perderás el acceso a tus fondos, pero tendrás que probar combinaciones de 0 a 9999 para encontrarlos.


![image](assets/fr/05.webp)





- 5. Nota o exportación seed frase secundaria**


ColdCard muestra ahora una nueva frase secundaria seed. Puede :




 - La **nota manual**.
 - Prensa :
     - 1` para guardarlo en la tarjeta SD
     - `2` para **entrar en modo "usar esta seed"** en la ColdCard (útil para exportar o firmar una transacción)
     - 3` para mostrar un **código QR** (para escanear con una aplicación móvil como BlueWallet o Nunchuck)
     - 4` para enviarlo por **NFC**



💡 En este punto, tienes una frase seed independiente, utilizable en cualquier BIP39 Wallet (Trezor, Ledger, BlueWallet, Nunchuck...).


![image](assets/fr/06.webp)


![image](assets/fr/07.webp)


### 4.2 Utilización de la seed secundaria



Ahora puede utilizar esta seed derivada para crear una nueva cartera en :




- una aplicación móvil
- otra Hardware Wallet
- una cartera Multisig



### 4.3 Recuperación de una frase secundaria perdida de seed



Para recuperar una seed secundaria en cualquier momento, repita el proceso:


1. Reinicie su ColdCard


2. Introduzca su PIN


3. Introduzca su passphrase, si está definido


4. Vaya a `Avanzado > Derivar seed B85`


5. Elija formato (12/18/24 palabras)


6. Introduzca el mismo índice (por ejemplo, `1`)


7. Obtendrás exactamente el mismo secundario seed




## 5. Límites, riesgos y buenas prácticas



### 5.1 Dependencia de la frase principal seed + passphrase



El uso de BIP85 depende totalmente de la frase principal seed de 24 palabras, así como de passphrase si ha aplicado una.




- A partir de estas dos Elements, se pueden regenerar todas las frases secundarias seed.
- Sin una de estas 2 Elements, pierdes el acceso a todas las carteras de derivados.



### 5.2 Riesgos de la configuración multifirma



Desaconsejamos encarecidamente el uso de frases seed secundarias generadas a partir de la misma frase seed primaria en una configuración multi-sig: si el dispositivo o la frase seed primaria se ven comprometidos, todas las claves multi-sig podrían ser regeneradas por un atacante.



### 5.3 Compatibilidad del software



No todas las aplicaciones admiten directamente la derivación BIP85. Sin embargo, las semillas generadas mediante BIP85 son semillas BIP39 estándar (12, 18 o 24 palabras), por lo que pueden utilizarse en cualquier cartera compatible con BIP39.



### 5.4 Registro de cuentas BIP85



Se recomienda llevar un registro personal actualizado de las frases secundarias seed.




- Le permite saber rápidamente qué índice BIP85 corresponde a qué cartera, sin tener que guardar seed frases secundarias.
- Este registro debe ser minimalista, sin mención explícita de Bitcoin, y debe almacenarse separado del seed principal. Recuerda mencionarlo en tu plan de sucesión.



El registro puede contener :




- bIP85 índice utilizado (número de 0 a 9999)
- un nombre de uso o referencia (por ejemplo, Hot Wallet, ahorros personales, Wallet de mamá)
- en caso necesario, la huella dactilar de Wallet para su verificación en ColdCard



### 5.5 Respaldo



Las copias de seguridad deben incluir :




- la seed principal
- gW-76 (si se utiliza)



No guardar nunca juntos:




- los principales seed y passphrase
- el seed principal y el registro de cuentas BIP85



Más recursos en los Anexos.




## ANEXOS



## A.1 Glosario





- [BEEP](https://planb.network/resources/glossary/bip)
- [BIP-32](https://planb.network/resources/glossary/bip0032)
- [BIP-39](https://planb.network/resources/glossary/bip0039)
- [BIP-85](https://planb.network/resources/glossary/bip0085)
- [seed frase](https://planb.network/resources/glossary/recovery-phrase)
- [passphrase](https://planb.network/resources/glossary/passphrase-bip39)
- [Multisig](https://planb.network/resources/glossary/multisig)




### A.2 Guarda tu frase de recuperación



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270


### A.3 Comprender el PIF39 de passphrase



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7


### A.4 Funcionamiento de las carteras Bitcoin



https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f