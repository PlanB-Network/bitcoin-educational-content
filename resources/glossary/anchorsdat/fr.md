---
term: Anchors.dat
definition: Fichier Bitcoin Core stockant les adresses IP des nœuds auxquels le client était connecté avant son arrêt, pour faciliter la reconnexion au redémarrage.
---

Fichier utilisé dans le client Bitcoin Core pour stocker les adresses IP des nœuds sortants auxquels un client était connecté avant d'être éteint. Anchors.dat est donc créé à chaque fois que le nœud est arrêté et supprimé lorsqu'il est relancé. Les nœuds dont les adresses IP sont contenues dans ce fichier sont utilisés pour aider à établir rapidement des connexions lors du redémarrage du nœud.
