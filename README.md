# ncbi-datasets-pyclient
### NCBI Datasets is a resource that lets you easily gather data from NCBI.
The Datasets version 2 API is still in alpha, and we're updating it often to add new functionality, iron out bugs and enhance usability.
For some larger downloads, you may want to download a [dehydrated zip archive](https://www.ncbi.nlm.nih.gov/datasets/docs/v2/how-tos/genomes/large-download/), and retrieve the individual data files at a later time. 

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: v2
- Package version: v17.2.0
- Generator version: 7.12.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://www.ncbi.nlm.nih.gov/datasets](https://www.ncbi.nlm.nih.gov/datasets)

## Requirements.

Python 3.8+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/misialq/ncbi-datasets-pyclient.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/misialq/ncbi-datasets-pyclient.git`)

Then import the package:
```python
import ncbi.datasets.openapi
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import ncbi.datasets.openapi
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import ncbi.datasets.openapi
from ncbi.datasets.openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ncbi.nlm.nih.gov/datasets/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = ncbi.datasets.openapi.Configuration(
    host = "https://api.ncbi.nlm.nih.gov/datasets/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuthHeader
configuration.api_key['ApiKeyAuthHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuthHeader'] = 'Bearer'


# Enter a context with an instance of the API client
with ncbi.datasets.openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ncbi.datasets.openapi.BioSampleApi(api_client)
    accessions = ['[\"SAMN15960293\"]'] # List[str] | 

    try:
        # Get BioSample dataset reports by accession(s)
        api_response = api_instance.bio_sample_dataset_report(accessions)
        print("The response of BioSampleApi->bio_sample_dataset_report:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BioSampleApi->bio_sample_dataset_report: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.ncbi.nlm.nih.gov/datasets/v2*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*BioSampleApi* | [**bio_sample_dataset_report**](docs/BioSampleApi.md#bio_sample_dataset_report) | **GET** /biosample/accession/{accessions}/biosample_report | Get BioSample dataset reports by accession(s)
*GeneApi* | [**download_gene_package**](docs/GeneApi.md#download_gene_package) | **GET** /gene/id/{gene_ids}/download | Get a gene dataset by gene ID
*GeneApi* | [**download_gene_package_post**](docs/GeneApi.md#download_gene_package_post) | **POST** /gene/download | Get a gene dataset by POST
*GeneApi* | [**gene_chromosome_summary**](docs/GeneApi.md#gene_chromosome_summary) | **GET** /gene/taxon/{taxon}/annotation/{annotation_name}/chromosome_summary | Get summary of chromosomes for a particular taxon&#39;s annotation
*GeneApi* | [**gene_counts_for_taxon**](docs/GeneApi.md#gene_counts_for_taxon) | **GET** /gene/taxon/{taxon}/counts | Get gene counts by taxonomic identifier
*GeneApi* | [**gene_counts_for_taxon_by_post**](docs/GeneApi.md#gene_counts_for_taxon_by_post) | **POST** /gene/taxon/counts | Get gene counts by taxonomic identifier
*GeneApi* | [**gene_dataset_report**](docs/GeneApi.md#gene_dataset_report) | **POST** /gene/dataset_report | Get gene dataset report as JSON
*GeneApi* | [**gene_dataset_report_by_accession**](docs/GeneApi.md#gene_dataset_report_by_accession) | **GET** /gene/accession/{accessions}/dataset_report | Get dataset reports by accession IDs
*GeneApi* | [**gene_dataset_report_by_tax_and_symbol**](docs/GeneApi.md#gene_dataset_report_by_tax_and_symbol) | **GET** /gene/symbol/{symbols}/taxon/{taxon}/dataset_report | Get dataset reports by taxons.
*GeneApi* | [**gene_dataset_reports_by_id**](docs/GeneApi.md#gene_dataset_reports_by_id) | **GET** /gene/id/{gene_ids}/dataset_report | Get dataset reports by gene IDs.
*GeneApi* | [**gene_dataset_reports_by_locus_tag**](docs/GeneApi.md#gene_dataset_reports_by_locus_tag) | **GET** /gene/locus_tag/{locus_tags}/dataset_report | Get gene dataset reports by locus tag
*GeneApi* | [**gene_dataset_reports_by_taxon**](docs/GeneApi.md#gene_dataset_reports_by_taxon) | **GET** /gene/taxon/{taxon}/dataset_report | Get gene dataset reports by taxonomic identifier
*GeneApi* | [**gene_download_summary_by_id**](docs/GeneApi.md#gene_download_summary_by_id) | **GET** /gene/id/{gene_ids}/download_summary | Get gene download summary by GeneID
*GeneApi* | [**gene_download_summary_by_post**](docs/GeneApi.md#gene_download_summary_by_post) | **POST** /gene/download_summary | Get gene download summary
*GeneApi* | [**gene_links_by_id**](docs/GeneApi.md#gene_links_by_id) | **GET** /gene/id/{gene_ids}/links | Get gene links by gene ID
*GeneApi* | [**gene_links_by_id_by_post**](docs/GeneApi.md#gene_links_by_id_by_post) | **POST** /gene/links | Get gene links by gene ID
*GeneApi* | [**gene_metadata_by_accession**](docs/GeneApi.md#gene_metadata_by_accession) | **GET** /gene/accession/{accessions} | Get gene metadata by RefSeq Accession
*GeneApi* | [**gene_metadata_by_post**](docs/GeneApi.md#gene_metadata_by_post) | **POST** /gene | Get gene metadata as JSON
*GeneApi* | [**gene_metadata_by_tax_and_symbol**](docs/GeneApi.md#gene_metadata_by_tax_and_symbol) | **GET** /gene/symbol/{symbols}/taxon/{taxon} | Get gene metadata by gene symbol
*GeneApi* | [**gene_orthologs_by_id**](docs/GeneApi.md#gene_orthologs_by_id) | **GET** /gene/id/{gene_id}/orthologs | Get gene orthologs by gene ID
*GeneApi* | [**gene_orthologs_by_post**](docs/GeneApi.md#gene_orthologs_by_post) | **POST** /gene/orthologs | Get gene orthologs by gene ID
*GeneApi* | [**gene_product_report**](docs/GeneApi.md#gene_product_report) | **POST** /gene/product_report | Get gene product reports as JSON
*GeneApi* | [**gene_product_report_by_accession**](docs/GeneApi.md#gene_product_report_by_accession) | **GET** /gene/accession/{accessions}/product_report | Get gene product reports by accession IDs
*GeneApi* | [**gene_product_report_by_tax_and_symbol**](docs/GeneApi.md#gene_product_report_by_tax_and_symbol) | **GET** /gene/symbol/{symbols}/taxon/{taxon}/product_report | Get product reports by taxon.
*GeneApi* | [**gene_product_reports_by_id**](docs/GeneApi.md#gene_product_reports_by_id) | **GET** /gene/id/{gene_ids}/product_report | Get gene product reports by gene IDs.
*GeneApi* | [**gene_product_reports_by_locus_tags**](docs/GeneApi.md#gene_product_reports_by_locus_tags) | **GET** /gene/locus_tag/{locus_tags}/product_report | Get gene product reports by locus tags
*GeneApi* | [**gene_product_reports_by_taxon**](docs/GeneApi.md#gene_product_reports_by_taxon) | **GET** /gene/taxon/{taxon}/product_report | Get gene product reports by taxonomic identifier
*GeneApi* | [**gene_reports_by_id**](docs/GeneApi.md#gene_reports_by_id) | **GET** /gene/id/{gene_ids} | Get gene reports by GeneID
*GeneApi* | [**gene_reports_by_taxon**](docs/GeneApi.md#gene_reports_by_taxon) | **GET** /gene/taxon/{taxon} | Get gene reports by taxonomic identifier
*GenomeApi* | [**annotation_report_facets_by_accession**](docs/GenomeApi.md#annotation_report_facets_by_accession) | **GET** /genome/accession/{accession}/annotation_summary | Get genome annotation report summary information
*GenomeApi* | [**annotation_report_facets_by_post**](docs/GenomeApi.md#annotation_report_facets_by_post) | **POST** /genome/annotation_summary | Get genome annotation report summary information
*GenomeApi* | [**assembly_accessions_for_sequence_accession**](docs/GenomeApi.md#assembly_accessions_for_sequence_accession) | **GET** /genome/sequence_accession/{accession}/sequence_assemblies | Get assembly accessions for a sequence accession
*GenomeApi* | [**assembly_accessions_for_sequence_accession_by_post**](docs/GenomeApi.md#assembly_accessions_for_sequence_accession_by_post) | **POST** /genome/sequence_assemblies | Get assembly accessions for a sequence accession
*GenomeApi* | [**assembly_revision_history_by_get**](docs/GenomeApi.md#assembly_revision_history_by_get) | **GET** /genome/accession/{accession}/revision_history | Get revision history for assembly by accession
*GenomeApi* | [**assembly_revision_history_by_post**](docs/GenomeApi.md#assembly_revision_history_by_post) | **POST** /genome/revision_history | Get revision history for assembly by accession
*GenomeApi* | [**check_assembly_availability**](docs/GenomeApi.md#check_assembly_availability) | **GET** /genome/accession/{accessions}/check | Check the validity of genome accessions
*GenomeApi* | [**check_assembly_availability_post**](docs/GenomeApi.md#check_assembly_availability_post) | **POST** /genome/check | Check the validity of many genome accessions in a single request
*GenomeApi* | [**checkm_histogram_by_taxon**](docs/GenomeApi.md#checkm_histogram_by_taxon) | **GET** /genome/taxon/{species_taxon}/checkm_histogram | Get CheckM histogram by species taxon
*GenomeApi* | [**checkm_histogram_by_taxon_by_post**](docs/GenomeApi.md#checkm_histogram_by_taxon_by_post) | **POST** /genome/checkm_histogram | Get CheckM histogram by species taxon
*GenomeApi* | [**download_assembly_package**](docs/GenomeApi.md#download_assembly_package) | **GET** /genome/accession/{accessions}/download | Get a genome dataset by accession
*GenomeApi* | [**download_assembly_package_post**](docs/GenomeApi.md#download_assembly_package_post) | **POST** /genome/download | Get a genome dataset by post
*GenomeApi* | [**download_genome_annotation_package**](docs/GenomeApi.md#download_genome_annotation_package) | **GET** /genome/accession/{accession}/annotation_report/download | Get an annotation report dataset by accession
*GenomeApi* | [**download_genome_annotation_package_by_post**](docs/GenomeApi.md#download_genome_annotation_package_by_post) | **POST** /genome/annotation_report/download | Get an annotation report dataset by accession
*GenomeApi* | [**genome_annotation_download_summary**](docs/GenomeApi.md#genome_annotation_download_summary) | **GET** /genome/accession/{accession}/annotation_report/download_summary | Preview feature dataset download
*GenomeApi* | [**genome_annotation_download_summary_by_post**](docs/GenomeApi.md#genome_annotation_download_summary_by_post) | **POST** /genome/annotation_report/download_summary | Preview feature download by POST
*GenomeApi* | [**genome_annotation_report**](docs/GenomeApi.md#genome_annotation_report) | **GET** /genome/accession/{accession}/annotation_report | Get genome annotation reports by genome accession
*GenomeApi* | [**genome_annotation_report_by_post**](docs/GenomeApi.md#genome_annotation_report_by_post) | **POST** /genome/annotation_report | Get genome annotation reports by genome accession
*GenomeApi* | [**genome_dataset_report**](docs/GenomeApi.md#genome_dataset_report) | **GET** /genome/accession/{accessions}/dataset_report | Get dataset reports by accessions
*GenomeApi* | [**genome_dataset_report_by_post**](docs/GenomeApi.md#genome_dataset_report_by_post) | **POST** /genome/dataset_report | Get dataset reports by accessions
*GenomeApi* | [**genome_dataset_reports_by_assembly_name**](docs/GenomeApi.md#genome_dataset_reports_by_assembly_name) | **GET** /genome/assembly_name/{assembly_names}/dataset_report | Get dataset reports by assembly name (exact)
*GenomeApi* | [**genome_dataset_reports_by_bioproject**](docs/GenomeApi.md#genome_dataset_reports_by_bioproject) | **GET** /genome/bioproject/{bioprojects}/dataset_report | Get dataset reports by bioproject
*GenomeApi* | [**genome_dataset_reports_by_biosample_id**](docs/GenomeApi.md#genome_dataset_reports_by_biosample_id) | **GET** /genome/biosample/{biosample_ids}/dataset_report | Get dataset reports by biosample id
*GenomeApi* | [**genome_dataset_reports_by_taxon**](docs/GenomeApi.md#genome_dataset_reports_by_taxon) | **GET** /genome/taxon/{taxons}/dataset_report | Get dataset reports by taxons
*GenomeApi* | [**genome_dataset_reports_by_wgs**](docs/GenomeApi.md#genome_dataset_reports_by_wgs) | **GET** /genome/wgs/{wgs_accessions}/dataset_report | Get dataset reports by wgs accession
*GenomeApi* | [**genome_download_summary**](docs/GenomeApi.md#genome_download_summary) | **GET** /genome/accession/{accessions}/download_summary | Preview genome dataset download
*GenomeApi* | [**genome_download_summary_by_post**](docs/GenomeApi.md#genome_download_summary_by_post) | **POST** /genome/download_summary | Preview genome dataset download by POST
*GenomeApi* | [**genome_links_by_accession**](docs/GenomeApi.md#genome_links_by_accession) | **GET** /genome/accession/{accessions}/links | Get assembly links by accessions
*GenomeApi* | [**genome_links_by_accession_by_post**](docs/GenomeApi.md#genome_links_by_accession_by_post) | **POST** /genome/links | Get assembly links by accessions
*GenomeApi* | [**genome_sequence_report**](docs/GenomeApi.md#genome_sequence_report) | **GET** /genome/accession/{accession}/sequence_reports | Get sequence reports by accessions
*GenomeApi* | [**genome_sequence_report_by_post**](docs/GenomeApi.md#genome_sequence_report_by_post) | **POST** /genome/sequence_reports | Get sequence reports by accessions
*OrganelleApi* | [**download_organelle_package**](docs/OrganelleApi.md#download_organelle_package) | **GET** /organelle/accession/{accessions}/download | Get a organelle data package by accesions
*OrganelleApi* | [**download_organelle_package_by_post**](docs/OrganelleApi.md#download_organelle_package_by_post) | **POST** /organelle/download | Get a organelle data package by post
*OrganelleApi* | [**organelle_datareport_by_accession**](docs/OrganelleApi.md#organelle_datareport_by_accession) | **GET** /organelle/accessions/{accessions}/dataset_report | Get Organelle dataset report by accession
*OrganelleApi* | [**organelle_datareport_by_post**](docs/OrganelleApi.md#organelle_datareport_by_post) | **POST** /organelle/dataset_report | Get Organelle dataset report by http post
*OrganelleApi* | [**organelle_datareport_by_taxon**](docs/OrganelleApi.md#organelle_datareport_by_taxon) | **GET** /organelle/taxon/{taxons}/dataset_report | Get Organelle dataset report by taxons
*ProkaryoteApi* | [**download_prokaryote_gene_package**](docs/ProkaryoteApi.md#download_prokaryote_gene_package) | **GET** /protein/accession/{accessions}/download | Get a prokaryote gene dataset by RefSeq protein accession
*ProkaryoteApi* | [**download_prokaryote_gene_package_post**](docs/ProkaryoteApi.md#download_prokaryote_gene_package_post) | **POST** /protein/accession/download | Get a prokaryote gene dataset by RefSeq protein accession by POST
*TaxonomyApi* | [**download_taxonomy_package**](docs/TaxonomyApi.md#download_taxonomy_package) | **GET** /taxonomy/taxon/{tax_ids}/download | Get a taxonomy data package by tax ID
*TaxonomyApi* | [**download_taxonomy_package_by_post**](docs/TaxonomyApi.md#download_taxonomy_package_by_post) | **POST** /taxonomy/download | Get a taxonomy data package by tax_id
*TaxonomyApi* | [**tax_name_query**](docs/TaxonomyApi.md#tax_name_query) | **GET** /taxonomy/taxon_suggest/{taxon_query} | Get a list of taxonomy names and IDs given a partial taxonomic name
*TaxonomyApi* | [**tax_name_query_by_post**](docs/TaxonomyApi.md#tax_name_query_by_post) | **POST** /taxonomy/taxon_suggest | Get a list of taxonomy names and IDs given a partial taxonomic name
*TaxonomyApi* | [**taxonomy_data_report**](docs/TaxonomyApi.md#taxonomy_data_report) | **GET** /taxonomy/taxon/{taxons}/dataset_report | Use taxonomic identifiers to get taxonomic data report
*TaxonomyApi* | [**taxonomy_data_report_post**](docs/TaxonomyApi.md#taxonomy_data_report_post) | **POST** /taxonomy/dataset_report | Use taxonomic identifiers to get taxonomic names data report by post
*TaxonomyApi* | [**taxonomy_filtered_subtree**](docs/TaxonomyApi.md#taxonomy_filtered_subtree) | **GET** /taxonomy/taxon/{taxons}/filtered_subtree | Use taxonomic identifiers to get a filtered taxonomic subtree
*TaxonomyApi* | [**taxonomy_filtered_subtree_post**](docs/TaxonomyApi.md#taxonomy_filtered_subtree_post) | **POST** /taxonomy/filtered_subtree | Use taxonomic identifiers to get a filtered taxonomic subtree by post
*TaxonomyApi* | [**taxonomy_image**](docs/TaxonomyApi.md#taxonomy_image) | **GET** /taxonomy/taxon/{taxon}/image | Retrieve image associated with a taxonomic identifier
*TaxonomyApi* | [**taxonomy_image_metadata**](docs/TaxonomyApi.md#taxonomy_image_metadata) | **GET** /taxonomy/taxon/{taxon}/image/metadata | Retrieve image metadata associated with a taxonomic identifier
*TaxonomyApi* | [**taxonomy_image_metadata_post**](docs/TaxonomyApi.md#taxonomy_image_metadata_post) | **POST** /taxonomy/image/metadata | Retrieve image metadata associated with a taxonomic identifier by post
*TaxonomyApi* | [**taxonomy_image_post**](docs/TaxonomyApi.md#taxonomy_image_post) | **POST** /taxonomy/image | Retrieve image associated with a taxonomic identifier by post
*TaxonomyApi* | [**taxonomy_links**](docs/TaxonomyApi.md#taxonomy_links) | **GET** /taxonomy/taxon/{taxon}/links | Retrieve external links associated with a taxonomic identifier.
*TaxonomyApi* | [**taxonomy_links_by_post**](docs/TaxonomyApi.md#taxonomy_links_by_post) | **POST** /taxonomy/links | Retrieve external links associated with a taxonomic identifier.
*TaxonomyApi* | [**taxonomy_metadata**](docs/TaxonomyApi.md#taxonomy_metadata) | **GET** /taxonomy/taxon/{taxons} | Use taxonomic identifiers to get taxonomic metadata
*TaxonomyApi* | [**taxonomy_metadata_post**](docs/TaxonomyApi.md#taxonomy_metadata_post) | **POST** /taxonomy | Use taxonomic identifiers to get taxonomic metadata by post
*TaxonomyApi* | [**taxonomy_names**](docs/TaxonomyApi.md#taxonomy_names) | **GET** /taxonomy/taxon/{taxons}/name_report | Use taxonomic identifiers to get taxonomic names data report
*TaxonomyApi* | [**taxonomy_names_post**](docs/TaxonomyApi.md#taxonomy_names_post) | **POST** /taxonomy/name_report | Use taxonomic identifiers to get taxonomic names data report by post
*TaxonomyApi* | [**taxonomy_related_ids**](docs/TaxonomyApi.md#taxonomy_related_ids) | **GET** /taxonomy/taxon/{tax_id}/related_ids | Use taxonomic identifier to get related taxonomic identifiers, such as children
*TaxonomyApi* | [**taxonomy_related_ids_post**](docs/TaxonomyApi.md#taxonomy_related_ids_post) | **POST** /taxonomy/related_ids | Use taxonomic identifier to get related taxonomic identifiers, such as children
*VersionApi* | [**version**](docs/VersionApi.md#version) | **GET** /version | Retrieve service version
*VirusApi* | [**sars2_protein_download**](docs/VirusApi.md#sars2_protein_download) | **GET** /virus/taxon/sars2/protein/{proteins}/download | Download SARS-CoV-2 protein and CDS datasets by protein name
*VirusApi* | [**sars2_protein_download_post**](docs/VirusApi.md#sars2_protein_download_post) | **POST** /virus/taxon/sars2/protein/download | Download SARS-CoV-2 protein and CDS datasets by protein name by POST request
*VirusApi* | [**sars2_protein_summary**](docs/VirusApi.md#sars2_protein_summary) | **GET** /virus/taxon/sars2/protein/{proteins} | Summary of SARS-CoV-2 protein and CDS datasets by protein name
*VirusApi* | [**sars2_protein_summary_by_post**](docs/VirusApi.md#sars2_protein_summary_by_post) | **POST** /virus/taxon/sars2/protein | Summary of SARS-CoV-2 protein and CDS datasets by protein name
*VirusApi* | [**sars2_protein_table**](docs/VirusApi.md#sars2_protein_table) | **GET** /virus/taxon/sars2/protein/{proteins}/table | Get SARS-CoV-2 protein metadata in a tabular format.
*VirusApi* | [**virus_accession_availability**](docs/VirusApi.md#virus_accession_availability) | **GET** /virus/accession/{accessions}/check | Check available viruses by accession
*VirusApi* | [**virus_accession_availability_post**](docs/VirusApi.md#virus_accession_availability_post) | **POST** /virus/check | Check available viruses by accession
*VirusApi* | [**virus_annotation_reports_by_acessions**](docs/VirusApi.md#virus_annotation_reports_by_acessions) | **GET** /virus/accession/{accessions}/annotation_report | Get virus annotation report by accession
*VirusApi* | [**virus_annotation_reports_by_post**](docs/VirusApi.md#virus_annotation_reports_by_post) | **POST** /virus/annotation_report | Get virus annotation report by POST
*VirusApi* | [**virus_annotation_reports_by_taxon**](docs/VirusApi.md#virus_annotation_reports_by_taxon) | **GET** /virus/taxon/{taxon}/annotation_report | Get virus annotation report by taxon
*VirusApi* | [**virus_genome_download**](docs/VirusApi.md#virus_genome_download) | **GET** /virus/taxon/{taxon}/genome/download | Download a virus genome dataset by taxon
*VirusApi* | [**virus_genome_download_accession**](docs/VirusApi.md#virus_genome_download_accession) | **GET** /virus/accession/{accessions}/genome/download | Download a virus genome dataset by accession
*VirusApi* | [**virus_genome_download_post**](docs/VirusApi.md#virus_genome_download_post) | **POST** /virus/genome/download | Get a virus genome dataset by post
*VirusApi* | [**virus_genome_summary**](docs/VirusApi.md#virus_genome_summary) | **GET** /virus/taxon/{taxon}/genome | Get summary data for virus genomes by taxon
*VirusApi* | [**virus_genome_summary_by_post**](docs/VirusApi.md#virus_genome_summary_by_post) | **POST** /virus/genome | Get summary data for virus genomes by post
*VirusApi* | [**virus_genome_table**](docs/VirusApi.md#virus_genome_table) | **GET** /virus/taxon/{taxon}/genome/table | Get virus genome metadata in a tabular format.
*VirusApi* | [**virus_reports_by_acessions**](docs/VirusApi.md#virus_reports_by_acessions) | **GET** /virus/accession/{accessions}/dataset_report | Get virus metadata by accession
*VirusApi* | [**virus_reports_by_post**](docs/VirusApi.md#virus_reports_by_post) | **POST** /virus | Get virus metadata by POST
*VirusApi* | [**virus_reports_by_taxon**](docs/VirusApi.md#virus_reports_by_taxon) | **GET** /virus/taxon/{taxon}/dataset_report | Get virus metadata by taxon


## Documentation For Models

 - [ProtobufAny](docs/ProtobufAny.md)
 - [RpcStatus](docs/RpcStatus.md)
 - [V2AnnotationForAssemblyType](docs/V2AnnotationForAssemblyType.md)
 - [V2AnnotationForOrganelleType](docs/V2AnnotationForOrganelleType.md)
 - [V2AssemblyAccessions](docs/V2AssemblyAccessions.md)
 - [V2AssemblyCheckMHistogramReply](docs/V2AssemblyCheckMHistogramReply.md)
 - [V2AssemblyCheckMHistogramReplyHistogramInterval](docs/V2AssemblyCheckMHistogramReplyHistogramInterval.md)
 - [V2AssemblyCheckMHistogramRequest](docs/V2AssemblyCheckMHistogramRequest.md)
 - [V2AssemblyDatasetAvailability](docs/V2AssemblyDatasetAvailability.md)
 - [V2AssemblyDatasetDescriptorsFilter](docs/V2AssemblyDatasetDescriptorsFilter.md)
 - [V2AssemblyDatasetDescriptorsFilterAssemblySource](docs/V2AssemblyDatasetDescriptorsFilterAssemblySource.md)
 - [V2AssemblyDatasetDescriptorsFilterAssemblyVersion](docs/V2AssemblyDatasetDescriptorsFilterAssemblyVersion.md)
 - [V2AssemblyDatasetDescriptorsFilterMetagenomeDerivedFilter](docs/V2AssemblyDatasetDescriptorsFilterMetagenomeDerivedFilter.md)
 - [V2AssemblyDatasetDescriptorsFilterTypeMaterialCategory](docs/V2AssemblyDatasetDescriptorsFilterTypeMaterialCategory.md)
 - [V2AssemblyDatasetReportsRequest](docs/V2AssemblyDatasetReportsRequest.md)
 - [V2AssemblyDatasetReportsRequestContentType](docs/V2AssemblyDatasetReportsRequestContentType.md)
 - [V2AssemblyDatasetRequest](docs/V2AssemblyDatasetRequest.md)
 - [V2AssemblyDatasetRequestResolution](docs/V2AssemblyDatasetRequestResolution.md)
 - [V2AssemblyLinksReply](docs/V2AssemblyLinksReply.md)
 - [V2AssemblyLinksReplyAssemblyLink](docs/V2AssemblyLinksReplyAssemblyLink.md)
 - [V2AssemblyLinksReplyAssemblyLinkType](docs/V2AssemblyLinksReplyAssemblyLinkType.md)
 - [V2AssemblyLinksRequest](docs/V2AssemblyLinksRequest.md)
 - [V2AssemblyRevisionHistory](docs/V2AssemblyRevisionHistory.md)
 - [V2AssemblyRevisionHistoryRequest](docs/V2AssemblyRevisionHistoryRequest.md)
 - [V2AssemblySequenceReportsRequest](docs/V2AssemblySequenceReportsRequest.md)
 - [V2DatasetRequest](docs/V2DatasetRequest.md)
 - [V2DownloadSummary](docs/V2DownloadSummary.md)
 - [V2DownloadSummaryAvailableFiles](docs/V2DownloadSummaryAvailableFiles.md)
 - [V2DownloadSummaryDehydrated](docs/V2DownloadSummaryDehydrated.md)
 - [V2DownloadSummaryFileSummary](docs/V2DownloadSummaryFileSummary.md)
 - [V2DownloadSummaryHydrated](docs/V2DownloadSummaryHydrated.md)
 - [V2Fasta](docs/V2Fasta.md)
 - [V2GeneChromosomeSummaryReply](docs/V2GeneChromosomeSummaryReply.md)
 - [V2GeneChromosomeSummaryReplyGeneChromosomeSummary](docs/V2GeneChromosomeSummaryReplyGeneChromosomeSummary.md)
 - [V2GeneCountsByTaxonReply](docs/V2GeneCountsByTaxonReply.md)
 - [V2GeneCountsByTaxonReplyGeneTypeAndCount](docs/V2GeneCountsByTaxonReplyGeneTypeAndCount.md)
 - [V2GeneCountsByTaxonRequest](docs/V2GeneCountsByTaxonRequest.md)
 - [V2GeneDatasetReportsRequest](docs/V2GeneDatasetReportsRequest.md)
 - [V2GeneDatasetReportsRequestContentType](docs/V2GeneDatasetReportsRequestContentType.md)
 - [V2GeneDatasetReportsRequestSymbolsForTaxon](docs/V2GeneDatasetReportsRequestSymbolsForTaxon.md)
 - [V2GeneDatasetRequest](docs/V2GeneDatasetRequest.md)
 - [V2GeneDatasetRequestContentType](docs/V2GeneDatasetRequestContentType.md)
 - [V2GeneDatasetRequestGeneDatasetReportType](docs/V2GeneDatasetRequestGeneDatasetReportType.md)
 - [V2GeneLinksReply](docs/V2GeneLinksReply.md)
 - [V2GeneLinksReplyGeneLink](docs/V2GeneLinksReplyGeneLink.md)
 - [V2GeneLinksReplyGeneLinkType](docs/V2GeneLinksReplyGeneLinkType.md)
 - [V2GeneLinksRequest](docs/V2GeneLinksRequest.md)
 - [V2GeneType](docs/V2GeneType.md)
 - [V2GenomeAnnotationRequest](docs/V2GenomeAnnotationRequest.md)
 - [V2GenomeAnnotationRequestAnnotationType](docs/V2GenomeAnnotationRequestAnnotationType.md)
 - [V2GenomeAnnotationRequestGenomeAnnotationTableFormat](docs/V2GenomeAnnotationRequestGenomeAnnotationTableFormat.md)
 - [V2GenomeAnnotationTableSummaryReply](docs/V2GenomeAnnotationTableSummaryReply.md)
 - [V2HttpBody](docs/V2HttpBody.md)
 - [V2ImageSize](docs/V2ImageSize.md)
 - [V2IncludeTabularHeader](docs/V2IncludeTabularHeader.md)
 - [V2OrganelleDownloadRequest](docs/V2OrganelleDownloadRequest.md)
 - [V2OrganelleMetadataRequest](docs/V2OrganelleMetadataRequest.md)
 - [V2OrganelleMetadataRequestContentType](docs/V2OrganelleMetadataRequestContentType.md)
 - [V2OrganelleMetadataRequestOrganelleTableFormat](docs/V2OrganelleMetadataRequestOrganelleTableFormat.md)
 - [V2OrganelleSort](docs/V2OrganelleSort.md)
 - [V2OrganismQueryRequest](docs/V2OrganismQueryRequest.md)
 - [V2OrganismQueryRequestTaxRankFilter](docs/V2OrganismQueryRequestTaxRankFilter.md)
 - [V2OrganismQueryRequestTaxonResourceFilter](docs/V2OrganismQueryRequestTaxonResourceFilter.md)
 - [V2OrthologRequest](docs/V2OrthologRequest.md)
 - [V2OrthologRequestContentType](docs/V2OrthologRequestContentType.md)
 - [V2ProkaryoteGeneRequest](docs/V2ProkaryoteGeneRequest.md)
 - [V2ProkaryoteGeneRequestGeneFlankConfig](docs/V2ProkaryoteGeneRequestGeneFlankConfig.md)
 - [V2Sars2ProteinDatasetRequest](docs/V2Sars2ProteinDatasetRequest.md)
 - [V2SciNameAndIds](docs/V2SciNameAndIds.md)
 - [V2SciNameAndIdsSciNameAndId](docs/V2SciNameAndIdsSciNameAndId.md)
 - [V2SequenceAccessionRequest](docs/V2SequenceAccessionRequest.md)
 - [V2SequenceReportPage](docs/V2SequenceReportPage.md)
 - [V2SortDirection](docs/V2SortDirection.md)
 - [V2SortField](docs/V2SortField.md)
 - [V2TableFormat](docs/V2TableFormat.md)
 - [V2TabularOutput](docs/V2TabularOutput.md)
 - [V2TaxonomyDatasetRequest](docs/V2TaxonomyDatasetRequest.md)
 - [V2TaxonomyDatasetRequestTaxonomyReportType](docs/V2TaxonomyDatasetRequestTaxonomyReportType.md)
 - [V2TaxonomyFilteredSubtreeRequest](docs/V2TaxonomyFilteredSubtreeRequest.md)
 - [V2TaxonomyFilteredSubtreeResponse](docs/V2TaxonomyFilteredSubtreeResponse.md)
 - [V2TaxonomyFilteredSubtreeResponseEdge](docs/V2TaxonomyFilteredSubtreeResponseEdge.md)
 - [V2TaxonomyFilteredSubtreeResponseEdgeChildStatus](docs/V2TaxonomyFilteredSubtreeResponseEdgeChildStatus.md)
 - [V2TaxonomyFilteredSubtreeResponseEdgesEntry](docs/V2TaxonomyFilteredSubtreeResponseEdgesEntry.md)
 - [V2TaxonomyImageMetadataRequest](docs/V2TaxonomyImageMetadataRequest.md)
 - [V2TaxonomyImageMetadataResponse](docs/V2TaxonomyImageMetadataResponse.md)
 - [V2TaxonomyImageRequest](docs/V2TaxonomyImageRequest.md)
 - [V2TaxonomyLinksRequest](docs/V2TaxonomyLinksRequest.md)
 - [V2TaxonomyLinksResponse](docs/V2TaxonomyLinksResponse.md)
 - [V2TaxonomyLinksResponseGenericLink](docs/V2TaxonomyLinksResponseGenericLink.md)
 - [V2TaxonomyMatch](docs/V2TaxonomyMatch.md)
 - [V2TaxonomyMetadataRequest](docs/V2TaxonomyMetadataRequest.md)
 - [V2TaxonomyMetadataRequestContentType](docs/V2TaxonomyMetadataRequestContentType.md)
 - [V2TaxonomyMetadataRequestTableFormat](docs/V2TaxonomyMetadataRequestTableFormat.md)
 - [V2TaxonomyMetadataResponse](docs/V2TaxonomyMetadataResponse.md)
 - [V2TaxonomyNode](docs/V2TaxonomyNode.md)
 - [V2TaxonomyNodeCountByType](docs/V2TaxonomyNodeCountByType.md)
 - [V2TaxonomyRelatedIdRequest](docs/V2TaxonomyRelatedIdRequest.md)
 - [V2TaxonomyTaxIdsPage](docs/V2TaxonomyTaxIdsPage.md)
 - [V2VersionReply](docs/V2VersionReply.md)
 - [V2ViralSequenceType](docs/V2ViralSequenceType.md)
 - [V2VirusAnnotationFilter](docs/V2VirusAnnotationFilter.md)
 - [V2VirusAnnotationReportRequest](docs/V2VirusAnnotationReportRequest.md)
 - [V2VirusAvailability](docs/V2VirusAvailability.md)
 - [V2VirusAvailabilityRequest](docs/V2VirusAvailabilityRequest.md)
 - [V2VirusDataReportRequest](docs/V2VirusDataReportRequest.md)
 - [V2VirusDataReportRequestContentType](docs/V2VirusDataReportRequestContentType.md)
 - [V2VirusDatasetFilter](docs/V2VirusDatasetFilter.md)
 - [V2VirusDatasetReportType](docs/V2VirusDatasetReportType.md)
 - [V2VirusDatasetRequest](docs/V2VirusDatasetRequest.md)
 - [V2VirusTableField](docs/V2VirusTableField.md)
 - [V2reportsANIMatch](docs/V2reportsANIMatch.md)
 - [V2reportsANITypeCategory](docs/V2reportsANITypeCategory.md)
 - [V2reportsAdditionalSubmitter](docs/V2reportsAdditionalSubmitter.md)
 - [V2reportsAnnotation](docs/V2reportsAnnotation.md)
 - [V2reportsAnnotationInfo](docs/V2reportsAnnotationInfo.md)
 - [V2reportsAssemblyDataReport](docs/V2reportsAssemblyDataReport.md)
 - [V2reportsAssemblyDataReportPage](docs/V2reportsAssemblyDataReportPage.md)
 - [V2reportsAssemblyInfo](docs/V2reportsAssemblyInfo.md)
 - [V2reportsAssemblyLevel](docs/V2reportsAssemblyLevel.md)
 - [V2reportsAssemblyRevision](docs/V2reportsAssemblyRevision.md)
 - [V2reportsAssemblyStats](docs/V2reportsAssemblyStats.md)
 - [V2reportsAssemblyStatus](docs/V2reportsAssemblyStatus.md)
 - [V2reportsAtypicalInfo](docs/V2reportsAtypicalInfo.md)
 - [V2reportsAverageNucleotideIdentity](docs/V2reportsAverageNucleotideIdentity.md)
 - [V2reportsAverageNucleotideIdentityMatchStatus](docs/V2reportsAverageNucleotideIdentityMatchStatus.md)
 - [V2reportsAverageNucleotideIdentityTaxonomyCheckStatus](docs/V2reportsAverageNucleotideIdentityTaxonomyCheckStatus.md)
 - [V2reportsBioProject](docs/V2reportsBioProject.md)
 - [V2reportsBioProjectLineage](docs/V2reportsBioProjectLineage.md)
 - [V2reportsBioSampleAttribute](docs/V2reportsBioSampleAttribute.md)
 - [V2reportsBioSampleContact](docs/V2reportsBioSampleContact.md)
 - [V2reportsBioSampleDataReport](docs/V2reportsBioSampleDataReport.md)
 - [V2reportsBioSampleDataReportPage](docs/V2reportsBioSampleDataReportPage.md)
 - [V2reportsBioSampleDescription](docs/V2reportsBioSampleDescription.md)
 - [V2reportsBioSampleDescriptor](docs/V2reportsBioSampleDescriptor.md)
 - [V2reportsBioSampleId](docs/V2reportsBioSampleId.md)
 - [V2reportsBioSampleOwner](docs/V2reportsBioSampleOwner.md)
 - [V2reportsBioSampleStatus](docs/V2reportsBioSampleStatus.md)
 - [V2reportsBuscoStat](docs/V2reportsBuscoStat.md)
 - [V2reportsCheckM](docs/V2reportsCheckM.md)
 - [V2reportsClassification](docs/V2reportsClassification.md)
 - [V2reportsCollectionType](docs/V2reportsCollectionType.md)
 - [V2reportsConservedDomain](docs/V2reportsConservedDomain.md)
 - [V2reportsContentType](docs/V2reportsContentType.md)
 - [V2reportsCountType](docs/V2reportsCountType.md)
 - [V2reportsError](docs/V2reportsError.md)
 - [V2reportsErrorAssemblyErrorCode](docs/V2reportsErrorAssemblyErrorCode.md)
 - [V2reportsErrorGeneErrorCode](docs/V2reportsErrorGeneErrorCode.md)
 - [V2reportsErrorOrganelleErrorCode](docs/V2reportsErrorOrganelleErrorCode.md)
 - [V2reportsErrorTaxonomyErrorCode](docs/V2reportsErrorTaxonomyErrorCode.md)
 - [V2reportsErrorVirusErrorCode](docs/V2reportsErrorVirusErrorCode.md)
 - [V2reportsFeatureCounts](docs/V2reportsFeatureCounts.md)
 - [V2reportsGeneCounts](docs/V2reportsGeneCounts.md)
 - [V2reportsGeneDataReportPage](docs/V2reportsGeneDataReportPage.md)
 - [V2reportsGeneDescriptor](docs/V2reportsGeneDescriptor.md)
 - [V2reportsGeneGroup](docs/V2reportsGeneGroup.md)
 - [V2reportsGeneOntology](docs/V2reportsGeneOntology.md)
 - [V2reportsGeneReportMatch](docs/V2reportsGeneReportMatch.md)
 - [V2reportsGeneSummary](docs/V2reportsGeneSummary.md)
 - [V2reportsGeneType](docs/V2reportsGeneType.md)
 - [V2reportsGenomeAnnotation](docs/V2reportsGenomeAnnotation.md)
 - [V2reportsGenomeAnnotationReportMatch](docs/V2reportsGenomeAnnotationReportMatch.md)
 - [V2reportsGenomeAnnotationReportPage](docs/V2reportsGenomeAnnotationReportPage.md)
 - [V2reportsGenomicLocation](docs/V2reportsGenomicLocation.md)
 - [V2reportsGenomicRegion](docs/V2reportsGenomicRegion.md)
 - [V2reportsGenomicRegionGenomicRegionType](docs/V2reportsGenomicRegionGenomicRegionType.md)
 - [V2reportsInfraspecificNames](docs/V2reportsInfraspecificNames.md)
 - [V2reportsIsolate](docs/V2reportsIsolate.md)
 - [V2reportsLineageOrganism](docs/V2reportsLineageOrganism.md)
 - [V2reportsLinkedAssembly](docs/V2reportsLinkedAssembly.md)
 - [V2reportsLinkedAssemblyType](docs/V2reportsLinkedAssemblyType.md)
 - [V2reportsMaturePeptide](docs/V2reportsMaturePeptide.md)
 - [V2reportsMessage](docs/V2reportsMessage.md)
 - [V2reportsNameAndAuthority](docs/V2reportsNameAndAuthority.md)
 - [V2reportsNameAndAuthorityNote](docs/V2reportsNameAndAuthorityNote.md)
 - [V2reportsNameAndAuthorityNoteClassifier](docs/V2reportsNameAndAuthorityNoteClassifier.md)
 - [V2reportsNameAndAuthorityPublication](docs/V2reportsNameAndAuthorityPublication.md)
 - [V2reportsNomenclatureAuthority](docs/V2reportsNomenclatureAuthority.md)
 - [V2reportsOrganelle](docs/V2reportsOrganelle.md)
 - [V2reportsOrganelleBiosample](docs/V2reportsOrganelleBiosample.md)
 - [V2reportsOrganelleDataReports](docs/V2reportsOrganelleDataReports.md)
 - [V2reportsOrganelleGeneCounts](docs/V2reportsOrganelleGeneCounts.md)
 - [V2reportsOrganelleInfo](docs/V2reportsOrganelleInfo.md)
 - [V2reportsOrganelleTopology](docs/V2reportsOrganelleTopology.md)
 - [V2reportsOrganelleType](docs/V2reportsOrganelleType.md)
 - [V2reportsOrganism](docs/V2reportsOrganism.md)
 - [V2reportsOrientation](docs/V2reportsOrientation.md)
 - [V2reportsPairedAssembly](docs/V2reportsPairedAssembly.md)
 - [V2reportsProcessMetadata](docs/V2reportsProcessMetadata.md)
 - [V2reportsProductDescriptor](docs/V2reportsProductDescriptor.md)
 - [V2reportsProtein](docs/V2reportsProtein.md)
 - [V2reportsPurposeOfSampling](docs/V2reportsPurposeOfSampling.md)
 - [V2reportsRange](docs/V2reportsRange.md)
 - [V2reportsRankType](docs/V2reportsRankType.md)
 - [V2reportsReference](docs/V2reportsReference.md)
 - [V2reportsRnaType](docs/V2reportsRnaType.md)
 - [V2reportsSeqRangeSet](docs/V2reportsSeqRangeSet.md)
 - [V2reportsSeqRangeSetFasta](docs/V2reportsSeqRangeSetFasta.md)
 - [V2reportsSequenceInfo](docs/V2reportsSequenceInfo.md)
 - [V2reportsSequenceInformation](docs/V2reportsSequenceInformation.md)
 - [V2reportsSourceDatabase](docs/V2reportsSourceDatabase.md)
 - [V2reportsTaxData](docs/V2reportsTaxData.md)
 - [V2reportsTaxonomyDataReportPage](docs/V2reportsTaxonomyDataReportPage.md)
 - [V2reportsTaxonomyNamesDataReportPage](docs/V2reportsTaxonomyNamesDataReportPage.md)
 - [V2reportsTaxonomyNamesDescriptor](docs/V2reportsTaxonomyNamesDescriptor.md)
 - [V2reportsTaxonomyNamesDescriptorCitation](docs/V2reportsTaxonomyNamesDescriptorCitation.md)
 - [V2reportsTaxonomyNamesReportMatch](docs/V2reportsTaxonomyNamesReportMatch.md)
 - [V2reportsTaxonomyNode](docs/V2reportsTaxonomyNode.md)
 - [V2reportsTaxonomyNodeCountByType](docs/V2reportsTaxonomyNodeCountByType.md)
 - [V2reportsTaxonomyReportMatch](docs/V2reportsTaxonomyReportMatch.md)
 - [V2reportsTaxonomyTypeMaterial](docs/V2reportsTaxonomyTypeMaterial.md)
 - [V2reportsTranscript](docs/V2reportsTranscript.md)
 - [V2reportsTranscriptSelectCategory](docs/V2reportsTranscriptSelectCategory.md)
 - [V2reportsTranscriptTranscriptType](docs/V2reportsTranscriptTranscriptType.md)
 - [V2reportsTranscriptTypeCount](docs/V2reportsTranscriptTypeCount.md)
 - [V2reportsTypeMaterial](docs/V2reportsTypeMaterial.md)
 - [V2reportsVirusAnnotationReport](docs/V2reportsVirusAnnotationReport.md)
 - [V2reportsVirusAnnotationReportPage](docs/V2reportsVirusAnnotationReportPage.md)
 - [V2reportsVirusAssembly](docs/V2reportsVirusAssembly.md)
 - [V2reportsVirusAssemblyCollectionLocation](docs/V2reportsVirusAssemblyCollectionLocation.md)
 - [V2reportsVirusAssemblyCompleteness](docs/V2reportsVirusAssemblyCompleteness.md)
 - [V2reportsVirusAssemblySubmitterInfo](docs/V2reportsVirusAssemblySubmitterInfo.md)
 - [V2reportsVirusDataReportPage](docs/V2reportsVirusDataReportPage.md)
 - [V2reportsVirusGene](docs/V2reportsVirusGene.md)
 - [V2reportsVirusPeptide](docs/V2reportsVirusPeptide.md)
 - [V2reportsVirusPeptideUniProtId](docs/V2reportsVirusPeptideUniProtId.md)
 - [V2reportsVirusPeptideViralPeptideCompleteness](docs/V2reportsVirusPeptideViralPeptideCompleteness.md)
 - [V2reportsWGSInfo](docs/V2reportsWGSInfo.md)
 - [V2reportsWarning](docs/V2reportsWarning.md)
 - [V2reportsWarningGeneWarningCode](docs/V2reportsWarningGeneWarningCode.md)
 - [V2reportsWarningReplacedId](docs/V2reportsWarningReplacedId.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="ApiKeyAuth"></a>
### ApiKeyAuth

- **Type**: API key
- **API key parameter name**: api_key
- **Location**: URL query string

<a id="ApiKeyAuthHeader"></a>
### ApiKeyAuthHeader

- **Type**: API key
- **API key parameter name**: api-key
- **Location**: HTTP header


## Author

help@ncbi.nlm.nih.gov


