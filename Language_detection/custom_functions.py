# For getting full name
from pycountry import languages

def detect_language_properties_from_predictions(value):
    # Get language code
    lang_code = value[0][0][9:]

    # Get prediction confidence
    confidence = value[1][0]

    return (lang_code,confidence)

def detect_language_from_code(code):
    # Get language full name
    lang_name_full = languages.get(alpha_2=code).name
    print(lang_name_full)
    return lang_name_full
