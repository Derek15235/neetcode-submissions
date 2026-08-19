class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for i in range(len(position)):
            cars.append((position[i], speed[i]))

        cars.sort(reverse=True)

        fleets = []
        for car in cars:
            pos, speed = car[0], car[1]
            finTime = (target - pos) / speed

            if fleets and fleets[-1] < finTime:
                fleets.append(finTime)
            elif not fleets:
                fleets.append(finTime)
        return len(fleets)

            