import os
from dotenv import load_dotenv
load_dotenv()
from lib.ngsildclient.Client import Client

# Ngsi-ld broker client
client = Client()

# Fetch all WasteContainer entities
context = os.environ.get("WASTECONTAINERS_CONTEXT")
containers = client.get_all_entities_by_type("WasteContainer", context).json()

print(containers)