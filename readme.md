# Cursor 0.45.x 失效方案 (Fix for Cursor 0.45.x Issue)
* Key point: Keep the Cursor open when modifying `storage.json` instead of closing it before making changes
* 关键核心：在修改 `storage.json` 时保持 Cursor 打开，而不是关闭后修改
* The 0.45.x version of Cursor employs extremely robust mechanisms. Despite attempting various file-locking methods (high-frequency writes, hidden attributes, kernel-level locks), Cursor forcibly replaces the JSON file if it detects anomalies. 
* 0.45.x 版本的 Cursor 采用了极其强大的机制。尽管我尝试了各种文件锁定方法（高频写入、隐藏属性、内核级锁定），但如果发现异常，Cursor 还是会强制替换 JSON 文件

## English Version
### 0. Downgrade to 0.44.11
If you're experiencing issues with Cursor 0.45.x, consider downgrading to version 0.44.11.
**Download Cursor v0.44.11**
- [Download from Cursor Official](https://downloader.cursor.sh/builds/250103fqxdt5u9z/windows/nsis/x64)

### 1.  run `python fc.py`

### 🚀 Notes:
- Version:0.44.11 (not 0.45.x).
- Environment: Windows 11
- Account Status: Make sure you're logged into your Cursor account while performing the steps (this hasn't been verified, and it might work without logging in).\n


## 中文版

### 0.降级到0.44.11
**v0.44.11下载地址：**
- [官网下载](https://downloader.cursor.sh/builds/250103fqxdt5u9z/windows/nsis/x64)

### 1. 下载fc.py  在同目录下使用`python fc.py`运行脚本

### 🚀注意事项：
- 版本：0.44.11版本，0.45.x版本无效。
- 操作环境：Windows 11
- 账号状态：操作时全程登录着Cursor账号（未验证，也许不登陆也行）。

