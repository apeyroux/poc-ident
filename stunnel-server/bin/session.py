#!/usr/bin/env python

import redis
import hashlib
import socket
import os
import sys

if __name__ == "__main__":

    rh = os.getenv("REMOTE_HOST")
    rp = os.getenv("REMOTE_PORT")
    dn = os.getenv("SSL_CLIENT_DN")
    idb = os.getenv("SSL_CLIENT_I_DN")

    key = hashlib.md5("%s:%s:%s:%s" % (rh,rp,dn,idb)).hexdigest()

    redisclient = redis.Redis('redis')
    redisclient.set(key, True)

    # f = open("/etc/stunnel/log-session.txt", 'a')
    # f.write(sys.stdin.read())

    # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # s.connect(("squid", 3128))

    # st = socket.fromfd(sys.stdin.fileno(), socket.AF_INET, socket.SOCK_STREAM)
    s = socket.create_connection(('squid', 3128))

    while True:
        try:
            stdin = sys.stdin.readline().strip()
            s.sendall(stdin)
            data = s.recv(999999)
            # st.send(data)
            print data
            # # Look for the response
            # amount_received = 0
            # amount_expected = len(stdin)

            # while amount_received < amount_expected:
            #     data = s.recv(1024)
            #     amount_received += len(data)
            #     st.send(data)
        finally:
            print >>sys.stderr, 'closing socket'
            s.close()
            st.close()
