#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#Author: Read AUTHORS file.
#License: Read COPYING file.


class _const:
    class ConstError(TypeError): pass
    def __setattr__(self,name,value):
        if self.__dict__.has_key(name):
            raise self.ConstError, "Can't rebind const(%s)"%name
        self.__dict__[name]=value


const = _const()


#Include const and use global values below

const.APP_NAME = "paso"
const.APP_I18NDIR = "/usr/share/locale/"


const.JOB_NONE_ID = 0
const.JOB_INS_ID = 1
const.JOB_REP_ID = 2
const.JOB_ISO_ID = 3
const.JOB_ALT_ID = 4
const.JOB_RES_ID = 5
const.JOB_PAS_ID = 6
const.JOB_PAO_ID = 7
const.JOB_ALZ_ID = 8
const.JOB_CHC_ID = 9
const.JOB_BRP_ID = 10
const.JOB_BIS_ID = 11
const.JOB_SUCCES_ID = 12

const.OPT_ISODIRCHECK_ID = 1
const.OPT_ALTDIRCHECK_ID = 2
const.OPT_READINSCHECK_ID = 3
const.OPT_READREPOCHECK_ID = 4
const.OPT_ROOTDIR_ID = 5
const.OPT_ISODIR_ID = 6
const.OPT_ALTDIR_ID = 7
const.OPT_PASOFILE_ID = 8
const.OPT_OUTDIR_ID = 9
const.OPT_READPASOCHECK_ID = 10
const.OPT_READALTCHECK_ID = 11
const.OPT_FORCEPASOREAD_ID= 12
const.OPT_FORCECDREAD_ID = 13
const.OPT_FORCEALTREAD_ID = 14

const.OPT_CACHEPATH_VAL = "/var/cache/pisi/packages"
const.OPT_PACKPATH_VAL = "/var/lib/pisi/package"
const.OPT_INFOPATH_VAL = "/var/lib/pisi/info"
const.OPT_INDEXPATH_VAL = "/var/lib/pisi/index"
const.OPT_CDREPOPATH_VAL = "/repo"

const.PASO_DATAFILE_VAL = "packages.txt"
const.PACKAGE_INFO_FILE = "metadata.xml"
const.PASO_EXT = ".paso"
const.ISO_EXT = ".iso"
const.PISI_EXT = ".pisi"

const.ERR_01_ID = 1
const.ERR_02_ID = 2
const.ERR_03_ID = 3
const.ERR_04_ID = 4
const.ERR_05_ID = 5
const.ERR_06_ID = 6
const.ERR_07_ID = 7
const.ERR_08_ID = 8
const.ERR_09_ID = 9
