from os import environ

settings = {
    'host': environ.get('CosmosDbHost'),
    'master_key': environ.get('CosmosDbKey'),
}