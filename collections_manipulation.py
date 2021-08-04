from math_operation import distance_3d_points

def get_top_colors(colors_tuples : list) -> dict:

    return sorted(colors_tuples,reverse=True)

def get_unsimilar_rgbs(rgbs : list, max_rgbs : int) -> list:

    unsimilar_rgbs = list()
    unsimilar_rgbs.append(rgbs[0])

    for rgb in rgbs:
        
        distances_unsimilar_rgbs = []

        for rgb_unsimilar in unsimilar_rgbs:
            
            distance_between_rgbs = distance_3d_points(rgb[1],rgb_unsimilar[1])
            distances_unsimilar_rgbs.append(distance_between_rgbs)

        if all(i>=70 for i in distances_unsimilar_rgbs):
            unsimilar_rgbs.append(rgb)

        if len(unsimilar_rgbs) == max_rgbs:
            return unsimilar_rgbs

    return unsimilar_rgbs
