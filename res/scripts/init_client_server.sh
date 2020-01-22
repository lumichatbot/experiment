#/bin/bash

echo client
vim-emu compute start -d client_dc -n client -i rjpfitscher/genic-rubis --net '(id=client-eth0,ip=10.0.0.10/24)'

echo web
vim-emu compute start -d server_dc -n server -i rjpfitscher/genic-rubis --net '(id=server-eth0,ip=10.0.0.50/24)'
