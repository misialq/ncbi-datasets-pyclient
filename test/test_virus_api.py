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

from ncbi.datasets.openapi.api.virus_api import VirusApi


class TestVirusApi(unittest.TestCase):
    """VirusApi unit test stubs"""

    def setUp(self) -> None:
        self.api = VirusApi()

    def tearDown(self) -> None:
        pass

    def test_sars2_protein_download(self) -> None:
        """Test case for sars2_protein_download

        Download SARS-CoV-2 protein and CDS datasets by protein name
        """
        pass

    def test_sars2_protein_download_post(self) -> None:
        """Test case for sars2_protein_download_post

        Download SARS-CoV-2 protein and CDS datasets by protein name by POST request
        """
        pass

    def test_sars2_protein_summary(self) -> None:
        """Test case for sars2_protein_summary

        Summary of SARS-CoV-2 protein and CDS datasets by protein name
        """
        pass

    def test_sars2_protein_summary_by_post(self) -> None:
        """Test case for sars2_protein_summary_by_post

        Summary of SARS-CoV-2 protein and CDS datasets by protein name
        """
        pass

    def test_sars2_protein_table(self) -> None:
        """Test case for sars2_protein_table

        Get SARS-CoV-2 protein metadata in a tabular format.
        """
        pass

    def test_virus_accession_availability(self) -> None:
        """Test case for virus_accession_availability

        Check available viruses by accession
        """
        pass

    def test_virus_accession_availability_post(self) -> None:
        """Test case for virus_accession_availability_post

        Check available viruses by accession
        """
        pass

    def test_virus_annotation_reports_by_acessions(self) -> None:
        """Test case for virus_annotation_reports_by_acessions

        Get virus annotation report by accession
        """
        pass

    def test_virus_annotation_reports_by_post(self) -> None:
        """Test case for virus_annotation_reports_by_post

        Get virus annotation report by POST
        """
        pass

    def test_virus_annotation_reports_by_taxon(self) -> None:
        """Test case for virus_annotation_reports_by_taxon

        Get virus annotation report by taxon
        """
        pass

    def test_virus_genome_download(self) -> None:
        """Test case for virus_genome_download

        Download a virus genome dataset by taxon
        """
        pass

    def test_virus_genome_download_accession(self) -> None:
        """Test case for virus_genome_download_accession

        Download a virus genome dataset by accession
        """
        pass

    def test_virus_genome_download_post(self) -> None:
        """Test case for virus_genome_download_post

        Get a virus genome dataset by post
        """
        pass

    def test_virus_genome_summary(self) -> None:
        """Test case for virus_genome_summary

        Get summary data for virus genomes by taxon
        """
        pass

    def test_virus_genome_summary_by_post(self) -> None:
        """Test case for virus_genome_summary_by_post

        Get summary data for virus genomes by post
        """
        pass

    def test_virus_genome_table(self) -> None:
        """Test case for virus_genome_table

        Get virus genome metadata in a tabular format.
        """
        pass

    def test_virus_reports_by_acessions(self) -> None:
        """Test case for virus_reports_by_acessions

        Get virus metadata by accession
        """
        pass

    def test_virus_reports_by_post(self) -> None:
        """Test case for virus_reports_by_post

        Get virus metadata by POST
        """
        pass

    def test_virus_reports_by_taxon(self) -> None:
        """Test case for virus_reports_by_taxon

        Get virus metadata by taxon
        """
        pass


if __name__ == '__main__':
    unittest.main()
