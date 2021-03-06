"""Reviews a checklist to find changes made by reviewers."""

# Copyright (c) 2019 Guy Babineau

# These codes were developed by trial and error as I did not find them documented
# there is a certainty that some are missing

from ebird.api import get_checklist


auxcode_translation = {
                        'FO': {'C value': 'C1', 'readable': 'F Flyover (Observed)'},
                        'OS': {'C value': 'C2', 'readable': 'H In Appropriate Habitat (Possible)'},
                        'S1': {'C value': 'C2', 'readable': 'S Singing Male (Possible)'},
                        'S7': {'C value': 'C3', 'readable': 'S7 Singing Male Present 7+ days (Probable)'},
                        'PO': {'C value': 'C3', 'readable': 'P Pair in Suitable Habitat (Probable)'},
                        'AB': {'C value': 'C3', 'readable': 'A Agitated Behavior (Probable)'},
                        'T7': {'C value': 'C3', 'readable': 'T Territorial Defense (Probable)'},
                        'CC': {'C value': 'C3', 'readable': 'C Courtship, Display, or Copulation (Probable)'},
                        'VS': {'C value': 'C3', 'readable': 'N Visiting Probable Nest Site (Probable)'},
                        'NB': {'C value': 'C4', 'readable': 'NB Nest Building (Confirmed)'},
                        'CM': {'C value': 'C4', 'readable': 'CN Carrying Nesting Material (Confirmed)'},
                        'FY': {'C value': 'C4', 'readable': 'CF Carrying Food (Confirmed)'},
                        'UN': {'C value': 'C4', 'readable': 'UN Used Nest (enter 0 if no birds seen) (Confirmed)'},
                        'ON': {'C value': 'C4', 'readable': 'ON Occupied Nest (Confirmed)'},
                        'FL': {'C value': 'C4', 'readable': 'FL Recently Fledged Young (Confirmed)'},
                        'FR': {'C value': 'C4', 'readable': 'FY Feeding Young (Confirmed)'},
                        'NE': {'C value': 'C4', 'readable': 'NE Nest with Eggs (Confirmed)'},
                        'NY': {'C value': 'C4', 'readable': 'NY Nest with Young (Confirmed)'}
                        }


def review_checklist(ebird_api_key, checklist_name):
    """Looks at a single checklist for species and codes of interest

    According to eBird, this API should not be abused so limit calls to this function

    Args
        ebird_api_key : access key from eBird tied to account
        checklist_name : name of the checklist in eBird - e.g. S35636314

    Returns:
        NA - prints to stdout

    Raises:
        NA - but can exit on failure to retrieve data
    """
    checklist = get_checklist(ebird_api_key, checklist_name)
    search_species = {"dowwoo","haiwoo","pilwoo","rehwoo", "rebwoo"}
    search_code = {"CC"}

    observations = checklist['obs']
    for observation_dict in observations:
        # only look at entries with breeding codes
        if 'obsAux' in observation_dict:
            # only look at species of interest
            species=observation_dict['speciesCode']
            if species in search_species:
                aux_dict = observation_dict['obsAux'][0]
                entered_code = aux_dict['auxCode']
                if entered_code in search_code:
                    print(observation_dict['speciesCode'], ' Used a ',auxcode_translation[entered_code]['readable'])
                    if 'comments' in observation_dict:
                        print( ' comments:',observation_dict['comments'])


