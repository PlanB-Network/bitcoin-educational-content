---
term: DNS SEEDS
---

Các điểm kết nối ban đầu cho các nút Bitcoin mới tham gia vào mạng. Những seed này, thực chất là các máy chủ DNS cụ thể, có địa chỉ được nhúng vĩnh viễn trong mã nguồn Bitcoin Core. Khi một nút mới bắt đầu, nó liên hệ với các máy chủ này để nhận một danh sách ngẫu nhiên các địa chỉ IP của các nút Bitcoin được cho là đang hoạt động. Nút mới sau đó có thể thiết lập kết nối với các nút trong danh sách này để thu thập thông tin cần thiết để thực hiện Tải Khối Ban Đầu (IBD) và đồng bộ hóa với chuỗi có công việc tích lũy nhiều nhất. Tính đến năm 2024, đây là danh sách các DNS seeds của Bitcoin Core và cá nhân chịu trách nhiệm bảo trì chúng (https://github.com/bitcoin/bitcoin/blob/master/src/kernel/chainparams.cpp):
* seed.bitcoin.sipa.be: Pieter Wuille;
* dnsseed.bluematt.me: Matt Corallo;
* dnsseed.bitcoin.dashjr-list-of-p2p-nodes.us: Luke Dashjr;
* seed.bitcoinstats.com: Christian Decker;
* seed.bitcoin.jonasschnelli.ch: Jonas Schnelli;
* seed.btc.petertodd.net: Peter Todd;
* seed.bitcoin.sprovoost.nl: Sjors Provoost;
* dnsseed.emzy.de: Stephan Oeste;
* seed.bitcoin.wiz.biz: Jason Maurice;
* seed.mainnet.achownodes.xyz: Ava Chow.

DNS seeds là phương pháp thứ hai, theo thứ tự ưu tiên, để một nút Bitcoin thiết lập kết nối. Phương pháp đầu tiên liên quan đến việc sử dụng tệp peers.dat mà chính nút đã tạo ra. Tệp này tự nhiên sẽ trống trong trường hợp của một nút mới, trừ khi người dùng đã tự chỉnh sửa nó.

> ► *Lưu ý, DNS seeds không nên bị nhầm lẫn với "seed nodes," là cách thứ ba để thiết lập kết nối.*