#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#
# Imports
#
from future import standard_library
standard_library.install_aliases()
from builtins import str
import os
import sys
import urllib.parse
import xbmc
import xbmcaddon

LIB_DIR = xbmc.translatePath(
    os.path.join(xbmcaddon.Addon(id="plugin.video.dumpert").getAddonInfo('path'), 'resources', 'lib'))
sys.path.append(LIB_DIR)

from dumpert_const import ADDON, DATE, VERSION, SETTINGS

# Parse parameters...
if len(sys.argv[2]) == 0:
    #
    # Main menu
    #
    xbmc.log("[ADDON] %s, Python Version %s" % (ADDON, str(sys.version)), xbmc.LOGDEBUG)
    xbmc.log("[ADDON] %s v%s (%s) is starting, ARGV = %s" % (ADDON, VERSION, DATE, repr(sys.argv)),
                 xbmc.LOGDEBUG)

    if SETTINGS.getSetting('onlyshownewvideocategory') == 'true':
        import dumpert_list as plugin
    else:
        import dumpert_main as plugin
else:
    action = urllib.parse.parse_qs(urllib.parse.urlparse(sys.argv[2]).query)['action'][0]
    #
    # Themas
    #
    if action == 'list-themas':
        import dumpert_list_themas as plugin
    #
    # List
    #
    elif action == 'list':
        import dumpert_list as plugin
    #
    # Play
    #
    elif action == 'play':
        import dumpert_play as plugin

    #
    # Play file
    #
    elif action == 'play-file':
        import dumpert_play_file as plugin

    #
    # Search
    #
    elif action == 'search':
        import dumpert_search as plugin

    #
    # Timemachine
    #
    elif action == 'timemachine':
        import dumpert_timemachine as plugin

    #
    # JSON
    #
    elif action == 'json':
        import dumpert_json as plugin

plugin.Main()
