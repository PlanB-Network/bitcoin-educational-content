---
name: Electrum OP_RETURN
description: Registrar un mensaje en la Blockchain Bitcoin con Electrum
---

![cover](assets/cover.webp)




Este tutorial paso a paso le muestra cómo escribir un mensaje en la Blockchain Bitcoin utilizando la Wallet Electrum. Esta operación utiliza la instrucción OP_RETURN para insertar texto en una transacción, visible públicamente en la Blockchain. Siga estos sencillos pasos para un registro con éxito.



---
## Requisitos previos





- Un ordenador (Windows, macOS o Linux).
- Conexión a Internet.
- Unos cuantos satoshis (Sats) o bitcoins (BTC) en su Wallet para cubrir el importe de la transacción y las comisiones.
- Un conversor de texto a hexadecimal (por ejemplo, un sitio en línea) o una herramienta específica como [este generador de scripts OP_RETURN](https://resources.davidcoen.it/opreturnelectrum/).



---

## Paso 1: Descargar e instalar Electrum



![image](assets/fr/01.webp)



1. Visite el sitio web oficial de Electrum: [electrum.org](https://electrum.org/).


2. Descargue la versión correspondiente a su sistema operativo (Windows, macOS, Linux).


3. Instale Electrum siguiendo las instrucciones del instalador.


4. Compruebe la integridad del archivo descargado (opcional, pero recomendado por razones de seguridad) comparando la firma del archivo o Hash.



→ Más detalles en el tutorial de Electrum :



https://planb.network/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177


---

## Paso 2: Crear o importar una Wallet



1. Lanza Electrum.


2. Seleccione Crear una nueva Wallet o Restaurar una Wallet existente si ya dispone de una frase seed (frase de recuperación).


3. Siga las instrucciones para configurar su Wallet :




 - Para una nueva Wallet, anote su sentencia seed y guárdela en un lugar seguro (papel, caja fuerte, etc.).
 - Para una Wallet existente, introduzca su frase seed para restaurarla.


4. Establece una contraseña para proteger tu Wallet.



→ Más detalles en el tutorial de Electrum :



https://planb.network/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177


---

## Paso 3: Comprobar los fondos disponibles



Asegúrese de que su Wallet contiene suficientes bitcoins (BTC) o satoshis (Sats) para :




- Importe de la transacción (por ejemplo, 0,00001 BTC o 1000 Sats).
- Las comisiones por transacción, que varían en función del tamaño de la red (en general, unos miles de Sats).



Consulte el Saldo en Electrum para comprobar sus fondos.



![image](assets/fr/02.webp)



Si es necesario, transfiera BTC o Sats para alimentar su Wallet. Para ello, vaya a la pestaña "Recibir" y haga clic en "Crear solicitud" :



![image](assets/fr/03.webp)



Esto mostrará una recepción Address:



![image](assets/fr/04.webp)



→ Más detalles en el tutorial de Electrum :



https://planb.network/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177


---

## Paso 4: Preparar el mensaje que se va a inscribir



Seleccione el mensaje que desea introducir (por ejemplo, `Gracias Satoshi`). Nota: Los mensajes OP_RETURN están limitados a 80 bytes, es decir, unos 80 caracteres ASCII.



*Tómate un momento para pensar: lo que escribes en la Blockchain Bitcoin es eterno y accesible a todos, así que :*




- dejan una bella expresión de nuestra humanidad.
- evite introducir contenidos de los que pueda arrepentirse



*Blockchain el espacio y sus bitcoins son preciosos, utilícelos sabiamente y con intención*



Convierte tu mensaje a hexadecimal :




- Puede utilizar una [herramienta en línea](https://www.rapidtables.com/convert/number/ascii-to-hex.html), pero tenga cuidado de no tratar allí datos sensibles (aunque, en principio, la información destinada a ser publicada en Blockchain Bitcoin a través de una OP_RETURN no presenta problemas de confidencialidad);
- Para mayor confidencialidad, realice la conversión localmente utilizando un pequeño programa Python :



```py
#!/usr/bin/env python3

def main():
ascii_text = input("Enter ASCII text: ")
try:
hex_output = ascii_text.encode('ascii').hex()
print(hex_output)
except UnicodeEncodeError:
print("Error: Input contains non-ASCII characters.", file=sys.stderr)

if __name__ == "__main__":
import sys
main()
```



Ejemplo: `Gracias Satoshi` en ASCII da `5468616e6b73205361746f736869` en hexadecimal.



Prepare la secuencia de comandos de la transacción. He aquí un ejemplo del formato esperado:



```script
bc1q879cv4p5q6s9537orange3zss33d3turzad8, 0.00001
script(OP_RETURN 5468616e6b73205361746f736869), 0
```



que se compone de :





- **Destino Address**: Una Bitcoin Address válida. Ici, `bc1q879cv4p5q6s9537orange3zss33d3turzad8`. Puede ser su propia Address, si desea devolverse a sí mismo los fondos transferidos;
- **Importe transferido**: el importe de la transacción, aquí `0.00001` BTC. **Atención**: dado que la unidad utilizada en Electrum es el BTC, el importe indicado en el script de la transacción debe expresarse también en BTC, y no en Sats ;
- Script **OP_RETURN**: El mensaje convertido a hexadecimal precedido de script(`OP_RETURN <mensaje>), 0`. Aquí, `5468616e6b73205361746f736869` para el mensaje en hexadecimal.



⚠️ **Precaución**: Es muy importante indicar `0` después del OP_RETURN, ya que este opcode marca el script como inválido, haciendo que la salida no se pueda gastar permanentemente. Los nodos de red borrarán esta salida de su conjunto UTXO. Si introduces un valor distinto de `0`, se perderá irremediablemente: tus bitcoins se considerarán quemados. Por lo tanto, debes introducir siempre `0` con una OP_RETURN para registrar el dato deseado, pero sin asociarle fondos, que se perderían.



Consejo: Utilice la herramienta [OP_RETURN Generator] (https://resources.davidcoen.it/opreturnelectrum/) para generate el script automáticamente. Aunque esta herramienta sugiera introducir la cantidad en BTC, mantenga la unidad configurada en Electrum.



![image](assets/fr/05.webp)



Para cambiar la unidad utilizada por Electrum, en la barra de menús busque "Preferencias" y, a continuación, en la pestaña "Unidades" seleccione BTC / mBTC / bits o Sats :



![image](assets/fr/06.webp)




---

## Paso 5: Enviar la transacción



En Electrum, vaya a la pestaña Enviar.



![image](assets/fr/07.webp)



En el campo "Pagar a", pegue la secuencia de comandos preparada (por ejemplo, la anterior).



![image](assets/fr/08.webp)



El campo "Pagar a" debe aparecer en Green, y el importe de la transacción debe aparecer en la línea inferior.



Compruebe el importe y su unidad en el campo Importe.



Haga clic en "Pagar..." y ajuste las tarifas de transacción en función del importe que esté dispuesto a pagar y de la velocidad a la que desee que su transacción sea procesada por un Miner e integrada en un bloque.



![image](assets/fr/09.webp)



Pulse OK y confirme la transacción con su contraseña. Aparecerá una ventana de confirmación.




---

## Paso 6: Verificar el registro



Una vez confirmada la transacción (puede tardar unos minutos), vaya a la pestaña "Historial".



![image](assets/fr/10.webp)



Haga clic con el botón derecho en la transacción y seleccione "Ver en el Explorador" para ver los detalles.



Como alternativa, copie el Address de destino (por ejemplo, `bc1q879cv4p5q6s9537orange3zss33d3turzad8`) y visualícelo en un explorador Blockchain como [Mempool.space](https://Mempool.space/) o [blockstream.info](https://blockstream.info/).



Busque el campo OP_RETURN en los detalles de la transacción para ver su mensaje.



![image](assets/fr/11.webp)




![image](assets/fr/12.webp)




---

## Consejos y buenas prácticas





- Pruebe con una cantidad pequeña: Empieza con una transacción pequeña (por ejemplo, Sats 1000) para evitar errores costosos.
- Asegúrese de que la salida que contiene OP_RETURN es igual a cero, de lo contrario sus bitcoins se perderán permanentemente.
- Compruebe la unidad: Asegúrese de que el importe introducido se corresponde con la unidad que aparece en Electrum (BTC, mBTC o Sats).
- Tasa de transacción: Si la red está congestionada, aumenta la comisión para una confirmación más rápida.
- Mensaje corto: Las entradas OP_RETURN están limitadas a 80 bytes. Planifica tu mensaje en consecuencia.



---

## Recursos útiles





- Descargar Electrum: [electrum.org](https://electrum.org/)
- Generador de scripts OP_RETURN: [resources.davidcoen.it/opreturnelectrum/](https://resources.davidcoen.it/opreturnelectrum/)
- Exploradores de Blockchain: [Mempool.space](https://Mempool.space/), [blockstream.info](https://blockstream.info/)