# V2reportsBiocollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bio_collection_id** | **str** |  | [optional] 
**code** | **str** |  | [optional] 
**ncbi_unique_code** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**comments** | **str** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_biocollection import V2reportsBiocollection

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsBiocollection from a JSON string
v2reports_biocollection_instance = V2reportsBiocollection.from_json(json)
# print the JSON string representation of the object
print(V2reportsBiocollection.to_json())

# convert the object into a dict
v2reports_biocollection_dict = v2reports_biocollection_instance.to_dict()
# create an instance of V2reportsBiocollection from a dict
v2reports_biocollection_from_dict = V2reportsBiocollection.from_dict(v2reports_biocollection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


