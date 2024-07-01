# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Annotated, Literal

from .._utils import PropertyInfo

from typing import List

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo
from ..types import shared_params

__all__ = ["AuditGenerateParams", "AdditionalOptions"]


class AuditGenerateParams(TypedDict, total=False):
    additional_options: Annotated[AdditionalOptions, PropertyInfo(alias="additionalOptions")]


class AdditionalOptions(TypedDict, total=False):
    categories: List[Literal["credentials", "database", "nodes", "filesystem", "instance"]]

    days_abandoned_workflow: Annotated[int, PropertyInfo(alias="daysAbandonedWorkflow")]
    """Days for a workflow to be considered abandoned if not executed"""
