---
term: MINISCRIPT

---
Framework diseñado para proporcionar un marco para programar scripts de forma segura en Bitcoin. El lenguaje nativo de Bitcoin se llama script. Es bastante complejo de usar en la práctica, especialmente para aplicaciones sofisticadas y personalizadas. Sobre todo, es muy difícil verificar las limitaciones de un script. Miniscript utiliza un subconjunto de scripts de Bitcoin para simplificar su creación, análisis y verificación. Cada miniscript es equivalente 1 por 1 con un script nativo. Se utiliza un lenguaje de políticas fácil de usar, que luego se compila en miniscript, para que finalmente se corresponda con un script nativo.

![](../../dictionnaire/assets/30.webp)

De este modo, Miniscript permite a los desarrolladores crear scripts sofisticados de forma más segura y fiable. Las propiedades esenciales de Miniscript son las siguientes:


- Permite realizar un análisis estático del guión, incluidas las condiciones de gasto que permite y su coste en términos de recursos;
- Permite crear guiones que se adhieren al consenso;
- Permite analizar si las distintas vías de gasto cumplen o no las normas estándar de los nodos;
- Establece una norma general, comprensible y componible, para todo el software y hardware de las carteras.

El proyecto Miniscript fue lanzado en 2018 por Peter Wuille, Andrew Poelstra y Sanket Kanjalkar, a través de la empresa Blockstream. Miniscript se añadió al monedero Bitcoin Core en modo watch-only en diciembre de 2022 con la versión 24.0, y después completamente en mayo de 2023 con la versión 25.0.