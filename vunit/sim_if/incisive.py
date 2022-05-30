# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Copyright (c) 2014-2021, Lars Asplund lars.anders.asplund@gmail.com

"""
Interface for the Cadence Incisive simulator
"""

from ..vhdl_standard import VHDL
from . import ListOfStringOption
from .xcelium import XceliumInterface


class IncisiveInterface(XceliumInterface):
    """
    Interface for the Cadence Incisive simulator
    """

    name = "incisive"
    executable_name = "irun"
    option_prefix = "nc"

    compile_options = [
        ListOfStringOption("incisive.irun_vhdl_flags"),
        ListOfStringOption("incisive.irun_verilog_flags"),
    ]

    sim_options = [
        ListOfStringOption("incisive.irun_sim_flags")
    ]

    @staticmethod
    def add_arguments(parser):
        """
        Add command line arguments
        """
        # NOTE: Incisive shares the command-line arguments with Xcelium

    @staticmethod
    def supports_vhdl_contexts():
        """
        Returns True when this simulator supports VHDL 2008 contexts
        """
        return False

    @staticmethod
    def _vhdl_std_opt(vhdl_standard):
        """
        Convert standard to format of xrun command line flag
        """
        if vhdl_standard == VHDL.STD_2002:
            return "-v200x -extv200x"

        if vhdl_standard == VHDL.STD_2008:
            return "-v200x -extv200x"

        if vhdl_standard == VHDL.STD_1993:
            return "-v93"

        raise ValueError("Invalid VHDL standard %s" % vhdl_standard)
