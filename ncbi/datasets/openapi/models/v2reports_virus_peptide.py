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
from ncbi.datasets.openapi.models.v2reports_conserved_domain import V2reportsConservedDomain
from ncbi.datasets.openapi.models.v2reports_seq_range_set_fasta import V2reportsSeqRangeSetFasta
from ncbi.datasets.openapi.models.v2reports_virus_peptide_uni_prot_id import V2reportsVirusPeptideUniProtId
from ncbi.datasets.openapi.models.v2reports_virus_peptide_viral_peptide_completeness import V2reportsVirusPeptideViralPeptideCompleteness
from typing import Optional, Set
from typing_extensions import Self

class V2reportsVirusPeptide(BaseModel):
    """
    V2reportsVirusPeptide
    """ # noqa: E501
    accession: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    other_names: Optional[List[StrictStr]] = None
    nucleotide: Optional[V2reportsSeqRangeSetFasta] = None
    protein: Optional[V2reportsSeqRangeSetFasta] = None
    pdb_ids: Optional[List[StrictStr]] = None
    cdd: Optional[List[V2reportsConservedDomain]] = None
    uni_prot_kb: Optional[V2reportsVirusPeptideUniProtId] = None
    mature_peptide: Optional[List[V2reportsVirusPeptide]] = None
    protein_completeness: Optional[V2reportsVirusPeptideViralPeptideCompleteness] = None
    __properties: ClassVar[List[str]] = ["accession", "name", "other_names", "nucleotide", "protein", "pdb_ids", "cdd", "uni_prot_kb", "mature_peptide", "protein_completeness"]

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
        """Create an instance of V2reportsVirusPeptide from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of nucleotide
        if self.nucleotide:
            _dict['nucleotide'] = self.nucleotide.to_dict()
        # override the default output from pydantic by calling `to_dict()` of protein
        if self.protein:
            _dict['protein'] = self.protein.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in cdd (list)
        _items = []
        if self.cdd:
            for _item_cdd in self.cdd:
                if _item_cdd:
                    _items.append(_item_cdd.to_dict())
            _dict['cdd'] = _items
        # override the default output from pydantic by calling `to_dict()` of uni_prot_kb
        if self.uni_prot_kb:
            _dict['uni_prot_kb'] = self.uni_prot_kb.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in mature_peptide (list)
        _items = []
        if self.mature_peptide:
            for _item_mature_peptide in self.mature_peptide:
                if _item_mature_peptide:
                    _items.append(_item_mature_peptide.to_dict())
            _dict['mature_peptide'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V2reportsVirusPeptide from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "accession": obj.get("accession"),
            "name": obj.get("name"),
            "other_names": obj.get("other_names"),
            "nucleotide": V2reportsSeqRangeSetFasta.from_dict(obj["nucleotide"]) if obj.get("nucleotide") is not None else None,
            "protein": V2reportsSeqRangeSetFasta.from_dict(obj["protein"]) if obj.get("protein") is not None else None,
            "pdb_ids": obj.get("pdb_ids"),
            "cdd": [V2reportsConservedDomain.from_dict(_item) for _item in obj["cdd"]] if obj.get("cdd") is not None else None,
            "uni_prot_kb": V2reportsVirusPeptideUniProtId.from_dict(obj["uni_prot_kb"]) if obj.get("uni_prot_kb") is not None else None,
            "mature_peptide": [V2reportsVirusPeptide.from_dict(_item) for _item in obj["mature_peptide"]] if obj.get("mature_peptide") is not None else None,
            "protein_completeness": obj.get("protein_completeness")
        })
        return _obj

# TODO: Rewrite to not use raise_errors
V2reportsVirusPeptide.model_rebuild(raise_errors=False)

