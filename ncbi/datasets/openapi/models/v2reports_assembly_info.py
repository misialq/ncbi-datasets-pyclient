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
from ncbi.datasets.openapi.models.v2reports_assembly_status import V2reportsAssemblyStatus
from ncbi.datasets.openapi.models.v2reports_atypical_info import V2reportsAtypicalInfo
from ncbi.datasets.openapi.models.v2reports_bio_project_lineage import V2reportsBioProjectLineage
from ncbi.datasets.openapi.models.v2reports_bio_sample_descriptor import V2reportsBioSampleDescriptor
from ncbi.datasets.openapi.models.v2reports_linked_assembly import V2reportsLinkedAssembly
from ncbi.datasets.openapi.models.v2reports_linked_assembly_type import V2reportsLinkedAssemblyType
from ncbi.datasets.openapi.models.v2reports_paired_assembly import V2reportsPairedAssembly
from typing import Optional, Set
from typing_extensions import Self

class V2reportsAssemblyInfo(BaseModel):
    """
    V2reportsAssemblyInfo
    """ # noqa: E501
    assembly_level: Optional[StrictStr] = None
    assembly_status: Optional[V2reportsAssemblyStatus] = None
    paired_assembly: Optional[V2reportsPairedAssembly] = None
    assembly_name: Optional[StrictStr] = None
    assembly_long_name: Optional[StrictStr] = None
    assembly_type: Optional[StrictStr] = None
    bioproject_lineage: Optional[List[V2reportsBioProjectLineage]] = None
    bioproject_accession: Optional[StrictStr] = None
    submission_date: Optional[StrictStr] = None
    release_date: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    submitter: Optional[StrictStr] = None
    refseq_category: Optional[StrictStr] = None
    synonym: Optional[StrictStr] = None
    linked_assembly: Optional[StrictStr] = None
    linked_assemblies: Optional[List[V2reportsLinkedAssembly]] = None
    atypical: Optional[V2reportsAtypicalInfo] = None
    genome_notes: Optional[List[StrictStr]] = None
    sequencing_tech: Optional[StrictStr] = None
    assembly_method: Optional[StrictStr] = None
    grouping_method: Optional[StrictStr] = None
    biosample: Optional[V2reportsBioSampleDescriptor] = None
    blast_url: Optional[StrictStr] = None
    comments: Optional[StrictStr] = None
    suppression_reason: Optional[StrictStr] = None
    diploid_role: Optional[V2reportsLinkedAssemblyType] = None
    __properties: ClassVar[List[str]] = ["assembly_level", "assembly_status", "paired_assembly", "assembly_name", "assembly_long_name", "assembly_type", "bioproject_lineage", "bioproject_accession", "submission_date", "release_date", "description", "submitter", "refseq_category", "synonym", "linked_assembly", "linked_assemblies", "atypical", "genome_notes", "sequencing_tech", "assembly_method", "grouping_method", "biosample", "blast_url", "comments", "suppression_reason", "diploid_role"]

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
        """Create an instance of V2reportsAssemblyInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of paired_assembly
        if self.paired_assembly:
            _dict['paired_assembly'] = self.paired_assembly.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in bioproject_lineage (list)
        _items = []
        if self.bioproject_lineage:
            for _item_bioproject_lineage in self.bioproject_lineage:
                if _item_bioproject_lineage:
                    _items.append(_item_bioproject_lineage.to_dict())
            _dict['bioproject_lineage'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in linked_assemblies (list)
        _items = []
        if self.linked_assemblies:
            for _item_linked_assemblies in self.linked_assemblies:
                if _item_linked_assemblies:
                    _items.append(_item_linked_assemblies.to_dict())
            _dict['linked_assemblies'] = _items
        # override the default output from pydantic by calling `to_dict()` of atypical
        if self.atypical:
            _dict['atypical'] = self.atypical.to_dict()
        # override the default output from pydantic by calling `to_dict()` of biosample
        if self.biosample:
            _dict['biosample'] = self.biosample.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V2reportsAssemblyInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "assembly_level": obj.get("assembly_level"),
            "assembly_status": obj.get("assembly_status"),
            "paired_assembly": V2reportsPairedAssembly.from_dict(obj["paired_assembly"]) if obj.get("paired_assembly") is not None else None,
            "assembly_name": obj.get("assembly_name"),
            "assembly_long_name": obj.get("assembly_long_name"),
            "assembly_type": obj.get("assembly_type"),
            "bioproject_lineage": [V2reportsBioProjectLineage.from_dict(_item) for _item in obj["bioproject_lineage"]] if obj.get("bioproject_lineage") is not None else None,
            "bioproject_accession": obj.get("bioproject_accession"),
            "submission_date": obj.get("submission_date"),
            "release_date": obj.get("release_date"),
            "description": obj.get("description"),
            "submitter": obj.get("submitter"),
            "refseq_category": obj.get("refseq_category"),
            "synonym": obj.get("synonym"),
            "linked_assembly": obj.get("linked_assembly"),
            "linked_assemblies": [V2reportsLinkedAssembly.from_dict(_item) for _item in obj["linked_assemblies"]] if obj.get("linked_assemblies") is not None else None,
            "atypical": V2reportsAtypicalInfo.from_dict(obj["atypical"]) if obj.get("atypical") is not None else None,
            "genome_notes": obj.get("genome_notes"),
            "sequencing_tech": obj.get("sequencing_tech"),
            "assembly_method": obj.get("assembly_method"),
            "grouping_method": obj.get("grouping_method"),
            "biosample": V2reportsBioSampleDescriptor.from_dict(obj["biosample"]) if obj.get("biosample") is not None else None,
            "blast_url": obj.get("blast_url"),
            "comments": obj.get("comments"),
            "suppression_reason": obj.get("suppression_reason"),
            "diploid_role": obj.get("diploid_role")
        })
        return _obj


