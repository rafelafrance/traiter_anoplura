"""Get body length notations."""


def body_length(span):
    """Enrich the match."""
    data = {}

    for token in span:
        label = token.ent_type_

        if label == 'size':
            data = {**data, **token._.data}

    return data


LENGTH = """ length len """.split()


BODY_LENGTH = {
    'name': 'body_length',
    'attachers': [
        {
            'label': 'body_length',
            'on_match': body_length,
            'patterns': [
                [
                    {'LOWER': 'total', 'OP': '?'},
                    {'LOWER': 'body'},
                    {'LOWER': {'IN': LENGTH}},
                    {'ENT_TYPE': '', 'OP': '?'},
                    {'ENT_TYPE': '', 'OP': '?'},
                    {'ENT_TYPE': 'size'},
                ],
            ],
        }
    ]
}
