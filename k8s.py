import subprocess
class K8s:
    def get_namespaces(self):
        try: 
            res = subprocess.check_output(["kubectl", "get", "namespaces"], text=True) 
            print(res)
            return res
        except subprocess.CalledProcessError as e: 
            print(f"Command failed with return code {e.returncode}")

    def get_nodes(self):
        try: 
            res = subprocess.check_output(["kubectl", "get", "nodes"], text=True) 
            print(res)
            return res
        except subprocess.CalledProcessError as e: 
            print(f"Command failed with return code {e.returncode}")

    def get_pods(self):
        try: 
            res = subprocess.check_output(["kubectl", "get", "pods"], text=True) 
            print(res)
            return res
        except subprocess.CalledProcessError as e: 
            print(f"Command failed with return code {e.returncode}")

k = K8s()
k.get_namespaces()
k.get_nodes()
k.get_pods()
