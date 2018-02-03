#!/usr/bin/env python

"""
Description:
Hackish fast multiprocessing banner grabbing script for huge set of IPs

To-do:
[*] Integrating subnet scanner for TCP open port

author:		fengkai
version: 	1.0.0
tested:		python 2.7.10
"""

import sys, argparse, requests, socket, multiprocessing
from functools import partial
from requests.packages import urllib3
urllib3.disable_warnings()

def urls_parser(data, port, SSL=False):
	hosts = []
	url_type = "https://" if SSL else "http://"
	for line in data:
		if ":" in line:
			hosts.append(url_type + line + "/")
		else:
			if port and port > 0 and port < 65536:
				hosts.append(url_type + line + ":" + str(port) + "/")
			else:
				print message_formatter("unspecific port for host %s" % line, 2)
	return hosts

def hosts_parser(data, port):
	hosts = []
	for line in data:
		if ":" in line:
			host, port = line.split(":")
			hosts.append((host, int(port)))
		else:
			if port and port > 0 and port < 65536:
				hosts.append((line, port))
			else:
				print message_formatter("unspecific port for host %s" % line, 2)
	return hosts

def url_grabber(parsed_url, timeout):
	response = ""
	with requests.Session() as session:
		session.headers.update({'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:10.0) Gecko/20100101 Firefox/10.0'})
		try:
			response = session.head(parsed_url, timeout=timeout, verify=False)
			if response.ok:
				response = response.headers["Server"]
			else:
				response = response.text
		except requests.exceptions.Timeout:
			response = "timeout"
		except Exception as e:
			response = "failed to establish connection"
	return response

def host_grabber(host, timeout):
	response = ""
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.settimeout(timeout)
	try:
		sock.connect(host)
		response = sock.recv(4096)
	except Exception as e:
		response = str(e)
	sock.close()
	return response

def file_reader(filename):
	data = []
	try:
		with open(filename, "r") as file:
			data = [line.strip() for line in file]
		print message_formatter("host loaded: %s" % (len(data)), 0)
	except:
		print message_formatter("input file error", 0)
	return data

def file_writter(filename, data):
	try:
		with open(filename, "a", 0) as file:
			file.write(str(data)+"\n")
			file.flush()
	except:
		print message_formatter("unable to write to file", 0)

def multiplexer(timeout, match_string, host):
	response = ""
	try:
		if "http" in host:
			response = url_grabber(host, timeout)
		else:
			response = host_grabber(host, timeout)
		if not match_string or match_string in response:
			return message_formatter("host: %s\tbanner: %s" % (host, response), 2)
	except Exception as e:
		return message_formatter("host: %s\terror: %s" % (host, str(e)), 0)

def consolidator(workers, hosts, timeout, match_string, outputfile=False):
	if len(hosts) > 0:
		print message_formatter("starting", 0)
		pool = multiprocessing.Pool(workers)
		try:
			func = partial(multiplexer, timeout, match_string)
			for response in pool.imap_unordered(func, hosts):
				if response:
					if outputfile:
						file_writter(outputfile, response)
					else:
						print response
		except KeyboardInterrupt:
			print message_formatter("process interrupted", 0)
			return
		else:
			pool.close()
		pool.join()
		print message_formatter("run complete", 0)
	else:
		print message_formatter("no applicable hosts", 0)
	
def message_formatter(message, c=1):
	print_type = ["[*]", "[+]", "[-]"]
	return print_type[c] + " " + message

class ArgumentParser(argparse.ArgumentParser):
	def error(self, message):
		self.print_help()
		sys.exit(0)

def main(argv):
	parser = ArgumentParser()
	optional = parser._action_groups.pop()
	required = parser.add_argument_group("required arguments")
	web = parser.add_argument_group("webserver banner arguments")

	required.add_argument("-i", "--input", help="read input host file; Format: <IP>:<PORT>", default="hosts", required=True)

	optional.add_argument("-w", "--worker", help="workers to run; default workers: 4", default=4, type=int)
	optional.add_argument("-p", "--port", help="port to grab banner", nargs="?", const=0, type=int)
	optional.add_argument("-m", "--match", help="print ONLY when response contain string", default=False)
	optional.add_argument("-o", "--output", help="write output to file", default=False)
	optional.add_argument("-x", "--timeout", help="set timeout; default: 10 sec", default=10, type=int)

	web.add_argument("--web", help="run web server banner grabbing", action="store_true")
	web.add_argument("--ssl", help="run web server banner grabbing with https", action="store_true")

	parser._action_groups.append(optional)

	try:
		args = parser.parse_args()
		output_filename = args.output
		input_filename = args.input
		port = args.port 
		workers = args.worker
		match_string = args.match
		timeout = args.timeout
		web = args.web
		ssl = args.ssl

		data = file_reader(input_filename)
		hosts = urls_parser(data, port, ssl) if web else hosts_parser(data, port)
		consolidator(workers, hosts, timeout, match_string, output_filename)
	except:
		pass

if __name__ == "__main__":
    main(sys.argv)
    sys.exit(0)

