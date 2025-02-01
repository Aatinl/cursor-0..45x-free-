# Cursor 0.45.x 失效方案 (Fix for Cursor 0.45.x Issue)
* Key point: Keep the Cursor open when modifying `storage.json` instead of closing it before making changes
* 关键核心：在修改 `storage.json` 时保持 Cursor 打开，而不是关闭后修改
  
## English Version
### 0. Downgrade to 0.44.11
If you're experiencing issues with Cursor 0.45.x, consider downgrading to version 0.44.11.
**Download Cursor v0.44.11**
- [Download from Cursor Official](https://downloader.cursor.sh/builds/250103fqxdt5u9z/windows/nsis/x64)

### 1.  run `python fc.py`

### 🚀 Notes:
- Version: Tested on 0.44.11 (not verified for 0.45.x).\n
- Environment: Windows 11.\n
- Account Status: Make sure you're logged into your Cursor account while performing the steps (this hasn't been verified, and it might work without logging in).\n


## 中文版

### 0.降级到0.44.11
**v0.44.11下载地址：**
- [官网下载](https://downloader.cursor.sh/builds/250103fqxdt5u9z/windows/nsis/x64)

### 1. 下载fc.py  在同目录下使用`python fc.py`运行脚本

### 🚀注意事项：
- 版本：我测试的是0.44.11版本，未验证0.45.x版本。
- 操作环境：Windows 11。 
- 账号状态：操作时全程登录着Cursor账号（未验证，也许不登陆也行）。


