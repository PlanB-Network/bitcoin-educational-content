---
term: MINISCRIPT
---

Marco de trabajo diseñado para proporcionar un marco para programar scripts de manera segura en Bitcoin. El lenguaje nativo de Bitcoin se llama script. Es bastante complejo de usar en la práctica, especialmente para aplicaciones sofisticadas y personalizadas. Sobre todo, es muy difícil verificar las limitaciones de un script. Miniscript utiliza un subconjunto de scripts de Bitcoin para simplificar su creación, análisis y verificación. Cada miniscript es equivalente 1 a 1 con un script nativo. Se utiliza un lenguaje de políticas amigable para el usuario, que luego se compila en miniscript, para finalmente corresponder a un script nativo.

![](../../dictionnaire/assets/30.png)

Miniscript permite así a los desarrolladores construir scripts sofisticados de una manera más segura y confiable. Las propiedades esenciales de Miniscript son las siguientes:
* Permite el análisis estático del script, incluyendo las condiciones de gasto que permite y su costo en términos de recursos;
* Facilita la creación de scripts que se adhieren al consenso;
* Permite el análisis de si los diferentes caminos de gasto cumplen o no con las reglas estándar de los nodos;
* Establece un estándar general, comprensible y componible, para todo el software y hardware de billeteras.

El proyecto Miniscript fue lanzado en 2018 por Peter Wuille, Andrew Poelstra y Sanket Kanjalkar, a través de la empresa Blockstream. Miniscript se añadió a la billetera de Bitcoin Core en modo solo visualización en diciembre de 2022 con la versión 24.0, y luego completamente en mayo de 2023 con la versión 25.0.