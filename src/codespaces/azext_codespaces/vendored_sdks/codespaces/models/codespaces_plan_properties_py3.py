# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class CodespacesPlanProperties(Model):
    """Codespaces Additional properties.

    Additional Codespaces Plan properties.

    :param default_auto_suspend_delay_minutes: Specifies auto suspend interval
     for codespaces in this plan.
    :type default_auto_suspend_delay_minutes: long
    :param default_codespace_sku: Specifies the default codespace sku name for
     this plan.
    :type default_codespace_sku: str
    :param vnet_properties: Specifies the vnet injection properties for this
     plan.
    :type vnet_properties: ~microsoft.codespaces.models.VnetProperties
    """

    _attribute_map = {
        'default_auto_suspend_delay_minutes': {'key': 'defaultAutoSuspendDelayMinutes', 'type': 'long'},
        'default_codespace_sku': {'key': 'defaultCodespaceSku', 'type': 'str'},
        'vnet_properties': {'key': 'vnetProperties', 'type': 'VnetProperties'},
    }

    def __init__(self, *, default_auto_suspend_delay_minutes: int=None, default_codespace_sku: str=None, vnet_properties=None, **kwargs) -> None:
        super(CodespacesPlanProperties, self).__init__(**kwargs)
        self.default_auto_suspend_delay_minutes = default_auto_suspend_delay_minutes
        self.default_codespace_sku = default_codespace_sku
        self.vnet_properties = vnet_properties
