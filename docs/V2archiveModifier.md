# V2archiveModifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subtype** | [**V2archiveTaxonomySubtype**](V2archiveTaxonomySubtype.md) |  | [optional] [default to V2archiveTaxonomySubtype.UNKNOWN]
**subname** | **str** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2archive_modifier import V2archiveModifier

# TODO update the JSON string below
json = "{}"
# create an instance of V2archiveModifier from a JSON string
v2archive_modifier_instance = V2archiveModifier.from_json(json)
# print the JSON string representation of the object
print(V2archiveModifier.to_json())

# convert the object into a dict
v2archive_modifier_dict = v2archive_modifier_instance.to_dict()
# create an instance of V2archiveModifier from a dict
v2archive_modifier_from_dict = V2archiveModifier.from_dict(v2archive_modifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


