import socket
import time

HOST = "127.0.0.1"   # Porta local
PORT = 22            # porta fake SSH
BANNER = "SSH-2.0-OpenSSH_8.4 Ubuntu-5\r\n"
LOGFILE = "honeyssh.log"

def log(msg):
    with open(LOGFILE, "a") as f:
        f.write(msg + "\n")
    print(msg)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)
log(f"[+] HoneySSH rodando em {HOST}:{PORT}, banner: {BANNER.strip()}")

while True:
    conn, addr = s.accept()
    ip, port = addr
    ts = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    
    # envia banner fake
    try:
        conn.sendall(BANNER.encode())
    except:
        pass
    
    # fecha conexão
    conn.close()
    
    # log simples
    log(f"[{ts}] Conexão de {ip}:{port}")
