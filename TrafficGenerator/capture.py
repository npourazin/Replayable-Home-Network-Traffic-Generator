import subprocess
import time

if __name__ == '__main__':
    path = 'test.pcap'
    p = subprocess.Popen(['tcpdump', '-I', '-i', 'en1',
                          '-w', path], stdout=subprocess.PIPE)
    time.sleep(10)
    p.terminate()
