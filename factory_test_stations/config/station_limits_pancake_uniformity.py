CURRENT_FW_VERSION = 1001

STATION_LIMITS_ARRAYS = [
    
    ["W255_CenterColor(Cx)", 0.2782, 0.3218, 101],
    ["W255_CenterColor(Cy)", 0.2982, 0.3418, 102],
    ["W255_CenterLv", 87.88, 112.65, 103],
    ["W255_MinLv", 80.92, 126.08, 104],
    ["W255_MaxLv", 80.92, 126.08, 105],
    ["W255_MLOGlobalLvMaxVariation", -1E-12, 30.92, 106],
    ["W255_MLOLocalLvMaxVariation", -1E-12, 5.87, 107],
    ["W255_MLOGlobalColorMaxVariation", -1E-12, 0.01560, 108],
    ["W255_MLOLocalColorMaxVariation", -1E-12, 0.0102, 109],
    ["W255_Centeru_prime", 0.1702, 0.2208, 110],
    ["W255_Centerv_prime", 0.4402, 0.4838, 111],
    ["W255_LvUniformity", 75, 100, 112], ## added by CY

    ["W180_CenterLv", 38.15, 52.33, 203],
    ["W180_MinLv", 35.76, 62.05, 204],
    ["W180_MaxLv", 35.76, 62.05, 205],
    ["W180_MLOGlobalLvMaxVariation", -1E-12, 37.63, 206],
    ["W180_MLOLocalLvMaxVariation", -1E-12, 6.29, 207],
    ["W180_MLOGlobalColorMaxVariation", -1E-12, 0.01560, 208],
    ["W180_MLOLocalColorMaxVariation", -1E-12, 0.0102, 209],
    ["W180_CenterColorDifference", -1E-12, 0.0101, 210],

    ["W127_CenterLv", 17.23, 34.27, 303],
    ["W127_MinLv", 15.25, 41.06, 304],
    ["W127_MaxLv", 15.25, 41.06, 305],
    ["W127_MLOGlobalLvMaxVariation", -1E-12, 37.63, 306],
    ["W127_MLOLocalLvMaxVariation", -1E-12, 6.92, 307],
    ["W127_MLOGlobalColorMaxVariation", -1E-12, 0.01560, 308],
    ["W127_MLOLocalColorMaxVariation", -1E-12, 0.0102, 309],
    ["W127_CenterColorDifference", -1E-12, 0.0101, 310],

    ["W090_CenterLv", 7.7, 15.63, 403],
    ["W090_MinLv", 6.61, 16.3, 404],
    ["W090_MaxLv", 6.61, 16.3, 405],
    ["W090_MLOGlobalLvMaxVariation", -1E-12, 58.28, 406],
    ["W090_MLOLocalLvMaxVariation", -1E-12, 8.07, 407],
    ["W090_MLOGlobalColorMaxVariation", -1E-12, 0.01660, 408],
    ["W090_MLOLocalColorMaxVariation", -1E-12, 0.0101, 409],
    ["W090_CenterColorDifference", -1E-12, 0.0101, 410],

    ["R255_CenterColor(Cx)", 0.6352, 0.6988, 801],
    ["R255_CenterColor(Cy)", 0.3002, 0.3638, 802],
    ["R255_CenterLv", 20.8, 35.2, 803],
    ["R255_MinLv", 19.29, 38.66, 804],
    ["R255_MaxLv", 19.29, 38.66, 805],
    ["R255_MLOGlobalLvMaxVariation", -1E-12, 32.87, 806],
    ["R255_MLOLocalLvMaxVariation", -1E-12, 13.57, 807],
    ["R255_MLOGlobalColorMaxVariation", -1E-12, 0.0166, 808],
    ["R255_MLOLocalColorMaxVariation", -1E-12, 0.0222, 809],
    ["R255_Centeru_prime", 0.4362, 0.5018, 810],
    ["R255_Centerv_prime", 0.5112, 0.5438, 811],

    ["G255_CenterColor(Cx)", 0.1832, 0.2868, 901],
    ["G255_CenterColor(Cy)", 0.6662, 0.7698, 902],
    ["G255_CenterLv", 50.14, 78.52, 903],
    ["G255_MinLv", 42.44, 87.07, 904],
    ["G255_MaxLv", 42.44, 87.07, 905],
    ["G255_MLOGlobalLvMaxVariation", -1E-12, 33.72, 906],
    ["G255_MLOLocalLvMaxVariation", -1E-12, 13.36, 907],
    ["G255_MLOGlobalColorMaxVariation", -1E-12, 0.0111, 908],
    ["G255_MLOLocalColorMaxVariation", -1E-12, 0.0520, 909],
    ["G255_Centeru_prime", 0.0582, 0.1058, 910],
    ["G255_Centerv_prime", 0.5672, 0.5888, 911],

    ["B255_CenterColor(Cx)", 0.0982, 0.5818, 1001],
    ["B255_CenterColor(Cy)", 0.0032, 0.2868, 1002],
    ["B255_CenterLv", 4.50, 14.78, 1003],
    ["B255_MinLv", 4.24, 16.33, 1004],
    ["B255_MaxLv", 4.24, 16.33, 1005],
    ["B255_MLOGlobalLvMaxVariation", -1E-12, 32.87, 1006],
    ["B255_MLOLocalLvMaxVariation", -1E-12, 18.45, 1007],
    ["B255_MLOGlobalColorMaxVariation", -1E-12, 0.2610, 1008],
    ["B255_MLOLocalColorMaxVariation", -1E-12, 0.0902, 1009],
    ["B255_Centeru_prime", 0.1002, 0.4038, 1010],
    ["B255_Centerv_prime", 0.0722, 0.4378, 1011],

    ["DISPLAY_GAMMA", 1.9, 2.3, 3000],
]
global STATION_LIMITS

STATION_LIMITS = []
# turn the above array of arrays into
# a dictionary of arrays for ease of typing
for station_limit in STATION_LIMITS_ARRAYS:
    STATION_LIMITS.append(dict(zip(['name', 'low_limit', 'high_limit', 'unique_id'], station_limit)))
