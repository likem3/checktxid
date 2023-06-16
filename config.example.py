BASE_URL = "https://apilist.tronscanapi.com/api/transaction-info"
APIKEY = "apikeyhere"

PENDING_PREFIX = "pending"
CONFIRM_SUFFIX = "confirmed"

AFFECTED_TABLE = "txid_table"
TXID_FIELD = "txid"
STATUS_PAYMENT = "status"

DB_CONFIG = {
    'default': 'mysql',
    'mysql':{
        'driver': 'mysql',
        'host': 'localhost',
        'database': 'dbname',
        'user': 'root',
        'password': '',
        'prefix': ''
    }
}