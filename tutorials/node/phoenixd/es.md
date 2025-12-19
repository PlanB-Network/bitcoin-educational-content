---
name: Phoenixd
description: Despliegue su propio nodo Lightning minimalista con Phoenixd
---

![cover](assets/cover.webp)



La autonomía financiera también significa controlar tu infraestructura Lightning. Para los desarrolladores y las empresas que deseen integrar Bitcoin Lightning en sus aplicaciones, **Phoenixd** representa la solución ideal: un nodo Lightning minimalista y especializado con gestión automática de la liquidez.



Phoenixd es un servidor Lightning desarrollado por ACINQ, diseñado específicamente para enviar y recibir pagos Lightning a través de una API HTTP. A diferencia de las implementaciones con todas las funciones, como LND o Core Lightning, Phoenixd abstrae toda la complejidad de la gestión de canales al tiempo que preserva la autoprotección de sus fondos.



En este tutorial, veremos cómo instalar, configurar y utilizar Phoenixd para desarrollar aplicaciones Lightning con una infraestructura autoalojada y una API fácil de usar.



## ¿Qué es Phoenixd?



Phoenixd es un nodo Lightning mínimo y especializado desarrollado por ACINQ. Es una solución diseñada para desarrolladores y empresas que deseen integrar Lightning en sus aplicaciones sin la complejidad de gestión de un Full node.



### Principio de funcionamiento



**Phoenixd es un nodo Lightning mínimo que utiliza ACINQ como su LSP (Lightning Service Provider) para obtener liquidez automática. Cuando recibe pagos Lightning, abre automáticamente canales con nodos ACINQ para asignar la capacidad entrante necesaria. Esta liquidez "sobre la marcha" es instantánea, pero se cobra exactamente al **1% + tasas Mining** de la cantidad recibida.



**Gestión automatizada:** El sistema gestiona tres Elements clave:




- Canales Lightning**: Abre, cierra y gestiona automáticamente según sea necesario
- Liquidez entrante/saliente**: Provisión automática mediante empalme y apertura de canales
- Crédito de tasas** : Los pequeños pagos insuficientes para justificar un canal se almacenan como provisión para futuros cargos



### Beneficios de Phoenixd



**Usted controla sus claves privadas (seed de 12 palabras) y sus fondos. Phoenixd genera su Wallet localmente sin compartir nunca sus claves.



**Infraestructura personal:** Phoenixd se ejecuta en su servidor, dándole acceso a registros detallados, configuración y control de la API. Ya no dependes de un servicio de terceros para acceder a tus fondos.



**API integrada:** Phoenixd cuenta con una API HTTP para la integración con otros servicios, soporte nativo LNURL y desarrollo de aplicaciones personalizadas.



**Facilidad de integración:** Gracias a su sencilla API REST, Phoenixd puede integrarse en cualquier aplicación o servicio que requiera pagos Lightning.



**Nota importante:** La liquidez automática sigue procediendo de ACINQ como LSP (Lightning Service Provider). Phoenixd utiliza el mismo mecanismo que Phoenix mobile para la gestión automática de canales.



## Instalación de Phoenixd



### Requisitos previos



Phoenixd requiere un entorno Linux (se recomienda Ubuntu/Debian), con algunos conocimientos básicos de línea de comandos. Para un rendimiento óptimo, necesitará :





- Servidor Linux**: VPS o máquina local con conexión estable
- OpenJDK 21** : Entorno de ejecución Java
- Conexión estable a Internet**: Para la sincronización con el Lightning Network
- Nombre de dominio** (opcional) : Para un acceso HTTPS seguro a la API



### Descarga e instalación



**1. Descargar Phoenixd**



Vaya a la página [GitHub releases](https://github.com/ACINQ/phoenixd/releases) y descargue la última versión para su arquitectura:



```bash
# For Linux x86_64
# Replace with the latest release
wget https://github.com/ACINQ/phoenixd/releases/download/v0.6.1/phoenixd-0.6.1-linux-x64.zip
unzip -j phoenixd-0.6.1-linux-x64.zip
chmod +x phoenixd phoenix-cli
```



**2. Primera puesta en marcha



Inicie Phoenixd para la inicialización:



```bash
./phoenixd
```



En el primer inicio, se le pedirá que confirme dos pasos importantes escribiendo "Entiendo" :



**Mensaje 1 - Copia de seguridad:**


```
This software is self-custodial, you have full control and responsibility over your funds.
Your 12-words seed is located in /home/<user>/.phoenix, make sure to do a backup or you risk losing your funds.
Do not share the same seed with other phoenix instances (mobile or server), it will cause issues and channel force closes.
```



**Guarda estas 12 palabras** - es tu única garantía de recuperación.



**Mensaje 2 - Liquidez automática:**


```
Continuous liquidity
Liquidity management is fully automated.
When receiving a Lightning payment that doesn't fit in your existing channel:
- If the payment amount is large enough to cover mining fees and service fees for automated liquidity,
then your channel will be created or enlarged right away.
- If the payment is too small, then the full amount is added to your fee credit,
and will be used later to pay for future fees. The fee credit is non-refundable.
```



Escriba "Comprendo" para cada confirmación.



![Premier démarrage](assets/fr/01.webp)



*Phoenixd arranca por primera vez: confirmaciones de seguridad y liquidez automática*



**3. Configuración en servicio** (sólo en francés)



Para un funcionamiento continuo, cree un archivo systemd :



```bash
sudo nano /etc/systemd/system/phoenixd.service
```



```ini
[Unit]
Description=Phoenixd - Minimalist Lightning node
After=network.target

[Service]
User=your_user
WorkingDirectory=/home/your_user
ExecStart=/home/your_user/phoenixd
Restart=on-failure
RestartSec=5

[Install]
WantedBy=multi-user.target
```



```bash
sudo systemctl daemon-reload
sudo systemctl enable phoenixd
sudo systemctl start phoenixd
```



![Service systemd](assets/fr/02.webp)



*Servicio Phoenixd activo y operativo mediante systemd y `auto-liquidity` a 2m sat*



## Configuración y seguridad



### Archivo de configuración



Phoenixd crea automáticamente `~/.phoenix/phoenix.conf` con los parámetros esenciales:



```conf
# Network (mainnet by default)
chain=mainnet

# Size of automatic channels and requested liquidity amount (in satoshis)
auto-liquidity=2000000

# API configuration
http-bind-address=127.0.0.1
http-bind-port=9740
http-password=auto_generated_password
http-password-limited-access=limited_password
```



**Parámetros clave:**




- `auto-liquidez`: Tamaño de los canales abiertos automáticamente (por defecto: 2M Sats)
- http-password`: Contraseña de administrador para API (creación de Invoice Y envío de pagos)
- http-password-limited-access`: Contraseña restringida (sólo creación Invoice)



### Acceso seguro con HTTPS



Por defecto, la API Phoenixd sólo es accesible a través de HTTP local (`http://127.0.0.1:9740`). Para utilizar su nodo desde el exterior (aplicaciones móviles, otros servidores, integraciones web), debe configurar un acceso HTTPS seguro.



**Principio de proxy inverso:**


```
Internet → nginx (port 443 HTTPS) → Phoenixd (port 9740 HTTP local)
```



**Nginx** actúa como **proxy inverso**: escucha las peticiones HTTPS de Internet en el puerto 443, las redirige a Phoenixd localmente (puerto 9740), y luego envía respuestas cifradas de vuelta al cliente.



**El certificado SSL/TLS** es un archivo digital que :




- Demuestre la identidad de su servidor** (evita los ataques de intermediario)
- Habilita el cifrado HTTPS**: todos los datos, incluidas las contraseñas de la API, se cifran durante el transporte
- Emitido gratuitamente** por Let's Encrypt a través de la herramienta certbot



Esta configuración le permite :




- Acceso seguro a la API desde Internet**
- Cifre sus contraseñas API** durante el transporte (para evitar que se transmitan en texto claro)
- Integrar Phoenixd** en aplicaciones externas que requieran HTTPS
- Cumplimiento de las normas de seguridad** para API financieras



Configurar este proxy inverso HTTPS con nginx :



**1. Configuración de Nginx



```bash
sudo apt install nginx certbot python3-certbot-nginx
sudo nano /etc/nginx/sites-available/phoenixd.conf
```



```nginx
server {
listen 80;
server_name phoenixd.your-domain.com;

location / {
proxy_pass http://127.0.0.1:9740;
proxy_set_header X-Real-IP $remote_addr;
proxy_set_header Host $host;
}
}
```



```bash
sudo ln -s /etc/nginx/sites-available/phoenixd.conf /etc/nginx/sites-enabled/
sudo nginx -t && sudo systemctl reload nginx
```



**2. Certificado SSL



```bash
sudo certbot --nginx -d phoenixd.your-domain.com
```



### Prueba de funcionamiento



Compruebe que Phoenixd funciona correctamente:



```bash
./phoenix-cli getinfo
./phoenix-cli getbalance
```



Estos comandos deben devolver información JSON sobre el estado y el saldo del nodo (inicialmente vacío).



![Commandes CLI](assets/fr/03.webp)



*Comandos getinfo y getbalance para comprobar el estado de los nodos*



## Uso de la API



### Primera prueba de recepción



**1. Crear un Rayo** Invoice



Utilice la API para crear su primer Invoice:



```bash
curl -X POST http://localhost:9740/createinvoice \
-u :your_password \
-d description='First test' \
-d amountSat=100000
```



### Comprender el mecanismo automático de liquidez



**Principio fundamental:** Cuando recibe un pago Lightning, Phoenixd a veces tiene que abrir un nuevo canal para poder recibirlo. Esta apertura de canal tiene un coste que se **deduce automáticamente** del importe recibido.



**Ejemplo concreto con 100.000 Sats:**



![Premier test de réception](assets/fr/04.webp)



*Primera prueba de aceptación: Sats 100k recibidos, saldo final de Sats 75.561 tras deducción de los costes de liquidez*



```bash
# Payment received: 100,000 sats
# Channel created: 2,115,000 sats total capacity
# Liquidity fee: 24,439 sats
# Final balance: 75,561 sats
```



**Cálculo de tarifas:**




- Canon de servicio**: 1% de la capacidad del canal (2.115.000 Sats) = 21.150 Sats
- Mining tasas**: ~3.289 Sats (por transacción On-Chain)
- Total**: 24.439 Sats deducidos automáticamente



**Verificación con comandos CLI:**


```bash
# View details of all channels
./phoenix-cli listchannels

# Important output:
# "toLocal": 75561000 (your balance in milli-sats)
# "toRemote": 2039439000 (ACINQ's balance)
# Total channel: 2,115,000 sats
```



![Nouveau solde après paiement](assets/fr/05.webp)



*Saldo final tras el envío del pago: 257 Sats restantes tras el envío del Rayo*



**Si recibes pagos demasiado pequeños para justificar la apertura de un canal (< aprox. 25k Sats), se almacenan en un "crédito de cuota" no reembolsable. Este crédito se utilizará para pagar futuras cuotas de canal cuando recibas una cantidad suficiente.



**2. Sigue la apertura del canal**



Mira los registros de Phoenixd:



```bash
journalctl -u phoenixd -f
```



Verá la apertura del canal y la deducción automática de las comisiones de liquidez. Las comisiones varían según las condiciones de Mempool Bitcoin, pero siempre incluyen un 1% de comisión de servicio más la comisión vigente de Mining.



**3. Comprobar canal**



```bash
./phoenix-cli listchannels
```



Este comando muestra tus canales activos con su estado y saldo.



### Operaciones API completas



Phoenixd expone una API REST en el puerto 9740 que permite :



**Operaciones básicas:**


```bash
# Create an invoice
curl -X POST http://localhost:9740/createinvoice \
-u :your_password \
-d description='Test payment' \
-d amountSat=100000

# Send a payment (routing fee 0.4%)
curl -X POST http://localhost:9740/payinvoice \
-u :your_password \
-d invoice='lnbc...'

# Check balance
curl http://localhost:9740/getbalance \
-u :your_password

# Send on-chain funds (in case of channel closure)
./phoenix-cli sendtoaddress \
--address bc1q... \
--amountSat 50000 \
--feerateSatByte 12
```



**Importante sobre los costes:**




- Recibo**: 1% + Mining tasa de liquidez automática
- Gastos de envío**: 0.4% de gastos de envío en la Lightning Network



**Webhooks:** Los Webhooks permiten a Phoenixd **notificar automáticamente** a sus aplicaciones cuando se produce un evento (pago recibido, Invoice pagado, canal abierto, etc.). En lugar de pedir constantemente actualizaciones a Phoenixd, su aplicación recibe una notificación HTTP instantánea.



**Su tienda en línea recibe automáticamente una notificación cuando un cliente paga un pedido, lo que permite la validación instantánea de la transacción.



Configuración en `phoenix.conf` :


```conf
webhook-url=https://your-app.com/webhook-phoenixd
webhook-secret=votre_secret_de_verification
```



## Aplicaciones avanzadas



### Integraciones LNURL



Phoenixd soporta de forma nativa los protocolos LNURL para una integración avanzada:



**LNURL-Pay:** Pague por servicios compatibles con LNURL


```bash
curl -X POST http://localhost:9740/lnurlpay \
-u :your_password \
-d lnurl=LNURL1DP68GURN8GHJ7MRWW4EXCTN... \
-d amountSat=100
```



**LNURL-Withdraw :** Recuperar fondos de los servicios LNURL


```bash
curl -X POST http://localhost:9740/lnurlwithdraw \
-u :your_password \
-d lnurl=lightning:LNURL1DP68GURN8GHJ7MRW...
```



**LNURL-Auth:** Autenticación a través de Lightning para acceder a los servicios


```bash
curl -X POST http://localhost:9740/lnurlauth \
-u :your_password \
-d lnurl=lnurl1dp68gurn8ghj7um5v93kket...
```



### Integración con LNbits



LNbits puede utilizar Phoenixd como fuente de financiación según su [documentación oficial](https://docs.lnbits.org/guide/wallets.html):



**Configuración de LNbits:**


```bash
LNBITS_BACKEND_WALLET_CLASS=PhoenixdWallet
PHOENIXD_API_ENDPOINT=http://localhost:9740/
PHOENIXD_API_PASSWORD=your_password_phoenixd
```



Esta integración le permite crear subcuentas de LNbits alimentadas por su nodo Phoenixd, proporcionando un Interface basado en web para gestionar múltiples monederos Lightning.



### Aplicaciones personalizadas



Gracias a su completa API REST, puede desarrollar aplicaciones :



**Comercio electrónico:** Integración directa de los pagos Lightning en su tienda


**Servicios de donación:** Sistemas de donación con facturas y webhooks automáticos


**Bots de redes sociales:**Bots de Telegram/Discord con funciones de propina


**Paywall Lightning:** Contenidos premium disponibles por una tarifa Lightning



## Seguridad y buenas prácticas



### Protección de acceso



**Contraseñas de API:** Las contraseñas generadas automáticamente son las llaves de tu tesoro Lightning. No las compartas nunca y cámbialas en caso de duda.



**Firewall:** Nunca deje el puerto 9740 abierto directamente a Internet. Utilice siempre nginx con HTTPS.



**Autenticación mejorada:** Considera una VPN o Tailscale para restringir el acceso a tu servidor sólo a dispositivos autorizados.



### Copias de seguridad esenciales



**Recuperación de seed:** Guarda tus 12 palabras en un lugar seguro, fuera del servidor. Esta es tu única garantía de recuperación.



*directorio ~/.phoenix:** Realice copias de seguridad periódicas de esta carpeta (después de apagar Phoenixd) para conservar el estado del canal y acelerar la restauración.



**Códigos de recuperación de servicios:** Guarde también los códigos de copia de seguridad de todos los servicios en los que active 2FA con su Phoenix.



### Control y mantenimiento



**Registros de seguimiento:**


```bash
journalctl -u phoenixd -f  # Real-time logs
./phoenix-cli getinfo      # Node status
```



**Actualizaciones:** Consulte [GitHub releases](https://github.com/ACINQ/phoenixd/releases) para conocer las nuevas versiones. La actualización es tan sencilla como sustituir el binario y reiniciar el servicio.



## Comparación con alternativas



### Phoenixd vs Phoenix estándar



**Estándar Phoenix (móvil) :**




- ✅ Instalación inmediata, configuración cero
- ✅ Interface móvil intuitivo
- ✅ Mismo autoguardado que Phoenixd
- ❌ Sin API para desarrolladores
- ❌ Sin acceso a registros detallados



**Phoenixd (servidor) :**




- aPI HTTP para integraciones
- ✅ Acceso total a los registros
- infraestructura personal
- ❌ Requiere conocimientos técnicos
- ❌ Se requiere mantenimiento del servidor



**Ambos utilizan ACINQ como PSL para la liquidez automática.



### Phoenixd contra LND/Core Lightning



**LND/Core Lightning :**




- ✅ Control total, protocolo Lightning completo
- ✅ Gran comunidad, ecosistema maduro
- ❌ Gestión manual compleja de la liquidez
- ❌ Gran curva de aprendizaje



**Phoenixd :**




- ✅ Gestión automática de la liquidez (como Phoenix mobile)
- ✅ API para desarrolladores
- ✅ Configuración simplificada
- ❌ Utiliza ACINQ como LSP (sin enrutamiento independiente)
- ❌ Menos flexible que los nodos completos



## Resolución de problemas comunes



### Problemas de acceso a la API



**Error "Autenticación fallida":**


1. Compruebe la contraseña en el archivo `~/.phoenix/phoenix.conf`


2. Comprobar el formato de autenticación `-u:password`


3. Asegúrese de que Phoenixd se está ejecutando (`./phoenix-CLI getinfo`)



**Tiempos de conexión:**




- Compruebe que Phoenixd está escuchando en el puerto correcto (9740)
- Probar el acceso local antes de configurar HTTPS
- Compruebe los registros: `journalctl -u phoenixd -f`



### Problemas de liquidez



**Los pagos no llegan :**


1. Compruebe que el importe supera el umbral mínimo (~30k Sats)


2. Consultar los registros para identificar errores de canal


3. Reinicie Phoenixd si es necesario



**Saldo en "crédito de gastos":**


Los pagos pequeños se almacenan como provisión. Recibe una cantidad mayor para activar la apertura del canal y liberar estos fondos.



## Conclusión



Phoenixd representa un excelente compromiso entre facilidad de uso y soberanía técnica para los desarrolladores. Ofrece una API Lightning sencilla pero potente con gestión automática de la liquidez, eliminando la complejidad de los nodos Lightning tradicionales.



Esta solución es especialmente adecuada para desarrolladores y empresas que deseen :




- Integre Bitcoin Lightning en sus aplicaciones
- Evite la complejidad de la gestión de canales de rayos
- Benefíciese de una infraestructura autoalojada
- Una API sencilla y fiable



Con Phoenixd, construyes tu propia infraestructura Lightning privada con una moderna API REST y gestión automática de los aspectos técnicos. Es la solución ideal para democratizar la integración de Lightning en tus proyectos.



## Recursos útiles



### Documentación oficial




- GitHub Phoenixd** : [github.com/ACINQ/phoenixd](https://github.com/ACINQ/phoenixd) - Código fuente y versiones
- Sitio del servidor Phoenix**: [phoenix.acinq.co/server](https://phoenix.acinq.co/server) - Documentación completa
- FAQ Phoenixd** : [Phoenix.acinq.co/server/faq](https://phoenix.acinq.co/server/faq) - Preguntas más frecuentes



### Apoyo comunitario




- GitHub Issues** : [github.com/ACINQ/phoenixd/issues](https://github.com/ACINQ/phoenixd/issues) - Asistencia técnica
- Twitter ACINQ** : [@ACINQ_co](https://twitter.com/ACINQ_co) - Noticias y anuncios