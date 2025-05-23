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

from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ncbi.datasets.openapi.models.v2_assembly_dataset_descriptors_filter import V2AssemblyDatasetDescriptorsFilter
from ncbi.datasets.openapi.models.v2_assembly_dataset_reports_request_content_type import V2AssemblyDatasetReportsRequestContentType
from ncbi.datasets.openapi.models.v2_include_tabular_header import V2IncludeTabularHeader
from ncbi.datasets.openapi.models.v2_sort_field import V2SortField
from typing import Optional, Set
from typing_extensions import Self

class V2AssemblyDatasetReportsRequest(BaseModel):
    """
    V2AssemblyDatasetReportsRequest
    """ # noqa: E501
    taxons: Optional[List[StrictStr]] = None
    bioprojects: Optional[List[StrictStr]] = None
    biosample_ids: Optional[List[StrictStr]] = None
    assembly_names: Optional[List[StrictStr]] = None
    wgs_accessions: Optional[List[StrictStr]] = None
    accessions: Optional[List[StrictStr]] = None
    filters: Optional[V2AssemblyDatasetDescriptorsFilter] = None
    tax_exact_match: Optional[StrictBool] = None
    chromosomes: Optional[List[StrictStr]] = None
    table_fields: Optional[List[StrictStr]] = None
    returned_content: Optional[V2AssemblyDatasetReportsRequestContentType] = None
    page_size: Optional[StrictInt] = None
    page_token: Optional[StrictStr] = None
    sort: Optional[List[V2SortField]] = None
    include_tabular_header: Optional[V2IncludeTabularHeader] = None
    table_format: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["taxons", "bioprojects", "biosample_ids", "assembly_names", "wgs_accessions", "accessions", "filters", "tax_exact_match", "chromosomes", "table_fields", "returned_content", "page_size", "page_token", "sort", "include_tabular_header", "table_format"]

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
        """Create an instance of V2AssemblyDatasetReportsRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of filters
        if self.filters:
            _dict['filters'] = self.filters.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in sort (list)
        _items = []
        if self.sort:
            for _item_sort in self.sort:
                if _item_sort:
                    _items.append(_item_sort.to_dict())
            _dict['sort'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V2AssemblyDatasetReportsRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "taxons": obj.get("taxons"),
            "bioprojects": obj.get("bioprojects"),
            "biosample_ids": obj.get("biosample_ids"),
            "assembly_names": obj.get("assembly_names"),
            "wgs_accessions": obj.get("wgs_accessions"),
            "accessions": obj.get("accessions"),
            "filters": V2AssemblyDatasetDescriptorsFilter.from_dict(obj["filters"]) if obj.get("filters") is not None else None,
            "tax_exact_match": obj.get("tax_exact_match"),
            "chromosomes": obj.get("chromosomes"),
            "table_fields": obj.get("table_fields"),
            "returned_content": obj.get("returned_content"),
            "page_size": obj.get("page_size"),
            "page_token": obj.get("page_token"),
            "sort": [V2SortField.from_dict(_item) for _item in obj["sort"]] if obj.get("sort") is not None else None,
            "include_tabular_header": obj.get("include_tabular_header"),
            "table_format": obj.get("table_format")
        })
        return _obj


