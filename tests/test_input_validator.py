import yaml
from dm.utils.input_validator import InputValidator


def test_validator_intent_and_entity_ok():
    validator = InputValidator('test_input_validator_rules.yaml')
    previous = "utter_garantie_type_bien"
    parse_data = {
        'intent': {'name': 'garantie'},
        'entities': [{'entity': 'product_type'}]
    }
    assert validator._get_error(parse_data, previous) is None


def test_validator_dummy_valid():

    validator = InputValidator('test_input_validator_rules.yaml')
    previous = "not_in_file"
    parse_data = {
        'intent': {'name': 'affirm'},
        'entities': []
    }
    assert validator._get_error(parse_data, previous) is None


def test_validator_intent_no_entity():
    validator = InputValidator('test_input_validator_rules.yaml')
    previous = "utter_garantie_type_bien"
    parse_data = {
        'intent': {'name': 'cancel'},
        'entities': []
    }
    assert validator._get_error(parse_data, previous) is None


def test_validator_entity_not_in_expected():
    validator = InputValidator('test_input_validator_rules.yaml')

    previous = "utter_garantie_type_bien"
    parse_data = {
        'intent': {'name': 'cancel'},
        'entities': [{'entity': 'product_type'}]
    }
    assert validator._get_error(parse_data, previous) is None


def test_validator_regex():
    validator = InputValidator('test_input_validator_rules.yaml')

    previous = "utter_garantie_confirm_particulier"
    parse_data = {
        'intent': {'name': 'cancel'},
        'entities': [{'entity': 'product_type'}]
    }
    # having an entity in parse_data that is not expected is ok
    assert validator._get_error(parse_data, previous) is None

    previous = "utter_garantie_confirm_particulier"
    parse_data = {
        'intent': {'name': 'cancel'},
        'entities': []
    }
    assert validator._get_error(parse_data, previous) is None

    previous = "utter_garantie_confirm_particulier"
    parse_data = {
        'intent': {'name': 'lakjshdflkjashdf'},
        'entities': []
    }
    assert validator._get_error(parse_data, previous) == 'utter_general_validation_affirm_deny'


def test_validator_intent_ok_entity_missing():
    validator = InputValidator('test_input_validator_rules.yaml')
    previous = "utter_garantie_type_bien"
    parse_data = {
        'intent': {'name': 'garantie'},
        'entities': []
    }
    assert validator._get_error(parse_data, previous) == 'utter_general_validation_options'
