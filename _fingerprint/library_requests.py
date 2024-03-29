import requests
import json
import pickle

URL = "http://192.168.43.12:5002/api/smartlock/"


class ApiFingerprint(object):
    id = 0
    digital = ""

    def __init__(self, _id, _digital):
        self.id = _id

        print("id: {0} ".format(str(type(_id))))
        print("digital: {0} ".format(str(type(_digital))))

        if isinstance(_digital, str):
            self.digital = _digital

        elif isinstance(_digital, list):
            for bit in _digital:
                self.digital = self.digital + str(bit) + "|"
        else:
            raise Exception("_characteristics argument must be a str or a list.")


def envia_digital_api(_ApiFingerprint):
    result = False
    # print(_ApiFingerprint.id)
    # print(_ApiFingerprint.digital)

    if ((_ApiFingerprint.idUsuario == 0) or (_ApiFingerprint.digital == "")):
        raise Exception("Invalid object for request")
    else:
        print(json.dumps(_ApiFingerprint.__dict__))
        response = requests.post(
            url=URL + "inserirdigital",
            data=json.dumps(_ApiFingerprint.__dict__),
            headers={"Content-Type": "application/json"}
        )
        result = response.status_code == 200
    return result


def recebe_digitais_api():
    result = []
    # print(URL)
    response = requests.get(url=URL + "obterdigitais")
    # print(str(response.status_code))
    if response.status_code == 200:
        result = response.json()
    return result