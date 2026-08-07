---
name: Actualizar BTCPay Server
description: Aplica una actualización de seguridad a tu instancia de BTCPay Server y rota las credenciales que importan
---

![cover](assets/cover.webp)

Gestionar tu propio procesador de pagos significa que también eres tu propio equipo de seguridad. Cuando los mantenedores de BTCPay Server publican una versión de seguridad, nadie va a parchear tu instancia por ti: la actualización, la verificación y la rotación de credenciales que le sigue son tarea tuya.

Este tutorial recorre todo el procedimiento, sea cual sea la forma en que desplegaste BTCPay Server: comprobar la versión en ejecución, aplicar la actualización según tu tipo de despliegue, verificar que realmente se instaló, y rotar los secretos que un atacante pueda haber capturado mientras tu instancia era vulnerable.

Si aún no has desplegado BTCPay Server, empieza por la guía de instalación:

https://planb.academy/tutorials/business/point-of-sale/btcpay-server-928eb01e-824b-4b57-a3e8-8727633beddc

## La vulnerabilidad crítica de agosto de 2026

⚠️ **Alerta de seguridad crítica (7 de agosto de 2026):** una vulnerabilidad crítica que afecta a BTCPay Server está siendo explotada activamente y puede provocar la pérdida de fondos. Actualiza tu instancia a la **versión 2.4.2** de inmediato desde `Admin Dashboard > Server > Maintenance > Update`, y luego comprueba que el pie de página muestra `2.4.2`. Si no puedes actualizar de inmediato, apaga tu BTCPay Server. Una vez actualizado, también debes renovar por completo tus macaroons y tu `macaroons.db`, renovar por completo las cadenas de autenticación de cualquier otro backend Lightning, y, si generaste una billetera on-chain caliente dentro de BTCPay Server, mover esos fondos y recrear la billetera. Los integradores también deberían actualizar NBXplorer a la versión 2.6.10. Fuente: [notas de la versión 2.4.2 de BTCPay Server](https://github.com/btcpayserver/btcpayserver/releases/tag/v2.4.2).

La versión 2.4.2 se publicó el 7 de agosto de 2026. Las notas de la versión indican que corrige una vulnerabilidad crítica que ya estaba siendo explotada activamente, reportada por `brunoerg` y `benthecarman` a través del esfuerzo Bitcoin Red Team. La misma versión también corrige un bypass de la autenticación de dos factores TOTP a través de la autenticación Basic de Greenfield, y desactiva la autenticación Basic de Greenfield por defecto cinco minutos después de la creación de la cuenta.

De "explotada activamente" se derivan dos consecuencias:

- **Actualizar no es opcional ni algo que se pueda programar para la semana que viene.** Una instancia sin parchear y accesible desde internet debe ser actualizada o apagada.
- **Actualizar no basta por sí solo.** Si tu instancia fue comprometida antes de que la parchearas, el atacante puede tener ya copias de tus credenciales Lightning y de cualquier material de clave de billetera caliente que BTCPay Server generó para ti. Esos secretos siguen siendo válidos después de la actualización hasta que los rotes. La sección de rotación más abajo es la parte que la gente se salta, y es la parte que realmente protege tus fondos.

## Paso 1 — Averigua qué versión estás ejecutando

Inicia sesión en tu BTCPay Server y mira el **pie de página de cualquier página**: ahí se muestra la cadena de versión. También puedes abrir `Admin Dashboard > Server > Maintenance`, que muestra la versión actual y los controles de actualización.

Si tu instancia expone la API de Greenfield, `GET /api/v1/server/info` también devuelve la versión.

Cualquier versión inferior a `2.4.2` es vulnerable.

## Paso 2 — Actualiza

### Despliegue Docker autoalojado (la instalación estándar)

Esto cubre el despliegue oficial de Docker, que es lo que obtienes de la documentación de BTCPay Server, del lanzador de un clic de LunaNode, y de la mayoría de instalaciones en VPS.

La vía más simple es la interfaz web:

1. Ve a `Admin Dashboard > Server > Maintenance`.
2. Haz clic en **Update**.
3. Espera a que se descarguen y reinicien los contenedores. La interfaz quedará inaccesible durante unos minutos.

Si la interfaz web no está accesible, o prefieres ver los logs, hazlo por SSH:

```bash
sudo su -
cd "$BTCPAY_BASE_DIRECTORY/btcpayserver-docker"
. ./btcpay-update.sh
```

En una instalación por defecto, `$BTCPAY_BASE_DIRECTORY` es `/root`, así que el directorio es `/root/btcpayserver-docker`. El script descarga las últimas imágenes, recrea los contenedores y muestra las versiones resultantes.

El despliegue Docker incluye NBXplorer junto a BTCPay Server, así que una actualización estándar también lleva NBXplorer a la versión recomendada `2.6.10`. Si ejecutas NBXplorer por separado —algo habitual en integradores y stacks personalizados—, actualízalo explícitamente.

### Umbrel

Abre el panel de Umbrel, ve a la **App Store**, busca BTCPay Server y aplica la actualización si se ofrece una.

⚠️ **Importante:** los paquetes de la app store son reempaquetados por el equipo de Umbrel y pueden ir por detrás del proyecto original por horas o días. Comprueba la versión en el pie de página de BTCPay Server después de actualizar. Si sigue por debajo de `2.4.2`, **detén la app** desde el panel de Umbrel y espera a la versión empaquetada en lugar de dejar una instancia vulnerable en ejecución.

La guía dedicada a Umbrel cubre la aplicación en sí:

https://planb.academy/tutorials/business/point-of-sale/btcpay-server-umbrel-68e1c535-4322-4507-a69c-9dfcbc36dfd1

### Start9 / StartOS

La misma lógica: actualiza BTCPay Server desde el marketplace de StartOS, y luego verifica la versión en el pie de página. Si la versión empaquetada aún no es `2.4.2`, detén el servicio hasta que lo sea.

### Alojamiento gestionado y de terceros

Si otra persona opera tu instancia (un proveedor de hosting, una asociación, el servidor de un amigo), igualmente necesitas la confirmación. Pide al operador la cadena de versión mostrada en el pie de página, y pregunta explícitamente si se ha realizado la rotación de credenciales posterior a la actualización descrita más abajo. "Actualizamos" no es la misma respuesta que "rotamos tus macaroons".

## Paso 3 — Verifica que la actualización realmente se instaló

Recarga la interfaz de BTCPay Server y lee la versión en el pie de página. Debe mostrar `2.4.2` o superior.

No confíes en que el comando de actualización termine sin errores: en máquinas con recursos limitados, una descarga de imagen puede fallar en silencio y dejar el contenedor anterior en ejecución. Lee la versión, siempre.

## Paso 4 — Rota tus credenciales

Este es el paso que convierte "parcheado" en "seguro". Dado que la vulnerabilidad estaba siendo explotada antes de que se publicara la corrección, trata cada secreto que tu instancia guardaba como potencialmente conocido por un atacante.

### Lightning: LND

Regenera los macaroons **y** el archivo `macaroons.db`. Eliminar solo los archivos de macaroon no es suficiente — LND deriva los macaroons a partir de la clave raíz almacenada en `macaroons.db`, así que un atacante con una copia de un macaroon antiguo conserva el acceso hasta que esa base de datos se recree.

El procedimiento es: detener LND, eliminar `macaroons.db` y los archivos `*.macaroon` del directorio de la red (para mainnet, `data/chain/bitcoin/mainnet/` dentro del directorio de datos de LND), y luego reiniciar y desbloquear LND, lo que los recrea. Haz primero una copia de seguridad del directorio, y vuelve a emparejar cada aplicación que usara los macaroons antiguos — el propio BTCPay Server, Zeus, Thunderhub, RTL, Alby, y cualquier script que hayas escrito.

Si además expones LND a internet, revisa a la vez su certificado TLS y las credenciales de `lnd.conf`.

### Lightning: otros backends

Todo lo que se autentique ante tu nodo con una cadena debe recibir una cadena nueva:

- **Core Lightning**: regenera la rune o las credenciales de acceso usadas por la conexión.
- **Phoenixd**: rota la contraseña HTTP.
- **LNbits y similares**: revoca y reemite las claves de admin y de factura.
- **Cadenas de conexión a nodos remotos** almacenadas en la configuración de la tienda de BTCPay Server: reescríbelas con los nuevos secretos.

### Billetera on-chain caliente generada dentro de BTCPay Server

Si dejaste que BTCPay Server generara una billetera on-chain por ti —a diferencia de conectar una hardware wallet o importar un xpub cuyas claves nunca tocaron el servidor—, esa semilla vivió en la máquina.

Considérala quemada:

1. Crea una billetera nueva, idealmente con una hardware wallet para que las claves nunca vuelvan a estar en el servidor.
2. Barre los fondos de la billetera antigua a la nueva.
3. Sustituye el esquema de derivación en la configuración de la tienda por el de la nueva billetera.
4. Nunca reutilices la semilla antigua.

Las configuraciones de solo lectura (xpub o hardware wallet) no necesitan esto: las claves privadas nunca estuvieron en el servidor. Precisamente por eso la guía de instalación las recomienda.

### Cuentas de BTCPay Server y claves de API

Ya que estás en ello:

- Cambia las contraseñas de todas las cuentas de usuario de la instancia.
- Revoca y reemite todas las **claves de API** de Greenfield.
- Vuelve a inscribir la autenticación de dos factores, dado que la 2.4.2 corrige un bypass del 2FA.
- Abre `Admin Dashboard > Server > Users` y comprueba que no exista ninguna cuenta inesperada.
- Revisa los **payouts**, **pull payments** y **reembolsos** recientes en busca de entradas que no creaste tú.
- Revisa tus webhooks y sus secretos.

## Paso 5 — Mantente informado para la próxima vez

Las versiones de seguridad solo ayudan a los operadores que se enteran de ellas:

- Sigue las [versiones de BTCPay Server en GitHub](https://github.com/btcpayserver/btcpayserver/releases) — GitHub puede enviarte un correo con cada nueva versión de un repositorio.
- Sigue los canales de anuncios del proyecto y el [blog oficial](https://blog.btcpayserver.org/).
- Mantén tu instancia en una versión que puedas actualizar rápidamente: cuanto más atrás te quedes, más dolorosa se vuelve una actualización de emergencia.

Autoalojarte te da soberanía sobre tus pagos. El coste de esa soberanía es exactamente este: leer las notas de versión y ser quien parchea.
</content>
<parameter name="i">Write Spanish translation of tutorial