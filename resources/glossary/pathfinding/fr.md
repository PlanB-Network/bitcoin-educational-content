---
term: PATHFINDING
---

Processus utilisé par un nœud pour déterminer le chemin optimal afin de router un paiement à travers le réseau de canaux Lightning. Le pathfinding est réalisé par le nœud du payeur, qui doit sélectionner les nœuds intermédiaires les plus adaptés pour atteindre le destinataire. Ce choix est basé sur plusieurs critères tels que les frais, la capacité des canaux et les timelocks.
Les algorithmes de pathfinding construisent un graphe de la topologie du réseau à partir des données de gossip et évaluent les différentes routes possibles entre le nœud payeur et le receveur. Ces routes sont classées de la meilleure à la moins bonne selon divers critères. Le nœud teste ensuite ces routes jusqu'à réussir à effectuer le paiement sur l'une d'entre elles.
