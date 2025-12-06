# V2BioSampleDatasetReportsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessions** | **List[str]** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2_bio_sample_dataset_reports_request import V2BioSampleDatasetReportsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2BioSampleDatasetReportsRequest from a JSON string
v2_bio_sample_dataset_reports_request_instance = V2BioSampleDatasetReportsRequest.from_json(json)
# print the JSON string representation of the object
print(V2BioSampleDatasetReportsRequest.to_json())

# convert the object into a dict
v2_bio_sample_dataset_reports_request_dict = v2_bio_sample_dataset_reports_request_instance.to_dict()
# create an instance of V2BioSampleDatasetReportsRequest from a dict
v2_bio_sample_dataset_reports_request_from_dict = V2BioSampleDatasetReportsRequest.from_dict(v2_bio_sample_dataset_reports_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


