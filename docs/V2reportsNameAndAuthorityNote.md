# V2reportsNameAndAuthorityNote


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**note** | **str** |  | [optional] 
**note_classifier** | [**V2reportsNameAndAuthorityNoteClassifier**](V2reportsNameAndAuthorityNoteClassifier.md) |  | [optional] [default to V2reportsNameAndAuthorityNoteClassifier.NO_AUTHORITY_CLASSIFIER]

## Example

```python
from ncbi.datasets.openapi.models.v2reports_name_and_authority_note import V2reportsNameAndAuthorityNote

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsNameAndAuthorityNote from a JSON string
v2reports_name_and_authority_note_instance = V2reportsNameAndAuthorityNote.from_json(json)
# print the JSON string representation of the object
print(V2reportsNameAndAuthorityNote.to_json())

# convert the object into a dict
v2reports_name_and_authority_note_dict = v2reports_name_and_authority_note_instance.to_dict()
# create an instance of V2reportsNameAndAuthorityNote from a dict
v2reports_name_and_authority_note_from_dict = V2reportsNameAndAuthorityNote.from_dict(v2reports_name_and_authority_note_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


