# V2AssemblyCheckMHistogramReply


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**species_taxid** | **int** |  | [optional] 
**histogram_intervals** | [**List[V2AssemblyCheckMHistogramReplyHistogramInterval]**](V2AssemblyCheckMHistogramReplyHistogramInterval.md) |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2_assembly_check_m_histogram_reply import V2AssemblyCheckMHistogramReply

# TODO update the JSON string below
json = "{}"
# create an instance of V2AssemblyCheckMHistogramReply from a JSON string
v2_assembly_check_m_histogram_reply_instance = V2AssemblyCheckMHistogramReply.from_json(json)
# print the JSON string representation of the object
print(V2AssemblyCheckMHistogramReply.to_json())

# convert the object into a dict
v2_assembly_check_m_histogram_reply_dict = v2_assembly_check_m_histogram_reply_instance.to_dict()
# create an instance of V2AssemblyCheckMHistogramReply from a dict
v2_assembly_check_m_histogram_reply_from_dict = V2AssemblyCheckMHistogramReply.from_dict(v2_assembly_check_m_histogram_reply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


