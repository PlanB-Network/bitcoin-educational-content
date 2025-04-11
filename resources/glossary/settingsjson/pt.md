---
term: SETTINGS.JSON

---
Ficheiro utilizado no Bitcoin Core para armazenar as definições da interface gráfica do utilizador (GUI). Ele retém informações sobre as configurações do usuário, como carteiras abertas, por exemplo. Quando o Bitcoin Core é reiniciado, este ficheiro permite a reabertura automática de carteiras que estavam activas antes da aplicação ser fechada. Se uma carteira for fechada através da GUI, ela também é removida deste arquivo e, portanto, não será reaberta automaticamente na próxima inicialização.