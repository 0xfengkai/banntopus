# banntopus
Multiprocessing banner grabber

## Description
The tool is design to grab a huge set of host banner in parallel, using python multiprocessing module. Added in a match string switch to only display host banner user is interested in.

Tested to work in Windows, Kali Linux and MacOS.

## Usage
```
root@host# python banntops.py
usage: banntops.py [-h] -i INPUT [-w WORKER] [-p [PORT]] [-m MATCH]
                   [-o OUTPUT] [-x TIMEOUT] [--web] [--ssl]

required arguments:
  -i INPUT, --input INPUT
                        read input host file; Format: <IP>:<PORT>

webserver banner arguments:
  --web                 run web server banner grabbing
  --ssl                 run web server banner grabbing with https

optional arguments:
  -h, --help            show this help message and exit
  -w WORKER, --worker WORKER
                        workers to run; default workers: 4
  -p [PORT], --port [PORT]
                        port to grab banner if not specified in input file
  -m MATCH, --match MATCH
                        print ONLY when response contain string
  -o OUTPUT, --output OUTPUT
                        write output to file
  -x TIMEOUT, --timeout TIMEOUT
                        set timeout; default: 10 sec
```

## Usage Example
```

```

## Sample Output
```
root@host# python banntops.py -i iplist -p 22 -w 30
[*] host loaded: 200
[*] starting
<snipped>
[-] host: ('192.168.0.102', 22)	banner: SSH-2.0-OpenSSH_7.2p2 Ubuntu-4ubuntu2.4
[-] host: ('192.168.0.101', 22)	banner: SSH-2.0-OpenSSH_7.2p2 Ubuntu-4ubuntu2.4
[-] host: ('192.168.0.110', 22)	banner: SSH-2.0-OpenSSH_6.6.1
[-] host: ('192.168.0.87', 22)	banner: SSH-2.0-OpenSSH_7.2p2 Ubuntu-4ubuntu2.4
[-] host: ('192.168.0.108', 22)	banner: SSH-2.0-OpenSSH_6.6.1p1 Ubuntu-2ubuntu2.8
[-] host: ('192.168.0.96', 22)	banner: SSH-2.0-OpenSSH_7.2p2 Ubuntu-4ubuntu2.4
[-] host: ('192.168.0.104', 22)	banner: SSH-2.0-OpenSSH_7.2p2 Ubuntu-4ubuntu2.4
[-] host: ('192.168.0.106', 22)	banner: SSH-2.0-OpenSSH_7.2p2 Ubuntu-4ubuntu2.4
[-] host: ('192.168.0.84', 22)	banner: timed out
[-] host: ('192.168.0.85', 22)	banner: timed out
[-] host: ('192.168.0.86', 22)	banner: timed out
[-] host: ('192.168.0.114', 22)	banner: SSH-2.0-OpenSSH_7.4
[-] host: ('192.168.0.113', 22)	banner: SSH-2.0-OpenSSH_7.2p2 Ubuntu-4ubuntu2.4
[-] host: ('192.168.0.126', 22)	banner: SSH-2.0-OpenSSH_7.2p2 Ubuntu-4ubuntu2.4
[*] run complete

root@host# python banntops.py -i iplist -p 443 -w 30 --ssl
[*] host loaded: 200
[*] starting
<snipped>
[-] host: https://192.168.0.107:443/	banner: nginx/1.10.3 (Ubuntu)
[-] host: https://192.168.0.128:443/	banner: nginx/1.8.1
[-] host: https://192.168.0.117:443/	banner: nginx/1.10.3
[-] host: https://192.168.0.114:443/	banner: Apache
[-] host: https://192.168.0.140:443/	banner: nginx/1.10.3 (Ubuntu)
[-] host: https://192.168.0.133:443/	banner: timeout
[-] host: https://192.168.0.165:443/	banner: failed to establish connection
[-] host: https://192.168.0.161:443/	banner: nginx/1.10.3 (Ubuntu)
[-] host: https://192.168.0.217:443/	banner: Apache/2.2.31
[-] host: https://192.168.0.201:443/	banner: timeout
[-] host: https://192.168.0.202:443/	banner: timeout
[-] host: https://192.168.0.205:443/	banner: nginx/1.4.5
[-] host: https://192.168.0.234:443/	banner: Apache/2.2.29
[-] host: https://192.168.0.203:443/	banner: timeout
[*] run complete

root@host# python banntops.py -i iplist -p 22 -w 30 -m rosssh
[*] host loaded: 200
[*] starting
[-] host: ('192.168.0.74', 22)	banner: SSH-2.0-ROSSSH
[-] host: ('192.168.0.82', 22)	banner: SSH-2.0-ROSSSH
[-] host: ('192.168.0.90', 22)	banner: SSH-2.0-ROSSSH
[*] run complete
```

## To-do
* Integration of lightweight subnet port scanning utility
* Use regex for match switch

## Author
Feng Kai