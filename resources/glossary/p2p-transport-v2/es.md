---
term: P2P TRANSPORT V2
---

Nueva versión del protocolo de transporte P2P de Bitcoin que incorpora cifrado oportunista para mejorar la privacidad y seguridad de las comunicaciones entre nodos. Esta mejora busca abordar varios problemas con la versión básica del protocolo P2P, notablemente haciendo que los datos intercambiados sean indistinguibles para un observador pasivo (como un proveedor de servicios de internet), reduciendo así los riesgos de censura y ataques a través de la detección de patrones específicos en los paquetes de datos.

El cifrado implementado no incluye autenticación para evitar añadir complejidad innecesaria y para no comprometer la naturaleza sin permisos de la conexión de red. Este nuevo protocolo de transporte P2P ofrece, no obstante, mejor seguridad contra ataques pasivos y hace que los ataques activos sean significativamente más costosos y detectables (notablemente los ataques MITM). La introducción de un flujo de datos pseudoaleatorio complica la tarea para los atacantes que deseen censurar o manipular las comunicaciones.

El P2P Transport V2 fue incluido como una opción (deshabilitada por defecto) en la versión 26.0 de Bitcoin Core, desplegada en diciembre de 2023. Se puede activar con la opción `v2transport=1` en el archivo de configuración.