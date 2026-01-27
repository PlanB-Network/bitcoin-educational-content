---
name: Lightning Smoke Machine
description: Dispara una máquina de humo con un pago Lightning a través de ESP32.
---

![cover-lightning-smoke-machine](assets/cover.webp)



## Introducción



Transforma una máquina de humo clásica en un dispositivo pagadero en Bitcoin a través de Lightning Network. ¡Cada pago desencadena automáticamente un chorro de humo!





- Nivel: Intermedio
- Tiempo estimado: 2-3 horas
- Casos de uso: Eventos Bitcoin, actuaciones artísticas, demostraciones de Lightning, efectos escénicos automatizados



## Requisitos previos



### Conocimientos





 - Electrónica básica (cableado, relés)
 - Soldadura (o uso de conectores Dupont)
 - Configuración de red (WiFi, WebSocket)



### Cuentas necesarias





- Servidor BTCPay: Instancia funcional (autoalojada o alojada)
- Blink Wallet : Cuenta + acceso API



### Acceda a





- Acceso de administrador al servidor BTCPay
- Conexión WiFi para ESP32



## Material necesario



### Hardware - Componentes electrónicos





- 1 Microcontrolador - ESP32-WROOM-32


*El ESP32-WROOM-32 es un microcontrolador WiFi/Bluetooth compacto y de bajo coste para conectar dispositivos electrónicos a Internet y controlarlos a distancia*



![ESP32](assets/fr/1.webp)





- 1 Módulo relé - 5V con optoacoplador


*Un relé es como un interruptor que el ESP32 puede accionar para encender o apagar la máquina de humo*



![relay](assets/fr/2.webp)





- ~10 cables Dupont - Macho/Macho y Macho/Hembra



![dupont-cables](assets/fr/3.webp)





- 1 Fuente de alimentación para ESP32 - 5V USB o batería Li-Po



![battery](assets/fr/4.webp)





- 1 cable micro-USB - conexión entre ESP32 y la fuente de alimentación



![micro-usb-cables](assets/fr/5.webp)





- 1 máquina de niebla de 220 V con mando a distancia a pilas de 12 V



![remote-and-smoke-machine](assets/fr/6.webp)





- 1 botella de líquido compatible con su máquina de humo



### Ferretería - Herramientas





- Soldador + estaño (en caso de soldadura)
- Destornillador
- Multímetro (recomendado)



### Software





- Firmware BitcoinSwitch : **[https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/)**
- Navegador web compatible con WebSerial (Chrome/Edge/Brave)
- BTCPay Server configurado. Para obtener más información sobre la creación de una instancia de BTCPay Server, visite este tutorial: https://planb.academy/fr/tutorials/business/point-of-sale/btcpay-server-928eb01e-824b-4b57-a3e8-8727633beddc



## Arquitectura del sistema



![architecture-lightning-smoke-machine](assets/fr/7.webp)



---


**⚠️** **ADVERTENCIA DE SEGURIDAD - LEER ANTES DE CONTINUAR** **⚠️**



En este proyecto se utiliza una máquina de humo conectada a una red de **220 V**. Un funcionamiento incorrecto puede provocar **una electrocución mortal** o **un incendio**.



**Reglas no negociables:**



1. **Desconecte SIEMPRE la máquina de humo de la red eléctrica** antes de abrir el mando a distancia o manipular el cableado


2. **Retire la pila del mando a distancia** antes de manipularlo (riesgo de cortocircuito y daños en los componentes)


3. **Comprueba que todas tus conexiones están aisladas** antes de volver a conectar nada


4. **No vuelva a conectar los 220 V** hasta que la caja del mando a distancia esté cerrada y asegurada



Si no te sientes cómodo con este tipo de manejo, lleva contigo a alguien que sí lo esté.



---

## PARTE 1: Montaje del hardware



### Paso 1: Preparar el mando a distancia



Objetivo: Conectar el relé al botón ON/OFF del mando a distancia


1. Abrir el mando a distancia




    - Identificar el botón ON/OFF
    - Desenrosque la carcasa para abrir el mando a distancia


2. Localizar conexiones




 - Localice los terminales + y - del
 - Prueba de continuidad con un multímetro (opcional)



![smoke-machine-remote](assets/fr/8.webp)



3. Cableado de los botones (soldadura o conectores)




    - Soldar un cable negro al borne - del pulsador
    - Soldar un cable rojo al borne común +



![smoke-machine-remote](assets/fr/9.webp)



### Paso 2: Conexión al módulo de relés



**Recordatorio: Terminología de los relés




| **Terminal**         | **Descripción**           | **Función**                        |
| -------------------- | ------------------------- | ----------------------------------- |
| NO (Normalmente Abierto)   | Circuito abierto por defecto | Se cierra cuando se activa el relé |
| NC (Normalmente Cerrado) | Circuito cerrado por defecto  | Se abre cuando se activa el relé  |
| COM (Común)         | Terminal central          | Conmuta entre NO y NC              |

**Cableado del mando a distancia al módulo de relés:**




- Cable negro del botón ON/OFF **→** NO (normalmente abierto)
- Cable rojo (común) **→** COM (común)



**Lógica:**


Cuando el ESP32 activa el relé, conecta COM y NO, que es exactamente lo mismo que pulsar el botón del mando a distancia.


Cuando el ESP32 corta el relé, COM y NO se separan, lo que equivale a soltar el botón.



![remote-relay](assets/fr/10.webp)



### Paso 3: Conectar el ESP32 al módulo de relés



**Diagrama de cableado:**




| **ESP32** | **→** | **Módulo de relé** |
| --------- | ----- | ----------------- |
| V5 (5V)   | **→** | VCC               |
| GND       | **→** | GND               |
| GPIO 21   | **→** | IN (Entrada)        |

**Verificación:**




- VCC y GND bien conectados (polaridad)
- GPIO 21 utilizado para la señal de control
- No hay cortocircuito visible



![relay-esp32](assets/fr/11.webp)



**Hardware de punto de control**


Antes de cambiar al software, compruebe :




- Mando a distancia correctamente cableado
- Módulo de relés conectado a ESP32
- Ningún cable desnudo en contacto con otros componentes
- 220V siempre desconectado



![relay-esp32](assets/fr/12.webp)





---


## PARTE 2: Configuración del software



Utilizaremos *Blink* como ejemplo, pero *BTCPay Server* también ofrece *Strike, Breez y Boltz* si prefiere otra opción.



### Paso 1: Plugins, Instalación *BitcoinSwitch* + *Blink



1 - Vaya a su instancia *BTCPay Server* con una cuenta de administrador



2 - Cree su primera persiana



3 - En la parte izquierda de *BTCPay Server*, desplácese hasta la parte inferior y vaya a *"Manage Plugins "*



![btcpay-plugins](assets/fr/13.webp)



4 - Vamos a instalar los plugins *BitcoinSwitch* y *Blink*



![btcpay-plugins](assets/fr/14.webp)



5 - Desplácese por la lista de plugins y haga clic en *"Instalar "* : *BitcoinSwitch y Blink* (o el wallet disponible de su elección)



![btcpay-plugins](assets/fr/15.webp)



6 - Una vez finalizada la instalación, reinicie *BTCPay Server* y espere 1 minuto a que se reinicie la instancia



![btcpay-plugins](assets/fr/16.webp)



7 - Cuando vuelva a *"Administrar plugins "*, compruebe que se han instalado ambos plugins



![btcpay-plugins](assets/fr/17.webp)



### Paso 2: Backend : *Configuración del servidor BTCPay + Blink



**1 - Crear un wallet *Blink***




- Visite https://www.blink.sv
- Cree su cuenta. Consulte el tutorial :



[https://planb.academy/tutorials/wallet/mobile/blink-7ea5f5a4-e728-4ff9-b3f9-cf20aa6fc2bd)



**2 - Generar una clave API *Blink***




- Accede a la interfaz de API: **[https://www.blink.sv/en/api](https://www.blink.sv/en/api)** e inicie sesión con la misma cuenta que utilizó para crear su wallet *Blink*



![blink-api](assets/fr/18.webp)





   - Una vez conectado, vaya a la pestaña *Llaves API*



![blink-api](assets/fr/19.webp)





   - Haga clic en *" + en la esquina superior derecha para acceder a la configuración de su clave API



![blink-api](assets/fr/20.webp)





   - Dé un nombre a su Clave API y deje la configuración por defecto. A continuación, en el tercer paso, anote su Clave API - sólo la verá una vez: `blink_mZ5KxxxxxxxxxxxxxNbmX`



![blink-api](assets/fr/21.webp)





   - Una vez creada, debería aparecer en su lista de Claves API activas.



![blink-api](assets/fr/22.webp)



**3 - Conectar *Blink* a *Servidor BTCPay***




- Abra su *Servidor BTCPay*
- Navegar hasta : *Wallet* **→** *Lightning*



![btcpay-server](assets/fr/23.webp)





- Haga clic en *Utilizar un nodo personalizado*
- Pegue la siguiente cadena de conexión:



```
type=blink;server=https://api.blink.sv/graphql;api-key=blink_mZ5KxxxxxxxxNbmX;wallet-id=0a3fc465-082xxxxxxxxxx-2545595d856f
```



**⚠️** **Importante** :




- No modifique la primera parte: `type=blink;server=https://api.blink.sv/graphql`;
- Sustituir sólo :
    - api-key= *por su clave API Blink*
    - wallet-id= *por su wallet Blink* ID
- A continuación, haz clic en *Probar conexión* y luego en *Guardar*



![btcpay-server](assets/fr/24.webp)





 - Compruebe que la conexión está establecida (estado verde)



![btcpay-server](assets/fr/25.webp)



**4 - Crear un punto de venta (PoS)**




- En BTCPay Server, vaya a la pestaña *Plugins* y haga clic en *Point of sale*



![btcpay-server](assets/fr/26.webp)





- Dale un nombre a tu PoS y haz clic en *Crear*



![btcpay-server](assets/fr/27.webp)





- Configuración PoS :
    - Elija un estilo de punto de venta = *Pantalla de impresión*
    - Divisa = *SATS
    - Haga clic en *GUARDAR*



![btcpay-server](assets/fr/28.webp)





- Configuración del producto :
    - Borrar todos los productos por defecto
    - A continuación, haga clic en *añadir elemento*



![btcpay-server](assets/fr/29.webp)



![btcpay-server](assets/fr/30.webp)





- Configura el producto:
    - Título : *máquina de humo*
    - Precio : *10 sats*
    - Bitcoin Interruptor GPIO : 21
    - Bitcoin duración de conmutación (en milisegundos) : 5000
    - Haga clic en *Cerrar* y luego en *Guardar* para guardar el nuevo producto



![btcpay-server](assets/fr/31.webp)



### Paso 3: Firmware: Flashear el ESP32



**1 - Ir al sitio flash




- Ir a : [https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/)



![bitcoinswitch-lnbits](assets/fr/32.webp)



**2 - Flash el firmware BitcoinSwitch**




- Conecte el ESP32 a su ordenador con su cable USB/Micro-USB
- A continuación, haz clic en *Conectar con el dispositivo*
- Se abre una ventana, seleccione el puerto USB de su ESP32, luego haga clic en *Conectar*



![bitcoinswitch-lnbits](assets/fr/33.webp)





- Una vez que tu ESP32 esté conectado, vamos a flashear el firmware de BitcoinSwitch. En la sección *T-Display*, haz clic en *Upload Firmware* para obtener la última versión disponible (actualmente: *bitcoinSwitch T-Display v1.0.1*)



![bitcoinswitch-lnbits](assets/fr/34.webp)





- Espera a que se cargue, el proceso se habrá completado cuando los registros muestren *"Saliendo... "*


![bitcoinswitch-lnbits](assets/fr/35.webp)





- Desenchufa el ESP32



**3 - Comprobar la instalación del firmware BitcoinSwitch




- Recargar página: [https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/)
- Vuelva a conectar el ESP32 a su ordenador con su cable USB/Micro-USB
- A continuación, haz clic en *Conectar con el dispositivo
- Seleccione el puerto USB de su ESP32, a continuación, haga clic en *Conectar* como se ha descrito anteriormente
- Una vez conectado, pulse el botón **RESET** en el ESP32
- Comprueba en los registros que las últimas líneas muestran :



```
Welcome to BitcoinSwitch! (v1.0.1)
Config file does not exist.
Entering config mode. until we receive /config-done.
```



(Esto es normal, significa que aún no hay configuración, pero que el firmware ha sido instalado)



![bitcoinswitch-lnbits](assets/fr/36.webp)



**4 - Generar WebSocket LNURL** URL



Formato final previsto :



```
https://XXXXv/apps/46XXXXXXXXXXXXXXXXXXXXwFB/pos
```



Pasos de la generación :




- Abra su instancia del ServidorBTCPay, luego vaya al PoS que creamos más tarde.
- A continuación, haga clic en "Ver" para abrir su PoS en el navegador



![btcpay-server-https](assets/fr/37.webp)





- Copie la URL de la página, por ejemplo :



![btcpay-server-https](assets/fr/38.webp)



Desgranemos esta URL:



```
https://XXXXv/apps/46XXXXXXXXXXXXXXXXXXXXwFB/pos
```





- `XXXXv` → el dominio de su instancia del servidor BTCPay
- `46XXXXXXXXXXXXXXXXXXwFB` → su identificador único PoS
- `/pos` → indica un punto de venta



Transfórmalo:




- Sustituya `https://` por `wss://`
- Añade `/bitcoinswitch` al final



Resultado:



```
wss://XXXXv/apps/46XXXXXXXXXXXXXXXXXXXXwFB/pos/bitcoinswitch
```



Conserve esta URL para futuras configuraciones, ya que permitirá a su ESP32 comunicarse en tiempo real con BTCPay Server. El protocolo WebSocket (`wss://`) establece una conexión permanente entre ambos: en cuanto se confirma un pago Lightning en su PoS, BTCPay envía instantáneamente la información al ESP32, que puede entonces activar su máquina de humo.



**5 - Configuración de WiFi y WebSocket




- Volver a la página: [https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/) con su ESP32 conectado
- Ve a *Configurar dispositivo* → *Configuración wifi*



Inform :




- WiFi SSID: el nombre de su red WiFi
- Contraseña WiFi: tu contraseña WiFi



![bitcoinswitch-lnbits](assets/fr/39.webp)





- En la sección *LNbits Device URL*, pegue la URL WebSocket creada en el paso anterior
- Haga clic en *Subir configuración*



![bitcoinswitch-lnbits](assets/fr/40.webp)





- Espere a que se complete la carga; los registros deberían mostrar los parámetros que acaba de introducir (SSID, contraseña y URL WebSocket)



![bitcoinswitch-lnbits](assets/fr/41.webp)





- Espere mientras ESP32 establece la conexión WebSocket. Debería ver :



```
WiFi connection established!

[WebSocket] Connected to url: ...
```



![bitcoinswitch-lnbits](assets/fr/42.webp)





- Ahora puede desconectar el ESP32



---
## Software Checkpoint



Antes de la prueba final, compruebe :





- Blink conectado a BTCPay
- PoS creado con al menos 1 artículo
- ESP32 flasheado con BitcoinSwitch
- WiFi configurado en ESP32
- URL WebSocket correcta
- Registros ESP32 sin errores



---

## Pruebas y depuración



### Prueba final completa



1. Enchufe la máquina de humo (220 V) y enciéndala


2. Alimentar el ESP32 (batería o USB)


3. Abra su TPV BTCPay en su navegador


4. Escanear elemento "máquina de humo


5. Pagar con un wallet Lightning (Blink u otro wallet)


6. Observa:




 - El relé hace clic (sonido audible y el LED del relé se enciende)
 - La máquina de humo se activa
 - ¡Humo generado!



### Problemas de equidad y soluciones




| **Problema**                        | **Causa probable**              | **Solución**                                                                                 |
| ----------------------------------- | ------------------------------- | -------------------------------------------------------------------------------------------- |
| ESP32 no se conecta            | Falta de controlador USB             | Instalar [CH340 drivers](https://learn.sparkfun.com/tutorials/how-to-install-ch340-drivers) |
| El relé no hace clic                | Cableado GPIO incorrecto            | Verificar GPIO 21 → IN                                                                        |
| La máquina de humo no responde         | Control remoto incorrectamente cableado         | Verificar NO/NC/COM                                                                           |
| Tiempo de espera de WebSocket                   | URL incorrecta                  | Verificar wss:// y /bitcoinswitch                                                            |
| WiFi no se conecta             | SSID/Contraseña incorrecto            | Re-grabar la configuración de WiFi                                                                    |
| Pago recibido pero nada sucede | ESP32 no conectado a WebSocket | Verificar registros de RESET                                                                      |

## Recursos



### Enlaces útiles





- Firmware BitcoinSwitch: [https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/)
- BTCPay Server Docs : [https://docs.btcpayserver.org/](https://docs.btcpayserver.org/)
- Blink API : [https://dev.blink.sv/](https://dev.blink.sv/)
- ESP32 Pinout : [https://randomnerdtutorials.com/esp32-pinout-reference-gpios/](https://randomnerdtutorials.com/esp32-pinout-reference-gpios/)



### Comunidad y apoyo





- Servidor BTCPay** : [chat.btcpayserver.org](https://chat.btcpayserver.org/) - Mattermost Oficial
- Servidor BTCPay Telegram** : [t.me/btcpayserver](https://t.me/btcpayserver)
- LNbits** : [t.me/lnbits](https://t.me/lnbits) - Telegram oficial, comunidad activa
- BitcoinSwitch (errores de firmware)**: [github.com/lnbits/bitcoinswitch/issues](https://github.com/lnbits/bitcoinswitch/issues)



### Código fuente





- Código fuente del firmware de BitcoinSwitch: [https://github.com/lnbits/bitcoinswitch](https://github.com/lnbits/bitcoinswitch)



---

**⚡** ¡Apila sats, haz humo, diviértete, mantente humilde! **⚡**