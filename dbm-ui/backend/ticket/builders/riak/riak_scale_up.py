# -*- coding: utf-8 -*-
"""
TencentBlueKing is pleased to support the open source community by making 蓝鲸智云-DB管理系统(BlueKing-BK-DBM) available.
Copyright (C) 2017-2023 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at https://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.
"""

import logging

from django.utils.translation import ugettext as _
from rest_framework import serializers

from backend.db_meta.enums import ClusterPhase
from backend.db_meta.models import Cluster
from backend.db_services.dbbase.constants import IpSource
from backend.flow.engine.controller.riak import RiakController
from backend.ticket import builders
from backend.ticket.builders.common.bigdata import BaseKafkaTicketFlowBuilder
from backend.ticket.builders.riak.base import BaseRiakTicketFlowBuilder
from backend.ticket.constants import TicketType

logger = logging.getLogger("root")


class RiakScaleUpDetailSerializer(serializers.Serializer):
    cluster_id = serializers.Serializer(help_text=_("集群ID"))
    ip_source = serializers.ChoiceField(help_text=_("主机来源"), choices=IpSource.get_choices())
    resource_spec = serializers.JSONField(help_text=_("资源池规格"), required=False)


class RiakScaleUpFlowParamBuilder(builders.FlowParamBuilder):
    controller = RiakController.riak_cluster_scale_out_scene

    def format_ticket_data(self):
        # TODO: 补充db version
        cluster = Cluster.objects.get(id=self.ticket_data["cluster_id"])
        self.ticket_data["bk_cloud_id"] = cluster.bk_cloud_id


class RiakScaleUpResourceParamBuilder(builders.ResourceApplyParamBuilder):
    def post_callback(self):
        next_flow = self.ticket.next_flow()
        riak_nodes = next_flow.details["ticket_data"].pop("nodes")["riak"]
        next_flow.details["ticket_data"].update(nodes=riak_nodes)
        next_flow.save(update_fields=["details"])


@builders.BuilderFactory.register(TicketType.RIAK_CLUSTER_SCALE_OUT, is_apply=True)
class RiakScaleUpFlowBuilder(BaseRiakTicketFlowBuilder):
    serializer = RiakScaleUpDetailSerializer
    resource_apply_builder = RiakScaleUpResourceParamBuilder
    inner_flow_builder = RiakScaleUpFlowParamBuilder
    inner_flow_name = _("Riak 集群扩容")
