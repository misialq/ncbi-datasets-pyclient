# ncbi.datasets.openapi.ProkaryoteApi

All URIs are relative to *https://api.ncbi.nlm.nih.gov/datasets/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download_prokaryote_gene_package**](ProkaryoteApi.md#download_prokaryote_gene_package) | **GET** /protein/accession/{accessions}/download | Get a prokaryote gene dataset by RefSeq protein accession
[**download_prokaryote_gene_package_post**](ProkaryoteApi.md#download_prokaryote_gene_package_post) | **POST** /protein/accession/download | Get a prokaryote gene dataset by RefSeq protein accession by POST


# **download_prokaryote_gene_package**
> bytearray download_prokaryote_gene_package(accessions, include_annotation_type=include_annotation_type, gene_flank_config_length=gene_flank_config_length, taxon=taxon, filename=filename)

Get a prokaryote gene dataset by RefSeq protein accession

Get a prokaryote gene dataset including gene and protein fasta sequence, annotation and metadata by prokaryote protein accession.

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_fasta import V2Fasta
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
    api_instance = ncbi.datasets.openapi.ProkaryoteApi(api_client)
    accessions = ['[\"WP_015878339.1\"]'] # List[str] | WP prokaryote protein accession
    include_annotation_type = [ncbi.datasets.openapi.V2Fasta()] # List[V2Fasta] | Select additional types of annotation to include in the data package.  If unset, no annotation is provided. (optional)
    gene_flank_config_length = 56 # int |  (optional)
    taxon = 'taxon_example' # str | NCBI Taxonomy ID or name (common or scientific) at any taxonomic rank When specified, return data from this taxon and its subtree (optional)
    filename = 'ncbi_dataset.zip' # str | Output file name. (optional) (default to 'ncbi_dataset.zip')

    try:
        # Get a prokaryote gene dataset by RefSeq protein accession
        api_response = api_instance.download_prokaryote_gene_package(accessions, include_annotation_type=include_annotation_type, gene_flank_config_length=gene_flank_config_length, taxon=taxon, filename=filename)
        print("The response of ProkaryoteApi->download_prokaryote_gene_package:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProkaryoteApi->download_prokaryote_gene_package: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accessions** | [**List[str]**](str.md)| WP prokaryote protein accession | 
 **include_annotation_type** | [**List[V2Fasta]**](V2Fasta.md)| Select additional types of annotation to include in the data package.  If unset, no annotation is provided. | [optional] 
 **gene_flank_config_length** | **int**|  | [optional] 
 **taxon** | **str**| NCBI Taxonomy ID or name (common or scientific) at any taxonomic rank When specified, return data from this taxon and its subtree | [optional] 
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

# **download_prokaryote_gene_package_post**
> bytearray download_prokaryote_gene_package_post(v2_prokaryote_gene_request, filename=filename)

Get a prokaryote gene dataset by RefSeq protein accession by POST

Get a prokaryote gene dataset including gene and protein fasta sequence, annotation and metadata by prokaryote protein accession by POST.

### Example

* Api Key Authentication (ApiKeyAuthHeader):

```python
import ncbi.datasets.openapi
from ncbi.datasets.openapi.models.v2_prokaryote_gene_request import V2ProkaryoteGeneRequest
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
    api_instance = ncbi.datasets.openapi.ProkaryoteApi(api_client)
    v2_prokaryote_gene_request = {"accessions":["WP_000000001.1","WP_000000002.1"]} # V2ProkaryoteGeneRequest | 
    filename = 'ncbi_dataset.zip' # str | Output file name. (optional) (default to 'ncbi_dataset.zip')

    try:
        # Get a prokaryote gene dataset by RefSeq protein accession by POST
        api_response = api_instance.download_prokaryote_gene_package_post(v2_prokaryote_gene_request, filename=filename)
        print("The response of ProkaryoteApi->download_prokaryote_gene_package_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProkaryoteApi->download_prokaryote_gene_package_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v2_prokaryote_gene_request** | [**V2ProkaryoteGeneRequest**](V2ProkaryoteGeneRequest.md)|  | 
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

