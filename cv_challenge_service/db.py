import azure.cosmos.cosmos_client as cosmos_client
from . import config

HOST = config.settings['host']
MASTER_KEY = config.settings['master_key']

def __client() -> cosmos_client.CosmosClient:
    return  cosmos_client.CosmosClient(HOST, {'masterKey': MASTER_KEY})

def __get_visitor_item(container):
    return container.read_item(item="count", partition_key="p1")

def get_visitor_count():
    with __client() as c:
        db = c.get_database_client("cv")
        container = db.get_container_client("visitor")
        item = __get_visitor_item(container)
        return item.get("count", 0)

def update_visitor_count(by:int = 1):
     with __client() as c:
        db = c.get_database_client("cv")
        if by<1: 
            by = 1
        container = db.get_container_client("visitor")
    
        item = __get_visitor_item(container)
        item["count"] += 1
        container.upsert_item(body=item)
