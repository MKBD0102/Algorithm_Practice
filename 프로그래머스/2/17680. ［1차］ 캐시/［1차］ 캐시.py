def solution(cacheSize, cities):
    cache = []
    runtime  = 0
    
    if cacheSize == 0:
        return 5 * len(cities)
    
    for city in cities:
        city = city.upper()
        if city in cache:
            cache.remove(city)
            cache.append(city)
            runtime += 1
        elif city not in cache and len(cache) < cacheSize :
                cache.append(city)
                runtime += 5
        elif city not in cache and len(cache) == cacheSize :
            del cache[0]
            cache.append(city)
            runtime += 5
                
    return runtime