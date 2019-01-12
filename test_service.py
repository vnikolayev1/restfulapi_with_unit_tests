import unittest
import service

class AppTestMethods(unittest.TestCase):
    
    def test_multiply_calc_check(self):
        self.assertEqual(service.mul(5, 2), 25)
        self.assertEqual(service.mul(-5, -2), 0.04)
        self.assertEqual(service.mul(-5, 2), 25)
        self.assertEqual(service.mul(5, -2), 0.04)
        self.assertEqual(service.mul(5, 0.5), 2.24)
        self.assertEqual(service.mul(0.5, 2), 0.25)
        self.assertEqual(service.mul(5, 0), 1)
        self.assertEqual(service.mul(0, 5), 0)
        self.assertEqual(service.mul(99, 154), 2.12725703229019e+307)

    def test_grouping_words(self):
        #  sorting more than 4-letter words as it supposed to
        self.assertEqual(service.group_words(["word", "lord", "master", "keys", "foot", "loot"]),
                                     [["word", "lord"], ["foot", "loot"], ["master"], ["keys"]])
        #  sorting small words without grouping
        self.assertEqual(service.group_words(["a", "b", "abc", "ab", "abc"]),
                                     [["b"], ["abc"], ["abc"], ["ab"], ["a"]])
        #  sorting combo
        self.assertEqual(service.group_words(["word", "lord", "master", "keys", "foot",
                                         "keys", "loot", "a", "b", "abc", "ab", "abc"]),
                                     [["word", "lord"], ["keys", "keys"], ["foot", "loot"],
                                      ["master"], ["b"], ["abc"], ["abc"], ["ab"], ["a"]])
    
    def test_serializing_words(self):
        self.assertEqual(service.seri("hello -> brave -> new world"), "{'hello':{'brave':{'new world':''}}}")
        self.assertEqual(service.seri("hello    -> br   ave -> new world"), "{'hello':{'br   ave':{'new world':''}}}")
        self.assertEqual(service.seri("hello > brave - new world"), "{'hello > brave - new world':''}")


if __name__ == "__main__":
    unittest.main()