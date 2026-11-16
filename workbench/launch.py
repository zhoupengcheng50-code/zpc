# -*- coding: utf-8 -*-
import os
import sys
import webbrowser
import threading
import time
import socket

def get_lan_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"

def open_browser():
    time.sleep(1.8)
    try:
        webbrowser.open("http://127.0.0.1:8000")
    except Exception:
        pass

def main():
    lan_ip = get_lan_ip()
    print("=" * 70)
    print("           ★ 无极仙途国际化翻译工作台 (Web版) ★")
    print("=" * 70)
    print(f"[*] 本机访问地址:    http://127.0.0.1:8000")
    print(f"[*] 局域网访问地址:  http://{lan_ip}:8000")
    print(f"[*] 浏览器将在 2 秒内自动为您打开工作台...")
    print(f"[*] 如需退出服务，请在此窗口按下 Ctrl + C 即可")
    print("=" * 70 + "\n")

    threading.Thread(target=open_browser, daemon=True).start()

    import uvicorn
    # 切换到 workbench 所在目录
    wb_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(wb_dir)
    sys.path.insert(0, wb_dir)
    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=False, log_level="info")

if __name__ == "__main__":
    main()
