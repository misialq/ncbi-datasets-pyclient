# V2reportsBioSampleDescriptor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accession** | **str** |  | [optional] 
**last_updated** | **str** |  | [optional] 
**publication_date** | **str** |  | [optional] 
**submission_date** | **str** |  | [optional] 
**sample_ids** | [**List[V2reportsBioSampleId]**](V2reportsBioSampleId.md) |  | [optional] 
**description** | [**V2reportsBioSampleDescription**](V2reportsBioSampleDescription.md) |  | [optional] 
**owner** | [**V2reportsBioSampleOwner**](V2reportsBioSampleOwner.md) |  | [optional] 
**models** | **List[str]** |  | [optional] 
**bioprojects** | [**List[V2reportsBioProject]**](V2reportsBioProject.md) |  | [optional] 
**package** | **str** |  | [optional] 
**attributes** | [**List[V2reportsBioSampleAttribute]**](V2reportsBioSampleAttribute.md) |  | [optional] 
**status** | [**V2reportsBioSampleStatus**](V2reportsBioSampleStatus.md) |  | [optional] 
**age** | **str** |  | [optional] 
**biomaterial_provider** | **str** |  | [optional] 
**breed** | **str** |  | [optional] 
**collected_by** | **str** |  | [optional] 
**collection_date** | **str** |  | [optional] 
**cultivar** | **str** |  | [optional] 
**dev_stage** | **str** |  | [optional] 
**ecotype** | **str** |  | [optional] 
**geo_loc_name** | **str** |  | [optional] 
**host** | **str** |  | [optional] 
**host_disease** | **str** |  | [optional] 
**identified_by** | **str** |  | [optional] 
**ifsac_category** | **str** |  | [optional] 
**isolate** | **str** |  | [optional] 
**isolate_name_alias** | **str** |  | [optional] 
**isolation_source** | **str** |  | [optional] 
**lat_lon** | **str** |  | [optional] 
**project_name** | **str** |  | [optional] 
**sample_name** | **str** |  | [optional] 
**serovar** | **str** |  | [optional] 
**sex** | **str** |  | [optional] 
**source_type** | **str** |  | [optional] 
**strain** | **str** |  | [optional] 
**sub_species** | **str** |  | [optional] 
**tissue** | **str** |  | [optional] 
**serotype** | **str** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_bio_sample_descriptor import V2reportsBioSampleDescriptor

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsBioSampleDescriptor from a JSON string
v2reports_bio_sample_descriptor_instance = V2reportsBioSampleDescriptor.from_json(json)
# print the JSON string representation of the object
print(V2reportsBioSampleDescriptor.to_json())

# convert the object into a dict
v2reports_bio_sample_descriptor_dict = v2reports_bio_sample_descriptor_instance.to_dict()
# create an instance of V2reportsBioSampleDescriptor from a dict
v2reports_bio_sample_descriptor_from_dict = V2reportsBioSampleDescriptor.from_dict(v2reports_bio_sample_descriptor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


