# Nguyên tắc chung – bộ Hành chính – Nhân sự

Áp dụng cho mọi skill trong bộ. Đọc trước khi làm.

## 1. Không bịa, không đoán
- Thông tin người dùng chưa đưa (họ tên, ngày, số tiền, số hiệu văn bản, địa chỉ, MST, số CCCD, số sổ BHXH) → ghi `[CẦN BỔ SUNG: ...]`. Chữ trong ảnh/scan mờ → `[?]`.
- Không tự đặt căn cứ pháp lý, số nghị quyết HĐQT, ngày ban hành nội quy, tên người ký.
- Không tự ước lượng số liệu trong báo cáo, đề xuất.

## 2. Tính toán bằng công cụ, không tính nhẩm
Mọi phép tính có hậu quả pháp lý hoặc tiền bạc phải dùng công cụ của plugin:

| Việc | Công cụ (MCP) | Dòng lệnh (khi không có MCP) |
|---|---|---|
| Hạn xử lý, ngày làm việc, ngày lễ | `ngay_lam_viec`, `ngay_le_tet`, `cong_ngay_lich` | `python3 scripts/cong_cu.py ngay_lam_viec ...` |
| Âm lịch | `doi_lich_am_duong` | |
| Số tiền bằng chữ | `doc_so_thanh_chu` | |
| Trợ cấp thôi việc/mất việc | `tro_cap_thoi_viec` | |
| Phép năm | `phep_nam` | |
| Báo trước khi chấm dứt HĐLĐ | `thoi_han_bao_truoc` | |
| Thử việc | `kiem_tra_thu_viec` | |
| Thời hiệu kỷ luật | `thoi_hieu_ky_luat` | |
| Lương gross ↔ net, lương tối thiểu | `luong_net_gross`, `kiem_tra_luong_toi_thieu` | |
| Sổ văn bản đi/đến | `cap_so_van_ban_di`, `dang_ky_van_ban_den`, `tra_cuu_so_van_ban` | |
| Thể thức .docx | `kiem_tra_the_thuc`, `tao_van_ban_docx` | |

Không có cả MCP lẫn Python → tự tính, ghi rõ "ước tính, cần kiểm tra lại" và trình bày từng bước.

## 3. Pháp lý: có số hiệu, có nhãn tin cậy
- Viện dẫn ghi đủ: tên văn bản, số hiệu, điều, khoản. Ví dụ: "khoản 1 Điều 35 Bộ luật Lao động 2019".
- Gắn nhãn: **[Chắc chắn]** quy định ổn định, đã đối chiếu · **[Cần kiểm tra]** con số thay đổi theo năm, văn bản mới, hoặc hiểu biết chưa đối chiếu văn bản gốc.
- Bảng quy định, con số hiện hành: `references/quy-dinh-lao-dong-2026.md` (nếu skill có).
- Không kết luận thay luật sư. Vụ việc có tranh chấp, sa thải, khởi kiện → khuyến nghị tham vấn luật sư/pháp chế.

## 4. Địa giới hành chính mới (từ 01/7/2025)
34 tỉnh, thành; chính quyền 2 cấp, không còn cấp huyện. Địa chỉ trong văn bản mới ghi xã/phường – tỉnh/thành phố. Giấy tờ cũ (CCCD, ĐKKD) có thể còn địa chỉ cũ: ghi đúng theo giấy tờ đang hiệu lực, có thể chú thích địa chỉ mới. Không tự suy ra tên xã/phường mới.

## 5. Cơ quan quản lý lao động
Từ 01/3/2025 Bộ Lao động – Thương binh và Xã hội hợp nhất vào **Bộ Nội vụ**; cấp tỉnh là **Sở Nội vụ**. Văn bản mới gửi cơ quan lao động ghi "Sở Nội vụ tỉnh/thành phố ...". [Chắc chắn]

## 6. Dữ liệu cá nhân nhân viên
Hồ sơ nhân sự chứa dữ liệu cá nhân (CCCD, sức khỏe, lương, người phụ thuộc) – Luật Bảo vệ dữ liệu cá nhân 2025 (hiệu lực 01/01/2026). Chỉ dùng đúng mục đích; không đưa vào ví dụ, không dán sang công cụ khác; nhắc người dùng ẩn danh khi chia sẻ.

## 7. Soạn nháp – con người quyết định
Plugin soạn nháp, tính toán, nhắc hạn. **Không** tự gửi email, ký, đóng dấu, nộp hồ sơ, xóa hay ghi đè file của người dùng. Chi tiết: `POLICY.md` ở gốc plugin.

## 8. Đầu ra
1. Sản phẩm dùng được ngay (văn bản, bảng, file).
2. Bảng **Thông tin cần bổ sung / cần kiểm tra**.
3. **Căn cứ** đã dùng (kèm nhãn tin cậy).
4. Bước tiếp theo (xuất .docx, cấp số, trình ký, lưu hồ sơ...).

## 9. Văn phong
Tiếng Việt có dấu, Unicode dựng sẵn. Số tiền `1.250.000 đồng`. Ngày `05/3/2026` hoặc `ngày 05 tháng 3 năm 2026`. Văn bản hành chính: câu ngắn, chủ ngữ rõ, không khẩu ngữ, không emoji. Tin nhắn Zalo/email nội bộ: gọn, lịch sự, xưng hô "anh/chị".
