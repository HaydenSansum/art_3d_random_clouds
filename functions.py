import pandas as pd
import random

def return_offset(spread, offset):
    """
    Return a point offset which is either 0 or a random value determines by the multiplier "offset"
    The chance of being either zero or the number is based on the value of "spread"
    """
    move_cloud_check_num = random.random()
    if move_cloud_check_num > (spread - 1):
        actual_offset = random.random() * offset
    else:
        actual_offset = 0
    return(actual_offset)

def random_polarity_const():
    """
    A random 50/50 chance to return a 1 or a minus 1
    """
    if random.random() > 0.5:
        neg_const = 1
    else:
        neg_const = -1
    return(neg_const)

def create_random_points_list(n, spread, offset):
    """
    Create a single list of random points
    """
    a = 0
    points_out = []

    # Produce n points
    for i in range(n):
        
        actual_offset = return_offset(spread, offset)
        
        # Create a random 50/50 chance to be positive or negative
        neg_const = random_polarity_const()
                
        a = a + (neg_const * random.random()) + (neg_const * actual_offset)
        
        points_out.append(a)

    return(points_out)

def create_random_n_df_points(seed, n, dimensions, spread, offset):
    """
    Create a dataframe of random point lists


    spread - integer from 0 to 1, a spread of 1 will result in an offset 100% of the time
    offset - the ratio of spread distances (1 is no offset distance)
    """
    random.seed(seed)
    list_of_point_lists = []

    for i in range(dimensions):
        new_list = create_random_points_list(n, spread, offset)
        list_of_point_lists.append(new_list)

    df = pd.DataFrame(list_of_point_lists)
    return(df)