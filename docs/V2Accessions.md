# V2Accessions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessions** | **List[str]** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2_accessions import V2Accessions

# TODO update the JSON string below
json = "{}"
# create an instance of V2Accessions from a JSON string
v2_accessions_instance = V2Accessions.from_json(json)
# print the JSON string representation of the object
print(V2Accessions.to_json())

# convert the object into a dict
v2_accessions_dict = v2_accessions_instance.to_dict()
# create an instance of V2Accessions from a dict
v2_accessions_from_dict = V2Accessions.from_dict(v2_accessions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


