import os
import subprocess

# 저장할 리소스 목록 (namespace에 종속된 리소스)
RESOURCE_TYPES = [
    "deployments",
    "statefullsets",
    "services",
    "configmaps",
    "secrets",
    "persistentvolumeclaims"
]

EXCLUDED_NAMESPACE = "cots-dev"
OUTPUT_DIR = "output"

def get_namespaces():
    try:
        # kubectl로 namespace 정보를 JSON으로 조회
        result = subprocess.run(
            ["kubectl", "get", "namespaces", "-o", "jsonpath={.items[*].metadata.name}"],
            capture_output=True,
            text=True,
            check=True
        )

        # 결과 파싱
        return result.stdout.strip().split()

    except subprocess.CalledProcessError as e:
        print(f"Error running kubectl: {e.stderr}")
        return []

def save_resource_yaml(namespace, resource):
    try:
        # Save deployment yaml
        result = subprocess.run(
            ["kubectl", "get", resource, "-n", namespace, "-o", "yaml"],
            capture_output=True,
            text=True,
            check=True
        )
        if not result.stdout.strip():
            return # empty result, skip

        ns_dir = os.path.join(OUTPUT_DIR, namespace)
        os.makedirs(ns_dir, exist_ok=True)

        filename = os.path.join(ns_dir, f"{resource}.yaml")

        with open(filename, "w") as f:
            f.write(result.stdout)

        print(f"[✔] Saved deployments from namespace '{namespace}' to {filename}")

    except subprocess.CalledProcessError as e:
        print(f"[⚠] Failed to get deployments from namespace '{namespace}': {e.stderr.strip()}")

def save_persistent_volumes():
    # Save PV Resource
    try:
        result = subprocess.run(
            ["kubectl", "get", "persistentvolumes", "-o", "yaml"],
            capture_output=True,
            text=True,
            check=True
        )
        if not result.stdout.strip():
            return

        os.makedirs(OUTPUT_DIR, exist_ok=True)
        filename = os.path.join(OUTPUT_DIR, "persistentvolumes.yaml")
        with open(filename, "w") as f:
            f.write(result.stdout)
        print(f"[✔] Saved PersistentVolumes to {filename}")
    except subprocess.CalledProcessError as e:
        print(f"[⚠] Failed to get PersistentVolumes: {e.stderr.strip()}")

def run_backup():
    try:
        namespaces = get_namespaces()
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Failed to retrieve namespaces: {e.stderr.strip()}")
        return

    for ns in namespaces:
        if ns == EXCLUDED_NAMESPACE:
            print(f"[↷] Skipping excluded namespace: {ns}")
            continue
        for resource in RESOURCE_TYPES:
            save_resource_yaml(ns, resource)
    save_persistent_volumes()
