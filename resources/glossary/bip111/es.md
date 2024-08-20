---
term: BIP111
---

Propone la adición de un bit de servicio llamado `NODE_BLOOM` para permitir que los nodos señalen explícitamente su apoyo a los Filtros Bloom como se describe en BIP37. La introducción de `NODE_BLOOM` permite a los operadores de nodos deshabilitar este servicio para reducir los riesgos de DoS. La opción BIP37 está deshabilitada por defecto en Bitcoin Core. Para habilitarla, el parámetro `peerbloomfilters=1` debe ser ingresado en el archivo de configuración.