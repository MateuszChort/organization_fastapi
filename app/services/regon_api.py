from RegonAPI import RegonAPI


def nip_search(nip: int):
    api = RegonAPI(bir_version="bir1.1", is_production=True)
    api.authenticate(key="YOUR_API_KEY")
    return api.searchData(nip=str(nip))
