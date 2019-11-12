import requests
import json
import pickle

URL = "http://192.168.43.12:5002/api/smartlock/"


class ApiFingerprint(object):
    IdUsuario = 0
    Digital = ""

    def __init__(self, _IdUsuario, _Digital):
        self.IdUsuario = _IdUsuario

        if isinstance(_Digital, str):
            self.Digital = _Digital

        elif isinstance(_Digital, list):
            for bit in _Digital:
                self.Digital = self.Digital + str(bit) + "|"
        else:
            raise Exception("_characteristics argument must be a str or a list.")


def envia_digital_api(_ApiFingerprint):
    result = False
    print(_ApiFingerprint.IdUsuario)
    print(_ApiFingerprint.Digital)

    if ((_ApiFingerprint.IdUsuario == 0) or (_ApiFingerprint.Digital == "")):
        raise Exception("Invalid object for request")
    else:
        print(pickle.dumps(_ApiFingerprint))
        response = requests.post(
            url = URL + "inserirdigital",
            json = pickle.dumps(_ApiFingerprint)
        )
        result = response.status_code == 200
    return result


def recebe_digitais_api():
    result = []
    print(URL)
    response = requests.get(url=URL + "obterdigitais")
    print(str(response.status_code))
    if response.status_code == 200:
        result = response.json()
        print(json.dumps(result, sort_keys=True, indent=4))
    return result