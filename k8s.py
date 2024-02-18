import subprocess
class K8s:
    def get_namespaces(self):
        res = subprocess.check_output('sudo kubectl get namespaces', shell=True)
        print(res)
        return res

    def get_nodes(self):
        res = subprocess.check_output('sudo kubectl get nodes', shell=True)
        print(res)
        return res

    def get_pods(self):
        res = subprocess.check_output('sudo kubectl get pods', shell=True)
        print(res)
        return res

k = K8s()
k.get_namespaces()
k.get_nodes()
k.get_pods()
