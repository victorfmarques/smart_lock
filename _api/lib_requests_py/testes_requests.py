import library_requests

print("INSTANCIA CLASSE")
api = library_requests.ApiFingerprint(1,"digital")
print("CLASSE INSTANCIADA")

print("EXECUCAO RECEBE_DIGITAIS_API")
api.recebe_digitais_api()
print("EXECUTOU RECEBE_DIGITAIS_API")