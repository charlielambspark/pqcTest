import requests

from typing import List

DEV_PQC_URL = 'https://dev-pre-qualification-check-api.clover-technology.co.uk:6443/'
OPPORTUNITY_NUMBER = '223'
USER_ID = '1000877'

TYPES_AND_SUBTYPES = [[1, 1], [1, 2], [1, 3], [2, 1], [2, 2], [2, 3], [2, 4], [2, 5], [3, 1], [3, 2], [3, 3], [3, 4],
                      [3, 5], [3, 6], [4, 1], [4, 2], [4, 3], [5, 1], [5, 2], [5, 3], [5, 4]]
TYPE_DESCRIPTIONS = {1: 'Associated Business', 2: 'Business', 3: 'Director', 4: 'Psc', 5: 'Financials'}
SUBTYPE_DESCRIPTIONS = {
    1: {
        1: 'Associated Business Insolvency',
        2: 'HM Court Data',
        3: 'Charges on other businesses',
    },
    2: {
        1: 'CCJ (Business)',
        2: 'Director resignations',
        3: 'Accounts Overdue',
        4: 'Incorporation Date',
        5: 'Adverse SIC Code',
    },
    3: {
        1: 'Director bankruptcy',
        2: 'Director disqualifications',
        3: 'Director country of residence',
        4: 'Director nationality',
        5: 'Director average age',
        6: 'Director Personal Insolvency',
    },
    4: {
        1: 'UBO nationality',
        2: 'UBO is overseas company?',
        3: 'Recent ownership changes',
    },
    5: {
        1: 'Negative Audit report',
        2: 'Negative Balance Sheet',
        3: 'Estimated Losses',
        4: 'Substantial Debts',
    }
}


def get_pqc_data(company_numbers: List[str], types_as_int=True):
    pqc_data = [
        ['CompanyNumber', 'Type', 'Subtype', 'Result']]
    for company_number in company_numbers:
        response = requests.get(f"{DEV_PQC_URL}Pqc/{company_number}/{OPPORTUNITY_NUMBER}/{USER_ID}")
        json = response.json()
        pqc_data += get_pqc_response_data(json, types_as_int)
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
                adverse['sub_type'] == pqc_subtype for adverse in adverse_flag['data']) for adverse_flag in
            adverse_flags)])

    return adverse_flags_response_data
