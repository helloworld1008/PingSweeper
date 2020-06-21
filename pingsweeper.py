#!/usr/bin/env python

import threading, time, subprocess, os, sys

def hostLivelinessChecker(host):

	fo = open("/tmp/pingoutput_" + host, 'w')

	p = subprocess.Popen(["ping", "-c1", "-W1", host], stdout=fo, stderr=fo)

	time.sleep(2)

	p.poll()

	if p.returncode == 0:

		print "{0} is alive".format(host)

	else:

		print "{0} is dead".format(host)

	fo.close()

	os.remove("/tmp/pingoutput_" + host)
	


if __name__ == '__main__':

	if not os.access("IP_file", os.R_OK):

		print "\nIP_file does not exist in current directory\n"
		sys.exit(0)

	print ""

	threads = []

	t0 = time.time()

	for ip in open('IP_file'):

		thread = threading.Thread(target=hostLivelinessChecker, args=(ip.rstrip(),))

		threads.append(thread)

		thread.start()


	for t in threads:

		t.join()

	t1 = time.time()

	print ""

	print "\nTime taken: {0} seconds\n".format(t1-t0)
