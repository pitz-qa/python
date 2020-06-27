import arrow
import jwt
import requests

JWT_BEARER_URI = 'urn:ietf:params:oauth:grant-type:jwt-bearer'


def get_token(client_id, client_secret, scope, endpoint, audience):
    claim = {
        'iss': client_id,
        'aud': audience,
        'exp': arrow.utcnow().shift(months=3).timestamp,
        'scope': scope,
    }
    # print(claim)
    # jwt = JWT()
    assertion = jwt.encode(claim, client_secret, algorithm='HS256')
    params = {
        'assertion': assertion,
        'grant_type': JWT_BEARER_URI
    }
    # params = {
    #     'assertion': "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiIxNjQ3NTBkMS0wNWQ5LTRjZDEtYWI0NS01YjY4MGU2Njk3ZjkiLCJhdWQiOiJodHRwczovL2FwaS53ZWxraW5oZWFsdGguY29tL3YxL3Rva2VuIiwiZXhwIjoxNTk3NTAyMjI1LCJzY29wZSI6ImFsbCJ9.tZN1OGh8yIUXsYb0NSb8Nni5H4mN99E1Cx6pxPoUaFM",
    #     'grant_type': JWT_BEARER_URI
    # }

    print(params)
    resp = requests.post(endpoint, data=params)
    # print(params)
    # print("resp", resp.json())
    if 'errors' in resp.json():
        print("ERROORORORO")
        token = resp.json()
    else:
        token = resp.json()['access_token']
    return token


token = get_token('164750d1-05d9-4cd1-ab45-5b680e6697f9',
                  '87425a6a-ec4f-4b52-8ce9-3ec505e0003d',
                  'all',
                  #   'custom_data_type_records.read custom_data_type_records.write',
                  'https://api.welkinhealth.com/v1/token',
                  'https://api.welkinhealth.com/v1/token')
print("\n\n\n Token for Welkin APIs is : ", token)
