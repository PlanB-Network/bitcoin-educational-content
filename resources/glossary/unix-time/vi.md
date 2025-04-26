---
term: UNIX TIME

---
Unix Time or Unix Timestamp represents the number of seconds that have elapsed since January 1, 1970, at midnight UTC (Unix Epoch). This system is used in Unix operating systems and derivatives to mark time in a universal and standardized manner. It enables the synchronization of clocks and the management of time-based events, regardless of time zones.

In the context of Bitcoin, it is used for the local clock of nodes, and thus for the calculation of NAT (Network-Adjusted Time). The network-adjusted time is a median of the node times calculated locally by each node, and this reference is then used to verify the validity of block timestamps. Indeed, for a block to be accepted by a node, its timestamp must be between the MTP (Median Time Past of the last 11 mined blocks) and the NAT plus 2 hours:

```text
MTP < Valid Timestamp < (NAT + 2h)
```

Unix Time is also used to establish timelocks when they are based on real time, rather than on a number of blocks.