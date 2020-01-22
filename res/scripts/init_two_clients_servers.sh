#/bin/bash

echo client
vim-emu compute start -d client_dc -n iperf-client -i rjpfitscher/genic-rubis --net '(id=client-eth0,ip=10.0.0.10/24)'  -c "./start_iperfc.sh 100 &"
vim-emu compute start -d client_dc -n stratos-client -i rjpfitscher/genic-rubis --net '(id=client-eth0,ip=10.0.0.15/24)'  -c "./start_client.sh 100 100 100 100 '128KB' 0 &"

echo web
vim-emu compute start -d server_dc -n iperf-server -i rjpfitscher/genic-rubis --net '(id=server-eth0,ip=10.0.0.50/24)'  -c "./start_server.sh 100 100 100 100 '128KB' 0 &"
vim-emu compute start -d server_dc -n stratos-server -i rjpfitscher/genic-rubis --net '(id=server-eth0,ip=10.0.0.55/24)'  -c "./start_server.sh 100 100 100 100 '128KB' 0 &"
