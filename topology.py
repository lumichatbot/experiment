# Must be run inside SONATA NFV son-emu Docker image
import logging
import signal
import subprocess
import time

from emuvim.api.openstack.openstack_api_endpoint import OpenstackApiEndpoint
from emuvim.api.rest.rest_api_endpoint import RestApiEndpoint
from emuvim.dcemulator.net import DCNetwork
from mininet.log import setLogLevel

logging.basicConfig(level=logging.INFO)
setLogLevel('info')  # set Mininet loglevel
logging.getLogger('werkzeug').setLevel(logging.DEBUG)
logging.getLogger('api.openstack.base').setLevel(logging.DEBUG)
logging.getLogger('api.openstack.compute').setLevel(logging.DEBUG)
logging.getLogger('api.openstack.keystone').setLevel(logging.DEBUG)
logging.getLogger('api.openstack.nova').setLevel(logging.DEBUG)
logging.getLogger('api.openstack.neutron').setLevel(logging.DEBUG)
logging.getLogger('api.openstack.heat').setLevel(logging.DEBUG)
logging.getLogger('api.openstack.heat.parser').setLevel(logging.DEBUG)
logging.getLogger('api.openstack.glance').setLevel(logging.DEBUG)
logging.getLogger('api.openstack.helper').setLevel(logging.DEBUG)


class DaemonTopology(object):
    def __init__(self):
        self.running = True
        signal.signal(signal.SIGINT, self._stop_by_signal)
        signal.signal(signal.SIGTERM, self._stop_by_signal)
        # create and start topology
        self.create_topology()
        self.start_topology()
        self.daemonize()
        self.stop_topology()

    def create_topology(self):
        self.net = DCNetwork(monitor=False, enable_learning=True)
        self.client_dc = self.net.addDatacenter("client_dc")
        self.vnfs_dc = self.net.addDatacenter("vnfs_dc")
        self.server_dc = self.net.addDatacenter("server_dc")

        self.switch1 = self.net.addSwitch("switch1")
        self.switch2 = self.net.addSwitch("switch2")

        linkopts = dict(delay="1ms", bw=100)
        self.net.addLink(self.client_dc, self.switch1, **linkopts)
        self.net.addLink(self.vnfs_dc, self.switch1, **linkopts)
        self.net.addLink(self.switch1, self.switch2, **linkopts)
        self.net.addLink(self.vnfs_dc, self.switch2, **linkopts)
        self.net.addLink(self.switch2, self.server_dc, **linkopts)

        # add the command line interface endpoint to the emulated DC (REST API)
        self.rest = RestApiEndpoint("0.0.0.0", 5001)
        self.rest.connectDCNetwork(self.net)
        self.rest.connectDatacenter(self.client_dc)
        self.rest.connectDatacenter(self.vnfs_dc)
        self.rest.connectDatacenter(self.server_dc)

    def start_topology(self):
        self.rest.start()
        self.net.start()
        subprocess.call("./res/scripts/init_two_clients_servers.sh", shell=True)

    def daemonize(self):
        print("Daemonizing vim-emu. Send SIGTERM or SIGKILL to stop.")
        while self.running:
            time.sleep(1)

    def _stop_by_signal(self, signum, frame):
        print("Received SIGNAL {}. Stopping.".format(signum))
        self.running = False

    def stop_topology(self):
        self.rest.stop()
        self.net.stop()


def main():
    DaemonTopology()


if __name__ == '__main__':
    main()
