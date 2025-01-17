intent_map = {
    'new_issue': {'drug': ['uses'],
                'lab': ['What_is_the_test']},
    'what_is': {'drug': ['uses'],
                'lab': ['What_is_the_test']},
    'usage': {'drug': ['uses'],
              'lab': ['What_is_it_used_for', 'Why_do_I_need_the_test']},
    'risk': {'drug': ['warnings', 'side_effects'],
             'lab': ['Are_there_any_risks_to_the_test']},
    'lab_result': {'lab': ['What_do_the_results_mean']},
    'lab_prepare': {'lab': ['Will_I_need_to_do_anything_to_prepare_for_the_test']},
    'lab_during': {'lab': ['What_happens_during_the_test']},
    'drug_warning': {'drug': ['warnings']},
    'drug_dosage': {'drug': ['dosage']},
    'drug_interaction': {'drug': ['interactions']},
    'drug_sideeffects': {'drug': ['side_effects']},
}

def get_columns(intent, table):
    if table in intent_map[intent].keys():
        return intent_map[intent][table]
    else:
        return []