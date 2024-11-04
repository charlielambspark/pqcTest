import requests

from typing import List

DEV_PQC_URL = 'https://dev-pre-qualification-check-api.clover-technology.co.uk:6443/'
OPPORTUNITY_NUMBER = '223'
USER_ID = '1000877'

TYPES_AND_SUBTYPES =[[1, 1], [1, 2], [1, 3], [2, 1], [2, 2], [2, 3], [2, 4], [2, 5], [3, 1], [3, 2], [3, 3], [3, 4], [3, 5], [3, 6], [4, 1], [4, 2], [4, 3], [5, 1], [5, 2], [5, 3], [5, 4]]

def get_pqc_data(company_numbers: List[str]):
    pqc_data = [['CompanyNumber','1.1','1.2','1.3','2.1','2.2','2.3','2.4','2.5','3.1','3.2','3.3','3.4','3.5','3.6','4.1','4.2','4.3','5.1','5.2','5.3','5.4']]
    for company_number in company_numbers:
        response = requests.get(f"{DEV_PQC_URL}Pqc/{company_number}/{OPPORTUNITY_NUMBER}/{USER_ID}")
        json = response.json()
        pqc_data.append(get_pqc_response_data(json))
    return pqc_data

def get_pqc_response_data(json):
    company_number = json['company_number']
    adverse_flags = json['adverse_flags']

    return [company_number] + get_adverse_flags_response_data(adverse_flags)
def get_adverse_flags_response_data(adverse_flags : List):
    adverse_flags_response_data = []
    for type_and_subtype in TYPES_AND_SUBTYPES:
        adverse_flags_response_data.append(any(adverse_flag['type'] == type_and_subtype[0] and any(adverse['sub_type'] == type_and_subtype[1] for adverse in adverse_flag['data']) for adverse_flag in adverse_flags))


    return adverse_flags_response_data