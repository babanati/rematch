import pytest

from utils import collector_types, model_types

from idaplugin.rematch.collectors import vectors, annotations
from idaplugin.rematch import instances
from collab.models import Vector, Annotation, Instance


pairs = [(vectors, Vector),
         (annotations, Annotation),
         (instances, Instance)]


@pytest.mark.parametrize('collector_module, model_class', pairs)
def test_definition(collector_module, model_class):
  collector_types_set = set(collector_types(collector_module))
  model_types_set = set(model_types(model_class))
  assert collector_types_set == model_types_set
