# V2PubmedList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pubmed_ids** | **List[int]** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2_pubmed_list import V2PubmedList

# TODO update the JSON string below
json = "{}"
# create an instance of V2PubmedList from a JSON string
v2_pubmed_list_instance = V2PubmedList.from_json(json)
# print the JSON string representation of the object
print(V2PubmedList.to_json())

# convert the object into a dict
v2_pubmed_list_dict = v2_pubmed_list_instance.to_dict()
# create an instance of V2PubmedList from a dict
v2_pubmed_list_from_dict = V2PubmedList.from_dict(v2_pubmed_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


