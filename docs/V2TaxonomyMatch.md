# V2TaxonomyMatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**warnings** | [**List[V2reportsWarning]**](V2reportsWarning.md) |  | [optional] 
**errors** | [**List[V2reportsError]**](V2reportsError.md) |  | [optional] 
**query** | **List[str]** |  | [optional] 
**taxonomy** | [**V2TaxonomyNode**](V2TaxonomyNode.md) |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2_taxonomy_match import V2TaxonomyMatch

# TODO update the JSON string below
json = "{}"
# create an instance of V2TaxonomyMatch from a JSON string
v2_taxonomy_match_instance = V2TaxonomyMatch.from_json(json)
# print the JSON string representation of the object
print(V2TaxonomyMatch.to_json())

# convert the object into a dict
v2_taxonomy_match_dict = v2_taxonomy_match_instance.to_dict()
# create an instance of V2TaxonomyMatch from a dict
v2_taxonomy_match_from_dict = V2TaxonomyMatch.from_dict(v2_taxonomy_match_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


