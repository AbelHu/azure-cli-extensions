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

from .sub_resource import SubResource


class HealthProbeSettingsModel(SubResource):
    """Load balancing settings for a backend pool.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param id: Resource ID.
    :type id: str
    :param path: The path to use for the health probe. Default is /
    :type path: str
    :param protocol: Protocol scheme to use for this probe. Possible values
     include: 'Http', 'Https'
    :type protocol: str or ~azure.mgmt.frontdoor.models.FrontDoorProtocol
    :param interval_in_seconds: The number of seconds between health probes.
    :type interval_in_seconds: int
    :param health_probe_method: Configures which HTTP method to use to probe
     the backends defined under backendPools. Possible values include: 'GET',
     'HEAD'. Default value: "HEAD" .
    :type health_probe_method: str or
     ~azure.mgmt.frontdoor.models.FrontDoorHealthProbeMethod
    :param enabled_state: Whether to enable health probes to be made against
     backends defined under backendPools. Health probes can only be disabled if
     there is a single enabled backend in single enabled backend pool. Possible
     values include: 'Enabled', 'Disabled'
    :type enabled_state: str or
     ~azure.mgmt.frontdoor.models.HealthProbeEnabled
    :param resource_state: Resource status. Possible values include:
     'Creating', 'Enabling', 'Enabled', 'Disabling', 'Disabled', 'Deleting'
    :type resource_state: str or
     ~azure.mgmt.frontdoor.models.FrontDoorResourceState
    :param name: Resource name.
    :type name: str
    :ivar type: Resource type.
    :vartype type: str
    """

    _validation = {
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'path': {'key': 'properties.path', 'type': 'str'},
        'protocol': {'key': 'properties.protocol', 'type': 'str'},
        'interval_in_seconds': {'key': 'properties.intervalInSeconds', 'type': 'int'},
        'health_probe_method': {'key': 'properties.healthProbeMethod', 'type': 'str'},
        'enabled_state': {'key': 'properties.enabledState', 'type': 'str'},
        'resource_state': {'key': 'properties.resourceState', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(HealthProbeSettingsModel, self).__init__(**kwargs)
        self.path = kwargs.get('path', None)
        self.protocol = kwargs.get('protocol', None)
        self.interval_in_seconds = kwargs.get('interval_in_seconds', None)
        self.health_probe_method = kwargs.get('health_probe_method', "HEAD")
        self.enabled_state = kwargs.get('enabled_state', None)
        self.resource_state = kwargs.get('resource_state', None)
        self.name = kwargs.get('name', None)
        self.type = None