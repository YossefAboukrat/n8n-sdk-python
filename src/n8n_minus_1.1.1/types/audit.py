# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..types import shared

__all__ = ["Audit"]


class Audit(BaseModel):
    credentials_risk_report: Optional[object] = FieldInfo(alias="Credentials Risk Report", default=None)

    database_risk_report: Optional[object] = FieldInfo(alias="Database Risk Report", default=None)

    filesystem_risk_report: Optional[object] = FieldInfo(alias="Filesystem Risk Report", default=None)

    instance_risk_report: Optional[object] = FieldInfo(alias="Instance Risk Report", default=None)

    nodes_risk_report: Optional[object] = FieldInfo(alias="Nodes Risk Report", default=None)
