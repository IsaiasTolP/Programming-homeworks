class Plane:
    BLACKBOX = True

    @staticmethod
    def on_ground(method):
        def wrapper(self, *args, **kwargs):
            return method(self, *args, **kwargs) if not self.in_air else print('ERROR: Plane is in the air right now.')
        return wrapper

    @staticmethod
    def on_flight(method):
        def wrapper(self, *args, **kwargs):
            return method(self, *args, **kwargs) if self.in_air else print('ERROR: Plane is currently on ground.')
        return wrapper

    def __init__(
        self,
        seats: int,
        fuel_capacity: float,
        max_weight: float,
        curr_location: str,
        manufacturer: str,
        model: str,
    ):
        self.seats = seats
        self.fuel_capacity = fuel_capacity
        self.max_weight = max_weight
        self.curr_location = curr_location
        self.manufacturer = manufacturer
        self.model = model
        self.passengers = 0
        self.curr_fuel = 0.0
        self.in_air = False
        self.curr_destination = None
        self.loaded_weight = 0.0
        self.ocuppation_percentage = 0.0

    @staticmethod
    def get_possible_destinations() -> tuple[str]:
        return ('Madrid', 'Barcelona', 'Valencia', 'Sevilla', 'Milan', 'Paris')

    @property
    def occupation_percentage(self) -> float:
        return round(self.passengers / self.seats * 100, 2)

    def get_current_state(self):
        print()
        print(f'''El actual estado del avión es: Pasajeros: {self.passengers}; Queroseno a bordo: {self.curr_fuel}; Está en el aire: {self.in_air};
Destino actual: {self.curr_destination}; Carga a bordo: {self.loaded_weight}; Localización: {self.curr_location}''')

    def select_destination(self):
        print()
        print(Plane.get_possible_destinations())
        destination = input('Por favor inserte aeropuerto de destino: ').title()
        if destination in Plane.get_possible_destinations():
            self.curr_destination = destination
            print(f'Destination selected: {destination}')
        else:
            print('This destination is not possible')
            self.select_destination()

    @on_ground
    def take_off(self):
        self.in_air = True
        print('Plane has taken off.')

    @on_flight
    def land(self, expended_fuel: float):
        self.in_air = False
        print('Plane has landed.')
        self.curr_location = self.curr_destination
        self.curr_destination = None
        self.curr_fuel -= expended_fuel

    @on_flight
    def info_on_trip(self):
        print()
        print(f'''Señoras y señores pasajeros, al habla el capitán del avión
Nuestro vuelo con origen {self.curr_location} y destino {self.curr_destination}, será un vuelo tranquilo sin turbulencias.
El avión es el {self.manufacturer} {self.model} y tiene una capacidad de {self.seats} pasajeros, de los que ahora mismo se encuentran ocupados {self.passengers}.''')
        if self.ocuppation_percentage < 25:
            print(
                f'La actual ocupación del vuelo es baja, del {self.occupation_percentage}%, por lo que esperamos que disfruten de un comodo vuelo.'
            )
        elif self.ocuppation_percentage < 60:
            print(
                f'La actual ocupación del vuelo es media, del {self.ocuppation_percentage}%, será un vuelo cómodo pero por favor, tengan cuidado en los pasillos.'
            )
        else:
            print(
                f'La actual ocupación del vuelo es alta, del {self.ocuppation_percentage}%, por favor ruego que piden permiso para levantarse o ir al baño, la convivencia a bordo será esencial durante el vuelo.'
            )

    @on_flight
    def in_air_services(self):
        print('Atención pasajeros, vamos a proceder con el servicio de abordo')
        print('¿Quiere un vaso de agua y una Tirma?')
        say = input('¿Qué le digo?: ').lower()
        return say == 'si'

    @on_ground
    def refuel(self, fuel: float):
        if fuel < self.fuel_capacity - self.curr_fuel:
            self.curr_fuel += fuel
        else:
            print('Too much fuel, we will fill the tank.')
            self.curr_fuel = self.fuel_capacity
            print('Plane refueled')

    @on_ground
    def unload_fuel(self):
        self.curr_fuel = 0

    @on_ground
    def board(self, num_passengers: int):
        self.passengers = num_passengers
        if self.passengers > self.seats:
            print('This flight has overbooking. Be sure to fleet another flight.')
            self.passengers = self.seats
            self.ocuppation_percentage = 100
        print('Passengers boarded.')

    @on_ground
    def disembark(self):
        self.passengers = 0
        print('Plane has successfully disembarked.')

    @on_ground
    def load_hold(self, cargo_weight: float):
        if self.loaded_weight > self.max_weight:
            self.loaded_weight += cargo_weight
        else:
            print('We cannot take off due to the current weight')

    @on_ground
    def unload_hold(self):
        self.loaded_weight = 0


def do_a_flight(
    plane: Plane, passengers: int, necessary_fuel: float, added_weight: float
):
    plane.select_destination()
    while plane.curr_location == plane.curr_destination:
        print('We are already here.')
        plane.select_destination()
    if plane.BLACKBOX and not plane.in_air:
        plane.refuel(necessary_fuel)
        plane.board(passengers)
        plane.load_hold(added_weight)
        plane.take_off()
        plane.info_on_trip()
        has_tirma = plane.in_air_services()
        plane.land(necessary_fuel)
        plane.disembark()
        plane.unload_hold()
        plane.unload_fuel()
        plane.get_current_state()
        print('El avión ha llegado a su destino.')
        print(f'¿Tengo una Tirma?: {has_tirma}')


if __name__ == '__main__':
    IberiaFXA567 = Plane(335, 400.3, 200.548, 'Madrid', 'Airbus', 'A330')
    QatarAirLAF452 = Plane(300, 350.5, 254.011, 'Paris', 'Boeing', 'B787-9 Dreamliner')
    do_a_flight(plane=IberiaFXA567, passengers=240, necessary_fuel=150.30, added_weight=300.23)
    do_a_flight(plane=QatarAirLAF452, passengers=96, necessary_fuel=100.90, added_weight=200.50)
