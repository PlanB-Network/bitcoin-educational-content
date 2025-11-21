---
term: State Transition
---

在 RGB 协议中，State Transition 是用于将 Contract 状态更改为新配置的操作。它可以修改 Global State 和所有状态数据。每次转换都要根据 Contract 的 Schema 中定义的规则进行严格检查，以确保修改符合 Genesis 中规定的约束条件。该操作通过 Commitment 锚定在 Blockchain Bitcoin 中。