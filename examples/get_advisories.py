import getpass
from simple_nexus_dashboard import NexusDashboardClient
from pprint import pprint

nd = NexusDashboardClient("https://" + input("Nexus Dashboard IP:"), ssl_verify=False)

nd.login(input("Username:"), getpass.getpass("Password:"))
nd.nir.params["insightsGroupName"] = input("Site Groupname:")
nd.nir.params["aggr"] = "mnemonicTitle"

for item in nd.nir.telemetry.advisories.details.list_all().get("entries", []):
    pprint(item)
