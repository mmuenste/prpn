"""Ein Modul, das bestimmte Anwendungen auf den ONOS SDN-Controller aktiviert.
"""

import requests
from getpass import getpass
import sys

def activate_apps(username, password):
    """Aktiviere folgende Anwendungen.
    """
    app_names = ["hostprovider",
                 "lldpprovider",
                 "openflow-base",
                 "optical-model",
                 "proxyarp"]
    
    for app in app_names:
        url = f"http://localhost:8181/onos/v1/applications/org.onosproject.{app}/active"
        response = requests.post(url, auth=(username, password))
        #response.raise_for_status()
        print(f"Anwendung {app} Status: {response.status_code}")

def main():

    user = input("Username: ")
    password = getpass()
    activate_apps(user, password)

    return 0

if __name__ == "__main__":
    sys.exit(main())
