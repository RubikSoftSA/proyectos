# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
  "name" : "Módulo ejemplo",
  "version" : "0.1",
  "author" : "Fernando Vazquez Novoa",
  "website" : "http://ambiental.uvigo.es",
  "category" : "Unknown",
  "description": """Módulo ejemplo de programación de módulos """,
  'data': [],
  'depends' : ['base','web_pdf_widget'],
  'update_xml': ["modulo_ejemplo.xml"],
  'init_xml' : [ ],
  'demo_xml' : [ ],
  'installable': True,
  'active': False,
}
