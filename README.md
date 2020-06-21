# PingSweeper - ICMP ping scanner tool

As the name suggests, PingSweeper is a multi-threaded python-based tool that sends ICMP ping packets to specific IP addresses to check liveliness of hosts
The advantage of using multithreading is that a separate thread is created for pinging each host. So the program does not have to wait for a response from a particular host before moving on to the next IP address.

## How to use

- Download the script to a folder of your choice on your linux system 
- Give executable permissions to the script
- Create a file named ```IP_file``` and add the required IP addresses to it
- Execute the script
```
$ ls -l
-rwxr-xr-x. 1 user1 user1 853 Jun 21 20:06 pingsweeper.py
$
$ chmod 755 pingsweeper.py
$
$ cat IP_file
186.192.90.5
106.10.250.10
35.154.241.130
22.33.142.32
13.227.237.16
103.23.45.62
$
$ ./pingsweeper.py 

186.192.90.5 is alive
106.10.250.10 is alive
35.154.241.130 is alive
22.33.142.32 is dead
13.227.237.16 is alive
103.23.45.62 is dead

Time taken: 2.08218884468

$ 
```
