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
import json
from enum import Enum
from typing_extensions import Self


class V2TableFormat(str, Enum):
    """
    V2TableFormat
    """

    """
    allowed enum values
    """
    TSV = 'tsv'
    CSV = 'csv'
    JSONL = 'jsonl'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of V2TableFormat from a JSON string"""
        return cls(json.loads(json_str))


