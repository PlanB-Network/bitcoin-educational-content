---
name: Braiins Mini Miner
description: Dễ dàng thực hiện Mining tại nhà.
---
![cover](assets/cover.webp)



## Giới thiệu



Mini Miner braiins BMM 100 là sản phẩm do Mining pool Braiins tạo ra. Thiết bị này có thiết kế hấp dẫn và cực kỳ yên tĩnh. Nó tạo ra công suất tính toán 1,1 Th/s và tiêu thụ khoảng 40 watt. Không giống như các thiết bị khác, nó không phải là mã nguồn mở, nhưng nó thực sự dễ cài đặt, thực sự chỉ mất vài cú nhấp chuột! Mini Miner BMM 100 là phiên bản đầu tiên được phát hành. Hiện tại, phiên bản 2 đang được sản xuất, có tên là BMM 101, khác với phiên bản đầu tiên ở chỗ có màn hình lớn hơn và có Wi-Fi, nhưng quy trình cài đặt thì giống nhau.



Bạn cũng có thể tìm thấy nhiều thông tin quan trọng hơn bằng cách xem hướng dẫn đầy đủ trực tiếp trên [trang web của nhà sản xuất](https://braiins.com/hardware/mini-Miner-bmm-100).



## Tổng quan về BMM 100



thiết bị trông giống như một hình hộp chữ nhật có màn hình ở mặt trước



![image](assets/en/01.webp)



một cái quạt ở phía trên



![image](assets/en/02.webp)



trong khi ở mặt sau chúng ta có: lỗ cắm nguồn, không gian cho thẻ SD (có thể cần thiết cho bất kỳ bản cập nhật nào), một nút nhỏ có ghi `IP REPORT` cho phép bạn biết IP Address của mini Miner, Address nào cần thiết để truy cập bảng điều khiển thiết bị. Sau khi nhấn nút, IP Address sẽ hiển thị trong khoảng 5 giây, sau đó biến mất và màn hình cài đặt xuất hiện lại. Tuy nhiên, nếu bạn cần thay đổi một số cài đặt, chỉ cần nhấn lại nút đó và IP Address sẽ xuất hiện lại trên màn hình. Tiếp tục với danh sách, chúng ta tìm thấy một cổng Ethernet và quyền truy cập để thực hiện đặt lại thiết bị, bạn sẽ cần lấy một chốt và giữ trong 10 giây để đặt lại tất cả các cài đặt của mini Miner. Cuối cùng, chúng ta tìm thấy hai đèn báo, một Green và một màu đỏ, cho chúng ta biết trạng thái của Miner.



![image](assets/en/03.webp)



## Kết nối Mini Miner



Bạn sẽ cần kết nối thiết bị với internet qua ethernet, lưu ý rằng với phiên bản mới (BMM 101), điều này không còn cần thiết nữa. Quay lại với mini Miner này, sau khi xác định được vị trí, chúng ta sẽ cần kết nối nó với đường truyền internet trước rồi mới đến nguồn điện: thiết bị sẽ tự động bật và hiển thị IP Address trên màn hình.



## Cấu hình



Chúng ta cần mở trình duyệt và nhập IP Address cho chúng ta thấy mini Miner trong thanh tìm kiếm. Tôi nhắc bạn rằng để tìm thấy thiết bị trên mạng, bạn sẽ phải ở địa phương, vì vậy bạn sẽ phải kết nối máy tính bạn đang sử dụng với cùng mạng với mini Miner. Sau khi nhập IP Address, chúng ta nhấn enter và trang đăng nhập vào hệ điều hành của mini Miner, đó là Braiins OS, sẽ xuất hiện trên màn hình.



![image](assets/en/06.webp)



Để đăng nhập, bạn sẽ phải nhập `root` làm tên người dùng, trong khi bạn có thể để trống mật khẩu. Nhấp vào đăng nhập và bảng điều khiển mini Miner của bạn sẽ xuất hiện.



![image](assets/en/07.webp)



## Cài đặt chung



Chúng ta hãy đến Hệ thống



![image](assets/en/24.webp)



Trong phần cài đặt, chúng ta sẽ thấy một số cài đặt chung như chủ đề (sáng hoặc tối), ngôn ngữ, múi giờ và thay đổi mật khẩu.



![image](assets/en/25.webp)



Nếu chúng ta vào "Mini Miner Screen" thay vào đó, chúng ta có các thiết lập của mini Miner, chẳng hạn như màn hình hiển thị. Chúng ta có thể chọn hiển thị thời gian, hoặc giá của Bitcoin, hoặc màn hình có thông tin trạng thái máy như sản phẩm Hash, nhiệt độ, công suất tiêu thụ, v.v. Ở đây, tùy bạn chọn những gì bạn muốn thấy trên màn hình; chúng ta cũng có thể thay đổi độ sáng của màn hình, đặt chế độ ban đêm và hiển thị thời gian theo định dạng 12 giờ hoặc 24 giờ.



![image](assets/en/26.webp)



Sau khi bạn đã thực hiện thay đổi, hãy nhấp vào `Lưu thay đổi` và bạn sẽ thấy những thay đổi trên màn hình thiết bị của mình



![image](assets/en/27.webp)



## Kết nối với Mining pool



Bây giờ chúng ta vẫn chưa hoạt động, vì chúng ta phải kết nối với một nhóm để khởi động Mining, vì vậy chúng ta phải vào "Cấu hình"



![image](assets/en/08.webp)



và mục đầu tiên chỉ là `Pools`.



![image](assets/en/09.webp)



Ở đây chúng ta sẽ phải quyết định sử dụng pool nào. Trong hướng dẫn này, tôi sẽ chỉ cho bạn hai lựa chọn. Đầu tiên là kết nối chúng ta với Mining pool Braiins, cũng được các thợ đào chuyên nghiệp sử dụng, như bạn có thể thấy từ hướng dẫn này:



https://planb.network/it/tutorials/mining/pool/braiins-pool-557be706-35a9-4375-a563-d55ab5c69f55

Lựa chọn thứ hai là kết nối chúng ta với Mining pool có thể sử dụng solo, như Public Pool, hãy làm theo hướng dẫn sau để thực hiện:



https://planb.network/it/tutorials/mining/pool/public-pool-42b9e1b5-722d-471d-b1e3-9ca758065be1

### Bể não



Để kết nối với nhóm này, chúng ta cần tạo một tài khoản. Nhóm này cũng thực hiện thanh toán bằng Lightning Network, vì vậy chúng ta sẽ có thể nhận được một vài Sats mỗi ngày. Để làm được điều này, chúng ta cần thiết lập một Address lightning để nhận phần thưởng. Nếu bạn không biết cách tạo tài khoản trên nhóm brainins hoặc cách thiết lập Address lightning của mình, bạn có thể làm theo hướng dẫn này:



https://planb.network/it/tutorials/mining/pool/braiins-pool-557be706-35a9-4375-a563-d55ab5c69f55

Sau khi hoàn tất, chúng ta sẽ vào bảng điều khiển nhóm Braiins. Những gì chúng ta phải làm là cho nhóm biết rằng chúng ta muốn kết nối với một trong những Người khai thác của mình, vì vậy ở phía bên trái của màn hình, bạn sẽ thấy một số mục nhập. Chúng ta cần đến "người lao động".



![image](assets/en/04.webp)



và chúng ta cần nhấp vào nút màu tím bên phải có nội dung "Kết nối công nhân".



![image](assets/en/05.webp)



Đây là cửa sổ với thông tin chúng ta cần để kết nối mini Miner của mình với hồ bơi. Ở đây, thay đổi duy nhất chúng ta có thể thực hiện là chọn Stratum V2. Để tìm hiểu Stratum v2 là gì, hãy xem mục này trong [glossary](https://planb.network/en/resources/glossary/stratum-v2).



![image](assets/en/10.webp)



Bây giờ chúng ta cần sao chép chuỗi này bắt đầu bằng stratumv2. Vì vậy, chúng ta nhấp vào biểu tượng "sao chép" nhỏ, sau đó chúng ta đi đến bảng điều khiển của mini Miner mà chúng ta đã để lại trong cấu hình và nhóm. Chúng ta nhấp vào thêm nhóm mới



![image](assets/en/11.webp)



và dán chuỗi ký tự chúng ta đã sao chép vào khoảng trống bên dưới Pool URL.



![image](assets/en/12.webp)



Bây giờ chúng ta cần thêm tên người dùng và mật khẩu. Quay lại bảng điều khiển nhóm. Bên dưới chúng ta cũng có một userID và mật khẩu. UserID và tên người dùng của chúng ta, tên mà chúng ta đã cung cấp khi tạo tài khoản, cùng với tên của Miner mà chúng ta muốn đưa vào. Bạn có thể quyết định có nên đặt tên cho thiết bị mà bạn đang kết nối với nhóm hay không, tùy chọn này là tùy chọn, nhưng nên đưa vào, vì vậy nếu bạn kết nối nhiều thiết bị, sẽ dễ dàng hơn để xác định chúng ngay lập tức. Nếu bạn không muốn đưa bất kỳ thứ gì thay thế, bạn có thể để nguyên `workerName`.



![image](assets/en/13.webp)



Sau đó, chúng ta vào mini Miner và nhập tên người dùng. Ở đây, chúng ta sẽ nhập trong trường hợp của tôi là "finalstepbitcoin", đó là userID của tôi, miniminer dot. Đây là tên tôi quyết định đặt cho thiết bị. Nếu bạn không muốn đặt tên, chỉ cần viết userid dot workername. Trong trường hợp của tôi, đó sẽ là finalstepbitcoin.workername. Sau khi nhập tên người dùng, bạn có thể chọn mật khẩu và viết vào ô trống. Bạn cũng có thể nhập anithing123, đây cũng là mật khẩu được hiển thị trên màn hình nhóm, nhưng nó chỉ muốn chỉ ra rằng bạn có thể nhập bất kỳ mật khẩu nào bạn muốn.



Sau khi nhập tất cả dữ liệu, bạn phải nhấn nút lưu ở bên phải (nút có hình dạng giống đĩa mềm) và theo cách này, bạn đã cấu hình xong dữ liệu nhóm trong mini Miner.



![image](assets/en/14.webp)



Bây giờ bạn phải quay lại bảng điều khiển nhóm và nhấp vào "Đã kết nối! Quay lại".



![image](assets/en/15.webp)



Chúng tôi đã kết nối mini Miner của mình với nhóm brainins! Bây giờ bạn có thể thấy nó trong danh sách công nhân. Nếu nó không hiển thị, chỉ cần làm mới và đợi một vài phút. Khi nó xuất hiện, hãy xác minh rằng nó có trạng thái "OK" bằng dấu kiểm Green.



![image](assets/en/17.webp)



nếu bạn quay lại bảng điều khiển, bạn sẽ bắt đầu thấy chuyển động trên biểu đồ và thấy Hashrate của thiết bị của chúng tôi. Điều này có nghĩa là nhóm đang nhận công việc của chúng tôi và do đó chúng tôi đang phá hoại về mọi mặt.



![image](assets/en/16.webp)



### Hồ bơi công cộng



Thông qua nhóm này, người ta có thể thử vận may và khai thác một mình, dựa vào một nhóm. Trong trường hợp này, chúng ta sẽ không nhận được phần thưởng, nhưng chúng ta sẽ nhận được toàn bộ phần thưởng nếu chúng ta có thể khai thác một khối. Sau đó, chúng ta sẽ liên kết đến nhóm công khai, một nhóm chỉ dành cho Mining hoàn toàn là mã nguồn mở. Chúng ta mở một cửa sổ mới trên trình duyệt và đi đến [web.public-pool.io](https://web.public-pool.io/#/).



![image](assets/en/18.webp)



có một trang với tất cả thông tin chúng ta cần. Sau đó chúng ta sao chép tầng Address ở đó



![image](assets/en/19.webp)



sau đó chúng ta quay lại bảng điều khiển của mini Miner, vào cấu hình và nhóm, nhấp vào thêm nhóm mới (quy trình tương tự như trên) và dán 'stratum Address vào url nhóm.



![image](assets/en/20.webp)



Bây giờ chúng ta hãy quay lại trang pool và thấy rằng tên người dùng phải nhập Bitcoin Address, đây sẽ là số mà chúng ta sẽ nhận được phần thưởng trong trường hợp chúng ta phá được một khối, sau đó là một dấu chấm và sau đó là tên thiết bị của chúng ta, như chúng ta đã làm trước đó với Braiins Pool, trong khi mật khẩu chúng ta có thể tự chọn.



![image](assets/en/21.webp)



Chúng ta quay lại mini Miner và dưới tên người dùng, chúng ta dán Address Bitcoin theo sau là dấu chấm và tên, tôi sẽ đặt `miniminer`. Trong mật khẩu thay vào đó tôi sẽ đặt kiểm tra, bạn nhập bất cứ thứ gì bạn muốn.



![image](assets/en/22.webp)



Bây giờ chúng ta lưu cài đặt và vô hiệu hóa nhóm Braiins.



![image](assets/en/23.webp)



Tốt! Bây giờ chúng ta đang ở Mining trên hồ bơi công cộng!



![MINI MINER BRAIINS | un oggetto di design che mina BITCOIN.](https://www.youtube.com/watch?v=pzzWmM2tEAQ&t=284s)