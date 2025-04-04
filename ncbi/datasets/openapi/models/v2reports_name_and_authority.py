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

from pydantic import BaseModel, ConfigDict, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ncbi.datasets.openapi.models.v2reports_name_and_authority_note import V2reportsNameAndAuthorityNote
from ncbi.datasets.openapi.models.v2reports_name_and_authority_publication import V2reportsNameAndAuthorityPublication
from ncbi.datasets.openapi.models.v2reports_taxonomy_type_material import V2reportsTaxonomyTypeMaterial
from typing import Optional, Set
from typing_extensions import Self

class V2reportsNameAndAuthority(BaseModel):
    """
    V2reportsNameAndAuthority
    """ # noqa: E501
    name: Optional[StrictStr] = None
    authority: Optional[StrictStr] = None
    type_strains: Optional[List[V2reportsTaxonomyTypeMaterial]] = None
    curator_synonym: Optional[StrictStr] = None
    homotypic_synonyms: Optional[List[V2reportsNameAndAuthority]] = None
    heterotypic_synonyms: Optional[List[V2reportsNameAndAuthority]] = None
    other_synonyms: Optional[List[V2reportsNameAndAuthority]] = None
    informal_names: Optional[List[StrictStr]] = None
    basionym: Optional[V2reportsNameAndAuthority] = None
    publications: Optional[List[V2reportsNameAndAuthorityPublication]] = None
    notes: Optional[List[V2reportsNameAndAuthorityNote]] = None
    formal: Optional[StrictBool] = None
    __properties: ClassVar[List[str]] = ["name", "authority", "type_strains", "curator_synonym", "homotypic_synonyms", "heterotypic_synonyms", "other_synonyms", "informal_names", "basionym", "publications", "notes", "formal"]

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
        """Create an instance of V2reportsNameAndAuthority from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in type_strains (list)
        _items = []
        if self.type_strains:
            for _item_type_strains in self.type_strains:
                if _item_type_strains:
                    _items.append(_item_type_strains.to_dict())
            _dict['type_strains'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in homotypic_synonyms (list)
        _items = []
        if self.homotypic_synonyms:
            for _item_homotypic_synonyms in self.homotypic_synonyms:
                if _item_homotypic_synonyms:
                    _items.append(_item_homotypic_synonyms.to_dict())
            _dict['homotypic_synonyms'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in heterotypic_synonyms (list)
        _items = []
        if self.heterotypic_synonyms:
            for _item_heterotypic_synonyms in self.heterotypic_synonyms:
                if _item_heterotypic_synonyms:
                    _items.append(_item_heterotypic_synonyms.to_dict())
            _dict['heterotypic_synonyms'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in other_synonyms (list)
        _items = []
        if self.other_synonyms:
            for _item_other_synonyms in self.other_synonyms:
                if _item_other_synonyms:
                    _items.append(_item_other_synonyms.to_dict())
            _dict['other_synonyms'] = _items
        # override the default output from pydantic by calling `to_dict()` of basionym
        if self.basionym:
            _dict['basionym'] = self.basionym.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in publications (list)
        _items = []
        if self.publications:
            for _item_publications in self.publications:
                if _item_publications:
                    _items.append(_item_publications.to_dict())
            _dict['publications'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in notes (list)
        _items = []
        if self.notes:
            for _item_notes in self.notes:
                if _item_notes:
                    _items.append(_item_notes.to_dict())
            _dict['notes'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V2reportsNameAndAuthority from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "authority": obj.get("authority"),
            "type_strains": [V2reportsTaxonomyTypeMaterial.from_dict(_item) for _item in obj["type_strains"]] if obj.get("type_strains") is not None else None,
            "curator_synonym": obj.get("curator_synonym"),
            "homotypic_synonyms": [V2reportsNameAndAuthority.from_dict(_item) for _item in obj["homotypic_synonyms"]] if obj.get("homotypic_synonyms") is not None else None,
            "heterotypic_synonyms": [V2reportsNameAndAuthority.from_dict(_item) for _item in obj["heterotypic_synonyms"]] if obj.get("heterotypic_synonyms") is not None else None,
            "other_synonyms": [V2reportsNameAndAuthority.from_dict(_item) for _item in obj["other_synonyms"]] if obj.get("other_synonyms") is not None else None,
            "informal_names": obj.get("informal_names"),
            "basionym": V2reportsNameAndAuthority.from_dict(obj["basionym"]) if obj.get("basionym") is not None else None,
            "publications": [V2reportsNameAndAuthorityPublication.from_dict(_item) for _item in obj["publications"]] if obj.get("publications") is not None else None,
            "notes": [V2reportsNameAndAuthorityNote.from_dict(_item) for _item in obj["notes"]] if obj.get("notes") is not None else None,
            "formal": obj.get("formal")
        })
        return _obj

# TODO: Rewrite to not use raise_errors
V2reportsNameAndAuthority.model_rebuild(raise_errors=False)

