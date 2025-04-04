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

from ncbi.datasets.openapi.models.v2reports_virus_data_report_page import V2reportsVirusDataReportPage

class TestV2reportsVirusDataReportPage(unittest.TestCase):
    """V2reportsVirusDataReportPage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V2reportsVirusDataReportPage:
        """Test V2reportsVirusDataReportPage
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V2reportsVirusDataReportPage`
        """
        model = V2reportsVirusDataReportPage()
        if include_optional:
            return V2reportsVirusDataReportPage(
                reports = [
                    ncbi.datasets.openapi.models.v2reports_virus_assembly.v2reportsVirusAssembly(
                        accession = '', 
                        is_complete = True, 
                        is_annotated = True, 
                        isolate = ncbi.datasets.openapi.models.v2reports_isolate.v2reportsIsolate(
                            name = '', 
                            source = '', 
                            collection_date = '', ), 
                        source_database = '', 
                        protein_count = 56, 
                        host = ncbi.datasets.openapi.models.v2reports_organism.v2reportsOrganism(
                            tax_id = 56, 
                            sci_name = '', 
                            organism_name = '', 
                            common_name = '', 
                            lineage = [
                                ncbi.datasets.openapi.models.v2reports_lineage_organism.v2reportsLineageOrganism(
                                    tax_id = 56, 
                                    name = '', )
                                ], 
                            strain = '', 
                            pangolin_classification = '', 
                            infraspecific_names = ncbi.datasets.openapi.models.v2reports_infraspecific_names.v2reportsInfraspecificNames(
                                breed = '', 
                                cultivar = '', 
                                ecotype = '', 
                                sex = '', 
                                strain = '', ), ), 
                        virus = ncbi.datasets.openapi.models.v2reports_organism.v2reportsOrganism(
                            tax_id = 56, 
                            sci_name = '', 
                            organism_name = '', 
                            common_name = '', 
                            strain = '', 
                            pangolin_classification = '', ), 
                        bioprojects = [
                            ''
                            ], 
                        location = ncbi.datasets.openapi.models.v2reports_virus_assembly_collection_location.v2reportsVirusAssemblyCollectionLocation(
                            geographic_location = '', 
                            geographic_region = '', 
                            usa_state = '', ), 
                        update_date = '', 
                        release_date = '', 
                        nucleotide_completeness = '', 
                        completeness = 'UNKNOWN', 
                        length = 56, 
                        gene_count = 56, 
                        mature_peptide_count = 56, 
                        biosample = '', 
                        mol_type = '', 
                        nucleotide = ncbi.datasets.openapi.models.v2reports_seq_range_set_fasta.v2reportsSeqRangeSetFasta(
                            seq_id = '', 
                            accession_version = '', 
                            title = '', 
                            sequence_hash = '', 
                            range = [
                                ncbi.datasets.openapi.models.v2reports_range.v2reportsRange(
                                    begin = '', 
                                    end = '', 
                                    orientation = 'none', 
                                    order = 56, 
                                    ribosomal_slippage = 56, )
                                ], ), 
                        purpose_of_sampling = 'PURPOSE_OF_SAMPLING_UNKNOWN', 
                        sra_accessions = [
                            ''
                            ], 
                        submitter = ncbi.datasets.openapi.models.v2reports_virus_assembly_submitter_info.v2reportsVirusAssemblySubmitterInfo(
                            names = [
                                ''
                                ], 
                            affiliation = '', 
                            country = '', ), 
                        lab_host = '', 
                        is_lab_host = True, 
                        is_vaccine_strain = True, 
                        segment = '', )
                    ],
                total_count = 56,
                next_page_token = ''
            )
        else:
            return V2reportsVirusDataReportPage(
        )
        """

    def testV2reportsVirusDataReportPage(self):
        """Test V2reportsVirusDataReportPage"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
