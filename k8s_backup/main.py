# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from k8s_backup.services.manifest_backup import run_backup


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("🔄 Starting Kubernetes resource backup...")
    run_backup()
    print("✅ Backup completed.")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
