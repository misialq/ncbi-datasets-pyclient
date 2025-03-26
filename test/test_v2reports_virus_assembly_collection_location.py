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

from ncbi.datasets.openapi.models.v2reports_virus_assembly_collection_location import V2reportsVirusAssemblyCollectionLocation

class TestV2reportsVirusAssemblyCollectionLocation(unittest.TestCase):
    """V2reportsVirusAssemblyCollectionLocation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V2reportsVirusAssemblyCollectionLocation:
        """Test V2reportsVirusAssemblyCollectionLocation
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V2reportsVirusAssemblyCollectionLocation`
        """
        model = V2reportsVirusAssemblyCollectionLocation()
        if include_optional:
            return V2reportsVirusAssemblyCollectionLocation(
                geographic_location = '',
                geographic_region = '',
                usa_state = ''
            )
        else:
            return V2reportsVirusAssemblyCollectionLocation(
        )
        """

    def testV2reportsVirusAssemblyCollectionLocation(self):
        """Test V2reportsVirusAssemblyCollectionLocation"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
