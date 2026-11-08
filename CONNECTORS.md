# Connectors

Plugin gồm **1 connector có sẵn** (chạy trên máy, không cần tài khoản) và **các connector ngoài** bạn tự bật tùy công cụ đang dùng.

## 1. Connector có sẵn: `hcns-cong-cu` (MCP server cục bộ)

Khai báo trong `.mcp.json`, Claude Code / Claude Desktop tự khởi động khi bật plugin. Chỉ cần **Python 3.8+**, không cài thêm thư viện (riêng tạo/đọc file .docx cần `pip install python-docx`).

| Nhóm | Công cụ |
|---|---|
| Lịch | `doi_lich_am_duong`, `ngay_le_tet`, `ngay_lam_viec`, `cong_ngay_lich` |
| Văn thư | `cap_so_van_ban_di`, `dang_ky_van_ban_den`, `cap_nhat_van_ban_den`, `tra_cuu_so_van_ban`, `kiem_tra_the_thuc`, `tao_van_ban_docx`, `doc_so_thanh_chu` |
| Lao động | `tro_cap_thoi_viec`, `phep_nam`, `thoi_han_bao_truoc`, `kiem_tra_thu_viec`, `thoi_hieu_ky_luat`, `luong_net_gross`, `kiem_tra_luong_toi_thieu` |

Kiểm tra nhanh: `python3 mcp/server.py --tu-kiem-tra`

**Windows:** nếu lệnh `python3` không chạy, sửa `"command": "python3"` trong `.mcp.json` thành `"py"` hoặc `"python"`.

Sổ văn bản đi/đến lưu dạng CSV (mở bằng Excel) tại thư mục `so-van-ban/` trong thư mục làm việc hiện tại.

## 2. Connector ngoài (tùy chọn)

File skill dùng ký hiệu `~~nhóm` thay cho công cụ cụ thể. Bật connector tương ứng thì skill tự dùng; không có thì skill làm việc với file/nội dung bạn dán vào.

| Nhóm | Ký hiệu | Dùng để | Cách bật |
|---|---|---|---|
| Email | `~~email` | Soạn nháp thư mời phỏng vấn, offer, thông báo (chỉ tạo **nháp**) | Gmail / Microsoft 365 – bật trong claude.ai → Settings → Connectors (Claude Code đăng nhập tài khoản claude.ai dùng chung) |
| Lịch | `~~calendar` | Tìm giờ họp, lịch phỏng vấn, nhắc hạn | Google Calendar / Outlook Calendar – như trên |
| Lưu trữ tài liệu | `~~drive` | Tìm hồ sơ, mẫu văn bản, quy chế đã ban hành | Google Drive / OneDrive / SharePoint – như trên |
| Chat nội bộ | `~~chat` | Soạn tin thông báo nhóm | Slack, Microsoft Teams (có MCP chính thức). Zalo chưa có MCP chính thức: dùng n8n/Make làm cầu nối webhook |
| Phần mềm nhân sự (HRM) | `~~HRM` | Lấy danh sách nhân viên, chấm công, hợp đồng sắp hết hạn | MISA AMIS HRM, Base HRM, 1Office, Fast HRM... hiện chưa có MCP chính thức: xuất Excel rồi đưa cho Claude, hoặc làm MCP/n8n qua API của nhà cung cấp |
| Chữ ký số, hóa đơn | – | Không tích hợp: plugin **không ký số thay người dùng** | – |
| Cổng dịch vụ công / BHXH | – | Không tích hợp: plugin chuẩn bị hồ sơ, người dùng tự nộp | – |

### Thêm connector bằng `.mcp.json` (người dùng nâng cao)

Ví dụ thêm Notion (wiki quy chế nội bộ):

```json
{
  "mcpServers": {
    "hcns-cong-cu": { "command": "python3", "args": ["${CLAUDE_PLUGIN_ROOT}/mcp/server.py"] },
    "notion": { "type": "http", "url": "https://mcp.notion.com/mcp" }
  }
}
```

Chỉ thêm server bạn tin cậy; plugin không chịu trách nhiệm cho connector bên thứ ba.
