# Locally group and count records by the first byte in their key
gb = GB()
gb.localgroupby(lambda x: x['key'][:1],
                lambda k, a, r: (a if a else 0) + 1)
gb.run()
