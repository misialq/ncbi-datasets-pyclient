# coding: utf-8

"""
    NCBI Datasets API

    ### NCBI Datasets is a resource that lets you easily gather data from NCBI. The Datasets version 2 API is still in alpha, and we're updating it often to add new functionality, iron out bugs and enhance usability. For some larger downloads, you may want to download a [dehydrated zip archive](https://www.ncbi.nlm.nih.gov/datasets/docs/v2/how-tos/genomes/large-download/), and retrieve the individual data files at a later time. 

    The version of the OpenAPI document: v2
    Contact: help@ncbi.nlm.nih.gov
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ncbi.datasets.openapi.models.v2reports_busco_stat import V2reportsBuscoStat
from ncbi.datasets.openapi.models.v2reports_feature_counts import V2reportsFeatureCounts
from typing import Optional, Set
from typing_extensions import Self

class V2reportsAnnotationInfo(BaseModel):
    """
    V2reportsAnnotationInfo
    """ # noqa: E501
    name: Optional[StrictStr] = None
    provider: Optional[StrictStr] = None
    release_date: Optional[StrictStr] = None
    report_url: Optional[StrictStr] = None
    stats: Optional[V2reportsFeatureCounts] = None
    busco: Optional[V2reportsBuscoStat] = None
    method: Optional[StrictStr] = None
    pipeline: Optional[StrictStr] = None
    software_version: Optional[StrictStr] = None
    status: Optional[StrictStr] = None
    release_version: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["name", "provider", "release_date", "report_url", "stats", "busco", "method", "pipeline", "software_version", "status", "release_version"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of V2reportsAnnotationInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of stats
        if self.stats:
            _dict['stats'] = self.stats.to_dict()
        # override the default output from pydantic by calling `to_dict()` of busco
        if self.busco:
            _dict['busco'] = self.busco.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V2reportsAnnotationInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "provider": obj.get("provider"),
            "release_date": obj.get("release_date"),
            "report_url": obj.get("report_url"),
            "stats": V2reportsFeatureCounts.from_dict(obj["stats"]) if obj.get("stats") is not None else None,
            "busco": V2reportsBuscoStat.from_dict(obj["busco"]) if obj.get("busco") is not None else None,
            "method": obj.get("method"),
            "pipeline": obj.get("pipeline"),
            "software_version": obj.get("software_version"),
            "status": obj.get("status"),
            "release_version": obj.get("release_version")
        })
        return _obj


