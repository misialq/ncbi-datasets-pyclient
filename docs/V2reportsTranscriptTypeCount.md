# V2reportsTranscriptTypeCount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**V2reportsTranscriptTranscriptType**](V2reportsTranscriptTranscriptType.md) |  | [optional] [default to V2reportsTranscriptTranscriptType.UNKNOWN]
**count** | **int** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_transcript_type_count import V2reportsTranscriptTypeCount

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsTranscriptTypeCount from a JSON string
v2reports_transcript_type_count_instance = V2reportsTranscriptTypeCount.from_json(json)
# print the JSON string representation of the object
print(V2reportsTranscriptTypeCount.to_json())

# convert the object into a dict
v2reports_transcript_type_count_dict = v2reports_transcript_type_count_instance.to_dict()
# create an instance of V2reportsTranscriptTypeCount from a dict
v2reports_transcript_type_count_from_dict = V2reportsTranscriptTypeCount.from_dict(v2reports_transcript_type_count_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


