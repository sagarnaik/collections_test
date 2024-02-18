import subprocess
import pytest
from k8s import K8s

# Fixture for the K8s instance
@pytest.fixture
def k8s_instance():
    return K8s()

def test_get_namespaces(k8s_instance):
    print (k8s_instance.get_namespaces())
    assert 'kube-system' in K8s.get_namespaces()

def test_get_nodes(k8s_instance):
    print (k8s_instance.get_nodes())
    assert 'minikube' in K8s.get_nodes()

def test_get_pods(mock_check_output, k8s_instance):
    print (k8s_instance.get_pods())
    assert 'ImagePullBackOff' in get_pods()

def test_get_namespaces_error(k8s_instance):
    print (k8s_instance.get_namespaces())
    assert 'kube-system_error' in K8s.get_namespaces()
