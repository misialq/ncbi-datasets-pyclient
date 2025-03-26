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

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from ncbi.datasets.openapi.models.v2_assembly_dataset_request import V2AssemblyDatasetRequest
from ncbi.datasets.openapi.models.v2_gene_dataset_request import V2GeneDatasetRequest
from ncbi.datasets.openapi.models.v2_virus_dataset_request import V2VirusDatasetRequest
from typing import Optional, Set
from typing_extensions import Self

class V2DatasetRequest(BaseModel):
    """
    V2DatasetRequest
    """ # noqa: E501
    genome_v2: Optional[V2AssemblyDatasetRequest] = None
    gene_v2: Optional[V2GeneDatasetRequest] = None
    virus_v2: Optional[V2VirusDatasetRequest] = None
    __properties: ClassVar[List[str]] = ["genome_v2", "gene_v2", "virus_v2"]

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
        """Create an instance of V2DatasetRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of genome_v2
        if self.genome_v2:
            _dict['genome_v2'] = self.genome_v2.to_dict()
        # override the default output from pydantic by calling `to_dict()` of gene_v2
        if self.gene_v2:
            _dict['gene_v2'] = self.gene_v2.to_dict()
        # override the default output from pydantic by calling `to_dict()` of virus_v2
        if self.virus_v2:
            _dict['virus_v2'] = self.virus_v2.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V2DatasetRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "genome_v2": V2AssemblyDatasetRequest.from_dict(obj["genome_v2"]) if obj.get("genome_v2") is not None else None,
            "gene_v2": V2GeneDatasetRequest.from_dict(obj["gene_v2"]) if obj.get("gene_v2") is not None else None,
            "virus_v2": V2VirusDatasetRequest.from_dict(obj["virus_v2"]) if obj.get("virus_v2") is not None else None
        })
        return _obj


