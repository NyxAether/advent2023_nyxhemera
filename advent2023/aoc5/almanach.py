class Almanach:
    def __init__(
        self,
        seeds: list[int],
        seeds_soils: list[tuple[int, int, int]],
        soils_fert: list[tuple[int, int, int]],
        fert_water: list[tuple[int, int, int]],
        water_light: list[tuple[int, int, int]],
        light_temp: list[tuple[int, int, int]],
        temp_hum: list[tuple[int, int, int]],
        hum_loc: list[tuple[int, int, int]],
    ):
        self.seeds = seeds
        self.alt_seeds = {}
        for i in range(0,len(seeds),2):
            self.alt_seeds[seeds[i]]==seeds[i+1]
        self.from_to = (
            self.__untuple(seeds_soils),
            self.__untuple(soils_fert),
            self.__untuple(fert_water),
            self.__untuple(water_light),
            self.__untuple(light_temp),
            self.__untuple(temp_hum),
            self.__untuple(hum_loc),
        )

    def get_position(self, key: int) -> int:
        for ft in self.from_to:
            key = self.__equivalence(key, ft)
        return key

    def find_closest_position(self) -> int:
        all_pos = [self.get_position(seed) for seed in self.seeds]
        return min(all_pos)

    def __untuple(self, l: list[tuple[int, int, int]]) -> dict[int, tuple[int, int]]:
        to_dict = {source: (dest, nb) for dest, source, nb in l}
        return to_dict

    def __equivalence(self, key: int, ft: dict[int, tuple[int, int]]) -> int:
        found, k_interval = self.__find_interval(key, ft)
        if found:
            return ft[k_interval][0] + key - k_interval
        else:
            return key

    def __find_interval(
        self, key: int, ft: dict[int, tuple[int, int]]
    ) -> tuple[bool, int]:
        for k in ft.keys():
            if key >= k and key <= k + ft[k][1]:
                return True, k
        return False, key
