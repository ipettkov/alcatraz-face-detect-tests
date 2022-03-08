from libs.face_detect import face_detect
from libs.test_data.test_data import pictures_mixed, pictures_black_n_white, non_human_pics


class TestFaceDetectTests:
    def test_mixed_pictures(self):
        assert self.success_rate(pictures_mixed) > 90

    def test_black_and_white(self):
        assert self.success_rate(pictures_black_n_white) >= 50

    def test_non_human(self):
        assert self.success_rate(non_human_pics) >= 90

    def success_rate(self, pictures_set):
        success = 0
        fail = 0
        pics_failed = []
        pics_succeeded = []

        for pic, faces in pictures_set.items():
            faces_returned = face_detect(pic)
            if faces_returned == faces:
                success += 1
                pics_succeeded.append((pic, faces_returned))
            else:
                fail += 1
                pics_failed.append((pic, faces_returned))

        success_rate = (success / len(pictures_set)) * 100
        print("Success rate of function with provided data is {} %".format(success_rate))

        return success_rate

