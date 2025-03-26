# V2reportsBioProjectLineage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bioprojects** | [**List[V2reportsBioProject]**](V2reportsBioProject.md) |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_bio_project_lineage import V2reportsBioProjectLineage

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsBioProjectLineage from a JSON string
v2reports_bio_project_lineage_instance = V2reportsBioProjectLineage.from_json(json)
# print the JSON string representation of the object
print(V2reportsBioProjectLineage.to_json())

# convert the object into a dict
v2reports_bio_project_lineage_dict = v2reports_bio_project_lineage_instance.to_dict()
# create an instance of V2reportsBioProjectLineage from a dict
v2reports_bio_project_lineage_from_dict = V2reportsBioProjectLineage.from_dict(v2reports_bio_project_lineage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


