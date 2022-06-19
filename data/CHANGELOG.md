### Cập Nhập ###

# [v1.0] #

- Thêm các lệnh `help`,`add`,`credits`,`ping`,`roll`,`seedmc`,`covid`,`svmc`
- Chỉnh sửa lệnh `seedmc`: seed mặc định => seed ngẫu nhiên
- Chỉnh sửa lệnh `help`: dạng ban đầu => định dạng mới


# [v1.1] #

- Thêm các lệnh `meme`,`emojify`,`anime`,`animechar`,`animenew`,`kick`,`ban`,`unban`
- Sửa lỗi lệnh `covid`: số ca mắc, số tử vong,... bị nhầm lẫn => số ca mắc, số tử vong,... rõ ràng hơn và loại bỏ vài
- Sửa lỗi lệnh `anime`,`animechar`: tìm anime/nhân vật anime với từ đầu tiên => tìm anime/nhân vật anime với cả cụm từ đã ghi
- Thêm tính năng `Báo lỗi` mỗi khi dùng lệnh sai cách
- Thêm tính năng `Không rõ lệnh` mỗi khi dùng lệnh không tồn tại bắt đầu bằng prefix bot
- Sửa lỗi lệnh `unban`: không thể gỡ cấm với người dùng bằng id hoặc tên => có thể gỡ cấm với id người dùng hoặc tên
- Sửa lỗi lệnh `kick`,`ban`: không đá/cấm người dùng bằng tên hoặc đề cập được => đá/cấm người dùng bằng tên hoặc đề cập đều được nếu đúng tên


# [v1.2] #

- Thêm lệnh `reminder`,`mute`,`unmute`,`profile`,`avatar`,`lock`,`unlock`,`perms`,`role`,`update`,`nick`
- Sửa lỗi các lệnh thuộc `Quản lý`: không dùng được lệnh(Thường do người dùng thiếu quyền cần thiết của lệnh đó hoặc bot bị thiếu quyền để thực hiện, dùng lệnh `perms` để xem tất cả các quyền cần thiết của từng lệnh thuộc `Quản lý`. Tốt nhất nên để bot có quyền `Người quản lý`)
- Chỉnh sửa lệnh `reminder`: thời gian nhắc nhở tính bằng giây(Ví dụ: tính thời gian 1 giờ bằng bao nhiêu giây để dùng lệnh) => thời gian nhắc nhở tính bằng ký hiệu thời gian
- Thêm tính năng lệnh `profile`: trạng thái hoạt động của người dùng
- Thêm tính năng lệnh `anime`: Khi anime cần tìm có nội dung NSFW thì ảnh của anime sẽ thay vào đó là ảnh nội dung cấm
- Thêm tính năng lệnh `profile`: Khi người dùng discord có avatar mặc định của discord, thì khi dùng `profile` sẽ không hiện avatar người dùng đó
- Thêm tính năng lệnh `role`: giới hạn tên vai trò khi tạo


# [v1.3] #

- Thêm lệnh `clear`,`math`,`info`,`qrcode`,`request`,`vote`
- Gỡ bỏ lệnh `emojify`
- Chỉnh sửa lệnh `update`: định dạng tin nhắn => định dạng tập tin
- Sửa lỗi lệnh `math`: Không nhận phép tính
- Chỉnh sửa lệnh `nick`: giới hạn tên biệt danh khi đặt
- Bot chính thức được công khai trên https://top.gg
- Bot chạy 24/7 giờ
- Chỉnh sửa bot: thông báo lỗi khi bot thiếu quyền để thực thi lệnh

# [v1.4] #

- Thêm lệnh `badwords`,`timeout`,`untimeout`,`file(premium)`,`trans`,`cash`,`slots`,`giveKUY TREA`
- Sửa lỗi lệnh `badwords`: không hiện tất cả các từ/không thể thêm từ/không thể bỏ từ ngữ xấu của/cho/khỏi máy chủ
- Chỉnh sửa các lệnh `ban`,`unban`,`mute`,`unmute`,`kick`,`role`: không thực thi lệnh và thông báo lỗi nếu người dùng khôngd có trong máy chủ/không có bị tắt tiếng/đã bị tắt tiếng/v.v...
- Chỉnh sửa lệnh `covid`: hiện thêm cờ khu vực, API covid mới
- Chỉnh sửa lệnh `help`: dạng ban đầu -> định dạng mới
- Thêm tính năng lệnh `file`: nhật ký chỉnh sửa lệnh `file log`
- Thêm tính năng lệnh `avatar` và `guild icon`: định dạng ảnh avatar/ic on
- Sửa lỗi phát hiện ngôn từ xấu: lặp cảnh báo lỗi
- Chỉnh sửa lệnh `svmc`: hiện thêm ảnh máy chủ (Nếu có)

# [v1.5] #

- Thêm lệnh `skins`,`level`,`agentval`,`activity`
- Chỉnh sửa lệnh `slots`,`cfg`: tắt giới hạn chơi tiền