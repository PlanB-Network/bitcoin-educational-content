---
name: Firefox
description: ¿Cómo configurar Firefox para proteger tu privacidad?
---

![cover](assets/cover.webp)



## Introducción



Todos pasamos horas en Internet, a menudo sin darnos cuenta de lo que nuestro navegador revela sobre nosotros. Cada clic, cada búsqueda, cada sitio que visitamos alimenta una industria masiva de recopilación de datos personales.



![Statistiques navigateurs 2024](assets/fr/01.webp)


*Cuota de mercado de los navegadores web: Chrome domina con un 65% del mercado, seguido de Safari y Edge. Fuente: [gs.statcounter.com](https://gs.statcounter.com/browser-market-share)*



Como muestra este gráfico, Google Chrome domina masivamente, con más del 65% del uso mundial. Esta hegemonía significa que la mayoría de los internautas confían sus datos de navegación a Google, una empresa cuyo modelo de negocio se basa en la publicidad dirigida. Firefox, con apenas un 3% del mercado, representa una alternativa desarrollada por Mozilla, una organización sin ánimo de lucro que no tiene ningún interés comercial en explotar tus datos.



Pero elegir Firefox es sólo el primer paso. Por defecto, incluso Firefox requiere ajustes para maximizar tu protección. Esta guía te lleva paso a paso, desde lo más sencillo a lo más avanzado, para transformar Firefox en un auténtico escudo contra el rastreo, preservando al mismo tiempo una experiencia de navegación agradable.



### ¿Por qué Firefox?





- Libre y de código abierto** (motor Gecko): código auditable y transparente
- Organización sin ánimo de lucro**: Fundación Mozilla, misión de interés general
- Protecciones nativas integradas**: Protección de rastreo mejorada (ETP), Protección total de cookies (TCP), Partición de estados, Modo sólo HTTPS, DNS sobre HTTPS (DoH)
- Personalización avanzada**: a diferencia de Chrome, Firefox te permite modificar su comportamiento en profundidad



### Principios importantes antes de empezar





- No hay receta universal**: cuanto más se modifica, más se corre el riesgo de destacar (fingerprinting). El objetivo es estar mejor protegido sin destacar entre la multitud.
- Progresa paso a paso**: Cambia una configuración, prueba tus sitios habituales y continúa. No es necesario cambiarlo todo a la vez.
- Equilibrio personal**: Encuentra TU compromiso entre privacidad y facilidad de uso.



## Instalación rápida



![Téléchargement Firefox](assets/fr/02.webp)



**Descarga oficial:** Vaya a [firefox.com/browsers/desktop](https://www.firefox.com/en-US/browsers/desktop/). En esta página, seleccione su sistema operativo (Windows, macOS, Linux) para acceder a la página de descarga adecuada con instrucciones de instalación específicas.





- Windows**: descargue el instalador `.exe`, haga doble clic y siga las instrucciones del asistente de instalación
- macOS**: descarga el archivo `.dmg`, ábrelo y arrastra Firefox a la carpeta Aplicaciones
- Linux**: varias opciones disponibles - paquete `.deb`/`.rpm`, Flatpak (Flathub), Snap, o mediante gestor de paquetes (apt, dnf, pacman). Prefiera las fuentes oficiales de Mozilla.



**Consejo:** Una vez instalado, busca actualizaciones a través de Ayuda → **Sobre Firefox** (importante para los parches de seguridad).



![Configuration initiale Firefox](assets/fr/03.webp)


*Primera pantalla al iniciar Firefox: establece Firefox como navegador predeterminado, añádelo a tus accesos directos y haz clic en "Guardar y continuar "*



![Création compte Firefox](assets/fr/04.webp)


*Paso opcional: crea o inicia sesión en una cuenta de Firefox. Puedes omitir este paso haciendo clic en "Ahora no" en la parte inferior derecha*



![Page d'accueil Firefox](assets/fr/05.webp)


*Pantalla de inicio de Firefox una vez finalizada la configuración. Observa el menú ☰ en la parte superior derecha, que da acceso a Configuración y Extensiones para personalizar Firefox*



## Protecciones ya activadas por defecto (tranquilizador)





- Aislamiento de sitios (Fisión)**: en despliegue progresivo. Esta función ejecuta cada sitio en un proceso separado para evitar que una pestaña maliciosa acceda a los datos de otra. Compruebe su estado a través de `about:support` (busque "Fission"). Si no está activada, puedes activarla manualmente en `about:config` con `fission.autostart = true`.
- Protección total de cookies (TCP)**: activa por defecto. Las cookies y otros tipos de almacenamiento se limitan al sitio de la primera parte (un "tarro" por sitio), lo que neutraliza el seguimiento entre sitios. Se hacen excepciones temporales a través de la API de acceso al almacenamiento cuando es necesario (botones de inicio de sesión integrados).
- Protección de rastreo de rebote/redirección**: Firefox detecta y limpia automáticamente las cookies que dejan los sitios de rebote (enlaces que te redirigen a través de un rastreador antes del destino), reduciendo este canal de rastreo sin ninguna acción por tu parte.



## Nivel 1 - Esencial (≤ 10 minutos)



Objetivo: grandes ganancias en privacidad sin romper la web. Para el 90% de los usuarios.



Para acceder a los ajustes, pulsa en el menú ☰ de la parte superior derecha y, a continuación, en **"Ajustes "**:



![Paramètres généraux](assets/fr/07.webp)


*Página de configuración de Firefox - pestaña "General". Aquí es donde configuras la mayoría de tus opciones de privacidad*



**Protección de seguimiento (ETP)**




- Cambia **ETP** a **Strict**. Bloqueas más rastreadores (cookies cross-site, fingerprinting, cryptomining, widgets sociales...).
- Si un sitio se rompe (vídeo, botón de inicio de sesión...), desactive la protección sólo para ese sitio a través del escudo 🛡️ y, a continuación, actualice la pestaña.



Estos son los diferentes niveles de seguridad de ETP:




- Estándar** (equilibrado, máxima compatibilidad)
  - Bloquea: rastreadores sociales, cookies de sitios cruzados (todas las ventanas), rastreo de contenido en navegación privada, mineros de criptomonedas, detectores de huellas dactilares.
  - Incluye **Protección Total de Cookies** (TCP): un tarro por sitio.
- Estricto** (recomendado para la confidencialidad)
  - También bloquea el contenido de rastreo en todas las ventanas + huellas dactilares conocidas y sospechosas.
  - Puede romper algunos sitios; utilice el escudo 🛡️ para una excepción local.
- Personalizado** (avanzado)
  - Ajuste fino: cookies, rastreo de contenidos, menores, huellas dactilares (conocidas/sospechosas).



![Paramètres protection contre le pistage](assets/fr/06.webp)



**Cookies y datos del sitio




- Habilite **"Eliminar cookies y datos del sitio al cerrar "** para reiniciar limpiamente cada vez que reinicie.
- Añada **Excepciones** para 2-3 sitios esenciales si lo desea (correo electrónico, banco).


**Introducción automática de datos, sugerencias y página de inicio**




- Desactiva el **autocompletado** (DNI, direcciones, tarjetas). Utiliza un gestor de contraseñas.
- Búsqueda**: desactivar **"Mostrar sugerencias de búsqueda "**.
- Barra Address**: cortar **"Sugerencias patrocinadas "** y **"Sugerencias contextuales "**.
- Inicio**: desactivar **Bolsillo** y **contenido patrocinado**.



![Paramètres cookies et mots de passe](assets/fr/08.webp)



**SóloHTTPS**




- Activar **"Modo HTTPS sólo en todas las ventanas "**.


![Configuration DNS over HTTPS](assets/fr/09.webp)



**Medición de la telemetría y la publicidad




- En "Recogida de datos por Firefox", **desmarcar todo**.
- Desactivar **"Medidas de publicidad respetuosas con la intimidad "** (PPA).
- Navegación segura**: mantenla activada (recomendado). Firefox comprueba los sitios con listas de amenazas mediante consultas hash y comprobaciones locales, protegiendo contra el phishing y el malware con un impacto mínimo en la privacidad.



**Control Global de Privacidad (opcional)**




- Active el **GPC** para señalar su negativa a vender/compartir datos.



**Motor de búsqueda




- Cambia a **DuckDuckGo**, **Startpage**, **Qwant** o **Brave Search** (Ajustes → Buscar).



![Configuration moteur de recherche DuckDuckGo](assets/fr/11.webp)



**Navegación privada**




- Ventanas privadas (Ctrl/Cmd+Mayús+P) para sesiones puntuales (regalos, cuentas secundarias...). Evita el modo "siempre privado": las extensiones pueden estar inactivas y las excepciones de cookies son menos útiles.



**Extensiones esenciales** (instalar desde el catálogo oficial)




- uBlock Origin**: bloquea los anuncios y el rastreo actual, ligero.
- Privacy Badger**: aprende a bloquear lo que te sigue; envía Do Not Track / GPC.
- ClearURLs** (opcional): Firefox (ETP Strict) y uBO ya limpian mucho; mantenlo si aún ves URLs "sucias" (utm, fbclid).
- Contenedores multicuenta de Firefox**: **aísla cookies/sesiones y almacenamiento por contenedor; multicuentas paralelas; menos rastreo entre sitios**. Extensión oficial: `https://addons.mozilla.org/fr/firefox/addon/multi-account-containers/`.



![Extension Multi-Account Containers](assets/fr/12.webp)



**Contraseñas y 2FA




- Utiliza un gestor de contraseñas dedicado** (Bitwarden, KeePassXC). **Evita** almacenar contraseñas en el navegador. **Activar 2FA** siempre que sea posible.



## Nivel 2 - Reforzado (compartimentación y red)



Objetivo: compartimentar las actividades y reducir las fugas de la red.



**DNS sobre HTTPS (DoH)**




- Estado por defecto**: Activado automáticamente en algunas regiones (EE.UU., Canadá, Rusia, Ucrania). En el resto, se requiere activación manual.
- Configuración**: Configuración → General → Configuración de red → **Habilitar DoH** → **Cloudflare** o **Quad9** → **Protección máxima**.
- Máxima protección = TRR-only** (no fallback to system DNS). Si una red corporativa/hotelera bloquea, vuelva a **Estándar** o desactive DoH.
- Redundancia**: Si ya estás utilizando una VPN de confianza con su propio DNS seguro, DoH puede ser redundante.
- Prueba de verificación**: `https://www.dnsleaktest.com/` debe mostrar sólo el proveedor de DoH elegido.



![Sélection fournisseur DNS Cloudflare](assets/fr/10.webp)



**Compartimentación con contenedores y perfiles




- Contenedores Multicuenta**: cree espacios (Personal, Trabajo, Finanzas, Redes Sociales, Compras, Desechable). Configure **"Abrir siempre en este contenedor "** para sus sitios recurrentes. Extensión oficial: `https://addons.mozilla.org/fr/firefox/addon/multi-account-containers/`.
- ¿Por qué utilizarlos?
  - Fuerte aislamiento** de cookies/sesiones/almacenamiento por espacio.
  - Menos cross-site tracking**: confinar a los gigantes (Facebook, Google).
  - Multicuentas simultáneas** en el mismo servicio.
  - Menor riesgo de CSRF/XSS** entre identidades segmentadas.
  - Consejo: como mínimo, contenedores dedicados para Redes Sociales/Google, Trabajo, Finanzas.
- Facebook Container** (opcional): una versión simplificada dedicada a FB/Instagram.
- Perfiles separados**: mediante `about:profiles` (perfil principal, perfil mínimo "ultraseguro", perfil de prueba). Compartimentación total de datos y extensiones.



**Extensiones avanzadas** (pendiente de reserva)




- Cookie AutoDelete**: borra las cookies de un sitio en cuanto se cierra la pestaña (útil si Firefox está abierto mucho tiempo).
- LocalCDN**: sirve las bibliotecas actuales localmente (reduce las llamadas a Google/Microsoft). Compatibilidad parcial.



**Móvil (Android)**




- Firefox Android + uBlock Origin**: protección similar en movimiento.



## Nivel 3 - Experto (about:config & Arkenfox)



Objetivo: endurecimiento avanzado con compromisos aceptados. Recomendado en un **perfil independiente**.



Elija sólo uno de los dos enfoques siguientes:



**Enfoque A - Modificaciones manuales**: Algunos ajustes específicos a través de `about:config` (control más sencillo y preciso)


**Enfoque B - Arkenfox user.js**: Configuración automatizada completa (más compleja, máxima protección)



➡️ **Arkenfox ya incluye TODOS los cambios about:config mencionados a continuación** + cientos más. Si eliges Arkenfox, ignora la sección about:config.



### Método A: Modificaciones manuales a través de about:config



Escriba `about:config` en la barra Address → Aceptar riesgo.



![Avertissement about:config](assets/fr/13.webp)



![Interface about:config](assets/fr/14.webp)



![Préférences about:config](assets/fr/15.webp)





- Resistencia a las huellas dactilares (heredada del Navegador Tor)


```text
privacy.resistFingerprinting = true
```


Efectos: Zona horaria UTC, **boxing de letras** (tamaños de ventana estándar), User-Agent/políticas estandarizadas, restricciones Canvas/WebGL/AudioContext. Más uniformidad, pero algunas "peculiaridades" (desfase horario, a veces un poco de inglés).





- Desactivar WebRTC (evita fugas de IP; rompe Web visio)


```text
media.peerconnection.enabled = false
```





- Referer más compatible (por defecto)


```text
network.http.referer.XOriginPolicy = 1
network.http.referer.trimOnCrossOrigin = true
```


Opción estricta (puede romper pagos/SSO):


```text
network.http.referer.XOriginPolicy = 2
```





- Limitar las API parlanchinas y la especulación


```text
dom.battery.enabled = false
device.sensors.enabled = false
beacon.enabled = false
geo.enabled = false
media.navigator.enabled = false
network.prefetch-next = false
browser.urlbar.speculativeConnect.enabled = false
network.http.speculative-parallel-limit = 0
```



Regla de oro: si algo se rompe, vuelve al último cambio.



### Enfoque B: Arkenfox user.js (Configuración totalmente automatizada)



El proyecto **Arkenfox** proporciona un archivo `user.js` mantenido por la comunidad que aplica automáticamente cientos de preferencias de Firefox orientadas a la privacidad y la seguridad. Al reiniciar, Firefox lee este archivo de tu perfil y aplica estos ajustes.





- ¿Cuál es el objetivo? Partir de una **base consistente endurecida** sin "hacer clic en todas partes"; reducir los descuidos; ahorrar tiempo.
- Lo que cambia (ejemplos): corte de telemetría, cookies/cache/referrer/HTTPS reforzados, **RFP** + letterboxing, **WebRTC desactivado**, ajustes DoH/TLS, APIs chatty limitadas.
- Cuándo usarlo: si quieres Firefox reforzado en 10 minutos y aceptar algunas excepciones (DRM/streaming, Web visio, SSO/pagos).
- Ventajas: rápido, consistente, **actualizado** (alineado con ESR), muy bien **documentado** (wiki + comentarios), **personalizable** mediante overrides.
- Limitaciones: compatibilidad (algunas aplicaciones web), comodidad (UTC, tamaños de ventana), y un recordatorio: **no es Tor** (no hay anonimato en la red).



Instalación (idealmente en un **perfil dedicado**)


1. Guarda tu perfil/favoritos y haz una lista de tus sitios con excepciones de cookies.


2. Descarga `user.js` de `https://github.com/arkenfox/user.js` (versión ESR/estable).


3. Busca tu carpeta de perfiles a través de `about:profiles`:




   - Windows: `%APPDATA%/Mozilla/Firefox/Profiles/...`
   - Linux: `~/.mozilla/firefox/...`
   - macOS: `~/Library/Application Support/Firefox/Profiles/...`


4. Cierra Firefox y mueve `user.js` a la raíz de la carpeta del perfil.


5. Relanzar; personalizar a través de `about:config` o un archivo de anulaciones.



Actualizaciones




- Sigue las versiones de Arkenfox (alineadas con ESR), reemplaza el `user.js`, relanza Firefox; lee las notas de la versión.



**Personalización mediante anulaciones**



Arkenfox es deliberadamente restrictivo por defecto. Para adaptar ciertos ajustes a sus necesidades (streaming, visio, sitios específicos), puede crear un archivo `user-overrides.js` en la misma carpeta que `user.js`. Este archivo te permite "anular" ciertas preferencias de Arkenfox sin modificar el archivo principal.



Crea `user-overrides.js` y añade tus personalizaciones:


```javascript
// DRM/streaming
user_pref("media.eme.enabled", true);

// Safe Browsing (si vous préférez le garder)
user_pref("browser.safebrowsing.phishing.enabled", true);
user_pref("browser.safebrowsing.malware.enabled", true);

// Historique moins restrictif
user_pref("places.history.expiration.max_pages", 200000);

// Synchronisation Firefox
user_pref("identity.fxaccounts.enabled", true);

// WebRTC (si visio nécessaire)
user_pref("media.peerconnection.enabled", true);

// Referer plus compatible
user_pref("network.http.referer.XOriginPolicy", 1);
user_pref("network.http.referer.trimOnCrossOrigin", true);
```



Buenas prácticas




- Utiliza un perfil separado **"Arkenfox "** y mantén un perfil "normal" para mayor comodidad.
- Minimizar las extensiones (uBlock Origin OK) para limitar la superficie de ataque y la unicidad.
- Añadir excepciones sitio por sitio (blindar 🛡️, uBO, NoScript si se utiliza) cuando sea necesario.
- Prueba después de cada cambio: Fugas WebRTC/DNS, Cubre tus huellas, CreepJS.



## Buenas prácticas





- Actualizaciones**: Firefox y extensiones al día.
- Prórrogas**: razonables y fiables; cuidado con los canjes "dudosos".
- Descargas**: precaución; compruebe los archivos sensibles en VirusTotal.
- Contraseñas**: **gestor dedicado** (Bitwarden, KeePassXC); **2FA** activado; evitar almacenar en navegador.
- Higiene**: confinar Google/Facebook a contenedores; cerrar/abrir regularmente para "resetear" el contexto.



## Límites y alternativas





- Un navegador reforzado ≠ anonimato en la red: sin **VPN**, tu IP sigue siendo visible; incluso con ella, la correlación sigue siendo posible.
- Modificar demasiado puede hacerte **único**. **RFP** estandariza; las herramientas de aleatorización (por ejemplo, Chameleon) pueden... diferenciarte. Probar, comparar, ajustar.
- Alternativas/complementos:
 - Tor Browser: anonimato en la red a través de Tor; más lento. Consulte nuestra guía completa de instalación y configuración**:



https://planb.network/tutorials/computer-security/communication/tor-browser-a847e83c-31ef-4439-9eac-742b255129bb



 - Navegador Mullvad: "Tor sin Tor", para combinar con VPN; huella estandarizada. Descubre cómo instalarlo en nuestro tutorial dedicado**:



https://planb.network/tutorials/computer-security/communication/mullvad-browser-a16c13d6-8bf9-4cb5-9aa0-85411a9cda0e



- Combinaciones recomendadas: Firefox (Nivel 2) + VPN para uso diario; Tor/Mullvad para actividades sensibles; perfiles separados para compartimentación.



## Conclusión



Siguiendo esta guía paso a paso, habrás transformado Firefox en un verdadero baluarte contra la vigilancia digital. Desde los ajustes esenciales de nivel 1 hasta las configuraciones avanzadas de Arkenfox, cada cambio refuerza tu privacidad sin comprometer tu experiencia de navegación.



**Tu privacidad está ahora mejor protegida**: rastreadores de anuncios bloqueados, cookies compartimentadas, filtraciones IP Address neutralizadas, telemetría desactivada. Firefox ya no es solo un navegador, sino una herramienta de resistencia digital adaptada a tus necesidades.



**Recuerda: la confidencialidad nunca es un hecho. Pon a prueba tu protección con regularidad, actualiza tus ajustes y no dudes en adaptar tu configuración a medida que cambien tus hábitos. Tu anonimato en Internet depende tanto de tus herramientas como de tus prácticas.



## Recursos



### Plan ₿ Network




- SCU 202 - Mejora de tu seguridad digital personal: Para saber más sobre los conceptos de seguridad digital tratados en este tutorial**



https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1

### Documentación de Mozilla




- [Protección de seguimiento mejorada](https://support.mozilla.org/kb/enhanced-tracking-protection-firefox-desktop): Guía oficial de la protección reforzada contra el rastreo
- [Particionamiento de estados](https://developer.mozilla.org/docs/Mozilla/Firefox/Privacy/State_Partitioning): Documentación técnica sobre la partición de estados
- [MDN Seguridad Web](https://developer.mozilla.org/docs/Web/Security): Referencia completa sobre seguridad web



### Arkenfox




- [Wiki y guía de instalación](https://github.com/arkenfox/user.js/wiki): Documentación completa del proyecto Arkenfox
- [Depósito y lanzamientos](https://github.com/arkenfox/user.js): Descarga del archivo user.js y seguimiento de las actualizaciones



### Guías y comunidades




- [PrivacyGuides - Navegadores de escritorio](https://www.privacyguides.org/en/desktop-browsers/): Recomendaciones y comparaciones de navegadores
- Reddit**: r/firefox, r/privacy para comentarios y apoyo
- Foro de PrivacyGuides**: debates técnicos en profundidad



### Herramientas de prueba




- [Cover Your Tracks (EFF)](https://coveryourtracks.eff.org/): La huella digital y la eficacia contra el rastreo
- [Prueba de fuga de DNS](https://www.dnsleaktest.com/): Prueba de fuga de DNS y eficacia del DoH
- [BrowserLeaks](https://browserleaks.com/): Conjunto completo de pruebas (WebRTC, Canvas, Fuentes, etc.)
- [BadSSL](https://badssl.com/): Pruebas de validación de certificados SSL/TLS
- [CreepJS](https://abrahamjuliot.github.io/creepjs/): Análisis avanzado de más de 50 vectores de huellas dactilares
- [Prueba de DNS de Cloudflare](https://1.1.1.1/help): Comprobación de que Cloudflare DoH funciona correctamente
