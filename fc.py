import os
import json
import sys
import subprocess
import locale
import shutil
from pathlib import Path
from datetime import datetime

# 获取系统语言
def get_system_language():
    """
    get system language
    """
    try:
        # get system default language
        system_lang = locale.getdefaultlocale()[0].lower()
        return 'zh' if 'zh' in system_lang else 'en'
    except:
        return 'en'  # default return english

# define multi-language prompt information
MESSAGES = {
    'zh': {
        'checking_deps': '正在检查并安装所需依赖...',
        'installed': '已安装',
        'installing': '正在安装',
        'cursor_not_running': 'Cursor必须正在运行这个脚本才有效果，请启动Cursor后重新执行脚本',
        'cursor_running': '检测到Cursor正在运行',
        'cleared_data': '已清空json数据',
        'restart_prompt': '现在你可以手动重启Cursor了',
        'error': '发生错误',
        'press_exit': '按任意键退出...',
        'backup_success': '已备份原始文件到: {}',
        'backup_error': '备份文件失败'
    },
    'en': {
        'checking_deps': 'Checking and installing required packages...',
        'installed': 'installed',
        'installing': 'installing',
        'cursor_not_running': 'Cursor must be running for this script to work, please start Cursor and run this script again',
        'cursor_running': 'Cursor is running',
        'cleared_data': 'Cleared json data',
        'restart_prompt': 'Now you can restart Cursor manually',
        'error': 'Error',
        'press_exit': 'Press any key to exit...',
        'backup_success': 'Original file backed up to: {}',
        'backup_error': 'Failed to backup file'
    }
}

def install_dependencies():
    """
    install required packages
    """
    required_packages = ['psutil']
    lang = get_system_language()
    
    print(MESSAGES[lang]['checking_deps'])
    for package in required_packages:
        try:
            __import__(package)
            print(f'{package} {MESSAGES[lang]["installed"]}')
        except ImportError:
            print(f'{MESSAGES[lang]["installing"]} {package}...')
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
            print(f'{package} {MESSAGES[lang]["installed"]}')

install_dependencies()

import psutil

def is_cursor_running():
    """
    check if Cursor.exe is running
    """
    return "Cursor.exe" in (p.name() for p in psutil.process_iter())

def backup_file(source_path):
    """
    backup file
    """
    try:
        backup_path = source_path.parent / 'storage备份.json'
        shutil.copy2(source_path, backup_path)
        return backup_path
    except Exception as e:
        print(f'Backup error: {str(e)}')
        return None

def lock_storage_file():
    """
    lock storage.json file and clear data
    """
    lang = get_system_language()
    
    # check if Cursor.exe is running
    if not is_cursor_running():
        print(MESSAGES[lang]['cursor_not_running'])
        return
    else:
        print(MESSAGES[lang]['cursor_running'])
    
    # get storage.json path
    appdata = os.getenv('APPDATA')
    storage_path = Path(appdata) / 'Cursor' / 'User' / 'globalStorage' / 'storage.json'
    
    try:
        backup_path = backup_file(storage_path)
        if backup_path:
            print(MESSAGES[lang]['backup_success'].format(backup_path))
        else:
            print(MESSAGES[lang]['backup_error'])
            return
            
        with open(storage_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        # clear data
        data['telemetry.macMachineId'] = ''
        data['telemetry.sqmId'] = '{}'
        data['telemetry.machineId'] = ''
        data['telemetry.devDeviceId'] = ''
        
        # write modified data
        with open(storage_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)
            
        print('-' * 20)
        print(MESSAGES[lang]['cleared_data'])
        print('-' * 20)
        print(MESSAGES[lang]['restart_prompt'])
        return
    
    except Exception as e:
        print(f'{MESSAGES[lang]["error"]}: {str(e)}')
        
if __name__ == '__main__':
    try:
        lock_storage_file()
    except Exception as e:
        lang = get_system_language()
        print(f'{MESSAGES[lang]["error"]}: {str(e)}')
        input(MESSAGES[lang]['press_exit'])
