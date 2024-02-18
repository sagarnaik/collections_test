import subprocess
class K8s:
    def get_namespaces(self):
        res = subprocess.check_output('kubectl get namespaces', shell=True)
        return res

    def get_nodes(self):
        res = subprocess.check_output('kubectl get nodes', shell=True)
        return res

    def get_pods(self):
        res = subprocess.check_output('kubectl get pods', shell=True)
        return res
