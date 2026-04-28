---
name: COLDCARD Q - Chuyên gia
description: Sử dụng các tùy chọn nâng cao của COLDCARD Q
---
![cover](assets/cover.webp)


![video](https://youtu.be/6L2hhT0J27s)


Trong bài hướng dẫn trước, chúng ta đã tìm hiểu về cấu hình ban đầu của COLDCARD Q và các chức năng cơ bản dành cho người mới bắt đầu. Nếu bạn vừa nhận được COLDCARD Q và chưa thiết lập nó, tôi khuyên bạn nên bắt đầu với bài hướng dẫn đó trước khi tiếp tục ở đây:


https://planb.academy/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3

Hướng dẫn mới này dành riêng cho các tùy chọn nâng cao của COLDCARD Q, được thiết kế cho người dùng cao cấp và cẩn trọng. Trên thực tế, COLDCARD khác biệt so với các phần cứng wallet khác bởi nhiều tính năng bảo mật tiên tiến. Tất nhiên, bạn không cần phải sử dụng tất cả các tùy chọn này. Chỉ cần chọn những tùy chọn phù hợp với chiến lược bảo mật của bạn.


**Cảnh báo**, việc sử dụng sai một số tùy chọn nâng cao này có thể dẫn đến mất Bitcoin hoặc làm hỏng thiết bị phần cứng wallet của bạn. Do đó, tôi đặc biệt khuyên bạn nên đọc kỹ hướng dẫn và giải thích cho từng tùy chọn.


Trước khi bắt đầu, hãy đảm bảo bạn có bản sao lưu vật lý của cụm từ ghi nhớ gồm 12 hoặc 24 từ, và kiểm tra tính hợp lệ của nó thông qua menu sau: `Nâng cao/Công cụ > Vùng nguy hiểm > Chức năng hạt giống > Xem từ hạt giống`.


![CCQ](assets/fr/01.webp)


## BIP39 passphrase


Nếu bạn không biết BIP39 passphrase là gì, hoặc nếu bạn chưa hiểu rõ cách thức hoạt động của nó, tôi đặc biệt khuyên bạn nên xem trước hướng dẫn này, hướng dẫn này bao gồm các kiến ​​thức lý thuyết cần thiết để hiểu các rủi ro liên quan đến việc sử dụng passphrase:


https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Hãy nhớ rằng, sau khi bạn đã thiết lập passphrase trên wallet, chỉ riêng cụm từ ghi nhớ (mnemonic) sẽ không đủ để lấy lại quyền truy cập vào bitcoin của bạn. Bạn sẽ cần cả cụm từ ghi nhớ và passphrase. Hơn nữa, bạn sẽ cần nhập passphrase mỗi khi mở khóa COLDCARD Q. Điều này tăng cường bảo mật bằng cách khiến việc tiếp cận vật lý với COLDCARD và biết mã PIN trở nên không đủ nếu không có passphrase.


Trên COLDCARDS, bạn có hai tùy chọn để quản lý passphrase của mình:


1. **Cách nhập liệu truyền thống:** Bạn nhập passphrase thủ công mỗi khi sử dụng thiết bị phần cứng wallet, giống như với các thiết bị phần cứng wallet khác. COLDCARD Q đơn giản hóa thao tác này với bàn phím đầy đủ của nó.


2. **Bạn có thể chọn mã hóa passphrase và lưu trữ nó trên thẻ nhớ microSD. Trong trường hợp này, bạn cần lắp thẻ microSD vào COLDCARD Q mỗi khi sử dụng. Lưu ý rằng thẻ microSD này chỉ hoạt động trên COLDCARD Q và không phải là bản sao lưu. Do đó, điều rất quan trọng là bạn cũng phải giữ một bản sao của passphrase trên một phương tiện vật lý, chẳng hạn như giấy hoặc kim loại.**


Để thiết lập BIP39 passphrase của bạn, hãy truy cập vào menu "*Mật khẩu*".


![CCQ](assets/fr/02.webp)


Nhập mã passphrase của bạn bằng bàn phím. Hãy chắc chắn chọn một mã passphrase mạnh (dài và ngẫu nhiên) và tạo bản sao lưu vật lý.


![CCQ](assets/fr/03.webp)


Sau khi bạn đã thiết lập passphrase, COLDCARD Q sẽ hiển thị cho bạn dấu vân tay khóa chính của wallet mới được liên kết với passphrase này. Hãy nhớ lưu lại dấu vân tay này. Khi bạn nhập lại passphrase khi sử dụng thiết bị trong tương lai, bạn có thể kiểm tra xem dấu vân tay được hiển thị có khớp với dấu vân tay bạn đã lưu hay không. Việc kiểm tra này đảm bảo rằng bạn không mắc lỗi khi nhập passphrase.


![CCQ](assets/fr/04.webp)


Giờ bạn có thể nhấn "*ENTER*" để áp dụng passphrase này vào cụm từ ghi nhớ của mình và kích hoạt wallet mới. Nếu bạn muốn lưu passphrase này vào thẻ nhớ microSD, hãy lắp thẻ vào khe cắm thích hợp và nhấn "*1*".


![CCQ](assets/fr/05.webp)


Mã passphrase của bạn đã được áp dụng thành công. Dấu ấn mã khóa sẽ hiển thị trên màn hình chính và ở đầu màn hình.


![CCQ](assets/fr/06.webp)


Mỗi lần mở khóa COLDCARD Q, bạn cần truy cập vào menu "*Mật khẩu*" và nhập passphrase theo cách tương tự như trên để áp dụng mật khẩu đó vào cụm từ ghi nhớ được lưu trữ trong thiết bị và truy cập đúng Bitcoin wallet.


![CCQ](assets/fr/07.webp)


Nếu bạn đã lưu passphrase vào thẻ nhớ microSD, mỗi khi sử dụng, hãy lắp thẻ nhớ vào COLDCARD và truy cập menu "*Mật khẩu*". COLDCARD sẽ tải passphrase trực tiếp từ thẻ nhớ microSD, vì vậy bạn không cần nhập mật khẩu thủ công. Nhấp vào "*Khôi phục đã lưu*".


![CCQ](assets/fr/08.webp)


Hãy kiểm tra xem độ dài và chữ cái đầu tiên của passphrase đã tải có chính xác hay không.


![CCQ](assets/fr/09.webp)


Hãy xác nhận rằng dấu vân tay hiển thị khớp với dấu vân tay của wallet của bạn và nhấp vào "*Khôi phục*".


![CCQ](assets/fr/10.webp)


Hãy nhớ rằng việc sử dụng passphrase có nghĩa là bạn cần nhập một bộ khóa mới được tạo ra từ sự kết hợp giữa cụm từ ghi nhớ và passphrase vào phần mềm quản lý wallet của bạn (như Sparrow, Wallet). Để làm điều này, hãy làm theo bước "*Cấu hình wallet mới trên Sparrow*" trong hướng dẫn khác này:


https://planb.academy/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3

## Tùy chọn mở khóa


COLDCARD cũng được hưởng lợi từ nhiều tùy chọn trong quá trình mở khóa thiết bị. Hãy cùng tìm hiểu thêm về những tùy chọn nâng cao này.


### Mã PIN lừa đảo


Mã PIN bí mật (Trick PIN) là mã PIN thứ cấp, khác với mã PIN được thiết lập trong quá trình cấu hình thiết bị ban đầu. Mã này được sử dụng để kích hoạt các hành động cụ thể đã được cấu hình sẵn ngay khi được nhập vào lúc bật COLDCARD. Bạn có thể cấu hình nhiều mã PIN bí mật, mỗi mã được liên kết với một hành động khác nhau. Các tính năng này cho phép bạn tùy chỉnh COLDCARD theo chiến lược bảo mật cá nhân của mình. Chúng đặc biệt hữu ích trong các trường hợp bị đe dọa về thể chất, chẳng hạn như trong một vụ cướp (thường được gọi trong cộng đồng Bitcoin là "*vụ tấn công bằng cờ lê 5 đô la*").


Để kích hoạt mã PIN bí mật và liên kết mã PIN đó với một hành động, hãy truy cập menu `Cài đặt > Cài đặt đăng nhập > Mã PIN bí mật`.


![CCQ](assets/fr/11.webp)


Chọn "*Thêm thủ thuật mới*".


![CCQ](assets/fr/12.webp)


Hãy thiết lập mã PIN cho thao tác đó và nhớ lưu lại.


![CCQ](assets/fr/13.webp)


Sau đó, hãy chọn hành động sẽ được thực hiện tự động mỗi khi bạn nhập mã PIN bí mật này. Dưới đây là danh sách các hành động có sẵn cho mã PIN:




- "*Tự phá hủy*: Hành động này sẽ phá hủy cả hai chip COLDCARD Q nếu nhập mã PIN bí mật, khiến thiết bị hoàn toàn không thể sử dụng được. Khi đó, sẽ không thể bán lại, sử dụng lại hoặc thậm chí trả lại cho Coinkite. Thiết bị sẽ trở nên lỗi thời không thể phục hồi. Tính năng này có thể được sử dụng trong trường hợp bị cướp để thuyết phục kẻ tấn công rằng hắn sẽ không bao giờ có thể truy cập được bitcoin của bạn. **Vui lòng lưu ý**: nếu không có bản sao lưu vật lý của cụm từ ghi nhớ và bất kỳ chip passphrase nào, bitcoin của bạn sẽ bị mất vĩnh viễn."


![CCQ](assets/fr/14.webp)




- "*Xóa Seed*": Menu này cung cấp một số thao tác để xóa seed, tức là đặt lại COLDCARD mà không làm hỏng nó. Không giống như tùy chọn "*Tự làm hỏng*", bạn có thể cấu hình lại thiết bị bằng cách sử dụng bản sao lưu cụm từ ghi nhớ của mình. Tuy nhiên, nếu không có bản sao lưu này, bitcoin của bạn sẽ bị mất. Dưới đây là các tùy chọn có sẵn:
 - "*Xóa & Khởi động lại*: Gỡ bỏ seed và khởi động lại COLDCARD mà không hiển thị bất kỳ thông tin nào trên màn hình."
 - "*Xóa im lặng*": Xóa dữ liệu trên seed một cách im lặng và mở khóa COLDCARD trên một wallet giả ngẫu nhiên như thể không có chuyện gì xảy ra.
 - "*Xóa -> Wallet*": Thao tác này sẽ xóa seed một cách kín đáo và mở khóa COLDCARD trên một thiết bị wallet phụ đã được cấu hình sẵn, được thiết kế như một mồi nhử. Thiết bị wallet này có thể chứa một phần nhỏ số bitcoin bạn đang tiết kiệm để đáp ứng yêu cầu của kẻ tấn công.
 - "*Thông báo Đã xóa, Dừng lại*": Xóa seed và hiển thị thông báo `Dữ liệu đã bị xóa, Dừng lại` trên màn hình.


![CCQ](assets/fr/15.webp)




- "*Duress Wallet*": Với thao tác này, mã PIN giả sẽ mở khóa một wallet được tạo ra từ seed bằng cách sử dụng BIP85. wallet thứ cấp này có thể được sử dụng làm mồi nhử để thuyết phục kẻ tấn công. COLDCARD hoạt động như thể nó là wallet thật, nhưng nếu không có mã PIN chính (khác với mã PIN giả), kẻ tấn công sẽ không bao giờ có thể truy cập vào wallet thật. Chiến lược này được thiết kế để khiến mọi người tin rằng wallet được liên kết với mã PIN giả là wallet duy nhất tồn tại.


![CCQ](assets/fr/16.webp)




- "*Đếm ngược đăng nhập*": Menu này nhóm các hành động có bộ đếm ngược trước khi chúng được thực thi. **Cảnh báo**, một số hành động có thể làm hỏng thiết bị của bạn hoặc dẫn đến mất bitcoin. Dưới đây là các hành động phụ có sẵn:
 - "*Xóa & Đếm ngược*: Xóa seed khỏi bộ nhớ của COLDCARD, sau đó bắt đầu đếm ngược một giờ. Nếu không lưu lại cụm từ ghim hoặc passphrase, bitcoin của bạn sẽ bị mất. Tùy chọn này được thiết kế để đánh lừa kẻ tấn công, khiến chúng nghĩ rằng thiết bị sẽ được mở khóa khi kết thúc đếm ngược, trong khi thực tế nó sẽ được khôi phục về cài đặt gốc."
 - "*Đếm ngược & Phá hủy*": Bắt đầu đếm ngược một giờ, sau đó COLDCARD sẽ phá hủy hai chip bảo mật của nó, khiến thiết bị không thể sử dụng được vĩnh viễn. Nếu không sao lưu, bitcoin của bạn sẽ bị mất. Hành động này được thiết kế để đánh lừa kẻ tấn công, khiến hắn nghĩ rằng đang chờ mở khóa, trong khi thực tế thiết bị sẽ tự hủy.
 - "*Chỉ đếm ngược*: Kích hoạt chế độ đếm ngược đơn giản một giờ, sau đó COLDCARD sẽ khởi động lại mà không cần thực hiện thêm bất kỳ thao tác nào. seed không bị xóa và thiết bị vẫn còn nguyên vẹn. Hãy cẩn thận đừng nhầm lẫn thao tác này với tùy chọn "*Đếm ngược đăng nhập*", được thảo luận trong các phần tiếp theo, tùy chọn này sẽ thêm bộ đếm ngược vào mã PIN chính trong khi vẫn cho phép truy cập vào wallet thực sự."


![CCQ](assets/fr/17.webp)




- "*Trông trống rỗng*": Hành động này khiến COLDCARD hiển thị trống rỗng, tạo ấn tượng rằng seed đã bị xóa. Trên thực tế, không có gì xảy ra và seed vẫn còn nguyên vẹn. Điều này mô phỏng một COLDCARD chưa được sử dụng hoặc đã được đặt lại.


![CCQ](assets/fr/18.webp)




- "*Chỉ cần khởi động lại*: Khi sử dụng mã PIN bí mật, COLDCARD chỉ đơn giản là khởi động lại. Không có hành động nào khác được thực hiện."


![CCQ](assets/fr/19.webp)




- "*Chế độ Delta*": Chức năng phức tạp này, chỉ dành cho người dùng có kinh nghiệm, được thiết kế để chống lại các cuộc tấn công ép buộc tinh vi, dù là từ nhà nước hay người thân có thông tin đặc quyền. Khi Chế độ Delta được kích hoạt, COLDCARD cung cấp quyền truy cập vào wallet thật, cho phép kẻ tấn công điều hướng và xác minh đó là wallet chính xác. Tuy nhiên, chữ ký giao dịch bị chặn, do đó ngăn chặn mọi chuyển khoản bitcoin. Ngoài ra, quyền truy cập vào cụm từ ghi nhớ bị vô hiệu hóa và mọi nỗ lực khôi phục nó sẽ dẫn đến việc xóa bỏ. Để tăng độ tin cậy, mã PIN giả được sử dụng với Chế độ Delta phải có cùng tiền tố với mã PIN thật (để hiển thị cùng các từ chống lừa đảo), nhưng hậu tố phải khác nhau.


![CCQ](assets/fr/20.webp)


Sau khi chọn hành động, hãy xác nhận lựa chọn của bạn.


![CCQ](assets/fr/21.webp)


Sau đó, bạn có thể xem tất cả các mã PIN giả lập đã được cấu hình trong menu chuyên dụng.


![CCQ](assets/fr/22.webp)


Bằng cách chọn một mã PIN bí mật hiện có, bạn có thể kiểm tra hành động liên kết với nó. Bạn cũng có thể ẩn nó bằng cách chọn "*Ẩn mã PIN bí mật*", khiến nó không hiển thị trong menu mã PIN bí mật. Bạn có thể xóa nó bằng cách nhấp vào "*Xóa mã PIN bí mật*", hoặc thay đổi mã PIN mà vẫn giữ nguyên hành động liên kết bằng cách chọn "*Thay đổi mã PIN*".


![CCQ](assets/fr/23.webp)


Tùy chọn "*Thêm nếu nhập sai*", có sẵn trong menu "*Mã PIN bí mật*", cho phép bạn cấu hình một hành động cụ thể sẽ tự động được kích hoạt sau một số lần nhập sai mã PIN chính nhất định. Số lần nhập sai cho phép có thể được thiết lập trong quá trình cấu hình.


### Xáo trộn chìa khóa


Tùy chọn "Mã hóa phím" cho phép bạn xáo trộn các chữ số hiển thị trên bàn phím khi nhập mã PIN. Tính năng này bảo vệ quyền riêng tư của mã PIN của bạn, ngay cả khi bị người khác hoặc camera theo dõi.


Để kích hoạt tùy chọn này, hãy truy cập menu `Cài đặt > Cài đặt đăng nhập > Mã hóa mật khẩu`.


![CCQ](assets/fr/24.webp)


Chọn tùy chọn "*Xáo trộn phím*".


![CCQ](assets/fr/25.webp)


Từ nay trở đi, mỗi khi bạn mở khóa COLDCARD Q, các phím trên bàn phím sẽ được gán số mới một cách ngẫu nhiên mỗi lần bạn sử dụng chúng.


![CCQ](assets/fr/26.webp)


### Đếm ngược đăng nhập


Tùy chọn này cho phép bạn thiết lập bộ đếm ngược mỗi khi bạn cố gắng mở khóa COLDCARD. Bạn có thể tích hợp nó vào chiến lược bảo mật của mình bằng cách trì hoãn việc truy cập vào thiết bị trong trường hợp bị đánh cắp, hoặc bằng cách trì hoãn trước khi ký kết giao dịch, ví dụ để tự bảo vệ mình trong trường hợp bị cướp. Tuy nhiên, bộ đếm ngược này áp dụng cho tất cả các lần sử dụng của bạn, kể cả khi bạn đang sử dụng COLDCARD một cách hợp pháp, điều này cũng đòi hỏi bạn phải kiên nhẫn. Hãy cẩn thận đừng nhầm lẫn tùy chọn này với hành động "*Chỉ đếm ngược*", chỉ được kích hoạt khi sử dụng mã PIN bí mật cụ thể.


Để cấu hình tùy chọn này, hãy truy cập menu `Cài đặt > Cài đặt đăng nhập > Đếm ngược đăng nhập`.


![CCQ](assets/fr/27.webp)


Chọn thời gian đếm ngược. Ví dụ, nếu bạn chọn 1 giờ, bạn sẽ phải đợi 1 giờ cho mỗi lần thử mở khóa COLDCARD Q.


![CCQ](assets/fr/28.webp)


Mỗi lần mở khóa, bạn sẽ được yêu cầu nhập mã PIN.


![CCQ](assets/fr/29.webp)


Sau đó chờ đến hết thời gian được thiết lập bởi bộ đếm ngược.


![CCQ](assets/fr/30.webp)


Khi đồng hồ đếm ngược kết thúc, bạn cần nhập lại mã PIN để truy cập thiết bị.


![CCQ](assets/fr/31.webp)


### Đăng nhập máy tính


Tùy chọn này cho phép bạn ngụy trang COLDCARD của mình thành máy tính khi mở khóa. Để kích hoạt tính năng này, hãy truy cập menu `Cài đặt > Cài đặt đăng nhập > Đăng nhập bằng máy tính`.


![CCQ](assets/fr/32.webp)


Kích hoạt tùy chọn bằng cách chọn nó.


![CCQ](assets/fr/33.webp)


Từ nay trở đi, mỗi khi thiết bị được bật, một máy tính bỏ túi hoạt động với các lệnh cơ bản sẽ được hiển thị.


![CCQ](assets/fr/34.webp)


Ví dụ, bạn có thể tính SHA256 hash của "*Plan ₿ Academy*".


![CCQ](assets/fr/35.webp)


Để mở khóa COLDCARD khỏi chế độ máy tính, hãy bắt đầu bằng cách nhập tiền tố mã PIN của bạn, theo sau là dấu gạch ngang. Ví dụ, nếu mã PIN của bạn là `00-00` (mã này yếu và chỉ là ví dụ, vì vậy hãy chọn mã PIN mạnh hơn), hãy nhập `00-`. COLDCARD sau đó sẽ hiển thị hai từ chống lừa đảo của bạn.


![CCQ](assets/fr/36.webp)


Sau đó, nhập mã PIN đầy đủ của bạn, cách nhau bằng dấu cách hoặc dấu gạch ngang, ví dụ: `00 00`.


![CCQ](assets/fr/37.webp)


Sau đó, COLDCARD sẽ thoát khỏi chế độ máy tính và mở khóa bình thường.


## Hủy sạch COLDCARD của bạn


Nếu bạn có kế hoạch loại bỏ thiết bị COLDCARD Q của mình, ví dụ như vì bạn hiện đang sử dụng thiết bị phần cứng wallet khác, điều quan trọng là phải tiêu hủy thiết bị đúng cách. Điều này đảm bảo rằng không có thông tin nào liên quan đến wallet của bạn có thể được bên thứ ba khôi phục.


Có ba cấp độ hủy thông tin, tùy thuộc vào nhu cầu của bạn. Trước khi bắt đầu, hãy đảm bảo rằng wallet của bạn đã được nhập vào một thiết bị wallet phần cứng khác, rằng bạn có quyền truy cập vào tất cả số tiền của mình và trên hết, rằng bạn có cụm từ ghi nhớ và bất kỳ passphrase nào, cả hai đều hoạt động bình thường. Nếu không có bản sao lưu wallet, việc hủy COLDCARD của bạn sẽ dẫn đến việc mất bitcoin.


Mức độ phá hủy đầu tiên bao gồm việc chỉ xóa seed. Tùy chọn này sẽ xóa cụm từ ghi nhớ của bạn khỏi bộ nhớ của COLDCARD, trong khi thiết bị vẫn hoạt động bình thường. Đây là lựa chọn lý tưởng nếu bạn muốn sử dụng lại COLDCARD Q vào một thời điểm sau đó. Để xóa seed khỏi bộ nhớ, hãy truy cập menu `Nâng cao/Công cụ > Vùng nguy hiểm > Chức năng hạt giống > Phá hủy hạt giống`.


![CCQ](assets/fr/38.webp)


Mức độ phá hủy thứ hai bao gồm việc vô hiệu hóa vĩnh viễn hai chip bảo mật của COLDCARD thông qua phần mềm. Hành động này khiến thiết bị hoàn toàn không thể sử dụng được. Bạn sẽ không thể bán lại, sử dụng lại hoặc trả lại cho Coinkite: nó sẽ bị phá hủy vĩnh viễn. Để tiếp tục, hãy làm theo các bước được mô tả trong phần trước liên quan đến mã PIN "*Brick Me*", sau đó cố ý nhập mã PIN này khi mở khóa COLDCARD.


Bước thứ ba liên quan đến việc phá hủy vật lý các linh kiện bảo mật của COLDCARD Q. Như trước đây, điều này sẽ khiến thiết bị không thể sử dụng được nữa. Để làm điều này, hãy dùng mũi khoan tạo một lỗ trên hai con chip ở phía trên bên phải của thiết bị (sau khi lật ngược thiết bị), gần dòng chữ "*SHOOT HERE*".


**Lưu ý quan trọng**:




- Để tránh nguy cơ bị điện giật, hãy tháo pin ra khỏi thiết bị và rút phích cắm khỏi nguồn điện trước khi sử dụng.
- Hãy đợi vài phút sau khi tắt máy trước khi bắt đầu khoan.
- Hãy đeo găng tay cách nhiệt và kính bảo hộ để đảm bảo an toàn.


![CCQ](assets/fr/39.webp)


Sau khi đã đục lỗ các chip, không được cố gắng kết nối lại COLDCARD Q.


Chúc mừng, bạn đã nắm vững các tùy chọn nâng cao của COLDCARD Q rồi!


Nếu bạn thấy hướng dẫn này hữu ích, tôi sẽ rất biết ơn nếu bạn để lại một biểu tượng ngón tay cái màu xanh lá cây bên dưới. Hãy thoải mái chia sẻ hướng dẫn này trên mạng xã hội của bạn. Cảm ơn rất nhiều!


Tôi cũng khuyên bạn nên xem hướng dẫn khác này, trong đó chúng tôi thảo luận về việc sử dụng một đối thủ cạnh tranh trực tiếp của CCQ, Ledger Flex:


https://planb.academy/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a