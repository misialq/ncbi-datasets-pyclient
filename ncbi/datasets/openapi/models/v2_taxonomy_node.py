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
from ncbi.datasets.openapi.models.v2_taxonomy_node_count_by_type import V2TaxonomyNodeCountByType
from ncbi.datasets.openapi.models.v2reports_rank_type import V2reportsRankType
from typing import Optional, Set
from typing_extensions import Self

class V2TaxonomyNode(BaseModel):
    """
    V2TaxonomyNode
    """ # noqa: E501
    tax_id: Optional[StrictInt] = None
    organism_name: Optional[StrictStr] = None
    common_name: Optional[StrictStr] = None
    genbank_common_name: Optional[StrictStr] = None
    acronyms: Optional[List[StrictStr]] = None
    genbank_acronym: Optional[StrictStr] = None
    blast_name: Optional[StrictStr] = None
    lineage: Optional[List[StrictInt]] = None
    children: Optional[List[StrictInt]] = None
    descendent_with_described_species_names_count: Optional[StrictInt] = None
    rank: Optional[V2reportsRankType] = None
    has_described_species_name: Optional[StrictBool] = None
    counts: Optional[List[V2TaxonomyNodeCountByType]] = None
    min_ord: Optional[StrictInt] = None
    max_ord: Optional[StrictInt] = None
    extinct: Optional[StrictBool] = None
    genomic_moltype: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["tax_id", "organism_name", "common_name", "genbank_common_name", "acronyms", "genbank_acronym", "blast_name", "lineage", "children", "descendent_with_described_species_names_count", "rank", "has_described_species_name", "counts", "min_ord", "max_ord", "extinct", "genomic_moltype"]

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
        """Create an instance of V2TaxonomyNode from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in counts (list)
        _items = []
        if self.counts:
            for _item_counts in self.counts:
                if _item_counts:
                    _items.append(_item_counts.to_dict())
            _dict['counts'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V2TaxonomyNode from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "tax_id": obj.get("tax_id"),
            "organism_name": obj.get("organism_name"),
            "common_name": obj.get("common_name"),
            "genbank_common_name": obj.get("genbank_common_name"),
            "acronyms": obj.get("acronyms"),
            "genbank_acronym": obj.get("genbank_acronym"),
            "blast_name": obj.get("blast_name"),
            "lineage": obj.get("lineage"),
            "children": obj.get("children"),
            "descendent_with_described_species_names_count": obj.get("descendent_with_described_species_names_count"),
            "rank": obj.get("rank"),
            "has_described_species_name": obj.get("has_described_species_name"),
            "counts": [V2TaxonomyNodeCountByType.from_dict(_item) for _item in obj["counts"]] if obj.get("counts") is not None else None,
            "min_ord": obj.get("min_ord"),
            "max_ord": obj.get("max_ord"),
            "extinct": obj.get("extinct"),
            "genomic_moltype": obj.get("genomic_moltype")
        })
        return _obj


