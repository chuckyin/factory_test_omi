import factory_test_common.test_station.dut


class pancakeuniformityDut(factory_test_common.test_station.dut.DUT):
    """
        class for pancake uniformity DUT
            this is for doing all the specific things necessary to DUT
    """
    def __init__(self, serial_number, station_config, operator_interface):
        factory_test_common.test_station.dut.DUT.__init__(self, serial_number, station_config, operator_interface)

    def is_ready(self):
        pass

    def initialize(self):
        self._operator_interface.print_to_console("Initializing pancake uniformity Fixture\n")

    def close(self):
        self._operator_interface.print_to_console("Closing pancake uniformity Fixture\n")
