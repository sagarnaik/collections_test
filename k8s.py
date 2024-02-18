import subprocess
class K8s:
    def get_namespaces(self):
        try: 
            #subprocess.check_output(["KUBECONFIG=$HOME/.kube/config"], shell=True, text=True)
            res = subprocess.check_output(["uname", "-a"], text=True) 
            print(res)
            return res
        except subprocess.CalledProcessError as e: 
            print(f"Command failed with return code {e.returncode}")

    def get_nodes(self):
        try:
            #subprocess.check_output(["KUBECONFIG=$HOME/.kube/config"], text=True)
            res = subprocess.check_output(["df", "-h"], text=True) 
            print(res)
            return res
        except subprocess.CalledProcessError as e: 
            print(f"Command failed with return code {e.returncode}")

    def get_pods(self):
        try:
            #subprocess.check_output(["KUBECONFIG=$HOME/.kube/config"], shetext=True)
            res = subprocess.check_output(["python3", "--version"], text=True) 
            print(res)
            return res
        except subprocess.CalledProcessError as e: 
            print(f"Command failed with return code {e.returncode}")

k = K8s()
k.get_namespaces()
k.get_nodes()
k.get_pods()
