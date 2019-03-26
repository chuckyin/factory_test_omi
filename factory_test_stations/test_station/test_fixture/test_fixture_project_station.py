import factory_test_common.test_station.test_fixture


class projectstationFixture(factory_test_common.test_station.test_fixture.TestFixture):
    """
        class for project station Fixture
            this is for doing all the specific things necessary to interface with instruments
    """
    def __init__(self, station_config, operator_interface):
        factory_test_common.test_station.test_fixture.TestFixture.__init__(self, station_config, operator_interface)

    def is_ready(self):
        pass

    def initialize(self):
        self._operator_interface.print_to_console("Initializing project station Fixture\n")

    def close(self):
        self._operator_interface.print_to_console("Closing project station Fixture\n")
