#!/usr/bin/env python
# -*- coding:utf-8 -*-


# ############################################################################
#  license :
# ============================================================================
#
#  File :        MRUDeviceServer.py
#
#  Project :     MRUDeviceServer
#
# This file is part of Tango device class.
# 
# Tango is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# Tango is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with Tango.  If not, see <http://www.gnu.org/licenses/>.
# 
#
#  $Author :      thomas.madsen$
#
#  $Revision :    $
#
#  $Date :        $
#
#  $HeadUrl :     $
# ============================================================================
#            This file is generated by POGO
#     (Program Obviously used to Generate tango Object)
# ############################################################################

__all__ = ["MRUDeviceServer", "MRUDeviceServerClass", "main"]

__docformat__ = 'restructuredtext'

import PyTango
import sys
# Add additional import
#----- PROTECTED REGION ID(MRUDeviceServer.additionnal_import) ENABLED START -----#

#----- PROTECTED REGION END -----#	//	MRUDeviceServer.additionnal_import

# Device States Description
# No states for this device


class MRUDeviceServer (PyTango.Device_4Impl):
    """"""
    
    # -------- Add you global variables here --------------------------
    #----- PROTECTED REGION ID(MRUDeviceServer.global_variables) ENABLED START -----#
    
    #----- PROTECTED REGION END -----#	//	MRUDeviceServer.global_variables

    def __init__(self, cl, name):
        PyTango.Device_4Impl.__init__(self,cl,name)
        self.debug_stream("In __init__()")
        MRUDeviceServer.init_device(self)
        #----- PROTECTED REGION ID(MRUDeviceServer.__init__) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	MRUDeviceServer.__init__
        
    def delete_device(self):
        self.debug_stream("In delete_device()")
        #----- PROTECTED REGION ID(MRUDeviceServer.delete_device) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	MRUDeviceServer.delete_device

    def init_device(self):
        self.debug_stream("In init_device()")
        self.get_device_properties(self.get_device_class())
        self.attr_Weight401_read = 0.0
        self.attr_Pressure402_read = 0.0
        self.attr_Pressure401_read = 0.0
        self.attr_Flow401_read = 0.0
        self.attr_Flow402_read = 0.0
        #----- PROTECTED REGION ID(MRUDeviceServer.init_device) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	MRUDeviceServer.init_device

    def always_executed_hook(self):
        self.debug_stream("In always_excuted_hook()")
        #----- PROTECTED REGION ID(MRUDeviceServer.always_executed_hook) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	MRUDeviceServer.always_executed_hook

    # -------------------------------------------------------------------------
    #    MRUDeviceServer read/write attribute methods
    # -------------------------------------------------------------------------
    
    def read_Weight401(self, attr):
        self.debug_stream("In read_Weight401()")
        #----- PROTECTED REGION ID(MRUDeviceServer.Weight401_read) ENABLED START -----#
        attr.set_value(self.attr_Weight401_read)
        
        #----- PROTECTED REGION END -----#	//	MRUDeviceServer.Weight401_read
        
    def read_Pressure402(self, attr):
        self.debug_stream("In read_Pressure402()")
        #----- PROTECTED REGION ID(MRUDeviceServer.Pressure402_read) ENABLED START -----#
        attr.set_value(self.attr_Pressure402_read)
        
        #----- PROTECTED REGION END -----#	//	MRUDeviceServer.Pressure402_read
        
    def read_Pressure401(self, attr):
        self.debug_stream("In read_Pressure401()")
        #----- PROTECTED REGION ID(MRUDeviceServer.Pressure401_read) ENABLED START -----#
        attr.set_value(self.attr_Pressure401_read)
        
        #----- PROTECTED REGION END -----#	//	MRUDeviceServer.Pressure401_read
        
    def read_Flow401(self, attr):
        self.debug_stream("In read_Flow401()")
        #----- PROTECTED REGION ID(MRUDeviceServer.Flow401_read) ENABLED START -----#
        attr.set_value(self.attr_Flow401_read)
        
        #----- PROTECTED REGION END -----#	//	MRUDeviceServer.Flow401_read
        
    def read_Flow402(self, attr):
        self.debug_stream("In read_Flow402()")
        #----- PROTECTED REGION ID(MRUDeviceServer.Flow402_read) ENABLED START -----#
        attr.set_value(self.attr_Flow402_read)
        
        #----- PROTECTED REGION END -----#	//	MRUDeviceServer.Flow402_read
        
    
    
            
    def read_attr_hardware(self, data):
        self.debug_stream("In read_attr_hardware()")
        #----- PROTECTED REGION ID(MRUDeviceServer.read_attr_hardware) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	MRUDeviceServer.read_attr_hardware


    # -------------------------------------------------------------------------
    #    MRUDeviceServer command methods
    # -------------------------------------------------------------------------
    

    #----- PROTECTED REGION ID(MRUDeviceServer.programmer_methods) ENABLED START -----#
    
    #----- PROTECTED REGION END -----#	//	MRUDeviceServer.programmer_methods

class MRUDeviceServerClass(PyTango.DeviceClass):
    # -------- Add you global class variables here --------------------------
    #----- PROTECTED REGION ID(MRUDeviceServer.global_class_variables) ENABLED START -----#
    
    #----- PROTECTED REGION END -----#	//	MRUDeviceServer.global_class_variables


    #    Class Properties
    class_property_list = {
        }


    #    Device Properties
    device_property_list = {
        }


    #    Command definitions
    cmd_list = {
        }


    #    Attribute definitions
    attr_list = {
        'Weight401':
            [[PyTango.DevDouble,
            PyTango.SCALAR,
            PyTango.READ],
            {
                'Polling period': "1000",
            } ],
        'Pressure402':
            [[PyTango.DevDouble,
            PyTango.SCALAR,
            PyTango.READ],
            {
                'Polling period': "1000",
            } ],
        'Pressure401':
            [[PyTango.DevDouble,
            PyTango.SCALAR,
            PyTango.READ],
            {
                'Polling period': "1000",
            } ],
        'Flow401':
            [[PyTango.DevDouble,
            PyTango.SCALAR,
            PyTango.READ],
            {
                'Polling period': "1000",
            } ],
        'Flow402':
            [[PyTango.DevDouble,
            PyTango.SCALAR,
            PyTango.READ],
            {
                'Polling period': "1000",
            } ],
        }


def main():
    try:
        py = PyTango.Util(sys.argv)
        py.add_class(MRUDeviceServerClass, MRUDeviceServer, 'MRUDeviceServer')
        #----- PROTECTED REGION ID(MRUDeviceServer.add_classes) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	MRUDeviceServer.add_classes

        U = PyTango.Util.instance()
        U.server_init()
        U.server_run()

    except PyTango.DevFailed as e:
        print ('-------> Received a DevFailed exception:', e)
    except Exception as e:
        print ('-------> An unforeseen exception occured....', e)

if __name__ == '__main__':
    main()
