# Script for fetching security object from EMP

from kmip.pie import client
c = client.ProxyKmipClient(config_file="<path to pykmip.conf file>")
with c:
    key = c.get('<UUID of security object from EMP>')
    print(key)
