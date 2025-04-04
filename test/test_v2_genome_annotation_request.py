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

from ncbi.datasets.openapi.models.v2_genome_annotation_request import V2GenomeAnnotationRequest

class TestV2GenomeAnnotationRequest(unittest.TestCase):
    """V2GenomeAnnotationRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V2GenomeAnnotationRequest:
        """Test V2GenomeAnnotationRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V2GenomeAnnotationRequest`
        """
        model = V2GenomeAnnotationRequest()
        if include_optional:
            return V2GenomeAnnotationRequest(
                accession = '',
                annotation_ids = [
                    ''
                    ],
                symbols = [
                    ''
                    ],
                locations = [
                    ''
                    ],
                gene_types = [
                    ''
                    ],
                search_text = [
                    ''
                    ],
                sort = [
                    ncbi.datasets.openapi.models.v2_sort_field.v2SortField(
                        field = '', 
                        direction = 'SORT_DIRECTION_UNSPECIFIED', )
                    ],
                include_annotation_type = [
                    'GENOME_FASTA'
                    ],
                page_size = 56,
                table_fields = [
                    ''
                    ],
                table_format = 'NO_TABLE',
                include_tabular_header = 'INCLUDE_TABULAR_HEADER_FIRST_PAGE_ONLY',
                page_token = ''
            )
        else:
            return V2GenomeAnnotationRequest(
        )
        """

    def testV2GenomeAnnotationRequest(self):
        """Test V2GenomeAnnotationRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
