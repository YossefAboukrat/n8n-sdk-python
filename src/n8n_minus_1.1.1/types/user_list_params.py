# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Annotated

from .._utils import PropertyInfo

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo
from ..types import shared_params

__all__ = ["UserListParams"]


class UserListParams(TypedDict, total=False):
    cursor: str
    """
    Paginate by setting the cursor parameter to the nextCursor attribute returned by
    the previous request's response. Default value fetches the first "page" of the
    collection. See pagination for more detail.
    """

    include_role: Annotated[bool, PropertyInfo(alias="includeRole")]
    """Whether to include the user's role or not."""

    limit: float
    """The maximum number of items to return."""
