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
        self.alt_seeds = []
        for i in range(0, len(seeds), 2):
            self.alt_seeds.append((seeds[i], seeds[i + 1]))
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
    
    def find_closest_position_from_tuple(self):
        all_pos = self.get_positions_tuple(self.alt_seeds)
        return min((k for k,_ in all_pos))

    def get_positions_tuple(self, seeds: list[tuple[int, int]]) -> list[tuple[int, int]]:
        current = seeds
        for ft in self.from_to:
            next_range = []
            for key, range_key in current:
                next_range.extend(self.__tuple_equivalence(key, range_key, ft))
            current = next_range
        return current

    def __untuple(self, l: list[tuple[int, int, int]]) -> dict[int, tuple[int, int]]:
        to_dict = {source: (dest, nb) for dest, source, nb in l}
        self.__expand_dict(to_dict)
        return to_dict

    def __equivalence(self, key: int, ft: dict[int, tuple[int, int]]) -> int:
        found, k_interval = self.__find_interval(key, ft)
        if found:
            return ft[k_interval][0] + key - k_interval
        else:
            return key

    def __tuple_equivalence(
        self, key: int, range_key: int, ft: dict[int, tuple[int, int]]
    ) -> list[tuple[int, int]]:
        if range_key == 0:
            return []
        found, k_interval = self.__find_interval(key, ft)
        if found:
            range_interval = ft[k_interval][1]
            keys_left = range_interval - key + k_interval
            if range_key <= keys_left:
                return [(self.__equivalence(key, ft), range_key)]
            else:
                return [(self.__equivalence(key, ft), keys_left)] + self.__tuple_equivalence(
                    key + keys_left, range_key - keys_left, ft
                )
        else:
            return [(key, range_key)]

    def __find_interval(
        self, key: int, ft: dict[int, tuple[int, int]]
    ) -> tuple[bool, int]:
        for k in ft.keys():
            if key >= k and key < k + ft[k][1]:
                return True, k
        return False, key

    def __expand_dict(self, l: dict[int, tuple[int, int]]) -> None:
        current_key = 0
        keys = sorted(l.keys())
        i = 0
        while i < len(keys):
            if current_key == keys[i]:
                current_key += l[current_key][1]
                i += 1
            else:
                l[current_key] = (current_key, keys[i] - current_key)
                current_key = keys[i]
