# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models_py3 import AdministrativeCredentials
from ._models_py3 import BareMetalMachine
from ._models_py3 import BareMetalMachineCommandSpecification
from ._models_py3 import BareMetalMachineConfigurationData
from ._models_py3 import BareMetalMachineCordonParameters
from ._models_py3 import BareMetalMachineKeySet
from ._models_py3 import BareMetalMachineKeySetList
from ._models_py3 import BareMetalMachineKeySetPatchParameters
from ._models_py3 import BareMetalMachineList
from ._models_py3 import BareMetalMachinePatchParameters
from ._models_py3 import BareMetalMachinePowerOffParameters
from ._models_py3 import BareMetalMachineReplaceParameters
from ._models_py3 import BareMetalMachineRunCommandParameters
from ._models_py3 import BareMetalMachineRunDataExtractsParameters
from ._models_py3 import BareMetalMachineRunReadCommandsParameters
from ._models_py3 import BareMetalMachineValidateHardwareParameters
from ._models_py3 import BgpPeer
from ._models_py3 import BmcKeySet
from ._models_py3 import BmcKeySetList
from ._models_py3 import BmcKeySetPatchParameters
from ._models_py3 import CloudServicesNetwork
from ._models_py3 import CloudServicesNetworkList
from ._models_py3 import CloudServicesNetworkPatchParameters
from ._models_py3 import Cluster
from ._models_py3 import ClusterAvailableUpgradeVersion
from ._models_py3 import ClusterAvailableVersion
from ._models_py3 import ClusterCapacity
from ._models_py3 import ClusterDeployParameters
from ._models_py3 import ClusterList
from ._models_py3 import ClusterManager
from ._models_py3 import ClusterManagerList
from ._models_py3 import ClusterManagerPatchParameters
from ._models_py3 import ClusterMetricsConfiguration
from ._models_py3 import ClusterMetricsConfigurationList
from ._models_py3 import ClusterMetricsConfigurationPatchParameters
from ._models_py3 import ClusterPatchParameters
from ._models_py3 import ClusterUpdateVersionParameters
from ._models_py3 import CniBgpConfiguration
from ._models_py3 import CommunityAdvertisement
from ._models_py3 import Console
from ._models_py3 import ConsoleList
from ._models_py3 import ConsolePatchParameters
from ._models_py3 import DefaultCniNetwork
from ._models_py3 import DefaultCniNetworkList
from ._models_py3 import DefaultCniNetworkPatchParameters
from ._models_py3 import EgressEndpoint
from ._models_py3 import EndpointDependency
from ._models_py3 import ErrorAdditionalInfo
from ._models_py3 import ErrorDetail
from ._models_py3 import ErrorResponse
from ._models_py3 import ExtendedLocation
from ._models_py3 import HardwareInventory
from ._models_py3 import HardwareInventoryNetworkInterface
from ._models_py3 import HardwareValidationStatus
from ._models_py3 import HybridAksCluster
from ._models_py3 import HybridAksClusterList
from ._models_py3 import HybridAksClusterPatchParameters
from ._models_py3 import HybridAksClusterRestartNodeParameters
from ._models_py3 import ImageRepositoryCredentials
from ._models_py3 import KeySetUser
from ._models_py3 import KeySetUserStatus
from ._models_py3 import L2Network
from ._models_py3 import L2NetworkList
from ._models_py3 import L2NetworkPatchParameters
from ._models_py3 import L3Network
from ._models_py3 import L3NetworkList
from ._models_py3 import L3NetworkPatchParameters
from ._models_py3 import LldpNeighbor
from ._models_py3 import MachineDisk
from ._models_py3 import MachineSkuSlot
from ._models_py3 import ManagedResourceGroupConfiguration
from ._models_py3 import NetworkAttachment
from ._models_py3 import NetworkInterface
from ._models_py3 import Nic
from ._models_py3 import Node
from ._models_py3 import NodeConfiguration
from ._models_py3 import Operation
from ._models_py3 import OperationDisplay
from ._models_py3 import OperationListResult
from ._models_py3 import OsDisk
from ._models_py3 import Rack
from ._models_py3 import RackDefinition
from ._models_py3 import RackList
from ._models_py3 import RackPatchParameters
from ._models_py3 import RackSku
from ._models_py3 import RackSkuList
from ._models_py3 import Resource
from ._models_py3 import ServicePrincipalInformation
from ._models_py3 import SshPublicKey
from ._models_py3 import StorageAppliance
from ._models_py3 import StorageApplianceCommandSpecification
from ._models_py3 import StorageApplianceConfigurationData
from ._models_py3 import StorageApplianceEnableRemoteVendorManagementParameters
from ._models_py3 import StorageApplianceList
from ._models_py3 import StorageAppliancePatchParameters
from ._models_py3 import StorageApplianceRunReadCommandsParameters
from ._models_py3 import StorageApplianceSkuSlot
from ._models_py3 import StorageApplianceValidateHardwareParameters
from ._models_py3 import StorageProfile
from ._models_py3 import SystemData
from ._models_py3 import TagsParameter
from ._models_py3 import TrackedResource
from ._models_py3 import TrunkedNetwork
from ._models_py3 import TrunkedNetworkList
from ._models_py3 import TrunkedNetworkPatchParameters
from ._models_py3 import ValidationThreshold
from ._models_py3 import VirtualMachine
from ._models_py3 import VirtualMachineList
from ._models_py3 import VirtualMachinePatchParameters
from ._models_py3 import VirtualMachinePlacementHint
from ._models_py3 import VirtualMachinePowerOffParameters
from ._models_py3 import VirtualMachineVolumeParameters
from ._models_py3 import Volume
from ._models_py3 import VolumeList
from ._models_py3 import VolumePatchParameters

from ._network_cloud_mgmt_client_enums import ActionType
from ._network_cloud_mgmt_client_enums import BareMetalMachineCordonStatus
from ._network_cloud_mgmt_client_enums import BareMetalMachineDetailedStatus
from ._network_cloud_mgmt_client_enums import BareMetalMachineEvacuate
from ._network_cloud_mgmt_client_enums import BareMetalMachineHardwareValidationCategory
from ._network_cloud_mgmt_client_enums import BareMetalMachineHardwareValidationResult
from ._network_cloud_mgmt_client_enums import BareMetalMachineKeySetDetailedStatus
from ._network_cloud_mgmt_client_enums import BareMetalMachineKeySetPrivilegeLevel
from ._network_cloud_mgmt_client_enums import BareMetalMachineKeySetProvisioningState
from ._network_cloud_mgmt_client_enums import BareMetalMachineKeySetUserSetupStatus
from ._network_cloud_mgmt_client_enums import BareMetalMachinePowerState
from ._network_cloud_mgmt_client_enums import BareMetalMachineProvisioningState
from ._network_cloud_mgmt_client_enums import BareMetalMachineReadyState
from ._network_cloud_mgmt_client_enums import BareMetalMachineSkipShutdown
from ._network_cloud_mgmt_client_enums import BmcKeySetDetailedStatus
from ._network_cloud_mgmt_client_enums import BmcKeySetPrivilegeLevel
from ._network_cloud_mgmt_client_enums import BmcKeySetProvisioningState
from ._network_cloud_mgmt_client_enums import BootstrapProtocol
from ._network_cloud_mgmt_client_enums import CloudServicesNetworkDetailedStatus
from ._network_cloud_mgmt_client_enums import CloudServicesNetworkEnableDefaultEgressEndpoints
from ._network_cloud_mgmt_client_enums import CloudServicesNetworkProvisioningState
from ._network_cloud_mgmt_client_enums import ClusterConnectionStatus
from ._network_cloud_mgmt_client_enums import ClusterDetailedStatus
from ._network_cloud_mgmt_client_enums import ClusterManagerConnectionStatus
from ._network_cloud_mgmt_client_enums import ClusterManagerDetailedStatus
from ._network_cloud_mgmt_client_enums import ClusterManagerProvisioningState
from ._network_cloud_mgmt_client_enums import ClusterMetricsConfigurationDetailedStatus
from ._network_cloud_mgmt_client_enums import ClusterMetricsConfigurationProvisioningState
from ._network_cloud_mgmt_client_enums import ClusterProvisioningState
from ._network_cloud_mgmt_client_enums import ClusterType
from ._network_cloud_mgmt_client_enums import ConsoleDetailedStatus
from ._network_cloud_mgmt_client_enums import ConsoleEnabled
from ._network_cloud_mgmt_client_enums import ConsoleProvisioningState
from ._network_cloud_mgmt_client_enums import ControlImpact
from ._network_cloud_mgmt_client_enums import CreatedByType
from ._network_cloud_mgmt_client_enums import DefaultCniNetworkDetailedStatus
from ._network_cloud_mgmt_client_enums import DefaultCniNetworkProvisioningState
from ._network_cloud_mgmt_client_enums import DefaultGateway
from ._network_cloud_mgmt_client_enums import DeviceConnectionType
from ._network_cloud_mgmt_client_enums import DiskType
from ._network_cloud_mgmt_client_enums import HybridAksClusterDetailedStatus
from ._network_cloud_mgmt_client_enums import HybridAksClusterMachinePowerState
from ._network_cloud_mgmt_client_enums import HybridAksClusterProvisioningState
from ._network_cloud_mgmt_client_enums import HybridAksIpamEnabled
from ._network_cloud_mgmt_client_enums import HybridAksPluginType
from ._network_cloud_mgmt_client_enums import IpAllocationType
from ._network_cloud_mgmt_client_enums import L2NetworkDetailedStatus
from ._network_cloud_mgmt_client_enums import L2NetworkProvisioningState
from ._network_cloud_mgmt_client_enums import L3NetworkDetailedStatus
from ._network_cloud_mgmt_client_enums import L3NetworkProvisioningState
from ._network_cloud_mgmt_client_enums import MachineSkuDiskConnectionType
from ._network_cloud_mgmt_client_enums import Origin
from ._network_cloud_mgmt_client_enums import OsDiskCreateOption
from ._network_cloud_mgmt_client_enums import OsDiskDeleteOption
from ._network_cloud_mgmt_client_enums import RackDetailedStatus
from ._network_cloud_mgmt_client_enums import RackProvisioningState
from ._network_cloud_mgmt_client_enums import RackSkuProvisioningState
from ._network_cloud_mgmt_client_enums import RackSkuType
from ._network_cloud_mgmt_client_enums import RemoteVendorManagementFeature
from ._network_cloud_mgmt_client_enums import RemoteVendorManagementStatus
from ._network_cloud_mgmt_client_enums import SkipShutdown
from ._network_cloud_mgmt_client_enums import StorageApplianceDetailedStatus
from ._network_cloud_mgmt_client_enums import StorageApplianceHardwareValidationCategory
from ._network_cloud_mgmt_client_enums import StorageApplianceProvisioningState
from ._network_cloud_mgmt_client_enums import TrunkedNetworkDetailedStatus
from ._network_cloud_mgmt_client_enums import TrunkedNetworkProvisioningState
from ._network_cloud_mgmt_client_enums import ValidationThresholdGrouping
from ._network_cloud_mgmt_client_enums import ValidationThresholdType
from ._network_cloud_mgmt_client_enums import VirtualMachineBootMethod
from ._network_cloud_mgmt_client_enums import VirtualMachineDetailedStatus
from ._network_cloud_mgmt_client_enums import VirtualMachineDeviceModelType
from ._network_cloud_mgmt_client_enums import VirtualMachineIPAllocationMethod
from ._network_cloud_mgmt_client_enums import VirtualMachineIsolateEmulatorThread
from ._network_cloud_mgmt_client_enums import VirtualMachinePlacementHintPodAffinityScope
from ._network_cloud_mgmt_client_enums import VirtualMachinePlacementHintType
from ._network_cloud_mgmt_client_enums import VirtualMachinePowerState
from ._network_cloud_mgmt_client_enums import VirtualMachineProvisioningState
from ._network_cloud_mgmt_client_enums import VirtualMachineSchedulingExecution
from ._network_cloud_mgmt_client_enums import VirtualMachineVirtioInterfaceType
from ._network_cloud_mgmt_client_enums import VolumeDetailedStatus
from ._network_cloud_mgmt_client_enums import VolumeProvisioningState
from ._network_cloud_mgmt_client_enums import WorkloadImpact
from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "AdministrativeCredentials",
    "BareMetalMachine",
    "BareMetalMachineCommandSpecification",
    "BareMetalMachineConfigurationData",
    "BareMetalMachineCordonParameters",
    "BareMetalMachineKeySet",
    "BareMetalMachineKeySetList",
    "BareMetalMachineKeySetPatchParameters",
    "BareMetalMachineList",
    "BareMetalMachinePatchParameters",
    "BareMetalMachinePowerOffParameters",
    "BareMetalMachineReplaceParameters",
    "BareMetalMachineRunCommandParameters",
    "BareMetalMachineRunDataExtractsParameters",
    "BareMetalMachineRunReadCommandsParameters",
    "BareMetalMachineValidateHardwareParameters",
    "BgpPeer",
    "BmcKeySet",
    "BmcKeySetList",
    "BmcKeySetPatchParameters",
    "CloudServicesNetwork",
    "CloudServicesNetworkList",
    "CloudServicesNetworkPatchParameters",
    "Cluster",
    "ClusterAvailableUpgradeVersion",
    "ClusterAvailableVersion",
    "ClusterCapacity",
    "ClusterDeployParameters",
    "ClusterList",
    "ClusterManager",
    "ClusterManagerList",
    "ClusterManagerPatchParameters",
    "ClusterMetricsConfiguration",
    "ClusterMetricsConfigurationList",
    "ClusterMetricsConfigurationPatchParameters",
    "ClusterPatchParameters",
    "ClusterUpdateVersionParameters",
    "CniBgpConfiguration",
    "CommunityAdvertisement",
    "Console",
    "ConsoleList",
    "ConsolePatchParameters",
    "DefaultCniNetwork",
    "DefaultCniNetworkList",
    "DefaultCniNetworkPatchParameters",
    "EgressEndpoint",
    "EndpointDependency",
    "ErrorAdditionalInfo",
    "ErrorDetail",
    "ErrorResponse",
    "ExtendedLocation",
    "HardwareInventory",
    "HardwareInventoryNetworkInterface",
    "HardwareValidationStatus",
    "HybridAksCluster",
    "HybridAksClusterList",
    "HybridAksClusterPatchParameters",
    "HybridAksClusterRestartNodeParameters",
    "ImageRepositoryCredentials",
    "KeySetUser",
    "KeySetUserStatus",
    "L2Network",
    "L2NetworkList",
    "L2NetworkPatchParameters",
    "L3Network",
    "L3NetworkList",
    "L3NetworkPatchParameters",
    "LldpNeighbor",
    "MachineDisk",
    "MachineSkuSlot",
    "ManagedResourceGroupConfiguration",
    "NetworkAttachment",
    "NetworkInterface",
    "Nic",
    "Node",
    "NodeConfiguration",
    "Operation",
    "OperationDisplay",
    "OperationListResult",
    "OsDisk",
    "Rack",
    "RackDefinition",
    "RackList",
    "RackPatchParameters",
    "RackSku",
    "RackSkuList",
    "Resource",
    "ServicePrincipalInformation",
    "SshPublicKey",
    "StorageAppliance",
    "StorageApplianceCommandSpecification",
    "StorageApplianceConfigurationData",
    "StorageApplianceEnableRemoteVendorManagementParameters",
    "StorageApplianceList",
    "StorageAppliancePatchParameters",
    "StorageApplianceRunReadCommandsParameters",
    "StorageApplianceSkuSlot",
    "StorageApplianceValidateHardwareParameters",
    "StorageProfile",
    "SystemData",
    "TagsParameter",
    "TrackedResource",
    "TrunkedNetwork",
    "TrunkedNetworkList",
    "TrunkedNetworkPatchParameters",
    "ValidationThreshold",
    "VirtualMachine",
    "VirtualMachineList",
    "VirtualMachinePatchParameters",
    "VirtualMachinePlacementHint",
    "VirtualMachinePowerOffParameters",
    "VirtualMachineVolumeParameters",
    "Volume",
    "VolumeList",
    "VolumePatchParameters",
    "ActionType",
    "BareMetalMachineCordonStatus",
    "BareMetalMachineDetailedStatus",
    "BareMetalMachineEvacuate",
    "BareMetalMachineHardwareValidationCategory",
    "BareMetalMachineHardwareValidationResult",
    "BareMetalMachineKeySetDetailedStatus",
    "BareMetalMachineKeySetPrivilegeLevel",
    "BareMetalMachineKeySetProvisioningState",
    "BareMetalMachineKeySetUserSetupStatus",
    "BareMetalMachinePowerState",
    "BareMetalMachineProvisioningState",
    "BareMetalMachineReadyState",
    "BareMetalMachineSkipShutdown",
    "BmcKeySetDetailedStatus",
    "BmcKeySetPrivilegeLevel",
    "BmcKeySetProvisioningState",
    "BootstrapProtocol",
    "CloudServicesNetworkDetailedStatus",
    "CloudServicesNetworkEnableDefaultEgressEndpoints",
    "CloudServicesNetworkProvisioningState",
    "ClusterConnectionStatus",
    "ClusterDetailedStatus",
    "ClusterManagerConnectionStatus",
    "ClusterManagerDetailedStatus",
    "ClusterManagerProvisioningState",
    "ClusterMetricsConfigurationDetailedStatus",
    "ClusterMetricsConfigurationProvisioningState",
    "ClusterProvisioningState",
    "ClusterType",
    "ConsoleDetailedStatus",
    "ConsoleEnabled",
    "ConsoleProvisioningState",
    "ControlImpact",
    "CreatedByType",
    "DefaultCniNetworkDetailedStatus",
    "DefaultCniNetworkProvisioningState",
    "DefaultGateway",
    "DeviceConnectionType",
    "DiskType",
    "HybridAksClusterDetailedStatus",
    "HybridAksClusterMachinePowerState",
    "HybridAksClusterProvisioningState",
    "HybridAksIpamEnabled",
    "HybridAksPluginType",
    "IpAllocationType",
    "L2NetworkDetailedStatus",
    "L2NetworkProvisioningState",
    "L3NetworkDetailedStatus",
    "L3NetworkProvisioningState",
    "MachineSkuDiskConnectionType",
    "Origin",
    "OsDiskCreateOption",
    "OsDiskDeleteOption",
    "RackDetailedStatus",
    "RackProvisioningState",
    "RackSkuProvisioningState",
    "RackSkuType",
    "RemoteVendorManagementFeature",
    "RemoteVendorManagementStatus",
    "SkipShutdown",
    "StorageApplianceDetailedStatus",
    "StorageApplianceHardwareValidationCategory",
    "StorageApplianceProvisioningState",
    "TrunkedNetworkDetailedStatus",
    "TrunkedNetworkProvisioningState",
    "ValidationThresholdGrouping",
    "ValidationThresholdType",
    "VirtualMachineBootMethod",
    "VirtualMachineDetailedStatus",
    "VirtualMachineDeviceModelType",
    "VirtualMachineIPAllocationMethod",
    "VirtualMachineIsolateEmulatorThread",
    "VirtualMachinePlacementHintPodAffinityScope",
    "VirtualMachinePlacementHintType",
    "VirtualMachinePowerState",
    "VirtualMachineProvisioningState",
    "VirtualMachineSchedulingExecution",
    "VirtualMachineVirtioInterfaceType",
    "VolumeDetailedStatus",
    "VolumeProvisioningState",
    "WorkloadImpact",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
