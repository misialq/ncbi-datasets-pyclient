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
from ncbi.datasets.openapi.models.v2reports_error import V2reportsError
from ncbi.datasets.openapi.models.v2reports_gene_descriptor import V2reportsGeneDescriptor
from ncbi.datasets.openapi.models.v2reports_product_descriptor import V2reportsProductDescriptor
from ncbi.datasets.openapi.models.v2reports_warning import V2reportsWarning
from typing import Optional, Set
from typing_extensions import Self

class V2reportsGeneReportMatch(BaseModel):
    """
    V2reportsGeneReportMatch
    """ # noqa: E501
    gene: Optional[V2reportsGeneDescriptor] = None
    product: Optional[V2reportsProductDescriptor] = None
    query: Optional[List[StrictStr]] = None
    warnings: Optional[List[V2reportsWarning]] = None
    warning: Optional[V2reportsWarning] = None
    errors: Optional[List[V2reportsError]] = None
    __properties: ClassVar[List[str]] = ["gene", "product", "query", "warnings", "warning", "errors"]

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
        """Create an instance of V2reportsGeneReportMatch from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of gene
        if self.gene:
            _dict['gene'] = self.gene.to_dict()
        # override the default output from pydantic by calling `to_dict()` of product
        if self.product:
            _dict['product'] = self.product.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in warnings (list)
        _items = []
        if self.warnings:
            for _item_warnings in self.warnings:
                if _item_warnings:
                    _items.append(_item_warnings.to_dict())
            _dict['warnings'] = _items
        # override the default output from pydantic by calling `to_dict()` of warning
        if self.warning:
            _dict['warning'] = self.warning.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in errors (list)
        _items = []
        if self.errors:
            for _item_errors in self.errors:
                if _item_errors:
                    _items.append(_item_errors.to_dict())
            _dict['errors'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V2reportsGeneReportMatch from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "gene": V2reportsGeneDescriptor.from_dict(obj["gene"]) if obj.get("gene") is not None else None,
            "product": V2reportsProductDescriptor.from_dict(obj["product"]) if obj.get("product") is not None else None,
            "query": obj.get("query"),
            "warnings": [V2reportsWarning.from_dict(_item) for _item in obj["warnings"]] if obj.get("warnings") is not None else None,
            "warning": V2reportsWarning.from_dict(obj["warning"]) if obj.get("warning") is not None else None,
            "errors": [V2reportsError.from_dict(_item) for _item in obj["errors"]] if obj.get("errors") is not None else None
        })
        return _obj


