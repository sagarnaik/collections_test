import subprocess
class K8s:
    def get_namespaces(self):
        res = subprocess.run(["kubectl get namespaces"], shell=True, capture_output=True, text=True)
        #res = subprocess.check_output('sudo kubectl get namespaces', shell=False)
        print(res.stdout)
        return res.stdout

    def get_nodes(self):
        res = subprocess.run(["kubectl get nodes"], shell=True, capture_output=True, text=True)
        #res = subprocess.check_output('sudo kubectl get nodes', shell=False)
        print(res.stdout)
        return res.stdout

    def get_pods(self):
        res = subprocess.run(["kubectl get pods"], shell=True, capture_output=True, text=True)
        #res = subprocess.check_output('sudo kubectl get pods', shell=False)
        print(res.stdout)
        return res.stdout

k = K8s()
k.get_namespaces()
k.get_nodes()
k.get_pods()
