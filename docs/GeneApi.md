# ncbi.datasets.openapi.GeneApi

All URIs are relative to *https://api.ncbi.nlm.nih.gov/datasets/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download_gene_package**](GeneApi.md#download_gene_package) | **GET** /gene/id/{gene_ids}/download | Get a gene dataset by gene ID
[**download_gene_package_post**](GeneApi.md#download_gene_package_post) | **POST** /gene/download | Get a gene dataset by POST
[**gene_chromosome_summary**](GeneApi.md#gene_chromosome_summary) | **GET** /gene/taxon/{taxon}/annotation/{annotation_name}/chromosome_summary | Get summary of chromosomes for a particular taxon&#39;s annotation
[**gene_counts_for_taxon**](GeneApi.md#gene_counts_for_taxon) | **GET** /gene/taxon/{taxon}/counts | Get gene counts by taxonomic identifier
[**gene_counts_for_taxon_by_post**](GeneApi.md#gene_counts_for_taxon_by_post) | **POST** /gene/taxon/counts | Get gene counts by taxonomic identifier
[**gene_dataset_report**](GeneApi.md#gene_dataset_report) | **POST** /gene/dataset_report | Get gene dataset report as JSON
[**gene_dataset_report_by_accession**](GeneApi.md#gene_dataset_report_by_accession) | **GET** /gene/accession/{accessions}/dataset_report | Get dataset reports by accession IDs
[**gene_dataset_report_by_tax_and_symbol**](GeneApi.md#gene_dataset_report_by_tax_and_symbol) | **GET** /gene/symbol/{symbols}/taxon/{taxon}/dataset_report | Get dataset reports by taxons.
[**gene_dataset_reports_by_id**](GeneApi.md#gene_dataset_reports_by_id) | **GET** /gene/id/{gene_ids}/dataset_report | Get dataset reports by gene IDs.
[**gene_dataset_reports_by_locus_tag**](GeneApi.md#gene_dataset_reports_by_locus_tag) | **GET** /gene/locus_tag/{locus_tags}/dataset_report | Get gene dataset reports by locus tag
[**gene_dataset_reports_by_taxon**](GeneApi.md#gene_dataset_reports_by_taxon) | **GET** /gene/taxon/{taxon}/dataset_report | Get gene dataset reports by taxonomic identifier
[**gene_download_summary_by_id**](GeneApi.md#gene_download_summary_by_id) | **GET** /gene/id/{gene_ids}/download_summary | Get gene download summary by GeneID
[**gene_download_summary_by_post**](GeneApi.md#gene_download_summary_by_post) | **POST** /gene/download_summary | Get gene download summary
[**gene_links_by_id**](GeneApi.md#gene_links_by_id) | **GET** /gene/id/{gene_ids}/links | Get gene links by gene ID
[**gene_links_by_id_by_post**](GeneApi.md#gene_links_by_id_by_post) | **POST** /gene/links | Get gene links by gene ID
[**gene_metadata_by_accession**](GeneApi.md#gene_metadata_by_accession) | **GET** /gene/accession/{accessions} | Get gene metadata by RefSeq Accession
[**gene_metadata_by_post**](GeneApi.md#gene_metadata_by_post) | **POST** /gene | Get gene metadata as JSON
[**gene_metadata_by_tax_and_symbol**](GeneApi.md#gene_metadata_by_tax_and_symbol) | **GET** /gene/symbol/{symbols}/taxon/{taxon} | Get gene metadata by gene symbol
[**gene_orthologs_by_id**](GeneApi.md#gene_orthologs_by_id) | **GET** /gene/id/{gene_id}/orthologs | Get gene orthologs by gene ID
[**gene_orthologs_by_post**](GeneApi.md#gene_orthologs_by_post) | **POST** /gene/orthologs | Get gene orthologs by gene ID
[**gene_product_report**](GeneApi.md#gene_product_report) | **POST** /gene/product_report | Get gene product reports as JSON
[**gene_product_report_by_accession**](GeneApi.md#gene_product_report_by_accession) | **GET** /gene/accession/{accessions}/product_report | Get gene product reports by accession IDs
[**gene_product_report_by_tax_and_symbol**](GeneApi.md#gene_product_report_by_tax_and_symbol) | **GET** /gene/symbol/{symbols}/taxon/{taxon}/product_report | Get product reports by taxon.
[**gene_product_reports_by_id**](GeneApi.md#gene_product_reports_by_id) | **GET** /gene/id/{gene_ids}/product_report | Get gene product reports by gene IDs.
[**gene_product_reports_by_locus_tags**](GeneApi.md#gene_product_reports_by_locus_tags) | **GET** /gene/locus_tag/{locus_tags}/product_report | Get gene product reports by locus tags
[**gene_product_reports_by_taxon**](GeneApi.md#gene_product_reports_by_taxon) | **GET** /gene/taxon/{taxon}/product_report | Get gene product reports by taxonomic identifier
[**gene_reports_by_id**](GeneApi.md#gene_reports_by_id) | **GET** /gene/id/{gene_ids} | Get gene reports by GeneID
[**gene_reports_by_taxon**](GeneApi.md#gene_reports_by_taxon) | **GET** /gene/taxon/{taxon} | Get gene reports by taxonomic identifier


# **download_gene_package**
> bytearray download_gene_package(gene_ids, include_annotation_type=include_annotation_type, fasta_filter=fasta_filter, accession_filter=accession_filter, aux_report=aux_report, tabular_reports=tabular_reports, table_fields=table_fields, table_report_type=table_report_type, filename=filename)

Get a gene dataset by gene ID

Get a gene dataset including gene, transcript and protein fasta sequence, annotation and metadata by gene ID.

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
    gene_ids = [[59067]] # List[int] | NCBI gene ids
    include_annotation_type = [ncbi.datasets.openapi.V2Fasta()] # List[V2Fasta] | Select additional types of annotation to include in the data package.  If unset, no annotation is provided. (optional)
    fasta_filter = ['fasta_filter_example'] # List[str] | Limit the FASTA sequences in the datasets package to these transcript and protein accessions (deprecated) (optional)
    accession_filter = ['[\"NM_001408458.1\",\"NM_001407959.1\"]'] # List[str] | Limit the FASTA sequences and tabular product report in the datasets package to these transcript and protein accessions (optional)
    aux_report = [ncbi.datasets.openapi.V2GeneDatasetRequestGeneDatasetReportType()] # List[V2GeneDatasetRequestGeneDatasetReportType] | list additional reports to include with download. Data report is included by default. (optional)
    tabular_reports = [ncbi.datasets.openapi.V2GeneDatasetRequestGeneDatasetReportType()] # List[V2GeneDatasetRequestGeneDatasetReportType] |  (optional)
    table_fields = ['table_fields_example'] # List[str] | Specify which fields to include in the tabular report. This is currently deprecated - use tabular_reports instead. (optional)
    table_report_type = ncbi.datasets.openapi.V2GeneDatasetRequestGeneDatasetReportType() # V2GeneDatasetRequestGeneDatasetReportType | Specify the report from which the table fields will be taken. This is currently deprecated - use tabular_reports instead. (optional)
    filename = 'ncbi_dataset.zip' # str | Output file name. (optional) (default to 'ncbi_dataset.zip')

    try:
        # Get a gene dataset by gene ID
        api_response = api_instance.download_gene_package(gene_ids, include_annotation_type=include_annotation_type, fasta_filter=fasta_filter, accession_filter=accession_filter, aux_report=aux_report, tabular_reports=tabular_reports, table_fields=table_fields, table_report_type=table_report_type, filename=filename)
        print("The response of GeneApi->download_gene_package:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeneApi->download_gene_package: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gene_ids** | [**List[int]**](int.md)| NCBI gene ids | 
 **include_annotation_type** | [**List[V2Fasta]**](V2Fasta.md)| Select additional types of annotation to include in the data package.  If unset, no annotation is provided. | [optional] 
 **fasta_filter** | [**List[str]**](str.md)| Limit the FASTA sequences in the datasets package to these transcript and protein accessions (deprecated) | [optional] 
 **accession_filter** | [**List[str]**](str.md)| Limit the FASTA sequences and tabular product report in the datasets package to these transcript and protein accessions | [optional] 
 **aux_report** | [**List[V2GeneDatasetRequestGeneDatasetReportType]**](V2GeneDatasetRequestGeneDatasetReportType.md)| list additional reports to include with download. Data report is included by default. | [optional] 
 **tabular_reports** | [**List[V2GeneDatasetRequestGeneDatasetReportType]**](V2GeneDatasetRequestGeneDatasetReportType.md)|  | [optional] 
 **table_fields** | [**List[str]**](str.md)| Specify which fields to include in the tabular report. This is currently deprecated - use tabular_reports instead. | [optional] 
 **table_report_type** | [**V2GeneDatasetRequestGeneDatasetReportType**](.md)| Specify the report from which the table fields will be taken. This is currently deprecated - use tabular_reports instead. | [optional] 
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

Get a gene dataset by POST

Get a gene dataset including gene, transcript and protein fasta sequence, annotation and metadata by POST.

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
    v2_gene_dataset_request = {"gene_ids":[59067,50615]} # V2GeneDatasetRequest | 
    filename = 'ncbi_dataset.zip' # str | Output file name. (optional) (default to 'ncbi_dataset.zip')

    try:
        # Get a gene dataset by POST
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

Get summary of chromosomes for a particular taxon's annotation

Get summary of chromosomes for a particular taxon's annotation.

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
    taxon = '9117' # str | 
    annotation_name = 'GCF_028858705.1-RS_2023_03' # str | 

    try:
        # Get summary of chromosomes for a particular taxon's annotation
        api_response = api_instance.gene_chromosome_summary(taxon, annotation_name)
        print("The response of GeneApi->gene_chromosome_summary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeneApi->gene_chromosome_summary: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **taxon** | **str**|  | 
 **annotation_name** | **str**|  | 

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

Get gene counts by taxonomic identifier

Get gene counts for a specified NCBI Taxonomy ID or name (common or scientific) in JSON format.

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
        # Get gene counts by taxonomic identifier
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

Get gene counts by taxonomic identifier

Get gene counts for a specified NCBI Taxonomy ID or name (common or scientific) in JSON format.

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
        # Get gene counts by taxonomic identifier
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

Get gene dataset report as JSON

Get gene dataset report. By default, in paged JSON format, but also available as tabular (accept: text/tab-separated-values) or json-lines (accept: application/x-ndjson)

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
        # Get gene dataset report as JSON
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
> V2reportsGeneDataReportPage gene_dataset_report_by_accession(accessions, returned_content=returned_content, table_fields=table_fields, table_format=table_format, include_tabular_header=include_tabular_header, page_size=page_size, page_token=page_token, query=query, types=types)

Get dataset reports by accession IDs

Get dataset reports by accession IDs.  By default, in paged JSON format, but also available as tabular (accept: text/tab-separated-values) or json-lines (accept: application/x-ndjson)

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
    accessions = ['[\"NM_021803.4\"]'] # List[str] | RNA or Protein accessions.
    returned_content = ncbi.datasets.openapi.V2GeneDatasetReportsRequestContentType() # V2GeneDatasetReportsRequestContentType | Return either gene-ids, or entire gene metadata (optional)
    table_fields = ['[\"gene-id\",\"gene-type\",\"description\"]'] # List[str] | Specify which fields to include in the tabular report (optional)
    table_format = 'table_format_example' # str | Optional pre-defined template for processing a tabular data request (optional)
    include_tabular_header = ncbi.datasets.openapi.V2IncludeTabularHeader() # V2IncludeTabularHeader | Whether this request for tabular data should include the header row (optional)
    page_size = 20 # int | The maximum number of gene reports to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, `page_token` can be used to retrieve the remaining results. (optional) (default to 20)
    page_token = 'page_token_example' # str | A page token is returned from an `AssemblyDatasetReportsRequest` call with more than `page_size` results. Use this token, along with the previous `AssemblyDatasetReportsRequest` parameters, to retrieve the next page of results. When `page_token` is empty, all results have been retrieved. (optional)
    query = 'A2M immunoglobulin' # str | text search within gene symbol, aliases, name, locus-tag and protein name (optional)
    types = [ncbi.datasets.openapi.V2GeneType()] # List[V2GeneType] | Gene types to filter (optional)

    try:
        # Get dataset reports by accession IDs
        api_response = api_instance.gene_dataset_report_by_accession(accessions, returned_content=returned_content, table_fields=table_fields, table_format=table_format, include_tabular_header=include_tabular_header, page_size=page_size, page_token=page_token, query=query, types=types)
        print("The response of GeneApi->gene_dataset_report_by_accession:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeneApi->gene_dataset_report_by_accession: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accessions** | [**List[str]**](str.md)| RNA or Protein accessions. | 
 **returned_content** | [**V2GeneDatasetReportsRequestContentType**](.md)| Return either gene-ids, or entire gene metadata | [optional] 
 **table_fields** | [**List[str]**](str.md)| Specify which fields to include in the tabular report | [optional] 
 **table_format** | **str**| Optional pre-defined template for processing a tabular data request | [optional] 
 **include_tabular_header** | [**V2IncludeTabularHeader**](.md)| Whether this request for tabular data should include the header row | [optional] 
 **page_size** | **int**| The maximum number of gene reports to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, &#x60;page_token&#x60; can be used to retrieve the remaining results. | [optional] [default to 20]
 **page_token** | **str**| A page token is returned from an &#x60;AssemblyDatasetReportsRequest&#x60; call with more than &#x60;page_size&#x60; results. Use this token, along with the previous &#x60;AssemblyDatasetReportsRequest&#x60; parameters, to retrieve the next page of results. When &#x60;page_token&#x60; is empty, all results have been retrieved. | [optional] 
 **query** | **str**| text search within gene symbol, aliases, name, locus-tag and protein name | [optional] 
 **types** | [**List[V2GeneType]**](V2GeneType.md)| Gene types to filter | [optional] 

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
> V2reportsGeneDataReportPage gene_dataset_report_by_tax_and_symbol(symbols, taxon, returned_content=returned_content, table_fields=table_fields, table_format=table_format, include_tabular_header=include_tabular_header, page_size=page_size, page_token=page_token, query=query, types=types)

Get dataset reports by taxons.

Get dataset reports by taxons.  By default, in paged JSON format, but also available as tabular (accept: text/tab-separated-values) or json-lines (accept: application/x-ndjson)

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
    symbols = ['[\"GNAS\"]'] # List[str] | Gene symbol
    taxon = '9606' # str | Taxon for provided gene symbol
    returned_content = ncbi.datasets.openapi.V2GeneDatasetReportsRequestContentType() # V2GeneDatasetReportsRequestContentType | Return either gene-ids, or entire gene metadata (optional)
    table_fields = ['[\"gene-id\",\"gene-type\",\"description\"]'] # List[str] | Specify which fields to include in the tabular report (optional)
    table_format = 'table_format_example' # str | Optional pre-defined template for processing a tabular data request (optional)
    include_tabular_header = ncbi.datasets.openapi.V2IncludeTabularHeader() # V2IncludeTabularHeader | Whether this request for tabular data should include the header row (optional)
    page_size = 20 # int | The maximum number of gene reports to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, `page_token` can be used to retrieve the remaining results. (optional) (default to 20)
    page_token = 'page_token_example' # str | A page token is returned from an `AssemblyDatasetReportsRequest` call with more than `page_size` results. Use this token, along with the previous `AssemblyDatasetReportsRequest` parameters, to retrieve the next page of results. When `page_token` is empty, all results have been retrieved. (optional)
    query = 'A2M immunoglobulin' # str | text search within gene symbol, aliases, name, locus-tag and protein name (optional)
    types = [ncbi.datasets.openapi.V2GeneType()] # List[V2GeneType] | Gene types to filter (optional)

    try:
        # Get dataset reports by taxons.
        api_response = api_instance.gene_dataset_report_by_tax_and_symbol(symbols, taxon, returned_content=returned_content, table_fields=table_fields, table_format=table_format, include_tabular_header=include_tabular_header, page_size=page_size, page_token=page_token, query=query, types=types)
        print("The response of GeneApi->gene_dataset_report_by_tax_and_symbol:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeneApi->gene_dataset_report_by_tax_and_symbol: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbols** | [**List[str]**](str.md)| Gene symbol | 
 **taxon** | **str**| Taxon for provided gene symbol | 
 **returned_content** | [**V2GeneDatasetReportsRequestContentType**](.md)| Return either gene-ids, or entire gene metadata | [optional] 
 **table_fields** | [**List[str]**](str.md)| Specify which fields to include in the tabular report | [optional] 
 **table_format** | **str**| Optional pre-defined template for processing a tabular data request | [optional] 
 **include_tabular_header** | [**V2IncludeTabularHeader**](.md)| Whether this request for tabular data should include the header row | [optional] 
 **page_size** | **int**| The maximum number of gene reports to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, &#x60;page_token&#x60; can be used to retrieve the remaining results. | [optional] [default to 20]
 **page_token** | **str**| A page token is returned from an &#x60;AssemblyDatasetReportsRequest&#x60; call with more than &#x60;page_size&#x60; results. Use this token, along with the previous &#x60;AssemblyDatasetReportsRequest&#x60; parameters, to retrieve the next page of results. When &#x60;page_token&#x60; is empty, all results have been retrieved. | [optional] 
 **query** | **str**| text search within gene symbol, aliases, name, locus-tag and protein name | [optional] 
 **types** | [**List[V2GeneType]**](V2GeneType.md)| Gene types to filter | [optional] 

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
> V2reportsGeneDataReportPage gene_dataset_reports_by_id(gene_ids, returned_content=returned_content, table_fields=table_fields, table_format=table_format, include_tabular_header=include_tabular_header, page_size=page_size, page_token=page_token, query=query, types=types)

Get dataset reports by gene IDs.

Get dataset reports by gene IDs.  By default, in paged JSON format, but also available as tabular (accept: text/tab-separated-values) or json-lines (accept: application/x-ndjson)

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
    gene_ids = [[59067]] # List[int] | NCBI gene ids
    returned_content = ncbi.datasets.openapi.V2GeneDatasetReportsRequestContentType() # V2GeneDatasetReportsRequestContentType | Return either gene-ids, or entire gene metadata (optional)
    table_fields = ['[\"gene-id\",\"gene-type\",\"description\"]'] # List[str] | Specify which fields to include in the tabular report (optional)
    table_format = 'table_format_example' # str | Optional pre-defined template for processing a tabular data request (optional)
    include_tabular_header = ncbi.datasets.openapi.V2IncludeTabularHeader() # V2IncludeTabularHeader | Whether this request for tabular data should include the header row (optional)
    page_size = 20 # int | The maximum number of gene reports to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, `page_token` can be used to retrieve the remaining results. (optional) (default to 20)
    page_token = 'page_token_example' # str | A page token is returned from an `AssemblyDatasetReportsRequest` call with more than `page_size` results. Use this token, along with the previous `AssemblyDatasetReportsRequest` parameters, to retrieve the next page of results. When `page_token` is empty, all results have been retrieved. (optional)
    query = 'A2M immunoglobulin' # str | text search within gene symbol, aliases, name, locus-tag and protein name (optional)
    types = [ncbi.datasets.openapi.V2GeneType()] # List[V2GeneType] | Gene types to filter (optional)

    try:
        # Get dataset reports by gene IDs.
        api_response = api_instance.gene_dataset_reports_by_id(gene_ids, returned_content=returned_content, table_fields=table_fields, table_format=table_format, include_tabular_header=include_tabular_header, page_size=page_size, page_token=page_token, query=query, types=types)
        print("The response of GeneApi->gene_dataset_reports_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeneApi->gene_dataset_reports_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gene_ids** | [**List[int]**](int.md)| NCBI gene ids | 
 **returned_content** | [**V2GeneDatasetReportsRequestContentType**](.md)| Return either gene-ids, or entire gene metadata | [optional] 
 **table_fields** | [**List[str]**](str.md)| Specify which fields to include in the tabular report | [optional] 
 **table_format** | **str**| Optional pre-defined template for processing a tabular data request | [optional] 
 **include_tabular_header** | [**V2IncludeTabularHeader**](.md)| Whether this request for tabular data should include the header row | [optional] 
 **page_size** | **int**| The maximum number of gene reports to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, &#x60;page_token&#x60; can be used to retrieve the remaining results. | [optional] [default to 20]
 **page_token** | **str**| A page token is returned from an &#x60;AssemblyDatasetReportsRequest&#x60; call with more than &#x60;page_size&#x60; results. Use this token, along with the previous &#x60;AssemblyDatasetReportsRequest&#x60; parameters, to retrieve the next page of results. When &#x60;page_token&#x60; is empty, all results have been retrieved. | [optional] 
 **query** | **str**| text search within gene symbol, aliases, name, locus-tag and protein name | [optional] 
 **types** | [**List[V2GeneType]**](V2GeneType.md)| Gene types to filter | [optional] 

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
> V2reportsGeneDataReportPage gene_dataset_reports_by_locus_tag(locus_tags, returned_content=returned_content, table_fields=table_fields, table_format=table_format, include_tabular_header=include_tabular_header, page_size=page_size, page_token=page_token, query=query, types=types)

Get gene dataset reports by locus tag

Get a gene summary for one or more gene locus tags. By default, in paged JSON format, but also available as tabular (accept: text/tab-separated-values) or json-lines (accept: application/x-ndjson)

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
    locus_tags = ['[\"b0001\"]'] # List[str] | Gene locus tags
    returned_content = ncbi.datasets.openapi.V2GeneDatasetReportsRequestContentType() # V2GeneDatasetReportsRequestContentType | Return either gene-ids, or entire gene metadata (optional)
    table_fields = ['[\"gene-id\",\"gene-type\",\"description\"]'] # List[str] | Specify which fields to include in the tabular report (optional)
    table_format = 'table_format_example' # str | Optional pre-defined template for processing a tabular data request (optional)
    include_tabular_header = ncbi.datasets.openapi.V2IncludeTabularHeader() # V2IncludeTabularHeader | Whether this request for tabular data should include the header row (optional)
    page_size = 20 # int | The maximum number of gene reports to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, `page_token` can be used to retrieve the remaining results. (optional) (default to 20)
    page_token = 'page_token_example' # str | A page token is returned from an `AssemblyDatasetReportsRequest` call with more than `page_size` results. Use this token, along with the previous `AssemblyDatasetReportsRequest` parameters, to retrieve the next page of results. When `page_token` is empty, all results have been retrieved. (optional)
    query = 'A2M immunoglobulin' # str | text search within gene symbol, aliases, name, locus-tag and protein name (optional)
    types = [ncbi.datasets.openapi.V2GeneType()] # List[V2GeneType] | Gene types to filter (optional)

    try:
        # Get gene dataset reports by locus tag
        api_response = api_instance.gene_dataset_reports_by_locus_tag(locus_tags, returned_content=returned_content, table_fields=table_fields, table_format=table_format, include_tabular_header=include_tabular_header, page_size=page_size, page_token=page_token, query=query, types=types)
        print("The response of GeneApi->gene_dataset_reports_by_locus_tag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeneApi->gene_dataset_reports_by_locus_tag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **locus_tags** | [**List[str]**](str.md)| Gene locus tags | 
 **returned_content** | [**V2GeneDatasetReportsRequestContentType**](.md)| Return either gene-ids, or entire gene metadata | [optional] 
 **table_fields** | [**List[str]**](str.md)| Specify which fields to include in the tabular report | [optional] 
 **table_format** | **str**| Optional pre-defined template for processing a tabular data request | [optional] 
 **include_tabular_header** | [**V2IncludeTabularHeader**](.md)| Whether this request for tabular data should include the header row | [optional] 
 **page_size** | **int**| The maximum number of gene reports to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, &#x60;page_token&#x60; can be used to retrieve the remaining results. | [optional] [default to 20]
 **page_token** | **str**| A page token is returned from an &#x60;AssemblyDatasetReportsRequest&#x60; call with more than &#x60;page_size&#x60; results. Use this token, along with the previous &#x60;AssemblyDatasetReportsRequest&#x60; parameters, to retrieve the next page of results. When &#x60;page_token&#x60; is empty, all results have been retrieved. | [optional] 
 **query** | **str**| text search within gene symbol, aliases, name, locus-tag and protein name | [optional] 
 **types** | [**List[V2GeneType]**](V2GeneType.md)| Gene types to filter | [optional] 

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
> V2reportsGeneDataReportPage gene_dataset_reports_by_taxon(taxon, returned_content=returned_content, table_fields=table_fields, table_format=table_format, include_tabular_header=include_tabular_header, page_size=page_size, page_token=page_token, query=query, types=types)

Get gene dataset reports by taxonomic identifier

Get a gene summary for a specified NCBI Taxonomy ID or name (common or scientific). By default, in paged JSON format, but also available as tabular (accept: text/tab-separated-values) or json-lines (accept: application/x-ndjson)

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
    returned_content = ncbi.datasets.openapi.V2GeneDatasetReportsRequestContentType() # V2GeneDatasetReportsRequestContentType | Return either gene-ids, or entire gene metadata (optional)
    table_fields = ['[\"gene-id\",\"gene-type\",\"description\"]'] # List[str] | Specify which fields to include in the tabular report (optional)
    table_format = 'table_format_example' # str | Optional pre-defined template for processing a tabular data request (optional)
    include_tabular_header = ncbi.datasets.openapi.V2IncludeTabularHeader() # V2IncludeTabularHeader | Whether this request for tabular data should include the header row (optional)
    page_size = 20 # int | The maximum number of gene reports to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, `page_token` can be used to retrieve the remaining results. (optional) (default to 20)
    page_token = 'page_token_example' # str | A page token is returned from an `AssemblyDatasetReportsRequest` call with more than `page_size` results. Use this token, along with the previous `AssemblyDatasetReportsRequest` parameters, to retrieve the next page of results. When `page_token` is empty, all results have been retrieved. (optional)
    query = 'A2M immunoglobulin' # str | text search within gene symbol, aliases, name, locus-tag and protein name (optional)
    types = [ncbi.datasets.openapi.V2GeneType()] # List[V2GeneType] | Gene types to filter (optional)

    try:
        # Get gene dataset reports by taxonomic identifier
        api_response = api_instance.gene_dataset_reports_by_taxon(taxon, returned_content=returned_content, table_fields=table_fields, table_format=table_format, include_tabular_header=include_tabular_header, page_size=page_size, page_token=page_token, query=query, types=types)
        print("The response of GeneApi->gene_dataset_reports_by_taxon:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeneApi->gene_dataset_reports_by_taxon: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **taxon** | **str**| NCBI Taxonomy ID or name (common or scientific) that the genes are annotated at | 
 **returned_content** | [**V2GeneDatasetReportsRequestContentType**](.md)| Return either gene-ids, or entire gene metadata | [optional] 
 **table_fields** | [**List[str]**](str.md)| Specify which fields to include in the tabular report | [optional] 
 **table_format** | **str**| Optional pre-defined template for processing a tabular data request | [optional] 
 **include_tabular_header** | [**V2IncludeTabularHeader**](.md)| Whether this request for tabular data should include the header row | [optional] 
 **page_size** | **int**| The maximum number of gene reports to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, &#x60;page_token&#x60; can be used to retrieve the remaining results. | [optional] [default to 20]
 **page_token** | **str**| A page token is returned from an &#x60;AssemblyDatasetReportsRequest&#x60; call with more than &#x60;page_size&#x60; results. Use this token, along with the previous &#x60;AssemblyDatasetReportsRequest&#x60; parameters, to retrieve the next page of results. When &#x60;page_token&#x60; is empty, all results have been retrieved. | [optional] 
 **query** | **str**| text search within gene symbol, aliases, name, locus-tag and protein name | [optional] 
 **types** | [**List[V2GeneType]**](V2GeneType.md)| Gene types to filter | [optional] 

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
> V2DownloadSummary gene_download_summary_by_id(gene_ids, include_annotation_type=include_annotation_type, returned_content=returned_content, fasta_filter=fasta_filter, accession_filter=accession_filter, aux_report=aux_report, tabular_reports=tabular_reports, table_fields=table_fields, table_report_type=table_report_type)

Get gene download summary by GeneID

Get a download summary by GeneID in a JSON output format.

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
    gene_ids = [[59067]] # List[int] | NCBI gene ids
    include_annotation_type = [ncbi.datasets.openapi.V2Fasta()] # List[V2Fasta] | Select additional types of annotation to include in the data package.  If unset, no annotation is provided. (optional)
    returned_content = ncbi.datasets.openapi.V2GeneDatasetRequestContentType() # V2GeneDatasetRequestContentType | Return either gene-ids, or entire gene metadata (optional)
    fasta_filter = ['fasta_filter_example'] # List[str] | Limit the FASTA sequences in the datasets package to these transcript and protein accessions (deprecated) (optional)
    accession_filter = ['[\"NM_001408458.1\",\"NM_001407959.1\"]'] # List[str] | Limit the FASTA sequences and tabular product report in the datasets package to these transcript and protein accessions (optional)
    aux_report = [ncbi.datasets.openapi.V2GeneDatasetRequestGeneDatasetReportType()] # List[V2GeneDatasetRequestGeneDatasetReportType] | list additional reports to include with download. Data report is included by default. (optional)
    tabular_reports = [ncbi.datasets.openapi.V2GeneDatasetRequestGeneDatasetReportType()] # List[V2GeneDatasetRequestGeneDatasetReportType] |  (optional)
    table_fields = ['table_fields_example'] # List[str] | Specify which fields to include in the tabular report. This is currently deprecated - use tabular_reports instead. (optional)
    table_report_type = ncbi.datasets.openapi.V2GeneDatasetRequestGeneDatasetReportType() # V2GeneDatasetRequestGeneDatasetReportType | Specify the report from which the table fields will be taken. This is currently deprecated - use tabular_reports instead. (optional)

    try:
        # Get gene download summary by GeneID
        api_response = api_instance.gene_download_summary_by_id(gene_ids, include_annotation_type=include_annotation_type, returned_content=returned_content, fasta_filter=fasta_filter, accession_filter=accession_filter, aux_report=aux_report, tabular_reports=tabular_reports, table_fields=table_fields, table_report_type=table_report_type)
        print("The response of GeneApi->gene_download_summary_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeneApi->gene_download_summary_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gene_ids** | [**List[int]**](int.md)| NCBI gene ids | 
 **include_annotation_type** | [**List[V2Fasta]**](V2Fasta.md)| Select additional types of annotation to include in the data package.  If unset, no annotation is provided. | [optional] 
 **returned_content** | [**V2GeneDatasetRequestContentType**](.md)| Return either gene-ids, or entire gene metadata | [optional] 
 **fasta_filter** | [**List[str]**](str.md)| Limit the FASTA sequences in the datasets package to these transcript and protein accessions (deprecated) | [optional] 
 **accession_filter** | [**List[str]**](str.md)| Limit the FASTA sequences and tabular product report in the datasets package to these transcript and protein accessions | [optional] 
 **aux_report** | [**List[V2GeneDatasetRequestGeneDatasetReportType]**](V2GeneDatasetRequestGeneDatasetReportType.md)| list additional reports to include with download. Data report is included by default. | [optional] 
 **tabular_reports** | [**List[V2GeneDatasetRequestGeneDatasetReportType]**](V2GeneDatasetRequestGeneDatasetReportType.md)|  | [optional] 
 **table_fields** | [**List[str]**](str.md)| Specify which fields to include in the tabular report. This is currently deprecated - use tabular_reports instead. | [optional] 
 **table_report_type** | [**V2GeneDatasetRequestGeneDatasetReportType**](.md)| Specify the report from which the table fields will be taken. This is currently deprecated - use tabular_reports instead. | [optional] 

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

Get gene download summary

Get gene download summary in a JSON output format.

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
    v2_gene_dataset_request = {"gene_ids":[59067,50615]} # V2GeneDatasetRequest | 

    try:
        # Get gene download summary
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

Get gene links by gene ID

Get links to available gene resources by gene ID.

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
    gene_ids = [[59067]] # List[int] | NCBI gene ids, limited to 1000 ids

    try:
        # Get gene links by gene ID
        api_response = api_instance.gene_links_by_id(gene_ids)
        print("The response of GeneApi->gene_links_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeneApi->gene_links_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gene_ids** | [**List[int]**](int.md)| NCBI gene ids, limited to 1000 ids | 

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

Get gene links by gene ID

Get links to available gene resources by gene ID.

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
        # Get gene links by gene ID
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
> V2reportsGeneDataReportPage gene_metadata_by_accession(accessions, returned_content=returned_content, locus_tags=locus_tags, table_fields=table_fields, include_tabular_header=include_tabular_header, page_size=page_size, page_token=page_token, accession_filter=accession_filter)

Get gene metadata by RefSeq Accession

Get a gene summary by RefSeq Accession. By default, in paged JSON format, but also available as tabular (accept: text/tab-separated-values) or json-lines (accept: application/x-ndjson)

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_gene_dataset_reports_request_content_type import V2GeneDatasetReportsRequestContentType
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
    accessions = ['[\"NM_021803.4\"]'] # List[str] | RNA or Protein accessions.
    returned_content = ncbi.datasets.openapi.V2GeneDatasetReportsRequestContentType() # V2GeneDatasetReportsRequestContentType | Return either gene-ids, or entire gene metadata (optional)
    locus_tags = ['[\"b0001\"]'] # List[str] | Gene locus tags (optional)
    table_fields = ['[\"gene-id\",\"gene-type\",\"description\"]'] # List[str] | Specify which fields to include in the tabular report (optional)
    include_tabular_header = ncbi.datasets.openapi.V2IncludeTabularHeader() # V2IncludeTabularHeader | Whether this request for tabular data should include the header row (optional)
    page_size = 20 # int | The maximum number of gene reports to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, `page_token` can be used to retrieve the remaining results. (optional) (default to 20)
    page_token = 'page_token_example' # str | A page token is returned from an `AssemblyDatasetReportsRequest` call with more than `page_size` results. Use this token, along with the previous `AssemblyDatasetReportsRequest` parameters, to retrieve the next page of results. When `page_token` is empty, all results have been retrieved. (optional)
    accession_filter = ['[\"NM_001408458.1\",\"NM_001407959.1\"]'] # List[str] | Filter tabular product report to only include the selected accessions (optional)

    try:
        # Get gene metadata by RefSeq Accession
        api_response = api_instance.gene_metadata_by_accession(accessions, returned_content=returned_content, locus_tags=locus_tags, table_fields=table_fields, include_tabular_header=include_tabular_header, page_size=page_size, page_token=page_token, accession_filter=accession_filter)
        print("The response of GeneApi->gene_metadata_by_accession:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeneApi->gene_metadata_by_accession: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accessions** | [**List[str]**](str.md)| RNA or Protein accessions. | 
 **returned_content** | [**V2GeneDatasetReportsRequestContentType**](.md)| Return either gene-ids, or entire gene metadata | [optional] 
 **locus_tags** | [**List[str]**](str.md)| Gene locus tags | [optional] 
 **table_fields** | [**List[str]**](str.md)| Specify which fields to include in the tabular report | [optional] 
 **include_tabular_header** | [**V2IncludeTabularHeader**](.md)| Whether this request for tabular data should include the header row | [optional] 
 **page_size** | **int**| The maximum number of gene reports to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, &#x60;page_token&#x60; can be used to retrieve the remaining results. | [optional] [default to 20]
 **page_token** | **str**| A page token is returned from an &#x60;AssemblyDatasetReportsRequest&#x60; call with more than &#x60;page_size&#x60; results. Use this token, along with the previous &#x60;AssemblyDatasetReportsRequest&#x60; parameters, to retrieve the next page of results. When &#x60;page_token&#x60; is empty, all results have been retrieved. | [optional] 
 **accession_filter** | [**List[str]**](str.md)| Filter tabular product report to only include the selected accessions | [optional] 

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

Get gene metadata as JSON

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
        # Get gene metadata as JSON
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
> V2reportsGeneDataReportPage gene_metadata_by_tax_and_symbol(symbols, taxon, returned_content=returned_content, locus_tags=locus_tags, table_fields=table_fields, include_tabular_header=include_tabular_header, page_size=page_size, page_token=page_token, accession_filter=accession_filter)

Get gene metadata by gene symbol

Get a gene summary by by gene symbol. By default, in paged JSON format, but also available as tabular (accept: text/tab-separated-values) or json-lines (accept: application/x-ndjson)

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_gene_dataset_reports_request_content_type import V2GeneDatasetReportsRequestContentType
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
    symbols = ['[\"GNAS\"]'] # List[str] | Gene symbol
    taxon = '9606' # str | Taxon for provided gene symbol
    returned_content = ncbi.datasets.openapi.V2GeneDatasetReportsRequestContentType() # V2GeneDatasetReportsRequestContentType | Return either gene-ids, or entire gene metadata (optional)
    locus_tags = ['[\"b0001\"]'] # List[str] | Gene locus tags (optional)
    table_fields = ['[\"gene-id\",\"gene-type\",\"description\"]'] # List[str] | Specify which fields to include in the tabular report (optional)
    include_tabular_header = ncbi.datasets.openapi.V2IncludeTabularHeader() # V2IncludeTabularHeader | Whether this request for tabular data should include the header row (optional)
    page_size = 20 # int | The maximum number of gene reports to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, `page_token` can be used to retrieve the remaining results. (optional) (default to 20)
    page_token = 'page_token_example' # str | A page token is returned from an `AssemblyDatasetReportsRequest` call with more than `page_size` results. Use this token, along with the previous `AssemblyDatasetReportsRequest` parameters, to retrieve the next page of results. When `page_token` is empty, all results have been retrieved. (optional)
    accession_filter = ['[\"NM_001408458.1\",\"NM_001407959.1\"]'] # List[str] | Filter tabular product report to only include the selected accessions (optional)

    try:
        # Get gene metadata by gene symbol
        api_response = api_instance.gene_metadata_by_tax_and_symbol(symbols, taxon, returned_content=returned_content, locus_tags=locus_tags, table_fields=table_fields, include_tabular_header=include_tabular_header, page_size=page_size, page_token=page_token, accession_filter=accession_filter)
        print("The response of GeneApi->gene_metadata_by_tax_and_symbol:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeneApi->gene_metadata_by_tax_and_symbol: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbols** | [**List[str]**](str.md)| Gene symbol | 
 **taxon** | **str**| Taxon for provided gene symbol | 
 **returned_content** | [**V2GeneDatasetReportsRequestContentType**](.md)| Return either gene-ids, or entire gene metadata | [optional] 
 **locus_tags** | [**List[str]**](str.md)| Gene locus tags | [optional] 
 **table_fields** | [**List[str]**](str.md)| Specify which fields to include in the tabular report | [optional] 
 **include_tabular_header** | [**V2IncludeTabularHeader**](.md)| Whether this request for tabular data should include the header row | [optional] 
 **page_size** | **int**| The maximum number of gene reports to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, &#x60;page_token&#x60; can be used to retrieve the remaining results. | [optional] [default to 20]
 **page_token** | **str**| A page token is returned from an &#x60;AssemblyDatasetReportsRequest&#x60; call with more than &#x60;page_size&#x60; results. Use this token, along with the previous &#x60;AssemblyDatasetReportsRequest&#x60; parameters, to retrieve the next page of results. When &#x60;page_token&#x60; is empty, all results have been retrieved. | [optional] 
 **accession_filter** | [**List[str]**](str.md)| Filter tabular product report to only include the selected accessions | [optional] 

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

Get gene orthologs by gene ID

Get a gene summary for an ortholog set by gene ID in a JSON output format.

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
    gene_id = 2778 # int | 
    returned_content = ncbi.datasets.openapi.V2OrthologRequestContentType() # V2OrthologRequestContentType | Return either gene-ids, or entire gene metadata (optional)
    taxon_filter = ['[\"9606\",\"10090\"]'] # List[str] | Filter genes by taxa (optional)
    page_size = 20 # int | The maximum number of gene reports to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, `page_token` can be used to retrieve the remaining results. (optional) (default to 20)
    page_token = 'page_token_example' # str | A page token is returned from an `OrthologRequest` call with more than `page_size` results. Use this token, along with the previous `OrthologRequest` parameters, to retrieve the next page of results. When `page_token` is empty, all results have been retrieved. (optional)

    try:
        # Get gene orthologs by gene ID
        api_response = api_instance.gene_orthologs_by_id(gene_id, returned_content=returned_content, taxon_filter=taxon_filter, page_size=page_size, page_token=page_token)
        print("The response of GeneApi->gene_orthologs_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeneApi->gene_orthologs_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gene_id** | **int**|  | 
 **returned_content** | [**V2OrthologRequestContentType**](.md)| Return either gene-ids, or entire gene metadata | [optional] 
 **taxon_filter** | [**List[str]**](str.md)| Filter genes by taxa | [optional] 
 **page_size** | **int**| The maximum number of gene reports to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, &#x60;page_token&#x60; can be used to retrieve the remaining results. | [optional] [default to 20]
 **page_token** | **str**| A page token is returned from an &#x60;OrthologRequest&#x60; call with more than &#x60;page_size&#x60; results. Use this token, along with the previous &#x60;OrthologRequest&#x60; parameters, to retrieve the next page of results. When &#x60;page_token&#x60; is empty, all results have been retrieved. | [optional] 

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

Get gene orthologs by gene ID

Get a gene summary for an ortholog set by gene ID in a JSON output format by POST

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
    v2_ortholog_request = {"gene_id":2778} # V2OrthologRequest | 

    try:
        # Get gene orthologs by gene ID
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

Get gene product reports as JSON

Get gene product reports. By default, in paged JSON format, but also available as tabular (accept: text/tab-separated-values) or json-lines (accept: application/x-ndjson)

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
        # Get gene product reports as JSON
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
> V2reportsGeneDataReportPage gene_product_report_by_accession(accessions, table_fields=table_fields, table_format=table_format, include_tabular_header=include_tabular_header, page_size=page_size, page_token=page_token, query=query, types=types, accession_filter=accession_filter)

Get gene product reports by accession IDs

Get gene product reports by accession IDs.  By default, in paged JSON format, but also available as tabular (accept: text/tab-separated-values) or json-lines (accept: application/x-ndjson)

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
    accessions = ['[\"NM_021803.4\"]'] # List[str] | RNA or Protein accessions.
    table_fields = ['[\"gene-id\",\"gene-type\",\"description\"]'] # List[str] | Specify which fields to include in the tabular report (optional)
    table_format = 'table_format_example' # str | Optional pre-defined template for processing a tabular data request (optional)
    include_tabular_header = ncbi.datasets.openapi.V2IncludeTabularHeader() # V2IncludeTabularHeader | Whether this request for tabular data should include the header row (optional)
    page_size = 20 # int | The maximum number of gene reports to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, `page_token` can be used to retrieve the remaining results. (optional) (default to 20)
    page_token = 'page_token_example' # str | A page token is returned from an `AssemblyDatasetReportsRequest` call with more than `page_size` results. Use this token, along with the previous `AssemblyDatasetReportsRequest` parameters, to retrieve the next page of results. When `page_token` is empty, all results have been retrieved. (optional)
    query = 'A2M immunoglobulin' # str | text search within gene symbol, aliases, name, locus-tag and protein name (optional)
    types = [ncbi.datasets.openapi.V2GeneType()] # List[V2GeneType] | Gene types to filter (optional)
    accession_filter = ['[\"NM_001408458.1\",\"NM_001407959.1\"]'] # List[str] | Filter tabular product report to only include the selected accessions (optional)

    try:
        # Get gene product reports by accession IDs
        api_response = api_instance.gene_product_report_by_accession(accessions, table_fields=table_fields, table_format=table_format, include_tabular_header=include_tabular_header, page_size=page_size, page_token=page_token, query=query, types=types, accession_filter=accession_filter)
        print("The response of GeneApi->gene_product_report_by_accession:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeneApi->gene_product_report_by_accession: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accessions** | [**List[str]**](str.md)| RNA or Protein accessions. | 
 **table_fields** | [**List[str]**](str.md)| Specify which fields to include in the tabular report | [optional] 
 **table_format** | **str**| Optional pre-defined template for processing a tabular data request | [optional] 
 **include_tabular_header** | [**V2IncludeTabularHeader**](.md)| Whether this request for tabular data should include the header row | [optional] 
 **page_size** | **int**| The maximum number of gene reports to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, &#x60;page_token&#x60; can be used to retrieve the remaining results. | [optional] [default to 20]
 **page_token** | **str**| A page token is returned from an &#x60;AssemblyDatasetReportsRequest&#x60; call with more than &#x60;page_size&#x60; results. Use this token, along with the previous &#x60;AssemblyDatasetReportsRequest&#x60; parameters, to retrieve the next page of results. When &#x60;page_token&#x60; is empty, all results have been retrieved. | [optional] 
 **query** | **str**| text search within gene symbol, aliases, name, locus-tag and protein name | [optional] 
 **types** | [**List[V2GeneType]**](V2GeneType.md)| Gene types to filter | [optional] 
 **accession_filter** | [**List[str]**](str.md)| Filter tabular product report to only include the selected accessions | [optional] 

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
> V2reportsGeneDataReportPage gene_product_report_by_tax_and_symbol(symbols, taxon, table_fields=table_fields, table_format=table_format, include_tabular_header=include_tabular_header, page_size=page_size, page_token=page_token, query=query, types=types, accession_filter=accession_filter)

Get product reports by taxon.

Get gene product reports by taxon.  By default, in paged JSON format, but also available as tabular (accept: text/tab-separated-values) or json-lines (accept: application/x-ndjson)

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
    symbols = ['[\"GNAS\"]'] # List[str] | Gene symbol
    taxon = '9606' # str | Taxon for provided gene symbol
    table_fields = ['[\"gene-id\",\"gene-type\",\"description\"]'] # List[str] | Specify which fields to include in the tabular report (optional)
    table_format = 'table_format_example' # str | Optional pre-defined template for processing a tabular data request (optional)
    include_tabular_header = ncbi.datasets.openapi.V2IncludeTabularHeader() # V2IncludeTabularHeader | Whether this request for tabular data should include the header row (optional)
    page_size = 20 # int | The maximum number of gene reports to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, `page_token` can be used to retrieve the remaining results. (optional) (default to 20)
    page_token = 'page_token_example' # str | A page token is returned from an `AssemblyDatasetReportsRequest` call with more than `page_size` results. Use this token, along with the previous `AssemblyDatasetReportsRequest` parameters, to retrieve the next page of results. When `page_token` is empty, all results have been retrieved. (optional)
    query = 'A2M immunoglobulin' # str | text search within gene symbol, aliases, name, locus-tag and protein name (optional)
    types = [ncbi.datasets.openapi.V2GeneType()] # List[V2GeneType] | Gene types to filter (optional)
    accession_filter = ['[\"NM_001408458.1\",\"NM_001407959.1\"]'] # List[str] | Filter tabular product report to only include the selected accessions (optional)

    try:
        # Get product reports by taxon.
        api_response = api_instance.gene_product_report_by_tax_and_symbol(symbols, taxon, table_fields=table_fields, table_format=table_format, include_tabular_header=include_tabular_header, page_size=page_size, page_token=page_token, query=query, types=types, accession_filter=accession_filter)
        print("The response of GeneApi->gene_product_report_by_tax_and_symbol:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeneApi->gene_product_report_by_tax_and_symbol: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbols** | [**List[str]**](str.md)| Gene symbol | 
 **taxon** | **str**| Taxon for provided gene symbol | 
 **table_fields** | [**List[str]**](str.md)| Specify which fields to include in the tabular report | [optional] 
 **table_format** | **str**| Optional pre-defined template for processing a tabular data request | [optional] 
 **include_tabular_header** | [**V2IncludeTabularHeader**](.md)| Whether this request for tabular data should include the header row | [optional] 
 **page_size** | **int**| The maximum number of gene reports to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, &#x60;page_token&#x60; can be used to retrieve the remaining results. | [optional] [default to 20]
 **page_token** | **str**| A page token is returned from an &#x60;AssemblyDatasetReportsRequest&#x60; call with more than &#x60;page_size&#x60; results. Use this token, along with the previous &#x60;AssemblyDatasetReportsRequest&#x60; parameters, to retrieve the next page of results. When &#x60;page_token&#x60; is empty, all results have been retrieved. | [optional] 
 **query** | **str**| text search within gene symbol, aliases, name, locus-tag and protein name | [optional] 
 **types** | [**List[V2GeneType]**](V2GeneType.md)| Gene types to filter | [optional] 
 **accession_filter** | [**List[str]**](str.md)| Filter tabular product report to only include the selected accessions | [optional] 

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
> V2reportsGeneDataReportPage gene_product_reports_by_id(gene_ids, table_fields=table_fields, table_format=table_format, include_tabular_header=include_tabular_header, page_size=page_size, page_token=page_token, query=query, types=types, accession_filter=accession_filter)

Get gene product reports by gene IDs.

Get gene product reports by gene IDs.  By default, in paged JSON format, but also available as tabular (accept: text/tab-separated-values) or json-lines (accept: application/x-ndjson)

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
    gene_ids = [[59067]] # List[int] | NCBI gene ids
    table_fields = ['[\"gene-id\",\"gene-type\",\"description\"]'] # List[str] | Specify which fields to include in the tabular report (optional)
    table_format = 'table_format_example' # str | Optional pre-defined template for processing a tabular data request (optional)
    include_tabular_header = ncbi.datasets.openapi.V2IncludeTabularHeader() # V2IncludeTabularHeader | Whether this request for tabular data should include the header row (optional)
    page_size = 20 # int | The maximum number of gene reports to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, `page_token` can be used to retrieve the remaining results. (optional) (default to 20)
    page_token = 'page_token_example' # str | A page token is returned from an `AssemblyDatasetReportsRequest` call with more than `page_size` results. Use this token, along with the previous `AssemblyDatasetReportsRequest` parameters, to retrieve the next page of results. When `page_token` is empty, all results have been retrieved. (optional)
    query = 'A2M immunoglobulin' # str | text search within gene symbol, aliases, name, locus-tag and protein name (optional)
    types = [ncbi.datasets.openapi.V2GeneType()] # List[V2GeneType] | Gene types to filter (optional)
    accession_filter = ['[\"NM_001408458.1\",\"NM_001407959.1\"]'] # List[str] | Filter tabular product report to only include the selected accessions (optional)

    try:
        # Get gene product reports by gene IDs.
        api_response = api_instance.gene_product_reports_by_id(gene_ids, table_fields=table_fields, table_format=table_format, include_tabular_header=include_tabular_header, page_size=page_size, page_token=page_token, query=query, types=types, accession_filter=accession_filter)
        print("The response of GeneApi->gene_product_reports_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeneApi->gene_product_reports_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gene_ids** | [**List[int]**](int.md)| NCBI gene ids | 
 **table_fields** | [**List[str]**](str.md)| Specify which fields to include in the tabular report | [optional] 
 **table_format** | **str**| Optional pre-defined template for processing a tabular data request | [optional] 
 **include_tabular_header** | [**V2IncludeTabularHeader**](.md)| Whether this request for tabular data should include the header row | [optional] 
 **page_size** | **int**| The maximum number of gene reports to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, &#x60;page_token&#x60; can be used to retrieve the remaining results. | [optional] [default to 20]
 **page_token** | **str**| A page token is returned from an &#x60;AssemblyDatasetReportsRequest&#x60; call with more than &#x60;page_size&#x60; results. Use this token, along with the previous &#x60;AssemblyDatasetReportsRequest&#x60; parameters, to retrieve the next page of results. When &#x60;page_token&#x60; is empty, all results have been retrieved. | [optional] 
 **query** | **str**| text search within gene symbol, aliases, name, locus-tag and protein name | [optional] 
 **types** | [**List[V2GeneType]**](V2GeneType.md)| Gene types to filter | [optional] 
 **accession_filter** | [**List[str]**](str.md)| Filter tabular product report to only include the selected accessions | [optional] 

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
> V2reportsGeneDataReportPage gene_product_reports_by_locus_tags(locus_tags, table_fields=table_fields, table_format=table_format, include_tabular_header=include_tabular_header, page_size=page_size, page_token=page_token, query=query, types=types, accession_filter=accession_filter)

Get gene product reports by locus tags

Get gene product reports for one or more gene locus tags. By default, in paged JSON format, but also available as tabular (accept: text/tab-separated-values) or json-lines (accept: application/x-ndjson)

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
    locus_tags = ['[\"b0001\"]'] # List[str] | Gene locus tags
    table_fields = ['[\"gene-id\",\"gene-type\",\"description\"]'] # List[str] | Specify which fields to include in the tabular report (optional)
    table_format = 'table_format_example' # str | Optional pre-defined template for processing a tabular data request (optional)
    include_tabular_header = ncbi.datasets.openapi.V2IncludeTabularHeader() # V2IncludeTabularHeader | Whether this request for tabular data should include the header row (optional)
    page_size = 20 # int | The maximum number of gene reports to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, `page_token` can be used to retrieve the remaining results. (optional) (default to 20)
    page_token = 'page_token_example' # str | A page token is returned from an `AssemblyDatasetReportsRequest` call with more than `page_size` results. Use this token, along with the previous `AssemblyDatasetReportsRequest` parameters, to retrieve the next page of results. When `page_token` is empty, all results have been retrieved. (optional)
    query = 'A2M immunoglobulin' # str | text search within gene symbol, aliases, name, locus-tag and protein name (optional)
    types = [ncbi.datasets.openapi.V2GeneType()] # List[V2GeneType] | Gene types to filter (optional)
    accession_filter = ['[\"NM_001408458.1\",\"NM_001407959.1\"]'] # List[str] | Filter tabular product report to only include the selected accessions (optional)

    try:
        # Get gene product reports by locus tags
        api_response = api_instance.gene_product_reports_by_locus_tags(locus_tags, table_fields=table_fields, table_format=table_format, include_tabular_header=include_tabular_header, page_size=page_size, page_token=page_token, query=query, types=types, accession_filter=accession_filter)
        print("The response of GeneApi->gene_product_reports_by_locus_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeneApi->gene_product_reports_by_locus_tags: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **locus_tags** | [**List[str]**](str.md)| Gene locus tags | 
 **table_fields** | [**List[str]**](str.md)| Specify which fields to include in the tabular report | [optional] 
 **table_format** | **str**| Optional pre-defined template for processing a tabular data request | [optional] 
 **include_tabular_header** | [**V2IncludeTabularHeader**](.md)| Whether this request for tabular data should include the header row | [optional] 
 **page_size** | **int**| The maximum number of gene reports to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, &#x60;page_token&#x60; can be used to retrieve the remaining results. | [optional] [default to 20]
 **page_token** | **str**| A page token is returned from an &#x60;AssemblyDatasetReportsRequest&#x60; call with more than &#x60;page_size&#x60; results. Use this token, along with the previous &#x60;AssemblyDatasetReportsRequest&#x60; parameters, to retrieve the next page of results. When &#x60;page_token&#x60; is empty, all results have been retrieved. | [optional] 
 **query** | **str**| text search within gene symbol, aliases, name, locus-tag and protein name | [optional] 
 **types** | [**List[V2GeneType]**](V2GeneType.md)| Gene types to filter | [optional] 
 **accession_filter** | [**List[str]**](str.md)| Filter tabular product report to only include the selected accessions | [optional] 

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
> V2reportsGeneDataReportPage gene_product_reports_by_taxon(taxon, table_fields=table_fields, table_format=table_format, include_tabular_header=include_tabular_header, page_size=page_size, page_token=page_token, query=query, types=types, accession_filter=accession_filter)

Get gene product reports by taxonomic identifier

Get gene product reports for a specified NCBI Taxonomy ID or name (common or scientific). By default, in paged JSON format, but also available as tabular (accept: text/tab-separated-values) or json-lines (accept: application/x-ndjson)

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
    table_fields = ['[\"gene-id\",\"gene-type\",\"description\"]'] # List[str] | Specify which fields to include in the tabular report (optional)
    table_format = 'table_format_example' # str | Optional pre-defined template for processing a tabular data request (optional)
    include_tabular_header = ncbi.datasets.openapi.V2IncludeTabularHeader() # V2IncludeTabularHeader | Whether this request for tabular data should include the header row (optional)
    page_size = 20 # int | The maximum number of gene reports to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, `page_token` can be used to retrieve the remaining results. (optional) (default to 20)
    page_token = 'page_token_example' # str | A page token is returned from an `AssemblyDatasetReportsRequest` call with more than `page_size` results. Use this token, along with the previous `AssemblyDatasetReportsRequest` parameters, to retrieve the next page of results. When `page_token` is empty, all results have been retrieved. (optional)
    query = 'A2M immunoglobulin' # str | text search within gene symbol, aliases, name, locus-tag and protein name (optional)
    types = [ncbi.datasets.openapi.V2GeneType()] # List[V2GeneType] | Gene types to filter (optional)
    accession_filter = ['[\"NM_001408458.1\",\"NM_001407959.1\"]'] # List[str] | Filter tabular product report to only include the selected accessions (optional)

    try:
        # Get gene product reports by taxonomic identifier
        api_response = api_instance.gene_product_reports_by_taxon(taxon, table_fields=table_fields, table_format=table_format, include_tabular_header=include_tabular_header, page_size=page_size, page_token=page_token, query=query, types=types, accession_filter=accession_filter)
        print("The response of GeneApi->gene_product_reports_by_taxon:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeneApi->gene_product_reports_by_taxon: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **taxon** | **str**| NCBI Taxonomy ID or name (common or scientific) that the genes are annotated at | 
 **table_fields** | [**List[str]**](str.md)| Specify which fields to include in the tabular report | [optional] 
 **table_format** | **str**| Optional pre-defined template for processing a tabular data request | [optional] 
 **include_tabular_header** | [**V2IncludeTabularHeader**](.md)| Whether this request for tabular data should include the header row | [optional] 
 **page_size** | **int**| The maximum number of gene reports to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, &#x60;page_token&#x60; can be used to retrieve the remaining results. | [optional] [default to 20]
 **page_token** | **str**| A page token is returned from an &#x60;AssemblyDatasetReportsRequest&#x60; call with more than &#x60;page_size&#x60; results. Use this token, along with the previous &#x60;AssemblyDatasetReportsRequest&#x60; parameters, to retrieve the next page of results. When &#x60;page_token&#x60; is empty, all results have been retrieved. | [optional] 
 **query** | **str**| text search within gene symbol, aliases, name, locus-tag and protein name | [optional] 
 **types** | [**List[V2GeneType]**](V2GeneType.md)| Gene types to filter | [optional] 
 **accession_filter** | [**List[str]**](str.md)| Filter tabular product report to only include the selected accessions | [optional] 

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
> V2reportsGeneDataReportPage gene_reports_by_id(gene_ids, returned_content=returned_content, locus_tags=locus_tags, table_fields=table_fields, include_tabular_header=include_tabular_header, page_size=page_size, page_token=page_token, accession_filter=accession_filter)

Get gene reports by GeneID

Get a gene summary by GeneID. By default, in paged JSON format, but also available as tabular (accept: text/tab-separated-values) or json-lines (accept: application/x-ndjson)

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_gene_dataset_reports_request_content_type import V2GeneDatasetReportsRequestContentType
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
    gene_ids = [[59067]] # List[int] | NCBI gene ids
    returned_content = ncbi.datasets.openapi.V2GeneDatasetReportsRequestContentType() # V2GeneDatasetReportsRequestContentType | Return either gene-ids, or entire gene metadata (optional)
    locus_tags = ['[\"b0001\"]'] # List[str] | Gene locus tags (optional)
    table_fields = ['[\"gene-id\",\"gene-type\",\"description\"]'] # List[str] | Specify which fields to include in the tabular report (optional)
    include_tabular_header = ncbi.datasets.openapi.V2IncludeTabularHeader() # V2IncludeTabularHeader | Whether this request for tabular data should include the header row (optional)
    page_size = 20 # int | The maximum number of gene reports to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, `page_token` can be used to retrieve the remaining results. (optional) (default to 20)
    page_token = 'page_token_example' # str | A page token is returned from an `AssemblyDatasetReportsRequest` call with more than `page_size` results. Use this token, along with the previous `AssemblyDatasetReportsRequest` parameters, to retrieve the next page of results. When `page_token` is empty, all results have been retrieved. (optional)
    accession_filter = ['[\"NM_001408458.1\",\"NM_001407959.1\"]'] # List[str] | Filter tabular product report to only include the selected accessions (optional)

    try:
        # Get gene reports by GeneID
        api_response = api_instance.gene_reports_by_id(gene_ids, returned_content=returned_content, locus_tags=locus_tags, table_fields=table_fields, include_tabular_header=include_tabular_header, page_size=page_size, page_token=page_token, accession_filter=accession_filter)
        print("The response of GeneApi->gene_reports_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeneApi->gene_reports_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gene_ids** | [**List[int]**](int.md)| NCBI gene ids | 
 **returned_content** | [**V2GeneDatasetReportsRequestContentType**](.md)| Return either gene-ids, or entire gene metadata | [optional] 
 **locus_tags** | [**List[str]**](str.md)| Gene locus tags | [optional] 
 **table_fields** | [**List[str]**](str.md)| Specify which fields to include in the tabular report | [optional] 
 **include_tabular_header** | [**V2IncludeTabularHeader**](.md)| Whether this request for tabular data should include the header row | [optional] 
 **page_size** | **int**| The maximum number of gene reports to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, &#x60;page_token&#x60; can be used to retrieve the remaining results. | [optional] [default to 20]
 **page_token** | **str**| A page token is returned from an &#x60;AssemblyDatasetReportsRequest&#x60; call with more than &#x60;page_size&#x60; results. Use this token, along with the previous &#x60;AssemblyDatasetReportsRequest&#x60; parameters, to retrieve the next page of results. When &#x60;page_token&#x60; is empty, all results have been retrieved. | [optional] 
 **accession_filter** | [**List[str]**](str.md)| Filter tabular product report to only include the selected accessions | [optional] 

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
> V2reportsGeneDataReportPage gene_reports_by_taxon(taxon, returned_content=returned_content, locus_tags=locus_tags, table_fields=table_fields, include_tabular_header=include_tabular_header, page_size=page_size, page_token=page_token, query=query, types=types, accession_filter=accession_filter)

Get gene reports by taxonomic identifier

Get a gene summary for a specified NCBI Taxonomy ID or name (common or scientific). By default, in paged JSON format, but also available as tabular (accept: text/tab-separated-values) or json-lines (accept: application/x-ndjson)

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
    returned_content = ncbi.datasets.openapi.V2GeneDatasetReportsRequestContentType() # V2GeneDatasetReportsRequestContentType | Return either gene-ids, or entire gene metadata (optional)
    locus_tags = ['[\"b0001\"]'] # List[str] | Gene locus tags (optional)
    table_fields = ['[\"gene-id\",\"gene-type\",\"description\"]'] # List[str] | Specify which fields to include in the tabular report (optional)
    include_tabular_header = ncbi.datasets.openapi.V2IncludeTabularHeader() # V2IncludeTabularHeader | Whether this request for tabular data should include the header row (optional)
    page_size = 20 # int | The maximum number of gene reports to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, `page_token` can be used to retrieve the remaining results. (optional) (default to 20)
    page_token = 'page_token_example' # str | A page token is returned from an `AssemblyDatasetReportsRequest` call with more than `page_size` results. Use this token, along with the previous `AssemblyDatasetReportsRequest` parameters, to retrieve the next page of results. When `page_token` is empty, all results have been retrieved. (optional)
    query = 'A2M immunoglobulin' # str | text search within gene symbol, aliases, name, locus-tag and protein name (optional)
    types = [ncbi.datasets.openapi.V2GeneType()] # List[V2GeneType] | Gene types to filter (optional)
    accession_filter = ['[\"NM_001408458.1\",\"NM_001407959.1\"]'] # List[str] | Filter tabular product report to only include the selected accessions (optional)

    try:
        # Get gene reports by taxonomic identifier
        api_response = api_instance.gene_reports_by_taxon(taxon, returned_content=returned_content, locus_tags=locus_tags, table_fields=table_fields, include_tabular_header=include_tabular_header, page_size=page_size, page_token=page_token, query=query, types=types, accession_filter=accession_filter)
        print("The response of GeneApi->gene_reports_by_taxon:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeneApi->gene_reports_by_taxon: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **taxon** | **str**| NCBI Taxonomy ID or name (common or scientific) that the genes are annotated at | 
 **returned_content** | [**V2GeneDatasetReportsRequestContentType**](.md)| Return either gene-ids, or entire gene metadata | [optional] 
 **locus_tags** | [**List[str]**](str.md)| Gene locus tags | [optional] 
 **table_fields** | [**List[str]**](str.md)| Specify which fields to include in the tabular report | [optional] 
 **include_tabular_header** | [**V2IncludeTabularHeader**](.md)| Whether this request for tabular data should include the header row | [optional] 
 **page_size** | **int**| The maximum number of gene reports to return. Default is 20 and maximum is 1000. If the number of results exceeds the page size, &#x60;page_token&#x60; can be used to retrieve the remaining results. | [optional] [default to 20]
 **page_token** | **str**| A page token is returned from an &#x60;AssemblyDatasetReportsRequest&#x60; call with more than &#x60;page_size&#x60; results. Use this token, along with the previous &#x60;AssemblyDatasetReportsRequest&#x60; parameters, to retrieve the next page of results. When &#x60;page_token&#x60; is empty, all results have been retrieved. | [optional] 
 **query** | **str**| text search within gene symbol, aliases, name, locus-tag and protein name | [optional] 
 **types** | [**List[V2GeneType]**](V2GeneType.md)| Gene types to filter | [optional] 
 **accession_filter** | [**List[str]**](str.md)| Filter tabular product report to only include the selected accessions | [optional] 

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

