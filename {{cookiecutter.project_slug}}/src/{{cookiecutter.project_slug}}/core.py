"""Main module. If include_dataclasses_scaffolding is enabled, you will see Data Class scaffolding here"""

{%- if cookiecutter.include_dataclasses_scaffolding == 'y' %}
from dataclasses import dataclass
from datetime import datetime

from {{ cookiecutter.project_slug }}.utils import (default_field, now)

@dataclass
class BaseExample:
    """
    The BaseExample object. Contains helper functions and generalized metadata
    """
    run_time: datetime = default_field(now(), init=False, repr=False)
{%- endif %}

