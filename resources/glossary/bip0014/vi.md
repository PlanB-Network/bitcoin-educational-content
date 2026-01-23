---
term: BIP0014

definition: Tiêu chuẩn xác định định dạng nhận dạng của các máy khách Bitcoin trên mạng lưới, phân biệt phiên bản phần mềm với phiên bản giao thức.
---
BIP proposed by Patrick Strateman and Amir Taaki in 2011 that aims to distinguish between client version numbers and the protocol version. BIP14 specifies how Bitcoin protocol implementations should present themselves on the network. It suggests the use of a user-agent format to identify the version and type of the Bitcoin client used. The main goal of BIP14 is to facilitate the management of changes and the detection of incompatibilities between the different existing clients. While it was previously logical to consider Satoshi's client as de facto the Bitcoin protocol, the proliferation of software at this time led BIP14 to clearly differentiate the clients from the protocol itself.