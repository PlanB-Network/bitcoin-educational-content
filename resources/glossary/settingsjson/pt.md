---
term: SETTINGS.JSON
---

Arquivo usado no Bitcoin Core para armazenar as configurações da interface gráfica do usuário (GUI). Ele retém informações sobre configurações do usuário, como carteiras abertas, por exemplo. Quando o Bitcoin Core é reiniciado, este arquivo possibilita a reabertura automática das carteiras que estavam ativas antes do fechamento do aplicativo. Se uma carteira é fechada através da GUI, ela também é removida deste arquivo e, portanto, não será reaberta automaticamente na próxima inicialização.