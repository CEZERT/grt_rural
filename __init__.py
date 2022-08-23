# -*- coding: utf-8 -*-
"""
/***************************************************************************
 GRT_Rural
                                 A QGIS plugin
 GRT_Rural
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2022-07-20
        copyright            : (C) 2022 by Marc Yeranosyan
        email                : marc.yeranosyan@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load GRT_Rural class from file GRT_Rural.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .GRT_Rural import GRT_Rural
    return GRT_Rural(iface)
