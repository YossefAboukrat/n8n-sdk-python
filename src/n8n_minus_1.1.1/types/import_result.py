# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from typing import Optional, List

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..types import shared
from typing import TYPE_CHECKING

__all__ = ["ImportResult", "Credential", "Tags", "TagsMapping", "TagsTag", "Variables", "Workflow"]


class Credential(BaseModel):
    id: Optional[str] = None

    name: Optional[str] = None

    type: Optional[str] = None


class TagsMapping(BaseModel):
    tag_id: Optional[str] = FieldInfo(alias="tagId", default=None)

    workflow_id: Optional[str] = FieldInfo(alias="workflowId", default=None)


class TagsTag(BaseModel):
    id: Optional[str] = None

    name: Optional[str] = None


class Tags(BaseModel):
    mappings: Optional[List[TagsMapping]] = None

    tags: Optional[List[TagsTag]] = None


class Variables(BaseModel):
    added: Optional[List[str]] = None

    changed: Optional[List[str]] = None


class Workflow(BaseModel):
    id: Optional[str] = None

    name: Optional[str] = None


class ImportResult(BaseModel):
    credentials: Optional[List[Credential]] = None

    tags: Optional[Tags] = None

    variables: Optional[Variables] = None

    workflows: Optional[List[Workflow]] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object:
            ...
