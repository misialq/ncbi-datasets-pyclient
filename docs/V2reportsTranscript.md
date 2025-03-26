# V2reportsTranscript


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accession_version** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**length** | **int** |  | [optional] 
**cds** | [**V2reportsSeqRangeSet**](V2reportsSeqRangeSet.md) |  | [optional] 
**genomic_locations** | [**List[V2reportsGenomicLocation]**](V2reportsGenomicLocation.md) |  | [optional] 
**ensembl_transcript** | **str** |  | [optional] 
**protein** | [**V2reportsProtein**](V2reportsProtein.md) |  | [optional] 
**type** | [**V2reportsTranscriptTranscriptType**](V2reportsTranscriptTranscriptType.md) |  | [optional] 
**select_category** | [**V2reportsTranscriptSelectCategory**](V2reportsTranscriptSelectCategory.md) |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_transcript import V2reportsTranscript

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsTranscript from a JSON string
v2reports_transcript_instance = V2reportsTranscript.from_json(json)
# print the JSON string representation of the object
print(V2reportsTranscript.to_json())

# convert the object into a dict
v2reports_transcript_dict = v2reports_transcript_instance.to_dict()
# create an instance of V2reportsTranscript from a dict
v2reports_transcript_from_dict = V2reportsTranscript.from_dict(v2reports_transcript_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


