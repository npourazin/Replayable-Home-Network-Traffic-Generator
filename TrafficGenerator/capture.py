import subprocess
import time

if __name__ == '__main__':
    path = 'test.pcap'
    # p = subprocess.Popen(['tcpdump', '-I', '-i', 'en1',
    #                       '-w', path], stdout=subprocess.PIPE)

    p = subprocess.Popen(('sudo', 'tcpdump', '-l'), stdout=subprocess.PIPE)
    for row in iter(p.stdout.readline, b''):
        print(row.rstrip())

    time.sleep(10)
    p.terminate()
