import ipfshttpclient

import dataset

test_hash = 'bafybeic7qbuo2ail2y5urbm5btfp7dwcxigjs4kq6m36ecbozaurt4z3te'

client = ipfshttpclient.connect()

data = dataset.IPFSGeneralDataset(client, 'data', [test_hash])

#dataset.IPFSGeneralDataset(client, '', [test_hash])