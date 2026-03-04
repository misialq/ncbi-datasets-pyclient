# V2reportsBiocollectionInstitution


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**address** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**comments** | **str** |  | [optional] 
**bio_collections** | [**List[V2reportsBiocollection]**](V2reportsBiocollection.md) |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_biocollection_institution import V2reportsBiocollectionInstitution

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsBiocollectionInstitution from a JSON string
v2reports_biocollection_institution_instance = V2reportsBiocollectionInstitution.from_json(json)
# print the JSON string representation of the object
print(V2reportsBiocollectionInstitution.to_json())

# convert the object into a dict
v2reports_biocollection_institution_dict = v2reports_biocollection_institution_instance.to_dict()
# create an instance of V2reportsBiocollectionInstitution from a dict
v2reports_biocollection_institution_from_dict = V2reportsBiocollectionInstitution.from_dict(v2reports_biocollection_institution_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


