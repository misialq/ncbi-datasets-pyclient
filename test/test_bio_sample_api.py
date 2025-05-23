# coding: utf-8

"""
    NCBI Datasets API

    ### NCBI Datasets is a resource that lets you easily gather data from NCBI. The Datasets version 2 API is still in alpha, and we're updating it often to add new functionality, iron out bugs and enhance usability. For some larger downloads, you may want to download a [dehydrated zip archive](https://www.ncbi.nlm.nih.gov/datasets/docs/v2/how-tos/genomes/large-download/), and retrieve the individual data files at a later time. 

    The version of the OpenAPI document: v2
    Contact: help@ncbi.nlm.nih.gov
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ncbi.datasets.openapi.api.bio_sample_api import BioSampleApi


class TestBioSampleApi(unittest.TestCase):
    """BioSampleApi unit test stubs"""

    def setUp(self) -> None:
        self.api = BioSampleApi()

    def tearDown(self) -> None:
        pass

    def test_bio_sample_dataset_report(self) -> None:
        """Test case for bio_sample_dataset_report

        Get BioSample dataset reports by accession(s)
        """
        pass


if __name__ == '__main__':
    unittest.main()
