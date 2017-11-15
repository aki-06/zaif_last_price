import zaifapi
from zaifapi import *

if __name__ == '__main__':
    zaif = ZaifPublicApi()

    zaif_btc_jpy  = zaif.last_price(('btc_jpy'))
    zaif_xem_jpy  = zaif.last_price(('xem_jpy'))
    zaif_eth_jpy  = zaif.last_price(('eth_jpy'))
    zaif_mona_jpy = zaif.last_price(('mona_jpy'))
    zaif_bch_jpy  = zaif.last_price(('bch_jpy'))
    zaif_zaif_jpy = zaif.last_price(('zaif_jpy'))
    zaif_pepe_jpy = zaif.last_price(('pepecash_jpy'))

    print('btc_jpy  = ', zaif_btc_jpy['last_price'])
    print('xem_jpy  = ', zaif_xem_jpy['last_price'])
    print('eth_jpy  = ', zaif_eth_jpy['last_price'])
    print('mona_jpy = ', zaif_mona_jpy['last_price'])
    print('bch_jpy  = ', zaif_bch_jpy['last_price'])
    print('zaif_jpy = ', zaif_zaif_jpy['last_price'])
    print('pepe_jpy = ', zaif_pepe_jpy['last_price'])
