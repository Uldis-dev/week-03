def check_guess(minejums, merkis):
    """
    Salīdzina minējumu ar mērķi un atgriež rezultāta kodu.
    """
    if minejums < merkis:
        return "too_small"
    elif minejums > merkis:
        return "too_large"
    return "correct"

def get_status_message(result):
    """
    Pārvērš loģisko rezultātu cilvēkam saprotamā tekstā.
    """
    messages = {
        "too_small": "Par mazu!",
        "too_large": "Par lielu!",
        "correct": "Apsveicu! Tu uzminēji!"
    }
    return messages.get(result, "")