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
from ncbi.datasets.openapi.models.v2reports_annotation import V2reportsAnnotation
from ncbi.datasets.openapi.models.v2reports_gene_type import V2reportsGeneType
from ncbi.datasets.openapi.models.v2reports_genomic_region import V2reportsGenomicRegion
from ncbi.datasets.openapi.models.v2reports_orientation import V2reportsOrientation
from ncbi.datasets.openapi.models.v2reports_protein import V2reportsProtein
from ncbi.datasets.openapi.models.v2reports_rna_type import V2reportsRnaType
from ncbi.datasets.openapi.models.v2reports_transcript import V2reportsTranscript
from typing import Optional, Set
from typing_extensions import Self

class V2reportsGenomeAnnotation(BaseModel):
    """
    V2reportsGenomeAnnotation
    """ # noqa: E501
    gene_id: Optional[StrictStr] = None
    symbol: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    tax_id: Optional[StrictStr] = None
    taxname: Optional[StrictStr] = None
    common_name: Optional[StrictStr] = None
    type: Optional[V2reportsGeneType] = None
    gene_type: Optional[StrictStr] = None
    rna_type: Optional[V2reportsRnaType] = None
    orientation: Optional[V2reportsOrientation] = None
    locus_tag: Optional[StrictStr] = None
    reference_standards: Optional[List[V2reportsGenomicRegion]] = None
    genomic_regions: Optional[List[V2reportsGenomicRegion]] = None
    transcripts: Optional[List[V2reportsTranscript]] = None
    proteins: Optional[List[V2reportsProtein]] = None
    chromosomes: Optional[List[StrictStr]] = None
    swiss_prot_accessions: Optional[List[StrictStr]] = None
    ensembl_gene_ids: Optional[List[StrictStr]] = None
    omim_ids: Optional[List[StrictStr]] = None
    synonyms: Optional[List[StrictStr]] = None
    annotations: Optional[List[V2reportsAnnotation]] = None
    __properties: ClassVar[List[str]] = ["gene_id", "symbol", "description", "name", "tax_id", "taxname", "common_name", "type", "gene_type", "rna_type", "orientation", "locus_tag", "reference_standards", "genomic_regions", "transcripts", "proteins", "chromosomes", "swiss_prot_accessions", "ensembl_gene_ids", "omim_ids", "synonyms", "annotations"]

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
        """Create an instance of V2reportsGenomeAnnotation from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in reference_standards (list)
        _items = []
        if self.reference_standards:
            for _item_reference_standards in self.reference_standards:
                if _item_reference_standards:
                    _items.append(_item_reference_standards.to_dict())
            _dict['reference_standards'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in genomic_regions (list)
        _items = []
        if self.genomic_regions:
            for _item_genomic_regions in self.genomic_regions:
                if _item_genomic_regions:
                    _items.append(_item_genomic_regions.to_dict())
            _dict['genomic_regions'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in transcripts (list)
        _items = []
        if self.transcripts:
            for _item_transcripts in self.transcripts:
                if _item_transcripts:
                    _items.append(_item_transcripts.to_dict())
            _dict['transcripts'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in proteins (list)
        _items = []
        if self.proteins:
            for _item_proteins in self.proteins:
                if _item_proteins:
                    _items.append(_item_proteins.to_dict())
            _dict['proteins'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in annotations (list)
        _items = []
        if self.annotations:
            for _item_annotations in self.annotations:
                if _item_annotations:
                    _items.append(_item_annotations.to_dict())
            _dict['annotations'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V2reportsGenomeAnnotation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "gene_id": obj.get("gene_id"),
            "symbol": obj.get("symbol"),
            "description": obj.get("description"),
            "name": obj.get("name"),
            "tax_id": obj.get("tax_id"),
            "taxname": obj.get("taxname"),
            "common_name": obj.get("common_name"),
            "type": obj.get("type"),
            "gene_type": obj.get("gene_type"),
            "rna_type": obj.get("rna_type"),
            "orientation": obj.get("orientation"),
            "locus_tag": obj.get("locus_tag"),
            "reference_standards": [V2reportsGenomicRegion.from_dict(_item) for _item in obj["reference_standards"]] if obj.get("reference_standards") is not None else None,
            "genomic_regions": [V2reportsGenomicRegion.from_dict(_item) for _item in obj["genomic_regions"]] if obj.get("genomic_regions") is not None else None,
            "transcripts": [V2reportsTranscript.from_dict(_item) for _item in obj["transcripts"]] if obj.get("transcripts") is not None else None,
            "proteins": [V2reportsProtein.from_dict(_item) for _item in obj["proteins"]] if obj.get("proteins") is not None else None,
            "chromosomes": obj.get("chromosomes"),
            "swiss_prot_accessions": obj.get("swiss_prot_accessions"),
            "ensembl_gene_ids": obj.get("ensembl_gene_ids"),
            "omim_ids": obj.get("omim_ids"),
            "synonyms": obj.get("synonyms"),
            "annotations": [V2reportsAnnotation.from_dict(_item) for _item in obj["annotations"]] if obj.get("annotations") is not None else None
        })
        return _obj


