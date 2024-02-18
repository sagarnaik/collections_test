import subprocess
import pytest
from k8s import K8s

# Fixture for the K8s instance
@pytest.fixture
def k8s_instance():
    k = K8s()
    return k

def test_get_namespaces(k8s_instance):
    print (k8s_instance.get_namespaces())
    assert 'Ubuntu' in k8s_instance.get_namespaces()

def test_get_nodes(k8s_instance):
    print (k8s_instance.get_nodes())
    assert 'Filesystem' in k8s_instance.get_nodes()

def test_get_pods(k8s_instance):
    print (k8s_instance.get_pods())
    assert 'ImagePullBackOff' in k8s_instance.get_pods()

def test_get_namespaces_error(k8s_instance):
    print (k8s_instance.get_namespaces())
    assert 'kube-system_error' in k8s_instance.get_namespaces()
