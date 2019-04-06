import factory_test_common.test_station.test_equipment


class pancakeuniformityFixture(factory_test_common.test_station.test_equipment.TestEquipment):
    """
        class for pancake uniformity Equipment
            this is for doing all the specific things necessary to interface with equipment
    """
    def __init__(self, station_config, operator_interface):
        factory_test_common.test_station.test_equipment.TestEquipment.__init__(self, station_config, operator_interface)

    def is_ready(self):
        pass

    def initialize(self):
        self._operator_interface.print_to_console("Initializing pancake uniformity Fixture\n")

    def close(self):
        self._operator_interface.print_to_console("Closing pancake uniformity Fixture\n")
