import requests
from config import BASE_URL, APIKEY, CONFIRM_SUFFIX, PENDING_PREFIX, DB_CONFIG, AFFECTED_TABLE, STATUS_PAYMENT, TXID_FIELD
from orator import DatabaseManager
import time

class Main:
    txids = None

    def __init__(self):
        self.db = DatabaseManager(DB_CONFIG)
        self.def_get_pending_transaction()

    def def_get_pending_transaction(self):
        self.txids = self.db.table(AFFECTED_TABLE) \
            .where(STATUS_PAYMENT, PENDING_PREFIX)\
            .limit(100).lists(TXID_FIELD)
        
    def update_confirm(self, txid):
        self.db.table(AFFECTED_TABLE) \
            .where(TXID_FIELD, txid) \
            .update(status=CONFIRM_SUFFIX)
        print("{} : {}".format(txid, "updated"))
        
    def check_trx(self, txid, response={}):
        if response.get('contractRet') == "SUCCESS" and response.get('confirmed', False):
            print("{} : {}".format(txid, CONFIRM_SUFFIX))
            self.update_confirm(txid)
        else:
            print("{} : {}".format(txid, "not confirmed"))
        
    def execute(self):
        for txid in self.txids:
            url = BASE_URL 
            params = {"hash" : txid}
            headers = {
                "TRON-PRO-API-KEY" : APIKEY
            }
            resp = requests.get(url, headers=headers, params=params)
            self.check_trx(txid, resp.json())            
            time.sleep(1/3)

if __name__ == "__main__":
    m = Main()
    m.execute()