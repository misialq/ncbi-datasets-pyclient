# coding: utf-8

# flake8: noqa

"""
    NCBI Datasets API

    ### NCBI Datasets is a resource that lets you easily gather data from NCBI. The Datasets version 2 API is still in alpha, and we're updating it often to add new functionality, iron out bugs and enhance usability. For some larger downloads, you may want to download a [dehydrated zip archive](https://www.ncbi.nlm.nih.gov/datasets/docs/v2/how-tos/genomes/large-download/), and retrieve the individual data files at a later time. 

    The version of the OpenAPI document: v2
    Contact: help@ncbi.nlm.nih.gov
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "v18.4.0"

# import apis into sdk package
from ncbi.datasets.openapi.api.bio_sample_api import BioSampleApi
from ncbi.datasets.openapi.api.gene_api import GeneApi
from ncbi.datasets.openapi.api.genome_api import GenomeApi
from ncbi.datasets.openapi.api.organelle_api import OrganelleApi
from ncbi.datasets.openapi.api.prokaryote_api import ProkaryoteApi
from ncbi.datasets.openapi.api.taxonomy_api import TaxonomyApi
from ncbi.datasets.openapi.api.version_api import VersionApi
from ncbi.datasets.openapi.api.virus_api import VirusApi

# import ApiClient
from ncbi.datasets.openapi.api_response import ApiResponse
from ncbi.datasets.openapi.api_client import ApiClient
from ncbi.datasets.openapi.configuration import Configuration
from ncbi.datasets.openapi.exceptions import OpenApiException
from ncbi.datasets.openapi.exceptions import ApiTypeError
from ncbi.datasets.openapi.exceptions import ApiValueError
from ncbi.datasets.openapi.exceptions import ApiKeyError
from ncbi.datasets.openapi.exceptions import ApiAttributeError
from ncbi.datasets.openapi.exceptions import ApiException

# import models into sdk package
from ncbi.datasets.openapi.models.protobuf_any import ProtobufAny
from ncbi.datasets.openapi.models.rpc_status import RpcStatus
from ncbi.datasets.openapi.models.v2_annotation_for_assembly_type import V2AnnotationForAssemblyType
from ncbi.datasets.openapi.models.v2_annotation_for_organelle_type import V2AnnotationForOrganelleType
from ncbi.datasets.openapi.models.v2_assembly_accessions import V2AssemblyAccessions
from ncbi.datasets.openapi.models.v2_assembly_check_m_histogram_reply import V2AssemblyCheckMHistogramReply
from ncbi.datasets.openapi.models.v2_assembly_check_m_histogram_reply_histogram_interval import V2AssemblyCheckMHistogramReplyHistogramInterval
from ncbi.datasets.openapi.models.v2_assembly_check_m_histogram_request import V2AssemblyCheckMHistogramRequest
from ncbi.datasets.openapi.models.v2_assembly_dataset_availability import V2AssemblyDatasetAvailability
from ncbi.datasets.openapi.models.v2_assembly_dataset_descriptors_filter import V2AssemblyDatasetDescriptorsFilter
from ncbi.datasets.openapi.models.v2_assembly_dataset_descriptors_filter_assembly_source import V2AssemblyDatasetDescriptorsFilterAssemblySource
from ncbi.datasets.openapi.models.v2_assembly_dataset_descriptors_filter_assembly_version import V2AssemblyDatasetDescriptorsFilterAssemblyVersion
from ncbi.datasets.openapi.models.v2_assembly_dataset_descriptors_filter_metagenome_derived_filter import V2AssemblyDatasetDescriptorsFilterMetagenomeDerivedFilter
from ncbi.datasets.openapi.models.v2_assembly_dataset_descriptors_filter_type_material_category import V2AssemblyDatasetDescriptorsFilterTypeMaterialCategory
from ncbi.datasets.openapi.models.v2_assembly_dataset_reports_request import V2AssemblyDatasetReportsRequest
from ncbi.datasets.openapi.models.v2_assembly_dataset_reports_request_content_type import V2AssemblyDatasetReportsRequestContentType
from ncbi.datasets.openapi.models.v2_assembly_dataset_request import V2AssemblyDatasetRequest
from ncbi.datasets.openapi.models.v2_assembly_dataset_request_resolution import V2AssemblyDatasetRequestResolution
from ncbi.datasets.openapi.models.v2_assembly_links_reply import V2AssemblyLinksReply
from ncbi.datasets.openapi.models.v2_assembly_links_reply_assembly_link import V2AssemblyLinksReplyAssemblyLink
from ncbi.datasets.openapi.models.v2_assembly_links_reply_assembly_link_type import V2AssemblyLinksReplyAssemblyLinkType
from ncbi.datasets.openapi.models.v2_assembly_links_request import V2AssemblyLinksRequest
from ncbi.datasets.openapi.models.v2_assembly_revision_history import V2AssemblyRevisionHistory
from ncbi.datasets.openapi.models.v2_assembly_revision_history_request import V2AssemblyRevisionHistoryRequest
from ncbi.datasets.openapi.models.v2_assembly_sequence_reports_request import V2AssemblySequenceReportsRequest
from ncbi.datasets.openapi.models.v2_dataset_request import V2DatasetRequest
from ncbi.datasets.openapi.models.v2_download_summary import V2DownloadSummary
from ncbi.datasets.openapi.models.v2_download_summary_available_files import V2DownloadSummaryAvailableFiles
from ncbi.datasets.openapi.models.v2_download_summary_dehydrated import V2DownloadSummaryDehydrated
from ncbi.datasets.openapi.models.v2_download_summary_file_summary import V2DownloadSummaryFileSummary
from ncbi.datasets.openapi.models.v2_download_summary_hydrated import V2DownloadSummaryHydrated
from ncbi.datasets.openapi.models.v2_fasta import V2Fasta
from ncbi.datasets.openapi.models.v2_gene_chromosome_summary_reply import V2GeneChromosomeSummaryReply
from ncbi.datasets.openapi.models.v2_gene_chromosome_summary_reply_gene_chromosome_summary import V2GeneChromosomeSummaryReplyGeneChromosomeSummary
from ncbi.datasets.openapi.models.v2_gene_counts_by_taxon_reply import V2GeneCountsByTaxonReply
from ncbi.datasets.openapi.models.v2_gene_counts_by_taxon_reply_gene_type_and_count import V2GeneCountsByTaxonReplyGeneTypeAndCount
from ncbi.datasets.openapi.models.v2_gene_counts_by_taxon_request import V2GeneCountsByTaxonRequest
from ncbi.datasets.openapi.models.v2_gene_dataset_reports_request import V2GeneDatasetReportsRequest
from ncbi.datasets.openapi.models.v2_gene_dataset_reports_request_content_type import V2GeneDatasetReportsRequestContentType
from ncbi.datasets.openapi.models.v2_gene_dataset_reports_request_symbols_for_taxon import V2GeneDatasetReportsRequestSymbolsForTaxon
from ncbi.datasets.openapi.models.v2_gene_dataset_request import V2GeneDatasetRequest
from ncbi.datasets.openapi.models.v2_gene_dataset_request_content_type import V2GeneDatasetRequestContentType
from ncbi.datasets.openapi.models.v2_gene_dataset_request_gene_dataset_report_type import V2GeneDatasetRequestGeneDatasetReportType
from ncbi.datasets.openapi.models.v2_gene_links_reply import V2GeneLinksReply
from ncbi.datasets.openapi.models.v2_gene_links_reply_gene_link import V2GeneLinksReplyGeneLink
from ncbi.datasets.openapi.models.v2_gene_links_reply_gene_link_type import V2GeneLinksReplyGeneLinkType
from ncbi.datasets.openapi.models.v2_gene_links_request import V2GeneLinksRequest
from ncbi.datasets.openapi.models.v2_gene_type import V2GeneType
from ncbi.datasets.openapi.models.v2_genome_annotation_request import V2GenomeAnnotationRequest
from ncbi.datasets.openapi.models.v2_genome_annotation_request_annotation_type import V2GenomeAnnotationRequestAnnotationType
from ncbi.datasets.openapi.models.v2_genome_annotation_request_genome_annotation_table_format import V2GenomeAnnotationRequestGenomeAnnotationTableFormat
from ncbi.datasets.openapi.models.v2_genome_annotation_table_summary_reply import V2GenomeAnnotationTableSummaryReply
from ncbi.datasets.openapi.models.v2_http_body import V2HttpBody
from ncbi.datasets.openapi.models.v2_image_size import V2ImageSize
from ncbi.datasets.openapi.models.v2_include_tabular_header import V2IncludeTabularHeader
from ncbi.datasets.openapi.models.v2_organelle_download_request import V2OrganelleDownloadRequest
from ncbi.datasets.openapi.models.v2_organelle_metadata_request import V2OrganelleMetadataRequest
from ncbi.datasets.openapi.models.v2_organelle_metadata_request_content_type import V2OrganelleMetadataRequestContentType
from ncbi.datasets.openapi.models.v2_organelle_metadata_request_organelle_table_format import V2OrganelleMetadataRequestOrganelleTableFormat
from ncbi.datasets.openapi.models.v2_organelle_sort import V2OrganelleSort
from ncbi.datasets.openapi.models.v2_organism_query_request import V2OrganismQueryRequest
from ncbi.datasets.openapi.models.v2_organism_query_request_tax_rank_filter import V2OrganismQueryRequestTaxRankFilter
from ncbi.datasets.openapi.models.v2_organism_query_request_taxon_resource_filter import V2OrganismQueryRequestTaxonResourceFilter
from ncbi.datasets.openapi.models.v2_ortholog_request import V2OrthologRequest
from ncbi.datasets.openapi.models.v2_ortholog_request_content_type import V2OrthologRequestContentType
from ncbi.datasets.openapi.models.v2_prokaryote_gene_request import V2ProkaryoteGeneRequest
from ncbi.datasets.openapi.models.v2_prokaryote_gene_request_gene_flank_config import V2ProkaryoteGeneRequestGeneFlankConfig
from ncbi.datasets.openapi.models.v2_sars2_protein_dataset_request import V2Sars2ProteinDatasetRequest
from ncbi.datasets.openapi.models.v2_sci_name_and_ids import V2SciNameAndIds
from ncbi.datasets.openapi.models.v2_sci_name_and_ids_sci_name_and_id import V2SciNameAndIdsSciNameAndId
from ncbi.datasets.openapi.models.v2_sequence_accession_request import V2SequenceAccessionRequest
from ncbi.datasets.openapi.models.v2_sequence_report_page import V2SequenceReportPage
from ncbi.datasets.openapi.models.v2_sort_direction import V2SortDirection
from ncbi.datasets.openapi.models.v2_sort_field import V2SortField
from ncbi.datasets.openapi.models.v2_table_format import V2TableFormat
from ncbi.datasets.openapi.models.v2_tabular_output import V2TabularOutput
from ncbi.datasets.openapi.models.v2_taxonomy_dataset_request import V2TaxonomyDatasetRequest
from ncbi.datasets.openapi.models.v2_taxonomy_dataset_request_taxonomy_report_type import V2TaxonomyDatasetRequestTaxonomyReportType
from ncbi.datasets.openapi.models.v2_taxonomy_filtered_subtree_request import V2TaxonomyFilteredSubtreeRequest
from ncbi.datasets.openapi.models.v2_taxonomy_filtered_subtree_response import V2TaxonomyFilteredSubtreeResponse
from ncbi.datasets.openapi.models.v2_taxonomy_filtered_subtree_response_edge import V2TaxonomyFilteredSubtreeResponseEdge
from ncbi.datasets.openapi.models.v2_taxonomy_filtered_subtree_response_edge_child_status import V2TaxonomyFilteredSubtreeResponseEdgeChildStatus
from ncbi.datasets.openapi.models.v2_taxonomy_filtered_subtree_response_edges_entry import V2TaxonomyFilteredSubtreeResponseEdgesEntry
from ncbi.datasets.openapi.models.v2_taxonomy_image_metadata_request import V2TaxonomyImageMetadataRequest
from ncbi.datasets.openapi.models.v2_taxonomy_image_metadata_response import V2TaxonomyImageMetadataResponse
from ncbi.datasets.openapi.models.v2_taxonomy_image_request import V2TaxonomyImageRequest
from ncbi.datasets.openapi.models.v2_taxonomy_links_request import V2TaxonomyLinksRequest
from ncbi.datasets.openapi.models.v2_taxonomy_links_response import V2TaxonomyLinksResponse
from ncbi.datasets.openapi.models.v2_taxonomy_links_response_generic_link import V2TaxonomyLinksResponseGenericLink
from ncbi.datasets.openapi.models.v2_taxonomy_match import V2TaxonomyMatch
from ncbi.datasets.openapi.models.v2_taxonomy_metadata_request import V2TaxonomyMetadataRequest
from ncbi.datasets.openapi.models.v2_taxonomy_metadata_request_content_type import V2TaxonomyMetadataRequestContentType
from ncbi.datasets.openapi.models.v2_taxonomy_metadata_request_table_format import V2TaxonomyMetadataRequestTableFormat
from ncbi.datasets.openapi.models.v2_taxonomy_metadata_response import V2TaxonomyMetadataResponse
from ncbi.datasets.openapi.models.v2_taxonomy_node import V2TaxonomyNode
from ncbi.datasets.openapi.models.v2_taxonomy_node_count_by_type import V2TaxonomyNodeCountByType
from ncbi.datasets.openapi.models.v2_taxonomy_related_id_request import V2TaxonomyRelatedIdRequest
from ncbi.datasets.openapi.models.v2_taxonomy_tax_ids_page import V2TaxonomyTaxIdsPage
from ncbi.datasets.openapi.models.v2_version_reply import V2VersionReply
from ncbi.datasets.openapi.models.v2_viral_sequence_type import V2ViralSequenceType
from ncbi.datasets.openapi.models.v2_virus_annotation_filter import V2VirusAnnotationFilter
from ncbi.datasets.openapi.models.v2_virus_annotation_report_request import V2VirusAnnotationReportRequest
from ncbi.datasets.openapi.models.v2_virus_availability import V2VirusAvailability
from ncbi.datasets.openapi.models.v2_virus_availability_request import V2VirusAvailabilityRequest
from ncbi.datasets.openapi.models.v2_virus_data_report_request import V2VirusDataReportRequest
from ncbi.datasets.openapi.models.v2_virus_data_report_request_content_type import V2VirusDataReportRequestContentType
from ncbi.datasets.openapi.models.v2_virus_dataset_filter import V2VirusDatasetFilter
from ncbi.datasets.openapi.models.v2_virus_dataset_report_type import V2VirusDatasetReportType
from ncbi.datasets.openapi.models.v2_virus_dataset_request import V2VirusDatasetRequest
from ncbi.datasets.openapi.models.v2_virus_table_field import V2VirusTableField
from ncbi.datasets.openapi.models.v2reports_ani_match import V2reportsANIMatch
from ncbi.datasets.openapi.models.v2reports_ani_type_category import V2reportsANITypeCategory
from ncbi.datasets.openapi.models.v2reports_additional_submitter import V2reportsAdditionalSubmitter
from ncbi.datasets.openapi.models.v2reports_annotation import V2reportsAnnotation
from ncbi.datasets.openapi.models.v2reports_annotation_info import V2reportsAnnotationInfo
from ncbi.datasets.openapi.models.v2reports_assembly_data_report import V2reportsAssemblyDataReport
from ncbi.datasets.openapi.models.v2reports_assembly_data_report_page import V2reportsAssemblyDataReportPage
from ncbi.datasets.openapi.models.v2reports_assembly_info import V2reportsAssemblyInfo
from ncbi.datasets.openapi.models.v2reports_assembly_level import V2reportsAssemblyLevel
from ncbi.datasets.openapi.models.v2reports_assembly_revision import V2reportsAssemblyRevision
from ncbi.datasets.openapi.models.v2reports_assembly_stats import V2reportsAssemblyStats
from ncbi.datasets.openapi.models.v2reports_assembly_status import V2reportsAssemblyStatus
from ncbi.datasets.openapi.models.v2reports_atypical_info import V2reportsAtypicalInfo
from ncbi.datasets.openapi.models.v2reports_average_nucleotide_identity import V2reportsAverageNucleotideIdentity
from ncbi.datasets.openapi.models.v2reports_average_nucleotide_identity_match_status import V2reportsAverageNucleotideIdentityMatchStatus
from ncbi.datasets.openapi.models.v2reports_average_nucleotide_identity_taxonomy_check_status import V2reportsAverageNucleotideIdentityTaxonomyCheckStatus
from ncbi.datasets.openapi.models.v2reports_bio_project import V2reportsBioProject
from ncbi.datasets.openapi.models.v2reports_bio_project_lineage import V2reportsBioProjectLineage
from ncbi.datasets.openapi.models.v2reports_bio_sample_attribute import V2reportsBioSampleAttribute
from ncbi.datasets.openapi.models.v2reports_bio_sample_contact import V2reportsBioSampleContact
from ncbi.datasets.openapi.models.v2reports_bio_sample_data_report import V2reportsBioSampleDataReport
from ncbi.datasets.openapi.models.v2reports_bio_sample_data_report_page import V2reportsBioSampleDataReportPage
from ncbi.datasets.openapi.models.v2reports_bio_sample_description import V2reportsBioSampleDescription
from ncbi.datasets.openapi.models.v2reports_bio_sample_descriptor import V2reportsBioSampleDescriptor
from ncbi.datasets.openapi.models.v2reports_bio_sample_id import V2reportsBioSampleId
from ncbi.datasets.openapi.models.v2reports_bio_sample_owner import V2reportsBioSampleOwner
from ncbi.datasets.openapi.models.v2reports_bio_sample_status import V2reportsBioSampleStatus
from ncbi.datasets.openapi.models.v2reports_busco_stat import V2reportsBuscoStat
from ncbi.datasets.openapi.models.v2reports_check_m import V2reportsCheckM
from ncbi.datasets.openapi.models.v2reports_classification import V2reportsClassification
from ncbi.datasets.openapi.models.v2reports_collection_type import V2reportsCollectionType
from ncbi.datasets.openapi.models.v2reports_conserved_domain import V2reportsConservedDomain
from ncbi.datasets.openapi.models.v2reports_content_type import V2reportsContentType
from ncbi.datasets.openapi.models.v2reports_count_type import V2reportsCountType
from ncbi.datasets.openapi.models.v2reports_error import V2reportsError
from ncbi.datasets.openapi.models.v2reports_error_assembly_error_code import V2reportsErrorAssemblyErrorCode
from ncbi.datasets.openapi.models.v2reports_error_gene_error_code import V2reportsErrorGeneErrorCode
from ncbi.datasets.openapi.models.v2reports_error_organelle_error_code import V2reportsErrorOrganelleErrorCode
from ncbi.datasets.openapi.models.v2reports_error_taxonomy_error_code import V2reportsErrorTaxonomyErrorCode
from ncbi.datasets.openapi.models.v2reports_error_virus_error_code import V2reportsErrorVirusErrorCode
from ncbi.datasets.openapi.models.v2reports_feature_counts import V2reportsFeatureCounts
from ncbi.datasets.openapi.models.v2reports_gene_counts import V2reportsGeneCounts
from ncbi.datasets.openapi.models.v2reports_gene_data_report_page import V2reportsGeneDataReportPage
from ncbi.datasets.openapi.models.v2reports_gene_descriptor import V2reportsGeneDescriptor
from ncbi.datasets.openapi.models.v2reports_gene_group import V2reportsGeneGroup
from ncbi.datasets.openapi.models.v2reports_gene_ontology import V2reportsGeneOntology
from ncbi.datasets.openapi.models.v2reports_gene_report_match import V2reportsGeneReportMatch
from ncbi.datasets.openapi.models.v2reports_gene_summary import V2reportsGeneSummary
from ncbi.datasets.openapi.models.v2reports_gene_type import V2reportsGeneType
from ncbi.datasets.openapi.models.v2reports_genome_annotation import V2reportsGenomeAnnotation
from ncbi.datasets.openapi.models.v2reports_genome_annotation_report_match import V2reportsGenomeAnnotationReportMatch
from ncbi.datasets.openapi.models.v2reports_genome_annotation_report_page import V2reportsGenomeAnnotationReportPage
from ncbi.datasets.openapi.models.v2reports_genomic_location import V2reportsGenomicLocation
from ncbi.datasets.openapi.models.v2reports_genomic_region import V2reportsGenomicRegion
from ncbi.datasets.openapi.models.v2reports_genomic_region_genomic_region_type import V2reportsGenomicRegionGenomicRegionType
from ncbi.datasets.openapi.models.v2reports_infraspecific_names import V2reportsInfraspecificNames
from ncbi.datasets.openapi.models.v2reports_isolate import V2reportsIsolate
from ncbi.datasets.openapi.models.v2reports_lineage_organism import V2reportsLineageOrganism
from ncbi.datasets.openapi.models.v2reports_linked_assembly import V2reportsLinkedAssembly
from ncbi.datasets.openapi.models.v2reports_linked_assembly_type import V2reportsLinkedAssemblyType
from ncbi.datasets.openapi.models.v2reports_mature_peptide import V2reportsMaturePeptide
from ncbi.datasets.openapi.models.v2reports_message import V2reportsMessage
from ncbi.datasets.openapi.models.v2reports_name_and_authority import V2reportsNameAndAuthority
from ncbi.datasets.openapi.models.v2reports_name_and_authority_note import V2reportsNameAndAuthorityNote
from ncbi.datasets.openapi.models.v2reports_name_and_authority_note_classifier import V2reportsNameAndAuthorityNoteClassifier
from ncbi.datasets.openapi.models.v2reports_name_and_authority_publication import V2reportsNameAndAuthorityPublication
from ncbi.datasets.openapi.models.v2reports_nomenclature_authority import V2reportsNomenclatureAuthority
from ncbi.datasets.openapi.models.v2reports_organelle import V2reportsOrganelle
from ncbi.datasets.openapi.models.v2reports_organelle_biosample import V2reportsOrganelleBiosample
from ncbi.datasets.openapi.models.v2reports_organelle_data_reports import V2reportsOrganelleDataReports
from ncbi.datasets.openapi.models.v2reports_organelle_gene_counts import V2reportsOrganelleGeneCounts
from ncbi.datasets.openapi.models.v2reports_organelle_info import V2reportsOrganelleInfo
from ncbi.datasets.openapi.models.v2reports_organelle_topology import V2reportsOrganelleTopology
from ncbi.datasets.openapi.models.v2reports_organelle_type import V2reportsOrganelleType
from ncbi.datasets.openapi.models.v2reports_organism import V2reportsOrganism
from ncbi.datasets.openapi.models.v2reports_orientation import V2reportsOrientation
from ncbi.datasets.openapi.models.v2reports_paired_assembly import V2reportsPairedAssembly
from ncbi.datasets.openapi.models.v2reports_process_metadata import V2reportsProcessMetadata
from ncbi.datasets.openapi.models.v2reports_product_descriptor import V2reportsProductDescriptor
from ncbi.datasets.openapi.models.v2reports_protein import V2reportsProtein
from ncbi.datasets.openapi.models.v2reports_purpose_of_sampling import V2reportsPurposeOfSampling
from ncbi.datasets.openapi.models.v2reports_range import V2reportsRange
from ncbi.datasets.openapi.models.v2reports_rank_type import V2reportsRankType
from ncbi.datasets.openapi.models.v2reports_reference import V2reportsReference
from ncbi.datasets.openapi.models.v2reports_rna_type import V2reportsRnaType
from ncbi.datasets.openapi.models.v2reports_seq_range_set import V2reportsSeqRangeSet
from ncbi.datasets.openapi.models.v2reports_seq_range_set_fasta import V2reportsSeqRangeSetFasta
from ncbi.datasets.openapi.models.v2reports_sequence_info import V2reportsSequenceInfo
from ncbi.datasets.openapi.models.v2reports_sequence_information import V2reportsSequenceInformation
from ncbi.datasets.openapi.models.v2reports_source_database import V2reportsSourceDatabase
from ncbi.datasets.openapi.models.v2reports_tax_data import V2reportsTaxData
from ncbi.datasets.openapi.models.v2reports_taxonomy_data_report_page import V2reportsTaxonomyDataReportPage
from ncbi.datasets.openapi.models.v2reports_taxonomy_names_data_report_page import V2reportsTaxonomyNamesDataReportPage
from ncbi.datasets.openapi.models.v2reports_taxonomy_names_descriptor import V2reportsTaxonomyNamesDescriptor
from ncbi.datasets.openapi.models.v2reports_taxonomy_names_descriptor_citation import V2reportsTaxonomyNamesDescriptorCitation
from ncbi.datasets.openapi.models.v2reports_taxonomy_names_report_match import V2reportsTaxonomyNamesReportMatch
from ncbi.datasets.openapi.models.v2reports_taxonomy_node import V2reportsTaxonomyNode
from ncbi.datasets.openapi.models.v2reports_taxonomy_node_count_by_type import V2reportsTaxonomyNodeCountByType
from ncbi.datasets.openapi.models.v2reports_taxonomy_report_match import V2reportsTaxonomyReportMatch
from ncbi.datasets.openapi.models.v2reports_taxonomy_type_material import V2reportsTaxonomyTypeMaterial
from ncbi.datasets.openapi.models.v2reports_transcript import V2reportsTranscript
from ncbi.datasets.openapi.models.v2reports_transcript_select_category import V2reportsTranscriptSelectCategory
from ncbi.datasets.openapi.models.v2reports_transcript_transcript_type import V2reportsTranscriptTranscriptType
from ncbi.datasets.openapi.models.v2reports_transcript_type_count import V2reportsTranscriptTypeCount
from ncbi.datasets.openapi.models.v2reports_type_material import V2reportsTypeMaterial
from ncbi.datasets.openapi.models.v2reports_virus_annotation_report import V2reportsVirusAnnotationReport
from ncbi.datasets.openapi.models.v2reports_virus_annotation_report_page import V2reportsVirusAnnotationReportPage
from ncbi.datasets.openapi.models.v2reports_virus_assembly import V2reportsVirusAssembly
from ncbi.datasets.openapi.models.v2reports_virus_assembly_collection_location import V2reportsVirusAssemblyCollectionLocation
from ncbi.datasets.openapi.models.v2reports_virus_assembly_completeness import V2reportsVirusAssemblyCompleteness
from ncbi.datasets.openapi.models.v2reports_virus_assembly_submitter_info import V2reportsVirusAssemblySubmitterInfo
from ncbi.datasets.openapi.models.v2reports_virus_data_report_page import V2reportsVirusDataReportPage
from ncbi.datasets.openapi.models.v2reports_virus_gene import V2reportsVirusGene
from ncbi.datasets.openapi.models.v2reports_virus_peptide import V2reportsVirusPeptide
from ncbi.datasets.openapi.models.v2reports_virus_peptide_uni_prot_id import V2reportsVirusPeptideUniProtId
from ncbi.datasets.openapi.models.v2reports_virus_peptide_viral_peptide_completeness import V2reportsVirusPeptideViralPeptideCompleteness
from ncbi.datasets.openapi.models.v2reports_wgs_info import V2reportsWGSInfo
from ncbi.datasets.openapi.models.v2reports_warning import V2reportsWarning
from ncbi.datasets.openapi.models.v2reports_warning_gene_warning_code import V2reportsWarningGeneWarningCode
from ncbi.datasets.openapi.models.v2reports_warning_replaced_id import V2reportsWarningReplacedId
