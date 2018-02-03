# banntopus
Multiprocessing banner grabber

## Usage

python banntops.py 
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
                        port to grab banner
  -m MATCH, --match MATCH
                        print ONLY when response contain string
  -o OUTPUT, --output OUTPUT
                        write output to file
  -x TIMEOUT, --timeout TIMEOUT
                        set timeout; default: 10 sec
