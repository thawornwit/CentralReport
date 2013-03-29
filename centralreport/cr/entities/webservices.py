# -*- coding: utf-8 -*-

"""
    CentralReport - Webservices module
        Contains all entities used with webservices.

    https://github.com/miniche/CentralReport/
"""

from cr.utils import object


class Full:
    """
        This entity contains every host information
    """

    def __init__(self):
        self.checks = list()
        self.host = None

    def json_serialize(self):
        """
            Serializes this entity into JSON.
        """

        host_data = {
            'host': self.host.serialize()
        }

        host_data['host']['checks'] = []

        for check in self.checks:
            host_data['host']['checks'].append(check.serialize())

        object.object_converter(host_data, "json")


class Registration:
    """
        Entity used to get the host status on the remote server
    """

    def __init__(self):
        self.uuid = ""
        self.key = ""
        self.hostname = ""
        self.os = ""
        self.os_version = ""

    def serialize(self):
        """
            Serializes the current object
            @return: a dict with the class attributes
        """

        object.object_converter(self, "json")


class Answer:
    """
        This entity contains the result of a webservice
    """

    def __init__(self):
        self.code = 0
        self.headers = []
        self.text = ""

