"""Create a trait pipeline."""

from traiter.pipeline import SpacyPipeline
from traiter.rule_matcher import RuleMatcher
from traiter.term_matcher import TermMatcher
from traiter.to_entities import ToEntities

from .body_part import BODY_PART
from .body_part_count import BODY_PART_COUNT
from .description import DESCRIPTION
from .length import LENGTH
from .max_width import MAX_WIDTH
from .numeric import NUMERIC
from .sci_name import SCI_NAME
from .seta_count import SETA_COUNT
from .size import SIZE
from ..pylib.consts import ATTACH_STEP, DESCRIPTION_STEP, GROUP_STEP, NUMERIC_STEP, \
    TERMS, TRAIT_STEP

MATCHERS = [
    BODY_PART, BODY_PART_COUNT, DESCRIPTION, LENGTH, MAX_WIDTH, NUMERIC,
    SCI_NAME, SETA_COUNT, SIZE]


class Pipeline(SpacyPipeline):
    """Build a custom traiter pipeline."""

    token2entity = {GROUP_STEP, TRAIT_STEP, ATTACH_STEP}
    entities2keep = {TRAIT_STEP, ATTACH_STEP, DESCRIPTION_STEP}

    def __init__(self):
        super().__init__()

        self.nlp.max_length *= 2
        self.nlp.disable_pipes(['ner'])

        TermMatcher.add_pipes(self.nlp, TERMS)
        RuleMatcher.add_pipe(self.nlp, MATCHERS, NUMERIC_STEP)
        RuleMatcher.add_pipe(self.nlp, MATCHERS, GROUP_STEP)
        RuleMatcher.add_pipe(self.nlp, MATCHERS, TRAIT_STEP)
        RuleMatcher.add_pipe(self.nlp, MATCHERS, ATTACH_STEP)
        RuleMatcher.add_pipe(self.nlp, MATCHERS, DESCRIPTION_STEP)
        ToEntities.add_pipe(self.nlp, self.entities2keep, self.token2entity)
