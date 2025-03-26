# V2reportsBioProject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accession** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**parent_accession** | **str** |  | [optional] 
**parent_accessions** | **List[str]** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_bio_project import V2reportsBioProject

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsBioProject from a JSON string
v2reports_bio_project_instance = V2reportsBioProject.from_json(json)
# print the JSON string representation of the object
print(V2reportsBioProject.to_json())

# convert the object into a dict
v2reports_bio_project_dict = v2reports_bio_project_instance.to_dict()
# create an instance of V2reportsBioProject from a dict
v2reports_bio_project_from_dict = V2reportsBioProject.from_dict(v2reports_bio_project_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


