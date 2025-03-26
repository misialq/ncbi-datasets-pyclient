# V2SciNameAndIdsSciNameAndId


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sci_name** | **str** |  | [optional] 
**tax_id** | **str** |  | [optional] 
**common_name** | **str** |  | [optional] 
**matched_term** | **str** |  | [optional] 
**rank** | [**V2reportsRankType**](V2reportsRankType.md) |  | [optional] 
**group_name** | **str** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2_sci_name_and_ids_sci_name_and_id import V2SciNameAndIdsSciNameAndId

# TODO update the JSON string below
json = "{}"
# create an instance of V2SciNameAndIdsSciNameAndId from a JSON string
v2_sci_name_and_ids_sci_name_and_id_instance = V2SciNameAndIdsSciNameAndId.from_json(json)
# print the JSON string representation of the object
print(V2SciNameAndIdsSciNameAndId.to_json())

# convert the object into a dict
v2_sci_name_and_ids_sci_name_and_id_dict = v2_sci_name_and_ids_sci_name_and_id_instance.to_dict()
# create an instance of V2SciNameAndIdsSciNameAndId from a dict
v2_sci_name_and_ids_sci_name_and_id_from_dict = V2SciNameAndIdsSciNameAndId.from_dict(v2_sci_name_and_ids_sci_name_and_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


