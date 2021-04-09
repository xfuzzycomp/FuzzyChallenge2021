from scenarios import *

portfolio = [
    # wall,
    # threat_test_1,
    # threat_test_2,
    # threat_test_3,
    # threat_test_4,
    # accuracy_test_1,
    # accuracy_test_2,
    # accuracy_test_3,
    # accuracy_test_4,
    # accuracy_test_5,
    # accuracy_test_6,
    # accuracy_test_7,
    # accuracy_test_8,
    # accuracy_test_9,
    # accuracy_test_10,
    # wall_left_easy,
    # wall_right_easy,
    # wall_top_easy,
    # wall_bottom_easy,
    # ring_closing,
    # ring_static_left,
    # ring_static_right,
    # ring_static_top,
    # ring_static_bottom,

    # wall_right_wrap_1,
    # wall_right_wrap_2,
    # wall_right_wrap_3,
    # wall_right_wrap_4,
    # wall_left_wrap_1,
    # wall_left_wrap_2,
    # wall_left_wrap_3,
    # wall_left_wrap_4,
    # wall_top_wrap_1,
    # wall_top_wrap_2,
    # wall_top_wrap_3,
    # wall_top_wrap_4,
    # wall_bottom_wrap_1,
    # wall_bottom_wrap_2,
    # wall_bottom_wrap_3,
    # wall_bottom_wrap_4,
]

show_portfolio = [

]

alternate_scenarios = [
    corridor_left,
    corridor_right,
    corridor_top,
    corridor_bottom,

    # May have to cut these
    moving_corridor_1,
    moving_corridor_2,
    moving_corridor_3,
    moving_corridor_4,
    moving_corridor_angled_1,
    moving_corridor_angled_2,
    moving_corridor_curve_1,
    moving_corridor_curve_2,

    scenario_small_box,
    scenario_big_box,
    scenario_2_still_corridors,
]

portfolio_dict = {scenario.name: scenario for scenario in portfolio}
show_portfolio_dict = {scenario.name: scenario for scenario in show_portfolio}