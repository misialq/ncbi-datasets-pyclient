# V2reportsTaxData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**id** | **int** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_tax_data import V2reportsTaxData

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsTaxData from a JSON string
v2reports_tax_data_instance = V2reportsTaxData.from_json(json)
# print the JSON string representation of the object
print(V2reportsTaxData.to_json())

# convert the object into a dict
v2reports_tax_data_dict = v2reports_tax_data_instance.to_dict()
# create an instance of V2reportsTaxData from a dict
v2reports_tax_data_from_dict = V2reportsTaxData.from_dict(v2reports_tax_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


