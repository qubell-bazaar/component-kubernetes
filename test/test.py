import os
import requests

from qubell.api.testing import *

@environment({
    "default": {}
})
class KubernetesOnCoreOSDevTestCase(BaseComponentTestCase):
    name = "component-kubernetes"
    #meta = os.path.realpath(os.path.join(os.path.dirname(__file__), '../meta.yml')) 
    destroy_interval = int(os.environ.get('DESTROY_INTERVAL', 1000*60*60*2))
    apps = [
       {"name": name,
        "file": os.path.realpath(os.path.join(os.path.dirname(__file__), '../%s.yml' % name)),
        "settings": {"destroyInterval": destroy_interval}
       }
    ]

    @classmethod
    def timeout(cls):
        return 60
   
    @instance(byApplication=name)
    def test_kube_instans(self, instance):
        url = instance.returnValues['kubernetes.kube-ui']
        resp = requests.get(url, verify=False, allow_redirects=False)
        assert resp.status_code == 301
