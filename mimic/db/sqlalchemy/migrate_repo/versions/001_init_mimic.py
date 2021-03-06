# vim: tabstop=4 shiftwidth=4 softtabstop=4
# -*- encoding: utf-8 -*-
#
# Copyright 2013 Hewlett-Packard Development Company, L.P.
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


from sqlalchemy import Table, Column, ForeignKey, MetaData
from sqlalchemy import DateTime, Integer, String

from mimic.openstack.common import log as logging

LOG = logging.getLogger(__name__)

meta = MetaData()

lookup_value = Table('lookup_values', meta,
                     Column("id", Integer, primary_key=True, nullable=False),
                     Column("value", String(255)),
                     Column("match", String(255)),
                     Column("lookup_key_id", Integer),
                     Column("created_at", DateTime),
                     Column("updated_at", DateTime),
                     )


def upgrade(migrate_engine):
    meta.bind = migrate_engine
    lookup_value.create()


def downgrade(migrate_engine):
    meta.bind = migrate_engine
    lookup_value.drop()
