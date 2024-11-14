import requests
from typing import List

from lib.constants import DEV_PQC_URL, OPPORTUNITY_NUMBER, USER_ID, TYPES_AND_SUBTYPES, SUBTYPE_DESCRIPTIONS, \
    TYPE_DESCRIPTIONS


def get_pqc_data(company_numbers: List[str], types_as_int=True):
    pqc_data = [
        ['CompanyNumber', 'Type', 'Subtype', 'Result']]
    for i, company_number in enumerate(company_numbers):
        try:
            if len(company_number) == 7:
                company_number = "0" + company_number
            if (i % 10) == 0:
                print(f"Fetching {i}/{len(company_numbers)}")
            response = requests.get(f"{DEV_PQC_URL}Pqc/{company_number}/{OPPORTUNITY_NUMBER}/{USER_ID}/true")
            json = response.json()
            pqc_data += get_pqc_response_data(json, types_as_int)
        except Exception as e:
            print(f"Error fetching data for company number {company_number}: {str(e)}")
    return pqc_data


def get_pqc_response_data(json, types_as_int: bool):
    company_number = json['company_number']
    adverse_flags = json['adverse_flags']

    return get_adverse_flags_response_data(company_number, adverse_flags, types_as_int)


def get_adverse_flags_response_data(company_number: str, adverse_flags: List, types_as_int: bool):
    adverse_flags_response_data = []
    for pqc_type, pqc_subtype in TYPES_AND_SUBTYPES:
        pqc_subtype_label = SUBTYPE_DESCRIPTIONS[pqc_type][pqc_subtype] if not types_as_int else pqc_subtype
        pqc_type_label = TYPE_DESCRIPTIONS[pqc_type] if not types_as_int else pqc_type
        adverse_flags_response_data.append([company_number, pqc_type_label, pqc_subtype_label, any(
            adverse_flag['type'] == pqc_type and any(
                pqc_subtype == subtype for subtype in adverse_flag['subtypes']) for adverse_flag in
            adverse_flags)])

    return adverse_flags_response_data
