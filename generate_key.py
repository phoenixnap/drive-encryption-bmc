# Import libraries

from kmip.pie import client
from kmip import enums

# Establish connection

c = client.ProxyKmipClient(config_file="<path to conf file>")

# Create key

with c:
    key_id = c.create(
        enums.CryptographicAlgorithm.AES,
        256,
        name='<key name>',
        cryptographic_usage_mask=[
            enums.CryptographicUsageMask.ENCRYPT,
            enums.CryptographicUsageMask.DECRYPT
        ]
    )

# Activate key

    c.activate(key_id)
  
# Get key

    key = c.get(key_id)
    #print(key)
