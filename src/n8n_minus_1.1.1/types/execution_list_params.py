# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Annotated, Literal

from .._utils import PropertyInfo

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo
from ..types import shared_params

__all__ = ["ExecutionListParams"]


class ExecutionListParams(TypedDict, total=False):
    cursor: str
    """
    Paginate by setting the cursor parameter to the nextCursor attribute returned by
    the previous request's response. Default value fetches the first "page" of the
    collection. See pagination for more detail.
    """

    include_data: Annotated[bool, PropertyInfo(alias="includeData")]
    """Whether or not to include the execution's detailed data."""

    limit: float
    """The maximum number of items to return."""

    status: Literal["error", "success", "waiting"]
    """Status to filter the executions by."""

    workflow_id: Annotated[str, PropertyInfo(alias="workflowId")]
    """Workflow to filter the executions by."""
