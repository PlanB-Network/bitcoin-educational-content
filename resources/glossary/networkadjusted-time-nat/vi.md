---
term: NETWORK-ADJUSTED TIME (NAT)

---
Estimation of universal time established on the clocks of the network nodes. Each node calculates its NAT by taking the median of the time differences between its local clock (UTC) and those of the nodes it is connected to, then adding its local clock to the median of these differences, up to a maximum of 70 minutes. The network-adjusted time is therefore a median of the node times calculated locally by each node. This reference frame is then used to verify the validity of the block timestamps. Indeed, for a block to be accepted by a node, its timestamp must be between the MTP (median time of the last 11 mined blocks) and the NAT plus 2 hours:

```text
MTP < Valid Timestamp < (NAT + 2h)
```