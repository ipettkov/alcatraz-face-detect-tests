import os

path = os.getcwd() + '/test_data/'

pictures_mixed = {
    path + '1_bearded_tribal_man.jpeg': 1,
    path + '1_woman_on_focus_mask.jpeg': 1,
    path + '3_multicultural_women_webp_format.webp': 3,
    path + '5_people_with_frames_around_faces.jpg': 5,
    path + '18_various_ppl.jpeg': 18,
    path + 'abba.png': 4,
    path + 'animated_people_6.png': 0,
    path + 'dogs_2.jpeg': 0,
    path + 'macaque_monkeys_2.jpeg': 0,
    path + 'nature_0.jpeg': 0
}

path_b_w = os.getcwd() + '/libs/test_data/black_and_white_human/'

pictures_black_n_white = {
    path_b_w + '1_gettyimagess.jpeg': 1,
    path_b_w + '3_brown-family.jpeg': 3,
    path_b_w + '8_GettyImages.jpg': 8,
    path_b_w + 'abba.png': 4
}

path_n_h = os.getcwd() + '/libs/test_data/non_human/'
non_human_pics = {
    path_n_h + 'dogs_2.jpeg': 0,
    path_n_h + 'foxish_thing.jpeg': 0,
    path_n_h + 'macaque_monkeys_2.jpeg': 0,
    path_n_h + 'monkeys.jpeg': 0,
    path_n_h + 'zebra.jpeg': 0
}
