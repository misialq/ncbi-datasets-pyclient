# ncbi.datasets.openapi.GeneApi

All URIs are relative to *https://api.ncbi.nlm.nih.gov/datasets/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download_gene_package**](GeneApi.md#download_gene_package) | **GET** /gene/id/{gene_ids}/download | Get a gene data package by GeneID
[**download_gene_package_post**](GeneApi.md#download_gene_package_post) | **POST** /gene/download | Get a gene data package
[**gene_chromosome_summary**](GeneApi.md#gene_chromosome_summary) | **GET** /gene/taxon/{taxon}/annotation/{annotation_name}/chromosome_summary | Get gene counts per chromosome by taxon and annotation name
[**gene_counts_for_taxon**](GeneApi.md#gene_counts_for_taxon) | **GET** /gene/taxon/{taxon}/counts | Get gene counts by taxon
[**gene_counts_for_taxon_by_post**](GeneApi.md#gene_counts_for_taxon_by_post) | **POST** /gene/taxon/counts | Get gene counts by taxon
[**gene_dataset_report**](GeneApi.md#gene_dataset_report) | **POST** /gene/dataset_report | Get a gene data report
[**gene_dataset_report_by_accession**](GeneApi.md#gene_dataset_report_by_accession) | **GET** /gene/accession/{accessions}/dataset_report | Get a gene data report by RefSeq nucleotide or protein accession
[**gene_dataset_report_by_tax_and_symbol**](GeneApi.md#gene_dataset_report_by_tax_and_symbol) | **GET** /gene/symbol/{symbols}/taxon/{taxon}/dataset_report | Get a gene data report by symbol and taxon
[**gene_dataset_reports_by_id**](GeneApi.md#gene_dataset_reports_by_id) | **GET** /gene/id/{gene_ids}/dataset_report | Get a gene data report by GeneID
[**gene_dataset_reports_by_locus_tag**](GeneApi.md#gene_dataset_reports_by_locus_tag) | **GET** /gene/locus_tag/{locus_tags}/dataset_report | Get a gene data report by locus tag
[**gene_dataset_reports_by_taxon**](GeneApi.md#gene_dataset_reports_by_taxon) | **GET** /gene/taxon/{taxon}/dataset_report | Get a gene data report by taxon
[**gene_download_summary_by_id**](GeneApi.md#gene_download_summary_by_id) | **GET** /gene/id/{gene_ids}/download_summary | Get a download summary of a gene data package by GeneID
[**gene_download_summary_by_post**](GeneApi.md#gene_download_summary_by_post) | **POST** /gene/download_summary | Get a download summary of a gene data package
[**gene_links_by_id**](GeneApi.md#gene_links_by_id) | **GET** /gene/id/{gene_ids}/links | Get gene links by GeneID
[**gene_links_by_id_by_post**](GeneApi.md#gene_links_by_id_by_post) | **POST** /gene/links | Get gene links by GeneID
[**gene_metadata_by_accession**](GeneApi.md#gene_metadata_by_accession) | **GET** /gene/accession/{accessions} | Get gene metadata by RefSeq Accession (deprecated)
[**gene_metadata_by_post**](GeneApi.md#gene_metadata_by_post) | **POST** /gene | Get gene metadata as JSON (deprecated)
[**gene_metadata_by_tax_and_symbol**](GeneApi.md#gene_metadata_by_tax_and_symbol) | **GET** /gene/symbol/{symbols}/taxon/{taxon} | Get gene metadata by gene symbol (deprecated)
[**gene_orthologs_by_id**](GeneApi.md#gene_orthologs_by_id) | **GET** /gene/id/{gene_id}/orthologs | Get a gene data report for a gene ortholog set by GeneID
[**gene_orthologs_by_post**](GeneApi.md#gene_orthologs_by_post) | **POST** /gene/orthologs | Get a gene data report for a gene ortholog set by GeneID
[**gene_product_report**](GeneApi.md#gene_product_report) | **POST** /gene/product_report | Get a gene product report
[**gene_product_report_by_accession**](GeneApi.md#gene_product_report_by_accession) | **GET** /gene/accession/{accessions}/product_report | Get a gene product report by RefSeq nucleotide or protein accession
[**gene_product_report_by_tax_and_symbol**](GeneApi.md#gene_product_report_by_tax_and_symbol) | **GET** /gene/symbol/{symbols}/taxon/{taxon}/product_report | Get a gene product report by symbol and taxon
[**gene_product_reports_by_id**](GeneApi.md#gene_product_reports_by_id) | **GET** /gene/id/{gene_ids}/product_report | Get a gene product report by GeneID
[**gene_product_reports_by_locus_tags**](GeneApi.md#gene_product_reports_by_locus_tags) | **GET** /gene/locus_tag/{locus_tags}/product_report | Get a gene product report by locus tag
[**gene_product_reports_by_taxon**](GeneApi.md#gene_product_reports_by_taxon) | **GET** /gene/taxon/{taxon}/product_report | Get a gene product report by taxon
[**gene_reports_by_id**](GeneApi.md#gene_reports_by_id) | **GET** /gene/id/{gene_ids} | Get gene reports by GeneID (deprecated)
[**gene_reports_by_taxon**](GeneApi.md#gene_reports_by_taxon) | **GET** /gene/taxon/{taxon} | Get gene reports by taxonomic identifier (deprecated)


# **download_gene_package**
> bytearray download_gene_package(gene_ids, include_annotation_type=include_annotation_type, accession_filter=accession_filter, aux_report=aux_report, tabular_reports=tabular_reports, filename=filename)

Get a gene data package by GeneID

Download a gene data package including sequence, annotation and data reports, as a compressed zip archive, by GeneID.

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_fasta import V2Fasta
from ncbi.datasets.openapi.models.v2_gene_dataset_request_gene_dataset_report_type import V2GeneDatasetRequestGeneDatasetReportType
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
    api_instance = ncbi.datasets.openapi.GeneApi(api_client)
    gene_ids = [59067] # List[int] | One or more NCBI GeneIDs
    include_annotation_type = [ncbi.datasets.openapi.V2Fasta()] # List[V2Fasta] | Specify which sequence files to include in the data package. (optional)
    accession_filter = ['NM_021803.4'] # List[str] | Limit the contents of the sequence files and tabular product report to the specified RNA and protein accessions (optional)
    aux_report = [ncbi.datasets.openapi.V2GeneDatasetRequestGeneDatasetReportType()] # List[V2GeneDatasetRequestGeneDatasetReportType] | Specify additional report files to include in the data package. The gene data report is always included, and its inclusion is not affected by this parameter. (optional)
    tabular_reports = [ncbi.datasets.openapi.V2GeneDatasetRequestGeneDatasetReportType()] # List[V2GeneDatasetRequestGeneDatasetReportType] | Specify which tabular report files to include in the data package. (optional)
    filename = 'ncbi_dataset.zip' # str | Output file name. (optional) (default to 'ncbi_dataset.zip')

    try:
        # Get a gene data package by GeneID
        api_response = api_instance.download_gene_package(gene_ids, include_annotation_type=include_annotation_type, accession_filter=accession_filter, aux_report=aux_report, tabular_reports=tabular_reports, filename=filename)
        print("The response of GeneApi->download_gene_package:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeneApi->download_gene_package: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gene_ids** | [**List[int]**](int.md)| One or more NCBI GeneIDs | 
 **include_annotation_type** | [**List[V2Fasta]**](V2Fasta.md)| Specify which sequence files to include in the data package. | [optional] 
 **accession_filter** | [**List[str]**](str.md)| Limit the contents of the sequence files and tabular product report to the specified RNA and protein accessions | [optional] 
 **aux_report** | [**List[V2GeneDatasetRequestGeneDatasetReportType]**](V2GeneDatasetRequestGeneDatasetReportType.md)| Specify additional report files to include in the data package. The gene data report is always included, and its inclusion is not affected by this parameter. | [optional] 
 **tabular_reports** | [**List[V2GeneDatasetRequestGeneDatasetReportType]**](V2GeneDatasetRequestGeneDatasetReportType.md)| Specify which tabular report files to include in the data package. | [optional] 
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

# **download_gene_package_post**
> bytearray download_gene_package_post(v2_gene_dataset_request, filename=filename)

Get a gene data package

Download a gene data package including sequence, annotation and data reports, as a compressed zip archive.

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_gene_dataset_request import V2GeneDatasetRequest
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
    api_instance = ncbi.datasets.openapi.GeneApi(api_client)
    v2_gene_dataset_request = {"gene_ids":[59067,50615],"include_annotation_type":["FASTA_RNA","FASTA_PROTEIN"],"aux_report":["DATASET_REPORT","PRODUCT_REPORT"]} # V2GeneDatasetRequest | 
    filename = 'ncbi_dataset.zip' # str | Output file name. (optional) (default to 'ncbi_dataset.zip')

    try:
        # Get a gene data package
        api_response = api_instance.download_gene_package_post(v2_gene_dataset_request, filename=filename)
        print("The response of GeneApi->download_gene_package_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeneApi->download_gene_package_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v2_gene_dataset_request** | [**V2GeneDatasetRequest**](V2GeneDatasetRequest.md)|  | 
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

# **gene_chromosome_summary**
> V2GeneChromosomeSummaryReply gene_chromosome_summary(taxon, annotation_name)

Get gene counts per chromosome by taxon and annotation name

Get gene counts per chromosome by taxon and annotation name in JSON format.

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_gene_chromosome_summary_reply import V2GeneChromosomeSummaryReply
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
    api_instance = ncbi.datasets.openapi.GeneApi(api_client)
    taxon = '9117' # str | NCBI Taxonomy ID or name (common or scientific) at any taxonomic rank, with an anntoated genome
    annotation_name = 'GCF_028858705.1-RS_2023_03' # str | Annotation name corresponding to the provided taxon

    try:
        # Get gene counts per chromosome by taxon and annotation name
        api_response = api_instance.gene_chromosome_summary(taxon, annotation_name)
        print("The response of GeneApi->gene_chromosome_summary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeneApi->gene_chromosome_summary: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **taxon** | **str**| NCBI Taxonomy ID or name (common or scientific) at any taxonomic rank, with an anntoated genome | 
 **annotation_name** | **str**| Annotation name corresponding to the provided taxon | 

### Return type

[**V2GeneChromosomeSummaryReply**](V2GeneChromosomeSummaryReply.md)

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

# **gene_counts_for_taxon**
> V2GeneCountsByTaxonReply gene_counts_for_taxon(taxon)

Get gene counts by taxon

Get gene counts by taxon in JSON format.

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_gene_counts_by_taxon_reply import V2GeneCountsByTaxonReply
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
    api_instance = ncbi.datasets.openapi.GeneApi(api_client)
    taxon = '9606' # str | Taxon for provided gene symbol

    try:
        # Get gene counts by taxon
        api_response = api_instance.gene_counts_for_taxon(taxon)
        print("The response of GeneApi->gene_counts_for_taxon:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeneApi->gene_counts_for_taxon: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **taxon** | **str**| Taxon for provided gene symbol | 

### Return type

[**V2GeneCountsByTaxonReply**](V2GeneCountsByTaxonReply.md)

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

# **gene_counts_for_taxon_by_post**
> V2GeneCountsByTaxonReply gene_counts_for_taxon_by_post(v2_gene_counts_by_taxon_request)

Get gene counts by taxon

Get gene counts by taxon in JSON format.

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_gene_counts_by_taxon_reply import V2GeneCountsByTaxonReply
from ncbi.datasets.openapi.models.v2_gene_counts_by_taxon_request import V2GeneCountsByTaxonRequest
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
    api_instance = ncbi.datasets.openapi.GeneApi(api_client)
    v2_gene_counts_by_taxon_request = {"taxon":"9606"} # V2GeneCountsByTaxonRequest | 

    try:
        # Get gene counts by taxon
        api_response = api_instance.gene_counts_for_taxon_by_post(v2_gene_counts_by_taxon_request)
        print("The response of GeneApi->gene_counts_for_taxon_by_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeneApi->gene_counts_for_taxon_by_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v2_gene_counts_by_taxon_request** | [**V2GeneCountsByTaxonRequest**](V2GeneCountsByTaxonRequest.md)|  | 

### Return type

[**V2GeneCountsByTaxonReply**](V2GeneCountsByTaxonReply.md)

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

# **gene_dataset_report**
> V2reportsGeneDataReportPage gene_dataset_report(v2_gene_dataset_reports_request)

Get a gene data report

Get a gene data report. By default, in paged JSON format, but also available in tabular (accept: text/tab-separated-values) or JSON Lines (accept: application/x-ndjson) formats.

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_gene_dataset_reports_request import V2GeneDatasetReportsRequest
from ncbi.datasets.openapi.models.v2reports_gene_data_report_page import V2reportsGeneDataReportPage
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
    api_instance = ncbi.datasets.openapi.GeneApi(api_client)
    v2_gene_dataset_reports_request = {"gene_ids":[59067,50615]} # V2GeneDatasetReportsRequest | 

    try:
        # Get a gene data report
        api_response = api_instance.gene_dataset_report(v2_gene_dataset_reports_request)
        print("The response of GeneApi->gene_dataset_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeneApi->gene_dataset_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v2_gene_dataset_reports_request** | [**V2GeneDatasetReportsRequest**](V2GeneDatasetReportsRequest.md)|  | 

### Return type

[**V2reportsGeneDataReportPage**](V2reportsGeneDataReportPage.md)

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

# **gene_dataset_report_by_accession**
> V2reportsGeneDataReportPage gene_dataset_report_by_accession(accessions, returned_content=returned_content, table_fields=table_fields, table_format=table_format, include_tabular_header=include_tabular_header, page_size=page_size, page_token=page_token, query=query, types=types, sort_field=sort_field, sort_direction=sort_direction)

Get a gene data report by RefSeq nucleotide or protein accession

Get a gene data report by RefSeq nucleotide or protein accession. By default, in paged JSON format, but also available in tabular (accept: text/tab-separated-values) or JSON Lines (accept: application/x-ndjson) formats.

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_gene_dataset_reports_request_content_type import V2GeneDatasetReportsRequestContentType
from ncbi.datasets.openapi.models.v2_gene_type import V2GeneType
from ncbi.datasets.openapi.models.v2_include_tabular_header import V2IncludeTabularHeader
from ncbi.datasets.openapi.models.v2_sort_direction import V2SortDirection
from ncbi.datasets.openapi.models.v2reports_gene_data_report_page import V2reportsGeneDataReportPage
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
    api_instance = ncbi.datasets.openapi.GeneApi(api_client)
    accessions = ['NM_021803.4'] # List[str] | One or more RefSeq nucleotide or protein accessions
    returned_content = COMPLETE # V2GeneDatasetReportsRequestContentType | Return complete gene reports, or abbreviated reports with either GeneIDs only or GeneIDs, transcript and protein counts. (optional) (default to COMPLETE)
    table_fields = ['[\"gene-id\",\"gene-type\",\"description\"]'] # List[str] | Specify which fields to include in the tabular report. Additional fields are described here: [Create a table from the gene data reports](https://www.ncbi.nlm.nih.gov/datasets/docs/v2/command-line-tools/using-dataformat/gene-data-reports/). Use of this parameter requires the HTTP header, `accept: text/tab-separated-values`. (optional)
    table_format = 'summary' # str | Specify a predefined set of fields for the tabular report using built-in templates. Use of this parameter requires the HTTP header, `accept: text/tab-separated-values`. (optional)
    include_tabular_header = INCLUDE_TABULAR_HEADER_FIRST_PAGE_ONLY # V2IncludeTabularHeader | Specify when to include the table header when requesting a tabular report. (optional) (default to INCLUDE_TABULAR_HEADER_FIRST_PAGE_ONLY)
    page_size = 20 # int | The maximum number of gene reports to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, `page_token` can be used to retrieve the remaining results. (optional) (default to 20)
    page_token = 'page_token_example' # str | A page token is returned when the results count exceeds `page size`. Use this token along with previous request parameters to retrieve the next page of results. When `page_token` is empty, all results have been retrieved. (optional)
    query = 'A2M immunoglobulin' # str | Limit to genes that match the specified gene symbol, name (description), alias, locus tag or protein name. (optional)
    types = [ncbi.datasets.openapi.V2GeneType()] # List[V2GeneType] | Limit to genes matching the specified gene type. (optional)
    sort_field = 'sort_field_example' # str |  (optional)
    sort_direction = SORT_DIRECTION_UNSPECIFIED # V2SortDirection |  (optional) (default to SORT_DIRECTION_UNSPECIFIED)

    try:
        # Get a gene data report by RefSeq nucleotide or protein accession
        api_response = api_instance.gene_dataset_report_by_accession(accessions, returned_content=returned_content, table_fields=table_fields, table_format=table_format, include_tabular_header=include_tabular_header, page_size=page_size, page_token=page_token, query=query, types=types, sort_field=sort_field, sort_direction=sort_direction)
        print("The response of GeneApi->gene_dataset_report_by_accession:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeneApi->gene_dataset_report_by_accession: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accessions** | [**List[str]**](str.md)| One or more RefSeq nucleotide or protein accessions | 
 **returned_content** | [**V2GeneDatasetReportsRequestContentType**](.md)| Return complete gene reports, or abbreviated reports with either GeneIDs only or GeneIDs, transcript and protein counts. | [optional] [default to COMPLETE]
 **table_fields** | [**List[str]**](str.md)| Specify which fields to include in the tabular report. Additional fields are described here: [Create a table from the gene data reports](https://www.ncbi.nlm.nih.gov/datasets/docs/v2/command-line-tools/using-dataformat/gene-data-reports/). Use of this parameter requires the HTTP header, &#x60;accept: text/tab-separated-values&#x60;. | [optional] 
 **table_format** | **str**| Specify a predefined set of fields for the tabular report using built-in templates. Use of this parameter requires the HTTP header, &#x60;accept: text/tab-separated-values&#x60;. | [optional] 
 **include_tabular_header** | [**V2IncludeTabularHeader**](.md)| Specify when to include the table header when requesting a tabular report. | [optional] [default to INCLUDE_TABULAR_HEADER_FIRST_PAGE_ONLY]
 **page_size** | **int**| The maximum number of gene reports to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, &#x60;page_token&#x60; can be used to retrieve the remaining results. | [optional] [default to 20]
 **page_token** | **str**| A page token is returned when the results count exceeds &#x60;page size&#x60;. Use this token along with previous request parameters to retrieve the next page of results. When &#x60;page_token&#x60; is empty, all results have been retrieved. | [optional] 
 **query** | **str**| Limit to genes that match the specified gene symbol, name (description), alias, locus tag or protein name. | [optional] 
 **types** | [**List[V2GeneType]**](V2GeneType.md)| Limit to genes matching the specified gene type. | [optional] 
 **sort_field** | **str**|  | [optional] 
 **sort_direction** | [**V2SortDirection**](.md)|  | [optional] [default to SORT_DIRECTION_UNSPECIFIED]

### Return type

[**V2reportsGeneDataReportPage**](V2reportsGeneDataReportPage.md)

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

# **gene_dataset_report_by_tax_and_symbol**
> V2reportsGeneDataReportPage gene_dataset_report_by_tax_and_symbol(symbols, taxon, returned_content=returned_content, table_fields=table_fields, table_format=table_format, include_tabular_header=include_tabular_header, page_size=page_size, page_token=page_token, query=query, types=types, tax_search_subtree=tax_search_subtree)

Get a gene data report by symbol and taxon

Get a gene data report by gene symbol and taxon. By default, in paged JSON format, but also available in tabular (accept: text/tab-separated-values) or JSON Lines (accept: application/x-ndjson) formats.

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_gene_dataset_reports_request_content_type import V2GeneDatasetReportsRequestContentType
from ncbi.datasets.openapi.models.v2_gene_type import V2GeneType
from ncbi.datasets.openapi.models.v2_include_tabular_header import V2IncludeTabularHeader
from ncbi.datasets.openapi.models.v2reports_gene_data_report_page import V2reportsGeneDataReportPage
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
    api_instance = ncbi.datasets.openapi.GeneApi(api_client)
    symbols = ['GNAS'] # List[str] | One or more gene symbols
    taxon = '9606' # str | NCBI Taxonomy ID or name (common or scientific, any taxonomic rank) for the provided gene symbol
    returned_content = COMPLETE # V2GeneDatasetReportsRequestContentType | Return complete gene reports, or abbreviated reports with either GeneIDs only or GeneIDs, transcript and protein counts. (optional) (default to COMPLETE)
    table_fields = ['[\"gene-id\",\"gene-type\",\"description\"]'] # List[str] | Specify which fields to include in the tabular report. Additional fields are described here: [Create a table from the gene data reports](https://www.ncbi.nlm.nih.gov/datasets/docs/v2/command-line-tools/using-dataformat/gene-data-reports/). Use of this parameter requires the HTTP header, `accept: text/tab-separated-values`. (optional)
    table_format = 'summary' # str | Specify a predefined set of fields for the tabular report using built-in templates. Use of this parameter requires the HTTP header, `accept: text/tab-separated-values`. (optional)
    include_tabular_header = INCLUDE_TABULAR_HEADER_FIRST_PAGE_ONLY # V2IncludeTabularHeader | Specify when to include the table header when requesting a tabular report. (optional) (default to INCLUDE_TABULAR_HEADER_FIRST_PAGE_ONLY)
    page_size = 20 # int | The maximum number of gene reports to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, `page_token` can be used to retrieve the remaining results. (optional) (default to 20)
    page_token = 'page_token_example' # str | A page token is returned when the results count exceeds `page size`. Use this token along with previous request parameters to retrieve the next page of results. When `page_token` is empty, all results have been retrieved. (optional)
    query = 'A2M immunoglobulin' # str | Limit to genes that match the specified gene symbol, name (description), alias, locus tag or protein name. (optional)
    types = [ncbi.datasets.openapi.V2GeneType()] # List[V2GeneType] | Limit to genes matching the specified gene type. (optional)
    tax_search_subtree = False # bool | If true, include genes from taxonomic ranks below the requested taxon. (optional) (default to False)

    try:
        # Get a gene data report by symbol and taxon
        api_response = api_instance.gene_dataset_report_by_tax_and_symbol(symbols, taxon, returned_content=returned_content, table_fields=table_fields, table_format=table_format, include_tabular_header=include_tabular_header, page_size=page_size, page_token=page_token, query=query, types=types, tax_search_subtree=tax_search_subtree)
        print("The response of GeneApi->gene_dataset_report_by_tax_and_symbol:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeneApi->gene_dataset_report_by_tax_and_symbol: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbols** | [**List[str]**](str.md)| One or more gene symbols | 
 **taxon** | **str**| NCBI Taxonomy ID or name (common or scientific, any taxonomic rank) for the provided gene symbol | 
 **returned_content** | [**V2GeneDatasetReportsRequestContentType**](.md)| Return complete gene reports, or abbreviated reports with either GeneIDs only or GeneIDs, transcript and protein counts. | [optional] [default to COMPLETE]
 **table_fields** | [**List[str]**](str.md)| Specify which fields to include in the tabular report. Additional fields are described here: [Create a table from the gene data reports](https://www.ncbi.nlm.nih.gov/datasets/docs/v2/command-line-tools/using-dataformat/gene-data-reports/). Use of this parameter requires the HTTP header, &#x60;accept: text/tab-separated-values&#x60;. | [optional] 
 **table_format** | **str**| Specify a predefined set of fields for the tabular report using built-in templates. Use of this parameter requires the HTTP header, &#x60;accept: text/tab-separated-values&#x60;. | [optional] 
 **include_tabular_header** | [**V2IncludeTabularHeader**](.md)| Specify when to include the table header when requesting a tabular report. | [optional] [default to INCLUDE_TABULAR_HEADER_FIRST_PAGE_ONLY]
 **page_size** | **int**| The maximum number of gene reports to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, &#x60;page_token&#x60; can be used to retrieve the remaining results. | [optional] [default to 20]
 **page_token** | **str**| A page token is returned when the results count exceeds &#x60;page size&#x60;. Use this token along with previous request parameters to retrieve the next page of results. When &#x60;page_token&#x60; is empty, all results have been retrieved. | [optional] 
 **query** | **str**| Limit to genes that match the specified gene symbol, name (description), alias, locus tag or protein name. | [optional] 
 **types** | [**List[V2GeneType]**](V2GeneType.md)| Limit to genes matching the specified gene type. | [optional] 
 **tax_search_subtree** | **bool**| If true, include genes from taxonomic ranks below the requested taxon. | [optional] [default to False]

### Return type

[**V2reportsGeneDataReportPage**](V2reportsGeneDataReportPage.md)

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

# **gene_dataset_reports_by_id**
> V2reportsGeneDataReportPage gene_dataset_reports_by_id(gene_ids, returned_content=returned_content, table_fields=table_fields, table_format=table_format, include_tabular_header=include_tabular_header, page_size=page_size, page_token=page_token, query=query, types=types, sort_field=sort_field, sort_direction=sort_direction)

Get a gene data report by GeneID

Get a gene data report by GeneID.  By default, in paged JSON format, but also available in tabular (accept: text/tab-separated-values) or JSON Lines (accept: application/x-ndjson) formats.

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_gene_dataset_reports_request_content_type import V2GeneDatasetReportsRequestContentType
from ncbi.datasets.openapi.models.v2_gene_type import V2GeneType
from ncbi.datasets.openapi.models.v2_include_tabular_header import V2IncludeTabularHeader
from ncbi.datasets.openapi.models.v2_sort_direction import V2SortDirection
from ncbi.datasets.openapi.models.v2reports_gene_data_report_page import V2reportsGeneDataReportPage
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
    api_instance = ncbi.datasets.openapi.GeneApi(api_client)
    gene_ids = [59067] # List[int] | One or more NCBI GeneIDs
    returned_content = COMPLETE # V2GeneDatasetReportsRequestContentType | Return complete gene reports, or abbreviated reports with either GeneIDs only or GeneIDs, transcript and protein counts. (optional) (default to COMPLETE)
    table_fields = ['[\"gene-id\",\"gene-type\",\"description\"]'] # List[str] | Specify which fields to include in the tabular report. Additional fields are described here: [Create a table from the gene data reports](https://www.ncbi.nlm.nih.gov/datasets/docs/v2/command-line-tools/using-dataformat/gene-data-reports/). Use of this parameter requires the HTTP header, `accept: text/tab-separated-values`. (optional)
    table_format = 'summary' # str | Specify a predefined set of fields for the tabular report using built-in templates. Use of this parameter requires the HTTP header, `accept: text/tab-separated-values`. (optional)
    include_tabular_header = INCLUDE_TABULAR_HEADER_FIRST_PAGE_ONLY # V2IncludeTabularHeader | Specify when to include the table header when requesting a tabular report. (optional) (default to INCLUDE_TABULAR_HEADER_FIRST_PAGE_ONLY)
    page_size = 20 # int | The maximum number of gene reports to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, `page_token` can be used to retrieve the remaining results. (optional) (default to 20)
    page_token = 'page_token_example' # str | A page token is returned when the results count exceeds `page size`. Use this token along with previous request parameters to retrieve the next page of results. When `page_token` is empty, all results have been retrieved. (optional)
    query = 'A2M immunoglobulin' # str | Limit to genes that match the specified gene symbol, name (description), alias, locus tag or protein name. (optional)
    types = [ncbi.datasets.openapi.V2GeneType()] # List[V2GeneType] | Limit to genes matching the specified gene type. (optional)
    sort_field = 'sort_field_example' # str |  (optional)
    sort_direction = SORT_DIRECTION_UNSPECIFIED # V2SortDirection |  (optional) (default to SORT_DIRECTION_UNSPECIFIED)

    try:
        # Get a gene data report by GeneID
        api_response = api_instance.gene_dataset_reports_by_id(gene_ids, returned_content=returned_content, table_fields=table_fields, table_format=table_format, include_tabular_header=include_tabular_header, page_size=page_size, page_token=page_token, query=query, types=types, sort_field=sort_field, sort_direction=sort_direction)
        print("The response of GeneApi->gene_dataset_reports_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeneApi->gene_dataset_reports_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gene_ids** | [**List[int]**](int.md)| One or more NCBI GeneIDs | 
 **returned_content** | [**V2GeneDatasetReportsRequestContentType**](.md)| Return complete gene reports, or abbreviated reports with either GeneIDs only or GeneIDs, transcript and protein counts. | [optional] [default to COMPLETE]
 **table_fields** | [**List[str]**](str.md)| Specify which fields to include in the tabular report. Additional fields are described here: [Create a table from the gene data reports](https://www.ncbi.nlm.nih.gov/datasets/docs/v2/command-line-tools/using-dataformat/gene-data-reports/). Use of this parameter requires the HTTP header, &#x60;accept: text/tab-separated-values&#x60;. | [optional] 
 **table_format** | **str**| Specify a predefined set of fields for the tabular report using built-in templates. Use of this parameter requires the HTTP header, &#x60;accept: text/tab-separated-values&#x60;. | [optional] 
 **include_tabular_header** | [**V2IncludeTabularHeader**](.md)| Specify when to include the table header when requesting a tabular report. | [optional] [default to INCLUDE_TABULAR_HEADER_FIRST_PAGE_ONLY]
 **page_size** | **int**| The maximum number of gene reports to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, &#x60;page_token&#x60; can be used to retrieve the remaining results. | [optional] [default to 20]
 **page_token** | **str**| A page token is returned when the results count exceeds &#x60;page size&#x60;. Use this token along with previous request parameters to retrieve the next page of results. When &#x60;page_token&#x60; is empty, all results have been retrieved. | [optional] 
 **query** | **str**| Limit to genes that match the specified gene symbol, name (description), alias, locus tag or protein name. | [optional] 
 **types** | [**List[V2GeneType]**](V2GeneType.md)| Limit to genes matching the specified gene type. | [optional] 
 **sort_field** | **str**|  | [optional] 
 **sort_direction** | [**V2SortDirection**](.md)|  | [optional] [default to SORT_DIRECTION_UNSPECIFIED]

### Return type

[**V2reportsGeneDataReportPage**](V2reportsGeneDataReportPage.md)

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

# **gene_dataset_reports_by_locus_tag**
> V2reportsGeneDataReportPage gene_dataset_reports_by_locus_tag(locus_tags, returned_content=returned_content, table_fields=table_fields, table_format=table_format, include_tabular_header=include_tabular_header, page_size=page_size, page_token=page_token, query=query, types=types, sort_field=sort_field)

Get a gene data report by locus tag

Get a gene data report by gene locus tag. By default, in paged JSON format, but also available in tabular (accept: text/tab-separated-values) or JSON Lines (accept: application/x-ndjson) formats.

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_gene_dataset_reports_request_content_type import V2GeneDatasetReportsRequestContentType
from ncbi.datasets.openapi.models.v2_gene_type import V2GeneType
from ncbi.datasets.openapi.models.v2_include_tabular_header import V2IncludeTabularHeader
from ncbi.datasets.openapi.models.v2reports_gene_data_report_page import V2reportsGeneDataReportPage
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
    api_instance = ncbi.datasets.openapi.GeneApi(api_client)
    locus_tags = ['b0001'] # List[str] | Gene locus tags
    returned_content = COMPLETE # V2GeneDatasetReportsRequestContentType | Return complete gene reports, or abbreviated reports with either GeneIDs only or GeneIDs, transcript and protein counts. (optional) (default to COMPLETE)
    table_fields = ['[\"gene-id\",\"gene-type\",\"description\"]'] # List[str] | Specify which fields to include in the tabular report. Additional fields are described here: [Create a table from the gene data reports](https://www.ncbi.nlm.nih.gov/datasets/docs/v2/command-line-tools/using-dataformat/gene-data-reports/). Use of this parameter requires the HTTP header, `accept: text/tab-separated-values`. (optional)
    table_format = 'summary' # str | Specify a predefined set of fields for the tabular report using built-in templates. Use of this parameter requires the HTTP header, `accept: text/tab-separated-values`. (optional)
    include_tabular_header = INCLUDE_TABULAR_HEADER_FIRST_PAGE_ONLY # V2IncludeTabularHeader | Specify when to include the table header when requesting a tabular report. (optional) (default to INCLUDE_TABULAR_HEADER_FIRST_PAGE_ONLY)
    page_size = 20 # int | The maximum number of gene reports to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, `page_token` can be used to retrieve the remaining results. (optional) (default to 20)
    page_token = 'page_token_example' # str | A page token is returned when the results count exceeds `page size`. Use this token along with previous request parameters to retrieve the next page of results. When `page_token` is empty, all results have been retrieved. (optional)
    query = 'A2M immunoglobulin' # str | Limit to genes that match the specified gene symbol, name (description), alias, locus tag or protein name. (optional)
    types = [ncbi.datasets.openapi.V2GeneType()] # List[V2GeneType] | Limit to genes matching the specified gene type. (optional)
    sort_field = 'sort_field_example' # str |  (optional)

    try:
        # Get a gene data report by locus tag
        api_response = api_instance.gene_dataset_reports_by_locus_tag(locus_tags, returned_content=returned_content, table_fields=table_fields, table_format=table_format, include_tabular_header=include_tabular_header, page_size=page_size, page_token=page_token, query=query, types=types, sort_field=sort_field)
        print("The response of GeneApi->gene_dataset_reports_by_locus_tag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeneApi->gene_dataset_reports_by_locus_tag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **locus_tags** | [**List[str]**](str.md)| Gene locus tags | 
 **returned_content** | [**V2GeneDatasetReportsRequestContentType**](.md)| Return complete gene reports, or abbreviated reports with either GeneIDs only or GeneIDs, transcript and protein counts. | [optional] [default to COMPLETE]
 **table_fields** | [**List[str]**](str.md)| Specify which fields to include in the tabular report. Additional fields are described here: [Create a table from the gene data reports](https://www.ncbi.nlm.nih.gov/datasets/docs/v2/command-line-tools/using-dataformat/gene-data-reports/). Use of this parameter requires the HTTP header, &#x60;accept: text/tab-separated-values&#x60;. | [optional] 
 **table_format** | **str**| Specify a predefined set of fields for the tabular report using built-in templates. Use of this parameter requires the HTTP header, &#x60;accept: text/tab-separated-values&#x60;. | [optional] 
 **include_tabular_header** | [**V2IncludeTabularHeader**](.md)| Specify when to include the table header when requesting a tabular report. | [optional] [default to INCLUDE_TABULAR_HEADER_FIRST_PAGE_ONLY]
 **page_size** | **int**| The maximum number of gene reports to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, &#x60;page_token&#x60; can be used to retrieve the remaining results. | [optional] [default to 20]
 **page_token** | **str**| A page token is returned when the results count exceeds &#x60;page size&#x60;. Use this token along with previous request parameters to retrieve the next page of results. When &#x60;page_token&#x60; is empty, all results have been retrieved. | [optional] 
 **query** | **str**| Limit to genes that match the specified gene symbol, name (description), alias, locus tag or protein name. | [optional] 
 **types** | [**List[V2GeneType]**](V2GeneType.md)| Limit to genes matching the specified gene type. | [optional] 
 **sort_field** | **str**|  | [optional] 

### Return type

[**V2reportsGeneDataReportPage**](V2reportsGeneDataReportPage.md)

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

# **gene_dataset_reports_by_taxon**
> V2reportsGeneDataReportPage gene_dataset_reports_by_taxon(taxon, returned_content=returned_content, table_fields=table_fields, table_format=table_format, include_tabular_header=include_tabular_header, page_size=page_size, page_token=page_token, query=query, types=types, tax_search_subtree=tax_search_subtree)

Get a gene data report by taxon

Get a gene data report by taxon. By default, in paged JSON format, but also available in tabular (accept: text/tab-separated-values) or JSON Lines (accept: application/x-ndjson) formats.

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_gene_dataset_reports_request_content_type import V2GeneDatasetReportsRequestContentType
from ncbi.datasets.openapi.models.v2_gene_type import V2GeneType
from ncbi.datasets.openapi.models.v2_include_tabular_header import V2IncludeTabularHeader
from ncbi.datasets.openapi.models.v2reports_gene_data_report_page import V2reportsGeneDataReportPage
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
    api_instance = ncbi.datasets.openapi.GeneApi(api_client)
    taxon = '9606' # str | NCBI Taxonomy ID or name (common or scientific) that the genes are annotated at
    returned_content = COMPLETE # V2GeneDatasetReportsRequestContentType | Return complete gene reports, or abbreviated reports with either GeneIDs only or GeneIDs, transcript and protein counts. (optional) (default to COMPLETE)
    table_fields = ['[\"gene-id\",\"gene-type\",\"description\"]'] # List[str] | Specify which fields to include in the tabular report. Additional fields are described here: [Create a table from the gene data reports](https://www.ncbi.nlm.nih.gov/datasets/docs/v2/command-line-tools/using-dataformat/gene-data-reports/). Use of this parameter requires the HTTP header, `accept: text/tab-separated-values`. (optional)
    table_format = 'summary' # str | Specify a predefined set of fields for the tabular report using built-in templates. Use of this parameter requires the HTTP header, `accept: text/tab-separated-values`. (optional)
    include_tabular_header = INCLUDE_TABULAR_HEADER_FIRST_PAGE_ONLY # V2IncludeTabularHeader | Specify when to include the table header when requesting a tabular report. (optional) (default to INCLUDE_TABULAR_HEADER_FIRST_PAGE_ONLY)
    page_size = 20 # int | The maximum number of gene reports to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, `page_token` can be used to retrieve the remaining results. (optional) (default to 20)
    page_token = 'page_token_example' # str | A page token is returned when the results count exceeds `page size`. Use this token along with previous request parameters to retrieve the next page of results. When `page_token` is empty, all results have been retrieved. (optional)
    query = 'A2M immunoglobulin' # str | Limit to genes that match the specified gene symbol, name (description), alias, locus tag or protein name. (optional)
    types = [ncbi.datasets.openapi.V2GeneType()] # List[V2GeneType] | Limit to genes matching the specified gene type. (optional)
    tax_search_subtree = False # bool | If true, include genes from taxonomic ranks below the requested taxon. (optional) (default to False)

    try:
        # Get a gene data report by taxon
        api_response = api_instance.gene_dataset_reports_by_taxon(taxon, returned_content=returned_content, table_fields=table_fields, table_format=table_format, include_tabular_header=include_tabular_header, page_size=page_size, page_token=page_token, query=query, types=types, tax_search_subtree=tax_search_subtree)
        print("The response of GeneApi->gene_dataset_reports_by_taxon:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeneApi->gene_dataset_reports_by_taxon: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **taxon** | **str**| NCBI Taxonomy ID or name (common or scientific) that the genes are annotated at | 
 **returned_content** | [**V2GeneDatasetReportsRequestContentType**](.md)| Return complete gene reports, or abbreviated reports with either GeneIDs only or GeneIDs, transcript and protein counts. | [optional] [default to COMPLETE]
 **table_fields** | [**List[str]**](str.md)| Specify which fields to include in the tabular report. Additional fields are described here: [Create a table from the gene data reports](https://www.ncbi.nlm.nih.gov/datasets/docs/v2/command-line-tools/using-dataformat/gene-data-reports/). Use of this parameter requires the HTTP header, &#x60;accept: text/tab-separated-values&#x60;. | [optional] 
 **table_format** | **str**| Specify a predefined set of fields for the tabular report using built-in templates. Use of this parameter requires the HTTP header, &#x60;accept: text/tab-separated-values&#x60;. | [optional] 
 **include_tabular_header** | [**V2IncludeTabularHeader**](.md)| Specify when to include the table header when requesting a tabular report. | [optional] [default to INCLUDE_TABULAR_HEADER_FIRST_PAGE_ONLY]
 **page_size** | **int**| The maximum number of gene reports to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, &#x60;page_token&#x60; can be used to retrieve the remaining results. | [optional] [default to 20]
 **page_token** | **str**| A page token is returned when the results count exceeds &#x60;page size&#x60;. Use this token along with previous request parameters to retrieve the next page of results. When &#x60;page_token&#x60; is empty, all results have been retrieved. | [optional] 
 **query** | **str**| Limit to genes that match the specified gene symbol, name (description), alias, locus tag or protein name. | [optional] 
 **types** | [**List[V2GeneType]**](V2GeneType.md)| Limit to genes matching the specified gene type. | [optional] 
 **tax_search_subtree** | **bool**| If true, include genes from taxonomic ranks below the requested taxon. | [optional] [default to False]

### Return type

[**V2reportsGeneDataReportPage**](V2reportsGeneDataReportPage.md)

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

# **gene_download_summary_by_id**
> V2DownloadSummary gene_download_summary_by_id(gene_ids, include_annotation_type=include_annotation_type, returned_content=returned_content, fasta_filter=fasta_filter, accession_filter=accession_filter, aux_report=aux_report, tabular_reports=tabular_reports)

Get a download summary of a gene data package by GeneID

Get a download summary of a gene data package, including counts and estimated package size, in JSON format.

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_download_summary import V2DownloadSummary
from ncbi.datasets.openapi.models.v2_fasta import V2Fasta
from ncbi.datasets.openapi.models.v2_gene_dataset_request_content_type import V2GeneDatasetRequestContentType
from ncbi.datasets.openapi.models.v2_gene_dataset_request_gene_dataset_report_type import V2GeneDatasetRequestGeneDatasetReportType
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
    api_instance = ncbi.datasets.openapi.GeneApi(api_client)
    gene_ids = [59067] # List[int] | One or more NCBI GeneIDs
    include_annotation_type = [ncbi.datasets.openapi.V2Fasta()] # List[V2Fasta] | Specify which sequence files to include in the data package. (optional)
    returned_content = COMPLETE # V2GeneDatasetRequestContentType | Return complete gene reports, or abbreviated reports with either GeneIDs only or GeneIDs, transcript and protein counts. (optional) (default to COMPLETE)
    fasta_filter = ['fasta_filter_example'] # List[str] | Limit the FASTA sequences in the datasets package to these transcript and protein accessions (deprecated) (optional)
    accession_filter = ['NM_021803.4'] # List[str] | Limit the contents of the sequence files and tabular product report to the specified RNA and protein accessions (optional)
    aux_report = [ncbi.datasets.openapi.V2GeneDatasetRequestGeneDatasetReportType()] # List[V2GeneDatasetRequestGeneDatasetReportType] | Specify additional report files to include in the data package. The gene data report is always included, and its inclusion is not affected by this parameter. (optional)
    tabular_reports = [ncbi.datasets.openapi.V2GeneDatasetRequestGeneDatasetReportType()] # List[V2GeneDatasetRequestGeneDatasetReportType] | Specify which tabular report files to include in the data package. (optional)

    try:
        # Get a download summary of a gene data package by GeneID
        api_response = api_instance.gene_download_summary_by_id(gene_ids, include_annotation_type=include_annotation_type, returned_content=returned_content, fasta_filter=fasta_filter, accession_filter=accession_filter, aux_report=aux_report, tabular_reports=tabular_reports)
        print("The response of GeneApi->gene_download_summary_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeneApi->gene_download_summary_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gene_ids** | [**List[int]**](int.md)| One or more NCBI GeneIDs | 
 **include_annotation_type** | [**List[V2Fasta]**](V2Fasta.md)| Specify which sequence files to include in the data package. | [optional] 
 **returned_content** | [**V2GeneDatasetRequestContentType**](.md)| Return complete gene reports, or abbreviated reports with either GeneIDs only or GeneIDs, transcript and protein counts. | [optional] [default to COMPLETE]
 **fasta_filter** | [**List[str]**](str.md)| Limit the FASTA sequences in the datasets package to these transcript and protein accessions (deprecated) | [optional] 
 **accession_filter** | [**List[str]**](str.md)| Limit the contents of the sequence files and tabular product report to the specified RNA and protein accessions | [optional] 
 **aux_report** | [**List[V2GeneDatasetRequestGeneDatasetReportType]**](V2GeneDatasetRequestGeneDatasetReportType.md)| Specify additional report files to include in the data package. The gene data report is always included, and its inclusion is not affected by this parameter. | [optional] 
 **tabular_reports** | [**List[V2GeneDatasetRequestGeneDatasetReportType]**](V2GeneDatasetRequestGeneDatasetReportType.md)| Specify which tabular report files to include in the data package. | [optional] 

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

# **gene_download_summary_by_post**
> V2DownloadSummary gene_download_summary_by_post(v2_gene_dataset_request)

Get a download summary of a gene data package

Get a download summary of a gene data package, including counts and estimated package size, in JSON format.

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_download_summary import V2DownloadSummary
from ncbi.datasets.openapi.models.v2_gene_dataset_request import V2GeneDatasetRequest
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
    api_instance = ncbi.datasets.openapi.GeneApi(api_client)
    v2_gene_dataset_request = {"gene_ids":[59067,50615],"include_annotation_type":["FASTA_RNA","FASTA_PROTEIN"],"aux_report":["DATASET_REPORT","PRODUCT_REPORT"]} # V2GeneDatasetRequest | 

    try:
        # Get a download summary of a gene data package
        api_response = api_instance.gene_download_summary_by_post(v2_gene_dataset_request)
        print("The response of GeneApi->gene_download_summary_by_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeneApi->gene_download_summary_by_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v2_gene_dataset_request** | [**V2GeneDatasetRequest**](V2GeneDatasetRequest.md)|  | 

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

# **gene_links_by_id**
> V2GeneLinksReply gene_links_by_id(gene_ids)

Get gene links by GeneID

Get links to available gene resources in JSON format.

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_gene_links_reply import V2GeneLinksReply
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
    api_instance = ncbi.datasets.openapi.GeneApi(api_client)
    gene_ids = [59067] # List[int] | One or more NCBI GeneIDs, limited to 100

    try:
        # Get gene links by GeneID
        api_response = api_instance.gene_links_by_id(gene_ids)
        print("The response of GeneApi->gene_links_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeneApi->gene_links_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gene_ids** | [**List[int]**](int.md)| One or more NCBI GeneIDs, limited to 100 | 

### Return type

[**V2GeneLinksReply**](V2GeneLinksReply.md)

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

# **gene_links_by_id_by_post**
> V2GeneLinksReply gene_links_by_id_by_post(v2_gene_links_request)

Get gene links by GeneID

Get links to available gene resources in JSON format.

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_gene_links_reply import V2GeneLinksReply
from ncbi.datasets.openapi.models.v2_gene_links_request import V2GeneLinksRequest
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
    api_instance = ncbi.datasets.openapi.GeneApi(api_client)
    v2_gene_links_request = {"gene_ids":[59067,50615]} # V2GeneLinksRequest | 

    try:
        # Get gene links by GeneID
        api_response = api_instance.gene_links_by_id_by_post(v2_gene_links_request)
        print("The response of GeneApi->gene_links_by_id_by_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeneApi->gene_links_by_id_by_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v2_gene_links_request** | [**V2GeneLinksRequest**](V2GeneLinksRequest.md)|  | 

### Return type

[**V2GeneLinksReply**](V2GeneLinksReply.md)

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

# **gene_metadata_by_accession**
> V2reportsGeneDataReportPage gene_metadata_by_accession(accessions, returned_content=returned_content, locus_tags=locus_tags, table_fields=table_fields, include_tabular_header=include_tabular_header, page_size=page_size, page_token=page_token, accession_filter=accession_filter, tax_search_subtree=tax_search_subtree, sort_field=sort_field, sort_direction=sort_direction)

Get gene metadata by RefSeq Accession (deprecated)

Get a gene summary by RefSeq Accession. By default, in paged JSON format, but also available as tabular (accept: text/tab-separated-values) or json-lines (accept: application/x-ndjson)

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_gene_dataset_reports_request_content_type import V2GeneDatasetReportsRequestContentType
from ncbi.datasets.openapi.models.v2_include_tabular_header import V2IncludeTabularHeader
from ncbi.datasets.openapi.models.v2_sort_direction import V2SortDirection
from ncbi.datasets.openapi.models.v2reports_gene_data_report_page import V2reportsGeneDataReportPage
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
    api_instance = ncbi.datasets.openapi.GeneApi(api_client)
    accessions = ['NM_021803.4'] # List[str] | One or more RefSeq nucleotide or protein accessions
    returned_content = COMPLETE # V2GeneDatasetReportsRequestContentType | Return complete gene reports, or abbreviated reports with either GeneIDs only or GeneIDs, transcript and protein counts. (optional) (default to COMPLETE)
    locus_tags = ['b0001'] # List[str] | Gene locus tags (optional)
    table_fields = ['[\"gene-id\",\"gene-type\",\"description\"]'] # List[str] | Specify which fields to include in the tabular report. Additional fields are described here: [Create a table from the gene data reports](https://www.ncbi.nlm.nih.gov/datasets/docs/v2/command-line-tools/using-dataformat/gene-data-reports/). Use of this parameter requires the HTTP header, `accept: text/tab-separated-values`. (optional)
    include_tabular_header = INCLUDE_TABULAR_HEADER_FIRST_PAGE_ONLY # V2IncludeTabularHeader | Specify when to include the table header when requesting a tabular report. (optional) (default to INCLUDE_TABULAR_HEADER_FIRST_PAGE_ONLY)
    page_size = 20 # int | The maximum number of gene reports to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, `page_token` can be used to retrieve the remaining results. (optional) (default to 20)
    page_token = 'page_token_example' # str | A page token is returned when the results count exceeds `page size`. Use this token along with previous request parameters to retrieve the next page of results. When `page_token` is empty, all results have been retrieved. (optional)
    accession_filter = ['[\"NM_001407959.1\",\"NM_001408458.1\"]'] # List[str] | Filter tabular product report to only include the selected accessions. Use of this parameter requires the HTTP header, `accept: text/tab-separated-values`. (optional)
    tax_search_subtree = False # bool | If true, include genes from taxonomic ranks below the requested taxon. (optional) (default to False)
    sort_field = 'sort_field_example' # str |  (optional)
    sort_direction = SORT_DIRECTION_UNSPECIFIED # V2SortDirection |  (optional) (default to SORT_DIRECTION_UNSPECIFIED)

    try:
        # Get gene metadata by RefSeq Accession (deprecated)
        api_response = api_instance.gene_metadata_by_accession(accessions, returned_content=returned_content, locus_tags=locus_tags, table_fields=table_fields, include_tabular_header=include_tabular_header, page_size=page_size, page_token=page_token, accession_filter=accession_filter, tax_search_subtree=tax_search_subtree, sort_field=sort_field, sort_direction=sort_direction)
        print("The response of GeneApi->gene_metadata_by_accession:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeneApi->gene_metadata_by_accession: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accessions** | [**List[str]**](str.md)| One or more RefSeq nucleotide or protein accessions | 
 **returned_content** | [**V2GeneDatasetReportsRequestContentType**](.md)| Return complete gene reports, or abbreviated reports with either GeneIDs only or GeneIDs, transcript and protein counts. | [optional] [default to COMPLETE]
 **locus_tags** | [**List[str]**](str.md)| Gene locus tags | [optional] 
 **table_fields** | [**List[str]**](str.md)| Specify which fields to include in the tabular report. Additional fields are described here: [Create a table from the gene data reports](https://www.ncbi.nlm.nih.gov/datasets/docs/v2/command-line-tools/using-dataformat/gene-data-reports/). Use of this parameter requires the HTTP header, &#x60;accept: text/tab-separated-values&#x60;. | [optional] 
 **include_tabular_header** | [**V2IncludeTabularHeader**](.md)| Specify when to include the table header when requesting a tabular report. | [optional] [default to INCLUDE_TABULAR_HEADER_FIRST_PAGE_ONLY]
 **page_size** | **int**| The maximum number of gene reports to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, &#x60;page_token&#x60; can be used to retrieve the remaining results. | [optional] [default to 20]
 **page_token** | **str**| A page token is returned when the results count exceeds &#x60;page size&#x60;. Use this token along with previous request parameters to retrieve the next page of results. When &#x60;page_token&#x60; is empty, all results have been retrieved. | [optional] 
 **accession_filter** | [**List[str]**](str.md)| Filter tabular product report to only include the selected accessions. Use of this parameter requires the HTTP header, &#x60;accept: text/tab-separated-values&#x60;. | [optional] 
 **tax_search_subtree** | **bool**| If true, include genes from taxonomic ranks below the requested taxon. | [optional] [default to False]
 **sort_field** | **str**|  | [optional] 
 **sort_direction** | [**V2SortDirection**](.md)|  | [optional] [default to SORT_DIRECTION_UNSPECIFIED]

### Return type

[**V2reportsGeneDataReportPage**](V2reportsGeneDataReportPage.md)

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

# **gene_metadata_by_post**
> V2reportsGeneDataReportPage gene_metadata_by_post(v2_gene_dataset_reports_request)

Get gene metadata as JSON (deprecated)

Get a gene summary. By default, in paged JSON format, but also available as tabular (accept: text/tab-separated-values) or json-lines (accept: application/x-ndjson)

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_gene_dataset_reports_request import V2GeneDatasetReportsRequest
from ncbi.datasets.openapi.models.v2reports_gene_data_report_page import V2reportsGeneDataReportPage
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
    api_instance = ncbi.datasets.openapi.GeneApi(api_client)
    v2_gene_dataset_reports_request = {"gene_ids":[59067,50615]} # V2GeneDatasetReportsRequest | 

    try:
        # Get gene metadata as JSON (deprecated)
        api_response = api_instance.gene_metadata_by_post(v2_gene_dataset_reports_request)
        print("The response of GeneApi->gene_metadata_by_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeneApi->gene_metadata_by_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v2_gene_dataset_reports_request** | [**V2GeneDatasetReportsRequest**](V2GeneDatasetReportsRequest.md)|  | 

### Return type

[**V2reportsGeneDataReportPage**](V2reportsGeneDataReportPage.md)

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

# **gene_metadata_by_tax_and_symbol**
> V2reportsGeneDataReportPage gene_metadata_by_tax_and_symbol(symbols, taxon, returned_content=returned_content, locus_tags=locus_tags, table_fields=table_fields, include_tabular_header=include_tabular_header, page_size=page_size, page_token=page_token, accession_filter=accession_filter, tax_search_subtree=tax_search_subtree, sort_field=sort_field, sort_direction=sort_direction)

Get gene metadata by gene symbol (deprecated)

Get a gene summary by by gene symbol. By default, in paged JSON format, but also available as tabular (accept: text/tab-separated-values) or json-lines (accept: application/x-ndjson)

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_gene_dataset_reports_request_content_type import V2GeneDatasetReportsRequestContentType
from ncbi.datasets.openapi.models.v2_include_tabular_header import V2IncludeTabularHeader
from ncbi.datasets.openapi.models.v2_sort_direction import V2SortDirection
from ncbi.datasets.openapi.models.v2reports_gene_data_report_page import V2reportsGeneDataReportPage
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
    api_instance = ncbi.datasets.openapi.GeneApi(api_client)
    symbols = ['GNAS'] # List[str] | One or more gene symbols
    taxon = '9606' # str | NCBI Taxonomy ID or name (common or scientific, any taxonomic rank) for the provided gene symbol
    returned_content = COMPLETE # V2GeneDatasetReportsRequestContentType | Return complete gene reports, or abbreviated reports with either GeneIDs only or GeneIDs, transcript and protein counts. (optional) (default to COMPLETE)
    locus_tags = ['b0001'] # List[str] | Gene locus tags (optional)
    table_fields = ['[\"gene-id\",\"gene-type\",\"description\"]'] # List[str] | Specify which fields to include in the tabular report. Additional fields are described here: [Create a table from the gene data reports](https://www.ncbi.nlm.nih.gov/datasets/docs/v2/command-line-tools/using-dataformat/gene-data-reports/). Use of this parameter requires the HTTP header, `accept: text/tab-separated-values`. (optional)
    include_tabular_header = INCLUDE_TABULAR_HEADER_FIRST_PAGE_ONLY # V2IncludeTabularHeader | Specify when to include the table header when requesting a tabular report. (optional) (default to INCLUDE_TABULAR_HEADER_FIRST_PAGE_ONLY)
    page_size = 20 # int | The maximum number of gene reports to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, `page_token` can be used to retrieve the remaining results. (optional) (default to 20)
    page_token = 'page_token_example' # str | A page token is returned when the results count exceeds `page size`. Use this token along with previous request parameters to retrieve the next page of results. When `page_token` is empty, all results have been retrieved. (optional)
    accession_filter = ['[\"NM_001407959.1\",\"NM_001408458.1\"]'] # List[str] | Filter tabular product report to only include the selected accessions. Use of this parameter requires the HTTP header, `accept: text/tab-separated-values`. (optional)
    tax_search_subtree = False # bool | If true, include genes from taxonomic ranks below the requested taxon. (optional) (default to False)
    sort_field = 'sort_field_example' # str |  (optional)
    sort_direction = SORT_DIRECTION_UNSPECIFIED # V2SortDirection |  (optional) (default to SORT_DIRECTION_UNSPECIFIED)

    try:
        # Get gene metadata by gene symbol (deprecated)
        api_response = api_instance.gene_metadata_by_tax_and_symbol(symbols, taxon, returned_content=returned_content, locus_tags=locus_tags, table_fields=table_fields, include_tabular_header=include_tabular_header, page_size=page_size, page_token=page_token, accession_filter=accession_filter, tax_search_subtree=tax_search_subtree, sort_field=sort_field, sort_direction=sort_direction)
        print("The response of GeneApi->gene_metadata_by_tax_and_symbol:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeneApi->gene_metadata_by_tax_and_symbol: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbols** | [**List[str]**](str.md)| One or more gene symbols | 
 **taxon** | **str**| NCBI Taxonomy ID or name (common or scientific, any taxonomic rank) for the provided gene symbol | 
 **returned_content** | [**V2GeneDatasetReportsRequestContentType**](.md)| Return complete gene reports, or abbreviated reports with either GeneIDs only or GeneIDs, transcript and protein counts. | [optional] [default to COMPLETE]
 **locus_tags** | [**List[str]**](str.md)| Gene locus tags | [optional] 
 **table_fields** | [**List[str]**](str.md)| Specify which fields to include in the tabular report. Additional fields are described here: [Create a table from the gene data reports](https://www.ncbi.nlm.nih.gov/datasets/docs/v2/command-line-tools/using-dataformat/gene-data-reports/). Use of this parameter requires the HTTP header, &#x60;accept: text/tab-separated-values&#x60;. | [optional] 
 **include_tabular_header** | [**V2IncludeTabularHeader**](.md)| Specify when to include the table header when requesting a tabular report. | [optional] [default to INCLUDE_TABULAR_HEADER_FIRST_PAGE_ONLY]
 **page_size** | **int**| The maximum number of gene reports to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, &#x60;page_token&#x60; can be used to retrieve the remaining results. | [optional] [default to 20]
 **page_token** | **str**| A page token is returned when the results count exceeds &#x60;page size&#x60;. Use this token along with previous request parameters to retrieve the next page of results. When &#x60;page_token&#x60; is empty, all results have been retrieved. | [optional] 
 **accession_filter** | [**List[str]**](str.md)| Filter tabular product report to only include the selected accessions. Use of this parameter requires the HTTP header, &#x60;accept: text/tab-separated-values&#x60;. | [optional] 
 **tax_search_subtree** | **bool**| If true, include genes from taxonomic ranks below the requested taxon. | [optional] [default to False]
 **sort_field** | **str**|  | [optional] 
 **sort_direction** | [**V2SortDirection**](.md)|  | [optional] [default to SORT_DIRECTION_UNSPECIFIED]

### Return type

[**V2reportsGeneDataReportPage**](V2reportsGeneDataReportPage.md)

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

# **gene_orthologs_by_id**
> V2reportsGeneDataReportPage gene_orthologs_by_id(gene_id, returned_content=returned_content, taxon_filter=taxon_filter, page_size=page_size, page_token=page_token)

Get a gene data report for a gene ortholog set by GeneID

Get a gene data report for a gene ortholog set by GeneID in JSON format.

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_ortholog_request_content_type import V2OrthologRequestContentType
from ncbi.datasets.openapi.models.v2reports_gene_data_report_page import V2reportsGeneDataReportPage
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
    api_instance = ncbi.datasets.openapi.GeneApi(api_client)
    gene_id = 2778 # int | One or more NCBI GeneIDs
    returned_content = COMPLETE # V2OrthologRequestContentType | Return complete gene reports, or abbreviated reports with either GeneIDs only or GeneIDs, transcript and protein counts. (optional) (default to COMPLETE)
    taxon_filter = ['[\"9606\",\"10090\"]'] # List[str] | Limit to genes from the specified NCBI Taxonomy ID or name (common or scientific) at any taxonomic rank. (optional)
    page_size = 20 # int | The maximum number of gene reports to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, `page_token` can be used to retrieve the remaining results. (optional) (default to 20)
    page_token = 'page_token_example' # str | A page token is returned when the results count exceeds `page size`. Use this token along with previous request parameters to retrieve the next page of results. When `page_token` is empty, all results have been retrieved. (optional)

    try:
        # Get a gene data report for a gene ortholog set by GeneID
        api_response = api_instance.gene_orthologs_by_id(gene_id, returned_content=returned_content, taxon_filter=taxon_filter, page_size=page_size, page_token=page_token)
        print("The response of GeneApi->gene_orthologs_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeneApi->gene_orthologs_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gene_id** | **int**| One or more NCBI GeneIDs | 
 **returned_content** | [**V2OrthologRequestContentType**](.md)| Return complete gene reports, or abbreviated reports with either GeneIDs only or GeneIDs, transcript and protein counts. | [optional] [default to COMPLETE]
 **taxon_filter** | [**List[str]**](str.md)| Limit to genes from the specified NCBI Taxonomy ID or name (common or scientific) at any taxonomic rank. | [optional] 
 **page_size** | **int**| The maximum number of gene reports to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, &#x60;page_token&#x60; can be used to retrieve the remaining results. | [optional] [default to 20]
 **page_token** | **str**| A page token is returned when the results count exceeds &#x60;page size&#x60;. Use this token along with previous request parameters to retrieve the next page of results. When &#x60;page_token&#x60; is empty, all results have been retrieved. | [optional] 

### Return type

[**V2reportsGeneDataReportPage**](V2reportsGeneDataReportPage.md)

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

# **gene_orthologs_by_post**
> V2reportsGeneDataReportPage gene_orthologs_by_post(v2_ortholog_request)

Get a gene data report for a gene ortholog set by GeneID

Get a gene data report for a gene ortholog set by GeneID in JSON format.

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_ortholog_request import V2OrthologRequest
from ncbi.datasets.openapi.models.v2reports_gene_data_report_page import V2reportsGeneDataReportPage
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
    api_instance = ncbi.datasets.openapi.GeneApi(api_client)
    v2_ortholog_request = {"gene_id":2778,"taxon_filter":["primates"]} # V2OrthologRequest | 

    try:
        # Get a gene data report for a gene ortholog set by GeneID
        api_response = api_instance.gene_orthologs_by_post(v2_ortholog_request)
        print("The response of GeneApi->gene_orthologs_by_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeneApi->gene_orthologs_by_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v2_ortholog_request** | [**V2OrthologRequest**](V2OrthologRequest.md)|  | 

### Return type

[**V2reportsGeneDataReportPage**](V2reportsGeneDataReportPage.md)

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

# **gene_product_report**
> V2reportsGeneDataReportPage gene_product_report(v2_gene_dataset_reports_request)

Get a gene product report

Get a gene product report. By default, in paged JSON format, but also available in tabular (accept: text/tab-separated-values) or JSON Lines (accept: application/x-ndjson) formats.

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_gene_dataset_reports_request import V2GeneDatasetReportsRequest
from ncbi.datasets.openapi.models.v2reports_gene_data_report_page import V2reportsGeneDataReportPage
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
    api_instance = ncbi.datasets.openapi.GeneApi(api_client)
    v2_gene_dataset_reports_request = {"gene_ids":[59067,50615]} # V2GeneDatasetReportsRequest | 

    try:
        # Get a gene product report
        api_response = api_instance.gene_product_report(v2_gene_dataset_reports_request)
        print("The response of GeneApi->gene_product_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeneApi->gene_product_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v2_gene_dataset_reports_request** | [**V2GeneDatasetReportsRequest**](V2GeneDatasetReportsRequest.md)|  | 

### Return type

[**V2reportsGeneDataReportPage**](V2reportsGeneDataReportPage.md)

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

# **gene_product_report_by_accession**
> V2reportsGeneDataReportPage gene_product_report_by_accession(accessions, table_fields=table_fields, table_format=table_format, include_tabular_header=include_tabular_header, page_size=page_size, page_token=page_token, query=query, types=types, accession_filter=accession_filter, tax_search_subtree=tax_search_subtree, sort_field=sort_field, sort_direction=sort_direction)

Get a gene product report by RefSeq nucleotide or protein accession

Get a gene product report by RefSeq nucleotide or protein accession. By default, in paged JSON format, but also available in tabular (accept: text/tab-separated-values) or JSON Lines (accept: application/x-ndjson) formats.

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_gene_type import V2GeneType
from ncbi.datasets.openapi.models.v2_include_tabular_header import V2IncludeTabularHeader
from ncbi.datasets.openapi.models.v2_sort_direction import V2SortDirection
from ncbi.datasets.openapi.models.v2reports_gene_data_report_page import V2reportsGeneDataReportPage
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
    api_instance = ncbi.datasets.openapi.GeneApi(api_client)
    accessions = ['NM_021803.4'] # List[str] | One or more RefSeq nucleotide or protein accessions
    table_fields = ['[\"gene-id\",\"gene-type\",\"description\"]'] # List[str] | Specify which fields to include in the tabular report. Additional fields are described here: [Create a table from the gene data reports](https://www.ncbi.nlm.nih.gov/datasets/docs/v2/command-line-tools/using-dataformat/gene-data-reports/). Use of this parameter requires the HTTP header, `accept: text/tab-separated-values`. (optional)
    table_format = 'summary' # str | Specify a predefined set of fields for the tabular report using built-in templates. Use of this parameter requires the HTTP header, `accept: text/tab-separated-values`. (optional)
    include_tabular_header = INCLUDE_TABULAR_HEADER_FIRST_PAGE_ONLY # V2IncludeTabularHeader | Specify when to include the table header when requesting a tabular report. (optional) (default to INCLUDE_TABULAR_HEADER_FIRST_PAGE_ONLY)
    page_size = 20 # int | The maximum number of gene reports to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, `page_token` can be used to retrieve the remaining results. (optional) (default to 20)
    page_token = 'page_token_example' # str | A page token is returned when the results count exceeds `page size`. Use this token along with previous request parameters to retrieve the next page of results. When `page_token` is empty, all results have been retrieved. (optional)
    query = 'A2M immunoglobulin' # str | Limit to genes that match the specified gene symbol, name (description), alias, locus tag or protein name. (optional)
    types = [ncbi.datasets.openapi.V2GeneType()] # List[V2GeneType] | Limit to genes matching the specified gene type. (optional)
    accession_filter = ['[\"NM_001407959.1\",\"NM_001408458.1\"]'] # List[str] | Filter tabular product report to only include the selected accessions. Use of this parameter requires the HTTP header, `accept: text/tab-separated-values`. (optional)
    tax_search_subtree = False # bool | If true, include genes from taxonomic ranks below the requested taxon. (optional) (default to False)
    sort_field = 'sort_field_example' # str |  (optional)
    sort_direction = SORT_DIRECTION_UNSPECIFIED # V2SortDirection |  (optional) (default to SORT_DIRECTION_UNSPECIFIED)

    try:
        # Get a gene product report by RefSeq nucleotide or protein accession
        api_response = api_instance.gene_product_report_by_accession(accessions, table_fields=table_fields, table_format=table_format, include_tabular_header=include_tabular_header, page_size=page_size, page_token=page_token, query=query, types=types, accession_filter=accession_filter, tax_search_subtree=tax_search_subtree, sort_field=sort_field, sort_direction=sort_direction)
        print("The response of GeneApi->gene_product_report_by_accession:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeneApi->gene_product_report_by_accession: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accessions** | [**List[str]**](str.md)| One or more RefSeq nucleotide or protein accessions | 
 **table_fields** | [**List[str]**](str.md)| Specify which fields to include in the tabular report. Additional fields are described here: [Create a table from the gene data reports](https://www.ncbi.nlm.nih.gov/datasets/docs/v2/command-line-tools/using-dataformat/gene-data-reports/). Use of this parameter requires the HTTP header, &#x60;accept: text/tab-separated-values&#x60;. | [optional] 
 **table_format** | **str**| Specify a predefined set of fields for the tabular report using built-in templates. Use of this parameter requires the HTTP header, &#x60;accept: text/tab-separated-values&#x60;. | [optional] 
 **include_tabular_header** | [**V2IncludeTabularHeader**](.md)| Specify when to include the table header when requesting a tabular report. | [optional] [default to INCLUDE_TABULAR_HEADER_FIRST_PAGE_ONLY]
 **page_size** | **int**| The maximum number of gene reports to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, &#x60;page_token&#x60; can be used to retrieve the remaining results. | [optional] [default to 20]
 **page_token** | **str**| A page token is returned when the results count exceeds &#x60;page size&#x60;. Use this token along with previous request parameters to retrieve the next page of results. When &#x60;page_token&#x60; is empty, all results have been retrieved. | [optional] 
 **query** | **str**| Limit to genes that match the specified gene symbol, name (description), alias, locus tag or protein name. | [optional] 
 **types** | [**List[V2GeneType]**](V2GeneType.md)| Limit to genes matching the specified gene type. | [optional] 
 **accession_filter** | [**List[str]**](str.md)| Filter tabular product report to only include the selected accessions. Use of this parameter requires the HTTP header, &#x60;accept: text/tab-separated-values&#x60;. | [optional] 
 **tax_search_subtree** | **bool**| If true, include genes from taxonomic ranks below the requested taxon. | [optional] [default to False]
 **sort_field** | **str**|  | [optional] 
 **sort_direction** | [**V2SortDirection**](.md)|  | [optional] [default to SORT_DIRECTION_UNSPECIFIED]

### Return type

[**V2reportsGeneDataReportPage**](V2reportsGeneDataReportPage.md)

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

# **gene_product_report_by_tax_and_symbol**
> V2reportsGeneDataReportPage gene_product_report_by_tax_and_symbol(symbols, taxon, table_fields=table_fields, table_format=table_format, include_tabular_header=include_tabular_header, page_size=page_size, page_token=page_token, query=query, types=types, tax_search_subtree=tax_search_subtree)

Get a gene product report by symbol and taxon

Get a gene product report by symbol and taxon. By default, in paged JSON format, but also available in tabular (accept: text/tab-separated-values) or JSON Lines (accept: application/x-ndjson) formats.

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_gene_type import V2GeneType
from ncbi.datasets.openapi.models.v2_include_tabular_header import V2IncludeTabularHeader
from ncbi.datasets.openapi.models.v2reports_gene_data_report_page import V2reportsGeneDataReportPage
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
    api_instance = ncbi.datasets.openapi.GeneApi(api_client)
    symbols = ['GNAS'] # List[str] | One or more gene symbols
    taxon = '9606' # str | NCBI Taxonomy ID or name (common or scientific, any taxonomic rank) for the provided gene symbol
    table_fields = ['[\"gene-id\",\"gene-type\",\"description\"]'] # List[str] | Specify which fields to include in the tabular report. Additional fields are described here: [Create a table from the gene data reports](https://www.ncbi.nlm.nih.gov/datasets/docs/v2/command-line-tools/using-dataformat/gene-data-reports/). Use of this parameter requires the HTTP header, `accept: text/tab-separated-values`. (optional)
    table_format = 'summary' # str | Specify a predefined set of fields for the tabular report using built-in templates. Use of this parameter requires the HTTP header, `accept: text/tab-separated-values`. (optional)
    include_tabular_header = INCLUDE_TABULAR_HEADER_FIRST_PAGE_ONLY # V2IncludeTabularHeader | Specify when to include the table header when requesting a tabular report. (optional) (default to INCLUDE_TABULAR_HEADER_FIRST_PAGE_ONLY)
    page_size = 20 # int | The maximum number of gene reports to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, `page_token` can be used to retrieve the remaining results. (optional) (default to 20)
    page_token = 'page_token_example' # str | A page token is returned when the results count exceeds `page size`. Use this token along with previous request parameters to retrieve the next page of results. When `page_token` is empty, all results have been retrieved. (optional)
    query = 'A2M immunoglobulin' # str | Limit to genes that match the specified gene symbol, name (description), alias, locus tag or protein name. (optional)
    types = [ncbi.datasets.openapi.V2GeneType()] # List[V2GeneType] | Limit to genes matching the specified gene type. (optional)
    tax_search_subtree = False # bool | If true, include genes from taxonomic ranks below the requested taxon. (optional) (default to False)

    try:
        # Get a gene product report by symbol and taxon
        api_response = api_instance.gene_product_report_by_tax_and_symbol(symbols, taxon, table_fields=table_fields, table_format=table_format, include_tabular_header=include_tabular_header, page_size=page_size, page_token=page_token, query=query, types=types, tax_search_subtree=tax_search_subtree)
        print("The response of GeneApi->gene_product_report_by_tax_and_symbol:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeneApi->gene_product_report_by_tax_and_symbol: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbols** | [**List[str]**](str.md)| One or more gene symbols | 
 **taxon** | **str**| NCBI Taxonomy ID or name (common or scientific, any taxonomic rank) for the provided gene symbol | 
 **table_fields** | [**List[str]**](str.md)| Specify which fields to include in the tabular report. Additional fields are described here: [Create a table from the gene data reports](https://www.ncbi.nlm.nih.gov/datasets/docs/v2/command-line-tools/using-dataformat/gene-data-reports/). Use of this parameter requires the HTTP header, &#x60;accept: text/tab-separated-values&#x60;. | [optional] 
 **table_format** | **str**| Specify a predefined set of fields for the tabular report using built-in templates. Use of this parameter requires the HTTP header, &#x60;accept: text/tab-separated-values&#x60;. | [optional] 
 **include_tabular_header** | [**V2IncludeTabularHeader**](.md)| Specify when to include the table header when requesting a tabular report. | [optional] [default to INCLUDE_TABULAR_HEADER_FIRST_PAGE_ONLY]
 **page_size** | **int**| The maximum number of gene reports to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, &#x60;page_token&#x60; can be used to retrieve the remaining results. | [optional] [default to 20]
 **page_token** | **str**| A page token is returned when the results count exceeds &#x60;page size&#x60;. Use this token along with previous request parameters to retrieve the next page of results. When &#x60;page_token&#x60; is empty, all results have been retrieved. | [optional] 
 **query** | **str**| Limit to genes that match the specified gene symbol, name (description), alias, locus tag or protein name. | [optional] 
 **types** | [**List[V2GeneType]**](V2GeneType.md)| Limit to genes matching the specified gene type. | [optional] 
 **tax_search_subtree** | **bool**| If true, include genes from taxonomic ranks below the requested taxon. | [optional] [default to False]

### Return type

[**V2reportsGeneDataReportPage**](V2reportsGeneDataReportPage.md)

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

# **gene_product_reports_by_id**
> V2reportsGeneDataReportPage gene_product_reports_by_id(gene_ids, table_fields=table_fields, table_format=table_format, include_tabular_header=include_tabular_header, page_size=page_size, page_token=page_token, query=query, types=types, accession_filter=accession_filter, sort_field=sort_field, sort_direction=sort_direction)

Get a gene product report by GeneID

Get a gene product report by GeneID. By default, in paged JSON format, but also available in tabular (accept: text/tab-separated-values) or JSON Lines (accept: application/x-ndjson) formats.

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_gene_type import V2GeneType
from ncbi.datasets.openapi.models.v2_include_tabular_header import V2IncludeTabularHeader
from ncbi.datasets.openapi.models.v2_sort_direction import V2SortDirection
from ncbi.datasets.openapi.models.v2reports_gene_data_report_page import V2reportsGeneDataReportPage
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
    api_instance = ncbi.datasets.openapi.GeneApi(api_client)
    gene_ids = [59067] # List[int] | One or more NCBI GeneIDs
    table_fields = ['[\"gene-id\",\"gene-type\",\"description\"]'] # List[str] | Specify which fields to include in the tabular report. Additional fields are described here: [Create a table from the gene data reports](https://www.ncbi.nlm.nih.gov/datasets/docs/v2/command-line-tools/using-dataformat/gene-data-reports/). Use of this parameter requires the HTTP header, `accept: text/tab-separated-values`. (optional)
    table_format = 'summary' # str | Specify a predefined set of fields for the tabular report using built-in templates. Use of this parameter requires the HTTP header, `accept: text/tab-separated-values`. (optional)
    include_tabular_header = INCLUDE_TABULAR_HEADER_FIRST_PAGE_ONLY # V2IncludeTabularHeader | Specify when to include the table header when requesting a tabular report. (optional) (default to INCLUDE_TABULAR_HEADER_FIRST_PAGE_ONLY)
    page_size = 20 # int | The maximum number of gene reports to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, `page_token` can be used to retrieve the remaining results. (optional) (default to 20)
    page_token = 'page_token_example' # str | A page token is returned when the results count exceeds `page size`. Use this token along with previous request parameters to retrieve the next page of results. When `page_token` is empty, all results have been retrieved. (optional)
    query = 'A2M immunoglobulin' # str | Limit to genes that match the specified gene symbol, name (description), alias, locus tag or protein name. (optional)
    types = [ncbi.datasets.openapi.V2GeneType()] # List[V2GeneType] | Limit to genes matching the specified gene type. (optional)
    accession_filter = ['[\"NM_001407959.1\",\"NM_001408458.1\"]'] # List[str] | Filter tabular product report to only include the selected accessions. Use of this parameter requires the HTTP header, `accept: text/tab-separated-values`. (optional)
    sort_field = 'sort_field_example' # str |  (optional)
    sort_direction = SORT_DIRECTION_UNSPECIFIED # V2SortDirection |  (optional) (default to SORT_DIRECTION_UNSPECIFIED)

    try:
        # Get a gene product report by GeneID
        api_response = api_instance.gene_product_reports_by_id(gene_ids, table_fields=table_fields, table_format=table_format, include_tabular_header=include_tabular_header, page_size=page_size, page_token=page_token, query=query, types=types, accession_filter=accession_filter, sort_field=sort_field, sort_direction=sort_direction)
        print("The response of GeneApi->gene_product_reports_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeneApi->gene_product_reports_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gene_ids** | [**List[int]**](int.md)| One or more NCBI GeneIDs | 
 **table_fields** | [**List[str]**](str.md)| Specify which fields to include in the tabular report. Additional fields are described here: [Create a table from the gene data reports](https://www.ncbi.nlm.nih.gov/datasets/docs/v2/command-line-tools/using-dataformat/gene-data-reports/). Use of this parameter requires the HTTP header, &#x60;accept: text/tab-separated-values&#x60;. | [optional] 
 **table_format** | **str**| Specify a predefined set of fields for the tabular report using built-in templates. Use of this parameter requires the HTTP header, &#x60;accept: text/tab-separated-values&#x60;. | [optional] 
 **include_tabular_header** | [**V2IncludeTabularHeader**](.md)| Specify when to include the table header when requesting a tabular report. | [optional] [default to INCLUDE_TABULAR_HEADER_FIRST_PAGE_ONLY]
 **page_size** | **int**| The maximum number of gene reports to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, &#x60;page_token&#x60; can be used to retrieve the remaining results. | [optional] [default to 20]
 **page_token** | **str**| A page token is returned when the results count exceeds &#x60;page size&#x60;. Use this token along with previous request parameters to retrieve the next page of results. When &#x60;page_token&#x60; is empty, all results have been retrieved. | [optional] 
 **query** | **str**| Limit to genes that match the specified gene symbol, name (description), alias, locus tag or protein name. | [optional] 
 **types** | [**List[V2GeneType]**](V2GeneType.md)| Limit to genes matching the specified gene type. | [optional] 
 **accession_filter** | [**List[str]**](str.md)| Filter tabular product report to only include the selected accessions. Use of this parameter requires the HTTP header, &#x60;accept: text/tab-separated-values&#x60;. | [optional] 
 **sort_field** | **str**|  | [optional] 
 **sort_direction** | [**V2SortDirection**](.md)|  | [optional] [default to SORT_DIRECTION_UNSPECIFIED]

### Return type

[**V2reportsGeneDataReportPage**](V2reportsGeneDataReportPage.md)

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

# **gene_product_reports_by_locus_tags**
> V2reportsGeneDataReportPage gene_product_reports_by_locus_tags(locus_tags, table_fields=table_fields, table_format=table_format, include_tabular_header=include_tabular_header, page_size=page_size, page_token=page_token, query=query, types=types, accession_filter=accession_filter, sort_field=sort_field)

Get a gene product report by locus tag

Get a gene product report by gene locus tag. By default, in paged JSON format, but also available in tabular (accept: text/tab-separated-values) or JSON Lines (accept: application/x-ndjson) formats.

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_gene_type import V2GeneType
from ncbi.datasets.openapi.models.v2_include_tabular_header import V2IncludeTabularHeader
from ncbi.datasets.openapi.models.v2reports_gene_data_report_page import V2reportsGeneDataReportPage
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
    api_instance = ncbi.datasets.openapi.GeneApi(api_client)
    locus_tags = ['b0001'] # List[str] | Gene locus tags
    table_fields = ['[\"gene-id\",\"gene-type\",\"description\"]'] # List[str] | Specify which fields to include in the tabular report. Additional fields are described here: [Create a table from the gene data reports](https://www.ncbi.nlm.nih.gov/datasets/docs/v2/command-line-tools/using-dataformat/gene-data-reports/). Use of this parameter requires the HTTP header, `accept: text/tab-separated-values`. (optional)
    table_format = 'summary' # str | Specify a predefined set of fields for the tabular report using built-in templates. Use of this parameter requires the HTTP header, `accept: text/tab-separated-values`. (optional)
    include_tabular_header = INCLUDE_TABULAR_HEADER_FIRST_PAGE_ONLY # V2IncludeTabularHeader | Specify when to include the table header when requesting a tabular report. (optional) (default to INCLUDE_TABULAR_HEADER_FIRST_PAGE_ONLY)
    page_size = 20 # int | The maximum number of gene reports to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, `page_token` can be used to retrieve the remaining results. (optional) (default to 20)
    page_token = 'page_token_example' # str | A page token is returned when the results count exceeds `page size`. Use this token along with previous request parameters to retrieve the next page of results. When `page_token` is empty, all results have been retrieved. (optional)
    query = 'A2M immunoglobulin' # str | Limit to genes that match the specified gene symbol, name (description), alias, locus tag or protein name. (optional)
    types = [ncbi.datasets.openapi.V2GeneType()] # List[V2GeneType] | Limit to genes matching the specified gene type. (optional)
    accession_filter = ['[\"NM_001407959.1\",\"NM_001408458.1\"]'] # List[str] | Filter tabular product report to only include the selected accessions. Use of this parameter requires the HTTP header, `accept: text/tab-separated-values`. (optional)
    sort_field = 'sort_field_example' # str |  (optional)

    try:
        # Get a gene product report by locus tag
        api_response = api_instance.gene_product_reports_by_locus_tags(locus_tags, table_fields=table_fields, table_format=table_format, include_tabular_header=include_tabular_header, page_size=page_size, page_token=page_token, query=query, types=types, accession_filter=accession_filter, sort_field=sort_field)
        print("The response of GeneApi->gene_product_reports_by_locus_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeneApi->gene_product_reports_by_locus_tags: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **locus_tags** | [**List[str]**](str.md)| Gene locus tags | 
 **table_fields** | [**List[str]**](str.md)| Specify which fields to include in the tabular report. Additional fields are described here: [Create a table from the gene data reports](https://www.ncbi.nlm.nih.gov/datasets/docs/v2/command-line-tools/using-dataformat/gene-data-reports/). Use of this parameter requires the HTTP header, &#x60;accept: text/tab-separated-values&#x60;. | [optional] 
 **table_format** | **str**| Specify a predefined set of fields for the tabular report using built-in templates. Use of this parameter requires the HTTP header, &#x60;accept: text/tab-separated-values&#x60;. | [optional] 
 **include_tabular_header** | [**V2IncludeTabularHeader**](.md)| Specify when to include the table header when requesting a tabular report. | [optional] [default to INCLUDE_TABULAR_HEADER_FIRST_PAGE_ONLY]
 **page_size** | **int**| The maximum number of gene reports to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, &#x60;page_token&#x60; can be used to retrieve the remaining results. | [optional] [default to 20]
 **page_token** | **str**| A page token is returned when the results count exceeds &#x60;page size&#x60;. Use this token along with previous request parameters to retrieve the next page of results. When &#x60;page_token&#x60; is empty, all results have been retrieved. | [optional] 
 **query** | **str**| Limit to genes that match the specified gene symbol, name (description), alias, locus tag or protein name. | [optional] 
 **types** | [**List[V2GeneType]**](V2GeneType.md)| Limit to genes matching the specified gene type. | [optional] 
 **accession_filter** | [**List[str]**](str.md)| Filter tabular product report to only include the selected accessions. Use of this parameter requires the HTTP header, &#x60;accept: text/tab-separated-values&#x60;. | [optional] 
 **sort_field** | **str**|  | [optional] 

### Return type

[**V2reportsGeneDataReportPage**](V2reportsGeneDataReportPage.md)

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

# **gene_product_reports_by_taxon**
> V2reportsGeneDataReportPage gene_product_reports_by_taxon(taxon, table_fields=table_fields, table_format=table_format, include_tabular_header=include_tabular_header, page_size=page_size, page_token=page_token, query=query, types=types, tax_search_subtree=tax_search_subtree)

Get a gene product report by taxon

Get a gene product report by taxon. By default, in paged JSON format, but also available in tabular (accept: text/tab-separated-values) or JSON Lines (accept: application/x-ndjson) formats.

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_gene_type import V2GeneType
from ncbi.datasets.openapi.models.v2_include_tabular_header import V2IncludeTabularHeader
from ncbi.datasets.openapi.models.v2reports_gene_data_report_page import V2reportsGeneDataReportPage
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
    api_instance = ncbi.datasets.openapi.GeneApi(api_client)
    taxon = '9606' # str | NCBI Taxonomy ID or name (common or scientific) that the genes are annotated at
    table_fields = ['[\"gene-id\",\"gene-type\",\"description\"]'] # List[str] | Specify which fields to include in the tabular report. Additional fields are described here: [Create a table from the gene data reports](https://www.ncbi.nlm.nih.gov/datasets/docs/v2/command-line-tools/using-dataformat/gene-data-reports/). Use of this parameter requires the HTTP header, `accept: text/tab-separated-values`. (optional)
    table_format = 'summary' # str | Specify a predefined set of fields for the tabular report using built-in templates. Use of this parameter requires the HTTP header, `accept: text/tab-separated-values`. (optional)
    include_tabular_header = INCLUDE_TABULAR_HEADER_FIRST_PAGE_ONLY # V2IncludeTabularHeader | Specify when to include the table header when requesting a tabular report. (optional) (default to INCLUDE_TABULAR_HEADER_FIRST_PAGE_ONLY)
    page_size = 20 # int | The maximum number of gene reports to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, `page_token` can be used to retrieve the remaining results. (optional) (default to 20)
    page_token = 'page_token_example' # str | A page token is returned when the results count exceeds `page size`. Use this token along with previous request parameters to retrieve the next page of results. When `page_token` is empty, all results have been retrieved. (optional)
    query = 'A2M immunoglobulin' # str | Limit to genes that match the specified gene symbol, name (description), alias, locus tag or protein name. (optional)
    types = [ncbi.datasets.openapi.V2GeneType()] # List[V2GeneType] | Limit to genes matching the specified gene type. (optional)
    tax_search_subtree = False # bool | If true, include genes from taxonomic ranks below the requested taxon. (optional) (default to False)

    try:
        # Get a gene product report by taxon
        api_response = api_instance.gene_product_reports_by_taxon(taxon, table_fields=table_fields, table_format=table_format, include_tabular_header=include_tabular_header, page_size=page_size, page_token=page_token, query=query, types=types, tax_search_subtree=tax_search_subtree)
        print("The response of GeneApi->gene_product_reports_by_taxon:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeneApi->gene_product_reports_by_taxon: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **taxon** | **str**| NCBI Taxonomy ID or name (common or scientific) that the genes are annotated at | 
 **table_fields** | [**List[str]**](str.md)| Specify which fields to include in the tabular report. Additional fields are described here: [Create a table from the gene data reports](https://www.ncbi.nlm.nih.gov/datasets/docs/v2/command-line-tools/using-dataformat/gene-data-reports/). Use of this parameter requires the HTTP header, &#x60;accept: text/tab-separated-values&#x60;. | [optional] 
 **table_format** | **str**| Specify a predefined set of fields for the tabular report using built-in templates. Use of this parameter requires the HTTP header, &#x60;accept: text/tab-separated-values&#x60;. | [optional] 
 **include_tabular_header** | [**V2IncludeTabularHeader**](.md)| Specify when to include the table header when requesting a tabular report. | [optional] [default to INCLUDE_TABULAR_HEADER_FIRST_PAGE_ONLY]
 **page_size** | **int**| The maximum number of gene reports to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, &#x60;page_token&#x60; can be used to retrieve the remaining results. | [optional] [default to 20]
 **page_token** | **str**| A page token is returned when the results count exceeds &#x60;page size&#x60;. Use this token along with previous request parameters to retrieve the next page of results. When &#x60;page_token&#x60; is empty, all results have been retrieved. | [optional] 
 **query** | **str**| Limit to genes that match the specified gene symbol, name (description), alias, locus tag or protein name. | [optional] 
 **types** | [**List[V2GeneType]**](V2GeneType.md)| Limit to genes matching the specified gene type. | [optional] 
 **tax_search_subtree** | **bool**| If true, include genes from taxonomic ranks below the requested taxon. | [optional] [default to False]

### Return type

[**V2reportsGeneDataReportPage**](V2reportsGeneDataReportPage.md)

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

# **gene_reports_by_id**
> V2reportsGeneDataReportPage gene_reports_by_id(gene_ids, returned_content=returned_content, locus_tags=locus_tags, table_fields=table_fields, include_tabular_header=include_tabular_header, page_size=page_size, page_token=page_token, accession_filter=accession_filter, tax_search_subtree=tax_search_subtree, sort_field=sort_field, sort_direction=sort_direction)

Get gene reports by GeneID (deprecated)

Get a gene summary by GeneID. By default, in paged JSON format, but also available as tabular (accept: text/tab-separated-values) or json-lines (accept: application/x-ndjson)

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_gene_dataset_reports_request_content_type import V2GeneDatasetReportsRequestContentType
from ncbi.datasets.openapi.models.v2_include_tabular_header import V2IncludeTabularHeader
from ncbi.datasets.openapi.models.v2_sort_direction import V2SortDirection
from ncbi.datasets.openapi.models.v2reports_gene_data_report_page import V2reportsGeneDataReportPage
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
    api_instance = ncbi.datasets.openapi.GeneApi(api_client)
    gene_ids = [59067] # List[int] | One or more NCBI GeneIDs
    returned_content = COMPLETE # V2GeneDatasetReportsRequestContentType | Return complete gene reports, or abbreviated reports with either GeneIDs only or GeneIDs, transcript and protein counts. (optional) (default to COMPLETE)
    locus_tags = ['b0001'] # List[str] | Gene locus tags (optional)
    table_fields = ['[\"gene-id\",\"gene-type\",\"description\"]'] # List[str] | Specify which fields to include in the tabular report. Additional fields are described here: [Create a table from the gene data reports](https://www.ncbi.nlm.nih.gov/datasets/docs/v2/command-line-tools/using-dataformat/gene-data-reports/). Use of this parameter requires the HTTP header, `accept: text/tab-separated-values`. (optional)
    include_tabular_header = INCLUDE_TABULAR_HEADER_FIRST_PAGE_ONLY # V2IncludeTabularHeader | Specify when to include the table header when requesting a tabular report. (optional) (default to INCLUDE_TABULAR_HEADER_FIRST_PAGE_ONLY)
    page_size = 20 # int | The maximum number of gene reports to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, `page_token` can be used to retrieve the remaining results. (optional) (default to 20)
    page_token = 'page_token_example' # str | A page token is returned when the results count exceeds `page size`. Use this token along with previous request parameters to retrieve the next page of results. When `page_token` is empty, all results have been retrieved. (optional)
    accession_filter = ['[\"NM_001407959.1\",\"NM_001408458.1\"]'] # List[str] | Filter tabular product report to only include the selected accessions. Use of this parameter requires the HTTP header, `accept: text/tab-separated-values`. (optional)
    tax_search_subtree = False # bool | If true, include genes from taxonomic ranks below the requested taxon. (optional) (default to False)
    sort_field = 'sort_field_example' # str |  (optional)
    sort_direction = SORT_DIRECTION_UNSPECIFIED # V2SortDirection |  (optional) (default to SORT_DIRECTION_UNSPECIFIED)

    try:
        # Get gene reports by GeneID (deprecated)
        api_response = api_instance.gene_reports_by_id(gene_ids, returned_content=returned_content, locus_tags=locus_tags, table_fields=table_fields, include_tabular_header=include_tabular_header, page_size=page_size, page_token=page_token, accession_filter=accession_filter, tax_search_subtree=tax_search_subtree, sort_field=sort_field, sort_direction=sort_direction)
        print("The response of GeneApi->gene_reports_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeneApi->gene_reports_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gene_ids** | [**List[int]**](int.md)| One or more NCBI GeneIDs | 
 **returned_content** | [**V2GeneDatasetReportsRequestContentType**](.md)| Return complete gene reports, or abbreviated reports with either GeneIDs only or GeneIDs, transcript and protein counts. | [optional] [default to COMPLETE]
 **locus_tags** | [**List[str]**](str.md)| Gene locus tags | [optional] 
 **table_fields** | [**List[str]**](str.md)| Specify which fields to include in the tabular report. Additional fields are described here: [Create a table from the gene data reports](https://www.ncbi.nlm.nih.gov/datasets/docs/v2/command-line-tools/using-dataformat/gene-data-reports/). Use of this parameter requires the HTTP header, &#x60;accept: text/tab-separated-values&#x60;. | [optional] 
 **include_tabular_header** | [**V2IncludeTabularHeader**](.md)| Specify when to include the table header when requesting a tabular report. | [optional] [default to INCLUDE_TABULAR_HEADER_FIRST_PAGE_ONLY]
 **page_size** | **int**| The maximum number of gene reports to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, &#x60;page_token&#x60; can be used to retrieve the remaining results. | [optional] [default to 20]
 **page_token** | **str**| A page token is returned when the results count exceeds &#x60;page size&#x60;. Use this token along with previous request parameters to retrieve the next page of results. When &#x60;page_token&#x60; is empty, all results have been retrieved. | [optional] 
 **accession_filter** | [**List[str]**](str.md)| Filter tabular product report to only include the selected accessions. Use of this parameter requires the HTTP header, &#x60;accept: text/tab-separated-values&#x60;. | [optional] 
 **tax_search_subtree** | **bool**| If true, include genes from taxonomic ranks below the requested taxon. | [optional] [default to False]
 **sort_field** | **str**|  | [optional] 
 **sort_direction** | [**V2SortDirection**](.md)|  | [optional] [default to SORT_DIRECTION_UNSPECIFIED]

### Return type

[**V2reportsGeneDataReportPage**](V2reportsGeneDataReportPage.md)

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

# **gene_reports_by_taxon**
> V2reportsGeneDataReportPage gene_reports_by_taxon(taxon, returned_content=returned_content, locus_tags=locus_tags, table_fields=table_fields, include_tabular_header=include_tabular_header, page_size=page_size, page_token=page_token, query=query, types=types, accession_filter=accession_filter, tax_search_subtree=tax_search_subtree, sort_field=sort_field, sort_direction=sort_direction)

Get gene reports by taxonomic identifier (deprecated)

Get a gene summary for a specified NCBI Taxonomy ID or name (common or scientific). By default, in paged JSON format, but also available as tabular (accept: text/tab-separated-values) or json-lines (accept: application/x-ndjson)

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_gene_dataset_reports_request_content_type import V2GeneDatasetReportsRequestContentType
from ncbi.datasets.openapi.models.v2_gene_type import V2GeneType
from ncbi.datasets.openapi.models.v2_include_tabular_header import V2IncludeTabularHeader
from ncbi.datasets.openapi.models.v2_sort_direction import V2SortDirection
from ncbi.datasets.openapi.models.v2reports_gene_data_report_page import V2reportsGeneDataReportPage
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
    api_instance = ncbi.datasets.openapi.GeneApi(api_client)
    taxon = '9606' # str | NCBI Taxonomy ID or name (common or scientific) that the genes are annotated at
    returned_content = COMPLETE # V2GeneDatasetReportsRequestContentType | Return complete gene reports, or abbreviated reports with either GeneIDs only or GeneIDs, transcript and protein counts. (optional) (default to COMPLETE)
    locus_tags = ['b0001'] # List[str] | Gene locus tags (optional)
    table_fields = ['[\"gene-id\",\"gene-type\",\"description\"]'] # List[str] | Specify which fields to include in the tabular report. Additional fields are described here: [Create a table from the gene data reports](https://www.ncbi.nlm.nih.gov/datasets/docs/v2/command-line-tools/using-dataformat/gene-data-reports/). Use of this parameter requires the HTTP header, `accept: text/tab-separated-values`. (optional)
    include_tabular_header = INCLUDE_TABULAR_HEADER_FIRST_PAGE_ONLY # V2IncludeTabularHeader | Specify when to include the table header when requesting a tabular report. (optional) (default to INCLUDE_TABULAR_HEADER_FIRST_PAGE_ONLY)
    page_size = 20 # int | The maximum number of gene reports to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, `page_token` can be used to retrieve the remaining results. (optional) (default to 20)
    page_token = 'page_token_example' # str | A page token is returned when the results count exceeds `page size`. Use this token along with previous request parameters to retrieve the next page of results. When `page_token` is empty, all results have been retrieved. (optional)
    query = 'A2M immunoglobulin' # str | Limit to genes that match the specified gene symbol, name (description), alias, locus tag or protein name. (optional)
    types = [ncbi.datasets.openapi.V2GeneType()] # List[V2GeneType] | Limit to genes matching the specified gene type. (optional)
    accession_filter = ['[\"NM_001407959.1\",\"NM_001408458.1\"]'] # List[str] | Filter tabular product report to only include the selected accessions. Use of this parameter requires the HTTP header, `accept: text/tab-separated-values`. (optional)
    tax_search_subtree = False # bool | If true, include genes from taxonomic ranks below the requested taxon. (optional) (default to False)
    sort_field = 'sort_field_example' # str |  (optional)
    sort_direction = SORT_DIRECTION_UNSPECIFIED # V2SortDirection |  (optional) (default to SORT_DIRECTION_UNSPECIFIED)

    try:
        # Get gene reports by taxonomic identifier (deprecated)
        api_response = api_instance.gene_reports_by_taxon(taxon, returned_content=returned_content, locus_tags=locus_tags, table_fields=table_fields, include_tabular_header=include_tabular_header, page_size=page_size, page_token=page_token, query=query, types=types, accession_filter=accession_filter, tax_search_subtree=tax_search_subtree, sort_field=sort_field, sort_direction=sort_direction)
        print("The response of GeneApi->gene_reports_by_taxon:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeneApi->gene_reports_by_taxon: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **taxon** | **str**| NCBI Taxonomy ID or name (common or scientific) that the genes are annotated at | 
 **returned_content** | [**V2GeneDatasetReportsRequestContentType**](.md)| Return complete gene reports, or abbreviated reports with either GeneIDs only or GeneIDs, transcript and protein counts. | [optional] [default to COMPLETE]
 **locus_tags** | [**List[str]**](str.md)| Gene locus tags | [optional] 
 **table_fields** | [**List[str]**](str.md)| Specify which fields to include in the tabular report. Additional fields are described here: [Create a table from the gene data reports](https://www.ncbi.nlm.nih.gov/datasets/docs/v2/command-line-tools/using-dataformat/gene-data-reports/). Use of this parameter requires the HTTP header, &#x60;accept: text/tab-separated-values&#x60;. | [optional] 
 **include_tabular_header** | [**V2IncludeTabularHeader**](.md)| Specify when to include the table header when requesting a tabular report. | [optional] [default to INCLUDE_TABULAR_HEADER_FIRST_PAGE_ONLY]
 **page_size** | **int**| The maximum number of gene reports to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, &#x60;page_token&#x60; can be used to retrieve the remaining results. | [optional] [default to 20]
 **page_token** | **str**| A page token is returned when the results count exceeds &#x60;page size&#x60;. Use this token along with previous request parameters to retrieve the next page of results. When &#x60;page_token&#x60; is empty, all results have been retrieved. | [optional] 
 **query** | **str**| Limit to genes that match the specified gene symbol, name (description), alias, locus tag or protein name. | [optional] 
 **types** | [**List[V2GeneType]**](V2GeneType.md)| Limit to genes matching the specified gene type. | [optional] 
 **accession_filter** | [**List[str]**](str.md)| Filter tabular product report to only include the selected accessions. Use of this parameter requires the HTTP header, &#x60;accept: text/tab-separated-values&#x60;. | [optional] 
 **tax_search_subtree** | **bool**| If true, include genes from taxonomic ranks below the requested taxon. | [optional] [default to False]
 **sort_field** | **str**|  | [optional] 
 **sort_direction** | [**V2SortDirection**](.md)|  | [optional] [default to SORT_DIRECTION_UNSPECIFIED]

### Return type

[**V2reportsGeneDataReportPage**](V2reportsGeneDataReportPage.md)

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

