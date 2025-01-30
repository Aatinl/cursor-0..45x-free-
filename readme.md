# Cursor 0.45.x 失效方案 (Fix for Cursor 0.45.x Issue)

## English Version

### 0. Downgrade to 0.44.11
If you're experiencing issues with Cursor 0.45.x, consider downgrading to version 0.44.11.
**Download Cursor v0.44.11**
- [Download from Cursor Official](https://downloader.cursor.sh/builds/250103fqxdt5u9z/windows/nsis/x64)

### 1. Open `storage.json`
First, open the file:  
`%APPDATA%\Cursor\User\globalStorage\storage.json`  
Note: `%APPDATA%` is a system environment variable in Windows, ensure the path is correct.

### 2. Fake JSON Data
Use another AI (e.g., DeepSeek) to generate fake JSON data:  
```json
{
  "telemetry.macMachineId": "***", 
  "telemetry.sqmId": "{***}", 
  "telemetry.machineId": "***", 
  "telemetry.devDeviceId": "***"
}
```

### 3. Modify and Paste the Data
While Cursor is running, manually copy and paste the generated JSON data into the file and press ctrl+s to save changes.
If the file is read-only, change its properties to allow editing and then save the changes.

### 4. Restart Cursor
After saving the changes, restart Cursor and observe the file:
If you find that Cursor automatically reverts the data back to its original state (i.e., your fake data is lost), repeat step 3 and restart again.

### 🚀 Notes:
- Version: Tested on 0.44.11 (not verified for 0.45.x).\n
- Environment: Windows 11.\n
- Account Status: Make sure you're logged into your Cursor account while performing the steps (this hasn't been verified, and it might work without logging in).\n


## 中文版

### 0.降级到0.44.11
**v0.44.11下载地址：**
- [官网下载](https://downloader.cursor.sh/builds/250103fqxdt5u9z/windows/nsis/x64)

### 1. 打开Storage.json
首先，打开文件：  
`%APPDATA%\Cursor\User\globalStorage\storage.json`  
注意：`%APPDATA%` 是Windows的系统环境变量，确保路径是正确的。

### 2. 伪造 JSON 数据
使用其他AI（如 DeepSeek）生成伪造的JSON数据：  
```json
{
  "telemetry.macMachineId": "***", 
  "telemetry.sqmId": "{***}", 
  "telemetry.machineId": "***", 
  "telemetry.devDeviceId": "***"
}
```

### 3.修改并粘贴数据
在Cursor正在运行时，手动将生成的JSON数据复制粘贴到文件中,`ctrl+s`保存更改。
如果文件提示为只读，请修改文件属性为可写，然后保存更改。

### 4.重启 Cursor
保存更改后，重启Cursor并观察文件：
如果发现Cursor自动回滚到原始数据（即你更改的伪造数据丢失），请重复步骤3并重新启动。

### 🚀注意事项：
- 版本：我测试的是0.44.11版本，未验证0.45.x版本。
- 操作环境：Windows 11。 
- 账号状态：操作时全程登录着Cursor账号（未验证，也许不登陆也行）。


