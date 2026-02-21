# Ncbiprotddv2PubmedAbstractRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pmid** | **int** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.ncbiprotddv2_pubmed_abstract_request import Ncbiprotddv2PubmedAbstractRequest

# TODO update the JSON string below
json = "{}"
# create an instance of Ncbiprotddv2PubmedAbstractRequest from a JSON string
ncbiprotddv2_pubmed_abstract_request_instance = Ncbiprotddv2PubmedAbstractRequest.from_json(json)
# print the JSON string representation of the object
print(Ncbiprotddv2PubmedAbstractRequest.to_json())

# convert the object into a dict
ncbiprotddv2_pubmed_abstract_request_dict = ncbiprotddv2_pubmed_abstract_request_instance.to_dict()
# create an instance of Ncbiprotddv2PubmedAbstractRequest from a dict
ncbiprotddv2_pubmed_abstract_request_from_dict = Ncbiprotddv2PubmedAbstractRequest.from_dict(ncbiprotddv2_pubmed_abstract_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


