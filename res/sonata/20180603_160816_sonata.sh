vim-emu compute start -d vnfs_dc -n firewall -i rjpfitscher/genic-vnf --net "(id=input,ip=10.0.0.20/24),(id=output,ip=10.0.0.21/24)" -c "./start_firewall.sh &"
vim-emu compute start -d vnfs_dc -n ids -i rjpfitscher/genic-vnf --net "(id=input,ip=10.0.0.30/24),(id=output,ip=10.0.0.31/24)" -c "./start_snort.sh &"
vim-emu network add -b -src iperf-client:client-eth0 -dst firewall:input
vim-emu network add -b -src firewall:output -dst ids:input
vim-emu network add -b -src ids:output -dst iperf-server:server-eth0
