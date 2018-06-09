import inspect


def collector_types(module):
  for _, obj in inspect.getmembers(module):
    if inspect.isclass(obj) and hasattr(obj, 'type'):
      yield obj.type


def model_types(model):
  for type_name, text in model.TYPE_CHOICES:
    yield type_name
