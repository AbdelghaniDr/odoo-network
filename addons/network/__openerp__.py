# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2008 Tiny SPRL (<http://tiny.be>). All Rights Reserved
#    $Id$
#    code migrated to v7.0 by : nhomar@vauxoo.com
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    "name": "Network Management",
    "version": "1.0.6",
    "author": "Tiny & Vauxoo",
    "category": "Hardware Administration",
    "depends": [
        "base",
        "project", #Because a change in hardware or update MUST be a task.
        ],
    "description": """
A simple module to encode your networks and materials:

- Networks and connections between networks
- Hardwares and softwares with:
    - Versions
    - Access rights
    - Waranties.
- You can print interventions form for technical people.

Organize your software and configurations.

    - Additional network information: IP, domain, DNS, gateway
    - Protocols
    - Services
    - Ports
    - Public and private URLs
    - Password encryption

System dependency: package python-crypto required.
    """,
    "demo": [
        "demo/network_demo.xml"
        ],
    "data": [
        "data/module_data.xml",
        "security/network_security.xml",
        "security/ir.model.access.csv",
        "view/network_view.xml",
        "view/network_extension_view.xml",
        "report/network_report.xml",
        "data/network_data.xml",
        'data/network_protocol_data.xml',
        ],
    "active": False,
    "installable": True
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
