---
name: Ô của chúng ta
description: Cấu hình và sử dụng ứng dụng Nostr trên Umbrel
---

![cover](assets/cover.webp)



## Điều kiện tiên quyết: Cài đặt ô



Umbrel là một nền tảng mã nguồn mở cho phép bạn dễ dàng lưu trữ các ứng dụng Bitcoin và các dịch vụ khác trên máy chủ cá nhân của bạn. Đây là giải pháp tất cả trong một giúp đơn giản hóa đáng kể việc tự lưu trữ các nút Bitcoin và các ứng dụng phi tập trung.



Hãy đảm bảo bạn đã cài đặt Umbrel bằng cách làm theo hướng dẫn cài đặt của chúng tôi:



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

## Giới thiệu về Nostr



**Nostr** là một giao thức mạng mở, phi tập trung được thiết kế cho mạng xã hội. Tên của nó có nghĩa là _"Ghi chú và các thứ khác được truyền qua Relays"_. Nó cho phép bất kỳ ai xuất bản tin nhắn (ghi chú), được quản lý dưới dạng sự kiện JSON và truyền bá chúng thông qua các máy chủ chuyển tiếp thay vì một nền tảng tập trung. Mỗi người dùng sở hữu một cặp khóa mật mã (riêng tư/công khai) đóng vai trò là mã định danh: khóa công khai (npub) xác định người dùng và khóa riêng (nsec) cho phép ký tin nhắn. Nhờ kiến trúc phân tán này, **Nostr cung cấp khả năng chống kiểm duyệt** và tính linh hoạt cao: bạn có thể sử dụng nhiều máy khách và kết nối với nhiều rơle tùy thích mà không phụ thuộc vào một máy chủ duy nhất.



Tóm lại, Nostr là một giao thức truyền thông phi tập trung, trong đó **client** (ứng dụng người dùng) gửi và nhận sự kiện qua **relay** (máy chủ). Giao thức này đặc biệt phổ biến với cộng đồng Bitcoin kể từ năm 2023, do các giá trị phi tập trung và chủ quyền dữ liệu của nó.



**Lưu ý:** Để sử dụng Nostr, bạn sẽ cần khóa riêng (do máy khách Nostr tạo hoặc thông qua tiện ích mở rộng chuyên dụng). **Không bao giờ chia sẻ khóa riêng của bạn** vì điều đó sẽ cho phép bất kỳ ai mạo danh bạn. Giữ khóa ở nơi an toàn và sử dụng các công cụ quản lý khóa an toàn (xem Mẹo bên dưới).



## Ứng dụng ô dù cho Nostr



Umbrel cung cấp một hệ sinh thái các ứng dụng tích hợp để tận dụng tối đa Nostr trên nút cá nhân của bạn. Chúng tôi sẽ trình bày chi tiết cách sử dụng các ứng dụng chính liên quan đến Nostr: **Nostr Relay**, **noStrudel**, **Snort** và **Nostr Wallet Connect**. Mỗi ứng dụng đáp ứng một nhu cầu cụ thể: _Nostr Relay_ là **máy chủ chuyển tiếp riêng**, _noStrudel_ và _Snort_ là **máy khách Nostr** (giao diện để đọc/xuất bản ghi chú), trong khi _Nostr Wallet Connect_ là công cụ liên kết **danh mục đầu tư Lightning** của bạn với Nostr.



### Nostr Relay - Relay riêng tư của bạn trên Umbrel



![Page d'installation de Nostr Relay sur l'App Store Umbrel](assets/fr/01.webp)



**Nostr Relay** là ứng dụng chính thức của Umbrel để chạy **Nostr relay** của riêng bạn trên nút của bạn. Mục tiêu chính là có một relay **riêng tư** và đáng tin cậy để **sao lưu mọi hoạt động Nostr** của bạn theo thời gian thực. Nói cách khác, bằng cách sử dụng relay cá nhân này ngoài relay công khai, bạn đảm bảo rằng mọi ghi chú, tin nhắn và phản ứng của bạn đều được sao chép về nhà, an toàn khỏi kiểm duyệt hoặc mất dữ liệu.



**Cài đặt:** Từ Umbrel App Store (danh mục _Social_), cài đặt _Nostr Relay_. Sau khi khởi chạy, ứng dụng sẽ chạy ở chế độ nền (dịch vụ docker).



![Interface de Nostr Relay avec l'URL du relais](assets/fr/02.webp)



Bạn sẽ thấy trang web Interface của nó thông qua Umbrel: nó cung cấp thông tin cơ bản và trên hết là URL của rơle của bạn (phía trên bên phải), mà bạn sẽ cần sao chép để sử dụng sau này. Một nút đồng bộ hóa (biểu tượng quả địa cầu) cũng khả dụng.



**Để tận dụng chương trình tiếp sức ô của bạn:



**Thêm relay vào máy khách Nostr của bạn:** Trong ứng dụng máy khách của bạn (ví dụ: Damus trên iOS, Amethyst trên Android, Snort hoặc noStrudel trên Umbrel, v.v.), hãy thêm URL của relay riêng tư mà bạn đã sao chép trước đó. Theo mặc định, relay Umbrel lắng nghe trên cổng **4848**. Nếu bạn truy cập nó trên mạng cục bộ, điều này sẽ cung cấp một URL như: `ws://umbrel.local:4848` (hoặc sử dụng IP cục bộ của Umbrel).



Nếu bạn đang sử dụng Tailscale (xem bên dưới), bạn thậm chí có thể sử dụng bí danh DNS MagicDNS (thường là `umbrel` hoặc tên tự động tạo) để truy cập từ bất kỳ đâu, luôn ở cổng 4848.



Nếu bạn thích Tor, hãy lấy Umbrel's .onion Address và sử dụng nó với cổng 4848 thông qua trình duyệt hoặc máy khách tương thích với Tor (xem phần Tor)



Sau khi URL đã được thêm vào cấu hình Relay của máy khách Nostr, hãy kết nối với relay này. Bạn sẽ thấy trong máy khách của mình rằng relay Umbrel đã được kết nối (thường được chỉ ra bằng dấu chấm Green hoặc tương tự).



**Đồng bộ hóa lịch sử (tùy chọn)**: Trong trang web Interface của _Nostr Relay_ trên Umbrel, hãy nhấp vào biểu tượng **quả địa cầu** 🌐 (ở đầu trang). Hành động này sẽ buộc rơle Umbrel của bạn kết nối với các rơle khác (được cấu hình trong máy khách của bạn) để **nhập các hoạt động công khai cũ** của bạn. Điều này có nghĩa là các ghi chú trước đây mà bạn đã xuất bản hoặc đọc qua rơle công khai cũng sẽ được tải xuống và lưu trữ trên rơle riêng tư của bạn. Vui lòng đợi quá trình đồng bộ hóa diễn ra.



**Sử dụng Nostr như bình thường:** Từ bây giờ, bất kỳ hoạt động mới nào (ghi chú đã xuất bản, phản ứng, tin nhắn riêng được mã hóa, v.v.) mà bạn thực hiện trên Nostr sẽ được chuyển tiếp như bình thường đến các rơle công khai **và song song với rơle Umbrel của bạn**. Nếu máy khách Nostr của bạn được cấu hình đúng, nó sẽ gửi từng sự kiện đến tất cả các rơle (bao gồm cả rơle của bạn). Rơle riêng của bạn sẽ hoạt động như một bản sao lưu thời gian thực. Ngay cả trong trường hợp ngắt kết nối tạm thời, khách hàng của bạn sẽ có thể đồng bộ lại dữ liệu bị mất sau đó nhờ rơle này. điều này giúp bạn kiểm soát hoàn toàn dữ liệu Nostr của mình



Ở chế độ nền, _Nostr Relay_ của Umbrel dựa trên dự án **nostr-rs-relay** mã nguồn mở (triển khai giao thức Rust). Nó hỗ trợ toàn bộ giao thức Nostr và nhiều NIP chuẩn (NIP-01, 02, 03, 09, 11, 12, 15, 16, 20, 22, 26, 28, 33, v.v.), đảm bảo khả năng tương thích tối đa với khách hàng.



### noStrudel - Nostr client dành cho các nhà thám hiểm



![Page d'installation de noStrudel sur l'App Store Umbrel](assets/fr/03.webp)



**noStrudel** là một máy khách web Nostr hướng đến người dùng có năng lực, lý tưởng để hiểu và khám phá mạng Nostr một cách chi tiết. Đây là một loại hộp cát để kiểm tra các sự kiện và rơle, và để thử nghiệm các tính năng nâng cao của giao thức. Interface bằng tiếng Anh và tương đối kỹ thuật, khiến nó trở nên lý tưởng cho những người dùng có kinh nghiệm tò mò về hoạt động bên trong của Nostr.



**Cài đặt:** Cài đặt _noStrudel_ từ Umbrel App Store (danh mục _Social_). Sau khi khởi chạy, bạn có thể truy cập thông qua trình duyệt tại Address của Umbrel (ví dụ: `http://umbrel.local` hoặc thông qua .onion/Tailscale, hãy xem phần truy cập bên ngoài).



![Page d'accueil de noStrudel avec le bouton Setup Relays](assets/fr/04.webp)



**Cấu hình rơle:** Khi bạn mở noStrudel, bạn sẽ thấy nút "Cài đặt rơle" ở góc trên bên phải. Nhấp vào nút đó để cấu hình rơle của bạn.



![Page de configuration des relais dans noStrudel](assets/fr/05.webp)



Trên trang này, dán URL của rơle Umbrel mà bạn đã sao chép trước đó. Bạn cũng có thể thêm các rơle khác được ứng dụng đề xuất theo mặc định. Sau khi bạn đã cấu hình rơle của mình, hãy nhấp vào "Đăng nhập" ở góc dưới bên trái để tiếp tục.



![Options de connexion dans noStrudel](assets/fr/06.webp)



**Kết nối:** noStrudel cung cấp cho bạn một số tùy chọn kết nối. Trong trường hợp của chúng tôi, chúng tôi sẽ chọn "Private Key" và dán vào khóa riêng Nostr đã tạo trước đó của bạn. Nếu bạn chưa có khóa, bạn có thể cài đặt tiện ích mở rộng [Nostr Connect] (https://chromewebstore.google.com/detail/nostr-connect/ampjiinddmggbhpebhaegmjkbbeofoaj) để tạo và/hoặc lưu khóa Nostr của bạn và do đó giao tiếp an toàn hơn với các ứng dụng Nostr khác nhau.



![Interface principale de noStrudel](assets/fr/07.webp)



Sau khi kết nối, bạn có thể sử dụng noStrudel để chia sẻ ghi chú của mình qua Nostr. Interface cung cấp cho bạn quyền truy cập vào:





- Bảng điều khiển Nostr đầy đủ với dòng thời gian ghi chú, thông báo, nhắn tin, tìm kiếm hồ sơ
- Quản lý rơle và trạng thái kết nối
- Các công cụ nâng cao để kiểm tra các sự kiện và nội dung JSON của chúng
- Tùy chọn cấu hình cho bộ lọc dòng thời gian và mã PIN



**Mẹo:** Trên _noStrudel_, bạn có thể thiết lập _bộ lọc dòng thời gian_ hoặc thử nghiệm các _NIP (Khả năng triển khai Nostr)_ khác nhau. Ví dụ, kiểm tra hỗ trợ cho NIP-05 (mã định danh phi tập trung) hoặc các tính năng mới hơn. Điều này khiến _noStrudel_ trở thành một công cụ tuyệt vời để thử nghiệm trong môi trường được kiểm soát.



### Snort - Khách hàng Nostr hiện đại trên Umbrel



![Page d'installation de Snort sur l'App Store Umbrel](assets/fr/08.webp)



**Snort** là một ứng dụng web Nostr khác có trên Umbrel, cung cấp **Interface** hiện đại, nhanh chóng và gọn gàng để tương tác với mạng xã hội phi tập trung. Không giống như noStrudel, nhắm đến người dùng có năng lực, _Snort_ hướng đến sự đơn giản khi sử dụng mà không phải hy sinh chức năng. Nó được xây dựng trong React và cung cấp UX gọn gàng gợi nhớ đến các mạng xã hội cổ điển, khiến nó phù hợp để sử dụng hàng ngày.



**Cài đặt:** Cài đặt _Snort_ từ Umbrel App Store (thể loại _Xã hội_).



![Page d'accueil de Snort avec le bouton S'inscrire](assets/fr/09.webp)



Khi bạn mở Snort, bạn sẽ thấy nút "Đăng ký" ở góc dưới bên trái.



![Options de connexion dans Snort](assets/fr/10.webp)



Bạn có thể chọn đăng ký hoặc kết nối với một tài khoản hiện có (đây là những gì chúng ta sẽ thực hiện trong hướng dẫn này).



![Méthodes de connexion dans Snort](assets/fr/11.webp)



Snort cung cấp một số phương pháp kết nối. Bạn có thể sử dụng tiện ích mở rộng Nostr Connect đã cài đặt trước đó hoặc các phương pháp khả dụng khác. Sau khi kết nối, bạn sẽ có thể sử dụng ứng dụng đầy đủ.



Interface từ _Snort_ cung cấp:





- Màn hình **Bài đăng/Cuộc trò chuyện/Toàn cầu** để điều hướng giữa các ghi chú, thảo luận theo chủ đề hoặc nguồn cấp dữ liệu toàn cầu của bạn
- Các tab dành cho **Thông báo**, **Tin nhắn** (DM), **Tìm kiếm**, **Hồ sơ**, v.v.
- Nút ***** hoặc _Viết_ để xuất bản ghi chú mới
- Quản lý **đăng ký (theo dõi)** và **danh sách**
- Menu quản lý rơle để thêm/xóa rơle và theo dõi tính khả dụng của chúng



**Cấu hình rơle được đề xuất:** Để thêm rơle Umbrel của bạn, hãy vào Settings - Relays. Nhập URL của rơle của bạn (`ws://umbrel:4848` hoặc URL khác tùy thuộc vào cấu hình của bạn) vào danh sách rơle của Snort. Theo cách này, Snort sẽ xuất bản ghi chú của bạn trên rơle riêng tư của bạn ngoài các rơle công khai.



### Nostr Wallet Connect - Liên kết Lightning Wallet của bạn với Nostr



**Nostr Wallet Connect (NWC)** là một ứng dụng **kết nối nút Umbrel (Lightning)** của bạn với các ứng dụng Nostr tương thích để thực hiện thanh toán Lightning (ví dụ: gửi _zaps_, các khoản thanh toán nhỏ để "thích" nội dung). Trong hướng dẫn này, chúng ta sẽ xem cách kết nối noStrudel với nút Lightning của bạn để thực hiện thanh toán trực tiếp từ Interface.



**Cài đặt và cấu hình:**



![Page d'installation de Nostr Wallet Connect sur l'App Store Umbrel](assets/fr/12.webp)



Cài đặt _Nostr Wallet Connect_ từ cửa hàng Alby trên Umbrel.



![Configuration de NWC dans noStrudel - Étape 1](assets/fr/13.webp)



Trong noStrudel, nhấp vào hồ sơ của bạn ở góc trên bên phải, sau đó nhấp vào nút "quản lý".



![Configuration de NWC dans noStrudel - Étape 2](assets/fr/14.webp)



Nhấp vào "Lightning" rồi "kết nối Wallet".



![Configuration de NWC dans noStrudel - Étape 3](assets/fr/15.webp)



Trong số các tùy chọn kết nối có sẵn, hãy chọn "Umbrel".



![Configuration de NWC dans noStrudel - Étape 4](assets/fr/16.webp)



Nhấp vào "Kết nối" để tự động được chuyển hướng đến phiên Umbrel Nostr Wallet Connect của bạn.



![Page de configuration des autorisations NWC](assets/fr/17.webp)



Trên trang Nostr Wallet Connect, bạn có thể:




   - Xác định ngân sách tối đa của bạn
   - Xác thực quyền hạn
   - Đặt thời gian hết hạn cho kết nối


Nhấp vào "kết nối" để hoàn tất.



![Confirmation de connexion dans noStrudel](assets/fr/18.webp)



Bạn sẽ được chuyển hướng đến noStrudel với thông báo xác nhận: bây giờ bạn có thể kết nối toàn bộ thế giới từ nút Wallet/LND của mình!



Nhờ NWC, **thanh toán Lightning của bạn qua Nostr** (zaps để thưởng bài đăng, _Giá trị cho giá trị_ thanh toán, v.v.) bắt đầu từ **nút của riêng bạn**. Bạn không còn phải định tuyến giao dịch của mình qua các dịch vụ bên ngoài hoặc quét mã QR từ điện thoại của mình mỗi lần. Trải nghiệm của người dùng được cải thiện đáng kể, trong khi vẫn _không lưu ký_ và thân thiện với quyền riêng tư.



Nếu bạn muốn biết cách thiết lập nút Lightning của riêng mình trên Umbrel, tôi khuyên bạn nên xem hướng dẫn toàn diện khác này:



https://planb.network/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

## Cấu hình và bảo mật nâng cao



Sử dụng Umbrel và Nostr cùng nhau ở cấp độ nâng cao đòi hỏi phải đặc biệt chú ý đến **bảo mật** và **kết nối**. Sau đây là một số mẹo về cách bảo vệ cấu hình của bạn và truy cập cấu hình đó một cách tối ưu, bất kể bạn ở đâu.



### Truy cập bên ngoài an toàn: Tor và Tailscale



Vì lý do bảo mật, Umbrel của bạn chỉ có thể truy cập theo mặc định trên mạng cục bộ của bạn (và thông qua Tor). Để tương tác với Nostr khi không ở nhà, bạn có hai giải pháp ưu tiên: **Tor** (truy cập ẩn danh qua mạng onion) và **Tailscale** (mạng VPN riêng tư).





- Truy cập qua Tor:** Umbrel tự động cấu hình **dịch vụ Tor (.onion)** cho trang web và ứng dụng Interface của nó. Điều này có nghĩa là bạn có thể truy cập Interface Umbrel (bao gồm _noStrudel_ hoặc _Snort_) từ bất kỳ đâu, bằng trình duyệt Tor, mà không cần tiết lộ IP công khai của bạn. _Tor được sử dụng để truy cập các dịch vụ Umbrel của bạn từ bên ngoài mạng cục bộ của bạn, mà không cần tiết lộ thiết bị của bạn trên Internet ([Cài đặt Tor trên hệ thống của bạn - Hướng dẫn - Cộng đồng Umbrel](https://community.umbrel.com/t/setup-tor-on-your-system/7509#:~:text=Official%20website%3A%20https%3A%2F%2Fwww))._ Để sử dụng tùy chọn này, hãy vào cài đặt Umbrel và lấy URL .onion của Umbrel (hoặc quét mã QR được cung cấp). Trên trình duyệt Tor, hãy truy cập .onion Address này: bạn sẽ nhận được cùng một Interface như cục bộ. Sau đó, bạn có thể sử dụng ứng dụng Nostr giống như ở nhà.


**Nostr relay qua Tor:** Nếu bạn muốn Nostr relay của bạn có thể được khách hàng (hoặc bạn bè được ủy quyền) truy cập qua Tor, điều này là có thể. Umbrel không cung cấp trực tiếp .onion Address của relay, nhưng vì nó chạy trên cổng 4848, bạn có thể:





    - Sử dụng .onion Address của UI Umbrel và cấu hình máy khách của bạn để kết nối thông qua Interface này (không thực tế đối với WebSocket),





    - Hoặc** hiển thị cổng 4848 như một dịch vụ onion riêng biệt. Điều này đòi hỏi phải mày mò cấu hình Tor trên Umbrel (dành riêng cho người dùng nâng cao quen với SSH). Ngoài ra, hãy cân nhắc **đường hầm Tor** trên một máy chủ khác chuyển hướng đến Umbrel: tuy nhiên, đối với mục đích sử dụng cá nhân, cách dễ nhất là sử dụng Tailscale.





- Truy cập qua Tailscale:** [Tailscale](https://tailscale.com/) là giải pháp VPN dạng lưới tạo ra mạng riêng ảo giữa các thiết bị của bạn và Umbrel. Ưu điểm: hoạt động như thể bạn đang ở trên mạng LAN, nhưng qua Internet, được mã hóa và không cần cấu hình phức tạp. **Tailscale gán cho Umbrel của bạn một IP cố định và một tên miền riêng, bất kể vị trí mạng của nó ([Tailscale | Umbrel App Store](https://apps.umbrel.com/app/tailscale#:~:text=Tailscale%20is%20zero%20config%20VPN,reviewed%20and%20trusted%20standard))**. Trên thực tế, sau khi bạn cài đặt Tailscale trên Umbrel (từ Umbrel App Store, danh mục _Mạng_) **và** trên các thiết bị của mình (di động, PC...), bạn sẽ có thể truy cập Umbrel thông qua Address như `100.x.y.z` (Địa chỉ IP Tailscale) hoặc tên như `umbrel.tailnet123.ts.net`.


đối với Nostr_, Tailscale cực kỳ hữu ích: điện thoại di động của bạn, nếu Tailscale đang hoạt động, sẽ có thể kết nối tới `ws://umbrel:4848` (nhờ MagicDNS) hoặc trực tiếp tới IP Tailscale và cổng 4848 để sử dụng relay. Các máy khách như Damus hoặc Amethyst sẽ thấy Umbrel của bạn như thể nó nằm trên cùng một mạng cục bộ. **Mẹo:** Bật tùy chọn **MagicDNS** trong Tailscale để sử dụng tên máy chủ `umbrel` thay vì ghi nhớ IP. Điều này đảm bảo kết nối mượt mà tới relay của bạn ngay cả khi bạn đang di chuyển ([Nostr Relay | Umbrel App Store](https://apps.umbrel.com/app/nostr-relay#:~:text=client%20%28e,That%27s%20it%21%20Your%20past)).


Hơn nữa, Tailscale cho phép bạn truy cập Interface Umbrel (và do đó là _noStrudel/Snort_ web clients) thông qua trình duyệt đơn giản, sử dụng IP riêng hoặc tên miền được chỉ định. Không cần Tor Browser và tốc độ truyền dữ liệu thường tốt hơn so với qua mạng Tor.




**Lưu ý: Tor và Tailscale không loại trừ lẫn nhau. Bạn có thể giữ Tor hoạt động để truy cập ẩn danh hoặc các dịch vụ cụ thể và sử dụng Tailscale hàng ngày vì tính đơn giản của nó. Trong cả hai trường hợp, bạn không cần mở cổng trên bộ định tuyến, điều này giúp tăng cường bảo mật.



### Bảo mật rơle Nostr của bạn (thực hành được khuyến nghị)



Nếu bạn tổ chức một cuộc thi tiếp sức Nostr trên Umbrel, đặc biệt là trong bối cảnh nâng cao, hãy đảm bảo áp dụng một số biện pháp hữu ích sau:





- Relay riêng tư hoặc bị hạn chế:** Theo mặc định, relay Umbrel của bạn là riêng tư (không được công bố công khai) và nếu bạn chỉ truy cập qua Tailscale hoặc mạng LAN của mình, thì nó sẽ không thể truy cập được từ người lạ. **Giữ bí mật liên kết ** Không phát trên mạng Nostr công cộng trừ khi bạn muốn tự nguyện lưu trữ những người dùng khác, đây là một vấn đề hoàn toàn khác (kiểm duyệt, băng thông, v.v.). Đối với mục đích sử dụng cá nhân, chúng tôi khuyên bạn nên giới hạn quyền truy cập cho bản thân và nếu cần, cho một vài người bạn và gia đình đáng tin cậy.





- Danh sách trắng/Xác thực**: Triển khai nostr-rs-relay hỗ trợ cơ chế xác thực **NIP-42** cũng như _danh sách trắng_ của khóa công khai. Bằng cách bật các tùy chọn này, bạn có thể hạn chế rơle của mình để nó **chỉ chấp nhận các sự kiện được ký bởi một số khóa nhất định (của bạn)** hoặc các máy khách phải xác thực để xuất bản. Việc thiết lập này yêu cầu chỉnh sửa tệp cấu hình `config.toml` của rơle trong Umbrel (thông qua SSH trong vùng chứa Docker)._ Đây là một thao tác nâng cao, nhưng ví dụ, bạn có thể liệt kê các quảng cáo được phép (`pubkey_whitelist`). Theo cách này, ngay cả khi ai đó phát hiện ra rơle của bạn, họ sẽ không thể xuất bản bất kỳ thứ gì ở đó nếu họ không có trong danh sách.





- Cập nhật và bảo trì:** Luôn cập nhật Umbrel và ứng dụng _Nostr Relay_. Các bản cập nhật có thể bao gồm cải thiện hiệu suất (ví dụ: xử lý thư rác tốt hơn) và sửa lỗi bảo mật. Trên Umbrel, hãy thường xuyên kiểm tra App Store để cập nhật _Nostr Relay_ và áp dụng khi cần thiết.





- Giám sát và giới hạn:** Hãy chú ý đến cách sử dụng rơle của bạn. Nếu bạn mở nó cho những người khác, hãy chú ý đến tải (lưu trữ CPU/RAM) trên Umbrel của bạn, vì rơle có thể nhanh chóng tích lũy rất nhiều dữ liệu. nostr-rs-relay cung cấp **giới hạn tốc độ và lưu trữ** có thể cấu hình được (`giới hạn` trong cấu hình, ví dụ: số sự kiện mỗi giây, kích thước sự kiện tối đa, xóa các sự kiện cũ...). Đối với mục đích sử dụng riêng tư, có thể bạn sẽ không cần động đến những mục này, nhưng hãy lưu ý rằng các tham số này tồn tại nếu bạn cần chúng ([nostr-rs-relay/config.toml tại master - scsibug/nostr-rs-relay - GitHub](https://github.com/scsibug/nostr-rs-relay/blob/master/config.toml#:~:text=)).





- Bảo mật khóa Nostr:** Điểm này đã được đề cập, nhưng rất quan trọng: không bao giờ nhập khóa riêng Nostr của bạn vào Interface mà bạn không hoàn toàn tin tưởng. Thay vào đó, hãy sử dụng tiện ích mở rộng trình duyệt hoặc thiết bị bên ngoài (như Nostr _signers_ trên các điện thoại riêng biệt) để ký các hành động nhạy cảm. Trên Umbrel, các ứng dụng web của bạn như _Snort_ và _noStrudel_ có thể hoạt động mà không cần biết khóa bí mật của bạn, thông qua NIP-07. Hãy tận dụng cơ hội này để kết hợp sự thoải mái và bảo mật.




Bằng cách làm theo những mẹo này, việc tích hợp nút Umbrel với Nostr của bạn sẽ vừa mạnh mẽ vừa an toàn. Bạn sẽ có một môi trường hoàn chỉnh: một nút Bitcoin cho các khoản thanh toán Lightning, một rơle Nostr riêng tư cho chủ quyền dữ liệu và các máy khách web Nostr hiệu suất cao để điều hướng mạng xã hội phi tập trung mới này. Hãy tận hưởng việc khám phá Nostr với Umbrel!