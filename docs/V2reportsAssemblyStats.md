# V2reportsAssemblyStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_number_of_chromosomes** | **int** |  | [optional] 
**total_sequence_length** | **str** |  | [optional] 
**total_ungapped_length** | **str** |  | [optional] 
**number_of_contigs** | **int** |  | [optional] 
**contig_n50** | **int** |  | [optional] 
**contig_l50** | **int** |  | [optional] 
**number_of_scaffolds** | **int** |  | [optional] 
**scaffold_n50** | **int** |  | [optional] 
**scaffold_l50** | **int** |  | [optional] 
**gaps_between_scaffolds_count** | **int** |  | [optional] 
**number_of_component_sequences** | **int** |  | [optional] 
**atgc_count** | **str** |  | [optional] 
**gc_count** | **str** |  | [optional] 
**gc_percent** | **float** |  | [optional] 
**genome_coverage** | **str** |  | [optional] 
**number_of_organelles** | **int** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_assembly_stats import V2reportsAssemblyStats

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsAssemblyStats from a JSON string
v2reports_assembly_stats_instance = V2reportsAssemblyStats.from_json(json)
# print the JSON string representation of the object
print(V2reportsAssemblyStats.to_json())

# convert the object into a dict
v2reports_assembly_stats_dict = v2reports_assembly_stats_instance.to_dict()
# create an instance of V2reportsAssemblyStats from a dict
v2reports_assembly_stats_from_dict = V2reportsAssemblyStats.from_dict(v2reports_assembly_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


