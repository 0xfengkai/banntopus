# banntopus
Multiprocessing banner grabber

## Description
The tool is design to grab a huge set of host banner in parallel, using python multiprocessing module.
Added in a match string switch to only display host banner user is interested in.
Tested to work in windows, Kali Linux and MacOS.

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

```

## To-do
[-] Integration of lightweight subnet port scanning utility
[-] Use regex for match switch

## Author
Feng Kai