# 1333. Filter Restaurants by Vegan-Friendly, Price and Distance
from typing import List

class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        # Filter restaurants based on veganFriendly, maxPrice, and maxDistance
        filtered_restaurants = [r for r in restaurants if r[2] >= veganFriendly and r[3] <= maxPrice and r[4] <= maxDistance]
        
        # Sort filtered restaurants by rating (descending) and id (descending)
        sorted_restaurants = sorted(filtered_restaurants, key=lambda r: (-r[1], -r[0]))
        
        # Return the ids of the sorted restaurants
        return [r[0] for r in sorted_restaurants]
