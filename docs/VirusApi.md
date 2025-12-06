# ncbi.datasets.openapi.VirusApi

All URIs are relative to *https://api.ncbi.nlm.nih.gov/datasets/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sars2_protein_download**](VirusApi.md#sars2_protein_download) | **GET** /virus/taxon/sars2/protein/{proteins}/download | Get a SARS-CoV-2 protein data package by protein name
[**sars2_protein_download_post**](VirusApi.md#sars2_protein_download_post) | **POST** /virus/taxon/sars2/protein/download | Get a SARS-CoV-2 protein data package
[**sars2_protein_summary**](VirusApi.md#sars2_protein_summary) | **GET** /virus/taxon/sars2/protein/{proteins} | Get a download summary of a SARS-CoV-2 protein data package by protein name
[**sars2_protein_summary_by_post**](VirusApi.md#sars2_protein_summary_by_post) | **POST** /virus/taxon/sars2/protein | Get a download summary of a SARS-CoV-2 protein data package by protein name
[**sars2_protein_table**](VirusApi.md#sars2_protein_table) | **GET** /virus/taxon/sars2/protein/{proteins}/table | Get SARS-CoV-2 protein metadata in a tabular format by protein name
[**virus_accession_availability**](VirusApi.md#virus_accession_availability) | **GET** /virus/accession/{accessions}/check | Check the validity of a virus genome nucleotide accession
[**virus_accession_availability_post**](VirusApi.md#virus_accession_availability_post) | **POST** /virus/check | Check the validity of a virus genome nucleotide accession
[**virus_annotation_reports_by_acessions**](VirusApi.md#virus_annotation_reports_by_acessions) | **GET** /virus/accession/{accessions}/annotation_report | Get a virus annotation report by nucleotide accession
[**virus_annotation_reports_by_post**](VirusApi.md#virus_annotation_reports_by_post) | **POST** /virus/annotation_report | Get a virus annotation report
[**virus_annotation_reports_by_taxon**](VirusApi.md#virus_annotation_reports_by_taxon) | **GET** /virus/taxon/{taxon}/annotation_report | Get a virus annotation report by taxon
[**virus_genome_download**](VirusApi.md#virus_genome_download) | **GET** /virus/taxon/{taxon}/genome/download | Get a virus genome data package by taxon
[**virus_genome_download_accession**](VirusApi.md#virus_genome_download_accession) | **GET** /virus/accession/{accessions}/genome/download | Get a virus genome data package by nucleotide accession
[**virus_genome_download_post**](VirusApi.md#virus_genome_download_post) | **POST** /virus/genome/download | Get a virus genome data package
[**virus_genome_summary**](VirusApi.md#virus_genome_summary) | **GET** /virus/taxon/{taxon}/genome | Get a download summary of a virus genome data package by taxon
[**virus_genome_summary_by_post**](VirusApi.md#virus_genome_summary_by_post) | **POST** /virus/genome | Get a download summary of a virus genome data package
[**virus_genome_table**](VirusApi.md#virus_genome_table) | **GET** /virus/taxon/{taxon}/genome/table | Get virus genome metadata in a tabular format (deprecated)
[**virus_reports_by_acessions**](VirusApi.md#virus_reports_by_acessions) | **GET** /virus/accession/{accessions}/dataset_report | Get a virus data report by nucleotide accession
[**virus_reports_by_post**](VirusApi.md#virus_reports_by_post) | **POST** /virus | Get a virus data report
[**virus_reports_by_taxon**](VirusApi.md#virus_reports_by_taxon) | **GET** /virus/taxon/{taxon}/dataset_report | Get a virus data report by taxon


# **sars2_protein_download**
> bytearray sars2_protein_download(proteins, refseq_only=refseq_only, annotated_only=annotated_only, released_since=released_since, updated_since=updated_since, host=host, pangolin_classification=pangolin_classification, geo_location=geo_location, usa_state=usa_state, complete_only=complete_only, include_sequence=include_sequence, aux_report=aux_report, filename=filename)

Get a SARS-CoV-2 protein data package by protein name

Download a SARS-CoV-2 protein data package including sequence, annotation, BioSample data and a detailed data report by protein name.

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_viral_sequence_type import V2ViralSequenceType
from ncbi.datasets.openapi.models.v2_virus_dataset_report_type import V2VirusDatasetReportType
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
    api_instance = ncbi.datasets.openapi.VirusApi(api_client)
    proteins = ['spike protein'] # List[str] | One or more SARS-CoV-2 protein names
    refseq_only = False # bool | If true, limit results to RefSeq genomes. (optional) (default to False)
    annotated_only = False # bool | If true, limit results to annotated genomes. (optional) (default to False)
    released_since = '2025-01-15' # datetime | Limit to genomes released on or after the specified date. (optional)
    updated_since = '2025-01-15' # datetime | Limit to genomes updated on or after the specified date. (optional)
    host = '9606' # str | Limit to genomes isolated from the specified host species (NCBI Taxonomy ID, common or scientific name). (optional)
    pangolin_classification = 'LP.8.1' # str | Limit to SARS-CoV-2 genomes with the specified Pango lineage. (optional)
    geo_location = 'USA' # str | Limit to genomes collected from the specififed geographic location. (optional)
    usa_state = 'CA' # str | Limit to genomes collected from the specified U.S. state (two-letter abbreviation). (optional)
    complete_only = False # bool | Limit to genomes designated as complete, as defined by the submitter. (optional) (default to False)
    include_sequence = [ncbi.datasets.openapi.V2ViralSequenceType()] # List[V2ViralSequenceType] | Specify which sequence files to include in the data package. (optional)
    aux_report = [ncbi.datasets.openapi.V2VirusDatasetReportType()] # List[V2VirusDatasetReportType] | Specify which report files to include in the data package. The virus data report is always included, and its inclusion is not affected by this parameter. (optional)
    filename = 'ncbi_dataset.zip' # str | Output file name. (optional) (default to 'ncbi_dataset.zip')

    try:
        # Get a SARS-CoV-2 protein data package by protein name
        api_response = api_instance.sars2_protein_download(proteins, refseq_only=refseq_only, annotated_only=annotated_only, released_since=released_since, updated_since=updated_since, host=host, pangolin_classification=pangolin_classification, geo_location=geo_location, usa_state=usa_state, complete_only=complete_only, include_sequence=include_sequence, aux_report=aux_report, filename=filename)
        print("The response of VirusApi->sars2_protein_download:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirusApi->sars2_protein_download: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proteins** | [**List[str]**](str.md)| One or more SARS-CoV-2 protein names | 
 **refseq_only** | **bool**| If true, limit results to RefSeq genomes. | [optional] [default to False]
 **annotated_only** | **bool**| If true, limit results to annotated genomes. | [optional] [default to False]
 **released_since** | **datetime**| Limit to genomes released on or after the specified date. | [optional] 
 **updated_since** | **datetime**| Limit to genomes updated on or after the specified date. | [optional] 
 **host** | **str**| Limit to genomes isolated from the specified host species (NCBI Taxonomy ID, common or scientific name). | [optional] 
 **pangolin_classification** | **str**| Limit to SARS-CoV-2 genomes with the specified Pango lineage. | [optional] 
 **geo_location** | **str**| Limit to genomes collected from the specififed geographic location. | [optional] 
 **usa_state** | **str**| Limit to genomes collected from the specified U.S. state (two-letter abbreviation). | [optional] 
 **complete_only** | **bool**| Limit to genomes designated as complete, as defined by the submitter. | [optional] [default to False]
 **include_sequence** | [**List[V2ViralSequenceType]**](V2ViralSequenceType.md)| Specify which sequence files to include in the data package. | [optional] 
 **aux_report** | [**List[V2VirusDatasetReportType]**](V2VirusDatasetReportType.md)| Specify which report files to include in the data package. The virus data report is always included, and its inclusion is not affected by this parameter. | [optional] 
 **filename** | **str**| Output file name. | [optional] [default to &#39;ncbi_dataset.zip&#39;]

### Return type

**bytearray**

### Authorization

[ApiKeyAuthHeader](../README.md#ApiKeyAuthHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/zip

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sars2_protein_download_post**
> bytearray sars2_protein_download_post(v2_sars2_protein_dataset_request, filename=filename)

Get a SARS-CoV-2 protein data package

Download a SARS-CoV-2 protein data package including sequence, annotation, BioSample data and a detailed data report.

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_sars2_protein_dataset_request import V2Sars2ProteinDatasetRequest
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
    api_instance = ncbi.datasets.openapi.VirusApi(api_client)
    v2_sars2_protein_dataset_request = {"proteins":["spike"],"refseq_only":true,"include_sequence":["PROTEIN"]} # V2Sars2ProteinDatasetRequest | 
    filename = 'ncbi_dataset.zip' # str | Output file name. (optional) (default to 'ncbi_dataset.zip')

    try:
        # Get a SARS-CoV-2 protein data package
        api_response = api_instance.sars2_protein_download_post(v2_sars2_protein_dataset_request, filename=filename)
        print("The response of VirusApi->sars2_protein_download_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirusApi->sars2_protein_download_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v2_sars2_protein_dataset_request** | [**V2Sars2ProteinDatasetRequest**](V2Sars2ProteinDatasetRequest.md)|  | 
 **filename** | **str**| Output file name. | [optional] [default to &#39;ncbi_dataset.zip&#39;]

### Return type

**bytearray**

### Authorization

[ApiKeyAuthHeader](../README.md#ApiKeyAuthHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/zip

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sars2_protein_summary**
> V2DownloadSummary sars2_protein_summary(proteins, refseq_only=refseq_only, annotated_only=annotated_only, released_since=released_since, updated_since=updated_since, host=host, pangolin_classification=pangolin_classification, geo_location=geo_location, usa_state=usa_state, complete_only=complete_only, include_sequence=include_sequence, aux_report=aux_report)

Get a download summary of a SARS-CoV-2 protein data package by protein name

Get a download summary of a SARS-CoV-2 protein data package, including counts and file sizes, in JSON format.

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_download_summary import V2DownloadSummary
from ncbi.datasets.openapi.models.v2_viral_sequence_type import V2ViralSequenceType
from ncbi.datasets.openapi.models.v2_virus_dataset_report_type import V2VirusDatasetReportType
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
    api_instance = ncbi.datasets.openapi.VirusApi(api_client)
    proteins = ['spike protein'] # List[str] | One or more SARS-CoV-2 protein names
    refseq_only = False # bool | If true, limit results to RefSeq genomes. (optional) (default to False)
    annotated_only = False # bool | If true, limit results to annotated genomes. (optional) (default to False)
    released_since = '2025-01-15' # datetime | Limit to genomes released on or after the specified date. (optional)
    updated_since = '2025-01-15' # datetime | Limit to genomes updated on or after the specified date. (optional)
    host = '9606' # str | Limit to genomes isolated from the specified host species (NCBI Taxonomy ID, common or scientific name). (optional)
    pangolin_classification = 'LP.8.1' # str | Limit to SARS-CoV-2 genomes with the specified Pango lineage. (optional)
    geo_location = 'USA' # str | Limit to genomes collected from the specififed geographic location. (optional)
    usa_state = 'CA' # str | Limit to genomes collected from the specified U.S. state (two-letter abbreviation). (optional)
    complete_only = False # bool | Limit to genomes designated as complete, as defined by the submitter. (optional) (default to False)
    include_sequence = [ncbi.datasets.openapi.V2ViralSequenceType()] # List[V2ViralSequenceType] | Specify which sequence files to include in the data package. (optional)
    aux_report = [ncbi.datasets.openapi.V2VirusDatasetReportType()] # List[V2VirusDatasetReportType] | Specify which report files to include in the data package. The virus data report is always included, and its inclusion is not affected by this parameter. (optional)

    try:
        # Get a download summary of a SARS-CoV-2 protein data package by protein name
        api_response = api_instance.sars2_protein_summary(proteins, refseq_only=refseq_only, annotated_only=annotated_only, released_since=released_since, updated_since=updated_since, host=host, pangolin_classification=pangolin_classification, geo_location=geo_location, usa_state=usa_state, complete_only=complete_only, include_sequence=include_sequence, aux_report=aux_report)
        print("The response of VirusApi->sars2_protein_summary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirusApi->sars2_protein_summary: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proteins** | [**List[str]**](str.md)| One or more SARS-CoV-2 protein names | 
 **refseq_only** | **bool**| If true, limit results to RefSeq genomes. | [optional] [default to False]
 **annotated_only** | **bool**| If true, limit results to annotated genomes. | [optional] [default to False]
 **released_since** | **datetime**| Limit to genomes released on or after the specified date. | [optional] 
 **updated_since** | **datetime**| Limit to genomes updated on or after the specified date. | [optional] 
 **host** | **str**| Limit to genomes isolated from the specified host species (NCBI Taxonomy ID, common or scientific name). | [optional] 
 **pangolin_classification** | **str**| Limit to SARS-CoV-2 genomes with the specified Pango lineage. | [optional] 
 **geo_location** | **str**| Limit to genomes collected from the specififed geographic location. | [optional] 
 **usa_state** | **str**| Limit to genomes collected from the specified U.S. state (two-letter abbreviation). | [optional] 
 **complete_only** | **bool**| Limit to genomes designated as complete, as defined by the submitter. | [optional] [default to False]
 **include_sequence** | [**List[V2ViralSequenceType]**](V2ViralSequenceType.md)| Specify which sequence files to include in the data package. | [optional] 
 **aux_report** | [**List[V2VirusDatasetReportType]**](V2VirusDatasetReportType.md)| Specify which report files to include in the data package. The virus data report is always included, and its inclusion is not affected by this parameter. | [optional] 

### Return type

[**V2DownloadSummary**](V2DownloadSummary.md)

### Authorization

[ApiKeyAuthHeader](../README.md#ApiKeyAuthHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sars2_protein_summary_by_post**
> V2DownloadSummary sars2_protein_summary_by_post(v2_sars2_protein_dataset_request)

Get a download summary of a SARS-CoV-2 protein data package by protein name

Get a download summary of a SARS-CoV-2 protein data package, including counts and file sizes, in JSON format.

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_download_summary import V2DownloadSummary
from ncbi.datasets.openapi.models.v2_sars2_protein_dataset_request import V2Sars2ProteinDatasetRequest
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
    api_instance = ncbi.datasets.openapi.VirusApi(api_client)
    v2_sars2_protein_dataset_request = {"proteins":["spike"],"refseq_only":true,"include_sequence":["PROTEIN"]} # V2Sars2ProteinDatasetRequest | 

    try:
        # Get a download summary of a SARS-CoV-2 protein data package by protein name
        api_response = api_instance.sars2_protein_summary_by_post(v2_sars2_protein_dataset_request)
        print("The response of VirusApi->sars2_protein_summary_by_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirusApi->sars2_protein_summary_by_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v2_sars2_protein_dataset_request** | [**V2Sars2ProteinDatasetRequest**](V2Sars2ProteinDatasetRequest.md)|  | 

### Return type

[**V2DownloadSummary**](V2DownloadSummary.md)

### Authorization

[ApiKeyAuthHeader](../README.md#ApiKeyAuthHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sars2_protein_table**
> V2TabularOutput sars2_protein_table(proteins, refseq_only=refseq_only, annotated_only=annotated_only, released_since=released_since, updated_since=updated_since, host=host, pangolin_classification=pangolin_classification, geo_location=geo_location, usa_state=usa_state, complete_only=complete_only, table_fields=table_fields, format=format)

Get SARS-CoV-2 protein metadata in a tabular format by protein name

Get SARS-CoV-2 protein metadata in a tabular format by protein name.

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_table_format import V2TableFormat
from ncbi.datasets.openapi.models.v2_tabular_output import V2TabularOutput
from ncbi.datasets.openapi.models.v2_virus_table_field import V2VirusTableField
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
    api_instance = ncbi.datasets.openapi.VirusApi(api_client)
    proteins = ['spike protein'] # List[str] | One or more SARS-CoV-2 protein names
    refseq_only = False # bool | If true, limit results to RefSeq genomes. (optional) (default to False)
    annotated_only = False # bool | If true, limit results to annotated genomes. (optional) (default to False)
    released_since = '2025-01-15' # datetime | Limit to genomes released on or after the specified date. (optional)
    updated_since = '2025-01-15' # datetime | Limit to genomes updated on or after the specified date. (optional)
    host = '9606' # str | Limit to genomes isolated from the specified host species (NCBI Taxonomy ID, common or scientific name). (optional)
    pangolin_classification = 'LP.8.1' # str | Limit to SARS-CoV-2 genomes with the specified Pango lineage. (optional)
    geo_location = 'USA' # str | Limit to genomes collected from the specififed geographic location. (optional)
    usa_state = 'CA' # str | Limit to genomes collected from the specified U.S. state (two-letter abbreviation). (optional)
    complete_only = False # bool | Limit to genomes designated as complete, as defined by the submitter. (optional) (default to False)
    table_fields = [ncbi.datasets.openapi.V2VirusTableField()] # List[V2VirusTableField] | Specify which fields to include in the tabular report (optional)
    format = tsv # V2TableFormat | Specify output format (optional) (default to tsv)

    try:
        # Get SARS-CoV-2 protein metadata in a tabular format by protein name
        api_response = api_instance.sars2_protein_table(proteins, refseq_only=refseq_only, annotated_only=annotated_only, released_since=released_since, updated_since=updated_since, host=host, pangolin_classification=pangolin_classification, geo_location=geo_location, usa_state=usa_state, complete_only=complete_only, table_fields=table_fields, format=format)
        print("The response of VirusApi->sars2_protein_table:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirusApi->sars2_protein_table: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proteins** | [**List[str]**](str.md)| One or more SARS-CoV-2 protein names | 
 **refseq_only** | **bool**| If true, limit results to RefSeq genomes. | [optional] [default to False]
 **annotated_only** | **bool**| If true, limit results to annotated genomes. | [optional] [default to False]
 **released_since** | **datetime**| Limit to genomes released on or after the specified date. | [optional] 
 **updated_since** | **datetime**| Limit to genomes updated on or after the specified date. | [optional] 
 **host** | **str**| Limit to genomes isolated from the specified host species (NCBI Taxonomy ID, common or scientific name). | [optional] 
 **pangolin_classification** | **str**| Limit to SARS-CoV-2 genomes with the specified Pango lineage. | [optional] 
 **geo_location** | **str**| Limit to genomes collected from the specififed geographic location. | [optional] 
 **usa_state** | **str**| Limit to genomes collected from the specified U.S. state (two-letter abbreviation). | [optional] 
 **complete_only** | **bool**| Limit to genomes designated as complete, as defined by the submitter. | [optional] [default to False]
 **table_fields** | [**List[V2VirusTableField]**](V2VirusTableField.md)| Specify which fields to include in the tabular report | [optional] 
 **format** | [**V2TableFormat**](.md)| Specify output format | [optional] [default to tsv]

### Return type

[**V2TabularOutput**](V2TabularOutput.md)

### Authorization

[ApiKeyAuthHeader](../README.md#ApiKeyAuthHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virus_accession_availability**
> V2VirusAvailability virus_accession_availability(accessions)

Check the validity of a virus genome nucleotide accession

Check the validity of a virus genome nucleotide accession. Output in JSON format.

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_virus_availability import V2VirusAvailability
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
    api_instance = ncbi.datasets.openapi.VirusApi(api_client)
    accessions = ['NC_038294.1'] # List[str] | virus accessions

    try:
        # Check the validity of a virus genome nucleotide accession
        api_response = api_instance.virus_accession_availability(accessions)
        print("The response of VirusApi->virus_accession_availability:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirusApi->virus_accession_availability: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accessions** | [**List[str]**](str.md)| virus accessions | 

### Return type

[**V2VirusAvailability**](V2VirusAvailability.md)

### Authorization

[ApiKeyAuthHeader](../README.md#ApiKeyAuthHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virus_accession_availability_post**
> V2VirusAvailability virus_accession_availability_post(v2_virus_availability_request)

Check the validity of a virus genome nucleotide accession

Check the validity of a virus genome nucleotide accession. Output in JSON format.

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_virus_availability import V2VirusAvailability
from ncbi.datasets.openapi.models.v2_virus_availability_request import V2VirusAvailabilityRequest
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
    api_instance = ncbi.datasets.openapi.VirusApi(api_client)
    v2_virus_availability_request = {"accessions":["NC_038294.1"]} # V2VirusAvailabilityRequest | 

    try:
        # Check the validity of a virus genome nucleotide accession
        api_response = api_instance.virus_accession_availability_post(v2_virus_availability_request)
        print("The response of VirusApi->virus_accession_availability_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirusApi->virus_accession_availability_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v2_virus_availability_request** | [**V2VirusAvailabilityRequest**](V2VirusAvailabilityRequest.md)|  | 

### Return type

[**V2VirusAvailability**](V2VirusAvailability.md)

### Authorization

[ApiKeyAuthHeader](../README.md#ApiKeyAuthHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virus_annotation_reports_by_acessions**
> V2reportsVirusAnnotationReportPage virus_annotation_reports_by_acessions(accessions, filter_refseq_only=filter_refseq_only, filter_annotated_only=filter_annotated_only, filter_released_since=filter_released_since, filter_updated_since=filter_updated_since, filter_host=filter_host, filter_pangolin_classification=filter_pangolin_classification, filter_geo_location=filter_geo_location, filter_usa_state=filter_usa_state, filter_complete_only=filter_complete_only, table_fields=table_fields, page_size=page_size, page_token=page_token)

Get a virus annotation report by nucleotide accession

Get a virus annotation report by nucleotide accesion. By default, in paged JSON format, but also available in tabular (accept: text/tab-separated-values) or JSON Lines (accept: application/x-ndjson) formats.

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2reports_virus_annotation_report_page import V2reportsVirusAnnotationReportPage
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
    api_instance = ncbi.datasets.openapi.VirusApi(api_client)
    accessions = ['NC_038294.1'] # List[str] | One or more nucleotide sequence accessions
    filter_refseq_only = False # bool | If true, limit to RefSeq genomes. (optional) (default to False)
    filter_annotated_only = False # bool | If true, limit to annotated genomes. (optional) (default to False)
    filter_released_since = '2025-01-15' # datetime | Limit to genomes released on or after the specified date. (optional)
    filter_updated_since = '2025-01-15' # datetime | Limit to genomes updated on or after the specified date. (optional)
    filter_host = '9606' # str | Limit to genomes isolated from the specified host species (NCBI Taxonomy ID, common or scientific name). (optional)
    filter_pangolin_classification = 'LP.8.1' # str | Limit to SARS-CoV-2 genomes from the specified Pango lineage. (optional)
    filter_geo_location = 'USA' # str | Limit to genomes collected from the specififed geographic location. (optional)
    filter_usa_state = 'CA' # str | Limit to genomes collected from the specified U.S. state (two-letter abbreviation). (optional)
    filter_complete_only = False # bool | Limit to genomes designated as complete, as defined by the submitter. (optional) (default to False)
    table_fields = ['[\"accession\",\"gene-cds-name\",\"gene-cds-nuc-fasta-range-start\",\"gene-cds-nuc-fasta-range-stop\"]'] # List[str] | Specify which fields to include in the tabular report. Additional fields are described here: [virus annotation report fields](https://www.ncbi.nlm.nih.gov/datasets/docs/v2/command-line-tools/using-dataformat/virus-data-reports/#virus-annotation-report-fields). Use of this parameter requires the HTTP header, `accept: text/tab-separated-values`. (optional)
    page_size = 20 # int | The maximum number of virus data reports to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, `page_token` can be used to retrieve the remaining results. (optional) (default to 20)
    page_token = 'page_token_example' # str | A page token is returned when the results count exceeds `page size`. Use this token along with previous request parameters to retrieve the next page of results. When `page_token` is empty, all results have been retrieved. (optional)

    try:
        # Get a virus annotation report by nucleotide accession
        api_response = api_instance.virus_annotation_reports_by_acessions(accessions, filter_refseq_only=filter_refseq_only, filter_annotated_only=filter_annotated_only, filter_released_since=filter_released_since, filter_updated_since=filter_updated_since, filter_host=filter_host, filter_pangolin_classification=filter_pangolin_classification, filter_geo_location=filter_geo_location, filter_usa_state=filter_usa_state, filter_complete_only=filter_complete_only, table_fields=table_fields, page_size=page_size, page_token=page_token)
        print("The response of VirusApi->virus_annotation_reports_by_acessions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirusApi->virus_annotation_reports_by_acessions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accessions** | [**List[str]**](str.md)| One or more nucleotide sequence accessions | 
 **filter_refseq_only** | **bool**| If true, limit to RefSeq genomes. | [optional] [default to False]
 **filter_annotated_only** | **bool**| If true, limit to annotated genomes. | [optional] [default to False]
 **filter_released_since** | **datetime**| Limit to genomes released on or after the specified date. | [optional] 
 **filter_updated_since** | **datetime**| Limit to genomes updated on or after the specified date. | [optional] 
 **filter_host** | **str**| Limit to genomes isolated from the specified host species (NCBI Taxonomy ID, common or scientific name). | [optional] 
 **filter_pangolin_classification** | **str**| Limit to SARS-CoV-2 genomes from the specified Pango lineage. | [optional] 
 **filter_geo_location** | **str**| Limit to genomes collected from the specififed geographic location. | [optional] 
 **filter_usa_state** | **str**| Limit to genomes collected from the specified U.S. state (two-letter abbreviation). | [optional] 
 **filter_complete_only** | **bool**| Limit to genomes designated as complete, as defined by the submitter. | [optional] [default to False]
 **table_fields** | [**List[str]**](str.md)| Specify which fields to include in the tabular report. Additional fields are described here: [virus annotation report fields](https://www.ncbi.nlm.nih.gov/datasets/docs/v2/command-line-tools/using-dataformat/virus-data-reports/#virus-annotation-report-fields). Use of this parameter requires the HTTP header, &#x60;accept: text/tab-separated-values&#x60;. | [optional] 
 **page_size** | **int**| The maximum number of virus data reports to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, &#x60;page_token&#x60; can be used to retrieve the remaining results. | [optional] [default to 20]
 **page_token** | **str**| A page token is returned when the results count exceeds &#x60;page size&#x60;. Use this token along with previous request parameters to retrieve the next page of results. When &#x60;page_token&#x60; is empty, all results have been retrieved. | [optional] 

### Return type

[**V2reportsVirusAnnotationReportPage**](V2reportsVirusAnnotationReportPage.md)

### Authorization

[ApiKeyAuthHeader](../README.md#ApiKeyAuthHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, application/x-ndjson, text/tab-separated-values

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virus_annotation_reports_by_post**
> V2reportsVirusAnnotationReportPage virus_annotation_reports_by_post(v2_virus_annotation_report_request)

Get a virus annotation report

Get a virus annotation report. By default, in paged JSON format, but also available in tabular (accept: text/tab-separated-values) or JSON Lines (accept: application/x-ndjson) formats.

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_virus_annotation_report_request import V2VirusAnnotationReportRequest
from ncbi.datasets.openapi.models.v2reports_virus_annotation_report_page import V2reportsVirusAnnotationReportPage
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
    api_instance = ncbi.datasets.openapi.VirusApi(api_client)
    v2_virus_annotation_report_request = {"filter":{"taxons":["1335626"],"refseq_only":true}} # V2VirusAnnotationReportRequest | 

    try:
        # Get a virus annotation report
        api_response = api_instance.virus_annotation_reports_by_post(v2_virus_annotation_report_request)
        print("The response of VirusApi->virus_annotation_reports_by_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirusApi->virus_annotation_reports_by_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v2_virus_annotation_report_request** | [**V2VirusAnnotationReportRequest**](V2VirusAnnotationReportRequest.md)|  | 

### Return type

[**V2reportsVirusAnnotationReportPage**](V2reportsVirusAnnotationReportPage.md)

### Authorization

[ApiKeyAuthHeader](../README.md#ApiKeyAuthHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json, application/x-ndjson, text/tab-separated-values

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virus_annotation_reports_by_taxon**
> V2reportsVirusAnnotationReportPage virus_annotation_reports_by_taxon(taxon, filter_refseq_only=filter_refseq_only, filter_annotated_only=filter_annotated_only, filter_released_since=filter_released_since, filter_updated_since=filter_updated_since, filter_host=filter_host, filter_pangolin_classification=filter_pangolin_classification, filter_geo_location=filter_geo_location, filter_usa_state=filter_usa_state, filter_complete_only=filter_complete_only, table_fields=table_fields, page_size=page_size, page_token=page_token)

Get a virus annotation report by taxon

Get virus annotation report by taxon. By default, in paged JSON format, but also available in tabular (accept: text/tab-separated-values) or JSON Lines (accept: application/x-ndjson) formats.

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2reports_virus_annotation_report_page import V2reportsVirusAnnotationReportPage
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
    api_instance = ncbi.datasets.openapi.VirusApi(api_client)
    taxon = '1335626' # str | NCBI Taxonomy ID or name (common or scientific) at any taxonomic rank
    filter_refseq_only = False # bool | If true, limit to RefSeq genomes. (optional) (default to False)
    filter_annotated_only = False # bool | If true, limit to annotated genomes. (optional) (default to False)
    filter_released_since = '2025-01-15' # datetime | Limit to genomes released on or after the specified date. (optional)
    filter_updated_since = '2025-01-15' # datetime | Limit to genomes updated on or after the specified date. (optional)
    filter_host = '9606' # str | Limit to genomes isolated from the specified host species (NCBI Taxonomy ID, common or scientific name). (optional)
    filter_pangolin_classification = 'LP.8.1' # str | Limit to SARS-CoV-2 genomes from the specified Pango lineage. (optional)
    filter_geo_location = 'USA' # str | Limit to genomes collected from the specififed geographic location. (optional)
    filter_usa_state = 'CA' # str | Limit to genomes collected from the specified U.S. state (two-letter abbreviation). (optional)
    filter_complete_only = False # bool | Limit to genomes designated as complete, as defined by the submitter. (optional) (default to False)
    table_fields = ['[\"accession\",\"gene-cds-name\",\"gene-cds-nuc-fasta-range-start\",\"gene-cds-nuc-fasta-range-stop\"]'] # List[str] | Specify which fields to include in the tabular report. Additional fields are described here: [virus annotation report fields](https://www.ncbi.nlm.nih.gov/datasets/docs/v2/command-line-tools/using-dataformat/virus-data-reports/#virus-annotation-report-fields). Use of this parameter requires the HTTP header, `accept: text/tab-separated-values`. (optional)
    page_size = 20 # int | The maximum number of virus data reports to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, `page_token` can be used to retrieve the remaining results. (optional) (default to 20)
    page_token = 'page_token_example' # str | A page token is returned when the results count exceeds `page size`. Use this token along with previous request parameters to retrieve the next page of results. When `page_token` is empty, all results have been retrieved. (optional)

    try:
        # Get a virus annotation report by taxon
        api_response = api_instance.virus_annotation_reports_by_taxon(taxon, filter_refseq_only=filter_refseq_only, filter_annotated_only=filter_annotated_only, filter_released_since=filter_released_since, filter_updated_since=filter_updated_since, filter_host=filter_host, filter_pangolin_classification=filter_pangolin_classification, filter_geo_location=filter_geo_location, filter_usa_state=filter_usa_state, filter_complete_only=filter_complete_only, table_fields=table_fields, page_size=page_size, page_token=page_token)
        print("The response of VirusApi->virus_annotation_reports_by_taxon:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirusApi->virus_annotation_reports_by_taxon: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **taxon** | **str**| NCBI Taxonomy ID or name (common or scientific) at any taxonomic rank | 
 **filter_refseq_only** | **bool**| If true, limit to RefSeq genomes. | [optional] [default to False]
 **filter_annotated_only** | **bool**| If true, limit to annotated genomes. | [optional] [default to False]
 **filter_released_since** | **datetime**| Limit to genomes released on or after the specified date. | [optional] 
 **filter_updated_since** | **datetime**| Limit to genomes updated on or after the specified date. | [optional] 
 **filter_host** | **str**| Limit to genomes isolated from the specified host species (NCBI Taxonomy ID, common or scientific name). | [optional] 
 **filter_pangolin_classification** | **str**| Limit to SARS-CoV-2 genomes from the specified Pango lineage. | [optional] 
 **filter_geo_location** | **str**| Limit to genomes collected from the specififed geographic location. | [optional] 
 **filter_usa_state** | **str**| Limit to genomes collected from the specified U.S. state (two-letter abbreviation). | [optional] 
 **filter_complete_only** | **bool**| Limit to genomes designated as complete, as defined by the submitter. | [optional] [default to False]
 **table_fields** | [**List[str]**](str.md)| Specify which fields to include in the tabular report. Additional fields are described here: [virus annotation report fields](https://www.ncbi.nlm.nih.gov/datasets/docs/v2/command-line-tools/using-dataformat/virus-data-reports/#virus-annotation-report-fields). Use of this parameter requires the HTTP header, &#x60;accept: text/tab-separated-values&#x60;. | [optional] 
 **page_size** | **int**| The maximum number of virus data reports to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, &#x60;page_token&#x60; can be used to retrieve the remaining results. | [optional] [default to 20]
 **page_token** | **str**| A page token is returned when the results count exceeds &#x60;page size&#x60;. Use this token along with previous request parameters to retrieve the next page of results. When &#x60;page_token&#x60; is empty, all results have been retrieved. | [optional] 

### Return type

[**V2reportsVirusAnnotationReportPage**](V2reportsVirusAnnotationReportPage.md)

### Authorization

[ApiKeyAuthHeader](../README.md#ApiKeyAuthHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, application/x-ndjson, text/tab-separated-values

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virus_genome_download**
> bytearray virus_genome_download(taxon, refseq_only=refseq_only, annotated_only=annotated_only, released_since=released_since, updated_since=updated_since, host=host, pangolin_classification=pangolin_classification, geo_location=geo_location, usa_state=usa_state, complete_only=complete_only, include_sequence=include_sequence, aux_report=aux_report, use_psg=use_psg, filename=filename)

Get a virus genome data package by taxon

Download a virus genome data package including sequence, annotation, BioSample data and a detailed data report by taxon.

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_viral_sequence_type import V2ViralSequenceType
from ncbi.datasets.openapi.models.v2_virus_dataset_report_type import V2VirusDatasetReportType
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
    api_instance = ncbi.datasets.openapi.VirusApi(api_client)
    taxon = '1335626' # str | NCBI Taxonomy ID or name (common or scientific) at any taxonomic rank
    refseq_only = False # bool | If true, limit results to RefSeq genomes. (optional) (default to False)
    annotated_only = False # bool | If true, limit results to annotated genomes. (optional) (default to False)
    released_since = '2025-01-15' # datetime | Limit to genomes released on or after the specified date. (optional)
    updated_since = '2025-01-15' # datetime | Limit to genomes updated on or after the specified date. (optional)
    host = '9606' # str | Limit to genomes isolated from the specified host species (NCBI Taxonomy ID, common or scientific name). (optional)
    pangolin_classification = 'LP.8.1' # str | Limit to SARS-CoV-2 genomes from the specified Pango lineage. (optional)
    geo_location = 'USA' # str | Limit to genomes collected from the specified geographic location. (optional)
    usa_state = 'CA' # str | Limit to genomes collected from the specified U.S. state (two-letter abbreviation). (optional)
    complete_only = False # bool | Limit to genomes designated as complete, as defined by the submitter. (optional) (default to False)
    include_sequence = [ncbi.datasets.openapi.V2ViralSequenceType()] # List[V2ViralSequenceType] | Specify which sequence files to include in the data package. (optional)
    aux_report = [ncbi.datasets.openapi.V2VirusDatasetReportType()] # List[V2VirusDatasetReportType] | Specify which report files to include in the data package. The virus data report is always included, and its inclusion is not affected by this parameter. (optional)
    use_psg = True # bool | Experimental approach to retrieving sequence data. (optional)
    filename = 'ncbi_dataset.zip' # str | Output file name. (optional) (default to 'ncbi_dataset.zip')

    try:
        # Get a virus genome data package by taxon
        api_response = api_instance.virus_genome_download(taxon, refseq_only=refseq_only, annotated_only=annotated_only, released_since=released_since, updated_since=updated_since, host=host, pangolin_classification=pangolin_classification, geo_location=geo_location, usa_state=usa_state, complete_only=complete_only, include_sequence=include_sequence, aux_report=aux_report, use_psg=use_psg, filename=filename)
        print("The response of VirusApi->virus_genome_download:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirusApi->virus_genome_download: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **taxon** | **str**| NCBI Taxonomy ID or name (common or scientific) at any taxonomic rank | 
 **refseq_only** | **bool**| If true, limit results to RefSeq genomes. | [optional] [default to False]
 **annotated_only** | **bool**| If true, limit results to annotated genomes. | [optional] [default to False]
 **released_since** | **datetime**| Limit to genomes released on or after the specified date. | [optional] 
 **updated_since** | **datetime**| Limit to genomes updated on or after the specified date. | [optional] 
 **host** | **str**| Limit to genomes isolated from the specified host species (NCBI Taxonomy ID, common or scientific name). | [optional] 
 **pangolin_classification** | **str**| Limit to SARS-CoV-2 genomes from the specified Pango lineage. | [optional] 
 **geo_location** | **str**| Limit to genomes collected from the specified geographic location. | [optional] 
 **usa_state** | **str**| Limit to genomes collected from the specified U.S. state (two-letter abbreviation). | [optional] 
 **complete_only** | **bool**| Limit to genomes designated as complete, as defined by the submitter. | [optional] [default to False]
 **include_sequence** | [**List[V2ViralSequenceType]**](V2ViralSequenceType.md)| Specify which sequence files to include in the data package. | [optional] 
 **aux_report** | [**List[V2VirusDatasetReportType]**](V2VirusDatasetReportType.md)| Specify which report files to include in the data package. The virus data report is always included, and its inclusion is not affected by this parameter. | [optional] 
 **use_psg** | **bool**| Experimental approach to retrieving sequence data. | [optional] 
 **filename** | **str**| Output file name. | [optional] [default to &#39;ncbi_dataset.zip&#39;]

### Return type

**bytearray**

### Authorization

[ApiKeyAuthHeader](../README.md#ApiKeyAuthHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/zip

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virus_genome_download_accession**
> bytearray virus_genome_download_accession(accessions, taxons=taxons, refseq_only=refseq_only, annotated_only=annotated_only, released_since=released_since, updated_since=updated_since, host=host, pangolin_classification=pangolin_classification, geo_location=geo_location, usa_state=usa_state, complete_only=complete_only, include_sequence=include_sequence, aux_report=aux_report, use_psg=use_psg, filename=filename)

Get a virus genome data package by nucleotide accession

Download a virus genome data package including sequence, annotation, BioSample data and a detailed data report by nucleotide accession.

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_viral_sequence_type import V2ViralSequenceType
from ncbi.datasets.openapi.models.v2_virus_dataset_report_type import V2VirusDatasetReportType
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
    api_instance = ncbi.datasets.openapi.VirusApi(api_client)
    accessions = ['NC_038294.1'] # List[str] | One or more nucleotide sequence accessions
    taxons = ['1335626'] # List[str] | NCBI Taxonomy IDs or names (common or scientific) at any taxonomic rank (optional)
    refseq_only = False # bool | If true, limit results to RefSeq genomes. (optional) (default to False)
    annotated_only = False # bool | If true, limit results to annotated genomes. (optional) (default to False)
    released_since = '2025-01-15' # datetime | Limit to genomes released on or after the specified date. (optional)
    updated_since = '2025-01-15' # datetime | Limit to genomes updated on or after the specified date. (optional)
    host = '9606' # str | Limit to genomes isolated from the specified host species (NCBI Taxonomy ID, common or scientific name). (optional)
    pangolin_classification = 'LP.8.1' # str | Limit to SARS-CoV-2 genomes from the specified Pango lineage. (optional)
    geo_location = 'USA' # str | Limit to genomes collected from the specified geographic location. (optional)
    usa_state = 'CA' # str | Limit to genomes collected from the specified U.S. state (two-letter abbreviation). (optional)
    complete_only = False # bool | Limit to genomes designated as complete, as defined by the submitter. (optional) (default to False)
    include_sequence = [ncbi.datasets.openapi.V2ViralSequenceType()] # List[V2ViralSequenceType] | Specify which sequence files to include in the data package. (optional)
    aux_report = [ncbi.datasets.openapi.V2VirusDatasetReportType()] # List[V2VirusDatasetReportType] | Specify which report files to include in the data package. The virus data report is always included, and its inclusion is not affected by this parameter. (optional)
    use_psg = True # bool | Experimental approach to retrieving sequence data. (optional)
    filename = 'ncbi_dataset.zip' # str | Output file name. (optional) (default to 'ncbi_dataset.zip')

    try:
        # Get a virus genome data package by nucleotide accession
        api_response = api_instance.virus_genome_download_accession(accessions, taxons=taxons, refseq_only=refseq_only, annotated_only=annotated_only, released_since=released_since, updated_since=updated_since, host=host, pangolin_classification=pangolin_classification, geo_location=geo_location, usa_state=usa_state, complete_only=complete_only, include_sequence=include_sequence, aux_report=aux_report, use_psg=use_psg, filename=filename)
        print("The response of VirusApi->virus_genome_download_accession:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirusApi->virus_genome_download_accession: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accessions** | [**List[str]**](str.md)| One or more nucleotide sequence accessions | 
 **taxons** | [**List[str]**](str.md)| NCBI Taxonomy IDs or names (common or scientific) at any taxonomic rank | [optional] 
 **refseq_only** | **bool**| If true, limit results to RefSeq genomes. | [optional] [default to False]
 **annotated_only** | **bool**| If true, limit results to annotated genomes. | [optional] [default to False]
 **released_since** | **datetime**| Limit to genomes released on or after the specified date. | [optional] 
 **updated_since** | **datetime**| Limit to genomes updated on or after the specified date. | [optional] 
 **host** | **str**| Limit to genomes isolated from the specified host species (NCBI Taxonomy ID, common or scientific name). | [optional] 
 **pangolin_classification** | **str**| Limit to SARS-CoV-2 genomes from the specified Pango lineage. | [optional] 
 **geo_location** | **str**| Limit to genomes collected from the specified geographic location. | [optional] 
 **usa_state** | **str**| Limit to genomes collected from the specified U.S. state (two-letter abbreviation). | [optional] 
 **complete_only** | **bool**| Limit to genomes designated as complete, as defined by the submitter. | [optional] [default to False]
 **include_sequence** | [**List[V2ViralSequenceType]**](V2ViralSequenceType.md)| Specify which sequence files to include in the data package. | [optional] 
 **aux_report** | [**List[V2VirusDatasetReportType]**](V2VirusDatasetReportType.md)| Specify which report files to include in the data package. The virus data report is always included, and its inclusion is not affected by this parameter. | [optional] 
 **use_psg** | **bool**| Experimental approach to retrieving sequence data. | [optional] 
 **filename** | **str**| Output file name. | [optional] [default to &#39;ncbi_dataset.zip&#39;]

### Return type

**bytearray**

### Authorization

[ApiKeyAuthHeader](../README.md#ApiKeyAuthHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/zip

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virus_genome_download_post**
> bytearray virus_genome_download_post(v2_virus_dataset_request, filename=filename)

Get a virus genome data package

Download a virus genome data package including sequence, annotation, BioSample data and a detailed data report by nucleotide accession.

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_virus_dataset_request import V2VirusDatasetRequest
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
    api_instance = ncbi.datasets.openapi.VirusApi(api_client)
    v2_virus_dataset_request = {"accessions":["NC_038294.1"]} # V2VirusDatasetRequest | 
    filename = 'ncbi_dataset.zip' # str | Output file name. (optional) (default to 'ncbi_dataset.zip')

    try:
        # Get a virus genome data package
        api_response = api_instance.virus_genome_download_post(v2_virus_dataset_request, filename=filename)
        print("The response of VirusApi->virus_genome_download_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirusApi->virus_genome_download_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v2_virus_dataset_request** | [**V2VirusDatasetRequest**](V2VirusDatasetRequest.md)|  | 
 **filename** | **str**| Output file name. | [optional] [default to &#39;ncbi_dataset.zip&#39;]

### Return type

**bytearray**

### Authorization

[ApiKeyAuthHeader](../README.md#ApiKeyAuthHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/zip

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virus_genome_summary**
> V2DownloadSummary virus_genome_summary(taxon, accessions=accessions, refseq_only=refseq_only, annotated_only=annotated_only, released_since=released_since, updated_since=updated_since, host=host, pangolin_classification=pangolin_classification, geo_location=geo_location, usa_state=usa_state, complete_only=complete_only, include_sequence=include_sequence, aux_report=aux_report)

Get a download summary of a virus genome data package by taxon

Get a download summary of a virus genome data package, including counts and file sizes, in JSON format.

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_download_summary import V2DownloadSummary
from ncbi.datasets.openapi.models.v2_viral_sequence_type import V2ViralSequenceType
from ncbi.datasets.openapi.models.v2_virus_dataset_report_type import V2VirusDatasetReportType
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
    api_instance = ncbi.datasets.openapi.VirusApi(api_client)
    taxon = '1335626' # str | NCBI Taxonomy ID or name (common or scientific) at any taxonomic rank
    accessions = ['NC_038294.1'] # List[str] | One or more nucleotide sequence accessions (optional)
    refseq_only = False # bool | If true, limit results to RefSeq genomes. (optional) (default to False)
    annotated_only = False # bool | If true, limit results to annotated genomes. (optional) (default to False)
    released_since = '2025-01-15' # datetime | Limit to genomes released on or after the specified date. (optional)
    updated_since = '2025-01-15' # datetime | Limit to genomes updated on or after the specified date. (optional)
    host = '9606' # str | Limit to genomes isolated from the specified host species (NCBI Taxonomy ID, common or scientific name). (optional)
    pangolin_classification = 'LP.8.1' # str | Limit to SARS-CoV-2 genomes from the specified Pango lineage. (optional)
    geo_location = 'USA' # str | Limit to genomes collected from the specified geographic location. (optional)
    usa_state = 'CA' # str | Limit to genomes collected from the specified U.S. state (two-letter abbreviation). (optional)
    complete_only = False # bool | Limit to genomes designated as complete, as defined by the submitter. (optional) (default to False)
    include_sequence = [ncbi.datasets.openapi.V2ViralSequenceType()] # List[V2ViralSequenceType] | Specify which sequence files to include in the data package. (optional)
    aux_report = [ncbi.datasets.openapi.V2VirusDatasetReportType()] # List[V2VirusDatasetReportType] | Specify which report files to include in the data package. The virus data report is always included, and its inclusion is not affected by this parameter. (optional)

    try:
        # Get a download summary of a virus genome data package by taxon
        api_response = api_instance.virus_genome_summary(taxon, accessions=accessions, refseq_only=refseq_only, annotated_only=annotated_only, released_since=released_since, updated_since=updated_since, host=host, pangolin_classification=pangolin_classification, geo_location=geo_location, usa_state=usa_state, complete_only=complete_only, include_sequence=include_sequence, aux_report=aux_report)
        print("The response of VirusApi->virus_genome_summary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirusApi->virus_genome_summary: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **taxon** | **str**| NCBI Taxonomy ID or name (common or scientific) at any taxonomic rank | 
 **accessions** | [**List[str]**](str.md)| One or more nucleotide sequence accessions | [optional] 
 **refseq_only** | **bool**| If true, limit results to RefSeq genomes. | [optional] [default to False]
 **annotated_only** | **bool**| If true, limit results to annotated genomes. | [optional] [default to False]
 **released_since** | **datetime**| Limit to genomes released on or after the specified date. | [optional] 
 **updated_since** | **datetime**| Limit to genomes updated on or after the specified date. | [optional] 
 **host** | **str**| Limit to genomes isolated from the specified host species (NCBI Taxonomy ID, common or scientific name). | [optional] 
 **pangolin_classification** | **str**| Limit to SARS-CoV-2 genomes from the specified Pango lineage. | [optional] 
 **geo_location** | **str**| Limit to genomes collected from the specified geographic location. | [optional] 
 **usa_state** | **str**| Limit to genomes collected from the specified U.S. state (two-letter abbreviation). | [optional] 
 **complete_only** | **bool**| Limit to genomes designated as complete, as defined by the submitter. | [optional] [default to False]
 **include_sequence** | [**List[V2ViralSequenceType]**](V2ViralSequenceType.md)| Specify which sequence files to include in the data package. | [optional] 
 **aux_report** | [**List[V2VirusDatasetReportType]**](V2VirusDatasetReportType.md)| Specify which report files to include in the data package. The virus data report is always included, and its inclusion is not affected by this parameter. | [optional] 

### Return type

[**V2DownloadSummary**](V2DownloadSummary.md)

### Authorization

[ApiKeyAuthHeader](../README.md#ApiKeyAuthHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virus_genome_summary_by_post**
> V2DownloadSummary virus_genome_summary_by_post(v2_virus_dataset_request)

Get a download summary of a virus genome data package

Get a download summary of a virus genome data package, including counts and file sizes, in JSON format.

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_download_summary import V2DownloadSummary
from ncbi.datasets.openapi.models.v2_virus_dataset_request import V2VirusDatasetRequest
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
    api_instance = ncbi.datasets.openapi.VirusApi(api_client)
    v2_virus_dataset_request = {"accessions":["NC_038294.1"]} # V2VirusDatasetRequest | 

    try:
        # Get a download summary of a virus genome data package
        api_response = api_instance.virus_genome_summary_by_post(v2_virus_dataset_request)
        print("The response of VirusApi->virus_genome_summary_by_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirusApi->virus_genome_summary_by_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v2_virus_dataset_request** | [**V2VirusDatasetRequest**](V2VirusDatasetRequest.md)|  | 

### Return type

[**V2DownloadSummary**](V2DownloadSummary.md)

### Authorization

[ApiKeyAuthHeader](../README.md#ApiKeyAuthHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virus_genome_table**
> V2TabularOutput virus_genome_table(taxon, accessions=accessions, refseq_only=refseq_only, annotated_only=annotated_only, released_since=released_since, updated_since=updated_since, host=host, pangolin_classification=pangolin_classification, geo_location=geo_location, usa_state=usa_state, complete_only=complete_only, table_fields=table_fields, include_sequence=include_sequence, aux_report=aux_report, format=format)

Get virus genome metadata in a tabular format (deprecated)

Get virus genome metadata in tabular format for virus genomes by taxon.

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_table_format import V2TableFormat
from ncbi.datasets.openapi.models.v2_tabular_output import V2TabularOutput
from ncbi.datasets.openapi.models.v2_viral_sequence_type import V2ViralSequenceType
from ncbi.datasets.openapi.models.v2_virus_dataset_report_type import V2VirusDatasetReportType
from ncbi.datasets.openapi.models.v2_virus_table_field import V2VirusTableField
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
    api_instance = ncbi.datasets.openapi.VirusApi(api_client)
    taxon = '1335626' # str | NCBI Taxonomy ID or name (common or scientific) at any taxonomic rank
    accessions = ['NC_038294.1'] # List[str] | One or more nucleotide sequence accessions (optional)
    refseq_only = False # bool | If true, limit results to RefSeq genomes. (optional) (default to False)
    annotated_only = False # bool | If true, limit results to annotated genomes. (optional) (default to False)
    released_since = '2025-01-15' # datetime | Limit to genomes released on or after the specified date. (optional)
    updated_since = '2025-01-15' # datetime | Limit to genomes updated on or after the specified date. (optional)
    host = '9606' # str | Limit to genomes isolated from the specified host species (NCBI Taxonomy ID, common or scientific name). (optional)
    pangolin_classification = 'LP.8.1' # str | Limit to SARS-CoV-2 genomes from the specified Pango lineage. (optional)
    geo_location = 'USA' # str | Limit to genomes collected from the specified geographic location. (optional)
    usa_state = 'CA' # str | Limit to genomes collected from the specified U.S. state (two-letter abbreviation). (optional)
    complete_only = False # bool | Limit to genomes designated as complete, as defined by the submitter. (optional) (default to False)
    table_fields = [ncbi.datasets.openapi.V2VirusTableField()] # List[V2VirusTableField] | Specify which fields to include in the tabular report (optional)
    include_sequence = [ncbi.datasets.openapi.V2ViralSequenceType()] # List[V2ViralSequenceType] | Specify which sequence files to include in the data package. (optional)
    aux_report = [ncbi.datasets.openapi.V2VirusDatasetReportType()] # List[V2VirusDatasetReportType] | Specify which report files to include in the data package. The virus data report is always included, and its inclusion is not affected by this parameter. (optional)
    format = tsv # V2TableFormat | Choose download format (tsv, csv or jsonl) (optional) (default to tsv)

    try:
        # Get virus genome metadata in a tabular format (deprecated)
        api_response = api_instance.virus_genome_table(taxon, accessions=accessions, refseq_only=refseq_only, annotated_only=annotated_only, released_since=released_since, updated_since=updated_since, host=host, pangolin_classification=pangolin_classification, geo_location=geo_location, usa_state=usa_state, complete_only=complete_only, table_fields=table_fields, include_sequence=include_sequence, aux_report=aux_report, format=format)
        print("The response of VirusApi->virus_genome_table:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirusApi->virus_genome_table: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **taxon** | **str**| NCBI Taxonomy ID or name (common or scientific) at any taxonomic rank | 
 **accessions** | [**List[str]**](str.md)| One or more nucleotide sequence accessions | [optional] 
 **refseq_only** | **bool**| If true, limit results to RefSeq genomes. | [optional] [default to False]
 **annotated_only** | **bool**| If true, limit results to annotated genomes. | [optional] [default to False]
 **released_since** | **datetime**| Limit to genomes released on or after the specified date. | [optional] 
 **updated_since** | **datetime**| Limit to genomes updated on or after the specified date. | [optional] 
 **host** | **str**| Limit to genomes isolated from the specified host species (NCBI Taxonomy ID, common or scientific name). | [optional] 
 **pangolin_classification** | **str**| Limit to SARS-CoV-2 genomes from the specified Pango lineage. | [optional] 
 **geo_location** | **str**| Limit to genomes collected from the specified geographic location. | [optional] 
 **usa_state** | **str**| Limit to genomes collected from the specified U.S. state (two-letter abbreviation). | [optional] 
 **complete_only** | **bool**| Limit to genomes designated as complete, as defined by the submitter. | [optional] [default to False]
 **table_fields** | [**List[V2VirusTableField]**](V2VirusTableField.md)| Specify which fields to include in the tabular report | [optional] 
 **include_sequence** | [**List[V2ViralSequenceType]**](V2ViralSequenceType.md)| Specify which sequence files to include in the data package. | [optional] 
 **aux_report** | [**List[V2VirusDatasetReportType]**](V2VirusDatasetReportType.md)| Specify which report files to include in the data package. The virus data report is always included, and its inclusion is not affected by this parameter. | [optional] 
 **format** | [**V2TableFormat**](.md)| Choose download format (tsv, csv or jsonl) | [optional] [default to tsv]

### Return type

[**V2TabularOutput**](V2TabularOutput.md)

### Authorization

[ApiKeyAuthHeader](../README.md#ApiKeyAuthHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virus_reports_by_acessions**
> V2reportsVirusDataReportPage virus_reports_by_acessions(accessions, filter_refseq_only=filter_refseq_only, filter_annotated_only=filter_annotated_only, filter_released_since=filter_released_since, filter_updated_since=filter_updated_since, filter_host=filter_host, filter_pangolin_classification=filter_pangolin_classification, filter_geo_location=filter_geo_location, filter_usa_state=filter_usa_state, filter_complete_only=filter_complete_only, returned_content=returned_content, table_fields=table_fields, page_size=page_size, page_token=page_token)

Get a virus data report by nucleotide accession

Get a virus data report by nucleotide accession. By default, in paged JSON format, but also available in tabular (accept: text/tab-separated-values) or JSON Lines (accept: application/x-ndjson) formats.

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_virus_data_report_request_content_type import V2VirusDataReportRequestContentType
from ncbi.datasets.openapi.models.v2reports_virus_data_report_page import V2reportsVirusDataReportPage
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
    api_instance = ncbi.datasets.openapi.VirusApi(api_client)
    accessions = ['NC_038294.1'] # List[str] | One or more nucleotide sequence accessions
    filter_refseq_only = False # bool | If true, limit results to RefSeq genomes. (optional) (default to False)
    filter_annotated_only = False # bool | If true, limit results to annotated genomes. (optional) (default to False)
    filter_released_since = '2025-01-15' # datetime | Limit to genomes released on or after the specified date. (optional)
    filter_updated_since = '2025-01-15' # datetime | Limit to genomes updated on or after the specified date. (optional)
    filter_host = '9606' # str | Limit to genomes isolated from the specified host species (NCBI Taxonomy ID, common or scientific name). (optional)
    filter_pangolin_classification = 'LP.8.1' # str | Limit to SARS-CoV-2 genomes from the specified Pango lineage. (optional)
    filter_geo_location = 'USA' # str | Limit to genomes collected from the specified geographic location. (optional)
    filter_usa_state = 'CA' # str | Limit to genomes collected from the specified U.S. state (two-letter abbreviation). (optional)
    filter_complete_only = False # bool | Limit to genomes designated as complete, as defined by the submitter. (optional) (default to False)
    returned_content = COMPLETE # V2VirusDataReportRequestContentType | Return complete virus reports or nucleotide accessions only (optional) (default to COMPLETE)
    table_fields = ['[\"accession\",\"is-complete\",\"is-annotated\"]'] # List[str] | Specify which fields to include in the tabular report (optional)
    page_size = 20 # int | The maximum number of virus data reports to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, `page_token` can be used to retrieve the remaining results. (optional) (default to 20)
    page_token = 'page_token_example' # str | A page token is returned when the results count exceeds `page size`. Use this token along with previous request parameters to retrieve the next page of results. When `page_token` is empty, all results have been retrieved. (optional)

    try:
        # Get a virus data report by nucleotide accession
        api_response = api_instance.virus_reports_by_acessions(accessions, filter_refseq_only=filter_refseq_only, filter_annotated_only=filter_annotated_only, filter_released_since=filter_released_since, filter_updated_since=filter_updated_since, filter_host=filter_host, filter_pangolin_classification=filter_pangolin_classification, filter_geo_location=filter_geo_location, filter_usa_state=filter_usa_state, filter_complete_only=filter_complete_only, returned_content=returned_content, table_fields=table_fields, page_size=page_size, page_token=page_token)
        print("The response of VirusApi->virus_reports_by_acessions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirusApi->virus_reports_by_acessions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accessions** | [**List[str]**](str.md)| One or more nucleotide sequence accessions | 
 **filter_refseq_only** | **bool**| If true, limit results to RefSeq genomes. | [optional] [default to False]
 **filter_annotated_only** | **bool**| If true, limit results to annotated genomes. | [optional] [default to False]
 **filter_released_since** | **datetime**| Limit to genomes released on or after the specified date. | [optional] 
 **filter_updated_since** | **datetime**| Limit to genomes updated on or after the specified date. | [optional] 
 **filter_host** | **str**| Limit to genomes isolated from the specified host species (NCBI Taxonomy ID, common or scientific name). | [optional] 
 **filter_pangolin_classification** | **str**| Limit to SARS-CoV-2 genomes from the specified Pango lineage. | [optional] 
 **filter_geo_location** | **str**| Limit to genomes collected from the specified geographic location. | [optional] 
 **filter_usa_state** | **str**| Limit to genomes collected from the specified U.S. state (two-letter abbreviation). | [optional] 
 **filter_complete_only** | **bool**| Limit to genomes designated as complete, as defined by the submitter. | [optional] [default to False]
 **returned_content** | [**V2VirusDataReportRequestContentType**](.md)| Return complete virus reports or nucleotide accessions only | [optional] [default to COMPLETE]
 **table_fields** | [**List[str]**](str.md)| Specify which fields to include in the tabular report | [optional] 
 **page_size** | **int**| The maximum number of virus data reports to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, &#x60;page_token&#x60; can be used to retrieve the remaining results. | [optional] [default to 20]
 **page_token** | **str**| A page token is returned when the results count exceeds &#x60;page size&#x60;. Use this token along with previous request parameters to retrieve the next page of results. When &#x60;page_token&#x60; is empty, all results have been retrieved. | [optional] 

### Return type

[**V2reportsVirusDataReportPage**](V2reportsVirusDataReportPage.md)

### Authorization

[ApiKeyAuthHeader](../README.md#ApiKeyAuthHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, application/x-ndjson, text/tab-separated-values

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virus_reports_by_post**
> V2reportsVirusDataReportPage virus_reports_by_post(v2_virus_data_report_request)

Get a virus data report

Get a virus data report. By default, in paged JSON format, but also available in tabular (accept: text/tab-separated-values) or JSON Lines (accept: application/x-ndjson) formats.

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_virus_data_report_request import V2VirusDataReportRequest
from ncbi.datasets.openapi.models.v2reports_virus_data_report_page import V2reportsVirusDataReportPage
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
    api_instance = ncbi.datasets.openapi.VirusApi(api_client)
    v2_virus_data_report_request = {"filter":{"taxons":["1335626"],"refseq_only":true}} # V2VirusDataReportRequest | 

    try:
        # Get a virus data report
        api_response = api_instance.virus_reports_by_post(v2_virus_data_report_request)
        print("The response of VirusApi->virus_reports_by_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirusApi->virus_reports_by_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v2_virus_data_report_request** | [**V2VirusDataReportRequest**](V2VirusDataReportRequest.md)|  | 

### Return type

[**V2reportsVirusDataReportPage**](V2reportsVirusDataReportPage.md)

### Authorization

[ApiKeyAuthHeader](../README.md#ApiKeyAuthHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json, application/x-ndjson, text/tab-separated-values

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virus_reports_by_taxon**
> V2reportsVirusDataReportPage virus_reports_by_taxon(taxon, filter_refseq_only=filter_refseq_only, filter_annotated_only=filter_annotated_only, filter_released_since=filter_released_since, filter_updated_since=filter_updated_since, filter_host=filter_host, filter_pangolin_classification=filter_pangolin_classification, filter_geo_location=filter_geo_location, filter_usa_state=filter_usa_state, filter_complete_only=filter_complete_only, returned_content=returned_content, table_fields=table_fields, page_size=page_size, page_token=page_token)

Get a virus data report by taxon

Get a virus data report by taxon. By default, in paged JSON format, but also available in tabular (accept: text/tab-separated-values) or JSON Lines (accept: application/x-ndjson) formats.

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_virus_data_report_request_content_type import V2VirusDataReportRequestContentType
from ncbi.datasets.openapi.models.v2reports_virus_data_report_page import V2reportsVirusDataReportPage
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
    api_instance = ncbi.datasets.openapi.VirusApi(api_client)
    taxon = '1335626' # str | NCBI Taxonomy ID or name (common or scientific) at any taxonomic rank
    filter_refseq_only = False # bool | If true, limit results to RefSeq genomes. (optional) (default to False)
    filter_annotated_only = False # bool | If true, limit results to annotated genomes. (optional) (default to False)
    filter_released_since = '2025-01-15' # datetime | Limit to genomes released on or after the specified date. (optional)
    filter_updated_since = '2025-01-15' # datetime | Limit to genomes updated on or after the specified date. (optional)
    filter_host = '9606' # str | Limit to genomes isolated from the specified host species (NCBI Taxonomy ID, common or scientific name). (optional)
    filter_pangolin_classification = 'LP.8.1' # str | Limit to SARS-CoV-2 genomes from the specified Pango lineage. (optional)
    filter_geo_location = 'USA' # str | Limit to genomes collected from the specified geographic location. (optional)
    filter_usa_state = 'CA' # str | Limit to genomes collected from the specified U.S. state (two-letter abbreviation). (optional)
    filter_complete_only = False # bool | Limit to genomes designated as complete, as defined by the submitter. (optional) (default to False)
    returned_content = COMPLETE # V2VirusDataReportRequestContentType | Return complete virus reports or nucleotide accessions only (optional) (default to COMPLETE)
    table_fields = ['[\"accession\",\"is-complete\",\"is-annotated\"]'] # List[str] | Specify which fields to include in the tabular report (optional)
    page_size = 20 # int | The maximum number of virus data reports to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, `page_token` can be used to retrieve the remaining results. (optional) (default to 20)
    page_token = 'page_token_example' # str | A page token is returned when the results count exceeds `page size`. Use this token along with previous request parameters to retrieve the next page of results. When `page_token` is empty, all results have been retrieved. (optional)

    try:
        # Get a virus data report by taxon
        api_response = api_instance.virus_reports_by_taxon(taxon, filter_refseq_only=filter_refseq_only, filter_annotated_only=filter_annotated_only, filter_released_since=filter_released_since, filter_updated_since=filter_updated_since, filter_host=filter_host, filter_pangolin_classification=filter_pangolin_classification, filter_geo_location=filter_geo_location, filter_usa_state=filter_usa_state, filter_complete_only=filter_complete_only, returned_content=returned_content, table_fields=table_fields, page_size=page_size, page_token=page_token)
        print("The response of VirusApi->virus_reports_by_taxon:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirusApi->virus_reports_by_taxon: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **taxon** | **str**| NCBI Taxonomy ID or name (common or scientific) at any taxonomic rank | 
 **filter_refseq_only** | **bool**| If true, limit results to RefSeq genomes. | [optional] [default to False]
 **filter_annotated_only** | **bool**| If true, limit results to annotated genomes. | [optional] [default to False]
 **filter_released_since** | **datetime**| Limit to genomes released on or after the specified date. | [optional] 
 **filter_updated_since** | **datetime**| Limit to genomes updated on or after the specified date. | [optional] 
 **filter_host** | **str**| Limit to genomes isolated from the specified host species (NCBI Taxonomy ID, common or scientific name). | [optional] 
 **filter_pangolin_classification** | **str**| Limit to SARS-CoV-2 genomes from the specified Pango lineage. | [optional] 
 **filter_geo_location** | **str**| Limit to genomes collected from the specified geographic location. | [optional] 
 **filter_usa_state** | **str**| Limit to genomes collected from the specified U.S. state (two-letter abbreviation). | [optional] 
 **filter_complete_only** | **bool**| Limit to genomes designated as complete, as defined by the submitter. | [optional] [default to False]
 **returned_content** | [**V2VirusDataReportRequestContentType**](.md)| Return complete virus reports or nucleotide accessions only | [optional] [default to COMPLETE]
 **table_fields** | [**List[str]**](str.md)| Specify which fields to include in the tabular report | [optional] 
 **page_size** | **int**| The maximum number of virus data reports to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, &#x60;page_token&#x60; can be used to retrieve the remaining results. | [optional] [default to 20]
 **page_token** | **str**| A page token is returned when the results count exceeds &#x60;page size&#x60;. Use this token along with previous request parameters to retrieve the next page of results. When &#x60;page_token&#x60; is empty, all results have been retrieved. | [optional] 

### Return type

[**V2reportsVirusDataReportPage**](V2reportsVirusDataReportPage.md)

### Authorization

[ApiKeyAuthHeader](../README.md#ApiKeyAuthHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, application/x-ndjson, text/tab-separated-values

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

