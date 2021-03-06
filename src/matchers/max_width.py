"""Get maximum width notations."""

from ..pylib.consts import ATTACH_STEP


def max_width(span):
    """Enrich the match."""
    data = {}

    for token in span:
        label = token.ent_type_

        if label == 'body_part':
            data['part'] = token.text

        elif label == 'size':
            data = {**data, **token._.data}

    return data


MAXIMUM = """ maximum max """.split()
WIDTH = """ width """.split()

MAX_WIDTH = {
    ATTACH_STEP: [
        {
            'label': 'max_width',
            'on_match': max_width,
            'patterns': [
                [
                    {'LOWER': {'IN': MAXIMUM}},
                    {'ENT_TYPE': 'body_part'},
                    {'LOWER': {'IN': WIDTH}},
                    {'ENT_TYPE': '', 'OP': '?'},
                    {'ENT_TYPE': '', 'OP': '?'},
                    {'ENT_TYPE': 'size'},
                ],
            ],
        }
    ]
}
