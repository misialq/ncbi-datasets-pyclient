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

from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ncbi.datasets.openapi.models.v2_gene_dataset_reports_request_content_type import V2GeneDatasetReportsRequestContentType
from ncbi.datasets.openapi.models.v2_gene_dataset_reports_request_symbols_for_taxon import V2GeneDatasetReportsRequestSymbolsForTaxon
from ncbi.datasets.openapi.models.v2_gene_type import V2GeneType
from ncbi.datasets.openapi.models.v2_include_tabular_header import V2IncludeTabularHeader
from typing import Optional, Set
from typing_extensions import Self

class V2GeneDatasetReportsRequest(BaseModel):
    """
    V2GeneDatasetReportsRequest
    """ # noqa: E501
    returned_content: Optional[V2GeneDatasetReportsRequestContentType] = None
    gene_ids: Optional[List[StrictInt]] = None
    accessions: Optional[List[StrictStr]] = None
    symbols_for_taxon: Optional[V2GeneDatasetReportsRequestSymbolsForTaxon] = None
    taxon: Optional[StrictStr] = None
    locus_tags: Optional[List[StrictStr]] = None
    table_fields: Optional[List[StrictStr]] = None
    table_format: Optional[StrictStr] = None
    include_tabular_header: Optional[V2IncludeTabularHeader] = None
    page_size: Optional[StrictInt] = None
    page_token: Optional[StrictStr] = None
    query: Optional[StrictStr] = None
    types: Optional[List[V2GeneType]] = None
    accession_filter: Optional[List[StrictStr]] = None
    __properties: ClassVar[List[str]] = ["returned_content", "gene_ids", "accessions", "symbols_for_taxon", "taxon", "locus_tags", "table_fields", "table_format", "include_tabular_header", "page_size", "page_token", "query", "types", "accession_filter"]

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
        """Create an instance of V2GeneDatasetReportsRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of symbols_for_taxon
        if self.symbols_for_taxon:
            _dict['symbols_for_taxon'] = self.symbols_for_taxon.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V2GeneDatasetReportsRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "returned_content": obj.get("returned_content"),
            "gene_ids": obj.get("gene_ids"),
            "accessions": obj.get("accessions"),
            "symbols_for_taxon": V2GeneDatasetReportsRequestSymbolsForTaxon.from_dict(obj["symbols_for_taxon"]) if obj.get("symbols_for_taxon") is not None else None,
            "taxon": obj.get("taxon"),
            "locus_tags": obj.get("locus_tags"),
            "table_fields": obj.get("table_fields"),
            "table_format": obj.get("table_format"),
            "include_tabular_header": obj.get("include_tabular_header"),
            "page_size": obj.get("page_size"),
            "page_token": obj.get("page_token"),
            "query": obj.get("query"),
            "types": obj.get("types"),
            "accession_filter": obj.get("accession_filter")
        })
        return _obj


