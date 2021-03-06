# Copyright 2017 FiberHome Telecommunication Technologies CO.,LTD
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from tempest.lib.services.volume.v2 import volumes_client
from tempest.tests.lib import fake_auth_provider
from tempest.tests.lib.services import base


class TestVolumesClient(base.BaseServiceTest):

    FAKE_VOLUME_METADATA_ITEM = {
        "meta": {
            "key1": "value1"
        }
    }

    def setUp(self):
        super(TestVolumesClient, self).setUp()
        fake_auth = fake_auth_provider.FakeAuthProvider()
        self.client = volumes_client.VolumesClient(fake_auth,
                                                   'volume',
                                                   'regionOne')

    def _test_force_detach_volume(self, bytes_body=False):
        kwargs = {
            'attachment_id': '6980e295-920f-412e-b189-05c50d605acd',
            'connector': {
                'initiator': 'iqn.2017-04.org.fake:01'
            }
        }

        self.check_service_client_function(
            self.client.force_detach_volume,
            'tempest.lib.common.rest_client.RestClient.post',
            {},
            to_utf=bytes_body,
            status=202,
            volume_id="a3be971b-8de5-4bdf-bdb8-3d8eb0fb69f8",
            **kwargs
        )

    def _test_show_volume_metadata_item(self, bytes_body=False):
        self.check_service_client_function(
            self.client.show_volume_metadata_item,
            'tempest.lib.common.rest_client.RestClient.get',
            self.FAKE_VOLUME_METADATA_ITEM,
            to_utf=bytes_body,
            volume_id="a3be971b-8de5-4bdf-bdb8-3d8eb0fb69f8",
            id="key1")

    def test_force_detach_volume_with_str_body(self):
        self._test_force_detach_volume()

    def test_force_detach_volume_with_bytes_body(self):
        self._test_force_detach_volume(bytes_body=True)

    def test_show_volume_metadata_item_with_str_body(self):
        self._test_show_volume_metadata_item()

    def test_show_volume_metadata_item_with_bytes_body(self):
        self._test_show_volume_metadata_item(bytes_body=True)
