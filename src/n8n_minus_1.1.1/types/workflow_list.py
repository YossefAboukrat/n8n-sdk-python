# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from typing import Optional, List

from .workflow import Workflow

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..types import shared

__all__ = ["WorkflowList"]


class WorkflowList(BaseModel):
    data: Optional[List[Workflow]] = None

    next_cursor: Optional[str] = FieldInfo(alias="nextCursor", default=None)
    """
    Paginate through workflows by setting the cursor parameter to a nextCursor
    attribute returned by a previous request. Default value fetches the first "page"
    of the collection.
    """
