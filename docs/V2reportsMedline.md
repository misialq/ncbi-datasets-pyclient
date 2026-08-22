# V2reportsMedline


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pmid** | **int** |  | [optional] 
**medline_uid** | **str** |  | [optional] 
**entry_month** | **str** |  | [optional] 
**article** | [**V2reportsArticle**](V2reportsArticle.md) |  | [optional] 
**status** | [**V2reportsMedlineStatus**](V2reportsMedlineStatus.md) |  | [optional] [default to V2reportsMedlineStatus.UNKNOWN]

## Example

```python
from ncbi.datasets.openapi.models.v2reports_medline import V2reportsMedline

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsMedline from a JSON string
v2reports_medline_instance = V2reportsMedline.from_json(json)
# print the JSON string representation of the object
print(V2reportsMedline.to_json())

# convert the object into a dict
v2reports_medline_dict = v2reports_medline_instance.to_dict()
# create an instance of V2reportsMedline from a dict
v2reports_medline_from_dict = V2reportsMedline.from_dict(v2reports_medline_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


